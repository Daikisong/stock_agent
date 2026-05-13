"""Cheap-scan event rules for Korea free official data."""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import date
from statistics import mean
from typing import Sequence

from e2r.models import DisclosureEvent, Evidence, FinancialActual, Instrument, PriceBar
from e2r.sources.kind import KINDConnector, KINDRiskRecord
from e2r.sources.opendart import OpenDARTConnector


POSITIVE_DISCLOSURE_CODES = frozenset(
    {
        "DISC_SUPPLY_CONTRACT",
        "DISC_LONG_TERM_CONTRACT",
        "DISC_CONTRACT_TO_SALES_10P",
        "DISC_FACILITY_INVESTMENT",
        "DISC_FACILITY_TO_MARKET_CAP_5P",
        "DISC_CAPA_INCREASE",
        "DISC_EARNINGS_PREANNOUNCE",
        "DISC_OP_YOY_100P",
        "DISC_BUYBACK_OR_CANCELLATION",
    }
)

NEGATIVE_RISK_CODES = frozenset(
    {
        "DISC_RIGHTS_OFFERING",
        "DISC_CONVERTIBLE_BOND",
        "DISC_BOND_WITH_WARRANT",
        "DISC_LAWSUIT",
        "DISC_AUDIT_OPINION_ISSUE",
        "DISC_TRADING_HALT",
        "DISC_MANAGED_ISSUE",
        "DISC_DELISTING_RISK",
        "DISC_CONTRACT_CANCEL_OR_DELAY",
        "RISK_MANAGED_ISSUE",
        "RISK_TRADING_HALT",
        "RISK_INVESTMENT_WARNING",
        "RISK_UNFAITHFUL_DISCLOSURE",
        "RISK_DELISTING",
    }
)


@dataclass(frozen=True)
class CheapScanRuleResult:
    """Rule scores and reason codes for one instrument."""

    reason_codes: tuple[str, ...] = field(default_factory=tuple)
    price_event_score: float = 0.0
    disclosure_event_score: float = 0.0
    financial_event_score: float = 0.0
    risk_event_score: float = 0.0
    evidence: tuple[Evidence, ...] = field(default_factory=tuple)
    dropped_reason: str | None = None


def evaluate_cheap_scan_rules(
    *,
    instrument: Instrument,
    as_of_date: date,
    price_bars: Sequence[PriceBar] = (),
    disclosures: Sequence[DisclosureEvent] = (),
    financial_actuals: Sequence[FinancialActual] = (),
    risk_records: Sequence[KINDRiskRecord] = (),
    local_universe_returns_60d: Sequence[float] = (),
) -> CheapScanRuleResult:
    """Evaluate deterministic cheap-scan rules for one Korean instrument."""

    codes: list[str] = []
    evidence: list[Evidence] = []
    disclosure_score = 0.0
    price_score = 0.0
    financial_score = 0.0
    risk_score = 0.0

    if instrument.is_managed:
        codes.append("RISK_MANAGED_ISSUE")
        risk_score = max(risk_score, 75.0)
    if instrument.is_trading_halt:
        codes.append("RISK_TRADING_HALT")
        risk_score = max(risk_score, 85.0)
    if instrument.is_invest_warning:
        codes.append("RISK_INVESTMENT_WARNING")
        risk_score = max(risk_score, 55.0)

    for disclosure in disclosures:
        disclosure_codes, positive_score, disclosure_risk_score = _disclosure_codes(disclosure)
        codes.extend(disclosure_codes)
        disclosure_score = max(disclosure_score, positive_score)
        risk_score = max(risk_score, disclosure_risk_score)
        evidence.append(OpenDARTConnector.to_evidence(disclosure, instrument.market))

    price_codes, price_score = _price_codes(price_bars, disclosures, local_universe_returns_60d)
    codes.extend(price_codes)

    financial_codes, financial_score = _financial_codes(financial_actuals)
    codes.extend(financial_codes)

    for record in risk_records:
        risk_codes, score = _risk_codes(record)
        codes.extend(risk_codes)
        risk_score = max(risk_score, score)
        if risk_codes:
            evidence.append(KINDConnector.to_evidence(record))

    dropped_reason = None
    if risk_score >= 80.0:
        dropped_reason = "hard_risk_status"

    return CheapScanRuleResult(
        reason_codes=tuple(dict.fromkeys(codes)),
        price_event_score=round(min(price_score, 100.0), 4),
        disclosure_event_score=round(min(disclosure_score, 100.0), 4),
        financial_event_score=round(min(financial_score, 100.0), 4),
        risk_event_score=round(min(risk_score, 100.0), 4),
        evidence=tuple(_dedupe_evidence(evidence)),
        dropped_reason=dropped_reason,
    )


