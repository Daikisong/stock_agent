# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```yaml
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
scheduled_round: R12
scheduled_loop: "12"
completed_round: R12
completed_loop: "12"
large_sector_id: L10_POLICY_EVENT_CROSS_REDTEAM_MISC
canonical_archetype_id: C31_POLICY_SUBSIDY_LEGISLATION_EVENT
fine_archetype_id: PUBLIC_HEALTH_FOOD_SAFETY_DEMAND_SHOCK_EVENT_CAP
output_file: e2r_stock_web_v12_residual_round_R12_loop_12_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_C31_POLICY_SUBSIDY_LEGISLATION_EVENT_research.md
production_scoring_changed: false
shadow_weight_only: true
handoff_prompt_embedded: true
handoff_prompt_executed_now: false
current_stock_discovery_allowed: false
auto_trading_allowed: false
brokerage_api_allowed: false
stock_agent_code_access_allowed: false
stock_agent_code_patch_allowed: false
stock_web_price_atlas_access_required: true
price_route_hunt_allowed: false
```

This loop adds 4 new independent cases, 2 counterexamples, and 4 residual errors for R12/L10_POLICY_EVENT_CROSS_REDTEAM_MISC/C31_POLICY_SUBSIDY_LEGISLATION_EVENT.

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

The residual question is not whether a food-safety headline can move stocks. It can. The question is whether C31 public-health events deserve a durable Stage3 label when the evidence is mainly fear-driven demand, no margin pass-through, and no revision bridge. The answer from this loop is: early salt-demand routes can be Stage2-Actionable; late release headlines should be capped by event age and routed to 4B/watch unless earnings confirmation appears.

## 2. Round / Large Sector / Canonical Archetype Scope

| Field | Value |
|---|---|
| scheduled_round | R12 |
| scheduled_loop | 12 |
| large_sector_id | L10_POLICY_EVENT_CROSS_REDTEAM_MISC |
| canonical_archetype_id | C31_POLICY_SUBSIDY_LEGISLATION_EVENT |
| fine_archetype_id | PUBLIC_HEALTH_FOOD_SAFETY_DEMAND_SHOCK_EVENT_CAP |
| round_schedule_status | valid |
| round_sector_consistency | pass |
| loop_objective | coverage_gap_fill, counterexample_mining, residual_false_positive_mining, sector_specific_rule_discovery, canonical_archetype_compression, 4B_non_price_requirement_stress_test |

R12 is used as the agriculture/life-service/miscellaneous residual round. Because the canonical catalog has no separate agriculture-only ID, this study maps the salt and seafood public-health demand shock into C31_POLICY_SUBSIDY_LEGISLATION_EVENT under L10_POLICY_EVENT_CROSS_REDTEAM_MISC.

## 3. Previous Coverage / Duplicate Avoidance Check

Local v12 registry showed R12 loop10 already covered grain/feed export-curb supply shock under C31 and R12 loop11 covered C32 governance/tender-cap events. Therefore this file stays in R12/loop12 but moves the C31 evidence family from grain/feed supply shock to Fukushima-related food-safety demand shock.

| Check | Result |
|---|---|
| Same symbol + trigger_date + entry_date repeated | no |
| Same canonical_archetype_id repeated | yes, allowed |
| Existing R12 loop10 evidence family | grain/feed export-curb supply shock |
| This loop evidence family | Fukushima/salt/seafood public-health demand shock |
| New symbol count | 4 |
| New trigger family count | 2 |
| New independent case ratio | 1.00 |
| Wrong round penalty | 0 |
| Schema rematerialization penalty | 0 |

## 4. Stock-Web OHLC Input / Price Source Validation

Stock-Web manifest was checked for this execution. The manifest reports source_name FinanceData/marcap, price_adjustment_status raw_unadjusted_marcap, min_date 1995-05-02, max_date 2026-02-20, tradable_row_count 14,354,401, raw_row_count 15,214,118, symbol_count 5,414, and calibration_shard_root atlas/ohlcv_tradable_by_symbol_year. It also states that raw/unadjusted OHLC is used and corporate-action windows are blocked by default. The schema confirms d/o/h/l/c/v/a/mc/s/m as tradable columns and defines MFE/MAE as max high/min low from entry_date through N tradable rows.

```json
{
  "row_type": "price_source_validation",
  "source": "Songdaiki/stock-web",
  "source_url": "https://github.com/Songdaiki/stock-web",
  "manifest_path": "atlas/manifest.json",
  "schema_path": "atlas/schema.json",
  "universe_path": "atlas/universe/all_symbols.csv",
  "manifest_max_date": "2026-02-20",
  "price_basis": "tradable_raw",
  "price_adjustment_status": "raw_unadjusted_marcap",
  "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year",
  "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year",
  "validation_status": "usable_for_historical_calibration"
}
```

## 5. Historical Eligibility Gate

| case | symbol | profile status | corporate action window | forward 180D | calibration usable |
|---|---:|---|---|---|---|
| 인산가 salt panic | 277410 | active_like; CA candidate only 2018-09-11 | clean 2023-06~2024-02 | available | true |
| 보라티알 salt import panic | 250000 | active_like; no CA candidates | clean | available | true |
| CJ씨푸드 release headline | 011150 | active_like; CA candidate 2002 only | clean 2023-08~2024 | available | true |
| 사조씨푸드 release headline | 014710 | active_like; no CA candidates | clean | available | true |

All representative rows use tradable shards. Raw shards were not used for weight calibration.

## 6. Canonical Archetype Compression Map

```text
fine_archetype_id = PUBLIC_HEALTH_FOOD_SAFETY_DEMAND_SHOCK_EVENT_CAP
canonical_archetype_id = C31_POLICY_SUBSIDY_LEGISLATION_EVENT
large_sector_id = L10_POLICY_EVENT_CROSS_REDTEAM_MISC
```

The compression is intentionally C31, not C18/C20. These were not ordinary export-channel reorder cases. They were policy/public-health event shocks in which risk perception altered short-run buying behavior for salt and fishery-adjacent names. The correct scoring question is event freshness, direct demand route, and pass-through evidence, not brand/export growth.

## 7. Case Selection Summary

| case_id | symbol | company | role | new? | reason |
|---|---:|---|---|---|---|
| R12L12C31_277410_INSAN_SALT_PANIC_STAGE2 | 277410 | 인산가 | positive Stage2 / 4B later | yes | new symbol; direct salt panic demand route |
| R12L12C31_250000_BORATIAL_SALT_IMPORT_STAGE2 | 250000 | 보라티알 | positive Stage2 / 4B later | yes | new symbol; food/salt import adjacency with extreme MFE |
| R12L12C31_011150_CJSEAFOOD_RELEASE_FALSE_POSITIVE | 011150 | CJ씨푸드 | counterexample | yes | new symbol; late release headline produced poor residual reward-to-drawdown |
| R12L12C31_014710_SAJOSEAFOOD_RELEASE_FALSE_POSITIVE | 014710 | 사조씨푸드 | counterexample | yes | new symbol; seafood headline peak faded quickly |

## 8. Positive vs Counterexample Balance

| Type | Count | Interpretation |
|---|---:|---|
| positive_case_count | 2 | Early June salt-demand route was tradeable as Stage2-Actionable. |
| counterexample_count | 2 | Late August official-release headlines had insufficient residual MFE and high MAE. |
| 4B_case_count | 2 | Local event peaks required fast 4B overlay before durable Green evidence existed. |
| 4C_case_count | 0 | No hard thesis-break disclosure was needed; event-age fade was enough for watch/4B. |

## 9. Evidence Source Map

| Evidence family | Trigger dates | Evidence available then | Use in score |
|---|---|---|---|
| Korean salt and seafood risk perception ahead of Fukushima discharge | 2023-06-07 | Salt/seafood safety concern and Fukushima release debate were public before the official discharge; the market had visible volume and price response. | Stage2 public-event + direct demand route, not Green |
| IAEA/Japan decision and regional opposition | 2023-07~2023-08 | IAEA approval, South Korean protests, and Japan's release plan were public. | confirms event source, not earnings bridge |
| Japan announced/began release | 2023-08-22 to 2023-08-24 | Japan announced release timing and began discharge on August 24, 2023; China expanded restrictions on Japanese aquatic imports. | late-event 4B/event-cap, not durable Stage3 |
| No confirmed margin bridge | all triggers | No case here had public, same-date durable gross-margin, reorder, or earnings revision evidence. | blocks Green |

## 10. Price Data Source Map

| symbol | company | price_shard_path | profile_path |
|---:|---|---|---|
| 277410 | 인산가 | atlas/ohlcv_tradable_by_symbol_year/277/277410/2023.csv | atlas/symbol_profiles/277/277410.json |
| 250000 | 보라티알 | atlas/ohlcv_tradable_by_symbol_year/250/250000/2023.csv | atlas/symbol_profiles/250/250000.json |
| 011150 | CJ씨푸드 | atlas/ohlcv_tradable_by_symbol_year/011/011150/2023.csv | atlas/symbol_profiles/011/011150.json |
| 014710 | 사조씨푸드 | atlas/ohlcv_tradable_by_symbol_year/014/014710/2023.csv | atlas/symbol_profiles/014/014710.json |

## 11. Case-by-Case Trigger Grid

| trigger_id | symbol | company | trigger_type | trigger_date | entry_date | entry_price | MFE90 | MAE90 | current_profile_verdict | aggregate_role |
|---|---:|---|---|---|---|---:|---:|---:|---|---|
| R12L12C31_277410_T1_STAGE2_ACTIONABLE | 277410 | 인산가 | Stage2-Actionable | 2023-06-07 | 2023-06-07 | 2550 | 72.35 | -24.35 | current_profile_4B_too_late | representative |
| R12L12C31_250000_T1_STAGE2_ACTIONABLE | 250000 | 보라티알 | Stage2-Actionable | 2023-06-07 | 2023-06-07 | 12840 | 77.18 | -17.99 | current_profile_4B_too_late | representative |
| R12L12C31_011150_T1_RELEASE_ANNOUNCEMENT | 011150 | CJ씨푸드 | Stage2-Actionable | 2023-08-22 | 2023-08-22 | 3495 | 22.03 | -28.76 | current_profile_false_positive | representative |
| R12L12C31_014710_T1_RELEASE_ANNOUNCEMENT | 014710 | 사조씨푸드 | Stage2-Actionable | 2023-08-22 | 2023-08-22 | 4650 | 28.17 | -26.88 | current_profile_false_positive | representative |
| R12L12C31_277410_T2_4B_OVERLAY | 277410 | 인산가 | Stage4B-overlay | 2023-06-15 | 2023-06-15 | 4055 | 8.38 | -52.43 | current_profile_4B_too_late | 4B_overlay_only |
| R12L12C31_250000_T2_4B_OVERLAY | 250000 | 보라티알 | Stage4B-overlay | 2023-06-15 | 2023-06-15 | 21250 | 7.06 | -51.72 | current_profile_4B_too_late | 4B_overlay_only |

## 12. Trigger-Level OHLC Backtest Tables

| trigger_id | entry_date | entry_price | MFE30 | MFE90 | MFE180 | MAE30 | MAE90 | MAE180 | peak_date | peak_price | drawdown_after_peak |
|---|---|---:|---:|---:|---:|---:|---:|---:|---|---:|---:|
| R12L12C31_277410_T1_STAGE2_ACTIONABLE | 2023-06-07 | 2550 | 72.35 | 72.35 | 72.35 | -13.14 | -24.35 | -32.82 | 2023-06-16 | 4395 | -61.02 |
| R12L12C31_250000_T1_STAGE2_ACTIONABLE | 2023-06-07 | 12840 | 77.18 | 77.18 | 77.18 | -12.15 | -17.99 | -20.09 | 2023-06-15 | 22750 | -54.9 |
| R12L12C31_011150_T1_RELEASE_ANNOUNCEMENT | 2023-08-22 | 3495 | 22.03 | 22.03 | 22.03 | -24.46 | -28.76 | -28.76 | 2023-08-23 | 4265 | -41.62 |
| R12L12C31_014710_T1_RELEASE_ANNOUNCEMENT | 2023-08-22 | 4650 | 28.17 | 28.17 | 28.17 | -23.55 | -26.88 | -26.88 | 2023-08-23 | 5960 | -42.95 |
| R12L12C31_277410_T2_4B_OVERLAY | 2023-06-15 | 4055 | 8.38 | 8.38 | 8.38 | -45.38 | -52.43 | -57.76 | 2023-06-16 | 4395 | -61.02 |
| R12L12C31_250000_T2_4B_OVERLAY | 2023-06-15 | 21250 | 7.06 | 7.06 | 7.06 | -39.91 | -51.72 | -51.72 | 2023-06-15 | 22750 | -54.9 |

## 13. Current Calibrated Profile Stress Test

| case_id | symbol | type | MFE90 | MAE90 | current_profile_verdict | stress-test conclusion |
|---|---:|---|---:|---:|---|---|
| R12L12C31_277410_INSAN_SALT_PANIC_STAGE2 | 277410 | positive | 72.35 | -24.35 | current_profile_4B_too_late | Stage2 watch valid, Green blocked by no margin bridge |
| R12L12C31_250000_BORATIAL_SALT_IMPORT_STAGE2 | 250000 | positive | 77.18 | -17.99 | current_profile_4B_too_late | Stage2 watch valid, Green blocked by no margin bridge |
| R12L12C31_011150_CJSEAFOOD_RELEASE_FALSE_POSITIVE | 011150 | counterexample | 22.03 | -28.76 | current_profile_false_positive | Late headline should be capped to watch/4B, not Green |
| R12L12C31_014710_SAJOSEAFOOD_RELEASE_FALSE_POSITIVE | 014710 | counterexample | 28.17 | -26.88 | current_profile_false_positive | Late headline should be capped to watch/4B, not Green |

Stress-test answers:

1. The current profile correctly recognizes public events and relative strength as Stage2 evidence, but it still risks over-reading late food-safety headline moves as Stage3-Yellow if no event-age cap is applied.
2. Stage2 bonus was useful for 인산가 and 보라티알 because early June entries had large MFE. It was too permissive if applied to late August seafood headlines.
3. Yellow threshold 75 is not the main problem. The problem is component composition: no margin bridge, no revision, no durable order conversion.
4. Green threshold 87 and revision minimum 55 remain appropriate; none of these cases should be Green.
5. Price-only blowoff guard remains correct and should be strengthened by an event-age router.
6. Full 4B non-price requirement is still sound globally, but C31 event peaks need a local event-cap overlay when the only non-price evidence is public fear and no durable earnings proof.
7. Hard 4C is not the right tool here. The better route is 4B/watch, because the thesis did not break by disclosure; it expired by event age and lack of conversion.

## 14. Stage2 / Yellow / Green Comparison

| Case group | Stage2 entry | Stage3-Yellow proxy | Stage3-Green proxy | Green lateness ratio | Interpretation |
|---|---|---|---|---|---|
| 인산가 / 보라티알 early salt route | 2023-06-07 | not supported by earnings bridge | not supported | not_applicable | Stage2 catches event MFE; Green is blocked correctly. |
| CJ씨푸드 / 사조씨푸드 release headline | 2023-08-22 | should be capped | not supported | not_applicable | Late event headline has low residual quality. |

Green labels are intentionally absent. Treating the short-lived public-health demand shock as Green would be outcome-chasing by price rather than evidence.

## 15. 4B Local vs Full-window Timing Audit

| trigger_id | four_b_local_peak_proximity | four_b_full_window_peak_proximity | verdict |
|---|---:|---:|---|
| R12L12C31_277410_T2_4B_OVERLAY | 0.816 | 0.816 | good_local_event_4B_timing_but_not_stage3_green |
| R12L12C31_250000_T2_4B_OVERLAY | 0.849 | 0.849 | good_local_event_4B_timing_but_not_stage3_green |
| release-headline representatives | null | null | event-cap required; no full 4B promotion from price only |

The metaphor here is a siren, not an engine. The event siren can move a crowd fast, but once the siren stops, the crowd disperses unless there is an earnings engine underneath.

## 16. 4C Protection Audit

No hard 4C thesis-break row is proposed. The right protection label is `thesis_break_watch_only`: the thesis faded because the event aged and lacked conversion, not because a disclosed contract, approval, or subsidy was cancelled.

## 17. Sector-Specific Rule Candidate

```text
rule_scope = sector_specific
axis = L10_EVENT_CAP_FAST_4B_ROUTER
candidate_delta = +1 shadow-only
```

Rule: In L10 public-health / food-safety event shocks, if the stock reaches a local vertical peak while evidence is still mostly public fear + relative strength and no margin/revision bridge is public, route to Stage4B-overlay/watch rather than allowing Stage3-Yellow/Green promotion.

## 18. Canonical-Archetype Rule Candidate

```text
rule_scope = canonical_archetype_specific
axis = C31_PUBLIC_HEALTH_EVENT_GREEN_CAP
candidate_delta = +1 shadow-only
```

Rule: C31 public-health food-safety events require all three before Green can be considered:

```text
1. fresh event timing, not a stale headline replay,
2. direct demand or policy route to the listed company,
3. public pass-through evidence: margin, revision, reorder, inventory depletion, or confirmed financial visibility.
```

If only 1 and 2 exist, Stage2-Actionable is allowed. If only price/volume exists after the official release date, classify as event-cap watch or 4B overlay.

## 19. Before / After Backtest Comparison

| profile_id | scope | hypothesis | eligible_trigger_count | avg_MFE_90D_pct | avg_MAE_90D_pct | false_positive_rate | missed_structural_count | late_green_count | avg_four_b_local_peak_proximity | avg_four_b_full_window_peak_proximity | score_return_alignment_verdict |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| P0 e2r_2_1_stock_web_calibrated_proxy | current | Stage2 bonus works, but event-age and margin-bridge cap are incomplete | 4 | 49.93 | -24.5 | 0.50 | 0 | 2 | 0.83 | 0.83 | useful but too permissive for late food-safety headlines |
| P0b e2r_2_0_baseline_reference | rollback | Older profile over-weights price/RS and under-routes 4B event caps | 4 | 49.93 | -24.5 | 0.50 | 1 | 2 | 0.83 | 0.83 | weaker than calibrated profile |
| P1 sector_specific_candidate_profile | sector | L10 public-health event cap and fast 4B router | 4 | 49.93 | -24.50 | 0.00 qualitative | 0 | 0 | 0.83 | 0.83 | better false-positive control |
| P2 canonical_archetype_candidate_profile | C31 | C31 event-age + direct demand + pass-through gate | 4 | 49.93 | -24.50 | 0.00 qualitative | 0 | 0 | 0.83 | 0.83 | best canonical compression |
| P3 counterexample_guard_profile | guard | No Green unless margin pass-through or durable demand conversion is public | 2 selected positives | 74.77 | -21.17 | 0.00 | 0 | 0 | 0.83 | 0.83 | strongest protection, may miss short event trades if used for Stage2 |

## 20. Score-Return Alignment Matrix

| axis | before behavior | after shadow behavior | alignment |
|---|---|---|---|
| stage2_actionable_evidence_bonus | Helps early salt-demand entries | Kept | existing_axis_kept |
| price_only_blowoff_blocks_positive_stage | Correct but not sufficient for event-age | Strengthened through C31 event-cap | existing_axis_strengthened |
| full_4b_requires_non_price_evidence | Correct globally | Strengthened with local event-cap overlay | existing_axis_strengthened |
| hard_4c_thesis_break_routes_to_4c | Not needed here | Kept | existing_axis_kept |
| C31_PUBLIC_HEALTH_EVENT_GREEN_CAP | absent | proposed shadow-only | new_axis_proposed |

## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive_case_count | counterexample_count | 4B_case_count | 4C_case_count | new_independent_case_count | reused_case_count | calibration_usable_trigger_count | representative_trigger_count | current_profile_error_count | sector_rule_candidate | canonical_rule_candidate | coverage_gap_after_this_loop |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| L10_POLICY_EVENT_CROSS_REDTEAM_MISC | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | PUBLIC_HEALTH_FOOD_SAFETY_DEMAND_SHOCK_EVENT_CAP | 2 | 2 | 2 | 0 | 4 | 0 | 6 | 4 | 4 | true | true | public-health food-safety events still need other geographies and post-2024 holdout |

## 22. Residual Contribution Summary

```yaml
new_independent_case_count: 4
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 4
new_canonical_archetype_count: 0
new_fine_archetype_count: 1
new_trigger_family_count: 2
same_archetype_new_symbol_count: 4
same_archetype_new_trigger_family_count: 2
tested_existing_calibrated_axes:
  - stage2_actionable_evidence_bonus
  - price_only_blowoff_blocks_positive_stage
  - full_4b_requires_non_price_evidence
  - hard_4c_thesis_break_routes_to_4c
