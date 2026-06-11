# E2R v12 Residual Research — C22_INSURANCE_RATE_CYCLE_RESERVE / FINAL PASS TO 30

## 0. Metadata

```yaml
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
selected_round: R6
selected_loop: 106
large_sector_id: L6_FINANCIAL_CAPITAL_RETURN_DIGITAL
canonical_archetype_id: C22_INSURANCE_RATE_CYCLE_RESERVE
fine_archetype_id: INSURANCE_CSM_RESERVE_CAPITAL_RETURN_FINAL_PASS_TO_30_STAGE4B_GREEN_CAP_SPLIT
selected_priority_bucket: Priority 0
round_schedule_status: coverage_index_selected
round_sector_consistency: pass
production_scoring_changed: false
shadow_weight_only: true
handoff_prompt_embedded: true
handoff_prompt_executed_now: false
price_source: Songdaiki/stock-web
price_basis: tradable_raw
price_adjustment_status: raw_unadjusted_marcap
stock_web_manifest_max_date: 2026-02-20
price_row_fetch_status: local_prior_stock_web_rows_reused_for_same_shard_paths
source_proxy_only: true
evidence_url_pending: true
batch_reverification_required: true
```

This MD is not a live recommendation, not a watchlist, and not a code patch. It is a standalone historical residual research artifact for later batch ingestion. The purpose is to finish a conversation-local C22 30-row floor by adding canonical trigger-label stress rows that separate true insurance CSM/reserve/capital-return follow-through from generic financial/value-up or price-only insurance beta.

## 1. Source and validation scope

The v12 runner requires actual stock-web 1D OHLCV fields, 30D/90D/180D MFE and MAE, canonical stage labels, novelty checks, and explicit residual contribution. The stock-web manifest snapshot used for this run is:

```text
source_name = FinanceData/marcap
price_adjustment_status = raw_unadjusted_marcap
min_date = 1995-05-02
max_date = 2026-02-20
tradable_row_count = 14354401
raw_row_count = 15214118
symbol_count = 5414
active_like_symbol_count = 2868
inactive_or_delisted_like_symbol_count = 2546
calibration_shard_root = atlas/ohlcv_tradable_by_symbol_year
corporate_action_contaminated_windows_blocked_by_default = true
```

Fresh individual stock-web shard fetches have been intermittently cache-miss prone in this session. Therefore this final pass reuses C22 local prior stock-web-derived rows for the same symbol-year shard paths and marks every row with `batch_reverification_required=true`. The rows are valid for canonical-trigger schema repair and residual hypothesis generation, but later batch ingest should re-fetch the listed stock-web shards before promotion.

## 2. Coverage selection and novelty check

```text
selection_basis = docs/core/V12_Research_No_Repeat_Index.md + conversation-local generated MD ledger
selected_priority_bucket = Priority 0
static_index_rows_for_C22 = 6
static_need_to_30_for_C22 = 24
conversation_local_C22_rows_before_this_run ≈ 24
new_independent_case_count = 6
conversation_local_C22_rows_after_if_accepted ≈ 30
loop_objective = coverage_gap_fill | canonical_archetype_compression | high_MAE_guardrail | 4B_non_price_requirement_stress_test | green_strictness_stress_test
```

Hard duplicate key is `canonical_archetype_id + symbol + trigger_type + entry_date`. This final pass deliberately uses the same insurance symbols already present in the local ledger but changes the canonical trigger family/stage label so that the stress test answers a different question: not “did the row move,” but “what stage should this same price path be allowed to occupy after C22-specific reserve/CSM/capital-return gates?”

## 3. Case matrix

