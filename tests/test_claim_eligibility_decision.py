from __future__ import annotations

import json
import unittest
from pathlib import Path

from e2r.research_brain.scoring.claim_eligibility import (
    audit_claim_eligibility,
    compile_claim_eligibility_decisions,
)


class ClaimEligibilityDecisionTests(unittest.TestCase):
    ROOT = Path(__file__).resolve().parents[1]

    def test_accepted_claim_does_not_automatically_enter_every_plane(self) -> None:
        claim = {
            "claim_id": "CLM-PLANE",
            "target_id": "005930",
            "accepted": True,
            "evidence_origin": "ORGANIC_LIVE",
            "polarity": "POSITIVE",
            "exact_quote": "HBM4 양산 출하를 시작했다.",
        }
        provenance = {
            "claim_id": "CLM-PLANE",
            "source_proxy_only": False,
            "test_only": False,
            "fetched": True,
            "anchor_verified": True,
            "directness": "DIRECT",
            "temporal_status": "CURRENT",
            "mapping_status": "ACCEPTED",
        }
        decision = compile_claim_eligibility_decisions(
            claims=(claim,),
            claim_provenance=(provenance,),
            archetype_id="C06_HBM_MEMORY_CUSTOMER_CAPACITY",
        )[0]
        self.assertTrue(decision.ledger_acceptance)
        self.assertTrue(decision.component_scoring_eligibility)
        self.assertTrue(decision.full_thesis_eligibility)
        self.assertFalse(decision.risk_scoring_eligibility)
        self.assertFalse(decision.stage_event_eligibility)

    def test_source_proxy_can_stay_ledgered_but_not_score(self) -> None:
        claim = {
            "claim_id": "CLM-PROXY",
            "target_id": "005930",
            "accepted": True,
            "evidence_origin": "SOURCE_PROXY",
            "exact_quote": "HBM profile mention",
        }
        decision = compile_claim_eligibility_decisions(
            claims=(claim,),
            claim_provenance=(
                {
                    "claim_id": "CLM-PROXY",
                    "source_proxy_only": True,
                    "fetched": False,
                    "anchor_verified": False,
                    "directness": "DIRECT",
                    "temporal_status": "CURRENT",
                },
            ),
            archetype_id="C06_HBM_MEMORY_CUSTOMER_CAPACITY",
        )[0]
        self.assertTrue(decision.ledger_acceptance)
        self.assertFalse(decision.component_scoring_eligibility)
        self.assertEqual(decision.eligibility_status, "INELIGIBLE_SOURCE_PROXY")

    def test_accepted_primitive_and_same_document_context_define_scope(self) -> None:
        claims = (
            {
                "claim_id": "CLM-CAPACITY",
                "target_id": "123456",
                "accepted": True,
                "evidence_origin": "ORGANIC_LIVE",
                "exact_quote": "Customer demand exceeds supply capacity.",
            },
            {
                "claim_id": "CLM-MARGIN",
                "target_id": "123456",
                "accepted": True,
                "evidence_origin": "ORGANIC_LIVE",
                "exact_quote": "Operating margin reached 72%.",
                "document_context_excerpt": (
                    "HBM sales increased during the quarter. "
                    "Operating margin reached 72%."
                ),
            },
        )
        provenance = tuple(
            {
                "claim_id": claim["claim_id"],
                "source_proxy_only": False,
                "test_only": False,
                "fetched": True,
                "anchor_verified": True,
                "directness": "DIRECT",
                "temporal_status": "CURRENT",
                "mapping_status": "ACCEPTED",
            }
            for claim in claims
        )
        mappings = (
            {
                "claim_id": "CLM-CAPACITY",
                "primitive_id": "hbm_capacity_constraint",
                "accepted_by_evidence_os": True,
            },
            {
                "claim_id": "CLM-MARGIN",
                "primitive_id": "margin_fcf_conversion",
                "accepted_by_evidence_os": True,
            },
        )
        decisions = compile_claim_eligibility_decisions(
            claims=claims,
            claim_provenance=provenance,
            archetype_id="C06_HBM_MEMORY_CUSTOMER_CAPACITY",
            primitive_mappings=mappings,
        )
        self.assertTrue(
            all(row.component_scoring_eligibility for row in decisions)
        )

    def test_operational_eligibility_audit_ignores_legacy_boolean_for_scoring(self) -> None:
        audit = audit_claim_eligibility(repo_root=self.ROOT)
        artifact = json.loads(
            (
                self.ROOT / "docs/operational/e2r_claim_eligibility_audit.json"
            ).read_text()
        )
        self.assertEqual(audit, artifact)
        self.assertEqual(audit["status"], "CLAIM_ELIGIBILITY_PLANES_PASS")
        self.assertEqual(audit["decision_count"], 39)
        self.assertEqual(audit["legacy_boolean_contradiction_count"], 39)
        self.assertEqual(audit["critical_count_sum"], 0)
        self.assertEqual(audit["stage_event_eligible_count"], 0)


if __name__ == "__main__":
    unittest.main()
