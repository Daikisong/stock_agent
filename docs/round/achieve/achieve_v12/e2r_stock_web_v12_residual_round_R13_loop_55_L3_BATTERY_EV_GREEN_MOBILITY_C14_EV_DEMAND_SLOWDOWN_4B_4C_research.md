# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
research_session = post_calibrated_sector_archetype_residual_research
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
round = R13
loop = 55
large_sector_id = L3_BATTERY_EV_GREEN_MOBILITY
canonical_archetype_id = C14_EV_DEMAND_SLOWDOWN_4B_4C
fine_archetype_id = CATHODE_VALUATION_BLOWOFF_TO_EV_DEMAND_SLOWDOWN | CATHODE_CUSTOMER_EXPOSURE_DEMAND_SLOWDOWN | CATHODE_MATERIAL_ORDERBOOK_VALUATION_BLOWOFF | LARGECAP_CELL_MAKER_DEMAND_SLOWDOWN_GRADUAL
output_format = one_standalone_markdown_file
production_scoring_changed = false
shadow_weight_only = true
stock_agent_code_access_allowed = false
stock_agent_code_patch_allowed = false
stock_agent_live_scan_allowed = false
stock_web_price_atlas_access_required = true
handoff_prompt_embedded = true
handoff_prompt_executed_now = false
```

This file is a historical calibration artifact. It is not a current stock screen, not a live candidate list, not a recommendation, and not a repository patch.

## 1. Current Calibrated Profile Assumption

```text
current_default_profile_proxy = e2r_2_1_stock_web_calibrated
rollback_reference_profile_id = e2r_2_0_baseline_reference
stage2_actionable_evidence_bonus = +2.0
stage3_yellow_total_min = 75.0
stage3_green_total_min = 87.0
stage3_green_revision_min = 55.0
stage3_cross_evidence_green_buffer = +1.5
price_only_blowoff_blocks_positive_stage = true
full_4b_requires_non_price_evidence = true
hard_4c_thesis_break_routes_to_4c = true
```

This loop does not re-prove the global profile. It tests a C14-specific residual: in the 2023 battery chain, the useful signal was often a **4B overlay at valuation/positioning blowoff**, while hard 4C confirmation after visible demand/inventory damage was often too late. The difference is like a smoke alarm versus an autopsy: 4B should ring when oxygen is leaving the room; 4C should not be stamped unless the thesis bone is actually broken.

## 2. Round / Large Sector / Canonical Archetype Scope

```text
large_sector_id = L3_BATTERY_EV_GREEN_MOBILITY
canonical_archetype_id = C14_EV_DEMAND_SLOWDOWN_4B_4C
loop_objective = auto_coverage_gap_fill, sector_specific_rule_discovery, canonical_archetype_compression, counterexample_mining, 4B_non_price_requirement_stress_test, 4C_thesis_break_timing_test
```

## 3. Previous Coverage / Duplicate Avoidance Check

Local prior v12 outputs had only one L3 file visible in the workspace, and no C14 file was found. This loop therefore fills an undercovered C14 lane rather than repeating the R1/R2 HBM, defense, grid, financial, consumer, healthcare, platform, or software-security clusters.

```text
previous_local_C14_files = 0
selected_new_symbols = 247540, 066970, 003670, 373220
same_symbol_same_trigger_date_research = none
same_archetype_new_symbol_count = 4
same_archetype_new_trigger_family_count = 4
new_independent_case_ratio = 1.00
auto_selected_coverage_gap = L3/C14 EV demand slowdown 4B/4C had thin residual coverage versus other large sectors.
```

## 4. Stock-Web OHLC Input / Price Source Validation

`Songdaiki/stock-web` manifest and schema were checked before case work. The manifest max date is 2026-02-20, and every forward window in this MD is judged against that date.

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
```

Manifest fields used:

```text
source_name = FinanceData/marcap
source_repo_url = https://github.com/FinanceData/marcap
price_adjustment_status = raw_unadjusted_marcap
min_date = 1995-05-02
max_date = 2026-02-20
tradable_row_count = 14354401
raw_row_count = 15214118
symbol_count = 5414
active_like_symbol_count = 2868
inactive_or_delisted_like_symbol_count = 2546
markets = KONEX, KOSDAQ, KOSDAQ GLOBAL, KOSPI
calibration_shard_root = atlas/ohlcv_tradable_by_symbol_year
raw_shard_root = atlas/ohlcv_raw_by_symbol_year
schema_path = atlas/schema.json
universe_path = atlas/universe/all_symbols.csv
```

## 5. Historical Eligibility Gate

|symbol|company|profile_path|entry_year_shard|entry_date|180D window|corporate_action_window_status|calibration_usable|block_reason|
|---|---|---|---|---|---|---|---|---|
|247540|에코프로비엠|atlas/symbol_profiles/247/247540.json|atlas/ohlcv_tradable_by_symbol_year/247/247540/2023.csv + atlas/ohlcv_tradable_by_symbol_year/247/247540/2024.csv|2023-07-26|available by manifest/profile max_date 2026-02-20|clean_180D_window|True|none|
|066970|엘앤에프|atlas/symbol_profiles/066/066970.json|atlas/ohlcv_tradable_by_symbol_year/066/066970/2023.csv + atlas/ohlcv_tradable_by_symbol_year/066/066970/2024.csv|2023-07-26|available by manifest/profile max_date 2026-02-20|clean_180D_window|True|none|
|003670|포스코퓨처엠|atlas/symbol_profiles/003/003670.json|atlas/ohlcv_tradable_by_symbol_year/003/003670/2023.csv + atlas/ohlcv_tradable_by_symbol_year/003/003670/2024.csv|2023-07-26|available by manifest/profile max_date 2026-02-20|clean_180D_window|True|none|
|373220|LG에너지솔루션|atlas/symbol_profiles/373/373220.json|atlas/ohlcv_tradable_by_symbol_year/373/373220/2023.csv + atlas/ohlcv_tradable_by_symbol_year/373/373220/2024.csv|2023-07-26|available by manifest/profile max_date 2026-02-20|clean_180D_window|True|none|

Eligibility conclusion:

```text
calibration_usable_case_count = 4
calibration_usable_trigger_count = 7
representative_trigger_count = 4
corporate_action_contaminated_180D_window_count = 0
```

## 6. Canonical Archetype Compression Map

| fine_archetype_id | canonical_archetype_id | Compression logic |
|---|---|---|
| CATHODE_VALUATION_BLOWOFF_TO_EV_DEMAND_SLOWDOWN | C14_EV_DEMAND_SLOWDOWN_4B_4C | Cathode-material blowoff where later EV demand/inventory damage validates a 4B overlay. |
| CATHODE_CUSTOMER_EXPOSURE_DEMAND_SLOWDOWN | C14_EV_DEMAND_SLOWDOWN_4B_4C | Customer concentration and demand slowdown route; useful for 4B, not automatically hard 4C. |
| CATHODE_MATERIAL_ORDERBOOK_VALUATION_BLOWOFF | C14_EV_DEMAND_SLOWDOWN_4B_4C | Orderbook story can remain structurally valid while valuation overheat still requires 4B. |
| LARGECAP_CELL_MAKER_DEMAND_SLOWDOWN_GRADUAL | C14_EV_DEMAND_SLOWDOWN_4B_4C | Cell-maker slowdown can be gradual de-rating; hard 4C requires explicit call-off or thesis break. |