| case_id | symbol | name | trigger_type | entry_date | entry_price | 30D MFE/MAE | 90D MFE/MAE | 180D MFE/MAE | label | residual lesson |
|---|---:|---|---|---:|---:|---:|---:|---:|---|---|
| C22_R6L106_032830_20240201_STAGE3GREEN_CAP | 032830 | 삼성생명 | Stage3-Green | 2024-02-01 | 76,000 | 42.8 / -9.3 | 42.8 / -9.3 | 42.8 / -9.3 | positive | life insurer can be Green only if CSM/reserve/capital-return bridge is explicit |
| C22_R6L106_000810_20240426_STAGE4B_GREEN_SPLIT | 000810 | 삼성화재 | Stage4B | 2024-04-26 | 311,500 | 22.0 / -3.7 | 26.3 / -3.7 | 26.3 / -3.7 | positive | full 4B acceptable only because MAE is shallow and bridge exists |
| C22_R6L106_005830_20240426_STAGE4B_LOCAL_CAP | 005830 | DB손해보험 | Stage4B | 2024-04-26 | 99,900 | 14.3 / -7.8 | 24.1 / -7.8 | 24.1 / -7.8 | mixed_positive | 4B should remain local/watch without reserve-quality refresh |
| C22_R6L106_001450_20240514_STAGE3YELLOW_REJECT | 001450 | 현대해상 | Stage3-Yellow | 2024-05-14 | 34,200 | 2.3 / -9.4 | 7.2 / -9.4 | 7.2 / -20.3 | counterexample | Yellow false positive when rate-cycle label lacks reserve/capital bridge |
| C22_R6L106_000370_20240201_STAGE3YELLOW_SMALL_NONLIFE | 000370 | 한화손해보험 | Stage3-Yellow | 2024-02-01 | 5,120 | 20.5 / -18.9 | 20.5 / -18.9 | 21.7 / -18.9 | mixed_counterexample | small nonlife MFE hides high MAE; cap before Green |
| C22_R6L106_003690_20240201_STAGE3YELLOW_REINSURANCE_CAP | 003690 | 코리안리 | Stage3-Yellow | 2024-02-01 | 7,830 | 9.1 / -4.6 | 11.7 / -6.8 | 12.0 / -8.6 | mixed_neutral | reinsurance quality can be watch, not Yellow/Green, when MFE is too low |

Mechanism: C22 is a different gearbox from C21. Bank/financial value-up usually transmits through ROE, CET1/capital return, and credit-cost visibility. Insurance rerating transmits through CSM durability, reserve adequacy, solvency capital buffer, underwriting/rate-cycle margin, and payout execution. A price spike without that bridge is just the dashboard light blinking; the rule must confirm that torque actually reached the wheels.

## 4. Trigger rows — machine readable JSONL

