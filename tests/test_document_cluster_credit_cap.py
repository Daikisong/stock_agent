from __future__ import annotations

import unittest

from e2r.research_brain.scoring import (
    ClaimImpactProposal,
    ImpactValidator,
    ValidatedClaimImpact,
)


class DocumentClusterCreditCapTests(unittest.TestCase):
    def test_same_document_claim_fragments_do_not_stack_information_confidence(self) -> None:
        result = self._validate(
            rows=(
                ("C1", "M1", "I1", "memory_price_increase_mentioned", "ISSUER_OFFICIAL", "DOC-SAME", "FACT-ASP"),
                ("C2", "M2", "I2", "actual_earnings_conversion", "ISSUER_OFFICIAL", "DOC-SAME", "FACT-REVENUE"),
            )
        )
        self.assertEqual(len(result.document_clusters), 1)
        self.assertEqual(
            sum(item.validated_credit_fraction > 0 for item in result.impacts),
            1,
        )
        self.assertEqual(
            result.audit["suppressed_same_document_duplicate_count"], 1
        )
        self.assertEqual(
            result.audit["critical_counts"][
                "same_document_duplicate_credit_count"
            ],
            0,
        )

    def test_information_confidence_uses_best_source_plus_bounded_diversity(self) -> None:
        result = self._validate(
            rows=(
                ("C1", "M1", "I1", "memory_price_increase_mentioned", "ISSUER_OFFICIAL", "DOC-1", "FACT-1"),
                ("C2", "M2", "I2", "actual_earnings_conversion", "CUSTOMER_OFFICIAL", "DOC-2", "FACT-2"),
                ("C3", "M3", "I3", "shipment_or_revenue_mix", "TRUSTED_INDEPENDENT", "DOC-3", "FACT-3"),
            )
        )
        credited = [
            item.validated_credit_fraction
            for item in result.impacts
            if item.validated_credit_fraction > 0
        ]
        self.assertEqual(len(credited), 2)
        self.assertAlmostEqual(sum(credited), 0.8, places=6)
        self.assertGreaterEqual(
            result.audit["information_diversity_scaled_count"], 1
        )

    def _validate(self, *, rows):
        claims = []
        provenance = []
        eligibility = []
        impacts = []
        for claim_id, mapping_id, impact_id, primitive, source, document, fact in rows:
            claims.append(
                {
                    "claim_id": claim_id,
                    "target_id": "TARGET-X",
                    "accepted": True,
                    "mapping_ids": [mapping_id],
                    "economic_fact_key": fact,
                    "raw_assertion": {
                        "predicate": primitive,
                        "object_text": fact,
                    },
                }
            )
            provenance.append(
                {
                    "claim_id": claim_id,
                    "mapping_ids": [mapping_id],
                    "document_id": document,
                    "content_sha256": document,
                    "source_url": f"https://{document.casefold()}.example/full",
                    "source_proxy_only": False,
                    "directness": "DIRECT",
                    "temporal_status": "CURRENT",
                }
            )
            eligibility.append(
                {
                    "eligibility_decision_id": f"E-{claim_id}",
                    "claim_id": claim_id,
                    "component_scoring_eligibility": True,
                }
            )
            proposal = ClaimImpactProposal(
                impact_id=impact_id,
                claim_id=claim_id,
                mapping_id=mapping_id,
                target_id="TARGET-X",
                archetype_id="C06_HBM_MEMORY_CUSTOMER_CAPACITY",
                primitive_id=primitive,
                component_id="information_confidence",
                direction="SUPPORT",
                support_type="DIRECT_ACTUAL",
                strength_band="STRONG",
                completeness_band="SUBSTANTIAL",
                causal_distance="DIRECT",
                temporal_scope="CURRENT",
                source_family=source,
                evidence_family_id=f"F-{claim_id}",
                confidence=0.9,
                rationale="A distinct bounded source-backed fact.",
                unsupported_aspects=("No stronger effect is inferred.",),
            )
            impacts.append(
                ValidatedClaimImpact(
                    proposal,
                    scope_validation={
                        "status": "MECHANISM_SCOPE_PASS",
                        "scope_match": True,
                        "scope": {
                            "issuer_id": "TARGET-X",
                            "business_segment": "MEMORY",
                            "product_family": "HBM",
                            "economic_mechanism": "INFORMATION_ONLY",
                        },
                    },
                    eligibility_decision_id=f"E-{claim_id}",
                )
            )
        return ImpactValidator().validate(
            impacts=impacts,
            claim_provenance=provenance,
            claim_eligibility_decisions=eligibility,
            accepted_current_claims=claims,
        )


if __name__ == "__main__":
    unittest.main()
