# E2R Stock-Web v12 Residual Research — R1 / L1_INDUSTRIALS_INFRA_DEFENSE_GRID / C02_POWER_GRID_DATACENTER_CAPEX

```yaml
output_file: e2r_stock_web_v12_residual_round_R1_loop_118_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C02_POWER_GRID_DATACENTER_CAPEX_research.md
round: R1
selected_loop: 118
large_sector_id: L1_INDUSTRIALS_INFRA_DEFENSE_GRID
canonical_archetype_id: C02_POWER_GRID_DATACENTER_CAPEX
fine_archetype_family: GRID_TRANSFORMER_DATACENTER_CAPEX_CONFIRMED_BRIDGE_VS_PROXY_THEME
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
price_source: Songdaiki/stock-web
price_basis: tradable_raw
price_adjustment_status: raw_unadjusted_marcap
stock_web_manifest_min_date: 1995-05-02
stock_web_manifest_max_date: 2026-02-20
production_scoring_changed: false
shadow_only: true
investment_recommendation: false
```

## 0. Execution scope

This run follows the MAIN EXECUTION PROMPT and uses the NO-REPEAT INDEX only as a duplicate-avoidance and coverage-ledger artifact.  
The selected bucket is **Priority 0** because `C02_POWER_GRID_DATACENTER_CAPEX` is under-covered in the index: 10 representative rows, 10 symbols, 0/0 positive/counterexample split, and 0/0 4B/4C paths before this loop.

The research unit is not a live stock recommendation. It is a historical calibration record for `E2R 2.2` style archetype scoring. No production score file is changed here.

The loop label `118` is used as this execution's continuation label. If the local `docs/round` registry already contains a later R1/C02 loop, rename the filename and matching metadata only; the strict no-repeat keys are symbol/trigger/date based and should remain unchanged.

## 1. Round / canonical / fine-deep compression

- Derived round: `R1`
- Derived large sector: `L1_INDUSTRIALS_INFRA_DEFENSE_GRID`
- Canonical target: `C02_POWER_GRID_DATACENTER_CAPEX`
- Fine/deep stress axis: **confirmed transformer/grid order-backlog-CAPA-margin bridge versus product-category/proxy-theme beta**

C02 is treated as a power-grid/data-center CAPEX archetype. The key mechanism is not “AI data-center keyword appears near a power-equipment stock.” The key mechanism is: **demand shock → order/backlog or customer lock → capacity/lead-time scarcity → ASP or margin bridge → revenue/FCF realization.**  
When the chain breaks at the product-keyword or copper/theme layer, the case is a Watch or local 4B guardrail, not a Stage2-Actionable or Stage3-Yellow positive.

## 2. No-repeat and coverage check

Existing top-covered C02 symbols in the index snapshot include `000500`, `001440`, `006260`, `010120`, `017510`, and `024840`. This run avoids those and adds five independent symbols:

```text
267260 HD현대일렉트릭
033100 제룡전기
298040 효성중공업
237750 피앤씨테크
006340 대원전선
```

Strict duplicate key format used here:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

Estimated coverage impact if accepted:

```text
C02 representative rows: 10 -> 15
need_to_30_after_acceptance: 15
need_to_50_after_acceptance: 35
new_independent_case_count: 5
new_symbol_count: 5
positive_case_count: 3
counterexample_count: 2
4B_overlay_guardrail_count: 1
```

## 3. Stock-web validation

All price paths use stock-web tradable shards. The price basis is raw close/high/low from `tradable_raw`, not adjusted close.  
The MFE/MAE formula is:

```text
MFE_ND_pct = (max(high over entry_date through N trading days) / entry_price - 1) * 100
MAE_ND_pct = (min(low over entry_date through N trading days) / entry_price - 1) * 100
```

All selected primary rows have a complete 180-trading-day forward window before stock-web manifest max date `2026-02-20`. Corporate-action contamination was checked using the available symbol-profile summaries: 2024/2025 windows are clean for the five symbols used in the primary grid.

## 4. Case summary and price path grid

| Symbol | Company | Trigger | Entry | Type | MFE30 | MFE90 | MFE180 | MAE30 | MAE90 | MAE180 | Outcome |
|---|---:|---|---|---|---:|---:|---:|---:|---:|---:|---|
| 267260 | HD현대일렉트릭 | 2024-04-23 / Stage3-Yellow | 2024-04-24 @ 255,000 | positive | 23.14 | 46.86 | 71.18 | -10.20 | -10.20 | -11.57 | positive_structural_rerating_with_backlog_margin_bridge |
| 033100 | 제룡전기 | 2024-03-08 / Stage2-Actionable | 2024-03-11 @ 31,200 | positive | 81.09 | 222.76 | 222.76 | -3.04 | -3.04 | -3.04 | positive_high_mfe_but_requires_late_4B_peak_guard |
| 298040 | 효성중공업 | 2025-01-15 / Stage3-Yellow | 2025-01-16 @ 469,000 | positive | 17.06 | 41.79 | 258.85 | -10.23 | -18.55 | -18.55 | positive_structural_rerating_after_capa_order_bridge |
| 237750 | 피앤씨테크 | 2024-04-29 / Stage2 | 2024-04-29 @ 6,550 | counterexample | 16.64 | 16.64 | 16.64 | -12.98 | -32.21 | -49.92 | counterexample_source_proxy_theme_low_mfe_deep_mae |
| 006340 | 대원전선 | 2024-06-12 / Stage2 | 2024-06-13 @ 3,635 | counterexample | 31.36 | 31.36 | 31.36 | -8.25 | -29.85 | -39.34 | counterexample_cable_copper_proxy_high_early_mfe_deep_mae |
| 237750 | 피앤씨테크 | 2024-05-08 / Stage4B overlay | 2024-05-08 @ 6,990 | counterexample / overlay | 9.30 | 9.30 | 9.30 | -18.45 | -37.12 | -53.08 | price_only_local_4B_guardrail_only |

## 5. Case-level interpretation

### 5.1 Positive controls

