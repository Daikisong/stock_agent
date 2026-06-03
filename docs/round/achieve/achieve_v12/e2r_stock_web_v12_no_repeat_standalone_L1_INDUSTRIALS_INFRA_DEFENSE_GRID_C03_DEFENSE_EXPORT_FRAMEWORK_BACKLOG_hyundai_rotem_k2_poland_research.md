# E2R V12 No-Repeat Standalone Residual Research

```text
research_session = post_calibrated_sector_archetype_residual_research
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
output_format = one_standalone_markdown_file
production_scoring_changed = false
shadow_weight_only = true
handoff_prompt_embedded = true
handoff_prompt_executed_now = false
```

## 1. Metadata

```text
selected_round = R1
large_sector_id = L1_INDUSTRIALS_INFRA_DEFENSE_GRID
canonical_archetype_id = C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG
fine_archetype_id = DEFENSE_EXPORT_POLAND_K2_FRAMEWORK_EXECUTIVE_4B_PATH
loop_objective = coverage_gap_fill|green_strictness_stress_test|4B_non_price_requirement_stress_test|counterexample_mining
output_filename = e2r_stock_web_v12_no_repeat_standalone_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG_hyundai_rotem_k2_poland_research.md
```

This file is not a live stock scan, not a recommendation, and not a `stock_agent` code patch.  It is a historical trigger-level residual research artifact for later batch ingestion.

## 2. Source Basis

| item | value |
|---|---|
| main execution prompt | `docs/core/e2r_v12_prompt_round_scheduler_corrected.txt` |
| duplicate ledger | `docs/core/V12_Research_No_Repeat_Index.md` |
| primary price source | `Songdaiki/stock-web` |
| price source URL | `https://github.com/Songdaiki/stock-web` |
| manifest | `atlas/manifest.json` |
| schema | `atlas/schema.json` |
| symbol profile | `atlas/symbol_profiles/064/064350.json` |
| tradable shards | `atlas/ohlcv_tradable_by_symbol_year/064/064350/2022.csv`, `2023.csv`, `2024.csv` |
| price basis | `tradable_raw` |
| price adjustment status | `raw_unadjusted_marcap` |
| stock_web_manifest_max_date | `2026-02-20` |

Manifest fields verified: source_name=`FinanceData/marcap`, price_adjustment_status=`raw_unadjusted_marcap`, min_date=`1995-05-02`, max_date=`2026-02-20`, tradable_row_count=`14354401`, symbol_count=`5414`, calibration_shard_root=`atlas/ohlcv_tradable_by_symbol_year`, raw_shard_root=`atlas/ohlcv_raw_by_symbol_year`.

Symbol profile fields verified for `064350`:

```text
current_or_latest_name = 현대로템
market = KOSPI
first_date = 2013-10-30
last_date = 2026-02-20
trading_day_count = 3021
corporate_action_candidate_count = 1
corporate_action_candidate_dates = [2020-08-14]
calibration_caveat = Corporate-action candidate windows are blocked by default.
```

The selected 2022-07-27, 2022-08-26, and 2023-04-20 windows do not overlap the only listed corporate-action candidate date, 2020-08-14, so the 30D/90D/180D windows are treated as calibration-usable under the stock-web caveat.

## 3. No-Repeat / Coverage Selection

No-Repeat Index snapshot used:

```text
C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG coverage = 7 rows / 4 symbols
C03 top covered symbols = 012450, 079550, 047810, 065450
C03 date range = 2022-07-29~2024-11-12
C03 good/bad Stage2 = 4/1
C03 4B/4C = 0/0
```

Selected combination:

```text
canonical_archetype_id = C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG
symbol = 064350
company = 현대로템
trigger_family = Poland K2 framework/executive contract/localization path
```

Hard duplicate check:

```text
C03 + 064350 + Stage2-Actionable + 2022-07-27 = not present in No-Repeat Index high-repeat table
C03 + 064350 + Stage3-Yellow + 2022-08-26 = not present in No-Repeat Index high-repeat table
C03 + 064350 + Stage4B + 2023-04-20 = not present in No-Repeat Index high-repeat table
hard_duplicate_avoided = true
```

