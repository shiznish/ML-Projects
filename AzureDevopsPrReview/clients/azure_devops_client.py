import httpx
from config import AZURE_ORG, PROJECT, REPO_ID, PR_ID, AZURE_TOKEN
import logging
import re

logger = logging.getLogger(__name__)

class AzureDevOpsClient:
    def __init__(self):
        self.base_url = f"https://dev.azure.com/{AZURE_ORG}/{PROJECT}/_apis"
        self.headers = {
            "Authorization": f"Bearer {AZURE_TOKEN}",
            "Content-Type": "application/json"
        }
        self.session = httpx.AsyncClient(headers=self.headers, timeout=30)

    async def get_iterations(self):
        url = f"{self.base_url}/git/repositories/{REPO_ID}/pullRequests/{PR_ID}/iterations?api-version=7.1"
        resp = await self.session.get(url)
        resp.raise_for_status()
        return resp.json().get("value", [])

    async def get_iteration_changes(self, iteration_id):
        url = f"{self.base_url}/git/repositories/{REPO_ID}/pullRequests/{PR_ID}/iterations/{iteration_id}/changes?api-version=7.1"
        resp = await self.session.get(url)
        resp.raise_for_status()
        return resp.json().get("changeEntries", [])

    async def get_blob_content(self,  blob_id):
        url = f"{self.base_url}/git/repositories/{REPO_ID}/blobs/{blob_id}?api-version=7.1"
        headers = self.headers.copy()
        headers["Accept"] = "application/octet-stream"
        resp = await self.session.get(url, headers=headers)
        resp.raise_for_status()
        return resp.content.decode("utf-8", errors="replace")
    async def post_pr_comment(self, pr_summary: str):
        url = f"{self.base_url}/git/repositories/{REPO_ID}/pullRequests/{PR_ID}/threads?api-version=7.1-preview.1"
        payload = {
            "comments": [{
                "parentCommentId": 0,
                "content": pr_summary,
                "commentType": 1
            }],
            "status": "active"
        }
        try:
            resp = await self.session.post(url, json=payload)
            resp.raise_for_status()
            logger.info("PR summary comment posted successfully.")
        except Exception as e:
            logger.error(f"Failed to post PR summary comment: {e}")

    async def post_inline_and_block_comments(self, file_path: str, llm_output: str):
        inline_pattern = re.compile(r"- \*\*Line (\d+):\*\* (.+)")
        block_start = llm_output.find("### Block-Level Suggestions:")

        # ---- Inline Comments ----
        for line in llm_output.splitlines():
            match = inline_pattern.match(line.strip())
            if match:
                line_num = int(match.group(1))
                comment_text = match.group(2)
                await self._post_inline_comment(file_path, line_num, comment_text)

        # ---- Block-Level Comment ----
        if block_start != -1:
            block_text = llm_output[block_start:].strip()
            if "No suggestions for this file." not in block_text:
                await self._post_block_comment(file_path, block_text)

    async def _post_inline_comment(self, file_path: str, line_num: int, comment: str):
        url = f"{self.base_url}/git/repositories/{REPO_ID}/pullRequests/{PR_ID}/threads?api-version=7.1-preview.1"
        payload = {
            "comments": [{
                "parentCommentId": 0,
                "content": comment,
                "commentType": 1
            }],
            "threadContext": {
                "filePath": file_path,
                "rightFileStart": {"line": line_num, "offset": 1},
                "rightFileEnd": {"line": line_num, "offset": 1}
            },
            "status": "active"
        }
        try:
            resp = await self.session.post(url, json=payload)
            resp.raise_for_status()
            logger.info(f"Posted inline comment on {file_path}:{line_num}")
        except Exception as e:
            logger.error(f"Failed to post inline comment on {file_path}:{line_num}: {e}")

    async def _post_block_comment(self, file_path: str, comment_text: str):
        url = f"{self.base_url}/git/repositories/{REPO_ID}/pullRequests/{PR_ID}/threads?api-version=7.1-preview.1"
        payload = {
            "comments": [{
                "parentCommentId": 0,
                "content": comment_text,
                "commentType": 1
            }],
            "threadContext": {
                "filePath": file_path
            },
            "status": "active"
        }
        try:
            resp = await self.session.post(url, json=payload)
            resp.raise_for_status()
            logger.info(f"Posted block-level comment on {file_path}")
        except Exception as e:
            logger.error(f"Failed to post block-level comment on {file_path}: {e}")
    