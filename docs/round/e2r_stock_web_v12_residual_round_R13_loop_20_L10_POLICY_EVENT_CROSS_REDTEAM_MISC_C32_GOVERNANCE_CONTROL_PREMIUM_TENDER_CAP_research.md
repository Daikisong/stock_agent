# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
research_session = post_calibrated_sector_archetype_residual_research
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
round = R13
loop = 20
large_sector_id = L10_POLICY_EVENT_CROSS_REDTEAM_MISC
canonical_archetype_id = C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP
fine_archetype_id = GOVERNANCE_TENDER_EVENT_PREMIUM_CAP
selection_mode = auto_coverage_gap_fill
production_scoring_changed = false
shadow_weight_only = true
handoff_prompt_embedded = true
handoff_prompt_executed_now = false
```

This run deliberately avoids the previously generated R6/C22 insurance-reserve loop and moves into C32 governance/control-premium event residuals. The goal is not to prove the already applied global stage2/4B logic again, but to find where event premium behaves like a bright flare: useful as signal, dangerous as structural Green evidence.

## 1. Current Calibrated Profile Assumption

```text
current_default_profile_proxy = e2r_2_1_stock_web_calibrated_proxy
rollback_reference_profile_id = e2r_2_0_baseline_reference

stage2_actionable_evidence_bonus = +2.0
stage3_yellow_total_min = 75.0
stage3_green_total_min = 87.0
stage3_green_revision_min = 55.0
stage3_cross_evidence_green_buffer = +1.5
price_only_blowoff_blocks_positive_stage = true
full_4b_requires_non_price_evidence = true
hard_4c_thesis_break_routes_to_4c = true
```

Existing axis status for this loop:

```text
existing_axis_tested = [
  price_only_blowoff_blocks_positive_stage,
  full_4b_requires_non_price_evidence,
  stage3_green_revision_min
]
existing_axis_strengthened = [
  price_only_blowoff_blocks_positive_stage within C32 tender/control-premium cases,
  full_4b_requires_non_price_evidence with local-vs-full split,
  stage3_green_revision_min because C32 event premium lacks operating revision
]
existing_axis_weakened = []
new_axis_proposed = [
  c32_tender_event_cap_blocks_stage3_green,
  c32_competing_bid_squeeze_split_local_vs_full_4b,
  c32_rescue_financing_dilution_guard
]
```

## 2. Round / Large Sector / Canonical Archetype Scope

| field | value |
|---|---|
| round | R13 |
| loop | 20 |
| large_sector_id | L10_POLICY_EVENT_CROSS_REDTEAM_MISC |
| canonical_archetype_id | C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP |
| fine_archetype_id | GOVERNANCE_TENDER_EVENT_PREMIUM_CAP |
| loop_objective | coverage_gap_fill, counterexample_mining, 4B_non_price_requirement_stress_test, canonical_archetype_compression |
| rule_scope_preference | canonical_archetype_specific |

C32 is not a pure earnings archetype. It is a control-premium archetype. Price can move violently before any EPS or margin bridge appears. That makes it useful for Stage2-event recognition and 4B overlay calibration, but dangerous for Stage3-Green promotion.

## 3. Previous Coverage / Duplicate Avoidance Check

The calibration ingest artifact shows broad previous coverage: 107 parsed result MDs, 1,940 validated trigger rows, and 1,376 aggregate representative trigger rows across R1–R13. This loop is therefore treated as a coverage-gap/residual pass, not an initial calibration pass. fileciteturn473file0

GitHub search for `C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP` in the stock_agent calibration artifacts returned no direct matched file result in the accessible search layer, so this loop treats C32 as under-covered relative to R1/R2 representative sets.

Duplicate avoidance applied:

```text
same_symbol_same_trigger_date_research = blocked
same_archetype_new_symbol_or_counterexample = allowed
new_symbol_count = 3
reused_case_count = 0
minimum_new_independent_case_ratio = 1.00
```

## 4. Stock-Web OHLC Input / Price Source Validation

The price source is Songdaiki/stock-web. The manifest reports:

```text
source_name = FinanceData/marcap
price_adjustment_status = raw_unadjusted_marcap
min_date = 1995-05-02
max_date = 2026-02-20
tradable_row_count = 14354401
raw_row_count = 15214118
symbol_count = 5414
active_like_symbol_count = 2868
inactive_or_delisted_like_symbol_count = 2546
markets = KONEX, KOSDAQ, KOSDAQ GLOBAL, KOSPI
calibration_shard_root = atlas/ohlcv_tradable_by_symbol_year
raw_shard_root = atlas/ohlcv_raw_by_symbol_year
schema_path = atlas/schema.json
universe_path = atlas/universe/all_symbols.csv
```

The manifest also states that the data are raw/unadjusted OHLC, that zero-volume and zero-OHLC rows are excluded from calibration shards, and that corporate-action-contaminated windows are blocked by default. fileciteturn474file0

Profile validation:

| symbol | company | profile status | corporate action notes |
|---|---|---|---|
| 041510 | 에스엠 | active_like, last_date 2026-02-20 | historical corporate-action candidates in 2002/2005 only; clean 2023 window |
| 010130 | 고려아연 | active_like, last_date 2026-02-20 | corporate_action_candidate_count = 0; clean 2024–2025 window |
| 180640 | 한진칼 | active_like, last_date 2026-02-20 | 2014 candidate only; clean 2020–2021 window |

Profile source checks: 에스엠 profile fileciteturn475file0, 고려아연 profile fileciteturn476file0, 한진칼 profile fileciteturn477file0.

## 5. Historical Eligibility Gate

| case_id | trigger_date | entry_date | entry in tradable shard | forward 180D available | corporate-action contaminated? | calibration_usable |
|---|---:|---:|---:|---:|---:|---:|
| R13L20-C32-SM-20230213 | 2023-02-10 | 2023-02-13 | true | true | false | true |
| R13L20-C32-KZ-20240913 | 2024-09-13 | 2024-09-13 | true | true | false | true |
| R13L20-C32-HJKAL-20201116 | 2020-11-16 | 2020-11-16 | true | true | false | true |

## 6. Canonical Archetype Compression Map

```text
fine_archetype_id = GOVERNANCE_TENDER_EVENT_PREMIUM_CAP
canonical_archetype_id = C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP
compression_reason = tender offer, hostile bid, competing bid, rescue financing and control-premium events share one calibration problem:
  price can move before operational revision, and the move often has a visible event cap.
