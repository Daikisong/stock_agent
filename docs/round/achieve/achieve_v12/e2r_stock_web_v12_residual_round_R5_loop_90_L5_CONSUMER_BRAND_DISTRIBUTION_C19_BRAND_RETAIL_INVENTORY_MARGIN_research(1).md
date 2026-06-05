# E2R Stock-Web v12 Residual Research — R5 Loop 90 / L5 / C19

```yaml
schema_family: v12_sector_archetype_residual
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
round: R5
loop: 90
large_sector_id: L5_CONSUMER_BRAND_DISTRIBUTION
canonical_archetype_id: C19_BRAND_RETAIL_INVENTORY_MARGIN
fine_archetype_id: BEAUTY_BRAND_CHANNEL_INVENTORY_MARGIN_BRIDGE_VS_APPAREL_BRAND_INVENTORY_DESTOCKING_DECAY
sector: consumer / brand / retail / apparel / beauty / inventory / margin bridge
output_file: e2r_stock_web_v12_residual_round_R5_loop_90_L5_CONSUMER_BRAND_DISTRIBUTION_C19_BRAND_RETAIL_INVENTORY_MARGIN_research.md
production_scoring_changed: false
shadow_weight_only: true
stock_agent_code_accessed: false
handoff_prompt_embedded: true
handoff_prompt_executed_now: false
```

## 1. Scope lock

This run follows the v12 sequential scheduler after completed `R4 loop 90`.

```text
scheduled_round = R5
scheduled_loop = 90
large_sector_id = L5_CONSUMER_BRAND_DISTRIBUTION
canonical_archetype_id = C19_BRAND_RETAIL_INVENTORY_MARGIN
```

R5 is restricted to consumer / brand / distribution.  
C19 is selected because the recent R5 sequence moved through:

```text
R5 loop86: C18_CONSUMER_EXPORT_CHANNEL_REORDER
R5 loop87: C19_BRAND_RETAIL_INVENTORY_MARGIN
R5 loop88: C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION
R5 loop89: C18_CONSUMER_EXPORT_CHANNEL_REORDER
```

After C18, the R5 lane returns to C19.

No-Repeat Index snapshot:

```text
C19_BRAND_RETAIL_INVENTORY_MARGIN
rows = 38
symbols = 13
good/bad Stage2 = 8/9
4B/4C = 3/0
top-covered = 282330, 004170, 007070, 093050, 337930, 139480
```

This loop avoids the C19 top-covered symbols and recent R5 loop symbols:

```text
R5 loop86 C18: 003230, 005610, 007310
R5 loop87 C19: 069960, 008770, 031430
R5 loop88 C20: 352480, 237880, 018250
R5 loop89 C18: 005180, 101530, 248170
```

Candidate hygiene note:

```text
During this execution path, an R4/C16 materials file was accidentally regenerated once.
That file is not the valid output for this user request. The valid scheduled output is this R5/C19/loop90 MD.
```

Selected symbols:

```text
090430, 383220, 020000
```

This loop tests:

```text
beauty brand channel inventory / margin repair bridge
vs
apparel brand inventory destocking rebound without sell-through / margin bridge
vs
premium apparel retail rebound without inventory turn, sell-through and margin/cash bridge
```

This is not a live stock recommendation, not a `stock_agent` code patch, and not a production scoring change.

## 2. Price atlas validation

```jsonl
{"row_type":"price_source_validation","source_name":"FinanceData/marcap via Songdaiki/stock-web","price_data_source":"Songdaiki/stock-web","upstream_source":"FinanceData/marcap","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","manifest_min_date":"1995-05-02","manifest_max_date":"2026-02-20","tradable_row_count":14354401,"raw_row_count":15214118,"symbol_count":5414,"active_like_symbol_count":2868,"corporate_action_candidate_count":14435,"calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","notes":"Raw/unadjusted OHLC; zero-volume and invalid OHLC rows are excluded from tradable shards; corporate-action-contaminated windows are blocked by default."}
{"row_type":"price_source_validation","symbol":"090430","company_name":"아모레퍼시픽","profile_path":"atlas/symbol_profiles/090/090430.json","first_date":"2006-06-29","last_date":"2026-02-20","trading_day_count":4834,"corporate_action_candidate_count":1,"corporate_action_candidate_dates":["2015-05-08"],"has_major_raw_discontinuity":true,"calibration_caveat":"Historical corporate-action candidate exists long before selected 2024 forward window.","status_inferred":"active_like","price_adjustment_status":"raw_unadjusted_marcap","profile_check":"2024_forward_window_clean_for_selected_entry"}
{"row_type":"price_source_validation","symbol":"383220","company_name":"F&F","profile_path":"atlas/symbol_profiles/383/383220.json","first_date":"2021-05-21","last_date":"2026-02-20","trading_day_count":1161,"corporate_action_candidate_count":1,"corporate_action_candidate_dates":["2022-04-13"],"has_major_raw_discontinuity":true,"calibration_caveat":"Historical corporate-action candidate exists before selected 2024 forward window.","status_inferred":"active_like","price_adjustment_status":"raw_unadjusted_marcap","profile_check":"2024_forward_window_clean_for_selected_entry"}
{"row_type":"price_source_validation","symbol":"020000","company_name":"한섬","profile_path":"atlas/symbol_profiles/020/020000.json","first_date":"1996-07-11","last_date":"2026-02-20","trading_day_count":7381,"corporate_action_candidate_count":4,"corporate_action_candidate_dates":["1997-01-03","1999-07-26","2003-07-15","2008-01-16"],"has_major_raw_discontinuity":true,"calibration_caveat":"Historical corporate-action candidates exist before selected 2024 forward window. 2024 share-count drift is visible in the selected year rows and is kept as data-quality watch.","status_inferred":"active_like","price_adjustment_status":"raw_unadjusted_marcap","profile_check":"2024_forward_window_usable_with_share_count_drift_watch"}
```

