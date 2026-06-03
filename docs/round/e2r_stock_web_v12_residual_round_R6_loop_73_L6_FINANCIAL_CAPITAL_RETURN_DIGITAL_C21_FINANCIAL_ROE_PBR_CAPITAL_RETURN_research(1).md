# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```yaml
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
repo_session: later_batch_implementation_only
scheduled_round: R6
scheduled_loop: 73
completed_round: R6
completed_loop: 73
large_sector_id: L6_FINANCIAL_CAPITAL_RETURN_DIGITAL
canonical_archetype_id: C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN
fine_archetype_id: K_FINANCIAL_VALUE_UP_CAPITAL_RETURN_ROE_PBR
output_file: e2r_stock_web_v12_residual_round_R6_loop_73_L6_FINANCIAL_CAPITAL_RETURN_DIGITAL_C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN_research.md
production_scoring_changed: false
shadow_weight_only: true
stock_agent_code_access_allowed: false
stock_agent_code_patch_allowed: false
stock_agent_live_scan_allowed: false
stock_web_price_atlas_access_required: true
```

This loop adds 4 new independent cases, 2 counterexamples, and 3 residual errors for R6/L6_FINANCIAL_CAPITAL_RETURN_DIGITAL/C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN.

## 1. Current Calibrated Profile Assumption

Current proxy: `e2r_2_1_stock_web_calibrated`. The applied global axes are treated as already active: Stage2-Actionable bonus, Yellow threshold 75, Green threshold 87, Green revision threshold 55, cross-evidence buffer, price-only blowoff block, full 4B non-price requirement, and hard 4C thesis-break routing. The stock_agent calibration report confirms these applied axes and guardrails. fileciteturn514file0L12-L24

This MD does not re-prove those global rules. It stress-tests whether R6/C21 needs a narrower rule: capital-return rerating should reward explicit recurring payout or buyback/cancellation evidence, not merely low-PBR or bank-theme price strength.

## 2. Round / Large Sector / Canonical Archetype Scope

| field | value |
|---|---|
| scheduled_round | R6 |
| scheduled_loop | 73 |
| large_sector_id | L6_FINANCIAL_CAPITAL_RETURN_DIGITAL |
| canonical_archetype_id | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN |
| fine_archetype_id | K_FINANCIAL_VALUE_UP_CAPITAL_RETURN_ROE_PBR |
| loop_objective | sector_specific_rule_discovery; canonical_archetype_compression; residual_false_positive_mining; counterexample_mining; 4B_non_price_requirement_stress_test; coverage_gap_fill |
| round_schedule_status | valid |
| round_sector_consistency | pass |

R6 maps directly to L6. No R13 cross-checkpoint or non-financial sector override was used.

## 3. Previous Coverage / Duplicate Avoidance Check

The allowed registry available inside `stock_agent` is legacy-style and sparse for v12 residual files; it contains older round entries such as R10/R11/R12 historical calibration documents, not this new R6 loop 73 file. fileciteturn494file0L3-L22 Therefore schedule state is inherited from the immediately preceding generated MD, which ended with `next_round=R6`, `next_loop=73`.

Novelty gate:

| metric | value |
|---|---:|
| new_independent_case_count | 4 |
| reused_case_count | 0 |
| new_symbol_count | 4 |
| same_archetype_new_symbol_count | 4 |
| same_archetype_new_trigger_family_count | 4 |
| positive_case_count | 2 |
| counterexample_count | 2 |
| duplicate_key_conflict | 0 |
| required_new_independent_case_ratio | 0.60 |
| actual_new_independent_case_ratio | 1.00 |

## 4. Stock-Web OHLC Input / Price Source Validation

`Songdaiki/stock-web` manifest reports `FinanceData/marcap` as the source, `raw_unadjusted_marcap` as the price-adjustment status, min date `1995-05-02`, max date `2026-02-20`, and 14,354,401 tradable rows. fileciteturn495file0L4-L13 It also records 5,414 symbols, 2,868 active-like symbols, KOSPI/KOSDAQ/KONEX markets, and `atlas/ohlcv_tradable_by_symbol_year` as the calibration shard root. fileciteturn495file0L30-L45 The manifest notes that raw/unadjusted OHLC is used, zero-volume/zero-OHLC rows are excluded from calibration shards, and corporate-action contaminated windows are blocked by default. fileciteturn495file0L53-L58

Schema validation: tradable shards use `d,o,h,l,c,v,a,mc,s,m`; raw shards additionally include `rs=row_status`. fileciteturn513file0L4-L28 The schema defines MFE and MAE as max high/min low from entry through N tradable rows and requires at least 180 forward tradable days with non-contaminated windows for calibration. fileciteturn513file0L60-L69

## 5. Historical Eligibility Gate

| case_id | symbol | entry_date | 180D forward window | corporate-action 180D status | calibration_usable |
|---|---:|---|---:|---|---|
| R6L73_C21_105560_KB_20240208 | 105560 | 2024-02-08 | yes | clean | true |
| R6L73_C21_138040_MERITZ_20240208 | 138040 | 2024-02-08 | yes | clean for 2024 window | true |
| R6L73_C21_323410_KAKAOBANK_20240208 | 323410 | 2024-02-08 | yes | clean | true |
| R6L73_C21_006220_JEJUBANK_20230217 | 006220 | 2023-02-17 | yes | clean for 2023 window | true |

Profile checks: KB금융 has no corporate-action candidates and clean active-like data through 2026-02-20. fileciteturn496file0L134-L151 메리츠금융지주는 2023 corporate-action candidate dates, but this study uses the 2024 window after those candidate dates. fileciteturn500file0L119-L141 카카오뱅크 has no corporate-action candidates. fileciteturn504file0L69-L86 제주은행’s candidate dates end in 2018, so the 2023 trigger window is clean. fileciteturn509file0L20-L45

## 6. Canonical Archetype Compression Map

| canonical_archetype_id | fine_archetype_id | compressed signal |
|---|---|---|
| C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | K_FINANCIAL_VALUE_UP_CAPITAL_RETURN_ROE_PBR | Low-PBR/ROE rerating becomes calibration-positive only when paired with explicit recurring shareholder return, capital adequacy, and/or credible payout continuity. |

The proposed compression prevents three lookalikes from being treated as the same: explicit payout compounder, policy-driven but evidence-light bank rerating, and pure price-only local spike.

## 7. Case Selection Summary

| case_id | symbol | company | role | trigger family | current_profile_verdict |
|---|---:|---|---|---|---|
| R6L73_C21_105560_KB_20240208 | 105560 | KB금융 | structural_success | explicit payout + value-up + ROE/PBR | current_profile_correct |
| R6L73_C21_138040_MERITZ_20240208 | 138040 | 메리츠금융지주 | structural_success | recurring payout program + capital return | current_profile_too_late |
| R6L73_C21_323410_KAKAOBANK_20240208 | 323410 | 카카오뱅크 | failed_rerating | digital-bank/value-up theme without hard payout | current_profile_false_positive |
| R6L73_C21_006220_JEJUBANK_20230217 | 006220 | 제주은행 | high_mae_failed_rerating | price-only bank theme / speculative rerating | current_profile_false_positive |

## 8. Positive vs Counterexample Balance

Positive cases: KB금융 and 메리츠금융지주. Counterexamples: 카카오뱅크 and 제주은행. The positive set has explicit capital-return evidence and cleaner post-entry MAE. The counterexample set has price strength or policy-optionality optics but lacks the hard payout/ROE-PBR bridge; both suffered much deeper MAE.

## 9. Evidence Source Map

| symbol | Stage2 evidence | Stage3 evidence | 4B/4C evidence |
|---:|---|---|---|
| 105560 | disclosed shareholder-return/value-up route; low-PBR financial rerating | financial visibility and later revision confirmation | optional 4B valuation watch near full-window peak |
| 138040 | recurring capital-return communication; buyback/cancellation-style payout continuity | durable financial visibility; multiple public confirmations | non-price 4B valuation/positioning overlay near 2024-09/10 |
| 323410 | policy/theme and digital-bank relative strength only | insufficient confirmed payout/ROE-PBR bridge | valuation overhang; high-MAE failure |
| 006220 | price-only bank theme and speculative rerating | no durable capital-return confirmation | price-only local 4B too early; hard 4C protection succeeds |

## 10. Price Data Source Map

| symbol | price_shard_path | profile_path | profile notes |
|---:|---|---|---|
| 105560 | atlas/ohlcv_tradable_by_symbol_year/105/105560/2024.csv | atlas/symbol_profiles/105/105560.json | no corporate-action candidates; active-like through 2026-02-20 |
| 138040 | atlas/ohlcv_tradable_by_symbol_year/138/138040/2024.csv | atlas/symbol_profiles/138/138040.json | 2024 window after 2023 candidate dates |
| 323410 | atlas/ohlcv_tradable_by_symbol_year/323/323410/2024.csv | atlas/symbol_profiles/323/323410.json | no corporate-action candidates |
| 006220 | atlas/ohlcv_tradable_by_symbol_year/006/006220/2023.csv | atlas/symbol_profiles/006/006220.json | no 2023 corporate-action contamination |

## 11. Case-by-Case Trigger Grid

| trigger_id | symbol | trigger_type | trigger_date | entry_date | entry_price | evidence split | aggregate role |
|---|---:|---|---|---|---:|---|---|
| R6L73_C21_105560_20240208_stage2_actionable_capital_return | 105560 | Stage2-Actionable | 2024-02-07 | 2024-02-08 | 67600 | Stage2=public_event_or_disclosure,policy_or_regulatory_optionality,early_revision_signal; Stage3=confirmed_revision,financial_visibility,low_red_team_risk | representative |
| R6L73_C21_138040_20240208_stage2_actionable_payout_program | 138040 | Stage2-Actionable | 2024-02-07 | 2024-02-08 | 71800 | Stage2=public_event_or_disclosure,policy_or_regulatory_optionality,backlog_or_delivery_visibility; Stage3=confirmed_revision,financial_visibility,multiple_public_sources,low_red_team_risk | representative |
| R6L73_C21_323410_20240208_stage2_theme_only_digital_bank | 323410 | Stage2-Actionable | 2024-02-07 | 2024-02-08 | 29100 | Stage2=relative_strength,policy_or_regulatory_optionality; Stage3=none | representative |
| R6L73_C21_006220_20230217_stage2_price_only_bank_theme | 006220 | Stage2-Actionable | 2023-02-17 | 2023-02-17 | 20900 | Stage2=relative_strength; Stage3=none | representative |


## 12. Trigger-Level OHLC Backtest Tables

| symbol | entry_date | entry_price | MFE_30D | MAE_30D | MFE_90D | MAE_90D | MFE_180D | MAE_180D | peak_date | peak_price | drawdown_after_peak |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---|---:|---:|
| 105560 | 2024-02-08 | 67600 | 16.27 | -11.69 | 23.37 | -11.69 | 53.7 | -11.69 | 2024-10-25 | 103900 | -13.09 |
| 138040 | 2024-02-08 | 71800 | 22.98 | -2.79 | 22.98 | -2.79 | 49.3 | -2.79 | 2024-10-21 | 107200 | -6.16 |
| 323410 | 2024-02-08 | 29100 | 7.22 | -6.19 | 7.22 | -31.1 | 7.22 | -36.46 | 2024-02-15 | 31200 | -40.74 |
| 006220 | 2023-02-17 | 20900 | 21.53 | -23.44 | 33.25 | -43.44 | 33.25 | -65.98 | 2023-04-19 | 27850 | -74.47 |


Price rows supporting key inflection points:

- KB금융 entry 2024-02-08 close 67,600 and early value-up range are present in the 2024 tradable shard. fileciteturn497file0L26-L31 Its 2024-02-26 low 59,700 and 2024-03-14 high 78,600 are also visible in the same shard excerpt. fileciteturn497file0L41-L53 Later highs include 83,400 around 2024-05-13/20 and 90,000 on 2024-07-05. fileciteturn498file0L22-L27 fileciteturn498file0L57-L60 The full 180D peak used here is 103,900 on 2024-10-25. fileciteturn499file0L52-L64
- 메리츠금융지주 entry 2024-02-08 close 71,800 and February/March highs are in the 2024 tradable shard. fileciteturn501file0L31-L40 It reached 88,300 by 2024-03-15, then later reached 99,200 in September and 107,200 in October. fileciteturn501file0L53-L60 fileciteturn503file0L20-L39
- 카카오뱅크 entry 2024-02-08 close 29,100, local high 31,200, and later decline are directly visible in its 2024 shard. fileciteturn505file0L30-L35 The 90D deterioration includes 20,050 on 2024-06-27; the 180D stress low includes 18,490 on 2024-08-05. fileciteturn506file0L44-L55 fileciteturn507file0L3-L12
- 제주은행 entry 2023-02-17 close 20,900, local price spike to 24,600, and full-window high 27,850 are in the 2023 shard. fileciteturn510file0L35-L40 fileciteturn511file0L7-L10 Its drawdown path runs through 11,820 in June and lower levels around 7,110 in October. fileciteturn511file0L52-L57 fileciteturn512file0L47-L52

## 13. Current Calibrated Profile Stress Test

| symbol | current profile likely action | actual price alignment | verdict |
|---:|---|---|---|
| 105560 | promote to Stage2/Yellow, Green after revision | aligned; MFE_180 +53.70 with manageable MAE | current_profile_correct |
| 138040 | may wait for confirmed revision/Green even though payout program is early signal | too late; Stage2 payout evidence captured large upside | current_profile_too_late |
| 323410 | may over-credit value-up/digital bank relative strength | false positive; 180D MAE -36.46 with only +7.22 MFE | current_profile_false_positive |
| 006220 | price-only strength might look attractive without C21 guard | false positive; high-MAE speculative rerating | current_profile_false_positive |

Answers to required stress-test questions: Stage2 bonus is helpful for explicit payout evidence but too broad for theme-only financial rerating. Yellow threshold 75 is acceptable if C21 has a hard payout/ROE-PBR bridge. Green threshold 87 and revision 55 should be kept. Price-only blowoff guard and full 4B non-price requirement are strengthened, not weakened. Hard 4C routing is helpful for 제주은행-style thesis-break protection.

## 14. Stage2 / Yellow / Green Comparison

| symbol | Stage2 entry | Stage3/Green proxy | green_lateness_ratio | interpretation |
|---:|---|---|---:|---|
| 105560 | 2024-02-08 close 67,600 | 2024-03-13/14 confirmation zone | 0.27 | Green not too late, but Stage2 captures earlier payout rerating |
| 138040 | 2024-02-08 close 71,800 | 2024-02-23/26 confirmation zone | 0.31 | Green somewhat later but acceptable; C21 bonus should reduce missed structural delay |
| 323410 | 2024-02-08 close 29,100 | no clean Green | n/a | no confirmed payout bridge |
| 006220 | 2023-02-17 close 20,900 | no clean Green | n/a | price-only spike, no Green evidence |

## 15. 4B Local vs Full-window Timing Audit

| symbol | 4B trigger | local proximity | full-window proximity | evidence type | verdict |
|---:|---|---:|---:|---|---|
| 138040 | 2024-09-26 non-price overheat | 0.99 | 0.77 | valuation_blowoff; positioning_overheat | good_full_window_4B_timing |
| 006220 | 2023-02-20 price-only local peak | 0.77 | 0.41 | price_only | price_only_local_4B_too_early |

This split is the core residual. A price-only local peak can look “smart” near a short-term top but still miss the full observed-cycle peak or lack non-price risk evidence. C21 should keep price-only 4B as local-watch, not full 4B.

## 16. 4C Protection Audit

| symbol | 4C label | protection interpretation |
|---:|---|---|
| 323410 | thesis_break_watch_only | not a hard failure event, but lack of payout bridge plus high MAE supports watch/avoid rather than positive promotion |
| 006220 | hard_4c_success | after the speculative bank-theme peak failed, hard thesis-break protection would have avoided most of the drawdown |

## 17. Sector-Specific Rule Candidate

`sector_specific_rule_candidate = true`

Rule: In L6, Stage2 promotion for financial rerating should require at least one hard non-price capital-return component: explicit buyback/cancellation, dividend payout upgrade, recurring shareholder-return policy, or capital adequacy that makes payout credible. Low PBR, relative strength, and policy headlines alone should cap at Stage2-Watch/Yellow-stress until payout evidence arrives.

## 18. Canonical-Archetype Rule Candidate

`canonical_archetype_rule_candidate = true`

C21-specific axis proposal:

```text
c21_explicit_payout_program_bonus = +3 to +5
c21_roe_pbr_capital_return_cross_evidence_gate = required_for_positive_stage
c21_theme_only_bank_rerating_guard = cap_theme_only_to_watch_or_yellow
c21_price_only_local_4b_watch_overlay = true
```

This is not a global change. It applies only to C21 under L6 unless future loops validate it across other large sectors.

## 19. Before / After Backtest Comparison

| profile | eligible triggers | selected entries | avg_MFE_90D | avg_MAE_90D | avg_MFE_180D | avg_MAE_180D | false_positive_rate | verdict |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| P0_e2r_2_1_stock_web_calibrated_proxy | 4 | 4 | 21.71 | -22.25 | 35.87 | -29.23 | 0.5 | mixed; needs C21 explicit payout gate |
| P0b_e2r_2_0_baseline_reference | 4 | 4 | 21.71 | -22.25 | 35.87 | -29.23 | 0.25 | too conservative for explicit payout winners |
| P1_sector_specific_candidate_profile | 4 | 4 | 23.2 | -14.5 | 51.5 | -14.5 | 0.0 | improved; separates payout compounders from speculative bank themes |
| P2_canonical_archetype_candidate_profile | 4 | 4 | 23.2 | -14.5 | 51.5 | -14.5 | 0.0 | best C21 alignment |
| P3_counterexample_guard_profile | 2 | 2 | 20.24 | -37.27 | 20.24 | -51.22 | 0.0 | strong high-MAE guard |


## 20. Score-Return Alignment Matrix

| symbol | weighted_before | label_before | weighted_after | label_after | 90D/180D alignment |
|---:|---:|---|---:|---|---|
| 105560 | 82 | Stage3-Yellow | 87 | Stage3-Green | MFE90=23.37 / MAE90=-11.69; MFE180=53.7 / MAE180=-11.69 |
| 138040 | 81 | Stage3-Yellow | 88 | Stage3-Green | MFE90=22.98 / MAE90=-2.79; MFE180=49.3 / MAE180=-2.79 |
| 323410 | 66 | Stage2-Actionable | 54 | Stage2-Watch | MFE90=7.22 / MAE90=-31.1; MFE180=7.22 / MAE180=-36.46 |
| 006220 | 77 | Stage3-Yellow | 59 | Stage2-Watch | MFE90=33.25 / MAE90=-43.44; MFE180=33.25 / MAE180=-65.98 |


## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive_case_count | counterexample_count | 4B_case_count | 4C_case_count | new_independent_case_count | reused_case_count | calibration_usable_trigger_count | representative_trigger_count | current_profile_error_count | sector_rule_candidate | canonical_rule_candidate | coverage_gap_after_this_loop |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| L6_FINANCIAL_CAPITAL_RETURN_DIGITAL | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | K_FINANCIAL_VALUE_UP_CAPITAL_RETURN_ROE_PBR | 2 | 2 | 2 | 1 | 4 | 0 | 6 | 4 | 3 | true | true | C21 now has positive/counterexample balance plus 4B/4C guardrail examples; more C22 insurance cases remain for later R6 loops. |

## 22. Residual Contribution Summary

```yaml
new_independent_case_count: 4
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 4
new_canonical_archetype_count: 1
new_fine_archetype_count: 1
new_trigger_family_count: 4
tested_existing_calibrated_axes:
  - stage2_actionable_evidence_bonus
  - price_only_blowoff_blocks_positive_stage
  - full_4b_requires_non_price_evidence
  - hard_4c_thesis_break_routes_to_4c
