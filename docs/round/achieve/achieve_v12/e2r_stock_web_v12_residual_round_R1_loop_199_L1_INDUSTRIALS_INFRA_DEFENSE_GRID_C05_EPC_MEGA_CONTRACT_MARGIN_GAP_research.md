# E2R v12 Stock-Web Residual Calibration Research

```yaml
research_file: e2r_stock_web_v12_residual_round_R1_loop_199_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C05_EPC_MEGA_CONTRACT_MARGIN_GAP_research.md
created_at_kst: 2026-06-15 17:34:50 KST
research_mode: post_calibrated_residual_historical_research_v12
selected_round: R1
selected_loop: 199
large_sector_id: L1_INDUSTRIALS_INFRA_DEFENSE_GRID
canonical_archetype_id: C05_EPC_MEGA_CONTRACT_MARGIN_GAP
fine_archetype_id: EPC_MARGIN_GAP_4C_TIMING_DIRECT_URL_REPAIR
selection_basis: docs/core/V12_Research_No_Repeat_Index.md
round_schedule_status: coverage_index_selected
production_scoring_changed: false
shadow_weight_only: true
```

## 0. Execution guardrails

This file follows `docs/core/e2r_v12_prompt_round_scheduler_corrected.txt` as the main execution prompt. It is a standalone markdown research file for v12 residual calibration. It does **not** patch `stock_agent`, does **not** change production scoring, does **not** perform live discovery, and uses the No-Repeat Index only as a duplicate-prevention and coverage ledger.

## 1. Coverage-index selection rationale

The No-Repeat Index currently shows the corpus is no longer in a simple row-scarcity phase. For `C05_EPC_MEGA_CONTRACT_MARGIN_GAP`, the ledger records 180 representative rows across 54 symbols, with positives/counterexamples 29/39 and 4B/4C rows 23/10. Its next stated repair direction is margin / working-capital failure counterexamples and 4C transition timing. The prior local run also spent several cycles on R13 cross-archetype cleanup, so this run returns to a sector-specific C05 repair axis.

Selected repair axis:

```text
C05_EPC_MEGA_CONTRACT_MARGIN_GAP
fine_archetype_id = EPC_MARGIN_GAP_4C_TIMING_DIRECT_URL_REPAIR
objective = distinguish hard 4C thesis break from local 4B cost-rate shock,
            and distinguish direct order / cost-rate recovery Stage2-Actionable
            from backlog quantity without margin/working-capital quality.
```

## 2. Stock-Web price validation

Primary price source is `Songdaiki/stock-web`. Price basis is `tradable_raw`; price adjustment status is `raw_unadjusted_marcap`. The manifest maximum date is 2026-02-20. Tradable shard schema is `d,o,h,l,c,v,a,mc,s,m`. MFE/MAE use the schema rule: from entry date through N forward tradable rows, MFE is max high / entry close minus 1, and MAE is min low / entry close minus 1.

Profile / corporate-action audit:

| Symbol | Company | Profile status | Corporate-action contamination D~D+180 |
|---|---|---|---|
| 006360 | GS E&C | profile checked; listed through 2026-02-20 | false |
| 028050 | Samsung E&A | profile checked; listed through 2026-02-20 | false |
| 000720 | Hyundai E&C | profile checked; listed through 2026-02-20 | false |
| 375500 | DL E&C | profile checked; listed through 2026-02-20 | false |
| 047040 | Daewoo E&C | profile checked; listed through 2026-02-20 | false |

## 3. Batch ingest self-audit

```text
new_independent_case_count: 10
new_independent_trigger_count: 10
unique_symbol_count: 5
calibration_usable_case_count: 10
calibration_usable_trigger_count: 10

stage2_or_stage2_actionable_count: 5
stage4b_count: 4
stage4c_count: 1
positive_or_control_count: 5
counterexample_or_guardrail_count: 5
current_profile_error_count: 6

source_proxy_only_count: 0
evidence_url_pending_count: 0
missing_required_mfe_mae_count: 0
corporate_action_contaminated_180D_count: 0
insufficient_forward_window_180D_count: 0
new_independent_ratio: 1.00
production_scoring_changed: false
shadow_weight_only: true
```

Novelty check against the immediately preceding C05 local run:

- Previous C05 local duplicate-prone anchors included 2023-08-28 GS E&C, 2025-02-04 Samsung E&A, 2023-06-27 Hyundai E&C, 2025-02-07 DL E&C, and 2025-02-07 Daewoo E&C.
- This run uses different `symbol + trigger_type + entry_date` hard keys and avoids the near-duplicate 2025-02-06/2025-02-07 construction cluster as trigger rows.
- Reused symbols are allowed only with new trigger dates, new evidence family, and new forward-window pattern.

## 4. Trigger price matrix

| Symbol | Company | Trigger | Entry | Entry close | 30D MFE/MAE | 90D MFE/MAE | 180D MFE/MAE | 180D peak | 180D trough |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 006360 | GS E&C | Stage4C | 2023-07-06 | 14520 | 10.12/-7.92 | 10.12/-12.74 | 19.83/-12.74 | 2023-11-23 | 2023-10-10 |
| 006360 | GS E&C | Stage4B | 2024-02-01 | 15690 | 3.44/-6.05 | 6.56/-10.52 | 38.62/-10.52 | 2024-08-27 | 2024-04-19 |
| 006360 | GS E&C | Stage2-Actionable | 2024-04-03 | 15630 | 6.97/-10.17 | 30.52/-10.17 | 39.16/-10.17 | 2024-08-27 | 2024-04-19 |
| 028050 | Samsung E&A | Stage2-Actionable | 2024-04-03 | 25300 | 6.72/-5.93 | 15.81/-14.62 | 15.81/-35.57 | 2024-07-30 | 2024-12-09 |
| 028050 | Samsung E&A | Stage4B | 2024-07-26 | 27900 | 5.02/-16.85 | 5.02/-41.58 | 5.02/-41.58 | 2024-07-30 | 2024-12-09 |
| 000720 | Hyundai E&C | Stage4B | 2024-10-23 | 28500 | 4.04/-7.19 | 31.75/-15.44 | 198.60/-15.44 | 2025-06-25 | 2024-12-09 |
| 000720 | Hyundai E&C | Stage4B | 2025-01-21 | 26100 | 43.87/-0.96 | 183.52/-0.96 | 226.05/-0.96 | 2025-06-25 | 2025-01-21 |
| 375500 | DL E&C | Stage2-Actionable | 2024-10-31 | 30900 | 12.62/-5.18 | 51.94/-5.18 | 93.20/-5.18 | 2025-06-26 | 2024-11-13 |
| 047040 | Daewoo E&C | Stage2 | 2024-01-30 | 4065 | 2.83/-10.82 | 2.83/-11.93 | 22.14/-12.79 | 2024-07-18 | 2024-08-05 |
| 047040 | Daewoo E&C | Stage2-Actionable | 2025-04-29 | 3520 | 36.51/-3.12 | 36.51/-3.12 | 63.64/-5.68 | 2026-01-23 | 2025-11-07 |

