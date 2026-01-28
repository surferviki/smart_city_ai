import os
import requests

HF_API_KEY = os.getenv("HF_API_KEY")

EMBEDDING_URL = (
    "https://api-inference.huggingface.co/"
    "pipeline/feature-extraction/"
    "sentence-transformers/all-MiniLM-L6-v2"
)

HEADERS = {
    "Authorization": f"Bearer {HF_API_KEY}"
}

def get_embedding(text: str):
    response = requests.post(
        EMBEDDING_URL,
        headers=HEADERS,
        json={"inputs": text}
    )
    response.raise_for_status()
    return response.json()[0]
