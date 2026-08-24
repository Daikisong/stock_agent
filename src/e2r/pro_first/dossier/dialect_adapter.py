"""Fail-closed migration of known Pro output dialects into ResearchDossierV1.

The raw browser capture remains immutable.  This adapter only changes
allowlisted structural labels and identifiers before strict schema validation;
research statements, excerpts, URLs, values, dates, and scope fields are
protected byte-for-byte at the parsed-value level.
"""

from __future__ import annotations

from copy import deepcopy
from dataclasses import dataclass
import re
from typing import Any, Mapping

from ..ids import canonical_hash
from .delta_merge import SOURCE_LINEAGE_IDENTITY_FIELDS


_CANONICAL_DIRECTIONS = frozenset(
    {"POSITIVE", "COUNTER", "NEGATIVE", "NEUTRAL", "RESOLUTION"}
)
_CANONICAL_LIFECYCLES = frozenset(
    {"CURRENT", "OPEN", "RESOLVED", "SUPERSEDED", "HISTORICAL", "UNKNOWN"}
)
_CANONICAL_GAP_CLASSES = frozenset(
    {
        "CORE_SCORE_BLOCKER",
        "STAGE_BOUNDARY_GAP",
        "HARD_BREAK_GAP",
        "CORROBORATION_CAP",
        "MONITORING_GAP",
    }
)
_CANONICAL_SOURCE_ROLES = frozenset(
    {"CORE_SCORE_SOURCE", "INDEPENDENT_CORROBORATION", "MONITORING_ONLY"}
)
_LEGACY_FACT_ID = re.compile(r"^(?:MF|CF)-[A-Za-z0-9._:-]+$")
_LEGACY_GAP_ID = re.compile(r"^GAP-[A-Za-z0-9._:-]+$")
_COMPACT_V2_FACT_ID = re.compile(
    r"^(?:PROFACT-)?(?:MF|CF|RF)[A-Za-z0-9._:-]+$"
)
_SCOPED_REPAIR_ACTIONS = frozenset(
    {"CORRECTED", "REPLACED", "NARROWED", "WITHDRAWN"}
)
_SCOPED_REJECTION_CATEGORIES = frozenset(
    {
        "QUOTE_MISMATCH",
        "WRONG_SUBJECT",
        "WRONG_TARGET",
        "WRONG_SEGMENT",
        "WRONG_PRODUCT",
        "FUTURE_SOURCE",
        "SNIPPET_ONLY",
        "SOURCE_UNAVAILABLE",
        "DATE_UNRESOLVED",
        "DUPLICATE_LINEAGE",
        "UNSUPPORTED_DERIVATION",
    }
)

# Qualitative bands are converted to fixed conservative band midpoints.  This
# is a format policy, not a score or Stage decision, and remains subordinate to
# source verification and the deterministic scorer.
_CONFIDENCE_BAND_MIDPOINTS = {
    "VERY_HIGH": 0.95,
    "HIGH": 0.85,
    "MEDIUM_HIGH": 0.75,
    "MEDIUM": 0.50,
    "MEDIUM_LOW": 0.35,
    "LOW": 0.20,
    "VERY_LOW": 0.05,
}

_PROTECTED_FACT_FIELDS = (
    "statement",
    "subject",
    "target_id",
    "issuer_scoped",
    "business_segment",
    "product_family",
    "economic_mechanism",
    "predicate",
    "value",
    "unit",
    "period",
    "event_date",
    "candidate_components",
    "source_url",
    "source_title",
    "source_publisher",
    "published_at",
    "supporting_excerpt",
)
_CANONICAL_V2_FACT_REQUIRED_FIELDS = frozenset(
    {
        "dossier_fact_id",
        "research_pass_id",
        "source_lineage_id",
        "question_family_ids",
        "statement",
        "direction",
        "subject",
        "target_id",
        "issuer_scoped",
        "business_segment",
        "product_family",
        "economic_mechanism",
        "predicate",
        "value",
        "unit",
        "period",
        "event_date",
        "current_status",
        "candidate_components",
        "source_url",
        "source_title",
        "source_publisher",
        "published_at",
        "supporting_excerpt",
        "confidence",
    }
)


class DossierDialectError(ValueError):
    """The parsed dossier uses a dialect outside the explicit allowlist."""


@dataclass(frozen=True)
class AdaptedDossier:
    payload: Mapping[str, Any]
    before_hash: str
    after_hash: str
    operations: tuple[str, ...]
    id_map: Mapping[str, str]