## 3. No-repeat and novelty check

No-Repeat Index is used only as a duplicate-avoidance ledger.  
Hard duplicate key applied:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

New keys introduced:

```jsonl
{"row_type":"narrative_only","check":"no_repeat_key","canonical_archetype_id":"C19_BRAND_RETAIL_INVENTORY_MARGIN","symbol":"090430","trigger_type":"Stage2-Actionable-BeautyBrandChannelInventoryMarginBridge-Positive","entry_date":"2024-04-12","duplicate_status":"new C19 symbol/trigger/date combination outside top-covered and previous R5 loop symbols"}
{"row_type":"narrative_only","check":"no_repeat_key","canonical_archetype_id":"C19_BRAND_RETAIL_INVENTORY_MARGIN","symbol":"383220","trigger_type":"Stage2-FalsePositive-ApparelBrandInventoryDestockingRebound-NoSellthroughMarginBridge","entry_date":"2024-04-01","duplicate_status":"new C19 symbol/trigger/date combination outside top-covered and previous R5 loop symbols"}
{"row_type":"narrative_only","check":"no_repeat_key","canonical_archetype_id":"C19_BRAND_RETAIL_INVENTORY_MARGIN","symbol":"020000","trigger_type":"Stage2-FalsePositive-PremiumApparelRetailRebound-NoInventoryTurnMarginBridge","entry_date":"2024-02-07","duplicate_status":"new C19 symbol/trigger/date combination outside top-covered and previous R5 loop symbols; share-count drift watch"}
```

## 4. Research question

C19 is not “소비재/브랜드 주가가 반등했다.”  
The useful brand/retail signal must prove the inventory-to-margin chain:

```text
channel inventory normalization
sell-through
discount rate reduction
brand pricing
SKU / product mix
offline/online channel quality
gross-margin repair
working-capital discipline
cash conversion
```

A retail rebound without this bridge is a full display shelf in a quiet store. The product is visible, but the register has not yet rung.

Residual question:

```text
Can C19 distinguish:
1. beauty-brand channel inventory and margin repair with high MFE and tolerable entry MAE,
2. apparel-brand rebound where inventory destocking and sell-through are not confirmed,
3. premium apparel retail rebound where share-count/data-quality watch plus weak MFE means no Yellow/Green promotion?
```

## 5. Case rows

```jsonl
{"row_type":"case","case_id":"C19_R5L90_090430_AMORE_BEAUTY_CHANNEL_MARGIN","symbol":"090430","company_name":"아모레퍼시픽","round":"R5","loop":"90","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C19_BRAND_RETAIL_INVENTORY_MARGIN","fine_archetype_id":"BEAUTY_BRAND_CHANNEL_INVENTORY_MARGIN_BRIDGE","case_type":"structural_success_watch","positive_or_counterexample":"positive","best_trigger":"Stage2-Actionable-BeautyBrandChannelInventoryMarginBridge-Positive","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"positive_high_MFE90_tolerable_MAE_late_drawdown_watch","current_profile_verdict":"current_profile_correct_if_channel_inventory_sellthrough_margin_bridge_required","price_source":"Songdaiki/stock-web","notes":"Beauty-brand channel inventory/margin proxy produced high MFE90 with tolerable early MAE. Late drawdown keeps Green strict and requires exact inventory, sell-through, discount-rate and margin evidence."}
{"row_type":"case","case_id":"C19_R5L90_383220_FNF_APPAREL_INVENTORY_DESTOCKING","symbol":"383220","company_name":"F&F","round":"R5","loop":"90","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C19_BRAND_RETAIL_INVENTORY_MARGIN","fine_archetype_id":"APPAREL_BRAND_INVENTORY_DESTOCKING_REBOUND_WITHOUT_SELLTHROUGH_MARGIN_BRIDGE","case_type":"failed_entry","positive_or_counterexample":"counterexample","best_trigger":"Stage2-FalsePositive-ApparelBrandInventoryDestockingRebound-NoSellthroughMarginBridge","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"counterexample_near_zero_MFE_deep_MAE_no_inventory_margin_bridge","current_profile_verdict":"current_profile_false_positive_if_apparel_brand_rebound_overcredited","price_source":"Songdaiki/stock-web","notes":"Apparel brand rebound had only price-only local MFE and then deep MAE, with no confirmed sell-through, inventory turn, discount-rate or margin bridge."}
{"row_type":"case","case_id":"C19_R5L90_020000_HANSOME_PREMIUM_APPAREL_REBOUND","symbol":"020000","company_name":"한섬","round":"R5","loop":"90","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C19_BRAND_RETAIL_INVENTORY_MARGIN","fine_archetype_id":"PREMIUM_APPAREL_RETAIL_REBOUND_WITHOUT_INVENTORY_TURN_MARGIN_BRIDGE","case_type":"failed_entry","positive_or_counterexample":"counterexample","best_trigger":"Stage2-FalsePositive-PremiumApparelRetailRebound-NoInventoryTurnMarginBridge","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":0.9,"score_price_alignment":"counterexample_near_zero_MFE_deep_MAE_share_count_watch","current_profile_verdict":"current_profile_false_positive_if_premium_apparel_rebound_overcredited","price_source":"Songdaiki/stock-web","notes":"Premium apparel retail rebound had near-zero MFE and deep MAE without inventory turn, sell-through, gross-margin or cash bridge. 2024 share-count drift keeps data-quality watch."}
```

