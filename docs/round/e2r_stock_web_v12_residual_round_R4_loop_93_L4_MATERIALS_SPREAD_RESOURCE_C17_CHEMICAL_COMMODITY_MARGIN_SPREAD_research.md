# E2R Stock-Web v12 Residual Research — R4 Loop 93 / L4 / C17

```yaml
schema_family: v12_sector_archetype_residual
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
round: R4
loop: 93
large_sector_id: L4_MATERIALS_SPREAD_RESOURCE
canonical_archetype_id: C17_CHEMICAL_COMMODITY_MARGIN_SPREAD
fine_archetype_id: SPECIALTY_CHEMICAL_SPREAD_RESET_VS_CHLORALKALI_AND_INDUSTRIAL_MATERIALS_MARGIN_DECAY
sector: materials / chemical / specialty chemical / commodity spread / chlor-alkali / industrial materials / raw-material spread / margin bridge / FCF conversion
output_file: e2r_stock_web_v12_residual_round_R4_loop_93_L4_MATERIALS_SPREAD_RESOURCE_C17_CHEMICAL_COMMODITY_MARGIN_SPREAD_research.md
production_scoring_changed: false
shadow_weight_only: true
stock_agent_code_accessed: false
handoff_prompt_embedded: true
handoff_prompt_executed_now: false
```

## 1. Scope lock

This run follows the current v12 coverage-index-first scheduler after recent loop93 expansions in C09, C01, C07, C06, C10, C11, C19, C27, C24, C12 and C13.

```text
selected_round = R4
selected_loop = 93
large_sector_id = L4_MATERIALS_SPREAD_RESOURCE
canonical_archetype_id = C17_CHEMICAL_COMMODITY_MARGIN_SPREAD
```

Reason for selecting C17:

```text
v12 scheduler = coverage_index_first
sequential_round_cycle_required = false
coverage_gap_can_override_previous_round = true
selected_archetype_drives_round = true
```

No-Repeat Index under-30 snapshot used as duplicate-avoidance ledger:

```text
C17_CHEMICAL_COMMODITY_MARGIN_SPREAD = 29 rows / need_to_30 = 1
C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION = 29 rows / need_to_30 = 1
C28_SOFTWARE_SECURITY_CONTRACT_RETENTION = 27 rows / need_to_30 = 3 by raw index, but local loop92 already expanded C28 once
```

C17 can cross the 30-row minimum-stability threshold with one additional representative row, but this run still keeps the normal 3-row positive/counterexample balance.

This loop avoids C17 top-covered and recent material-sector symbols:

```text
C17 top-covered = 009830, 011170, 010060, 298000, 001340, 002380

Recent adjacent material/battery rows avoided:
R4 loop88 C15: 004020, 006110, 001430
R4 loop89 C16: 009520, 006260, 011810
R4 loop90 C15: 008350, 010060, 001340
R4 loop91 C16: 000670, 025820, 036460
R4 loop92 C16: 001120, 000910, 001550
R3 loop93 C11/C12/C13: 348370, 121600, 020150, 373220, 006400, 005070, 003670, 086520, 278280
```

Candidate hygiene note:

```text
During this execution path, C13/C12 battery rows such as 003670, 086520 and 278280 were visible from the stream.
They are not used in this C17 output because the valid output must be R4/L4/C17.
```

Selected symbols:

```text
014680, 004000, 120110
```

The selected pocket is:

```text
specialty chemical / semiconductor chemical spread reset positive-watch
vs
chlor-alkali / ammonia / commodity chemical vocabulary without durable spread-margin bridge
vs
industrial-materials / tire-cord / resin spread vocabulary without pricing-power and FCF bridge
```

This is not a live stock recommendation, not a `stock_agent` code patch, and not a production scoring change.

## 2. Price atlas validation

