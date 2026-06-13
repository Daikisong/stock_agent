"""Merge official and web evidence for as-of replay scoring."""

from __future__ import annotations

from dataclasses import dataclass, field, replace
from datetime import date, timedelta
from typing import Sequence

from e2r.audit.parser_audit import AuditFinding, audit_parser_outputs
from e2r.backtest.historical_official_store import HistoricalOfficialStore
from e2r.cheap_scan.models import CheapScanCandidate
from e2r.features import DeterministicFeatureEngineer, FeatureEngineeringInput, FeatureEngineeringResult
from e2r.models import (
    ConsensusRevision,
    ConsensusSnapshot,
    DisclosureEvent,
    Evidence,
    FinancialActual,
    NewsItem,
    PriceBar,
    ResearchReport,
    ScoreSnapshot,
    Stage,
    StageSnapshot,
)
from e2r.red_team import RedTeamAssessment, RedTeamEngine
from e2r.research.asof_web_research import AsOfWebResearchResult
from e2r.research.report_consensus_proxy import build_report_consensus_proxy
from e2r.score_validity import is_score_valid, score_block_reason
from e2r.sources.opendart import OpenDARTConnector
from e2r.staging import StageClassificationInput, StageClassifier


@dataclass(frozen=True)
class AsOfEvidenceBundle:
    """Complete point-in-time evidence bundle for one as-of candidate."""

    symbol: str
    company_name: str
    as_of_date: date
    sector_context: str | None = None
    price_bars: tuple[PriceBar, ...] = ()
    financial_actuals: tuple[FinancialActual, ...] = ()
    official_disclosures: tuple[DisclosureEvent, ...] = ()
    web_disclosures: tuple[DisclosureEvent, ...] = ()
    research_reports: tuple[ResearchReport, ...] = ()
    news_items: tuple[NewsItem, ...] = ()
    consensus: tuple[ConsensusSnapshot, ...] = ()
    consensus_revisions: tuple[ConsensusRevision, ...] = ()
    evidence: tuple[Evidence, ...] = ()
    source_types: tuple[str, ...] = ()

    def feature_input(self) -> FeatureEngineeringInput:
        return FeatureEngineeringInput(
            symbol=self.symbol,
            as_of_date=self.as_of_date,
            company_name=self.company_name,
            sector_context=self.sector_context,
            price_bars=self.price_bars,
            financial_actuals=self.financial_actuals,
            consensus=self.consensus,
            consensus_revisions=self.consensus_revisions,
            disclosures=self.official_disclosures + self.web_disclosures,
            research_reports=self.research_reports,
            news_items=self.news_items,
        )

    def coverage(self) -> dict[str, int]:
        return {
            "price_bars_count": len(self.price_bars),
            "financial_actuals_count": len(self.financial_actuals),
            "disclosures_count": len(self.official_disclosures) + len(self.web_disclosures),
            "research_reports_count": len(self.research_reports),
            "news_items_count": len(self.news_items),
            "consensus_count": len(self.consensus),
            "consensus_revisions_count": len(self.consensus_revisions),
        }


@dataclass(frozen=True)
class AsOfEvidenceBundleScore:
    """Merged deterministic scoring result for an evidence bundle."""

    bundle: AsOfEvidenceBundle
    feature_input: FeatureEngineeringInput
    feature_result: FeatureEngineeringResult
    score: ScoreSnapshot
    red_team: RedTeamAssessment
    stage: StageSnapshot
    audit_findings: tuple[AuditFinding, ...] = field(default_factory=tuple)


