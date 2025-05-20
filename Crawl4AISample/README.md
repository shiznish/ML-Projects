# Crawl4AISample: ChromaDB RAG AI Agent with Groq LLM

This project demonstrates a Retrieval-Augmented Generation (RAG) agent that uses ChromaDB for document retrieval and Groq LLMs for answer generation. The agent logic is built using **Pydantic AI**, which provides a structured and type-safe approach to agent orchestration. The project features a Streamlit web interface for interactive Q&A over your indexed documentation.

## Features

- Combines vector search (ChromaDB) with LLM-based answer generation (Groq)
- Agent logic and orchestration powered by **Pydantic AI**
- Interactive Streamlit web app for chat-based Q&A
- Easy document ingestion and indexing

## Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/<your-username>/Crawl4AISample.git
   cd Crawl4AISample
   ```

2. **Create and activate a virtual environment:**
   ```bash
   python -m venv .venv
   .venv\Scripts\activate 

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set your Groq API key in a `.env` file:**
   ```
   GROQ_API_KEY=your_groq_api_key_here
   ```

5. **Ingest documents (if needed):**
   ```bash
   python insert_docs.py --collection docs --db-dir ./chroma_db --embedding-model all-MiniLM-L6-v2
   ```

6. **Run the Streamlit app:**
   ```bash
   streamlit run streamlit_app.py
   ```

## Usage

- Open [http://localhost:8501](http://localhost:8501) in your browser.
- Ask questions about your indexed documents in the chat interface.

---