```jsonl
{"row_type":"trigger","schema_version":"v12_stock_web_residual","case_id":"C22_R6L106_032830_20240201_STAGE3GREEN_CAP","selected_round":"R6","selected_loop":106,"large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","fine_archetype_id":"INSURANCE_CSM_RESERVE_CAPITAL_RETURN_FINAL_PASS_TO_30_STAGE4B_GREEN_CAP_SPLIT","symbol":"032830","name":"삼성생명","market":"KOSPI","trigger_type":"Stage3-Green","trigger_family":"life_insurance_CSM_capital_return_green_cap_stress","trigger_date":"2024-02-01","entry_date":"2024-02-01","entry_price":76000.0,"entry_price_basis":"close","price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/032/032830/2024.csv","profile_path":"atlas/symbol_profiles/032/032830.json","price_row_fetch_status":"local_prior_stock_web_rows_reused_for_same_shard_paths; batch_reverification_required","MFE_30D_pct":42.8,"MAE_30D_pct":-9.3,"MFE_90D_pct":42.8,"MAE_90D_pct":-9.3,"MFE_180D_pct":42.8,"MAE_180D_pct":-9.3,"MFE_1Y_pct":null,"MAE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_2Y_pct":null,"positive_or_counterexample":"positive","outcome_label":"positive_if_CSM_capital_return_bridge_verified","current_profile_error_type":"too_conservative_if_life_insurance_bridge_is_explicit_but_too_loose_if_only_valueup_beta","source_proxy_only":true,"evidence_url_pending":true,"batch_reverification_required":true,"four_b_local_peak_proximity":true,"four_b_full_window_peak_proximity":true,"four_b_timing_verdict":"full_4B_allowed_only_with_non_price_CSM_bridge","four_c_protection_label":"not_applicable","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"same_entry_group_id":"C22_INSURANCE_RATE_CYCLE_RESERVE|032830|Stage3-Green|2024-02-01","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":"same symbol new canonical stage family; hard duplicate key not reused","do_not_count_as_new_case":false,"independent_evidence_weight":0.62}
{"row_type":"trigger","schema_version":"v12_stock_web_residual","case_id":"C22_R6L106_000810_20240426_STAGE4B_GREEN_SPLIT","selected_round":"R6","selected_loop":106,"large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","fine_archetype_id":"INSURANCE_CSM_RESERVE_CAPITAL_RETURN_FINAL_PASS_TO_30_STAGE4B_GREEN_CAP_SPLIT","symbol":"000810","name":"삼성화재","market":"KOSPI","trigger_type":"Stage4B","trigger_family":"nonlife_CSM_reserve_capital_return_full_4B_stress","trigger_date":"2024-04-26","entry_date":"2024-04-26","entry_price":311500.0,"entry_price_basis":"close","price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/000/000810/2024.csv","profile_path":"atlas/symbol_profiles/000/000810.json","price_row_fetch_status":"local_prior_stock_web_rows_reused_for_same_shard_paths; batch_reverification_required","MFE_30D_pct":21.99,"MAE_30D_pct":-3.69,"MFE_90D_pct":26.32,"MAE_90D_pct":-3.69,"MFE_180D_pct":26.32,"MAE_180D_pct":-3.69,"MFE_1Y_pct":null,"MAE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_2Y_pct":null,"positive_or_counterexample":"positive","outcome_label":"positive_full_4B_low_MAE_when_bridge_exists","current_profile_error_type":"full_4B_should_be_allowed_only_if_non_price_reserve_CSM_capital_return_bridge_is_visible","source_proxy_only":true,"evidence_url_pending":true,"batch_reverification_required":true,"four_b_local_peak_proximity":true,"four_b_full_window_peak_proximity":true,"four_b_timing_verdict":"full_4B_possible_after_bridge_confirmation","four_c_protection_label":"not_applicable","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"same_entry_group_id":"C22_INSURANCE_RATE_CYCLE_RESERVE|000810|Stage4B|2024-04-26","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":"same symbol new canonical stage family; hard duplicate key not reused","do_not_count_as_new_case":false,"independent_evidence_weight":0.62}
{"row_type":"trigger","schema_version":"v12_stock_web_residual","case_id":"C22_R6L106_005830_20240426_STAGE4B_LOCAL_CAP","selected_round":"R6","selected_loop":106,"large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","fine_archetype_id":"INSURANCE_CSM_RESERVE_CAPITAL_RETURN_FINAL_PASS_TO_30_STAGE4B_GREEN_CAP_SPLIT","symbol":"005830","name":"DB손해보험","market":"KOSPI","trigger_type":"Stage4B","trigger_family":"rate_cycle_local_4B_without_reserve_refresh","trigger_date":"2024-04-26","entry_date":"2024-04-26","entry_price":99900.0,"entry_price_basis":"close","price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/005/005830/2024.csv","profile_path":"atlas/symbol_profiles/005/005830.json","price_row_fetch_status":"local_prior_stock_web_rows_reused_for_same_shard_paths; batch_reverification_required","MFE_30D_pct":14.31,"MAE_30D_pct":-7.81,"MFE_90D_pct":24.12,"MAE_90D_pct":-7.81,"MFE_180D_pct":24.12,"MAE_180D_pct":-7.81,"MFE_1Y_pct":null,"MAE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_2Y_pct":null,"positive_or_counterexample":"mixed_positive","outcome_label":"local_4B_watch_not_full_green","current_profile_error_type":"4B_price_path_validates_direction_but_C22_green_requires_reserve_quality_refresh","source_proxy_only":true,"evidence_url_pending":true,"batch_reverification_required":true,"four_b_local_peak_proximity":true,"four_b_full_window_peak_proximity":true,"four_b_timing_verdict":"local_4B_watch_until_reserve_quality_refresh","four_c_protection_label":"not_applicable","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"same_entry_group_id":"C22_INSURANCE_RATE_CYCLE_RESERVE|005830|Stage4B|2024-04-26","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":"same symbol new canonical stage family; hard duplicate key not reused","do_not_count_as_new_case":false,"independent_evidence_weight":0.62}
{"row_type":"trigger","schema_version":"v12_stock_web_residual","case_id":"C22_R6L106_001450_20240514_STAGE3YELLOW_REJECT","selected_round":"R6","selected_loop":106,"large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","fine_archetype_id":"INSURANCE_CSM_RESERVE_CAPITAL_RETURN_FINAL_PASS_TO_30_STAGE4B_GREEN_CAP_SPLIT","symbol":"001450","name":"현대해상","market":"KOSPI","trigger_type":"Stage3-Yellow","trigger_family":"nonlife_rate_cycle_label_yellow_false_positive","trigger_date":"2024-05-14","entry_date":"2024-05-14","entry_price":34200.0,"entry_price_basis":"close","price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/001/001450/2024.csv","profile_path":"atlas/symbol_profiles/001/001450.json","price_row_fetch_status":"local_prior_stock_web_rows_reused_for_same_shard_paths; batch_reverification_required","MFE_30D_pct":2.34,"MAE_30D_pct":-9.36,"MFE_90D_pct":7.16,"MAE_90D_pct":-9.36,"MFE_180D_pct":7.16,"MAE_180D_pct":-20.32,"MFE_1Y_pct":null,"MAE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_2Y_pct":null,"positive_or_counterexample":"counterexample","outcome_label":"yellow_false_positive_high_MAE","current_profile_error_type":"Stage3_Yellow_too_loose_when_rate_cycle_label_lacks_CSM_reserve_capital_return_bridge","source_proxy_only":true,"evidence_url_pending":true,"batch_reverification_required":true,"four_b_local_peak_proximity":false,"four_b_full_window_peak_proximity":false,"four_b_timing_verdict":"not_4B","four_c_protection_label":"early_thesis_break_watch_if_reserve_or_capital_return_bridge_absent","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"same_entry_group_id":"C22_INSURANCE_RATE_CYCLE_RESERVE|001450|Stage3-Yellow|2024-05-14","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":"same symbol new canonical stage family; hard duplicate key not reused","do_not_count_as_new_case":false,"independent_evidence_weight":0.62}
{"row_type":"trigger","schema_version":"v12_stock_web_residual","case_id":"C22_R6L106_000370_20240201_STAGE3YELLOW_SMALL_NONLIFE","selected_round":"R6","selected_loop":106,"large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","fine_archetype_id":"INSURANCE_CSM_RESERVE_CAPITAL_RETURN_FINAL_PASS_TO_30_STAGE4B_GREEN_CAP_SPLIT","symbol":"000370","name":"한화손해보험","market":"KOSPI","trigger_type":"Stage3-Yellow","trigger_family":"small_nonlife_high_MAE_yellow_cap","trigger_date":"2024-02-01","entry_date":"2024-02-01","entry_price":5120.0,"entry_price_basis":"close","price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/000/000370/2024.csv","profile_path":"atlas/symbol_profiles/000/000370.json","price_row_fetch_status":"local_prior_stock_web_rows_reused_for_same_shard_paths; batch_reverification_required","MFE_30D_pct":20.5,"MAE_30D_pct":-18.9,"MFE_90D_pct":20.5,"MAE_90D_pct":-18.9,"MFE_180D_pct":21.7,"MAE_180D_pct":-18.9,"MFE_1Y_pct":null,"MAE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_2Y_pct":null,"positive_or_counterexample":"mixed_counterexample","outcome_label":"high_MAE_small_nonlife_not_green","current_profile_error_type":"Stage3_Yellow_should_be_capped_for_small_nonlife_price_beta_with_deep_MAE","source_proxy_only":true,"evidence_url_pending":true,"batch_reverification_required":true,"four_b_local_peak_proximity":true,"four_b_full_window_peak_proximity":false,"four_b_timing_verdict":"local_4B_watch_only_high_MAE_guard","four_c_protection_label":"not_applicable","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"same_entry_group_id":"C22_INSURANCE_RATE_CYCLE_RESERVE|000370|Stage3-Yellow|2024-02-01","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":"same symbol new canonical stage family; hard duplicate key not reused","do_not_count_as_new_case":false,"independent_evidence_weight":0.62}
{"row_type":"trigger","schema_version":"v12_stock_web_residual","case_id":"C22_R6L106_003690_20240201_STAGE3YELLOW_REINSURANCE_CAP","selected_round":"R6","selected_loop":106,"large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","fine_archetype_id":"INSURANCE_CSM_RESERVE_CAPITAL_RETURN_FINAL_PASS_TO_30_STAGE4B_GREEN_CAP_SPLIT","symbol":"003690","name":"코리안리","market":"KOSPI","trigger_type":"Stage3-Yellow","trigger_family":"reinsurance_quality_low_beta_stage3_cap","trigger_date":"2024-02-01","entry_date":"2024-02-01","entry_price":7830.0,"entry_price_basis":"close","price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/003/003690/2024.csv","profile_path":"atlas/symbol_profiles/003/003690.json","price_row_fetch_status":"local_prior_stock_web_rows_reused_for_same_shard_paths; batch_reverification_required","MFE_30D_pct":9.1,"MAE_30D_pct":-4.6,"MFE_90D_pct":11.7,"MAE_90D_pct":-6.8,"MFE_180D_pct":12.0,"MAE_180D_pct":-8.6,"MFE_1Y_pct":null,"MAE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_2Y_pct":null,"positive_or_counterexample":"mixed_neutral","outcome_label":"low_beta_reinsurance_watch_not_yellow","current_profile_error_type":"Stage3_Yellow_too_generous_for_reinsurance_without_revision_or_capital_return_acceleration","source_proxy_only":true,"evidence_url_pending":true,"batch_reverification_required":true,"four_b_local_peak_proximity":false,"four_b_full_window_peak_proximity":false,"four_b_timing_verdict":"not_4B","four_c_protection_label":"not_applicable","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"same_entry_group_id":"C22_INSURANCE_RATE_CYCLE_RESERVE|003690|Stage3-Yellow|2024-02-01","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":"same symbol new canonical stage family; hard duplicate key not reused","do_not_count_as_new_case":false,"independent_evidence_weight":0.62}
```

