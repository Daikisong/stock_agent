from __future__ import annotations

from contextlib import redirect_stdout
import hashlib
import io
import json
import multiprocessing
import os
import tempfile
import unittest
from pathlib import Path

from e2r.cli.run_e2r_researcher_mode_until_pass import (
    _build_research_provider,
    _research_provider_manifest,
    build_parser as build_phase94_parser,
)
from e2r.cli.import_e2r_collaboration_response import (
    main as import_response_main,
)
from e2r.research_brain.planning.provider_transport import (
    StructuredProviderRejected,
    StructuredProviderResponse,
    StructuredProviderUnavailable,
)
from e2r.research_brain.researcher_mode import (
    CodexResearcherProvider,
    CodexSubagentFallbackResearchProvider,
    CollaborationCodexResearcherProvider,
    CollaborationCodexSubagentTransport,
    ResearcherDocumentRanker,
    import_collaboration_response,
)
from e2r.research_brain.researcher_mode.collaboration_provider_bridge import (
    _prior_revision_fact_instruction,
    _prior_structured_valuation_fact_output_schema,
)
from e2r.research_brain.researcher_mode.component_researcher import (
    _single_payload_request_material,
)
from e2r.research_brain.researcher_mode.document_ranker import (
    candidate_materiality_full_prompt_input_hash,
)
from e2r.research_brain.researcher_mode.prompt_projection import (
    project_current_decision_citable_facts,
)


QUERY_RESPONSE = {
    "suggested_queries": [],
    "new_source_directions": [],
    "unresolved_research_notes": [],
}


class UsageLimitTransport:
    def __init__(self) -> None:
        self.call_count = 0

    def complete(self, *, prompt, output_schema, schema_name):
        del prompt, output_schema, schema_name
        self.call_count += 1
        raise StructuredProviderUnavailable(
            "ERROR: You've hit your usage limit. "
            "try again at Aug 5th, 2026 5:23 PM."
        )


class OtherFailureTransport:
    def __init__(self) -> None:
        self.call_count = 0

    def complete(self, *, prompt, output_schema, schema_name):
        del prompt, output_schema, schema_name
        self.call_count += 1
        raise StructuredProviderUnavailable("codex_cli_timeout")


class SuccessfulQueryTransport:
    def __init__(self) -> None:
        self.call_count = 0

    def complete(self, *, prompt, output_schema, schema_name):
        del prompt, output_schema, schema_name
        self.call_count += 1
        return StructuredProviderResponse(
            payload=QUERY_RESPONSE,
            raw_response=json.dumps(QUERY_RESPONSE),
            stderr="",
            returncode=0,
        )


class SuccessThenUsageLimitTransport(SuccessfulQueryTransport):
    def complete(self, *, prompt, output_schema, schema_name):
        if self.call_count:
            self.call_count += 1
            raise StructuredProviderUnavailable(
                "ERROR: You've hit your usage limit. "
                "try again at Aug 5th, 2026 5:23 PM."
            )
        return super().complete(
            prompt=prompt,
            output_schema=output_schema,
            schema_name=schema_name,
        )


def _business_model_response(payload):
    chunk = payload.get("loss_accounted_fact_chunk")
    if chunk:
        row_index = payload["current_evidence_fact_graph"][0][
            "fact_row_index"
        ]
        return {
            "business_model_summary": (
                f"chunk {chunk['chunk_index']} mechanism review"
            ),
            "revenue_engines": ["chunk revenue mechanism"],
            "cost_and_cash_drivers": ["chunk cash mechanism"],
            "capacity_and_supply_constraints": [
                "chunk capacity mechanism"
            ],
            "customer_and_channel_dependencies": [
                "chunk customer mechanism"
            ],
            "fact_row_indices": [row_index],
            "uncertainties": ["chunk uncertainty"],
            "confidence": 0.7,
            "research_complete": True,
        }
    partials = payload["loss_accounted_fact_chunk_synthesis"][
        "chunk_responses"
    ]
    return {
        "business_model_summary": "all chunks synthesized",
        "revenue_engines": ["all revenue mechanisms"],
        "cost_and_cash_drivers": ["all cash mechanisms"],
        "capacity_and_supply_constraints": [
            "all capacity mechanisms"
        ],
        "customer_and_channel_dependencies": [
            "all customer mechanisms"
        ],
        "fact_row_indices": [
            row_index
            for row in partials
            for row_index in row["response"]["fact_row_indices"]
        ],
        "uncertainties": ["cross-chunk uncertainty"],
        "confidence": 0.8,
        "research_complete": True,
    }


class BusinessChunkSuccessThenUsageLimitTransport:
    def __init__(self) -> None:
        self.call_count = 0
        self.payloads = []

    def provider_identity(self):
        return {
            "transport_class": self.__class__.__qualname__,
            "model": "test-codex",
        }

    def complete(self, *, prompt, output_schema, schema_name):
        del output_schema, schema_name
        payload = json.loads(prompt.rsplit("\n", 1)[-1])
        self.payloads.append(payload)
        self.call_count += 1
        if self.call_count > 1:
            raise StructuredProviderUnavailable(
                "ERROR: You've hit your usage limit. "
                "try again at Aug 5th, 2026 5:23 PM."
            )
        response = _business_model_response(payload)
        return StructuredProviderResponse(
            payload=response,
            raw_response=json.dumps(response),
            stderr="",
            returncode=0,
        )


class BoundedCodexResearcherProvider(CodexResearcherProvider):
    @property
    def memo_fact_prompt_chunk_chars(self) -> int:
        return 100_000


def _provider(primary_transport) -> CodexSubagentFallbackResearchProvider:
    return CodexSubagentFallbackResearchProvider(
        primary=CodexResearcherProvider(transport=primary_transport),  # type: ignore[arg-type]
        collaboration=CollaborationCodexResearcherProvider(
            transport=CollaborationCodexSubagentTransport()
        ),
    )


def _configure(provider, root: Path) -> Path:
    provider.configure_response_cache(
        root / "research_provider_response_cache"
    )
    return root / "collaboration_codex_subagent_provider"


def _request(journal_root: Path):
    paths = tuple((journal_root / "requests").glob("COLLABREQ-*.json"))
    if len(paths) != 1:
        raise AssertionError(f"expected one request, got {len(paths)}")
    return paths[0], json.loads(paths[0].read_text(encoding="utf-8"))


def _request_payload(request):
    return json.loads(request["prompt"].rsplit("\n", 1)[-1])


def _business_model_payload():
    facts = [
        {
            "fact_id": f"EFACT-{index:04d}",
            "target_id": "TEST",
            "as_of_date": "2026-06-29",
            "subject": "target memory business",
            "business_segment": "MEMORY",
            "product_family": "HBM",
            "economic_mechanism": (
                f"fact {index} " + "긴 경제 메커니즘 " * 500
            ),
            "predicate": f"CURRENT_HBM_MECHANISM_{index}",
            "value": index,
            "unit": "units",
            "period": "2026-06-29",
            "direction": (
                "POSITIVE" if index % 2 == 0 else "COUNTER"
            ),
            "current_lifecycle": "CURRENT",
            "confidence": 0.9,
            "structured_evidence_roles": [],
            "claim_ids": [f"CLAIM-{index:04d}"],
            "source_ids": [f"DOC-{index:04d}"],
            "source_independence_group": "issuer:test",
            "corroborating_independence_groups": ["issuer:test"],
            "allowed_component_ids": [],
            "question_family_tags": [],
            "primitive_tags": [],
        }
        for index in range(24)
    ]
    projection = project_current_decision_citable_facts(facts)
    return {
        "researcher_role": "BusinessMechanismResearcher",
        "target_id": "TEST",
        "archetype_id": "TEST_ARCHETYPE",
        "as_of_date": "2026-06-29",
        "current_evidence_fact_graph": projection["facts"],
        "current_evidence_fact_projection": {
            key: value
            for key, value in projection.items()
            if key not in {"facts", "fact_id_by_row_index"}
        },
        "source_claims": {},
        "source_documents": {},
        "source_coverage": ["ISSUER"],
    }


def _concurrent_import_worker(
    *,
    journal_root,
    request_id,
    response_payload,
    agent_id,
    barrier,
    result_queue,
):
    try:
        barrier.wait(timeout=10)
        envelope = import_collaboration_response(
            journal_root=journal_root,
            request_id=request_id,
            response_payload=response_payload,
            agent_id=agent_id,
            canonical_task_name=f"/root/{agent_id}",
            agent_model="codex-collaboration",
        )
    except Exception as exc:  # pragma: no cover - asserted in parent process
        result_queue.put(
            {
                "status": "ERROR",
                "error_type": exc.__class__.__name__,
                "error": str(exc),
            }
        )
    else:
        result_queue.put(
            {
                "status": "SUCCESS",
                "envelope": dict(envelope),
            }
        )