class ResearchDossierDialectAdapter:
    """Convert known ChatGPT Pro formatting variants without inventing facts."""

    def adapt(
        self,
        payload: Mapping[str, Any],
        *,
        prior_dossier: Mapping[str, Any] | None = None,
    ) -> AdaptedDossier:
        before_hash = canonical_hash(payload)
        adapted = deepcopy(dict(payload))
        if adapted.get("schema_version") == "e2r_pro_research_dossier_v2":
            if _is_canonical_v2(adapted):
                operations = ["V2_CANONICAL_DIALECT_NO_LEGACY_REWRITE"]
                if prior_dossier is not None:
                    adapted, scope_operations = (
                        _project_canonical_followup_contract_scope(
                            adapted,
                            prior_dossier=prior_dossier,
                        )
                    )
                    operations.extend(scope_operations)
                    adapted, lineage_operations = (
                        _project_existing_followup_lineage_identity(
                            adapted,
                            prior_dossier=prior_dossier,
                        )
                    )
                    operations.extend(lineage_operations)
                return AdaptedDossier(
                    payload=adapted,
                    before_hash=before_hash,
                    after_hash=canonical_hash(adapted),
                    operations=tuple(operations),
                    id_map={},
                )
            compact = _adapt_compact_v2(
                adapted,
                prior_dossier=prior_dossier,
            )
            compact_payload = dict(compact.payload)
            compact_operations = list(compact.operations)
            if prior_dossier is not None:
                compact_payload, scope_operations = (
                    _project_canonical_followup_contract_scope(
                        compact_payload,
                        prior_dossier=prior_dossier,
                    )
                )
                compact_operations.extend(scope_operations)
                compact_payload, lineage_operations = (
                    _project_existing_followup_lineage_identity(
                        compact_payload,
                        prior_dossier=prior_dossier,
                    )
                )
                compact_operations.extend(lineage_operations)
            return AdaptedDossier(
                payload=compact_payload,
                before_hash=before_hash,
                after_hash=canonical_hash(compact_payload),
                operations=tuple(compact_operations),
                id_map=compact.id_map,
            )
        protected_before = _protected_fact_values(adapted)
        fact_count_before = _fact_count(adapted)
        operations: list[str] = []

        id_map = self._build_id_map(adapted)
        if id_map:
            adapted = _rewrite_exact_identifiers(adapted, id_map)
            fact_mappings = sum(key.startswith(("MF-", "CF-")) for key in id_map)
            gap_mappings = sum(key.startswith("GAP-") for key in id_map)
            if fact_mappings:
                operations.append(f"MAP_LEGACY_FACT_IDS:{fact_mappings}")
            if gap_mappings:
                operations.append(f"MAP_LEGACY_GAP_IDS:{gap_mappings}")

        candidates = adapted.get("candidate_archetypes") or []
        if not isinstance(candidates, list):
            raise DossierDialectError("candidate_archetypes must be an array")
        candidate_ids: list[str] = []
        object_count = 0
        for row in candidates:
            if isinstance(row, str):
                candidate_id = row.strip()
            elif isinstance(row, Mapping):
                object_count += 1
                candidate_id = str(row.get("archetype_id") or "").strip()
            else:
                raise DossierDialectError(
                    "candidate_archetypes items must be strings or known objects"
                )
            if not candidate_id:
                raise DossierDialectError("candidate archetype id is empty")
            candidate_ids.append(candidate_id)
        if len(candidate_ids) != len(set(candidate_ids)):
            raise DossierDialectError("candidate archetype ids must be unique")
        adapted["candidate_archetypes"] = candidate_ids
        if object_count:
            operations.append(f"PROJECT_CANDIDATE_ARCHETYPE_OBJECTS_TO_IDS:{object_count}")

        facts = tuple(adapted.get("material_facts") or ()) + tuple(
            adapted.get("counterfacts") or ()
        )
        direction_count = confidence_count = lifecycle_count = 0
        for fact in facts:
            if not isinstance(fact, dict):
                raise DossierDialectError("fact rows must be objects")
            direction = str(fact.get("direction") or "")
            if direction not in _CANONICAL_DIRECTIONS:
                canonical_direction = direction.upper()
                if canonical_direction not in _CANONICAL_DIRECTIONS:
                    raise DossierDialectError(f"unsupported fact direction: {direction!r}")
                fact["direction"] = canonical_direction
                direction_count += 1

            confidence = fact.get("confidence")
            if isinstance(confidence, str):
                label = confidence.strip().upper().replace("-", "_").replace(" ", "_")
                if label not in _CONFIDENCE_BAND_MIDPOINTS:
                    raise DossierDialectError(
                        f"unsupported qualitative confidence: {confidence!r}"
                    )
                fact["confidence"] = _CONFIDENCE_BAND_MIDPOINTS[label]
                confidence_count += 1

            lifecycle = str(fact.get("current_status") or "")
            if lifecycle not in _CANONICAL_LIFECYCLES:
                fact["current_status"] = _canonical_lifecycle(lifecycle)
                lifecycle_count += 1
        if direction_count:
            operations.append(f"UPPERCASE_FACT_DIRECTIONS:{direction_count}")
        if confidence_count:
            operations.append(f"MAP_CONFIDENCE_BANDS_TO_MIDPOINTS:{confidence_count}")
        if lifecycle_count:
            operations.append(f"MAP_DETAILED_LIFECYCLES:{lifecycle_count}")

        gap_class_count = source_role_count = 0
        for gap in adapted.get("unresolved_gaps") or ():
            if not isinstance(gap, dict):
                raise DossierDialectError("unresolved gap rows must be objects")
            original_class = str(gap.get("proposed_gap_class") or "")
            if original_class not in _CANONICAL_GAP_CLASSES:
                gap["proposed_gap_class"] = _canonical_gap_class(
                    original_class,
                    could_change_score=gap.get("proposed_could_change_score") is True,
                    could_change_stage=gap.get("proposed_could_change_stage") is True,
                    could_change_hard_break=(
                        gap.get("proposed_could_change_hard_break") is True
                    ),
                )
                gap_class_count += 1
            original_role = str(gap.get("proposed_missing_source_role") or "")
            if original_role not in _CANONICAL_SOURCE_ROLES:
                if not re.fullmatch(r"[A-Z][A-Z0-9_]*", original_role):
                    raise DossierDialectError(
                        f"unsupported proposed missing source role: {original_role!r}"
                    )
                gap["proposed_missing_source_role"] = (
                    "MONITORING_ONLY"
                    if original_class == "EXPLICIT_UNKNOWN"
                    else "CORE_SCORE_SOURCE"
                )
                source_role_count += 1
        if gap_class_count:
            operations.append(f"MAP_PROPOSED_GAP_CLASSES:{gap_class_count}")
        if source_role_count:
            operations.append(f"MAP_PROPOSED_SOURCE_ROLES:{source_role_count}")

        proposed_ranges = adapted.get("proposed_score_ranges")
        if isinstance(proposed_ranges, list):
            if proposed_ranges:
                raise DossierDialectError(
                    "non-empty list proposed_score_ranges cannot be migrated safely"
                )
            adapted["proposed_score_ranges"] = {}
            operations.append("MAP_EMPTY_SCORE_RANGE_ARRAY_TO_OBJECT")

        if _fact_count(adapted) != fact_count_before:
            raise DossierDialectError("dialect adaptation cannot create or delete facts")
        if _protected_fact_values(adapted) != protected_before:
            raise DossierDialectError("dialect adaptation changed protected fact evidence")
        remaining = sorted(_legacy_identifier_strings(adapted))
        if remaining:
            raise DossierDialectError(
                f"unmapped legacy dossier identifiers remain: {remaining}"
            )
        return AdaptedDossier(
            payload=adapted,
            before_hash=before_hash,
            after_hash=canonical_hash(adapted),
            operations=tuple(operations),
            id_map=dict(sorted(id_map.items())),
        )

    @staticmethod
    def _build_id_map(payload: Mapping[str, Any]) -> dict[str, str]:
        id_map: dict[str, str] = {}
        for fact in tuple(payload.get("material_facts") or ()) + tuple(
            payload.get("counterfacts") or ()
        ):
            if not isinstance(fact, Mapping):
                continue
            fact_id = str(fact.get("dossier_fact_id") or "")
            if fact_id.startswith("PROFACT-"):
                continue
            if not _LEGACY_FACT_ID.fullmatch(fact_id):
                raise DossierDialectError(f"unsupported dossier fact id: {fact_id!r}")
            id_map[fact_id] = f"PROFACT-{fact_id}"
        for gap in payload.get("unresolved_gaps") or ():
            if not isinstance(gap, Mapping):
                continue
            gap_id = str(gap.get("dossier_gap_id") or "")
            if gap_id.startswith("PROGAP-"):
                continue
            if not _LEGACY_GAP_ID.fullmatch(gap_id):
                raise DossierDialectError(f"unsupported dossier gap id: {gap_id!r}")
            id_map[gap_id] = f"PROGAP-{gap_id}"
        if len(set(id_map.values())) != len(id_map):
            raise DossierDialectError("legacy id mapping would create a collision")
        return id_map


@dataclass(frozen=True)
class _CompactV2Adaptation:
    payload: Mapping[str, Any]
    operations: tuple[str, ...]
    id_map: Mapping[str, str]


def _project_canonical_followup_contract_scope(
    payload: Mapping[str, Any],
    *,
    prior_dossier: Mapping[str, Any],
) -> tuple[dict[str, Any], tuple[str, ...]]:
    """Keep deterministic contract selection immutable across follow-ups.

    A Pro follow-up may repeat the compiled R13 cross guards in its selected
    roster.  Those guards remain diagnostics/questions; they cannot expand the
    job's primary selected-archetype scope.
    """

    _validate_prior_dossier_scope(payload, prior_dossier)
    adapted = deepcopy(dict(payload))
    prior_candidates = tuple(
        str(value) for value in prior_dossier.get("candidate_archetypes") or ()
    )
    prior_selected = tuple(
        str(value) for value in prior_dossier.get("selected_archetypes") or ()
    )
    allowed_contracts = {
        *prior_candidates,
        *prior_selected,
        *(
            str(row.get("archetype_id") or "")
            for row in prior_dossier.get("question_family_results") or ()
            if isinstance(row, Mapping)
        ),
    }
    allowed_contracts.discard("")
    reported_candidates = tuple(
        str(value) for value in adapted.get("candidate_archetypes") or ()
    )
    reported_selected = tuple(
        str(value) for value in adapted.get("selected_archetypes") or ()
    )
    unknown = (set(reported_candidates) | set(reported_selected)) - allowed_contracts
    if unknown:
        raise DossierDialectError(
            "canonical follow-up introduced an uncompiled contract: "
            + ",".join(sorted(unknown))
        )
    if reported_selected and not set(prior_selected).issubset(reported_selected):
        raise DossierDialectError(
            "canonical follow-up omitted the immutable selected archetype"
        )
    reported_cross_guards = tuple(
        value for value in reported_selected if value not in set(prior_selected)
    )
    adapted["candidate_archetypes"] = list(prior_candidates)
    adapted["selected_archetypes"] = list(prior_selected)
    saturation = dict(adapted.get("research_saturation") or {})
    saturation["pro_reported_canonical_followup_candidates"] = list(
        reported_candidates
    )
    saturation["pro_reported_canonical_followup_selected"] = list(
        reported_selected
    )
    saturation["pro_reported_canonical_followup_cross_guards"] = list(
        reported_cross_guards
    )
    adapted["research_saturation"] = saturation
    return adapted, (
        "PROJECT_CANONICAL_FOLLOWUP_TO_IMMUTABLE_CONTRACT_SCOPE",
        (
            "PRESERVE_PRO_REPORTED_CANONICAL_CROSS_GUARDS_AS_DIAGNOSTIC:"
            f"{len(reported_cross_guards)}"
        ),
    )