## 6. Trigger-level Stock-Web rows

### 6.1 090430 아모레퍼시픽 — beauty-brand channel inventory / margin bridge positive

Entry row: `2024-04-12 c=135000`.  
Observed path: low `2024-04-12 l=125800`, peak `2024-05-31 h=200500`, and late-year low `2024-12-09 l=99500`.

```jsonl
{"row_type":"trigger","trigger_id":"R5L90_C19_090430_20240412_STAGE2_BEAUTY_CHANNEL_MARGIN","case_id":"C19_R5L90_090430_AMORE_BEAUTY_CHANNEL_MARGIN","symbol":"090430","company_name":"아모레퍼시픽","round":"R5","loop":"90","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C19_BRAND_RETAIL_INVENTORY_MARGIN","fine_archetype_id":"BEAUTY_BRAND_CHANNEL_INVENTORY_MARGIN_BRIDGE","loop_objective":"holdout_validation;canonical_archetype_rule_candidate;green_strictness_stress_test","trigger_type":"Stage2-Actionable-BeautyBrandChannelInventoryMarginBridge-Positive","trigger_date":"2024-04-12","entry_date":"2024-04-12","entry_price":135000.0,"entry_price_basis":"close","evidence_available_at_that_date":"historical_public_beauty_brand_channel_inventory_margin_proxy_available_by_entry","evidence_source":"source-name-level proxy; exact URL pending; beauty-brand channel inventory, sell-through and margin bridge treated as non-price proxy, not final citation-grade evidence","evidence_source_type":"historical_public_report_consensus_proxy","source_proxy_only":true,"evidence_url_pending":true,"stage2_evidence_fields":["channel_inventory_normalization_proxy","sellthrough_proxy","gross_margin_repair_proxy","relative_strength_turn"],"stage3_evidence_fields":["exact_inventory_turn_source_pending","discount_rate_source_pending","channel_quality_source_pending","cash_conversion_pending"],"stage4b_evidence_fields":["price_extension_watch","late_drawdown_watch"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/090/090430/2024.csv","profile_path":"atlas/symbol_profiles/090/090430.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":42.96,"MFE_90D_pct":48.52,"MFE_180D_pct":48.52,"MAE_30D_pct":-6.81,"MAE_90D_pct":-6.81,"MAE_180D_pct":-26.30,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-05-31","peak_price":200500.0,"max_drawdown_low_date":"2024-12-09","max_drawdown_low":99500.0,"drawdown_after_peak_pct":-50.37,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"positive_but_late_drawdown_blocks_Green_without_exact_inventory_sellthrough_margin_cash_evidence","four_b_evidence_type":["price_extension_watch","late_drawdown_watch"],"four_c_protection_label":"not_applicable","trigger_outcome_label":"positive_high_MFE90_tolerable_MAE_late_drawdown_watch","current_profile_verdict":"current_profile_correct_if_channel_inventory_sellthrough_margin_bridge_required","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"historical_candidate_pre_2024; selected_window_clean","same_entry_group_id":"090430_2024-04-12_135000","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"current_profile_residual":"C19 can allow Stage2/Yellow when brand strength is tied to inventory normalization, sell-through, discount-rate improvement, gross-margin repair and cash conversion. Green requires exact source-grade evidence."}
```

### 6.2 383220 F&F — apparel brand inventory destocking rebound without sell-through/margin bridge

Entry row: `2024-04-01 c=76500`.  
Observed path: same-day high `2024-04-01 h=77400`, then lows to `2024-12-09 l=47250`.

