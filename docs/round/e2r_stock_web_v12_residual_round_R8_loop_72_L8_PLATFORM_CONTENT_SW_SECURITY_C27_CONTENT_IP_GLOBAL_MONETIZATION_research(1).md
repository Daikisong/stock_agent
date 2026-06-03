# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
scheduled_round: R8
scheduled_loop: 72
round_schedule_status: valid
round_sector_consistency: pass
computed_next_round: R9
computed_next_loop: 72
large_sector_id: L8_PLATFORM_CONTENT_SW_SECURITY
canonical_archetype_id: C27_CONTENT_IP_GLOBAL_MONETIZATION
fine_archetype_id: C27_GAME_CONTENT_LAUNCH_REVENUE_RETENTION_BRIDGE_GUARD
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

R8 maps to `L8_PLATFORM_CONTENT_SW_SECURITY`. The prior R8 loop used C28 software/security retention, so this run shifts to C27 content/IP global monetization. The residual is simple: content IP is a lighthouse only when the beam reaches monetization. Game launch, trailer, P2E, metaverse, or IP heat must turn into live-service revenue, retention, ranking durability, global distribution, or repeat monetization before Stage2 can climb toward Yellow/Green.

| layer | id | definition |
|---|---|---|
| round | R8 | platform / content / software / security |
| large_sector | L8_PLATFORM_CONTENT_SW_SECURITY | platform, content, game, software, security |
| canonical | C27_CONTENT_IP_GLOBAL_MONETIZATION | content IP, game launch, global monetization and hit-risk control |
| fine | C27_GAME_CONTENT_LAUNCH_REVENUE_RETENTION_BRIDGE_GUARD | launch/IP event must become revenue and retention |
| deep | ODIN_LAUNCH_RANKING_TO_REVENUE_RETENTION_CONVERSION | game launch monetization success |
| deep | TRAILER_REVEAL_PRICE_SPIKE_WITHOUT_LAUNCH_RETENTION_REVENUE | trailer/IP hype watch |
| deep | P2E_TOKEN_METAVERSE_OPTIONALITY_WITHOUT_DURABLE_GAME_MONETIZATION | P2E/metaverse theme high-MAE watch |

## 3. No-Repeat / Coverage Check

No-Repeat hard duplicate key:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

C27 top-covered symbols are `035900`, `194480`, `259960`, `352820`, `225570`, and `253450`. This run avoids that cluster and uses non-top-covered C27 game/content names.

| archetype | selected symbol | duplicate status | reason |
|---|---:|---|---|
| C27 | 293490 | new independent | not top-covered C27 symbol; game launch revenue/retention bridge positive |
| C27 | 263750 | new independent | not top-covered C27 symbol; trailer/IP hype without launch monetization bridge |
| C27 | 078340 | new independent | not top-covered C27 symbol; P2E/metaverse theme high-MAE watch |

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

## 6. Case Selection Summary

| role | symbol | company | trigger | entry | price | result |
|---|---:|---|---|---:|---:|---|
| structural_success_then_4B_watch | 293490 | 카카오게임즈 | Stage2-Actionable | 2021-06-29 | 59700 | launch-to-revenue monetization bridge worked |
| IP_hype_success_but_no_durable_monetization_bridge | 263750 | 펄어비스 | Stage2-Actionable | 2021-08-26 | 87900 | trailer/IP hype produced MFE but should remain 4B watch |
| theme_success_then_high_MAE_counterexample | 078340 | 컴투스 | Stage2-Actionable | 2021-10-18 | 111500 | P2E/metaverse theme produced high MFE then high-MAE drawdown |

## 7. Positive vs Counterexample Balance

```text
positive_case_count: 1
counterexample_count: 2
4B_case_count: 3
4C_or_high_MAE_watch_count: 2
calibration_usable_case_count: 3
current_profile_error_count: 2
```

## 8. Trigger-Level OHLC Backtest Table

