# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
research_session = post_calibrated_sector_archetype_residual_research
scheduled_round = R11
scheduled_loop = 74
completed_round = R11
completed_loop = 74
large_sector_id = L10_POLICY_EVENT_CROSS_REDTEAM_MISC
canonical_archetype_id = C31_POLICY_SUBSIDY_LEGISLATION_EVENT
fine_archetype_id = KOREA_VALUE_UP_POLICY_CAPITAL_RETURN_CONVERSION_SPLIT
output_file = e2r_stock_web_v12_residual_round_R11_loop_74_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_C31_POLICY_SUBSIDY_LEGISLATION_EVENT_research.md
production_scoring_changed = false
shadow_weight_only = true
handoff_prompt_embedded = true
handoff_prompt_executed_now = false
```

This loop adds 4 new independent cases, 2 counterexamples, and 2 residual errors for R11/L10_POLICY_EVENT_CROSS_REDTEAM_MISC/C31_POLICY_SUBSIDY_LEGISLATION_EVENT.

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

The residual question here is not whether Stage2 can precede Green. The question is whether a broad policy headline, specifically Korea's 2024 Corporate Value-up policy package, should count as actionable evidence when the issuer has no visible capital-return conversion route. The policy headline is like rain on a field: fertile balance sheets sprout, but bare rock only gets wet.

## 2. Round / Large Sector / Canonical Archetype Scope

```text
scheduled_round = R11
scheduled_loop = 74
round_schedule_status = valid
round_sector_consistency = pass
large_sector_id = L10_POLICY_EVENT_CROSS_REDTEAM_MISC
canonical_archetype_id = C31_POLICY_SUBSIDY_LEGISLATION_EVENT
fine_archetype_id = KOREA_VALUE_UP_POLICY_CAPITAL_RETURN_CONVERSION_SPLIT
loop_objective = sector_specific_rule_discovery | canonical_archetype_compression | counterexample_mining | coverage_gap_fill | 4B_non_price_requirement_stress_test
```

R11 allows L10 policy/event research. The selected canonical archetype is C31 because the trigger is a policy reform / incentive framework rather than a normal sector earnings cycle.

## 3. Previous Coverage / Duplicate Avoidance Check

Accessible research registry snippets showed old R11 policy/geopolitics/disaster-event loops and R10 construction loops, but this run uses a new v12 case set centered on the Corporate Value-up policy split. The hard duplicate key is not repeated in this MD:

```text
duplicate_key = canonical_archetype_id + symbol + trigger_type + entry_date
new_symbols = 105560 | 000810 | 006220 | 004990
new_trigger_families = policy_headline_to_capital_return_conversion | policy_only_beta_false_positive | price_only_policy_4B_overlay
new_independent_case_count = 4
reused_case_count = 0
```

The old global axis is not re-proposed. It is stress-tested: the existing Stage2 bonus can be too generous for policy-only beta, while the price-only 4B guard remains useful.

## 4. Stock-Web OHLC Input / Price Source Validation

The stock-web manifest was checked for the current run. The atlas reports FinanceData/marcap as the upstream source, raw/unadjusted marcap prices, max_date 2026-02-20, tradable_row_count 14,354,401, raw_row_count 15,214,118, symbol_count 5,414, and calibration_shard_root `atlas/ohlcv_tradable_by_symbol_year`.

```json
{
  "source_name": "FinanceData/marcap",
  "source_repo_url": "https://github.com/FinanceData/marcap",
  "price_adjustment_status": "raw_unadjusted_marcap",
  "min_date": "1995-05-02",
  "max_date": "2026-02-20",
  "tradable_row_count": 14354401,
  "raw_row_count": 15214118,
  "symbol_count": 5414,
  "active_like_symbol_count": 2868,
  "inactive_or_delisted_like_symbol_count": 2546,
  "markets": [
    "KONEX",
    "KOSDAQ",
    "KOSDAQ GLOBAL",
    "KOSPI"
  ],
  "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year",
  "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year",
  "schema_path": "atlas/schema.json",
  "universe_path": "atlas/universe/all_symbols.csv"
}
```

## 5. Historical Eligibility Gate

All representative triggers pass the 180 trading-day forward-window gate.

| symbol | entry_date | 180D available | corporate-action overlap in 180D | calibration_usable | reason |
|---:|---|---|---|---|---|
| 105560 | 2024-02-26 | true | none in profile | true | clean 180D window |
| 000810 | 2024-02-26 | true | no post-2000 profile candidate in window | true | clean 180D window |
| 006220 | 2024-02-26 | true | no 2024 candidate in profile | true | clean 180D window |
| 004990 | 2024-02-26 | true | no 2024 candidate in profile | true | clean 180D window |

## 6. Canonical Archetype Compression Map

```text
fine_archetype = KOREA_VALUE_UP_POLICY_CAPITAL_RETURN_CONVERSION_SPLIT
canonical_archetype_id = C31_POLICY_SUBSIDY_LEGISLATION_EVENT
compression_logic = policy reform headline + company-specific conversion route
```

Policy events are compressed into C31, but the proposed shadow rule splits them into two channels:

```text
convertible_policy_signal:
  policy headline + clear capital-return / ROE / governance execution route
  -> can remain Stage2-Actionable or Stage3-Yellow