```jsonl
{"row_type":"trigger","trigger_id":"R5L90_C19_383220_20240401_STAGE2_FALSE_POSITIVE_APPAREL_INVENTORY","case_id":"C19_R5L90_383220_FNF_APPAREL_INVENTORY_DESTOCKING","symbol":"383220","company_name":"F&F","round":"R5","loop":"90","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C19_BRAND_RETAIL_INVENTORY_MARGIN","fine_archetype_id":"APPAREL_BRAND_INVENTORY_DESTOCKING_REBOUND_WITHOUT_SELLTHROUGH_MARGIN_BRIDGE","loop_objective":"residual_false_positive_mining;counterexample_mining;4B_non_price_requirement_stress_test","trigger_type":"Stage2-FalsePositive-ApparelBrandInventoryDestockingRebound-NoSellthroughMarginBridge","trigger_date":"2024-04-01","entry_date":"2024-04-01","entry_price":76500.0,"entry_price_basis":"close","evidence_available_at_that_date":"historical_public_apparel_brand_inventory_destocking_rebound_proxy_available_by_entry","evidence_source":"source-name-level proxy; exact URL pending; apparel-brand rebound treated as insufficient without sell-through, inventory turn, discount-rate, gross-margin and cash bridge","evidence_source_type":"historical_public_report_news_proxy","source_proxy_only":true,"evidence_url_pending":true,"stage2_evidence_fields":["apparel_brand_rebound","inventory_destocking_keyword","relative_strength_rebound"],"stage3_evidence_fields":["sellthrough_bridge_missing","inventory_turn_bridge_missing","discount_rate_missing","margin_cash_bridge_missing"],"stage4b_evidence_fields":["price_only_near_zero_MFE","inventory_margin_bridge_missing_watch","deep_MAE"],"stage4c_evidence_fields":["thesis_break_watch_only"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/383/383220/2024.csv","profile_path":"atlas/symbol_profiles/383/383220.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":1.18,"MFE_90D_pct":1.18,"MFE_180D_pct":1.18,"MAE_30D_pct":-19.35,"MAE_90D_pct":-24.58,"MAE_180D_pct":-38.24,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-04-01","peak_price":77400.0,"max_drawdown_low_date":"2024-12-09","max_drawdown_low":47250.0,"drawdown_after_peak_pct":-38.95,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"apparel_brand_rebound_without_sellthrough_inventory_margin_bridge_should_be_4B_watch_not_positive","four_b_evidence_type":["price_only","inventory_margin_bridge_missing_watch","deep_MAE"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"counterexample_near_zero_MFE_deep_MAE_no_inventory_margin_bridge","current_profile_verdict":"current_profile_false_positive_if_apparel_brand_rebound_overcredited","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"historical_candidate_pre_2024; selected_window_clean","same_entry_group_id":"383220_2024-04-01_76500","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"current_profile_residual":"C19 should not promote apparel-brand rebound without sell-through, inventory turn, discount-rate reduction, gross-margin repair and cash conversion. Near-zero MFE and deep MAE require 4B-watch."}
```

### 6.3 020000 한섬 — premium apparel retail rebound without inventory-turn/margin bridge

Entry row: `2024-02-07 c=21550`.  
Observed path: same-day high `2024-02-07 h=21650`, low `2024-04-08 l=18880`, and later low around `2024-10-25 l=15700`.

```jsonl
{"row_type":"trigger","trigger_id":"R5L90_C19_020000_20240207_STAGE2_FALSE_POSITIVE_PREMIUM_APPAREL","case_id":"C19_R5L90_020000_HANSOME_PREMIUM_APPAREL_REBOUND","symbol":"020000","company_name":"한섬","round":"R5","loop":"90","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C19_BRAND_RETAIL_INVENTORY_MARGIN","fine_archetype_id":"PREMIUM_APPAREL_RETAIL_REBOUND_WITHOUT_INVENTORY_TURN_MARGIN_BRIDGE","loop_objective":"residual_false_positive_mining;counterexample_mining;data_quality_watch","trigger_type":"Stage2-FalsePositive-PremiumApparelRetailRebound-NoInventoryTurnMarginBridge","trigger_date":"2024-02-07","entry_date":"2024-02-07","entry_price":21550.0,"entry_price_basis":"close","evidence_available_at_that_date":"historical_public_premium_apparel_retail_rebound_proxy_available_by_entry","evidence_source":"source-name-level proxy; exact URL pending; premium apparel retail rebound treated as insufficient without inventory turn, sell-through, gross-margin and working-capital bridge","evidence_source_type":"historical_public_report_news_proxy","source_proxy_only":true,"evidence_url_pending":true,"stage2_evidence_fields":["premium_apparel_rebound","retail_inventory_keyword"],"stage3_evidence_fields":["inventory_turn_missing","sellthrough_missing","gross_margin_repair_missing","cash_conversion_missing"],"stage4b_evidence_fields":["near_zero_MFE","share_count_drift_watch","inventory_margin_bridge_missing_watch"],"stage4c_evidence_fields":["thesis_break_watch_only"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/020/020000/2024.csv","profile_path":"atlas/symbol_profiles/020/020000.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":0.46,"MFE_90D_pct":0.46,"MFE_180D_pct":0.46,"MAE_30D_pct":-12.39,"MAE_90D_pct":-12.39,"MAE_180D_pct":-27.15,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-02-07","peak_price":21650.0,"max_drawdown_low_date":"2024-10-25","max_drawdown_low":15700.0,"drawdown_after_peak_pct":-27.48,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"premium_apparel_rebound_without_inventory_turn_margin_bridge_should_be_4B_watch_not_positive; share_count_drift_watch_before_patch","four_b_evidence_type":["near_zero_MFE","share_count_drift_watch","inventory_margin_bridge_missing_watch"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"counterexample_near_zero_MFE_deep_MAE_share_count_watch","current_profile_verdict":"current_profile_false_positive_if_premium_apparel_rebound_overcredited","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":["2024_share_count_drift_watch"],"corporate_action_window_status":"historical_candidates_pre_2024; selected_window_usable_with_share_count_drift_watch","same_entry_group_id":"020000_2024-02-07_21550","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":0.9,"do_not_count_as_new_case":false,"current_profile_residual":"C19 should not promote premium apparel rebound without inventory turn, sell-through, margin and cash bridge. 2024 share-count drift requires data-quality repair before patch consideration."}
```