def _project_existing_followup_lineage_identity(
    payload: Mapping[str, Any],
    *,
    prior_dossier: Mapping[str, Any],
) -> tuple[dict[str, Any], tuple[str, ...]]:
    """Project repeated lineage labels onto their immutable prior identity.

    Pro may describe the same lineage more narrowly in a follow-up, for
    example changing ``SK hynix earnings cycle`` to ``SK hynix 2Q26
    earnings``.  The raw capture preserves that wording, while the effective
    append-only dossier keeps the original entity identity and accepts only
    the new URL/fact/current-state evidence through the delta merger.
    """

    _validate_prior_dossier_scope(payload, prior_dossier)
    adapted = deepcopy(dict(payload))
    prior_by_id = {
        str(row.get("source_lineage_id") or ""): row
        for row in prior_dossier.get("source_lineages") or ()
        if isinstance(row, Mapping)
    }
    restatements: list[dict[str, Any]] = []
    projected_rows: list[Any] = []
    for raw_row in adapted.get("source_lineages") or ():
        if not isinstance(raw_row, Mapping):
            projected_rows.append(raw_row)
            continue
        row = deepcopy(dict(raw_row))
        lineage_id = str(row.get("source_lineage_id") or "")
        prior = prior_by_id.get(lineage_id)
        changed_fields: list[str] = []
        if prior is not None:
            for key in sorted(SOURCE_LINEAGE_IDENTITY_FIELDS):
                if key not in prior:
                    continue
                if key in row and canonical_hash(row[key]) != canonical_hash(prior[key]):
                    changed_fields.append(key)
                row[key] = deepcopy(prior[key])
        if changed_fields:
            restatements.append(
                {
                    "source_lineage_id": lineage_id,
                    "projected_identity_fields": changed_fields,
                }
            )
        projected_rows.append(row)
    adapted["source_lineages"] = projected_rows
    saturation = dict(adapted.get("research_saturation") or {})
    saturation["pro_reported_source_lineage_identity_restatements"] = restatements
    adapted["research_saturation"] = saturation
    return adapted, (
        "PROJECT_REPEATED_SOURCE_LINEAGES_TO_IMMUTABLE_PRIOR_IDENTITY:"
        f"{len(restatements)}",
    )


def _is_canonical_v2(payload: Mapping[str, Any]) -> bool:
    facts = tuple(
        row
        for collection in ("material_facts", "counterfacts", "resolution_facts")
        for row in payload.get(collection) or ()
    )
    return bool(
        all(
            isinstance(row, Mapping)
            and str(row.get("dossier_fact_id") or "").startswith("PROFACT-")
            and _CANONICAL_V2_FACT_REQUIRED_FIELDS.issubset(row)
            for row in facts
        )
        and all(isinstance(value, str) for value in payload.get("candidate_archetypes") or ())
        and all(isinstance(value, str) for value in payload.get("selected_archetypes") or ())
        and isinstance(payload.get("component_research"), Mapping)
        and all(
            "query_or_navigation_objective" in row
            and "opened_source_urls" in row
            for row in payload.get("search_route_receipts") or ()
            if isinstance(row, Mapping)
        )
    )


