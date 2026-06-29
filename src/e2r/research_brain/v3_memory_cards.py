"""Research Brain v3 memory-card distillation reports."""

from __future__ import annotations

import hashlib
from dataclasses import asdict, dataclass, field
from datetime import datetime, timezone
from typing import Any, Mapping, Sequence

from e2r.research_brain.v2_schemas import ArchetypeMemoryCard, _json_safe


@dataclass(frozen=True)
class ArchetypeMemoryCardV3:
    archetype_id: str
    large_sector_id: str | None
    seed_rules: tuple[str, ...]
    data_distilled_rules: tuple[str, ...]
    conflict_summary: tuple[str, ...] = ()
    source_quality_weighted_patterns: Mapping[str, Any] = field(default_factory=dict)
    url_backed_supporting_records: tuple[str, ...] = ()
    source_proxy_supporting_records: tuple[str, ...] = ()
    price_path_only_warning_records: tuple[str, ...] = ()
    source_gap: tuple[str, ...] = ()
    confidence: str = "MEDIUM"
    last_compiled_at: str = ""
    compile_input_hash: str = ""

    def to_dict(self) -> dict[str, Any]:
        return _json_safe(asdict(self))


def distill_memory_cards_v3(cards: Sequence[ArchetypeMemoryCard]) -> tuple[ArchetypeMemoryCardV3, ...]:
    compiled_at = datetime.now(timezone.utc).replace(microsecond=0).isoformat()
    return tuple(_distill_card(card, compiled_at=compiled_at) for card in cards)


def build_memory_card_distillation_report_v3(cards: Sequence[ArchetypeMemoryCardV3]) -> Mapping[str, Any]:
    return {
        "schema_version": "research_brain_v3_memory_card_distillation_report",
        "summary": {
            "card_count": len(cards),
            "cards_with_data_distilled_rules": sum(bool(card.data_distilled_rules) for card in cards),
            "source_proxy_positive_unlock_count": 0,
            "card_with_source_gap_count": sum(bool(card.source_gap) for card in cards),
        },
        "cards": [card.to_dict() for card in cards],
    }


def build_memory_card_conflicts_report_v3(cards: Sequence[ArchetypeMemoryCardV3]) -> Mapping[str, Any]:
    rows = [
        {
            "archetype_id": card.archetype_id,
            "conflict_summary": list(card.conflict_summary),
            "source_gap": list(card.source_gap),
        }
        for card in cards
        if card.conflict_summary or card.source_gap
    ]
    return {
        "schema_version": "research_brain_v3_memory_card_conflicts",
        "summary": {
            "conflict_or_gap_row_count": len(rows),
            "conflict_count": sum(bool(row["conflict_summary"]) for row in rows),
            "source_gap_count": sum(bool(row["source_gap"]) for row in rows),
        },
        "rows": rows,
    }


def _distill_card(card: ArchetypeMemoryCard, *, compiled_at: str) -> ArchetypeMemoryCardV3:
    seed_rules = tuple(
        dict.fromkeys(
            (
                *card.stage2_unlocks[:4],
                *card.green_blockers[:4],
                *card.false_positive_patterns[:4],
            )
        )
    )
    data_rules = tuple(
        dict.fromkeys(
            (
                *(f"required primitive: {item}" for item in card.required_primitives[:6]),
                *(f"route via {primitive}: {', '.join(routes)}" for primitive, routes in list(card.source_route_by_primitive.items())[:3]),
                "source-backed records have higher prompt weight than source proxy rows",
                "price-path-only records can create guard warnings but not positive unlocks",
            )
        )
    )
    quality = dict(card.quality_breakdown)
    conflicts = []
    if card.representative_source_proxy_ontology_ids and not card.representative_url_backed_fixture_ids:
        conflicts.append("proxy_only_patterns_cannot_unlock_positive_stage")
    if quality.get("price_path_only_count", 0):
        conflicts.append("price_path_only_records_are_guard_only")
    source_gap = tuple(card.source_gaps) or (() if card.representative_url_backed_fixture_ids else ("url_backed_support_gap",))
    input_hash = hashlib.sha256(repr(card.to_dict()).encode("utf-8")).hexdigest()
    return ArchetypeMemoryCardV3(
        archetype_id=card.archetype_id,
        large_sector_id=card.large_sector_id,
        seed_rules=seed_rules,
        data_distilled_rules=data_rules,
        conflict_summary=tuple(dict.fromkeys(conflicts)),
        source_quality_weighted_patterns=quality,
        url_backed_supporting_records=card.representative_url_backed_fixture_ids,
        source_proxy_supporting_records=card.representative_source_proxy_ontology_ids,
        price_path_only_warning_records=(),
        source_gap=source_gap,
        confidence=card.confidence,
        last_compiled_at=compiled_at,
        compile_input_hash=input_hash,
    )


__all__ = [
    "ArchetypeMemoryCardV3",
    "build_memory_card_conflicts_report_v3",
    "build_memory_card_distillation_report_v3",
    "distill_memory_cards_v3",
]
