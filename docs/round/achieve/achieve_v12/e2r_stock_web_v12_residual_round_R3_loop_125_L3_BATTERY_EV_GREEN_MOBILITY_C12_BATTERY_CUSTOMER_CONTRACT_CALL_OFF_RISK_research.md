# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```yaml
output_file: e2r_stock_web_v12_residual_round_R3_loop_125_L3_BATTERY_EV_GREEN_MOBILITY_C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK_research.md
selected_round: R3
selected_loop: 125
selection_basis: docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket: Priority 1 / under_50_rows_static_ledger / C12 rows 32 need_to_50 18 before this local loop
round_schedule_status: coverage_index_selected
round_sector_consistency: pass
large_sector_id: L3_BATTERY_EV_GREEN_MOBILITY
canonical_archetype_id: C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK
fine_archetype_id: BATTERY_CUSTOMER_CONTRACT_CALLOFF_DEMAND_RISK_VS_CONTRACT_HEADLINE
loop_objective: coverage_gap_fill|counterexample_mining|4C_thesis_break_timing_test|stage2_actionable_bonus_stress_test|canonical_archetype_compression|sector_specific_rule_discovery
price_source: Songdaiki/stock-web
price_basis: tradable_raw
price_adjustment_status: raw_unadjusted_marcap
stock_web_manifest_max_date: 2026-02-20
production_scoring_changed: false
shadow_weight_only: true
handoff_prompt_embedded: true
handoff_prompt_executed_now: false
```

This loop adds 5 new independent calibration-usable cases, 4 counterexamples, and 6 residual errors for R3/L3/C12. It separates customer-contract headlines from actual call-off cadence, utilization, ASP survival, inventory rebalancing and margin/cash conversion.

## 1. Current Calibrated Profile Assumption

```text
current_default_profile_proxy = e2r_2_1_stock_web_calibrated_proxy
rollback_reference_profile_id = e2r_2_0_baseline_reference
production_scoring_changed = false
shadow_weight_only = true
already_applied_axes_tested = stage2_actionable_evidence_bonus | price_only_blowoff_blocks_positive_stage | full_4b_requires_non_price_evidence | hard_4c_thesis_break_routes_to_4c
```

The current profile already knows that price-only blowoff cannot promote Stage2/Stage3 and that hard 4C requires non-price thesis break. C12 needs a narrower battery-contract rule: a named customer or large contract is not enough unless the customer actually calls off volume and the ramp survives demand, ASP and utilization pressure.

## 2. Round / Large Sector / Canonical Archetype Scope

|field|value|
|---|---|
|round|R3|
|large_sector_id|L3_BATTERY_EV_GREEN_MOBILITY|
|canonical_archetype_id|C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK|
|fine_archetype_id|BATTERY_CUSTOMER_CONTRACT_CALLOFF_DEMAND_RISK_VS_CONTRACT_HEADLINE|
|round_sector_consistency|pass|
|R3_mapping_reason|C11~C14 map to R3 / L3_BATTERY_EV_GREEN_MOBILITY|

## 3. Previous Coverage / Duplicate Avoidance Check

Static No-Repeat Index state: C12 has 32 representative rows and needs 18 rows to reach the 50-row practical calibration zone. The current interactive run already produced fresh Priority-0 passes for C02/C09/C14/C10/C06/C07/C11/C01/C28, so C12 is the next non-duplicate Priority-1 battery-contract gap.

```text
hard_duplicate_key = canonical_archetype_id + symbol + trigger_type + entry_date
hard_duplicates_in_this_file = 0
new_independent_case_ratio = 1.00 among calibration-usable trigger rows
```

## 4. Stock-Web OHLC Input / Price Source Validation

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","source_name":"FinanceData/marcap","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration","caveat":"raw/unadjusted OHLC; corporate-action-contaminated windows are blocked by default"}
```

Formula used: `MFE_ND_pct = (max(high from entry_date through N trading rows) / entry_price - 1) * 100`; `MAE_ND_pct = (min(low from entry_date through N trading rows) / entry_price - 1) * 100`. Entry price is the stock-web tradable close on `entry_date`.

## 5. Historical Eligibility Gate

|symbol|entry_date|entry_price|forward_window_trading_days|corporate_action_window_status|calibration_usable|
|---|---|---|---|---|---|
|373220|2024-01-26|381000.0|180|clean_180D_window_by_local_tradable_rows_share_count_constant|True|
|247540|2024-02-07|230500.0|180|clean_180D_window_by_local_tradable_rows_share_count_constant|True|
|003670|2024-02-01|260000.0|180|clean_180D_window_by_local_tradable_rows_share_count_constant|True|
|393890|2024-02-16|42000.0|180|clean_180D_window_by_local_tradable_rows_share_count_constant|True|
|336370|2024-02-01|11160.0|180|clean_180D_window_by_local_tradable_rows_share_count_constant|True|
|348370|2024-01-25|113600.0|180+ local rows but blocked|blocked_share_count_change|False|
|066970|2023-02-28|262000.0|180+ local rows but blocked|blocked_share_count_change|False|

## 6. Canonical Archetype Compression Map

|symbol|fine_archetype_id|compressed_to|role|stage2_key|risk_key|
|---|---|---|---|---|---|
|373220|LGES_OEM_INVENTORY_CONTROL_EV_DEMAND_SLOWDOWN_CAPEX_PRIORITY_GUARD|C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK|counterexample|named_OEM_customer_base/inventory_control_or_calloff_risk/capex_priority_adjustment|utilization_adjustment/ASP_metal_price_pressure/weak_90D_asymmetry|
|247540|CATHODE_CUSTOMER_INVENTORY_ADJUSTMENT_SKON_SAMSUNGSDI_ASP_MARGIN_GUARD|C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK|counterexample|major_customer_inventory_adjustment/cathode_supply_chain_contract_base|ASP_decline/inventory_valuation_loss/MAE90_below_minus20/operating_loss_if_customer_inventory_adjustment_persists|
|003670|CATHODE_CONTRACT_BASE_RAW_MATERIAL_PRICE_CUSTOMER_DEMAND_MARGIN_GUARD|C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK|counterexample|battery_materials_contract_base/high_nickel_product_mix|raw_material_price_decline/inventory_valuation_loss/MAE180_below_minus20/margin_collapse_if_customer_demand_and_ASP_do_not_recover|
|393890|SEPARATOR_CLIENT_STOCK_REBALANCING_EUROPE_DEMAND_REDUCTION_HARD4C|C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK|counterexample|separator_customer_contract_base|low_MFE/MAE90_below_minus30/client_stock_rebalancing/reduced_client_demand_and_shipment_stagnation|
|336370|BATTERY_COPPER_FOIL_CUSTOMER_DIVERSIFICATION_SUPPLY_VOLUME_POSITIVE_WATCH|C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK|positive|customer_diversification/battery_copper_foil_supply_growth/top_ten_customer_base|source_repair_required/proof_of_mass_production_timing_required|
|348370|ELECTROLYTE_NORTH_AMERICA_TOP_TIER_CUSTOMER_CONTRACT_BLOWOFF_SHARECOUNT_GUARD|C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK|positive_blocked|named_top_tier_customer_contract/North_America_localization|valuation_blowoff/share_count_change_inside_window|
|066970|TESLA_HIGH_NICKEL_CATHODE_CONTRACT_LATER_CALLOFF_REVERSAL_GUARD|C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK|counterexample_blocked|named_customer_Tesla/large_supply_contract|large_contract_size_but_calloff_risk/share_count_change_inside_window/later_contract_reduction_validates_calloff_risk|

## 7. Case Selection Summary

|symbol|company_name|case_type|positive_or_counterexample|calibration_usable|current_profile_verdict|score_price_alignment|
|---|---|---|---|---|---|---|
|373220|LG Energy Solution|failed_rerating|counterexample|True|current_profile_false_positive|counterexample_moderate_MFE_high_MAE_demand_slowdown_guard|
|247540|EcoPro BM|failed_rerating|counterexample|True|current_profile_false_positive|counterexample_customer_inventory_adjustment_low_MFE_deep_MAE|
|003670|POSCO Future M|failed_rerating|counterexample|True|current_profile_false_positive|counterexample_contract_base_not_enough_without_price_margin_recovery|
|393890|WCP|failed_rerating|counterexample|True|current_profile_4C_too_late|hard_4c_candidate_client_stock_rebalancing_low_MFE_deep_MAE|
|336370|Solus Advanced Materials|structural_success|positive|True|current_profile_correct|positive_customer_diversification_with_controlled_MAE_source_repair_required|
|348370|Enchem|narrative_only|blocked_guardrail|False|current_profile_4B_too_late|positive_price_path_but_share_count_contaminated_local4B_overlay|
|066970|L&F|narrative_only|counterexample|False|current_profile_4C_too_late|contract_headline_later_calloff_reversal_sharecount_contaminated|

