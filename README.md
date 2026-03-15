# Workshop 1: Cloud Tutor — Gemini 2.5 Flash via LiteLLM

A conversational AI tutor powered by Google's Gemini 2.5 Flash through Google AI Studio's free tier. Same architecture as Lab 4, different model provider.

## Setup

```bash
# Clone and enter the repo
git clone <your-repo-url>
cd workshop1-cloud-tutor

# Create environment
conda create -n workshop1 python=3.11 -y
conda activate workshop1
pip install -r requirements.txt

# Configure your API key
cp .env.example .env
# Edit .env and paste your key from aistudio.google.com

# Test the connection
python chat_cli.py

# Run the web app
python app.py
```

Open http://127.0.0.1:5000 in your browser.

## API Key Security

- **NEVER** commit `.env` to Git — it's in `.gitignore` for a reason
- Run `git status` before every commit — if `.env` appears, stop
- If you accidentally commit a key: revoke it at aistudio.google.com immediately

## Swapping Models

Change the `MODEL` variable in `app.py`:

| Provider         | Model string                          |
|------------------|---------------------------------------|
| Google AI Studio | `"gemini/gemini-2.5-flash"`           |
| Ollama (local)   | `"ollama/llama3.2"`                   |
| OpenAI           | `"gpt-4o-mini"`                       |
| Anthropic        | `"anthropic/claude-sonnet-4-20250514"`|
