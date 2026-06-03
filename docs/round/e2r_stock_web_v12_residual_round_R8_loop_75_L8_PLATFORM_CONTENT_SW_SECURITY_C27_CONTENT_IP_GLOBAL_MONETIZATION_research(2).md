# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
scheduled_round: R8
scheduled_loop: 75
round_schedule_status: valid
round_sector_consistency: pass
computed_next_round: R9
computed_next_loop: 75
large_sector_id: L8_PLATFORM_CONTENT_SW_SECURITY
canonical_archetype_id: C27_CONTENT_IP_GLOBAL_MONETIZATION
fine_archetype_id: C27_GLOBAL_LAUNCH_RETENTION_MONETIZATION_MARGIN_BRIDGE_GUARD
loop_objective: coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | canonical_archetype_compression
price_source: Songdaiki/stock-web
stock_web_manifest_max_date: 2026-02-20
production_scoring_changed: false
shadow_weight_only: true
```

## 1. Current Calibrated Profile Assumption

```text
current_default_profile_proxy = e2r_2_1_stock_web_calibrated
previous_baseline_reference = e2r_2_0_baseline
stage2_actionable_evidence_bonus = +2.0
stage3_yellow_total_min = 75.0
stage3_green_total_min = 87.0
stage3_green_revision_min = 55.0
stage3_cross_evidence_green_buffer = +1.5
price_only_blowoff_blocks_positive_stage = true
full_4b_requires_non_price_evidence = true
hard_4c_thesis_break_routes_to_4c = true
```

## 2. Round / Large Sector / Canonical Archetype Scope

R8 maps to `L8_PLATFORM_CONTENT_SW_SECURITY`. The previous R8 loop used C28 software/security contract retention, so this run rotates to C27 content/IP global monetization. The focus is not top-covered K-pop/content names. It is game/content IP where MFE often appears before launch, but durable value requires global launch, retention, monetization, revenue and margin bridge.

| layer | id | definition |
|---|---|---|
| round | R8 | platform / content / software / security |
| large_sector | L8_PLATFORM_CONTENT_SW_SECURITY | platform, content, software, security, IP monetization |
| canonical | C27_CONTENT_IP_GLOBAL_MONETIZATION | content IP, game IP, global launch, monetization |
| fine | C27_GLOBAL_LAUNCH_RETENTION_MONETIZATION_MARGIN_BRIDGE_GUARD | IP signal must become launch, retention, monetization and margin evidence |
| deep | AAA_GAME_IP_GLOBAL_LAUNCH_VISIBILITY_TO_WISHLIST_PIPELINE_AND_MONETIZATION_OPTION_VALUE | game IP positive |
| deep | BLOCKCHAIN_GAME_TOKEN_AND_NEW_TITLE_OPTIONALITY_WITHOUT_USER_RETENTION_REVENUE_MARGIN_CONVERSION | blockchain game/theme false positive |
| deep | MOBILE_GAME_IP_PIPELINE_OPTIONALITY_WITHOUT_USER_RETENTION_REORDER_REVENUE_MARGIN_CONVERSION | mobile game pipeline false positive |

## 3. No-Repeat / Coverage Check

No-Repeat hard duplicate key:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

C27 top-covered symbols are `035900`, `194480`, `259960`, `352820`, `225570`, and `253450`. This run avoids that cluster and also avoids the previous R8/C28 representatives.

| archetype | selected symbol | duplicate status | reason |
|---|---:|---|---|
| C27 | 263750 | new independent | not top-covered C27 symbol; AAA game IP/global launch monetization bridge |
| C27 | 112040 | new independent | not top-covered C27 symbol; blockchain game/IP MFE without durable monetization bridge |
| C27 | 293490 | new independent | not top-covered C27 symbol; mobile game IP/pipeline low-MFE high-MAE counterexample |

## 4. Stock-Web OHLC Input / Price Source Validation

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","source_name":"FinanceData/marcap","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
```

Stock-web assumptions:

```text
source_name = FinanceData/marcap
price_adjustment_status = raw_unadjusted_marcap
min_date = 1995-05-02
max_date = 2026-02-20
tradable_row_count = 14354401
symbol_count = 5414
calibration_shard_root = atlas/ohlcv_tradable_by_symbol_year
tradable columns = d,o,h,l,c,v,a,mc,s,m
```

## 5. Historical Eligibility Gate

```text
entry row exists = true
forward 180 trading days available = true
MFE/MAE 30D/90D/180D computed = true
price_basis = tradable_raw
price_adjustment_status = raw_unadjusted_marcap
corporate_action_window_status = clean_180D_window
```

Corporate-action caveat:

```text
263750 has a 2021-04-16 corporate-action candidate, outside the selected 2024 representative window.
112040 has corporate-action candidates ending 2021-10-06, outside the selected 2024 representative window.
293490 has no corporate-action candidate dates.
All three representative 180D windows are treated as clean for this residual calibration.
```