**267260 / HD현대일렉트릭**  
This is the cleanest positive control. By the trigger date, the record contains actual order and backlog expansion, explicit demand commentary, and a margin realization bridge through selective ordering and higher selling prices. The path shows large 180D upside despite early drawdown, which argues for Stage3-Yellow credit when the bridge is hard, not merely thematic.

**033100 / 제룡전기**  
This is a small pure-play transformer exporter case. The March 2024 evidence already contained pure transformer exposure, export mix expansion, backlog above the 3,000억원 neighborhood, U.S. shortage, data-center/grid demand, and price/cost spread logic. The 180D MFE is very high, but the post-peak drawdown is severe. C02 should allow earlier Stage2-Actionable/Yellow credit for pure-play exporter structures, while still demanding late 4B discipline after the move.

**298040 / 효성중공업**  
This is a mixed-segment heavy transformer case. The January 2025 trigger contains heavy-industry order strength, guidance support, and high-voltage transformer CAPA expansion. The residual is that a broad construction/PF discount can make the current profile too slow if it blocks the power-equipment bridge at the consolidated-company layer. The proposed rule is to separate segment-specific C02 evidence from non-C02 segment discount.

### 5.2 Counterexamples

**237750 / 피앤씨테크**  
The source names a relevant product category and export regions under the AI/data-center power-demand umbrella, but it lacks signed order, backlog, named customer, CAPA slot, ASP, or margin bridge. The price path gives only a short-lived MFE and then a deep 180D MAE. It is a clean example of product-category proximity that should remain Watch or local 4B, not Stage2-Actionable.

**006340 / 대원전선**  
This case has a cable/copper/AI-power-demand story. It produced a strong early MFE but collapsed into a deep forward MAE. The bridge is weaker than transformer-specific C02 because copper pass-through and cable beta do not by themselves prove data-center or grid CAPEX customer lock. It should be handled as proxy beta unless company-specific order/backlog/margin evidence appears.

### 5.3 4B overlay

The 237750 local peak on 2024-05-08 is a useful **price-only local 4B guardrail**. It is not a full 4B because no non-price deterioration evidence was added by that date. The overlay exists to test the current rule that full 4B requires non-price evidence; the rule should be preserved.

## 6. Profile stress test

| Profile | Description | Expected C02 behavior |
|---|---|---|
| P0 current | `e2r_2_2_rolling_calibrated` style baseline | Should already block pure price/proxy theme and require a bridge. May still be too late for pure transformer exporter or mixed-segment heavy transformer. |
| P0b stricter current | Baseline plus stricter source-proxy rejection | Blocks 237750 and 006340 cleanly; risk is missing smaller pure-play exporters. |
| P1 weaker proxy-credit | Credits product/category/news theme too easily | Generates false positives in 237750 and 006340. |
| P2 C02 bridge profile | Credits confirmed order/backlog/CAPA/margin bridge and penalizes proxy theme | Best fit for this loop. |
| P3 late-4B overlay | Adds price-only 4B local watch but blocks full 4B without non-price evidence | Useful for 237750/006340 after local blowoff. |

## 7. Shadow rule candidate

```text
C02_CONFIRMED_ORDER_BACKLOG_CAPA_MARGIN_BRIDGE_VS_PROXY_THEME
```

Candidate behavior:

1. Add C02 credit when at least two hard bridge fields exist:
   - confirmed order / backlog growth
   - customer or geography lock
   - CAPA / lead-time scarcity / production slot
   - ASP / margin realization
   - revenue or EPS revision visibility

2. Subtract or block Stage2-Actionable when the evidence is only:
   - AI/data-center keyword
   - product-category relevance
   - copper/cable beta
   - one-day relative strength
   - source-proxy article without company-specific conversion bridge

3. Keep 4B conservative:
   - price-only local peak can create local 4B watch
   - full 4B requires non-price evidence such as order cancellation, margin break, customer loss, guide-down, accounting/trust issue, or thesis break

Confidence: **medium-low** because this is a single-loop candidate. Apply only through shadow calibration and later aggregate promotion logic, not directly to production.

## 8. Machine-readable rows

