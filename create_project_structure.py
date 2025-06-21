import os

# Define the base structure
folders = [
    "rag_project/app",
    "rag_project/config",
    "rag_project/data",
    "rag_project/src/embeddings",
    "rag_project/src/ingestion",
    "rag_project/src/vectorstore",
    "rag_project/src/pipeline",
    "rag_project/src/llm",
]

# Files to create within the structure
init_files = [
    "rag_project/app/__init__.py",
    "rag_project/config/__init__.py",
    "rag_project/src/__init__.py",
    "rag_project/src/embeddings/__init__.py",
    "rag_project/src/ingestion/__init__.py",
    "rag_project/src/vectorstore/__init__.py",
    "rag_project/src/pipeline/__init__.py",
    "rag_project/src/llm/__init__.py",
]

# Create folders
for folder in folders:
    os.makedirs(folder, exist_ok=True)
    print(f"Created folder: {folder}")

# Create __init__.py files
for file in init_files:
    with open(file, "w") as f:
        pass  # Empty __init__.py
    print(f"Created file: {file}")

