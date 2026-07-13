from __future__ import annotations

import inspect
import json
import unittest
from pathlib import Path
from typing import Any, Mapping

from e2r.research_brain.researcher_mode import (
    PHASE84_PASS,
    AnalystJudge,
    BusinessMechanismResearcher,
    CANONICAL_COMPONENT_ORDER,
    CalibrationJudge,
    CanonicalResearchDossierBuilder,
    ComponentResearchPlanner,
    DeterministicScoreAggregator,
    EPSFCFResearcher,
    EvidenceFact,
    EvidenceFactCompiler,
    MaterialDocumentRanker,
    RedTeamResearcher,
    SATURATION_REVIEW_ROLES,
    SaturationReview,
    SemanticSaturationCertifier,
    SkepticJudge,
    StructuredDataResearcher,
    SynthesisJudge,
    compile_phase84_researcher_mode_audit,
)
from e2r.research_brain.researcher_mode.component_researcher import (
    CodexResearcherProvider,
    _PROVIDER_SCHEMAS,
)


ARCHETYPE = "C06_HBM_MEMORY_CUSTOMER_CAPACITY"
TARGET = "CURRENT-TARGET"
AS_OF_DATE = "2026-06-29"


class ScriptedResearchProvider:
    provider_name = "SCRIPTED_RESEARCH_PROVIDER"

    def __init__(self, *, fail: bool = False, inject_stage: bool = False) -> None:
        self.fail = fail
        self.inject_stage = inject_stage
        self.calls: list[Mapping[str, Any]] = []

    def complete(
        self, *, pass_name: str, payload: Mapping[str, Any]
    ) -> Mapping[str, Any]:
        self.calls.append({"pass_name": pass_name, "payload": payload})
        if self.fail:
            raise RuntimeError("simulated provider outage")
        if pass_name == "BUSINESS_MODEL_RESEARCH":
            facts = _projected_fact_rows(payload)
            return {
                "business_model_summary": "설비와 고객 수요가 매출·현금 전환을 결정한다.",
                "revenue_engines": ["제품 출하와 가격"],
                "cost_and_cash_drivers": ["원가와 설비투자"],
                "capacity_and_supply_constraints": ["가용 생산능력"],
                "customer_and_channel_dependencies": ["고객 승인과 배정"],
                "fact_row_indices": [row["fact_row_index"] for row in facts],
                "uncertainties": [],
                "confidence": 0.8,
                "research_complete": True,
            }
        if pass_name == "COMPONENT_RESEARCH":
            facts = _projected_fact_rows(payload)
            positive = [
                row["fact_row_index"]
                for row in facts
                if row["direction"] == "POSITIVE"
            ]
            counter = [
                row["fact_row_index"]
                for row in facts
                if row["direction"] == "COUNTER"
            ]
            anchors = payload["historical_component_anchors"]
            positive_anchors = [row["anchor_id"] for row in anchors if row["role"] == "POSITIVE"]
            counter_anchors = [row["anchor_id"] for row in anchors if row["role"] == "COUNTER"]
            maximum = float(payload["component_max_points"])
            response: dict[str, Any] = {
                "positive_fact_row_indices": positive[:1],
                "counter_fact_row_indices": counter[:1],
                "resolution_fact_row_indices": [],
                "structured_metric_ids": list(payload["structured_metrics"]),
                "historical_anchor_ids": [*positive_anchors[:1], *counter_anchors[:1]],
                "nearest_positive_anchor_ids": positive_anchors[:1],
                "nearest_counter_anchor_ids": counter_anchors[:1],
                "researcher_summary": "현재 사실과 반증을 경제적 메커니즘으로 비교했다.",
                "positive_case": "현재 직접 증거가 경제적 강도를 지지한다.",
                "counter_case": "반증 때문에 상단 점수는 아직 제한된다.",
                "uncertainties": [],
                "source_coverage": ["ISSUER_OFFICIAL"],
                "proposed_score_lower": maximum * 0.30,
                "proposed_score_mid": maximum * 0.55,
                "proposed_score_upper": maximum * 0.75,
                "why_not_higher": "반증과 추가 확인 항목이 남아 있다.",
                "why_not_lower": "직접적인 현재 사실과 source lineage가 있다.",
                "confidence": 0.75,
                "research_complete": True,
            }
            if self.inject_stage:
                response["stage"] = "3-Green"
            return response
        if pass_name == "RED_TEAM_RESEARCH":
            facts = _projected_fact_rows(payload)
            counters = [
                row["fact_row_index"]
                for row in facts
                if row["direction"] == "COUNTER"
            ]
            return {
                "reviewed_component_ids": [
                    row["component_id"] for row in payload["component_research_memos"]
                ],
                "challenged_fact_row_indices": counters[:1],
                "counter_fact_row_indices": counters[:1],
                "resolved_challenges": ["source와 lifecycle을 대조함"],
                "unresolved_challenges": [],
                "recommended_research_directions": [],
                "source_coverage": ["ISSUER_OFFICIAL"],
                "confidence": 0.7,
                "review_complete": True,
            }
        if pass_name == "SYNTHESIS_REVIEW":
            return {
                "component_memo_ids": [
                    row["memo_id"] for row in payload["component_research_memos"]
                ],
                "cross_component_support": ["매출·현금·가시성 연결"],
                "cross_component_tensions": ["긍정 사실과 반증 공존"],
                "unresolved_material_questions": [],
                "synthesis_summary": "7개 메모와 red team 결과를 함께 종합했다.",
                "confidence": 0.72,
                "synthesis_complete": True,
            }
        if pass_name in {
            "COMPONENT_ANALYST_JUDGE",
            "COMPONENT_SKEPTIC_JUDGE",
            "CALIBRATION_JUDGE",
        }:
            memo = payload["component_research_memo"]
            maximum = float(payload["component_max_points"])
            fraction = {
                "COMPONENT_ANALYST_JUDGE": 0.60,
                "COMPONENT_SKEPTIC_JUDGE": 0.50,
                "CALIBRATION_JUDGE": 0.55,
            }[pass_name]
            return {
                "anchor_comparisons": ["현재 사실은 중간~상단 앵커 사이"],
                "proposed_points": maximum * fraction,
                "allowed_range": [maximum * 0.40, maximum * 0.70],
                "rationale": "사실·반증·앵커를 함께 비교했다.",
                "disagreements": [],
                "support_fact_ids": list(memo["positive_fact_ids"]),
                "counter_fact_ids": list(memo["counter_fact_ids"]),
                "nearest_anchor_ids": list(memo["historical_anchor_ids"]),
                "why_not_higher": "반증이 남아 있다.",
                "why_not_lower": "직접 사실이 존재한다.",
            }
        raise AssertionError(pass_name)


