from vector_store import VectorSearch

class Chatbot:
    def __init__(self):
        self.vs = VectorSearch()
        self.vs.build_index("data/policy.json")
        self.chat_history = []
        self.last_topic = ""

    def is_follow_up(self, query: str) -> bool:
        vague_starts = ["what about", "and", "more on", "it", "that", "tell me more", "can you elaborate"]
        return any(query.lower().startswith(v) for v in vague_starts) or len(query.split()) < 4

    def answer(self, query: str) -> str:
        if self.is_follow_up(query) and self.last_topic:
            full_query = f"{self.last_topic} {query}"
        else:
            full_query = query
            self.last_topic = query

        context = self.vs.search(full_query, top_k=3)

        self.chat_history.append({"user": query})
        answer = context[0]["content"]
        source = context[0]["source"]
        self.chat_history.append({"bot": answer})

        return f"📘 **Answer**: {answer}\n\n📌 *Source: {source}*"
