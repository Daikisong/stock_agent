"""Validate and apply compact RepairDeltaV3 without trusting Pro authority."""

from __future__ import annotations

from copy import deepcopy
import json
from pathlib import Path
from typing import Any, Mapping, Sequence
from urllib.parse import urlsplit

from jsonschema import Draft202012Validator, FormatChecker

from ..dossier import DossierValidationContext, ResearchDossierValidator
from ..ids import canonical_hash, stable_id
from ..preflight import CanonicalURLResolver, TextQuoteNormalizer
from .models_v3 import (
    CompiledCompactRepairPromptV3,
    PRO_REPAIRABLE_ROOT_CAUSES,
    REPAIR_ACTIONS_V3,
    REPAIR_ACTION_CONTRACT,
    REPAIR_DELTA_V3_SCHEMA_VERSION,
    RepairActionOutcomeV3,
    RepairApplicationV3,
)


_FACT_COLLECTIONS = ("material_facts", "counterfacts", "resolution_facts")
_FORBIDDEN_AUTHORITY_FIELDS = frozenset(
    {"final_score", "final_stage", "canonical_stage", "score_value", "stage_decision"}
)


class RepairDeltaV3ValidationError(ValueError):
    pass


class RepairDeltaV3Validator:
    def __init__(self, schema_path: str | Path | None = None) -> None:
        path = (
            Path(schema_path).resolve()
            if schema_path
            else Path(__file__).resolve().parents[4]
            / "configs/e2r_pro_repair_delta_v3.schema.json"
        )
        self.schema = json.loads(path.read_text(encoding="utf-8"))
        Draft202012Validator.check_schema(self.schema)
        self.validator = Draft202012Validator(
            self.schema,
            format_checker=FormatChecker(),
        )

    def validate(
        self,
        payload: Mapping[str, Any],
        *,
        dossier: Mapping[str, Any],
        compiled_prompt: CompiledCompactRepairPromptV3,
    ) -> None:
        errors = sorted(
            self.validator.iter_errors(payload), key=lambda row: tuple(row.path)
        )
        if errors:
            details = "; ".join(
                f"{'/'.join(str(value) for value in row.path) or '$'}: {row.message}"
                for row in errors
            )
            raise RepairDeltaV3ValidationError(
                f"RepairDeltaV3 schema validation failed: {details}"
            )
        for key, expected in (
            ("schema_version", REPAIR_DELTA_V3_SCHEMA_VERSION),
            ("job_id", compiled_prompt.job_id),
            ("run_id", compiled_prompt.run_id),
            ("research_pass_id", compiled_prompt.research_pass_id),
            ("parent_pass_id", compiled_prompt.parent_pass_id),
            ("as_of_date", compiled_prompt.as_of_date),
        ):
            if payload.get(key) != expected:
                raise RepairDeltaV3ValidationError(f"repair delta {key} mismatch")
        if canonical_hash(payload.get("target") or {}) != canonical_hash(
            compiled_prompt.target
        ):
            raise RepairDeltaV3ValidationError("repair delta target mismatch")
        if payload.get("score_authority") is not False:
            raise RepairDeltaV3ValidationError("repair delta score_authority must be false")
        if payload.get("stage_authority") is not False:
            raise RepairDeltaV3ValidationError("repair delta stage_authority must be false")
        forbidden = _find_forbidden_fields(payload)
        if forbidden:
            raise RepairDeltaV3ValidationError(
                f"repair delta contains score/Stage authority fields: {forbidden}"
            )

        prompt_candidates = {
            str(row.get("candidate_id") or ""): row
            for group in compiled_prompt.groups
            for row in group.candidates
        }
        actions = tuple(payload.get("repair_actions") or ())
        action_ids = tuple(str(row.get("candidate_id") or "") for row in actions)
        if len(action_ids) != len(set(action_ids)):
            raise RepairDeltaV3ValidationError(
                "one compact repair candidate may have only one action"
            )
        if set(action_ids) != set(compiled_prompt.candidate_ids):
            raise RepairDeltaV3ValidationError(
                "repair actions must cover the exact compiled candidate roster"
            )

        existing_facts = _fact_map(dossier)
        existing_sources = {
            str(row.get("source_document_id") or ""): row
            for row in dossier.get("source_documents") or ()
        }
        new_sources = tuple(payload.get("new_source_documents") or ())
        new_source_by_id = {
            str(row.get("source_document_id") or ""): row for row in new_sources
        }
        if len(new_source_by_id) != len(new_sources):
            raise RepairDeltaV3ValidationError("duplicate new source document ids")
        if set(new_source_by_id).intersection(existing_sources):
            raise RepairDeltaV3ValidationError(
                "new source document id collides with the dossier"
            )
        used_nested_source_ids: set[str] = set()
        replacement_ids: set[str] = set()
        replacement_questions: dict[str, set[str]] = {}
        replacement_sources: dict[str, str] = {}
        for action in actions:
            candidate_id = str(action.get("candidate_id") or "")
            prompt_candidate = prompt_candidates[candidate_id]
            original = existing_facts.get(candidate_id)
            if original is None:
                raise RepairDeltaV3ValidationError(
                    "repair action references an unknown dossier candidate"
                )
            immutable_echo = {
                "question_family_ids": list(
                    prompt_candidate.get("question_family_ids") or ()
                ),
                "rejection_category": prompt_candidate.get("rejection_category"),
                "original_statement": prompt_candidate.get("original_statement"),
                "source_document_id": prompt_candidate.get("source_document_id"),
                "canonical_url": prompt_candidate.get("canonical_url"),
                "allowed_action": REPAIR_ACTION_CONTRACT,
            }
            for key, expected in immutable_echo.items():
                if action.get(key) != expected:
                    raise RepairDeltaV3ValidationError(
                        f"repair action changed immutable packet field: {candidate_id}/{key}"
                    )
            if action.get("rejection_category") not in PRO_REPAIRABLE_ROOT_CAUSES:
                raise RepairDeltaV3ValidationError(
                    "non-semantic/local rejection escaped into repair"
                )
            selected = str(action.get("action") or "")
            if selected not in REPAIR_ACTIONS_V3:
                raise RepairDeltaV3ValidationError("unknown compact repair action")
            replacement = action.get("replacement_fact")
            nested_source = action.get("replacement_source_document")
            if selected == "WITHDRAW":
                if replacement is not None or nested_source is not None:
                    raise RepairDeltaV3ValidationError(
                        "WITHDRAW cannot carry replacement evidence"
                    )
                continue
            if not isinstance(replacement, Mapping):
                raise RepairDeltaV3ValidationError(
                    "non-withdraw repair requires one replacement fact"
                )
            replacement_id = str(replacement.get("dossier_fact_id") or "")
            if (
                not replacement_id
                or replacement_id in existing_facts
                or replacement_id in replacement_ids
            ):
                raise RepairDeltaV3ValidationError(
                    "replacement fact id must be new and unique"
                )
            replacement_ids.add(replacement_id)
            if replacement.get("research_pass_id") != compiled_prompt.research_pass_id:
                raise RepairDeltaV3ValidationError(
                    "replacement fact belongs to another research pass"
                )
            if replacement.get("target_id") != (
                (dossier.get("target") or {}).get("target_id")
            ):
                raise RepairDeltaV3ValidationError("replacement fact changed target")
            if replacement.get("fact_kind") != original.get("fact_kind"):
                raise RepairDeltaV3ValidationError("replacement fact changed fact kind")
            replacement_question_ids = {
                str(value) for value in replacement.get("question_family_ids") or ()
            }
            if replacement_question_ids != set(
                str(value) for value in original.get("question_family_ids") or ()
            ):
                raise RepairDeltaV3ValidationError(
                    "replacement fact changed its question-family scope"
                )
            source_id = str(replacement.get("source_document_id") or "")
            if selected in {"CORRECT", "NARROW"}:
                if nested_source is not None or source_id != original.get(
                    "source_document_id"
                ):
                    raise RepairDeltaV3ValidationError(
                        "CORRECT/NARROW must stay on the original source document"
                    )
            else:
                if nested_source is not None:
                    if not isinstance(nested_source, Mapping):
                        raise RepairDeltaV3ValidationError(
                            "replacement source document must be an object"
                        )
                    nested_id = str(nested_source.get("source_document_id") or "")
                    if source_id != nested_id or new_source_by_id.get(nested_id) != nested_source:
                        raise RepairDeltaV3ValidationError(
                            "REPLACE source must exactly match new_source_documents"
                        )
                    used_nested_source_ids.add(nested_id)
                elif source_id not in existing_sources:
                    raise RepairDeltaV3ValidationError(
                        "REPLACE fact references an undeclared source document"
                    )
            replacement_questions[replacement_id] = replacement_question_ids
            replacement_sources[replacement_id] = source_id
        if used_nested_source_ids != set(new_source_by_id):
            raise RepairDeltaV3ValidationError(
                "new_source_documents contains an unused or unbound document"
            )

        existing_route_ids = {
            str(row.get("route_receipt_id") or "")
            for row in dossier.get("search_route_receipts") or ()
        }
        routes = tuple(payload.get("new_route_receipts") or ())
        route_ids = tuple(str(row.get("route_receipt_id") or "") for row in routes)
        if len(route_ids) != len(set(route_ids)) or set(route_ids).intersection(
            existing_route_ids
        ):
            raise RepairDeltaV3ValidationError("repair route id is duplicate")
        covered_replacements: set[str] = set()
        source_by_id = {**existing_sources, **new_source_by_id}
        for route in routes:
            if route.get("pass_id") != compiled_prompt.research_pass_id:
                raise RepairDeltaV3ValidationError(
                    "repair route belongs to another research pass"
                )
            accepted = {
                str(value) for value in route.get("accepted_fact_ids") or ()
            }
            if not accepted or not accepted.issubset(replacement_ids):
                raise RepairDeltaV3ValidationError(
                    "repair route must bind only replacement facts"
                )
            question_id = str(route.get("question_family_id") or "")
            for replacement_id in accepted:
                if question_id not in replacement_questions[replacement_id]:
                    raise RepairDeltaV3ValidationError(
                        "repair route escapes replacement question scope"
                    )
                source = source_by_id[replacement_sources[replacement_id]]
                if str(source.get("canonical_url") or "") not in {
                    str(value) for value in route.get("opened_source_urls") or ()
                }:
                    raise RepairDeltaV3ValidationError(
                        "repair route did not open the replacement source URL"
                    )
            covered_replacements.update(accepted)
        if covered_replacements != replacement_ids:
            raise RepairDeltaV3ValidationError(
                "every replacement fact requires a current-pass route receipt"
            )


