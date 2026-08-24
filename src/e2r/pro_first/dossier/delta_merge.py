"""Append-only merge of same-conversation ResearchDossierV2 follow-up deltas."""

from __future__ import annotations

from copy import deepcopy
from dataclasses import dataclass
from typing import Any, Mapping, Sequence

from ..ids import canonical_hash
from .validator import DossierValidationContext, ResearchDossierValidator


class DossierDeltaMergeError(ValueError):
    """A follow-up attempted to rewrite accepted dossier history or scope."""


@dataclass(frozen=True)
class DossierDeltaMergeResult:
    effective_dossier: Mapping[str, Any]
    original_hash: str
    response_hash: str
    effective_hash: str
    new_fact_ids: tuple[str, ...]
    new_source_lineage_ids: tuple[str, ...]
    new_route_receipt_ids: tuple[str, ...]
    updated_question_family_ids: tuple[str, ...]


def apply_research_dossier_delta(
    *,
    original_dossier: Mapping[str, Any],
    response_dossier: Mapping[str, Any],
    validation_context: DossierValidationContext,
) -> DossierDeltaMergeResult:
    """Accept cumulative or delta-shaped V2 responses under one strict rule.

    Existing fact/lineage/route/pass rows are immutable.  A follow-up may add
    rows and may advance its question closure row, but it cannot delete prior
    fact/route links.  The resulting full ledger is then validated as ordinary
    ResearchDossierV2 before it can reach verification or saturation.
    """

    _validate_scope_identity(original_dossier, response_dossier, validation_context)
    effective = deepcopy(dict(original_dossier))
    new_fact_ids: list[str] = []
    for collection in ("material_facts", "counterfacts", "resolution_facts"):
        new_fact_ids.extend(
            _append_immutable_rows(
                effective,
                response_dossier,
                collection=collection,
                id_key="dossier_fact_id",
                required_new_pass_id=validation_context.research_pass_id,
            )
        )
    new_lineages = _merge_source_lineages(effective, response_dossier)
    new_routes = _append_immutable_rows(
        effective,
        response_dossier,
        collection="search_route_receipts",
        id_key="route_receipt_id",
        required_new_pass_id=validation_context.research_pass_id,
    )
    _append_immutable_rows(
        effective,
        response_dossier,
        collection="research_passes",
        id_key="pass_id",
    )
    updated_questions = _merge_question_results(effective, response_dossier)
    _merge_gap_state(effective, response_dossier)
    _append_repair_register(effective, response_dossier)

    for key in (
        "research_pass_id",
        "parent_pass_id",
        "research_status",
        "research_saturation",
    ):
        effective[key] = deepcopy(response_dossier.get(key))
    for key in ("component_research", "structured_metrics"):
        incoming = response_dossier.get(key)
        if isinstance(incoming, Mapping):
            current = dict(effective.get(key) or {})
            current.update(deepcopy(dict(incoming)))
            effective[key] = current
    effective["proposed_score_ranges"] = []
    effective["score_authority"] = False
    effective["stage_authority"] = False
    try:
        ResearchDossierValidator().validate(effective, validation_context)
    except Exception as error:
        raise DossierDeltaMergeError(
            f"merged ResearchDossierV2 failed strict validation: {error}"
        ) from error
    return DossierDeltaMergeResult(
        effective_dossier=effective,
        original_hash=canonical_hash(original_dossier),
        response_hash=canonical_hash(response_dossier),
        effective_hash=canonical_hash(effective),
        new_fact_ids=tuple(new_fact_ids),
        new_source_lineage_ids=tuple(new_lineages),
        new_route_receipt_ids=tuple(new_routes),
        updated_question_family_ids=tuple(updated_questions),
    )


def _validate_scope_identity(
    original: Mapping[str, Any],
    response: Mapping[str, Any],
    context: DossierValidationContext,
) -> None:
    if (
        original.get("schema_version") != "e2r_pro_research_dossier_v2"
        or response.get("schema_version") != "e2r_pro_research_dossier_v2"
    ):
        raise DossierDeltaMergeError("follow-up merge requires two V2 dossiers")
    for key in ("job_id", "run_id", "conversation_id", "as_of_date"):
        if response.get(key) != original.get(key):
            raise DossierDeltaMergeError(f"follow-up changed immutable scope field: {key}")
    original_target = original.get("target") or {}
    response_target = response.get("target") or {}
    for key in ("target_id", "symbol", "company_name"):
        before = original_target.get(key)
        after = response_target.get(key)
        if before is not None and after != before:
            raise DossierDeltaMergeError(f"follow-up changed immutable target field: {key}")
    for key in ("candidate_archetypes", "selected_archetypes"):
        # A delta-shaped follow-up must carry the required schema arrays, but
        # an empty array means "no scope update".  A non-empty roster still has
        # to match exactly, so a follow-up cannot select a new mechanism.
        incoming = set(str(value) for value in response.get(key) or ())
        if incoming and incoming != set(
            str(value) for value in original.get(key) or ()
        ):
            raise DossierDeltaMergeError(f"follow-up changed contract scope: {key}")
    if response.get("score_authority") is not False or response.get(
        "stage_authority"
    ) is not False:
        raise DossierDeltaMergeError("follow-up dossier cannot own score or Stage")
    if (
        context.research_pass_id
        and response.get("research_pass_id") != context.research_pass_id
    ):
        raise DossierDeltaMergeError("follow-up response belongs to another pass")
    if (
        context.enforce_parent_pass_id
        and response.get("parent_pass_id") != context.parent_pass_id
    ):
        raise DossierDeltaMergeError("follow-up response has wrong parent lineage")


