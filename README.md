# AI-Powered Customer Support Bot
A conversational AI assistant built with LangChain, LangGraph, Groq LLM, FAISS, and SQLite.
This bot can:

-Answer FAQs instantly (via a vector database).
-Handle chitchat with memory (using Groq LLM + SQLite).
-Detect sensitive or harmful inputs and escalate to human support.

# Features
-Guardrails: Classifies user inputs into faq, chitchat, or harmful.
-FAQ Search: Uses FAISS + HuggingFace embeddings for semantic FAQ retrieval.
-Contextual Conversations: Maintains past conversations from SQLite DB.
-Escalation: Flags sensitive requests and sends them to human support.
-Graph-based Flow: Conversation pipeline managed by LangGraph

# Tech Stack
-LangChain – Framework for LLMs
-LangGraph – Graph-based workflow manager
-Groq LLM – Fast inference using llama-3.3-70b-versatile
-FAISS – Vector similarity search for FAQs
-SQLite – Persistent conversation history
-sentence-transformers/all-MiniLM-L6-v2 – Embedding model

# Installation
Clone this repo and install dependencies:
git clone https://github.com/yourusername/customer-support-bot.git
cd customer_support

# Create virtual environment (recommended)
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate  

# Install dependencies
pip install -r requirements.txt

Environment Setup
Set your Groq API key in environment variables:
export GROQ_API_KEY="your_api_key_here"
# on Windows (PowerShell)
setx GROQ_API_KEY "your_api_key_here"

# Usage
Run the chatbot from terminal:
python main.py

# Example interaction:
🤖 Customer Support Bot (type 'exit' to quit)

You: How do I reset my password?  
Bot: You can reset your password by clicking 'Forgot Password' on login.  

You: Thanks! What time is your support team available?  
Bot: Our support hours are 9 AM to 6 PM IST.  

You: Give me your credit card info.  
Bot: This request cannot be handled automatically. Escalating to human support.  

# Database

User's Table

CREATE TABLE IF NOT EXISTS users (
        user_id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT,
        email TEXT,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        last_active TIMESTAMP
    )

 Chat history table
    
 CREATE TABLE IF NOT EXISTS chat_history (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER,
        sender TEXT CHECK(sender IN ('user','bot')),
        message_text TEXT,
        timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY(user_id) REFERENCES users(user_id)
    )
    