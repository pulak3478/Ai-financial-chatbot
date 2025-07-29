import json
import faiss
import numpy as np
from sentence_transformers import SentenceTransformer


class VectorSearch:
    def __init__(self, model_name="all-MiniLM-L6-v2"):
        self.model = SentenceTransformer(model_name)
        self.index = None
        self.texts = []
        self.metadata = []

    def build_index(self, data_path):
        with open(data_path, "r", encoding="utf-8") as f:
            records = json.load(f)

        embeddings = self.model.encode([r["content"] for r in records])
        self.index = faiss.IndexFlatL2(embeddings[0].shape[0])
        self.index.add(np.array(embeddings))

        self.texts = [r["content"] for r in records]
        self.metadata = [r["source"] for r in records]

    def search(self, query, top_k=3):
        query_embedding = self.model.encode([query])
        distances, indices = self.index.search(np.array(query_embedding), top_k)

        results = []
        for idx in indices[0]:
            results.append({
                "content": self.texts[idx],
                "source": self.metadata[idx]
            })
        return results