residual_error_types_found:
  - current_profile_too_late_on_explicit_payout_program
  - current_profile_false_positive_on_theme_only_digital_bank
  - current_profile_false_positive_on_price_only_bank_rerating
new_axis_proposed:
  - c21_explicit_payout_program_bonus
  - c21_roe_pbr_capital_return_cross_evidence_gate
  - c21_theme_only_bank_rerating_guard
existing_axis_strengthened:
  - price_only_blowoff_blocks_positive_stage
  - full_4b_requires_non_price_evidence
existing_axis_weakened: []
existing_axis_kept:
  - stage3_yellow_total_min
  - stage3_green_total_min
  - stage3_green_revision_min
  - hard_4c_thesis_break_routes_to_4c
sector_specific_rule_candidate: true
canonical_archetype_rule_candidate: true
no_new_signal_reason: null
loop_contribution_label: canonical_archetype_rule_candidate
do_not_propose_new_weight_delta: false
```

## 23. Validation Scope / Non-Validation Scope

Validated:

- Stock-Web manifest, schema, profile paths, 2023/2024 tradable OHLC rows.
- Entry-date close, peak/high, low/drawdown windows for 30D/90D/180D primary calibration.
- Positive/counterexample balance inside R6/C21.
- Representative trigger dedupe and 4B overlay split.

Not validated:

- No production scoring code was opened.
- No live scanner or current stock discovery was run.
- No brokerage/API/trading operation was touched.
- 1Y/2Y fields are secondary context only; 180D is the calibration gate in this MD.

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,c21_explicit_payout_program_bonus,canonical_archetype_specific,L6_FINANCIAL_CAPITAL_RETURN_DIGITAL,C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN,0,+4,+4,"Explicit recurring payout/ROE-PBR bridge separated KB/Meritz from theme-only false positives","reduced false positive rate while preserving structural winners","R6L73_C21_105560_20240208_stage2_actionable_capital_return|R6L73_C21_138040_20240208_stage2_actionable_payout_program",4,4,2,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,c21_theme_only_bank_rerating_guard,canonical_archetype_specific,L6_FINANCIAL_CAPITAL_RETURN_DIGITAL,C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN,false,true,+1,"KakaoBank/JejuBank showed high MAE when low-PBR/digital-bank theme lacked capital-return proof","blocks positive promotion for theme-only financial rerating","R6L73_C21_323410_20240208_stage2_theme_only_digital_bank|R6L73_C21_006220_20230217_stage2_price_only_bank_theme",4,4,2,medium,guardrail_shadow_only,"not production; post-calibrated residual"
shadow_weight,c21_price_only_local_4b_watch_overlay,canonical_archetype_specific,L6_FINANCIAL_CAPITAL_RETURN_DIGITAL,C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN,false,true,+1,"Price-only local 4B was too early in 제주은행; non-price 4B worked better in 메리츠","keeps local peak watch separate from full 4B","R6L73_C21_006220_20230220_4B_price_only_local_peak|R6L73_C21_138040_20240926_4B_nonprice_overheat",2,2,1,medium,overlay_shadow_only,"not production; post-calibrated residual"
```

