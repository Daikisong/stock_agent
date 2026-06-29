"""Archetype routing correctness for Research Brain v2."""

from __future__ import annotations

import json
import math
import re
from pathlib import Path
from typing import Any, Mapping, Sequence

from e2r.calibration.taxonomy import CANONICAL_ARCHETYPE_IDS
from e2r.research_brain.v2_schemas import (
    ArchetypeMemoryCard,
    ArchetypeRouteCandidate,
    ArchetypeRouteResult,
    CandidateEventV2,
    RouterConfidence,
)


_TOKEN_RE = re.compile(r"[a-zA-Z0-9가-힣]+")
_R13_PREFIX = "R13_"
_EXPLICIT_R13_TERMS = {
    "cross",
    "redteam",
    "red",
    "team",
    "false",
    "positive",
    "review",
    "guardrail",
    "accounting",
    "trust",
    "validation",
    "mae",
}
_R13_OVERLAY_TERMS = {"false", "positive", "red", "team", "risk", "guard", "hard", "break", "overheat"}
_ROUTER_STOPWORDS = {
    "event",
    "operating",
    "mechanism",
    "manual",
    "none",
    "source",
    "row",
    "candidate",
    "unclear",
    "fixture",
    "other",
    "with",
    "from",
    "review",
}


def route_candidate_event_v2(
    event: CandidateEventV2,
    cards: Sequence[ArchetypeMemoryCard],
    *,
    top_k: int = 3,
) -> ArchetypeRouteResult:
    card_by_id = {card.archetype_id: card for card in cards}
    event_tokens = _event_tokens(event)
    explicit_r13 = _is_explicit_r13_event(event_tokens, event)
    scored = []
    for card in cards:
        score, reason = _score_card(card, event_tokens, explicit_r13=explicit_r13)
        scored.append((score, card.archetype_id, reason))
    scored.sort(key=lambda item: (item[0], item[1]), reverse=True)
    if not explicit_r13:
        non_r13 = [item for item in scored if not item[1].startswith(_R13_PREFIX)]
        r13 = [item for item in scored if item[1].startswith(_R13_PREFIX)]
        scored = non_r13 + r13
    top = scored[: max(1, top_k)]
    best_score, primary, best_reason = top[0]
    second_score = top[1][0] if len(top) > 1 else 0.0
    confidence = _confidence(best_score, second_score)
    status = "ROUTED" if confidence != RouterConfidence.LOW.value else "ARCTYPE_PENDING_DISAMBIGUATION"
    if status != "ROUTED":
        primary_value: str | None = None
    else:
        primary_value = primary
    overlays = _secondary_r13_overlays(event_tokens, scored, primary_value, explicit_r13)
    top_candidates = tuple(
        ArchetypeRouteCandidate(
            archetype_id=archetype_id,
            probability_or_score=round(score, 6),
            reason=reason,
        )
        for score, archetype_id, reason in top
    )
    why_not = tuple(
        f"{candidate.archetype_id} scored lower than {primary_value or 'unrouted'}: {candidate.reason}"
        for candidate in top_candidates[1:]
    )
    disambiguation = ()
    if status != "ROUTED":
        disambiguation = tuple(f"compare {item[1]} mechanism with event evidence" for item in top[:3])
    return ArchetypeRouteResult(
        primary_archetype=primary_value,
        top_k_archetypes=top_candidates,
        router_confidence=confidence,
        status=status,
        why_not_other_top_archetypes=why_not,
        required_disambiguation_tasks=disambiguation,
        secondary_overlays=overlays,
        r13_primary_allowed=explicit_r13,
    )


