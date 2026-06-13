# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
selected_round = R2
selected_loop = 143
selection_basis = docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket = Priority 0
round_schedule_status = coverage_index_selected_not_sequential
round_sector_consistency = pass
large_sector_id = L2_AI_SEMICONDUCTOR_ELECTRONICS
canonical_archetype_id = C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF
fine_archetype_id = mixed_c09_advanced_equipment_order_qualification_ladder_leaf_set
loop_objective = coverage_gap_fill|counterexample_mining|4B_non_price_requirement_stress_test|canonical_archetype_compression|sector_specific_rule_discovery
price_source = Songdaiki/stock-web
stock_web_manifest_max_date = 2026-02-20
production_scoring_changed = false
shadow_weight_only = true
```

## 1. Current Calibrated Profile Assumption

Current proxy is `e2r_2_1_stock_web_calibrated_proxy`; this MD does not patch production scoring. Applied global axes are treated as assumptions, then stress-tested inside C09 only.

## 2. Round / Large Sector / Canonical Archetype Scope

C09 sits in R2/L2. The selected scope is advanced semiconductor equipment where valuation blowoff, qualification-only narratives, and order-backed exceptions must be separated.

## 3. Previous Coverage / Duplicate Avoidance Check

No-Repeat Index baseline lists C09 as Priority 0 with 10 rows, needing 20 more to 30. This loop avoids prior session C09 symbols DIT, Park Systems, YC, Auros, Intekplus, Hanmi, HPSP, YEST, Laserssel, and Neosem. New symbols here are 039030, 036930, 168360, 348210, 083310, 053610, and 098460.

index baseline C09 rows 10 -> 17 if accepted; session-aware after loop126 + loop135 + loop143 ≈ 29 representative rows.

## 4. Stock-Web OHLC Input / Price Source Validation

Manifest fields used: `source_name=FinanceData/marcap`, `price_basis=tradable_raw`, `price_adjustment_status=raw_unadjusted_marcap`, `calibration_shard_root=atlas/ohlcv_tradable_by_symbol_year`, `max_date=2026-02-20`. All trigger rows below have 180 trading-day forward windows and clean 180D corporate-action windows.

## 5. Historical Eligibility Gate

| symbol | company | shard | profile | corporate_action_window_status |
| --- | --- | --- | --- | --- |
| 039030 | 이오테크닉스 | atlas/ohlcv_tradable_by_symbol_year/039/039030/2023.csv | atlas/symbol_profiles/039/039030.json | clean_180D_window |
| 036930 | 주성엔지니어링 | atlas/ohlcv_tradable_by_symbol_year/036/036930/2024.csv | atlas/symbol_profiles/036/036930.json | clean_180D_window |
| 168360 | 펨트론 | atlas/ohlcv_tradable_by_symbol_year/168/168360/2024.csv | atlas/symbol_profiles/168/168360.json | clean_180D_window |
| 348210 | 넥스틴 | atlas/ohlcv_tradable_by_symbol_year/348/348210/2025.csv | atlas/symbol_profiles/348/348210.json | clean_180D_window |
| 083310 | 엘오티베큠 | atlas/ohlcv_tradable_by_symbol_year/083/083310/2024.csv | atlas/symbol_profiles/083/083310.json | clean_180D_window |
| 053610 | 프로텍 | atlas/ohlcv_tradable_by_symbol_year/053/053610/2024.csv | atlas/symbol_profiles/053/053610.json | clean_180D_window |
| 098460 | 고영 | atlas/ohlcv_tradable_by_symbol_year/098/098460/2024.csv | atlas/symbol_profiles/098/098460.json | clean_180D_window |

## 6. Canonical Archetype Compression Map

- `HBM_LASER_ANNEALING_ADVANCED_EQUIPMENT_EARLY_ROUTE` -> `C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF`: laser_annealing_grooving_hbm_route_positive.
- `ALD_MEMORY_CAPA_UNIT_ORDER_INCREASE_ROUTE` -> `C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF`: ald_memory_capa_order_bridge_positive_high_mae.
- `HBM_INSPECTION_QUALITY_TEST_TO_COMMERCIALIZATION_ROUTE` -> `C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF`: hbm_inspection_quality_test_missed_structural_positive.
- `ADVANCED_INSPECTION_KROKY_ASPER_CUSTOMER_ROUTE` -> `C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF`: kroky_asper_customer_route_positive_but_late_mae.
- `VACUUM_EQUIPMENT_HBM_DDR5_CONVERSION_INVESTMENT_ROUTE` -> `C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF`: vacuum_equipment_conversion_investment_positive.
- `LASER_BONDER_AI_HBM_PRODUCTION_TIMING_HYPE` -> `C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF`: laser_bonder_production_timing_false_positive.
- `SEMICONDUCTOR_INSPECTION_MIXED_CORE_DEMAND_MISS` -> `C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF`: semiconductor_inspection_growth_inside_core_demand_miss_false_positive.

## 7. Case Selection Summary

| symbol | company | trigger_date | entry_date | trigger_type | outcome | MFE90 | MAE90 | MFE180 | MAE180 | verdict |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 039030 | 이오테크닉스 | 2023-09-06 | 2023-09-07 | Stage2-Actionable | positive | 26.6 | -20.01 | 71.45 | -20.01 | current_profile_correct_with_4B_exit_needed |
| 036930 | 주성엔지니어링 | 2024-08-27 | 2024-08-28 | Stage2-Actionable | positive | 21.39 | -21.39 | 54.72 | -21.39 | current_profile_too_early |
| 168360 | 펨트론 | 2024-12-02 | 2024-12-03 | Stage2 | positive | 126.56 | -25.31 | 137.03 | -25.31 | current_profile_missed_structural |
| 348210 | 넥스틴 | 2025-04-22 | 2025-04-23 | Stage2 | positive | 4.67 | -26.84 | 37.52 | -26.84 | current_profile_too_early |
| 083310 | 엘오티베큠 | 2024-12-10 | 2024-12-11 | Stage2-Actionable | positive | 31.95 | -6.71 | 49.15 | -6.71 | current_profile_correct |
| 053610 | 프로텍 | 2024-08-19 | 2024-08-20 | Stage2 | counterexample | 7.39 | -34.75 | 7.39 | -37.36 | current_profile_false_positive |
| 098460 | 고영 | 2024-05-03 | 2024-05-07 | Stage2 | counterexample | 4.81 | -39.58 | 12.44 | -51.19 | current_profile_false_positive |

## 8. Positive vs Counterexample Balance

Positive cases: 5. Counterexamples: 2. Positives averaged MFE90 42.23% / MAE90 -20.05%, while counterexamples averaged MFE90 6.1% / MAE90 -37.16%. The split is useful because C09 is not simply a short/avoid bucket: order-backed or real customer-route equipment names can work, but narrative-only equipment exposure can crush entries.

## 9. Evidence Source Map

| symbol | company | trigger_date | evidence_source | evidence_family |
| --- | --- | --- | --- | --- |
| 039030 | 이오테크닉스 | 2023-09-06 | https://v.daum.net/v/plgvYIJG0e | laser_annealing_grooving_hbm_route_positive |
| 036930 | 주성엔지니어링 | 2024-08-27 | https://www.sks.co.kr/data1/research/qna_file/20240826143929688_0_ko.pdf | ald_memory_capa_order_bridge_positive_high_mae |
| 168360 | 펨트론 | 2024-12-02 | https://v.daum.net/v/GP7PE0HERO?f=p | hbm_inspection_quality_test_missed_structural_positive |
| 348210 | 넥스틴 | 2025-04-22 | https://w4.kirs.or.kr/download/research/250422_%EB%84%A5%EC%8A%A4%ED%8B%B4%28%EA%B8%80%EC%84%B8%29_%EC%B5%9C%EC%A2%85.pdf | kroky_asper_customer_route_positive_but_late_mae |
| 083310 | 엘오티베큠 | 2024-12-10 | https://w4.kirs.or.kr/download/research/241210_%EC%97%98%EC%98%A4%ED%8B%B0%EB%B2%A0%ED%81%A0-%EB%9D%BC%EC%9D%B4%EC%A7%95%EC%8A%A4%ED%83%80.pdf | vacuum_equipment_conversion_investment_positive |
| 053610 | 프로텍 | 2024-08-19 | https://stock.pstatic.net/stock-research/company/72/20240819_company_970470000.pdf | laser_bonder_production_timing_false_positive |
| 098460 | 고영 | 2024-05-03 | https://www.newspim.com/news/view/20240503000144 | semiconductor_inspection_growth_inside_core_demand_miss_false_positive |

## 10. Price Data Source Map

All OHLC rows were computed from locally downloaded stock-web raw CSV shards after first viewing the raw shard URLs in this session. Entry uses close price on the selected entry_date.

## 11. Case-by-Case Trigger Grid

### 039030 이오테크닉스 — laser_annealing_grooving_hbm_route_positive
- trigger: 2023-09-06 / entry: 2023-09-07 close 163900.0
- evidence fields: existing laser annealing supply route, HBM3/HBM3E CAPA linkage, grooving/stealth dicing expansion
- stage3 fields: customer process exposure, technology bottleneck
- 4B fields: full-window overheat after 180D peak
- 4C fields: none
- current profile verdict: current_profile_correct_with_4B_exit_needed

### 036930 주성엔지니어링 — ald_memory_capa_order_bridge_positive_high_mae
- trigger: 2024-08-27 / entry: 2024-08-28 close 28050.0
- evidence fields: ALD equipment exposure, Samsung/SK Hynix customer exposure, 2025 DRAM investment recovery bridge
- stage3 fields: unit order amount increase, memory capex cycle
- 4B fields: entry MAE guard required
- 4C fields: none
- current profile verdict: current_profile_too_early

### 168360 펨트론 — hbm_inspection_quality_test_missed_structural_positive
- trigger: 2024-12-02 / entry: 2024-12-03 close 6400.0
- evidence fields: HBM inspection equipment contract/use agreement, quality-test start, unique 3D inspection technology
- stage3 fields: commercialization path still early
- 4B fields: high volatility and later 4B exit guard
- 4C fields: none
- current profile verdict: current_profile_missed_structural

### 348210 넥스틴 — kroky_asper_customer_route_positive_but_late_mae
- trigger: 2025-04-22 / entry: 2025-04-23 close 55700.0
- evidence fields: KROKY advanced memory package inspection, major memory maker supply expectation, ASPER customer diversification
- stage3 fields: new equipment mix expected to rise later
- 4B fields: 90D high-MAE guard
- 4C fields: none
- current profile verdict: current_profile_too_early

### 083310 엘오티베큠 — vacuum_equipment_conversion_investment_positive
- trigger: 2024-12-10 / entry: 2024-12-11 close 8200.0
- evidence fields: HBM/DDR5 conversion investment, vacuum pump equipment exposure, semiconductor capex recovery
- stage3 fields: revenue conversion visible through equipment demand
- 4B fields: none
- 4C fields: none
- current profile verdict: current_profile_correct

### 053610 프로텍 — laser_bonder_production_timing_false_positive
- trigger: 2024-08-19 / entry: 2024-08-20 close 31800.0
- evidence fields: AI semiconductor laser bonder development, expected end-2024 production, Samsung/SK Hynix starting customer wording
- stage3 fields: none
- 4B fields: non-price execution risk and legal/accounting overhang
- 4C fields: 180D thesis drawdown confirmed
- current profile verdict: current_profile_false_positive

### 098460 고영 — semiconductor_inspection_growth_inside_core_demand_miss_false_positive
- trigger: 2024-05-03 / entry: 2024-05-07 close 15590.0
- evidence fields: semiconductor inspection equipment revenue growth, multi-purpose inspection product growth
- stage3 fields: none
- 4B fields: core automotive/server/IoT customer demand weakness
- 4C fields: earnings miss and 180D drawdown
- current profile verdict: current_profile_false_positive

## 12. Trigger-Level OHLC Backtest Tables

| trigger_id | entry_price | MFE30 | MAE30 | MFE90 | MAE90 | MFE180 | MAE180 | peak_date | peak_price | DD_after_peak |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| T_C09_L143_039030_LASER_ANNEALING_EARLY | 163900.0 | 1.59 | -20.01 | 26.6 | -20.01 | 71.45 | -20.01 | 2024-04-12 | 281000.0 | -30.82 |
| T_C09_L143_036930_ALD_MEMORY_CAPA | 28050.0 | 2.5 | -21.39 | 21.39 | -21.39 | 54.72 | -21.39 | 2025-03-21 | 43400.0 | -29.03 |
| T_C09_L143_168360_HBM_INSPECTION_QUALIFICATION | 6400.0 | 36.56 | -25.31 | 126.56 | -25.31 | 137.03 | -25.31 | 2025-06-27 | 15170.0 | -35.73 |
| T_C09_L143_348210_KROKY_ASPER_ROUTE | 55700.0 | 4.67 | -8.08 | 4.67 | -26.84 | 37.52 | -26.84 | 2025-12-05 | 76600.0 | -15.67 |
| T_C09_L143_083310_VACUUM_HBM_DDR5_CONVERSION | 8200.0 | 22.8 | -4.63 | 31.95 | -6.71 | 49.15 | -6.71 | 2025-08-29 | 12230.0 | -6.87 |
| T_C09_L143_053610_LASER_BONDER_HYPE | 31800.0 | 3.3 | -27.67 | 7.39 | -34.75 | 7.39 | -37.36 | 2024-11-06 | 34150.0 | -41.67 |
| T_C09_L143_098460_INSPECTION_MIXED_1Q24 | 15590.0 | 4.81 | -22.0 | 4.81 | -39.58 | 12.44 | -51.19 | 2025-02-03 | 17530.0 | -9.24 |

## 13. Current Calibrated Profile Stress Test

The calibrated Stage2 evidence bonus works for true customer/equipment routes, but C09 still needs a qualification ladder. Protec and Koh Young show that AI/HBM/inspection language without signed commercial bridge or margin conversion produces low MFE and deep MAE. Pemtron is the counter-pressure: qualification language can be early but real when a specific HBM inspection use agreement and quality-test route exists.

## 14. Stage2 / Yellow / Green Comparison

No confirmed Stage3-Green trigger is used as representative. For positives, Stage2/Stage2-Actionable captured most of the 180D upside before Green-quality confirmation. For C09, Green strictness should remain high; the earlier action is Stage2-Watch/Actionable only when commercial bridge is visible.

## 15. 4B Local vs Full-window Timing Audit

Eo Technics and Pemtron both show later drawdown after strong MFE; Protec and Koh Young show that a full 4B/4C watch should be driven by execution/earnings weakness rather than price-only local peak. The C09 rule should keep local price-only 4B as watch, then escalate if qualification/revenue bridge fails.

## 16. 4C Protection Audit

Protec and Koh Young are 4C-watch candidates because non-price weakness appeared with poor forward path. They do not prove immediate hard 4C on every C09 narrative; they prove that absence of order/revenue/margin bridge should block Stage2-Actionable.

## 17. Sector-Specific Rule Candidate

`L2_ADVANCED_EQUIPMENT_COMMERCIAL_BRIDGE_AND_QUALIFICATION_LADDER_GATE_V1`: In L2 equipment, Stage2-Actionable requires either named customer/order evidence, already-shipping equipment route, or explicit quality-test/use-agreement path plus revenue/margin timing. Pure HBM/AI/advanced-packaging vocabulary remains Stage2-Watch or 4B-Watch.

## 18. Canonical-Archetype Rule Candidate

`C09_ORDER_BACKED_EXCEPTION_VS_QUALIFICATION_ONLY_BLOWOFF_GATE_V3`: C09 should not be a permanent penalty bucket. It should admit order-backed exceptions while penalizing qualification-only, pilot-only, or theme-only blowoffs until customer, shipment, revenue, or margin conversion is visible.

## 19. Before / After Backtest Comparison

| profile_id | eligible_trigger_count | selected | avg_MFE_90D_pct | avg_MAE_90D_pct | avg_MFE_180D_pct | avg_MAE_180D_pct | false_positive_rate | verdict |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| P0 e2r_2_1_stock_web_calibrated_proxy | 7 | all 7 | 31.91 | -24.94 | 52.81 | -26.97 | 2/7 | mixed; broad advanced-equipment vocabulary still lets false positives through |
| P0b e2r_2_0_baseline_reference | 7 | mostly theme/RS | 31.91 | -24.94 | 52.81 | -26.97 | higher | too permissive on valuation/narrative |
| P1 L2 sector candidate | 5 | drops 053610/098460 | 42.23 | -20.05 | 69.97 | -20.05 | 0/5 in this loop | improves score-return alignment |
| P2 C09 canonical candidate | 5 | order/customer/revenue bridge routes | 42.23 | -20.05 | 69.97 | -20.05 | 0/5 in this loop | best canonical compression |
| P3 counterexample guard | 2 | 053610/098460 blocked | 6.1 | -37.16 | 9.91 | -44.27 | guard-only | blocks low-MFE/high-MAE narratives |

## 20. Score-Return Alignment Matrix

The C09 shadow gate improves alignment by filtering the two high-MAE false positives while keeping the five cases where identifiable equipment route or conversion bridge existed. This is not a global delta; it is a C09-specific compression rule.

## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive_case_count | counterexample_count | 4B_case_count | 4C_case_count | new_independent_case_count | reused_case_count | calibration_usable_trigger_count | representative_trigger_count | current_profile_error_count | sector_rule_candidate | canonical_rule_candidate | coverage_gap_after_this_loop |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| L2_AI_SEMICONDUCTOR_ELECTRONICS | C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF | mixed_c09_advanced_equipment_order_qualification_ladder_leaf_set | 5 | 2 | 5 | 2 | 7 | 0 | 7 | 7 | 5 | L2_ADVANCED_EQUIPMENT_COMMERCIAL_BRIDGE_AND_QUALIFICATION_LADDER_GATE_V1 | C09_ORDER_BACKED_EXCEPTION_VS_QUALIFICATION_ONLY_BLOWOFF_GATE_V3 | index baseline C09 rows 10 -> 17 if accepted; session-aware after loop126 + loop135 + loop143 ≈ 29 representative rows |

## 22. Residual Contribution Summary

```text
new_independent_case_count: 7
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 7
new_canonical_archetype_count: 0
new_fine_archetype_count: 7
new_trigger_family_count: 7
tested_existing_calibrated_axes: stage2_actionable_evidence_bonus|price_only_blowoff_blocks_positive_stage|full_4b_requires_non_price_evidence|hard_4c_thesis_break_routes_to_4c
residual_error_types_found: qualification_only_false_positive|late_high_MAE_entry|missed_structural_from_quality_test|execution_overhang_4C_watch
new_axis_proposed: c09_order_backed_exception_vs_qualification_only_blowoff_gate_v3
existing_axis_strengthened: price_only_blowoff_blocks_positive_stage|full_4b_requires_non_price_evidence
existing_axis_weakened: null
existing_axis_kept: stage3_green_total_min|stage3_green_revision_min|hard_4c_thesis_break_routes_to_4c
sector_specific_rule_candidate: L2_ADVANCED_EQUIPMENT_COMMERCIAL_BRIDGE_AND_QUALIFICATION_LADDER_GATE_V1
canonical_archetype_rule_candidate: C09_ORDER_BACKED_EXCEPTION_VS_QUALIFICATION_ONLY_BLOWOFF_GATE_V3
no_new_signal_reason: null
loop_contribution_label: canonical_archetype_rule_candidate
do_not_propose_new_weight_delta: false
```

## 23. Validation Scope / Non-Validation Scope

Validation scope: historical 1D OHLC path, clean 180D windows, C09 archetype-specific scoring stress. Non-validation scope: no live recommendation, no current candidate scan, no production patch, no brokerage/API action.

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes

shadow_weight,c09_order_backed_exception_vs_qualification_only_blowoff_gate,canonical_archetype_specific,L2_AI_SEMICONDUCTOR_ELECTRONICS,C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF,0,1,+1,"separate order/customer route from qualification-only blowoff","filtered 2 false positives while retaining 5 positives","T_C09_L143_039030_LASER_ANNEALING_EARLY|T_C09_L143_036930_ALD_MEMORY_CAPA|T_C09_L143_168360_HBM_INSPECTION_QUALIFICATION|T_C09_L143_348210_KROKY_ASPER_ROUTE|T_C09_L143_083310_VACUUM_HBM_DDR5_CONVERSION|T_C09_L143_053610_LASER_BONDER_HYPE|T_C09_L143_098460_INSPECTION_MIXED_1Q24",7,7,2,medium,canonical_shadow_only,"not production; post-calibrated residual"
```

