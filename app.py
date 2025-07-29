from chatbot import Chatbot

def main():
    print("🧧 Welcome to the Financial Policy Chatbot!")
    print("Type your question below. Type 'exit' to quit.\n")

    bot = Chatbot()

    while True:
        query = input("You: ")
        if query.lower() in ("exit", "quit"):
            break
        response = bot.answer(query)
        print(response + "\n")


if __name__ == "__main__":
    main()