## 5. Evidence-to-price case notes


### Case 1. 006360 GS E&C — Stage4C / confirmed_non_price_thesis_break

- **Entry:** 2023-07-06 close 14520
- **Forward path:** 30D 10.12/-7.92, 90D 10.12/-12.74, 180D 19.83/-12.74; peak 2023-11-23, trough 2023-10-10
- **Evidence:** The evidence is a direct hard-break event: government findings blamed GS E&C quality management, the company accepted a full rebuild of 17 apartment blocks, and analysts discussed large rebuild-cost / earnings-cut risk. This is not a normal EPC order-cycle pause; it is a construction-quality and cash-cost thesis break.
- **Residual read:** hard_4c_validated_by_non_price_break_even_though_180d_rebound_exists
- **Duplicate key:** `C05_EPC_MEGA_CONTRACT_MARGIN_GAP|006360|Stage4C|2023-07-06`

### Case 2. 006360 GS E&C — Stage4B / regulatory_penalty_with_order_backlog_offset

- **Entry:** 2024-02-01 close 15690
- **Forward path:** 30D 3.44/-6.05, 90D 6.56/-10.52, 180D 38.62/-10.52; peak 2024-08-27, trough 2024-04-19
- **Evidence:** A regulatory and litigation overhang remained visible, including suspension risk and loss of brand/order trust. The later stock-web path rebounded, so the event should remain local 4B unless fresh order/backlog collapse or cash-liquidity break is confirmed.
- **Residual read:** current_profile_should_not_double_count_old_geomdan_break_as_fresh_hard_4c
- **Duplicate key:** `C05_EPC_MEGA_CONTRACT_MARGIN_GAP|006360|Stage4B|2024-02-01`

### Case 3. 006360 GS E&C — Stage2-Actionable / mega_gas_epc_order_with_margin_phasing_required

- **Entry:** 2024-04-03 close 15630
- **Forward path:** 30D 6.97/-10.17, 90D 30.52/-10.17, 180D 39.16/-10.17; peak 2024-08-27, trough 2024-04-19
- **Evidence:** The order evidence is direct and customer-specific, not a generic EPC rumor. It supports Stage2-Actionable, but Stage3/Green still require margin recognition, working-capital discipline, and execution-cost control because C05 failures often hide inside cost-rate drift.
- **Residual read:** current_profile_stage2_actionable_correct_but_green_should_wait_for_margin_bridge
- **Duplicate key:** `C05_EPC_MEGA_CONTRACT_MARGIN_GAP|006360|Stage2-Actionable|2024-04-03`

### Case 4. 028050 Samsung E&A — Stage2-Actionable / direct_order_positive_with_execution_mae

- **Entry:** 2024-04-03 close 25300
- **Forward path:** 30D 6.72/-5.93, 90D 15.81/-14.62, 180D 15.81/-35.57; peak 2024-07-30, trough 2024-12-09
- **Evidence:** Direct project-award evidence supports Stage2-Actionable. The 180D MAE of -35.57% shows why C05 direct-order positives need Green brakes until backlog conversion and margin are visible; order alone is a bridge, not the finished bridge deck.
- **Residual read:** stage2_actionable_preserved_green_blocked_by_high_mae_and_execution_gap
- **Duplicate key:** `C05_EPC_MEGA_CONTRACT_MARGIN_GAP|028050|Stage2-Actionable|2024-04-03`

### Case 5. 028050 Samsung E&A — Stage4B / late_backlog_extension_after_order_rerating

- **Entry:** 2024-07-26 close 27900
- **Forward path:** 30D 5.02/-16.85, 90D 5.02/-41.58, 180D 5.02/-41.58; peak 2024-07-30, trough 2024-12-09
- **Evidence:** 2Q24 had strong backlog and order visibility, so this is not a hard 4C. But the entry came after the order narrative had already been priced, and stock-web shows 180D MFE only 5.02% vs MAE -41.58%; this is a late-extension 4B / Green blocker row.
- **Residual read:** profile_should_cap_late_backlog_language_at_4b_not_green
- **Duplicate key:** `C05_EPC_MEGA_CONTRACT_MARGIN_GAP|028050|Stage4B|2024-07-26`

### Case 6. 000720 Hyundai E&C — Stage4B / cost_rate_shock_with_future_project_offset

- **Entry:** 2024-10-23 close 28500
- **Forward path:** 30D 4.04/-7.19, 90D 31.75/-15.44, 180D 198.60/-15.44; peak 2025-06-25, trough 2024-12-09
- **Evidence:** The cost-rate shock is genuine non-price 4B evidence. Yet the later stock-web path was extremely positive, showing that temporary cost-rate damage should not be upgraded to hard 4C if overseas/new-project offsets remain alive.
- **Residual read:** current_profile_false_4c_if_cost_rate_shock_overweighted
- **Duplicate key:** `C05_EPC_MEGA_CONTRACT_MARGIN_GAP|000720|Stage4B|2024-10-23`

### Case 7. 000720 Hyundai E&C — Stage4B / overseas_site_loss_with_bad_mix_rolloff_offset

- **Entry:** 2025-01-21 close 26100
- **Forward path:** 30D 43.87/-0.96, 90D 183.52/-0.96, 180D 226.05/-0.96; peak 2025-06-25, trough 2025-01-21
- **Evidence:** The news flow still contained overseas-site and low-margin mix concerns. But explicit mix rolloff / completion timing provided an offset bridge, and stock-web forward path validated that this was not a hard 4C. This is a strong C05 overhard-4C repair row.
- **Residual read:** current_profile_should_downshift_hard_4c_to_4b_watch_when_offset_bridge_is_explicit
- **Duplicate key:** `C05_EPC_MEGA_CONTRACT_MARGIN_GAP|000720|Stage4B|2025-01-21`

### Case 8. 375500 DL E&C — Stage2-Actionable / cost_rate_recovery_and_selective_order_strategy

- **Entry:** 2024-10-31 close 30900
- **Forward path:** 30D 12.62/-5.18, 90D 51.94/-5.18, 180D 93.20/-5.18; peak 2025-06-26, trough 2024-11-13
- **Evidence:** This is a clean positive C05 repair row: the evidence explicitly connects profitability to cost-rate improvement and high-profit order strategy. The forward path validates Stage2-Actionable while keeping Green gated until cash conversion and backlog quality are confirmed.
- **Residual read:** current_profile_stage2_actionable_correct_green_requires_cash_conversion
- **Duplicate key:** `C05_EPC_MEGA_CONTRACT_MARGIN_GAP|375500|Stage2-Actionable|2024-10-31`

