"""Autopsy why as-of replay candidates did or did not promote stages."""

from __future__ import annotations

import csv
import json
from collections import Counter
from dataclasses import dataclass, fields, is_dataclass
from datetime import date, datetime
from enum import Enum
from pathlib import Path
from typing import Any, Mapping, Sequence

from e2r.backtest.asof_evidence_bundle import (
    AsOfEvidenceBundleScore,
    build_asof_evidence_bundle,
    score_asof_evidence_bundle,
)
from e2r.backtest.historical_official_store import DEFAULT_HISTORICAL_OFFICIAL_ROOT, HistoricalOfficialStore
from e2r.backtest.runtime_fixture_evidence import RuntimeFixtureEvidenceStore
from e2r.cheap_scan.models import CheapScanCandidate, RecommendedNextLayer
from e2r.models import Market, Stage
from e2r.research.asof_web_research import (
    AsOfWebResearchConfig,
    AsOfWebResearchRunner,
    RetrospectiveSnapshotSearchProvider,
    fixture_text_by_url_for_candidate,
)
from e2r.score_validity import (
    is_score_valid,
    normalized_score_state_mapping_if_present,
    normalized_score_state_payload,
    raw_score_total_before_block,
    research_input_fingerprint,
    serialized_score_block_reason,
    serialized_score_valid,
    score_block_reason,
    score_fingerprint,
    score_variability_drivers,
    visible_score_total,
)
from e2r.research.report_snapshot_store import ReportSnapshotStore
from e2r.research.search_snapshot_store import SearchSnapshotStore
from e2r.stage_gate_diagnostics import StageGateDiagnostics, diagnose_stage_gates, promotion_band


DEFAULT_STAGE_PROMOTION_OUTPUT_DIR = Path("output/backtests/asof_stage_promotion_autopsy")


@dataclass(frozen=True)
class AsOfStagePromotionAutopsyConfig:
    """Configuration for stage promotion autopsy."""

    asof_output: str | Path
    output_directory: str | Path = DEFAULT_STAGE_PROMOTION_OUTPUT_DIR
    official_root: str | Path = DEFAULT_HISTORICAL_OFFICIAL_ROOT
    search_snapshot_root: str | Path = "data/search_snapshots"
    report_snapshot_root: str | Path = "data/report_snapshots"
    top_candidates: int | None = None
    max_queries_per_candidate: int | None = None
    max_results_per_query: int = 100
    report_date: date | None = None
    runtime_fixture_spec_paths: Sequence[str | Path] = ()

    def __post_init__(self) -> None:
        if self.max_queries_per_candidate is not None and self.max_queries_per_candidate < 0:
            raise ValueError("max_queries_per_candidate cannot be negative")
        if self.top_candidates is not None and self.top_candidates <= 0:
            raise ValueError("top_candidates must be positive")
        object.__setattr__(self, "runtime_fixture_spec_paths", tuple(self.runtime_fixture_spec_paths or ()))


@dataclass(frozen=True)
class StagePromotionAutopsyRow:
    """One candidate stage-promotion diagnostic row."""

    symbol: str
    company_name: str
    as_of_date: date
    layer: str
    current_stage: Stage
    current_score: float | None
    score_valid: bool
    score_blocked_reason: str | None
    score_fingerprint: str | None
    research_input_fingerprint: str | None
    score_variability_drivers: tuple[str, ...]
    raw_score_before_block: float | None
    eps_fcf_explosion: float | None
    earnings_visibility: float | None
    bottleneck_pricing: float | None
    market_mispricing: float | None
    valuation_rerating: float | None
    capital_allocation: float | None
    information_confidence: float | None
    risk_penalty: float | None
    large_sector_id: str
    canonical_archetype_id: str
    archetype_weight_profile_applied: float | None
    archetype_weighted_total_before_calibration: float | None
    archetype_weight_eps_fcf_explosion: float | None
    archetype_weight_earnings_visibility: float | None
    archetype_weight_bottleneck_pricing: float | None
    archetype_weight_market_mispricing: float | None
    archetype_weight_valuation_rerating: float | None
    archetype_weight_capital_allocation: float | None
    archetype_weight_information_confidence: float | None
    archetype_component_eps_fcf_explosion: float | None
    archetype_component_earnings_visibility: float | None
    archetype_component_bottleneck_pricing: float | None
    archetype_component_market_mispricing: float | None
    archetype_component_valuation_rerating: float | None
    archetype_component_capital_allocation: float | None
    archetype_component_information_confidence: float | None
    archetype_green_policy_absolute_block: float | None
    archetype_green_policy_unlock_required: float | None
    archetype_green_policy_unlock_evidence: float | None
    archetype_green_restricted_by_profile: float | None
    revision_score: float | None
    price_stage_score: float | None
    contract_quality: float | None
    backlog_rpo_visibility: float | None
    capa_constraint: float | None
    asp_pricing_power: float | None
    structural_shortage: float | None
    one_off_shortage_risk: float | None
    structural_visibility_quality: float | None
    sector_visibility_score: float | None
    sector_bottleneck_score: float | None
    recurring_demand_visibility: float | None
    export_channel_visibility: float | None
    medium_term_revision_visibility: float | None
    domain_specific_evidence_score: float | None
    research_axis_bridge_present_count_capped: float | None
    research_axis_bridge_margin: float | None
    research_axis_bridge_customer: float | None
    research_axis_bridge_backlog: float | None
    research_axis_bridge_contract: float | None
    research_axis_bridge_valuation_repricing: float | None
    research_axis_bridge_capital_return: float | None
    research_axis_bridge_insurance_quality: float | None
    research_axis_bridge_bio_commercialization: float | None
    research_axis_bridge_software_retention: float | None
    research_axis_bridge_consumer_sell_through: float | None
    research_axis_bridge_guard_risk: float | None
    research_axis_bridge_guard_risk_penalty_points: float | None
    actual_profit_conversion_score: float | None
    bottleneck_industrial_raw: float | None
    bottleneck_sector_raw: float | None
    bottleneck_actual_conversion_raw: float | None
    bottleneck_validated_conversion_raw: float | None
    bottleneck_selected_raw: float | None
    bottleneck_selected_path: str
    bottleneck_component_before_one_off_penalty: float | None
    bottleneck_one_off_penalty_points: float | None
    bottleneck_raw_required_for_green: float | None
    bottleneck_raw_deficit_to_green: float | None
    sector_profile: str
    promotion_band: str
    cross_evidence_families_present: str
    missing_evidence_families: str
    price_bars_count: int
    financial_actuals_count: int
    disclosures_count: int
    research_reports_count: int
    news_items_count: int
    consensus_count: int
    consensus_revisions_count: int
    failed_stage2_total_score: bool
    failed_stage2_eps_fcf: bool
    failed_stage2_valuation: bool
    failed_stage2_information_confidence: bool
    failed_stage3_total_score: bool
    failed_stage3_eps_fcf: bool
    failed_stage3_visibility: bool
    failed_stage3_bottleneck: bool
    failed_stage3_market_mispricing: bool
    failed_stage3_valuation: bool
    failed_stage3_revision: bool
    failed_stage3_contract_quality: bool
    failed_structural_visibility_quality: bool
    failed_sector_visibility: bool
    failed_sector_bottleneck: bool
    failed_green_cross_evidence: bool
    failed_report_date_confidence: bool
    failed_date_unverified_green_evidence: bool
    failed_domain_specific_evidence: bool
    failed_stage3_red_team: bool
    stage3_total_deficit: float | None
    stage3_eps_fcf_deficit: float | None
    stage3_visibility_deficit: float | None
    stage3_bottleneck_deficit: float | None
    stage3_market_mispricing_deficit: float | None
    stage3_valuation_deficit: float | None
    stage3_revision_deficit: float | None
    stage3_contract_quality_deficit: float | None
    structural_visibility_deficit: float | None
    sector_visibility_deficit: float | None
    sector_bottleneck_deficit: float | None
    green_cross_evidence_deficit: float | None
    domain_specific_evidence_deficit: float | None
    stage3_yellow_total_deficit: float | None
    green_gate_deficit_summary: str
    red_team_risk: str
    hard_audit_count: int
    audit_finding_codes: str
    audit_finding_fields: str
    audit_finding_actions: str
    explanation: str


