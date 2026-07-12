from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path
from typing import Any, Mapping, Sequence

from e2r.research_brain.researcher_mode import (
    CANONICAL_COMPONENT_MAX_POINTS,
    CANONICAL_COMPONENT_ORDER,
    CLAIM_COMPONENT_IMPACT_MAPPING_SCHEMA,
    CLAIM_IMPACT_MAPPING_OUTPUT_FILE,
    CLAIM_UTILIZATION_STATUSES,
    EVIDENCE_FACT_GRAPH_OUTPUT_FILES,
    PHASE88_PASS,
    ClaimComponentImpactProposal,
    ClaimComponentImpactMapper,
    ClaimTerminalDisposition,
    ClaimUtilizationLedgerBuilder,
    ComponentResearchMemo,
    ComponentResearchResult,
    EvidenceFactCompiler,
    EvidenceFactGraphEngine,
    compile_phase88_evidence_fact_graph_audit,
    write_claim_impact_mapping_result,
    write_evidence_fact_graph_result,
)


TARGET = "CURRENT-TARGET"
AS_OF_DATE = "2026-06-29"
MECHANISM = "capacity allocation converts into durable earnings and cash flow"


class Phase88ImpactProvider:
    provider_name = "PHASE88_IMPACT_PROVIDER"

    def __init__(self, mode: str = "COMPLETE") -> None:
        self.mode = mode
        self.calls: list[Mapping[str, Any]] = []

    def complete(
        self, *, pass_name: str, payload: Mapping[str, Any]
    ) -> Mapping[str, Any]:
        self.calls.append({"pass_name": pass_name, "payload": payload})
        if self.mode == "ERROR":
            raise RuntimeError("impact mapper unavailable")
        if pass_name != "CLAIM_COMPONENT_IMPACT_MAPPING":
            raise AssertionError(pass_name)
        links = {
            row["claim_id"]: row
            for row in payload["claim_fact_links"]
            if row["link_role"] == "PRIMARY_FACT_CLAIM"
        }
        facts = {row["fact_id"]: row for row in payload["evidence_facts"]}
        support_link = links["CLAIM-SUPPORT"]
        profile_link = links["CLAIM-PROFILE"]
        unresolved = self.mode == "UNRESOLVED"
        return {
            "impact_proposals": [
                {
                    "claim_id": "CLAIM-SUPPORT",
                    "fact_id": support_link["fact_id"],
                    "component_id": "eps_fcf_explosion",
                    "direction": "SUPPORT",
                    "component_mechanism_id": "EARNINGS_CONVERSION",
                    "fact_economic_mechanism": facts[
                        support_link["fact_id"]
                    ]["economic_mechanism"],
                    "proposed_credit_units": 0.7,
                    "rationale": "component memo and fact share earnings conversion",
                }
            ],
            "non_scoring_dispositions": (
                []
                if unresolved
                else [
                    {
                        "claim_id": "CLAIM-PROFILE",
                        "fact_id": profile_link["fact_id"],
                        "status": "PROFILE_ONLY",
                        "rationale": "profile context has no direct component mechanism",
                        "component_ids": [],
                    }
                ]
            ),
            "mapping_complete": not unresolved,
            "unresolved_claim_ids": (
                ["CLAIM-PROFILE"] if unresolved else []
            ),
            "rationale": "all primary material claims were reviewed",
        }


