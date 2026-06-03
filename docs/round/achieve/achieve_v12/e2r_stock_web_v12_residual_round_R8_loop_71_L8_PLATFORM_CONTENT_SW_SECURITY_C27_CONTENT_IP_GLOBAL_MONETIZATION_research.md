# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
round=R8
loop=71
scheduled_round=R8
scheduled_loop=71
round_schedule_status=valid
round_sector_consistency=pass
computed_next_round=R9
computed_next_loop=71
large_sector_id=L8_PLATFORM_CONTENT_SW_SECURITY
canonical_archetype_id=C27_CONTENT_IP_GLOBAL_MONETIZATION
fine_archetype_id=GAME_IP_GLOBAL_LIVE_SERVICE_MONETIZATION_VS_LAUNCH_RETENTION_GUARD
price_source=Songdaiki/stock-web
price_basis=tradable_raw
price_adjustment_status=raw_unadjusted_marcap
stock_web_manifest_max_date=2026-02-20
loop_objective=coverage_gap_fill | counterexample_mining | 4B_non_price_requirement_stress_test | sector_specific_rule_discovery | canonical_archetype_compression
```

This loop adds 3 new independent cases, 2 counterexamples, and 3 residual errors for R8/L8_PLATFORM_CONTENT_SW_SECURITY/C27_CONTENT_IP_GLOBAL_MONETIZATION.

## 1. Current Calibrated Profile Assumption

current_default_profile_proxy = `e2r_2_1_stock_web_calibrated_proxy`  
rollback_reference_profile_id = `e2r_2_0_baseline_reference`

Tested axes: `stage2_actionable_evidence_bonus`, `price_only_blowoff_blocks_positive_stage`, `full_4b_requires_non_price_evidence`.

## 2. Round / Large Sector / Canonical Archetype Scope

- scheduled_round: `R8`
- scheduled_loop: `71`
- large_sector_id: `L8_PLATFORM_CONTENT_SW_SECURITY`
- canonical_archetype_id: `C27_CONTENT_IP_GLOBAL_MONETIZATION`
- fine_archetype_id: `GAME_IP_GLOBAL_LIVE_SERVICE_MONETIZATION_VS_LAUNCH_RETENTION_GUARD`
- round_sector_consistency: `pass`
- next_round: `R9`
- next_loop: `71`

## 3. Previous Coverage / Duplicate Avoidance Check

`V12_Research_No_Repeat_Index.md` was used only as the duplicate-avoidance ledger. C27 already had 51 rows / 19 symbols, but its top-covered symbols were music/content names such as 035900, 253450, 352820, 122870, and 036420. This loop deliberately selected three game-IP symbols not present in the top-covered list: `259960`, `225570`, and `095660`.

Hard duplicate key avoided: `canonical_archetype_id + symbol + trigger_type + entry_date`.

## 4. Stock-Web OHLC Input / Price Source Validation

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
```

Stock-Web context: manifest max date `2026-02-20`, price basis `tradable_raw`, adjustment `raw_unadjusted_marcap`, shard root `atlas/ohlcv_tradable_by_symbol_year`.

## 5. Historical Eligibility Gate

All three representative cases have entry rows in stock-web tradable shards, at least 180 forward trading days, computed 30D/90D/180D MFE/MAE, and no 180D overlapping corporate-action candidate dates. 225570 has old corporate-action candidates around the 2022 merger/name transition, but they do not overlap the 2024 First Descendant window.

## 6. Canonical Archetype Compression Map

```text
C27 game-IP monetization quality gate =
    global IP reach
  + recurring/live-service monetization
  + retention or repeat-payer evidence
  + operating leverage after launch
  - one-time premium launch already priced in
  - launch-spike without retention
  - tokenized/theme beta without cash conversion
```

## 7. Case Selection Summary

| case_id | symbol | company_name | case_type | positive_or_counterexample | calibration_usable | is_new_independent_case | current_profile_verdict |
| --- | --- | --- | --- | --- | --- | --- | --- |
| R8L71_C27_259960_PUBG_BGMI_LIVE_SERVICE_MONETIZATION | 259960 | 크래프톤 | structural_success | positive | True | True | current_profile_missed_structural |
| R8L71_C27_225570_FIRST_DESCENDANT_LAUNCH_RETENTION_4B | 225570 | 넥슨게임즈 | 4B_overlay_success | counterexample | True | True | current_profile_4B_too_late |
| R8L71_C27_095660_LIES_OF_P_PRICED_IN_LAUNCH_GUARD | 095660 | 네오위즈 | failed_rerating | counterexample | True | True | current_profile_false_positive |

