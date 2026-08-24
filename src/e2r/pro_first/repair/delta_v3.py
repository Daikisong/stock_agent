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
                "fetched_excerpt": prompt_candidate.get("fetched_excerpt"),
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
