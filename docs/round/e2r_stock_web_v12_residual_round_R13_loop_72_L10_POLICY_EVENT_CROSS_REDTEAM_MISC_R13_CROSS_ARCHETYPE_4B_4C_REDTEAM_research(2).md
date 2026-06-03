# E2R Stock-Web Historical Calibration / R13 Cross-Archetype 4B·4C Red-Team Round

## 0. Research Metadata

```text
scheduled_round: R13
scheduled_loop: 72
round_schedule_status: valid
round_sector_consistency: pass
computed_next_round: R1
computed_next_loop: 73
large_sector_id: L10_POLICY_EVENT_CROSS_REDTEAM_MISC
canonical_archetype_id: R13_CROSS_ARCHETYPE_4B_4C_REDTEAM
fine_archetype_id: R13_EVENT_PRICE_PEAK_4B_4C_ROUTE_GUARD
loop_objective: cross_archetype_redteam | 4B_non_price_requirement_stress_test | 4C_thesis_break_timing_test | stage2_false_positive_review | high_MAE_guardrail
price_source: Songdaiki/stock-web
stock_web_manifest_max_date: 2026-02-20
production_scoring_changed: false
shadow_weight_only: true
r13_cross_case_mode: true
new_independent_case_count: 0
do_not_count_as_new_case: true
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

## 2. R13 Scope

R13 is not a normal sector expansion round. It is a cross-archetype checkpoint. Therefore every representative row in this MD is deliberately marked:

```text
r13_cross_case = true
do_not_count_as_new_case = true
independent_evidence_weight = 0.0
aggregate_group_role = r13_cross_check
```

This run tests a narrower question than generic high-MAE:

```text
Can a row with strong MFE or local peak proximity be routed incorrectly to Stage3/Green
when the correct outcome is 4B watch or hard 4C?
```

The answer from this R13 set is yes. The guardrail should keep price/event peaks from becoming positive evidence unless the source-archetype bridge survives.

## 3. Cross-Archetype Source Map

| source large sector | source canonical | symbol | company | 4B verdict | 4C/watch label |
|---|---|---:|---|---|---|
| L7_BIO_HEALTHCARE_MEDICAL | C24_BIO_TRIAL_DATA_EVENT_RISK | 007390 | 네이처셀 | event_peak_local_4B_rejected_as_positive_and_routed_to_hard_4C | hard_4C_thesis_break |
| L8_PLATFORM_CONTENT_SW_SECURITY | C27_CONTENT_IP_GLOBAL_MONETIZATION | 263750 | 펄어비스 | full_window_MFE_but_non_price_bridge_absent_keep_4B_watch_not_green | bridge_absent_watch |
| L10_POLICY_EVENT_CROSS_REDTEAM_MISC | C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP | 241560 | 두산밥캣 | local_event_4B_rejected_as_positive_due_to_terms_value_bridge_absence | high_MAE_watch |
| L10_POLICY_EVENT_CROSS_REDTEAM_MISC | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | 008770 | 호텔신라 | policy_theme_local_4B_rejected_as_positive_stage | high_MAE_watch |

## 4. No-Repeat / Duplicate Handling

No-Repeat hard duplicate key remains:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

For R13, these are cross-check rows, not new source-archetype rows.

```text
r13_cross_case_count = 4
new_independent_case_count = 0
reused_case_count = 4
source_archetype_coverage_increment = 0
independent_evidence_weight = 0.0
do_not_count_as_new_case = true
```

## 5. Stock-Web OHLC Input / Price Source Validation

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","source_name":"FinanceData/marcap","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
```

Stock-web assumptions used in this MD:

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

## 6. Historical Eligibility Gate

```text
entry row exists = true
forward 180 trading days available = true
MFE/MAE 30D/90D/180D computed = true
price_basis = tradable_raw
price_adjustment_status = raw_unadjusted_marcap
corporate_action_window_status = clean_180D_window
```

R13 rows are calibration-usable for guardrail diagnostics but carry zero source-archetype evidence weight.

## 7. Trigger-Level OHLC Backtest Table

| symbol | company | source canonical | trigger | entry_date | entry_price | MFE30 | MFE90 | MFE180 | MAE30 | MAE90 | MAE180 | peak_date | peak_price | DD after peak |
|---:|---|---|---|---|---:|---:|---:|---:|---:|---:|---:|---|---:|---:|
| 007390 | 네이처셀 | C24_BIO_TRIAL_DATA_EVENT_RISK | Stage2-Actionable | 2023-03-31 | 18000 | 41.67 | 41.67 | 41.67 | -48.28 | -59.56 | -61.78 | 2023-04-06 | 25500 | -73.02 |
| 263750 | 펄어비스 | C27_CONTENT_IP_GLOBAL_MONETIZATION | Stage2-Actionable | 2021-08-26 | 87900 | 16.04 | 65.19 | 65.19 | -17.97 | -17.97 | -17.97 | 2021-11-17 | 145200 | -37.53 |
| 241560 | 두산밥캣 | C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP | Stage2-Actionable | 2024-07-12 | 54600 | 8.97 | 8.97 | 8.97 | -38.92 | -38.92 | -38.92 | 2024-07-12 | 59500 | -43.95 |
| 008770 | 호텔신라 | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | Stage2-Actionable | 2023-08-10 | 86800 | 8.29 | 8.29 | 8.29 | -9.45 | -33.29 | -33.29 | 2023-08-28 | 94000 | -38.4 |

## 8. Cross-Case Diagnosis

### 8.1 007390 / 네이처셀 — pre-event MFE cannot defeat hard 4C

The entry row is 2023-03-31 at 18,000. The event path reaches 25,500, but then breaks into deep MAE after regulatory failure. This is the cleanest R13 lesson: in binary biotech, pre-event MFE is only a flare. If the thesis breaks, hard 4C must override the earlier price path.

```text
source_canonical = C24_BIO_TRIAL_DATA_EVENT_RISK
R13 route = hard_4C_thesis_break
guardrail = hard_4c_thesis_break_routes_to_4c must override prior MFE
```

