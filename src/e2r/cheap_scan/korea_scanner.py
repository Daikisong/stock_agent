"""Korea all-listed cheap scan runner."""

from __future__ import annotations

from collections import Counter
from dataclasses import dataclass, field
from datetime import date
from typing import Mapping, Sequence

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
    event_search_min_score: float = 25.0
    deep_research_min_score: float = 45.0
    price_only_event_allowed: bool = True
    report_radar_enabled: bool = False


@dataclass(frozen=True)
class KoreaCheapScanResult:
    """Ranked cheap-scan output."""

    as_of_date: date
    candidates: tuple[CheapScanCandidate, ...]
    instruments_scanned: int
    diagnostics: tuple["CheapScanDiagnostic", ...] = field(default_factory=tuple)
    calibration: "CheapScanCalibrationReport | None" = None


@dataclass(frozen=True)
class CheapScanDiagnostic:
    """Explains why one instrument did or did not become a Layer-1 candidate."""

    symbol: str
    company_name: str
    market: Market
    as_of_date: date
    reason_codes: tuple[str, ...]
    diagnostic_reasons: tuple[str, ...]
    price_event_score: float
    disclosure_event_score: float
    financial_event_score: float
    risk_event_score: float
    cheap_scan_total_score: float
    recommended_next_layer: RecommendedNextLayer
    dropped_reason: str | None = None
    price_bar_count: int = 0
    disclosure_count: int = 0
    financial_actual_count: int = 0