def build_asof_evidence_bundle(
    *,
    candidate: CheapScanCandidate,
    store: HistoricalOfficialStore,
    web_result: AsOfWebResearchResult | None = None,
    lookback_days: int = 370,
) -> AsOfEvidenceBundle:
    """Build a complete as-of feature bundle from official and web evidence."""

    start = candidate.as_of_date - timedelta(days=lookback_days)
    price_bars = store.load_price_bars(candidate.symbol, start, candidate.as_of_date, candidate.as_of_date)
    financial_actuals = store.load_financial_actuals(candidate.symbol, candidate.as_of_date)
    official_disclosures = store.load_disclosures(candidate.symbol, start, candidate.as_of_date, candidate.as_of_date)

    web_disclosures: tuple[DisclosureEvent, ...] = ()
    reports: tuple[ResearchReport, ...] = ()
    news: tuple[NewsItem, ...] = ()
    evidence: list[Evidence] = [OpenDARTConnector.to_evidence(item) for item in official_disclosures]
    if web_result is not None and web_result.pipeline_result is not None:
        web = web_result.pipeline_result.web_result
        web_disclosures = tuple(web.parsed_disclosures)
        reports = tuple(web.parsed_reports)
        news = tuple(web.parsed_news)
        evidence.extend(web.evidence)

    proxy = build_report_consensus_proxy(reports, as_of_date=candidate.as_of_date)
    reports = proxy.reports
    source_types = _source_types(
        price_bars=price_bars,
        financial_actuals=financial_actuals,
        official_disclosures=official_disclosures,
        web_disclosures=web_disclosures,
        reports=reports,
        news=news,
        consensus=proxy.consensus,
        consensus_revisions=proxy.consensus_revisions,
    )
    return AsOfEvidenceBundle(
        symbol=candidate.symbol,
        company_name=candidate.company_name,
        as_of_date=candidate.as_of_date,
        sector_context=" ".join(candidate.reason_codes) or None,
        price_bars=price_bars,
        financial_actuals=financial_actuals,
        official_disclosures=official_disclosures,
        web_disclosures=web_disclosures,
        research_reports=reports,
        news_items=news,
        consensus=proxy.consensus,
        consensus_revisions=proxy.consensus_revisions,
        evidence=_dedupe_evidence(evidence),
        source_types=source_types,
    )


def score_asof_evidence_bundle(
    bundle: AsOfEvidenceBundle,
    *,
    candidate: CheapScanCandidate,
    web_result: AsOfWebResearchResult | None = None,
    previous_stage: Stage | None = None,
) -> AsOfEvidenceBundleScore:
    """Run deterministic score/stage/audit on a merged as-of bundle."""

    feature_input = bundle.feature_input()
    feature_result = DeterministicFeatureEngineer().engineer(feature_input)
    score = feature_result.score()
    red_team = RedTeamEngine().assess(feature_result.red_team_signals)
    if _web_score_invalid(web_result):
        score = _invalidate_merged_score_for_web_block(score, web_result)
        stage = _blocked_stage_for_invalid_web_score(score, web_result, previous_stage)
        return AsOfEvidenceBundleScore(
            bundle=bundle,
            feature_input=feature_input,
            feature_result=feature_result,
            score=score,
            red_team=red_team,
            stage=stage,
            audit_findings=(),
        )
    stage = StageClassifier().classify(
        StageClassificationInput(
            score=score,
            red_team=red_team,
            previous_stage=previous_stage,
            theme_regime_score=80.0 if bundle.research_reports or bundle.news_items else 0.0,
            company_event_score=80.0 if bundle.official_disclosures or bundle.web_disclosures or bundle.research_reports or bundle.news_items else candidate.cheap_scan_total_score,
            high_quality_company_event=bool(bundle.official_disclosures or bundle.web_disclosures or bundle.research_reports),
            evidence_ids=score.evidence_ids,
        )
    )
    stage = _downgrade_green_if_date_unverified(stage, web_result)
    audit_findings = audit_parser_outputs(evidence=bundle.evidence, scores=(score,), stages=(stage,))
    if stage.stage == Stage.STAGE_3_GREEN and any(item.severity == "hard" or item.suggested_action == "block_green" for item in audit_findings):
        stage = replace(
            stage,
            stage=Stage.STAGE_3_YELLOW,
            grade="B",
            stage_reason=tuple(stage.stage_reason) + ("parser audit blocked unsafe Stage 3-Green",),
        )
    return AsOfEvidenceBundleScore(
        bundle=bundle,
        feature_input=feature_input,
        feature_result=feature_result,
        score=score,
        red_team=red_team,
        stage=stage,
        audit_findings=audit_findings,
    )


def _web_score_invalid(web_result: AsOfWebResearchResult | None) -> bool:
    if web_result is None or web_result.pipeline_result is None:
        return False
    return not is_score_valid(web_result.pipeline_result.score)


