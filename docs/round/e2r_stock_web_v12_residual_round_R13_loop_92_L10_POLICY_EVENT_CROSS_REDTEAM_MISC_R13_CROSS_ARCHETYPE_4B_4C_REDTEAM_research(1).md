# E2R Stock-Web v12 Residual Research — R13 Loop 92 / Cross-Archetype 4B·4C Redteam

```yaml
schema_family: v12_sector_archetype_residual
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
round: R13
loop: 92
large_sector_id: L10_POLICY_EVENT_CROSS_REDTEAM_MISC
canonical_archetype_id: R13_CROSS_ARCHETYPE_4B_4C_REDTEAM
fine_archetype_id: LOOP92_BRIDGE_PRESENT_POSITIVE_VS_WEAK_BRIDGE_PRICE_MFE_LATE_SPIKE_DATA_QUALITY_HARD_4C_GUARD
sector: cross-sector / 4B / 4C / bridge-missing / price-MFE / false-overblock / late-spike / data-quality / Green strictness
output_file: e2r_stock_web_v12_residual_round_R13_loop_92_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_R13_CROSS_ARCHETYPE_4B_4C_REDTEAM_research.md
production_scoring_changed: false
shadow_weight_only: true
stock_agent_code_accessed: false
handoff_prompt_embedded: true
handoff_prompt_executed_now: false
new_independent_case_count: 0
do_not_count_as_new_case: true
do_not_propose_new_weight_delta: true
```

## 1. Scope lock

This run follows the v12 sequential scheduler after completed `R12 loop 92`.

```text
scheduled_round = R13
scheduled_loop = 92
large_sector_id = L10_POLICY_EVENT_CROSS_REDTEAM_MISC
canonical_archetype_id = R13_CROSS_ARCHETYPE_4B_4C_REDTEAM
```

R13 is not a fresh symbol-mining round.
It is a cross-archetype redteam checkpoint that reviews the 36 trigger rows produced by R1~R12 loop92.

All R13 review rows are locked as:

```text
new_independent_case_count = 0
r13_do_not_count_as_new_case = true
independent_evidence_weight = 0.0
do_not_propose_new_weight_delta = true
production_scoring_changed = false
shadow_weight_only = true
```

No-Repeat Index reminder:

```text
R13_CROSS_ARCHETYPE_4B_4C_REDTEAM is a review archetype.
This run does not add independent cases to the registry; it adds a cross-check artifact only.
```

## 2. Price source and validation scope

The reviewed rows were already built from Songdaiki/stock-web 1D tradable raw OHLC shards.

```jsonl
{"row_type":"price_source_validation","round":"R13","loop":"92","source_name":"FinanceData/marcap via Songdaiki/stock-web","price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","manifest_min_date":"1995-05-02","manifest_max_date":"2026-02-20","tradable_row_count":14354401,"raw_row_count":15214118,"symbol_count":5414,"active_like_symbol_count":2868,"calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","validation_scope":"R13 reviews R1~R12 loop92 trigger rows; it does not create new price triggers."}
```

Reviewed files:

```text
- e2r_stock_web_v12_residual_round_R1_loop_92_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C02_POWER_GRID_DATACENTER_CAPEX_research.md
- e2r_stock_web_v12_residual_round_R2_loop_92_L2_AI_SEMICONDUCTOR_ELECTRONICS_C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY_research.md
- e2r_stock_web_v12_residual_round_R3_loop_92_L3_BATTERY_EV_GREEN_MOBILITY_C14_EV_DEMAND_SLOWDOWN_4B_4C_research.md
- e2r_stock_web_v12_residual_round_R4_loop_92_L4_MATERIALS_SPREAD_RESOURCE_C16_STRATEGIC_RESOURCE_POLICY_SUPPLY_research.md
- e2r_stock_web_v12_residual_round_R5_loop_92_L5_CONSUMER_BRAND_DISTRIBUTION_C18_CONSUMER_EXPORT_CHANNEL_REORDER_research.md
- e2r_stock_web_v12_residual_round_R6_loop_92_L6_FINANCIAL_CAPITAL_RETURN_DIGITAL_C22_INSURANCE_RATE_CYCLE_RESERVE_research.md
- e2r_stock_web_v12_residual_round_R7_loop_92_L7_BIO_HEALTHCARE_MEDICAL_C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT_research.md
- e2r_stock_web_v12_residual_round_R8_loop_92_L8_PLATFORM_CONTENT_SW_SECURITY_C28_SOFTWARE_SECURITY_CONTRACT_RETENTION_research.md
- e2r_stock_web_v12_residual_round_R9_loop_92_L3_BATTERY_EV_GREEN_MOBILITY_C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE_research.md
- e2r_stock_web_v12_residual_round_R10_loop_92_L9_CONSTRUCTION_REALESTATE_HOUSING_C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK_research.md
- e2r_stock_web_v12_residual_round_R11_loop_92_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C05_EPC_MEGA_CONTRACT_MARGIN_GAP_research.md
- e2r_stock_web_v12_residual_round_R12_loop_92_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP_research.md
```

## 3. Aggregate redteam statistics

```jsonl
{"row_type":"aggregate_metric","round":"R13","loop":"92","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_4B_4C_REDTEAM","review_trigger_count":36,"reviewed_source_file_count":12,"reviewed_original_round_count":12,"reviewed_original_canonical_count":12,"positive_bridge_count":11,"validated_4B_guard_count":2,"hard_4C_count":1,"false_overblock_override_count":1,"weak_bridge_or_spillover_counterexample_count":21,"counter_or_guard_review_count":25,"positive_avg_MFE90_pct":83.72,"positive_avg_MAE90_pct":-4.27,"positive_avg_MFE180_pct":98.62,"positive_avg_MAE180_pct":-11.03,"counter_guard_avg_MFE90_pct":25.58,"counter_guard_avg_MAE90_pct":-16.8,"counter_guard_avg_MFE180_pct":29.75,"counter_guard_avg_MAE180_pct":-30.02,"weak_counter_avg_MFE90_pct":14.25,"weak_counter_avg_MAE90_pct":-16.01,"weak_counter_avg_MFE180_pct":19.21,"weak_counter_avg_MAE180_pct":-28.94,"weak_counter_MFE90_lt20_count":18,"weak_counter_MFE90_ge20_count":3,"weak_counter_MAE90_le_minus20_count":6,"weak_counter_MAE180_le_minus25_count":14,"price_only_or_price_MFE_count":4,"late_spike_or_late_price_nonvalidation_count":5,"data_quality_watch_count":9,"source_proxy_only_count":36,"evidence_url_pending_count":36}
```

Interpretation:

```text
Bridge-present positive/positive-watch controls: 11.
Positive controls avg MFE90 83.72% / avg MAE90 -4.27%.
Positive controls avg MFE180 98.62% / avg MAE180 -11.03%.

Validated 4B risk guards: 2.
Hard 4C credit-event / hard-break rows: 1.
False-overblock override rows: 1.
Weak-bridge / spillover / price-MFE counterexamples: 21.

Weak-bridge counterexamples avg MFE90 14.25% / avg MAE90 -16.01%.
Weak-bridge counterexamples avg MFE180 19.21% / avg MAE180 -28.94%.

Weak-bridge counterexamples with MFE90 < 20: 18 / 21.
Weak-bridge counterexamples with MFE90 >= 20 but still not positive evidence: 3 / 21.
Weak-bridge counterexamples with MAE90 <= -20: 6 / 21.
Weak-bridge counterexamples with MAE180 <= -25: 14 / 21.

Price-only / price-MFE / spillover flags: 4.
Late-spike or late-price non-validation flags: 5.
Data-quality / listing / segment-change / inactive-like / future-candidate watch flags: 9.
source_proxy_only rows: 36.
evidence_url_pending rows: 36.
```

## 4. R13 research question

Across loop92, can the calibrated profile keep Yellow/Green closed when price action is loud but the non-price bridge is wrong, missing, late, cross-label, or data-quality contaminated?

The answer is directionally yes. The repeated error shape is stable across sectors:

```text
theme label without bridge
price MFE without direct company-specific cash path
late spike pretending to validate an old weak entry
hard 4B risk guard that should not be softened
hard 4C credit-event / PF-workout / liquidity-break row that must not be treated as bargain rebound
false-overblock case where broad risk vocabulary should be overridden by stronger customer-capacity/order bridge
data-quality repair before patching
Green-candidate rows that still require exact source-grade evidence
```

The same mechanism appears whether the surface story is grid/datacenter, semiconductor tester, EV demand slowdown, strategic resource policy, consumer export reorder, insurance reserve cycle, medical device reimbursement, software/security retention, mobility operating leverage, construction PF, EPC order margin, or governance tender premium.

Price is the spotlight. The bridge is the stage floor. If the floor is missing, the spotlight only makes the fall easier to see.

## 5. Cross-round case summary