## 6. Case Selection Summary

| role | symbol | company | trigger | entry | price | result |
|---|---:|---|---|---:|---:|---|
| game_IP_global_launch_success_then_4B_watch | 263750 | 펄어비스 | Stage2-Actionable | 2024-03-25 | 30000 | global game IP launch visibility worked, but launch/drawdown 4B watch required |
| game_token_IP_MFE_then_high_MAE_counterexample | 112040 | 위메이드 | Stage2-Actionable | 2024-03-11 | 55000 | blockchain game/IP MFE lacked durable retention/monetization bridge |
| mobile_game_IP_low_MFE_high_MAE_counterexample | 293490 | 카카오게임즈 | Stage2-Actionable | 2024-01-29 | 24600 | mobile game IP/pipeline theme produced shallow MFE and high MAE |

## 7. Positive vs Counterexample Balance

```text
positive_case_count: 1
counterexample_count: 2
4B_case_count: 3
4C_or_high_MAE_watch_count: 3
calibration_usable_case_count: 3
current_profile_error_count: 2
```

## 8. Trigger-Level OHLC Backtest Table

| symbol | company | trigger | entry_date | entry_price | MFE30 | MFE90 | MFE180 | MAE30 | MAE90 | MAE180 | peak_date | peak_price | DD after peak |
|---:|---|---|---|---:|---:|---:|---:|---:|---:|---:|---|---:|---:|
| 263750 | 펄어비스 | Stage2-Actionable | 2024-03-25 | 30000 | 35.83 | 58.83 | 58.83 | -11.33 | -11.33 | -11.33 | 2024-07-10 | 47650 | -29.49 |
| 112040 | 위메이드 | Stage2-Actionable | 2024-03-11 | 55000 | 46.36 | 46.36 | 46.36 | -15.91 | -24.45 | -45.45 | 2024-03-20 | 80500 | -62.73 |
| 293490 | 카카오게임즈 | Stage2-Actionable | 2024-01-29 | 24600 | 7.11 | 7.11 | 7.11 | -7.32 | -13.62 | -33.25 | 2024-02-05 | 26350 | -37.69 |

## 9. Case-by-Case Notes

### 9.1 263750 / 펄어비스 — game IP global launch monetization bridge

The entry row is 2024-03-25 at 30,000. The 30D path reached 40,750 and the 90D/180D path reached 47,650. This is a valid C27 positive because the bridge is not just “game stock moved.” The bridge is AAA IP, global launch visibility, pipeline/wishlist optionality and monetization option value. Still, the post-peak low reached 33,600, so Green should remain blocked.

### 9.2 112040 / 위메이드 — blockchain game/IP theme without durable monetization

The entry row is 2024-03-11 at 55,000. The stock reached 80,500 quickly, but later fell to 30,000. MFE was real, but it did not prove durable user retention, global launch revenue, token/platform economics, margin or cashflow bridge. This is a 4B/high-MAE row, not a Stage3-Green row.

### 9.3 293490 / 카카오게임즈 — mobile game IP/pipeline false start

The entry row is 2024-01-29 at 24,600. The best forward high was 26,350, while the 180D low fell to 16,420. This is the clean C27 false-positive shape: mobile game IP or pipeline optionality without user retention, reorder monetization, revenue and margin bridge should be demoted.

## 10. Current Calibrated Profile Stress Test

| question | result |
|---|---|
| Stage2 actionable bonus too strong? | Yes when C27 treats game/content IP theme MFE as enough evidence. |
| Stage3 Yellow threshold too loose? | Not globally; C27 needs global launch/retention/monetization/margin bridge before Yellow. |
| Stage3 Green too strict? | Correct. This round reinforces strict Green. |
| Price-only blowoff guard appropriate? | Yes, especially for 112040 event spike and 293490 weak local peak. |
| Full 4B non-price requirement appropriate? | Yes. 263750 has a better non-price bridge; 112040/293490 do not. |
| 4C timing issue? | High-MAE watch is useful; no immediate hard 4C production delta proposed. |

## 11. Stage2 / Yellow / Green Comparison

```text
263750:
  Stage2-Actionable = correct
  Stage3-Yellow = allowed after global launch / IP monetization bridge
  Stage3-Green = reject unless launch execution, retention and post-peak drawdown clear

112040:
  Stage2-Actionable = acceptable only as game-token/IP event watch
  Stage3-Yellow = reject without user retention, revenue, margin or cashflow bridge
  Stage3-Green = reject despite MFE

293490:
  Stage2-Actionable = too generous if based only on mobile game IP/pipeline theme
  Stage3-Yellow = reject without retention, reorder monetization, revenue and margin bridge
  Stage3-Green = reject
```

## 12. 4B Local vs Full-window Timing Audit