def _invalidate_merged_score_for_web_block(
    score: ScoreSnapshot,
    web_result: AsOfWebResearchResult | None,
) -> ScoreSnapshot:
    upstream_score = web_result.pipeline_result.score if web_result is not None and web_result.pipeline_result is not None else None
    upstream_reason = score_block_reason(upstream_score) or "score_invalid"
    diagnostics = dict(score.diagnostic_scores)
    diagnostics.update(
        {
            "raw_eps_fcf_before_asof_web_block": score.eps_fcf_explosion_score,
            "raw_earnings_visibility_before_asof_web_block": score.earnings_visibility_score,
            "raw_bottleneck_pricing_before_asof_web_block": score.bottleneck_pricing_score,
            "raw_market_mispricing_before_asof_web_block": score.market_mispricing_score,
            "raw_valuation_rerating_before_asof_web_block": score.valuation_rerating_score,
            "raw_capital_allocation_before_asof_web_block": score.capital_allocation_score,
            "raw_information_confidence_before_asof_web_block": score.information_confidence_score,
            "raw_score_total_before_asof_web_block": score.total_score,
            "raw_risk_penalty_before_asof_web_block": min(100.0, score.risk_penalty),
            "score_valid": 0.0,
            "score_blocked_by_asof_web": 100.0,
            "asof_web_score_required_for_merged_scoring": 100.0,
        }
    )
    if upstream_score is not None:
        diagnostics["upstream_invalid_score_total_capped"] = min(100.0, upstream_score.total_score)
    diagnostics["asof_web_block_reason_code"] = _asof_web_block_reason_code(upstream_reason)
    return replace(
        score,
        eps_fcf_explosion_score=0.0,
        earnings_visibility_score=0.0,
        bottleneck_pricing_score=0.0,
        market_mispricing_score=0.0,
        valuation_rerating_score=0.0,
        capital_allocation_score=0.0,
        information_confidence_score=0.0,
        risk_penalty=0.0,
        total_score=0.0,
        diagnostic_scores=diagnostics,
        scoring_version=f"{score.scoring_version}:asof-web-block",
    )


def _blocked_stage_for_invalid_web_score(
    score: ScoreSnapshot,
    web_result: AsOfWebResearchResult | None,
    previous_stage: Stage | None,
) -> StageSnapshot:
    upstream_score = web_result.pipeline_result.score if web_result is not None and web_result.pipeline_result is not None else None
    reason = score_block_reason(upstream_score) or "score_invalid"
    evidence_ids = score.evidence_ids
    if web_result is not None and web_result.pipeline_result is not None:
        evidence_ids = tuple(dict.fromkeys(evidence_ids + web_result.pipeline_result.stage.evidence_ids))
    return StageSnapshot(
        symbol=score.symbol,
        as_of_date=score.as_of_date,
        stage=Stage.STAGE_0,
        previous_stage=previous_stage,
        stage_changed=previous_stage is not None and previous_stage != Stage.STAGE_0,
        grade="Watch",
        stage_reason=(f"as-of merged scoring blocked because web score is invalid: {reason}",),
        red_team_status="Watch",
        evidence_ids=evidence_ids,
        classifier_version=f"{StageClassifier.version}:asof-web-block",
    )


def _asof_web_block_reason_code(reason: str) -> float:
    codes = {
        "theme_route_unresolved": 20.0,
        "score_gap_unresolved": 40.0,
        "asof_web_score_unresolved": 60.0,
        "score_invalid": 80.0,
    }
    return codes.get(reason, 90.0)


def _downgrade_green_if_date_unverified(
    stage: StageSnapshot,
    web_result: AsOfWebResearchResult | None,
) -> StageSnapshot:
    if stage.stage != Stage.STAGE_3_GREEN or web_result is None:
        return stage
    if web_result.date_verified_count > 0:
        return stage
    if web_result.date_unverified_count <= 0:
        return stage
    return replace(
        stage,
        stage=Stage.STAGE_3_YELLOW,
        grade="B",
        stage_reason=tuple(stage.stage_reason) + ("date-unverified documents cannot create Stage 3-Green alone",),
    )


def _source_types(
    *,
    price_bars: Sequence[PriceBar],
    financial_actuals: Sequence[FinancialActual],
    official_disclosures: Sequence[DisclosureEvent],
    web_disclosures: Sequence[DisclosureEvent],
    reports: Sequence[ResearchReport],
    news: Sequence[NewsItem],
    consensus: Sequence[ConsensusSnapshot],
    consensus_revisions: Sequence[ConsensusRevision],
) -> tuple[str, ...]:
    values: list[str] = []
    if price_bars:
        values.append("price")
    if financial_actuals:
        values.append("financial_actual")
    if official_disclosures or web_disclosures:
        values.append("disclosure")
    if reports:
        values.append("research_report")
    if news:
        values.append("news")
    if consensus:
        values.append("consensus")
    if consensus_revisions:
        values.append("consensus_revision")
    return tuple(values) or ("official_cheap_scan",)


def _dedupe_evidence(evidence: Sequence[Evidence]) -> tuple[Evidence, ...]:
    unique: dict[str, Evidence] = {}
    for item in evidence:
        unique.setdefault(item.evidence_id, item)
    return tuple(unique.values())


__all__ = [
    "AsOfEvidenceBundle",
    "AsOfEvidenceBundleScore",
    "build_asof_evidence_bundle",
    "score_asof_evidence_bundle",
]
