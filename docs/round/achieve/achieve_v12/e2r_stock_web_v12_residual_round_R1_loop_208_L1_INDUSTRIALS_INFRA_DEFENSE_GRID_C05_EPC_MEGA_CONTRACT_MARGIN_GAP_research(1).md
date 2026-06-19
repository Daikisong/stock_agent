# E2R v12 Stock-Web Residual Research — R1 / C05 midsize contractor cost-rate and working-capital gate

```text
research_session = post_calibrated_sector_archetype_residual_research_v12
selected_round = R1
selected_loop = 208
large_sector_id = L1_INDUSTRIALS_INFRA_DEFENSE_GRID
canonical_archetype_id = C05_EPC_MEGA_CONTRACT_MARGIN_GAP
fine_archetype_id = C05_MIDSIZE_CONTRACTOR_COST_RATE_WORKING_CAPITAL_GATE_V6
selection_basis = docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket = Priority 1 balance reinforcement / URL-proxy quality repair
round_schedule_status = coverage_index_selected
round_sector_consistency = pass
production_scoring_changed = false
shadow_weight_only = true
```

## 1. Selection memo

`V12_Research_No_Repeat_Index.md` says the corpus has moved beyond simple 30/50/80-row filling. The remaining high-value work is direct-URL quality repair, source-proxy reduction, and balance reinforcement. Within Priority 1, `C05_EPC_MEGA_CONTRACT_MARGIN_GAP` remains one of the lower-row quality targets and specifically asks for margin / working-capital failure cases and 4C timing repair.

This loop keeps the selected canonical in R1/L1, but avoids the recently repeated large EPC names. The chosen sample moves to midsize contractors, semiconductor utility EPC, regional builders, and weak-credit contractors where the second bridge is not simply “order/backlog exists” but **cost-rate recovery, operating-profit conversion, liquidity support, receivable collection, or working-capital/cashflow visibility**.

Hard duplicate key used for avoidance:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

## 2. Price atlas validation

```text
price_source = Songdaiki/stock-web
upstream_source = FinanceData/marcap
manifest_max_date = 2026-02-20
price_basis = tradable_raw
price_adjustment_status = raw_unadjusted_marcap
calibration_shard_root = atlas/ohlcv_tradable_by_symbol_year
schema = d,o,h,l,c,v,a,mc,s,m
```

MFE/MAE calculation follows the stock-web schema:

```text
MFE_N_pct = (max high from entry_date through N tradable rows / entry_price - 1) * 100
MAE_N_pct = (min low from entry_date through N tradable rows / entry_price - 1) * 100
```

All six usable trigger rows have 30/90/180D MFE and MAE, an actual entry OHLC row, and no D~D+180 corporate-action contamination in the checked profile window. One Sambu Construction audit row is retained as narrative-only because the 180D forward window is insufficient in stock-web.

## 3. Trigger result table

| symbol | company | trigger | entry | entry close | 30D MFE/MAE | 90D MFE/MAE | 180D MFE/MAE | case role |
|---|---|---|---:|---:|---:|---:|---:|---|
| 034300 | Shinsegae E&C | Stage4B | 2024-03-21 | 10,890 | 6.15 / -9.55 | 71.26 / -9.55 | 71.26 / -9.55 | counterexample_guardrail |
| 045100 | Hanyang ENG | Stage2-Actionable | 2025-05-14 | 16,550 | 11.54 / -5.50 | 23.56 / -5.50 | 105.14 / -5.50 | positive_control |
| 001260 | Namkwang E&C | Stage2 | 2025-03-13 | 8,160 | 5.88 / -11.15 | 50.00 / -11.15 | 50.00 / -14.71 | positive_but_capped |
| 035890 | Seohee Construction | Stage2-Actionable | 2024-08-14 | 1,342 | 17.14 / -2.53 | 25.19 / -2.53 | 33.46 / -2.53 | positive_guarded |
| 002780 | ChinHung International | Stage4B | 2025-03-14 | 784 | 4.85 / -11.86 | 6.76 / -11.86 | 6.76 / -20.79 | counterexample_guardrail |
| 002410 | Bumyang Construction | Stage4C | 2023-12-21 | 2,185 | 7.32 / -21.05 | 7.32 / -38.22 | 7.32 / -48.51 | counterexample_hard4c |


