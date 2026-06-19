# E2R Stock-Web v12 Residual Research — R1 / L1_INDUSTRIALS_INFRA_DEFENSE_GRID / C05_EPC_MEGA_CONTRACT_MARGIN_GAP

```text
research_file = e2r_stock_web_v12_residual_round_R1_loop_200_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C05_EPC_MEGA_CONTRACT_MARGIN_GAP_research.md
selected_round = R1
selected_loop = 200
selection_basis = docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket = Priority 1 balance / quality reinforcement
large_sector_id = L1_INDUSTRIALS_INFRA_DEFENSE_GRID
canonical_archetype_id = C05_EPC_MEGA_CONTRACT_MARGIN_GAP
fine_archetype_id = EPC_COST_RATE_BACKLOG_TO_CASHFLOW_OFFSET_REPAIR
round_schedule_status = coverage_index_selected
round_sector_consistency = pass
production_scoring_changed = false
shadow_weight_only = true
```

## 1. Execution Mode Compliance

- This is a historical trigger-level residual calibration MD, not a live scan and not a stock_agent code patch.
- Price basis is Songdaiki/stock-web `tradable_raw` / `raw_unadjusted_marcap`.
- The selected archetype is driven by the No-Repeat Index quality-repair priority, not by strict R1~R13 sequencing.
- Hard duplicate key used for this run: `canonical_archetype_id + symbol + trigger_type + entry_date`.
- All usable trigger rows include actual 1D OHLCV, 30/90/180D MFE/MAE, profile/corporate-action notes, score simulation, and residual labels.

## 2. Coverage-Index Selection Rationale

The No-Repeat Index shows all C01~C32 archetypes above the old 80-row threshold, so this run does not add raw coverage for its own sake. Priority 1 still calls out C05 for margin / working-capital failure and 4C timing repair. This batch therefore uses C05 again, but with a new fine axis: cost-rate and cash-flow offset handling after backlog/order/sales headlines.

| check | result |
|---|---|
| strict sequential R1~R13 required | false |
| selected archetype drives round | true |
| selected_round | R1 |
| selected large sector | L1_INDUSTRIALS_INFRA_DEFENSE_GRID |
| selected canonical | C05_EPC_MEGA_CONTRACT_MARGIN_GAP |
| prior local duplicate keys checked | pass |
| exact duplicate collisions in this batch | 0 |

### New hard duplicate keys

- `C05_EPC_MEGA_CONTRACT_MARGIN_GAP|000720|Stage2|2024-04-19`
- `C05_EPC_MEGA_CONTRACT_MARGIN_GAP|000720|Stage4B|2024-07-19`
- `C05_EPC_MEGA_CONTRACT_MARGIN_GAP|028050|Stage2-Actionable|2024-07-25`
- `C05_EPC_MEGA_CONTRACT_MARGIN_GAP|028050|Stage2-Actionable|2025-01-23`
- `C05_EPC_MEGA_CONTRACT_MARGIN_GAP|006360|Stage2|2025-02-05`
- `C05_EPC_MEGA_CONTRACT_MARGIN_GAP|047040|Stage4B|2025-02-06`
- `C05_EPC_MEGA_CONTRACT_MARGIN_GAP|375500|Stage4B|2024-05-02`
- `C05_EPC_MEGA_CONTRACT_MARGIN_GAP|375500|Stage4B|2024-08-01`

## 3. Stock-Web Manifest / Schema Validation

```text
source_name = FinanceData/marcap
source_repo_url = https://github.com/FinanceData/marcap
price_adjustment_status = raw_unadjusted_marcap
manifest_max_date = 2026-02-20
tradable_row_count = 14,354,401
raw_row_count = 15,214,118
symbol_count = 5,414
calibration_shard_root = atlas/ohlcv_tradable_by_symbol_year
raw_shard_root = atlas/ohlcv_raw_by_symbol_year
tradable columns = d,o,h,l,c,v,a,mc,s,m
mfe_mae_formula = entry close 대비 window max high / min low
window convention = entry row through D+N tradable rows, inclusive
```

## 4. Trigger-Level Backtest Summary

| # | symbol | company | trigger | entry | entry close | MFE30/MAE30 | MFE90/MAE90 | MFE180/MAE180 | case role |
|---:|---|---|---|---|---:|---:|---:|---:|---|
| 1 | 000720 | Hyundai E&C | Stage2 | 2024-04-19 | 33,250 | 8.27/-4.96 | 8.27/-12.63 | 8.27/-27.52 | stage2_false_positive_counterexample |
| 2 | 000720 | Hyundai E&C | Stage4B | 2024-07-19 | 32,600 | 4.75/-10.89 | 4.75/-16.87 | 22.24/-26.07 | local_4b_cost_rate_guardrail |
| 3 | 028050 | Samsung E&A | Stage2-Actionable | 2024-07-25 | 25,700 | 14.01/-8.75 | 14.01/-36.58 | 14.01/-36.58 | high_mae_positive_guardrail |
| 4 | 028050 | Samsung E&A | Stage2-Actionable | 2025-01-23 | 17,440 | 12.67/-6.08 | 36.18/-6.08 | 75.75/-6.08 | positive_control |
| 5 | 006360 | GS E&C | Stage2 | 2025-02-05 | 17,300 | 14.45/-0.29 | 43.64/-12.20 | 43.64/-12.20 | turnaround_positive_but_trust_discount |
| 6 | 047040 | Daewoo E&C | Stage4B | 2025-02-06 | 3,360 | 11.90/-4.76 | 43.01/-12.50 | 43.01/-12.50 | overhard_4c_counterexample |
| 7 | 375500 | DL E&C | Stage4B | 2024-05-02 | 36,700 | 7.63/-10.22 | 7.63/-22.07 | 7.63/-22.07 | correct_4b_negative_control |
| 8 | 375500 | DL E&C | Stage4B | 2024-08-01 | 34,650 | 3.32/-17.46 | 3.32/-17.46 | 35.50/-17.46 | offset_quality_counterexample |

## 5. Case Notes

### 1. Hyundai E&C (000720) — Stage2 — 2024-04-19

```text
duplicate_key = C05_EPC_MEGA_CONTRACT_MARGIN_GAP|000720|Stage2|2024-04-19
actual_1d_ohlcv = o:32000.0, h:33450.0, l:31600.0, c:33250.0, v:727477
MFE_30D / MAE_30D = 8.27 / -4.96
MFE_90D / MAE_90D = 8.27 / -12.63
MFE_180D / MAE_180D = 8.27 / -27.52
peak_180D = 2024-05-09 @ 36000.0
drawdown_after_peak_180D = -33.06% to 2024-12-09
```
Evidence: Yonhap reported that Hyundai E&C Q1 2024 operating profit surged 44.6% YoY to KRW250.9B and revenue rose 41.7% to KRW8.55T on strong housing and overseas business. The same 2024 cycle later showed Q4 one-off/cost pressure, so the Q1 headline is a Stage2 signal but not Actionable/Yellow without cost-rate and cash-flow durability. Source: `https://en.yna.co.kr/view/AEN20240419005652320`

Residual read: q1_growth_headline_needs_cost_rate_and_fcf_follow_through. Current profile stress label: `false_positive_if_q1_growth_is_treated_as_durable_margin_bridge`.

### 2. Hyundai E&C (000720) — Stage4B — 2024-07-19

```text
duplicate_key = C05_EPC_MEGA_CONTRACT_MARGIN_GAP|000720|Stage4B|2024-07-19
actual_1d_ohlcv = o:33100.0, h:33100.0, l:32450.0, c:32600.0, v:775289
MFE_30D / MAE_30D = 4.75 / -10.89
MFE_90D / MAE_90D = 4.75 / -16.87
MFE_180D / MAE_180D = 22.24 / -26.07
peak_180D = 2025-04-18 @ 39850.0
drawdown_after_peak_180D = -3.01% to 2025-04-18
```
Evidence: Yonhap reported Q2 2024 net profit down 31.2% and operating profit down 34.1% YoY, while sales rose 20.4%; the explicit reason was a rise in raw material costs. This is not a new positive bridge; it is a C05 cost-rate watch despite later rebound. Source: `https://en.yna.co.kr/view/AEN20240719004551320`

Residual read: revenue_growth_with_raw_material_cost_pressure_routes_to_4b_watch. Current profile stress label: `revenue_growth_overstates_quality_when_cost_rate_break_is_explicit`.

### 3. Samsung E&A (028050) — Stage2-Actionable — 2024-07-25

```text
duplicate_key = C05_EPC_MEGA_CONTRACT_MARGIN_GAP|028050|Stage2-Actionable|2024-07-25
actual_1d_ohlcv = o:24700.0, h:26200.0, l:24400.0, c:25700.0, v:1753958
MFE_30D / MAE_30D = 14.01 / -8.75
MFE_90D / MAE_90D = 14.01 / -36.58
MFE_180D / MAE_180D = 14.01 / -36.58
peak_180D = 2024-07-30 @ 29300.0
drawdown_after_peak_180D = -44.37% to 2024-12-09
```
Evidence: Samsung E&A said H1 2024 revenue reached KRW5.71T, operating profit KRW471.9B and net profit KRW369.4B, citing settlement and cost improvements in late-stage hydrocarbon projects and a stable profit structure. The forward path had deep MAE, so it is Actionable but not Green. Source: `https://samsungena.com/en/newsroom/news/view?idx=15609`

Residual read: cost_improvement_positive_still_needs_entry_quality_and_fcf_check. Current profile stress label: `too_early_yellow_if_cost_improvement_not_checked_against_peak_proximity`.