def _append_immutable_rows(
    effective: dict[str, Any],
    response: Mapping[str, Any],
    *,
    collection: str,
    id_key: str,
    required_new_pass_id: str | None = None,
) -> tuple[str, ...]:
    rows = list(effective.get(collection) or ())
    existing = {str(row.get(id_key) or ""): row for row in rows}
    if len(existing) != len(rows):
        raise DossierDeltaMergeError(f"original {collection} contains duplicate ids")
    added: list[str] = []
    for incoming in response.get(collection) or ():
        identity = str(incoming.get(id_key) or "")
        if not identity:
            raise DossierDeltaMergeError(f"follow-up {collection} row lacks {id_key}")
        prior = existing.get(identity)
        if prior is not None:
            if canonical_hash(prior) != canonical_hash(incoming):
                # The current pass receipt is capture-bound transport metadata;
                # the bound row may safely replace Pro's non-authoritative row.
                if collection == "research_passes" and identity == required_new_pass_id:
                    rows[rows.index(prior)] = deepcopy(dict(incoming))
                    existing[identity] = rows[rows.index(prior)]
                    continue
                raise DossierDeltaMergeError(
                    f"follow-up rewrote immutable {collection} row: {identity}"
                )
            continue
        if required_new_pass_id is not None and str(
            incoming.get("research_pass_id")
            if collection.endswith("facts")
            else incoming.get("pass_id")
            or ""
        ) != required_new_pass_id:
            raise DossierDeltaMergeError(
                f"new {collection} row is detached from the current pass"
            )
        copied = deepcopy(dict(incoming))
        rows.append(copied)
        existing[identity] = copied
        added.append(identity)
    effective[collection] = rows
    return tuple(added)


_LINEAGE_UNION_FIELDS = frozenset(
    {
        "source_urls",
        "canonical_source_urls",
        "fact_ids",
        "publisher_roster",
        "same_fact_reprints_collapsed",
        "existing_fact_ids_referenced",
    }
)
_LINEAGE_IDENTITY_FIELDS = frozenset(
    {
        "source_lineage_id",
        "independence_group_id",
        "lineage_subject",
        "status",
    }
)
_LINEAGE_CURRENT_STATE_FIELDS = frozenset(
    {"lineage_status", "lineage_operation"}
)


