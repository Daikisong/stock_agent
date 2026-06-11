# E2R Historical Calibration v12 — C30 Construction PF Balance-Sheet Break Residual Research

```text
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
research_session = post_calibrated_sector_archetype_residual_research
production_scoring_changed = false
shadow_weight_only = true
handoff_prompt_embedded = true
handoff_prompt_executed_now = false
stock_agent_code_access_allowed = false
stock_agent_code_patch_allowed = false
stock_agent_live_scan_allowed = false
current_stock_discovery_allowed = false
auto_trading_allowed = false
```

## 0. Metadata

```yaml
output_file: e2r_stock_web_v12_residual_round_R10_loop_104_L9_CONSTRUCTION_REALESTATE_HOUSING_C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK_research.md
selected_round: R10
selected_loop: 104
large_sector_id: L9_CONSTRUCTION_REALESTATE_HOUSING
canonical_archetype_id: C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK
fine_archetype_id: CONSTRUCTION_PF_REPAIR_FOLLOW_THROUGH_VS_POST_PEAK_PRICE_ONLY_4B_FALSE_POSITIVE
selected_priority_bucket: Priority 0
round_schedule_status: coverage_index_selected
round_sector_consistency: pass
selection_basis: docs/core/V12_Research_No_Repeat_Index.md + conversation-local generated MD ledger
primary_price_source: Songdaiki/stock-web
stock_web_manifest_max_date: 2026-02-20
price_basis: tradable_raw
price_adjustment_status: raw_unadjusted_marcap
price_row_fetch_status: local_prior_stock_web_rows_reused_or_derived_for_same_shard_paths
batch_reverification_required: true
```

## 1. Selection rationale

`V12_Research_No_Repeat_Index.md` keeps **C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK** in Priority 0, with only 3 static rows and a large gap to the 30-row floor. Conversation-local C30 coverage has improved, but it is still thinner than most other Priority 0 buckets after the recent C18/C26/C29/C31/C32 passes. This run therefore continues C30 rather than advancing mechanically by round sequence.

The loop objective is not to rediscover the generic global rule that price-only blowoff must be capped. The more useful residual question is narrower:

```text
When a builder or housing developer first bounces from PF / low-PBR / housing-relief headlines,
which follow-through paths are real balance-sheet repair,
and which are merely post-peak local 4B traps?
```

For C30, a price chart can look like a bridge over the PF pit. But the load-bearing beams are not candles; they are PF guarantee reduction, refinancing success, unsold inventory relief, unbilled receivables stabilization, operating cash-flow conversion, and margin repair. If those beams are missing, the bridge is painted on the floor.

## 2. Stock-Web validation scope

```yaml
manifest_checked: true
manifest_path: atlas/manifest.json
manifest_source_name: FinanceData/marcap
manifest_price_adjustment_status: raw_unadjusted_marcap
manifest_min_date: 1995-05-02
manifest_max_date: 2026-02-20
manifest_tradable_row_count: 14354401
manifest_raw_row_count: 15214118
manifest_symbol_count: 5414
manifest_markets: [KONEX, KOSDAQ, KOSDAQ GLOBAL, KOSPI]
calibration_shard_root: atlas/ohlcv_tradable_by_symbol_year
raw_shard_root: atlas/ohlcv_raw_by_symbol_year
```

Browser-side access to some new raw GitHub shard URLs was unstable in this session. This MD therefore uses stock-web rows already read in prior local C30/C30-adjacent v12 passes for the same shard paths and marks every row with `source_proxy_only=true`, `evidence_url_pending=true`, and `batch_reverification_required=true`. The row schema remains complete so the later batch agent can re-open each shard and recompute the fields.

## 3. Novelty / no-repeat check

```yaml
prior_C30_symbols_seen_in_conversation:
  - 294870 # HDC현대산업개발
  - 006360 # GS건설
  - 047040 # 대우건설
  - 000720 # 현대건설
  - 028050 # 삼성E&A
  - 375500 # DL이앤씨
  - 004960 # 한신공영
  - 013580 # 계룡건설
  - 009410 # 태영건설 narrative-only
this_run_symbols:
  - 294870
  - 047040
  - 375500
  - 013580
  - 004960
hard_duplicate_key_format: canonical_archetype_id + symbol + trigger_type + entry_date
hard_duplicate_key_check: pass
reuse_policy: same_symbol_new_trigger_family_or_new_entry_date_allowed
new_independent_case_count: 5
reused_case_count: 0
same_archetype_new_symbol_count: 0
same_symbol_new_trigger_family_count: 5
same_archetype_new_trigger_family_count: 5
```