### 4. Samsung E&A (028050) — Stage2-Actionable — 2025-01-23

```text
duplicate_key = C05_EPC_MEGA_CONTRACT_MARGIN_GAP|028050|Stage2-Actionable|2025-01-23
actual_1d_ohlcv = o:18500.0, h:18580.0, l:17400.0, c:17440.0, v:1839171
MFE_30D / MAE_30D = 12.67 / -6.08
MFE_90D / MAE_90D = 36.18 / -6.08
MFE_180D / MAE_180D = 75.75 / -6.08
peak_180D = 2025-10-23 @ 30650.0
drawdown_after_peak_180D = -8.65% to 2025-10-23
```
Evidence: Samsung E&A reported Q4 2024 operating profit of KRW295.8B, up 9.6% YoY, and attributed performance to project profitability, settlement effects and cost improvements while setting 2025 guidance. This is a cleaner positive control after the July high-MAE case. Source: `https://www.samsungena.com/en/newsroom/news/view?idx=15673`

Residual read: confirmed_cost_improvement_and_order_guidance_can_repair_late_stage2. Current profile stress label: `too_late_if_direct_margin_order_bridge_is_underweighted`.

### 5. GS E&C (006360) — Stage2 — 2025-02-05

```text
duplicate_key = C05_EPC_MEGA_CONTRACT_MARGIN_GAP|006360|Stage2|2025-02-05
actual_1d_ohlcv = o:17300.0, h:17760.0, l:17260.0, c:17300.0, v:338689
MFE_30D / MAE_30D = 14.45 / -0.29
MFE_90D / MAE_90D = 43.64 / -12.2
MFE_180D / MAE_180D = 43.64 / -12.2
peak_180D = 2025-06-12 @ 24850.0
drawdown_after_peak_180D = -28.41% to 2025-09-03
```
Evidence: Yonhap reported GS E&C 2024 net profit of KRW264.9B, swinging from a KRW419.5B loss. The price path validates that turnaround language mattered, but the prior quality/regulatory overhang means this should repair Stage2, not jump straight to Yellow/Green. Source: `https://en.yna.co.kr/view/AEN20250205002400320`

Residual read: profit_turnaround_repairs_stage2_but_quality_overhang_blocks_green. Current profile stress label: `mild_too_late_if_turnaround_ignored_but_green_blocker_stays`.

### 6. Daewoo E&C (047040) — Stage4B — 2025-02-06

```text
duplicate_key = C05_EPC_MEGA_CONTRACT_MARGIN_GAP|047040|Stage4B|2025-02-06
actual_1d_ohlcv = o:3290.0, h:3420.0, l:3285.0, c:3360.0, v:1843821
MFE_30D / MAE_30D = 11.9 / -4.76
MFE_90D / MAE_90D = 43.01 / -12.5
MFE_180D / MAE_180D = 43.01 / -12.5
peak_180D = 2025-06-05 @ 4805.0
drawdown_after_peak_180D = -26.33% to 2025-08-20
```
Evidence: Yonhap reported Daewoo E&C 2024 net income down 53.4%, operating profit down 39.2% and revenue down 9.8%. The stock-web path rebounded strongly, so this is a 4B earnings-quality watch unless order backlog, liquidity or project-cost thesis breaks are confirmed. Source: `https://en.yna.co.kr/view/AEN20250206001600320`

Residual read: annual_op_decline_is_4b_unless_project_or_balance_sheet_break_confirms_4c. Current profile stress label: `false_positive_hard_4c_when_earnings_decline_lacks_order_liquidity_break`.

### 7. DL E&C (375500) — Stage4B — 2024-05-02

```text
duplicate_key = C05_EPC_MEGA_CONTRACT_MARGIN_GAP|375500|Stage4B|2024-05-02
actual_1d_ohlcv = o:36800.0, h:37500.0, l:36350.0, c:36700.0, v:76767
MFE_30D / MAE_30D = 7.63 / -10.22
MFE_90D / MAE_90D = 7.63 / -22.07
MFE_180D / MAE_180D = 7.63 / -22.07
peak_180D = 2024-06-13 @ 39500.0
drawdown_after_peak_180D = -27.59% to 2024-08-05
```
Evidence: Yonhap reported DL E&C Q1 2024 net income down 72.3% YoY. The forward price path had shallow MFE and -22% 180D MAE, validating a local 4B/caution route rather than treating weak earnings as harmless noise. Source: `https://en.yna.co.kr/view/AEN20240502003000320`

Residual read: weak_net_income_and_cost_visibility_should_keep_c05_in_4b_watch. Current profile stress label: `false_positive_if_backlog_language_offsets_earnings_quality_too_much`.

### 8. DL E&C (375500) — Stage4B — 2024-08-01

```text
duplicate_key = C05_EPC_MEGA_CONTRACT_MARGIN_GAP|375500|Stage4B|2024-08-01
actual_1d_ohlcv = o:34900.0, h:35800.0, l:34350.0, c:34650.0, v:202635
MFE_30D / MAE_30D = 3.32 / -17.46
MFE_90D / MAE_90D = 3.32 / -17.46
MFE_180D / MAE_180D = 35.5 / -17.46
peak_180D = 2025-03-10 @ 46950.0
drawdown_after_peak_180D = -20.87% to 2025-04-09
```
Evidence: Asiae reported DL E&C Q2 2024 operating profit down 54.7%, but the article also framed an expected second-half operating profit rebound due to cost-ratio improvement. Later 180D MFE was positive, so hard 4C should be deferred when offset quality is explicit. Source: `https://www.asiae.co.kr/en/article/2024080114294271959`

Residual read: explicit_cost_rate_rebound_guidance_keeps_negative_earnings_case_in_4b_not_4c. Current profile stress label: `overhard_4c_if_cost_rate_rebound_guidance_is_ignored`.

## 6. Raw Component Score Simulation

Weights used for C05 shadow stress: `EPS/Vis/Bott/Mis/Val/Cap/Info = 18/22/10/12/10/8/20`. These are not production changes; they are traceable stress rows for later batch calibration.

### C05_200_01_HYUNDAI_EC_Q1_2024_HEADLINE_WITH_LATER_COST_BREAK

```json
{
  "before_stage": "Stage2-Actionable if headline-only bonus is overused",
  "before_total_score_label": 76.0,
  "before_weighted_calc": 68.42,
  "raw_component_scores_before": {
    "eps_fcf_explosion": 78,
    "earnings_visibility": 76,
    "bottleneck_pricing": 45,
    "market_mispricing": 58,
    "valuation_rerating": 54,
    "capital_allocation": 55,
    "information_confidence": 82
  },
  "after_stage": "Stage2 capped / Green blocker",
  "after_total_score_label": 62.0,
  "after_weighted_calc": 54.8,
  "raw_component_scores_after": {
    "eps_fcf_explosion": 55,
    "earnings_visibility": 58,
    "bottleneck_pricing": 35,
    "market_mispricing": 45,
    "valuation_rerating": 38,
    "capital_allocation": 48,
    "information_confidence": 78
  },
  "production_scoring_changed": false,
  "shadow_weight_only": true
}
```

### C05_200_02_HYUNDAI_EC_Q2_2024_RAW_MATERIAL_COST_4B

```json
{
  "before_stage": "Stage2 if revenue growth is overweighted",
  "before_total_score_label": 67.0,
  "before_weighted_calc": 60.8,
  "raw_component_scores_before": {
    "eps_fcf_explosion": 62,
    "earnings_visibility": 64,
    "bottleneck_pricing": 42,
    "market_mispricing": 55,
    "valuation_rerating": 50,
    "capital_allocation": 52,
    "information_confidence": 78
  },
  "after_stage": "Stage4B local watch, not hard 4C",
  "after_total_score_label": 54.0,
  "after_weighted_calc": 48.2,
  "raw_component_scores_after": {
    "eps_fcf_explosion": 38,
    "earnings_visibility": 42,
    "bottleneck_pricing": 28,
    "market_mispricing": 48,
    "valuation_rerating": 38,
    "capital_allocation": 42,
    "information_confidence": 82
  },
  "production_scoring_changed": false,
  "shadow_weight_only": true
}
```

### C05_200_03_SAMSUNG_ENA_H1_2024_COST_IMPROVEMENT_HIGH_MAE

```json
{
  "before_stage": "Stage3-Yellow if cost-improvement language is overtrusted",
  "before_total_score_label": 79.0,
  "before_weighted_calc": 71.66,
  "raw_component_scores_before": {
    "eps_fcf_explosion": 76,
    "earnings_visibility": 78,
    "bottleneck_pricing": 55,
    "market_mispricing": 62,
    "valuation_rerating": 58,
    "capital_allocation": 56,
    "information_confidence": 88
  },
  "after_stage": "Stage2-Actionable with Green blocker",
  "after_total_score_label": 70.0,
  "after_weighted_calc": 64.16,
  "raw_component_scores_after": {
    "eps_fcf_explosion": 68,
    "earnings_visibility": 72,
    "bottleneck_pricing": 48,
    "market_mispricing": 43,
    "valuation_rerating": 42,
    "capital_allocation": 54,
    "information_confidence": 88
  },
  "production_scoring_changed": false,
  "shadow_weight_only": true
}
```

### C05_200_04_SAMSUNG_ENA_Q4_2024_ORDER_AND_MARGIN_POSITIVE_CONTROL