def normalize_repair_delta_v3_transport(
    *,
    repair_delta: Mapping[str, Any],
    dossier: Mapping[str, Any],
    compiled_prompt: CompiledCompactRepairPromptV3,
    performed_at: str,
) -> tuple[Mapping[str, Any], Mapping[str, Any]]:
    """Canonicalize bounded response-envelope omissions before validation.

    The raw Pro response remains immutable in the browser capture.  This
    normalizer never changes a replacement statement, excerpt, value, question
    scope, source URL/content, or authority field.  It may canonicalize a new
    source ID back to an existing document with the exact same canonical URL,
    bind a declared new source to the action that already references it,
    relabel a source-changing action as REPLACE, fail closed to WITHDRAW when a
    proposed fact conflicts with the canonical source scope, and create a
    pending local-reverification route when the response omitted that
    redundant envelope row.
    """

    normalized = deepcopy(dict(repair_delta))
    actions = tuple(normalized.get("repair_actions") or ())
    action_ids = tuple(str(row.get("candidate_id") or "") for row in actions)
    if len(action_ids) != len(set(action_ids)) or set(action_ids) != set(
        compiled_prompt.candidate_ids
    ):
        raise RepairDeltaV3ValidationError(
            "repair transport normalization requires the exact candidate roster"
        )
    prompt_candidates = {
        str(row.get("candidate_id") or ""): row
        for group in compiled_prompt.groups
        for row in group.candidates
    }
    facts = _fact_map(dossier)
    sources = {
        str(row.get("source_document_id") or ""): row
        for row in dossier.get("source_documents") or ()
    }
    existing_source_by_url = {
        str(row.get("canonical_url") or ""): row
        for row in sources.values()
        if str(row.get("canonical_url") or "")
    }
    operations: list[Mapping[str, Any]] = []
    source_id_remap: dict[str, str] = {}
    canonical_new_source_rows: list[Mapping[str, Any]] = []
    for source in normalized.get("new_source_documents") or ():
        source_id = str(source.get("source_document_id") or "")
        canonical_url = str(source.get("canonical_url") or "")
        existing = existing_source_by_url.get(canonical_url)
        if existing is None:
            canonical_new_source_rows.append(source)
            continue
        existing_id = str(existing.get("source_document_id") or "")
        source_id_remap[source_id] = existing_id
        operations.append(
            {
                "operation": "DEDUPLICATE_DECLARED_SOURCE_BY_CANONICAL_URL",
                "declared_source_document_id": source_id,
                "canonical_source_document_id": existing_id,
                "canonical_url_hash": canonical_hash(canonical_url),
            }
        )
    normalized["new_source_documents"] = canonical_new_source_rows
    new_sources = {
        str(row.get("source_document_id") or ""): row
        for row in canonical_new_source_rows
    }
    all_sources = {**sources, **new_sources}
    questions = {
        str(row.get("question_family_id") or ""): row
        for row in dossier.get("question_family_results") or ()
    }
    existing_route_ids = {
        str(row.get("route_receipt_id") or "")
        for row in dossier.get("search_route_receipts") or ()
    }
    routes = list(normalized.get("new_route_receipts") or ())
    for action in actions:
        candidate_id = str(action.get("candidate_id") or "")
        candidate = prompt_candidates.get(candidate_id)
        original = facts.get(candidate_id)
        if candidate is None or original is None:
            raise RepairDeltaV3ValidationError(
                "repair transport normalization encountered an unknown candidate"
            )
        for key, expected in (
            ("question_family_ids", list(candidate.get("question_family_ids") or ())),
            ("rejection_category", candidate.get("rejection_category")),
            ("original_statement", candidate.get("original_statement")),
            ("source_document_id", candidate.get("source_document_id")),
            ("canonical_url", candidate.get("canonical_url")),
            ("allowed_action", REPAIR_ACTION_CONTRACT),
        ):
            if action.get(key) != expected:
                raise RepairDeltaV3ValidationError(
                    "repair transport normalization refuses changed immutable "
                    f"scope: {candidate_id}/{key}"
                )
        replacement = action.get("replacement_fact")
        if not isinstance(replacement, Mapping):
            continue
        replacement_id = str(replacement.get("dossier_fact_id") or "")
        source_id = str(replacement.get("source_document_id") or "")
        canonical_source_id = source_id_remap.get(source_id)
        if canonical_source_id is not None:
            replacement["source_document_id"] = canonical_source_id
            nested = action.get("replacement_source_document")
            if isinstance(nested, Mapping) and str(
                nested.get("source_document_id") or ""
            ) == source_id:
                action["replacement_source_document"] = None
            operations.append(
                {
                    "operation": "REMAP_REPLACEMENT_TO_CANONICAL_SOURCE_ID",
                    "candidate_id": candidate_id,
                    "declared_source_document_id": source_id,
                    "canonical_source_document_id": canonical_source_id,
                }
            )
            source_id = canonical_source_id
        source = all_sources.get(source_id)
        if source is None:
            raise RepairDeltaV3ValidationError(
                "repair transport normalization cannot invent a missing source"
            )
        source_issuer_scoped = (source.get("target_scope") or {}).get(
            "issuer_scoped"
        )
        if replacement.get("issuer_scoped") is not source_issuer_scoped:
            action["action"] = "WITHDRAW"
            action["replacement_fact"] = None
            action["replacement_source_document"] = None
            action["reason"] = (
                "Deterministic source-scope validation rejected the proposed "
                "replacement; the original candidate is withdrawn."
            )
            operations.append(
                {
                    "operation": "WITHDRAW_SCOPE_MISMATCHED_REPLACEMENT",
                    "candidate_id": candidate_id,
                    "replacement_id": replacement_id,
                    "source_document_id": source_id,
                }
            )
            continue
        if source_id in new_sources and action.get("replacement_source_document") is None:
            action["replacement_source_document"] = deepcopy(new_sources[source_id])
            operations.append(
                {
                    "operation": "BIND_DECLARED_NEW_SOURCE_TO_ACTION",
                    "candidate_id": candidate_id,
                    "source_document_id": source_id,
                }
            )
        if (
            str(action.get("action") or "") in {"CORRECT", "NARROW"}
            and source_id != str(original.get("source_document_id") or "")
        ):
            action["action"] = "REPLACE"
            operations.append(
                {
                    "operation": "RELABEL_SOURCE_CHANGING_ACTION_AS_REPLACE",
                    "candidate_id": candidate_id,
                    "source_document_id": source_id,
                }
            )
        already_covered = any(
            replacement_id
            in {str(value) for value in row.get("accepted_fact_ids") or ()}
            for row in routes
        )
        if already_covered:
            continue
        replacement_questions = tuple(
            sorted(str(value) for value in replacement.get("question_family_ids") or ())
        )
        question_id = next(
            (value for value in replacement_questions if value in questions),
            None,
        )
        source_roles = tuple(
            sorted(str(value) for value in source.get("source_role_ids") or ())
        )
        canonical_url = str(source.get("canonical_url") or "")
        if question_id is None or not source_roles or not canonical_url:
            raise RepairDeltaV3ValidationError(
                "repair transport normalization lacks route derivation inputs"
            )
        question = questions[question_id]
        route_id = stable_id(
            "PROREPAIRROUTE",
            {
                "pass_id": compiled_prompt.research_pass_id,
                "candidate_id": candidate_id,
                "replacement_id": replacement_id,
                "source_document_id": source_id,
                "question_family_id": question_id,
            },
        )
        if route_id in existing_route_ids or any(
            str(row.get("route_receipt_id") or "") == route_id for row in routes
        ):
            raise RepairDeltaV3ValidationError(
                "derived compact repair route collides with an existing route"
            )
        unresolved_gaps = tuple(question.get("unresolved_gap_ids") or ())
        routes.append(
            {
                "route_receipt_id": route_id,
                "pass_id": compiled_prompt.research_pass_id,
                "archetype_id": str(question.get("archetype_id") or ""),
                "question_family_id": question_id,
                "gap_id": str(unresolved_gaps[0]) if unresolved_gaps else None,
                "source_role_id": source_roles[0],
                "query_or_navigation_objective": (
                    "Deterministic post-capture re-verification of Pro-declared "
                    f"repair source for {candidate_id}"
                ),
                "query_text": None,
                "result_count_seen": 1,
                "opened_source_urls": [canonical_url],
                "accepted_fact_ids": [replacement_id],
                "rejected_candidate_ids": [],
                "provider_status": "PROVIDER_PENDING",
                "no_new_route_reason": (
                    "Awaiting deterministic local source re-verification"
                ),
                "performed_at": performed_at,
            }
        )
        operations.append(
            {
                "operation": "ADD_LOCAL_REVERIFICATION_PENDING_ROUTE",
                "candidate_id": candidate_id,
                "replacement_id": replacement_id,
                "route_receipt_id": route_id,
                "source_document_id": source_id,
            }
        )
    active_replacement_ids = {
        str((row.get("replacement_fact") or {}).get("dossier_fact_id") or "")
        for row in actions
        if isinstance(row.get("replacement_fact"), Mapping)
    }
    retained_routes: list[Mapping[str, Any]] = []
    for route in routes:
        accepted_before = tuple(
            str(value) for value in route.get("accepted_fact_ids") or ()
        )
        accepted_after = tuple(
            value for value in accepted_before if value in active_replacement_ids
        )
        if not accepted_after:
            operations.append(
                {
                    "operation": "DROP_ROUTE_WITHOUT_ACTIVE_REPLACEMENT",
                    "route_receipt_id": str(route.get("route_receipt_id") or ""),
                }
            )
            continue
        if accepted_after != accepted_before:
            route["accepted_fact_ids"] = list(accepted_after)
            operations.append(
                {
                    "operation": "REMOVE_WITHDRAWN_REPLACEMENT_FROM_ROUTE",
                    "route_receipt_id": str(route.get("route_receipt_id") or ""),
                }
            )
        retained_routes.append(route)
    normalized["new_route_receipts"] = retained_routes
    referenced_new_source_ids = {
        str((row.get("replacement_fact") or {}).get("source_document_id") or "")
        for row in actions
        if isinstance(row.get("replacement_fact"), Mapping)
    }
    retained_new_sources: list[Mapping[str, Any]] = []
    for source in normalized.get("new_source_documents") or ():
        source_id = str(source.get("source_document_id") or "")
        if source_id not in referenced_new_source_ids:
            operations.append(
                {
                    "operation": "DROP_UNREFERENCED_DECLARED_SOURCE",
                    "source_document_id": source_id,
                }
            )
            continue
        retained_new_sources.append(source)
    normalized["new_source_documents"] = retained_new_sources
    raw_hash = canonical_hash(repair_delta)
    normalized_hash = canonical_hash(normalized)
    receipt_payload = {
        "schema_version": "e2r_repair_delta_v3_transport_normalization_v1",
        "status": "BOUNDED_STRUCTURAL_NORMALIZATION",
        "job_id": compiled_prompt.job_id,
        "run_id": compiled_prompt.run_id,
        "research_pass_id": compiled_prompt.research_pass_id,
        "parent_pass_id": compiled_prompt.parent_pass_id,
        "raw_delta_hash": raw_hash,
        "normalized_delta_hash": normalized_hash,
        "operation_count": len(operations),
        "operations": operations,
        "ignored_non_authority_response_fields": ["fetched_excerpt"],
        "replacement_semantic_field_changed_count": 0,
        "replacement_source_identity_canonicalized_count": sum(
            1
            for row in operations
            if row.get("operation")
            == "REMAP_REPLACEMENT_TO_CANONICAL_SOURCE_ID"
        ),
        "scope_mismatched_replacement_withdrawn_count": sum(
            1
            for row in operations
            if row.get("operation")
            == "WITHDRAW_SCOPE_MISMATCHED_REPLACEMENT"
        ),
        "question_scope_changed_count": 0,
        "source_url_or_content_changed_count": 0,
        "score_authority": False,
        "stage_authority": False,
    }
    receipt = {
        **receipt_payload,
        "receipt_hash": canonical_hash(receipt_payload),
    }
    return normalized, receipt


