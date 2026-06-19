# E2R v12 residual research — R10/L9/C30 PF balance-sheet break

```text
output_file_name = e2r_stock_web_v12_residual_round_R10_loop_221_L9_CONSTRUCTION_REALESTATE_HOUSING_C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK_research.md
selected_round = R10
selected_loop = 221
large_sector_id = L9_CONSTRUCTION_REALESTATE_HOUSING
canonical_archetype_id = C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK
fine_archetype_id = C30_PF_WORKOUT_LIQUIDITY_AND_REOPEN_GATE_V1
selection_basis = docs/core/V12_Research_No_Repeat_Index.md
round_schedule_status = coverage_index_selected
round_sector_consistency = pass
production_scoring_changed = false
shadow_weight_only = true
```

## 1. Execution scope

This file follows `docs/core/e2r_v12_prompt_round_scheduler_corrected.txt`: no `stock_agent` code access, no code patch, no live scan, no current recommendation, and no production scoring change. The only output is a standalone Markdown research handoff using actual Songdaiki/stock-web daily OHLCV rows.

The No-Repeat Index is used as the duplicate ledger and coverage guide. Since all C01~C32 canonical archetypes are already above the 80-row floor, this run selects a quality-repair path rather than a row-count filler. C30 has a high URL/proxy burden and a meaningful 4B/4C balance need, so the selected target is PF/workout/liquidity break versus reopen/offset quality in construction/real-estate balance sheets.

## 2. Stock-Web manifest validation

```text
price_source = Songdaiki/stock-web
upstream_source = FinanceData/marcap
manifest_max_date = 2026-02-20
price_basis = tradable_raw
price_adjustment_status = raw_unadjusted_marcap
calibration_shard_root = atlas/ohlcv_tradable_by_symbol_year
tradable_schema = d,o,h,l,c,v,a,mc,s,m
forward_window_basis = stock_web_manifest_max_date, not current date
```

All usable trigger rows below use the tradable calibration shard. Taeyoung E&C is kept as narrative-only because its 180-trading-day forward window crosses a corporate-action candidate date in the profile.

## 3. Novelty and duplicate check

```text
hard_duplicate_key = canonical_archetype_id + symbol + trigger_type + entry_date
selected_canonical = C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK
new_usable_trigger_count = 6
narrative_only_blocked_count = 1
unique_symbol_count_usable = 6
source_proxy_only_count = 0
evidence_url_pending_count = 0
missing_required_mfe_mae_count = 0
corporate_action_contaminated_180D_count_for_usable_rows = 0
insufficient_forward_window_180D_count_for_usable_rows = 0
```

The session already had repeated C05 contractor rows. This run deliberately moves the same construction stress vocabulary into the proper C30 balance-sheet/PF archetype and uses a different duplicate key space. Same-sector overlap is not counted as duplication because the canonical archetype and thesis are different.

## 4. Evidence design

C30 is not a generic “builder earnings” bucket. It asks a narrower question: when does PF exposure, debt maturity, receivables, cost-rate pressure, workout/liquidity support, or audit/trust stress become a balance-sheet thesis break rather than a temporary 4B/watch event?

Evidence references used in this run:

- Taeyoung E&C debt workout and PF-liquidity event: Reuters, FSC, YNA.
- Shinsegae E&C PF-driven loss/liquidity stress and management reset: Asiae, KED Global.
- Bumyang Construction financial statement / operating-income row: English DART annual report.
- Seohee Construction order backlog and new-order evidence: Asiae.
- KCC E&C official financial information: company IR page.
- HL D&I Halla official financial page and Reuters/MarketScreener earnings-event snippets.
- Ilsung Construction reported consolidated performance: English DART.

## 5. Trigger-level backtest table

| symbol | company | trigger | entry | entry close | 30D MFE/MAE | 90D MFE/MAE | 180D MFE/MAE | role |
|---|---|---|---:|---:|---:|---:|---:|---|
| 034300 | Shinsegae E&C | Stage4B | 2024-03-21 | 10890 | 6.15 / -9.55 | 71.26 / -9.55 | 71.26 / -9.55 | liquidity_support_watch |
| 002410 | Bumyang Construction | Stage4C | 2023-12-21 | 2185 | 7.32 / -22.47 | 7.32 / -38.22 | 7.32 / -48.51 | small_builder_loss_debt_break |
| 035890 | Seohee Construction | Stage2-Actionable | 2024-08-14 | 1342 | 17.29 / -2.53 | 25.19 / -2.53 | 33.46 / -2.53 | backlog_order_positive_control |
| 014790 | HL D&I Halla | Stage4B | 2025-02-06 | 2280 | 9.21 / -9.21 | 24.56 / -9.21 | 35.75 / -9.21 | profit_decline_with_order_offset_watch |
| 021320 | KCC E&C | Stage2-Actionable | 2025-02-28 | 3955 | 8.34 / -3.92 | 50.70 / -3.92 | 50.70 / -3.92 | profit_balance_sheet_positive_control |
| 013360 | Ilsung Construction | Stage4C | 2025-02-25 | 3520 | 41.05 / -23.01 | 41.05 / -52.27 | 41.05 / -66.14 | operating_loss_margin_break |


