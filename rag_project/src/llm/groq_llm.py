from langchain_groq import ChatGroq
from rag_project.config.settings import settings

def get_llm():
    """
    Initialize and return the Groq LLM model.
    """
    return ChatGroq(groq_api_key=settings.GROQ_API_KEY, model_name="llama3-8b-8192")