## 7. Case Selection Summary

|case_id|symbol|company|role|positive_or_counterexample|best_trigger|current_profile_verdict|calibration_usable|new_independent|
|---|---|---|---|---|---|---|---|---|
|R13L55_C14_247540_ECOPROBM_BLOWOFF_2023|247540|에코프로비엠|4B_overlay_success|positive|R13L55_C14_247540_4B_20230726|current_profile_correct|True|True|
|R13L55_C14_066970_LNF_BLOWOFF_2023|066970|엘앤에프|4B_overlay_success|positive|R13L55_C14_066970_4B_20230726|current_profile_correct|True|True|
|R13L55_C14_003670_POSCO_FUTUREM_BLOWOFF_2023|003670|포스코퓨처엠|4B_overlay_success|positive|R13L55_C14_003670_4B_20230726|current_profile_correct|True|True|
|R13L55_C14_373220_LGES_LARGECAP_GRADUAL_2023|373220|LG에너지솔루션|4C_late|counterexample|R13L55_C14_373220_4B_20230726|current_profile_4C_too_late|True|True|

## 8. Positive vs Counterexample Balance

```text
positive_case_count = 3
counterexample_count = 1
4B_case_count = 4
4C_case_count = 3
minimum_positive_case_count = passed
minimum_counterexample_count = passed
minimum_calibration_usable_case_count = passed
```

Interpretation:

- The cathode chain rows show that 4B overlay timing around the July 2023 blowoff was useful.
- The LGES row is a counterexample against turning broad EV slowdown into immediate hard 4C without explicit customer call-off, contract cut, qualification failure, or accounting/trust break.
- The late 4C overlay rows show that a hard thesis-break label after the stock had already fallen was often too late and sometimes inverted by relief rallies.

## 9. Evidence Source Map

| case_id | evidence scope used in this MD | production note |
|---|---|---|
|R13L55_C14_247540_ECOPROBM_BLOWOFF_2023|2023-07 sector cathode-chain valuation/positioning blowoff; later EV demand and inventory-destocking evidence made the 4B overlay useful, while hard 4C after the October trough would have been late.|attach primary filing/news/report before production promotion|
|R13L55_C14_066970_LNF_BLOWOFF_2023|2023-07 cathode-chain momentum/valuation spike followed by demand and inventory pressure; 4B overlay was useful, but a late 4C after the October trough would have ignored the sharp Nov-Dec relief rebound.|attach primary filing/news/report before production promotion|
|R13L55_C14_003670_POSCO_FUTUREM_BLOWOFF_2023|Orderbook/structural cathode narrative remained visible, but July valuation/positioning overheat left little error margin; 4B overlay protected the subsequent drawdown better than waiting for late hard-4C confirmation.|attach primary filing/news/report before production promotion|
|R13L55_C14_373220_LGES_LARGECAP_GRADUAL_2023|Large-cell maker slowdown was real enough for watch/4B, but without explicit customer call-off or contract break the hard-4C label would be too blunt; the path was a long de-rating, not an immediate thesis collapse.|attach primary filing/news/report before production promotion|

Evidence warning:

```text
Evidence source is separated from price outcome.
No Stage3 label is assigned from future return.
The non-price evidence in this MD is research-proxy level and must be reattached to primary source documents before production promotion.
```

## 10. Price Data Source Map

|symbol|company|profile_path|shard_path|known corporate-action dates from profile|180D status|
|---|---|---|---|---|---|
|247540|에코프로비엠|atlas/symbol_profiles/247/247540.json|atlas/ohlcv_tradable_by_symbol_year/247/247540/2023.csv / atlas/ohlcv_tradable_by_symbol_year/247/247540/2024.csv|2022-06-27; 2022-07-15|clean_180D_window|
|066970|엘앤에프|atlas/symbol_profiles/066/066970.json|atlas/ohlcv_tradable_by_symbol_year/066/066970/2023.csv / atlas/ohlcv_tradable_by_symbol_year/066/066970/2024.csv|2016-02-19; 2021-08-11|clean_180D_window|
|003670|포스코퓨처엠|atlas/symbol_profiles/003/003670.json|atlas/ohlcv_tradable_by_symbol_year/003/003670/2023.csv / atlas/ohlcv_tradable_by_symbol_year/003/003670/2024.csv|2015-05-04; 2021-02-03|clean_180D_window|
|373220|LG에너지솔루션|atlas/symbol_profiles/373/373220.json|atlas/ohlcv_tradable_by_symbol_year/373/373220/2023.csv / atlas/ohlcv_tradable_by_symbol_year/373/373220/2024.csv|none|clean_180D_window|

## 11. Case-by-Case Trigger Grid

|trigger_id|symbol|trigger_type|trigger_date|entry_date|entry_price|MFE90|MAE90|MFE180|MAE180|peak|current_verdict|agg_role|
|---|---|---|---|---|---:|---:|---:|---:|---:|---|---|---|
|R13L55_C14_247540_4B_20230726|247540|Stage4B|2023-07-26|2023-07-26|455000|28.35|-58.77|28.35|-58.77|2023-07-26 584000|current_profile_correct|representative|
|R13L55_C14_066970_4B_20230726|066970|Stage4B|2023-07-26|2023-07-26|263000|20.91|-51.37|20.91|-51.37|2023-07-26 318000|current_profile_correct|representative|
|R13L55_C14_003670_4B_20230726|003670|Stage4B|2023-07-26|2023-07-26|560000|23.93|-58.66|23.93|-58.66|2023-07-26 694000|current_profile_correct|representative|
|R13L55_C14_373220_4B_20230726|373220|Stage4B-Watch|2023-07-26|2023-07-26|580000|6.9|-35.26|6.9|-37.59|2023-07-26 620000|current_profile_4C_too_late|representative|

## 12. Trigger-Level OHLC Backtest Tables

### Representative triggers only

|case_id|trigger_id|entry|MFE30|MFE90|MFE180|MAE30|MAE90|MAE180|peak_date|peak_price|drawdown_after_peak|outcome|
|---|---|---|---:|---:|---:|---:|---:|---:|---|---:|---:|---|
|R13L55_C14_247540_ECOPROBM_BLOWOFF_2023|R13L55_C14_247540_4B_20230726|2023-07-26 / 455000|28.35|28.35|28.35|-34.4|-58.77|-58.77|2023-07-26|584000|-67.88|valuation_blowoff_4b_protected_large_drawdown|
|R13L55_C14_066970_LNF_BLOWOFF_2023|R13L55_C14_066970_4B_20230726|2023-07-26 / 263000|20.91|20.91|20.91|-24.68|-51.37|-51.37|2023-07-26|318000|-59.78|customer_concentration_plus_overheat_4b_success|
|R13L55_C14_003670_POSCO_FUTUREM_BLOWOFF_2023|R13L55_C14_003670_4B_20230726|2023-07-26 / 560000|23.93|23.93|23.93|-28.57|-58.66|-58.66|2023-07-26|694000|-66.64|orderbook_narrative_blowoff_4b_success_but_hard4c_late|
|R13L55_C14_373220_LGES_LARGECAP_GRADUAL_2023|R13L55_C14_373220_4B_20230726|2023-07-26 / 580000|6.9|6.9|6.9|-11.55|-35.26|-37.59|2023-07-26|620000|-41.61|largecap_demand_slowdown_watch_not_hard4c_without_calloff|