## 6. Actual Stock-Web entry rows

| symbol | entry OHLCV source row | 180D peak/trough | validation |
|---|---|---|---|
| 034300 | `atlas/ohlcv_tradable_by_symbol_year/034/034300/2024.csv` / 2024-03-21 o=10900, h=11190, l=10830, c=10890, v=2875 | peak=2024-05-30, trough=2024-04-26 | usable=true, corp_action_180D=false |
| 002410 | `atlas/ohlcv_tradable_by_symbol_year/002/002410/2023.csv` / 2023-12-21 o=2175, h=2230, l=2135, c=2185, v=180833 | peak=2024-01-02, trough=2024-09-09 | usable=true, corp_action_180D=false |
| 035890 | `atlas/ohlcv_tradable_by_symbol_year/035/035890/2024.csv` / 2024-08-14 o=1308, h=1352, l=1308, c=1342, v=408782 | peak=2025-04-22, trough=2024-08-14 | usable=true, corp_action_180D=false |
| 014790 | `atlas/ohlcv_tradable_by_symbol_year/014/014790/2025.csv` / 2025-02-06 o=2230, h=2280, l=2070, c=2280, v=50488 | peak=2025-08-08, trough=2025-02-06 | usable=true, corp_action_180D=false |
| 021320 | `atlas/ohlcv_tradable_by_symbol_year/021/021320/2025.csv` / 2025-02-28 o=4065, h=4075, l=3955, c=3955, v=11757 | peak=2025-07-14, trough=2025-04-07 | usable=true, corp_action_180D=false |
| 013360 | `atlas/ohlcv_tradable_by_symbol_year/013/013360/2025.csv` / 2025-02-25 o=3620, h=3730, l=3455, c=3520, v=1783917 | peak=2025-04-02, trough=2025-11-19 | usable=true, corp_action_180D=false |


Narrative-only blocked row:

| symbol | company | trigger | entry | reason | observed 180D MFE/MAE |
|---|---|---|---:|---|---:|
| 009410 | Taeyoung E&C | Stage4C | 2023-12-28 | corporate_action_candidate_2024-10-31_inside_180D_forward_window | 163.93 / -16.41 |

## 7. Case notes

### 034300 Shinsegae E&C — Stage4B, not sticky 4C

Shinsegae E&C had PF-linked loss and liquidity stress. The evidence is ugly enough to prevent Stage2/Yellow, but the parent/management support and subsequent price path make a sticky hard 4C too harsh. The correct calibration label is local Stage4B/watch until liquidity support either converts into margin/cash repair or fails.

### 002410 Bumyang Construction — hard 4C control

Bumyang is a small-builder control row: the evidence profile is operating-loss/debt stress with no visible high-quality offset before the forward path breaks. The 180D MAE of -48.51% supports retaining hard-4C protection when the non-price break is genuine.

### 035890 Seohee Construction — Stage2-Actionable positive control

Seohee shows why C30 cannot simply punish all construction names. New orders and backlog can reopen Stage2-Actionable when the balance-sheet route is not broken and forward drawdown is shallow. This is a positive-control row for backlog + order-quality bridge.

### 014790 HL D&I Halla — 4B/watch with offset quality

The case shows earnings pressure and construction-cycle risk, but later order/operating-profit evidence means hard 4C should not stick without liquidity failure or backlog collapse. This row supports “Stage4B first when offsets survive.”

### 021320 KCC E&C — Stage2-Actionable positive control

KCC E&C is a low-drawdown positive-control row. The official financial table gives operating-profit and balance-sheet visibility; forward MFE of +50.70% with MAE of only -3.92% supports Stage2-Actionable when profitability and balance-sheet bridge are direct.

### 013360 Ilsung Construction — severe 4C / high-MAE control

