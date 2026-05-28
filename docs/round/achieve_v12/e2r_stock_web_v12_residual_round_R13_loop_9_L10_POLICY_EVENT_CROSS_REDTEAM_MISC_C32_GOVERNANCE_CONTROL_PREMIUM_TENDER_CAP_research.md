# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
research_session = post_calibrated_sector_archetype_residual_research
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
round = R13
loop = 9
large_sector_id = L10_POLICY_EVENT_CROSS_REDTEAM_MISC
canonical_archetype_id = C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP
fine_archetype_id = HOSTILE_TENDER_WITH_COUNTER_TENDER_AND_BOARDROOM_CONTEST | FRIENDLY_TENDER_FIXED_PRICE_CAP_AFTER_BIDDING_WAR | GOVERNMENT_PRIVATIZATION_EXPECTATION_WITHOUT_BINDING_PRICE_CAP | PE_TENDER_TO_DELISTING_FORWARD_WINDOW_BLOCKED
output_format = one_standalone_markdown_file
production_scoring_changed = false
shadow_weight_only = true
handoff_prompt_embedded = true
handoff_prompt_executed_now = false
```

This file is historical calibration research only. It is not a live candidate screen, not an investment recommendation, and not a `stock_agent` implementation patch.

## 1. Current Calibrated Profile Assumption

```text
current_default_profile_proxy = e2r_2_1_stock_web_calibrated
previous_baseline_reference = e2r_2_0_baseline
```

Applied global assumptions kept as the starting point:

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

This loop does not re-prove those axes. It stress-tests whether C32 needs a narrower split between open-ended control contests and capped/one-shot control-premium events.

## 2. Round / Large Sector / Canonical Archetype Scope

| field | value |
|---|---|
| round | R13 |
| loop | 9 |
| large_sector_id | L10_POLICY_EVENT_CROSS_REDTEAM_MISC |
| canonical_archetype_id | C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP |
| loop_objective | residual_false_positive_mining; 4B_non_price_requirement_stress_test; 4C_thesis_break_timing_test; canonical_archetype_compression; coverage_gap_fill; counterexample_mining |
| rule_scope_preference | canonical_archetype_specific |
| current_profile_error_target | fixed tender cap / event-only control premium false positives |

## 3. Previous Coverage / Duplicate Avoidance Check

The calibration registry shows repeated R10, R11, R12 and R13 historical calibration files already parsed. R11 policy/event loops appear through loop 8, and R13 cross-redteam loops appear through loop 8. This loop therefore uses `R13 / loop 9` and focuses on C32 rather than reusing the broad R11 policy/geopolitics/disaster bucket.

Duplicate avoidance conclusion:

```text
auto_selected_coverage_gap = C32_governance_control_premium_tender_cap_under_split_from_generic_policy_event
new_independent_case_count = 4
reused_case_count = 0
new_symbol_count = 4
same_archetype_new_symbol_count = 4
same_archetype_new_trigger_family_count = 4
new_canonical_archetype_count = 0
new_trigger_family_count = 4
```

Registry evidence note: `md_registry.jsonl` shows R11 loops 1-8 and R13 loops 1-8 already registered; this file is therefore named as R13 loop 9, not a rematerialization of earlier loops.

## 4. Stock-Web OHLC Input / Price Source Validation

The stock-web manifest used for this loop:

```text
source_name = FinanceData/marcap
source_repo_url = https://github.com/FinanceData/marcap
price_adjustment_status = raw_unadjusted_marcap
min_date = 1995-05-02
max_date = 2026-02-20
tradable_row_count = 14354401
raw_row_count = 15214118
symbol_count = 5414
active_like_symbol_count = 2868
inactive_or_delisted_like_symbol_count = 2546
markets = KONEX | KOSDAQ | KOSDAQ GLOBAL | KOSPI
calibration_shard_root = atlas/ohlcv_tradable_by_symbol_year
raw_shard_root = atlas/ohlcv_raw_by_symbol_year
schema_path = atlas/schema.json
universe_path = atlas/universe/all_symbols.csv
```

Validation:

```text
price_data_source = Songdaiki/stock-web
price_basis = tradable_raw
price_adjustment_status = raw_unadjusted_marcap
stock_web_manifest_max_date = 2026-02-20
validation_status = usable_for_historical_calibration
```

Manifest notes used in this loop: calibration shards are raw/unadjusted; zero-volume and zero-OHLC rows are excluded; corporate-action contaminated windows should be blocked by default.

## 5. Historical Eligibility Gate

| case_id | symbol | entry_date | 180D available by manifest max_date | corporate-action 180D status | calibration_usable |
|---|---:|---:|---:|---|---:|
| C32_010130_20240913_MBK_YOUNGPOONG_TENDER | 010130 | 2024-09-13 | yes | clean_180D_window_not_flagged_in_fetched_profile | true |
| C32_041510_20230307_KAKAO_TENDER_CAP | 041510 | 2023-03-08 | yes | clean_180D_window_not_flagged_in_fetched_profile | true |
| C32_040300_20230308_YTN_PRIVATIZATION_SPIKE | 040300 | 2023-03-08 | yes | clean_180D_window_not_flagged_in_fetched_profile | true |
| C32_048260_20230125_OSSTEM_TENDER_DELISTING | 048260 | narrative_only | not validated | listing/forward-window blocked in this loop | false |

## 6. Canonical Archetype Compression Map

| fine_archetype_id | canonical_archetype_id | compression rule |
|---|---|---|
| HOSTILE_TENDER_WITH_COUNTER_TENDER_AND_BOARDROOM_CONTEST | C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP | positive only when control premium is open-ended and supported by contest escalation |
| FRIENDLY_TENDER_FIXED_PRICE_CAP_AFTER_BIDDING_WAR | C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP | cap guard / 4B overlay, not structural positive |
| GOVERNMENT_PRIVATIZATION_EXPECTATION_WITHOUT_BINDING_PRICE_CAP | C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP | event-only watch; no Stage2/3 promotion without binding buyer/price |
| PE_TENDER_TO_DELISTING_FORWARD_WINDOW_BLOCKED | C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP | narrative-only unless forward 180D stock-web path remains listed/tradable |

## 7. Case Selection Summary

| case_id | symbol | company | role | trigger_family | new_independent | why selected |
|---|---:|---|---|---|---:|---|
| C32_010130_20240913_MBK_YOUNGPOONG_TENDER | 010130 | 고려아연 | structural_success + 4B overlay | hostile tender / counter tender / boardroom contest | true | open-ended control contest produced large MFE with low initial MAE |
| C32_041510_20230307_KAKAO_TENDER_CAP | 041510 | 에스엠 | false_positive_green | fixed tender cap after bidding war | true | entry above/near offer price converted control premium into cap risk |
| C32_040300_20230308_YTN_PRIVATIZATION_SPIKE | 040300 | YTN | failed_rerating | privatization expectation without binding cap | true | event-only control-transfer narrative spiked then mean-reverted |
| C32_048260_20230125_OSSTEM_TENDER_DELISTING | 048260 | 오스템임플란트 | narrative_only | tender-to-delisting | true | documents delisting path but excluded from weight calibration |

## 8. Positive vs Counterexample Balance

```text
positive_case_count = 1
counterexample_count = 3
calibration_usable_case_count = 3
calibration_usable_trigger_count = 4
representative_trigger_count = 3
current_profile_error_count = 3
```

This loop is intentionally counterexample-heavy because the residual error is asymmetric: current scoring can treat “control premium exists” as positive evidence even when the tender price itself is the ceiling.

## 9. Evidence Source Map

| case_id | date | event evidence | source note |
|---|---:|---|---|
| C32_010130_20240913_MBK_YOUNGPOONG_TENDER | 2024-09-13 | MBK Partners and Young Poong tender offer at KRW 660,000/share; Korea Zinc opposed as hostile | Reuters 2024-09-13 |
| C32_010130_20241029_4B_OVERLAY | 2024-10-21 to 2024-10-29 | court rejection of injunction and buyback/control contest escalation; stock-web peak later in October | Reuters 2024-10-21; stock-web OHLC |
| C32_041510_20230307_KAKAO_TENDER_CAP | 2023-03-07 | Kakao tender offer at KRW 150,000/share to acquire up to 35% of SM | AP 2023-03-07 |
| C32_040300_20230308_YTN_PRIVATIZATION_SPIKE | 2023-03-08 | privatization/control-transfer expectation; no binding same-day tender price confirmed in this loop | stock-web OHLC; YTN privatization background |
| C32_048260_20230125_OSSTEM_TENDER_DELISTING | 2023-01-25 | PE tender-to-delisting pattern | narrative only |

## 10. Price Data Source Map

| symbol | shard | profile |
|---:|---|---|
| 010130 | atlas/ohlcv_tradable_by_symbol_year/010/010130/2024.csv; atlas/ohlcv_tradable_by_symbol_year/010/010130/2025.csv | atlas/symbol_profiles/010/010130.json |
| 041510 | atlas/ohlcv_tradable_by_symbol_year/041/041510/2023.csv | atlas/symbol_profiles/041/041510.json |
| 040300 | atlas/ohlcv_tradable_by_symbol_year/040/040300/2023.csv | atlas/symbol_profiles/040/040300.json |
| 048260 | not used for quantitative calibration | narrative only |

## 11. Case-by-Case Trigger Grid

| trigger_id | symbol | type | trigger_date | entry_date | entry_price | evidence split | current_profile_verdict | role |
|---|---:|---|---:|---:|---:|---|---|---|
| T_C32_010130_20240913_STAGE2_ACTIONABLE | 010130 | Stage2-Actionable | 2024-09-13 | 2024-09-13 | 666000 | tender + hostile contest | current_profile_too_late | representative |
| T_C32_010130_20241029_4B_OVERLAY | 010130 | 4B | 2024-10-29 | 2024-10-29 | 1543000 | valuation/control-premium blowoff | current_profile_4B_too_late | 4B_overlay_only |
| T_C32_041510_20230307_STAGE2_CAP_GUARD | 041510 | Stage2-CapGuard | 2023-03-07 | 2023-03-08 | 158500 | fixed tender price cap | current_profile_false_positive | representative |
| T_C32_040300_20230308_STAGE2_EVENT_RUMOR | 040300 | Stage2-EventOnly | 2023-03-08 | 2023-03-08 | 9390 | event-only privatization expectation | current_profile_false_positive | representative |

## 12. Trigger-Level OHLC Backtest Tables

### 12.1 Representative trigger rows

| trigger_id | entry | MFE30 | MAE30 | MFE90 | MAE90 | MFE180 | MAE180 | peak_date | peak_price | drawdown_after_peak |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| T_C32_010130_20240913_STAGE2_ACTIONABLE | 666000 | 131.68 | -1.65 | 131.68 | -1.65 | 131.68 | -3.45 | 2024-10-29 | 1543000 | -58.33 |
| T_C32_041510_20230307_STAGE2_CAP_GUARD | 158500 | 1.70 | -44.73 | 1.70 | -44.73 | 1.70 | -44.73 | 2023-03-08 | 161200 | -45.66 |
| T_C32_040300_20230308_STAGE2_EVENT_RUMOR | 9390 | 11.82 | -36.63 | 11.82 | -36.63 | 11.82 | -39.00 | 2023-03-08 | 10500 | -43.33 |

### 12.2 4B overlay row

| trigger_id | entry | MFE30 | MAE30 | MFE90 | MAE90 | MFE180 | MAE180 | verdict |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| T_C32_010130_20241029_4B_OVERLAY | 1543000 | 0.00 | -46.21 | 0.00 | -54.89 | 0.00 | -58.33 | good_full_window_4B_timing |

## 13. Current Calibrated Profile Stress Test

| case_id | current profile likely label | outcome | verdict | residual error |
|---|---|---|---|---|
| C32_010130_20240913_MBK_YOUNGPOONG_TENDER | Stage3-Yellow, maybe delayed Green because no EPS revision | strong MFE with low initial MAE | current_profile_too_late | open-ended control contest underweighted |
| C32_041510_20230307_KAKAO_TENDER_CAP | Stage2/Yellow risk if control premium overweights event | low MFE / severe MAE | current_profile_false_positive | fixed tender cap treated as upside |
| C32_040300_20230308_YTN_PRIVATIZATION_SPIKE | Stage2 risk if privatization narrative overweights policy optionality | local spike then drawdown | current_profile_false_positive | event-only path lacked binding cap |
| C32_048260_20230125_OSSTEM_TENDER_DELISTING | data insufficient | narrative only | current_profile_data_insufficient | not used |

Answers to the required stress questions:

```text
1. current calibrated profile judgment: too late for open-ended Korea Zinc, too permissive for SM/YTN event-only or capped tender.
2. actual MFE/MAE alignment: positive only in Korea Zinc; SM/YTN false-positive if promoted.
3. Stage2 bonus: too broad in C32 unless capped tender/event-only guard is applied.
4. Yellow threshold 75: not the issue; component semantics are the issue.
5. Green threshold 87/revision 55: too earnings-centric for open-ended control contests, but should not be loosened globally.
6. price-only blowoff guard: kept; should be strengthened by explicit tender-cap semantics.
7. full 4B non-price requirement: kept; fixed tender cap and legal/control contest are non-price 4B evidence.
8. hard 4C routing: kept; route only after tender withdrawal, failed financing, court block, delisting failure, or thesis break.
```

## 14. Stage2 / Yellow / Green Comparison

C32 is not a standard EPS-revision archetype. The residual is not “Green is too late” in general. It is that C32 needs an evidence gate:

```text
if control premium is open-ended and contest is escalating:
    Stage2-Actionable can be early even without earnings revision
