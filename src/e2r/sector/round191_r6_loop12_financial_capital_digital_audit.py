"""Round-191 audit over the R6 Loop-12 financial/capital/digital pack.

Round 191 repeats the R6 Loop-12 design with emphasis on whether Round 190
actually captured the required targets, stage gates, price fields, and
guardrails. This module is a calibration audit only. Production feature
engineering, scoring, staging, and RedTeam code must not import it.
"""

from __future__ import annotations

import csv
import json
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable, Mapping

from e2r.sector.round190_r6_loop12_financial_capital_digital import (
    ROUND190_PRICE_FIELDS,
    ROUND190_SOURCE_CANONICAL_TARGET_IDS,
    round190_case_candidate_rows,
    round190_case_records,
    round190_score_profile_rows,
    round190_stage_cap_rows,
    round190_summary,
)


ROUND191_SOURCE_ROUND_PATH = "docs/round/round_191.md"
ROUND191_DEFAULT_OUTPUT_DIRECTORY = "output/e2r_round191_r6_loop12_financial_capital_digital_audit"
ROUND191_DEFAULT_AUDIT_PATH = "data/sector_taxonomy/round191_r6_loop12_financial_capital_digital_audit.json"

ROUND191_REQUIRED_TARGETS: tuple[str, ...] = (
    "INSURANCE_NAV_VALUEUP_SAMSUNG_ELECTRONICS_STAKE",
    "SHAREHOLDER_RETURN_COMPOUNDING_FINANCIAL_HOLDCO",
    "DIGITAL_ASSET_BANK_EQUITY_OPTION",
    "KRW_STABLECOIN_POLICY_THEME",
    "PAYMENT_BIOMETRIC_INFRASTRUCTURE",
    "PAYMENT_PRIVACY_REGULATORY_4C",
    "CREDIT_INFORMATION_RECURRING_DATA",
    "SECURITIES_BROKERAGE_MARKET_BETA",
    "BUYBACK_EXECUTION_PRICE_FAILED",
    "POLICY_TAX_REVERSAL_MARKET_SHOCK",
    "DISCLOSURE_CONFIDENCE_CAP",
)

ROUND191_REQUIRED_CASES: tuple[str, ...] = (
    "samsung_life_insurance_nav_valueup_stage23_case",
    "meritz_financial_shareholder_return_stage23_case",
    "hana_financial_dunamu_equity_option_stage2_case",
    "toss_facepay_payment_biometric_stage2_case",
    "nice_credit_information_recurring_data_stage23_case",
    "krw_stablecoin_policy_theme_4b_watch_case",
    "kakaopay_privacy_regulatory_4c_watch_case",
    "samsung_electronics_buyback_execution_price_failed_case",
    "policy_tax_reversal_market_shock_4c_watch_case",
    "securities_brokerage_market_beta_cycle_case",
    "stablecoin_related_stock_price_only_rally_case",
    "digital_asset_exchange_security_incident_4c_reference_case",
    "r6_loop12_disclosure_confidence_reference_case",
)

ROUND191_REQUIRED_STAGE3_CHECKS: tuple[str, ...] = (
    "roe_or_net_profit_improves_yoy",
    "cet1_kics_or_csm_stable",
    "actual_buyback_cancel_or_dividend_expansion_executed",
    "credit_cost_or_pf_reserve_stable",
    "stage2_60d_mfe_20pct",
    "pbr_band_rises_from_history",
    "repeat_return_policy_or_midterm_tsr_target",
    "digital_take_rate_issuance_or_equity_method_income_confirmed",
    "no_privacy_security_regulatory_hard_issue",
)

ROUND191_REQUIRED_STAGE4B_CHECKS: tuple[str, ...] = (
    "stage2_120d_mfe_60pct",
    "valueup_stablecoin_or_dunamu_keyword_doubles_price_before_earnings",
    "pbr_rerating_ahead_of_roe_eps",
    "actual_cancellation_equity_method_or_take_rate_missing",
    "policy_or_regulatory_framework_unclear",
    "financial_basket_crowded",
)

ROUND191_REQUIRED_STAGE4C_HARD_GATES: tuple[str, ...] = (
    "cet1_or_kics_falls_sharply",
    "pf_credit_cost_spike",
    "buyback_cancelled_or_return_cut",
    "large_capital_raise_or_capital_pressure",
    "exchange_hack_or_abnormal_withdrawal",
    "privacy_or_biometric_data_leak",
    "stablecoin_regulation_damages_issuer_margin",
    "tax_policy_shock_hits_valueup_basket",
    "buyback_price_fail_and_operating_concern_dominates",
)

