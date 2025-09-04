import os
from langchain_groq import ChatGroq

# Load API Key
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
if not GROQ_API_KEY:
    raise ValueError("Please set the GROQ_API_KEY environment variable.")

# Initialize Groq LLM
chat = ChatGroq(
    groq_api_key=GROQ_API_KEY,
    model="llama-3.3-70b-versatile"
)

# Database file
DB_FILE = "chatbot.db"