def _adapt_compact_v2(
    payload: Mapping[str, Any],
    *,
    prior_dossier: Mapping[str, Any] | None = None,
) -> _CompactV2Adaptation:
    """Project the visible Pro V2 field dialect without changing raw evidence.

    The compact dialect uses source facts plus counter/resolution relationship
    rows.  Canonical verification still requires one fact-shaped row per
    relationship, so each relationship is bound to its explicitly declared
    first source fact.  This does not make it accepted evidence: the normal
    full-document quote verifier must still accept it or open verifier repair.
    """

    adapted = deepcopy(dict(payload))
    material_rows = adapted.get("material_facts") or []
    counter_rows = adapted.get("counterfacts") or []
    resolution_rows = adapted.get("resolution_facts") or []
    if not all(isinstance(rows, list) for rows in (material_rows, counter_rows, resolution_rows)):
        raise DossierDialectError("compact V2 fact collections must be arrays")
    projected_repair_source_identity_count = (
        _project_compact_repair_source_identity(
            adapted,
            prior_dossier=prior_dossier,
        )
    )
    raw_fact_ids: list[str] = []
    for collection, id_key in (
        (material_rows, "fact_id"),
        (counter_rows, "counterfact_id"),
        (resolution_rows, "resolution_fact_id"),
    ):
        for row in collection:
            if not isinstance(row, Mapping):
                raise DossierDialectError("compact V2 fact rows must be objects")
            fact_id = _compact_input_fact_id(row, id_key=id_key)
            if not _COMPACT_V2_FACT_ID.fullmatch(fact_id):
                raise DossierDialectError(
                    f"unsupported compact V2 fact id: {fact_id!r}"
                )
            raw_fact_ids.append(fact_id)
    if len(raw_fact_ids) != len(set(raw_fact_ids)):
        raise DossierDialectError("compact V2 fact ids must be unique")
    referenced_fact_ids = _compact_fact_reference_ids(adapted)
    id_map = {
        value: _canonical_compact_fact_id(value)
        for value in dict.fromkeys((*raw_fact_ids, *referenced_fact_ids))
        if value != _canonical_compact_fact_id(value)
    }
    prior_material_by_id = _prior_compact_source_fact_index(
        payload,
        prior_dossier=prior_dossier,
    )
    material_by_id = {
        **prior_material_by_id,
        **{
            _compact_input_fact_id(row, id_key="fact_id"): row
            for row in material_rows
        },
    }
    target = adapted.get("target") or {}
    target_id = str(target.get("target_id") or target.get("symbol") or "")
    company_name = str(target.get("company_name") or "")
    research_pass_id = str(adapted.get("research_pass_id") or "")
    if not target_id or not research_pass_id:
        raise DossierDialectError("compact V2 target and research pass are required")
    adapted["target"] = {**dict(target), "target_id": target_id}

    question_rows = tuple(adapted.get("question_family_results") or ())
    questions_by_id = {
        str(row.get("question_family_id") or ""): row
        for row in question_rows
        if isinstance(row, Mapping)
    }
    question_refs: dict[str, list[str]] = {value: [] for value in raw_fact_ids}
    component_refs: dict[str, list[str]] = {value: [] for value in raw_fact_ids}
    for row in question_rows:
        if not isinstance(row, Mapping):
            raise DossierDialectError("compact V2 question rows must be objects")
        question_id = str(row.get("question_family_id") or "")
        for key in ("support_fact_ids", "counter_fact_ids", "resolution_fact_ids"):
            for fact_id in row.get(key) or ():
                if str(fact_id) in question_refs:
                    question_refs[str(fact_id)].append(question_id)
                    component_refs[str(fact_id)].extend(
                        str(value) for value in row.get("affected_component_ids") or ()
                    )
    components = adapted.get("component_research") or []
    if not isinstance(components, (list, Mapping)):
        raise DossierDialectError("compact V2 component research must be an array or object")
    component_rows = list(components.values()) if isinstance(components, Mapping) else list(components)
    for row in component_rows:
        if not isinstance(row, Mapping):
            raise DossierDialectError("compact V2 component rows must be objects")
        component_id = str(row.get("component_id") or "")
        for key in ("positive_fact_ids", "counter_fact_ids", "resolution_fact_ids"):
            for fact_id in row.get(key) or ():
                if str(fact_id) in component_refs:
                    component_refs[str(fact_id)].append(component_id)

    canonical_material = []
    for row in material_rows:
        raw_id = _compact_input_fact_id(row, id_key="fact_id")
        canonical_material.append(
            _compact_source_fact(
                row,
                fact_id=_canonical_compact_fact_id(raw_id),
                direction=(
                    "POSITIVE"
                    if question_refs[raw_id] or component_refs[raw_id]
                    else "NEUTRAL"
                ),
                target_id=target_id,
                company_name=company_name,
                research_pass_id=research_pass_id,
                question_ids=question_refs[raw_id],
                component_ids=component_refs[raw_id],
            )
        )
    canonical_counter = _adapt_compact_nonmaterial_facts(
        counter_rows,
        id_key="counterfact_id",
        anchor_key="fact_ids",
        direction="COUNTER",
        material_by_id=material_by_id,
        target_id=target_id,
        company_name=company_name,
        research_pass_id=research_pass_id,
        question_refs=question_refs,
        component_refs=component_refs,
    )
    canonical_resolution = _adapt_compact_nonmaterial_facts(
        resolution_rows,
        id_key="resolution_fact_id",
        anchor_key="support_fact_ids",
        direction="RESOLUTION",
        material_by_id=material_by_id,
        target_id=target_id,
        company_name=company_name,
        research_pass_id=research_pass_id,
        question_refs=question_refs,
        component_refs=component_refs,
    )
    adapted["material_facts"] = canonical_material
    adapted["counterfacts"] = canonical_counter
    adapted["resolution_facts"] = canonical_resolution

    candidates = adapted.get("candidate_archetypes") or []
    if not isinstance(candidates, list):
        raise DossierDialectError("compact V2 candidate archetypes must be an array")
    adapted["candidate_archetypes"] = [
        str(row.get("archetype_id") or "") if isinstance(row, Mapping) else str(row)
        for row in candidates
    ]
    selected = adapted.get("selected_archetypes") or []
    if not isinstance(selected, list):
        raise DossierDialectError("compact V2 selected archetypes must be an array")
    selected_objects = [row for row in selected if isinstance(row, Mapping)]
    primary_selected = [
        str(row.get("archetype_id") or "")
        for row in selected_objects
        if str(row.get("role") or "").upper() == "PRIMARY"
    ]
    if not primary_selected:
        primary_selected = [
            str(row.get("archetype_id") or "") if isinstance(row, Mapping) else str(row)
            for row in selected
        ]
    adapted["selected_archetypes"] = primary_selected

    if isinstance(components, list):
        adapted["component_research"] = {
            str(row.get("component_id") or ""): {
                key: value for key, value in row.items() if key != "component_id"
            }
            for row in components
        }

    route_question_by_id = _route_question_ownership(
        adapted,
        prior_dossier=prior_dossier,
    )
    cross_question_route_references = [
        diagnostic
        for row in question_rows
        if (
            diagnostic := _cross_question_route_reference_diagnostic(
                row,
                route_question_by_id=route_question_by_id,
            )
        )
    ]
    adapted["question_family_results"] = [
        _canonical_question_result(
            row,
            route_question_by_id=route_question_by_id,
        )
        for row in question_rows
    ]
    adapted["unresolved_gaps"] = _canonical_compact_gaps(
        adapted.get("unresolved_gaps") or (),
        questions_by_id=questions_by_id,
    )
    adapted["source_lineages"] = [
        {
            **dict(row),
            "source_urls": list(row.get("source_urls") or row.get("canonical_source_urls") or ()),
            "independence_group_id": str(
                row.get("independence_group_id")
                or row.get("source_lineage_id")
                or ""
            ),
            "status": "ACTIVE",
        }
        for row in adapted.get("source_lineages") or ()
    ]
    projected_prior_lineage_count = _project_referenced_prior_lineages(
        adapted,
        prior_dossier=prior_dossier,
    )
    adapted["search_route_receipts"] = [
        _canonical_route_receipt(row)
        for row in adapted.get("search_route_receipts") or ()
    ]
    adapted["research_passes"] = [
        _canonical_research_pass(row)
        for row in adapted.get("research_passes") or ()
    ]
    self_reported_repairs = deepcopy(adapted.get("verification_repair_register") or [])
    adapted["verification_repair_register"] = _scoped_verifier_repair_proposals(
        self_reported_repairs,
        research_pass_id=research_pass_id,
        research_passes=adapted["research_passes"],
    )
    saturation = dict(adapted.get("research_saturation") or {})
    saturation["pro_self_reported_verification_repairs"] = self_reported_repairs
    saturation["pro_applied_cross_guards"] = [
        deepcopy(row)
        for row in selected_objects
        if str(row.get("role") or "").upper() != "PRIMARY"
    ]
    saturation["pro_cross_question_route_references"] = (
        cross_question_route_references
    )
    adapted["research_saturation"] = saturation
    adapted["parent_pass_id"] = _none_to_null(adapted.get("parent_pass_id"))
    adapted = _rewrite_exact_identifiers(adapted, id_map)
    return _CompactV2Adaptation(
        payload=adapted,
        operations=(
            f"ADAPT_COMPACT_V2_SOURCE_FACTS:{len(canonical_material)}",
            f"ADAPT_COMPACT_V2_COUNTER_RELATIONSHIPS:{len(canonical_counter)}",
            f"ADAPT_COMPACT_V2_RESOLUTION_RELATIONSHIPS:{len(canonical_resolution)}",
            f"MAP_COMPACT_V2_FACT_IDS:{len(id_map)}",
            "PROJECT_PRIMARY_SELECTED_ARCHETYPES_AND_PRESERVE_CROSS_GUARDS",
            "PROJECT_COMPONENT_RESEARCH_ARRAY_TO_ID_OBJECT",
            f"PROJECT_COMPACT_V2_GAPS:{len(adapted['unresolved_gaps'])}",
            f"PROJECT_COMPACT_V2_ROUTE_RECEIPTS:{len(adapted['search_route_receipts'])}",
            (
                "PROJECT_EXACT_PRIOR_REPAIR_SOURCE_IDENTITY:"
                f"{projected_repair_source_identity_count}"
            ),
            (
                "PROJECT_REFERENCED_PRIOR_LINEAGES_FOR_DELTA_VALIDATION:"
                f"{projected_prior_lineage_count}"
            ),
            "FILTER_CROSS_QUESTION_ROUTE_REFERENCES_TO_CANONICAL_OWNER",
            "PRESERVE_PRO_SELF_REPAIR_AS_NONAUTHORITATIVE_DIAGNOSTIC",
            (
                "PRESERVE_SCOPED_VERIFIER_REPAIR_PROPOSALS_FOR_"
                "DETERMINISTIC_REVERIFICATION:"
                f"{len(adapted['verification_repair_register'])}"
            ),
        ),
        id_map=dict(sorted(id_map.items())),
    )