ROUND191_REQUIRED_PRICE_FIELDS: tuple[str, ...] = (
    "roe",
    "roe_change_yoy",
    "net_profit_growth_yoy",
    "cet1_ratio",
    "k_ics_ratio",
    "csm",
    "credit_cost",
    "pf_exposure",
    "dividend_per_share",
    "buyback_amount",
    "cancelled_share_amount",
    "total_shareholder_return_ratio",
    "eps_accretion_from_buyback",
    "pbr_band_percentile",
    "nav_discount",
    "major_equity_stake_value",
    "digital_asset_stake_value",
    "equity_method_income",
    "stablecoin_issuance_volume",
    "reserve_income",
    "take_rate",
    "merchant_count",
    "user_count",
    "transaction_volume",
    "privacy_fine_flag",
    "biometric_data_risk_flag",
    "exchange_security_incident_flag",
    "regulatory_approval_pending",
    "tax_policy_shock_flag",
    "disclosure_confidence",
)


@dataclass(frozen=True)
class Round191AuditCheck:
    check_id: str
    status: str
    expected_count: int
    actual_count: int
    missing_items: tuple[str, ...]
    notes: str

    def as_row(self) -> dict[str, str]:
        return {
            "check_id": self.check_id,
            "status": self.status,
            "expected_count": str(self.expected_count),
            "actual_count": str(self.actual_count),
            "missing_items": "|".join(self.missing_items),
            "notes": self.notes,
            "production_scoring_changed": "false",
        }


def round191_audit_checks() -> tuple[Round191AuditCheck, ...]:
    score_targets = {row["target_id"] for row in round190_score_profile_rows()}
    case_ids = {row["case_id"] for row in round190_case_candidate_rows()}
    caps = {row["stage_band"]: row for row in round190_stage_cap_rows()}
    price_fields = set(ROUND190_PRICE_FIELDS)
    records = round190_case_records()
    hard_gate_targets = {
        row["target_id"]
        for row in round190_score_profile_rows()
        if row["hard_gate"] == "true"
    }

    checks = (
        _check(
            "required_targets_present",
            ROUND191_REQUIRED_TARGETS,
            score_targets,
            "Round191 required target list must be covered by the Round190 pack.",
        ),
        _check(
            "required_case_records_present",
            ROUND191_REQUIRED_CASES,
            case_ids,
            "Round191 named Stage 2/3, 4B, 4C, price-fail, and confidence-cap cases must exist.",
        ),
        _check(
            "stage3_six_of_nine_checks_present",
            ROUND191_REQUIRED_STAGE3_CHECKS,
            _split_required(caps["Stage 3"]["required_evidence"]),
            "Stage 3 remains strict: at least 6 of 9 checks are required.",
        ),
        _check(
            "stage4b_four_of_six_checks_present",
            ROUND191_REQUIRED_STAGE4B_CHECKS,
            _split_required(caps["Stage 4B"]["required_evidence"]),
            "Stage 4B cools crowded value-up, Dunamu, stablecoin, and FacePay rallies.",
        ),
        _check(
            "stage4c_hard_gates_present",
            ROUND191_REQUIRED_STAGE4C_HARD_GATES,
            _split_required(caps["Stage 4C"]["required_evidence"]),
            "Stage 4C hard gates cover capital, credit, security, privacy, policy, and buyback price-fail breaks.",
        ),
        _check(
            "price_fields_present",
            ROUND191_REQUIRED_PRICE_FIELDS,
            price_fields,
            "Round191 price-path and financial backfill fields must exist before any future scoring implementation.",
        ),
        Round191AuditCheck(
            "hard_gate_target_count",
            "pass" if len(hard_gate_targets) == 3 else "fail",
            3,
            len(hard_gate_targets),
            tuple(sorted({"PAYMENT_PRIVACY_REGULATORY_4C", "BUYBACK_EXECUTION_PRICE_FAILED", "POLICY_TAX_REVERSAL_MARKET_SHOCK"} - hard_gate_targets)),
            "The three explicit Round191 hard-gate targets should remain hard gates.",
        ),
        Round191AuditCheck(
            "case_records_not_production_input",
            "pass" if all("do_not_use_case_as_candidate_input" in record.green_guardrails for record in records) else "fail",
            len(records),
            sum(1 for record in records if "do_not_use_case_as_candidate_input" in record.green_guardrails),
            (),
            "Round191 is audit/calibration material only; case records must not become candidate-generation input.",
        ),
        Round191AuditCheck(
            "production_scoring_unchanged",
            "pass" if round190_summary()["production_scoring_changed"] is False else "fail",
            1,
            1 if round190_summary()["production_scoring_changed"] is False else 0,
            (),
            "Round191 confirms no production scoring threshold or StageClassifier change.",
        ),
    )
    return checks