def _paused_import_worker(
    *,
    journal_root,
    request_id,
    response_payload,
    agent_id,
    reached_commit,
    resume_commit,
    result_queue,
):
    from e2r.research_brain.researcher_mode import (
        collaboration_provider_bridge as bridge,
    )

    original_create = bridge._atomic_create_json

    def pausing_create(path, value):
        if path.parent.name == "responses":
            reached_commit.set()
            if not resume_commit.wait(timeout=10):
                raise TimeoutError("import commit was not resumed")
        return original_create(path, value)

    bridge._atomic_create_json = pausing_create
    try:
        envelope = import_collaboration_response(
            journal_root=journal_root,
            request_id=request_id,
            response_payload=response_payload,
            agent_id=agent_id,
            canonical_task_name=f"/root/{agent_id}",
            agent_model="codex-collaboration",
        )
    except Exception as exc:  # pragma: no cover - asserted in parent process
        result_queue.put(
            {
                "worker": "IMPORT",
                "status": "ERROR",
                "error_type": exc.__class__.__name__,
                "error": str(exc),
            }
        )
    else:
        result_queue.put(
            {
                "worker": "IMPORT",
                "status": "SUCCESS",
                "envelope": dict(envelope),
            }
        )


def _semantic_quarantine_worker(
    *,
    journal_root,
    request_id,
    response_id,
    started,
    result_queue,
):
    transport = CollaborationCodexSubagentTransport()
    transport.configure_journal_root(journal_root)
    transport._last_request_id = request_id
    transport._last_response_id = response_id
    started.set()
    try:
        event = transport.invalidate_last_response("semantic poison")
    except Exception as exc:  # pragma: no cover - asserted in parent process
        result_queue.put(
            {
                "worker": "QUARANTINE",
                "status": "ERROR",
                "error_type": exc.__class__.__name__,
                "error": str(exc),
            }
        )
    else:
        result_queue.put(
            {
                "worker": "QUARANTINE",
                "status": "SUCCESS",
                "event": dict(event),
            }
        )


