# This is the file for training the model
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

if api_key:
    print("API key: " + api_key[0:6])
else:
    print("API key not found")

documents = []

# Load documents from PDF directory if it exists and has files
pdf_dir = "pdf"
if os.path.exists(pdf_dir) and os.listdir(pdf_dir):
    print("Indexing from:", os.path.abspath(pdf_dir))
    try:
        pdf_docs = SimpleDirectoryReader(pdf_dir).load_data()
        documents.extend(pdf_docs)
        print(f"Loaded {len(pdf_docs)} PDF documents")
    except ValueError as e:
        print(f"No PDF files found: {e}")
else:
    print(f"PDF directory is empty or doesn't exist")

# Load documents from DOCX directory if it exists and has files
docx_dir = "docx"
if os.path.exists(docx_dir) and os.listdir(docx_dir):
    print("Indexing from:", os.path.abspath(docx_dir))
    try:
        docx_docs = SimpleDirectoryReader(docx_dir).load_data()
        documents.extend(docx_docs)
        print(f"Loaded {len(docx_docs)} DOCX documents")
    except ValueError as e:
        print(f"No DOCX files found: {e}")
else:
    print(f"DOCX directory is empty or doesn't exist")

# Check if any documents were loaded
if not documents:
    print("ERROR: No documents found in pdf/ or docx/ directories. Please add files and try again.")
    exit(1)

# Application Verification / Not needed for application
print(f"Total documents loaded: {len(documents)}")
for d in documents:
    print("Document preview:", d.text[:200])

# Create index
index = VectorStoreIndex.from_documents(documents)
print("Index built successfully")

# Nodes for verification / Not needed for application
nodes = index.storage_context.docstore.docs
print("Number of nodes:", len(nodes))

# Create query engine
engine = index.as_query_engine()

index.storage_context.persist("ml_index")