import logging

from clients.azure_devops_client import AzureDevOpsClient
from clients.ollama_client import OllamaClient
from clients.groq_client import GroqClient
from services.diff_analyzer import DiffAnalyzer
from utils.prompt_builder import PromptBuilder


logger = logging.getLogger(__name__)

class ReviewService:
    def __init__(self):
        self.azure_client = AzureDevOpsClient()
        self.ollama_client = OllamaClient()
        self.groq_client = GroqClient()

    async def run_review(self) -> None:
        iterations = await self.azure_client.get_iterations()
        iteration_id = iterations[-1]["id"]
        changes = await self.azure_client.get_iteration_changes(iteration_id)

        if not changes:
            logger.info("No changes found in the PR.")
            return

        file_summaries = []

        for change in changes:
            file_path = change["item"]["path"]
            old_blob_id = change["item"].get("originalObjectId")
            new_blob_id = change["item"].get("objectId")

            old_content = await self.azure_client.get_blob_content(old_blob_id) if old_blob_id else ""
            new_content = await self.azure_client.get_blob_content(new_blob_id)

            if not new_content:
                logger.info(f"Skipping file with no content: {file_path}")
                continue

            diff_with_line_numbers = DiffAnalyzer.generate_diff_with_line_numbers(old_content, new_content)
            if not diff_with_line_numbers:
                logger.info(f"No meaningful changes in file: {file_path}")
                continue

            # Generate File-Level Summary           
            file_level_prompt = PromptBuilder.create_analysis_prompt(diff_with_line_numbers)
            file_summary = await self.ollama_client.get_llm_response(file_level_prompt)
            file_summaries.append(f"## File: `{file_path}`\n{file_summary.strip()}\n")

            # Generate Inline Comments
            review_prompt = PromptBuilder.create_review_prompt(file_path, diff_with_line_numbers)
            inline_review = await self.ollama_client.get_llm_response(review_prompt)
            if inline_review:
                await self.azure_client.post_inline_and_block_comments(file_path, inline_review)

        # Post Overall PR Summary
        if file_summaries:
            combined_summary = "\n".join(file_summaries)
            final_prompt = PromptBuilder.create_pr_summary_prompt(combined_summary)
            pr_summary = await self.ollama_client.get_llm_response(final_prompt)
            await self.azure_client.post_pr_comment(pr_summary)

