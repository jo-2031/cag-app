import redis
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

redis_client =  redis.StrictRedis(host="localhost", port=6379, db=0, decode_responses=False)

def get_cached_resposne(question_embedding, threshold=0.9):
    cached_keys = redis_client.keys("embedding:*")
    if not cached_keys:
        return None, False
    
    cached_embeddings = []
    cached_questions = []

    for key in cached_keys:
        cached_emb = np.frombuffer(redis_client.get(key), dtype=np.float32)
        cached_embeddings.append(cached_emb)
        cached_questions.append(key.decode("utf-8").replace("embedding:", ""))

    cached_embeddings = np.array(cached_embeddings)
    similarities = cosine_similarity([question_embedding], cached_embeddings)[0]
    max_sim_index = np.argmax(similarities)

    if similarities[max_sim_index] >= threshold:
        similar_question = cached_questions[max_sim_index]
        cached_response = redis_client.get(f"response:{similar_question}")
        if cached_response:
            return cached_response.decode("utf-8"), True  # Cached response found

    return None, False


def store_response(question: str, embedding: list[float], answer: str):
    redis_client.set(f"response:{question}", answer.encode("utf-8"))
    redis_client.set(f"embedding:{question}", np.array(embedding).astype(np.float32).tobytes())

def clear_cache():
    redis_client.flushdb()
