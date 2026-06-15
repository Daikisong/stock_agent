# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```yaml
selected_round: R1
selected_loop: 142
selection_basis: docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket: Priority 0 / under 30 rows
round_schedule_status: coverage_index_selected
round_sector_consistency: pass
large_sector_id: L1_INDUSTRIALS_INFRA_DEFENSE_GRID
canonical_archetype_id: C02_POWER_GRID_DATACENTER_CAPEX
fine_archetype_id: mixed_C02_grid_datacenter_switchgear_dr_uc_fourth_pass
loop_objective: coverage_gap_fill | counterexample_mining | C02_theme_vs_order_bridge_validation | 4B_non_price_requirement_stress_test
price_source: Songdaiki/stock-web
stock_web_manifest_max_date: 2026-02-20
output_filename: e2r_stock_web_v12_residual_round_R1_loop_142_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C02_POWER_GRID_DATACENTER_CAPEX_research.md
production_scoring_changed: false
shadow_weight_only: true
handoff_prompt_executed_now: false
```

## 1. Current Calibrated Profile Assumption

- Current proxy profile: `e2r_2_1_stock_web_calibrated`.
- Stage2-Actionable bonus, Stage3-Yellow/Green thresholds, price-only blowoff block, full 4B non-price evidence rule, and hard 4C routing are treated as already applied global rules.
- This MD does not change production scoring. It proposes a C02 shadow rule only.

## 2. Round / Large Sector / Canonical Archetype Scope

| field | value |
|---|---|
| selected_round | `R1` |
| selected_loop | `142` |
| large_sector_id | `L1_INDUSTRIALS_INFRA_DEFENSE_GRID` |
| canonical_archetype_id | `C02_POWER_GRID_DATACENTER_CAPEX` |
| fine_archetype_id | `mixed_C02_grid_datacenter_switchgear_dr_uc_fourth_pass` |
| loop_objective | `coverage_gap_fill | counterexample_mining | C02_theme_vs_order_bridge_validation | 4B_non_price_requirement_stress_test` |

Scope rationale: C02 sits in R1 / L1. This pass focuses on smaller or boundary C02 names where AI datacenter/grid narratives, switchgear, DR/V2G grid-tech, cable exports, and grid-stability ultracapacitor optionality can look like Stage2/3, but only named order, delivery/revenue recognition, and margin bridge should unlock Stage3.

## 3. Previous Coverage / Duplicate Avoidance Check

- Static No-Repeat ledger: C02 has 10 rows and need-to-30 = 20.
- Current session already created C02 loops 139, 140, and 141 with 15 new symbols.
- This loop uses five additional C02 symbols not used in those three session C02 passes.
- Session-adjusted C02 coverage estimate: static 10 + session loops 139/140/141 15 + this loop 5 = 30.

| symbol | company | novelty key | reuse status |
|---|---|---|---|
| 147830 | 제룡산업 | `C02_POWER_GRID_DATACENTER_CAPEX|147830|Stage2-Actionable|2024-05-14` | new_independent_case |
| 189860 | 서전기전 | `C02_POWER_GRID_DATACENTER_CAPEX|189860|Stage2-Actionable|2025-05-16` | new_independent_case |
| 229640 | LS에코에너지 | `C02_POWER_GRID_DATACENTER_CAPEX|229640|Stage4B|2025-02-06` | new_independent_case |
| 453450 | 그리드위즈 | `C02_POWER_GRID_DATACENTER_CAPEX|453450|Stage4B|2024-06-14` | new_independent_case |
| 417200 | LS머트리얼즈 | `C02_POWER_GRID_DATACENTER_CAPEX|417200|Stage4B|2024-04-16` | new_independent_case |

## 4. Stock-Web OHLC Input / Price Source Validation

| field | value |
|---|---|
| source | `Songdaiki/stock-web` |
| upstream_source | `FinanceData/marcap` |
| price_basis | `tradable_raw` |
| price_adjustment_status | `raw_unadjusted_marcap` |
| manifest_max_date | `2026-02-20` |
| calibration_shard_root | `atlas/ohlcv_tradable_by_symbol_year` |
| raw_shard_root | `atlas/ohlcv_raw_by_symbol_year` |

## 5. Historical Eligibility Gate

| symbol | trigger_date | entry_date | entry_price | forward_window_trading_days | window_end | corporate_action_window_status | calibration_usable |
|---|---:|---:|---:|---:|---:|---|---|
| 147830 | 2024-05-13 | 2024-05-14 | 6,900 | 180 | 2025-02-11 | clean_180D_window | true |
| 189860 | 2025-05-15 | 2025-05-16 | 3,975 | 180 | 2026-02-06 | clean_180D_window | true |
| 229640 | 2025-02-05 | 2025-02-06 | 44,750 | 180 | 2025-10-31 | clean_180D_window | true |
| 453450 | 2024-05-24 | 2024-06-14 | 49,500 | 180 | 2025-03-13 | clean_180D_window | true |
| 417200 | 2024-04-15 | 2024-04-16 | 24,200 | 180 | 2025-01-10 | clean_180D_window | true |

## 6. Canonical Archetype Compression Map

| trigger family | compresses to | stage implication |
|---|---|---|
| transmission/distribution materials with no named export order | C02 | Stage2 allowed; Green blocked until customer/order and margin bridge |
| switchgear/panel/datacenter power-distribution narrative | C02 | Stage2 allowed; local 4B if high-MAE or no named project |
| cable export result / AI-grid demand after price run | C02 | late-chase 4B unless new incremental order/backlog appears |
| DR/V2G grid-tech IPO | C02 boundary | IPO/theme 4B; no Stage3 without recurring margin bridge |
| grid-stability UC technology optionality | C02 boundary | product optionality 4B until signed supply/revenue conversion |

## 7. Case Selection Summary

| symbol | company | case_type | trigger_type | trigger_date | entry_date | positive_or_counterexample | current_profile_verdict |
|---|---|---|---|---:|---:|---|---|
| 147830 | 제룡산업 | high_mae_success | Stage2-Actionable | 2024-05-13 | 2024-05-14 | positive | current_profile_4B_too_late |
| 189860 | 서전기전 | boundary_positive_with_watch | Stage2-Actionable | 2025-05-15 | 2025-05-16 | positive | current_profile_4B_too_late |
| 229640 | LS에코에너지 | late_chase_counterexample | Stage4B | 2025-02-05 | 2025-02-06 | counterexample | current_profile_false_positive_or_too_late_4B |
| 453450 | 그리드위즈 | ipo_theme_counterexample | Stage4B | 2024-05-24 | 2024-06-14 | counterexample | current_profile_false_positive |
| 417200 | LS머트리얼즈 | optionality_counterexample | Stage4B | 2024-04-15 | 2024-04-16 | counterexample | current_profile_false_positive |

## 8. Positive vs Counterexample Balance

- positive_case_count: `2`
- counterexample_count: `3`
- 4B_case_count: `5`
- 4C_case_count: `0`

The pass intentionally keeps two Stage2-positive / positive-with-watch cases and three counterexamples. C02 is not failing because the demand story is false; it is failing when the model treats theme, product scope, or already-priced results as if they were fresh named-order margin bridge.

## 9. Evidence Source Map

| symbol | company | trigger_date | evidence source | evidence summary |
|---|---|---:|---|---|
| 147830 | 제룡산업 | 2024-05-13 | https://kind.krx.co.kr/common/disclsviewer.do?acptno=20240513000189&docno=&method=search&viewerhost= | 2024-05-13 KRX quarterly report identified JeRyong Industrial as a producer of transmission/distribution electric-power materials; the business fit is real, but it did not yet prove export/customer margin bridge at Stage3 level. |
| 189860 | 서전기전 | 2025-05-15 | https://kind.krx.co.kr/common/disclsviewer.do?acptNo=20250515002422&docno=&method=searchInitInfo | 2025-05-15 KRX quarterly report disclosed switchgear/power-device development and delivery context; SJElectric also frames its business around switchgear, power devices, rail power, power IT, SCADA and smart grid systems. |
| 229640 | LS에코에너지 | 2025-02-05 | https://v.daum.net/v/00wc7TDxu7 | 2025-02-05 article reported record 2024 revenue/profit, AI datacenter and power-grid expansion demand, high-value cable exports, and US/Europe cable strategy; price path shows this evidence was already vulnerable to late-chase 4B. |
| 453450 | 그리드위즈 | 2024-05-24 | https://www.yna.co.kr/view/AKR20240524092900008 | 2024-05-24 IPO coverage described Gridwiz as Korea DR market leader, DR cash-generation base, V2G/grid-service expansion plan, and 2023 revenue/operating profit; first tradable entry after listing still behaved like a theme/IPO blowoff. |
| 417200 | LS머트리얼즈 | 2024-04-15 | https://www.lscns.co.kr/kr/pr/news_view.asp?brd_id=news1&idx=117607&lang_cd=kr&mode=MOD | 2024-04-15 LS Cable news said LS Materials developed a high-power load-control system using ultracapacitors for grid voltage/frequency stability and was in supply discussions with German/Japanese/US power-equipment makers; no signed delivery or revenue bridge was visible yet. |

## 10. Price Data Source Map

| symbol | price_shard_path | profile_path | price_basis | price_adjustment_status |
|---|---|---|---|---|
| 147830 | `atlas/ohlcv_tradable_by_symbol_year/147/147830/2024.csv|atlas/ohlcv_tradable_by_symbol_year/147/147830/2025.csv` | `atlas/symbol_profiles/147/147830.json` | tradable_raw | raw_unadjusted_marcap |
| 189860 | `atlas/ohlcv_tradable_by_symbol_year/189/189860/2025.csv|atlas/ohlcv_tradable_by_symbol_year/189/189860/2026.csv` | `atlas/symbol_profiles/189/189860.json` | tradable_raw | raw_unadjusted_marcap |
| 229640 | `atlas/ohlcv_tradable_by_symbol_year/229/229640/2025.csv` | `atlas/symbol_profiles/229/229640.json` | tradable_raw | raw_unadjusted_marcap |
| 453450 | `atlas/ohlcv_tradable_by_symbol_year/453/453450/2024.csv|atlas/ohlcv_tradable_by_symbol_year/453/453450/2025.csv` | `atlas/symbol_profiles/453/453450.json` | tradable_raw | raw_unadjusted_marcap |
| 417200 | `atlas/ohlcv_tradable_by_symbol_year/417/417200/2024.csv|atlas/ohlcv_tradable_by_symbol_year/417/417200/2025.csv` | `atlas/symbol_profiles/417/417200.json` | tradable_raw | raw_unadjusted_marcap |

## 11. Case-by-Case Trigger Grid

| symbol | Stage2 evidence | Stage3 evidence | 4B evidence | 4C evidence |
|---|---|---|---|---|
| 147830 | public_event_or_disclosure, capacity_or_volume_route, sector_demand_route, relative_strength | - | price_only_local_peak, valuation_blowoff, margin_bridge_missing | - |
| 189860 | public_event_or_disclosure, capacity_or_volume_route, product_scope_fit | - | margin_bridge_missing, smallcap_liquidity_risk, price_only_local_peak | - |
| 229640 | public_event_or_disclosure, financial_visibility, capacity_or_volume_route, global_grid_demand_route | financial_visibility, margin_bridge | late_chase_after_result, valuation_blowoff, margin_bridge_already_priced | - |
| 453450 | public_event_or_disclosure, capacity_or_volume_route, policy_or_energy_transition_route | - | ipo_blowoff, price_only_local_peak, valuation_blowoff, commercial_margin_bridge_missing | - |
| 417200 | public_event_or_disclosure, technology_route, capacity_or_volume_route | - | supply_discussion_not_signed, revenue_bridge_missing, valuation_blowoff, price_only_local_peak | - |

## 12. Trigger-Level OHLC Backtest Tables

| symbol | entry_price | MFE_30D_pct | MAE_30D_pct | MFE_90D_pct | MAE_90D_pct | MFE_180D_pct | MAE_180D_pct | peak_date | peak_price | drawdown_after_peak_pct |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 147830 | 6,900 | 60.72 | -24.93 | 69.28 | -24.93 | 69.28 | -34.71 | 2024-07-11 | 11,680 | -61.43 |
| 189860 | 3,975 | 27.8 | -1.01 | 27.8 | -23.14 | 30.06 | -29.06 | 2026-01-27 | 5,170 | -26.4 |
| 229640 | 44,750 | 5.03 | -24.47 | 5.03 | -41.68 | 9.39 | -41.68 | 2025-10-30 | 48,950 | -6.54 |
| 453450 | 49,500 | 66.06 | -45.45 | 66.06 | -61.09 | 66.06 | -72.44 | 2024-06-14 | 82,200 | -83.41 |
| 417200 | 24,200 | 30.37 | -2.27 | 32.02 | -41.98 | 32.02 | -60.33 | 2024-06-10 | 31,950 | -69.95 |

## 13. Current Calibrated Profile Stress Test

| symbol | before_score | stage_before | after_score_shadow | stage_after_shadow | price-path alignment |
|---|---:|---|---:|---|---|
| 147830 | 74 | Stage2-Actionable | 70 | Stage2-Actionable + local 4B Watch | mixed_high_mfe_high_mae_stage2_ok_green_block |
| 189860 | 71 | Stage2-Actionable | 68 | Stage2-Actionable + local 4B Watch | mixed_high_mfe_high_mae_stage2_ok_green_block |
| 229640 | 78 | Stage3-Yellow | 60 | Stage4B | misaligned_without_4B_cap |
| 453450 | 72 | Stage2-Actionable | 48 | Stage1/Watch + Stage4B Overlay | misaligned_without_4B_cap |
| 417200 | 70 | Stage2-Actionable | 55 | Stage4B | misaligned_without_4B_cap |

## 14. Stage2 / Yellow / Green Comparison

- Stage2: allowed for public C02 exposure, product scope, DR/V2G, grid-stability technology, and cable export/result evidence.
- Stage3-Yellow: should require named order/customer, delivery or revenue-recognition timing, and visible margin bridge.
- Stage3-Green: should require confirmed revision or durable margin conversion. None of this loop should be promoted to Green at entry.
- Stage4B: should overlay high-MAE, IPO/theme blowoff, product optionality without signed supply, and late-chase after already-reported results.

## 15. 4B Local vs Full-window Timing Audit

| symbol | local peak clue | full-window MAE | 4B timing verdict |
|---|---|---:|---|
| 147830 | peak 2024-07-11 / 11,680 | -34.71 | post_peak_4B_overlay_needed_not_entry_block |
| 189860 | peak 2026-01-27 / 5,170 | -29.06 | post_peak_4B_overlay_needed_not_entry_block |
| 229640 | peak 2025-10-30 / 48,950 | -41.68 | entry_or_fast_local_4B_watch_needed |
| 453450 | peak 2024-06-14 / 82,200 | -72.44 | entry_or_fast_local_4B_watch_needed |
| 417200 | peak 2024-06-10 / 31,950 | -60.33 | entry_or_fast_local_4B_watch_needed |

## 16. 4C Protection Audit

No hard 4C thesis-break row is used in this pass. The residual error is not contract cancellation or accounting-trust break; it is over-promotion of theme/product/result evidence before order-to-margin conversion.

## 17. Sector-Specific Rule Candidate

`L1_C02_GRID_DATACENTER_NAMED_ORDER_DELIVERY_MARGIN_BRIDGE_AND_THEME_BLOWOFF_SPLIT`

L1/C02 should split three buckets: real named order/delivery margin bridge; real product scope but no conversion; and pure theme/IPO/late-chase blowoff. Only the first bucket can open Stage3-Yellow.

## 18. Canonical-Archetype Rule Candidate

`C02_GRID_DATACENTER_CAPEX_REQUIRES_NAMED_ORDER_DELIVERY_REVENUE_AND_MARGIN_BRIDGE_WITH_THEME_4B_CAP_FOURTH_PASS`

Shadow behavior:

```text
if C02 evidence is product scope / IPO / result headline / technology optionality only:
    cap at Stage2-Actionable