### Case 9. 047040 Daewoo E&C — Stage2 / backlog_large_but_housing_cost_burden

- **Entry:** 2024-01-30 close 4065
- **Forward path:** 30D 2.83/-10.82, 90D 2.83/-11.93, 180D 22.14/-12.79; peak 2024-07-18, trough 2024-08-05
- **Evidence:** The row separates backlog quantity from margin quality. New orders and backlog were visible, but housing cost burden kept it at Stage2 rather than Stage2-Actionable/Yellow. The later 180D upside was positive, but the initial 90D path had little upside and meaningful drawdown.
- **Residual read:** current_profile_should_not_promote_backlog_quantity_without_margin_quality
- **Duplicate key:** `C05_EPC_MEGA_CONTRACT_MARGIN_GAP|047040|Stage2|2024-01-30`

### Case 10. 047040 Daewoo E&C — Stage2-Actionable / housing_and_plant_profit_recovery_backlog_confirmation

- **Entry:** 2025-04-29 close 3520
- **Forward path:** 30D 36.51/-3.12, 90D 36.51/-3.12, 180D 63.64/-5.68; peak 2026-01-23, trough 2025-11-07
- **Evidence:** Unlike generic backlog language, this row has explicit profitability improvement plus order/backlog support. The stock-web path validates Stage2-Actionable; the rule lesson is that C05 can be upgraded when cost-rate improvement is tied to business-line profit recovery, not merely order volume.
- **Residual read:** current_profile_stage2_actionable_correct_green_requires_more_than_one_quarter
- **Duplicate key:** `C05_EPC_MEGA_CONTRACT_MARGIN_GAP|047040|Stage2-Actionable|2025-04-29`


## 6. Shadow component score simulation

Weights used for C05 shadow simulation:

```json
{"eps_fcf_explosion": 18, "earnings_visibility": 22, "bottleneck_pricing": 10, "market_mispricing": 12, "valuation_rerating": 10, "capital_allocation": 8, "information_confidence": 20}
```

| case_id | trigger | EPS/FCF | Visibility | Bottleneck | Mispricing | Valuation | Capital | Info | Weighted total | verdict |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| C05_GS_GEOMDAN_REBUILD_COST_HARD_4C | Stage4C | 25 | 20 | 10 | 35 | 15 | 20 | 90 | 35.20 | hard_4c_validated_by_non_price_break_even_though_180d_rebound_exists |
| C05_GS_BUSINESS_SUSPENSION_OFFSET_4B | Stage4B | 35 | 30 | 20 | 50 | 30 | 35 | 85 | 43.70 | current_profile_should_not_double_count_old_geomdan_break_as_fresh_hard_4c |
| C05_GS_FADHILI_EPC_ORDER_STAGE2A | Stage2-Actionable | 75 | 82 | 55 | 55 | 50 | 60 | 92 | 71.84 | current_profile_stage2_actionable_correct_but_green_should_wait_for_margin_bridge |
| C05_SAMSUNG_ENA_FADHILI_ORDER_HIGH_MAE_STAGE2A | Stage2-Actionable | 72 | 80 | 50 | 45 | 45 | 55 | 92 | 68.26 | stage2_actionable_preserved_green_blocked_by_high_mae_and_execution_gap |
| C05_SAMSUNG_ENA_Q2_BACKLOG_LATE_EXTENSION_4B | Stage4B | 58 | 78 | 45 | 25 | 25 | 50 | 90 | 59.60 | profile_should_cap_late_backlog_language_at_4b_not_green |
| C05_HYUNDAI_ENC_Q3_COST_RATE_OFFSET_4B | Stage4B | 48 | 45 | 35 | 45 | 35 | 45 | 88 | 52.14 | current_profile_false_4c_if_cost_rate_shock_overweighted |
| C05_HYUNDAI_ENC_OVERSEAS_SITE_LOSS_OFFSET_4B | Stage4B | 58 | 60 | 35 | 60 | 55 | 55 | 86 | 61.44 | current_profile_should_downshift_hard_4c_to_4b_watch_when_offset_bridge_is_explicit |
| C05_DLENC_Q3_COST_RATE_RECOVERY_STAGE2A | Stage2-Actionable | 78 | 85 | 55 | 55 | 50 | 65 | 90 | 73.04 | current_profile_stage2_actionable_correct_green_requires_cash_conversion |
| C05_DAEWOO_2023_BACKLOG_COST_BURDEN_STAGE2 | Stage2 | 52 | 62 | 30 | 45 | 40 | 45 | 85 | 56.00 | current_profile_should_not_promote_backlog_quantity_without_margin_quality |
| C05_DAEWOO_Q1_IMPROVED_HOUSING_PLANT_STAGE2A | Stage2-Actionable | 80 | 80 | 50 | 50 | 45 | 60 | 88 | 69.90 | current_profile_stage2_actionable_correct_green_requires_more_than_one_quarter |

Interpretation:

- `Stage2-Actionable` in C05 is strongest when the evidence is not merely backlog quantity but a second bridge: customer-specific mega order, cost-rate improvement, business-line profit recovery, or explicit margin/working-capital visibility.
- `Stage4B` is the right holding pen when the company has a real cost-rate, regulatory, or execution shock but there is also a visible order-cycle, backlog, mix-rolloff, net-cash, or recovery offset.
- `Stage4C` is protected for confirmed non-price thesis breaks: quality failure, full rebuild/rework obligation, backlog/order collapse, liquidity break, or accounting trust break with weak offsets.
- High MFE after an ugly headline does not retroactively erase the 4B signal; it teaches that C05 needs an offset-quality gate before hard 4C.

## 7. Residual contribution

```yaml
residual_contribution_label: C05_4C_TIMING_AND_MARGIN_BRIDGE_DIRECT_URL_REPAIR
sector_rule_candidate: L1_C05_EPC_MARGIN_CASH_BRIDGE_AND_OFFSET_GATE
canonical_rule_candidate: C05_HARD_4C_REQUIRES_IRREVERSIBLE_MARGIN_CASH_BREAK
production_scoring_changed: false
shadow_weight_only: true
new_axis_proposed: false
existing_axis_strengthened:
  - stage2_required_bridge
  - 4b_non_price_evidence_required
  - hard_4c_thesis_break_confirmation
  - late_backlog_extension_green_blocker
existing_axis_refined:
  - order_backlog_quantity_is_not_margin_quality
  - cost_rate_shock_with_explicit_offset_is_4b_not_4c
  - direct_order_positive_requires_margin_phasing_for_stage3
existing_axis_weakened: []
```