def _scoped_verifier_repair_proposals(
    rows: list[Any],
    *,
    research_pass_id: str,
    research_passes: list[Mapping[str, Any]],
) -> list[Mapping[str, Any]]:
    """Keep only packet-shaped repair proposals from the current repair pass.

    The adapter does not approve these proposals.  ``response_delta`` must
    still bind each one to an exact durable rejection packet and the source
    verifier must accept the replacement fact before it can affect the
    effective dossier.
    """

    current_pass_is_repair = any(
        str(row.get("pass_id") or row.get("research_pass_id") or "")
        == research_pass_id
        and str(row.get("pass_name") or "").upper() == "VERIFIER_REPAIR"
        for row in research_passes
        if isinstance(row, Mapping)
    )
    if not current_pass_is_repair:
        return []
    result: list[Mapping[str, Any]] = []
    for row in rows:
        if not isinstance(row, Mapping):
            continue
        candidate_id = str(row.get("candidate_id") or "")
        question_id = str(row.get("question_family_id") or "")
        category = str(row.get("rejection_category") or "")
        action = str(row.get("status") or "")
        replacement_id = str(
            row.get("dossier_fact_id")
            or row.get("replacement_candidate_id")
            or row.get("replacement_dossier_fact_id")
            or ""
        )
        if not _COMPACT_V2_FACT_ID.fullmatch(candidate_id):
            continue
        if not question_id:
            continue
        if category not in _SCOPED_REJECTION_CATEGORIES:
            continue
        if action not in _SCOPED_REPAIR_ACTIONS:
            continue
        if action != "WITHDRAWN" and not _COMPACT_V2_FACT_ID.fullmatch(
            replacement_id
        ):
            continue
        result.append(deepcopy(dict(row)))
    return result


def _project_compact_repair_source_identity(
    payload: Mapping[str, Any],
    *,
    prior_dossier: Mapping[str, Any] | None,
) -> int:
    """Fill only omitted source identity from the exact repaired candidate.

    A compact repair replacement can repeat the immutable source URL,
    lineage, and a corrected literal excerpt while omitting the publisher.
    The publisher/title are source identity rather than new research claims,
    so they may be copied byte-for-byte only when ``repair_of_candidate_id``
    resolves in the exact prior dossier and URL plus lineage are unchanged.
    Any changed source remains fail-closed.
    """

    rows = tuple(
        row
        for collection in ("material_facts", "counterfacts", "resolution_facts")
        for row in payload.get(collection) or ()
        if isinstance(row, dict)
    )
    candidates = tuple(
        row
        for row in rows
        if str(row.get("repair_of_candidate_id") or "")
        and not str(
            row.get("source_publisher") or row.get("publisher") or ""
        ).strip()
    )
    if not candidates:
        return 0
    if prior_dossier is None:
        return 0
    _validate_prior_dossier_scope(payload, prior_dossier)
    prior_by_id = {
        str(row.get("dossier_fact_id") or ""): row
        for collection in ("material_facts", "counterfacts", "resolution_facts")
        for row in prior_dossier.get(collection) or ()
        if isinstance(row, Mapping)
    }
    projected = 0
    for row in candidates:
        repair_of = str(row.get("repair_of_candidate_id") or "")
        canonical_repair_of = _canonical_compact_fact_id(repair_of)
        prior = prior_by_id.get(canonical_repair_of)
        if prior is None:
            continue
        source_url = str(row.get("source_url") or row.get("url") or "")
        prior_url = str(prior.get("source_url") or prior.get("url") or "")
        lineage_id = str(row.get("source_lineage_id") or "")
        prior_lineage_id = str(prior.get("source_lineage_id") or "")
        if source_url != prior_url or lineage_id != prior_lineage_id:
            raise DossierDialectError(
                "compact repair omitted publisher while changing prior source identity: "
                f"{row.get('dossier_fact_id') or row.get('fact_id') or repair_of}"
            )
        prior_publisher = str(prior.get("source_publisher") or "")
        if not prior_publisher:
            continue
        row["source_publisher"] = prior_publisher
        if not str(row.get("source_title") or "").strip():
            prior_title = str(prior.get("source_title") or "")
            if prior_title:
                row["source_title"] = prior_title
        projected += 1
    return projected


def _compact_input_fact_id(row: Mapping[str, Any], *, id_key: str) -> str:
    return str(row.get(id_key) or row.get("dossier_fact_id") or "")


def _canonical_compact_fact_id(value: str) -> str:
    return value if value.startswith("PROFACT-") else f"PROFACT-{value}"


def _adapt_compact_nonmaterial_facts(
    rows: list[Mapping[str, Any]],
    *,
    id_key: str,
    anchor_key: str,
    direction: str,
    material_by_id: Mapping[str, Mapping[str, Any]],
    target_id: str,
    company_name: str,
    research_pass_id: str,
    question_refs: Mapping[str, list[str]],
    component_refs: Mapping[str, list[str]],
) -> list[Mapping[str, Any]]:
    result: list[Mapping[str, Any]] = []
    for row in rows:
        raw_id = _compact_input_fact_id(row, id_key=id_key)
        canonical_id = _canonical_compact_fact_id(raw_id)
        question_ids = tuple(
            dict.fromkeys(
                (
                    *(str(value) for value in row.get("affected_question_ids") or ()),
                    *question_refs[raw_id],
                )
            )
        )
        if _compact_row_has_direct_source_evidence(row):
            result.append(
                _compact_source_fact(
                    row,
                    fact_id=canonical_id,
                    direction=direction,
                    target_id=target_id,
                    company_name=company_name,
                    research_pass_id=research_pass_id,
                    question_ids=question_ids,
                    component_ids=component_refs[raw_id],
                )
            )
            continue
        result.append(
            _compact_relationship_fact(
                row,
                relationship_id=canonical_id,
                anchor_ids=tuple(str(value) for value in row.get(anchor_key) or ()),
                direction=direction,
                material_by_id=material_by_id,
                target_id=target_id,
                company_name=company_name,
                research_pass_id=research_pass_id,
                question_ids=question_ids,
                component_ids=component_refs[raw_id],
            )
        )
    return result


def _compact_row_has_direct_source_evidence(row: Mapping[str, Any]) -> bool:
    values = (
        row.get("statement") or row.get("summary"),
        row.get("source_url") or row.get("url"),
        row.get("source_publisher") or row.get("publisher"),
        row.get("supporting_excerpt") or row.get("exact_short_excerpt"),
        row.get("source_lineage_id"),
    )
    return all(str(value or "").strip() for value in values)


def _project_referenced_prior_lineages(
    payload: dict[str, Any],
    *,
    prior_dossier: Mapping[str, Any] | None,
) -> int:
    facts = tuple(
        row
        for collection in ("material_facts", "counterfacts", "resolution_facts")
        for row in payload.get(collection) or ()
        if isinstance(row, Mapping)
    )
    references: dict[str, list[Mapping[str, Any]]] = {}
    for fact in facts:
        lineage_id = str(fact.get("source_lineage_id") or "")
        if not lineage_id:
            raise DossierDialectError("compact V2 fact lacks source lineage identity")
        references.setdefault(lineage_id, []).append(fact)
    current_rows = payload.get("source_lineages") or []
    current_ids = {
        str(row.get("source_lineage_id") or "")
        for row in current_rows
        if isinstance(row, Mapping)
    }
    missing = tuple(value for value in references if value not in current_ids)
    if not missing:
        return 0
    if prior_dossier is None:
        raise DossierDialectError(
            "compact V2 delta references a lineage absent from its response"
        )
    _validate_prior_dossier_scope(payload, prior_dossier)
    prior_by_id = {
        str(row.get("source_lineage_id") or ""): row
        for row in prior_dossier.get("source_lineages") or ()
        if isinstance(row, Mapping)
    }
    prior_facts_by_lineage: dict[str, list[Mapping[str, Any]]] = {}
    for collection in ("material_facts", "counterfacts", "resolution_facts"):
        for fact in prior_dossier.get(collection) or ():
            if not isinstance(fact, Mapping):
                continue
            prior_facts_by_lineage.setdefault(
                str(fact.get("source_lineage_id") or ""), []
            ).append(fact)
    for lineage_id in missing:
        prior = prior_by_id.get(lineage_id)
        if prior is None:
            prior_facts = prior_facts_by_lineage.get(lineage_id) or []
            prior_urls = list(
                dict.fromkeys(
                    str(fact.get("source_url") or "")
                    for fact in prior_facts
                    if str(fact.get("source_url") or "")
                )
            )
            if not prior_urls:
                raise DossierDialectError(
                    "compact V2 delta references an unknown prior lineage: "
                    f"{lineage_id}"
                )
            prior = {
                "source_lineage_id": lineage_id,
                "source_urls": prior_urls,
                "fact_ids": [
                    str(fact.get("dossier_fact_id") or "")
                    for fact in prior_facts
                    if str(fact.get("dossier_fact_id") or "")
                ],
                "independence_group_id": lineage_id,
                "status": "ACTIVE",
                "projection_source": "EXACT_PRIOR_FACT_EVIDENCE",
            }
        prior_urls = {
            str(value) for value in prior.get("source_urls") or ()
        }
        response_fact_ids: list[str] = []
        for fact in references[lineage_id]:
            source_url = str(fact.get("source_url") or "")
            if source_url not in prior_urls:
                raise DossierDialectError(
                    "compact V2 fact changed the URL of a referenced prior lineage"
                )
            response_fact_ids.append(str(fact.get("dossier_fact_id") or ""))
        current_rows.append(
            {
                **deepcopy(dict(prior)),
                "fact_ids": list(dict.fromkeys(response_fact_ids)),
            }
        )
    payload["source_lineages"] = current_rows
    return len(missing)


