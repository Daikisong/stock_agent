"""Korea all-listed cheap scan runner."""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import date
from typing import Sequence

from e2r.cheap_scan.event_rules import cheap_scan_total_score, evaluate_cheap_scan_rules
from e2r.cheap_scan.models import CheapScanCandidate, RecommendedNextLayer
from e2r.cheap_scan.query_escalation import EscalationQueryPlanner, queries_for_candidate
from e2r.cheap_scan.korea_sources import KoreaCheapScanSources
from e2r.models import Instrument, Market, PriceBar
from e2r.research.free_web_research_runner import FreeWebResearchInput, FreeWebResearchRunner, WebResearchPipelineResult
from e2r.research.search_budget import SearchBudget
from e2r.research.search_provider import SearchProvider


@dataclass(frozen=True)
class KoreaCheapScanConfig:
    """Configuration for one Korea cheap scan."""

    as_of_date: date
    markets: tuple[Market, ...] = (Market.KR,)
    sources: KoreaCheapScanSources | None = None
    universe_limit: int | None = None
    lookback_days: int = 370
    disclosure_lookback_days: int = 3
    top_n: int | None = None


@dataclass(frozen=True)
class KoreaCheapScanResult:
    """Ranked cheap-scan output."""

    as_of_date: date
    candidates: tuple[CheapScanCandidate, ...]
    instruments_scanned: int


class KoreaCheapScanner:
    """Cheap official scan before web event search and deep research."""

    def __init__(self, sources: KoreaCheapScanSources | None = None) -> None:
        self._sources = sources or KoreaCheapScanSources.local_defaults()

    def run(self, config: KoreaCheapScanConfig) -> KoreaCheapScanResult:
        sources = config.sources or self._sources
        instruments = self._list_universe(sources, config.markets, config.as_of_date)
        if config.universe_limit is not None:
            instruments = instruments[: config.universe_limit]

        bars_by_symbol = {
            instrument.symbol: sources.get_price_bars(instrument.symbol, config.as_of_date, config.lookback_days)
            for instrument in instruments
        }
        returns_60d = tuple(
            value
            for value in (_return_60d(bars) for bars in bars_by_symbol.values())
            if value is not None
        )

        candidates: list[CheapScanCandidate] = []
        for instrument in instruments:
            bars = bars_by_symbol[instrument.symbol]
            disclosures = sources.get_disclosures(instrument.symbol, config.as_of_date, config.disclosure_lookback_days)
            actuals = sources.get_financial_actuals(instrument.symbol, config.as_of_date)
            risks = sources.get_risk_records(instrument.symbol, config.as_of_date)
            rule_result = evaluate_cheap_scan_rules(
                instrument=instrument,
                as_of_date=config.as_of_date,
                price_bars=bars,
                disclosures=disclosures,
                financial_actuals=actuals,
                risk_records=risks,
                local_universe_returns_60d=returns_60d,
            )
            if not rule_result.reason_codes:
                continue
            total = cheap_scan_total_score(rule_result)
            next_layer = _recommended_next_layer(rule_result)
            candidates.append(
                CheapScanCandidate(
                    symbol=instrument.symbol,
                    company_name=instrument.name,
                    market=instrument.market,
                    as_of_date=config.as_of_date,
                    reason_codes=rule_result.reason_codes,
                    price_event_score=rule_result.price_event_score,
                    disclosure_event_score=rule_result.disclosure_event_score,
                    financial_event_score=rule_result.financial_event_score,
                    risk_event_score=rule_result.risk_event_score,
                    cheap_scan_total_score=total,
                    evidence_ids=tuple(item.evidence_id for item in rule_result.evidence),
                    recommended_next_layer=next_layer,
                    dropped_reason=rule_result.dropped_reason,
                )
            )

        ranked = tuple(sorted(candidates, key=lambda item: (-item.cheap_scan_total_score, item.symbol)))
        if config.top_n is not None:
            ranked = ranked[: config.top_n]
        return KoreaCheapScanResult(
            as_of_date=config.as_of_date,
            candidates=ranked,
            instruments_scanned=len(instruments),
        )

    def escalate_candidates_to_web_research(
        self,
        candidates: Sequence[CheapScanCandidate],
        budget: SearchBudget,
        *,
        browser_provider: SearchProvider | None = None,
        free_search_provider: SearchProvider | None = None,
        fixture_text_by_url=None,
    ) -> tuple[WebResearchPipelineResult, ...]:
        """Run targeted free web research for event/deep candidates only."""

        results: list[WebResearchPipelineResult] = []
        for candidate in candidates:
            if candidate.recommended_next_layer not in {RecommendedNextLayer.EVENT_SEARCH, RecommendedNextLayer.DEEP_RESEARCH}:
                continue
            if not queries_for_candidate(candidate).queries:
                continue
            runner = FreeWebResearchRunner(
                browser_provider=browser_provider,
                free_search_provider=free_search_provider,
                query_planner=EscalationQueryPlanner(candidate),
            )
            results.append(
                runner.run(
                    FreeWebResearchInput(
                        company_name=candidate.company_name,
                        symbol=candidate.symbol,
                        sector=None,
                        market=candidate.market,
                        as_of_date=candidate.as_of_date,
                        budget=budget,
                        fixture_text_by_url=fixture_text_by_url or {},
                    )
                )
            )
        return tuple(results)

    @staticmethod
    def _list_universe(sources: KoreaCheapScanSources, markets: tuple[Market, ...], as_of_date: date) -> tuple[Instrument, ...]:
        instruments: dict[str, Instrument] = {}
        for market in markets:
            for item in sources.list_instruments(market, as_of_date):
                if _invalid_for_scan(item):
                    continue
                instruments.setdefault(item.symbol, item)
        return tuple(sorted(instruments.values(), key=lambda item: item.symbol))


