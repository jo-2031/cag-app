# Cache-Augmented Generation (CAG): Context-Aware AI Assistant

This project implements a **Cache-Augmented Generation (CAG)** system that enhances the efficiency of Large Language Models (LLMs) by caching and reusing semantically similar responses. Built with **FastAPI**, **Redis**, and **Streamlit**, this system provides rapid, context-aware answers to user queries.

---

## Features

- **Semantic Caching with Redis**  
  Avoids redundant LLM calls by storing and retrieving responses based on semantic similarity.

- **Dynamic Response Generation**  
  Utilizes an LLM to generate context-aware responses when no cached answer is available.

- **FastAPI Backend**  
  Handles API requests, manages response logic, and integrates with Redis for caching.

- **Streamlit Frontend**  
  Provides a user-friendly interface for interacting with the AI assistant.

---

## Tech Stack

- **Frontend**: Streamlit
- **Backend**: FastAPI
- **Cache**: Redis
- **LLM**: OpenAI / LLaMA / Any pluggable LLM
- **Vector Search**: Sentence embedding similarity

---

## Setup Instructions

### Prerequisites

Ensure you have the following installed:

- Python 3.8+
- Redis server running locally or remotely

### Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/yourusername/cag-system.git

2. **Install dependencies:**
    ```bash
    pip install -r requirements.txt
3. **Run the FastAPI server:**

    To start the FastAPI backend server, run the following command:
    ```bash 
    uvicorn app.main:app --reload
4. **Run the Streamlit frontend:**
    To run the Streamlit frontend application, use the following command:
    ```bash
    streamlit run frontend/main.py