## 8. Positive vs Counterexample Balance

- positive_case_count: 1
- counterexample_count: 2
- 4B_case_count: 2
- 4C_case_count: 0
- calibration_usable_case_count: 3

The loop satisfies the minimum balance rule: at least one positive, one counterexample, and three usable calibration cases.

## 9. Evidence Source Map

| case_id | symbol | trigger_type | trigger_date | entry_date | evidence_source |
| --- | --- | --- | --- | --- | --- |
| R8L71_C27_259960_PUBG_BGMI_LIVE_SERVICE_MONETIZATION | 259960 | Stage2-Actionable | 2024-02-08 | 2024-02-13 | Krafton IR earnings-release page / public earnings headlines; source_proxy_only=false for price calibration, evidence URL can be replaced by exact IR PDF in implementation pass. |
| R8L71_C27_225570_FIRST_DESCENDANT_LAUNCH_RETENTION_4B | 225570 | Stage2-Actionable | 2024-07-02 | 2024-07-03 | Nexon/Steam public launch pages and public launch headlines; exact IR/news URL can be hardened in implementation pass. |
| R8L71_C27_225570_FIRST_DESCENDANT_LAUNCH_RETENTION_4B | 225570 | Stage4B | 2024-08-01 | 2024-08-01 | Stock-web price path + public launch/Steam visibility; 4B overlay only, not positive promotion evidence. |
| R8L71_C27_095660_LIES_OF_P_PRICED_IN_LAUNCH_GUARD | 095660 | Stage2-Actionable | 2023-09-19 | 2023-09-19 | Game launch/public marketplace pages and release headlines; source_proxy_only=false for price-path residual, exact URL can be hardened later. |

## 10. Price Data Source Map

| case_id | symbol | price_shard_path | profile_path | entry_date | entry_price | corporate_action_window_status |
| --- | --- | --- | --- | --- | ---: | --- |
| R8L71_C27_259960_PUBG_BGMI_LIVE_SERVICE_MONETIZATION | 259960 | atlas/ohlcv_tradable_by_symbol_year/259/259960/2024.csv | atlas/symbol_profiles/259/259960.json | 2024-02-13 | 230000 | clean_180D |
| R8L71_C27_225570_FIRST_DESCENDANT_LAUNCH_RETENTION_4B | 225570 | atlas/ohlcv_tradable_by_symbol_year/225/225570/2024.csv | atlas/symbol_profiles/225/225570.json | 2024-07-03 | 17900 | clean_180D; old corporate-action candidates do not overlap 2024 window |
| R8L71_C27_095660_LIES_OF_P_PRICED_IN_LAUNCH_GUARD | 095660 | atlas/ohlcv_tradable_by_symbol_year/095/095660/2023.csv | atlas/symbol_profiles/095/095660.json | 2023-09-19 | 34500 | clean_180D; old corporate-action candidates do not overlap 2023 window |

## 11. Case-by-Case Trigger Grid

| trigger_id | symbol | trigger_type | entry_date | entry_price | MFE_30D_pct | MAE_30D_pct | MFE_90D_pct | MAE_90D_pct | MFE_180D_pct | MAE_180D_pct | current_profile_verdict |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| TRG_R8L71_C27_259960_STAGE2_LIVE_SERVICE_MONETIZATION | 259960 | Stage2-Actionable | 2024-02-13 | 230000 | 15.22 | -8.48 | 30.0 | -8.48 | 54.35 | -8.48 | current_profile_missed_structural |
| TRG_R8L71_C27_225570_STAGE2_LAUNCH_SPIKE | 225570 | Stage2-Actionable | 2024-07-03 | 17900 | 68.72 | -7.88 | 72.91 | -23.85 | 72.91 | -33.52 | current_profile_4B_too_late |
| TRG_R8L71_C27_225570_STAGE4B_FULL_WINDOW_OVERLAY | 225570 | Stage4B | 2024-08-01 | 28800 | 7.47 | -47.08 | 7.47 | -52.71 | 7.47 | -60.24 | current_profile_4B_too_late |
| TRG_R8L71_C27_095660_STAGE2_LAUNCH_PRICED_IN | 095660 | Stage2-Actionable | 2023-09-19 | 34500 | 3.04 | -32.32 | 3.04 | -32.32 | 3.04 | -41.01 | current_profile_false_positive |

