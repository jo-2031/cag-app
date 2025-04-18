from fastapi import APIRouter, Query, HTTPException
from app.services.retriever import query_rag
from app.services.cache import clear_cache
from app.services.extract_load import store_in_vector_db

router = APIRouter()


@router.get("/extract_vector_load")
def extract_vector_load(url:str = Query(..., description="Enter the url forthe extract")):
    try: 
        store_in_vector_db(url)
        return {
            "message": "Data wee succesfully loaded to Vector DB"
        }
    except Exception as e:
        raise HTTPException(status_code=500, detial=f"failed to ingest URL: {str(e)}")


@router.post("/query_to_ask")
def ask_question(q:str = Query(..., description="your question")):
    response, is_cached = query_rag(q)
    return {
        "question":q,
        "response": response,
        "cached":is_cached
    }

@router.post("/clear_cache")
def clear_cache_endpoint():
    clear_cache()
    return {
        "message":"cache cleared successfully"
    }