policy_only_beta:
  policy headline + price spike + no issuer-level execution path
  -> cap at Watch / Stage2-only, block Green and do not treat as full 4B without non-price risk evidence
```

## 7. Case Selection Summary

| case | symbol | role | trigger | entry | entry_px | MFE30 | MAE30 | MFE90 | MAE90 | MFE180 | MAE180 | current profile |
|---|---:|---|---|---|---:|---:|---:|---:|---:|---:|---:|---|
| R11L74_C31_105560_VALUEUP_BANK_CAPITAL_RETURN | 105560 | positive | 2024-02-26 | 2024-02-26 | 62500 | 25.76 | -4.48 | 44.0 | -4.48 | 66.24 | -4.48 | current_profile_correct |
| R11L74_C31_000810_VALUEUP_INSURANCE_CAPITAL_RETURN | 000810 | positive | 2024-02-26 | 2024-02-26 | 300000 | 15.33 | -4.83 | 31.17 | -4.83 | 31.17 | -4.83 | current_profile_correct |
| R11L74_C31_006220_VALUEUP_SMALL_BANK_FALSE_POSITIVE | 006220 | counterexample | 2024-02-26 | 2024-02-26 | 11710 | 29.63 | -7.51 | 29.63 | -7.51 | 29.63 | -33.3 | current_profile_false_positive |
| R11L74_C31_004990_VALUEUP_HOLDCO_FALSE_POSITIVE | 004990 | counterexample | 2024-02-26 | 2024-02-26 | 28800 | 5.38 | -8.51 | 5.38 | -15.62 | 5.38 | -25.52 | current_profile_false_positive |

## 8. Positive vs Counterexample Balance

```text
positive_case_count = 2
counterexample_count = 2
4B_case_count = 1
4C_case_count = 0
calibration_usable_case_count = 4
calibration_usable_trigger_count = 5
```

The balance is intentional. KB금융 and 삼성화재 show that the policy can become structural when it meets capital-return machinery. 제주은행 and 롯데지주 show the opposite: a policy headline without issuer-level execution is a gust of wind, not an engine.

## 9. Evidence Source Map

| evidence family | evidence available at trigger date | used for Stage2/3? | limitation |
|---|---|---|---|
| Korea Corporate Value-up policy package | Public policy announcement/reporting around 2024-02-26 | yes, but only as policy option | not enough by itself |
| ROE/PBR/capital-return conversion route | Visible market thesis for high-quality financials | yes for KB/삼성화재 | proxy research score, not production score |
| Low-PBR/holding-company label | broad market narrative | watch-only | insufficient without execution |
| Small-bank policy beta | price/relative-strength dominated | watch-only | high MAE and drawdown |

## 10. Price Data Source Map

| symbol | company | shard | profile | entry row | profile status | corporate action status |
|---:|---|---|---|---|---|---|
| 105560 | KB금융 | atlas/ohlcv_tradable_by_symbol_year/105/105560/2024.csv | atlas/symbol_profiles/105/105560.json | 2024-02-26 c=62500 | active_like | clean_180D_window |
| 000810 | 삼성화재 | atlas/ohlcv_tradable_by_symbol_year/000/000810/2024.csv | atlas/symbol_profiles/000/000810.json | 2024-02-26 c=300000 | active_like | clean_180D_window |
| 006220 | 제주은행 | atlas/ohlcv_tradable_by_symbol_year/006/006220/2024.csv | atlas/symbol_profiles/006/006220.json | 2024-02-26 c=11710 | active_like | clean_180D_window |
| 004990 | 롯데지주 | atlas/ohlcv_tradable_by_symbol_year/004/004990/2024.csv | atlas/symbol_profiles/004/004990.json | 2024-02-26 c=28800 | active_like | clean_180D_window |

## 11. Case-by-Case Trigger Grid

### 11.1 KB금융 / 105560

Stage2 was not just "policy." It had a policy catalyst plus capital-return acceptance. Entry was 2024-02-26 close 62,500. The path produced MFE_180D +66.24% with MAE_180D -4.48%.

### 11.2 삼성화재 / 000810

The insurer path also converted. Entry was 2024-02-26 close 300,000. MFE_180D was +31.17% with MAE_180D -4.83%.

### 11.3 제주은행 / 006220

This is the sharp counterexample. Entry was 2024-02-26 close 11,710. It produced MFE_30D +29.63%, so a naive score-return table might celebrate it. But by 180D the same trigger carried MAE_180D -33.30% and post-peak drawdown -48.55%. That is a policy-beta trap.

### 11.4 롯데지주 / 004990

This is the slow counterexample. Entry was 2024-02-26 close 28,800. MFE_180D was only +5.38%, while MAE_180D reached -25.52%. A low-PBR headline without a conversion route behaved like a value trap.

## 12. Trigger-Level OHLC Backtest Tables

| symbol | entry | entry_price | high_30D | low_30D | MFE_30D | MAE_30D | high_90D | low_90D | MFE_90D | MAE_90D | high_180D | low_180D | MFE_180D | MAE_180D | peak_date | peak_price | drawdown_after_peak |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|---:|
| 105560 | 2024-02-26 | 62500 | 78600 | 59700 | 25.76 | -4.48 | 90000 | 59700 | 44.00 | -4.48 | 103900 | 59700 | 66.24 | -4.48 | 2024-10-25 | 103900 | -15.01 |
| 000810 | 2024-02-26 | 300000 | 346000 | 285500 | 15.33 | -4.83 | 393500 | 285500 | 31.17 | -4.83 | 393500 | 285500 | 31.17 | -4.83 | 2024-06-28 | 393500 | -17.66 |
| 006220 | 2024-02-26 | 11710 | 15180 | 10830 | 29.63 | -7.51 | 15180 | 10830 | 29.63 | -7.51 | 15180 | 7810 | 29.63 | -33.30 | 2024-03-14 | 15180 | -48.55 |
| 004990 | 2024-02-26 | 28800 | 30350 | 26350 | 5.38 | -8.51 | 30350 | 24300 | 5.38 | -15.62 | 30350 | 21450 | 5.38 | -25.52 | 2024-02-29 | 30350 | -29.32 |

## 13. Current Calibrated Profile Stress Test

| symbol | current profile likely label | outcome fit | verdict |
|---:|---|---|---|
| 105560 | Stage3-Yellow / actionable policy-capital-return | strong MFE, low MAE | current_profile_correct |
| 000810 | Stage3-Yellow / actionable policy-capital-return | strong MFE, low MAE | current_profile_correct |
| 006220 | Stage3-Yellow if policy + RS overcounted | high early MFE but severe 180D drawdown | current_profile_false_positive |
| 004990 | Stage3-Yellow if policy + low-PBR overcounted | low MFE and high MAE | current_profile_false_positive |

Answers to the profile audit:

```text
stage2_actionable_evidence_bonus = kept, but C31-specific cap needed when no issuer-level conversion exists
stage3_yellow_total_min_75 = too low for policy-only beta
stage3_green_total_min_87 = kept
stage3_green_revision_min_55 = kept
price_only_blowoff_blocks_positive_stage = strengthened
full_4b_requires_non_price_evidence = strengthened
hard_4c_thesis_break_routes_to_4c = kept
```

## 14. Stage2 / Yellow / Green Comparison

No confirmed Stage3-Green trigger is created in this MD. Green would require issuer-level execution evidence after the policy announcement, not merely price movement or low-PBR category membership.

```text
green_lateness_ratio = not_applicable
reason = no_confirmed_Stage3_Green_trigger
```

For KB금융 and 삼성화재, Stage3-Yellow is acceptable because policy optionality and capital-return visibility already reinforce each other. For 제주은행 and 롯데지주, the same policy headline should be capped below Yellow unless non-price execution evidence appears.

## 15. 4B Local vs Full-window Timing Audit

The explicit 4B overlay is 제주은행.

```text
Stage2_Actionable_entry_price = 11710
Stage4B_overlay_entry_price = 14460
local_peak_price_after_Stage2 = 15180
full_window_peak_price_after_Stage2 = 15180
four_b_local_peak_proximity = 0.79
four_b_full_window_peak_proximity = 0.79
four_b_evidence_type = price_only | positioning_overheat
four_b_timing_verdict = price_only_peak_near_full_peak_but_not_full_4B_without_non_price_evidence
```

This supports the existing guard: price-only local peaks can be useful as watch overlays, but they should not become full 4B without non-price evidence.

## 16. 4C Protection Audit

No hard 4C trigger is promoted. 제주은행 and 롯데지주 become thesis-break watch items, but not 4C rows, because the trigger was not a cancelled contract, forced liquidation, regulatory rejection, accounting break, or explicit thesis collapse.

```text
four_c_protection_label = thesis_break_watch_only
hard_4c_routing = kept
```

## 17. Sector-Specific Rule Candidate

```text
rule_scope = sector_specific
rule_id = L10_C31_POLICY_EVENT_CAPITAL_RETURN_CONVERSION_GATE
candidate = true
```

Proposed shadow-only rule:

```text
if large_sector_id == L10_POLICY_EVENT_CROSS_REDTEAM_MISC
and canonical_archetype_id == C31_POLICY_SUBSIDY_LEGISLATION_EVENT
and policy event is broad market-wide incentive/reform
and issuer has no measurable capital-return, contract, subsidy, earnings, or governance execution route:
    cap_positive_stage = Stage2-Watch
    block_Stage3_Yellow_or_Green_from_policy_headline_alone = true
