from __future__ import annotations

import unittest
from types import SimpleNamespace

from e2r.research_brain.compiler.evidence_impact_rubric_compiler import compile_evidence_impact_rubrics
from e2r.research_brain.scoring import (
    CodexEvidenceImpactProvider,
    EvidenceImpactAdjudicator,
)
from e2r.research_brain.scoring.business_mechanism_scope import (
    infer_business_mechanism_scope,
)
from e2r.research_brain.scoring.evidence_impact_adjudicator import (
    compile_question_component_subcriteria,
)
from e2r.research_brain.scoring.question_impact_contract import (
    load_question_impact_contracts,
)


class FakeProvider:
    provider_name = "fake_test_only"
    def __init__(self, *, bad_key: str = "", skeptic: str = "APPROVE", omit_field: str = "") -> None:
        self.bad_key = bad_key; self.skeptic = skeptic; self.omit_field = omit_field; self.payloads = []
    def complete(self, *, pass_name, payload):
        self.payloads.append(payload)
        if pass_name == "IMPACT_SKEPTIC": return {"verdict":self.skeptic,"issues":[]}
        question = next(row for row in payload["question_impact_contracts"] if "actual_earnings_conversion" in row["allowed_primitive_ids"] and "information_confidence" in row["allowed_component_ids"])
        subcriterion = next(row for row in payload["component_subcriteria"]["information_confidence"] if row["question_family_id"] == question["question_family_id"])
        result = {"impacts":[{"mapping_id":"MAP-1","primitive_id":"actual_earnings_conversion","question_family_id":question["question_family_id"],"question_contract_hash":question["contract_hash"],"component_id":"information_confidence","component_subcriterion_id":subcriterion["subcriterion_id"],"mechanism_scope_match":payload["mechanism_scope_validation_by_component"]["information_confidence"]["scope_match"],"direction":"SUPPORT","support_type":"DIRECT_ACTUAL","strength_band":"STRONG","completeness_band":"SUBSTANTIAL","causal_distance":"DIRECT","temporal_scope":"CURRENT","source_family":"ISSUER_OFFICIAL","evidence_family_id":"FAM-1","confidence":0.9,"rationale":"Official actual result directly supports information confidence.","unsupported_aspects":["customer allocation is not established"],"counter_claim_ids":[]}],"unsupported_aspects":["customer allocation","pre-sold capacity"],"counter_thesis":["HBM attribution remains partial"],"reasoning_summary":"bounded impact only"}
        if self.omit_field:
            result["impacts"][0].pop(self.omit_field, None)
            if self.omit_field == "unsupported_aspects":
                result["unsupported_aspects"] = []
        if self.bad_key: result[self.bad_key] = 90 if self.bad_key == "total_score" else "3-Green"
        return result


class SchemaCaptureTransport:
    def __init__(self) -> None:
        self.output_schema = None
        self.prompt = ""

    def complete(self, *, prompt, output_schema, schema_name):
        self.prompt = prompt
        self.output_schema = output_schema
        return SimpleNamespace(
            payload={
                "impacts": [],
                "unsupported_aspects": ["no bounded impact"],
                "counter_thesis": [],
                "reasoning_summary": "No impact.",
            }
        )