def apply_repair_delta_v3(
    *,
    dossier: Mapping[str, Any],
    repair_delta: Mapping[str, Any],
    compiled_prompt: CompiledCompactRepairPromptV3,
    prior_accepted_candidate_ids: Sequence[str],
    prompt_hash: str,
    response_hash: str,
    repair_pass_ordinal: int = 1,
    validator: RepairDeltaV3Validator | None = None,
    dossier_validator: ResearchDossierValidator | None = None,
) -> RepairApplicationV3:
    if repair_pass_ordinal != 1 or compiled_prompt.repair_pass_ordinal != 1:
        raise RepairDeltaV3ValidationError(
            "SECOND_REPAIR_PASS_BLOCKS_OPERATIONAL_READY"
        )
    if prompt_hash != compiled_prompt.prompt_hash:
        raise RepairDeltaV3ValidationError("repair prompt hash mismatch")
    if len(response_hash) != 64:
        raise RepairDeltaV3ValidationError("repair response hash must be sha256")
    (validator or RepairDeltaV3Validator()).validate(
        repair_delta,
        dossier=dossier,
        compiled_prompt=compiled_prompt,
    )
    facts_before = _fact_map(dossier)
    prior_accepted = tuple(
        dict.fromkeys(str(value) for value in prior_accepted_candidate_ids)
    )
    if not set(prior_accepted).issubset(facts_before):
        raise RepairDeltaV3ValidationError(
            "prior accepted roster references an unknown fact"
        )
    accepted_hashes = {
        candidate_id: canonical_hash(facts_before[candidate_id])
        for candidate_id in prior_accepted
    }
    candidate_ids = set(compiled_prompt.candidate_ids)
    if candidate_ids.intersection(prior_accepted):
        raise RepairDeltaV3ValidationError("repair cannot target an accepted fact")

    effective = deepcopy(dict(dossier))
    question_ids = {
        str(value)
        for action in repair_delta.get("repair_actions") or ()
        for value in action.get("question_family_ids") or ()
    }
    prior_question_states = {
        str(row.get("question_family_id") or ""): deepcopy(dict(row))
        for row in effective.get("question_family_results") or ()
        if str(row.get("question_family_id") or "") in question_ids
    }
    new_sources = [
        _normalize_new_source_document(row)
        for row in repair_delta.get("new_source_documents") or ()
    ]
    effective.setdefault("source_documents", []).extend(new_sources)
    _attach_new_source_documents_to_lineages(effective, new_sources)

    outcomes: list[RepairActionOutcomeV3] = []
    has_replacement = False
    for action in repair_delta.get("repair_actions") or ():
        candidate_id = str(action["candidate_id"])
        original = facts_before[candidate_id]
        collection = _collection_for_fact(effective, candidate_id)
        effective[collection] = [
            row
            for row in effective.get(collection) or ()
            if str(row.get("dossier_fact_id") or "") != candidate_id
        ]
        _remove_fact_from_lineages(effective, candidate_id)
        _move_prior_route_fact_to_rejected(effective, candidate_id)
        effective["derived_metrics"] = [
            row
            for row in effective.get("derived_metrics") or ()
            if candidate_id
            not in {str(value) for value in row.get("input_fact_ids") or ()}
        ]
        selected = str(action["action"])
        replacement = action.get("replacement_fact")
        replacement_id: str | None = None
        if isinstance(replacement, Mapping):
            has_replacement = True
            normalized_fact = _normalize_replacement_fact(replacement)
            replacement_id = str(normalized_fact["dossier_fact_id"])
            effective.setdefault(collection, []).append(normalized_fact)
            _attach_fact_to_lineage(effective, normalized_fact)
            _replace_question_fact_reference(
                effective,
                original_fact=original,
                old_candidate_id=candidate_id,
                replacement_candidate_id=replacement_id,
            )
            _mark_questions_repair_required(
                effective, action.get("question_family_ids") or ()
            )
        else:
            _replace_question_fact_reference(
                effective,
                original_fact=original,
                old_candidate_id=candidate_id,
                replacement_candidate_id=None,
            )
            _mark_questions_public(
                effective, action.get("question_family_ids") or ()
            )
        outcomes.append(
            RepairActionOutcomeV3(
                candidate_id=candidate_id,
                action=selected,
                replacement_candidate_id=replacement_id,
                question_family_ids=tuple(
                    str(value) for value in action.get("question_family_ids") or ()
                ),
                action_hash=canonical_hash(action),
            )
        )

    routes = [deepcopy(dict(row)) for row in repair_delta.get("new_route_receipts") or ()]
    effective.setdefault("search_route_receipts", []).extend(routes)
    _attach_routes_to_questions(effective, routes)
    effective.setdefault("research_passes", []).append(
        {
            "pass_id": compiled_prompt.research_pass_id,
            "parent_pass_id": compiled_prompt.parent_pass_id,
            "pass_name": "VERIFIER_REPAIR",
            "status": "COMPLETE",
            "prompt_hash": prompt_hash,
            "response_hash": response_hash,
        }
    )
    effective["research_pass_id"] = compiled_prompt.research_pass_id
    effective["parent_pass_id"] = compiled_prompt.parent_pass_id
    effective["research_status"] = (
        "NEEDS_VERIFIER_REPAIR" if has_replacement else "NEEDS_PUBLIC_GAP_CLOSURE"
    )

    validation_context = DossierValidationContext(
        job_id=str(effective.get("job_id") or ""),
        run_id=str(effective.get("run_id") or ""),
        target_id=str((effective.get("target") or {}).get("target_id") or ""),
        as_of_date=str(effective.get("as_of_date") or ""),
        conversation_id=str(effective.get("conversation_id") or ""),
        candidate_archetype_ids=tuple(
            str(value) for value in effective.get("candidate_archetypes") or ()
        ),
        research_pass_id=compiled_prompt.research_pass_id,
        parent_pass_id=compiled_prompt.parent_pass_id,
        enforce_parent_pass_id=True,
    )
    (dossier_validator or ResearchDossierValidator()).validate(
        effective,
        validation_context,
    )
    facts_after = _fact_map(effective)
    preserved = tuple(
        candidate_id
        for candidate_id in prior_accepted
        if candidate_id in facts_after
        and canonical_hash(facts_after[candidate_id]) == accepted_hashes[candidate_id]
    )
    if set(preserved) != set(prior_accepted):
        raise RepairDeltaV3ValidationError(
            "compact repair changed or deleted an accepted fact"
        )
    return RepairApplicationV3(
        effective_dossier=effective,
        outcomes=tuple(outcomes),
        prior_accepted_candidate_ids=prior_accepted,
        preserved_accepted_candidate_ids=preserved,
        prior_question_states=prior_question_states,
        delta_hash=canonical_hash(repair_delta),
        effective_dossier_hash=canonical_hash(effective),
        repair_pass_ordinal=repair_pass_ordinal,
    )


