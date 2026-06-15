# E2R Stock-Web v12 Residual Research — R9 Loop 92 / L3 / C29

```yaml
schema_family: v12_sector_archetype_residual
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
round: R9
loop: 92
large_sector_id: L3_BATTERY_EV_GREEN_MOBILITY
canonical_archetype_id: C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE
fine_archetype_id: AUTO_INTERIOR_OEM_VOLUME_MIX_BRIDGE_VS_SEAT_EXHAUST_PARTS_VOCABULARY_DECAY
sector: mobility / auto parts / interior module / seat parts / exhaust system / OEM volume / program mix / margin / cash conversion
output_file: e2r_stock_web_v12_residual_round_R9_loop_92_L3_BATTERY_EV_GREEN_MOBILITY_C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE_research.md
production_scoring_changed: false
shadow_weight_only: true
stock_agent_code_accessed: false
handoff_prompt_embedded: true
handoff_prompt_executed_now: false
```

## 1. Scope lock

This run follows the v12 sequential scheduler after completed `R8 loop 92`.

```text
scheduled_round = R9
scheduled_loop = 92
large_sector_id = L3_BATTERY_EV_GREEN_MOBILITY
canonical_archetype_id = C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE
```

R9 is the mobility / auto-parts / EV operating-leverage lane.
C29 remains the correct R9 archetype because this lane continues the mobility volume / margin / operating-leverage residual set.

No-Repeat Index snapshot used only as duplicate ledger:

```text
C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE
rows = 86
symbols = 53
good/bad Stage2 = 20/23
4B/4C = 7/10
top-covered = 073240, 204320, 064960, 092200, 002350, 009900
```

This loop avoids the C29 top-covered list and prior C29 loop sets:

```text
R9 loop84: 086280, 161390, 271940
R9 loop85: 000120, 003620, 215360
R9 loop86: 073240, 118990, 090080
R9 loop87: 004490, 009900, 024900
R9 loop88: 200880, 092200, 123040
R9 loop89: 064960, 067570, 012860
R9 loop90: 092780, 126640, 013870
R9 loop91: 123410, 033250, 012280
earlier known C29: 012330, 002350, 204320
```

Candidate hygiene note:

```text
During this execution path, stale R8/C28, R7/C25 and earlier-sector candidate rows were touched while checking alternatives.
Those rows are not used in this R9/C29 output.
```

Selected symbols:

```text
007860, 005710, 033530
```

The selected pocket is:

```text
auto interior / OEM model-volume / program-mix bridge
vs
seat-parts vocabulary without fresh customer-volume and margin bridge
vs
exhaust-system / legacy auto-parts vocabulary without durable OEM volume / utilization / cash bridge
```

This is not a live stock recommendation, not a `stock_agent` code patch, and not a production scoring change.

## 2. Price atlas validation

```jsonl
{"row_type":"price_source_validation","source_name":"FinanceData/marcap via Songdaiki/stock-web","price_data_source":"Songdaiki/stock-web","upstream_source":"FinanceData/marcap","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","manifest_min_date":"1995-05-02","manifest_max_date":"2026-02-20","tradable_row_count":14354401,"raw_row_count":15214118,"symbol_count":5414,"active_like_symbol_count":2868,"corporate_action_candidate_count":14435,"calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","notes":"Raw/unadjusted OHLC; zero-volume and invalid OHLC rows are excluded from tradable shards; corporate-action-contaminated windows are blocked by default."}
{"row_type":"price_source_validation","symbol":"007860","company_name":"서연","profile_path":"atlas/symbol_profiles/007/007860.json","first_date":"1995-05-02","last_date":"2026-02-20","trading_day_count":7712,"corporate_action_candidate_count":"profile_tail_not_fetched_in_this_run","corporate_action_candidate_dates":"historical_name_transition_watch","has_major_raw_discontinuity":true,"calibration_caveat":"Historical name transition from 한일이화 to 서연 exists before selected 2024 forward window; selected 2024 window is usable.","status_inferred":"active_like","price_adjustment_status":"raw_unadjusted_marcap","profile_check":"2024_forward_window_clean_for_selected_entry"}
{"row_type":"price_source_validation","symbol":"005710","company_name":"대원산업","profile_path":"atlas/symbol_profiles/005/005710.json","first_date":"1996-07-26","last_date":"2026-02-20","trading_day_count":6720,"corporate_action_candidate_count":6,"corporate_action_candidate_dates":["1996-08-27","1997-12-23","1998-01-16","1999-06-03","2004-11-24","2011-04-07"],"has_major_raw_discontinuity":true,"calibration_caveat":"Historical corporate-action candidates exist before selected 2024 forward window.","status_inferred":"active_like","price_adjustment_status":"raw_unadjusted_marcap","profile_check":"2024_forward_window_clean_for_selected_entry"}
{"row_type":"price_source_validation","symbol":"033530","company_name":"SJG세종","profile_path":"atlas/symbol_profiles/033/033530.json","first_date":"1997-12-27","last_date":"2026-02-20","trading_day_count":6678,"corporate_action_candidate_count":1,"corporate_action_candidate_dates":["1999-11-29"],"has_major_raw_discontinuity":true,"calibration_caveat":"Historical corporate-action candidate exists before selected 2024 forward window. Name changed within 2024 from 세종공업 to 에스제이지세종/SJG세종; keep name-transition watch before patching.","status_inferred":"active_like","price_adjustment_status":"raw_unadjusted_marcap","profile_check":"2024_forward_window_usable; 2024_name_transition_watch"}
```

