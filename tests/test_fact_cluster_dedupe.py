from __future__ import annotations

import unittest

from e2r.research_brain.scoring import (
    ClaimImpactProposal,
    ImpactValidator,
    ValidatedClaimImpact,
)


def _scope(claim_id: str):
    del claim_id
    return {
        "status": "MECHANISM_SCOPE_PASS",
        "scope_match": True,
        "scope": {
            "issuer_id": "TARGET-X",
            "business_segment": "MEMORY",
            "product_family": "HBM",
            "economic_mechanism": "REALIZED_PRICING",
        },
    }


class FactClusterDedupeTests(unittest.TestCase):
    def test_same_economic_fact_across_claims_and_documents_gets_one_credit(self) -> None:
        claims = []
        provenance = []
        eligibility = []
        impacts = []
        for index, source in enumerate(
            ("ISSUER_OFFICIAL", "TRUSTED_INDEPENDENT"), start=1
        ):
            claim_id = f"C{index}"
            mapping_id = f"M{index}"
            claims.append(
                {
                    "claim_id": claim_id,
                    "target_id": "TARGET-X",
                    "accepted": True,
                    "mapping_ids": [mapping_id],
                    "economic_fact_key": "MEMORY_ASP_2026Q1_UP_146_PERCENT",
                    "reporting_period": "2026Q1",
                    "raw_assertion": {
                        "predicate": "memory average selling price changed",
                        "object_text": "memory ASP increased 146 percent",
                    },
                }
            )
            provenance.append(
                {
                    "claim_id": claim_id,
                    "mapping_ids": [mapping_id],
                    "document_id": f"D{index}",
                    "content_sha256": str(index) * 64,
                    "source_url": f"https://source{index}.example/fact",
                    "exact_quote": "Memory ASP increased 146 percent.",
                    "source_proxy_only": False,
                    "directness": "DIRECT",
                    "temporal_status": "CURRENT",
                }
            )
            eligibility.append(
                {
                    "eligibility_decision_id": f"E{index}",
                    "claim_id": claim_id,
                    "component_scoring_eligibility": True,
                }
            )
            proposal = ClaimImpactProposal(
                impact_id=f"I{index}",
                claim_id=claim_id,
                mapping_id=mapping_id,
                target_id="TARGET-X",
                archetype_id="C06_HBM_MEMORY_CUSTOMER_CAPACITY",
                primitive_id="memory_price_increase_mentioned",
                component_id="bottleneck_pricing",
                direction="SUPPORT",
                support_type="DIRECT_ACTUAL",
                strength_band="STRONG",
                completeness_band="SUBSTANTIAL",
                causal_distance="DIRECT",
                temporal_scope="CURRENT",
                source_family=source,
                evidence_family_id=f"F{index}",
                confidence=0.9,
                rationale="The same bounded realized pricing fact.",
                unsupported_aspects=("No allocation volume is established.",),
            )
            impacts.append(
                ValidatedClaimImpact(
                    proposal,
                    scope_validation=_scope(claim_id),
                    eligibility_decision_id=f"E{index}",
                )
            )
        result = ImpactValidator().validate(
            impacts=impacts,
            claim_provenance=provenance,
            claim_eligibility_decisions=eligibility,
            accepted_current_claims=claims,
        )
        self.assertEqual(result.status, "IMPACT_CREDIT_CAP_PASS")
        self.assertEqual(len(result.economic_fact_clusters), 1)
        self.assertEqual(
            sum(item.validated_credit_fraction > 0 for item in result.impacts),
            1,
        )
        self.assertEqual(
            sum(item.corroboration_only for item in result.impacts),
            1,
        )
        self.assertEqual(
            result.audit["suppressed_same_fact_duplicate_count"], 1
        )
        self.assertEqual(
            result.audit["critical_counts"][
                "same_fact_duplicate_credit_count"
            ],
            0,
        )


if __name__ == "__main__":
    unittest.main()