## 7. Score simulation rows

```jsonl
{"row_type":"score_simulation","profile_id":"P0_e2r_2_1_stock_web_calibrated_proxy","case_id":"C19_R5L90_090430_AMORE_BEAUTY_CHANNEL_MARGIN","trigger_id":"R5L90_C19_090430_20240412_STAGE2_BEAUTY_CHANNEL_MARGIN","symbol":"090430","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C19_BRAND_RETAIL_INVENTORY_MARGIN","profile_scope":"current_default_proxy","profile_hypothesis":"current profile works if C19 requires channel inventory normalization, sell-through, discount-rate repair, gross-margin improvement and cash bridge rather than consumer brand rebound alone","raw_component_scores_before":{"channel_inventory_score":13,"sellthrough_score":12,"discount_rate_score":10,"brand_pricing_score":11,"SKU_mix_score":10,"gross_margin_score":12,"cash_conversion_score":7,"relative_strength_score":14,"valuation_repricing_score":8,"execution_risk_score":-5,"theme_spike_risk":-2,"information_confidence":5},"weighted_score_before":74,"stage_label_before":"Stage2-Actionable/Yellow-Watch","raw_component_scores_after":{"channel_inventory_score":16,"sellthrough_score":15,"discount_rate_score":12,"brand_pricing_score":13,"SKU_mix_score":12,"gross_margin_score":15,"cash_conversion_score":9,"relative_strength_score":15,"valuation_repricing_score":9,"execution_risk_score":-4,"theme_spike_risk":-1,"information_confidence":6},"weighted_score_after":87,"stage_label_after":"Stage3-Yellow/Green-candidate-watch","component_delta_explanation":"Beauty channel inventory/margin bridge plus high MFE90 supports Yellow/Green-candidate watch; exact sell-through and margin evidence blocks automatic Green."}
{"row_type":"score_simulation","profile_id":"P0_e2r_2_1_stock_web_calibrated_proxy","case_id":"C19_R5L90_383220_FNF_APPAREL_INVENTORY_DESTOCKING","trigger_id":"R5L90_C19_383220_20240401_STAGE2_FALSE_POSITIVE_APPAREL_INVENTORY","symbol":"383220","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C19_BRAND_RETAIL_INVENTORY_MARGIN","profile_scope":"current_default_proxy","profile_hypothesis":"apparel brand rebound without sell-through and inventory-turn bridge should be blocked","raw_component_scores_before":{"channel_inventory_score":2,"sellthrough_score":0,"discount_rate_score":0,"brand_pricing_score":2,"SKU_mix_score":1,"gross_margin_score":0,"cash_conversion_score":0,"relative_strength_score":6,"valuation_repricing_score":3,"execution_risk_score":-14,"theme_spike_risk":-16,"information_confidence":3},"weighted_score_before":0,"stage_label_before":"Stage2-Watch/FalsePositive","raw_component_scores_after":{"channel_inventory_score":0,"sellthrough_score":0,"discount_rate_score":0,"brand_pricing_score":1,"SKU_mix_score":0,"gross_margin_score":0,"cash_conversion_score":0,"relative_strength_score":1,"valuation_repricing_score":0,"execution_risk_score":-22,"theme_spike_risk":-20,"information_confidence":2},"weighted_score_after":0,"stage_label_after":"Stage1/4B-Watch","component_delta_explanation":"Near-zero MFE and deep MAE convert apparel rebound into missing sell-through/margin bridge failure."}
{"row_type":"score_simulation","profile_id":"P0_e2r_2_1_stock_web_calibrated_proxy","case_id":"C19_R5L90_020000_HANSOME_PREMIUM_APPAREL_REBOUND","trigger_id":"R5L90_C19_020000_20240207_STAGE2_FALSE_POSITIVE_PREMIUM_APPAREL","symbol":"020000","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C19_BRAND_RETAIL_INVENTORY_MARGIN","profile_scope":"current_default_proxy","profile_hypothesis":"premium apparel rebound without inventory-turn and margin bridge should remain Watch/4B, especially with share-count drift watch","raw_component_scores_before":{"channel_inventory_score":2,"sellthrough_score":0,"discount_rate_score":0,"brand_pricing_score":2,"SKU_mix_score":1,"gross_margin_score":0,"cash_conversion_score":0,"relative_strength_score":4,"valuation_repricing_score":2,"execution_risk_score":-12,"theme_spike_risk":-14,"information_confidence":2},"weighted_score_before":0,"stage_label_before":"Stage2-Watch/FalsePositive/DataQualityWatch","raw_component_scores_after":{"channel_inventory_score":0,"sellthrough_score":0,"discount_rate_score":0,"brand_pricing_score":1,"SKU_mix_score":0,"gross_margin_score":0,"cash_conversion_score":0,"relative_strength_score":1,"valuation_repricing_score":0,"execution_risk_score":-20,"theme_spike_risk":-18,"information_confidence":1},"weighted_score_after":0,"stage_label_after":"Stage1/4B-Watch/DataQualityWatch","component_delta_explanation":"Near-zero MFE, deep MAE and share-count drift watch block Yellow/Green until inventory and price-path evidence are repaired."}
```

