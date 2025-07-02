import difflib
from typing import List, Tuple

class DiffAnalyzer:
    @staticmethod
    def generate_diff_with_line_numbers(old_text, new_text):
        old_lines = old_text.splitlines()
        new_lines = new_text.splitlines()
        differ = difflib.SequenceMatcher(None, old_lines, new_lines, autojunk=False)
        changes = []
        current_line = 0
        for tag, i1, i2, j1, j2 in differ.get_opcodes():
            if tag == 'equal':
                current_line += (j2 - j1)
                continue
            if tag in ('insert', 'replace'):
                for j in range(j1, j2):
                    current_line += 1
                    changes.append((current_line, new_lines[j]))
        return changes