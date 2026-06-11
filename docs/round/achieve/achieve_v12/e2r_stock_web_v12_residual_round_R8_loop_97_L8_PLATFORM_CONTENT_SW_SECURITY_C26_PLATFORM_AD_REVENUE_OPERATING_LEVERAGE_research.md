# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
output_file = e2r_stock_web_v12_residual_round_R8_loop_97_L8_PLATFORM_CONTENT_SW_SECURITY_C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE_research.md
selected_round = R8
selected_loop = 97
selection_basis = docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket = Priority 0
round_schedule_status = coverage_index_selected
round_sector_consistency = pass
large_sector_id = L8_PLATFORM_CONTENT_SW_SECURITY
canonical_archetype_id = C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE
fine_archetype_id = PLATFORM_AD_TRAFFIC_MONETIZATION_OPERATING_LEVERAGE_BRIDGE_VS_AD_RECOVERY_LABEL_FALSE_POSITIVE
loop_objective = coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | canonical_archetype_compression | sector_specific_rule_discovery
```

This loop follows the v12 coverage-index scheduler. C26 had only 3 representative rows in the no-repeat ledger, with no positive/counterexample balance and only one 4B case. The selected scope remains R8/L8 because C26 maps directly to platform/content/software/security.

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

```text
selected_round = R8
large_sector_id = L8_PLATFORM_CONTENT_SW_SECURITY
canonical_archetype_id = C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE
```

C26 is not simply "internet platform went up." It is the narrower bridge where traffic, ad inventory, ARPU, take-rate, and cost base convert into operating leverage. The same word "ad recovery" can be a strong bridge in a platform and an empty label in an ad-rep or portal with margin/regulatory drag.

## 3. Previous Coverage / Duplicate Avoidance Check

Known top covered C26 symbols in the no-repeat index are `035420`, `042000`, and `237820`. This loop avoids those and selects three new symbols:

```text
067160 SOOP
035720 Kakao
089600 KT Nasmedia
```

Duplicate check:

```text
hard_duplicate = false
same_symbol_same_trigger_entry = false
same_archetype_new_symbol_count = 3
same_archetype_new_trigger_family_count = 3
```

## 4. Stock-Web OHLC Input / Price Source Validation

```text
price_data_source = Songdaiki/stock-web
price_data_repo = https://github.com/Songdaiki/stock-web
manifest_path = atlas/manifest.json
stock_web_manifest_max_date = 2026-02-20
price_basis = tradable_raw
price_adjustment_status = raw_unadjusted_marcap
calibration_shard_root = atlas/ohlcv_tradable_by_symbol_year
```

All three symbol profiles have 180D windows available after the selected entry dates. Corporate-action candidates do not overlap the selected 180D windows.

## 5. Historical Eligibility Gate

| symbol | profile_path | selected entry | forward 180D available | corporate action window |
|---|---|---:|---|---|
| 067160 | atlas/symbol_profiles/067/067160.json | 2024-06-20 | true | clean_180D_window |
| 035720 | atlas/symbol_profiles/035/035720.json | 2024-05-09 | true | clean_180D_window |
| 089600 | atlas/symbol_profiles/089/089600.json | 2024-05-09 | true | clean_180D_window |

## 6. Canonical Archetype Compression Map

| canonical | fine/deep sub-archetype | compression rule |
|---|---|---|
| C26 | LIVE_STREAMING_PLATFORM_MIGRATION_GLOBAL_SOOP_REBRAND_USER_TRAFFIC_OPERATING_LEVERAGE | Traffic migration is Stage2-Actionable only if monetization and cost leverage are visible. |
| C26 | TALK_BIZ_AD_RECOVERY_WITHOUT_MARGIN_REVISION_AND_REGULATORY_TRUST_BRIDGE | Ad recovery vocabulary without margin/revision/trust bridge is weak-watch, not Green. |
| C26 | AD_REP_DIGITAL_AD_RECOVERY_LABEL_WITHOUT_PLATFORM_TAKE_RATE_OR_OP_LEVERAGE | Ad agency or ad-rep cyclicality should not inherit platform operating leverage weight. |

## 7. Case Selection Summary

| symbol | company | role | trigger date | entry price | 30D MFE/MAE | 90D MFE/MAE | 180D MFE/MAE | current profile verdict |
|---|---|---|---:|---:|---:|---:|---:|---|
| 067160 | SOOP | high_mae_success | 2024-06-20 | 117000 | 22.91 / -17.86 | 22.91 / -26.07 | 22.91 / -32.82 | current_profile_4B_too_late |
| 035720 | 카카오 | failed_rerating | 2024-05-09 | 48600 | 4.12 / -13.48 | 4.12 / -32.3 | 4.12 / -33.02 | current_profile_false_positive |
| 089600 | KT나스미디어 | failed_rerating | 2024-05-09 | 18800 | 1.06 / -12.87 | 1.06 / -19.15 | 1.06 / -28.09 | current_profile_false_positive |

## 8. Positive vs Counterexample Balance

```text
positive_case_count = 1
counterexample_count = 2
calibration_usable_case_count = 3
new_independent_case_count = 3
```

SOOP is a positive/high-MAE case: the platform migration/rebrand produced a real local MFE, but the drawdown shows that C26 needs a 4B watch once the move becomes local-peak/price-only. Kakao and KT Nasmedia are counterexamples: ad-recovery wording without operating leverage did not protect price path.

## 9. Evidence Source Map

| symbol | evidence source | bridge quality | source quality |
|---|---|---|---|
| 067160 | SOOP/AfreecaTV rebrand/global launch and Twitch Korea exit event | traffic migration + platform optionality, but 180D drawdown requires 4B watch | source_proxy_only |
| 035720 | Kakao quarterly earnings / Talk Biz advertising proxy | ad recovery wording but weak margin/trust bridge | source_proxy_only |
| 089600 | Nasmedia quarterly earnings / ad market recovery proxy | ad-rep recovery label without platform take-rate | source_proxy_only |

## 10. Price Data Source Map

| symbol | price shard | profile |
|---|---|---|
| 067160 | atlas/ohlcv_tradable_by_symbol_year/067/067160/2024.csv; 2025.csv | atlas/symbol_profiles/067/067160.json |
| 035720 | atlas/ohlcv_tradable_by_symbol_year/035/035720/2024.csv; 2025.csv | atlas/symbol_profiles/035/035720.json |
| 089600 | atlas/ohlcv_tradable_by_symbol_year/089/089600/2024.csv; 2025.csv | atlas/symbol_profiles/089/089600.json |

## 11. Case-by-Case Trigger Grid

| case_id | trigger_type | trigger_outcome_label | representative |
|---|---|---|---|
| C26_R8_L97_067160_SOOP_GLOBAL_PLATFORM_MIGRATION | Stage2-Actionable | platform_migration_positive_but_high_mae_after_local_peak | true |
| C26_R8_L97_035720_KAKAO_TALKBIZ_AD_RECOVERY_LABEL | Stage2-Actionable | ad_recovery_label_false_positive_without_operating_leverage | true |
| C26_R8_L97_089600_NASMEDIA_DIGITAL_AD_RECOVERY_LABEL | Stage2-Actionable | ad_rep_recovery_label_false_positive | true |

## 12. Trigger-Level OHLC Backtest Tables

MFE/MAE formula:

```text
MFE_N_pct = (max(high from entry_date through N trading days) / entry_price - 1) * 100
MAE_N_pct = (min(low from entry_date through N trading days) / entry_price - 1) * 100
```

The three rows carry explicit 30D/90D/180D MFE and MAE fields in both the table and JSONL.

## 13. Current Calibrated Profile Stress Test

| symbol | P0 verdict | actual path | residual error |
|---|---|---|---|
| 067160 | Stage2-Actionable was useful, but 4B watch was too late | +22.91% MFE then -32.82% 180D MAE | high_MAE_after_local_peak |
| 035720 | Stage2-Actionable too generous | +4.12% MFE / -33.02% MAE | false_positive |
| 089600 | Stage2-Actionable too generous | +1.06% MFE / -28.09% MAE | false_positive |

## 14. Stage2 / Yellow / Green Comparison

No confirmed Stage3-Yellow or Stage3-Green trigger is promoted in this loop. The result argues for C26 Stage2 bridge quality rather than Green looseness.

```text
green_lateness_ratio = not_applicable
reason = no_confirmed_Stage3_Green_trigger
```

## 15. 4B Local vs Full-window Timing Audit

SOOP demonstrates the useful 4B lesson in C26. A traffic migration can produce a local MFE quickly, but if monetization evidence is not durable, price-only local peak should become watch rather than full Green extension.

```text
067160 local_peak_price = 143800
067160 entry_price = 117000
067160 180D low_after_peak = 78600
drawdown_after_peak_pct = -45.34
four_b_timing_verdict = price_only_local_4B_too_early / full 4B requires non-price evidence
```

## 16. 4C Protection Audit

No hard 4C confirmation is proposed. Kakao gets `thesis_break_watch_only` because trust/regulatory drag weakened the ad recovery thesis, but this loop is not a hard 4C study.

## 17. Sector-Specific Rule Candidate

```text
sector_specific_rule_candidate = false
```

The sample is one canonical archetype, not enough to change all L8 platform/software/content scoring.

## 18. Canonical-Archetype Rule Candidate

```text
canonical_archetype_rule_candidate = true
rule_scope = canonical_archetype_specific
candidate = C26_stage2_required_monetization_bridge
```

Proposed C26 bridge:

```text
C26 Stage2-Actionable requires at least two of:
- traffic/user migration or durable inventory expansion
- ARPU/take-rate/ad-fill evidence
- OPM or contribution-margin expansion
- paid conversion or commerce/ads monetization
- cost base operating leverage
```

Counter-guard:

```text
If evidence is only "ad market recovery" or "traffic headline" without monetization and margin bridge:
    route to Stage1/weak-watch
    do_not_apply_stage2_actionable_bonus = true