## 8. Profile comparison

```jsonl
{"row_type":"profile_comparison","comparison_id":"R5L90_C19_P0_CURRENT","round":"R5","loop":"90","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C19_BRAND_RETAIL_INVENTORY_MARGIN","profile_id":"P0_e2r_2_1_stock_web_calibrated_proxy","profile_scope":"current_default_proxy","profile_hypothesis":"global guardrails help but C19 needs explicit channel-inventory, sell-through, discount-rate, gross-margin, cash and apparel inventory 4B taxonomy","eligible_trigger_count":3,"avg_MFE90_pct":16.72,"avg_MAE90_pct":-14.59,"avg_MFE180_pct":16.72,"avg_MAE180_pct":-30.56,"false_positive_rate":0.67,"missed_structural_count":0,"late_green_count":0,"avg_four_b_local_peak_proximity":1.0,"avg_four_b_full_window_peak_proximity":1.0,"score_return_alignment_verdict":"mixed_without_C19_inventory_sellthrough_margin_cash_bridge_guard"}
{"row_type":"profile_comparison","comparison_id":"R5L90_C19_P1_SECTOR_SPECIFIC","round":"R5","loop":"90","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C19_BRAND_RETAIL_INVENTORY_MARGIN","profile_id":"P1_L5_brand_inventory_margin_bridge_candidate","profile_scope":"sector_specific","profile_hypothesis":"L5 brand/retail signals need inventory turn, sell-through, discount-rate repair, SKU mix, gross margin or cash conversion before Stage2-Actionable","changed_axes":["inventory_turn_required","sellthrough_margin_required","apparel_rebound_penalty"],"changed_thresholds":{"stage2_actionable_bridge_min":"one_of_inventory_turn_sellthrough_discount_rate_SKU_mix_margin_or_cash_proxy"},"eligible_trigger_count":3,"avg_MFE90_pct":16.72,"avg_MAE90_pct":-14.59,"avg_MFE180_pct":16.72,"avg_MAE180_pct":-30.56,"false_positive_rate":0.33,"score_return_alignment_verdict":"better_if_exact_evidence_repaired"}
{"row_type":"profile_comparison","comparison_id":"R5L90_C19_P2_CANONICAL","round":"R5","loop":"90","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C19_BRAND_RETAIL_INVENTORY_MARGIN","profile_id":"P2_C19_inventory_sellthrough_margin_guard","profile_scope":"canonical_archetype_specific","profile_hypothesis":"C19 should reward inventory-to-margin mechanics, not apparel or brand rebound labels","changed_axes":["C19_inventory_sellthrough_margin_cash_bridge_required","C19_apparel_rebound_local_4B_guard","C19_share_count_drift_data_quality_watch"],"changed_thresholds":{"stage2_yellow_gate":"inventory_normalization_or_sellthrough_plus_margin_or_cash_bridge_required"},"eligible_trigger_count":3,"avg_MFE90_pct":16.72,"avg_MAE90_pct":-14.59,"avg_MFE180_pct":16.72,"avg_MAE180_pct":-30.56,"false_positive_rate":0.0,"score_return_alignment_verdict":"best_local_shadow_candidate"}
{"row_type":"profile_comparison","comparison_id":"R5L90_C19_P3_COUNTEREXAMPLE_GUARD","round":"R5","loop":"90","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C19_BRAND_RETAIL_INVENTORY_MARGIN","profile_id":"P3_C19_low_MFE_deep_MAE_guard","profile_scope":"counterexample_guard","profile_hypothesis":"If inventory/sell-through bridge is missing, MFE90<5 or MAE180<=-25 should block Yellow/Green and route to 4B-watch","changed_axes":["C19_low_MFE_guardrail","C19_deep_MAE_4B_guardrail","C19_share_count_drift_watch_guardrail"],"changed_thresholds":{"bad_entry_filter":"bridge_missing_and_(MFE90_lt_5_or_MAE180_le_minus_25)"},"eligible_trigger_count":3,"avg_MFE90_pct":16.72,"avg_MAE90_pct":-14.59,"avg_MFE180_pct":16.72,"avg_MAE180_pct":-30.56,"false_positive_rate":0.0,"score_return_alignment_verdict":"safe_guardrail_candidate"}
```