## 4. Case table

| case_id | ticker | name | trigger_type | entry_date | entry_price | 30D MFE / MAE | 90D MFE / MAE | 180D MFE / MAE | label | core lesson |
|---|---:|---|---|---:|---:|---:|---:|---:|---|---|
| C30-R10-L104-01 | 294870 | HDC현대산업개발 | Stage2-Actionable | 2024-04-24 | 17,670 | +3.57 / -2.94 | +22.80 / -4.70 | +59.59 / -4.70 | positive | durable rebound allowed only after PF break absence and repair follow-through |
| C30-R10-L104-02 | 047040 | 대우건설 | 4B-Local-Watch | 2024-07-17 | 4,355 | +0.00 / -6.20 | +0.00 / -10.45 | +0.00 / -14.47 | counterexample | broad builder price confirmation after weak evidence was post-peak local 4B |
| C30-R10-L104-03 | 375500 | DL이앤씨 | 4B-Local-Watch | 2024-06-13 | 39,500 | +0.00 / -12.66 | +0.00 / -26.96 | +0.00 / -26.96 | counterexample | low-PBR contractor spike failed once non-price balance-sheet bridge was missing |
| C30-R10-L104-04 | 013580 | 계룡건설 | Stage2-Actionable | 2024-04-29 | 13,700 | +2.19 / -5.40 | +13.07 / -5.40 | +13.07 / -13.21 | mixed_positive | thin-liquidity regional builder bounce is tradable but not Green without FCF refresh |
| C30-R10-L104-05 | 004960 | 한신공영 | Stage2 | 2024-04-29 | 6,550 | +2.29 / -8.70 | +2.29 / -15.88 | +2.29 / -19.85 | counterexample | small builder PF discount remained a drawdown machine after a brief relief bounce |

## 5. Trigger rows JSONL

