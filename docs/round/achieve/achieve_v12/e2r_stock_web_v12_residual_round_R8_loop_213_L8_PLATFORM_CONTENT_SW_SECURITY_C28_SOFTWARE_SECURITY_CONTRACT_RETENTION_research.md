# E2R v12 Stock-Web Residual Research — R8 / L8 / C28

```text
research_session = post_calibrated_sector_archetype_residual_research
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
production_scoring_changed = false
shadow_weight_only = true
handoff_prompt_embedded = true
handoff_prompt_executed_now = false
```

## 1. File Identity

```text
output_file = e2r_stock_web_v12_residual_round_R8_loop_213_L8_PLATFORM_CONTENT_SW_SECURITY_C28_SOFTWARE_SECURITY_CONTRACT_RETENTION_research.md
selected_round = R8
selected_loop = 213
large_sector_id = L8_PLATFORM_CONTENT_SW_SECURITY
canonical_archetype_id = C28_SOFTWARE_SECURITY_CONTRACT_RETENTION
fine_archetype_id = C28_ENTERPRISE_SOFTWARE_SECURITY_RENEWAL_REVENUE_DIRECT_ROW_REPAIR_V2
selection_basis = docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket = Priority 0 URL/proxy quality + Priority 1-style bridge quality reinforcement
round_schedule_status = coverage_index_selected
round_sector_consistency = pass
```

## 2. Selection Rationale / Novelty Check

The MAIN prompt requires coverage-index-first selection, not a strict R1→R13 cycle. The No-Repeat ledger shows all C01~C32 buckets already above 80 representative rows, so this run treats `C28_SOFTWARE_SECURITY_CONTRACT_RETENTION` as a quality-repair target: direct URL rows, renewal/revenue bridge, and profile-only false-positive separation.

Recent R8 work already covered C28 once through Genians / AhnLab / Douzone / Hancom / IGLOO style rows. This run avoids that exact basket and tests enterprise IT/SW/security names where the confusion is slightly different: **cloud/SI/ITO revenue bridge, automotive SW margin bridge, procurement SaaS profit conversion, and digital-ID contract without realized recurring revenue**.

Hard duplicate key used:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

Batch duplicate check result:

```text
new_independent_case_count = 7
new_independent_trigger_count = 7
unique_symbol_count = 4
reused_case_count = 0
same_symbol_new_trigger_count = 3
source_proxy_only_count = 0
evidence_url_pending_count = 0
```

## 3. Price Atlas Validation

```text
price_source = Songdaiki/stock-web
price_basis = tradable_raw
price_adjustment_status = raw_unadjusted_marcap
calibration_shard_root = atlas/ohlcv_tradable_by_symbol_year
manifest_max_date = 2026-02-20
tradable_schema = d,o,h,l,c,v,a,mc,s,m
```

Profile caveats checked:

```text
018260 Samsung SDS: corporate_action_candidate_count = 0
307950 Hyundai AutoEver: corporate_action_candidate_dates = [2021-04-14], outside all 2024/2025 windows
058970 EMRO: corporate_action_candidate_dates = [2022-01-17, 2022-02-09], outside all 2024/2025 windows
042510 RaonSecure: candidate date 2025-05-07 exists; only entry after 2025-05-07 is used
```

All usable rows use Stock-Web tradable rows. No raw/all rows are used for calibration.

## 4. Trigger-Level Backtest Table

