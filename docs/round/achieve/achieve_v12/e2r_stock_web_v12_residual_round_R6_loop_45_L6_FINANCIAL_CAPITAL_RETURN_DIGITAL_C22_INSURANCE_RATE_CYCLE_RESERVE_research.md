# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
research_session = post_calibrated_sector_archetype_residual_research
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
round = R6
loop = 45
large_sector_id = L6_FINANCIAL_CAPITAL_RETURN_DIGITAL
canonical_archetype_id = C22_INSURANCE_RATE_CYCLE_RESERVE
fine_archetype_id = NONLIFE_IFRS17_CSM_RESERVE_CAPITAL_RETURN | LIFE_RATE_SENSITIVITY_WITHOUT_EXPLICIT_RETURN_COUNTEREXAMPLE
output_file = e2r_stock_web_v12_residual_round_R6_loop_45_L6_FINANCIAL_CAPITAL_RETURN_DIGITAL_C22_INSURANCE_RATE_CYCLE_RESERVE_research.md
production_scoring_changed = false
shadow_weight_only = true
handoff_prompt_embedded = true
handoff_prompt_executed_now = false
```

This file is historical calibration research only. It is not a live candidate scan, investment recommendation, trading instruction, or repository patch.

## 1. Current Calibrated Profile Assumption

```text
current_default_profile_proxy = e2r_2_1_stock_web_calibrated
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

The loop does not re-prove the global rules. It asks a narrower C22 question: in Korean insurers, does IFRS17/CSM/reserve quality plus explicit capital-return optionality deserve a canonical C22 bridge, and where does a life-insurer rate-beta counterexample block that bridge?

## 2. Round / Large Sector / Canonical Archetype Scope

```text
round = R6
large_sector_id = L6_FINANCIAL_CAPITAL_RETURN_DIGITAL
canonical_archetype_id = C22_INSURANCE_RATE_CYCLE_RESERVE
loop_objective = coverage_gap_fill | counterexample_mining | sector_specific_rule_discovery | canonical_archetype_compression | green_strictness_stress_test | 4B_non_price_requirement_stress_test
```

Chosen cases:

| case_id | symbol | company | role | current_profile_verdict | key lesson |
|---|---:|---|---|---|---|
| R6L45_C22_005830_DB_NONLIFE_CAPRETURN | 005830 | DB손해보험 | positive | current_profile_too_late | nonlife reserve quality + capital return can justify C22 Green bridge |
| R6L45_C22_000810_SF_QUALITY_PREMIUM | 000810 | 삼성화재 | positive | current_profile_too_late | quality premium rerated before generic revision-only Green |
| R6L45_C22_088350_HANWHA_LIFE_RATE_COUNTEREXAMPLE | 088350 | 한화생명 | counterexample | current_profile_correct_with_counterexample_guard | rate/value-up beta without explicit capital return should be guarded |

## 3. Previous Coverage / Duplicate Avoidance Check

`stock_agent` artifact search for `C22_INSURANCE_RATE_CYCLE_RESERVE` returned no matched prior calibration file in this session. The prior registry excerpts inspected were concentrated in R12/R13 and R1 loops, while a direct C22 lookup was empty. Therefore this loop is treated as an auto-selected L6/C22 coverage gap fill rather than a duplicate of the prior R6/C21 financial capital-return file.

```text
auto_selected_coverage_gap = L6/C22 insurance rate-cycle reserve undercovered
new_independent_case_count = 3
reused_case_count = 0
new_symbol_count = 3
same_archetype_new_symbol_count = 3
same_archetype_new_trigger_family_count = 4
new_canonical_archetype_count = 1
```

Diversity score summary:

```text
same_archetype_new_symbol_bonus = +12
counterexample_gap_bonus = +4
undercovered_sector_bonus = +3
new_trigger_family_bonus = +12
residual_error_bonus = +5
repeated_symbol_penalty = 0
schema_rematerialization_penalty = 0

diversity_score_summary = high / usable / not schema rematerialization
```

## 4. Stock-Web OHLC Input / Price Source Validation

The stock-web manifest used in this loop:

```json
{
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

Validation notes:

```text
source_name = FinanceData/marcap
price_basis = tradable_raw
price_adjustment_status = raw_unadjusted_marcap
manifest_max_date = 2026-02-20
calibration_shard_root = atlas/ohlcv_tradable_by_symbol_year
raw_shard_root = atlas/ohlcv_raw_by_symbol_year
```

Stock-web states that raw/unadjusted OHLC is used, zero-volume / invalid rows are excluded from calibration shards, and corporate-action contaminated windows are blocked by default. This loop applies the 180D corporate-action window gate and uses only tradable shards for MFE/MAE.

## 5. Historical Eligibility Gate

All representative trigger rows satisfy:

```text
trigger_date is historical = true
entry_date exists in tradable shard = true
forward_180D window available by stock-web manifest max_date = true
required OHLCV fields present = true
corporate-action contaminated 180D window = false
```

| symbol | company | representative entry | forward 180D usable | corporate-action window status |
|---:|---|---:|---|---|
| 005830 | DB손해보험 | 2024-02-23 | true | clean_180D_window_old_1999_candidate_outside_window |
| 000810 | 삼성화재 | 2024-02-23 | true | clean_180D_window_old_1999_2000_candidates_outside_window |
| 088350 | 한화생명 | 2024-02-23 | true | clean_180D_window |

## 6. Canonical Archetype Compression Map

```text
canonical_archetype_id = C22_INSURANCE_RATE_CYCLE_RESERVE

positive fine archetypes:
- NONLIFE_IFRS17_CSM_RESERVE_CAPITAL_RETURN
- NONLIFE_QUALITY_PREMIUM_RESERVE_CAPITAL_RETURN