```jsonl
{"row_type":"price_source_validation","schema_family":"v12_sector_archetype_residual","round":"R1","loop":"118","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","manifest_generated_at":"2026-05-21T06:12:04Z","stock_web_manifest_min_date":"1995-05-02","stock_web_manifest_max_date":"2026-02-20","tradable_row_count":14354401,"raw_row_count":15214118,"symbol_count":5414,"forward_window_policy":"entry_date_through_180_trading_days_required","corporate_action_window_policy":"non-contaminated 180D window required","symbols_checked":["267260","033100","298040","237750","006340"],"source_file":"docs/round/e2r_stock_web_v12_residual_round_R1_loop_118_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C02_POWER_GRID_DATACENTER_CAPEX_research.md"}
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","trigger_id":"R1L118_C02_267260_20240424_STAGE3_YELLOW","case_id":"C02_R1L118_267260_GRID_TRANSFORMER_BACKLOG_PRICE_REALIZATION_CONFIRMED_20240424","round":"R1","loop":"118","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","fine_archetype_id":"GRID_TRANSFORMER_BACKLOG_PRICE_REALIZATION_CONFIRMED","symbol":"267260","company_name":"HD현대일렉트릭","trigger_type":"Stage3-Yellow","trigger_date":"2024-04-23","entry_date":"2024-04-24","entry_price":255000.0,"entry_price_basis":"close","price_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/267/267260/2024.csv + 2025.csv","profile_path":"atlas/symbol_profiles/267/267260.json","stock_web_manifest_max_date":"2026-02-20","forward_window_trading_days":180,"MFE_30D_pct":23.14,"MFE_90D_pct":46.86,"MFE_180D_pct":71.18,"MAE_30D_pct":-10.2,"MAE_90D_pct":-10.2,"MAE_180D_pct":-11.57,"peak_date":"2025-01-20","peak_price":436500.0,"max_drawdown_low":382000.0,"max_drawdown_low_date":"2025-01-20","drawdown_after_peak_pct":-12.49,"below_entry_price_flag_30d":true,"below_entry_price_flag_90d":true,"positive_or_counterexample":"positive","case_type":"structural_success","trigger_outcome_label":"positive_structural_rerating_with_backlog_margin_bridge","current_profile_verdict":"current_profile_correct_if_order_backlog_margin_bridge_is_creditable","current_profile_error":false,"current_profile_false_positive":false,"current_profile_too_late":false,"current_profile_missed_structural":false,"current_profile_4B_too_early":false,"current_profile_4C_too_late":false,"calibration_usable":true,"calibration_block_reasons":[],"usable_for_v12_shadow_calibration":true,"usable_for_archetype_shadow":true,"usable_for_sector_shadow":true,"usable_for_global_promotion":false,"usable_for_new_weight_evidence":true,"usable_for_weight_calibration":false,"guardrail_usable":false,"is_new_independent_case":true,"do_not_count_as_new_case":false,"is_aggregate_representative":true,"aggregate_group_role":"representative","dedupe_for_aggregate":true,"dedupe_key":"v12_strict|267260|C02_POWER_GRID_DATACENTER_CAPEX|Stage3-Yellow|2024-04-24|2024-04-24|255000.0|GRID_TRANSFORMER_BACKLOG_PRICE_REALIZATION_CONFIRMED","same_entry_group_id":"C02_POWER_GRID_DATACENTER_CAPEX_267260_2024-04-24_255000","dedupe_member_count":1,"source_proxy_only":false,"evidence_available_at_that_date":"1Q24 earnings: revenue/OP jump, OPM from selective-ordering price realization, orders/backlog expansion, explicit electrification/digital-transition demand.","evidence_source":"HD Hyundai / Newswire 2024-04-23; Herald/Daum same-day coverage","evidence_url":"https://www.newswire.co.kr/newsRead.php?no=988377","evidence_url_pending":false,"independent_evidence_weight":2.0,"stage2_evidence_fields":["confirmed_orders","backlog_growth","power_grid_demand","selective_order_strategy"],"stage3_evidence_fields":["margin_realization","revenue_conversion","order_backlog_visibility","non_price_evidence"],"stage4b_evidence_fields":["not_applicable"],"stage4c_evidence_fields":["not_applicable"],"four_b_evidence_type":["not_applicable"],"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_applicable_for_primary_entry","four_c_protection_label":"not_applicable","green_lateness_ratio":"not_measured","corporate_action_window_status":"clean_180D_window; profile corporate-action candidates are historical 2017-2019 only","price_path_valid":true,"validation_reasons":[],"residual_counterexample":false,"loop_objective":"coverage_gap_fill|counterexample_mining|sector_specific_rule_discovery|stage2_actionable_bonus_stress_test|4B_non_price_requirement_stress_test","source_file":"docs/round/e2r_stock_web_v12_residual_round_R1_loop_118_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C02_POWER_GRID_DATACENTER_CAPEX_research.md"}
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","trigger_id":"R1L118_C02_033100_20240311_STAGE2_ACTIONABLE","case_id":"C02_R1L118_033100_SMALL_TRANSFORMER_US_EXPORT_BACKLOG_CAPACITY_LOCK_20240311","round":"R1","loop":"118","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","fine_archetype_id":"SMALL_TRANSFORMER_US_EXPORT_BACKLOG_CAPACITY_LOCK","symbol":"033100","company_name":"제룡전기","trigger_type":"Stage2-Actionable","trigger_date":"2024-03-08","entry_date":"2024-03-11","entry_price":31200.0,"entry_price_basis":"close","price_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/033/033100/2024.csv","profile_path":"atlas/symbol_profiles/033/033100.json","stock_web_manifest_max_date":"2026-02-20","forward_window_trading_days":180,"MFE_30D_pct":81.09,"MFE_90D_pct":222.76,"MFE_180D_pct":222.76,"MAE_30D_pct":-3.04,"MAE_90D_pct":-3.04,"MAE_180D_pct":-3.04,"peak_date":"2024-07-11","peak_price":100700.0,"max_drawdown_low":39200.0,"max_drawdown_low_date":"2024-12-02","drawdown_after_peak_pct":-61.07,"below_entry_price_flag_30d":true,"below_entry_price_flag_90d":true,"positive_or_counterexample":"positive","case_type":"structural_success_with_late_4B_risk","trigger_outcome_label":"positive_high_mfe_but_requires_late_4B_peak_guard","current_profile_verdict":"current_profile_too_late_for_small_pure_transformer_exporter_if_large_customer_contract_required","current_profile_error":true,"current_profile_false_positive":false,"current_profile_too_late":true,"current_profile_missed_structural":true,"current_profile_4B_too_early":false,"current_profile_4C_too_late":false,"calibration_usable":true,"calibration_block_reasons":[],"usable_for_v12_shadow_calibration":true,"usable_for_archetype_shadow":true,"usable_for_sector_shadow":true,"usable_for_global_promotion":false,"usable_for_new_weight_evidence":true,"usable_for_weight_calibration":false,"guardrail_usable":false,"is_new_independent_case":true,"do_not_count_as_new_case":false,"is_aggregate_representative":true,"aggregate_group_role":"representative","dedupe_for_aggregate":true,"dedupe_key":"v12_strict|033100|C02_POWER_GRID_DATACENTER_CAPEX|Stage2-Actionable|2024-03-11|2024-03-11|31200.0|SMALL_TRANSFORMER_US_EXPORT_BACKLOG_CAPACITY_LOCK","same_entry_group_id":"C02_POWER_GRID_DATACENTER_CAPEX_033100_2024-03-11_31200","dedupe_member_count":1,"source_proxy_only":false,"evidence_available_at_that_date":"Distributor-scale transformer pure play: export mix surged, backlog above 3,000억원, U.S. transformer shortage, data-center and grid replacement demand, price/cost spread and production-efficiency bridge.","evidence_source":"Yuanta company report 2024-03-08; AsiaEconomy 2024-03-08; BigDataNews/NH follow-up 2024-05-29","evidence_url":"https://ssl.pstatic.net/imgstock/upload/research/company/1709852777300.pdf","evidence_url_pending":false,"independent_evidence_weight":2.0,"stage2_evidence_fields":["pure_transformer_exposure","export_mix_growth","backlog_above_3000억","us_transformer_shortage"],"stage3_evidence_fields":["margin_spread","production_efficiency","revenue_growth","asof_report_evidence"],"stage4b_evidence_fields":["late_peak_drawdown_after_success_watch"],"stage4c_evidence_fields":["not_applicable_at_entry"],"four_b_evidence_type":["late_peak_drawdown_after_success_watch"],"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_applicable_for_primary_entry","four_c_protection_label":"not_applicable","green_lateness_ratio":"not_measured","corporate_action_window_status":"clean_180D_window; profile corporate-action candidates ended 2014-11-06","price_path_valid":true,"validation_reasons":[],"residual_counterexample":false,"loop_objective":"coverage_gap_fill|counterexample_mining|sector_specific_rule_discovery|stage2_actionable_bonus_stress_test|4B_non_price_requirement_stress_test","source_file":"docs/round/e2r_stock_web_v12_residual_round_R1_loop_118_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C02_POWER_GRID_DATACENTER_CAPEX_research.md"}
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","trigger_id":"R1L118_C02_298040_20250116_STAGE3_YELLOW","case_id":"C02_R1L118_298040_HEAVY_TRANSFORMER_CHAWON_MEMPHIS_CAPA_ORDER_GUIDANCE_20250116","round":"R1","loop":"118","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","fine_archetype_id":"HEAVY_TRANSFORMER_CHAWON_MEMPHIS_CAPA_ORDER_GUIDANCE","symbol":"298040","company_name":"효성중공업","trigger_type":"Stage3-Yellow","trigger_date":"2025-01-15","entry_date":"2025-01-16","entry_price":469000.0,"entry_price_basis":"close","price_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/298/298040/2025.csv","profile_path":"atlas/symbol_profiles/298/298040.json","stock_web_manifest_max_date":"2026-02-20","forward_window_trading_days":180,"MFE_30D_pct":17.06,"MFE_90D_pct":41.79,"MFE_180D_pct":258.85,"MAE_30D_pct":-10.23,"MAE_90D_pct":-18.55,"MAE_180D_pct":-18.55,"peak_date":"2025-10-16","peak_price":1683000.0,"max_drawdown_low":1577000.0,"max_drawdown_low_date":"2025-10-16","drawdown_after_peak_pct":-6.3,"below_entry_price_flag_30d":true,"below_entry_price_flag_90d":true,"positive_or_counterexample":"positive","case_type":"structural_success","trigger_outcome_label":"positive_structural_rerating_after_capa_order_bridge","current_profile_verdict":"current_profile_too_late_if_construction_discount_overrides_power_equipment_capa_bridge","current_profile_error":true,"current_profile_false_positive":false,"current_profile_too_late":true,"current_profile_missed_structural":true,"current_profile_4B_too_early":false,"current_profile_4C_too_late":false,"calibration_usable":true,"calibration_block_reasons":[],"usable_for_v12_shadow_calibration":true,"usable_for_archetype_shadow":true,"usable_for_sector_shadow":true,"usable_for_global_promotion":false,"usable_for_new_weight_evidence":true,"usable_for_weight_calibration":false,"guardrail_usable":false,"is_new_independent_case":true,"do_not_count_as_new_case":false,"is_aggregate_representative":true,"aggregate_group_role":"representative","dedupe_for_aggregate":true,"dedupe_key":"v12_strict|298040|C02_POWER_GRID_DATACENTER_CAPEX|Stage3-Yellow|2025-01-16|2025-01-16|469000.0|HEAVY_TRANSFORMER_CHAWON_MEMPHIS_CAPA_ORDER_GUIDANCE","same_entry_group_id":"C02_POWER_GRID_DATACENTER_CAPEX_298040_2025-01-16_469000","dedupe_member_count":1,"source_proxy_only":false,"evidence_available_at_that_date":"4Q24 preview: heavy-industry segment strength, 1Q24-3Q24 order growth, aggressive order guidance, high-voltage transformer CAPA expansion at Changwon/Memphis, construction risk partially ring-fenced.","evidence_source":"LS Securities company report 2025-01-15","evidence_url":"https://file.alphasquare.co.kr/media/pdfs/company-report/_%ED%9A%A8%EC%84%B1%EC%A4%91%EA%B3%B5%EC%97%85_4Q24%20Preview_250115%E2%98%86_%EC%84%B1%EC%A2%85%ED%99%94_1899_Online%20report%20_%206_10p_%ED%9A%A8%EC%84%B1%EC%A4%91%EA%B3%B5%EC%97%85.pdf","evidence_url_pending":false,"independent_evidence_weight":2.0,"stage2_evidence_fields":["heavy_industry_order_growth","power_equipment_upcycle","order_guidance"],"stage3_evidence_fields":["capa_expansion","margin_outlook","segment_separation","backlog_visibility"],"stage4b_evidence_fields":["not_applicable"],"stage4c_evidence_fields":["construction_risk_needs_separate_discount_not_canonical_block"],"four_b_evidence_type":["not_applicable"],"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_applicable_for_primary_entry","four_c_protection_label":"not_applicable","green_lateness_ratio":"not_measured","corporate_action_window_status":"clean_180D_window; profile corporate_action_candidate_count=0","price_path_valid":true,"validation_reasons":[],"residual_counterexample":false,"loop_objective":"coverage_gap_fill|counterexample_mining|sector_specific_rule_discovery|stage2_actionable_bonus_stress_test|4B_non_price_requirement_stress_test","source_file":"docs/round/e2r_stock_web_v12_residual_round_R1_loop_118_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C02_POWER_GRID_DATACENTER_CAPEX_research.md"}
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","trigger_id":"R1L118_C02_237750_20240429_STAGE2","case_id":"C02_R1L118_237750_PROTECTION_PANEL_EXPORT_THEME_WITHOUT_ORDER_BACKLOG_BRIDGE_20240429","round":"R1","loop":"118","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","fine_archetype_id":"PROTECTION_PANEL_EXPORT_THEME_WITHOUT_ORDER_BACKLOG_BRIDGE","symbol":"237750","company_name":"피앤씨테크","trigger_type":"Stage2","trigger_date":"2024-04-29","entry_date":"2024-04-29","entry_price":6550.0,"entry_price_basis":"close","price_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/237/237750/2024.csv + 2025.csv","profile_path":"atlas/symbol_profiles/237/237750.json","stock_web_manifest_max_date":"2026-02-20","forward_window_trading_days":180,"MFE_30D_pct":16.64,"MFE_90D_pct":16.64,"MFE_180D_pct":16.64,"MAE_30D_pct":-12.98,"MAE_90D_pct":-32.21,"MAE_180D_pct":-49.92,"peak_date":"2024-05-08","peak_price":7640.0,"max_drawdown_low":3280.0,"max_drawdown_low_date":"2024-12-09","drawdown_after_peak_pct":-57.07,"below_entry_price_flag_30d":true,"below_entry_price_flag_90d":true,"positive_or_counterexample":"counterexample","case_type":"failed_rerating","trigger_outcome_label":"counterexample_source_proxy_theme_low_mfe_deep_mae","current_profile_verdict":"current_profile_correct_if_source_proxy_only_is_blocked; false_positive_if_product_keyword_gets_stage2_actionable_credit","current_profile_error":false,"current_profile_false_positive":false,"current_profile_too_late":false,"current_profile_missed_structural":false,"current_profile_4B_too_early":false,"current_profile_4C_too_late":false,"calibration_usable":true,"calibration_block_reasons":[],"usable_for_v12_shadow_calibration":true,"usable_for_archetype_shadow":true,"usable_for_sector_shadow":true,"usable_for_global_promotion":false,"usable_for_new_weight_evidence":false,"usable_for_weight_calibration":false,"guardrail_usable":true,"is_new_independent_case":true,"do_not_count_as_new_case":false,"is_aggregate_representative":true,"aggregate_group_role":"representative","dedupe_for_aggregate":true,"dedupe_key":"v12_strict|237750|C02_POWER_GRID_DATACENTER_CAPEX|Stage2|2024-04-29|2024-04-29|6550.0|PROTECTION_PANEL_EXPORT_THEME_WITHOUT_ORDER_BACKLOG_BRIDGE","same_entry_group_id":"C02_POWER_GRID_DATACENTER_CAPEX_237750_2024-04-29_6550","dedupe_member_count":1,"source_proxy_only":true,"evidence_available_at_that_date":"Theme article tied AI-data-center power demand to power-equipment cycle and noted transformer-protection panels/export regions, but did not supply company-specific signed order, backlog, customer lock, CAPA, ASP, or margin conversion.","evidence_source":"MoneyToday/Daum 2024-04-29","evidence_url":"https://v.daum.net/v/20240429103131538","evidence_url_pending":false,"independent_evidence_weight":1.0,"stage2_evidence_fields":["power_equipment_theme","product_category_match","export_regions_claim"],"stage3_evidence_fields":["none_confirmed"],"stage4b_evidence_fields":["price_only_local_peak_watch"],"stage4c_evidence_fields":["bridge_absent_watch"],"four_b_evidence_type":["price_only_local_peak_watch"],"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"proxy_theme_peak_should_remain_watch_or_local_4B_not_full_4B","four_c_protection_label":"not_applicable","green_lateness_ratio":"not_measured","corporate_action_window_status":"clean_180D_window; profile corporate_action_candidate_count=0","price_path_valid":true,"validation_reasons":[],"residual_counterexample":true,"loop_objective":"coverage_gap_fill|counterexample_mining|sector_specific_rule_discovery|stage2_actionable_bonus_stress_test|4B_non_price_requirement_stress_test","source_file":"docs/round/e2r_stock_web_v12_residual_round_R1_loop_118_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C02_POWER_GRID_DATACENTER_CAPEX_research.md"}
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","trigger_id":"R1L118_C02_006340_20240613_STAGE2","case_id":"C02_R1L118_006340_CABLE_COPPER_AI_POWER_PROXY_WITHOUT_CONTRACT_LOCK_20240613","round":"R1","loop":"118","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","fine_archetype_id":"CABLE_COPPER_AI_POWER_PROXY_WITHOUT_CONTRACT_LOCK","symbol":"006340","company_name":"대원전선","trigger_type":"Stage2","trigger_date":"2024-06-12","entry_date":"2024-06-13","entry_price":3635.0,"entry_price_basis":"close","price_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/006/006340/2024.csv + 2025.csv","profile_path":"atlas/symbol_profiles/006/006340.json","stock_web_manifest_max_date":"2026-02-20","forward_window_trading_days":180,"MFE_30D_pct":31.36,"MFE_90D_pct":31.36,"MFE_180D_pct":31.36,"MAE_30D_pct":-8.25,"MAE_90D_pct":-29.85,"MAE_180D_pct":-39.34,"peak_date":"2024-06-28","peak_price":4775.0,"max_drawdown_low":2205.0,"max_drawdown_low_date":"2024-12-09","drawdown_after_peak_pct":-53.82,"below_entry_price_flag_30d":true,"below_entry_price_flag_90d":true,"positive_or_counterexample":"counterexample","case_type":"failed_rerating","trigger_outcome_label":"counterexample_cable_copper_proxy_high_early_mfe_deep_mae","current_profile_verdict":"current_profile_correct_if_cable_copper_beta_is_not_compressed_into_full_C02_without_contract_backlog_bridge","current_profile_error":false,"current_profile_false_positive":false,"current_profile_too_late":false,"current_profile_missed_structural":false,"current_profile_4B_too_early":false,"current_profile_4C_too_late":false,"calibration_usable":true,"calibration_block_reasons":[],"usable_for_v12_shadow_calibration":true,"usable_for_archetype_shadow":true,"usable_for_sector_shadow":true,"usable_for_global_promotion":false,"usable_for_new_weight_evidence":false,"usable_for_weight_calibration":false,"guardrail_usable":true,"is_new_independent_case":true,"do_not_count_as_new_case":false,"is_aggregate_representative":true,"aggregate_group_role":"representative","dedupe_for_aggregate":true,"dedupe_key":"v12_strict|006340|C02_POWER_GRID_DATACENTER_CAPEX|Stage2|2024-06-13|2024-06-13|3635.0|CABLE_COPPER_AI_POWER_PROXY_WITHOUT_CONTRACT_LOCK","same_entry_group_id":"C02_POWER_GRID_DATACENTER_CAPEX_006340_2024-06-13_3635","dedupe_member_count":1,"source_proxy_only":true,"evidence_available_at_that_date":"AI power-demand/copper-price article explained cable-sector beta and pass-through economics, but lacked company-specific DC/grid contract, backlog, customer lock, CAPA allocation, or durable margin bridge.","evidence_source":"TheBell 2024-06-12","evidence_url":"https://www.thebell.co.kr/front/newsview.asp?key=202406112215446480103775","evidence_url_pending":false,"independent_evidence_weight":1.0,"stage2_evidence_fields":["ai_power_demand_theme","cable_beta","copper_price_pass_through"],"stage3_evidence_fields":["none_confirmed"],"stage4b_evidence_fields":["price_only_peak_after_theme"],"stage4c_evidence_fields":["no_contract_backlog_bridge"],"four_b_evidence_type":["price_only_peak_after_theme"],"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"proxy_theme_peak_should_remain_watch_or_local_4B_not_full_4B","four_c_protection_label":"not_applicable","green_lateness_ratio":"not_measured","corporate_action_window_status":"clean_180D_window; profile corporate-action candidates pre-2011 only","price_path_valid":true,"validation_reasons":[],"residual_counterexample":true,"loop_objective":"coverage_gap_fill|counterexample_mining|sector_specific_rule_discovery|stage2_actionable_bonus_stress_test|4B_non_price_requirement_stress_test","source_file":"docs/round/e2r_stock_web_v12_residual_round_R1_loop_118_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C02_POWER_GRID_DATACENTER_CAPEX_research.md"}
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","trigger_id":"R1L118_C02_237750_20240508_STAGE4B_PRICE_ONLY_LOCAL_PEAK","case_id":"C02_R1L118_237750_PRICE_ONLY_4B_OVERLAY_20240508","round":"R1","loop":"118","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","fine_archetype_id":"PROTECTION_PANEL_PROXY_THEME_PRICE_ONLY_4B_OVERLAY","symbol":"237750","company_name":"피앤씨테크","trigger_type":"Stage4B","trigger_date":"2024-05-08","entry_date":"2024-05-08","entry_price":6990.0,"entry_price_basis":"close","price_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/237/237750/2024.csv + 2025.csv","profile_path":"atlas/symbol_profiles/237/237750.json","stock_web_manifest_max_date":"2026-02-20","forward_window_trading_days":180,"MFE_30D_pct":9.3,"MFE_90D_pct":9.3,"MFE_180D_pct":9.3,"MAE_30D_pct":-18.45,"MAE_90D_pct":-37.12,"MAE_180D_pct":-53.08,"peak_date":"2024-05-08","peak_price":7640.0,"max_drawdown_low":3280.0,"max_drawdown_low_date":"2024-12-09","drawdown_after_peak_pct":-57.07,"below_entry_price_flag_30d":true,"below_entry_price_flag_90d":true,"positive_or_counterexample":"counterexample","case_type":"4B_overlay_price_only_guardrail","trigger_outcome_label":"price_only_local_peak_after_proxy_theme_low_forward_mfe_deep_mae","current_profile_verdict":"current_profile_correct_if_full_4B_requires_non_price_evidence; overlay is guardrail-only","current_profile_error":false,"current_profile_false_positive":false,"current_profile_too_late":false,"current_profile_missed_structural":false,"current_profile_4B_too_early":false,"current_profile_4C_too_late":false,"calibration_usable":true,"calibration_block_reasons":[],"usable_for_v12_shadow_calibration":true,"usable_for_archetype_shadow":true,"usable_for_sector_shadow":true,"usable_for_global_promotion":false,"usable_for_new_weight_evidence":false,"usable_for_weight_calibration":false,"guardrail_usable":true,"is_new_independent_case":false,"do_not_count_as_new_case":true,"is_aggregate_representative":false,"aggregate_group_role":"4B_overlay_guardrail_only","dedupe_for_aggregate":false,"dedupe_key":"v12_strict|237750|C02_POWER_GRID_DATACENTER_CAPEX|Stage4B|2024-05-08|2024-05-08|6990.0|PROTECTION_PANEL_PROXY_THEME_PRICE_ONLY_4B_OVERLAY","same_entry_group_id":"C02_POWER_GRID_DATACENTER_CAPEX_237750_2024-05-08_6990","dedupe_member_count":1,"source_proxy_only":true,"evidence_available_at_that_date":"price-only/local-peak overlay after the 2024-04-29 proxy-theme article; no signed order/backlog/customer/CAPA/margin bridge added by the peak date.","evidence_source":"Songdaiki/stock-web price path + MoneyToday/Daum proxy-theme article","evidence_url":"https://v.daum.net/v/20240429103131538","evidence_url_pending":false,"independent_evidence_weight":1.0,"stage2_evidence_fields":["proxy_theme_prior"],"stage3_evidence_fields":["none_confirmed"],"stage4b_evidence_fields":["price_only_local_peak","post_theme_low_forward_mfe","deep_forward_mae"],"stage4c_evidence_fields":["bridge_absent_watch"],"four_b_evidence_type":["price_only","proxy_theme_bridge_missing"],"four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"price_only_local_4B_watch_valid; full_4B_not_valid_without_non_price_deterioration_evidence","four_c_protection_label":"watch_only_not_hard_4C","green_lateness_ratio":"not_applicable","corporate_action_window_status":"clean_180D_window; profile corporate_action_candidate_count=0","price_path_valid":true,"validation_reasons":[],"residual_counterexample":true,"loop_objective":"4B_non_price_requirement_stress_test","source_file":"docs/round/e2r_stock_web_v12_residual_round_R1_loop_118_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C02_POWER_GRID_DATACENTER_CAPEX_research.md"}
{"row_type":"score_simulation","schema_family":"v12_sector_archetype_residual","round":"R1","loop":"118","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","fine_archetype_id":"GRID_TRANSFORMER_BACKLOG_PRICE_REALIZATION_CONFIRMED","symbol":"267260","company_name":"HD현대일렉트릭","profile_before":"e2r_2_2_rolling_calibrated_P0_current","profile_after_shadow":"P2_C02_confirmed_bridge_plus_proxy_penalty","weighted_score_before":80,"weighted_score_after_shadow":83,"stage_before":"Stage3-Yellow","stage_after_shadow":"Stage3-Yellow","raw_component_scores":{"order_backlog":9,"capa_lock":7,"customer_visibility":8,"margin_realization":9,"source_quality":9,"proxy_penalty":0,"construction_or_balance_risk":0},"component_delta_explanation":"Shadow-only C02 stress profile credits confirmed order/backlog/CAPA/margin bridges and subtracts proxy-theme/product-category-only beta.","production_scoring_changed":false,"source_file":"docs/round/e2r_stock_web_v12_residual_round_R1_loop_118_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C02_POWER_GRID_DATACENTER_CAPEX_research.md"}
{"row_type":"score_simulation","schema_family":"v12_sector_archetype_residual","round":"R1","loop":"118","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","fine_archetype_id":"SMALL_TRANSFORMER_US_EXPORT_BACKLOG_CAPACITY_LOCK","symbol":"033100","company_name":"제룡전기","profile_before":"e2r_2_2_rolling_calibrated_P0_current","profile_after_shadow":"P2_C02_confirmed_bridge_plus_proxy_penalty","weighted_score_before":72,"weighted_score_after_shadow":79,"stage_before":"Stage2-Actionable","stage_after_shadow":"Stage3-Yellow","raw_component_scores":{"order_backlog":8,"capa_lock":7,"customer_visibility":7,"margin_realization":9,"source_quality":8,"proxy_penalty":0,"construction_or_balance_risk":0},"component_delta_explanation":"Shadow-only C02 stress profile credits confirmed order/backlog/CAPA/margin bridges and subtracts proxy-theme/product-category-only beta.","production_scoring_changed":false,"source_file":"docs/round/e2r_stock_web_v12_residual_round_R1_loop_118_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C02_POWER_GRID_DATACENTER_CAPEX_research.md"}
{"row_type":"score_simulation","schema_family":"v12_sector_archetype_residual","round":"R1","loop":"118","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","fine_archetype_id":"HEAVY_TRANSFORMER_CHAWON_MEMPHIS_CAPA_ORDER_GUIDANCE","symbol":"298040","company_name":"효성중공업","profile_before":"e2r_2_2_rolling_calibrated_P0_current","profile_after_shadow":"P2_C02_confirmed_bridge_plus_proxy_penalty","weighted_score_before":73,"weighted_score_after_shadow":80,"stage_before":"Stage2-Actionable","stage_after_shadow":"Stage3-Yellow","raw_component_scores":{"order_backlog":8,"capa_lock":9,"customer_visibility":7,"margin_realization":8,"source_quality":8,"proxy_penalty":0,"construction_or_balance_risk":-2},"component_delta_explanation":"Shadow-only C02 stress profile credits confirmed order/backlog/CAPA/margin bridges and subtracts proxy-theme/product-category-only beta.","production_scoring_changed":false,"source_file":"docs/round/e2r_stock_web_v12_residual_round_R1_loop_118_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C02_POWER_GRID_DATACENTER_CAPEX_research.md"}
{"row_type":"score_simulation","schema_family":"v12_sector_archetype_residual","round":"R1","loop":"118","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","fine_archetype_id":"PROTECTION_PANEL_EXPORT_THEME_WITHOUT_ORDER_BACKLOG_BRIDGE","symbol":"237750","company_name":"피앤씨테크","profile_before":"e2r_2_2_rolling_calibrated_P0_current","profile_after_shadow":"P2_C02_confirmed_bridge_plus_proxy_penalty","weighted_score_before":64,"weighted_score_after_shadow":56,"stage_before":"Stage2","stage_after_shadow":"Watch","raw_component_scores":{"order_backlog":0,"capa_lock":0,"customer_visibility":0,"margin_realization":0,"source_quality":4,"proxy_penalty":-8,"construction_or_balance_risk":0},"component_delta_explanation":"Shadow-only C02 stress profile credits confirmed order/backlog/CAPA/margin bridges and subtracts proxy-theme/product-category-only beta.","production_scoring_changed":false,"source_file":"docs/round/e2r_stock_web_v12_residual_round_R1_loop_118_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C02_POWER_GRID_DATACENTER_CAPEX_research.md"}
{"row_type":"score_simulation","schema_family":"v12_sector_archetype_residual","round":"R1","loop":"118","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","fine_archetype_id":"CABLE_COPPER_AI_POWER_PROXY_WITHOUT_CONTRACT_LOCK","symbol":"006340","company_name":"대원전선","profile_before":"e2r_2_2_rolling_calibrated_P0_current","profile_after_shadow":"P2_C02_confirmed_bridge_plus_proxy_penalty","weighted_score_before":63,"weighted_score_after_shadow":55,"stage_before":"Stage2","stage_after_shadow":"Watch","raw_component_scores":{"order_backlog":0,"capa_lock":0,"customer_visibility":0,"margin_realization":3,"source_quality":5,"proxy_penalty":-8,"construction_or_balance_risk":0},"component_delta_explanation":"Shadow-only C02 stress profile credits confirmed order/backlog/CAPA/margin bridges and subtracts proxy-theme/product-category-only beta.","production_scoring_changed":false,"source_file":"docs/round/e2r_stock_web_v12_residual_round_R1_loop_118_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C02_POWER_GRID_DATACENTER_CAPEX_research.md"}
{"row_type":"shadow_weight_change_candidate","schema_family":"v12_sector_archetype_residual","round":"R1","loop":"118","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","axis_id":"C02_CONFIRMED_ORDER_BACKLOG_CAPA_MARGIN_BRIDGE_VS_PROXY_THEME","axis_scope":"canonical_archetype_specific","profile_tested":"P2_C02_confirmed_bridge_plus_proxy_penalty","direction":"increase_confirmed_bridge_weight_and_proxy_penalty","proposed_delta_not_for_production":{"confirmed_order_backlog_capa_margin_bridge_bonus":"+4_to_+7","source_proxy_only_product_keyword_penalty":"-6_to_-10","full_4B_non_price_evidence_requirement":"unchanged_strengthen"},"positive_support_symbols":["267260","033100","298040"],"counterexample_support_symbols":["237750","006340"],"4B_overlay_support_symbols":["237750"],"do_not_apply_directly":true,"production_scoring_changed":false,"confidence":"medium_low_single_loop_only","source_file":"docs/round/e2r_stock_web_v12_residual_round_R1_loop_118_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C02_POWER_GRID_DATACENTER_CAPEX_research.md"}
{"row_type":"residual_contribution","schema_family":"v12_sector_archetype_residual","round":"R1","loop":"118","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","selected_priority_bucket":"Priority_0_under_30_rows","index_before_representative_rows":10,"representative_rows_added_if_accepted":5,"index_after_estimated_representative_rows":15,"new_symbol_count":5,"positive_case_count":3,"counterexample_count":2,"stage4b_overlay_count":1,"current_profile_error_count":2,"main_residual":"C02 should differentiate hard transformer/grid equipment rerating with order/backlog/CAPA/margin conversion from proxy-theme product-category or copper/cable beta.","rule_candidate":"confirmed bridge required for Stage2-Actionable/Yellow; proxy-theme-only C02 remains Watch or local 4B guardrail","loop_contribution_label":"canonical_archetype_rule_candidate","source_file":"docs/round/e2r_stock_web_v12_residual_round_R1_loop_118_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C02_POWER_GRID_DATACENTER_CAPEX_research.md"}
```