```

## 18. Canonical-Archetype Rule Candidate

```text
rule_scope = canonical_archetype_specific
rule_id = C31_POLICY_HEADLINE_WITHOUT_CONVERSION_PENALTY
candidate = true
```

Component adjustment proposal:

```text
policy_or_regulatory_score:
  allow +7~+8 only when issuer-level conversion exists
  cap at +5 when broad policy only

relative_strength_score:
  cap when the only reinforcement is theme beta

execution_risk_score:
  add penalty when no capital-return / governance / contract / subsidy execution route is visible
```

## 19. Before / After Backtest Comparison

| profile_id | scope | hypothesis | eligible_trigger_count | selected cases | avg_MFE_90D_pct | avg_MAE_90D_pct | avg_MFE_180D_pct | avg_MAE_180D_pct | false_positive_rate | missed_structural_count | late_green_count | score_return_alignment_verdict |
|---|---|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---|
| P0 e2r_2_1_stock_web_calibrated_proxy | current | treats value-up policy as potentially actionable with general Stage2 bonus | 4 | KB, 삼성화재, 제주은행, 롯데지주 | 27.55 | -8.11 | 33.10 | -17.03 | 0.50 | 0 | 0 | mixed; policy-only beta causes residual false positives |
| P0b e2r_2_0_baseline_reference | rollback | lower policy/stage2 conversion; misses part of early financial rerating | 4 | KB, 삼성화재 only partially selected | 37.59 | -4.66 | 48.70 | -4.66 | 0.00 | 2 | 0 | safer but too late/too conservative for real capital-return converters |
| P1 sector_specific_candidate_profile | L10 policy-event | add capital-return conversion requirement and execution-risk penalty | 2 | KB, 삼성화재 | 37.59 | -4.66 | 48.70 | -4.66 | 0.00 | 0 | 0 | better |
| P2 canonical_archetype_candidate_profile | C31 | cap policy-only Stage2 at watch unless ROE/capital-return route exists | 4 | KB, 삼성화재 selected; 제주은행/롯데지주 blocked | 37.59 | -4.66 | 48.70 | -4.66 | 0.00 | 0 | 0 | best shadow candidate |
| P3 counterexample_guard_profile | guard | price-only local policy beta cannot promote Stage3 or full 4B | 4 | same as P2 with 4B overlay only | 37.59 | -4.66 | 48.70 | -4.66 | 0.00 | 0 | 0 | best risk guard |

## 20. Score-Return Alignment Matrix

| symbol | before_score | before_label | after_score | after_label | MFE_90D | MAE_90D | alignment |
|---:|---:|---|---:|---|---:|---:|---|
| 105560 | 82 | Stage3-Yellow | 86 | Stage3-Yellow-Actionable | 44.00 | -4.48 | improved / retained |
| 000810 | 80 | Stage3-Yellow | 84 | Stage3-Yellow-Actionable | 31.17 | -4.83 | improved / retained |
| 006220 | 76 | Stage3-Yellow | 63 | Stage2-Watch-Blocked | 29.63 | -7.51 | corrected false positive |
| 004990 | 75 | Stage3-Yellow | 60 | Stage2-Watch-Blocked | 5.38 | -15.62 | corrected false positive |

The current profile's weakness is not early-entry timing. It is over-trusting a policy label when no issuer-level gear engages.

## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive_case_count | counterexample_count | 4B_case_count | 4C_case_count | new_independent_case_count | reused_case_count | calibration_usable_trigger_count | representative_trigger_count | current_profile_error_count | sector_rule_candidate | canonical_rule_candidate | coverage_gap_after_this_loop |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| L10_POLICY_EVENT_CROSS_REDTEAM_MISC | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | KOREA_VALUE_UP_POLICY_CAPITAL_RETURN_CONVERSION_SPLIT | 2 | 2 | 1 | 0 | 4 | 0 | 5 | 4 | 2 | true | true | Still needs non-financial policy-event holdouts; value-up financial/holdco split now covered. |

## 22. Residual Contribution Summary

```text
new_independent_case_count: 4
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 4
new_canonical_archetype_count: 0
new_fine_archetype_count: 1
new_trigger_family_count: 3
tested_existing_calibrated_axes:
  - stage2_actionable_evidence_bonus
  - stage3_yellow_total_min
  - price_only_blowoff_blocks_positive_stage
  - full_4b_requires_non_price_evidence
