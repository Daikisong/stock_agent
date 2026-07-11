from __future__ import annotations

import json
import unittest
from pathlib import Path

from e2r.research_brain.scoring import (
    ClaimImpactLedgerBuilder,
    ClaimImpactProposal,
)


class FoundryNotHBMAllocationTests(unittest.TestCase):
    ROOT = Path(__file__).resolve().parents[1]

    def test_tesla_foundry_claim_stays_global_but_c06_impact_is_rerouted(self) -> None:
        root = self.ROOT / "output/evidence_to_score/c06/2026-07-11/005930"
        claims = [
            json.loads(line)
            for line in (root / "accepted_current_claims.jsonl").read_text().splitlines()
            if line.strip()
        ]
        claim = next(
            row
            for row in claims
            if row["claim_id"] == "CLM-464ca5cde1b30c363997"
        )
        provenance = [
            json.loads(line)
            for line in (root / "claim_provenance.jsonl").read_text().splitlines()
            if line.strip()
        ]
        prov = next(row for row in provenance if row["claim_id"] == claim["claim_id"])
        proposal = ClaimImpactProposal(
            impact_id="IMPACT-FOUNDRY-C06-GUARD",
            claim_id=claim["claim_id"],
            mapping_id=claim["mapping_ids"][1],
            target_id="005930",
            archetype_id="C06_HBM_MEMORY_CUSTOMER_CAPACITY",
            primitive_id="revenue_visibility_contract",
            component_id="earnings_visibility",
            direction="SUPPORT",
            support_type="PARTIAL_BRIDGE",
            strength_band="MODERATE",
            completeness_band="PARTIAL",
            causal_distance="ONE_HOP",
            temporal_scope="CURRENT",
            source_family="OFFICIAL_FILING",
            evidence_family_id=claim["document_id"],
            confidence=0.9,
            rationale="동일 issuer 계약이지만 C06 scope 검증이 필요하다.",
            unsupported_aspects=("HBM 제품과 고객 배정은 확인되지 않았다.",),
        )
        result = ClaimImpactLedgerBuilder().build(
            proposals=(proposal,),
            accepted_current_claims=(claim,),
            claim_provenance=(prov,),
            source_task_satisfaction=(),
        )
        self.assertTrue(claim["accepted"])
        self.assertEqual(result.status, "MANY_TO_MANY_CLAIM_IMPACT_PASS")
        self.assertEqual(result.validated_impacts, ())
        self.assertEqual(
            result.rejected_impacts[0]["reason"],
            "REROUTED_TO_OTHER_MECHANISM",
        )
        scope = result.rejected_impacts[0]["scope_validation"]
        self.assertEqual(scope["rerouted_archetype_id"], "C01_ORDER_BACKLOG_MARGIN_BRIDGE")
        self.assertTrue(scope["original_gap_open"])


if __name__ == "__main__":
    unittest.main()