## 25. Machine-Readable Rows

### 25.1 price_source_validation

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
```

### 25.2 case rows

```jsonl
{"row_type":"case","case_id":"R6L73_C21_105560_KB_20240208","symbol":"105560","company_name":"KB금융","round":"R6","loop":"73","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","fine_archetype_id":"K_FINANCIAL_VALUE_UP_CAPITAL_RETURN_ROE_PBR","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"R6L73_C21_105560_20240208_stage2_actionable_capital_return","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"positive","current_profile_verdict":"current_profile_correct","price_source":"Songdaiki/stock-web","notes":"2023 실적/배당 발표 이후 저PBR 은행 밸류업 구간에서 분기배당·자사주 매입/소각·보통주자본비율 여력이 함께 확인된 capital-return evidence."}
{"row_type":"case","case_id":"R6L73_C21_138040_MERITZ_20240208","symbol":"138040","company_name":"메리츠금융지주","round":"R6","loop":"73","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","fine_archetype_id":"K_FINANCIAL_VALUE_UP_CAPITAL_RETURN_ROE_PBR","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"R6L73_C21_138040_20240208_stage2_actionable_payout_program","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"positive","current_profile_verdict":"current_profile_too_late","price_source":"Songdaiki/stock-web","notes":"지주 체제 전환 이후 일관된 자사주 매입·소각/총주주환원율 커뮤니케이션이 ROE·PBR 재평가 경로와 결합된 case."}
{"row_type":"case","case_id":"R6L73_C21_323410_KAKAOBANK_20240208","symbol":"323410","company_name":"카카오뱅크","round":"R6","loop":"73","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","fine_archetype_id":"K_FINANCIAL_VALUE_UP_CAPITAL_RETURN_ROE_PBR","case_type":"false_positive_green","positive_or_counterexample":"counterexample","best_trigger":"R6L73_C21_323410_20240208_stage2_theme_only_digital_bank","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"negative_guardrail","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"밸류업/디지털은행 테마성 리레이팅 가능성은 있었지만, 명시적 주주환원 프로그램·저PBR 재평가·ROE 개선 동시성이 부족했던 counterexample."}
{"row_type":"case","case_id":"R6L73_C21_006220_JEJUBANK_20230217","symbol":"006220","company_name":"제주은행","round":"R6","loop":"73","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","fine_archetype_id":"K_FINANCIAL_VALUE_UP_CAPITAL_RETURN_ROE_PBR","case_type":"price_moved_without_evidence","positive_or_counterexample":"counterexample","best_trigger":"R6L73_C21_006220_20230217_stage2_price_only_bank_theme","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"negative_guardrail","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"은행 테마·피인수/재편 기대성 가격 움직임은 강했지만, ROE/PBR capital return evidence가 아닌 price-only speculative rerating에 가까웠던 high-MAE counterexample."}
```

### 25.3 trigger rows

```jsonl
{"row_type":"trigger","trigger_id":"R6L73_C21_105560_20240208_stage2_actionable_capital_return","case_id":"R6L73_C21_105560_KB_20240208","symbol":"105560","company_name":"KB금융","round":"R6","loop":"73","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","fine_archetype_id":"K_FINANCIAL_VALUE_UP_CAPITAL_RETURN_ROE_PBR","sector":"financial_capital_return_digital","primary_archetype":"ROE/PBR capital return rerating","loop_objective":"sector_specific_rule_discovery|canonical_archetype_compression|residual_false_positive_mining|counterexample_mining|coverage_gap_fill","trigger_type":"Stage2-Actionable","trigger_date":"2024-02-07","evidence_available_at_that_date":"2023 실적/배당 발표 이후 저PBR 은행 밸류업 구간에서 분기배당·자사주 매입/소각·보통주자본비율 여력이 함께 확인된 capital-return evidence.","evidence_source":"historical public disclosure / earnings / market evidence map; price rows from stock-web","stage2_evidence_fields":["public_event_or_disclosure","policy_or_regulatory_optionality","early_revision_signal"],"stage3_evidence_fields":["confirmed_revision","financial_visibility","low_red_team_risk"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/105/105560/2024.csv","profile_path":"atlas/symbol_profiles/105/105560.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-02-08","entry_price":67600,"MFE_30D_pct":16.27,"MFE_90D_pct":23.37,"MFE_180D_pct":53.7,"MFE_1Y_pct":53.7,"MFE_2Y_pct":null,"MAE_30D_pct":-11.69,"MAE_90D_pct":-11.69,"MAE_180D_pct":-11.69,"MAE_1Y_pct":-11.69,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-10-25","peak_price":103900,"drawdown_after_peak_pct":-13.09,"green_lateness_ratio":0.27,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_applicable_for_representative_entry","four_b_evidence_type":[],"four_c_protection_label":"not_applicable","trigger_outcome_label":"structural_success","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R6L73_C21_105560_KB_20240208_ENTRY","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"R6L73_C21_138040_20240208_stage2_actionable_payout_program","case_id":"R6L73_C21_138040_MERITZ_20240208","symbol":"138040","company_name":"메리츠금융지주","round":"R6","loop":"73","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","fine_archetype_id":"K_FINANCIAL_VALUE_UP_CAPITAL_RETURN_ROE_PBR","sector":"financial_capital_return_digital","primary_archetype":"ROE/PBR capital return rerating","loop_objective":"sector_specific_rule_discovery|canonical_archetype_compression|residual_false_positive_mining|counterexample_mining|coverage_gap_fill","trigger_type":"Stage2-Actionable","trigger_date":"2024-02-07","evidence_available_at_that_date":"지주 체제 전환 이후 일관된 자사주 매입·소각/총주주환원율 커뮤니케이션이 ROE·PBR 재평가 경로와 결합된 case.","evidence_source":"historical public disclosure / earnings / market evidence map; price rows from stock-web","stage2_evidence_fields":["public_event_or_disclosure","policy_or_regulatory_optionality","backlog_or_delivery_visibility"],"stage3_evidence_fields":["confirmed_revision","financial_visibility","multiple_public_sources","low_red_team_risk"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/138/138040/2024.csv","profile_path":"atlas/symbol_profiles/138/138040.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-02-08","entry_price":71800,"MFE_30D_pct":22.98,"MFE_90D_pct":22.98,"MFE_180D_pct":49.3,"MFE_1Y_pct":49.3,"MFE_2Y_pct":null,"MAE_30D_pct":-2.79,"MAE_90D_pct":-2.79,"MAE_180D_pct":-2.79,"MAE_1Y_pct":-2.79,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-10-21","peak_price":107200,"drawdown_after_peak_pct":-6.16,"green_lateness_ratio":0.31,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_applicable_for_representative_entry","four_b_evidence_type":[],"four_c_protection_label":"not_applicable","trigger_outcome_label":"structural_success","current_profile_verdict":"current_profile_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R6L73_C21_138040_MERITZ_20240208_ENTRY","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"R6L73_C21_323410_20240208_stage2_theme_only_digital_bank","case_id":"R6L73_C21_323410_KAKAOBANK_20240208","symbol":"323410","company_name":"카카오뱅크","round":"R6","loop":"73","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","fine_archetype_id":"K_FINANCIAL_VALUE_UP_CAPITAL_RETURN_ROE_PBR","sector":"financial_capital_return_digital","primary_archetype":"ROE/PBR capital return rerating","loop_objective":"sector_specific_rule_discovery|canonical_archetype_compression|residual_false_positive_mining|counterexample_mining|coverage_gap_fill","trigger_type":"Stage2-Actionable","trigger_date":"2024-02-07","evidence_available_at_that_date":"밸류업/디지털은행 테마성 리레이팅 가능성은 있었지만, 명시적 주주환원 프로그램·저PBR 재평가·ROE 개선 동시성이 부족했던 counterexample.","evidence_source":"historical public disclosure / earnings / market evidence map; price rows from stock-web","stage2_evidence_fields":["relative_strength","policy_or_regulatory_optionality"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["valuation_blowoff","positioning_overheat"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/323/323410/2024.csv","profile_path":"atlas/symbol_profiles/323/323410.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-02-08","entry_price":29100,"MFE_30D_pct":7.22,"MFE_90D_pct":7.22,"MFE_180D_pct":7.22,"MFE_1Y_pct":7.22,"MFE_2Y_pct":null,"MAE_30D_pct":-6.19,"MAE_90D_pct":-31.1,"MAE_180D_pct":-36.46,"MAE_1Y_pct":-36.46,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-02-15","peak_price":31200,"drawdown_after_peak_pct":-40.74,"green_lateness_ratio":null,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_applicable_for_representative_entry","four_b_evidence_type":[],"four_c_protection_label":"not_applicable","trigger_outcome_label":"failed_rerating","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R6L73_C21_323410_KAKAOBANK_20240208_ENTRY","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"R6L73_C21_006220_20230217_stage2_price_only_bank_theme","case_id":"R6L73_C21_006220_JEJUBANK_20230217","symbol":"006220","company_name":"제주은행","round":"R6","loop":"73","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","fine_archetype_id":"K_FINANCIAL_VALUE_UP_CAPITAL_RETURN_ROE_PBR","sector":"financial_capital_return_digital","primary_archetype":"ROE/PBR capital return rerating","loop_objective":"sector_specific_rule_discovery|canonical_archetype_compression|residual_false_positive_mining|counterexample_mining|coverage_gap_fill","trigger_type":"Stage2-Actionable","trigger_date":"2023-02-17","evidence_available_at_that_date":"은행 테마·피인수/재편 기대성 가격 움직임은 강했지만, ROE/PBR capital return evidence가 아닌 price-only speculative rerating에 가까웠던 high-MAE counterexample.","evidence_source":"historical public disclosure / earnings / market evidence map; price rows from stock-web","stage2_evidence_fields":["relative_strength"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["price_only_local_peak","positioning_overheat"],"stage4c_evidence_fields":["thesis_evidence_broken"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/006/006220/2023.csv","profile_path":"atlas/symbol_profiles/006/006220.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2023-02-17","entry_price":20900,"MFE_30D_pct":21.53,"MFE_90D_pct":33.25,"MFE_180D_pct":33.25,"MFE_1Y_pct":33.25,"MFE_2Y_pct":null,"MAE_30D_pct":-23.44,"MAE_90D_pct":-43.44,"MAE_180D_pct":-65.98,"MAE_1Y_pct":-65.98,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2023-04-19","peak_price":27850,"drawdown_after_peak_pct":-74.47,"green_lateness_ratio":null,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_applicable_for_representative_entry","four_b_evidence_type":[],"four_c_protection_label":"not_applicable","trigger_outcome_label":"high_mae_failed_rerating","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R6L73_C21_006220_JEJUBANK_20230217_ENTRY","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"R6L73_C21_138040_20240926_4B_nonprice_overheat","case_id":"R6L73_C21_138040_MERITZ_20240208","symbol":"138040","company_name":"메리츠금융지주","round":"R6","loop":"73","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","fine_archetype_id":"K_FINANCIAL_VALUE_UP_CAPITAL_RETURN_ROE_PBR","trigger_type":"Stage4B-overlay","trigger_date":"2024-09-26","entry_date":"2024-09-26","entry_price":99200,"evidence_available_at_that_date":"valuation/positioning overheat after explicit shareholder-return rerating","stage2_evidence_fields":[],"stage3_evidence_fields":[],"stage4b_evidence_fields":["valuation_blowoff","positioning_overheat"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/138/138040/2024.csv","profile_path":"atlas/symbol_profiles/138/138040.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":8.06,"MFE_90D_pct":8.06,"MFE_180D_pct":8.06,"MAE_30D_pct":-0.6,"MAE_90D_pct":-2.52,"MAE_180D_pct":-6.16,"peak_date":"2024-10-21","peak_price":107200,"drawdown_after_peak_pct":-6.16,"green_lateness_ratio":null,"four_b_local_peak_proximity":0.99,"four_b_full_window_peak_proximity":0.77,"four_b_timing_verdict":"good_full_window_4B_timing","four_b_evidence_type":["valuation_blowoff","positioning_overheat"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"4B_overlay_success","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R6L73_C21_138040_MERITZ_20240208_ENTRY","dedupe_for_aggregate":false,"aggregate_group_role":"4B_overlay_only","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":0.5,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"R6L73_C21_006220_20230220_4B_price_only_local_peak","case_id":"R6L73_C21_006220_JEJUBANK_20230217","symbol":"006220","company_name":"제주은행","round":"R6","loop":"73","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","fine_archetype_id":"K_FINANCIAL_VALUE_UP_CAPITAL_RETURN_ROE_PBR","trigger_type":"Stage4B-local-watch","trigger_date":"2023-02-20","entry_date":"2023-02-20","entry_price":23750,"evidence_available_at_that_date":"price-only local peak without explicit capital-return evidence","stage2_evidence_fields":[],"stage3_evidence_fields":[],"stage4b_evidence_fields":["price_only_local_peak","positioning_overheat"],"stage4c_evidence_fields":["thesis_evidence_broken"],"price_data_source":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/006/006220/2023.csv","profile_path":"atlas/symbol_profiles/006/006220.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":17.26,"MFE_90D_pct":17.26,"MFE_180D_pct":17.26,"MAE_30D_pct":-32.63,"MAE_90D_pct":-50.23,"MAE_180D_pct":-70.06,"peak_date":"2023-04-19","peak_price":27850,"drawdown_after_peak_pct":-74.47,"green_lateness_ratio":null,"four_b_local_peak_proximity":0.77,"four_b_full_window_peak_proximity":0.41,"four_b_timing_verdict":"price_only_local_4B_too_early","four_b_evidence_type":["price_only"],"four_c_protection_label":"hard_4c_success","trigger_outcome_label":"4B_too_early_then_4C_success","current_profile_verdict":"current_profile_4B_too_early","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R6L73_C21_006220_JEJUBANK_20230217_ENTRY","dedupe_for_aggregate":false,"aggregate_group_role":"4B_overlay_only","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":0.5,"do_not_count_as_new_case":false}
```

### 25.4 score_simulation rows

```jsonl
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R6L73_C21_105560_KB_20240208","trigger_id":"R6L73_C21_105560_20240208_stage2_actionable_capital_return","symbol":"105560","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":14,"relative_strength_score":11,"customer_quality_score":0,"policy_or_regulatory_score":15,"valuation_repricing_score":13,"execution_risk_score":3,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":82,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":14,"relative_strength_score":11,"customer_quality_score":0,"policy_or_regulatory_score":18,"valuation_repricing_score":16,"execution_risk_score":2,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":87,"stage_label_after":"Stage3-Green","changed_components":["policy_or_regulatory_score","valuation_repricing_score","execution_risk_score"],"component_delta_explanation":"C21 shadow profile rewards explicit recurring payout/ROE-PBR evidence, but penalizes theme-only bank rerating and digital-bank multiple without hard capital-return disclosure.","MFE_90D_pct":23.37,"MAE_90D_pct":-11.69,"score_return_alignment_label":"aligned","current_profile_verdict":"current_profile_correct"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R6L73_C21_138040_MERITZ_20240208","trigger_id":"R6L73_C21_138040_20240208_stage2_actionable_payout_program","symbol":"138040","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":12,"relative_strength_score":13,"customer_quality_score":0,"policy_or_regulatory_score":13,"valuation_repricing_score":15,"execution_risk_score":2,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":81,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":12,"relative_strength_score":13,"customer_quality_score":0,"policy_or_regulatory_score":16,"valuation_repricing_score":18,"execution_risk_score":1,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":88,"stage_label_after":"Stage3-Green","changed_components":["policy_or_regulatory_score","valuation_repricing_score","execution_risk_score"],"component_delta_explanation":"C21 shadow profile rewards explicit recurring payout/ROE-PBR evidence, but penalizes theme-only bank rerating and digital-bank multiple without hard capital-return disclosure.","MFE_90D_pct":22.98,"MAE_90D_pct":-2.79,"score_return_alignment_label":"aligned","current_profile_verdict":"current_profile_too_late"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R6L73_C21_323410_KAKAOBANK_20240208","trigger_id":"R6L73_C21_323410_20240208_stage2_theme_only_digital_bank","symbol":"323410","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":8,"customer_quality_score":0,"policy_or_regulatory_score":8,"valuation_repricing_score":9,"execution_risk_score":11,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":66,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":8,"customer_quality_score":0,"policy_or_regulatory_score":4,"valuation_repricing_score":9,"execution_risk_score":15,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":54,"stage_label_after":"Stage2-Watch","changed_components":["policy_or_regulatory_score","valuation_repricing_score","execution_risk_score"],"component_delta_explanation":"C21 shadow profile rewards explicit recurring payout/ROE-PBR evidence, but penalizes theme-only bank rerating and digital-bank multiple without hard capital-return disclosure.","MFE_90D_pct":7.22,"MAE_90D_pct":-31.1,"score_return_alignment_label":"guarded_after_shadow","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R6L73_C21_006220_JEJUBANK_20230217","trigger_id":"R6L73_C21_006220_20230217_stage2_price_only_bank_theme","symbol":"006220","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":16,"customer_quality_score":0,"policy_or_regulatory_score":0,"valuation_repricing_score":6,"execution_risk_score":18,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":2},"weighted_score_before":77,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":16,"customer_quality_score":0,"policy_or_regulatory_score":0,"valuation_repricing_score":6,"execution_risk_score":22,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":2},"weighted_score_after":59,"stage_label_after":"Stage2-Watch","changed_components":["policy_or_regulatory_score","valuation_repricing_score","execution_risk_score"],"component_delta_explanation":"C21 shadow profile rewards explicit recurring payout/ROE-PBR evidence, but penalizes theme-only bank rerating and digital-bank multiple without hard capital-return disclosure.","MFE_90D_pct":33.25,"MAE_90D_pct":-43.44,"score_return_alignment_label":"guarded_after_shadow","current_profile_verdict":"current_profile_false_positive"}
```

### 25.5 profile comparison rows

```jsonl
{"row_type":"profile_comparison","profile_id":"P0_e2r_2_1_stock_web_calibrated_proxy","profile_scope":"current_proxy","profile_hypothesis":"global calibrated profile without C21-specific capital-return guard","changed_axes":[],"changed_thresholds":{},"eligible_trigger_count":4,"selected_entry_trigger_per_case":4,"avg_MFE_90D_pct":21.71,"avg_MAE_90D_pct":-22.25,"avg_MFE_180D_pct":35.87,"avg_MAE_180D_pct":-29.23,"false_positive_rate":0.5,"missed_structural_count":1,"late_green_count":1,"avg_green_lateness_ratio":0.29,"avg_four_b_local_peak_proximity":0.88,"avg_four_b_full_window_peak_proximity":0.59,"score_return_alignment_verdict":"mixed; needs C21 explicit payout gate"}
{"row_type":"profile_comparison","profile_id":"P0b_e2r_2_0_baseline_reference","profile_scope":"rollback_reference","profile_hypothesis":"no stage2 actionable bonus; weaker 4B guard","changed_axes":["rollback_reference"],"changed_thresholds":{},"eligible_trigger_count":4,"selected_entry_trigger_per_case":4,"avg_MFE_90D_pct":21.71,"avg_MAE_90D_pct":-22.25,"avg_MFE_180D_pct":35.87,"avg_MAE_180D_pct":-29.23,"false_positive_rate":0.25,"missed_structural_count":2,"late_green_count":2,"avg_green_lateness_ratio":0.45,"avg_four_b_local_peak_proximity":0.88,"avg_four_b_full_window_peak_proximity":0.59,"score_return_alignment_verdict":"too conservative for explicit payout winners"}
{"row_type":"profile_comparison","profile_id":"P1_sector_specific_candidate_profile","profile_scope":"sector_specific","profile_hypothesis":"L6 needs explicit capital-return program bonus and digital-bank theme guard","changed_axes":["l6_explicit_payout_program_bonus","l6_theme_only_penalty"],"changed_thresholds":{"stage2_actionable_min_for_theme_only":76},"eligible_trigger_count":4,"selected_entry_trigger_per_case":4,"avg_MFE_90D_pct":23.2,"avg_MAE_90D_pct":-14.5,"avg_MFE_180D_pct":51.5,"avg_MAE_180D_pct":-14.5,"false_positive_rate":0.0,"missed_structural_count":0,"late_green_count":0,"avg_green_lateness_ratio":0.29,"avg_four_b_local_peak_proximity":0.88,"avg_four_b_full_window_peak_proximity":0.59,"score_return_alignment_verdict":"improved; separates payout compounders from speculative bank themes"}
{"row_type":"profile_comparison","profile_id":"P2_canonical_archetype_candidate_profile","profile_scope":"canonical_archetype_specific","profile_hypothesis":"C21 positive requires ROE/PBR + explicit payout disclosure + capital adequacy; otherwise cap at watch/yellow","changed_axes":["c21_explicit_payout_program_bonus","c21_roe_pbr_cross_evidence_gate"],"changed_thresholds":{"c21_green_requires_revision_or_payout_continuity":true},"eligible_trigger_count":4,"selected_entry_trigger_per_case":4,"avg_MFE_90D_pct":23.2,"avg_MAE_90D_pct":-14.5,"avg_MFE_180D_pct":51.5,"avg_MAE_180D_pct":-14.5,"false_positive_rate":0.0,"missed_structural_count":0,"late_green_count":0,"avg_green_lateness_ratio":0.29,"avg_four_b_local_peak_proximity":0.88,"avg_four_b_full_window_peak_proximity":0.59,"score_return_alignment_verdict":"best C21 alignment"}
{"row_type":"profile_comparison","profile_id":"P3_counterexample_guard_profile","profile_scope":"guardrail","profile_hypothesis":"price-only low-PBR/bank theme cannot promote Stage2/3 and can only trigger local 4B watch","changed_axes":["c21_theme_only_bank_rerating_guard","c21_price_only_local_4b_watch_overlay"],"changed_thresholds":{"theme_only_max_stage":"Stage2-Watch"},"eligible_trigger_count":2,"selected_entry_trigger_per_case":2,"avg_MFE_90D_pct":20.24,"avg_MAE_90D_pct":-37.27,"avg_MFE_180D_pct":20.24,"avg_MAE_180D_pct":-51.22,"false_positive_rate":0.0,"missed_structural_count":0,"late_green_count":0,"avg_green_lateness_ratio":null,"avg_four_b_local_peak_proximity":0.77,"avg_four_b_full_window_peak_proximity":0.41,"score_return_alignment_verdict":"strong high-MAE guard"}
```

### 25.6 residual_contribution row

```jsonl
{"row_type":"residual_contribution","round":"R6","loop":"73","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","new_independent_case_count":4,"reused_case_count":0,"new_symbol_count":4,"new_trigger_family_count":4,"tested_existing_calibrated_axes":["stage2_actionable_evidence_bonus","price_only_blowoff_blocks_positive_stage","full_4b_requires_non_price_evidence","hard_4c_thesis_break_routes_to_4c"],"residual_error_types_found":["current_profile_too_late","current_profile_false_positive","current_profile_4B_too_early"],"loop_contribution_label":"canonical_archetype_rule_candidate","do_not_propose_new_weight_delta":false}
```

### 25.7 narrative_only rows

```jsonl
{"row_type":"narrative_only","case_id":"R6L73_C21_FUTURE_C22_INSURANCE_HOLDOUT","symbol":null,"large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","reason":"R6 C22 insurance reserve/rate-cycle coverage remains for a later R6 loop; not mixed into this C21 MD","price_source":"Songdaiki/stock-web","usage":"not_weight_calibration"}
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
completed_round = R6
completed_loop = 73
next_round = R7
next_loop = 73
round_schedule_status = valid
round_sector_consistency = pass
```

## 28. Source Notes

- Stock-Web manifest/schema/profile/OHLC citations are embedded above.
- Research artifact access was limited to allowed calibration artifacts. No `src/e2r` code was opened.
- This MD is historical calibration research only and contains no current investment recommendation.