class SchemaRecordingTransport:
    def __init__(self) -> None:
        self.output_schema: Mapping[str, Any] | None = None

    def complete(self, *, prompt, output_schema, schema_name):
        from e2r.research_brain.planning.provider_transport import (
            StructuredProviderResponse,
        )

        del prompt, schema_name
        self.output_schema = output_schema
        return StructuredProviderResponse(
            payload={
                "suggested_queries": [],
                "new_source_directions": [],
                "unresolved_research_notes": [],
            },
            raw_response="{}",
            stderr="",
            returncode=0,
        )


class E2RV5ResearcherModeTests(unittest.TestCase):
    ROOT = Path(__file__).resolve().parents[1]

    def setUp(self) -> None:
        self.facts = (
            _fact("FACT-POS", "POSITIVE", "CURRENT", primitive_tags=()),
            _fact("FACT-COUNTER", "COUNTER", "OPEN", predicate="customer_reopen_risk"),
        )
        self.anchors = tuple(
            anchor
            for component_id in CANONICAL_COMPONENT_ORDER
            for anchor in (
                _anchor(component_id, "POSITIVE"),
                _anchor(component_id, "COUNTER"),
            )
        )
        self.maxima = {
            "eps_fcf_explosion": 24.0,
            "earnings_visibility": 21.0,
            "bottleneck_pricing": 19.0,
            "market_mispricing": 15.0,
            "valuation_rerating": 12.0,
            "capital_allocation": 4.0,
            "information_confidence": 5.0,
        }

    def test_phase84_modules_and_ten_roles_are_committed_and_audited(self) -> None:
        audit = compile_phase84_researcher_mode_audit(self.ROOT)
        self.assertEqual(audit["status"], PHASE84_PASS)
        self.assertEqual(audit["critical_count_sum"], 0)
        self.assertEqual(len(audit["required_modules"]), 16)
        self.assertEqual(len(audit["researcher_roles"]), 10)
        committed = json.loads(
            (
                self.ROOT
                / "docs/operational/e2r_v5_researcher_mode_architecture_audit.json"
            ).read_text(encoding="utf-8")
        )
        self.assertEqual(committed, audit)

    def test_codex_researcher_schema_uses_supported_strict_json_subset(self) -> None:
        transport = SchemaRecordingTransport()
        provider = CodexResearcherProvider(transport=transport)  # type: ignore[arg-type]

        provider.complete(
            pass_name="SOURCE_QUERY_GENERATION",
            payload={"target_id": TARGET, "as_of_date": AS_OF_DATE},
        )

        self.assertIsNotNone(transport.output_schema)
        self.assertNotIn("uniqueItems", _recursive_keys(transport.output_schema))
        for pass_name, schema in _PROVIDER_SCHEMAS.items():
            with self.subTest(pass_name=pass_name):
                self.assertEqual(_open_schema_object_paths(schema), ())
                self.assertEqual(_object_property_requirement_gaps(schema), ())

    def test_component_research_resolves_metric_ids_to_immutable_input_values(self) -> None:
        provider = ScriptedResearchProvider()
        plans = ComponentResearchPlanner().plan(
            target_id=TARGET,
            archetype_id=ARCHETYPE,
            evidence_facts=self.facts,
            historical_anchors=self.anchors,
            research_seeds=(),
            component_max_points=self.maxima,
            structured_metric_requirements={
                key: (("FCF_ACTUALS",) if key == "eps_fcf_explosion" else ())
                for key in self.maxima
            },
        )
        business = BusinessMechanismResearcher(provider=provider).research(
            target_id=TARGET,
            archetype_id=ARCHETYPE,
            as_of_date=AS_OF_DATE,
            evidence_facts=self.facts,
            source_claims=[],
            source_documents=[],
            source_coverage=["ISSUER_OFFICIAL"],
        ).memo
        metric = {"value": 1250.0, "unit": "KRW_BN", "period": "2026Q2"}

        result = EPSFCFResearcher(provider=provider).research(
            plan=plans[0],
            business_model=business,  # type: ignore[arg-type]
            evidence_facts=self.facts,
            historical_anchors=self.anchors,
            source_coverage=["ISSUER_OFFICIAL"],
            structured_metrics={"FCF_ACTUALS": metric},
        )

        self.assertEqual(result.status, "COMPLETE")
        self.assertEqual(
            result.memo.structured_metrics,  # type: ignore[union-attr]
            {"FCF_ACTUALS": metric},
        )

    def test_planner_builds_seven_open_ended_plans_and_exposes_every_fact(self) -> None:
        plans = ComponentResearchPlanner().plan(
            target_id=TARGET,
            archetype_id=ARCHETYPE,
            evidence_facts=self.facts,
            historical_anchors=self.anchors,
            research_seeds=(),
            component_max_points=self.maxima,
            structured_metric_requirements={key: () for key in self.maxima},
        )
        self.assertEqual(tuple(row.component_id for row in plans), CANONICAL_COMPONENT_ORDER)
        self.assertEqual({row.researcher_role for row in plans}, {
            "EPSFCFResearcher",
            "EarningsVisibilityResearcher",
            "BottleneckPricingResearcher",
            "MarketExpectationResearcher",
            "ValuationResearcher",
            "CapitalAllocationResearcher",
            "InformationConfidenceResearcher",
        })
        for plan in plans:
            self.assertEqual(set(plan.candidate_fact_ids), {"FACT-POS", "FACT-COUNTER"})
            self.assertTrue(plan.research_questions)

    def test_component_research_accepts_material_fact_without_exact_primitive(self) -> None:
        provider = ScriptedResearchProvider()
        plan = self._plans()[0]
        business = BusinessMechanismResearcher(provider=provider).research(
            target_id=TARGET,
            archetype_id=ARCHETYPE,
            as_of_date=AS_OF_DATE,
            evidence_facts=self.facts,
            source_claims=[],
            source_documents=[],
            source_coverage=["ISSUER_OFFICIAL"],
        ).memo
        self.assertIsNotNone(business)
        result = EPSFCFResearcher(provider=provider).research(
            plan=plan,
            business_model=business,  # type: ignore[arg-type]
            evidence_facts=self.facts,
            historical_anchors=self.anchors,
            source_coverage=["ISSUER_OFFICIAL"],
        )
        self.assertEqual(result.status, "COMPLETE")
        self.assertGreater(result.memo.proposed_score_mid, 0)  # type: ignore[union-attr]
        self.assertEqual(self.facts[0].primitive_tags, ())

    def test_provider_payload_is_blind_and_contains_all_required_research_inputs(self) -> None:
        provider = ScriptedResearchProvider()
        builder = CanonicalResearchDossierBuilder(provider=provider, research_seeds=())
        dossier = builder.build(
            target_id=TARGET,
            archetype_id=ARCHETYPE,
            as_of_date=AS_OF_DATE,
            evidence_facts=self.facts,
            historical_anchors=self.anchors,
            source_claims=[{"claim_id": "C1", "future_outcome": "+90%"}],
            source_documents=[
                {
                    "document_id": "SRC-1",
                    "expected_score": 99,
                    "reported_stage": "3-Green",
                }
            ],
            source_coverage=["ISSUER_OFFICIAL"],
            structured_metrics_by_component={key: {} for key in self.maxima},
            component_max_points=self.maxima,
            structured_metric_requirements={key: () for key in self.maxima},
        )
        self.assertEqual(dossier.status, "RESEARCH_MEMOS_COMPLETE")
        self.assertEqual(len(dossier.component_results), 7)
        for call in provider.calls:
            keys = _recursive_keys(call["payload"])
            self.assertFalse(
                keys
                & {
                    "stage",
                    "reported_stage",
                    "expected_score",
                    "future_outcome",
                    "mfe",
                    "mae",
                    "total_score",
                }
            )
        component_payload = next(
            call["payload"]
            for call in provider.calls
            if call["pass_name"] == "COMPONENT_RESEARCH"
        )
        self.assertTrue(
            {
                "current_evidence_fact_graph",
                "current_counterfacts",
                "target_business_model",
                "historical_component_anchors",
                "source_coverage",
            }.issubset(component_payload)
        )

    def test_fabricated_fact_or_stage_output_becomes_pending_not_low_score(self) -> None:
        class FabricatingProvider(ScriptedResearchProvider):
            def complete(self, *, pass_name: str, payload: Mapping[str, Any]) -> Mapping[str, Any]:
                result = dict(super().complete(pass_name=pass_name, payload=payload))
                if pass_name == "COMPONENT_RESEARCH":
                    result["positive_fact_row_indices"] = [999_999]
                return result

        for provider in (FabricatingProvider(), ScriptedResearchProvider(inject_stage=True)):
            business = BusinessMechanismResearcher(provider=provider).research(
                target_id=TARGET,
                archetype_id=ARCHETYPE,
                as_of_date=AS_OF_DATE,
                evidence_facts=self.facts,
                source_claims=[],
                source_documents=[],
                source_coverage=["ISSUER_OFFICIAL"],
            ).memo
            result = EPSFCFResearcher(provider=provider).research(
                plan=self._plans()[0],
                business_model=business,  # type: ignore[arg-type]
                evidence_facts=self.facts,
                historical_anchors=self.anchors,
                source_coverage=["ISSUER_OFFICIAL"],
            )
            self.assertEqual(result.status, "PENDING")
            self.assertIsNone(result.memo)
            self.assertTrue(result.pending_reasons[0].startswith("INVALID_PROVIDER_OUTPUT"))

    def test_provider_outage_is_research_pending_without_score_or_stage(self) -> None:
        dossier = CanonicalResearchDossierBuilder(
            provider=ScriptedResearchProvider(fail=True), research_seeds=()
        ).build(
            target_id=TARGET,
            archetype_id=ARCHETYPE,
            as_of_date=AS_OF_DATE,
            evidence_facts=self.facts,
            historical_anchors=self.anchors,
            source_claims=[],
            source_documents=[],
            source_coverage=["ISSUER_OFFICIAL"],
            component_max_points=self.maxima,
            structured_metric_requirements={key: () for key in self.maxima},
        )
        self.assertEqual(dossier.status, "RESEARCH_PENDING")
        payload = dossier.to_dict()
        self.assertNotIn("total_score", payload)
        self.assertNotIn("stage", payload)

    def test_future_document_is_rejected_before_any_researcher_prompt(self) -> None:
        provider = ScriptedResearchProvider()
        with self.assertRaisesRegex(ValueError, "future source exposure"):
            BusinessMechanismResearcher(provider=provider).research(
                target_id=TARGET,
                archetype_id=ARCHETYPE,
                as_of_date=AS_OF_DATE,
                evidence_facts=self.facts,
                source_claims=[],
                source_documents=[
                    {"document_id": "FUTURE", "published_at": "2026-06-30"}
                ],
                source_coverage=["ISSUER_OFFICIAL"],
            )
        self.assertEqual(provider.calls, [])

    def test_three_judges_and_deterministic_aggregator_preserve_lineage(self) -> None:
        provider = ScriptedResearchProvider()
        business = BusinessMechanismResearcher(provider=provider).research(
            target_id=TARGET,
            archetype_id=ARCHETYPE,
            as_of_date=AS_OF_DATE,
            evidence_facts=self.facts,
            source_claims=[],
            source_documents=[],
            source_coverage=["ISSUER_OFFICIAL"],
        ).memo
        component = EPSFCFResearcher(provider=provider).research(
            plan=self._plans()[0],
            business_model=business,  # type: ignore[arg-type]
            evidence_facts=self.facts,
            historical_anchors=self.anchors,
            source_coverage=["ISSUER_OFFICIAL"],
        ).memo
        self.assertIsNotNone(component)
        decisions = tuple(
            judge.judge(
                memo=component,  # type: ignore[arg-type]
                evidence_facts=self.facts,
                historical_anchors=self.anchors,
            ).decision
            for judge in (
                AnalystJudge(provider=provider),
                SkepticJudge(provider=provider),
                CalibrationJudge(provider=provider),
            )
        )
        self.assertTrue(all(decisions))
        result = DeterministicScoreAggregator().aggregate_component(
            memo=component,  # type: ignore[arg-type]
            judge_decisions=decisions,  # type: ignore[arg-type]
            evidence_facts=self.facts,
            historical_anchors=self.anchors,
            expected_as_of_date=AS_OF_DATE,
        )
        self.assertEqual(result.status, "COMPLETE")
        self.assertEqual(len(result.decision.judge_ids), 3)  # type: ignore[union-attr]
        self.assertIn("FACT-POS", result.decision.fact_ids)  # type: ignore[union-attr]
        self.assertLessEqual(
            result.decision.final_points, result.decision.support_points  # type: ignore[union-attr]
        )

    def test_fact_compiler_dedupes_economics_and_rejects_future_source(self) -> None:
        base = {
            "accepted_by_evidence_os": True,
            "target_id": TARGET,
            "subject": "current business",
            "business_segment": "segment",
            "product_family": "product",
            "economic_mechanism": "capacity allocation converts into revenue",
            "predicate": "allocation_confirmed",
            "value": 1,
            "unit": "flag",
            "period": "2026Q2",
            "direction": "POSITIVE",
            "current_lifecycle": "CURRENT",
            "confidence": 0.8,
        }
        result = EvidenceFactCompiler().compile(
            target_id=TARGET,
            as_of_date=AS_OF_DATE,
            accepted_claims=[
                {
                    **base,
                    "claim_id": "C1",
                    "source_id": "S1",
                    "source_independence_group": "ISSUER",
                    "published_at": "2026-06-20",
                },
                {
                    **base,
                    "claim_id": "C2",
                    "source_id": "S2",
                    "source_independence_group": "INDEPENDENT",
                    "published_at": "2026-06-21",
                },
                {
                    **base,
                    "claim_id": "C3",
                    "source_id": "S3",
                    "source_independence_group": "FUTURE",
                    "published_at": "2026-06-30",
                },
            ],
        )
        self.assertEqual(len(result.facts), 1)
        self.assertEqual(result.duplicate_fact_merge_count, 1)
        self.assertEqual(set(result.facts[0].claim_ids), {"C1", "C2"})
        self.assertEqual(result.facts[0].primitive_tags, ())
        self.assertEqual(result.rejected_claims[0].reason, "FUTURE_SOURCE_LEAKAGE")

    def test_document_ranker_has_no_top_n_and_snippet_is_not_evidence(self) -> None:
        ranker = MaterialDocumentRanker()
        self.assertNotIn("top_n", inspect.signature(ranker.select_material).parameters)
        plans = self._plans()
        documents = [
            {
                "document_id": f"D{index}",
                "target_id": TARGET,
                "full_text": "현재 증거와 반증의 경제적 강도와 지속성을 조사한다",
                "source_tier": "ISSUER_OFFICIAL",
                "published_at": "2026-06-20",
            }
            for index in range(12)
        ]
        documents.append(
            {
                "document_id": "SNIPPET",
                "target_id": TARGET,
                "content": "현재 증거",
                "snippet_only": True,
            }
        )
        decisions = ranker.rank(
            target_id=TARGET,
            as_of_date=AS_OF_DATE,
            documents=documents,
            research_plans=plans,
        )
        self.assertEqual(len(ranker.select_material(decisions)), 12)
        snippet = next(row for row in decisions if row.document_id == "SNIPPET")
        self.assertFalse(snippet.evidence_eligible)

    def test_structured_connector_gap_is_pending_not_zero_score(self) -> None:
        result = StructuredDataResearcher().assess(
            target_id=TARGET,
            as_of_date=AS_OF_DATE,
            records=(),
            required_roles_by_component={"eps_fcf_explosion": ("CASH_CONVERSION",)},
        )
        self.assertEqual(result.status, "SOURCE_PENDING")
        self.assertEqual(
            result.missing_roles_by_component["eps_fcf_explosion"],
            ("CASH_CONVERSION",),
        )
        self.assertFalse(result.score_authority)

    def test_saturation_needs_three_independent_approvals(self) -> None:
        partial = SemanticSaturationCertifier().certify(
            [_saturation_review(SATURATION_REVIEW_ROLES[0])]
        )
        self.assertEqual(partial.status, "PENDING")
        complete = SemanticSaturationCertifier().certify(
            [_saturation_review(role) for role in SATURATION_REVIEW_ROLES]
        )
        self.assertEqual(complete.status, "CERTIFIED")
        self.assertTrue(complete.semantic_saturation_certified)

    def _plans(self):
        return ComponentResearchPlanner().plan(
            target_id=TARGET,
            archetype_id=ARCHETYPE,
            evidence_facts=self.facts,
            historical_anchors=self.anchors,
            research_seeds=(),
            component_max_points=self.maxima,
            structured_metric_requirements={key: () for key in self.maxima},
        )