| symbol | local_peak_proximity | full_window_peak_proximity | verdict |
|---:|---:|---:|---|
| 263750 | 0.86 | 1.00 | game IP launch bridge positive but full-window 4B/drawdown watch |
| 112040 | 1.00 | 1.00 | blockchain game theme MFE but no durable monetization bridge; keep 4B/high-MAE watch |
| 293490 | 1.00 | 1.00 | mobile game pipeline theme local 4B watch, not positive stage |

## 13. Canonical-Archetype Rule Candidate

```text
canonical_archetype_rule_candidate: true
rule_scope: canonical_archetype_specific
rule_id: c27_requires_global_launch_retention_monetization_margin_bridge

rule:
  For C27 content/IP global-monetization rows, do not promote game,
  content, music, fan platform, mobile game, blockchain game, or IP-pipeline
  Stage2 signals into Stage3-Yellow/Green unless at least one non-price bridge is visible:
  global launch visibility, user retention, MAU/ARPU or reorder monetization,
  platform distribution, revenue conversion, margin conversion, FCF/cash conversion,
  or earnings revision tied to IP monetization.
```

## 14. Before / After Backtest Comparison

| profile | eligible triggers | avg MFE90 | avg MAE90 | false positive rate | verdict |
|---|---:|---:|---:|---:|---|
| P0 e2r_2_1_stock_web_calibrated_proxy | 3 | 37.43 | -16.47 | 66.7% | too generous to game/content IP theme rows |
| P0b e2r_2_0_baseline_reference | 3 | 37.43 | -16.47 | 33.3% | safer but may miss 263750 |
| P1 sector_specific_candidate_profile | 3 | 37.43 | -16.47 | 66.7% | no broad L8 loosen |
| P2 canonical_archetype_candidate_profile | 1 selected positive | 58.83 | -11.33 | 0% after bridge gate | preferred shadow |
| P3 counterexample_guard_profile | 2 rejected/watch | 26.73 | -19.04 | 0% after no-Green routing | useful guard |

## 15. Score-Return Alignment Matrix

| case | current profile verdict | alignment |
|---|---|---|
| 263750 | current_profile_correct_but_no_green | global-launch/IP monetization bridge aligned with MFE but Green blocked by 4B |
| 112040 | current_profile_false_positive_if_green | game-token/IP MFE lacked retention/monetization bridge |
| 293490 | current_profile_false_positive | mobile game IP row produced shallow MFE and high MAE |

## 16. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive | counterexample | 4B | 4C/watch | new_independent | reused | usable_triggers | representative | profile_errors | sector_rule | canonical_rule | coverage_gap_after |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| L8_PLATFORM_CONTENT_SW_SECURITY | C27_CONTENT_IP_GLOBAL_MONETIZATION | C27_GLOBAL_LAUNCH_RETENTION_MONETIZATION_MARGIN_BRIDGE_GUARD | 1 | 2 | 3 | 3 | 3 | 0 | 3 | 3 | 2 | false | true | R8/C27 non-top-covered content IP monetization residual reduced |

## 17. Residual Contribution Summary

```text
new_independent_case_count: 3
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 3
new_canonical_archetype_count: 0
new_fine_archetype_count: 1
new_trigger_family_count: 3
tested_existing_calibrated_axes:
- stage2_actionable_evidence_bonus
- price_only_blowoff_blocks_positive_stage
- full_4b_requires_non_price_evidence
- local_4b_watch_guard
- high_MAE_guardrail
residual_error_types_found:
- game/IP theme without retention monetization bridge
- global launch IP winner needs 4B watch
- mobile game pipeline low-MFE high-MAE
new_axis_proposed: null
existing_axis_strengthened:
- stage2_required_bridge
- full_4b_requires_non_price_evidence
- local_4b_watch_guard
- high_MAE_watch_guard
existing_axis_weakened: null
existing_axis_kept:
- stage3_green_total_min
- stage3_green_revision_min
sector_specific_rule_candidate: false
canonical_archetype_rule_candidate: true
loop_contribution_label: canonical_archetype_rule_candidate
```

## 18. Validation Scope / Non-Validation Scope

Validated:

```text
- stock-web tradable_raw OHLC rows
- entry_date / entry_price
- MFE/MAE/peak/drawdown
- R8 direct L8 sector consistency
- large_sector/canonical consistency
- duplicate avoidance at symbol level
- representative rows use clean 180D windows
```

Not validated:

```text
- exact disclosure/report URLs
- exact game launch or platform announcement URLs
- production scoring behavior
- live candidate status
```

