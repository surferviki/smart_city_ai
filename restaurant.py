import os
from chromadb.utils import embedding_functions
import chromadb

# Initialize ChromaDB client (in-memory for free usage)
client = chromadb.Client()
collection = client.create_collection("restaurants")

# Embedding function using sentence-transformers
embed_fn = embedding_functions.SentenceTransformerEmbeddingFunction(
    model_name="all-MiniLM-L6-v2"
)

# Sample restaurant data (can expand later)
restaurants_data = [
    {
        "name": "Sunny Veggie",
        "type": "Vegetarian",
        "location": "Marina Beach",
        "review": "Great outdoor seating, fresh food",
    },
    {
        "name": "Beachside Bites",
        "type": "Fast Food",
        "location": "Besant Nagar",
        "review": "Quick service, nice ambiance",
    },
    {
        "name": "Spice Delight",
        "type": "Indian",
        "location": "Chennai Central",
        "review": "Delicious traditional meals",
    },
]

# Add to vector database
for r in restaurants_data:
    text = f"{r['name']} | {r['type']} | {r['location']} | {r['review']}"
    collection.add(
        documents=[text],
        metadatas=r,
        ids=[r["name"]],
        embeddings=[embed_fn(text)]
    )

# Function to search restaurants
def search_restaurants(query: str, top_k=3):
    # Create embedding for query
    query_emb = embed_fn(query)
    results = collection.query(
        query_embeddings=[query_emb],
        n_results=top_k
    )
    
    # Build human-readable answer
    answer = "Here are some restaurant suggestions:\n"
    for i, metadata in enumerate(results["metadatas"][0]):
        answer += f"{i+1}. {metadata['name']} ({metadata['type']}) - {metadata['location']}\n"
    return answer