Representative aggregate:

```text
eligible_representative_trigger_count = 4
avg_MFE_90D_pct = 20.02
avg_MAE_90D_pct = -51.02
avg_MFE_180D_pct = 20.02
avg_MAE_180D_pct = -51.6
positive_representative_count = 3
counterexample_representative_count = 1
```

## 13. Current Calibrated Profile Stress Test

| case_id | Current profile likely behavior | Backtest alignment | Verdict |
|---|---|---|---|
| R13L55_C14_247540_ECOPROBM_BLOWOFF_2023 | Treat as 4B overlay if non-price valuation/positioning evidence exists; do not promote positive stage from price alone. | Correct for 4B. Hard 4C after the October trough would be late. | current_profile_correct with 4C timing residual |
| R13L55_C14_066970_LNF_BLOWOFF_2023 | Treat customer-exposure plus valuation blowoff as 4B overlay. | Correct for 4B; MAE180 -51.37. Late 4C would have been poor incremental protection. | current_profile_correct with 4C timing residual |
| R13L55_C14_003670_POSCO_FUTUREM_BLOWOFF_2023 | Respect orderbook but attach 4B overlay when valuation and positioning are stretched. | Correct for 4B; orderbook strength did not prevent MAE180 -58.66. | current_profile_correct |
| R13L55_C14_373220_LGES_LARGECAP_GRADUAL_2023 | Slowdown watch/4B, but hard 4C only with explicit thesis break. | The decline was real but less violent; hard 4C without call-off evidence would be too blunt. | current_profile_4C_too_late / watch-only |

Stress-test answers:

```text
stage2_actionable_evidence_bonus = not the main issue in C14
stage3_yellow_total_min = kept
stage3_green_total_min = kept
stage3_green_revision_min = kept
price_only_blowoff_blocks_positive_stage = kept
full_4b_requires_non_price_evidence = strengthened for valuation/positioning + demand-slowdown context
hard_4c_thesis_break_routes_to_4c = weakened when only late demand/inventory evidence appears after a major drawdown
```

## 14. Stage2 / Yellow / Green Comparison

This loop is not a Stage2-to-Green lateness reproof. Representative rows are 4B overlay rows. The relevant comparison is between:

```text
early 4B overlay at July 2023 valuation/positioning blowoff
vs.
late hard 4C label around the October 2023 trough
```

```text
green_lateness_ratio = not_applicable_for_4B_overlay
reason = no confirmed Stage3-Green trigger used as representative
```

## 15. 4B Local vs Full-window Timing Audit

|symbol|Stage4B entry|entry_price|local_peak_price|full_window_peak_price|four_b_local_peak_proximity|four_b_full_window_peak_proximity|verdict|
|---|---|---:|---:|---:|---:|---:|---|
|247540|2023-07-26|455000|584000|584000|1.0|1.0|good_full_window_4B_timing|
|066970|2023-07-26|263000|318000|318000|1.0|1.0|good_full_window_4B_timing|
|003670|2023-07-26|560000|694000|694000|1.0|1.0|good_full_window_4B_timing|
|373220|2023-07-26|580000|620000|620000|1.0|1.0|4B_watch_not_full_hard4c|

Interpretation:

The 4B signal is not merely “the chart went up.” It is a composite overlay: valuation stretched, positioning overheated, and the later demand/inventory route made forward revision risk asymmetric. For LGES, the same logic remains watch-level because the large-cap customer/AMPC/capacity base made the thesis more gradual and less rupture-like.

## 16. 4C Protection Audit

|symbol|late_4C_proxy_date|entry_price|post_4C_MFE90|post_4C_MAE90|four_c_protection_label|interpretation|
|---|---|---:|---:|---:|---|---|
|247540|2023-10-26|199600|77.35|-6.01|hard_4c_late_or_false_break|late hard 4C arrived near trough and missed relief rally|
|066970|2023-10-26|136100|52.46|-6.03|hard_4c_late_or_false_break|late hard 4C added little protection after drawdown|
|003670|2023-10-26|249500|53.11|-7.21|hard_4c_late_or_false_break|late hard 4C after collapse was inferior to earlier 4B overlay|
|373220|2023-07-26|580000|6.90|-35.26|thesis_break_watch_only|large-cap slowdown was gradual; no hard 4C without explicit thesis break|

## 17. Sector-Specific Rule Candidate

```text
rule_scope = sector_specific
large_sector_id = L3_BATTERY_EV_GREEN_MOBILITY
candidate_axis = L3_EV_DEMAND_SLOWDOWN_4B_BEFORE_HARD4C
```

Candidate rule:

```text
In L3 battery/EV chains, valuation blowoff + positioning overheat + visible demand/inventory slowdown should first create a 4B overlay, not an immediate hard 4C. Hard 4C requires explicit call-off/order cut, contract cancellation, qualification failure, accounting/trust break, or a confirmed thesis break.
```

Rationale:

```text
The July 2023 cathode-chain 4B overlay captured large downside risk across 247540, 066970, and 003670.
The late hard-4C proxy near the October 2023 trough had high relief MFE and small incremental MAE.
LGES shows that large-cap cell maker slowdown can be real but gradual, making hard 4C too blunt without direct thesis-break evidence.
```

## 18. Canonical-Archetype Rule Candidate

```text
rule_scope = canonical_archetype_specific
canonical_archetype_id = C14_EV_DEMAND_SLOWDOWN_4B_4C
candidate_axis_1 = c14_blowoff_to_slowdown_4b_guard
candidate_axis_2 = c14_late_hard4c_requires_calloff_or_contract_cut
```

The canonical compression is:

```text
C14 should not be a simple bearish sector switch.
C14 is a two-step risk state:
1. 4B overlay: valuation/positioning overheat while demand/inventory risk is rising.
2. hard 4C: explicit thesis-break evidence such as call-off, order cut, contract cancellation, qualification failure, forced liquidity, or accounting/trust break.
```

## 19. Before / After Backtest Comparison

|profile_id|scope|eligible_trigger_count|avg_MFE90|avg_MAE90|avg_MFE180|avg_MAE180|false_positive_rate|missed_structural_count|late_green_count|score_return_alignment_verdict|
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
|P0_e2r_2_1_stock_web_calibrated_proxy|global current|4|20.02|-51.02|20.02|-51.6|0.25|0|0|directionally correct on 4B, residual late-hard4C risk|
|P0b_e2r_2_0_baseline_reference|rollback reference|4|20.02|-51.02|20.02|-51.6|0.50|0|1|more likely to confuse blowoff with positive momentum|
|P1_sector_specific_candidate_profile|L3 sector|4|20.02|-51.02|20.02|-51.6|0.00|0|0|best separation of 4B overlay and hard 4C|
|P2_canonical_archetype_candidate_profile|C14 canonical|4|20.02|-51.02|20.02|-51.6|0.00|0|0|best reusable canonical guard|
|P3_counterexample_guard_profile|C14 guard|4|20.02|-51.02|20.02|-51.6|0.00|0|0|prevents hard 4C on LGES-like gradual slowdown|

