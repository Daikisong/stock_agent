"""Schemas for LLM-assisted theme routing.

The route output is intentionally JSON-safe and deterministic-rule friendly.
It may suggest searches and diagnostics, but it must not carry a final Stage.
"""

from __future__ import annotations

import re
from collections.abc import Sequence
from dataclasses import dataclass, field
from datetime import date
from typing import Any, Mapping


ALLOWED_ROUTE_STATUSES = {
    "no_transition",
    "mixed_route",
    "transition_detected",
    "disabled_no_provider",
    "provider_error",
    "invalid_provider_output",
    "needs_more_evidence",
    "more_evidence_needed",
}
DISALLOWED_STAGE_FIELDS = {"stage", "deterministic_stage", "stage_override", "attempted_stage_override"}
ROUTE_STATUS_ALIASES = {
    "insufficient_evidence": "needs_more_evidence",
    "insufficient-evidence": "needs_more_evidence",
    "need_more_evidence": "needs_more_evidence",
    "blocked": "needs_more_evidence",
    "uncertain": "needs_more_evidence",
    "unknown": "needs_more_evidence",
    "mixed": "mixed_route",
    "transition": "transition_detected",
    "theme_transition": "transition_detected",
    "error": "provider_error",
}


@dataclass(frozen=True)
class ThemeRouteSearchResult:
    """Primitive search result view passed to a theme route provider."""

    title: str
    url: str
    snippet: str | None = None
    source: str | None = None
    published_at: str | None = None
    query: str | None = None

    @classmethod
    def from_search_result(cls, result: Any) -> "ThemeRouteSearchResult":
        return cls(
            title=result.title,
            url=result.url,
            snippet=result.snippet,
            source=result.source,
            published_at=result.published_at.isoformat() if result.published_at else None,
            query=result.query,
        )


@dataclass(frozen=True)
class ThemeRouteDocument:
    """Fetched document excerpt and parser context passed to a theme route provider."""

    title: str
    url: str
    source: str | None = None
    published_at: str | None = None
    query: str | None = None
    fetch_ok: bool = False
    fetch_reason: str | None = None
    text_excerpt: str | None = None
    evidence_ids: tuple[str, ...] = field(default_factory=tuple)
    parsed_fields: Mapping[str, bool | float | str] = field(default_factory=dict)

    def __post_init__(self) -> None:
        object.__setattr__(self, "title", str(self.title or ""))
        object.__setattr__(self, "url", str(self.url or ""))
        object.__setattr__(self, "evidence_ids", tuple(str(item) for item in self.evidence_ids if str(item).strip()))
        object.__setattr__(self, "parsed_fields", _json_safe_parsed_fields(self.parsed_fields))


@dataclass(frozen=True)
class EvidenceSlotStatus:
    """Whether a required theme evidence slot is source-backed."""

    slot: str
    status: str = "unknown"
    evidence_refs: tuple[str, ...] = field(default_factory=tuple)
    confidence: float = 0.0
    missing_reason: str | None = None

    def __post_init__(self) -> None:
        status = self.status if self.status in {"present", "missing", "contradicted", "unknown"} else "unknown"
        confidence = _clamp_unit(_float_or_none(self.confidence) or 0.0)
        object.__setattr__(self, "slot", str(self.slot or "unknown"))
        object.__setattr__(self, "status", status)
        object.__setattr__(self, "evidence_refs", tuple(str(item) for item in self.evidence_refs if str(item).strip()))
        object.__setattr__(self, "confidence", confidence)


@dataclass(frozen=True)
class ThemeRouteInput:
    """LLM theme route request for one company and as-of date."""

    company_name: str
    symbol: str
    as_of_date: date
    market: str
    sector: str | None = None
    stage_context: str | None = None
    candidate_reason_codes: tuple[str, ...] = field(default_factory=tuple)
    current_large_sector_id: str | None = None
    current_canonical_archetype_id: str | None = None
    search_results: tuple[ThemeRouteSearchResult, ...] = field(default_factory=tuple)
    documents: tuple[ThemeRouteDocument, ...] = field(default_factory=tuple)
    score_gap_context: tuple[str, ...] = field(default_factory=tuple)

    def __post_init__(self) -> None:
        object.__setattr__(self, "candidate_reason_codes", tuple(str(item) for item in self.candidate_reason_codes))
        object.__setattr__(self, "search_results", tuple(self.search_results))
        object.__setattr__(self, "documents", tuple(self.documents))
        object.__setattr__(self, "score_gap_context", tuple(str(item) for item in self.score_gap_context if str(item).strip()))


