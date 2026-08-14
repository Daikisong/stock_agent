from __future__ import annotations

import hashlib
import json
import tempfile
import unittest
from pathlib import Path

from e2r.research_brain.planning.provider_transport import (
    StructuredProviderUnavailable,
)
from e2r.research_brain.researcher_mode.collaboration_provider_bridge import (
    COLLABORATION_RESPONSE_SCHEMA_VERSION,
    CollaborationCodexSubagentTransport,
    _authority_recovery_fact_request_material,
    _canonical_hash,
    _validate_agent_provenance,
    import_collaboration_response,
)
from e2r.research_brain.researcher_mode.component_researcher import (
    _single_payload_request_material,
)
from e2r.research_brain.researcher_mode.evidence_fact_compiler import (
    EvidenceFactCompiler,
)
from e2r.research_brain.researcher_mode.evidence_fact_extractor import (
    FACT_EXTRACTION_SEMANTICS_VERSION,
    _fact_extraction_primary_payload,
    _validate_response,
)
from e2r.research_brain.researcher_mode.fact_lineage_materials import (
    load_authoritative_research_epoch_fact_ledger,
    validate_current_v5_fact_lineage_materials,
)
from e2r.research_brain.researcher_mode.research_epoch import (
    _research_checkpoint_hash,
    _research_checkpoint_id,
)
from e2r.research_brain.researcher_mode.research_supervisor import (
    ResearchSupervisorReview,
)
from e2r.research_brain.researcher_mode.schemas import (
    CANONICAL_COMPONENT_ORDER,
)
from e2r.research_brain.scoring.business_mechanism_scope import (
    load_mechanism_scope_contracts,
)


TARGET = "CURRENT-TARGET"
AS_OF_DATE = "2026-07-12"
ARCHETYPE = "C06_HBM_MEMORY_CUSTOMER_CAPACITY"
OBJECTIVE_COMPONENT = "eps_fcf_explosion"
BATCH_SIZES = (12, 2, 12, 12, 4, 12)
CURRENT_BATCH_SIZES = (12, 1, 12, 12, 3, 12)
CLAIMS_PER_BATCH = (9, 8, 10, 3, 10, 2)
CLAIMED_DOCS_PER_BATCH = (3, 1, 3, 2, 2, 2)


def _json_safe(value):
    return json.loads(json.dumps(value, ensure_ascii=False, sort_keys=True))


def _mechanism_contract():
    contract = load_mechanism_scope_contracts()[ARCHETYPE]
    return {
        "allowed_business_segments": list(contract.allowed_business_segments),
        "allowed_product_families": list(contract.allowed_product_families),
        "allowed_technology_families": list(
            contract.allowed_technology_families
        ),
        "allowed_transaction_types": list(contract.allowed_transaction_types),
        "allowed_economic_mechanisms": list(
            contract.allowed_economic_mechanisms
        ),
        "generic_company_allowed_components": list(
            contract.generic_company_allowed_components
        ),
        "forbidden_business_segments": list(
            contract.forbidden_business_segments
        ),
        "forbidden_product_families": list(
            contract.forbidden_product_families
        ),
        "issuer_wide_fact_encoding": {
            "scope_business_segment": "CORPORATE_GENERIC",
            "scope_product_family": "CORPORATE_GENERIC",
            "scope_technology_family": "CORPORATE_GENERIC",
            "scope_transaction_type": "GENERIC_INFORMATION",
            "scope_economic_mechanism": "INFORMATION_ONLY",
            "allowed_only_for_components": list(
                contract.generic_company_allowed_components
            ),
            "instruction": "fixture issuer-wide encoding contract",
        },
    }


def _prompt_document(document_id: str, objective_id: str):
    content = " ".join(
        f"{document_id} material statement {index}."
        for index in range(12)
    )
    return {
        "document_id": document_id,
        "canonical_url": f"https://issuer.example/{document_id}",
        "title": f"Current filing {document_id}",
        "source_family": "ISSUER_PRESENTATION",
        "published_at": "2026-07-10",
        "available_at": "2026-07-10",
        "source_independence_group": f"ISSUER-{document_id}",
        "objective_ids": [objective_id],
        "content_text": content,
        "full_fetch_performed": True,
        "snippet_used_as_document": False,
    }