def _prior_compact_source_fact_index(
    payload: Mapping[str, Any],
    *,
    prior_dossier: Mapping[str, Any] | None,
) -> Mapping[str, Mapping[str, Any]]:
    """Expose exact prior material facts as anchors for a follow-up delta.

    A follow-up is allowed to cite a material fact accepted into the same
    conversation's immediately preceding effective dossier without repeating
    the full fact row.  This projection copies source evidence byte-for-byte;
    it never synthesizes a URL, publication date, or excerpt.
    """

    if prior_dossier is None:
        return {}
    _validate_prior_dossier_scope(payload, prior_dossier)
    result: dict[str, Mapping[str, Any]] = {}
    for row in prior_dossier.get("material_facts") or ():
        if not isinstance(row, Mapping):
            raise DossierDialectError("prior dossier material fact must be an object")
        canonical_id = str(row.get("dossier_fact_id") or "")
        if not canonical_id.startswith("PROFACT-"):
            raise DossierDialectError(
                "prior dossier material fact lacks a canonical PROFACT id"
            )
        compact_id = canonical_id.removeprefix("PROFACT-")
        if not _COMPACT_V2_FACT_ID.fullmatch(compact_id):
            raise DossierDialectError(
                f"prior dossier fact has an unsupported compact id: {canonical_id!r}"
            )
        source_url = str(row.get("source_url") or "")
        source_publisher = str(row.get("source_publisher") or "")
        supporting_excerpt = str(row.get("supporting_excerpt") or "")
        source_lineage_id = str(row.get("source_lineage_id") or "")
        if not all(
            (source_url, source_publisher, supporting_excerpt, source_lineage_id)
        ):
            raise DossierDialectError(
                f"prior dossier source fact lacks exact evidence fields: {canonical_id}"
            )
        projected = {
            **dict(row),
            "fact_id": compact_id,
            "summary": str(row.get("statement") or ""),
            "url": source_url,
            "publisher": source_publisher,
            "publication_date": row.get("published_at"),
            "availability_date": row.get("availability_date")
            or row.get("event_date")
            or row.get("published_at"),
            "exact_short_excerpt": supporting_excerpt,
            "source_lineage_id": source_lineage_id,
            "fact_type": str(
                row.get("fact_type")
                or row.get("economic_mechanism")
                or "SOURCE_BACKED_FACT"
            ),
            "target": row.get("target") or row.get("target_id"),
        }
        result[compact_id] = projected
        result[canonical_id] = projected
    return result


def _validate_prior_dossier_scope(
    payload: Mapping[str, Any], prior_dossier: Mapping[str, Any]
) -> None:
    for key in ("job_id", "run_id", "conversation_id", "as_of_date"):
        if payload.get(key) != prior_dossier.get(key):
            raise DossierDialectError(
                f"prior dossier differs from compact follow-up scope: {key}"
            )
    payload_target = payload.get("target") or {}
    prior_target = prior_dossier.get("target") or {}
    payload_target_id = str(
        payload_target.get("target_id") or payload_target.get("symbol") or ""
    )
    prior_target_id = str(
        prior_target.get("target_id") or prior_target.get("symbol") or ""
    )
    if not payload_target_id or payload_target_id != prior_target_id:
        raise DossierDialectError(
            "prior dossier differs from compact follow-up target"
        )
    parent_pass_id = str(payload.get("parent_pass_id") or "")
    prior_pass_id = str(prior_dossier.get("research_pass_id") or "")
    if not parent_pass_id or parent_pass_id != prior_pass_id:
        raise DossierDialectError(
            "prior dossier is not the compact follow-up's exact parent pass"
        )


def _route_question_ownership(
    payload: Mapping[str, Any],
    *,
    prior_dossier: Mapping[str, Any] | None,
) -> Mapping[str, str]:
    result: dict[str, str] = {}
    rows = [
        *((prior_dossier or {}).get("search_route_receipts") or ()),
        *(payload.get("search_route_receipts") or ()),
    ]
    for row in rows:
        if not isinstance(row, Mapping):
            raise DossierDialectError("search route receipt must be an object")
        route_id = str(row.get("route_receipt_id") or "")
        question_id = str(row.get("question_family_id") or "")
        if not route_id or not question_id:
            raise DossierDialectError(
                "search route receipt lacks route/question identity"
            )
        prior_owner = result.get(route_id)
        if prior_owner is not None and prior_owner != question_id:
            raise DossierDialectError(
                f"search route receipt changed question owner: {route_id}"
            )
        result[route_id] = question_id
    return result


def _compact_source_fact(
    row: Mapping[str, Any],
    *,
    fact_id: str,
    direction: str,
    target_id: str,
    company_name: str,
    research_pass_id: str,
    question_ids: list[str] | tuple[str, ...],
    component_ids: list[str] | tuple[str, ...],
) -> Mapping[str, Any]:
    statement = str(row.get("summary") or row.get("statement") or "")
    source_url = str(row.get("url") or row.get("source_url") or "")
    source_publisher = str(
        row.get("publisher") or row.get("source_publisher") or ""
    )
    supporting_excerpt = str(
        row.get("exact_short_excerpt") or row.get("supporting_excerpt") or ""
    )
    source_lineage_id = str(row.get("source_lineage_id") or "")
    if any(
        not value.strip()
        for value in (
            statement,
            source_url,
            source_publisher,
            supporting_excerpt,
            source_lineage_id,
        )
    ):
        raise DossierDialectError(
            f"compact V2 source fact lacks required evidence fields: {fact_id}"
        )
    publication_date = str(
        row.get("publication_date") or row.get("published_at") or ""
    ) or None
    availability_date = str(
        row.get("availability_date") or row.get("event_date") or ""
    ) or publication_date
    target_text = str(row.get("target") or "")
    subject = str(
        row.get("subject")
        or target_text
        or source_publisher
    )
    return {
        **dict(row),
        "dossier_fact_id": fact_id,
        "research_pass_id": research_pass_id,
        "question_family_ids": list(dict.fromkeys(str(value) for value in question_ids if str(value))),
        "statement": statement,
        "direction": direction,
        "subject": subject,
        "target_id": target_id,
        "issuer_scoped": _compact_issuer_scope(row),
        "business_segment": row.get("business_segment"),
        "product_family": row.get("product_family"),
        "economic_mechanism": str(row.get("fact_type") or "SOURCE_BACKED_FACT"),
        "predicate": str(row.get("fact_type") or "SOURCE_BACKED_FACT"),
        "value": None,
        "unit": None,
        "period": f"AS_OF:{availability_date or publication_date or 'UNDATED'}",
        "event_date": (
            availability_date
            if availability_date and re.fullmatch(r"\d{4}-\d{2}-\d{2}", availability_date)
            else None
        ),
        "current_status": _canonical_compact_lifecycle(row.get("current_status")),
        "candidate_components": list(dict.fromkeys(str(value) for value in component_ids if str(value))),
        "source_url": source_url,
        "source_title": str(row.get("source_title") or source_publisher),
        "source_publisher": source_publisher,
        "published_at": (
            publication_date
            if publication_date and re.fullmatch(r"\d{4}-\d{2}-\d{2}", publication_date)
            else None
        ),
        "supporting_excerpt": supporting_excerpt,
        "source_lineage_id": source_lineage_id,
        "confidence": 0.0,
    }