@dataclass(frozen=True)
class AsOfStagePromotionAutopsyResult:
    """Complete stage-promotion autopsy result."""

    config: AsOfStagePromotionAutopsyConfig
    rows: tuple[StagePromotionAutopsyRow, ...]
    benchmark_rows: tuple[Mapping[str, Any], ...]
    output_paths: Mapping[str, Path]


class AsOfStagePromotionAutopsy:
    """Re-score as-of candidates with merged evidence and explain stage gates."""

    def run(self, config: AsOfStagePromotionAutopsyConfig, *, write_outputs: bool = True) -> AsOfStagePromotionAutopsyResult:
        asof_output = Path(config.asof_output)
        candidate_rows = _load_json(asof_output / "discovered_candidates.json")
        benchmark_rows = tuple(_load_json(asof_output / "benchmark_recall_report.json"))
        selected = _select_candidate_rows(candidate_rows, benchmark_rows, config.top_candidates)
        store = HistoricalOfficialStore(config.official_root)
        search_store = SearchSnapshotStore(config.search_snapshot_root)
        report_store = ReportSnapshotStore(config.report_snapshot_root)
        fixture_store = RuntimeFixtureEvidenceStore(_runtime_fixture_spec_paths(config, asof_output))
        rows: list[StagePromotionAutopsyRow] = []
        for item in selected:
            candidate = _candidate_from_row(item)
            provider = RetrospectiveSnapshotSearchProvider(
                store=search_store,
                symbol=candidate.symbol,
                company_name=candidate.company_name,
            )
            fixture_text = fixture_text_by_url_for_candidate(
                store=report_store,
                symbol=candidate.symbol,
                company_name=candidate.company_name,
            )
            web_result = AsOfWebResearchRunner().run(
                candidate=candidate,
                search_provider=provider,
                fixture_text_by_url=fixture_text,
                config=AsOfWebResearchConfig(
                    as_of_date=candidate.as_of_date,
                    max_queries_per_candidate=config.max_queries_per_candidate,
                    max_results_per_query=config.max_results_per_query,
                    require_date_verified_for_green=True,
                    allow_undated_docs_for_yellow_only=True,
                ),
            )
            extra_reports = fixture_store.reports_for_candidate(candidate)
            extra_evidence = fixture_store.evidence_for_candidate(candidate)
            bundle = build_asof_evidence_bundle(
                candidate=candidate,
                store=store,
                web_result=web_result,
                extra_reports=extra_reports,
                extra_evidence=extra_evidence,
            )
            scored = score_asof_evidence_bundle(bundle, candidate=candidate, web_result=web_result)
            diagnostics = diagnose_stage_gates(scored.score, scored.red_team)
            rows.append(_autopsy_row(candidate, scored, diagnostics))
        output_paths: Mapping[str, Path] = {}
        result = AsOfStagePromotionAutopsyResult(
            config=config,
            rows=tuple(rows),
            benchmark_rows=benchmark_rows,
            output_paths=output_paths,
        )
        if write_outputs:
            output_paths = _write_outputs(result)
            result = AsOfStagePromotionAutopsyResult(
                config=config,
                rows=result.rows,
                benchmark_rows=result.benchmark_rows,
                output_paths=output_paths,
            )
        return result


