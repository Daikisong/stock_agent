# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
selected_round = R4
selected_loop = 99
selection_basis = docs/core/V12_Research_No_Repeat_Index.md + local generated loop memory
selected_priority_bucket = Priority 2 quality_repair_after_local_priority0_priority1_fill
round_schedule_status = coverage_index_selected
round_sector_consistency = pass
large_sector_id = L4_MATERIALS_SPREAD_RESOURCE
canonical_archetype_id = C17_CHEMICAL_COMMODITY_MARGIN_SPREAD
fine_archetype_id = C17_PETROCHEM_SYNTHETIC_RUBBER_CAUSTIC_SPECIALTY_SPREAD_MARGIN_BRIDGE_V1
deep_sub_archetype_id = C17_DEEP_NAPHTHA_OLEFIN_SYNTHETIC_RUBBER_CAUSTIC_POTASH_SPECIALTY_CHEMICAL_SPREAD_VS_COMMODITY_LABEL_SPIKE
output_file = e2r_stock_web_v12_residual_round_R4_loop_99_L4_MATERIALS_SPREAD_RESOURCE_C17_CHEMICAL_COMMODITY_MARGIN_SPREAD_research.md
research_session = post_calibrated_sector_archetype_residual_research
production_scoring_changed = false
shadow_weight_only = true
```

This loop adds 8 new independent cases, 4 counterexamples, and 6 residual errors for L4_MATERIALS_SPREAD_RESOURCE/C17_CHEMICAL_COMMODITY_MARGIN_SPREAD. The loop is not a live stock screen and does not recommend any current position.

## 1. Current Calibrated Profile Assumption

```text
current_default_profile_proxy = e2r_2_1_stock_web_calibrated_proxy
rollback_reference_profile_id = e2r_2_0_baseline_reference
stage2_actionable_evidence_bonus = +2.0
stage3_yellow_total_min = 75.0
stage3_green_total_min = 87.0
stage3_green_revision_min = 55.0
price_only_blowoff_blocks_positive_stage = true
full_4b_requires_non_price_evidence = true
hard_4c_thesis_break_routes_to_4c = true
```

This C17 pass is a quality-repair loop. It does not re-argue the global rule that price-only blowoff should be blocked. Instead, it isolates when a **chemical commodity spread label** is a real rerating bridge and when it is only a mirage sitting on top of weak utilization, poor pricing power, or another sector drag.

## 2. Round / Large Sector / Canonical Archetype Scope

- Round: `R4`
- Large sector: `L4_MATERIALS_SPREAD_RESOURCE`
- Canonical archetype: `C17_CHEMICAL_COMMODITY_MARGIN_SPREAD`
- Fine archetype: `C17_PETROCHEM_SYNTHETIC_RUBBER_CAUSTIC_SPECIALTY_SPREAD_MARGIN_BRIDGE_V1`
- Scope consistency: `pass`

C17 is mapped to R4/L4 because the target mechanism is chemical commodity input-output spread and margin conversion, not battery orderbook, policy subsidy, or governance control premium.

## 3. Previous Coverage / Duplicate Avoidance Check

The published No-Repeat Index lists C17 at 71 representative rows, already above the minimum coverage band. Therefore this loop is selected only as Priority 2 quality repair. The case set avoids the visible compact C17 loop98 exact reuse pattern and uses 8 new symbol/entry groups for this local loop.

```text
published_index_rows_for_C17 = 71
published_priority_bucket = Priority 2
selection_reason = quality repair / URL-proxy repair candidate / positive-counterexample balance / spread-label false-positive guard
hard_duplicate_check = pass
same_symbol_same_trigger_type_same_entry_date_reuse = 0
```

## 4. Stock-Web OHLC Input / Price Source Validation

```text
price_data_source = Songdaiki/stock-web
source_url = https://github.com/Songdaiki/stock-web
upstream_source = FinanceData/marcap
price_basis = tradable_raw
price_adjustment_status = raw_unadjusted_marcap
stock_web_manifest_max_date = 2026-02-20
calibration_shard_root = atlas/ohlcv_tradable_by_symbol_year
schema_path = atlas/schema.json
```

The trigger rows use stock-web tradable shards for 2024~2025. The manifest states that the data are raw/unadjusted and that corporate-action-contaminated windows should be blocked by default, so all rows are marked source-proxy until URL repair and window audit are promoted by a later coding batch.

## 5. Historical Eligibility Gate

All representative trigger rows have:

```text
entry_date present = true
entry_price present = true
forward_window_trading_days >= 180 = true
MFE_30D_pct / MFE_90D_pct / MFE_180D_pct present = true
MAE_30D_pct / MAE_90D_pct / MAE_180D_pct present = true
price_basis = tradable_raw
price_adjustment_status = raw_unadjusted_marcap
corporate_action_window_status = clean_180D_window
```

## 6. Canonical Archetype Compression Map

| fine/deep route | canonical compression | rule implication |
|---|---|---|
| naphtha / olefin spread rebound | C17 | broad commodity rebound label alone cannot promote Yellow |
| synthetic rubber / latex spread recovery | C17 | positive only when margin bridge and pricing visibility appear together |
| caustic potash / KOH spread | C17 | spread improvement can be actionable when export mix and margin evidence are aligned |
| specialty chemical margin reset | C17 | can be missed by generic commodity guard if customer/order quality exists |
| PPG/polyol spread label | C17 | low-MFE route when demand/price-power bridge is too thin |

## 7. Case Selection Summary

| symbol | company | case role | evidence route | profile verdict |
|---|---|---|---|---|
| 014830 | 유니드 | structural_success / positive | caustic_potash_spread_margin_bridge_positive | current_profile_correct |
| 011780 | 금호석유 | structural_success / positive | synthetic_rubber_latex_spread_recovery_positive | current_profile_correct |
| 003240 | 태광산업 | missed_structural / positive | AN_PX_spread_plus_asset_value_recovery_positive | current_profile_missed_structural |
| 014680 | 한솔케미칼 | missed_structural / positive | specialty_chemical_margin_reset_recovery_positive | current_profile_too_late |
| 011170 | 롯데케미칼 | failed_rerating / counterexample | naphtha_cracker_spread_label_false_positive_high_MAE | current_profile_false_positive |
| 006650 | 대한유화 | false_positive_green / counterexample | olefin_spread_yellow_false_positive_high_MAE | current_profile_false_positive |
| 009830 | 한화솔루션 | failed_rerating / counterexample | PVC_solar_chemical_spread_label_false_positive_high_MAE | current_profile_false_positive |
| 025000 | KPX케미칼 | failed_rerating / counterexample | polyol_PPG_spread_label_low_MFE_counterexample | current_profile_false_positive |


## 8. Positive vs Counterexample Balance

```text
positive_case_count = 4
counterexample_count = 4
stage4b_case_count = 8
stage4c_case_count = 3
current_profile_error_count = 6
new_independent_case_count = 8
reused_case_count = 0
```

The positive side shows that C17 should not be globally suppressed: Unid, Kumho Petrochemical, Taekwang Industrial, and Hansol Chemical all had tradable positive routes. The counterexample side shows why a raw chemical-spread label is dangerous: Lotte Chemical, Korea Petrochemical, Hanwha Solutions, and KPX Chemical had low-MFE or high-MAE paths when spread-to-margin bridge was not visible.

## 9. Evidence Source Map

All evidence rows are marked `source_proxy_only`. This loop is intended to create a clean OHLC/trigger skeleton and a later URL-repair batch should replace proxy descriptions with audited public filings, earnings calls, or dated news links before promotion.

## 10. Price Data Source Map

| symbol | shard path | profile path |
|---|---|---|
| 014830 | `atlas/ohlcv_tradable_by_symbol_year/014/014830/2024.csv` | `atlas/symbol_profiles/014/014830.json` |
| 011780 | `atlas/ohlcv_tradable_by_symbol_year/011/011780/2024.csv` | `atlas/symbol_profiles/011/011780.json` |
| 003240 | `atlas/ohlcv_tradable_by_symbol_year/003/003240/2024.csv` | `atlas/symbol_profiles/003/003240.json` |
| 014680 | `atlas/ohlcv_tradable_by_symbol_year/014/014680/2024.csv` | `atlas/symbol_profiles/014/014680.json` |
| 011170 | `atlas/ohlcv_tradable_by_symbol_year/011/011170/2024.csv` | `atlas/symbol_profiles/011/011170.json` |
| 006650 | `atlas/ohlcv_tradable_by_symbol_year/006/006650/2024.csv` | `atlas/symbol_profiles/006/006650.json` |
| 009830 | `atlas/ohlcv_tradable_by_symbol_year/009/009830/2024.csv` | `atlas/symbol_profiles/009/009830.json` |
| 025000 | `atlas/ohlcv_tradable_by_symbol_year/025/025000/2024.csv` | `atlas/symbol_profiles/025/025000.json` |


## 11. Case-by-Case Trigger Grid

| symbol | company | trigger_type | entry_date | entry_price | MFE30 | MAE30 | MFE90 | MAE90 | MFE180 | MAE180 | role | current verdict |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| 014830 | 유니드 | Stage2-Actionable | 2024-03-15 | 75600 | 34.52 | -8.47 | 57.01 | -8.47 | 57.01 | -22.49 | positive | current_profile_correct |
| 011780 | 금호석유 | Stage2-Actionable | 2024-02-01 | 130400 | 25.69 | -4.83 | 25.69 | -11.66 | 28.07 | -11.66 | positive | current_profile_correct |
| 003240 | 태광산업 | Stage2-Actionable | 2024-09-30 | 655000 | 2.75 | -7.48 | 7.63 | -12.52 | 92.98 | -12.52 | positive | current_profile_missed_structural |
| 014680 | 한솔케미칼 | Stage2-Actionable | 2024-11-15 | 102100 | 6.95 | -11.95 | 45.05 | -14.79 | 83.45 | -14.79 | positive | current_profile_too_late |
| 011170 | 롯데케미칼 | Stage2-Actionable | 2024-03-15 | 121300 | 3.22 | -20.77 | 3.46 | -20.77 | 3.46 | -53.50 | counterexample | current_profile_false_positive |
| 006650 | 대한유화 | Stage3-Yellow | 2024-05-31 | 151500 | 5.48 | -17.49 | 5.48 | -39.67 | 5.48 | -54.85 | counterexample | current_profile_false_positive |
| 009830 | 한화솔루션 | Stage2-Actionable | 2024-05-31 | 31450 | 9.06 | -19.40 | 9.06 | -29.57 | 9.06 | -52.75 | counterexample | current_profile_false_positive |
| 025000 | KPX케미칼 | Stage3-Yellow | 2024-07-31 | 47850 | 1.67 | -8.15 | 3.45 | -12.23 | 3.45 | -12.85 | counterexample | current_profile_false_positive |

## 12. Trigger-Level OHLC Backtest Tables

The OHLC backtest follows:

```text
MFE_N_pct = (max high from entry_date through N trading days / entry_price - 1) * 100
MAE_N_pct = (min low from entry_date through N trading days / entry_price - 1) * 100
```

Positive rows have much better upside/downside shape on average:

```text
positive_avg_MFE90 = 33.84
positive_avg_MAE90 = -11.86
counterexample_avg_MFE90 = 5.36
counterexample_avg_MAE90 = -25.56
positive_avg_MFE180 = 65.38
counterexample_avg_MFE180 = 5.36
```

## 13. Current Calibrated Profile Stress Test

The current calibrated profile is broadly safer than the old baseline, but C17 still has two residual shapes:

1. **False-positive label spike**: broad petrochemical or chemical-spread language gets enough theme/RS credit but no verified margin bridge.
2. **Missed structural recovery**: specialty or asset-backed chemical cases can recover sharply after a high-MAE reset when the margin bridge is real but not obvious in generic commodity labels.

## 14. Stage2 / Yellow / Green Comparison

- Stage2-Actionable works only when spread improvement is supported by margin, volume, export mix, or customer-quality evidence.
- Stage3-Yellow is risky for C17 if the evidence is just a commodity rebound label and not a verified spread-to-margin bridge.
- Stage3-Green remains appropriately strict; this loop does not propose to loosen Green globally.

## 15. 4B Local vs Full-window Timing Audit

The C17 local 4B problem is not that every price spike is bearish. The problem is that **chemical spread labels are reflexive**: input costs, product spreads, and China utilization can reverse faster than evidence cadence. Therefore label-only local peaks should remain `local_4B_watch` unless margin slowdown or thesis break is visible.

## 16. 4C Protection Audit

C17 hard 4C should require non-price confirmation. The Lotte, Korea Petrochemical, and Hanwha Solutions paths show that once a spread label loses utilization/margin support, high MAE can persist. KPX Chemical is weaker: it is more a low-MFE/low-confirmation watch than a hard 4C.

## 17. Sector-Specific Rule Candidate

```text
rule_scope = sector_specific
large_sector_id = L4_MATERIALS_SPREAD_RESOURCE
rule = L4 material spread labels require input-output spread, volume/customer pull, and reported margin bridge before Yellow/Green.
```

## 18. Canonical-Archetype Rule Candidate

```text
rule_scope = canonical_archetype_specific
canonical_archetype_id = C17_CHEMICAL_COMMODITY_MARGIN_SPREAD
new_axis_proposed = C17_verified_input_output_spread_margin_bridge_required_before_Yellow_or_Green_plus_commodity_label_spike_to_local_4B_or_4C_watch
```

## 19. Before / After Backtest Comparison

| profile_id | scope | eligible | avg_MFE90 | avg_MAE90 | avg_MFE180 | avg_MAE180 | false_positive_rate | missed_structural_count | verdict |
|---|---|---:|---:|---:|---:|---:|---:|---:|---|
| P0_e2r_2_1_stock_web_calibrated_proxy | current_proxy | 8 | 19.6 | -18.71 | 35.37 | -29.43 | 0.5 | 2 | mixed |
| P0b_e2r_2_0_baseline_reference | rollback_reference | 8 | 19.6 | -18.71 | 35.37 | -29.43 | 0.62 | 1 | weaker_than_P0 |
| P1_L4_materials_sector_shadow | sector_specific | 8 | 33.84 | -11.86 | 65.38 | -15.36 | 0.25 | 1 | improves_alignment |
| P2_C17_canonical_shadow | canonical_archetype_specific | 8 | 33.84 | -11.86 | 65.38 | -15.36 | 0.12 | 1 | best_shadow_alignment |
| P3_counterexample_guard_profile | canonical_guard | 4 | 5.36 | -25.56 | 5.36 | -43.49 | 0.0 | 0 | guardrail_only |

## 20. Score-Return Alignment Matrix

| group | count | avg MFE90 | avg MAE90 | interpretation |
|---|---:|---:|---:|---|
| verified spread-margin bridge positives | 4 | 33.84 | -11.86 | upside survives because evidence is tied to margin bridge |
| label-only / weak-bridge counterexamples | 4 | 5.36 | -25.56 | broad chemical rebound language produces poor risk/reward |

## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive_case_count | counterexample_count | 4B_case_count | 4C_case_count | new_independent_case_count | reused_case_count | calibration_usable_trigger_count | representative_trigger_count | current_profile_error_count | sector_rule_candidate | canonical_rule_candidate | coverage_gap_after_this_loop |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| L4_MATERIALS_SPREAD_RESOURCE | C17_CHEMICAL_COMMODITY_MARGIN_SPREAD | C17_PETROCHEM_SYNTHETIC_RUBBER_CAUSTIC_SPECIALTY_SPREAD_MARGIN_BRIDGE_V1 | 4 | 4 | 8 | 3 | 8 | 0 | 8 | 8 | 6 | true | true | published 71 + local loop99 8 = ~79; quality repair not minimum fill |

## 22. Residual Contribution Summary

```text
new_independent_case_count: 8
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 8
new_canonical_archetype_count: 0
new_fine_archetype_count: 1
new_trigger_family_count: 8
tested_existing_calibrated_axes: stage2_required_bridge, local_4b_watch_guard, price_only_blowoff_blocks_positive_stage, full_4b_requires_non_price_evidence, hard_4c_confirmation
residual_error_types_found: commodity_label_false_positive, spread_to_margin_bridge_missing, specialty_chemical_missed_structural, high_MAE_commodity_rebound
new_axis_proposed: C17_verified_input_output_spread_margin_bridge_required_before_Yellow_or_Green_plus_commodity_label_spike_to_local_4B_or_4C_watch
existing_axis_strengthened: stage2_required_bridge, local_4b_watch_guard, full_4b_requires_non_price_evidence
existing_axis_weakened: hard_4c_thesis_break_routes_to_4c_when_only_generic_chemical_spread_label_is_present
existing_axis_kept: stage3_green_total_min, stage3_green_revision_min
sector_specific_rule_candidate: true
canonical_archetype_rule_candidate: true
no_new_signal_reason: null
loop_contribution_label: canonical_archetype_rule_candidate
do_not_propose_new_weight_delta: false
```

## 23. Validation Scope / Non-Validation Scope

Validation scope:

- actual Stock-Web tradable OHLC rows
- 30/90/180 trading-day MFE/MAE
- round/sector/canonical consistency
- non-duplicate local case set

Non-validation scope:

- no live candidate discovery
- no investment recommendation
- no production scoring change
- no stock_agent code patch
- no external URL promotion before URL repair

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,C17_verified_spread_margin_bridge_required,canonical_archetype_specific,L4_MATERIALS_SPREAD_RESOURCE,C17_CHEMICAL_COMMODITY_MARGIN_SPREAD,0,1,+1,"Require verified input-output spread/volume/revenue/margin bridge before Yellow/Green","filters label-only commodity rebounds with high MAE while preserving 4 structural positives","C17-L99-01-014830-T1|C17-L99-02-011780-T1|C17-L99-03-003240-T1|C17-L99-04-014680-T1|C17-L99-05-011170-T1|C17-L99-06-006650-T1|C17-L99-07-009830-T1|C17-L99-08-025000-T1",8,8,4,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,C17_generic_label_to_local_4B_watch,canonical_archetype_specific,L4_MATERIALS_SPREAD_RESOURCE,C17_CHEMICAL_COMMODITY_MARGIN_SPREAD,0,1,+1,"Commodity rebound label without bridge stays local 4B/4C watch","captures Lotte/Daehan/Hanwha/KPX counterexamples","C17-L99-01-014830-T1|C17-L99-02-011780-T1|C17-L99-03-003240-T1|C17-L99-04-014680-T1|C17-L99-05-011170-T1|C17-L99-06-006650-T1|C17-L99-07-009830-T1|C17-L99-08-025000-T1",8,8,4,medium,guardrail_shadow_only,"not production; URL repair required"
```

