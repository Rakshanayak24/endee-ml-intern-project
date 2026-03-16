from endee import Client
from sentence_transformers import SentenceTransformer

client = Client(api_key="YOUR_ENDEE_API_KEY")
collection = client.get_collection("faq_collection")

model = SentenceTransformer('all-MiniLM-L6-v2')

def rag_query(query, top_k=3):
    query_vec = model.encode(query).tolist()
    results = collection.query(vector=query_vec, top_k=top_k)
    
    print(f"\nQuery: {query}\n")
    for i, r in enumerate(results):
        print(f"Rank {i+1}:")
        print(f"Q: {r.metadata['question']}")
        print(f"A: {r.metadata['answer']}")
        print("-"*50)

if __name__ == "__main__":
    rag_query("How can I use Endee for AI?")
