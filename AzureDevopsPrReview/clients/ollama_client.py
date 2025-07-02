import httpx
from tenacity import retry, stop_after_attempt, wait_fixed
from config import OLLAMA_MODEL, OLLAMA_URL
import logging

logger = logging.getLogger(__name__)

class OllamaClient:
    def __init__(self):
        self.client = httpx.AsyncClient(timeout=60)

    @retry(stop=stop_after_attempt(3), wait=wait_fixed(2))
    async def get_llm_response(self, prompt: str) -> str:
        payload = {
            "model": OLLAMA_MODEL,
            "messages": [{"role": "user", "content": prompt}],
            "stream": False
        }
        try:
            resp = await self.client.post(OLLAMA_URL, json=payload)
            resp.raise_for_status()
            return resp.json().get("message", {}).get("content", "")
        except Exception as e:
            logger.error(f"Ollama call failed: {e}")
            raise