def _fact_map(dossier: Mapping[str, Any]) -> dict[str, Mapping[str, Any]]:
    return {
        str(row.get("dossier_fact_id") or ""): row
        for collection in _FACT_COLLECTIONS
        for row in dossier.get(collection) or ()
    }


def _collection_for_fact(dossier: Mapping[str, Any], candidate_id: str) -> str:
    matches = [
        collection
        for collection in _FACT_COLLECTIONS
        if any(
            str(row.get("dossier_fact_id") or "") == candidate_id
            for row in dossier.get(collection) or ()
        )
    ]
    if len(matches) != 1:
        raise RepairDeltaV3ValidationError(
            "repair candidate must occur in exactly one collection"
        )
    return matches[0]


def _normalize_new_source_document(row: Mapping[str, Any]) -> Mapping[str, Any]:
    normalized = deepcopy(dict(row))
    resolver = CanonicalURLResolver()
    for field in ("canonical_url", "opened_url"):
        normalized[field] = resolver.resolve(str(normalized.get(field) or "")).canonical_url
    text = TextQuoteNormalizer()
    for field in ("source_title", "locator_value"):
        normalized[field] = text.normalize_text(
            str(normalized.get(field) or "")
        ).normalized_text
    return normalized


def _normalize_replacement_fact(row: Mapping[str, Any]) -> Mapping[str, Any]:
    normalized = deepcopy(dict(row))
    text = TextQuoteNormalizer()
    for field in ("statement", "supporting_excerpt", "source_locator"):
        normalized[field] = text.normalize_text(
            str(normalized.get(field) or "")
        ).normalized_text
    return normalized