```jsonl
{"row_type":"price_source_validation","source_name":"FinanceData/marcap via Songdaiki/stock-web","price_data_source":"Songdaiki/stock-web","upstream_source":"FinanceData/marcap","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","manifest_min_date":"1995-05-02","manifest_max_date":"2026-02-20","tradable_row_count":14354401,"raw_row_count":15214118,"symbol_count":5414,"active_like_symbol_count":2868,"corporate_action_candidate_count":14435,"calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","schema_path":"atlas/schema.json","notes":"Raw/unadjusted OHLC; zero-volume and invalid OHLC rows are excluded from tradable shards; corporate-action-contaminated windows are blocked by default."}
{"row_type":"price_source_validation","symbol":"014680","company_name":"한솔케미칼","profile_path":"atlas/symbol_profiles/014/014680.json","first_date":"1995-05-02","last_date":"2026-02-20","trading_day_count":7764,"corporate_action_candidate_count":1,"corporate_action_candidate_dates":["1999-07-12"],"has_major_raw_discontinuity":true,"calibration_caveat":"Historical corporate-action/name-transition candidate exists long before selected 2024 window.","status_inferred":"active_like","price_adjustment_status":"raw_unadjusted_marcap","profile_check":"2024_forward_window_usable"}
{"row_type":"price_source_validation","symbol":"004000","company_name":"롯데정밀화학","profile_path":"atlas/symbol_profiles/004/004000.json","first_date":"1995-05-02","last_date":"2026-02-20","trading_day_count":7749,"corporate_action_candidate_count":"profile_tail_not_fetched_in_this_run","corporate_action_candidate_dates":"historical_name_transition_before_2024","has_major_raw_discontinuity":true,"calibration_caveat":"Name changed from 삼성정밀화학 to 롯데정밀화학 in 2016, before selected 2024 window. Selected 2024 window is usable for residual analysis.","status_inferred":"active_like","price_adjustment_status":"raw_unadjusted_marcap","profile_check":"2024_forward_window_usable"}
{"row_type":"price_source_validation","symbol":"120110","company_name":"코오롱인더","profile_path":"atlas/symbol_profiles/120/120110.json","first_date":"2010-02-01","last_date":"2026-02-20","trading_day_count":3952,"corporate_action_candidate_count":1,"corporate_action_candidate_dates":["2010-12-27"],"has_major_raw_discontinuity":true,"calibration_caveat":"Historical corporate-action candidate exists long before selected 2024 window.","status_inferred":"active_like","price_adjustment_status":"raw_unadjusted_marcap","profile_check":"2024_forward_window_usable"}
```

## 3. No-repeat and novelty check

Hard duplicate key applied:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

New keys introduced:

```jsonl
{"row_type":"narrative_only","check":"no_repeat_key","canonical_archetype_id":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD","symbol":"014680","trigger_type":"Stage2-Actionable-SpecialtyChemicalSpreadResetMarginBridge-PositiveWatch","entry_date":"2024-02-27","duplicate_status":"new C17 symbol/trigger/date combination outside C17 top-covered and recent R4 loop symbols"}
{"row_type":"narrative_only","check":"no_repeat_key","canonical_archetype_id":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD","symbol":"004000","trigger_type":"Stage2-FalsePositive-ChlorAlkaliAmmoniaCommodityVocabularyNoDurableSpreadMarginBridge","entry_date":"2024-01-02","duplicate_status":"new C17 symbol/trigger/date combination outside C17 top-covered and recent R4 loop symbols"}
{"row_type":"narrative_only","check":"no_repeat_key","canonical_archetype_id":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD","symbol":"120110","trigger_type":"Stage2-FalsePositive-IndustrialMaterialsSpreadVocabularyNoPricingPowerFCFBridge","entry_date":"2024-01-02","duplicate_status":"new C17 symbol/trigger/date combination outside C17 top-covered and recent R4 loop symbols"}
```

## 4. Research question

C17 is not “화학/스프레드가 좋아진다.”
The useful signal must prove a raw-material-to-margin chain:

```text
product spread improvement
raw-material or feedstock cost relief
pricing-power or pass-through discipline
inventory revaluation control
volume / utilization recovery
mix quality
gross-margin / operating-margin bridge
working-capital discipline
FCF conversion
late-cycle spread reversal risk
```

A spread headline without this bridge is a widening crack drawn on paper. It matters only if the realized selling price, feedstock cost, volume, inventory mark and cash ledger move together.

Residual question:

```text
Can C17 distinguish:
1. specialty chemical / semiconductor chemical spread reset where MFE opens but late drawdown keeps Green strict,
2. chlor-alkali / ammonia commodity vocabulary with no durable spread-margin bridge,
3. industrial-materials / resin / tire-cord vocabulary with weak pricing-power and FCF conversion?
```

## 5. Case rows

