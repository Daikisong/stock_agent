# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
research_session = post_calibrated_sector_archetype_residual_research
output_format = one_standalone_markdown_file

scheduled_round = R9
scheduled_loop = 14
completed_round = R9
completed_loop = 14
next_round = R10
next_loop = 14

large_sector_id = L3_BATTERY_EV_GREEN_MOBILITY
canonical_archetype_id = C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE
fine_archetype_id = AUTO_AIRLINE_VOLUME_MIX_MARGIN_OPERATING_LEVERAGE

price_source = Songdaiki/stock-web
price_basis = tradable_raw
price_adjustment_status = raw_unadjusted_marcap
stock_web_manifest_max_date = 2026-02-20

stock_agent_code_access_allowed = false
stock_agent_code_patch_allowed = false
stock_agent_live_scan_allowed = false
production_scoring_changed = false
shadow_weight_only = true
handoff_prompt_embedded = true
handoff_prompt_executed_now = false

round_schedule_status = valid
round_sector_consistency = pass
```

This loop adds 3 new independent cases, 1 counterexample, and 3 residual errors for R9/L3_BATTERY_EV_GREEN_MOBILITY/C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE.

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

This file does not re-prove the global Stage2 bonus or the global Green threshold. It stress-tests whether those already-calibrated gates still leave a C29-specific residual: in mobility/transport, “volume” can be a real operating-leverage spark only when the volume path is joined to ASP/mix and margin conversion. Otherwise, volume is just traffic through a turnstile: busy, visible, and still economically thin.

## 2. Round / Large Sector / Canonical Archetype Scope

R9 is treated as the mobility / transport round. Under the v12 consistency gate, this run maps R9 to `L3_BATTERY_EV_GREEN_MOBILITY` because the selected cases are auto OEM and airline mobility cases rather than construction or real-estate cases.

```text
round = R9
loop = 14
large_sector_id = L3_BATTERY_EV_GREEN_MOBILITY
canonical_archetype_id = C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE
fine_archetype_id = AUTO_AIRLINE_VOLUME_MIX_MARGIN_OPERATING_LEVERAGE
```

Canonical compression:

```text
AUTO_EXPORT_MIX_MARGIN_OPERATING_LEVERAGE              -> C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE
AUTO_EXPORT_ASP_MARGIN_OPERATING_LEVERAGE              -> C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE
AIRLINE_REOPENING_LOAD_FACTOR_WITHOUT_MARGIN_CONVERSION -> C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE
```

## 3. Previous Coverage / Duplicate Avoidance Check

A repository search for `e2r_stock_web_v12_residual_round_R9_loop_14` returned no existing result file. A repository search for `C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE` returned no directly indexed prior v12 residual artifact in the accessible search result set.

Duplicate avoidance result:

```text
same_symbol_same_trigger_date_research = false
same_symbol_same_entry_group_research = false
same_evidence_family_repeat = false
new_independent_case_count = 3
new_symbol_count = 3
reused_case_count = 0
same_archetype_new_symbol_count = 3
same_archetype_new_trigger_family_count = 5
```

## 4. Stock-Web OHLC Input / Price Source Validation

The Stock-Web manifest was read first.

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

The file uses only `atlas/ohlcv_tradable_by_symbol_year` rows for quantitative calibration. Raw rows are not used for score calibration.

## 5. Historical Eligibility Gate

All representative triggers are historical, have entry rows in tradable shards, and have at least 180 trading days available before the Stock-Web manifest max date.

| symbol | company | profile_path | profile status | corporate action window check | calibration usable |
|---:|---|---|---|---|---|
| 005380 | 현대차 | atlas/symbol_profiles/005/005380.json | active_like, 2023 available, last_date 2026-02-20 | candidates only 1998-1999; no 2023 overlap | true |
| 000270 | 기아 | atlas/symbol_profiles/000/000270.json | active_like, 2023 available, last_date 2026-02-20 | candidates only 1999; no 2023 overlap | true |
| 089590 | 제주항공 | atlas/symbol_profiles/089/089590.json | active_like, 2023 available, last_date 2026-02-20 | latest candidate 2022-11-24; no 2023 180D overlap | true |

## 6. Canonical Archetype Compression Map

C29 should not be treated as a single “transport volume up = buy” bucket. The research split is:

1. **Auto OEM margin leverage**: vehicle volume / export mix / ASP / incentive discipline combine. When this bridge is visible, Stage2-Actionable can appear before formal Stage3-Green.
2. **Airline reopening volume**: passenger recovery or load factor can be obvious while earnings quality is still hostage to fuel, FX, debt, lease burden, and fare yield. This needs a margin-conversion guard.

The canonical rule candidate therefore compresses both positives and counterexample under C29:

```text
C29 = mobility volume path + durable margin conversion + manageable cost risk
not C29-Green = volume traffic alone
```

## 7. Case Selection Summary

| case_id | symbol | trigger_type | trigger_date | entry_date | entry_price | MFE_90D | MAE_90D | MFE_180D | MAE_180D | verdict |
|---|---:|---|---|---|---:|---:|---:|---:|---:|---|
| R9L14_C29_005380_2023_AUTO_MIX_MARGIN | 005380 | Stage2-Actionable | 2023-01-26 | 2023-01-26 | 174,900 | 20.93 | -4.75 | 20.93 | -4.75 | current_profile_too_late |
| R9L14_C29_000270_2023_AUTO_MIX_MARGIN | 000270 | Stage2-Actionable | 2023-01-26 | 2023-01-26 | 69,300 | 32.61 | -5.63 | 32.61 | -5.63 | current_profile_too_late |
| R9L14_C29_089590_2023_AIRLINE_REOPENING_VOLUME_FALSE_POSITIVE | 089590 | Stage2-Actionable | 2023-01-18 | 2023-01-18 | 16,350 | 5.93 | -22.26 | 5.93 | -42.57 | current_profile_false_positive |


Selected cases:

- Hyundai Motor and Kia are positive structural auto OEM cases where volume/mix/margin arrived before the formal full Green confirmation.
- Jeju Air is the counterexample: reopening volume was visible, but price action showed that traffic recovery without durable margin conversion was not enough.

## 8. Positive vs Counterexample Balance

```text
positive_case_count = 2
counterexample_count = 1
4B_case_count = 3
4C_case_count = 1
calibration_usable_case_count = 3
calibration_usable_trigger_count = 8
minimum_positive_case_count = pass
minimum_counterexample_count = pass
minimum_calibration_usable_case_count = pass
```

The balance is deliberate: C29 needs at least one visible false-positive archetype because “volume recovery” is an easy phrase for a model to over-credit. In autos, volume plus ASP/mix can feed operating profit like a gear train; in airlines, passenger recovery can simply spin the turbine faster while fuel and lease costs eat the thrust.

## 9. Evidence Source Map

| case | Stage2 evidence | Stage3 evidence | 4B evidence | 4C evidence |
|---|---|---|---|---|
| 현대차 | FY2022 / 4Q22 results, mix and margin bridge, relative strength | Q1 2023 margin/revision confirmation | local valuation/price peak only | none |
| 기아 | FY2022 / 4Q22 results, ASP and margin bridge, relative strength | Q1 2023 margin/revision confirmation | local valuation/price peak only | none |
| 제주항공 | reopening passenger recovery / load-factor narrative | not confirmed enough for Green | reopening-positioning / local price peak only | margin-conversion thesis failed after the stock was already deeply below entry |

## 10. Price Data Source Map

| symbol | company | price_shard_path | profile_path | entry anchor | peak / low anchors |
|---:|---|---|---|---|---|
| 005380 | 현대차 | atlas/ohlcv_tradable_by_symbol_year/005/005380/2023.csv | atlas/symbol_profiles/005/005380.json | 2023-01-26 close 174,900 | 2023-05-11 high 211,500; 2023-10-31 low 169,300 |
| 000270 | 기아 | atlas/ohlcv_tradable_by_symbol_year/000/000270/2023.csv | atlas/symbol_profiles/000/000270.json | 2023-01-26 close 69,300 | 2023-05-11 high 91,900; 2023-10-31 low 76,900 |
| 089590 | 제주항공 | atlas/ohlcv_tradable_by_symbol_year/089/089590/2023.csv | atlas/symbol_profiles/089/089590.json | 2023-01-18 close 16,350 | 2023-02-17 high 17,320; 2023-10-20 low 9,390 |

## 11. Case-by-Case Trigger Grid

| case_id | symbol | trigger_type | trigger_date | entry_date | entry_price | MFE_90D | MAE_90D | MFE_180D | MAE_180D | verdict |
|---|---:|---|---|---|---:|---:|---:|---:|---:|---|
| R9L14_C29_005380_2023_AUTO_MIX_MARGIN | 005380 | Stage2-Actionable | 2023-01-26 | 2023-01-26 | 174,900 | 20.93 | -4.75 | 20.93 | -4.75 | current_profile_too_late |
| R9L14_C29_000270_2023_AUTO_MIX_MARGIN | 000270 | Stage2-Actionable | 2023-01-26 | 2023-01-26 | 69,300 | 32.61 | -5.63 | 32.61 | -5.63 | current_profile_too_late |
| R9L14_C29_089590_2023_AIRLINE_REOPENING_VOLUME_FALSE_POSITIVE | 089590 | Stage2-Actionable | 2023-01-18 | 2023-01-18 | 16,350 | 5.93 | -22.26 | 5.93 | -42.57 | current_profile_false_positive |


## 12. Trigger-Level OHLC Backtest Tables

| symbol | entry | 30D MFE/MAE | 90D MFE/MAE | 180D MFE/MAE | peak | drawdown after peak | usable |
|---:|---:|---:|---:|---:|---|---:|---|
| 005380 | 174,900 | 2.92 / -4.75 | 20.93 / -4.75 | 20.93 / -4.75 | 2023-05-11 211,500 | -19.95 | true |
| 000270 | 69,300 | 14.43 / -5.63 | 32.61 / -5.63 | 32.61 / -5.63 | 2023-05-11 91,900 | -16.32 | true |
| 089590 | 16,350 | 5.93 / -5.57 | 5.93 / -22.26 | 5.93 / -42.57 | 2023-02-17 17,320 | -45.79 | true |


Aggregate representative-trigger backtest:

```text
representative_trigger_count = 3
avg_MFE_90D_pct = 19.82
avg_MAE_90D_pct = -10.88
avg_MFE_180D_pct = 19.82
avg_MAE_180D_pct = -17.65
```

Positive-only representative-trigger backtest:

```text
positive_cases = Hyundai + Kia
avg_positive_MFE_90D_pct = 26.77
avg_positive_MAE_90D_pct = -5.19
```

Counterexample representative-trigger backtest:

```text
Jeju_Air_MFE_180D_pct = 5.93
Jeju_Air_MAE_180D_pct = -42.57
Jeju_Air_drawdown_after_peak_pct = -45.79
```

## 13. Current Calibrated Profile Stress Test

| question | answer |
|---|---|
| How would current profile judge Hyundai / Kia? | It would likely wait for Stage3-Green confirmation through revision and margin visibility. |
| Was that aligned? | Directionally correct, but too late. Hyundai green_lateness_ratio = 0.713; Kia = 0.726. |
| Was Stage2 bonus too high? | Not for auto OEMs with margin bridge. It was too permissive for airline volume-only reopening. |
| Was Yellow threshold 75 too high/low? | Reasonable globally, but C29 needs a margin-conversion sub-gate. |
| Was Green threshold 87 / revision 55 too high/low? | Directionally safe, but auto margin cycles show useful Stage2-Actionable can happen before Green. |
| Was price-only blowoff guard appropriate? | Kept. Price-only 4B rows are overlay rows, not full thesis breaks. |
| Was full 4B non-price requirement appropriate? | Kept and strengthened. |
| Was hard 4C routing late/excessive? | For Jeju Air it was late; a C29 margin-conversion failure guard should degrade before hard 4C. |

Current profile verdicts:

```text
005380 = current_profile_too_late
000270 = current_profile_too_late
089590 = current_profile_false_positive
current_profile_error_count = 3
```

## 14. Stage2 / Yellow / Green Comparison

| symbol | Stage2 entry | Stage3-Green entry | peak | green_lateness_ratio | interpretation |
|---:|---:|---:|---:|---:|---|
| 005380 | 174,900 | 201,000 | 211,500 | 0.713 | Green caught confirmation, but gave up most Stage2-to-peak upside |
| 000270 | 69,300 | 85,700 | 91,900 | 0.726 | Green was directionally right but late |
| 089590 | 16,350 | not_applicable | 17,320 | not_applicable | No supported Green; volume-only signal should remain Stage2/watch |

Interpretation: C29 needs a **two-speed gearbox**. Auto OEMs with ASP/mix/margin bridge can move from Stage2 to Actionable before full Green. Airlines with only reopening volume should stay watch-only until margin quality is proven.

## 15. 4B Local vs Full-window Timing Audit

| symbol | 4B overlay date | 4B entry | local proximity | full-window proximity | evidence type | verdict |
|---:|---|---:|---:|---:|---|---|
| 005380 | 2023-05-11 | 208,000 | 0.904 | 0.904 | price_only, valuation_blowoff | price-only local 4B was near 180D peak but lacks thesis-break evidence |
| 000270 | 2023-05-11 | 90,100 | 0.92 | 0.92 | price_only, valuation_blowoff | local 4B would have been too early versus later 1Y high; keep non-price requirement |
| 089590 | 2023-02-17 | 17,080 | 0.753 | 0.753 | price_only, positioning_overheat | price-only local top was not enough; the missing guard was margin conversion, not price |

Conclusion:

```text
existing_axis_strengthened = full_4b_requires_non_price_evidence
existing_axis_kept = price_only_blowoff_blocks_positive_stage
```

## 16. 4C Protection Audit

Jeju Air 4C trigger:

```text
stage2_entry = 2023-01-18 close 16,350
peak = 2023-02-17 high 17,320
hard_4c_trigger = 2023-09-07 close 11,880
low_after_4c_90D = 9,390
MAE_90D_after_4C = -20.96%
drawdown_after_peak_from_prior_stage = -45.79%
four_c_protection_score = 0.542
four_c_protection_label = hard_4c_late
```

The 4C route protected some remaining downside, but it was late because the C29-specific error had occurred earlier: the model over-read passenger recovery as operating leverage before margin conversion existed.

## 17. Sector-Specific Rule Candidate

```text
sector_specific_rule_candidate = false
reason = sample is C29-specific but not yet broad enough across all L3 sub-sectors for sector-wide rule
```

## 18. Canonical-Archetype Rule Candidate

```text
canonical_archetype_rule_candidate = true
rule_scope = canonical_archetype_specific
canonical_archetype_id = C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE
```

Candidate rule:

```text
For C29, Stage2-Actionable may be promoted early only when volume route is paired with at least one durable profit bridge:
- ASP / mix improvement,
- margin bridge,
- cost absorption evidence,
- inventory / incentive discipline,
- or financial revision.