if MAE_90D or MAE_180D is severe after a fast local MFE:
    add local 4B watch
if named customer/order + delivery/revenue timing + margin bridge are all visible:
    allow Stage3-Yellow
if confirmed revision and low red-team risk are visible:
    only then consider Stage3-Green
```

## 19. Before / After Backtest Comparison

| symbol | before_stage | after_stage_shadow | MFE_180D_pct | MAE_180D_pct | improvement |
|---|---|---|---:|---:|---|
| 147830 | Stage2-Actionable | Stage2-Actionable + local 4B Watch | 69.28 | -34.71 | keeps Stage2 but blocks Green |
| 189860 | Stage2-Actionable | Stage2-Actionable + local 4B Watch | 30.06 | -29.06 | keeps Stage2 but blocks Green |
| 229640 | Stage3-Yellow | Stage4B | 9.39 | -41.68 | blocks false positive / late-chase promotion |
| 453450 | Stage2-Actionable | Stage1/Watch + Stage4B Overlay | 66.06 | -72.44 | blocks false positive / late-chase promotion |
| 417200 | Stage2-Actionable | Stage4B | 32.02 | -60.33 | blocks false positive / late-chase promotion |

## 20. Score-Return Alignment Matrix

| bucket | symbols | interpretation |
|---|---|---|
| mixed but usable Stage2 | 147830, 189860 | Real C02 exposure and upside, but high-MAE prevents Stage3 unlock |
| counterexample / 4B cap | 229640, 453450, 417200 | Thematic/result/technology optionality did not support risk-adjusted Stage3 |

## 21. Coverage Matrix

| scope | static rows | session prior added | this loop added | session-adjusted rows |
|---|---:|---:|---:|---:|
| C02_POWER_GRID_DATACENTER_CAPEX | 10 | 15 | 5 | 30 |

## 22. Residual Contribution Summary

```yaml
new_independent_case_count: 5
reused_case_count: 0
new_symbol_count: 5
same_archetype_new_symbol_count: 5
same_archetype_new_trigger_family_count: 5
positive_case_count: 2
counterexample_count: 3
current_profile_error_count: 5
diversity_score_summary: "5 new C02 symbols / 5 trigger families / positive 2 + counterexample 3 + 4B watch 5"
loop_contribution_label: canonical_archetype_rule_candidate
do_not_propose_new_weight_delta: false
```

## 23. Validation Scope / Non-Validation Scope

Validated: historical trigger evidence date, next-tradable entry date, stock-web 1D OHLC entry price, 30D/90D/180D MFE·MAE, peak, drawdown, clean 180D corporate-action profile check, and duplicate-avoidance within this session.

Not validated: live stock recommendation, 2026 current valuation, production scoring code, future price after stock-web manifest max_date, broker/API data, or any immediate production patch.

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,C02_named_order_delivery_margin_bridge_gate,canonical,L1_INDUSTRIALS_INFRA_DEFENSE_GRID,C02_POWER_GRID_DATACENTER_CAPEX,0,1,+1,"named order + delivery/revenue + margin bridge required before Stage3","blocks three high-MAE counterexamples while preserving two Stage2 positives","C02_R1L142_147830_C02_TRANSMISSION_DISTRIBUTION_MATERIALS_HIGH_MAE_WATCH_20240513_T1|C02_R1L142_189860_C02_SWITCHGEAR_DATACENTER_DISTRIBUTION_PANEL_BOUNDARY_WATCH_20250515_T1|C02_R1L142_229640_C02_CABLE_EXPORT_RESULT_LATE_CHASE_4B_COUNTEREXAMPLE_20250205_T1|C02_R1L142_453450_C02_GRID_TECH_IPO_DR_V2G_THEME_4B_COUNTEREXAMPLE_20240524_T1|C02_R1L142_417200_C02_GRID_STABILITY_ULTRACAPACITOR_OPTIONALITY_4B_COUNTEREXAMPLE_20240415_T1",5,5,3,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,C02_theme_ipo_product_optionality_4B_cap,canonical,L1_INDUSTRIALS_INFRA_DEFENSE_GRID,C02_POWER_GRID_DATACENTER_CAPEX,0,1,+1,"theme/IPO/product optionality without signed supply should cap promotion","adds local 4B watch to five rows with severe full-window drawdown","C02_R1L142_147830_C02_TRANSMISSION_DISTRIBUTION_MATERIALS_HIGH_MAE_WATCH_20240513_T1|C02_R1L142_189860_C02_SWITCHGEAR_DATACENTER_DISTRIBUTION_PANEL_BOUNDARY_WATCH_20250515_T1|C02_R1L142_229640_C02_CABLE_EXPORT_RESULT_LATE_CHASE_4B_COUNTEREXAMPLE_20250205_T1|C02_R1L142_453450_C02_GRID_TECH_IPO_DR_V2G_THEME_4B_COUNTEREXAMPLE_20240524_T1|C02_R1L142_417200_C02_GRID_STABILITY_ULTRACAPACITOR_OPTIONALITY_4B_COUNTEREXAMPLE_20240415_T1",5,5,3,medium,canonical_shadow_only,"not production; post-calibrated residual"
```