def _autopsy_row(
    candidate: CheapScanCandidate,
    scored: AsOfEvidenceBundleScore,
    diagnostics: StageGateDiagnostics,
) -> StagePromotionAutopsyRow:
    score = scored.score
    coverage = scored.bundle.coverage()
    valid_score = is_score_valid(score)
    failed = set(diagnostics.failed_gate_names)
    hard_audit_count = sum(1 for item in scored.audit_findings if item.severity == "hard" or item.suggested_action == "block_green")
    input_counts = {
        "price_bars": coverage["price_bars_count"],
        "financial_actuals": coverage["financial_actuals_count"],
        "disclosures": coverage["disclosures_count"],
        "research_reports": coverage["research_reports_count"],
        "news_items": coverage["news_items_count"],
        "consensus": coverage["consensus_count"],
        "consensus_revisions": coverage["consensus_revisions_count"],
    }
    input_fingerprint = research_input_fingerprint(
        score=score,
        evidence=getattr(scored.bundle, "evidence", ()),
        input_counts=input_counts,
        source_fields=getattr(getattr(scored, "feature_result", None), "source_fields", None),
    )
    return StagePromotionAutopsyRow(
        symbol=candidate.symbol,
        company_name=candidate.company_name,
        as_of_date=candidate.as_of_date,
        layer=candidate.recommended_next_layer.value,
        current_stage=scored.stage.stage,
        current_score=visible_score_total(score),
        score_valid=valid_score,
        score_blocked_reason=score_block_reason(score),
        score_fingerprint=score_fingerprint(score),
        research_input_fingerprint=input_fingerprint,
        score_variability_drivers=score_variability_drivers(
            score,
            input_counts=input_counts,
            evidence_count=len(score.evidence_ids),
            input_fingerprint=input_fingerprint,
        ),
        raw_score_before_block=raw_score_total_before_block(score),
        eps_fcf_explosion=score.eps_fcf_explosion_score if valid_score else None,
        earnings_visibility=score.earnings_visibility_score if valid_score else None,
        bottleneck_pricing=score.bottleneck_pricing_score if valid_score else None,
        market_mispricing=score.market_mispricing_score if valid_score else None,
        valuation_rerating=score.valuation_rerating_score if valid_score else None,
        capital_allocation=score.capital_allocation_score if valid_score else None,
        information_confidence=score.information_confidence_score if valid_score else None,
        risk_penalty=score.risk_penalty if valid_score else None,
        large_sector_id=_source_field_text(scored, "large_sector_id", valid_score),
        canonical_archetype_id=_source_field_text(scored, "canonical_archetype_id", valid_score),
        archetype_weight_profile_applied=_valid_diag(score.diagnostic_scores, "archetype_weight_profile_applied", valid_score),
        archetype_weighted_total_before_calibration=_valid_diag(
            score.diagnostic_scores,
            "archetype_weighted_total_before_calibration",
            valid_score,
        ),
        archetype_weight_eps_fcf_explosion=_valid_diag(score.diagnostic_scores, "archetype_weight_eps_fcf_explosion", valid_score),
        archetype_weight_earnings_visibility=_valid_diag(score.diagnostic_scores, "archetype_weight_earnings_visibility", valid_score),
        archetype_weight_bottleneck_pricing=_valid_diag(score.diagnostic_scores, "archetype_weight_bottleneck_pricing", valid_score),
        archetype_weight_market_mispricing=_valid_diag(score.diagnostic_scores, "archetype_weight_market_mispricing", valid_score),
        archetype_weight_valuation_rerating=_valid_diag(score.diagnostic_scores, "archetype_weight_valuation_rerating", valid_score),
        archetype_weight_capital_allocation=_valid_diag(score.diagnostic_scores, "archetype_weight_capital_allocation", valid_score),
        archetype_weight_information_confidence=_valid_diag(score.diagnostic_scores, "archetype_weight_information_confidence", valid_score),
        archetype_component_eps_fcf_explosion=_valid_diag(
            score.diagnostic_scores,
            "archetype_component_eps_fcf_explosion",
            valid_score,
        ),
        archetype_component_earnings_visibility=_valid_diag(
            score.diagnostic_scores,
            "archetype_component_earnings_visibility",
            valid_score,
        ),
        archetype_component_bottleneck_pricing=_valid_diag(
            score.diagnostic_scores,
            "archetype_component_bottleneck_pricing",
            valid_score,
        ),
        archetype_component_market_mispricing=_valid_diag(
            score.diagnostic_scores,
            "archetype_component_market_mispricing",
            valid_score,
        ),
        archetype_component_valuation_rerating=_valid_diag(
            score.diagnostic_scores,
            "archetype_component_valuation_rerating",
            valid_score,
        ),
        archetype_component_capital_allocation=_valid_diag(
            score.diagnostic_scores,
            "archetype_component_capital_allocation",
            valid_score,
        ),
        archetype_component_information_confidence=_valid_diag(
            score.diagnostic_scores,
            "archetype_component_information_confidence",
            valid_score,
        ),
        archetype_green_policy_absolute_block=_valid_diag(
            score.diagnostic_scores,
            "archetype_green_policy_absolute_block",
            valid_score,
        ),
        archetype_green_policy_unlock_required=_valid_diag(
            score.diagnostic_scores,
            "archetype_green_policy_unlock_required",
            valid_score,
        ),
        archetype_green_policy_unlock_evidence=_valid_diag(
            score.diagnostic_scores,
            "archetype_green_policy_unlock_evidence",
            valid_score,
        ),
        archetype_green_restricted_by_profile=_valid_diag(
            score.diagnostic_scores,
            "archetype_green_restricted_by_profile",
            valid_score,
        ),
        revision_score=_valid_diag(score.diagnostic_scores, "revision_score", valid_score),
        price_stage_score=_valid_diag(score.diagnostic_scores, "price_stage_score", valid_score),
        contract_quality=_valid_diag(score.diagnostic_scores, "contract_quality", valid_score),
        backlog_rpo_visibility=_valid_diag(score.diagnostic_scores, "backlog_rpo_visibility", valid_score),
        capa_constraint=_valid_diag(score.diagnostic_scores, "capa_constraint", valid_score),
        asp_pricing_power=_valid_diag(score.diagnostic_scores, "asp_pricing_power", valid_score),
        structural_shortage=_valid_diag(score.diagnostic_scores, "structural_shortage", valid_score),
        one_off_shortage_risk=_valid_diag(score.diagnostic_scores, "one_off_shortage_risk", valid_score),
        structural_visibility_quality=_valid_diag(score.diagnostic_scores, "structural_visibility_quality", valid_score),
        sector_visibility_score=_valid_diag(score.diagnostic_scores, "sector_visibility_score", valid_score),
        sector_bottleneck_score=_valid_diag(score.diagnostic_scores, "sector_bottleneck_score", valid_score),
        recurring_demand_visibility=_valid_diag(score.diagnostic_scores, "recurring_demand_visibility", valid_score),
        export_channel_visibility=_valid_diag(score.diagnostic_scores, "export_channel_visibility", valid_score),
        medium_term_revision_visibility=_valid_diag(score.diagnostic_scores, "medium_term_revision_visibility", valid_score),
        domain_specific_evidence_score=_valid_diag(score.diagnostic_scores, "domain_specific_evidence_score", valid_score),
        research_axis_bridge_present_count_capped=_valid_diag(
            score.diagnostic_scores,
            "research_axis_bridge_present_count_capped",
            valid_score,
        ),
        research_axis_bridge_margin=_valid_diag(score.diagnostic_scores, "research_axis_bridge_margin", valid_score),
        research_axis_bridge_customer=_valid_diag(score.diagnostic_scores, "research_axis_bridge_customer", valid_score),
        research_axis_bridge_backlog=_valid_diag(score.diagnostic_scores, "research_axis_bridge_backlog", valid_score),
        research_axis_bridge_contract=_valid_diag(score.diagnostic_scores, "research_axis_bridge_contract", valid_score),
        research_axis_bridge_valuation_repricing=_valid_diag(
            score.diagnostic_scores,
            "research_axis_bridge_valuation_repricing",
            valid_score,
        ),
        research_axis_bridge_capital_return=_valid_diag(
            score.diagnostic_scores,
            "research_axis_bridge_capital_return",
            valid_score,
        ),
        research_axis_bridge_insurance_quality=_valid_diag(
            score.diagnostic_scores,
            "research_axis_bridge_insurance_quality",
            valid_score,
        ),
        research_axis_bridge_bio_commercialization=_valid_diag(
            score.diagnostic_scores,
            "research_axis_bridge_bio_commercialization",
            valid_score,
        ),
        research_axis_bridge_software_retention=_valid_diag(
            score.diagnostic_scores,
            "research_axis_bridge_software_retention",
            valid_score,
        ),
        research_axis_bridge_consumer_sell_through=_valid_diag(
            score.diagnostic_scores,
            "research_axis_bridge_consumer_sell_through",
            valid_score,
        ),
        research_axis_bridge_guard_risk=_valid_diag(score.diagnostic_scores, "research_axis_bridge_guard_risk", valid_score),
        research_axis_bridge_guard_risk_penalty_points=_valid_diag(
            score.diagnostic_scores,
            "research_axis_bridge_guard_risk_penalty_points",
            valid_score,
        ),
        actual_profit_conversion_score=_valid_diag(score.diagnostic_scores, "actual_profit_conversion_score", valid_score),
        bottleneck_industrial_raw=_valid_diag(score.diagnostic_scores, "bottleneck_industrial_raw", valid_score),
        bottleneck_sector_raw=_valid_diag(score.diagnostic_scores, "bottleneck_sector_raw", valid_score),
        bottleneck_actual_conversion_raw=_valid_diag(score.diagnostic_scores, "bottleneck_actual_conversion_raw", valid_score),
        bottleneck_validated_conversion_raw=_valid_diag(
            score.diagnostic_scores,
            "bottleneck_validated_conversion_raw",
            valid_score,
        ),
        bottleneck_selected_raw=_valid_diag(score.diagnostic_scores, "bottleneck_selected_raw", valid_score),
        bottleneck_selected_path=_source_field_text(scored, "bottleneck_selected_path", valid_score),
        bottleneck_component_before_one_off_penalty=_valid_diag(
            score.diagnostic_scores,
            "bottleneck_component_before_one_off_penalty",
            valid_score,
        ),
        bottleneck_one_off_penalty_points=_valid_diag(score.diagnostic_scores, "bottleneck_one_off_penalty_points", valid_score),
        bottleneck_raw_required_for_green=_valid_diag(score.diagnostic_scores, "bottleneck_raw_required_for_green", valid_score),
        bottleneck_raw_deficit_to_green=_valid_diag(score.diagnostic_scores, "bottleneck_raw_deficit_to_green", valid_score),
        sector_profile=diagnostics.sector_profile,
        promotion_band=promotion_band(score, scored.stage.stage),
        cross_evidence_families_present=", ".join(diagnostics.cross_evidence_families_present),
        missing_evidence_families=", ".join(diagnostics.missing_evidence_families),
        price_bars_count=coverage["price_bars_count"],
        financial_actuals_count=coverage["financial_actuals_count"],
        disclosures_count=coverage["disclosures_count"],
        research_reports_count=coverage["research_reports_count"],
        news_items_count=coverage["news_items_count"],
        consensus_count=coverage["consensus_count"],
        consensus_revisions_count=coverage["consensus_revisions_count"],
        failed_stage2_total_score="failed_stage2_total_score" in failed,
        failed_stage2_eps_fcf="failed_stage2_eps_fcf" in failed,
        failed_stage2_valuation="failed_stage2_valuation" in failed,
        failed_stage2_information_confidence="failed_stage2_information_confidence" in failed,
        failed_stage3_total_score="failed_stage3_total_score" in failed,
        failed_stage3_eps_fcf="failed_stage3_eps_fcf" in failed,
        failed_stage3_visibility="failed_stage3_visibility" in failed,
        failed_stage3_bottleneck="failed_stage3_bottleneck" in failed,
        failed_stage3_market_mispricing="failed_stage3_market_mispricing" in failed,
        failed_stage3_valuation="failed_stage3_valuation" in failed,
        failed_stage3_revision="failed_stage3_revision" in failed,
        failed_stage3_contract_quality="failed_stage3_contract_quality" in failed,
        failed_structural_visibility_quality="failed_structural_visibility_quality" in failed,
        failed_sector_visibility="failed_sector_visibility" in failed,
        failed_sector_bottleneck="failed_sector_bottleneck" in failed,
        failed_green_cross_evidence="failed_green_cross_evidence" in failed,
        failed_report_date_confidence="failed_report_date_confidence" in failed,
        failed_date_unverified_green_evidence="failed_date_unverified_green_evidence" in failed,
        failed_domain_specific_evidence="failed_domain_specific_evidence" in failed,
        failed_stage3_red_team="failed_stage3_red_team" in failed,
        stage3_total_deficit=_gate_deficit(diagnostics, "failed_stage3_total_score", valid_score),
        stage3_eps_fcf_deficit=_gate_deficit(diagnostics, "failed_stage3_eps_fcf", valid_score),
        stage3_visibility_deficit=_gate_deficit(diagnostics, "failed_stage3_visibility", valid_score),
        stage3_bottleneck_deficit=_gate_deficit(diagnostics, "failed_stage3_bottleneck", valid_score),
        stage3_market_mispricing_deficit=_gate_deficit(diagnostics, "failed_stage3_market_mispricing", valid_score),
        stage3_valuation_deficit=_gate_deficit(diagnostics, "failed_stage3_valuation", valid_score),
        stage3_revision_deficit=_gate_deficit(diagnostics, "failed_stage3_revision", valid_score),
        stage3_contract_quality_deficit=_gate_deficit(diagnostics, "failed_stage3_contract_quality", valid_score),
        structural_visibility_deficit=_gate_deficit(diagnostics, "failed_structural_visibility_quality", valid_score),
        sector_visibility_deficit=_gate_deficit(diagnostics, "failed_sector_visibility", valid_score),
        sector_bottleneck_deficit=_gate_deficit(diagnostics, "failed_sector_bottleneck", valid_score),
        green_cross_evidence_deficit=_gate_deficit(diagnostics, "failed_green_cross_evidence", valid_score),
        domain_specific_evidence_deficit=_gate_deficit(diagnostics, "failed_domain_specific_evidence", valid_score),
        stage3_yellow_total_deficit=_gate_deficit(diagnostics, "failed_stage3_yellow_calibrated_total", valid_score),
        green_gate_deficit_summary=_gate_deficit_summary(diagnostics, valid_score),
        red_team_risk=scored.red_team.risk_level.value,
        hard_audit_count=hard_audit_count,
        audit_finding_codes=_audit_finding_values(scored.audit_findings, "code"),
        audit_finding_fields=_audit_finding_values(scored.audit_findings, "field_name"),
        audit_finding_actions=_audit_finding_values(scored.audit_findings, "suggested_action"),
        explanation=_explain(scored, diagnostics, hard_audit_count),
    )