For airlines and other high-fixed-cost mobility names, passenger volume, load factor, or reopening demand alone cannot promote to Stage3-Green unless margin conversion and fuel/FX/cost risk are controlled.
```

Shadow axes:

```text
new_axis_proposed:
- c29_margin_conversion_required_for_green
- c29_auto_mix_asp_bonus
- c29_reopening_volume_without_margin_guard
```

## 19. Before / After Backtest Comparison

| profile_id | scope | eligible representative triggers | avg_MFE_90D | avg_MAE_90D | avg_MFE_180D | avg_MAE_180D | false_positive_rate | missed_structural_count | late_green_count | score_return_alignment_verdict |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| P0 e2r_2_1_stock_web_calibrated_proxy | global current | 3 | 19.82 | -10.88 | 19.82 | -17.65 | 0.33 | 0 | 2 | mixed: correct on autos, false positive risk on airline volume-only |
| P0b e2r_2_0_baseline_reference | rollback | 3 | 19.82 | -10.88 | 19.82 | -17.65 | 0.33+ | 0 | 1 | worse; volume-only Jeju would be more easily over-promoted |
| P1 sector_specific_candidate_profile | L3-only | 3 | 19.82 | -10.88 | 19.82 | -17.65 | 0.33 | 0 | 2 | insufficient; sector rule too broad |
| P2 canonical_archetype_candidate_profile | C29-only | 3 | 19.82 | -10.88 | 19.82 | -17.65 | 0.00 simulated | 0 | 2 | best: keeps auto Stage2 early, blocks Jeju Green |
| P3 counterexample_guard_profile | C29 guard | 3 | 19.82 | -10.88 | 19.82 | -17.65 | 0.00 simulated | 0 | 2 | defensive: reduces volume-only false positives |

## 20. Score-Return Alignment Matrix

| case | current profile | price outcome | residual |
|---|---|---|---|
| 현대차 | too late: Green waited for Q1 confirmation | +20.93% MFE_180D / -4.75% MAE_180D | Stage2 auto mix-margin signal deserved earlier actionable status |
| 기아 | too late: Green waited for Q1 confirmation | +32.61% MFE_180D / -5.63% MAE_180D | Same as Hyundai; auto ASP/mix bridge is earlier than full revision cycle |
| 제주항공 | false positive risk from volume-only reopening | +5.93% MFE_180D / -42.57% MAE_180D | Load-factor/passenger volume without margin conversion must be blocked from Green |


## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive_case_count | counterexample_count | 4B_case_count | 4C_case_count | new_independent_case_count | reused_case_count | calibration_usable_trigger_count | representative_trigger_count | current_profile_error_count | sector_rule_candidate | canonical_rule_candidate | coverage_gap_after_this_loop |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| L3_BATTERY_EV_GREEN_MOBILITY | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | AUTO_AIRLINE_VOLUME_MIX_MARGIN_OPERATING_LEVERAGE | 2 | 1 | 3 | 1 | 3 | 0 | 8 | 3 | 3 | false | true | C29 now has auto positive + airline counterexample balance; needs rail/logistics/shipping holdout later |


## 22. Residual Contribution Summary

```text
new_independent_case_count: 3
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 3
new_canonical_archetype_count: 1
new_fine_archetype_count: 3
new_trigger_family_count: 5