def _recommended_next_layer(rule_result) -> RecommendedNextLayer:
    codes = set(rule_result.reason_codes)
    if rule_result.risk_event_score >= 70.0 or rule_result.dropped_reason:
        return RecommendedNextLayer.NONE
    has_structural_disclosure = bool(
        codes
        & {
            "DISC_SUPPLY_CONTRACT",
            "DISC_LONG_TERM_CONTRACT",
            "DISC_CONTRACT_TO_SALES_10P",
            "DISC_FACILITY_INVESTMENT",
            "DISC_CAPA_INCREASE",
            "DISC_EARNINGS_PREANNOUNCE",
        }
    )
    has_price_confirmation = bool(codes & {"PRICE_VOLUME_SPIKE", "PRICE_GAP_WITH_DISCLOSURE", "PRICE_NEAR_52W_HIGH"})
    has_financial_confirmation = bool(codes & {"FIN_OP_TURNAROUND", "FIN_OPM_EXPANSION_5P", "FIN_FCF_TURNAROUND"})
    if has_structural_disclosure and (has_price_confirmation or has_financial_confirmation):
        return RecommendedNextLayer.DEEP_RESEARCH
    if has_structural_disclosure or rule_result.financial_event_score >= 45.0 or rule_result.price_event_score >= 35.0:
        return RecommendedNextLayer.EVENT_SEARCH
    return RecommendedNextLayer.NONE


def _invalid_for_scan(item: Instrument) -> bool:
    return item.is_preferred or item.is_spac or item.is_reit or item.is_etf


def _return_60d(bars: Sequence[PriceBar]) -> float | None:
    bars = sorted(bars, key=lambda item: item.date)
    if len(bars) < 2:
        return None
    latest = bars[-1]
    prior_candidates = [bar for bar in bars[:-1] if (latest.date - bar.date).days >= 60]
    prior = prior_candidates[-1] if prior_candidates else bars[0]
    if prior.close <= 0:
        return None
    return latest.close / prior.close - 1.0


__all__ = ["KoreaCheapScanConfig", "KoreaCheapScanResult", "KoreaCheapScanner"]