residual_error_types_found:
  - policy_headline_false_positive
  - policy_only_beta_high_MAE
  - price_only_local_peak_not_full_4B
new_axis_proposed:
  - C31_policy_headline_requires_issuer_level_conversion
  - C31_policy_only_beta_stage_cap
existing_axis_strengthened:
  - price_only_blowoff_blocks_positive_stage
  - full_4b_requires_non_price_evidence
existing_axis_weakened: null
existing_axis_kept:
  - stage3_green_total_min
  - stage3_green_revision_min
  - hard_4c_thesis_break_routes_to_4c
sector_specific_rule_candidate: true
canonical_archetype_rule_candidate: true
no_new_signal_reason: null
loop_contribution_label: sector_specific_rule_candidate
do_not_propose_new_weight_delta: false
```

## 23. Validation Scope / Non-Validation Scope

Validation scope:

```text
- Historical policy-event trigger dated 2024-02-26
- Songdaiki/stock-web tradable_raw OHLC rows
- 30D / 90D / 180D MFE and MAE
- 4B local-vs-full-window proximity for 제주은행
- C31 policy-event score-return alignment
```

Non-validation scope:

```text
- No live candidate scan
- No current recommendation
- No production scoring change
- No broker/API/trading action
- No stock_agent code reading or patching
- No adjusted-price reconstruction
```

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,C31_policy_headline_requires_capital_return_conversion,canonical_archetype_specific,L10_POLICY_EVENT_CROSS_REDTEAM_MISC,C31_POLICY_SUBSIDY_LEGISLATION_EVENT,0,1,+1,"Value-up policy headline only worked when ROE/capital-return execution existed; false positives had weak execution and high MAE.","P0 false_positive_rate 50%; guard profile reduces false positives while retaining KB/Samsung success","R11L74_C31_105560_20240226_STAGE2A|R11L74_C31_000810_20240226_STAGE2A|R11L74_C31_006220_20240226_STAGE2A|R11L74_C31_004990_20240226_STAGE2A",4,4,2,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,C31_price_only_policy_beta_cap,canonical_archetype_specific,L10_POLICY_EVENT_CROSS_REDTEAM_MISC,C31_POLICY_SUBSIDY_LEGISLATION_EVENT,0,1,+1,"Policy beta without non-price execution may create MFE but produces poor score-return alignment.","Jeju and Lotte block prevents Yellow/Green promotion for high-MAE value-up beta.","R11L74_C31_006220_20240226_STAGE2A|R11L74_C31_004990_20240226_STAGE2A|R11L74_C31_006220_20240313_4B_PRICE_ONLY_OVERHEAT",3,2,2,medium,canonical_shadow_only,"not production; post-calibrated residual"
```