This is a useful expansion because C03 has no existing 4B/4C coverage in the index snapshot and `064350` is not one of the listed top-covered C03 symbols.

## 4. Historical Evidence Context

The non-price evidence path is not a generic defense theme. It has a dated company-level export framework and later executive contract path.

| date | evidence role | evidence summary | scoring implication |
|---|---|---|---|
| 2022-07-27 | Stage2/Actionable trigger | Poland/PGZ and Hyundai Rotem K2 framework path became public; the framework linked Hyundai Rotem to a large K2 supply/localization route. | Company-level export framework is enough for Stage2-Actionable candidate, not automatically Stage3-Green. |
| 2022-08-26 | Stage3-Yellow / strictness trigger | First executive agreement for 180 K2 tanks was signed. | Stronger than framework; however entry occurred after a large price move and was followed by high MAE, so Green should require contract-margin/revision and price-path alignment. |
| 2023-03-31 / 2023-04-20 price response | 4B watch trigger | Foundational/localization agreement for K2PL production in Poland became part of the narrative. Price accelerated again in April 2023. | Useful as 4B / valuation-overheat watch, not a fresh positive entry without incremental EPS/margin evidence. |

External evidence references used for historical dating:

- Reuters later summary confirming Hyundai Rotem/Poland first-batch 2022 agreement and second-batch context: `https://www.reuters.com/business/aerospace-defense/poland-completes-negotiations-buy-south-korean-k2-tanks-agency-says-2025-07-02/`
- Reuters later summary of second contract and explicit reference to the earlier 2022 180-tank deal: `https://www.reuters.com/markets/emerging/poland-signs-contract-buy-more-south-korean-battle-tanks-2025-08-01/`
- K2 export chronology source used only for historical event dating and cross-checking, not as price data: `https://en.wikipedia.org/wiki/K2_Black_Panther`

## 5. Stock-Web OHLC Path Calculations

All calculations use stock-web tradable raw OHLC rows. Returns are calculated as:

```text
MFE_N_pct = (max_high_in_window / entry_price - 1) * 100
MAE_N_pct = (min_low_in_window / entry_price - 1) * 100
peak_drawdown_pct = (post_peak_min_low / peak_price - 1) * 100
```

### 5.1 Trigger A — Stage2-Actionable, framework agreement recognition

```text
symbol = 064350
entry_date = 2022-07-27
entry_price = 25000.0
entry_row = 2022-07-27, o=25650, h=25900, l=24050, c=25000, v=13917584
```

Window observations from stock-web rows:

```text
30D max_high = 32850.0 on 2022-08-26
30D min_low = 24050.0 on 2022-07-27
90D max_high = 32850.0 on 2022-08-26
90D min_low = 23050.0 on 2022-10-27
180D max_high = 32850.0 on 2022-08-26
180D min_low = 23050.0 on 2022-10-27
peak_date_180D = 2022-08-26
peak_price_180D = 32850.0
post_peak_min_low_180D = 23050.0
```

| metric | value |
|---|---:|
| MFE_30D_pct | 31.4000 |
| MAE_30D_pct | -3.8000 |
| MFE_90D_pct | 31.4000 |
| MAE_90D_pct | -7.8000 |
| MFE_180D_pct | 31.4000 |
| MAE_180D_pct | -7.8000 |
| peak_return_180D_pct | 31.4000 |
| drawdown_after_peak_180D_pct | -29.8326 |

Interpretation: this was a usable Stage2-Actionable trigger. The contract framework was not yet a fully margin-verified Green, but the entry had strong asymmetric MFE with tolerable MAE before the later drawdown.

### 5.2 Trigger B — Stage3-Yellow / false-Green stress, executive agreement

```text
symbol = 064350
entry_date = 2022-08-26
entry_price = 30550.0
entry_row = 2022-08-26, o=32700, h=32850, l=30150, c=30550, v=12602955
```

Window observations:

```text
30D max_high = 32850.0 on 2022-08-26
30D min_low = 23500.0 on 2022-10-12 / 2022-10-13
90D max_high = 32850.0 on 2022-08-26
90D min_low = 23050.0 on 2022-10-27
180D max_high = 37800.0 on 2023-04-25
180D min_low = 23050.0 on 2022-10-27
peak_date_180D = 2023-04-25
peak_price_180D = 37800.0
post_peak_min_low_180D = 30850.0 on 2023-05-18
```