tested_existing_calibrated_axes:
- stage2_actionable_evidence_bonus
- stage3_green_revision_min
- price_only_blowoff_blocks_positive_stage
- full_4b_requires_non_price_evidence
- hard_4c_thesis_break_routes_to_4c

residual_error_types_found:
- green_late_for_auto_margin_confirmation
- volume_only_reopening_false_positive
- 4C_too_late_after_reopening_margin_failure

new_axis_proposed:
- c29_margin_conversion_required_for_green
- c29_auto_mix_asp_bonus
- c29_reopening_volume_without_margin_guard

existing_axis_strengthened:
- full_4b_requires_non_price_evidence
- price_only_blowoff_blocks_positive_stage

existing_axis_weakened: null
existing_axis_kept:
- stage3_green_revision_min
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
- actual stock-web tradable OHLC rows used
- entry_date / entry_price split from trigger_date
- 30D / 90D / 180D MFE and MAE
- peak date / peak price / drawdown after peak
- corporate-action overlap check by profile
- representative trigger dedupe
- Stage3-Green lateness audit
- 4B local vs full-window proximity split
- 4C protection label for counterexample
```

Not validated in this MD:

```text
- live candidate scan
- current 2026 watchlist
- broker execution
- production scoring code
- sector-wide L3 rule beyond C29
- global scoring rule promotion
```

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,c29_margin_conversion_required_for_green,canonical_archetype_specific,L3_BATTERY_EV_GREEN_MOBILITY,C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE,0,1,+1,"Auto/airline volume must convert to durable margin bridge before Green; blocks Jeju-type volume-only false positive while keeping Hyundai/Kia Stage2 Actionable","false_positive_rate reduced; Jeju score falls from Stage3-Yellow/near-Green to Stage2 watch","R9L14_C29_005380_T1_STAGE2_ACTIONABLE_20230126|R9L14_C29_000270_T1_STAGE2_ACTIONABLE_20230126|R9L14_C29_089590_T1_STAGE2_ACTIONABLE_20230118",3,3,1,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,c29_auto_mix_asp_bonus,canonical_archetype_specific,L3_BATTERY_EV_GREEN_MOBILITY,C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE,0,1,+1,"Autos with volume + ASP/mix + margin bridge showed strong MFE/controlled MAE; Stage2 should not wait for full Green confirmation","positive cases average MFE_90D > 25% for Hyundai/Kia while Green lateness exceeded 0.70","R9L14_C29_005380_T1_STAGE2_ACTIONABLE_20230126|R9L14_C29_000270_T1_STAGE2_ACTIONABLE_20230126",2,2,0,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,c29_reopening_volume_without_margin_guard,canonical_archetype_specific,L3_BATTERY_EV_GREEN_MOBILITY,C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE,0,1,+1,"Reopening passenger/load-factor recovery without cost/margin confirmation produced shallow MFE and deep MAE in Jeju Air","counterexample MFE_180D +5.93 vs MAE_180D -42.57","R9L14_C29_089590_T1_STAGE2_ACTIONABLE_20230118",1,1,1,medium,canonical_shadow_only,"not production; post-calibrated residual"
```