## 19. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,c27_requires_global_launch_retention_monetization_margin_bridge,canonical_archetype_specific,L8_PLATFORM_CONTENT_SW_SECURITY,C27_CONTENT_IP_GLOBAL_MONETIZATION,0,1,+1,"C27 content/IP global monetization rows should not promote toward Stage3-Yellow/Green unless IP signal converts into global launch visibility, user retention, MAU/ARPU or reorder monetization, platform distribution, revenue, margin, or cashflow bridge","263750 survives as guarded positive after global-launch/IP monetization bridge; 112040 and 293490 are demoted because game/IP theme MFE lacked durable user-retention and monetization bridge","TRG_R8L75_C27_263750_20240325_GAME_IP_GLOBAL_LAUNCH_MONETIZATION_BRIDGE|TRG_R8L75_C27_112040_20240311_BLOCKCHAIN_GAME_IP_THEME_NO_DURABLE_MONETIZATION|TRG_R8L75_C27_293490_20240129_MOBILE_GAME_IP_PIPELINE_NO_REORDER_MONETIZATION_BRIDGE",3,3,2,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,c27_content_ip_4b_high_mae_watch_guard,canonical_archetype_specific,L8_PLATFORM_CONTENT_SW_SECURITY,C27_CONTENT_IP_GLOBAL_MONETIZATION,1,1,0,"Content/IP winners and game-theme false starts can peak before launch, retention and monetization durability are confirmed; local/full-window 4B and high-MAE watch should remain active","preserves 263750 guarded positive while preventing 112040/293490 IP-theme false positives","TRG_R8L75_C27_263750_20240325_GAME_IP_GLOBAL_LAUNCH_MONETIZATION_BRIDGE|TRG_R8L75_C27_112040_20240311_BLOCKCHAIN_GAME_IP_THEME_NO_DURABLE_MONETIZATION|TRG_R8L75_C27_293490_20240129_MOBILE_GAME_IP_PIPELINE_NO_REORDER_MONETIZATION_BRIDGE",3,3,2,medium,existing_axis_kept,"strengthens local/full-window 4B and high-MAE watch without global delta"
```

## 20. Machine-Readable Rows

### 20.1 price_source_validation

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","source_name":"FinanceData/marcap","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
```

### 20.2 case rows

```jsonl
{"row_type":"case","case_id":"R8L75_C27_263750_20240325_GAME_IP_GLOBAL_LAUNCH_MONETIZATION_BRIDGE","symbol":"263750","company_name":"펄어비스","round":"R8","loop":"75","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C27_CONTENT_IP_GLOBAL_MONETIZATION","fine_archetype_id":"C27_GAME_IP_GLOBAL_LAUNCH_MONETIZATION_BRIDGE","deep_sub_archetype_id":"AAA_GAME_IP_GLOBAL_LAUNCH_VISIBILITY_TO_WISHLIST_PIPELINE_AND_MONETIZATION_OPTION_VALUE","case_type":"game_IP_global_launch_success_then_4B_watch","positive_or_counterexample":"positive","best_trigger":"Stage2-Actionable","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"score_return_aligned","current_profile_verdict":"current_profile_correct_but_no_green","price_source":"Songdaiki/stock-web","notes":"C27 content/IP global monetization rows require global launch visibility, user retention, reorder/MAU/ARPU, platform distribution, revenue, margin or cashflow bridge; IP/theme MFE alone is insufficient."}
{"row_type":"case","case_id":"R8L75_C27_112040_20240311_BLOCKCHAIN_GAME_IP_THEME_NO_DURABLE_MONETIZATION","symbol":"112040","company_name":"위메이드","round":"R8","loop":"75","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C27_CONTENT_IP_GLOBAL_MONETIZATION","fine_archetype_id":"C27_BLOCKCHAIN_GAME_IP_THEME_WITHOUT_DURABLE_GLOBAL_MONETIZATION_BRIDGE","deep_sub_archetype_id":"BLOCKCHAIN_GAME_TOKEN_AND_NEW_TITLE_OPTIONALITY_WITHOUT_USER_RETENTION_REVENUE_MARGIN_CONVERSION","case_type":"game_token_IP_MFE_then_high_MAE_counterexample","positive_or_counterexample":"counterexample","best_trigger":"Stage2-Actionable","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"score_return_mixed","current_profile_verdict":"current_profile_false_positive_if_green","price_source":"Songdaiki/stock-web","notes":"C27 content/IP global monetization rows require global launch visibility, user retention, reorder/MAU/ARPU, platform distribution, revenue, margin or cashflow bridge; IP/theme MFE alone is insufficient."}
{"row_type":"case","case_id":"R8L75_C27_293490_20240129_MOBILE_GAME_IP_PIPELINE_NO_REORDER_MONETIZATION_BRIDGE","symbol":"293490","company_name":"카카오게임즈","round":"R8","loop":"75","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C27_CONTENT_IP_GLOBAL_MONETIZATION","fine_archetype_id":"C27_MOBILE_GAME_IP_PIPELINE_WITHOUT_REORDER_MONETIZATION_BRIDGE","deep_sub_archetype_id":"MOBILE_GAME_IP_PIPELINE_OPTIONALITY_WITHOUT_USER_RETENTION_REORDER_REVENUE_MARGIN_CONVERSION","case_type":"mobile_game_IP_low_MFE_high_MAE_counterexample","positive_or_counterexample":"counterexample","best_trigger":"Stage2-Actionable","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"score_return_misaligned","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"C27 content/IP global monetization rows require global launch visibility, user retention, reorder/MAU/ARPU, platform distribution, revenue, margin or cashflow bridge; IP/theme MFE alone is insufficient."}
```

