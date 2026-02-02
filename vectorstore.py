from chromadb import Client
from embeddings import get_embedding

client = Client()
collection = client.get_or_create_collection("restaurants")

def seed_restaurants():
    restaurants = [
        "Saravana Bhavan vegetarian South Indian restaurant",
        "Anjappar Chettinad spicy non-veg food",
        "Sangeetha pure veg family restaurant"
    ]

    for i, text in enumerate(restaurants):
        collection.add(
            ids=[str(i)],
            documents=[text],
            embeddings=[get_embedding(text)]
        )

def search_restaurants(query: str):
    results = collection.query(
        query_embeddings=[get_embedding(query)],
        n_results=2
    )
    return results["documents"][0]