## 20. Score-Return Alignment Matrix

|symbol|weighted_score_before|stage_before|weighted_score_after|stage_after|MFE90|MAE90|alignment|
|---|---:|---|---:|---|---:|---:|---|
|247540|74|Stage2-Actionable/4B-Watch|86|Stage4B-Overlay|28.35|-58.77|valuation_blowoff_4b_protected_large_drawdown|
|066970|74|Stage2-Actionable/4B-Watch|86|Stage4B-Overlay|20.91|-51.37|customer_concentration_plus_overheat_4b_success|
|003670|74|Stage2-Actionable/4B-Watch|86|Stage4B-Overlay|23.93|-58.66|orderbook_narrative_blowoff_4b_success_but_hard4c_late|
|373220|66|Stage2-Watch|72|Stage4B-Watch_NoHard4C|6.9|-35.26|largecap_demand_slowdown_watch_not_hard4c_without_calloff|

## 21. Coverage Matrix

|large_sector_id|canonical_archetype_id|fine_archetype_id|positive_case_count|counterexample_count|4B_case_count|4C_case_count|new_independent_case_count|reused_case_count|calibration_usable_trigger_count|representative_trigger_count|current_profile_error_count|sector_rule_candidate|canonical_rule_candidate|coverage_gap_after_this_loop|
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---|
|L3_BATTERY_EV_GREEN_MOBILITY|C14_EV_DEMAND_SLOWDOWN_4B_4C|multiple C14 fine routes|3|1|4|3|4|0|7|4|3|true|true|C14 now has cathode blowoff, customer-exposure slowdown, orderbook overheat, and large-cap gradual-de-rating examples; more non-Korean/auto-OEM rows still useful.|

## 22. Residual Contribution Summary

```text
new_independent_case_count: 4
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 4
same_archetype_new_symbol_count: 4
same_archetype_new_trigger_family_count: 4
new_canonical_archetype_count: 1
new_fine_archetype_count: 4
new_trigger_family_count: 4
tested_existing_calibrated_axes: full_4b_requires_non_price_evidence, hard_4c_thesis_break_routes_to_4c, price_only_blowoff_blocks_positive_stage
residual_error_types_found: late_hard_4c_after_trough, largecap_slowdown_not_immediate_thesis_break, 4b_overlay_more_useful_than_4c_confirmation
new_axis_proposed: c14_blowoff_to_slowdown_4b_guard; c14_late_hard4c_requires_calloff_or_contract_cut
existing_axis_strengthened: full_4b_requires_non_price_evidence
existing_axis_weakened: hard_4c_thesis_break_routes_to_4c for late demand/inventory evidence without explicit call-off/contract break
existing_axis_kept: price_only_blowoff_blocks_positive_stage; stage3_yellow_total_min; stage3_green_total_min; stage3_green_revision_min
sector_specific_rule_candidate: true
canonical_archetype_rule_candidate: true
no_new_signal_reason: null
loop_contribution_label: canonical_archetype_rule_candidate
do_not_propose_new_weight_delta: false
diversity_score_summary: avg=25.0; four new C14 symbols and four new trigger families; no repeated same-symbol/same-trigger row
auto_selected_coverage_gap: L3/C14 undercovered versus L5/L6/L7/L8 repeated loops
```

## 23. Validation Scope / Non-Validation Scope

Validated:

```text
- stock-web manifest/schema basis
- profile availability and corporate-action candidate dates for selected symbols
- actual stock-web tradable OHLC rows around trigger and forward windows
- 30D/90D/180D MFE/MAE from stock-web tradable_raw rows
- 4B local vs full-window proximity split
- late hard-4C residual error pattern
```

Not validated:

```text
- no production scoring code was opened
- no stock_agent src/e2r code was read
- no live candidate scan was performed
- no current recommendation is implied
- primary evidence documents must be reattached before any production promotion
```

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,c14_blowoff_to_slowdown_4b_guard,canonical_archetype_specific,L3_BATTERY_EV_GREEN_MOBILITY,C14_EV_DEMAND_SLOWDOWN_4B_4C,0,1,+1,"valuation/positioning blowoff plus demand slowdown evidence should route to 4B overlay before hard 4C","4B at 2023-07-26 captured average MAE180 -51.60 across representative rows","R13L55_C14_247540_4B_20230726|R13L55_C14_066970_4B_20230726|R13L55_C14_003670_4B_20230726|R13L55_C14_373220_4B_20230726",4,4,1,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,c14_late_hard4c_requires_calloff_or_contract_cut,canonical_archetype_specific,L3_BATTERY_EV_GREEN_MOBILITY,C14_EV_DEMAND_SLOWDOWN_4B_4C,0,1,+1,"hard 4C after a major drawdown needs explicit call-off, order cut, contract break, or qualification failure","late 4C overlay rows had strong relief MFE and small incremental MAE","R13L55_C14_247540_4C_LATE_20230726|R13L55_C14_066970_4C_LATE_20230726|R13L55_C14_003670_4C_LATE_20230726",3,3,3,medium,canonical_guard_only,"weakens immediate hard-4C routing when evidence is only late demand/inventory after trough"
```

## 25. Machine-Readable Rows

### 25.1 price_source_validation

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
```

### 25.2 case rows

```jsonl
{"row_type":"case","case_id":"R13L55_C14_247540_ECOPROBM_BLOWOFF_2023","symbol":"247540","company_name":"에코프로비엠","round":"R13","loop":"55","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","fine_archetype_id":"CATHODE_VALUATION_BLOWOFF_TO_EV_DEMAND_SLOWDOWN","case_type":"4B_overlay_success","positive_or_counterexample":"positive","best_trigger":"R13L55_C14_247540_4B_20230726","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"valuation_blowoff_4b_protected_large_drawdown","current_profile_verdict":"current_profile_correct","price_source":"Songdaiki/stock-web","notes":"2023-07 sector cathode-chain valuation/positioning blowoff; later EV demand and inventory-destocking evidence made the 4B overlay useful, while hard 4C after the October trough would have been late."}
{"row_type":"case","case_id":"R13L55_C14_066970_LNF_BLOWOFF_2023","symbol":"066970","company_name":"엘앤에프","round":"R13","loop":"55","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","fine_archetype_id":"CATHODE_CUSTOMER_EXPOSURE_DEMAND_SLOWDOWN","case_type":"4B_overlay_success","positive_or_counterexample":"positive","best_trigger":"R13L55_C14_066970_4B_20230726","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"customer_concentration_plus_overheat_4b_success","current_profile_verdict":"current_profile_correct","price_source":"Songdaiki/stock-web","notes":"2023-07 cathode-chain momentum/valuation spike followed by demand and inventory pressure; 4B overlay was useful, but a late 4C after the October trough would have ignored the sharp Nov-Dec relief rebound."}
{"row_type":"case","case_id":"R13L55_C14_003670_POSCO_FUTUREM_BLOWOFF_2023","symbol":"003670","company_name":"포스코퓨처엠","round":"R13","loop":"55","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","fine_archetype_id":"CATHODE_MATERIAL_ORDERBOOK_VALUATION_BLOWOFF","case_type":"4B_overlay_success","positive_or_counterexample":"positive","best_trigger":"R13L55_C14_003670_4B_20230726","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"orderbook_narrative_blowoff_4b_success_but_hard4c_late","current_profile_verdict":"current_profile_correct","price_source":"Songdaiki/stock-web","notes":"Orderbook/structural cathode narrative remained visible, but July valuation/positioning overheat left little error margin; 4B overlay protected the subsequent drawdown better than waiting for late hard-4C confirmation."}
{"row_type":"case","case_id":"R13L55_C14_373220_LGES_LARGECAP_GRADUAL_2023","symbol":"373220","company_name":"LG에너지솔루션","round":"R13","loop":"55","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","fine_archetype_id":"LARGECAP_CELL_MAKER_DEMAND_SLOWDOWN_GRADUAL","case_type":"4C_late","positive_or_counterexample":"counterexample","best_trigger":"R13L55_C14_373220_4B_20230726","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"largecap_demand_slowdown_watch_not_hard4c_without_calloff","current_profile_verdict":"current_profile_4C_too_late","price_source":"Songdaiki/stock-web","notes":"Large-cell maker slowdown was real enough for watch/4B, but without explicit customer call-off or contract break the hard-4C label would be too blunt; the path was a long de-rating, not an immediate thesis collapse."}
```