_COMPACT_ISSUER_SOURCE_ROLES = frozenset(
    {"ISSUER_OFFICIAL", "ISSUER_EARNINGS", "OFFICIAL_FILING", "AUDITOR_FILING"}
)


def _compact_issuer_scope(row: Mapping[str, Any]) -> bool:
    explicit = row.get("issuer_scoped")
    if isinstance(explicit, bool):
        return explicit
    roles = {
        str(value).strip().upper()
        for value in row.get("source_role_ids") or ()
    }
    return bool(roles.intersection(_COMPACT_ISSUER_SOURCE_ROLES))


def _compact_relationship_fact(
    row: Mapping[str, Any],
    *,
    relationship_id: str,
    anchor_ids: tuple[str, ...],
    direction: str,
    material_by_id: Mapping[str, Mapping[str, Any]],
    target_id: str,
    company_name: str,
    research_pass_id: str,
    question_ids: tuple[str, ...],
    component_ids: list[str] | tuple[str, ...],
) -> Mapping[str, Any]:
    anchors = [material_by_id[value] for value in anchor_ids if value in material_by_id]
    if not anchors:
        raise DossierDialectError(
            f"compact V2 relationship lacks a source-fact anchor: {relationship_id}"
        )
    anchor = anchors[0]
    statement = _compact_relationship_statement(row, relationship_id)
    projected = _compact_source_fact(
        {
            **dict(anchor),
            "summary": statement,
            "current_status": row.get("current_status") or "OPEN",
            "fact_type": f"{direction}_RELATIONSHIP",
        },
        fact_id=relationship_id,
        direction=direction,
        target_id=target_id,
        company_name=company_name,
        research_pass_id=research_pass_id,
        question_ids=question_ids,
        component_ids=component_ids,
    )
    return {
        **projected,
        **dict(row),
        "dossier_fact_id": relationship_id,
        "research_pass_id": research_pass_id,
        "question_family_ids": list(question_ids),
        "statement": statement,
        "direction": direction,
        "economic_mechanism": f"{direction}_RELATIONSHIP",
        "predicate": f"{direction}_RELATIONSHIP",
        "current_status": _canonical_compact_lifecycle(row.get("current_status")),
        "candidate_components": list(dict.fromkeys(component_ids)),
        "source_anchor_fact_ids": list(anchor_ids),
        "issuer_scoped": bool(
            anchor.get("issuer_scoped", projected.get("issuer_scoped", False))
        ),
    }


def _compact_relationship_statement(
    row: Mapping[str, Any], relationship_id: str
) -> str:
    for key in ("current_state_summary", "summary", "claim_text", "statement"):
        value = str(row.get(key) or "").strip()
        if value:
            return value
    raise DossierDialectError(
        f"compact V2 relationship lacks a statement: {relationship_id}"
    )


def _canonical_question_result(
    row: Mapping[str, Any],
    *,
    route_question_by_id: Mapping[str, str],
) -> Mapping[str, Any]:
    availability = str(row.get("availability_class") or "")
    if availability in {
        "PUBLIC_SEARCHABLE",
        "LIKELY_NONPUBLIC",
        "FUTURE_EVENT_ONLY",
        "PROVIDER_BLOCKED",
        "PARSER_BLOCKED",
        "NOT_APPLICABLE",
        "UNKNOWN_ROUTE_NOT_YET_TESTED",
    }:
        canonical_availability = availability
    elif "LIKELY_NONPUBLIC" in availability:
        canonical_availability = "LIKELY_NONPUBLIC"
    elif "FUTURE_EVENT" in availability and "PUBLIC" not in availability:
        canonical_availability = "FUTURE_EVENT_ONLY"
    elif availability == "NOT_APPLICABLE_WITH_REASON":
        canonical_availability = "NOT_APPLICABLE"
    else:
        canonical_availability = "PUBLIC_SEARCHABLE"
    question_id = str(row.get("question_family_id") or "")
    route_ids = tuple(
        str(value) for value in row.get("search_route_receipt_ids") or ()
    )
    unknown = tuple(value for value in route_ids if value not in route_question_by_id)
    if unknown:
        raise DossierDialectError(
            f"compact V2 question references unknown route receipts: {unknown!r}"
        )
    owned = tuple(
        value
        for value in route_ids
        if route_question_by_id[value] == question_id
    )
    return {
        **dict(row),
        "availability_class": canonical_availability,
        "search_route_receipt_ids": list(dict.fromkeys(owned)),
    }


def _cross_question_route_reference_diagnostic(
    row: Mapping[str, Any],
    *,
    route_question_by_id: Mapping[str, str],
) -> Mapping[str, Any] | None:
    question_id = str(row.get("question_family_id") or "")
    cross_question = tuple(
        str(value)
        for value in row.get("search_route_receipt_ids") or ()
        if route_question_by_id.get(str(value)) not in {None, question_id}
    )
    if not cross_question:
        return None
    return {
        "question_family_id": question_id,
        "route_receipt_ids": list(dict.fromkeys(cross_question)),
    }


def _canonical_compact_gaps(
    rows: Any,
    *,
    questions_by_id: Mapping[str, Mapping[str, Any]],
) -> list[Mapping[str, Any]]:
    result: list[Mapping[str, Any]] = []
    for row in rows:
        if not isinstance(row, Mapping):
            raise DossierDialectError("compact V2 gap rows must be objects")
        question_ids = tuple(str(value) for value in row.get("question_family_ids") or ())
        if not question_ids:
            raise DossierDialectError("compact V2 gap must identify a question family")
        for question_id in question_ids:
            question = questions_by_id.get(question_id)
            if question is None:
                raise DossierDialectError("compact V2 gap references an unknown question")
            could_score = question.get("could_change_score") is True
            could_stage = question.get("could_change_stage") is True
            could_hard = question.get("could_change_hard_break") is True
            materiality = (
                "HARD_BREAK"
                if could_hard
                else "STAGE_BOUNDARY"
                if could_stage
                else "SCORE_BOUNDARY"
                if could_score
                else "MONITORING"
            )
            original_gap_id = str(row.get("gap_id") or "")
            result.append(
                {
                    **dict(row),
                    "gap_id": f"{original_gap_id}:{question_id}",
                    "stable_gap_key": f"{original_gap_id}:{question_id}",
                    "archetype_id": str(question.get("archetype_id") or ""),
                    "question_family_id": question_id,
                    "availability_class": str(row.get("availability_class") or question.get("availability_class") or "UNKNOWN_ROUTE_NOT_YET_TESTED"),
                    "materiality": materiality,
                    "required_source_role_ids": list(question.get("required_source_roles_missing") or ()),
                    # Compact Pro repair responses can omit this gap-level
                    # duplicate while retaining the authoritative attempted
                    # role roster on the exact same question row. Project
                    # only that same-question value; never infer roles from a
                    # different question or from a source-family template.
                    "attempted_source_role_ids": list(
                        question.get("attempted_source_role_ids") or ()
                    ),
                    "affected_component_ids": list(question.get("affected_component_ids") or ()),
                    "could_change_score": could_score,
                    "could_change_stage": could_stage,
                    "could_change_hard_break": could_hard,
                }
            )
    return result


