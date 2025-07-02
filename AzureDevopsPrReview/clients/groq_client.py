import httpx
import logging
from tenacity import retry, wait_exponential, stop_after_attempt, retry_if_exception
from config import GROQ_API_KEY, GROQ_MODEL, GROQ_URL

logger = logging.getLogger(__name__)

def is_retryable_exception(exception):
    """Retry only for HTTP 429 (Too Many Requests) and 5xx server errors."""
    if isinstance(exception, httpx.HTTPStatusError):
        status = exception.response.status_code
        return status == 429 or 500 <= status < 600
    return False

class GroqClient:
    def __init__(self):
        self.headers = {
            "Authorization": f"Bearer {GROQ_API_KEY}",
            "Content-Type": "application/json"
        }

    @retry(
        stop=stop_after_attempt(5),
        wait=wait_exponential(multiplier=1, min=2, max=10),
        retry=retry_if_exception(is_retryable_exception),
        reraise=True
    )
    async def get_llm_response(self, prompt: str) -> str:
        payload = {
            "model": GROQ_MODEL,
            "messages": [
                {"role": "system", "content": "You are an experienced code reviewer."},
                {"role": "user", "content": prompt}
            ]
        }

        async with httpx.AsyncClient(timeout=60) as client:
            try:
                logger.info(f"Calling Groq API for prompt of length {len(prompt)}")
                response = await client.post(GROQ_URL, json=payload, headers=self.headers)
                response.raise_for_status()
                return response.json()["choices"][0]["message"]["content"]
            except httpx.HTTPStatusError as e:
                logger.error(f"Groq API error {e.response.status_code}: {e.response.text}")
                raise
            except Exception as e:
                logger.error(f"Unexpected error while calling Groq API: {str(e)}")
                raise