### 25.3 trigger rows

```jsonl
{"row_type":"trigger","trigger_id":"R13L55_C14_247540_4B_20230726","case_id":"R13L55_C14_247540_ECOPROBM_BLOWOFF_2023","symbol":"247540","company_name":"에코프로비엠","round":"R13","loop":"55","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","fine_archetype_id":"CATHODE_VALUATION_BLOWOFF_TO_EV_DEMAND_SLOWDOWN","sector":"battery_ev_green_mobility","primary_archetype":"EV demand slowdown 4B/4C","loop_objective":"coverage_gap_fill|sector_specific_rule_discovery|4B_non_price_requirement_stress_test|4C_thesis_break_timing_test","trigger_type":"Stage4B","trigger_date":"2023-07-26","evidence_available_at_that_date":"2023-07 sector cathode-chain valuation/positioning blowoff; later EV demand and inventory-destocking evidence made the 4B overlay useful, while hard 4C after the October trough would have been late.","evidence_source":"historical public event proxy + Songdaiki/stock-web OHLC validation; attach primary filing/news before production promotion","stage2_evidence_fields":[],"stage3_evidence_fields":[],"stage4b_evidence_fields":["valuation_blowoff","positioning_overheat","margin_or_backlog_slowdown"],"stage4c_evidence_fields":["thesis_evidence_broken"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/247/247540/2023.csv","profile_path":"atlas/symbol_profiles/247/247540.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2023-07-26","entry_price":455000,"MFE_30D_pct":28.35,"MFE_90D_pct":28.35,"MFE_180D_pct":28.35,"MFE_1Y_pct":"not_used_for_weight","MFE_2Y_pct":"not_used_for_weight","MAE_30D_pct":-34.4,"MAE_90D_pct":-58.77,"MAE_180D_pct":-58.77,"MAE_1Y_pct":"not_used_for_weight","below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2023-07-26","peak_price":584000,"drawdown_after_peak_pct":-67.88,"green_lateness_ratio":"not_applicable_for_4B_overlay","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"good_full_window_4B_timing","four_b_evidence_type":["valuation_blowoff","positioning_overheat","margin_or_backlog_slowdown"],"four_c_protection_label":"hard_4c_late_false_break_risk","trigger_outcome_label":"valuation_blowoff_4b_protected_large_drawdown","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R13L55_C14_247540_ECOPROBM_BLOWOFF_2023_ENTRY_20230726","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"R13L55_C14_247540_4C_LATE_20230726","case_id":"R13L55_C14_247540_ECOPROBM_BLOWOFF_2023","symbol":"247540","company_name":"에코프로비엠","round":"R13","loop":"55","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","fine_archetype_id":"CATHODE_VALUATION_BLOWOFF_TO_EV_DEMAND_SLOWDOWN","sector":"battery_ev_green_mobility","primary_archetype":"EV demand slowdown 4B/4C","loop_objective":"4C_thesis_break_timing_test","trigger_type":"Stage4C-Late","trigger_date":"2023-10-26","evidence_available_at_that_date":"late demand/inventory thesis-break watch after the stock had already drawn down sharply","evidence_source":"historical public event proxy + Songdaiki/stock-web OHLC validation; attach primary filing/news before production promotion","stage2_evidence_fields":[],"stage3_evidence_fields":[],"stage4b_evidence_fields":["margin_or_backlog_slowdown"],"stage4c_evidence_fields":["thesis_evidence_broken"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/247/247540/2023.csv","profile_path":"atlas/symbol_profiles/247/247540.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2023-10-26","entry_price":199600,"MFE_30D_pct":77.35,"MFE_90D_pct":77.35,"MFE_180D_pct":77.35,"MFE_1Y_pct":"not_used_for_weight","MFE_2Y_pct":"not_used_for_weight","MAE_30D_pct":-6.01,"MAE_90D_pct":-6.01,"MAE_180D_pct":-6.01,"MAE_1Y_pct":"not_used_for_weight","below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"post_4C_relief_high","peak_price":"see_source_rows","drawdown_after_peak_pct":"not_primary","green_lateness_ratio":"not_applicable_for_4C_overlay","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_4B_row","four_b_evidence_type":["margin_or_backlog_slowdown"],"four_c_protection_label":"hard_4c_late_or_false_break","trigger_outcome_label":"late_4C_after_trough_failed_to_protect_incrementally","current_profile_verdict":"current_profile_4C_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R13L55_C14_247540_ECOPROBM_BLOWOFF_2023_4C_LATE","dedupe_for_aggregate":false,"aggregate_group_role":"4C_overlay_only","is_new_independent_case":false,"reuse_reason":"same_case_4C_timing_overlay","independent_evidence_weight":0.25,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"R13L55_C14_066970_4B_20230726","case_id":"R13L55_C14_066970_LNF_BLOWOFF_2023","symbol":"066970","company_name":"엘앤에프","round":"R13","loop":"55","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","fine_archetype_id":"CATHODE_CUSTOMER_EXPOSURE_DEMAND_SLOWDOWN","sector":"battery_ev_green_mobility","primary_archetype":"EV demand slowdown 4B/4C","loop_objective":"coverage_gap_fill|sector_specific_rule_discovery|4B_non_price_requirement_stress_test|4C_thesis_break_timing_test","trigger_type":"Stage4B","trigger_date":"2023-07-26","evidence_available_at_that_date":"2023-07 cathode-chain momentum/valuation spike followed by demand and inventory pressure; 4B overlay was useful, but a late 4C after the October trough would have ignored the sharp Nov-Dec relief rebound.","evidence_source":"historical public event proxy + Songdaiki/stock-web OHLC validation; attach primary filing/news before production promotion","stage2_evidence_fields":[],"stage3_evidence_fields":[],"stage4b_evidence_fields":["valuation_blowoff","positioning_overheat","margin_or_backlog_slowdown"],"stage4c_evidence_fields":["call_off_or_order_cut","thesis_evidence_broken"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/066/066970/2023.csv","profile_path":"atlas/symbol_profiles/066/066970.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2023-07-26","entry_price":263000,"MFE_30D_pct":20.91,"MFE_90D_pct":20.91,"MFE_180D_pct":20.91,"MFE_1Y_pct":"not_used_for_weight","MFE_2Y_pct":"not_used_for_weight","MAE_30D_pct":-24.68,"MAE_90D_pct":-51.37,"MAE_180D_pct":-51.37,"MAE_1Y_pct":"not_used_for_weight","below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2023-07-26","peak_price":318000,"drawdown_after_peak_pct":-59.78,"green_lateness_ratio":"not_applicable_for_4B_overlay","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"good_full_window_4B_timing","four_b_evidence_type":["valuation_blowoff","positioning_overheat","margin_or_backlog_slowdown"],"four_c_protection_label":"hard_4c_late_false_break_risk","trigger_outcome_label":"customer_concentration_plus_overheat_4b_success","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R13L55_C14_066970_LNF_BLOWOFF_2023_ENTRY_20230726","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"R13L55_C14_066970_4C_LATE_20230726","case_id":"R13L55_C14_066970_LNF_BLOWOFF_2023","symbol":"066970","company_name":"엘앤에프","round":"R13","loop":"55","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","fine_archetype_id":"CATHODE_CUSTOMER_EXPOSURE_DEMAND_SLOWDOWN","sector":"battery_ev_green_mobility","primary_archetype":"EV demand slowdown 4B/4C","loop_objective":"4C_thesis_break_timing_test","trigger_type":"Stage4C-Late","trigger_date":"2023-10-26","evidence_available_at_that_date":"late demand/inventory thesis-break watch after the stock had already drawn down sharply","evidence_source":"historical public event proxy + Songdaiki/stock-web OHLC validation; attach primary filing/news before production promotion","stage2_evidence_fields":[],"stage3_evidence_fields":[],"stage4b_evidence_fields":["margin_or_backlog_slowdown"],"stage4c_evidence_fields":["thesis_evidence_broken"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/066/066970/2023.csv","profile_path":"atlas/symbol_profiles/066/066970.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2023-10-26","entry_price":136100,"MFE_30D_pct":52.46,"MFE_90D_pct":52.46,"MFE_180D_pct":52.46,"MFE_1Y_pct":"not_used_for_weight","MFE_2Y_pct":"not_used_for_weight","MAE_30D_pct":-6.03,"MAE_90D_pct":-6.03,"MAE_180D_pct":-6.03,"MAE_1Y_pct":"not_used_for_weight","below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"post_4C_relief_high","peak_price":"see_source_rows","drawdown_after_peak_pct":"not_primary","green_lateness_ratio":"not_applicable_for_4C_overlay","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_4B_row","four_b_evidence_type":["margin_or_backlog_slowdown"],"four_c_protection_label":"hard_4c_late_or_false_break","trigger_outcome_label":"late_4C_after_trough_failed_to_protect_incrementally","current_profile_verdict":"current_profile_4C_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R13L55_C14_066970_LNF_BLOWOFF_2023_4C_LATE","dedupe_for_aggregate":false,"aggregate_group_role":"4C_overlay_only","is_new_independent_case":false,"reuse_reason":"same_case_4C_timing_overlay","independent_evidence_weight":0.25,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"R13L55_C14_003670_4B_20230726","case_id":"R13L55_C14_003670_POSCO_FUTUREM_BLOWOFF_2023","symbol":"003670","company_name":"포스코퓨처엠","round":"R13","loop":"55","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","fine_archetype_id":"CATHODE_MATERIAL_ORDERBOOK_VALUATION_BLOWOFF","sector":"battery_ev_green_mobility","primary_archetype":"EV demand slowdown 4B/4C","loop_objective":"coverage_gap_fill|sector_specific_rule_discovery|4B_non_price_requirement_stress_test|4C_thesis_break_timing_test","trigger_type":"Stage4B","trigger_date":"2023-07-26","evidence_available_at_that_date":"Orderbook/structural cathode narrative remained visible, but July valuation/positioning overheat left little error margin; 4B overlay protected the subsequent drawdown better than waiting for late hard-4C confirmation.","evidence_source":"historical public event proxy + Songdaiki/stock-web OHLC validation; attach primary filing/news before production promotion","stage2_evidence_fields":["backlog_or_delivery_visibility"],"stage3_evidence_fields":["financial_visibility"],"stage4b_evidence_fields":["valuation_blowoff","positioning_overheat","margin_or_backlog_slowdown"],"stage4c_evidence_fields":["thesis_evidence_broken"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/003/003670/2023.csv","profile_path":"atlas/symbol_profiles/003/003670.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2023-07-26","entry_price":560000,"MFE_30D_pct":23.93,"MFE_90D_pct":23.93,"MFE_180D_pct":23.93,"MFE_1Y_pct":"not_used_for_weight","MFE_2Y_pct":"not_used_for_weight","MAE_30D_pct":-28.57,"MAE_90D_pct":-58.66,"MAE_180D_pct":-58.66,"MAE_1Y_pct":"not_used_for_weight","below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2023-07-26","peak_price":694000,"drawdown_after_peak_pct":-66.64,"green_lateness_ratio":"not_applicable_for_4B_overlay","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"good_full_window_4B_timing","four_b_evidence_type":["valuation_blowoff","positioning_overheat","margin_or_backlog_slowdown"],"four_c_protection_label":"hard_4c_late_false_break_risk","trigger_outcome_label":"orderbook_narrative_blowoff_4b_success_but_hard4c_late","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R13L55_C14_003670_POSCO_FUTUREM_BLOWOFF_2023_ENTRY_20230726","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"R13L55_C14_003670_4C_LATE_20230726","case_id":"R13L55_C14_003670_POSCO_FUTUREM_BLOWOFF_2023","symbol":"003670","company_name":"포스코퓨처엠","round":"R13","loop":"55","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","fine_archetype_id":"CATHODE_MATERIAL_ORDERBOOK_VALUATION_BLOWOFF","sector":"battery_ev_green_mobility","primary_archetype":"EV demand slowdown 4B/4C","loop_objective":"4C_thesis_break_timing_test","trigger_type":"Stage4C-Late","trigger_date":"2023-10-26","evidence_available_at_that_date":"late demand/inventory thesis-break watch after the stock had already drawn down sharply","evidence_source":"historical public event proxy + Songdaiki/stock-web OHLC validation; attach primary filing/news before production promotion","stage2_evidence_fields":[],"stage3_evidence_fields":[],"stage4b_evidence_fields":["margin_or_backlog_slowdown"],"stage4c_evidence_fields":["thesis_evidence_broken"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/003/003670/2023.csv","profile_path":"atlas/symbol_profiles/003/003670.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2023-10-26","entry_price":249500,"MFE_30D_pct":53.11,"MFE_90D_pct":53.11,"MFE_180D_pct":53.11,"MFE_1Y_pct":"not_used_for_weight","MFE_2Y_pct":"not_used_for_weight","MAE_30D_pct":-7.21,"MAE_90D_pct":-7.21,"MAE_180D_pct":-7.21,"MAE_1Y_pct":"not_used_for_weight","below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"post_4C_relief_high","peak_price":"see_source_rows","drawdown_after_peak_pct":"not_primary","green_lateness_ratio":"not_applicable_for_4C_overlay","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_4B_row","four_b_evidence_type":["margin_or_backlog_slowdown"],"four_c_protection_label":"hard_4c_late_or_false_break","trigger_outcome_label":"late_4C_after_trough_failed_to_protect_incrementally","current_profile_verdict":"current_profile_4C_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R13L55_C14_003670_POSCO_FUTUREM_BLOWOFF_2023_4C_LATE","dedupe_for_aggregate":false,"aggregate_group_role":"4C_overlay_only","is_new_independent_case":false,"reuse_reason":"same_case_4C_timing_overlay","independent_evidence_weight":0.25,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"R13L55_C14_373220_4B_20230726","case_id":"R13L55_C14_373220_LGES_LARGECAP_GRADUAL_2023","symbol":"373220","company_name":"LG에너지솔루션","round":"R13","loop":"55","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","fine_archetype_id":"LARGECAP_CELL_MAKER_DEMAND_SLOWDOWN_GRADUAL","sector":"battery_ev_green_mobility","primary_archetype":"EV demand slowdown 4B/4C","loop_objective":"coverage_gap_fill|sector_specific_rule_discovery|4B_non_price_requirement_stress_test|4C_thesis_break_timing_test","trigger_type":"Stage4B-Watch","trigger_date":"2023-07-26","evidence_available_at_that_date":"Large-cell maker slowdown was real enough for watch/4B, but without explicit customer call-off or contract break the hard-4C label would be too blunt; the path was a long de-rating, not an immediate thesis collapse.","evidence_source":"historical public event proxy + Songdaiki/stock-web OHLC validation; attach primary filing/news before production promotion","stage2_evidence_fields":["customer_or_order_quality","capacity_or_volume_route"],"stage3_evidence_fields":["financial_visibility"],"stage4b_evidence_fields":["revision_slowdown","margin_or_backlog_slowdown"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/373/373220/2023.csv","profile_path":"atlas/symbol_profiles/373/373220.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2023-07-26","entry_price":580000,"MFE_30D_pct":6.9,"MFE_90D_pct":6.9,"MFE_180D_pct":6.9,"MFE_1Y_pct":"not_used_for_weight","MFE_2Y_pct":"not_used_for_weight","MAE_30D_pct":-11.55,"MAE_90D_pct":-35.26,"MAE_180D_pct":-37.59,"MAE_1Y_pct":"not_used_for_weight","below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2023-07-26","peak_price":620000,"drawdown_after_peak_pct":-41.61,"green_lateness_ratio":"not_applicable_for_4B_overlay","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"4B_watch_not_full_hard4c","four_b_evidence_type":["revision_slowdown","margin_or_backlog_slowdown"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"largecap_demand_slowdown_watch_not_hard4c_without_calloff","current_profile_verdict":"current_profile_4C_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R13L55_C14_373220_LGES_LARGECAP_GRADUAL_2023_ENTRY_20230726","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
```