@dataclass(frozen=True)
class ThemeRouteOutput:
    """Validated route result used by the deterministic pipeline."""

    status: str = "no_transition"
    transition_detected: bool = False
    route_confidence: float = 0.0
    emerging_theme_id: str | None = None
    primary_route_id: str | None = None
    large_sector_id: str | None = None
    canonical_archetype_id: str | None = None
    secondary_archetype_ids: tuple[str, ...] = field(default_factory=tuple)
    normalized_parsed_fields: Mapping[str, bool | float | str] = field(default_factory=dict)
    diagnostic_scores: Mapping[str, float] = field(default_factory=dict)
    evidence_slots: tuple[EvidenceSlotStatus, ...] = field(default_factory=tuple)
    missing_information: tuple[str, ...] = field(default_factory=tuple)
    suggested_queries: tuple[str, ...] = field(default_factory=tuple)
    blocked_reason: str | None = None

    def __post_init__(self) -> None:
        if self.status not in ALLOWED_ROUTE_STATUSES:
            object.__setattr__(self, "status", "invalid_provider_output")
        object.__setattr__(self, "route_confidence", _clamp_unit(float(self.route_confidence)))
        object.__setattr__(self, "secondary_archetype_ids", tuple(str(item) for item in self.secondary_archetype_ids if str(item).strip()))
        object.__setattr__(self, "missing_information", tuple(str(item) for item in self.missing_information if str(item).strip()))
        object.__setattr__(self, "suggested_queries", tuple(str(item) for item in self.suggested_queries if str(item).strip()))
        object.__setattr__(self, "evidence_slots", tuple(self.evidence_slots))
        object.__setattr__(self, "normalized_parsed_fields", dict(self.normalized_parsed_fields))
        object.__setattr__(self, "diagnostic_scores", dict(self.diagnostic_scores))


def validate_theme_route_output(raw: ThemeRouteOutput | Mapping[str, Any] | None) -> ThemeRouteOutput:
    """Return a sanitized route output with no direct stage override channel."""

    if raw is None:
        return ThemeRouteOutput()
    if isinstance(raw, ThemeRouteOutput):
        data = _theme_route_output_to_dict(raw)
    elif isinstance(raw, Mapping):
        data = dict(raw)
    else:
        return ThemeRouteOutput(status="invalid_provider_output", blocked_reason="provider output was not a mapping")

    for key in DISALLOWED_STAGE_FIELDS:
        data.pop(key, None)

    fields = _json_safe_parsed_fields(data.get("normalized_parsed_fields") or data.get("parsed_fields") or {})
    diagnostics = _diagnostic_scores(data.get("diagnostic_scores") or {})
    slots = _evidence_slots(data.get("evidence_slots") or ())
    status = _normalise_route_status(data.get("status"))
    return ThemeRouteOutput(
        status=status,
        transition_detected=_bool_value(data.get("transition_detected")),
        route_confidence=_clamp_unit(_float_or_none(data.get("route_confidence")) or _float_or_none(data.get("confidence")) or 0.0),
        emerging_theme_id=_clean_optional_text(data.get("emerging_theme_id")),
        primary_route_id=_clean_optional_text(data.get("primary_route_id") or data.get("route_id")),
        large_sector_id=_clean_optional_text(data.get("large_sector_id")),
        canonical_archetype_id=_clean_optional_text(data.get("canonical_archetype_id")),
        secondary_archetype_ids=_text_tuple(data.get("secondary_archetype_ids") or ()),
        normalized_parsed_fields=fields,
        diagnostic_scores=diagnostics,
        evidence_slots=slots,
        missing_information=_text_tuple(data.get("missing_information") or ()),
        suggested_queries=_text_tuple(data.get("suggested_queries") or ()),
        blocked_reason=_clean_optional_text(data.get("blocked_reason")),
    )


def route_diagnostics(route: ThemeRouteOutput | None) -> dict[str, float]:
    """Convert a validated route into bounded numeric diagnostics."""

    if route is None:
        return {}
    diagnostics = dict(route.diagnostic_scores)
    diagnostics["theme_route_confidence"] = round(route.route_confidence * 100.0, 4)
    diagnostics["theme_transition_detected"] = 100.0 if route.transition_detected else 0.0
    diagnostics["emerging_theme_active"] = 100.0 if route.emerging_theme_id else 0.0
    present_slots = sum(1 for slot in route.evidence_slots if slot.status == "present" and slot.evidence_refs)
    missing_slots = sum(1 for slot in route.evidence_slots if slot.status in {"missing", "unknown"})
    if route.evidence_slots:
        diagnostics["theme_evidence_slot_present_count_capped"] = min(float(present_slots), 100.0)
        diagnostics["theme_evidence_slot_missing_count_capped"] = min(float(missing_slots), 100.0)
        diagnostics["green_unlock_evidence_score"] = round(min(100.0, present_slots / max(1, len(route.evidence_slots)) * 100.0), 4)
    return {key: _clamp_100(float(value)) for key, value in diagnostics.items()}