### Proposed shadow rule text

```text
C05_EPC_MARGIN_GAP_4C_TIMING_GATE:
  IF evidence is mega EPC order / backlog expansion only
  THEN cap at Stage2-Actionable until margin recognition, cost-rate control,
       working-capital conversion, or customer payment schedule is confirmed.

  IF evidence is cost-rate shock, bad debt, project loss, regulatory suspension,
     or one-off overseas-site loss
  AND explicit offset exists via backlog, net cash, mix rolloff, project completion,
      or next-quarter cost-rate normalization
  THEN route to Stage4B / thesis_break_watch, not hard Stage4C.

  IF evidence confirms construction-quality failure, full rebuild/rework obligation,
     order/backlog collapse, liquidity stress, or accounting-trust break
  AND offset quality is weak
  THEN hard Stage4C is allowed even if later price path partially rebounds.
```

## 8. Machine-readable JSONL trigger rows

```jsonl
{"source_row_type":"v12_trigger_row","research_file":"e2r_stock_web_v12_residual_round_R1_loop_199_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C05_EPC_MEGA_CONTRACT_MARGIN_GAP_research.md","selected_round":"R1","selected_loop":199,"large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP","fine_archetype_id":"EPC_MARGIN_GAP_4C_TIMING_DIRECT_URL_REPAIR","case_id":"C05_GS_GEOMDAN_REBUILD_COST_HARD_4C","symbol":"006360","company_name":"GS E&C","evidence_date":"2023-07-06","entry_date":"2023-07-06","entry_price":14520.0,"trigger_type":"Stage4C","case_role":"counterexample_guardrail","fine_case_role":"confirmed_non_price_thesis_break","hard_duplicate_key":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP|006360|Stage4C|2023-07-06","evidence_source_class":"direct_url","evidence_urls":["https://en.yna.co.kr/view/AEN20230706005300320"],"evidence_summary":"The evidence is a direct hard-break event: government findings blamed GS E&C quality management, the company accepted a full rebuild of 17 apartment blocks, and analysts discussed large rebuild-cost / earnings-cut risk. This is not a normal EPC order-cycle pause; it is a construction-quality and cash-cost thesis break.","price_source_validation":{"primary_price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","manifest_max_date":"2026-02-20","schema_columns":"d,o,h,l,c,v,a,mc,s,m","shard_paths":["atlas/ohlcv_tradable_by_symbol_year/006/006360/2023.csv","atlas/ohlcv_tradable_by_symbol_year/006/006360/2024.csv"],"profile_checked":true,"corporate_action_contaminated_D_to_D_plus_180":false,"insufficient_forward_window_180D":false,"calibration_usable":true},"actual_entry_ohlc":{"d":"2023-07-06","c":14520.0},"price_path":{"mfe_30d_pct":10.12,"mae_30d_pct":-7.92,"mfe_90d_pct":10.12,"mae_90d_pct":-12.74,"mfe_180d_pct":19.83,"mae_180d_pct":-12.74,"peak_180d_date":"2023-11-23","trough_180d_date":"2023-10-10","rows_180d_inclusive":181},"stage_evidence":{"stage2_fields":[],"stage3_fields":[],"stage4b_fields":["large rebuild cost","brand/order damage","cost provision risk"],"stage4c_fields":["quality-management break","full rebuild obligation","non-price thesis break"]},"score_simulation":{"weights":{"eps_fcf_explosion":18,"earnings_visibility":22,"bottleneck_pricing":10,"market_mispricing":12,"valuation_rerating":10,"capital_allocation":8,"information_confidence":20},"raw_components":{"eps_fcf_explosion":25,"earnings_visibility":20,"bottleneck_pricing":10,"market_mispricing":35,"valuation_rerating":15,"capital_allocation":20,"information_confidence":90},"weighted_total":35.2,"profile_scope":"C05_shadow_only","production_scoring_changed":false,"shadow_weight_only":true},"trigger_outcome_label":"hard_4c_with_later_partial_rebound","source_proxy_only":false,"evidence_url_pending":false,"narrative_only":false}
{"source_row_type":"v12_trigger_row","research_file":"e2r_stock_web_v12_residual_round_R1_loop_199_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C05_EPC_MEGA_CONTRACT_MARGIN_GAP_research.md","selected_round":"R1","selected_loop":199,"large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP","fine_archetype_id":"EPC_MARGIN_GAP_4C_TIMING_DIRECT_URL_REPAIR","case_id":"C05_GS_BUSINESS_SUSPENSION_OFFSET_4B","symbol":"006360","company_name":"GS E&C","evidence_date":"2024-02-01","entry_date":"2024-02-01","entry_price":15690.0,"trigger_type":"Stage4B","case_role":"counterexample_guardrail","fine_case_role":"regulatory_penalty_with_order_backlog_offset","hard_duplicate_key":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP|006360|Stage4B|2024-02-01","evidence_source_class":"direct_url","evidence_urls":["https://www.koreatimes.co.kr/www/biz/2024/02/126_367620.html"],"evidence_summary":"A regulatory and litigation overhang remained visible, including suspension risk and loss of brand/order trust. The later stock-web path rebounded, so the event should remain local 4B unless fresh order/backlog collapse or cash-liquidity break is confirmed.","price_source_validation":{"primary_price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","manifest_max_date":"2026-02-20","schema_columns":"d,o,h,l,c,v,a,mc,s,m","shard_paths":["atlas/ohlcv_tradable_by_symbol_year/006/006360/2024.csv"],"profile_checked":true,"corporate_action_contaminated_D_to_D_plus_180":false,"insufficient_forward_window_180D":false,"calibration_usable":true},"actual_entry_ohlc":{"d":"2024-02-01","c":15690.0},"price_path":{"mfe_30d_pct":3.44,"mae_30d_pct":-6.05,"mfe_90d_pct":6.56,"mae_90d_pct":-10.52,"mfe_180d_pct":38.62,"mae_180d_pct":-10.52,"peak_180d_date":"2024-08-27","trough_180d_date":"2024-04-19","rows_180d_inclusive":181},"stage_evidence":{"stage2_fields":["existing backlog/order cycle still not fully erased"],"stage3_fields":[],"stage4b_fields":["business suspension","lawsuit/brand overhang","order trust damage"],"stage4c_fields":["hard 4C deferred without new backlog/cash collapse"]},"score_simulation":{"weights":{"eps_fcf_explosion":18,"earnings_visibility":22,"bottleneck_pricing":10,"market_mispricing":12,"valuation_rerating":10,"capital_allocation":8,"information_confidence":20},"raw_components":{"eps_fcf_explosion":35,"earnings_visibility":30,"bottleneck_pricing":20,"market_mispricing":50,"valuation_rerating":30,"capital_allocation":35,"information_confidence":85},"weighted_total":43.7,"profile_scope":"C05_shadow_only","production_scoring_changed":false,"shadow_weight_only":true},"trigger_outcome_label":"4b_regulatory_overhang_with_rebound","source_proxy_only":false,"evidence_url_pending":false,"narrative_only":false}
{"source_row_type":"v12_trigger_row","research_file":"e2r_stock_web_v12_residual_round_R1_loop_199_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C05_EPC_MEGA_CONTRACT_MARGIN_GAP_research.md","selected_round":"R1","selected_loop":199,"large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP","fine_archetype_id":"EPC_MARGIN_GAP_4C_TIMING_DIRECT_URL_REPAIR","case_id":"C05_GS_FADHILI_EPC_ORDER_STAGE2A","symbol":"006360","company_name":"GS E&C","evidence_date":"2024-04-02","entry_date":"2024-04-03","entry_price":15630.0,"trigger_type":"Stage2-Actionable","case_role":"positive_control","fine_case_role":"mega_gas_epc_order_with_margin_phasing_required","hard_duplicate_key":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP|006360|Stage2-Actionable|2024-04-03","evidence_source_class":"direct_url","evidence_urls":["https://www.reuters.com/business/energy/saudi-aramco-awards-77-bln-contracts-expand-fadhili-gas-plant-2024-04-02/"],"evidence_summary":"The order evidence is direct and customer-specific, not a generic EPC rumor. It supports Stage2-Actionable, but Stage3/Green still require margin recognition, working-capital discipline, and execution-cost control because C05 failures often hide inside cost-rate drift.","price_source_validation":{"primary_price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","manifest_max_date":"2026-02-20","schema_columns":"d,o,h,l,c,v,a,mc,s,m","shard_paths":["atlas/ohlcv_tradable_by_symbol_year/006/006360/2024.csv"],"profile_checked":true,"corporate_action_contaminated_D_to_D_plus_180":false,"insufficient_forward_window_180D":false,"calibration_usable":true},"actual_entry_ohlc":{"d":"2024-04-03","c":15630.0},"price_path":{"mfe_30d_pct":6.97,"mae_30d_pct":-10.17,"mfe_90d_pct":30.52,"mae_90d_pct":-10.17,"mfe_180d_pct":39.16,"mae_180d_pct":-10.17,"peak_180d_date":"2024-08-27","trough_180d_date":"2024-04-19","rows_180d_inclusive":181},"stage_evidence":{"stage2_fields":["customer-specific mega EPC award","gas-plant expansion project","visible backlog addition"],"stage3_fields":["needs later margin and working-capital proof"],"stage4b_fields":[],"stage4c_fields":[]},"score_simulation":{"weights":{"eps_fcf_explosion":18,"earnings_visibility":22,"bottleneck_pricing":10,"market_mispricing":12,"valuation_rerating":10,"capital_allocation":8,"information_confidence":20},"raw_components":{"eps_fcf_explosion":75,"earnings_visibility":82,"bottleneck_pricing":55,"market_mispricing":55,"valuation_rerating":50,"capital_allocation":60,"information_confidence":92},"weighted_total":71.84,"profile_scope":"C05_shadow_only","production_scoring_changed":false,"shadow_weight_only":true},"trigger_outcome_label":"stage2a_order_positive_control","source_proxy_only":false,"evidence_url_pending":false,"narrative_only":false}
{"source_row_type":"v12_trigger_row","research_file":"e2r_stock_web_v12_residual_round_R1_loop_199_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C05_EPC_MEGA_CONTRACT_MARGIN_GAP_research.md","selected_round":"R1","selected_loop":199,"large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP","fine_archetype_id":"EPC_MARGIN_GAP_4C_TIMING_DIRECT_URL_REPAIR","case_id":"C05_SAMSUNG_ENA_FADHILI_ORDER_HIGH_MAE_STAGE2A","symbol":"028050","company_name":"Samsung E&A","evidence_date":"2024-04-02","entry_date":"2024-04-03","entry_price":25300.0,"trigger_type":"Stage2-Actionable","case_role":"positive_control_high_mae","fine_case_role":"direct_order_positive_with_execution_mae","hard_duplicate_key":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP|028050|Stage2-Actionable|2024-04-03","evidence_source_class":"direct_url","evidence_urls":["https://www.reuters.com/business/energy/saudi-aramco-awards-77-bln-contracts-expand-fadhili-gas-plant-2024-04-02/"],"evidence_summary":"Direct project-award evidence supports Stage2-Actionable. The 180D MAE of -35.57% shows why C05 direct-order positives need Green brakes until backlog conversion and margin are visible; order alone is a bridge, not the finished bridge deck.","price_source_validation":{"primary_price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","manifest_max_date":"2026-02-20","schema_columns":"d,o,h,l,c,v,a,mc,s,m","shard_paths":["atlas/ohlcv_tradable_by_symbol_year/028/028050/2024.csv"],"profile_checked":true,"corporate_action_contaminated_D_to_D_plus_180":false,"insufficient_forward_window_180D":false,"calibration_usable":true},"actual_entry_ohlc":{"d":"2024-04-03","c":25300.0},"price_path":{"mfe_30d_pct":6.72,"mae_30d_pct":-5.93,"mfe_90d_pct":15.81,"mae_90d_pct":-14.62,"mfe_180d_pct":15.81,"mae_180d_pct":-35.57,"peak_180d_date":"2024-07-30","trough_180d_date":"2024-12-09","rows_180d_inclusive":181},"stage_evidence":{"stage2_fields":["direct customer order","backlog expansion candidate"],"stage3_fields":["requires execution margin phasing"],"stage4b_fields":["high-MAE execution/valuation risk"],"stage4c_fields":[]},"score_simulation":{"weights":{"eps_fcf_explosion":18,"earnings_visibility":22,"bottleneck_pricing":10,"market_mispricing":12,"valuation_rerating":10,"capital_allocation":8,"information_confidence":20},"raw_components":{"eps_fcf_explosion":72,"earnings_visibility":80,"bottleneck_pricing":50,"market_mispricing":45,"valuation_rerating":45,"capital_allocation":55,"information_confidence":92},"weighted_total":68.26,"profile_scope":"C05_shadow_only","production_scoring_changed":false,"shadow_weight_only":true},"trigger_outcome_label":"positive_order_high_mae_control","source_proxy_only":false,"evidence_url_pending":false,"narrative_only":false}
{"source_row_type":"v12_trigger_row","research_file":"e2r_stock_web_v12_residual_round_R1_loop_199_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C05_EPC_MEGA_CONTRACT_MARGIN_GAP_research.md","selected_round":"R1","selected_loop":199,"large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP","fine_archetype_id":"EPC_MARGIN_GAP_4C_TIMING_DIRECT_URL_REPAIR","case_id":"C05_SAMSUNG_ENA_Q2_BACKLOG_LATE_EXTENSION_4B","symbol":"028050","company_name":"Samsung E&A","evidence_date":"2024-07-25","entry_date":"2024-07-26","entry_price":27900.0,"trigger_type":"Stage4B","case_role":"counterexample_guardrail","fine_case_role":"late_backlog_extension_after_order_rerating","hard_duplicate_key":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP|028050|Stage4B|2024-07-26","evidence_source_class":"direct_url","evidence_urls":["https://www.samsungena.com/en/about-us/media-center/news/detail/2024-07-25-samsung-e-a-announces-2q-2024-financial-results"],"evidence_summary":"2Q24 had strong backlog and order visibility, so this is not a hard 4C. But the entry came after the order narrative had already been priced, and stock-web shows 180D MFE only 5.02% vs MAE -41.58%; this is a late-extension 4B / Green blocker row.","price_source_validation":{"primary_price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","manifest_max_date":"2026-02-20","schema_columns":"d,o,h,l,c,v,a,mc,s,m","shard_paths":["atlas/ohlcv_tradable_by_symbol_year/028/028050/2024.csv"],"profile_checked":true,"corporate_action_contaminated_D_to_D_plus_180":false,"insufficient_forward_window_180D":false,"calibration_usable":true},"actual_entry_ohlc":{"d":"2024-07-26","c":27900.0},"price_path":{"mfe_30d_pct":5.02,"mae_30d_pct":-16.85,"mfe_90d_pct":5.02,"mae_90d_pct":-41.58,"mfe_180d_pct":5.02,"mae_180d_pct":-41.58,"peak_180d_date":"2024-07-30","trough_180d_date":"2024-12-09","rows_180d_inclusive":181},"stage_evidence":{"stage2_fields":["large backlog","new orders visibility"],"stage3_fields":["execution margin bridge not enough to offset late entry"],"stage4b_fields":["late extension","price validation failed after small MFE","high 180D MAE"],"stage4c_fields":["no hard thesis break because backlog remains visible"]},"score_simulation":{"weights":{"eps_fcf_explosion":18,"earnings_visibility":22,"bottleneck_pricing":10,"market_mispricing":12,"valuation_rerating":10,"capital_allocation":8,"information_confidence":20},"raw_components":{"eps_fcf_explosion":58,"earnings_visibility":78,"bottleneck_pricing":45,"market_mispricing":25,"valuation_rerating":25,"capital_allocation":50,"information_confidence":90},"weighted_total":59.6,"profile_scope":"C05_shadow_only","production_scoring_changed":false,"shadow_weight_only":true},"trigger_outcome_label":"late_backlog_extension_4b","source_proxy_only":false,"evidence_url_pending":false,"narrative_only":false}
{"source_row_type":"v12_trigger_row","research_file":"e2r_stock_web_v12_residual_round_R1_loop_199_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C05_EPC_MEGA_CONTRACT_MARGIN_GAP_research.md","selected_round":"R1","selected_loop":199,"large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP","fine_archetype_id":"EPC_MARGIN_GAP_4C_TIMING_DIRECT_URL_REPAIR","case_id":"C05_HYUNDAI_ENC_Q3_COST_RATE_OFFSET_4B","symbol":"000720","company_name":"Hyundai E&C","evidence_date":"2024-10-23","entry_date":"2024-10-23","entry_price":28500.0,"trigger_type":"Stage4B","case_role":"counterexample_guardrail","fine_case_role":"cost_rate_shock_with_future_project_offset","hard_duplicate_key":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP|000720|Stage4B|2024-10-23","evidence_source_class":"direct_url","evidence_urls":["https://www.mk.co.kr/en/stock/11147947"],"evidence_summary":"The cost-rate shock is genuine non-price 4B evidence. Yet the later stock-web path was extremely positive, showing that temporary cost-rate damage should not be upgraded to hard 4C if overseas/new-project offsets remain alive.","price_source_validation":{"primary_price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","manifest_max_date":"2026-02-20","schema_columns":"d,o,h,l,c,v,a,mc,s,m","shard_paths":["atlas/ohlcv_tradable_by_symbol_year/000/000720/2024.csv","atlas/ohlcv_tradable_by_symbol_year/000/000720/2025.csv"],"profile_checked":true,"corporate_action_contaminated_D_to_D_plus_180":false,"insufficient_forward_window_180D":false,"calibration_usable":true},"actual_entry_ohlc":{"d":"2024-10-23","c":28500.0},"price_path":{"mfe_30d_pct":4.04,"mae_30d_pct":-7.19,"mfe_90d_pct":31.75,"mae_90d_pct":-15.44,"mfe_180d_pct":198.6,"mae_180d_pct":-15.44,"peak_180d_date":"2025-06-25","trough_180d_date":"2024-12-09","rows_180d_inclusive":181},"stage_evidence":{"stage2_fields":["order/backlog cycle not invalidated"],"stage3_fields":["requires future cost-rate normalization"],"stage4b_fields":["domestic cost ratio pressure","overseas one-off cost","profit decline"],"stage4c_fields":["hard 4C deferred because order-cycle and project offsets are not broken"]},"score_simulation":{"weights":{"eps_fcf_explosion":18,"earnings_visibility":22,"bottleneck_pricing":10,"market_mispricing":12,"valuation_rerating":10,"capital_allocation":8,"information_confidence":20},"raw_components":{"eps_fcf_explosion":48,"earnings_visibility":45,"bottleneck_pricing":35,"market_mispricing":45,"valuation_rerating":35,"capital_allocation":45,"information_confidence":88},"weighted_total":52.14,"profile_scope":"C05_shadow_only","production_scoring_changed":false,"shadow_weight_only":true},"trigger_outcome_label":"4b_cost_rate_shock_with_rebound","source_proxy_only":false,"evidence_url_pending":false,"narrative_only":false}
{"source_row_type":"v12_trigger_row","research_file":"e2r_stock_web_v12_residual_round_R1_loop_199_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C05_EPC_MEGA_CONTRACT_MARGIN_GAP_research.md","selected_round":"R1","selected_loop":199,"large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP","fine_archetype_id":"EPC_MARGIN_GAP_4C_TIMING_DIRECT_URL_REPAIR","case_id":"C05_HYUNDAI_ENC_OVERSEAS_SITE_LOSS_OFFSET_4B","symbol":"000720","company_name":"Hyundai E&C","evidence_date":"2025-01-21","entry_date":"2025-01-21","entry_price":26100.0,"trigger_type":"Stage4B","case_role":"positive_control_overhard_4c_false_positive","fine_case_role":"overseas_site_loss_with_bad_mix_rolloff_offset","hard_duplicate_key":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP|000720|Stage4B|2025-01-21","evidence_source_class":"direct_url","evidence_urls":["https://view.asiae.co.kr/article/2025012108300867498"],"evidence_summary":"The news flow still contained overseas-site and low-margin mix concerns. But explicit mix rolloff / completion timing provided an offset bridge, and stock-web forward path validated that this was not a hard 4C. This is a strong C05 overhard-4C repair row.","price_source_validation":{"primary_price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","manifest_max_date":"2026-02-20","schema_columns":"d,o,h,l,c,v,a,mc,s,m","shard_paths":["atlas/ohlcv_tradable_by_symbol_year/000/000720/2025.csv"],"profile_checked":true,"corporate_action_contaminated_D_to_D_plus_180":false,"insufficient_forward_window_180D":false,"calibration_usable":true},"actual_entry_ohlc":{"d":"2025-01-21","c":26100.0},"price_path":{"mfe_30d_pct":43.87,"mae_30d_pct":-0.96,"mfe_90d_pct":183.52,"mae_90d_pct":-0.96,"mfe_180d_pct":226.05,"mae_180d_pct":-0.96,"peak_180d_date":"2025-06-25","trough_180d_date":"2025-01-21","rows_180d_inclusive":181},"stage_evidence":{"stage2_fields":["future cost-rate normalization bridge","bad-mix share decline"],"stage3_fields":["price validation very strong but Green should require direct margin normalization evidence"],"stage4b_fields":["overseas site loss","low-margin site completion risk"],"stage4c_fields":["hard 4C blocked by explicit cost-rate offset bridge"]},"score_simulation":{"weights":{"eps_fcf_explosion":18,"earnings_visibility":22,"bottleneck_pricing":10,"market_mispricing":12,"valuation_rerating":10,"capital_allocation":8,"information_confidence":20},"raw_components":{"eps_fcf_explosion":58,"earnings_visibility":60,"bottleneck_pricing":35,"market_mispricing":60,"valuation_rerating":55,"capital_allocation":55,"information_confidence":86},"weighted_total":61.44,"profile_scope":"C05_shadow_only","production_scoring_changed":false,"shadow_weight_only":true},"trigger_outcome_label":"overhard_4c_false_positive_repair","source_proxy_only":false,"evidence_url_pending":false,"narrative_only":false}
{"source_row_type":"v12_trigger_row","research_file":"e2r_stock_web_v12_residual_round_R1_loop_199_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C05_EPC_MEGA_CONTRACT_MARGIN_GAP_research.md","selected_round":"R1","selected_loop":199,"large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP","fine_archetype_id":"EPC_MARGIN_GAP_4C_TIMING_DIRECT_URL_REPAIR","case_id":"C05_DLENC_Q3_COST_RATE_RECOVERY_STAGE2A","symbol":"375500","company_name":"DL E&C","evidence_date":"2024-10-31","entry_date":"2024-10-31","entry_price":30900.0,"trigger_type":"Stage2-Actionable","case_role":"positive_control","fine_case_role":"cost_rate_recovery_and_selective_order_strategy","hard_duplicate_key":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP|375500|Stage2-Actionable|2024-10-31","evidence_source_class":"direct_url","evidence_urls":["https://www.dlenc.co.kr/eng/pr/NewsView.do?cd_mnu=EU03010000&idx=31032"],"evidence_summary":"This is a clean positive C05 repair row: the evidence explicitly connects profitability to cost-rate improvement and high-profit order strategy. The forward path validates Stage2-Actionable while keeping Green gated until cash conversion and backlog quality are confirmed.","price_source_validation":{"primary_price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","manifest_max_date":"2026-02-20","schema_columns":"d,o,h,l,c,v,a,mc,s,m","shard_paths":["atlas/ohlcv_tradable_by_symbol_year/375/375500/2024.csv","atlas/ohlcv_tradable_by_symbol_year/375/375500/2025.csv"],"profile_checked":true,"corporate_action_contaminated_D_to_D_plus_180":false,"insufficient_forward_window_180D":false,"calibration_usable":true},"actual_entry_ohlc":{"d":"2024-10-31","c":30900.0},"price_path":{"mfe_30d_pct":12.62,"mae_30d_pct":-5.18,"mfe_90d_pct":51.94,"mae_90d_pct":-5.18,"mfe_180d_pct":93.2,"mae_180d_pct":-5.18,"peak_180d_date":"2025-06-26","trough_180d_date":"2024-11-13","rows_180d_inclusive":181},"stage_evidence":{"stage2_fields":["improved cost ratio","selective high-profit order strategy","operating-profit recovery"],"stage3_fields":["needs cash conversion / working-capital follow-through"],"stage4b_fields":[],"stage4c_fields":[]},"score_simulation":{"weights":{"eps_fcf_explosion":18,"earnings_visibility":22,"bottleneck_pricing":10,"market_mispricing":12,"valuation_rerating":10,"capital_allocation":8,"information_confidence":20},"raw_components":{"eps_fcf_explosion":78,"earnings_visibility":85,"bottleneck_pricing":55,"market_mispricing":55,"valuation_rerating":50,"capital_allocation":65,"information_confidence":90},"weighted_total":73.04,"profile_scope":"C05_shadow_only","production_scoring_changed":false,"shadow_weight_only":true},"trigger_outcome_label":"stage2a_cost_rate_recovery_positive_control","source_proxy_only":false,"evidence_url_pending":false,"narrative_only":false}
{"source_row_type":"v12_trigger_row","research_file":"e2r_stock_web_v12_residual_round_R1_loop_199_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C05_EPC_MEGA_CONTRACT_MARGIN_GAP_research.md","selected_round":"R1","selected_loop":199,"large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP","fine_archetype_id":"EPC_MARGIN_GAP_4C_TIMING_DIRECT_URL_REPAIR","case_id":"C05_DAEWOO_2023_BACKLOG_COST_BURDEN_STAGE2","symbol":"047040","company_name":"Daewoo E&C","evidence_date":"2024-01-30","entry_date":"2024-01-30","entry_price":4065.0,"trigger_type":"Stage2","case_role":"mixed_guardrail","fine_case_role":"backlog_large_but_housing_cost_burden","hard_duplicate_key":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP|047040|Stage2|2024-01-30","evidence_source_class":"direct_url","evidence_urls":["https://view.asiae.co.kr/article/2024013011184560726"],"evidence_summary":"The row separates backlog quantity from margin quality. New orders and backlog were visible, but housing cost burden kept it at Stage2 rather than Stage2-Actionable/Yellow. The later 180D upside was positive, but the initial 90D path had little upside and meaningful drawdown.","price_source_validation":{"primary_price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","manifest_max_date":"2026-02-20","schema_columns":"d,o,h,l,c,v,a,mc,s,m","shard_paths":["atlas/ohlcv_tradable_by_symbol_year/047/047040/2024.csv"],"profile_checked":true,"corporate_action_contaminated_D_to_D_plus_180":false,"insufficient_forward_window_180D":false,"calibration_usable":true},"actual_entry_ohlc":{"d":"2024-01-30","c":4065.0},"price_path":{"mfe_30d_pct":2.83,"mae_30d_pct":-10.82,"mfe_90d_pct":2.83,"mae_90d_pct":-11.93,"mfe_180d_pct":22.14,"mae_180d_pct":-12.79,"peak_180d_date":"2024-07-18","trough_180d_date":"2024-08-05","rows_180d_inclusive":181},"stage_evidence":{"stage2_fields":["large order backlog","new orders above target"],"stage3_fields":["not enough margin/FCF bridge"],"stage4b_fields":["housing cost burden","OP decline"],"stage4c_fields":["hard 4C blocked by backlog/order visibility"]},"score_simulation":{"weights":{"eps_fcf_explosion":18,"earnings_visibility":22,"bottleneck_pricing":10,"market_mispricing":12,"valuation_rerating":10,"capital_allocation":8,"information_confidence":20},"raw_components":{"eps_fcf_explosion":52,"earnings_visibility":62,"bottleneck_pricing":30,"market_mispricing":45,"valuation_rerating":40,"capital_allocation":45,"information_confidence":85},"weighted_total":56.0,"profile_scope":"C05_shadow_only","production_scoring_changed":false,"shadow_weight_only":true},"trigger_outcome_label":"backlog_quantity_stage2_not_actionable","source_proxy_only":false,"evidence_url_pending":false,"narrative_only":false}
{"source_row_type":"v12_trigger_row","research_file":"e2r_stock_web_v12_residual_round_R1_loop_199_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C05_EPC_MEGA_CONTRACT_MARGIN_GAP_research.md","selected_round":"R1","selected_loop":199,"large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP","fine_archetype_id":"EPC_MARGIN_GAP_4C_TIMING_DIRECT_URL_REPAIR","case_id":"C05_DAEWOO_Q1_IMPROVED_HOUSING_PLANT_STAGE2A","symbol":"047040","company_name":"Daewoo E&C","evidence_date":"2025-04-29","entry_date":"2025-04-29","entry_price":3520.0,"trigger_type":"Stage2-Actionable","case_role":"positive_control","fine_case_role":"housing_and_plant_profit_recovery_backlog_confirmation","hard_duplicate_key":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP|047040|Stage2-Actionable|2025-04-29","evidence_source_class":"direct_url","evidence_urls":["https://en.yna.co.kr/view/AEN20250429003300320"],"evidence_summary":"Unlike generic backlog language, this row has explicit profitability improvement plus order/backlog support. The stock-web path validates Stage2-Actionable; the rule lesson is that C05 can be upgraded when cost-rate improvement is tied to business-line profit recovery, not merely order volume.","price_source_validation":{"primary_price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","manifest_max_date":"2026-02-20","schema_columns":"d,o,h,l,c,v,a,mc,s,m","shard_paths":["atlas/ohlcv_tradable_by_symbol_year/047/047040/2025.csv","atlas/ohlcv_tradable_by_symbol_year/047/047040/2026.csv"],"profile_checked":true,"corporate_action_contaminated_D_to_D_plus_180":false,"insufficient_forward_window_180D":false,"calibration_usable":true},"actual_entry_ohlc":{"d":"2025-04-29","c":3520.0},"price_path":{"mfe_30d_pct":36.51,"mae_30d_pct":-3.12,"mfe_90d_pct":36.51,"mae_90d_pct":-3.12,"mfe_180d_pct":63.64,"mae_180d_pct":-5.68,"peak_180d_date":"2026-01-23","trough_180d_date":"2025-11-07","rows_180d_inclusive":181},"stage_evidence":{"stage2_fields":["profitability improvement","new orders growth","large backlog"],"stage3_fields":["needs multi-quarter cost-rate confirmation for Green"],"stage4b_fields":[],"stage4c_fields":[]},"score_simulation":{"weights":{"eps_fcf_explosion":18,"earnings_visibility":22,"bottleneck_pricing":10,"market_mispricing":12,"valuation_rerating":10,"capital_allocation":8,"information_confidence":20},"raw_components":{"eps_fcf_explosion":80,"earnings_visibility":80,"bottleneck_pricing":50,"market_mispricing":50,"valuation_rerating":45,"capital_allocation":60,"information_confidence":88},"weighted_total":69.9,"profile_scope":"C05_shadow_only","production_scoring_changed":false,"shadow_weight_only":true},"trigger_outcome_label":"stage2a_margin_recovery_positive_control","source_proxy_only":false,"evidence_url_pending":false,"narrative_only":false}
```

