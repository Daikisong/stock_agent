"""ArchetypeMemoryCard generation for Research Brain v2."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Mapping, Sequence

from e2r.calibration.taxonomy import CANONICAL_ARCHETYPE_IDS, large_sector_for_archetype
from e2r.research_brain.v2_schemas import ArchetypeMemoryCard


_SEMANTIC_OVERRIDES: dict[str, Mapping[str, tuple[str, ...] | str]] = {
    "C06_HBM_MEMORY_CUSTOMER_CAPACITY": {
        "canonical_mechanism": "HBM memory customer allocation capacity sold-out qualification revenue mix shipment visibility",
        "stage2_unlocks": ("capacity sold-out", "customer allocation", "qualification pass", "HBM revenue mix", "shipment visibility"),
        "green_blockers": ("cashflow bridge", "repeat evidence family", "conventional memory drag"),
        "false_positive_patterns": ("package substrate sympathy", "qualification lag with reopen path", "HBM keyword only"),
        "four_c_hard_break_patterns": ("confirmed permanent customer loss", "confirmed cancellation"),
    },
    "C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY": {
        "canonical_mechanism": "semiconductor test socket customer quality named customer supply order margin bridge",
        "stage2_unlocks": ("named customer", "customer qualification", "supply order", "revenue conversion"),
        "green_blockers": ("repeat customer order", "margin bridge", "customer quality evidence"),
        "false_positive_patterns": ("product profile only", "award without customer order"),
    },
    "C15_MATERIAL_SPREAD_SUPERCYCLE": {
        "canonical_mechanism": "material spread supercycle pass-through inventory lag realized margin fcf revision",
        "stage2_unlocks": ("price pass-through", "realized spread", "inventory lag bridge", "margin conversion"),
        "green_blockers": ("FCF conversion", "EPS revision", "issuer-level pass-through"),
        "false_positive_patterns": ("raw commodity headline only", "price weather without issuer spread"),
    },
    "C17_CHEMICAL_COMMODITY_MARGIN_SPREAD": {
        "canonical_mechanism": "chemical commodity margin spread ASP raw material pass-through OPM FCF",
        "stage2_unlocks": ("chemical spread expansion", "ASP pass-through", "raw material cost lag", "OPM bridge"),
        "green_blockers": ("FCF bridge", "revision confirmation", "realized spread"),
        "false_positive_patterns": ("commodity price article only", "industry spread without issuer margin"),
    },
    "C24_BIO_TRIAL_DATA_EVENT_RISK": {
        "canonical_mechanism": "bio trial endpoint effect size safety regulatory approval partner runway binary event risk",
        "stage2_unlocks": ("trial endpoint", "effect size", "safety profile", "regulatory milestone"),
        "green_blockers": ("cash runway", "partner economics", "regulatory path"),
        "false_positive_patterns": ("trial headline without endpoint", "binary event without runway"),
    },
    "C28_SOFTWARE_SECURITY_CONTRACT_RETENTION": {
        "canonical_mechanism": "software security contract retention ARR RPO renewal churn recurring revenue margin cash durability",
        "stage2_unlocks": ("ARR growth", "RPO backlog", "renewal rate", "retention", "contract backlog"),
        "green_blockers": ("recurring revenue durability", "margin cash conversion", "churn evidence"),
        "false_positive_patterns": ("security theme spike", "software keyword without retention bridge"),
    },
}


def build_memory_cards_from_v1_matrix(v1_matrix: Mapping[str, Any]) -> tuple[ArchetypeMemoryCard, ...]:
    """Build deterministic v2 cards from the v1 profile matrix document."""

    rows_by_id = {
        str(row.get("canonical_archetype_id")): row
        for row in v1_matrix.get("rows", [])
        if row.get("canonical_archetype_id")
    }
    cards = []
    for archetype_id in CANONICAL_ARCHETYPE_IDS:
        row = rows_by_id.get(archetype_id, {})
        cards.append(build_memory_card(archetype_id, row))
    return tuple(cards)


def build_memory_card(archetype_id: str, profile_row: Mapping[str, Any] | None = None) -> ArchetypeMemoryCard:
    row = profile_row or {}
    override = _SEMANTIC_OVERRIDES.get(archetype_id, {})
    required = _strings(row.get("required_primitives_observed")) or _default_primitives(archetype_id)
    source_routes = _strings(row.get("source_routes")) or ("DART", "IR", "Official")
    quality_breakdown = _quality_breakdown(row)
    representative_url = _representative_ids(row, preferred_prefix="A", limit=12)
    representative_proxy = _representative_ids(row, preferred_prefix="C", limit=12)
    source_gaps = _strings(row.get("source_gap_summary"))
    runtime_usage_policy = str(row.get("runtime_usage_policy") or "planning_only").upper()
    if runtime_usage_policy == "READY" and not representative_url:
        runtime_usage_policy = "PLANNING_ONLY"
    return ArchetypeMemoryCard(
        archetype_id=archetype_id,
        large_sector_id=large_sector_for_archetype(archetype_id),
        generated_from_record_count=int(row.get("memory_record_count") or 0),
        quality_breakdown=quality_breakdown,
        canonical_mechanism=str(override.get("canonical_mechanism") or _mechanism_from_id(archetype_id)),
        stage2_unlocks=tuple(override.get("stage2_unlocks") or _strings(row.get("stage2_unlock_conditions")) or required[:6]),
        yellow_unlocks=_strings(row.get("yellow_blockers")),
        green_unlocks=tuple(item for item in required[:8] if item),
        green_blockers=tuple(override.get("green_blockers") or _strings(row.get("green_blockers"))),
        stage2_caps=_strings(row.get("stage2_cap_conditions")),
        false_positive_patterns=tuple(override.get("false_positive_patterns") or _strings(row.get("false_positive_patterns"))),
        four_b_watch_patterns=_strings(row.get("four_b_watch_conditions")),
        four_c_hard_break_patterns=tuple(
            override.get("four_c_hard_break_patterns") or _strings(row.get("four_c_thesis_break_conditions"))
        ),
        required_primitives=required,
        alternative_primitives=_strings(row.get("optional_primitives_observed")) or required,
        source_route_by_primitive={primitive: tuple(source_routes[:4]) for primitive in required[:16]},
        source_quorum_by_primitive={primitive: "one_official_or_two_independent_tier2" for primitive in required[:16]},
        do_not_promote_rules=_do_not_promote_rules(archetype_id, row, override),
        lifecycle_rules=_lifecycle_rules(archetype_id),
        query_intent_patterns=_strings(row.get("query_pattern_hints")),
        bad_query_patterns=_strings(row.get("bad_query_patterns")),
        representative_url_backed_fixture_ids=representative_url,
        representative_source_proxy_ontology_ids=representative_proxy,
        source_gaps=source_gaps,
        confidence=_confidence(row, representative_url),
        runtime_usage_policy=runtime_usage_policy,
    )


def write_memory_card_reports(
    *,
    cards: Sequence[ArchetypeMemoryCard],
    output_directory: str | Path,
) -> Mapping[str, Path]:
    output = Path(output_directory)
    output.mkdir(parents=True, exist_ok=True)
    cards_payload = {
        "schema_version": "research_brain_v2_memory_cards",
        "summary": {
            "card_count": len(cards),
            "ready_card_count": sum(card.runtime_usage_policy == "READY" for card in cards),
            "source_gap_count": sum(len(card.source_gaps) for card in cards),
        },
        "cards": [card.to_dict() for card in cards],
    }
    matrix = {
        "schema_version": "research_brain_v2_memory_card_matrix",
        "summary": cards_payload["summary"],
        "rows": [
            {
                "archetype_id": card.archetype_id,
                "large_sector_id": card.large_sector_id,
                "runtime_usage_policy": card.runtime_usage_policy,
                "confidence": card.confidence,
                "generated_from_record_count": card.generated_from_record_count,
                "required_primitive_count": len(card.required_primitives),
                "source_gap_count": len(card.source_gaps),
                "representative_url_backed_fixture_count": len(card.representative_url_backed_fixture_ids),
            }
            for card in cards
        ],
    }
    paths = {
        "memory_cards": output / "research_brain_v2_memory_cards.json",
        "memory_card_matrix": output / "research_brain_v2_memory_card_matrix.json",
    }
    paths["memory_cards"].write_text(json.dumps(cards_payload, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    paths["memory_card_matrix"].write_text(json.dumps(matrix, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    return paths


def _mechanism_from_id(archetype_id: str) -> str:
    return archetype_id.lower().replace("_", " ")


def _default_primitives(archetype_id: str) -> tuple[str, ...]:
    tokens = tuple(token.lower() for token in archetype_id.split("_") if len(token) > 1)
    return tuple(dict.fromkeys(tokens + ("source_quorum", "issuer_directness", "current_anchor")))


def _strings(value: Any, limit: int = 40) -> tuple[str, ...]:
    if value is None:
        return ()
    if isinstance(value, str):
        values = [value]
    else:
        values = [str(item) for item in value if item]
    return tuple(dict.fromkeys(item.strip() for item in values if item.strip()))[:limit]


def _quality_breakdown(row: Mapping[str, Any]) -> Mapping[str, int]:
    counts = row.get("source_quality_counts") or row.get("source_quality_class_counts") or {}
    if isinstance(counts, Mapping):
        converted = {str(key): int(value) for key, value in counts.items() if isinstance(value, (int, float))}
        if converted:
            return converted
    return {
        "url_backed_count": int(row.get("url_backed_count") or 0),
        "source_proxy_count": int(row.get("source_proxy_count") or 0),
        "price_path_only_count": int(row.get("price_path_only_count") or 0),
        "production_fixture_count": int(row.get("production_fixture_count") or 0),
        "ontology_only_count": int(row.get("ontology_only_count") or 0),
    }


def _representative_ids(row: Mapping[str, Any], *, preferred_prefix: str, limit: int) -> tuple[str, ...]:
    fixture_status = row.get("fixture_status") or {}
    seed = str(row.get("canonical_archetype_id") or "UNKNOWN")
    if preferred_prefix == "A" and fixture_status.get("positive_url_backed"):
        return tuple(f"{seed}:url_backed:{idx}" for idx in range(min(limit, 3)))
    if preferred_prefix == "C" and row.get("source_proxy_count"):
        return tuple(f"{seed}:source_proxy:{idx}" for idx in range(min(limit, 3)))
    return ()


def _do_not_promote_rules(archetype_id: str, row: Mapping[str, Any], override: Mapping[str, Any]) -> tuple[str, ...]:
    values = list(_strings(row.get("false_positive_patterns")))
    values.extend(str(item) for item in override.get("false_positive_patterns", ()) if item)
    values.append("Research Brain planning output is not score evidence until Evidence OS accepts source-backed claims.")
    if archetype_id.startswith("R13_"):
        values.append("R13 is a red-team overlay unless the candidate event is explicitly a red-team review event.")
    return tuple(dict.fromkeys(values))[:16]


def _lifecycle_rules(archetype_id: str) -> tuple[str, ...]:
    if "BIO" in archetype_id or "REGULATORY" in archetype_id:
        return ("trial/regulatory claims require latest current-status follow-up",)
    if "CONTRACT" in archetype_id or "BACKLOG" in archetype_id:
        return ("contract claims expire or supersede by cancellation, amendment, fulfillment, or period end",)
    if "SPREAD" in archetype_id or "MARGIN" in archetype_id:
        return ("commodity or spread claims must be bridged to issuer realized margin and current period",)
    return ("old claims require current/supersession check before score use",)


def _confidence(row: Mapping[str, Any], representative_url: Sequence[str]) -> str:
    record_count = int(row.get("memory_record_count") or 0)
    if representative_url and record_count >= 100:
        return "HIGH"
    if record_count:
        return "MEDIUM"
    return "LOW"


__all__ = ["build_memory_card", "build_memory_cards_from_v1_matrix", "write_memory_card_reports"]