## 9. Batch ingest self-audit

```yaml
v12_schema_family_present: true
trigger_rows_present: true
price_source_validation_rows_present: true
score_simulation_rows_present: true
shadow_weight_change_candidate_rows_present: true
residual_contribution_rows_present: true
required_mfe_mae_fields_present: true
mfe_mae_30_90_180_all_present: true
entry_date_present: true
entry_price_present: true
price_source_present: true
price_basis_present: true
price_adjustment_status_present: true
large_sector_id_present: true
canonical_archetype_id_present: true
trigger_type_enum_valid: true
positive_case_count: 3
counterexample_count: 2
stage4b_overlay_count: 1
new_independent_case_count: 5
new_symbol_count: 5
duplicate_top_covered_c02_symbols_used: false
production_scoring_changed: false
do_not_apply_directly: true
```

## 10. Deferred handoff prompt — DO NOT EXECUTE NOW

```text
Read this MD as one v12 residual research artifact. Do not change production scoring directly.
Run the standard v12 ingest/validation/dedupe/aggregate path. Treat NO-REPEAT INDEX as the duplicate ledger.
If rows validate, add the five representative C02 cases and one guardrail-only Stage4B overlay.
Evaluate the shadow candidate:
C02_CONFIRMED_ORDER_BACKLOG_CAPA_MARGIN_BRIDGE_VS_PROXY_THEME.
Promote only if subsequent loops confirm that confirmed transformer/grid order-backlog-CAPA-margin evidence improves Stage2/Stage3 timing without increasing proxy-theme false positives.
```