def build_router_confusion_matrix(cards: Sequence[ArchetypeMemoryCard]) -> Mapping[str, Any]:
    fixtures = build_router_fixtures(cards)
    rows = []
    top1 = 0
    top3 = 0
    r13_overroute = 0
    mandatory = {
        "C06_HBM_MEMORY_CUSTOMER_CAPACITY",
        "C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY",
        "C15_MATERIAL_SPREAD_SUPERCYCLE",
        "C17_CHEMICAL_COMMODITY_MARGIN_SPREAD",
        "C24_BIO_TRIAL_DATA_EVENT_RISK",
        "C28_SOFTWARE_SECURITY_CONTRACT_RETENTION",
    }
    mandatory_rows = {}
    for fixture in fixtures:
        route = route_candidate_event_v2(fixture["event"], cards)
        expected = fixture["expected_archetype"]
        top_ids = [item.archetype_id for item in route.top_k_archetypes]
        top1_ok = route.primary_archetype == expected
        top3_ok = expected in top_ids
        explicit_r13 = fixture["explicit_r13"]
        overroute = bool(
            route.primary_archetype
            and route.primary_archetype.startswith(_R13_PREFIX)
            and not str(expected).startswith(_R13_PREFIX)
            and not explicit_r13
        )
        top1 += int(top1_ok)
        top3 += int(top3_ok)
        r13_overroute += int(overroute)
        row = {
            "fixture_id": fixture["fixture_id"],
            "expected_archetype": expected,
            "primary_archetype": route.primary_archetype,
            "top3_archetypes": top_ids,
            "router_confidence": route.router_confidence,
            "status": route.status,
            "top1_exact_match": top1_ok,
            "top3_contains_expected": top3_ok,
            "explicit_r13_fixture": explicit_r13,
            "r13_overroute": overroute,
            "secondary_overlays": list(route.secondary_overlays),
        }
        if expected in mandatory:
            mandatory_rows[expected] = row
        rows.append(row)
    count = len(rows)
    mandatory_pass = all(mandatory_rows.get(item, {}).get("top1_exact_match") for item in mandatory)
    return {
        "schema_version": "research_brain_v2_archetype_router_confusion_matrix",
        "summary": {
            "fixture_count": count,
            "top1_accuracy": round(top1 / count, 6) if count else 0.0,
            "top3_accuracy": round(top3 / count, 6) if count else 0.0,
            "top1_correct_count": top1,
            "top3_correct_count": top3,
            "r13_overroute_count": r13_overroute,
            "mandatory_six_top1_pass": mandatory_pass,
            "mandatory_six_results": mandatory_rows,
        },
        "rows": rows,
    }


def build_router_fixtures(cards: Sequence[ArchetypeMemoryCard]) -> tuple[Mapping[str, Any], ...]:
    fixtures = []
    for card in cards:
        explicit_r13 = card.archetype_id.startswith(_R13_PREFIX)
        summary = _fixture_summary(card, explicit_r13=explicit_r13)
        event = CandidateEventV2(
            candidate_event_id=f"ROUTE-{card.archetype_id}",
            symbol=f"RT{len(fixtures):04d}",
            company_name=f"Route Fixture {card.archetype_id}",
            event_date="2026-06-29",
            detected_at="2026-06-29",
            source_family="ReplayFixture",
            source_id=card.archetype_id,
            event_type="red_team_review" if explicit_r13 else "operating_event",
            raw_reason_codes=(card.archetype_id, "EXPLICIT_R13_REVIEW") if explicit_r13 else (card.archetype_id,),
            event_title=card.canonical_mechanism,
            event_summary=summary,
            issuer_directness="DIRECT",
            initial_evidence_document_ids=(f"fixture:{card.archetype_id}",),
        )
        fixtures.append(
            {
                "fixture_id": f"FIX-{card.archetype_id}",
                "expected_archetype": card.archetype_id,
                "explicit_r13": explicit_r13,
                "event": event,
            }
        )
    return tuple(fixtures)


