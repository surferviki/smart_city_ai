from fastapi import FastAPI
from vectorstore import search_restaurants, seed_restaurants

app = FastAPI()

# Seed once at startup
seed_restaurants()

@app.get("/ask")
def ask(question: str):
    results = search_restaurants(question)
    return {
        "question": question,
        "results": results
    }