## 25. Machine-Readable Rows

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
{"row_type":"case","case_id":"C02_R1L142_147830_C02_TRANSMISSION_DISTRIBUTION_MATERIALS_HIGH_MAE_WATCH_20240513","symbol":"147830","company_name":"제룡산업","round":"R1","loop":"142","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","fine_archetype_id":"C02_TRANSMISSION_DISTRIBUTION_MATERIALS_HIGH_MAE_WATCH","case_type":"high_mae_success","positive_or_counterexample":"positive","best_trigger":"C02_R1L142_147830_C02_TRANSMISSION_DISTRIBUTION_MATERIALS_HIGH_MAE_WATCH_20240513_T1","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"mixed","current_profile_verdict":"current_profile_4B_too_late","price_source":"Songdaiki/stock-web","notes":"Real C02 exposure produced strong MFE, but the 180D path still carried deep MAE and post-peak drawdown. Stage2 is acceptable; immediate Green is not."}
{"row_type":"trigger","trigger_id":"C02_R1L142_147830_C02_TRANSMISSION_DISTRIBUTION_MATERIALS_HIGH_MAE_WATCH_20240513_T1","case_id":"C02_R1L142_147830_C02_TRANSMISSION_DISTRIBUTION_MATERIALS_HIGH_MAE_WATCH_20240513","symbol":"147830","company_name":"제룡산업","round":"R1","loop":"142","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","fine_archetype_id":"C02_TRANSMISSION_DISTRIBUTION_MATERIALS_HIGH_MAE_WATCH","loop_objective":"coverage_gap_fill | counterexample_mining | C02_theme_vs_order_bridge_validation | 4B_non_price_requirement_stress_test","trigger_type":"Stage2-Actionable","trigger_date":"2024-05-13","entry_date":"2024-05-14","entry_price":6900.0,"evidence_available_at_that_date":"2024-05-13 KRX quarterly report identified JeRyong Industrial as a producer of transmission/distribution electric-power materials; the business fit is real, but it did not yet prove export/customer margin bridge at Stage3 level.","evidence_source":"https://kind.krx.co.kr/common/disclsviewer.do?acptno=20240513000189&docno=&method=search&viewerhost=","stage2_evidence_fields":["public_event_or_disclosure","capacity_or_volume_route","sector_demand_route","relative_strength"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["price_only_local_peak","valuation_blowoff","margin_bridge_missing"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/147/147830/2024.csv|atlas/ohlcv_tradable_by_symbol_year/147/147830/2025.csv","profile_path":"atlas/symbol_profiles/147/147830.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":60.72,"MFE_90D_pct":69.28,"MFE_180D_pct":69.28,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-24.93,"MAE_90D_pct":-24.93,"MAE_180D_pct":-34.71,"MAE_1Y_pct":null,"MAE_2Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"below_entry_price_flag_180D":true,"peak_date":"2024-07-11","peak_price":11680.0,"drawdown_after_peak_pct":-61.43,"green_lateness_ratio":null,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"post_peak_4B_overlay_needed_not_entry_block","four_b_evidence_type":["price_only_local_peak","valuation_blowoff","margin_bridge_missing"],"four_c_protection_label":"not_applicable_no_hard_4c","trigger_outcome_label":"transmission_distribution_materials_high_mfe_high_mae_watch","current_profile_verdict":"current_profile_4B_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C02_POWER_GRID_DATACENTER_CAPEX|147830|2024-05-14|6900.0","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C02_R1L142_147830_C02_TRANSMISSION_DISTRIBUTION_MATERIALS_HIGH_MAE_WATCH_20240513","trigger_id":"C02_R1L142_147830_C02_TRANSMISSION_DISTRIBUTION_MATERIALS_HIGH_MAE_WATCH_20240513_T1","symbol":"147830","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","raw_component_scores_before":{"contract_score":42,"backlog_visibility_score":50,"margin_bridge_score":44,"revision_score":48,"relative_strength_score":88,"customer_quality_score":45,"policy_or_regulatory_score":30,"valuation_repricing_score":80,"execution_risk_score":70,"legal_or_contract_risk_score":5,"dilution_cb_risk_score":0,"accounting_trust_risk_score":5},"weighted_score_before":74,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"contract_score":38,"backlog_visibility_score":48,"margin_bridge_score":38,"revision_score":46,"relative_strength_score":78,"customer_quality_score":42,"policy_or_regulatory_score":30,"valuation_repricing_score":58,"execution_risk_score":80,"legal_or_contract_risk_score":5,"dilution_cb_risk_score":0,"accounting_trust_risk_score":5},"weighted_score_after":70,"stage_label_after":"Stage2-Actionable + local 4B Watch","changed_components":["contract_score","margin_bridge_score","valuation_repricing_score","execution_risk_score"],"component_delta_explanation":"C02 fourth-pass shadow rule rewards named order/delivery/revenue/margin bridge and caps theme, IPO, result-late-chase, or product-optionality rows with local 4B watch.","MFE_90D_pct":69.28,"MAE_90D_pct":-24.93,"score_return_alignment_label":"mixed_high_mfe_high_mae","current_profile_verdict":"current_profile_4B_too_late"}
{"row_type":"case","case_id":"C02_R1L142_189860_C02_SWITCHGEAR_DATACENTER_DISTRIBUTION_PANEL_BOUNDARY_WATCH_20250515","symbol":"189860","company_name":"서전기전","round":"R1","loop":"142","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","fine_archetype_id":"C02_SWITCHGEAR_DATACENTER_DISTRIBUTION_PANEL_BOUNDARY_WATCH","case_type":"boundary_positive_with_watch","positive_or_counterexample":"positive","best_trigger":"C02_R1L142_189860_C02_SWITCHGEAR_DATACENTER_DISTRIBUTION_PANEL_BOUNDARY_WATCH_20250515_T1","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"mixed","current_profile_verdict":"current_profile_4B_too_late","price_source":"Songdaiki/stock-web","notes":"Switchgear/panel exposure is a valid C02 Stage2 bridge, but the path does not justify Stage3 without named project order, delivery timing and margin bridge."}
{"row_type":"trigger","trigger_id":"C02_R1L142_189860_C02_SWITCHGEAR_DATACENTER_DISTRIBUTION_PANEL_BOUNDARY_WATCH_20250515_T1","case_id":"C02_R1L142_189860_C02_SWITCHGEAR_DATACENTER_DISTRIBUTION_PANEL_BOUNDARY_WATCH_20250515","symbol":"189860","company_name":"서전기전","round":"R1","loop":"142","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","fine_archetype_id":"C02_SWITCHGEAR_DATACENTER_DISTRIBUTION_PANEL_BOUNDARY_WATCH","loop_objective":"coverage_gap_fill | counterexample_mining | C02_theme_vs_order_bridge_validation | 4B_non_price_requirement_stress_test","trigger_type":"Stage2-Actionable","trigger_date":"2025-05-15","entry_date":"2025-05-16","entry_price":3975.0,"evidence_available_at_that_date":"2025-05-15 KRX quarterly report disclosed switchgear/power-device development and delivery context; SJElectric also frames its business around switchgear, power devices, rail power, power IT, SCADA and smart grid systems.","evidence_source":"https://kind.krx.co.kr/common/disclsviewer.do?acptNo=20250515002422&docno=&method=searchInitInfo","stage2_evidence_fields":["public_event_or_disclosure","capacity_or_volume_route","product_scope_fit"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["margin_bridge_missing","smallcap_liquidity_risk","price_only_local_peak"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/189/189860/2025.csv|atlas/ohlcv_tradable_by_symbol_year/189/189860/2026.csv","profile_path":"atlas/symbol_profiles/189/189860.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":27.8,"MFE_90D_pct":27.8,"MFE_180D_pct":30.06,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-1.01,"MAE_90D_pct":-23.14,"MAE_180D_pct":-29.06,"MAE_1Y_pct":null,"MAE_2Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"below_entry_price_flag_180D":true,"peak_date":"2026-01-27","peak_price":5170.0,"drawdown_after_peak_pct":-26.4,"green_lateness_ratio":null,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"post_peak_4B_overlay_needed_not_entry_block","four_b_evidence_type":["margin_bridge_missing","smallcap_liquidity_risk","price_only_local_peak"],"four_c_protection_label":"not_applicable_no_hard_4c","trigger_outcome_label":"switchgear_distribution_panel_stage2_positive_with_high_mae_watch","current_profile_verdict":"current_profile_4B_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C02_POWER_GRID_DATACENTER_CAPEX|189860|2025-05-16|3975.0","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C02_R1L142_189860_C02_SWITCHGEAR_DATACENTER_DISTRIBUTION_PANEL_BOUNDARY_WATCH_20250515","trigger_id":"C02_R1L142_189860_C02_SWITCHGEAR_DATACENTER_DISTRIBUTION_PANEL_BOUNDARY_WATCH_20250515_T1","symbol":"189860","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","raw_component_scores_before":{"contract_score":40,"backlog_visibility_score":42,"margin_bridge_score":35,"revision_score":40,"relative_strength_score":70,"customer_quality_score":42,"policy_or_regulatory_score":25,"valuation_repricing_score":62,"execution_risk_score":64,"legal_or_contract_risk_score":5,"dilution_cb_risk_score":0,"accounting_trust_risk_score":5},"weighted_score_before":71,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"contract_score":38,"backlog_visibility_score":40,"margin_bridge_score":32,"revision_score":38,"relative_strength_score":65,"customer_quality_score":40,"policy_or_regulatory_score":25,"valuation_repricing_score":52,"execution_risk_score":75,"legal_or_contract_risk_score":5,"dilution_cb_risk_score":0,"accounting_trust_risk_score":5},"weighted_score_after":68,"stage_label_after":"Stage2-Actionable + local 4B Watch","changed_components":["contract_score","margin_bridge_score","valuation_repricing_score","execution_risk_score"],"component_delta_explanation":"C02 fourth-pass shadow rule rewards named order/delivery/revenue/margin bridge and caps theme, IPO, result-late-chase, or product-optionality rows with local 4B watch.","MFE_90D_pct":27.8,"MAE_90D_pct":-23.14,"score_return_alignment_label":"mixed_high_mfe_high_mae","current_profile_verdict":"current_profile_4B_too_late"}
{"row_type":"case","case_id":"C02_R1L142_229640_C02_CABLE_EXPORT_RESULT_LATE_CHASE_4B_COUNTEREXAMPLE_20250205","symbol":"229640","company_name":"LS에코에너지","round":"R1","loop":"142","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","fine_archetype_id":"C02_CABLE_EXPORT_RESULT_LATE_CHASE_4B_COUNTEREXAMPLE","case_type":"late_chase_counterexample","positive_or_counterexample":"counterexample","best_trigger":"C02_R1L142_229640_C02_CABLE_EXPORT_RESULT_LATE_CHASE_4B_COUNTEREXAMPLE_20250205_T1","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"misaligned_without_4B_cap","current_profile_verdict":"current_profile_false_positive_or_too_late_4B","price_source":"Songdaiki/stock-web","notes":"The fundamental story was real, but post-result entry produced weak upside and large drawdown. The shadow rule should cap post-result chases unless new order backlog or margin bridge appears after the result."}
{"row_type":"trigger","trigger_id":"C02_R1L142_229640_C02_CABLE_EXPORT_RESULT_LATE_CHASE_4B_COUNTEREXAMPLE_20250205_T1","case_id":"C02_R1L142_229640_C02_CABLE_EXPORT_RESULT_LATE_CHASE_4B_COUNTEREXAMPLE_20250205","symbol":"229640","company_name":"LS에코에너지","round":"R1","loop":"142","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","fine_archetype_id":"C02_CABLE_EXPORT_RESULT_LATE_CHASE_4B_COUNTEREXAMPLE","loop_objective":"coverage_gap_fill | counterexample_mining | C02_theme_vs_order_bridge_validation | 4B_non_price_requirement_stress_test","trigger_type":"Stage4B","trigger_date":"2025-02-05","entry_date":"2025-02-06","entry_price":44750.0,"evidence_available_at_that_date":"2025-02-05 article reported record 2024 revenue/profit, AI datacenter and power-grid expansion demand, high-value cable exports, and US/Europe cable strategy; price path shows this evidence was already vulnerable to late-chase 4B.","evidence_source":"https://v.daum.net/v/00wc7TDxu7","stage2_evidence_fields":["public_event_or_disclosure","financial_visibility","capacity_or_volume_route","global_grid_demand_route"],"stage3_evidence_fields":["financial_visibility","margin_bridge"],"stage4b_evidence_fields":["late_chase_after_result","valuation_blowoff","margin_bridge_already_priced"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/229/229640/2025.csv","profile_path":"atlas/symbol_profiles/229/229640.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":5.03,"MFE_90D_pct":5.03,"MFE_180D_pct":9.39,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-24.47,"MAE_90D_pct":-41.68,"MAE_180D_pct":-41.68,"MAE_1Y_pct":null,"MAE_2Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"below_entry_price_flag_180D":true,"peak_date":"2025-10-30","peak_price":48950.0,"drawdown_after_peak_pct":-6.54,"green_lateness_ratio":null,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"entry_or_fast_local_4B_watch_needed","four_b_evidence_type":["late_chase_after_result","valuation_blowoff","margin_bridge_already_priced"],"four_c_protection_label":"not_applicable_no_hard_4c","trigger_outcome_label":"cable_export_ai_grid_result_late_chase_high_mae_counterexample","current_profile_verdict":"current_profile_false_positive_or_too_late_4B","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C02_POWER_GRID_DATACENTER_CAPEX|229640|2025-02-06|44750.0","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C02_R1L142_229640_C02_CABLE_EXPORT_RESULT_LATE_CHASE_4B_COUNTEREXAMPLE_20250205","trigger_id":"C02_R1L142_229640_C02_CABLE_EXPORT_RESULT_LATE_CHASE_4B_COUNTEREXAMPLE_20250205_T1","symbol":"229640","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","raw_component_scores_before":{"contract_score":62,"backlog_visibility_score":55,"margin_bridge_score":76,"revision_score":68,"relative_strength_score":75,"customer_quality_score":70,"policy_or_regulatory_score":35,"valuation_repricing_score":82,"execution_risk_score":58,"legal_or_contract_risk_score":5,"dilution_cb_risk_score":0,"accounting_trust_risk_score":5},"weighted_score_before":78,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":55,"backlog_visibility_score":50,"margin_bridge_score":60,"revision_score":60,"relative_strength_score":55,"customer_quality_score":65,"policy_or_regulatory_score":35,"valuation_repricing_score":45,"execution_risk_score":82,"legal_or_contract_risk_score":5,"dilution_cb_risk_score":0,"accounting_trust_risk_score":5},"weighted_score_after":60,"stage_label_after":"Stage4B","changed_components":["contract_score","margin_bridge_score","valuation_repricing_score","execution_risk_score"],"component_delta_explanation":"C02 fourth-pass shadow rule rewards named order/delivery/revenue/margin bridge and caps theme, IPO, result-late-chase, or product-optionality rows with local 4B watch.","MFE_90D_pct":5.03,"MAE_90D_pct":-41.68,"score_return_alignment_label":"misaligned_high_mae","current_profile_verdict":"current_profile_false_positive_or_too_late_4B"}
{"row_type":"case","case_id":"C02_R1L142_453450_C02_GRID_TECH_IPO_DR_V2G_THEME_4B_COUNTEREXAMPLE_20240524","symbol":"453450","company_name":"그리드위즈","round":"R1","loop":"142","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","fine_archetype_id":"C02_GRID_TECH_IPO_DR_V2G_THEME_4B_COUNTEREXAMPLE","case_type":"ipo_theme_counterexample","positive_or_counterexample":"counterexample","best_trigger":"C02_R1L142_453450_C02_GRID_TECH_IPO_DR_V2G_THEME_4B_COUNTEREXAMPLE_20240524_T1","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"misaligned_without_4B_cap","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"DR/V2G grid-tech exposure is real, but IPO-day pricing and lack of post-listing margin conversion made it a C02 Stage4B counterexample."}
{"row_type":"trigger","trigger_id":"C02_R1L142_453450_C02_GRID_TECH_IPO_DR_V2G_THEME_4B_COUNTEREXAMPLE_20240524_T1","case_id":"C02_R1L142_453450_C02_GRID_TECH_IPO_DR_V2G_THEME_4B_COUNTEREXAMPLE_20240524","symbol":"453450","company_name":"그리드위즈","round":"R1","loop":"142","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","fine_archetype_id":"C02_GRID_TECH_IPO_DR_V2G_THEME_4B_COUNTEREXAMPLE","loop_objective":"coverage_gap_fill | counterexample_mining | C02_theme_vs_order_bridge_validation | 4B_non_price_requirement_stress_test","trigger_type":"Stage4B","trigger_date":"2024-05-24","entry_date":"2024-06-14","entry_price":49500.0,"evidence_available_at_that_date":"2024-05-24 IPO coverage described Gridwiz as Korea DR market leader, DR cash-generation base, V2G/grid-service expansion plan, and 2023 revenue/operating profit; first tradable entry after listing still behaved like a theme/IPO blowoff.","evidence_source":"https://www.yna.co.kr/view/AKR20240524092900008","stage2_evidence_fields":["public_event_or_disclosure","capacity_or_volume_route","policy_or_energy_transition_route"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["ipo_blowoff","price_only_local_peak","valuation_blowoff","commercial_margin_bridge_missing"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/453/453450/2024.csv|atlas/ohlcv_tradable_by_symbol_year/453/453450/2025.csv","profile_path":"atlas/symbol_profiles/453/453450.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":66.06,"MFE_90D_pct":66.06,"MFE_180D_pct":66.06,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-45.45,"MAE_90D_pct":-61.09,"MAE_180D_pct":-72.44,"MAE_1Y_pct":null,"MAE_2Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"below_entry_price_flag_180D":true,"peak_date":"2024-06-14","peak_price":82200.0,"drawdown_after_peak_pct":-83.41,"green_lateness_ratio":null,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"entry_or_fast_local_4B_watch_needed","four_b_evidence_type":["ipo_blowoff","price_only_local_peak","valuation_blowoff","commercial_margin_bridge_missing"],"four_c_protection_label":"not_applicable_no_hard_4c","trigger_outcome_label":"grid_tech_ipo_dr_v2g_theme_high_mae_counterexample","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C02_POWER_GRID_DATACENTER_CAPEX|453450|2024-06-14|49500.0","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C02_R1L142_453450_C02_GRID_TECH_IPO_DR_V2G_THEME_4B_COUNTEREXAMPLE_20240524","trigger_id":"C02_R1L142_453450_C02_GRID_TECH_IPO_DR_V2G_THEME_4B_COUNTEREXAMPLE_20240524_T1","symbol":"453450","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","raw_component_scores_before":{"contract_score":25,"backlog_visibility_score":38,"margin_bridge_score":30,"revision_score":35,"relative_strength_score":92,"customer_quality_score":45,"policy_or_regulatory_score":65,"valuation_repricing_score":90,"execution_risk_score":88,"legal_or_contract_risk_score":5,"dilution_cb_risk_score":0,"accounting_trust_risk_score":5},"weighted_score_before":72,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"contract_score":20,"backlog_visibility_score":30,"margin_bridge_score":20,"revision_score":30,"relative_strength_score":60,"customer_quality_score":38,"policy_or_regulatory_score":55,"valuation_repricing_score":30,"execution_risk_score":95,"legal_or_contract_risk_score":5,"dilution_cb_risk_score":0,"accounting_trust_risk_score":5},"weighted_score_after":48,"stage_label_after":"Stage1/Watch + Stage4B Overlay","changed_components":["contract_score","margin_bridge_score","valuation_repricing_score","execution_risk_score"],"component_delta_explanation":"C02 fourth-pass shadow rule rewards named order/delivery/revenue/margin bridge and caps theme, IPO, result-late-chase, or product-optionality rows with local 4B watch.","MFE_90D_pct":66.06,"MAE_90D_pct":-61.09,"score_return_alignment_label":"misaligned_high_mae","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"case","case_id":"C02_R1L142_417200_C02_GRID_STABILITY_ULTRACAPACITOR_OPTIONALITY_4B_COUNTEREXAMPLE_20240415","symbol":"417200","company_name":"LS머트리얼즈","round":"R1","loop":"142","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","fine_archetype_id":"C02_GRID_STABILITY_ULTRACAPACITOR_OPTIONALITY_4B_COUNTEREXAMPLE","case_type":"optionality_counterexample","positive_or_counterexample":"counterexample","best_trigger":"C02_R1L142_417200_C02_GRID_STABILITY_ULTRACAPACITOR_OPTIONALITY_4B_COUNTEREXAMPLE_20240415_T1","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"misaligned_without_4B_cap","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"Technology relevance was strong, but the trigger was a product/optionality event, not an order-conversion event. The price path supports Stage4B cap."}
{"row_type":"trigger","trigger_id":"C02_R1L142_417200_C02_GRID_STABILITY_ULTRACAPACITOR_OPTIONALITY_4B_COUNTEREXAMPLE_20240415_T1","case_id":"C02_R1L142_417200_C02_GRID_STABILITY_ULTRACAPACITOR_OPTIONALITY_4B_COUNTEREXAMPLE_20240415","symbol":"417200","company_name":"LS머트리얼즈","round":"R1","loop":"142","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","fine_archetype_id":"C02_GRID_STABILITY_ULTRACAPACITOR_OPTIONALITY_4B_COUNTEREXAMPLE","loop_objective":"coverage_gap_fill | counterexample_mining | C02_theme_vs_order_bridge_validation | 4B_non_price_requirement_stress_test","trigger_type":"Stage4B","trigger_date":"2024-04-15","entry_date":"2024-04-16","entry_price":24200.0,"evidence_available_at_that_date":"2024-04-15 LS Cable news said LS Materials developed a high-power load-control system using ultracapacitors for grid voltage/frequency stability and was in supply discussions with German/Japanese/US power-equipment makers; no signed delivery or revenue bridge was visible yet.","evidence_source":"https://www.lscns.co.kr/kr/pr/news_view.asp?brd_id=news1&idx=117607&lang_cd=kr&mode=MOD","stage2_evidence_fields":["public_event_or_disclosure","technology_route","capacity_or_volume_route"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["supply_discussion_not_signed","revenue_bridge_missing","valuation_blowoff","price_only_local_peak"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/417/417200/2024.csv|atlas/ohlcv_tradable_by_symbol_year/417/417200/2025.csv","profile_path":"atlas/symbol_profiles/417/417200.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":30.37,"MFE_90D_pct":32.02,"MFE_180D_pct":32.02,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-2.27,"MAE_90D_pct":-41.98,"MAE_180D_pct":-60.33,"MAE_1Y_pct":null,"MAE_2Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"below_entry_price_flag_180D":true,"peak_date":"2024-06-10","peak_price":31950.0,"drawdown_after_peak_pct":-69.95,"green_lateness_ratio":null,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"entry_or_fast_local_4B_watch_needed","four_b_evidence_type":["supply_discussion_not_signed","revenue_bridge_missing","valuation_blowoff","price_only_local_peak"],"four_c_protection_label":"not_applicable_no_hard_4c","trigger_outcome_label":"uc_grid_stability_optional_revenue_delay_high_mae_counterexample","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C02_POWER_GRID_DATACENTER_CAPEX|417200|2024-04-16|24200.0","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C02_R1L142_417200_C02_GRID_STABILITY_ULTRACAPACITOR_OPTIONALITY_4B_COUNTEREXAMPLE_20240415","trigger_id":"C02_R1L142_417200_C02_GRID_STABILITY_ULTRACAPACITOR_OPTIONALITY_4B_COUNTEREXAMPLE_20240415_T1","symbol":"417200","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","raw_component_scores_before":{"contract_score":25,"backlog_visibility_score":35,"margin_bridge_score":28,"revision_score":35,"relative_strength_score":78,"customer_quality_score":50,"policy_or_regulatory_score":45,"valuation_repricing_score":80,"execution_risk_score":75,"legal_or_contract_risk_score":5,"dilution_cb_risk_score":0,"accounting_trust_risk_score":5},"weighted_score_before":70,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"contract_score":22,"backlog_visibility_score":30,"margin_bridge_score":20,"revision_score":30,"relative_strength_score":60,"customer_quality_score":45,"policy_or_regulatory_score":45,"valuation_repricing_score":36,"execution_risk_score":90,"legal_or_contract_risk_score":5,"dilution_cb_risk_score":0,"accounting_trust_risk_score":5},"weighted_score_after":55,"stage_label_after":"Stage4B","changed_components":["contract_score","margin_bridge_score","valuation_repricing_score","execution_risk_score"],"component_delta_explanation":"C02 fourth-pass shadow rule rewards named order/delivery/revenue/margin bridge and caps theme, IPO, result-late-chase, or product-optionality rows with local 4B watch.","MFE_90D_pct":32.02,"MAE_90D_pct":-41.98,"score_return_alignment_label":"misaligned_high_mae","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"residual_contribution","round":"R1","loop":"142","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","new_independent_case_count":5,"reused_case_count":0,"new_symbol_count":5,"same_archetype_new_symbol_count":5,"same_archetype_new_trigger_family_count":5,"new_trigger_family_count":5,"positive_case_count":2,"counterexample_count":3,"current_profile_error_count":5,"tested_existing_calibrated_axes":["stage2_required_bridge","price_only_blowoff_blocks_positive_stage","full_4b_requires_non_price_evidence","local_4b_watch_guard"],"residual_error_types_found":["theme_or_product_scope_overpromotion","late_chase_after_result","IPO_grid_tech_blowoff","UC_technology_optionality_without_signed_supply","switchgear_stage2_ok_green_block_needed"],"loop_contribution_label":"canonical_archetype_rule_candidate","do_not_propose_new_weight_delta":false}
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
completed_round = R1
completed_loop = 142
selection_basis = docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket = Priority 0 / under 30 rows
round_schedule_status = coverage_index_selected
round_sector_consistency = pass
next_recommended_archetypes = C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF | C14_EV_DEMAND_SLOWDOWN_4B_4C | C06_HBM_MEMORY_CUSTOMER_CAPACITY
```

## 28. Source Notes

- Main execution prompt: https://raw.githubusercontent.com/Songdaiki/stock_agent/main/docs/core/e2r_v12_prompt_round_scheduler_corrected.txt
- No-repeat ledger: https://raw.githubusercontent.com/Songdaiki/stock_agent/main/docs/core/V12_Research_No_Repeat_Index.md
- Stock-web manifest: https://raw.githubusercontent.com/Songdaiki/stock-web/main/atlas/manifest.json
- Stock-web schema: https://raw.githubusercontent.com/Songdaiki/stock-web/main/atlas/schema.json
- Evidence source URLs are listed per trigger in section 9 and in every JSONL trigger row.