## 8. Positive vs Counterexample Balance

|metric|value|
|---|---|
|calibration_usable_trigger_count|5|
|representative_trigger_count|5|
|positive_case_count|1|
|counterexample_count|4|
|narrative_only_or_rejected_count|2|
|stage4b_overlay_count|7|
|stage4c_case_count|4|
|current_profile_error_count|6|

## 9. Evidence Source Map

|symbol|company_name|trigger_date|evidence_summary|evidence_source|
|---|---|---|---|---|
|373220|LG Energy Solution|2024-01-26|LGES forecast temporary slowdown in global EV battery demand due to OEM conservative inventory control and metal price decline; Q1 showed utilization adjustment and demand weakening.|https://www.reuters.com/business/battery-firm-lg-energy-solutions-q4-profit-up-43-higher-us-output-2024-01-26/; https://inside.lgensol.com/en/2024/04/lg-energy-solution-makes-progress-amid-market-uncertainties-aims-to-strengthen-fundamental-competitiveness-this-year/|
|247540|EcoPro BM|2024-02-07|EcoPro BM earnings path was pressured by inventory adjustments at SK On and Samsung SDI and cathode ASP decline; later Q3 results confirmed revenue decline and operating loss.|https://securities.miraeasset.com/bbs/download/2126480.pdf?attachmentId=2126480; https://www.asiae.co.kr/en/article/2024110110191994466|
|003670|POSCO Future M|2024-02-01|2024 full-year result later showed revenue/profitability declined due to cathode price decreases, inventory valuation losses, and an emergency management response to post-chasm conditions.|https://www.poscofuturem.com/en/pr/view.do?num=899|
|393890|WCP|2024-02-16|Separator makers including WCP later showed shipment stagnation due to reduced European customer demand and client stock rebalancing, matching the 2024 price-path failure mode.|https://www.sneresearch.com/en/insight/release_view/433/page/96?s_cat=%7C1%7C&s_keyword=|
|336370|Solus Advanced Materials|2024-02-01|Solus described maintained partnerships and new supply agreements with global top-ten battery cell and OEM customers; separate 2024 supply-volume disclosures support a customer-diversification bridge but exact as-of trigger requires source repair.|https://www.solusadvancedmaterials.com/en/ir/shareholder-letter/; https://www.miningstockeducation.com/2024/06/solus-advanced-materials-significantly-increases-its-supply-of-battery-copper-foil-to-north-american-customers-expanding-influence-in-the-global-market/|
|348370|Enchem|2024-01-25|Enchem announced consecutive product supply contracts with global top-tier North American customers including LG Energy Solution and SK On.|https://www.asiae.co.kr/en/article/2024012508342937399|
|066970|L&F|2023-02-28|L&F signed a high-nickel cathode supply deal with Tesla in 2023; later disclosures showed the contract value was effectively reduced amid changed global EV and battery supply conditions.|https://www.kedglobal.com/batteries/newsView/ked202302280017; https://www.asiae.co.kr/en/article/2025122918185667860|

## 10. Price Data Source Map

|symbol|price_shard_path|profile_path|price_basis|entry_date|
|---|---|---|---|---|
|373220|atlas/ohlcv_tradable_by_symbol_year/373/373220/2024.csv|atlas/symbol_profiles/373/373220.json|tradable_raw|2024-01-26|
|247540|atlas/ohlcv_tradable_by_symbol_year/247/247540/2024.csv|atlas/symbol_profiles/247/247540.json|tradable_raw|2024-02-07|
|003670|atlas/ohlcv_tradable_by_symbol_year/003/003670/2024.csv|atlas/symbol_profiles/003/003670.json|tradable_raw|2024-02-01|
|393890|atlas/ohlcv_tradable_by_symbol_year/393/393890/2024.csv|atlas/symbol_profiles/393/393890.json|tradable_raw|2024-02-16|
|336370|atlas/ohlcv_tradable_by_symbol_year/336/336370/2024.csv|atlas/symbol_profiles/336/336370.json|tradable_raw|2024-02-01|
|348370|atlas/ohlcv_tradable_by_symbol_year/348/348370/2024.csv|atlas/symbol_profiles/348/348370.json|tradable_raw|2024-01-25|
|066970|atlas/ohlcv_tradable_by_symbol_year/066/066970/2023.csv|atlas/symbol_profiles/066/066970.json|tradable_raw|2023-02-28|

## 11. Case-by-Case Trigger Grid

|trigger_id|symbol|trigger_type|entry_date|case_polarity|current_profile_verdict|aggregate_group_role|
|---|---|---|---|---|---|---|
|TRG_R3L125_C12_373220_20240126_01|373220|Stage2|2024-01-26|counterexample|current_profile_false_positive|representative|
|TRG_R3L125_C12_247540_20240207_02|247540|Stage2|2024-02-07|counterexample|current_profile_false_positive|representative|
|TRG_R3L125_C12_003670_20240201_03|003670|Stage2|2024-02-01|counterexample|current_profile_false_positive|representative|
|TRG_R3L125_C12_393890_20240216_04|393890|Stage4C|2024-02-16|counterexample|current_profile_4C_too_late|representative|
|TRG_R3L125_C12_336370_20240201_05|336370|Stage2-Actionable|2024-02-01|positive|current_profile_correct|representative|
|narrative_only|348370|narrative_only|2024-01-25|blocked_guardrail|current_profile_4B_too_late|narrative_only|
|narrative_only|066970|narrative_only|2023-02-28|blocked_guardrail|current_profile_4C_too_late|narrative_only|

## 12. Trigger-Level OHLC Backtest Tables

|symbol|entry_date|entry_price|MFE_30D_pct|MAE_30D_pct|MFE_90D_pct|MAE_90D_pct|MFE_180D_pct|MAE_180D_pct|peak_date|peak_price|trough_date|trough_price|
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|373220|2024-01-26|381000.0|10.24|-4.99|10.76|-14.44|16.54|-18.37|2024-10-08|444000.0|2024-08-05|311000.0|
|247540|2024-02-07|230500.0|21.69|-2.17|29.5|-21.26|29.5|-35.49|2024-03-27|298500.0|2024-09-10|148700.0|
|003670|2024-02-01|260000.0|31.15|-7.5|31.15|-7.5|31.15|-24.81|2024-03-13|341000.0|2024-08-05|195500.0|
|393890|2024-02-16|42000.0|17.86|-6.43|17.86|-30.24|17.86|-66.24|2024-03-07|49500.0|2024-11-12|14180.0|
|336370|2024-02-01|11160.0|24.82|-1.34|94.44|-1.34|110.57|-1.34|2024-07-01|23500.0|2024-02-01|11010.0|

## 13. Current Calibrated Profile Stress Test

|symbol|actual_path_label|current_profile_verdict|detail|
|---|---|---|---|
|373220|counterexample_moderate_MFE_high_MAE_demand_slowdown_guard|current_profile_false_positive|Customer base and OEM inventory control evidence justify Stage2-Watch, but Actionable/Yellow should be blocked until utilization and call-off recovery are visible.|
|247540|counterexample_customer_inventory_adjustment_low_MFE_deep_MAE|current_profile_false_positive|Customer inventory adjustment at SK On/Samsung SDI plus ASP pressure should block Stage2-Actionable/Yellow.|
|003670|counterexample_contract_base_not_enough_without_price_margin_recovery|current_profile_false_positive|Battery materials contract base is insufficient when ASP decline, inventory valuation loss and emergency-management language dominate.|
|393890|hard_4c_candidate_client_stock_rebalancing_low_MFE_deep_MAE|current_profile_4C_too_late|Reduced client demand and stock rebalancing are non-price hard-4C evidence; low MFE and deep MAE confirm the route.|
|336370|positive_customer_diversification_with_controlled_MAE_source_repair_required|current_profile_correct|Customer diversification and supply-volume bridge can remain Stage2-Actionable while Green waits for exact customer cadence and margin/cash proof.|
|348370|blocked_guardrail_narrative|current_profile_4B_too_late|Named customer contracts produced blowoff-style MFE, but share-count change and lifecycle risk make it a blocked local-4B audit row.|
|066970|blocked_guardrail_narrative|current_profile_4C_too_late|Large named-customer contract should carry explicit call-off/reduction risk; later Tesla reduction validates the guardrail, but the row is blocked for aggregate.|

## 14. Stage2 / Yellow / Green Comparison

No Stage3-Green row is emitted in this loop. The useful comparison is Stage2/Stage2-Actionable vs later 4B/4C evidence. Customer-contract Stage2 entries had mixed MFE, but the MAE split shows why Yellow/Green must wait: WCP reached -66.24% MAE_180D and EcoPro BM reached -35.49% MAE_180D despite customer-contract relevance, while Solus kept MAE_180D at -1.34%.