@dataclass(frozen=True)
class CheapScanCalibrationReport:
    """Aggregated Layer-1 recall and routing diagnostics."""

    as_of_date: date
    instruments_scanned: int
    candidate_count: int
    event_search_count: int
    deep_research_count: int
    reason_code_distribution: Mapping[str, int]
    dropped_reason_distribution: Mapping[str, int]
    diagnostic_reason_distribution: Mapping[str, int]
    near_miss_top_50: tuple[CheapScanDiagnostic, ...]
    top_high_signal_disclosures: tuple[CheapScanDiagnostic, ...]
    top_price_signal_instruments: tuple[CheapScanDiagnostic, ...]
    top_financial_signal_instruments: tuple[CheapScanDiagnostic, ...]
    instruments_blocked_by_risk: tuple[CheapScanDiagnostic, ...]
    instruments_missing_price_bars: tuple[CheapScanDiagnostic, ...]


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
        diagnostics: list[CheapScanDiagnostic] = []
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
            total = cheap_scan_total_score(rule_result)
            next_layer = _recommended_next_layer(rule_result, total, config)
            diagnostic = CheapScanDiagnostic(
                symbol=instrument.symbol,
                company_name=instrument.name,
                market=instrument.market,
                as_of_date=config.as_of_date,
                reason_codes=rule_result.reason_codes,
                diagnostic_reasons=_diagnostic_reasons(rule_result, bars, disclosures, actuals, next_layer, total, config),
                price_event_score=rule_result.price_event_score,
                disclosure_event_score=rule_result.disclosure_event_score,
                financial_event_score=rule_result.financial_event_score,
                risk_event_score=rule_result.risk_event_score,
                cheap_scan_total_score=total,
                recommended_next_layer=next_layer,
                dropped_reason=rule_result.dropped_reason,
                price_bar_count=len(bars),
                disclosure_count=len(disclosures),
                financial_actual_count=len(actuals),
            )
            diagnostics.append(diagnostic)
            if not rule_result.reason_codes:
                continue
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
        calibration = _build_calibration_report(config.as_of_date, len(instruments), ranked, diagnostics)
        return KoreaCheapScanResult(
            as_of_date=config.as_of_date,
            candidates=ranked,
            instruments_scanned=len(instruments),
            diagnostics=tuple(sorted(diagnostics, key=lambda item: (-item.cheap_scan_total_score, item.symbol))),
            calibration=calibration,
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
                        company_aliases=(candidate.company_name, candidate.symbol),
                        candidate_reason_codes=candidate.reason_codes,
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


def _recommended_next_layer(rule_result, total_score: float, config: KoreaCheapScanConfig) -> RecommendedNextLayer:
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
    if has_structural_disclosure and (has_price_confirmation or has_financial_confirmation) and total_score >= config.deep_research_min_score:
        return RecommendedNextLayer.DEEP_RESEARCH
    if has_structural_disclosure:
        return RecommendedNextLayer.EVENT_SEARCH
    if rule_result.financial_event_score >= 45.0 and total_score >= min(config.event_search_min_score, 15.0):
        return RecommendedNextLayer.EVENT_SEARCH
    if config.price_only_event_allowed and rule_result.price_event_score >= 35.0:
        return RecommendedNextLayer.EVENT_SEARCH
    if total_score < config.event_search_min_score:
        return RecommendedNextLayer.NONE
    return RecommendedNextLayer.NONE


def _diagnostic_reasons(
    rule_result,
    bars: Sequence[PriceBar],
    disclosures,
    actuals,
    next_layer: RecommendedNextLayer,
    total_score: float,
    config: KoreaCheapScanConfig,
) -> tuple[str, ...]:
    reasons: list[str] = []
    if next_layer == RecommendedNextLayer.EVENT_SEARCH:
        reasons.append("candidate_event_search")
    if next_layer == RecommendedNextLayer.DEEP_RESEARCH:
        reasons.append("candidate_deep_research")
    if not bars:
        reasons.append("missing_price_bars")
    if rule_result.price_event_score <= 0:
        reasons.append("no_price_signal")
    if not any(code.startswith("DISC_") for code in rule_result.reason_codes if code not in {"DISC_RIGHTS_OFFERING", "DISC_CONVERTIBLE_BOND", "DISC_BOND_WITH_WARRANT"}):
        if disclosures:
            reasons.append("only_routine_disclosure")
        else:
            reasons.append("no_high_signal_disclosure")
    if rule_result.financial_event_score <= 0:
        reasons.append("no_financial_signal")
    if rule_result.risk_event_score > 0:
        reasons.append("risk_only" if rule_result.disclosure_event_score <= 0 and rule_result.price_event_score <= 0 and rule_result.financial_event_score <= 0 else "risk_present")
    if total_score < config.event_search_min_score and next_layer == RecommendedNextLayer.NONE:
        reasons.append("below_score_threshold")
    if any(code in rule_result.reason_codes for code in ("DISC_SUPPLY_CONTRACT", "DISC_FACILITY_INVESTMENT")) and rule_result.disclosure_event_score < 60:
        reasons.append("insufficient_disclosure_detail")
    return tuple(dict.fromkeys(reasons))


def _build_calibration_report(
    as_of_date: date,
    instruments_scanned: int,
    candidates: Sequence[CheapScanCandidate],
    diagnostics: Sequence[CheapScanDiagnostic],
) -> CheapScanCalibrationReport:
    reason_counter = Counter(code for item in diagnostics for code in item.reason_codes)
    dropped_counter = Counter(item.dropped_reason for item in diagnostics if item.dropped_reason)
    diagnostic_counter = Counter(reason for item in diagnostics for reason in item.diagnostic_reasons)
    near_miss = tuple(
        item
        for item in sorted(diagnostics, key=lambda row: (-row.cheap_scan_total_score, row.symbol))
        if item.recommended_next_layer == RecommendedNextLayer.NONE and item.cheap_scan_total_score > 0
    )[:50]
    return CheapScanCalibrationReport(
        as_of_date=as_of_date,
        instruments_scanned=instruments_scanned,
        candidate_count=len(candidates),
        event_search_count=sum(1 for item in candidates if item.recommended_next_layer == RecommendedNextLayer.EVENT_SEARCH),
        deep_research_count=sum(1 for item in candidates if item.recommended_next_layer == RecommendedNextLayer.DEEP_RESEARCH),
        reason_code_distribution=dict(reason_counter.most_common()),
        dropped_reason_distribution=dict(dropped_counter.most_common()),
        diagnostic_reason_distribution=dict(diagnostic_counter.most_common()),
        near_miss_top_50=near_miss,
        top_high_signal_disclosures=tuple(sorted((item for item in diagnostics if item.disclosure_event_score > 0), key=lambda row: (-row.disclosure_event_score, row.symbol))[:50]),
        top_price_signal_instruments=tuple(sorted((item for item in diagnostics if item.price_event_score > 0), key=lambda row: (-row.price_event_score, row.symbol))[:50]),
        top_financial_signal_instruments=tuple(sorted((item for item in diagnostics if item.financial_event_score > 0), key=lambda row: (-row.financial_event_score, row.symbol))[:50]),
        instruments_blocked_by_risk=tuple(sorted((item for item in diagnostics if item.risk_event_score >= 70 or item.dropped_reason), key=lambda row: (-row.risk_event_score, row.symbol))[:50]),
        instruments_missing_price_bars=tuple(item for item in diagnostics if "missing_price_bars" in item.diagnostic_reasons)[:50],
    )


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


__all__ = [
    "CheapScanCalibrationReport",
    "CheapScanDiagnostic",
    "KoreaCheapScanConfig",
    "KoreaCheapScanResult",
    "KoreaCheapScanner",
]
