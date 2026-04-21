import redis
import numpy as np
import google.generativeai as genai
from pinecone import Pinecone

# Connexion Pinecone pour récupérer les métadonnées
pc = Pinecone(api_key="pcsk_5NpWkA_56YP3LDHoXRbnWE9ZkQnLRPvG7mMaffYe1MmzRaNpWNDCUrqYFNg1j7tJ8YHawv")
index = pc.Index(host="https://api-discovery-yaclsn0.svc.aped-4627-b74a.pinecone.io")

# Connexion Gemini
genai.configure(api_key="TA_CLE_GEMINI_PRO")

# Connexion Redis Cloud
r = redis.Redis(
    host="redis-13110.c256.us-east-1-2.ec2.cloud.redislabs.com",
    port=13110,
    password="2w3vsmNhw9xrDeOaEn3785ouKqRQXQdW",
    decode_responses=False,
    ssl=False
)

# Créer l'index avec 3072 dims
try:
    r.execute_command(
        "FT.CREATE", "idx:apis",
        "ON", "HASH",
        "PREFIX", "1", "api:",
        "SCHEMA",
        "name", "TEXT",
        "description", "TEXT",
        "team", "TEXT",
        "endpoints", "TEXT",
        "content_vector", "VECTOR", "FLAT", "6",
        "TYPE", "FLOAT32",
        "DIM", "3072",
        "DISTANCE_METRIC", "COSINE"
    )
    print("Index créé")
except Exception as e:
    print(f"Index existe déjà : {e}")

# Récupérer métadonnées depuis Pinecone
ids = [
    "order-api", "inventory-api", "auth-api", "user-api",
    "search-api", "cart-api", "pricing-api", "shipping-api",
    "review-api", "analytics-api", "webhook-api"
]

result = index.fetch(ids=ids)

# Regénérer embeddings avec Gemini et insérer dans Redis
for id, vector in result.vectors.items():
    text = f"{vector.metadata.get('name', '')}. {vector.metadata.get('description', '')}. Team: {vector.metadata.get('team', '')}. Endpoints: {vector.metadata.get('endpoints', '')}"
    
    # Générer embedding avec Gemini
    response = genai.embed_content(
        model="models/text-embedding-004",
        content=text
    )
    embedding = np.array(response['embedding'], dtype=np.float32).tobytes()
    
    r.hset(f"api:{id}", mapping={
        "name": vector.metadata.get("name", id),
        "description": vector.metadata.get("description", ""),
        "team": vector.metadata.get("team", ""),
        "endpoints": vector.metadata.get("endpoints", ""),
        "content_vector": embedding
    })
    print(f"✅ {id} migré avec Gemini embeddings")

print("Migration terminée !")