else if tender price is fixed and entry trades at/above tender cap:
    positive Stage2/3 must be blocked; treat as 4B/event-cap overlay
else if privatization rumor lacks binding buyer/price:
    narrative_only or watch
```

Green lateness ratio is not applicable because confirmed Stage3-Green triggers were not separately used. This is a canonical-archetype component semantics study, not a Stage3 timing study.

## 15. 4B Local vs Full-window Timing Audit

| trigger_id | four_b_evidence_type | local_peak_proximity | full_window_peak_proximity | verdict |
|---|---|---:|---:|---|
| T_C32_010130_20241029_4B_OVERLAY | valuation_blowoff; positioning_overheat; control_premium_or_event_premium | 1.00 | 1.00 | good_full_window_4B_timing |
| T_C32_041510_20230307_STAGE2_CAP_GUARD | explicit_event_cap; control_premium_or_event_premium | 1.00 | 1.00 | good 4B/cap guard, bad positive-stage trigger |
| T_C32_040300_20230308_STAGE2_EVENT_RUMOR | price_only | 1.00 | 1.00 | price-only local 4B too early unless binding cap appears |

## 16. 4C Protection Audit

| case_id | 4C evidence | label | comment |
|---|---|---|---|
| C32_010130_20240913_MBK_YOUNGPOONG_TENDER | no clean thesis-break at Stage2 entry | thesis_break_watch_only | 4B worked before 4C |
| C32_041510_20230307_KAKAO_TENDER_CAP | tender cap / offer resolution | hard_4c_success_if_failed_offer_resolution_used | cap guard was useful before severe drawdown |
| C32_040300_20230308_YTN_PRIVATIZATION_SPIKE | no binding control thesis | false_break | should remain event-only watch |
| C32_048260_20230125_OSSTEM_TENDER_DELISTING | delisting path | narrative_only | not used |

## 17. Sector-Specific Rule Candidate

```text
sector_specific_rule_candidate = false
```

The evidence is concentrated in one canonical archetype, not enough for a large-sector-wide L10 rule.

## 18. Canonical-Archetype Rule Candidate

```text
canonical_archetype_rule_candidate = true
rule_scope = canonical_archetype_specific
canonical_archetype_id = C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP
```

Proposed C32 shadow rules:

```text
new_axis_proposed:
1. c32_open_ended_control_contest_bonus
   - If tender/control event is hostile or contested and follow-on counter-tender, court, boardroom, or buyback path keeps the premium open-ended, add +6 to +8 C32 control-premium component.
   - This is not a global Stage3 Green relaxation.