def write_router_confusion_matrix(matrix: Mapping[str, Any], output_directory: str | Path) -> Path:
    path = Path(output_directory) / "research_brain_v2_archetype_router_confusion_matrix.json"
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(matrix, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    return path


def _score_card(card: ArchetypeMemoryCard, event_tokens: set[str], *, explicit_r13: bool) -> tuple[float, str]:
    card_tokens = _card_tokens(card)
    overlap = event_tokens & card_tokens
    score = float(len(overlap))
    id_tokens = set(_tokens(card.archetype_id))
    id_overlap = event_tokens & id_tokens
    score += len(id_overlap) * 2.5
    primitive_overlap = event_tokens & set(token for primitive in card.required_primitives for token in _tokens(primitive))
    score += len(primitive_overlap) * 1.2
    if card.archetype_id == "C15_MATERIAL_SPREAD_SUPERCYCLE" and {"material", "spread"} <= event_tokens:
        score += 4.0
        if "supercycle" in event_tokens:
            score += 3.0
    if card.archetype_id == "C17_CHEMICAL_COMMODITY_MARGIN_SPREAD" and {"chemical", "spread"} <= event_tokens:
        score += 4.0
    if card.archetype_id.startswith(_R13_PREFIX):
        if explicit_r13:
            score += 10.0
        else:
            score -= 10.0
    reason = f"overlap={len(overlap)}, id_overlap={len(id_overlap)}, primitive_overlap={len(primitive_overlap)}"
    return score, reason


def _confidence(best: float, second: float) -> str:
    if best < 2.0:
        return RouterConfidence.LOW.value
    if best >= 8.0 and best - second >= 2.0:
        return RouterConfidence.HIGH.value
    return RouterConfidence.MEDIUM.value


def _event_tokens(event: CandidateEventV2) -> set[str]:
    payload = " ".join(
        [
            event.event_type,
            event.source_family,
            event.source_id,
            " ".join(event.raw_reason_codes),
            event.primary_disclosure_type or "",
            event.event_title,
            event.event_summary,
            json.dumps(event.structured_payload, ensure_ascii=False, sort_keys=True),
        ]
    )
    return set(_tokens(payload))


def _card_tokens(card: ArchetypeMemoryCard) -> set[str]:
    parts = [
        card.archetype_id,
        card.canonical_mechanism,
        " ".join(card.stage2_unlocks),
        " ".join(card.green_unlocks),
        " ".join(card.green_blockers),
        " ".join(card.false_positive_patterns),
        " ".join(card.required_primitives),
        " ".join(card.query_intent_patterns),
    ]
    return set(_tokens(" ".join(parts)))


def _tokens(text: str) -> tuple[str, ...]:
    return tuple(
        token.lower()
        for token in _TOKEN_RE.findall(text)
        if len(token) > 1 and token.lower() not in _ROUTER_STOPWORDS
    )


def _is_explicit_r13_event(event_tokens: set[str], event: CandidateEventV2) -> bool:
    text = " ".join(event_tokens)
    if event.event_type in {"red_team_review", "cross_archetype_review", "false_positive_review"}:
        return True
    if any(code.startswith("R13_") or code == "EXPLICIT_R13_REVIEW" for code in event.raw_reason_codes):
        return True
    return len(event_tokens & _EXPLICIT_R13_TERMS) >= 4 and "review" in event_tokens


def _secondary_r13_overlays(
    event_tokens: set[str],
    scored: Sequence[tuple[float, str, str]],
    primary: str | None,
    explicit_r13: bool,
) -> tuple[str, ...]:
    if explicit_r13 or not primary or primary.startswith(_R13_PREFIX):
        return ()
    if not event_tokens & _R13_OVERLAY_TERMS:
        return ()
    overlays = [archetype_id for _, archetype_id, _ in scored if archetype_id.startswith(_R13_PREFIX)]
    return tuple(overlays[:2])


def _fixture_summary(card: ArchetypeMemoryCard, *, explicit_r13: bool) -> str:
    if explicit_r13:
        return f"explicit cross archetype red team review for {card.archetype_id}: {card.canonical_mechanism}"
    return " ".join(
        item
        for item in (
            card.archetype_id,
            card.canonical_mechanism,
            " ".join(card.stage2_unlocks[:4]),
            " ".join(card.required_primitives[:4]),
        )
        if item
    )


__all__ = [
    "build_router_confusion_matrix",
    "build_router_fixtures",
    "route_candidate_event_v2",
    "write_router_confusion_matrix",
]
