# 💡 CAG: Context-Aware Generation System

This project is a **Context-Aware Generation (CAG)** system built with **FastAPI**, **Redis**, and **Streamlit**, powered by a **Large Language Model (LLM)**. It caches generated responses using Redis and intelligently retrieves them based on semantic similarity — even when user queries are phrased differently but have the same meaning.

---

## 🚀 Features

- 🔁 **Redis Caching**  
  Avoids repeated generation by caching LLM responses based on semantic similarity.

- 🧠 **LLM Integration**  
  Uses a language model to dynamically generate context-aware responses.

- 🌐 **FastAPI Backend**  
  Handles API requests and manages response logic.

- 🎨 **Streamlit Frontend**  
  Provides a simple and intuitive user interface.


---

## 🧱 Tech Stack

- **Frontend**: Streamlit
- **Backend**: FastAPI
- **Cache**: Redis
- **LLM**: (OpenAI / LLaMA / any pluggable LLM)
- **Vector Search**: Sentence embedding similarity