Narrative-only blocked row:

| symbol | company | trigger | entry | reason | available rows | 30D MFE/MAE | 90D MFE/MAE |
|---|---|---|---:|---|---:|---:|---:|
| 001470 | Sambu Construction | Stage4C | 2024-08-19 | insufficient_forward_window_180D_in_stock_web | 140 | 13.28 / -40.38 | 120.87 / -40.38 |

## 4. Case notes

### 4.1 034300 Shinsegae E&C — Stage4B, liquidity-support offset after margin break

The issuer had a real construction-margin and leverage problem, so a positive Stage2 reading is not justified. However, the board-approved KRW 650bn hybrid-capital package and parent support created a strong offset. The forward path shows why C05 should avoid sticky hard 4C when explicit parent liquidity support, deleveraging route, and restructuring mechanics are present. This row is a **4B/watch over hard-4C** guardrail.

### 4.2 045100 Hanyang ENG — Stage2-Actionable, semiconductor utility EPC reopen

Hanyang ENG belongs to C05 because the evidence is semiconductor fab utility / special facility EPC, not semiconductor equipment order conversion. The row is valid Actionable only because the evidence is not a generic “chip capex” headline; it has issuer-level EPC / service route and earnings-disclosure visibility. The 180D path is strong, but C05 Green remains blocked until cashflow / working-capital conversion is repeated.

### 4.3 001260 Namkwang E&C — Stage2 cap, public-civil contract bridge without cash conversion

Namkwang has an official reporting route and public civil/building contractor evidence, but the row remains Stage2 because the available evidence is not enough to show cash conversion or a durable margin bridge. The 180D MFE is good, but that is not enough to loosen Green.

### 4.4 035890 Seohee Construction — Stage2-Actionable, backlog and earnings support with housing concentration cap

Seohee has backlog and earnings support, but its regional-housing / private-housing concentration means C05 should not automatically read this as a clean EPC margin bridge. Actionable is allowed because operating performance and secured backlog are visible; Yellow/Green is blocked by concentration and working-capital risk.

### 4.5 002780 ChinHung International — Stage4B, low OPM / receivable watch

ChinHung is a useful 4B/watch row because the evidence points to weak OPM and receivable / liquidity pressure. The later improvement possibility from new starts and backlog means the system should avoid instant hard 4C unless cashflow, liquidity, or order collapse is confirmed.

### 4.6 002410 Bumyang Construction — hard Stage4C, cost delay and liquidity stress

Bumyang is the direct negative control. The evidence family is not merely weak share price; it is repeated losses, delay penalties, cost pressure, debt/liquidity stress, and deteriorating balance-sheet ratios. The 180D path is downside-dominant and supports hard 4C protection.

### 4.7 001470 Sambu Construction — narrative-only audit hard-4C row

The August 2024 audit-review rejection / management-item row is important for C05 taxonomy, but stock-web only provides 140 tradable rows from the entry date to the latest tradable row for this symbol. It is therefore kept as narrative-only and not used for weight calibration.

## 5. Residual contribution

```text
loop_contribution_label = C05_midsize_contractor_cost_rate_working_capital_gate
new_axis_proposed = false
existing_axis_strengthened = stage2_required_bridge, earlier_thesis_break_watch, hard_4c_confirmation
existing_axis_refined = offset_quality_before_sticky_4c, working_capital_cashflow_second_bridge
existing_axis_weakened = none_global
production_scoring_changed = false
shadow_weight_only = true
```

