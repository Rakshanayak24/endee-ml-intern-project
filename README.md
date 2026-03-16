# Endee Semantic Search & RAG QA System
🚀 **This project demonstrates a real-world AI workflow using Endee for semantic search and RAG. Fully reproducible, modular, and ready for production-level AI retrieval systems.**
## 🔍 Overview
This project demonstrates a **semantic search and Retrieval-Augmented Generation (RAG) system** using the Endee vector database.  
It allows users to ask natural language questions and retrieves the most relevant answers from a dataset of FAQs/articles using **embeddings** and **vector search**.

---

## 🧠 Features
- Convert questions into embeddings using `sentence-transformers`
- Store embeddings with metadata in Endee
- Perform semantic search to retrieve top-K similar questions
- RAG-style query interface ready for AI applications
- Modular and easy to extend for larger datasets or other AI workflows

---

## ⚙️ System Design
1. **Data Preparation**  
   Store questions and answers in `data/faq_data.csv`.
2. **Embedding Creation**  
   Use `sentence-transformers` to generate vector embeddings for each question.
3. **Storage in Endee**  
   Add embeddings + metadata to an Endee collection.
4. **Query System**  
   Convert user query to embedding → retrieve top-K similar items from Endee → display results.

---
## 📁 Project Structure
```bash
data/faq_data.csv         # Dataset of questions and answers
src/create_embeddings.py  # Script to create embeddings and store in Endee
src/search_query.py       # Script to query Endee and display top results
requirements.txt          # Python dependencies
README.md                 # Project documentation
```

## 🚀 Quick Start

1. **Install dependencies**
```bash
pip install -r requirements.txt
```

2. **Add your Endee API key**
Replace "YOUR_ENDEE_API_KEY" in both scripts:
```bash
src/create_embeddings.py
src/search_query.py
```
3. **Create embeddings**
```bash
python src/create_embeddings.py
Run a semantic query
python src/search_query.py
```
## 💡 Example Query
```bash

Input:

How can I use Endee for AI?

Output:

Rank 1:
Q: What is Endee?
A: Endee is a vector database for AI-powered semantic search.
--------------------------------------------------
Rank 2:
Q: What can Endee be used for?
A: Semantic search, RAG QA, and recommendation workflows.
--------------------------------------------------
Rank 3:
Q: How to query Endee?
A: Convert your query to an embedding and use the Endee query API.
--------------------------------------------------
```