counterexample fine archetype:
- LIFE_RATE_SENSITIVITY_WITHOUT_EXPLICIT_RETURN_COUNTEREXAMPLE
```

C22 should not mean “all insurance stocks during value-up.” It should mean a reserve/rate-cycle structure where capital return is actually distributable or visible. The counterexample keeps the archetype from swallowing generic rate beta.

## 7. Case Selection Summary

| case_id | symbol | company | role | current_profile_verdict | key lesson |
|---|---:|---|---|---|---|
| R6L45_C22_005830_DB_NONLIFE_CAPRETURN | 005830 | DB손해보험 | positive | current_profile_too_late | nonlife reserve quality + capital return can justify C22 Green bridge |
| R6L45_C22_000810_SF_QUALITY_PREMIUM | 000810 | 삼성화재 | positive | current_profile_too_late | quality premium rerated before generic revision-only Green |
| R6L45_C22_088350_HANWHA_LIFE_RATE_COUNTEREXAMPLE | 088350 | 한화생명 | counterexample | current_profile_correct_with_counterexample_guard | rate/value-up beta without explicit capital return should be guarded |

Case selection logic:

```text
positive_structural_success = 2
counterexample_or_failed_rerating = 1
4B_or_4C_case = 1
calibration_usable_case_count = 3
```

## 8. Positive vs Counterexample Balance

The two nonlife positives show strong 90D/180D MFE but also meaningful drawdowns. The life-insurer counterexample shows weak upside and deeper downside. That shape is useful because it prevents the new shadow rule from becoming a naive insurance-sector beta rule.

| bucket | cases | alignment |
|---|---|---|
| Positive structural success | DB손해보험, 삼성화재 | MFE90 23.42% / 27.55%, but with early MAE around -11% |
| Counterexample | 한화생명 | MFE90 3.84%, MAE90 -23.78% |
| 4B overlay | 한화생명 2024-02-08 | price-only local risk warning worked, but no full non-price 4B thesis break |

## 9. Evidence Source Map

Evidence is separated by stage and intentionally avoids outcome-labeling. Price action itself is not used as Stage2/3 evidence.

| case | Stage2 evidence | Stage3 evidence | 4B evidence | 4C evidence |
|---|---|---|---|---|
| DB손해보험 | FY2023/IFRS17 result season, nonlife reserve quality, value-up/capital-return optionality | financial visibility, margin/CSM bridge, lower red-team risk | none at entry | none |
| 삼성화재 | quality nonlife franchise, reserve/capital-return optionality, relative strength | confirmed financial visibility and quality premium | none at entry | none |
| 한화생명 | insurance/value-up and rate-sensitivity narrative | not enough explicit capital-return proof | price-only local peak / positioning overheat | thesis-break watch only |

## 10. Price Data Source Map

| symbol | price shard | profile | profile window status |
|---:|---|---|---|
| 005830 | atlas/ohlcv_tradable_by_symbol_year/005/005830/2024.csv | atlas/symbol_profiles/005/005830.json | old 1999 corporate-action candidate only; 2024 180D clean |
| 000810 | atlas/ohlcv_tradable_by_symbol_year/000/000810/2024.csv | atlas/symbol_profiles/000/000810.json | old 1999/2000 corporate-action candidates only; 2024 180D clean |
| 088350 | atlas/ohlcv_tradable_by_symbol_year/088/088350/2024.csv | atlas/symbol_profiles/088/088350.json | no corporate-action candidate; 2024 180D clean |

## 11. Case-by-Case Trigger Grid

| trigger_id | symbol | type | entry | price | MFE30 | MAE30 | MFE90 | MAE90 | MFE180 | MAE180 | verdict | aggregate |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| R6L45_C22_005830_T1_STAGE2_ACTIONABLE_2024-02-23 | 005830 | Stage2-Actionable | 2024-02-23 | 97800 | 12.47 | -6.85 | 23.42 | -11.55 | 26.79 | -11.55 | current_profile_too_late | representative |
| R6L45_C22_005830_T2_STAGE3_GREEN_COMPARISON_2024-05-16 | 005830 | Stage3-Green | 2024-05-16 | 111500 | 3.5 | -11.84 | 11.21 | -15.61 | 11.21 | -15.61 | current_profile_too_late | label_comparison_only |
| R6L45_C22_000810_T1_STAGE2_ACTIONABLE_2024-02-23 | 000810 | Stage2-Actionable | 2024-02-23 | 308500 | 12.16 | -7.46 | 27.55 | -11.67 | 27.55 | -11.67 | current_profile_too_late | representative |
| R6L45_C22_000810_T2_STAGE3_GREEN_COMPARISON_2024-05-16 | 000810 | Stage3-Green | 2024-05-16 | 370000 | 6.35 | -12.43 | 6.35 | -12.43 | 6.35 | -12.43 | current_profile_too_late | label_comparison_only |
| R6L45_C22_088350_T1_STAGE2_ACTIONABLE_2024-02-23 | 088350 | Stage2-Actionable | 2024-02-23 | 3385 | 3.84 | -17.13 | 3.84 | -23.78 | 3.84 | -23.78 | current_profile_correct_with_counterexample_guard | representative |
| R6L45_C22_088350_T2_4B_PRICE_ONLY_2024-02-08 | 088350 | 4B | 2024-02-08 | 3645 | 4.66 | -17.97 | 4.66 | -29.22 | 4.66 | -29.22 | current_profile_correct | 4B_overlay_only |

## 12. Trigger-Level OHLC Backtest Tables

### Representative trigger backtest

| case | entry | entry_price | max high used | min low used | MFE30 | MAE30 | MFE90 | MAE90 | MFE180 | MAE180 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| DB손해보험 | 2024-02-23 | 97,800 | 124,000 | 86,500 | 12.47 | -6.85 | 23.42 | -11.55 | 26.79 | -11.55 |
| 삼성화재 | 2024-02-23 | 308,500 | 393,500 | 272,500 | 12.16 | -7.46 | 27.55 | -11.67 | 27.55 | -11.67 |
| 한화생명 | 2024-02-23 | 3,385 | 3,515 | 2,580 | 3.84 | -17.13 | 3.84 | -23.78 | 3.84 | -23.78 |

### Data row anchors

```text
DB손해보험:
- entry row = 2024-02-23, c=97800
- 30D high row = 2024-03-14, h=110000
- 90D high row = 2024-07-02, h=120700
- 180D high row = 2024-08-22, h=124000
- adverse low = 2024-04-12, l=86500

