from __future__ import annotations

from copy import deepcopy
from dataclasses import replace
import json
import tempfile
import unittest
from pathlib import Path
from typing import Any, Mapping

from e2r.research_brain.planning.provider_transport import (
    StructuredProviderRejected,
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
from e2r.research_brain.researcher_mode.component_researcher import (
    _materialize_stage_gate_fact_chunks,
    _merge_stage_gate_chunk_responses,
    _single_payload_request_material,
    _stage_gate_chunk_fact_directions,
    _validate_loss_accounted_chunk_response,
)
from e2r.research_brain.researcher_mode.prompt_projection import (
    project_stage_gate_citable_facts,
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
        fact_row_indices = [
            int(row[0])
            for row in payload.get("current_evidence_fact_graph") or ()
        ]
        mapped = {
            int(row_index)
            for mapping in self.mappings
            for row_index in mapping.get("fact_row_indices") or ()
            if isinstance(row_index, int)
            and not isinstance(row_index, bool)
        }
        return {
            "mappings": self.mappings,
            "fact_dispositions": [
                {
                    "fact_row_index": row_index,
                    "status": (
                        "MAPPED" if row_index in mapped else "NO_MATCH"
                    ),
                    "rationale": (
                        "mapped to a configured primitive"
                        if row_index in mapped
                        else "reviewed without a semantic primitive match"
                    ),
                }
                for row_index in fact_row_indices
            ],
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
                _mapping(primitive_id, "SUPPORT", 1)
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

    def test_research_in_progress_is_not_final_stage0(self) -> None:
        run = _decide(
            provider=StageMappingProvider(),
            archetype_id=C06,
            research_complete=False,
        )

        self.assertEqual("RESEARCH_IN_PROGRESS", run.decision.status)
        self.assertIsNone(run.decision.canonical_stage)
        self.assertNotEqual("0", run.decision.canonical_stage)

    def test_provider_failure_is_pending_without_score_or_stage_fabrication(self) -> None:
        provider = StageMappingProvider(fail=True)
        run = _decide(provider=provider, archetype_id=C06)

        self.assertEqual(run.decision.status, "PROVIDER_PENDING")
        self.assertIsNone(run.decision.canonical_stage)
        self.assertIn("PROVIDER_USAGE_LIMIT", run.decision.pending_reasons[0])
        self.assertFalse(run.decision.stage_gates_complete)

    def test_unknown_fact_row_mapping_is_pending_instead_of_silent_drop(self) -> None:
        provider = StageMappingProvider(
            mappings=[
                _mapping(
                    "customer_preorder_or_allocation",
                    "SUPPORT",
                    999,
                )
            ]
        )
        run = _decide(provider=provider, archetype_id=C06)

        self.assertEqual(run.decision.status, "STAGE_GATE_MAPPING_PENDING")
        self.assertIsNone(run.decision.canonical_stage)
        self.assertIn(
            "UNKNOWN_FACT_ROW_INDEX",
            {row["reason"] for row in run.mapping_rejections},
        )

    def test_hard_break_requires_open_official_target_mechanism_claim(self) -> None:
        provider = StageMappingProvider(
            mappings=[
                _mapping(
                    "contract_cancelled_or_delayed",
                    "COUNTER",
                    0,
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
            provider=StageMappingProvider(),
            archetype_id=C12,
            counter_source_tier="REGULATORY_OFFICIAL",
            counter_lifecycle="RESOLVED",
        )
        self.assertNotEqual(resolved.decision.canonical_stage, "4C")
        self.assertEqual(resolved.decision.hard_break_claim_ids, ())

    def test_daily_event_overlay_cannot_change_canonical_stage(self) -> None:
        mappings = [
            _mapping(primitive_id, "SUPPORT", 1)
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
                    _mapping(primitive_id, "SUPPORT", 1)
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

    def test_stagecourt_uses_deterministic_component_vector(self) -> None:
        provider = StageMappingProvider()
        run = _decide(provider=provider, archetype_id=C06)
        deterministic = _aggregation_run(mode="STRONG")[0]
        expected = deterministic.total_result.score
        assert expected is not None

        self.assertEqual(
            dict(expected.component_points),
            run.decision.component_vector,
        )
        self.assertNotIn(
            "component_vector",
            _recursive_keys(provider.calls[0]["payload"]),
        )

    def test_empty_mapping_cannot_skip_explicit_fact_dispositions(self) -> None:
        class MissingDispositionProvider(StageMappingProvider):
            def complete(self, *, pass_name, payload):
                self.calls.append(
                    {"pass_name": pass_name, "payload": payload}
                )
                return {
                    "mappings": [],
                    "unresolved_material_questions": [],
                    "mapping_complete": True,
                }

        run = _decide(
            provider=MissingDispositionProvider(),
            archetype_id=C06,
        )

        self.assertEqual(
            run.decision.status,
            "STAGE_GATE_MAPPING_PENDING",
        )
        self.assertIn(
            "FACT_DISPOSITIONS_NOT_ARRAY",
            {row["reason"] for row in run.mapping_rejections},
        )

    def test_stage_projection_accounts_every_eligibility_partition(self) -> None:
        support_claim = _claim(
            claim_id="CLAIM-SUPPORT",
            document_id="DOC-SUPPORT",
            direction="POSITIVE",
            lifecycle="CURRENT",
            source_tier="TRUSTED_INDEPENDENT",
            exact_quote="support",
        )
        counter_claim = _claim(
            claim_id="CLAIM-COUNTER",
            document_id="DOC-COUNTER",
            direction="COUNTER",
            lifecycle="OPEN",
            source_tier="TRUSTED_INDEPENDENT",
            exact_quote="counter",
        )
        neutral_claim = {
            **support_claim,
            "claim_id": "CLAIM-NEUTRAL",
            "document_id": "DOC-NEUTRAL",
            "source_ids": ["DOC-NEUTRAL"],
            "direction": "NEUTRAL",
        }
        resolved_claim = {
            **counter_claim,
            "claim_id": "CLAIM-RESOLVED",
            "document_id": "DOC-RESOLVED",
            "source_ids": ["DOC-RESOLVED"],
            "current_lifecycle": "RESOLVED",
        }
        facts = (
            _fact_from_claim(
                claim=support_claim,
                fact_id="FACT-SUPPORT",
            ),
            _fact_from_claim(
                claim=counter_claim,
                fact_id="FACT-COUNTER",
            ),
            _fact_from_claim(
                claim=neutral_claim,
                fact_id="FACT-NEUTRAL",
            ),
            _fact_from_claim(
                claim=resolved_claim,
                fact_id="FACT-RESOLVED",
            ),
        )

        projection = project_stage_gate_citable_facts(facts)

        self.assertEqual(projection["input_fact_count"], 4)
        self.assertEqual(projection["fact_count"], 2)
        self.assertEqual(projection["closed_fact_count"], 1)
        self.assertEqual(
            projection["active_non_mappable_fact_count"],
            1,
        )
        self.assertTrue(projection["every_input_fact_accounted"])
        self.assertTrue(
            projection[
                "every_ineligible_fact_accounted_by_count_and_hash"
            ]
        )
        self.assertFalse(projection["fixed_top_n_used"])
        self.assertEqual(
            projection["all_fact_lineage_profile"]["fact_count"],
            4,
        )

    def test_large_stage_fact_plane_materializes_exhaustive_bounded_chunks(
        self,
    ) -> None:
        class ExhaustiveStageTransport:
            def __init__(self) -> None:
                self.payloads = []
                self.prompt_lengths = []

            def provider_identity(self):
                return {
                    "transport_class": "ExhaustiveStageTransport",
                    "model": "test-model",
                }

            def complete(self, *, prompt, output_schema, schema_name):
                del output_schema, schema_name
                payload = json.loads(prompt.rsplit("\n", 1)[-1])
                self.payloads.append(payload)
                self.prompt_lengths.append(len(prompt))
                row_indices = [
                    int(row["fact_row_index"])
                    for row in payload["current_evidence_fact_graph"]
                ]
                response = {
                    "mappings": [],
                    "fact_dispositions": [
                        {
                            "fact_row_index": row_index,
                            "status": "NO_MATCH",
                            "rationale": "fully reviewed without a match",
                        }
                        for row_index in row_indices
                    ],
                    "unresolved_material_questions": [],
                    "mapping_complete": True,
                }
                return StructuredProviderResponse(
                    payload=response,
                    raw_response=json.dumps(response),
                    stderr="",
                    returncode=0,
                )

        class BoundedStageProvider(CodexResearcherProvider):
            @property
            def memo_fact_prompt_chunk_chars(self) -> int:
                return 120_000

        facts = _large_stage_facts(count=36, mechanism_chars=35_000)
        payload = _stage_provider_payload(facts)
        transport = ExhaustiveStageTransport()
        response = BoundedStageProvider(
            transport=transport  # type: ignore[arg-type]
        ).complete(
            pass_name="STAGE_GATE_FACT_MAPPING",
            payload=payload,
        )

        self.assertGreater(len(transport.payloads), 1)
        self.assertTrue(
            all(
                payload.get("loss_accounted_fact_chunk")
                for payload in transport.payloads
            )
        )
        emitted = [
            global_index
            for payload in transport.payloads
            for global_index in payload["loss_accounted_fact_chunk"][
                "global_fact_row_index_by_chunk_local_index"
            ]
        ]
        self.assertEqual(emitted, list(range(len(facts))))
        self.assertEqual(len(emitted), len(set(emitted)))
        self.assertTrue(
            all(length < 1_000_000 for length in transport.prompt_lengths)
        )
        self.assertEqual(
            [row["fact_row_index"] for row in response["fact_dispositions"]],
            list(range(len(facts))),
        )
        self.assertTrue(response["mapping_complete"])

    def test_samsung_scale_fact_counts_remain_loss_accounted(self) -> None:
        facts = _large_stage_facts(
            count=8_377,
            mechanism_chars=64,
        )
        for index in range(4_341, 7_987):
            facts[index]["current_lifecycle"] = "RESOLVED"
        for index in range(7_987, 8_377):
            facts[index]["direction"] = "NEUTRAL"
        projection = project_stage_gate_citable_facts(facts)
        payload = _stage_provider_payload(facts)
        chunks = _materialize_stage_gate_fact_chunks(
            payload,
            target_projection_chars=250_000,
            max_prompt_chars=1_000_000,
        )

        self.assertEqual(projection["input_fact_count"], 8_377)
        self.assertEqual(projection["fact_count"], 4_341)
        self.assertEqual(projection["closed_fact_count"], 3_646)
        self.assertEqual(
            projection["active_non_mappable_fact_count"],
            390,
        )
        emitted = [
            global_index
            for chunk in chunks
            for global_index in (
                chunk["loss_accounted_fact_chunk"][
                    "global_fact_row_index_by_chunk_local_index"
                ]
                if chunk.get("loss_accounted_fact_chunk")
                else [row[0] for row in chunk["current_evidence_fact_graph"]]
            )
        ]
        self.assertEqual(emitted, list(range(4_341)))
        self.assertEqual(len(emitted), len(set(emitted)))
        self.assertTrue(
            all(
                len(
                    _single_payload_request_material(
                        pass_name="STAGE_GATE_FACT_MAPPING",
                        payload=chunk,
                    )[2]
                )
                < 1_000_000
                for chunk in chunks
            )
        )

    def test_stage_chunk_rejects_omission_duplicate_scope_and_direction_tamper(
        self,
    ) -> None:
        facts = _large_stage_facts(count=4, mechanism_chars=12_000)
        chunks = _materialize_stage_gate_fact_chunks(
            _stage_provider_payload(facts),
            target_projection_chars=30_000,
            max_prompt_chars=1_000_000,
        )
        self.assertGreater(len(chunks), 1)
        chunk = chunks[0]
        allowed = {
            int(row["fact_row_index"])
            for row in chunk["current_evidence_fact_graph"]
        }
        directions = _stage_gate_chunk_fact_directions(chunk)
        primitives = {"test_primitive"}
        valid = {
            "mappings": [],
            "fact_dispositions": [
                {
                    "fact_row_index": row_index,
                    "status": "NO_MATCH",
                    "rationale": "reviewed",
                }
                for row_index in sorted(allowed)
            ],
            "unresolved_material_questions": [],
            "mapping_complete": True,
        }
        _validate_loss_accounted_chunk_response(
            pass_name="STAGE_GATE_FACT_MAPPING",
            response=valid,
            allowed_fact_row_indices=allowed,
            prior_fact_row_indices=set(),
            expected_component_groundings={},
            expected_stage_directions=directions,
            allowed_stage_primitives=primitives,
        )

        omission = deepcopy(valid)
        omission["fact_dispositions"] = omission[
            "fact_dispositions"
        ][1:]
        duplicate = deepcopy(valid)
        duplicate["fact_dispositions"].append(
            dict(duplicate["fact_dispositions"][0])
        )
        outside = deepcopy(valid)
        outside["mappings"] = [
            _mapping("test_primitive", "SUPPORT", 999)
        ]
        tampered = deepcopy(valid)
        counter_index = next(
            row_index
            for row_index, direction in directions.items()
            if direction == "COUNTER"
        )
        tampered["mappings"] = [
            _mapping("test_primitive", "SUPPORT", counter_index)
        ]
        for changed, error in (
            (omission, "disposition_roster_mismatch"),
            (duplicate, "disposition_duplicate"),
            (outside, "fact_row_outside_chunk"),
            (tampered, "fact_direction_mismatch"),
        ):
            with self.subTest(error=error), self.assertRaisesRegex(
                StructuredProviderRejected,
                error,
            ):
                _validate_loss_accounted_chunk_response(
                    pass_name="STAGE_GATE_FACT_MAPPING",
                    response=changed,
                    allowed_fact_row_indices=allowed,
                    prior_fact_row_indices=set(),
                    expected_component_groundings={},
                    expected_stage_directions=directions,
                    allowed_stage_primitives=primitives,
                )

    def test_stage_chunk_union_is_order_invariant_and_semantic_hash_sensitive(
        self,
    ) -> None:
        facts = _large_stage_facts(count=6, mechanism_chars=10_000)
        payload = _stage_provider_payload(facts)
        chunks = _materialize_stage_gate_fact_chunks(
            payload,
            target_projection_chars=30_000,
            max_prompt_chars=1_000_000,
        )
        self.assertGreater(len(chunks), 1)
        chunk_responses = []
        for chunk in chunks:
            global_indices = list(
                chunk["loss_accounted_fact_chunk"][
                    "global_fact_row_index_by_chunk_local_index"
                ]
            )
            selected = global_indices[0]
            chunk_responses.append(
                {
                    "chunk_index": chunk["loss_accounted_fact_chunk"][
                        "chunk_index"
                    ],
                    "response": {
                        "mappings": [
                            _mapping(
                                "test_primitive",
                                "SUPPORT",
                                selected,
                            )
                        ],
                        "fact_dispositions": [
                            {
                                "fact_row_index": row_index,
                                "status": (
                                    "MAPPED"
                                    if row_index == selected
                                    else "NO_MATCH"
                                ),
                                "rationale": f"reviewed {row_index}",
                            }
                            for row_index in global_indices
                        ],
                        "unresolved_material_questions": [],
                        "mapping_complete": True,
                    },
                }
            )
        forward = _merge_stage_gate_chunk_responses(
            chunks=chunks,
            chunk_responses=chunk_responses,
        )
        reverse = _merge_stage_gate_chunk_responses(
            chunks=tuple(reversed(chunks)),
            chunk_responses=tuple(reversed(chunk_responses)),
        )
        self.assertEqual(forward, reverse)

        changed_facts = list(deepcopy(facts))
        changed_facts[0]["economic_mechanism"] += " semantic change"
        original_hash = _single_payload_request_material(
            pass_name="STAGE_GATE_FACT_MAPPING",
            payload=payload,
        )[3]
        reordered_hash = _single_payload_request_material(
            pass_name="STAGE_GATE_FACT_MAPPING",
            payload=_stage_provider_payload(list(reversed(facts))),
        )[3]
        changed_hash = _single_payload_request_material(
            pass_name="STAGE_GATE_FACT_MAPPING",
            payload=_stage_provider_payload(changed_facts),
        )[3]
        self.assertEqual(original_hash, reordered_hash)
        self.assertNotEqual(original_hash, changed_hash)

    def test_stage_chunk_collaboration_wait_fans_out_but_other_errors_fail_fast(
        self,
    ) -> None:
        class PendingTransport:
            def __init__(self, *, generic_error: bool = False) -> None:
                self.prompts = []
                self.generic_error = generic_error

            def provider_identity(self):
                return {
                    "transport_class": "PendingTransport",
                    "model": "test-model",
                    "generic_error": self.generic_error,
                }

            def complete(self, *, prompt, output_schema, schema_name):
                del output_schema, schema_name
                self.prompts.append(prompt)
                if self.generic_error:
                    raise StructuredProviderUnavailable("network down")
                request_id = "COLLABREQ-" + format(
                    len(self.prompts),
                    "064x",
                )
                raise StructuredProviderUnavailable(
                    f"COLLABORATION_RESPONSE_PENDING:{request_id}"
                )

        class BoundedStageProvider(CodexResearcherProvider):
            @property
            def memo_fact_prompt_chunk_chars(self) -> int:
                return 80_000

        payload = _stage_provider_payload(
            _large_stage_facts(count=18, mechanism_chars=24_000)
        )
        expected_chunks = _materialize_stage_gate_fact_chunks(
            payload,
            target_projection_chars=80_000,
            max_prompt_chars=1_000_000,
        )
        self.assertGreater(len(expected_chunks), 1)

        pending_transport = PendingTransport()
        with self.assertRaises(StructuredProviderUnavailable) as context:
            BoundedStageProvider(
                transport=pending_transport  # type: ignore[arg-type]
            ).complete(
                pass_name="STAGE_GATE_FACT_MAPPING",
                payload=payload,
            )
        self.assertEqual(
            len(pending_transport.prompts),
            len(expected_chunks),
        )
        for index in range(1, len(expected_chunks) + 1):
            self.assertIn(
                "COLLABREQ-" + format(index, "064x"),
                str(context.exception),
            )

        error_transport = PendingTransport(generic_error=True)
        with self.assertRaisesRegex(
            StructuredProviderUnavailable,
            "network down",
        ):
            BoundedStageProvider(
                transport=error_transport  # type: ignore[arg-type]
            ).complete(
                pass_name="STAGE_GATE_FACT_MAPPING",
                payload=payload,
            )
        self.assertEqual(len(error_transport.prompts), 1)

    def test_one_claim_to_many_facts_maps_only_selected_fact(self) -> None:
        run = _decide(
            provider=StageMappingProvider(
                mappings=[
                    _mapping(
                        "customer_preorder_or_allocation",
                        "SUPPORT",
                        1,
                    )
                ]
            ),
            archetype_id=C06,
            support_fact_count=2,
        )

        self.assertEqual(run.decision.status, "FINAL")
        self.assertEqual(run.mapping_rejections, ())
        self.assertEqual(
            run.mappings[0].fact_ids,
            ("PHASE90-FACT-SUPPORT-0",),
        )
        self.assertEqual(
            run.mappings[0].claim_ids,
            ("CLAIM-SUPPORT",),
        )

    def test_default_codex_provider_registers_stage_mapping_pass_and_schema(self) -> None:
        class RecordingTransport:
            def __init__(self) -> None:
                self.output_schema = None

            def complete(self, *, prompt, output_schema, schema_name):
                del prompt, schema_name
                self.output_schema = output_schema
                payload = {
                    "mappings": [],
                    "fact_dispositions": [],
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
        self.assertEqual(
            set(transport.output_schema["required"]),
            set(STAGE_GATE_FACT_MAPPING_SCHEMA["required"]),
        )
        self.assertEqual(
            transport.output_schema["properties"]["mappings"]["maxItems"],
            0,
        )
        self.assertEqual(
            transport.output_schema["properties"]["fact_dispositions"][
                "maxItems"
            ],
            0,
        )


def _decide(
    *,
    provider: StageMappingProvider,
    archetype_id: str,
    research_complete: bool = True,
    counter_source_tier: str = "TRUSTED_INDEPENDENT",
    counter_lifecycle: str = "OPEN",
    event_overlay: ResearcherEventOverlay | None = None,
    support_fact_count: int = 1,
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
    support_fact_ids = tuple(
        (
            "PHASE90-FACT-SUPPORT"
            if support_fact_count == 1
            else f"PHASE90-FACT-SUPPORT-{index}"
        )
        for index in range(support_fact_count)
    )
    links = (
        *(
            {
                "claim_id": "CLAIM-SUPPORT",
                "fact_id": fact_id,
            }
            for fact_id in support_fact_ids
        ),
        {
            "claim_id": "CLAIM-COUNTER",
            "fact_id": "PHASE90-FACT-COUNTER",
        },
    )
    facts = (
        *(
            _fact_from_claim(
                claim=claims[0],
                fact_id=fact_id,
            )
            for fact_id in support_fact_ids
        ),
        _fact_from_claim(
            claim=claims[1],
            fact_id="PHASE90-FACT-COUNTER",
        ),
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
        evidence_facts=facts,
        material_claims=claims,
        claim_fact_links=links,
        source_documents=documents,
        structured_records=structured,
        research_complete=research_complete,
        counter_thesis_complete=True,
        transition=StageTransitionContext(),
        event_overlay=event_overlay,
    )


def _mapping(
    primitive_id: str,
    direction: str,
    fact_row_index: int,
) -> Mapping[str, Any]:
    return {
        "primitive_id": primitive_id,
        "direction": direction,
        "fact_row_indices": [fact_row_index],
        "semantic_rationale": "the exact source-backed mechanism matches the configured primitive",
    }


def _fact_from_claim(
    *,
    claim: Mapping[str, Any],
    fact_id: str,
) -> Mapping[str, Any]:
    return {
        "fact_id": fact_id,
        "target_id": TARGET,
        "as_of_date": AS_OF_DATE,
        "subject": claim["subject"],
        "business_segment": claim["scope_business_segment"],
        "product_family": claim["scope_product_family"],
        "economic_mechanism": claim["economic_mechanism"],
        "predicate": claim["predicate"],
        "value": claim.get("value"),
        "unit": claim.get("unit"),
        "period": claim["period"],
        "direction": claim["direction"],
        "source_ids": list(claim["source_ids"]),
        "claim_ids": [claim["claim_id"]],
        "quote_ids": [f"QUOTE-{claim['claim_id']}"],
        "current_lifecycle": claim["current_lifecycle"],
        "source_independence_group": claim[
            "source_independence_group"
        ],
        "confidence": 0.95,
        "corroborating_independence_groups": [],
        "question_family_tags": [],
        "primitive_tags": [],
        "allowed_component_ids": [],
        "structured_evidence_roles": [],
    }


def _large_stage_facts(
    *,
    count: int,
    mechanism_chars: int,
) -> list[Mapping[str, Any]]:
    return [
        {
            "fact_id": f"FACT-{index:04d}",
            "target_id": TARGET,
            "as_of_date": AS_OF_DATE,
            "subject": f"target operating mechanism {index}",
            "business_segment": "CORE",
            "product_family": "CORE_PRODUCT",
            "economic_mechanism": (
                f"distinct mechanism {index} "
                + ("경제 메커니즘 " * (mechanism_chars // 8))
            ),
            "predicate": f"DIRECT_MECHANISM_{index}",
            "value": {"value": index},
            "unit": "UNITS",
            "period": "2026Q2",
            "direction": "POSITIVE" if index % 2 == 0 else "COUNTER",
            "source_ids": [f"DOC-{index:04d}"],
            "claim_ids": [f"CLAIM-{index:04d}"],
            "quote_ids": [f"QUOTE-{index:04d}"],
            "current_lifecycle": "CURRENT",
            "source_independence_group": f"SOURCE-{index:04d}",
            "confidence": 0.9,
            "corroborating_independence_groups": [],
            "question_family_tags": [],
            "primitive_tags": [],
            "allowed_component_ids": [],
            "structured_evidence_roles": [],
        }
        for index in range(count)
    ]


def _stage_provider_payload(
    facts: list[Mapping[str, Any]] | tuple[Mapping[str, Any], ...],
) -> Mapping[str, Any]:
    projection = project_stage_gate_citable_facts(facts)
    return {
        "researcher_role": "STAGE_GATE_FACT_MAPPER",
        "target_id": TARGET,
        "archetype_id": "TEST_ARCHETYPE",
        "as_of_date": AS_OF_DATE,
        "evidence_contract": {
            "allowed_primitive_ids": ["test_primitive"],
            "green_gate_primitive_ids": [],
            "guard_modes": {},
            "primitive_aliases": {},
            "aggregation_rules": [],
        },
        "current_evidence_fact_graph": projection["facts"],
        "current_evidence_fact_projection": {
            key: value
            for key, value in projection.items()
            if key not in {"facts", "fact_id_by_row_index"}
        },
        "source_claims": {},
        "source_documents": {},
        "claim_fact_links": {},
        "instructions": "review every supplied fact row",
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