## 3. No-repeat and novelty check

Hard duplicate key applied:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

New keys introduced:

```jsonl
{"row_type":"narrative_only","check":"no_repeat_key","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","symbol":"007860","trigger_type":"Stage2-Actionable-AutoInteriorOEMVolumeProgramMixBridge-Positive","entry_date":"2024-01-29","duplicate_status":"new C29 symbol/trigger/date combination outside top-covered and previous C29 loop sets"}
{"row_type":"narrative_only","check":"no_repeat_key","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","symbol":"005710","trigger_type":"Stage2-FalsePositive-SeatPartsVocabularyNoFreshOEMVolumeMarginCashBridge","entry_date":"2024-01-29","duplicate_status":"new C29 symbol/trigger/date combination outside top-covered and previous C29 loop sets"}
{"row_type":"narrative_only","check":"no_repeat_key","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","symbol":"033530","trigger_type":"Stage2-FalsePositive-ExhaustSystemLegacyAutopartsVocabularyNoDurableOEMVolumeBridge","entry_date":"2024-01-02","duplicate_status":"new C29 symbol/trigger/date combination outside top-covered and previous C29 loop sets; 2024 name-transition watch"}
```

## 4. Research question

C29 is not “자동차 부품주가 움직였다.”
The useful mobility operating-leverage signal must prove the operating chain:

```text
fresh OEM/customer volume
program mix or model exposure
hybrid/EV platform or high-margin platform exposure
utilization recovery
price/cost pass-through
margin bridge
working-capital discipline
cash conversion
```

An auto-parts headline without this bridge is an engine on a test stand. It may rev loudly, but it does not move the car until OEM volume, utilization, program mix, margin, and cash conversion reach the axle.

Residual question:

```text
Can C29 distinguish:
1. auto interior / OEM model-volume / program-mix bridge with high MFE and controlled early MAE,
2. seat-parts vocabulary with only low MFE and no fresh customer-volume evidence,
3. exhaust-system / legacy auto-parts vocabulary where early theme strength fails without durable OEM volume and margin/cash repair?
```

## 5. Case rows

```jsonl
{"row_type":"case","case_id":"C29_R9L92_007860_SEOYON_AUTO_INTERIOR_VOLUME_MIX","symbol":"007860","company_name":"서연","round":"R9","loop":"92","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"AUTO_INTERIOR_OEM_VOLUME_PROGRAM_MIX_BRIDGE","case_type":"structural_success_watch","positive_or_counterexample":"positive","best_trigger":"Stage2-Actionable-AutoInteriorOEMVolumeProgramMixBridge-Positive","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"positive_high_MFE90_controlled_entry_MAE_auto_interior_volume_mix_bridge","current_profile_verdict":"current_profile_correct_if_OEM_volume_program_mix_margin_cash_bridge_required","price_source":"Songdaiki/stock-web","notes":"Auto interior / OEM model-volume / program-mix proxy produced high MFE with controlled entry MAE. Green still requires exact OEM volume, program mix, utilization, margin and cash evidence."}
{"row_type":"case","case_id":"C29_R9L92_005710_DAEWON_SEAT_PARTS_WEAK_BRIDGE","symbol":"005710","company_name":"대원산업","round":"R9","loop":"92","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"SEAT_PARTS_VOCABULARY_WITHOUT_FRESH_OEM_VOLUME_MARGIN_CASH_BRIDGE","case_type":"weak_entry","positive_or_counterexample":"counterexample","best_trigger":"Stage2-FalsePositive-SeatPartsVocabularyNoFreshOEMVolumeMarginCashBridge","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"counterexample_low_MFE_flat_path_no_fresh_OEM_volume_bridge","current_profile_verdict":"current_profile_false_positive_if_seat_parts_vocabulary_overcredited","price_source":"Songdaiki/stock-web","notes":"Seat-parts vocabulary produced only low MFE and flat/weak path without fresh OEM/customer-volume, utilization, program mix, margin or cash bridge."}
{"row_type":"case","case_id":"C29_R9L92_033530_SJGSEJONG_EXHAUST_LEGACY_DECAY","symbol":"033530","company_name":"SJG세종","round":"R9","loop":"92","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"EXHAUST_SYSTEM_LEGACY_AUTOPARTS_WITHOUT_DURABLE_OEM_VOLUME_BRIDGE","case_type":"failed_entry","positive_or_counterexample":"counterexample","best_trigger":"Stage2-FalsePositive-ExhaustSystemLegacyAutopartsVocabularyNoDurableOEMVolumeBridge","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":0.95,"score_price_alignment":"counterexample_sub20_MFE_deep_MAE_name_transition_watch_no_OEM_volume_bridge","current_profile_verdict":"current_profile_false_positive_if_exhaust_legacy_autoparts_vocabulary_overcredited","price_source":"Songdaiki/stock-web","notes":"Exhaust-system / legacy auto-parts vocabulary had sub-20 MFE and deep 180D/full-window MAE without durable OEM volume, utilization, price/cost pass-through, margin or cash bridge. 2024 name-transition watch remains."}
```

