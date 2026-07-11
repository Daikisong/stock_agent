from __future__ import annotations

import json
import unittest
from pathlib import Path

from e2r.research_brain.scoring import (
    ClaimImpactProposal,
    ImpactValidator,
    ValidatedClaimImpact,
    audit_component_scoring_model,
    load_component_scoring_model,
    score_component_subcriteria,
)


class ComponentSubcriterionScoringTests(unittest.TestCase):
    ROOT = Path(__file__).resolve().parents[1]
    ARCHETYPE = "C06_HBM_MEMORY_CUSTOMER_CAPACITY"

    def test_model_budgets_sum_to_all_seven_component_maxima(self) -> None:
        audit = audit_component_scoring_model(archetype_id=self.ARCHETYPE)
        expected = json.loads(
            (
                self.ROOT
                / "docs/operational/e2r_component_scoring_model_audit.json"
            ).read_text(encoding="utf-8")
        )
        self.assertEqual(audit, expected)
        self.assertEqual(audit["critical_count_sum"], 0)
        self.assertEqual(audit["component_count"], 7)
        self.assertEqual(audit["subcriterion_count"], 26)

    def test_one_actual_fact_credits_only_its_declared_subcriterion(self) -> None:
        impact = self._validated_impact(
            impact_id="I-ACTUAL",
            claim_id="C-ACTUAL",
            mapping_id="M-ACTUAL",
            primitive_id="actual_earnings_conversion",
            component_id="eps_fcf_explosion",
            subcriterion_id="C06_EPS_ACTUAL_REVENUE_PROFIT",
            question_family_id="revenue_operating_profit_conversion",
        )
        result = score_component_subcriteria(
            model=load_component_scoring_model(self.ARCHETYPE),
            impacts=(impact,),
        )
        credited = [
            row
            for row in result.scores
            if row.component_id == "eps_fcf_explosion" and row.points > 0
        ]
        self.assertEqual(len(credited), 1)
        self.assertEqual(
            credited[0].subcriterion_id,
            "C06_EPS_ACTUAL_REVENUE_PROFIT",
        )
        self.assertEqual(result.audit["critical_count_sum"], 0)

    def test_market_component_is_capped_when_required_valuation_bridge_is_missing(self) -> None:
        revision = self._validated_impact(
            impact_id="I-REV",
            claim_id="C-REV",
            mapping_id="M-REV",
            primitive_id="medium_term_revision_visibility",
            component_id="market_mispricing",
            subcriterion_id="C06_MKT_REVISION_VS_CONSENSUS",
            question_family_id="medium_term_revision_consensus",
            strength="VERY_STRONG",
            completeness="COMPLETE_FOR_PRIMITIVE",
        )
        expectation = self._validated_impact(
            impact_id="I-EXPECT",
            claim_id="C-EXPECT",
            mapping_id="M-EXPECT",
            primitive_id="market_expectation_gap",
            component_id="market_mispricing",
            subcriterion_id="C06_MKT_CURRENT_EXPECTATION_GAP",
            question_family_id="medium_term_revision_consensus",
            strength="VERY_STRONG",
            completeness="COMPLETE_FOR_PRIMITIVE",
        )
        result = score_component_subcriteria(
            model=load_component_scoring_model(self.ARCHETYPE),
            impacts=(revision, expectation),
        )
        self.assertEqual(result.component_points["market_mispricing"], 8.25)
        self.assertEqual(result.audit["critical_count_sum"], 0)

    def test_information_confidence_uses_best_source_dimensions_not_claim_count(self) -> None:
        impact = self._validated_impact(
            impact_id="I-INFO",
            claim_id="C-INFO",
            mapping_id="M-INFO",
            primitive_id="actual_earnings_conversion",
            component_id="information_confidence",
            subcriterion_id="C06_INFO_SOURCE_QUALITY",
            question_family_id="revenue_operating_profit_conversion",
        )
        result = score_component_subcriteria(
            model=load_component_scoring_model(self.ARCHETYPE),
            impacts=(impact,),
        )
        info_scores = {
            row.subcriterion_id: row
            for row in result.scores
            if row.component_id == "information_confidence"
        }
        self.assertEqual(result.component_points["information_confidence"], 2.4)
        self.assertEqual(
            info_scores["C06_INFO_INDEPENDENT_CORROBORATION"].points,
            0.0,
        )
        self.assertEqual(result.audit["critical_count_sum"], 0)

    def _validated_impact(
        self,
        *,
        impact_id: str,
        claim_id: str,
        mapping_id: str,
        primitive_id: str,
        component_id: str,
        subcriterion_id: str,
        question_family_id: str,
        strength: str = "STRONG",
        completeness: str = "SUBSTANTIAL",
    ):
        proposal = ClaimImpactProposal(
            impact_id=impact_id,
            claim_id=claim_id,
            mapping_id=mapping_id,
            target_id="TARGET-X",
            archetype_id=self.ARCHETYPE,
            primitive_id=primitive_id,
            component_id=component_id,
            direction="SUPPORT",
            support_type="DIRECT_ACTUAL",
            strength_band=strength,
            completeness_band=completeness,
            causal_distance="DIRECT",
            temporal_scope="CURRENT",
            source_family="ISSUER_OFFICIAL",
            evidence_family_id=f"F-{impact_id}",
            confidence=0.9,
            rationale="A bounded subcriterion-specific current fact.",
            unsupported_aspects=("No other subcriterion is inferred.",),
            question_family_id=question_family_id,
            component_subcriterion_id=subcriterion_id,
            mechanism_scope_match=True,
        )
        scope = {
            "status": "MECHANISM_SCOPE_PASS",
            "scope_match": True,
            "scope": {
                "issuer_id": "TARGET-X",
                "business_segment": "MEMORY",
                "product_family": "HBM",
                "economic_mechanism": "MARKET_EXPECTATION_GAP",
            },
        }
        validation = ImpactValidator().validate(
            impacts=(
                ValidatedClaimImpact(
                    proposal,
                    scope_validation=scope,
                    eligibility_decision_id=f"E-{claim_id}",
                ),
            ),
            claim_provenance=(
                {
                    "claim_id": claim_id,
                    "mapping_ids": [mapping_id],
                    "document_id": f"D-{claim_id}",
                    "source_proxy_only": False,
                    "directness": "DIRECT",
                    "temporal_status": "CURRENT",
                },
            ),
            claim_eligibility_decisions=(
                {
                    "eligibility_decision_id": f"E-{claim_id}",
                    "claim_id": claim_id,
                    "component_scoring_eligibility": True,
                },
            ),
            accepted_current_claims=(
                {
                    "claim_id": claim_id,
                    "target_id": "TARGET-X",
                    "accepted": True,
                    "mapping_ids": [mapping_id],
                    "economic_fact_key": f"FACT-{claim_id}",
                },
            ),
        )
        self.assertEqual(validation.status, "IMPACT_CREDIT_CAP_PASS")
        return validation.impacts[0]


if __name__ == "__main__":
    unittest.main()
