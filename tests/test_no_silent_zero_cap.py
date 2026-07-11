from __future__ import annotations

import unittest
from dataclasses import replace
from unittest.mock import patch

from e2r.research_brain.runtime.scoring_contracts import (
    ScoringContractIncompleteError,
    load_scoring_policy_v2,
)
from e2r.research_brain.scoring import (
    ClaimImpactProposal,
    ImpactValidator,
    ValidatedClaimImpact,
)


def _impact(*, source_family: str = "ISSUER_OFFICIAL", temporal_scope: str = "CURRENT", direction: str = "SUPPORT", support_type: str = "DIRECT_ACTUAL"):
    return ValidatedClaimImpact(
        ClaimImpactProposal(
            impact_id="IMPACT-TOTALITY",
            claim_id="CLM-TOTALITY",
            mapping_id="MAP-TOTALITY",
            target_id="005930",
            archetype_id="C06_HBM_MEMORY_CUSTOMER_CAPACITY",
            primitive_id="actual_earnings_conversion",
            component_id="eps_fcf_explosion",
            direction=direction,
            support_type=support_type,
            strength_band="STRONG",
            completeness_band="SUBSTANTIAL",
            causal_distance="DIRECT",
            temporal_scope=temporal_scope,
            source_family=source_family,
            evidence_family_id="DOC-TOTALITY",
            confidence=0.9,
            rationale="직접 actual earnings conversion 근거다.",
            unsupported_aspects=("FCF는 별도 확인이 필요하다.",),
        ),
        scope_validation={"status":"MECHANISM_SCOPE_PASS","scope_match":True,"scope":{"issuer_id":"005930","business_segment":"MEMORY","product_family":"HBM","economic_mechanism":"ACTUAL_EARNINGS_CONVERSION"}},
        eligibility_decision_id="ELIG-TOTALITY",
    )


PROVENANCE = (
    {
        "claim_id": "CLM-TOTALITY",
        "mapping_ids": ["MAP-TOTALITY"],
        "source_proxy_only": False,
        "directness": "DIRECT",
        "temporal_status": "CURRENT",
    },
)
ELIGIBILITY = (
    {
        "eligibility_decision_id": "ELIG-TOTALITY",
        "claim_id": "CLM-TOTALITY",
        "component_scoring_eligibility": True,
    },
)


class NoSilentZeroCapTests(unittest.TestCase):
    def test_unknown_source_family_is_hard_error_not_zero_credit(self) -> None:
        with self.assertRaisesRegex(
            ScoringContractIncompleteError,
            "SCORING_CONTRACT_INCOMPLETE:source_family_caps:UNKNOWN_NEW_SOURCE",
        ):
            ImpactValidator().validate(
                impacts=(_impact(source_family="UNKNOWN_NEW_SOURCE"),),
                claim_provenance=PROVENANCE,
                claim_eligibility_decisions=ELIGIBILITY,
            )

    def test_unknown_temporal_scope_is_hard_error_not_zero_credit(self) -> None:
        with self.assertRaisesRegex(
            ScoringContractIncompleteError,
            "SCORING_CONTRACT_INCOMPLETE:temporal_scope_caps:UNKNOWN_PERIOD",
        ):
            ImpactValidator().validate(
                impacts=(_impact(temporal_scope="UNKNOWN_PERIOD"),),
                claim_provenance=PROVENANCE,
                claim_eligibility_decisions=ELIGIBILITY,
            )

    def test_missing_support_type_policy_has_explicit_contract_error(self) -> None:
        policy = load_scoring_policy_v2()
        policies = dict(policy.support_type_policies)
        policies.pop("DIRECT_ACTUAL")
        broken = replace(policy, support_type_policies=policies)
        with patch(
            "e2r.research_brain.scoring.impact_validator.load_scoring_policy_v2",
            return_value=broken,
        ), self.assertRaisesRegex(
            ScoringContractIncompleteError,
            "MISSING_SUPPORT_TYPE_POLICY",
        ):
            ImpactValidator().validate(
                impacts=(_impact(),),
                claim_provenance=PROVENANCE,
                claim_eligibility_decisions=ELIGIBILITY,
            )

    def test_missing_counter_effect_policy_has_explicit_contract_error(self) -> None:
        policy = load_scoring_policy_v2()
        directions = dict(policy.direction_policy_fields)
        directions.pop("COUNTER")
        broken = replace(policy, direction_policy_fields=directions)
        with patch(
            "e2r.research_brain.scoring.impact_validator.load_scoring_policy_v2",
            return_value=broken,
        ), self.assertRaisesRegex(
            ScoringContractIncompleteError,
            "MISSING_COUNTER_EFFECT_POLICY",
        ):
            ImpactValidator().validate(
                impacts=(
                    _impact(direction="COUNTER", support_type="RISK_OPEN"),
                ),
                claim_provenance=PROVENANCE,
                claim_eligibility_decisions=ELIGIBILITY,
            )


if __name__ == "__main__":
    unittest.main()
