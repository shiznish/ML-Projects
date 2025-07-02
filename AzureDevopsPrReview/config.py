import os
from dotenv import load_dotenv

load_dotenv()

AZURE_ORG = os.getenv("AZURE_ORG")
PROJECT = os.getenv("AZURE_PROJECT")
REPO_ID = os.getenv("AZURE_REPO_ID")
PR_ID = os.getenv("PR_ID")
AZURE_TOKEN = os.getenv("SYSTEM_ACCESSTOKEN")
OLLAMA_MODEL = os.getenv("OLLAMA_MODEL")
OLLAMA_URL = os.getenv("OLLAMA_URL")
GROQ_MODEL = os.getenv("GROQ_MODEL")
GROQ_URL = os.getenv("GROQ_URL")
GROQ_API_KEY = os.getenv("GROQ_API_KEY")