def _canonical_route_receipt(row: Mapping[str, Any]) -> Mapping[str, Any]:
    if not isinstance(row, Mapping):
        raise DossierDialectError("compact V2 route receipts must be objects")
    opened = list(row.get("opened_source_urls") or row.get("opened_url_roster") or ())
    accepted = list(row.get("accepted_fact_ids") or row.get("accepted_fact_roster") or ())
    rejected = list(row.get("rejected_candidate_ids") or row.get("rejection_roster") or ())
    return {
        "route_receipt_id": str(row.get("route_receipt_id") or ""),
        "pass_id": str(row.get("pass_id") or ""),
        "archetype_id": str(row.get("archetype_id") or ""),
        "question_family_id": str(row.get("question_family_id") or ""),
        "gap_id": row.get("gap_id"),
        "source_role_id": str(row.get("source_role_id") or ""),
        "query_or_navigation_objective": str(row.get("query_or_navigation_objective") or row.get("navigation_objective") or ""),
        "query_text": row.get("query_text") if "query_text" in row else row.get("query"),
        "result_count_seen": len(row.get("result_roster") or ()),
        "opened_source_urls": opened,
        "accepted_fact_ids": accepted,
        "rejected_candidate_ids": rejected,
        "provider_status": (
            str(row.get("provider_status"))
            if str(row.get("provider_status"))
            in {"SUCCESS", "PROVIDER_PENDING", "PARSER_PENDING", "TRANSPORT_PENDING", "FAILED"}
            else "SUCCESS"
        ),
        "no_new_route_reason": row.get("no_new_route_reason"),
        "performed_at": str(row.get("performed_at") or ""),
    }


def _canonical_research_pass(row: Mapping[str, Any]) -> Mapping[str, Any]:
    if not isinstance(row, Mapping):
        raise DossierDialectError("compact V2 research pass rows must be objects")
    pass_id = str(row.get("pass_id") or row.get("research_pass_id") or "")
    return {
        **dict(row),
        "pass_id": pass_id,
        "parent_pass_id": _none_to_null(row.get("parent_pass_id")),
        "status": str(row.get("status") or "COMPLETE"),
        "prompt_hash": str(row.get("prompt_hash") or "PENDING_DURABLE_BINDING"),
        "response_hash": row.get("response_hash"),
    }


def _canonical_compact_lifecycle(value: Any) -> str:
    normalized = str(value or "UNKNOWN").strip().upper()
    if normalized == "HISTORICAL_ONLY":
        return "HISTORICAL"
    if normalized in _CANONICAL_LIFECYCLES:
        return normalized
    if normalized.startswith("SUPERSEDED"):
        return "SUPERSEDED"
    if normalized.startswith("RESOLVED"):
        return "RESOLVED"
    return "UNKNOWN"


def _none_to_null(value: Any) -> Any:
    return None if str(value or "").strip().upper() in {"", "NONE", "NULL"} else value


def _compact_fact_reference_ids(payload: Mapping[str, Any]) -> tuple[str, ...]:
    """Collect only allowlisted fact-reference fields from a compact delta.

    Follow-up deltas may reference facts created by an earlier pass without
    repeating those fact rows.  Their compact IDs still need the same exact
    canonical prefix mapping as newly returned rows.
    """

    reference_keys = frozenset(
        {
            "support_fact_ids",
            "supporting_material_fact_ids",
            "counter_fact_ids",
            "resolution_fact_ids",
            "positive_fact_ids",
            "fact_ids",
            "resolved_or_superseded_fact_ids",
            "source_anchor_fact_ids",
            "prior_counterfact_ids",
            "existing_fact_ids_referenced",
            "accepted_fact_ids",
            "accepted_fact_roster",
        }
    )
    found: list[str] = []

    def visit(value: Any, *, key: str | None = None) -> None:
        if isinstance(value, Mapping):
            for child_key, child in value.items():
                visit(child, key=str(child_key))
            return
        if isinstance(value, (list, tuple)):
            if key in reference_keys:
                for child in value:
                    text = str(child or "")
                    if _COMPACT_V2_FACT_ID.fullmatch(text):
                        found.append(text)
                return
            for child in value:
                visit(child, key=key)

    visit(payload)
    return tuple(dict.fromkeys(found))


def _canonical_lifecycle(value: str) -> str:
    normalized = value.strip().upper()
    if normalized.startswith("EXPLICIT_UNKNOWN"):
        return "UNKNOWN"
    if normalized.startswith(("OPEN_", "ANNOUNCED_", "BOARD_APPROVED_")):
        return "OPEN"
    if normalized == "CONFIRMED_EXECUTION_UNCERTAINTY":
        return "OPEN"
    if normalized.startswith(("CONFIRMED_", "COMPLETED_")):
        return "CURRENT"
    raise DossierDialectError(f"unsupported detailed lifecycle: {value!r}")


def _canonical_gap_class(
    value: str,
    *,
    could_change_score: bool,
    could_change_stage: bool,
    could_change_hard_break: bool,
) -> str:
    normalized = value.strip().upper()
    if normalized == "EXPLICIT_UNKNOWN":
        return "MONITORING_GAP"
    if normalized not in {"MATERIAL_UNKNOWN", "HIGH_MATERIALITY_UNKNOWN"}:
        raise DossierDialectError(f"unsupported proposed gap class: {value!r}")
    if could_change_hard_break:
        return "HARD_BREAK_GAP"
    if normalized == "HIGH_MATERIALITY_UNKNOWN":
        return "CORE_SCORE_BLOCKER"
    if could_change_score or could_change_stage:
        return "STAGE_BOUNDARY_GAP"
    return "CORROBORATION_CAP"


def _rewrite_exact_identifiers(value: Any, id_map: Mapping[str, str]) -> Any:
    if isinstance(value, dict):
        return {key: _rewrite_exact_identifiers(child, id_map) for key, child in value.items()}
    if isinstance(value, list):
        return [_rewrite_exact_identifiers(child, id_map) for child in value]
    if isinstance(value, str):
        return id_map.get(value, value)
    return value


def _legacy_identifier_strings(value: Any) -> set[str]:
    found: set[str] = set()
    if isinstance(value, Mapping):
        for child in value.values():
            found.update(_legacy_identifier_strings(child))
    elif isinstance(value, (list, tuple)):
        for child in value:
            found.update(_legacy_identifier_strings(child))
    elif isinstance(value, str) and (
        _LEGACY_FACT_ID.fullmatch(value) or _LEGACY_GAP_ID.fullmatch(value)
    ):
        found.add(value)
    return found


def _protected_fact_values(payload: Mapping[str, Any]) -> tuple[tuple[Any, ...], ...]:
    return tuple(
        tuple(deepcopy(fact.get(key)) for key in _PROTECTED_FACT_FIELDS)
        for collection in ("material_facts", "counterfacts", "resolution_facts")
        for fact in payload.get(collection) or ()
        if isinstance(fact, Mapping)
    )


def _fact_count(payload: Mapping[str, Any]) -> int:
    return sum(
        len(payload.get(key) or ())
        for key in ("material_facts", "counterfacts", "resolution_facts")
    )


__all__ = [
    "AdaptedDossier",
    "DossierDialectError",
    "ResearchDossierDialectAdapter",
]
