from flow import app
from database import init_db

def run_chatbot():
    print("🤖 Customer Support Bot (type 'exit' to quit)\n")

    # Initialize database
    init_db()

    # For now, use demo user
    user_id = 1  

    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit"]:
            print("Bot: Goodbye! 👋")
            break

        result = app.invoke({
            "user_id": user_id,
            "input": user_input
        })
        print("Bot:", result["response"])

if __name__ == "__main__":
    run_chatbot()