```jsonl
{"row_type":"r13_loop92_cross_case","round":"R13","loop":"92","reviewed_round":"R1","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","reviewed_trigger_count":3,"positive_bridge_symbols":["267260"],"validated_4B_guard_symbols":[],"validated_4C_symbols":[],"false_overblock_symbols":[],"counterexample_symbols":["037030","237750"],"avg_positive_MFE90_pct":210.28,"avg_counter_or_guard_MFE90_pct":21.24,"avg_counter_or_guard_MAE180_pct":-39.19,"cross_redteam_verdict":"bridge_required_guard_passed; weak bridge, price-MFE, late-spike, data-quality and hard-4C rows remain Watch/4B/4C unless exact non-price bridge is repaired","r13_do_not_count_as_new_case":true,"independent_evidence_weight":0.0}
{"row_type":"r13_loop92_cross_case","round":"R13","loop":"92","reviewed_round":"R2","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY","reviewed_trigger_count":3,"positive_bridge_symbols":["092870"],"validated_4B_guard_symbols":[],"validated_4C_symbols":[],"false_overblock_symbols":[],"counterexample_symbols":["080580","237750"],"avg_positive_MFE90_pct":97.43,"avg_counter_or_guard_MFE90_pct":25.75,"avg_counter_or_guard_MAE180_pct":-49.5,"cross_redteam_verdict":"bridge_required_guard_passed; weak bridge, price-MFE, late-spike, data-quality and hard-4C rows remain Watch/4B/4C unless exact non-price bridge is repaired","r13_do_not_count_as_new_case":true,"independent_evidence_weight":0.0}
{"row_type":"r13_loop92_cross_case","round":"R13","loop":"92","reviewed_round":"R3","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","reviewed_trigger_count":3,"positive_bridge_symbols":[],"validated_4B_guard_symbols":["006110","282880"],"validated_4C_symbols":[],"false_overblock_symbols":["101360"],"counterexample_symbols":[],"avg_positive_MFE90_pct":null,"avg_counter_or_guard_MFE90_pct":104.52,"avg_counter_or_guard_MAE180_pct":-36.68,"cross_redteam_verdict":"bridge_required_guard_passed; weak bridge, price-MFE, late-spike, data-quality and hard-4C rows remain Watch/4B/4C unless exact non-price bridge is repaired","r13_do_not_count_as_new_case":true,"independent_evidence_weight":0.0}
{"row_type":"r13_loop92_cross_case","round":"R13","loop":"92","reviewed_round":"R4","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C16_STRATEGIC_RESOURCE_POLICY_SUPPLY","reviewed_trigger_count":3,"positive_bridge_symbols":["001120"],"validated_4B_guard_symbols":[],"validated_4C_symbols":[],"false_overblock_symbols":[],"counterexample_symbols":["000910","001550"],"avg_positive_MFE90_pct":6.33,"avg_counter_or_guard_MFE90_pct":8.86,"avg_counter_or_guard_MAE180_pct":-31.95,"cross_redteam_verdict":"bridge_required_guard_passed; weak bridge, price-MFE, late-spike, data-quality and hard-4C rows remain Watch/4B/4C unless exact non-price bridge is repaired","r13_do_not_count_as_new_case":true,"independent_evidence_weight":0.0}
{"row_type":"r13_loop92_cross_case","round":"R13","loop":"92","reviewed_round":"R5","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C18_CONSUMER_EXPORT_CHANNEL_REORDER","reviewed_trigger_count":3,"positive_bridge_symbols":["017810"],"validated_4B_guard_symbols":[],"validated_4C_symbols":[],"false_overblock_symbols":[],"counterexample_symbols":["264900","267980"],"avg_positive_MFE90_pct":21.41,"avg_counter_or_guard_MFE90_pct":1.92,"avg_counter_or_guard_MAE180_pct":-5.7,"cross_redteam_verdict":"bridge_required_guard_passed; weak bridge, price-MFE, late-spike, data-quality and hard-4C rows remain Watch/4B/4C unless exact non-price bridge is repaired","r13_do_not_count_as_new_case":true,"independent_evidence_weight":0.0}
{"row_type":"r13_loop92_cross_case","round":"R13","loop":"92","reviewed_round":"R6","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","reviewed_trigger_count":3,"positive_bridge_symbols":["001450"],"validated_4B_guard_symbols":[],"validated_4C_symbols":[],"false_overblock_symbols":[],"counterexample_symbols":["085620","138930"],"avg_positive_MFE90_pct":16.09,"avg_counter_or_guard_MFE90_pct":7.53,"avg_counter_or_guard_MAE180_pct":-16.99,"cross_redteam_verdict":"bridge_required_guard_passed; weak bridge, price-MFE, late-spike, data-quality and hard-4C rows remain Watch/4B/4C unless exact non-price bridge is repaired","r13_do_not_count_as_new_case":true,"independent_evidence_weight":0.0}
{"row_type":"r13_loop92_cross_case","round":"R13","loop":"92","reviewed_round":"R7","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT","reviewed_trigger_count":3,"positive_bridge_symbols":["214150"],"validated_4B_guard_symbols":[],"validated_4C_symbols":[],"false_overblock_symbols":[],"counterexample_symbols":["099190","145720"],"avg_positive_MFE90_pct":89.67,"avg_counter_or_guard_MFE90_pct":2.07,"avg_counter_or_guard_MAE180_pct":-56.36,"cross_redteam_verdict":"bridge_required_guard_passed; weak bridge, price-MFE, late-spike, data-quality and hard-4C rows remain Watch/4B/4C unless exact non-price bridge is repaired","r13_do_not_count_as_new_case":true,"independent_evidence_weight":0.0}
{"row_type":"r13_loop92_cross_case","round":"R13","loop":"92","reviewed_round":"R8","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","reviewed_trigger_count":3,"positive_bridge_symbols":["012510"],"validated_4B_guard_symbols":[],"validated_4C_symbols":[],"false_overblock_symbols":[],"counterexample_symbols":["042510","150900"],"avg_positive_MFE90_pct":91.22,"avg_counter_or_guard_MFE90_pct":5.45,"avg_counter_or_guard_MAE180_pct":-38.43,"cross_redteam_verdict":"bridge_required_guard_passed; weak bridge, price-MFE, late-spike, data-quality and hard-4C rows remain Watch/4B/4C unless exact non-price bridge is repaired","r13_do_not_count_as_new_case":true,"independent_evidence_weight":0.0}
{"row_type":"r13_loop92_cross_case","round":"R13","loop":"92","reviewed_round":"R9","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","reviewed_trigger_count":3,"positive_bridge_symbols":["007860"],"validated_4B_guard_symbols":[],"validated_4C_symbols":[],"false_overblock_symbols":[],"counterexample_symbols":["005710","033530"],"avg_positive_MFE90_pct":83.22,"avg_counter_or_guard_MFE90_pct":12.46,"avg_counter_or_guard_MAE180_pct":-17.55,"cross_redteam_verdict":"bridge_required_guard_passed; weak bridge, price-MFE, late-spike, data-quality and hard-4C rows remain Watch/4B/4C unless exact non-price bridge is repaired","r13_do_not_count_as_new_case":true,"independent_evidence_weight":0.0}
{"row_type":"r13_loop92_cross_case","round":"R13","loop":"92","reviewed_round":"R10","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","reviewed_trigger_count":3,"positive_bridge_symbols":["183190"],"validated_4B_guard_symbols":[],"validated_4C_symbols":["009410"],"false_overblock_symbols":[],"counterexample_symbols":["034300"],"avg_positive_MFE90_pct":13.16,"avg_counter_or_guard_MFE90_pct":18.57,"avg_counter_or_guard_MAE180_pct":-25.94,"cross_redteam_verdict":"bridge_required_guard_passed; weak bridge, price-MFE, late-spike, data-quality and hard-4C rows remain Watch/4B/4C unless exact non-price bridge is repaired","r13_do_not_count_as_new_case":true,"independent_evidence_weight":0.0}
{"row_type":"r13_loop92_cross_case","round":"R13","loop":"92","reviewed_round":"R11","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP","reviewed_trigger_count":3,"positive_bridge_symbols":["011930"],"validated_4B_guard_symbols":[],"validated_4C_symbols":[],"false_overblock_symbols":[],"counterexample_symbols":["023350","023960"],"avg_positive_MFE90_pct":30.65,"avg_counter_or_guard_MFE90_pct":16.07,"avg_counter_or_guard_MAE180_pct":-19.46,"cross_redteam_verdict":"bridge_required_guard_passed; weak bridge, price-MFE, late-spike, data-quality and hard-4C rows remain Watch/4B/4C unless exact non-price bridge is repaired","r13_do_not_count_as_new_case":true,"independent_evidence_weight":0.0}
{"row_type":"r13_loop92_cross_case","round":"R13","loop":"92","reviewed_round":"R12","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","reviewed_trigger_count":3,"positive_bridge_symbols":["010130"],"validated_4B_guard_symbols":[],"validated_4C_symbols":[],"false_overblock_symbols":[],"counterexample_symbols":["000670","180640"],"avg_positive_MFE90_pct":261.41,"avg_counter_or_guard_MFE90_pct":43.04,"avg_counter_or_guard_MAE180_pct":-19.23,"cross_redteam_verdict":"bridge_required_guard_passed; weak bridge, price-MFE, late-spike, data-quality and hard-4C rows remain Watch/4B/4C unless exact non-price bridge is repaired","r13_do_not_count_as_new_case":true,"independent_evidence_weight":0.0}
```

## 6. R13 loop92 review trigger rows