residual_error_types_found:
  - public_health_event_green_false_positive
  - late_release_headline_low_residual_mfe
  - event_4B_too_late_without_margin_bridge
new_axis_proposed:
  - C31_PUBLIC_HEALTH_EVENT_GREEN_CAP
  - L10_EVENT_CAP_FAST_4B_ROUTER
existing_axis_strengthened:
  - price_only_blowoff_blocks_positive_stage
  - full_4b_requires_non_price_evidence
existing_axis_weakened: null
existing_axis_kept:
  - stage2_actionable_evidence_bonus
  - hard_4c_thesis_break_routes_to_4c
sector_specific_rule_candidate: true
canonical_archetype_rule_candidate: true
no_new_signal_reason: null
loop_contribution_label: canonical_archetype_rule_candidate
do_not_propose_new_weight_delta: false
```

## 23. Validation Scope / Non-Validation Scope

Validated:

```text
- scheduled_round = R12 and scheduled_loop = 12
- large_sector_id = L10_POLICY_EVENT_CROSS_REDTEAM_MISC
- canonical_archetype_id = C31_POLICY_SUBSIDY_LEGISLATION_EVENT
- stock-web manifest/schema/profile/shard paths checked
- actual stock-web OHLC rows used for entry/peak/drawdown estimates
- representative trigger rows deduplicated for aggregate metrics
- positive and counterexample balance satisfied
```

Not validated:

```text
- No live watchlist or current candidate scan.
- No stock_agent source code was opened.
- No production scoring patch was written.
- No broker/API/auto-trading execution.
- News URLs were used only to establish historical event timing, not to recommend securities.
```

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,C31_PUBLIC_HEALTH_EVENT_GREEN_CAP,canonical_archetype_specific,L10_POLICY_EVENT_CROSS_REDTEAM_MISC,C31_POLICY_SUBSIDY_LEGISLATION_EVENT,0,1,+1,"Do not promote Fukushima/salt/seafood public-health events to Stage3-Green unless fresh event timing plus direct demand route plus margin/pass-through confirmation are all present.","Reduced late-event false positives while preserving early salt-demand Stage2 watch MFE.","R12L12C31_277410_T1_STAGE2_ACTIONABLE|R12L12C31_250000_T1_STAGE2_ACTIONABLE|R12L12C31_011150_T1_RELEASE_ANNOUNCEMENT|R12L12C31_014710_T1_RELEASE_ANNOUNCEMENT",4,4,2,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,L10_EVENT_CAP_FAST_4B_ROUTER,sector_specific,L10_POLICY_EVENT_CROSS_REDTEAM_MISC,C31_POLICY_SUBSIDY_LEGISLATION_EVENT,0,1,+1,"If price reaches local event peak without non-price earnings bridge, route to 4B overlay even when Stage2 evidence was valid.","Improves 4B timing for 인산가/보라티알; prevents price-only late entries from being treated as durable positives.","R12L12C31_277410_T2_4B_OVERLAY|R12L12C31_250000_T2_4B_OVERLAY",2,2,0,medium,sector_shadow_only,"not production; post-calibrated residual"
```