```jsonl
{"row_type":"case","case_id":"C17_R4L93_014680_HANSOL_SPECIALTY_CHEM_SPREAD","symbol":"014680","company_name":"한솔케미칼","round":"R4","loop":"93","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD","fine_archetype_id":"SPECIALTY_CHEMICAL_SEMICONDUCTOR_CHEMICAL_SPREAD_RESET_MARGIN_BRIDGE","case_type":"structural_success_watch","positive_or_counterexample":"positive","best_trigger":"Stage2-Actionable-SpecialtyChemicalSpreadResetMarginBridge-PositiveWatch","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"positive_watch_MFE90_ge20_low_initial_MAE_but_late_drawdown","current_profile_verdict":"current_profile_correct_if_spread_cost_margin_FCF_bridge_required_but_Green_strict","price_source":"Songdaiki/stock-web","notes":"Specialty chemical / semiconductor chemical spread-reset proxy produced MFE90 above 20 with very shallow initial MAE, but later drawdown keeps this positive-watch only unless exact spread, cost, margin and cash evidence is repaired."}
{"row_type":"case","case_id":"C17_R4L93_004000_LOTTE_FINE_CHLORALKALI_DECAY","symbol":"004000","company_name":"롯데정밀화학","round":"R4","loop":"93","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD","fine_archetype_id":"CHLORALKALI_AMMONIA_COMMODITY_VOCABULARY_WITHOUT_DURABLE_SPREAD_MARGIN_BRIDGE","case_type":"failed_entry","positive_or_counterexample":"counterexample","best_trigger":"Stage2-FalsePositive-ChlorAlkaliAmmoniaCommodityVocabularyNoDurableSpreadMarginBridge","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"counterexample_near_zero_MFE_deep_MAE_no_durable_spread_margin_bridge","current_profile_verdict":"current_profile_false_positive_if_chloralkali_ammonia_spread_vocabulary_overcredited","price_source":"Songdaiki/stock-web","notes":"Chlor-alkali/ammonia commodity-spread vocabulary had near-zero MFE and deep drawdown when realized spread, margin and FCF bridge were not repaired."}
{"row_type":"case","case_id":"C17_R4L93_120110_KOLON_INDUSTRIES_MATERIALS_DECAY","symbol":"120110","company_name":"코오롱인더","round":"R4","loop":"93","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD","fine_archetype_id":"INDUSTRIAL_MATERIALS_RESIN_TIRECORD_SPREAD_VOCABULARY_WITHOUT_PRICING_POWER_FCF_BRIDGE","case_type":"failed_entry","positive_or_counterexample":"counterexample","best_trigger":"Stage2-FalsePositive-IndustrialMaterialsSpreadVocabularyNoPricingPowerFCFBridge","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"counterexample_low_MFE_deep_MAE_no_pricing_power_FCF_bridge","current_profile_verdict":"current_profile_false_positive_if_industrial_materials_spread_vocabulary_overcredited","price_source":"Songdaiki/stock-web","notes":"Industrial materials / resin / tire-cord spread vocabulary had weak forward MFE and persistent drawdown without pricing-power, utilization, margin or FCF bridge."}
```

## 6. Trigger-level Stock-Web rows

### 6.1 014680 한솔케미칼 — specialty chemical spread reset / margin bridge positive-watch

Entry row: `2024-02-27 c=169300`, after a sharp first-quarter reset.
Observed path: local high `2024-03-21 h=214000`, followed by late-cycle decline to `2024-11-15 l=98800`.

```jsonl
{"row_type":"trigger","trigger_id":"R4L93_C17_014680_20240227_STAGE2_SPECIALTY_CHEM_SPREAD_RESET","case_id":"C17_R4L93_014680_HANSOL_SPECIALTY_CHEM_SPREAD","symbol":"014680","company_name":"한솔케미칼","round":"R4","loop":"93","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD","fine_archetype_id":"SPECIALTY_CHEMICAL_SEMICONDUCTOR_CHEMICAL_SPREAD_RESET_MARGIN_BRIDGE","loop_objective":"holdout_validation;canonical_archetype_rule_candidate;green_strictness_stress_test","trigger_type":"Stage2-Actionable-SpecialtyChemicalSpreadResetMarginBridge-PositiveWatch","trigger_date":"2024-02-27","entry_date":"2024-02-27","entry_price":169300.0,"entry_price_basis":"close","evidence_available_at_that_date":"historical_public_specialty_chemical_semiconductor_chemical_spread_reset_proxy_available_by_entry","evidence_source":"source-name-level proxy; exact URL pending; specialty chemical spread, feedstock cost relief, mix quality, margin and cash bridge treated as non-price proxy, not final citation-grade evidence","evidence_source_type":"historical_public_report_consensus_proxy","source_proxy_only":true,"evidence_url_pending":true,"stage2_evidence_fields":["specialty_chemical_spread_proxy","feedstock_cost_relief_proxy","semiconductor_chemical_mix_proxy","relative_strength_after_reset"],"stage3_evidence_fields":["exact_spread_source_pending","raw_material_cost_source_pending","gross_margin_source_pending","FCF_bridge_pending"],"stage4b_evidence_fields":["late_drawdown_watch","Green_strict_watch"],"stage4c_evidence_fields":["spread_reversal_watch_only"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/014/014680/2024.csv","profile_path":"atlas/symbol_profiles/014/014680.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":26.40,"MFE_90D_pct":26.40,"MFE_180D_pct":26.40,"MAE_30D_pct":-0.41,"MAE_90D_pct":-0.41,"MAE_180D_pct":-41.64,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-03-21","peak_price":214000.0,"max_drawdown_low_date":"2024-11-15","max_drawdown_low":98800.0,"drawdown_after_peak_pct":-53.83,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"positive_watch_but_Green_requires_exact_spread_cost_margin_FCF_evidence_and_late_drawdown_review","four_b_evidence_type":["late_drawdown_watch","Green_strict_watch"],"four_c_protection_label":"spread_reversal_watch_only","trigger_outcome_label":"positive_watch_MFE90_ge20_low_initial_MAE_but_late_drawdown","current_profile_verdict":"current_profile_correct_if_spread_cost_margin_FCF_bridge_required_but_Green_strict","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"historical_candidate_pre_2024; selected_window_clean","same_entry_group_id":"014680_2024-02-27_169300","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"current_profile_residual":"C17 can allow Yellow/positive-watch when chemical strength is tied to realized spread, feedstock cost relief, mix quality, margin and FCF. Late drawdown and source-proxy evidence block automatic Green."}
```