## 6. Trigger-level Stock-Web rows

### 6.1 007860 서연 — auto interior / OEM volume / program-mix bridge positive-control

Entry row: `2024-01-29 c=7570`.
Observed path: entry-area low `2024-01-29 l=7340`, 90D peak `2024-02-13 h=13870`, and later full-year low `2024-12-09 l=5780`.

```jsonl
{"row_type":"trigger","trigger_id":"R9L92_C29_007860_20240129_STAGE2_AUTO_INTERIOR_VOLUME_MIX","case_id":"C29_R9L92_007860_SEOYON_AUTO_INTERIOR_VOLUME_MIX","symbol":"007860","company_name":"서연","round":"R9","loop":"92","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"AUTO_INTERIOR_OEM_VOLUME_PROGRAM_MIX_BRIDGE","loop_objective":"holdout_validation;canonical_archetype_rule_candidate;green_strictness_stress_test","trigger_type":"Stage2-Actionable-AutoInteriorOEMVolumeProgramMixBridge-Positive","trigger_date":"2024-01-29","entry_date":"2024-01-29","entry_price":7570.0,"entry_price_basis":"close","evidence_available_at_that_date":"historical_public_auto_interior_OEM_volume_program_mix_proxy_available_by_entry","evidence_source":"source-name-level proxy; exact URL pending; auto interior, OEM model-volume, program mix, utilization and margin bridge treated as non-price proxy, not final citation-grade evidence","evidence_source_type":"historical_public_report_news_proxy","source_proxy_only":true,"evidence_url_pending":true,"stage2_evidence_fields":["OEM_customer_volume_proxy","auto_interior_program_mix_proxy","utilization_recovery_proxy","relative_strength_turn"],"stage3_evidence_fields":["exact_customer_volume_source_pending","program_mix_source_pending","margin_bridge_pending","cash_conversion_pending"],"stage4b_evidence_fields":["price_extension_watch","late_drawdown_watch"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/007/007860/2024.csv","profile_path":"atlas/symbol_profiles/007/007860.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":83.22,"MFE_90D_pct":83.22,"MFE_180D_pct":83.22,"MAE_30D_pct":-3.04,"MAE_90D_pct":-3.04,"MAE_180D_pct":-10.96,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-02-13","peak_price":13870.0,"max_drawdown_low_date":"2024-12-09","max_drawdown_low":5780.0,"drawdown_after_peak_pct":-58.33,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"positive_but_Green_requires_exact_OEM_volume_program_mix_utilization_margin_cash_evidence","four_b_evidence_type":["price_extension_watch","late_drawdown_watch"],"four_c_protection_label":"not_applicable","trigger_outcome_label":"positive_high_MFE90_controlled_entry_MAE_auto_interior_volume_mix_bridge","current_profile_verdict":"current_profile_correct_if_OEM_volume_program_mix_margin_cash_bridge_required","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"historical_name_transition_pre_2024; selected_window_clean","same_entry_group_id":"007860_2024-01-29_7570","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"current_profile_residual":"C29 can allow Stage2/Yellow when mobility strength is tied to OEM/customer volume, program mix, utilization, margin and cash conversion. Green requires exact source-grade evidence."}
```

### 6.2 005710 대원산업 — seat-parts vocabulary without fresh OEM volume / margin-cash bridge

Entry row: `2024-01-29 c=6150`, after an auto-parts/seat-parts price burst.
Observed path: high `2024-02-02 h=6770`, but follow-through remained flat/weak and later revisited the original range.

