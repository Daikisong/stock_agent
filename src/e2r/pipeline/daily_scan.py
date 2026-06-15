"""Daily local-fixture scan runner."""

from __future__ import annotations

import json
from dataclasses import dataclass, field, fields, is_dataclass
from datetime import date, datetime
from enum import Enum
from pathlib import Path
from typing import Any, Mapping, Sequence

from e2r.briefing import MorningBrief, MorningBriefInput, generate_morning_briefing
from e2r.historical_cases import HistoricalCase, load_historical_cases
from e2r.llm.theme_provider import ThemeRouteProvider
from e2r.models import BacktestResult, Evidence, Instrument, Market, RedTeamFinding, ScoreSnapshot, StageSnapshot
from e2r.pipeline.company_research import (
    CompanyResearchInput,
    CompanyResearchPipeline,
    CompanyResearchResult,
    ConnectorBundle,
)
from e2r.score_validity import (
    is_score_valid,
    normalized_score_state_mapping_if_present,
    raw_score_total_before_block,
    research_input_fingerprint,
    score_block_reason,
    score_fingerprint,
    score_variability_drivers,
    visible_score_total,
)


@dataclass(frozen=True)
class DailyScanConfig:
    """Configuration for one local daily scan."""

    as_of_date: date
    markets: Sequence[Market] = (Market.KR, Market.US)
    connector_bundle: ConnectorBundle = field(default_factory=ConnectorBundle.local_defaults)
    universe_limit: int | None = None
    active_watchlist_symbols: Sequence[str] = field(default_factory=tuple)
    output_directory: str | Path = "output"
    fixture_mode: bool = True
    include_historical_cases: bool = False
    historical_case_dir: str | Path = "data/historical_cases"
    lookback_days: int = 756
    theme_rebalance_enabled: bool | None = None
    theme_route_provider: ThemeRouteProvider | None = None
    theme_evidence_review_enabled: bool = True
    max_theme_expansion_rounds: int | None = None

    def __post_init__(self) -> None:
        if type(self.as_of_date) is not date:
            raise ValueError("as_of_date must be a date")
        object.__setattr__(self, "markets", tuple(Market(market) for market in self.markets))
        object.__setattr__(self, "active_watchlist_symbols", tuple(str(item) for item in self.active_watchlist_symbols))
        if self.universe_limit is not None and self.universe_limit <= 0:
            raise ValueError("universe_limit must be positive when set")
        if self.lookback_days <= 0:
            raise ValueError("lookback_days must be positive")
        if self.max_theme_expansion_rounds is not None and self.max_theme_expansion_rounds < 0:
            raise ValueError("max_theme_expansion_rounds must be non-negative")


@dataclass(frozen=True)
class DailyScanResult:
    as_of_date: date
    instruments: tuple[Instrument, ...]
    company_results: tuple[CompanyResearchResult, ...]
    scores: tuple[ScoreSnapshot, ...]
    stages: tuple[StageSnapshot, ...]
    red_team_findings: tuple[RedTeamFinding, ...]
    evidence: tuple[Evidence, ...]
    backtests: tuple[BacktestResult, ...]
    morning_brief: MorningBrief
    markdown_path: Path
    json_path: Path
    errors: tuple[str, ...] = field(default_factory=tuple)


