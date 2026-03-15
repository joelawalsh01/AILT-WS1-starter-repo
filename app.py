"""
app.py - Flask web application for the conversational tutor.

Workshop 1: Uses LiteLLM to call Google's Gemini 2.5 Flash model via Google AI Studio.
"""

import os
from dotenv import load_dotenv
from flask import Flask, render_template, request, jsonify, session
from litellm import completion
from questions import TOPIC, QUESTIONS, SYSTEM_PROMPT

# Load environment variables from .env file
load_dotenv()

# Verify the API key is set
if not os.getenv("GEMINI_API_KEY"):
    print("=" * 50)
    print("ERROR: GEMINI_API_KEY not found!")
    print("1. Copy .env.example to .env")
    print("2. Paste your API key from aistudio.google.com")
    print("=" * 50)
    exit(1)

app = Flask(__name__)
app.secret_key = os.urandom(24)

# Model configuration - change this one string to swap providers
MODEL = "gemini/gemini-2.5-flash"


def get_llm_response(messages):
    """Send the full conversation history to the LLM and return its response."""
    try:
        response = completion(
            model=MODEL,
            messages=messages,
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Error calling the model: {str(e)}"


@app.route("/")
def index():
    """Start a new conversation."""
    session["history"] = [{"role": "system", "content": SYSTEM_PROMPT}]
    return render_template("chat.html", topic=TOPIC, num_questions=len(QUESTIONS))


@app.route("/chat", methods=["POST"])
def chat():
    """Handle a chat message from the student."""
    user_message = request.json.get("message", "").strip()
    if not user_message:
        return jsonify({"error": "Empty message"}), 400

    # Add user message to history
    session["history"].append({"role": "user", "content": user_message})

    # Get LLM response (sends FULL history every time - LLMs are stateless)
    reply = get_llm_response(session["history"])

    # Add assistant response to history
    session["history"].append({"role": "assistant", "content": reply})
    session.modified = True

    return jsonify({"reply": reply})


@app.route("/reset", methods=["POST"])
def reset():
    """Reset the conversation."""
    session["history"] = [{"role": "system", "content": SYSTEM_PROMPT}]
    return jsonify({"status": "ok"})


if __name__ == "__main__":
    print(f"Starting tutor on topic: {TOPIC}")
    print(f"Using model: {MODEL}")
    print(f"Questions loaded: {len(QUESTIONS)}")
    print(f"Open http://127.0.0.1:5000 in your browser")
    app.run(debug=True)