### 6.2 004000 롯데정밀화학 — chlor-alkali / ammonia commodity vocabulary without durable spread-margin bridge

Entry row: `2024-01-02 c=56600`.
Observed path: same-day high `2024-01-02 h=58100`, then persistent weakness into the second half and later low near `2024-11-29 l=34000`.

```jsonl
{"row_type":"trigger","trigger_id":"R4L93_C17_004000_20240102_STAGE2_FALSE_POSITIVE_CHLORALKALI_AMMONIA","case_id":"C17_R4L93_004000_LOTTE_FINE_CHLORALKALI_DECAY","symbol":"004000","company_name":"롯데정밀화학","round":"R4","loop":"93","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD","fine_archetype_id":"CHLORALKALI_AMMONIA_COMMODITY_VOCABULARY_WITHOUT_DURABLE_SPREAD_MARGIN_BRIDGE","loop_objective":"residual_false_positive_mining;counterexample_mining;4B_non_price_requirement_stress_test","trigger_type":"Stage2-FalsePositive-ChlorAlkaliAmmoniaCommodityVocabularyNoDurableSpreadMarginBridge","trigger_date":"2024-01-02","entry_date":"2024-01-02","entry_price":56600.0,"entry_price_basis":"close","evidence_available_at_that_date":"historical_public_chloralkali_ammonia_commodity_spread_vocabulary_proxy_available_by_entry","evidence_source":"source-name-level proxy; exact URL pending; chlor-alkali/ammonia commodity-spread vocabulary treated as insufficient without realized spread, margin and FCF bridge","evidence_source_type":"historical_public_report_news_proxy","source_proxy_only":true,"evidence_url_pending":true,"stage2_evidence_fields":["chloralkali_spread_vocabulary","ammonia_commodity_cycle_keyword","relative_strength_rebound"],"stage3_evidence_fields":["realized_spread_missing","feedstock_pass_through_missing","gross_margin_bridge_missing","FCF_conversion_missing"],"stage4b_evidence_fields":["near_zero_MFE","deep_MAE","spread_margin_bridge_missing_watch"],"stage4c_evidence_fields":["spread_reversal_watch_only"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/004/004000/2024.csv","profile_path":"atlas/symbol_profiles/004/004000.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":2.65,"MFE_90D_pct":2.65,"MFE_180D_pct":2.65,"MAE_30D_pct":-17.93,"MAE_90D_pct":-18.20,"MAE_180D_pct":-23.06,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-01-02","peak_price":58100.0,"max_drawdown_low_date":"2024-11-29","max_drawdown_low":34000.0,"drawdown_after_peak_pct":-41.48,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"chloralkali_ammonia_vocabulary_without_realized_spread_margin_FCF_bridge_should_be_4B_watch_not_positive","four_b_evidence_type":["near_zero_MFE","deep_MAE","spread_margin_bridge_missing_watch"],"four_c_protection_label":"spread_reversal_watch_only","trigger_outcome_label":"counterexample_near_zero_MFE_deep_MAE_no_durable_spread_margin_bridge","current_profile_verdict":"current_profile_false_positive_if_chloralkali_ammonia_spread_vocabulary_overcredited","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"historical_name_transition_pre_2024; selected_window_clean","same_entry_group_id":"004000_2024-01-02_56600","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"current_profile_residual":"C17 should not promote chlor-alkali/ammonia vocabulary unless realized spread, feedstock pass-through, margin and FCF evidence are exact-repaired. Near-zero MFE and deep MAE force Watch/4B routing."}
```