```jsonl
{"row_type":"r13_loop92_review_trigger","round":"R13","loop":"92","reviewed_round":"R1","reviewed_large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","reviewed_canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","reviewed_trigger_id":"R1L92_C02_037030_20240102_STAGE2_FALSE_POSITIVE_POWER_SUPPLY","symbol":"037030","company_name":"파워넷","entry_date":"2024-01-02","entry_price":3175.0,"r13_class":"weak_bridge_counterexample","MFE_90D_pct":6.3,"MAE_90D_pct":-14.02,"MFE_180D_pct":6.3,"MAE_180D_pct":-36.85,"trigger_outcome_label":"counterexample_low_MFE_deep_MAE_no_datacenter_order_bridge","current_profile_verdict":"current_profile_false_positive_if_power_supply_vocabulary_overcredited","r13_guard_verdict":"bridge_missing_or_unverified_keep_4B_watch","r13_do_not_count_as_new_case":true,"independent_evidence_weight":0.0,"source_md":"e2r_stock_web_v12_residual_round_R1_loop_92_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C02_POWER_GRID_DATACENTER_CAPEX_research.md"}
{"row_type":"r13_loop92_review_trigger","round":"R13","loop":"92","reviewed_round":"R1","reviewed_large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","reviewed_canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","reviewed_trigger_id":"R1L92_C02_237750_20240102_STAGE2_FALSE_POSITIVE_DIGITAL_GRID_RELAY","symbol":"237750","company_name":"피앤씨테크","entry_date":"2024-01-02","entry_price":5610.0,"r13_class":"price_MFE_or_spillover_counterexample","MFE_90D_pct":36.19,"MAE_90D_pct":-5.7,"MFE_180D_pct":36.19,"MAE_180D_pct":-41.53,"trigger_outcome_label":"counterexample_price_MFE_deep_MAE_no_order_backlog_bridge","current_profile_verdict":"current_profile_false_positive_if_digital_grid_price_MFE_overcredited","r13_guard_verdict":"price_MFE_spillover_without_direct_cash_path_keep_4B_watch","r13_do_not_count_as_new_case":true,"independent_evidence_weight":0.0,"source_md":"e2r_stock_web_v12_residual_round_R1_loop_92_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C02_POWER_GRID_DATACENTER_CAPEX_research.md"}
{"row_type":"r13_loop92_review_trigger","round":"R13","loop":"92","reviewed_round":"R1","reviewed_large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","reviewed_canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","reviewed_trigger_id":"R1L92_C02_267260_20240129_STAGE2_TRANSFORMER_DATACENTER_BACKLOG","symbol":"267260","company_name":"HD현대일렉트릭","entry_date":"2024-01-29","entry_price":101200.0,"r13_class":"positive_bridge_control","MFE_90D_pct":210.28,"MAE_90D_pct":-3.66,"MFE_180D_pct":308.6,"MAE_180D_pct":-3.66,"trigger_outcome_label":"positive_extreme_MFE90_and_MFE180_low_MAE_transformer_backlog_bridge","current_profile_verdict":"current_profile_correct_if_customer_order_delivery_margin_cash_bridge_required","r13_guard_verdict":"bridge_present_positive_or_positive_watch_but_Green_requires_exact_evidence","r13_do_not_count_as_new_case":true,"independent_evidence_weight":0.0,"source_md":"e2r_stock_web_v12_residual_round_R1_loop_92_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C02_POWER_GRID_DATACENTER_CAPEX_research.md"}
{"row_type":"r13_loop92_review_trigger","round":"R13","loop":"92","reviewed_round":"R2","reviewed_large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","reviewed_canonical_archetype_id":"C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY","reviewed_trigger_id":"R2L92_C08_080580_20240122_STAGE2_FALSE_POSITIVE_TEST_SOCKET_VOLATILITY","symbol":"080580","company_name":"오킨스전자","entry_date":"2024-01-22","entry_price":12930.0,"r13_class":"weak_bridge_counterexample","MFE_90D_pct":15.31,"MAE_90D_pct":-40.06,"MFE_180D_pct":15.31,"MAE_180D_pct":-57.46,"trigger_outcome_label":"counterexample_sub20_MFE_deep_MAE_no_durable_customer_order_bridge","current_profile_verdict":"current_profile_false_positive_if_test_socket_theme_volatility_overcredited","r13_guard_verdict":"bridge_missing_or_unverified_keep_4B_watch","r13_do_not_count_as_new_case":true,"independent_evidence_weight":0.0,"source_md":"e2r_stock_web_v12_residual_round_R2_loop_92_L2_AI_SEMICONDUCTOR_ELECTRONICS_C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY_research.md"}
{"row_type":"r13_loop92_review_trigger","round":"R13","loop":"92","reviewed_round":"R2","reviewed_large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","reviewed_canonical_archetype_id":"C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY","reviewed_trigger_id":"R2L92_C08_092870_20240228_STAGE2_MEMORY_TESTER_CUSTOMER_QUALITY","symbol":"092870","company_name":"엑시콘","entry_date":"2024-02-28","entry_price":17930.0,"r13_class":"positive_bridge_control","MFE_90D_pct":97.43,"MAE_90D_pct":-4.8,"MFE_180D_pct":97.43,"MAE_180D_pct":-45.34,"trigger_outcome_label":"positive_high_MFE90_low_entry_MAE_but_2024_CA_data_quality_watch","current_profile_verdict":"current_profile_correct_if_customer_qualification_order_delivery_margin_cash_bridge_required_and_data_quality_repaired","r13_guard_verdict":"bridge_present_positive_or_positive_watch_but_Green_requires_exact_evidence","r13_do_not_count_as_new_case":true,"independent_evidence_weight":0.0,"source_md":"e2r_stock_web_v12_residual_round_R2_loop_92_L2_AI_SEMICONDUCTOR_ELECTRONICS_C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY_research.md"}
{"row_type":"r13_loop92_review_trigger","round":"R13","loop":"92","reviewed_round":"R2","reviewed_large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","reviewed_canonical_archetype_id":"C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY","reviewed_trigger_id":"R2L92_C08_237750_20240102_STAGE2_FALSE_POSITIVE_CROSSLABEL_GRID_MFE","symbol":"237750","company_name":"피앤씨테크","entry_date":"2024-01-02","entry_price":5610.0,"r13_class":"price_MFE_or_spillover_counterexample","MFE_90D_pct":36.19,"MAE_90D_pct":-5.7,"MFE_180D_pct":36.19,"MAE_180D_pct":-41.53,"trigger_outcome_label":"counterexample_price_MFE_deep_MAE_no_semi_customer_quality_bridge","current_profile_verdict":"current_profile_false_positive_if_cross_label_price_MFE_overcredited","r13_guard_verdict":"price_MFE_spillover_without_direct_cash_path_keep_4B_watch","r13_do_not_count_as_new_case":true,"independent_evidence_weight":0.0,"source_md":"e2r_stock_web_v12_residual_round_R2_loop_92_L2_AI_SEMICONDUCTOR_ELECTRONICS_C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY_research.md"}
{"row_type":"r13_loop92_review_trigger","round":"R13","loop":"92","reviewed_round":"R3","reviewed_large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","reviewed_canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","reviewed_trigger_id":"R3L92_C14_006110_20240102_STAGE2_4B_EV_FOIL_SLOWDOWN","symbol":"006110","company_name":"삼아알미늄","entry_date":"2024-01-02","entry_price":102900.0,"r13_class":"validated_4B_risk_guard","MFE_90D_pct":13.12,"MAE_90D_pct":-28.28,"MFE_180D_pct":13.12,"MAE_180D_pct":-54.62,"trigger_outcome_label":"valid_4B_low_MFE_deep_MAE_EV_demand_slowdown_guard","current_profile_verdict":"current_profile_correct_if_demand_slowdown_calloff_margin_cash_drag_routes_to_4B","r13_guard_verdict":"validated_4B_risk_guard_keep_blocked_from_positive_stages","r13_do_not_count_as_new_case":true,"independent_evidence_weight":0.0,"source_md":"e2r_stock_web_v12_residual_round_R3_loop_92_L3_BATTERY_EV_GREEN_MOBILITY_C14_EV_DEMAND_SLOWDOWN_4B_4C_research.md"}
{"row_type":"r13_loop92_review_trigger","round":"R13","loop":"92","reviewed_round":"R3","reviewed_large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","reviewed_canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","reviewed_trigger_id":"R3L92_C14_101360_20240111_STAGE2_FALSE_OVERBLOCK_PRECURSOR_RAMP","symbol":"101360","company_name":"에코앤드림","entry_date":"2024-01-11","entry_price":22800.0,"r13_class":"false_overblock_override","MFE_90D_pct":294.3,"MAE_90D_pct":-7.89,"MFE_180D_pct":294.3,"MAE_180D_pct":-7.89,"trigger_outcome_label":"counterexample_extreme_MFE_low_MAE_if_broad_slowdown_overblocked","current_profile_verdict":"current_profile_false_positive_if_EV_slowdown_guard_ignores_customer_capacity_ramp_bridge","r13_guard_verdict":"do_not_overblock_when_stronger_customer_capacity_or_order_bridge_exists","r13_do_not_count_as_new_case":true,"independent_evidence_weight":0.0,"source_md":"e2r_stock_web_v12_residual_round_R3_loop_92_L3_BATTERY_EV_GREEN_MOBILITY_C14_EV_DEMAND_SLOWDOWN_4B_4C_research.md"}
{"row_type":"r13_loop92_review_trigger","round":"R13","loop":"92","reviewed_round":"R3","reviewed_large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","reviewed_canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","reviewed_trigger_id":"R3L92_C14_282880_20240102_STAGE2_4B_EQUIPMENT_CAPEX_DELAY","symbol":"282880","company_name":"코윈테크","entry_date":"2024-01-02","entry_price":27750.0,"r13_class":"validated_4B_risk_guard","MFE_90D_pct":6.13,"MAE_90D_pct":-14.77,"MFE_180D_pct":6.13,"MAE_180D_pct":-47.53,"trigger_outcome_label":"valid_4B_low_MFE_deep_MAE_capex_delay_guard","current_profile_verdict":"current_profile_correct_if_capex_delay_backlog_margin_cash_drag_routes_to_4B","r13_guard_verdict":"validated_4B_risk_guard_keep_blocked_from_positive_stages","r13_do_not_count_as_new_case":true,"independent_evidence_weight":0.0,"source_md":"e2r_stock_web_v12_residual_round_R3_loop_92_L3_BATTERY_EV_GREEN_MOBILITY_C14_EV_DEMAND_SLOWDOWN_4B_4C_research.md"}
{"row_type":"r13_loop92_review_trigger","round":"R13","loop":"92","reviewed_round":"R4","reviewed_large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","reviewed_canonical_archetype_id":"C16_STRATEGIC_RESOURCE_POLICY_SUPPLY","reviewed_trigger_id":"R4L92_C16_000910_20240110_STAGE2_FALSE_POSITIVE_RARE_EARTH_POLICY","symbol":"000910","company_name":"유니온","entry_date":"2024-01-10","entry_price":5840.0,"r13_class":"weak_bridge_counterexample","MFE_90D_pct":12.67,"MAE_90D_pct":-12.5,"MFE_180D_pct":12.67,"MAE_180D_pct":-30.91,"trigger_outcome_label":"counterexample_sub20_MFE_deep_MAE_policy_vocabulary_no_offtake_bridge","current_profile_verdict":"current_profile_false_positive_if_rare_earth_policy_vocabulary_overcredited","r13_guard_verdict":"bridge_missing_or_unverified_keep_4B_watch","r13_do_not_count_as_new_case":true,"independent_evidence_weight":0.0,"source_md":"e2r_stock_web_v12_residual_round_R4_loop_92_L4_MATERIALS_SPREAD_RESOURCE_C16_STRATEGIC_RESOURCE_POLICY_SUPPLY_research.md"}
{"row_type":"r13_loop92_review_trigger","round":"R13","loop":"92","reviewed_round":"R4","reviewed_large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","reviewed_canonical_archetype_id":"C16_STRATEGIC_RESOURCE_POLICY_SUPPLY","reviewed_trigger_id":"R4L92_C16_001120_20240129_STAGE2_RESOURCE_TRADING_CASH","symbol":"001120","company_name":"LX인터내셔널","entry_date":"2024-01-29","entry_price":27650.0,"r13_class":"positive_bridge_control","MFE_90D_pct":6.33,"MAE_90D_pct":-6.51,"MFE_180D_pct":13.92,"MAE_180D_pct":-6.69,"trigger_outcome_label":"positive_watch_moderate_MFE_low_MAE_resource_trading_cash_bridge","current_profile_verdict":"current_profile_correct_if_resource_channel_margin_cash_bridge_required_but_Green_strict","r13_guard_verdict":"bridge_present_positive_or_positive_watch_but_Green_requires_exact_evidence","r13_do_not_count_as_new_case":true,"independent_evidence_weight":0.0,"source_md":"e2r_stock_web_v12_residual_round_R4_loop_92_L4_MATERIALS_SPREAD_RESOURCE_C16_STRATEGIC_RESOURCE_POLICY_SUPPLY_research.md"}
{"row_type":"r13_loop92_review_trigger","round":"R13","loop":"92","reviewed_round":"R4","reviewed_large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","reviewed_canonical_archetype_id":"C16_STRATEGIC_RESOURCE_POLICY_SUPPLY","reviewed_trigger_id":"R4L92_C16_001550_20240102_STAGE2_FALSE_POSITIVE_FERTILIZER_POLICY","symbol":"001550","company_name":"조비","entry_date":"2024-01-02","entry_price":14280.0,"r13_class":"weak_bridge_counterexample","MFE_90D_pct":5.04,"MAE_90D_pct":-10.08,"MFE_180D_pct":5.04,"MAE_180D_pct":-32.98,"trigger_outcome_label":"counterexample_low_MFE_deep_MAE_no_subsidy_volume_cash_bridge","current_profile_verdict":"current_profile_false_positive_if_fertilizer_policy_vocabulary_overcredited","r13_guard_verdict":"bridge_missing_or_unverified_keep_4B_watch","r13_do_not_count_as_new_case":true,"independent_evidence_weight":0.0,"source_md":"e2r_stock_web_v12_residual_round_R4_loop_92_L4_MATERIALS_SPREAD_RESOURCE_C16_STRATEGIC_RESOURCE_POLICY_SUPPLY_research.md"}
{"row_type":"r13_loop92_review_trigger","round":"R13","loop":"92","reviewed_round":"R5","reviewed_large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","reviewed_canonical_archetype_id":"C18_CONSUMER_EXPORT_CHANNEL_REORDER","reviewed_trigger_id":"R5L92_C18_017810_20240117_STAGE2_FOOD_EXPORT_REORDER","symbol":"017810","company_name":"풀무원","entry_date":"2024-01-17","entry_price":10040.0,"r13_class":"positive_bridge_control","MFE_90D_pct":21.41,"MAE_90D_pct":-0.8,"MFE_180D_pct":21.41,"MAE_180D_pct":-0.8,"trigger_outcome_label":"positive_watch_MFE90_ge20_low_MAE_reorder_margin_bridge","current_profile_verdict":"current_profile_correct_if_channel_sellthrough_reorder_margin_cash_bridge_required_but_Green_strict","r13_guard_verdict":"bridge_present_positive_or_positive_watch_but_Green_requires_exact_evidence","r13_do_not_count_as_new_case":true,"independent_evidence_weight":0.0,"source_md":"e2r_stock_web_v12_residual_round_R5_loop_92_L5_CONSUMER_BRAND_DISTRIBUTION_C18_CONSUMER_EXPORT_CHANNEL_REORDER_research.md"}
{"row_type":"r13_loop92_review_trigger","round":"R13","loop":"92","reviewed_round":"R5","reviewed_large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","reviewed_canonical_archetype_id":"C18_CONSUMER_EXPORT_CHANNEL_REORDER","reviewed_trigger_id":"R5L92_C18_264900_20240102_STAGE2_FALSE_POSITIVE_SNACK_EXPORT","symbol":"264900","company_name":"크라운제과","entry_date":"2024-01-02","entry_price":8380.0,"r13_class":"weak_bridge_counterexample","MFE_90D_pct":1.67,"MAE_90D_pct":-4.53,"MFE_180D_pct":10.38,"MAE_180D_pct":-4.53,"trigger_outcome_label":"counterexample_low_MFE_MAE_expansion_no_repeat_order_cash_bridge","current_profile_verdict":"current_profile_false_positive_if_snack_export_channel_vocabulary_overcredited","r13_guard_verdict":"late_spike_or_late_price_does_not_validate_original_weak_entry","r13_do_not_count_as_new_case":true,"independent_evidence_weight":0.0,"source_md":"e2r_stock_web_v12_residual_round_R5_loop_92_L5_CONSUMER_BRAND_DISTRIBUTION_C18_CONSUMER_EXPORT_CHANNEL_REORDER_research.md"}
{"row_type":"r13_loop92_review_trigger","round":"R13","loop":"92","reviewed_round":"R5","reviewed_large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","reviewed_canonical_archetype_id":"C18_CONSUMER_EXPORT_CHANNEL_REORDER","reviewed_trigger_id":"R5L92_C18_267980_20240102_STAGE2_FALSE_POSITIVE_DAIRY_CHANNEL","symbol":"267980","company_name":"매일유업","entry_date":"2024-01-02","entry_price":41550.0,"r13_class":"weak_bridge_counterexample","MFE_90D_pct":2.17,"MAE_90D_pct":-5.9,"MFE_180D_pct":2.17,"MAE_180D_pct":-6.86,"trigger_outcome_label":"counterexample_near_zero_MFE_market_segment_watch_no_reorder_bridge","current_profile_verdict":"current_profile_false_positive_if_dairy_global_channel_vocabulary_overcredited","r13_guard_verdict":"data_quality_repair_required_before_patch","r13_do_not_count_as_new_case":true,"independent_evidence_weight":0.0,"source_md":"e2r_stock_web_v12_residual_round_R5_loop_92_L5_CONSUMER_BRAND_DISTRIBUTION_C18_CONSUMER_EXPORT_CHANNEL_REORDER_research.md"}
{"row_type":"r13_loop92_review_trigger","round":"R13","loop":"92","reviewed_round":"R6","reviewed_large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","reviewed_canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","reviewed_trigger_id":"R6L92_C22_001450_20240129_STAGE2_PC_INSURANCE_RESERVE","symbol":"001450","company_name":"현대해상","entry_date":"2024-01-29","entry_price":31700.0,"r13_class":"positive_bridge_control","MFE_90D_pct":16.09,"MAE_90D_pct":-4.57,"MFE_180D_pct":16.09,"MAE_180D_pct":-5.99,"trigger_outcome_label":"positive_watch_moderate_MFE90_low_MAE_reserve_capital_return_bridge","current_profile_verdict":"current_profile_correct_if_loss_ratio_reserve_capital_payout_bridge_required_but_Green_strict","r13_guard_verdict":"bridge_present_positive_or_positive_watch_but_Green_requires_exact_evidence","r13_do_not_count_as_new_case":true,"independent_evidence_weight":0.0,"source_md":"e2r_stock_web_v12_residual_round_R6_loop_92_L6_FINANCIAL_CAPITAL_RETURN_DIGITAL_C22_INSURANCE_RATE_CYCLE_RESERVE_research.md"}
{"row_type":"r13_loop92_review_trigger","round":"R13","loop":"92","reviewed_round":"R6","reviewed_large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","reviewed_canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","reviewed_trigger_id":"R6L92_C22_085620_20240205_STAGE2_FALSE_POSITIVE_LIFE_INSURANCE_SPIKE","symbol":"085620","company_name":"미래에셋생명","entry_date":"2024-02-05","entry_price":6390.0,"r13_class":"weak_bridge_counterexample","MFE_90D_pct":1.72,"MAE_90D_pct":-30.75,"MFE_180D_pct":1.72,"MAE_180D_pct":-30.75,"trigger_outcome_label":"counterexample_near_zero_MFE_deep_MAE_after_spike_no_reserve_payout_bridge","current_profile_verdict":"current_profile_false_positive_if_life_insurance_spike_overcredited","r13_guard_verdict":"bridge_missing_or_unverified_keep_4B_watch","r13_do_not_count_as_new_case":true,"independent_evidence_weight":0.0,"source_md":"e2r_stock_web_v12_residual_round_R6_loop_92_L6_FINANCIAL_CAPITAL_RETURN_DIGITAL_C22_INSURANCE_RATE_CYCLE_RESERVE_research.md"}
{"row_type":"r13_loop92_review_trigger","round":"R13","loop":"92","reviewed_round":"R6","reviewed_large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","reviewed_canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","reviewed_trigger_id":"R6L92_C22_138930_20240129_STAGE2_FALSE_POSITIVE_BANK_RATE_CROSSLABEL","symbol":"138930","company_name":"BNK금융지주","entry_date":"2024-01-29","entry_price":7420.0,"r13_class":"price_MFE_or_spillover_counterexample","MFE_90D_pct":13.34,"MAE_90D_pct":-3.23,"MFE_180D_pct":35.44,"MAE_180D_pct":-3.23,"trigger_outcome_label":"counterexample_price_MFE_but_cross_label_no_insurance_reserve_bridge","current_profile_verdict":"current_profile_false_positive_if_bank_rate_PBR_MFE_counted_as_C22_insurance_evidence","r13_guard_verdict":"price_MFE_spillover_without_direct_cash_path_keep_4B_watch","r13_do_not_count_as_new_case":true,"independent_evidence_weight":0.0,"source_md":"e2r_stock_web_v12_residual_round_R6_loop_92_L6_FINANCIAL_CAPITAL_RETURN_DIGITAL_C22_INSURANCE_RATE_CYCLE_RESERVE_research.md"}
{"row_type":"r13_loop92_review_trigger","round":"R13","loop":"92","reviewed_round":"R7","reviewed_large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","reviewed_canonical_archetype_id":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT","reviewed_trigger_id":"R7L92_C25_099190_20240111_STAGE2_FALSE_POSITIVE_CGM_REIMBURSEMENT","symbol":"099190","company_name":"아이센스","entry_date":"2024-01-11","entry_price":30050.0,"r13_class":"weak_bridge_counterexample","MFE_90D_pct":1.16,"MAE_90D_pct":-37.17,"MFE_180D_pct":1.16,"MAE_180D_pct":-50.18,"trigger_outcome_label":"counterexample_near_zero_MFE_deep_MAE_no_reimbursement_adoption_consumables_bridge","current_profile_verdict":"current_profile_false_positive_if_CGM_reimbursement_vocabulary_overcredited","r13_guard_verdict":"bridge_missing_or_unverified_keep_4B_watch","r13_do_not_count_as_new_case":true,"independent_evidence_weight":0.0,"source_md":"e2r_stock_web_v12_residual_round_R7_loop_92_L7_BIO_HEALTHCARE_MEDICAL_C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT_research.md"}
{"row_type":"r13_loop92_review_trigger","round":"R13","loop":"92","reviewed_round":"R7","reviewed_large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","reviewed_canonical_archetype_id":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT","reviewed_trigger_id":"R7L92_C25_145720_20240229_STAGE2_FALSE_POSITIVE_DENTAL_IMPLANT_EXPORT_SPIKE","symbol":"145720","company_name":"덴티움","entry_date":"2024-02-29","entry_price":144200.0,"r13_class":"weak_bridge_counterexample","MFE_90D_pct":2.98,"MAE_90D_pct":-13.18,"MFE_180D_pct":2.98,"MAE_180D_pct":-62.55,"trigger_outcome_label":"counterexample_near_zero_MFE_extreme_MAE_after_export_spike_no_bridge","current_profile_verdict":"current_profile_false_positive_if_dental_export_spike_overcredited","r13_guard_verdict":"bridge_missing_or_unverified_keep_4B_watch","r13_do_not_count_as_new_case":true,"independent_evidence_weight":0.0,"source_md":"e2r_stock_web_v12_residual_round_R7_loop_92_L7_BIO_HEALTHCARE_MEDICAL_C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT_research.md"}
{"row_type":"r13_loop92_review_trigger","round":"R13","loop":"92","reviewed_round":"R7","reviewed_large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","reviewed_canonical_archetype_id":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT","reviewed_trigger_id":"R7L92_C25_214150_20240214_STAGE2_AESTHETIC_DEVICE_CONSUMABLE_EXPORT","symbol":"214150","company_name":"클래시스","entry_date":"2024-02-14","entry_price":30000.0,"r13_class":"positive_bridge_control","MFE_90D_pct":89.67,"MAE_90D_pct":-6.5,"MFE_180D_pct":109.67,"MAE_180D_pct":-6.5,"trigger_outcome_label":"positive_high_MFE90_and_MFE180_low_MAE_device_consumable_export_bridge","current_profile_verdict":"current_profile_correct_if_procedure_volume_consumable_reorder_margin_cash_bridge_required_but_data_quality_repair_needed","r13_guard_verdict":"bridge_present_positive_or_positive_watch_but_Green_requires_exact_evidence","r13_do_not_count_as_new_case":true,"independent_evidence_weight":0.0,"source_md":"e2r_stock_web_v12_residual_round_R7_loop_92_L7_BIO_HEALTHCARE_MEDICAL_C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT_research.md"}
{"row_type":"r13_loop92_review_trigger","round":"R13","loop":"92","reviewed_round":"R8","reviewed_large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","reviewed_canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","reviewed_trigger_id":"R8L92_C28_012510_20240108_STAGE2_ERP_CLOUD_CONTRACT_RETENTION","symbol":"012510","company_name":"더존비즈온","entry_date":"2024-01-08","entry_price":34150.0,"r13_class":"positive_bridge_control","MFE_90D_pct":91.22,"MAE_90D_pct":-9.08,"MFE_180D_pct":129.28,"MAE_180D_pct":-9.08,"trigger_outcome_label":"positive_extreme_MFE90_and_MFE180_controlled_MAE_contract_retention_bridge","current_profile_verdict":"current_profile_correct_if_contract_renewal_ARR_margin_cash_bridge_required","r13_guard_verdict":"bridge_present_positive_or_positive_watch_but_Green_requires_exact_evidence","r13_do_not_count_as_new_case":true,"independent_evidence_weight":0.0,"source_md":"e2r_stock_web_v12_residual_round_R8_loop_92_L8_PLATFORM_CONTENT_SW_SECURITY_C28_SOFTWARE_SECURITY_CONTRACT_RETENTION_research.md"}
{"row_type":"r13_loop92_review_trigger","round":"R13","loop":"92","reviewed_round":"R8","reviewed_large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","reviewed_canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","reviewed_trigger_id":"R8L92_C28_042510_20240126_STAGE2_FALSE_POSITIVE_DIGITAL_ID_AUTH","symbol":"042510","company_name":"라온시큐어","entry_date":"2024-01-26","entry_price":2940.0,"r13_class":"weak_bridge_counterexample","MFE_90D_pct":4.25,"MAE_90D_pct":-22.45,"MFE_180D_pct":4.25,"MAE_180D_pct":-30.61,"trigger_outcome_label":"counterexample_low_MFE_deep_MAE_theme_spike_no_contract_retention_bridge","current_profile_verdict":"current_profile_false_positive_if_digital_ID_authentication_theme_overcredited","r13_guard_verdict":"data_quality_repair_required_before_patch","r13_do_not_count_as_new_case":true,"independent_evidence_weight":0.0,"source_md":"e2r_stock_web_v12_residual_round_R8_loop_92_L8_PLATFORM_CONTENT_SW_SECURITY_C28_SOFTWARE_SECURITY_CONTRACT_RETENTION_research.md"}
{"row_type":"r13_loop92_review_trigger","round":"R13","loop":"92","reviewed_round":"R8","reviewed_large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","reviewed_canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","reviewed_trigger_id":"R8L92_C28_150900_20240102_STAGE2_FALSE_POSITIVE_DATA_SECURITY","symbol":"150900","company_name":"파수","entry_date":"2024-01-02","entry_price":9470.0,"r13_class":"weak_bridge_counterexample","MFE_90D_pct":6.65,"MAE_90D_pct":-34.0,"MFE_180D_pct":6.65,"MAE_180D_pct":-46.25,"trigger_outcome_label":"counterexample_low_MFE_deep_MAE_no_renewal_ARR_bridge","current_profile_verdict":"current_profile_false_positive_if_data_security_vocabulary_overcredited","r13_guard_verdict":"bridge_missing_or_unverified_keep_4B_watch","r13_do_not_count_as_new_case":true,"independent_evidence_weight":0.0,"source_md":"e2r_stock_web_v12_residual_round_R8_loop_92_L8_PLATFORM_CONTENT_SW_SECURITY_C28_SOFTWARE_SECURITY_CONTRACT_RETENTION_research.md"}
{"row_type":"r13_loop92_review_trigger","round":"R13","loop":"92","reviewed_round":"R9","reviewed_large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","reviewed_canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","reviewed_trigger_id":"R9L92_C29_005710_20240129_STAGE2_FALSE_POSITIVE_SEAT_PARTS","symbol":"005710","company_name":"대원산업","entry_date":"2024-01-29","entry_price":6150.0,"r13_class":"weak_bridge_counterexample","MFE_90D_pct":10.08,"MAE_90D_pct":-8.94,"MFE_180D_pct":10.08,"MAE_180D_pct":-9.11,"trigger_outcome_label":"counterexample_low_MFE_flat_path_no_fresh_OEM_volume_bridge","current_profile_verdict":"current_profile_false_positive_if_seat_parts_vocabulary_overcredited","r13_guard_verdict":"bridge_missing_or_unverified_keep_4B_watch","r13_do_not_count_as_new_case":true,"independent_evidence_weight":0.0,"source_md":"e2r_stock_web_v12_residual_round_R9_loop_92_L3_BATTERY_EV_GREEN_MOBILITY_C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE_research.md"}
{"row_type":"r13_loop92_review_trigger","round":"R13","loop":"92","reviewed_round":"R9","reviewed_large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","reviewed_canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","reviewed_trigger_id":"R9L92_C29_007860_20240129_STAGE2_AUTO_INTERIOR_VOLUME_MIX","symbol":"007860","company_name":"서연","entry_date":"2024-01-29","entry_price":7570.0,"r13_class":"positive_bridge_control","MFE_90D_pct":83.22,"MAE_90D_pct":-3.04,"MFE_180D_pct":83.22,"MAE_180D_pct":-10.96,"trigger_outcome_label":"positive_high_MFE90_controlled_entry_MAE_auto_interior_volume_mix_bridge","current_profile_verdict":"current_profile_correct_if_OEM_volume_program_mix_margin_cash_bridge_required","r13_guard_verdict":"bridge_present_positive_or_positive_watch_but_Green_requires_exact_evidence","r13_do_not_count_as_new_case":true,"independent_evidence_weight":0.0,"source_md":"e2r_stock_web_v12_residual_round_R9_loop_92_L3_BATTERY_EV_GREEN_MOBILITY_C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE_research.md"}
{"row_type":"r13_loop92_review_trigger","round":"R13","loop":"92","reviewed_round":"R9","reviewed_large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","reviewed_canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","reviewed_trigger_id":"R9L92_C29_033530_20240102_STAGE2_FALSE_POSITIVE_EXHAUST_LEGACY_AUTOPARTS","symbol":"033530","company_name":"SJG세종","entry_date":"2024-01-02","entry_price":6000.0,"r13_class":"weak_bridge_counterexample","MFE_90D_pct":14.83,"MAE_90D_pct":-9.17,"MFE_180D_pct":14.83,"MAE_180D_pct":-26.0,"trigger_outcome_label":"counterexample_sub20_MFE_deep_MAE_name_transition_watch_no_OEM_volume_bridge","current_profile_verdict":"current_profile_false_positive_if_exhaust_legacy_autoparts_vocabulary_overcredited","r13_guard_verdict":"data_quality_repair_required_before_patch","r13_do_not_count_as_new_case":true,"independent_evidence_weight":0.0,"source_md":"e2r_stock_web_v12_residual_round_R9_loop_92_L3_BATTERY_EV_GREEN_MOBILITY_C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE_research.md"}
{"row_type":"r13_loop92_review_trigger","round":"R13","loop":"92","reviewed_round":"R10","reviewed_large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","reviewed_canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","reviewed_trigger_id":"R10L92_C30_009410_20240103_STAGE2_4C_PF_WORKOUT_HARD_BREAK","symbol":"009410","company_name":"태영건설","entry_date":"2024-01-03","entry_price":3245.0,"r13_class":"validated_4C_hard_break","MFE_90D_pct":26.66,"MAE_90D_pct":-32.82,"MFE_180D_pct":26.66,"MAE_180D_pct":-32.82,"trigger_outcome_label":"hard_4C_PF_workout_high_volatility_high_MAE_trading_halt_share_count_change_watch","current_profile_verdict":"current_profile_correct_if_PF_workout_liquidity_hard_break_routes_to_4C_not_bargain_rebound","r13_guard_verdict":"hard_4C_credit_event_or_thesis_break_guard_keep_out_of_positive_stages","r13_do_not_count_as_new_case":true,"independent_evidence_weight":0.0,"source_md":"e2r_stock_web_v12_residual_round_R10_loop_92_L9_CONSTRUCTION_REALESTATE_HOUSING_C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK_research.md"}
{"row_type":"r13_loop92_review_trigger","round":"R13","loop":"92","reviewed_round":"R10","reviewed_large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","reviewed_canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","reviewed_trigger_id":"R10L92_C30_034300_20240118_STAGE2_FALSE_POSITIVE_LATE_PRICE_NONVALIDATION","symbol":"034300","company_name":"신세계건설","entry_date":"2024-01-18","entry_price":12600.0,"r13_class":"weak_bridge_counterexample","MFE_90D_pct":10.48,"MAE_90D_pct":-19.05,"MFE_180D_pct":45.56,"MAE_180D_pct":-19.05,"trigger_outcome_label":"counterexample_CA_late_price_not_original_PF_backlog_cash_validation","current_profile_verdict":"current_profile_false_positive_if_late_corporate_action_price_behavior_validates_original_weak_entry","r13_guard_verdict":"late_spike_or_late_price_does_not_validate_original_weak_entry","r13_do_not_count_as_new_case":true,"independent_evidence_weight":0.0,"source_md":"e2r_stock_web_v12_residual_round_R10_loop_92_L9_CONSTRUCTION_REALESTATE_HOUSING_C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK_research.md"}
{"row_type":"r13_loop92_review_trigger","round":"R13","loop":"92","reviewed_round":"R10","reviewed_large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","reviewed_canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","reviewed_trigger_id":"R10L92_C30_183190_20240129_STAGE2_CEMENT_MARGIN_CASH","symbol":"183190","company_name":"아세아시멘트","entry_date":"2024-01-29","entry_price":10260.0,"r13_class":"positive_bridge_control","MFE_90D_pct":13.16,"MAE_90D_pct":-4.58,"MFE_180D_pct":13.16,"MAE_180D_pct":-4.58,"trigger_outcome_label":"positive_watch_moderate_MFE_low_MAE_materials_margin_cash_bridge","current_profile_verdict":"current_profile_correct_if_ASP_input_cost_margin_cash_bridge_required_but_Green_strict","r13_guard_verdict":"bridge_present_positive_or_positive_watch_but_Green_requires_exact_evidence","r13_do_not_count_as_new_case":true,"independent_evidence_weight":0.0,"source_md":"e2r_stock_web_v12_residual_round_R10_loop_92_L9_CONSTRUCTION_REALESTATE_HOUSING_C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK_research.md"}
{"row_type":"r13_loop92_review_trigger","round":"R13","loop":"92","reviewed_round":"R11","reviewed_large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","reviewed_canonical_archetype_id":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP","reviewed_trigger_id":"R11L92_C05_011930_20240129_STAGE2_CLEANROOM_EPC_ORDER_MARGIN","symbol":"011930","company_name":"신성이엔지","entry_date":"2024-01-29","entry_price":1948.0,"r13_class":"positive_bridge_control","MFE_90D_pct":30.65,"MAE_90D_pct":-1.75,"MFE_180D_pct":30.65,"MAE_180D_pct":-26.08,"trigger_outcome_label":"positive_watch_MFE90_ge30_low_entry_MAE_but_late_drawdown_EPC_margin_bridge","current_profile_verdict":"current_profile_correct_if_signed_order_delivery_cost_pass_through_margin_cash_bridge_required_but_Green_strict","r13_guard_verdict":"bridge_present_positive_or_positive_watch_but_Green_requires_exact_evidence","r13_do_not_count_as_new_case":true,"independent_evidence_weight":0.0,"source_md":"e2r_stock_web_v12_residual_round_R11_loop_92_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C05_EPC_MEGA_CONTRACT_MARGIN_GAP_research.md"}
{"row_type":"r13_loop92_review_trigger","round":"R13","loop":"92","reviewed_round":"R11","reviewed_large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","reviewed_canonical_archetype_id":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP","reviewed_trigger_id":"R11L92_C05_023350_20240110_STAGE2_FALSE_POSITIVE_ENGINEERING_POLICY_PROJECT","symbol":"023350","company_name":"한국종합기술","entry_date":"2024-01-10","entry_price":5840.0,"r13_class":"weak_bridge_counterexample","MFE_90D_pct":16.27,"MAE_90D_pct":-7.53,"MFE_180D_pct":16.27,"MAE_180D_pct":-25.17,"trigger_outcome_label":"counterexample_policy_project_vocabulary_late_spike_not_original_margin_bridge","current_profile_verdict":"current_profile_false_positive_if_engineering_policy_project_vocabulary_overcredited","r13_guard_verdict":"late_spike_or_late_price_does_not_validate_original_weak_entry","r13_do_not_count_as_new_case":true,"independent_evidence_weight":0.0,"source_md":"e2r_stock_web_v12_residual_round_R11_loop_92_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C05_EPC_MEGA_CONTRACT_MARGIN_GAP_research.md"}
{"row_type":"r13_loop92_review_trigger","round":"R13","loop":"92","reviewed_round":"R11","reviewed_large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","reviewed_canonical_archetype_id":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP","reviewed_trigger_id":"R11L92_C05_023960_20240129_STAGE2_FALSE_POSITIVE_SMALL_EPC_LATE_SPIKE","symbol":"023960","company_name":"에쓰씨엔지니어링","entry_date":"2024-01-29","entry_price":1700.0,"r13_class":"weak_bridge_counterexample","MFE_90D_pct":15.88,"MAE_90D_pct":-13.76,"MFE_180D_pct":44.12,"MAE_180D_pct":-13.76,"trigger_outcome_label":"counterexample_late_spike_not_original_entry_validation_deep_full_window_MAE","current_profile_verdict":"current_profile_false_positive_if_late_spike_validates_original_small_EPC_vocabulary_entry","r13_guard_verdict":"late_spike_or_late_price_does_not_validate_original_weak_entry","r13_do_not_count_as_new_case":true,"independent_evidence_weight":0.0,"source_md":"e2r_stock_web_v12_residual_round_R11_loop_92_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C05_EPC_MEGA_CONTRACT_MARGIN_GAP_research.md"}
{"row_type":"r13_loop92_review_trigger","round":"R13","loop":"92","reviewed_round":"R12","reviewed_large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","reviewed_canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","reviewed_trigger_id":"R12L92_C32_000670_20240913_STAGE2_FALSE_POSITIVE_SPILLOVER_CONTROL_BATTLE","symbol":"000670","company_name":"영풍","entry_date":"2024-09-13","entry_price":386000.0,"r13_class":"price_MFE_or_spillover_counterexample","MFE_90D_pct":68.13,"MAE_90D_pct":-13.08,"MFE_180D_pct":68.13,"MAE_180D_pct":-13.08,"trigger_outcome_label":"counterexample_price_MFE_but_spillover_no_direct_minority_cash_path_high_after_peak_drawdown","current_profile_verdict":"current_profile_false_positive_if_spillover_MFE_counted_as_direct_C32_tender_evidence","r13_guard_verdict":"price_MFE_spillover_without_direct_cash_path_keep_4B_watch","r13_do_not_count_as_new_case":true,"independent_evidence_weight":0.0,"source_md":"e2r_stock_web_v12_residual_round_R12_loop_92_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP_research.md"}
{"row_type":"r13_loop92_review_trigger","round":"R13","loop":"92","reviewed_round":"R12","reviewed_large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","reviewed_canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","reviewed_trigger_id":"R12L92_C32_010130_20240913_STAGE2_CONTROL_PREMIUM_TENDER_CASH_PATH","symbol":"010130","company_name":"고려아연","entry_date":"2024-09-13","entry_price":666000.0,"r13_class":"positive_bridge_control","MFE_90D_pct":261.41,"MAE_90D_pct":-1.65,"MFE_180D_pct":261.41,"MAE_180D_pct":-1.65,"trigger_outcome_label":"positive_extreme_MFE90_and_MFE180_low_entry_MAE_direct_tender_cash_path","current_profile_verdict":"current_profile_correct_if_tender_terms_minority_eligibility_financing_settlement_floor_required","r13_guard_verdict":"bridge_present_positive_or_positive_watch_but_Green_requires_exact_evidence","r13_do_not_count_as_new_case":true,"independent_evidence_weight":0.0,"source_md":"e2r_stock_web_v12_residual_round_R12_loop_92_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP_research.md"}
{"row_type":"r13_loop92_review_trigger","round":"R13","loop":"92","reviewed_round":"R12","reviewed_large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","reviewed_canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","reviewed_trigger_id":"R12L92_C32_180640_20240129_STAGE2_FALSE_POSITIVE_HISTORICAL_CONTROL_PREMIUM","symbol":"180640","company_name":"한진칼","entry_date":"2024-01-29","entry_price":74100.0,"r13_class":"weak_bridge_counterexample","MFE_90D_pct":17.95,"MAE_90D_pct":-25.37,"MFE_180D_pct":28.07,"MAE_180D_pct":-25.37,"trigger_outcome_label":"counterexample_sub20_MFE_deep_MAE_no_fresh_tender_cap","current_profile_verdict":"current_profile_false_positive_if_historical_control_premium_vocabulary_overcredited","r13_guard_verdict":"late_spike_or_late_price_does_not_validate_original_weak_entry","r13_do_not_count_as_new_case":true,"independent_evidence_weight":0.0,"source_md":"e2r_stock_web_v12_residual_round_R12_loop_92_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP_research.md"}
```