## 25. Machine-Readable Rows

```jsonl

{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}

{"row_type":"case","case_id":"C09_L143_039030_LASER_ANNEALING_EARLY","symbol":"039030","company_name":"이오테크닉스","round":"R2","loop":"143","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF","fine_archetype_id":"HBM_LASER_ANNEALING_ADVANCED_EQUIPMENT_EARLY_ROUTE","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"Stage2-Actionable","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"aligned_positive","current_profile_verdict":"current_profile_correct_with_4B_exit_needed","price_source":"Songdaiki/stock-web","notes":"laser_annealing_grooving_hbm_route_positive"}

{"row_type":"trigger","trigger_id":"T_C09_L143_039030_LASER_ANNEALING_EARLY","case_id":"C09_L143_039030_LASER_ANNEALING_EARLY","symbol":"039030","company_name":"이오테크닉스","round":"R2","loop":"143","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF","fine_archetype_id":"HBM_LASER_ANNEALING_ADVANCED_EQUIPMENT_EARLY_ROUTE","sector":"AI/semiconductor/equipment","primary_archetype":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF","loop_objective":"coverage_gap_fill|counterexample_mining|4B_non_price_requirement_stress_test|canonical_archetype_compression|sector_specific_rule_discovery","trigger_type":"Stage2-Actionable","trigger_date":"2023-09-06","entry_date":"2023-09-07","entry_price":163900.0,"evidence_available_at_that_date":"published_or_available_on_trigger_date; next-trading-day close if timing unclear","evidence_source":"https://v.daum.net/v/plgvYIJG0e","stage2_evidence_fields":["existing laser annealing supply route","HBM3/HBM3E CAPA linkage","grooving/stealth dicing expansion"],"stage3_evidence_fields":["customer process exposure","technology bottleneck"],"stage4b_evidence_fields":["full-window overheat after 180D peak"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/039/039030/2023.csv","profile_path":"atlas/symbol_profiles/039/039030.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":1.59,"MFE_90D_pct":26.6,"MFE_180D_pct":71.45,"MFE_1Y_pct":71.45,"MFE_2Y_pct":null,"MAE_30D_pct":-20.01,"MAE_90D_pct":-20.01,"MAE_180D_pct":-20.01,"MAE_1Y_pct":-21.05,"MAE_2Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-04-12","peak_price":281000.0,"drawdown_after_peak_pct":-30.82,"green_lateness_ratio":null,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"4B_exit_guard_needed","four_b_evidence_type":["full-window overheat after 180D peak"],"four_c_protection_label":"not_applicable","trigger_outcome_label":"laser_annealing_grooving_hbm_route_positive","current_profile_verdict":"current_profile_correct_with_4B_exit_needed","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C09_L143_039030_LASER_ANNEALING_EARLY|2023-09-07","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}

{"row_type":"case","case_id":"C09_L143_036930_ALD_MEMORY_CAPA","symbol":"036930","company_name":"주성엔지니어링","round":"R2","loop":"143","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF","fine_archetype_id":"ALD_MEMORY_CAPA_UNIT_ORDER_INCREASE_ROUTE","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"Stage2-Actionable","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"aligned_positive","current_profile_verdict":"current_profile_too_early","price_source":"Songdaiki/stock-web","notes":"ald_memory_capa_order_bridge_positive_high_mae"}

{"row_type":"trigger","trigger_id":"T_C09_L143_036930_ALD_MEMORY_CAPA","case_id":"C09_L143_036930_ALD_MEMORY_CAPA","symbol":"036930","company_name":"주성엔지니어링","round":"R2","loop":"143","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF","fine_archetype_id":"ALD_MEMORY_CAPA_UNIT_ORDER_INCREASE_ROUTE","sector":"AI/semiconductor/equipment","primary_archetype":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF","loop_objective":"coverage_gap_fill|counterexample_mining|4B_non_price_requirement_stress_test|canonical_archetype_compression|sector_specific_rule_discovery","trigger_type":"Stage2-Actionable","trigger_date":"2024-08-27","entry_date":"2024-08-28","entry_price":28050.0,"evidence_available_at_that_date":"published_or_available_on_trigger_date; next-trading-day close if timing unclear","evidence_source":"https://www.sks.co.kr/data1/research/qna_file/20240826143929688_0_ko.pdf","stage2_evidence_fields":["ALD equipment exposure","Samsung/SK Hynix customer exposure","2025 DRAM investment recovery bridge"],"stage3_evidence_fields":["unit order amount increase","memory capex cycle"],"stage4b_evidence_fields":["entry MAE guard required"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/036/036930/2024.csv","profile_path":"atlas/symbol_profiles/036/036930.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":2.5,"MFE_90D_pct":21.39,"MFE_180D_pct":54.72,"MFE_1Y_pct":54.72,"MFE_2Y_pct":null,"MAE_30D_pct":-21.39,"MAE_90D_pct":-21.39,"MAE_180D_pct":-21.39,"MAE_1Y_pct":-21.39,"MAE_2Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2025-03-21","peak_price":43400.0,"drawdown_after_peak_pct":-29.03,"green_lateness_ratio":null,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"4B_exit_guard_needed","four_b_evidence_type":["entry MAE guard required"],"four_c_protection_label":"not_applicable","trigger_outcome_label":"ald_memory_capa_order_bridge_positive_high_mae","current_profile_verdict":"current_profile_too_early","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C09_L143_036930_ALD_MEMORY_CAPA|2024-08-28","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}

{"row_type":"case","case_id":"C09_L143_168360_HBM_INSPECTION_QUALIFICATION","symbol":"168360","company_name":"펨트론","round":"R2","loop":"143","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF","fine_archetype_id":"HBM_INSPECTION_QUALITY_TEST_TO_COMMERCIALIZATION_ROUTE","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"Stage2","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"aligned_positive","current_profile_verdict":"current_profile_missed_structural","price_source":"Songdaiki/stock-web","notes":"hbm_inspection_quality_test_missed_structural_positive"}

{"row_type":"trigger","trigger_id":"T_C09_L143_168360_HBM_INSPECTION_QUALIFICATION","case_id":"C09_L143_168360_HBM_INSPECTION_QUALIFICATION","symbol":"168360","company_name":"펨트론","round":"R2","loop":"143","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF","fine_archetype_id":"HBM_INSPECTION_QUALITY_TEST_TO_COMMERCIALIZATION_ROUTE","sector":"AI/semiconductor/equipment","primary_archetype":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF","loop_objective":"coverage_gap_fill|counterexample_mining|4B_non_price_requirement_stress_test|canonical_archetype_compression|sector_specific_rule_discovery","trigger_type":"Stage2","trigger_date":"2024-12-02","entry_date":"2024-12-03","entry_price":6400.0,"evidence_available_at_that_date":"published_or_available_on_trigger_date; next-trading-day close if timing unclear","evidence_source":"https://v.daum.net/v/GP7PE0HERO?f=p","stage2_evidence_fields":["HBM inspection equipment contract/use agreement","quality-test start","unique 3D inspection technology"],"stage3_evidence_fields":["commercialization path still early"],"stage4b_evidence_fields":["high volatility and later 4B exit guard"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/168/168360/2024.csv","profile_path":"atlas/symbol_profiles/168/168360.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":36.56,"MFE_90D_pct":126.56,"MFE_180D_pct":137.03,"MFE_1Y_pct":279.69,"MFE_2Y_pct":null,"MAE_30D_pct":-25.31,"MAE_90D_pct":-25.31,"MAE_180D_pct":-25.31,"MAE_1Y_pct":-25.31,"MAE_2Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2025-06-27","peak_price":15170.0,"drawdown_after_peak_pct":-35.73,"green_lateness_ratio":null,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"4B_exit_guard_needed","four_b_evidence_type":["high volatility and later 4B exit guard"],"four_c_protection_label":"not_applicable","trigger_outcome_label":"hbm_inspection_quality_test_missed_structural_positive","current_profile_verdict":"current_profile_missed_structural","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C09_L143_168360_HBM_INSPECTION_QUALIFICATION|2024-12-03","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}

{"row_type":"case","case_id":"C09_L143_348210_KROKY_ASPER_ROUTE","symbol":"348210","company_name":"넥스틴","round":"R2","loop":"143","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF","fine_archetype_id":"ADVANCED_INSPECTION_KROKY_ASPER_CUSTOMER_ROUTE","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"Stage2","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"aligned_positive","current_profile_verdict":"current_profile_too_early","price_source":"Songdaiki/stock-web","notes":"kroky_asper_customer_route_positive_but_late_mae"}

{"row_type":"trigger","trigger_id":"T_C09_L143_348210_KROKY_ASPER_ROUTE","case_id":"C09_L143_348210_KROKY_ASPER_ROUTE","symbol":"348210","company_name":"넥스틴","round":"R2","loop":"143","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF","fine_archetype_id":"ADVANCED_INSPECTION_KROKY_ASPER_CUSTOMER_ROUTE","sector":"AI/semiconductor/equipment","primary_archetype":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF","loop_objective":"coverage_gap_fill|counterexample_mining|4B_non_price_requirement_stress_test|canonical_archetype_compression|sector_specific_rule_discovery","trigger_type":"Stage2","trigger_date":"2025-04-22","entry_date":"2025-04-23","entry_price":55700.0,"evidence_available_at_that_date":"published_or_available_on_trigger_date; next-trading-day close if timing unclear","evidence_source":"https://w4.kirs.or.kr/download/research/250422_%EB%84%A5%EC%8A%A4%ED%8B%B4%28%EA%B8%80%EC%84%B8%29_%EC%B5%9C%EC%A2%85.pdf","stage2_evidence_fields":["KROKY advanced memory package inspection","major memory maker supply expectation","ASPER customer diversification"],"stage3_evidence_fields":["new equipment mix expected to rise later"],"stage4b_evidence_fields":["90D high-MAE guard"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/348/348210/2025.csv","profile_path":"atlas/symbol_profiles/348/348210.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":4.67,"MFE_90D_pct":4.67,"MFE_180D_pct":37.52,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-8.08,"MAE_90D_pct":-26.84,"MAE_180D_pct":-26.84,"MAE_1Y_pct":null,"MAE_2Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2025-12-05","peak_price":76600.0,"drawdown_after_peak_pct":-15.67,"green_lateness_ratio":null,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"4B_exit_guard_needed","four_b_evidence_type":["90D high-MAE guard"],"four_c_protection_label":"not_applicable","trigger_outcome_label":"kroky_asper_customer_route_positive_but_late_mae","current_profile_verdict":"current_profile_too_early","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C09_L143_348210_KROKY_ASPER_ROUTE|2025-04-23","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}

{"row_type":"case","case_id":"C09_L143_083310_VACUUM_HBM_DDR5_CONVERSION","symbol":"083310","company_name":"엘오티베큠","round":"R2","loop":"143","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF","fine_archetype_id":"VACUUM_EQUIPMENT_HBM_DDR5_CONVERSION_INVESTMENT_ROUTE","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"Stage2-Actionable","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"aligned_positive","current_profile_verdict":"current_profile_correct","price_source":"Songdaiki/stock-web","notes":"vacuum_equipment_conversion_investment_positive"}

{"row_type":"trigger","trigger_id":"T_C09_L143_083310_VACUUM_HBM_DDR5_CONVERSION","case_id":"C09_L143_083310_VACUUM_HBM_DDR5_CONVERSION","symbol":"083310","company_name":"엘오티베큠","round":"R2","loop":"143","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF","fine_archetype_id":"VACUUM_EQUIPMENT_HBM_DDR5_CONVERSION_INVESTMENT_ROUTE","sector":"AI/semiconductor/equipment","primary_archetype":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF","loop_objective":"coverage_gap_fill|counterexample_mining|4B_non_price_requirement_stress_test|canonical_archetype_compression|sector_specific_rule_discovery","trigger_type":"Stage2-Actionable","trigger_date":"2024-12-10","entry_date":"2024-12-11","entry_price":8200.0,"evidence_available_at_that_date":"published_or_available_on_trigger_date; next-trading-day close if timing unclear","evidence_source":"https://w4.kirs.or.kr/download/research/241210_%EC%97%98%EC%98%A4%ED%8B%B0%EB%B2%A0%ED%81%A0-%EB%9D%BC%EC%9D%B4%EC%A7%95%EC%8A%A4%ED%83%80.pdf","stage2_evidence_fields":["HBM/DDR5 conversion investment","vacuum pump equipment exposure","semiconductor capex recovery"],"stage3_evidence_fields":["revenue conversion visible through equipment demand"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/083/083310/2024.csv","profile_path":"atlas/symbol_profiles/083/083310.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":22.8,"MFE_90D_pct":31.95,"MFE_180D_pct":49.15,"MFE_1Y_pct":89.02,"MFE_2Y_pct":null,"MAE_30D_pct":-4.63,"MAE_90D_pct":-6.71,"MAE_180D_pct":-6.71,"MAE_1Y_pct":-6.71,"MAE_2Y_pct":null,"below_entry_price_flag_30D":false,"below_entry_price_flag_90D":true,"peak_date":"2025-08-29","peak_price":12230.0,"drawdown_after_peak_pct":-6.87,"green_lateness_ratio":null,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_applicable","four_b_evidence_type":[],"four_c_protection_label":"not_applicable","trigger_outcome_label":"vacuum_equipment_conversion_investment_positive","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C09_L143_083310_VACUUM_HBM_DDR5_CONVERSION|2024-12-11","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}

{"row_type":"case","case_id":"C09_L143_053610_LASER_BONDER_HYPE","symbol":"053610","company_name":"프로텍","round":"R2","loop":"143","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF","fine_archetype_id":"LASER_BONDER_AI_HBM_PRODUCTION_TIMING_HYPE","case_type":"residual_false_positive","positive_or_counterexample":"counterexample","best_trigger":"Stage2","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"aligned_counterexample","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"laser_bonder_production_timing_false_positive"}

{"row_type":"trigger","trigger_id":"T_C09_L143_053610_LASER_BONDER_HYPE","case_id":"C09_L143_053610_LASER_BONDER_HYPE","symbol":"053610","company_name":"프로텍","round":"R2","loop":"143","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF","fine_archetype_id":"LASER_BONDER_AI_HBM_PRODUCTION_TIMING_HYPE","sector":"AI/semiconductor/equipment","primary_archetype":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF","loop_objective":"coverage_gap_fill|counterexample_mining|4B_non_price_requirement_stress_test|canonical_archetype_compression|sector_specific_rule_discovery","trigger_type":"Stage2","trigger_date":"2024-08-19","entry_date":"2024-08-20","entry_price":31800.0,"evidence_available_at_that_date":"published_or_available_on_trigger_date; next-trading-day close if timing unclear","evidence_source":"https://stock.pstatic.net/stock-research/company/72/20240819_company_970470000.pdf","stage2_evidence_fields":["AI semiconductor laser bonder development","expected end-2024 production","Samsung/SK Hynix starting customer wording"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["non-price execution risk and legal/accounting overhang"],"stage4c_evidence_fields":["180D thesis drawdown confirmed"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/053/053610/2024.csv","profile_path":"atlas/symbol_profiles/053/053610.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":3.3,"MFE_90D_pct":7.39,"MFE_180D_pct":7.39,"MFE_1Y_pct":7.39,"MFE_2Y_pct":null,"MAE_30D_pct":-27.67,"MAE_90D_pct":-34.75,"MAE_180D_pct":-37.36,"MAE_1Y_pct":-37.36,"MAE_2Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-11-06","peak_price":34150.0,"drawdown_after_peak_pct":-41.67,"green_lateness_ratio":null,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"4B_exit_guard_needed","four_b_evidence_type":["non-price execution risk and legal/accounting overhang"],"four_c_protection_label":"thesis_break_watch_or_hard_4c","trigger_outcome_label":"laser_bonder_production_timing_false_positive","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C09_L143_053610_LASER_BONDER_HYPE|2024-08-20","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}

{"row_type":"case","case_id":"C09_L143_098460_INSPECTION_MIXED_1Q24","symbol":"098460","company_name":"고영","round":"R2","loop":"143","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF","fine_archetype_id":"SEMICONDUCTOR_INSPECTION_MIXED_CORE_DEMAND_MISS","case_type":"residual_false_positive","positive_or_counterexample":"counterexample","best_trigger":"Stage2","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"aligned_counterexample","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"semiconductor_inspection_growth_inside_core_demand_miss_false_positive"}

{"row_type":"trigger","trigger_id":"T_C09_L143_098460_INSPECTION_MIXED_1Q24","case_id":"C09_L143_098460_INSPECTION_MIXED_1Q24","symbol":"098460","company_name":"고영","round":"R2","loop":"143","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF","fine_archetype_id":"SEMICONDUCTOR_INSPECTION_MIXED_CORE_DEMAND_MISS","sector":"AI/semiconductor/equipment","primary_archetype":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF","loop_objective":"coverage_gap_fill|counterexample_mining|4B_non_price_requirement_stress_test|canonical_archetype_compression|sector_specific_rule_discovery","trigger_type":"Stage2","trigger_date":"2024-05-03","entry_date":"2024-05-07","entry_price":15590.0,"evidence_available_at_that_date":"published_or_available_on_trigger_date; next-trading-day close if timing unclear","evidence_source":"https://www.newspim.com/news/view/20240503000144","stage2_evidence_fields":["semiconductor inspection equipment revenue growth","multi-purpose inspection product growth"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["core automotive/server/IoT customer demand weakness"],"stage4c_evidence_fields":["earnings miss and 180D drawdown"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/098/098460/2024.csv","profile_path":"atlas/symbol_profiles/098/098460.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":4.81,"MFE_90D_pct":4.81,"MFE_180D_pct":12.44,"MFE_1Y_pct":42.72,"MFE_2Y_pct":null,"MAE_30D_pct":-22.0,"MAE_90D_pct":-39.58,"MAE_180D_pct":-51.19,"MAE_1Y_pct":-51.19,"MAE_2Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2025-02-03","peak_price":17530.0,"drawdown_after_peak_pct":-9.24,"green_lateness_ratio":null,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"4B_exit_guard_needed","four_b_evidence_type":["core automotive/server/IoT customer demand weakness"],"four_c_protection_label":"thesis_break_watch_or_hard_4c","trigger_outcome_label":"semiconductor_inspection_growth_inside_core_demand_miss_false_positive","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C09_L143_098460_INSPECTION_MIXED_1Q24|2024-05-07","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}

{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C09_L143_039030_LASER_ANNEALING_EARLY","trigger_id":"T_C09_L143_039030_LASER_ANNEALING_EARLY","symbol":"039030","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF","raw_component_scores_before":{"contract_score":4,"backlog_visibility_score":2,"margin_bridge_score":4,"revision_score":2,"relative_strength_score":7,"customer_quality_score":7,"policy_or_regulatory_score":0,"valuation_repricing_score":7,"execution_risk_score":4,"legal_or_contract_risk_score":1,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":78,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"contract_score":5,"backlog_visibility_score":2,"margin_bridge_score":5,"revision_score":2,"relative_strength_score":7,"customer_quality_score":8,"policy_or_regulatory_score":0,"valuation_repricing_score":6,"execution_risk_score":4,"legal_or_contract_risk_score":1,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":82,"stage_label_after":"Stage3-Yellow","changed_components":["qualification_ladder_gate","order_or_revenue_bridge_required","high_mae_guard"],"component_delta_explanation":"C09 shadow gate separates signed/order-backed equipment routes from qualification-only or narrative-only valuation blowoff.","MFE_90D_pct":26.6,"MAE_90D_pct":-20.01,"score_return_alignment_label":"aligned_positive","current_profile_verdict":"current_profile_correct_with_4B_exit_needed"}

{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C09_L143_036930_ALD_MEMORY_CAPA","trigger_id":"T_C09_L143_036930_ALD_MEMORY_CAPA","symbol":"036930","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF","raw_component_scores_before":{"contract_score":3,"backlog_visibility_score":4,"margin_bridge_score":3,"revision_score":4,"relative_strength_score":6,"customer_quality_score":6,"policy_or_regulatory_score":0,"valuation_repricing_score":7,"execution_risk_score":6,"legal_or_contract_risk_score":1,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":74,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"contract_score":4,"backlog_visibility_score":5,"margin_bridge_score":4,"revision_score":4,"relative_strength_score":5,"customer_quality_score":6,"policy_or_regulatory_score":0,"valuation_repricing_score":5,"execution_risk_score":7,"legal_or_contract_risk_score":1,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":76,"stage_label_after":"Stage2-Actionable","changed_components":["qualification_ladder_gate","order_or_revenue_bridge_required","high_mae_guard"],"component_delta_explanation":"C09 shadow gate separates signed/order-backed equipment routes from qualification-only or narrative-only valuation blowoff.","MFE_90D_pct":21.39,"MAE_90D_pct":-21.39,"score_return_alignment_label":"aligned_positive","current_profile_verdict":"current_profile_too_early"}

{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C09_L143_168360_HBM_INSPECTION_QUALIFICATION","trigger_id":"T_C09_L143_168360_HBM_INSPECTION_QUALIFICATION","symbol":"168360","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF","raw_component_scores_before":{"contract_score":5,"backlog_visibility_score":2,"margin_bridge_score":2,"revision_score":2,"relative_strength_score":5,"customer_quality_score":5,"policy_or_regulatory_score":0,"valuation_repricing_score":4,"execution_risk_score":7,"legal_or_contract_risk_score":1,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":66,"stage_label_before":"Stage2-Watch","raw_component_scores_after":{"contract_score":6,"backlog_visibility_score":4,"margin_bridge_score":3,"revision_score":3,"relative_strength_score":7,"customer_quality_score":6,"policy_or_regulatory_score":0,"valuation_repricing_score":5,"execution_risk_score":6,"legal_or_contract_risk_score":1,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":75,"stage_label_after":"Stage2-Actionable","changed_components":["qualification_ladder_gate","order_or_revenue_bridge_required","high_mae_guard"],"component_delta_explanation":"C09 shadow gate separates signed/order-backed equipment routes from qualification-only or narrative-only valuation blowoff.","MFE_90D_pct":126.56,"MAE_90D_pct":-25.31,"score_return_alignment_label":"aligned_positive","current_profile_verdict":"current_profile_missed_structural"}

{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C09_L143_348210_KROKY_ASPER_ROUTE","trigger_id":"T_C09_L143_348210_KROKY_ASPER_ROUTE","symbol":"348210","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF","raw_component_scores_before":{"contract_score":3,"backlog_visibility_score":3,"margin_bridge_score":2,"revision_score":3,"relative_strength_score":5,"customer_quality_score":5,"policy_or_regulatory_score":0,"valuation_repricing_score":6,"execution_risk_score":7,"legal_or_contract_risk_score":1,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":68,"stage_label_before":"Stage2-Watch","raw_component_scores_after":{"contract_score":4,"backlog_visibility_score":4,"margin_bridge_score":3,"revision_score":3,"relative_strength_score":4,"customer_quality_score":6,"policy_or_regulatory_score":0,"valuation_repricing_score":5,"execution_risk_score":8,"legal_or_contract_risk_score":1,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":70,"stage_label_after":"Stage2-Watch","changed_components":["qualification_ladder_gate","order_or_revenue_bridge_required","high_mae_guard"],"component_delta_explanation":"C09 shadow gate separates signed/order-backed equipment routes from qualification-only or narrative-only valuation blowoff.","MFE_90D_pct":4.67,"MAE_90D_pct":-26.84,"score_return_alignment_label":"aligned_positive","current_profile_verdict":"current_profile_too_early"}

{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C09_L143_083310_VACUUM_HBM_DDR5_CONVERSION","trigger_id":"T_C09_L143_083310_VACUUM_HBM_DDR5_CONVERSION","symbol":"083310","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF","raw_component_scores_before":{"contract_score":4,"backlog_visibility_score":3,"margin_bridge_score":4,"revision_score":3,"relative_strength_score":5,"customer_quality_score":5,"policy_or_regulatory_score":0,"valuation_repricing_score":4,"execution_risk_score":4,"legal_or_contract_risk_score":1,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":73,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"contract_score":5,"backlog_visibility_score":4,"margin_bridge_score":5,"revision_score":4,"relative_strength_score":6,"customer_quality_score":5,"policy_or_regulatory_score":0,"valuation_repricing_score":4,"execution_risk_score":3,"legal_or_contract_risk_score":1,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":79,"stage_label_after":"Stage3-Yellow","changed_components":["qualification_ladder_gate","order_or_revenue_bridge_required","high_mae_guard"],"component_delta_explanation":"C09 shadow gate separates signed/order-backed equipment routes from qualification-only or narrative-only valuation blowoff.","MFE_90D_pct":31.95,"MAE_90D_pct":-6.71,"score_return_alignment_label":"aligned_positive","current_profile_verdict":"current_profile_correct"}

{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C09_L143_053610_LASER_BONDER_HYPE","trigger_id":"T_C09_L143_053610_LASER_BONDER_HYPE","symbol":"053610","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF","raw_component_scores_before":{"contract_score":2,"backlog_visibility_score":1,"margin_bridge_score":1,"revision_score":2,"relative_strength_score":6,"customer_quality_score":4,"policy_or_regulatory_score":0,"valuation_repricing_score":6,"execution_risk_score":8,"legal_or_contract_risk_score":6,"dilution_cb_risk_score":0,"accounting_trust_risk_score":4},"weighted_score_before":69,"stage_label_before":"Stage2-Watch","raw_component_scores_after":{"contract_score":1,"backlog_visibility_score":1,"margin_bridge_score":1,"revision_score":1,"relative_strength_score":2,"customer_quality_score":3,"policy_or_regulatory_score":0,"valuation_repricing_score":2,"execution_risk_score":9,"legal_or_contract_risk_score":7,"dilution_cb_risk_score":0,"accounting_trust_risk_score":5},"weighted_score_after":47,"stage_label_after":"Stage4C-Watch","changed_components":["qualification_ladder_gate","order_or_revenue_bridge_required","high_mae_guard"],"component_delta_explanation":"C09 shadow gate separates signed/order-backed equipment routes from qualification-only or narrative-only valuation blowoff.","MFE_90D_pct":7.39,"MAE_90D_pct":-34.75,"score_return_alignment_label":"false_positive_reduced","current_profile_verdict":"current_profile_false_positive"}

{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C09_L143_098460_INSPECTION_MIXED_1Q24","trigger_id":"T_C09_L143_098460_INSPECTION_MIXED_1Q24","symbol":"098460","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF","raw_component_scores_before":{"contract_score":2,"backlog_visibility_score":1,"margin_bridge_score":1,"revision_score":1,"relative_strength_score":5,"customer_quality_score":4,"policy_or_regulatory_score":0,"valuation_repricing_score":5,"execution_risk_score":8,"legal_or_contract_risk_score":1,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":67,"stage_label_before":"Stage2-Watch","raw_component_scores_after":{"contract_score":1,"backlog_visibility_score":1,"margin_bridge_score":1,"revision_score":1,"relative_strength_score":2,"customer_quality_score":3,"policy_or_regulatory_score":0,"valuation_repricing_score":2,"execution_risk_score":9,"legal_or_contract_risk_score":1,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":49,"stage_label_after":"Stage4B-Watch","changed_components":["qualification_ladder_gate","order_or_revenue_bridge_required","high_mae_guard"],"component_delta_explanation":"C09 shadow gate separates signed/order-backed equipment routes from qualification-only or narrative-only valuation blowoff.","MFE_90D_pct":4.81,"MAE_90D_pct":-39.58,"score_return_alignment_label":"false_positive_reduced","current_profile_verdict":"current_profile_false_positive"}

{"row_type":"residual_contribution","round":"R2","loop":"143","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF","new_independent_case_count":7,"reused_case_count":0,"new_symbol_count":7,"new_trigger_family_count":7,"tested_existing_calibrated_axes":["stage2_actionable_evidence_bonus","price_only_blowoff_blocks_positive_stage","full_4b_requires_non_price_evidence","hard_4c_thesis_break_routes_to_4c"],"residual_error_types_found":["qualification_only_false_positive","late_high_MAE_entry","missed_structural_from_quality_test","execution_overhang_4C_watch"],"loop_contribution_label":"canonical_archetype_rule_candidate","do_not_propose_new_weight_delta":false}

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
completed_round = R2
completed_loop = 143
selection_basis = docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket = Priority 0
next_recommended_archetypes = C14_EV_DEMAND_SLOWDOWN_4B_4C|C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE|C06_HBM_MEMORY_CUSTOMER_CAPACITY|C11_BATTERY_ORDERBOOK_RERATING|C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK
round_schedule_status = coverage_index_selected
round_sector_consistency = pass
```

## 28. Source Notes

The evidence sources are recorded as raw URLs in the Evidence Source Map and JSONL rows. The stock-web manifest and symbol profiles are used only for historical calibration path validation.