def _current_document(prompt_document, *, drift: bool = False):
    row = dict(prompt_document)
    if drift:
        historical = list(row["objective_ids"])
        row["objective_ids"] = ["OBJECTIVE-CURRENT-DRIFT"]
        row["historical_objective_ids"] = historical
    row.update(
        {
            "target_id": TARGET,
            "as_of_date": AS_OF_DATE,
            "content_hash": hashlib.sha256(
                str(row["content_text"]).encode("utf-8")
            ).hexdigest(),
            "evidence_eligible": True,
            "snippet_only": False,
        }
    )
    return row


def _scope_contract(documents):
    objective_ids = sorted(
        {
            objective_id
            for document in documents
            for objective_id in document["objective_ids"]
        }
    )
    return {
        "mode": "PRODUCTION_OBJECTIVE_LOCAL",
        "allowed_objective_relations": [
            "ADVANCE",
            "COUNTER",
            "SUPERSEDE",
        ],
        "objective_component_rows": [
            {
                "objective_id": objective_id,
                "component_id": OBJECTIVE_COMPONENT,
            }
            for objective_id in objective_ids
        ],
        "document_objective_ids": [
            {
                "document_id": document["document_id"],
                "objective_ids": list(document["objective_ids"]),
            }
            for document in documents
        ],
        "material_fact_definition": "fixture objective-linked material fact",
        "completion_definition": "fixture distinct facts exhausted",
        "deterministic_validation_scope": (
            "objective roster, document lineage, exact quote, cutoff and scope"
        ),
        "llm_owns_economic_relevance": True,
    }


def _prompt_payload(
    documents,
    *,
    marker: str,
    semantics_version: str = FACT_EXTRACTION_SEMANTICS_VERSION,
):
    discovery_objective_scope = {
        str(document["document_id"]): frozenset(
            str(value) for value in document["objective_ids"]
        )
        for document in documents
    }
    current_open_objective_ids = frozenset(
        objective_id
        for values in discovery_objective_scope.values()
        for objective_id in values
    )
    objective_scope = {
        str(document["document_id"]): current_open_objective_ids
        for document in documents
    }
    objective_components = {
        objective_id: OBJECTIVE_COMPONENT
        for objective_id in current_open_objective_ids
    }
    return _fact_extraction_primary_payload(
        target_id=TARGET,
        target_name="Current Corp",
        target_aliases=("Current",),
        archetype_id=ARCHETYPE,
        as_of_date=AS_OF_DATE,
        extraction_semantics_version=semantics_version,
        open_objectives=(),
        current_evidence_facts={"fact_count": 499},
        score_gap_context={
            "fixture_marker": marker,
            "score_authority": False,
        },
        scope_contract=load_mechanism_scope_contracts()[ARCHETYPE],
        batch=documents,
        objective_scope_by_document=objective_scope,
        objective_component_by_id=objective_components,
        discovery_objective_scope_by_document=(
            discovery_objective_scope
        ),
    )


def _proposal(document, *, claim_index: int, quote_index: int):
    return {
        "document_id": document["document_id"],
        "question_family_id": f"question_{claim_index}",
        "subject_id": f"subject_{claim_index}",
        "subject": f"Current Corp mechanism {claim_index}",
        "business_segment": "MEMORY",
        "product_family": "HBM",
        "scope_business_segment": "MEMORY",
        "scope_product_family": "HBM",
        "scope_technology_family": "HBM",
        "scope_transaction_type": "REVENUE_ACTUAL",
        "scope_economic_mechanism": "REVENUE_CONVERSION",
        "scope_confidence": 0.95,
        "economic_mechanism": f"revenue conversion mechanism {claim_index}",
        "mechanism_scope_id": f"TARGET-DIRECT-{claim_index}",
        "predicate": f"reported material outcome {claim_index}",
        "predicate_family": f"predicate_{claim_index}",
        "value": claim_index + 1,
        "normalized_object": f"normalized_{claim_index}",
        "unit": "KRW billion",
        "period": "2026Q2",
        "direction": "POSITIVE",
        "current_lifecycle": "CURRENT",
        "exact_quote": (
            f"{document['document_id']} material statement {quote_index}."
        ),
        "material": True,
        "materiality": "CRITICAL",
        "materiality_rationale": "fixture material economic evidence",
        "confidence": 0.9,
        "question_family_tags": [f"question_{claim_index}"],
        "primitive_tags": [],
        "structured_evidence_roles": [],
        "objective_ids": list(document["objective_ids"]),
        "objective_relation": "ADVANCE",
    }