```

Sub-routes compressed into C32:

| sub-route | C32 handling |
|---|---|
| competing tender offer | Stage2 event possible; explicit tender price supports 4B cap |
| hostile tender plus counter-bid squeeze | Stage2 event possible; local 4B may be too early; split local/full peak |
| policy rescue financing inside governance fight | event premium is weakened by dilution/capital overhang guard |
| control-premium price-only blowoff | cannot promote Stage3 Green |

## 7. Case Selection Summary

| case_id | symbol | company | role | trigger family | new independent? |
|---|---:|---|---|---|---:|
| R13L20-C32-SM-20230213 | 041510 | 에스엠 | 4B_overlay_success / positive event premium | competing_tender_offer_control_premium | true |
| R13L20-C32-KZ-20240913 | 010130 | 고려아연 | 4B_overlay_success / positive event squeeze | hostile_tender_offer_plus_counter_bid_squeeze | true |
| R13L20-C32-HJKAL-20201116 | 180640 | 한진칼 | false_positive_green / counterexample | policy_rescue_financing_governance_dispute | true |

## 8. Positive vs Counterexample Balance

```text
positive_case_count = 2
counterexample_count = 1
4B_case_count = 2
4C_case_count = 0
calibration_usable_case_count = 3
minimum_positive_case_count_met = true
minimum_counterexample_count_met = true
minimum_calibration_usable_case_count_met = true
```

The positive cases are not "buy because event premium" cases. They are positive for calibration because the event evidence explained the MFE, while the same evidence also showed why this should be treated as Stage2-event plus 4B overlay, not Green.

## 9. Evidence Source Map

SM: Kakao launched a tender offer to buy up to 35% of SM at 150,000 won per share after HYBE had acquired a 14.8% stake and attempted to increase its stake; the tender offer escalated the control battle. citeturn260056news1

Korea Zinc: MBK Partners and Young Poong launched a tender offer for Korea Zinc at 660,000 won per share on 2024-09-13, seeking 6.98%–14.61%; Korea Zinc opposed it as hostile. citeturn260056news0 Later non-price 4B evidence appeared when Korea Zinc's share-issuance plan drew financial-regulator scrutiny and then a revision/suspension order. citeturn260056news2turn260056news3

Hanjin KAL: the Korean Air–Asiana merger policy process was initiated on 2020-11-16, with Korean Air to acquire a major Asiana stake using financing linked to Korea Development Bank support; the deal ultimately took years to complete. citeturn317647search1turn317647news0

## 10. Price Data Source Map

| symbol | shard(s) used | profile |
|---|---|---|
| 041510 | atlas/ohlcv_tradable_by_symbol_year/041/041510/2023.csv | atlas/symbol_profiles/041/041510.json |
| 010130 | atlas/ohlcv_tradable_by_symbol_year/010/010130/2024.csv; atlas/ohlcv_tradable_by_symbol_year/010/010130/2025.csv | atlas/symbol_profiles/010/010130.json |
| 180640 | atlas/ohlcv_tradable_by_symbol_year/180/180640/2020.csv; atlas/ohlcv_tradable_by_symbol_year/180/180640/2021.csv | atlas/symbol_profiles/180/180640.json |

Key OHLC rows for SM include 2023-02-13 entry close 116,000, 2023-03-07 close 149,700, 2023-03-08 high 161,200, and 2023-03-27 low 90,500. fileciteturn479file0

Key OHLC rows for Korea Zinc include 2024-09-13 close 666,000, 2024-10-29 high/close 1,543,000, 2024-12-05 close/high 2,000,000, 2024-12-06 high 2,407,000, and the 2025 decline to 643,000 low on 2025-04-09. fileciteturn481file0 fileciteturn482file0

Key OHLC rows for Hanjin KAL include 2020-11-16 close 82,200 and high 95,500, followed by lows down to 59,400 in December 2020 and 49,050 in May 2021. fileciteturn484file0 fileciteturn485file0

## 11. Case-by-Case Trigger Grid

| trigger_id | case_id | symbol | trigger_type | trigger_date | entry_date | entry_price | evidence family | dedupe_for_aggregate |
|---|---|---:|---|---:|---:|---:|---|---:|
| R13L20-C32-SM-STAGE2-20230213 | R13L20-C32-SM-20230213 | 041510 | Stage2-Actionable | 2023-02-10 | 2023-02-13 | 116000 | competing tender offer | true |
| R13L20-C32-SM-4B-20230307 | R13L20-C32-SM-20230213 | 041510 | Stage4B | 2023-03-07 | 2023-03-07 | 149700 | explicit tender cap | false |
| R13L20-C32-KZ-STAGE2-20240913 | R13L20-C32-KZ-20240913 | 010130 | Stage2-Actionable | 2024-09-13 | 2024-09-13 | 666000 | hostile tender offer | true |
| R13L20-C32-KZ-4B-20241205 | R13L20-C32-KZ-20240913 | 010130 | Stage4B | 2024-12-05 | 2024-12-05 | 2000000 | squeeze/positioning/regulatory overhang | false |
| R13L20-C32-HJKAL-STAGE2-20201116 | R13L20-C32-HJKAL-20201116 | 180640 | Stage2-Actionable | 2020-11-16 | 2020-11-16 | 82200 | policy rescue financing + governance dispute | true |

## 12. Trigger-Level OHLC Backtest Tables

| trigger_id | entry_price | MFE_30D | MAE_30D | MFE_90D | MAE_90D | MFE_180D | MAE_180D | peak_date | peak_price | drawdown_after_peak |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| R13L20-C32-SM-STAGE2-20230213 | 116000 | 38.97 | -21.98 | 38.97 | -21.98 | 38.97 | -21.98 | 2023-03-08 | 161200 | -48.82 |
| R13L20-C32-SM-4B-20230307 | 149700 | 7.68 | -39.55 | 7.68 | -39.55 | 7.68 | -39.55 | 2023-03-08 | 161200 | -48.82 |
| R13L20-C32-KZ-STAGE2-20240913 | 666000 | 131.68 | -1.65 | 261.41 | -1.65 | 261.41 | -3.45 | 2024-12-06 | 2407000 | -73.29 |
| R13L20-C32-KZ-4B-20241205 | 2000000 | 20.35 | -63.05 | 20.35 | -65.2 | 20.35 | -67.85 | 2024-12-06 | 2407000 | -73.29 |
| R13L20-C32-HJKAL-STAGE2-20201116 | 82200 | 16.18 | -27.74 | 16.18 | -31.75 | 16.18 | -40.33 | 2020-11-16 | 95500 | -48.64 |

## 13. Current Calibrated Profile Stress Test

| case_id | current profile likely judgment | actual price path | verdict |
|---|---|---|---|
| SM | Stage2-event allowed; Green blocked because no revision/margin bridge; 4B event cap valid | MFE worked, but drawdown after tender cap was severe | current_profile_correct |
| Korea Zinc | Stage2-event allowed; price-only local 4B could be too early; full-window 4B needed later | full peak came far above first tender price, then -73% drawdown from peak | current_profile_4B_too_early / later 4B_too_late |
| Hanjin KAL | relative strength and policy event could over-score Stage2/Yellow | same-day high failed; 90D/180D MAE dominated | current_profile_false_positive |

Stress-test answers:

```text
stage2_actionable_evidence_bonus = kept, but C32 needs event-premium guard
yellow_threshold_75 = insufficient alone for C32 because event evidence can exceed it without revision
green_threshold_87 / revision_55 = strengthened; C32 should require revision/margin/cash-flow bridge for Green
price_only_blowoff_guard = strengthened
full_4b_non_price_requirement = kept, but local/full-window split is required
hard_4C routing = not directly tested; no hard thesis-break row used
```

## 14. Stage2 / Yellow / Green Comparison

C32 cases should not promote to Green merely because price, tender premium and media attention align. The Green label needs a different engine: operating revision, durable cash-flow bridge, or repeated public evidence that value is no longer only control premium.

```text
green_lateness_ratio = not_applicable
reason = no confirmed operating Stage3-Green trigger in any selected C32 case
```

The absence of a Green trigger is itself the finding. C32 is a room with a mirror: price movement looks like confirmation, but often only reflects the bidder's flashlight.

## 15. 4B Local vs Full-window Timing Audit

| 4B trigger | stage2 entry | 4B entry | local_peak | full_window_peak | local proximity | full-window proximity | verdict |
|---|---:|---:|---:|---:|---:|---:|---|
| SM 2023-03-07 | 116000 | 149700 | 161200 | 161200 | 0.746 | 0.746 | good_full_window_4B_timing |
| Korea Zinc 2024-12-05 | 666000 | 2000000 | 2407000 | 2407000 | 0.766 | 0.766 | good_full_window_4B_timing |
| Hanjin KAL 2020-11-16 | 82200 | n/a | 95500 | 95500 | 0.000 | 0.000 | event_day_spike_not_full_4B_entry |

C32-specific observation: a fixed tender price can be a good 4B cap when it is near the local/full observed peak. But in a competing-control-bid squeeze, the first local overheat can be too early; 4B should be upgraded only when non-price evidence appears, such as tender price cap, buyback limit, financing risk, regulator scrutiny, special shareholder meeting, or failed bid path.

## 16. 4C Protection Audit

No hard 4C row is promoted in this MD. Korea Zinc's later drawdown after the 2024-12-06 peak shows that a 4B overlay could have protected a large portion of the post-peak decline, but this is not coded as a hard 4C because the operating thesis was not the central evidence.

```text
four_c_protection_label = thesis_break_watch_only for SM
four_c_protection_label = hard_4c_success_if_exit_on_4B_overlay for Korea Zinc
four_c_protection_label = false_break for Hanjin KAL
```

## 17. Sector-Specific Rule Candidate

```text
sector_specific_rule_candidate = false
reason = Only one large_sector_id is tested. Global/L10 sector delta would be premature.
```

## 18. Canonical-Archetype Rule Candidate

```text
canonical_archetype_rule_candidate = true
scope = C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP
```

Rule candidates:

1. `c32_tender_event_cap_blocks_stage3_green`
   - If evidence is primarily tender price, control-premium battle, white knight, hostile bid, or governance premium, do not promote Stage3 Green without operating revision, cash-flow bridge, or durable business evidence.

2. `c32_competing_bid_squeeze_split_local_vs_full_4b`
   - In competing bid/squeeze paths, a price-only local peak can be too early. Keep `four_b_local_peak_proximity` and `four_b_full_window_peak_proximity` separate.

3. `c32_rescue_financing_dilution_guard`
   - If the event premium is entangled with policy rescue financing, capital increase, dilution, or government/creditor bailout structure, downgrade positive promotion and allow only watch/event overlay.

## 19. Before / After Backtest Comparison

| profile_id | scope | hypothesis | eligible_trigger_count | selected_entry_trigger_per_case | avg_MFE_90D_pct | avg_MAE_90D_pct | avg_MFE_180D_pct | avg_MAE_180D_pct | false_positive_rate | missed_structural_count | late_green_count | avg_green_lateness_ratio | avg_four_b_local_peak_proximity | avg_four_b_full_window_peak_proximity | score_return_alignment_verdict |
|---|---:|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---|---:|---:|---|
| P0 e2r_2_1_stock_web_calibrated_proxy | global proxy | current profile with price-only blowoff and 4B non-price guard, but no C32-specific tender cap | 3 | SM/KZ/HJKAL | 105.52 | -18.46 | 105.52 | -21.92 | 0.33 | 0 | 0 | n/a | n/a | n/a | mixed; Hanjin false positive remains |
| P0b e2r_2_0_baseline_reference | rollback | older profile would over-credit event price and relative strength | 3 | SM/KZ/HJKAL | 105.52 | -18.46 | 105.52 | -21.92 | 0.67 | 0 | 1 | n/a | n/a | n/a | weak; treats event premium as structural |
| P1 sector_specific_candidate_profile | L10 shadow | cross-event red-team guard for event premium | 3 | SM/KZ/HJKAL | 105.52 | -18.46 | 105.52 | -21.92 | 0.33 | 0 | 0 | n/a | 0.756 | 0.756 | better but too broad |
| P2 canonical_archetype_candidate_profile | C32 shadow | tender/control premium cannot be Green without operating revision; separate 4B overlay | 3 | SM/KZ/HJKAL | 105.52 | -18.46 | 105.52 | -21.92 | 0.00 | 0 | 0 | n/a | 0.756 | 0.756 | best alignment |
| P3 counterexample_guard_profile | C32 guard | blocks policy-rescue financing/dilution paths | 3 | SM/KZ/HJKAL | 105.52 | -18.46 | 105.52 | -21.92 | 0.00 | 0 | 0 | n/a | 0.756 | 0.756 | best downside control |


## 20. Score-Return Alignment Matrix

| case_id | before score label | after score label | return alignment |
|---|---|---|---|
| SM | Stage3-Yellow candidate | Stage2-Actionable / 4B-watch | aligned_after_shadow |
| Korea Zinc | Stage3-Green candidate | Stage2-Actionable / staged 4B overlay | aligned_after_shadow |
| Hanjin KAL | Stage3-Yellow candidate | Stage2-watch / blocked positive | false_positive_blocked_after_shadow |

## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive_case_count | counterexample_count | 4B_case_count | 4C_case_count | new_independent_case_count | reused_case_count | calibration_usable_trigger_count | representative_trigger_count | current_profile_error_count | sector_rule_candidate | canonical_rule_candidate | coverage_gap_after_this_loop |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| L10_POLICY_EVENT_CROSS_REDTEAM_MISC | C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP | GOVERNANCE_TENDER_EVENT_PREMIUM_CAP | 2 | 1 | 2 | 0 | 3 | 0 | 5 | 3 | 2 | false | true | hard 4C / failed bid aftermath still needs more rows |

## 22. Residual Contribution Summary

```text
new_independent_case_count: 3
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 3
same_archetype_new_symbol_count: 3
same_archetype_new_trigger_family_count: 3
new_canonical_archetype_count: 1
new_fine_archetype_count: 1
new_trigger_family_count: 3