### 8.2 263750 / 펄어비스 — large MFE without monetization bridge is 4B watch, not Green

The entry row is 2021-08-26 at 87,900. The full window reaches 145,200. That looks strong on price alone, but the source bridge is not launch-to-revenue or retention; it is trailer/IP hype. R13 should preserve the move as a 4B watch example, not transform it into Stage3-Green evidence.

```text
source_canonical = C27_CONTENT_IP_GLOBAL_MONETIZATION
R13 route = 4B watch / no Green
guardrail = full 4B requires non-price evidence
```

### 8.3 241560 / 두산밥캣 — governance terms risk can invert the premium

The entry row is 2024-07-12 at 54,600. The local high was the same event window, but the path then falls to 33,350. This is the governance version of the same pattern: if minority value and terms quality are absent, a restructuring headline can become a discount-widening event.

```text
source_canonical = C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP
R13 route = local 4B watch + high-MAE guard
guardrail = event terms and minority-value bridge required
```

### 8.4 008770 / 호텔신라 — policy reopening is not sell-through

The entry row is 2023-08-10 at 86,800. The policy theme creates a local MFE, then collapses into high MAE. This is the service-policy version: tourism news can open the door, but sell-through, margin, inventory, and cashflow determine whether anyone walks through it.

```text
source_canonical = C31_POLICY_SUBSIDY_LEGISLATION_EVENT
R13 route = local 4B watch + high-MAE guard
guardrail = policy-to-economics bridge required
```

## 9. Stage2 / Yellow / Green / 4B / 4C Comparison

```text
Common R13 pattern:
  Stage2-Actionable = may be acceptable as event watch
  Stage3-Yellow = reject unless source-archetype bridge survives
  Stage3-Green = reject when bridge is absent, even if MFE was large
  4B = local/full-window watch only unless non-price evidence confirms peak-quality
  4C = hard route when binary thesis breaks
```

## 10. Current Calibrated Profile Stress Test

| question | R13 result |
|---|---|
| Stage2 actionable bonus too strong? | It becomes too strong if price/event evidence is allowed to travel upward without source bridge. |
| Stage3 Yellow threshold too loose? | Not globally; the source-bridge gate should intercept before Yellow. |
| Stage3 Green too strict? | Correct. This R13 run reinforces strict Green. |
| Price-only blowoff guard appropriate? | Yes, but it must cooperate with 4B and high-MAE routing. |
| Full 4B non-price requirement appropriate? | Yes. Large MFE alone is not full 4B-positive evidence. |
| 4C routing issue? | 007390 confirms hard 4C must override earlier MFE after thesis break. |

## 11. Cross-Archetype Guardrail Candidate

```text
canonical_archetype_rule_candidate: true
rule_scope: cross_archetype_guardrail
rule_id: r13_cross_4b_price_peak_not_positive_without_source_bridge

rule:
  A local or full-window price peak must not become Stage3-positive evidence unless the source-archetype bridge survives.
  If the evidence is event/price/theme-heavy and the source bridge is absent, route to 4B watch or high-MAE guard.
  If the source thesis breaks, route to hard 4C even if pre-break MFE was large.

source_bridge_examples:
  C24 -> validated clinical/regulatory/license bridge
  C27 -> launch-to-revenue / retention / monetization bridge
  C31 -> policy-to-economics / sell-through / margin bridge
  C32 -> control/NAV/minority-value / terms-quality bridge
```

## 12. Before / After Backtest Comparison

| profile | eligible R13 cross rows | avg MFE90 | avg MAE90 | Green false-positive risk | verdict |
|---|---:|---:|---:|---:|---|
| P0 e2r_2_1_stock_web_calibrated_proxy | 4 | 31.03 | -37.44 | high if MFE is over-read | good base, needs R13 guard overlay |
| P0b e2r_2_0_baseline_reference | 4 | 31.03 | -37.44 | medium | safer but less explanatory |
| P2 cross_4B_4C_guard_profile | 4 routed | 31.03 | -37.44 | 0% after no-Green routing | preferred shadow |
| P3 hard_4C_override_profile | 1 hard route | 41.67 | -59.56 | 0% after hard 4C | necessary for binary events |

## 13. Score-Return Alignment Matrix

| case | source canonical | current profile verdict | R13 alignment |
|---|---|---|---|
| 007390 | C24 | current_profile_false_positive_without_hard_4C | hard 4C overrides pre-event MFE |
| 263750 | C27 | current_profile_partially_false_positive_if_green | large MFE remains 4B watch, not Green |
| 241560 | C32 | current_profile_false_positive_without_terms_guard | local 4B/high-MAE guard blocks governance headline |
| 008770 | C31 | current_profile_false_positive_without_bridge_guard | policy theme blocked without sell-through/margin bridge |

## 14. Coverage Matrix

| large_sector_id | canonical_archetype_id | source archetypes | cross rows | new independent | reused/cross | counterexample | 4B watch | hard 4C | sector_rule | canonical_rule | coverage contribution |
|---|---|---|---:|---:|---:|---:|---:|---:|---|---|---|
| L10_POLICY_EVENT_CROSS_REDTEAM_MISC | R13_CROSS_ARCHETYPE_4B_4C_REDTEAM | C24/C27/C31/C32 | 4 | 0 | 4 | 4 | 4 | 1 | false | true | strengthens R13 4B/4C routing without adding source-archetype coverage |

## 15. Residual Contribution Summary