2. c32_fixed_tender_cap_guard
   - If entry_price >= tender_price or observed price is within +0~5% of a fixed tender price, block positive Stage2/3 promotion and route to 4B/event-cap overlay.
   - This strengthens full_4b_requires_non_price_evidence inside C32.

3. c32_event_only_privatization_guard
   - If narrative is privatization/sale expectation without binding buyer, binding tender price, financing, regulatory clearance, or mandatory offer, label as narrative_only/watch, not positive Stage2.
```

## 19. Before / After Backtest Comparison

| profile_id | scope | hypothesis | eligible_trigger_count | selected_entry_trigger_per_case | avg_MFE_90D | avg_MAE_90D | false_positive_rate | score_return_alignment |
|---|---|---|---:|---|---:|---:|---:|---|
| P0 | global_current | no C32 cap split | 3 | all 3 promoted risk | 48.40 | -27.67 | 0.67 | misclassifies capped/event-only control premium |
| P0b | baseline_reference | more permissive event promotion | 3 | all 3 promoted risk | 48.40 | -27.67 | 0.67 | worse false-positive risk |
| P1 | sector_specific_candidate | L10 event guard | 3 | broad guard | 48.40 | -27.67 | 0.33 | better but too broad |
| P2 | canonical_archetype_candidate | split open contest vs fixed cap | 3 | 010130 positive; SM/YTN blocked | 131.68 | -1.65 | 0.00 | best alignment |
| P3 | counterexample_guard | fixed cap/event-only cannot promote | 3 | 010130 positive; SM/YTN cap/watch | 131.68 | -1.65 | 0.00 | strong guard |

## 20. Score-Return Alignment Matrix

| case_id | P0 label | P2/P3 label | MFE90 | MAE90 | alignment verdict |
|---|---|---|---:|---:|---|
| C32_010130_20240913_MBK_YOUNGPOONG_TENDER | Stage3-Yellow / late Green | Stage3-Green-shadow | 131.68 | -1.65 | improved |
| C32_041510_20230307_KAKAO_TENDER_CAP | Stage2/Yellow risk | 4B/event-cap overlay | 1.70 | -44.73 | improved |
| C32_040300_20230308_YTN_PRIVATIZATION_SPIKE | Stage2 risk | narrative-only/watch | 11.82 | -36.63 | improved |

## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive_case_count | counterexample_count | 4B_case_count | 4C_case_count | new_independent_case_count | reused_case_count | calibration_usable_trigger_count | representative_trigger_count | current_profile_error_count | sector_rule_candidate | canonical_rule_candidate | coverage_gap_after_this_loop |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| L10_POLICY_EVENT_CROSS_REDTEAM_MISC | C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP | mixed | 1 | 3 | 2 | 1 | 4 | 0 | 4 | 3 | 3 | false | true | still needs 1-2 more positive open-ended contests and one failed hostile-bid 4C |

## 22. Residual Contribution Summary

```text
new_independent_case_count: 4
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 4
same_archetype_new_symbol_count: 4
same_archetype_new_trigger_family_count: 4
new_canonical_archetype_count: 0
new_fine_archetype_count: 4
new_trigger_family_count: 4
tested_existing_calibrated_axes:
  - price_only_blowoff_blocks_positive_stage
  - full_4b_requires_non_price_evidence
  - hard_4c_thesis_break_routes_to_4c