## 25. Machine-Readable Rows

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
{"row_type":"case","case_id":"R9L14_C29_005380_2023_AUTO_MIX_MARGIN","symbol":"005380","company_name":"현대차","round":"R9","loop":"14","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"AUTO_EXPORT_MIX_MARGIN_OPERATING_LEVERAGE","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"R9L14_C29_005380_T1_STAGE2_ACTIONABLE_20230126","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"aligned","current_profile_verdict":"current_profile_too_late","price_source":"Songdaiki/stock-web","notes":"FY2022 / 4Q22 results made the volume-mix-margin bridge visible; Q1 2023 confirmation later converted the thesis to Green but consumed much of the cycle upside."}
{"row_type":"case","case_id":"R9L14_C29_000270_2023_AUTO_MIX_MARGIN","symbol":"000270","company_name":"기아","round":"R9","loop":"14","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"AUTO_EXPORT_ASP_MARGIN_OPERATING_LEVERAGE","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"R9L14_C29_000270_T1_STAGE2_ACTIONABLE_20230126","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"aligned","current_profile_verdict":"current_profile_too_late","price_source":"Songdaiki/stock-web","notes":"FY2022 / 4Q22 profit quality created the first actionable auto operating-leverage trigger; Q1 2023 confirmed margins but the Green trigger occurred after most 180D upside had already been priced."}
{"row_type":"case","case_id":"R9L14_C29_089590_2023_AIRLINE_REOPENING_VOLUME_FALSE_POSITIVE","symbol":"089590","company_name":"제주항공","round":"R9","loop":"14","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"AIRLINE_REOPENING_LOAD_FACTOR_WITHOUT_MARGIN_CONVERSION","case_type":"false_positive_green","positive_or_counterexample":"counterexample","best_trigger":"R9L14_C29_089590_T1_STAGE2_ACTIONABLE_20230118","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"misaligned_volume_only_false_positive","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"Passenger recovery / reopening traffic created a volume trigger, but margin conversion was not sufficiently confirmed. The stock made only a shallow MFE and then a deep MAE, showing that C29 must separate load-factor or volume recovery from durable operating leverage."}
{"row_type":"trigger","trigger_id":"R9L14_C29_005380_T1_STAGE2_ACTIONABLE_20230126","case_id":"R9L14_C29_005380_2023_AUTO_MIX_MARGIN","symbol":"005380","company_name":"현대차","round":"R9","loop":"14","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"AUTO_EXPORT_MIX_MARGIN_OPERATING_LEVERAGE","sector":"Auto OEM","primary_archetype":"mobility_volume_margin_operating_leverage","loop_objective":"coverage_gap_fill|counterexample_mining|canonical_archetype_compression","trigger_type":"Stage2-Actionable","trigger_date":"2023-01-26","evidence_available_at_that_date":"FY2022 / 4Q22 results made the volume-mix-margin bridge visible; Q1 2023 confirmation later converted the thesis to Green but consumed much of the cycle upside.","evidence_source":"Hyundai Motor 2022 results / Q1 2023 results public release; stock-web OHLC shard anchors.","stage2_evidence_fields":["public_event_or_disclosure","customer_or_order_quality","relative_strength","capacity_or_volume_route","early_revision_signal"],"stage3_evidence_fields":["confirmed_revision","margin_bridge","multiple_public_sources","financial_visibility","low_red_team_risk"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/005/005380/2023.csv","profile_path":"atlas/symbol_profiles/005/005380.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2023-01-26","entry_price":174900,"MFE_30D_pct":2.92,"MFE_90D_pct":20.93,"MFE_180D_pct":20.93,"MFE_1Y_pct":20.93,"MFE_2Y_pct":null,"MAE_30D_pct":-4.75,"MAE_90D_pct":-4.75,"MAE_180D_pct":-4.75,"MAE_1Y_pct":-4.75,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2023-05-11","peak_price":211500,"drawdown_after_peak_pct":-19.95,"green_lateness_ratio":0.713,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":null,"four_b_evidence_type":[],"four_c_protection_label":null,"trigger_outcome_label":"structural_success_but_green_late","current_profile_verdict":"current_profile_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R9L14_C29_005380_2023_AUTO_MIX_MARGIN_ENTRY_2023-01-26","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"R9L14_C29_005380_T2_STAGE3_GREEN_20230425","case_id":"R9L14_C29_005380_2023_AUTO_MIX_MARGIN","symbol":"005380","company_name":"현대차","round":"R9","loop":"14","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"AUTO_EXPORT_MIX_MARGIN_OPERATING_LEVERAGE","sector":"Auto OEM","primary_archetype":"mobility_volume_margin_operating_leverage","loop_objective":"green_strictness_stress_test","trigger_type":"Stage3-Green","trigger_date":"2023-04-25","evidence_available_at_that_date":"confirmed revision and margin bridge were visible, but after much of the 180D move from Stage2 entry had already occurred.","evidence_source":"Hyundai Motor 2022 results / Q1 2023 results public release; stock-web OHLC shard anchors.","stage2_evidence_fields":["public_event_or_disclosure","customer_or_order_quality","relative_strength","capacity_or_volume_route","early_revision_signal"],"stage3_evidence_fields":["confirmed_revision","margin_bridge","multiple_public_sources","financial_visibility","low_red_team_risk"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/005/005380/2023.csv","profile_path":"atlas/symbol_profiles/005/005380.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2023-04-25","entry_price":201000,"MFE_30D_pct":5.22,"MFE_90D_pct":5.22,"MFE_180D_pct":5.22,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":null,"MAE_90D_pct":-15.77,"MAE_180D_pct":-15.77,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2023-05-11","peak_price":211500,"drawdown_after_peak_pct":-19.95,"green_lateness_ratio":0.713,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":null,"four_b_evidence_type":[],"four_c_protection_label":null,"trigger_outcome_label":"late_green_confirmation","current_profile_verdict":"current_profile_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R9L14_C29_005380_2023_AUTO_MIX_MARGIN_GREEN_2023-04-25","dedupe_for_aggregate":false,"aggregate_group_role":"label_comparison_only","is_new_independent_case":true,"reuse_reason":"same case, distinct Stage3-Green lateness comparison","independent_evidence_weight":0.25,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"R9L14_C29_005380_T3_4B_PRICE_LOCAL_20230511","case_id":"R9L14_C29_005380_2023_AUTO_MIX_MARGIN","symbol":"005380","company_name":"현대차","round":"R9","loop":"14","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"AUTO_EXPORT_MIX_MARGIN_OPERATING_LEVERAGE","sector":"Auto OEM","primary_archetype":"mobility_volume_margin_operating_leverage","loop_objective":"4B_non_price_requirement_stress_test","trigger_type":"Stage4B-overlay","trigger_date":"2023-05-11","evidence_available_at_that_date":"price local peak / valuation stretch overlay only; no hard thesis break on the date.","evidence_source":"Hyundai Motor 2022 results / Q1 2023 results public release; stock-web OHLC shard anchors.","stage2_evidence_fields":[],"stage3_evidence_fields":[],"stage4b_evidence_fields":["valuation_blowoff","price_only_local_peak"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/005/005380/2023.csv","profile_path":"atlas/symbol_profiles/005/005380.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2023-05-11","entry_price":208000,"MFE_30D_pct":1.68,"MFE_90D_pct":1.68,"MFE_180D_pct":1.68,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":null,"MAE_90D_pct":-18.61,"MAE_180D_pct":-18.61,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2023-05-11","peak_price":211500,"drawdown_after_peak_pct":-19.95,"green_lateness_ratio":0.713,"four_b_local_peak_proximity":0.904,"four_b_full_window_peak_proximity":0.904,"four_b_timing_verdict":"price_only_local_4B_ambiguous_keep_non_price_guard","four_b_evidence_type":["price_only","valuation_blowoff"],"four_c_protection_label":null,"trigger_outcome_label":"4B_overlay_only","current_profile_verdict":"current_profile_4B_too_early","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R9L14_C29_005380_2023_AUTO_MIX_MARGIN_4B_2023-05-11","dedupe_for_aggregate":false,"aggregate_group_role":"4B_overlay_only","is_new_independent_case":true,"reuse_reason":"same case, distinct 4B overlay timing audit","independent_evidence_weight":0.25,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"R9L14_C29_000270_T1_STAGE2_ACTIONABLE_20230126","case_id":"R9L14_C29_000270_2023_AUTO_MIX_MARGIN","symbol":"000270","company_name":"기아","round":"R9","loop":"14","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"AUTO_EXPORT_ASP_MARGIN_OPERATING_LEVERAGE","sector":"Auto OEM","primary_archetype":"mobility_volume_margin_operating_leverage","loop_objective":"coverage_gap_fill|counterexample_mining|canonical_archetype_compression","trigger_type":"Stage2-Actionable","trigger_date":"2023-01-26","evidence_available_at_that_date":"FY2022 / 4Q22 profit quality created the first actionable auto operating-leverage trigger; Q1 2023 confirmed margins but the Green trigger occurred after most 180D upside had already been priced.","evidence_source":"Kia 2022 results / Q1 2023 results public release; stock-web OHLC shard anchors.","stage2_evidence_fields":["public_event_or_disclosure","customer_or_order_quality","relative_strength","capacity_or_volume_route","early_revision_signal"],"stage3_evidence_fields":["confirmed_revision","margin_bridge","financial_visibility","repeat_order_or_conversion","low_red_team_risk"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/000/000270/2023.csv","profile_path":"atlas/symbol_profiles/000/000270.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2023-01-26","entry_price":69300,"MFE_30D_pct":14.43,"MFE_90D_pct":32.61,"MFE_180D_pct":32.61,"MFE_1Y_pct":45.6,"MFE_2Y_pct":null,"MAE_30D_pct":-5.63,"MAE_90D_pct":-5.63,"MAE_180D_pct":-5.63,"MAE_1Y_pct":-5.63,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2023-05-11","peak_price":91900,"drawdown_after_peak_pct":-16.32,"green_lateness_ratio":0.726,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":null,"four_b_evidence_type":[],"four_c_protection_label":null,"trigger_outcome_label":"structural_success_but_green_late","current_profile_verdict":"current_profile_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R9L14_C29_000270_2023_AUTO_MIX_MARGIN_ENTRY_2023-01-26","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"R9L14_C29_000270_T2_STAGE3_GREEN_20230426","case_id":"R9L14_C29_000270_2023_AUTO_MIX_MARGIN","symbol":"000270","company_name":"기아","round":"R9","loop":"14","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"AUTO_EXPORT_ASP_MARGIN_OPERATING_LEVERAGE","sector":"Auto OEM","primary_archetype":"mobility_volume_margin_operating_leverage","loop_objective":"green_strictness_stress_test","trigger_type":"Stage3-Green","trigger_date":"2023-04-26","evidence_available_at_that_date":"confirmed revision and margin bridge were visible, but after much of the 180D move from Stage2 entry had already occurred.","evidence_source":"Kia 2022 results / Q1 2023 results public release; stock-web OHLC shard anchors.","stage2_evidence_fields":["public_event_or_disclosure","customer_or_order_quality","relative_strength","capacity_or_volume_route","early_revision_signal"],"stage3_evidence_fields":["confirmed_revision","margin_bridge","financial_visibility","repeat_order_or_conversion","low_red_team_risk"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/000/000270/2023.csv","profile_path":"atlas/symbol_profiles/000/000270.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2023-04-26","entry_price":85700,"MFE_30D_pct":7.23,"MFE_90D_pct":7.23,"MFE_180D_pct":7.23,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":null,"MAE_90D_pct":-10.27,"MAE_180D_pct":-10.27,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2023-05-11","peak_price":91900,"drawdown_after_peak_pct":-16.32,"green_lateness_ratio":0.726,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":null,"four_b_evidence_type":[],"four_c_protection_label":null,"trigger_outcome_label":"late_green_confirmation","current_profile_verdict":"current_profile_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R9L14_C29_000270_2023_AUTO_MIX_MARGIN_GREEN_2023-04-26","dedupe_for_aggregate":false,"aggregate_group_role":"label_comparison_only","is_new_independent_case":true,"reuse_reason":"same case, distinct Stage3-Green lateness comparison","independent_evidence_weight":0.25,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"R9L14_C29_000270_T3_4B_PRICE_LOCAL_20230511","case_id":"R9L14_C29_000270_2023_AUTO_MIX_MARGIN","symbol":"000270","company_name":"기아","round":"R9","loop":"14","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"AUTO_EXPORT_ASP_MARGIN_OPERATING_LEVERAGE","sector":"Auto OEM","primary_archetype":"mobility_volume_margin_operating_leverage","loop_objective":"4B_non_price_requirement_stress_test","trigger_type":"Stage4B-overlay","trigger_date":"2023-05-11","evidence_available_at_that_date":"price local peak / valuation stretch overlay only; no hard thesis break on the date.","evidence_source":"Kia 2022 results / Q1 2023 results public release; stock-web OHLC shard anchors.","stage2_evidence_fields":[],"stage3_evidence_fields":[],"stage4b_evidence_fields":["valuation_blowoff","price_only_local_peak"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/000/000270/2023.csv","profile_path":"atlas/symbol_profiles/000/000270.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2023-05-11","entry_price":90100,"MFE_30D_pct":2.0,"MFE_90D_pct":2.0,"MFE_180D_pct":2.0,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":null,"MAE_90D_pct":-14.65,"MAE_180D_pct":-14.65,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2023-05-11","peak_price":91900,"drawdown_after_peak_pct":-16.32,"green_lateness_ratio":0.726,"four_b_local_peak_proximity":0.92,"four_b_full_window_peak_proximity":0.92,"four_b_timing_verdict":"price_only_local_4B_too_early_for_full_cycle_because_1Y_peak_later","four_b_evidence_type":["price_only","valuation_blowoff"],"four_c_protection_label":null,"trigger_outcome_label":"4B_overlay_only","current_profile_verdict":"current_profile_4B_too_early","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R9L14_C29_000270_2023_AUTO_MIX_MARGIN_4B_2023-05-11","dedupe_for_aggregate":false,"aggregate_group_role":"4B_overlay_only","is_new_independent_case":true,"reuse_reason":"same case, distinct 4B overlay timing audit","independent_evidence_weight":0.25,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"R9L14_C29_089590_T1_STAGE2_ACTIONABLE_20230118","case_id":"R9L14_C29_089590_2023_AIRLINE_REOPENING_VOLUME_FALSE_POSITIVE","symbol":"089590","company_name":"제주항공","round":"R9","loop":"14","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"AIRLINE_REOPENING_LOAD_FACTOR_WITHOUT_MARGIN_CONVERSION","sector":"Airline / low-cost carrier","primary_archetype":"mobility_volume_margin_operating_leverage","loop_objective":"coverage_gap_fill|counterexample_mining|canonical_archetype_compression","trigger_type":"Stage2-Actionable","trigger_date":"2023-01-18","evidence_available_at_that_date":"Passenger recovery / reopening traffic created a volume trigger, but margin conversion was not sufficiently confirmed. The stock made only a shallow MFE and then a deep MAE, showing that C29 must separate load-factor or volume recovery from durable operating leverage.","evidence_source":"2023 reopening passenger recovery narrative; Jeju Air financial / traffic disclosures; stock-web OHLC shard anchors.","stage2_evidence_fields":["public_event_or_disclosure","capacity_or_volume_route","relative_strength"],"stage3_evidence_fields":[],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/089/089590/2023.csv","profile_path":"atlas/symbol_profiles/089/089590.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2023-01-18","entry_price":16350,"MFE_30D_pct":5.93,"MFE_90D_pct":5.93,"MFE_180D_pct":5.93,"MFE_1Y_pct":5.93,"MFE_2Y_pct":null,"MAE_30D_pct":-5.57,"MAE_90D_pct":-22.26,"MAE_180D_pct":-42.57,"MAE_1Y_pct":-42.57,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2023-02-17","peak_price":17320,"drawdown_after_peak_pct":-45.79,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":null,"four_b_evidence_type":[],"four_c_protection_label":null,"trigger_outcome_label":"volume_recovery_failed_rerating","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R9L14_C29_089590_2023_AIRLINE_REOPENING_VOLUME_FALSE_POSITIVE_ENTRY_2023-01-18","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"R9L14_C29_089590_T2_4B_PRICE_LOCAL_20230217","case_id":"R9L14_C29_089590_2023_AIRLINE_REOPENING_VOLUME_FALSE_POSITIVE","symbol":"089590","company_name":"제주항공","round":"R9","loop":"14","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"AIRLINE_REOPENING_LOAD_FACTOR_WITHOUT_MARGIN_CONVERSION","sector":"Airline / low-cost carrier","primary_archetype":"mobility_volume_margin_operating_leverage","loop_objective":"4B_non_price_requirement_stress_test","trigger_type":"Stage4B-overlay","trigger_date":"2023-02-17","evidence_available_at_that_date":"price local peak / valuation stretch overlay only; no hard thesis break on the date.","evidence_source":"2023 reopening passenger recovery narrative; Jeju Air financial / traffic disclosures; stock-web OHLC shard anchors.","stage2_evidence_fields":[],"stage3_evidence_fields":[],"stage4b_evidence_fields":["positioning_overheat","price_only_local_peak"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/089/089590/2023.csv","profile_path":"atlas/symbol_profiles/089/089590.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2023-02-17","entry_price":17080,"MFE_30D_pct":1.41,"MFE_90D_pct":1.41,"MFE_180D_pct":1.41,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":null,"MAE_90D_pct":-45.02,"MAE_180D_pct":-45.02,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2023-02-17","peak_price":17320,"drawdown_after_peak_pct":-45.79,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":0.753,"four_b_full_window_peak_proximity":0.753,"four_b_timing_verdict":"price_only_local_4B_should_not_be_full_4B_but_reopening_volume_needed_margin_guard","four_b_evidence_type":["price_only","positioning_overheat"],"four_c_protection_label":null,"trigger_outcome_label":"4B_overlay_only","current_profile_verdict":"current_profile_4B_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R9L14_C29_089590_2023_AIRLINE_REOPENING_VOLUME_FALSE_POSITIVE_4B_2023-02-17","dedupe_for_aggregate":false,"aggregate_group_role":"4B_overlay_only","is_new_independent_case":true,"reuse_reason":"same case, distinct 4B overlay timing audit","independent_evidence_weight":0.25,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"R9L14_C29_089590_T3_4C_THESIS_BREAK_20230907","case_id":"R9L14_C29_089590_2023_AIRLINE_REOPENING_VOLUME_FALSE_POSITIVE","symbol":"089590","company_name":"제주항공","round":"R9","loop":"14","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"AIRLINE_REOPENING_LOAD_FACTOR_WITHOUT_MARGIN_CONVERSION","sector":"Airline / low-cost carrier","primary_archetype":"mobility_volume_margin_operating_leverage","loop_objective":"4C_thesis_break_timing_test","trigger_type":"Stage4C","trigger_date":"2023-09-07","evidence_available_at_that_date":"volume recovery thesis had failed to convert to durable margin; price was already far below Stage2 entry.","evidence_source":"2023 reopening passenger recovery narrative; Jeju Air financial / traffic disclosures; stock-web OHLC shard anchors.","stage2_evidence_fields":[],"stage3_evidence_fields":[],"stage4b_evidence_fields":[],"stage4c_evidence_fields":["thesis_evidence_broken"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/089/089590/2023.csv","profile_path":"atlas/symbol_profiles/089/089590.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2023-09-07","entry_price":11880,"MFE_30D_pct":1.35,"MFE_90D_pct":1.35,"MFE_180D_pct":1.35,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-20.96,"MAE_90D_pct":-20.96,"MAE_180D_pct":-20.96,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2023-02-17","peak_price":17320,"drawdown_after_peak_pct":-45.79,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":null,"four_b_evidence_type":[],"four_c_protection_label":"hard_4c_late; protection_score=0.542","trigger_outcome_label":"4C_late","current_profile_verdict":"current_profile_4C_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R9L14_C29_089590_2023_AIRLINE_REOPENING_VOLUME_FALSE_POSITIVE_4C_2023-09-07","dedupe_for_aggregate":false,"aggregate_group_role":"4C_overlay_only","is_new_independent_case":true,"reuse_reason":"same case, distinct thesis-break timing audit","independent_evidence_weight":0.25,"do_not_count_as_new_case":false}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R9L14_C29_005380_2023_AUTO_MIX_MARGIN","trigger_id":"R9L14_C29_005380_T1_STAGE2_ACTIONABLE_20230126","symbol":"005380","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":20,"margin_bridge_score":62,"revision_score":54,"relative_strength_score":56,"customer_quality_score":58,"policy_or_regulatory_score":18,"valuation_repricing_score":45,"execution_risk_score":14,"legal_or_contract_risk_score":6,"dilution_cb_risk_score":0,"accounting_trust_risk_score":4,"volume_route_score":57,"mix_asp_score":63,"margin_conversion_score":62,"load_factor_quality_score":"unknown_or_not_supported","fuel_fx_cost_risk_score":10},"weighted_score_before":79.0,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":20,"margin_bridge_score":62,"revision_score":57,"relative_strength_score":56,"customer_quality_score":58,"policy_or_regulatory_score":18,"valuation_repricing_score":45,"execution_risk_score":14,"legal_or_contract_risk_score":6,"dilution_cb_risk_score":0,"accounting_trust_risk_score":4,"volume_route_score":57,"mix_asp_score":66,"margin_conversion_score":68,"load_factor_quality_score":"unknown_or_not_supported","fuel_fx_cost_risk_score":10},"weighted_score_after":83.0,"stage_label_after":"Stage3-Yellow","changed_components":["margin_conversion_score","mix_asp_score","load_factor_quality_score","fuel_fx_cost_risk_score","c29_volume_without_margin_guard"],"component_delta_explanation":"C29 shadow profile rewards durable margin conversion in autos but penalizes volume-only airline reopening without fuel/FX/margin confirmation.","MFE_90D_pct":20.93,"MAE_90D_pct":-4.75,"score_return_alignment_label":"aligned","current_profile_verdict":"current_profile_too_late"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R9L14_C29_000270_2023_AUTO_MIX_MARGIN","trigger_id":"R9L14_C29_000270_T1_STAGE2_ACTIONABLE_20230126","symbol":"000270","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":18,"margin_bridge_score":65,"revision_score":57,"relative_strength_score":60,"customer_quality_score":58,"policy_or_regulatory_score":15,"valuation_repricing_score":50,"execution_risk_score":13,"legal_or_contract_risk_score":5,"dilution_cb_risk_score":0,"accounting_trust_risk_score":4,"volume_route_score":60,"mix_asp_score":66,"margin_conversion_score":67,"load_factor_quality_score":"unknown_or_not_supported","fuel_fx_cost_risk_score":11},"weighted_score_before":81.5,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":18,"margin_bridge_score":65,"revision_score":61,"relative_strength_score":60,"customer_quality_score":58,"policy_or_regulatory_score":15,"valuation_repricing_score":50,"execution_risk_score":13,"legal_or_contract_risk_score":5,"dilution_cb_risk_score":0,"accounting_trust_risk_score":4,"volume_route_score":60,"mix_asp_score":70,"margin_conversion_score":72,"load_factor_quality_score":"unknown_or_not_supported","fuel_fx_cost_risk_score":11},"weighted_score_after":85.5,"stage_label_after":"Stage3-Yellow","changed_components":["margin_conversion_score","mix_asp_score","load_factor_quality_score","fuel_fx_cost_risk_score","c29_volume_without_margin_guard"],"component_delta_explanation":"C29 shadow profile rewards durable margin conversion in autos but penalizes volume-only airline reopening without fuel/FX/margin confirmation.","MFE_90D_pct":32.61,"MAE_90D_pct":-5.63,"score_return_alignment_label":"aligned","current_profile_verdict":"current_profile_too_late"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R9L14_C29_089590_2023_AIRLINE_REOPENING_VOLUME_FALSE_POSITIVE","trigger_id":"R9L14_C29_089590_T1_STAGE2_ACTIONABLE_20230118","symbol":"089590","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":5,"margin_bridge_score":18,"revision_score":12,"relative_strength_score":52,"customer_quality_score":22,"policy_or_regulatory_score":20,"valuation_repricing_score":36,"execution_risk_score":54,"legal_or_contract_risk_score":6,"dilution_cb_risk_score":10,"accounting_trust_risk_score":5,"volume_route_score":58,"mix_asp_score":18,"margin_conversion_score":12,"load_factor_quality_score":36,"fuel_fx_cost_risk_score":60},"weighted_score_before":74.5,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":5,"margin_bridge_score":18,"revision_score":12,"relative_strength_score":35,"customer_quality_score":22,"policy_or_regulatory_score":20,"valuation_repricing_score":36,"execution_risk_score":66,"legal_or_contract_risk_score":6,"dilution_cb_risk_score":10,"accounting_trust_risk_score":5,"volume_route_score":58,"mix_asp_score":18,"margin_conversion_score":4,"load_factor_quality_score":36,"fuel_fx_cost_risk_score":70},"weighted_score_after":61.0,"stage_label_after":"Stage2","changed_components":["margin_conversion_score","mix_asp_score","load_factor_quality_score","fuel_fx_cost_risk_score","c29_volume_without_margin_guard"],"component_delta_explanation":"C29 shadow profile rewards durable margin conversion in autos but penalizes volume-only airline reopening without fuel/FX/margin confirmation.","MFE_90D_pct":5.93,"MAE_90D_pct":-22.26,"score_return_alignment_label":"corrected_by_shadow_guard","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"residual_contribution","round":"R9","loop":"14","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","new_independent_case_count":3,"reused_case_count":0,"new_symbol_count":3,"new_trigger_family_count":5,"tested_existing_calibrated_axes":["stage2_actionable_evidence_bonus","stage3_green_revision_min","price_only_blowoff_blocks_positive_stage","full_4b_requires_non_price_evidence","hard_4c_thesis_break_routes_to_4c"],"residual_error_types_found":["green_late_for_auto_margin_confirmation","volume_only_reopening_false_positive","4C_too_late_after_reopening_margin_failure"],"loop_contribution_label":"canonical_archetype_rule_candidate","do_not_propose_new_weight_delta":false}
```

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,c29_margin_conversion_required_for_green,canonical_archetype_specific,L3_BATTERY_EV_GREEN_MOBILITY,C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE,0,1,+1,"Auto/airline volume must convert to durable margin bridge before Green; blocks Jeju-type volume-only false positive while keeping Hyundai/Kia Stage2 Actionable","false_positive_rate reduced; Jeju score falls from Stage3-Yellow/near-Green to Stage2 watch","R9L14_C29_005380_T1_STAGE2_ACTIONABLE_20230126|R9L14_C29_000270_T1_STAGE2_ACTIONABLE_20230126|R9L14_C29_089590_T1_STAGE2_ACTIONABLE_20230118",3,3,1,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,c29_auto_mix_asp_bonus,canonical_archetype_specific,L3_BATTERY_EV_GREEN_MOBILITY,C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE,0,1,+1,"Autos with volume + ASP/mix + margin bridge showed strong MFE/controlled MAE; Stage2 should not wait for full Green confirmation","positive cases average MFE_90D > 25% for Hyundai/Kia while Green lateness exceeded 0.70","R9L14_C29_005380_T1_STAGE2_ACTIONABLE_20230126|R9L14_C29_000270_T1_STAGE2_ACTIONABLE_20230126",2,2,0,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,c29_reopening_volume_without_margin_guard,canonical_archetype_specific,L3_BATTERY_EV_GREEN_MOBILITY,C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE,0,1,+1,"Reopening passenger/load-factor recovery without cost/margin confirmation produced shallow MFE and deep MAE in Jeju Air","counterexample MFE_180D +5.93 vs MAE_180D -42.57","R9L14_C29_089590_T1_STAGE2_ACTIONABLE_20230118",1,1,1,medium,canonical_shadow_only,"not production; post-calibrated residual"
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
completed_round = R9
completed_loop = 14
next_round = R10
next_loop = 14
round_schedule_status = valid
round_sector_consistency = pass
```

## 28. Source Notes

Primary price source:

```text
repo = https://github.com/Songdaiki/stock-web
manifest = atlas/manifest.json
schema = atlas/schema.json
universe = atlas/universe/all_symbols.csv
calibration_shard_root = atlas/ohlcv_tradable_by_symbol_year
raw_shard_root = atlas/ohlcv_raw_by_symbol_year
```

Stock-Web source anchors used in this run:

```text
manifest: max_date 2026-02-20; raw_unadjusted_marcap; calibration shard root atlas/ohlcv_tradable_by_symbol_year
005380 profile: available_years includes 2023; last_date 2026-02-20; corporate action candidates outside 2023 window
000270 profile: available_years includes 2023; last_date 2026-02-20; corporate action candidates outside 2023 window
089590 profile: available_years includes 2023; last_date 2026-02-20; latest corporate action candidate 2022-11-24, outside selected 2023 windows
005380 rows: 2023-01-26 close 174,900; 2023-05-11 high 211,500; 2023-10-31 low 169,300
000270 rows: 2023-01-26 close 69,300; 2023-05-11 high 91,900; 2023-10-31 low 76,900
089590 rows: 2023-01-18 close 16,350; 2023-02-17 high 17,320; 2023-10-20 low 9,390
```

Non-price evidence note:

```text
Non-price evidence is used only to assign trigger families and stress-test the C29 rule.
Production scoring is not changed by this MD.
```