## Source notes

- MAIN EXECUTION PROMPT: https://raw.githubusercontent.com/Songdaiki/stock_agent/main/docs/core/e2r_v12_prompt_round_scheduler_corrected.txt
- NO-REPEAT INDEX: https://raw.githubusercontent.com/Songdaiki/stock_agent/main/docs/core/V12_Research_No_Repeat_Index.md
- stock-web manifest: https://raw.githubusercontent.com/Songdaiki/stock-web/main/atlas/manifest.json
- stock-web schema: https://raw.githubusercontent.com/Songdaiki/stock-web/main/atlas/schema.md
- HD현대일렉트릭 1Q24 release: https://www.newswire.co.kr/newsRead.php?no=988377
- HD현대일렉트릭 1Q24 Daum/Herald coverage: https://v.daum.net/v/20240423144258485?f=p
- 제룡전기 Yuanta report: https://ssl.pstatic.net/imgstock/upload/research/company/1709852777300.pdf
- 제룡전기 AsiaEconomy report coverage: https://view.asiae.co.kr/realtime/sokbo_viewNew.htm?idxno=2024030809242302536
- 제룡전기 BigDataNews/NH follow-up: https://www.thebigdata.co.kr/view.php?ud=202405290538457085cd1e7f0bdf_23
- 효성중공업 LS Securities report: https://file.alphasquare.co.kr/media/pdfs/company-report/_%ED%9A%A8%EC%84%B1%EC%A4%91%EA%B3%B5%EC%97%85_4Q24%20Preview_250115%E2%98%86_%EC%84%B1%EC%A2%85%ED%99%94_1899_Online%20report%20_%206_10p_%ED%9A%A8%EC%84%B1%EC%A4%91%EA%B3%B5%EC%97%85.pdf
- 피앤씨테크 Daum/MoneyToday proxy-theme article: https://v.daum.net/v/20240429103131538
- 대원전선 TheBell article: https://www.thebell.co.kr/front/newsview.asp?key=202406112215446480103775


## Final one-line conclusion

C02 should not be keyed to “AI power demand” alone. It should be keyed to the hard bridge: **order/backlog or customer lock, CAPA/lead-time scarcity, ASP or margin realization, and revenue/EPS conversion**. Without that bridge, the case belongs in Watch or price-only local 4B guardrail.