```jsonl
{"row_type":"trigger","schema_version":"v12_residual_research","research_session":"post_calibrated_sector_archetype_residual_research","mode":"historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12","trigger_id":"C30_R10L104_294870_20240424_Stage2_Actionable","case_id":"C30_R10L104_294870_20240424","symbol":"294870","company_name":"HDC현대산업개발","round":"R10","loop":104,"large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","fine_archetype_id":"CONSTRUCTION_PF_REPAIR_FOLLOW_THROUGH_VS_POST_PEAK_PRICE_ONLY_4B_FALSE_POSITIVE","sector":"construction / real estate / housing / PF balance-sheet repair","primary_archetype":"repair follow-through positive","loop_objective":"coverage_gap_fill | holdout_validation | residual_missed_structural_mining","trigger_type":"Stage2-Actionable","trigger_family":"spring_repair_follow_through_after_PF_discount_reversal","trigger_date":"2024-04-23","entry_date":"2024-04-24","entry_price":17670.0,"entry_price_basis":"close","evidence_available_at_that_date":"source_proxy_only: spring housing/PF relief plus sustained follow-through; no hard-break contamination in 180D window from prior local validation","evidence_source":"source_proxy_only","stage2_evidence_fields":["relative_strength","sector_repair","PF_hard_break_absent"],"stage3_evidence_fields":["balance_sheet_repair_bridge_required","working_capital_bridge_required","margin_FCF_bridge_required"],"stage4b_evidence_fields":["price_confirmation_not_yet_full_4B"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/294/294870/2024.csv","profile_path":"atlas/symbol_profiles/294/294870.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","price_row_fetch_status":"local_prior_stock_web_rows_reused_for_same_shard_path","MFE_30D_pct":3.57,"MAE_30D_pct":-2.94,"MFE_90D_pct":22.80,"MAE_90D_pct":-4.70,"MFE_180D_pct":59.59,"MAE_180D_pct":-4.70,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_30D_date":"2024-05-16","peak_90D_date":"2024-07-17","peak_180D_date":"2024-08-26","peak_price":28200.0,"trough_180D_date":"2024-06-04","four_b_local_peak_proximity":false,"four_b_full_window_peak_proximity":false,"four_b_timing_verdict":"early_stage2_before_durable_summer_repair_move","four_b_evidence_type":"price_plus_source_proxy_only","four_c_protection_label":"not_applicable","trigger_outcome_label":"positive_follow_through","current_profile_verdict":"current_profile_may_be_too_late_if_it_waits_for_full_4B","classification":"positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"no_2024_180D_overlap_in_prior_validation","same_entry_group_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK|294870|Stage2-Actionable|2024-04-24","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":"same_symbol_new_entry_date_and_new_trigger_family_vs_prior_2024_01_26_and_2024_08_entries","independent_evidence_weight":0.75,"do_not_count_as_new_case":false,"source_proxy_only":true,"evidence_url_pending":true}
{"row_type":"trigger","schema_version":"v12_residual_research","research_session":"post_calibrated_sector_archetype_residual_research","mode":"historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12","trigger_id":"C30_R10L104_047040_20240717_4B_Local_Watch","case_id":"C30_R10L104_047040_20240717","symbol":"047040","company_name":"대우건설","round":"R10","loop":104,"large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","fine_archetype_id":"CONSTRUCTION_PF_REPAIR_FOLLOW_THROUGH_VS_POST_PEAK_PRICE_ONLY_4B_FALSE_POSITIVE","sector":"construction / real estate / housing / PF balance-sheet repair","primary_archetype":"post-peak local 4B false positive","loop_objective":"coverage_gap_fill | counterexample_mining | 4B_non_price_requirement_stress_test","trigger_type":"4B-Local-Watch","trigger_family":"broad_builder_post_peak_price_confirmation_without_cash_bridge","trigger_date":"2024-07-17","entry_date":"2024-07-17","entry_price":4355.0,"entry_price_basis":"close","evidence_available_at_that_date":"source_proxy_only: price path near local C30 peak; no fresh PF guarantee reduction, working-capital repair, or margin bridge in evidence packet","evidence_source":"source_proxy_only","stage2_evidence_fields":["relative_strength","sector_rebound"],"stage3_evidence_fields":["PF_bridge_missing","working_capital_bridge_missing","margin_FCF_bridge_missing"],"stage4b_evidence_fields":["price_confirmation_after_local_move"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/047/047040/2024.csv","profile_path":"atlas/symbol_profiles/047/047040.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","price_row_fetch_status":"local_prior_stock_web_rows_reused_for_same_shard_path","MFE_30D_pct":0.00,"MAE_30D_pct":-6.20,"MFE_90D_pct":0.00,"MAE_90D_pct":-10.45,"MFE_180D_pct":0.00,"MAE_180D_pct":-14.47,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_30D_date":"2024-07-17","peak_90D_date":"2024-07-17","peak_180D_date":"2024-07-17","peak_price":4355.0,"trough_180D_date":"2024-10-31","four_b_local_peak_proximity":true,"four_b_full_window_peak_proximity":true,"four_b_timing_verdict":"post_peak_local_4b_false_positive","four_b_evidence_type":"price_plus_source_proxy_only","four_c_protection_label":"not_applicable","trigger_outcome_label":"counterexample_full_4B_block_needed","current_profile_verdict":"current_profile_false_positive_if_promoted_beyond_local_4B","classification":"counterexample","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"no_2024_180D_overlap_in_prior_validation","same_entry_group_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK|047040|4B-Local-Watch|2024-07-17","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":"same_symbol_new_trigger_family_and_new_entry_date_vs_prior_2024_04_entries","independent_evidence_weight":0.75,"do_not_count_as_new_case":false,"source_proxy_only":true,"evidence_url_pending":true}
{"row_type":"trigger","schema_version":"v12_residual_research","research_session":"post_calibrated_sector_archetype_residual_research","mode":"historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12","trigger_id":"C30_R10L104_375500_20240613_4B_Local_Watch","case_id":"C30_R10L104_375500_20240613","symbol":"375500","company_name":"DL이앤씨","round":"R10","loop":104,"large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","fine_archetype_id":"CONSTRUCTION_PF_REPAIR_FOLLOW_THROUGH_VS_POST_PEAK_PRICE_ONLY_4B_FALSE_POSITIVE","sector":"construction / real estate / housing / PF balance-sheet repair","primary_archetype":"low-PBR contractor post-peak reversal","loop_objective":"coverage_gap_fill | counterexample_mining | high_MAE_guardrail","trigger_type":"4B-Local-Watch","trigger_family":"low_PBR_contractor_local_peak_without_PF_cash_bridge","trigger_date":"2024-06-13","entry_date":"2024-06-13","entry_price":39500.0,"entry_price_basis":"close","evidence_available_at_that_date":"source_proxy_only: contractor/low-PBR repair rally at local high; missing PF/working-capital/margin bridge","evidence_source":"source_proxy_only","stage2_evidence_fields":["valuation_rebound","relative_strength"],"stage3_evidence_fields":["PF_bridge_missing","cash_conversion_missing","margin_bridge_missing"],"stage4b_evidence_fields":["local_price_spike"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/375/375500/2024.csv","profile_path":"atlas/symbol_profiles/375/375500.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","price_row_fetch_status":"local_prior_stock_web_rows_reused_for_same_shard_path","MFE_30D_pct":0.00,"MAE_30D_pct":-12.66,"MFE_90D_pct":0.00,"MAE_90D_pct":-26.96,"MFE_180D_pct":0.00,"MAE_180D_pct":-26.96,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_30D_date":"2024-06-13","peak_90D_date":"2024-06-13","peak_180D_date":"2024-06-13","peak_price":39500.0,"trough_180D_date":"2024-08-08","four_b_local_peak_proximity":true,"four_b_full_window_peak_proximity":true,"four_b_timing_verdict":"local_4b_after_repair_peak_failed","four_b_evidence_type":"price_plus_source_proxy_only","four_c_protection_label":"not_applicable","trigger_outcome_label":"counterexample_high_MAE_after_peak","current_profile_verdict":"current_profile_false_positive_if_full_4B","classification":"counterexample","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"no_2024_180D_overlap_in_prior_validation","same_entry_group_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK|375500|4B-Local-Watch|2024-06-13","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":"same_symbol_new_trigger_family_and_new_entry_date_vs_prior_2024_04_29_stage2","independent_evidence_weight":0.75,"do_not_count_as_new_case":false,"source_proxy_only":true,"evidence_url_pending":true}
{"row_type":"trigger","schema_version":"v12_residual_research","research_session":"post_calibrated_sector_archetype_residual_research","mode":"historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12","trigger_id":"C30_R10L104_013580_20240429_Stage2_Actionable","case_id":"C30_R10L104_013580_20240429","symbol":"013580","company_name":"계룡건설","round":"R10","loop":104,"large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","fine_archetype_id":"CONSTRUCTION_PF_REPAIR_FOLLOW_THROUGH_VS_POST_PEAK_PRICE_ONLY_4B_FALSE_POSITIVE","sector":"construction / real estate / housing / PF balance-sheet repair","primary_archetype":"thin liquidity regional builder partial repair","loop_objective":"coverage_gap_fill | holdout_validation | yellow_threshold_stress_test","trigger_type":"Stage2-Actionable","trigger_family":"regional_builder_partial_repair_without_green_confirmation","trigger_date":"2024-04-26","entry_date":"2024-04-29","entry_price":13700.0,"entry_price_basis":"close","evidence_available_at_that_date":"source_proxy_only: regional builder valuation repair and later thin-liquidity spike; no durable cash-flow bridge for Green","evidence_source":"source_proxy_only","stage2_evidence_fields":["relative_strength","sector_repair"],"stage3_evidence_fields":["margin_FCF_bridge_required","working_capital_bridge_required"],"stage4b_evidence_fields":["thin_liquidity_price_extension_later"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/013/013580/2024.csv","profile_path":"atlas/symbol_profiles/013/013580.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","price_row_fetch_status":"local_prior_stock_web_rows_reused_for_same_shard_path","MFE_30D_pct":2.19,"MAE_30D_pct":-5.40,"MFE_90D_pct":13.07,"MAE_90D_pct":-5.40,"MFE_180D_pct":13.07,"MAE_180D_pct":-13.21,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_30D_date":"2024-05-20","peak_90D_date":"2024-07-17","peak_180D_date":"2024-07-17","peak_price":15490.0,"trough_180D_date":"2024-11-14","four_b_local_peak_proximity":false,"four_b_full_window_peak_proximity":false,"four_b_timing_verdict":"later_spike_not_entry_peak","four_b_evidence_type":"price_plus_source_proxy_only","four_c_protection_label":"not_applicable","trigger_outcome_label":"mixed_positive_stage2_only","current_profile_verdict":"current_profile_too_positive_if_green_too_late_if_blocks_stage2","classification":"mixed_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"no_2024_180D_overlap_in_prior_validation","same_entry_group_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK|013580|Stage2-Actionable|2024-04-29","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":"same_symbol_new_entry_date_and_trigger_family_vs_prior_2024_02_01_and_2024_07_17_entries","independent_evidence_weight":0.75,"do_not_count_as_new_case":false,"source_proxy_only":true,"evidence_url_pending":true}
{"row_type":"trigger","schema_version":"v12_residual_research","research_session":"post_calibrated_sector_archetype_residual_research","mode":"historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12","trigger_id":"C30_R10L104_004960_20240429_Stage2","case_id":"C30_R10L104_004960_20240429","symbol":"004960","company_name":"한신공영","round":"R10","loop":104,"large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","fine_archetype_id":"CONSTRUCTION_PF_REPAIR_FOLLOW_THROUGH_VS_POST_PEAK_PRICE_ONLY_4B_FALSE_POSITIVE","sector":"construction / real estate / housing / PF balance-sheet repair","primary_archetype":"small builder PF discount false positive","loop_objective":"coverage_gap_fill | counterexample_mining | high_MAE_guardrail","trigger_type":"Stage2","trigger_family":"small_builder_low_PBR_discount_without_repair_follow_through","trigger_date":"2024-04-26","entry_date":"2024-04-29","entry_price":6550.0,"entry_price_basis":"close","evidence_available_at_that_date":"source_proxy_only: cheap small builder and PF-relief background, but no net-debt/unsold/unbilled-receivables improvement evidence","evidence_source":"source_proxy_only","stage2_evidence_fields":["valuation_rebound","sector_policy_context"],"stage3_evidence_fields":["PF_bridge_missing","working_capital_bridge_missing","margin_FCF_bridge_missing"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":["unresolved_balance_sheet_risk_watch"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/004/004960/2024.csv","profile_path":"atlas/symbol_profiles/004/004960.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","price_row_fetch_status":"local_prior_stock_web_rows_reused_for_same_shard_path","MFE_30D_pct":2.29,"MAE_30D_pct":-8.70,"MFE_90D_pct":2.29,"MAE_90D_pct":-15.88,"MFE_180D_pct":2.29,"MAE_180D_pct":-19.85,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_30D_date":"2024-05-16","peak_90D_date":"2024-05-16","peak_180D_date":"2024-05-16","peak_price":6700.0,"trough_180D_date":"2024-11-14","four_b_local_peak_proximity":false,"four_b_full_window_peak_proximity":false,"four_b_timing_verdict":"not_4b_low_quality_stage2","four_b_evidence_type":"none","four_c_protection_label":"soft_4c_watch_if_balance_sheet_deteriorates","trigger_outcome_label":"counterexample_small_builder_drawdown","current_profile_verdict":"current_profile_false_positive_if_stage2_actionable_bonus_overcredits_low_PBR","classification":"counterexample","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"no_2024_180D_overlap_in_prior_validation","same_entry_group_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK|004960|Stage2|2024-04-29","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":"same_symbol_new_entry_date_and_trigger_family_vs_prior_2024_02_01_entry","independent_evidence_weight":0.75,"do_not_count_as_new_case":false,"source_proxy_only":true,"evidence_url_pending":true}
```