class E2RV5CollaborationProviderBridgeTests(unittest.TestCase):
    def test_v6_fact_instruction_recovery_is_frozen_across_v7_clarifications(
        self,
    ) -> None:
        instruction = _prior_revision_fact_instruction()

        # This is the exact instruction hash carried by immutable v6
        # Collaboration requests.  Reconstructing only the newly-added enum
        # token is insufficient because v7 also changed FORWARD_GUIDANCE
        # wording and the adjacent "Tags" sentence.
        self.assertEqual(
            hashlib.sha256(instruction.encode("utf-8")).hexdigest(),
            "948201a296d0d2be4e8d4a4f87c5b15be74aebab8b82fee3aa231128ffc03bab",
        )
        self.assertNotIn(
            "FORWARD_GUIDANCE includes a numeric issuer-owned future",
            instruction,
        )
        self.assertNotIn(
            "LATEST_ACTUAL_DEPRECIATION_AMORTIZATION",
            instruction,
        )
        self.assertIn(
            "Tags are extraction context only and never assign points.",
            instruction,
        )

    def test_candidate_materiality_scope_attestation_binds_official_request(
        self,
    ) -> None:
        with tempfile.TemporaryDirectory() as directory:
            provider = CollaborationCodexResearcherProvider(
                transport=CollaborationCodexSubagentTransport()
            )
            provider.configure_response_cache(
                Path(directory) / "research_provider_response_cache"
            )
            journal = (
                Path(directory) / "collaboration_codex_subagent_provider"
            )
            ranker = ResearcherDocumentRanker(provider=provider)
            kwargs = {
                "target_id": "CURRENT-TARGET",
                "target_name": "Current Corp",
                "as_of_date": "2026-07-12",
                "open_objectives": [
                    {
                        "objective_id": "OBJ-1",
                        "question": "현재 고객 공식 확인이 있는가?",
                    }
                ],
                "candidates": [
                    {
                        "candidate_id": "CAND-1",
                        "title": "customer update",
                        "url": "https://example.com/update",
                        "normalized_url": "https://example.com/update",
                        "snippet": "customer update",
                        "source": "test",
                        "query_ids": ["Q-1"],
                        "materiality_query_ids": ["Q-1"],
                        "objective_ids": ["OBJ-1"],
                        "requested_source_families": [
                            "CUSTOMER_OFFICIAL"
                        ],
                    }
                ],
                "current_evidence_facts": [],
                "target_business_model": None,
                "source_coverage": [],
            }
            first = ranker.rank_candidates(**kwargs)
            self.assertEqual(first.status, "PENDING")
            _, request = _request(journal)
            response = {
                "decisions": [
                    {
                        "candidate_id": "CAND-1",
                        "material_relevance": False,
                        "priority": 0.1,
                        "objective_ids": [],
                        "matched_requested_source_family": "NONE",
                        "rationale": "현재 질문을 직접 해결하지 않는다.",
                    }
                ],
                "ranking_complete": True,
                "unresolved_notes": [],
            }
            import_collaboration_response(
                journal_root=journal,
                request_id=request["request_id"],
                response_payload=response,
                agent_id="agent-scope",
                canonical_task_name="/root/rank_scope",
                agent_model="codex-collaboration",
            )

            roster = provider.validated_candidate_materiality_scope_attestations(
                target_id="CURRENT-TARGET",
                as_of_date="2026-07-12",
            )

            self.assertIsNotNone(roster)
            assert roster is not None
            self.assertEqual(roster["attestation_count"], 1)
            attestation = next(
                iter(roster["attestations_by_scope_receipt_id"].values())
            )
            self.assertEqual(attestation["candidate_id"], "CAND-1")
            self.assertEqual(
                attestation["candidate_objective_ids"], ["OBJ-1"]
            )
            self.assertEqual(
                attestation["requested_source_families"],
                ["CUSTOMER_OFFICIAL"],
            )
            self.assertEqual(attestation["materiality_query_ids"], ["Q-1"])
            self.assertRegex(
                str(attestation["decision_input_hash"]), r"^[0-9a-f]{64}$"
            )
            self.assertRegex(
                str(attestation["decision_prompt_input_hash"]),
                r"^[0-9a-f]{64}$",
            )
            request_candidate = _request_payload(request)[
                "discovery_candidates"
            ][0]
            self.assertEqual(
                attestation["decision_prompt_input_hash"],
                candidate_materiality_full_prompt_input_hash(
                    request_candidate
                ),
            )
            self.assertEqual(
                candidate_materiality_full_prompt_input_hash(
                    request_candidate
                ),
                candidate_materiality_full_prompt_input_hash(
                    kwargs["candidates"][0]
                ),
            )

    def test_candidate_scope_attestation_fails_closed_on_request_tamper(
        self,
    ) -> None:
        with tempfile.TemporaryDirectory() as directory:
            provider = CollaborationCodexResearcherProvider(
                transport=CollaborationCodexSubagentTransport()
            )
            provider.configure_response_cache(
                Path(directory) / "research_provider_response_cache"
            )
            journal = (
                Path(directory) / "collaboration_codex_subagent_provider"
            )
            ranker = ResearcherDocumentRanker(provider=provider)
            result = ranker.rank_candidates(
                target_id="CURRENT-TARGET",
                target_name="Current Corp",
                as_of_date="2026-07-12",
                open_objectives=[
                    {"objective_id": "OBJ-1", "question": "현재 반증은?"}
                ],
                candidates=[
                    {
                        "candidate_id": "CAND-1",
                        "title": "issuer update",
                        "url": "https://example.com/update",
                        "snippet": "issuer update",
                        "source": "test",
                        "objective_ids": ["OBJ-1"],
                        "requested_source_families": [
                            "ISSUER_PRESENTATION"
                        ],
                    }
                ],
                current_evidence_facts=[],
                target_business_model=None,
                source_coverage=[],
            )
            self.assertEqual(result.status, "PENDING")
            request_path, request = _request(journal)
            request["prompt_hash"] = "0" * 64
            request_path.write_text(
                json.dumps(request, ensure_ascii=False),
                encoding="utf-8",
            )

            self.assertIsNone(
                provider.validated_candidate_materiality_scope_attestations(
                    target_id="CURRENT-TARGET",
                    as_of_date="2026-07-12",
                )
            )

    def test_identical_decision_can_attest_two_legitimate_ranking_scopes(
        self,
    ) -> None:
        with tempfile.TemporaryDirectory() as directory:
            provider = CollaborationCodexResearcherProvider(
                transport=CollaborationCodexSubagentTransport()
            )
            provider.configure_response_cache(
                Path(directory) / "research_provider_response_cache"
            )
            journal = (
                Path(directory) / "collaboration_codex_subagent_provider"
            )
            ranker = ResearcherDocumentRanker(provider=provider)
            response_payload = {
                "decisions": [
                    {
                        "candidate_id": "CAND-SHARED",
                        "material_relevance": False,
                        "priority": 0.1,
                        "objective_ids": [],
                        "matched_requested_source_family": "NONE",
                        "rationale": "현재 범위를 직접 해결하지 않는다.",
                    }
                ],
                "ranking_complete": True,
                "unresolved_notes": [],
            }
            for index, (objective_id, query_id, source_family) in enumerate(
                (
                    ("OBJ-A", "Q-A", "ISSUER_PRESENTATION"),
                    ("OBJ-B", "Q-B", "CUSTOMER_OFFICIAL"),
                )
            ):
                result = ranker.rank_candidates(
                    target_id="CURRENT-TARGET",
                    target_name="Current Corp",
                    as_of_date="2026-07-12",
                    open_objectives=[
                        {
                            "objective_id": objective_id,
                            "question": f"현재 반증 범위 {index}",
                        }
                    ],
                    candidates=[
                        {
                            "candidate_id": "CAND-SHARED",
                            "title": "same unrelated page",
                            "url": "https://example.com/shared",
                            "snippet": "same unrelated snippet",
                            "source": "test",
                            "query_ids": [query_id],
                            "materiality_query_ids": [query_id],
                            "objective_ids": [objective_id],
                            "requested_source_families": [source_family],
                        }
                    ],
                    current_evidence_facts=[],
                    target_business_model=None,
                    source_coverage=[],
                )
                self.assertEqual(result.status, "PENDING")
                pending_requests = []
                for request_path in sorted(
                    (journal / "requests").glob("COLLABREQ-*.json")
                ):
                    request = json.loads(
                        request_path.read_text(encoding="utf-8")
                    )
                    if not (
                        journal / "responses" / request_path.name
                    ).is_file():
                        pending_requests.append(request)
                self.assertEqual(len(pending_requests), 1)
                import_collaboration_response(
                    journal_root=journal,
                    request_id=pending_requests[0]["request_id"],
                    response_payload=response_payload,
                    agent_id=f"agent-scope-{index}",
                    canonical_task_name=f"/root/rank_scope_{index}",
                    agent_model="codex-collaboration",
                )

            roster = provider.validated_candidate_materiality_scope_attestations(
                target_id="CURRENT-TARGET",
                as_of_date="2026-07-12",
            )

            self.assertIsNotNone(roster)
            assert roster is not None
            self.assertEqual(roster["attestation_count"], 2)
            attestations = tuple(
                roster["attestations_by_scope_receipt_id"].values()
            )
            self.assertEqual(
                len({row["decision_id"] for row in attestations}), 1
            )
            self.assertEqual(
                {
                    tuple(row["materiality_query_ids"])
                    for row in attestations
                },
                {("Q-A",), ("Q-B",)},
            )

    def test_v4_fact_semantics_migration_receipt_is_read_only_and_exact(
        self,
    ) -> None:
        with tempfile.TemporaryDirectory() as directory:
            provider = CollaborationCodexResearcherProvider(
                transport=CollaborationCodexSubagentTransport()
            )
            journal = _configure(provider, Path(directory))
            current_payload = {
                "target_id": "CURRENT-TARGET",
                "as_of_date": "2026-07-12",
                "archetype_hypothesis": "C06_HBM_MEMORY_CUSTOMER_CAPACITY",
                "fact_extraction_semantics_version": (
                    "e2r_v5_structured_valuation_roles_v5"
                ),
                "current_evidence_facts": {},
                "score_gap_context": {},
                "full_documents": [
                    {
                        "document_id": "DOCUMENT-V4",
                        "source_family": "OPENDART",
                        "content_text": "literal filing text",
                    }
                ],
            }
            (
                _safe,
                current_schema,
                _prompt,
                _prompt_hash,
                _schema_hash,
            ) = _single_payload_request_material(
                pass_name="EVIDENCE_FACT_EXTRACTION",
                payload=current_payload,
            )
            prior_schema = _prior_structured_valuation_fact_output_schema(
                current_schema
            )
            self.assertIsNotNone(prior_schema)
            historical_payload = {
                **current_payload,
                "fact_extraction_semantics_version": (
                    "e2r_v5_source_boundary_context_v4"
                ),
            }
            (
                _old_safe,
                _old_current_schema,
                historical_prompt,
                _old_prompt_hash,
                _old_schema_hash,
            ) = _single_payload_request_material(
                pass_name="EVIDENCE_FACT_EXTRACTION",
                payload=historical_payload,
            )
            with self.assertRaisesRegex(
                StructuredProviderUnavailable,
                "COLLABORATION_RESPONSE_PENDING",
            ):
                provider.transport.complete(
                    prompt=historical_prompt,
                    output_schema=prior_schema,
                    schema_name="e2r_v5_evidence_fact_extraction",
                )
            _, request = _request(journal)
            import_collaboration_response(
                journal_root=journal,
                request_id=request["request_id"],
                response_payload={
                    "facts": [],
                    "document_dispositions": [],
                    "unresolved_document_ids": [],
                    "unresolved_research_notes": [],
                    "extraction_complete": True,
                },
                agent_id="fact-migration-agent",
                canonical_task_name="/root/fact_migration",
                agent_model="codex-collaboration",
            )
            request_path = (
                journal / "requests" / f"{request['request_id']}.json"
            )
            response_path = (
                journal / "responses" / f"{request['request_id']}.json"
            )
            before = (request_path.read_bytes(), response_path.read_bytes())

            recovered = provider.validated_fact_extraction_semantics_migration_materials(
                target_id="CURRENT-TARGET",
                as_of_date="2026-07-12",
                archetype_id="C06_HBM_MEMORY_CUSTOMER_CAPACITY",
                document_ids=("DOCUMENT-V4",),
            )

            self.assertIsNotNone(recovered)
            assert recovered is not None
            self.assertEqual(
                recovered["recovery_material_status"], "COMPLETE"
            )
            self.assertEqual(len(recovered["materials"]), 1)
            self.assertEqual(
                recovered["materials"][0]["request_id"],
                request["request_id"],
            )
            self.assertEqual(
                before,
                (request_path.read_bytes(), response_path.read_bytes()),
            )
            tampered_request = dict(request)
            tampered_request["prompt_hash"] = "0" * 64
            request_path.write_text(
                json.dumps(tampered_request, ensure_ascii=False),
                encoding="utf-8",
            )
            invalid = provider.validated_fact_extraction_semantics_migration_materials(
                target_id="CURRENT-TARGET",
                as_of_date="2026-07-12",
                archetype_id="C06_HBM_MEMORY_CUSTOMER_CAPACITY",
                document_ids=("DOCUMENT-V4",),
            )
            self.assertIsNotNone(invalid)
            assert invalid is not None
            self.assertEqual(
                invalid["recovery_material_status"], "INVALID"
            )
            self.assertEqual(invalid["materials"], [])
            request_path.write_text(
                json.dumps(request, ensure_ascii=False),
                encoding="utf-8",
            )
            renamed_path = (
                request_path.parent / ("COLLABREQ-" + "f" * 64 + ".json")
            )
            request_path.rename(renamed_path)
            renamed = provider.validated_fact_extraction_semantics_migration_materials(
                target_id="CURRENT-TARGET",
                as_of_date="2026-07-12",
                archetype_id="C06_HBM_MEMORY_CUSTOMER_CAPACITY",
                document_ids=("DOCUMENT-V4",),
            )
            self.assertIsNotNone(renamed)
            assert renamed is not None
            self.assertEqual(
                renamed["recovery_material_status"], "INVALID"
            )
            renamed_path.rename(request_path)
            broken_prompt_request = dict(request)
            broken_prompt_request["prompt"] = str(request["prompt"])[:-1]
            request_path.write_text(
                json.dumps(broken_prompt_request, ensure_ascii=False),
                encoding="utf-8",
            )
            broken_prompt = provider.validated_fact_extraction_semantics_migration_materials(
                target_id="CURRENT-TARGET",
                as_of_date="2026-07-12",
                archetype_id="C06_HBM_MEMORY_CUSTOMER_CAPACITY",
                document_ids=("DOCUMENT-V4",),
            )
            self.assertIsNotNone(broken_prompt)
            assert broken_prompt is not None
            self.assertEqual(
                broken_prompt["recovery_material_status"], "INVALID"
            )

    def test_v4_fact_semantics_migration_distinguishes_absent_receipts(
        self,
    ) -> None:
        with tempfile.TemporaryDirectory() as directory:
            provider = CollaborationCodexResearcherProvider(
                transport=CollaborationCodexSubagentTransport()
            )
            journal = _configure(provider, Path(directory))

            recovered = provider.validated_fact_extraction_semantics_migration_materials(
                target_id="CURRENT-TARGET",
                as_of_date="2026-07-12",
                archetype_id="C06_HBM_MEMORY_CUSTOMER_CAPACITY",
                document_ids=("DOCUMENT-WITHOUT-V4-RECEIPT",),
            )

            self.assertIsNotNone(recovered)
            assert recovered is not None
            self.assertEqual(
                recovered["recovery_material_status"], "ABSENT"
            )
            self.assertEqual(recovered["materials"], [])
            self.assertEqual(
                tuple(journal.rglob("COLLABREQ-*.json")), ()
            )

    def test_default_composite_primary_keeps_normal_codex_cache_identity(
        self,
    ) -> None:
        normal = CodexResearcherProvider.default(
            working_directory="/repo",
            timeout_seconds=300.0,
        )
        composite = CodexSubagentFallbackResearchProvider.default(
            working_directory="/repo",
            timeout_seconds=300.0,
        )

        self.assertEqual(
            composite.primary.provider_name,
            normal.provider_name,
        )
        self.assertEqual(
            composite.primary._provider_identity(),
            normal._provider_identity(),
        )

    def test_exact_primary_codex_cache_hit_precedes_collaboration_journal(
        self,
    ) -> None:
        with tempfile.TemporaryDirectory() as directory:
            transport = SuccessThenUsageLimitTransport()
            provider = _provider(transport)
            journal = _configure(provider, Path(directory))
            payload = {
                "target_id": "CURRENT-TARGET",
                "as_of_date": "2026-07-12",
            }

            first = provider.complete(
                pass_name="SOURCE_QUERY_GENERATION",
                payload=payload,
            )
            with self.assertRaisesRegex(
                StructuredProviderUnavailable,
                "COLLABORATION_RESPONSE_PENDING",
            ):
                provider.complete(
                    pass_name="SOURCE_QUERY_GENERATION",
                    payload={**payload, "target_id": "UNCACHED-TARGET"},
                )
            request_count_before_cache_replay = len(
                tuple((journal / "requests").glob("*.json"))
            )
            second = provider.complete(
                pass_name="SOURCE_QUERY_GENERATION",
                payload=payload,
            )

            self.assertEqual(first, QUERY_RESPONSE)
            self.assertEqual(second, QUERY_RESPONSE)
            self.assertEqual(transport.call_count, 2)
            self.assertTrue(provider.primary.calls[-1]["cache_hit"])
            self.assertEqual(request_count_before_cache_replay, 1)
            self.assertEqual(
                len(tuple((journal / "requests").glob("*.json"))),
                request_count_before_cache_replay,
            )

    def test_usage_limit_cache_miss_writes_full_request_and_resumes_after_import(
        self,
    ) -> None:
        with tempfile.TemporaryDirectory() as directory:
            provider = _provider(UsageLimitTransport())
            journal = _configure(provider, Path(directory))
            payload = {
                "target_id": "CURRENT-TARGET",
                "as_of_date": "2026-07-12",
            }

            with self.assertRaisesRegex(
                StructuredProviderUnavailable,
                "COLLABORATION_RESPONSE_PENDING",
            ):
                provider.complete(
                    pass_name="SOURCE_QUERY_GENERATION",
                    payload=payload,
                )

            request_path, request = _request(journal)
            self.assertEqual(request["pass_name"], "SOURCE_QUERY_GENERATION")
            self.assertIn("independent E2R 2.0 research analyst", request["prompt"])
            self.assertEqual(
                request["prompt_hash"],
                __import__("hashlib").sha256(
                    request["prompt"].encode("utf-8")
                ).hexdigest(),
            )
            self.assertIsInstance(request["output_schema"], dict)
            self.assertFalse(request["score_or_stage_authority"])
            self.assertFalse(request["production_score_authority"])
            self.assertTrue(request_path.name.startswith("COLLABREQ-"))

            envelope = import_collaboration_response(
                journal_root=journal,
                request_id=request["request_id"],
                response_payload=QUERY_RESPONSE,
                agent_id="agent-123",
                canonical_task_name="/root/rank_partition_0",
                agent_model="codex-collaboration",
            )
            resumed = provider.complete(
                pass_name="SOURCE_QUERY_GENERATION",
                payload=payload,
            )

            self.assertEqual(resumed, QUERY_RESPONSE)
            self.assertFalse(envelope["score_or_stage_authority"])
            self.assertEqual(
                envelope["provenance"]["provenance_assurance"],
                "ORCHESTRATOR_ATTESTED_NOT_CRYPTOGRAPHIC",
            )
            audit = provider.response_cache_audit()
            self.assertTrue(audit["provider_usage_limit_detected"])
            self.assertEqual(
                audit["collaboration_journal"]["validated_response_count"],
                1,
            )
            self.assertEqual(
                provider.calls[-1]["provider_route"],
                "COLLABORATION_CODEX_SUBAGENT",
            )

    def test_validated_journal_recovers_exact_request_payload_read_only(
        self,
    ) -> None:
        with tempfile.TemporaryDirectory() as directory:
            provider = CollaborationCodexResearcherProvider(
                transport=CollaborationCodexSubagentTransport()
            )
            journal = _configure(provider, Path(directory))
            payload = {
                "target_id": "CURRENT-TARGET",
                "as_of_date": "2026-07-12",
                "prior_supervisor_review": {
                    "prior_review_semantic_hash": "a" * 64,
                    "score_authority": False,
                },
            }
            with self.assertRaisesRegex(
                StructuredProviderUnavailable,
                "COLLABORATION_RESPONSE_PENDING",
            ):
                provider.complete(
                    pass_name="SOURCE_QUERY_GENERATION",
                    payload=payload,
                )
            _, request = _request(journal)
            self.assertEqual(
                provider.validated_pending_request_payload(
                    pass_name="SOURCE_QUERY_GENERATION",
                    prompt_hash=request["prompt_hash"],
                ),
                payload,
            )
            self.assertIsNone(
                provider.validated_request_payload(
                    pass_name="SOURCE_QUERY_GENERATION",
                    prompt_hash=request["prompt_hash"],
                )
            )
            envelope = import_collaboration_response(
                journal_root=journal,
                request_id=request["request_id"],
                response_payload=QUERY_RESPONSE,
                agent_id="agent-recover",
                canonical_task_name="/root/recover_request_payload",
                agent_model="codex-collaboration",
            )
            response_path = (
                journal
                / "responses"
                / f"{request['request_id']}.json"
            )
            response_bytes = response_path.read_bytes()
            response_path.unlink()
            self.assertIsNone(
                provider.validated_request_payload(
                    pass_name="SOURCE_QUERY_GENERATION",
                    prompt_hash=request["prompt_hash"],
                )
            )
            self.assertEqual(
                provider.validated_pending_request_payload(
                    pass_name="SOURCE_QUERY_GENERATION",
                    prompt_hash=request["prompt_hash"],
                ),
                payload,
            )
            response_path.write_bytes(response_bytes)
            tampered_response = json.loads(response_bytes)
            tampered_response["validation"]["request_hashes_valid"] = False
            response_path.write_text(
                json.dumps(tampered_response, ensure_ascii=False),
                encoding="utf-8",
            )
            self.assertIsNone(
                provider.validated_request_payload(
                    pass_name="SOURCE_QUERY_GENERATION",
                    prompt_hash=request["prompt_hash"],
                )
            )
            self.assertIsNone(
                provider.validated_pending_request_payload(
                    pass_name="SOURCE_QUERY_GENERATION",
                    prompt_hash=request["prompt_hash"],
                )
            )
            response_path.write_bytes(response_bytes)
            before = {
                path.relative_to(journal): path.read_bytes()
                for path in journal.rglob("*.json")
            }

            recovered = provider.validated_request_payload(
                pass_name="SOURCE_QUERY_GENERATION",
                prompt_hash=request["prompt_hash"],
            )

            self.assertEqual(recovered, payload)
            self.assertEqual(
                {
                    path.relative_to(journal): path.read_bytes()
                    for path in journal.rglob("*.json")
                },
                before,
            )
            self.assertIsNone(
                provider.validated_request_payload(
                    pass_name="SOURCE_QUERY_GENERATION",
                    prompt_hash="f" * 64,
                )
            )

            quarantine_path = (
                journal
                / "quarantine"
                / request["request_id"]
                / f"{envelope['response_id']}.json"
            )
            quarantine_path.parent.mkdir(parents=True, exist_ok=True)
            quarantine_path.write_text("{}\n", encoding="utf-8")
            response_path.unlink()
            self.assertIsNone(
                provider.validated_request_payload(
                    pass_name="SOURCE_QUERY_GENERATION",
                    prompt_hash=request["prompt_hash"],
                )
            )
            self.assertIsNone(
                provider.validated_pending_request_payload(
                    pass_name="SOURCE_QUERY_GENERATION",
                    prompt_hash=request["prompt_hash"],
                )
            )

    def test_clean_resume_recovers_exact_peer_retry_after_primary_quarantine(
        self,
    ) -> None:
        with tempfile.TemporaryDirectory() as directory:
            provider = CollaborationCodexResearcherProvider(
                transport=CollaborationCodexSubagentTransport()
            )
            journal = _configure(provider, Path(directory))
            primary_payload = {
                "target_id": "005930",
                "as_of_date": "2026-07-12",
            }
            incomplete_response = {
                "peers": [
                    {
                        "peer_symbol": symbol,
                        "peer_name": name,
                        "shared_economic_drivers": ["same cycle"],
                        "material_differences": ["evidence pending"],
                        "comparability_rationale": "candidate only",
                        "confidence": 0.1,
                    }
                    for symbol, name in (
                        ("000660", "SK하이닉스"),
                        ("000990", "DB하이텍"),
                    )
                ],
                "selection_complete": False,
                "selection_rationale": "selection is pending",
                "unresolved_research_notes": ["more evidence required"],
            }
            complete_response = {
                **incomplete_response,
                "selection_complete": True,
                "selection_rationale": "selection task is complete",
            }

            with self.assertRaisesRegex(
                StructuredProviderUnavailable,
                "COLLABORATION_RESPONSE_PENDING",
            ):
                provider.complete(
                    pass_name="STRUCTURED_PEER_SELECTION",
                    payload=primary_payload,
                )
            _, primary_request = _request(journal)
            import_collaboration_response(
                journal_root=journal,
                request_id=primary_request["request_id"],
                response_payload=incomplete_response,
                agent_id="peer-primary-agent",
                canonical_task_name="/root/peer_primary",
                agent_model="codex-collaboration",
            )
            self.assertEqual(
                provider.complete(
                    pass_name="STRUCTURED_PEER_SELECTION",
                    payload=primary_payload,
                ),
                incomplete_response,
            )
            provider.invalidate_last_response_cache(
                "STRUCTURED_PEER_RESPONSE_VALIDATION_REJECTED:"
                "FRESH_SELECTION_RESPONSE_ATTEMPT_1:"
                "peer selection is incomplete"
            )
            retry_payload = {
                **primary_payload,
                "peer_selection_retry_context": {
                    "validation_error": "peer selection is incomplete",
                    "instruction": (
                        "Rewrite the complete peer selection under the original "
                        "two-to-five peer contract; do not invent any valuation values."
                    ),
                },
            }
            with self.assertRaisesRegex(
                StructuredProviderUnavailable,
                "COLLABORATION_RESPONSE_PENDING",
            ):
                provider.complete(
                    pass_name="STRUCTURED_PEER_SELECTION",
                    payload=retry_payload,
                )
            requests = [
                json.loads(path.read_text(encoding="utf-8"))
                for path in (journal / "requests").glob("COLLABREQ-*.json")
            ]
            retry_requests = [
                row
                for row in requests
                if row["request_id"] != primary_request["request_id"]
            ]
            self.assertEqual(len(retry_requests), 1)
            retry_request = retry_requests[0]
            import_collaboration_response(
                journal_root=journal,
                request_id=retry_request["request_id"],
                response_payload=complete_response,
                agent_id="peer-retry-agent",
                canonical_task_name="/root/peer_retry",
                agent_model="codex-collaboration",
            )

            self.assertEqual(
                provider.validated_peer_selection_retry_payload(
                    primary_payload=primary_payload,
                ),
                retry_payload,
            )
            self.assertEqual(
                provider.complete(
                    pass_name="STRUCTURED_PEER_SELECTION",
                    payload=retry_payload,
                ),
                complete_response,
            )

    def test_clean_resume_recovers_fact_pagination_origin_before_page_two(
        self,
    ) -> None:
        with tempfile.TemporaryDirectory() as directory:
            provider = CollaborationCodexResearcherProvider(
                transport=CollaborationCodexSubagentTransport()
            )
            journal = _configure(provider, Path(directory))
            origin_payload = {
                "target_id": "CURRENT-TARGET",
                "as_of_date": "2026-07-12",
                "full_documents": [
                    {
                        "document_id": "DOCUMENT-1",
                        "content_text": "literal source text",
                    }
                ],
                "score_gap_context": {"pending": ["old gap"]},
            }
            empty_response = {
                "facts": [],
                "document_dispositions": [],
                "unresolved_document_ids": [],
                "unresolved_research_notes": [],
                "extraction_complete": True,
            }
            with self.assertRaisesRegex(
                StructuredProviderUnavailable,
                "COLLABORATION_RESPONSE_PENDING",
            ):
                provider.complete(
                    pass_name="EVIDENCE_FACT_EXTRACTION",
                    payload=origin_payload,
                )
            _, origin_request = _request(journal)
            import_collaboration_response(
                journal_root=journal,
                request_id=origin_request["request_id"],
                response_payload=empty_response,
                agent_id="fact-page-one-agent",
                canonical_task_name="/root/fact_page_one",
                agent_model="codex-collaboration",
            )
            page_two_payload = {
                **origin_payload,
                "fact_extraction_continuation_context": {
                    "page_number": 2,
                    "page_fact_limit": 12,
                    "required_document_ids": ["DOCUMENT-1"],
                    "previously_accepted_facts": [
                        {
                            "document_id": "DOCUMENT-1",
                            "exact_quote": "literal source text",
                        }
                    ],
                    "instruction": "continue without duplicates",
                },
            }
            with self.assertRaisesRegex(
                StructuredProviderUnavailable,
                "COLLABORATION_RESPONSE_PENDING",
            ):
                provider.complete(
                    pass_name="EVIDENCE_FACT_EXTRACTION",
                    payload=page_two_payload,
                )

            current_payload = {
                **origin_payload,
                "score_gap_context": {"pending": ["new downstream gap"]},
            }
            self.assertEqual(
                provider.validated_fact_extraction_pagination_origin_payload(
                    primary_payload=current_payload,
                ),
                origin_payload,
            )

    def test_multichunk_usage_limit_falls_back_only_for_missing_leaf(
        self,
    ) -> None:
        with tempfile.TemporaryDirectory() as directory:
            transport = BusinessChunkSuccessThenUsageLimitTransport()
            provider = CodexSubagentFallbackResearchProvider(
                primary=BoundedCodexResearcherProvider(
                    transport=transport  # type: ignore[arg-type]
                ),
                collaboration=CollaborationCodexResearcherProvider(
                    transport=CollaborationCodexSubagentTransport()
                ),
            )
            journal = _configure(provider, Path(directory))
            payload = _business_model_payload()

            with self.assertRaisesRegex(
                StructuredProviderUnavailable,
                "COLLABORATION_RESPONSE_PENDING",
            ):
                provider.complete(
                    pass_name="BUSINESS_MODEL_RESEARCH",
                    payload=payload,
                )

            request_paths = tuple(
                (journal / "requests").glob("COLLABREQ-*.json")
            )
            self.assertEqual(len(request_paths), 1)
            second_chunk_request = json.loads(
                request_paths[0].read_text(encoding="utf-8")
            )
            second_chunk_payload = _request_payload(second_chunk_request)
            self.assertEqual(
                second_chunk_payload["loss_accounted_fact_chunk"][
                    "chunk_index"
                ],
                1,
            )
            self.assertEqual(transport.call_count, 2)

            import_collaboration_response(
                journal_root=journal,
                request_id=second_chunk_request["request_id"],
                response_payload=_business_model_response(
                    second_chunk_payload
                ),
                agent_id="agent-chunk-1",
                canonical_task_name="/root/business_chunk_1",
                agent_model="codex-collaboration",
            )

            with self.assertRaisesRegex(
                StructuredProviderUnavailable,
                "COLLABORATION_RESPONSE_PENDING",
            ):
                provider.complete(
                    pass_name="BUSINESS_MODEL_RESEARCH",
                    payload=payload,
                )

            requests = [
                json.loads(path.read_text(encoding="utf-8"))
                for path in (
                    journal / "requests"
                ).glob("COLLABREQ-*.json")
            ]
            self.assertEqual(len(requests), 2)
            request_payloads = [
                _request_payload(request) for request in requests
            ]
            self.assertEqual(
                sum(
                    (
                        row.get("loss_accounted_fact_chunk") or {}
                    ).get("chunk_index")
                    == 0
                    for row in request_payloads
                ),
                0,
            )
            synthesis_requests = [
                request
                for request, row in zip(requests, request_payloads)
                if row.get("loss_accounted_fact_chunk_synthesis")
            ]
            self.assertEqual(len(synthesis_requests), 1)
            self.assertTrue(provider.primary.calls[-3]["cache_hit"])
            self.assertEqual(transport.call_count, 2)

            synthesis_request = synthesis_requests[0]
            synthesis_payload = _request_payload(synthesis_request)
            import_collaboration_response(
                journal_root=journal,
                request_id=synthesis_request["request_id"],
                response_payload=_business_model_response(
                    synthesis_payload
                ),
                agent_id="agent-synthesis",
                canonical_task_name="/root/business_synthesis",
                agent_model="codex-collaboration",
            )
            response = provider.complete(
                pass_name="BUSINESS_MODEL_RESEARCH",
                payload=payload,
            )

            self.assertTrue(response["research_complete"])
            self.assertEqual(
                len(
                    tuple(
                        (journal / "requests").glob(
                            "COLLABREQ-*.json"
                        )
                    )
                ),
                2,
            )
            self.assertEqual(transport.call_count, 2)
            self.assertEqual(
                provider.calls[-1]["provider_route"],
                "COLLABORATION_CODEX_SUBAGENT",
            )

    def test_non_usage_provider_failure_does_not_open_subagent_fallback(
        self,
    ) -> None:
        with tempfile.TemporaryDirectory() as directory:
            provider = _provider(OtherFailureTransport())
            journal = _configure(provider, Path(directory))

            with self.assertRaisesRegex(
                StructuredProviderUnavailable,
                "codex_cli_timeout",
            ):
                provider.complete(
                    pass_name="SOURCE_QUERY_GENERATION",
                    payload={
                        "target_id": "CURRENT-TARGET",
                        "as_of_date": "2026-07-12",
                    },
                )

            self.assertEqual(tuple((journal / "requests").glob("*.json")), ())
            self.assertEqual(provider.calls[-1]["provider_route"], "CODEX_CLI")

    def test_import_rejects_schema_violation_and_request_hash_tampering(
        self,
    ) -> None:
        with tempfile.TemporaryDirectory() as directory:
            provider = _provider(UsageLimitTransport())
            journal = _configure(provider, Path(directory))
            with self.assertRaises(StructuredProviderUnavailable):
                provider.complete(
                    pass_name="SOURCE_QUERY_GENERATION",
                    payload={
                        "target_id": "CURRENT-TARGET",
                        "as_of_date": "2026-07-12",
                    },
                )
            request_path, request = _request(journal)

            with self.assertRaisesRegex(ValueError, "schema violation"):
                import_collaboration_response(
                    journal_root=journal,
                    request_id=request["request_id"],
                    response_payload={"suggested_queries": []},
                    agent_id="agent-123",
                    canonical_task_name="/root/rank_partition_0",
                    agent_model="codex-collaboration",
                )
            self.assertFalse(
                (journal / "responses" / request_path.name).exists()
            )

            request["prompt"] += "\ntampered"
            request_path.write_text(
                json.dumps(request, ensure_ascii=False),
                encoding="utf-8",
            )
            with self.assertRaisesRegex(ValueError, "content hash mismatch"):
                import_collaboration_response(
                    journal_root=journal,
                    request_id=request["request_id"],
                    response_payload=QUERY_RESPONSE,
                    agent_id="agent-123",
                    canonical_task_name="/root/rank_partition_0",
                    agent_model="codex-collaboration",
                )

    def test_request_contract_rejects_schema_flag_and_identity_tampering(
        self,
    ) -> None:
        def canonical_hash(value):
            return hashlib.sha256(
                json.dumps(
                    value,
                    ensure_ascii=False,
                    sort_keys=True,
                    separators=(",", ":"),
                ).encode("utf-8")
            ).hexdigest()

        for variant in (
            "schema_pass_mismatch",
            "response_import_disabled",
            "provider_identity",
            "extra_key",
        ):
            with self.subTest(variant=variant):
                with tempfile.TemporaryDirectory() as directory:
                    provider = _provider(UsageLimitTransport())
                    journal = _configure(provider, Path(directory))
                    with self.assertRaises(
                        StructuredProviderUnavailable
                    ):
                        provider.complete(
                            pass_name="SOURCE_QUERY_GENERATION",
                            payload={
                                "target_id": f"TARGET-{variant}",
                                "as_of_date": "2026-07-12",
                            },
                        )
                    request_path, original = _request(journal)
                    tampered = dict(original)
                    if variant == "schema_pass_mismatch":
                        tampered["schema_name"] = (
                            "e2r_v5_business_model_research"
                        )
                    elif variant == "response_import_disabled":
                        tampered["response_import_required"] = False
                    elif variant == "provider_identity":
                        provider_identity = dict(
                            tampered["provider_identity"]
                        )
                        provider_identity["provider_route"] = "TAMPERED"
                        provider_identity_hash = canonical_hash(
                            provider_identity
                        )
                        identity = {
                            **tampered["request_identity"],
                            "provider_identity_hash": (
                                provider_identity_hash
                            ),
                        }
                        tampered.update(
                            {
                                "provider_identity": provider_identity,
                                "provider_identity_hash": (
                                    provider_identity_hash
                                ),
                                "request_identity": identity,
                                "request_id": (
                                    "COLLABREQ-"
                                    + canonical_hash(identity)
                                ),
                            }
                        )
                    else:
                        tampered["extra_metadata"] = "not bound"
                    request_path.unlink()
                    request_id = tampered["request_id"]
                    (
                        journal
                        / "requests"
                        / f"{request_id}.json"
                    ).write_text(
                        json.dumps(tampered, ensure_ascii=False),
                        encoding="utf-8",
                    )

                    with self.assertRaises(ValueError):
                        import_collaboration_response(
                            journal_root=journal,
                            request_id=request_id,
                            response_payload=QUERY_RESPONSE,
                            agent_id="tamper-agent",
                            canonical_task_name="/root/tamper_agent",
                            agent_model="codex-collaboration",
                        )
                    audit = provider.response_cache_audit()[
                        "collaboration_journal"
                    ]
                    self.assertEqual(audit["request_count"], 1)
                    self.assertEqual(
                        audit["validated_request_count"],
                        0,
                    )
                    self.assertEqual(audit["invalid_request_count"], 1)

    def test_concurrent_import_is_atomic_first_writer_wins(
        self,
    ) -> None:
        with tempfile.TemporaryDirectory() as directory:
            provider = _provider(UsageLimitTransport())
            journal = _configure(provider, Path(directory))
            with self.assertRaises(StructuredProviderUnavailable):
                provider.complete(
                    pass_name="SOURCE_QUERY_GENERATION",
                    payload={
                        "target_id": "CURRENT-TARGET",
                        "as_of_date": "2026-07-12",
                    },
                )
            _, request = _request(journal)
            payloads = (
                {
                    **QUERY_RESPONSE,
                    "unresolved_research_notes": ["candidate A"],
                },
                {
                    **QUERY_RESPONSE,
                    "unresolved_research_notes": ["candidate B"],
                },
            )
            context = multiprocessing.get_context("spawn")
            barrier = context.Barrier(2)
            result_queue = context.Queue()
            processes = [
                context.Process(
                    target=_concurrent_import_worker,
                    kwargs={
                        "journal_root": str(journal),
                        "request_id": request["request_id"],
                        "response_payload": payload,
                        "agent_id": f"race-agent-{index}",
                        "barrier": barrier,
                        "result_queue": result_queue,
                    },
                )
                for index, payload in enumerate(payloads)
            ]
            for process in processes:
                process.start()
            for process in processes:
                process.join(timeout=20)
                if process.is_alive():
                    process.terminate()
                    process.join(timeout=5)
                    self.fail("concurrent importer process did not finish")
                self.assertEqual(process.exitcode, 0)
            results = [result_queue.get(timeout=5) for _ in processes]

            successes = [
                row for row in results if row["status"] == "SUCCESS"
            ]
            failures = [
                row for row in results if row["status"] == "ERROR"
            ]
            self.assertEqual(len(successes), 1)
            self.assertEqual(len(failures), 1)
            self.assertEqual(failures[0]["error_type"], "ValueError")
            self.assertIn(
                "a different collaboration response is already imported",
                failures[0]["error"],
            )
            final_envelope = json.loads(
                (
                    journal
                    / "responses"
                    / f"{request['request_id']}.json"
                ).read_text(encoding="utf-8")
            )
            self.assertEqual(final_envelope, successes[0]["envelope"])
            self.assertIn(final_envelope["payload"], payloads)
            self.assertEqual(
                tuple(
                    (
                        journal / "responses"
                    ).glob(f"{request['request_id']}.json")
                ),
                (
                    journal
                    / "responses"
                    / f"{request['request_id']}.json",
                ),
            )

    def test_downstream_semantic_rejection_quarantines_imported_response(
        self,
    ) -> None:
        with tempfile.TemporaryDirectory() as directory:
            provider = _provider(UsageLimitTransport())
            journal = _configure(provider, Path(directory))
            ranker = ResearcherDocumentRanker(provider=provider)
            kwargs = {
                "target_id": "CURRENT-TARGET",
                "target_name": "Current Corp",
                "as_of_date": "2026-07-12",
                "open_objectives": [
                    {
                        "objective_id": "OBJ-1",
                        "question": "현재 고객 공식 확인이 있는가?",
                    }
                ],
                "candidates": [
                    {
                        "candidate_id": "CAND-1",
                        "title": "customer update",
                        "url": "https://example.com/update",
                        "snippet": "customer update",
                        "source": "test",
                        "objective_ids": ["OBJ-1"],
                        "requested_source_families": [
                            "CUSTOMER_OFFICIAL"
                        ],
                    }
                ],
                "current_evidence_facts": [],
                "target_business_model": None,
                "source_coverage": [],
            }

            first = ranker.rank_candidates(**kwargs)
            self.assertEqual(first.status, "PENDING")
            _, request = _request(journal)
            # Schema-valid, but the ordinary semantic ranker must reject the
            # unknown candidate id rather than allowing the bridge to repair it.
            import_collaboration_response(
                journal_root=journal,
                request_id=request["request_id"],
                response_payload={
                    "decisions": [
                        {
                            "candidate_id": "UNKNOWN-CANDIDATE",
                            "material_relevance": False,
                            "priority": 0.0,
                            "objective_ids": [],
                            "matched_requested_source_family": "NONE",
                            "rationale": "입력 후보와 관련이 없다.",
                        }
                    ],
                    "ranking_complete": True,
                    "unresolved_notes": [],
                },
                agent_id="agent-123",
                canonical_task_name="/root/rank_partition_0",
                agent_model="codex-collaboration",
            )

            retried = ranker.rank_candidates(**kwargs)

            self.assertEqual(retried.status, "PENDING")
            self.assertFalse(
                (
                    journal
                    / "responses"
                    / f"{request['request_id']}.json"
                ).exists()
            )
            quarantined = tuple(
                path
                for path in (journal / "quarantine").rglob("*.json")
                if not path.name.endswith(".reason.json")
            )
            self.assertEqual(len(quarantined), 1)
            self.assertEqual(
                provider.response_cache_audit()[
                    "downstream_semantic_invalidation_count"
                ],
                1,
            )
            journal_audit = provider.collaboration.transport.journal_audit()
            self.assertEqual(
                journal_audit["validated_quarantined_response_count"],
                1,
            )
            self.assertEqual(
                journal_audit["invalid_quarantined_response_count"],
                0,
            )
            # One clean retry is still unanswered; the quarantined original is
            # accounted history, not the current pending request.
            self.assertEqual(
                journal_audit["unresolved_pending_response_count"],
                1,
            )
            relative_transport = CollaborationCodexSubagentTransport()
            relative_transport.configure_journal_root(
                Path(os.path.relpath(journal, Path.cwd()))
            )
            relative_audit = relative_transport.journal_audit()
            self.assertEqual(
                relative_audit["validated_quarantined_response_count"],
                1,
            )
            self.assertEqual(
                relative_audit["invalid_quarantined_response_count"],
                0,
            )
            # The clean semantic retry has a different prompt hash and request.
            self.assertEqual(
                len(tuple((journal / "requests").glob("*.json"))),
                2,
            )

            reason_path = next(
                (journal / "quarantine").rglob("*.reason.json")
            )
            reason = json.loads(reason_path.read_text(encoding="utf-8"))
            reason["production_score_authority"] = True
            reason_path.write_text(
                json.dumps(reason, ensure_ascii=False, sort_keys=True) + "\n",
                encoding="utf-8",
            )
            tampered_audit = (
                provider.collaboration.transport.journal_audit()
            )
            self.assertEqual(
                tampered_audit["invalid_quarantined_response_count"],
                1,
            )

    def test_malformed_response_id_cannot_escape_quarantine_root(
        self,
    ) -> None:
        for variant in ("absolute", "traversal"):
            with self.subTest(variant=variant):
                with tempfile.TemporaryDirectory() as directory:
                    root = Path(directory)
                    provider = _provider(UsageLimitTransport())
                    journal = _configure(provider, root)
                    with self.assertRaises(
                        StructuredProviderUnavailable
                    ):
                        provider.complete(
                            pass_name="SOURCE_QUERY_GENERATION",
                            payload={
                                "target_id": f"TARGET-{variant}",
                                "as_of_date": "2026-07-12",
                            },
                        )
                    _, request = _request(journal)
                    quarantine_root = (
                        journal
                        / "quarantine"
                        / request["request_id"]
                    )
                    escaped_path = root / f"escaped-{variant}.json"
                    escaped_stem = escaped_path.with_suffix("")
                    malicious_response_id = (
                        str(escaped_stem)
                        if variant == "absolute"
                        else os.path.relpath(
                            escaped_stem,
                            quarantine_root,
                        )
                    )
                    malformed = {
                        "schema_version": "malformed",
                        "response_id": malicious_response_id,
                    }
                    response_bytes = json.dumps(
                        malformed,
                        ensure_ascii=False,
                        sort_keys=True,
                    ).encode("utf-8")
                    (
                        journal
                        / "responses"
                        / f"{request['request_id']}.json"
                    ).write_bytes(response_bytes)

                    with self.assertRaisesRegex(
                        StructuredProviderRejected,
                        "COLLABORATION_RESPONSE_REJECTED",
                    ):
                        provider.complete(
                            pass_name="SOURCE_QUERY_GENERATION",
                            payload={
                                "target_id": f"TARGET-{variant}",
                                "as_of_date": "2026-07-12",
                            },
                        )

                    safe_response_id = (
                        "COLLABRESP-"
                        + hashlib.sha256(response_bytes).hexdigest()
                    )
                    quarantine_path = (
                        quarantine_root / f"{safe_response_id}.json"
                    )
                    self.assertFalse(escaped_path.exists())
                    self.assertTrue(quarantine_path.is_file())
                    self.assertEqual(
                        quarantine_path.read_bytes(),
                        response_bytes,
                    )
                    reason_paths = tuple(
                        quarantine_root.glob(
                            f"{safe_response_id}.json.*.reason.json"
                        )
                    )
                    self.assertEqual(len(reason_paths), 1)
                    self.assertTrue(
                        all(
                            path.resolve().is_relative_to(
                                quarantine_root.resolve()
                            )
                            for path in (
                                quarantine_path,
                                *reason_paths,
                            )
                        )
                    )

        transport = CollaborationCodexSubagentTransport()
        with tempfile.TemporaryDirectory() as directory:
            transport.configure_journal_root(directory)
            with self.assertRaisesRegex(
                ValueError,
                "quarantine request id is invalid",
            ):
                transport._quarantine_response(
                    request_id="../../escaped",
                    reason="malformed request id",
                )

    def test_unvalidated_response_id_cannot_collide_with_existing_quarantine(
        self,
    ) -> None:
        with tempfile.TemporaryDirectory() as directory:
            provider = _provider(UsageLimitTransport())
            journal = _configure(provider, Path(directory))
            payload = {
                "target_id": "CURRENT-TARGET",
                "as_of_date": "2026-07-12",
            }
            with self.assertRaises(StructuredProviderUnavailable):
                provider.complete(
                    pass_name="SOURCE_QUERY_GENERATION",
                    payload=payload,
                )
            _, request = _request(journal)
            attacker_selected_id = "COLLABRESP-" + "a" * 64
            quarantine_root = (
                journal / "quarantine" / request["request_id"]
            )
            quarantine_root.mkdir(parents=True, exist_ok=True)
            existing_quarantine_path = (
                quarantine_root / f"{attacker_selected_id}.json"
            )
            existing_bytes = b'{"existing":true}'
            existing_quarantine_path.write_bytes(existing_bytes)
            malformed = {
                "schema_version": "malformed",
                "response_id": attacker_selected_id,
            }
            response_bytes = json.dumps(
                malformed,
                ensure_ascii=False,
                sort_keys=True,
            ).encode("utf-8")
            active_response_path = (
                journal
                / "responses"
                / f"{request['request_id']}.json"
            )
            active_response_path.write_bytes(response_bytes)

            with self.assertRaisesRegex(
                StructuredProviderRejected,
                "COLLABORATION_RESPONSE_REJECTED",
            ):
                provider.complete(
                    pass_name="SOURCE_QUERY_GENERATION",
                    payload=payload,
                )

            safe_response_id = (
                "COLLABRESP-" + hashlib.sha256(response_bytes).hexdigest()
            )
            self.assertFalse(active_response_path.exists())
            self.assertEqual(
                existing_quarantine_path.read_bytes(),
                existing_bytes,
            )
            self.assertEqual(
                (
                    quarantine_root / f"{safe_response_id}.json"
                ).read_bytes(),
                response_bytes,
            )

    def test_semantically_quarantined_response_cannot_be_reimported(
        self,
    ) -> None:
        with tempfile.TemporaryDirectory() as directory:
            provider = _provider(UsageLimitTransport())
            journal = _configure(provider, Path(directory))
            payload = {
                "target_id": "CURRENT-TARGET",
                "as_of_date": "2026-07-12",
            }
            with self.assertRaises(StructuredProviderUnavailable):
                provider.complete(
                    pass_name="SOURCE_QUERY_GENERATION",
                    payload=payload,
                )
            _, request = _request(journal)
            import_kwargs = {
                "journal_root": journal,
                "request_id": request["request_id"],
                "response_payload": QUERY_RESPONSE,
                "agent_id": "semantic-agent",
                "canonical_task_name": "/root/semantic_agent",
                "agent_model": "codex-collaboration",
            }
            imported = import_collaboration_response(**import_kwargs)
            self.assertEqual(
                provider.complete(
                    pass_name="SOURCE_QUERY_GENERATION",
                    payload=payload,
                ),
                QUERY_RESPONSE,
            )

            event = provider.invalidate_last_response_cache(
                "semantic poison"
            )

            self.assertEqual(
                event["collaboration_journal_invalidation"]["status"],
                "COLLABORATION_RESPONSE_QUARANTINED",
            )
            self.assertTrue(
                (
                    journal
                    / "quarantine"
                    / request["request_id"]
                    / f"{imported['response_id']}.json"
                ).is_file()
            )
            with self.assertRaisesRegex(
                ValueError,
                "same collaboration response was previously quarantined",
            ):
                import_collaboration_response(**import_kwargs)

            corrected_payload = {
                **QUERY_RESPONSE,
                "unresolved_research_notes": ["corrected response"],
            }
            corrected = import_collaboration_response(
                **{
                    **import_kwargs,
                    "response_payload": corrected_payload,
                }
            )
            self.assertNotEqual(
                corrected["response_id"],
                imported["response_id"],
            )
            self.assertEqual(corrected["payload"], corrected_payload)

    def test_import_commit_and_semantic_quarantine_are_serialized(
        self,
    ) -> None:
        with tempfile.TemporaryDirectory() as directory:
            provider = _provider(UsageLimitTransport())
            journal = _configure(provider, Path(directory))
            payload = {
                "target_id": "CURRENT-TARGET",
                "as_of_date": "2026-07-12",
            }
            with self.assertRaises(StructuredProviderUnavailable):
                provider.complete(
                    pass_name="SOURCE_QUERY_GENERATION",
                    payload=payload,
                )
            _, request = _request(journal)
            agent_id = "race-semantic-agent"
            provenance = {
                "agent_id": agent_id,
                "canonical_task_name": f"/root/{agent_id}",
                "agent_model": "codex-collaboration",
                "agent_surface": "CODEX_COLLABORATION_SUBAGENT",
                "provenance_assurance": (
                    "ORCHESTRATOR_ATTESTED_NOT_CRYPTOGRAPHIC"
                ),
            }

            def canonical_hash(value):
                return hashlib.sha256(
                    json.dumps(
                        value,
                        ensure_ascii=False,
                        sort_keys=True,
                        separators=(",", ":"),
                    ).encode("utf-8")
                ).hexdigest()

            response_id = "COLLABRESP-" + canonical_hash(
                {
                    "request_id": request["request_id"],
                    "payload_hash": canonical_hash(QUERY_RESPONSE),
                    "provenance": provenance,
                }
            )
            context = multiprocessing.get_context("spawn")
            reached_commit = context.Event()
            resume_commit = context.Event()
            quarantine_started = context.Event()
            result_queue = context.Queue()
            importer = context.Process(
                target=_paused_import_worker,
                kwargs={
                    "journal_root": str(journal),
                    "request_id": request["request_id"],
                    "response_payload": QUERY_RESPONSE,
                    "agent_id": agent_id,
                    "reached_commit": reached_commit,
                    "resume_commit": resume_commit,
                    "result_queue": result_queue,
                },
            )
            importer.start()
            self.assertTrue(reached_commit.wait(timeout=10))
            quarantiner = context.Process(
                target=_semantic_quarantine_worker,
                kwargs={
                    "journal_root": str(journal),
                    "request_id": request["request_id"],
                    "response_id": response_id,
                    "started": quarantine_started,
                    "result_queue": result_queue,
                },
            )
            quarantiner.start()
            self.assertTrue(quarantine_started.wait(timeout=10))
            resume_commit.set()
            for process in (importer, quarantiner):
                process.join(timeout=20)
                if process.is_alive():
                    process.terminate()
                    process.join(timeout=5)
                    self.fail("journal transition process did not finish")
                self.assertEqual(process.exitcode, 0)
            results = [result_queue.get(timeout=5) for _ in range(2)]
            self.assertEqual(
                {row["worker"] for row in results},
                {"IMPORT", "QUARANTINE"},
            )
            self.assertTrue(
                all(row["status"] == "SUCCESS" for row in results)
            )

            active_path = (
                journal
                / "responses"
                / f"{request['request_id']}.json"
            )
            tombstone_path = (
                journal
                / "quarantine"
                / request["request_id"]
                / f"{response_id}.json"
            )
            self.assertFalse(active_path.exists())
            self.assertTrue(tombstone_path.is_file())
            with self.assertRaisesRegex(
                ValueError,
                "same collaboration response was previously quarantined",
            ):
                import_collaboration_response(
                    journal_root=journal,
                    request_id=request["request_id"],
                    response_payload=QUERY_RESPONSE,
                    agent_id=agent_id,
                    canonical_task_name=f"/root/{agent_id}",
                    agent_model="codex-collaboration",
                )
            self.assertFalse(active_path.exists())
            self.assertTrue(tombstone_path.is_file())

    def test_journal_audit_counts_only_revalidated_responses(
        self,
    ) -> None:
        with tempfile.TemporaryDirectory() as directory:
            provider = _provider(UsageLimitTransport())
            journal = _configure(provider, Path(directory))
            payload = {
                "target_id": "CURRENT-TARGET",
                "as_of_date": "2026-07-12",
            }
            with self.assertRaises(StructuredProviderUnavailable):
                provider.complete(
                    pass_name="SOURCE_QUERY_GENERATION",
                    payload=payload,
                )
            _, request = _request(journal)
            imported = import_collaboration_response(
                journal_root=journal,
                request_id=request["request_id"],
                response_payload=QUERY_RESPONSE,
                agent_id="audit-agent",
                canonical_task_name="/root/audit_agent",
                agent_model="codex-collaboration",
            )
            tampered = {
                **imported,
                "payload_hash": "0" * 64,
            }
            response_path = (
                journal
                / "responses"
                / f"{request['request_id']}.json"
            )
            response_path.write_text(
                json.dumps(tampered, ensure_ascii=False),
                encoding="utf-8",
            )
            orphan_id = "COLLABREQ-" + "f" * 64
            (journal / "responses" / f"{orphan_id}.json").write_text(
                "{malformed",
                encoding="utf-8",
            )

            audit = provider.response_cache_audit()[
                "collaboration_journal"
            ]

            self.assertEqual(audit["request_count"], 1)
            self.assertEqual(audit["validated_request_count"], 1)
            self.assertEqual(audit["invalid_request_count"], 0)
            self.assertEqual(audit["response_file_count"], 2)
            self.assertEqual(audit["validated_response_count"], 0)
            self.assertEqual(audit["invalid_response_count"], 1)
            self.assertEqual(audit["orphan_response_count"], 1)
            self.assertEqual(audit["pending_response_count"], 1)

    def test_response_envelope_extra_key_is_not_audited_as_valid(
        self,
    ) -> None:
        with tempfile.TemporaryDirectory() as directory:
            provider = _provider(UsageLimitTransport())
            journal = _configure(provider, Path(directory))
            with self.assertRaises(StructuredProviderUnavailable):
                provider.complete(
                    pass_name="SOURCE_QUERY_GENERATION",
                    payload={
                        "target_id": "CURRENT-TARGET",
                        "as_of_date": "2026-07-12",
                    },
                )
            _, request = _request(journal)
            imported = import_collaboration_response(
                journal_root=journal,
                request_id=request["request_id"],
                response_payload=QUERY_RESPONSE,
                agent_id="audit-agent",
                canonical_task_name="/root/audit_agent",
                agent_model="codex-collaboration",
            )
            tampered = {
                **imported,
                "extra_metadata": "not bound",
            }
            (
                journal
                / "responses"
                / f"{request['request_id']}.json"
            ).write_text(
                json.dumps(tampered, ensure_ascii=False),
                encoding="utf-8",
            )

            audit = provider.response_cache_audit()[
                "collaboration_journal"
            ]

            self.assertEqual(audit["validated_response_count"], 0)
            self.assertEqual(audit["invalid_response_count"], 1)
            self.assertEqual(audit["pending_response_count"], 1)

    def test_phase94_explicit_codex_subagent_option_has_separate_provenance(
        self,
    ) -> None:
        args = build_phase94_parser().parse_args(
            [
                "--as-of-date",
                "2026-07-12",
                "--symbols",
                "005930",
                "--archetype",
                "C06_HBM_MEMORY_CUSTOMER_CAPACITY",
                "--live-materialization-authorized",
                "true",
                "--checkpoint-resume",
                "true",
                "--gold-lane-isolated",
                "true",
                "--require-researcher-parity",
                "true",
                "--output-root",
                "output/test",
                "--research-provider",
                "codex-subagent",
            ]
        )

        provider = _build_research_provider(args)
        self.assertIsInstance(
            provider,
            CodexSubagentFallbackResearchProvider,
        )
        manifest = _research_provider_manifest(provider)
        self.assertTrue(manifest["provider_selected_explicitly"])
        self.assertFalse(manifest["score_or_stage_authority"])
        self.assertEqual(
            manifest["provider_identity"]["fallback_condition"],
            "CODEX_CLI_USAGE_LIMIT_CACHE_MISS_ONLY",
        )
        self.assertEqual(
            manifest["provider_identity"]["provenance_assurance"],
            "ORCHESTRATOR_ATTESTED_NOT_CRYPTOGRAPHIC",
        )

    def test_phase94_explicit_codex_collaboration_option_skips_cli_primary(
        self,
    ) -> None:
        args = build_phase94_parser().parse_args(
            [
                "--as-of-date",
                "2026-07-12",
                "--symbols",
                "005930",
                "--archetype",
                "C06_HBM_MEMORY_CUSTOMER_CAPACITY",
                "--live-materialization-authorized",
                "true",
                "--checkpoint-resume",
                "true",
                "--gold-lane-isolated",
                "true",
                "--require-researcher-parity",
                "true",
                "--output-root",
                "output/test",
                "--research-provider",
                "codex-collaboration",
            ]
        )

        provider = _build_research_provider(args)
        self.assertIsInstance(
            provider,
            CollaborationCodexResearcherProvider,
        )
        self.assertNotIsInstance(
            provider,
            CodexSubagentFallbackResearchProvider,
        )
        manifest = _research_provider_manifest(provider)
        self.assertTrue(manifest["provider_selected_explicitly"])
        self.assertFalse(manifest["score_or_stage_authority"])
        self.assertEqual(
            manifest["provider_identity"]["provider_route"],
            "COLLABORATION_CODEX_SUBAGENT",
        )
        self.assertEqual(
            manifest["provider_identity"]["provenance_assurance"],
            "ORCHESTRATOR_ATTESTED_NOT_CRYPTOGRAPHIC",
        )

    def test_dedicated_importer_cli_writes_only_validated_response_namespace(
        self,
    ) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            provider = _provider(UsageLimitTransport())
            journal = _configure(provider, root)
            with self.assertRaises(StructuredProviderUnavailable):
                provider.complete(
                    pass_name="SOURCE_QUERY_GENERATION",
                    payload={
                        "target_id": "CURRENT-TARGET",
                        "as_of_date": "2026-07-12",
                    },
                )
            _, request = _request(journal)
            draft_path = root / "subagent-draft.json"
            draft_path.write_text(
                json.dumps(QUERY_RESPONSE, ensure_ascii=False),
                encoding="utf-8",
            )
            stdout = io.StringIO()

            with redirect_stdout(stdout):
                exit_code = import_response_main(
                    [
                        "--journal-root",
                        str(journal),
                        "--request-id",
                        request["request_id"],
                        "--response-path",
                        str(draft_path),
                        "--agent-id",
                        "agent-123",
                        "--canonical-task-name",
                        "/root/rank_partition_0",
                        "--agent-model",
                        "codex-collaboration",
                    ]
                )

            self.assertEqual(exit_code, 0)
            receipt = json.loads(stdout.getvalue())
            self.assertEqual(
                receipt["status"],
                "COLLABORATION_RESPONSE_IMPORTED",
            )
            self.assertFalse(receipt["score_or_stage_authority"])
            self.assertTrue(
                (
                    journal
                    / "responses"
                    / f"{request['request_id']}.json"
                ).is_file()
            )
            self.assertEqual(
                tuple(
                    (
                        root / "research_provider_response_cache"
                    ).glob("source_query_generation-*.json")
                ),
                (),
            )


if __name__ == "__main__":
    unittest.main()