Core residual:

```text
- C05 order/backlog/revenue headline alone cannot create Stage2-Actionable, Yellow, or Green.
- Stage2-Actionable requires at least one direct second bridge:
  cost-rate recovery, operating-profit conversion, working-capital release,
  receivable collection improvement, debt/net-cash improvement,
  parent liquidity support with restructuring mechanics, high-margin project recognition,
  or cashflow visibility.
- Ugly earnings with explicit parent liquidity, net-cash, project-mix, or backlog offset routes first to Stage4B/watch before sticky hard 4C.
- Hard Stage4C requires confirmed non-price thesis break:
  sustained operating loss, liquidity stress, auditor rejection, working-capital failure,
  order/backlog collapse, accounting/trust break, or weak offset quality.
- High MFE after ugly earnings is a warning against hard-4C stickiness.
- High MAE on valid bridge rows blocks Stage3-Yellow/Green first; it does not erase Stage2-Actionable.
```

## 6. Shadow rule candidate

```text
canonical_archetype_rule_candidate = C05_MIDSIZE_CONTRACTOR_WORKING_CAPITAL_CASHFLOW_GATE_V6
sector_rule_candidate = L1_CONTRACTOR_COST_RATE_LIQUIDITY_AND_REOPEN_GATE_V6
```

Proposed shadow behavior:

```text
if canonical_archetype_id == C05_EPC_MEGA_CONTRACT_MARGIN_GAP:
    if evidence in [generic_backlog, generic_revenue_growth, new_order_headline] and no second_bridge:
        cap_stage = Stage2
    if second_bridge in [cost_rate_recovery, op_conversion, working_capital_release,
                         receivable_collection, debt_reduction, parent_liquidity_support,
                         high_margin_project_recognition, cashflow_visibility]:
        allow_stage2_actionable = true
    if ugly_earnings and explicit_offset_quality >= medium:
        prefer_stage4b_watch_over_hard4c = true
    if liquidity_stress or auditor_rejection or repeated_operating_loss or working_capital_failure:
        allow_hard4c = true
    if 180d_mae_pct <= -20 and no cashflow_or_working_capital_bridge:
        block_stage3_green = true
```

## 7. Machine-readable JSONL

