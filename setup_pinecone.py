# setup_pinecone.py
import json
from utils.embeddings import get_embedding
from utils.pinecone_helper import get_index, upsert_data

# Load your JSON food data
with open("data/food_items.json", "r") as f:
    food_data = json.load(f)

index = get_index()
upsert_data(index, food_data, get_embedding)

print("✅ Successfully uploaded food data to Pinecone!")
