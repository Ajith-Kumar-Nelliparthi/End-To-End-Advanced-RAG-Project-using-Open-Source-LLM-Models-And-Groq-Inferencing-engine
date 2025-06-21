from langchain_core.prompts import ChatPromptTemplate
from langchain.chains import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain

def build_rag_chain(vectorstore, llm):
    """
    Build a Retrieval-Augmented Generation (RAG) chain using the provided LLM and vector store.
    
    Args:
        llm: The language model to use for generation.
        vectorstore: The vector store to use for document retrieval.
        
    Returns:
        A chain that combines document retrieval and generation.
    """
    # Create a prompt template for the RAG chain
    prompt = ChatPromptTemplate.from_template("""
    Answer the following question based only on the provided context.
    Think step by step before providing a detailed answer.
    I will tip you $1000 if the user finds the answer helpful.
    <context>
    {context}
    </context>

    Question: {input}""")

    retriever = vectorstore.vectorstore.as_retriever()
    document_chain = create_stuff_documents_chain(llm, prompt)
    return create_retrieval_chain(retriever, document_chain)