```json
{
  "before_stage": "Stage2-Actionable",
  "before_total_score_label": 74.0,
  "before_weighted_calc": 67.08,
  "raw_component_scores_before": {
    "eps_fcf_explosion": 70,
    "earnings_visibility": 72,
    "bottleneck_pricing": 52,
    "market_mispricing": 55,
    "valuation_rerating": 50,
    "capital_allocation": 58,
    "information_confidence": 86
  },
  "after_stage": "Stage3-Yellow, not Green",
  "after_total_score_label": 81.0,
  "after_weighted_calc": 75.2,
  "raw_component_scores_after": {
    "eps_fcf_explosion": 82,
    "earnings_visibility": 84,
    "bottleneck_pricing": 58,
    "market_mispricing": 62,
    "valuation_rerating": 56,
    "capital_allocation": 64,
    "information_confidence": 90
  },
  "production_scoring_changed": false,
  "shadow_weight_only": true
}
```

### C05_200_05_GS_EC_2024_PROFIT_TURNAROUND_WITH_TRUST_OVERHANG

```json
{
  "before_stage": "Stage2",
  "before_total_score_label": 68.0,
  "before_weighted_calc": 59.58,
  "raw_component_scores_before": {
    "eps_fcf_explosion": 66,
    "earnings_visibility": 62,
    "bottleneck_pricing": 35,
    "market_mispricing": 58,
    "valuation_rerating": 48,
    "capital_allocation": 55,
    "information_confidence": 72
  },
  "after_stage": "Stage2-Actionable capped below Yellow",
  "after_total_score_label": 72.0,
  "after_weighted_calc": 64.64,
  "raw_component_scores_after": {
    "eps_fcf_explosion": 72,
    "earnings_visibility": 70,
    "bottleneck_pricing": 38,
    "market_mispricing": 62,
    "valuation_rerating": 52,
    "capital_allocation": 58,
    "information_confidence": 76
  },
  "production_scoring_changed": false,
  "shadow_weight_only": true
}
```

### C05_200_06_DAEWOO_EC_2024_OP_DOWN_OVERHARD_4C_OFFSET

```json
{
  "before_stage": "Stage4C if earnings decline is treated as thesis break",
  "before_total_score_label": 46.0,
  "before_weighted_calc": 37.22,
  "raw_component_scores_before": {
    "eps_fcf_explosion": 25,
    "earnings_visibility": 28,
    "bottleneck_pricing": 18,
    "market_mispricing": 35,
    "valuation_rerating": 28,
    "capital_allocation": 32,
    "information_confidence": 76
  },
  "after_stage": "Stage4B local watch",
  "after_total_score_label": 58.0,
  "after_weighted_calc": 45.0,
  "raw_component_scores_after": {
    "eps_fcf_explosion": 34,
    "earnings_visibility": 38,
    "bottleneck_pricing": 22,
    "market_mispricing": 48,
    "valuation_rerating": 36,
    "capital_allocation": 42,
    "information_confidence": 78
  },
  "production_scoring_changed": false,
  "shadow_weight_only": true
}
```

### C05_200_07_DLENC_Q1_2024_NET_INCOME_DROP_CORRECT_4B

```json
{
  "before_stage": "Stage2 if backlog/order language offsets too much",
  "before_total_score_label": 57.0,
  "before_weighted_calc": 47.84,
  "raw_component_scores_before": {
    "eps_fcf_explosion": 44,
    "earnings_visibility": 42,
    "bottleneck_pricing": 24,
    "market_mispricing": 50,
    "valuation_rerating": 38,
    "capital_allocation": 46,
    "information_confidence": 74
  },
  "after_stage": "Stage4B confirmed",
  "after_total_score_label": 48.0,
  "after_weighted_calc": 40.72,
  "raw_component_scores_after": {
    "eps_fcf_explosion": 30,
    "earnings_visibility": 32,
    "bottleneck_pricing": 18,
    "market_mispricing": 42,
    "valuation_rerating": 32,
    "capital_allocation": 38,
    "information_confidence": 76
  },
  "production_scoring_changed": false,
  "shadow_weight_only": true
}
```

### C05_200_08_DLENC_Q2_2024_COST_IMPROVEMENT_OFFSET_4B_NOT_4C

```json
{
  "before_stage": "Stage4C if operating-profit drop is overhardened",
  "before_total_score_label": 51.0,
  "before_weighted_calc": 40.12,
  "raw_component_scores_before": {
    "eps_fcf_explosion": 30,
    "earnings_visibility": 32,
    "bottleneck_pricing": 18,
    "market_mispricing": 42,
    "valuation_rerating": 30,
    "capital_allocation": 38,
    "information_confidence": 74
  },
  "after_stage": "Stage4B watch with offset check",
  "after_total_score_label": 59.0,
  "after_weighted_calc": 46.76,
  "raw_component_scores_after": {
    "eps_fcf_explosion": 38,
    "earnings_visibility": 42,
    "bottleneck_pricing": 22,
    "market_mispricing": 48,
    "valuation_rerating": 36,
    "capital_allocation": 44,
    "information_confidence": 78
  },
  "production_scoring_changed": false,
  "shadow_weight_only": true
}
```

## 7. Residual Contribution Summary

```text
new_independent_case_count = 8
new_independent_trigger_count = 8
unique_symbol_count = 5
positive_case_count = 3
counterexample_or_guardrail_case_count = 6
Stage2_count = 2
Stage2_Actionable_count = 2
Stage4B_count = 4
Stage4C_count = 0
source_proxy_only_count = 0
evidence_url_pending_count = 0
missing_required_mfe_mae_count = 0
corporate_action_contaminated_180D_count = 0
insufficient_forward_window_180D_count = 0
production_scoring_changed = false
shadow_weight_only = true
```

### Rule candidate

```text
C05_COST_RATE_BACKLOG_CASHFLOW_OFFSET_GATE

Rule idea:
- Order/backlog/sales/quarterly-profit headlines are not sufficient for Stage2-Actionable or Yellow when raw-material cost, cost-rate adjustment, bad debt, or construction-quality trust breaks are explicit.
- If explicit cost improvement, settlement profit, project profitability, and next-year order/profit guidance appear together, the case can repair Stage2-Actionable and, in clean price paths, Stage3-Yellow; Green remains blocked until FCF/margin conversion is visible.
- Earnings decline alone does not make hard 4C. Hard 4C needs a confirmed non-price thesis break: order collapse, liquidity/covenant stress, irreversible project cost blow-up, quality/trust failure without offset, or working-capital break.
- Explicit offset quality, such as cost-ratio rebound guidance or net-cash/order stability, routes negative headlines to local 4B watch rather than hard 4C.
```

## 8. Machine-Readable JSONL Rows

### trigger rows