def _fact(
    fact_id: str,
    direction: str,
    lifecycle: str,
    *,
    predicate: str = "capacity_allocation_confirmed",
    primitive_tags: tuple[str, ...] = (),
) -> EvidenceFact:
    return EvidenceFact(
        fact_id=fact_id,
        target_id=TARGET,
        as_of_date=AS_OF_DATE,
        subject="current target business",
        business_segment="core segment",
        product_family="core product",
        economic_mechanism="capacity and customer allocation convert into cash earnings",
        predicate=predicate,
        value=True,
        unit=None,
        period="2026Q2",
        direction=direction,
        source_ids=("SRC-1",),
        claim_ids=(f"CLAIM-{fact_id}",),
        quote_ids=(f"QUOTE-{fact_id}",),
        current_lifecycle=lifecycle,
        source_independence_group="ISSUER",
        confidence=0.8,
        primitive_tags=primitive_tags,
    )


def _anchor(component_id: str, role: str) -> Mapping[str, Any]:
    suffix = "P" if role == "POSITIVE" else "C"
    maximum = {
        "eps_fcf_explosion": 24.0,
        "earnings_visibility": 21.0,
        "bottleneck_pricing": 19.0,
        "market_mispricing": 15.0,
        "valuation_rerating": 12.0,
        "capital_allocation": 4.0,
        "information_confidence": 5.0,
    }[component_id]
    return {
        "anchor_id": f"ANCHOR-{component_id}-{suffix}",
        "archetype_id": ARCHETYPE,
        "component_id": component_id,
        "economic_fact_patterns": ["economic pattern"],
        "role": role,
        "score_band": "HIGH" if role == "POSITIVE" else "LOW",
        "points_lower": maximum * 0.3,
        "points_mid": maximum * 0.5,
        "points_upper": maximum * 0.7,
        "max_points": maximum,
        "confidence": "MEDIUM",
        "usable_as_exact_anchor": False,
        "usable_as_ordinal_anchor": True,
    }