## 9. Aggregate, transition, and coverage rows

```jsonl
{"row_type":"aggregate_metric","round":"R5","loop":"90","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C19_BRAND_RETAIL_INVENTORY_MARGIN","fine_archetype_id":"C19_BEAUTY_CHANNEL_MARGIN_POSITIVE_VS_APPAREL_INVENTORY_DECAY","row_count":3,"unique_symbol_count":3,"positive_case_count":1,"counterexample_count":2,"good_stage2_count":1,"bad_stage2_count":2,"4B_case_count":2,"4C_case_count":0,"source_proxy_only_count":3,"evidence_url_pending_count":3,"calibration_usable_count":3,"avg_MFE90_pct":16.72,"avg_MAE90_pct":-14.59,"avg_MFE180_pct":16.72,"avg_MAE180_pct":-30.56,"stage2_hit_rate_MFE90_ge20":0.33,"stage2_bad_entry_rate_bridge_missing":0.67,"stage2_bad_entry_rate_MFE90_lt5":0.67,"interpretation":"C19 needs bridge discipline. 아모레퍼시픽 shows beauty-channel inventory and gross-margin repair can support Yellow/Green-candidate-watch, while F&F and 한섬 show apparel/retail rebounds should not be promoted without inventory turn, sell-through, discount-rate repair, margin and cash evidence."}
{"row_type":"stage_transition_summary","round":"R5","loop":"90","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C19_BRAND_RETAIL_INVENTORY_MARGIN","symbol":"090430","trigger_type":"Stage2-Actionable-BeautyBrandChannelInventoryMarginBridge-Positive","entry_date":"2024-04-12","stage2_to_90D_outcome":"good_stage2_high_MFE_tolerable_MAE","stage2_to_180D_outcome":"positive_inventory_margin_bridge_but_late_drawdown_Green_strict","MFE90_ge20":true,"MAE90_le_minus20":false,"transition_note":"Allow Stage2/Yellow when brand strength is tied to inventory normalization, sell-through, discount-rate and margin bridge; Green requires exact evidence."}
{"row_type":"stage_transition_summary","round":"R5","loop":"90","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C19_BRAND_RETAIL_INVENTORY_MARGIN","symbol":"383220","trigger_type":"Stage2-FalsePositive-ApparelBrandInventoryDestockingRebound-NoSellthroughMarginBridge","entry_date":"2024-04-01","stage2_to_90D_outcome":"bad_stage2_near_zero_MFE_deep_MAE","stage2_to_180D_outcome":"failed_apparel_rebound_deep_MAE","MFE90_ge20":false,"MAE180_le_minus25":true,"transition_note":"Apparel rebound without sell-through/inventory-margin bridge should stay Watch/4B-risk."}
{"row_type":"stage_transition_summary","round":"R5","loop":"90","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C19_BRAND_RETAIL_INVENTORY_MARGIN","symbol":"020000","trigger_type":"Stage2-FalsePositive-PremiumApparelRetailRebound-NoInventoryTurnMarginBridge","entry_date":"2024-02-07","stage2_to_90D_outcome":"bad_stage2_near_zero_MFE_bridge_missing","stage2_to_180D_outcome":"failed_premium_apparel_rebound_deep_MAE_data_quality_watch","MFE90_ge20":false,"MAE180_le_minus25":true,"transition_note":"Premium apparel rebound without inventory turn and margin bridge should remain Watch/4B-risk; share-count drift requires data-quality watch."}
{"row_type":"residual_contribution","round":"R5","loop":"90","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C19_BRAND_RETAIL_INVENTORY_MARGIN","residual_type":"apparel_brand_rebound_overcredit_without_inventory_sellthrough_margin_cash_bridge","contribution":"Adds two C19 4B counterexamples against one beauty-channel inventory/margin positive, avoiding C19 top-covered and recent R5 loop symbols.","needs_coding_agent":true,"handoff_priority":"medium"}
{"row_type":"coverage_matrix","round":"R5","loop":"90","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C19_BRAND_RETAIL_INVENTORY_MARGIN","fine_archetype_id":"BEAUTY_BRAND_CHANNEL_INVENTORY_MARGIN_BRIDGE_VS_APPAREL_BRAND_INVENTORY_DESTOCKING_DECAY","positive_case_count":1,"counterexample_count":2,"4B_case_count":2,"4C_case_count":0,"new_independent_case_count":3,"reused_case_count":0,"calibration_usable_trigger_count":3,"representative_trigger_count":3,"current_profile_error_count":2,"sector_rule_candidate":false,"canonical_rule_candidate":true,"coverage_gap_after_this_loop":"C19 now has non-top-symbol beauty channel-margin positive and two apparel inventory weak-bridge counterexamples; next R5 C19 loops should exact-URL repair inventory turn, sell-through, discount-rate, brand pricing, SKU mix, margin and cash-conversion evidence."}
```

## 10. Shadow rule candidates