삼성화재:
- entry row = 2024-02-23, c=308500
- 30D high row = 2024-03-22, h=346000
- 90D/180D high row = 2024-06-28, h=393500
- adverse low = 2024-04-19, l=272500

한화생명:
- entry row = 2024-02-23, c=3385
- high row = 2024-02-23, h=3515
- adverse low = 2024-04-16, l=2580
```

## 13. Current Calibrated Profile Stress Test

| case | P0 likely decision | observed result | verdict |
|---|---|---|---|
| DB손해보험 | Stage3-Yellow first, Green later after revision/visibility | Positive MFE but early MAE; Green comparison captures much less upside | current_profile_too_late |
| 삼성화재 | Stage3-Yellow first, Green later due strict revision/threshold | Positive MFE; later Green enters after a large part of upside | current_profile_too_late |
| 한화생명 | Current price-only blowoff guard helps, but generic insurance beta can still tempt Stage2 scoring | Counterexample: poor upside and deep downside | current_profile_correct_with_counterexample_guard |

Stress-test answers:

```text
1. current calibrated profile likely judges nonlife cases conservatively as Yellow before Green.
2. That judgment is directionally safe but too late for C22 nonlife capital-return rerating.
3. Stage2 bonus is not too high for DB/Samsung Fire; it is too high for Hanwha if rate/value-up beta is overread as capital return.
4. Yellow threshold 75 is acceptable.
5. Green threshold 87 / revision 55 is too strict for C22 when explicit capital-return and reserve-quality evidence are both present.
6. price-only blowoff guard is appropriate and is strengthened by Hanwha.
7. full 4B non-price requirement is appropriate; Hanwha 2024-02-08 is risk overlay, not full 4B.
8. hard 4C routing is not materially tested; Hanwha remained thesis-break watch rather than hard 4C.
```

## 14. Stage2 / Yellow / Green Comparison

| case | Stage2 entry | Stage3-Green comparison | peak after Stage2 | green_lateness_ratio | interpretation |
|---|---:|---:|---:|---:|---|
| DB손해보험 | 97,800 | 111,500 | 124,000 | 0.52 | Green captured only the back half of upside |
| 삼성화재 | 308,500 | 370,000 | 393,500 | 0.72 | Green was materially late |
| 한화생명 | 3,385 | no confirmed Green | 3,515 | not_applicable | no Green trigger; counterexample blocks promotion |

C22-specific implication: the issue is not “Stage2 is always better.” The issue is that nonlife reserve/capital-return evidence can close the Stage3 quality gap before slow generic revision evidence arrives.

## 15. 4B Local vs Full-window Timing Audit

| trigger | entry_price | local peak | full-window peak | local proximity | full proximity | verdict |
|---|---:|---:|---:|---:|---:|---|
| 한화생명 2024-02-08 4B overlay | 3,645 | 3,815 | 3,815 | 0.89 | 0.89 | good local risk warning, but price-only means overlay-only |
| DB손해보험 2024-08-22 peak | 124,000 | 124,000 | 124,000 | not formal 4B | not formal 4B | no full 4B without non-price evidence |
| 삼성화재 2024-06-28 peak | 393,500 | 393,500 | 393,500 | not formal 4B | not formal 4B | no full 4B without non-price evidence |

The Hanwha row strengthens the existing full_4b_requires_non_price_evidence axis. It is a usable 4B risk overlay, not a production sell signal or thesis break.

## 16. 4C Protection Audit

No hard 4C route is proposed. Hanwha is labelled `thesis_break_watch_only` / `hard_4c_late` because the price path deteriorated, but this loop did not verify contract-cancel, reserve-accounting break, forced liquidation, or regulatory rejection evidence.

## 17. Sector-Specific Rule Candidate

```text
rule_scope = sector_specific
axis = L6_C22_nonlife_reserve_quality_capital_return_bridge
proposal_type = sector_shadow_only
production_scoring_changed = false
```

Candidate rule:

```text
if large_sector_id == L6_FINANCIAL_CAPITAL_RETURN_DIGITAL
and canonical_archetype_id == C22_INSURANCE_RATE_CYCLE_RESERVE
and insurer_subtype == nonlife
and reserve_quality_or_CSM_visibility == supported
and explicit_or_highly_visible_capital_return == supported
and accounting_trust_risk_score >= 0
then allow a +2~+3 shadow bridge from high Yellow to Green
without lowering global Green thresholds.
```

Guard:

```text
if insurer_subtype == life
and evidence is mostly rate sensitivity / value-up beta / price momentum
and explicit capital return is not supported
then apply -3~-4 C22 guard and block Green promotion.
```

## 18. Canonical-Archetype Rule Candidate

```text
canonical_archetype_id = C22_INSURANCE_RATE_CYCLE_RESERVE
preferred_rule_scope = canonical_archetype_specific
canonical_rule_candidate = true
```

Canonical compression:

```text
C22 positive evidence = reserve quality + CSM/contractual service visibility + capital return distributability
C22 counterexample evidence = rate sensitivity + price momentum without explicit return
C22 4B evidence = price-only local blowoff is overlay-only unless non-price deterioration appears
```

## 19. Before / After Backtest Comparison

| profile_id | scope | selected reps | avg MFE90 | avg MAE90 | avg MFE180 | avg MAE180 | false positive | late green | verdict |
|---|---|---:|---:|---:|---:|---:|---:|---:|---|
| P0 e2r_2_1_stock_web_calibrated_proxy | current proxy | 3 | 18.27 | -15.67 | 19.39 | -15.67 | 1 | 2 | current rules avoid pure price blowoff but C22 nonlife Green is late |
| P0b e2r_2_0_baseline_reference | rollback | 3 | 18.27 | -15.67 | 19.39 | -15.67 | 1 | 0 | too permissive for Hanwha-like rate beta |
| P1 sector_specific_candidate_profile | L6 | 2 | 25.49 | -11.61 | 27.17 | -11.61 | 0 | 1 | better after excluding life-rate-only beta |
| P2 canonical_archetype_candidate_profile | C22 | 2 | 25.49 | -11.61 | 27.17 | -11.61 | 0 | 0 | best alignment: nonlife bridge + life-rate guard |
| P3 counterexample_guard_profile | C22 guard | 2 | 25.49 | -11.61 | 27.17 | -11.61 | 0 | 1 | strongest downside protection but may under-promote DB/Samsung Fire |

## 20. Score-Return Alignment Matrix

| case | P0 score label | proposed label | MFE90 | MAE90 | alignment |
|---|---|---|---:|---:|---|
| DB손해보험 | Stage3-Yellow | Stage3-Green via C22 bridge | 23.42 | -11.55 | improved |
| 삼성화재 | Stage3-Yellow | Stage3-Green via C22 bridge | 27.55 | -11.67 | improved |
| 한화생명 | Stage2/Yellow risk | Watch / NoGreen via C22 guard | 3.84 | -23.78 | improved false-positive control |

## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive_case_count | counterexample_count | 4B_case_count | 4C_case_count | new_independent_case_count | reused_case_count | calibration_usable_trigger_count | representative_trigger_count | current_profile_error_count | sector_rule_candidate | canonical_rule_candidate | coverage_gap_after_this_loop |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| L6_FINANCIAL_CAPITAL_RETURN_DIGITAL | C22_INSURANCE_RATE_CYCLE_RESERVE | NONLIFE_IFRS17_CSM_RESERVE_CAPITAL_RETURN / LIFE_RATE_SENSITIVITY_WITHOUT_EXPLICIT_RETURN_COUNTEREXAMPLE | 2 | 1 | 1 | 0 | 3 | 0 | 6 | 3 | 2 | true | true | C22 now has positive/counterexample balance; needs another insurance reserve holdout loop for C22 robustness |

## 22. Residual Contribution Summary

```text
new_independent_case_count: 3
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 3
same_archetype_new_symbol_count: 3
same_archetype_new_trigger_family_count: 4
new_canonical_archetype_count: 1
new_fine_archetype_count: 3
new_trigger_family_count: 4
tested_existing_calibrated_axes:
  - stage3_green_total_min
  - stage3_green_revision_min
  - price_only_blowoff_blocks_positive_stage
  - full_4b_requires_non_price_evidence