class E2RV5EvidenceFactGraphTests(unittest.TestCase):
    ROOT = Path(__file__).resolve().parents[1]

    def test_phase88_audit_is_reproducible_and_complete(self) -> None:
        actual = compile_phase88_evidence_fact_graph_audit(self.ROOT)
        committed = json.loads(
            (
                self.ROOT
                / "docs/operational/e2r_v5_evidence_fact_graph_claim_utilization_audit.json"
            ).read_text(encoding="utf-8")
        )
        self.assertEqual(actual, committed)
        self.assertEqual(actual["status"], PHASE88_PASS)
        self.assertEqual(actual["critical_count_sum"], 0)
        self.assertEqual(
            set(actual["claim_utilization_statuses"]),
            set(CLAIM_UTILIZATION_STATUSES),
        )

    def test_llm_mapper_closes_primary_claims_and_graph_builder_reuses_facts(self) -> None:
        claims = (*_claims()[:3], _claims()[4])
        compilation = EvidenceFactCompiler().compile(
            target_id=TARGET,
            as_of_date=AS_OF_DATE,
            accepted_claims=claims,
        )
        provider = Phase88ImpactProvider()
        mapping = ClaimComponentImpactMapper(provider=provider).map(
            fact_compilation=compilation,
            component_results=_component_results(compilation),
        )
        self.assertEqual(mapping.status, "COMPLETE")
        self.assertEqual(len(mapping.impact_proposals), 1)
        self.assertEqual(len(mapping.explicit_dispositions), 1)
        result = EvidenceFactGraphEngine().build(
            target_id=TARGET,
            as_of_date=AS_OF_DATE,
            fact_compilation=compilation,
            impact_proposals=mapping.impact_proposals,
            explicit_dispositions=mapping.explicit_dispositions,
        )
        self.assertEqual(result.status, "EVIDENCE_FACT_GRAPH_COMPLETE")
        payload = provider.calls[0]["payload"]
        self.assertFalse(payload["question_family_score_gateway"])
        self.assertFalse(payload["primitive_score_gateway"])

    def test_llm_mapper_provider_error_or_unresolved_claim_stays_pending(self) -> None:
        claims = (*_claims()[:3], _claims()[4])
        compilation = EvidenceFactCompiler().compile(
            target_id=TARGET,
            as_of_date=AS_OF_DATE,
            accepted_claims=claims,
        )
        components = _component_results(compilation)
        for provider in (
            Phase88ImpactProvider("ERROR"),
            Phase88ImpactProvider("UNRESOLVED"),
        ):
            mapping = ClaimComponentImpactMapper(provider=provider).map(
                fact_compilation=compilation,
                component_results=components,
            )
            self.assertEqual(mapping.status, "PENDING")
            self.assertFalse(mapping.mapping_complete)
            self.assertTrue(mapping.unresolved_claim_ids)
            self.assertNotIn("suggested_queries", mapping.to_score_gap_context())

    def test_llm_mapper_rejects_schema_shaped_but_non_string_semantics(self) -> None:
        class InvalidSemanticProvider(Phase88ImpactProvider):
            def complete(self, **kwargs):
                response = dict(super().complete(**kwargs))
                response["rationale"] = None
                return response

        claims = (*_claims()[:3], _claims()[4])
        compilation = EvidenceFactCompiler().compile(
            target_id=TARGET,
            as_of_date=AS_OF_DATE,
            accepted_claims=claims,
        )
        mapping = ClaimComponentImpactMapper(
            provider=InvalidSemanticProvider()
        ).map(
            fact_compilation=compilation,
            component_results=_component_results(compilation),
        )
        self.assertEqual(mapping.status, "PENDING")
        self.assertIn("TypeError", mapping.pending_reasons[0])

    def test_llm_mapper_result_writer_emits_reproducible_leaf(self) -> None:
        claims = (*_claims()[:3], _claims()[4])
        compilation = EvidenceFactCompiler().compile(
            target_id=TARGET,
            as_of_date=AS_OF_DATE,
            accepted_claims=claims,
        )
        mapping = ClaimComponentImpactMapper(
            provider=Phase88ImpactProvider()
        ).map(
            fact_compilation=compilation,
            component_results=_component_results(compilation),
        )
        with tempfile.TemporaryDirectory() as directory:
            path = write_claim_impact_mapping_result(mapping, directory)
            self.assertEqual(path.name, CLAIM_IMPACT_MAPPING_OUTPUT_FILE)
            self.assertEqual(
                json.loads(path.read_text(encoding="utf-8")),
                json.loads(json.dumps(mapping.to_dict())),
            )

    def test_impact_mapper_schema_has_no_score_or_stage_authority(self) -> None:
        self.assertIs(
            CLAIM_COMPONENT_IMPACT_MAPPING_SCHEMA["additionalProperties"],
            False,
        )
        self.assertFalse(
            {"score", "total_score", "stage", "final_stage"}
            & set(CLAIM_COMPONENT_IMPACT_MAPPING_SCHEMA["properties"])
        )

    def test_all_material_claims_end_in_exact_utilization_roster(self) -> None:
        result = _complete_graph()
        self.assertEqual(result.status, "EVIDENCE_FACT_GRAPH_COMPLETE")
        self.assertTrue(result.ready_for_component_scoring_memos)
        statuses = {
            row.status for row in result.claim_utilization.utilization_decisions
        }
        self.assertEqual(statuses, set(CLAIM_UTILIZATION_STATUSES))
        self.assertEqual(result.audit["critical_count_sum"], 0)
        self.assertEqual(
            result.fact_compilation.input_claim_count,
            len(_claims()),
        )

    def test_same_economic_fact_gets_one_fact_and_independent_confidence_gain(self) -> None:
        compilation = EvidenceFactCompiler().compile(
            target_id=TARGET,
            as_of_date=AS_OF_DATE,
            accepted_claims=_claims()[:3],
        )
        self.assertEqual(len(compilation.facts), 1)
        self.assertEqual(compilation.duplicate_fact_merge_count, 2)
        fact = compilation.facts[0]
        self.assertAlmostEqual(fact.confidence, 0.98)
        roles = {
            row.claim_id: row.link_role for row in compilation.claim_fact_links
        }
        self.assertEqual(roles["CLAIM-SUPPORT"], "PRIMARY_FACT_CLAIM")
        self.assertEqual(roles["CLAIM-CORROBORATION"], "INDEPENDENT_CORROBORATION")
        self.assertEqual(roles["CLAIM-DUPLICATE"], "SAME_GROUP_DUPLICATE")
        self.assertEqual(
            set(fact.question_family_tags),
            {"earnings_quality", "visibility_quality"},
        )
        self.assertEqual(
            set(fact.primitive_tags),
            {"capacity_allocation", "cash_conversion"},
        )

    def test_same_source_id_cannot_fake_an_independent_confidence_gain(self) -> None:
        claims = (
            _claim(
                "CLAIM-SOURCE-A",
                source_id="SAME-SOURCE",
                independence_group="ISSUER",
                confidence=0.8,
            ),
            _claim(
                "CLAIM-SOURCE-B",
                source_id="SAME-SOURCE",
                independence_group="INDEPENDENT-LABEL-ONLY",
                confidence=0.7,
            ),
        )
        compilation = EvidenceFactCompiler().compile(
            target_id=TARGET,
            as_of_date=AS_OF_DATE,
            accepted_claims=claims,
        )
        self.assertAlmostEqual(compilation.facts[0].confidence, 0.8)
        self.assertEqual(
            len(compilation.facts[0].corroborating_independence_groups),
            1,
        )
        self.assertEqual(
            {row.link_role for row in compilation.claim_fact_links},
            {"PRIMARY_FACT_CLAIM", "SAME_GROUP_DUPLICATE"},
        )

    def test_one_claim_can_feed_multiple_components_but_total_credit_is_capped(self) -> None:
        claims = _claims()[:3]
        compilation = EvidenceFactCompiler().compile(
            target_id=TARGET,
            as_of_date=AS_OF_DATE,
            accepted_claims=claims,
        )
        fact = compilation.facts[0]
        proposals = (
            _impact(
                "IMPACT-EPS",
                "CLAIM-SUPPORT",
                fact.fact_id,
                "eps_fcf_explosion",
                "SUPPORT",
                "EARNINGS_CONVERSION",
                fact.economic_mechanism,
                0.8,
            ),
            _impact(
                "IMPACT-VISIBILITY",
                "CLAIM-SUPPORT",
                fact.fact_id,
                "earnings_visibility",
                "SUPPORT",
                "REVENUE_VISIBILITY",
                fact.economic_mechanism,
                0.8,
            ),
        )
        ledger = ClaimUtilizationLedgerBuilder().build(
            fact_compilation=compilation,
            impact_proposals=proposals,
        )
        self.assertEqual(ledger.status, "CLAIM_UTILIZATION_COMPLETE")
        self.assertEqual(
            {row.component_id for row in ledger.validated_impacts},
            {"eps_fcf_explosion", "earnings_visibility"},
        )
        self.assertAlmostEqual(
            sum(row.validated_credit_units for row in ledger.validated_impacts),
            1.0,
        )
        self.assertTrue(all(row.claim_cap_scaled for row in ledger.validated_impacts))
        self.assertFalse(
            any(row.production_points_authority for row in ledger.validated_impacts)
        )

    def test_corroborating_or_same_group_duplicate_claim_cannot_score_again(self) -> None:
        claims = _claims()[:3]
        compilation = EvidenceFactCompiler().compile(
            target_id=TARGET,
            as_of_date=AS_OF_DATE,
            accepted_claims=claims,
        )
        fact = compilation.facts[0]
        ledger = ClaimUtilizationLedgerBuilder().build(
            fact_compilation=compilation,
            impact_proposals=(
                _impact(
                    "IMPACT-CORROBORATION",
                    "CLAIM-CORROBORATION",
                    fact.fact_id,
                    "information_confidence",
                    "SUPPORT",
                    "INDEPENDENT_CORROBORATION",
                    fact.economic_mechanism,
                    0.5,
                ),
                _impact(
                    "IMPACT-DUPLICATE",
                    "CLAIM-DUPLICATE",
                    fact.fact_id,
                    "eps_fcf_explosion",
                    "SUPPORT",
                    "EARNINGS_CONVERSION",
                    fact.economic_mechanism,
                    0.5,
                ),
            ),
            explicit_dispositions=(
                ClaimTerminalDisposition(
                    disposition_id="DISPOSITION-PRIMARY",
                    claim_id="CLAIM-SUPPORT",
                    fact_id=fact.fact_id,
                    status="PROFILE_ONLY",
                    rationale="primary fact is retained for profile in this canary",
                ),
            ),
        )
        self.assertEqual(ledger.validated_impacts, ())
        self.assertEqual(
            {row.reason for row in ledger.rejected_impacts},
            {"CORROBORATION_OR_DUPLICATE_CANNOT_SCORE_AGAIN"},
        )
        status_by_claim = {
            row.claim_id: row.status for row in ledger.utilization_decisions
        }
        self.assertEqual(status_by_claim["CLAIM-CORROBORATION"], "CONFIDENCE_ONLY")
        self.assertEqual(status_by_claim["CLAIM-DUPLICATE"], "DUPLICATE_FACT")

    def test_wrong_component_mechanism_is_terminal_but_never_scored(self) -> None:
        claim = _claim(
            "CLAIM-WRONG",
            predicate="wrong_mechanism_fact",
            value="profile",
        )
        compilation = EvidenceFactCompiler().compile(
            target_id=TARGET,
            as_of_date=AS_OF_DATE,
            accepted_claims=(claim,),
        )
        fact = compilation.facts[0]
        ledger = ClaimUtilizationLedgerBuilder().build(
            fact_compilation=compilation,
            impact_proposals=(
                _impact(
                    "IMPACT-WRONG",
                    "CLAIM-WRONG",
                    fact.fact_id,
                    "valuation_rerating",
                    "SUPPORT",
                    "EARNINGS_CONVERSION",
                    fact.economic_mechanism,
                    0.7,
                ),
            ),
        )
        self.assertEqual(ledger.validated_impacts, ())
        self.assertEqual(ledger.rejected_impacts[0].reason, "WRONG_COMPONENT_MECHANISM")
        self.assertEqual(ledger.utilization_decisions[0].status, "WRONG_MECHANISM")
        self.assertTrue(ledger.ready_for_component_scoring_memos)

    def test_material_claim_without_use_is_visible_and_blocks_readiness(self) -> None:
        compilation = EvidenceFactCompiler().compile(
            target_id=TARGET,
            as_of_date=AS_OF_DATE,
            accepted_claims=(
                _claim(
                    "CLAIM-UNACCOUNTED",
                    predicate="unaccounted_material_fact",
                    value=1,
                ),
            ),
        )
        ledger = ClaimUtilizationLedgerBuilder().build(
            fact_compilation=compilation,
            impact_proposals=(),
        )
        self.assertEqual(ledger.status, "CLAIM_UTILIZATION_PENDING")
        self.assertEqual(
            ledger.audit["critical_counts"][
                "material_claim_without_terminal_utilization_count"
            ],
            1,
        )
        self.assertEqual(
            ledger.utilization_decisions[0].status,
            "REJECTED_WITH_REASON",
        )
        self.assertIn(
            "MATERIAL_CLAIM_UTILIZATION_MISSING",
            ledger.utilization_decisions[0].rationale,
        )

    def test_accepted_future_claim_cannot_disappear_or_become_a_fact(self) -> None:
        claim = {
            **_claim(
                "CLAIM-FUTURE",
                predicate="future_fact",
                value=1,
            ),
            "published_at": "2026-06-30",
        }
        result = EvidenceFactGraphEngine().compile(
            target_id=TARGET,
            as_of_date=AS_OF_DATE,
            material_claims=(claim,),
            impact_proposals=(),
        )
        self.assertEqual(result.status, "EVIDENCE_FACT_GRAPH_PENDING")
        self.assertEqual(result.facts, ())
        self.assertEqual(
            result.fact_compilation.accepted_claim_without_fact_count,
            1,
        )
        decision = result.claim_utilization.utilization_decisions[0]
        self.assertEqual(decision.status, "REJECTED_WITH_REASON")
        self.assertEqual(decision.rationale, "FUTURE_SOURCE_LEAKAGE")

    def test_empty_fact_compilation_cannot_be_relabelled_to_another_target(self) -> None:
        compilation = EvidenceFactCompiler().compile(
            target_id=TARGET,
            as_of_date=AS_OF_DATE,
            accepted_claims=(),
        )
        with self.assertRaisesRegex(ValueError, "target/as_of mismatch"):
            EvidenceFactGraphEngine().build(
                target_id="ANOTHER-TARGET",
                as_of_date=AS_OF_DATE,
                fact_compilation=compilation,
                impact_proposals=(),
            )

    def test_question_family_and_primitive_tags_are_metadata_not_gateways(self) -> None:
        result = _complete_graph()
        fact = next(
            row
            for row in result.facts
            if "capacity_allocation" in row.primitive_tags
        )
        self.assertIn("earnings_quality", fact.question_family_tags)
        self.assertEqual(
            result.audit["critical_counts"][
                "question_or_primitive_tag_score_gateway_count"
            ],
            0,
        )
        views = result.component_fact_views()
        self.assertFalse(views["eps_fcf_explosion"]["question_family_score_gateway"])
        self.assertFalse(views["eps_fcf_explosion"]["primitive_score_gateway"])

    def test_fact_compilation_and_graph_are_order_stable(self) -> None:
        claims = _claims()[:3]
        forward = EvidenceFactCompiler().compile(
            target_id=TARGET,
            as_of_date=AS_OF_DATE,
            accepted_claims=claims,
        )
        reverse = EvidenceFactCompiler().compile(
            target_id=TARGET,
            as_of_date=AS_OF_DATE,
            accepted_claims=tuple(reversed(claims)),
        )
        self.assertEqual(
            [row.to_dict() for row in forward.facts],
            [row.to_dict() for row in reverse.facts],
        )
        self.assertEqual(
            [row.to_dict() for row in forward.claim_fact_links],
            [row.to_dict() for row in reverse.claim_fact_links],
        )

    def test_writer_emits_exact_fact_graph_leaf_files(self) -> None:
        result = _complete_graph()
        with tempfile.TemporaryDirectory() as directory:
            paths = write_evidence_fact_graph_result(result, directory)
            self.assertEqual(set(paths), set(EVIDENCE_FACT_GRAPH_OUTPUT_FILES))
            self.assertTrue(all(path.is_file() for path in paths.values()))
            audit = json.loads(paths["audit"].read_text(encoding="utf-8"))
            self.assertEqual(audit, result.audit)
            utilization_rows = [
                json.loads(line)
                for line in paths["claim_utilization"]
                .read_text(encoding="utf-8")
                .splitlines()
            ]
            self.assertEqual(
                {row["status"] for row in utilization_rows},
                set(CLAIM_UTILIZATION_STATUSES),
            )