```jsonl
{"row_type":"trigger","trigger_id":"R9L92_C29_005710_20240129_STAGE2_FALSE_POSITIVE_SEAT_PARTS","case_id":"C29_R9L92_005710_DAEWON_SEAT_PARTS_WEAK_BRIDGE","symbol":"005710","company_name":"대원산업","round":"R9","loop":"92","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"SEAT_PARTS_VOCABULARY_WITHOUT_FRESH_OEM_VOLUME_MARGIN_CASH_BRIDGE","loop_objective":"residual_false_positive_mining;counterexample_mining;4B_non_price_requirement_stress_test","trigger_type":"Stage2-FalsePositive-SeatPartsVocabularyNoFreshOEMVolumeMarginCashBridge","trigger_date":"2024-01-29","entry_date":"2024-01-29","entry_price":6150.0,"entry_price_basis":"close","evidence_available_at_that_date":"historical_public_seat_parts_autoparts_vocabulary_proxy_available_by_entry","evidence_source":"source-name-level proxy; exact URL pending; seat-parts auto-parts vocabulary treated as insufficient without fresh OEM/customer volume, utilization recovery, program mix, margin and cash bridge","evidence_source_type":"historical_public_report_news_proxy","source_proxy_only":true,"evidence_url_pending":true,"stage2_evidence_fields":["seat_parts_keyword","legacy_autoparts_rebound","relative_strength_burst"],"stage3_evidence_fields":["fresh_OEM_volume_missing","program_mix_missing","utilization_bridge_missing","margin_cash_bridge_missing"],"stage4b_evidence_fields":["low_MFE","OEM_volume_bridge_missing_watch","flat_followthrough_watch"],"stage4c_evidence_fields":["thesis_break_watch_only"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/005/005710/2024.csv","profile_path":"atlas/symbol_profiles/005/005710.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":10.08,"MFE_90D_pct":10.08,"MFE_180D_pct":10.08,"MAE_30D_pct":-8.78,"MAE_90D_pct":-8.94,"MAE_180D_pct":-9.11,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-02-02","peak_price":6770.0,"max_drawdown_low_date":"2024-11-13","max_drawdown_low":5590.0,"drawdown_after_peak_pct":-17.43,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"seat_parts_vocabulary_without_fresh_OEM_volume_program_mix_margin_cash_bridge_should_be_4B_watch_not_positive","four_b_evidence_type":["low_MFE","OEM_volume_bridge_missing_watch","flat_followthrough_watch"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"counterexample_low_MFE_flat_path_no_fresh_OEM_volume_bridge","current_profile_verdict":"current_profile_false_positive_if_seat_parts_vocabulary_overcredited","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"historical_candidates_pre_2024; selected_window_clean","same_entry_group_id":"005710_2024-01-29_6150","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"current_profile_residual":"C29 should not promote seat-parts vocabulary without fresh OEM/customer volume, program mix, utilization, margin and cash evidence. Low MFE and weak follow-through require Watch/4B routing."}
```

### 6.3 033530 SJG세종 — exhaust-system / legacy auto-parts vocabulary without durable OEM volume bridge

Entry row: `2024-01-02 c=6000`.
Observed path: early high `2024-01-05 h=6890`, then full-year decay to `2024-12-09 l=3550`. Name changes occurred within 2024, so production patching should retain name-transition watch.

```jsonl
{"row_type":"trigger","trigger_id":"R9L92_C29_033530_20240102_STAGE2_FALSE_POSITIVE_EXHAUST_LEGACY_AUTOPARTS","case_id":"C29_R9L92_033530_SJGSEJONG_EXHAUST_LEGACY_DECAY","symbol":"033530","company_name":"SJG세종","round":"R9","loop":"92","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"EXHAUST_SYSTEM_LEGACY_AUTOPARTS_WITHOUT_DURABLE_OEM_VOLUME_BRIDGE","loop_objective":"residual_false_positive_mining;counterexample_mining;name_transition_watch;4B_non_price_requirement_stress_test","trigger_type":"Stage2-FalsePositive-ExhaustSystemLegacyAutopartsVocabularyNoDurableOEMVolumeBridge","trigger_date":"2024-01-02","entry_date":"2024-01-02","entry_price":6000.0,"entry_price_basis":"close","evidence_available_at_that_date":"historical_public_exhaust_system_legacy_autoparts_vocabulary_proxy_available_by_entry","evidence_source":"source-name-level proxy; exact URL pending; exhaust-system/legacy auto-parts vocabulary treated as insufficient without durable OEM volume, utilization, price/cost pass-through, margin and cash bridge","evidence_source_type":"historical_public_report_news_proxy","source_proxy_only":true,"evidence_url_pending":true,"stage2_evidence_fields":["exhaust_system_keyword","legacy_autoparts_rebound","relative_strength_spike"],"stage3_evidence_fields":["durable_OEM_volume_missing","program_mix_missing","utilization_pricing_bridge_missing","margin_cash_bridge_missing"],"stage4b_evidence_fields":["sub20_MFE","deep_MAE","name_transition_watch","OEM_volume_bridge_missing_watch"],"stage4c_evidence_fields":["thesis_break_watch_only"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/033/033530/2024.csv","profile_path":"atlas/symbol_profiles/033/033530.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":14.83,"MFE_90D_pct":14.83,"MFE_180D_pct":14.83,"MAE_30D_pct":-9.17,"MAE_90D_pct":-9.17,"MAE_180D_pct":-26.00,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-01-05","peak_price":6890.0,"max_drawdown_low_date":"2024-12-09","max_drawdown_low":3550.0,"drawdown_after_peak_pct":-48.48,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"exhaust_legacy_autoparts_vocabulary_without_OEM_volume_utilization_margin_cash_bridge_should_be_4B_watch_not_positive","four_b_evidence_type":["sub20_MFE","deep_MAE","name_transition_watch","OEM_volume_bridge_missing_watch"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"counterexample_sub20_MFE_deep_MAE_name_transition_watch_no_OEM_volume_bridge","current_profile_verdict":"current_profile_false_positive_if_exhaust_legacy_autoparts_vocabulary_overcredited","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":["2024_name_transition_watch_before_patch"],"corporate_action_window_status":"historical_candidate_pre_2024; selected_window_usable; 2024_name_transition_watch","same_entry_group_id":"033530_2024-01-02_6000","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":0.95,"do_not_count_as_new_case":false,"current_profile_residual":"C29 should not equate exhaust-system/legacy auto-parts vocabulary with operating leverage. Durable OEM volume, utilization recovery, price/cost pass-through, margin and cash bridge must be repaired before Yellow/Green."}
```

