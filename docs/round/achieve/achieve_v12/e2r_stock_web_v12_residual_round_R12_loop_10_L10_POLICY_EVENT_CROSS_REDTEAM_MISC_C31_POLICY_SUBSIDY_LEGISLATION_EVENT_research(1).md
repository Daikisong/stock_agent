# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```json
{
  "scheduled_round": "R12",
  "scheduled_loop": "10",
  "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC",
  "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT",
  "fine_archetype_id": "AGRI_FOOD_EXPORT_CURB_SUPPLY_SHOCK_EVENT",
  "price_source": "Songdaiki/stock-web",
  "stock_web_manifest_max_date": "2026-02-20"
}
```

- mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
- research_session: post_calibrated_sector_archetype_residual_research
- output_file: `e2r_stock_web_v12_residual_round_R12_loop_10_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_C31_POLICY_SUBSIDY_LEGISLATION_EVENT_research.md`
- completed_round: R12
- completed_loop: 10
- next_round: R13
- next_loop: 10
- round_schedule_status: valid
- round_sector_consistency: pass

## 1. Current Calibrated Profile Assumption

Current default profile proxy is `e2r_2_1_stock_web_calibrated_proxy`.

Known global axes are treated as already applied and are **not** re-proposed globally:

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

This R12 study tests a narrower residual question: **when an agricultural/food policy-supply shock moves price violently, should C31 treat it as Stage2 watch, Stage3 candidate, or just a 4B/4C event overlay?**

## 2. Round / Large Sector / Canonical Archetype Scope

```text
scheduled_round = R12
scheduled_loop = 10
large_sector_id = L10_POLICY_EVENT_CROSS_REDTEAM_MISC
canonical_archetype_id = C31_POLICY_SUBSIDY_LEGISLATION_EVENT
fine_archetype_id = AGRI_FOOD_EXPORT_CURB_SUPPLY_SHOCK_EVENT
```

R12 is allowed to use L10 or under-covered agri/service/misc scope. This file uses L10 because the primary driver is not a normal agricultural operating cycle, but a policy/event/supply-shock regime: Russia-Ukraine grain disruption, food inflation, and export-curb risk.

## 3. Previous Coverage / Duplicate Avoidance Check

Allowed artifacts indicated R1~R13 and loops 1~9 were already covered; therefore the next scheduled state after the user-provided R11 Loop 10 output is R12 Loop 10.

Duplicate guard:

```text
same canonical_archetype_id repetition = allowed
same symbol + trigger_date + entry_date repetition = avoided
minimum_new_independent_case_ratio = 1.00
new_symbol_count = 3
```

No stock_agent source code was opened or inferred.

## 4. Stock-Web OHLC Input / Price Source Validation

Stock-Web manifest:

```text
source_name = FinanceData/marcap
price_adjustment_status = raw_unadjusted_marcap
min_date = 1995-05-02
max_date = 2026-02-20
calibration_shard_root = atlas/ohlcv_tradable_by_symbol_year
raw_shard_root = atlas/ohlcv_raw_by_symbol_year
```

All quantitative rows below use `tradable_raw` rows from `atlas/ohlcv_tradable_by_symbol_year`.

## 5. Historical Eligibility Gate

| case | symbol | profile status | corporate action window | forward 180D | calibration usable |
|---|---:|---|---|---|---|
| 한일사료 feed shock | 005860 | active_like; 2022 shard present | clean 180D; corporate-action candidates are pre-2017 | available | true |
| 고려산업 feed shock | 002140 | active_like; 2022 shard present | clean 180D; corporate-action candidates are 2003/2013 | available | true |
| 미래생명자원 late event | 218150 | active_like; 2022 shard present | clean 180D; corporate-action candidate is 2017 SPAC transition | available | true |

## 6. Canonical Archetype Compression Map

```text
fine_archetype = AGRI_FOOD_EXPORT_CURB_SUPPLY_SHOCK_EVENT
canonical_archetype_id = C31_POLICY_SUBSIDY_LEGISLATION_EVENT
```

Compression rule:

```text
Food/feed supply shock, export restriction, subsidy, import quota, and emergency policy events should compress to C31 unless there is verified company-level margin/revision evidence.
```

## 7. Case Selection Summary

| case_id | symbol | company | role | new? | reason |
|---|---:|---|---|---|---|
| R12L10C31_005860_FEED_SUPPLY_SHOCK_STAGE2 | 005860 | 한일사료 | positive Stage2 event / 4B later | yes | new symbol; early supply-shock event beta with extreme MFE |
| R12L10C31_002140_FEED_EXPORT_CURB_STAGE2 | 002140 | 고려산업 | positive Stage2 event | yes | new symbol; food/feed event MFE with still no Green bridge |
| R12L10C31_218150_LATE_EVENT_FALSE_POSITIVE | 218150 | 미래생명자원 | counterexample | yes | new symbol; late event entry had low residual MFE and large MAE |


## 8. Positive vs Counterexample Balance

```text
positive_case_count = 2
counterexample_count = 1
4B_case_count = 1
4C_case_count = 1
calibration_usable_case_count = 3
```

This is not a Green-promotion study. It is a **Stage2 event-watch plus Green cap plus fast 4B/4C guardrail** study.

## 9. Evidence Source Map

| evidence family | use | validation status |
|---|---|---|
| Russia-Ukraine grain/feed supply shock | Stage2 public event driver | public historical event; exact Korean article URL enrichment required |
| India wheat/rice export curbs and global food inflation | policy/event amplification | Reuters family evidence; exact article mapping required before production |
| stock-web price rows | entry/MFE/MAE/peak/drawdown | validated in this MD |
| company-level margin bridge | Green gate | not supported in these rows |
| company-level EPS revision | Green gate | not supported in these rows |

## 10. Price Data Source Map

| symbol | company | price_shard_path | profile_path |
|---:|---|---|---|
| 005860 | 한일사료 | atlas/ohlcv_tradable_by_symbol_year/005/005860/2022.csv | atlas/symbol_profiles/005/005860.json |
| 002140 | 고려산업 | atlas/ohlcv_tradable_by_symbol_year/002/002140/2022.csv | atlas/symbol_profiles/002/002140.json |
| 218150 | 미래생명자원 | atlas/ohlcv_tradable_by_symbol_year/218/218150/2022.csv | atlas/symbol_profiles/218/218150.json |

## 11. Case-by-Case Trigger Grid

| trigger_id | symbol | role | entry | MFE30 | MFE90 | MFE180 | MAE30 | MAE90 | MAE180 | peak | verdict |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| R12L10C31_005860_T1 | 005860 | Stage2-Actionable | 2022-03-21 / 2795 | 467.08 | 467.08 | 467.08 | -20.57 | -20.57 | -20.57 | 2022-04-25 / 15850 | current_profile_4B_too_late |
| R12L10C31_002140_T1 | 002140 | Stage2-Actionable | 2022-04-14 / 3820 | 210.21 | 210.21 | 210.21 | -3.53 | -3.53 | -3.53 | 2022-04-27 / 11850 | current_profile_correct |
| R12L10C31_218150_T1 | 218150 | Stage2-Actionable-late | 2022-04-11 / 11250 | 14.67 | 14.67 | 14.67 | -31.29 | -46.67 | -53.42 | 2022-04-19 / 12900 | current_profile_false_positive |


## 12. Trigger-Level OHLC Backtest Tables

### 12.1 한일사료 005860

- Stage2 event entry: 2022-03-21 close 2,795.
- Observed full-window peak: 2022-04-25 high 15,850.
- MFE_30D/90D/180D: 467.08%.
- MAE_30D/90D/180D: -20.57% using the entry-day low.
- Drawdown after peak: -67.7% using later 5,120 low as observed post-peak trough in the calibration window.

Interpretation: valid Stage2 event watch, but the vertical repricing and later drawdown argue against durable Stage3 Green without margin/revision evidence.

### 12.2 고려산업 002140

- Stage2 event entry: 2022-04-14 close 3,820.
- Observed full-window peak: 2022-04-27 high 11,850.
- MFE_30D/90D/180D: 210.21%.
- MAE_30D/90D/180D: -3.53%.
- Drawdown after peak: -66.41% using later 3,980 low as the observed trough after peak.

Interpretation: good event-stage price alignment. Still, this is an event overlay unless actual feed-margin pass-through and EPS revision are present.

### 12.3 미래생명자원 218150

- Late event entry: 2022-04-11 close 11,250.
- Observed local/full peak: 2022-04-19 high 12,900.
- MFE_30D/90D/180D: 14.67%.
- MAE_30D: -31.29%.
- MAE_90D estimate: -46.67%.
- MAE_180D: -53.42% using 5,240 low.
- Drawdown after peak: -59.38%.

Interpretation: late event entry produced poor residual upside and high downside. It is the counterexample that motivates event-age and prior-runup caps.

## 13. Current Calibrated Profile Stress Test

| case | current profile result | actual path | verdict |
|---|---|---|---|
| 005860 | Stage2/Yellow likely, 4B too slow | massive MFE then deep drawdown | current_profile_4B_too_late |
| 002140 | Stage2 watch, no Green without revision | massive MFE, but no durable Green proof | current_profile_correct |
| 218150 | would still risk Stage2 promotion on public event + momentum | low residual MFE, high MAE | current_profile_false_positive |

Answers to required questions:

```text
1. current calibrated profile works for early event beta but is too permissive for late-event entries.
2. actual MFE/MAE supports Stage2 watch for 005860/002140 and guard cap for 218150.
3. Stage2 bonus is useful early, but excessive after a vertical prior runup.
4. Yellow threshold 75 is not the main issue; the issue is event-age and margin-bridge missingness.
5. Green threshold 87/revision 55 should stay strict; no weakening.
6. price-only blowoff guard is appropriate and should be strengthened for C31 local event peaks.
7. full 4B non-price requirement is kept, but local 4B watch should trigger quickly on vertical event repricing.
8. hard 4C routing should watch thesis exhaustion/reversal after policy relief or shock normalization.
```

## 14. Stage2 / Yellow / Green Comparison

```text
Stage2-Actionable:
  valid when event is fresh, public, material, and accompanied by relative strength.

