# 🤖 AI-Powered Financial Policy Chatbot

This project is a submission for the **AI Developer Assessment**, where the goal is to build a simple AI chatbot that can answer questions from a government **financial policy document**.

The chatbot extracts and indexes information from the document, allowing users to query it using natural language and receive smart, context-aware answers — including follow-up questions like "What about debt?"

---

## 📄 Project Features

✅ Extracts structured information from a PDF  
✅ Embeds content using **SentenceTransformers**  
✅ Performs fast and accurate semantic search using **FAISS**  
✅ Answers questions with **relevant source reference (page number)**  
✅ Tracks conversation context to handle **follow-up queries**  
✅ Lightweight and runs **fully locally**

---

## Technologies Used

- **Python 3**
- [Sentence-Transformers](https://www.sbert.net/) – for text embeddings
- [FAISS](https://github.com/facebookresearch/faiss) – for vector similarity search
- **PyMuPDF (fitz)** – for parsing PDF documents
- **Standard Python CLI** – for chat interaction

---

## 🛠️ How It Works

1. **Document Parsing**: The PDF is split into small meaningful chunks (by paragraph or line) and stored in a JSON file.
2. **Embedding + Indexing**: Chunks are embedded into vectors using a pre-trained transformer model (`all-MiniLM-L6-v2`), and stored in FAISS for fast retrieval.
3. **Chatbot with Memory**: The chatbot keeps track of the last query. If a user asks something vague like "What about debt?", it combines it with the previous question to maintain context.
4. **Semantic Search**: For each query, the top matching chunks are fetched from the index and returned with the source page number.

---
## Requirements

- Python 3.8+
- sentence-transformers
- faiss or chromadb
- openai or huggingface transformers
- numpy
- faiss-cpu/gpu
- sentence-transformers
- PyMuPDF

## 🚀 How to Run

### 1. Clone this repo

- ```bash
- git clone https://github.com/your-username/Ai-financial-chatbot.git
- cd Ai-financial-chatbot
