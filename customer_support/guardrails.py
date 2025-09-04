def classify_input(user_query: str) -> str:
    """Return route: 'harmful', 'faq', 'chitchat'"""
    sensitive_keywords = ["kill", "suicide", "credit card", "ssn"]
    if any(word in user_query.lower() for word in sensitive_keywords):
        return "harmful"
    elif "password" in user_query.lower() or "support" in user_query.lower() or "hours" in user_query.lower():
        return "faq"
    else:
        return "chitchat"

def guardrail_node(state):
    route = classify_input(state["input"])
    state["route"] = route
    return state