### 20.3 trigger rows

```jsonl
{"row_type":"trigger","trigger_id":"TRG_R8L75_C27_263750_20240325_GAME_IP_GLOBAL_LAUNCH_MONETIZATION_BRIDGE","case_id":"R8L75_C27_263750_20240325_GAME_IP_GLOBAL_LAUNCH_MONETIZATION_BRIDGE","symbol":"263750","company_name":"펄어비스","round":"R8","loop":"75","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C27_CONTENT_IP_GLOBAL_MONETIZATION","fine_archetype_id":"C27_GAME_IP_GLOBAL_LAUNCH_MONETIZATION_BRIDGE","deep_sub_archetype_id":"AAA_GAME_IP_GLOBAL_LAUNCH_VISIBILITY_TO_WISHLIST_PIPELINE_AND_MONETIZATION_OPTION_VALUE","loop_objective":"coverage_gap_fill|counterexample_mining|stage2_actionable_bonus_stress_test|4B_non_price_requirement_stress_test|canonical_archetype_compression","trigger_type":"Stage2-Actionable","trigger_date":"2024-03-25","entry_date":"2024-03-25","entry_price":30000,"evidence_available_at_that_date":"source_proxy_AAA_game_IP_global_launch_visibility_wishlist_pipeline_monetization_bridge; evidence_url_pending","evidence_source":"source_proxy_AAA_game_IP_global_launch_visibility_wishlist_pipeline_monetization_bridge; evidence_url_pending","bridge_summary":"AAA game IP global launch visibility and pipeline/wishlist optionality converted into monetization bridge, but launch timing and post-peak drawdown required 4B watch","stage2_evidence_fields":["AAA_game_IP","global_launch_visibility","pipeline_optionality","relative_strength"],"stage3_evidence_fields":["launch_to_revenue_visibility","global_monetization_option_value","publisher_or_platform_attention_proxy"],"stage4b_evidence_fields":["post_MFE_peak_watch","launch_delay_or_execution_risk","game_IP_crowding_after_rerating"],"stage4c_evidence_fields":["post_peak_drawdown_watch"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/263/263750/2024.csv","profile_path":"atlas/symbol_profiles/263/263750.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":35.83,"MFE_90D_pct":58.83,"MFE_180D_pct":58.83,"MFE_1Y_pct":58.83,"MFE_2Y_pct":58.83,"MAE_30D_pct":-11.33,"MAE_90D_pct":-11.33,"MAE_180D_pct":-11.33,"MAE_1Y_pct":-11.33,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-07-10","peak_price":47650,"drawdown_after_peak_pct":-29.49,"green_lateness_ratio":"0.44","four_b_local_peak_proximity":0.86,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"game_IP_launch_bridge_positive_but_full_window_4B_drawdown_watch","four_b_evidence_type":"non_price_global_launch_monetization_bridge","four_c_protection_label":"post_peak_drawdown_watch","trigger_outcome_label":"game_IP_global_launch_success_then_4B_watch","current_profile_verdict":"current_profile_correct_but_no_green","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R8L75_C27_263750_20240325_GAME_IP_GLOBAL_LAUNCH_MONETIZATION_BRIDGE_entry","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"TRG_R8L75_C27_112040_20240311_BLOCKCHAIN_GAME_IP_THEME_NO_DURABLE_MONETIZATION","case_id":"R8L75_C27_112040_20240311_BLOCKCHAIN_GAME_IP_THEME_NO_DURABLE_MONETIZATION","symbol":"112040","company_name":"위메이드","round":"R8","loop":"75","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C27_CONTENT_IP_GLOBAL_MONETIZATION","fine_archetype_id":"C27_BLOCKCHAIN_GAME_IP_THEME_WITHOUT_DURABLE_GLOBAL_MONETIZATION_BRIDGE","deep_sub_archetype_id":"BLOCKCHAIN_GAME_TOKEN_AND_NEW_TITLE_OPTIONALITY_WITHOUT_USER_RETENTION_REVENUE_MARGIN_CONVERSION","loop_objective":"coverage_gap_fill|counterexample_mining|stage2_actionable_bonus_stress_test|4B_non_price_requirement_stress_test|canonical_archetype_compression","trigger_type":"Stage2-Actionable","trigger_date":"2024-03-11","entry_date":"2024-03-11","entry_price":55000,"evidence_available_at_that_date":"source_proxy_blockchain_game_token_new_title_theme_without_user_retention_revenue_margin_bridge; evidence_url_pending","evidence_source":"source_proxy_blockchain_game_token_new_title_theme_without_user_retention_revenue_margin_bridge; evidence_url_pending","bridge_summary":"blockchain game/token and new-title optionality produced MFE, but durable user retention, global launch revenue, margin or cashflow bridge did not hold","stage2_evidence_fields":["blockchain_game_theme","new_title_optionality","token_or_platform_beta","relative_strength"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["event_theme_peak","user_retention_bridge_absent","revenue_margin_bridge_absent"],"stage4c_evidence_fields":["high_MAE_without_global_monetization_bridge"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/112/112040/2024.csv","profile_path":"atlas/symbol_profiles/112/112040.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":46.36,"MFE_90D_pct":46.36,"MFE_180D_pct":46.36,"MFE_1Y_pct":46.36,"MFE_2Y_pct":46.36,"MAE_30D_pct":-15.91,"MAE_90D_pct":-24.45,"MAE_180D_pct":-45.45,"MAE_1Y_pct":-45.45,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-03-20","peak_price":80500,"drawdown_after_peak_pct":-62.73,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"blockchain_game_theme_MFE_but_no_durable_monetization_bridge_keep_4B_high_MAE_watch","four_b_evidence_type":"IP_theme_without_durable_monetization_bridge","four_c_protection_label":"high_MAE_watch","trigger_outcome_label":"game_token_IP_MFE_then_high_MAE_counterexample","current_profile_verdict":"current_profile_false_positive_if_green","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R8L75_C27_112040_20240311_BLOCKCHAIN_GAME_IP_THEME_NO_DURABLE_MONETIZATION_entry","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"TRG_R8L75_C27_293490_20240129_MOBILE_GAME_IP_PIPELINE_NO_REORDER_MONETIZATION_BRIDGE","case_id":"R8L75_C27_293490_20240129_MOBILE_GAME_IP_PIPELINE_NO_REORDER_MONETIZATION_BRIDGE","symbol":"293490","company_name":"카카오게임즈","round":"R8","loop":"75","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C27_CONTENT_IP_GLOBAL_MONETIZATION","fine_archetype_id":"C27_MOBILE_GAME_IP_PIPELINE_WITHOUT_REORDER_MONETIZATION_BRIDGE","deep_sub_archetype_id":"MOBILE_GAME_IP_PIPELINE_OPTIONALITY_WITHOUT_USER_RETENTION_REORDER_REVENUE_MARGIN_CONVERSION","loop_objective":"coverage_gap_fill|counterexample_mining|stage2_actionable_bonus_stress_test|4B_non_price_requirement_stress_test|canonical_archetype_compression","trigger_type":"Stage2-Actionable","trigger_date":"2024-01-29","entry_date":"2024-01-29","entry_price":24600,"evidence_available_at_that_date":"source_proxy_mobile_game_IP_pipeline_without_user_retention_reorder_revenue_margin_bridge; evidence_url_pending","evidence_source":"source_proxy_mobile_game_IP_pipeline_without_user_retention_reorder_revenue_margin_bridge; evidence_url_pending","bridge_summary":"mobile game IP/pipeline optionality did not convert into durable user retention, reorder monetization, revenue, margin or cashflow bridge; MFE stayed shallow and MAE expanded","stage2_evidence_fields":["mobile_game_IP_theme","pipeline_optionality","relative_strength"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["weak_local_peak","user_retention_bridge_absent","monetization_margin_bridge_absent"],"stage4c_evidence_fields":["high_MAE_without_user_retention_or_margin_bridge"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/293/293490/2024.csv","profile_path":"atlas/symbol_profiles/293/293490.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":7.11,"MFE_90D_pct":7.11,"MFE_180D_pct":7.11,"MFE_1Y_pct":7.11,"MFE_2Y_pct":7.11,"MAE_30D_pct":-7.32,"MAE_90D_pct":-13.62,"MAE_180D_pct":-33.25,"MAE_1Y_pct":-33.25,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-02-05","peak_price":26350,"drawdown_after_peak_pct":-37.69,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"mobile_game_pipeline_theme_local_4B_watch_not_positive_stage","four_b_evidence_type":"IP_theme_without_durable_monetization_bridge","four_c_protection_label":"high_MAE_watch","trigger_outcome_label":"mobile_game_IP_low_MFE_high_MAE_counterexample","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R8L75_C27_293490_20240129_MOBILE_GAME_IP_PIPELINE_NO_REORDER_MONETIZATION_BRIDGE_entry","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
```