## 7. Score simulation rows

```jsonl
{"row_type":"score_simulation","profile_id":"P0_e2r_2_1_stock_web_calibrated_proxy","case_id":"C29_R9L92_007860_SEOYON_AUTO_INTERIOR_VOLUME_MIX","trigger_id":"R9L92_C29_007860_20240129_STAGE2_AUTO_INTERIOR_VOLUME_MIX","symbol":"007860","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","profile_scope":"current_default_proxy","profile_hypothesis":"current profile works if C29 requires OEM/customer volume, model/program mix, utilization recovery, margin and cash bridge rather than auto-parts label alone","raw_component_scores_before":{"customer_volume_score":13,"program_mix_score":12,"platform_exposure_score":10,"operating_leverage_score":12,"utilization_score":10,"margin_bridge_score":10,"cash_conversion_score":7,"relative_strength_score":15,"valuation_repricing_score":8,"execution_risk_score":-5,"theme_spike_risk":-2,"information_confidence":4},"weighted_score_before":72,"stage_label_before":"Stage2-Actionable/Yellow-Watch","raw_component_scores_after":{"customer_volume_score":16,"program_mix_score":15,"platform_exposure_score":12,"operating_leverage_score":15,"utilization_score":12,"margin_bridge_score":12,"cash_conversion_score":9,"relative_strength_score":16,"valuation_repricing_score":9,"execution_risk_score":-4,"theme_spike_risk":-1,"information_confidence":5},"weighted_score_after":87,"stage_label_after":"Stage3-Yellow/Green-candidate-watch","component_delta_explanation":"OEM volume/program-mix bridge plus high MFE supports Yellow/Green-candidate watch; exact customer-volume and margin evidence blocks automatic Green."}
{"row_type":"score_simulation","profile_id":"P0_e2r_2_1_stock_web_calibrated_proxy","case_id":"C29_R9L92_005710_DAEWON_SEAT_PARTS_WEAK_BRIDGE","trigger_id":"R9L92_C29_005710_20240129_STAGE2_FALSE_POSITIVE_SEAT_PARTS","symbol":"005710","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","profile_scope":"current_default_proxy","profile_hypothesis":"seat-parts vocabulary without fresh OEM/customer volume and margin bridge should remain Watch/4B","raw_component_scores_before":{"customer_volume_score":1,"program_mix_score":1,"platform_exposure_score":0,"operating_leverage_score":0,"utilization_score":0,"margin_bridge_score":0,"cash_conversion_score":0,"relative_strength_score":4,"valuation_repricing_score":2,"execution_risk_score":-10,"theme_spike_risk":-14,"information_confidence":3},"weighted_score_before":0,"stage_label_before":"Stage2-Watch/FalsePositive","raw_component_scores_after":{"customer_volume_score":0,"program_mix_score":0,"platform_exposure_score":0,"operating_leverage_score":0,"utilization_score":0,"margin_bridge_score":0,"cash_conversion_score":0,"relative_strength_score":1,"valuation_repricing_score":0,"execution_risk_score":-16,"theme_spike_risk":-18,"information_confidence":2},"weighted_score_after":0,"stage_label_after":"Stage1/4B-Watch","component_delta_explanation":"Low MFE and flat follow-through convert seat-parts vocabulary into missing OEM-volume/margin bridge failure."}
{"row_type":"score_simulation","profile_id":"P0_e2r_2_1_stock_web_calibrated_proxy","case_id":"C29_R9L92_033530_SJGSEJONG_EXHAUST_LEGACY_DECAY","trigger_id":"R9L92_C29_033530_20240102_STAGE2_FALSE_POSITIVE_EXHAUST_LEGACY_AUTOPARTS","symbol":"033530","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","profile_scope":"current_default_proxy","profile_hypothesis":"legacy exhaust auto-parts vocabulary without durable OEM volume and utilization/margin bridge should be blocked","raw_component_scores_before":{"customer_volume_score":1,"program_mix_score":0,"platform_exposure_score":0,"operating_leverage_score":0,"utilization_score":0,"margin_bridge_score":0,"cash_conversion_score":0,"relative_strength_score":5,"valuation_repricing_score":2,"execution_risk_score":-14,"theme_spike_risk":-16,"information_confidence":3},"weighted_score_before":0,"stage_label_before":"Stage2-Watch/FalsePositive/NameTransitionWatch","raw_component_scores_after":{"customer_volume_score":0,"program_mix_score":0,"platform_exposure_score":0,"operating_leverage_score":0,"utilization_score":0,"margin_bridge_score":0,"cash_conversion_score":0,"relative_strength_score":1,"valuation_repricing_score":0,"execution_risk_score":-24,"theme_spike_risk":-20,"information_confidence":2},"weighted_score_after":0,"stage_label_after":"Stage1/4B-Watch/NameTransitionWatch","component_delta_explanation":"Sub-20 MFE and deep MAE require durable OEM volume, utilization, margin and cash evidence before any Yellow/Green promotion."}
```

