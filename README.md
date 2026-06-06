# 🤖 GenAI Summer of Code 2026

> A hands-on learning journey through Generative AI — building real projects week by week as part of the MSTC GenAI SOC 2026 programme.

---

## 👨‍💻 About Me

| | |
|---|---|
| **Name** | Tirth Kheni |
| **College** | DA-IICT, Gandhinagar |
| **Year** | First Year B.Tech ICT |
| **GitHub** | [@tirthkheni09-collab](https://github.com/tirthkheni09-collab) |

---

## 📌 What is this repo?

This repository contains all my weekly projects, experiments, and learnings from the **MSTC GenAI SOC 2026** programme. Each week I build a real AI-powered project from scratch — starting from environment setup all the way to deploying working applications.

The goal is simple: **learn by building.**

---

## 🗺️ Programme Roadmap

| Week | Project | Status | Key Concepts |
|------|---------|--------|--------------|
| Week 0 | Environment Setup | ✅ Complete | Python, venv, dotenv, Git, Groq API |
| Week 1 | PromptForge | ✅ Complete | System prompts, personas, Gradio, streaming |
| Week 2 | Coming Soon | ⬜ Upcoming | TBA |
| Week 3 | Coming Soon | ⬜ Upcoming | TBA |

---

## 🚀 Projects

### ✅ Week 0 — Environment Setup
Setting up the complete development environment for AI development.

**What I did:**
- Installed Python 3.10+ and VS Code
- Created and managed virtual environments
- Learned the `.env` file pattern for storing API keys safely
- Set up Git and GitHub for version control
- Made my first ever Groq API call using LLaMA 3.3 70B
- Verified Google Colab works for cloud notebooks

**Key learning:** Never push API keys to GitHub — always use `.gitignore` and `.env` files.

---

### ✅ Week 1 — PromptForge
A multi-persona AI chat application that demonstrates the power of prompt engineering.

**What I built:**
A web app with 4 completely different AI personas — all powered by the same LLaMA model, but behaving differently based on their system prompts.

| Persona | What it does |
|---------|-------------|
| 🧠 Technical Explainer | Explains complex concepts simply using analogies |
| ⚖️ Debate Coach | Gives balanced FOR and AGAINST arguments on any topic |
| 🔍 Code Reviewer | Reviews code and returns structured JSON feedback |
| ✍️ Creative Writer | Responds with vivid, sensory-rich creative writing |

**Key learnings:**
- System prompts completely change how an AI responds
- Few-shot examples guide the model's output style
- Streaming responses make apps feel faster and more alive
- Gradio makes building AI web UIs incredibly fast
- LLMs can return structured JSON when prompted correctly

**Tech stack:** Python · Groq API · LLaMA 3.3 70B · Gradio · python-dotenv

📁 [View Week 1 code](./week1-promptforge/)

---

## 🛠️ Tech Stack

| Tool | Purpose |
|------|---------|
| Python 3.10+ | Core language |
| Groq API | Fast LLM inference |
| LLaMA 3.3 70B | The AI model |
| Gradio | Web UI for AI apps |
| python-dotenv | Secure API key management |
| Git & GitHub | Version control |
| Google Colab | Cloud notebooks |

---

## 📁 Repository Structure
genai-soc-2026/
│
├── 📄 README.md                  ← You are here
├── 🐍 hello_ai.py                ← First Groq API call (Week 0)
├── 🔒 .gitignore                 ← Keeps secrets safe
│
└── 📁 week1-promptforge/         ← Week 1 Project
├── 📄 README.md
├── 🐍 app.py                 ← Main Gradio app
├── 📋 requirements.txt
└── 🔒 .gitignore
---

## ⚙️ How to Run Any Project

```bash
# Clone the repo
git clone https://github.com/tirthkheni09-collab/genai-soc-2026.git
cd genai-soc-2026

# Go to a specific week
cd week1-promptforge

# Create and activate virtual environment
python -m venv venv
venv\Scripts\activate        # Windows
source venv/bin/activate     # Mac/Linux

# Install dependencies
pip install -r requirements.txt

# Add your API key
# Create a .env file and add: GROQ_API_KEY=your_key_here

# Run the app
python app.py
```

---

## 🔑 API Keys & Security

All API keys are stored in local `.env` files and are **never pushed to GitHub**. If you clone this repo, you will need to create your own `.env` file with your own Groq API key from [console.groq.com](https://console.groq.com).

---

## 📬 Connect with Me

- 🔗 LinkedIn: [Tirth Kheni](https://in/tirth-kheni-2a59ba370)
- 🐦 Twitter/X: [@tirth_kheni_06](https://x.com/tirth_kheni_06)
- 💻 GitHub: [@tirthkheni09-collab](https://github.com/tirthkheni09-collab)