def round191_audit_summary() -> dict[str, int | bool | str]:
    checks = round191_audit_checks()
    passed = sum(1 for check in checks if check.status == "pass")
    return {
        "source_round": ROUND191_SOURCE_ROUND_PATH,
        "audited_round": "round_190",
        "audit_check_count": len(checks),
        "passed_check_count": passed,
        "failed_check_count": len(checks) - passed,
        "required_target_count": len(ROUND191_REQUIRED_TARGETS),
        "required_case_count": len(ROUND191_REQUIRED_CASES),
        "required_price_field_count": len(ROUND191_REQUIRED_PRICE_FIELDS),
        "round190_case_candidate_count": round190_summary()["case_candidate_count"],
        "round190_hard_gate_target_count": round190_summary()["hard_gate_target_count"],
        "production_scoring_changed": False,
        "case_records_are_candidate_generation_input": False,
    }


def round191_audit_rows() -> tuple[dict[str, str], ...]:
    return tuple(check.as_row() for check in round191_audit_checks())


def write_round191_r6_loop12_audit_reports(
    *,
    output_directory: str | Path = ROUND191_DEFAULT_OUTPUT_DIRECTORY,
    audit_path: str | Path = ROUND191_DEFAULT_AUDIT_PATH,
) -> dict[str, Path]:
    output = Path(output_directory)
    output.mkdir(parents=True, exist_ok=True)
    audit = Path(audit_path)
    audit.parent.mkdir(parents=True, exist_ok=True)
    paths = {
        "audit_json": audit,
        "summary": output / "round191_r6_loop12_audit_summary.md",
        "coverage_matrix": output / "round191_r6_loop12_coverage_matrix.csv",
        "backfill_plan": output / "round191_r6_loop12_followup_backfill.md",
        "guardrail_review": output / "round191_r6_loop12_guardrail_review.md",
    }
    audit.write_text(json.dumps(round191_audit_payload(), ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    _write_rows(round191_audit_rows(), paths["coverage_matrix"])
    paths["summary"].write_text(render_round191_summary_markdown(), encoding="utf-8")
    paths["backfill_plan"].write_text(render_round191_followup_backfill_markdown(), encoding="utf-8")
    paths["guardrail_review"].write_text(render_round191_guardrail_review_markdown(), encoding="utf-8")
    return paths


def round191_audit_payload() -> dict[str, object]:
    return {
        "summary": round191_audit_summary(),
        "checks": [check.as_row() for check in round191_audit_checks()],
        "required_targets": list(ROUND191_REQUIRED_TARGETS),
        "required_cases": list(ROUND191_REQUIRED_CASES),
        "required_price_fields": list(ROUND191_REQUIRED_PRICE_FIELDS),
        "production_scoring_changed": False,
        "case_records_are_candidate_generation_input": False,
    }


def render_round191_summary_markdown() -> str:
    summary = round191_audit_summary()
    lines = [
        "# Round-191 R6 Loop-12 Financial / Capital / Digital Audit",
        "",
        f"- source_round: `{ROUND191_SOURCE_ROUND_PATH}`",
        "- audited_pack: `round190_r6_loop12_financial_capital_digital`",
        f"- audit_check_count: {summary['audit_check_count']}",
        f"- passed_check_count: {summary['passed_check_count']}",
        f"- failed_check_count: {summary['failed_check_count']}",
        f"- required_target_count: {summary['required_target_count']}",
        f"- required_case_count: {summary['required_case_count']}",
        f"- required_price_field_count: {summary['required_price_field_count']}",
        f"- round190_case_candidate_count: {summary['round190_case_candidate_count']}",
        f"- round190_hard_gate_target_count: {summary['round190_hard_gate_target_count']}",
        "- production_scoring_changed: false",
        "- case_records_are_candidate_generation_input: false",
        "",
        "## Interpretation",
        "",
        "- Round191 is a follow-up audit, not a second copy of the same case pack.",
        "- Example: Samsung Life remains Stage 2 until K-ICS, CSM, ROE/profit, return execution, and price path are backfilled.",
        "- Example: KRW stablecoin price spikes stay 4B-watch until issuance, reserve income, take-rate, and regulation are verified.",
        "- Example: KakaoPay privacy, tax reversal, and buyback price-fail are hard gates, not score bonuses.",
    ]
    return "\n".join(lines) + "\n"


def render_round191_followup_backfill_markdown() -> str:
    lines = [
        "# Round-191 R6 Loop-12 Follow-up Backfill Plan",
        "",
        "Round191 confirms that the schema exists. The next step is evidence backfill, not production score changes.",
        "",
        "## Required Backfill Groups",
        "",
        "- Insurance NAV: `nav_discount`, `major_equity_stake_value`, `k_ics_ratio`, `csm`, `roe`, `dividend_per_share`.",
        "- Shareholder return: `buyback_amount`, `cancelled_share_amount`, `total_shareholder_return_ratio`, `eps_accretion_from_buyback`.",
        "- Digital asset bank option: `digital_asset_stake_value`, `equity_method_income`, `regulatory_approval_pending`, `exchange_security_incident_flag`.",
        "- Stablecoin theme: `stablecoin_issuance_volume`, `reserve_income`, `take_rate`, `stablecoin_regulatory_status`.",
        "- Biometric payment: `merchant_count`, `user_count`, `transaction_volume`, `biometric_data_risk_flag`.",
        "- Financial cycle / policy risk: `relative_strength_vs_financial_basket`, `credit_cost`, `pf_exposure`, `tax_policy_shock_flag`.",
        "",
        "## What Not To Change",
        "",
        "- Do not lower Stage 3-Green thresholds to improve recall.",
        "- Do not treat low-PBR, value-up, stablecoin, Dunamu, FacePay, or buyback headlines as structural evidence by themselves.",
        "- Do not use Round190/Round191 case records as candidate-generation input.",
        "- Do not invent missing ROE, capital-ratio, take-rate, issuance, security, or stage-price fields.",
    ]
    return "\n".join(lines) + "\n"


def render_round191_guardrail_review_markdown() -> str:
    lines = [
        "# Round-191 R6 Loop-12 Guardrail Review",
        "",
        "| check | status | missing |",
        "| --- | --- | --- |",
    ]
    for check in round191_audit_checks():
        lines.append(f"| `{check.check_id}` | {check.status} | {', '.join(check.missing_items) or '-'} |")
    lines.extend(
        [
            "",
            "## Plain-English Examples",
            "",
            "- `저PBR + 밸류업`은 출발점이다. ROE, 자본비율, 실제 환원, 가격경로가 없으면 Stage 1~2에 머문다.",
            "- `스테이블코인 + 급등`은 관심 신호다. 발행량과 수익모델이 없으면 4B-watch다.",
            "- `자사주 소각`은 좋은 증거일 수 있다. 하지만 발표 뒤 가격이 실패하고 본업 우려가 크면 Green 근거가 아니다.",
        ]
    )
    return "\n".join(lines) + "\n"


def _check(
    check_id: str,
    required: Iterable[str],
    actual: Iterable[str],
    notes: str,
) -> Round191AuditCheck:
    required_set = set(required)
    actual_set = set(actual)
    missing = tuple(sorted(required_set - actual_set))
    return Round191AuditCheck(
        check_id=check_id,
        status="pass" if not missing else "fail",
        expected_count=len(required_set),
        actual_count=len(required_set & actual_set),
        missing_items=missing,
        notes=notes,
    )


def _split_required(value: str) -> set[str]:
    return {item for item in value.split("|") if item}


def _write_rows(rows: Iterable[Mapping[str, str]], path: Path) -> None:
    rows = tuple(rows)
    if not rows:
        path.write_text("", encoding="utf-8")
        return
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=tuple(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)


__all__ = [
    "ROUND191_DEFAULT_AUDIT_PATH",
    "ROUND191_DEFAULT_OUTPUT_DIRECTORY",
    "ROUND191_REQUIRED_CASES",
    "ROUND191_REQUIRED_PRICE_FIELDS",
    "ROUND191_REQUIRED_STAGE3_CHECKS",
    "ROUND191_REQUIRED_STAGE4B_CHECKS",
    "ROUND191_REQUIRED_STAGE4C_HARD_GATES",
    "ROUND191_REQUIRED_TARGETS",
    "ROUND191_SOURCE_ROUND_PATH",
    "render_round191_followup_backfill_markdown",
    "render_round191_guardrail_review_markdown",
    "render_round191_summary_markdown",
    "round191_audit_checks",
    "round191_audit_payload",
    "round191_audit_rows",
    "round191_audit_summary",
    "write_round191_r6_loop12_audit_reports",
]
