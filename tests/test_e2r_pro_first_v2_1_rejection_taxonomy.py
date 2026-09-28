from __future__ import annotations

import json
from pathlib import Path
from tempfile import TemporaryDirectory
import unittest

from e2r.pro_first.fresh_session.rejection_taxonomy import (
    GENUINE_SEMANTIC_OR_SOURCE_DEFECT,
    INITIAL_PROMPT_OUTPUT_DEFECT,
    LOCAL_NORMALIZATION_OR_VERIFIER_DEFECT,
    build_old_run_rejection_taxonomy,
    render_old_run_rejection_taxonomy_markdown,
)
from e2r.pro_first.ids import canonical_hash


class ProFirstV21RejectionTaxonomyTest(unittest.TestCase):
    def setUp(self) -> None:
        self.temporary_directory = TemporaryDirectory()
        self.addCleanup(self.temporary_directory.cleanup)
        self.root = Path(self.temporary_directory.name)

    def _fact(self, candidate_id: str, **changes):
        fact = {
            "dossier_fact_id": candidate_id,
            "question_family_ids": ["C00_Q01"],
            "current_status": "OPEN",
            "issuer_scoped": True,
            "business_segment": "CORPORATE_GENERIC",
            "product_family": "CORPORATE_GENERIC",
            "supporting_excerpt": "a literal source excerpt",
            "source_url": "https://example.com/report?utm_source=test",
            "source_lineage_id": "SL01",
        }
        fact.update(changes)
        return fact

    def _write_snapshot(self, facts_and_categories):
        facts = [item[0] for item in facts_and_categories]
        register = [
            {
                "candidate_id": fact["dossier_fact_id"],
                "original_candidate_hash": canonical_hash(fact),
                "packet_id": f"PACKET-{index}",
                "question_family_id": "C00_Q01",
                "rejection_category": category,
                "status": "REPAIR_REQUIRED",
            }
            for index, (fact, category) in enumerate(facts_and_categories, 1)
        ]
        path = self.root / "research_passes/01_PROPASS-test/effective_dossier.json"
        path.parent.mkdir(parents=True)
        path.write_text(
            json.dumps(
                {
                    "job_id": "PROJOB-test",
                    "material_facts": facts,
                    "counterfacts": [],
                    "resolution_facts": [],
                    "verification_repair_register": register,
                }
            ),
            encoding="utf-8",
        )

    def test_classifies_a_b_c_without_candidate_specific_rules(self) -> None:
        self._write_snapshot(
            [
                (
                    self._fact("PROFACT-A", current_status="UNKNOWN"),
                    "UNSUPPORTED_DERIVATION",
                ),
                (
                    self._fact(
                        "PROFACT-B1",
                        issuer_scoped=False,
                    ),
                    "WRONG_SUBJECT",
                ),
                (
                    self._fact(
                        "PROFACT-B2",
                        issuer_scoped=False,
                    ),
                    "WRONG_SUBJECT",
                ),
                (self._fact("PROFACT-C"), "WRONG_PRODUCT"),
            ]
        )
        report = build_old_run_rejection_taxonomy(self.root)
        counts = report["aggregates"]["root_cause_class_counts"]
        self.assertEqual(counts[INITIAL_PROMPT_OUTPUT_DEFECT], 1)
        self.assertEqual(counts[LOCAL_NORMALIZATION_OR_VERIFIER_DEFECT], 2)
        self.assertEqual(counts[GENUINE_SEMANTIC_OR_SOURCE_DEFECT], 1)
        self.assertEqual(
            report["aggregates"]["duplicate_mechanical_rejection_count"],
            1,
        )
        self.assertEqual(report["aggregates"]["source_document_count"], 1)
        self.assertNotIn("literal source excerpt", json.dumps(report))
        self.assertNotIn("statement", json.dumps(report))

        required = {
            "candidate_id",
            "question_family_ids",
            "rejection_category",
            "root_cause_class",
            "root_cause_detail",
            "source_document_id",
            "could_be_fixed_locally",
            "requires_new_public_search",
            "requires_pro_semantic_repair",
            "generic_fix_file",
            "generic_fix_function",
            "regression_test_id",
        }
        self.assertTrue(required.issubset(report["rows"][0]))
        markdown = render_old_run_rejection_taxonomy_markdown(report)
        self.assertIn("실제 Pro 의미 수리 대상: **1개**", markdown)

    def test_rejects_register_without_hash_bound_original_fact(self) -> None:
        fact = self._fact("PROFACT-A", current_status="UNKNOWN")
        self._write_snapshot([(fact, "UNSUPPORTED_DERIVATION")])
        path = self.root / "research_passes/01_PROPASS-test/effective_dossier.json"
        payload = json.loads(path.read_text())
        payload["material_facts"][0]["current_status"] = "CURRENT"
        path.write_text(json.dumps(payload), encoding="utf-8")
        with self.assertRaisesRegex(ValueError, "hash-bound original fact"):
            build_old_run_rejection_taxonomy(self.root)

    def test_tracking_parameters_do_not_split_source_document_group(self) -> None:
        self._write_snapshot(
            [
                (
                    self._fact(
                        "PROFACT-B1",
                        issuer_scoped=False,
                        source_url="https://example.com/report?utm_source=a",
                    ),
                    "WRONG_SUBJECT",
                ),
                (
                    self._fact(
                        "PROFACT-B2",
                        issuer_scoped=False,
                        source_url="https://example.com/report?utm_campaign=b",
                    ),
                    "WRONG_SUBJECT",
                ),
            ]
        )
        report = build_old_run_rejection_taxonomy(self.root)
        self.assertEqual(report["aggregates"]["source_document_count"], 1)
        self.assertEqual(
            report["aggregates"]["same_source_grouped_rejection_count"], 2
        )


if __name__ == "__main__":
    unittest.main()
