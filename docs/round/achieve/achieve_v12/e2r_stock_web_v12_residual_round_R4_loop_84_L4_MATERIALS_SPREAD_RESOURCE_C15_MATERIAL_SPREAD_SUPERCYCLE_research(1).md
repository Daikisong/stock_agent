# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```yaml
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
selected_round: R4
selected_loop: 84
selection_basis: docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket: Priority 1 C15 spread reversal / inventory-cycle balance repair + Priority 0 direct URL/proxy/MFE-MAE repair
round_schedule_status: coverage_index_selected; local C15 max loop 83 -> selected loop 84; 직전 C10 loop 224 반복 회피
round_sector_consistency: pass
large_sector_id: L4_MATERIALS_SPREAD_RESOURCE
canonical_archetype_id: C15_MATERIAL_SPREAD_SUPERCYCLE
fine_archetype_id: C15_STEEL_CHEMICAL_FERTILIZER_PASSTHROUGH_LAG_AND_PHASE_GUARD
loop_objective: counterexample_mining; residual_false_positive_mining; direct_url_proxy_mfe_mae_repair; 4B_non_price_requirement_stress_test; canonical_archetype_compression
price_source: Songdaiki/stock-web
stock_web_manifest_max_date: 2026-02-20
production_scoring_changed: false
shadow_weight_only: true
output_file: e2r_stock_web_v12_residual_round_R4_loop_84_L4_MATERIALS_SPREAD_RESOURCE_C15_MATERIAL_SPREAD_SUPERCYCLE_research.md
```

This loop adds **8 new independent cases**, **4 counterexamples**, and **6 residual errors** for `L4_MATERIALS_SPREAD_RESOURCE/C15_MATERIAL_SPREAD_SUPERCYCLE`.

## 1. Current Calibrated Profile Assumption

Current proxy profile: `e2r_2_1_stock_web_calibrated_proxy`. The global calibration already contains `stage2_required_bridge`, `local_4b_watch_guard`, `full_4b_requires_non_price_evidence`, and hard 4C thesis-break routing. This MD does not loosen or patch production scoring. It tests a C15-specific residual: raw material movement is too often read as issuer margin conversion even when product pass-through, inventory lag, demand, and cash conversion are not yet visible.

## 2. Round / Large Sector / Canonical Archetype Scope

`C15_MATERIAL_SPREAD_SUPERCYCLE` maps to `R4 / L4_MATERIALS_SPREAD_RESOURCE`. The selected fine archetype is `C15_STEEL_CHEMICAL_FERTILIZER_PASSTHROUGH_LAG_AND_PHASE_GUARD`. This is not a current-stock scan and not an investment recommendation.

## 3. Previous Coverage / Duplicate Avoidance Check

The No-Repeat Index says C15 already has sufficient row volume but remains a Priority-1 quality target because spread reversal and inventory-cycle counterexamples need reinforcement. The current C15 top symbols in the cumulative table are `005490`, `004020`, `103140`, `018470`, `010130`, and `025820`; this loop avoids those top repeat symbols and uses eight different symbol/date/trigger-family combinations. Hard duplicate key check in this conversation-local archive: `canonical_archetype_id + symbol + trigger_type + entry_date = 0` duplicate hits.

## 4. Stock-Web OHLC Input / Price Source Validation

Stock-Web manifest basis used in this MD:

```text
source_name = FinanceData/marcap
price_adjustment_status = raw_unadjusted_marcap
min_date = 1995-05-02
max_date = 2026-02-20
tradable_row_count = 14354401
raw_row_count = 15214118
symbol_count = 5414
calibration_shard_root = atlas/ohlcv_tradable_by_symbol_year
schema_path = atlas/schema.json
price_basis = tradable_raw
```

## 5. Historical Eligibility Gate

All eight trigger rows have entry rows in Stock-Web tradable shards, at least 180 forward tradable rows, complete 30D/90D/180D MFE and MAE fields, and no 180D stock-count drift above the 20% corporate-action contamination gate.

## 6. Canonical Archetype Compression Map

C15 rows are compressed into five evidence links:

1. Raw-material or commodity-weather headline.
2. Product price / ASP pass-through.
3. Demand, shipment, or customer route.
4. Realized margin / working-capital / cash conversion.
5. Inventory-lag and price-phase sanity.

Raw material news is only the pressure gauge. Promotion should ask whether the pressure reaches the issuer’s income statement.

## 7. Case Selection Summary

| case_id | symbol | company | trigger_type | entry_date | entry_price | MFE30 | MFE90 | MFE180 | MAE30 | MAE90 | MAE180 | outcome | verdict |
|---|---:|---|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| C15L84_001430_20240802 | 001430 | SeAH Besteel Holdings | Stage2-Actionable | 2024-08-02 | 19480 | 4.21 | 30.39 | 30.39 | -14.58 | -14.58 | -24.28 | special_steel_margin_bridge_high_mae_success | current_profile_correct |
| C15L84_003030_20241115 | 003030 | SeAH Steel Holdings | Stage2-Actionable | 2024-11-15 | 162100 | 20.91 | 80.44 | 80.44 | -2.59 | -2.59 | -2.59 | octg_export_route_after_reset_positive | current_profile_missed_structural |
| C15L84_002240_20240516 | 002240 | KISWIRE / Korea Steel Wire | Stage2 | 2024-05-16 | 24350 | 1.64 | 1.64 | 1.64 | -10.68 | -24.85 | -28.75 | wire_material_price_proxy_failed_conversion | current_profile_false_positive |
| C15L84_025860_20240112 | 025860 | Namhae Chemical | Stage2 | 2024-01-12 | 7570 | 2.38 | 2.38 | 2.38 | -4.62 | -9.11 | -18.1 | fertilizer_spread_normalization_demand_gap_counterexample | current_profile_false_positive |
| C15L84_001390_20250401 | 001390 | KG Chemical | Stage2-Actionable | 2025-04-01 | 3625 | 11.31 | 43.45 | 67.17 | -6.76 | -6.76 | -6.76 | chemical_fertilizer_reset_positive | current_profile_too_late |
| C15L84_002710_20240308 | 002710 | TCC Steel | Stage4B | 2024-03-08 | 63700 | 7.38 | 7.38 | 7.38 | -21.04 | -35.16 | -57.61 | tinplate_nickel_sheet_after_rerating_4b_success | current_profile_4B_too_late |
| C15L84_007690_20240216 | 007690 | KUKDO Chemical | Stage2 | 2024-02-16 | 39850 | 4.64 | 4.64 | 4.64 | -6.4 | -14.05 | -24.34 | epoxy_spread_stale_result_false_positive | current_profile_false_positive |
| C15L84_004890_20241115 | 004890 | Dongil Industries | Stage2-Actionable | 2024-11-15 | 38200 | 3.93 | 9.69 | 23.69 | -2.23 | -2.23 | -2.23 | special_bar_ferroalloy_reset_stage2_positive | current_profile_correct |


## 8. Positive vs Counterexample Balance

Positive cases: `4`. Counterexamples: `4`. 4B/watch overlay rows: `1`. Hard 4C rows: `0` because none of the selected rows proves durable thesis death; high MAE is handled as watch/cap unless the route dies.

## 9. Evidence Source Map

| symbol | source family | source URL / note | directness |
|---:|---|---|---|
| 001430 | special_steel_result_margin_bridge | SeAH Besteel 2Q24 result / analyst source: file.myasset 2024-08-02, https://file.myasset.com/sitemanager/upload/2024/0801/140214/20240801140214903_0_ko.pdf | direct_or_named_source_with_proxy_context |
| 003030 | octg_export_route_after_margin_reset | SeAH Steel Holdings 3Q24 result article: https://press.todayan.com/newsRead.php?no=1000810 | direct_or_named_source_with_proxy_context |
| 002240 | source_proxy_raw_material_price_only_without_conversion | KISWIRE 2024 business report / raw-material disclosure: https://www.kiswire.com/bbs/board.php?bo_table=notice&device=pc&wr_id=15 | direct_or_named_source_with_proxy_context |
| 025860 | fertilizer_spread_normalization_without_demand_bridge | Namhae Chemical KIRS report 2024-01-12: https://ssl.pstatic.net/imgstock/upload/research/company/1705023719958.pdf | direct_or_named_source_with_proxy_context |
| 001390 | company_valueup_direct_route_after_reset | KG Chemical KIRS value-up report 2025-04-01: https://w4.kirs.or.kr/download/valueup/250401_KG%EC%BC%80%EB%AF%B8%EC%B9%BC%28%EB%B0%B8%EB%A5%98%EC%97%85%29.pdf | direct_or_named_source_with_proxy_context |
| 002710 | tinplate_demand_and_financial_health_warning_after_rerating | TCC Steel IBTomato article 2024-03-08: https://www.ibtomato.com/ExternalView.aspx?no=11719&type=1 | direct_or_named_source_with_proxy_context |
| 007690 | epoxy_spread_downward_stabilization_counterexample | KUKDO Chemical KIRS report 2024-02-16: https://ssl.pstatic.net/imgstock/upload/research/company/1708038661744.pdf | direct_or_named_source_with_proxy_context |
| 004890 | official_business_report_low_phase_direct_material_route | Dongil Industries financial report list / business report: https://www.dongil.co.kr/bizdemo55059/menu05/page01.php?com_board_basic=read_form&com_board_id=13&com_board_id=13&com_board_idx=30&com_board_page=&com_board_search_code=&com_board_search_value1=&com_board_search_value2= | direct_or_named_source_with_proxy_context |


## 10. Price Data Source Map

| symbol | primary shard | entry_date | entry_price | shares drift in 180D | corporate action gate |
|---:|---|---:|---:|---:|---|
| 001430 | `atlas/ohlcv_tradable_by_symbol_year/001/001430/2024.csv` | 2024-08-02 | 19480 | 0.0% | clean_180D_window |
| 003030 | `atlas/ohlcv_tradable_by_symbol_year/003/003030/2024.csv` | 2024-11-15 | 162100 | 0.0% | clean_180D_window |
| 002240 | `atlas/ohlcv_tradable_by_symbol_year/002/002240/2024.csv` | 2024-05-16 | 24350 | 8.0% | clean_180D_window |
| 025860 | `atlas/ohlcv_tradable_by_symbol_year/025/025860/2024.csv` | 2024-01-12 | 7570 | 0.0% | clean_180D_window |
| 001390 | `atlas/ohlcv_tradable_by_symbol_year/001/001390/2025.csv` | 2025-04-01 | 3625 | 1.84% | clean_180D_window |
| 002710 | `atlas/ohlcv_tradable_by_symbol_year/002/002710/2024.csv` | 2024-03-08 | 63700 | 0.0% | clean_180D_window |
| 007690 | `atlas/ohlcv_tradable_by_symbol_year/007/007690/2024.csv` | 2024-02-16 | 39850 | 0.0% | clean_180D_window |
| 004890 | `atlas/ohlcv_tradable_by_symbol_year/004/004890/2024.csv` | 2024-11-15 | 38200 | 0.0% | clean_180D_window |


## 11. Case-by-Case Trigger Grid

- `001430`: direct special-steel result/margin evidence after a weak phase worked, but the later drawdown shows why Green should wait for fresh margin/cash.
- `003030`: weak headline result did not kill the direct OCTG/export route; price reset created the best positive asymmetry in this loop.
- `002240`: raw-material and business-description evidence lacked a visible pass-through bridge; it is a clean source-proxy counterexample.
- `025860`: fertilizer spread normalization was not enough without demand/offtake strength.
- `001390`: post-reset direct route and value-up style evidence worked as Stage2-Actionable, not Green.
- `002710`: after rerating, product-route optimism needed 4B-watch because financial/competition risk dominated.
- `007690`: epoxy spread normalization was stale; BPA/ECH pressure and supply-demand weakness kept the row below promotion quality.
- `004890`: low-phase business-route evidence supports Stage2 after reset, but not Green.

## 12. Trigger-Level OHLC Backtest Tables

| case_id | symbol | company | trigger_type | entry_date | entry_price | MFE30 | MFE90 | MFE180 | MAE30 | MAE90 | MAE180 | outcome | verdict |
|---|---:|---|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| C15L84_001430_20240802 | 001430 | SeAH Besteel Holdings | Stage2-Actionable | 2024-08-02 | 19480 | 4.21 | 30.39 | 30.39 | -14.58 | -14.58 | -24.28 | special_steel_margin_bridge_high_mae_success | current_profile_correct |
| C15L84_003030_20241115 | 003030 | SeAH Steel Holdings | Stage2-Actionable | 2024-11-15 | 162100 | 20.91 | 80.44 | 80.44 | -2.59 | -2.59 | -2.59 | octg_export_route_after_reset_positive | current_profile_missed_structural |
| C15L84_002240_20240516 | 002240 | KISWIRE / Korea Steel Wire | Stage2 | 2024-05-16 | 24350 | 1.64 | 1.64 | 1.64 | -10.68 | -24.85 | -28.75 | wire_material_price_proxy_failed_conversion | current_profile_false_positive |
| C15L84_025860_20240112 | 025860 | Namhae Chemical | Stage2 | 2024-01-12 | 7570 | 2.38 | 2.38 | 2.38 | -4.62 | -9.11 | -18.1 | fertilizer_spread_normalization_demand_gap_counterexample | current_profile_false_positive |
| C15L84_001390_20250401 | 001390 | KG Chemical | Stage2-Actionable | 2025-04-01 | 3625 | 11.31 | 43.45 | 67.17 | -6.76 | -6.76 | -6.76 | chemical_fertilizer_reset_positive | current_profile_too_late |
| C15L84_002710_20240308 | 002710 | TCC Steel | Stage4B | 2024-03-08 | 63700 | 7.38 | 7.38 | 7.38 | -21.04 | -35.16 | -57.61 | tinplate_nickel_sheet_after_rerating_4b_success | current_profile_4B_too_late |
| C15L84_007690_20240216 | 007690 | KUKDO Chemical | Stage2 | 2024-02-16 | 39850 | 4.64 | 4.64 | 4.64 | -6.4 | -14.05 | -24.34 | epoxy_spread_stale_result_false_positive | current_profile_false_positive |
| C15L84_004890_20241115 | 004890 | Dongil Industries | Stage2-Actionable | 2024-11-15 | 38200 | 3.93 | 9.69 | 23.69 | -2.23 | -2.23 | -2.23 | special_bar_ferroalloy_reset_stage2_positive | current_profile_correct |


## 13. Current Calibrated Profile Stress Test

Current profile residual errors found:

- `raw_material_proxy_false_positive`: `002240`, `025860`, `007690`.
- `after-rerating direct route 4B too late`: `002710`.
- `missed direct route after reset`: `003030`, partially `001390`.
- `high-MAE live-route ambiguity`: `001430`.

The Stage2 bridge axis is directionally right, but C15 needs a sharper material-spread bridge: raw commodity movement must not receive the same confidence as product ASP pass-through plus realized margin/cash.

## 14. Stage2 / Yellow / Green Comparison

No Stage3-Green row is proposed. The loop explicitly avoids outcome-based Green labels. For C15, Green should require at least one of: realized margin expansion, forward spread freshness, cash conversion, or repeat customer/demand visibility. Stage2-Actionable is still allowed after price reset when the issuer route is direct.

## 15. 4B Local vs Full-window Timing Audit

`002710` is the cleanest 4B/watch row: product-route optimism existed, but the entry came after a major rerating with financial/competition risk visible. It produced MFE180 of `7.38`% and MAE180 of `-57.61`%, so the guard should cap promotion rather than wait for hard thesis death.

Rows with deep MAE but surviving route, such as `001430`, should become local 4B/watch, not automatic 4C.

## 16. 4C Protection Audit

No selected row has confirmed thesis death. `hard_4c_thesis_break_routes_to_4c` is kept, but weakened only for C15 high-MAE rows where the customer/product route survives. In this loop, severe MAE is a smoke alarm, not the fire itself.

## 17. Sector-Specific Rule Candidate

`L4_MATERIALS_SPREAD_RESOURCE` rows should split commodity weather, product price or ASP pass-through, inventory-cost lag, demand/customer route, realized margin/cash conversion, and price phase.

## 18. Canonical-Archetype Rule Candidate

`C15_MATERIAL_SPREAD_SUPERCYCLE` should use a pass-through and inventory-lag ladder:

`raw-material headline → product price or ASP pass-through → demand/customer/shipment route → realized margin/cash conversion → inventory-lag and price-phase sanity`.

Raw commodity proxy alone stays Stage2-watch. Product-route after reset can become Stage2-Actionable. Result-only rows after rerating are capped below Green. High-MAE rows with live issuer route become 4B-watch before hard 4C.

## 19. Before / After Backtest Comparison

| profile_id | scope | hypothesis | avg_MFE90 | avg_MAE90 | avg_MFE180 | avg_MAE180 | verdict |
|---|---|---|---:|---:|---:|---:|---|
| P0_e2r_2_1_stock_web_calibrated_proxy | current_proxy | Current calibrated profile with global bridge and 4B guards. | 22.5 | -13.67 | 27.22 | -20.58 | mixed; too much credit for raw-spread proxy rows |
| P1_L4_sector_spread_freshness_profile | sector_specific | L4 rows require product pass-through plus demand/customer route before promotion. | 40.99 | -6.54 | 50.42 | -8.96 | better after separating direct route from raw proxy |
| P2_C15_passthrough_inventory_phase_guard | canonical_archetype_specific | C15 promotion ladder = raw material -> product pass-through -> demand/customer route -> realized margin/cash -> price phase. | 4.01 | -20.79 | 4.01 | -32.2 | best for C15-specific counterexample control |
| P3_C15_high_MAE_live_route_watch_guard | counterexample_guard | High MAE with surviving route becomes 4B-watch, not hard 4C. | 11.01 | -22.16 | 11.01 | -33.74 | useful guardrail; not a promotion rule |


## 20. Score-Return Alignment Matrix

The counterexamples had average MFE90 of `4.01`% and average MAE90 of `-20.79`%. The positives had average MFE90 of `40.99`% and average MAE90 of `-6.54`%. That split is explained better by pass-through/finality/phase than by raw material headline alone.

## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive_case_count | counterexample_count | 4B_case_count | 4C_case_count | new_independent_case_count | reused_case_count | calibration_usable_trigger_count | representative_trigger_count | current_profile_error_count | sector_rule_candidate | canonical_rule_candidate | coverage_gap_after_this_loop |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| L4_MATERIALS_SPREAD_RESOURCE | C15_MATERIAL_SPREAD_SUPERCYCLE | C15_STEEL_CHEMICAL_FERTILIZER_PASSTHROUGH_LAG_AND_PHASE_GUARD | 4 | 4 | 1 | 0 | 8 | 0 | 8 | 8 | 6 | L4 spread rows require pass-through / inventory-lag / demand-route separation | C15 pass-through inventory phase guard | URL/proxy and direct MFE-MAE repair improved with 8 clean trigger rows |


## 22. Residual Contribution Summary

```yaml
new_independent_case_count: 8
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 8
new_canonical_archetype_count: 0
new_fine_archetype_count: 1
new_trigger_family_count: 8
tested_existing_calibrated_axes:
  - stage2_required_bridge
  - local_4b_watch_guard
  - full_4b_requires_non_price_evidence
  - hard_4c_thesis_break_routes_to_4c