## 8. Profile comparison

```jsonl
{"row_type":"profile_comparison","comparison_id":"R9L92_C29_P0_CURRENT","round":"R9","loop":"92","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","profile_id":"P0_e2r_2_1_stock_web_calibrated_proxy","profile_scope":"current_default_proxy","profile_hypothesis":"global guardrails help but C29 needs explicit OEM/customer volume, program mix, platform exposure, utilization, price/cost, margin/cash and legacy-autoparts 4B taxonomy","eligible_trigger_count":3,"avg_MFE90_pct":36.04,"avg_MAE90_pct":-7.05,"avg_MFE180_pct":36.04,"avg_MAE180_pct":-15.36,"false_positive_rate":0.67,"missed_structural_count":0,"late_green_count":0,"avg_four_b_local_peak_proximity":1.0,"avg_four_b_full_window_peak_proximity":1.0,"score_return_alignment_verdict":"mixed_without_C29_OEM_volume_program_mix_margin_cash_bridge_guard"}
{"row_type":"profile_comparison","comparison_id":"R9L92_C29_P1_SECTOR_SPECIFIC","round":"R9","loop":"92","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","profile_id":"P1_L3_mobility_volume_mix_margin_bridge_candidate","profile_scope":"sector_specific","profile_hypothesis":"L3 mobility signals need customer volume, program mix, platform exposure, utilization, operating leverage, margin or cash conversion before Stage2-Actionable","changed_axes":["customer_volume_required","program_mix_platform_required","legacy_autoparts_vocabulary_penalty"],"changed_thresholds":{"stage2_actionable_bridge_min":"one_of_customer_volume_program_mix_platform_utilization_margin_or_cash_proxy"},"eligible_trigger_count":3,"avg_MFE90_pct":36.04,"avg_MAE90_pct":-7.05,"avg_MFE180_pct":36.04,"avg_MAE180_pct":-15.36,"false_positive_rate":0.33,"score_return_alignment_verdict":"better_if_exact_evidence_and_name_transition_repaired"}
{"row_type":"profile_comparison","comparison_id":"R9L92_C29_P2_CANONICAL","round":"R9","loop":"92","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","profile_id":"P2_C29_OEM_volume_program_mix_margin_cash_guard","profile_scope":"canonical_archetype_specific","profile_hypothesis":"C29 should reward customer-volume-to-margin mechanics, not seat/exhaust legacy auto-parts vocabulary","changed_axes":["C29_OEM_volume_program_mix_margin_cash_bridge_required","C29_seat_exhaust_legacy_autoparts_local_4B_guard","C29_name_transition_data_quality_guard"],"changed_thresholds":{"stage2_yellow_gate":"customer_volume_or_program_mix_plus_utilization_or_margin_cash_bridge_required"},"eligible_trigger_count":3,"avg_MFE90_pct":36.04,"avg_MAE90_pct":-7.05,"avg_MFE180_pct":36.04,"avg_MAE180_pct":-15.36,"false_positive_rate":0.0,"score_return_alignment_verdict":"best_local_shadow_candidate"}
{"row_type":"profile_comparison","comparison_id":"R9L92_C29_P3_COUNTEREXAMPLE_GUARD","round":"R9","loop":"92","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","profile_id":"P3_C29_low_MFE_or_deep_MAE_guard","profile_scope":"counterexample_guard","profile_hypothesis":"If OEM volume/margin bridge is missing, MFE90<15 or MAE180<=-25 should block Yellow/Green and route to Watch/4B","changed_axes":["C29_low_MFE_guardrail","C29_deep_MAE_4B_guardrail"],"changed_thresholds":{"bad_entry_filter":"bridge_missing_and_(MFE90_lt_15_or_MAE180_le_minus_25)"},"eligible_trigger_count":3,"avg_MFE90_pct":36.04,"avg_MAE90_pct":-7.05,"avg_MFE180_pct":36.04,"avg_MAE180_pct":-15.36,"false_positive_rate":0.0,"score_return_alignment_verdict":"safe_guardrail_candidate"}
```

