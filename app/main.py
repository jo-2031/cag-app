from fastapi import FastAPI
from pydantic import BaseModel
from app.api.routes import router

app = FastAPI(description="Jothika", title="CAG - Redis")

app.include_router(router, tags=["API Endpoint"])

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main.app:app", host="0.0.0.0", log_level="info")