```jsonl
{"row_type": "trigger", "schema_version": "e2r_stock_web_v12_residual.v1", "research_file": "e2r_stock_web_v12_residual_round_R1_loop_200_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C05_EPC_MEGA_CONTRACT_MARGIN_GAP_research.md", "selected_round": "R1", "selected_loop": 200, "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C05_EPC_MEGA_CONTRACT_MARGIN_GAP", "fine_archetype_id": "EPC_COST_RATE_BACKLOG_TO_CASHFLOW_OFFSET_REPAIR", "case_id": "C05_200_01_HYUNDAI_EC_Q1_2024_HEADLINE_WITH_LATER_COST_BREAK", "symbol": "000720", "company_name": "Hyundai E&C", "trigger_type": "Stage2", "case_role": "stage2_false_positive_counterexample", "fine_case_role": "q1_headline_without_durable_cost_bridge", "trigger_date": "2024-04-19", "entry_date": "2024-04-19", "entry_price": 33250.0, "actual_1d_ohlcv": {"o": 32000.0, "h": 33450.0, "l": 31600.0, "c": 33250.0, "v": 727477, "a": 23799312600.0, "mc": 3702579186250.0, "s": 111355765, "m": "KOSPI"}, "price_source": "Songdaiki/stock-web", "price_source_url": "https://github.com/Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/000/000720/<year>.csv", "shard_files_used": ["000720_2024.csv", "000720_2025.csv"], "profile_path": "atlas/symbol_profiles/000/000720.json", "profile_note": "profile: atlas/symbol_profiles/000/000720.json; corporate_action_candidate_dates=[1998-05-23, 1998-11-19, 1999-03-05, 2001-07-06, 2001-07-12, 2004-01-13, 2004-04-07]; outside selected 2024/2025 D~D+180 windows.", "corporate_action_contaminated_180D": false, "insufficient_forward_window_180D": false, "calibration_usable": true, "forward_rows_available": 411, "shares_unique_180D_window": 1, "MFE_30D_pct": 8.27, "MAE_30D_pct": -4.96, "MFE_90D_pct": 8.27, "MAE_90D_pct": -12.63, "MFE_180D_pct": 8.27, "MAE_180D_pct": -27.52, "peak_date": "2024-05-09", "peak_price": 36000.0, "drawdown_after_peak_pct": -33.06, "drawdown_trough_date": "2024-12-09", "window_30D_end_date": "2024-06-05", "window_90D_end_date": "2024-08-30", "window_180D_end_date": "2025-01-16", "evidence_summary": "Yonhap reported that Hyundai E&C Q1 2024 operating profit surged 44.6% YoY to KRW250.9B and revenue rose 41.7% to KRW8.55T on strong housing and overseas business. The same 2024 cycle later showed Q4 one-off/cost pressure, so the Q1 headline is a Stage2 signal but not Actionable/Yellow without cost-rate and cash-flow durability.", "evidence_url": "https://en.yna.co.kr/view/AEN20240419005652320", "evidence_family": ["earnings_headline", "overseas_business_growth", "later_cost_rate_break", "backlog_to_cashflow_gap"], "source_proxy_only": false, "evidence_url_pending": false, "raw_component_score_breakdown_before": {"eps_fcf_explosion": 78, "earnings_visibility": 76, "bottleneck_pricing": 45, "market_mispricing": 58, "valuation_rerating": 54, "capital_allocation": 55, "information_confidence": 82}, "raw_component_score_breakdown_after": {"eps_fcf_explosion": 55, "earnings_visibility": 58, "bottleneck_pricing": 35, "market_mispricing": 45, "valuation_rerating": 38, "capital_allocation": 48, "information_confidence": 78}, "score_simulation": {"current_profile_stage": "Stage2-Actionable if headline-only bonus is overused", "current_profile_score": 76.0, "shadow_stage": "Stage2 capped / Green blocker", "shadow_score": 62.0, "weighted_before_calc": 68.42, "weighted_after_calc": 54.8}, "current_profile_error_label": "false_positive_if_q1_growth_is_treated_as_durable_margin_bridge", "duplicate_key": "C05_EPC_MEGA_CONTRACT_MARGIN_GAP|000720|Stage2|2024-04-19", "representative_for_aggregate": true, "is_new_independent_case": true, "production_scoring_changed": false, "shadow_weight_only": true, "positive_case": false, "counterexample_or_guardrail_case": true, "residual_label": "q1_growth_headline_needs_cost_rate_and_fcf_follow_through"}
{"row_type": "trigger", "schema_version": "e2r_stock_web_v12_residual.v1", "research_file": "e2r_stock_web_v12_residual_round_R1_loop_200_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C05_EPC_MEGA_CONTRACT_MARGIN_GAP_research.md", "selected_round": "R1", "selected_loop": 200, "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C05_EPC_MEGA_CONTRACT_MARGIN_GAP", "fine_archetype_id": "EPC_COST_RATE_BACKLOG_TO_CASHFLOW_OFFSET_REPAIR", "case_id": "C05_200_02_HYUNDAI_EC_Q2_2024_RAW_MATERIAL_COST_4B", "symbol": "000720", "company_name": "Hyundai E&C", "trigger_type": "Stage4B", "case_role": "local_4b_cost_rate_guardrail", "fine_case_role": "revenue_growth_with_raw_material_cost_pressure", "trigger_date": "2024-07-19", "entry_date": "2024-07-19", "entry_price": 32600.0, "actual_1d_ohlcv": {"o": 33100.0, "h": 33100.0, "l": 32450.0, "c": 32600.0, "v": 775289, "a": 25298546100.0, "mc": 3630197939000.0, "s": 111355765, "m": "KOSPI"}, "price_source": "Songdaiki/stock-web", "price_source_url": "https://github.com/Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/000/000720/<year>.csv", "shard_files_used": ["000720_2024.csv", "000720_2025.csv"], "profile_path": "atlas/symbol_profiles/000/000720.json", "profile_note": "profile: atlas/symbol_profiles/000/000720.json; corporate_action_candidate_dates=[1998-05-23, 1998-11-19, 1999-03-05, 2001-07-06, 2001-07-12, 2004-01-13, 2004-04-07]; outside selected 2024/2025 D~D+180 windows.", "corporate_action_contaminated_180D": false, "insufficient_forward_window_180D": false, "calibration_usable": true, "forward_rows_available": 350, "shares_unique_180D_window": 1, "MFE_30D_pct": 4.75, "MAE_30D_pct": -10.89, "MFE_90D_pct": 4.75, "MAE_90D_pct": -16.87, "MFE_180D_pct": 22.24, "MAE_180D_pct": -26.07, "peak_date": "2025-04-18", "peak_price": 39850.0, "drawdown_after_peak_pct": -3.01, "drawdown_trough_date": "2025-04-18", "window_30D_end_date": "2024-09-02", "window_90D_end_date": "2024-12-03", "window_180D_end_date": "2025-04-18", "evidence_summary": "Yonhap reported Q2 2024 net profit down 31.2% and operating profit down 34.1% YoY, while sales rose 20.4%; the explicit reason was a rise in raw material costs. This is not a new positive bridge; it is a C05 cost-rate watch despite later rebound.", "evidence_url": "https://en.yna.co.kr/view/AEN20240719004551320", "evidence_family": ["raw_material_cost_pressure", "margin_gap", "revenue_growth_quality_check", "local_4b_watch"], "source_proxy_only": false, "evidence_url_pending": false, "raw_component_score_breakdown_before": {"eps_fcf_explosion": 62, "earnings_visibility": 64, "bottleneck_pricing": 42, "market_mispricing": 55, "valuation_rerating": 50, "capital_allocation": 52, "information_confidence": 78}, "raw_component_score_breakdown_after": {"eps_fcf_explosion": 38, "earnings_visibility": 42, "bottleneck_pricing": 28, "market_mispricing": 48, "valuation_rerating": 38, "capital_allocation": 42, "information_confidence": 82}, "score_simulation": {"current_profile_stage": "Stage2 if revenue growth is overweighted", "current_profile_score": 67.0, "shadow_stage": "Stage4B local watch, not hard 4C", "shadow_score": 54.0, "weighted_before_calc": 60.8, "weighted_after_calc": 48.2}, "current_profile_error_label": "revenue_growth_overstates_quality_when_cost_rate_break_is_explicit", "duplicate_key": "C05_EPC_MEGA_CONTRACT_MARGIN_GAP|000720|Stage4B|2024-07-19", "representative_for_aggregate": true, "is_new_independent_case": true, "production_scoring_changed": false, "shadow_weight_only": true, "positive_case": false, "counterexample_or_guardrail_case": true, "residual_label": "revenue_growth_with_raw_material_cost_pressure_routes_to_4b_watch"}
{"row_type": "trigger", "schema_version": "e2r_stock_web_v12_residual.v1", "research_file": "e2r_stock_web_v12_residual_round_R1_loop_200_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C05_EPC_MEGA_CONTRACT_MARGIN_GAP_research.md", "selected_round": "R1", "selected_loop": 200, "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C05_EPC_MEGA_CONTRACT_MARGIN_GAP", "fine_archetype_id": "EPC_COST_RATE_BACKLOG_TO_CASHFLOW_OFFSET_REPAIR", "case_id": "C05_200_03_SAMSUNG_ENA_H1_2024_COST_IMPROVEMENT_HIGH_MAE", "symbol": "028050", "company_name": "Samsung E&A", "trigger_type": "Stage2-Actionable", "case_role": "high_mae_positive_guardrail", "fine_case_role": "cost_improvement_positive_but_entry_near_local_peak", "trigger_date": "2024-07-25", "entry_date": "2024-07-25", "entry_price": 25700.0, "actual_1d_ohlcv": {"o": 24700.0, "h": 26200.0, "l": 24400.0, "c": 25700.0, "v": 1753958, "a": 44657396850.0, "mc": 5037200000000.0, "s": 196000000, "m": "KOSPI"}, "price_source": "Songdaiki/stock-web", "price_source_url": "https://github.com/Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/028/028050/<year>.csv", "shard_files_used": ["028050_2024.csv", "028050_2025.csv"], "profile_path": "atlas/symbol_profiles/028/028050.json", "profile_note": "profile: atlas/symbol_profiles/028/028050.json; name changed to Samsung E&A from 2024-04-08; corporate_action_candidate_dates=[1997-08-22, 1999-01-13, 1999-05-26, 1999-09-29, 2016-02-26]; outside selected D~D+180 windows.", "corporate_action_contaminated_180D": false, "insufficient_forward_window_180D": false, "calibration_usable": true, "forward_rows_available": 346, "shares_unique_180D_window": 1, "MFE_30D_pct": 14.01, "MAE_30D_pct": -8.75, "MFE_90D_pct": 14.01, "MAE_90D_pct": -36.58, "MFE_180D_pct": 14.01, "MAE_180D_pct": -36.58, "peak_date": "2024-07-30", "peak_price": 29300.0, "drawdown_after_peak_pct": -44.37, "drawdown_trough_date": "2024-12-09", "window_30D_end_date": "2024-09-06", "window_90D_end_date": "2024-12-09", "window_180D_end_date": "2025-04-24", "evidence_summary": "Samsung E&A said H1 2024 revenue reached KRW5.71T, operating profit KRW471.9B and net profit KRW369.4B, citing settlement and cost improvements in late-stage hydrocarbon projects and a stable profit structure. The forward path had deep MAE, so it is Actionable but not Green.", "evidence_url": "https://samsungena.com/en/newsroom/news/view?idx=15609", "evidence_family": ["cost_improvement", "late_stage_hydrocarbon_projects", "stable_profit_structure", "high_mae_green_blocker"], "source_proxy_only": false, "evidence_url_pending": false, "raw_component_score_breakdown_before": {"eps_fcf_explosion": 76, "earnings_visibility": 78, "bottleneck_pricing": 55, "market_mispricing": 62, "valuation_rerating": 58, "capital_allocation": 56, "information_confidence": 88}, "raw_component_score_breakdown_after": {"eps_fcf_explosion": 68, "earnings_visibility": 72, "bottleneck_pricing": 48, "market_mispricing": 43, "valuation_rerating": 42, "capital_allocation": 54, "information_confidence": 88}, "score_simulation": {"current_profile_stage": "Stage3-Yellow if cost-improvement language is overtrusted", "current_profile_score": 79.0, "shadow_stage": "Stage2-Actionable with Green blocker", "shadow_score": 70.0, "weighted_before_calc": 71.66, "weighted_after_calc": 64.16}, "current_profile_error_label": "too_early_yellow_if_cost_improvement_not_checked_against_peak_proximity", "duplicate_key": "C05_EPC_MEGA_CONTRACT_MARGIN_GAP|028050|Stage2-Actionable|2024-07-25", "representative_for_aggregate": true, "is_new_independent_case": true, "production_scoring_changed": false, "shadow_weight_only": true, "positive_case": true, "counterexample_or_guardrail_case": true, "residual_label": "cost_improvement_positive_still_needs_entry_quality_and_fcf_check"}
{"row_type": "trigger", "schema_version": "e2r_stock_web_v12_residual.v1", "research_file": "e2r_stock_web_v12_residual_round_R1_loop_200_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C05_EPC_MEGA_CONTRACT_MARGIN_GAP_research.md", "selected_round": "R1", "selected_loop": 200, "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C05_EPC_MEGA_CONTRACT_MARGIN_GAP", "fine_archetype_id": "EPC_COST_RATE_BACKLOG_TO_CASHFLOW_OFFSET_REPAIR", "case_id": "C05_200_04_SAMSUNG_ENA_Q4_2024_ORDER_AND_MARGIN_POSITIVE_CONTROL", "symbol": "028050", "company_name": "Samsung E&A", "trigger_type": "Stage2-Actionable", "case_role": "positive_control", "fine_case_role": "operating_profit_growth_plus_order_profitability_bridge", "trigger_date": "2025-01-23", "entry_date": "2025-01-23", "entry_price": 17440.0, "actual_1d_ohlcv": {"o": 18500.0, "h": 18580.0, "l": 17400.0, "c": 17440.0, "v": 1839171, "a": 32770360080.0, "mc": 3418240000000.0, "s": 196000000, "m": "KOSPI"}, "price_source": "Songdaiki/stock-web", "price_source_url": "https://github.com/Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/028/028050/<year>.csv", "shard_files_used": ["028050_2025.csv"], "profile_path": "atlas/symbol_profiles/028/028050.json", "profile_note": "profile: atlas/symbol_profiles/028/028050.json; name changed to Samsung E&A from 2024-04-08; corporate_action_candidate_dates=[1997-08-22, 1999-01-13, 1999-05-26, 1999-09-29, 2016-02-26]; outside selected D~D+180 windows.", "corporate_action_contaminated_180D": false, "insufficient_forward_window_180D": false, "calibration_usable": true, "forward_rows_available": 226, "shares_unique_180D_window": 1, "MFE_30D_pct": 12.67, "MAE_30D_pct": -6.08, "MFE_90D_pct": 36.18, "MAE_90D_pct": -6.08, "MFE_180D_pct": 75.75, "MAE_180D_pct": -6.08, "peak_date": "2025-10-23", "peak_price": 30650.0, "drawdown_after_peak_pct": -8.65, "drawdown_trough_date": "2025-10-23", "window_30D_end_date": "2025-03-13", "window_90D_end_date": "2025-06-12", "window_180D_end_date": "2025-10-24", "evidence_summary": "Samsung E&A reported Q4 2024 operating profit of KRW295.8B, up 9.6% YoY, and attributed performance to project profitability, settlement effects and cost improvements while setting 2025 guidance. This is a cleaner positive control after the July high-MAE case.", "evidence_url": "https://www.samsungena.com/en/newsroom/news/view?idx=15673", "evidence_family": ["operating_profit_growth", "stable_profit_structure", "new_order_guidance", "backlog_margin_bridge"], "source_proxy_only": false, "evidence_url_pending": false, "raw_component_score_breakdown_before": {"eps_fcf_explosion": 70, "earnings_visibility": 72, "bottleneck_pricing": 52, "market_mispricing": 55, "valuation_rerating": 50, "capital_allocation": 58, "information_confidence": 86}, "raw_component_score_breakdown_after": {"eps_fcf_explosion": 82, "earnings_visibility": 84, "bottleneck_pricing": 58, "market_mispricing": 62, "valuation_rerating": 56, "capital_allocation": 64, "information_confidence": 90}, "score_simulation": {"current_profile_stage": "Stage2-Actionable", "current_profile_score": 74.0, "shadow_stage": "Stage3-Yellow, not Green", "shadow_score": 81.0, "weighted_before_calc": 67.08, "weighted_after_calc": 75.2}, "current_profile_error_label": "too_late_if_direct_margin_order_bridge_is_underweighted", "duplicate_key": "C05_EPC_MEGA_CONTRACT_MARGIN_GAP|028050|Stage2-Actionable|2025-01-23", "representative_for_aggregate": true, "is_new_independent_case": true, "production_scoring_changed": false, "shadow_weight_only": true, "positive_case": true, "counterexample_or_guardrail_case": false, "residual_label": "confirmed_cost_improvement_and_order_guidance_can_repair_late_stage2"}
{"row_type": "trigger", "schema_version": "e2r_stock_web_v12_residual.v1", "research_file": "e2r_stock_web_v12_residual_round_R1_loop_200_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C05_EPC_MEGA_CONTRACT_MARGIN_GAP_research.md", "selected_round": "R1", "selected_loop": 200, "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C05_EPC_MEGA_CONTRACT_MARGIN_GAP", "fine_archetype_id": "EPC_COST_RATE_BACKLOG_TO_CASHFLOW_OFFSET_REPAIR", "case_id": "C05_200_05_GS_EC_2024_PROFIT_TURNAROUND_WITH_TRUST_OVERHANG", "symbol": "006360", "company_name": "GS E&C", "trigger_type": "Stage2", "case_role": "turnaround_positive_but_trust_discount", "fine_case_role": "profit_swing_without_full_quality_recovery", "trigger_date": "2025-02-05", "entry_date": "2025-02-05", "entry_price": 17300.0, "actual_1d_ohlcv": {"o": 17300.0, "h": 17760.0, "l": 17260.0, "c": 17300.0, "v": 338689, "a": 5904286820.0, "mc": 1480559777000.0, "s": 85581490, "m": "KOSPI"}, "price_source": "Songdaiki/stock-web", "price_source_url": "https://github.com/Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/006/006360/<year>.csv", "shard_files_used": ["006360_2025.csv"], "profile_path": "atlas/symbol_profiles/006/006360.json", "profile_note": "profile: atlas/symbol_profiles/006/006360.json; corporate_action_candidate_dates=[1999-05-07, 1999-12-01, 2014-06-25]; outside selected 2025 D~D+180 window.", "corporate_action_contaminated_180D": false, "insufficient_forward_window_180D": false, "calibration_usable": true, "forward_rows_available": 221, "shares_unique_180D_window": 1, "MFE_30D_pct": 14.45, "MAE_30D_pct": -0.29, "MFE_90D_pct": 43.64, "MAE_90D_pct": -12.2, "MFE_180D_pct": 43.64, "MAE_180D_pct": -12.2, "peak_date": "2025-06-12", "peak_price": 24850.0, "drawdown_after_peak_pct": -28.41, "drawdown_trough_date": "2025-09-03", "window_30D_end_date": "2025-03-20", "window_90D_end_date": "2025-06-19", "window_180D_end_date": "2025-10-31", "evidence_summary": "Yonhap reported GS E&C 2024 net profit of KRW264.9B, swinging from a KRW419.5B loss. The price path validates that turnaround language mattered, but the prior quality/regulatory overhang means this should repair Stage2, not jump straight to Yellow/Green.", "evidence_url": "https://en.yna.co.kr/view/AEN20250205002400320", "evidence_family": ["profit_turnaround", "regulatory_trust_overhang", "housing_quality_tail", "stage2_cap"], "source_proxy_only": false, "evidence_url_pending": false, "raw_component_score_breakdown_before": {"eps_fcf_explosion": 66, "earnings_visibility": 62, "bottleneck_pricing": 35, "market_mispricing": 58, "valuation_rerating": 48, "capital_allocation": 55, "information_confidence": 72}, "raw_component_score_breakdown_after": {"eps_fcf_explosion": 72, "earnings_visibility": 70, "bottleneck_pricing": 38, "market_mispricing": 62, "valuation_rerating": 52, "capital_allocation": 58, "information_confidence": 76}, "score_simulation": {"current_profile_stage": "Stage2", "current_profile_score": 68.0, "shadow_stage": "Stage2-Actionable capped below Yellow", "shadow_score": 72.0, "weighted_before_calc": 59.58, "weighted_after_calc": 64.64}, "current_profile_error_label": "mild_too_late_if_turnaround_ignored_but_green_blocker_stays", "duplicate_key": "C05_EPC_MEGA_CONTRACT_MARGIN_GAP|006360|Stage2|2025-02-05", "representative_for_aggregate": true, "is_new_independent_case": true, "production_scoring_changed": false, "shadow_weight_only": true, "positive_case": true, "counterexample_or_guardrail_case": false, "residual_label": "profit_turnaround_repairs_stage2_but_quality_overhang_blocks_green"}
{"row_type": "trigger", "schema_version": "e2r_stock_web_v12_residual.v1", "research_file": "e2r_stock_web_v12_residual_round_R1_loop_200_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C05_EPC_MEGA_CONTRACT_MARGIN_GAP_research.md", "selected_round": "R1", "selected_loop": 200, "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C05_EPC_MEGA_CONTRACT_MARGIN_GAP", "fine_archetype_id": "EPC_COST_RATE_BACKLOG_TO_CASHFLOW_OFFSET_REPAIR", "case_id": "C05_200_06_DAEWOO_EC_2024_OP_DOWN_OVERHARD_4C_OFFSET", "symbol": "047040", "company_name": "Daewoo E&C", "trigger_type": "Stage4B", "case_role": "overhard_4c_counterexample", "fine_case_role": "annual_op_down_but_no_liquidity_or_order_collapse", "trigger_date": "2025-02-06", "entry_date": "2025-02-06", "entry_price": 3360.0, "actual_1d_ohlcv": {"o": 3290.0, "h": 3420.0, "l": 3285.0, "c": 3360.0, "v": 1843821, "a": 6202796950.0, "mc": 1396492063680.0, "s": 415622638, "m": "KOSPI"}, "price_source": "Songdaiki/stock-web", "price_source_url": "https://github.com/Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/047/047040/<year>.csv", "shard_files_used": ["047040_2025.csv"], "profile_path": "atlas/symbol_profiles/047/047040.json", "profile_note": "profile: atlas/symbol_profiles/047/047040.json; corporate_action_candidate_dates=[2001-07-13, 2003-11-18, 2011-01-18]; outside selected 2025 D~D+180 window.", "corporate_action_contaminated_180D": false, "insufficient_forward_window_180D": false, "calibration_usable": true, "forward_rows_available": 253, "shares_unique_180D_window": 1, "MFE_30D_pct": 11.9, "MAE_30D_pct": -4.76, "MFE_90D_pct": 43.01, "MAE_90D_pct": -12.5, "MFE_180D_pct": 43.01, "MAE_180D_pct": -12.5, "peak_date": "2025-06-05", "peak_price": 4805.0, "drawdown_after_peak_pct": -26.33, "drawdown_trough_date": "2025-08-20", "window_30D_end_date": "2025-03-21", "window_90D_end_date": "2025-06-20", "window_180D_end_date": "2025-11-03", "evidence_summary": "Yonhap reported Daewoo E&C 2024 net income down 53.4%, operating profit down 39.2% and revenue down 9.8%. The stock-web path rebounded strongly, so this is a 4B earnings-quality watch unless order backlog, liquidity or project-cost thesis breaks are confirmed.", "evidence_url": "https://en.yna.co.kr/view/AEN20250206001600320", "evidence_family": ["operating_profit_down", "revenue_down", "net_income_down", "hard_4c_offset_check"], "source_proxy_only": false, "evidence_url_pending": false, "raw_component_score_breakdown_before": {"eps_fcf_explosion": 25, "earnings_visibility": 28, "bottleneck_pricing": 18, "market_mispricing": 35, "valuation_rerating": 28, "capital_allocation": 32, "information_confidence": 76}, "raw_component_score_breakdown_after": {"eps_fcf_explosion": 34, "earnings_visibility": 38, "bottleneck_pricing": 22, "market_mispricing": 48, "valuation_rerating": 36, "capital_allocation": 42, "information_confidence": 78}, "score_simulation": {"current_profile_stage": "Stage4C if earnings decline is treated as thesis break", "current_profile_score": 46.0, "shadow_stage": "Stage4B local watch", "shadow_score": 58.0, "weighted_before_calc": 37.22, "weighted_after_calc": 45.0}, "current_profile_error_label": "false_positive_hard_4c_when_earnings_decline_lacks_order_liquidity_break", "duplicate_key": "C05_EPC_MEGA_CONTRACT_MARGIN_GAP|047040|Stage4B|2025-02-06", "representative_for_aggregate": true, "is_new_independent_case": true, "production_scoring_changed": false, "shadow_weight_only": true, "positive_case": false, "counterexample_or_guardrail_case": true, "residual_label": "annual_op_decline_is_4b_unless_project_or_balance_sheet_break_confirms_4c"}
{"row_type": "trigger", "schema_version": "e2r_stock_web_v12_residual.v1", "research_file": "e2r_stock_web_v12_residual_round_R1_loop_200_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C05_EPC_MEGA_CONTRACT_MARGIN_GAP_research.md", "selected_round": "R1", "selected_loop": 200, "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C05_EPC_MEGA_CONTRACT_MARGIN_GAP", "fine_archetype_id": "EPC_COST_RATE_BACKLOG_TO_CASHFLOW_OFFSET_REPAIR", "case_id": "C05_200_07_DLENC_Q1_2024_NET_INCOME_DROP_CORRECT_4B", "symbol": "375500", "company_name": "DL E&C", "trigger_type": "Stage4B", "case_role": "correct_4b_negative_control", "fine_case_role": "net_income_drop_with_limited_positive_window", "trigger_date": "2024-05-02", "entry_date": "2024-05-02", "entry_price": 36700.0, "actual_1d_ohlcv": {"o": 36800.0, "h": 37500.0, "l": 36350.0, "c": 36700.0, "v": 76767, "a": 2815375350.0, "mc": 1420055964100.0, "s": 38693623, "m": "KOSPI"}, "price_source": "Songdaiki/stock-web", "price_source_url": "https://github.com/Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/375/375500/<year>.csv", "shard_files_used": ["375500_2024.csv", "375500_2025.csv"], "profile_path": "atlas/symbol_profiles/375/375500.json", "profile_note": "profile: atlas/symbol_profiles/375/375500.json; corporate_action_candidate_dates=[2022-04-08, 2022-04-28]; outside selected 2024/2025 D~D+180 windows.", "corporate_action_contaminated_180D": false, "insufficient_forward_window_180D": false, "calibration_usable": true, "forward_rows_available": 403, "shares_unique_180D_window": 1, "MFE_30D_pct": 7.63, "MAE_30D_pct": -10.22, "MFE_90D_pct": 7.63, "MAE_90D_pct": -22.07, "MFE_180D_pct": 7.63, "MAE_180D_pct": -22.07, "peak_date": "2024-06-13", "peak_price": 39500.0, "drawdown_after_peak_pct": -27.59, "drawdown_trough_date": "2024-08-05", "window_30D_end_date": "2024-06-18", "window_90D_end_date": "2024-09-11", "window_180D_end_date": "2025-02-03", "evidence_summary": "Yonhap reported DL E&C Q1 2024 net income down 72.3% YoY. The forward price path had shallow MFE and -22% 180D MAE, validating a local 4B/caution route rather than treating weak earnings as harmless noise.", "evidence_url": "https://en.yna.co.kr/view/AEN20240502003000320", "evidence_family": ["net_income_down", "cost_rate_watch", "earnings_visibility_break", "correct_4b"], "source_proxy_only": false, "evidence_url_pending": false, "raw_component_score_breakdown_before": {"eps_fcf_explosion": 44, "earnings_visibility": 42, "bottleneck_pricing": 24, "market_mispricing": 50, "valuation_rerating": 38, "capital_allocation": 46, "information_confidence": 74}, "raw_component_score_breakdown_after": {"eps_fcf_explosion": 30, "earnings_visibility": 32, "bottleneck_pricing": 18, "market_mispricing": 42, "valuation_rerating": 32, "capital_allocation": 38, "information_confidence": 76}, "score_simulation": {"current_profile_stage": "Stage2 if backlog/order language offsets too much", "current_profile_score": 57.0, "shadow_stage": "Stage4B confirmed", "shadow_score": 48.0, "weighted_before_calc": 47.84, "weighted_after_calc": 40.72}, "current_profile_error_label": "false_positive_if_backlog_language_offsets_earnings_quality_too_much", "duplicate_key": "C05_EPC_MEGA_CONTRACT_MARGIN_GAP|375500|Stage4B|2024-05-02", "representative_for_aggregate": true, "is_new_independent_case": true, "production_scoring_changed": false, "shadow_weight_only": true, "positive_case": false, "counterexample_or_guardrail_case": true, "residual_label": "weak_net_income_and_cost_visibility_should_keep_c05_in_4b_watch"}
{"row_type": "trigger", "schema_version": "e2r_stock_web_v12_residual.v1", "research_file": "e2r_stock_web_v12_residual_round_R1_loop_200_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C05_EPC_MEGA_CONTRACT_MARGIN_GAP_research.md", "selected_round": "R1", "selected_loop": 200, "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C05_EPC_MEGA_CONTRACT_MARGIN_GAP", "fine_archetype_id": "EPC_COST_RATE_BACKLOG_TO_CASHFLOW_OFFSET_REPAIR", "case_id": "C05_200_08_DLENC_Q2_2024_COST_IMPROVEMENT_OFFSET_4B_NOT_4C", "symbol": "375500", "company_name": "DL E&C", "trigger_type": "Stage4B", "case_role": "offset_quality_counterexample", "fine_case_role": "q2_op_drop_but_explicit_cost_rate_rebound_guidance", "trigger_date": "2024-08-01", "entry_date": "2024-08-01", "entry_price": 34650.0, "actual_1d_ohlcv": {"o": 34900.0, "h": 35800.0, "l": 34350.0, "c": 34650.0, "v": 202635, "a": 7080301350.0, "mc": 1340734036950.0, "s": 38693623, "m": "KOSPI"}, "price_source": "Songdaiki/stock-web", "price_source_url": "https://github.com/Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/375/375500/<year>.csv", "shard_files_used": ["375500_2024.csv", "375500_2025.csv"], "profile_path": "atlas/symbol_profiles/375/375500.json", "profile_note": "profile: atlas/symbol_profiles/375/375500.json; corporate_action_candidate_dates=[2022-04-08, 2022-04-28]; outside selected 2024/2025 D~D+180 windows.", "corporate_action_contaminated_180D": false, "insufficient_forward_window_180D": false, "calibration_usable": true, "forward_rows_available": 341, "shares_unique_180D_window": 1, "MFE_30D_pct": 3.32, "MAE_30D_pct": -17.46, "MFE_90D_pct": 3.32, "MAE_90D_pct": -17.46, "MFE_180D_pct": 35.5, "MAE_180D_pct": -17.46, "peak_date": "2025-03-10", "peak_price": 46950.0, "drawdown_after_peak_pct": -20.87, "drawdown_trough_date": "2025-04-09", "window_30D_end_date": "2024-09-13", "window_90D_end_date": "2024-12-16", "window_180D_end_date": "2025-05-02", "evidence_summary": "Asiae reported DL E&C Q2 2024 operating profit down 54.7%, but the article also framed an expected second-half operating profit rebound due to cost-ratio improvement. Later 180D MFE was positive, so hard 4C should be deferred when offset quality is explicit.", "evidence_url": "https://www.asiae.co.kr/en/article/2024080114294271959", "evidence_family": ["operating_profit_down", "cost_ratio_improvement_guidance", "4b_not_4c", "offset_quality"], "source_proxy_only": false, "evidence_url_pending": false, "raw_component_score_breakdown_before": {"eps_fcf_explosion": 30, "earnings_visibility": 32, "bottleneck_pricing": 18, "market_mispricing": 42, "valuation_rerating": 30, "capital_allocation": 38, "information_confidence": 74}, "raw_component_score_breakdown_after": {"eps_fcf_explosion": 38, "earnings_visibility": 42, "bottleneck_pricing": 22, "market_mispricing": 48, "valuation_rerating": 36, "capital_allocation": 44, "information_confidence": 78}, "score_simulation": {"current_profile_stage": "Stage4C if operating-profit drop is overhardened", "current_profile_score": 51.0, "shadow_stage": "Stage4B watch with offset check", "shadow_score": 59.0, "weighted_before_calc": 40.12, "weighted_after_calc": 46.76}, "current_profile_error_label": "overhard_4c_if_cost_rate_rebound_guidance_is_ignored", "duplicate_key": "C05_EPC_MEGA_CONTRACT_MARGIN_GAP|375500|Stage4B|2024-08-01", "representative_for_aggregate": true, "is_new_independent_case": true, "production_scoring_changed": false, "shadow_weight_only": true, "positive_case": false, "counterexample_or_guardrail_case": true, "residual_label": "explicit_cost_rate_rebound_guidance_keeps_negative_earnings_case_in_4b_not_4c"}
```

