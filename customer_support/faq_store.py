from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings
from langchain.docstore.document import Document

# Sample FAQs
faqs = [
    Document(page_content="You can reset your password by clicking 'Forgot Password' on login."),
    Document(page_content="Our support hours are 9 AM to 6 PM IST."),
    Document(page_content="To contact support, email us at support@example.com."),
]

# Embeddings + Vector Store
embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
vectorstore = FAISS.from_documents(faqs, embeddings)
