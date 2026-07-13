from __future__ import annotations

from dataclasses import replace
import tempfile
import unittest
from pathlib import Path
from typing import Any, Mapping

from e2r.research_brain.planning.provider_transport import (
    StructuredProviderResponse,
    StructuredProviderUnavailable,
)
from e2r.research_brain.researcher_mode import (
    CodexResearcherProvider,
    ResearcherEventOverlay,
    ResearcherStageCourt,
    STAGE_GATE_FACT_MAPPING_SCHEMA,
    StageTransitionContext,
    write_researcher_stagecourt_run,
)
from tests.test_e2r_v5_deterministic_score_aggregator import _aggregation_run


TARGET = "CURRENT-TARGET"
AS_OF_DATE = "2026-06-29"
C06 = "C06_HBM_MEMORY_CUSTOMER_CAPACITY"
C12 = "C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK"


class StageMappingProvider:
    provider_name = "TEST_STAGE_GATE_MAPPER"

    def __init__(
        self,
        *,
        mappings: list[Mapping[str, Any]] | None = None,
        fail: bool = False,
        complete: bool = True,
    ) -> None:
        self.mappings = list(mappings or [])
        self.fail = fail
        self.mapping_complete = complete
        self.calls: list[Mapping[str, Any]] = []

    def complete(self, *, pass_name: str, payload: Mapping[str, Any]):
        self.calls.append({"pass_name": pass_name, "payload": payload})
        if self.fail:
            raise StructuredProviderUnavailable("provider usage limit")
        return {
            "mappings": self.mappings,
            "unresolved_material_questions": (
                []
                if self.mapping_complete
                else ["material primitive mapping remains open"]
            ),
            "mapping_complete": self.mapping_complete,
        }