class DailyScanRunner:
    """Run the local E2R daily scan and write morning-brief outputs."""

    def __init__(self, company_pipeline: CompanyResearchPipeline | None = None) -> None:
        self._company_pipeline = company_pipeline or CompanyResearchPipeline()

    def run(self, config: DailyScanConfig) -> DailyScanResult:
        historical_cases = self._historical_cases(config)
        instruments, case_by_symbol = self._universe(config, historical_cases)
        company_results: list[CompanyResearchResult] = []
        errors: list[str] = []

        for instrument in instruments:
            case = case_by_symbol.get(instrument.symbol)
            if case is not None:
                result = self._company_pipeline.run_historical_case(case)
            else:
                result = self._company_pipeline.run(
                    CompanyResearchInput(
                        instrument=instrument,
                        as_of_date=config.as_of_date,
                        connectors=config.connector_bundle,
                        lookback_days=config.lookback_days,
                        fixture_mode=config.fixture_mode,
                        theme_rebalance_enabled=config.theme_rebalance_enabled,
                        theme_route_provider=config.theme_route_provider,
                        theme_evidence_review_enabled=config.theme_evidence_review_enabled,
                        max_theme_expansion_rounds=config.max_theme_expansion_rounds,
                    )
                )
            company_results.append(result)
            errors.extend(result.errors)

        scores = tuple(result.score for result in company_results)
        stages = tuple(result.stage for result in company_results)
        findings = tuple(finding for result in company_results for finding in result.red_team_findings)
        evidence = _dedupe_evidence(tuple(item for result in company_results for item in result.evidence))
        backtests = tuple(result.backtest for result in company_results if result.backtest is not None)
        morning_brief = generate_morning_briefing(
            as_of_date=config.as_of_date,
            instruments=instruments,
            scores=scores,
            stages=stages,
            red_team_findings=findings,
            backtests=backtests,
            evidence=evidence,
        )
        markdown_path, json_path = self._write_outputs(
            config=config,
            instruments=instruments,
            results=tuple(company_results),
            scores=scores,
            stages=stages,
            findings=findings,
            evidence=evidence,
            backtests=backtests,
            morning_brief=morning_brief,
            errors=tuple(errors),
        )
        return DailyScanResult(
            as_of_date=config.as_of_date,
            instruments=instruments,
            company_results=tuple(company_results),
            scores=scores,
            stages=stages,
            red_team_findings=findings,
            evidence=evidence,
            backtests=backtests,
            morning_brief=morning_brief,
            markdown_path=markdown_path,
            json_path=json_path,
            errors=tuple(errors),
        )

    @staticmethod
    def _historical_cases(config: DailyScanConfig) -> tuple[HistoricalCase, ...]:
        if not config.include_historical_cases:
            return ()
        return tuple(
            case
            for case in load_historical_cases(config.historical_case_dir)
            if case.market in config.markets and case.stage3_date <= config.as_of_date
        )

    @staticmethod
    def _universe(
        config: DailyScanConfig,
        historical_cases: Sequence[HistoricalCase],
    ) -> tuple[tuple[Instrument, ...], dict[str, HistoricalCase]]:
        instruments_by_symbol: dict[str, Instrument] = {}
        case_by_symbol: dict[str, HistoricalCase] = {}

        if config.connector_bundle.krx is not None:
            for market in config.markets:
                try:
                    for instrument in config.connector_bundle.krx.list_instruments(market, config.as_of_date):
                        instruments_by_symbol.setdefault(instrument.symbol, instrument)
                except (AttributeError, ValueError, FileNotFoundError):
                    continue

        for case in historical_cases:
            if case.instrument is not None:
                instruments_by_symbol[case.symbol] = case.instrument
            else:
                instruments_by_symbol[case.symbol] = Instrument(
                    symbol=case.symbol,
                    name=case.company_name,
                    market=case.market,
                    exchange="KRX" if case.market == Market.KR else "US",
                    sector_custom="historical_case",
                )
            case_by_symbol[case.symbol] = case

        default_market = config.markets[0] if config.markets else Market.KR
        for symbol in config.active_watchlist_symbols:
            instruments_by_symbol.setdefault(
                symbol,
                Instrument(
                    symbol=symbol,
                    name=symbol,
                    market=default_market,
                    exchange="WATCHLIST",
                    sector_custom="watchlist",
                ),
            )

        instruments = [
            instrument
            for instrument in instruments_by_symbol.values()
            if instrument.market in config.markets and _is_valid_instrument(instrument)
        ]
        instruments = sorted(instruments, key=lambda item: (item.market.value, item.symbol))
        if config.universe_limit is not None:
            instruments = instruments[: config.universe_limit]
        filtered_symbols = {instrument.symbol for instrument in instruments}
        return tuple(instruments), {symbol: case for symbol, case in case_by_symbol.items() if symbol in filtered_symbols}

    @staticmethod
    def _write_outputs(
        *,
        config: DailyScanConfig,
        instruments: Sequence[Instrument],
        results: Sequence[CompanyResearchResult],
        scores: Sequence[ScoreSnapshot],
        stages: Sequence[StageSnapshot],
        findings: Sequence[RedTeamFinding],
        evidence: Sequence[Evidence],
        backtests: Sequence[BacktestResult],
        morning_brief: MorningBrief,
        errors: Sequence[str],
    ) -> tuple[Path, Path]:
        output_dir = Path(config.output_directory) / "morning_briefs"
        output_dir.mkdir(parents=True, exist_ok=True)
        stem = config.as_of_date.isoformat()
        markdown_path = output_dir / f"{stem}.md"
        json_path = output_dir / f"{stem}.json"
        markdown_path.write_text(morning_brief.text, encoding="utf-8")
        company_result_rows = [_company_result_output_row(result) for result in results]
        score_rows = [
            _score_output_row(
                result.score,
                input_fingerprint=str(row["research_input_fingerprint"]),
                input_counts=row["feature_input_counts"],
                evidence_count=int(row["evidence_count"]),
            )
            for result, row in zip(results, company_result_rows)
        ]
        if not score_rows:
            score_rows = [_score_output_row(score) for score in scores]
        payload = {
            "as_of_date": config.as_of_date,
            "instruments": instruments,
            "scores": score_rows,
            "stages": stages,
            "red_team_findings": findings,
            "evidence": evidence,
            "backtests": backtests,
            "company_results": company_result_rows,
            "brief_text": morning_brief.text,
            "errors": tuple(errors),
        }
        json_path.write_text(json.dumps(_jsonable(payload), ensure_ascii=False, indent=2, sort_keys=True), encoding="utf-8")
        return markdown_path, json_path