| metric | value |
|---|---:|
| MFE_30D_pct | 7.5286 |
| MAE_30D_pct | -23.0769 |
| MFE_90D_pct | 7.5286 |
| MAE_90D_pct | -24.5499 |
| MFE_180D_pct | 23.7316 |
| MAE_180D_pct | -24.5499 |
| peak_return_180D_pct | 23.7316 |
| drawdown_after_peak_180D_pct | -18.3862 |

Interpretation: the executive agreement was real non-price evidence, but the trigger came after a large pre-run and produced a severe 30D/90D MAE. This is not a clean fresh Green entry. It is better classified as Stage3-Yellow / high-MAE success / false-Green stress. C03 should keep a Green gate requiring contract quality, backlog conversion, margin/revision visibility, and price-path alignment.

### 5.3 Trigger C — 4B watch, April 2023 localization/continuation repricing

```text
symbol = 064350
entry_date = 2023-04-20
entry_price = 31700.0
entry_row = 2023-04-20, o=28600, h=33150, l=28500, c=31700, v=30787700
```

Window observations:

```text
30D max_high = 37800.0 on 2023-04-25
30D min_low = 30550.0 on 2023-05-30
90D max_high = 40250.0 on 2023-06-21
90D min_low = 30050.0 on 2023-07-26 / 2023-08-04
180D max_high = 40250.0 on 2023-06-21
180D min_low = 23050.0 on 2023-10-31
peak_date_180D = 2023-06-21
peak_price_180D = 40250.0
post_peak_min_low_180D = 23050.0
```

| metric | value |
|---|---:|
| MFE_30D_pct | 19.2429 |
| MAE_30D_pct | -3.6278 |
| MFE_90D_pct | 26.9716 |
| MAE_90D_pct | -5.2050 |
| MFE_180D_pct | 26.9716 |
| MAE_180D_pct | -27.2871 |
| peak_return_180D_pct | 26.9716 |
| drawdown_after_peak_180D_pct | -42.7329 |

Interpretation: the April 2023 continuation move was useful for 4B watch and peak-capture logic. It should not be used as a fresh Stage2/Green entry unless there is new, verified non-price evidence that upgrades earnings visibility rather than merely extending the existing Poland K2 narrative.

## 6. Stage Evidence Separation

| evidence layer | Stage2 | Stage3 | 4B | 4C |
|---|---|---|---|---|
| public event / disclosure | Poland K2 framework | first executive contract | localization/production continuation | none observed in this path |
| customer / order quality | sovereign customer, defense modernization urgency | 180 K2 executive order | Europe/local production narrative | none |
| backlog / delivery visibility | framework route visible | delivery route stronger | no new incremental EPS proof in price surge | none |
| margin / EPS bridge | incomplete | still incomplete at trigger date | not enough for fresh positive entry | none |
| price path | strong MFE with tolerable early MAE | high MAE after late entry | peak-capture and later drawdown | no hard thesis break |
| RedTeam | moderate because margin unknown | Green-block due high MAE / late trigger | 4B watch | no 4C trigger |

## 7. Current Calibrated Profile Stress Test

Current calibrated proxy assumptions:

```text
stage2_actionable_evidence_bonus = +2.0
stage3_yellow_total_min = 75.0
stage3_green_total_min = 87.0
stage3_green_revision_min = 55.0
stage3_cross_evidence_green_buffer = +1.5
price_only_blowoff_blocks_positive_stage = true
full_4b_requires_non_price_evidence = true
hard_4c_thesis_break_routes_to_4c = true
```

Stress-test verdict:

| trigger | current profile expectation | residual finding |
|---|---|---|
| 2022-07-27 framework | Stage2-Actionable allowed with non-price evidence | Pass. This is the useful C03 early entry. |
| 2022-08-26 executive contract | Could look like Stage3-Green if contract evidence is over-weighted | Residual risk. High MAE and late price path argue for Stage3-Yellow unless margin/revision proof is visible. |
| 2023-04-20 continuation repricing | 4B watch should activate before full 4B | Pass/strengthen. Later drawdown supports 4B watch after renewed price acceleration. |