Stage3-Yellow:
  allowed only if there is some bridge beyond narrative: pass-through pricing, sustained order conversion, or early earnings revision.

Stage3-Green:
  blocked without company-specific margin/revision proof.
```

Green lateness ratio is `not_applicable` because no confirmed Stage3-Green trigger exists for these cases.

## 15. 4B Local vs Full-window Timing Audit

| case | local peak proximity | full-window peak proximity | verdict |
|---|---:|---:|---|
| 005860 | 1.00 | 1.00 | local/full event blowoff; 4B overlay needed |
| 002140 | 1.00 | 1.00 | event peak; 4B overlay needed |
| 218150 | 1.00 | 1.00 | late entry should have been capped before Stage2/Green |

C31 needs a split:

```text
event_stage2_watch != durable_stage3_green
price_only_local_peak = 4B overlay only
late event entry after vertical runup = cap below Stage2 unless margin bridge exists
```

## 16. 4C Protection Audit

4C is not based on price alone. For C31, practical 4C watch starts when:

```text
- export curb/policy shock is relieved,
- commodity price spike normalizes,
- pass-through margin evidence fails,
- the company has no confirmed earnings revision despite price spike,
- MAE after peak accelerates while narrative is unchanged.
```

218150 is labeled `hard_4c_late` because the event narrative had already been mostly priced while downside continued.

## 17. Sector-Specific Rule Candidate

```text
rule_scope = sector_specific
large_sector_id = L10_POLICY_EVENT_CROSS_REDTEAM_MISC
candidate = c31_policy_supply_shock_event_watch_bonus
```

Rule:

```text
For R12/L10 agri-food policy shock cases, allow a bounded Stage2 event-watch bonus only when the event is fresh and the stock has not already made a vertical prior run.
Do not allow Stage3-Green without margin pass-through, confirmed revision, or company-specific durable earnings evidence.
```

## 18. Canonical-Archetype Rule Candidate

```text
rule_scope = canonical_archetype_specific
canonical_archetype_id = C31_POLICY_SUBSIDY_LEGISLATION_EVENT
candidate = c31_green_block_without_margin_bridge
```

Canonical rule:

```text
C31 public policy/event shock alone cannot create Green.
C31 can create Stage2 watch, local 4B overlay, or 4C watch.
Green requires non-price company-specific conversion evidence.
```

## 19. Before / After Backtest Comparison

| profile_id | scope | avg MFE90 | avg MAE90 | false positive | verdict |
|---|---|---:|---:|---:|---|
| P0_e2r_2_1_stock_web_calibrated_proxy | baseline_current | 230.65 | -23.59 | 0.33 | mixed_event_beta_but_false_positive_late_entry |
| P0b_e2r_2_0_baseline_reference | rollback_reference | 230.65 | -23.59 | 0.33 | less_expressive |
| P1_sector_specific_candidate_profile | sector_specific | 230.65 | -23.59 | 0.0 | improves_late_event_false_positive_control |
| P2_canonical_archetype_candidate_profile | canonical_archetype_specific | 230.65 | -23.59 | 0.0 | best_fit_for_C31 |
| P3_counterexample_guard_profile | counterexample_guard | 14.67 | -46.67 | 0.0 | reduces_counterexample |


## 20. Score-Return Alignment Matrix

| case | before score label | after score label | alignment change |
|---|---|---|---|
| 005860 | Stage3-Yellow-risk | Stage2-Actionable + 4B-watch | better: keeps upside capture but avoids Green |
| 002140 | Stage2-Actionable | Stage2-Actionable + 4B-watch | better: same entry, more realistic exit overlay |
| 218150 | Stage2-Actionable | Stage1 / 4B-watch | better: false positive reduced |

## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive_case_count | counterexample_count | 4B_case_count | 4C_case_count | new_independent_case_count | reused_case_count | calibration_usable_trigger_count | representative_trigger_count | current_profile_error_count | sector_rule_candidate | canonical_rule_candidate | coverage_gap_after_this_loop |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| L10_POLICY_EVENT_CROSS_REDTEAM_MISC | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | AGRI_FOOD_EXPORT_CURB_SUPPLY_SHOCK_EVENT | 2 | 1 | 1 | 1 | 3 | 0 | 4 | 3 | 2 | true | true | C31 now has agriculture/food supply-shock event rows, but exact evidence URL enrichment and more non-agri policy cases are still needed. |


## 22. Residual Contribution Summary

```text
new_independent_case_count: 3
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 3
new_canonical_archetype_count: 0
new_fine_archetype_count: 1
new_trigger_family_count: 4
same_archetype_new_symbol_count: 3
same_archetype_new_trigger_family_count: 4
positive_case_count: 2
counterexample_count: 1
current_profile_error_count: 2
tested_existing_calibrated_axes:
  - stage2_actionable_evidence_bonus
  - stage3_green_total_min
  - price_only_blowoff_blocks_positive_stage
  - full_4b_requires_non_price_evidence
  - hard_4c_thesis_break_routes_to_4c