def cheap_scan_total_score(result: CheapScanRuleResult) -> float:
    """Aggregate cheap scan scores without turning risk into a Green signal."""

    positive = (
        result.disclosure_event_score * 0.45
        + result.price_event_score * 0.25
        + result.financial_event_score * 0.30
    )
    risk_drag = min(result.risk_event_score * 0.35, 30.0)
    if result.risk_event_score >= 80.0:
        risk_drag = 45.0
    return round(max(0.0, min(100.0, positive - risk_drag)), 4)


def _disclosure_codes(disclosure: DisclosureEvent) -> tuple[tuple[str, ...], float, float]:
    fields = disclosure.parsed_fields
    haystack = f"{disclosure.title} {disclosure.report_type} {disclosure.raw_text or ''}"
    codes: list[str] = []
    positive_score = 0.0
    risk_score = 0.0

    if any(token in haystack for token in ("단일판매", "공급계약", "장기공급")):
        codes.append("DISC_SUPPLY_CONTRACT")
        positive_score += 30.0
    if _num(fields.get("contract_duration_months")) is not None and _num(fields.get("contract_duration_months")) >= 24:
        codes.append("DISC_LONG_TERM_CONTRACT")
        positive_score += 20.0
    if _num(fields.get("contract_amount_to_prior_sales")) is not None and _num(fields.get("contract_amount_to_prior_sales")) >= 0.10:
        codes.append("DISC_CONTRACT_TO_SALES_10P")
        positive_score += 20.0
    if "신규시설투자" in haystack:
        codes.append("DISC_FACILITY_INVESTMENT")
        positive_score += 25.0
    if _num(fields.get("facility_investment_to_market_cap")) is not None and _num(fields.get("facility_investment_to_market_cap")) >= 0.05:
        codes.append("DISC_FACILITY_TO_MARKET_CAP_5P")
        positive_score += 15.0
    if _num(fields.get("capa_increase_pct")) is not None or "CAPA" in haystack or "생산능력" in haystack:
        codes.append("DISC_CAPA_INCREASE")
        positive_score += 15.0
    if any(token in haystack for token in ("잠정실적", "영업실적 전망", "실적")):
        codes.append("DISC_EARNINGS_PREANNOUNCE")
        positive_score += 20.0
    if _num(fields.get("op_yoy_pct")) is not None and _num(fields.get("op_yoy_pct")) >= 100:
        codes.append("DISC_OP_YOY_100P")
        positive_score += 20.0
    if any(token in haystack for token in ("자기주식", "소각", "buyback", "cancellation")):
        codes.append("DISC_BUYBACK_OR_CANCELLATION")
        positive_score += 10.0

    if "유상증자" in haystack or fields.get("dilution_type") == "rights_offering":
        codes.append("DISC_RIGHTS_OFFERING")
        risk_score = max(risk_score, 45.0)
    if "전환사채" in haystack or fields.get("dilution_type") == "convertible_bond":
        codes.append("DISC_CONVERTIBLE_BOND")
        risk_score = max(risk_score, 45.0)
    if "신주인수권부사채" in haystack or fields.get("dilution_type") == "bond_with_warrant":
        codes.append("DISC_BOND_WITH_WARRANT")
        risk_score = max(risk_score, 45.0)
    if "소송" in haystack:
        codes.append("DISC_LAWSUIT")
        risk_score = max(risk_score, 55.0)
    if "감사의견" in haystack:
        codes.append("DISC_AUDIT_OPINION_ISSUE")
        risk_score = max(risk_score, 80.0)
    if "거래정지" in haystack:
        codes.append("DISC_TRADING_HALT")
        risk_score = max(risk_score, 85.0)
    if "관리종목" in haystack:
        codes.append("DISC_MANAGED_ISSUE")
        risk_score = max(risk_score, 80.0)
    if "상장폐지" in haystack:
        codes.append("DISC_DELISTING_RISK")
        risk_score = max(risk_score, 95.0)
    if any(token in haystack for token in ("계약 취소", "계약 해지", "계약 지연")):
        codes.append("DISC_CONTRACT_CANCEL_OR_DELAY")
        risk_score = max(risk_score, 75.0)
    return tuple(dict.fromkeys(codes)), min(positive_score, 100.0), min(risk_score, 100.0)


def _price_codes(
    price_bars: Sequence[PriceBar],
    disclosures: Sequence[DisclosureEvent],
    local_universe_returns_60d: Sequence[float],
) -> tuple[tuple[str, ...], float]:
    if not price_bars:
        return (), 0.0
    bars = sorted(price_bars, key=lambda item: item.date)
    latest = bars[-1]
    codes: list[str] = []
    score = 0.0
    prior_20 = bars[-21:-1]
    if prior_20:
        avg_trading_value = mean(item.trading_value for item in prior_20)
        if avg_trading_value > 0 and latest.trading_value >= avg_trading_value * 3:
            codes.append("PRICE_VOLUME_SPIKE")
            score += 35.0
    high_52w = max(item.high for item in bars)
    if high_52w > 0 and latest.close >= high_52w * 0.95:
        codes.append("PRICE_NEAR_52W_HIGH")
        score += 25.0
    return_60d = _return_since(bars, 60)
    if return_60d is not None and _is_top_percentile(return_60d, local_universe_returns_60d):
        codes.append("PRICE_60D_TOP_PERCENTILE")
        score += 25.0
    if disclosures and latest.date >= max(item.published_at.date() for item in disclosures):
        if latest.open > 0 and (latest.close / latest.open - 1.0) >= 0.05:
            codes.append("PRICE_GAP_WITH_DISCLOSURE")
            score += 20.0
    return tuple(dict.fromkeys(codes)), min(score, 100.0)