| symbol | company | trigger | entry_date | entry_price | MFE30 | MFE90 | MFE180 | MAE30 | MAE90 | MAE180 | peak_date | peak_price | DD after peak |
|---:|---|---|---|---:|---:|---:|---:|---:|---:|---:|---|---:|---:|
| 293490 | 카카오게임즈 | Stage2-Actionable | 2021-06-29 | 59700 | 77.55 | 77.55 | 94.3 | -6.87 | -6.87 | -6.87 | 2021-11-17 | 116000 | -44.91 |
| 263750 | 펄어비스 | Stage2-Actionable | 2021-08-26 | 87900 | 16.04 | 65.19 | 65.19 | -17.97 | -17.97 | -17.97 | 2021-11-17 | 145200 | -37.53 |
| 078340 | 컴투스 | Stage2-Actionable | 2021-10-18 | 111500 | 64.39 | 64.39 | 64.39 | -9.87 | -9.87 | -41.7 | 2021-11-11 | 183300 | -64.54 |

## 9. Case-by-Case Notes

### 9.1 293490 / 카카오게임즈 — game launch to monetization bridge positive

The entry row is 2021-06-29 at 59,700. The first 30D window already reaches 106,000 and the wider path reaches 116,000. This is the C27 success condition: a game launch did not stay as a press-cycle event; it converted into revenue ranking, live-service monetization, and ranking durability. The path still needs 4B watch after the peak.

### 9.2 263750 / 펄어비스 — trailer/IP hype without monetization bridge

The entry row is 2021-08-26 at 87,900. The trailer/IP event produced large MFE, reaching 145,200 later, but the signal was not a launch-to-revenue bridge. This should not become Stage3-Green merely because the price path worked for a while. It is a 4B watch / Green false-positive counterexample.

### 9.3 078340 / 컴투스 — P2E/metaverse theme high-MAE watch

The entry row is 2021-10-18 at 111,500. The path reaches 183,300 quickly, then later falls to 65,000 within the broader window. This is the C27 theme trap: P2E and metaverse optionality can light the whole room for a month, but without durable retention/revenue conversion the wiring overheats.

## 10. Current Calibrated Profile Stress Test

| question | result |
|---|---|
| Stage2 actionable bonus too strong? | Yes when C27 treats trailer/IP/P2E theme price strength as enough evidence. |
| Stage3 Yellow threshold too loose? | Not globally; C27 needs launch-to-revenue, retention, or monetization bridge before Yellow. |
| Stage3 Green too strict? | Correct. No Green loosening. |
| Price-only blowoff guard appropriate? | Yes, especially for 263750 and 078340. |
| Full 4B non-price requirement appropriate? | Yes. 293490 has a better non-price bridge; 263750/078340 should remain watch/guard. |
| 4C timing issue? | High-MAE watch is useful after theme peaks; no immediate hard 4C promotion proposed. |

## 11. Stage2 / Yellow / Green Comparison

```text
293490:
  Stage2-Actionable = correct
  Stage3-Yellow = allowed after launch-to-revenue / retention bridge
  Stage3-Green = wait for stronger earnings durability and 4B check

263750:
  Stage2-Actionable = acceptable as watch
  Stage3-Yellow = reject without launch/retention/revenue bridge
  Stage3-Green = reject despite MFE because evidence is trailer/IP hype

078340:
  Stage2-Actionable = too generous if based only on P2E/metaverse price strength
  Stage3-Yellow = reject without durable game monetization bridge
  Stage3-Green = reject
```

## 12. 4B Local vs Full-window Timing Audit

| symbol | local_peak_proximity | full_window_peak_proximity | verdict |
|---:|---:|---:|---|
| 293490 | 0.91 | 1.00 | good full-window 4B watch after launch monetization bridge |
| 263750 | 0.88 | 1.00 | large MFE but IP-hype 4B watch, not Green |
| 078340 | 1.00 | 1.00 | price/theme local 4B watch, not positive stage |

## 13. Canonical-Archetype Rule Candidate