Residual contribution:

```text
current_profile_error_count = 1
residual_error_type = contract_evidence_green_too_easy_without_price_path_alignment
recommended_shadow_rule = C03 Green must require contract_quality + backlog/delivery visibility + margin/revision bridge + no high-MAE late-entry pattern.
```

## 8. Positive / Counterexample Balance

```text
positive_structural_success = 1
counterexample_or_failed_rerating = 1
4B_or_4C_case = 1
calibration_usable_case_count = 3
new_independent_case_count = 3
reused_case_count = 0
counterexample_count = 1
```

This is not a broad global rule proposal. It is a C03-specific residual row set. The value is filling a missing C03 symbol and adding a 4B path, not loosening Green.

## 9. Score Simulation

| trigger_id | raw component interpretation | simulated current stage | residual action |
|---|---|---|---|
| C03_064350_20220727_STAGE2_FRAMEWORK | EPS/FCF early 12, visibility 15, bottleneck 13, mispricing 11, valuation 10, capital 3, info 4; total proxy 68 | Stage2-Actionable | keep as early C03 candidate |
| C03_064350_20220826_STAGE3_YELLOW_EXECUTIVE | EPS/FCF 15, visibility 20, bottleneck 15, mispricing 10, valuation 9, capital 3, info 5; total proxy 77 | Stage3-Yellow | block Green unless margin/revision bridge appears |
| C03_064350_20230420_4B_WATCH | EPS/FCF 13, visibility 18, bottleneck 14, mispricing 6, valuation 5, capital 3, info 5; total proxy 64 with price-overheat diagnostic | 4B-watch / no fresh positive stage | keep full 4B non-price requirement |

## 10. Machine-Readable Rows

### 10.1 case rows JSONL

```jsonl
{"row_type":"case","schema_family":"v12_sector_archetype_residual","case_id":"C03_064350_K2_POLAND_FRAMEWORK_EXECUTIVE_PATH","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG","fine_archetype_id":"DEFENSE_EXPORT_POLAND_K2_FRAMEWORK_EXECUTIVE_4B_PATH","symbol":"064350","company_name":"현대로템","positive_or_counterexample":"positive","case_type":"structural_success","loop_objective":"coverage_gap_fill|green_strictness_stress_test|4B_non_price_requirement_stress_test","new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"case","schema_family":"v12_sector_archetype_residual","case_id":"C03_064350_K2_EXECUTIVE_HIGH_MAE_FALSE_GREEN_STRESS","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG","fine_archetype_id":"DEFENSE_EXPORT_POLAND_K2_FRAMEWORK_EXECUTIVE_4B_PATH","symbol":"064350","company_name":"현대로템","positive_or_counterexample":"counterexample","case_type":"high_mae_success","loop_objective":"green_strictness_stress_test","new_independent_case":true,"reuse_reason":"same_symbol_new_trigger_family_executive_contract_after_framework","independent_evidence_weight":0.5,"do_not_count_as_new_case":false}
{"row_type":"case","schema_family":"v12_sector_archetype_residual","case_id":"C03_064350_K2PL_LOCALIZATION_4B_WATCH","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG","fine_archetype_id":"DEFENSE_EXPORT_POLAND_K2_FRAMEWORK_EXECUTIVE_4B_PATH","symbol":"064350","company_name":"현대로템","positive_or_counterexample":"counterexample","case_type":"4B_overlay_success","loop_objective":"4B_non_price_requirement_stress_test","new_independent_case":true,"reuse_reason":"same_symbol_new_trigger_family_4b_continuation_path","independent_evidence_weight":0.5,"do_not_count_as_new_case":false}
```

### 10.2 trigger rows JSONL

