from endee import Client
from sentence_transformers import SentenceTransformer
import pandas as pd

# Load data
df = pd.read_csv("../data/faq_data.csv")

# Initialize Endee client (add YOUR API key)
client = Client(api_key="YOUR_ENDEE_API_KEY")

# Load embedding model
model = SentenceTransformer('all-MiniLM-L6-v2')

# Create collection
collection = client.create_collection("faq_collection")

# Add embeddings
for idx, row in df.iterrows():
    vector = model.encode(row['question']).tolist()
    collection.add_item(
        id=str(idx),
        vector=vector,
        metadata={"question": row['question'], "answer": row['answer']}
    )

print("✅ Embeddings added to Endee!")