def _explain(scored: AsOfEvidenceBundleScore, diagnostics: StageGateDiagnostics, hard_audit_count: int) -> str:
    if not is_score_valid(scored.score):
        return f"Score pending: {score_block_reason(scored.score) or 'score_invalid'}."
    if hard_audit_count:
        audit_codes = _audit_finding_values(scored.audit_findings, "code")
        audit_text = f"Parser audit produced hard findings ({audit_codes or 'unknown'}), so Green is blocked"
        if not diagnostics.stage2_gate_passed:
            gates = ", ".join(_stage2_failed_gate_names(diagnostics))
            return f"{audit_text}; Stage 2 gate also failed: {gates}."
        if not diagnostics.stage3_green_gate_passed:
            gates = ", ".join(_stage3_green_failed_gate_names(diagnostics))
            return f"{audit_text}; Stage 3-Green gate also failed: {gates}."
        return f"{audit_text}."
    if scored.red_team.has_hard_break:
        return "Red Team hard thesis-break blocked promotion."
    if not diagnostics.stage2_gate_passed:
        gates = ", ".join(_stage2_failed_gate_names(diagnostics))
        return f"Stage 2 gate failed: {gates}."
    if not diagnostics.stage3_green_gate_passed:
        gates = ", ".join(_stage3_green_failed_gate_names(diagnostics))
        return f"Stage 2 is possible, but Stage 3-Green gate failed: {gates}."
    return "All Stage 3-Green gates passed."