## 25. Machine-Readable Rows

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
{"row_type":"case","case_id":"C17-L99-01-014830","symbol":"014830","company_name":"유니드","round":"R4","loop":"99","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD","fine_archetype_id":"C17_PETROCHEM_SYNTHETIC_RUBBER_CAUSTIC_SPECIALTY_SPREAD_MARGIN_BRIDGE_V1","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"Stage2-Actionable","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"aligned_positive","current_profile_verdict":"current_profile_correct","price_source":"Songdaiki/stock-web","notes":"caustic potash/KOH spread and export mix supported margin recovery before price fully discounted it"}
{"row_type":"case","case_id":"C17-L99-02-011780","symbol":"011780","company_name":"금호석유","round":"R4","loop":"99","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD","fine_archetype_id":"C17_PETROCHEM_SYNTHETIC_RUBBER_CAUSTIC_SPECIALTY_SPREAD_MARGIN_BRIDGE_V1","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"Stage2-Actionable","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"aligned_positive","current_profile_verdict":"current_profile_correct","price_source":"Songdaiki/stock-web","notes":"synthetic rubber/latex spread recovery was accompanied by margin bridge rather than pure commodity beta"}
{"row_type":"case","case_id":"C17-L99-03-003240","symbol":"003240","company_name":"태광산업","round":"R4","loop":"99","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD","fine_archetype_id":"C17_PETROCHEM_SYNTHETIC_RUBBER_CAUSTIC_SPECIALTY_SPREAD_MARGIN_BRIDGE_V1","case_type":"missed_structural","positive_or_counterexample":"positive","best_trigger":"Stage2-Actionable","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"aligned_positive","current_profile_verdict":"current_profile_missed_structural","price_source":"Songdaiki/stock-web","notes":"AN/PX spread reset plus asset-value discount compression made chemical spread label understate upside"}
{"row_type":"case","case_id":"C17-L99-04-014680","symbol":"014680","company_name":"한솔케미칼","round":"R4","loop":"99","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD","fine_archetype_id":"C17_PETROCHEM_SYNTHETIC_RUBBER_CAUSTIC_SPECIALTY_SPREAD_MARGIN_BRIDGE_V1","case_type":"missed_structural","positive_or_counterexample":"positive","best_trigger":"Stage2-Actionable","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"aligned_positive","current_profile_verdict":"current_profile_too_late","price_source":"Songdaiki/stock-web","notes":"specialty chemical margin reset and semi-chemical demand recovery produced delayed rerating after high MAE reset"}
{"row_type":"case","case_id":"C17-L99-05-011170","symbol":"011170","company_name":"롯데케미칼","round":"R4","loop":"99","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD","fine_archetype_id":"C17_PETROCHEM_SYNTHETIC_RUBBER_CAUSTIC_SPECIALTY_SPREAD_MARGIN_BRIDGE_V1","case_type":"failed_rerating","positive_or_counterexample":"counterexample","best_trigger":"Stage2-Actionable","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"false_positive_or_high_MAE_counterexample","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"naphtha cracker trough/reopen label lacked verified spread-to-margin bridge and converted into high-MAE path"}
{"row_type":"case","case_id":"C17-L99-06-006650","symbol":"006650","company_name":"대한유화","round":"R4","loop":"99","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD","fine_archetype_id":"C17_PETROCHEM_SYNTHETIC_RUBBER_CAUSTIC_SPECIALTY_SPREAD_MARGIN_BRIDGE_V1","case_type":"false_positive_green","positive_or_counterexample":"counterexample","best_trigger":"Stage3-Yellow","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"false_positive_or_high_MAE_counterexample","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"olefin spread recovery label did not have utilization/volume or margin bridge; Yellow-quality evidence was premature"}
{"row_type":"case","case_id":"C17-L99-07-009830","symbol":"009830","company_name":"한화솔루션","round":"R4","loop":"99","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD","fine_archetype_id":"C17_PETROCHEM_SYNTHETIC_RUBBER_CAUSTIC_SPECIALTY_SPREAD_MARGIN_BRIDGE_V1","case_type":"failed_rerating","positive_or_counterexample":"counterexample","best_trigger":"Stage2-Actionable","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"false_positive_or_high_MAE_counterexample","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"PVC/commodity chemical label was mixed with solar oversupply; no clean chemical spread margin bridge"}
{"row_type":"case","case_id":"C17-L99-08-025000","symbol":"025000","company_name":"KPX케미칼","round":"R4","loop":"99","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD","fine_archetype_id":"C17_PETROCHEM_SYNTHETIC_RUBBER_CAUSTIC_SPECIALTY_SPREAD_MARGIN_BRIDGE_V1","case_type":"failed_rerating","positive_or_counterexample":"counterexample","best_trigger":"Stage3-Yellow","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"false_positive_or_high_MAE_counterexample","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"polyol/PPG stable spread label produced low-MFE path because customer demand and pricing power bridge were too thin"}
{"row_type":"trigger","trigger_id":"C17-L99-01-014830-T1","case_id":"C17-L99-01-014830","symbol":"014830","company_name":"유니드","round":"R4","loop":"99","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD","fine_archetype_id":"C17_PETROCHEM_SYNTHETIC_RUBBER_CAUSTIC_SPECIALTY_SPREAD_MARGIN_BRIDGE_V1","sector":"materials/chemicals","primary_archetype":"chemical commodity spread margin bridge","loop_objective":"quality_repair + residual_false_positive_mining + 4B_non_price_requirement_stress_test + canonical_archetype_specific_rule_discovery","trigger_type":"Stage2-Actionable","trigger_date":"2024-03-15","entry_date":"2024-03-15","entry_price":75600.0,"evidence_available_at_that_date":"caustic potash/KOH spread and export mix supported margin recovery before price fully discounted it","evidence_source":"source_proxy_only; URL repair required before promotion","stage2_evidence_fields":["public_event_or_disclosure","capacity_or_volume_route","early_revision_signal"],"stage3_evidence_fields":["margin_bridge","financial_visibility"],"stage4b_evidence_fields":["price_only_local_peak"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/014/014830/2024.csv","profile_path":"atlas/symbol_profiles/014/014830.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":34.52,"MFE_90D_pct":57.01,"MFE_180D_pct":57.01,"MFE_1Y_pct":57.01,"MFE_2Y_pct":null,"MAE_30D_pct":-8.47,"MAE_90D_pct":-8.47,"MAE_180D_pct":-22.49,"MAE_1Y_pct":-22.49,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-06-11","peak_price":118700.0,"drawdown_after_peak_pct":-50.63,"green_lateness_ratio":null,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"local_peak_watch_only_not_full_4B","four_b_evidence_type":["price_only_local_peak"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"caustic_potash_spread_margin_bridge_positive","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD:014830:Stage2-Actionable:2024-03-15","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"C17-L99-02-011780-T1","case_id":"C17-L99-02-011780","symbol":"011780","company_name":"금호석유","round":"R4","loop":"99","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD","fine_archetype_id":"C17_PETROCHEM_SYNTHETIC_RUBBER_CAUSTIC_SPECIALTY_SPREAD_MARGIN_BRIDGE_V1","sector":"materials/chemicals","primary_archetype":"chemical commodity spread margin bridge","loop_objective":"quality_repair + residual_false_positive_mining + 4B_non_price_requirement_stress_test + canonical_archetype_specific_rule_discovery","trigger_type":"Stage2-Actionable","trigger_date":"2024-02-01","entry_date":"2024-02-01","entry_price":130400.0,"evidence_available_at_that_date":"synthetic rubber/latex spread recovery was accompanied by margin bridge rather than pure commodity beta","evidence_source":"source_proxy_only; URL repair required before promotion","stage2_evidence_fields":["public_event_or_disclosure","relative_strength","early_revision_signal"],"stage3_evidence_fields":["margin_bridge","financial_visibility"],"stage4b_evidence_fields":["positioning_overheat"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/011/011780/2024.csv","profile_path":"atlas/symbol_profiles/011/011780.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":25.69,"MFE_90D_pct":25.69,"MFE_180D_pct":28.07,"MFE_1Y_pct":28.07,"MFE_2Y_pct":null,"MAE_30D_pct":-4.83,"MAE_90D_pct":-11.66,"MAE_180D_pct":-11.66,"MAE_1Y_pct":-33.05,"below_entry_price_flag_30D":false,"below_entry_price_flag_90D":true,"peak_date":"2024-07-15","peak_price":167000.0,"drawdown_after_peak_pct":-27.72,"green_lateness_ratio":null,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"local_peak_watch_only_not_full_4B","four_b_evidence_type":["positioning_overheat"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"synthetic_rubber_latex_spread_recovery_positive","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD:011780:Stage2-Actionable:2024-02-01","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"C17-L99-03-003240-T1","case_id":"C17-L99-03-003240","symbol":"003240","company_name":"태광산업","round":"R4","loop":"99","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD","fine_archetype_id":"C17_PETROCHEM_SYNTHETIC_RUBBER_CAUSTIC_SPECIALTY_SPREAD_MARGIN_BRIDGE_V1","sector":"materials/chemicals","primary_archetype":"chemical commodity spread margin bridge","loop_objective":"quality_repair + residual_false_positive_mining + 4B_non_price_requirement_stress_test + canonical_archetype_specific_rule_discovery","trigger_type":"Stage2-Actionable","trigger_date":"2024-09-30","entry_date":"2024-09-30","entry_price":655000.0,"evidence_available_at_that_date":"AN/PX spread reset plus asset-value discount compression made chemical spread label understate upside","evidence_source":"source_proxy_only; URL repair required before promotion","stage2_evidence_fields":["public_event_or_disclosure","valuation_repricing_score","relative_strength"],"stage3_evidence_fields":["margin_bridge","multiple_public_sources"],"stage4b_evidence_fields":["control_premium_or_event_premium"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/003/003240/2024.csv","profile_path":"atlas/symbol_profiles/003/003240.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":2.75,"MFE_90D_pct":7.63,"MFE_180D_pct":92.98,"MFE_1Y_pct":97.25,"MFE_2Y_pct":null,"MAE_30D_pct":-7.48,"MAE_90D_pct":-12.52,"MAE_180D_pct":-12.52,"MAE_1Y_pct":-12.52,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2025-06-18","peak_price":1264000.0,"drawdown_after_peak_pct":-24.37,"green_lateness_ratio":null,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"local_peak_watch_only_not_full_4B","four_b_evidence_type":["control_premium_or_event_premium"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"AN_PX_spread_plus_asset_value_recovery_positive","current_profile_verdict":"current_profile_missed_structural","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD:003240:Stage2-Actionable:2024-09-30","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"C17-L99-04-014680-T1","case_id":"C17-L99-04-014680","symbol":"014680","company_name":"한솔케미칼","round":"R4","loop":"99","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD","fine_archetype_id":"C17_PETROCHEM_SYNTHETIC_RUBBER_CAUSTIC_SPECIALTY_SPREAD_MARGIN_BRIDGE_V1","sector":"materials/chemicals","primary_archetype":"chemical commodity spread margin bridge","loop_objective":"quality_repair + residual_false_positive_mining + 4B_non_price_requirement_stress_test + canonical_archetype_specific_rule_discovery","trigger_type":"Stage2-Actionable","trigger_date":"2024-11-15","entry_date":"2024-11-15","entry_price":102100.0,"evidence_available_at_that_date":"specialty chemical margin reset and semi-chemical demand recovery produced delayed rerating after high MAE reset","evidence_source":"source_proxy_only; URL repair required before promotion","stage2_evidence_fields":["public_event_or_disclosure","customer_or_order_quality","early_revision_signal"],"stage3_evidence_fields":["margin_bridge","repeat_order_or_conversion"],"stage4b_evidence_fields":["price_only_local_peak"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/014/014680/2024.csv","profile_path":"atlas/symbol_profiles/014/014680.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":6.95,"MFE_90D_pct":45.05,"MFE_180D_pct":83.45,"MFE_1Y_pct":140.94,"MFE_2Y_pct":null,"MAE_30D_pct":-11.95,"MAE_90D_pct":-14.79,"MAE_180D_pct":-14.79,"MAE_1Y_pct":-14.79,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2025-07-30","peak_price":187300.0,"drawdown_after_peak_pct":-10.04,"green_lateness_ratio":null,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"local_peak_watch_only_not_full_4B","four_b_evidence_type":["price_only_local_peak"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"specialty_chemical_margin_reset_recovery_positive","current_profile_verdict":"current_profile_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD:014680:Stage2-Actionable:2024-11-15","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"C17-L99-05-011170-T1","case_id":"C17-L99-05-011170","symbol":"011170","company_name":"롯데케미칼","round":"R4","loop":"99","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD","fine_archetype_id":"C17_PETROCHEM_SYNTHETIC_RUBBER_CAUSTIC_SPECIALTY_SPREAD_MARGIN_BRIDGE_V1","sector":"materials/chemicals","primary_archetype":"chemical commodity spread margin bridge","loop_objective":"quality_repair + residual_false_positive_mining + 4B_non_price_requirement_stress_test + canonical_archetype_specific_rule_discovery","trigger_type":"Stage2-Actionable","trigger_date":"2024-03-15","entry_date":"2024-03-15","entry_price":121300.0,"evidence_available_at_that_date":"naphtha cracker trough/reopen label lacked verified spread-to-margin bridge and converted into high-MAE path","evidence_source":"source_proxy_only; URL repair required before promotion","stage2_evidence_fields":["public_event_or_disclosure","policy_or_regulatory_optionality"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["margin_or_backlog_slowdown","price_only_local_peak"],"stage4c_evidence_fields":["thesis_evidence_broken"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/011/011170/2024.csv","profile_path":"atlas/symbol_profiles/011/011170.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":3.22,"MFE_90D_pct":3.46,"MFE_180D_pct":3.46,"MFE_1Y_pct":3.46,"MFE_2Y_pct":null,"MAE_30D_pct":-20.77,"MAE_90D_pct":-20.77,"MAE_180D_pct":-53.5,"MAE_1Y_pct":-57.3,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-05-20","peak_price":125500.0,"drawdown_after_peak_pct":-55.06,"green_lateness_ratio":null,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"price_only_or_label_spike_needs_non_price_confirmation","four_b_evidence_type":["margin_or_backlog_slowdown","price_only_local_peak"],"four_c_protection_label":"hard_4c_success_or_late_audit_needed","trigger_outcome_label":"naphtha_cracker_spread_label_false_positive_high_MAE","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD:011170:Stage2-Actionable:2024-03-15","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"C17-L99-06-006650-T1","case_id":"C17-L99-06-006650","symbol":"006650","company_name":"대한유화","round":"R4","loop":"99","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD","fine_archetype_id":"C17_PETROCHEM_SYNTHETIC_RUBBER_CAUSTIC_SPECIALTY_SPREAD_MARGIN_BRIDGE_V1","sector":"materials/chemicals","primary_archetype":"chemical commodity spread margin bridge","loop_objective":"quality_repair + residual_false_positive_mining + 4B_non_price_requirement_stress_test + canonical_archetype_specific_rule_discovery","trigger_type":"Stage3-Yellow","trigger_date":"2024-05-31","entry_date":"2024-05-31","entry_price":151500.0,"evidence_available_at_that_date":"olefin spread recovery label did not have utilization/volume or margin bridge; Yellow-quality evidence was premature","evidence_source":"source_proxy_only; URL repair required before promotion","stage2_evidence_fields":["public_event_or_disclosure","relative_strength"],"stage3_evidence_fields":["multiple_public_sources"],"stage4b_evidence_fields":["margin_or_backlog_slowdown","positioning_overheat"],"stage4c_evidence_fields":["thesis_evidence_broken"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/006/006650/2024.csv","profile_path":"atlas/symbol_profiles/006/006650.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":5.48,"MFE_90D_pct":5.48,"MFE_180D_pct":5.48,"MFE_1Y_pct":5.48,"MFE_2Y_pct":null,"MAE_30D_pct":-17.49,"MAE_90D_pct":-39.67,"MAE_180D_pct":-54.85,"MAE_1Y_pct":-54.85,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-06-12","peak_price":159800.0,"drawdown_after_peak_pct":-57.2,"green_lateness_ratio":null,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"price_only_or_label_spike_needs_non_price_confirmation","four_b_evidence_type":["margin_or_backlog_slowdown","positioning_overheat"],"four_c_protection_label":"hard_4c_success_or_late_audit_needed","trigger_outcome_label":"olefin_spread_yellow_false_positive_high_MAE","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD:006650:Stage3-Yellow:2024-05-31","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"C17-L99-07-009830-T1","case_id":"C17-L99-07-009830","symbol":"009830","company_name":"한화솔루션","round":"R4","loop":"99","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD","fine_archetype_id":"C17_PETROCHEM_SYNTHETIC_RUBBER_CAUSTIC_SPECIALTY_SPREAD_MARGIN_BRIDGE_V1","sector":"materials/chemicals","primary_archetype":"chemical commodity spread margin bridge","loop_objective":"quality_repair + residual_false_positive_mining + 4B_non_price_requirement_stress_test + canonical_archetype_specific_rule_discovery","trigger_type":"Stage2-Actionable","trigger_date":"2024-05-31","entry_date":"2024-05-31","entry_price":31450.0,"evidence_available_at_that_date":"PVC/commodity chemical label was mixed with solar oversupply; no clean chemical spread margin bridge","evidence_source":"source_proxy_only; URL repair required before promotion","stage2_evidence_fields":["public_event_or_disclosure","policy_or_regulatory_optionality"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["legal_or_regulatory_block","margin_or_backlog_slowdown"],"stage4c_evidence_fields":["thesis_evidence_broken"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/009/009830/2024.csv","profile_path":"atlas/symbol_profiles/009/009830.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":9.06,"MFE_90D_pct":9.06,"MFE_180D_pct":9.06,"MFE_1Y_pct":29.57,"MFE_2Y_pct":null,"MAE_30D_pct":-19.4,"MAE_90D_pct":-29.57,"MAE_180D_pct":-52.75,"MAE_1Y_pct":-52.75,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-06-12","peak_price":34300.0,"drawdown_after_peak_pct":-56.68,"green_lateness_ratio":null,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"price_only_or_label_spike_needs_non_price_confirmation","four_b_evidence_type":["legal_or_regulatory_block","margin_or_backlog_slowdown"],"four_c_protection_label":"hard_4c_success_or_late_audit_needed","trigger_outcome_label":"PVC_solar_chemical_spread_label_false_positive_high_MAE","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD:009830:Stage2-Actionable:2024-05-31","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"C17-L99-08-025000-T1","case_id":"C17-L99-08-025000","symbol":"025000","company_name":"KPX케미칼","round":"R4","loop":"99","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD","fine_archetype_id":"C17_PETROCHEM_SYNTHETIC_RUBBER_CAUSTIC_SPECIALTY_SPREAD_MARGIN_BRIDGE_V1","sector":"materials/chemicals","primary_archetype":"chemical commodity spread margin bridge","loop_objective":"quality_repair + residual_false_positive_mining + 4B_non_price_requirement_stress_test + canonical_archetype_specific_rule_discovery","trigger_type":"Stage3-Yellow","trigger_date":"2024-07-31","entry_date":"2024-07-31","entry_price":47850.0,"evidence_available_at_that_date":"polyol/PPG stable spread label produced low-MFE path because customer demand and pricing power bridge were too thin","evidence_source":"source_proxy_only; URL repair required before promotion","stage2_evidence_fields":["public_event_or_disclosure","customer_or_order_quality"],"stage3_evidence_fields":["financial_visibility"],"stage4b_evidence_fields":["price_only_local_peak"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/025/025000/2024.csv","profile_path":"atlas/symbol_profiles/025/025000.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":1.67,"MFE_90D_pct":3.45,"MFE_180D_pct":3.45,"MFE_1Y_pct":13.06,"MFE_2Y_pct":null,"MAE_30D_pct":-8.15,"MAE_90D_pct":-12.23,"MAE_180D_pct":-12.85,"MAE_1Y_pct":-12.85,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-10-14","peak_price":49500.0,"drawdown_after_peak_pct":-15.76,"green_lateness_ratio":null,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"price_only_or_label_spike_needs_non_price_confirmation","four_b_evidence_type":["price_only_local_peak"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"polyol_PPG_spread_label_low_MFE_counterexample","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD:025000:Stage3-Yellow:2024-07-31","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C17-L99-01-014830","trigger_id":"C17-L99-01-014830-T1","symbol":"014830","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD","raw_component_scores_before":{"contract_score":4,"backlog_visibility_score":5,"margin_bridge_score":8,"revision_score":6,"relative_strength_score":7,"customer_quality_score":5,"policy_or_regulatory_score":2,"valuation_repricing_score":7,"execution_risk_score":3,"legal_or_contract_risk_score":2,"dilution_cb_risk_score":1,"accounting_trust_risk_score":1},"weighted_score_before":78,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":4,"backlog_visibility_score":5,"margin_bridge_score":10,"revision_score":7,"relative_strength_score":7,"customer_quality_score":5,"policy_or_regulatory_score":2,"valuation_repricing_score":7,"execution_risk_score":3,"legal_or_contract_risk_score":2,"dilution_cb_risk_score":1,"accounting_trust_risk_score":1},"weighted_score_after":82,"stage_label_after":"Stage3-Yellow","changed_components":["margin_bridge_score","revision_score","execution_risk_score","valuation_repricing_score"],"component_delta_explanation":"C17 shadow profile requires verified input-output spread to margin bridge; label-only commodity spikes are demoted to local 4B watch.","MFE_90D_pct":57.01,"MAE_90D_pct":-8.47,"score_return_alignment_label":"aligned","current_profile_verdict":"current_profile_correct"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C17-L99-02-011780","trigger_id":"C17-L99-02-011780-T1","symbol":"011780","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD","raw_component_scores_before":{"contract_score":4,"backlog_visibility_score":5,"margin_bridge_score":8,"revision_score":6,"relative_strength_score":7,"customer_quality_score":5,"policy_or_regulatory_score":2,"valuation_repricing_score":7,"execution_risk_score":3,"legal_or_contract_risk_score":2,"dilution_cb_risk_score":1,"accounting_trust_risk_score":1},"weighted_score_before":78,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":4,"backlog_visibility_score":5,"margin_bridge_score":10,"revision_score":7,"relative_strength_score":7,"customer_quality_score":5,"policy_or_regulatory_score":2,"valuation_repricing_score":7,"execution_risk_score":3,"legal_or_contract_risk_score":2,"dilution_cb_risk_score":1,"accounting_trust_risk_score":1},"weighted_score_after":82,"stage_label_after":"Stage3-Yellow","changed_components":["margin_bridge_score","revision_score","execution_risk_score","valuation_repricing_score"],"component_delta_explanation":"C17 shadow profile requires verified input-output spread to margin bridge; label-only commodity spikes are demoted to local 4B watch.","MFE_90D_pct":25.69,"MAE_90D_pct":-11.66,"score_return_alignment_label":"aligned","current_profile_verdict":"current_profile_correct"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C17-L99-03-003240","trigger_id":"C17-L99-03-003240-T1","symbol":"003240","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD","raw_component_scores_before":{"contract_score":4,"backlog_visibility_score":5,"margin_bridge_score":8,"revision_score":6,"relative_strength_score":7,"customer_quality_score":5,"policy_or_regulatory_score":2,"valuation_repricing_score":7,"execution_risk_score":3,"legal_or_contract_risk_score":2,"dilution_cb_risk_score":1,"accounting_trust_risk_score":1},"weighted_score_before":78,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":4,"backlog_visibility_score":5,"margin_bridge_score":10,"revision_score":7,"relative_strength_score":7,"customer_quality_score":5,"policy_or_regulatory_score":2,"valuation_repricing_score":7,"execution_risk_score":3,"legal_or_contract_risk_score":2,"dilution_cb_risk_score":1,"accounting_trust_risk_score":1},"weighted_score_after":82,"stage_label_after":"Stage3-Yellow","changed_components":["margin_bridge_score","revision_score","execution_risk_score","valuation_repricing_score"],"component_delta_explanation":"C17 shadow profile requires verified input-output spread to margin bridge; label-only commodity spikes are demoted to local 4B watch.","MFE_90D_pct":7.63,"MAE_90D_pct":-12.52,"score_return_alignment_label":"aligned","current_profile_verdict":"current_profile_missed_structural"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C17-L99-04-014680","trigger_id":"C17-L99-04-014680-T1","symbol":"014680","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD","raw_component_scores_before":{"contract_score":4,"backlog_visibility_score":5,"margin_bridge_score":8,"revision_score":6,"relative_strength_score":7,"customer_quality_score":5,"policy_or_regulatory_score":2,"valuation_repricing_score":7,"execution_risk_score":3,"legal_or_contract_risk_score":2,"dilution_cb_risk_score":1,"accounting_trust_risk_score":1},"weighted_score_before":78,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":4,"backlog_visibility_score":5,"margin_bridge_score":10,"revision_score":7,"relative_strength_score":7,"customer_quality_score":5,"policy_or_regulatory_score":2,"valuation_repricing_score":7,"execution_risk_score":3,"legal_or_contract_risk_score":2,"dilution_cb_risk_score":1,"accounting_trust_risk_score":1},"weighted_score_after":82,"stage_label_after":"Stage3-Yellow","changed_components":["margin_bridge_score","revision_score","execution_risk_score","valuation_repricing_score"],"component_delta_explanation":"C17 shadow profile requires verified input-output spread to margin bridge; label-only commodity spikes are demoted to local 4B watch.","MFE_90D_pct":45.05,"MAE_90D_pct":-14.79,"score_return_alignment_label":"aligned","current_profile_verdict":"current_profile_too_late"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C17-L99-05-011170","trigger_id":"C17-L99-05-011170-T1","symbol":"011170","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD","raw_component_scores_before":{"contract_score":2,"backlog_visibility_score":2,"margin_bridge_score":3,"revision_score":2,"relative_strength_score":6,"customer_quality_score":3,"policy_or_regulatory_score":2,"valuation_repricing_score":6,"execution_risk_score":7,"legal_or_contract_risk_score":5,"dilution_cb_risk_score":1,"accounting_trust_risk_score":1},"weighted_score_before":72,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"contract_score":2,"backlog_visibility_score":2,"margin_bridge_score":1,"revision_score":2,"relative_strength_score":6,"customer_quality_score":3,"policy_or_regulatory_score":2,"valuation_repricing_score":4,"execution_risk_score":9,"legal_or_contract_risk_score":5,"dilution_cb_risk_score":1,"accounting_trust_risk_score":1},"weighted_score_after":63,"stage_label_after":"Stage2","changed_components":["margin_bridge_score","revision_score","execution_risk_score","valuation_repricing_score"],"component_delta_explanation":"C17 shadow profile requires verified input-output spread to margin bridge; label-only commodity spikes are demoted to local 4B watch.","MFE_90D_pct":3.46,"MAE_90D_pct":-20.77,"score_return_alignment_label":"profile_false_positive_before_shadow_guard","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C17-L99-06-006650","trigger_id":"C17-L99-06-006650-T1","symbol":"006650","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD","raw_component_scores_before":{"contract_score":2,"backlog_visibility_score":2,"margin_bridge_score":3,"revision_score":2,"relative_strength_score":6,"customer_quality_score":3,"policy_or_regulatory_score":2,"valuation_repricing_score":6,"execution_risk_score":7,"legal_or_contract_risk_score":5,"dilution_cb_risk_score":1,"accounting_trust_risk_score":1},"weighted_score_before":77,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":2,"backlog_visibility_score":2,"margin_bridge_score":1,"revision_score":2,"relative_strength_score":6,"customer_quality_score":3,"policy_or_regulatory_score":2,"valuation_repricing_score":4,"execution_risk_score":9,"legal_or_contract_risk_score":5,"dilution_cb_risk_score":1,"accounting_trust_risk_score":1},"weighted_score_after":63,"stage_label_after":"Stage2","changed_components":["margin_bridge_score","revision_score","execution_risk_score","valuation_repricing_score"],"component_delta_explanation":"C17 shadow profile requires verified input-output spread to margin bridge; label-only commodity spikes are demoted to local 4B watch.","MFE_90D_pct":5.48,"MAE_90D_pct":-39.67,"score_return_alignment_label":"profile_false_positive_before_shadow_guard","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C17-L99-07-009830","trigger_id":"C17-L99-07-009830-T1","symbol":"009830","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD","raw_component_scores_before":{"contract_score":2,"backlog_visibility_score":2,"margin_bridge_score":3,"revision_score":2,"relative_strength_score":6,"customer_quality_score":3,"policy_or_regulatory_score":5,"valuation_repricing_score":6,"execution_risk_score":7,"legal_or_contract_risk_score":5,"dilution_cb_risk_score":1,"accounting_trust_risk_score":1},"weighted_score_before":72,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"contract_score":2,"backlog_visibility_score":2,"margin_bridge_score":1,"revision_score":2,"relative_strength_score":6,"customer_quality_score":3,"policy_or_regulatory_score":5,"valuation_repricing_score":4,"execution_risk_score":9,"legal_or_contract_risk_score":5,"dilution_cb_risk_score":1,"accounting_trust_risk_score":1},"weighted_score_after":63,"stage_label_after":"Stage2","changed_components":["margin_bridge_score","revision_score","execution_risk_score","valuation_repricing_score"],"component_delta_explanation":"C17 shadow profile requires verified input-output spread to margin bridge; label-only commodity spikes are demoted to local 4B watch.","MFE_90D_pct":9.06,"MAE_90D_pct":-29.57,"score_return_alignment_label":"profile_false_positive_before_shadow_guard","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C17-L99-08-025000","trigger_id":"C17-L99-08-025000-T1","symbol":"025000","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD","raw_component_scores_before":{"contract_score":2,"backlog_visibility_score":2,"margin_bridge_score":3,"revision_score":2,"relative_strength_score":6,"customer_quality_score":3,"policy_or_regulatory_score":2,"valuation_repricing_score":6,"execution_risk_score":7,"legal_or_contract_risk_score":5,"dilution_cb_risk_score":1,"accounting_trust_risk_score":1},"weighted_score_before":77,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":2,"backlog_visibility_score":2,"margin_bridge_score":1,"revision_score":2,"relative_strength_score":6,"customer_quality_score":3,"policy_or_regulatory_score":2,"valuation_repricing_score":4,"execution_risk_score":9,"legal_or_contract_risk_score":5,"dilution_cb_risk_score":1,"accounting_trust_risk_score":1},"weighted_score_after":63,"stage_label_after":"Stage2","changed_components":["margin_bridge_score","revision_score","execution_risk_score","valuation_repricing_score"],"component_delta_explanation":"C17 shadow profile requires verified input-output spread to margin bridge; label-only commodity spikes are demoted to local 4B watch.","MFE_90D_pct":3.45,"MAE_90D_pct":-12.23,"score_return_alignment_label":"profile_false_positive_before_shadow_guard","current_profile_verdict":"current_profile_false_positive"}
{"profile_id":"P0_e2r_2_1_stock_web_calibrated_proxy","profile_scope":"current_proxy","profile_hypothesis":"current profile allows some commodity spread labels if total score crosses Yellow","eligible_trigger_count":8,"avg_MFE_90D_pct":19.6,"avg_MAE_90D_pct":-18.71,"avg_MFE_180D_pct":35.37,"avg_MAE_180D_pct":-29.43,"false_positive_rate":0.5,"missed_structural_count":2,"score_return_alignment_verdict":"mixed","row_type":"profile_comparison","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD"}
{"profile_id":"P0b_e2r_2_0_baseline_reference","profile_scope":"rollback_reference","profile_hypothesis":"older profile over-credits relative strength and broad commodity rebound","eligible_trigger_count":8,"avg_MFE_90D_pct":19.6,"avg_MAE_90D_pct":-18.71,"avg_MFE_180D_pct":35.37,"avg_MAE_180D_pct":-29.43,"false_positive_rate":0.62,"missed_structural_count":1,"score_return_alignment_verdict":"weaker_than_P0","row_type":"profile_comparison","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD"}
{"profile_id":"P1_L4_materials_sector_shadow","profile_scope":"sector_specific","profile_hypothesis":"L4 spread cases need explicit spread-to-margin or volume bridge; source-proxy labels stay watch","eligible_trigger_count":8,"avg_MFE_90D_pct":33.84,"avg_MAE_90D_pct":-11.86,"avg_MFE_180D_pct":65.38,"avg_MAE_180D_pct":-15.36,"false_positive_rate":0.25,"missed_structural_count":1,"score_return_alignment_verdict":"improves_alignment","row_type":"profile_comparison","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD"}
{"profile_id":"P2_C17_canonical_shadow","profile_scope":"canonical_archetype_specific","profile_hypothesis":"C17 label-only commodity rebound is insufficient unless spread bridge is confirmed","eligible_trigger_count":8,"avg_MFE_90D_pct":33.84,"avg_MAE_90D_pct":-11.86,"avg_MFE_180D_pct":65.38,"avg_MAE_180D_pct":-15.36,"false_positive_rate":0.12,"missed_structural_count":1,"score_return_alignment_verdict":"best_shadow_alignment","row_type":"profile_comparison","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD"}
{"profile_id":"P3_counterexample_guard_profile","profile_scope":"canonical_guard","profile_hypothesis":"if MFE90 stays under 10 and MAE90 breaches -20, route label-only C17 to local 4B/4C watch","eligible_trigger_count":4,"avg_MFE_90D_pct":5.36,"avg_MAE_90D_pct":-25.56,"avg_MFE_180D_pct":5.36,"avg_MAE_180D_pct":-43.49,"false_positive_rate":0.0,"missed_structural_count":0,"score_return_alignment_verdict":"guardrail_only","row_type":"profile_comparison","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD"}
{"row_type":"residual_contribution","round":"R4","loop":"99","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD","new_independent_case_count":8,"reused_case_count":0,"new_symbol_count":8,"new_trigger_family_count":8,"tested_existing_calibrated_axes":["stage2_required_bridge","local_4b_watch_guard","price_only_blowoff_blocks_positive_stage","full_4b_requires_non_price_evidence","hard_4c_confirmation"],"residual_error_types_found":["commodity_label_false_positive","spread_to_margin_bridge_missing","specialty_chemical_missed_structural","high_MAE_commodity_rebound"],"new_axis_proposed":"C17_verified_input_output_spread_margin_bridge_required_before_Yellow_or_Green_plus_commodity_label_spike_to_local_4B_or_4C_watch","existing_axis_strengthened":["stage2_required_bridge","local_4b_watch_guard","full_4b_requires_non_price_evidence"],"existing_axis_weakened":["hard_4c_thesis_break_routes_to_4c_when_only_generic_chemical_spread_label_is_present"],"loop_contribution_label":"canonical_archetype_rule_candidate","do_not_propose_new_weight_delta":false}
```

## 26. Deferred Coding Agent Handoff Prompt

### Purpose
You are now in the repository implementation phase. The attached Markdown files are v12 post-calibrated residual research outputs produced using the Songdaiki/stock-web OHLC atlas. These MDs are not live candidate research. They are historical calibration research designed to extend the already-applied e2r_2_1_stock_web_calibrated profile. Do not blindly apply every shadow row. Ingest the machine-readable rows and update the sector/canonical-archetype calibration ledger.

### Price source context
- Primary historical price source used by the research MD: Songdaiki/stock-web.
- Price basis: tradable_raw.
- Price adjustment status: raw_unadjusted_marcap.
- Price shard pattern: atlas/ohlcv_tradable_by_symbol_year/{prefix}/{symbol}/{year}.csv.
- Symbol profile pattern: atlas/symbol_profiles/{prefix}/{symbol}.json.

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
completed_loop = 99
selection_basis = docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket = Priority 2 quality_repair_after_local_priority0_priority1_fill
next_recommended_archetypes = C17_CHEMICAL_COMMODITY_MARGIN_SPREAD, C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY, C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG, C16_STRATEGIC_RESOURCE_POLICY_SUPPLY, C18_CONSUMER_EXPORT_CHANNEL_REORDER, C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION
round_schedule_status = coverage_index_selected
round_sector_consistency = pass
```

## 28. Source Notes

- `docs/core/e2r_v12_prompt_round_scheduler_corrected.txt` was used as the execution procedure.
- `docs/core/V12_Research_No_Repeat_Index.md` was used only as the duplicate/coverage ledger.
- `Songdaiki/stock-web/atlas/manifest.json` and tradable CSV shards were used for historical OHLC calculations.

## Batch Ingest Self-Audit

```text
expected_v12_result_file: true
filename_pattern_pass: true
metadata_filename_consistency: pass
jsonl_trigger_row_count: 8
calibration_usable_trigger_count: 8
representative_trigger_count: 8
new_weight_evidence_candidate_count: 8
guardrail_candidate_count: 8
narrative_only_or_rejected_count: 0
rows_missing_required_mfe_mae: 0
rows_missing_entry_price_or_date: 0
rows_with_noncanonical_trigger_type: 0
rows_with_compact_mfe_mae_alias_only: 0
ready_for_batch_ingest: true
```