```text
green_lateness_ratio = not_applicable_no_confirmed_Stage3_Green_trigger
Yellow gate implication = customer contract + call-off/demand/margin survival, not contract size alone
```

## 15. 4B Local vs Full-window Timing Audit

4B is not assigned from price alone. In C12, full-window 4B needs non-price evidence such as customer inventory adjustment, utilization adjustment, ASP/metal price pressure, client stock rebalancing or later contract reduction. Enchem and L&F are narrative-only guardrails: the price paths are informative, but share-count/corporate-action windows block quantitative aggregate use.

|symbol|four_b_evidence|verdict|
|---|---|---|
|373220|utilization adjustment / metal price pressure|watch not full 4B unless customer schedule weakens|
|247540|customer inventory adjustment / ASP decline / loss risk|full 4B guardrail candidate|
|003670|raw material price decline / inventory valuation loss|full 4B guardrail candidate|
|393890|client stock rebalancing and reduced demand|4B to hard-4C route|
|336370|source repair required|not full 4B; positive watch|
|348370|valuation blowoff / share-count change|narrative-only local 4B|
|066970|later contract reduction / share-count change|narrative-only delayed call-off guardrail|

## 16. 4C Protection Audit

Hard 4C should not trigger when a contract merely feels uncertain. It should trigger when customer call-off, stock rebalancing, utilization reduction, contract reduction, or repeated operating loss breaks the thesis. WCP is the cleanest hard-4C usable row in this file; L&F is the archetypal delayed contract-reduction warning but remains narrative-only until corporate-action/share-count verification is repaired.

## 17. Sector-Specific Rule Candidate

```text
L3_BATTERY_CONTRACT_DEMAND_SURVIVAL_GATE: In L3, named customer contracts are Stage2 raw material, not Stage3 proof. Require call-off cadence, customer production schedule, utilization, ASP/pass-through and margin/cash survival before Actionable/Yellow. Route customer inventory adjustment and client stock rebalancing toward 4B/4C.
```

## 18. Canonical-Archetype Rule Candidate

```jsonl
{"row_type":"shadow_rule_candidate","round":"R3","loop":125,"large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","rule_id":"C12_CUSTOMER_CONTRACT_REQUIRES_CALLOFF_AND_DEMAND_SURVIVAL_GATE","rule_scope":"canonical_archetype_specific","rule_text":"For C12, do not promote a named battery customer contract above Stage2-Watch or weak Stage2-Actionable unless call-off cadence, customer production schedule, utilization, ASP/metal pass-through, shipment recovery, margin/cash conversion and low-MAE survival are visible. If customer inventory adjustment, stock rebalancing, utilization adjustment or contract reduction appears, route to Stage4B-watch or hard Stage4C depending on non-price severity.","support_trigger_ids":["TRG_R3L125_C12_373220_20240126_01","TRG_R3L125_C12_247540_20240207_02","TRG_R3L125_C12_003670_20240201_03","TRG_R3L125_C12_393890_20240216_04","TRG_R3L125_C12_336370_20240201_05"],"narrative_guardrail_symbols":["348370","066970"],"candidate_delta":"tighten C12 Stage2-Actionable/Yellow gate; strengthen hard-4C routing where customer call-off, stock rebalancing or contract reduction is explicit; keep AMPC/IRA subsidy economics separate from demand survival","apply_now":false,"shadow_only":true,"production_scoring_changed":false}
```

## 19. Before / After Backtest Comparison

|profile_id|profile_scope|profile_hypothesis|changed_axes|eligible_trigger_count|avg_MFE_90D_pct|avg_MAE_90D_pct|avg_MFE_180D_pct|avg_MAE_180D_pct|false_positive_rate|score_return_alignment_verdict|
|---|---|---|---|---|---|---|---|---|---|---|
|P0_e2r_2_1_stock_web_calibrated_proxy|current_proxy|current global calibrated rules recognize non-price bridge but may overcredit named battery customer contracts before call-off survival is checked|none|5|36.74|-14.96|41.12|-29.25|4/5 usable rows if headline contract is overpromoted|mixed|
|P0b_e2r_2_0_baseline_reference|rollback_reference|older baseline likely overcredits contract size/customer name and under-routes call-off risk|rollback_reference_only|5|36.74|-14.96|41.12|-29.25|high|worse|
|P1_L3_sector_specific_candidate_profile|sector_specific|L3 battery contract scores must subtract inventory adjustment, utilization cuts, ASP decline and client stock rebalancing before Yellow|L3_customer_contract_demand_survival_penalty|5|36.74|-14.96|41.12|-29.25|reduced to 1/5 or 2/5 depending source proxy handling|better|
|P2_C12_canonical_archetype_candidate_profile|canonical_archetype_specific|C12 requires call-off cadence/customer production schedule and margin/cash survival before Actionable/Yellow|C12_CUSTOMER_CONTRACT_REQUIRES_CALLOFF_AND_DEMAND_SURVIVAL_GATE|5|36.74|-14.96|41.12|-29.25|reduced; counterexamples route to watch/4B/4C instead of promotion|best_for_this_loop|
|P3_counterexample_guard_profile|guardrail|customer inventory adjustment, client stock rebalancing, utilization adjustment and later contract reduction are 4B/4C guard words|C12_calloff_inventory_hard4c_guard|4|22.32|-18.36|23.76|-36.23|counterexample-focused|guardrail_pass|

## 20. Score-Return Alignment Matrix

|symbol|weighted_score_before|stage_label_before|weighted_score_after|stage_label_after|MFE_90D_pct|MAE_90D_pct|alignment|
|---|---|---|---|---|---|---|---|
|373220|65.33|Stage2-Actionable|47.12|Stage2|10.76|-14.44|counterexample_moderate_MFE_high_MAE_demand_slowdown_guard|
|247540|65.46|Stage2-Actionable|48.3|Stage2|29.5|-21.26|counterexample_customer_inventory_adjustment_low_MFE_deep_MAE|
|003670|63.39|Stage2-Actionable|46.23|Stage2|31.15|-7.5|counterexample_contract_base_not_enough_without_price_margin_recovery|
|393890|56.3|Stage2-Actionable|44.42|Stage2|17.86|-30.24|hard_4c_candidate_client_stock_rebalancing_low_MFE_deep_MAE|
|336370|77.27|Stage3-Yellow|82.73|Stage3-Yellow|94.44|-1.34|positive_customer_diversification_with_controlled_MAE_source_repair_required|

## 21. Coverage Matrix

|large_sector_id|canonical_archetype_id|fine_archetype_id|positive_case_count|counterexample_count|4B_case_count|4C_case_count|new_independent_case_count|reused_case_count|calibration_usable_trigger_count|representative_trigger_count|current_profile_error_count|sector_rule_candidate|canonical_rule_candidate|coverage_gap_after_this_loop|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|L3_BATTERY_EV_GREEN_MOBILITY|C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK|BATTERY_CUSTOMER_CONTRACT_CALLOFF_DEMAND_RISK_VS_CONTRACT_HEADLINE|1|4|7|4|5|0|5|5|6|L3_BATTERY_CONTRACT_DEMAND_SURVIVAL_GATE|C12_CUSTOMER_CONTRACT_REQUIRES_CALLOFF_AND_DEMAND_SURVIVAL_GATE|static C12 32 + 5 usable local rows = 37; need_to_50 becomes 13 after commit|

## 22. Residual Contribution Summary

```yaml
new_independent_case_count: 5
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 7
new_canonical_archetype_count: 1
new_fine_archetype_count: 7
new_trigger_family_count: 7
tested_existing_calibrated_axes: [stage2_actionable_evidence_bonus, price_only_blowoff_blocks_positive_stage, full_4b_requires_non_price_evidence, hard_4c_thesis_break_routes_to_4c]
residual_error_types_found: [battery_customer_contract_headline_overcredit, customer_inventory_adjustment_false_positive, client_stock_rebalancing_hard4c_late, contract_reduction_calloff_risk_guardrail]
new_axis_proposed: C12_CUSTOMER_CONTRACT_REQUIRES_CALLOFF_AND_DEMAND_SURVIVAL_GATE
existing_axis_strengthened: [stage2_required_bridge, full_4b_requires_non_price_evidence, hard_4c_thesis_break_routes_to_4c]
existing_axis_weakened: null
existing_axis_kept: [price_only_blowoff_blocks_positive_stage]
sector_specific_rule_candidate: L3_BATTERY_CONTRACT_DEMAND_SURVIVAL_GATE
canonical_archetype_rule_candidate: C12_CUSTOMER_CONTRACT_REQUIRES_CALLOFF_AND_DEMAND_SURVIVAL_GATE
no_new_signal_reason: null
loop_contribution_label: canonical_archetype_rule_candidate
do_not_propose_new_weight_delta: false
```