def _stage2_failed_gate_names(diagnostics: StageGateDiagnostics) -> tuple[str, ...]:
    return tuple(
        name
        for name in diagnostics.failed_gate_names
        if name.startswith("failed_stage2") or name == "failed_positive_stage_price_only_blowoff"
    )


def _stage3_green_failed_gate_names(diagnostics: StageGateDiagnostics) -> tuple[str, ...]:
    return tuple(
        name
        for name in diagnostics.failed_gate_names
        if not name.startswith("failed_stage2") and name != "failed_score_validity"
    )


def _audit_finding_values(findings: Sequence[Any], attr_name: str) -> str:
    values = {
        str(value)
        for finding in findings
        if (value := getattr(finding, attr_name, None)) not in (None, "")
    }
    return ", ".join(sorted(values))


def _source_field_text(scored: AsOfEvidenceBundleScore, key: str, valid_score: bool) -> str:
    if not valid_score:
        return ""
    source_fields = getattr(getattr(scored, "feature_result", None), "source_fields", None)
    if not isinstance(source_fields, Mapping):
        return ""
    value = source_fields.get(key)
    return "" if value in (None, "") else str(value)


_DEFICIT_GATES: tuple[tuple[str, str], ...] = (
    ("failed_stage3_total_score", "total"),
    ("failed_stage3_eps_fcf", "eps_fcf"),
    ("failed_stage3_visibility", "visibility"),
    ("failed_stage3_bottleneck", "bottleneck"),
    ("failed_stage3_market_mispricing", "mispricing"),
    ("failed_stage3_valuation", "valuation"),
    ("failed_stage3_revision", "revision"),
    ("failed_stage3_contract_quality", "contract"),
    ("failed_structural_visibility_quality", "structural_visibility"),
    ("failed_sector_visibility", "sector_visibility"),
    ("failed_sector_bottleneck", "sector_bottleneck"),
    ("failed_green_cross_evidence", "cross_evidence"),
    ("failed_domain_specific_evidence", "domain_evidence"),
    ("failed_stage3_yellow_calibrated_total", "yellow_total"),
)