Ilsung has a large early spike but then a very deep 180D MAE. That pattern is useful: short-term MFE does not cancel the risk signal when the non-price evidence points to a margin/balance-sheet break.

## 8. Residual contribution

```text
sector_specific_rule_candidate = L9_CONSTRUCTION_PF_LIQUIDITY_OFFSET_QUALITY_GATE_V1
canonical_rule_candidate = C30_PF_WORKOUT_LIQUIDITY_AND_REOPEN_GATE_V1
loop_contribution_label = C30_balance_sheet_break_vs_offset_reopen_quality_repair
new_axis_proposed = no_global_axis
existing_axis_strengthened = hard_4c_confirmation, local_4b_watch_guard, stage2_required_bridge
existing_axis_weakened = none
do_not_propose_new_weight_delta = false
```

Core residual:

1. PF/workout/liquidity evidence is hard 4C only when the break is issuer-confirmed and offset quality is weak.
2. Parent liquidity support, creditor support, cost-rate normalization, order visibility, or operating-profit recovery routes first to Stage4B/watch.
3. Stage2-Actionable requires a second bridge: backlog-to-revenue, receivable collection, debt/net-cash improvement, operating-profit conversion, cashflow visibility, or high-quality order mix.
4. A positive forward path after an ugly headline is a warning against sticky hard 4C, not a reason to loosen Green.
5. Stage3-Green remains blocked until cashflow / working-capital / debt repair repeats across more than one evidence family.

## 9. Shadow profile suggestion

```yaml
shadow_rule_candidate:
  id: C30_PF_WORKOUT_LIQUIDITY_AND_REOPEN_GATE_V1
  scope:
    large_sector_id: L9_CONSTRUCTION_REALESTATE_HOUSING
    canonical_archetype_id: C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK
  production_scoring_changed: false
  shadow_weight_only: true
  rule:
    hard_4c_requires:
      - confirmed_liquidity_break_or_workout_or_audit_trust_break
      - weak_offset_quality
    stage4b_first_when_any:
      - parent_or_creditor_liquidity_support
      - cost_rate_normalization
      - order_backlog_survives
      - operating_profit_recovery
      - net_cash_or_debt_repair
    stage2_actionable_requires_any:
      - backlog_to_revenue_conversion
      - operating_profit_conversion
      - working_capital_release
      - receivable_collection_improvement
      - debt_or_net_cash_improvement
      - cashflow_visibility
    green_blocker:
      - missing_repeated_cashflow_working_capital_bridge
      - high_MAE_after_single_bridge
```

## 10. Machine-readable JSONL trigger rows

