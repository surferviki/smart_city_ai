from fastapi import FastAPI
from weather import get_weather
from ai_brain import ask_ai

app = FastAPI()

@app.get("/")
def home():
    return {"message": "🌆 Smart City Explorer AI for Chennai is running!"}

@app.get("/ask")
def ask(question: str):
    q = question.lower()

    # Simple rule: if question mentions weather, call weather tool
    if "weather" in q or "temperature" in q or "rain" in q:
        answer = get_weather("Chennai")
    else:
        answer = ask_ai(question)

    return {"question": question, "answer": answer}