## 6. Score-return alignment

| bucket | current calibrated profile stress | observed residual | C30-specific correction |
|---|---|---|---|
| early repair follow-through with no hard break | may stay too cautious if it waits only for full 4B | 294870 produced durable 90/180D MFE from a non-peak entry | allow Stage2 → Yellow when balance-sheet bridge begins forming |
| local 4B after visible price spike | global 4B may over-credit if non-price evidence is thin | 047040 and 375500 lost convexity after peak entries | keep as local 4B only; do not treat post-peak price as full 4B |
| low-PBR small builder | Stage2 bonus can over-credit cheapness | 004960 produced low MFE and high MAE | require PF/net-debt/working-capital repair before Actionable |
| thin-liquidity regional builder | can look strong on a single spike | 013580 showed local upside but poor durability | Yellow watch only unless cash-flow bridge confirms |

## 7. Aggregate rows

```jsonl
{"row_type":"aggregate_metrics","round":"R10","loop":104,"large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","new_independent_case_count":5,"reused_case_count":0,"same_archetype_new_symbol_count":0,"same_symbol_new_trigger_family_count":5,"same_archetype_new_trigger_family_count":5,"calibration_usable_case_count":5,"calibration_usable_trigger_count":5,"positive_case_count":1,"mixed_positive_count":1,"counterexample_count":3,"local_4b_watch_count":3,"hard_4c_or_blocked_break_count":0,"current_profile_error_count":5,"median_mfe_30d_pct":2.29,"median_mae_30d_pct":-6.20,"median_mfe_90d_pct":2.29,"median_mae_90d_pct":-10.45,"median_mfe_180d_pct":2.29,"median_mae_180d_pct":-14.47,"dominant_residual_error":"C30 overcredits post-peak price-only repair and low-PBR relief without balance-sheet bridge","coverage_gap_after_acceptance_static":"C30 rows 3 -> 8 if accepted","coverage_gap_after_acceptance_conversation_local":"C30 approx rows 19 -> 24 if accepted"}
```

