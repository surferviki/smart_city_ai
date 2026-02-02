import os
import requests

HF_API_KEY = os.getenv("HF_API_KEY")

MODEL_ID = "sentence-transformers/all-MiniLM-L6-v2"
EMBEDDING_URL = f"https://api-inference.huggingface.co/models/{MODEL_ID}"

HEADERS = {
    "Authorization": f"Bearer {HF_API_KEY}",
    "Content-Type": "application/json"
}

def get_embedding(text: str):
    response = requests.post(
        EMBEDDING_URL,
        headers=HEADERS,
        json={"inputs": text}
    )

    response.raise_for_status()

    data = response.json()

    # HF sometimes returns nested lists
    if isinstance(data[0], list):
        return data[0]

    return data