```jsonl
{"row_type":"trigger","trigger_id":"C03_064350_20220727_STAGE2_FRAMEWORK","case_id":"C03_064350_K2_POLAND_FRAMEWORK_EXECUTIVE_PATH","round":"R1","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG","fine_archetype_id":"DEFENSE_EXPORT_POLAND_K2_FRAMEWORK_EXECUTIVE_4B_PATH","symbol":"064350","company_name":"현대로템","trigger_type":"Stage2-Actionable","trigger_family":"poland_k2_framework_agreement","trigger_date":"2022-07-27","entry_date":"2022-07-27","entry_price":25000.0,"price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","MFE_30D_pct":31.4,"MAE_30D_pct":-3.8,"MFE_90D_pct":31.4,"MAE_90D_pct":-7.8,"MFE_180D_pct":31.4,"MAE_180D_pct":-7.8,"peak_date":"2022-08-26","peak_price":32850.0,"peak_return_from_entry_pct":31.4,"drawdown_after_peak_pct":-29.8326,"forward_window_trading_days":180,"corporate_action_window_status":"clean_no_overlap","calibration_usable":true,"aggregate_group_role":"representative","dedupe_for_aggregate":true,"positive_or_counterexample":"positive","current_profile_verdict":"current_profile_correct_stage2_actionable","trigger_outcome_label":"good_stage2","evidence_source":"public_event|defense_export_framework|stock_web_ohlc","evidence_url_pending":false,"source_proxy_only":false,"same_archetype_new_symbol_count":1,"same_archetype_new_trigger_family_count":1,"new_independent_case_count":1,"reused_case_count":0,"loop_contribution_label":"new_independent_signal"}
{"row_type":"trigger","trigger_id":"C03_064350_20220826_STAGE3_YELLOW_EXECUTIVE","case_id":"C03_064350_K2_EXECUTIVE_HIGH_MAE_FALSE_GREEN_STRESS","round":"R1","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG","fine_archetype_id":"DEFENSE_EXPORT_POLAND_K2_FRAMEWORK_EXECUTIVE_4B_PATH","symbol":"064350","company_name":"현대로템","trigger_type":"Stage3-Yellow","trigger_family":"poland_k2_executive_contract_high_mae_green_stress","trigger_date":"2022-08-26","entry_date":"2022-08-26","entry_price":30550.0,"price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","MFE_30D_pct":7.5286,"MAE_30D_pct":-23.0769,"MFE_90D_pct":7.5286,"MAE_90D_pct":-24.5499,"MFE_180D_pct":23.7316,"MAE_180D_pct":-24.5499,"peak_date":"2023-04-25","peak_price":37800.0,"peak_return_from_entry_pct":23.7316,"drawdown_after_peak_pct":-18.3862,"forward_window_trading_days":180,"corporate_action_window_status":"clean_no_overlap","calibration_usable":true,"aggregate_group_role":"representative","dedupe_for_aggregate":true,"positive_or_counterexample":"counterexample","current_profile_verdict":"current_profile_green_too_easy_if_contract_only","trigger_outcome_label":"high_mae_success_false_green_stress","evidence_source":"public_contract_event|stock_web_ohlc","evidence_url_pending":false,"source_proxy_only":false,"same_archetype_new_symbol_count":0,"same_archetype_new_trigger_family_count":1,"new_independent_case_count":1,"reused_case_count":0,"loop_contribution_label":"residual_error_found"}
{"row_type":"trigger","trigger_id":"C03_064350_20230420_4B_WATCH","case_id":"C03_064350_K2PL_LOCALIZATION_4B_WATCH","round":"R1","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG","fine_archetype_id":"DEFENSE_EXPORT_POLAND_K2_FRAMEWORK_EXECUTIVE_4B_PATH","symbol":"064350","company_name":"현대로템","trigger_type":"Stage4B","trigger_family":"k2pl_localization_continuation_repricing_4b_watch","trigger_date":"2023-04-20","entry_date":"2023-04-20","entry_price":31700.0,"price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","MFE_30D_pct":19.2429,"MAE_30D_pct":-3.6278,"MFE_90D_pct":26.9716,"MAE_90D_pct":-5.205,"MFE_180D_pct":26.9716,"MAE_180D_pct":-27.2871,"peak_date":"2023-06-21","peak_price":40250.0,"peak_return_from_entry_pct":26.9716,"drawdown_after_peak_pct":-42.7329,"four_b_local_peak_proximity":0.9392,"four_b_full_window_peak_proximity":1.0,"forward_window_trading_days":180,"corporate_action_window_status":"clean_no_overlap","calibration_usable":true,"guardrail_usable":true,"aggregate_group_role":"representative","dedupe_for_aggregate":true,"positive_or_counterexample":"counterexample","current_profile_verdict":"current_profile_correct_4b_watch_but_scope_undercovered","trigger_outcome_label":"good_4b_timing_with_later_drawdown","evidence_source":"public_continuation_event|stock_web_ohlc","evidence_url_pending":false,"source_proxy_only":false,"same_archetype_new_symbol_count":0,"same_archetype_new_trigger_family_count":1,"new_independent_case_count":1,"reused_case_count":0,"loop_contribution_label":"counterexample_added"}
```

