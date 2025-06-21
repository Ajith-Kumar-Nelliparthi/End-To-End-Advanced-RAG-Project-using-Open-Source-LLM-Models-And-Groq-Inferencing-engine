import cassio
from langchain.vectorstores.cassandra import Cassandra
from langchain.indexes.vectorstore import VectorStoreIndexWrapper
from config.settings import settings

def create_vector_index(docs, embedder):
    """
    Create a vector index using Cassandra as the vector store.
    """
    # Initialize the Cassandra vector store with the provided settings
    cassio.init(token=settings.ASTRA_DB_TOKEN, database_id=settings.ASTRA_DB_ID)
    store = Cassandra(embedding=embedder, table_name="qa_mini", session=None, keyspace=None)
    store.add_documents(docs)
    
    # Create and return a VectorStoreIndexWrapper for the vector store
    return VectorStoreIndexWrapper(vectorstore=store)