```jsonl
{"row_type": "trigger", "research_version": "v12", "selected_round": "R10", "selected_loop": 221, "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "fine_archetype_id": "C30_PF_WORKOUT_LIQUIDITY_AND_REOPEN_GATE_V1", "symbol": "034300", "company_name": "Shinsegae E&C", "case_role": "liquidity_support_watch", "trigger_type": "Stage4B", "evidence_date": "2024-03-21", "entry_date": "2024-03-21", "entry_price": 10890.0, "entry_ohlcv": {"o": 10900.0, "h": 11190.0, "l": 10830.0, "c": 10890.0, "v": 2875, "a": 31508350.0, "mc": 84512433060.0, "m": "KOSPI"}, "mfe_mae": {"30": {"mfe_pct": 6.15, "mae_pct": -9.55, "peak_date": "2024-03-27", "trough_date": "2024-04-26", "window_end": "2024-05-07"}, "90": {"mfe_pct": 71.26, "mae_pct": -9.55, "peak_date": "2024-05-30", "trough_date": "2024-04-26", "window_end": "2024-08-01"}, "180": {"mfe_pct": 71.26, "mae_pct": -9.55, "peak_date": "2024-05-30", "trough_date": "2024-04-26", "window_end": "2024-12-16"}}, "price_source_validation": {"source": "Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_usable": true, "corporate_action_contaminated_180d": false, "insufficient_forward_window_180d": false}, "raw_component_score_breakdown": {"eps_fcf_explosion": 6, "earnings_visibility": 10, "bottleneck_pricing": 3, "market_mispricing": 8, "valuation_rerating": 6, "capital_allocation": 6, "information_confidence": 22}, "score_total_proxy": 61, "current_profile_error_label": "too_strict_hard_4c", "production_scoring_changed": false, "shadow_weight_only": true}
{"row_type": "trigger", "research_version": "v12", "selected_round": "R10", "selected_loop": 221, "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "fine_archetype_id": "C30_PF_WORKOUT_LIQUIDITY_AND_REOPEN_GATE_V1", "symbol": "002410", "company_name": "Bumyang Construction", "case_role": "small_builder_loss_debt_break", "trigger_type": "Stage4C", "evidence_date": "2023-12-21", "entry_date": "2023-12-21", "entry_price": 2185.0, "entry_ohlcv": {"o": 2175.0, "h": 2230.0, "l": 2135.0, "c": 2185.0, "v": 180833, "a": 394571895.0, "mc": 54257880670.0, "m": "KOSPI"}, "mfe_mae": {"30": {"mfe_pct": 7.32, "mae_pct": -22.47, "peak_date": "2024-01-02", "trough_date": "2024-02-06", "window_end": "2024-02-06"}, "90": {"mfe_pct": 7.32, "mae_pct": -38.22, "peak_date": "2024-01-02", "trough_date": "2024-04-16", "window_end": "2024-05-08"}, "180": {"mfe_pct": 7.32, "mae_pct": -48.51, "peak_date": "2024-01-02", "trough_date": "2024-09-09", "window_end": "2024-09-19"}}, "price_source_validation": {"source": "Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_usable": true, "corporate_action_contaminated_180d": false, "insufficient_forward_window_180d": false}, "raw_component_score_breakdown": {"eps_fcf_explosion": 2, "earnings_visibility": 4, "bottleneck_pricing": 1, "market_mispricing": 5, "valuation_rerating": 3, "capital_allocation": 3, "information_confidence": 30}, "score_total_proxy": 48, "current_profile_error_label": "hard_4c_control_or_stage2_cap", "production_scoring_changed": false, "shadow_weight_only": true}
{"row_type": "trigger", "research_version": "v12", "selected_round": "R10", "selected_loop": 221, "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "fine_archetype_id": "C30_PF_WORKOUT_LIQUIDITY_AND_REOPEN_GATE_V1", "symbol": "035890", "company_name": "Seohee Construction", "case_role": "backlog_order_positive_control", "trigger_type": "Stage2-Actionable", "evidence_date": "2024-08-14", "entry_date": "2024-08-14", "entry_price": 1342.0, "entry_ohlcv": {"o": 1308.0, "h": 1352.0, "l": 1308.0, "c": 1342.0, "v": 408782, "a": 542229896.0, "mc": 308402949294.0, "m": "KOSDAQ"}, "mfe_mae": {"30": {"mfe_pct": 17.29, "mae_pct": -2.53, "peak_date": "2024-10-02", "trough_date": "2024-08-14", "window_end": "2024-10-02"}, "90": {"mfe_pct": 25.19, "mae_pct": -2.53, "peak_date": "2024-12-18", "trough_date": "2024-08-14", "window_end": "2024-12-30"}, "180": {"mfe_pct": 33.46, "mae_pct": -2.53, "peak_date": "2025-04-22", "trough_date": "2024-08-14", "window_end": "2025-05-19"}}, "price_source_validation": {"source": "Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_usable": true, "corporate_action_contaminated_180d": false, "insufficient_forward_window_180d": false}, "raw_component_score_breakdown": {"eps_fcf_explosion": 14, "earnings_visibility": 18, "bottleneck_pricing": 5, "market_mispricing": 12, "valuation_rerating": 11, "capital_allocation": 9, "information_confidence": 16}, "score_total_proxy": 85, "current_profile_error_label": "green_blocker_ok", "production_scoring_changed": false, "shadow_weight_only": true}
{"row_type": "trigger", "research_version": "v12", "selected_round": "R10", "selected_loop": 221, "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "fine_archetype_id": "C30_PF_WORKOUT_LIQUIDITY_AND_REOPEN_GATE_V1", "symbol": "014790", "company_name": "HL D&I Halla", "case_role": "profit_decline_with_order_offset_watch", "trigger_type": "Stage4B", "evidence_date": "2025-02-06", "entry_date": "2025-02-06", "entry_price": 2280.0, "entry_ohlcv": {"o": 2230.0, "h": 2280.0, "l": 2070.0, "c": 2280.0, "v": 50488, "a": 110590965.0, "mc": 86317610280.0, "m": "KOSPI"}, "mfe_mae": {"30": {"mfe_pct": 9.21, "mae_pct": -9.21, "peak_date": "2025-02-25", "trough_date": "2025-02-06", "window_end": "2025-03-21"}, "90": {"mfe_pct": 24.56, "mae_pct": -9.21, "peak_date": "2025-06-20", "trough_date": "2025-02-06", "window_end": "2025-06-20"}, "180": {"mfe_pct": 35.75, "mae_pct": -9.21, "peak_date": "2025-08-08", "trough_date": "2025-02-06", "window_end": "2025-11-03"}}, "price_source_validation": {"source": "Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_usable": true, "corporate_action_contaminated_180d": false, "insufficient_forward_window_180d": false}, "raw_component_score_breakdown": {"eps_fcf_explosion": 6, "earnings_visibility": 10, "bottleneck_pricing": 3, "market_mispricing": 8, "valuation_rerating": 6, "capital_allocation": 6, "information_confidence": 22}, "score_total_proxy": 61, "current_profile_error_label": "too_strict_hard_4c", "production_scoring_changed": false, "shadow_weight_only": true}
{"row_type": "trigger", "research_version": "v12", "selected_round": "R10", "selected_loop": 221, "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "fine_archetype_id": "C30_PF_WORKOUT_LIQUIDITY_AND_REOPEN_GATE_V1", "symbol": "021320", "company_name": "KCC E&C", "case_role": "profit_balance_sheet_positive_control", "trigger_type": "Stage2-Actionable", "evidence_date": "2025-02-28", "entry_date": "2025-02-28", "entry_price": 3955.0, "entry_ohlcv": {"o": 4065.0, "h": 4075.0, "l": 3955.0, "c": 3955.0, "v": 11757, "a": 47226780.0, "mc": 84637000000.0, "m": "KOSDAQ"}, "mfe_mae": {"30": {"mfe_pct": 8.34, "mae_pct": -3.92, "peak_date": "2025-04-14", "trough_date": "2025-04-07", "window_end": "2025-04-14"}, "90": {"mfe_pct": 50.7, "mae_pct": -3.92, "peak_date": "2025-07-14", "trough_date": "2025-04-07", "window_end": "2025-07-14"}, "180": {"mfe_pct": 50.7, "mae_pct": -3.92, "peak_date": "2025-07-14", "trough_date": "2025-04-07", "window_end": "2025-11-25"}}, "price_source_validation": {"source": "Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_usable": true, "corporate_action_contaminated_180d": false, "insufficient_forward_window_180d": false}, "raw_component_score_breakdown": {"eps_fcf_explosion": 14, "earnings_visibility": 18, "bottleneck_pricing": 5, "market_mispricing": 12, "valuation_rerating": 11, "capital_allocation": 9, "information_confidence": 16}, "score_total_proxy": 85, "current_profile_error_label": "green_blocker_ok", "production_scoring_changed": false, "shadow_weight_only": true}
{"row_type": "trigger", "research_version": "v12", "selected_round": "R10", "selected_loop": 221, "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "fine_archetype_id": "C30_PF_WORKOUT_LIQUIDITY_AND_REOPEN_GATE_V1", "symbol": "013360", "company_name": "Ilsung Construction", "case_role": "operating_loss_margin_break", "trigger_type": "Stage4C", "evidence_date": "2025-02-25", "entry_date": "2025-02-25", "entry_price": 3520.0, "entry_ohlcv": {"o": 3620.0, "h": 3730.0, "l": 3455.0, "c": 3520.0, "v": 1783917, "a": 6407407865.0, "mc": 190167577600.0, "m": "KOSPI"}, "mfe_mae": {"30": {"mfe_pct": 41.05, "mae_pct": -23.01, "peak_date": "2025-04-02", "trough_date": "2025-04-04", "window_end": "2025-04-09"}, "90": {"mfe_pct": 41.05, "mae_pct": -52.27, "peak_date": "2025-04-02", "trough_date": "2025-07-08", "window_end": "2025-07-09"}, "180": {"mfe_pct": 41.05, "mae_pct": -66.14, "peak_date": "2025-04-02", "trough_date": "2025-11-19", "window_end": "2025-11-20"}}, "price_source_validation": {"source": "Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_usable": true, "corporate_action_contaminated_180d": false, "insufficient_forward_window_180d": false}, "raw_component_score_breakdown": {"eps_fcf_explosion": 2, "earnings_visibility": 4, "bottleneck_pricing": 1, "market_mispricing": 5, "valuation_rerating": 3, "capital_allocation": 3, "information_confidence": 30}, "score_total_proxy": 48, "current_profile_error_label": "hard_4c_control_or_stage2_cap", "production_scoring_changed": false, "shadow_weight_only": true}
```