```text
canonical_archetype_rule_candidate: true
rule_scope: canonical_archetype_specific
rule_id: c27_requires_launch_revenue_retention_monetization_bridge

rule:
  For C27 content/game/IP rows, do not promote game launch, trailer, content IP,
  P2E, or metaverse theme Stage2 signals into Stage3-Yellow/Green unless at least one
  non-price bridge is visible:
  launch-to-revenue conversion, ranking durability, retention, live-service monetization,
  global distribution, repeat IP monetization, margin leverage, or earnings revision.
```

## 14. Before / After Backtest Comparison

| profile | eligible triggers | avg MFE90 | avg MAE90 | Green false-positive rate | verdict |
|---|---:|---:|---:|---:|---|
| P0 e2r_2_1_stock_web_calibrated_proxy | 3 | 69.04 | -11.57 | 66.7% | price path can look good, but Green would over-credit hype |
| P0b e2r_2_0_baseline_reference | 3 | 69.04 | -11.57 | 33.3% | safer but may miss 293490 launch bridge |
| P1 sector_specific_candidate_profile | 3 | 69.04 | -11.57 | 66.7% | no broad L8 loosen |
| P2 canonical_archetype_candidate_profile | 1 selected positive | 77.55 | -6.87 | 0% after bridge gate | preferred shadow |
| P3 counterexample_guard_profile | 2 watch/rejected | 64.79 | -13.92 | 0% after no-Green routing | useful guard |

## 15. Score-Return Alignment Matrix

| case | current profile verdict | alignment |
|---|---|---|
| 293490 | current_profile_correct | launch monetization bridge aligned with strong MFE |
| 263750 | current_profile_partially_false_positive | MFE existed, but Green would over-credit trailer/IP hype |
| 078340 | current_profile_false_positive_if_green | theme produced high MFE but also deep high-MAE drawdown |

## 16. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive | counterexample | 4B | 4C/watch | new_independent | reused | usable_triggers | representative | profile_errors | sector_rule | canonical_rule | coverage_gap_after |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| L8_PLATFORM_CONTENT_SW_SECURITY | C27_CONTENT_IP_GLOBAL_MONETIZATION | C27_GAME_CONTENT_LAUNCH_REVENUE_RETENTION_BRIDGE_GUARD | 1 | 2 | 3 | 2 | 3 | 0 | 3 | 3 | 2 | false | true | C27 non-top-covered game/content monetization residual reduced |

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
- game trailer/IP hype without monetization bridge
- P2E/metaverse theme without retention/revenue bridge
- game launch success still needs 4B watch
new_axis_proposed: null
existing_axis_strengthened:
- stage2_required_bridge
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
- round/sector/canonical consistency
- duplicate avoidance at symbol level
```

Not validated:

```text
- exact disclosure URLs
- exact report URLs
- production scoring behavior
- live candidate status
```

## 19. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,c27_requires_launch_revenue_retention_monetization_bridge,canonical_archetype_specific,L8_PLATFORM_CONTENT_SW_SECURITY,C27_CONTENT_IP_GLOBAL_MONETIZATION,0,1,+1,"C27 content/game/IP rows should not promote toward Stage3-Yellow/Green unless launch, IP, trailer, or theme signal converts into revenue ranking, retention, live-service monetization, global distribution, or repeat monetization bridge","293490 survives with strong MFE after launch-to-revenue bridge; 263750 and 078340 show large MFE but remain 4B/watch because monetization durability was not confirmed","TRG_R8L72_C27_293490_20210629_GAME_LAUNCH_MONETIZATION_BRIDGE|TRG_R8L72_C27_263750_20210826_TRAILER_IP_HYPE_NO_MONETIZATION_BRIDGE|TRG_R8L72_C27_078340_20211018_P2E_METAVERSE_THEME_HIGH_MAE",3,3,2,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,c27_content_theme_4b_high_mae_watch_guard,canonical_archetype_specific,L8_PLATFORM_CONTENT_SW_SECURITY,C27_CONTENT_IP_GLOBAL_MONETIZATION,1,1,0,"Game/content/IP winners and theme failures can peak quickly; local/full-window 4B and high-MAE watch must stay active after MFE","prevents 263750 and 078340 from Green routing while preserving 293490 positive","TRG_R8L72_C27_293490_20210629_GAME_LAUNCH_MONETIZATION_BRIDGE|TRG_R8L72_C27_263750_20210826_TRAILER_IP_HYPE_NO_MONETIZATION_BRIDGE|TRG_R8L72_C27_078340_20211018_P2E_METAVERSE_THEME_HIGH_MAE",3,3,2,medium,existing_axis_kept,"strengthens local 4B/high-MAE watch without global delta"
```