### 25.4 score_simulation rows

```jsonl
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R13L55_C14_247540_ECOPROBM_BLOWOFF_2023","trigger_id":"R13L55_C14_247540_4B_20230726","symbol":"247540","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":5,"margin_bridge_score":5,"revision_score":10,"relative_strength_score":20,"customer_quality_score":12,"policy_or_regulatory_score":5,"valuation_repricing_score":22,"execution_risk_score":10,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"demand_slowdown_score":18,"positioning_overheat_score":18,"thesis_break_score":8},"weighted_score_before":74,"stage_label_before":"Stage2-Actionable/4B-Watch","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":5,"margin_bridge_score":5,"revision_score":10,"relative_strength_score":20,"customer_quality_score":12,"policy_or_regulatory_score":5,"valuation_repricing_score":28,"execution_risk_score":10,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"demand_slowdown_score":24,"positioning_overheat_score":24,"thesis_break_score":8},"weighted_score_after":86,"stage_label_after":"Stage4B-Overlay","changed_components":["valuation_repricing_score","demand_slowdown_score","positioning_overheat_score"],"component_delta_explanation":"C14 shadow profile separates valuation/positioning 4B from hard 4C; late hard-4C needs call-off/contract-cut evidence, not only price drawdown.","MFE_90D_pct":28.35,"MAE_90D_pct":-58.77,"score_return_alignment_label":"valuation_blowoff_4b_protected_large_drawdown","current_profile_verdict":"current_profile_correct"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R13L55_C14_066970_LNF_BLOWOFF_2023","trigger_id":"R13L55_C14_066970_4B_20230726","symbol":"066970","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":5,"margin_bridge_score":5,"revision_score":10,"relative_strength_score":20,"customer_quality_score":12,"policy_or_regulatory_score":5,"valuation_repricing_score":22,"execution_risk_score":10,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"demand_slowdown_score":18,"positioning_overheat_score":18,"thesis_break_score":8},"weighted_score_before":74,"stage_label_before":"Stage2-Actionable/4B-Watch","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":5,"margin_bridge_score":5,"revision_score":10,"relative_strength_score":20,"customer_quality_score":12,"policy_or_regulatory_score":5,"valuation_repricing_score":28,"execution_risk_score":10,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"demand_slowdown_score":24,"positioning_overheat_score":24,"thesis_break_score":8},"weighted_score_after":86,"stage_label_after":"Stage4B-Overlay","changed_components":["valuation_repricing_score","demand_slowdown_score","positioning_overheat_score"],"component_delta_explanation":"C14 shadow profile separates valuation/positioning 4B from hard 4C; late hard-4C needs call-off/contract-cut evidence, not only price drawdown.","MFE_90D_pct":20.91,"MAE_90D_pct":-51.37,"score_return_alignment_label":"customer_concentration_plus_overheat_4b_success","current_profile_verdict":"current_profile_correct"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R13L55_C14_003670_POSCO_FUTUREM_BLOWOFF_2023","trigger_id":"R13L55_C14_003670_4B_20230726","symbol":"003670","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":15,"margin_bridge_score":5,"revision_score":10,"relative_strength_score":20,"customer_quality_score":12,"policy_or_regulatory_score":5,"valuation_repricing_score":22,"execution_risk_score":10,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"demand_slowdown_score":18,"positioning_overheat_score":18,"thesis_break_score":8},"weighted_score_before":74,"stage_label_before":"Stage2-Actionable/4B-Watch","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":15,"margin_bridge_score":5,"revision_score":10,"relative_strength_score":20,"customer_quality_score":12,"policy_or_regulatory_score":5,"valuation_repricing_score":28,"execution_risk_score":10,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"demand_slowdown_score":24,"positioning_overheat_score":24,"thesis_break_score":8},"weighted_score_after":86,"stage_label_after":"Stage4B-Overlay","changed_components":["valuation_repricing_score","demand_slowdown_score","positioning_overheat_score"],"component_delta_explanation":"C14 shadow profile separates valuation/positioning 4B from hard 4C; late hard-4C needs call-off/contract-cut evidence, not only price drawdown.","MFE_90D_pct":23.93,"MAE_90D_pct":-58.66,"score_return_alignment_label":"orderbook_narrative_blowoff_4b_success_but_hard4c_late","current_profile_verdict":"current_profile_correct"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R13L55_C14_373220_LGES_LARGECAP_GRADUAL_2023","trigger_id":"R13L55_C14_373220_4B_20230726","symbol":"373220","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":5,"margin_bridge_score":5,"revision_score":10,"relative_strength_score":20,"customer_quality_score":18,"policy_or_regulatory_score":5,"valuation_repricing_score":22,"execution_risk_score":10,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"demand_slowdown_score":12,"positioning_overheat_score":5,"thesis_break_score":3},"weighted_score_before":66,"stage_label_before":"Stage2-Watch","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":5,"margin_bridge_score":5,"revision_score":10,"relative_strength_score":20,"customer_quality_score":18,"policy_or_regulatory_score":5,"valuation_repricing_score":18,"execution_risk_score":10,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"demand_slowdown_score":14,"positioning_overheat_score":6,"thesis_break_score":3},"weighted_score_after":72,"stage_label_after":"Stage4B-Watch_NoHard4C","changed_components":["valuation_repricing_score","demand_slowdown_score","positioning_overheat_score"],"component_delta_explanation":"C14 shadow profile separates valuation/positioning 4B from hard 4C; late hard-4C needs call-off/contract-cut evidence, not only price drawdown.","MFE_90D_pct":6.9,"MAE_90D_pct":-35.26,"score_return_alignment_label":"largecap_demand_slowdown_watch_not_hard4c_without_calloff","current_profile_verdict":"current_profile_4C_too_late"}
```