## 7. Guardrail stress-test results

```jsonl
{"row_type":"r13_guardrail_summary","round":"R13","loop":"92","guardrail_id":"bridge_missing_price_MFE_late_spike_data_quality_false_overblock_hard4C_guard","reviewed_trigger_count":36,"positive_bridge_count":11,"validated_4B_guard_count":2,"hard_4C_count":1,"false_overblock_override_count":1,"weak_bridge_or_spillover_counterexample_count":21,"weak_counter_MFE90_lt20_count":18,"weak_counter_MFE90_ge20_count":3,"weak_counter_MAE90_le_minus20_count":6,"weak_counter_MAE180_le_minus25_count":14,"price_MFE_or_spillover_count":4,"late_spike_nonvalidation_count":5,"data_quality_watch_count":9,"verdict":"existing calibrated axes are directionally correct; do not loosen Green; do not let price-MFE, spillover, late spikes or data-quality rows validate missing bridges."}
{"row_type":"r13_guardrail_rule_candidate","round":"R13","loop":"92","rule_candidate":"cross_archetype_bridge_missing_hard_4B_watch","condition":"bridge_missing_or_unverified AND (MFE90 < 20 OR MAE180 <= -25 OR evidence_type includes price_only_or_price_MFE)","action":"block Stage2-Actionable/Yellow/Green; route to Watch/4B/evidence repair","apply_now":false,"shadow_only":true,"do_not_propose_new_weight_delta":true}
{"row_type":"r13_guardrail_rule_candidate","round":"R13","loop":"92","rule_candidate":"price_MFE_or_spillover_not_direct_bridge_validation","condition":"price_MFE_exists BUT direct company-specific bridge/cash-path/customer-order/tender/reimbursement/evidence is missing","action":"do not classify as positive; require exact direct bridge evidence","apply_now":false,"shadow_only":true,"do_not_propose_new_weight_delta":true}
{"row_type":"r13_guardrail_rule_candidate","round":"R13","loop":"92","rule_candidate":"late_spike_not_original_entry_validation","condition":"original_entry_bridge_missing AND later_spike_or_late_price_behavior_occurs","action":"do not retroactively validate original entry; require fresh trigger date and fresh non-price bridge evidence","apply_now":false,"shadow_only":true,"do_not_propose_new_weight_delta":true}
{"row_type":"r13_guardrail_rule_candidate","round":"R13","loop":"92","rule_candidate":"hard_4C_credit_or_thesis_break_not_bargain_rebound","condition":"PF_workout OR liquidity_hard_break OR trading_halt OR hard thesis failure","action":"route to hard 4C/data-quality watch even if local MFE appears","apply_now":false,"shadow_only":true,"do_not_propose_new_weight_delta":true}
{"row_type":"r13_guardrail_rule_candidate","round":"R13","loop":"92","rule_candidate":"false_overblock_customer_ramp_override","condition":"broad sector risk vocabulary exists BUT exact customer capacity ramp / offtake / order bridge is stronger","action":"do not hard-block; move to evidence-repair / Yellow-candidate watch, not automatic Green","apply_now":false,"shadow_only":true,"do_not_propose_new_weight_delta":true}
{"row_type":"r13_guardrail_rule_candidate","round":"R13","loop":"92","rule_candidate":"data_quality_repair_before_patch","condition":"corporate-action candidate, market segment change, inactive-like, future candidate, name transition, share-count movement, or recent listing is present","action":"allow research annotation but block production patch until price path and exact evidence are repaired","apply_now":false,"shadow_only":true,"do_not_propose_new_weight_delta":true}
{"row_type":"r13_guardrail_rule_candidate","round":"R13","loop":"92","rule_candidate":"Green_requires_exact_non_price_bridge","condition":"positive_control_has_high_MFE_but_source_proxy_only_or_late_drawdown_or_data_quality_watch","action":"allow Yellow/Green-candidate-watch only; exact source-grade bridge required before Green","apply_now":false,"shadow_only":true,"do_not_propose_new_weight_delta":true}
```