## 12. Trigger-Level OHLC Backtest Tables

### 259960 / Krafton
- entry row: `2024-02-13, close 230000`; stock-web high path reached `2024-08-22 high 355000`.
- Interpretation: live-service monetization created durable rerating; waiting only for a one-time launch-style trigger would miss the structural route.

### 225570 / Nexon Games
- representative entry row: `2024-07-03, close 17900`; full-window peak `2024-08-09 high 30950`; later drawdown reached the 12k area by early 2025.
- 4B overlay row: `2024-08-01, close 28800`, with full-window proximity near 0.84.
- Interpretation: launch spike was real, but without retention/monetization confirmation it should be 4B watch, not Green.

### 095660 / Neowiz
- launch entry row: `2023-09-19, close 34500`; immediate post-launch path fell to `2023-10-05 low 23350`, and 2024 rows show continued low-20k drift.
- Interpretation: premium launch visibility was priced in before release; recurring monetization was not proven.

## 13. Current Calibrated Profile Stress Test

- 259960: current profile can be too slow if it demands a discrete launch headline rather than recognizing recurring live-service monetization.
- 225570: current profile can be too late on 4B if it lets launch momentum continue without retention proof.
- 095660: current profile can be false positive if a premium launch headline receives Stage2 bonus after the pre-launch move has already priced it.

## 14. Stage2 / Yellow / Green Comparison

- Stage2-Actionable is valid for 259960 when repeat monetization and financial visibility are attached.
- Stage2/Yellow should be capped for 225570 until retention and payer conversion evidence appears.
- Stage3-Green should not be allowed for 095660 on launch visibility alone.

## 15. 4B Local vs Full-window Timing Audit

- 225570: 4B overlay at 2024-08-01 had proximity 0.84 to the full-window peak, making it a useful full-window 4B if non-price retention/overheat evidence is attached.
- 095660: launch-day price was already near the post-launch maximum; pre-launch blowoff should have been a 4B watch.
- 259960: 4B is only a later valuation watch; it should not suppress early Stage2/Yellow evidence.

## 16. 4C Protection Audit

No hard 4C route is proposed. The residual is mostly Stage2/4B differentiation: launch spike without retention should be capped before thesis-break language is used.

## 17. Sector-Specific Rule Candidate

`sector_specific_rule_candidate = true`

For L8, content-IP evidence should distinguish subscription/live-service recurrence from a one-time launch headline. The market can pay for global reach first, but E2R should require retention/repeat-payer evidence before Green.

## 18. Canonical-Archetype Rule Candidate

`canonical_archetype_rule_candidate = true`

```text
if content_ip_global_launch and recurring_monetization_bridge is missing:
    cap at Stage2-Watch or Yellow
    attach 4B watch if price spike already captured large upside

if live_service_revenue_visibility and repeat_payer/retention evidence exist:
    allow Stage2-Actionable / Yellow even without a new launch headline

if premium_game_launch is already priced in before release:
    do not upgrade to Green on launch date alone
```

## 19. Before / After Backtest Comparison

| profile | avg_MFE_90D_pct | avg_MAE_90D_pct | false_positive_rate | missed_structural_count | verdict |
| --- | ---: | ---: | ---: | ---: | --- |
| P0 current calibrated proxy | 35.32 | -21.55 | 0.67 | 1 | mixed |
| P2 C27 live-service candidate | 35.32 | -21.55 | 0.33 | 0 | better alignment |

## 20. Score-Return Alignment Matrix

| case_id | score-return alignment | component explanation |
| --- | --- | --- |
| R8L71_C27_259960_PUBG_BGMI_LIVE_SERVICE_MONETIZATION | aligned after adding recurring-monetization bridge | repeat revenue + financial visibility explain durable MFE |
| R8L71_C27_225570_FIRST_DESCENDANT_LAUNCH_RETENTION_4B | high MFE but failed durable rerating | launch distribution worked; retention proof missing |
| R8L71_C27_095660_LIES_OF_P_PRICED_IN_LAUNCH_GUARD | false positive if launch alone promoted | premium-game launch lacked recurring monetization |