```text
r13_cross_case_count: 4
new_independent_case_count: 0
reused_case_count: 4
reused_case_policy: R13 cross-check rows only; no source-archetype evidence weight
new_symbol_count_for_source_archetype: 0
new_trigger_family_count_for_source_archetype: 0
tested_existing_calibrated_axes:
- stage2_actionable_evidence_bonus
- price_only_blowoff_blocks_positive_stage
- full_4b_requires_non_price_evidence
- local_4b_watch_guard
- high_MAE_guardrail
- hard_4c_thesis_break_routes_to_4c
residual_error_types_found:
- pre-event MFE misread as positive
- large MFE without source bridge Green false positive
- local 4B high-MAE event terms risk
- hard 4C after binary event failure
new_axis_proposed: null
existing_axis_strengthened:
- full_4b_requires_non_price_evidence
- local_4b_watch_guard
- high_MAE_watch_guard
- hard_4c_thesis_break_routes_to_4c
existing_axis_weakened: null
sector_specific_rule_candidate: false
canonical_archetype_rule_candidate: true
loop_contribution_label: r13_cross_archetype_4B_4C_redteam
```

## 16. Validation Scope / Non-Validation Scope

Validated:

```text
- stock-web tradable_raw OHLC rows
- entry_date / entry_price
- MFE/MAE/peak/drawdown
- R13 round consistency
- R13 canonical scope
- cross-archetype source mapping
- do_not_count_as_new_case handling
```

Not validated:

```text
- exact disclosure URLs
- exact report URLs
- production scoring behavior
- live candidate status
- source-archetype coverage increments
```

## 17. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,r13_cross_4b_price_peak_not_positive_without_source_bridge,cross_archetype_guardrail,L10_POLICY_EVENT_CROSS_REDTEAM_MISC,R13_CROSS_ARCHETYPE_4B_4C_REDTEAM,0,1,+1,"Across C24/C27/C31/C32, local or full-window MFE cannot become Stage3-positive evidence when the source-archetype bridge is absent or broken","4 cross-check rows remain Watch/4B/4C instead of Stage3-Green; no source-archetype independent evidence is added","TRG_R13L72_4B4C_C24_007390_20230331_APPROVAL_EVENT_TO_HARD_4C|TRG_R13L72_4B4C_C27_263750_20210826_TRAILER_IP_MFE_BUT_NO_GREEN|TRG_R13L72_4B4C_C32_241560_20240712_GOVERNANCE_RATIO_LOCAL_4B_HIGH_MAE|TRG_R13L72_4B4C_C31_008770_20230810_DUTYFREE_POLICY_LOCAL_4B_HIGH_MAE",4,0,4,medium,cross_archetype_shadow_only,"R13 rows have do_not_count_as_new_case=true"
shadow_weight,r13_hard_4c_overrides_pre_event_mfe,cross_archetype_guardrail,L10_POLICY_EVENT_CROSS_REDTEAM_MISC,R13_CROSS_ARCHETYPE_4B_4C_REDTEAM,1,1,0,"A binary thesis break should override prior MFE and route to hard 4C when regulatory/terms/economic evidence breaks","007390 validates hard 4C routing; 241560/008770 validate high-MAE watch before hard 4C","TRG_R13L72_4B4C_C24_007390_20230331_APPROVAL_EVENT_TO_HARD_4C|TRG_R13L72_4B4C_C32_241560_20240712_GOVERNANCE_RATIO_LOCAL_4B_HIGH_MAE|TRG_R13L72_4B4C_C31_008770_20230810_DUTYFREE_POLICY_LOCAL_4B_HIGH_MAE",3,0,3,medium,existing_axis_kept,"strengthens hard_4c/high_MAE routing without production delta"
```

## 18. Machine-Readable Rows

### 18.1 price_source_validation

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","source_name":"FinanceData/marcap","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
```

### 18.2 case rows

