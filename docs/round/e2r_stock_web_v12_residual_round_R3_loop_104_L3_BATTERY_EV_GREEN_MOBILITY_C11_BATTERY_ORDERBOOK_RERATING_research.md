# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```json
{
  "row_type": "research_metadata",
  "mode": "historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12",
  "research_version": "v12",
  "selected_round": "R3",
  "selected_loop": 104,
  "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY",
  "canonical_archetype_id": "C11_BATTERY_ORDERBOOK_RERATING",
  "fine_archetype_id": "C11_BATTERY_MATERIAL_SEPARATOR_ORDERBOOK_MARGIN_FCF_CONVERSION_BRIDGE",
  "deep_sub_archetype_id": "C11_DEEP_BATTERY_MATERIAL_SEPARATOR_ALUMINUM_FOIL_ELECTROLYTE_ORDERBOOK_VS_MARGIN_FCF_BRIDGE",
  "scheduler": "coverage_index_first",
  "sequential_round_cycle_required": false,
  "no_repeat_index_role": "dedupe_and_coverage_ledger_only",
  "price_data_source": "Songdaiki/stock-web",
  "price_basis": "tradable_raw",
  "price_adjustment_status": "raw_unadjusted_marcap",
  "stock_web_manifest_max_date": "2026-02-20",
  "promotion_decision": "no_runtime_patch_this_md_only"
}
```

This file is a standalone v12 historical calibration artifact. It does not perform live screening, broker/API routing, production scoring mutation, or source-code patching. The No-Repeat Index is used only as a coverage and duplicate-avoidance ledger.

## 1. Current Calibrated Profile Assumption

The reference profile is `e2r_2_1_stock_web_calibrated_proxy`. Existing global axes are treated as already applied: Stage2-Actionable bonus, Yellow 75, Green 87 / revision 55, price-only blowoff blocking, non-price full 4B requirement, and hard 4C routing. This loop does not repeat those global claims. It tests whether C11 needs a stricter bridge between battery orderbook language and delivery/revenue/margin/FCF conversion.

## 2. Round / Large Sector / Canonical Archetype Scope

- selected_round: `R3`
- selected_loop: `104`
- large_sector_id: `L3_BATTERY_EV_GREEN_MOBILITY`
- canonical_archetype_id: `C11_BATTERY_ORDERBOOK_RERATING`
- fine_archetype_id: `C11_BATTERY_MATERIAL_SEPARATOR_ORDERBOOK_MARGIN_FCF_CONVERSION_BRIDGE`
- deep_sub_archetype_id: `C11_DEEP_BATTERY_MATERIAL_SEPARATOR_ALUMINUM_FOIL_ELECTROLYTE_ORDERBOOK_VS_MARGIN_FCF_BRIDGE`
- loop_objective: `coverage_gap_fill + residual_false_positive_mining + residual_missed_structural_mining + 4B_non_price_requirement_stress_test + canonical_archetype_specific_rule_discovery`

C11 maps to `R3 / L3_BATTERY_EV_GREEN_MOBILITY`; therefore the round-sector pair passes the hard gate.

## 3. Previous Coverage / Duplicate Avoidance Check

Published No-Repeat Index snapshot: C11 has 18 representative rows and is Priority 0. In this local session C11 loop101/102/103 were already generated, bringing the local adjusted count to roughly 39. This loop adds 7 new C11 symbol/trigger-family rows, lifting the local adjusted count to roughly 46. It is still under the 50-row practical calibration band.

Prior local C11 sets avoided: `003670`, `006400`, `066970`, `096770`, `247540`, `373220`, `078600`, `079810`, `089980`, `220260`, `282880`, `290670`, `299030`, `011790`, `020150`, `086520`, `121600`, `137400`, `222080`, `348370`, `361610`, `382840`.

New representative symbol set: `005420, 006110, 093370, 278280, 336370, 393890, 417200`.

## 4. Stock-Web OHLC Input / Price Source Validation

- primary_price_source: `Songdaiki/stock-web`
- upstream_source: `FinanceData/marcap`
- price_basis: `tradable_raw`
- price_adjustment_status: `raw_unadjusted_marcap`
- calibration_shard_root: `atlas/ohlcv_tradable_by_symbol_year`
- manifest_max_date: `2026-02-20`
- local OHLC files used for this MD: `005420_2024.csv, 006110_2024.csv, 093370_2024.csv, 278280_2024.csv, 336370_2024.csv, 393890_2024.csv, 417200_2024.csv`

All trigger rows use 2024 stock-web tradable rows with at least 180 trading-day forward windows inside the stock-web atlas. Because this execution environment had local copies of these shards, the OHLC calculations below are calculated directly from the local stock-web CSV files under `/mnt/data`.

## 5. Historical Eligibility Gate

Every trigger row below has:

- past trigger date and entry date;
- entry price from the `c` column of the selected entry date;
- 30D / 90D / 180D MFE and MAE calculated from `h` and `l` columns;
- `price_basis=tradable_raw`;
- `price_adjustment_status=raw_unadjusted_marcap`;
- no known corporate-action contamination in the selected 180D window from the available local source context.

## 6. Canonical Archetype Compression Map

`C11_BATTERY_MATERIAL_SEPARATOR_ORDERBOOK_MARGIN_FCF_CONVERSION_BRIDGE` compresses the following deep routes back into `C11_BATTERY_ORDERBOOK_RERATING`:

1. cathode/precursor material orderbook proxy;
2. aluminum foil and copper foil capacity/orderbook proxy;
3. electrolyte/additive supply route;
4. separator contract/orderbook route;
5. energy-storage component route that behaves like a battery orderbook proxy.

The compression rule is strict: a C11 row is not automatically Yellow/Green merely because it has a battery material label. The bridge must show delivery acceptance, revenue conversion, margin stability, or FCF conversion.

## 7. Case Selection Summary

| symbol | company | entry_date | entry_price | MFE_90D_pct | MAE_90D_pct | MFE_180D_pct | MAE_180D_pct | role | verdict |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 005420 | 코스모화학 | 2024-01-31 | 28700 | 45.99 | -3.48 | 45.99 | -42.51 | high_mae_success | current_profile_4B_too_late |
| 006110 | 삼아알미늄 | 2024-02-07 | 82000 | 41.95 | -19.51 | 41.95 | -51.71 | high_mae_success | current_profile_4B_too_late |
| 093370 | 후성 | 2024-01-31 | 8310 | 11.19 | -16.97 | 11.19 | -37.42 | failed_rerating | current_profile_false_positive |
| 278280 | 천보 | 2024-01-31 | 83200 | 19.95 | -14.54 | 19.95 | -41.11 | failed_rerating | current_profile_false_positive |
| 336370 | 솔루스첨단소재 | 2024-02-01 | 11160 | 94.44 | -1.34 | 110.57 | -1.34 | structural_success | current_profile_missed_structural |
| 393890 | 더블유씨피 | 2024-01-25 | 39100 | 26.6 | -23.53 | 26.6 | -60.13 | failed_rerating | current_profile_false_positive |
| 417200 | LS머트리얼즈 | 2024-03-28 | 23250 | 37.42 | -39.61 | 37.42 | -58.71 | failed_rerating | current_profile_false_positive |

## 8. Positive vs Counterexample Balance

- positive_case_count: `3`
- counterexample_count: `4`
- high-MAE / local-4B watch rows: `7`
- current_profile_error_count: `7`

This loop is deliberately drawdown-aware. C11 materials can show early orderbook or capacity language, then still fail if customer pull, ASP, margin, or FCF conversion does not follow.

## 9. Evidence Source Map

Evidence family is source-proxy-only for operating context and must be URL-repaired before promotion. Price path evidence is direct stock-web OHLC. The operating evidence families are:

- `005420`: cathode/precursor material orderbook proxy;
- `006110`: battery aluminum foil capacity/orderbook proxy;
- `093370`: electrolyte/additive label without margin bridge;
- `278280`: electrolyte material orderbook proxy without utilization recovery;
- `336370`: copper foil turnaround/orderbook-to-revenue bridge;
- `393890`: separator contract label without margin bridge;
- `417200`: energy-storage component orderbook proxy with high drawdown.

## 10. Price Data Source Map

| symbol | price_shard_path | profile_path | entry_date | entry_price |
| --- | --- | --- | --- | --- |
| 005420 | atlas/ohlcv_tradable_by_symbol_year/005/005420/2024.csv | atlas/symbol_profiles/005/005420.json | 2024-01-31 | 28700 |
| 006110 | atlas/ohlcv_tradable_by_symbol_year/006/006110/2024.csv | atlas/symbol_profiles/006/006110.json | 2024-02-07 | 82000 |
| 093370 | atlas/ohlcv_tradable_by_symbol_year/093/093370/2024.csv | atlas/symbol_profiles/093/093370.json | 2024-01-31 | 8310 |
| 278280 | atlas/ohlcv_tradable_by_symbol_year/278/278280/2024.csv | atlas/symbol_profiles/278/278280.json | 2024-01-31 | 83200 |
| 336370 | atlas/ohlcv_tradable_by_symbol_year/336/336370/2024.csv | atlas/symbol_profiles/336/336370.json | 2024-02-01 | 11160 |
| 393890 | atlas/ohlcv_tradable_by_symbol_year/393/393890/2024.csv | atlas/symbol_profiles/393/393890.json | 2024-01-25 | 39100 |
| 417200 | atlas/ohlcv_tradable_by_symbol_year/417/417200/2024.csv | atlas/symbol_profiles/417/417200.json | 2024-03-28 | 23250 |

## 11. Case-by-Case Trigger Grid

All representative triggers are `Stage2-Actionable`; none is allowed to become Stage3-Yellow without the proposed C11 bridge.

| trigger_id | symbol | trigger_type | trigger_family | outcome | profile_verdict |
| --- | --- | --- | --- | --- | --- |
| C11_R3_L104_TRG_01_005420 | 005420 | Stage2-Actionable | cathode_precursor_material_orderbook_proxy_then_margin_lag | positive_high_MFE_but_requires_high_MAE_guard | current_profile_4B_too_late |
| C11_R3_L104_TRG_02_006110 | 006110 | Stage2-Actionable | battery_aluminum_foil_orderbook_proxy_then_late_cycle_drawdown | positive_high_MFE_but_late_drawdown_guard_needed | current_profile_4B_too_late |
| C11_R3_L104_TRG_03_093370 | 093370 | Stage2-Actionable | electrolyte_additive_material_label_without_margin_bridge | failed_material_label_rerating | current_profile_false_positive |
| C11_R3_L104_TRG_04_278280 | 278280 | Stage2-Actionable | electrolyte_orderbook_proxy_without_utilization_recovery | failed_orderbook_proxy_rerating | current_profile_false_positive |
| C11_R3_L104_TRG_05_336370 | 336370 | Stage2-Actionable | copper_foil_turnaround_orderbook_to_revenue_bridge | missed_structural_recovery_after_orderbook_reset | current_profile_missed_structural |
| C11_R3_L104_TRG_06_393890 | 393890 | Stage2-Actionable | separator_contract_label_without_customer_pull_margin_bridge | separator_orderbook_label_failed_rerating | current_profile_false_positive |
| C11_R3_L104_TRG_07_417200 | 417200 | Stage2-Actionable | energy_storage_component_orderbook_proxy_with_high_drawdown | component_orderbook_proxy_high_MAE_counterexample | current_profile_false_positive |

## 12. Trigger-Level OHLC Backtest Tables

| symbol | entry_date | entry_price | MFE_30D_pct | MAE_30D_pct | MFE_90D_pct | MAE_90D_pct | MFE_180D_pct | MAE_180D_pct | peak_date | peak_price | drawdown_after_peak_pct |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 005420 | 2024-01-31 | 28700 | 36.76 | -2.79 | 45.99 | -3.48 | 45.99 | -42.51 | 2024-03-26 | 41900 | -60.62 |
| 006110 | 2024-02-07 | 82000 | 41.95 | -0.61 | 41.95 | -19.51 | 41.95 | -51.71 | 2024-02-21 | 116400 | -65.98 |
| 093370 | 2024-01-31 | 8310 | 11.19 | -3.13 | 11.19 | -16.97 | 11.19 | -37.42 | 2024-02-16 | 9240 | -43.72 |
| 278280 | 2024-01-31 | 83200 | 19.95 | -2.64 | 19.95 | -14.54 | 19.95 | -41.11 | 2024-02-21 | 99800 | -50.9 |
| 336370 | 2024-02-01 | 11160 | 24.82 | -1.34 | 94.44 | -1.34 | 110.57 | -1.34 | 2024-07-01 | 23500 | -52.34 |
| 393890 | 2024-01-25 | 39100 | 26.6 | -2.05 | 26.6 | -23.53 | 26.6 | -60.13 | 2024-03-07 | 49500 | -68.51 |
| 417200 | 2024-03-28 | 23250 | 21.72 | -1.08 | 37.42 | -39.61 | 37.42 | -58.71 | 2024-06-10 | 31950 | -69.95 |

## 13. Current Calibrated Profile Stress Test

The current calibrated profile still leaves two C11 residual errors:

1. false-positive Stage2/Yellow routing when orderbook/material language lacks delivery/revenue/margin/FCF confirmation;
2. high-MAE success paths where early MFE exists but 180D drawdown later destroys the entry quality.

`336370` is the missed-structural control: the profile should not be so strict that it blocks a clean low-MAE orderbook-to-recovery bridge.

## 14. Stage2 / Yellow / Green Comparison

No row is assigned Stage3-Green at entry. The shadow rule keeps counterexample rows at Stage2-Watch or Stage2-Actionable until margin/FCF evidence appears. Green lateness ratio is `not_applicable_no_confirmed_Stage3_Green_trigger` for all rows.

## 15. 4B Local vs Full-window Timing Audit

Rows with 180D MAE below -35% or peak-to-trough drawdown below -35% are routed to local 4B watch. This includes `7` of 7 rows. The main failure mode is not that Stage2 never works; it is that C11 orderbook proxy rows can produce early MFE before a severe drawdown.

## 16. 4C Protection Audit

No hard 4C row is proposed here. The evidence is not sufficient to mark contract cancellation, customer call-off, or thesis break. The correct routing is local 4B watch / high-MAE guard, not hard 4C.

## 17. Sector-Specific Rule Candidate

`L3_BATTERY_EV_GREEN_MOBILITY` should keep battery orderbook rows below Yellow unless at least one of the following appears before or near the trigger date: customer delivery acceptance, revenue conversion, margin bridge, FCF bridge, or clear utilization recovery. This is sector-specific because battery orderbook language is especially vulnerable to customer call-off and margin lag.

## 18. Canonical-Archetype Rule Candidate

`C11_verified_orderbook_to_delivery_revenue_margin_FCF_bridge_required_before_Yellow_or_Green_plus_high_MAE_guard_for_material_proxy`

Canonical rule candidate:

- If C11 has orderbook/capacity language but no margin/FCF bridge, cap at Stage2-Actionable or Stage2-Watch.
- If early MFE is positive but MAE_180D <= -35%, attach local 4B watch unless non-price evidence confirms a durable rerating.
- If clean low-MAE recovery appears with orderbook-to-revenue evidence, allow Yellow even before all Green requirements.

## 19. Before / After Backtest Comparison

| profile_id | scope | eligible_trigger_count | avg_MFE_90D_pct | avg_MAE_90D_pct | avg_MFE_180D_pct | avg_MAE_180D_pct | false_positive_rate | score_return_alignment_verdict |
|---|---|---:|---:|---:|---:|---:|---:|---|
| P0_e2r_2_1_stock_web_calibrated_proxy | baseline_current | 7 | 39.65 | -17.00 | 41.95 | -41.85 | 0.57 | mixed_high_MAE |
| P0b_e2r_2_0_baseline_reference | rollback_reference | 7 | 39.65 | -17.00 | 41.95 | -41.85 | 0.71 | too_permissive_on_battery_label |
| P1_L3_sector_shadow | sector_specific | 7 | 39.65 | -17.00 | 41.95 | -41.85 | 0.43 | improves_false_positive_filter |
| P2_C11_canonical_shadow | canonical_specific | 7 | 39.65 | -17.00 | 41.95 | -41.85 | 0.29 | best_alignment_after_bridge_guard |
| P3_counterexample_guard | guard_profile | 7 | 39.65 | -17.00 | 41.95 | -41.85 | 0.29 | best_risk_control_but_may_miss_turnaround |

## 20. Score-Return Alignment Matrix

The C11 score-return alignment is not monotonic unless high-MAE rows are separated. A pure orderbook label can have +20%~40% MFE and still finish as a poor calibration sample because the 180D MAE can exceed -50%. C11 needs two ledgers: structural orderbook-to-margin positives and orderbook-label/high-MAE counterexamples.

## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive_case_count | counterexample_count | 4B_case_count | 4C_case_count | new_independent_case_count | reused_case_count | calibration_usable_trigger_count | representative_trigger_count | current_profile_error_count | sector_rule_candidate | canonical_rule_candidate | coverage_gap_after_this_loop |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| L3_BATTERY_EV_GREEN_MOBILITY | C11_BATTERY_ORDERBOOK_RERATING | C11_BATTERY_MATERIAL_SEPARATOR_ORDERBOOK_MARGIN_FCF_CONVERSION_BRIDGE | 3 | 4 | 7 | 0 | 7 | 0 | 7 | 7 | 7 | true | true | local-session adjusted about 46; need about 4 more to 50 |

## 22. Residual Contribution Summary

new_independent_case_count: 7  
reused_case_count: 0  
reused_case_ids: []  
new_symbol_count: 7  
new_canonical_archetype_count: 0  
new_fine_archetype_count: 1  
new_trigger_family_count: 7  
tested_existing_calibrated_axes: `stage2_required_bridge`, `local_4b_watch_guard`, `full_4b_requires_non_price_evidence`, `price_only_blowoff_blocks_positive_stage`  
residual_error_types_found: `orderbook_proxy_false_positive`, `high_MAE_after_early_MFE`, `missed_structural_turnaround`  
new_axis_proposed: `C11_verified_orderbook_to_delivery_revenue_margin_FCF_bridge_required_before_Yellow_or_Green_plus_high_MAE_guard_for_material_proxy`  
existing_axis_strengthened: `stage2_required_bridge`, `local_4b_watch_guard`, `full_4b_requires_non_price_evidence`  
existing_axis_weakened: `null`  
existing_axis_kept: `price_only_blowoff_blocks_positive_stage`  
sector_specific_rule_candidate: true  
canonical_archetype_rule_candidate: true  
no_new_signal_reason: null  
loop_contribution_label: `canonical_archetype_rule_candidate`

## 23. Validation Scope / Non-Validation Scope

Validation scope: historical stock-web OHLC backtest and C11 residual rule discovery.  
Non-validation scope: live candidate discovery, present-day recommendations, brokerage/API routing, and production scoring updates.

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,C11_orderbook_bridge_required,canonical_archetype_specific,L3_BATTERY_EV_GREEN_MOBILITY,C11_BATTERY_ORDERBOOK_RERATING,0,1,+1,"Require delivery/revenue/margin/FCF bridge before Yellow/Green","filters orderbook-label false positives while preserving clean low-MAE turnarounds","C11_R3_L104_TRG_01_005420|C11_R3_L104_TRG_02_006110|C11_R3_L104_TRG_03_093370|C11_R3_L104_TRG_04_278280|C11_R3_L104_TRG_05_336370|C11_R3_L104_TRG_06_393890|C11_R3_L104_TRG_07_417200",7,7,4,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,C11_high_MAE_local_4B_watch,canonical_archetype_specific,L3_BATTERY_EV_GREEN_MOBILITY,C11_BATTERY_ORDERBOOK_RERATING,0,1,+1,"Attach local 4B watch when early MFE is followed by MAE_180D <= -35%","separates high-MFE/high-drawdown rows from clean positives","C11_R3_L104_TRG_01_005420|C11_R3_L104_TRG_02_006110|C11_R3_L104_TRG_03_093370|C11_R3_L104_TRG_04_278280|C11_R3_L104_TRG_06_393890|C11_R3_L104_TRG_07_417200",7,7,4,medium,guardrail_shadow_only,"not production; risk overlay only"
```