| # | symbol | name | trigger_type | evidence_date | entry_date | entry_close | 30D MFE/MAE | 90D MFE/MAE | 180D MFE/MAE | peak_180D | trough_180D | role |
|---:|---|---|---|---|---|---:|---:|---:|---:|---|---|---|
| 1 | 018260 | Samsung SDS | Stage2-Actionable | 2024-04-30 | 2024-04-30 | 160100 | 7.31/-7.25 | 7.31/-16.36 | 7.31/-29.36 | 2024-05-23 | 2025-01-24 | direct_bridge_high_MAE_guardrail |
| 2 | 018260 | Samsung SDS | Stage2-Actionable | 2025-04-28 | 2025-04-28 | 127400 | 32.65/-3.14 | 56.04/-3.14 | 56.04/-3.14 | 2025-06-24 | 2025-04-28 | positive_reopen_after_2024_drawdown |
| 3 | 307950 | Hyundai AutoEver | Stage2-Actionable | 2024-07-26 | 2024-07-26 | 166500 | 3.54/-16.10 | 3.54/-26.13 | 3.54/-35.74 | 2024-07-30 | 2025-04-09 | direct_earnings_but_post_spike_drawdown |
| 4 | 307950 | Hyundai AutoEver | Stage2-Actionable | 2025-02-03 | 2025-02-03 | 144400 | 6.09/-11.84 | 6.09/-25.90 | 32.83/-25.90 | 2025-06-27 | 2025-04-09 | annual_result_positive_but_high_MAE |
| 5 | 058970 | EMRO | Stage4B | 2024-05-16 | 2024-05-16 | 67000 | 13.88/-16.42 | 13.88/-43.43 | 25.52/-43.43 | 2025-02-06 | 2024-08-08 | sales_record_but_profit_collapse_false_positive |
| 6 | 058970 | EMRO | Stage2-Actionable | 2025-04-18 | 2025-04-18 | 52700 | 15.75/-14.61 | 15.75/-22.77 | 15.75/-36.05 | 2025-04-25 | 2026-01-15 | q1_2025_revenue_growth_but_green_blocker |
| 7 | 042510 | RaonSecure | Stage2 | 2025-05-12 | 2025-05-12 | 9720 | 42.08/-7.10 | 42.08/-7.10 | 42.08/-7.92 | 2025-06-24 | 2026-01-19 | digital_id_contract_profile_only_cap |

## 5. Case Notes

### 5.1 Samsung SDS / 018260 — cloud and IT service bridge, but Green still needs cash/retention proof

- 2024-04-30 is a valid Stage2-Actionable row because IT-service revenue and cloud revenue were explicitly tied to the earnings release. However, the 180D path was only `+7.31% / -29.36%`, so this cannot be allowed to leak into Stage3-Green.
- 2025-04-28 is the cleaner reopen row: revenue and operating profit both increased YoY, and the 180D path improved to `+56.04% / -3.14%`. It supports Actionable preservation after a prior bad-entry period.

### 5.2 Hyundai AutoEver / 307950 — direct earnings bridge can still be a late-entry trap

- 2024-07-26 has direct earnings evidence, but the 180D path was `+3.54% / -35.74%`. The evidence was real, but the price location was wrong.
- 2025-02-03 has a stronger annual result bridge and later MFE recovered, but the 90D/180D drawdown still says Yellow/Green must wait for repeated margin / cash conversion.

### 5.3 EMRO / 058970 — SaaS/procurement profile must be separated from profit conversion

- 2024-05-16 is a false-positive repair row: record first-quarter sales alone looked like a software demand bridge, but operating profit collapsed. It should route to Stage4B/watch or capped Stage2, not Stage2-Actionable.
- 2025-04-18 is the reopen row because revenue growth and positive operating profit returned. The 180D MAE stayed deep at `-36.05%`, so Actionable survives but Green remains blocked.

### 5.4 RaonSecure / 042510 — digital ID contract is not recurring revenue yet

RaonSecure had a digital-ID contract/project route after the 2025-05-07 corporate-action candidate. Because there is still no direct recurring revenue, renewal, margin, or cash conversion evidence in this row, it is kept at Stage2 despite a favorable 180D path of `+42.08% / -7.92%`.

## 6. Aggregate Result

```text
calibration_usable_case_count = 7
calibration_usable_trigger_count = 7
positive_or_direct_bridge_count = 5
counterexample_or_guardrail_count = 2
stage2_count = 1
stage2_actionable_count = 5
stage4b_count = 1
stage4c_count = 0
high_MAE_180D_count = 5
source_proxy_only_count = 0
evidence_url_pending_count = 0
missing_required_mfe_mae_count = 0
missing_entry_price_count = 0
missing_actual_entry_ohlcv_count = 0
corporate_action_contaminated_180D_count = 0
insufficient_forward_window_180D_count = 0
```

## 7. Score / Return Alignment