```jsonl
{"row_type":"shadow_weight","round":"R5","loop":"90","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C19_BRAND_RETAIL_INVENTORY_MARGIN","axis":"C19_inventory_sellthrough_margin_cash_bridge_required","scope":"canonical_archetype","candidate_delta":1.0,"direction":"tighten","apply_now":false,"shadow_only":true,"evidence_basis":"090430 worked when channel inventory/margin proxy existed; 383220 and 020000 failed when apparel/retail price action lacked sell-through, inventory turn, gross-margin and cash bridge."}
{"row_type":"shadow_weight","round":"R5","loop":"90","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C19_BRAND_RETAIL_INVENTORY_MARGIN","axis":"C19_apparel_rebound_local_4B_guard","scope":"canonical_archetype","candidate_delta":1.0,"direction":"guardrail","apply_now":false,"shadow_only":true,"evidence_basis":"Apparel rows showed near-zero MFE and deep 180D MAE when non-price inventory-margin evidence was missing."}
{"row_type":"shadow_weight","round":"R5","loop":"90","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C19_BRAND_RETAIL_INVENTORY_MARGIN","axis":"C19_share_count_drift_data_quality_watch","scope":"canonical_archetype","candidate_delta":1.0,"direction":"data_quality_guard","apply_now":false,"shadow_only":true,"evidence_basis":"020000 has 2024 share-count drift in the selected year row and should remain data-quality-watch before patch consideration."}
```

## 11. Residual Contribution Summary

```text
new_independent_case_count: 3
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 3
new_canonical_archetype_count: 0
new_fine_archetype_count: 1
new_trigger_family_count: 3
tested_existing_calibrated_axes:
  - price_only_blowoff_blocks_positive_stage
  - full_4b_requires_non_price_evidence
  - hard_4c_thesis_break_routes_to_4c
residual_error_types_found:
  - apparel_rebound_overcredit
  - brand_price_rebound_overcredit
  - inventory_turn_bridge_missing
  - sellthrough_margin_cash_bridge_missing
new_axis_proposed:
  - C19_inventory_sellthrough_margin_cash_bridge_required_shadow_only
  - C19_apparel_rebound_local_4B_guard_shadow_only
  - C19_share_count_drift_data_quality_watch_shadow_only
existing_axis_strengthened:
  - price_only_blowoff_blocks_positive_stage within C19
  - full_4b_requires_non_price_evidence within C19
  - hard_4c_thesis_break_routes_to_4c within C19
existing_axis_weakened: null
existing_axis_kept:
  - stage3_green_total_min
  - stage3_green_revision_min
sector_specific_rule_candidate: false
canonical_archetype_rule_candidate: true
no_new_signal_reason: null
loop_contribution_label: canonical_archetype_rule_candidate
do_not_propose_new_weight_delta: false
```

## 12. Data-quality caveat

All selected triggers use Stock-Web tradable raw OHLC rows.  
`020000` is calibration-usable but has a 2024 share-count drift visible in the selected year row, so any production patch should keep data-quality repair before consideration.  
The non-price evidence layer remains source-name/proxy level for all three rows.

```text
calibration_usable = true for price-path residual analysis
evidence_url_pending = true
source_proxy_only = true
data_quality_watch = true for 020000 share-count drift
promotion should prefer hold / data-quality repair until exact URLs are added
```

## 13. Deferred Coding Agent Handoff Prompt

```text
You are the coding agent for Songdaiki/stock_agent.

Do not execute this handoff during the research-writing session.

When a later batch implementation is requested:
1. Ingest this MD through run-v12-calibration.
2. Confirm all trigger rows validate with:
   - price_data_source=Songdaiki/stock-web
   - price_basis=tradable_raw
   - price_adjustment_status=raw_unadjusted_marcap
3. Confirm R5 / L5 / C19 round-sector consistency.
4. Check no hard duplicate exists by canonical_archetype_id + symbol + trigger_type + entry_date.
5. Confirm this loop avoided:
   - C19 top-covered symbols
   - previous R5 loop86 C18 symbols
   - previous R5 loop87 C19 symbols
   - previous R5 loop88 C20 symbols
   - previous R5 loop89 C18 symbols
6. Keep 020000 in share-count-drift data-quality watch before patch consideration.
7. If aggregate support remains stable after exact evidence URL repair, consider C19-scoped safe patch candidates:
   - C19_inventory_sellthrough_margin_cash_bridge_required
   - C19_apparel_rebound_local_4B_guard
   - C19_share_count_drift_data_quality_watch
8. Do not loosen Stage3-Green.
9. Do not use future MFE/MAE in runtime scoring.
10. Use this MD only for calibration profile planning.
```

## 14. Round state

```text
completed_round = R5
completed_loop = 90
next_round = R6
next_loop = 90
round_schedule_status = valid
round_sector_consistency = pass
production_scoring_changed = false
shadow_weight_only = true
```

## 15. Final one-line contribution

```text
This loop adds 3 new independent cases, 1 positive, 2 counterexamples, and 2 local 4B-watch rows for R5/L5_CONSUMER_BRAND_DISTRIBUTION/C19_BRAND_RETAIL_INVENTORY_MARGIN.
```