## 20. Machine-Readable Rows

### 20.1 price_source_validation

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","source_name":"FinanceData/marcap","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
```

### 20.2 case rows

```jsonl
{"row_type":"case","case_id":"R8L72_C27_293490_20210629_GAME_LAUNCH_MONETIZATION_BRIDGE","symbol":"293490","company_name":"카카오게임즈","round":"R8","loop":"72","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C27_CONTENT_IP_GLOBAL_MONETIZATION","fine_archetype_id":"C27_GAME_LAUNCH_LIVE_SERVICE_MONETIZATION_BRIDGE","deep_sub_archetype_id":"ODIN_LAUNCH_RANKING_TO_REVENUE_RETENTION_CONVERSION","case_type":"structural_success_then_4B_watch","positive_or_counterexample":"positive","best_trigger":"Stage2-Actionable","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"score_return_aligned","current_profile_verdict":"current_profile_correct","price_source":"Songdaiki/stock-web","notes":"C27 content/game/IP rows require launch-to-revenue, retention, live-service, or repeat monetization bridge; trailer/theme price strength alone is insufficient."}
{"row_type":"case","case_id":"R8L72_C27_263750_20210826_TRAILER_IP_HYPE_NO_MONETIZATION_BRIDGE","symbol":"263750","company_name":"펄어비스","round":"R8","loop":"72","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C27_CONTENT_IP_GLOBAL_MONETIZATION","fine_archetype_id":"C27_GAME_TRAILER_IP_HYPE_WITHOUT_MONETIZATION_BRIDGE","deep_sub_archetype_id":"TRAILER_REVEAL_PRICE_SPIKE_WITHOUT_LAUNCH_RETENTION_REVENUE","case_type":"IP_hype_success_but_no_durable_monetization_bridge","positive_or_counterexample":"counterexample","best_trigger":"Stage2-Actionable","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"score_return_mixed","current_profile_verdict":"current_profile_partially_false_positive","price_source":"Songdaiki/stock-web","notes":"C27 content/game/IP rows require launch-to-revenue, retention, live-service, or repeat monetization bridge; trailer/theme price strength alone is insufficient."}
{"row_type":"case","case_id":"R8L72_C27_078340_20211018_P2E_METAVERSE_THEME_HIGH_MAE","symbol":"078340","company_name":"컴투스","round":"R8","loop":"72","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C27_CONTENT_IP_GLOBAL_MONETIZATION","fine_archetype_id":"C27_P2E_METAVERSE_THEME_WITHOUT_RETENTION_REVENUE_BRIDGE","deep_sub_archetype_id":"P2E_TOKEN_METAVERSE_OPTIONALITY_WITHOUT_DURABLE_GAME_MONETIZATION","case_type":"theme_success_then_high_MAE_counterexample","positive_or_counterexample":"counterexample","best_trigger":"Stage2-Actionable","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"score_return_mixed","current_profile_verdict":"current_profile_false_positive_if_green","price_source":"Songdaiki/stock-web","notes":"C27 content/game/IP rows require launch-to-revenue, retention, live-service, or repeat monetization bridge; trailer/theme price strength alone is insufficient."}
```

### 20.3 trigger rows

```jsonl
{"row_type":"trigger","trigger_id":"TRG_R8L72_C27_293490_20210629_GAME_LAUNCH_MONETIZATION_BRIDGE","case_id":"R8L72_C27_293490_20210629_GAME_LAUNCH_MONETIZATION_BRIDGE","symbol":"293490","company_name":"카카오게임즈","round":"R8","loop":"72","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C27_CONTENT_IP_GLOBAL_MONETIZATION","fine_archetype_id":"C27_GAME_LAUNCH_LIVE_SERVICE_MONETIZATION_BRIDGE","deep_sub_archetype_id":"ODIN_LAUNCH_RANKING_TO_REVENUE_RETENTION_CONVERSION","loop_objective":"coverage_gap_fill|counterexample_mining|stage2_actionable_bonus_stress_test|4B_non_price_requirement_stress_test|canonical_archetype_compression","trigger_type":"Stage2-Actionable","trigger_date":"2021-06-29","entry_date":"2021-06-29","entry_price":59700,"evidence_available_at_that_date":"source_proxy_game_launch_revenue_ranking_and_live_service_monetization_bridge; evidence_url_pending","evidence_source":"source_proxy_game_launch_revenue_ranking_and_live_service_monetization_bridge; evidence_url_pending","bridge_summary":"game launch ranking converted into monetization/retention and repeated revenue optionality rather than remaining only a launch headline","stage2_evidence_fields":["game_launch_signal","revenue_ranking_proxy","relative_strength","live_service_monetization_bridge"],"stage3_evidence_fields":["launch_to_revenue_conversion","retention_or_ranking_durability","earnings_revision_proxy"],"stage4b_evidence_fields":["post_MFE_peak_watch","game_launch_crowding"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/293/293490/2021.csv|atlas/ohlcv_tradable_by_symbol_year/293/293490/2022.csv","profile_path":"atlas/symbol_profiles/293/293490.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":77.55,"MFE_90D_pct":77.55,"MFE_180D_pct":94.3,"MFE_1Y_pct":94.3,"MFE_2Y_pct":94.3,"MAE_30D_pct":-6.87,"MAE_90D_pct":-6.87,"MAE_180D_pct":-6.87,"MAE_1Y_pct":-6.87,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2021-11-17","peak_price":116000,"drawdown_after_peak_pct":-44.91,"green_lateness_ratio":"0.36","four_b_local_peak_proximity":0.91,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"good_full_window_4B_watch_after_launch_monetization_bridge","four_b_evidence_type":"non_price_launch_revenue_bridge","four_c_protection_label":"none","trigger_outcome_label":"structural_success_then_4B_watch","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R8L72_C27_293490_20210629_GAME_LAUNCH_MONETIZATION_BRIDGE_entry","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"TRG_R8L72_C27_263750_20210826_TRAILER_IP_HYPE_NO_MONETIZATION_BRIDGE","case_id":"R8L72_C27_263750_20210826_TRAILER_IP_HYPE_NO_MONETIZATION_BRIDGE","symbol":"263750","company_name":"펄어비스","round":"R8","loop":"72","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C27_CONTENT_IP_GLOBAL_MONETIZATION","fine_archetype_id":"C27_GAME_TRAILER_IP_HYPE_WITHOUT_MONETIZATION_BRIDGE","deep_sub_archetype_id":"TRAILER_REVEAL_PRICE_SPIKE_WITHOUT_LAUNCH_RETENTION_REVENUE","loop_objective":"coverage_gap_fill|counterexample_mining|stage2_actionable_bonus_stress_test|4B_non_price_requirement_stress_test|canonical_archetype_compression","trigger_type":"Stage2-Actionable","trigger_date":"2021-08-26","entry_date":"2021-08-26","entry_price":87900,"evidence_available_at_that_date":"source_proxy_game_trailer_IP_reveal_without_launch_retention_or_revenue_bridge; evidence_url_pending","evidence_source":"source_proxy_game_trailer_IP_reveal_without_launch_retention_or_revenue_bridge; evidence_url_pending","bridge_summary":"trailer/IP reveal created large MFE, but launch timing, retention, and revenue conversion were absent; should route to 4B watch, not Green","stage2_evidence_fields":["game_trailer_IP_reveal","price_spike","relative_strength"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["price_IP_hype_local_peak","launch_delay_or_monetization_uncertainty"],"stage4c_evidence_fields":["monetization_bridge_absent_watch"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/263/263750/2021.csv|atlas/ohlcv_tradable_by_symbol_year/263/263750/2022.csv","profile_path":"atlas/symbol_profiles/263/263750.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":16.04,"MFE_90D_pct":65.19,"MFE_180D_pct":65.19,"MFE_1Y_pct":65.19,"MFE_2Y_pct":65.19,"MAE_30D_pct":-17.97,"MAE_90D_pct":-17.97,"MAE_180D_pct":-17.97,"MAE_1Y_pct":-17.97,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2021-11-17","peak_price":145200,"drawdown_after_peak_pct":-37.53,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":0.88,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"large_MFE_but_IP_hype_4B_watch_not_green","four_b_evidence_type":"price_theme_IP_hype_without_monetization_bridge","four_c_protection_label":"bridge_absent_watch","trigger_outcome_label":"hype_success_but_green_false_positive_counterexample","current_profile_verdict":"current_profile_partially_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R8L72_C27_263750_20210826_TRAILER_IP_HYPE_NO_MONETIZATION_BRIDGE_entry","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"TRG_R8L72_C27_078340_20211018_P2E_METAVERSE_THEME_HIGH_MAE","case_id":"R8L72_C27_078340_20211018_P2E_METAVERSE_THEME_HIGH_MAE","symbol":"078340","company_name":"컴투스","round":"R8","loop":"72","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C27_CONTENT_IP_GLOBAL_MONETIZATION","fine_archetype_id":"C27_P2E_METAVERSE_THEME_WITHOUT_RETENTION_REVENUE_BRIDGE","deep_sub_archetype_id":"P2E_TOKEN_METAVERSE_OPTIONALITY_WITHOUT_DURABLE_GAME_MONETIZATION","loop_objective":"coverage_gap_fill|counterexample_mining|stage2_actionable_bonus_stress_test|4B_non_price_requirement_stress_test|canonical_archetype_compression","trigger_type":"Stage2-Actionable","trigger_date":"2021-10-18","entry_date":"2021-10-18","entry_price":111500,"evidence_available_at_that_date":"source_proxy_P2E_metaverse_theme_without_durable_retention_or_revenue_bridge; evidence_url_pending","evidence_source":"source_proxy_P2E_metaverse_theme_without_durable_retention_or_revenue_bridge; evidence_url_pending","bridge_summary":"P2E/metaverse optionality created a strong short-run peak but lacked durable game retention, revenue, or margin conversion and produced large drawdown","stage2_evidence_fields":["P2E_metaverse_theme","price_spike","relative_strength"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["price_theme_local_peak","token_or_metaverse_crowding","weak_monetization_bridge"],"stage4c_evidence_fields":["high_MAE_without_retention_revenue_bridge"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/078/078340/2021.csv|atlas/ohlcv_tradable_by_symbol_year/078/078340/2022.csv","profile_path":"atlas/symbol_profiles/078/078340.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":64.39,"MFE_90D_pct":64.39,"MFE_180D_pct":64.39,"MFE_1Y_pct":64.39,"MFE_2Y_pct":64.39,"MAE_30D_pct":-9.87,"MAE_90D_pct":-9.87,"MAE_180D_pct":-41.7,"MAE_1Y_pct":-41.7,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2021-11-11","peak_price":183300,"drawdown_after_peak_pct":-64.54,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"price_theme_local_4B_watch_not_positive_stage","four_b_evidence_type":"price_theme_IP_hype_without_monetization_bridge","four_c_protection_label":"high_MAE_watch","trigger_outcome_label":"theme_success_then_high_MAE_counterexample","current_profile_verdict":"current_profile_false_positive_if_green","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R8L72_C27_078340_20211018_P2E_METAVERSE_THEME_HIGH_MAE_entry","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
```

### 20.4 score_simulation rows

```jsonl
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R8L72_C27_293490_20210629_GAME_LAUNCH_MONETIZATION_BRIDGE","trigger_id":"TRG_R8L72_C27_293490_20210629_GAME_LAUNCH_MONETIZATION_BRIDGE","symbol":"293490","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C27_CONTENT_IP_GLOBAL_MONETIZATION","raw_component_scores_before":{"content_IP_score":10,"launch_monetization_score":12,"retention_revenue_score":12,"global_distribution_score":8,"relative_strength_score":10,"event_hype_risk_penalty":4},"weighted_score_before":74,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"content_IP_score":10,"launch_monetization_score":16,"retention_revenue_score":15,"global_distribution_score":9,"relative_strength_score":8,"event_hype_risk_penalty":4},"weighted_score_after":82,"stage_label_after":"Stage3-Yellow","changed_components":["content_IP_score","launch_monetization_score","retention_revenue_score","relative_strength_score","event_hype_risk_penalty"],"component_delta_explanation":"C27 row is promoted only because launch/IP event converts into live-service revenue, ranking durability, and monetization bridge.","MFE_90D_pct":77.55,"MAE_90D_pct":-6.87,"score_return_alignment_label":"score_return_aligned","current_profile_verdict":"current_profile_correct"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R8L72_C27_263750_20210826_TRAILER_IP_HYPE_NO_MONETIZATION_BRIDGE","trigger_id":"TRG_R8L72_C27_263750_20210826_TRAILER_IP_HYPE_NO_MONETIZATION_BRIDGE","symbol":"263750","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C27_CONTENT_IP_GLOBAL_MONETIZATION","raw_component_scores_before":{"content_IP_score":12,"launch_monetization_score":2,"retention_revenue_score":1,"global_distribution_score":5,"relative_strength_score":12,"event_hype_risk_penalty":7},"weighted_score_before":63,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"content_IP_score":6,"launch_monetization_score":0,"retention_revenue_score":0,"global_distribution_score":2,"relative_strength_score":5,"event_hype_risk_penalty":14},"weighted_score_after":42,"stage_label_after":"Stage1-Watch_or_4B-Watch","changed_components":["content_IP_score","launch_monetization_score","retention_revenue_score","relative_strength_score","event_hype_risk_penalty"],"component_delta_explanation":"C27 guard demotes trailer/P2E/metaverse/theme rows when retention, launch revenue, or monetization bridge is absent.","MFE_90D_pct":65.19,"MAE_90D_pct":-17.97,"score_return_alignment_label":"score_return_mixed","current_profile_verdict":"current_profile_partially_false_positive"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R8L72_C27_078340_20211018_P2E_METAVERSE_THEME_HIGH_MAE","trigger_id":"TRG_R8L72_C27_078340_20211018_P2E_METAVERSE_THEME_HIGH_MAE","symbol":"078340","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C27_CONTENT_IP_GLOBAL_MONETIZATION","raw_component_scores_before":{"content_IP_score":12,"launch_monetization_score":2,"retention_revenue_score":1,"global_distribution_score":5,"relative_strength_score":12,"event_hype_risk_penalty":7},"weighted_score_before":63,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"content_IP_score":6,"launch_monetization_score":0,"retention_revenue_score":0,"global_distribution_score":2,"relative_strength_score":5,"event_hype_risk_penalty":14},"weighted_score_after":42,"stage_label_after":"Stage1-Watch_or_4B-Watch","changed_components":["content_IP_score","launch_monetization_score","retention_revenue_score","relative_strength_score","event_hype_risk_penalty"],"component_delta_explanation":"C27 guard demotes trailer/P2E/metaverse/theme rows when retention, launch revenue, or monetization bridge is absent.","MFE_90D_pct":64.39,"MAE_90D_pct":-9.87,"score_return_alignment_label":"score_return_mixed","current_profile_verdict":"current_profile_false_positive_if_green"}
```

### 20.5 shadow_weight rows

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,c27_requires_launch_revenue_retention_monetization_bridge,canonical_archetype_specific,L8_PLATFORM_CONTENT_SW_SECURITY,C27_CONTENT_IP_GLOBAL_MONETIZATION,0,1,+1,"C27 content/game/IP rows should not promote toward Stage3-Yellow/Green unless launch, IP, trailer, or theme signal converts into revenue ranking, retention, live-service monetization, global distribution, or repeat monetization bridge","293490 survives with strong MFE after launch-to-revenue bridge; 263750 and 078340 show large MFE but remain 4B/watch because monetization durability was not confirmed","TRG_R8L72_C27_293490_20210629_GAME_LAUNCH_MONETIZATION_BRIDGE|TRG_R8L72_C27_263750_20210826_TRAILER_IP_HYPE_NO_MONETIZATION_BRIDGE|TRG_R8L72_C27_078340_20211018_P2E_METAVERSE_THEME_HIGH_MAE",3,3,2,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,c27_content_theme_4b_high_mae_watch_guard,canonical_archetype_specific,L8_PLATFORM_CONTENT_SW_SECURITY,C27_CONTENT_IP_GLOBAL_MONETIZATION,1,1,0,"Game/content/IP winners and theme failures can peak quickly; local/full-window 4B and high-MAE watch must stay active after MFE","prevents 263750 and 078340 from Green routing while preserving 293490 positive","TRG_R8L72_C27_293490_20210629_GAME_LAUNCH_MONETIZATION_BRIDGE|TRG_R8L72_C27_263750_20210826_TRAILER_IP_HYPE_NO_MONETIZATION_BRIDGE|TRG_R8L72_C27_078340_20211018_P2E_METAVERSE_THEME_HIGH_MAE",3,3,2,medium,existing_axis_kept,"strengthens local 4B/high-MAE watch without global delta"
```

### 20.6 residual_contribution row

```jsonl
{"row_type":"residual_contribution","round":"R8","loop":"72","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C27_CONTENT_IP_GLOBAL_MONETIZATION","new_independent_case_count":3,"reused_case_count":0,"new_symbol_count":3,"new_trigger_family_count":3,"tested_existing_calibrated_axes":["stage2_actionable_evidence_bonus","price_only_blowoff_blocks_positive_stage","full_4b_requires_non_price_evidence","local_4b_watch_guard","high_MAE_guardrail"],"residual_error_types_found":["game_trailer_IP_hype_without_monetization_bridge","P2E_metaverse_theme_without_retention_revenue_bridge","game_launch_success_still_needs_4B_watch"],"loop_contribution_label":"canonical_archetype_rule_candidate","do_not_propose_new_weight_delta":false}
```

## 21. Deferred Coding Agent Handoff Prompt

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

### Expected output

- Concise implementation summary.
- Rows accepted/rejected.
- New sector/canonical archetype coverage.
- Existing axis strengthened/weakened/kept.
- No investment recommendation language.

## 22. Next Round State

```text
completed_round = R8
completed_loop = 72
next_round = R9
next_loop = 72
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
atlas/symbol_profiles/293/293490.json
atlas/symbol_profiles/263/263750.json
atlas/symbol_profiles/078/078340.json
atlas/ohlcv_tradable_by_symbol_year/293/293490/2021.csv
atlas/ohlcv_tradable_by_symbol_year/293/293490/2022.csv
atlas/ohlcv_tradable_by_symbol_year/263/263750/2021.csv
atlas/ohlcv_tradable_by_symbol_year/263/263750/2022.csv
atlas/ohlcv_tradable_by_symbol_year/078/078340/2021.csv
atlas/ohlcv_tradable_by_symbol_year/078/078340/2022.csv
```

This loop adds 3 new independent C27 cases, 1 positive, 2 counterexamples/watch cases, and 1 canonical-archetype residual guard candidate for R8/L8.
