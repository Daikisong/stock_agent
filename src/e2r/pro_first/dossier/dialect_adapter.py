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

    def adapt(self, payload: Mapping[str, Any]) -> AdaptedDossier:
        before_hash = canonical_hash(payload)
        adapted = deepcopy(dict(payload))
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
        for collection in ("material_facts", "counterfacts")
        for fact in payload.get(collection) or ()
        if isinstance(fact, Mapping)
    )


def _fact_count(payload: Mapping[str, Any]) -> int:
    return sum(len(payload.get(key) or ()) for key in ("material_facts", "counterfacts"))


__all__ = [
    "AdaptedDossier",
    "DossierDialectError",
    "ResearchDossierDialectAdapter",
]