| trigger_type | intended reading | observed path | calibration implication |
|---|---|---|---|
| Stage2-Actionable direct bridge | earnings / cloud / IT service / procurement-SaaS conversion exists | mixed: some high-MFE, some deep-MAE | preserve Actionable, block Yellow/Green until repeated conversion |
| Stage4B sales-without-profit | revenue headline but OP/margin collapsed | EMRO 2024 had deep MAE before later recovery | sales headline alone must not receive Actionable bonus |
| Stage2 profile/project-only | digital ID contract/profile without recurring revenue bridge | Raon had strong price path but missing revenue bridge | price path cannot backfill revenue/retention evidence |

## 8. Residual Contribution Summary

```text
rule_candidate = C28_RENEWAL_REVENUE_DIRECT_BRIDGE_AND_PROFILE_ONLY_GATE_V2
sector_rule_candidate = L8_ENTERPRISE_SW_SECURITY_CONTRACT_RETENTION_GATE_V2
loop_contribution_label = C28_direct_bridge_vs_profile_only_quality_repair
new_axis_proposed = false
existing_axis_strengthened = stage2_required_bridge, stage3_green_not_loosened, local_4b_watch_guard
existing_axis_weakened = none
production_scoring_changed = false
shadow_weight_only = true
```

Core residual:

```text
- Security / software / cloud / AI / digital-ID profile alone cannot create Stage2-Actionable, Stage3-Yellow, or Stage3-Green.
- Stage2-Actionable requires at least one issuer-level second bridge:
  recurring revenue, renewal, client-base growth, recognized service revenue,
  cloud/SI/ITO revenue conversion, operating-profit conversion, margin conversion,
  ARR/subscription retention, or repeat contract.
- Revenue growth without OP/margin conversion routes to Stage4B/watch or capped Stage2.
- High MAE on a valid direct bridge blocks Yellow/Green first; it does not delete Stage2-Actionable.
- Strong price path after profile-only / project-only evidence does not retroactively create recurring revenue quality.
- Stage3-Green remains blocked until revenue/retention/margin/cash conversion repeats across more than one evidence family.
```

## 9. Machine-Readable JSONL Trigger Rows

