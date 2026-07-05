import json
import unittest
from pathlib import Path


class ResearchSourceRouteNoSnippetScoreTests(unittest.TestCase):
    def test_snippet_is_never_score_source(self) -> None:
        matrix = json.loads(Path("docs/operational/research_source_route_recovery_matrix.json").read_text(encoding="utf-8"))
        self.assertFalse(matrix["snippet_score_allowed"])
        self.assertFalse(matrix["research_memory_score_allowed"])
        snippet_patterns = [pattern for pattern in matrix["patterns"] if pattern["source_family"] == "Snippet"]
        self.assertGreater(len(snippet_patterns), 0)
        for pattern in snippet_patterns:
            self.assertEqual(pattern["route_role"], "FORBIDDEN_FOR_SCORE")
            self.assertFalse(pattern["requires_quote_anchor"])


if __name__ == "__main__":
    unittest.main()