tested_existing_calibrated_axes:
- price_only_blowoff_blocks_positive_stage
- full_4b_requires_non_price_evidence
- stage3_green_revision_min

residual_error_types_found:
- event_premium_false_green
- local_4B_too_early_without_full_window_split
- policy_rescue_financing_dilution_caps_control_premium

new_axis_proposed:
- c32_tender_event_cap_blocks_stage3_green
- c32_competing_bid_squeeze_split_local_vs_full_4b
- c32_rescue_financing_dilution_guard

existing_axis_strengthened:
- price_only_blowoff_blocks_positive_stage within C32
- full_4b_requires_non_price_evidence within C32
- stage3_green_revision_min within C32

existing_axis_weakened: []
existing_axis_kept:
- stage2_actionable_evidence_bonus
- hard_4c_thesis_break_routes_to_4c

sector_specific_rule_candidate: false
canonical_archetype_rule_candidate: true
no_new_signal_reason: null

loop_contribution_label: canonical_archetype_rule_candidate
do_not_propose_new_weight_delta: false
```

## 23. Validation Scope / Non-Validation Scope

Validated:

```text
- stock-web manifest max_date and raw_unadjusted_marcap basis
- profile availability and corporate-action candidate windows
- entry_date and entry_price from tradable shards
- 30D/90D/180D MFE/MAE from visible OHLC rows
- local-vs-full 4B proximity for SM and Korea Zinc
- positive/counterexample balance for C32
```

Not validated:

```text
- live/current candidate scan
- brokerage or auto-trading route
- production code behavior inside stock_agent
- exact intraday disclosure timestamp
- 1Y/2Y aggregate scoring; primary calibration window is 30D/90D/180D
```

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,c32_tender_event_cap_blocks_stage3_green,canonical_archetype_specific,L10_POLICY_EVENT_CROSS_REDTEAM_MISC,C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP,0,1,+1,"fixed tender/control-premium cap is event evidence, not operating revision","blocked Hanjin false positive; kept SM/Korea Zinc as event/4B not Green","R13L20-C32-SM-STAGE2-20230213|R13L20-C32-KZ-STAGE2-20240913|R13L20-C32-HJKAL-STAGE2-20201116",3,3,1,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,c32_competing_bid_squeeze_split_local_vs_full_4b,canonical_archetype_specific,L10_POLICY_EVENT_CROSS_REDTEAM_MISC,C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP,0,1,+1,"competing control bids can make price-only local 4B too early","Korea Zinc required full-window split; SM tender cap worked earlier","R13L20-C32-SM-4B-20230307|R13L20-C32-KZ-4B-20241205",2,2,0,medium,canonical_shadow_only,"4B overlay only"
shadow_weight,c32_rescue_financing_dilution_guard,canonical_archetype_specific,L10_POLICY_EVENT_CROSS_REDTEAM_MISC,C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP,0,1,+1,"policy rescue financing or capital raise overhang weakens control-premium signal","Hanjin KAL event spike failed and drawdown dominated 90D/180D","R13L20-C32-HJKAL-STAGE2-20201116",1,1,1,low,canonical_shadow_only,"needs additional holdout"

```