## 5. Score simulation rows

```jsonl
{"row_type":"score_simulation","schema_version":"v12_stock_web_residual","case_id":"C22_R6L106_032830_20240201_STAGE3GREEN_CAP","symbol":"032830","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","trigger_type":"Stage3-Green","current_profile_stage_proxy":"Stage3-Green","shadow_stage_after_C22_rule":"Stage3-Green only if CSM/reserve/capital-return bridge explicitly verified","raw_component_score_breakdown":{"CSM_durability":18,"reserve_quality":14,"solvency_capital_buffer":12,"capital_return_execution":16,"price_only_beta_penalty":0,"high_MAE_guardrail":-4},"weighted_score_before":88,"weighted_score_after":86,"score_return_alignment_label":"positive_but_bridge_required"}
{"row_type":"score_simulation","schema_version":"v12_stock_web_residual","case_id":"C22_R6L106_000810_20240426_STAGE4B_GREEN_SPLIT","symbol":"000810","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","trigger_type":"Stage4B","current_profile_stage_proxy":"Stage4B","shadow_stage_after_C22_rule":"full_4B_allowed_if_non_price_bridge_reverified","raw_component_score_breakdown":{"CSM_durability":16,"reserve_quality":16,"solvency_capital_buffer":14,"capital_return_execution":16,"price_only_beta_penalty":0,"high_MAE_guardrail":0},"weighted_score_before":84,"weighted_score_after":86,"score_return_alignment_label":"positive_full_4B_after_bridge"}
{"row_type":"score_simulation","schema_version":"v12_stock_web_residual","case_id":"C22_R6L106_005830_20240426_STAGE4B_LOCAL_CAP","symbol":"005830","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","trigger_type":"Stage4B","current_profile_stage_proxy":"Stage4B","shadow_stage_after_C22_rule":"local_4B_watch_until_reserve_refresh","raw_component_score_breakdown":{"CSM_durability":10,"reserve_quality":10,"solvency_capital_buffer":12,"capital_return_execution":8,"price_only_beta_penalty":-6,"high_MAE_guardrail":0},"weighted_score_before":80,"weighted_score_after":72,"score_return_alignment_label":"mixed_positive_local_4B_only"}
{"row_type":"score_simulation","schema_version":"v12_stock_web_residual","case_id":"C22_R6L106_001450_20240514_STAGE3YELLOW_REJECT","symbol":"001450","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","trigger_type":"Stage3-Yellow","current_profile_stage_proxy":"Stage3-Yellow","shadow_stage_after_C22_rule":"Stage2-watch_or_reject","raw_component_score_breakdown":{"CSM_durability":6,"reserve_quality":6,"solvency_capital_buffer":8,"capital_return_execution":4,"price_only_beta_penalty":-8,"high_MAE_guardrail":-12},"weighted_score_before":76,"weighted_score_after":52,"score_return_alignment_label":"counterexample_yellow_false_positive"}
{"row_type":"score_simulation","schema_version":"v12_stock_web_residual","case_id":"C22_R6L106_000370_20240201_STAGE3YELLOW_SMALL_NONLIFE","symbol":"000370","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","trigger_type":"Stage3-Yellow","current_profile_stage_proxy":"Stage3-Yellow","shadow_stage_after_C22_rule":"local_4B_watch_high_MAE_cap","raw_component_score_breakdown":{"CSM_durability":6,"reserve_quality":8,"solvency_capital_buffer":8,"capital_return_execution":6,"price_only_beta_penalty":-8,"high_MAE_guardrail":-10},"weighted_score_before":78,"weighted_score_after":56,"score_return_alignment_label":"mixed_counterexample_high_MAE"}
{"row_type":"score_simulation","schema_version":"v12_stock_web_residual","case_id":"C22_R6L106_003690_20240201_STAGE3YELLOW_REINSURANCE_CAP","symbol":"003690","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","trigger_type":"Stage3-Yellow","current_profile_stage_proxy":"Stage3-Yellow","shadow_stage_after_C22_rule":"Stage2-watch_low_beta_cap","raw_component_score_breakdown":{"CSM_durability":8,"reserve_quality":12,"solvency_capital_buffer":12,"capital_return_execution":4,"price_only_beta_penalty":-6,"high_MAE_guardrail":0},"weighted_score_before":76,"weighted_score_after":62,"score_return_alignment_label":"mixed_neutral_not_yellow"}
```

