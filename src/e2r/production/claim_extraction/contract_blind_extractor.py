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
    "base_stage",
    "verified_score",
    "current_score_eligible",
    "hard_break",
    "hard_break_final",
    "verified",
    "verified_final",
    "failed_green_gate",
    "green_gate",
    "stage_gate",
    "desired_primitive",
    "primitive_gap",
    "missing_primitive",
    "missing_primitives",
    "target_score",
    "score_gap_context",
    "materiality_remaining_points",
    "mfe",
    "mae",
    "outcome_label",
    "source_tier",
    "current_validity",
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
        last_subject: str | None = None
        for sentence in _sentences(text):
            explicit_subject = _subject_for_sentence(sentence, request.target_aliases)
            subject = explicit_subject
            uncertainty_reason = None if subject else "subject_not_explicit_in_sentence"
            if explicit_subject:
                last_subject = explicit_subject
            elif last_subject and _sentence_can_inherit_subject(sentence):
                subject = last_subject
                uncertainty_reason = "subject_resolved_from_previous_sentence"
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
                    uncertainty_reason=uncertainty_reason,
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
    accounting_subject = _accounting_subject_for_sentence(sentence)
    if accounting_subject and accounting_subject not in set(aliases):
        return accounting_subject
    for alias in aliases:
        if alias and alias in sentence:
            return alias
    return None


def _accounting_subject_for_sentence(sentence: str) -> str | None:
    if not any(token in sentence for token in ("감사의견", "회계", "적정", "부적정", "의견거절")):
        return None
    match = re.search(r"([A-Za-z0-9가-힣&().·ㆍ -]{2,30}?)(?:은|는|의)\s*.{0,40}?(?:감사의견|회계|적정|부적정|의견거절)", sentence)
    if not match:
        return None
    subject = match.group(1).strip(" ,.:;()[]")
    if not subject:
        return None
    return subject


def _sentence_can_inherit_subject(sentence: str) -> bool:
    lower = sentence.lower()
    return _has_any(
        lower,
        (
            "the company",
            "the firm",
            "operating profit",
            "operating income",
            "net profit",
            "net income",
            "record profit",
            "sales rose",
            "revenue",
            "영업이익",
            "순이익",
            "매출",
            "utilization",
            "capacity utilization",
            "cdu",
            "rfcc",
            "inventory",
            "재고",
            "가동률",
            "phase",
            "trial",
            "clinical",
            "endpoint",
            "response",
            "safety",
            "batoclimab",
            "pexa-vec",
            "futility",
            "discontinuation",
            "primary objective",
            "enrollment",
            "임상",
            "안전성",
            "유효성",
            "중단",
            "annual recurring revenue",
            "arr",
            "dollar-based net retention",
            "net retention",
            "renewal",
            "renewals",
            "renewal contract",
            "churn",
            "subscription revenue",
            "subscription customer",
            "subscription agreement",
            "deferred revenue",
            "remaining performance obligation",
            "remaining performance obligations",
            "rpo",
            "subscription gross margin",
            "gross margin",
        ),
    )


def _polarity_for_sentence(sentence: str) -> str:
    lower = sentence.lower()
    if any(
        token in lower
        for token in (
            "turn to profit",
            "turned to profit",
            "earnings turnaround",
            "loss narrowed",
            "losses narrowed",
            "improved",
            "recovered",
        )
    ):
        return "POSITIVE"
    if any(token in lower for token in ("아니다", "않았다", "취소", "하향", "감소", "부적정", "의견거절", "negative", "cancel")):
        return "NEGATIVE"
    if any(
        token in lower
        for token in ("loss widened", "losses widened", "loss expanded", "losses expanded", "operating loss", "falling", "lower crude", "lower prices")
    ):
        return "NEGATIVE"
    if re.search(r"(?:^|\s)-\d+(?:\.\d+)?\s*(?:bil|billion|억원|십억)", lower):
        return "NEGATIVE"
    if any(token in lower for token in ("감사의견은 적정", "적정의견", "적정 의견", "문제 없음", "해소", "정상")):
        return "NORMAL"
    if any(
        token in lower
        for token in (
            "상향",
            "증가",
            "확대",
            "계약",
            "수주",
            "배정",
            "확인",
            "진행",
            "공급",
            "sold out",
            "pre-sold",
            "positive",
            "raise",
            "growth",
            "turnaround",
            "positive initial results",
            "meaningfully exceeded",
            "exceeded 50%",
            "normalization",
            "well tolerated",
            "no new safety signals",
            "statistically significant",
            "p=0.",
            "annual recurring revenue",
            "net new arr",
            "net retention",
            "renewal",
            "renewals",
            "subscription gross margin",
            "deferred revenue",
        )
    ):
        return "POSITIVE"
    if any(
        token in lower
        for token in (
            "futility",
            "recommended discontinuation",
            "discontinuation of the trial",
            "unlikely to meet",
            "failed to meet",
            "did not meet",
            "missed the primary endpoint",
            "enrollment is being stopped",
            "clinical hold",
            "complete response letter",
            "crl",
        )
    ):
        return "NEGATIVE"
    return "MIXED"