```jsonl
{"row_type":"case","case_id":"R13L72_4B4C_C24_007390_20230331_APPROVAL_EVENT_TO_HARD_4C","symbol":"007390","company_name":"네이처셀","round":"R13","loop":"72","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_4B_4C_REDTEAM","source_large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","source_canonical_archetype_id":"C24_BIO_TRIAL_DATA_EVENT_RISK","source_fine_archetype_id":"C24_CELL_THERAPY_APPROVAL_EVENT_BINARY_RISK_GUARD","fine_archetype_id":"R13_EVENT_PEAK_TO_HARD_4C_ROUTE","deep_sub_archetype_id":"BINARY_APPROVAL_EVENT_MFE_THEN_REGULATORY_THESIS_BREAK","case_type":"r13_cross_case_hard_4C_after_event_peak","positive_or_counterexample":"counterexample","best_trigger":"Stage2-Actionable","calibration_usable":true,"r13_cross_case":true,"is_new_independent_case":false,"do_not_count_as_new_case":true,"reuse_reason":"R13 cross-archetype checkpoint row; no source-archetype independent evidence weight","independent_evidence_weight":0.0,"score_price_alignment":"score_return_misaligned","current_profile_verdict":"current_profile_false_positive_without_hard_4C","price_source":"Songdaiki/stock-web","notes":"R13 cross-check only: validates 4B/4C/high-MAE routing, not source archetype coverage."}
{"row_type":"case","case_id":"R13L72_4B4C_C27_263750_20210826_TRAILER_IP_MFE_BUT_NO_GREEN","symbol":"263750","company_name":"펄어비스","round":"R13","loop":"72","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_4B_4C_REDTEAM","source_large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","source_canonical_archetype_id":"C27_CONTENT_IP_GLOBAL_MONETIZATION","source_fine_archetype_id":"C27_GAME_TRAILER_IP_HYPE_WITHOUT_MONETIZATION_BRIDGE","fine_archetype_id":"R13_LARGE_MFE_WITHOUT_NON_PRICE_BRIDGE_4B_WATCH","deep_sub_archetype_id":"TRAILER_IP_HYPE_FULL_WINDOW_MFE_WITHOUT_LAUNCH_REVENUE_RETENTION","case_type":"r13_cross_case_large_MFE_but_4B_watch_not_green","positive_or_counterexample":"counterexample","best_trigger":"Stage2-Actionable","calibration_usable":true,"r13_cross_case":true,"is_new_independent_case":false,"do_not_count_as_new_case":true,"reuse_reason":"R13 cross-archetype checkpoint row; no source-archetype independent evidence weight","independent_evidence_weight":0.0,"score_price_alignment":"score_return_mixed","current_profile_verdict":"current_profile_partially_false_positive_if_green","price_source":"Songdaiki/stock-web","notes":"R13 cross-check only: validates 4B/4C/high-MAE routing, not source archetype coverage."}
{"row_type":"case","case_id":"R13L72_4B4C_C32_241560_20240712_GOVERNANCE_RATIO_LOCAL_4B_HIGH_MAE","symbol":"241560","company_name":"두산밥캣","round":"R13","loop":"72","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_4B_4C_REDTEAM","source_large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","source_canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","source_fine_archetype_id":"C32_GOVERNANCE_RATIO_EVENT_PREMIUM_CAP_GUARD","fine_archetype_id":"R13_LOCAL_4B_EVENT_TERMS_HIGH_MAE_GUARD","deep_sub_archetype_id":"RESTRUCTURING_RATIO_EVENT_WITHOUT_MINORITY_VALUE_BRIDGE","case_type":"r13_cross_case_local_4B_high_MAE_governance_ratio","positive_or_counterexample":"counterexample","best_trigger":"Stage2-Actionable","calibration_usable":true,"r13_cross_case":true,"is_new_independent_case":false,"do_not_count_as_new_case":true,"reuse_reason":"R13 cross-archetype checkpoint row; no source-archetype independent evidence weight","independent_evidence_weight":0.0,"score_price_alignment":"score_return_misaligned","current_profile_verdict":"current_profile_false_positive_without_terms_guard","price_source":"Songdaiki/stock-web","notes":"R13 cross-check only: validates 4B/4C/high-MAE routing, not source archetype coverage."}
{"row_type":"case","case_id":"R13L72_4B4C_C31_008770_20230810_DUTYFREE_POLICY_LOCAL_4B_HIGH_MAE","symbol":"008770","company_name":"호텔신라","round":"R13","loop":"72","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_4B_4C_REDTEAM","source_large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","source_canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","source_fine_archetype_id":"C31_DUTYFREE_TOURISM_POLICY_WITHOUT_SELLTHROUGH_MARGIN_BRIDGE","fine_archetype_id":"R13_POLICY_EVENT_LOCAL_4B_SELLTHROUGH_BRIDGE_GUARD","deep_sub_archetype_id":"DUTYFREE_POLICY_THEME_WITHOUT_SELLTHROUGH_MARGIN_HIGH_MAE","case_type":"r13_cross_case_policy_theme_local_4B_high_MAE","positive_or_counterexample":"counterexample","best_trigger":"Stage2-Actionable","calibration_usable":true,"r13_cross_case":true,"is_new_independent_case":false,"do_not_count_as_new_case":true,"reuse_reason":"R13 cross-archetype checkpoint row; no source-archetype independent evidence weight","independent_evidence_weight":0.0,"score_price_alignment":"score_return_misaligned","current_profile_verdict":"current_profile_false_positive_without_bridge_guard","price_source":"Songdaiki/stock-web","notes":"R13 cross-check only: validates 4B/4C/high-MAE routing, not source archetype coverage."}
```

### 18.3 trigger rows

