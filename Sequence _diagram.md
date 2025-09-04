```mermaid
%%{init: {'theme': 'default'}}%%
sequenceDiagram
    participant U as User
    participant M as main.py
    participant F as flow.py (LangGraph)
    participant G as guardrails.py
    participant N as nodes.py
    participant DB as SQLite DB
    participant V as FAQ Vector DB
    participant L as Groq LLM

    U->>M: Enter query
    M->>F: app.invoke({"input": query})

    F->>G: guardrail_node(state)
    G-->>F: route = "faq" | "chitchat" | "harmful"

    alt FAQ Route
        F->>N: faq_node(state)
        N->>V: similarity_search(query)
        V-->>N: best FAQ match
        N->>DB: save_message(user, answer)
        N-->>F: response
        F-->>M: response
        M-->>U: Display bot response
    else Chitchat Route
        F->>N: chitchat_node(state)
        N->>DB: load_recent_history(limit=5)
        DB-->>N: past messages
        N->>L: invoke(messages + query)
        L-->>N: generated response
        N->>DB: save_message(user, response)
        N-->>F: response
        F-->>M: response
        M-->>U: Display bot response
    else Harmful Route
        F->>N: escalation_node(state)
        N->>DB: save_message(user, escalation msg)
        N-->>F: escalation msg
        F-->>M: escalation msg
        M-->>U: Display bot response
    end