class E2RV5StageCourtTests(unittest.TestCase):
    def test_complete_high_score_green_gate_becomes_final_without_llm_stage(self) -> None:
        provider = StageMappingProvider(
            mappings=[
                _mapping(primitive_id, "SUPPORT", "CLAIM-SUPPORT")
                for primitive_id in (
                    "customer_preorder_or_allocation",
                    "revenue_visibility_contract",
                    "hbm_capacity_constraint",
                    "hbm_capacity_pre_sold",
                )
            ]
        )
        run = _decide(provider=provider, archetype_id=C06)

        self.assertEqual(run.decision.status, "FINAL")
        self.assertEqual(run.decision.canonical_stage, "3-Green")
        self.assertTrue(run.decision.stage_gates_complete)
        self.assertFalse(run.decision.llm_stage_authority)
        self.assertEqual(run.audit["critical_count_sum"], 0)
        self.assertNotIn("stage", _recursive_keys(provider.calls[0]["payload"]))
        self.assertEqual(provider.calls[0]["pass_name"], "STAGE_GATE_FACT_MAPPING")

    def test_research_incomplete_is_not_disguised_as_stage0_and_skips_provider(self) -> None:
        provider = StageMappingProvider()
        run = _decide(
            provider=provider,
            archetype_id=C06,
            research_complete=False,
        )

        self.assertEqual(run.decision.status, "RESEARCH_IN_PROGRESS")
        self.assertIsNone(run.decision.canonical_stage)
        self.assertIn("RESEARCHER_MODE_NOT_COMPLETE", run.decision.pending_reasons)
        self.assertEqual(provider.calls, [])
        self.assertEqual(
            run.audit["critical_counts"]["pending_disguised_as_stage0_count"],
            0,
        )

    def test_provider_failure_is_pending_without_score_or_stage_fabrication(self) -> None:
        provider = StageMappingProvider(fail=True)
        run = _decide(provider=provider, archetype_id=C06)

        self.assertEqual(run.decision.status, "PROVIDER_PENDING")
        self.assertIsNone(run.decision.canonical_stage)
        self.assertIn("PROVIDER_USAGE_LIMIT", run.decision.pending_reasons[0])
        self.assertFalse(run.decision.stage_gates_complete)

    def test_unknown_claim_mapping_is_pending_instead_of_silent_drop(self) -> None:
        provider = StageMappingProvider(
            mappings=[
                _mapping(
                    "customer_preorder_or_allocation",
                    "SUPPORT",
                    "FABRICATED-CLAIM",
                )
            ]
        )
        run = _decide(provider=provider, archetype_id=C06)

        self.assertEqual(run.decision.status, "STAGE_GATE_MAPPING_PENDING")
        self.assertIsNone(run.decision.canonical_stage)
        self.assertEqual(run.mapping_rejections[0]["reason"], "UNKNOWN_CLAIM_ID")

    def test_hard_break_requires_open_official_target_mechanism_claim(self) -> None:
        provider = StageMappingProvider(
            mappings=[
                _mapping(
                    "contract_cancelled_or_delayed",
                    "COUNTER",
                    "CLAIM-COUNTER",
                )
            ]
        )
        run = _decide(
            provider=provider,
            archetype_id=C12,
            counter_source_tier="REGULATORY_OFFICIAL",
        )

        self.assertEqual(run.decision.status, "FINAL")
        self.assertEqual(run.decision.canonical_stage, "4C")
        self.assertEqual(run.decision.hard_break_claim_ids, ("CLAIM-COUNTER",))

        resolved = _decide(
            provider=provider,
            archetype_id=C12,
            counter_source_tier="REGULATORY_OFFICIAL",
            counter_lifecycle="RESOLVED",
        )
        self.assertNotEqual(resolved.decision.canonical_stage, "4C")
        self.assertEqual(resolved.decision.hard_break_claim_ids, ())

    def test_daily_event_overlay_cannot_change_canonical_stage(self) -> None:
        mappings = [
            _mapping(primitive_id, "SUPPORT", "CLAIM-SUPPORT")
            for primitive_id in (
                "customer_preorder_or_allocation",
                "revenue_visibility_contract",
                "hbm_capacity_constraint",
                "hbm_capacity_pre_sold",
            )
        ]
        without_event = _decide(
            provider=StageMappingProvider(mappings=mappings),
            archetype_id=C06,
        )
        with_event = _decide(
            provider=StageMappingProvider(mappings=mappings),
            archetype_id=C06,
            event_overlay=ResearcherEventOverlay(
                status="EVENT_OVERLAY_ACTIVE",
                event_claim_ids=("CLAIM-SUPPORT",),
                event_type="EARNINGS_RELEASE",
                rationale="source-backed daily event",
                source_evidence_ids=("DOC-SUPPORT",),
            ),
        )

        self.assertEqual(
            with_event.decision.canonical_stage,
            without_event.decision.canonical_stage,
        )
        self.assertEqual(
            with_event.decision.event_overlay["canonical_stage_effect"],
            "NONE",
        )

    def test_stagecourt_writes_required_atomic_leaf_and_trace(self) -> None:
        run = _decide(
            provider=StageMappingProvider(
                mappings=[
                    _mapping(primitive_id, "SUPPORT", "CLAIM-SUPPORT")
                    for primitive_id in (
                        "customer_preorder_or_allocation",
                        "revenue_visibility_contract",
                        "hbm_capacity_constraint",
                        "hbm_capacity_pre_sold",
                    )
                ]
            ),
            archetype_id=C06,
        )
        with tempfile.TemporaryDirectory() as directory:
            paths = write_researcher_stagecourt_run(run, directory)
            self.assertEqual(set(paths), {"mappings", "decision", "trace", "audit"})
            self.assertTrue((Path(directory) / "atomic_stage_decision.json").is_file())
            self.assertTrue((Path(directory) / "stagecourt_trace.json").is_file())

    def test_mapping_schema_forbids_score_and_stage_output_fields(self) -> None:
        keys = _recursive_keys(STAGE_GATE_FACT_MAPPING_SCHEMA)
        self.assertNotIn("score", keys)
        self.assertNotIn("stage", keys)
        self.assertNotIn("uniqueItems", keys)

    def test_default_codex_provider_registers_stage_mapping_pass_and_schema(self) -> None:
        class RecordingTransport:
            def __init__(self) -> None:
                self.output_schema = None

            def complete(self, *, prompt, output_schema, schema_name):
                del prompt, schema_name
                self.output_schema = output_schema
                payload = {
                    "mappings": [],
                    "unresolved_material_questions": [],
                    "mapping_complete": True,
                }
                return StructuredProviderResponse(
                    payload=payload,
                    raw_response="{}",
                    stderr="",
                    returncode=0,
                )

        transport = RecordingTransport()
        provider = CodexResearcherProvider(transport=transport)  # type: ignore[arg-type]
        response = provider.complete(
            pass_name="STAGE_GATE_FACT_MAPPING",
            payload={"target_id": TARGET, "as_of_date": AS_OF_DATE},
        )
        self.assertTrue(response["mapping_complete"])
        self.assertEqual(transport.output_schema, STAGE_GATE_FACT_MAPPING_SCHEMA)