def _component_results(compilation) -> tuple[ComponentResearchResult, ...]:
    support_fact_id = next(
        row.fact_id
        for row in compilation.claim_fact_links
        if row.claim_id == "CLAIM-SUPPORT"
    )
    rows = []
    for component_id in CANONICAL_COMPONENT_ORDER:
        maximum = float(CANONICAL_COMPONENT_MAX_POINTS[component_id])
        supports = (
            (support_fact_id,) if component_id == "eps_fcf_explosion" else ()
        )
        midpoint = maximum * 0.4 if supports else 0.0
        memo = ComponentResearchMemo(
            memo_id=f"MAPPER-MEMO-{component_id}",
            target_id=TARGET,
            archetype_id="CURRENT-ARCHETYPE",
            component_id=component_id,
            component_max_points=maximum,
            positive_fact_ids=supports,
            counter_fact_ids=(),
            resolution_fact_ids=(),
            structured_metrics=({"current_metric": 1.0} if supports else {}),
            historical_anchor_ids=(),
            researcher_summary="current facts reviewed for component mechanism mapping",
            positive_case="source-backed positive mechanism was reviewed",
            counter_case="counter mechanism was independently reviewed",
            uncertainties=(),
            source_coverage=("ISSUER_PRESENTATION",),
            proposed_score_lower=midpoint,
            proposed_score_mid=midpoint,
            proposed_score_upper=midpoint,
            confidence=0.8,
            research_complete=True,
            nearest_positive_anchor_ids=(),
            nearest_counter_anchor_ids=(),
            why_not_higher="bounded by current evidence",
            why_not_lower="direct fact lineage exists" if supports else "no direct support",
            researcher_role=f"MAPPER-{component_id}",
        )
        rows.append(
            ComponentResearchResult(
                component_id=component_id,
                researcher_role=memo.researcher_role,
                status="COMPLETE",
                memo=memo,
                pending_reasons=(),
                provider_name="PHASE88_COMPONENT_FIXTURE",
                prompt_hash=f"MAPPER-PROMPT-{component_id}",
            )
        )
    return tuple(rows)