residual_error_types_found:
  - C22_nonlife_Green_too_late
  - life_insurer_rate_beta_false_positive_risk
new_axis_proposed:
  - c22_nonlife_reserve_quality_capital_return_bridge
  - c22_life_rate_sensitivity_without_explicit_return_guard
existing_axis_strengthened:
  - price_only_blowoff_blocks_positive_stage
  - full_4b_requires_non_price_evidence
existing_axis_weakened: null
existing_axis_kept:
  - stage2_actionable_evidence_bonus
  - stage3_yellow_total_min
sector_specific_rule_candidate: true
canonical_archetype_rule_candidate: true
no_new_signal_reason: null
loop_contribution_label: canonical_archetype_rule_candidate
do_not_propose_new_weight_delta: false
auto_selected_coverage_gap: L6/C22 undercovered
```

## 23. Validation Scope / Non-Validation Scope

Validated:

```text
- stock-web manifest max_date and price basis
- profile-level corporate-action window status
- tradable OHLC rows for 2024 representative windows
- 30D / 90D / 180D MFE and MAE for representative triggers
- positive/counterexample balance
- same_entry_group_id dedupe logic
- 4B local vs full-window split for Hanwha Life risk overlay
```

Not validated:

```text
- current live candidate quality
- post-2026-02-20 prices
- production scoring implementation
- stock_agent src/e2r code
- brokerage execution
- exact consensus EPS revision database values
```

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,c22_nonlife_reserve_quality_capital_return_bridge,canonical_archetype_specific,L6_FINANCIAL_CAPITAL_RETURN_DIGITAL,C22_INSURANCE_RATE_CYCLE_RESERVE,0,+3,+3,"Nonlife reserve-quality/CSM visibility plus shareholder-return optionality shortened Green delay in DB손보/삼성화재","avg MFE90 of promoted positives 25.49 vs counterexample 3.84","R6L45_C22_005830_T1_STAGE2_ACTIONABLE_2024-02-23|R6L45_C22_000810_T1_STAGE2_ACTIONABLE_2024-02-23",3,3,1,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,c22_life_rate_sensitivity_without_explicit_return_guard,canonical_archetype_specific,L6_FINANCIAL_CAPITAL_RETURN_DIGITAL,C22_INSURANCE_RATE_CYCLE_RESERVE,0,-4,-4,"Life insurer rate/value-up beta without explicit capital return caused poor MFE/MAE in Hanwha Life","counterexample MFE90 3.84 and MAE90 -23.78","R6L45_C22_088350_T1_STAGE2_ACTIONABLE_2024-02-23",3,3,1,medium,counterexample_guard_only,"not production; blocks generic insurance promotion"
shadow_weight,price_only_local_4b_stays_overlay_only,existing_axis_strengthened,L6_FINANCIAL_CAPITAL_RETURN_DIGITAL,C22_INSURANCE_RATE_CYCLE_RESERVE,true,true,0,"Hanwha Life 2024-02-08 was useful risk warning but lacked non-price evidence for full 4B","4B overlay protected risk but should not be a production thesis-break","R6L45_C22_088350_T2_4B_PRICE_ONLY_2024-02-08",1,1,1,medium,axis_stress_test,"strengthens existing full_4b_requires_non_price_evidence"
```

## 25. Machine-Readable Rows