```jsonl
{"row_type":"residual_contribution","round":"R3","loop":"125","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","new_independent_case_count":5,"reused_case_count":0,"new_symbol_count":7,"new_trigger_family_count":7,"tested_existing_calibrated_axes":["stage2_actionable_evidence_bonus","price_only_blowoff_blocks_positive_stage","full_4b_requires_non_price_evidence","hard_4c_thesis_break_routes_to_4c"],"residual_error_types_found":["battery_customer_contract_headline_overcredit","customer_inventory_adjustment_false_positive","client_stock_rebalancing_hard4c_late","contract_reduction_calloff_risk_guardrail"],"loop_contribution_label":"canonical_archetype_rule_candidate","do_not_propose_new_weight_delta":false,"new_axis_proposed":"C12_CUSTOMER_CONTRACT_REQUIRES_CALLOFF_AND_DEMAND_SURVIVAL_GATE","existing_axis_strengthened":["stage2_required_bridge","full_4b_requires_non_price_evidence","hard_4c_thesis_break_routes_to_4c"],"existing_axis_weakened":null}
```

## 23. Validation Scope / Non-Validation Scope

Validated for calibration: 5 clean 180D stock-web trigger rows with all six MFE/MAE fields, canonical trigger labels, entry date, entry price, shard path, profile path, same-entry group id, and aggregate representative flags.