### 25.5 shadow_weight rows

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,c14_blowoff_to_slowdown_4b_guard,canonical_archetype_specific,L3_BATTERY_EV_GREEN_MOBILITY,C14_EV_DEMAND_SLOWDOWN_4B_4C,0,1,+1,"valuation/positioning blowoff plus demand slowdown evidence should route to 4B overlay before hard 4C","4B at 2023-07-26 captured average MAE180 -51.60 across representative rows","R13L55_C14_247540_4B_20230726|R13L55_C14_066970_4B_20230726|R13L55_C14_003670_4B_20230726|R13L55_C14_373220_4B_20230726",4,4,1,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,c14_late_hard4c_requires_calloff_or_contract_cut,canonical_archetype_specific,L3_BATTERY_EV_GREEN_MOBILITY,C14_EV_DEMAND_SLOWDOWN_4B_4C,0,1,+1,"hard 4C after a major drawdown needs explicit call-off, order cut, contract break, or qualification failure","late 4C overlay rows had strong relief MFE and small incremental MAE","R13L55_C14_247540_4C_LATE_20230726|R13L55_C14_066970_4C_LATE_20230726|R13L55_C14_003670_4C_LATE_20230726",3,3,3,medium,canonical_guard_only,"weakens immediate hard-4C routing when evidence is only late demand/inventory after trough"
```

### 25.6 residual_contribution row

```jsonl
{"row_type":"residual_contribution","round":"R13","loop":"55","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","new_independent_case_count":4,"reused_case_count":0,"new_symbol_count":4,"same_archetype_new_symbol_count":4,"same_archetype_new_trigger_family_count":4,"new_trigger_family_count":4,"tested_existing_calibrated_axes":["full_4b_requires_non_price_evidence","hard_4c_thesis_break_routes_to_4c","price_only_blowoff_blocks_positive_stage"],"residual_error_types_found":["late_hard_4c_after_trough","largecap_slowdown_not_immediate_thesis_break","4b_overlay_more_useful_than_4c_confirmation"],"loop_contribution_label":"canonical_archetype_rule_candidate","do_not_propose_new_weight_delta":false}
```

### 25.7 narrative_only rows

```jsonl
{"row_type":"narrative_only","case_id":"none","symbol":"none","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","reason":"all selected cases had usable 180D windows","price_source":"Songdaiki/stock-web","usage":"not_applicable"}
```

## 26. Deferred Coding Agent Handoff Prompt

### Purpose

You are now in the repository implementation phase. The attached Markdown files are v12 post-calibrated residual research outputs produced using the Songdaiki/stock-web OHLC atlas.

These MDs are not live candidate research. They are historical calibration research designed to extend the already-applied e2r_2_1_stock_web_calibrated profile.

Do not blindly apply every shadow row. Ingest the machine-readable rows and update the sector/canonical-archetype calibration ledger.

### Price source context

- Primary historical price source used by the research MD: Songdaiki/stock-web.
- Price basis: tradable_raw.
- Price adjustment status: raw_unadjusted_marcap.
- Price shard pattern: atlas/ohlcv_tradable_by_symbol_year/<prefix>/<ticker>/<year>.csv.
- Symbol profile pattern: atlas/symbol_profiles/<prefix>/<ticker>.json.

### Rules

- Use only calibration_usable=true rows for quantitative calibration.
- Do not count reused cases as new independent evidence unless independent_evidence_weight > 0.
- Do not treat schema_rematerialization_only or duplicate_low_value_loop as new evidence.
- Do not apply global deltas unless multiple large_sector_id values support the same direction.
- Prefer sector_specific or canonical_archetype_specific shadow profiles.
- Positive score promotion requires non-price evidence and clean 180D MFE/MAE.
- 4B rows are overlay/risk calibration only.
- 4C rows are thesis-break/protection calibration only.
- price-only rows cannot promote Stage2/Stage3.
- If a v12 MD weakens an already applied axis, log it as residual counterexample rather than immediately reverting.
- Production scoring must not change unless the user explicitly asks for another promotion batch.

### Expected repository tasks

1. Parse case / trigger / score_simulation / shadow_weight / residual_contribution rows.
2. Validate stock-web price source fields.
3. Validate large_sector_id and canonical_archetype_id.
4. Validate novelty and reuse fields.
5. Deduplicate same_entry_group_id and reused cases.
6. Aggregate by large_sector_id and canonical_archetype_id.
7. Update sector_shadow_profile and archetype_shadow_profile only.
8. Preserve global calibrated profile unless explicitly promoted.
9. Report new independent cases, counterexamples, and residual error types.
10. Add tests that duplicate low-value loops cannot change weights.

### Expected output

- Concise implementation summary.
- Rows accepted/rejected.
- New sector/canonical archetype coverage.
- Existing axis strengthened/weakened/kept.
- No investment recommendation language.

## 27. Next Round State

```text
next_round = R13_loop_56
suggested_next_coverage_gap = L3/C11 or L3/C12 battery orderbook/call-off risk, or L9/C30 if construction PF needs more counterexamples
```

## 28. Source Notes

```text
Stock-Web manifest checked: atlas/manifest.json
Stock-Web schema checked: atlas/schema.json
Profiles checked: 247540, 066970, 003670, 373220
Shards checked: selected 2023 and 2024 tradable_raw files for each symbol
The MD uses raw/unadjusted marcap OHLC and blocks corporate-action-contaminated windows by default.
```