def _attach_new_source_documents_to_lineages(
    dossier: dict[str, Any], documents: Sequence[Mapping[str, Any]]
) -> None:
    lineages = dossier.setdefault("source_lineages", [])
    by_id = {str(row.get("lineage_id") or ""): row for row in lineages}
    for document in documents:
        lineage_id = str(document.get("lineage_id") or "")
        document_id = str(document.get("source_document_id") or "")
        lineage = by_id.get(lineage_id)
        if lineage is None:
            host = (urlsplit(str(document.get("canonical_url") or "")).hostname or "").casefold()
            publisher = str(document.get("source_publisher") or "").casefold()
            lineage = {
                "lineage_id": lineage_id,
                "source_document_ids": [],
                "fact_ids": [],
                "independence_group_id": stable_id(
                    "SLGROUP",
                    {"publisher": publisher, "host": host},
                ),
                "status": "ACTIVE",
            }
            lineages.append(lineage)
            by_id[lineage_id] = lineage
        lineage["source_document_ids"] = list(
            dict.fromkeys(
                (
                    *(str(value) for value in lineage.get("source_document_ids") or ()),
                    document_id,
                )
            )
        )


def _remove_fact_from_lineages(dossier: dict[str, Any], candidate_id: str) -> None:
    for lineage in dossier.get("source_lineages") or ():
        lineage["fact_ids"] = [
            str(value)
            for value in lineage.get("fact_ids") or ()
            if str(value) != candidate_id
        ]


