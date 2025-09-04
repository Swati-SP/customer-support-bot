from database import save_message, load_recent_history
from faq_store import vectorstore
from config import chat

def faq_node(state):
    user_id = state.get("user_id", 1)  # default to 1 if not provided

    docs = vectorstore.similarity_search(state["input"], k=1)
    response = docs[0].page_content if docs else "I couldn't find an exact match in our FAQs."
    
    state["response"] = response

    # Save user and bot messages
    save_message(user_id, "user", state["input"])
    save_message(user_id, "bot", response)

    return state


def chitchat_node(state):
    user_id = state.get("user_id", 1)  # default to 1 if not provided

    # Load last 5 exchanges from DB
    history_messages = load_recent_history(user_id, limit=5)
    history_messages.append({"role": "user", "content": state["input"]})

    # LLM response
    response = chat.invoke(history_messages).content
    state["response"] = response

    # Save user and bot messages
    save_message(user_id, "user", state["input"])
    save_message(user_id, "bot", response)

    return state


def escalation_node(state):
    user_id = state.get("user_id", 1)  # default to 1 if not provided

    response = "This request cannot be handled automatically. Escalating to human support."
    state["response"] = response

    save_message(user_id, "user", state["input"])
    save_message(user_id, "bot", response)

    return state
