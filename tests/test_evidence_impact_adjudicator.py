from __future__ import annotations

import unittest

from e2r.research_brain.compiler.evidence_impact_rubric_compiler import compile_evidence_impact_rubrics
from e2r.research_brain.scoring import EvidenceImpactAdjudicator


class FakeProvider:
    provider_name = "fake_test_only"
    def __init__(self, *, bad_key: str = "", skeptic: str = "APPROVE") -> None:
        self.bad_key = bad_key; self.skeptic = skeptic; self.payloads = []
    def complete(self, *, pass_name, payload):
        self.payloads.append(payload)
        if pass_name == "IMPACT_SKEPTIC": return {"verdict":self.skeptic,"issues":[]}
        result = {"impacts":[{"mapping_id":"MAP-1","primitive_id":"actual_earnings_conversion","component_id":"information_confidence","direction":"SUPPORT","support_type":"DIRECT_ACTUAL","strength_band":"STRONG","completeness_band":"SUBSTANTIAL","causal_distance":"DIRECT","temporal_scope":"CURRENT","source_family":"ISSUER_OFFICIAL","evidence_family_id":"FAM-1","confidence":0.9,"rationale":"Official actual result directly supports information confidence.","unsupported_aspects":["customer allocation is not established"],"counter_claim_ids":[]}],"unsupported_aspects":["customer allocation","pre-sold capacity"],"counter_thesis":["HBM attribution remains partial"],"reasoning_summary":"bounded impact only"}
        if self.bad_key: result[self.bad_key] = 90 if self.bad_key == "total_score" else "3-Green"
        return result


class EvidenceImpactAdjudicatorTests(unittest.TestCase):
    def _run(self, provider):
        rubrics = compile_evidence_impact_rubrics("C06_HBM_MEMORY_CUSTOMER_CAPACITY")
        return EvidenceImpactAdjudicator(provider).adjudicate(
            target_identity={"target_id":"005930","company":"삼성전자","stage":"3-Green"},
            as_of_date="2026-07-11", archetype_id="C06_HBM_MEMORY_CUSTOMER_CAPACITY",
            accepted_claim={"claim_id":"CLM-1","target_id":"005930","mapping_ids":["MAP-1"],"score":99},
            exact_quote="record revenue and operating profit with higher ASP",
            document_metadata={"source_url":"https://issuer.example/results","future_outcome":"hidden"},
            current_claim_ledger=(), counter_claims=(), rubrics=rubrics.rubrics,
            allowed_component_ids=("eps_fcf_explosion","earnings_visibility","bottleneck_pricing","market_mispricing","valuation_rerating","capital_allocation","information_confidence"),
        )

    def test_two_pass_adjudicator_outputs_bands_without_score_or_stage(self) -> None:
        provider=FakeProvider(); result=self._run(provider)
        self.assertEqual(result.status,"IMPACT_ADJUDICATION_PASS")
        self.assertEqual(len(result.proposals),1); self.assertEqual(result.audit["provider_call_count"],2)
        serialized=str(provider.payloads).lower()
        self.assertNotIn("'stage':",serialized); self.assertNotIn("'score':",serialized); self.assertNotIn("future_outcome",serialized)

    def test_llm_score_key_is_validation_failure(self) -> None:
        result=self._run(FakeProvider(bad_key="total_score"))
        self.assertEqual(result.status,"IMPACT_ADJUDICATION_FAIL")
        self.assertEqual(result.audit["critical_counts"]["llm_final_score_key_count"],1)
        self.assertEqual(result.proposals,())

    def test_llm_stage_key_is_validation_failure(self) -> None:
        result=self._run(FakeProvider(bad_key="canonical_stage"))
        self.assertEqual(result.status,"IMPACT_ADJUDICATION_FAIL")
        self.assertEqual(result.audit["critical_counts"]["llm_stage_key_count"],1)

    def test_skeptic_conflict_becomes_review_pending(self) -> None:
        result=self._run(FakeProvider(skeptic="REVIEW_PENDING"))
        self.assertEqual(result.status,"REVIEW_PENDING"); self.assertEqual(result.proposals,())


if __name__ == "__main__": unittest.main()