## 8. Sector-by-sector redteam notes

```text
R1 / C02 grid-datacenter:
  267260 confirms transformer/datacenter backlog bridge; 037030 and 237750 show power-supply/digital-grid vocabulary and price-MFE require customer order, backlog, delivery and margin/cash evidence.

R2 / C08 semiconductor test/socket:
  092870 confirms memory-tester/customer-quality bridge but needs 2024 CA repair; 080580 and 237750 show socket-theme or cross-label price-MFE is not customer qualification/order evidence.

R3 / C14 EV slowdown:
  006110 and 282880 validate 4B demand-slowdown/capex-delay guards; 101360 shows broad EV slowdown must not overblock when customer capacity-ramp/offtake bridge is stronger.

R4 / C16 strategic resource:
  001120 is resource-trading positive-watch only; 000910 and 001550 show rare-earth/fertilizer policy vocabulary fails without offtake, subsidy-to-volume, margin and cash evidence.

R5 / C18 consumer export reorder:
  017810 supports food export/reorder positive-watch; 267980 and 264900 show dairy/snack channel vocabulary fails without sell-through, reorder, SKU/mix and cash bridge.

R6 / C22 insurance reserve:
  001450 supports P&C reserve/capital-return positive-watch; 085620 and 138930 show life-insurance spike and bank-rate/PBR cross-label MFE cannot validate C22.

R7 / C25 medical device:
  214150 confirms aesthetic-device procedure/consumables bridge; 145720 and 099190 show dental/CGM/reimbursement vocabulary fails without repeat order, adoption, margin and cash bridge.

R8 / C28 software/security:
  012510 confirms ERP/cloud contract-retention and ARR bridge; 150900 and 042510 show security/digital-ID vocabulary fails without renewal, ARR, module expansion and margin/cash bridge.

R9 / C29 mobility:
  007860 confirms auto-interior OEM volume/program-mix bridge; 005710 and 033530 show seat/exhaust vocabulary fails without fresh OEM volume, utilization and margin/cash bridge.

R10 / C30 construction:
  183190 is cement-margin positive-watch; 009410 is PF-workout hard 4C; 034300 shows corporate-action/inactive-like late price does not validate original PF/backlog/cash.

R11 / C05 EPC:
  011930 confirms cleanroom EPC order-margin positive-watch; 023960 and 023350 show late Q3/Q4 or December spikes require fresh trigger evidence and cannot backfill old weak entries.

R12 / C32 governance:
  010130 confirms direct tender/control-premium cash path; 000670 and 180640 show spillover MFE or historical control-premium vocabulary fails without direct minority tender/cash path.
```