```

## 19. Before / After Backtest Comparison

| profile | eligible triggers | avg MFE90 | avg MAE90 | verdict |
|---|---:|---:|---:|---|
| P0 e2r_2_1_stock_web_calibrated_proxy | 3 | 9.36 | -25.17 | too permissive for ad-recovery labels |
| P2 C26 monetization bridge guard | 3 | 22.91 on accepted positive only | -26.07 on accepted positive | better precision but still needs 4B watch |
| P3 counterexample guard | 2 rejected weak-bridge cases | 2.59 | -25.73 | avoids low-MFE/high-MAE false positives |

## 20. Score-Return Alignment Matrix

| symbol | weighted_score_before | stage_before | weighted_score_after | stage_after | score_return_alignment |
|---|---:|---|---:|---|---|
| 067160 | 72 | Stage2-Actionable | 70 | Stage2-Actionable+4B-watch | positive_but_high_drawdown |
| 035720 | 68 | Stage2-Actionable | 61 | Stage1/weak-watch | false_positive_reduced |
| 089600 | 66 | Stage2-Actionable | 58 | Stage1/weak-watch | false_positive_reduced |

## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive_case_count | counterexample_count | 4B_case_count | 4C_case_count | new_independent_case_count | reused_case_count | calibration_usable_trigger_count | representative_trigger_count | current_profile_error_count | sector_rule_candidate | canonical_rule_candidate | coverage_gap_after_this_loop |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| L8_PLATFORM_CONTENT_SW_SECURITY | C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE | PLATFORM_AD_TRAFFIC_MONETIZATION_OPERATING_LEVERAGE_BRIDGE_VS_AD_RECOVERY_LABEL_FALSE_POSITIVE | 1 | 2 | 0 | 0 | 3 | 0 | 3 | 3 | 3 | false | true | C26 moves from 3 to synthetic 6 if accepted; still Priority 0 |

## 22. Residual Contribution Summary

```text
new_independent_case_count: 3
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 3
new_canonical_archetype_count: 0
new_fine_archetype_count: 3
new_trigger_family_count: 3
tested_existing_calibrated_axes:
  - stage2_actionable_evidence_bonus
  - price_only_blowoff_blocks_positive_stage
  - full_4b_requires_non_price_evidence