```jsonl
{"row_type": "trigger", "research_file": "e2r_stock_web_v12_residual_round_R1_loop_208_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C05_EPC_MEGA_CONTRACT_MARGIN_GAP_research.md", "selected_round": "R1", "selected_loop": 208, "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C05_EPC_MEGA_CONTRACT_MARGIN_GAP", "fine_archetype_id": "C05_MIDSIZE_CONTRACTOR_COST_RATE_WORKING_CAPITAL_GATE_V6", "symbol": "034300", "company_name": "Shinsegae E&C", "trigger_type": "Stage4B", "trigger_date": "2024-03-21", "entry_date": "2024-03-21", "entry_price": 10890.0, "entry_ohlcv": {"o": 10900.0, "h": 11190.0, "l": 10830.0, "c": 10890.0}, "mfe_30d_pct": 6.15, "mae_30d_pct": -9.55, "peak_30d_date": "2024-03-27", "trough_30d_date": "2024-04-26", "mfe_90d_pct": 71.26, "mae_90d_pct": -9.55, "peak_90d_date": "2024-05-30", "trough_90d_date": "2024-04-26", "mfe_180d_pct": 71.26, "mae_180d_pct": -9.55, "peak_180d_date": "2024-05-30", "trough_180d_date": "2024-04-26", "price_source_validation": {"price_source": "Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "available_rows_from_entry": 207, "calibration_usable": true, "corporate_action_contaminated_180D": false, "insufficient_forward_window_180D": false}, "evidence": {"summary": "2023 large operating loss and high leverage created 4B/watch, but parent liquidity/hybrid capital support gave a strong offset; use as hard-4C overstickiness guard.", "source_url": "https://shinsegae-enc.com/news-dtl?id=118"}, "score_simulation": {"component_breakdown": {"eps_fcf_explosion": 4, "earnings_visibility": 8, "bottleneck_pricing": 2, "market_mispricing": 8, "valuation_rerating": 4, "capital_allocation": 10, "information_confidence": 18, "total": 54}, "current_profile_stage_interpretation": "Stage4B"}, "residual_contribution": {"case_role": "counterexample_guardrail", "residual_label": "liquidity_support_offset_after_margin_break"}, "production_scoring_changed": false, "shadow_weight_only": true}
{"row_type": "trigger", "research_file": "e2r_stock_web_v12_residual_round_R1_loop_208_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C05_EPC_MEGA_CONTRACT_MARGIN_GAP_research.md", "selected_round": "R1", "selected_loop": 208, "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C05_EPC_MEGA_CONTRACT_MARGIN_GAP", "fine_archetype_id": "C05_MIDSIZE_CONTRACTOR_COST_RATE_WORKING_CAPITAL_GATE_V6", "symbol": "045100", "company_name": "Hanyang ENG", "trigger_type": "Stage2-Actionable", "trigger_date": "2025-05-14", "entry_date": "2025-05-14", "entry_price": 16550.0, "entry_ohlcv": {"o": 16430.0, "h": 16580.0, "l": 16390.0, "c": 16550.0}, "mfe_30d_pct": 11.54, "mae_30d_pct": -5.5, "peak_30d_date": "2025-06-26", "trough_30d_date": "2025-05-19", "mfe_90d_pct": 23.56, "mae_90d_pct": -5.5, "peak_90d_date": "2025-09-15", "trough_90d_date": "2025-05-19", "mfe_180d_pct": 105.14, "mae_180d_pct": -5.5, "peak_180d_date": "2026-01-29", "trough_180d_date": "2025-05-19", "price_source_validation": {"price_source": "Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "available_rows_from_entry": 189, "calibration_usable": true, "corporate_action_contaminated_180D": false, "insufficient_forward_window_180D": false}, "evidence": {"summary": "semiconductor fab utility/EPC exposure plus earnings-disclosure route; strong forward path shows supplier/EPC second bridge can reopen Actionable when customer capex resumes.", "source_url": "https://kind.krx.co.kr/common/disclsviewer.do?acptno=20250313002442&docno=&method=search&viewerhost="}, "score_simulation": {"component_breakdown": {"eps_fcf_explosion": 16, "earnings_visibility": 19, "bottleneck_pricing": 8, "market_mispricing": 11, "valuation_rerating": 8, "capital_allocation": 7, "information_confidence": 14, "total": 83}, "current_profile_stage_interpretation": "Stage2-Actionable"}, "residual_contribution": {"case_role": "positive_control", "residual_label": "semiconductor_epc_order_profit_reopen"}, "production_scoring_changed": false, "shadow_weight_only": true}
{"row_type": "trigger", "research_file": "e2r_stock_web_v12_residual_round_R1_loop_208_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C05_EPC_MEGA_CONTRACT_MARGIN_GAP_research.md", "selected_round": "R1", "selected_loop": 208, "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C05_EPC_MEGA_CONTRACT_MARGIN_GAP", "fine_archetype_id": "C05_MIDSIZE_CONTRACTOR_COST_RATE_WORKING_CAPITAL_GATE_V6", "symbol": "001260", "company_name": "Namkwang E&C", "trigger_type": "Stage2", "trigger_date": "2025-03-13", "entry_date": "2025-03-13", "entry_price": 8160.0, "entry_ohlcv": {"o": 8360.0, "h": 8500.0, "l": 8160.0, "c": 8160.0}, "mfe_30d_pct": 5.88, "mae_30d_pct": -11.15, "peak_30d_date": "2025-04-21", "trough_30d_date": "2025-03-31", "mfe_90d_pct": 50.0, "mae_90d_pct": -11.15, "peak_90d_date": "2025-06-12", "trough_90d_date": "2025-03-31", "mfe_180d_pct": 50.0, "mae_180d_pct": -14.71, "peak_180d_date": "2025-06-12", "trough_180d_date": "2025-11-19", "price_source_validation": {"price_source": "Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "available_rows_from_entry": 230, "calibration_usable": true, "corporate_action_contaminated_180D": false, "insufficient_forward_window_180D": false}, "evidence": {"summary": "public civil/building contractor with official report route; revenue/order visibility supports Stage2 but not Actionable absent cash-conversion evidence.", "source_url": "https://www.namkwang.co.kr/ManageInfo"}, "score_simulation": {"component_breakdown": {"eps_fcf_explosion": 12, "earnings_visibility": 16, "bottleneck_pricing": 5, "market_mispricing": 9, "valuation_rerating": 7, "capital_allocation": 7, "information_confidence": 12, "total": 68}, "current_profile_stage_interpretation": "Stage2"}, "residual_contribution": {"case_role": "positive_but_capped", "residual_label": "public_contract_backlog_stage2_cap"}, "production_scoring_changed": false, "shadow_weight_only": true}
{"row_type": "trigger", "research_file": "e2r_stock_web_v12_residual_round_R1_loop_208_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C05_EPC_MEGA_CONTRACT_MARGIN_GAP_research.md", "selected_round": "R1", "selected_loop": 208, "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C05_EPC_MEGA_CONTRACT_MARGIN_GAP", "fine_archetype_id": "C05_MIDSIZE_CONTRACTOR_COST_RATE_WORKING_CAPITAL_GATE_V6", "symbol": "035890", "company_name": "Seohee Construction", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-08-14", "entry_date": "2024-08-14", "entry_price": 1342.0, "entry_ohlcv": {"o": 1308.0, "h": 1352.0, "l": 1308.0, "c": 1342.0}, "mfe_30d_pct": 17.14, "mae_30d_pct": -2.53, "peak_30d_date": "2024-09-30", "trough_30d_date": "2024-08-14", "mfe_90d_pct": 25.19, "mae_90d_pct": -2.53, "peak_90d_date": "2024-12-18", "trough_90d_date": "2024-08-14", "mfe_180d_pct": 33.46, "mae_180d_pct": -2.53, "peak_180d_date": "2025-04-22", "trough_180d_date": "2024-08-14", "price_source_validation": {"price_source": "Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "available_rows_from_entry": 239, "calibration_usable": true, "corporate_action_contaminated_180D": false, "insufficient_forward_window_180D": false}, "evidence": {"summary": "regional housing-contracting model retains earnings and backlog support, but private-housing concentration keeps Green blocked.", "source_url": "https://m.kisrating.com/fileDown.do?fileName=rs20250619-69.pdf&gubun=2&menuCd=R8"}, "score_simulation": {"component_breakdown": {"eps_fcf_explosion": 15, "earnings_visibility": 18, "bottleneck_pricing": 5, "market_mispricing": 10, "valuation_rerating": 9, "capital_allocation": 8, "information_confidence": 13, "total": 78}, "current_profile_stage_interpretation": "Stage2-Actionable"}, "residual_contribution": {"case_role": "positive_guarded", "residual_label": "secured_backlog_but_housing_concentration_cap"}, "production_scoring_changed": false, "shadow_weight_only": true}
{"row_type": "trigger", "research_file": "e2r_stock_web_v12_residual_round_R1_loop_208_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C05_EPC_MEGA_CONTRACT_MARGIN_GAP_research.md", "selected_round": "R1", "selected_loop": 208, "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C05_EPC_MEGA_CONTRACT_MARGIN_GAP", "fine_archetype_id": "C05_MIDSIZE_CONTRACTOR_COST_RATE_WORKING_CAPITAL_GATE_V6", "symbol": "002780", "company_name": "ChinHung International", "trigger_type": "Stage4B", "trigger_date": "2025-03-14", "entry_date": "2025-03-14", "entry_price": 784.0, "entry_ohlcv": {"o": 775.0, "h": 791.0, "l": 775.0, "c": 784.0}, "mfe_30d_pct": 4.85, "mae_30d_pct": -11.86, "peak_30d_date": "2025-04-08", "trough_30d_date": "2025-04-16", "mfe_90d_pct": 6.76, "mae_90d_pct": -11.86, "peak_90d_date": "2025-04-29", "trough_90d_date": "2025-04-16", "mfe_180d_pct": 6.76, "mae_180d_pct": -20.79, "peak_180d_date": "2025-04-29", "trough_180d_date": "2025-11-10", "price_source_validation": {"price_source": "Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "available_rows_from_entry": 229, "calibration_usable": true, "corporate_action_contaminated_180D": false, "insufficient_forward_window_180D": false}, "evidence": {"summary": "profitability below downgrade-monitoring threshold and receivable/liquidity pressure route to 4B/watch; later project-start offset prevents automatic 4C.", "source_url": "https://m.kisrating.com/fileDown.do?fileName=rs20250619-38.pdf&gubun=2&menuCd=R8"}, "score_simulation": {"component_breakdown": {"eps_fcf_explosion": 6, "earnings_visibility": 10, "bottleneck_pricing": 3, "market_mispricing": 7, "valuation_rerating": 4, "capital_allocation": 5, "information_confidence": 18, "total": 53}, "current_profile_stage_interpretation": "Stage4B"}, "residual_contribution": {"case_role": "counterexample_guardrail", "residual_label": "low_opm_receivable_watch_not_hard4c"}, "production_scoring_changed": false, "shadow_weight_only": true}
{"row_type": "trigger", "research_file": "e2r_stock_web_v12_residual_round_R1_loop_208_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C05_EPC_MEGA_CONTRACT_MARGIN_GAP_research.md", "selected_round": "R1", "selected_loop": 208, "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C05_EPC_MEGA_CONTRACT_MARGIN_GAP", "fine_archetype_id": "C05_MIDSIZE_CONTRACTOR_COST_RATE_WORKING_CAPITAL_GATE_V6", "symbol": "002410", "company_name": "Bumyang Construction", "trigger_type": "Stage4C", "trigger_date": "2023-12-21", "entry_date": "2023-12-21", "entry_price": 2185.0, "entry_ohlcv": {"o": 2175.0, "h": 2230.0, "l": 2135.0, "c": 2185.0}, "mfe_30d_pct": 7.32, "mae_30d_pct": -21.05, "peak_30d_date": "2024-01-02", "trough_30d_date": "2024-01-25", "mfe_90d_pct": 7.32, "mae_90d_pct": -38.22, "peak_90d_date": "2024-01-02", "trough_90d_date": "2024-04-16", "mfe_180d_pct": 7.32, "mae_180d_pct": -48.51, "peak_180d_date": "2024-01-02", "trough_180d_date": "2024-09-09", "price_source_validation": {"price_source": "Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "available_rows_from_entry": 299, "calibration_usable": true, "corporate_action_contaminated_180D": false, "insufficient_forward_window_180D": false}, "evidence": {"summary": "multi-year losses, delay penalties, cost pressure, and weak financial ratios are direct thesis-break evidence; 180D path confirms downside-dominant row.", "source_url": "https://ssl.pstatic.net/imgstock/upload/research/company/1703202682401.pdf"}, "score_simulation": {"component_breakdown": {"eps_fcf_explosion": 2, "earnings_visibility": 6, "bottleneck_pricing": 2, "market_mispricing": 4, "valuation_rerating": 2, "capital_allocation": 2, "information_confidence": 20, "total": 38}, "current_profile_stage_interpretation": "Stage4C"}, "residual_contribution": {"case_role": "counterexample_hard4c", "residual_label": "cost_delay_penalty_liquidity_hard4c"}, "production_scoring_changed": false, "shadow_weight_only": true}
{"row_type": "narrative_only", "research_file": "e2r_stock_web_v12_residual_round_R1_loop_208_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C05_EPC_MEGA_CONTRACT_MARGIN_GAP_research.md", "selected_round": "R1", "selected_loop": 208, "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C05_EPC_MEGA_CONTRACT_MARGIN_GAP", "symbol": "001470", "company_name": "Sambu Construction", "trigger_type": "Stage4C", "trigger_date": "2024-08-19", "entry_date": "2024-08-19", "entry_price": 738.0, "mfe_30d_pct": 13.28, "mae_30d_pct": -40.38, "mfe_90d_pct": 120.87, "mae_90d_pct": -40.38, "calibration_usable": false, "blocked_reason": "insufficient_forward_window_180D_in_stock_web", "source_url": "https://www.mk.co.kr/en/stock/11095664", "production_scoring_changed": false, "shadow_weight_only": true}
```