def _gate_deficit(diagnostics: StageGateDiagnostics, gate_name: str, valid_score: bool) -> float | None:
    if not valid_score:
        return None
    detail = diagnostics.values_vs_thresholds.get(gate_name, {})
    if detail.get("passed") is True:
        return 0.0
    value = detail.get("value")
    threshold = detail.get("threshold")
    if not isinstance(value, (int, float)) or not isinstance(threshold, (int, float)):
        return None
    return round(max(float(threshold) - float(value), 0.0), 4)


def _gate_deficit_summary(diagnostics: StageGateDiagnostics, valid_score: bool) -> str:
    if not valid_score:
        return ""
    items: list[tuple[float, str]] = []
    for gate_name, label in _DEFICIT_GATES:
        deficit = _gate_deficit(diagnostics, gate_name, valid_score)
        if deficit is None or deficit <= 0:
            continue
        detail = diagnostics.values_vs_thresholds.get(gate_name, {})
        value = detail.get("value")
        threshold = detail.get("threshold")
        if isinstance(value, (int, float)) and isinstance(threshold, (int, float)):
            items.append((deficit, f"{label}:{float(value):.2f}/{float(threshold):.2f}(-{deficit:.2f})"))
    return "; ".join(text for _, text in sorted(items, reverse=True))


def render_autopsy_markdown(result: AsOfStagePromotionAutopsyResult) -> str:
    stage_counts = Counter(row.current_stage.value for row in result.rows)
    lines = [
        "# As-Of Stage Promotion Autopsy",
        "",
        "## Executive Summary",
        "",
        f"- candidates_analyzed: {len(result.rows)}",
        f"- Stage 2 count: {stage_counts.get(Stage.STAGE_2.value, 0)}",
        f"- Stage 3-Green count: {stage_counts.get(Stage.STAGE_3_GREEN.value, 0)}",
        f"- Stage 3-Yellow count: {stage_counts.get(Stage.STAGE_3_YELLOW.value, 0)}",
        f"- Stage 3-Red count: {stage_counts.get(Stage.STAGE_3_RED.value, 0)}",
        "",
        "Promotion is based on merged official plus web evidence. Stage thresholds were not changed.",
        "",
        "## Benchmark Gate Answers",
        "",
        "| company | appeared | first stage | autopsy stage | main explanation |",
        "| --- | --- | --- | --- | --- |",
    ]
    by_symbol = {row.symbol: row for row in result.rows}
    for item in result.benchmark_rows:
        symbol = str(item.get("symbol"))
        row = by_symbol.get(symbol)
        lines.append(
            f"| {item.get('company_name')} | {'yes' if item.get('appeared_in_candidates') else 'no'} | "
            f"{item.get('first_stage') or 'n/a'} | {row.current_stage.value if row else 'not analyzed'} | "
            f"{row.explanation if row else item.get('failure_stage', 'not selected for autopsy')} |"
        )
    lines.extend(
        [
            "",
            "## Candidate Gate Matrix",
            "",
            "| symbol | company | date | stage | band | sector | visible_score | score state | info | EPS/FCF | visibility | structural visibility | bottleneck | valuation | failed gates | top deficits |",
            "| --- | --- | --- | --- | --- | --- | ---: | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |",
        ]
    )
    for row in result.rows:
        failed_gates = [field.name for field in fields(row) if field.name.startswith("failed_") and getattr(row, field.name)]
        lines.append(
            f"| {row.symbol} | {row.company_name} | {row.as_of_date.isoformat()} | {row.current_stage.value} | {row.promotion_band} | {row.sector_profile} | "
            f"{_fmt_score(row.current_score)} | {_score_state_text(row)} | {_fmt_component(row.information_confidence)} | {_fmt_component(row.eps_fcf_explosion)} | "
            f"{_fmt_component(row.earnings_visibility)} | {_fmt_component(row.structural_visibility_quality)} | "
            f"{_fmt_component(row.bottleneck_pricing)} | {_fmt_component(row.valuation_rerating)} | "
            f"{', '.join(failed_gates) or 'none'} | {row.green_gate_deficit_summary or 'none'} |"
        )
    lines.extend(
        [
            "",
            "## What This Means",
            "",
            "- If a structural case remains Stage 1, the table shows whether the block is total score, EPS/FCF, visibility, bottleneck, valuation, revision, contract quality, Red Team, or audit.",
            "- If a case is Stage 2 but not Green, it means the candidate evidence improved but at least one strict Green gate still failed.",
            "- One-off and overheat labels should remain contained and should not be forced into Green.",
        ]
    )
    return "\n".join(lines).rstrip() + "\n"


def _write_outputs(result: AsOfStagePromotionAutopsyResult) -> Mapping[str, Path]:
    report_date = result.config.report_date or date.today()
    root = Path(result.config.output_directory)
    root.mkdir(parents=True, exist_ok=True)
    paths = {
        "autopsy_md": root / f"{report_date.isoformat()}_autopsy.md",
        "autopsy_json": root / f"{report_date.isoformat()}_autopsy.json",
        "score_components_csv": root / "score_components_by_candidate.csv",
        "stage_gate_matrix_csv": root / "stage_gate_matrix.csv",
        "feature_input_coverage_csv": root / "feature_input_coverage.csv",
    }
    paths["autopsy_md"].write_text(render_autopsy_markdown(result), encoding="utf-8")
    paths["autopsy_json"].write_text(json.dumps(_jsonable(result.rows), ensure_ascii=False, indent=2, sort_keys=True), encoding="utf-8")
    _write_csv(paths["score_components_csv"], result.rows, _score_component_fields())
    _write_csv(paths["stage_gate_matrix_csv"], result.rows, _gate_fields())
    _write_csv(paths["feature_input_coverage_csv"], result.rows, _coverage_fields())
    return paths


def _write_csv(path: Path, rows: Sequence[StagePromotionAutopsyRow], fieldnames: Sequence[str]) -> None:
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        for row in rows:
            item = _jsonable(row)
            writer.writerow({key: _csv_value(item.get(key)) for key in fieldnames})


def _csv_value(value: Any) -> Any:
    if isinstance(value, list):
        return "|".join(str(item) for item in value)
    return value