### 6.3 120110 코오롱인더 — industrial-materials spread vocabulary without pricing-power / FCF bridge

Entry row: `2024-01-02 c=44000`.
Observed path: local high `2024-01-04 h=45800`, then repeated drawdowns and later low near `2024-11-29 l=34000`.

```jsonl
{"row_type":"trigger","trigger_id":"R4L93_C17_120110_20240102_STAGE2_FALSE_POSITIVE_INDUSTRIAL_MATERIALS","case_id":"C17_R4L93_120110_KOLON_INDUSTRIES_MATERIALS_DECAY","symbol":"120110","company_name":"코오롱인더","round":"R4","loop":"93","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD","fine_archetype_id":"INDUSTRIAL_MATERIALS_RESIN_TIRECORD_SPREAD_VOCABULARY_WITHOUT_PRICING_POWER_FCF_BRIDGE","loop_objective":"residual_false_positive_mining;counterexample_mining;4B_non_price_requirement_stress_test","trigger_type":"Stage2-FalsePositive-IndustrialMaterialsSpreadVocabularyNoPricingPowerFCFBridge","trigger_date":"2024-01-02","entry_date":"2024-01-02","entry_price":44000.0,"entry_price_basis":"close","evidence_available_at_that_date":"historical_public_industrial_materials_resin_tirecord_spread_vocabulary_proxy_available_by_entry","evidence_source":"source-name-level proxy; exact URL pending; industrial materials/resin/tire-cord spread vocabulary treated as insufficient without pricing power, utilization, margin and FCF bridge","evidence_source_type":"historical_public_report_news_proxy","source_proxy_only":true,"evidence_url_pending":true,"stage2_evidence_fields":["industrial_materials_spread_vocabulary","resin_tirecord_cycle_keyword","relative_strength_watch"],"stage3_evidence_fields":["pricing_power_missing","utilization_recovery_missing","gross_margin_bridge_missing","FCF_conversion_missing"],"stage4b_evidence_fields":["low_MFE","deep_MAE","pricing_power_FCF_bridge_missing_watch"],"stage4c_evidence_fields":["spread_reversal_watch_only"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/120/120110/2024.csv","profile_path":"atlas/symbol_profiles/120/120110.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":4.09,"MFE_90D_pct":4.09,"MFE_180D_pct":4.09,"MAE_30D_pct":-14.09,"MAE_90D_pct":-17.61,"MAE_180D_pct":-22.73,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-01-04","peak_price":45800.0,"max_drawdown_low_date":"2024-11-29","max_drawdown_low":34000.0,"drawdown_after_peak_pct":-25.76,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"industrial_materials_spread_vocabulary_without_pricing_power_utilization_margin_FCF_bridge_should_be_4B_watch_not_positive","four_b_evidence_type":["low_MFE","deep_MAE","pricing_power_FCF_bridge_missing_watch"],"four_c_protection_label":"spread_reversal_watch_only","trigger_outcome_label":"counterexample_low_MFE_deep_MAE_no_pricing_power_FCF_bridge","current_profile_verdict":"current_profile_false_positive_if_industrial_materials_spread_vocabulary_overcredited","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"historical_candidate_pre_2024; selected_window_clean","same_entry_group_id":"120110_2024-01-02_44000","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"current_profile_residual":"C17 should not count industrial-materials/resin/tire-cord vocabulary as margin-spread evidence unless pricing power, utilization, gross-margin and FCF conversion are repaired."}
```

## 7. Score simulation rows