```jsonl
{"row_type":"trigger","trigger_id":"TRG_R13L72_4B4C_C24_007390_20230331_APPROVAL_EVENT_TO_HARD_4C","case_id":"R13L72_4B4C_C24_007390_20230331_APPROVAL_EVENT_TO_HARD_4C","symbol":"007390","company_name":"네이처셀","round":"R13","loop":"72","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_4B_4C_REDTEAM","source_large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","source_canonical_archetype_id":"C24_BIO_TRIAL_DATA_EVENT_RISK","source_fine_archetype_id":"C24_CELL_THERAPY_APPROVAL_EVENT_BINARY_RISK_GUARD","fine_archetype_id":"R13_EVENT_PEAK_TO_HARD_4C_ROUTE","deep_sub_archetype_id":"BINARY_APPROVAL_EVENT_MFE_THEN_REGULATORY_THESIS_BREAK","loop_objective":"cross_archetype_redteam|4B_non_price_requirement_stress_test|4C_thesis_break_timing_test|stage2_false_positive_review|high_MAE_guardrail","trigger_type":"Stage2-Actionable","trigger_date":"2023-03-31","entry_date":"2023-03-31","entry_price":18000,"evidence_available_at_that_date":"source_proxy_cell_therapy_approval_binary_event_followed_by_regulatory_rejection; evidence_url_pending","evidence_source":"source_proxy_cell_therapy_approval_binary_event_followed_by_regulatory_rejection; evidence_url_pending","bridge_summary":"approval-event price MFE was not a durable clinical-data bridge; regulatory failure should route to hard 4C rather than 4B-success or Green","stage2_evidence_fields":["binary_approval_event","price_spike","relative_strength"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["price_event_local_peak","event_crowding"],"stage4c_evidence_fields":["hard_regulatory_thesis_break","high_MAE_after_event_failure"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/007/007390/2023.csv","profile_path":"atlas/symbol_profiles/007/007390.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":41.67,"MFE_90D_pct":41.67,"MFE_180D_pct":41.67,"MFE_1Y_pct":41.67,"MFE_2Y_pct":41.67,"MAE_30D_pct":-48.28,"MAE_90D_pct":-59.56,"MAE_180D_pct":-61.78,"MAE_1Y_pct":-61.78,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2023-04-06","peak_price":25500,"drawdown_after_peak_pct":-73.02,"green_lateness_ratio":"not_applicable_for_R13_cross_case","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"event_peak_local_4B_rejected_as_positive_and_routed_to_hard_4C","four_b_evidence_type":"r13_cross_price_event_or_bridge_absent_watch","four_c_protection_label":"hard_4C_thesis_break","trigger_outcome_label":"hard_4C_after_event_MFE","current_profile_verdict":"current_profile_false_positive_without_hard_4C","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R13L72_4B4C_C24_007390_20230331_APPROVAL_EVENT_TO_HARD_4C_entry","dedupe_for_aggregate":true,"aggregate_group_role":"r13_cross_check","r13_cross_case":true,"is_new_independent_case":false,"reuse_reason":"R13 cross-archetype checkpoint; no new source-archetype evidence weight","independent_evidence_weight":0.0,"do_not_count_as_new_case":true}
{"row_type":"trigger","trigger_id":"TRG_R13L72_4B4C_C27_263750_20210826_TRAILER_IP_MFE_BUT_NO_GREEN","case_id":"R13L72_4B4C_C27_263750_20210826_TRAILER_IP_MFE_BUT_NO_GREEN","symbol":"263750","company_name":"펄어비스","round":"R13","loop":"72","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_4B_4C_REDTEAM","source_large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","source_canonical_archetype_id":"C27_CONTENT_IP_GLOBAL_MONETIZATION","source_fine_archetype_id":"C27_GAME_TRAILER_IP_HYPE_WITHOUT_MONETIZATION_BRIDGE","fine_archetype_id":"R13_LARGE_MFE_WITHOUT_NON_PRICE_BRIDGE_4B_WATCH","deep_sub_archetype_id":"TRAILER_IP_HYPE_FULL_WINDOW_MFE_WITHOUT_LAUNCH_REVENUE_RETENTION","loop_objective":"cross_archetype_redteam|4B_non_price_requirement_stress_test|4C_thesis_break_timing_test|stage2_false_positive_review|high_MAE_guardrail","trigger_type":"Stage2-Actionable","trigger_date":"2021-08-26","entry_date":"2021-08-26","entry_price":87900,"evidence_available_at_that_date":"source_proxy_game_trailer_IP_reveal_without_launch_retention_or_revenue_bridge; evidence_url_pending","evidence_source":"source_proxy_game_trailer_IP_reveal_without_launch_retention_or_revenue_bridge; evidence_url_pending","bridge_summary":"large MFE existed, but evidence remained trailer/IP hype without launch-to-revenue or retention bridge; classify as 4B watch, not Green","stage2_evidence_fields":["trailer_IP_reveal","price_strength","relative_strength"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["large_MFE_without_monetization_bridge","IP_hype_crowding","launch_delay_watch"],"stage4c_evidence_fields":["bridge_absent_watch"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/263/263750/2021.csv|atlas/ohlcv_tradable_by_symbol_year/263/263750/2022.csv","profile_path":"atlas/symbol_profiles/263/263750.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":16.04,"MFE_90D_pct":65.19,"MFE_180D_pct":65.19,"MFE_1Y_pct":65.19,"MFE_2Y_pct":65.19,"MAE_30D_pct":-17.97,"MAE_90D_pct":-17.97,"MAE_180D_pct":-17.97,"MAE_1Y_pct":-17.97,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2021-11-17","peak_price":145200,"drawdown_after_peak_pct":-37.53,"green_lateness_ratio":"not_applicable_for_R13_cross_case","four_b_local_peak_proximity":0.88,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"full_window_MFE_but_non_price_bridge_absent_keep_4B_watch_not_green","four_b_evidence_type":"r13_cross_price_event_or_bridge_absent_watch","four_c_protection_label":"bridge_absent_watch","trigger_outcome_label":"large_MFE_but_green_false_positive_guard","current_profile_verdict":"current_profile_partially_false_positive_if_green","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R13L72_4B4C_C27_263750_20210826_TRAILER_IP_MFE_BUT_NO_GREEN_entry","dedupe_for_aggregate":true,"aggregate_group_role":"r13_cross_check","r13_cross_case":true,"is_new_independent_case":false,"reuse_reason":"R13 cross-archetype checkpoint; no new source-archetype evidence weight","independent_evidence_weight":0.0,"do_not_count_as_new_case":true}
{"row_type":"trigger","trigger_id":"TRG_R13L72_4B4C_C32_241560_20240712_GOVERNANCE_RATIO_LOCAL_4B_HIGH_MAE","case_id":"R13L72_4B4C_C32_241560_20240712_GOVERNANCE_RATIO_LOCAL_4B_HIGH_MAE","symbol":"241560","company_name":"두산밥캣","round":"R13","loop":"72","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_4B_4C_REDTEAM","source_large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","source_canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","source_fine_archetype_id":"C32_GOVERNANCE_RATIO_EVENT_PREMIUM_CAP_GUARD","fine_archetype_id":"R13_LOCAL_4B_EVENT_TERMS_HIGH_MAE_GUARD","deep_sub_archetype_id":"RESTRUCTURING_RATIO_EVENT_WITHOUT_MINORITY_VALUE_BRIDGE","loop_objective":"cross_archetype_redteam|4B_non_price_requirement_stress_test|4C_thesis_break_timing_test|stage2_false_positive_review|high_MAE_guardrail","trigger_type":"Stage2-Actionable","trigger_date":"2024-07-12","entry_date":"2024-07-12","entry_price":54600,"evidence_available_at_that_date":"source_proxy_group_restructuring_ratio_event_without_minority_shareholder_value_bridge; evidence_url_pending","evidence_source":"source_proxy_group_restructuring_ratio_event_without_minority_shareholder_value_bridge; evidence_url_pending","bridge_summary":"governance ratio event lacked minority shareholder value and terms-quality bridge; local 4B should not promote and high-MAE watch should override theme score","stage2_evidence_fields":["governance_restructuring_event","ratio_terms_uncertainty","price_spike"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["price_event_local_peak","minority_value_bridge_absent","governance_discount_widening"],"stage4c_evidence_fields":["high_MAE_after_governance_terms_risk"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/241/241560/2024.csv","profile_path":"atlas/symbol_profiles/241/241560.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":8.97,"MFE_90D_pct":8.97,"MFE_180D_pct":8.97,"MFE_1Y_pct":8.97,"MFE_2Y_pct":8.97,"MAE_30D_pct":-38.92,"MAE_90D_pct":-38.92,"MAE_180D_pct":-38.92,"MAE_1Y_pct":-38.92,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-07-12","peak_price":59500,"drawdown_after_peak_pct":-43.95,"green_lateness_ratio":"not_applicable_for_R13_cross_case","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"local_event_4B_rejected_as_positive_due_to_terms_value_bridge_absence","four_b_evidence_type":"r13_cross_price_event_or_bridge_absent_watch","four_c_protection_label":"high_MAE_watch","trigger_outcome_label":"failed_rerating_high_MAE_governance_terms_counterexample","current_profile_verdict":"current_profile_false_positive_without_terms_guard","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R13L72_4B4C_C32_241560_20240712_GOVERNANCE_RATIO_LOCAL_4B_HIGH_MAE_entry","dedupe_for_aggregate":true,"aggregate_group_role":"r13_cross_check","r13_cross_case":true,"is_new_independent_case":false,"reuse_reason":"R13 cross-archetype checkpoint; no new source-archetype evidence weight","independent_evidence_weight":0.0,"do_not_count_as_new_case":true}
{"row_type":"trigger","trigger_id":"TRG_R13L72_4B4C_C31_008770_20230810_DUTYFREE_POLICY_LOCAL_4B_HIGH_MAE","case_id":"R13L72_4B4C_C31_008770_20230810_DUTYFREE_POLICY_LOCAL_4B_HIGH_MAE","symbol":"008770","company_name":"호텔신라","round":"R13","loop":"72","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_4B_4C_REDTEAM","source_large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","source_canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","source_fine_archetype_id":"C31_DUTYFREE_TOURISM_POLICY_WITHOUT_SELLTHROUGH_MARGIN_BRIDGE","fine_archetype_id":"R13_POLICY_EVENT_LOCAL_4B_SELLTHROUGH_BRIDGE_GUARD","deep_sub_archetype_id":"DUTYFREE_POLICY_THEME_WITHOUT_SELLTHROUGH_MARGIN_HIGH_MAE","loop_objective":"cross_archetype_redteam|4B_non_price_requirement_stress_test|4C_thesis_break_timing_test|stage2_false_positive_review|high_MAE_guardrail","trigger_type":"Stage2-Actionable","trigger_date":"2023-08-10","entry_date":"2023-08-10","entry_price":86800,"evidence_available_at_that_date":"source_proxy_China_group_tour_dutyfree_policy_theme_without_sellthrough_margin_bridge; evidence_url_pending","evidence_source":"source_proxy_China_group_tour_dutyfree_policy_theme_without_sellthrough_margin_bridge; evidence_url_pending","bridge_summary":"tourism policy theme lacked sell-through/margin/inventory bridge; local 4B and high-MAE watch should block Stage3 routing","stage2_evidence_fields":["tourism_policy_theme","dutyfree_reopening","relative_strength"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["policy_theme_local_peak","sellthrough_margin_bridge_absent"],"stage4c_evidence_fields":["high_MAE_without_margin_or_inventory_bridge"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/008/008770/2023.csv","profile_path":"atlas/symbol_profiles/008/008770.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":8.29,"MFE_90D_pct":8.29,"MFE_180D_pct":8.29,"MFE_1Y_pct":8.29,"MFE_2Y_pct":8.29,"MAE_30D_pct":-9.45,"MAE_90D_pct":-33.29,"MAE_180D_pct":-33.29,"MAE_1Y_pct":-33.29,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2023-08-28","peak_price":94000,"drawdown_after_peak_pct":-38.4,"green_lateness_ratio":"not_applicable_for_R13_cross_case","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"policy_theme_local_4B_rejected_as_positive_stage","four_b_evidence_type":"r13_cross_price_event_or_bridge_absent_watch","four_c_protection_label":"high_MAE_watch","trigger_outcome_label":"failed_rerating_high_MAE_policy_theme_counterexample","current_profile_verdict":"current_profile_false_positive_without_bridge_guard","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R13L72_4B4C_C31_008770_20230810_DUTYFREE_POLICY_LOCAL_4B_HIGH_MAE_entry","dedupe_for_aggregate":true,"aggregate_group_role":"r13_cross_check","r13_cross_case":true,"is_new_independent_case":false,"reuse_reason":"R13 cross-archetype checkpoint; no new source-archetype evidence weight","independent_evidence_weight":0.0,"do_not_count_as_new_case":true}
```

