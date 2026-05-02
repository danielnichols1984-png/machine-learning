# server.py
from llama_index.core import StorageContext, load_index_from_storage
from dotenv import load_dotenv
import os
from pydantic import BaseModel
import uvicorn
from fastapi import FastAPI, HTTPException

class Item(BaseModel):
    question: str

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

# --- Load Index Safely ---
print("Loading index...")

INDEX_DIR = "ml_index"

if not os.path.exists(INDEX_DIR):
    raise RuntimeError(
        f"Index directory '{INDEX_DIR}' not found. "
        "Run your llama-indexing.py script first to build the index."
    )

try:
    storage_context = StorageContext.from_defaults(persist_dir=INDEX_DIR)
    index = load_index_from_storage(storage_context)
    print("Index loaded.")
except Exception as e:
    raise RuntimeError(f"Failed to load index: {e}")

engine = index.as_query_engine()

# --- FastAPI App ---
app = FastAPI()

@app.post("/")
async def query(item: Item):
    try:
        result = engine.query(item.question)
        return {"response": str(result)}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Query failed: {e}")

if __name__ == "__main__":
    uvicorn.run("server:app", host="0.0.0.0", port=8000)