## 8. Shadow rule candidates

```jsonl
{"row_type":"shadow_weight","axis":"C30_EARLY_REPAIR_FOLLOW_THROUGH_ALLOWED_WITH_BALANCE_SHEET_BRIDGE","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","direction":"allow_selective_positive","suggested_delta":0.9,"evidence":"294870 shows early C30 repair can be positive when hard PF break is absent and follow-through appears before the local peak","production_scoring_changed":false}
{"row_type":"shadow_weight","axis":"C30_POST_PEAK_LOCAL_4B_CAP","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","direction":"cap_false_positive","suggested_delta":-1.3,"evidence":"047040 and 375500 show post-peak price confirmation without cash bridge produces high MAE and no forward MFE","production_scoring_changed":false}
{"row_type":"shadow_weight","axis":"C30_SMALL_BUILDER_LOW_PBR_HIGH_MAE_GUARD","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","direction":"strengthen_high_mae_guard","suggested_delta":-1.0,"evidence":"004960 small builder low-PBR discount produced minimal MFE and deep MAE without balance-sheet repair evidence","production_scoring_changed":false}
```

## 9. Residual contribution summary

```yaml
sector_specific_rule_candidate: true
canonical_archetype_rule_candidate: true
loop_contribution_label: canonical_archetype_rule_candidate
do_not_propose_new_weight_delta: false
new_axis_proposed:
  - C30_EARLY_REPAIR_FOLLOW_THROUGH_ALLOWED_WITH_BALANCE_SHEET_BRIDGE
  - C30_POST_PEAK_LOCAL_4B_CAP
  - C30_SMALL_BUILDER_LOW_PBR_HIGH_MAE_GUARD
  - C30_UNSOLD_INVENTORY_UNBILLED_RECEIVABLES_NET_DEBT_CHECK
existing_axis_strengthened:
  - stage2_required_bridge
  - price_only_blowoff_blocks_positive_stage
  - full_4b_requires_non_price_evidence
  - local_4b_watch_guard
  - high_MAE_guardrail
  - hard_4c_thesis_break_routes_to_4c
existing_axis_weakened: null
```

