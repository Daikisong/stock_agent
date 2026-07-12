"""Material-relevance document ranking without a fixed top-N completion gate."""

from __future__ import annotations

import re
from dataclasses import dataclass
from datetime import date
from typing import Any, Mapping, Sequence

from .schemas import ComponentResearchPlan


@dataclass(frozen=True)
class DocumentRelevanceDecision:
    document_id: str
    material_relevance: bool
    relevance_score: float
    matched_research_questions: tuple[str, ...]
    reasons: tuple[str, ...]
    evidence_eligible: bool

    def to_dict(self) -> Mapping[str, Any]:
        return {
            "document_id": self.document_id,
            "material_relevance": self.material_relevance,
            "relevance_score": self.relevance_score,
            "matched_research_questions": list(self.matched_research_questions),
            "reasons": list(self.reasons),
            "evidence_eligible": self.evidence_eligible,
        }


class MaterialDocumentRanker:
    """Ranks every candidate and retains every material one.

    Token overlap is a retrieval signal only.  It never creates an
    EvidenceFact, a component point, absence, or completion decision.
    """

    def rank(
        self,
        *,
        target_id: str,
        as_of_date: str,
        documents: Sequence[Mapping[str, Any]],
        research_plans: Sequence[ComponentResearchPlan],
    ) -> tuple[DocumentRelevanceDecision, ...]:
        cutoff = date.fromisoformat(as_of_date)
        questions = tuple(
            dict.fromkeys(
                question
                for plan in research_plans
                for question in plan.research_questions
            )
        )
        question_tokens = {question: _tokens(question) for question in questions}
        decisions = []
        seen = set()
        for row in documents:
            document_id = str(
                row.get("document_id") or row.get("source_id") or ""
            ).strip()
            if not document_id:
                raise ValueError("document_id is required")
            if document_id in seen:
                raise ValueError("document ids must be unique")
            seen.add(document_id)
            content = str(
                row.get("full_text")
                or row.get("content")
                or row.get("body")
                or ""
            ).strip()
            is_snippet = bool(row.get("snippet_only")) or str(
                row.get("document_kind") or ""
            ).upper() in {"SNIPPET", "SEARCH_RESULT"}
            published = _published_date(row)
            future = bool(published and published > cutoff)
            row_target = str(row.get("target_id") or "").strip()
            target_match = row_target == target_id or target_id.lower() in content.lower()
            content_tokens = _tokens(content)
            matched = tuple(
                question
                for question, tokens in question_tokens.items()
                if tokens and len(tokens & content_tokens) / len(tokens) >= 0.20
            )
            source_tier = str(row.get("source_tier") or row.get("source_family") or "")
            authoritative = source_tier.upper() in {
                "ISSUER_OFFICIAL",
                "OFFICIAL_FILING",
                "CUSTOMER_OFFICIAL",
                "STRUCTURED",
                "TRUSTED_INDEPENDENT",
            }
            evidence_eligible = bool(content) and not is_snippet and not future
            score = (
                (0.35 if target_match else 0.0)
                + (0.35 * min(1.0, len(matched) / max(1, len(questions))))
                + (0.20 if authoritative else 0.0)
                + (0.10 if evidence_eligible else 0.0)
            )
            material = evidence_eligible and target_match and (
                bool(matched) or authoritative
            )
            reasons = []
            if future:
                reasons.append("FUTURE_DOCUMENT_EXCLUDED")
            if is_snippet:
                reasons.append("SNIPPET_DISCOVERY_ONLY")
            if not content:
                reasons.append("FULL_DOCUMENT_NOT_FETCHED")
            if not target_match:
                reasons.append("TARGET_SCOPE_NOT_ESTABLISHED")
            if matched:
                reasons.append("MATERIAL_RESEARCH_QUESTION_MATCH")
            if authoritative:
                reasons.append("AUTHORITATIVE_SOURCE_FAMILY")
            decisions.append(
                DocumentRelevanceDecision(
                    document_id=document_id,
                    material_relevance=material,
                    relevance_score=round(score, 6),
                    matched_research_questions=matched,
                    reasons=tuple(reasons),
                    evidence_eligible=evidence_eligible,
                )
            )
        return tuple(
            sorted(decisions, key=lambda row: (-row.relevance_score, row.document_id))
        )

    def select_material(
        self, decisions: Sequence[DocumentRelevanceDecision]
    ) -> tuple[str, ...]:
        """Return all material ids; deliberately no top_n parameter exists."""

        return tuple(
            row.document_id for row in decisions if row.material_relevance
        )


def _published_date(row: Mapping[str, Any]) -> date | None:
    raw = str(
        row.get("published_at")
        or row.get("publication_date")
        or row.get("filed_at")
        or ""
    ).strip()
    if not raw:
        return None
    try:
        return date.fromisoformat(raw[:10])
    except ValueError:
        return None


def _tokens(value: str) -> set[str]:
    return {
        token
        for token in re.findall(r"[0-9A-Za-z가-힣_]{2,}", value.lower())
        if token
    }


__all__ = ["DocumentRelevanceDecision", "MaterialDocumentRanker"]