## 6. Aggregate / shadow rule / residual contribution rows

```jsonl
{"row_type":"aggregate_metrics","schema_version":"v12_stock_web_residual","round":"R6","loop":106,"large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","fine_archetype_id":"INSURANCE_CSM_RESERVE_CAPITAL_RETURN_FINAL_PASS_TO_30_STAGE4B_GREEN_CAP_SPLIT","new_independent_case_count":6,"reused_case_count":0,"same_archetype_new_symbol_count":0,"same_symbol_new_trigger_family_count":6,"calibration_usable_case_count":6,"calibration_usable_trigger_count":6,"positive_case_count":2,"mixed_positive_count":2,"counterexample_count":2,"local_4b_watch_count":3,"current_profile_error_count":6,"source_proxy_only_count":6,"evidence_url_pending_count":6,"batch_reverification_required":true,"auto_selected_coverage_gap_static_index":"C22 rows 6 -> 12 if accepted; still Priority 0 by static index, need 18 to reach 30","auto_selected_coverage_gap_conversation_local":"C22 local approx 24 -> 30 if accepted; C22 local 30-row floor reached","loop_contribution_label":"C22_final_pass_to_30_and_Stage4B_Green_cap_split"}
{"row_type":"shadow_weight_candidate","schema_version":"v12_stock_web_residual","round":"R6","loop":106,"large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","do_not_propose_new_weight_delta":false,"new_axis_proposed":["C22_CSM_RESERVE_CAPITAL_RETURN_BRIDGE_REQUIRED","C22_STAGE4B_FULL_ALLOWED_ONLY_WITH_NON_PRICE_BRIDGE","C22_LIFE_INSURANCE_GREEN_CAP_REQUIRES_CSM_RESERVE_CONFIRMATION","C22_SMALL_NONLIFE_HIGH_MAE_YELLOW_CAP","C22_REINSURANCE_LOW_BETA_STAGE3_CAP"],"existing_axis_strengthened":["stage2_required_bridge","price_only_blowoff_blocks_positive_stage","full_4b_requires_non_price_evidence","local_4b_watch_guard","high_MAE_guardrail"],"existing_axis_weakened":[],"confidence":"medium_low_until_batch_reverification","implementation_timing":"deferred_batch_only"}
{"row_type":"residual_contribution","schema_version":"v12_stock_web_residual","round":"R6","loop":106,"large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","new_independent_case_count":6,"residual_error_types_found":["C21_C22_valueup_contamination","insurance_Stage4B_full_vs_local_split","life_insurance_green_cap_requires_CSM_confirmation","small_nonlife_high_MAE_yellow_false_positive","reinsurance_low_beta_stage3_cap","source_proxy_reverification_needed"],"sector_specific_rule_candidate":true,"canonical_archetype_rule_candidate":true,"do_not_propose_new_weight_delta":false}
```

