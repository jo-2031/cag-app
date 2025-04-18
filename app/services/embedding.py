import openai
from app.config import OPENAI_API_KEY

def get_openai_embedding(texts: list[str]) -> list[list[float]]:
    client = openai.OpenAI(api_key=OPENAI_API_KEY)
    response = client.embeddings.create(
        model="text-embedding-ada-002",
        input=texts
    )
    return [res.embedding for res in response.data]