def _complete_graph():
    claims = _claims()
    compilation = EvidenceFactCompiler().compile(
        target_id=TARGET,
        as_of_date=AS_OF_DATE,
        accepted_claims=claims,
    )
    fact_by_claim = {
        link.claim_id: next(
            fact for fact in compilation.facts if fact.fact_id == link.fact_id
        )
        for link in compilation.claim_fact_links
    }
    support = fact_by_claim["CLAIM-SUPPORT"]
    counter = fact_by_claim["CLAIM-COUNTER"]
    wrong = fact_by_claim["CLAIM-WRONG"]
    proposals = (
        _impact(
            "IMPACT-EPS",
            "CLAIM-SUPPORT",
            support.fact_id,
            "eps_fcf_explosion",
            "SUPPORT",
            "EARNINGS_CONVERSION",
            support.economic_mechanism,
            0.8,
        ),
        _impact(
            "IMPACT-VISIBILITY",
            "CLAIM-SUPPORT",
            support.fact_id,
            "earnings_visibility",
            "SUPPORT",
            "REVENUE_VISIBILITY",
            support.economic_mechanism,
            0.8,
        ),
        _impact(
            "IMPACT-COUNTER",
            "CLAIM-COUNTER",
            counter.fact_id,
            "earnings_visibility",
            "COUNTER",
            "CONTRACT_DURABILITY",
            counter.economic_mechanism,
            0.6,
        ),
        _impact(
            "IMPACT-WRONG",
            "CLAIM-WRONG",
            wrong.fact_id,
            "valuation_rerating",
            "SUPPORT",
            "EARNINGS_CONVERSION",
            wrong.economic_mechanism,
            0.5,
        ),
    )
    profile_fact = fact_by_claim["CLAIM-PROFILE"]
    return EvidenceFactGraphEngine().compile(
        target_id=TARGET,
        as_of_date=AS_OF_DATE,
        material_claims=claims,
        impact_proposals=proposals,
        explicit_dispositions=(
            ClaimTerminalDisposition(
                disposition_id="DISPOSITION-PROFILE",
                claim_id="CLAIM-PROFILE",
                fact_id=profile_fact.fact_id,
                status="PROFILE_ONLY",
                rationale="business profile only; no component credit",
            ),
        ),
    )