### 10.3 score_simulation rows JSONL

```jsonl
{"row_type":"score_simulation","trigger_id":"C03_064350_20220727_STAGE2_FRAMEWORK","baseline_current_proxy":"e2r_2_1_stock_web_calibrated","simulated_stage":"Stage2-Actionable","raw_component_scores_before":{"eps_fcf_explosion":12,"earnings_visibility":15,"bottleneck_pricing":13,"market_mispricing":11,"valuation_rerating":10,"capital_allocation":3,"information_confidence":4},"raw_total_proxy":68,"existing_axis_tested":"stage2_actionable_evidence_bonus","existing_axis_verdict":"existing_axis_kept","reason":"company-level export framework plus Stock-Web MFE/MAE supports early Stage2 but not Green."}
{"row_type":"score_simulation","trigger_id":"C03_064350_20220826_STAGE3_YELLOW_EXECUTIVE","baseline_current_proxy":"e2r_2_1_stock_web_calibrated","simulated_stage":"Stage3-Yellow","raw_component_scores_before":{"eps_fcf_explosion":15,"earnings_visibility":20,"bottleneck_pricing":15,"market_mispricing":10,"valuation_rerating":9,"capital_allocation":3,"information_confidence":5},"raw_total_proxy":77,"existing_axis_tested":"stage3_green_total_min|stage3_green_revision_min|stage3_cross_evidence_green_buffer","existing_axis_verdict":"existing_axis_strengthened","reason":"contract evidence was real but price-path alignment failed after a late high-MAE entry."}
{"row_type":"score_simulation","trigger_id":"C03_064350_20230420_4B_WATCH","baseline_current_proxy":"e2r_2_1_stock_web_calibrated","simulated_stage":"Stage4B-watch","raw_component_scores_before":{"eps_fcf_explosion":13,"earnings_visibility":18,"bottleneck_pricing":14,"market_mispricing":6,"valuation_rerating":5,"capital_allocation":3,"information_confidence":5},"raw_total_proxy":64,"existing_axis_tested":"full_4b_requires_non_price_evidence","existing_axis_verdict":"existing_axis_kept","reason":"new price acceleration after continuation narrative produced good 4B timing and later drawdown, but not a fresh Green."}
```

### 10.4 aggregate / shadow / residual rows JSONL

```jsonl
{"row_type":"aggregate_metric","group_name":"canonical_archetype_id","group_value":"C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG","new_symbol_count":1,"new_trigger_family_count":3,"positive_case_count":1,"counterexample_count":1,"4B_case_count":1,"4C_case_count":0,"good_stage2_count":1,"bad_stage2_count":1,"good_4b_timing_count":1,"evidence_url_pending_count":0,"source_proxy_only_count":0,"hard_duplicate_avoided":true,"coverage_gap_filled":"C03 lacked 064350 and had no 4B/4C coverage in No-Repeat snapshot."}
{"row_type":"shadow_weight","scope":"canonical_archetype","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG","axis":"stage3_green_contract_quality_price_path_gate","decision":"hold_for_more_evidence","shadow_candidate_value":"require_contract_quality_plus_margin_revision_plus_price_path_alignment","max_delta":"guardrail_only","reason":"Hyundai Rotem shows early Stage2 worked, but executive-contract late entry suffered high MAE; C03 Green should not be contract-title-only."}
{"row_type":"shadow_weight","scope":"canonical_archetype","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG","axis":"local_4b_watch_guard","decision":"apply_next_patch_candidate_after_batch_review","shadow_candidate_value":"price_acceleration_after_existing_contract_route_is_4b_watch_until_incremental_margin_revision","max_delta":"guardrail_only","reason":"April 2023 continuation repricing captured local peak and subsequent drawdown."}
{"row_type":"residual_contribution","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG","current_profile_error_count":1,"residual_error_type":"contract_evidence_green_too_easy_without_price_path_alignment","new_independent_case_count":3,"reused_case_count":0,"counterexample_count":1,"index_update_needed":true}
{"row_type":"narrative_only","note":"Reuters/Wikipedia/defense chronology sources are used only to date public non-price events; all return calculations use Songdaiki/stock-web tradable raw OHLC rows."}
```

