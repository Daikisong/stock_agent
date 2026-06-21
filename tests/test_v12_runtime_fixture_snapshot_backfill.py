from pathlib import Path
import json
import tempfile
import unittest

from e2r.calibration.v12_runtime_fixture_snapshot_backfill import (
    snapshot_text_from_runtime_fixture,
    write_v12_runtime_fixture_snapshot_backfill,
)
from e2r.backtest.runtime_fixture_evidence import RuntimeFixtureEvidenceStore
from e2r.research.report_snapshot_store import ReportSnapshotStore
from e2r.research.search_snapshot_store import SearchSnapshotStore
from e2r.research.web_research_runner import extract_e2r_text_fields


class V12RuntimeFixtureSnapshotBackfillTests(unittest.TestCase):
    def test_writes_normal_search_and_report_snapshots_with_source_backed_fields(self) -> None:
        with tempfile.TemporaryDirectory() as root:
            root_path = Path(root)
            source_path = root_path / "research.md"
            source_path.write_text(
                json.dumps(
                    {
                        "row_type": "trigger",
                        "trigger_id": "T1",
                        "case_id": "C1",
                        "symbol": "000660",
                        "company_name": "SK하이닉스",
                        "market": "KR",
                        "canonical_archetype_id": "C06_HBM_MEMORY_CUSTOMER_CAPACITY",
                        "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS",
                        "evidence_available_at_that_date": "HBM sold out capacity allocation and customer preorder.",
                        "evidence_source": "https://example.com/hbm.pdf",
                    },
                    ensure_ascii=False,
                )
                + "\n",
                encoding="utf-8",
            )
            spec_path = root_path / "spec.json"
            spec_path.write_text(
                json.dumps(
                    {
                        "rows": [
                            {
                                "role": "green",
                                "fixture_status": "ready_for_runtime_replay_fixture",
                                "canonical_archetype_id": "C06_HBM_MEMORY_CUSTOMER_CAPACITY",
                                "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS",
                                "expected_runtime_primitives": [
                                    "hbm_capacity_pre_sold",
                                    "customer_preorder_or_allocation",
                                    "revenue_visibility_contract",
                                ],
                                "candidate": {
                                    "symbol": "000660",
                                    "as_of_date": "2024-04-25",
                                    "trigger_id": "T1",
                                    "case_id": "C1",
                                    "source_file": str(source_path),
                                    "source_proxy_only": False,
                                    "evidence_url_pending": False,
                                    "evidence_source": "https://example.com/hbm.pdf",
                                },
                            }
                        ]
                    },
                    ensure_ascii=False,
                ),
                encoding="utf-8",
            )

            summary = write_v12_runtime_fixture_snapshot_backfill(
                spec_paths=(spec_path,),
                search_snapshot_root=root_path / "search",
                report_snapshot_root=root_path / "reports",
                project_root=root_path,
            )

            search_rows = SearchSnapshotStore(root_path / "search").load_snapshots()
            report_rows = ReportSnapshotStore(root_path / "reports").load_snapshots()
            report_text = ReportSnapshotStore(root_path / "reports").text_for_snapshot(report_rows[0])

        self.assertEqual(summary["snapshot_row_count"], 1)
        self.assertEqual(len(search_rows), 1)
        self.assertEqual(len(report_rows), 1)
        self.assertIn("SK하이닉스 (000660) C06_HBM_MEMORY_CUSTOMER_CAPACITY green source-backed fixture", report_text)
        self.assertIn("E2R_SOURCE_BACKED_FIELD hbm_capacity_pre_sold=true", report_text)
        fields = extract_e2r_text_fields(report_text)
        self.assertEqual(fields["canonical_archetype_id"], "C06_HBM_MEMORY_CUSTOMER_CAPACITY")
        self.assertEqual(fields["large_sector_id"], "L2_AI_SEMICONDUCTOR_ELECTRONICS")
        self.assertTrue(fields["hbm_capacity_pre_sold"])
        self.assertTrue(fields["customer_preorder_or_allocation"])
        self.assertTrue(fields["revenue_visibility_contract"])

    def test_snapshot_text_excludes_claim_metadata_fields(self) -> None:
        with tempfile.TemporaryDirectory() as root:
            root_path = Path(root)
            source_path = root_path / "research.md"
            source_path.write_text(
                '{"row_type":"trigger","trigger_id":"T1","case_id":"C1","symbol":"000660","company_name":"SK하이닉스"}\n',
                encoding="utf-8",
            )
            spec_path = root_path / "spec.json"
            spec_path.write_text(
                json.dumps(
                    {
                        "rows": [
                            {
                                "role": "green",
                                "fixture_status": "ready_for_runtime_replay_fixture",
                                "canonical_archetype_id": "C06_HBM_MEMORY_CUSTOMER_CAPACITY",
                                "expected_runtime_primitives": ["hbm_capacity_pre_sold"],
                                "candidate": {
                                    "symbol": "000660",
                                    "as_of_date": "2024-04-25",
                                    "trigger_id": "T1",
                                    "case_id": "C1",
                                    "source_file": str(source_path),
                                    "source_proxy_only": False,
                                    "evidence_url_pending": False,
                                },
                            }
                        ]
                    }
                ),
                encoding="utf-8",
            )
            row = RuntimeFixtureEvidenceStore((spec_path,), project_root=root_path).rows[0]

        text = snapshot_text_from_runtime_fixture(row)

        self.assertIn("E2R_SOURCE_BACKED_FIELD hbm_capacity_pre_sold=true", text)
        self.assertNotIn("compiled_claim_ids", text)
        self.assertNotIn("source_url", text)


if __name__ == "__main__":
    unittest.main()