## 9. Aggregate, transition, and coverage rows

```jsonl
{"row_type":"aggregate_metric","round":"R9","loop":"92","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"C29_AUTO_INTERIOR_POSITIVE_VS_SEAT_EXHAUST_DECAY","row_count":3,"unique_symbol_count":3,"positive_case_count":1,"counterexample_count":2,"good_stage2_count":1,"bad_stage2_count":2,"4B_case_count":2,"4C_case_count":0,"source_proxy_only_count":3,"evidence_url_pending_count":3,"calibration_usable_count":3,"data_quality_watch_count":1,"avg_MFE90_pct":36.04,"avg_MAE90_pct":-7.05,"avg_MFE180_pct":36.04,"avg_MAE180_pct":-15.36,"stage2_hit_rate_MFE90_ge20":0.33,"stage2_bad_entry_rate_bridge_missing":0.67,"stage2_bad_entry_rate_MFE90_lt15":0.67,"interpretation":"C29 needs bridge discipline. 서연 shows auto interior / OEM model-volume / program-mix bridge can support Yellow/Green-candidate-watch, while 대원산업 and SJG세종 show seat/exhaust/legacy auto-parts vocabulary should not be promoted without fresh OEM volume, utilization, price/cost pass-through, margin and cash evidence."}
{"row_type":"stage_transition_summary","round":"R9","loop":"92","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","symbol":"007860","trigger_type":"Stage2-Actionable-AutoInteriorOEMVolumeProgramMixBridge-Positive","entry_date":"2024-01-29","stage2_to_90D_outcome":"good_stage2_high_MFE_low_entry_MAE","stage2_to_180D_outcome":"positive_auto_interior_OEM_volume_bridge_Green_strict","MFE90_ge20":true,"MAE90_le_minus20":false,"transition_note":"Allow Stage2/Yellow when OEM/customer volume, program mix, utilization and margin/cash bridge exists; Green requires exact evidence."}
{"row_type":"stage_transition_summary","round":"R9","loop":"92","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","symbol":"005710","trigger_type":"Stage2-FalsePositive-SeatPartsVocabularyNoFreshOEMVolumeMarginCashBridge","entry_date":"2024-01-29","stage2_to_90D_outcome":"weak_stage2_low_MFE_bridge_missing","stage2_to_180D_outcome":"flat_followthrough_no_OEM_volume_margin_bridge","MFE90_ge20":false,"MAE180_le_minus20":false,"transition_note":"Seat-parts vocabulary without fresh OEM volume and margin/cash bridge should stay Watch/4B-risk despite limited drawdown."}
{"row_type":"stage_transition_summary","round":"R9","loop":"92","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","symbol":"033530","trigger_type":"Stage2-FalsePositive-ExhaustSystemLegacyAutopartsVocabularyNoDurableOEMVolumeBridge","entry_date":"2024-01-02","stage2_to_90D_outcome":"bad_stage2_sub20_MFE_bridge_missing","stage2_to_180D_outcome":"failed_exhaust_legacy_autoparts_deep_MAE_name_transition_watch","MFE90_ge20":false,"MAE180_le_minus25":true,"transition_note":"Exhaust/legacy auto-parts vocabulary without durable OEM volume and margin/cash bridge should remain Watch/4B-risk; 2024 name-transition needs repair."}
{"row_type":"residual_contribution","round":"R9","loop":"92","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","residual_type":"seat_exhaust_legacy_autoparts_vocabulary_overcredit_without_OEM_volume_mix_margin_cash_bridge","contribution":"Adds two C29 4B counterexamples against one auto interior OEM-volume positive, avoiding C29 top-covered and previous C29 loop symbols.","needs_coding_agent":true,"handoff_priority":"medium"}
{"row_type":"coverage_matrix","round":"R9","loop":"92","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"AUTO_INTERIOR_OEM_VOLUME_MIX_BRIDGE_VS_SEAT_EXHAUST_PARTS_VOCABULARY_DECAY","positive_case_count":1,"counterexample_count":2,"4B_case_count":2,"4C_case_count":0,"new_independent_case_count":3,"reused_case_count":0,"calibration_usable_trigger_count":3,"representative_trigger_count":3,"current_profile_error_count":2,"sector_rule_candidate":false,"canonical_rule_candidate":true,"coverage_gap_after_this_loop":"C29 now has non-top-symbol auto-interior OEM-volume positive and two seat/exhaust weak-bridge counterexamples; next R9 loops should exact-URL repair OEM/customer volume, model/program mix, utilization, price/cost pass-through, margin and cash-conversion evidence."}
```

