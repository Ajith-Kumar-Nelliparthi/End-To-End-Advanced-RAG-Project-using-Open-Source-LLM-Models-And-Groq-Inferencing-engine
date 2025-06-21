from langchain.embeddings import HuggingFaceEmbeddings
import torch 
from config.settings import settings

def get_embeddings():
    """
    Initialize and return the HuggingFace embeddings model.
    """
    # Check if GPU is available and set device accordingly
    device = "cuda" if torch.cuda.is_available() else "cpu"
    
    # Initialize the HuggingFace embeddings model with the specified model name and device
    embeddings = HuggingFaceEmbeddings(
        model_name=settings.EMBED_MODEL,
        model_kwargs={"device": device},
        encode_kwargs={"normalize_embeddings": True}  # Normalize embeddings to unit length
    )
    
    return embeddings