def _attach_fact_to_lineage(dossier: dict[str, Any], fact: Mapping[str, Any]) -> None:
    source_id = str(fact.get("source_document_id") or "")
    source = next(
        (
            row
            for row in dossier.get("source_documents") or ()
            if str(row.get("source_document_id") or "") == source_id
        ),
        None,
    )
    if source is None:
        raise RepairDeltaV3ValidationError("replacement source document is absent")
    lineage_id = str(source.get("lineage_id") or "")
    lineage = next(
        (
            row
            for row in dossier.get("source_lineages") or ()
            if str(row.get("lineage_id") or "") == lineage_id
        ),
        None,
    )
    if lineage is None:
        raise RepairDeltaV3ValidationError("replacement source lineage is absent")
    lineage["fact_ids"] = list(
        dict.fromkeys(
            (
                *(str(value) for value in lineage.get("fact_ids") or ()),
                str(fact.get("dossier_fact_id") or ""),
            )
        )
    )


def _move_prior_route_fact_to_rejected(
    dossier: dict[str, Any], candidate_id: str
) -> None:
    for route in dossier.get("search_route_receipts") or ():
        accepted = [str(value) for value in route.get("accepted_fact_ids") or ()]
        if candidate_id not in accepted:
            continue
        route["accepted_fact_ids"] = [
            value for value in accepted if value != candidate_id
        ]
        route["rejected_candidate_ids"] = list(
            dict.fromkeys(
                (
                    *(
                        str(value)
                        for value in route.get("rejected_candidate_ids") or ()
                    ),
                    candidate_id,
                )
            )
        )