## 8. Batch Ingest Self-Audit

```text
standard_v12_filename = true
filename = e2r_stock_web_v12_residual_round_R1_loop_208_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C05_EPC_MEGA_CONTRACT_MARGIN_GAP_research.md
filename_round = R1
metadata_round = R1
filename_loop = 208
metadata_loop = 208
large_sector_id = L1_INDUSTRIALS_INFRA_DEFENSE_GRID
canonical_archetype_id = C05_EPC_MEGA_CONTRACT_MARGIN_GAP
round_sector_consistency = pass
selected_priority_bucket = Priority 1 balance reinforcement / URL-proxy quality repair
source_proxy_only_count = 0
evidence_url_pending_count = 0
missing_required_mfe_mae_count = 0
missing_entry_price_count = 0
missing_actual_entry_ohlcv_count = 0
corporate_action_contaminated_180D_count = 0
insufficient_forward_window_180D_count = 0
narrative_only_blocked_count = 1
calibration_usable_trigger_count = 6
new_independent_case_count = 6
new_independent_trigger_count = 6
unique_symbol_count_usable = 6
production_scoring_changed = false
shadow_weight_only = true
ready_for_batch_ingest = true
```

## 9. Deferred Coding Agent Handoff Prompt

```text
Do not execute during this research session.

When batch-applying v12 research, parse this MD as one C05 residual research input.
Use only calibration_usable=true trigger rows for aggregate / promotion decisions.
Keep the Sambu Construction audit row as narrative-only taxonomy evidence until a full 180D tradable window can be validated or a separate earlier as-of row is found.
Evaluate whether C05 should add a midsize contractor working-capital/cashflow second-bridge gate.
Do not loosen Stage3-Green globally.
Do not change production scoring outside the C05/L1 scoped candidate.
```

## 10. Next Research State

```text
completed_round = R1
completed_loop = 208
selection_basis = docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket = Priority 1 balance reinforcement / URL-proxy quality repair
next_recommended_archetypes =
  - C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE_SUPPLIER_ORDER_DIRECT_URL_REPAIR
  - C13_BATTERY_JV_UTILIZATION_AMPC_IRA_EX_SUBSIDY_MARGIN_DIRECT_REPAIR
  - C16_STRATEGIC_RESOURCE_POLICY_SUPPLY_DIRECT_OFFTAKE_POSITIVE_CONTROL_REPAIR
  - C01_ORDER_BACKLOG_MARGIN_BRIDGE_WORKING_CAPITAL_CASHFLOW_ONLY_REPAIR
  - R13_CROSS_ARCHETYPE_4B_4C_REDTEAM_OFFSET_QUALITY_REFRESH
round_schedule_status = coverage_index_selected
round_sector_consistency = pass
```