```jsonl
{"row_type":"score_simulation","profile_id":"P0_e2r_2_1_stock_web_calibrated_proxy","case_id":"C17_R4L93_014680_HANSOL_SPECIALTY_CHEM_SPREAD","trigger_id":"R4L93_C17_014680_20240227_STAGE2_SPECIALTY_CHEM_SPREAD_RESET","symbol":"014680","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD","profile_scope":"current_default_proxy","profile_hypothesis":"current profile works if C17 requires realized spread, feedstock cost relief, mix, margin and FCF bridge rather than chemical vocabulary alone","raw_component_scores_before":{"realized_spread_score":10,"feedstock_cost_relief_score":10,"pricing_power_score":8,"mix_quality_score":9,"utilization_recovery_score":8,"gross_margin_bridge_score":9,"OPM_bridge_score":7,"working_capital_score":7,"FCF_bridge_score":6,"relative_strength_score":10,"spread_reversal_risk":-5,"theme_spike_risk":-2,"information_confidence":4},"weighted_score_before":64,"stage_label_before":"Stage2-Watch/PositiveControl","raw_component_scores_after":{"realized_spread_score":13,"feedstock_cost_relief_score":13,"pricing_power_score":10,"mix_quality_score":11,"utilization_recovery_score":10,"gross_margin_bridge_score":11,"OPM_bridge_score":9,"working_capital_score":9,"FCF_bridge_score":8,"relative_strength_score":12,"spread_reversal_risk":-4,"theme_spike_risk":-1,"information_confidence":5},"weighted_score_after":80,"stage_label_after":"Stage2-Actionable/Yellow-Watch","component_delta_explanation":"Specialty chemical spread reset plus MFE90 supports Yellow-watch; late drawdown and proxy-only evidence block automatic Green."}
{"row_type":"score_simulation","profile_id":"P0_e2r_2_1_stock_web_calibrated_proxy","case_id":"C17_R4L93_004000_LOTTE_FINE_CHLORALKALI_DECAY","trigger_id":"R4L93_C17_004000_20240102_STAGE2_FALSE_POSITIVE_CHLORALKALI_AMMONIA","symbol":"004000","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD","profile_scope":"current_default_proxy","profile_hypothesis":"chlor-alkali/ammonia vocabulary without realized spread and FCF bridge should be blocked","raw_component_scores_before":{"realized_spread_score":1,"feedstock_cost_relief_score":1,"pricing_power_score":0,"mix_quality_score":0,"utilization_recovery_score":0,"gross_margin_bridge_score":0,"OPM_bridge_score":0,"working_capital_score":0,"FCF_bridge_score":0,"relative_strength_score":1,"spread_reversal_risk":-12,"theme_spike_risk":-12,"information_confidence":3},"weighted_score_before":0,"stage_label_before":"Stage2-Watch/FalsePositive","raw_component_scores_after":{"realized_spread_score":0,"feedstock_cost_relief_score":0,"pricing_power_score":0,"mix_quality_score":0,"utilization_recovery_score":0,"gross_margin_bridge_score":0,"OPM_bridge_score":0,"working_capital_score":0,"FCF_bridge_score":0,"relative_strength_score":0,"spread_reversal_risk":-20,"theme_spike_risk":-18,"information_confidence":2},"weighted_score_after":0,"stage_label_after":"Stage1/4B-Watch","component_delta_explanation":"Near-zero MFE and deep MAE require realized spread, margin and FCF evidence before any promotion."}
{"row_type":"score_simulation","profile_id":"P0_e2r_2_1_stock_web_calibrated_proxy","case_id":"C17_R4L93_120110_KOLON_INDUSTRIES_MATERIALS_DECAY","trigger_id":"R4L93_C17_120110_20240102_STAGE2_FALSE_POSITIVE_INDUSTRIAL_MATERIALS","symbol":"120110","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD","profile_scope":"current_default_proxy","profile_hypothesis":"industrial materials spread vocabulary without pricing-power and FCF bridge should remain Watch/4B","raw_component_scores_before":{"realized_spread_score":1,"feedstock_cost_relief_score":1,"pricing_power_score":0,"mix_quality_score":1,"utilization_recovery_score":0,"gross_margin_bridge_score":0,"OPM_bridge_score":0,"working_capital_score":0,"FCF_bridge_score":0,"relative_strength_score":2,"spread_reversal_risk":-10,"theme_spike_risk":-12,"information_confidence":3},"weighted_score_before":0,"stage_label_before":"Stage2-Watch/FalsePositive","raw_component_scores_after":{"realized_spread_score":0,"feedstock_cost_relief_score":0,"pricing_power_score":0,"mix_quality_score":0,"utilization_recovery_score":0,"gross_margin_bridge_score":0,"OPM_bridge_score":0,"working_capital_score":0,"FCF_bridge_score":0,"relative_strength_score":0,"spread_reversal_risk":-18,"theme_spike_risk":-18,"information_confidence":2},"weighted_score_after":0,"stage_label_after":"Stage1/4B-Watch","component_delta_explanation":"Low MFE and persistent drawdown require pricing-power, utilization, margin and FCF evidence before any Yellow/Green promotion."}
```

## 8. Aggregate and transition rows

