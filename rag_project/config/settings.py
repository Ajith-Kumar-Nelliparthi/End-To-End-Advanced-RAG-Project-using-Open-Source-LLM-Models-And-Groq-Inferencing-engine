import os 
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Define a settings class to hold configuration values
class Settings:
    GROQ_API_KEY=os.getenv("GROQ_API_KEY")
    ASTRA_DB_TOKEN=os.getenv("ASTRA_DB_TOKEN")
    ASTRA_DB_ID=os.getenv("ASTRA_DB_ID")
    EMBED_MODEL= "BAAI/bge-small-en-v1.5"
settings = Settings()