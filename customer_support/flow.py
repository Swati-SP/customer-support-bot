from langgraph.graph import StateGraph, END
from guardrails import guardrail_node
from nodes import faq_node, chitchat_node, escalation_node

# Build LangGraph Flow
graph = StateGraph(dict)

graph.add_node("guardrail", guardrail_node)
graph.add_node("faq", faq_node)
graph.add_node("chitchat", chitchat_node)
graph.add_node("escalation", escalation_node)

# Conditional routing
graph.add_conditional_edges(
    "guardrail",
    lambda state: state["route"],
    {
        "faq": "faq",
        "chitchat": "chitchat",
        "harmful": "escalation",
    },
)

graph.set_entry_point("guardrail")
graph.add_edge("faq", END)
graph.add_edge("chitchat", END)
graph.add_edge("escalation", END)

# Compile
app = graph.compile()
