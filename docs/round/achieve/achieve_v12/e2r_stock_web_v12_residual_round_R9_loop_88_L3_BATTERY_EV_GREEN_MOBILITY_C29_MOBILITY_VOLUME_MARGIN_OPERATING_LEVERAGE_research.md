---
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
scheduled_round: R9
scheduled_loop: 88
completed_round: R9
completed_loop: 88
next_round: R10
next_loop: 88
round_schedule_status: valid
round_sector_consistency: pass
large_sector_id: L3_BATTERY_EV_GREEN_MOBILITY
canonical_archetype_id: C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE
fine_archetype_id: AUTO_PARTS_TIRE_ELECTRONICS_VOLUME_MARGIN_BRIDGE_VS_GENERIC_MOBILITY_BETA
output_file: e2r_stock_web_v12_residual_round_R9_loop_88_L3_BATTERY_EV_GREEN_MOBILITY_C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE_research.md
price_data_source: Songdaiki/stock-web
upstream_source: FinanceData/marcap
price_basis: tradable_raw
price_adjustment_status: raw_unadjusted_marcap
stock_web_manifest_max_date: 2026-02-20
production_scoring_changed: false
shadow_weight_only: true
handoff_prompt_embedded: true
handoff_prompt_executed_now: false
---

# E2R Stock-Web v12 Residual Research — R9 Loop 88 — C29 Mobility Volume/Margin Operating Leverage

## 1. Executive summary

This R9 loop continues the sequential v12 round scheduler after `R8 / loop 88`. R9 allows mobility/transport-oriented residual work under `L3_BATTERY_EV_GREEN_MOBILITY`, so this file uses `C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE`.

The loop avoids the R9 loop87 symbols already created in this session (`064960`, `005850`, `204320`) and avoids the dominant No-Repeat C29 congestion names visible in the index (`011210`, `000270`, `005380`, `005850`, `010690`, `018880`). It instead tests a second cluster of mobility/auto-parts exposure:

- `002350` Nexen Tire / tire operating leverage positive-with-local-4B case.
- `009900` Myoung Shin Industry / EV body supplier generic beta false-positive case.
- `012860` Mobase Electronics / auto-electronics theme-spike high-MAE counterexample.

Core residual finding:

```text
C29 should not treat generic auto-parts / EV supplier / mobility beta as Stage2-Actionable unless there is a visible volume, mix, margin, and earnings bridge.

Tire/parts names can produce sharp MFE from beta and theme flow, but if the evidence is price-only or revenue-line-only without margin bridge, the path tends to become local-4B watch or high-MAE false positive.
```

No global scoring change is proposed. This loop adds C29-specific residual evidence only.

```text
new_independent_case_count = 3
reused_case_count = 0
same_archetype_new_symbol_count = 3
positive_case_count = 1
counterexample_count = 2
local_4b_overlay_case_count = 2
calibration_usable_trigger_count = 3
do_not_propose_new_weight_delta = true
```

---

