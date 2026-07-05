import json
import unittest
from pathlib import Path

from e2r.research_reverse.source_quality_inferencer import extract_urls, infer_source_families, infer_source_quality


class ResearchReverseSourceQualityTests(unittest.TestCase):
    def test_url_backed_source_quality(self) -> None:
        text = "회사 IR 원문 https://dart.fss.or.kr/dsaf001/main.do?rcpNo=20260101000001"
        urls = extract_urls(text)
        self.assertEqual(infer_source_quality(text, urls), "A2_URL_BACKED")
        self.assertIn("DART", infer_source_families(urls, text))

    def test_source_proxy_and_evidence_pending_win_over_generic_text(self) -> None:
        self.assertEqual(infer_source_quality("source_proxy_only: true\n기사명만 있음", []), "SOURCE_PROXY_ONLY")
        self.assertEqual(infer_source_quality("evidence_url_pending = true", []), "EVIDENCE_URL_PENDING")

    def test_source_quality_matrix_separates_proxy_and_url_backed(self) -> None:
        matrix = json.loads(
            Path("docs/operational/research_reverse_source_quality_matrix.json").read_text(encoding="utf-8")
        )
        self.assertGreater(matrix["url_backed_replay_candidate_count"], 0)
        self.assertGreater(matrix["source_quality_counts"].get("SOURCE_PROXY_ONLY", 0), 0)
        self.assertEqual(matrix["source_proxy_score_leak_count"], 0)
        self.assertFalse(matrix["price_path_rows_runtime_prompt_allowed"])


if __name__ == "__main__":
    unittest.main()