```jsonl
{"row_type":"aggregate_metric","round":"R4","loop":"93","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD","fine_archetype_id":"C17_SPECIALTY_CHEM_POSITIVE_VS_COMMODITY_INDUSTRIAL_DECAY","row_count":3,"unique_symbol_count":3,"positive_case_count":1,"counterexample_count":2,"good_stage2_count":1,"bad_stage2_count":2,"4B_case_count":2,"4C_case_count":0,"source_proxy_only_count":3,"evidence_url_pending_count":3,"calibration_usable_count":3,"avg_MFE90_pct":11.05,"avg_MAE90_pct":-12.07,"avg_MFE180_pct":11.05,"avg_MAE180_pct":-29.14,"stage2_hit_rate_MFE90_ge20":0.33,"stage2_bad_entry_rate_bridge_missing":0.67,"stage2_bad_entry_rate_MAE180_le_minus20":1.0,"interpretation":"C17 needs realized-spread discipline. 한솔케미칼 shows specialty chemical spread reset can support Yellow/positive-watch, while 롯데정밀화학 and 코오롱인더 show commodity/industrial-material spread vocabulary should not be promoted without pricing power, realized margin and FCF evidence."}
{"row_type":"stage_transition_summary","round":"R4","loop":"93","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD","symbol":"014680","trigger_type":"Stage2-Actionable-SpecialtyChemicalSpreadResetMarginBridge-PositiveWatch","entry_date":"2024-02-27","stage2_to_90D_outcome":"positive_watch_MFE90_ge20_low_MAE","stage2_to_180D_outcome":"specialty_chemical_spread_bridge_but_late_drawdown_Green_strict","MFE90_ge20":true,"MAE90_le_minus20":false,"transition_note":"Allow Yellow/positive-watch when chemical strength is tied to realized spread, cost relief, margin and FCF; Green requires exact evidence."}
{"row_type":"stage_transition_summary","round":"R4","loop":"93","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD","symbol":"004000","trigger_type":"Stage2-FalsePositive-ChlorAlkaliAmmoniaCommodityVocabularyNoDurableSpreadMarginBridge","entry_date":"2024-01-02","stage2_to_90D_outcome":"bad_stage2_near_zero_MFE_spread_bridge_missing","stage2_to_180D_outcome":"failed_chloralkali_ammonia_vocabulary_deep_MAE","MFE90_ge20":false,"MAE180_le_minus20":true,"transition_note":"Commodity-spread vocabulary without realized spread/margin/FCF bridge should stay Watch/4B-risk."}
{"row_type":"stage_transition_summary","round":"R4","loop":"93","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD","symbol":"120110","trigger_type":"Stage2-FalsePositive-IndustrialMaterialsSpreadVocabularyNoPricingPowerFCFBridge","entry_date":"2024-01-02","stage2_to_90D_outcome":"bad_stage2_low_MFE_pricing_power_missing","stage2_to_180D_outcome":"failed_industrial_materials_spread_vocabulary_deep_MAE","MFE90_ge20":false,"MAE180_le_minus20":true,"transition_note":"Industrial-materials spread vocabulary without pricing-power and FCF bridge should remain Watch/4B."}
{"row_type":"residual_contribution","round":"R4","loop":"93","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD","residual_type":"commodity_industrial_spread_vocabulary_overcredit_without_realized_margin_FCF_bridge","contribution":"Adds two C17 4B counterexamples against one specialty-chemical spread reset positive-watch, bringing C17 from 29 beyond the 30-row minimum stability threshold.","needs_coding_agent":true,"handoff_priority":"medium"}
{"row_type":"coverage_matrix","round":"R4","loop":"93","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD","fine_archetype_id":"SPECIALTY_CHEMICAL_SPREAD_RESET_VS_CHLORALKALI_AND_INDUSTRIAL_MATERIALS_MARGIN_DECAY","positive_case_count":1,"counterexample_count":2,"4B_case_count":2,"4C_case_count":0,"new_independent_case_count":3,"reused_case_count":0,"calibration_usable_trigger_count":3,"representative_trigger_count":3,"current_profile_error_count":2,"sector_rule_candidate":false,"canonical_rule_candidate":true,"coverage_gap_after_this_loop":"C17 now has one specialty chemical spread reset positive-watch and two commodity/industrial weak-bridge counterexamples; next C17 loops should exact-URL repair realized spread, feedstock cost relief, pricing power, margin and FCF evidence."}
```

## 9. Shadow rule candidates