```jsonl
{"row_type": "trigger", "research_id": "R8_loop_213_C28_enterprise_sw_security_revenue_bridge", "round": "R8", "loop": 213, "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C28_SOFTWARE_SECURITY_CONTRACT_RETENTION", "fine_archetype_id": "C28_ENTERPRISE_SOFTWARE_SECURITY_RENEWAL_REVENUE_DIRECT_ROW_REPAIR_V2", "symbol": "018260", "name": "Samsung SDS", "trigger_type": "Stage2-Actionable", "evidence_date": "2024-04-30", "entry_date": "2024-04-30", "entry_price": 160100.0, "entry_ohlcv": {"o": 157400.0, "h": 164200.0, "l": 157300.0, "c": 160100.0, "v": 183368, "a": 29611358300.0, "mc": 12388185780000.0, "m": "KOSPI"}, "mfe_mae": {"mfe_30d_pct": 7.31, "mae_30d_pct": -7.25, "mfe_90d_pct": 7.31, "mae_90d_pct": -16.36, "mfe_180d_pct": 7.31, "mae_180d_pct": -29.36, "peak_180d_date": "2024-05-23", "trough_180d_date": "2025-01-24"}, "price_source_validation": "pass_stock_web_tradable_raw", "price_data_source": "Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_usable": true, "corporate_action_contaminated_180D": false, "insufficient_forward_window_180D": false, "raw_component_score_breakdown": {"eps_fcf_explosion": 14, "earnings_visibility": 22, "bottleneck_pricing": 8, "market_mispricing": 11, "valuation_rerating": 10, "capital_allocation": 4, "information_confidence": 18}, "raw_total_score": 87, "case_role": "direct_bridge_high_MAE_guardrail", "profile_error": "would_over_escalate_if_green_given", "evidence_summary": "1Q24 official result: revenue down YoY overall but operating profit rose 16.2%; IT-service revenue grew 5.7% YoY and cloud revenue grew 29% YoY. Direct second bridge exists, but forward path has deep 180D MAE.", "evidence_url": "https://www.samsungsds.com/us/news/1283793_5933.html", "hard_duplicate_key": "C28_SOFTWARE_SECURITY_CONTRACT_RETENTION|018260|Stage2-Actionable|2024-04-30"}
{"row_type": "trigger", "research_id": "R8_loop_213_C28_enterprise_sw_security_revenue_bridge", "round": "R8", "loop": 213, "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C28_SOFTWARE_SECURITY_CONTRACT_RETENTION", "fine_archetype_id": "C28_ENTERPRISE_SOFTWARE_SECURITY_RENEWAL_REVENUE_DIRECT_ROW_REPAIR_V2", "symbol": "018260", "name": "Samsung SDS", "trigger_type": "Stage2-Actionable", "evidence_date": "2025-04-28", "entry_date": "2025-04-28", "entry_price": 127400.0, "entry_ohlcv": {"o": 123400.0, "h": 128300.0, "l": 123400.0, "c": 127400.0, "v": 201789, "a": 25589657450.0, "mc": 9857931720000.0, "m": "KOSPI"}, "mfe_mae": {"mfe_30d_pct": 32.65, "mae_30d_pct": -3.14, "mfe_90d_pct": 56.04, "mae_90d_pct": -3.14, "mfe_180d_pct": 56.04, "mae_180d_pct": -3.14, "peak_180d_date": "2025-06-24", "trough_180d_date": "2025-04-28"}, "price_source_validation": "pass_stock_web_tradable_raw", "price_data_source": "Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_usable": true, "corporate_action_contaminated_180D": false, "insufficient_forward_window_180D": false, "raw_component_score_breakdown": {"eps_fcf_explosion": 17, "earnings_visibility": 24, "bottleneck_pricing": 8, "market_mispricing": 12, "valuation_rerating": 12, "capital_allocation": 5, "information_confidence": 18}, "raw_total_score": 96, "case_role": "positive_reopen_after_2024_drawdown", "profile_error": "prior_high_MAE_should_not_delete_stage2", "evidence_summary": "1Q25 official result: revenue +7.5% YoY and operating profit +18.9% YoY, with IT service revenue +3% YoY. This is a cleaner realized earnings bridge than the 2024 profile-only rows.", "evidence_url": "https://www.samsungsds.com/en/news/sdsfr-250428.html", "hard_duplicate_key": "C28_SOFTWARE_SECURITY_CONTRACT_RETENTION|018260|Stage2-Actionable|2025-04-28"}
{"row_type": "trigger", "research_id": "R8_loop_213_C28_enterprise_sw_security_revenue_bridge", "round": "R8", "loop": 213, "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C28_SOFTWARE_SECURITY_CONTRACT_RETENTION", "fine_archetype_id": "C28_ENTERPRISE_SOFTWARE_SECURITY_RENEWAL_REVENUE_DIRECT_ROW_REPAIR_V2", "symbol": "307950", "name": "Hyundai AutoEver", "trigger_type": "Stage2-Actionable", "evidence_date": "2024-07-26", "entry_date": "2024-07-26", "entry_price": 166500.0, "entry_ohlcv": {"o": 154000.0, "h": 167300.0, "l": 148000.0, "c": 166500.0, "v": 306342, "a": 49159899300.0, "mc": 4566093003000.0, "m": "KOSPI"}, "mfe_mae": {"mfe_30d_pct": 3.54, "mae_30d_pct": -16.1, "mfe_90d_pct": 3.54, "mae_90d_pct": -26.13, "mfe_180d_pct": 3.54, "mae_180d_pct": -35.74, "peak_180d_date": "2024-07-30", "trough_180d_date": "2025-04-09"}, "price_source_validation": "pass_stock_web_tradable_raw", "price_data_source": "Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_usable": true, "corporate_action_contaminated_180D": false, "insufficient_forward_window_180D": false, "raw_component_score_breakdown": {"eps_fcf_explosion": 16, "earnings_visibility": 23, "bottleneck_pricing": 8, "market_mispricing": 11, "valuation_rerating": 10, "capital_allocation": 5, "information_confidence": 16}, "raw_total_score": 89, "case_role": "direct_earnings_but_post_spike_drawdown", "profile_error": "direct_bridge_needs_late_extension_guard", "evidence_summary": "Q2 2024 article reports revenue around KRW 918.1bn and operating profit around KRW 68.5bn. Direct earnings bridge exists, but the entry arrived near a local peak and produced poor 90/180D path.", "evidence_url": "https://www.mk.co.kr/en/it/11077963", "hard_duplicate_key": "C28_SOFTWARE_SECURITY_CONTRACT_RETENTION|307950|Stage2-Actionable|2024-07-26"}
{"row_type": "trigger", "research_id": "R8_loop_213_C28_enterprise_sw_security_revenue_bridge", "round": "R8", "loop": 213, "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C28_SOFTWARE_SECURITY_CONTRACT_RETENTION", "fine_archetype_id": "C28_ENTERPRISE_SOFTWARE_SECURITY_RENEWAL_REVENUE_DIRECT_ROW_REPAIR_V2", "symbol": "307950", "name": "Hyundai AutoEver", "trigger_type": "Stage2-Actionable", "evidence_date": "2025-02-03", "entry_date": "2025-02-03", "entry_price": 144400.0, "entry_ohlcv": {"o": 140200.0, "h": 146800.0, "l": 138000.0, "c": 144400.0, "v": 133052, "a": 18922005600.0, "mc": 3960023000800.0, "m": "KOSPI"}, "mfe_mae": {"mfe_30d_pct": 6.09, "mae_30d_pct": -11.84, "mfe_90d_pct": 6.09, "mae_90d_pct": -25.9, "mfe_180d_pct": 32.83, "mae_180d_pct": -25.9, "peak_180d_date": "2025-06-27", "trough_180d_date": "2025-04-09"}, "price_source_validation": "pass_stock_web_tradable_raw", "price_data_source": "Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_usable": true, "corporate_action_contaminated_180D": false, "insufficient_forward_window_180D": false, "raw_component_score_breakdown": {"eps_fcf_explosion": 17, "earnings_visibility": 24, "bottleneck_pricing": 9, "market_mispricing": 12, "valuation_rerating": 12, "capital_allocation": 5, "information_confidence": 16}, "raw_total_score": 95, "case_role": "annual_result_positive_but_high_MAE", "profile_error": "green_escalation_too_early_if_no_cash_retention", "evidence_summary": "FY2024 result coverage reports annual revenue and operating profit growth; Q4 operating profit grew 37.4% YoY. Strong bridge, but 90D MAE remained deep, so Green should stay blocked.", "evidence_url": "https://biz.chosun.com/en/en-it/2025/02/03/RFBFCOQNJNAUFMDS4MZYR3Z6Y4/", "hard_duplicate_key": "C28_SOFTWARE_SECURITY_CONTRACT_RETENTION|307950|Stage2-Actionable|2025-02-03"}
{"row_type": "trigger", "research_id": "R8_loop_213_C28_enterprise_sw_security_revenue_bridge", "round": "R8", "loop": 213, "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C28_SOFTWARE_SECURITY_CONTRACT_RETENTION", "fine_archetype_id": "C28_ENTERPRISE_SOFTWARE_SECURITY_RENEWAL_REVENUE_DIRECT_ROW_REPAIR_V2", "symbol": "058970", "name": "EMRO", "trigger_type": "Stage4B", "evidence_date": "2024-05-16", "entry_date": "2024-05-16", "entry_price": 67000.0, "entry_ohlcv": {"o": 68000.0, "h": 69500.0, "l": 66300.0, "c": 67000.0, "v": 147447, "a": 9997206700.0, "mc": 751212040000.0, "m": "KOSDAQ"}, "mfe_mae": {"mfe_30d_pct": 13.88, "mae_30d_pct": -16.42, "mfe_90d_pct": 13.88, "mae_90d_pct": -43.43, "mfe_180d_pct": 25.52, "mae_180d_pct": -43.43, "peak_180d_date": "2025-02-06", "trough_180d_date": "2024-08-08"}, "price_source_validation": "pass_stock_web_tradable_raw", "price_data_source": "Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_usable": true, "corporate_action_contaminated_180D": false, "insufficient_forward_window_180D": false, "raw_component_score_breakdown": {"eps_fcf_explosion": 5, "earnings_visibility": 12, "bottleneck_pricing": 5, "market_mispricing": 10, "valuation_rerating": 8, "capital_allocation": 4, "information_confidence": 20}, "raw_total_score": 64, "case_role": "sales_record_but_profit_collapse_false_positive", "profile_error": "headline_sales_should_not_get_actionable_bonus", "evidence_summary": "Q1 2024 record first-quarter sales were reported, but operating profit fell 97% YoY. Revenue/profile headline alone should be capped; this is a 4B/watch or Stage2 false-positive repair row.", "evidence_url": "https://www.mk.co.kr/en/it/11017211", "hard_duplicate_key": "C28_SOFTWARE_SECURITY_CONTRACT_RETENTION|058970|Stage4B|2024-05-16"}
{"row_type": "trigger", "research_id": "R8_loop_213_C28_enterprise_sw_security_revenue_bridge", "round": "R8", "loop": 213, "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C28_SOFTWARE_SECURITY_CONTRACT_RETENTION", "fine_archetype_id": "C28_ENTERPRISE_SOFTWARE_SECURITY_RENEWAL_REVENUE_DIRECT_ROW_REPAIR_V2", "symbol": "058970", "name": "EMRO", "trigger_type": "Stage2-Actionable", "evidence_date": "2025-04-18", "entry_date": "2025-04-18", "entry_price": 52700.0, "entry_ohlcv": {"o": 53700.0, "h": 54100.0, "l": 52300.0, "c": 52700.0, "v": 72542, "a": 3826341300.0, "mc": 643540305700.0, "m": "KOSDAQ"}, "mfe_mae": {"mfe_30d_pct": 15.75, "mae_30d_pct": -14.61, "mfe_90d_pct": 15.75, "mae_90d_pct": -22.77, "mfe_180d_pct": 15.75, "mae_180d_pct": -36.05, "peak_180d_date": "2025-04-25", "trough_180d_date": "2026-01-15"}, "price_source_validation": "pass_stock_web_tradable_raw", "price_data_source": "Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_usable": true, "corporate_action_contaminated_180D": false, "insufficient_forward_window_180D": false, "raw_component_score_breakdown": {"eps_fcf_explosion": 13, "earnings_visibility": 21, "bottleneck_pricing": 8, "market_mispricing": 12, "valuation_rerating": 10, "capital_allocation": 5, "information_confidence": 18}, "raw_total_score": 87, "case_role": "q1_2025_revenue_growth_but_green_blocker", "profile_error": "actionable_valid_but_green_blocked_by_mae", "evidence_summary": "Q1 2025 revenue rose 41% to KRW 20.6bn, with operating profit and net income positive. This repairs the 2024 sales-without-profit false-positive, but forward MAE still blocks Yellow/Green.", "evidence_url": "https://biz.chosun.com/en/en-it/2025/04/18/5AR6VLFXAZHR5PCSQEHOIPG42U/", "hard_duplicate_key": "C28_SOFTWARE_SECURITY_CONTRACT_RETENTION|058970|Stage2-Actionable|2025-04-18"}
{"row_type": "trigger", "research_id": "R8_loop_213_C28_enterprise_sw_security_revenue_bridge", "round": "R8", "loop": 213, "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C28_SOFTWARE_SECURITY_CONTRACT_RETENTION", "fine_archetype_id": "C28_ENTERPRISE_SOFTWARE_SECURITY_RENEWAL_REVENUE_DIRECT_ROW_REPAIR_V2", "symbol": "042510", "name": "RaonSecure", "trigger_type": "Stage2", "evidence_date": "2025-05-12", "entry_date": "2025-05-12", "entry_price": 9720.0, "entry_ohlcv": {"o": 9700.0, "h": 9760.0, "l": 9620.0, "c": 9720.0, "v": 60489, "a": 585890390.0, "mc": 108914291280.0, "m": "KOSDAQ"}, "mfe_mae": {"mfe_30d_pct": 42.08, "mae_30d_pct": -7.1, "mfe_90d_pct": 42.08, "mae_90d_pct": -7.1, "mfe_180d_pct": 42.08, "mae_180d_pct": -7.92, "peak_180d_date": "2025-06-24", "trough_180d_date": "2026-01-19"}, "price_source_validation": "pass_stock_web_tradable_raw", "price_data_source": "Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_usable": true, "corporate_action_contaminated_180D": false, "insufficient_forward_window_180D": false, "raw_component_score_breakdown": {"eps_fcf_explosion": 8, "earnings_visibility": 16, "bottleneck_pricing": 8, "market_mispricing": 14, "valuation_rerating": 12, "capital_allocation": 4, "information_confidence": 16}, "raw_total_score": 78, "case_role": "digital_id_contract_profile_only_cap", "profile_error": "price_path_strong_but_conversion_bridge_absent", "evidence_summary": "OmniOne digital ID partnership/project evidence exists, but the row is still project/profile exposure without realized revenue, renewal, ARR, or margin conversion. Entry is after the 2025-05-07 corporate-action candidate.", "evidence_url": "https://biz.chosun.com/en/en-it/2025/05/12/A3QKCUGIUVHAHD5AZENUM75MNY/", "hard_duplicate_key": "C28_SOFTWARE_SECURITY_CONTRACT_RETENTION|042510|Stage2|2025-05-12"}
```