## 21. Coverage Matrix

```jsonl
{"row_type":"coverage_matrix","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C27_CONTENT_IP_GLOBAL_MONETIZATION","fine_archetype_id":"GAME_IP_GLOBAL_LIVE_SERVICE_MONETIZATION_VS_LAUNCH_RETENTION_GUARD","positive_case_count":1,"counterexample_count":2,"4B_case_count":2,"4C_case_count":0,"new_independent_case_count":3,"reused_case_count":0,"calibration_usable_trigger_count":4,"representative_trigger_count":3,"current_profile_error_count":3,"sector_rule_candidate":true,"canonical_rule_candidate":true,"coverage_gap_after_this_loop":"C27 now has additional game-IP live-service vs launch-retention differentiation using 095660/225570/259960."}
```

## 22. Residual Contribution Summary

```text
new_independent_case_count: 3
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 3
new_canonical_archetype_count: 0
new_fine_archetype_count: 1
new_trigger_family_count: 3
tested_existing_calibrated_axes: stage2_actionable_evidence_bonus, price_only_blowoff_blocks_positive_stage, full_4b_requires_non_price_evidence
residual_error_types_found: current_profile_missed_structural, current_profile_4B_too_late, current_profile_false_positive
new_axis_proposed: null
existing_axis_strengthened: full_4b_requires_non_price_evidence; price_only_blowoff_blocks_positive_stage
existing_axis_weakened: null
existing_axis_kept: stage2_actionable_evidence_bonus
sector_specific_rule_candidate: true
canonical_archetype_rule_candidate: true
no_new_signal_reason: null
loop_contribution_label: canonical_archetype_rule_candidate
do_not_propose_new_weight_delta: false
```

## 23. Validation Scope / Non-Validation Scope

Validation scope: stock-web OHLC rows, entry/price path, MFE/MAE, forward-window availability, round-sector consistency, duplicate-avoidance fields.

Non-validation scope: this file does not patch production scoring, does not run live discovery, and does not claim current recommendations. Exact evidence URLs can be hardened in a later implementation pass; price calibration uses only stock-web OHLC.

## 24. Shadow Weight Calibration

```jsonl
{"row_type":"shadow_weight","round":"R8","loop":"71","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C27_CONTENT_IP_GLOBAL_MONETIZATION","fine_archetype_id":"GAME_IP_GLOBAL_LIVE_SERVICE_MONETIZATION_VS_LAUNCH_RETENTION_GUARD","rule_scope":"canonical_archetype_specific","axis":"content_ip_recurring_monetization_bridge_required","direction":"strengthen","proposed_delta":"+guard not +score","positive_support_case_ids":["R8L71_C27_259960_PUBG_BGMI_LIVE_SERVICE_MONETIZATION"],"counterexample_case_ids":["R8L71_C27_225570_FIRST_DESCENDANT_LAUNCH_RETENTION_4B","R8L71_C27_095660_LIES_OF_P_PRICED_IN_LAUNCH_GUARD"],"risk_level":"medium","application_mode":"shadow_only","notes":"Do not promote one-time launch headlines to Green without recurring monetization/retention evidence."}
```

