import json
import tempfile
import unittest
from datetime import date
from pathlib import Path

from e2r.research_brain.v4_source_quality_promotion import build_source_quality_promotion_report_v4


class ResearchBrainV4SourceQualityRealA2Tests(unittest.TestCase):
    def test_a2_requires_url_snapshot_anchor_claim_and_blocks_source_proxy(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            root = Path(tmpdir)
            snapshot = root / "source.txt"
            snapshot.write_text("삼성전자는 HBM 고객 수요와 medium term revision visibility를 설명했다.", encoding="utf-8")
            sample = root / "memory.jsonl"
            rows = [
                {
                    "record_id": "url-backed",
                    "canonical_archetype_id": "C06_HBM_MEMORY_CUSTOMER_CAPACITY",
                    "symbol": "005930",
                    "company_name": "삼성전자",
                    "source_url": "https://example.com/report",
                    "source_artifact_path": str(snapshot),
                    "entry_date": "2026-06-20",
                    "primitive_ids": ["medium_term_revision_visibility"],
                    "source_proxy_only": False,
                    "evidence_url_pending": False,
                },
                {
                    "record_id": "source-proxy",
                    "canonical_archetype_id": "C24_BIOTECH_BINARY_EVENT",
                    "source_url": "https://example.com/proxy",
                    "source_proxy_only": True,
                    "evidence_url_pending": False,
                },
            ]
            sample.write_text("\n".join(json.dumps(row, ensure_ascii=False) for row in rows), encoding="utf-8")
            report = build_source_quality_promotion_report_v4(
                memory_record_sample_path=sample,
                as_of_date=date(2026, 6, 29),
                attempt_limit=2,
                promotion_limit=2,
                repo_root=root,
            )
        self.assertEqual(report["summary"]["A2_REAL_REPLAY_VERIFIED_count"], 1)
        self.assertEqual(report["summary"]["source_proxy_to_A2_count"], 0)
        promoted = report["promoted_rows"][0]
        self.assertTrue(promoted["snapshot_loaded"])
        self.assertTrue(promoted["anchor_id"])
        self.assertTrue(promoted["claim_id"])


if __name__ == "__main__":
    unittest.main()
