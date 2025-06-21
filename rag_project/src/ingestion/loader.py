from langchain_community.document_loaders import WebBaseLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
import bs4 

def load_and_split(url):
    loader = WebBaseLoader(
        web_paths=url,
        bs_kwargs=dict(parse_only=bs4.SoupStrainer(
            class_=("post-title", "post-content", "post-header")
        ))
    )

    text_documents = loader.load()
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200
    )
    return splitter.split_documents(text_documents)