## 9. Shadow-only recommendations

```jsonl
{"row_type":"shadow_weight","round":"R13","loop":"92","axis":"cross_archetype_direct_bridge_required_before_Yellow","scope":"cross_archetype","candidate_delta":0.0,"direction":"diagnostic_guard","apply_now":false,"shadow_only":true,"do_not_propose_new_weight_delta":true,"evidence_basis":"Positive controls averaged MFE90 83.72% with MAE90 -4.27%, but weak-bridge/spillover counterexamples averaged MFE90 14.25% and MAE180 -28.94%."}
{"row_type":"shadow_weight","round":"R13","loop":"92","axis":"cross_archetype_price_MFE_not_positive_evidence","scope":"cross_archetype","candidate_delta":0.0,"direction":"diagnostic_guard","apply_now":false,"shadow_only":true,"do_not_propose_new_weight_delta":true,"evidence_basis":"Price-MFE/spillover flags appeared in grid, semi, financial, governance and other rows; direct bridge evidence remained the differentiator."}
{"row_type":"shadow_weight","round":"R13","loop":"92","axis":"cross_archetype_late_spike_not_original_entry_validation","scope":"cross_archetype","candidate_delta":0.0,"direction":"diagnostic_guard","apply_now":false,"shadow_only":true,"do_not_propose_new_weight_delta":true,"evidence_basis":"Late-spike non-validation appeared in consumer, construction and EPC rows; old weak entries require fresh trigger-date evidence."}
{"row_type":"shadow_weight","round":"R13","loop":"92","axis":"cross_archetype_hard_4C_credit_event_guard","scope":"cross_archetype","candidate_delta":0.0,"direction":"hard_failure_guard","apply_now":false,"shadow_only":true,"do_not_propose_new_weight_delta":true,"evidence_basis":"009410 shows PF workout/liquidity hard break cannot be treated as ordinary 4B or bargain rebound even when local MFE appears."}
{"row_type":"shadow_weight","round":"R13","loop":"92","axis":"cross_archetype_false_overblock_override_guard","scope":"cross_archetype","candidate_delta":0.0,"direction":"override_guard","apply_now":false,"shadow_only":true,"do_not_propose_new_weight_delta":true,"evidence_basis":"101360 shows broad sector risk vocabulary must yield when exact customer-ramp/offtake bridge is stronger."}
{"row_type":"shadow_weight","round":"R13","loop":"92","axis":"cross_archetype_data_quality_repair_before_patch","scope":"cross_archetype","candidate_delta":0.0,"direction":"data_quality_guard","apply_now":false,"shadow_only":true,"do_not_propose_new_weight_delta":true,"evidence_basis":"Data-quality watches appeared in 9 rows, including CA candidates, market-segment changes, name transitions, future candidates, share-count movement and inactive-like paths."}
{"row_type":"shadow_weight","round":"R13","loop":"92","axis":"cross_archetype_Green_requires_exact_non_price_bridge","scope":"cross_archetype","candidate_delta":0.0,"direction":"green_strictness_guard","apply_now":false,"shadow_only":true,"do_not_propose_new_weight_delta":true,"evidence_basis":"All reviewed rows remain source-proxy-only and evidence-url-pending, so Green should not be loosened from this batch alone."}
```

