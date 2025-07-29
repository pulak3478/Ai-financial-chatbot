from vector_store import VectorSearch


class Chatbot:
    def __init__(self):
        self.vs = VectorSearch()
        self.vs.build_index("data/policy.json")
        self.chat_history = []

    def answer(self, query):
        context = self.vs.search(query, top_k=3)
        self.chat_history.append({"user": query})

        # Simple response using first result
        answer = context[0]["content"]
        source = context[0]["source"]

        self.chat_history.append({"bot": answer})

        return f"📘 **Answer**: {answer}\n\n📌 *Source: {source}*"