## 10. Deferred Coding Agent Handoff Prompt

```text
This handoff prompt is embedded for later batch implementation only. Do not execute it in this research run.

Task:
Read this MD as one v12 residual research input. Parse the JSONL trigger rows and evaluate whether the candidate rule below should be batched with other C28/L8 evidence:

candidate_rule_id = C28_RENEWAL_REVENUE_DIRECT_BRIDGE_AND_PROFILE_ONLY_GATE_V2
scope = large_sector_id:L8_PLATFORM_CONTENT_SW_SECURITY + canonical_archetype_id:C28_SOFTWARE_SECURITY_CONTRACT_RETENTION
intended_effect:
- require issuer-level recurring/contract/revenue/margin bridge before Stage2-Actionable
- keep Green strict when the row has high MAE or lacks repeated retention/cash evidence
- route sales-without-profit rows to local 4B/watch
- do not promote project/profile-only digital ID/security/SW rows even when later price path is strong

Constraints:
- Do not change production scoring from this MD alone.
- Apply only as shadow / candidate patch if supported by adjacent C28 and R13 rows.
- Respect hard duplicate key canonical_archetype_id + symbol + trigger_type + entry_date.
```

## 11. Batch Ingest Self-Audit

```text
required_filename_regex_pass = true
filename_round_matches_metadata = true
filename_loop_matches_metadata = true
large_sector_id_valid = true
round_sector_consistency = pass
canonical_archetype_id_valid = true
stock_web_price_rows_used = true
actual_entry_ohlcv_included = true
complete_30_90_180_mfe_mae_in_every_trigger_row = true
jsonl_trigger_rows_present = true
calibration_usable_rows_missing_mfe_mae = 0
source_proxy_only_count = 0
evidence_url_pending_count = 0
production_scoring_changed = false
shadow_weight_only = true
handoff_prompt_embedded = true
handoff_prompt_executed_now = false
```

## 12. Next Research State

```text
completed_round = R8
completed_loop = 213
selection_basis = docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket = Priority 0 URL/proxy quality + C28 direct bridge quality reinforcement
round_schedule_status = coverage_index_selected
round_sector_consistency = pass
next_recommended_archetypes =
- C05_EPC_MEGA_CONTRACT_MARGIN_GAP_WORKING_CAPITAL_CASHFLOW_ONLY_REPAIR
- C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE_SUPPLIER_ORDER_DIRECT_URL_REPAIR
- C13_BATTERY_JV_UTILIZATION_AMPC_IRA_EX_SUBSIDY_MARGIN_DIRECT_REPAIR
- C16_STRATEGIC_RESOURCE_POLICY_SUPPLY_DIRECT_OFFTAKE_POSITIVE_CONTROL_REPAIR
- R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL_HOLDOUT_REFRESH
```