def _financial_codes(actuals: Sequence[FinancialActual]) -> tuple[tuple[str, ...], float]:
    if len(actuals) < 2:
        return (), 0.0
    ordered = sorted(actuals, key=lambda item: (item.period_end, item.reported_at))
    previous, latest = ordered[-2], ordered[-1]
    codes: list[str] = []
    score = 0.0
    if (previous.operating_profit or 0.0) <= 0 < (latest.operating_profit or 0.0):
        codes.append("FIN_OP_TURNAROUND")
        score += 30.0
    if previous.opm is not None and latest.opm is not None and latest.opm - previous.opm >= 5.0:
        codes.append("FIN_OPM_EXPANSION_5P")
        score += 25.0
    if (previous.fcf or 0.0) <= 0 < (latest.fcf or 0.0):
        codes.append("FIN_FCF_TURNAROUND")
        score += 25.0
    previous_cfo_ratio = _safe_divide(previous.cashflow_from_operations, previous.net_income)
    latest_cfo_ratio = _safe_divide(latest.cashflow_from_operations, latest.net_income)
    if previous_cfo_ratio is not None and latest_cfo_ratio is not None and latest_cfo_ratio - previous_cfo_ratio >= 0.30:
        codes.append("FIN_CFO_NET_INCOME_IMPROVEMENT")
        score += 15.0
    if _spike(latest.receivables, previous.receivables) or _spike(latest.inventory, previous.inventory):
        codes.append("FIN_RECEIVABLES_INVENTORY_SPIKE")
        score = max(score, 35.0)
    return tuple(dict.fromkeys(codes)), min(score, 100.0)


def _risk_codes(record: KINDRiskRecord) -> tuple[tuple[str, ...], float]:
    codes: list[str] = []
    score = 0.0
    if record.managed_issue:
        codes.append("RISK_MANAGED_ISSUE")
        score = max(score, 75.0)
    if record.trading_halt:
        codes.append("RISK_TRADING_HALT")
        score = max(score, 85.0)
    if record.investment_warning or record.investor_caution:
        codes.append("RISK_INVESTMENT_WARNING")
        score = max(score, 55.0)
    if record.unfaithful_disclosure:
        codes.append("RISK_UNFAITHFUL_DISCLOSURE")
        score = max(score, 80.0)
    if record.delisting_risk:
        codes.append("RISK_DELISTING")
        score = max(score, 95.0)
    return tuple(codes), score


def _return_since(bars: Sequence[PriceBar], days: int) -> float | None:
    bars = sorted(bars, key=lambda item: item.date)
    if len(bars) < 2:
        return None
    latest = bars[-1]
    prior_candidates = [item for item in bars[:-1] if (latest.date - item.date).days >= days]
    prior = prior_candidates[-1] if prior_candidates else bars[0]
    if prior.close <= 0:
        return None
    return latest.close / prior.close - 1.0


def _is_top_percentile(value: float, values: Sequence[float]) -> bool:
    if not values:
        return value >= 0.30
    sorted_values = sorted(values)
    threshold_index = max(0, int(len(sorted_values) * 0.80) - 1)
    return value >= sorted_values[threshold_index]


def _num(value) -> float | None:
    if value in (None, ""):
        return None
    try:
        return float(value)
    except (TypeError, ValueError):
        return None


def _safe_divide(numerator: float | None, denominator: float | None) -> float | None:
    if numerator is None or denominator in (None, 0):
        return None
    return numerator / denominator


def _spike(latest: float | None, previous: float | None) -> bool:
    if latest is None or previous is None:
        return False
    if previous <= 0 < latest:
        return True
    return previous > 0 and latest / previous - 1.0 >= 0.50


def _dedupe_evidence(items: Sequence[Evidence]) -> tuple[Evidence, ...]:
    unique: dict[str, Evidence] = {}
    for item in items:
        unique.setdefault(item.evidence_id, item)
    return tuple(unique.values())


__all__ = [
    "NEGATIVE_RISK_CODES",
    "POSITIVE_DISCLOSURE_CODES",
    "CheapScanRuleResult",
    "cheap_scan_total_score",
    "evaluate_cheap_scan_rules",
]
