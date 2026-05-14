"""Lightweight report/news radar for Layer-1 recall."""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import date
from typing import Mapping, Sequence

from e2r.cheap_scan.models import CheapScanCandidate, RecommendedNextLayer
from e2r.models import Instrument, Market
from e2r.research.search_budget import ResearchLayer, SearchBudget, SearchBudgetTracker
from e2r.research.search_provider import SearchProvider, SearchResult


REPORT_RADAR_PHRASES: tuple[str, ...] = (
    "목표주가 상향 EPS 상향 PDF",
    "컨센서스 상회 Review PDF",
    "실적 서프라이즈 목표주가 상향 PDF",
    "수주잔고 OPM 수출 비중 PDF",
    "신규시설투자 CAPA 증설 PDF",
    "장기공급계약 매출액 대비 PDF",
    "ASP 상승 판가 상승 리드타임 PDF",
    "북미 미국향 데이터센터 수주 PDF",
)


@dataclass(frozen=True)
class ReportRadarCandidate:
    """One candidate discovered by a broad but budgeted report/news radar."""

    company_name: str
    symbol: str | None
    market: Market
    as_of_date: date
    trigger_query: str
    matched_result: SearchResult
    confidence: float
    reason_codes: tuple[str, ...] = field(default_factory=tuple)
    recommended_next_layer: RecommendedNextLayer = RecommendedNextLayer.EVENT_SEARCH

    def to_cheap_scan_candidate(self) -> CheapScanCandidate:
        return CheapScanCandidate(
            symbol=self.symbol or self.company_name,
            company_name=self.company_name,
            market=self.market,
            as_of_date=self.as_of_date,
            reason_codes=self.reason_codes,
            price_event_score=0.0,
            disclosure_event_score=0.0,
            financial_event_score=0.0,
            risk_event_score=0.0,
            cheap_scan_total_score=round(min(100.0, self.confidence * 100.0), 4),
            evidence_ids=(),
            recommended_next_layer=self.recommended_next_layer,
            candidate_source_path="report_radar",
            production_candidate=True,
        )


@dataclass
class ReportRadar:
    """Run high-signal E2R phrase searches for a capped universe slice."""

    search_provider: SearchProvider
    max_results_per_query: int = 3

    def run(
        self,
        *,
        instruments: Sequence[Instrument],
        as_of_date: date,
        budget: SearchBudget,
        active_watchlist_symbols: Sequence[str] = (),
        max_symbols: int = 20,
    ) -> tuple[ReportRadarCandidate, ...]:
        tracker = SearchBudgetTracker(budget)
        selected = _select_instruments(instruments, active_watchlist_symbols, max_symbols)
        candidates: dict[str, ReportRadarCandidate] = {}
        for instrument in selected:
            for phrase in REPORT_RADAR_PHRASES:
                query = f"{instrument.name} {phrase}"
                decision = tracker.can_run(instrument.symbol, ResearchLayer.EVENT_SEARCH)
                if not decision.allowed:
                    return tuple(candidates.values())
                tracker.record_query(instrument.symbol, ResearchLayer.EVENT_SEARCH)
                for result in self.search_provider.search(query, as_of_date, self.max_results_per_query):
                    candidate = _candidate_from_result(instrument, as_of_date, query, result)
                    if candidate is None:
                        continue
                    key = f"{candidate.symbol}:{candidate.matched_result.url}"
                    existing = candidates.get(key)
                    if existing is None or candidate.confidence > existing.confidence:
                        candidates[key] = candidate
        return tuple(sorted(candidates.values(), key=lambda item: (-item.confidence, item.company_name)))


def _select_instruments(
    instruments: Sequence[Instrument],
    active_watchlist_symbols: Sequence[str],
    max_symbols: int,
) -> tuple[Instrument, ...]:
    by_symbol: Mapping[str, Instrument] = {item.symbol: item for item in instruments}
    selected: list[Instrument] = []
    for symbol in active_watchlist_symbols:
        item = by_symbol.get(symbol)
        if item is not None:
            selected.append(item)
    for item in instruments:
        if item not in selected:
            selected.append(item)
        if len(selected) >= max_symbols:
            break
    return tuple(selected[:max_symbols])


def _candidate_from_result(
    instrument: Instrument,
    as_of_date: date,
    query: str,
    result: SearchResult,
) -> ReportRadarCandidate | None:
    confidence = _result_confidence(instrument.name, result)
    if confidence < 0.55:
        return None
    return ReportRadarCandidate(
        company_name=instrument.name,
        symbol=instrument.symbol,
        market=instrument.market,
        as_of_date=as_of_date,
        trigger_query=query,
        matched_result=result,
        confidence=confidence,
        reason_codes=_reason_codes(result),
        recommended_next_layer=RecommendedNextLayer.DEEP_RESEARCH if confidence >= 0.78 else RecommendedNextLayer.EVENT_SEARCH,
    )


def _result_confidence(company_name: str, result: SearchResult) -> float:
    haystack = f"{result.title} {result.snippet or ''}"
    score = result.confidence
    if company_name in haystack:
        score += 0.20
    if result.is_report_domain:
        score += 0.15
    if result.is_pdf:
        score += 0.10
    if any(token in haystack for token in ("Review", "컨센서스", "목표주가", "수주잔고", "CAPA", "장기공급계약", "ASP", "OPM", "리드타임")):
        score += 0.20
    if result.is_news:
        score += 0.05
    return max(0.0, min(1.0, score))


def _reason_codes(result: SearchResult) -> tuple[str, ...]:
    haystack = f"{result.title} {result.snippet or ''}"
    codes: list[str] = ["REPORT_RADAR_MATCH"]
    if result.is_pdf or result.is_report_domain:
        codes.append("REPORT_RADAR_REPORT")
    if "컨센서스" in haystack or "목표주가" in haystack or "EPS" in haystack:
        codes.append("REPORT_RADAR_REVISION")
    if "수주잔고" in haystack or "장기공급계약" in haystack:
        codes.append("REPORT_RADAR_CONTRACT")
    if "CAPA" in haystack or "신규시설투자" in haystack:
        codes.append("REPORT_RADAR_CAPA")
    if "ASP" in haystack or "판가" in haystack or "리드타임" in haystack:
        codes.append("REPORT_RADAR_PRICING")
    return tuple(dict.fromkeys(codes))


__all__ = ["REPORT_RADAR_PHRASES", "ReportRadar", "ReportRadarCandidate"]