## 10. Residual Contribution Summary

```text
new_independent_case_count: 0
reused_case_count: 36
reviewed_trigger_count: 36
reviewed_source_file_count: 12
reviewed_original_round_count: 12
reviewed_original_canonical_count: 12

positive_bridge_count: 11
validated_4B_guard_count: 2
hard_4C_count: 1
false_overblock_override_count: 1
weak_bridge_or_spillover_counterexample_count: 21

do_not_count_as_new_case: true
independent_evidence_weight: 0.0
do_not_propose_new_weight_delta: true

tested_existing_calibrated_axes:
  - price_only_blowoff_blocks_positive_stage
  - full_4b_requires_non_price_evidence
  - hard_4c_thesis_break_routes_to_4c
  - stage3_green_total_min
  - stage3_green_revision_min

residual_error_types_confirmed:
  - theme_label_overcredit
  - bridge_missing_or_unverified
  - price_MFE_or_spillover_overcredit
  - late_spike_or_late_price_not_original_entry_validation
  - data_quality_watch_before_patch
  - hard_4C_credit_event_not_bargain_rebound
  - false_overblock_when_stronger_customer_or_order_bridge_exists
  - source_proxy_only_before_Green

diagnostic_axis_proposed:
  - cross_archetype_direct_bridge_required_before_Yellow
  - cross_archetype_price_MFE_not_positive_evidence
  - cross_archetype_late_spike_not_original_entry_validation
  - cross_archetype_hard_4C_credit_event_guard
  - cross_archetype_false_overblock_override_guard
  - cross_archetype_data_quality_repair_before_patch
  - cross_archetype_Green_requires_exact_non_price_bridge

existing_axis_strengthened:
  - price_only_blowoff_blocks_positive_stage
  - full_4b_requires_non_price_evidence
  - hard_4c_thesis_break_routes_to_4c

existing_axis_weakened: null
sector_specific_rule_candidate: false
canonical_archetype_rule_candidate: false
R13_cross_redteam_rule_candidate: true
loop_contribution_label: axis_stress_test_passed
```