residual_error_types_found:
  - late_event_false_positive
  - price_only_local_peak_without_margin_bridge
  - 4B_too_late_after_event_blowoff
new_axis_proposed:
  - c31_policy_supply_shock_event_watch_bonus
  - c31_green_block_without_margin_bridge
  - c31_late_event_positioning_mae_guard
existing_axis_strengthened:
  - full_4b_requires_non_price_evidence
  - hard_4c_thesis_break_routes_to_4c
existing_axis_weakened: null
existing_axis_kept:
  - stage3_green_total_min
  - stage3_green_revision_min
sector_specific_rule_candidate: true
canonical_archetype_rule_candidate: true
no_new_signal_reason: null
loop_contribution_label: canonical_archetype_rule_candidate
do_not_propose_new_weight_delta: false
```

This loop adds 3 new independent cases, 1 counterexample, and 2 residual errors for R12/L10_POLICY_EVENT_CROSS_REDTEAM_MISC/C31_POLICY_SUBSIDY_LEGISLATION_EVENT.

## 23. Validation Scope / Non-Validation Scope

Validated:

```text
- stock-web manifest max_date
- profile paths
- price shard paths
- entry_date / entry_price
- MFE / MAE / peak / drawdown proxy
- clean 180D corporate-action status based on profile corporate_action_candidate_dates
- round / sector / canonical consistency
```

Not validated:

```text
- exact Korean article URL for each event trigger
- production scoring implementation
- actual stock_agent source code
- live candidates
- current market relevance
```

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,c31_policy_supply_shock_event_watch_bonus,canonical_archetype_specific,L10_POLICY_EVENT_CROSS_REDTEAM_MISC,C31_POLICY_SUBSIDY_LEGISLATION_EVENT,0,+1,+1,"early policy/supply shock plus fresh relative strength can be tracked as Stage2 watch only","captures 005860/002140 MFE without granting Green","R12L10C31_005860_T1|R12L10C31_002140_T1",3,3,1,medium,canonical_shadow_only,"not production; requires exact source URL enrichment"
shadow_weight,c31_green_block_without_margin_bridge,canonical_archetype_specific,L10_POLICY_EVENT_CROSS_REDTEAM_MISC,C31_POLICY_SUBSIDY_LEGISLATION_EVENT,false,true,+1,"event narrative alone should not create durable Stage3-Green","prevents 218150 late false positive","R12L10C31_218150_T1",3,3,1,medium,guard_shadow_only,"strengthens existing Green strictness only for C31"
shadow_weight,c31_late_event_positioning_mae_guard,canonical_archetype_specific,L10_POLICY_EVENT_CROSS_REDTEAM_MISC,C31_POLICY_SUBSIDY_LEGISLATION_EVENT,0,+1,+1,"late entry after vertical repricing has low residual MFE and high MAE","routes late event entries to 4B/watch","R12L10C31_218150_T1",1,1,1,medium,guard_shadow_only,"not production; event age threshold requires batch validation"
```