def _response(documents, proposals, *, complete=True):
    fact_document_ids = {
        str(row["document_id"])
        for row in proposals
        if row.get("material") is True
    }
    return {
        "facts": [dict(row) for row in proposals],
        "document_dispositions": [
            {
                "document_id": document["document_id"],
                "status": (
                    "FACTS_EXTRACTED"
                    if document["document_id"] in fact_document_ids
                    else "NO_MATERIAL_FACT"
                ),
                "rationale": "the complete canonical document was inspected",
            }
            for document in documents
        ],
        "unresolved_document_ids": (
            [] if complete else [documents[0]["document_id"]]
        ),
        "unresolved_research_notes": [],
        "extraction_complete": complete,
    }


def _write_pair(
    transport,
    journal_root,
    *,
    payload,
    response,
    agent_model,
):
    semantics_version = str(
        payload.get("fact_extraction_semantics_version") or ""
    )
    _, schema, prompt, _, _ = _authority_recovery_fact_request_material(
        payload=payload,
        fact_extraction_semantics_version=semantics_version,
    )
    with unittest.TestCase().assertRaises(StructuredProviderUnavailable):
        transport.complete(
            prompt=prompt,
            output_schema=schema,
            schema_name="e2r_v5_evidence_fact_extraction",
        )
    request_id = transport._last_request_id
    assert request_id is not None
    import_collaboration_response(
        journal_root=journal_root,
        request_id=request_id,
        response_payload=response,
        agent_id="fact-lineage-agent",
        canonical_task_name="/root/fact_lineage_fixture",
        agent_model=agent_model,
    )
    return request_id


def _build_actual_shaped_journal(root: Path):
    journal = root / "collaboration_codex_subagent_provider"
    transport = CollaborationCodexSubagentTransport()
    transport.configure_journal_root(journal)
    current_documents = []
    payloads = []
    responses = []
    current_cursor = 0
    stale_cursor = 0
    claim_cursor = 0
    for batch_index, (
        batch_size,
        current_batch_size,
        claim_count,
        claimed_document_count,
    ) in enumerate(
        zip(
            BATCH_SIZES,
            CURRENT_BATCH_SIZES,
            CLAIMS_PER_BATCH,
            CLAIMED_DOCS_PER_BATCH,
        )
    ):
        current_prompt_documents = []
        for _ in range(current_batch_size):
            document_id = f"SGDOC-CURRENT-{current_cursor:03d}"
            objective_id = (
                "OBJECTIVE-HISTORICAL-DRIFT"
                if current_cursor == 0
                else f"OBJECTIVE-{current_cursor:03d}"
            )
            prompt_document = _prompt_document(document_id, objective_id)
            current_prompt_documents.append(prompt_document)
            current_documents.append(
                _current_document(
                    prompt_document,
                    drift=current_cursor == 0,
                )
            )
            current_cursor += 1
        stale_documents = []
        for _ in range(batch_size - current_batch_size):
            document_id = f"SGDOC-STALE-{stale_cursor:03d}"
            stale_documents.append(
                _prompt_document(
                    document_id,
                    f"OBJECTIVE-STALE-{stale_cursor:03d}",
                )
            )
            stale_cursor += 1
        documents = [*current_prompt_documents, *stale_documents]
        proposals = []
        quote_count_by_document = {}
        for local_index in range(claim_count):
            document = current_prompt_documents[
                local_index % claimed_document_count
            ]
            quote_index = quote_count_by_document.get(
                document["document_id"],
                0,
            )
            quote_count_by_document[document["document_id"]] = quote_index + 1
            proposals.append(
                _proposal(
                    document,
                    claim_index=claim_cursor,
                    quote_index=quote_index,
                )
            )
            claim_cursor += 1
        payload = _prompt_payload(documents, marker=f"batch-{batch_index}")
        response = _response(documents, proposals)
        _write_pair(
            transport,
            journal,
            payload=payload,
            response=response,
            agent_model=(
                "codex-gpt-5"
                if batch_index < 4
                else "codex-collaboration"
            ),
        )
        payloads.append(payload)
        responses.append(response)
    return {
        "journal": journal,
        "current_documents": current_documents,
        "current_prompt_payload": payloads[0],
        "payloads": payloads,
        "responses": responses,
    }