### score_simulation rows

```jsonl
{"row_type": "score_simulation", "schema_version": "e2r_stock_web_v12_residual.v1", "research_file": "e2r_stock_web_v12_residual_round_R1_loop_200_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C05_EPC_MEGA_CONTRACT_MARGIN_GAP_research.md", "case_id": "C05_200_01_HYUNDAI_EC_Q1_2024_HEADLINE_WITH_LATER_COST_BREAK", "symbol": "000720", "canonical_archetype_id": "C05_EPC_MEGA_CONTRACT_MARGIN_GAP", "fine_archetype_id": "EPC_COST_RATE_BACKLOG_TO_CASHFLOW_OFFSET_REPAIR", "before_profile_id": "e2r_2_1_stock_web_calibrated_proxy", "after_profile_id": "proposed_C05_cost_rate_cashflow_offset_shadow_profile", "before_stage": "Stage2-Actionable if headline-only bonus is overused", "after_stage": "Stage2 capped / Green blocker", "before_total_score": 76.0, "after_total_score": 62.0, "raw_component_scores_before": {"eps_fcf_explosion": 78, "earnings_visibility": 76, "bottleneck_pricing": 45, "market_mispricing": 58, "valuation_rerating": 54, "capital_allocation": 55, "information_confidence": 82}, "raw_component_scores_after": {"eps_fcf_explosion": 55, "earnings_visibility": 58, "bottleneck_pricing": 35, "market_mispricing": 45, "valuation_rerating": 38, "capital_allocation": 48, "information_confidence": 78}, "simulation_purpose": "shadow_residual_research_only", "production_scoring_changed": false}
{"row_type": "score_simulation", "schema_version": "e2r_stock_web_v12_residual.v1", "research_file": "e2r_stock_web_v12_residual_round_R1_loop_200_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C05_EPC_MEGA_CONTRACT_MARGIN_GAP_research.md", "case_id": "C05_200_02_HYUNDAI_EC_Q2_2024_RAW_MATERIAL_COST_4B", "symbol": "000720", "canonical_archetype_id": "C05_EPC_MEGA_CONTRACT_MARGIN_GAP", "fine_archetype_id": "EPC_COST_RATE_BACKLOG_TO_CASHFLOW_OFFSET_REPAIR", "before_profile_id": "e2r_2_1_stock_web_calibrated_proxy", "after_profile_id": "proposed_C05_cost_rate_cashflow_offset_shadow_profile", "before_stage": "Stage2 if revenue growth is overweighted", "after_stage": "Stage4B local watch, not hard 4C", "before_total_score": 67.0, "after_total_score": 54.0, "raw_component_scores_before": {"eps_fcf_explosion": 62, "earnings_visibility": 64, "bottleneck_pricing": 42, "market_mispricing": 55, "valuation_rerating": 50, "capital_allocation": 52, "information_confidence": 78}, "raw_component_scores_after": {"eps_fcf_explosion": 38, "earnings_visibility": 42, "bottleneck_pricing": 28, "market_mispricing": 48, "valuation_rerating": 38, "capital_allocation": 42, "information_confidence": 82}, "simulation_purpose": "shadow_residual_research_only", "production_scoring_changed": false}
{"row_type": "score_simulation", "schema_version": "e2r_stock_web_v12_residual.v1", "research_file": "e2r_stock_web_v12_residual_round_R1_loop_200_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C05_EPC_MEGA_CONTRACT_MARGIN_GAP_research.md", "case_id": "C05_200_03_SAMSUNG_ENA_H1_2024_COST_IMPROVEMENT_HIGH_MAE", "symbol": "028050", "canonical_archetype_id": "C05_EPC_MEGA_CONTRACT_MARGIN_GAP", "fine_archetype_id": "EPC_COST_RATE_BACKLOG_TO_CASHFLOW_OFFSET_REPAIR", "before_profile_id": "e2r_2_1_stock_web_calibrated_proxy", "after_profile_id": "proposed_C05_cost_rate_cashflow_offset_shadow_profile", "before_stage": "Stage3-Yellow if cost-improvement language is overtrusted", "after_stage": "Stage2-Actionable with Green blocker", "before_total_score": 79.0, "after_total_score": 70.0, "raw_component_scores_before": {"eps_fcf_explosion": 76, "earnings_visibility": 78, "bottleneck_pricing": 55, "market_mispricing": 62, "valuation_rerating": 58, "capital_allocation": 56, "information_confidence": 88}, "raw_component_scores_after": {"eps_fcf_explosion": 68, "earnings_visibility": 72, "bottleneck_pricing": 48, "market_mispricing": 43, "valuation_rerating": 42, "capital_allocation": 54, "information_confidence": 88}, "simulation_purpose": "shadow_residual_research_only", "production_scoring_changed": false}
{"row_type": "score_simulation", "schema_version": "e2r_stock_web_v12_residual.v1", "research_file": "e2r_stock_web_v12_residual_round_R1_loop_200_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C05_EPC_MEGA_CONTRACT_MARGIN_GAP_research.md", "case_id": "C05_200_04_SAMSUNG_ENA_Q4_2024_ORDER_AND_MARGIN_POSITIVE_CONTROL", "symbol": "028050", "canonical_archetype_id": "C05_EPC_MEGA_CONTRACT_MARGIN_GAP", "fine_archetype_id": "EPC_COST_RATE_BACKLOG_TO_CASHFLOW_OFFSET_REPAIR", "before_profile_id": "e2r_2_1_stock_web_calibrated_proxy", "after_profile_id": "proposed_C05_cost_rate_cashflow_offset_shadow_profile", "before_stage": "Stage2-Actionable", "after_stage": "Stage3-Yellow, not Green", "before_total_score": 74.0, "after_total_score": 81.0, "raw_component_scores_before": {"eps_fcf_explosion": 70, "earnings_visibility": 72, "bottleneck_pricing": 52, "market_mispricing": 55, "valuation_rerating": 50, "capital_allocation": 58, "information_confidence": 86}, "raw_component_scores_after": {"eps_fcf_explosion": 82, "earnings_visibility": 84, "bottleneck_pricing": 58, "market_mispricing": 62, "valuation_rerating": 56, "capital_allocation": 64, "information_confidence": 90}, "simulation_purpose": "shadow_residual_research_only", "production_scoring_changed": false}
{"row_type": "score_simulation", "schema_version": "e2r_stock_web_v12_residual.v1", "research_file": "e2r_stock_web_v12_residual_round_R1_loop_200_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C05_EPC_MEGA_CONTRACT_MARGIN_GAP_research.md", "case_id": "C05_200_05_GS_EC_2024_PROFIT_TURNAROUND_WITH_TRUST_OVERHANG", "symbol": "006360", "canonical_archetype_id": "C05_EPC_MEGA_CONTRACT_MARGIN_GAP", "fine_archetype_id": "EPC_COST_RATE_BACKLOG_TO_CASHFLOW_OFFSET_REPAIR", "before_profile_id": "e2r_2_1_stock_web_calibrated_proxy", "after_profile_id": "proposed_C05_cost_rate_cashflow_offset_shadow_profile", "before_stage": "Stage2", "after_stage": "Stage2-Actionable capped below Yellow", "before_total_score": 68.0, "after_total_score": 72.0, "raw_component_scores_before": {"eps_fcf_explosion": 66, "earnings_visibility": 62, "bottleneck_pricing": 35, "market_mispricing": 58, "valuation_rerating": 48, "capital_allocation": 55, "information_confidence": 72}, "raw_component_scores_after": {"eps_fcf_explosion": 72, "earnings_visibility": 70, "bottleneck_pricing": 38, "market_mispricing": 62, "valuation_rerating": 52, "capital_allocation": 58, "information_confidence": 76}, "simulation_purpose": "shadow_residual_research_only", "production_scoring_changed": false}
{"row_type": "score_simulation", "schema_version": "e2r_stock_web_v12_residual.v1", "research_file": "e2r_stock_web_v12_residual_round_R1_loop_200_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C05_EPC_MEGA_CONTRACT_MARGIN_GAP_research.md", "case_id": "C05_200_06_DAEWOO_EC_2024_OP_DOWN_OVERHARD_4C_OFFSET", "symbol": "047040", "canonical_archetype_id": "C05_EPC_MEGA_CONTRACT_MARGIN_GAP", "fine_archetype_id": "EPC_COST_RATE_BACKLOG_TO_CASHFLOW_OFFSET_REPAIR", "before_profile_id": "e2r_2_1_stock_web_calibrated_proxy", "after_profile_id": "proposed_C05_cost_rate_cashflow_offset_shadow_profile", "before_stage": "Stage4C if earnings decline is treated as thesis break", "after_stage": "Stage4B local watch", "before_total_score": 46.0, "after_total_score": 58.0, "raw_component_scores_before": {"eps_fcf_explosion": 25, "earnings_visibility": 28, "bottleneck_pricing": 18, "market_mispricing": 35, "valuation_rerating": 28, "capital_allocation": 32, "information_confidence": 76}, "raw_component_scores_after": {"eps_fcf_explosion": 34, "earnings_visibility": 38, "bottleneck_pricing": 22, "market_mispricing": 48, "valuation_rerating": 36, "capital_allocation": 42, "information_confidence": 78}, "simulation_purpose": "shadow_residual_research_only", "production_scoring_changed": false}
{"row_type": "score_simulation", "schema_version": "e2r_stock_web_v12_residual.v1", "research_file": "e2r_stock_web_v12_residual_round_R1_loop_200_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C05_EPC_MEGA_CONTRACT_MARGIN_GAP_research.md", "case_id": "C05_200_07_DLENC_Q1_2024_NET_INCOME_DROP_CORRECT_4B", "symbol": "375500", "canonical_archetype_id": "C05_EPC_MEGA_CONTRACT_MARGIN_GAP", "fine_archetype_id": "EPC_COST_RATE_BACKLOG_TO_CASHFLOW_OFFSET_REPAIR", "before_profile_id": "e2r_2_1_stock_web_calibrated_proxy", "after_profile_id": "proposed_C05_cost_rate_cashflow_offset_shadow_profile", "before_stage": "Stage2 if backlog/order language offsets too much", "after_stage": "Stage4B confirmed", "before_total_score": 57.0, "after_total_score": 48.0, "raw_component_scores_before": {"eps_fcf_explosion": 44, "earnings_visibility": 42, "bottleneck_pricing": 24, "market_mispricing": 50, "valuation_rerating": 38, "capital_allocation": 46, "information_confidence": 74}, "raw_component_scores_after": {"eps_fcf_explosion": 30, "earnings_visibility": 32, "bottleneck_pricing": 18, "market_mispricing": 42, "valuation_rerating": 32, "capital_allocation": 38, "information_confidence": 76}, "simulation_purpose": "shadow_residual_research_only", "production_scoring_changed": false}
{"row_type": "score_simulation", "schema_version": "e2r_stock_web_v12_residual.v1", "research_file": "e2r_stock_web_v12_residual_round_R1_loop_200_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C05_EPC_MEGA_CONTRACT_MARGIN_GAP_research.md", "case_id": "C05_200_08_DLENC_Q2_2024_COST_IMPROVEMENT_OFFSET_4B_NOT_4C", "symbol": "375500", "canonical_archetype_id": "C05_EPC_MEGA_CONTRACT_MARGIN_GAP", "fine_archetype_id": "EPC_COST_RATE_BACKLOG_TO_CASHFLOW_OFFSET_REPAIR", "before_profile_id": "e2r_2_1_stock_web_calibrated_proxy", "after_profile_id": "proposed_C05_cost_rate_cashflow_offset_shadow_profile", "before_stage": "Stage4C if operating-profit drop is overhardened", "after_stage": "Stage4B watch with offset check", "before_total_score": 51.0, "after_total_score": 59.0, "raw_component_scores_before": {"eps_fcf_explosion": 30, "earnings_visibility": 32, "bottleneck_pricing": 18, "market_mispricing": 42, "valuation_rerating": 30, "capital_allocation": 38, "information_confidence": 74}, "raw_component_scores_after": {"eps_fcf_explosion": 38, "earnings_visibility": 42, "bottleneck_pricing": 22, "market_mispricing": 48, "valuation_rerating": 36, "capital_allocation": 44, "information_confidence": 78}, "simulation_purpose": "shadow_residual_research_only", "production_scoring_changed": false}
```