residual_error_types_found:
  - raw_material_proxy_false_positive
  - inventory_lag_damage
  - product_pass_through_missing
  - high_MAE_live_route_not_hard4C
  - direct_route_after_reset_missed_structural
new_axis_proposed: c15_passthrough_inventory_phase_guard
existing_axis_strengthened: stage2_required_bridge; local_4b_watch_guard; stage3_green_revision_min_by_margin_cash_freshness
existing_axis_weakened: hard_4c_thesis_break_routes_to_4c qualified for high-MAE rows with surviving issuer route only
existing_axis_kept: full_4b_requires_non_price_evidence
sector_specific_rule_candidate: L4 material-spread rows require pass-through / demand-route / inventory-lag separation
canonical_archetype_rule_candidate: C15 pass-through inventory-lag phase ladder
no_new_signal_reason: null
loop_contribution_label: canonical_archetype_rule_candidate
do_not_propose_new_weight_delta: false
```

## 23. Validation Scope / Non-Validation Scope

Validated: historical 1D OHLC rows from Stock-Web, entry close, 30D/90D/180D MFE/MAE, 180D stock-count contamination gate, C15-specific evidence compression.

Not validated: live candidates, present-day recommendation, production scoring code, broker API, order execution, full audited financial restatement logic, and post-2026-02-20 price path.

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,c15_passthrough_inventory_phase_guard,canonical_archetype_specific,L4_MATERIALS_SPREAD_RESOURCE,C15_MATERIAL_SPREAD_SUPERCYCLE,0,1,+1,"Raw material headline must be separated from product price pass-through, demand/customer route, inventory lag, and realized margin/cash.","4 positive direct-route rows preserved; 4 raw-proxy/lag counterexamples capped.","TRG_C15L84_001430_20240802_Stage2Actionable|TRG_C15L84_003030_20241115_Stage2Actionable|TRG_C15L84_002240_20240516_Stage2|TRG_C15L84_025860_20240112_Stage2|TRG_C15L84_001390_20250401_Stage2Actionable|TRG_C15L84_002710_20240308_Stage4B|TRG_C15L84_007690_20240216_Stage2|TRG_C15L84_004890_20241115_Stage2Actionable",8,8,4,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,high_mae_live_route_not_hard4c_guard,canonical_archetype_specific,L4_MATERIALS_SPREAD_RESOURCE,C15_MATERIAL_SPREAD_SUPERCYCLE,0,1,+1,"High MAE alone should not force hard 4C if issuer route survives; route-only rows should be watch/cap.","prevents over-routing 001430 and selected reset cases to hard thesis death.","TRG_C15L84_001430_20240802_Stage2Actionable|TRG_C15L84_002240_20240516_Stage2|TRG_C15L84_002710_20240308_Stage4B|TRG_C15L84_007690_20240216_Stage2",5,5,3,low,guardrail_shadow_only,"qualify hard_4c only; no production change"
```

