from __future__ import annotations

import json
import unittest
from pathlib import Path

from e2r.research_brain.scoring import ClaimImpactLedgerBuilder, ClaimImpactProposal


def proposal(impact_id: str, mapping_id: str, primitive_id: str, component_id: str, *, evidence_family_id: str = "FAM-1") -> ClaimImpactProposal:
    return ClaimImpactProposal(
        impact_id=impact_id, claim_id="CLM-1", mapping_id=mapping_id,
        target_id="005930", archetype_id="C06_HBM_MEMORY_CUSTOMER_CAPACITY",
        primitive_id=primitive_id, component_id=component_id, direction="SUPPORT",
        support_type="DIRECT_ACTUAL", strength_band="STRONG",
        completeness_band="SUBSTANTIAL", causal_distance="DIRECT",
        temporal_scope="CURRENT", source_family="ISSUER_OFFICIAL",
        evidence_family_id=evidence_family_id, confidence=0.9,
        rationale="The accepted current claim directly supports this bounded economic aspect.",
        unsupported_aspects=("customer allocation is not inferred",),
    )


class ClaimManyToManyImpactTests(unittest.TestCase):
    ROOT = Path(__file__).resolve().parents[1]
    def setUp(self) -> None:
        self.claims = ({"claim_id":"CLM-1","target_id":"005930","accepted":True,"mapping_ids":["MAP-1","MAP-2"]},)
        self.provenance = ({"claim_id":"CLM-1","mapping_ids":["MAP-1","MAP-2"]},)
        self.satisfaction = ({"status":"REROUTED_CLAIM_ACCEPTED_ORIGINAL_GAP_OPEN","original_gap_open":True,"rerouted_mapping_ids":["MAP-2"]},)

    def test_one_claim_can_support_multiple_primitive_and_component_impacts(self) -> None:
        proposals = (
            proposal("IMP-1","MAP-1","memory_price_increase_mentioned","bottleneck_pricing"),
            proposal("IMP-2","MAP-1","memory_price_increase_mentioned","eps_fcf_explosion"),
            proposal("IMP-3","MAP-2","actual_earnings_conversion","information_confidence",evidence_family_id="FAM-2"),
        )
        result = ClaimImpactLedgerBuilder().build(proposals=proposals, accepted_current_claims=self.claims, claim_provenance=self.provenance, source_task_satisfaction=self.satisfaction)
        self.assertEqual(result.status,"MANY_TO_MANY_CLAIM_IMPACT_PASS")
        self.assertEqual(len(result.validated_impacts),3)
        self.assertEqual(result.audit["multi_impact_claim_count"],1)
        self.assertEqual(result.audit["critical_count_sum"],0)

    def test_rerouted_impact_survives_without_closing_original_gap(self) -> None:
        result = ClaimImpactLedgerBuilder().build(
            proposals=(proposal("IMP-1","MAP-2","actual_earnings_conversion","information_confidence"),),
            accepted_current_claims=self.claims, claim_provenance=self.provenance,
            source_task_satisfaction=self.satisfaction,
        )
        self.assertEqual(len(result.validated_impacts),1)
        self.assertTrue(result.source_task_satisfaction[0]["original_gap_open"])
        self.assertFalse(result.validated_impacts[0].original_source_task_gap_closed)

    def test_mapping_lineage_loss_is_rejected(self) -> None:
        result = ClaimImpactLedgerBuilder().build(
            proposals=(proposal("IMP-X","MAP-NOT-CLAIM","memory_price_increase_mentioned","bottleneck_pricing"),),
            accepted_current_claims=self.claims, claim_provenance=self.provenance,
            source_task_satisfaction=(),
        )
        self.assertEqual(result.status,"MANY_TO_MANY_CLAIM_IMPACT_FAIL")
        self.assertEqual(result.audit["critical_counts"]["mapping_lineage_loss_count"],1)

    def test_duplicate_economic_credit_is_rejected(self) -> None:
        result = ClaimImpactLedgerBuilder().build(
            proposals=(
                proposal("IMP-1","MAP-1","memory_price_increase_mentioned","bottleneck_pricing"),
                proposal("IMP-2","MAP-1","memory_price_increase_mentioned","bottleneck_pricing"),
            ),
            accepted_current_claims=self.claims, claim_provenance=self.provenance,
            source_task_satisfaction=(),
        )
        self.assertEqual(result.audit["critical_counts"]["duplicate_economic_credit_count"],1)

    def test_operational_contract_audit_has_zero_critical_counts(self) -> None:
        audit = json.loads(
            (self.ROOT / "docs/operational/e2r_claim_impact_ledger_audit.json").read_text()
        )
        self.assertEqual(audit["status"], "MANY_TO_MANY_CLAIM_IMPACT_PASS")
        self.assertEqual(audit["validated_impact_count"], 3)
        self.assertEqual(audit["multi_impact_claim_count"], 1)
        self.assertEqual(sum(audit["critical_counts"].values()), 0)


if __name__ == "__main__": unittest.main()