## 2. Price source validation

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","source_name":"FinanceData/marcap","validation_status":"usable_for_historical_calibration_with_batch_recalc_recommended"}
```

The stock-web manifest used in this loop reports:

| field | value |
|---|---:|
| min_date | 1995-05-02 |
| max_date | 2026-02-20 |
| tradable_row_count | 14,354,401 |
| raw_row_count | 15,214,118 |
| symbol_count | 5,414 |
| calibration_shard_root | atlas/ohlcv_tradable_by_symbol_year |
| raw_shard_root | atlas/ohlcv_raw_by_symbol_year |
| price_adjustment_status | raw_unadjusted_marcap |

Caveat: these OHLC rows are raw/unadjusted. Corporate-action contaminated 180D windows are blocked. The selected 2024 entry windows for `002350`, `009900`, and `012860` do not overlap the symbol profile corporate-action candidate dates.

---

## 3. No-Repeat / novelty check

Hard duplicate key used:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

C29 is already a heavily populated archetype. The No-Repeat Index snapshot shows:

```text
C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | 60 rows | 27 symbols | date range 2021-01-08~2024-08-26 | positive/counterexample 26/13 | 4B/4C 6/0 | top repeats: 011210(7), 000270(5), 005380(5), 005850(5), 010690(5), 018880(3)
```

Therefore this loop avoids:

```text
011210, 000270, 005380, 005850, 010690, 018880
```

It also avoids the immediately previous C29 R9 loop87 local-session symbols:

```text
064960, 005850, 204320
```

Selected symbols:

| symbol | company_name | duplicate status | reason selected |
|---|---|---|---|
| 002350 | 넥센타이어 | new in this local C29 loop | Tire margin/volume bridge; positive with local 4B risk. |
| 009900 | 명신산업 | new in this local C29 loop | EV supplier beta; persistent high-MAE false-positive path. |
| 012860 | 모베이스전자 | new in this local C29 loop | Auto-electronics theme spike; high-MAE theme fade counterexample. |

A candidate such as `007340` was inspected but not used as a calibration row because its profile includes a 2024-10-08 corporate-action candidate, which would contaminate many otherwise tempting 2024 forward windows.

---

## 4. Selected symbol profiles

| symbol | profile_path | profile status | corporate action status | calibration note |
|---|---|---|---|---|
| 002350 | atlas/symbol_profiles/002/002350.json | active_like | CA candidates old: 1999/2008 only | 2024 trigger windows clean. |
| 009900 | atlas/symbol_profiles/009/009900.json | active_like | CA candidate 2021-06-18 only | 2024 trigger windows clean. |
| 012860 | atlas/symbol_profiles/012/012860.json | active_like | CA candidates through 2020 only | 2024 trigger windows clean. |

---

## 5. Case grid

| case_id | symbol | company | trigger_type | trigger_date | entry_date | entry_price | case verdict |
|---|---|---|---|---|---|---:|---|
| C29_R9L88_002350_TIRE_MARGIN_POSITIVE_4B | 002350 | 넥센타이어 | Stage2-Actionable | 2024-01-24 | 2024-01-24 | 7700 | positive with local 4B watch |
| C29_R9L88_009900_EV_SUPPLIER_FALSE_POSITIVE | 009900 | 명신산업 | Stage2-FalsePositive-Candidate | 2024-02-02 | 2024-02-02 | 17440 | counterexample |
| C29_R9L88_012860_AUTO_ELECTRONICS_THEME_FADE | 012860 | 모베이스전자 | Stage2-FalsePositive-Candidate | 2024-02-05 | 2024-02-05 | 2100 | counterexample with local theme spike |

---

## 6. Price path backtest summary

The following MFE/MAE values are calculated from stock-web raw/unadjusted daily OHLC rows. Values are approximate to one decimal point and should be batch-recomputed from the CSV shards before promotion.

| trigger_id | entry | MFE_30D | MAE_30D | MFE_90D | MAE_90D | MFE_180D | MAE_180D | peak_date | peak_price | drawdown_after_peak | notes |
|---|---:|---:|---:|---:|---:|---:|---:|---|---:|---:|---|
| C29_R9L88_TRG_002350_S2 | 7700 | +25.3% | -1.9% | +25.3% | -1.9% | +25.3% | -12.3% | 2024-02-26 | 9650 | -30.1% | Positive control, but local 4B watch after fast tire rerating. |
| C29_R9L88_TRG_009900_FP | 17440 | +1.6% | -13.3% | +1.6% | -19.9% | +1.6% | -39.8% | 2024-02-05 | 17720 | -40.7% | EV supplier beta failed without margin/order bridge. |
| C29_R9L88_TRG_012860_FP | 2100 | +13.8% | -15.2% | +13.8% | -15.2% | +13.8% | -30.2% | 2024-02-05 | 2390 | -38.7% | Intraday theme spike faded into high-MAE path. |

---

## 7. Current calibrated profile stress test

Current profile proxy assumptions:

```text
current_default_profile_proxy = e2r_2_1_stock_web_calibrated
stage2_actionable_evidence_bonus = +2.0
stage3_yellow_total_min = 75
stage3_green_total_min = 87
stage3_green_revision_min = 55
price_only_blowoff_blocks_positive_stage = true
full_4b_requires_non_price_evidence = true
hard_4c_thesis_break_routes_to_4c = true
```

Stress test result:

| case_id | current_profile_expected_judgment | price alignment | verdict |
|---|---|---|---|
| C29_R9L88_002350_TIRE_MARGIN_POSITIVE_4B | Stage2-Actionable allowed if tire margin/volume bridge exists | MFE strong, low 30D MAE, later drawdown | current profile broadly correct; local 4B watch needed |
| C29_R9L88_009900_EV_SUPPLIER_FALSE_POSITIVE | Generic EV supplier beta may be over-scored if relative strength gets too much credit | Weak MFE, very high MAE | current profile false-positive risk |
| C29_R9L88_012860_AUTO_ELECTRONICS_THEME_FADE | Auto-electronics theme spike may be over-scored if price/volume spike is mistaken for evidence | Intraday MFE but large drawdown | current profile false-positive risk |

Residual error type:

```text
C29 generic mobility beta false positive
C29 local 4B watch after rapid tire/parts MFE
C29 theme-spike without order/margin/revision bridge
```

---

## 8. Stage and 4B/4C interpretation

### Stage2 / Stage2-Actionable

C29 Stage2-Actionable should require at least two of the following non-price bridges:

```text
- OEM or customer volume visibility
- product mix / ASP bridge
- operating margin or EPS revision bridge
- repeatable supply chain role, not one-day theme flow
- inventory / utilization evidence that confirms demand conversion
```

### Stage3-Yellow / Stage3-Green

No Stage3-Green claim is proposed. `002350` shows a good MFE path, but the evidence remains source-proxy-only in this run. Promotion should wait for primary IR/DART evidence.

### 4B local vs full window

| trigger_id | local peak proximity | full-window peak proximity | evidence type | verdict |
|---|---:|---:|---|---|
| C29_R9L88_TRG_002350_S2 | 1.00 | 1.00 | price + sector proxy | local 4B watch only, not full 4B without non-price evidence |
| C29_R9L88_TRG_009900_FP | 1.00 | 1.00 | price-only / EV beta | false-positive guard, not 4B success |
| C29_R9L88_TRG_012860_FP | 1.00 | 1.00 | volume spike / theme | theme-spike 4B watch, not full 4B |

### 4C

```text
4C trigger count = 0
reason = no hard thesis-break trigger asserted; this loop is Stage2 false-positive / local 4B watch calibration.
```

---

## 9. Raw component score simulation

The score simulation is narrative-only and should be batch-recomputed before runtime use.

| case_id | raw component summary | P0 score/stage | proposed guard score/stage | alignment |
|---|---|---:|---:|---|
| C29_R9L88_002350_TIRE_MARGIN_POSITIVE_4B | tire recovery + margin beta + low initial MAE | 74 / Stage2-Actionable | 72 / Stage2-Actionable with local 4B watch | aligned |
| C29_R9L88_009900_EV_SUPPLIER_FALSE_POSITIVE | EV supplier beta + weak verified margin bridge | 69 / Stage2-Actionable | 58 / Stage1-Watch | guard improves alignment |
| C29_R9L88_012860_AUTO_ELECTRONICS_THEME_FADE | theme volume spike + weak order/revision bridge | 68 / Stage2-Actionable | 57 / Stage1-Watch | guard improves alignment |

```jsonl
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C29_R9L88_002350_TIRE_MARGIN_POSITIVE_4B","trigger_id":"C29_R9L88_TRG_002350_S2","symbol":"002350","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","raw_component_scores_before":{"volume_bridge_score":6,"margin_bridge_score":6,"revision_score":4,"relative_strength_score":7,"customer_quality_score":4,"valuation_repricing_score":5,"execution_risk_score":2},"weighted_score_before":74,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"volume_bridge_score":6,"margin_bridge_score":5,"revision_score":4,"relative_strength_score":6,"customer_quality_score":4,"valuation_repricing_score":5,"execution_risk_score":3},"weighted_score_after":72,"stage_label_after":"Stage2-Actionable-local-4B-watch","changed_components":["margin_bridge_score","relative_strength_score","execution_risk_score"],"component_delta_explanation":"Fast tire rerating remains actionable but needs local 4B watch after +20% MFE without new primary evidence.","MFE_90D_pct":25.3,"MAE_90D_pct":-1.9,"score_return_alignment_label":"aligned_with_4B_watch","current_profile_verdict":"current_profile_correct_with_watch"}
{"row_type":"score_simulation","profile_id":"C29_generic_beta_guard_profile","case_id":"C29_R9L88_009900_EV_SUPPLIER_FALSE_POSITIVE","trigger_id":"C29_R9L88_TRG_009900_FP","symbol":"009900","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","raw_component_scores_before":{"volume_bridge_score":3,"margin_bridge_score":2,"revision_score":1,"relative_strength_score":7,"customer_quality_score":4,"valuation_repricing_score":4,"execution_risk_score":4},"weighted_score_before":69,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"volume_bridge_score":2,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":4,"customer_quality_score":3,"valuation_repricing_score":3,"execution_risk_score":7},"weighted_score_after":58,"stage_label_after":"Stage1-Watch","changed_components":["volume_bridge_score","margin_bridge_score","revision_score","relative_strength_score","execution_risk_score"],"component_delta_explanation":"Generic EV supplier beta should not get actionable credit without verified order/margin/revision bridge.","MFE_90D_pct":1.6,"MAE_90D_pct":-19.9,"score_return_alignment_label":"proposed_guard_better","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"score_simulation","profile_id":"C29_theme_spike_guard_profile","case_id":"C29_R9L88_012860_AUTO_ELECTRONICS_THEME_FADE","trigger_id":"C29_R9L88_TRG_012860_FP","symbol":"012860","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","raw_component_scores_before":{"volume_bridge_score":3,"margin_bridge_score":1,"revision_score":1,"relative_strength_score":8,"customer_quality_score":3,"valuation_repricing_score":5,"execution_risk_score":5},"weighted_score_before":68,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"volume_bridge_score":1,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":4,"customer_quality_score":2,"valuation_repricing_score":3,"execution_risk_score":8},"weighted_score_after":57,"stage_label_after":"Stage1-Watch","changed_components":["volume_bridge_score","margin_bridge_score","revision_score","relative_strength_score","valuation_repricing_score","execution_risk_score"],"component_delta_explanation":"One-day electronics/auto theme volume spike fades unless followed by order, margin, or EPS revision evidence.","MFE_90D_pct":13.8,"MAE_90D_pct":-15.2,"score_return_alignment_label":"proposed_guard_better","current_profile_verdict":"current_profile_false_positive"}
```

---

## 10. Machine-readable case rows

```jsonl
{"row_type":"case","case_id":"C29_R9L88_002350_TIRE_MARGIN_POSITIVE_4B","symbol":"002350","company_name":"넥센타이어","round":"R9","loop":"88","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"AUTO_PARTS_TIRE_ELECTRONICS_VOLUME_MARGIN_BRIDGE_VS_GENERIC_MOBILITY_BETA","case_type":"structural_success_with_local_4B_watch","positive_or_counterexample":"positive","best_trigger":"C29_R9L88_TRG_002350_S2","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"aligned_with_local_4B_watch","current_profile_verdict":"current_profile_correct_with_watch","price_source":"Songdaiki/stock-web","notes":"source_proxy_only; primary DART/IR evidence URL required before promotion"}
{"row_type":"case","case_id":"C29_R9L88_009900_EV_SUPPLIER_FALSE_POSITIVE","symbol":"009900","company_name":"명신산업","round":"R9","loop":"88","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"AUTO_PARTS_TIRE_ELECTRONICS_VOLUME_MARGIN_BRIDGE_VS_GENERIC_MOBILITY_BETA","case_type":"failed_rerating","positive_or_counterexample":"counterexample","best_trigger":"C29_R9L88_TRG_009900_FP","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"weak_MFE_high_MAE_false_positive","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"generic EV supplier beta insufficient without margin/order bridge"}
{"row_type":"case","case_id":"C29_R9L88_012860_AUTO_ELECTRONICS_THEME_FADE","symbol":"012860","company_name":"모베이스전자","round":"R9","loop":"88","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"AUTO_PARTS_TIRE_ELECTRONICS_VOLUME_MARGIN_BRIDGE_VS_GENERIC_MOBILITY_BETA","case_type":"theme_spike_fade","positive_or_counterexample":"counterexample","best_trigger":"C29_R9L88_TRG_012860_FP","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"intraday_theme_MFE_high_MAE","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"volume spike should not become Stage2-Actionable without order/margin/revision evidence"}
```

---

## 11. Machine-readable trigger rows

```jsonl
{"row_type":"trigger","trigger_id":"C29_R9L88_TRG_002350_S2","case_id":"C29_R9L88_002350_TIRE_MARGIN_POSITIVE_4B","symbol":"002350","company_name":"넥센타이어","round":"R9","loop":"88","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"AUTO_PARTS_TIRE_ELECTRONICS_VOLUME_MARGIN_BRIDGE_VS_GENERIC_MOBILITY_BETA","sector":"mobility_tire_auto_parts","primary_archetype":"C29 tire margin/volume bridge","loop_objective":"coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test","trigger_type":"Stage2-Actionable","trigger_date":"2024-01-24","entry_date":"2024-01-24","entry_price":7700,"evidence_available_at_that_date":"source-proxy: tire recovery / mobility volume and margin beta; primary DART/IR URL pending","evidence_source":"source_proxy_pending_primary_url","stage2_evidence_fields":["volume_or_mix_route","margin_bridge_proxy","relative_strength"],"stage3_evidence_fields":["primary_margin_revision_pending"],"stage4b_evidence_fields":["rapid_price_MFE_watch"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/002/002350/2024.csv","profile_path":"atlas/symbol_profiles/002/002350.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":25.3,"MFE_90D_pct":25.3,"MFE_180D_pct":25.3,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-1.9,"MAE_90D_pct":-1.9,"MAE_180D_pct":-12.3,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-02-26","peak_price":9650,"drawdown_after_peak_pct":-30.1,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"local_4B_watch_only","four_b_evidence_type":["price_and_sector_proxy_only"],"four_c_protection_label":"not_applicable","trigger_outcome_label":"positive_with_local_4B_watch","current_profile_verdict":"current_profile_correct_with_watch","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C29_R9L88_002350_2024-01-24_7700","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"evidence_url_pending":true,"source_proxy_only":true,"batch_recalc_required":true}
{"row_type":"trigger","trigger_id":"C29_R9L88_TRG_009900_FP","case_id":"C29_R9L88_009900_EV_SUPPLIER_FALSE_POSITIVE","symbol":"009900","company_name":"명신산업","round":"R9","loop":"88","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"AUTO_PARTS_TIRE_ELECTRONICS_VOLUME_MARGIN_BRIDGE_VS_GENERIC_MOBILITY_BETA","sector":"mobility_ev_supplier","primary_archetype":"C29 generic EV supplier beta guard","loop_objective":"coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test","trigger_type":"Stage2-FalsePositive-Candidate","trigger_date":"2024-02-02","entry_date":"2024-02-02","entry_price":17440,"evidence_available_at_that_date":"source-proxy: EV supplier/theme beta without verified order/margin bridge; primary DART/IR URL pending","evidence_source":"source_proxy_pending_primary_url","stage2_evidence_fields":["relative_strength_proxy","customer_quality_pending"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["weak_MFE_high_MAE"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/009/009900/2024.csv","profile_path":"atlas/symbol_profiles/009/009900.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":1.6,"MFE_90D_pct":1.6,"MFE_180D_pct":1.6,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-13.3,"MAE_90D_pct":-19.9,"MAE_180D_pct":-39.8,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-02-05","peak_price":17720,"drawdown_after_peak_pct":-40.7,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"false_positive_guard_candidate","four_b_evidence_type":["price_only_or_theme_beta"],"four_c_protection_label":"not_applicable","trigger_outcome_label":"failed_rerating_generic_beta","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C29_R9L88_009900_2024-02-02_17440","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"evidence_url_pending":true,"source_proxy_only":true,"batch_recalc_required":true}
{"row_type":"trigger","trigger_id":"C29_R9L88_TRG_012860_FP","case_id":"C29_R9L88_012860_AUTO_ELECTRONICS_THEME_FADE","symbol":"012860","company_name":"모베이스전자","round":"R9","loop":"88","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"AUTO_PARTS_TIRE_ELECTRONICS_VOLUME_MARGIN_BRIDGE_VS_GENERIC_MOBILITY_BETA","sector":"mobility_auto_electronics","primary_archetype":"C29 auto-electronics theme spike guard","loop_objective":"coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test","trigger_type":"Stage2-FalsePositive-Candidate","trigger_date":"2024-02-05","entry_date":"2024-02-05","entry_price":2100,"evidence_available_at_that_date":"source-proxy: auto-electronics theme/volume spike without confirmed order, margin, or EPS revision bridge; primary DART/IR URL pending","evidence_source":"source_proxy_pending_primary_url","stage2_evidence_fields":["relative_strength_spike","volume_spike"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["theme_spike_local_peak"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/012/012860/2024.csv","profile_path":"atlas/symbol_profiles/012/012860.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":13.8,"MFE_90D_pct":13.8,"MFE_180D_pct":13.8,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-15.2,"MAE_90D_pct":-15.2,"MAE_180D_pct":-30.2,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-02-05","peak_price":2390,"drawdown_after_peak_pct":-38.7,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"theme_spike_4B_watch_only","four_b_evidence_type":["volume_spike_price_only"],"four_c_protection_label":"not_applicable","trigger_outcome_label":"theme_spike_fade_high_MAE","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C29_R9L88_012860_2024-02-05_2100","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"evidence_url_pending":true,"source_proxy_only":true,"batch_recalc_required":true}
```

---

## 12. Aggregate metric rows

```jsonl
{"row_type":"aggregate_metric","round":"R9","loop":"88","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"AUTO_PARTS_TIRE_ELECTRONICS_VOLUME_MARGIN_BRIDGE_VS_GENERIC_MOBILITY_BETA","eligible_trigger_count":3,"representative_trigger_count":3,"positive_case_count":1,"counterexample_count":2,"local_4b_overlay_case_count":2,"hard_4c_count":0,"avg_MFE_90D_pct":13.6,"avg_MAE_90D_pct":-12.3,"avg_MFE_180D_pct":13.6,"avg_MAE_180D_pct":-27.4,"current_profile_error_count":2,"false_positive_rate":0.667,"score_return_alignment":"guard_needed","source_proxy_only_count":3,"evidence_url_pending_count":3,"calibration_usable_count":3,"do_not_propose_new_weight_delta":true}
```

---

## 13. Shadow rule candidate

This loop does not propose a global scoring change. It proposes a C29-specific guard for future batch consideration only.

```jsonl
{"row_type":"shadow_weight","axis":"C29_generic_mobility_beta_guard","scope":"canonical_archetype","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","baseline_value":"generic auto/EV/mobility beta can contribute Stage2 credit if relative strength and theme evidence exist","tested_value":"require at least one verified volume/mix/margin/revision bridge before Stage2-Actionable; otherwise cap at Stage1-Watch or Stage2-Watch","delta":"conditional_guard_only","reason":"009900 and 012860 show weak/temporary MFE and high MAE when mobility beta is not accompanied by margin/order/revision evidence; 002350 shows positive path but requires local 4B watch after rapid tire rerating","backtest_effect":"reduces false-positive Stage2-Actionable rows while preserving tire margin positive as Stage2 with local 4B watch","trigger_ids":["C29_R9L88_TRG_002350_S2","C29_R9L88_TRG_009900_FP","C29_R9L88_TRG_012860_FP"],"calibration_usable_count":3,"new_independent_case_count":3,"counterexample_count":2,"confidence":"medium_low_until_primary_evidence_urls_resolved","proposal_type":"hold_for_more_evidence","notes":"source_proxy_only; do not promote until primary evidence URLs are attached and batch OHLC recalc passes"}
```

---

## 14. Residual contribution summary

```jsonl
{"row_type":"residual_contribution","round":"R9","loop":"88","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"AUTO_PARTS_TIRE_ELECTRONICS_VOLUME_MARGIN_BRIDGE_VS_GENERIC_MOBILITY_BETA","new_independent_case_count":3,"reused_case_count":0,"same_archetype_new_symbol_count":3,"same_archetype_new_trigger_family_count":2,"tested_existing_calibrated_axes":["stage2_actionable_evidence_bonus","price_only_blowoff_blocks_positive_stage","full_4b_requires_non_price_evidence"],"residual_error_types_found":["C29_generic_EV_supplier_false_positive","C29_theme_volume_spike_high_MAE","C29_tire_margin_positive_local_4B_watch"],"loop_contribution_label":"residual_error_found","do_not_propose_new_weight_delta":true,"batch_recalc_required":true,"evidence_url_pending":true}
```

---

## 15. Narrative-only row

```jsonl
{"row_type":"narrative_only","case_id":"C29_R9L88_PRIMARY_EVIDENCE_TODO","symbol":"MULTI","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","reason":"primary DART/IR evidence URLs were not attached in this run; keep shadow rows out of promotion until evidence_url_pending=false and source_proxy_only=false","price_source":"Songdaiki/stock-web","usage":"not_weight_promotion"}
```

---

## 16. Validation scope

Validation performed in this standalone MD:

```text
- Main prompt used as execution procedure.
- No-Repeat Index used as duplicate ledger only.
- R9 / loop 88 selected from prior local sequence after R8 / loop 88.
- R9 large_sector consistency: pass, because C29 mobility/auto-parts belongs to L3 mobility path.
- stock-web manifest checked.
- selected symbol profiles checked.
- tradable 2024 OHLC shards checked.
- corporate-action candidate windows checked against 2024 entry~D+180 windows.
- machine-readable case / trigger / aggregate / shadow_weight / residual_contribution rows included.
```

Limitations:

```text
- This run does not attach primary DART/IR/filing URLs.
- Source-proxy-only evidence means shadow rule promotion should be blocked.
- MFE/MAE values are approximate from inspected stock-web rows and should be batch-recomputed from CSV shards.
- No production scoring is changed.
```

---

## 17. Deferred Coding Agent Handoff Prompt

Do not execute this prompt in the current research session.

```text
You are a coding agent working on Songdaiki/stock_agent after v12 research ingestion.

Input MD:
e2r_stock_web_v12_residual_round_R9_loop_88_L3_BATTERY_EV_GREEN_MOBILITY_C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE_research.md

Tasks:
1. Parse all JSONL rows under case, trigger, score_simulation, aggregate_metric, shadow_weight, residual_contribution, and narrative_only sections.
2. Recompute OHLC-derived MFE/MAE/peak/drawdown from Songdaiki/stock-web tradable shards:
   - atlas/ohlcv_tradable_by_symbol_year/002/002350/2024.csv
   - atlas/ohlcv_tradable_by_symbol_year/009/009900/2024.csv
   - atlas/ohlcv_tradable_by_symbol_year/012/012860/2024.csv
3. Confirm profile corporate-action windows:
   - atlas/symbol_profiles/002/002350.json
   - atlas/symbol_profiles/009/009900.json
   - atlas/symbol_profiles/012/012860.json
4. Do not promote shadow_weight rows until primary evidence URLs are attached.
5. If evidence URLs are later attached and rows pass validation, treat this as C29 canonical guard evidence:
   - generic mobility/EV supplier beta without volume/mix/margin/revision bridge should cap below Stage2-Actionable;
   - rapid tire/parts MFE may become local 4B watch unless non-price evidence confirms continuation.
6. Do not alter global thresholds based on this single loop.
```

---

## 18. Final round state

```text
completed_round = R9
completed_loop = 88
next_round = R10
next_loop = 88
round_schedule_status = valid
round_sector_consistency = pass
large_sector_id = L3_BATTERY_EV_GREEN_MOBILITY
canonical_archetype_id = C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE
fine_archetype_id = AUTO_PARTS_TIRE_ELECTRONICS_VOLUME_MARGIN_BRIDGE_VS_GENERIC_MOBILITY_BETA
new_independent_case_count = 3
reused_case_count = 0
same_archetype_new_symbol_count = 3
positive_case_count = 1
counterexample_count = 2
local_4b_overlay_case_count = 2
hard_4c_count = 0
calibration_usable_trigger_count = 3
loop_contribution_label = residual_error_found
do_not_propose_new_weight_delta = true
```
