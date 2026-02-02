import chromadb
from embeddings import get_embedding

client = chromadb.Client()
collection = client.get_or_create_collection(name="restaurants")

def seed_restaurants():
    restaurants = [
        "Sunny Veggie is a vegetarian restaurant near Marina Beach",
        "Spice Hub serves South Indian food in T Nagar",
        "Ocean Treat offers seafood near Besant Nagar"
    ]

    for idx, text in enumerate(restaurants):
        try:
            collection.add(
                documents=[text],
                embeddings=[get_embedding(text)],
                ids=[str(idx)]
            )
        except Exception as e:
            print(f"⚠️ Failed to seed restaurant {idx}: {e}")

def search_restaurants(query: str):
    query_embedding = get_embedding(query)

    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=2
    )

    return results["documents"][0]