def _fmt_score(value: float | None) -> str:
    return "" if value is None else f"{value:.2f}"


def _score_state_text(row: StagePromotionAutopsyRow) -> str:
    if serialized_score_valid(row):
        return f"valid / fp {row.score_fingerprint or 'none'}"
    raw = f" / raw {_fmt_score(row.raw_score_before_block)}" if row.raw_score_before_block is not None else ""
    return f"pending {serialized_score_block_reason(row) or 'score_invalid'}{raw} / fp {row.score_fingerprint or 'none'}"


def _score_component_fields() -> tuple[str, ...]:
    return (
        "symbol",
        "company_name",
        "as_of_date",
        "layer",
        "current_stage",
        "current_score",
        "score_valid",
        "score_blocked_reason",
        "score_fingerprint",
        "research_input_fingerprint",
        "score_variability_drivers",
        "raw_score_before_block",
        "eps_fcf_explosion",
        "earnings_visibility",
        "bottleneck_pricing",
        "market_mispricing",
        "valuation_rerating",
        "capital_allocation",
        "information_confidence",
        "risk_penalty",
        "large_sector_id",
        "canonical_archetype_id",
        "archetype_weight_profile_applied",
        "archetype_weighted_total_before_calibration",
        "archetype_weight_eps_fcf_explosion",
        "archetype_weight_earnings_visibility",
        "archetype_weight_bottleneck_pricing",
        "archetype_weight_market_mispricing",
        "archetype_weight_valuation_rerating",
        "archetype_weight_capital_allocation",
        "archetype_weight_information_confidence",
        "archetype_component_eps_fcf_explosion",
        "archetype_component_earnings_visibility",
        "archetype_component_bottleneck_pricing",
        "archetype_component_market_mispricing",
        "archetype_component_valuation_rerating",
        "archetype_component_capital_allocation",
        "archetype_component_information_confidence",
        "archetype_green_policy_absolute_block",
        "archetype_green_policy_unlock_required",
        "archetype_green_policy_unlock_evidence",
        "archetype_green_restricted_by_profile",
        "revision_score",
        "price_stage_score",
        "contract_quality",
        "backlog_rpo_visibility",
        "capa_constraint",
        "asp_pricing_power",
        "structural_shortage",
        "one_off_shortage_risk",
        "structural_visibility_quality",
        "sector_visibility_score",
        "sector_bottleneck_score",
        "recurring_demand_visibility",
        "export_channel_visibility",
        "medium_term_revision_visibility",
        "domain_specific_evidence_score",
        "research_axis_bridge_present_count_capped",
        "research_axis_bridge_margin",
        "research_axis_bridge_customer",
        "research_axis_bridge_backlog",
        "research_axis_bridge_contract",
        "research_axis_bridge_valuation_repricing",
        "research_axis_bridge_capital_return",
        "research_axis_bridge_insurance_quality",
        "research_axis_bridge_bio_commercialization",
        "research_axis_bridge_software_retention",
        "research_axis_bridge_consumer_sell_through",
        "research_axis_bridge_guard_risk",
        "research_axis_bridge_guard_risk_penalty_points",
        "actual_profit_conversion_score",
        "bottleneck_industrial_raw",
        "bottleneck_sector_raw",
        "bottleneck_actual_conversion_raw",
        "bottleneck_validated_conversion_raw",
        "bottleneck_selected_raw",
        "bottleneck_selected_path",
        "bottleneck_component_before_one_off_penalty",
        "bottleneck_one_off_penalty_points",
        "bottleneck_raw_required_for_green",
        "bottleneck_raw_deficit_to_green",
        "sector_profile",
        "promotion_band",
        "cross_evidence_families_present",
        "missing_evidence_families",
        "stage3_total_deficit",
        "stage3_eps_fcf_deficit",
        "stage3_visibility_deficit",
        "stage3_bottleneck_deficit",
        "stage3_market_mispricing_deficit",
        "stage3_valuation_deficit",
        "stage3_revision_deficit",
        "stage3_contract_quality_deficit",
        "structural_visibility_deficit",
        "sector_visibility_deficit",
        "sector_bottleneck_deficit",
        "green_cross_evidence_deficit",
        "domain_specific_evidence_deficit",
        "stage3_yellow_total_deficit",
        "green_gate_deficit_summary",
        "red_team_risk",
        "hard_audit_count",
        "audit_finding_codes",
        "audit_finding_fields",
        "audit_finding_actions",
        "explanation",
    )