def _official_replay(material_result):
    scope_contract = load_mechanism_scope_contracts()[ARCHETYPE]
    current_ids = set(material_result["current_document_ids"])
    claims = []
    dispositions = []
    for material in material_result["materials"]:
        request = material["request_payload"]
        if request.get("fact_extraction_continuation_context"):
            raise AssertionError("actual-shaped fixture is base-only")
        documents = request["full_documents"]
        objective_scope = {
            row["document_id"]: frozenset(row["objective_ids"])
            for row in request["fact_extraction_scope_contract"][
                "document_objective_ids"
            ]
        }
        objective_components = {
            row["objective_id"]: row["component_id"]
            for row in request["fact_extraction_scope_contract"][
                "objective_component_rows"
            ]
        }
        (
            page_claims,
            rejections,
            page_dispositions,
            pending,
            _feedback,
            _completion_reconciled,
        ) = _validate_response(
            material["response_payload"],
            batch_id=f"BATCH-{material['request_id']}",
            documents=documents,
            target_id=TARGET,
            as_of_date=AS_OF_DATE,
            scope_contract=scope_contract,
            provider_name="COLLABORATION_CODEX_SUBAGENT",
            prompt_hash=material["prompt_hash"],
            response_hash=material["payload_hash"],
            objective_scope_by_document=objective_scope,
            objective_component_by_id=objective_components,
            extraction_semantics_version=FACT_EXTRACTION_SEMANTICS_VERSION,
        )
        if rejections or pending:
            raise AssertionError((rejections, pending))
        claims.extend(
            row for row in page_claims if row["document_id"] in current_ids
        )
        dispositions.extend(
            row
            for row in page_dispositions
            if row["document_id"] in current_ids
        )
    compilation = EvidenceFactCompiler().compile(
        target_id=TARGET,
        as_of_date=AS_OF_DATE,
        accepted_claims=claims,
    )
    return claims, dispositions, compilation


def _checkpoint_payload(*, epoch, prior, fact_rows):
    review = ResearchSupervisorReview(
        review_id=f"SUPERVISOR-{epoch}",
        epoch=epoch,
        status="NEXT_RESEARCH_REQUIRED",
        component_status={
            component_id: "PENDING"
            for component_id in CANONICAL_COMPONENT_ORDER
        },
        unresolved_material_questions=("fixture remains pending",),
        source_family_gaps=(),
        parser_or_extractor_failures=(),
        next_actions=("continue deterministic fixture verification",),
        counter_and_supersession_checked=False,
        structured_data_complete=False,
        ready_for_independent_saturation_review=False,
        rationale="fixture supervisor remains pending",
    )
    fact_ids = sorted(str(row["fact_id"]) for row in fact_rows)
    state = {
        "schema_version": "e2r_research_epoch_checkpoint_v3",
        "target_id": TARGET,
        "as_of_date": AS_OF_DATE,
        "epoch": epoch,
        "status": "NEXT_RESEARCH_REQUIRED",
        "resumed_from_checkpoint_id": (
            prior["checkpoint_id"] if prior is not None else None
        ),
        "source_graph_checkpoint_id": f"SGCHECK-{epoch}",
        "queries": [],
        "documents": [],
        "new_facts": [dict(row) for row in fact_rows] if prior is None else [],
        "retired_facts": [],
        "changed_component_memos": [],
        "unresolved_material_questions": ["fixture remains pending"],
        "next_actions": ["continue deterministic fixture verification"],
        "supervisor_review": review.to_dict(),
        "saturation_reviews": [],
        "saturation_certificate": None,
        "cumulative_query_ids": [],
        "cumulative_document_ids": [],
        "cumulative_fact_ids": fact_ids,
        "current_fact_ids": fact_ids,
        "retired_fact_ids": [],
        "component_memo_hashes": {},
        "semantic_saturation_certified": False,
        "gold_evaluation_status": "NOT_RUN_POST_RUN_ONLY",
        "gold_critical_fact_miss_count": None,
        "completion_based_on_fixed_rounds": False,
        "zero_search_result_treated_as_saturation": False,
        "transport_budget_treated_as_completion": False,
        "production_score_authority": False,
    }
    state = _json_safe(state)
    state["checkpoint_id"] = _research_checkpoint_id(state)
    state["checkpoint_hash"] = _research_checkpoint_hash(state)
    return state


