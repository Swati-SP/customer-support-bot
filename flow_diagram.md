```mermaid
flowchart TD
    A[User Input] --> B{Guardrail Node}
    B -->|FAQ detected| C[FAQ Node]
    B -->|Chit-Chat detected| D[Chitchat Node]
    B -->|PII/Harmful detected| E[Escalation Node]
    C --> F[DB Save + Response]
    D --> F[DB Save + Response]
    E --> F[DB Save + Response]
    F --> G[Bot Output to User]