def _decide(
    *,
    provider: StageMappingProvider,
    archetype_id: str,
    research_complete: bool = True,
    counter_source_tier: str = "TRUSTED_INDEPENDENT",
    counter_lifecycle: str = "OPEN",
    event_overlay: ResearcherEventOverlay | None = None,
):
    base = _aggregation_run(mode="STRONG")[0]
    aggregation = replace(
        base,
        target_id=TARGET,
        archetype_id=archetype_id,
        as_of_date=AS_OF_DATE,
    )
    claims = (
        _claim(
            claim_id="CLAIM-SUPPORT",
            document_id="DOC-SUPPORT",
            direction="POSITIVE",
            lifecycle="CURRENT",
            source_tier="TRUSTED_INDEPENDENT",
            exact_quote="binding customer allocation and sold-out capacity",
        ),
        _claim(
            claim_id="CLAIM-COUNTER",
            document_id="DOC-COUNTER",
            direction="COUNTER",
            lifecycle=counter_lifecycle,
            source_tier=counter_source_tier,
            exact_quote="the customer cancelled the binding contract",
        ),
    )
    links = (
        {"claim_id": "CLAIM-SUPPORT", "fact_id": "PHASE90-FACT-SUPPORT"},
        {"claim_id": "CLAIM-COUNTER", "fact_id": "PHASE90-FACT-COUNTER"},
    )
    documents = tuple(
        {
            "document_id": claim["document_id"],
            "target_id": TARGET,
            "published_at": "2026-06-20",
            "available_at": "2026-06-20",
            "content_text": claim["exact_quote"],
            "evidence_eligible": True,
            "snippet_only": False,
        }
        for claim in claims
    )
    structured = (
        {
            "record_id": "REVISION-1",
            "target_id": TARGET,
            "as_of_date": AS_OF_DATE,
            "observed_at": "2026-06-25",
            "record_kind": "EARNINGS_REVISION",
            "metric_id": "eps_revision_1m_pct",
            "value": 20.0,
            "unit": "PERCENT",
            "metadata": {
                "revision_family": "EARNINGS",
                "target_price_only": False,
            },
        },
    )
    return ResearcherStageCourt(provider=provider).decide(
        target_id=TARGET,
        archetype_id=archetype_id,
        as_of_date=AS_OF_DATE,
        score_aggregation=aggregation,
        material_claims=claims,
        claim_fact_links=links,
        source_documents=documents,
        structured_records=structured,
        research_complete=research_complete,
        counter_thesis_complete=True,
        transition=StageTransitionContext(),
        event_overlay=event_overlay,
    )


def _mapping(primitive_id: str, direction: str, claim_id: str) -> Mapping[str, Any]:
    return {
        "primitive_id": primitive_id,
        "direction": direction,
        "claim_ids": [claim_id],
        "semantic_rationale": "the exact source-backed mechanism matches the configured primitive",
    }


def _claim(
    *,
    claim_id: str,
    document_id: str,
    direction: str,
    lifecycle: str,
    source_tier: str,
    exact_quote: str,
) -> Mapping[str, Any]:
    return {
        "claim_id": claim_id,
        "target_id": TARGET,
        "as_of_date": AS_OF_DATE,
        "published_at": "2026-06-20",
        "available_at": "2026-06-20",
        "accepted": True,
        "accepted_by_evidence_os": True,
        "material": True,
        "materiality": "CRITICAL",
        "direction": direction,
        "current_lifecycle": lifecycle,
        "document_id": document_id,
        "source_ids": [document_id],
        "source_family": "OPENDART" if "OFFICIAL" in source_tier else "PUBLIC_BROKER_PDF",
        "source_tier": source_tier,
        "source_independence_group": (
            f"{source_tier}:{document_id}"
        ),
        "subject": "current target direct operating mechanism",
        "predicate": "DIRECT_MECHANISM_STATE",
        "predicate_family": "DIRECT_MECHANISM",
        "normalized_object": "current target mechanism",
        "economic_mechanism": "target customer commitment directly changes revenue visibility",
        "exact_quote": exact_quote,
        "period": "2026Q2",
        "mechanism_scope_id": f"{TARGET}:DIRECT:MECHANISM",
        "scope_business_segment": "CORE",
        "scope_product_family": "CORE_PRODUCT",
        "scope_technology_family": "CORE_TECHNOLOGY",
        "scope_transaction_type": "CUSTOMER_COMMITMENT",
        "scope_economic_mechanism": "REVENUE_VISIBILITY",
        "scope_confidence": 0.95,
        "llm_score_authority": False,
        "llm_stage_authority": False,
    }


def _recursive_keys(value: Any) -> set[str]:
    keys: set[str] = set()
    if isinstance(value, Mapping):
        for key, child in value.items():
            keys.add(str(key))
            keys.update(_recursive_keys(child))
    elif isinstance(value, (list, tuple)):
        for child in value:
            keys.update(_recursive_keys(child))
    return keys


if __name__ == "__main__":
    unittest.main()