## 25. Machine-Readable Rows

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration"}
{"row_type": "case", "case_id": "R12L12C31_277410_INSAN_SALT_PANIC_STAGE2", "symbol": "277410", "company_name": "인산가", "round": "R12", "loop": "12", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "fine_archetype_id": "PUBLIC_HEALTH_FOOD_SAFETY_DEMAND_SHOCK_EVENT_CAP", "case_type": "structural_success", "positive_or_counterexample": "positive", "best_trigger": "R12L12C31_277410_T1_STAGE2_ACTIONABLE", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "event_stage2_aligned_but_green_capped", "current_profile_verdict": "current_profile_4B_too_late", "price_source": "Songdaiki/stock-web", "notes": "Early Korean salt-stock panic captured an event tradeable MFE, but no durable margin/revision bridge justified Stage3-Green."}
{"row_type": "case", "case_id": "R12L12C31_250000_BORATIAL_SALT_IMPORT_STAGE2", "symbol": "250000", "company_name": "보라티알", "round": "R12", "loop": "12", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "fine_archetype_id": "PUBLIC_HEALTH_FOOD_SAFETY_DEMAND_SHOCK_EVENT_CAP", "case_type": "structural_success", "positive_or_counterexample": "positive", "best_trigger": "R12L12C31_250000_T1_STAGE2_ACTIONABLE", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "event_stage2_aligned_but_green_capped", "current_profile_verdict": "current_profile_4B_too_late", "price_source": "Songdaiki/stock-web", "notes": "Food-import/salt adjacency reacted strongly to the public-health demand shock, then mean-reverted without a confirmed earnings bridge."}
{"row_type": "case", "case_id": "R12L12C31_011150_CJSEAFOOD_RELEASE_FALSE_POSITIVE", "symbol": "011150", "company_name": "CJ씨푸드", "round": "R12", "loop": "12", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "fine_archetype_id": "PUBLIC_HEALTH_FOOD_SAFETY_DEMAND_SHOCK_EVENT_CAP", "case_type": "false_positive_green", "positive_or_counterexample": "counterexample", "best_trigger": "R12L12C31_011150_T1_RELEASE_ANNOUNCEMENT", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "late_event_false_positive_reduced_by_event_cap", "current_profile_verdict": "current_profile_false_positive", "price_source": "Songdaiki/stock-web", "notes": "Official release-announcement trade had a brief gap-up but poor 90D/180D reward-to-drawdown; seafood exposure was not enough without domestic demand or margin confirmation."}
{"row_type": "case", "case_id": "R12L12C31_014710_SAJOSEAFOOD_RELEASE_FALSE_POSITIVE", "symbol": "014710", "company_name": "사조씨푸드", "round": "R12", "loop": "12", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "fine_archetype_id": "PUBLIC_HEALTH_FOOD_SAFETY_DEMAND_SHOCK_EVENT_CAP", "case_type": "false_positive_green", "positive_or_counterexample": "counterexample", "best_trigger": "R12L12C31_014710_T1_RELEASE_ANNOUNCEMENT", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "late_event_false_positive_reduced_by_event_cap", "current_profile_verdict": "current_profile_false_positive", "price_source": "Songdaiki/stock-web", "notes": "The release announcement produced a sharp one-day theme peak, but no durable pass-through evidence; it is a 4B/event-cap example rather than a positive Stage3 case."}
{"row_type": "trigger", "trigger_id": "R12L12C31_277410_T1_STAGE2_ACTIONABLE", "case_id": "R12L12C31_277410_INSAN_SALT_PANIC_STAGE2", "symbol": "277410", "company_name": "인산가", "round": "R12", "loop": "12", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "fine_archetype_id": "PUBLIC_HEALTH_FOOD_SAFETY_DEMAND_SHOCK_EVENT_CAP", "sector": "농업·생활서비스·기타", "primary_archetype": "public_health_food_safety_demand_shock_event_cap", "loop_objective": "coverage_gap_fill|counterexample_mining|residual_false_positive_mining|4B_non_price_requirement_stress_test", "trigger_type": "Stage2-Actionable", "trigger_date": "2023-06-07", "evidence_available_at_that_date": "Fukushima treated-water release concern was public; Korean salt/seafood risk perception and demand shock were visible before and around the release decision.", "evidence_source": "AP/Reuters-family public news; stock-web OHLC row verified", "stage2_evidence_fields": ["public_event_or_disclosure", "policy_or_regulatory_optionality", "relative_strength", "capacity_or_volume_route"], "stage3_evidence_fields": ["unknown_or_not_supported_margin_bridge", "unknown_or_not_supported_revision"], "stage4b_evidence_fields": ["valuation_blowoff", "positioning_overheat", "price_only_local_peak"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/277/277410/2023.csv", "profile_path": "atlas/symbol_profiles/277/277410.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2023-06-07", "entry_price": 2550, "MFE_30D_pct": 72.35, "MFE_90D_pct": 72.35, "MFE_180D_pct": 72.35, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -13.14, "MAE_90D_pct": -24.35, "MAE_180D_pct": -32.82, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2023-06-16", "peak_price": 4395, "drawdown_after_peak_pct": -61.02, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "event_cap_required_not_full_4B_from_price_only", "four_b_evidence_type": ["price_only", "valuation_blowoff", "positioning_overheat"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "high_MFE_event_positive_with_fast_fade", "current_profile_verdict": "current_profile_4B_too_late", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R12L12C31_277410_20230607", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "R12L12C31_250000_T1_STAGE2_ACTIONABLE", "case_id": "R12L12C31_250000_BORATIAL_SALT_IMPORT_STAGE2", "symbol": "250000", "company_name": "보라티알", "round": "R12", "loop": "12", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "fine_archetype_id": "PUBLIC_HEALTH_FOOD_SAFETY_DEMAND_SHOCK_EVENT_CAP", "sector": "농업·생활서비스·기타", "primary_archetype": "public_health_food_safety_demand_shock_event_cap", "loop_objective": "coverage_gap_fill|counterexample_mining|residual_false_positive_mining|4B_non_price_requirement_stress_test", "trigger_type": "Stage2-Actionable", "trigger_date": "2023-06-07", "evidence_available_at_that_date": "Fukushima treated-water release concern was public; Korean salt/seafood risk perception and demand shock were visible before and around the release decision.", "evidence_source": "AP/Reuters-family public news; stock-web OHLC row verified", "stage2_evidence_fields": ["public_event_or_disclosure", "policy_or_regulatory_optionality", "relative_strength", "customer_or_order_quality"], "stage3_evidence_fields": ["unknown_or_not_supported_margin_bridge", "unknown_or_not_supported_financial_visibility"], "stage4b_evidence_fields": ["valuation_blowoff", "positioning_overheat", "price_only_local_peak"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/250/250000/2023.csv", "profile_path": "atlas/symbol_profiles/250/250000.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2023-06-07", "entry_price": 12840, "MFE_30D_pct": 77.18, "MFE_90D_pct": 77.18, "MFE_180D_pct": 77.18, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -12.15, "MAE_90D_pct": -17.99, "MAE_180D_pct": -20.09, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2023-06-15", "peak_price": 22750, "drawdown_after_peak_pct": -54.9, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "event_cap_required_not_full_4B_from_price_only", "four_b_evidence_type": ["price_only", "valuation_blowoff", "positioning_overheat"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "high_MFE_event_positive_with_late_drawdown", "current_profile_verdict": "current_profile_4B_too_late", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R12L12C31_250000_20230607", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "R12L12C31_011150_T1_RELEASE_ANNOUNCEMENT", "case_id": "R12L12C31_011150_CJSEAFOOD_RELEASE_FALSE_POSITIVE", "symbol": "011150", "company_name": "CJ씨푸드", "round": "R12", "loop": "12", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "fine_archetype_id": "PUBLIC_HEALTH_FOOD_SAFETY_DEMAND_SHOCK_EVENT_CAP", "sector": "농업·생활서비스·기타", "primary_archetype": "public_health_food_safety_demand_shock_event_cap", "loop_objective": "coverage_gap_fill|counterexample_mining|residual_false_positive_mining|4B_non_price_requirement_stress_test", "trigger_type": "Stage2-Actionable", "trigger_date": "2023-08-22", "evidence_available_at_that_date": "Fukushima treated-water release concern was public; Korean salt/seafood risk perception and demand shock were visible before and around the release decision.", "evidence_source": "AP/Reuters-family public news; stock-web OHLC row verified", "stage2_evidence_fields": ["public_event_or_disclosure", "policy_or_regulatory_optionality", "relative_strength"], "stage3_evidence_fields": ["unknown_or_not_supported_margin_bridge", "unknown_or_not_supported_revision"], "stage4b_evidence_fields": ["event_cap", "positioning_overheat", "price_only_local_peak"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/011/011150/2023.csv", "profile_path": "atlas/symbol_profiles/011/011150.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2023-08-22", "entry_price": 3495, "MFE_30D_pct": 22.03, "MFE_90D_pct": 22.03, "MFE_180D_pct": 22.03, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -24.46, "MAE_90D_pct": -28.76, "MAE_180D_pct": -28.76, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2023-08-23", "peak_price": 4265, "drawdown_after_peak_pct": -41.62, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "event_cap_required_not_full_4B_from_price_only", "four_b_evidence_type": ["price_only", "positioning_overheat", "event_cap"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "late_event_counterexample_low_residual_MFE_high_MAE", "current_profile_verdict": "current_profile_false_positive", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R12L12C31_011150_20230822", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "R12L12C31_014710_T1_RELEASE_ANNOUNCEMENT", "case_id": "R12L12C31_014710_SAJOSEAFOOD_RELEASE_FALSE_POSITIVE", "symbol": "014710", "company_name": "사조씨푸드", "round": "R12", "loop": "12", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "fine_archetype_id": "PUBLIC_HEALTH_FOOD_SAFETY_DEMAND_SHOCK_EVENT_CAP", "sector": "농업·생활서비스·기타", "primary_archetype": "public_health_food_safety_demand_shock_event_cap", "loop_objective": "coverage_gap_fill|counterexample_mining|residual_false_positive_mining|4B_non_price_requirement_stress_test", "trigger_type": "Stage2-Actionable", "trigger_date": "2023-08-22", "evidence_available_at_that_date": "Fukushima treated-water release concern was public; Korean salt/seafood risk perception and demand shock were visible before and around the release decision.", "evidence_source": "AP/Reuters-family public news; stock-web OHLC row verified", "stage2_evidence_fields": ["public_event_or_disclosure", "policy_or_regulatory_optionality", "relative_strength"], "stage3_evidence_fields": ["unknown_or_not_supported_margin_bridge", "unknown_or_not_supported_financial_visibility"], "stage4b_evidence_fields": ["event_cap", "positioning_overheat", "price_only_local_peak"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/014/014710/2023.csv", "profile_path": "atlas/symbol_profiles/014/014710.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2023-08-22", "entry_price": 4650, "MFE_30D_pct": 28.17, "MFE_90D_pct": 28.17, "MFE_180D_pct": 28.17, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -23.55, "MAE_90D_pct": -26.88, "MAE_180D_pct": -26.88, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2023-08-23", "peak_price": 5960, "drawdown_after_peak_pct": -42.95, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "event_cap_required_not_full_4B_from_price_only", "four_b_evidence_type": ["price_only", "positioning_overheat", "event_cap"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "late_event_counterexample_mfe_not_enough_for_green", "current_profile_verdict": "current_profile_false_positive", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R12L12C31_014710_20230822", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "R12L12C31_277410_T2_4B_OVERLAY", "case_id": "R12L12C31_277410_INSAN_SALT_PANIC_STAGE2", "symbol": "277410", "company_name": "인산가", "round": "R12", "loop": "12", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "fine_archetype_id": "PUBLIC_HEALTH_FOOD_SAFETY_DEMAND_SHOCK_EVENT_CAP", "sector": "농업·생활서비스·기타", "primary_archetype": "public_health_event_4B_overlay", "loop_objective": "4B_non_price_requirement_stress_test", "trigger_type": "Stage4B-overlay", "trigger_date": "2023-06-15", "evidence_available_at_that_date": "Short-window price had already repriced into a vertical local peak while no margin bridge or repeat-order evidence was confirmed.", "evidence_source": "stock-web OHLC row; public Fukushima/salt-demand event context", "stage2_evidence_fields": [], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["valuation_blowoff", "positioning_overheat", "price_only_local_peak", "event_cap"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/277/277410/2023.csv", "profile_path": "atlas/symbol_profiles/277/277410.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2023-06-15", "entry_price": 4055, "MFE_30D_pct": 8.38, "MFE_90D_pct": 8.38, "MFE_180D_pct": 8.38, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -45.38, "MAE_90D_pct": -52.43, "MAE_180D_pct": -57.76, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2023-06-16", "peak_price": 4395, "drawdown_after_peak_pct": -61.02, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.816, "four_b_full_window_peak_proximity": 0.816, "four_b_timing_verdict": "good_local_event_4B_timing_but_not_stage3_green", "four_b_evidence_type": ["price_only", "valuation_blowoff", "positioning_overheat", "event_cap"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "4B_overlay_success", "current_profile_verdict": "current_profile_4B_too_late", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R12L12C31_277410_20230615", "dedupe_for_aggregate": false, "aggregate_group_role": "4B_overlay_only", "is_new_independent_case": false, "reuse_reason": "same case, separate 4B timing audit", "independent_evidence_weight": 0.25, "do_not_count_as_new_case": true}
{"row_type": "trigger", "trigger_id": "R12L12C31_250000_T2_4B_OVERLAY", "case_id": "R12L12C31_250000_BORATIAL_SALT_IMPORT_STAGE2", "symbol": "250000", "company_name": "보라티알", "round": "R12", "loop": "12", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "fine_archetype_id": "PUBLIC_HEALTH_FOOD_SAFETY_DEMAND_SHOCK_EVENT_CAP", "sector": "농업·생활서비스·기타", "primary_archetype": "public_health_event_4B_overlay", "loop_objective": "4B_non_price_requirement_stress_test", "trigger_type": "Stage4B-overlay", "trigger_date": "2023-06-15", "evidence_available_at_that_date": "Short-window price had already repriced into a vertical local peak while no margin bridge or repeat-order evidence was confirmed.", "evidence_source": "stock-web OHLC row; public Fukushima/salt-demand event context", "stage2_evidence_fields": [], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["valuation_blowoff", "positioning_overheat", "price_only_local_peak", "event_cap"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/250/250000/2023.csv", "profile_path": "atlas/symbol_profiles/250/250000.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2023-06-15", "entry_price": 21250, "MFE_30D_pct": 7.06, "MFE_90D_pct": 7.06, "MFE_180D_pct": 7.06, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -39.91, "MAE_90D_pct": -51.72, "MAE_180D_pct": -51.72, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2023-06-15", "peak_price": 22750, "drawdown_after_peak_pct": -54.9, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.849, "four_b_full_window_peak_proximity": 0.849, "four_b_timing_verdict": "good_local_event_4B_timing_but_not_stage3_green", "four_b_evidence_type": ["price_only", "valuation_blowoff", "positioning_overheat", "event_cap"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "4B_overlay_success", "current_profile_verdict": "current_profile_4B_too_late", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R12L12C31_250000_20230615", "dedupe_for_aggregate": false, "aggregate_group_role": "4B_overlay_only", "is_new_independent_case": false, "reuse_reason": "same case, separate 4B timing audit", "independent_evidence_weight": 0.25, "do_not_count_as_new_case": true}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R12L12C31_277410_INSAN_SALT_PANIC_STAGE2", "trigger_id": "R12L12C31_277410_T1_STAGE2_ACTIONABLE", "symbol": "277410", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 10, "revision_score": 5, "relative_strength_score": 80, "customer_quality_score": 25, "policy_or_regulatory_score": 75, "valuation_repricing_score": 65, "execution_risk_score": 45, "legal_or_contract_risk_score": 20, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 5, "event_age_freshness_score": 70, "food_safety_demand_route_score": 65, "margin_pass_through_confirmation_score": 10, "event_cap_risk_score": 55}, "weighted_score_before": 74, "stage_label_before": "Stage2-Actionable", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 10, "revision_score": 5, "relative_strength_score": 80, "customer_quality_score": 25, "policy_or_regulatory_score": 75, "valuation_repricing_score": 65, "execution_risk_score": 45, "legal_or_contract_risk_score": 20, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 5, "event_age_freshness_score": 70, "food_safety_demand_route_score": 65, "margin_pass_through_confirmation_score": 10, "event_cap_risk_score": 80}, "weighted_score_after": 74, "stage_label_after": "Stage2-Actionable", "changed_components": ["event_age_freshness_score", "food_safety_demand_route_score", "margin_pass_through_confirmation_score", "event_cap_risk_score"], "component_delta_explanation": "C31 shadow caps public-health food-safety events unless fresh event timing, direct demand route, and margin/pass-through confirmation align; late release headlines are routed to event-cap/4B watch.", "MFE_90D_pct": 72.35, "MAE_90D_pct": -24.35, "score_return_alignment_label": "green_capped_after_shadow", "current_profile_verdict": "current_profile_4B_too_late"}
{"row_type": "score_simulation", "profile_id": "e2r_2_0_baseline_reference", "case_id": "R12L12C31_277410_INSAN_SALT_PANIC_STAGE2", "trigger_id": "R12L12C31_277410_T1_STAGE2_ACTIONABLE", "symbol": "277410", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 10, "revision_score": 5, "relative_strength_score": 80, "customer_quality_score": 25, "policy_or_regulatory_score": 75, "valuation_repricing_score": 65, "execution_risk_score": 45, "legal_or_contract_risk_score": 20, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 5, "event_age_freshness_score": 70, "food_safety_demand_route_score": 65, "margin_pass_through_confirmation_score": 10, "event_cap_risk_score": 55}, "weighted_score_before": 74, "stage_label_before": "Stage2-Actionable", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 10, "revision_score": 5, "relative_strength_score": 80, "customer_quality_score": 25, "policy_or_regulatory_score": 75, "valuation_repricing_score": 65, "execution_risk_score": 45, "legal_or_contract_risk_score": 20, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 5, "event_age_freshness_score": 70, "food_safety_demand_route_score": 65, "margin_pass_through_confirmation_score": 10, "event_cap_risk_score": 80}, "weighted_score_after": 74, "stage_label_after": "Stage2-Actionable", "changed_components": ["event_age_freshness_score", "food_safety_demand_route_score", "margin_pass_through_confirmation_score", "event_cap_risk_score"], "component_delta_explanation": "C31 shadow caps public-health food-safety events unless fresh event timing, direct demand route, and margin/pass-through confirmation align; late release headlines are routed to event-cap/4B watch.", "MFE_90D_pct": 72.35, "MAE_90D_pct": -24.35, "score_return_alignment_label": "green_capped_after_shadow", "current_profile_verdict": "current_profile_4B_too_late"}
{"row_type": "score_simulation", "profile_id": "sector_specific_candidate_profile", "case_id": "R12L12C31_277410_INSAN_SALT_PANIC_STAGE2", "trigger_id": "R12L12C31_277410_T1_STAGE2_ACTIONABLE", "symbol": "277410", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 10, "revision_score": 5, "relative_strength_score": 80, "customer_quality_score": 25, "policy_or_regulatory_score": 75, "valuation_repricing_score": 65, "execution_risk_score": 45, "legal_or_contract_risk_score": 20, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 5, "event_age_freshness_score": 70, "food_safety_demand_route_score": 65, "margin_pass_through_confirmation_score": 10, "event_cap_risk_score": 55}, "weighted_score_before": 74, "stage_label_before": "Stage2-Actionable", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 10, "revision_score": 5, "relative_strength_score": 80, "customer_quality_score": 25, "policy_or_regulatory_score": 75, "valuation_repricing_score": 65, "execution_risk_score": 45, "legal_or_contract_risk_score": 20, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 5, "event_age_freshness_score": 70, "food_safety_demand_route_score": 65, "margin_pass_through_confirmation_score": 10, "event_cap_risk_score": 80}, "weighted_score_after": 66, "stage_label_after": "Stage2-Actionable", "changed_components": ["event_age_freshness_score", "food_safety_demand_route_score", "margin_pass_through_confirmation_score", "event_cap_risk_score"], "component_delta_explanation": "C31 shadow caps public-health food-safety events unless fresh event timing, direct demand route, and margin/pass-through confirmation align; late release headlines are routed to event-cap/4B watch.", "MFE_90D_pct": 72.35, "MAE_90D_pct": -24.35, "score_return_alignment_label": "green_capped_after_shadow", "current_profile_verdict": "current_profile_4B_too_late"}
{"row_type": "score_simulation", "profile_id": "canonical_archetype_candidate_profile", "case_id": "R12L12C31_277410_INSAN_SALT_PANIC_STAGE2", "trigger_id": "R12L12C31_277410_T1_STAGE2_ACTIONABLE", "symbol": "277410", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 10, "revision_score": 5, "relative_strength_score": 80, "customer_quality_score": 25, "policy_or_regulatory_score": 75, "valuation_repricing_score": 65, "execution_risk_score": 45, "legal_or_contract_risk_score": 20, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 5, "event_age_freshness_score": 70, "food_safety_demand_route_score": 65, "margin_pass_through_confirmation_score": 10, "event_cap_risk_score": 55}, "weighted_score_before": 74, "stage_label_before": "Stage2-Actionable", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 10, "revision_score": 5, "relative_strength_score": 80, "customer_quality_score": 25, "policy_or_regulatory_score": 75, "valuation_repricing_score": 65, "execution_risk_score": 45, "legal_or_contract_risk_score": 20, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 5, "event_age_freshness_score": 70, "food_safety_demand_route_score": 65, "margin_pass_through_confirmation_score": 10, "event_cap_risk_score": 80}, "weighted_score_after": 66, "stage_label_after": "Stage2-Actionable", "changed_components": ["event_age_freshness_score", "food_safety_demand_route_score", "margin_pass_through_confirmation_score", "event_cap_risk_score"], "component_delta_explanation": "C31 shadow caps public-health food-safety events unless fresh event timing, direct demand route, and margin/pass-through confirmation align; late release headlines are routed to event-cap/4B watch.", "MFE_90D_pct": 72.35, "MAE_90D_pct": -24.35, "score_return_alignment_label": "green_capped_after_shadow", "current_profile_verdict": "current_profile_4B_too_late"}
{"row_type": "score_simulation", "profile_id": "counterexample_guard_profile", "case_id": "R12L12C31_277410_INSAN_SALT_PANIC_STAGE2", "trigger_id": "R12L12C31_277410_T1_STAGE2_ACTIONABLE", "symbol": "277410", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 10, "revision_score": 5, "relative_strength_score": 80, "customer_quality_score": 25, "policy_or_regulatory_score": 75, "valuation_repricing_score": 65, "execution_risk_score": 45, "legal_or_contract_risk_score": 20, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 5, "event_age_freshness_score": 70, "food_safety_demand_route_score": 65, "margin_pass_through_confirmation_score": 10, "event_cap_risk_score": 55}, "weighted_score_before": 74, "stage_label_before": "Stage2-Actionable", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 10, "revision_score": 5, "relative_strength_score": 80, "customer_quality_score": 25, "policy_or_regulatory_score": 75, "valuation_repricing_score": 65, "execution_risk_score": 45, "legal_or_contract_risk_score": 20, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 5, "event_age_freshness_score": 70, "food_safety_demand_route_score": 65, "margin_pass_through_confirmation_score": 10, "event_cap_risk_score": 80}, "weighted_score_after": 64, "stage_label_after": "Stage2-Actionable", "changed_components": ["event_age_freshness_score", "food_safety_demand_route_score", "margin_pass_through_confirmation_score", "event_cap_risk_score"], "component_delta_explanation": "C31 shadow caps public-health food-safety events unless fresh event timing, direct demand route, and margin/pass-through confirmation align; late release headlines are routed to event-cap/4B watch.", "MFE_90D_pct": 72.35, "MAE_90D_pct": -24.35, "score_return_alignment_label": "green_capped_after_shadow", "current_profile_verdict": "current_profile_4B_too_late"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R12L12C31_250000_BORATIAL_SALT_IMPORT_STAGE2", "trigger_id": "R12L12C31_250000_T1_STAGE2_ACTIONABLE", "symbol": "250000", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 10, "revision_score": 5, "relative_strength_score": 80, "customer_quality_score": 25, "policy_or_regulatory_score": 75, "valuation_repricing_score": 65, "execution_risk_score": 45, "legal_or_contract_risk_score": 20, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 5, "event_age_freshness_score": 70, "food_safety_demand_route_score": 65, "margin_pass_through_confirmation_score": 10, "event_cap_risk_score": 55}, "weighted_score_before": 74, "stage_label_before": "Stage2-Actionable", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 10, "revision_score": 5, "relative_strength_score": 80, "customer_quality_score": 25, "policy_or_regulatory_score": 75, "valuation_repricing_score": 65, "execution_risk_score": 45, "legal_or_contract_risk_score": 20, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 5, "event_age_freshness_score": 70, "food_safety_demand_route_score": 65, "margin_pass_through_confirmation_score": 10, "event_cap_risk_score": 80}, "weighted_score_after": 74, "stage_label_after": "Stage2-Actionable", "changed_components": ["event_age_freshness_score", "food_safety_demand_route_score", "margin_pass_through_confirmation_score", "event_cap_risk_score"], "component_delta_explanation": "C31 shadow caps public-health food-safety events unless fresh event timing, direct demand route, and margin/pass-through confirmation align; late release headlines are routed to event-cap/4B watch.", "MFE_90D_pct": 77.18, "MAE_90D_pct": -17.99, "score_return_alignment_label": "green_capped_after_shadow", "current_profile_verdict": "current_profile_4B_too_late"}
{"row_type": "score_simulation", "profile_id": "e2r_2_0_baseline_reference", "case_id": "R12L12C31_250000_BORATIAL_SALT_IMPORT_STAGE2", "trigger_id": "R12L12C31_250000_T1_STAGE2_ACTIONABLE", "symbol": "250000", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 10, "revision_score": 5, "relative_strength_score": 80, "customer_quality_score": 25, "policy_or_regulatory_score": 75, "valuation_repricing_score": 65, "execution_risk_score": 45, "legal_or_contract_risk_score": 20, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 5, "event_age_freshness_score": 70, "food_safety_demand_route_score": 65, "margin_pass_through_confirmation_score": 10, "event_cap_risk_score": 55}, "weighted_score_before": 74, "stage_label_before": "Stage2-Actionable", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 10, "revision_score": 5, "relative_strength_score": 80, "customer_quality_score": 25, "policy_or_regulatory_score": 75, "valuation_repricing_score": 65, "execution_risk_score": 45, "legal_or_contract_risk_score": 20, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 5, "event_age_freshness_score": 70, "food_safety_demand_route_score": 65, "margin_pass_through_confirmation_score": 10, "event_cap_risk_score": 80}, "weighted_score_after": 74, "stage_label_after": "Stage2-Actionable", "changed_components": ["event_age_freshness_score", "food_safety_demand_route_score", "margin_pass_through_confirmation_score", "event_cap_risk_score"], "component_delta_explanation": "C31 shadow caps public-health food-safety events unless fresh event timing, direct demand route, and margin/pass-through confirmation align; late release headlines are routed to event-cap/4B watch.", "MFE_90D_pct": 77.18, "MAE_90D_pct": -17.99, "score_return_alignment_label": "green_capped_after_shadow", "current_profile_verdict": "current_profile_4B_too_late"}
{"row_type": "score_simulation", "profile_id": "sector_specific_candidate_profile", "case_id": "R12L12C31_250000_BORATIAL_SALT_IMPORT_STAGE2", "trigger_id": "R12L12C31_250000_T1_STAGE2_ACTIONABLE", "symbol": "250000", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 10, "revision_score": 5, "relative_strength_score": 80, "customer_quality_score": 25, "policy_or_regulatory_score": 75, "valuation_repricing_score": 65, "execution_risk_score": 45, "legal_or_contract_risk_score": 20, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 5, "event_age_freshness_score": 70, "food_safety_demand_route_score": 65, "margin_pass_through_confirmation_score": 10, "event_cap_risk_score": 55}, "weighted_score_before": 74, "stage_label_before": "Stage2-Actionable", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 10, "revision_score": 5, "relative_strength_score": 80, "customer_quality_score": 25, "policy_or_regulatory_score": 75, "valuation_repricing_score": 65, "execution_risk_score": 45, "legal_or_contract_risk_score": 20, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 5, "event_age_freshness_score": 70, "food_safety_demand_route_score": 65, "margin_pass_through_confirmation_score": 10, "event_cap_risk_score": 80}, "weighted_score_after": 66, "stage_label_after": "Stage2-Actionable", "changed_components": ["event_age_freshness_score", "food_safety_demand_route_score", "margin_pass_through_confirmation_score", "event_cap_risk_score"], "component_delta_explanation": "C31 shadow caps public-health food-safety events unless fresh event timing, direct demand route, and margin/pass-through confirmation align; late release headlines are routed to event-cap/4B watch.", "MFE_90D_pct": 77.18, "MAE_90D_pct": -17.99, "score_return_alignment_label": "green_capped_after_shadow", "current_profile_verdict": "current_profile_4B_too_late"}
{"row_type": "score_simulation", "profile_id": "canonical_archetype_candidate_profile", "case_id": "R12L12C31_250000_BORATIAL_SALT_IMPORT_STAGE2", "trigger_id": "R12L12C31_250000_T1_STAGE2_ACTIONABLE", "symbol": "250000", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 10, "revision_score": 5, "relative_strength_score": 80, "customer_quality_score": 25, "policy_or_regulatory_score": 75, "valuation_repricing_score": 65, "execution_risk_score": 45, "legal_or_contract_risk_score": 20, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 5, "event_age_freshness_score": 70, "food_safety_demand_route_score": 65, "margin_pass_through_confirmation_score": 10, "event_cap_risk_score": 55}, "weighted_score_before": 74, "stage_label_before": "Stage2-Actionable", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 10, "revision_score": 5, "relative_strength_score": 80, "customer_quality_score": 25, "policy_or_regulatory_score": 75, "valuation_repricing_score": 65, "execution_risk_score": 45, "legal_or_contract_risk_score": 20, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 5, "event_age_freshness_score": 70, "food_safety_demand_route_score": 65, "margin_pass_through_confirmation_score": 10, "event_cap_risk_score": 80}, "weighted_score_after": 66, "stage_label_after": "Stage2-Actionable", "changed_components": ["event_age_freshness_score", "food_safety_demand_route_score", "margin_pass_through_confirmation_score", "event_cap_risk_score"], "component_delta_explanation": "C31 shadow caps public-health food-safety events unless fresh event timing, direct demand route, and margin/pass-through confirmation align; late release headlines are routed to event-cap/4B watch.", "MFE_90D_pct": 77.18, "MAE_90D_pct": -17.99, "score_return_alignment_label": "green_capped_after_shadow", "current_profile_verdict": "current_profile_4B_too_late"}
{"row_type": "score_simulation", "profile_id": "counterexample_guard_profile", "case_id": "R12L12C31_250000_BORATIAL_SALT_IMPORT_STAGE2", "trigger_id": "R12L12C31_250000_T1_STAGE2_ACTIONABLE", "symbol": "250000", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 10, "revision_score": 5, "relative_strength_score": 80, "customer_quality_score": 25, "policy_or_regulatory_score": 75, "valuation_repricing_score": 65, "execution_risk_score": 45, "legal_or_contract_risk_score": 20, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 5, "event_age_freshness_score": 70, "food_safety_demand_route_score": 65, "margin_pass_through_confirmation_score": 10, "event_cap_risk_score": 55}, "weighted_score_before": 74, "stage_label_before": "Stage2-Actionable", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 10, "revision_score": 5, "relative_strength_score": 80, "customer_quality_score": 25, "policy_or_regulatory_score": 75, "valuation_repricing_score": 65, "execution_risk_score": 45, "legal_or_contract_risk_score": 20, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 5, "event_age_freshness_score": 70, "food_safety_demand_route_score": 65, "margin_pass_through_confirmation_score": 10, "event_cap_risk_score": 80}, "weighted_score_after": 64, "stage_label_after": "Stage2-Actionable", "changed_components": ["event_age_freshness_score", "food_safety_demand_route_score", "margin_pass_through_confirmation_score", "event_cap_risk_score"], "component_delta_explanation": "C31 shadow caps public-health food-safety events unless fresh event timing, direct demand route, and margin/pass-through confirmation align; late release headlines are routed to event-cap/4B watch.", "MFE_90D_pct": 77.18, "MAE_90D_pct": -17.99, "score_return_alignment_label": "green_capped_after_shadow", "current_profile_verdict": "current_profile_4B_too_late"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R12L12C31_011150_CJSEAFOOD_RELEASE_FALSE_POSITIVE", "trigger_id": "R12L12C31_011150_T1_RELEASE_ANNOUNCEMENT", "symbol": "011150", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 5, "revision_score": 5, "relative_strength_score": 65, "customer_quality_score": 15, "policy_or_regulatory_score": 70, "valuation_repricing_score": 55, "execution_risk_score": 65, "legal_or_contract_risk_score": 30, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 5, "event_age_freshness_score": 25, "food_safety_demand_route_score": 25, "margin_pass_through_confirmation_score": 5, "event_cap_risk_score": 80}, "weighted_score_before": 76, "stage_label_before": "Stage3-Yellow", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 5, "revision_score": 5, "relative_strength_score": 65, "customer_quality_score": 15, "policy_or_regulatory_score": 70, "valuation_repricing_score": 55, "execution_risk_score": 65, "legal_or_contract_risk_score": 30, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 5, "event_age_freshness_score": 25, "food_safety_demand_route_score": 25, "margin_pass_through_confirmation_score": 0, "event_cap_risk_score": 90}, "weighted_score_after": 76, "stage_label_after": "Stage3-Yellow", "changed_components": ["event_age_freshness_score", "food_safety_demand_route_score", "margin_pass_through_confirmation_score", "event_cap_risk_score"], "component_delta_explanation": "C31 shadow caps public-health food-safety events unless fresh event timing, direct demand route, and margin/pass-through confirmation align; late release headlines are routed to event-cap/4B watch.", "MFE_90D_pct": 22.03, "MAE_90D_pct": -28.76, "score_return_alignment_label": "false_positive_reduced_after_shadow", "current_profile_verdict": "current_profile_false_positive"}
{"row_type": "score_simulation", "profile_id": "e2r_2_0_baseline_reference", "case_id": "R12L12C31_011150_CJSEAFOOD_RELEASE_FALSE_POSITIVE", "trigger_id": "R12L12C31_011150_T1_RELEASE_ANNOUNCEMENT", "symbol": "011150", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 5, "revision_score": 5, "relative_strength_score": 65, "customer_quality_score": 15, "policy_or_regulatory_score": 70, "valuation_repricing_score": 55, "execution_risk_score": 65, "legal_or_contract_risk_score": 30, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 5, "event_age_freshness_score": 25, "food_safety_demand_route_score": 25, "margin_pass_through_confirmation_score": 5, "event_cap_risk_score": 80}, "weighted_score_before": 76, "stage_label_before": "Stage3-Yellow", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 5, "revision_score": 5, "relative_strength_score": 65, "customer_quality_score": 15, "policy_or_regulatory_score": 70, "valuation_repricing_score": 55, "execution_risk_score": 65, "legal_or_contract_risk_score": 30, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 5, "event_age_freshness_score": 25, "food_safety_demand_route_score": 25, "margin_pass_through_confirmation_score": 0, "event_cap_risk_score": 90}, "weighted_score_after": 76, "stage_label_after": "Stage3-Yellow", "changed_components": ["event_age_freshness_score", "food_safety_demand_route_score", "margin_pass_through_confirmation_score", "event_cap_risk_score"], "component_delta_explanation": "C31 shadow caps public-health food-safety events unless fresh event timing, direct demand route, and margin/pass-through confirmation align; late release headlines are routed to event-cap/4B watch.", "MFE_90D_pct": 22.03, "MAE_90D_pct": -28.76, "score_return_alignment_label": "false_positive_reduced_after_shadow", "current_profile_verdict": "current_profile_false_positive"}
{"row_type": "score_simulation", "profile_id": "sector_specific_candidate_profile", "case_id": "R12L12C31_011150_CJSEAFOOD_RELEASE_FALSE_POSITIVE", "trigger_id": "R12L12C31_011150_T1_RELEASE_ANNOUNCEMENT", "symbol": "011150", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 5, "revision_score": 5, "relative_strength_score": 65, "customer_quality_score": 15, "policy_or_regulatory_score": 70, "valuation_repricing_score": 55, "execution_risk_score": 65, "legal_or_contract_risk_score": 30, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 5, "event_age_freshness_score": 25, "food_safety_demand_route_score": 25, "margin_pass_through_confirmation_score": 5, "event_cap_risk_score": 80}, "weighted_score_before": 76, "stage_label_before": "Stage3-Yellow", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 5, "revision_score": 5, "relative_strength_score": 65, "customer_quality_score": 15, "policy_or_regulatory_score": 70, "valuation_repricing_score": 55, "execution_risk_score": 65, "legal_or_contract_risk_score": 30, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 5, "event_age_freshness_score": 25, "food_safety_demand_route_score": 25, "margin_pass_through_confirmation_score": 0, "event_cap_risk_score": 90}, "weighted_score_after": 54, "stage_label_after": "Stage2-Watch", "changed_components": ["event_age_freshness_score", "food_safety_demand_route_score", "margin_pass_through_confirmation_score", "event_cap_risk_score"], "component_delta_explanation": "C31 shadow caps public-health food-safety events unless fresh event timing, direct demand route, and margin/pass-through confirmation align; late release headlines are routed to event-cap/4B watch.", "MFE_90D_pct": 22.03, "MAE_90D_pct": -28.76, "score_return_alignment_label": "false_positive_reduced_after_shadow", "current_profile_verdict": "current_profile_false_positive"}
{"row_type": "score_simulation", "profile_id": "canonical_archetype_candidate_profile", "case_id": "R12L12C31_011150_CJSEAFOOD_RELEASE_FALSE_POSITIVE", "trigger_id": "R12L12C31_011150_T1_RELEASE_ANNOUNCEMENT", "symbol": "011150", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 5, "revision_score": 5, "relative_strength_score": 65, "customer_quality_score": 15, "policy_or_regulatory_score": 70, "valuation_repricing_score": 55, "execution_risk_score": 65, "legal_or_contract_risk_score": 30, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 5, "event_age_freshness_score": 25, "food_safety_demand_route_score": 25, "margin_pass_through_confirmation_score": 5, "event_cap_risk_score": 80}, "weighted_score_before": 76, "stage_label_before": "Stage3-Yellow", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 5, "revision_score": 5, "relative_strength_score": 65, "customer_quality_score": 15, "policy_or_regulatory_score": 70, "valuation_repricing_score": 55, "execution_risk_score": 65, "legal_or_contract_risk_score": 30, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 5, "event_age_freshness_score": 25, "food_safety_demand_route_score": 25, "margin_pass_through_confirmation_score": 0, "event_cap_risk_score": 90}, "weighted_score_after": 54, "stage_label_after": "Stage2-Watch", "changed_components": ["event_age_freshness_score", "food_safety_demand_route_score", "margin_pass_through_confirmation_score", "event_cap_risk_score"], "component_delta_explanation": "C31 shadow caps public-health food-safety events unless fresh event timing, direct demand route, and margin/pass-through confirmation align; late release headlines are routed to event-cap/4B watch.", "MFE_90D_pct": 22.03, "MAE_90D_pct": -28.76, "score_return_alignment_label": "false_positive_reduced_after_shadow", "current_profile_verdict": "current_profile_false_positive"}
{"row_type": "score_simulation", "profile_id": "counterexample_guard_profile", "case_id": "R12L12C31_011150_CJSEAFOOD_RELEASE_FALSE_POSITIVE", "trigger_id": "R12L12C31_011150_T1_RELEASE_ANNOUNCEMENT", "symbol": "011150", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 5, "revision_score": 5, "relative_strength_score": 65, "customer_quality_score": 15, "policy_or_regulatory_score": 70, "valuation_repricing_score": 55, "execution_risk_score": 65, "legal_or_contract_risk_score": 30, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 5, "event_age_freshness_score": 25, "food_safety_demand_route_score": 25, "margin_pass_through_confirmation_score": 5, "event_cap_risk_score": 80}, "weighted_score_before": 76, "stage_label_before": "Stage3-Yellow", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 5, "revision_score": 5, "relative_strength_score": 65, "customer_quality_score": 15, "policy_or_regulatory_score": 70, "valuation_repricing_score": 55, "execution_risk_score": 65, "legal_or_contract_risk_score": 30, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 5, "event_age_freshness_score": 25, "food_safety_demand_route_score": 25, "margin_pass_through_confirmation_score": 0, "event_cap_risk_score": 90}, "weighted_score_after": 50, "stage_label_after": "Stage2-Watch", "changed_components": ["event_age_freshness_score", "food_safety_demand_route_score", "margin_pass_through_confirmation_score", "event_cap_risk_score"], "component_delta_explanation": "C31 shadow caps public-health food-safety events unless fresh event timing, direct demand route, and margin/pass-through confirmation align; late release headlines are routed to event-cap/4B watch.", "MFE_90D_pct": 22.03, "MAE_90D_pct": -28.76, "score_return_alignment_label": "false_positive_reduced_after_shadow", "current_profile_verdict": "current_profile_false_positive"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R12L12C31_014710_SAJOSEAFOOD_RELEASE_FALSE_POSITIVE", "trigger_id": "R12L12C31_014710_T1_RELEASE_ANNOUNCEMENT", "symbol": "014710", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 5, "revision_score": 5, "relative_strength_score": 65, "customer_quality_score": 15, "policy_or_regulatory_score": 70, "valuation_repricing_score": 55, "execution_risk_score": 65, "legal_or_contract_risk_score": 30, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 5, "event_age_freshness_score": 25, "food_safety_demand_route_score": 25, "margin_pass_through_confirmation_score": 5, "event_cap_risk_score": 80}, "weighted_score_before": 76, "stage_label_before": "Stage3-Yellow", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 5, "revision_score": 5, "relative_strength_score": 65, "customer_quality_score": 15, "policy_or_regulatory_score": 70, "valuation_repricing_score": 55, "execution_risk_score": 65, "legal_or_contract_risk_score": 30, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 5, "event_age_freshness_score": 25, "food_safety_demand_route_score": 25, "margin_pass_through_confirmation_score": 0, "event_cap_risk_score": 90}, "weighted_score_after": 76, "stage_label_after": "Stage3-Yellow", "changed_components": ["event_age_freshness_score", "food_safety_demand_route_score", "margin_pass_through_confirmation_score", "event_cap_risk_score"], "component_delta_explanation": "C31 shadow caps public-health food-safety events unless fresh event timing, direct demand route, and margin/pass-through confirmation align; late release headlines are routed to event-cap/4B watch.", "MFE_90D_pct": 28.17, "MAE_90D_pct": -26.88, "score_return_alignment_label": "false_positive_reduced_after_shadow", "current_profile_verdict": "current_profile_false_positive"}
{"row_type": "score_simulation", "profile_id": "e2r_2_0_baseline_reference", "case_id": "R12L12C31_014710_SAJOSEAFOOD_RELEASE_FALSE_POSITIVE", "trigger_id": "R12L12C31_014710_T1_RELEASE_ANNOUNCEMENT", "symbol": "014710", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 5, "revision_score": 5, "relative_strength_score": 65, "customer_quality_score": 15, "policy_or_regulatory_score": 70, "valuation_repricing_score": 55, "execution_risk_score": 65, "legal_or_contract_risk_score": 30, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 5, "event_age_freshness_score": 25, "food_safety_demand_route_score": 25, "margin_pass_through_confirmation_score": 5, "event_cap_risk_score": 80}, "weighted_score_before": 76, "stage_label_before": "Stage3-Yellow", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 5, "revision_score": 5, "relative_strength_score": 65, "customer_quality_score": 15, "policy_or_regulatory_score": 70, "valuation_repricing_score": 55, "execution_risk_score": 65, "legal_or_contract_risk_score": 30, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 5, "event_age_freshness_score": 25, "food_safety_demand_route_score": 25, "margin_pass_through_confirmation_score": 0, "event_cap_risk_score": 90}, "weighted_score_after": 76, "stage_label_after": "Stage3-Yellow", "changed_components": ["event_age_freshness_score", "food_safety_demand_route_score", "margin_pass_through_confirmation_score", "event_cap_risk_score"], "component_delta_explanation": "C31 shadow caps public-health food-safety events unless fresh event timing, direct demand route, and margin/pass-through confirmation align; late release headlines are routed to event-cap/4B watch.", "MFE_90D_pct": 28.17, "MAE_90D_pct": -26.88, "score_return_alignment_label": "false_positive_reduced_after_shadow", "current_profile_verdict": "current_profile_false_positive"}
{"row_type": "score_simulation", "profile_id": "sector_specific_candidate_profile", "case_id": "R12L12C31_014710_SAJOSEAFOOD_RELEASE_FALSE_POSITIVE", "trigger_id": "R12L12C31_014710_T1_RELEASE_ANNOUNCEMENT", "symbol": "014710", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 5, "revision_score": 5, "relative_strength_score": 65, "customer_quality_score": 15, "policy_or_regulatory_score": 70, "valuation_repricing_score": 55, "execution_risk_score": 65, "legal_or_contract_risk_score": 30, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 5, "event_age_freshness_score": 25, "food_safety_demand_route_score": 25, "margin_pass_through_confirmation_score": 5, "event_cap_risk_score": 80}, "weighted_score_before": 76, "stage_label_before": "Stage3-Yellow", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 5, "revision_score": 5, "relative_strength_score": 65, "customer_quality_score": 15, "policy_or_regulatory_score": 70, "valuation_repricing_score": 55, "execution_risk_score": 65, "legal_or_contract_risk_score": 30, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 5, "event_age_freshness_score": 25, "food_safety_demand_route_score": 25, "margin_pass_through_confirmation_score": 0, "event_cap_risk_score": 90}, "weighted_score_after": 54, "stage_label_after": "Stage2-Watch", "changed_components": ["event_age_freshness_score", "food_safety_demand_route_score", "margin_pass_through_confirmation_score", "event_cap_risk_score"], "component_delta_explanation": "C31 shadow caps public-health food-safety events unless fresh event timing, direct demand route, and margin/pass-through confirmation align; late release headlines are routed to event-cap/4B watch.", "MFE_90D_pct": 28.17, "MAE_90D_pct": -26.88, "score_return_alignment_label": "false_positive_reduced_after_shadow", "current_profile_verdict": "current_profile_false_positive"}
{"row_type": "score_simulation", "profile_id": "canonical_archetype_candidate_profile", "case_id": "R12L12C31_014710_SAJOSEAFOOD_RELEASE_FALSE_POSITIVE", "trigger_id": "R12L12C31_014710_T1_RELEASE_ANNOUNCEMENT", "symbol": "014710", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 5, "revision_score": 5, "relative_strength_score": 65, "customer_quality_score": 15, "policy_or_regulatory_score": 70, "valuation_repricing_score": 55, "execution_risk_score": 65, "legal_or_contract_risk_score": 30, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 5, "event_age_freshness_score": 25, "food_safety_demand_route_score": 25, "margin_pass_through_confirmation_score": 5, "event_cap_risk_score": 80}, "weighted_score_before": 76, "stage_label_before": "Stage3-Yellow", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 5, "revision_score": 5, "relative_strength_score": 65, "customer_quality_score": 15, "policy_or_regulatory_score": 70, "valuation_repricing_score": 55, "execution_risk_score": 65, "legal_or_contract_risk_score": 30, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 5, "event_age_freshness_score": 25, "food_safety_demand_route_score": 25, "margin_pass_through_confirmation_score": 0, "event_cap_risk_score": 90}, "weighted_score_after": 54, "stage_label_after": "Stage2-Watch", "changed_components": ["event_age_freshness_score", "food_safety_demand_route_score", "margin_pass_through_confirmation_score", "event_cap_risk_score"], "component_delta_explanation": "C31 shadow caps public-health food-safety events unless fresh event timing, direct demand route, and margin/pass-through confirmation align; late release headlines are routed to event-cap/4B watch.", "MFE_90D_pct": 28.17, "MAE_90D_pct": -26.88, "score_return_alignment_label": "false_positive_reduced_after_shadow", "current_profile_verdict": "current_profile_false_positive"}
{"row_type": "score_simulation", "profile_id": "counterexample_guard_profile", "case_id": "R12L12C31_014710_SAJOSEAFOOD_RELEASE_FALSE_POSITIVE", "trigger_id": "R12L12C31_014710_T1_RELEASE_ANNOUNCEMENT", "symbol": "014710", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 5, "revision_score": 5, "relative_strength_score": 65, "customer_quality_score": 15, "policy_or_regulatory_score": 70, "valuation_repricing_score": 55, "execution_risk_score": 65, "legal_or_contract_risk_score": 30, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 5, "event_age_freshness_score": 25, "food_safety_demand_route_score": 25, "margin_pass_through_confirmation_score": 5, "event_cap_risk_score": 80}, "weighted_score_before": 76, "stage_label_before": "Stage3-Yellow", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 5, "revision_score": 5, "relative_strength_score": 65, "customer_quality_score": 15, "policy_or_regulatory_score": 70, "valuation_repricing_score": 55, "execution_risk_score": 65, "legal_or_contract_risk_score": 30, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 5, "event_age_freshness_score": 25, "food_safety_demand_route_score": 25, "margin_pass_through_confirmation_score": 0, "event_cap_risk_score": 90}, "weighted_score_after": 50, "stage_label_after": "Stage2-Watch", "changed_components": ["event_age_freshness_score", "food_safety_demand_route_score", "margin_pass_through_confirmation_score", "event_cap_risk_score"], "component_delta_explanation": "C31 shadow caps public-health food-safety events unless fresh event timing, direct demand route, and margin/pass-through confirmation align; late release headlines are routed to event-cap/4B watch.", "MFE_90D_pct": 28.17, "MAE_90D_pct": -26.88, "score_return_alignment_label": "false_positive_reduced_after_shadow", "current_profile_verdict": "current_profile_false_positive"}
{"row_type": "residual_contribution", "round": "R12", "loop": "12", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "new_independent_case_count": 4, "reused_case_count": 0, "new_symbol_count": 4, "new_trigger_family_count": 2, "tested_existing_calibrated_axes": ["price_only_blowoff_blocks_positive_stage", "full_4b_requires_non_price_evidence", "hard_4c_thesis_break_routes_to_4c"], "residual_error_types_found": ["public_health_event_green_false_positive", "late_release_headline_low_residual_mfe", "event_4b_too_late_without_margin_bridge"], "loop_contribution_label": "canonical_archetype_rule_candidate", "do_not_propose_new_weight_delta": false}
```

### Shadow weight rows

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,C31_PUBLIC_HEALTH_EVENT_GREEN_CAP,canonical_archetype_specific,L10_POLICY_EVENT_CROSS_REDTEAM_MISC,C31_POLICY_SUBSIDY_LEGISLATION_EVENT,0,1,+1,"Do not promote Fukushima/salt/seafood public-health events to Stage3-Green unless fresh event timing plus direct demand route plus margin/pass-through confirmation are all present.","Reduced late-event false positives while preserving early salt-demand Stage2 watch MFE.","R12L12C31_277410_T1_STAGE2_ACTIONABLE|R12L12C31_250000_T1_STAGE2_ACTIONABLE|R12L12C31_011150_T1_RELEASE_ANNOUNCEMENT|R12L12C31_014710_T1_RELEASE_ANNOUNCEMENT",4,4,2,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,L10_EVENT_CAP_FAST_4B_ROUTER,sector_specific,L10_POLICY_EVENT_CROSS_REDTEAM_MISC,C31_POLICY_SUBSIDY_LEGISLATION_EVENT,0,1,+1,"If price reaches local event peak without non-price earnings bridge, route to 4B overlay even when Stage2 evidence was valid.","Improves 4B timing for 인산가/보라티알; prevents price-only late entries from being treated as durable positives.","R12L12C31_277410_T2_4B_OVERLAY|R12L12C31_250000_T2_4B_OVERLAY",2,2,0,medium,sector_shadow_only,"not production; post-calibrated residual"
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
completed_round = R12
completed_loop = 12
next_round = R13
next_loop = 12
round_schedule_status = valid
round_sector_consistency = pass
```

## 28. Source Notes

- Stock-Web manifest: source_name, price adjustment, min/max date, row counts, shard roots, and caveats were read from `atlas/manifest.json`.
- Stock-Web schema: tradable/raw columns and MFE/MAE formulas were read from `atlas/schema.json`.
- Symbol profile status was checked for 277410, 250000, 011150, and 014710.
- Historical event timing: AP reported South Korean protests and public concern after IAEA approval; AP/Time reported Japan began releasing treated Fukushima water on 2023-08-24; search snippets also noted salt/seafood hoarding ahead of the release. These are used only as historical trigger context.
- Quantitative price rows were taken from Songdaiki/stock-web tradable shards shown in this MD's Price Data Source Map.
