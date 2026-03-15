"""
chat_cli.py - Test your Gemini connection in the terminal.

Run this FIRST to verify your API key works before starting the web app.
Usage: python chat_cli.py
"""

import os
from dotenv import load_dotenv
from litellm import completion

load_dotenv()

if not os.getenv("GEMINI_API_KEY"):
    print("ERROR: GEMINI_API_KEY not found in .env file.")
    print("1. Copy .env.example to .env")
    print("2. Paste your Google AI Studio API key")
    exit(1)

MODEL = "gemini/gemini-2.5-flash"

def ask_llm(messages):
    """Send messages to the LLM and return its response."""
    response = completion(model=MODEL, messages=messages)
    return response.choices[0].message.content

if __name__ == "__main__":
    print(f"Chat with {MODEL} (type 'quit' to exit)")
    print("-" * 40)

    history = [
        {"role": "system", "content": "You are a helpful assistant. Keep responses brief."}
    ]

    while True:
        user_input = input("\nYou: ")
        if user_input.lower() in ["quit", "exit"]:
            print("Goodbye!")
            break

        history.append({"role": "user", "content": user_input})
        reply = ask_llm(history)
        history.append({"role": "assistant", "content": reply})
        print(f"\nAssistant: {reply}")
