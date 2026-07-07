import json
import unittest
from pathlib import Path
from tempfile import TemporaryDirectory

from e2r.census.source_lineage_repair_audit import (
    build_source_lineage_repair_audit,
    write_source_lineage_repair_audit,
)


class SourceLineageRepairAuditTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.output_root = Path(
            "output/census_v4/2026-07-05-research-to-runtime-parity-self-repair-01-20260707T130702Z"
        )
        cls.audit = build_source_lineage_repair_audit(output_root=cls.output_root)
        cls.by_archetype = {row["archetype_id"]: row for row in cls.audit["archetypes"]}

    def test_audit_splits_route_only_candidates_from_generic_rejections(self) -> None:
        self.assertEqual(self.audit["schema_version"], "e2r_source_lineage_repair_audit_v1")
        self.assertGreater(self.audit["lineage_rejection_count"], 0)
        self.assertGreater(self.audit["route_only_candidate_count"], 0)
        self.assertGreater(self.audit["current_code_verified_retry_candidate_count"], 0)
        self.assertFalse(self.audit["score_evidence_allowed_from_rejected_rows"])
        self.assertIn("source_lineage_unverified_original", self.audit["reason_counts"])
        self.assertIn("BrokerReportPublicPDF", self.audit["source_class_counts"])

    def test_c28_broker_report_routes_are_retry_candidates_not_score_evidence(self) -> None:
        c28 = self.by_archetype["C28_SOFTWARE_SECURITY_CONTRACT_RETENTION"]
        self.assertGreater(c28["lineage_rejection_count"], 0)
        self.assertGreater(c28["route_only_candidate_count"], 0)
        self.assertGreater(c28["current_code_verified_retry_candidate_count"], 0)
        self.assertIn("BrokerReportPublicPDF", c28["source_class_counts"])
        self.assertTrue({"bbn.kiwoom.com", "securities.miraeasset.com"}.issubset(c28["source_domain_counts"]))
        self.assertTrue(
            any(
                sample["current_route_patch_status"]
                == "CURRENT_CODE_VERIFIES_BROKER_REPORT_ORIGINAL_RETRY_REQUIRED"
                for sample in c28["samples"]
            )
        )

    def test_c08_contains_broker_route_candidates_but_still_needs_semantic_or_primitive_repair(self) -> None:
        c08 = self.by_archetype["C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY"]
        self.assertGreater(c08["lineage_rejection_count"], 0)
        self.assertGreater(c08["current_code_verified_retry_candidate_count"], 0)
        self.assertIn("eugenefn.com", c08["source_domain_counts"])
        self.assertTrue(
            any(sample["non_route_reasons"] for sample in c08["samples"]),
            "C08 should not be reported as source-route-only complete; some samples still fail target/semantic/primitive checks.",
        )

    def test_writer_outputs_json_markdown_and_alias(self) -> None:
        with TemporaryDirectory() as tmpdir:
            reports = write_source_lineage_repair_audit(output_root=self.output_root, docs_dir=tmpdir)
            payload = json.loads(Path(reports["json_path"]).read_text(encoding="utf-8"))
            alias = json.loads((Path(tmpdir) / "source_lineage_repair_audit.json").read_text(encoding="utf-8"))
            markdown = Path(reports["markdown_path"]).read_text(encoding="utf-8")

        self.assertEqual(payload["schema_version"], "e2r_source_lineage_repair_audit_v1")
        self.assertEqual(alias["lineage_rejection_count"], payload["lineage_rejection_count"])
        self.assertIn("Source Lineage Repair Audit", markdown)
        self.assertIn("점수 근거가 아니다", markdown)


if __name__ == "__main__":
    unittest.main()