### 20.4 score_simulation rows

```jsonl
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R8L75_C27_263750_20240325_GAME_IP_GLOBAL_LAUNCH_MONETIZATION_BRIDGE","trigger_id":"TRG_R8L75_C27_263750_20240325_GAME_IP_GLOBAL_LAUNCH_MONETIZATION_BRIDGE","symbol":"263750","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C27_CONTENT_IP_GLOBAL_MONETIZATION","raw_component_scores_before":{"IP_strength_score":12,"global_launch_score":12,"retention_monetization_score":9,"revenue_margin_score":9,"relative_strength_score":11,"theme_risk_penalty":6},"weighted_score_before":73,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"IP_strength_score":14,"global_launch_score":15,"retention_monetization_score":12,"revenue_margin_score":11,"relative_strength_score":8,"theme_risk_penalty":8},"weighted_score_after":80,"stage_label_after":"Stage3-Yellow","changed_components":["IP_strength_score","global_launch_score","retention_monetization_score","revenue_margin_score","relative_strength_score","theme_risk_penalty"],"component_delta_explanation":"C27 row is promoted only because IP strength converts into global launch visibility and monetization option bridge; launch execution/drawdown watch blocks Green.","MFE_90D_pct":58.83,"MAE_90D_pct":-11.33,"score_return_alignment_label":"score_return_aligned","current_profile_verdict":"current_profile_correct_but_no_green"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R8L75_C27_112040_20240311_BLOCKCHAIN_GAME_IP_THEME_NO_DURABLE_MONETIZATION","trigger_id":"TRG_R8L75_C27_112040_20240311_BLOCKCHAIN_GAME_IP_THEME_NO_DURABLE_MONETIZATION","symbol":"112040","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C27_CONTENT_IP_GLOBAL_MONETIZATION","raw_component_scores_before":{"IP_strength_score":11,"global_launch_score":7,"retention_monetization_score":1,"revenue_margin_score":1,"relative_strength_score":10,"theme_risk_penalty":8},"weighted_score_before":61,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"IP_strength_score":5,"global_launch_score":3,"retention_monetization_score":0,"revenue_margin_score":0,"relative_strength_score":4,"theme_risk_penalty":16},"weighted_score_after":39,"stage_label_after":"Stage1-Watch_or_4B-HighMAE","changed_components":["IP_strength_score","global_launch_score","retention_monetization_score","revenue_margin_score","relative_strength_score","theme_risk_penalty"],"component_delta_explanation":"C27 guard demotes game/content IP theme rows when global launch, user retention, monetization, revenue, margin and cashflow bridge are absent.","MFE_90D_pct":46.36,"MAE_90D_pct":-24.45,"score_return_alignment_label":"score_return_mixed","current_profile_verdict":"current_profile_false_positive_if_green"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R8L75_C27_293490_20240129_MOBILE_GAME_IP_PIPELINE_NO_REORDER_MONETIZATION_BRIDGE","trigger_id":"TRG_R8L75_C27_293490_20240129_MOBILE_GAME_IP_PIPELINE_NO_REORDER_MONETIZATION_BRIDGE","symbol":"293490","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C27_CONTENT_IP_GLOBAL_MONETIZATION","raw_component_scores_before":{"IP_strength_score":11,"global_launch_score":7,"retention_monetization_score":1,"revenue_margin_score":1,"relative_strength_score":10,"theme_risk_penalty":8},"weighted_score_before":61,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"IP_strength_score":5,"global_launch_score":3,"retention_monetization_score":0,"revenue_margin_score":0,"relative_strength_score":4,"theme_risk_penalty":16},"weighted_score_after":39,"stage_label_after":"Stage1-Watch_or_4B-HighMAE","changed_components":["IP_strength_score","global_launch_score","retention_monetization_score","revenue_margin_score","relative_strength_score","theme_risk_penalty"],"component_delta_explanation":"C27 guard demotes game/content IP theme rows when global launch, user retention, monetization, revenue, margin and cashflow bridge are absent.","MFE_90D_pct":7.11,"MAE_90D_pct":-13.62,"score_return_alignment_label":"score_return_misaligned","current_profile_verdict":"current_profile_false_positive"}
```

