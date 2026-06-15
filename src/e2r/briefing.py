"""Korean E2R morning briefing generator."""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import date
from typing import Iterable, Mapping, Sequence

from .models import (
    BacktestResult,
    Evidence,
    Instrument,
    RedTeamFinding,
    ScoreSnapshot,
    SectorRegime,
    Stage,
    StageSnapshot,
)
from .score_validity import (
    is_score_valid,
    raw_score_total_before_block,
    score_block_reason,
    score_fingerprint,
    score_variability_drivers,
    visible_score_total,
)


STAGE_3_STAGES = frozenset({Stage.STAGE_3_GREEN, Stage.STAGE_3_YELLOW, Stage.STAGE_3_RED})
STAGE_4_STAGES = frozenset({Stage.STAGE_4A, Stage.STAGE_4B, Stage.STAGE_4C})
_FORBIDDEN_TERMS = ("매" + "수", "매" + "도", "비중 " + "축소", "오늘 " + "사야 함", "b" + "uy", "s" + "ell")


def _require_date(value: date, field_name: str) -> None:
    if type(value) is not date:
        raise ValueError(f"{field_name} must be a date")


def _require_text(value: str, field_name: str) -> None:
    if not isinstance(value, str) or not value.strip():
        raise ValueError(f"{field_name} must be a non-empty string")


def _pct(value: float | None) -> str:
    if value is None:
        return "n/a"
    return f"{value * 100:+.1f}%"


def _score(value: float | None) -> str:
    if value is None:
        return "n/a"
    return f"{value:.1f}"


def _assert_no_recommendation_terms(text: str) -> None:
    lowered = text.lower()
    for term in _FORBIDDEN_TERMS:
        if term.lower() in lowered:
            raise ValueError("briefing text contains disallowed recommendation wording")


def _brief_score_state_text(score: ScoreSnapshot) -> str:
    drivers = tuple(
        driver
        for driver in score_variability_drivers(score)
        if driver.startswith(
            (
                "estimate_source_missing:",
                "estimate_quality:",
                "input_missing:",
                "input_count:",
                "evidence_count:",
                "score_evidence_count:",
                "llm_expansion_query_count:",
                "theme_rebalance_status:",
                "theme_route_status:",
                "theme_evidence_gate_status:",
                "route_mismatch:",
            )
        )
    )
    driver_text = f" / 변동요인 {', '.join(drivers[:3])}" if drivers else ""
    return f"상태 valid fp {score_fingerprint(score) or 'none'}{driver_text}"


@dataclass(frozen=True)
class ScheduledEvent:
    """Upcoming item to monitor in the morning brief."""

    event_date: date
    title: str
    event_type: str
    as_of_date: date
    symbol: str | None = None
    source: str | None = None

    def __post_init__(self) -> None:
        _require_date(self.event_date, "event_date")
        _require_text(self.title, "title")
        _require_text(self.event_type, "event_type")
        _require_date(self.as_of_date, "as_of_date")
        if self.symbol is not None:
            _require_text(self.symbol, "symbol")


@dataclass(frozen=True)
class MorningBriefInput:
    """Input bundle for a Korean morning briefing."""

    as_of_date: date
    instruments: Sequence[Instrument] = field(default_factory=tuple)
    scores: Sequence[ScoreSnapshot] = field(default_factory=tuple)
    stages: Sequence[StageSnapshot] = field(default_factory=tuple)
    red_team_findings: Sequence[RedTeamFinding] = field(default_factory=tuple)
    backtests: Sequence[BacktestResult] = field(default_factory=tuple)
    evidence: Sequence[Evidence] = field(default_factory=tuple)
    sector_regimes: Sequence[SectorRegime] = field(default_factory=tuple)
    scheduled_events: Sequence[ScheduledEvent] = field(default_factory=tuple)

    def __post_init__(self) -> None:
        _require_date(self.as_of_date, "as_of_date")
        object.__setattr__(self, "instruments", tuple(self.instruments))
        object.__setattr__(self, "scores", tuple(self.scores))
        object.__setattr__(self, "stages", tuple(self.stages))
        object.__setattr__(self, "red_team_findings", tuple(self.red_team_findings))
        object.__setattr__(self, "backtests", tuple(self.backtests))
        object.__setattr__(self, "evidence", tuple(self.evidence))
        object.__setattr__(self, "sector_regimes", tuple(self.sector_regimes))
        object.__setattr__(self, "scheduled_events", tuple(self.scheduled_events))