### aggregate / shadow rows

```jsonl
{"row_type": "aggregate", "research_file": "e2r_stock_web_v12_residual_round_R1_loop_200_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C05_EPC_MEGA_CONTRACT_MARGIN_GAP_research.md", "selected_round": "R1", "selected_loop": 200, "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C05_EPC_MEGA_CONTRACT_MARGIN_GAP", "fine_archetype_id": "EPC_COST_RATE_BACKLOG_TO_CASHFLOW_OFFSET_REPAIR", "new_independent_case_count": 8, "new_independent_trigger_count": 8, "unique_symbol_count": 5, "positive_case_count": 3, "counterexample_or_guardrail_case_count": 6, "stage4b_case_count": 4, "stage4c_case_count": 0, "stage2_case_count": 2, "stage2_actionable_case_count": 2, "source_proxy_only_count": 0, "evidence_url_pending_count": 0, "missing_required_mfe_mae_count": 0, "corporate_action_contaminated_180D_count": 0, "insufficient_forward_window_180D_count": 0, "production_scoring_changed": false, "shadow_weight_only": true, "residual_summary": "C05 needs a cost-rate/backlog-to-cashflow offset gate: sales/order/backlog headlines should not override raw-material cost, bad-debt or cost-rate breaks; explicit cost improvement and order guidance can repair Stage2, but Green remains blocked until FCF/margin conversion is visible."}
{"row_type": "shadow_weight", "research_file": "e2r_stock_web_v12_residual_round_R1_loop_200_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C05_EPC_MEGA_CONTRACT_MARGIN_GAP_research.md", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C05_EPC_MEGA_CONTRACT_MARGIN_GAP", "axis": "C05_COST_RATE_BACKLOG_CASHFLOW_OFFSET_GATE", "baseline_weights": {"eps_fcf_explosion": 18, "earnings_visibility": 22, "bottleneck_pricing": 10, "market_mispricing": 12, "valuation_rerating": 10, "capital_allocation": 8, "information_confidence": 20}, "tested_weight_bias": "increase information_confidence and earnings_visibility penalty power for cost-rate/bad-debt breaks; allow limited earnings_visibility repair when cost improvement + order guidance both exist", "production_scoring_changed": false, "shadow_weight_only": true, "recommended_action": "hold_for_batch_calibration_not_immediate_patch"}
```