## 11. Narrative-only row

```json
{
  "row_type": "narrative_only",
  "research_version": "v12",
  "selected_round": "R10",
  "selected_loop": 221,
  "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING",
  "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK",
  "fine_archetype_id": "C30_PF_WORKOUT_LIQUIDITY_AND_REOPEN_GATE_V1",
  "symbol": "009410",
  "company_name": "Taeyoung E&C",
  "trigger_type": "Stage4C",
  "evidence_date": "2023-12-28",
  "entry_date": "2023-12-28",
  "entry_price": 2315.0,
  "blocked_reason": "corporate_action_candidate_2024-10-31_inside_180D_forward_window",
  "mfe_180d_pct": 163.93,
  "mae_180d_pct": -16.41,
  "calibration_usable": false,
  "production_scoring_changed": false,
  "shadow_weight_only": true
}
```

## 12. Batch ingest self-audit

```text
standard_v12_filename = pass
filename_round = R10
metadata_round = R10
filename_loop = 221
metadata_loop = 221
large_sector_id_allowed = pass
round_sector_consistency = pass
canonical_archetype_known = pass
all_usable_rows_have_entry_date = true
all_usable_rows_have_entry_price = true
all_usable_rows_have_actual_ohlcv = true
all_usable_rows_have_30_90_180_mfe_mae = true
valid_rows_missing_required_mfe_mae = 0
corporate_action_contaminated_usable_rows = 0
insufficient_forward_window_usable_rows = 0
source_proxy_only_count = 0
evidence_url_pending_count = 0
production_scoring_changed = false
shadow_weight_only = true
ready_for_batch_ingest = true
```