residual_error_types_found:
  - fixed_tender_cap_false_positive
  - privatization_event_only_false_positive
  - control_premium_4b_too_late
new_axis_proposed:
  - c32_open_ended_control_contest_bonus
  - c32_fixed_tender_cap_guard
  - c32_event_only_privatization_guard
existing_axis_strengthened:
  - full_4b_requires_non_price_evidence inside C32
  - price_only_blowoff_blocks_positive_stage inside C32
existing_axis_weakened: null
existing_axis_kept:
  - hard_4c_thesis_break_routes_to_4c
sector_specific_rule_candidate: false
canonical_archetype_rule_candidate: true
no_new_signal_reason: null
loop_contribution_label: canonical_archetype_rule_candidate
do_not_propose_new_weight_delta: false
auto_selected_coverage_gap: C32_governance_control_premium_tender_cap_under_split_from_generic_policy_event
```

## 23. Validation Scope / Non-Validation Scope

Validated:

```text
- Songdaiki/stock-web tradable_raw OHLC snippets for 010130, 041510, 040300.
- Manifest max_date = 2026-02-20.
- 180D windows available by manifest/profile max_date for the three quantitative cases.
- C32 component-level residual rule candidate.
```

Not validated:

```text
- This MD does not patch production code.
- This MD does not run stock_agent live scans.
- This MD does not use brokerage APIs.
- This MD does not claim current investment suitability.
- 1Y/2Y metrics are not used for weight calibration in this loop and are left null in JSONL rows.
```

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,c32_open_ended_control_contest_bonus,canonical_archetype_specific,L10_POLICY_EVENT_CROSS_REDTEAM_MISC,C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP,0,+7,+7,"open-ended hostile/control contest behaved unlike fixed tender cap","selects 010130 as positive and avoids global revision relaxation","T_C32_010130_20240913_STAGE2_ACTIONABLE",3,4,3,medium,canonical_shadow_only,"not production; needs more positives"
shadow_weight,c32_fixed_tender_cap_guard,canonical_archetype_specific,L10_POLICY_EVENT_CROSS_REDTEAM_MISC,C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP,0,+12,+12,"entry at/above fixed tender price produced low MFE and severe MAE","blocks SM false-positive promotion","T_C32_041510_20230307_STAGE2_CAP_GUARD",3,4,3,medium,canonical_shadow_only,"strengthens 4B non-price evidence in C32"
shadow_weight,c32_event_only_privatization_guard,canonical_archetype_specific,L10_POLICY_EVENT_CROSS_REDTEAM_MISC,C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP,0,+8,+8,"privatization narrative without binding buyer/price is not enough","blocks YTN event-only false-positive","T_C32_040300_20230308_STAGE2_EVENT_RUMOR",3,4,3,low,canonical_shadow_only,"needs additional public-sale cases"
```

