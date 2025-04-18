from app.services.embedding import get_openai_embedding
from app.services.cache import get_cached_resposne, store_response
from app.services.extract_load import collection
from app.config import OPENAI_API_KEY
import openai


def query_rag(question:str):
    question_embedding = get_openai_embedding([question])[0]
    cached_response, is_cached = get_cached_resposne(question_embedding)

    if cached_response:
        return cached_response, is_cached
    
    results = collection.query(
        query_embeddings=[question_embedding],
        n_results=3
    )
    retrieved_texts = [doc for doc in results["documents"][0]] if results["documents"] else []

    if not retrieved_texts:
        return "No relevant documents found.", False

    context = "\n".join(retrieved_texts)
    prompt = f"Based on this context, answer the question:\n\n{context}\n\nQ: {question}\nA:"

    client = openai.OpenAI(api_key=OPENAI_API_KEY)
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[{"role": "system", "content": prompt}]
    )

    answer = response.choices[0].message.content

    store_response(question, question_embedding, answer)
    return answer, False

