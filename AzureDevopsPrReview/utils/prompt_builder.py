from typing import List, Tuple

class PromptBuilder:
    @staticmethod
    def create_analysis_prompt(diff_text: str) -> str:
        return f"""You are an AI reviewer helping summarize Pull Requests for comments.

                    Given the following unified diff, generate a clear and concise summary of the key code changes.

                    ### VERY IMPORTANT:
                    - Do NOT include any preamble, disclaimers, introductions, model behavior notes, or explanations about AI or the task.
                    - Output should start **directly with the section heading: `### Summary of Changes`**
                    - No extra text before that.

                    ### Instructions:
                    - Focus ONLY on meaningful behavior, logic, or structure changes.
                    - Ignore whitespace, formatting, or minor naming changes.
                    - Use a neutral, technical tone – no opinions.
                    - Group related changes together logically.
                    - Output should be short and skimmable.

                    ### Output Format (Start exactly like this, with no extra lines before it):

                    ### Summary of Changes
                    - <Short and specific change #1>
                    - <Short and specific change #2>
                    - <Short and specific change #3>
                    [Add more only if significant, maximum 6 lines total]

                    Diff:
                    {diff_text}"""
    
    @staticmethod
    def create_review_prompt(file_path: str, diff_lines: List[Tuple[int, str]]) -> str:
        diff_preview = "\n".join(f"Line {line}: {code}" for line, code in diff_lines)
        return f"""
                You are an AI Code Reviewer for a professional enterprise software development team working on C#/.NET projects.

                You will receive a unified diff of the file `{file_path}` containing the code changes in this pull request.

                ---

                ###  Review Objectives:

                Focus ONLY on:
                - Logical correctness
                - Code structure and design
                - Security vulnerabilities
                - Performance issues
                - Readability and maintainability
                - Proper exception handling
                - Missing input validations
                - Resource leaks or thread-safety concerns (where applicable)

                Ignore and **do not comment on**:
                - Minor formatting (indentation, spacing, etc.)
                - Naming preferences unless misleading
                - File-scoped namespace declarations (e.g., `namespace X.Y.Z;` are valid in C# 10+)
                - Modern C# syntax features like:
                    - `record`, `init`, `expression-bodied members`, etc.

                Do not suggest:
                - Replacing valid file-scoped namespaces with using statements.
                - Stylistic changes unrelated to logic or functionality.
                - Personal opinions or subjective phrasing.

                ---

                ###  Output Format (STRICTLY FOLLOW THIS):

                ```markdown
                ## File: {file_path}

                ### Line-Level Comments:
                - **Line <number>:** <Your precise, actionable code review comment>

                ### Block-Level Suggestions:
                - **Lines <start>-<end>:** <Your high-level block comment for multi-line issues>

                If there are no issues at all, reply with:

                No suggestions for this file.
                Additional Context:
                If a coding standard or design principle is violated (like SOLID, error handling, null checks), mention it.

                If input validation is missing, highlight it.

                Focus on providing concise, non-redundant, technically sound, and production-grade review comments.

                Diff Preview for Review:
                {diff_preview}
                """
    
    @staticmethod
    def create_pr_summary_prompt(file_summaries: str) -> str:
        return f"""
                You are a senior code reviewer.

                Below are file-wise summaries from a PR:

                {file_summaries}

                Now generate a concise **Overall PR Summary** following good enterprise tone.
                """