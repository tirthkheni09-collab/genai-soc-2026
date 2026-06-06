# 🔧 PromptForge — Multi-Mode AI Assistant

A multi-persona AI chat app built with Gradio and Groq API as part of GenAI SOC 2026 Week 1.

## What it does
- Switch between 4 AI personas in real time
- **Technical Explainer** — explains concepts simply with analogies
- **Debate Coach** — gives balanced FOR and AGAINST arguments
- **Code Reviewer** — reviews code and returns structured JSON feedback
- **Creative Writer** — responds with rich, vivid creative writing

## How system prompts work
Each persona has a different system prompt that completely changes
how the AI responds to the same question. This shows the power of
prompt engineering.

## Tech Stack
- Python 3.10+
- Groq API (LLaMA 3.3 70B)
- Gradio 6.x
- python-dotenv

## How to run locally
1. Clone the repo
2. cd week1-promptforge
3. python -m venv venv
4. venv\Scripts\activate
5. pip install -r requirements.txt
6. Add your GROQ_API_KEY to a .env file
7. python app.py

## What I learned
- How system prompts change AI behaviour
- Few-shot examples to guide model output
- Streaming responses with Groq API
- Building web UIs with Gradio
- Structured JSON output from LLMs