residual_error_types_found:
  - ad_recovery_label_false_positive
  - traffic_migration_high_MAE_after_local_peak
  - missing_operating_leverage_bridge
new_axis_proposed: null
existing_axis_strengthened:
  - C26_stage2_required_bridge
  - C26_local_4b_watch_guard
existing_axis_weakened: null
existing_axis_kept:
  - Stage3-Green strictness
sector_specific_rule_candidate: false
canonical_archetype_rule_candidate: true
no_new_signal_reason: null

loop_contribution_label: canonical_archetype_rule_candidate
do_not_propose_new_weight_delta: false
```

This loop adds 3 new independent cases, 2 counterexamples, and 3 residual errors for R8/L8_PLATFORM_CONTENT_SW_SECURITY/C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE.

## 23. Validation Scope / Non-Validation Scope

Validation scope:

```text
- stock-web OHLC path validation
- clean 180D window check from symbol profiles
- trigger rows with complete 30D/90D/180D MFE/MAE
- C26 canonical compression and duplicate avoidance
```

Non-validation scope:

```text
- production scoring change
- live candidate discovery
- brokerage/API connection
- exact official DART URL repair
```

Evidence URL repair is useful later, but this MD is still usable as source-proxy v12 research because price path fields and canonical scope are complete.

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,stage2_required_bridge,canonical_archetype_specific,L8_PLATFORM_CONTENT_SW_SECURITY,C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE,0,1,+1,"Require monetization/OP leverage bridge, not ad-recovery label only","Rejects 035720 and 089600 weak-bridge false positives while keeping 067160 as high-MAE positive","TRG_C26_R8_L97_067160_2024-06-20_STAGE2A|TRG_C26_R8_L97_035720_2024-05-09_STAGE2A|TRG_C26_R8_L97_089600_2024-05-09_STAGE2A",3,3,2,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,local_4b_watch_guard,canonical_archetype_specific,L8_PLATFORM_CONTENT_SW_SECURITY,C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE,0,1,+1,"Traffic migration can local-peak before durable monetization evidence","SOOP MFE30 +22.91 but MAE180 -32.82; use 4B watch after local peak","TRG_C26_R8_L97_067160_2024-06-20_STAGE2A",1,1,0,low,canonical_shadow_only,"guardrail only"
```