## 9. Batch Ingest Self-Audit

| gate | result | note |
|---|---|---|
| standard filename regex | pass | full v12 result filename used |
| filename round/loop equals metadata | pass | R1 / loop 200 |
| selected round-sector pair | pass | R1 -> L1 |
| canonical archetype recognized | pass | C05_EPC_MEGA_CONTRACT_MARGIN_GAP |
| stock-web actual 1D rows used | pass | local shards from Songdaiki/stock-web mirror |
| 30/90/180D MFE/MAE present in every trigger row | pass | 8/8 |
| entry price present in every trigger row | pass | 8/8 |
| corporate action contamination | pass | profile candidate dates outside D~D+180; 180D shares column stable |
| insufficient forward 180D window | pass | all windows end before manifest max date |
| source_proxy_only | pass | 0 |
| evidence_url_pending | pass | 0 |
| production scoring changed | pass | false |
| handoff prompt embedded but not executed | pass | see below |

## 10. Deferred Coding Agent Handoff Prompt

```text
Read this MD only in a later batch calibration/coding session. Do not treat it as an immediate production patch. Parse the JSONL trigger rows, verify stock-web paths, dedupe by canonical_archetype_id + symbol + trigger_type + entry_date, and compare with existing C05 rows. If enough independent C05 rows agree, consider a shadow-only C05_COST_RATE_BACKLOG_CASHFLOW_OFFSET_GATE. The patch should require explicit cost-rate / working-capital / bad-debt / quality-trust checks before Stage2-Actionable or Yellow, and should prevent earnings-decline-only hard 4C when offset quality is explicit. Maintain stage3_green_not_loosened_by_v12 = true.
```

## 11. Next Research State

```text
completed_round = R1
completed_loop = 200
selection_basis = docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket = Priority 1 balance / quality reinforcement
completed_large_sector_id = L1_INDUSTRIALS_INFRA_DEFENSE_GRID
completed_canonical_archetype_id = C05_EPC_MEGA_CONTRACT_MARGIN_GAP
completed_fine_archetype_id = EPC_COST_RATE_BACKLOG_TO_CASHFLOW_OFFSET_REPAIR
round_schedule_status = coverage_index_selected
round_sector_consistency = pass
next_recommended_archetypes = C01_ORDER_BACKLOG_MARGIN_BRIDGE_FCF_COUNTEREXAMPLE_REPAIR; C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE_SUPPLIER_ORDER_CONVERSION_REPAIR; C13_BATTERY_JV_UTILIZATION_AMPC_IRA_OFFSET_QUALITY_REPAIR; R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL_HOLDOUT_REFRESH; C05_EPC_MEGA_CONTRACT_MARGIN_GAP_HARD_4C_DIRECT_BREAK_ONLY
```