### 18.4 score_simulation rows

```jsonl
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R13L72_4B4C_C24_007390_20230331_APPROVAL_EVENT_TO_HARD_4C","trigger_id":"TRG_R13L72_4B4C_C24_007390_20230331_APPROVAL_EVENT_TO_HARD_4C","symbol":"007390","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_4B_4C_REDTEAM","source_canonical_archetype_id":"C24_BIO_TRIAL_DATA_EVENT_RISK","raw_component_scores_before":{"price_or_event_score":11,"source_bridge_score":2,"relative_strength_score":11,"local_4b_watch_score":4,"hard_4c_or_high_mae_penalty":3,"stage2_actionable_bonus":2},"weighted_score_before":63,"stage_label_before":"Stage2-Actionable_or_4B-Watch","raw_component_scores_after":{"price_or_event_score":4,"source_bridge_score":0,"relative_strength_score":5,"local_4b_watch_score":9,"hard_4c_or_high_mae_penalty":15,"stage2_actionable_bonus":0},"weighted_score_after":38,"stage_label_after":"4C-Hard","changed_components":["price_or_event_score","source_bridge_score","relative_strength_score","local_4b_watch_score","hard_4c_or_high_mae_penalty","stage2_actionable_bonus"],"component_delta_explanation":"R13 4B/4C guard separates local/full-window price peaks from positive Stage3 evidence and routes hard thesis breaks to 4C.","MFE_90D_pct":41.67,"MAE_90D_pct":-59.56,"score_return_alignment_label":"score_return_misaligned","current_profile_verdict":"current_profile_false_positive_without_hard_4C"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R13L72_4B4C_C27_263750_20210826_TRAILER_IP_MFE_BUT_NO_GREEN","trigger_id":"TRG_R13L72_4B4C_C27_263750_20210826_TRAILER_IP_MFE_BUT_NO_GREEN","symbol":"263750","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_4B_4C_REDTEAM","source_canonical_archetype_id":"C27_CONTENT_IP_GLOBAL_MONETIZATION","raw_component_scores_before":{"price_or_event_score":11,"source_bridge_score":3,"relative_strength_score":11,"local_4b_watch_score":4,"hard_4c_or_high_mae_penalty":3,"stage2_actionable_bonus":2},"weighted_score_before":63,"stage_label_before":"Stage2-Actionable_or_4B-Watch","raw_component_scores_after":{"price_or_event_score":4,"source_bridge_score":0,"relative_strength_score":5,"local_4b_watch_score":9,"hard_4c_or_high_mae_penalty":12,"stage2_actionable_bonus":0},"weighted_score_after":42,"stage_label_after":"Stage1-Watch_or_4B-HighMAE-Guard","changed_components":["price_or_event_score","source_bridge_score","relative_strength_score","local_4b_watch_score","hard_4c_or_high_mae_penalty","stage2_actionable_bonus"],"component_delta_explanation":"R13 4B/4C guard separates local/full-window price peaks from positive Stage3 evidence and routes hard thesis breaks to 4C.","MFE_90D_pct":65.19,"MAE_90D_pct":-17.97,"score_return_alignment_label":"score_return_mixed","current_profile_verdict":"current_profile_partially_false_positive_if_green"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R13L72_4B4C_C32_241560_20240712_GOVERNANCE_RATIO_LOCAL_4B_HIGH_MAE","trigger_id":"TRG_R13L72_4B4C_C32_241560_20240712_GOVERNANCE_RATIO_LOCAL_4B_HIGH_MAE","symbol":"241560","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_4B_4C_REDTEAM","source_canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","raw_component_scores_before":{"price_or_event_score":11,"source_bridge_score":2,"relative_strength_score":11,"local_4b_watch_score":4,"hard_4c_or_high_mae_penalty":3,"stage2_actionable_bonus":2},"weighted_score_before":63,"stage_label_before":"Stage2-Actionable_or_4B-Watch","raw_component_scores_after":{"price_or_event_score":4,"source_bridge_score":0,"relative_strength_score":5,"local_4b_watch_score":9,"hard_4c_or_high_mae_penalty":12,"stage2_actionable_bonus":0},"weighted_score_after":42,"stage_label_after":"Stage1-Watch_or_4B-HighMAE-Guard","changed_components":["price_or_event_score","source_bridge_score","relative_strength_score","local_4b_watch_score","hard_4c_or_high_mae_penalty","stage2_actionable_bonus"],"component_delta_explanation":"R13 4B/4C guard separates local/full-window price peaks from positive Stage3 evidence and routes hard thesis breaks to 4C.","MFE_90D_pct":8.97,"MAE_90D_pct":-38.92,"score_return_alignment_label":"score_return_misaligned","current_profile_verdict":"current_profile_false_positive_without_terms_guard"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R13L72_4B4C_C31_008770_20230810_DUTYFREE_POLICY_LOCAL_4B_HIGH_MAE","trigger_id":"TRG_R13L72_4B4C_C31_008770_20230810_DUTYFREE_POLICY_LOCAL_4B_HIGH_MAE","symbol":"008770","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_4B_4C_REDTEAM","source_canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","raw_component_scores_before":{"price_or_event_score":11,"source_bridge_score":2,"relative_strength_score":11,"local_4b_watch_score":4,"hard_4c_or_high_mae_penalty":3,"stage2_actionable_bonus":2},"weighted_score_before":63,"stage_label_before":"Stage2-Actionable_or_4B-Watch","raw_component_scores_after":{"price_or_event_score":4,"source_bridge_score":0,"relative_strength_score":5,"local_4b_watch_score":9,"hard_4c_or_high_mae_penalty":12,"stage2_actionable_bonus":0},"weighted_score_after":42,"stage_label_after":"Stage1-Watch_or_4B-HighMAE-Guard","changed_components":["price_or_event_score","source_bridge_score","relative_strength_score","local_4b_watch_score","hard_4c_or_high_mae_penalty","stage2_actionable_bonus"],"component_delta_explanation":"R13 4B/4C guard separates local/full-window price peaks from positive Stage3 evidence and routes hard thesis breaks to 4C.","MFE_90D_pct":8.29,"MAE_90D_pct":-33.29,"score_return_alignment_label":"score_return_misaligned","current_profile_verdict":"current_profile_false_positive_without_bridge_guard"}
```

