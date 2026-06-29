"""Contract-blind raw assertion extraction.

The extractor deliberately does not receive a desired primitive or score gap.
It only turns source text into raw factual assertions.
"""

from __future__ import annotations

import hashlib
import re
from dataclasses import asdict, dataclass, field
from typing import Any, Mapping, Sequence


_FORBIDDEN_CONTEXT_KEYS = {
    "score",
    "stage",
    "failed_green_gate",
    "desired_primitive",
    "primitive_gap",
    "target_score",
    "mfe",
    "mae",
    "outcome_label",
}


@dataclass(frozen=True)
class ExtractionInput:
    target_entity_id: str
    target_aliases: tuple[str, ...]
    as_of_date: str
    document_id: str
    anchor_id: str
    source_text: str
    source_metadata: Mapping[str, Any] = field(default_factory=dict)
    extra_context: Mapping[str, Any] = field(default_factory=dict)


@dataclass(frozen=True)
class RawAssertionRecord:
    raw_assertion_id: str
    document_id: str
    anchor_id: str
    subject: str
    predicate: str
    object_text: str
    polarity_proposal: str
    modality: str
    event_date: str | None
    exact_quote: str
    related_entities: tuple[str, ...]
    uncertainty_reason: str | None = None

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


class ContractBlindRawAssertionExtractor:
    def extract(self, request: ExtractionInput) -> tuple[RawAssertionRecord, ...]:
        leaked = sorted(key for key in request.extra_context if key.lower() in _FORBIDDEN_CONTEXT_KEYS)
        if leaked:
            raise ValueError(f"contract-blind extractor received forbidden context: {', '.join(leaked)}")
        text = _clean(request.source_text)
        if not text:
            return ()
        assertions: list[RawAssertionRecord] = []
        for sentence in _sentences(text):
            subject = _subject_for_sentence(sentence, request.target_aliases)
            polarity = _polarity_for_sentence(sentence)
            predicate = _predicate_for_sentence(sentence)
            if predicate == "mention_only":
                continue
            assertion_id = _stable_id("RAWPROD", request.document_id, request.anchor_id, sentence, predicate)
            assertions.append(
                RawAssertionRecord(
                    raw_assertion_id=assertion_id,
                    document_id=request.document_id,
                    anchor_id=request.anchor_id,
                    subject=subject or "UNKNOWN",
                    predicate=predicate,
                    object_text=sentence,
                    polarity_proposal=polarity,
                    modality=_modality_for_sentence(sentence),
                    event_date=_date_in_text(sentence),
                    exact_quote=sentence,
                    related_entities=tuple(alias for alias in request.target_aliases if alias and alias in sentence),
                    uncertainty_reason=None if subject else "subject_not_explicit_in_sentence",
                )
            )
        return tuple(assertions)


def _clean(text: str) -> str:
    text = re.sub(r"<br\s*/?>", "\n", text, flags=re.IGNORECASE)
    text = re.sub(r"<[^>]+>", " ", text)
    return re.sub(r"\s+", " ", text).strip()


def _sentences(text: str) -> tuple[str, ...]:
    chunks = re.split(r"(?<=[.!?。])\s+|[▶\n\r]+", text)
    return tuple(chunk.strip()[:500] for chunk in chunks if len(chunk.strip()) >= 8)[:20]


def _subject_for_sentence(sentence: str, aliases: Sequence[str]) -> str | None:
    for alias in aliases:
        if alias and alias in sentence:
            return alias
    return None


def _polarity_for_sentence(sentence: str) -> str:
    lower = sentence.lower()
    if any(token in lower for token in ("아니다", "않았다", "취소", "하향", "감소", "부적정", "의견거절", "negative", "cancel")):
        return "NEGATIVE"
    if any(token in lower for token in ("상향", "증가", "확대", "계약", "수주", "적정", "positive", "raise", "growth")):
        return "POSITIVE"
    return "MIXED"


def _predicate_for_sentence(sentence: str) -> str:
    lower = sentence.lower()
    if any(token in lower for token in ("계약", "수주", "supply agreement", "order")):
        return "contract_or_order_claim"
    if any(token in lower for token in ("유상증자", "자기주식", "배당", "증권발행")):
        return "capital_event_claim"
    if any(token in lower for token in ("신규시설투자", "시설투자", "투자판단", "설비투자")):
        return "capacity_investment_claim"
    if any(token in lower for token in ("eps", "목표주가", "상향", "컨센서스", "revision")):
        return "revision_claim"
    if any(token in lower for token in ("감사의견", "적정", "부적정", "의견거절", "회계")):
        return "audit_or_accounting_claim"
    if any(token in lower for token in ("영업이익", "fcf", "현금흐름", "마진", "margin")):
        return "profitability_or_cash_claim"
    return "mention_only"


def _modality_for_sentence(sentence: str) -> str:
    lower = sentence.lower()
    if any(token in lower for token in ("예상", "전망", "guidance", "expected")):
        return "EXPECTED"
    if any(token in lower for token in ("확정", "공시", "reported", "confirmed")):
        return "CONFIRMED"
    return "STATED"


def _date_in_text(sentence: str) -> str | None:
    match = re.search(r"\b(20\d{2})[.\-/](\d{1,2})[.\-/](\d{1,2})\b", sentence)
    if not match:
        return None
    return f"{int(match.group(1)):04d}-{int(match.group(2)):02d}-{int(match.group(3)):02d}"


def _stable_id(prefix: str, *parts: object) -> str:
    digest = hashlib.sha256("|".join(str(part) for part in parts).encode("utf-8")).hexdigest()[:20]
    return f"{prefix}-{digest}"


__all__ = ["ContractBlindRawAssertionExtractor", "ExtractionInput", "RawAssertionRecord"]
