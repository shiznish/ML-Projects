# Local AI Agent (RAG)

## Project Overview

The **Local AI Agent (RAG)** is a Retrieval-Augmented Generation (RAG) system designed to answer user queries about a pizza restaurant. By leveraging a combination of a language model and a vector-based retriever, the system provides accurate and contextually relevant answers based on pre-existing reviews.

## Key Features

- **Retrieval-Augmented Generation (RAG)**: Combines retrieval of relevant context with generative AI for precise and informed responses.
- **Customizable Prompt**: Uses a structured prompt template to guide the language model's responses.
- **Interactive Console Application**: Allows users to ask questions interactively in a terminal-based interface.
- **Local Vector Store Integration**: Retrieves relevant reviews using a vector-based retriever for enhanced contextual understanding.

## How It Works

1. **Input Question**: The user inputs a question about the pizza restaurant.
2. **Retrieve Context**: The system retrieves relevant reviews using the `retriever` module.
3. **Generate Response**: The retrieved reviews and the user's question are passed to the language model, which generates a detailed response.
4. **Output Answer**: The system displays the generated answer to the user.

## Code Structure

- **`main.py`**: The entry point of the application. It handles user interaction, context retrieval, and response generation.
- **`vector.py`**: Contains the `retriever` module for fetching relevant reviews from a vector store.
- **Dependencies**:
  - `langchain_ollama`: For integrating the Ollama LLM.
  - `langchain_core`: For prompt templates and chaining operations.

## Example Usage

1. Run the application:
   ```bash
   python main.py