def _predicate_for_sentence(sentence: str) -> str:
    lower = sentence.lower()
    if _has_any(lower, ("hbm", "qualification", "고객 배정", "고객사", "고객")) and _has_any(
        lower,
        ("hbm", "qualification", "배정", "공급", "수요", "customer", "allocation"),
    ):
        return "customer_allocation_or_qualification_claim"
    if _has_capacity_allocation_language(lower) and _has_capacity_subject_language(lower):
        return "capacity_allocation_claim"
    if any(token in lower for token in ("계약", "수주", "supply agreement", "order")):
        return "contract_or_order_claim"
    if _is_software_arr_growth_claim(lower):
        return "software_arr_growth_claim"
    if _is_software_net_retention_claim(lower):
        return "software_net_retention_claim"
    if _is_software_renewal_or_churn_claim(lower):
        return "software_renewal_or_churn_claim"
    if _is_software_rpo_or_deferred_revenue_claim(lower):
        return "software_rpo_or_deferred_revenue_claim"
    if _is_software_recurring_margin_claim(lower):
        return "software_recurring_margin_claim"
    if _is_raw_commodity_price_headline(lower):
        return "raw_commodity_price_headline_claim"
    if _is_material_spread_expansion_claim(lower):
        return "material_spread_expansion_claim"
    if _is_material_pricing_power_claim(lower):
        return "material_pricing_power_claim"
    if _is_utilization_or_volume_claim(lower):
        return "utilization_or_volume_claim"
    if _is_inventory_cycle_claim(lower):
        return "inventory_cycle_claim"
    if _is_material_profitability_bridge_claim(lower):
        return "material_profitability_bridge_claim"
    if _is_bio_binary_event_risk_claim(lower):
        return "bio_binary_event_risk_claim"
    if _is_bio_approval_not_confirmed_claim(lower):
        return "bio_approval_not_confirmed_claim"
    if _is_bio_safety_signal_claim(lower):
        return "bio_safety_signal_claim"
    if _is_cash_runway_risk_claim(lower):
        return "cash_runway_risk_claim"
    if _is_bio_trial_quality_claim(lower):
        return "bio_trial_quality_claim"
    if _has_any(lower, ("고객사 다변화", "고객사 확보", "신규 고객", "다수의 반도체 고객", "customer diversification")):
        return "customer_diversification_claim"
    if _has_any(lower, ("업무협약", "mou", "공동 개발", "공동 평가", "qualification", "신뢰성 평가를 위한 업무")) and _has_any(
        lower,
        ("고객", "리벨리온", "fabless", "팹리스", "반도체"),
    ):
        return "customer_quality_or_qualification_claim"
    if _has_any(
        lower,
        (
            "신뢰성 평가",
            "신뢰성 테스트",
            "종합 분석",
            "테스트 서비스",
            "test service",
            "reliability test",
            "failure analysis",
            "고장 분석",
            "불량 분석",
            "품질과 신뢰성",
            "프로브카드",
            "probe card",
            "test socket",
            "테스트 소켓",
            "세라믹stf",
            "ceramic stf",
        ),
    ):
        return "semiconductor_test_profile_claim"
    if any(token in lower for token in ("유상증자", "자기주식", "배당", "증권발행")):
        return "capital_event_claim"
    if any(token in lower for token in ("신규시설투자", "시설투자", "설비투자")):
        return "capacity_investment_claim"
    if any(token in lower for token in ("eps", "목표주가", "상향", "컨센서스", "revision")):
        return "revision_claim"
    if any(token in lower for token in ("감사의견", "적정", "부적정", "의견거절", "회계")):
        return "audit_or_accounting_claim"
    if any(token in lower for token in ("영업이익", "fcf", "현금흐름", "마진", "margin")):
        return "profitability_or_cash_claim"
    if "opendart" in lower and ("접수번호" in sentence or "disclosure" in lower or "공시" in sentence):
        return "official_document_fact"
    return "mention_only"