class EvidenceImpactAdjudicatorTests(unittest.TestCase):
    def test_codex_schema_allows_required_semantic_impact_fields(self) -> None:
        transport = SchemaCaptureTransport()
        provider = CodexEvidenceImpactProvider(transport)  # type: ignore[arg-type]

        provider.complete(pass_name="IMPACT_PROPOSAL", payload={"claim": "x"})

        item = transport.output_schema["properties"]["impacts"]["items"]
        required = set(item["required"])
        properties = set(item["properties"])
        semantic_fields = {
            "question_family_id",
            "question_contract_hash",
            "component_subcriterion_id",
            "mechanism_scope_match",
        }
        self.assertTrue(semantic_fields <= required)
        self.assertTrue(semantic_fields <= properties)
        self.assertIn("same-document evidence", transport.prompt)
        self.assertIn("bounded PARTIAL_BRIDGE", transport.prompt)

    def test_skeptic_can_terminally_reject_invalid_mapping(self) -> None:
        provider = FakeProvider(skeptic="REJECT_MAPPING")
        result = self._run(provider)
        self.assertEqual(result.status, "IMPACT_MAPPING_REJECTED")
        self.assertEqual(result.proposals, ())

    def _run(self, provider):
        rubrics = compile_evidence_impact_rubrics("C06_HBM_MEMORY_CUSTOMER_CAPACITY")
        contracts = tuple(
            row
            for row in load_question_impact_contracts().values()
            if "actual_earnings_conversion" in row.allowed_primitive_ids
        )
        claim = {"claim_id":"CLM-1","target_id":"005930","mapping_ids":["MAP-1"],"score":99,"raw_assertion":{"predicate":"HBM memory actual earnings","object_text":"memory revenue and operating profit"}}
        return EvidenceImpactAdjudicator(provider).adjudicate(
            target_identity={"target_id":"005930","company":"삼성전자","stage":"3-Green"},
            as_of_date="2026-07-11", archetype_id="C06_HBM_MEMORY_CUSTOMER_CAPACITY",
            accepted_claim=claim,
            exact_quote="record revenue and operating profit with higher ASP",
            document_metadata={"source_url":"https://issuer.example/results","future_outcome":"hidden"},
            current_claim_ledger=(), counter_claims=(), rubrics=rubrics.rubrics,
            allowed_component_ids=("eps_fcf_explosion","earnings_visibility","bottleneck_pricing","market_mispricing","valuation_rerating","capital_allocation","information_confidence"),
            business_mechanism_scope=infer_business_mechanism_scope(claim,primitive_id="actual_earnings_conversion",archetype_id="C06_HBM_MEMORY_CUSTOMER_CAPACITY"),
            question_impact_contracts=contracts,
            claim_eligibility_decision={"eligibility_decision_id":"ELIG-1","claim_id":"CLM-1","component_scoring_eligibility":True},
            component_subcriteria=compile_question_component_subcriteria(contracts,allowed_component_ids=("eps_fcf_explosion","earnings_visibility","bottleneck_pricing","market_mispricing","valuation_rerating","capital_allocation","information_confidence")),
        )

    def test_two_pass_adjudicator_outputs_bands_without_score_or_stage(self) -> None:
        provider=FakeProvider(); result=self._run(provider)
        self.assertEqual(result.status,"IMPACT_ADJUDICATION_PASS")
        self.assertEqual(len(result.proposals),1); self.assertEqual(result.audit["provider_call_count"],2)
        serialized=str(provider.payloads).lower()
        self.assertNotIn("'stage':",serialized); self.assertNotIn("'score':",serialized); self.assertNotIn("future_outcome",serialized)
        payload = provider.payloads[0]
        self.assertIn("business_mechanism_scope", payload)
        self.assertIn("question_impact_contracts", payload)
        self.assertIn("claim_eligibility_decision", payload)
        self.assertIn("component_subcriteria", payload)
        self.assertIn("counter_claims", payload)

    def test_missing_scope_question_or_unsupported_aspect_is_hard_failure(self) -> None:
        cases = {
            "mechanism_scope_match": "impact_without_mechanism_scope_count",
            "question_contract_hash": "impact_without_question_contract_count",
            "unsupported_aspects": "impact_without_unsupported_aspects_count",
        }
        for field, counter in cases.items():
            with self.subTest(field=field):
                result = self._run(FakeProvider(omit_field=field))
                self.assertEqual(result.status, "IMPACT_ADJUDICATION_FAIL")
                self.assertGreater(result.audit["critical_counts"][counter], 0)
                self.assertEqual(
                    result.audit["critical_counts"][
                        "high_materiality_single_pass_count"
                    ],
                    1,
                )

    def test_unknown_skeptic_verdict_is_not_treated_as_approval(self) -> None:
        result = self._run(FakeProvider(skeptic="MAYBE"))
        self.assertEqual(result.status, "IMPACT_ADJUDICATION_FAIL")
        self.assertEqual(
            result.audit["critical_counts"]["skeptic_invalid_verdict_count"],
            1,
        )

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