```jsonl
{"row_type":"shadow_weight","round":"R4","loop":"93","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD","axis":"C17_realized_spread_margin_FCF_bridge_required","scope":"canonical_archetype","candidate_delta":1.0,"direction":"tighten","apply_now":false,"shadow_only":true,"evidence_basis":"014680 worked as positive-watch only when spread/margin proxy existed; 004000 and 120110 failed when realized spread and FCF evidence was missing."}
{"row_type":"shadow_weight","round":"R4","loop":"93","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD","axis":"C17_commodity_industrial_vocabulary_local_4B_guard","scope":"canonical_archetype","candidate_delta":1.0,"direction":"guardrail","apply_now":false,"shadow_only":true,"evidence_basis":"004000 and 120110 showed near-zero/low MFE and deep MAE when spread vocabulary was not tied to realized margin and FCF."}
{"row_type":"shadow_weight","round":"R4","loop":"93","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD","axis":"C17_late_drawdown_Green_strict_guard","scope":"canonical_archetype","candidate_delta":1.0,"direction":"green_strictness_guard","apply_now":false,"shadow_only":true,"evidence_basis":"014680 had MFE90 above 20 but later drawdown exceeded -40%; Green requires exact spread/margin/FCF evidence."}
```

## 10. Residual Contribution Summary

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
  - commodity_spread_vocabulary_overcredit
  - industrial_materials_spread_vocabulary_overcredit
  - realized_spread_bridge_missing
  - pricing_power_margin_FCF_bridge_missing
  - late_drawdown_Green_strict_watch
new_axis_proposed:
  - C17_realized_spread_margin_FCF_bridge_required_shadow_only
  - C17_commodity_industrial_vocabulary_local_4B_guard_shadow_only
  - C17_late_drawdown_Green_strict_guard_shadow_only
existing_axis_strengthened:
  - price_only_blowoff_blocks_positive_stage within C17
  - full_4b_requires_non_price_evidence within C17
  - hard_4c_thesis_break_routes_to_4c within C17
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

## 11. Data-quality caveat

All selected triggers use Stock-Web tradable raw OHLC rows.
`014680` has an old 1999 corporate-action/name-transition candidate before 2024; the selected 2024 window is usable.
`004000` changed name long before 2024; the selected 2024 window is usable.
`120110` has an old 2010 corporate-action candidate before 2024; the selected 2024 window is usable.
The non-price evidence layer remains source-name/proxy level for all three rows.

```text
calibration_usable = true for price-path residual analysis
evidence_url_pending = true
source_proxy_only = true
promotion should prefer hold / exact evidence repair until exact URLs are added
```

## 12. Deferred Coding Agent Handoff Prompt

```text
You are the coding agent for Songdaiki/stock_agent.

Do not execute this handoff during the research-writing session.

When a later batch implementation is requested:
1. Ingest this MD through run-v12-calibration.
2. Confirm all trigger rows validate with:
   - price_data_source=Songdaiki/stock-web
   - price_basis=tradable_raw
   - price_adjustment_status=raw_unadjusted_marcap
3. Confirm R4 / L4 / C17 round-sector consistency.
4. Check no hard duplicate exists by canonical_archetype_id + symbol + trigger_type + entry_date.
5. Confirm this loop was selected by coverage-index-first and brings C17 over the 30-row minimum stability threshold.
6. Confirm this loop avoided C17 top-covered symbols:
   - 009830
   - 011170
   - 010060
   - 298000
   - 001340
   - 002380
7. Confirm recently touched C13/C12 battery rows are not ingested from this MD.
8. Treat 014680 as Yellow/positive-watch only, not Green, until exact spread/cost/margin/FCF evidence is repaired.
9. Treat 004000 and 120110 as weak-bridge failure modes unless exact realized-spread/margin/FCF evidence is added later.
10. If aggregate support remains stable after exact evidence URL repair, consider C17-scoped safe patch candidates:
   - C17_realized_spread_margin_FCF_bridge_required
   - C17_commodity_industrial_vocabulary_local_4B_guard
   - C17_late_drawdown_Green_strict_guard
11. Do not loosen Stage3-Green.
12. Do not use future MFE/MAE in runtime scoring.
13. Use this MD only for calibration profile planning.
```

## 13. Round state

```text
completed_round = R4
completed_loop = 93
next_selection_mode = coverage_index_first
suggested_next_archetype = C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION or C28_SOFTWARE_SECURITY_CONTRACT_RETENTION depending on newest coverage pressure and recent-loop avoidance
round_schedule_status = valid
round_sector_consistency = pass
production_scoring_changed = false
shadow_weight_only = true
```

## 14. Final one-line contribution

```text
This loop adds 3 new independent cases, 1 specialty-chemical spread-reset positive-watch, 2 weak-bridge counterexamples, and 2 local 4B-watch rows for R4/L4_MATERIALS_SPREAD_RESOURCE/C17_CHEMICAL_COMMODITY_MARGIN_SPREAD.
```