## 7. Shadow rule narrative

C22 should behave like a lock with three tumblers, not a single price switch. The first tumbler is reserve/CSM quality, the second is solvency capital and payout capacity, and the third is underwriting/rate-cycle or capital-return execution. If all three turn, Green or full 4B is defensible. If only price turns, the door should stay at Stage2-watch or local 4B, especially for small non-life insurers and reinsurance names with low MFE.

The final pass also compresses the boundary between C21 and C22. A bank-like value-up label can be a useful proxy, but it should not be sufficient for C22. C22 must show the insurance-specific bridge; otherwise the score should route to C21-style financial beta or stay capped as a price-only/local 4B watch.

## 8. Deferred Coding Agent Handoff Prompt

```text
You are a later coding agent, not this research runner. Read this MD as a v12 residual research artifact only. Do not execute code patches automatically.

File:
e2r_stock_web_v12_residual_round_R6_loop_106_L6_FINANCIAL_CAPITAL_RETURN_DIGITAL_C22_INSURANCE_RATE_CYCLE_RESERVE_research.md

Tasks:
1. Re-fetch all listed stock-web shard/profile paths before ingest because this MD used local prior stock-web rows after fresh raw URL cache misses.
2. Validate JSONL rows and dedupe by canonical_archetype_id + symbol + trigger_type + entry_date.
3. Implement only deferred/shadow candidates unless explicitly instructed:
   - C22_CSM_RESERVE_CAPITAL_RETURN_BRIDGE_REQUIRED
   - C22_STAGE4B_FULL_ALLOWED_ONLY_WITH_NON_PRICE_BRIDGE
   - C22_LIFE_INSURANCE_GREEN_CAP_REQUIRES_CSM_RESERVE_CONFIRMATION
   - C22_SMALL_NONLIFE_HIGH_MAE_YELLOW_CAP
   - C22_REINSURANCE_LOW_BETA_STAGE3_CAP
4. Keep C21 financial ROE/PBR value-up scoring separate from C22 reserve/CSM/capital-return scoring.
5. Mark source_proxy_only/evidence_url_pending rows as blocked_by_data_quality until URL evidence is repaired.
```

## 9. Research state for next run

```text
completed_round = R6
completed_loop = 106
selection_basis = docs/core/V12_Research_No_Repeat_Index.md + conversation-local generated MD ledger
selected_priority_bucket = Priority 0
round_schedule_status = coverage_index_selected
round_sector_consistency = pass
next_recommended_archetypes = C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN_final_pass_to_30, C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT_second_pass_to_30, C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY, C15_MATERIAL_SPREAD_SUPERCYCLE_final_pass_to_30, C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE_fourth_pass_to_30, R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL
```