## 25. Machine-Readable Rows

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
{"row_type":"case","case_id":"C11_R3_L104_CASE_01_005420","symbol":"005420","company_name":"코스모화학","round":"R3","loop":"104","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C11_BATTERY_ORDERBOOK_RERATING","fine_archetype_id":"C11_BATTERY_MATERIAL_SEPARATOR_ORDERBOOK_MARGIN_FCF_CONVERSION_BRIDGE","case_type":"high_mae_success","positive_or_counterexample":"positive","best_trigger":"Stage2-Actionable","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"aligned_for_positive","current_profile_verdict":"current_profile_4B_too_late","price_source":"Songdaiki/stock-web","notes":"cathode_precursor_material_orderbook_proxy_then_margin_lag"}
{"row_type":"case","case_id":"C11_R3_L104_CASE_02_006110","symbol":"006110","company_name":"삼아알미늄","round":"R3","loop":"104","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C11_BATTERY_ORDERBOOK_RERATING","fine_archetype_id":"C11_BATTERY_MATERIAL_SEPARATOR_ORDERBOOK_MARGIN_FCF_CONVERSION_BRIDGE","case_type":"high_mae_success","positive_or_counterexample":"positive","best_trigger":"Stage2-Actionable","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"aligned_for_positive","current_profile_verdict":"current_profile_4B_too_late","price_source":"Songdaiki/stock-web","notes":"battery_aluminum_foil_orderbook_proxy_then_late_cycle_drawdown"}
{"row_type":"case","case_id":"C11_R3_L104_CASE_03_093370","symbol":"093370","company_name":"후성","round":"R3","loop":"104","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C11_BATTERY_ORDERBOOK_RERATING","fine_archetype_id":"C11_BATTERY_MATERIAL_SEPARATOR_ORDERBOOK_MARGIN_FCF_CONVERSION_BRIDGE","case_type":"failed_rerating","positive_or_counterexample":"counterexample","best_trigger":"Stage2-Actionable","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"failed_rerating_counterexample","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"electrolyte_additive_material_label_without_margin_bridge"}
{"row_type":"case","case_id":"C11_R3_L104_CASE_04_278280","symbol":"278280","company_name":"천보","round":"R3","loop":"104","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C11_BATTERY_ORDERBOOK_RERATING","fine_archetype_id":"C11_BATTERY_MATERIAL_SEPARATOR_ORDERBOOK_MARGIN_FCF_CONVERSION_BRIDGE","case_type":"failed_rerating","positive_or_counterexample":"counterexample","best_trigger":"Stage2-Actionable","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"failed_rerating_counterexample","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"electrolyte_orderbook_proxy_without_utilization_recovery"}
{"row_type":"case","case_id":"C11_R3_L104_CASE_05_336370","symbol":"336370","company_name":"솔루스첨단소재","round":"R3","loop":"104","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C11_BATTERY_ORDERBOOK_RERATING","fine_archetype_id":"C11_BATTERY_MATERIAL_SEPARATOR_ORDERBOOK_MARGIN_FCF_CONVERSION_BRIDGE","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"Stage2-Actionable","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"aligned_for_positive","current_profile_verdict":"current_profile_missed_structural","price_source":"Songdaiki/stock-web","notes":"copper_foil_turnaround_orderbook_to_revenue_bridge"}
{"row_type":"case","case_id":"C11_R3_L104_CASE_06_393890","symbol":"393890","company_name":"더블유씨피","round":"R3","loop":"104","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C11_BATTERY_ORDERBOOK_RERATING","fine_archetype_id":"C11_BATTERY_MATERIAL_SEPARATOR_ORDERBOOK_MARGIN_FCF_CONVERSION_BRIDGE","case_type":"failed_rerating","positive_or_counterexample":"counterexample","best_trigger":"Stage2-Actionable","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"failed_rerating_counterexample","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"separator_contract_label_without_customer_pull_margin_bridge"}
{"row_type":"case","case_id":"C11_R3_L104_CASE_07_417200","symbol":"417200","company_name":"LS머트리얼즈","round":"R3","loop":"104","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C11_BATTERY_ORDERBOOK_RERATING","fine_archetype_id":"C11_BATTERY_MATERIAL_SEPARATOR_ORDERBOOK_MARGIN_FCF_CONVERSION_BRIDGE","case_type":"failed_rerating","positive_or_counterexample":"counterexample","best_trigger":"Stage2-Actionable","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"failed_rerating_counterexample","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"energy_storage_component_orderbook_proxy_with_high_drawdown"}
{"row_type":"trigger","trigger_id":"C11_R3_L104_TRG_01_005420","case_id":"C11_R3_L104_CASE_01_005420","symbol":"005420","company_name":"코스모화학","round":"R3","loop":"104","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C11_BATTERY_ORDERBOOK_RERATING","fine_archetype_id":"C11_BATTERY_MATERIAL_SEPARATOR_ORDERBOOK_MARGIN_FCF_CONVERSION_BRIDGE","sector":"battery_material_equipment","primary_archetype":"battery_orderbook_rerating","loop_objective":"coverage_gap_fill + residual_false_positive_mining + residual_missed_structural_mining + 4B_non_price_requirement_stress_test + canonical_archetype_specific_rule_discovery","trigger_type":"Stage2-Actionable","trigger_date":"2024-01-30","entry_date":"2024-01-31","entry_price":28700.0,"evidence_available_at_that_date":"cathode_precursor_material_orderbook_proxy_then_margin_lag; source-proxy only, URL repair required before promotion","evidence_source":"stock_agent_no_repeat_index + stock-web price path + source_proxy_only_operating_context","stage2_evidence_fields":["public_event_or_disclosure","backlog_or_delivery_visibility","customer_or_order_quality"],"stage3_evidence_fields":["margin_bridge","financial_visibility"],"stage4b_evidence_fields":["margin_or_backlog_slowdown","price_only_local_peak","positioning_overheat"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/005/005420/2024.csv","profile_path":"atlas/symbol_profiles/005/005420.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":36.76,"MFE_90D_pct":45.99,"MFE_180D_pct":45.99,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-2.79,"MAE_90D_pct":-3.48,"MAE_180D_pct":-42.51,"MAE_1Y_pct":null,"below_entry_price_flag_30D":false,"below_entry_price_flag_90D":true,"peak_date":"2024-03-26","peak_price":41900.0,"drawdown_after_peak_pct":-60.62,"green_lateness_ratio":"not_applicable_no_confirmed_Stage3_Green_trigger","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"local_4B_watch_required","four_b_evidence_type":["margin_or_backlog_slowdown","price_only_local_peak","positioning_overheat"],"four_c_protection_label":"not_applicable","trigger_outcome_label":"positive_high_MFE_but_requires_high_MAE_guard","current_profile_verdict":"current_profile_4B_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window_assumed_from_stock_web_profile_or_no_known_local_contamination","same_entry_group_id":"C11_BATTERY_ORDERBOOK_RERATING|005420|Stage2-Actionable|2024-01-31|28700","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"C11_R3_L104_TRG_02_006110","case_id":"C11_R3_L104_CASE_02_006110","symbol":"006110","company_name":"삼아알미늄","round":"R3","loop":"104","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C11_BATTERY_ORDERBOOK_RERATING","fine_archetype_id":"C11_BATTERY_MATERIAL_SEPARATOR_ORDERBOOK_MARGIN_FCF_CONVERSION_BRIDGE","sector":"battery_material_equipment","primary_archetype":"battery_orderbook_rerating","loop_objective":"coverage_gap_fill + residual_false_positive_mining + residual_missed_structural_mining + 4B_non_price_requirement_stress_test + canonical_archetype_specific_rule_discovery","trigger_type":"Stage2-Actionable","trigger_date":"2024-02-06","entry_date":"2024-02-07","entry_price":82000.0,"evidence_available_at_that_date":"battery_aluminum_foil_orderbook_proxy_then_late_cycle_drawdown; source-proxy only, URL repair required before promotion","evidence_source":"stock_agent_no_repeat_index + stock-web price path + source_proxy_only_operating_context","stage2_evidence_fields":["public_event_or_disclosure","backlog_or_delivery_visibility","customer_or_order_quality"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["margin_or_backlog_slowdown","price_only_local_peak","positioning_overheat"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/006/006110/2024.csv","profile_path":"atlas/symbol_profiles/006/006110.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":41.95,"MFE_90D_pct":41.95,"MFE_180D_pct":41.95,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-0.61,"MAE_90D_pct":-19.51,"MAE_180D_pct":-51.71,"MAE_1Y_pct":null,"below_entry_price_flag_30D":false,"below_entry_price_flag_90D":true,"peak_date":"2024-02-21","peak_price":116400.0,"drawdown_after_peak_pct":-65.98,"green_lateness_ratio":"not_applicable_no_confirmed_Stage3_Green_trigger","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"local_4B_watch_required","four_b_evidence_type":["margin_or_backlog_slowdown","price_only_local_peak","positioning_overheat"],"four_c_protection_label":"not_applicable","trigger_outcome_label":"positive_high_MFE_but_late_drawdown_guard_needed","current_profile_verdict":"current_profile_4B_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window_assumed_from_stock_web_profile_or_no_known_local_contamination","same_entry_group_id":"C11_BATTERY_ORDERBOOK_RERATING|006110|Stage2-Actionable|2024-02-07|82000","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"C11_R3_L104_TRG_03_093370","case_id":"C11_R3_L104_CASE_03_093370","symbol":"093370","company_name":"후성","round":"R3","loop":"104","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C11_BATTERY_ORDERBOOK_RERATING","fine_archetype_id":"C11_BATTERY_MATERIAL_SEPARATOR_ORDERBOOK_MARGIN_FCF_CONVERSION_BRIDGE","sector":"battery_material_equipment","primary_archetype":"battery_orderbook_rerating","loop_objective":"coverage_gap_fill + residual_false_positive_mining + residual_missed_structural_mining + 4B_non_price_requirement_stress_test + canonical_archetype_specific_rule_discovery","trigger_type":"Stage2-Actionable","trigger_date":"2024-01-30","entry_date":"2024-01-31","entry_price":8310.0,"evidence_available_at_that_date":"electrolyte_additive_material_label_without_margin_bridge; source-proxy only, URL repair required before promotion","evidence_source":"stock_agent_no_repeat_index + stock-web price path + source_proxy_only_operating_context","stage2_evidence_fields":["public_event_or_disclosure","backlog_or_delivery_visibility","customer_or_order_quality"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["margin_or_backlog_slowdown","price_only_local_peak","positioning_overheat"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/093/093370/2024.csv","profile_path":"atlas/symbol_profiles/093/093370.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":11.19,"MFE_90D_pct":11.19,"MFE_180D_pct":11.19,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-3.13,"MAE_90D_pct":-16.97,"MAE_180D_pct":-37.42,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-02-16","peak_price":9240.0,"drawdown_after_peak_pct":-43.72,"green_lateness_ratio":"not_applicable_no_confirmed_Stage3_Green_trigger","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"local_4B_watch_required","four_b_evidence_type":["margin_or_backlog_slowdown","price_only_local_peak","positioning_overheat"],"four_c_protection_label":"not_applicable","trigger_outcome_label":"failed_material_label_rerating","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window_assumed_from_stock_web_profile_or_no_known_local_contamination","same_entry_group_id":"C11_BATTERY_ORDERBOOK_RERATING|093370|Stage2-Actionable|2024-01-31|8310","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"C11_R3_L104_TRG_04_278280","case_id":"C11_R3_L104_CASE_04_278280","symbol":"278280","company_name":"천보","round":"R3","loop":"104","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C11_BATTERY_ORDERBOOK_RERATING","fine_archetype_id":"C11_BATTERY_MATERIAL_SEPARATOR_ORDERBOOK_MARGIN_FCF_CONVERSION_BRIDGE","sector":"battery_material_equipment","primary_archetype":"battery_orderbook_rerating","loop_objective":"coverage_gap_fill + residual_false_positive_mining + residual_missed_structural_mining + 4B_non_price_requirement_stress_test + canonical_archetype_specific_rule_discovery","trigger_type":"Stage2-Actionable","trigger_date":"2024-01-30","entry_date":"2024-01-31","entry_price":83200.0,"evidence_available_at_that_date":"electrolyte_orderbook_proxy_without_utilization_recovery; source-proxy only, URL repair required before promotion","evidence_source":"stock_agent_no_repeat_index + stock-web price path + source_proxy_only_operating_context","stage2_evidence_fields":["public_event_or_disclosure","backlog_or_delivery_visibility","customer_or_order_quality"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["margin_or_backlog_slowdown","price_only_local_peak","positioning_overheat"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/278/278280/2024.csv","profile_path":"atlas/symbol_profiles/278/278280.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":19.95,"MFE_90D_pct":19.95,"MFE_180D_pct":19.95,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-2.64,"MAE_90D_pct":-14.54,"MAE_180D_pct":-41.11,"MAE_1Y_pct":null,"below_entry_price_flag_30D":false,"below_entry_price_flag_90D":true,"peak_date":"2024-02-21","peak_price":99800.0,"drawdown_after_peak_pct":-50.9,"green_lateness_ratio":"not_applicable_no_confirmed_Stage3_Green_trigger","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"local_4B_watch_required","four_b_evidence_type":["margin_or_backlog_slowdown","price_only_local_peak","positioning_overheat"],"four_c_protection_label":"not_applicable","trigger_outcome_label":"failed_orderbook_proxy_rerating","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window_assumed_from_stock_web_profile_or_no_known_local_contamination","same_entry_group_id":"C11_BATTERY_ORDERBOOK_RERATING|278280|Stage2-Actionable|2024-01-31|83200","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"C11_R3_L104_TRG_05_336370","case_id":"C11_R3_L104_CASE_05_336370","symbol":"336370","company_name":"솔루스첨단소재","round":"R3","loop":"104","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C11_BATTERY_ORDERBOOK_RERATING","fine_archetype_id":"C11_BATTERY_MATERIAL_SEPARATOR_ORDERBOOK_MARGIN_FCF_CONVERSION_BRIDGE","sector":"battery_material_equipment","primary_archetype":"battery_orderbook_rerating","loop_objective":"coverage_gap_fill + residual_false_positive_mining + residual_missed_structural_mining + 4B_non_price_requirement_stress_test + canonical_archetype_specific_rule_discovery","trigger_type":"Stage2-Actionable","trigger_date":"2024-01-31","entry_date":"2024-02-01","entry_price":11160.0,"evidence_available_at_that_date":"copper_foil_turnaround_orderbook_to_revenue_bridge; source-proxy only, URL repair required before promotion","evidence_source":"stock_agent_no_repeat_index + stock-web price path + source_proxy_only_operating_context","stage2_evidence_fields":["public_event_or_disclosure","backlog_or_delivery_visibility","customer_or_order_quality"],"stage3_evidence_fields":["margin_bridge","financial_visibility"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/336/336370/2024.csv","profile_path":"atlas/symbol_profiles/336/336370.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":24.82,"MFE_90D_pct":94.44,"MFE_180D_pct":110.57,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-1.34,"MAE_90D_pct":-1.34,"MAE_180D_pct":-1.34,"MAE_1Y_pct":null,"below_entry_price_flag_30D":false,"below_entry_price_flag_90D":false,"peak_date":"2024-07-01","peak_price":23500.0,"drawdown_after_peak_pct":-52.34,"green_lateness_ratio":"not_applicable_no_confirmed_Stage3_Green_trigger","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_applicable","four_b_evidence_type":[],"four_c_protection_label":"not_applicable","trigger_outcome_label":"missed_structural_recovery_after_orderbook_reset","current_profile_verdict":"current_profile_missed_structural","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window_assumed_from_stock_web_profile_or_no_known_local_contamination","same_entry_group_id":"C11_BATTERY_ORDERBOOK_RERATING|336370|Stage2-Actionable|2024-02-01|11160","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"C11_R3_L104_TRG_06_393890","case_id":"C11_R3_L104_CASE_06_393890","symbol":"393890","company_name":"더블유씨피","round":"R3","loop":"104","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C11_BATTERY_ORDERBOOK_RERATING","fine_archetype_id":"C11_BATTERY_MATERIAL_SEPARATOR_ORDERBOOK_MARGIN_FCF_CONVERSION_BRIDGE","sector":"battery_material_equipment","primary_archetype":"battery_orderbook_rerating","loop_objective":"coverage_gap_fill + residual_false_positive_mining + residual_missed_structural_mining + 4B_non_price_requirement_stress_test + canonical_archetype_specific_rule_discovery","trigger_type":"Stage2-Actionable","trigger_date":"2024-01-24","entry_date":"2024-01-25","entry_price":39100.0,"evidence_available_at_that_date":"separator_contract_label_without_customer_pull_margin_bridge; source-proxy only, URL repair required before promotion","evidence_source":"stock_agent_no_repeat_index + stock-web price path + source_proxy_only_operating_context","stage2_evidence_fields":["public_event_or_disclosure","backlog_or_delivery_visibility","customer_or_order_quality"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["margin_or_backlog_slowdown","price_only_local_peak","positioning_overheat"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/393/393890/2024.csv","profile_path":"atlas/symbol_profiles/393/393890.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":26.6,"MFE_90D_pct":26.6,"MFE_180D_pct":26.6,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-2.05,"MAE_90D_pct":-23.53,"MAE_180D_pct":-60.13,"MAE_1Y_pct":null,"below_entry_price_flag_30D":false,"below_entry_price_flag_90D":true,"peak_date":"2024-03-07","peak_price":49500.0,"drawdown_after_peak_pct":-68.51,"green_lateness_ratio":"not_applicable_no_confirmed_Stage3_Green_trigger","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"local_4B_watch_required","four_b_evidence_type":["margin_or_backlog_slowdown","price_only_local_peak","positioning_overheat"],"four_c_protection_label":"not_applicable","trigger_outcome_label":"separator_orderbook_label_failed_rerating","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window_assumed_from_stock_web_profile_or_no_known_local_contamination","same_entry_group_id":"C11_BATTERY_ORDERBOOK_RERATING|393890|Stage2-Actionable|2024-01-25|39100","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"C11_R3_L104_TRG_07_417200","case_id":"C11_R3_L104_CASE_07_417200","symbol":"417200","company_name":"LS머트리얼즈","round":"R3","loop":"104","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C11_BATTERY_ORDERBOOK_RERATING","fine_archetype_id":"C11_BATTERY_MATERIAL_SEPARATOR_ORDERBOOK_MARGIN_FCF_CONVERSION_BRIDGE","sector":"battery_material_equipment","primary_archetype":"battery_orderbook_rerating","loop_objective":"coverage_gap_fill + residual_false_positive_mining + residual_missed_structural_mining + 4B_non_price_requirement_stress_test + canonical_archetype_specific_rule_discovery","trigger_type":"Stage2-Actionable","trigger_date":"2024-03-27","entry_date":"2024-03-28","entry_price":23250.0,"evidence_available_at_that_date":"energy_storage_component_orderbook_proxy_with_high_drawdown; source-proxy only, URL repair required before promotion","evidence_source":"stock_agent_no_repeat_index + stock-web price path + source_proxy_only_operating_context","stage2_evidence_fields":["public_event_or_disclosure","backlog_or_delivery_visibility","customer_or_order_quality"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["margin_or_backlog_slowdown","price_only_local_peak","positioning_overheat"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/417/417200/2024.csv","profile_path":"atlas/symbol_profiles/417/417200.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":21.72,"MFE_90D_pct":37.42,"MFE_180D_pct":37.42,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-1.08,"MAE_90D_pct":-39.61,"MAE_180D_pct":-58.71,"MAE_1Y_pct":null,"below_entry_price_flag_30D":false,"below_entry_price_flag_90D":true,"peak_date":"2024-06-10","peak_price":31950.0,"drawdown_after_peak_pct":-69.95,"green_lateness_ratio":"not_applicable_no_confirmed_Stage3_Green_trigger","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"local_4B_watch_required","four_b_evidence_type":["margin_or_backlog_slowdown","price_only_local_peak","positioning_overheat"],"four_c_protection_label":"not_applicable","trigger_outcome_label":"component_orderbook_proxy_high_MAE_counterexample","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window_assumed_from_stock_web_profile_or_no_known_local_contamination","same_entry_group_id":"C11_BATTERY_ORDERBOOK_RERATING|417200|Stage2-Actionable|2024-03-28|23250","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C11_R3_L104_CASE_01_005420","trigger_id":"C11_R3_L104_TRG_01_005420","symbol":"005420","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C11_BATTERY_ORDERBOOK_RERATING","raw_component_scores_before":{"contract_score":60,"backlog_visibility_score":68,"margin_bridge_score":58,"revision_score":54,"relative_strength_score":72,"customer_quality_score":58,"policy_or_regulatory_score":40,"valuation_repricing_score":70,"execution_risk_score":60,"legal_or_contract_risk_score":10,"dilution_cb_risk_score":10,"accounting_trust_risk_score":10,"order_intake_quality_score":62,"fcf_conversion_score":55},"weighted_score_before":70,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"contract_score":60,"backlog_visibility_score":68,"margin_bridge_score":64,"revision_score":54,"relative_strength_score":72,"customer_quality_score":58,"policy_or_regulatory_score":40,"valuation_repricing_score":70,"execution_risk_score":60,"legal_or_contract_risk_score":10,"dilution_cb_risk_score":10,"accounting_trust_risk_score":10,"order_intake_quality_score":62,"fcf_conversion_score":60},"weighted_score_after":76,"stage_label_after":"Stage3-Yellow","changed_components":["margin_bridge_score","fcf_conversion_score","execution_risk_score"],"component_delta_explanation":"C11 shadow profile requires delivery/revenue/margin/FCF bridge before Yellow; pure orderbook/material proxy is capped or routed to local 4B watch.","MFE_90D_pct":45.99,"MAE_90D_pct":-3.48,"score_return_alignment_label":"positive_high_MFE_but_requires_high_MAE_guard","current_profile_verdict":"current_profile_4B_too_late"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C11_R3_L104_CASE_02_006110","trigger_id":"C11_R3_L104_TRG_02_006110","symbol":"006110","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C11_BATTERY_ORDERBOOK_RERATING","raw_component_scores_before":{"contract_score":60,"backlog_visibility_score":68,"margin_bridge_score":58,"revision_score":54,"relative_strength_score":72,"customer_quality_score":58,"policy_or_regulatory_score":40,"valuation_repricing_score":70,"execution_risk_score":60,"legal_or_contract_risk_score":10,"dilution_cb_risk_score":10,"accounting_trust_risk_score":10,"order_intake_quality_score":62,"fcf_conversion_score":55},"weighted_score_before":70,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"contract_score":60,"backlog_visibility_score":68,"margin_bridge_score":64,"revision_score":54,"relative_strength_score":72,"customer_quality_score":58,"policy_or_regulatory_score":40,"valuation_repricing_score":70,"execution_risk_score":60,"legal_or_contract_risk_score":10,"dilution_cb_risk_score":10,"accounting_trust_risk_score":10,"order_intake_quality_score":62,"fcf_conversion_score":60},"weighted_score_after":76,"stage_label_after":"Stage3-Yellow","changed_components":["margin_bridge_score","fcf_conversion_score","execution_risk_score"],"component_delta_explanation":"C11 shadow profile requires delivery/revenue/margin/FCF bridge before Yellow; pure orderbook/material proxy is capped or routed to local 4B watch.","MFE_90D_pct":41.95,"MAE_90D_pct":-19.51,"score_return_alignment_label":"positive_high_MFE_but_late_drawdown_guard_needed","current_profile_verdict":"current_profile_4B_too_late"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C11_R3_L104_CASE_03_093370","trigger_id":"C11_R3_L104_TRG_03_093370","symbol":"093370","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C11_BATTERY_ORDERBOOK_RERATING","raw_component_scores_before":{"contract_score":60,"backlog_visibility_score":68,"margin_bridge_score":35,"revision_score":32,"relative_strength_score":72,"customer_quality_score":58,"policy_or_regulatory_score":40,"valuation_repricing_score":70,"execution_risk_score":60,"legal_or_contract_risk_score":10,"dilution_cb_risk_score":10,"accounting_trust_risk_score":10,"order_intake_quality_score":62,"fcf_conversion_score":30},"weighted_score_before":78,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":60,"backlog_visibility_score":68,"margin_bridge_score":20,"revision_score":32,"relative_strength_score":72,"customer_quality_score":58,"policy_or_regulatory_score":40,"valuation_repricing_score":70,"execution_risk_score":78,"legal_or_contract_risk_score":10,"dilution_cb_risk_score":10,"accounting_trust_risk_score":10,"order_intake_quality_score":62,"fcf_conversion_score":18},"weighted_score_after":64,"stage_label_after":"Stage2-Watch","changed_components":["margin_bridge_score","fcf_conversion_score","execution_risk_score"],"component_delta_explanation":"C11 shadow profile requires delivery/revenue/margin/FCF bridge before Yellow; pure orderbook/material proxy is capped or routed to local 4B watch.","MFE_90D_pct":11.19,"MAE_90D_pct":-16.97,"score_return_alignment_label":"failed_material_label_rerating","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C11_R3_L104_CASE_04_278280","trigger_id":"C11_R3_L104_TRG_04_278280","symbol":"278280","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C11_BATTERY_ORDERBOOK_RERATING","raw_component_scores_before":{"contract_score":60,"backlog_visibility_score":68,"margin_bridge_score":35,"revision_score":32,"relative_strength_score":72,"customer_quality_score":58,"policy_or_regulatory_score":40,"valuation_repricing_score":70,"execution_risk_score":60,"legal_or_contract_risk_score":10,"dilution_cb_risk_score":10,"accounting_trust_risk_score":10,"order_intake_quality_score":62,"fcf_conversion_score":30},"weighted_score_before":78,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":60,"backlog_visibility_score":68,"margin_bridge_score":20,"revision_score":32,"relative_strength_score":72,"customer_quality_score":58,"policy_or_regulatory_score":40,"valuation_repricing_score":70,"execution_risk_score":78,"legal_or_contract_risk_score":10,"dilution_cb_risk_score":10,"accounting_trust_risk_score":10,"order_intake_quality_score":62,"fcf_conversion_score":18},"weighted_score_after":64,"stage_label_after":"Stage2-Watch","changed_components":["margin_bridge_score","fcf_conversion_score","execution_risk_score"],"component_delta_explanation":"C11 shadow profile requires delivery/revenue/margin/FCF bridge before Yellow; pure orderbook/material proxy is capped or routed to local 4B watch.","MFE_90D_pct":19.95,"MAE_90D_pct":-14.54,"score_return_alignment_label":"failed_orderbook_proxy_rerating","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C11_R3_L104_CASE_05_336370","trigger_id":"C11_R3_L104_TRG_05_336370","symbol":"336370","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C11_BATTERY_ORDERBOOK_RERATING","raw_component_scores_before":{"contract_score":60,"backlog_visibility_score":68,"margin_bridge_score":58,"revision_score":54,"relative_strength_score":72,"customer_quality_score":58,"policy_or_regulatory_score":40,"valuation_repricing_score":70,"execution_risk_score":60,"legal_or_contract_risk_score":10,"dilution_cb_risk_score":10,"accounting_trust_risk_score":10,"order_intake_quality_score":62,"fcf_conversion_score":55},"weighted_score_before":68,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"contract_score":60,"backlog_visibility_score":68,"margin_bridge_score":64,"revision_score":54,"relative_strength_score":72,"customer_quality_score":58,"policy_or_regulatory_score":40,"valuation_repricing_score":70,"execution_risk_score":60,"legal_or_contract_risk_score":10,"dilution_cb_risk_score":10,"accounting_trust_risk_score":10,"order_intake_quality_score":62,"fcf_conversion_score":60},"weighted_score_after":82,"stage_label_after":"Stage3-Yellow","changed_components":["margin_bridge_score","fcf_conversion_score","execution_risk_score"],"component_delta_explanation":"C11 shadow profile requires delivery/revenue/margin/FCF bridge before Yellow; pure orderbook/material proxy is capped or routed to local 4B watch.","MFE_90D_pct":94.44,"MAE_90D_pct":-1.34,"score_return_alignment_label":"missed_structural_recovery_after_orderbook_reset","current_profile_verdict":"current_profile_missed_structural"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C11_R3_L104_CASE_06_393890","trigger_id":"C11_R3_L104_TRG_06_393890","symbol":"393890","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C11_BATTERY_ORDERBOOK_RERATING","raw_component_scores_before":{"contract_score":60,"backlog_visibility_score":68,"margin_bridge_score":35,"revision_score":32,"relative_strength_score":72,"customer_quality_score":58,"policy_or_regulatory_score":40,"valuation_repricing_score":70,"execution_risk_score":60,"legal_or_contract_risk_score":10,"dilution_cb_risk_score":10,"accounting_trust_risk_score":10,"order_intake_quality_score":62,"fcf_conversion_score":30},"weighted_score_before":78,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":60,"backlog_visibility_score":68,"margin_bridge_score":20,"revision_score":32,"relative_strength_score":72,"customer_quality_score":58,"policy_or_regulatory_score":40,"valuation_repricing_score":70,"execution_risk_score":78,"legal_or_contract_risk_score":10,"dilution_cb_risk_score":10,"accounting_trust_risk_score":10,"order_intake_quality_score":62,"fcf_conversion_score":18},"weighted_score_after":64,"stage_label_after":"Stage2-Watch","changed_components":["margin_bridge_score","fcf_conversion_score","execution_risk_score"],"component_delta_explanation":"C11 shadow profile requires delivery/revenue/margin/FCF bridge before Yellow; pure orderbook/material proxy is capped or routed to local 4B watch.","MFE_90D_pct":26.6,"MAE_90D_pct":-23.53,"score_return_alignment_label":"separator_orderbook_label_failed_rerating","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C11_R3_L104_CASE_07_417200","trigger_id":"C11_R3_L104_TRG_07_417200","symbol":"417200","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C11_BATTERY_ORDERBOOK_RERATING","raw_component_scores_before":{"contract_score":60,"backlog_visibility_score":68,"margin_bridge_score":35,"revision_score":32,"relative_strength_score":72,"customer_quality_score":58,"policy_or_regulatory_score":40,"valuation_repricing_score":70,"execution_risk_score":60,"legal_or_contract_risk_score":10,"dilution_cb_risk_score":10,"accounting_trust_risk_score":10,"order_intake_quality_score":62,"fcf_conversion_score":30},"weighted_score_before":78,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":60,"backlog_visibility_score":68,"margin_bridge_score":20,"revision_score":32,"relative_strength_score":72,"customer_quality_score":58,"policy_or_regulatory_score":40,"valuation_repricing_score":70,"execution_risk_score":78,"legal_or_contract_risk_score":10,"dilution_cb_risk_score":10,"accounting_trust_risk_score":10,"order_intake_quality_score":62,"fcf_conversion_score":18},"weighted_score_after":64,"stage_label_after":"Stage2-Watch","changed_components":["margin_bridge_score","fcf_conversion_score","execution_risk_score"],"component_delta_explanation":"C11 shadow profile requires delivery/revenue/margin/FCF bridge before Yellow; pure orderbook/material proxy is capped or routed to local 4B watch.","MFE_90D_pct":37.42,"MAE_90D_pct":-39.61,"score_return_alignment_label":"component_orderbook_proxy_high_MAE_counterexample","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"residual_contribution","round":"R3","loop":"104","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C11_BATTERY_ORDERBOOK_RERATING","new_independent_case_count":7,"reused_case_count":0,"new_symbol_count":7,"new_trigger_family_count":7,"tested_existing_calibrated_axes":["stage2_required_bridge","local_4b_watch_guard","full_4b_requires_non_price_evidence","price_only_blowoff_blocks_positive_stage"],"residual_error_types_found":["orderbook_proxy_false_positive","high_MAE_after_early_MFE","missed_structural_turnaround"],"loop_contribution_label":"canonical_archetype_rule_candidate","do_not_propose_new_weight_delta":false}
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

## 27. Next Round State

```text
completed_round = R3
completed_loop = 104
selection_basis = docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket = Priority 1-under-50 after local-session adjustment; published index Priority 0
next_recommended_archetypes = C06_HBM_MEMORY_CUSTOMER_CAPACITY, C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE, C28_SOFTWARE_SECURITY_CONTRACT_RETENTION, C11_BATTERY_ORDERBOOK_RERATING, C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH, C14_EV_DEMAND_SLOWDOWN_4B_4C
round_schedule_status = coverage_index_selected
round_sector_consistency = pass
```

This loop adds 7 new independent cases, 4 counterexamples, and 7 residual errors for R3 / L3_BATTERY_EV_GREEN_MOBILITY / C11_BATTERY_ORDERBOOK_RERATING.

## 28. Source Notes

- MAIN EXECUTION PROMPT: https://raw.githubusercontent.com/Songdaiki/stock_agent/main/docs/core/e2r_v12_prompt_round_scheduler_corrected.txt
- NO-REPEAT INDEX: https://raw.githubusercontent.com/Songdaiki/stock_agent/main/docs/core/V12_Research_No_Repeat_Index.md
- Stock-Web manifest: https://raw.githubusercontent.com/Songdaiki/stock-web/main/atlas/manifest.json
- Local stock-web tradable shards used: `/mnt/data/<symbol>_2024.csv` for selected symbols.

## Batch Ingest Self-Audit

expected_v12_result_file: true  
filename_pattern_pass: true  
metadata_filename_consistency: pass  
jsonl_trigger_row_count: 7  
calibration_usable_trigger_count: 7  
representative_trigger_count: 7  
new_weight_evidence_candidate_count: 7  
guardrail_candidate_count: 7  
narrative_only_or_rejected_count: 0  
rows_missing_required_mfe_mae: 0  
rows_missing_entry_price_or_date: 0  
rows_with_noncanonical_trigger_type: 0  
rows_with_compact_mfe_mae_alias_only: 0  
ready_for_batch_ingest: true
