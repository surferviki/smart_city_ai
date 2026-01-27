import os
import requests

HF_API_KEY = os.getenv("HF_API_KEY")
MODEL_URL = "https://api-inference.huggingface.co/models/mistralai/Mistral-7B-Instruct-v0.2"

HEADERS = {
    "Authorization": f"Bearer {HF_API_KEY}",
    "Content-Type": "application/json"
}

def ask_ai(question: str):
    prompt = f"""
You are a helpful Smart City Explorer assistant for Chennai.
Answer the user's question in a friendly, simple way.

User question: {question}
"""

    payload = {
        "inputs": prompt,
        "parameters": {
            "max_new_tokens": 200,
            "temperature": 0.6,
            "top_p": 0.9,
            "do_sample": True
        }
    }

    try:
        response = requests.post(MODEL_URL, headers=HEADERS, json=payload, timeout=30)
        response.raise_for_status()
        result = response.json()

        if isinstance(result, list) and "generated_text" in result[0]:
            return result[0]["generated_text"].strip()
    except Exception as e:
        print("⚠️ AI Error:", e)

    return "Sorry, I’m having trouble thinking right now 😅"