## 25. Machine-Readable Rows

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
{"row_type":"case","case_id":"R8L71_C27_259960_PUBG_BGMI_LIVE_SERVICE_MONETIZATION","symbol":"259960","company_name":"크래프톤","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"TRG_R8L71_C27_259960_STAGE2_LIVE_SERVICE_MONETIZATION","calibration_usable":true,"is_new_independent_case":true,"current_profile_verdict":"current_profile_missed_structural","notes":"PUBG/BGMI live-service revenue durability created a slower but durable rerating; Stage2/Yellow should not require a single launch headline when recurring monetization is visible.","round":"R8","loop":"71","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C27_CONTENT_IP_GLOBAL_MONETIZATION","fine_archetype_id":"GAME_IP_GLOBAL_LIVE_SERVICE_MONETIZATION_VS_LAUNCH_RETENTION_GUARD","price_source":"Songdaiki/stock-web","independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"case","case_id":"R8L71_C27_225570_FIRST_DESCENDANT_LAUNCH_RETENTION_4B","symbol":"225570","company_name":"넥슨게임즈","case_type":"4B_overlay_success","positive_or_counterexample":"counterexample","best_trigger":"TRG_R8L71_C27_225570_STAGE2_LAUNCH_SPIKE","calibration_usable":true,"is_new_independent_case":true,"current_profile_verdict":"current_profile_4B_too_late","notes":"The First Descendant launch created a strong price move, but the lack of durable retention/monetization evidence required a 4B overlay rather than Green promotion.","round":"R8","loop":"71","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C27_CONTENT_IP_GLOBAL_MONETIZATION","fine_archetype_id":"GAME_IP_GLOBAL_LIVE_SERVICE_MONETIZATION_VS_LAUNCH_RETENTION_GUARD","price_source":"Songdaiki/stock-web","independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"case","case_id":"R8L71_C27_095660_LIES_OF_P_PRICED_IN_LAUNCH_GUARD","symbol":"095660","company_name":"네오위즈","case_type":"failed_rerating","positive_or_counterexample":"counterexample","best_trigger":"TRG_R8L71_C27_095660_STAGE2_LAUNCH_PRICED_IN","calibration_usable":true,"is_new_independent_case":true,"current_profile_verdict":"current_profile_false_positive","notes":"A successful premium-game launch headline without recurring monetization/retention evidence was already priced in; the price path failed after launch.","round":"R8","loop":"71","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C27_CONTENT_IP_GLOBAL_MONETIZATION","fine_archetype_id":"GAME_IP_GLOBAL_LIVE_SERVICE_MONETIZATION_VS_LAUNCH_RETENTION_GUARD","price_source":"Songdaiki/stock-web","independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"TRG_R8L71_C27_259960_STAGE2_LIVE_SERVICE_MONETIZATION","case_id":"R8L71_C27_259960_PUBG_BGMI_LIVE_SERVICE_MONETIZATION","symbol":"259960","company_name":"크래프톤","round":"R8","loop":"71","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C27_CONTENT_IP_GLOBAL_MONETIZATION","fine_archetype_id":"GAME_IP_GLOBAL_LIVE_SERVICE_MONETIZATION_VS_LAUNCH_RETENTION_GUARD","sector":"platform_content_sw_security","primary_archetype":"game_ip_live_service_monetization","loop_objective":"coverage_gap_fill | counterexample_mining | 4B_non_price_requirement_stress_test | sector_specific_rule_discovery | canonical_archetype_compression","trigger_type":"Stage2-Actionable","trigger_date":"2024-02-08","evidence_available_at_that_date":"PUBG/BGMI live-service monetization and earnings-visibility evidence was public before the 2024 rerating leg; entry is next tradable post-earnings close used as conservative trigger proxy.","evidence_source":"Krafton IR earnings-release page / public earnings headlines; source_proxy_only=false for price calibration, evidence URL can be replaced by exact IR PDF in implementation pass.","stage2_evidence_fields":["public_event_or_disclosure","repeat_order_or_conversion","early_revision_signal","relative_strength"],"stage3_evidence_fields":["confirmed_revision","financial_visibility","repeat_order_or_conversion","low_red_team_risk"],"stage4b_evidence_fields":["valuation_blowoff_watch_after_fast_rerating"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/259/259960/2024.csv","profile_path":"atlas/symbol_profiles/259/259960.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-02-13","entry_price":230000,"MFE_30D_pct":15.22,"MFE_90D_pct":30.0,"MFE_180D_pct":54.35,"MFE_1Y_pct":54.35,"MFE_2Y_pct":null,"MAE_30D_pct":-8.48,"MAE_90D_pct":-8.48,"MAE_180D_pct":-8.48,"MAE_1Y_pct":-8.48,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-08-22","peak_price":355000,"drawdown_after_peak_pct":-11.69,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"4B_watch_after_rerating_not_representative","four_b_evidence_type":["valuation_blowoff_watch"],"four_c_protection_label":"not_applicable","trigger_outcome_label":"structural_success","current_profile_verdict":"current_profile_missed_structural","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D","same_entry_group_id":"R8L71_C27_259960_2024-02-13","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"TRG_R8L71_C27_225570_STAGE2_LAUNCH_SPIKE","case_id":"R8L71_C27_225570_FIRST_DESCENDANT_LAUNCH_RETENTION_4B","symbol":"225570","company_name":"넥슨게임즈","round":"R8","loop":"71","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C27_CONTENT_IP_GLOBAL_MONETIZATION","fine_archetype_id":"GAME_IP_GLOBAL_LIVE_SERVICE_MONETIZATION_VS_LAUNCH_RETENTION_GUARD","sector":"platform_content_sw_security","primary_archetype":"game_ip_global_launch_retention_guard","loop_objective":"coverage_gap_fill | counterexample_mining | 4B_non_price_requirement_stress_test | sector_specific_rule_discovery | canonical_archetype_compression","trigger_type":"Stage2-Actionable","trigger_date":"2024-07-02","evidence_available_at_that_date":"The First Descendant global launch / Steam and console distribution visibility created a launch-spike thesis.","evidence_source":"Nexon/Steam public launch pages and public launch headlines; exact IR/news URL can be hardened in implementation pass.","stage2_evidence_fields":["public_event_or_disclosure","relative_strength","global_launch_distribution"],"stage3_evidence_fields":["unknown_or_not_supported: durable retention and monetization not yet proven"],"stage4b_evidence_fields":["positioning_overheat","price_only_local_peak","retention_or_monetization_gap"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/225/225570/2024.csv","profile_path":"atlas/symbol_profiles/225/225570.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-07-03","entry_price":17900,"MFE_30D_pct":68.72,"MFE_90D_pct":72.91,"MFE_180D_pct":72.91,"MFE_1Y_pct":72.91,"MFE_2Y_pct":null,"MAE_30D_pct":-7.88,"MAE_90D_pct":-23.85,"MAE_180D_pct":-33.52,"MAE_1Y_pct":-35.98,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-08-09","peak_price":30950,"drawdown_after_peak_pct":-61.55,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"Stage2_launch_spike_required_4B_overlay","four_b_evidence_type":["price_only","positioning_overheat","retention_or_monetization_gap"],"four_c_protection_label":"watch_only_not_hard_4c","trigger_outcome_label":"high_mfe_but_failed_retention_rerating","current_profile_verdict":"current_profile_4B_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D; old corporate-action candidates do not overlap 2024 window","same_entry_group_id":"R8L71_C27_225570_2024-07-03","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"TRG_R8L71_C27_225570_STAGE4B_FULL_WINDOW_OVERLAY","case_id":"R8L71_C27_225570_FIRST_DESCENDANT_LAUNCH_RETENTION_4B","symbol":"225570","company_name":"넥슨게임즈","round":"R8","loop":"71","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C27_CONTENT_IP_GLOBAL_MONETIZATION","fine_archetype_id":"GAME_IP_GLOBAL_LIVE_SERVICE_MONETIZATION_VS_LAUNCH_RETENTION_GUARD","sector":"platform_content_sw_security","primary_archetype":"game_ip_global_launch_retention_guard","loop_objective":"4B_non_price_requirement_stress_test","trigger_type":"Stage4B","trigger_date":"2024-08-01","evidence_available_at_that_date":"Launch-spike valuation/positioning was visible; durable retention evidence was not yet confirmed.","evidence_source":"Stock-web price path + public launch/Steam visibility; 4B overlay only, not positive promotion evidence.","stage2_evidence_fields":[],"stage3_evidence_fields":[],"stage4b_evidence_fields":["valuation_blowoff","positioning_overheat","price_only_local_peak","retention_or_monetization_gap"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/225/225570/2024.csv","profile_path":"atlas/symbol_profiles/225/225570.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-08-01","entry_price":28800,"MFE_30D_pct":7.47,"MFE_90D_pct":7.47,"MFE_180D_pct":7.47,"MFE_1Y_pct":7.47,"MFE_2Y_pct":null,"MAE_30D_pct":-47.08,"MAE_90D_pct":-52.71,"MAE_180D_pct":-60.24,"MAE_1Y_pct":-60.24,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-08-09","peak_price":30950,"drawdown_after_peak_pct":-61.55,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":0.84,"four_b_full_window_peak_proximity":0.84,"four_b_timing_verdict":"good_full_window_4B_timing_if_non_price_retention_gap_is_attached","four_b_evidence_type":["valuation_blowoff","positioning_overheat","retention_or_monetization_gap"],"four_c_protection_label":"watch_only_not_hard_4c","trigger_outcome_label":"4B_overlay_success","current_profile_verdict":"current_profile_4B_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D","same_entry_group_id":"R8L71_C27_225570_2024-08-01_4B","dedupe_for_aggregate":false,"aggregate_group_role":"4B_overlay_only","is_new_independent_case":true,"reuse_reason":"same_symbol_different_trigger_family_4B_timing","independent_evidence_weight":0.5,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"TRG_R8L71_C27_095660_STAGE2_LAUNCH_PRICED_IN","case_id":"R8L71_C27_095660_LIES_OF_P_PRICED_IN_LAUNCH_GUARD","symbol":"095660","company_name":"네오위즈","round":"R8","loop":"71","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C27_CONTENT_IP_GLOBAL_MONETIZATION","fine_archetype_id":"GAME_IP_GLOBAL_LIVE_SERVICE_MONETIZATION_VS_LAUNCH_RETENTION_GUARD","sector":"platform_content_sw_security","primary_archetype":"premium_game_launch_without_recurring_monetization","loop_objective":"coverage_gap_fill | counterexample_mining | 4B_non_price_requirement_stress_test | sector_specific_rule_discovery | canonical_archetype_compression","trigger_type":"Stage2-Actionable","trigger_date":"2023-09-19","evidence_available_at_that_date":"Lies of P global launch/review visibility was public, but the premium-game launch did not prove recurring monetization or long-term live-service retention.","evidence_source":"Game launch/public marketplace pages and release headlines; source_proxy_only=false for price-path residual, exact URL can be hardened later.","stage2_evidence_fields":["public_event_or_disclosure","global_launch_distribution","relative_strength_before_event"],"stage3_evidence_fields":["unknown_or_not_supported: recurring monetization not established"],"stage4b_evidence_fields":["priced_in_launch","valuation_blowoff","positioning_overheat"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/095/095660/2023.csv","profile_path":"atlas/symbol_profiles/095/095660.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2023-09-19","entry_price":34500,"MFE_30D_pct":3.04,"MFE_90D_pct":3.04,"MFE_180D_pct":3.04,"MFE_1Y_pct":3.04,"MFE_2Y_pct":3.04,"MAE_30D_pct":-32.32,"MAE_90D_pct":-32.32,"MAE_180D_pct":-41.01,"MAE_1Y_pct":-42.9,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2023-09-19","peak_price":35550,"drawdown_after_peak_pct":-42.9,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"launch_priced_in_4B_watch_was_needed_before_positive_promotion","four_b_evidence_type":["valuation_blowoff","positioning_overheat","premium_launch_no_recurring_revenue"],"four_c_protection_label":"not_hard_4c_but_failed_rerating","trigger_outcome_label":"failed_rerating","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D; old corporate-action candidates do not overlap 2023 window","same_entry_group_id":"R8L71_C27_095660_2023-09-19","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"score_simulation","profile_id":"P0_e2r_2_1_stock_web_calibrated_proxy","profile_scope":"current_proxy","profile_hypothesis":"Launch/global IP headlines receive Stage2 bonus if there is non-price evidence.","changed_axes":[],"eligible_trigger_count":3,"selected_entry_trigger_per_case":["R8L71_C27_259960_PUBG_BGMI_LIVE_SERVICE_MONETIZATION","R8L71_C27_225570_FIRST_DESCENDANT_LAUNCH_RETENTION_4B","R8L71_C27_095660_LIES_OF_P_PRICED_IN_LAUNCH_GUARD"],"avg_MFE_90D_pct":35.32,"avg_MAE_90D_pct":-21.55,"avg_MFE_180D_pct":43.43,"avg_MAE_180D_pct":-27.67,"false_positive_rate":0.67,"missed_structural_count":1,"late_green_count":0,"avg_green_lateness_ratio":"not_applicable","avg_four_b_local_peak_proximity":0.92,"avg_four_b_full_window_peak_proximity":0.92,"score_return_alignment_verdict":"mixed; too generous to premium/launch spikes, too slow on live-service recurring monetization"}
{"row_type":"score_simulation","profile_id":"P2_C27_game_ip_live_service_candidate","profile_scope":"canonical_archetype_specific","profile_hypothesis":"Reward recurring live-service monetization and repeat revenue; cap one-time premium-game launch or launch-spike without retention at Stage2-Watch/Yellow and attach 4B.","changed_axes":["content_ip_recurring_monetization_bridge_required","launch_spike_retention_guard"],"eligible_trigger_count":3,"selected_entry_trigger_per_case":["R8L71_C27_259960_PUBG_BGMI_LIVE_SERVICE_MONETIZATION","R8L71_C27_225570_FIRST_DESCENDANT_LAUNCH_RETENTION_4B","R8L71_C27_095660_LIES_OF_P_PRICED_IN_LAUNCH_GUARD"],"avg_MFE_90D_pct":35.32,"avg_MAE_90D_pct":-21.55,"avg_MFE_180D_pct":43.43,"avg_MAE_180D_pct":-27.67,"false_positive_rate":0.33,"missed_structural_count":0,"late_green_count":0,"avg_green_lateness_ratio":"not_applicable","avg_four_b_local_peak_proximity":0.92,"avg_four_b_full_window_peak_proximity":0.92,"score_return_alignment_verdict":"better; separates 259960 durable live-service route from 225570/095660 launch spike traps"}
{"row_type":"shadow_weight","round":"R8","loop":"71","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C27_CONTENT_IP_GLOBAL_MONETIZATION","fine_archetype_id":"GAME_IP_GLOBAL_LIVE_SERVICE_MONETIZATION_VS_LAUNCH_RETENTION_GUARD","rule_scope":"canonical_archetype_specific","axis":"content_ip_recurring_monetization_bridge_required","direction":"strengthen","proposed_delta":"+guard not +score","positive_support_case_ids":["R8L71_C27_259960_PUBG_BGMI_LIVE_SERVICE_MONETIZATION"],"counterexample_case_ids":["R8L71_C27_225570_FIRST_DESCENDANT_LAUNCH_RETENTION_4B","R8L71_C27_095660_LIES_OF_P_PRICED_IN_LAUNCH_GUARD"],"risk_level":"medium","application_mode":"shadow_only","notes":"Do not promote one-time launch headlines to Green without recurring monetization/retention evidence."}
{"row_type":"coverage_matrix","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C27_CONTENT_IP_GLOBAL_MONETIZATION","fine_archetype_id":"GAME_IP_GLOBAL_LIVE_SERVICE_MONETIZATION_VS_LAUNCH_RETENTION_GUARD","positive_case_count":1,"counterexample_count":2,"4B_case_count":2,"4C_case_count":0,"new_independent_case_count":3,"reused_case_count":0,"calibration_usable_trigger_count":4,"representative_trigger_count":3,"current_profile_error_count":3,"sector_rule_candidate":true,"canonical_rule_candidate":true,"coverage_gap_after_this_loop":"C27 now has additional game-IP live-service vs launch-retention differentiation using 095660/225570/259960."}
{"row_type":"residual_contribution","round":"R8","loop":"71","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C27_CONTENT_IP_GLOBAL_MONETIZATION","new_independent_case_count":3,"reused_case_count":0,"new_symbol_count":3,"same_archetype_new_symbol_count":3,"same_archetype_new_trigger_family_count":3,"new_trigger_family_count":3,"tested_existing_calibrated_axes":["stage2_actionable_evidence_bonus","price_only_blowoff_blocks_positive_stage","full_4b_requires_non_price_evidence"],"residual_error_types_found":["current_profile_missed_structural","current_profile_4B_too_late","current_profile_false_positive"],"loop_contribution_label":"canonical_archetype_rule_candidate","do_not_propose_new_weight_delta":false}
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
completed_round=R8
completed_loop=71
computed_next_round=R9
computed_next_loop=71
next_large_sector_id=L3_BATTERY_EV_GREEN_MOBILITY or L9_CONSTRUCTION_REALESTATE_HOUSING depending on mobility/transport nature
```

## 28. Source Notes

- Main execution prompt: `docs/core/e2r_v12_prompt_round_scheduler_corrected.txt`.
- Duplicate-avoidance ledger: `docs/core/V12_Research_No_Repeat_Index.md`.
- Price atlas: `Songdaiki/stock-web`, manifest max date `2026-02-20`.
- Stock-web rows checked: `259/259960/2024.csv`, `225/225570/2024.csv`, `225/225570/2025.csv`, `095/095660/2023.csv`, `095/095660/2024.csv`.