## 10. Deferred Coding Agent Handoff Prompt

```text
Do not execute this handoff during research.

Input MD:
e2r_stock_web_v12_residual_round_R10_loop_104_L9_CONSTRUCTION_REALESTATE_HOUSING_C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK_research.md

Batch verification tasks:
1. Re-open stock-web profiles and tradable shards for all trigger rows.
2. Recompute entry_price, 30D/90D/180D MFE/MAE, peak dates, and post-peak drawdown from tradable_raw rows.
3. Reject rows where corporate_action_candidate_dates overlap entry_date~D+180.
4. If verified, test C30-specific shadow rules:
   - allow early repair follow-through only when balance-sheet bridge is visible;
   - cap post-peak local 4B construction spikes without non-price evidence;
   - strengthen high-MAE guard for small builders and low-PBR PF-discount names;
   - require unsold inventory / unbilled receivables / net debt checks before Stage3.
5. Do not patch production scoring without batch reviewer approval.
```

## 11. Research state

```text
completed_round = R10
completed_loop = 104
selection_basis = docs/core/V12_Research_No_Repeat_Index.md + conversation-local generated MD ledger
selected_priority_bucket = Priority 0
round_schedule_status = coverage_index_selected
round_sector_consistency = pass

auto_selected_coverage_gap_static_index = C30 rows 3 -> 8 if accepted; still Priority 0, need 22 to reach 30
auto_selected_coverage_gap_conversation_local = C30 approx rows 19 -> 24 if accepted; still Priority 0, need about 6 to reach 30

next_recommended_archetypes = C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK_fifth_pass_to_30, C31_POLICY_SUBSIDY_LEGISLATION_EVENT_fourth_pass_to_30, C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP_fourth_pass_to_30, C18_CONSUMER_EXPORT_CHANNEL_REORDER_third_pass_to_30, C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE_fourth_pass_to_30, R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL
```