## 25. Machine-Readable Rows

### 25.1 price_source_validation

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
```

### 25.2 case rows

```jsonl
{"row_type":"case","case_id":"C32_010130_20240913_MBK_YOUNGPOONG_TENDER","symbol":"010130","company_name":"고려아연","round":"R13","loop":"9","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","fine_archetype_id":"HOSTILE_TENDER_WITH_COUNTER_TENDER_AND_BOARDROOM_CONTEST","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"T_C32_010130_20240913_STAGE2_ACTIONABLE","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"strong_positive_alignment","current_profile_verdict":"current_profile_too_late","notes":"Fixed tender price was not the whole story; subsequent hostile/defensive control contest, court/tender escalation and boardroom path made this different from a capped one-shot tender.","price_source":"Songdaiki/stock-web"}
{"row_type":"case","case_id":"C32_041510_20230307_KAKAO_TENDER_CAP","symbol":"041510","company_name":"에스엠","round":"R13","loop":"9","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","fine_archetype_id":"FRIENDLY_TENDER_FIXED_PRICE_CAP_AFTER_BIDDING_WAR","case_type":"false_positive_green","positive_or_counterexample":"counterexample","best_trigger":"T_C32_041510_20230307_STAGE2_CAP_GUARD","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"negative_alignment_if_promoted","current_profile_verdict":"current_profile_false_positive","notes":"Kakao tender offer created a visible control-premium event, but entry already sat above/near the tender cap and then drew down sharply.","price_source":"Songdaiki/stock-web"}
{"row_type":"case","case_id":"C32_040300_20230308_YTN_PRIVATIZATION_SPIKE","symbol":"040300","company_name":"YTN","round":"R13","loop":"9","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","fine_archetype_id":"GOVERNMENT_PRIVATIZATION_EXPECTATION_WITHOUT_BINDING_PRICE_CAP","case_type":"failed_rerating","positive_or_counterexample":"counterexample","best_trigger":"T_C32_040300_20230308_STAGE2_EVENT_RUMOR","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"negative_alignment_if_event_only_promoted","current_profile_verdict":"current_profile_false_positive","notes":"Privatization/control-transfer narrative spiked price without a same-day binding tender price, buyer financing, or immediate mandatory-offer path.","price_source":"Songdaiki/stock-web"}
{"row_type":"case","case_id":"C32_048260_20230125_OSSTEM_TENDER_DELISTING","symbol":"048260","company_name":"오스템임플란트","round":"R13","loop":"9","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","fine_archetype_id":"PE_TENDER_TO_DELISTING_FORWARD_WINDOW_BLOCKED","case_type":"narrative_only","positive_or_counterexample":"counterexample","best_trigger":"N_C32_048260_20230125_TENDER_DELISTING","calibration_usable":false,"is_new_independent_case":true,"reuse_reason":"forward_window_or_listing_status_not_validated_in_this_loop","independent_evidence_weight":0.0,"score_price_alignment":"not_weight_calibration","current_profile_verdict":"current_profile_data_insufficient","notes":"Included only to document a tender-to-delisting path. Not used for quantitative calibration.","price_source":"Songdaiki/stock-web"}
```

### 25.3 trigger rows

```jsonl
{"row_type":"trigger","trigger_id":"T_C32_010130_20240913_STAGE2_ACTIONABLE","case_id":"C32_010130_20240913_MBK_YOUNGPOONG_TENDER","symbol":"010130","company_name":"고려아연","round":"R13","loop":"9","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","fine_archetype_id":"HOSTILE_TENDER_WITH_COUNTER_TENDER_AND_BOARDROOM_CONTEST","sector":"정책·이벤트·지배구조","primary_archetype":"governance_control_premium_tender_cap","loop_objective":"coverage_gap_fill|counterexample_mining|4B_non_price_requirement_stress_test|canonical_archetype_compression","trigger_type":"Stage2-Actionable","trigger_date":"2024-09-13","entry_date":"2024-09-13","entry_price":666000,"evidence_available_at_that_date":"MBK Partners and Young Poong launched a tender offer at KRW 660,000/share; Korea Zinc opposed it as hostile.","evidence_source":"Reuters 2024-09-13; stock-web 010130 2024 shard lines around 2024-09-13","stage2_evidence_fields":["public_event_or_disclosure","policy_or_regulatory_optionality","customer_or_order_quality"],"stage3_evidence_fields":["multiple_public_sources","durable_customer_confirmation"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/010/010130/2024.csv","profile_path":"atlas/symbol_profiles/010/010130.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":131.68,"MFE_90D_pct":131.68,"MFE_180D_pct":131.68,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-1.65,"MAE_90D_pct":-1.65,"MAE_180D_pct":-3.45,"MAE_1Y_pct":null,"below_entry_price_flag_30D":false,"below_entry_price_flag_90D":false,"peak_date":"2024-10-29","peak_price":1543000,"drawdown_after_peak_pct":-58.33,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_4b_entry","four_b_evidence_type":[],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"structural_control_premium_success","current_profile_verdict":"current_profile_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window_not_flagged_in_fetched_profile","same_entry_group_id":"SEG_C32_010130_20240913","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"T_C32_010130_20241029_4B_OVERLAY","case_id":"C32_010130_20240913_MBK_YOUNGPOONG_TENDER","symbol":"010130","company_name":"고려아연","round":"R13","loop":"9","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","fine_archetype_id":"HOSTILE_TENDER_WITH_COUNTER_TENDER_AND_BOARDROOM_CONTEST","sector":"정책·이벤트·지배구조","primary_archetype":"governance_control_premium_tender_cap","loop_objective":"4B_non_price_requirement_stress_test","trigger_type":"4B","trigger_date":"2024-10-29","entry_date":"2024-10-29","entry_price":1543000,"evidence_available_at_that_date":"Control contest had become a full event-premium blowoff; observed price reached the control-premium peak.","evidence_source":"stock-web 010130 2024 shard; Reuters 2024-10-21 court/tender context","stage2_evidence_fields":[],"stage3_evidence_fields":[],"stage4b_evidence_fields":["valuation_blowoff","positioning_overheat","control_premium_or_event_premium"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/010/010130/2024.csv","profile_path":"atlas/symbol_profiles/010/010130.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":0.0,"MFE_90D_pct":0.0,"MFE_180D_pct":0.0,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-46.21,"MAE_90D_pct":-54.89,"MAE_180D_pct":-58.33,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-10-29","peak_price":1543000,"drawdown_after_peak_pct":-58.33,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"good_full_window_4B_timing","four_b_evidence_type":["valuation_blowoff","positioning_overheat","control_premium_or_event_premium"],"four_c_protection_label":"hard_4c_late","trigger_outcome_label":"4B_overlay_success","current_profile_verdict":"current_profile_4B_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window_not_flagged_in_fetched_profile","same_entry_group_id":"SEG_C32_010130_20241029","dedupe_for_aggregate":false,"aggregate_group_role":"4B_overlay_only","is_new_independent_case":false,"reuse_reason":"same_case_new_4B_timing_path","independent_evidence_weight":0.5,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"T_C32_041510_20230307_STAGE2_CAP_GUARD","case_id":"C32_041510_20230307_KAKAO_TENDER_CAP","symbol":"041510","company_name":"에스엠","round":"R13","loop":"9","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","fine_archetype_id":"FRIENDLY_TENDER_FIXED_PRICE_CAP_AFTER_BIDDING_WAR","sector":"정책·이벤트·지배구조","primary_archetype":"governance_control_premium_tender_cap","loop_objective":"residual_false_positive_mining|counterexample_mining|4B_non_price_requirement_stress_test","trigger_type":"Stage2-CapGuard","trigger_date":"2023-03-07","entry_date":"2023-03-08","entry_price":158500,"evidence_available_at_that_date":"Kakao launched KRW 150,000/share tender offer to buy up to 35% of SM; entry was above the tender price cap.","evidence_source":"AP 2023-03-07; stock-web 041510 2023 shard lines around 2023-03-07/08","stage2_evidence_fields":["public_event_or_disclosure","policy_or_regulatory_optionality"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["explicit_event_cap","control_premium_or_event_premium"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/041/041510/2023.csv","profile_path":"atlas/symbol_profiles/041/041510.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":1.7,"MFE_90D_pct":1.7,"MFE_180D_pct":1.7,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-44.73,"MAE_90D_pct":-44.73,"MAE_180D_pct":-44.73,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2023-03-08","peak_price":161200,"drawdown_after_peak_pct":-45.66,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"good_full_window_4B_timing_when_treated_as_cap_not_entry","four_b_evidence_type":["explicit_event_cap","control_premium_or_event_premium"],"four_c_protection_label":"hard_4c_success_if_failed_offer_resolution_used","trigger_outcome_label":"false_positive_green_if_promoted","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window_not_flagged_in_fetched_profile","same_entry_group_id":"SEG_C32_041510_20230308","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"T_C32_040300_20230308_STAGE2_EVENT_RUMOR","case_id":"C32_040300_20230308_YTN_PRIVATIZATION_SPIKE","symbol":"040300","company_name":"YTN","round":"R13","loop":"9","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","fine_archetype_id":"GOVERNMENT_PRIVATIZATION_EXPECTATION_WITHOUT_BINDING_PRICE_CAP","sector":"정책·이벤트·지배구조","primary_archetype":"governance_control_premium_tender_cap","loop_objective":"residual_false_positive_mining|counterexample_mining","trigger_type":"Stage2-EventOnly","trigger_date":"2023-03-08","entry_date":"2023-03-08","entry_price":9390,"evidence_available_at_that_date":"Privatization/control-transfer expectation created price spike, but there was no same-day binding tender cap or immediate buyer-financing confirmation in this loop.","evidence_source":"stock-web YTN 2023 shard; background note that YTN was privatized in 2024 with Eugene Group as main shareholder","stage2_evidence_fields":["public_event_or_disclosure","policy_or_regulatory_optionality"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["price_only_local_peak"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/040/040300/2023.csv","profile_path":"atlas/symbol_profiles/040/040300.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":11.82,"MFE_90D_pct":11.82,"MFE_180D_pct":11.82,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-36.63,"MAE_90D_pct":-36.63,"MAE_180D_pct":-39.0,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2023-03-08","peak_price":10500,"drawdown_after_peak_pct":-43.33,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"price_only_local_4B_too_early_unless_event_cap_confirmed","four_b_evidence_type":["price_only"],"four_c_protection_label":"false_break","trigger_outcome_label":"failed_rerating_event_only","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window_not_flagged_in_fetched_profile","same_entry_group_id":"SEG_C32_040300_20230308","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
```

### 25.4 score_simulation rows

```jsonl
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C32_010130_20240913_MBK_YOUNGPOONG_TENDER","trigger_id":"T_C32_010130_20240913_STAGE2_ACTIONABLE","symbol":"010130","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","raw_component_scores_before":{"contract_score":"unknown_or_not_supported","backlog_visibility_score":"unknown_or_not_supported","margin_bridge_score":"unknown_or_not_supported","revision_score":"unknown_or_not_supported","relative_strength_score":"unknown_or_not_supported","customer_quality_score":"unknown_or_not_supported","policy_or_regulatory_score":75,"valuation_repricing_score":70,"execution_risk_score":45,"legal_or_contract_risk_score":"unknown_or_not_supported","dilution_cb_risk_score":"unknown_or_not_supported","accounting_trust_risk_score":"unknown_or_not_supported","control_premium_score":75,"event_cap_score":"unknown_or_not_supported","auction_competition_score":40,"governance_dispute_score":80},"weighted_score_before":78,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":"unknown_or_not_supported","backlog_visibility_score":"unknown_or_not_supported","margin_bridge_score":"unknown_or_not_supported","revision_score":"unknown_or_not_supported","relative_strength_score":"unknown_or_not_supported","customer_quality_score":"unknown_or_not_supported","policy_or_regulatory_score":82,"valuation_repricing_score":78,"execution_risk_score":50,"legal_or_contract_risk_score":"unknown_or_not_supported","dilution_cb_risk_score":"unknown_or_not_supported","accounting_trust_risk_score":"unknown_or_not_supported","control_premium_score":90,"event_cap_score":"unknown_or_not_supported","auction_competition_score":78,"governance_dispute_score":92},"weighted_score_after":87,"stage_label_after":"Stage3-Green-shadow","changed_components":["control_premium_score","auction_competition_score","governance_dispute_score"],"component_delta_explanation":"C32 shadow rewards open-ended hostile/control contest with subsequent counter-tender/boardroom path, not mere one-shot tender price.","MFE_90D_pct":131.68,"MAE_90D_pct":-1.65,"score_return_alignment_label":"aligned","current_profile_verdict":"current_profile_too_late"}
{"row_type":"score_simulation","profile_id":"c32_counterexample_guard_profile","case_id":"C32_041510_20230307_KAKAO_TENDER_CAP","trigger_id":"T_C32_041510_20230307_STAGE2_CAP_GUARD","symbol":"041510","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","raw_component_scores_before":{"contract_score":"unknown_or_not_supported","backlog_visibility_score":"unknown_or_not_supported","margin_bridge_score":"unknown_or_not_supported","revision_score":"unknown_or_not_supported","relative_strength_score":"unknown_or_not_supported","customer_quality_score":"unknown_or_not_supported","policy_or_regulatory_score":70,"valuation_repricing_score":72,"execution_risk_score":55,"legal_or_contract_risk_score":"unknown_or_not_supported","dilution_cb_risk_score":"unknown_or_not_supported","accounting_trust_risk_score":"unknown_or_not_supported","control_premium_score":85,"event_cap_score":30,"auction_competition_score":"unknown_or_not_supported","governance_dispute_score":"unknown_or_not_supported"},"weighted_score_before":76,"stage_label_before":"Stage3-Yellow-or-Green-risk","raw_component_scores_after":{"contract_score":"unknown_or_not_supported","backlog_visibility_score":"unknown_or_not_supported","margin_bridge_score":"unknown_or_not_supported","revision_score":"unknown_or_not_supported","relative_strength_score":"unknown_or_not_supported","customer_quality_score":"unknown_or_not_supported","policy_or_regulatory_score":60,"valuation_repricing_score":35,"execution_risk_score":75,"legal_or_contract_risk_score":"unknown_or_not_supported","dilution_cb_risk_score":"unknown_or_not_supported","accounting_trust_risk_score":"unknown_or_not_supported","control_premium_score":45,"event_cap_score":95,"auction_competition_score":"unknown_or_not_supported","governance_dispute_score":"unknown_or_not_supported"},"weighted_score_after":58,"stage_label_after":"4B-overlay / no-positive-stage","changed_components":["event_cap_score","valuation_repricing_score","control_premium_score"],"component_delta_explanation":"Entry above a fixed tender price is event-cap risk, not structural upside evidence.","MFE_90D_pct":1.7,"MAE_90D_pct":-44.73,"score_return_alignment_label":"guard_improves_alignment","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"score_simulation","profile_id":"c32_counterexample_guard_profile","case_id":"C32_040300_20230308_YTN_PRIVATIZATION_SPIKE","trigger_id":"T_C32_040300_20230308_STAGE2_EVENT_RUMOR","symbol":"040300","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","raw_component_scores_before":{"contract_score":"unknown_or_not_supported","backlog_visibility_score":"unknown_or_not_supported","margin_bridge_score":"unknown_or_not_supported","revision_score":"unknown_or_not_supported","relative_strength_score":"unknown_or_not_supported","customer_quality_score":"unknown_or_not_supported","policy_or_regulatory_score":75,"valuation_repricing_score":68,"execution_risk_score":60,"legal_or_contract_risk_score":"unknown_or_not_supported","dilution_cb_risk_score":"unknown_or_not_supported","accounting_trust_risk_score":"unknown_or_not_supported","control_premium_score":55,"event_cap_score":20,"auction_competition_score":"unknown_or_not_supported","governance_dispute_score":"unknown_or_not_supported"},"weighted_score_before":72,"stage_label_before":"Stage2-Actionable-risk","raw_component_scores_after":{"contract_score":"unknown_or_not_supported","backlog_visibility_score":"unknown_or_not_supported","margin_bridge_score":"unknown_or_not_supported","revision_score":"unknown_or_not_supported","relative_strength_score":"unknown_or_not_supported","customer_quality_score":"unknown_or_not_supported","policy_or_regulatory_score":55,"valuation_repricing_score":30,"execution_risk_score":80,"legal_or_contract_risk_score":"unknown_or_not_supported","dilution_cb_risk_score":"unknown_or_not_supported","accounting_trust_risk_score":"unknown_or_not_supported","control_premium_score":20,"event_cap_score":40,"auction_competition_score":"unknown_or_not_supported","governance_dispute_score":"unknown_or_not_supported"},"weighted_score_after":49,"stage_label_after":"Narrative-only / watch","changed_components":["control_premium_score","execution_risk_score","event_cap_score"],"component_delta_explanation":"Privatization narrative without binding buyer/price/mandatory-offer path is event-only and should not promote.","MFE_90D_pct":11.82,"MAE_90D_pct":-36.63,"score_return_alignment_label":"guard_improves_alignment","current_profile_verdict":"current_profile_false_positive"}
```

### 25.5 shadow_weight rows

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,c32_open_ended_control_contest_bonus,canonical_archetype_specific,L10_POLICY_EVENT_CROSS_REDTEAM_MISC,C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP,0,+7,+7,"open-ended hostile/control contest behaved unlike fixed tender cap","selects 010130 as positive and avoids global revision relaxation","T_C32_010130_20240913_STAGE2_ACTIONABLE",3,4,3,medium,canonical_shadow_only,"not production; needs more positives"
shadow_weight,c32_fixed_tender_cap_guard,canonical_archetype_specific,L10_POLICY_EVENT_CROSS_REDTEAM_MISC,C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP,0,+12,+12,"entry at/above fixed tender price produced low MFE and severe MAE","blocks SM false-positive promotion","T_C32_041510_20230307_STAGE2_CAP_GUARD",3,4,3,medium,canonical_shadow_only,"strengthens 4B non-price evidence in C32"
shadow_weight,c32_event_only_privatization_guard,canonical_archetype_specific,L10_POLICY_EVENT_CROSS_REDTEAM_MISC,C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP,0,+8,+8,"privatization narrative without binding buyer/price is not enough","blocks YTN event-only false-positive","T_C32_040300_20230308_STAGE2_EVENT_RUMOR",3,4,3,low,canonical_shadow_only,"needs additional public-sale cases"
```

### 25.6 residual_contribution row

```jsonl
{"row_type":"residual_contribution","round":"R13","loop":"9","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","new_independent_case_count":4,"reused_case_count":0,"new_symbol_count":4,"same_archetype_new_symbol_count":4,"same_archetype_new_trigger_family_count":4,"new_canonical_archetype_count":0,"new_trigger_family_count":4,"positive_case_count":1,"counterexample_count":3,"current_profile_error_count":3,"tested_existing_calibrated_axes":["price_only_blowoff_blocks_positive_stage","full_4b_requires_non_price_evidence","hard_4c_thesis_break_routes_to_4c"],"residual_error_types_found":["fixed_tender_cap_false_positive","privatization_event_only_false_positive","control_premium_4b_too_late"],"loop_contribution_label":"canonical_archetype_rule_candidate","do_not_propose_new_weight_delta":false,"auto_selected_coverage_gap":"C32_governance_control_premium_tender_cap_under_split_from_generic_policy_event"}
```

### 25.7 narrative_only row

```jsonl
{"row_type":"narrative_only","case_id":"C32_048260_20230125_OSSTEM_TENDER_DELISTING","symbol":"048260","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","reason":"tender_to_delisting_forward_window_or_listing_status_not_validated_in_this_loop","price_source":"Songdaiki/stock-web","usage":"not_weight_calibration"}
```

## 26. Deferred Coding Agent Handoff Prompt

### Purpose

You are now in the repository implementation phase. The attached Markdown files are v12 post-calibrated residual research outputs produced using the Songdaiki/stock-web OHLC atlas.

These MDs are not live candidate research. They are historical calibration research designed to extend the already-applied e2r_2_1_stock_web_calibrated profile.

Do not blindly apply every shadow row.
Ingest the machine-readable rows and update the sector/canonical-archetype calibration ledger.

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
next_round = R13_loop_10
suggested_scope = C32 additional positive holdout or C31 policy-subsidy-legislation event residual
priority = add_failed_hostile_bid_4C_case + add_successful_tender_positive_case
```

## 28. Source Notes

- Stock-web manifest confirms raw/unadjusted marcap price basis, max_date 2026-02-20, and calibration shard root.
- Stock-web 010130 2024/2025 shards were used for Korea Zinc entry, peak, and post-peak drawdown.
- Stock-web 041510 2023 shard was used for SM entry/peak/drawdown.
- Stock-web 040300 2023 shard was used for YTN event-only spike/drawdown.
- Reuters and AP were used only for event-date context; OHLC metrics come from Songdaiki/stock-web.