## 13. Deferred Coding Agent Handoff Prompt

```text
Do not execute during this research session.

When multiple v12 residual MDs are gathered, parse this file as a standard v12 result MD.
Use the JSONL trigger rows above as candidate input for validation/dedupe/aggregate.
Do not apply production scoring directly from this single file.
Evaluate C30_PF_WORKOUT_LIQUIDITY_AND_REOPEN_GATE_V1 only as a scoped shadow rule candidate.
Block narrative_only rows from promotion if calibration_usable=false.
```

## 14. Next Research State

```text
completed_round = R10
completed_loop = 221
selection_basis = docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket = Priority 2 quality repair / C30 direct evidence refresh
round_schedule_status = coverage_index_selected
round_sector_consistency = pass
next_recommended_archetypes =
  - C05_EPC_MEGA_CONTRACT_MARGIN_GAP_WORKING_CAPITAL_CASHFLOW_ONLY_REPAIR
  - C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE_SUPPLIER_ORDER_DIRECT_URL_REPAIR
  - C13_BATTERY_JV_UTILIZATION_AMPC_IRA_EX_SUBSIDY_MARGIN_DIRECT_REPAIR
  - C16_STRATEGIC_RESOURCE_POLICY_SUPPLY_DIRECT_OFFTAKE_POSITIVE_CONTROL_REPAIR
  - R13_CROSS_ARCHETYPE_4B_4C_REDTEAM_OFFSET_QUALITY_REFRESH
```

## 15. Source URLs

```text
main_prompt = https://raw.githubusercontent.com/Songdaiki/stock_agent/main/docs/core/e2r_v12_prompt_round_scheduler_corrected.txt
no_repeat_index = https://raw.githubusercontent.com/Songdaiki/stock_agent/main/docs/core/V12_Research_No_Repeat_Index.md
stock_web_manifest = https://raw.githubusercontent.com/Songdaiki/stock-web/main/atlas/manifest.json
stock_web_schema = https://raw.githubusercontent.com/Songdaiki/stock-web/main/atlas/schema.json
taeyoung_reuters_workout = https://www.reuters.com/markets/asia/south-korea-moves-reassure-markets-builder-seeks-restructure-debt-2023-12-28/
taeyoung_fsc = https://www.fsc.go.kr/eng/pr010101/81369
shinsegae_asiae = https://www.asiae.co.kr/en/article/2024040315003608412
shinsegae_ked = https://www.kedglobal.com/executive-reshuffles/newsView/ked202404020012
bumyang_english_dart = https://englishdart.fss.or.kr/dsbh002/main.do?rcpNo=20250605000491
seohee_asiae = https://www.asiae.co.kr/en/print.htm?idxno=2025032522383515141
kcc_enc_financial = https://www.kccworld.net/eng/investment/balance.do
hl_dni_financial = https://www.hldni.com/eng/html/invest/finance.asp
ilsung_english_dart = https://englishdart.fss.or.kr/dsbh001/main.do?rcpNo=20250225801008
```