def _claims() -> tuple[Mapping[str, Any], ...]:
    support = _claim(
        "CLAIM-SUPPORT",
        source_id="SOURCE-ISSUER-1",
        independence_group="ISSUER",
        confidence=0.9,
        question_tags=("earnings_quality",),
        primitive_tags=("capacity_allocation",),
    )
    corroboration = _claim(
        "CLAIM-CORROBORATION",
        source_id="SOURCE-INDEPENDENT-1",
        independence_group="INDEPENDENT",
        confidence=0.8,
        question_tags=("visibility_quality",),
        primitive_tags=("cash_conversion",),
    )
    duplicate = _claim(
        "CLAIM-DUPLICATE",
        source_id="SOURCE-ISSUER-2",
        independence_group="ISSUER",
        confidence=0.7,
    )
    counter = _claim(
        "CLAIM-COUNTER",
        predicate="customer_reopen_risk",
        value=True,
        direction="COUNTER",
        economic_mechanism="customer cancellation can weaken earnings durability",
    )
    profile = _claim(
        "CLAIM-PROFILE",
        predicate="product_profile",
        value="current product",
        economic_mechanism="product profile describes the business without direct score credit",
    )
    wrong = _claim(
        "CLAIM-WRONG",
        predicate="adjacent_mechanism",
        value=True,
        economic_mechanism="adjacent industry activity does not prove issuer valuation rerating",
    )
    superseded = _claim(
        "CLAIM-SUPERSEDED",
        predicate="old_guidance",
        value=100,
        current_lifecycle="SUPERSEDED",
        economic_mechanism="old guidance was replaced by a newer current statement",
    )
    rejected = {
        **_claim(
            "CLAIM-REJECTED",
            predicate="unaccepted_material_assertion",
            value=True,
        ),
        "accepted_by_evidence_os": False,
        "status": "REJECTED",
    }
    return (
        support,
        corroboration,
        duplicate,
        counter,
        profile,
        wrong,
        superseded,
        rejected,
    )