def _gate_fields() -> tuple[str, ...]:
    return (
        "symbol",
        "company_name",
        "as_of_date",
        "current_stage",
        "score_valid",
        "score_blocked_reason",
        "score_fingerprint",
        "research_input_fingerprint",
        "score_variability_drivers",
        "raw_score_before_block",
        "promotion_band",
        "sector_profile",
        "large_sector_id",
        "canonical_archetype_id",
        "archetype_weight_profile_applied",
        "archetype_weighted_total_before_calibration",
        "archetype_weight_eps_fcf_explosion",
        "archetype_weight_earnings_visibility",
        "archetype_weight_bottleneck_pricing",
        "archetype_weight_market_mispricing",
        "archetype_weight_valuation_rerating",
        "archetype_weight_capital_allocation",
        "archetype_weight_information_confidence",
        "archetype_component_eps_fcf_explosion",
        "archetype_component_earnings_visibility",
        "archetype_component_bottleneck_pricing",
        "archetype_component_market_mispricing",
        "archetype_component_valuation_rerating",
        "archetype_component_capital_allocation",
        "archetype_component_information_confidence",
        "archetype_green_policy_absolute_block",
        "archetype_green_policy_unlock_required",
        "archetype_green_policy_unlock_evidence",
        "archetype_green_restricted_by_profile",
        "failed_stage2_total_score",
        "failed_stage2_eps_fcf",
        "failed_stage2_valuation",
        "failed_stage2_information_confidence",
        "failed_stage3_total_score",
        "failed_stage3_eps_fcf",
        "failed_stage3_visibility",
        "failed_stage3_bottleneck",
        "failed_stage3_market_mispricing",
        "failed_stage3_valuation",
        "failed_stage3_revision",
        "failed_stage3_contract_quality",
        "failed_structural_visibility_quality",
        "failed_sector_visibility",
        "failed_sector_bottleneck",
        "failed_green_cross_evidence",
        "failed_report_date_confidence",
        "failed_date_unverified_green_evidence",
        "failed_domain_specific_evidence",
        "failed_stage3_red_team",
        "bottleneck_industrial_raw",
        "bottleneck_sector_raw",
        "bottleneck_actual_conversion_raw",
        "bottleneck_validated_conversion_raw",
        "bottleneck_selected_raw",
        "bottleneck_selected_path",
        "bottleneck_component_before_one_off_penalty",
        "bottleneck_one_off_penalty_points",
        "bottleneck_raw_required_for_green",
        "bottleneck_raw_deficit_to_green",
        "stage3_total_deficit",
        "stage3_eps_fcf_deficit",
        "stage3_visibility_deficit",
        "stage3_bottleneck_deficit",
        "stage3_market_mispricing_deficit",
        "stage3_valuation_deficit",
        "stage3_revision_deficit",
        "stage3_contract_quality_deficit",
        "structural_visibility_deficit",
        "sector_visibility_deficit",
        "sector_bottleneck_deficit",
        "green_cross_evidence_deficit",
        "domain_specific_evidence_deficit",
        "stage3_yellow_total_deficit",
        "green_gate_deficit_summary",
        "hard_audit_count",
        "audit_finding_codes",
        "audit_finding_fields",
        "audit_finding_actions",
    )


def _coverage_fields() -> tuple[str, ...]:
    return (
        "symbol",
        "company_name",
        "as_of_date",
        "current_stage",
        "score_valid",
        "score_blocked_reason",
        "score_fingerprint",
        "research_input_fingerprint",
        "score_variability_drivers",
        "raw_score_before_block",
        "price_bars_count",
        "financial_actuals_count",
        "disclosures_count",
        "research_reports_count",
        "news_items_count",
        "consensus_count",
        "consensus_revisions_count",
    )


def _select_candidate_rows(
    candidates: Sequence[Mapping[str, Any]],
    benchmark_rows: Sequence[Mapping[str, Any]],
    top_candidates: int | None,
) -> tuple[Mapping[str, Any], ...]:
    selected: dict[tuple[str, str], Mapping[str, Any]] = {}
    candidate_slice = candidates if top_candidates is None else candidates[:top_candidates]
    for item in candidate_slice:
        selected[(str(item["symbol"]), str(item["as_of_date"]))] = item
    by_symbol: dict[str, list[Mapping[str, Any]]] = {}
    for item in candidates:
        by_symbol.setdefault(str(item["symbol"]), []).append(item)
    for benchmark in benchmark_rows:
        if not benchmark.get("appeared_in_candidates"):
            continue
        symbol = str(benchmark.get("symbol"))
        first_date = str(benchmark.get("first_detected_date"))
        matches = [item for item in by_symbol.get(symbol, ()) if str(item.get("as_of_date")) == first_date]
        if matches:
            selected[(symbol, first_date)] = matches[0]
    return tuple(selected.values())


def _candidate_from_row(row: Mapping[str, Any]) -> CheapScanCandidate:
    layer = RecommendedNextLayer(str(row.get("layer") or "event_search"))
    return CheapScanCandidate(
        symbol=str(row["symbol"]),
        company_name=str(row["company_name"]),
        market=Market.KR,
        as_of_date=date.fromisoformat(str(row["as_of_date"])),
        reason_codes=tuple(row.get("reason_codes") or ()),
        cheap_scan_total_score=float(row.get("score") or row.get("merged_score") or 0.0),
        recommended_next_layer=layer,
        candidate_source_path=str(row.get("candidate_source_path") or "official_cheap_scan"),
    )


def _runtime_fixture_spec_paths(config: AsOfStagePromotionAutopsyConfig, asof_output: Path) -> tuple[str | Path, ...]:
    if config.runtime_fixture_spec_paths:
        return tuple(config.runtime_fixture_spec_paths)
    summary = _load_json(asof_output / "asof_replay_summary.json")
    if not isinstance(summary, Mapping):
        return ()
    replay_config = summary.get("config")
    if not isinstance(replay_config, Mapping):
        return ()
    paths = replay_config.get("runtime_fixture_spec_paths") or ()
    if isinstance(paths, (str, Path)):
        return (paths,)
    if isinstance(paths, Sequence):
        return tuple(str(item) for item in paths if item)
    return ()


def _load_json(path: Path) -> Any:
    if not path.exists():
        return []
    return json.loads(path.read_text(encoding="utf-8"))


def _diag(values: Mapping[str, Any], key: str) -> float:
    try:
        return float(values.get(key, 0.0))
    except (TypeError, ValueError):
        return 0.0


def _valid_diag(values: Mapping[str, Any], key: str, valid_score: bool) -> float | None:
    if not valid_score:
        return None
    return _diag(values, key)


def _fmt_component(value: float | None) -> str:
    return "" if value is None else f"{value:.2f}"


def _jsonable(value: Any) -> Any:
    if isinstance(value, (date, datetime)):
        return value.isoformat()
    if isinstance(value, Enum):
        return value.value
    if isinstance(value, Path):
        return str(value)
    if is_dataclass(value):
        payload = {field.name: _jsonable(getattr(value, field.name)) for field in fields(value)}
        if "score_valid" in payload:
            payload = normalized_score_state_payload(payload)
        return payload
    if isinstance(value, Mapping):
        return normalized_score_state_mapping_if_present({str(key): _jsonable(item) for key, item in value.items()})
    if isinstance(value, (list, tuple, set, frozenset)):
        return [_jsonable(item) for item in value]
    return value


__all__ = [
    "AsOfStagePromotionAutopsy",
    "AsOfStagePromotionAutopsyConfig",
    "AsOfStagePromotionAutopsyResult",
    "StagePromotionAutopsyRow",
    "render_autopsy_markdown",
]