### 20.5 shadow_weight rows

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,c27_requires_global_launch_retention_monetization_margin_bridge,canonical_archetype_specific,L8_PLATFORM_CONTENT_SW_SECURITY,C27_CONTENT_IP_GLOBAL_MONETIZATION,0,1,+1,"C27 content/IP global monetization rows should not promote toward Stage3-Yellow/Green unless IP signal converts into global launch visibility, user retention, MAU/ARPU or reorder monetization, platform distribution, revenue, margin, or cashflow bridge","263750 survives as guarded positive after global-launch/IP monetization bridge; 112040 and 293490 are demoted because game/IP theme MFE lacked durable user-retention and monetization bridge","TRG_R8L75_C27_263750_20240325_GAME_IP_GLOBAL_LAUNCH_MONETIZATION_BRIDGE|TRG_R8L75_C27_112040_20240311_BLOCKCHAIN_GAME_IP_THEME_NO_DURABLE_MONETIZATION|TRG_R8L75_C27_293490_20240129_MOBILE_GAME_IP_PIPELINE_NO_REORDER_MONETIZATION_BRIDGE",3,3,2,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,c27_content_ip_4b_high_mae_watch_guard,canonical_archetype_specific,L8_PLATFORM_CONTENT_SW_SECURITY,C27_CONTENT_IP_GLOBAL_MONETIZATION,1,1,0,"Content/IP winners and game-theme false starts can peak before launch, retention and monetization durability are confirmed; local/full-window 4B and high-MAE watch should remain active","preserves 263750 guarded positive while preventing 112040/293490 IP-theme false positives","TRG_R8L75_C27_263750_20240325_GAME_IP_GLOBAL_LAUNCH_MONETIZATION_BRIDGE|TRG_R8L75_C27_112040_20240311_BLOCKCHAIN_GAME_IP_THEME_NO_DURABLE_MONETIZATION|TRG_R8L75_C27_293490_20240129_MOBILE_GAME_IP_PIPELINE_NO_REORDER_MONETIZATION_BRIDGE",3,3,2,medium,existing_axis_kept,"strengthens local/full-window 4B and high-MAE watch without global delta"
```

### 20.6 residual_contribution row

```jsonl
{"row_type":"residual_contribution","round":"R8","loop":"75","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C27_CONTENT_IP_GLOBAL_MONETIZATION","new_independent_case_count":3,"reused_case_count":0,"new_symbol_count":3,"new_trigger_family_count":3,"tested_existing_calibrated_axes":["stage2_actionable_evidence_bonus","price_only_blowoff_blocks_positive_stage","full_4b_requires_non_price_evidence","local_4b_watch_guard","high_MAE_guardrail"],"residual_error_types_found":["game_IP_theme_without_retention_monetization_bridge","global_launch_IP_winner_needs_4B_watch","mobile_game_pipeline_low_MFE_high_MAE"],"loop_contribution_label":"canonical_archetype_rule_candidate","do_not_propose_new_weight_delta":false}
```

## 21. Deferred Coding Agent Handoff Prompt

### Purpose

You are now in the repository implementation phase. The attached Markdown files are v12 post-calibrated residual research outputs produced using the Songdaiki/stock-web OHLC atlas.

These MDs are not live candidate research. They are historical calibration research designed to extend the already-applied e2r_2_1_stock_web_calibrated profile.

Do not blindly apply every shadow row. Ingest the machine-readable rows and update the sector/canonical-archetype calibration ledger.

### R8-specific handling

- R8 maps to `L8_PLATFORM_CONTENT_SW_SECURITY`.
- This MD uses `C27_CONTENT_IP_GLOBAL_MONETIZATION`.
- Validate `round_schedule_status=valid` and `round_sector_consistency=pass` before accepting rows.

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
- price-only/content-IP-theme-only rows cannot promote Stage2/Stage3.
- If a v12 MD weakens an already applied axis, log it as residual counterexample rather than immediately reverting.
- Production scoring must not change unless the user explicitly asks for another promotion batch.

### Expected repository tasks

1. Parse case / trigger / score_simulation / shadow_weight / residual_contribution rows.
2. Validate stock-web price source fields.
3. Validate R8 direct L8 sector.
4. Validate canonical_archetype_id.
5. Validate novelty and reuse fields.
6. Deduplicate same_entry_group_id and reused cases.
7. Aggregate by large_sector_id and canonical_archetype_id.
8. Update sector_shadow_profile and archetype_shadow_profile only.
9. Preserve global calibrated profile unless explicitly promoted.
10. Report new independent cases, counterexamples, and residual error types.
11. Add tests that duplicate low-value loops cannot change weights.
12. Add validation that C27 content/IP global monetization rows cannot promote without global launch visibility, user retention, MAU/ARPU or reorder monetization, platform distribution, revenue conversion, margin conversion, FCF/cash conversion, or earnings revision tied to IP monetization.

### Expected output

- Concise implementation summary.
- Rows accepted/rejected.
- New sector/canonical archetype coverage.
- Existing axis strengthened/weakened/kept.
- No investment recommendation language.

## 22. Next Round State

```text
completed_round = R8
completed_loop = 75
next_round = R9
next_loop = 75
round_schedule_status = valid
round_sector_consistency = pass
```

## 23. Source Notes

```text
MAIN EXECUTION PROMPT:
docs/core/e2r_v12_prompt_round_scheduler_corrected.txt

NO-REPEAT INDEX:
docs/core/V12_Research_No_Repeat_Index.md

Stock-web:
atlas/manifest.json
atlas/schema.json
atlas/symbol_profiles/263/263750.json
atlas/symbol_profiles/112/112040.json
atlas/symbol_profiles/293/293490.json
atlas/ohlcv_tradable_by_symbol_year/263/263750/2024.csv
atlas/ohlcv_tradable_by_symbol_year/112/112040/2024.csv
atlas/ohlcv_tradable_by_symbol_year/293/293490/2024.csv
```

This loop continues loop 75 with R8 and adds 3 new independent C27 representative cases, 1 positive, 2 counterexamples/watch cases, and 1 canonical-archetype residual guard candidate for R8/L8.