## 25. Machine-Readable Rows

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
{"row_type":"case","case_id":"C26_R8_L97_067160_SOOP_GLOBAL_PLATFORM_MIGRATION","symbol":"067160","company_name":"SOOP","round":"R8","loop":"97","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE","fine_archetype_id":"LIVE_STREAMING_PLATFORM_MIGRATION_GLOBAL_SOOP_REBRAND_USER_TRAFFIC_OPERATING_LEVERAGE","case_type":"high_mae_success","positive_or_counterexample":"positive","best_trigger":"TRG_C26_R8_L97_067160_2024-06-20_STAGE2A","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"aligned_positive_high_mae","current_profile_verdict":"current_profile_4B_too_late","price_source":"Songdaiki/stock-web","notes":"Twitch Korea shutdown / SOOP global beta and rebrand route created traffic migration optionality, but monetization bridge was not yet durable enough to protect 180D drawdown."}
{"row_type":"case","case_id":"C26_R8_L97_035720_KAKAO_TALKBIZ_AD_RECOVERY_LABEL","symbol":"035720","company_name":"카카오","round":"R8","loop":"97","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE","fine_archetype_id":"TALK_BIZ_AD_RECOVERY_WITHOUT_MARGIN_REVISION_AND_REGULATORY_TRUST_BRIDGE","case_type":"failed_rerating","positive_or_counterexample":"counterexample","best_trigger":"TRG_C26_R8_L97_035720_2024-05-09_STAGE2A","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"false_positive_low_mfe_high_mae","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"Q1/Q2 Talk Biz advertising recovery language existed, but operating leverage was diluted by group cost, execution, and trust/regulatory overhang."}
{"row_type":"case","case_id":"C26_R8_L97_089600_NASMEDIA_DIGITAL_AD_RECOVERY_LABEL","symbol":"089600","company_name":"KT나스미디어","round":"R8","loop":"97","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE","fine_archetype_id":"AD_REP_DIGITAL_AD_RECOVERY_LABEL_WITHOUT_PLATFORM_TAKE_RATE_OR_OP_LEVERAGE","case_type":"failed_rerating","positive_or_counterexample":"counterexample","best_trigger":"TRG_C26_R8_L97_089600_2024-05-09_STAGE2A","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"false_positive_low_mfe_high_mae","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"Digital ad recovery label did not become platform-level monetization or operating leverage; the stock path behaved like ad-rep cyclicality rather than C26 structural platform rerating."}
{"row_type":"trigger","trigger_id":"TRG_C26_R8_L97_067160_2024-06-20_STAGE2A","case_id":"C26_R8_L97_067160_SOOP_GLOBAL_PLATFORM_MIGRATION","symbol":"067160","company_name":"SOOP","round":"R8","loop":"97","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE","fine_archetype_id":"LIVE_STREAMING_PLATFORM_MIGRATION_GLOBAL_SOOP_REBRAND_USER_TRAFFIC_OPERATING_LEVERAGE","sector":"platform / content / software / advertising / digital monetization","primary_archetype":"platform_ad_revenue_operating_leverage","loop_objective":"coverage_gap_fill|counterexample_mining|stage2_actionable_bonus_stress_test|canonical_archetype_compression|sector_specific_rule_discovery","trigger_type":"Stage2-Actionable","trigger_date":"2024-06-20","evidence_available_at_that_date":"Twitch Korea shutdown / SOOP global beta and rebrand route created traffic migration optionality, but monetization bridge was not yet durable enough to protect 180D drawdown.","evidence_source":"SOOP/AfreecaTV company rebrand and global platform launch news; Twitch Korea exit event; source_proxy_only=true","stage2_evidence_fields":["public_event_or_disclosure","relative_strength","capacity_or_volume_route","policy_or_regulatory_optionality"],"stage3_evidence_fields":["repeat_order_or_conversion"],"stage4b_evidence_fields":["positioning_overheat","price_only_local_peak"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/067/067160/2024.csv|atlas/ohlcv_tradable_by_symbol_year/067/067160/2025.csv","profile_path":"atlas/symbol_profiles/067/067160.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-06-20","entry_price":117000,"MFE_30D_pct":22.91,"MFE_90D_pct":22.91,"MFE_180D_pct":22.91,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-17.86,"MAE_90D_pct":-26.07,"MAE_180D_pct":-32.82,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-07-11","peak_price":143800,"drawdown_after_peak_pct":-45.34,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"price_only_local_4B_too_early","four_b_evidence_type":["positioning_overheat","price_only_local_peak"],"four_c_protection_label":"not_applicable","trigger_outcome_label":"platform_migration_positive_but_high_mae_after_local_peak","current_profile_verdict":"current_profile_4B_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C26_R8_L97_067160_2024-06-20_117000","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"TRG_C26_R8_L97_035720_2024-05-09_STAGE2A","case_id":"C26_R8_L97_035720_KAKAO_TALKBIZ_AD_RECOVERY_LABEL","symbol":"035720","company_name":"카카오","round":"R8","loop":"97","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE","fine_archetype_id":"TALK_BIZ_AD_RECOVERY_WITHOUT_MARGIN_REVISION_AND_REGULATORY_TRUST_BRIDGE","sector":"platform / content / software / advertising / digital monetization","primary_archetype":"platform_ad_revenue_operating_leverage","loop_objective":"coverage_gap_fill|counterexample_mining|stage2_actionable_bonus_stress_test|canonical_archetype_compression|sector_specific_rule_discovery","trigger_type":"Stage2-Actionable","trigger_date":"2024-05-09","evidence_available_at_that_date":"Q1/Q2 Talk Biz advertising recovery language existed, but operating leverage was diluted by group cost, execution, and trust/regulatory overhang.","evidence_source":"Kakao quarterly earnings / Talk Biz disclosure proxy; source_proxy_only=true","stage2_evidence_fields":["public_event_or_disclosure","early_revision_signal"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["accounting_or_trust_break","positioning_overheat"],"stage4c_evidence_fields":["accounting_or_trust_break"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/035/035720/2024.csv|atlas/ohlcv_tradable_by_symbol_year/035/035720/2025.csv","profile_path":"atlas/symbol_profiles/035/035720.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-05-09","entry_price":48600,"MFE_30D_pct":4.12,"MFE_90D_pct":4.12,"MFE_180D_pct":4.12,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-13.48,"MAE_90D_pct":-32.3,"MAE_180D_pct":-33.02,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-05-09","peak_price":50600,"drawdown_after_peak_pct":-35.67,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_applicable","four_b_evidence_type":["accounting_or_trust_break","positioning_overheat"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"ad_recovery_label_false_positive_without_operating_leverage","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C26_R8_L97_035720_2024-05-09_48600","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"TRG_C26_R8_L97_089600_2024-05-09_STAGE2A","case_id":"C26_R8_L97_089600_NASMEDIA_DIGITAL_AD_RECOVERY_LABEL","symbol":"089600","company_name":"KT나스미디어","round":"R8","loop":"97","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE","fine_archetype_id":"AD_REP_DIGITAL_AD_RECOVERY_LABEL_WITHOUT_PLATFORM_TAKE_RATE_OR_OP_LEVERAGE","sector":"platform / content / software / advertising / digital monetization","primary_archetype":"platform_ad_revenue_operating_leverage","loop_objective":"coverage_gap_fill|counterexample_mining|stage2_actionable_bonus_stress_test|canonical_archetype_compression|sector_specific_rule_discovery","trigger_type":"Stage2-Actionable","trigger_date":"2024-05-09","evidence_available_at_that_date":"Digital ad recovery label did not become platform-level monetization or operating leverage; the stock path behaved like ad-rep cyclicality rather than C26 structural platform rerating.","evidence_source":"Nasmedia quarterly earnings / ad market recovery proxy; source_proxy_only=true","stage2_evidence_fields":["public_event_or_disclosure"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["price_only_local_peak","revision_slowdown"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/089/089600/2024.csv|atlas/ohlcv_tradable_by_symbol_year/089/089600/2025.csv","profile_path":"atlas/symbol_profiles/089/089600.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-05-09","entry_price":18800,"MFE_30D_pct":1.06,"MFE_90D_pct":1.06,"MFE_180D_pct":1.06,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-12.87,"MAE_90D_pct":-19.15,"MAE_180D_pct":-28.09,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-05-09","peak_price":19000,"drawdown_after_peak_pct":-28.84,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_applicable","four_b_evidence_type":["price_only_local_peak","revision_slowdown"],"four_c_protection_label":"not_applicable","trigger_outcome_label":"ad_rep_recovery_label_false_positive","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C26_R8_L97_089600_2024-05-09_18800","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C26_R8_L97_067160_SOOP_GLOBAL_PLATFORM_MIGRATION","trigger_id":"TRG_C26_R8_L97_067160_2024-06-20_STAGE2A","symbol":"067160","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":2,"revision_score":4,"relative_strength_score":8,"customer_quality_score":5,"policy_or_regulatory_score":3,"valuation_repricing_score":4,"execution_risk_score":2,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":72,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":2,"revision_score":4,"relative_strength_score":8,"customer_quality_score":5,"policy_or_regulatory_score":3,"valuation_repricing_score":6,"execution_risk_score":7,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":70,"stage_label_after":"Stage2-Actionable+4B-watch","changed_components":["revision_score","relative_strength_score","execution_risk_score","valuation_repricing_score"],"component_delta_explanation":"C26 should reward monetization/OP leverage only when traffic or ad recovery converts into margin/revision; weak bridge routes to watch/guard.","MFE_90D_pct":22.91,"MAE_90D_pct":-26.07,"score_return_alignment_label":"positive_but_high_drawdown","current_profile_verdict":"current_profile_4B_too_late"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C26_R8_L97_035720_KAKAO_TALKBIZ_AD_RECOVERY_LABEL","trigger_id":"TRG_C26_R8_L97_035720_2024-05-09_STAGE2A","symbol":"035720","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":2,"relative_strength_score":2,"customer_quality_score":2,"policy_or_regulatory_score":0,"valuation_repricing_score":3,"execution_risk_score":4,"legal_or_contract_risk_score":5,"dilution_cb_risk_score":0,"accounting_trust_risk_score":6},"weighted_score_before":68,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":1,"customer_quality_score":2,"policy_or_regulatory_score":0,"valuation_repricing_score":3,"execution_risk_score":7,"legal_or_contract_risk_score":5,"dilution_cb_risk_score":0,"accounting_trust_risk_score":6},"weighted_score_after":61,"stage_label_after":"Stage1/weak-watch","changed_components":["revision_score","relative_strength_score","execution_risk_score","valuation_repricing_score"],"component_delta_explanation":"C26 should reward monetization/OP leverage only when traffic or ad recovery converts into margin/revision; weak bridge routes to watch/guard.","MFE_90D_pct":4.12,"MAE_90D_pct":-32.3,"score_return_alignment_label":"false_positive","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C26_R8_L97_089600_NASMEDIA_DIGITAL_AD_RECOVERY_LABEL","trigger_id":"TRG_C26_R8_L97_089600_2024-05-09_STAGE2A","symbol":"089600","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":2,"relative_strength_score":2,"customer_quality_score":2,"policy_or_regulatory_score":0,"valuation_repricing_score":3,"execution_risk_score":4,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":66,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":1,"customer_quality_score":2,"policy_or_regulatory_score":0,"valuation_repricing_score":3,"execution_risk_score":7,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":58,"stage_label_after":"Stage1/weak-watch","changed_components":["revision_score","relative_strength_score","execution_risk_score","valuation_repricing_score"],"component_delta_explanation":"C26 should reward monetization/OP leverage only when traffic or ad recovery converts into margin/revision; weak bridge routes to watch/guard.","MFE_90D_pct":1.06,"MAE_90D_pct":-19.15,"score_return_alignment_label":"false_positive","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"residual_contribution","round":"R8","loop":"97","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE","new_independent_case_count":3,"reused_case_count":0,"new_symbol_count":3,"new_trigger_family_count":3,"tested_existing_calibrated_axes":["stage2_actionable_evidence_bonus","price_only_blowoff_blocks_positive_stage","full_4b_requires_non_price_evidence"],"residual_error_types_found":["ad_recovery_label_false_positive","traffic_migration_high_MAE_after_local_peak","missing_operating_leverage_bridge"],"loop_contribution_label":"canonical_archetype_rule_candidate","do_not_propose_new_weight_delta":false}
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

## 27. Next Round State

```text
completed_round = R8
completed_loop = 97
selection_basis = docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket = Priority 0
next_recommended_archetypes = C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE, C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK, C31_POLICY_SUBSIDY_LEGISLATION_EVENT, C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP, C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY, C15_MATERIAL_SPREAD_SUPERCYCLE, C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION, C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN, C22_INSURANCE_RATE_CYCLE_RESERVE, C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT
round_schedule_status = coverage_index_selected
round_sector_consistency = pass
```

## 28. Batch Ingest Self-Audit

```text
expected_v12_result_file: true
filename_pattern_pass: true
metadata_filename_consistency: pass
jsonl_trigger_row_count: 3
calibration_usable_trigger_count: 3
representative_trigger_count: 3
new_weight_evidence_candidate_count: 3
guardrail_candidate_count: 1
narrative_only_or_rejected_count: 0
rows_missing_required_mfe_mae: 0
rows_missing_entry_price_or_date: 0
rows_with_noncanonical_trigger_type: 0
rows_with_compact_mfe_mae_alias_only: 0
ready_for_batch_ingest: true
```
