from __future__ import annotations

import inspect
import json
import tempfile
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
    _project_prior_component_memo_context,
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
            selected = [*positive[:1], *counter[:1]]
            anchors = payload["historical_component_anchors"]
            positive_anchors = [row["anchor_id"] for row in anchors if row["role"] == "POSITIVE"]
            counter_anchors = [row["anchor_id"] for row in anchors if row["role"] == "COUNTER"]
            maximum = float(payload["component_max_points"])
            response: dict[str, Any] = {
                "selected_fact_row_indices": selected,
                "selected_fact_groundings": _selected_fact_groundings(
                    payload, selected
                ),
                "prior_fact_dispositions": [
                    {
                        "fact_row_index": row["fact_row_index"],
                        "disposition": (
                            "RETAIN"
                            if row["fact_row_index"]
                            in {*positive[:1], *counter[:1]}
                            else "OMIT"
                        ),
                        "reason": (
                            "현재 컴포넌트 근거로 계속 유효함"
                            if row["fact_row_index"]
                            in {*positive[:1], *counter[:1]}
                            else "이번 컴포넌트 점수의 직접 근거로는 약함"
                        ),
                    }
                    for row in payload["prior_component_memo_context"][
                        "current_fact_rows"
                    ]
                ],
                "structured_metric_row_indices": [
                    row["structured_metric_row_index"]
                    for row in payload["structured_metric_rows"]
                ],
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
        self.prompt: str | None = None
        self.call_count = 0

    def complete(self, *, prompt, output_schema, schema_name):
        from e2r.research_brain.planning.provider_transport import (
            StructuredProviderResponse,
        )

        del schema_name
        self.call_count += 1
        self.prompt = prompt
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


class FailingRecordingTransport:
    def __init__(self) -> None:
        self.call_count = 0

    def complete(self, *, prompt, output_schema, schema_name):
        del prompt, output_schema, schema_name
        self.call_count += 1
        raise RuntimeError("fixture provider failure")


class UsageLimitAfterOneTransport(SchemaRecordingTransport):
    def complete(self, *, prompt, output_schema, schema_name):
        if self.call_count:
            self.call_count += 1
            raise RuntimeError(
                "ERROR: You've hit your usage limit. "
                "try again at Aug 3rd, 2031 7:09 PM."
            )
        return super().complete(
            prompt=prompt,
            output_schema=output_schema,
            schema_name=schema_name,
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
        self.assertIsNotNone(transport.prompt)
        self.assertIn("if it is a loss-accounted profile", transport.prompt or "")
        self.assertNotIn(
            "decode source_claims.claims with source_claims.claim_fields",
            (transport.prompt or "").casefold(),
        )
        self.assertNotIn("uniqueItems", _recursive_keys(transport.output_schema))
        for pass_name, schema in _PROVIDER_SCHEMAS.items():
            with self.subTest(pass_name=pass_name):
                self.assertEqual(_open_schema_object_paths(schema), ())
                self.assertEqual(_object_property_requirement_gaps(schema), ())

    def test_codex_provider_reuses_only_exact_prompt_and_schema_checkpoint(
        self,
    ) -> None:
        with tempfile.TemporaryDirectory() as directory:
            payload = {"target_id": TARGET, "as_of_date": AS_OF_DATE}
            first_transport = SchemaRecordingTransport()
            first = CodexResearcherProvider(  # type: ignore[arg-type]
                transport=first_transport
            )
            first.configure_response_cache(directory)

            first.complete(pass_name="SOURCE_QUERY_GENERATION", payload=payload)
            first.complete(pass_name="SOURCE_QUERY_GENERATION", payload=payload)

            self.assertEqual(first_transport.call_count, 1)
            self.assertFalse(first.calls[0]["cache_hit"])
            self.assertTrue(first.calls[1]["cache_hit"])
            self.assertEqual(first.response_cache_audit()["cache_hit_count"], 1)

            resumed_transport = SchemaRecordingTransport()
            resumed = CodexResearcherProvider(  # type: ignore[arg-type]
                transport=resumed_transport
            )
            resumed.configure_response_cache(directory)
            resumed.complete(pass_name="SOURCE_QUERY_GENERATION", payload=payload)
            self.assertEqual(resumed_transport.call_count, 0)
            self.assertTrue(resumed.calls[-1]["cache_hit"])

            resumed.complete(
                pass_name="SOURCE_QUERY_GENERATION",
                payload={**payload, "as_of_date": "2026-06-30"},
            )
            self.assertEqual(resumed_transport.call_count, 1)
            self.assertFalse(resumed.calls[-1]["cache_hit"])

    def test_codex_provider_never_caches_failed_response(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            transport = FailingRecordingTransport()
            provider = CodexResearcherProvider(  # type: ignore[arg-type]
                transport=transport
            )
            provider.configure_response_cache(directory)
            for _ in range(2):
                with self.assertRaisesRegex(RuntimeError, "fixture provider failure"):
                    provider.complete(
                        pass_name="SOURCE_QUERY_GENERATION",
                        payload={"target_id": TARGET, "as_of_date": AS_OF_DATE},
                    )

            self.assertEqual(transport.call_count, 2)
            self.assertEqual(provider.response_cache_audit()["cache_hit_count"], 0)
            self.assertEqual(provider.response_cache_audit()["provider_error_count"], 2)
            self.assertEqual(list(Path(directory).glob("*.json")), [])

    def test_usage_limit_opens_transport_circuit_but_keeps_cache_readable(
        self,
    ) -> None:
        with tempfile.TemporaryDirectory() as directory:
            transport = UsageLimitAfterOneTransport()
            provider = CodexResearcherProvider(  # type: ignore[arg-type]
                transport=transport
            )
            provider.configure_response_cache(directory)
            cached_payload = {"target_id": TARGET, "as_of_date": AS_OF_DATE}
            provider.complete(
                pass_name="SOURCE_QUERY_GENERATION",
                payload=cached_payload,
            )
            with self.assertRaisesRegex(RuntimeError, "usage limit"):
                provider.complete(
                    pass_name="SOURCE_QUERY_GENERATION",
                    payload={**cached_payload, "target_id": "SECOND-TARGET"},
                )
            with self.assertRaisesRegex(
                RuntimeError, "PROVIDER_USAGE_LIMIT_CIRCUIT_OPEN"
            ):
                provider.complete(
                    pass_name="SOURCE_QUERY_GENERATION",
                    payload={**cached_payload, "target_id": "THIRD-TARGET"},
                )

            cached = provider.complete(
                pass_name="SOURCE_QUERY_GENERATION",
                payload=cached_payload,
            )
            self.assertEqual(cached["suggested_queries"], [])
            self.assertEqual(transport.call_count, 2)
            audit = provider.response_cache_audit()
            self.assertTrue(audit["provider_usage_limit_detected"])
            self.assertEqual(audit["transport_call_count"], 2)
            self.assertEqual(
                audit["provider_usage_limit_transport_error_count"], 1
            )
            self.assertEqual(
                audit["provider_usage_limit_short_circuit_count"], 1
            )
            self.assertEqual(
                audit["provider_usage_limit_reset_hints"],
                ["Aug 3rd, 2031 7:09 PM"],
            )
            self.assertEqual(audit["cache_hit_count"], 1)

    def test_codex_provider_evicts_only_downstream_semantically_invalid_response(
        self,
    ) -> None:
        with tempfile.TemporaryDirectory() as directory:
            payload = {"target_id": TARGET, "as_of_date": AS_OF_DATE}
            first_transport = SchemaRecordingTransport()
            first = CodexResearcherProvider(  # type: ignore[arg-type]
                transport=first_transport
            )
            first.configure_response_cache(directory)
            first.complete(pass_name="SOURCE_QUERY_GENERATION", payload=payload)

            event = first.invalidate_last_response_cache(
                "nearest anchors must also be historical_anchor_ids"
            )

            self.assertEqual(event["status"], "INVALID_RESPONSE_CACHE_DELETED")
            self.assertEqual(list(Path(directory).glob("*.json")), [])
            quarantine = Path(directory) / "_invalidated"
            quarantined_responses = [
                path
                for path in quarantine.glob("*.json")
                if not path.name.endswith(".reason.json")
            ]
            self.assertEqual(len(quarantined_responses), 1)
            reason_paths = list(quarantine.glob("*.reason.json"))
            self.assertEqual(len(reason_paths), 1)
            reason = json.loads(reason_paths[0].read_text(encoding="utf-8"))
            self.assertIn("nearest anchors", reason["reason"])
            self.assertFalse(reason["production_score_authority"])
            self.assertFalse(reason["reusable_provider_response"])
            audit = first.response_cache_audit()
            self.assertEqual(audit["downstream_semantic_invalidation_count"], 1)
            self.assertEqual(audit["downstream_semantic_cache_delete_count"], 1)
            self.assertEqual(
                audit["downstream_semantic_cache_delete_failure_count"], 0
            )
            self.assertFalse(
                audit[
                    "invalidated_response_quarantine_is_score_authority"
                ]
            )
            self.assertFalse(
                audit[
                    "invalidated_response_quarantine_is_reusable_cache"
                ]
            )

            resumed_transport = SchemaRecordingTransport()
            resumed = CodexResearcherProvider(  # type: ignore[arg-type]
                transport=resumed_transport
            )
            resumed.configure_response_cache(directory)
            resumed.complete(pass_name="SOURCE_QUERY_GENERATION", payload=payload)
            self.assertEqual(resumed_transport.call_count, 1)
            self.assertFalse(resumed.calls[-1]["cache_hit"])

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

    def test_component_research_rewrites_when_available_required_metric_was_omitted(
        self,
    ) -> None:
        class OmitFirstMetricProvider(ScriptedResearchProvider):
            def complete(
                self, *, pass_name: str, payload: Mapping[str, Any]
            ) -> Mapping[str, Any]:
                response = dict(
                    super().complete(pass_name=pass_name, payload=payload)
                )
                if (
                    pass_name == "COMPONENT_RESEARCH"
                    and not payload.get(
                        "component_research_validation_retry_context"
                    )
                ):
                    response["structured_metric_row_indices"] = [0]
                return response

        provider = OmitFirstMetricProvider()
        plans = ComponentResearchPlanner().plan(
            target_id=TARGET,
            archetype_id=ARCHETYPE,
            evidence_facts=self.facts,
            historical_anchors=self.anchors,
            research_seeds=(),
            component_max_points=self.maxima,
            structured_metric_requirements={
                key: (
                    ("CURRENT_VALUATION", "DURABLE_VISIBILITY")
                    if key == "eps_fcf_explosion"
                    else ()
                )
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

        result = EPSFCFResearcher(provider=provider).research(
            plan=plans[0],
            business_model=business,  # type: ignore[arg-type]
            evidence_facts=self.facts,
            historical_anchors=self.anchors,
            source_coverage=["ISSUER_OFFICIAL"],
            structured_metrics={
                "CURRENT_VALUATION": {"record_count": 3},
                "DURABLE_VISIBILITY": {"record_count": 2},
            },
        )

        self.assertEqual(result.status, "COMPLETE")
        self.assertEqual(
            set(result.memo.structured_metrics),  # type: ignore[union-attr]
            {"CURRENT_VALUATION", "DURABLE_VISIBILITY"},
        )
        component_calls = [
            row
            for row in provider.calls
            if row["pass_name"] == "COMPONENT_RESEARCH"
        ]
        self.assertEqual(len(component_calls), 2)
        retry = component_calls[-1]["payload"][
            "component_research_validation_retry_context"
        ]
        self.assertEqual(
            retry["required_structured_metric_row_indices"],
            [0, 1],
        )
        self.assertIn(
            "omitted available required structured metrics",
            retry["validation_error"],
        )

    def test_component_research_plan_projects_fact_ids_without_losing_rows(self) -> None:
        provider = ScriptedResearchProvider()
        plans = ComponentResearchPlanner().plan(
            target_id=TARGET,
            archetype_id=ARCHETYPE,
            evidence_facts=self.facts,
            historical_anchors=self.anchors,
            research_seeds=(),
            component_max_points=self.maxima,
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

        result = EPSFCFResearcher(provider=provider).research(
            plan=plans[0],
            business_model=business,  # type: ignore[arg-type]
            evidence_facts=self.facts,
            historical_anchors=self.anchors,
            source_coverage=["ISSUER_OFFICIAL"],
        )

        call = [
            row for row in provider.calls if row["pass_name"] == "COMPONENT_RESEARCH"
        ][-1]
        payload = call["payload"]
        plan_projection = payload["research_plan"]
        roster = plan_projection["candidate_fact_roster_projection"]
        self.assertEqual(result.status, "COMPLETE")
        self.assertNotIn("candidate_fact_ids", plan_projection)
        self.assertEqual(
            roster["candidate_fact_count"], len(plans[0].candidate_fact_ids)
        )
        self.assertFalse(roster["candidate_fact_ids_exposed_to_provider"])
        self.assertTrue(roster["every_candidate_fact_accounted_by_count_and_hash"])
        self.assertFalse(roster["fixed_top_n_used"])
        self.assertEqual(
            payload["current_evidence_fact_projection"]["fact_count"],
            len(self.facts),
        )
        self.assertTrue(
            payload["current_evidence_fact_projection"][
                "every_current_fact_individually_citable"
            ]
        )
        self.assertEqual(set(plans[0].candidate_fact_ids), {"FACT-POS", "FACT-COUNTER"})

    def test_business_model_semantic_validation_retries_once(self) -> None:
        class BusinessCorrectingProvider(ScriptedResearchProvider):
            def __init__(self) -> None:
                super().__init__()
                self.invalidated_reasons: list[str] = []

            def invalidate_last_response_cache(self, reason: str):
                self.invalidated_reasons.append(reason)
                return {"status": "FIXTURE_INVALIDATED"}

            def complete(
                self, *, pass_name: str, payload: Mapping[str, Any]
            ) -> Mapping[str, Any]:
                response = dict(
                    super().complete(pass_name=pass_name, payload=payload)
                )
                if (
                    pass_name == "BUSINESS_MODEL_RESEARCH"
                    and "business_model_validation_retry_context"
                    not in payload
                ):
                    response["fact_row_indices"] = []
                return response

        provider = BusinessCorrectingProvider()
        result = BusinessMechanismResearcher(provider=provider).research(
            target_id=TARGET,
            archetype_id=ARCHETYPE,
            as_of_date=AS_OF_DATE,
            evidence_facts=self.facts,
            source_claims=[],
            source_documents=[],
            source_coverage=["ISSUER_OFFICIAL"],
        )

        calls = [
            row
            for row in provider.calls
            if row["pass_name"] == "BUSINESS_MODEL_RESEARCH"
        ]
        self.assertEqual(result.status, "COMPLETE")
        self.assertEqual(len(calls), 2)
        self.assertEqual(len(provider.invalidated_reasons), 1)
        self.assertIn(
            "requires source-backed facts", provider.invalidated_reasons[0]
        )
        retry_context = calls[-1]["payload"][
            "business_model_validation_retry_context"
        ]
        self.assertIn(
            "requires source-backed facts", retry_context["validation_error"]
        )
        self.assertIn(
            "select at least one source-backed current fact_row_index",
            retry_context["instruction"],
        )

    def test_component_semantic_validation_retries_once_without_code_repair(
        self,
    ) -> None:
        class CorrectingProvider(ScriptedResearchProvider):
            def __init__(self) -> None:
                super().__init__()
                self.invalidated_reasons: list[str] = []

            def invalidate_last_response_cache(self, reason: str):
                self.invalidated_reasons.append(reason)
                return {"status": "FIXTURE_INVALIDATED"}

            def complete(
                self, *, pass_name: str, payload: Mapping[str, Any]
            ) -> Mapping[str, Any]:
                response = dict(
                    super().complete(pass_name=pass_name, payload=payload)
                )
                if (
                    pass_name == "COMPONENT_RESEARCH"
                    and "component_research_validation_retry_context"
                    not in payload
                ):
                    response["historical_anchor_ids"] = list(
                        response["nearest_counter_anchor_ids"]
                    )
                return response

        provider = CorrectingProvider()
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

        component_calls = [
            row for row in provider.calls
            if row["pass_name"] == "COMPONENT_RESEARCH"
        ]
        retry_context = component_calls[-1]["payload"][
            "component_research_validation_retry_context"
        ]
        self.assertEqual(result.status, "COMPLETE")
        self.assertEqual(len(component_calls), 2)
        self.assertEqual(len(provider.invalidated_reasons), 1)
        self.assertIn("nearest anchors", provider.invalidated_reasons[0])
        self.assertIn("nearest anchors", retry_context["validation_error"])
        self.assertNotEqual(
            retry_context["rejected_response"]["historical_anchor_ids"],
            result.memo.historical_anchor_ids,  # type: ignore[union-attr]
        )

    def test_component_fact_grounding_retries_predicate_drift(self) -> None:
        class GroundingCorrectingProvider(ScriptedResearchProvider):
            def __init__(self) -> None:
                super().__init__()
                self.invalidated_reasons: list[str] = []

            def invalidate_last_response_cache(self, reason: str):
                self.invalidated_reasons.append(reason)
                return {"status": "FIXTURE_INVALIDATED"}

            def complete(
                self, *, pass_name: str, payload: Mapping[str, Any]
            ) -> Mapping[str, Any]:
                response = dict(
                    super().complete(pass_name=pass_name, payload=payload)
                )
                if (
                    pass_name == "COMPONENT_RESEARCH"
                    and "component_research_validation_retry_context"
                    not in payload
                ):
                    groundings = [
                        dict(row)
                        for row in response["selected_fact_groundings"]
                    ]
                    groundings[0]["source_predicate"] = (
                        "invented_peer_relative_underperformance"
                    )
                    response["selected_fact_groundings"] = groundings
                return response

        provider = GroundingCorrectingProvider()
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

        component_calls = [
            row
            for row in provider.calls
            if row["pass_name"] == "COMPONENT_RESEARCH"
        ]
        self.assertEqual(result.status, "COMPLETE")
        self.assertEqual(len(component_calls), 2)
        self.assertEqual(len(provider.invalidated_reasons), 1)
        self.assertIn(
            "source_predicate mismatch", provider.invalidated_reasons[0]
        )
        retry_context = component_calls[-1]["payload"][
            "component_research_validation_retry_context"
        ]
        self.assertIn(
            "source_predicate mismatch", retry_context["validation_error"]
        )
        self.assertIn(
            "Copy its decoded predicate", retry_context["instruction"]
        )
        expected_grounding = retry_context[
            "expected_selected_fact_groundings"
        ][0]
        self.assertEqual(
            expected_grounding["source_predicate"], self.facts[0].predicate
        )
        self.assertEqual(
            expected_grounding["source_value_json"],
            json.dumps(
                self.facts[0].value,
                ensure_ascii=False,
                sort_keys=True,
                separators=(",", ":"),
            ),
        )
        self.assertEqual(
            expected_grounding["source_period_json"],
            json.dumps(
                self.facts[0].period,
                ensure_ascii=False,
                sort_keys=True,
                separators=(",", ":"),
            ),
        )

    def test_component_retry_preserves_llm_retain_decision_across_arrays(
        self,
    ) -> None:
        seed_provider = ScriptedResearchProvider()
        business = BusinessMechanismResearcher(provider=seed_provider).research(
            target_id=TARGET,
            archetype_id=ARCHETYPE,
            as_of_date=AS_OF_DATE,
            evidence_facts=self.facts,
            source_claims=[],
            source_documents=[],
            source_coverage=["ISSUER_OFFICIAL"],
        ).memo
        seed = EPSFCFResearcher(provider=seed_provider).research(
            plan=self._plans()[0],
            business_model=business,  # type: ignore[arg-type]
            evidence_facts=self.facts,
            historical_anchors=self.anchors,
            source_coverage=["ISSUER_OFFICIAL"],
        )

        class RetainSelectionCorrectingProvider(ScriptedResearchProvider):
            def complete(
                self, *, pass_name: str, payload: Mapping[str, Any]
            ) -> Mapping[str, Any]:
                response = dict(
                    super().complete(pass_name=pass_name, payload=payload)
                )
                if (
                    pass_name == "COMPONENT_RESEARCH"
                    and "component_research_validation_retry_context"
                    not in payload
                ):
                    retained = [
                        row["fact_row_index"]
                        for row in response["prior_fact_dispositions"]
                        if row["disposition"] == "RETAIN"
                    ]
                    missing = retained[-1]
                    response["selected_fact_row_indices"] = [
                        row
                        for row in response["selected_fact_row_indices"]
                        if row != missing
                    ]
                    response["selected_fact_groundings"] = [
                        row
                        for row in response["selected_fact_groundings"]
                        if row["fact_row_index"] != missing
                    ]
                return response

        provider = RetainSelectionCorrectingProvider()
        result = EPSFCFResearcher(provider=provider).research(
            plan=self._plans()[0],
            business_model=business,  # type: ignore[arg-type]
            evidence_facts=self.facts,
            historical_anchors=self.anchors,
            source_coverage=["ISSUER_OFFICIAL"],
            prior_memo=seed.memo,
        )

        component_calls = [
            row
            for row in provider.calls
            if row["pass_name"] == "COMPONENT_RESEARCH"
        ]
        retry = component_calls[-1]["payload"][
            "component_research_validation_retry_context"
        ]
        mismatch_rows = retry[
            "retained_not_selected_fact_row_indices"
        ]
        expected_rows = {
            row["fact_row_index"]
            for row in retry["expected_selected_fact_groundings"]
        }
        self.assertEqual(result.status, "COMPLETE")
        self.assertEqual(len(component_calls), 2)
        self.assertEqual(len(mismatch_rows), 1)
        self.assertTrue(set(mismatch_rows).issubset(expected_rows))
        self.assertEqual(
            retry["omitted_but_selected_fact_row_indices"], []
        )
        self.assertNotIn("rejected_response", retry)
        self.assertTrue(
            retry[
                "rejected_response_omitted_to_prevent_cross_array_error_copy"
            ]
        )
        self.assertEqual(
            set(retry["required_model_selected_fact_row_indices"]),
            expected_rows,
        )
        self.assertEqual(
            retry["required_model_selection_source"],
            "REJECTED_LLM_SELECTED_UNION_REJECTED_LLM_RETAIN",
        )
        self.assertFalse(retry["deterministic_selection_decision"])
        self.assertIn(
            "cross-array expression", retry["instruction"]
        )

    def test_component_research_reselects_every_prior_fact_without_score_carry_forward(
        self,
    ) -> None:
        first_provider = ScriptedResearchProvider()
        business = BusinessMechanismResearcher(provider=first_provider).research(
            target_id=TARGET,
            archetype_id=ARCHETYPE,
            as_of_date=AS_OF_DATE,
            evidence_facts=self.facts,
            source_claims=[],
            source_documents=[],
            source_coverage=["ISSUER_OFFICIAL"],
        ).memo
        first = EPSFCFResearcher(provider=first_provider).research(
            plan=self._plans()[0],
            business_model=business,  # type: ignore[arg-type]
            evidence_facts=self.facts,
            historical_anchors=self.anchors,
            source_coverage=["ISSUER_OFFICIAL"],
        )

        resumed_provider = ScriptedResearchProvider()
        resumed = EPSFCFResearcher(provider=resumed_provider).research(
            plan=self._plans()[0],
            business_model=business,  # type: ignore[arg-type]
            evidence_facts=self.facts,
            historical_anchors=self.anchors,
            source_coverage=["ISSUER_OFFICIAL"],
            prior_memo=first.memo,
        )

        payload = resumed_provider.calls[-1]["payload"]
        context = payload["prior_component_memo_context"]
        self.assertEqual(resumed.status, "COMPLETE")
        self.assertTrue(context["available"])
        self.assertFalse(context["score_authority"])
        self.assertFalse(context["deterministic_fact_carry_forward"])
        self.assertEqual(context["current_fact_row_count"], 2)
        self.assertNotIn("fact_id", _recursive_keys(context))
        self.assertEqual(
            resumed.memo.positive_fact_ids,  # type: ignore[union-attr]
            first.memo.positive_fact_ids,  # type: ignore[union-attr]
        )
        self.assertEqual(
            resumed.memo.counter_fact_ids,  # type: ignore[union-attr]
            first.memo.counter_fact_ids,  # type: ignore[union-attr]
        )
        unavailable_context = _project_prior_component_memo_context(
            prior_memo=first.memo,
            plan=self._plans()[0],
            facts={row.fact_id: row for row in self.facts},
            fact_id_by_row_index={},
        )
        self.assertFalse(unavailable_context["available"])
        self.assertFalse(
            unavailable_context["prior_fact_dispositions_required"]
        )
        self.assertEqual(
            unavailable_context["required_prior_fact_disposition_count"], 0
        )
        self.assertEqual(
            unavailable_context["unavailable_prior_fact_count"], 2
        )

    def test_prior_fact_omission_requires_explicit_llm_disposition(self) -> None:
        seed_provider = ScriptedResearchProvider()
        business = BusinessMechanismResearcher(provider=seed_provider).research(
            target_id=TARGET,
            archetype_id=ARCHETYPE,
            as_of_date=AS_OF_DATE,
            evidence_facts=self.facts,
            source_claims=[],
            source_documents=[],
            source_coverage=["ISSUER_OFFICIAL"],
        ).memo
        seed = EPSFCFResearcher(provider=seed_provider).research(
            plan=self._plans()[0],
            business_model=business,  # type: ignore[arg-type]
            evidence_facts=self.facts,
            historical_anchors=self.anchors,
            source_coverage=["ISSUER_OFFICIAL"],
        )

        class SilentDropProvider(ScriptedResearchProvider):
            def complete(
                self, *, pass_name: str, payload: Mapping[str, Any]
            ) -> Mapping[str, Any]:
                response = dict(
                    super().complete(pass_name=pass_name, payload=payload)
                )
                if pass_name == "COMPONENT_RESEARCH":
                    response["prior_fact_dispositions"] = []
                return response

        provider = SilentDropProvider()
        result = EPSFCFResearcher(provider=provider).research(
            plan=self._plans()[0],
            business_model=business,  # type: ignore[arg-type]
            evidence_facts=self.facts,
            historical_anchors=self.anchors,
            source_coverage=["ISSUER_OFFICIAL"],
            prior_memo=seed.memo,
        )

        self.assertEqual(result.status, "PENDING")
        self.assertIn(
            "prior fact dispositions must account",
            result.pending_reasons[0],
        )
        self.assertEqual(
            len(
                [
                    row
                    for row in provider.calls
                    if row["pass_name"] == "COMPONENT_RESEARCH"
                ]
            ),
            2,
        )

    def test_positive_score_without_positive_fact_is_rejected_and_rewritten(
        self,
    ) -> None:
        class UnsupportedPositiveProvider(ScriptedResearchProvider):
            def complete(
                self, *, pass_name: str, payload: Mapping[str, Any]
            ) -> Mapping[str, Any]:
                response = dict(
                    super().complete(pass_name=pass_name, payload=payload)
                )
                if pass_name == "COMPONENT_RESEARCH":
                    selected = [
                        row["fact_row_index"]
                        for row in _projected_fact_rows(payload)
                        if row["direction"] == "NEUTRAL"
                    ]
                    response["selected_fact_row_indices"] = selected
                    response["selected_fact_groundings"] = (
                        _selected_fact_groundings(payload, selected)
                    )
                return response

        provider = UnsupportedPositiveProvider()
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
        self.assertIn(
            "positive component score requires at least one selected current POSITIVE",
            result.pending_reasons[0],
        )
        retry_payload = provider.calls[-1]["payload"]
        self.assertIn(
            "Positive points require at least one selected current POSITIVE fact",
            retry_payload["component_research_validation_retry_context"][
                "instruction"
            ],
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

    def test_component_prompt_excludes_only_prevalidated_non_citable_scope(self) -> None:
        provider = ScriptedResearchProvider()
        restricted = _fact(
            "FACT-CORPORATE-ONLY",
            "POSITIVE",
            "CURRENT",
            allowed_component_ids=("capital_allocation", "information_confidence"),
        )
        facts = (*self.facts, restricted)
        plans = ComponentResearchPlanner().plan(
            target_id=TARGET,
            archetype_id=ARCHETYPE,
            evidence_facts=facts,
            historical_anchors=self.anchors,
            research_seeds=(),
            component_max_points=self.maxima,
            structured_metric_requirements={key: () for key in self.maxima},
        )
        business = BusinessMechanismResearcher(provider=provider).research(
            target_id=TARGET,
            archetype_id=ARCHETYPE,
            as_of_date=AS_OF_DATE,
            evidence_facts=facts,
            source_claims=[],
            source_documents=[],
            source_coverage=["ISSUER_OFFICIAL"],
        ).memo

        result = EPSFCFResearcher(provider=provider).research(
            plan=plans[0],
            business_model=business,  # type: ignore[arg-type]
            evidence_facts=facts,
            historical_anchors=self.anchors,
            source_coverage=["ISSUER_OFFICIAL"],
        )

        component_payload = provider.calls[-1]["payload"]
        visible_rows = _projected_fact_rows(component_payload)
        self.assertEqual(result.status, "COMPLETE")
        self.assertIn("FACT-CORPORATE-ONLY", plans[0].candidate_fact_ids)
        self.assertEqual(len(visible_rows), len(facts) - 1)
        self.assertNotIn(
            "fact_id",
            component_payload["current_evidence_fact_projection"][
                "fact_fields"
            ],
        )
        self.assertEqual(
            component_payload["component_fact_scope_projection"]
            ["non_citable_fact_count"],
            1,
        )
        self.assertTrue(
            component_payload["component_fact_scope_projection"]
            ["every_input_fact_accounted"]
        )

    def test_component_fact_direction_is_resolved_from_immutable_fact_graph(self) -> None:
        class SelectAllFactsProvider(ScriptedResearchProvider):
            def complete(
                self, *, pass_name: str, payload: Mapping[str, Any]
            ) -> Mapping[str, Any]:
                response = dict(super().complete(pass_name=pass_name, payload=payload))
                if pass_name == "COMPONENT_RESEARCH":
                    selected = [
                        row["fact_row_index"]
                        for row in _projected_fact_rows(payload)
                    ]
                    response["selected_fact_row_indices"] = selected
                    response["selected_fact_groundings"] = (
                        _selected_fact_groundings(payload, selected)
                    )
                return response

        provider = SelectAllFactsProvider()
        neutral = _fact("FACT-NEUTRAL", "NEUTRAL", "OPEN")
        facts = (*self.facts, neutral)
        plans = ComponentResearchPlanner().plan(
            target_id=TARGET,
            archetype_id=ARCHETYPE,
            evidence_facts=facts,
            historical_anchors=self.anchors,
            research_seeds=(),
            component_max_points=self.maxima,
            structured_metric_requirements={key: () for key in self.maxima},
        )
        business = BusinessMechanismResearcher(provider=provider).research(
            target_id=TARGET,
            archetype_id=ARCHETYPE,
            as_of_date=AS_OF_DATE,
            evidence_facts=facts,
            source_claims=[],
            source_documents=[],
            source_coverage=["ISSUER_OFFICIAL"],
        ).memo

        result = EPSFCFResearcher(provider=provider).research(
            plan=plans[0],
            business_model=business,  # type: ignore[arg-type]
            evidence_facts=facts,
            historical_anchors=self.anchors,
            source_coverage=["ISSUER_OFFICIAL"],
        )

        self.assertEqual(result.status, "COMPLETE")
        self.assertEqual(result.memo.context_fact_ids, ("FACT-NEUTRAL",))  # type: ignore[union-attr]
        self.assertNotIn("FACT-NEUTRAL", result.memo.counter_fact_ids)  # type: ignore[union-attr]

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
            prior_supervisor_feedback_by_component={
                "market_mispricing": {
                    "review_id": "SUPERVISOR-7",
                    "component_findings": [
                        {
                            "component_id": "market_mispricing",
                            "memo_sufficient": False,
                            "rationale": (
                                "이전 row 777과 FACT-POS의 현재 방향을 "
                                "메모 서술과 일치시켜야 한다"
                            ),
                        }
                    ],
                }
            },
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
        component_payloads = {
            call["payload"]["component_id"]: call["payload"]
            for call in provider.calls
            if call["pass_name"] == "COMPONENT_RESEARCH"
        }
        feedback_context = component_payloads["market_mispricing"][
            "prior_supervisor_feedback_context"
        ]
        feedback_json = json.dumps(feedback_context, ensure_ascii=False)
        self.assertTrue(feedback_context["available"])
        self.assertFalse(feedback_context["score_authority"])
        self.assertFalse(feedback_context["stage_authority"])
        self.assertNotIn("FACT-POS", feedback_json)
        self.assertNotIn("row 777", feedback_json)
        self.assertIn("unavailable_prior_row", feedback_json)
        self.assertIn("current_fact_row_index=", feedback_json)
        self.assertFalse(
            component_payloads["earnings_visibility"]
            ["prior_supervisor_feedback_context"]["available"]
        )

    def test_reusable_complete_memos_skip_component_provider_except_actionable_findings(
        self,
    ) -> None:
        first_provider = ScriptedResearchProvider()
        common = {
            "target_id": TARGET,
            "archetype_id": ARCHETYPE,
            "as_of_date": AS_OF_DATE,
            "evidence_facts": self.facts,
            "historical_anchors": self.anchors,
            "source_claims": (),
            "source_documents": (),
            "source_coverage": ("ISSUER_OFFICIAL",),
            "structured_metrics_by_component": {
                key: {} for key in self.maxima
            },
            "component_max_points": self.maxima,
            "structured_metric_requirements": {
                key: () for key in self.maxima
            },
        }
        first = CanonicalResearchDossierBuilder(
            provider=first_provider,
            research_seeds=(),
        ).build(**common)
        prior = {
            row.component_id: row.memo
            for row in first.component_results
            if row.memo is not None
        }

        second_provider = ScriptedResearchProvider()
        second = CanonicalResearchDossierBuilder(
            provider=second_provider,
            research_seeds=(),
        ).build(
            **common,
            prior_component_memos_by_component=prior,
            reusable_prior_component_memos_by_component=prior,
            prior_supervisor_feedback_by_component={
                component_id: {
                    "component_id": component_id,
                    "component_findings": [
                        {
                            "component_id": component_id,
                            "memo_sufficient": False,
                            "rationale": "semantic judge disagreement",
                        }
                    ],
                }
                for component_id in (
                    "bottleneck_pricing",
                    "capital_allocation",
                )
            },
        )

        component_calls = [
            call
            for call in second_provider.calls
            if call["pass_name"] == "COMPONENT_RESEARCH"
        ]
        self.assertEqual(
            {
                call["payload"]["component_id"]
                for call in component_calls
            },
            {"bottleneck_pricing", "capital_allocation"},
        )
        self.assertEqual(second.status, "RESEARCH_MEMOS_COMPLETE")
        self.assertEqual(
            {
                row.component_id
                for row in second.component_results
                if row.provider_name
                == "CHECKPOINT_REUSED_PRIOR_COMPONENT_MEMO"
            },
            set(CANONICAL_COMPONENT_ORDER)
            - {"bottleneck_pricing", "capital_allocation"},
        )

    def test_large_dossier_keeps_every_fact_but_compacts_repeated_lineage(self) -> None:
        provider = ScriptedResearchProvider()
        facts = tuple(
            _fact(
                f"FACT-{index:04d}",
                "POSITIVE" if index % 2 == 0 else "COUNTER",
                "CURRENT" if index % 2 == 0 else "OPEN",
            )
            for index in range(1_200)
        )
        claims = tuple(
            {
                "claim_id": f"CLAIM-FACT-{index:04d}",
                "document_id": "SRC-1",
                "source_ids": ("SRC-1",),
                "exact_quote": f"검증된 현재 사실 원문 {index}",
                "source_family": "ISSUER_DISCLOSURE",
                "source_tier": "PRIMARY",
                "published_at": "2026-06-20",
                "available_at": "2026-06-20",
                "structured_evidence_roles": (),
            }
            for index in range(1_200)
        )
        dossier = CanonicalResearchDossierBuilder(
            provider=provider, research_seeds=()
        ).build(
            target_id=TARGET,
            archetype_id=ARCHETYPE,
            as_of_date=AS_OF_DATE,
            evidence_facts=facts,
            historical_anchors=self.anchors,
            source_claims=claims,
            source_documents=(
                {
                    "document_id": "SRC-1",
                    "canonical_url": "https://issuer.example.com/current.pdf",
                    "title": "현재 공식 원문",
                    "source_family": "ISSUER_DISCLOSURE",
                    "source_provider": "OFFICIAL",
                    "published_at": "2026-06-20",
                    "available_at": "2026-06-20",
                    "content_type": "application/pdf",
                    "content_hash": "a" * 64,
                    "evidence_eligible": True,
                    "content_text": "이미 사실 추출을 마친 원문 " * 20_000,
                },
            ),
            source_coverage=("ISSUER_OFFICIAL",),
            structured_metrics_by_component={key: {} for key in self.maxima},
            component_max_points=self.maxima,
            structured_metric_requirements={key: () for key in self.maxima},
        )

        self.assertEqual(dossier.status, "RESEARCH_MEMOS_COMPLETE")
        research_calls = tuple(
            call
            for call in provider.calls
            if call["pass_name"]
            in {"BUSINESS_MODEL_RESEARCH", "COMPONENT_RESEARCH", "RED_TEAM_RESEARCH"}
        )
        self.assertEqual(len(research_calls), 9)
        for call in research_calls:
            payload = call["payload"]
            projection = payload["current_evidence_fact_projection"]
            self.assertEqual(projection["fact_count"], 1_200)
            self.assertEqual(projection["input_fact_count"], 1_200)
            self.assertEqual(projection["closed_fact_count"], 0)
            self.assertFalse(projection["fixed_top_n_used"])
            self.assertTrue(
                projection["every_current_fact_individually_citable"]
            )
            self.assertTrue(projection["dictionary_encoding_is_lossless"])
            self.assertNotIn("fact_id_by_row_index", projection)
            self.assertEqual(payload["source_claims"]["record_count"], 1_200)
            self.assertTrue(
                payload["source_claims"][
                    "every_record_accounted_by_hash_and_group_count"
                ]
            )
            self.assertNotIn("claims", payload["source_claims"])
            self.assertNotIn("documents", payload["source_documents"])
            self.assertLess(
                len(json.dumps(payload, ensure_ascii=False, sort_keys=True)),
                500_000,
            )

    def test_fabricated_fact_or_stage_output_becomes_pending_not_low_score(self) -> None:
        class FabricatingProvider(ScriptedResearchProvider):
            def complete(self, *, pass_name: str, payload: Mapping[str, Any]) -> Mapping[str, Any]:
                result = dict(super().complete(pass_name=pass_name, payload=payload))
                if pass_name == "COMPONENT_RESEARCH":
                    result["selected_fact_row_indices"] = [999_999]
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
    allowed_component_ids: tuple[str, ...] = (),
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
        allowed_component_ids=allowed_component_ids,
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
    projection = payload["current_evidence_fact_projection"]
    fields = projection["fact_fields"]
    dictionaries = projection.get("fact_value_dictionaries") or {}
    decoded_rows = []
    for row in payload["current_evidence_fact_graph"]:
        encoded = dict(zip(fields, row))
        decoded: dict[str, Any] = {}
        for field, value in encoded.items():
            suffix = "_dictionary_index"
            if field.endswith(suffix):
                semantic_field = field[: -len(suffix)]
                decoded[semantic_field] = dictionaries[semantic_field][value]
            else:
                decoded[field] = value
        decoded_rows.append(decoded)
    return tuple(decoded_rows)


def _selected_fact_groundings(
    payload: Mapping[str, Any], selected: list[int]
) -> list[Mapping[str, Any]]:
    return [
        {
            "fact_row_index": row["fact_row_index"],
            "source_predicate": row["predicate"],
            "source_value_json": json.dumps(
                row["value"],
                ensure_ascii=False,
                sort_keys=True,
                separators=(",", ":"),
            ),
            "source_period_json": json.dumps(
                row["period"],
                ensure_ascii=False,
                sort_keys=True,
                separators=(",", ":"),
            ),
            "source_economic_mechanism": row["economic_mechanism"],
            "component_interpretation": (
                "원 predicate, value, period와 경제 메커니즘을 그대로 반영한다."
            ),
        }
        for row in _projected_fact_rows(payload)
        if row["fact_row_index"] in selected
    ]


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