### 25.1 price_source_validation

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
```

### 25.2 case rows

```jsonl
{"row_type":"case","case_id":"R6L45_C22_005830_DB_NONLIFE_CAPRETURN","symbol":"005830","company_name":"DB손해보험","round":"R6","loop":"45","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","fine_archetype_id":"NONLIFE_IFRS17_CSM_RESERVE_CAPITAL_RETURN","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"R6L45_C22_005830_T1_STAGE2_ACTIONABLE_2024-02-23","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"positive but high early MAE; capital-return clarity explains why a later Green-only gate is too slow","current_profile_verdict":"current_profile_too_late","price_source":"Songdaiki/stock-web","notes":"Clean modern 180D window; old corporate-action candidate only in 1999. C22-specific lesson: nonlife CSM/reserve quality plus explicit shareholder return should bridge Yellow->Green earlier than generic revision-only Green."}
{"row_type":"case","case_id":"R6L45_C22_000810_SF_QUALITY_PREMIUM","symbol":"000810","company_name":"삼성화재","round":"R6","loop":"45","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","fine_archetype_id":"NONLIFE_QUALITY_PREMIUM_RESERVE_CAPITAL_RETURN","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"R6L45_C22_000810_T1_STAGE2_ACTIONABLE_2024-02-23","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"large MFE with a meaningful spring drawdown; high-quality nonlife franchise rerated before slow Green confirmation","current_profile_verdict":"current_profile_too_late","price_source":"Songdaiki/stock-web","notes":"Old corporate-action candidates are outside the 2024 validation window. The lesson is not generic Green lateness; it is the C22-specific combination of reserve quality, K-ICS room, and shareholder-return optionality."}
{"row_type":"case","case_id":"R6L45_C22_088350_HANWHA_LIFE_RATE_COUNTEREXAMPLE","symbol":"088350","company_name":"한화생명","round":"R6","loop":"45","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","fine_archetype_id":"LIFE_RATE_SENSITIVITY_WITHOUT_EXPLICIT_RETURN_COUNTEREXAMPLE","case_type":"failed_rerating","positive_or_counterexample":"counterexample","best_trigger":"R6L45_C22_088350_T1_STAGE2_ACTIONABLE_2024-02-23","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"poor MFE and deep MAE; rate/IFRS17 narrative without explicit capital return should not receive the same C22 promotion as nonlife quality cases","current_profile_verdict":"current_profile_correct_with_counterexample_guard","price_source":"Songdaiki/stock-web","notes":"Clean 180D window. This is the paired counterexample that prevents C22 from becoming a generic insurance/value-up promotion rule."}
```

### 25.3 trigger rows

```jsonl
{"row_type":"trigger","trigger_id":"R6L45_C22_005830_T1_STAGE2_ACTIONABLE_2024-02-23","case_id":"R6L45_C22_005830_DB_NONLIFE_CAPRETURN","symbol":"005830","company_name":"DB손해보험","round":"R6","loop":"45","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","fine_archetype_id":"NONLIFE_IFRS17_CSM_RESERVE_CAPITAL_RETURN","sector":"금융·자본배분·디지털금융","primary_archetype":"보험 IFRS17/CSM/준비금 + 자본환원","loop_objective":"coverage_gap_fill|sector_specific_rule_discovery|counterexample_mining","trigger_type":"Stage2-Actionable","trigger_date":"2024-02-23","evidence_available_at_that_date":"FY2023/IFRS17 result season, nonlife reserve-quality discussion, value-up/capital-return expectation; public evidence was observable by close.","evidence_source":"public result/IR/disclosure season; stock-web OHLC validation in this loop","stage2_evidence_fields":["public_event_or_disclosure","early_revision_signal","policy_or_regulatory_optionality","relative_strength"],"stage3_evidence_fields":["financial_visibility","margin_bridge","low_red_team_risk"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/005/005830/2024.csv","profile_path":"atlas/symbol_profiles/005/005830.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-02-23","entry_price":97800,"MFE_30D_pct":12.47,"MFE_90D_pct":23.42,"MFE_180D_pct":26.79,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-6.85,"MAE_90D_pct":-11.55,"MAE_180D_pct":-11.55,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-08-22","peak_price":124000,"drawdown_after_peak_pct":-14.44,"green_lateness_ratio":0.52,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":null,"four_b_evidence_type":[],"four_c_protection_label":"not_applicable","trigger_outcome_label":"positive_structural_success_with_high_initial_MAE","current_profile_verdict":"current_profile_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window_old_1999_candidate_outside_window","same_entry_group_id":"005830_2024-02-23_97800","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"R6L45_C22_005830_T2_STAGE3_GREEN_COMPARISON_2024-05-16","case_id":"R6L45_C22_005830_DB_NONLIFE_CAPRETURN","symbol":"005830","company_name":"DB손해보험","round":"R6","loop":"45","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","fine_archetype_id":"NONLIFE_IFRS17_CSM_RESERVE_CAPITAL_RETURN","sector":"금융·자본배분·디지털금융","primary_archetype":"보험 IFRS17/CSM/준비금 + 자본환원","loop_objective":"green_strictness_stress_test|canonical_archetype_compression","trigger_type":"Stage3-Green","trigger_date":"2024-05-16","evidence_available_at_that_date":"Later confirmation route after spring repricing and stronger nonlife result visibility.","evidence_source":"public result/IR/disclosure season; stock-web OHLC validation in this loop","stage2_evidence_fields":["public_event_or_disclosure","relative_strength"],"stage3_evidence_fields":["confirmed_revision","financial_visibility","margin_bridge"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/005/005830/2024.csv","profile_path":"atlas/symbol_profiles/005/005830.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-05-16","entry_price":111500,"MFE_30D_pct":3.5,"MFE_90D_pct":11.21,"MFE_180D_pct":11.21,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-11.84,"MAE_90D_pct":-15.61,"MAE_180D_pct":-15.61,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-08-22","peak_price":124000,"drawdown_after_peak_pct":-14.44,"green_lateness_ratio":0.52,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":null,"four_b_evidence_type":[],"four_c_protection_label":"not_applicable","trigger_outcome_label":"late_green_comparison","current_profile_verdict":"current_profile_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window_old_1999_candidate_outside_window","same_entry_group_id":"005830_2024-05-16_111500","dedupe_for_aggregate":false,"aggregate_group_role":"label_comparison_only","is_new_independent_case":false,"reuse_reason":"same_case_label_comparison_for_green_lateness","independent_evidence_weight":0.25,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"R6L45_C22_000810_T1_STAGE2_ACTIONABLE_2024-02-23","case_id":"R6L45_C22_000810_SF_QUALITY_PREMIUM","symbol":"000810","company_name":"삼성화재","round":"R6","loop":"45","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","fine_archetype_id":"NONLIFE_QUALITY_PREMIUM_RESERVE_CAPITAL_RETURN","sector":"금융·자본배분·디지털금융","primary_archetype":"보험 IFRS17/CSM/준비금 + 자본환원","loop_objective":"coverage_gap_fill|sector_specific_rule_discovery|green_strictness_stress_test","trigger_type":"Stage2-Actionable","trigger_date":"2024-02-23","evidence_available_at_that_date":"Nonlife quality premium and shareholder-return optionality were observable during FY2023 result/value-up rerating window.","evidence_source":"public result/IR/disclosure season; stock-web OHLC validation in this loop","stage2_evidence_fields":["public_event_or_disclosure","customer_or_order_quality","relative_strength","policy_or_regulatory_optionality"],"stage3_evidence_fields":["financial_visibility","margin_bridge","low_red_team_risk"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/000/000810/2024.csv","profile_path":"atlas/symbol_profiles/000/000810.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-02-23","entry_price":308500,"MFE_30D_pct":12.16,"MFE_90D_pct":27.55,"MFE_180D_pct":27.55,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-7.46,"MAE_90D_pct":-11.67,"MAE_180D_pct":-11.67,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-06-28","peak_price":393500,"drawdown_after_peak_pct":-17.66,"green_lateness_ratio":0.72,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":null,"four_b_evidence_type":[],"four_c_protection_label":"not_applicable","trigger_outcome_label":"positive_structural_success_quality_premium","current_profile_verdict":"current_profile_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window_old_1999_2000_candidates_outside_window","same_entry_group_id":"000810_2024-02-23_308500","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"R6L45_C22_000810_T2_STAGE3_GREEN_COMPARISON_2024-05-16","case_id":"R6L45_C22_000810_SF_QUALITY_PREMIUM","symbol":"000810","company_name":"삼성화재","round":"R6","loop":"45","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","fine_archetype_id":"NONLIFE_QUALITY_PREMIUM_RESERVE_CAPITAL_RETURN","sector":"금융·자본배분·디지털금융","primary_archetype":"보험 IFRS17/CSM/준비금 + 자본환원","loop_objective":"green_strictness_stress_test","trigger_type":"Stage3-Green","trigger_date":"2024-05-16","evidence_available_at_that_date":"Later confirmation route after visible nonlife premium expansion.","evidence_source":"public result/IR/disclosure season; stock-web OHLC validation in this loop","stage2_evidence_fields":["public_event_or_disclosure","relative_strength"],"stage3_evidence_fields":["confirmed_revision","financial_visibility","margin_bridge","low_red_team_risk"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/000/000810/2024.csv","profile_path":"atlas/symbol_profiles/000/000810.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-05-16","entry_price":370000,"MFE_30D_pct":6.35,"MFE_90D_pct":6.35,"MFE_180D_pct":6.35,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-12.43,"MAE_90D_pct":-12.43,"MAE_180D_pct":-12.43,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-06-28","peak_price":393500,"drawdown_after_peak_pct":-17.66,"green_lateness_ratio":0.72,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":null,"four_b_evidence_type":[],"four_c_protection_label":"not_applicable","trigger_outcome_label":"late_green_comparison","current_profile_verdict":"current_profile_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window_old_1999_2000_candidates_outside_window","same_entry_group_id":"000810_2024-05-16_370000","dedupe_for_aggregate":false,"aggregate_group_role":"label_comparison_only","is_new_independent_case":false,"reuse_reason":"same_case_label_comparison_for_green_lateness","independent_evidence_weight":0.25,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"R6L45_C22_088350_T1_STAGE2_ACTIONABLE_2024-02-23","case_id":"R6L45_C22_088350_HANWHA_LIFE_RATE_COUNTEREXAMPLE","symbol":"088350","company_name":"한화생명","round":"R6","loop":"45","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","fine_archetype_id":"LIFE_RATE_SENSITIVITY_WITHOUT_EXPLICIT_RETURN_COUNTEREXAMPLE","sector":"금융·자본배분·디지털금융","primary_archetype":"보험 금리민감/IFRS17 착시","loop_objective":"counterexample_mining|residual_false_positive_mining|4B_non_price_requirement_stress_test","trigger_type":"Stage2-Actionable","trigger_date":"2024-02-23","evidence_available_at_that_date":"Insurance/value-up and life-insurer rate-sensitivity narrative was observable, but explicit capital return and reserve-quality proof were weaker than nonlife peers.","evidence_source":"public result/IR/disclosure season; stock-web OHLC validation in this loop","stage2_evidence_fields":["public_event_or_disclosure","policy_or_regulatory_optionality","relative_strength"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["price_only_local_peak","positioning_overheat"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/088/088350/2024.csv","profile_path":"atlas/symbol_profiles/088/088350.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-02-23","entry_price":3385,"MFE_30D_pct":3.84,"MFE_90D_pct":3.84,"MFE_180D_pct":3.84,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-17.13,"MAE_90D_pct":-23.78,"MAE_180D_pct":-23.78,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-02-23","peak_price":3515,"drawdown_after_peak_pct":-26.6,"green_lateness_ratio":"not_applicable:no_confirmed_Stage3_Green_trigger","four_b_local_peak_proximity":0.82,"four_b_full_window_peak_proximity":0.82,"four_b_timing_verdict":"price_only_local_4B_watch_but_not_full_4B","four_b_evidence_type":["price_only","positioning_overheat"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"failed_rerating_counterexample","current_profile_verdict":"current_profile_correct_with_counterexample_guard","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"088350_2024-02-23_3385","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"R6L45_C22_088350_T2_4B_PRICE_ONLY_2024-02-08","case_id":"R6L45_C22_088350_HANWHA_LIFE_RATE_COUNTEREXAMPLE","symbol":"088350","company_name":"한화생명","round":"R6","loop":"45","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","fine_archetype_id":"LIFE_RATE_SENSITIVITY_WITHOUT_EXPLICIT_RETURN_COUNTEREXAMPLE","sector":"금융·자본배분·디지털금융","primary_archetype":"보험 금리민감/IFRS17 착시","loop_objective":"4B_non_price_requirement_stress_test|counterexample_mining","trigger_type":"4B","trigger_date":"2024-02-08","evidence_available_at_that_date":"Local blow-off/positioning overheat after rapid insurance/value-up rerating; no explicit hard thesis break yet.","evidence_source":"stock-web OHLC validation in this loop","stage2_evidence_fields":["relative_strength"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["price_only_local_peak","positioning_overheat"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/088/088350/2024.csv","profile_path":"atlas/symbol_profiles/088/088350.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-02-08","entry_price":3645,"MFE_30D_pct":4.66,"MFE_90D_pct":4.66,"MFE_180D_pct":4.66,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-17.97,"MAE_90D_pct":-29.22,"MAE_180D_pct":-29.22,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-02-13","peak_price":3815,"drawdown_after_peak_pct":-32.37,"green_lateness_ratio":"not_applicable:4B_overlay","four_b_local_peak_proximity":0.89,"four_b_full_window_peak_proximity":0.89,"four_b_timing_verdict":"good_local_risk_warning_but_price_only_not_full_4B","four_b_evidence_type":["price_only","positioning_overheat"],"four_c_protection_label":"hard_4c_late","trigger_outcome_label":"4B_overlay_success_for_risk_only","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"088350_2024-02-08_3645","dedupe_for_aggregate":false,"aggregate_group_role":"4B_overlay_only","is_new_independent_case":false,"reuse_reason":"same_case_4B_timing_overlay","independent_evidence_weight":0.5,"do_not_count_as_new_case":false}
```

### 25.4 score_simulation rows

```jsonl
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R6L45_C22_005830_DB_NONLIFE_CAPRETURN","trigger_id":"R6L45_C22_005830_T1_STAGE2_ACTIONABLE_2024-02-23","symbol":"005830","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","raw_component_scores_before":{"contract_score":"unknown_or_not_supported","backlog_visibility_score":"unknown_or_not_supported","margin_bridge_score":16,"revision_score":15,"relative_strength_score":15,"customer_quality_score":"unknown_or_not_supported","policy_or_regulatory_score":10,"valuation_repricing_score":12,"execution_risk_score":-4,"legal_or_contract_risk_score":"unknown_or_not_supported","dilution_cb_risk_score":"unknown_or_not_supported","accounting_trust_risk_score":0},"weighted_score_before":82,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":"unknown_or_not_supported","backlog_visibility_score":"unknown_or_not_supported","margin_bridge_score":17,"revision_score":16,"relative_strength_score":15,"customer_quality_score":6,"policy_or_regulatory_score":12,"valuation_repricing_score":13,"execution_risk_score":-4,"legal_or_contract_risk_score":"unknown_or_not_supported","dilution_cb_risk_score":"unknown_or_not_supported","accounting_trust_risk_score":0},"weighted_score_after":88,"stage_label_after":"Stage3-Green","changed_components":["c22_nonlife_reserve_quality_bonus","+c22_explicit_capital_return_bridge"],"component_delta_explanation":"C22 nonlife cases deserve a narrow Yellow->Green bridge when reserve quality/CSM visibility and shareholder-return optionality are both present; this is not a generic insurance boost.","MFE_90D_pct":23.42,"MAE_90D_pct":-11.55,"score_return_alignment_label":"improved_alignment","current_profile_verdict":"current_profile_too_late"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R6L45_C22_000810_SF_QUALITY_PREMIUM","trigger_id":"R6L45_C22_000810_T1_STAGE2_ACTIONABLE_2024-02-23","symbol":"000810","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","raw_component_scores_before":{"contract_score":"unknown_or_not_supported","backlog_visibility_score":"unknown_or_not_supported","margin_bridge_score":17,"revision_score":14,"relative_strength_score":16,"customer_quality_score":7,"policy_or_regulatory_score":10,"valuation_repricing_score":12,"execution_risk_score":-3,"legal_or_contract_risk_score":"unknown_or_not_supported","dilution_cb_risk_score":"unknown_or_not_supported","accounting_trust_risk_score":0},"weighted_score_before":84,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":"unknown_or_not_supported","backlog_visibility_score":"unknown_or_not_supported","margin_bridge_score":18,"revision_score":15,"relative_strength_score":16,"customer_quality_score":8,"policy_or_regulatory_score":12,"valuation_repricing_score":14,"execution_risk_score":-3,"legal_or_contract_risk_score":"unknown_or_not_supported","dilution_cb_risk_score":"unknown_or_not_supported","accounting_trust_risk_score":0},"weighted_score_after":90,"stage_label_after":"Stage3-Green","changed_components":["c22_nonlife_quality_premium_bonus","+c22_capital_return_visibility_bridge"],"component_delta_explanation":"High-quality nonlife reserve/capital-return combination should compress the Green wait once the case is no longer just price momentum.","MFE_90D_pct":27.55,"MAE_90D_pct":-11.67,"score_return_alignment_label":"improved_alignment","current_profile_verdict":"current_profile_too_late"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R6L45_C22_088350_HANWHA_LIFE_RATE_COUNTEREXAMPLE","trigger_id":"R6L45_C22_088350_T1_STAGE2_ACTIONABLE_2024-02-23","symbol":"088350","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","raw_component_scores_before":{"contract_score":"unknown_or_not_supported","backlog_visibility_score":"unknown_or_not_supported","margin_bridge_score":4,"revision_score":6,"relative_strength_score":14,"customer_quality_score":"unknown_or_not_supported","policy_or_regulatory_score":12,"valuation_repricing_score":13,"execution_risk_score":-9,"legal_or_contract_risk_score":"unknown_or_not_supported","dilution_cb_risk_score":"unknown_or_not_supported","accounting_trust_risk_score":-2},"weighted_score_before":76,"stage_label_before":"Stage3-Yellow_or_Stage2-Actionable","raw_component_scores_after":{"contract_score":"unknown_or_not_supported","backlog_visibility_score":"unknown_or_not_supported","margin_bridge_score":3,"revision_score":4,"relative_strength_score":8,"customer_quality_score":"unknown_or_not_supported","policy_or_regulatory_score":8,"valuation_repricing_score":7,"execution_risk_score":-12,"legal_or_contract_risk_score":"unknown_or_not_supported","dilution_cb_risk_score":"unknown_or_not_supported","accounting_trust_risk_score":-2},"weighted_score_after":65,"stage_label_after":"Stage2-Watch_or_NoGreen","changed_components":["-c22_life_rate_sensitivity_without_explicit_return_guard","-price_only_local_blowoff_guard_strengthened"],"component_delta_explanation":"Life-insurer rate sensitivity and value-up beta cannot be treated as the same as nonlife reserve-quality/capital-return evidence.","MFE_90D_pct":3.84,"MAE_90D_pct":-23.78,"score_return_alignment_label":"guard_improves_false_positive_control","current_profile_verdict":"current_profile_correct_with_counterexample_guard"}
```

### 25.5 shadow_weight rows

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,c22_nonlife_reserve_quality_capital_return_bridge,canonical_archetype_specific,L6_FINANCIAL_CAPITAL_RETURN_DIGITAL,C22_INSURANCE_RATE_CYCLE_RESERVE,0,+3,+3,"Nonlife reserve-quality/CSM visibility plus shareholder-return optionality shortened Green delay in DB손보/삼성화재","avg MFE90 of promoted positives 25.49 vs counterexample 3.84","R6L45_C22_005830_T1_STAGE2_ACTIONABLE_2024-02-23|R6L45_C22_000810_T1_STAGE2_ACTIONABLE_2024-02-23",3,3,1,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,c22_life_rate_sensitivity_without_explicit_return_guard,canonical_archetype_specific,L6_FINANCIAL_CAPITAL_RETURN_DIGITAL,C22_INSURANCE_RATE_CYCLE_RESERVE,0,-4,-4,"Life insurer rate/value-up beta without explicit capital return caused poor MFE/MAE in Hanwha Life","counterexample MFE90 3.84 and MAE90 -23.78","R6L45_C22_088350_T1_STAGE2_ACTIONABLE_2024-02-23",3,3,1,medium,counterexample_guard_only,"not production; blocks generic insurance promotion"
shadow_weight,price_only_local_4b_stays_overlay_only,existing_axis_strengthened,L6_FINANCIAL_CAPITAL_RETURN_DIGITAL,C22_INSURANCE_RATE_CYCLE_RESERVE,true,true,0,"Hanwha Life 2024-02-08 was useful risk warning but lacked non-price evidence for full 4B","4B overlay protected risk but should not be a production thesis-break","R6L45_C22_088350_T2_4B_PRICE_ONLY_2024-02-08",1,1,1,medium,axis_stress_test,"strengthens existing full_4b_requires_non_price_evidence"
```

### 25.6 residual_contribution row

```jsonl
{"row_type":"residual_contribution","round":"R6","loop":"45","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","new_independent_case_count":3,"reused_case_count":0,"new_symbol_count":3,"same_archetype_new_symbol_count":3,"same_archetype_new_trigger_family_count":4,"new_canonical_archetype_count":1,"new_trigger_family_count":4,"positive_case_count":2,"counterexample_count":1,"current_profile_error_count":2,"tested_existing_calibrated_axes":["stage3_green_total_min","stage3_green_revision_min","price_only_blowoff_blocks_positive_stage","full_4b_requires_non_price_evidence"],"residual_error_types_found":["C22_nonlife_Green_too_late","life_insurer_rate_beta_false_positive_risk"],"loop_contribution_label":"canonical_archetype_rule_candidate","do_not_propose_new_weight_delta":false,"auto_selected_coverage_gap":"L6/C22 was not found in stock_agent calibration artifact search and remains undercovered versus R1/R2/R12/R13-heavy prior loops"}
```

### 25.7 narrative_only rows

```jsonl
{"row_type":"narrative_only","case_id":"R6L45_C22_NONE","symbol":null,"large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","reason":"no blocked narrative-only case in this loop","price_source":"Songdaiki/stock-web","usage":"not_weight_calibration"}
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
next_round = R6/C22 holdout validation with additional insurer/reserve-accounting cases OR R8 platform/content/SW/security undercovered loop
suggested_next_objective = holdout_validation | counterexample_mining
avoid_next = repeating 005830/000810/088350 same 2024-02-23 entry group
```

## 28. Source Notes

Stock-web connector checks used in this loop:

```text
manifest = atlas/manifest.json
DB손해보험 profile = atlas/symbol_profiles/005/005830.json
삼성화재 profile = atlas/symbol_profiles/000/000810.json
한화생명 profile = atlas/symbol_profiles/088/088350.json
DB손해보험 price rows = atlas/ohlcv_tradable_by_symbol_year/005/005830/2024.csv
삼성화재 price rows = atlas/ohlcv_tradable_by_symbol_year/000/000810/2024.csv
한화생명 price rows = atlas/ohlcv_tradable_by_symbol_year/088/088350/2024.csv
```

Caveat: The OHLC backtest uses stock-web tradable_raw rows only. Evidence labels are research-proxy labels and are not production scoring code.
