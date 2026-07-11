from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path

from e2r.research_brain.dossier.scoring_pipeline import (
    COMPONENT_QUESTION_FAMILIES,
    run_dossier_scoring_pipeline,
)


class _ImpactProvider:
    provider_name = "TEST_ORGANIC_IMPACT_PROVIDER"

    def complete(self, *, pass_name, payload):
        if pass_name == "IMPACT_SKEPTIC":
            return {"verdict": "APPROVE", "issues": []}
        return {
            "impacts": [
                {
                    "mapping_id": "MAP-1",
                    "primitive_id": "hbm_product_profile",
                    "component_id": "information_confidence",
                    "direction": "SUPPORT",
                    "support_type": "PROFILE_ONLY",
                    "strength_band": "WEAK",
                    "completeness_band": "PARTIAL",
                    "causal_distance": "DIRECT",
                    "temporal_scope": "CURRENT",
                    "source_family": "ISSUER_OFFICIAL",
                    "evidence_family_id": "FAM-PROFILE",
                    "confidence": 0.8,
                    "rationale": "The current issuer quote establishes product profile only.",
                    "unsupported_aspects": ["No customer allocation is established."],
                    "counter_claim_ids": [],
                }
            ],
            "unsupported_aspects": ["No customer, booked capacity, or FCF fact."],
            "counter_thesis": [],
            "reasoning_summary": "Bounded profile impact.",
        }


class _ReviewPendingProvider(_ImpactProvider):
    def complete(self, *, pass_name, payload):
        if pass_name == "IMPACT_SKEPTIC":
            return {"verdict": "REVIEW_PENDING", "issues": ["needs bounded retry"]}
        return super().complete(pass_name=pass_name, payload=payload)


class OrganicDossierScoringPipelineTests(unittest.TestCase):
    def test_full_leaf_chain_requires_impacts_and_terminal_components(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            self._write_inputs(root)
            result = run_dossier_scoring_pipeline(
                dossier_root=root,
                target_id="123456",
                company_name="임의회사",
                as_of_date="2026-07-11",
                archetype_id="C06_HBM_MEMORY_CUSTOMER_CAPACITY",
                impact_provider=_ImpactProvider(),
            )
            self.assertEqual(result["status"], "ORGANIC_DOSSIER_FULL_SCORE_PASS")
            self.assertTrue(result["full_score_valid"])
            self.assertEqual(result["score_type"], "FULL_E2R_100")
            self.assertGreater(result["verified_supported_score"], 0)
            self.assertEqual(result["critical_count_sum"], 0)
            decision = json.loads((root / "atomic_stage_decision.json").read_text())
            self.assertTrue(decision["full_score_valid"])
            self.assertEqual(decision["accepted_claim_ids"], ["CLM-1"])

    def test_provider_pending_component_preserves_points_but_blocks_full_score(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            self._write_inputs(root, pending_family="medium_term_revision_consensus")
            result = run_dossier_scoring_pipeline(
                dossier_root=root,
                target_id="123456",
                company_name="임의회사",
                as_of_date="2026-07-11",
                archetype_id="C06_HBM_MEMORY_CUSTOMER_CAPACITY",
                impact_provider=_ImpactProvider(),
            )
            self.assertEqual(result["status"], "ORGANIC_DOSSIER_SCORING_PENDING")
            self.assertFalse(result["full_score_valid"])
            self.assertGreater(result["verified_supported_score"], 0)
            score = json.loads((root / "component_score_vector.json").read_text())
            self.assertEqual(score["score_type"], "VERIFIED_COMPONENT_PARTIAL")

    def test_retry_failed_only_preserves_passed_rows_and_replaces_failure(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            self._write_inputs(root)
            first = run_dossier_scoring_pipeline(
                dossier_root=root,
                target_id="123456",
                company_name="임의회사",
                as_of_date="2026-07-11",
                archetype_id="C06_HBM_MEMORY_CUSTOMER_CAPACITY",
                impact_provider=_ReviewPendingProvider(),
            )
            self.assertGreater(first["critical_count_sum"], 0)
            second = run_dossier_scoring_pipeline(
                dossier_root=root,
                target_id="123456",
                company_name="임의회사",
                as_of_date="2026-07-11",
                archetype_id="C06_HBM_MEMORY_CUSTOMER_CAPACITY",
                impact_provider=_ImpactProvider(),
                retry_failed_only=True,
            )
            self.assertEqual(second["critical_count_sum"], 0)
            rows = [
                json.loads(line)
                for line in (root / "impact_adjudications.jsonl").read_text().splitlines()
            ]
            self.assertEqual(rows[0]["status"], "IMPACT_ADJUDICATION_PASS")
            self.assertEqual(rows[0]["review_issues"], [])

    def _write_inputs(self, root: Path, pending_family: str | None = None) -> None:
        self._jsonl(
            root / "accepted_current_claims.jsonl",
            [
                {
                    "claim_id": "CLM-1",
                    "target_id": "123456",
                    "mapping_ids": ["MAP-1"],
                    "accepted": True,
                    "evidence_origin": "ORGANIC_LIVE",
                    "fetched": True,
                    "source_proxy_only": False,
                    "exact_quote": "The issuer introduced its current HBM product.",
                }
            ],
        )
        self._jsonl(
            root / "claim_provenance.jsonl",
            [
                {
                    "claim_id": "CLM-1",
                    "target_id": "123456",
                    "document_id": "DOC-1",
                    "source_url": "https://issuer.example/doc",
                    "published_date": "2026-07-10",
                    "exact_quote": "The issuer introduced its current HBM product.",
                    "mapping_ids": ["MAP-1"],
                    "directness": "DIRECT",
                    "temporal_status": "CURRENT",
                    "source_proxy_only": False,
                    "test_only": False,
                    "fetched": True,
                    "anchor_verified": True,
                    "mapping_status": "ACCEPTED",
                }
            ],
        )
        self._jsonl(
            root / "primitive_mappings.jsonl",
            [
                {
                    "mapping_id": "MAP-1",
                    "claim_id": "CLM-1",
                    "primitive_id": "hbm_product_profile",
                    "support_direction": "SUPPORT",
                    "accepted_by_evidence_os": True,
                }
            ],
        )
        self._jsonl(
            root / "evidence_documents.jsonl",
            [
                {
                    "document_id": "DOC-1",
                    "source_class": "IssuerIR",
                    "canonical_url": "https://issuer.example/doc",
                }
            ],
        )
        families = sorted(
            {family for values in COMPONENT_QUESTION_FAMILIES.values() for family in values}
        )
        self._jsonl(
            root / "question_closure.jsonl",
            [
                {
                    "question_family_id": family,
                    "status": "PROVIDER_PENDING" if family == pending_family else "EVALUATED_ABSENT",
                    "search_exhaustion_proof": []
                    if family == pending_family
                    else [f"SEARCH-{family}"],
                }
                for family in families
            ],
        )

    @staticmethod
    def _jsonl(path: Path, rows):
        path.write_text("".join(json.dumps(row) + "\n" for row in rows))


if __name__ == "__main__":
    unittest.main()