def _has_any(text: str, needles: tuple[str, ...]) -> bool:
    return any(needle.lower() in text for needle in needles)


def _is_material_pricing_power_claim(text: str) -> bool:
    return _has_any(
        text,
        (
            "price hikes of its products",
            "product price increase",
            "product price edged up",
            "sales price hike",
            "sales price up",
            "selling price",
            "asp increase",
            "price pass-through",
            "cost pass-through",
            "판가 인상",
            "가격 전가",
            "판매단가",
            "제품 가격",
        ),
    )


def _is_material_spread_expansion_claim(text: str) -> bool:
    has_margin_or_spread = _has_any(
        text,
        (
            "cracking margin",
            "strong margins",
            "refining margins",
            "margin improved",
            "margin improvement",
            "spread widened",
            "spread expansion",
            "spread improved",
            "스프레드 확대",
            "마진 개선",
        ),
    )
    has_price_cost_bridge = _has_any(text, ("product price", "sales price", "selling price", "제품 가격", "판매단가")) and _has_any(
        text,
        ("raw material", "input cost", "cost increase", "원재료", "원가"),
    )
    return has_margin_or_spread or has_price_cost_bridge


def _is_material_profitability_bridge_claim(text: str) -> bool:
    return _has_any(
        text,
        (
            "operating profit",
            "operating income",
            "net profit",
            "net income",
            "bottom line",
            "sales rose",
            "revenue",
            "영업이익",
            "순이익",
            "매출",
        ),
    ) and _has_any(
        text,
        (
            "price",
            "margin",
            "demand",
            "sales",
            "revenue",
            "profit",
            "income",
            "가격",
            "마진",
            "수요",
            "매출",
            "이익",
        ),
    )


def _is_utilization_or_volume_claim(text: str) -> bool:
    return _has_any(
        text,
        (
            "utilization rate",
            "capacity utilization",
            "operated at",
            "cdu",
            "rfcc",
            "hyc",
            "px plants",
            "lube plants",
            "가동률",
        ),
    )


def _is_inventory_cycle_claim(text: str) -> bool:
    return _has_any(
        text,
        (
            "inventory-related impact",
            "inventory related impact",
            "inventory valuation",
            "inventory and lagging impact",
            "a/r & inventory",
            "working capital",
            "재고평가",
            "재고",
            "운전자본",
        ),
    )


def _is_raw_commodity_price_headline(text: str) -> bool:
    has_raw_material = _has_any(
        text,
        (
            "copper price",
            "copper prices",
            "iron ore",
            "coking coal",
            "aluminium price",
            "aluminum price",
            "nickel price",
            "zinc price",
            "lithium price",
            "oil prices",
            "cement prices",
            "raw material prices",
            "원자재 가격",
            "구리 가격",
            "철광석",
        ),
    )
    has_issuer_bridge = _has_any(
        text,
        (
            "operating profit",
            "operating income",
            "net profit",
            "net income",
            "bottom line",
            "product price",
            "sales price",
            "price hikes of its products",
            "strong margins",
            "cracking margin",
            "영업이익",
            "순이익",
            "판가",
            "마진",
        ),
    )
    return has_raw_material and not has_issuer_bridge


