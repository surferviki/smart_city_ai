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
            print(f"⚠️ Failed to add restaurant {idx}: {e}")