## 9. Deferred coding-agent handoff prompt

```text
handoff_prompt_executed_now: false

If promoted later, add a C05 scoped shadow gate that separates:
1) direct customer/order/backlog bridge,
2) margin/cost-rate/working-capital bridge,
3) explicit offset quality,
4) irreversible non-price 4C thesis break.
Do not loosen Stage3-Green globally. Do not change production scoring from this MD alone.
```

## 10. Next Round State

```yaml
next_round_state:
  previous_round: R1
  previous_loop: 199
  completed_large_sector_id: L1_INDUSTRIALS_INFRA_DEFENSE_GRID
  completed_canonical_archetype_id: C05_EPC_MEGA_CONTRACT_MARGIN_GAP
  completed_fine_archetype_id: EPC_MARGIN_GAP_4C_TIMING_DIRECT_URL_REPAIR
  completion_status: completed
  production_scoring_changed: false
  shadow_weight_only: true
  next_recommended_archetypes:
    - C01_ORDER_BACKLOG_MARGIN_BRIDGE_FCF_COUNTEREXAMPLE_REPAIR
    - C13_BATTERY_JV_UTILIZATION_AMPC_IRA_OFFSET_QUALITY_REPAIR
    - C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE_SUPPLIER_ORDER_CONVERSION_REPAIR
    - R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL_HOLDOUT_REFRESH
    - C05_EPC_MEGA_CONTRACT_MARGIN_GAP_WORKING_CAPITAL_CASH_CONVERSION_REPAIR
```