def _is_valid_instrument(instrument: Instrument) -> bool:
    return not (
        instrument.is_preferred
        or instrument.is_spac
        or instrument.is_reit
        or instrument.is_etf
        or instrument.is_managed
        or instrument.is_invest_warning
        or instrument.is_trading_halt
    )


def _dedupe_evidence(items: Sequence[Evidence]) -> tuple[Evidence, ...]:
    unique: dict[str, Evidence] = {}
    for item in items:
        unique.setdefault(item.evidence_id, item)
    return tuple(unique.values())


def _score_output_row(
    score: ScoreSnapshot,
    *,
    input_fingerprint: str | None = None,
    input_counts: Mapping[str, int] | None = None,
    evidence_count: int | None = None,
) -> Mapping[str, Any]:
    valid = is_score_valid(score)
    visible_score = visible_score_total(score)
    component_scores = None
    risk_penalty = None
    if valid:
        component_scores = {
            "eps_fcf_explosion": score.eps_fcf_explosion_score,
            "earnings_visibility": score.earnings_visibility_score,
            "bottleneck_pricing": score.bottleneck_pricing_score,
            "market_mispricing": score.market_mispricing_score,
            "valuation_rerating": score.valuation_rerating_score,
            "capital_allocation": score.capital_allocation_score,
            "information_confidence": score.information_confidence_score,
        }
        risk_penalty = score.risk_penalty
    return {
        "symbol": score.symbol,
        "as_of_date": score.as_of_date,
        "score_valid": valid,
        "score_blocked_reason": score_block_reason(score),
        "score_fingerprint": score_fingerprint(score),
        "research_input_fingerprint": input_fingerprint,
        "score_variability_drivers": score_variability_drivers(
            score,
            input_counts=input_counts,
            evidence_count=evidence_count,
            input_fingerprint=input_fingerprint,
        ),
        "visible_score": visible_score,
        "total_score": visible_score,
        "raw_score_before_block": raw_score_total_before_block(score),
        "component_scores": component_scores,
        "risk_penalty": risk_penalty,
        "diagnostic_scores": score.diagnostic_scores,
        "evidence_ids": score.evidence_ids,
        "scoring_version": score.scoring_version,
    }


def _company_result_output_row(result: CompanyResearchResult) -> Mapping[str, Any]:
    input_counts = _feature_input_count_row(result.feature_input)
    input_fingerprint = _company_result_input_fingerprint(result, input_counts=input_counts)
    visible_score = visible_score_total(result.score)
    return {
        "symbol": result.instrument.symbol,
        "name": result.instrument.name,
        "stage": result.stage.stage,
        "score": visible_score,
        "visible_score": visible_score,
        "score_valid": is_score_valid(result.score),
        "score_blocked_reason": score_block_reason(result.score),
        "score_fingerprint": score_fingerprint(result.score),
        "research_input_fingerprint": input_fingerprint,
        "score_variability_drivers": score_variability_drivers(
            result.score,
            input_counts=input_counts,
            evidence_count=len(result.evidence),
            input_fingerprint=input_fingerprint,
        ),
        "raw_score_before_block": raw_score_total_before_block(result.score),
        "shortage_type": result.feature_result.shortage_type,
        "feature_input_counts": input_counts,
        "evidence_count": len(result.evidence),
        "error_count": len(result.errors),
    }


def _company_result_input_fingerprint(
    result: CompanyResearchResult,
    *,
    input_counts: Mapping[str, int] | None = None,
) -> str:
    return research_input_fingerprint(
        score=result.score,
        evidence=result.evidence,
        input_counts=input_counts or _feature_input_count_row(result.feature_input),
        source_fields=result.feature_result.source_fields,
    )


def _feature_input_count_row(feature_input: Any) -> Mapping[str, int]:
    return {
        "price_bars": len(feature_input.price_bars),
        "financial_actuals": len(feature_input.financial_actuals),
        "consensus": len(feature_input.consensus),
        "consensus_revisions": len(feature_input.consensus_revisions),
        "disclosures": len(feature_input.disclosures),
        "research_reports": len(feature_input.research_reports),
        "news_items": len(feature_input.news_items),
        "agent_extracted_fields": len(feature_input.agent_extracted_fields),
    }


def _jsonable(value: Any) -> Any:
    if isinstance(value, (date, datetime)):
        return value.isoformat()
    if isinstance(value, Enum):
        return value.value
    if isinstance(value, Path):
        return str(value)
    if is_dataclass(value):
        return {field.name: _jsonable(getattr(value, field.name)) for field in fields(value)}
    if isinstance(value, Mapping):
        return normalized_score_state_mapping_if_present({str(key): _jsonable(item) for key, item in value.items()})
    if isinstance(value, (list, tuple)):
        return [_jsonable(item) for item in value]
    return value