Not validated for quantitative calibration: Enchem and L&F are retained as narrative-only guardrail rows because local stock-web rows show share-count/corporate-action changes inside the 180D window. They are not counted as representative triggers or new independent weight evidence.

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,C12_customer_contract_calloff_survival_gate,canonical_archetype_specific,L3_BATTERY_EV_GREEN_MOBILITY,C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK,0,1,+1,"customer contract headline must be gated by call-off cadence, utilization, ASP survival, inventory rebalancing and margin/cash conversion","reduced false positives in LGES/EcoProBM/POSCOFutureM/WCP while preserving Solus positive watch","TRG_R3L125_C12_373220_20240126_01|TRG_R3L125_C12_247540_20240207_02|TRG_R3L125_C12_003670_20240201_03|TRG_R3L125_C12_393890_20240216_04|TRG_R3L125_C12_336370_20240201_05",5,5,4,medium,canonical_shadow_only,"not production; post-calibrated residual"
```

## 25. Machine-Readable Rows

### 25.1 price_source_validation
```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","source_name":"FinanceData/marcap","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration","caveat":"raw/unadjusted OHLC; corporate-action-contaminated windows are blocked by default"}
```

### 25.2 case rows
```jsonl
{"row_type":"case","case_id":"R3L125-C12-373220-20240126-LGES-DEMAND-SLOWDOWN-CALLOFF-WATCH","symbol":"373220","company_name":"LG Energy Solution","round":"R3","loop":"125","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","fine_archetype_id":"LGES_OEM_INVENTORY_CONTROL_EV_DEMAND_SLOWDOWN_CAPEX_PRIORITY_GUARD","case_type":"failed_rerating","positive_or_counterexample":"counterexample","best_trigger":"TRG_R3L125_C12_373220_20240126_01","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"counterexample_moderate_MFE_high_MAE_demand_slowdown_guard","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"Customer base and OEM inventory control evidence justify Stage2-Watch, but Actionable/Yellow should be blocked until utilization and call-off recovery are visible."}
{"row_type":"case","case_id":"R3L125-C12-247540-20240207-ECOPROBM-CUSTOMER-INVENTORY-ADJUSTMENT","symbol":"247540","company_name":"EcoPro BM","round":"R3","loop":"125","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","fine_archetype_id":"CATHODE_CUSTOMER_INVENTORY_ADJUSTMENT_SKON_SAMSUNGSDI_ASP_MARGIN_GUARD","case_type":"failed_rerating","positive_or_counterexample":"counterexample","best_trigger":"TRG_R3L125_C12_247540_20240207_02","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"counterexample_customer_inventory_adjustment_low_MFE_deep_MAE","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"Customer inventory adjustment at SK On/Samsung SDI plus ASP pressure should block Stage2-Actionable/Yellow."}
{"row_type":"case","case_id":"R3L125-C12-003670-20240201-POSCOFUTUREM-RAWMATERIAL-PRICE-CUSTOMER-DEMAND","symbol":"003670","company_name":"POSCO Future M","round":"R3","loop":"125","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","fine_archetype_id":"CATHODE_CONTRACT_BASE_RAW_MATERIAL_PRICE_CUSTOMER_DEMAND_MARGIN_GUARD","case_type":"failed_rerating","positive_or_counterexample":"counterexample","best_trigger":"TRG_R3L125_C12_003670_20240201_03","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":0.6,"score_price_alignment":"counterexample_contract_base_not_enough_without_price_margin_recovery","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"Battery materials contract base is insufficient when ASP decline, inventory valuation loss and emergency-management language dominate."}
{"row_type":"case","case_id":"R3L125-C12-393890-20240216-WCP-SEPARATOR-STOCK-REBALANCING","symbol":"393890","company_name":"WCP","round":"R3","loop":"125","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","fine_archetype_id":"SEPARATOR_CLIENT_STOCK_REBALANCING_EUROPE_DEMAND_REDUCTION_HARD4C","case_type":"failed_rerating","positive_or_counterexample":"counterexample","best_trigger":"TRG_R3L125_C12_393890_20240216_04","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":0.7,"score_price_alignment":"hard_4c_candidate_client_stock_rebalancing_low_MFE_deep_MAE","current_profile_verdict":"current_profile_4C_too_late","price_source":"Songdaiki/stock-web","notes":"Reduced client demand and stock rebalancing are non-price hard-4C evidence; low MFE and deep MAE confirm the route."}
{"row_type":"case","case_id":"R3L125-C12-336370-20240201-SOLUS-CUSTOMER-DIVERSIFICATION-POSITIVE-WATCH","symbol":"336370","company_name":"Solus Advanced Materials","round":"R3","loop":"125","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","fine_archetype_id":"BATTERY_COPPER_FOIL_CUSTOMER_DIVERSIFICATION_SUPPLY_VOLUME_POSITIVE_WATCH","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"TRG_R3L125_C12_336370_20240201_05","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":0.6,"score_price_alignment":"positive_customer_diversification_with_controlled_MAE_source_repair_required","current_profile_verdict":"current_profile_correct","price_source":"Songdaiki/stock-web","notes":"Customer diversification and supply-volume bridge can remain Stage2-Actionable while Green waits for exact customer cadence and margin/cash proof."}
{"row_type":"case","case_id":"R3L125-C12-348370-20240125-ENCHEM-NORTH-AMERICA-CONTRACT-LOCAL4B-CORPACTION-BLOCKED","symbol":"348370","company_name":"Enchem","round":"R3","loop":"125","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","fine_archetype_id":"ELECTROLYTE_NORTH_AMERICA_TOP_TIER_CUSTOMER_CONTRACT_BLOWOFF_SHARECOUNT_GUARD","case_type":"narrative_only","positive_or_counterexample":"blocked_guardrail","best_trigger":"TRG_R3L125_C12_348370_20240125_06","calibration_usable":false,"is_new_independent_case":false,"reuse_reason":"blocked_guardrail_row_not_counted_for_aggregate","independent_evidence_weight":0.0,"score_price_alignment":"positive_price_path_but_share_count_contaminated_local4B_overlay","current_profile_verdict":"current_profile_4B_too_late","price_source":"Songdaiki/stock-web","notes":"Named customer contracts produced blowoff-style MFE, but share-count change and lifecycle risk make it a blocked local-4B audit row."}
{"row_type":"case","case_id":"R3L125-C12-066970-20230228-LNF-TESLA-CONTRACT-LATER-CALLOFF-CORPACTION-BLOCKED","symbol":"066970","company_name":"L&F","round":"R3","loop":"125","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","fine_archetype_id":"TESLA_HIGH_NICKEL_CATHODE_CONTRACT_LATER_CALLOFF_REVERSAL_GUARD","case_type":"narrative_only","positive_or_counterexample":"counterexample","best_trigger":"TRG_R3L125_C12_066970_20230228_07","calibration_usable":false,"is_new_independent_case":false,"reuse_reason":"blocked_guardrail_row_not_counted_for_aggregate","independent_evidence_weight":0.0,"score_price_alignment":"contract_headline_later_calloff_reversal_sharecount_contaminated","current_profile_verdict":"current_profile_4C_too_late","price_source":"Songdaiki/stock-web","notes":"Large named-customer contract should carry explicit call-off/reduction risk; later Tesla reduction validates the guardrail, but the row is blocked for aggregate."}
```

### 25.3 trigger rows
```jsonl
{"row_type":"trigger","trigger_id":"TRG_R3L125_C12_373220_20240126_01","case_id":"R3L125-C12-373220-20240126-LGES-DEMAND-SLOWDOWN-CALLOFF-WATCH","symbol":"373220","company_name":"LG Energy Solution","round":"R3","loop":"125","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","fine_archetype_id":"LGES_OEM_INVENTORY_CONTROL_EV_DEMAND_SLOWDOWN_CAPEX_PRIORITY_GUARD","sector":"battery / EV materials / customer contract call-off risk","primary_archetype":"customer_contract_to_calloff_demand_risk","loop_objective":"coverage_gap_fill|counterexample_mining|4C_thesis_break_timing_test|stage2_actionable_bonus_stress_test|canonical_archetype_compression|sector_specific_rule_discovery","trigger_type":"Stage2","trigger_date":"2024-01-26","evidence_available_at_that_date":"LGES forecast temporary slowdown in global EV battery demand due to OEM conservative inventory control and metal price decline; Q1 showed utilization adjustment and demand weakening.","evidence_source":"https://www.reuters.com/business/battery-firm-lg-energy-solutions-q4-profit-up-43-higher-us-output-2024-01-26/; https://inside.lgensol.com/en/2024/04/lg-energy-solution-makes-progress-amid-market-uncertainties-aims-to-strengthen-fundamental-competitiveness-this-year/","stage2_evidence_fields":["named_OEM_customer_base","inventory_control_or_calloff_risk","capex_priority_adjustment"],"stage3_evidence_fields":["customer_launch_shipments_partial","ESS_offset_partial"],"stage4b_evidence_fields":["utilization_adjustment","ASP_metal_price_pressure","weak_90D_asymmetry"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/373/373220/2024.csv","profile_path":"atlas/symbol_profiles/373/373220.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-01-26","entry_price":381000.0,"entry_price_type":"tradable_close","MFE_30D_pct":10.24,"MFE_90D_pct":10.76,"MFE_180D_pct":16.54,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-4.99,"MAE_90D_pct":-14.44,"MAE_180D_pct":-18.37,"MAE_1Y_pct":null,"MAE_2Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-10-08","peak_price":444000.0,"trough_date":"2024-08-05","trough_price":311000.0,"drawdown_after_peak_pct":null,"green_lateness_ratio":"not_applicable_no_confirmed_Stage3_Green_trigger","four_b_local_peak_proximity":"local_4B_if_large_MFE_without_fresh_customer_calloff_or_margin_refresh","four_b_full_window_peak_proximity":"full_4B_requires_non_price_customer_schedule_cut_capacity_delay_inventory_or_contract_break","four_b_timing_verdict":"separate_price_spike_from_customer_contract_quality","four_b_evidence_type":["customer_contract_quality","calloff_or_inventory_risk","price_path_asymmetry"],"four_c_protection_label":"hard_4C_only_after_customer_demand_contract_or_utilization_break_not_price_only","trigger_outcome_label":"counterexample_moderate_MFE_high_MAE_demand_slowdown_guard","case_polarity":"counterexample","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window_by_local_tradable_rows_share_count_constant","share_count_change_inside_window":false,"same_entry_group_id":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK|373220|Stage2|2024-01-26","dedupe_key":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK|373220|Stage2|2024-01-26","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"source_proxy_only":false,"evidence_url_pending":false,"batch_reverification_required":false,"current_profile_verdict_detail":"Customer base and OEM inventory control evidence justify Stage2-Watch, but Actionable/Yellow should be blocked until utilization and call-off recovery are visible."}
{"row_type":"trigger","trigger_id":"TRG_R3L125_C12_247540_20240207_02","case_id":"R3L125-C12-247540-20240207-ECOPROBM-CUSTOMER-INVENTORY-ADJUSTMENT","symbol":"247540","company_name":"EcoPro BM","round":"R3","loop":"125","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","fine_archetype_id":"CATHODE_CUSTOMER_INVENTORY_ADJUSTMENT_SKON_SAMSUNGSDI_ASP_MARGIN_GUARD","sector":"battery / EV materials / customer contract call-off risk","primary_archetype":"customer_contract_to_calloff_demand_risk","loop_objective":"coverage_gap_fill|counterexample_mining|4C_thesis_break_timing_test|stage2_actionable_bonus_stress_test|canonical_archetype_compression|sector_specific_rule_discovery","trigger_type":"Stage2","trigger_date":"2024-02-07","evidence_available_at_that_date":"EcoPro BM earnings path was pressured by inventory adjustments at SK On and Samsung SDI and cathode ASP decline; later Q3 results confirmed revenue decline and operating loss.","evidence_source":"https://securities.miraeasset.com/bbs/download/2126480.pdf?attachmentId=2126480; https://www.asiae.co.kr/en/article/2024110110191994466","stage2_evidence_fields":["major_customer_inventory_adjustment","cathode_supply_chain_contract_base"],"stage3_evidence_fields":["potential_3Q24_recovery_not_yet_confirmed"],"stage4b_evidence_fields":["ASP_decline","inventory_valuation_loss","MAE90_below_minus20"],"stage4c_evidence_fields":["operating_loss_if_customer_inventory_adjustment_persists"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/247/247540/2024.csv","profile_path":"atlas/symbol_profiles/247/247540.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-02-07","entry_price":230500.0,"entry_price_type":"tradable_close","MFE_30D_pct":21.69,"MFE_90D_pct":29.5,"MFE_180D_pct":29.5,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-2.17,"MAE_90D_pct":-21.26,"MAE_180D_pct":-35.49,"MAE_1Y_pct":null,"MAE_2Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-03-27","peak_price":298500.0,"trough_date":"2024-09-10","trough_price":148700.0,"drawdown_after_peak_pct":null,"green_lateness_ratio":"not_applicable_no_confirmed_Stage3_Green_trigger","four_b_local_peak_proximity":"local_4B_if_large_MFE_without_fresh_customer_calloff_or_margin_refresh","four_b_full_window_peak_proximity":"full_4B_requires_non_price_customer_schedule_cut_capacity_delay_inventory_or_contract_break","four_b_timing_verdict":"separate_price_spike_from_customer_contract_quality","four_b_evidence_type":["customer_contract_quality","calloff_or_inventory_risk","price_path_asymmetry"],"four_c_protection_label":"hard_4C_only_after_customer_demand_contract_or_utilization_break_not_price_only","trigger_outcome_label":"counterexample_customer_inventory_adjustment_low_MFE_deep_MAE","case_polarity":"counterexample","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window_by_local_tradable_rows_share_count_constant","share_count_change_inside_window":false,"same_entry_group_id":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK|247540|Stage2|2024-02-07","dedupe_key":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK|247540|Stage2|2024-02-07","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"source_proxy_only":false,"evidence_url_pending":false,"batch_reverification_required":false,"current_profile_verdict_detail":"Customer inventory adjustment at SK On/Samsung SDI plus ASP pressure should block Stage2-Actionable/Yellow."}
{"row_type":"trigger","trigger_id":"TRG_R3L125_C12_003670_20240201_03","case_id":"R3L125-C12-003670-20240201-POSCOFUTUREM-RAWMATERIAL-PRICE-CUSTOMER-DEMAND","symbol":"003670","company_name":"POSCO Future M","round":"R3","loop":"125","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","fine_archetype_id":"CATHODE_CONTRACT_BASE_RAW_MATERIAL_PRICE_CUSTOMER_DEMAND_MARGIN_GUARD","sector":"battery / EV materials / customer contract call-off risk","primary_archetype":"customer_contract_to_calloff_demand_risk","loop_objective":"coverage_gap_fill|counterexample_mining|4C_thesis_break_timing_test|stage2_actionable_bonus_stress_test|canonical_archetype_compression|sector_specific_rule_discovery","trigger_type":"Stage2","trigger_date":"2024-02-01","evidence_available_at_that_date":"2024 full-year result later showed revenue/profitability declined due to cathode price decreases, inventory valuation losses, and an emergency management response to post-chasm conditions.","evidence_source":"https://www.poscofuturem.com/en/pr/view.do?num=899","stage2_evidence_fields":["battery_materials_contract_base","high_nickel_product_mix"],"stage3_evidence_fields":["new_EV_model_supply_partial"],"stage4b_evidence_fields":["raw_material_price_decline","inventory_valuation_loss","MAE180_below_minus20"],"stage4c_evidence_fields":["margin_collapse_if_customer_demand_and_ASP_do_not_recover"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/003/003670/2024.csv","profile_path":"atlas/symbol_profiles/003/003670.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-02-01","entry_price":260000.0,"entry_price_type":"tradable_close","MFE_30D_pct":31.15,"MFE_90D_pct":31.15,"MFE_180D_pct":31.15,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-7.5,"MAE_90D_pct":-7.5,"MAE_180D_pct":-24.81,"MAE_1Y_pct":null,"MAE_2Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-03-13","peak_price":341000.0,"trough_date":"2024-08-05","trough_price":195500.0,"drawdown_after_peak_pct":null,"green_lateness_ratio":"not_applicable_no_confirmed_Stage3_Green_trigger","four_b_local_peak_proximity":"local_4B_if_large_MFE_without_fresh_customer_calloff_or_margin_refresh","four_b_full_window_peak_proximity":"full_4B_requires_non_price_customer_schedule_cut_capacity_delay_inventory_or_contract_break","four_b_timing_verdict":"separate_price_spike_from_customer_contract_quality","four_b_evidence_type":["customer_contract_quality","calloff_or_inventory_risk","price_path_asymmetry"],"four_c_protection_label":"hard_4C_only_after_customer_demand_contract_or_utilization_break_not_price_only","trigger_outcome_label":"counterexample_contract_base_not_enough_without_price_margin_recovery","case_polarity":"counterexample","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window_by_local_tradable_rows_share_count_constant","share_count_change_inside_window":false,"same_entry_group_id":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK|003670|Stage2|2024-02-01","dedupe_key":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK|003670|Stage2|2024-02-01","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":0.6,"do_not_count_as_new_case":false,"source_proxy_only":true,"evidence_url_pending":false,"batch_reverification_required":true,"current_profile_verdict_detail":"Battery materials contract base is insufficient when ASP decline, inventory valuation loss and emergency-management language dominate."}
{"row_type":"trigger","trigger_id":"TRG_R3L125_C12_393890_20240216_04","case_id":"R3L125-C12-393890-20240216-WCP-SEPARATOR-STOCK-REBALANCING","symbol":"393890","company_name":"WCP","round":"R3","loop":"125","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","fine_archetype_id":"SEPARATOR_CLIENT_STOCK_REBALANCING_EUROPE_DEMAND_REDUCTION_HARD4C","sector":"battery / EV materials / customer contract call-off risk","primary_archetype":"customer_contract_to_calloff_demand_risk","loop_objective":"coverage_gap_fill|counterexample_mining|4C_thesis_break_timing_test|stage2_actionable_bonus_stress_test|canonical_archetype_compression|sector_specific_rule_discovery","trigger_type":"Stage4C","trigger_date":"2024-02-16","evidence_available_at_that_date":"Separator makers including WCP later showed shipment stagnation due to reduced European customer demand and client stock rebalancing, matching the 2024 price-path failure mode.","evidence_source":"https://www.sneresearch.com/en/insight/release_view/433/page/96?s_cat=%7C1%7C&s_keyword=","stage2_evidence_fields":["separator_customer_contract_base"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["low_MFE","MAE90_below_minus30","client_stock_rebalancing"],"stage4c_evidence_fields":["reduced_client_demand_and_shipment_stagnation"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/393/393890/2024.csv","profile_path":"atlas/symbol_profiles/393/393890.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-02-16","entry_price":42000.0,"entry_price_type":"tradable_close","MFE_30D_pct":17.86,"MFE_90D_pct":17.86,"MFE_180D_pct":17.86,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-6.43,"MAE_90D_pct":-30.24,"MAE_180D_pct":-66.24,"MAE_1Y_pct":null,"MAE_2Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-03-07","peak_price":49500.0,"trough_date":"2024-11-12","trough_price":14180.0,"drawdown_after_peak_pct":null,"green_lateness_ratio":"not_applicable_no_confirmed_Stage3_Green_trigger","four_b_local_peak_proximity":"local_4B_if_large_MFE_without_fresh_customer_calloff_or_margin_refresh","four_b_full_window_peak_proximity":"full_4B_requires_non_price_customer_schedule_cut_capacity_delay_inventory_or_contract_break","four_b_timing_verdict":"separate_price_spike_from_customer_contract_quality","four_b_evidence_type":["customer_contract_quality","calloff_or_inventory_risk","price_path_asymmetry"],"four_c_protection_label":"hard_4C_only_after_customer_demand_contract_or_utilization_break_not_price_only","trigger_outcome_label":"hard_4c_candidate_client_stock_rebalancing_low_MFE_deep_MAE","case_polarity":"counterexample","current_profile_verdict":"current_profile_4C_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window_by_local_tradable_rows_share_count_constant","share_count_change_inside_window":false,"same_entry_group_id":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK|393890|Stage4C|2024-02-16","dedupe_key":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK|393890|Stage4C|2024-02-16","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":0.7,"do_not_count_as_new_case":false,"source_proxy_only":true,"evidence_url_pending":false,"batch_reverification_required":true,"current_profile_verdict_detail":"Reduced client demand and stock rebalancing are non-price hard-4C evidence; low MFE and deep MAE confirm the route."}
{"row_type":"trigger","trigger_id":"TRG_R3L125_C12_336370_20240201_05","case_id":"R3L125-C12-336370-20240201-SOLUS-CUSTOMER-DIVERSIFICATION-POSITIVE-WATCH","symbol":"336370","company_name":"Solus Advanced Materials","round":"R3","loop":"125","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","fine_archetype_id":"BATTERY_COPPER_FOIL_CUSTOMER_DIVERSIFICATION_SUPPLY_VOLUME_POSITIVE_WATCH","sector":"battery / EV materials / customer contract call-off risk","primary_archetype":"customer_contract_to_calloff_demand_risk","loop_objective":"coverage_gap_fill|counterexample_mining|4C_thesis_break_timing_test|stage2_actionable_bonus_stress_test|canonical_archetype_compression|sector_specific_rule_discovery","trigger_type":"Stage2-Actionable","trigger_date":"2024-02-01","evidence_available_at_that_date":"Solus described maintained partnerships and new supply agreements with global top-ten battery cell and OEM customers; separate 2024 supply-volume disclosures support a customer-diversification bridge but exact as-of trigger requires source repair.","evidence_source":"https://www.solusadvancedmaterials.com/en/ir/shareholder-letter/; https://www.miningstockeducation.com/2024/06/solus-advanced-materials-significantly-increases-its-supply-of-battery-copper-foil-to-north-american-customers-expanding-influence-in-the-global-market/","stage2_evidence_fields":["customer_diversification","battery_copper_foil_supply_growth","top_ten_customer_base"],"stage3_evidence_fields":["controlled_MAE","supply_volume_increase"],"stage4b_evidence_fields":["source_repair_required","proof_of_mass_production_timing_required"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/336/336370/2024.csv","profile_path":"atlas/symbol_profiles/336/336370.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-02-01","entry_price":11160.0,"entry_price_type":"tradable_close","MFE_30D_pct":24.82,"MFE_90D_pct":94.44,"MFE_180D_pct":110.57,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-1.34,"MAE_90D_pct":-1.34,"MAE_180D_pct":-1.34,"MAE_1Y_pct":null,"MAE_2Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-07-01","peak_price":23500.0,"trough_date":"2024-02-01","trough_price":11010.0,"drawdown_after_peak_pct":null,"green_lateness_ratio":"not_applicable_no_confirmed_Stage3_Green_trigger","four_b_local_peak_proximity":"local_4B_if_large_MFE_without_fresh_customer_calloff_or_margin_refresh","four_b_full_window_peak_proximity":"full_4B_requires_non_price_customer_schedule_cut_capacity_delay_inventory_or_contract_break","four_b_timing_verdict":"separate_price_spike_from_customer_contract_quality","four_b_evidence_type":["customer_contract_quality","calloff_or_inventory_risk","price_path_asymmetry"],"four_c_protection_label":"hard_4C_only_after_customer_demand_contract_or_utilization_break_not_price_only","trigger_outcome_label":"positive_customer_diversification_with_controlled_MAE_source_repair_required","case_polarity":"positive","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window_by_local_tradable_rows_share_count_constant","share_count_change_inside_window":false,"same_entry_group_id":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK|336370|Stage2-Actionable|2024-02-01","dedupe_key":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK|336370|Stage2-Actionable|2024-02-01","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":0.6,"do_not_count_as_new_case":false,"source_proxy_only":true,"evidence_url_pending":false,"batch_reverification_required":true,"current_profile_verdict_detail":"Customer diversification and supply-volume bridge can remain Stage2-Actionable while Green waits for exact customer cadence and margin/cash proof."}
```

### 25.4 score_simulation rows
```jsonl
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy_to_C12_shadow_guard","case_id":"R3L125-C12-373220-20240126-LGES-DEMAND-SLOWDOWN-CALLOFF-WATCH","trigger_id":"TRG_R3L125_C12_373220_20240126_01","symbol":"373220","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","raw_component_scores_before":{"contract_score":18,"backlog_visibility_score":6,"margin_bridge_score":6,"revision_score":4,"relative_strength_score":3.41,"customer_quality_score":14,"policy_or_regulatory_score":0,"valuation_repricing_score":1.34,"execution_risk_score":4,"legal_or_contract_risk_score":8,"dilution_cb_risk_score":10,"accounting_trust_risk_score":9},"weighted_score_before":65.33,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"contract_score":12,"backlog_visibility_score":6,"margin_bridge_score":2,"revision_score":1,"relative_strength_score":3.41,"customer_quality_score":14,"policy_or_regulatory_score":0,"valuation_repricing_score":0,"execution_risk_score":0,"legal_or_contract_risk_score":3,"dilution_cb_risk_score":10,"accounting_trust_risk_score":9},"weighted_score_after":47.12,"stage_label_after":"Stage2","changed_components":["contract_score","margin_bridge_score","revision_score","execution_risk_score","legal_or_contract_risk_score","valuation_repricing_score"],"component_delta_explanation":"C12 shadow guard discounts headline customer contracts when inventory adjustment, stock rebalancing, utilization cut, ASP decline, call-off risk or later contract reduction appears; it allows Stage2-Actionable only when demand/call-off survival and margin/cash bridge are visible.","MFE_90D_pct":10.76,"MAE_90D_pct":-14.44,"score_return_alignment_label":"counterexample_moderate_MFE_high_MAE_demand_slowdown_guard","current_profile_verdict":"current_profile_false_positive","production_scoring_changed":false}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy_to_C12_shadow_guard","case_id":"R3L125-C12-247540-20240207-ECOPROBM-CUSTOMER-INVENTORY-ADJUSTMENT","trigger_id":"TRG_R3L125_C12_247540_20240207_02","symbol":"247540","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","raw_component_scores_before":{"contract_score":18,"backlog_visibility_score":6,"margin_bridge_score":6,"revision_score":4,"relative_strength_score":7.23,"customer_quality_score":14,"policy_or_regulatory_score":0,"valuation_repricing_score":3.69,"execution_risk_score":4,"legal_or_contract_risk_score":2,"dilution_cb_risk_score":10,"accounting_trust_risk_score":9},"weighted_score_before":65.46,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"contract_score":12,"backlog_visibility_score":6,"margin_bridge_score":2,"revision_score":1,"relative_strength_score":7.23,"customer_quality_score":14,"policy_or_regulatory_score":0,"valuation_repricing_score":0.69,"execution_risk_score":0,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":10,"accounting_trust_risk_score":9},"weighted_score_after":48.3,"stage_label_after":"Stage2","changed_components":["contract_score","margin_bridge_score","revision_score","execution_risk_score","legal_or_contract_risk_score","valuation_repricing_score"],"component_delta_explanation":"C12 shadow guard discounts headline customer contracts when inventory adjustment, stock rebalancing, utilization cut, ASP decline, call-off risk or later contract reduction appears; it allows Stage2-Actionable only when demand/call-off survival and margin/cash bridge are visible.","MFE_90D_pct":29.5,"MAE_90D_pct":-21.26,"score_return_alignment_label":"counterexample_customer_inventory_adjustment_low_MFE_deep_MAE","current_profile_verdict":"current_profile_false_positive","production_scoring_changed":false}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy_to_C12_shadow_guard","case_id":"R3L125-C12-003670-20240201-POSCOFUTUREM-RAWMATERIAL-PRICE-CUSTOMER-DEMAND","trigger_id":"TRG_R3L125_C12_003670_20240201_03","symbol":"003670","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","raw_component_scores_before":{"contract_score":18,"backlog_visibility_score":6,"margin_bridge_score":6,"revision_score":4,"relative_strength_score":10.38,"customer_quality_score":8,"policy_or_regulatory_score":0,"valuation_repricing_score":3.89,"execution_risk_score":4,"legal_or_contract_risk_score":2,"dilution_cb_risk_score":10,"accounting_trust_risk_score":9},"weighted_score_before":63.39,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"contract_score":12,"backlog_visibility_score":6,"margin_bridge_score":2,"revision_score":1,"relative_strength_score":10.38,"customer_quality_score":8,"policy_or_regulatory_score":0,"valuation_repricing_score":0.8900000000000001,"execution_risk_score":0,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":10,"accounting_trust_risk_score":9},"weighted_score_after":46.23,"stage_label_after":"Stage2","changed_components":["contract_score","margin_bridge_score","revision_score","execution_risk_score","legal_or_contract_risk_score","valuation_repricing_score"],"component_delta_explanation":"C12 shadow guard discounts headline customer contracts when inventory adjustment, stock rebalancing, utilization cut, ASP decline, call-off risk or later contract reduction appears; it allows Stage2-Actionable only when demand/call-off survival and margin/cash bridge are visible.","MFE_90D_pct":31.15,"MAE_90D_pct":-7.5,"score_return_alignment_label":"counterexample_contract_base_not_enough_without_price_margin_recovery","current_profile_verdict":"current_profile_false_positive","production_scoring_changed":false}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy_to_C12_shadow_guard","case_id":"R3L125-C12-393890-20240216-WCP-SEPARATOR-STOCK-REBALANCING","trigger_id":"TRG_R3L125_C12_393890_20240216_04","symbol":"393890","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","raw_component_scores_before":{"contract_score":18,"backlog_visibility_score":6,"margin_bridge_score":1,"revision_score":0,"relative_strength_score":5.95,"customer_quality_score":14,"policy_or_regulatory_score":0,"valuation_repricing_score":2.23,"execution_risk_score":4,"legal_or_contract_risk_score":2,"dilution_cb_risk_score":10,"accounting_trust_risk_score":9},"weighted_score_before":56.3,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"contract_score":12,"backlog_visibility_score":6,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":5.95,"customer_quality_score":14,"policy_or_regulatory_score":0,"valuation_repricing_score":0,"execution_risk_score":0,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":10,"accounting_trust_risk_score":9},"weighted_score_after":44.42,"stage_label_after":"Stage2","changed_components":["contract_score","margin_bridge_score","revision_score","execution_risk_score","legal_or_contract_risk_score","valuation_repricing_score"],"component_delta_explanation":"C12 shadow guard discounts headline customer contracts when inventory adjustment, stock rebalancing, utilization cut, ASP decline, call-off risk or later contract reduction appears; it allows Stage2-Actionable only when demand/call-off survival and margin/cash bridge are visible.","MFE_90D_pct":17.86,"MAE_90D_pct":-30.24,"score_return_alignment_label":"hard_4c_candidate_client_stock_rebalancing_low_MFE_deep_MAE","current_profile_verdict":"current_profile_4C_too_late","production_scoring_changed":false}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy_to_C12_shadow_guard","case_id":"R3L125-C12-336370-20240201-SOLUS-CUSTOMER-DIVERSIFICATION-POSITIVE-WATCH","trigger_id":"TRG_R3L125_C12_336370_20240201_05","symbol":"336370","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","raw_component_scores_before":{"contract_score":18,"backlog_visibility_score":6,"margin_bridge_score":6,"revision_score":4,"relative_strength_score":8.27,"customer_quality_score":14,"policy_or_regulatory_score":0,"valuation_repricing_score":11.8,"execution_risk_score":4,"legal_or_contract_risk_score":8,"dilution_cb_risk_score":10,"accounting_trust_risk_score":9},"weighted_score_before":77.27,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":18,"backlog_visibility_score":6,"margin_bridge_score":10,"revision_score":4,"relative_strength_score":8.27,"customer_quality_score":16,"policy_or_regulatory_score":0,"valuation_repricing_score":11.8,"execution_risk_score":5,"legal_or_contract_risk_score":8,"dilution_cb_risk_score":10,"accounting_trust_risk_score":9},"weighted_score_after":82.73,"stage_label_after":"Stage3-Yellow","changed_components":["contract_score","margin_bridge_score","revision_score","execution_risk_score","legal_or_contract_risk_score","valuation_repricing_score"],"component_delta_explanation":"C12 shadow guard discounts headline customer contracts when inventory adjustment, stock rebalancing, utilization cut, ASP decline, call-off risk or later contract reduction appears; it allows Stage2-Actionable only when demand/call-off survival and margin/cash bridge are visible.","MFE_90D_pct":94.44,"MAE_90D_pct":-1.34,"score_return_alignment_label":"positive_customer_diversification_with_controlled_MAE_source_repair_required","current_profile_verdict":"current_profile_correct","production_scoring_changed":false}
```

### 25.5 residual / aggregate / shadow rows
```jsonl
{"row_type":"aggregate","research_file":"e2r_stock_web_v12_residual_round_R3_loop_125_L3_BATTERY_EV_GREEN_MOBILITY_C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK_research.md","selected_round":"R3","selected_loop":125,"selection_basis":"docs/core/V12_Research_No_Repeat_Index.md; coverage-index-first; C12 selected after current-session Priority-0 continuation","selected_priority_bucket":"Priority 1 / under_50_rows_static_ledger / C12 rows 32 need_to_50 18 before this local loop","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","fine_archetype_id":"BATTERY_CUSTOMER_CONTRACT_CALLOFF_DEMAND_RISK_VS_CONTRACT_HEADLINE","trigger_rows_total":5,"calibration_usable_trigger_count":5,"representative_trigger_count":5,"narrative_only_or_rejected_count":2,"new_independent_case_count":5,"reused_case_count":0,"same_archetype_new_symbol_count":7,"new_symbol_count":7,"same_archetype_new_trigger_family_count":7,"new_trigger_family_count":7,"positive_case_count":1,"counterexample_count":4,"stage4b_overlay_count":7,"stage4c_case_count":4,"current_profile_error_count":6,"avg_MFE_30D_pct":21.15,"avg_MAE_30D_pct":-4.49,"avg_MFE_90D_pct":36.74,"avg_MAE_90D_pct":-14.96,"avg_MFE_180D_pct":41.12,"avg_MAE_180D_pct":-29.25,"diversity_score_summary":"7 symbols, 7 trigger families, 5 aggregate-usable rows, 2 narrative-only share-count/corporate-action guardrail rows; hard_duplicate=0; new_independent_ratio=1.00 for usable triggers","production_scoring_changed":false,"shadow_weight_only":true}
{"row_type":"shadow_rule_candidate","round":"R3","loop":125,"large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","rule_id":"C12_CUSTOMER_CONTRACT_REQUIRES_CALLOFF_AND_DEMAND_SURVIVAL_GATE","rule_scope":"canonical_archetype_specific","rule_text":"For C12, do not promote a named battery customer contract above Stage2-Watch or weak Stage2-Actionable unless call-off cadence, customer production schedule, utilization, ASP/metal pass-through, shipment recovery, margin/cash conversion and low-MAE survival are visible. If customer inventory adjustment, stock rebalancing, utilization adjustment or contract reduction appears, route to Stage4B-watch or hard Stage4C depending on non-price severity.","support_trigger_ids":["TRG_R3L125_C12_373220_20240126_01","TRG_R3L125_C12_247540_20240207_02","TRG_R3L125_C12_003670_20240201_03","TRG_R3L125_C12_393890_20240216_04","TRG_R3L125_C12_336370_20240201_05"],"narrative_guardrail_symbols":["348370","066970"],"candidate_delta":"tighten C12 Stage2-Actionable/Yellow gate; strengthen hard-4C routing where customer call-off, stock rebalancing or contract reduction is explicit; keep AMPC/IRA subsidy economics separate from demand survival","apply_now":false,"shadow_only":true,"production_scoring_changed":false}
{"row_type":"residual_contribution","round":"R3","loop":"125","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","new_independent_case_count":5,"reused_case_count":0,"new_symbol_count":7,"new_trigger_family_count":7,"tested_existing_calibrated_axes":["stage2_actionable_evidence_bonus","price_only_blowoff_blocks_positive_stage","full_4b_requires_non_price_evidence","hard_4c_thesis_break_routes_to_4c"],"residual_error_types_found":["battery_customer_contract_headline_overcredit","customer_inventory_adjustment_false_positive","client_stock_rebalancing_hard4c_late","contract_reduction_calloff_risk_guardrail"],"loop_contribution_label":"canonical_archetype_rule_candidate","do_not_propose_new_weight_delta":false,"new_axis_proposed":"C12_CUSTOMER_CONTRACT_REQUIRES_CALLOFF_AND_DEMAND_SURVIVAL_GATE","existing_axis_strengthened":["stage2_required_bridge","full_4b_requires_non_price_evidence","hard_4c_thesis_break_routes_to_4c"],"existing_axis_weakened":null}
```

### 25.6 narrative_only rows
```jsonl
{"row_type":"narrative_only","case_id":"R3L125-C12-348370-20240125-ENCHEM-NORTH-AMERICA-CONTRACT-LOCAL4B-CORPACTION-BLOCKED","symbol":"348370","company_name":"Enchem","round":"R3","loop":"125","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","fine_archetype_id":"ELECTROLYTE_NORTH_AMERICA_TOP_TIER_CUSTOMER_CONTRACT_BLOWOFF_SHARECOUNT_GUARD","reason":"corporate_action_or_share_count_change_inside_180D_window_reverify_before_weight_calibration","price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","entry_date":"2024-01-25","entry_price":113600.0,"MFE_30D_pct":215.58,"MFE_90D_pct":247.27,"MFE_180D_pct":247.27,"MAE_30D_pct":-5.55,"MAE_90D_pct":-5.55,"MAE_180D_pct":-5.55,"calibration_usable":false,"calibration_block_reasons":["share_count_change_inside_180D_window_batch_reverification_required"],"usage":"guardrail_narrative_only_not_weight_calibration","current_profile_verdict":"current_profile_4B_too_late","current_profile_verdict_detail":"Named customer contracts produced blowoff-style MFE, but share-count change and lifecycle risk make it a blocked local-4B audit row.","evidence_source":"https://www.asiae.co.kr/en/article/2024012508342937399","stage4b_evidence_fields":["valuation_blowoff","share_count_change_inside_window"],"stage4c_evidence_fields":[]}
{"row_type":"narrative_only","case_id":"R3L125-C12-066970-20230228-LNF-TESLA-CONTRACT-LATER-CALLOFF-CORPACTION-BLOCKED","symbol":"066970","company_name":"L&F","round":"R3","loop":"125","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","fine_archetype_id":"TESLA_HIGH_NICKEL_CATHODE_CONTRACT_LATER_CALLOFF_REVERSAL_GUARD","reason":"corporate_action_or_share_count_change_inside_180D_window_reverify_before_weight_calibration","price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","entry_date":"2023-02-28","entry_price":262000.0,"MFE_30D_pct":33.4,"MFE_90D_pct":33.4,"MFE_180D_pct":33.4,"MAE_30D_pct":-16.41,"MAE_90D_pct":-16.41,"MAE_180D_pct":-51.18,"calibration_usable":false,"calibration_block_reasons":["share_count_change_inside_180D_window_batch_reverification_required"],"usage":"guardrail_narrative_only_not_weight_calibration","current_profile_verdict":"current_profile_4C_too_late","current_profile_verdict_detail":"Large named-customer contract should carry explicit call-off/reduction risk; later Tesla reduction validates the guardrail, but the row is blocked for aggregate.","evidence_source":"https://www.kedglobal.com/batteries/newsView/ked202302280017; https://www.asiae.co.kr/en/article/2025122918185667860","stage4b_evidence_fields":["large_contract_size_but_calloff_risk","share_count_change_inside_window"],"stage4c_evidence_fields":["later_contract_reduction_validates_calloff_risk"]}
```

## Batch Ingest Self-Audit

```yaml
expected_v12_result_file: true
filename_pattern_pass: true
metadata_filename_consistency: pass
jsonl_trigger_row_count: 5
calibration_usable_trigger_count: 5
representative_trigger_count: 5
new_weight_evidence_candidate_count: 5
guardrail_candidate_count: 2
narrative_only_or_rejected_count: 2
rows_missing_required_mfe_mae: 0
rows_missing_entry_price_or_date: 0
rows_with_noncanonical_trigger_type: 0
rows_with_compact_mfe_mae_alias_only: 0
ready_for_batch_ingest: true
```

## 26. Deferred Coding Agent Handoff Prompt

```md
### Purpose
You are now in the repository implementation phase. The attached Markdown files are v12 post-calibrated residual research outputs produced using the Songdaiki/stock-web OHLC atlas. These MDs are not live candidate research. They are historical calibration research designed to extend the already-applied e2r_2_1_stock_web_calibrated profile. Do not blindly apply every shadow row. Ingest the machine-readable rows and update the sector/canonical-archetype calibration ledger.

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
- Enchem and L&F are narrative-only until corporate-action/share-count verification is repaired.

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
```

## 27. Next Round State

```yaml
completed_round: R3
completed_loop: 125
selection_basis: docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket: Priority 1 / under_50_rows_static_ledger
round_schedule_status: coverage_index_selected
round_sector_consistency: pass
next_recommended_archetypes:
  - C05_EPC_MEGA_CONTRACT_MARGIN_GAP
  - C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION
  - C27_CONTENT_IP_GLOBAL_MONETIZATION
  - C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK_followup_to_50
  - C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY_quality_repair
```

## 28. Source Notes

- Scheduler / rules source: `docs/core/e2r_v12_prompt_round_scheduler_corrected.txt`.
- Duplicate ledger source: `docs/core/V12_Research_No_Repeat_Index.md`.
- Price source: `Songdaiki/stock-web` manifest `atlas/manifest.json`, `tradable_raw`, `raw_unadjusted_marcap`, max_date 2026-02-20.
- External evidence URLs are stored in each case row and trigger row. Some sources are explicitly marked source_proxy_only or narrative-only, and those rows are not promoted directly.