## 25. Machine-Readable Rows

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
{"row_type":"case","case_id":"R13L20-C32-SM-20230213","symbol":"041510","company_name":"에스엠","case_type":"4B_overlay_success","positive_or_counterexample":"positive","best_trigger":"R13L20-C32-SM-STAGE2-20230213","trigger_family":"competing_tender_offer_control_premium","score_price_alignment":"event premium worked, but tender cap/competing bid produced 4B rather than structural Green","current_profile_verdict":"current_profile_correct","notes":"HYBE/Kakao control-premium battle. Stage2 event entry had high MFE but later tender cap and failed persistence argue against Stage3 Green.","round":"R13","loop":"20","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","fine_archetype_id":"GOVERNANCE_TENDER_EVENT_PREMIUM_CAP","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"price_source":"Songdaiki/stock-web"}
{"row_type":"case","case_id":"R13L20-C32-KZ-20240913","symbol":"010130","company_name":"고려아연","case_type":"4B_overlay_success","positive_or_counterexample":"positive","best_trigger":"R13L20-C32-KZ-STAGE2-20240913","trigger_family":"hostile_tender_offer_plus_counter_bid_squeeze","score_price_alignment":"large MFE came from control contest and squeeze, not operating revision; full-window 4B needed local/full split","current_profile_verdict":"current_profile_4B_too_early","notes":"MBK/Young Poong tender offer and later defensive actions created a two-step price path: first tender premium, then squeeze/blowoff.","round":"R13","loop":"20","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","fine_archetype_id":"GOVERNANCE_TENDER_EVENT_PREMIUM_CAP","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"price_source":"Songdaiki/stock-web"}
{"row_type":"case","case_id":"R13L20-C32-HJKAL-20201116","symbol":"180640","company_name":"한진칼","case_type":"false_positive_green","positive_or_counterexample":"counterexample","best_trigger":"R13L20-C32-HJKAL-STAGE2-20201116","trigger_family":"policy_rescue_financing_governance_dispute","score_price_alignment":"same-day event spike was not durable; 90D/180D drawdown dominated the entry","current_profile_verdict":"current_profile_false_positive","notes":"Korean Air/Asiana rescue-merger policy shock intersected with the pre-existing Hanjin governance fight; dilution/policy financing capped control premium.","round":"R13","loop":"20","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","fine_archetype_id":"GOVERNANCE_TENDER_EVENT_PREMIUM_CAP","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"price_source":"Songdaiki/stock-web"}
{"trigger_id":"R13L20-C32-SM-STAGE2-20230213","case_id":"R13L20-C32-SM-20230213","symbol":"041510","company_name":"에스엠","round":"R13","loop":"20","trigger_type":"Stage2-Actionable","trigger_date":"2023-02-10","entry_date":"2023-02-13","entry_price":116000,"evidence_available_at_that_date":"HYBE had acquired Lee Soo-man's stake and launched/continued a control-premium tender route; market could react by the next trading-day close.","evidence_source":"AP/Reuters-style historical event sources; stock-web OHLC rows.","stage2_evidence_fields":["public_event_or_disclosure","policy_or_regulatory_optionality","relative_strength"],"stage3_evidence_fields":[],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"MFE_30D_pct":38.97,"MFE_90D_pct":38.97,"MFE_180D_pct":38.97,"MFE_1Y_pct":38.97,"MFE_2Y_pct":null,"MAE_30D_pct":-21.98,"MAE_90D_pct":-21.98,"MAE_180D_pct":-21.98,"MAE_1Y_pct":-28.88,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2023-03-08","peak_price":161200,"drawdown_after_peak_pct":-48.82,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_4B_trigger","four_b_evidence_type":[],"four_c_protection_label":"not_applicable","trigger_outcome_label":"event_premium_success_but_not_structural_green","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"SM-20230213-116000","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"row_type":"trigger","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","fine_archetype_id":"GOVERNANCE_TENDER_EVENT_PREMIUM_CAP","sector":"Cross-archetype RedTeam / 4B / 회계신뢰도 / 가격검증 총정리","primary_archetype":"governance_control_premium_tender_cap","loop_objective":"coverage_gap_fill|counterexample_mining|4B_non_price_requirement_stress_test|canonical_archetype_compression","price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","calibration_block_reasons":[],"price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/041/041510/2023.csv","profile_path":"atlas/symbol_profiles/041/041510.json"}
{"trigger_id":"R13L20-C32-SM-4B-20230307","case_id":"R13L20-C32-SM-20230213","symbol":"041510","company_name":"에스엠","round":"R13","loop":"20","trigger_type":"Stage4B","trigger_date":"2023-03-07","entry_date":"2023-03-07","entry_price":149700,"evidence_available_at_that_date":"Kakao tender price at 150,000 won created an explicit event cap close to the market price.","evidence_source":"AP report on Kakao tender offer; stock-web OHLC rows.","stage2_evidence_fields":[],"stage3_evidence_fields":[],"stage4b_evidence_fields":["explicit_event_cap","control_premium_or_event_premium","valuation_blowoff"],"stage4c_evidence_fields":[],"MFE_30D_pct":7.68,"MFE_90D_pct":7.68,"MFE_180D_pct":7.68,"MFE_1Y_pct":7.68,"MFE_2Y_pct":null,"MAE_30D_pct":-39.55,"MAE_90D_pct":-39.55,"MAE_180D_pct":-39.55,"MAE_1Y_pct":-44.89,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2023-03-08","peak_price":161200,"drawdown_after_peak_pct":-48.82,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":0.746,"four_b_full_window_peak_proximity":0.746,"four_b_timing_verdict":"good_full_window_4B_timing","four_b_evidence_type":["explicit_event_cap","control_premium_or_event_premium"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"good_event_cap_4B","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"SM-20230307-149700","dedupe_for_aggregate":false,"aggregate_group_role":"4B_overlay_only","is_new_independent_case":true,"reuse_reason":"same_case_4B_overlay_not_representative","independent_evidence_weight":0.25,"do_not_count_as_new_case":true,"row_type":"trigger","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","fine_archetype_id":"GOVERNANCE_TENDER_EVENT_PREMIUM_CAP","sector":"Cross-archetype RedTeam / 4B / 회계신뢰도 / 가격검증 총정리","primary_archetype":"governance_control_premium_tender_cap","loop_objective":"coverage_gap_fill|counterexample_mining|4B_non_price_requirement_stress_test|canonical_archetype_compression","price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","calibration_block_reasons":[],"price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/041/041510/2023.csv","profile_path":"atlas/symbol_profiles/041/041510.json"}
{"trigger_id":"R13L20-C32-KZ-STAGE2-20240913","case_id":"R13L20-C32-KZ-20240913","symbol":"010130","company_name":"고려아연","round":"R13","loop":"20","trigger_type":"Stage2-Actionable","trigger_date":"2024-09-13","entry_date":"2024-09-13","entry_price":666000,"evidence_available_at_that_date":"MBK Partners and Young Poong launched a tender offer at 660,000 won; shares immediately repriced above the offer.","evidence_source":"Reuters 2024-09-13; stock-web OHLC rows.","stage2_evidence_fields":["public_event_or_disclosure","policy_or_regulatory_optionality","relative_strength"],"stage3_evidence_fields":[],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"MFE_30D_pct":131.68,"MFE_90D_pct":261.41,"MFE_180D_pct":261.41,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-1.65,"MAE_90D_pct":-1.65,"MAE_180D_pct":-3.45,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-12-06","peak_price":2407000,"drawdown_after_peak_pct":-73.29,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_4B_trigger","four_b_evidence_type":[],"four_c_protection_label":"not_applicable","trigger_outcome_label":"control_premium_squeeze_success_but_not_operating_revision","current_profile_verdict":"current_profile_4B_too_early","calibration_usable":true,"forward_window_trading_days":180,"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"KZ-20240913-666000","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"row_type":"trigger","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","fine_archetype_id":"GOVERNANCE_TENDER_EVENT_PREMIUM_CAP","sector":"Cross-archetype RedTeam / 4B / 회계신뢰도 / 가격검증 총정리","primary_archetype":"governance_control_premium_tender_cap","loop_objective":"coverage_gap_fill|counterexample_mining|4B_non_price_requirement_stress_test|canonical_archetype_compression","price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","calibration_block_reasons":[],"price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/010/010130/2024.csv","profile_path":"atlas/symbol_profiles/010/010130.json"}
{"trigger_id":"R13L20-C32-KZ-4B-20241205","case_id":"R13L20-C32-KZ-20240913","symbol":"010130","company_name":"고려아연","round":"R13","loop":"20","trigger_type":"Stage4B","trigger_date":"2024-12-05","entry_date":"2024-12-05","entry_price":2000000,"evidence_available_at_that_date":"control fight had turned into squeeze/positioning overheat after tender, buyback, proposed share issue, regulator scrutiny and special-meeting path.","evidence_source":"Reuters 2024-10-31, 2024-11-06, 2024-12-03; stock-web OHLC rows.","stage2_evidence_fields":[],"stage3_evidence_fields":[],"stage4b_evidence_fields":["positioning_overheat","valuation_blowoff","legal_or_regulatory_block","control_premium_or_event_premium"],"stage4c_evidence_fields":[],"MFE_30D_pct":20.35,"MFE_90D_pct":20.35,"MFE_180D_pct":20.35,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-63.05,"MAE_90D_pct":-65.2,"MAE_180D_pct":-67.85,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-12-06","peak_price":2407000,"drawdown_after_peak_pct":-73.29,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":0.766,"four_b_full_window_peak_proximity":0.766,"four_b_timing_verdict":"good_full_window_4B_timing","four_b_evidence_type":["positioning_overheat","legal_or_regulatory_block","control_premium_or_event_premium"],"four_c_protection_label":"hard_4c_success_if_exit_on_4B_overlay","trigger_outcome_label":"good_full_window_4B_timing","current_profile_verdict":"current_profile_4B_too_late","calibration_usable":true,"forward_window_trading_days":180,"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"KZ-20241205-2000000","dedupe_for_aggregate":false,"aggregate_group_role":"4B_overlay_only","is_new_independent_case":true,"reuse_reason":"same_case_4B_overlay_not_representative","independent_evidence_weight":0.25,"do_not_count_as_new_case":true,"row_type":"trigger","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","fine_archetype_id":"GOVERNANCE_TENDER_EVENT_PREMIUM_CAP","sector":"Cross-archetype RedTeam / 4B / 회계신뢰도 / 가격검증 총정리","primary_archetype":"governance_control_premium_tender_cap","loop_objective":"coverage_gap_fill|counterexample_mining|4B_non_price_requirement_stress_test|canonical_archetype_compression","price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","calibration_block_reasons":[],"price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/010/010130/2024.csv","profile_path":"atlas/symbol_profiles/010/010130.json"}
{"trigger_id":"R13L20-C32-HJKAL-STAGE2-20201116","case_id":"R13L20-C32-HJKAL-20201116","symbol":"180640","company_name":"한진칼","round":"R13","loop":"20","trigger_type":"Stage2-Actionable","trigger_date":"2020-11-16","entry_date":"2020-11-16","entry_price":82200,"evidence_available_at_that_date":"Government/KDB-backed Korean Air–Asiana merger announcement intersected with an ongoing Hanjin governance dispute; same-day high was strong but close failed to hold.","evidence_source":"Historical merger policy sources; stock-web OHLC rows.","stage2_evidence_fields":["public_event_or_disclosure","policy_or_regulatory_optionality","relative_strength"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["dilution_or_cb","capital_raise_or_overhang","control_premium_or_event_premium"],"stage4c_evidence_fields":[],"MFE_30D_pct":16.18,"MFE_90D_pct":16.18,"MFE_180D_pct":16.18,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-27.74,"MAE_90D_pct":-31.75,"MAE_180D_pct":-40.33,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2020-11-16","peak_price":95500,"drawdown_after_peak_pct":-48.64,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":0.0,"four_b_full_window_peak_proximity":0.0,"four_b_timing_verdict":"event_day_spike_not_full_4B_entry","four_b_evidence_type":["capital_raise_or_overhang","control_premium_or_event_premium"],"four_c_protection_label":"false_break","trigger_outcome_label":"false_positive_event_premium","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"HJKAL-20201116-82200","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"row_type":"trigger","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","fine_archetype_id":"GOVERNANCE_TENDER_EVENT_PREMIUM_CAP","sector":"Cross-archetype RedTeam / 4B / 회계신뢰도 / 가격검증 총정리","primary_archetype":"governance_control_premium_tender_cap","loop_objective":"coverage_gap_fill|counterexample_mining|4B_non_price_requirement_stress_test|canonical_archetype_compression","price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","calibration_block_reasons":[],"price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/180/180640/2020.csv","profile_path":"atlas/symbol_profiles/180/180640.json"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy_to_c32_shadow","case_id":"R13L20-C32-SM-20230213","trigger_id":"R13L20-C32-SM-STAGE2-20230213","symbol":"041510","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":80,"customer_quality_score":0,"policy_or_regulatory_score":55,"valuation_repricing_score":70,"execution_risk_score":45,"legal_or_contract_risk_score":25,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":84,"stage_label_before":"Stage3-Yellow_candidate","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":80,"customer_quality_score":0,"policy_or_regulatory_score":55,"valuation_repricing_score":45,"execution_risk_score":60,"legal_or_contract_risk_score":35,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":72,"stage_label_after":"Stage2-Actionable/4B-watch","changed_components":["valuation_repricing_score","execution_risk_score","legal_or_contract_risk_score"],"component_delta_explanation":"C32 event premium is reweighted from positive Stage3 evidence into explicit event-cap / 4B overlay unless operating revision or cash-flow bridge exists.","MFE_90D_pct":38.97,"MAE_90D_pct":-21.98,"score_return_alignment_label":"aligned_after_shadow","current_profile_verdict":"current_profile_correct"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy_to_c32_shadow","case_id":"R13L20-C32-KZ-20240913","trigger_id":"R13L20-C32-KZ-STAGE2-20240913","symbol":"010130","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":90,"customer_quality_score":0,"policy_or_regulatory_score":65,"valuation_repricing_score":85,"execution_risk_score":60,"legal_or_contract_risk_score":45,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":88,"stage_label_before":"Stage3-Green_candidate","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":90,"customer_quality_score":0,"policy_or_regulatory_score":65,"valuation_repricing_score":55,"execution_risk_score":75,"legal_or_contract_risk_score":65,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":77,"stage_label_after":"Stage2-Actionable/4B-watch","changed_components":["valuation_repricing_score","execution_risk_score","legal_or_contract_risk_score"],"component_delta_explanation":"C32 event premium is reweighted from positive Stage3 evidence into explicit event-cap / 4B overlay unless operating revision or cash-flow bridge exists.","MFE_90D_pct":261.41,"MAE_90D_pct":-1.65,"score_return_alignment_label":"aligned_after_shadow","current_profile_verdict":"current_profile_4B_too_early"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy_to_c32_shadow","case_id":"R13L20-C32-HJKAL-20201116","trigger_id":"R13L20-C32-HJKAL-STAGE2-20201116","symbol":"180640","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":75,"customer_quality_score":0,"policy_or_regulatory_score":80,"valuation_repricing_score":65,"execution_risk_score":70,"legal_or_contract_risk_score":45,"dilution_cb_risk_score":65,"accounting_trust_risk_score":0},"weighted_score_before":79,"stage_label_before":"Stage3-Yellow_candidate","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":65,"customer_quality_score":0,"policy_or_regulatory_score":75,"valuation_repricing_score":25,"execution_risk_score":85,"legal_or_contract_risk_score":55,"dilution_cb_risk_score":80,"accounting_trust_risk_score":0},"weighted_score_after":60,"stage_label_after":"Stage2-watch/blocked_positive","changed_components":["valuation_repricing_score","execution_risk_score","dilution_cb_risk_score"],"component_delta_explanation":"C32 event premium is reweighted from positive Stage3 evidence into explicit event-cap / 4B overlay unless operating revision or cash-flow bridge exists.","MFE_90D_pct":16.18,"MAE_90D_pct":-31.75,"score_return_alignment_label":"false_positive_blocked_after_shadow","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"residual_contribution","round":"R13","loop":"20","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","new_independent_case_count":3,"reused_case_count":0,"new_symbol_count":3,"same_archetype_new_symbol_count":3,"same_archetype_new_trigger_family_count":3,"new_canonical_archetype_count":1,"new_trigger_family_count":3,"positive_case_count":2,"counterexample_count":1,"current_profile_error_count":2,"tested_existing_calibrated_axes":["price_only_blowoff_blocks_positive_stage","full_4b_requires_non_price_evidence","stage3_green_revision_min"],"residual_error_types_found":["event_premium_false_green","local_4B_too_early_without_full_window_split","policy_rescue_financing_dilution_caps_control_premium"],"loop_contribution_label":"canonical_archetype_rule_candidate","do_not_propose_new_weight_delta":false}
```

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,c32_tender_event_cap_blocks_stage3_green,canonical_archetype_specific,L10_POLICY_EVENT_CROSS_REDTEAM_MISC,C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP,0,1,+1,"fixed tender/control-premium cap is event evidence, not operating revision","blocked Hanjin false positive; kept SM/Korea Zinc as event/4B not Green","R13L20-C32-SM-STAGE2-20230213|R13L20-C32-KZ-STAGE2-20240913|R13L20-C32-HJKAL-STAGE2-20201116",3,3,1,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,c32_competing_bid_squeeze_split_local_vs_full_4b,canonical_archetype_specific,L10_POLICY_EVENT_CROSS_REDTEAM_MISC,C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP,0,1,+1,"competing control bids can make price-only local 4B too early","Korea Zinc required full-window split; SM tender cap worked earlier","R13L20-C32-SM-4B-20230307|R13L20-C32-KZ-4B-20241205",2,2,0,medium,canonical_shadow_only,"4B overlay only"
shadow_weight,c32_rescue_financing_dilution_guard,canonical_archetype_specific,L10_POLICY_EVENT_CROSS_REDTEAM_MISC,C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP,0,1,+1,"policy rescue financing or capital raise overhang weakens control-premium signal","Hanjin KAL event spike failed and drawdown dominated 90D/180D","R13L20-C32-HJKAL-STAGE2-20201116",1,1,1,low,canonical_shadow_only,"needs additional holdout"

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
next_round_candidate_1 = R8 / C28_SOFTWARE_SECURITY_CONTRACT_RETENTION / contract-retention false positive vs durable ARR
next_round_candidate_2 = R13 / C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP / failed-bid hard 4C aftermath
next_round_candidate_3 = R7 / C24_BIO_TRIAL_DATA_EVENT_RISK / trial-data price-only false Green
```

## 28. Source Notes

- The user prompt for v12 requires actual stock-web OHLC rows, standalone MD output, duplicate avoidance, current-profile stress test, machine-readable rows and a deferred coding-agent handoff. fileciteturn471file0
- Stock-agent ingest summary was used only for coverage/duplicate avoidance, not code inspection. fileciteturn473file0
- Stock-web manifest and symbol profiles were used as the price-source validation layer. fileciteturn474file0turn475file0turn476file0turn477file0
- Event evidence uses historical public reports for SM/Kakao/HYBE, Korea Zinc/MBK/Young Poong and Korean Air/Asiana/Hanjin KAL. citeturn260056news1turn260056news0turn260056news2turn260056news3turn317647search1turn317647news0