## 11. Residual Rule Candidate

C03 currently has a runtime policy that allows Green with government backlog and delivery visibility. This Hyundai Rotem path supports that policy for Stage2, but adds a stricter Green distinction.

```text
C03_GREEN_GATE_CANDIDATE:
  allow_stage2_if:
    - sovereign/government customer framework or executive contract is public
    - stock-web price path shows MFE/MAE asymmetry is not price-only noise
  block_or_downgrade_green_if:
    - entry is after large pre-run
    - MAE_30D <= -20% or MAE_90D <= -20%
    - no margin/revision bridge is visible as of trigger date
    - contract evidence is title-level without delivery/margin conversion
  route_to_4B_watch_if:
    - existing contract narrative re-accelerates price
    - peak proximity is high
    - later drawdown confirms overheat risk
```

This is a `hold_for_more_evidence` / batch-review candidate, not an immediate production patch.

## 12. Novelty / Diversity Summary

```text
selected_round = R1
round_scheduler_override_used = true
round_as_taxonomy_only = true
round_sector_consistency = pass
large_sector_id = L1_INDUSTRIALS_INFRA_DEFENSE_GRID
canonical_archetype_id = C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG
fine_archetype_id = DEFENSE_EXPORT_POLAND_K2_FRAMEWORK_EXECUTIVE_4B_PATH
new_independent_case_count = 3
reused_case_count = 0
new_symbol_count = 1
same_archetype_new_symbol_count = 1
same_archetype_new_trigger_family_count = 3
new_trigger_family_count = 3
positive_case_count = 1
counterexample_count = 1
current_profile_error_count = 1
diversity_score_summary = new_symbol_plus_new_trigger_families_plus_4B_path
loop_contribution_label = residual_error_found
do_not_propose_new_weight_delta = false
hard_duplicate_avoided = true
index_update_needed = true
```

One-line contribution:

```text
This standalone run adds 3 new independent trigger-family cases, 1 counterexample, and 1 current-profile residual error for R1/L1_INDUSTRIALS_INFRA_DEFENSE_GRID/C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG using 064350 Hyundai Rotem's Poland K2 path.
```

## 13. Deferred Coding Agent Handoff Prompt

```text
You are a coding agent working in Songdaiki/stock_agent.
Do not execute this prompt during the research run that generated this file.

Task:
Ingest this standalone v12 no-repeat residual research MD as a new docs/round-compatible or standalone calibration artifact.

Required checks:
1. Confirm `price_data_source == Songdaiki/stock-web` for all trigger rows.
2. Confirm `price_basis == tradable_raw` and `price_adjustment_status == raw_unadjusted_marcap`.
3. Confirm `canonical_archetype_id == C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG` exists in runtime weight profile.
4. Confirm No-Repeat hard key is not already present:
   - C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG + 064350 + Stage2-Actionable + 2022-07-27
   - C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG + 064350 + Stage3-Yellow + 2022-08-26
   - C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG + 064350 + Stage4B + 2023-04-20
5. Validate MFE/MAE windows from stock-web tradable shards.
6. Add rows only if validation passes; otherwise write rejected rows with explicit reasons.
7. Do not loosen Stage3-Green globally.
8. Treat proposed C03 Green gate as shadow/hold-for-more-evidence unless later batch support confirms it.
9. Update V12_Research_No_Repeat_Index.md after ingestion.

Expected output classification:
- Stage2 framework row: usable positive Stage2 evidence.
- Executive-contract row: counterexample / high-MAE false-Green stress.
- April continuation row: 4B watch guardrail evidence.
```