## 11. Deferred Coding Agent Handoff Prompt

```text
You are the coding agent for Songdaiki/stock_agent.

Do not execute this handoff during the research-writing session.

When a later batch implementation is requested:
1. Ingest this R13 MD only as a cross-redteam review artifact.
2. Do not count any r13_loop92_review_trigger as a new independent case.
3. Confirm reviewed rows came from R1~R12 loop92 MDs.
4. Confirm all reviewed source rows use:
   - price_data_source=Songdaiki/stock-web
   - price_basis=tradable_raw
   - price_adjustment_status=raw_unadjusted_marcap
5. Confirm R13 / L10 / R13_CROSS_ARCHETYPE_4B_4C_REDTEAM round-sector consistency.
6. Treat all recommendations here as shadow-only diagnostics.
7. Do not apply weight deltas from this MD alone.
8. Use this MD to prioritize exact evidence repair and canonical guard design:
   - direct_bridge_required_before_Yellow
   - price_MFE_not_positive_evidence
   - late_spike_not_original_entry_validation
   - hard_4C_credit_event_guard
   - false_overblock_override_guard
   - data_quality_repair_before_patch
   - Green_requires_exact_non_price_bridge
9. Confirm accidentally touched stale R11/C05, R10/C30, R8/C28, R7/C25 and earlier-sector candidate rows are not double-counted here beyond their already-reviewed scheduled MDs.
10. Do not loosen Stage3-Green.
11. Do not use future MFE/MAE in runtime scoring.
```

## 12. Round state

```text
completed_round = R13
completed_loop = 92
next_round = R1
next_loop = 93
round_schedule_status = valid
round_sector_consistency = pass
production_scoring_changed = false
shadow_weight_only = true
```

## 13. Final one-line contribution

```text
This R13 loop reviews 36 loop92 triggers across R1~R12, adds 0 new independent cases, and confirms that bridge-missing / price-MFE / spillover / late-spike / data-quality / false-overblock / hard-4C / Green-exact-evidence guards should remain hard Watch/4B/4C barriers or override checks before any Yellow/Green promotion.
```