@dataclass(frozen=True)
class MorningBrief:
    """Rendered Korean morning briefing."""

    as_of_date: date
    text: str

    def __post_init__(self) -> None:
        _require_date(self.as_of_date, "as_of_date")
        _assert_no_recommendation_terms(self.text)


class MorningBriefingGenerator:
    """Render Stage, score, evidence, and monitoring data into Korean text."""

    def generate(self, inputs: MorningBriefInput) -> MorningBrief:
        instrument_by_symbol = {instrument.symbol: instrument for instrument in inputs.instruments}
        score_by_symbol = self._latest_scores(inputs.scores, inputs.as_of_date)
        evidence_by_id = {item.evidence_id: item for item in inputs.evidence if item.as_of_date <= inputs.as_of_date}
        findings_by_symbol = self._findings_by_symbol(inputs.red_team_findings, inputs.as_of_date)
        backtest_by_symbol = {item.symbol: item for item in inputs.backtests}

        lines = [f"[E2R Morning Brief / {inputs.as_of_date.isoformat()}]", ""]
        sections = (
            ("1. 신규 Stage 2 후보", self._stage_items(inputs, {Stage.STAGE_2}, True)),
            ("2. Stage 3-Green / Yellow / Red 변화", self._stage_items(inputs, STAGE_3_STAGES, True)),
            ("3. Stage 4A / 4B / 4C 변화", self._stage_items(inputs, STAGE_4_STAGES, True)),
        )
        for title, stage_items in sections:
            lines.append(title)
            lines.extend(
                self._render_stage_items(
                    stage_items,
                    instrument_by_symbol,
                    score_by_symbol,
                    findings_by_symbol,
                    backtest_by_symbol,
                    evidence_by_id,
                )
            )
            lines.append("")

        lines.append("4. Red Team thesis-break 감시")
        lines.extend(self._render_red_team(findings_by_symbol, instrument_by_symbol, evidence_by_id))
        lines.append("")

        lines.append("5. 섹터 레짐 변화")
        lines.extend(self._render_sector_regimes(inputs.sector_regimes, inputs.as_of_date))
        lines.append("")

        lines.append("6. 오늘 확인할 공시, 실적, 리포트 일정")
        lines.extend(self._render_scheduled_events(inputs.scheduled_events, inputs.as_of_date))

        text = "\n".join(lines).rstrip() + "\n"
        _assert_no_recommendation_terms(text)
        return MorningBrief(as_of_date=inputs.as_of_date, text=text)

    @staticmethod
    def _latest_scores(scores: Sequence[ScoreSnapshot], as_of_date: date) -> dict[str, ScoreSnapshot]:
        latest: dict[str, ScoreSnapshot] = {}
        for score in sorted(scores, key=lambda item: item.as_of_date):
            if score.as_of_date <= as_of_date:
                latest[score.symbol] = score
        return latest

    @staticmethod
    def _findings_by_symbol(
        findings: Sequence[RedTeamFinding],
        as_of_date: date,
    ) -> dict[str, tuple[RedTeamFinding, ...]]:
        grouped: dict[str, list[RedTeamFinding]] = {}
        for finding in findings:
            if finding.as_of_date <= as_of_date:
                grouped.setdefault(finding.symbol, []).append(finding)
        return {
            symbol: tuple(sorted(items, key=lambda item: (-item.severity, item.risk_type)))
            for symbol, items in grouped.items()
        }

    @staticmethod
    def _stage_items(inputs: MorningBriefInput, stages: Iterable[Stage], changed_only: bool) -> tuple[StageSnapshot, ...]:
        allowed = set(stages)
        items = [
            stage
            for stage in inputs.stages
            if stage.as_of_date <= inputs.as_of_date
            and stage.stage in allowed
            and (stage.stage_changed or not changed_only)
        ]
        return tuple(sorted(items, key=lambda item: (item.stage.value, item.symbol)))

    def _render_stage_items(
        self,
        stages: Sequence[StageSnapshot],
        instruments: Mapping[str, Instrument],
        scores: Mapping[str, ScoreSnapshot],
        findings: Mapping[str, tuple[RedTeamFinding, ...]],
        backtests: Mapping[str, BacktestResult],
        evidence: Mapping[str, Evidence],
    ) -> list[str]:
        if not stages:
            return ["- 해당 없음"]
        rendered: list[str] = []
        for stage in stages:
            instrument = instruments.get(stage.symbol)
            score = scores.get(stage.symbol)
            finding_items = findings.get(stage.symbol, ())
            backtest = backtests.get(stage.symbol)
            rendered.append(f"- {self._instrument_label(stage.symbol, instrument)}")
            rendered.append(f"  현재 Stage: {stage.stage.value} / 전일 대비: {self._stage_delta(stage)}")
            rendered.append(f"  표시점수와 주요 점수: {self._score_line(score)}")
            rendered.append(f"  핵심 변화: {self._reasons(stage)}")
            rendered.append(f"  핵심 숫자: {self._metric_line(score, backtest)}")
            rendered.append(f"  근거: {self._evidence_line(stage.evidence_ids, evidence)}")
            rendered.append(f"  Red Team: {self._risk_line(stage.red_team_status, finding_items)}")
            rendered.append(f"  다음 확인 트리거: {self._next_triggers(stage.stage)}")
        return rendered

    @staticmethod
    def _instrument_label(symbol: str, instrument: Instrument | None) -> str:
        if instrument is None:
            return f"{symbol} / 시장 n/a / 섹터 n/a"
        sector = instrument.sector_custom or instrument.sector_exchange or "n/a"
        return f"{instrument.name} / {instrument.symbol} / {instrument.market.value} / {sector}"

    @staticmethod
    def _stage_delta(stage: StageSnapshot) -> str:
        if not stage.stage_changed:
            return "유지"
        if stage.previous_stage is None:
            return "신규"
        return f"{stage.previous_stage.value} -> {stage.stage.value}"

    @staticmethod
    def _score_line(score: ScoreSnapshot | None) -> str:
        if score is None:
            return "점수 n/a"
        if not is_score_valid(score):
            reason = score_block_reason(score) or "score_invalid"
            raw = raw_score_total_before_block(score)
            raw_text = f" / 참고 raw {_score(raw)}" if raw is not None else ""
            return f"점수 산출 보류 ({reason}){raw_text} | 상태 pending fp {score_fingerprint(score) or 'none'}"
        state_text = _brief_score_state_text(score)
        return (
            f"표시점수 {_score(visible_score_total(score))} | "
            f"EPS/FCF {_score(score.eps_fcf_explosion_score)}/20, "
            f"가시성 {_score(score.earnings_visibility_score)}/20, "
            f"병목/가격 {_score(score.bottleneck_pricing_score)}/20, "
            f"밸류여지 {_score(score.valuation_rerating_score)}/15 | "
            f"{state_text}"
        )

    @staticmethod
    def _reasons(stage: StageSnapshot) -> str:
        if stage.stage_reason:
            return "; ".join(stage.stage_reason)
        return "분류 사유 n/a"

    @staticmethod
    def _metric_line(score: ScoreSnapshot | None, backtest: BacktestResult | None) -> str:
        parts: list[str] = []
        if score is not None and not is_score_valid(score):
            reason = score_block_reason(score) or "score_invalid"
            parts.append(f"Score Pending {reason}")
        elif score is not None:
            revision = score.diagnostic_scores.get("revision_score")
            price_stage = score.diagnostic_scores.get("price_stage_score")
            if revision is not None:
                parts.append(f"Revision {_score(revision)}")
            if price_stage is not None:
                parts.append(f"Price Stage {_score(price_stage)}")
        if backtest is not None:
            parts.extend(
                [
                    f"PreRunUp252D {_pct(backtest.pre_runup_252d)}",
                    f"MFE90D {_pct(backtest.mfe_90d)}",
                    f"MAE90D {_pct(backtest.mae_90d)}",
                    f"BelowEntry {backtest.below_entry_flag}",
                ]
            )
        return ", ".join(parts) if parts else "핵심 숫자 n/a"

    @staticmethod
    def _evidence_line(evidence_ids: Sequence[str], evidence_by_id: Mapping[str, Evidence]) -> str:
        items = [evidence_by_id[evidence_id] for evidence_id in evidence_ids if evidence_id in evidence_by_id]
        if not items:
            return "근거 n/a"
        rendered = [
            f"{item.source_name}/{item.source_type}/as_of {item.as_of_date.isoformat()}"
            for item in items[:3]
        ]
        if len(items) > 3:
            rendered.append(f"외 {len(items) - 3}건")
        return "; ".join(rendered)

    @staticmethod
    def _risk_line(status: str | None, findings: Sequence[RedTeamFinding]) -> str:
        status_text = status or "n/a"
        if not findings:
            return f"{status_text} / 특이 신호 없음"
        top = findings[0]
        return f"{status_text} / {top.risk_type} severity {_score(top.severity)} / as_of {top.as_of_date.isoformat()}"

    @staticmethod
    def _next_triggers(stage: Stage) -> str:
        if stage == Stage.STAGE_2:
            return "다음 실적, 수주잔고, OPM, 컨센서스 상향 확인"
        if stage in STAGE_3_STAGES:
            return "EPS/FCF 재상향, 계약 질, 밸류 반영 속도 확인"
        if stage == Stage.STAGE_4A:
            return "4B Soft Exit 점수와 수주/마진 지속성 확인"
        if stage == Stage.STAGE_4B:
            return "EPS/FCF 상향 재개 여부와 과밀 신호 확인"
        if stage == Stage.STAGE_4C:
            return "논리 훼손 원인의 지속 여부와 새 근거 발생 여부 확인"
        return "추가 공개 데이터 확인"

    def _render_red_team(
        self,
        findings: Mapping[str, tuple[RedTeamFinding, ...]],
        instruments: Mapping[str, Instrument],
        evidence: Mapping[str, Evidence],
    ) -> list[str]:
        all_findings = sorted(
            (finding for items in findings.values() for finding in items),
            key=lambda item: (-item.severity, item.symbol, item.risk_type),
        )
        if not all_findings:
            return ["- 해당 없음"]
        lines: list[str] = []
        for finding in all_findings:
            lines.append(f"- {self._instrument_label(finding.symbol, instruments.get(finding.symbol))}")
            lines.append(
                f"  논리 훼손 위험 증가: {finding.risk_type} / severity {_score(finding.severity)} / "
                f"hard_break {finding.is_hard_break}"
            )
            lines.append(f"  근거: {self._evidence_line(finding.evidence_ids, evidence)}")
        return lines

    @staticmethod
    def _render_sector_regimes(regimes: Sequence[SectorRegime], as_of_date: date) -> list[str]:
        items = sorted(
            (regime for regime in regimes if regime.as_of_date <= as_of_date),
            key=lambda item: (-item.theme_regime_score, item.sector),
        )
        if not items:
            return ["- 해당 없음"]
        return [
            (
                f"- {item.sector}: regime {_score(item.theme_regime_score)} / "
                f"official {_score(item.official_data_confirmation)} / "
                f"relative {_score(item.sector_relative_strength)} / as_of {item.as_of_date.isoformat()}"
            )
            for item in items
        ]

    @staticmethod
    def _render_scheduled_events(events: Sequence[ScheduledEvent], as_of_date: date) -> list[str]:
        items = sorted(
            (event for event in events if event.as_of_date <= as_of_date and event.event_date >= as_of_date),
            key=lambda item: (item.event_date, item.symbol or "", item.title),
        )
        if not items:
            return ["- 해당 없음"]
        return [
            (
                f"- {item.event_date.isoformat()} / {item.event_type} / "
                f"{item.symbol or '공통'} / {item.title} / source {item.source or 'n/a'} / "
                f"as_of {item.as_of_date.isoformat()}"
            )
            for item in items
        ]


def generate_morning_briefing(
    *,
    as_of_date: date,
    instruments: Iterable[Instrument] = (),
    scores: Iterable[ScoreSnapshot] = (),
    stages: Iterable[StageSnapshot] = (),
    red_team_findings: Iterable[RedTeamFinding] = (),
    backtests: Iterable[BacktestResult] = (),
    evidence: Iterable[Evidence] = (),
    sector_regimes: Iterable[SectorRegime] = (),
    scheduled_events: Iterable[ScheduledEvent] = (),
) -> MorningBrief:
    """Convenience wrapper for the Korean morning briefing generator."""

    return MorningBriefingGenerator().generate(
        MorningBriefInput(
            as_of_date=as_of_date,
            instruments=tuple(instruments),
            scores=tuple(scores),
            stages=tuple(stages),
            red_team_findings=tuple(red_team_findings),
            backtests=tuple(backtests),
            evidence=tuple(evidence),
            sector_regimes=tuple(sector_regimes),
            scheduled_events=tuple(scheduled_events),
        )
    )