### 18.5 shadow_weight rows

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,r13_cross_4b_price_peak_not_positive_without_source_bridge,cross_archetype_guardrail,L10_POLICY_EVENT_CROSS_REDTEAM_MISC,R13_CROSS_ARCHETYPE_4B_4C_REDTEAM,0,1,+1,"Across C24/C27/C31/C32, local or full-window MFE cannot become Stage3-positive evidence when the source-archetype bridge is absent or broken","4 cross-check rows remain Watch/4B/4C instead of Stage3-Green; no source-archetype independent evidence is added","TRG_R13L72_4B4C_C24_007390_20230331_APPROVAL_EVENT_TO_HARD_4C|TRG_R13L72_4B4C_C27_263750_20210826_TRAILER_IP_MFE_BUT_NO_GREEN|TRG_R13L72_4B4C_C32_241560_20240712_GOVERNANCE_RATIO_LOCAL_4B_HIGH_MAE|TRG_R13L72_4B4C_C31_008770_20230810_DUTYFREE_POLICY_LOCAL_4B_HIGH_MAE",4,0,4,medium,cross_archetype_shadow_only,"R13 rows have do_not_count_as_new_case=true"
shadow_weight,r13_hard_4c_overrides_pre_event_mfe,cross_archetype_guardrail,L10_POLICY_EVENT_CROSS_REDTEAM_MISC,R13_CROSS_ARCHETYPE_4B_4C_REDTEAM,1,1,0,"A binary thesis break should override prior MFE and route to hard 4C when regulatory/terms/economic evidence breaks","007390 validates hard 4C routing; 241560/008770 validate high-MAE watch before hard 4C","TRG_R13L72_4B4C_C24_007390_20230331_APPROVAL_EVENT_TO_HARD_4C|TRG_R13L72_4B4C_C32_241560_20240712_GOVERNANCE_RATIO_LOCAL_4B_HIGH_MAE|TRG_R13L72_4B4C_C31_008770_20230810_DUTYFREE_POLICY_LOCAL_4B_HIGH_MAE",3,0,3,medium,existing_axis_kept,"strengthens hard_4c/high_MAE routing without production delta"
```

### 18.6 residual_contribution row

```jsonl
{"row_type":"residual_contribution","round":"R13","loop":"72","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_4B_4C_REDTEAM","r13_cross_case_count":4,"new_independent_case_count":0,"reused_case_count":4,"new_symbol_count_for_source_archetype":0,"new_trigger_family_count_for_source_archetype":0,"tested_existing_calibrated_axes":["stage2_actionable_evidence_bonus","price_only_blowoff_blocks_positive_stage","full_4b_requires_non_price_evidence","local_4b_watch_guard","high_MAE_guardrail","hard_4c_thesis_break_routes_to_4c"],"residual_error_types_found":["pre_event_MFE_misread_as_positive","large_MFE_without_source_bridge_green_false_positive","local_4B_high_MAE_event_terms_risk","hard_4C_after_binary_event_failure"],"loop_contribution_label":"r13_cross_archetype_4B_4C_redteam","do_not_propose_new_weight_delta":false}
```

## 19. Deferred Coding Agent Handoff Prompt

### Purpose

You are now in the repository implementation phase. The attached Markdown files are v12 post-calibrated residual research outputs produced using the Songdaiki/stock-web OHLC atlas.

These MDs are not live candidate research. They are historical calibration research designed to extend the already-applied e2r_2_1_stock_web_calibrated profile.

Do not blindly apply every shadow row. Ingest the machine-readable rows and update the sector/canonical-archetype calibration ledger.

### R13-specific handling

- R13 cross-case rows must be parsed as trigger rows.
- R13 cross-case rows must keep `do_not_count_as_new_case=true`.
- R13 cross-case rows must not increase source archetype positive/counterexample coverage.
- Use them only for cross-archetype guardrail calibration.
- `independent_evidence_weight=0.0` means no duplicate source evidence.
- R13 `R13_CROSS_ARCHETYPE_4B_4C_REDTEAM` rows should update cross_archetype_shadow_profile only.

### Price source context

- Primary historical price source used by the research MD: Songdaiki/stock-web.
- Price basis: tradable_raw.
- Price adjustment status: raw_unadjusted_marcap.
- Price shard pattern: atlas/ohlcv_tradable_by_symbol_year/<prefix>/<ticker>/<year>.csv.
- Symbol profile pattern: atlas/symbol_profiles/<prefix>/<ticker>.json.

### Rules

- Use only calibration_usable=true rows for guardrail diagnostics.
- Do not count R13 cross rows as new source-archetype evidence.
- Do not apply global deltas unless multiple large_sector_id values support the same direction.
- Positive score promotion requires non-price evidence and clean 180D MFE/MAE.
- 4B rows are overlay/risk calibration only.
- 4C rows are thesis-break/protection calibration only.
- price-only/event-only rows cannot promote Stage2/Stage3.
- A hard 4C thesis break overrides prior MFE.
- Production scoring must not change unless the user explicitly asks for another promotion batch.

### Expected repository tasks

1. Parse case / trigger / score_simulation / shadow_weight / residual_contribution rows.
2. Validate stock-web price source fields.
3. Validate R13 canonical_archetype_id.
4. Confirm `do_not_count_as_new_case=true` for every R13 cross row.
5. Deduplicate same_entry_group_id.
6. Aggregate only under R13 guardrail, not source archetype coverage.
7. Update cross_archetype_shadow_profile only.
8. Preserve global calibrated profile unless explicitly promoted.
9. Report cross-case count, counterexamples, 4B watch rows, hard 4C rows, and residual error types.
10. Add tests that R13 rows cannot change source archetype independent coverage.
11. Add tests that prior MFE cannot block hard 4C routing after a thesis break.

### Expected output

- Concise implementation summary.
- Rows accepted/rejected.
- R13 4B/4C guardrail coverage.
- Existing axis strengthened/weakened/kept.
- No investment recommendation language.

## 20. Next Round State

```text
completed_round = R13
completed_loop = 72
next_round = R1
next_loop = 73
round_schedule_status = valid
round_sector_consistency = pass
```

## 21. Source Notes

```text
MAIN EXECUTION PROMPT:
docs/core/e2r_v12_prompt_round_scheduler_corrected.txt

NO-REPEAT INDEX:
docs/core/V12_Research_No_Repeat_Index.md

Stock-web:
atlas/manifest.json
atlas/schema.json
atlas/symbol_profiles/007/007390.json
atlas/symbol_profiles/263/263750.json
atlas/symbol_profiles/241/241560.json
atlas/symbol_profiles/008/008770.json
atlas/ohlcv_tradable_by_symbol_year/007/007390/2023.csv
atlas/ohlcv_tradable_by_symbol_year/263/263750/2021.csv
atlas/ohlcv_tradable_by_symbol_year/263/263750/2022.csv
atlas/ohlcv_tradable_by_symbol_year/241/241560/2024.csv
atlas/ohlcv_tradable_by_symbol_year/008/008770/2023.csv
```

This loop completes R13 / loop 72 and moves the scheduler to R1 / loop 73.