## 25. Machine-Readable Rows

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration"}
{"row_type": "case", "case_id": "R11L74_C31_105560_VALUEUP_BANK_CAPITAL_RETURN", "symbol": "105560", "company_name": "KB금융", "round": "R11", "loop": "74", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "fine_archetype_id": "KOREA_VALUE_UP_POLICY_CAPITAL_RETURN_CONVERSION_SPLIT", "case_type": "structural_success", "positive_or_counterexample": "positive", "best_trigger": "R11L74_C31_105560_20240226_STAGE2A", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "aligned", "current_profile_verdict": "current_profile_correct", "price_source": "Songdaiki/stock-web", "notes": "Policy headline is allowed only because a pre-existing capital-return route and balance-sheet quality made it convertible."}
{"row_type": "case", "case_id": "R11L74_C31_000810_VALUEUP_INSURANCE_CAPITAL_RETURN", "symbol": "000810", "company_name": "삼성화재", "round": "R11", "loop": "74", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "fine_archetype_id": "KOREA_VALUE_UP_POLICY_CAPITAL_RETURN_CONVERSION_SPLIT", "case_type": "structural_success", "positive_or_counterexample": "positive", "best_trigger": "R11L74_C31_000810_20240226_STAGE2A", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "aligned", "current_profile_verdict": "current_profile_correct", "price_source": "Songdaiki/stock-web", "notes": "Sector-specific policy conversion works when capital-return capacity is visible and drawdown remains controlled."}
{"row_type": "case", "case_id": "R11L74_C31_006220_VALUEUP_SMALL_BANK_FALSE_POSITIVE", "symbol": "006220", "company_name": "제주은행", "round": "R11", "loop": "74", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "fine_archetype_id": "KOREA_VALUE_UP_POLICY_CAPITAL_RETURN_CONVERSION_SPLIT", "case_type": "false_positive_green", "positive_or_counterexample": "counterexample", "best_trigger": "R11L74_C31_006220_20240226_STAGE2A", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "misaligned_policy_headline", "current_profile_verdict": "current_profile_false_positive", "price_source": "Songdaiki/stock-web", "notes": "Policy-only beta created MFE but not a durable rerating; high MAE and post-peak drawdown force guard."}
{"row_type": "case", "case_id": "R11L74_C31_004990_VALUEUP_HOLDCO_FALSE_POSITIVE", "symbol": "004990", "company_name": "롯데지주", "round": "R11", "loop": "74", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "fine_archetype_id": "KOREA_VALUE_UP_POLICY_CAPITAL_RETURN_CONVERSION_SPLIT", "case_type": "failed_rerating", "positive_or_counterexample": "counterexample", "best_trigger": "R11L74_C31_004990_20240226_STAGE2A", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "misaligned_policy_headline", "current_profile_verdict": "current_profile_false_positive", "price_source": "Songdaiki/stock-web", "notes": "Low-PBR/holding-company policy language without measurable execution decays into a value trap."}
{"row_type": "trigger", "trigger_id": "R11L74_C31_105560_20240226_STAGE2A", "case_id": "R11L74_C31_105560_VALUEUP_BANK_CAPITAL_RETURN", "symbol": "105560", "company_name": "KB금융", "round": "R11", "loop": "74", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "fine_archetype_id": "KOREA_VALUE_UP_POLICY_CAPITAL_RETURN_CONVERSION_SPLIT", "sector": "policy_event_cross_redteam", "primary_archetype": "policy_subsidy_legislation_event", "loop_objective": "sector_specific_rule_discovery|counterexample_mining|coverage_gap_fill|4B_non_price_requirement_stress_test", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-02-26", "evidence_available_at_that_date": "Corporate Value-up announcement date; bank already had high-quality capital-return/ROE route, treasury-share cancellation capacity, and foreign/institutional ownership acceptance.", "evidence_source": "Reuters/FT value-up package reporting; stock-web OHLC entry row 2024-02-26.", "stage2_evidence_fields": ["policy_or_regulatory_optionality", "relative_strength", "early_revision_signal"], "stage3_evidence_fields": ["financial_visibility", "low_red_team_risk", "multiple_public_sources"], "stage4b_evidence_fields": [], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/105/105560/2024.csv", "profile_path": "atlas/symbol_profiles/105/105560.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-02-26", "entry_price": 62500, "MFE_30D_pct": 25.76, "MFE_90D_pct": 44.0, "MFE_180D_pct": 66.24, "MFE_1Y_pct": 66.24, "MFE_2Y_pct": null, "MAE_30D_pct": -4.48, "MAE_90D_pct": -4.48, "MAE_180D_pct": -4.48, "MAE_1Y_pct": -4.48, "below_entry_price_flag_30D": false, "below_entry_price_flag_90D": true, "peak_date": "2024-10-25", "peak_price": 103900, "drawdown_after_peak_pct": -15.01, "green_lateness_ratio": "not_applicable:no_confirmed_Stage3_Green_trigger", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "not_applicable_for_representative_entry", "four_b_evidence_type": [], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "policy_plus_capital_return_rerating_success", "current_profile_verdict": "current_profile_correct", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R11L74_C31_105560_VALUEUP_BANK_CAPITAL_RETURN_20240226", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "R11L74_C31_000810_20240226_STAGE2A", "case_id": "R11L74_C31_000810_VALUEUP_INSURANCE_CAPITAL_RETURN", "symbol": "000810", "company_name": "삼성화재", "round": "R11", "loop": "74", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "fine_archetype_id": "KOREA_VALUE_UP_POLICY_CAPITAL_RETURN_CONVERSION_SPLIT", "sector": "policy_event_cross_redteam", "primary_archetype": "policy_subsidy_legislation_event", "loop_objective": "sector_specific_rule_discovery|counterexample_mining|coverage_gap_fill|4B_non_price_requirement_stress_test", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-02-26", "evidence_available_at_that_date": "Value-up policy interacted with insurer solvency/capital-return rerating. The case behaved like quality financial operating leverage rather than pure policy beta.", "evidence_source": "Reuters/FT value-up package reporting; stock-web OHLC entry row 2024-02-26.", "stage2_evidence_fields": ["policy_or_regulatory_optionality", "relative_strength", "customer_or_order_quality"], "stage3_evidence_fields": ["financial_visibility", "low_red_team_risk", "multiple_public_sources"], "stage4b_evidence_fields": [], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/000/000810/2024.csv", "profile_path": "atlas/symbol_profiles/000/000810.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-02-26", "entry_price": 300000, "MFE_30D_pct": 15.33, "MFE_90D_pct": 31.17, "MFE_180D_pct": 31.17, "MFE_1Y_pct": 31.17, "MFE_2Y_pct": null, "MAE_30D_pct": -4.83, "MAE_90D_pct": -4.83, "MAE_180D_pct": -4.83, "MAE_1Y_pct": -4.83, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-06-28", "peak_price": 393500, "drawdown_after_peak_pct": -17.66, "green_lateness_ratio": "not_applicable:no_confirmed_Stage3_Green_trigger", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "not_applicable_for_representative_entry", "four_b_evidence_type": [], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "policy_plus_solvency_capital_return_success", "current_profile_verdict": "current_profile_correct", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R11L74_C31_000810_VALUEUP_INSURANCE_CAPITAL_RETURN_20240226", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "R11L74_C31_006220_20240226_STAGE2A", "case_id": "R11L74_C31_006220_VALUEUP_SMALL_BANK_FALSE_POSITIVE", "symbol": "006220", "company_name": "제주은행", "round": "R11", "loop": "74", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "fine_archetype_id": "KOREA_VALUE_UP_POLICY_CAPITAL_RETURN_CONVERSION_SPLIT", "sector": "policy_event_cross_redteam", "primary_archetype": "policy_subsidy_legislation_event", "loop_objective": "sector_specific_rule_discovery|counterexample_mining|coverage_gap_fill|4B_non_price_requirement_stress_test", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-02-26", "evidence_available_at_that_date": "Same policy headline, but no durable capital-return conversion was visible. Price beta and small-bank theme volatility dominated.", "evidence_source": "Reuters/FT value-up package reporting; stock-web OHLC entry row 2024-02-26.", "stage2_evidence_fields": ["policy_or_regulatory_optionality", "relative_strength"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["price_only_local_peak", "positioning_overheat"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/006/006220/2024.csv", "profile_path": "atlas/symbol_profiles/006/006220.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-02-26", "entry_price": 11710, "MFE_30D_pct": 29.63, "MFE_90D_pct": 29.63, "MFE_180D_pct": 29.63, "MFE_1Y_pct": 29.63, "MFE_2Y_pct": null, "MAE_30D_pct": -7.51, "MAE_90D_pct": -7.51, "MAE_180D_pct": -33.3, "MAE_1Y_pct": -33.3, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-03-14", "peak_price": 15180, "drawdown_after_peak_pct": -48.55, "green_lateness_ratio": "not_applicable:no_confirmed_Stage3_Green_trigger", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "not_applicable_for_representative_entry", "four_b_evidence_type": [], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "policy_beta_failed_rerating_high_drawdown", "current_profile_verdict": "current_profile_false_positive", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R11L74_C31_006220_VALUEUP_SMALL_BANK_FALSE_POSITIVE_20240226", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "R11L74_C31_004990_20240226_STAGE2A", "case_id": "R11L74_C31_004990_VALUEUP_HOLDCO_FALSE_POSITIVE", "symbol": "004990", "company_name": "롯데지주", "round": "R11", "loop": "74", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "fine_archetype_id": "KOREA_VALUE_UP_POLICY_CAPITAL_RETURN_CONVERSION_SPLIT", "sector": "policy_event_cross_redteam", "primary_archetype": "policy_subsidy_legislation_event", "loop_objective": "sector_specific_rule_discovery|counterexample_mining|coverage_gap_fill|4B_non_price_requirement_stress_test", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-02-26", "evidence_available_at_that_date": "Holding-company low-PBR headline did not convert into identifiable capital-return / governance execution during the forward window.", "evidence_source": "Reuters/FT value-up package reporting; stock-web OHLC entry row 2024-02-26.", "stage2_evidence_fields": ["policy_or_regulatory_optionality"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["price_only_local_peak"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/004/004990/2024.csv", "profile_path": "atlas/symbol_profiles/004/004990.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-02-26", "entry_price": 28800, "MFE_30D_pct": 5.38, "MFE_90D_pct": 5.38, "MFE_180D_pct": 5.38, "MFE_1Y_pct": 5.38, "MFE_2Y_pct": null, "MAE_30D_pct": -8.51, "MAE_90D_pct": -15.62, "MAE_180D_pct": -25.52, "MAE_1Y_pct": -25.52, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-02-29", "peak_price": 30350, "drawdown_after_peak_pct": -29.32, "green_lateness_ratio": "not_applicable:no_confirmed_Stage3_Green_trigger", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "not_applicable_for_representative_entry", "four_b_evidence_type": [], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "policy_headline_no_execution_failed_rerating", "current_profile_verdict": "current_profile_false_positive", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R11L74_C31_004990_VALUEUP_HOLDCO_FALSE_POSITIVE_20240226", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "R11L74_C31_006220_20240313_4B_PRICE_ONLY_OVERHEAT", "case_id": "R11L74_C31_006220_VALUEUP_SMALL_BANK_FALSE_POSITIVE", "symbol": "006220", "company_name": "제주은행", "round": "R11", "loop": "74", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "fine_archetype_id": "KOREA_VALUE_UP_POLICY_CAPITAL_RETURN_CONVERSION_SPLIT", "sector": "policy_event_cross_redteam", "primary_archetype": "policy_subsidy_legislation_event", "loop_objective": "4B_non_price_requirement_stress_test|counterexample_mining", "trigger_type": "4B-overlay-price-only", "trigger_date": "2024-03-13", "evidence_available_at_that_date": "Local price spike without new non-price execution evidence; close 14,460 vs Stage2 entry 11,710 and full/local peak 15,180.", "evidence_source": "stock-web OHLC row 2024-03-13/2024-03-14; no non-price evidence used.", "stage2_evidence_fields": ["policy_or_regulatory_optionality", "relative_strength"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["price_only_local_peak", "positioning_overheat"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/006/006220/2024.csv", "profile_path": "atlas/symbol_profiles/006/006220.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-03-13", "entry_price": 14460, "MFE_30D_pct": 4.98, "MFE_90D_pct": 4.98, "MFE_180D_pct": 4.98, "MFE_1Y_pct": 4.98, "MFE_2Y_pct": null, "MAE_30D_pct": -18.88, "MAE_90D_pct": -24.2, "MAE_180D_pct": -45.99, "MAE_1Y_pct": -45.99, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-03-14", "peak_price": 15180, "drawdown_after_peak_pct": -48.55, "green_lateness_ratio": "not_applicable:no_confirmed_Stage3_Green_trigger", "four_b_local_peak_proximity": 0.79, "four_b_full_window_peak_proximity": 0.79, "four_b_timing_verdict": "price_only_peak_near_full_peak_but_not_full_4B_without_non_price_evidence", "four_b_evidence_type": ["price_only", "positioning_overheat"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "4B_overlay_price_only_watch_succeeded_but_not_stage_promotion", "current_profile_verdict": "current_profile_correct", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R11L74_C31_006220_VALUEUP_SMALL_BANK_FALSE_POSITIVE_20240313_4B", "dedupe_for_aggregate": false, "aggregate_group_role": "4B_overlay_only", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R11L74_C31_105560_VALUEUP_BANK_CAPITAL_RETURN", "trigger_id": "R11L74_C31_105560_20240226_STAGE2A", "symbol": "105560", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 3, "revision_score": 6, "relative_strength_score": 8, "customer_quality_score": 5, "policy_or_regulatory_score": 7, "valuation_repricing_score": 8, "execution_risk_score": 2, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "roe_pbr_capital_return_score": 9}, "weighted_score_before": 82, "stage_label_before": "Stage3-Yellow", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 3, "revision_score": 6, "relative_strength_score": 8, "customer_quality_score": 5, "policy_or_regulatory_score": 8, "valuation_repricing_score": 8, "execution_risk_score": 1, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "roe_pbr_capital_return_score": 10}, "weighted_score_after": 86, "stage_label_after": "Stage3-Yellow-Actionable", "changed_components": ["policy_or_regulatory_score", "roe_pbr_capital_return_score", "execution_risk_score", "relative_strength_score"], "component_delta_explanation": "Policy headline is allowed only because a pre-existing capital-return route and balance-sheet quality made it convertible.", "MFE_90D_pct": 44.0, "MAE_90D_pct": -4.48, "score_return_alignment_label": "aligned", "current_profile_verdict": "current_profile_correct"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R11L74_C31_000810_VALUEUP_INSURANCE_CAPITAL_RETURN", "trigger_id": "R11L74_C31_000810_20240226_STAGE2A", "symbol": "000810", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 2, "revision_score": 6, "relative_strength_score": 7, "customer_quality_score": 6, "policy_or_regulatory_score": 7, "valuation_repricing_score": 7, "execution_risk_score": 2, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "roe_pbr_capital_return_score": 8}, "weighted_score_before": 80, "stage_label_before": "Stage3-Yellow", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 2, "revision_score": 6, "relative_strength_score": 7, "customer_quality_score": 6, "policy_or_regulatory_score": 8, "valuation_repricing_score": 7, "execution_risk_score": 1, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "roe_pbr_capital_return_score": 9}, "weighted_score_after": 84, "stage_label_after": "Stage3-Yellow-Actionable", "changed_components": ["policy_or_regulatory_score", "roe_pbr_capital_return_score", "execution_risk_score", "relative_strength_score"], "component_delta_explanation": "Sector-specific policy conversion works when capital-return capacity is visible and drawdown remains controlled.", "MFE_90D_pct": 31.17, "MAE_90D_pct": -4.83, "score_return_alignment_label": "aligned", "current_profile_verdict": "current_profile_correct"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R11L74_C31_006220_VALUEUP_SMALL_BANK_FALSE_POSITIVE", "trigger_id": "R11L74_C31_006220_20240226_STAGE2A", "symbol": "006220", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 1, "relative_strength_score": 9, "customer_quality_score": 2, "policy_or_regulatory_score": 7, "valuation_repricing_score": 5, "execution_risk_score": 5, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "roe_pbr_capital_return_score": 2}, "weighted_score_before": 76, "stage_label_before": "Stage3-Yellow", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 5, "customer_quality_score": 1, "policy_or_regulatory_score": 5, "valuation_repricing_score": 2, "execution_risk_score": 8, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "roe_pbr_capital_return_score": 0}, "weighted_score_after": 63, "stage_label_after": "Stage2-Watch-Blocked", "changed_components": ["policy_or_regulatory_score", "roe_pbr_capital_return_score", "execution_risk_score", "relative_strength_score"], "component_delta_explanation": "Policy-only beta created MFE but not a durable rerating; high MAE and post-peak drawdown force guard.", "MFE_90D_pct": 29.63, "MAE_90D_pct": -7.51, "score_return_alignment_label": "false_positive_guard_needed", "current_profile_verdict": "current_profile_false_positive"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R11L74_C31_004990_VALUEUP_HOLDCO_FALSE_POSITIVE", "trigger_id": "R11L74_C31_004990_20240226_STAGE2A", "symbol": "004990", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 1, "relative_strength_score": 3, "customer_quality_score": 2, "policy_or_regulatory_score": 7, "valuation_repricing_score": 5, "execution_risk_score": 5, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "roe_pbr_capital_return_score": 2}, "weighted_score_before": 75, "stage_label_before": "Stage3-Yellow", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 1, "customer_quality_score": 1, "policy_or_regulatory_score": 5, "valuation_repricing_score": 2, "execution_risk_score": 8, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "roe_pbr_capital_return_score": 0}, "weighted_score_after": 60, "stage_label_after": "Stage2-Watch-Blocked", "changed_components": ["policy_or_regulatory_score", "roe_pbr_capital_return_score", "execution_risk_score", "relative_strength_score"], "component_delta_explanation": "Low-PBR/holding-company policy language without measurable execution decays into a value trap.", "MFE_90D_pct": 5.38, "MAE_90D_pct": -15.62, "score_return_alignment_label": "false_positive_guard_needed", "current_profile_verdict": "current_profile_false_positive"}
{"row_type": "residual_contribution", "round": "R11", "loop": "74", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "new_independent_case_count": 4, "reused_case_count": 0, "new_symbol_count": 4, "new_trigger_family_count": 3, "tested_existing_calibrated_axes": ["stage2_actionable_evidence_bonus", "price_only_blowoff_blocks_positive_stage", "full_4b_requires_non_price_evidence", "stage3_yellow_total_min"], "residual_error_types_found": ["policy_headline_false_positive", "price_only_local_peak_misread", "capital_return_conversion_split"], "loop_contribution_label": "sector_specific_rule_candidate", "do_not_propose_new_weight_delta": false}
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
completed_round = R11
completed_loop = 74
next_round = R12
next_loop = 74
round_schedule_status = valid
round_sector_consistency = pass
```

## 28. Source Notes

```text
stock_web_manifest = atlas/manifest.json
stock_web_manifest_max_date = 2026-02-20
price_basis = tradable_raw
price_adjustment_status = raw_unadjusted_marcap
primary_price_source = Songdaiki/stock-web
upstream_source = FinanceData/marcap

official/news event context:
- Korea Corporate Value-up policy package was publicly reported around February 2024.
- This MD uses policy-event timing only as trigger context; quantitative calibration uses stock-web OHLC rows only.

price rows manually checked:
- 105560 2024-02-26 close 62500; 2024-10-25 high 103900
- 000810 2024-02-26 close 300000; 2024-06-28 high 393500
- 006220 2024-02-26 close 11710; 2024-03-14 high 15180; 2024-11-13 low 7810
- 004990 2024-02-26 close 28800; 2024-02-29 high 30350; 2024-11-13 low 21450
```