def _replace_question_fact_reference(
    dossier: dict[str, Any],
    *,
    original_fact: Mapping[str, Any],
    old_candidate_id: str,
    replacement_candidate_id: str | None,
) -> None:
    key = {
        "MATERIAL": "support_fact_ids",
        "COUNTER": "counter_fact_ids",
        "RESOLUTION": "resolution_fact_ids",
    }[str(original_fact.get("fact_kind") or "")]
    for question in dossier.get("question_family_results") or ():
        values = [str(value) for value in question.get(key) or ()]
        if old_candidate_id not in values:
            continue
        question[key] = [
            replacement_candidate_id if value == old_candidate_id else value
            for value in values
            if value != old_candidate_id or replacement_candidate_id is not None
        ]


def _mark_questions_repair_required(
    dossier: dict[str, Any], question_family_ids: Sequence[str]
) -> None:
    affected = {str(value) for value in question_family_ids}
    for question in dossier.get("question_family_results") or ():
        if str(question.get("question_family_id") or "") not in affected:
            continue
        question["status"] = "VERIFIER_REPAIR_REQUIRED"
        question["closure_reason"] = (
            "compact replacement awaits deterministic source reverification"
        )


def _mark_questions_public(
    dossier: dict[str, Any], question_family_ids: Sequence[str]
) -> None:
    affected = {str(value) for value in question_family_ids}
    for question in dossier.get("question_family_results") or ():
        if str(question.get("question_family_id") or "") not in affected:
            continue
        question["status"] = "PUBLIC_SEARCHABLE"
        question["availability_class"] = "PUBLIC_SEARCHABLE"
        question["adequate_search_proven"] = False
        question["closure_reason"] = (
            "rejected fact was withdrawn; public evidence gap reopened"
        )