def _merge_source_lineages(
    effective: dict[str, Any], response: Mapping[str, Any]
) -> tuple[str, ...]:
    """Append evidence to an existing lineage without rewriting its identity.

    A later pass often finds a newer document in an already known publisher or
    event lineage.  The lineage entity therefore keeps immutable identity
    fields while URL/fact/publisher rosters grow monotonically.  Current-state
    diagnostics retain an explicit value history before advancing.
    """

    rows = list(effective.get("source_lineages") or ())
    index = {
        str(row.get("source_lineage_id") or ""): position
        for position, row in enumerate(rows)
    }
    if len(index) != len(rows):
        raise DossierDeltaMergeError(
            "original source_lineages contains duplicate ids"
        )
    added: list[str] = []
    for incoming_raw in response.get("source_lineages") or ():
        if not isinstance(incoming_raw, Mapping):
            raise DossierDeltaMergeError(
                "follow-up source lineage row must be an object"
            )
        incoming = deepcopy(dict(incoming_raw))
        lineage_id = str(incoming.get("source_lineage_id") or "")
        if not lineage_id:
            raise DossierDeltaMergeError(
                "follow-up source lineage lacks source_lineage_id"
            )
        if lineage_id not in index:
            index[lineage_id] = len(rows)
            rows.append(incoming)
            added.append(lineage_id)
            continue

        prior = deepcopy(dict(rows[index[lineage_id]]))
        for key in _LINEAGE_IDENTITY_FIELDS:
            before = prior.get(key)
            after = incoming.get(key)
            if before is not None and after is not None and before != after:
                raise DossierDeltaMergeError(
                    f"follow-up rewrote source lineage identity: {lineage_id}.{key}"
                )
        merged = deepcopy(prior)
        for key in _LINEAGE_UNION_FIELDS:
            merged[key] = list(
                dict.fromkeys(
                    str(value)
                    for value in (
                        *(prior.get(key) or ()),
                        *(incoming.get(key) or ()),
                    )
                    if str(value)
                )
            )
        for key in _LINEAGE_CURRENT_STATE_FIELDS:
            before = prior.get(key)
            after = incoming.get(key)
            history_key = f"{key}_history"
            merged[history_key] = list(
                dict.fromkeys(
                    str(value)
                    for value in (
                        *(prior.get(history_key) or ()),
                        before,
                        after,
                    )
                    if value is not None and str(value)
                )
            )
            if after is not None:
                merged[key] = deepcopy(after)
        handled = (
            _LINEAGE_UNION_FIELDS
            | _LINEAGE_IDENTITY_FIELDS
            | _LINEAGE_CURRENT_STATE_FIELDS
            | {f"{key}_history" for key in _LINEAGE_CURRENT_STATE_FIELDS}
        )
        for key, value in incoming.items():
            if key in handled:
                continue
            if key not in merged:
                merged[key] = deepcopy(value)
                continue
            if canonical_hash(merged[key]) != canonical_hash(value):
                raise DossierDeltaMergeError(
                    f"follow-up rewrote source lineage metadata: {lineage_id}.{key}"
                )
        rows[index[lineage_id]] = merged
    effective["source_lineages"] = rows
    return tuple(added)


def _merge_question_results(
    effective: dict[str, Any], response: Mapping[str, Any]
) -> tuple[str, ...]:
    rows = list(effective.get("question_family_results") or ())
    index = {
        str(row.get("question_family_id") or ""): position
        for position, row in enumerate(rows)
    }
    if len(index) != len(rows):
        raise DossierDeltaMergeError("original question results contain duplicate ids")
    updated: list[str] = []
    cumulative_keys = (
        "support_fact_ids",
        "counter_fact_ids",
        "resolution_fact_ids",
        "attempted_source_role_ids",
        "search_route_receipt_ids",
    )
    for incoming in response.get("question_family_results") or ():
        question_id = str(incoming.get("question_family_id") or "")
        if not question_id:
            raise DossierDeltaMergeError("follow-up question result lacks identity")
        if question_id in index:
            prior = rows[index[question_id]]
            merged = deepcopy(dict(incoming))
            for key in cumulative_keys:
                # Follow-up output may be cumulative or a true delta.  Unioning
                # the immutable prior links with incoming links supports both
                # shapes and makes deletion impossible by construction.
                merged[key] = list(
                    dict.fromkeys(
                        str(value)
                        for value in (
                            *(prior.get(key) or ()),
                            *(incoming.get(key) or ()),
                        )
                        if str(value)
                    )
                )
            rows[index[question_id]] = merged
        else:
            index[question_id] = len(rows)
            rows.append(deepcopy(dict(incoming)))
        updated.append(question_id)
    effective["question_family_results"] = rows
    return tuple(dict.fromkeys(updated))


def _merge_gap_state(effective: dict[str, Any], response: Mapping[str, Any]) -> None:
    rows = list(effective.get("unresolved_gaps") or ())
    index = {
        str(row.get("stable_gap_key") or row.get("gap_id") or ""): position
        for position, row in enumerate(rows)
    }
    for incoming in response.get("unresolved_gaps") or ():
        key = str(incoming.get("stable_gap_key") or incoming.get("gap_id") or "")
        if not key:
            raise DossierDeltaMergeError("follow-up gap lacks stable identity")
        if key in index:
            rows[index[key]] = deepcopy(dict(incoming))
        else:
            index[key] = len(rows)
            rows.append(deepcopy(dict(incoming)))
    effective["unresolved_gaps"] = rows


def _append_repair_register(
    effective: dict[str, Any], response: Mapping[str, Any]
) -> None:
    rows = list(effective.get("verification_repair_register") or ())
    identities = {
        (str(row.get("candidate_id") or ""), str(row.get("question_family_id") or ""))
        for row in rows
    }
    for incoming in response.get("verification_repair_register") or ():
        identity = (
            str(incoming.get("candidate_id") or ""),
            str(incoming.get("question_family_id") or ""),
        )
        if identity not in identities:
            rows.append(deepcopy(dict(incoming)))
            identities.add(identity)
    effective["verification_repair_register"] = rows


__all__ = [
    "DossierDeltaMergeError",
    "DossierDeltaMergeResult",
    "apply_research_dossier_delta",
]
