"""Source quality classification for normalized research memory rows."""

from __future__ import annotations

import re
from typing import Any, Mapping

from e2r.research_brain.schemas import SourceQualityClass, UsagePolicy


_URL_RE = re.compile(r"https?://[^\s)>\]\"']+")
_PRICE_OUTCOME_KEYS = (
    "mfe",
    "mae",
    "drawdown",
    "post_peak",
    "future_outcome",
    "outcome_label",
)


def classify_source_quality(data: Mapping[str, Any], text: str = "") -> SourceQualityClass:
    haystack = _haystack(data, text)
    source_proxy_only = _boolish(data.get("source_proxy_only")) or "source_proxy_only" in haystack
    evidence_url_pending = _boolish(data.get("evidence_url_pending")) or "evidence_url_pending" in haystack
    invalid = any(token in haystack for token in ("invalid", "duplicate", "corporate_action_contaminated"))
    has_url = bool(_first_url(data, text))
    has_anchor_hint = any(token in haystack for token in ("quote", "anchor", "source_url", "evidence_url", "url_backed"))
    price_path = any(token in haystack for token in _PRICE_OUTCOME_KEYS)

    if invalid:
        return SourceQualityClass.E_INVALID_OR_DUPLICATE
    if source_proxy_only or evidence_url_pending:
        return SourceQualityClass.C_SOURCE_PROXY_ONTOLOGY_ONLY
    if price_path and not has_url:
        return SourceQualityClass.D_PRICE_PATH_ONLY_OR_FUTURE_LEAKAGE_RISK
    if has_url and has_anchor_hint:
        return SourceQualityClass.A_URL_BACKED_REPLAY_READY
    if has_url:
        return SourceQualityClass.B_URL_BACKED_REPAIR_NEEDED
    if price_path:
        return SourceQualityClass.D_PRICE_PATH_ONLY_OR_FUTURE_LEAKAGE_RISK
    return SourceQualityClass.C_SOURCE_PROXY_ONTOLOGY_ONLY


def usage_policy_for_quality(quality: SourceQualityClass) -> UsagePolicy:
    if quality == SourceQualityClass.A_URL_BACKED_REPLAY_READY:
        return UsagePolicy(allowed_for_replay_fixture=True)
    if quality == SourceQualityClass.B_URL_BACKED_REPAIR_NEEDED:
        return UsagePolicy(allowed_for_runtime_planning=True, allowed_for_replay_fixture=False)
    if quality == SourceQualityClass.C_SOURCE_PROXY_ONTOLOGY_ONLY:
        return UsagePolicy(allowed_for_runtime_planning=True, allowed_for_replay_fixture=False)
    if quality == SourceQualityClass.D_PRICE_PATH_ONLY_OR_FUTURE_LEAKAGE_RISK:
        return UsagePolicy(
            allowed_for_runtime_planning=True,
            allowed_for_replay_fixture=False,
            allowed_for_query_planning=False,
        )
    return UsagePolicy(
        allowed_for_runtime_planning=False,
        allowed_for_replay_fixture=False,
        allowed_for_ontology=False,
        allowed_for_query_planning=False,
        allowed_for_red_team_planning=False,
    )


def source_url_status(data: Mapping[str, Any], text: str = "") -> str:
    if _first_url(data, text):
        return "present"
    haystack = _haystack(data, text)
    if "evidence_url_pending" in haystack or "url pending" in haystack:
        return "pending"
    if "source_url" in haystack or "evidence_url" in haystack:
        return "missing"
    return "not_applicable"


def first_url(data: Mapping[str, Any], text: str = "") -> str | None:
    return _first_url(data, text)


def _first_url(data: Mapping[str, Any], text: str = "") -> str | None:
    for key in ("source_url", "evidence_url", "url", "canonical_url"):
        value = data.get(key)
        if isinstance(value, str) and value.startswith(("http://", "https://")):
            return value
    match = _URL_RE.search(text)
    return match.group(0) if match else None


def _haystack(data: Mapping[str, Any], text: str) -> str:
    try:
        items = " ".join(f"{key}={value}" for key, value in data.items())
    except Exception:
        items = str(data)
    return f"{items} {text}".lower()


def _boolish(value: Any) -> bool:
    if isinstance(value, bool):
        return value
    if isinstance(value, (int, float)):
        return value != 0
    if isinstance(value, str):
        return value.strip().lower() in {"1", "true", "yes", "y"}
    return False


__all__ = ["classify_source_quality", "first_url", "source_url_status", "usage_policy_for_quality"]
