# Crawl4AISample: URL Scraping Knowledgebase with ChromaDB, Groq LLM, and Pydantic AI

This project demonstrates how to **scrape any URL to build a knowledge base**, then use Retrieval-Augmented Generation (RAG) with ChromaDB for document retrieval and Groq LLMs for answer generation. The agent logic is orchestrated using **Pydantic AI**. An interactive Streamlit web app allows you to chat with your custom knowledge base.

## Features

- **URL Scraping:** Crawl and extract content from any URL to populate your knowledge base.
- **Vector Search:** Store and retrieve knowledge using ChromaDB.
- **LLM-Powered Answers:** Use Groq LLMs for generating responses based on retrieved context.
- **Agent Orchestration:** Built with Pydantic AI for structured, type-safe logic.
- **Interactive UI:** Chat with your knowledge base using Streamlit.
- **Easy Document Ingestion:** Add new knowledge with a simple script.

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
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set your Groq API key in a `.env` file:**
   ```
   GROQ_API_KEY=your_groq_api_key_here
   ```

5. **Ingest documents by scraping URLs:**
   ```bash
   python insert_docs.py --url <your-url> --collection docs --db-dir ./chroma_db --embedding-model all-MiniLM-L6-v2
   ```

6. **Run the Streamlit app:**
   ```bash
   streamlit run streamlit_app.py
   ```

## Usage

- Open [http://localhost:8501](http://localhost:8501) in your browser.
- Ask questions about your scraped and indexed knowledge base in the chat interface.