def _theme_route_output_to_dict(output: ThemeRouteOutput) -> dict[str, Any]:
    return {
        "status": output.status,
        "transition_detected": output.transition_detected,
        "route_confidence": output.route_confidence,
        "emerging_theme_id": output.emerging_theme_id,
        "primary_route_id": output.primary_route_id,
        "large_sector_id": output.large_sector_id,
        "canonical_archetype_id": output.canonical_archetype_id,
        "secondary_archetype_ids": output.secondary_archetype_ids,
        "normalized_parsed_fields": output.normalized_parsed_fields,
        "diagnostic_scores": output.diagnostic_scores,
        "evidence_slots": output.evidence_slots,
        "missing_information": output.missing_information,
        "suggested_queries": output.suggested_queries,
        "blocked_reason": output.blocked_reason,
    }


def _evidence_slots(raw: Any) -> tuple[EvidenceSlotStatus, ...]:
    slots: list[EvidenceSlotStatus] = []
    for item in raw if isinstance(raw, Sequence) and not isinstance(raw, (str, bytes)) else ():
        if isinstance(item, EvidenceSlotStatus):
            slots.append(item)
        elif isinstance(item, Mapping):
            slots.append(
                EvidenceSlotStatus(
                    slot=str(item.get("slot") or item.get("name") or "unknown"),
                    status=str(item.get("status") or "unknown"),
                    evidence_refs=_text_tuple(item.get("evidence_refs") or item.get("evidence_ids") or ()),
                    confidence=_float_or_none(item.get("confidence")) or 0.0,
                    missing_reason=_clean_optional_text(item.get("missing_reason")),
                )
            )
    return tuple(slots)


def _diagnostic_scores(raw: Any) -> dict[str, float]:
    if not isinstance(raw, Mapping):
        return {}
    diagnostics: dict[str, float] = {}
    for key, value in raw.items():
        number = _float_or_none(value)
        if number is None:
            continue
        diagnostics[str(key)] = _clamp_100(number)
    return diagnostics


def _normalise_route_status(raw: Any) -> str:
    text = str(raw or "no_transition").strip()
    if text in ALLOWED_ROUTE_STATUSES:
        return text
    key = re.sub(r"[\s/]+", "_", text.lower())
    key = key.replace("-", "_")
    if key in ROUTE_STATUS_ALIASES:
        return ROUTE_STATUS_ALIASES[key]
    return "invalid_provider_output"


def _json_safe_parsed_fields(raw: Any) -> dict[str, bool | float | str]:
    if not isinstance(raw, Mapping):
        return {}
    fields: dict[str, bool | float | str] = {}
    for key, value in raw.items():
        key_text = str(key).strip()
        if not key_text or key_text in DISALLOWED_STAGE_FIELDS:
            continue
        clean = _json_safe_value(value)
        if clean is not None:
            fields[key_text] = clean
    return fields


def _json_safe_value(value: Any) -> bool | float | str | None:
    if isinstance(value, bool):
        return value
    if isinstance(value, (int, float)) and not isinstance(value, bool):
        return float(value)
    if isinstance(value, str):
        text = value.strip()
        lowered = text.lower()
        if lowered in {"true", "yes", "y", "1"}:
            return True
        if lowered in {"false", "no", "n", "0"}:
            return False
        percent = re.fullmatch(r"([-+]?\d+(?:\.\d+)?)\s*%", text.replace(",", ""))
        if percent:
            return float(percent.group(1))
        number = _float_or_none(text.replace(",", ""))
        if number is not None:
            return number
        return text
    return None


def _text_tuple(value: Any) -> tuple[str, ...]:
    if isinstance(value, str):
        return (value.strip(),) if value.strip() else ()
    if not isinstance(value, Sequence):
        return ()
    return tuple(str(item).strip() for item in value if str(item).strip())


def _clean_optional_text(value: Any) -> str | None:
    if value in (None, ""):
        return None
    text = str(value).strip()
    return text or None


def _bool_value(value: Any) -> bool:
    clean = _json_safe_value(value)
    if isinstance(clean, bool):
        return clean
    if isinstance(clean, (int, float)):
        return clean != 0
    return False


def _float_or_none(value: Any) -> float | None:
    if value in (None, ""):
        return None
    if isinstance(value, bool):
        return 1.0 if value else 0.0
    try:
        return float(value)
    except (TypeError, ValueError):
        return None


def _clamp_unit(value: float) -> float:
    return max(0.0, min(1.0, value))


def _clamp_100(value: float) -> float:
    return max(0.0, min(100.0, value))


__all__ = [
    "DISALLOWED_STAGE_FIELDS",
    "EvidenceSlotStatus",
    "ThemeRouteDocument",
    "ThemeRouteInput",
    "ThemeRouteOutput",
    "ThemeRouteSearchResult",
    "route_diagnostics",
    "validate_theme_route_output",
]