## 25. Machine-Readable Rows

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
{"row_type":"case","case_id":"C15L84_001430_20240802","symbol":"001430","company_name":"SeAH Besteel Holdings","round":"R4","loop":"84","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C15_MATERIAL_SPREAD_SUPERCYCLE","fine_archetype_id":"C15_STEEL_CHEMICAL_FERTILIZER_PASSTHROUGH_LAG_AND_PHASE_GUARD","case_type":"high_mae_success","positive_or_counterexample":"positive","best_trigger":"TRG_C15L84_001430_20240802_Stage2Actionable","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"aligned","current_profile_verdict":"current_profile_correct","price_source":"Songdaiki/stock-web","notes":"Scrap/alloy-cost relief and sales mix supported a Stage2-Actionable entry, but later drawdown shows why Green needs fresh margin/cash confirmation."}
{"row_type":"trigger","trigger_id":"TRG_C15L84_001430_20240802_Stage2Actionable","case_id":"C15L84_001430_20240802","symbol":"001430","company_name":"SeAH Besteel Holdings","round":"R4","loop":"84","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C15_MATERIAL_SPREAD_SUPERCYCLE","fine_archetype_id":"C15_STEEL_CHEMICAL_FERTILIZER_PASSTHROUGH_LAG_AND_PHASE_GUARD","sector":"special_steel_alloy_bar","primary_archetype":"special_steel_scrap_alloy_spread_passthrough","loop_objective":"counterexample_mining; residual_false_positive_mining; direct_url_proxy_mfe_mae_repair; 4B_non_price_requirement_stress_test; canonical_archetype_compression","trigger_type":"Stage2-Actionable","trigger_date":"2024-08-01","evidence_available_at_that_date":"2Q24 result note available around 2024-08-01/02; entry uses 2024-08-02 close.","evidence_source":"SeAH Besteel 2Q24 result / analyst source: file.myasset 2024-08-02, https://file.myasset.com/sitemanager/upload/2024/0801/140214/20240801140214903_0_ko.pdf","stage2_evidence_fields":["public_event_or_disclosure","customer_or_order_quality","capacity_or_volume_route"],"stage3_evidence_fields":["margin_bridge","financial_visibility","multiple_public_sources"],"stage4b_evidence_fields":["margin_or_backlog_slowdown","price_only_local_peak"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/001/001430/2024.csv","profile_path":"atlas/symbol_profiles/001/001430.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-08-02","entry_price":19480.0,"MFE_30D_pct":4.21,"MFE_90D_pct":30.39,"MFE_180D_pct":30.39,"MFE_1Y_pct":80.44,"MFE_2Y_pct":null,"MAE_30D_pct":-14.58,"MAE_90D_pct":-14.58,"MAE_180D_pct":-24.28,"MAE_1Y_pct":-24.28,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-11-12","peak_price":25400.0,"drawdown_after_peak_pct":-41.93,"green_lateness_ratio":null,"four_b_local_peak_proximity":0.55,"four_b_full_window_peak_proximity":0.34,"four_b_timing_verdict":"local_4B_watch_only","four_b_evidence_type":["margin_or_backlog_slowdown","price_only_local_peak"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"special_steel_margin_bridge_high_mae_success","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window; shares_drift=0.0pct_under_20pct_gate","same_entry_group_id":"SEG_C15L84_001430_20240802","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C15L84_001430_20240802","trigger_id":"TRG_C15L84_001430_20240802_Stage2Actionable","symbol":"001430","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C15_MATERIAL_SPREAD_SUPERCYCLE","raw_component_scores_before":{"contract_score":58,"backlog_visibility_score":35,"margin_bridge_score":58,"revision_score":45,"relative_strength_score":55,"customer_quality_score":56,"policy_or_regulatory_score":15,"valuation_repricing_score":50,"execution_risk_score":30,"legal_or_contract_risk_score":15,"dilution_cb_risk_score":18,"accounting_trust_risk_score":15},"weighted_score_before":58.16,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"contract_score":58,"backlog_visibility_score":35,"margin_bridge_score":66,"revision_score":45,"relative_strength_score":55,"customer_quality_score":62,"policy_or_regulatory_score":15,"valuation_repricing_score":50,"execution_risk_score":25,"legal_or_contract_risk_score":15,"dilution_cb_risk_score":18,"accounting_trust_risk_score":15},"weighted_score_after":61.13,"stage_label_after":"Stage2-Actionable","changed_components":["margin_bridge_score","customer_quality_score","execution_risk_score","valuation_repricing_score"],"component_delta_explanation":"C15 shadow profile separates raw commodity headline from product pass-through, demand/customer route, realized margin/cash, and local price phase. Counterexamples are capped; post-reset direct-route positives remain eligible.","MFE_90D_pct":30.39,"MAE_90D_pct":-14.58,"score_return_alignment_label":"aligned","current_profile_verdict":"current_profile_correct"}
{"row_type":"case","case_id":"C15L84_003030_20241115","symbol":"003030","company_name":"SeAH Steel Holdings","round":"R4","loop":"84","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C15_MATERIAL_SPREAD_SUPERCYCLE","fine_archetype_id":"C15_STEEL_CHEMICAL_FERTILIZER_PASSTHROUGH_LAG_AND_PHASE_GUARD","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"TRG_C15L84_003030_20241115_Stage2Actionable","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"aligned","current_profile_verdict":"current_profile_missed_structural","price_source":"Songdaiki/stock-web","notes":"The headline result was weak, but the direct OCTG/export route and reset price phase later produced strong asymmetry."}
{"row_type":"trigger","trigger_id":"TRG_C15L84_003030_20241115_Stage2Actionable","case_id":"C15L84_003030_20241115","symbol":"003030","company_name":"SeAH Steel Holdings","round":"R4","loop":"84","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C15_MATERIAL_SPREAD_SUPERCYCLE","fine_archetype_id":"C15_STEEL_CHEMICAL_FERTILIZER_PASSTHROUGH_LAG_AND_PHASE_GUARD","sector":"steel_pipe_octg_export","primary_archetype":"octg_pipe_price_and_export_route","loop_objective":"counterexample_mining; residual_false_positive_mining; direct_url_proxy_mfe_mae_repair; 4B_non_price_requirement_stress_test; canonical_archetype_compression","trigger_type":"Stage2-Actionable","trigger_date":"2024-11-14","evidence_available_at_that_date":"3Q24 result was public on 2024-11-14; entry uses next tradable close 2024-11-15.","evidence_source":"SeAH Steel Holdings 3Q24 result article: https://press.todayan.com/newsRead.php?no=1000810","stage2_evidence_fields":["public_event_or_disclosure","customer_or_order_quality","backlog_or_delivery_visibility"],"stage3_evidence_fields":["durable_customer_confirmation","financial_visibility"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/003/003030/2024.csv","profile_path":"atlas/symbol_profiles/003/003030.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-11-15","entry_price":162100.0,"MFE_30D_pct":20.91,"MFE_90D_pct":80.44,"MFE_180D_pct":80.44,"MFE_1Y_pct":80.44,"MFE_2Y_pct":null,"MAE_30D_pct":-2.59,"MAE_90D_pct":-2.59,"MAE_180D_pct":-2.59,"MAE_1Y_pct":-18.38,"below_entry_price_flag_30D":false,"below_entry_price_flag_90D":false,"peak_date":"2025-03-06","peak_price":292500.0,"drawdown_after_peak_pct":-35.35,"green_lateness_ratio":null,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_applicable","four_b_evidence_type":[],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"octg_export_route_after_reset_positive","current_profile_verdict":"current_profile_missed_structural","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window; shares_drift=0.0pct_under_20pct_gate","same_entry_group_id":"SEG_C15L84_003030_20241115","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C15L84_003030_20241115","trigger_id":"TRG_C15L84_003030_20241115_Stage2Actionable","symbol":"003030","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C15_MATERIAL_SPREAD_SUPERCYCLE","raw_component_scores_before":{"contract_score":58,"backlog_visibility_score":50,"margin_bridge_score":58,"revision_score":45,"relative_strength_score":55,"customer_quality_score":56,"policy_or_regulatory_score":15,"valuation_repricing_score":30,"execution_risk_score":30,"legal_or_contract_risk_score":15,"dilution_cb_risk_score":18,"accounting_trust_risk_score":15},"weighted_score_before":61.96,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"contract_score":58,"backlog_visibility_score":50,"margin_bridge_score":66,"revision_score":45,"relative_strength_score":55,"customer_quality_score":62,"policy_or_regulatory_score":15,"valuation_repricing_score":30,"execution_risk_score":25,"legal_or_contract_risk_score":15,"dilution_cb_risk_score":18,"accounting_trust_risk_score":15},"weighted_score_after":64.93,"stage_label_after":"Stage2-Actionable","changed_components":["margin_bridge_score","customer_quality_score","execution_risk_score","valuation_repricing_score"],"component_delta_explanation":"C15 shadow profile separates raw commodity headline from product pass-through, demand/customer route, realized margin/cash, and local price phase. Counterexamples are capped; post-reset direct-route positives remain eligible.","MFE_90D_pct":80.44,"MAE_90D_pct":-2.59,"score_return_alignment_label":"aligned","current_profile_verdict":"current_profile_missed_structural"}
{"row_type":"case","case_id":"C15L84_002240_20240516","symbol":"002240","company_name":"KISWIRE / Korea Steel Wire","round":"R4","loop":"84","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C15_MATERIAL_SPREAD_SUPERCYCLE","fine_archetype_id":"C15_STEEL_CHEMICAL_FERTILIZER_PASSTHROUGH_LAG_AND_PHASE_GUARD","case_type":"failed_rerating","positive_or_counterexample":"counterexample","best_trigger":"TRG_C15L84_002240_20240516_Stage2","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"aligned","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"Material-cost disclosure alone was not enough; no clean pass-through or order/margin bridge appeared within the calibration window."}
{"row_type":"trigger","trigger_id":"TRG_C15L84_002240_20240516_Stage2","case_id":"C15L84_002240_20240516","symbol":"002240","company_name":"KISWIRE / Korea Steel Wire","round":"R4","loop":"84","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C15_MATERIAL_SPREAD_SUPERCYCLE","fine_archetype_id":"C15_STEEL_CHEMICAL_FERTILIZER_PASSTHROUGH_LAG_AND_PHASE_GUARD","sector":"wire_rope_and_special_wire","primary_archetype":"wire_material_cost_passthrough","loop_objective":"counterexample_mining; residual_false_positive_mining; direct_url_proxy_mfe_mae_repair; 4B_non_price_requirement_stress_test; canonical_archetype_compression","trigger_type":"Stage2","trigger_date":"2024-05-15","evidence_available_at_that_date":"Q1/regular filing window proxy; entry uses 2024-05-16 close.","evidence_source":"KISWIRE 2024 business report / raw-material disclosure: https://www.kiswire.com/bbs/board.php?bo_table=notice&device=pc&wr_id=15","stage2_evidence_fields":["public_event_or_disclosure"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["margin_or_backlog_slowdown","price_only_local_peak"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/002/002240/2024.csv","profile_path":"atlas/symbol_profiles/002/002240.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-05-16","entry_price":24350.0,"MFE_30D_pct":1.64,"MFE_90D_pct":1.64,"MFE_180D_pct":1.64,"MFE_1Y_pct":1.64,"MFE_2Y_pct":null,"MAE_30D_pct":-10.68,"MAE_90D_pct":-24.85,"MAE_180D_pct":-28.75,"MAE_1Y_pct":-34.5,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-05-16","peak_price":24750.0,"drawdown_after_peak_pct":-29.9,"green_lateness_ratio":null,"four_b_local_peak_proximity":0.55,"four_b_full_window_peak_proximity":0.92,"four_b_timing_verdict":"local_4B_watch_only","four_b_evidence_type":["margin_or_backlog_slowdown","price_only_local_peak"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"wire_material_price_proxy_failed_conversion","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window; shares_drift=8.0pct_under_20pct_gate","same_entry_group_id":"SEG_C15L84_002240_20240516","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C15L84_002240_20240516","trigger_id":"TRG_C15L84_002240_20240516_Stage2","symbol":"002240","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C15_MATERIAL_SPREAD_SUPERCYCLE","raw_component_scores_before":{"contract_score":40,"backlog_visibility_score":35,"margin_bridge_score":28,"revision_score":25,"relative_strength_score":25,"customer_quality_score":32,"policy_or_regulatory_score":15,"valuation_repricing_score":50,"execution_risk_score":65,"legal_or_contract_risk_score":15,"dilution_cb_risk_score":18,"accounting_trust_risk_score":15},"weighted_score_before":39.39,"stage_label_before":"Stage2-watch","raw_component_scores_after":{"contract_score":40,"backlog_visibility_score":35,"margin_bridge_score":16,"revision_score":25,"relative_strength_score":25,"customer_quality_score":24,"policy_or_regulatory_score":15,"valuation_repricing_score":58,"execution_risk_score":75,"legal_or_contract_risk_score":15,"dilution_cb_risk_score":18,"accounting_trust_risk_score":15},"weighted_score_after":33.93,"stage_label_after":"Stage2-watch","changed_components":["margin_bridge_score","customer_quality_score","execution_risk_score","valuation_repricing_score"],"component_delta_explanation":"C15 shadow profile separates raw commodity headline from product pass-through, demand/customer route, realized margin/cash, and local price phase. Counterexamples are capped; post-reset direct-route positives remain eligible.","MFE_90D_pct":1.64,"MAE_90D_pct":-24.85,"score_return_alignment_label":"aligned","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"case","case_id":"C15L84_025860_20240112","symbol":"025860","company_name":"Namhae Chemical","round":"R4","loop":"84","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C15_MATERIAL_SPREAD_SUPERCYCLE","fine_archetype_id":"C15_STEEL_CHEMICAL_FERTILIZER_PASSTHROUGH_LAG_AND_PHASE_GUARD","case_type":"failed_rerating","positive_or_counterexample":"counterexample","best_trigger":"TRG_C15L84_025860_20240112_Stage2","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"mixed","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"Spread normalization narrative had no issuer-level demand/offtake bridge; MFE stayed shallow and MAE deepened over 180D."}
{"row_type":"trigger","trigger_id":"TRG_C15L84_025860_20240112_Stage2","case_id":"C15L84_025860_20240112","symbol":"025860","company_name":"Namhae Chemical","round":"R4","loop":"84","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C15_MATERIAL_SPREAD_SUPERCYCLE","fine_archetype_id":"C15_STEEL_CHEMICAL_FERTILIZER_PASSTHROUGH_LAG_AND_PHASE_GUARD","sector":"fertilizer_ammonia_urea","primary_archetype":"fertilizer_product_raw_material_spread","loop_objective":"counterexample_mining; residual_false_positive_mining; direct_url_proxy_mfe_mae_repair; 4B_non_price_requirement_stress_test; canonical_archetype_compression","trigger_type":"Stage2","trigger_date":"2024-01-12","evidence_available_at_that_date":"Report was dated 2024-01-12; entry uses 2024-01-12 close.","evidence_source":"Namhae Chemical KIRS report 2024-01-12: https://ssl.pstatic.net/imgstock/upload/research/company/1705023719958.pdf","stage2_evidence_fields":["public_event_or_disclosure","policy_or_regulatory_optionality"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["margin_or_backlog_slowdown"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/025/025860/2024.csv","profile_path":"atlas/symbol_profiles/025/025860.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-01-12","entry_price":7570.0,"MFE_30D_pct":2.38,"MFE_90D_pct":2.38,"MFE_180D_pct":2.38,"MFE_1Y_pct":2.38,"MFE_2Y_pct":null,"MAE_30D_pct":-4.62,"MAE_90D_pct":-9.11,"MAE_180D_pct":-18.1,"MAE_1Y_pct":-21.27,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-01-18","peak_price":7750.0,"drawdown_after_peak_pct":-20.0,"green_lateness_ratio":null,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_applicable","four_b_evidence_type":[],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"fertilizer_spread_normalization_demand_gap_counterexample","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window; shares_drift=0.0pct_under_20pct_gate","same_entry_group_id":"SEG_C15L84_025860_20240112","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C15L84_025860_20240112","trigger_id":"TRG_C15L84_025860_20240112_Stage2","symbol":"025860","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C15_MATERIAL_SPREAD_SUPERCYCLE","raw_component_scores_before":{"contract_score":40,"backlog_visibility_score":35,"margin_bridge_score":28,"revision_score":25,"relative_strength_score":25,"customer_quality_score":32,"policy_or_regulatory_score":35,"valuation_repricing_score":30,"execution_risk_score":65,"legal_or_contract_risk_score":15,"dilution_cb_risk_score":18,"accounting_trust_risk_score":15},"weighted_score_before":41.39,"stage_label_before":"Stage2-watch","raw_component_scores_after":{"contract_score":40,"backlog_visibility_score":35,"margin_bridge_score":16,"revision_score":25,"relative_strength_score":25,"customer_quality_score":24,"policy_or_regulatory_score":35,"valuation_repricing_score":38,"execution_risk_score":75,"legal_or_contract_risk_score":15,"dilution_cb_risk_score":18,"accounting_trust_risk_score":15},"weighted_score_after":35.93,"stage_label_after":"Stage2-watch","changed_components":["margin_bridge_score","customer_quality_score","execution_risk_score","valuation_repricing_score"],"component_delta_explanation":"C15 shadow profile separates raw commodity headline from product pass-through, demand/customer route, realized margin/cash, and local price phase. Counterexamples are capped; post-reset direct-route positives remain eligible.","MFE_90D_pct":2.38,"MAE_90D_pct":-9.11,"score_return_alignment_label":"mixed","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"case","case_id":"C15L84_001390_20250401","symbol":"001390","company_name":"KG Chemical","round":"R4","loop":"84","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C15_MATERIAL_SPREAD_SUPERCYCLE","fine_archetype_id":"C15_STEEL_CHEMICAL_FERTILIZER_PASSTHROUGH_LAG_AND_PHASE_GUARD","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"TRG_C15L84_001390_20250401_Stage2Actionable","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"aligned","current_profile_verdict":"current_profile_too_late","price_source":"Songdaiki/stock-web","notes":"After price reset, a direct business-route report produced good 90/180D asymmetry; generic proxy caps would have been too conservative."}
{"row_type":"trigger","trigger_id":"TRG_C15L84_001390_20250401_Stage2Actionable","case_id":"C15L84_001390_20250401","symbol":"001390","company_name":"KG Chemical","round":"R4","loop":"84","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C15_MATERIAL_SPREAD_SUPERCYCLE","fine_archetype_id":"C15_STEEL_CHEMICAL_FERTILIZER_PASSTHROUGH_LAG_AND_PHASE_GUARD","sector":"fertilizer_and_construction_chemical","primary_archetype":"fertilizer_construction_chemical_margin_recovery","loop_objective":"counterexample_mining; residual_false_positive_mining; direct_url_proxy_mfe_mae_repair; 4B_non_price_requirement_stress_test; canonical_archetype_compression","trigger_type":"Stage2-Actionable","trigger_date":"2025-04-01","evidence_available_at_that_date":"KIRS value-up report dated 2025-04-01; entry uses 2025-04-01 close.","evidence_source":"KG Chemical KIRS value-up report 2025-04-01: https://w4.kirs.or.kr/download/valueup/250401_KG%EC%BC%80%EB%AF%B8%EC%B9%BC%28%EB%B0%B8%EB%A5%98%EC%97%85%29.pdf","stage2_evidence_fields":["public_event_or_disclosure","customer_or_order_quality","capacity_or_volume_route"],"stage3_evidence_fields":["financial_visibility","multiple_public_sources"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/001/001390/2025.csv","profile_path":"atlas/symbol_profiles/001/001390.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2025-04-01","entry_price":3625.0,"MFE_30D_pct":11.31,"MFE_90D_pct":43.45,"MFE_180D_pct":67.17,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-6.76,"MAE_90D_pct":-6.76,"MAE_180D_pct":-6.76,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2025-11-13","peak_price":6060.0,"drawdown_after_peak_pct":-17.49,"green_lateness_ratio":null,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_applicable","four_b_evidence_type":[],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"chemical_fertilizer_reset_positive","current_profile_verdict":"current_profile_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window; shares_drift=1.84pct_under_20pct_gate","same_entry_group_id":"SEG_C15L84_001390_20250401","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C15L84_001390_20250401","trigger_id":"TRG_C15L84_001390_20250401_Stage2Actionable","symbol":"001390","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C15_MATERIAL_SPREAD_SUPERCYCLE","raw_component_scores_before":{"contract_score":58,"backlog_visibility_score":35,"margin_bridge_score":58,"revision_score":45,"relative_strength_score":55,"customer_quality_score":56,"policy_or_regulatory_score":15,"valuation_repricing_score":30,"execution_risk_score":30,"legal_or_contract_risk_score":15,"dilution_cb_risk_score":18,"accounting_trust_risk_score":15},"weighted_score_before":60.16,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"contract_score":58,"backlog_visibility_score":35,"margin_bridge_score":66,"revision_score":45,"relative_strength_score":55,"customer_quality_score":62,"policy_or_regulatory_score":15,"valuation_repricing_score":30,"execution_risk_score":25,"legal_or_contract_risk_score":15,"dilution_cb_risk_score":18,"accounting_trust_risk_score":15},"weighted_score_after":63.13,"stage_label_after":"Stage2-Actionable","changed_components":["margin_bridge_score","customer_quality_score","execution_risk_score","valuation_repricing_score"],"component_delta_explanation":"C15 shadow profile separates raw commodity headline from product pass-through, demand/customer route, realized margin/cash, and local price phase. Counterexamples are capped; post-reset direct-route positives remain eligible.","MFE_90D_pct":43.45,"MAE_90D_pct":-6.76,"score_return_alignment_label":"aligned","current_profile_verdict":"current_profile_too_late"}
{"row_type":"case","case_id":"C15L84_002710_20240308","symbol":"002710","company_name":"TCC Steel","round":"R4","loop":"84","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C15_MATERIAL_SPREAD_SUPERCYCLE","fine_archetype_id":"C15_STEEL_CHEMICAL_FERTILIZER_PASSTHROUGH_LAG_AND_PHASE_GUARD","case_type":"4B_overlay_success","positive_or_counterexample":"counterexample","best_trigger":"TRG_C15L84_002710_20240308_Stage4B","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"aligned","current_profile_verdict":"current_profile_4B_too_late","price_source":"Songdaiki/stock-web","notes":"Product-route narrative after rerating needed 4B-watch; the 180D path had shallow MFE and severe MAE."}
{"row_type":"trigger","trigger_id":"TRG_C15L84_002710_20240308_Stage4B","case_id":"C15L84_002710_20240308","symbol":"002710","company_name":"TCC Steel","round":"R4","loop":"84","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C15_MATERIAL_SPREAD_SUPERCYCLE","fine_archetype_id":"C15_STEEL_CHEMICAL_FERTILIZER_PASSTHROUGH_LAG_AND_PHASE_GUARD","sector":"tinplate_nickel_plated_steel","primary_archetype":"steel_sheet_product_mix_and_raw_material_pass_through","loop_objective":"counterexample_mining; residual_false_positive_mining; direct_url_proxy_mfe_mae_repair; 4B_non_price_requirement_stress_test; canonical_archetype_compression","trigger_type":"Stage4B","trigger_date":"2024-03-08","evidence_available_at_that_date":"Risk article dated 2024-03-08; entry uses 2024-03-08 close.","evidence_source":"TCC Steel IBTomato article 2024-03-08: https://www.ibtomato.com/ExternalView.aspx?no=11719&type=1","stage2_evidence_fields":["public_event_or_disclosure","customer_or_order_quality"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["valuation_blowoff","capital_raise_or_overhang","margin_or_backlog_slowdown","positioning_overheat"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/002/002710/2024.csv","profile_path":"atlas/symbol_profiles/002/002710.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-03-08","entry_price":63700.0,"MFE_30D_pct":7.38,"MFE_90D_pct":7.38,"MFE_180D_pct":7.38,"MFE_1Y_pct":7.38,"MFE_2Y_pct":null,"MAE_30D_pct":-21.04,"MAE_90D_pct":-35.16,"MAE_180D_pct":-57.61,"MAE_1Y_pct":-63.81,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-03-12","peak_price":68400.0,"drawdown_after_peak_pct":-60.53,"green_lateness_ratio":null,"four_b_local_peak_proximity":0.88,"four_b_full_window_peak_proximity":0.92,"four_b_timing_verdict":"good_4B_watch_or_cap","four_b_evidence_type":["valuation_blowoff","capital_raise_or_overhang","margin_or_backlog_slowdown","positioning_overheat"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"tinplate_nickel_sheet_after_rerating_4b_success","current_profile_verdict":"current_profile_4B_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window; shares_drift=0.0pct_under_20pct_gate","same_entry_group_id":"SEG_C15L84_002710_20240308","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C15L84_002710_20240308","trigger_id":"TRG_C15L84_002710_20240308_Stage4B","symbol":"002710","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C15_MATERIAL_SPREAD_SUPERCYCLE","raw_component_scores_before":{"contract_score":58,"backlog_visibility_score":35,"margin_bridge_score":28,"revision_score":25,"relative_strength_score":25,"customer_quality_score":32,"policy_or_regulatory_score":15,"valuation_repricing_score":65,"execution_risk_score":65,"legal_or_contract_risk_score":15,"dilution_cb_risk_score":45,"accounting_trust_risk_score":15},"weighted_score_before":40.23,"stage_label_before":"Stage4B","raw_component_scores_after":{"contract_score":58,"backlog_visibility_score":35,"margin_bridge_score":16,"revision_score":25,"relative_strength_score":25,"customer_quality_score":24,"policy_or_regulatory_score":15,"valuation_repricing_score":73,"execution_risk_score":75,"legal_or_contract_risk_score":15,"dilution_cb_risk_score":45,"accounting_trust_risk_score":15},"weighted_score_after":34.77,"stage_label_after":"Stage4B","changed_components":["margin_bridge_score","customer_quality_score","execution_risk_score","valuation_repricing_score"],"component_delta_explanation":"C15 shadow profile separates raw commodity headline from product pass-through, demand/customer route, realized margin/cash, and local price phase. Counterexamples are capped; post-reset direct-route positives remain eligible.","MFE_90D_pct":7.38,"MAE_90D_pct":-35.16,"score_return_alignment_label":"aligned","current_profile_verdict":"current_profile_4B_too_late"}
{"row_type":"case","case_id":"C15L84_007690_20240216","symbol":"007690","company_name":"KUKDO Chemical","round":"R4","loop":"84","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C15_MATERIAL_SPREAD_SUPERCYCLE","fine_archetype_id":"C15_STEEL_CHEMICAL_FERTILIZER_PASSTHROUGH_LAG_AND_PHASE_GUARD","case_type":"failed_rerating","positive_or_counterexample":"counterexample","best_trigger":"TRG_C15L84_007690_20240216_Stage2","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"aligned","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"Global share and spread normalization text did not overcome BPA/ECH spread compression; route-only evidence stayed weak."}
{"row_type":"trigger","trigger_id":"TRG_C15L84_007690_20240216_Stage2","case_id":"C15L84_007690_20240216","symbol":"007690","company_name":"KUKDO Chemical","round":"R4","loop":"84","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C15_MATERIAL_SPREAD_SUPERCYCLE","fine_archetype_id":"C15_STEEL_CHEMICAL_FERTILIZER_PASSTHROUGH_LAG_AND_PHASE_GUARD","sector":"epoxy_resin_bpa_ech","primary_archetype":"epoxy_spread_and_cost_pass_through","loop_objective":"counterexample_mining; residual_false_positive_mining; direct_url_proxy_mfe_mae_repair; 4B_non_price_requirement_stress_test; canonical_archetype_compression","trigger_type":"Stage2","trigger_date":"2024-02-16","evidence_available_at_that_date":"Report dated 2024-02-16; entry uses 2024-02-16 close.","evidence_source":"KUKDO Chemical KIRS report 2024-02-16: https://ssl.pstatic.net/imgstock/upload/research/company/1708038661744.pdf","stage2_evidence_fields":["public_event_or_disclosure","capacity_or_volume_route"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["margin_or_backlog_slowdown"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/007/007690/2024.csv","profile_path":"atlas/symbol_profiles/007/007690.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-02-16","entry_price":39850.0,"MFE_30D_pct":4.64,"MFE_90D_pct":4.64,"MFE_180D_pct":4.64,"MFE_1Y_pct":4.64,"MFE_2Y_pct":null,"MAE_30D_pct":-6.4,"MAE_90D_pct":-14.05,"MAE_180D_pct":-24.34,"MAE_1Y_pct":-33.75,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-02-20","peak_price":41700.0,"drawdown_after_peak_pct":-27.7,"green_lateness_ratio":null,"four_b_local_peak_proximity":0.55,"four_b_full_window_peak_proximity":0.92,"four_b_timing_verdict":"local_4B_watch_only","four_b_evidence_type":["margin_or_backlog_slowdown"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"epoxy_spread_stale_result_false_positive","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window; shares_drift=0.0pct_under_20pct_gate","same_entry_group_id":"SEG_C15L84_007690_20240216","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C15L84_007690_20240216","trigger_id":"TRG_C15L84_007690_20240216_Stage2","symbol":"007690","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C15_MATERIAL_SPREAD_SUPERCYCLE","raw_component_scores_before":{"contract_score":40,"backlog_visibility_score":35,"margin_bridge_score":28,"revision_score":25,"relative_strength_score":25,"customer_quality_score":32,"policy_or_regulatory_score":15,"valuation_repricing_score":50,"execution_risk_score":65,"legal_or_contract_risk_score":15,"dilution_cb_risk_score":18,"accounting_trust_risk_score":15},"weighted_score_before":39.39,"stage_label_before":"Stage2-watch","raw_component_scores_after":{"contract_score":40,"backlog_visibility_score":35,"margin_bridge_score":16,"revision_score":25,"relative_strength_score":25,"customer_quality_score":24,"policy_or_regulatory_score":15,"valuation_repricing_score":58,"execution_risk_score":75,"legal_or_contract_risk_score":15,"dilution_cb_risk_score":18,"accounting_trust_risk_score":15},"weighted_score_after":33.93,"stage_label_after":"Stage2-watch","changed_components":["margin_bridge_score","customer_quality_score","execution_risk_score","valuation_repricing_score"],"component_delta_explanation":"C15 shadow profile separates raw commodity headline from product pass-through, demand/customer route, realized margin/cash, and local price phase. Counterexamples are capped; post-reset direct-route positives remain eligible.","MFE_90D_pct":4.64,"MAE_90D_pct":-14.05,"score_return_alignment_label":"aligned","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"case","case_id":"C15L84_004890_20241115","symbol":"004890","company_name":"Dongil Industries","round":"R4","loop":"84","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C15_MATERIAL_SPREAD_SUPERCYCLE","fine_archetype_id":"C15_STEEL_CHEMICAL_FERTILIZER_PASSTHROUGH_LAG_AND_PHASE_GUARD","case_type":"stage2_promote_candidate","positive_or_counterexample":"positive","best_trigger":"TRG_C15L84_004890_20241115_Stage2Actionable","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"mixed","current_profile_verdict":"current_profile_correct","price_source":"Songdaiki/stock-web","notes":"A small but clean post-reset path; this is not a Green case, but it supports Stage2 after reset with direct business-route evidence."}
{"row_type":"trigger","trigger_id":"TRG_C15L84_004890_20241115_Stage2Actionable","case_id":"C15L84_004890_20241115","symbol":"004890","company_name":"Dongil Industries","round":"R4","loop":"84","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C15_MATERIAL_SPREAD_SUPERCYCLE","fine_archetype_id":"C15_STEEL_CHEMICAL_FERTILIZER_PASSTHROUGH_LAG_AND_PHASE_GUARD","sector":"special_bar_ferroalloy","primary_archetype":"bar_ferroalloy_spread_after_reset","loop_objective":"counterexample_mining; residual_false_positive_mining; direct_url_proxy_mfe_mae_repair; 4B_non_price_requirement_stress_test; canonical_archetype_compression","trigger_type":"Stage2-Actionable","trigger_date":"2024-11-14","evidence_available_at_that_date":"Quarterly/official reporting window around 2024-11-14; entry uses next tradable close 2024-11-15.","evidence_source":"Dongil Industries financial report list / business report: https://www.dongil.co.kr/bizdemo55059/menu05/page01.php?com_board_basic=read_form&com_board_id=13&com_board_id=13&com_board_idx=30&com_board_page=&com_board_search_code=&com_board_search_value1=&com_board_search_value2=","stage2_evidence_fields":["public_event_or_disclosure","customer_or_order_quality"],"stage3_evidence_fields":["financial_visibility"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/004/004890/2024.csv","profile_path":"atlas/symbol_profiles/004/004890.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-11-15","entry_price":38200.0,"MFE_30D_pct":3.93,"MFE_90D_pct":9.69,"MFE_180D_pct":23.69,"MFE_1Y_pct":23.69,"MFE_2Y_pct":null,"MAE_30D_pct":-2.23,"MAE_90D_pct":-2.23,"MAE_180D_pct":-2.23,"MAE_1Y_pct":-2.23,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2025-06-12","peak_price":47250.0,"drawdown_after_peak_pct":-11.32,"green_lateness_ratio":null,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_applicable","four_b_evidence_type":[],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"special_bar_ferroalloy_reset_stage2_positive","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window; shares_drift=0.0pct_under_20pct_gate","same_entry_group_id":"SEG_C15L84_004890_20241115","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C15L84_004890_20241115","trigger_id":"TRG_C15L84_004890_20241115_Stage2Actionable","symbol":"004890","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C15_MATERIAL_SPREAD_SUPERCYCLE","raw_component_scores_before":{"contract_score":58,"backlog_visibility_score":35,"margin_bridge_score":58,"revision_score":45,"relative_strength_score":25,"customer_quality_score":56,"policy_or_regulatory_score":15,"valuation_repricing_score":30,"execution_risk_score":30,"legal_or_contract_risk_score":15,"dilution_cb_risk_score":18,"accounting_trust_risk_score":15},"weighted_score_before":57.16,"stage_label_before":"Stage2","raw_component_scores_after":{"contract_score":58,"backlog_visibility_score":35,"margin_bridge_score":66,"revision_score":45,"relative_strength_score":25,"customer_quality_score":62,"policy_or_regulatory_score":15,"valuation_repricing_score":30,"execution_risk_score":25,"legal_or_contract_risk_score":15,"dilution_cb_risk_score":18,"accounting_trust_risk_score":15},"weighted_score_after":60.13,"stage_label_after":"Stage2-Actionable","changed_components":["margin_bridge_score","customer_quality_score","execution_risk_score","valuation_repricing_score"],"component_delta_explanation":"C15 shadow profile separates raw commodity headline from product pass-through, demand/customer route, realized margin/cash, and local price phase. Counterexamples are capped; post-reset direct-route positives remain eligible.","MFE_90D_pct":9.69,"MAE_90D_pct":-2.23,"score_return_alignment_label":"mixed","current_profile_verdict":"current_profile_correct"}
{"row_type":"residual_contribution","round":"R4","loop":"84","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C15_MATERIAL_SPREAD_SUPERCYCLE","new_independent_case_count":8,"reused_case_count":0,"new_symbol_count":8,"new_trigger_family_count":8,"tested_existing_calibrated_axes":["stage2_required_bridge","local_4b_watch_guard","full_4b_requires_non_price_evidence","hard_4c_thesis_break_routes_to_4c"],"residual_error_types_found":["raw_material_proxy_false_positive","inventory_lag_damage","product_pass_through_missing","high_MAE_live_route_not_hard4C","direct_route_after_reset_missed_structural"],"loop_contribution_label":"canonical_archetype_rule_candidate","do_not_propose_new_weight_delta":false}
```

## 26. Deferred Coding Agent Handoff Prompt

### Purpose
You are now in the repository implementation phase. The attached Markdown files are v12 post-calibrated residual research outputs produced using the Songdaiki/stock-web OHLC atlas. These MDs are not live candidate research. They are historical calibration research designed to extend the already-applied e2r_2_1_stock_web_calibrated profile. Do not blindly apply every shadow row. Ingest the machine-readable rows and update the sector/canonical-archetype calibration ledger.

### Price source context
- Primary historical price source used by the research MD: Songdaiki/stock-web.
- Price basis: tradable_raw.
- Price adjustment status: raw_unadjusted_marcap.
- Price shard pattern: atlas/ohlcv_tradable_by_symbol_year/<prefix>/<symbol>/<year>.csv.
- Symbol profile pattern: atlas/symbol_profiles/<prefix>/<symbol>.json.

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
completed_round = R4
completed_loop = 84
selection_basis = docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket = Priority 1 C15 spread reversal / inventory-cycle balance repair + Priority 0 direct URL/proxy/MFE-MAE repair
next_recommended_archetypes = C01/C05 direct FCF or cash-conversion rows; C13 strict-new utilization/ex-credit rows; C10 strict-new order-conversion rows; C31 non-semi/battery awarded-cashflow rows; R13 only for genuinely new taxonomy compression
round_schedule_status = coverage_index_selected
round_sector_consistency = pass
```

## 28. Source Notes

- MAIN prompt source: `docs/core/e2r_v12_prompt_round_scheduler_corrected.txt`.
- No-repeat source: `docs/core/V12_Research_No_Repeat_Index.md`.
- Price source: `Songdaiki/stock-web`, manifest `atlas/manifest.json`, schema `atlas/schema.json`.
- Evidence source URLs are stored per trigger row under `evidence_source`.

## Batch Ingest Self-Audit

```text
expected_v12_result_file: true
filename_pattern_pass: true
metadata_filename_consistency: pass
jsonl_trigger_row_count: 8
calibration_usable_trigger_count: 8
representative_trigger_count: 8
new_weight_evidence_candidate_count: 8
guardrail_candidate_count: 5
narrative_only_or_rejected_count: 0
rows_missing_required_mfe_mae: 0
rows_missing_entry_price_or_date: 0
rows_with_noncanonical_trigger_type: 0
rows_with_compact_mfe_mae_alias_only: 0
hard_duplicate_key_count_vs_local_C15_archive: 0
ready_for_batch_ingest: true
```