def _recursive_keys(value: Any) -> set[str]:
    if isinstance(value, Mapping):
        return set(value) | {
            nested
            for item in value.values()
            for nested in _recursive_keys(item)
        }
    if isinstance(value, (list, tuple)):
        return {nested for item in value for nested in _recursive_keys(item)}
    return set()


def _projected_fact_rows(payload: Mapping[str, Any]) -> tuple[Mapping[str, Any], ...]:
    fields = payload["current_evidence_fact_projection"]["fact_fields"]
    return tuple(
        dict(zip(fields, row))
        for row in payload["current_evidence_fact_graph"]
    )


def _open_schema_object_paths(
    value: Any, path: tuple[str, ...] = ()
) -> tuple[str, ...]:
    paths: list[str] = []
    if isinstance(value, Mapping):
        if (
            value.get("type") == "object"
            and value.get("additionalProperties") is not False
        ):
            paths.append("/".join(path) or "<root>")
        for key, child in value.items():
            paths.extend(_open_schema_object_paths(child, (*path, str(key))))
    elif isinstance(value, (list, tuple)):
        for index, child in enumerate(value):
            paths.extend(_open_schema_object_paths(child, (*path, str(index))))
    return tuple(paths)


def _object_property_requirement_gaps(
    value: Any, path: tuple[str, ...] = ()
) -> tuple[str, ...]:
    gaps: list[str] = []
    if isinstance(value, Mapping):
        if value.get("type") == "object":
            properties = set((value.get("properties") or {}).keys())
            required = set(value.get("required") or ())
            if properties != required:
                gaps.append("/".join(path) or "<root>")
        for key, child in value.items():
            gaps.extend(_object_property_requirement_gaps(child, (*path, str(key))))
    elif isinstance(value, (list, tuple)):
        for index, child in enumerate(value):
            gaps.extend(
                _object_property_requirement_gaps(child, (*path, str(index)))
            )
    return tuple(gaps)


def _saturation_review(role: str) -> SaturationReview:
    return SaturationReview(
        review_id=f"REVIEW-{role}",
        reviewer_role=role,
        approve=True,
        seven_component_memos_complete=True,
        material_positive_routes_reviewed=True,
        counter_and_supersession_routes_checked=True,
        structured_data_complete=True,
        new_source_family_directions_reviewed=True,
        unresolved_material_questions=(),
        gold_critical_fact_miss_count=0,
        rationale="모든 semantic saturation 기준을 독립적으로 확인했다.",
    )


if __name__ == "__main__":
    unittest.main()