def _write_fact_ledger(root: Path, compiled_facts):
    compiled_rows = [row.to_dict() for row in compiled_facts]
    filler_rows = [
        {
            "fact_id": f"EFACT-FILLER-{index:04d}",
            "target_id": TARGET,
            "as_of_date": AS_OF_DATE,
            "claim_ids": [f"RFC-FILLER-{index:04d}"],
            "source_ids": [f"SGDOC-FILLER-{index:04d}"],
        }
        for index in range(457)
    ]
    all_rows = [*compiled_rows, *filler_rows]
    first = _checkpoint_payload(epoch=1, prior=None, fact_rows=all_rows)
    second = _checkpoint_payload(epoch=2, prior=first, fact_rows=all_rows)
    (root / "research_epochs.jsonl").write_text(
        "\n".join(
            json.dumps(row, ensure_ascii=False, sort_keys=True)
            for row in (first, second)
        )
        + "\n",
        encoding="utf-8",
    )
    (root / "research_epoch_checkpoint.json").write_text(
        json.dumps(second, ensure_ascii=False, sort_keys=True, indent=2)
        + "\n",
        encoding="utf-8",
    )
    return filler_rows, first, second


class CurrentFactLineageMaterialTests(unittest.TestCase):
    def test_actual_shaped_54_to_52_to_42_replays_official_validator(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            fixture = _build_actual_shaped_journal(root)

            materials = validate_current_v5_fact_lineage_materials(
                journal_root=fixture["journal"],
                target_id=TARGET,
                as_of_date=AS_OF_DATE,
                archetype_id=ARCHETYPE,
                current_documents=fixture["current_documents"],
                current_fact_prompt_payload=fixture[
                    "current_prompt_payload"
                ],
            )

            self.assertEqual(
                materials["status"],
                "READY_FOR_OFFICIAL_SEMANTIC_REPLAY",
            )
            self.assertFalse(materials["safe_to_materialize_facts"])
            self.assertEqual(materials["request_count"], 6)
            self.assertEqual(materials["lineage_call_group_count"], 6)
            self.assertEqual(materials["historical_batch_document_count"], 54)
            self.assertEqual(materials["current_document_count"], 52)
            self.assertEqual(materials["stale_sibling_document_count"], 2)
            self.assertEqual(materials["response_fact_proposal_count"], 42)
            self.assertEqual(
                set(materials["current_document_material_occurrence_counts"].values()),
                {1},
            )
            self.assertEqual(
                materials["objective_binding_reassessment_pending_count"],
                1,
            )
            self.assertTrue(
                materials["objective_lineage_reassessment"][0][
                    "preserve_current_fact_lineage"
                ]
            )

            claims, dispositions, compilation = _official_replay(materials)
            self.assertEqual(len(claims), 42)
            self.assertEqual(len(dispositions), 52)
            self.assertEqual(compilation.status, "FACT_COMPILATION_COMPLETE")
            self.assertEqual(len(compilation.facts), 42)
            self.assertEqual(
                len({row["document_id"] for row in claims}),
                13,
            )

            filler_rows, _first, _second = _write_fact_ledger(
                root,
                compilation.facts,
            )
            ledger = load_authoritative_research_epoch_fact_ledger(
                root,
                target_id=TARGET,
                as_of_date=AS_OF_DATE,
            )
            expectation = ledger.recovery_expectation(
                persisted_fact_ids=[row["fact_id"] for row in filler_rows]
            )
            compiled_fact_ids = [row.fact_id for row in compilation.facts]
            claim_ids = [row["claim_id"] for row in claims]
            self.assertEqual(ledger.epoch_count, 2)
            self.assertEqual(len(ledger.current_fact_ids), 499)
            self.assertEqual(
                set(expectation["expected_recovered_fact_ids"]),
                set(compiled_fact_ids),
            )
            self.assertEqual(
                set(expectation["expected_recovered_claim_ids"]),
                set(claim_ids),
            )
            self.assertEqual(
                expectation["expected_recovered_source_document_count"],
                13,
            )
            receipt = ledger.exact_recovery_receipt(
                persisted_fact_ids=[row["fact_id"] for row in filler_rows],
                recovered_fact_ids=compiled_fact_ids,
                recovered_claim_ids=claim_ids,
            )
            self.assertTrue(receipt["exact_intersection"])
            self.assertEqual(receipt["authoritative_current_fact_count"], 499)
            self.assertEqual(receipt["persisted_current_fact_count"], 457)
            self.assertEqual(receipt["recovered_fact_count"], 42)

            pending_id = "EFACT-PENDING-NEXT-EPOCH"
            with self.assertRaisesRegex(ValueError, "pending_new_fact_ids"):
                ledger.recovery_expectation(
                    persisted_fact_ids=[*ledger.current_fact_ids, pending_id]
                )
            pending = ledger.recovery_expectation(
                persisted_fact_ids=[*ledger.current_fact_ids, pending_id],
                pending_new_fact_ids=[pending_id],
            )
            self.assertEqual(
                pending["status"],
                "PENDING_NEW_FACT_EPOCH_COMMIT_REQUIRED",
            )
            self.assertEqual(pending["expected_recovered_fact_count"], 0)
            with self.assertRaisesRegex(ValueError, "authority loss"):
                ledger.exact_recovery_receipt(
                    persisted_fact_ids=[*ledger.current_fact_ids, pending_id],
                    pending_new_fact_ids=[pending_id],
                    recovered_fact_ids=[],
                    recovered_claim_ids=[],
                )

            retired_id = ledger.current_fact_ids[0]
            projected = ledger.recovery_expectation(
                persisted_fact_ids=[
                    fact_id
                    for fact_id in ledger.current_fact_ids
                    if fact_id != retired_id
                ],
                pending_retired_fact_ids=[retired_id],
            )
            self.assertEqual(
                projected["status"],
                "PENDING_FACT_RETIREMENT_EPOCH_COMMIT_REQUIRED",
            )
            self.assertEqual(projected["expected_recovered_fact_count"], 0)
            self.assertEqual(
                projected["pending_retired_fact_ids"],
                [retired_id],
            )
            unclassified = ledger.recovery_expectation(
                persisted_fact_ids=[
                    fact_id
                    for fact_id in ledger.current_fact_ids
                    if fact_id != retired_id
                ],
            )
            self.assertEqual(
                unclassified["status"],
                "AUTHORITY_LOSS_RECOVERY_REQUIRED",
            )
            self.assertEqual(
                unclassified["expected_recovered_fact_ids"],
                [retired_id],
            )

    def test_content_mismatch_invalidates_the_entire_material_set(self):
        with tempfile.TemporaryDirectory() as directory:
            fixture = _build_actual_shaped_journal(Path(directory))
            current = [dict(row) for row in fixture["current_documents"]]
            current[0]["content_text"] += " changed"
            current[0]["content_hash"] = hashlib.sha256(
                current[0]["content_text"].encode("utf-8")
            ).hexdigest()

            result = validate_current_v5_fact_lineage_materials(
                journal_root=fixture["journal"],
                target_id=TARGET,
                as_of_date=AS_OF_DATE,
                archetype_id=ARCHETYPE,
                current_documents=current,
                current_fact_prompt_payload=fixture[
                    "current_prompt_payload"
                ],
            )

            self.assertEqual(result["status"], "INVALID")
            self.assertEqual(result["materials"], [])
            self.assertEqual(result["request_count"], 0)
            self.assertTrue(result["atomic_all_or_nothing"])

    def test_absent_journal_is_distinct_from_invalid_lineage(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            document = _prompt_document("SGDOC-ABSENT", "OBJECTIVE-ABSENT")
            payload = _prompt_payload([document], marker="absent")

            result = validate_current_v5_fact_lineage_materials(
                journal_root=root / "collaboration_codex_subagent_provider",
                target_id=TARGET,
                as_of_date=AS_OF_DATE,
                archetype_id=ARCHETYPE,
                current_documents=[_current_document(document)],
                current_fact_prompt_payload=payload,
            )

            self.assertEqual(result["status"], "ABSENT")
            self.assertEqual(result["materials"], [])
            self.assertNotIn("invalid_reason", result)

    def test_ordered_continuation_is_returned_with_its_base(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            journal = root / "collaboration_codex_subagent_provider"
            transport = CollaborationCodexSubagentTransport()
            transport.configure_journal_root(journal)
            document = _prompt_document("SGDOC-PAGED", "OBJECTIVE-PAGED")
            current = _current_document(document)
            first = _proposal(document, claim_index=1, quote_index=0)
            second = _proposal(document, claim_index=2, quote_index=1)
            base = _prompt_payload([document], marker="paged")
            _write_pair(
                transport,
                journal,
                payload=base,
                response=_response([document], [first], complete=False),
                agent_model="codex-gpt-5.4",
            )
            continuation = {
                **base,
                "fact_extraction_continuation_context": {
                    "page_number": 2,
                    "page_fact_limit": 12,
                    "required_document_ids": [document["document_id"]],
                    "previously_accepted_facts": [
                        {
                            "document_id": first["document_id"],
                            "question_family_id": first["question_family_id"],
                            "subject_id": first["subject_id"],
                            "predicate_family": first["predicate_family"],
                            "normalized_object": first["normalized_object"],
                            "period": first["period"],
                            "direction": first["direction"],
                            "current_lifecycle": first["current_lifecycle"],
                            "objective_ids": first["objective_ids"],
                            "objective_relation": first["objective_relation"],
                            "exact_quote": first["exact_quote"],
                        }
                    ],
                    "instruction": "continue the exact ordered batch",
                },
            }
            _write_pair(
                transport,
                journal,
                payload=continuation,
                response=_response([document], [second], complete=True),
                agent_model="codex-collaboration",
            )

            result = validate_current_v5_fact_lineage_materials(
                journal_root=journal,
                target_id=TARGET,
                as_of_date=AS_OF_DATE,
                archetype_id=ARCHETYPE,
                current_documents=[current],
                current_fact_prompt_payload=base,
            )

            self.assertEqual(
                result["status"],
                "READY_FOR_OFFICIAL_SEMANTIC_REPLAY",
            )
            self.assertEqual(result["request_count"], 2)
            self.assertEqual(result["lineage_call_group_count"], 1)
            self.assertEqual(result["historical_batch_document_count"], 1)
            self.assertEqual(result["response_fact_proposal_count"], 2)
            self.assertEqual(
                [row["continuation_page_number"] for row in result["materials"]],
                [1, 2],
            )

    def test_local_or_unknown_codex_labels_fail_closed(self):
        for model in (
            "codex-local",
            "codex-ollama",
            "codex-unknown",
            "codex-gpt-5-local",
        ):
            with self.subTest(model=model), tempfile.TemporaryDirectory() as directory:
                root = Path(directory)
                journal = root / "collaboration_codex_subagent_provider"
                transport = CollaborationCodexSubagentTransport()
                transport.configure_journal_root(journal)
                document = _prompt_document("SGDOC-ONE", "OBJECTIVE-ONE")
                payload = _prompt_payload([document], marker=model)
                _write_pair(
                    transport,
                    journal,
                    payload=payload,
                    response=_response([document], []),
                    agent_model=model,
                )

                result = validate_current_v5_fact_lineage_materials(
                    journal_root=journal,
                    target_id=TARGET,
                    as_of_date=AS_OF_DATE,
                    archetype_id=ARCHETYPE,
                    current_documents=[_current_document(document)],
                    current_fact_prompt_payload=payload,
                )

                self.assertEqual(result["status"], "INVALID")
                self.assertEqual(result["materials"], [])

    def test_current_hosted_codex_collaboration_model_labels_are_accepted(self):
        for model in (
            "gpt-5.6-sol",
            "gpt-5.6-terra",
            "gpt-5.6-luna",
            "gpt-5.5",
            "gpt-daybreak-blue-latest",
        ):
            with self.subTest(model=model), tempfile.TemporaryDirectory() as directory:
                root = Path(directory)
                journal = root / "collaboration_codex_subagent_provider"
                transport = CollaborationCodexSubagentTransport()
                transport.configure_journal_root(journal)
                document = _prompt_document("SGDOC-ONE", "OBJECTIVE-ONE")
                payload = _prompt_payload([document], marker=model)
                _write_pair(
                    transport,
                    journal,
                    payload=payload,
                    response=_response([document], []),
                    agent_model=model,
                )

                result = validate_current_v5_fact_lineage_materials(
                    journal_root=journal,
                    target_id=TARGET,
                    as_of_date=AS_OF_DATE,
                    archetype_id=ARCHETYPE,
                    current_documents=[_current_document(document)],
                    current_fact_prompt_payload=payload,
                )

                self.assertEqual(
                    result["status"],
                    "READY_FOR_OFFICIAL_SEMANTIC_REPLAY",
                )
                self.assertEqual(len(result["materials"]), 1)

    def test_current_hosted_codex_label_with_local_suffix_fails_closed(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            journal = root / "collaboration_codex_subagent_provider"
            transport = CollaborationCodexSubagentTransport()
            transport.configure_journal_root(journal)
            document = _prompt_document("SGDOC-ONE", "OBJECTIVE-ONE")
            payload = _prompt_payload([document], marker="gpt-5.6-sol-local")
            _write_pair(
                transport,
                journal,
                payload=payload,
                response=_response([document], []),
                agent_model="gpt-5.6-sol-local",
            )

            result = validate_current_v5_fact_lineage_materials(
                journal_root=journal,
                target_id=TARGET,
                as_of_date=AS_OF_DATE,
                archetype_id=ARCHETYPE,
                current_documents=[_current_document(document)],
                current_fact_prompt_payload=payload,
            )

            self.assertEqual(result["status"], "INVALID")
            self.assertEqual(result["materials"], [])

    def test_blind_envelope_and_epoch_head_tampering_fail_closed(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            journal = root / "collaboration_codex_subagent_provider"
            transport = CollaborationCodexSubagentTransport()
            transport.configure_journal_root(journal)
            document = _prompt_document("SGDOC-BLIND", "OBJECTIVE-BLIND")
            payload = _prompt_payload([document], marker="blind")
            prompt = "fact fixture\n" + json.dumps(
                payload,
                ensure_ascii=False,
                sort_keys=True,
                separators=(",", ":"),
            )
            permissive_schema = {"type": "object"}
            with self.assertRaises(StructuredProviderUnavailable):
                transport.complete(
                    prompt=prompt,
                    output_schema=permissive_schema,
                    schema_name="e2r_v5_evidence_fact_extraction",
                )
            request_id = transport._last_request_id
            assert request_id is not None
            request = json.loads(
                (journal / "requests" / f"{request_id}.json").read_text(
                    encoding="utf-8"
                )
            )
            blind_payload = {"stage": "5"}
            provenance = _validate_agent_provenance(
                agent_id="blind-agent",
                canonical_task_name="/root/blind_fixture",
                agent_model="codex-gpt-5",
            )
            payload_hash = _canonical_hash(blind_payload)
            response_id = "COLLABRESP-" + _canonical_hash(
                {
                    "request_id": request_id,
                    "payload_hash": payload_hash,
                    "provenance": provenance,
                }
            )
            envelope = {
                "schema_version": COLLABORATION_RESPONSE_SCHEMA_VERSION,
                "response_id": response_id,
                "request_id": request_id,
                "prompt_hash": request["prompt_hash"],
                "output_schema_hash": request["output_schema_hash"],
                "provider_identity_hash": request["provider_identity_hash"],
                "payload_hash": payload_hash,
                "payload": blind_payload,
                "provenance": provenance,
                "validation": {
                    "draft202012_schema_valid": True,
                    "blind_research_output_valid": True,
                    "request_hashes_valid": True,
                    "downstream_semantic_validation_required": True,
                },
                "score_or_stage_authority": False,
                "production_score_authority": False,
            }
            (journal / "responses" / f"{request_id}.json").write_text(
                json.dumps(envelope, ensure_ascii=False, sort_keys=True),
                encoding="utf-8",
            )
            result = validate_current_v5_fact_lineage_materials(
                journal_root=journal,
                target_id=TARGET,
                as_of_date=AS_OF_DATE,
                archetype_id=ARCHETYPE,
                current_documents=[_current_document(document)],
                current_fact_prompt_payload=payload,
            )
            self.assertEqual(result["status"], "INVALID")
            self.assertEqual(result["materials"], [])

            fact = {
                "fact_id": "EFACT-ONE",
                "target_id": TARGET,
                "as_of_date": AS_OF_DATE,
                "claim_ids": ["RFC-ONE"],
                "source_ids": ["SGDOC-ONE"],
            }
            first = _checkpoint_payload(epoch=1, prior=None, fact_rows=[fact])
            second = _checkpoint_payload(epoch=2, prior=first, fact_rows=[fact])
            (root / "research_epochs.jsonl").write_text(
                "\n".join(json.dumps(row) for row in (first, second)) + "\n",
                encoding="utf-8",
            )
            (root / "research_epoch_checkpoint.json").write_text(
                json.dumps(first),
                encoding="utf-8",
            )
            with self.assertRaisesRegex(ValueError, "canonical JSONL head"):
                load_authoritative_research_epoch_fact_ledger(
                    root,
                    target_id=TARGET,
                    as_of_date=AS_OF_DATE,
                )


if __name__ == "__main__":
    unittest.main()