## 10. Shadow rule candidates

```jsonl
{"row_type":"shadow_weight","round":"R9","loop":"92","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","axis":"C29_OEM_volume_program_mix_margin_cash_bridge_required","scope":"canonical_archetype","candidate_delta":1.0,"direction":"tighten","apply_now":false,"shadow_only":true,"evidence_basis":"007860 worked when auto interior OEM-volume/program-mix proxy existed; 005710 and 033530 failed when seat/exhaust vocabulary lacked fresh OEM volume, utilization and margin bridge."}
{"row_type":"shadow_weight","round":"R9","loop":"92","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","axis":"C29_seat_exhaust_legacy_autoparts_local_4B_guard","scope":"canonical_archetype","candidate_delta":1.0,"direction":"guardrail","apply_now":false,"shadow_only":true,"evidence_basis":"Seat and exhaust auto-parts rows showed low/sub-15 MFE or deep MAE when non-price OEM volume/margin evidence was missing."}
{"row_type":"shadow_weight","round":"R9","loop":"92","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","axis":"C29_name_transition_data_quality_guard","scope":"canonical_archetype","candidate_delta":1.0,"direction":"data_quality_guard","apply_now":false,"shadow_only":true,"evidence_basis":"033530 changed names during 2024, so production patching requires price-path and evidence repair."}
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
  - seat_parts_vocabulary_overcredit
  - exhaust_system_legacy_autoparts_vocabulary_overcredit
  - OEM_customer_volume_bridge_missing
  - utilization_pricing_margin_cash_bridge_missing
  - 2024_name_transition_watch
new_axis_proposed:
  - C29_OEM_volume_program_mix_margin_cash_bridge_required_shadow_only
  - C29_seat_exhaust_legacy_autoparts_local_4B_guard_shadow_only
  - C29_name_transition_data_quality_guard_shadow_only
existing_axis_strengthened:
  - price_only_blowoff_blocks_positive_stage within C29
  - full_4b_requires_non_price_evidence within C29
  - hard_4c_thesis_break_routes_to_4c within C29
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
`007860` has historical name-transition before 2024; the selected 2024 window is usable.
`005710` has older corporate-action candidates before 2024; the selected 2024 window is usable.
`033530` has an old corporate-action candidate before 2024 and name changes within 2024, so it remains name-transition data-quality watch before patching.
The non-price evidence layer remains source-name/proxy level for all three rows.

```text
calibration_usable = true for price-path residual analysis
evidence_url_pending = true
source_proxy_only = true
name_transition_watch = true for 033530
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
3. Confirm R9 / L3 / C29 round-sector consistency.
4. Check no hard duplicate exists by canonical_archetype_id + symbol + trigger_type + entry_date.
5. Confirm this loop avoided:
   - C29 top-covered symbols
   - previous R9 loop84 symbols
   - previous R9 loop85 symbols
   - previous R9 loop86 symbols
   - previous R9 loop87 symbols
   - previous R9 loop88 symbols
   - previous R9 loop89 symbols
   - previous R9 loop90 symbols
   - previous R9 loop91 symbols
   - earlier known C29 symbols listed in this MD
6. Confirm stale R8/C28, R7/C25 and earlier-sector candidate rows are not ingested from this MD.
7. Keep 033530 in name-transition data-quality watch before patch consideration.
8. If aggregate support remains stable after exact evidence URL repair, consider C29-scoped safe patch candidates:
   - C29_OEM_volume_program_mix_margin_cash_bridge_required
   - C29_seat_exhaust_legacy_autoparts_local_4B_guard
   - C29_name_transition_data_quality_guard
9. Do not loosen Stage3-Green.
10. Do not use future MFE/MAE in runtime scoring.
11. Use this MD only for calibration profile planning.
```

## 14. Round state

```text
completed_round = R9
completed_loop = 92
next_round = R10
next_loop = 92
round_schedule_status = valid
round_sector_consistency = pass
production_scoring_changed = false
shadow_weight_only = true
```

## 15. Final one-line contribution

```text
This loop adds 3 new independent cases, 1 positive, 2 counterexamples, and 2 local 4B-watch rows for R9/L3_BATTERY_EV_GREEN_MOBILITY/C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE.
```
