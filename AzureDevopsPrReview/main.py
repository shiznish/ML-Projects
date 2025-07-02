import asyncio
from services.review_service import ReviewService
from utils.logger import setup_logger

setup_logger()

async def main():
    reviewer = ReviewService()
    await reviewer.run_review()

if __name__ == "__main__":
    asyncio.run(main())