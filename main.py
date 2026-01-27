from fastapi import FastAPI
from weather import get_weather
from ai_brain import ask_ai
from restaurant import search_restaurants

app = FastAPI()

@app.get("/")
def home():
    return {"message": "🌆 Smart City Explorer AI for Chennai is running!"}

@app.get("/ask")
def ask(question: str):
    q = question.lower()
    weather_keywords = ["weather", "temperature", "rain"]
    restaurant_keywords = ["restaurant", "food", "eat"]

    wants_weather = any(k in q for k in weather_keywords)
    wants_restaurant = any(k in q for k in restaurant_keywords)

    answer_parts = []

    if wants_weather:
        answer_parts.append(get_weather("Chennai"))

    if wants_restaurant:
        answer_parts.append(search_restaurants(question))

    if not answer_parts:
        answer_parts.append(ask_ai(question))

    answer = "\n\n".join(answer_parts)
    return {"question": question, "answer": answer}