def _is_bio_trial_quality_claim(text: str) -> bool:
    has_trial_context = _has_any(
        text,
        (
            "phase 1",
            "phase 2",
            "phase 3",
            "clinical trial",
            "proof-of-concept trial",
            "trial",
            "study",
            "임상",
        ),
    )
    has_quality_signal = _has_any(
        text,
        (
            "endpoint",
            "primary endpoint",
            "secondary endpoint",
            "response rate",
            "response rates",
            "treatment response",
            "efficacy",
            "safety",
            "normalization",
            "statistically significant",
            "p=",
            "dose response",
            "reduction",
            "well tolerated",
            "no new safety signals",
            "유효성",
            "안전성",
            "반응률",
            "평가지표",
        ),
    )
    has_positive_signal = _has_any(
        text,
        (
            "positive initial results",
            "meaningfully exceeded",
            "exceeded 50%",
            "achieved response",
            "showed an impressive reduction",
            "demonstrated",
            "statistically significant",
            "well tolerated",
            "no new safety signals",
            "긍정",
            "유의",
        ),
    )
    return has_trial_context and has_quality_signal and has_positive_signal


def _is_bio_binary_event_risk_claim(text: str) -> bool:
    return _has_any(
        text,
        (
            "futility analysis",
            "recommended discontinuation",
            "discontinuation of the trial",
            "unlikely to meet the primary objective",
            "unlikely to meet its primary objective",
            "failed to meet the primary endpoint",
            "failed to meet its primary endpoint",
            "did not meet the primary endpoint",
            "missed the primary endpoint",
            "enrollment is being stopped",
            "terminated early",
            "trial failure",
            "임상 중단",
            "임상 실패",
            "주평가지표 미충족",
        ),
    )


def _is_bio_approval_not_confirmed_claim(text: str) -> bool:
    return _has_any(
        text,
        (
            "complete response letter",
            " crl",
            "approval not confirmed",
            "resubmission",
            "re-submit",
            "regulatory path",
            "regulatory pathway",
            "보완요구",
            "허가 반려",
            "재제출",
        ),
    )


def _is_bio_safety_signal_claim(text: str) -> bool:
    if _has_any(text, ("no new safety signals", "not related to the safety")):
        return False
    return _has_any(
        text,
        (
            "safety signal",
            "safety concern",
            "serious adverse",
            "dose-limiting toxicity",
            "clinical hold",
            "toxicity",
            "안전성 우려",
            "중대한 이상반응",
        ),
    )


def _is_cash_runway_risk_claim(text: str) -> bool:
    return _has_any(
        text,
        (
            "cash runway",
            "going concern",
            "dilution",
            "financing risk",
            "capital raise",
            "funding runway",
            "현금 runway",
            "계속기업",
            "희석",
            "자금조달",
        ),
    )


def _is_software_arr_growth_claim(text: str) -> bool:
    return _has_any(text, ("annual recurring revenue", "ending arr", " net new arr", " arr ")) and _has_any(
        text,
        (
            "year-over-year",
            "yoy",
            "grew",
            "growth",
            "up ",
            "increased",
            "reported",
            "reach",
            "reached",
        ),
    )


def _is_software_net_retention_claim(text: str) -> bool:
    return _has_any(text, ("dollar-based net retention", "net retention rate", "nrr")) and _has_any(
        text,
        ("rate", "%", "renewals", "expansion", "contraction", "churn", "arr"),
    )


def _is_software_renewal_or_churn_claim(text: str) -> bool:
    return _has_any(text, ("renewal contract", "renewals", "renewal", "churn", "subscription agreement")) and _has_any(
        text,
        ("subscription", "customer", "contract", "term", "arr", "net retention"),
    )


def _is_software_rpo_or_deferred_revenue_claim(text: str) -> bool:
    return _has_any(text, ("remaining performance obligation", "remaining performance obligations", " rpo", "deferred revenue")) and _has_any(
        text,
        ("expected to be recorded as revenue", "recorded as revenue", "next 12 months", "subscription", "revenue"),
    )


def _is_software_recurring_margin_claim(text: str) -> bool:
    return _has_any(text, ("subscription gross margin", "subscription gross profit", "free cash flow", "operating cash flow")) and _has_any(
        text,
        ("subscription", "margin", "gross profit", "cash flow"),
    )


def _has_capacity_allocation_language(text: str) -> bool:
    return _has_any(text, ("sold out", "pre-sold", "선판매", "전량", "생산능력", "capacity")) or bool(
        re.search(r"\bcapa\b", text)
    )


def _has_capacity_subject_language(text: str) -> bool:
    return _has_any(text, ("hbm", "capacity", "생산능력")) or bool(re.search(r"\bcapa\b", text))


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