def _attach_routes_to_questions(
    dossier: dict[str, Any], routes: Sequence[Mapping[str, Any]]
) -> None:
    by_question: dict[str, list[Mapping[str, Any]]] = {}
    for route in routes:
        by_question.setdefault(str(route.get("question_family_id") or ""), []).append(
            route
        )
    for question in dossier.get("question_family_results") or ():
        question_id = str(question.get("question_family_id") or "")
        scoped = by_question.get(question_id) or ()
        if not scoped:
            continue
        question["search_route_receipt_ids"] = list(
            dict.fromkeys(
                (
                    *(
                        str(value)
                        for value in question.get("search_route_receipt_ids") or ()
                    ),
                    *(str(row.get("route_receipt_id") or "") for row in scoped),
                )
            )
        )
        question["attempted_source_role_ids"] = list(
            dict.fromkeys(
                (
                    *(
                        str(value)
                        for value in question.get("attempted_source_role_ids") or ()
                    ),
                    *(str(row.get("source_role_id") or "") for row in scoped),
                )
            )
        )


def _find_forbidden_fields(value: Any, path: str = "$") -> tuple[str, ...]:
    found: list[str] = []
    if isinstance(value, Mapping):
        for key, child in value.items():
            next_path = f"{path}.{key}"
            if str(key).casefold() in _FORBIDDEN_AUTHORITY_FIELDS:
                found.append(next_path)
            found.extend(_find_forbidden_fields(child, next_path))
    elif isinstance(value, (list, tuple)):
        for index, child in enumerate(value):
            found.extend(_find_forbidden_fields(child, f"{path}[{index}]"))
    return tuple(found)


__all__ = [
    "RepairDeltaV3ValidationError",
    "RepairDeltaV3Validator",
    "apply_repair_delta_v3",
]
