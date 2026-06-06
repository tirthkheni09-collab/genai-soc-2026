import json
import os
import gradio as gr
from groq import Groq
from dotenv import load_dotenv

load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

PERSONAS = {
    "Technical Explainer": {
        "system_prompt": "You are a clear technical explainer. Explain concepts simply, avoid jargon, use analogies. Keep responses under 150 words.",
        "few_shot_examples": [
            {"role": "user", "content": "What is an API?"},
            {"role": "assistant", "content": "An API is a waiter in a restaurant. You tell the waiter what you want, the waiter goes to the kitchen, and brings it back. You never enter the kitchen directly."}
        ],
    },
    "Debate Coach": {
        "system_prompt": "You are a debate coach. For any topic, present both FOR and AGAINST arguments clearly. Label them. Be balanced.",
        "few_shot_examples": [
            {"role": "user", "content": "Should students use AI for homework?"},
            {"role": "assistant", "content": "FOR: AI accelerates learning and prepares students for an AI-integrated workforce.\n\nAGAINST: Over-reliance reduces critical thinking skills."}
        ],
    },
    "Code Reviewer": {
        "system_prompt": "You are a code reviewer. Respond ONLY with valid JSON: {\"issues\": [...], \"suggestions\": [...], \"severity\": \"low|medium|high\"}. No preamble.",
        "few_shot_examples": [
            {"role": "user", "content": "def add(a,b):\n  return a+b"},
            {"role": "assistant", "content": "{\"issues\": [\"No type hints\", \"No docstring\"], \"suggestions\": [\"Add type hints\", \"Add docstring\"], \"severity\": \"low\"}"}
        ],
    },
    "Creative Writer": {
        "system_prompt": "You are a vivid creative writer. Use rich sensory details and strong verbs. Make every response feel alive.",
        "few_shot_examples": [
            {"role": "user", "content": "Describe rain."},
            {"role": "assistant", "content": "The rain didn't fall — it arrived, drumming against the tin roof like impatient fingers."}
        ],
    }
}

def build_messages(persona_name, history, user_message):
    persona = PERSONAS[persona_name]
    messages = [{"role": "system", "content": persona["system_prompt"]}]
    messages.extend(persona["few_shot_examples"])
    for item in history:
        messages.append({"role": item["role"], "content": item["content"]})
    messages.append({"role": "user", "content": user_message})
    return messages

def respond(message, history, persona_name, temperature):
    history = history or []
    messages = build_messages(persona_name, history, message)

    stream = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=messages,
        temperature=temperature,
        max_tokens=500,
        stream=True,
    )

    history = history + [{"role": "user", "content": message}, {"role": "assistant", "content": ""}]
    accumulated = ""
    for chunk in stream:
        delta = chunk.choices[0].delta.content or ""
        accumulated += delta
        history[-1]["content"] = accumulated
        yield "", history


def update_prompt(persona_name):
    return PERSONAS[persona_name]["system_prompt"]

with gr.Blocks(title="PromptForge") as app:
    gr.Markdown("# 🔧 PromptForge — Multi-Mode AI Assistant")
    gr.Markdown("Switch between AI personas and see how system prompts change the behaviour!")

    with gr.Row():
        persona_dropdown = gr.Dropdown(
            choices=list(PERSONAS.keys()),
            value="Technical Explainer",
            label="🎭 Select Persona"
        )
        temp_slider = gr.Slider(
            minimum=0.0, maximum=1.5, value=0.7, step=0.1,
            label="🌡️ Temperature (creativity)"
        )

    with gr.Accordion("📋 Active System Prompt", open=False):
        system_prompt_display = gr.Textbox(
            value=PERSONAS["Technical Explainer"]["system_prompt"],
            label="", interactive=False, lines=3
        )

    chatbot = gr.Chatbot(height=400, label="PromptForge Chat")
    msg_box = gr.Textbox(placeholder="Type your message here...", label="Your message")

    with gr.Row():
        send_btn = gr.Button("Send 🚀", variant="primary")
        clear_btn = gr.Button("Clear Chat 🗑️")

    persona_dropdown.change(update_prompt, persona_dropdown, system_prompt_display)
    send_btn.click(respond, [msg_box, chatbot, persona_dropdown, temp_slider], [msg_box, chatbot])
    msg_box.submit(respond, [msg_box, chatbot, persona_dropdown, temp_slider], [msg_box, chatbot])
    clear_btn.click(lambda: ([], ""), outputs=[chatbot, msg_box])

app.launch(inbrowser=True)