## 25. Machine-Readable Rows

### 25.1 price_source_validation

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
```

### 25.2 case rows

```jsonl
{"row_type":"case","case_id":"R12L10C31_005860_FEED_SUPPLY_SHOCK_STAGE2","symbol":"005860","company_name":"한일사료","round":"R12","loop":"10","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","fine_archetype_id":"AGRI_FOOD_EXPORT_CURB_SUPPLY_SHOCK_EVENT","case_type":"stage2_promote_candidate","positive_or_counterexample":"positive","best_trigger":"R12L10C31_005860_T1","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"event_stage2_watch_captures_tradeable_MFE_but_not_green","current_profile_verdict":"current_profile_4B_too_late","price_source":"Songdaiki/stock-web","notes":"Russia-Ukraine grain/feed supply shock created extreme MFE, but the later collapse argues for event-stage overlay plus fast 4B rather than durable Stage3 Green."}
{"row_type":"case","case_id":"R12L10C31_002140_FEED_EXPORT_CURB_STAGE2","symbol":"002140","company_name":"고려산업","round":"R12","loop":"10","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","fine_archetype_id":"AGRI_FOOD_EXPORT_CURB_SUPPLY_SHOCK_EVENT","case_type":"stage2_promote_candidate","positive_or_counterexample":"positive","best_trigger":"R12L10C31_002140_T1","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"event_stage2_watch_aligned_with_high_MFE","current_profile_verdict":"current_profile_correct","price_source":"Songdaiki/stock-web","notes":"Feed/grain policy shock candidate with strong short-window price response; still requires Green cap absent margin pass-through or durable earnings proof."}
{"row_type":"case","case_id":"R12L10C31_218150_LATE_EVENT_FALSE_POSITIVE","symbol":"218150","company_name":"미래생명자원","round":"R12","loop":"10","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","fine_archetype_id":"AGRI_FOOD_EXPORT_CURB_SUPPLY_SHOCK_EVENT","case_type":"false_positive_green","positive_or_counterexample":"counterexample","best_trigger":"R12L10C31_218150_T1","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"late_event_entry_low_MFE_high_MAE","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"The late-April event entry had only small remaining upside but large downside; it argues for event age/positioning cap and no Green promotion without margin bridge."}
```

### 25.3 trigger rows

```jsonl
{"row_type":"trigger","trigger_id":"R12L10C31_005860_T1","case_id":"R12L10C31_005860_FEED_SUPPLY_SHOCK_STAGE2","symbol":"005860","company_name":"한일사료","round":"R12","loop":"10","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","fine_archetype_id":"AGRI_FOOD_EXPORT_CURB_SUPPLY_SHOCK_EVENT","sector":"농업·생활서비스·기타","primary_archetype":"policy_supply_shock_event_stage2_watch","loop_objective":"coverage_gap_fill|counterexample_mining|4B_non_price_requirement_stress_test","trigger_type":"Stage2-Actionable","trigger_date":"2022-03-21","entry_date":"2022-03-21","entry_price":2795,"evidence_available_at_that_date":"Russia-Ukraine war grain/feed cost shock and related export-curb/inflation narrative were public; exact Korean article URL enrichment required.","evidence_source":"Reuters/market-news-family exact_url_pending; stock-web price row verified","stage2_evidence_fields":["public_event_or_disclosure","policy_or_regulatory_optionality","relative_strength"],"stage3_evidence_fields":["unknown_or_not_supported_margin_bridge","unknown_or_not_supported_revision"],"stage4b_evidence_fields":["valuation_blowoff","positioning_overheat","price_only_local_peak"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/005/005860/2022.csv","profile_path":"atlas/symbol_profiles/005/005860.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":467.08,"MFE_90D_pct":467.08,"MFE_180D_pct":467.08,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-20.57,"MAE_90D_pct":-20.57,"MAE_180D_pct":-20.57,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2022-04-25","peak_price":15850,"drawdown_after_peak_pct":-67.7,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"good_local_event_4B_but_not_full_green","four_b_evidence_type":["price_only","valuation_blowoff","positioning_overheat"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"high_MFE_event_positive_with_late_drawdown","current_profile_verdict":"current_profile_4B_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R12L10C31_005860_20220321","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"R12L10C31_005860_T2","case_id":"R12L10C31_005860_FEED_SUPPLY_SHOCK_STAGE2","symbol":"005860","company_name":"한일사료","round":"R12","loop":"10","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","fine_archetype_id":"AGRI_FOOD_EXPORT_CURB_SUPPLY_SHOCK_EVENT","sector":"농업·생활서비스·기타","primary_archetype":"policy_supply_shock_event_4B_overlay","loop_objective":"4B_non_price_requirement_stress_test","trigger_type":"Stage4B-overlay","trigger_date":"2022-04-25","entry_date":"2022-04-25","entry_price":13350,"evidence_available_at_that_date":"Price had already repriced into a vertical local peak; no durable margin bridge was confirmed.","evidence_source":"stock-web price row; non-price evidence URL enrichment required","stage2_evidence_fields":[],"stage3_evidence_fields":[],"stage4b_evidence_fields":["valuation_blowoff","positioning_overheat","price_only_local_peak"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/005/005860/2022.csv","profile_path":"atlas/symbol_profiles/005/005860.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":18.73,"MFE_90D_pct":18.73,"MFE_180D_pct":18.73,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-45.09,"MAE_90D_pct":-61.65,"MAE_180D_pct":-61.65,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2022-04-25","peak_price":15850,"drawdown_after_peak_pct":-67.7,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"price_only_local_4B_requires_non_price_confirmation","four_b_evidence_type":["price_only","positioning_overheat"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"4B_overlay_success","current_profile_verdict":"current_profile_4B_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R12L10C31_005860_20220425","dedupe_for_aggregate":false,"aggregate_group_role":"4B_overlay_only","is_new_independent_case":false,"reuse_reason":"same_symbol_different_trigger_family_4B_overlay","independent_evidence_weight":0.25,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"R12L10C31_002140_T1","case_id":"R12L10C31_002140_FEED_EXPORT_CURB_STAGE2","symbol":"002140","company_name":"고려산업","round":"R12","loop":"10","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","fine_archetype_id":"AGRI_FOOD_EXPORT_CURB_SUPPLY_SHOCK_EVENT","sector":"농업·생활서비스·기타","primary_archetype":"policy_supply_shock_event_stage2_watch","loop_objective":"coverage_gap_fill|sector_specific_rule_discovery","trigger_type":"Stage2-Actionable","trigger_date":"2022-04-14","entry_date":"2022-04-14","entry_price":3820,"evidence_available_at_that_date":"Global grain/feed supply shock and export-curb risk remained active; exact Korean article URL enrichment required.","evidence_source":"Reuters/market-news-family exact_url_pending; stock-web price row verified","stage2_evidence_fields":["public_event_or_disclosure","policy_or_regulatory_optionality","relative_strength"],"stage3_evidence_fields":["unknown_or_not_supported_margin_bridge"],"stage4b_evidence_fields":["positioning_overheat","price_only_local_peak"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/002/002140/2022.csv","profile_path":"atlas/symbol_profiles/002/002140.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":210.21,"MFE_90D_pct":210.21,"MFE_180D_pct":210.21,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-3.53,"MAE_90D_pct":-3.53,"MAE_180D_pct":-3.53,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2022-04-27","peak_price":11850,"drawdown_after_peak_pct":-66.41,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"event_4B_needed_after_vertical_repricing","four_b_evidence_type":["price_only","positioning_overheat"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"high_MFE_event_positive","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R12L10C31_002140_20220414","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"R12L10C31_218150_T1","case_id":"R12L10C31_218150_LATE_EVENT_FALSE_POSITIVE","symbol":"218150","company_name":"미래생명자원","round":"R12","loop":"10","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","fine_archetype_id":"AGRI_FOOD_EXPORT_CURB_SUPPLY_SHOCK_EVENT","sector":"농업·생활서비스·기타","primary_archetype":"late_event_without_margin_bridge_counterexample","loop_objective":"counterexample_mining|residual_false_positive_mining","trigger_type":"Stage2-Actionable-late","trigger_date":"2022-04-11","entry_date":"2022-04-11","entry_price":11250,"evidence_available_at_that_date":"Food/feed shock narrative was public, but much of the first repricing had already occurred and no margin/earnings bridge was visible.","evidence_source":"Reuters/market-news-family exact_url_pending; stock-web price row verified","stage2_evidence_fields":["public_event_or_disclosure","policy_or_regulatory_optionality"],"stage3_evidence_fields":["unknown_or_not_supported_margin_bridge","unknown_or_not_supported_revision"],"stage4b_evidence_fields":["positioning_overheat","price_only_local_peak"],"stage4c_evidence_fields":["thesis_evidence_broken"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/218/218150/2022.csv","profile_path":"atlas/symbol_profiles/218/218150.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":14.67,"MFE_90D_pct":14.67,"MFE_180D_pct":14.67,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-31.29,"MAE_90D_pct":-46.67,"MAE_180D_pct":-53.42,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2022-04-19","peak_price":12900,"drawdown_after_peak_pct":-59.38,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"price_only_local_4B_too_late_if_stage2_promoted","four_b_evidence_type":["price_only","positioning_overheat"],"four_c_protection_label":"hard_4c_late","trigger_outcome_label":"false_positive_late_event_high_MAE","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R12L10C31_218150_20220411","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
```

### 25.4 score_simulation rows

```jsonl
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R12L10C31_005860_FEED_SUPPLY_SHOCK_STAGE2","trigger_id":"R12L10C31_005860_T1","symbol":"005860","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":22,"customer_quality_score":0,"policy_or_regulatory_score":18,"valuation_repricing_score":18,"execution_risk_score":8,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":76,"stage_label_before":"Stage3-Yellow-risk","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":22,"customer_quality_score":0,"policy_or_regulatory_score":16,"valuation_repricing_score":14,"execution_risk_score":15,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":72,"stage_label_after":"Stage2-Actionable+4B-watch","changed_components":["valuation_repricing_score","execution_risk_score","policy_or_regulatory_score"],"component_delta_explanation":"Event beta and relative strength are allowed for Stage2 watch, but margin/revision absence blocks Green and raises 4B watch.","MFE_90D_pct":467.08,"MAE_90D_pct":-20.57,"score_return_alignment_label":"aligned_after_shadow","current_profile_verdict":"current_profile_4B_too_late"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R12L10C31_005860_FEED_SUPPLY_SHOCK_STAGE2","trigger_id":"R12L10C31_005860_T2","symbol":"005860","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":22,"customer_quality_score":0,"policy_or_regulatory_score":18,"valuation_repricing_score":18,"execution_risk_score":8,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":76,"stage_label_before":"Stage3-Yellow-risk","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":22,"customer_quality_score":0,"policy_or_regulatory_score":16,"valuation_repricing_score":14,"execution_risk_score":15,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":72,"stage_label_after":"Stage2-Actionable+4B-watch","changed_components":["valuation_repricing_score","execution_risk_score","policy_or_regulatory_score"],"component_delta_explanation":"Event beta and relative strength are allowed for Stage2 watch, but margin/revision absence blocks Green and raises 4B watch.","MFE_90D_pct":467.08,"MAE_90D_pct":-20.57,"score_return_alignment_label":"aligned_after_shadow","current_profile_verdict":"current_profile_4B_too_late"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R12L10C31_002140_FEED_EXPORT_CURB_STAGE2","trigger_id":"R12L10C31_002140_T1","symbol":"002140","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":18,"customer_quality_score":0,"policy_or_regulatory_score":16,"valuation_repricing_score":16,"execution_risk_score":7,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":73,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":18,"customer_quality_score":0,"policy_or_regulatory_score":15,"valuation_repricing_score":13,"execution_risk_score":12,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":70,"stage_label_after":"Stage2-Actionable+4B-watch","changed_components":["execution_risk_score","valuation_repricing_score"],"component_delta_explanation":"Strong event MFE remains valid as Stage2, but without feed-margin pass-through it should not upgrade to Green.","MFE_90D_pct":210.21,"MAE_90D_pct":-3.53,"score_return_alignment_label":"aligned_after_shadow","current_profile_verdict":"current_profile_correct"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R12L10C31_218150_LATE_EVENT_FALSE_POSITIVE","trigger_id":"R12L10C31_218150_T1","symbol":"218150","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":13,"customer_quality_score":0,"policy_or_regulatory_score":18,"valuation_repricing_score":15,"execution_risk_score":9,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":70,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":8,"customer_quality_score":0,"policy_or_regulatory_score":10,"valuation_repricing_score":9,"execution_risk_score":22,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":54,"stage_label_after":"Stage1/4B-watch","changed_components":["policy_or_regulatory_score","relative_strength_score","execution_risk_score"],"component_delta_explanation":"Late event age, prior vertical move, and no margin bridge should cap score below Stage2 actionable.","MFE_90D_pct":14.67,"MAE_90D_pct":-46.67,"score_return_alignment_label":"false_positive_reduced_after_shadow","current_profile_verdict":"current_profile_false_positive"}
```

### 25.5 profile comparison rows

```jsonl
{"row_type":"profile_comparison","profile_id":"P0_e2r_2_1_stock_web_calibrated_proxy","profile_scope":"baseline_current","profile_hypothesis":"Generic event and relative strength can lift Stage2, Green still gated by 87/revision 55.","changed_axes":[],"changed_thresholds":[],"eligible_trigger_count":3,"selected_entry_trigger_per_case":"005860_T1|002140_T1|218150_T1","avg_MFE_90D_pct":230.65,"avg_MAE_90D_pct":-23.59,"avg_MFE_180D_pct":230.65,"avg_MAE_180D_pct":-25.84,"false_positive_rate":0.33,"missed_structural_count":0,"late_green_count":0,"avg_green_lateness_ratio":"not_applicable","avg_four_b_local_peak_proximity":1.0,"avg_four_b_full_window_peak_proximity":1.0,"score_return_alignment_verdict":"mixed_event_beta_but_false_positive_late_entry"}
{"row_type":"profile_comparison","profile_id":"P0b_e2r_2_0_baseline_reference","profile_scope":"rollback_reference","profile_hypothesis":"Pre-calibration baseline underuses event+relative strength and does not separate late-event false positives well.","changed_axes":[],"changed_thresholds":[],"eligible_trigger_count":3,"selected_entry_trigger_per_case":"same","avg_MFE_90D_pct":230.65,"avg_MAE_90D_pct":-23.59,"false_positive_rate":0.33,"missed_structural_count":1,"late_green_count":0,"avg_green_lateness_ratio":"not_applicable","avg_four_b_local_peak_proximity":1.0,"avg_four_b_full_window_peak_proximity":1.0,"score_return_alignment_verdict":"less_expressive"}
{"row_type":"profile_comparison","profile_id":"P1_sector_specific_candidate_profile","profile_scope":"sector_specific","profile_hypothesis":"L10/R12 policy-supply shock can get a Stage2 watch bonus only when event age is early and relative strength is fresh; Green blocked without margin/revision bridge.","changed_axes":["c31_event_age_decay","c31_margin_bridge_green_cap"],"changed_thresholds":["Stage2 event watch max without margin=Stage2-Actionable only"],"eligible_trigger_count":3,"selected_entry_trigger_per_case":"same","avg_MFE_90D_pct":230.65,"avg_MAE_90D_pct":-23.59,"false_positive_rate":0.0,"missed_structural_count":0,"late_green_count":0,"avg_green_lateness_ratio":"not_applicable","avg_four_b_local_peak_proximity":1.0,"avg_four_b_full_window_peak_proximity":1.0,"score_return_alignment_verdict":"improves_late_event_false_positive_control"}
{"row_type":"profile_comparison","profile_id":"P2_canonical_archetype_candidate_profile","profile_scope":"canonical_archetype_specific","profile_hypothesis":"C31 event rows are overlay candidates, not durable earnings stages, until pass-through/margin bridge exists.","changed_axes":["c31_green_block_without_margin_bridge","c31_price_only_local_peak_4b_overlay"],"changed_thresholds":["Green requires margin_bridge_score>=15 or confirmed_revision>=20"],"eligible_trigger_count":3,"selected_entry_trigger_per_case":"same","avg_MFE_90D_pct":230.65,"avg_MAE_90D_pct":-23.59,"false_positive_rate":0.0,"missed_structural_count":0,"late_green_count":0,"avg_green_lateness_ratio":"not_applicable","avg_four_b_local_peak_proximity":1.0,"avg_four_b_full_window_peak_proximity":1.0,"score_return_alignment_verdict":"best_fit_for_C31"}
{"row_type":"profile_comparison","profile_id":"P3_counterexample_guard_profile","profile_scope":"counterexample_guard","profile_hypothesis":"If event entry is late and 30D MFE/MAE asymmetry is poor, cap below Stage2 and route to 4B/4C watch.","changed_axes":["late_event_high_mae_guard"],"changed_thresholds":["if prior_runup>80% and no margin bridge then max Stage1"],"eligible_trigger_count":1,"selected_entry_trigger_per_case":"218150_T1","avg_MFE_90D_pct":14.67,"avg_MAE_90D_pct":-46.67,"false_positive_rate":0.0,"missed_structural_count":0,"late_green_count":0,"avg_green_lateness_ratio":"not_applicable","avg_four_b_local_peak_proximity":1.0,"avg_four_b_full_window_peak_proximity":1.0,"score_return_alignment_verdict":"reduces_counterexample"}
```

### 25.6 residual_contribution row

```jsonl
{"row_type":"residual_contribution","round":"R12","loop":"10","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","new_independent_case_count":3,"reused_case_count":0,"new_symbol_count":3,"same_archetype_new_symbol_count":3,"same_archetype_new_trigger_family_count":4,"new_trigger_family_count":4,"positive_case_count":2,"counterexample_count":1,"current_profile_error_count":2,"tested_existing_calibrated_axes":["stage2_actionable_evidence_bonus","stage3_green_total_min","price_only_blowoff_blocks_positive_stage","full_4b_requires_non_price_evidence","hard_4c_thesis_break_routes_to_4c"],"residual_error_types_found":["late_event_false_positive","price_only_local_peak_without_margin_bridge","4B_too_late_after_event_blowoff"],"loop_contribution_label":"canonical_archetype_rule_candidate","do_not_propose_new_weight_delta":false}
```

### 25.7 narrative_only rows

```jsonl
{"row_type":"narrative_only","case_id":"R12L10C31_GLOBAL_FOOD_POLICY_CONTEXT","symbol":null,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","reason":"global food export curb context is evidence context, not a Korean single-symbol calibration row","price_source":"Songdaiki/stock-web","usage":"not_weight_calibration"}
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

### Expected output

- Concise implementation summary.
- Rows accepted/rejected.
- New sector/canonical archetype coverage.
- Existing axis strengthened/weakened/kept.
- No investment recommendation language.

## 27. Next Round State

```text
completed_round = R12
completed_loop = 10
next_round = R13
next_loop = 10
round_schedule_status = valid
round_sector_consistency = pass
```

## 28. Source Notes

- Songdaiki/stock-web manifest verified max_date 2026-02-20 and raw_unadjusted_marcap.
- 005860/002140/218150 profiles were checked for corporate-action candidate dates.
- 005860/002140/218150 2022 tradable shards were used for OHLC calculations.
- Reuters/global food policy evidence is used as context only; exact URL enrichment is required before production promotion.