def _claim(
    claim_id: str,
    *,
    predicate: str = "allocation_confirmed",
    value: Any = 1,
    direction: str = "POSITIVE",
    current_lifecycle: str = "CURRENT",
    economic_mechanism: str = MECHANISM,
    source_id: str | None = None,
    independence_group: str = "ISSUER",
    confidence: float = 0.8,
    question_tags: Sequence[str] = (),
    primitive_tags: Sequence[str] = (),
) -> Mapping[str, Any]:
    return {
        "claim_id": claim_id,
        "accepted_by_evidence_os": True,
        "target_id": TARGET,
        "as_of_date": AS_OF_DATE,
        "subject": "current target business",
        "business_segment": "core segment",
        "product_family": "core product",
        "economic_mechanism": economic_mechanism,
        "predicate": predicate,
        "value": value,
        "unit": "flag",
        "period": "2026Q2",
        "direction": direction,
        "current_lifecycle": current_lifecycle,
        "confidence": confidence,
        "source_id": source_id or f"SOURCE-{claim_id}",
        "source_independence_group": independence_group,
        "published_at": "2026-06-20",
        "exact_quote": f"source-backed quote for {claim_id}",
        "question_family_tags": list(question_tags),
        "primitive_tags": list(primitive_tags),
        "material": True,
    }


def _impact(
    impact_id: str,
    claim_id: str,
    fact_id: str,
    component_id: str,
    direction: str,
    component_mechanism_id: str,
    fact_economic_mechanism: str,
    credit: float,
) -> ClaimComponentImpactProposal:
    return ClaimComponentImpactProposal(
        impact_id=impact_id,
        claim_id=claim_id,
        fact_id=fact_id,
        component_id=component_id,
        direction=direction,
        component_mechanism_id=component_mechanism_id,
        fact_economic_mechanism=fact_economic_mechanism,
        proposed_credit_units=credit,
        rationale="component-specific economic mechanism is explicitly proposed",
    )


if __name__ == "__main__":
    unittest.main()
