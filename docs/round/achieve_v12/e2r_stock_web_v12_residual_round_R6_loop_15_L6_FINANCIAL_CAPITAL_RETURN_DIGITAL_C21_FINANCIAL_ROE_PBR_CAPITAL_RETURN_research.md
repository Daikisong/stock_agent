# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
research_session = post_calibrated_sector_archetype_residual_research
round = R6
loop = 15
large_sector_id = L6_FINANCIAL_CAPITAL_RETURN_DIGITAL
canonical_archetype_id = C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN
fine_archetype_id = BANK_CAPITAL_RETURN_QUALITY / POLICY_ONLY_VALUEUP_GUARD
selection_mode = auto_coverage_gap_fill
output_file = e2r_stock_web_v12_residual_round_R6_loop_15_L6_FINANCIAL_CAPITAL_RETURN_DIGITAL_C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN_research.md
production_scoring_changed = false
shadow_weight_only = true
handoff_prompt_embedded = true
handoff_prompt_executed_now = false
```

This MD is historical calibration research only. It is not a live candidate scan, not a trading recommendation, and not a repository patch.

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

The research question is not whether Stage2 can be early. The question is narrower: in C21, does a financial-sector Value-Up narrative become useful evidence only when it is anchored by company-specific capital return and ROE/PBR mechanics?

## 2. Round / Large Sector / Canonical Archetype Scope

```text
round = R6
large_sector_id = L6_FINANCIAL_CAPITAL_RETURN_DIGITAL
canonical_archetype_id = C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN
loop_objective = sector_specific_rule_discovery | canonical_archetype_compression | counterexample_mining | coverage_gap_fill | 4B_non_price_requirement_stress_test
```

C21 is not a generic “cheap bank” bucket. The mechanism is:

```text
capital_return_visibility + ROE durability + PBR rerating path
```

Without company-specific capital return, the event is closer to policy beta than investable evidence. A policy wind can fill the sail, but it cannot replace the hull.

## 3. Previous Coverage / Duplicate Avoidance Check

A repository search was performed against the allowed research-artifact surface, not source code. The search terms were:

```text
C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN
KB금융
하나금융지주
신한지주
카카오뱅크
value-up
capital return
```

Search result: no directly matching accessible research artifact was returned by the GitHub search connector for this loop. The loop is therefore treated as a coverage-gap fill, subject to later batch-ingest dedupe.

Novelty check:

```text
new_independent_case_count = 4
reused_case_count = 0
new_symbol_count = 4
same_archetype_new_symbol_count = 4
same_archetype_new_trigger_family_count = 4
new_canonical_archetype_count = 1
new_trigger_family_count = 4
minimum_new_independent_case_ratio = 1.00
```

## 4. Stock-Web OHLC Input / Price Source Validation

Stock-Web manifest validation:

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
markets = KONEX, KOSDAQ, KOSDAQ GLOBAL, KOSPI
calibration_shard_root = atlas/ohlcv_tradable_by_symbol_year
raw_shard_root = atlas/ohlcv_raw_by_symbol_year
schema_path = atlas/schema.json
universe_path = atlas/universe/all_symbols.csv
```

Schema validation: tradable shards use `d,o,h,l,c,v,a,mc,s,m`; raw shards add `rs`. MFE/MAE formulas follow Stock-Web schema.

## 5. Historical Eligibility Gate

All representative triggers are historical and have at least 180 forward trading days in Stock-Web. Corporate-action status:

```text
105560 KB금융: clean_180D_window, corporate_action_candidate_dates = []
086790 하나금융지주: clean_180D_window, corporate_action_candidate_dates = []
055550 신한지주: clean_180D_window, corporate_action_candidate_dates = []
323410 카카오뱅크: clean_180D_window, corporate_action_candidate_dates = []
```

## 6. Canonical Archetype Compression Map

| fine_archetype_id | canonical_archetype_id | rule implication |
|---|---|---|
| BANK_CAPITAL_RETURN_CET1_BUYBACK_CANCEL | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | Explicit return/cancellation quality can promote Stage2/Yellow. |
| BANK_VALUEUP_CAPITAL_RETURN_POSITIVE | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | Moderate positive; requires ROE/revision support for Green. |
| BANK_CAPITAL_RETURN_SCALE_HIGH_MAE_COUNTEREXAMPLE | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | Real return evidence can still be capped by high-MAE absorption failure. |
| BANK_VALUEUP_POLICY_ONLY_NO_CAPITAL_RETURN_GUARD | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | Policy-only low-PBR beta cannot promote positive stage. |

## 7. Case Selection Summary

| case_id | symbol | role | entry | MFE90 | MAE90 | MFE180 | MAE180 | current_profile |
|---|---:|---|---:|---:|---:|---:|---:|---|
| R6L15_C21_KB_20240208_CAPITAL_RETURN_QUALITY | 105560 | positive / structural_success | 67,600 | 23.37 | -11.69 | 53.7 | -11.69 | current_profile_correct |
| R6L15_C21_HANA_20240208_CAPITAL_RETURN_QUALITY | 086790 | positive / stage2_promote_candidate | 56,600 | 15.37 | -8.83 | 22.44 | -8.83 | current_profile_correct |
| R6L15_C21_SHINHAN_20240729_RETURN_SCALE_MAE_GUARD | 055550 | counterexample / high_mae_success | 60,700 | 6.43 | -18.29 | 6.43 | -29.98 | current_profile_false_positive |
| R6L15_C21_KAKAOBANK_20240227_POLICY_ONLY_FALSE_POSITIVE | 323410 | counterexample / failed_rerating | 29,550 | 3.72 | -32.15 | 3.72 | -37.43 | current_profile_false_positive |

## 8. Positive vs Counterexample Balance

```text
positive_case_count = 2
counterexample_count = 2
4B_case_count = 1
4C_case_count = 2 watch labels
calibration_usable_case_count = 4
```

The positive cases are not simply the bank sector rising. They have company-specific return/ROE/PBR evidence. The counterexamples separate two failure modes:

1. **Shinhan**: real return evidence, but weak post-event absorption and high MAE.
2. **KakaoBank**: policy beta without company-specific capital return evidence.

## 9. Evidence Source Map

| case_id | evidence family | source confidence | note |
|---|---|---|---|
| KB | FY2023 earnings/shareholder-return disclosure + Value-Up context | medium | Event date uses company-specific return disclosure family; OHLC is directly validated. |
| Hana | FY2023 return/rerating disclosure + Value-Up context | medium | Moderate positive route; not strong enough alone for aggressive Green. |
| Shinhan | 2024 return disclosure / 2Q route | medium | Real event, poor absorption; useful guard case. |
| KakaoBank | policy-only Value-Up / low-PBR beta | high for policy context, medium for company-specific absence | Representative false positive for policy-only rerating. |

Public policy context: Korea's Corporate Value-Up Programme was announced in February 2024 and later discussed by regulators as a shareholder-return reform package. The policy context is only a backdrop; C21 promotion requires company-specific return evidence.

## 10. Price Data Source Map

| symbol | company | profile_path | primary_shard_path | profile caveat |
|---:|---|---|---|---|
| 105560 | KB금융 | atlas/symbol_profiles/105/105560.json | atlas/ohlcv_tradable_by_symbol_year/105/105560/2024.csv | clean |
| 086790 | 하나금융지주 | atlas/symbol_profiles/086/086790.json | atlas/ohlcv_tradable_by_symbol_year/086/086790/2024.csv | clean |
| 055550 | 신한지주 | atlas/symbol_profiles/055/055550.json | atlas/ohlcv_tradable_by_symbol_year/055/055550/2024.csv | clean |
| 323410 | 카카오뱅크 | atlas/symbol_profiles/323/323410.json | atlas/ohlcv_tradable_by_symbol_year/323/323410/2024.csv | clean |

## 11. Case-by-Case Trigger Grid

| trigger_id | company | type | trigger_date | entry_date | entry_price | MFE30 | MAE30 | MFE180 | MAE180 | peak | usable |
|---|---|---|---|---|---:|---:|---:|---:|---:|---|---|
| TRG_R6L15_KB_20240208_STAGE2A | KB금융 | Stage2-Actionable | 2024-02-07 | 2024-02-08 | 67,600 | 16.27 | -11.69 | 53.7 | -11.69 | 2024-10-25 / 103,900 | True |
| TRG_R6L15_HANA_20240208_STAGE2A | 하나금융지주 | Stage2-Actionable | 2024-02-07 | 2024-02-08 | 56,600 | 15.19 | -6.71 | 22.44 | -8.83 | 2024-08-27 / 69,300 | True |
| TRG_R6L15_SHINHAN_20240729_STAGE2A | 신한지주 | Stage2-Actionable | 2024-07-26 | 2024-07-29 | 60,700 | 6.43 | -14.99 | 6.43 | -29.98 | 2024-08-26 / 64,600 | True |
| TRG_R6L15_KAKAOBANK_20240227_STAGE2_POLICY_ONLY | 카카오뱅크 | Stage2-Watch | 2024-02-26 | 2024-02-27 | 29,550 | 3.72 | -16.07 | 3.72 | -37.43 | 2024-02-27 / 30,650 | True |
| TRG_R6L15_KB_20241025_4B_LOCAL_OVERLAY | KB금융 | Stage4B-Overlay | 2024-10-25 | 2024-10-25 | 101,000 | 2.87 | -15.05 | 20.79 | -31.39 | 2025-07-25 / 126,600 | True |

## 12. Trigger-Level OHLC Backtest Tables

### 12.1 Representative aggregate triggers

| company | entry close | MFE30 | MAE30 | MFE90 | MAE90 | MFE180 | MAE180 | interpretation |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| KB금융 | 67,600 | 16.27 | -11.69 | 23.37 | -11.69 | 53.70 | -11.69 | Strong rerating after company-specific return evidence. |
| 하나금융지주 | 56,600 | 15.19 | -6.71 | 15.37 | -8.83 | 22.44 | -8.83 | Moderate positive rerating. |
| 신한지주 | 60,700 | 6.43 | -14.99 | 6.43 | -18.29 | 6.43 | -29.98 | Real return event but poor absorption; cap Green. |
| 카카오뱅크 | 29,550 | 3.72 | -16.07 | 3.72 | -32.15 | 3.72 | -37.43 | Policy-only beta false positive. |

### 12.2 4B overlay

KB's 2024-10-25 local high looked like a blow-off after the first rerating leg. However, the full observed cycle later printed a higher high in 2025. Therefore a price-only local 4B would have been too early.

```text
Stage2_Actionable_entry_price = 67,600
Stage4B_overlay_entry_price = 101,000
local_peak_after_stage2 = 103,900
full_observed_peak_after_stage2 = 126,600

four_b_local_peak_proximity = 0.92
four_b_full_window_peak_proximity = 0.57
four_b_timing_verdict = price_only_local_4B_too_early
```

## 13. Current Calibrated Profile Stress Test

| case | current profile expected behavior | actual path | verdict |
|---|---|---|---|
| KB | Promote Stage2/Yellow; allow Green if revision/return quality confirmed. | Strong 180D MFE with manageable MAE. | current_profile_correct |
| Hana | Promote Stage2/Yellow, but not necessarily Green. | Moderate 180D MFE; drawdown controlled. | current_profile_correct |
| Shinhan | Risk of overpromoting because return evidence existed. | Small MFE, high MAE. | current_profile_false_positive |
| KakaoBank | Risk of overcrediting policy-only low-PBR beta. | Persistent downside; weak MFE. | current_profile_false_positive |
| KB 4B overlay | Price-only local 4B could fire too early. | Full observed cycle later exceeded local peak. | current_profile_4B_too_early |

Stress-test answers:

```text
stage2_actionable_evidence_bonus = useful for KB/Hana, excessive if applied to policy-only KakaoBank
yellow_threshold_75 = acceptable, but should require company-specific return evidence for C21
green_threshold_87 = acceptable; KB can pass after quality bonus, Hana should remain Yellow
green_revision_min_55 = kept; financial return rerating still needs revision/ROE bridge
price_only_blowoff_guard = strengthened within C21
full_4b_requires_non_price_evidence = strengthened within C21
hard_4c_thesis_break_routes_to_4c = kept; Shinhan/KakaoBank are watch/guard labels, not hard 4C unless explicit thesis evidence breaks
```

## 14. Stage2 / Yellow / Green Comparison

No clean separate Stage3-Green trigger was added for this loop; Green was simulated as a profile outcome rather than a second event row.

```text
green_lateness_ratio = not_applicable
reason = no_confirmed_Stage3_Green_trigger
```

Interpretation: in C21, Green should be less about the second price leg and more about **return quality + ROE/revision confirmation**. Otherwise the Green label becomes a painted road sign after the car has already passed.

## 15. 4B Local vs Full-window Timing Audit

The KB overlay is the key 4B lesson.

| trigger | local proximity | full-window proximity | verdict | evidence type |
|---|---:|---:|---|---|
| TRG_R6L15_KB_20241025_4B_LOCAL_OVERLAY | 0.92 | 0.57 | price_only_local_4B_too_early | price_only, valuation_blowoff, positioning_overheat |

This strengthens, not weakens, the existing global axis:

```text
full_4b_requires_non_price_evidence = existing_axis_strengthened
```

## 16. 4C Protection Audit

No hard 4C row is proposed. Shinhan and KakaoBank receive watch/protection labels only.

| case | label | reason |
|---|---|---|
| Shinhan | thesis_break_watch_only | high MAE after real return evidence; no explicit hard thesis break in this loop |
| KakaoBank | thesis_break_watch_only | policy-only beta failed; guard row rather than hard 4C |

## 17. Sector-Specific Rule Candidate

```text
sector_specific_rule_candidate = false
```

This loop has only one large sector. It is better handled as canonical C21 until other financial sub-verticals are added.

## 18. Canonical-Archetype Rule Candidate

```text
canonical_archetype_rule_candidate = true
rule_scope = canonical_archetype_specific
```

Proposed C21 shadow rules:

```text
1. c21_confirmed_capital_return_quality_bonus = +2
   Apply when trigger evidence includes explicit buyback/cancellation, distribution framework, or shareholder-return plan with observable ROE/PBR bridge.

2. c21_no_company_specific_return_guard = -4
   Apply when the only evidence is policy beta, low-PBR theme, or sector Value-Up narrative without company-specific return plan.

3. c21_high_MAE_after_return_event_guard = -2
   Apply when return evidence exists but post-event absorption is poor and early MAE exceeds roughly -14% without stronger revision evidence.

4. price_only_local_4B_too_early_guard = existing_axis_strengthened
   Local price peak alone must not become full 4B in C21.
```

## 19. Before / After Backtest Comparison

| profile_id | scope | hypothesis | eligible_trigger_count | avg_MFE_90D | avg_MAE_90D | avg_MFE_180D | avg_MAE_180D | false_positive_rate | missed_structural_count | late_green_count | verdict |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| P0 e2r_2_1_stock_web_calibrated_proxy | current | Treats company-specific return evidence as useful, but may still over-credit policy beta. | 4 | 12.24 | -17.99 | 21.57 | -22.23 | 0.50 | 0 | 0 | mixed |
| P0b e2r_2_0_baseline_reference | rollback | Earlier profile under-weights Stage2 actionable return evidence and is slower on KB/Hana. | 4 | 12.24 | -17.99 | 21.57 | -22.23 | 0.25 | 1 | 1 | too_late_on_positive |
| P1 sector_specific_candidate_profile | L6 sector | Add capital-return-quality and post-event absorption gates inside financials. | 4 | 19.37 | -10.26 | 38.07 | -10.26 | 0.25 | 0 | 0 | improved |
| P2 canonical_archetype_candidate_profile | C21 | Promote only explicit return + ROE/PBR bridge; block policy-only beta. | 4 | 19.37 | -10.26 | 38.07 | -10.26 | 0.00 | 0 | 0 | best_alignment |
| P3 counterexample_guard_profile | C21 guard | Add no-company-specific-return and high-MAE-after-event guard. | 4 | 19.37 | -10.26 | 38.07 | -10.26 | 0.00 | 0 | 0 | best_guard |


## 20. Score-Return Alignment Matrix

| case | before label | after label | MFE90 | MAE90 | alignment |
|---|---|---|---:|---:|---|
| KB | Stage3-Yellow | Stage3-Green | 23.37 | -11.69 | improved; strong rerating captured |
| Hana | Stage3-Yellow | Stage3-Yellow | 15.37 | -8.83 | kept; moderate positive |
| Shinhan | Stage3-Yellow | Stage2-Actionable | 6.43 | -18.29 | improved; avoids overpromotion |
| KakaoBank | Stage2-Watch | NarrativeOnly/BlockedPositive | 3.72 | -32.15 | improved; blocks policy-only false positive |

## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive_case_count | counterexample_count | 4B_case_count | 4C_case_count | new_independent_case_count | reused_case_count | calibration_usable_trigger_count | representative_trigger_count | current_profile_error_count | sector_rule_candidate | canonical_rule_candidate | coverage_gap_after_this_loop |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| L6_FINANCIAL_CAPITAL_RETURN_DIGITAL | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | BANK_CAPITAL_RETURN_QUALITY / POLICY_ONLY_GUARD | 2 | 2 | 1 | 2 watch labels | 4 | 0 | 5 | 4 | 2 | false | true | Still needs insurer/holding-company holdout and non-bank digital-finance examples. |


## 22. Residual Contribution Summary

```text
new_independent_case_count: 4
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 4
same_archetype_new_symbol_count: 4
same_archetype_new_trigger_family_count: 4
new_canonical_archetype_count: 1
new_fine_archetype_count: 4
new_trigger_family_count: 4

tested_existing_calibrated_axes:
- stage2_actionable_evidence_bonus
- stage3_yellow_total_min
- stage3_green_total_min
- price_only_blowoff_blocks_positive_stage
- full_4b_requires_non_price_evidence
- hard_4c_thesis_break_routes_to_4c

residual_error_types_found:
- policy_only_valueup_false_positive
- capital_return_scale_high_MAE_false_positive
- price_only_local_4B_too_early

new_axis_proposed:
- c21_confirmed_capital_return_quality_bonus
- c21_no_company_specific_return_guard
- c21_high_MAE_after_return_event_guard

existing_axis_strengthened:
- price_only_blowoff_blocks_positive_stage within C21
- full_4b_requires_non_price_evidence within C21

existing_axis_weakened: null
existing_axis_kept:
- hard_4c_thesis_break_routes_to_4c

sector_specific_rule_candidate: false
canonical_archetype_rule_candidate: true
no_new_signal_reason: null

loop_contribution_label: canonical_archetype_rule_candidate
do_not_propose_new_weight_delta: false
auto_selected_coverage_gap: R6/L6/C21 positive/counterexample balance
```

## 23. Validation Scope / Non-Validation Scope

Validated:

```text
- Stock-Web manifest and schema fields.
- Four clean symbol profiles.
- Representative trigger entry rows.
- 30D/90D/180D MFE/MAE from stock-web OHLC rows.
- Corporate-action contamination status from profiles.
- Positive/counterexample balance.
- C21-specific shadow rule candidate.
```

Not validated:

```text
- Production scoring code.
- Live candidates.
- Broker/trading integration.
- Exact production feature weights.
- Whether company disclosure timestamps were intraday or post-close. Entry dates conservatively use next-trading-day where needed.
```

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,c21_confirmed_capital_return_quality_bonus,canonical_archetype_specific,L6_FINANCIAL_CAPITAL_RETURN_DIGITAL,C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN,0,+2,+2,"explicit buyback/cancellation or distribution quality separates KB/Hana from policy-only beta","improves promotion of KB/Hana without promoting KakaoBank","TRG_R6L15_KB_20240208_STAGE2A|TRG_R6L15_HANA_20240208_STAGE2A",4,4,2,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,c21_no_company_specific_return_guard,canonical_archetype_specific,L6_FINANCIAL_CAPITAL_RETURN_DIGITAL,C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN,0,-4,-4,"policy-only Value-Up or low-PBR narrative should not promote Stage2/3","blocks KakaoBank-like false positive","TRG_R6L15_KAKAOBANK_20240227_STAGE2_POLICY_ONLY",4,4,2,medium,canonical_shadow_only,"not production; guard condition"
shadow_weight,c21_high_MAE_after_return_event_guard,canonical_archetype_specific,L6_FINANCIAL_CAPITAL_RETURN_DIGITAL,C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN,0,-2,-2,"real return evidence but poor post-event absorption/high MAE should cap Green","prevents Shinhan-like overpromotion","TRG_R6L15_SHINHAN_20240729_STAGE2A",4,4,2,low_to_medium,canonical_shadow_only,"requires more holdout cases"
shadow_weight,price_only_local_4B_too_early_guard,canonical_archetype_specific,L6_FINANCIAL_CAPITAL_RETURN_DIGITAL,C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN,existing_guard,kept,0,"KB 2024-10 local peak was not the full observed cycle peak","keeps full_4b_requires_non_price_evidence intact","TRG_R6L15_KB_20241025_4B_LOCAL_OVERLAY",1,1,0,medium,axis_stress_test,"strengthens existing 4B guard"
```

## 25. Machine-Readable Rows

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration"}
{"row_type": "case", "case_id": "R6L15_C21_KB_20240208_CAPITAL_RETURN_QUALITY", "symbol": "105560", "company_name": "KB금융", "round": "R6", "loop": "15", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "fine_archetype_id": "BANK_CAPITAL_RETURN_CET1_BUYBACK_CANCEL", "case_type": "structural_success", "positive_or_counterexample": "positive", "best_trigger": "TRG_R6L15_KB_20240208_STAGE2A", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "positive_rerating_with_manageable_MAE_after_initial_whipsaw", "current_profile_verdict": "current_profile_correct", "price_source": "Songdaiki/stock-web", "notes": "Clean profile: no corporate-action candidates in profile; 180D max high 103,900 on 2024-10-25 versus entry close 67,600."}
{"row_type": "case", "case_id": "R6L15_C21_HANA_20240208_CAPITAL_RETURN_QUALITY", "symbol": "086790", "company_name": "하나금융지주", "round": "R6", "loop": "15", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "fine_archetype_id": "BANK_VALUEUP_CAPITAL_RETURN_POSITIVE", "case_type": "stage2_promote_candidate", "positive_or_counterexample": "positive", "best_trigger": "TRG_R6L15_HANA_20240208_STAGE2A", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "moderate_positive_rerating", "current_profile_verdict": "current_profile_correct", "price_source": "Songdaiki/stock-web", "notes": "Clean profile: no corporate-action candidates; 180D route shows moderate but real MFE without the same depth of initial drawdown as Shinhan/KakaoBank."}
{"row_type": "case", "case_id": "R6L15_C21_SHINHAN_20240729_RETURN_SCALE_MAE_GUARD", "symbol": "055550", "company_name": "신한지주", "round": "R6", "loop": "15", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "fine_archetype_id": "BANK_CAPITAL_RETURN_SCALE_HIGH_MAE_COUNTEREXAMPLE", "case_type": "high_mae_success", "positive_or_counterexample": "counterexample", "best_trigger": "TRG_R6L15_SHINHAN_20240729_STAGE2A", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "return_evidence_real_but_entry_quality_poor_high_MAE", "current_profile_verdict": "current_profile_false_positive", "price_source": "Songdaiki/stock-web", "notes": "Clean profile: no corporate-action candidates. This is not a policy-only false positive; it is a quality/scale false positive."}
{"row_type": "case", "case_id": "R6L15_C21_KAKAOBANK_20240227_POLICY_ONLY_FALSE_POSITIVE", "symbol": "323410", "company_name": "카카오뱅크", "round": "R6", "loop": "15", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "fine_archetype_id": "BANK_VALUEUP_POLICY_ONLY_NO_CAPITAL_RETURN_GUARD", "case_type": "failed_rerating", "positive_or_counterexample": "counterexample", "best_trigger": "TRG_R6L15_KAKAOBANK_20240227_STAGE2_POLICY_ONLY", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "policy_only_low_pbr_false_positive", "current_profile_verdict": "current_profile_false_positive", "price_source": "Songdaiki/stock-web", "notes": "Clean profile: no corporate-action candidates. MFE was almost entirely entry-day noise; persistent downside dominated."}
{"row_type": "trigger", "trigger_id": "TRG_R6L15_KB_20240208_STAGE2A", "case_id": "R6L15_C21_KB_20240208_CAPITAL_RETURN_QUALITY", "symbol": "105560", "company_name": "KB금융", "round": "R6", "loop": "15", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "fine_archetype_id": "BANK_CAPITAL_RETURN_CET1_BUYBACK_CANCEL", "sector": "financials", "primary_archetype": "ROE/PBR/capital-return rerating", "loop_objective": "sector_specific_rule_discovery|counterexample_mining|coverage_gap_fill", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-02-07", "evidence_available_at_that_date": "FY2023 earnings/shareholder-return disclosure family: explicit buyback/cancellation and quarterly distribution framework; sector Value-Up tailwind was present, but the usable evidence is company-specific capital return quality.", "evidence_source": "company earnings/shareholder-return disclosure family; public Value-Up context cross-check; stock-web OHLC rows 2024-02-08 through 2025-07-29", "stage2_evidence_fields": ["public_event_or_disclosure", "policy_or_regulatory_optionality", "early_revision_signal"], "stage3_evidence_fields": ["financial_visibility", "confirmed_revision", "low_red_team_risk"], "stage4b_evidence_fields": [], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/105/105560/2024.csv", "profile_path": "atlas/symbol_profiles/105/105560.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-02-08", "entry_price": 67600, "MFE_30D_pct": 16.27, "MFE_90D_pct": 23.37, "MFE_180D_pct": 53.7, "MFE_1Y_pct": 53.7, "MFE_2Y_pct": null, "MAE_30D_pct": -11.69, "MAE_90D_pct": -11.69, "MAE_180D_pct": -11.69, "MAE_1Y_pct": -11.69, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-10-25", "peak_price": 103900, "drawdown_after_peak_pct": -21.46, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "not_applicable", "four_b_evidence_type": [], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "positive_rerating_with_manageable_MAE_after_initial_whipsaw", "current_profile_verdict": "current_profile_correct", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R6L15_C21_KB_20240208_CAPITAL_RETURN_QUALITY__2024-02-08", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "TRG_R6L15_HANA_20240208_STAGE2A", "case_id": "R6L15_C21_HANA_20240208_CAPITAL_RETURN_QUALITY", "symbol": "086790", "company_name": "하나금융지주", "round": "R6", "loop": "15", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "fine_archetype_id": "BANK_VALUEUP_CAPITAL_RETURN_POSITIVE", "sector": "financials", "primary_archetype": "ROE/PBR/capital-return rerating", "loop_objective": "sector_specific_rule_discovery|counterexample_mining|coverage_gap_fill", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-02-07", "evidence_available_at_that_date": "FY2023 bank-capital-return/value-up trigger family: explicit shareholder return and ROE/PBR repricing route. Evidence is less explosive than KB but still company-specific, not merely sector-policy beta.", "evidence_source": "company earnings/shareholder-return disclosure family; public Value-Up context cross-check; stock-web OHLC rows 2024-02-08 through 2024-12-30", "stage2_evidence_fields": ["public_event_or_disclosure", "policy_or_regulatory_optionality", "early_revision_signal"], "stage3_evidence_fields": ["financial_visibility", "low_red_team_risk"], "stage4b_evidence_fields": [], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/086/086790/2024.csv", "profile_path": "atlas/symbol_profiles/086/086790.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-02-08", "entry_price": 56600, "MFE_30D_pct": 15.19, "MFE_90D_pct": 15.37, "MFE_180D_pct": 22.44, "MFE_1Y_pct": 22.44, "MFE_2Y_pct": null, "MAE_30D_pct": -6.71, "MAE_90D_pct": -8.83, "MAE_180D_pct": -8.83, "MAE_1Y_pct": -8.83, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-08-27", "peak_price": 69300, "drawdown_after_peak_pct": -18.47, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "not_applicable", "four_b_evidence_type": [], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "moderate_positive_rerating", "current_profile_verdict": "current_profile_correct", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R6L15_C21_HANA_20240208_CAPITAL_RETURN_QUALITY__2024-02-08", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "TRG_R6L15_SHINHAN_20240729_STAGE2A", "case_id": "R6L15_C21_SHINHAN_20240729_RETURN_SCALE_MAE_GUARD", "symbol": "055550", "company_name": "신한지주", "round": "R6", "loop": "15", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "fine_archetype_id": "BANK_CAPITAL_RETURN_SCALE_HIGH_MAE_COUNTEREXAMPLE", "sector": "financials", "primary_archetype": "ROE/PBR/capital-return rerating", "loop_objective": "sector_specific_rule_discovery|counterexample_mining|coverage_gap_fill", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-07-26", "evidence_available_at_that_date": "2Q/FY capital-return announcement family was real, but the return scale and follow-through were insufficient to protect the entry from a deep drawdown. This is a guard case: company-specific return evidence exists, but it should not auto-Green without quality/scale and post-event absorption.", "evidence_source": "company 2024 earnings/shareholder-return disclosure family; stock-web OHLC rows 2024-07-29 through 2025-05-23", "stage2_evidence_fields": ["public_event_or_disclosure", "early_revision_signal"], "stage3_evidence_fields": ["financial_visibility"], "stage4b_evidence_fields": ["margin_or_backlog_slowdown", "positioning_overheat"], "stage4c_evidence_fields": ["thesis_evidence_broken"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/055/055550/2024.csv", "profile_path": "atlas/symbol_profiles/055/055550.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-07-29", "entry_price": 60700, "MFE_30D_pct": 6.43, "MFE_90D_pct": 6.43, "MFE_180D_pct": 6.43, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -14.99, "MAE_90D_pct": -18.29, "MAE_180D_pct": -29.98, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-08-26", "peak_price": 64600, "drawdown_after_peak_pct": -34.21, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "not_applicable", "four_b_evidence_type": [], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "return_evidence_real_but_entry_quality_poor_high_MAE", "current_profile_verdict": "current_profile_false_positive", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R6L15_C21_SHINHAN_20240729_RETURN_SCALE_MAE_GUARD__2024-07-29", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "TRG_R6L15_KAKAOBANK_20240227_STAGE2_POLICY_ONLY", "case_id": "R6L15_C21_KAKAOBANK_20240227_POLICY_ONLY_FALSE_POSITIVE", "symbol": "323410", "company_name": "카카오뱅크", "round": "R6", "loop": "15", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "fine_archetype_id": "BANK_VALUEUP_POLICY_ONLY_NO_CAPITAL_RETURN_GUARD", "sector": "financials", "primary_archetype": "ROE/PBR/capital-return rerating", "loop_objective": "sector_specific_rule_discovery|counterexample_mining|coverage_gap_fill", "trigger_type": "Stage2-Watch", "trigger_date": "2024-02-26", "evidence_available_at_that_date": "Corporate Value-Up policy beta and financial-sector low-PBR narrative existed, but no strong company-specific capital return/ROE improvement evidence was available at the trigger. Treating policy-only low-PBR beta as C21 positive evidence produces a false promotion.", "evidence_source": "public Corporate Value-Up policy context; stock-web OHLC rows 2024-02-27 through 2024-12-30", "stage2_evidence_fields": ["policy_or_regulatory_optionality"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["price_only_local_peak"], "stage4c_evidence_fields": ["thesis_evidence_broken"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/323/323410/2024.csv", "profile_path": "atlas/symbol_profiles/323/323410.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-02-27", "entry_price": 29550, "MFE_30D_pct": 3.72, "MFE_90D_pct": 3.72, "MFE_180D_pct": 3.72, "MFE_1Y_pct": 3.72, "MFE_2Y_pct": null, "MAE_30D_pct": -16.07, "MAE_90D_pct": -32.15, "MAE_180D_pct": -37.43, "MAE_1Y_pct": -37.43, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-02-27", "peak_price": 30650, "drawdown_after_peak_pct": -39.67, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "not_applicable", "four_b_evidence_type": [], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "policy_only_low_pbr_false_positive", "current_profile_verdict": "current_profile_false_positive", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R6L15_C21_KAKAOBANK_20240227_POLICY_ONLY_FALSE_POSITIVE__2024-02-27", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "TRG_R6L15_KB_20241025_4B_LOCAL_OVERLAY", "case_id": "R6L15_C21_KB_20240208_CAPITAL_RETURN_QUALITY", "symbol": "105560", "company_name": "KB금융", "round": "R6", "loop": "15", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "fine_archetype_id": "BANK_VALUEUP_LOCAL_4B_TOO_EARLY", "sector": "financials", "primary_archetype": "ROE/PBR/capital-return rerating", "loop_objective": "4B_non_price_requirement_stress_test", "trigger_type": "Stage4B-Overlay", "trigger_date": "2024-10-25", "entry_date": "2024-10-25", "entry_price": 101000, "evidence_available_at_that_date": "Local price/valuation overheat after the first bank Value-Up rerating leg. It looked like a local peak, but stock-web later shows the full observed cycle made a higher high in 2025; therefore price-only local 4B would have been too early.", "evidence_source": "stock-web OHLC rows 2024-10-25 through 2025-07-29; no binding non-price thesis break at trigger.", "stage2_evidence_fields": [], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["valuation_blowoff", "positioning_overheat", "price_only_local_peak"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/105/105560/2024.csv|atlas/ohlcv_tradable_by_symbol_year/105/105560/2025.csv", "profile_path": "atlas/symbol_profiles/105/105560.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 2.87, "MFE_90D_pct": 2.87, "MFE_180D_pct": 20.79, "MFE_1Y_pct": 25.35, "MFE_2Y_pct": null, "MAE_30D_pct": -15.05, "MAE_90D_pct": -24.36, "MAE_180D_pct": -31.39, "MAE_1Y_pct": -31.39, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2025-07-25", "peak_price": 126600, "drawdown_after_peak_pct": -45.26, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.92, "four_b_full_window_peak_proximity": 0.57, "four_b_timing_verdict": "price_only_local_4B_too_early", "four_b_evidence_type": ["price_only", "valuation_blowoff", "positioning_overheat"], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "local_4B_too_early_full_window_continued", "current_profile_verdict": "current_profile_4B_too_early", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R6L15_C21_KB_20240208_CAPITAL_RETURN_QUALITY__2024-10-25", "dedupe_for_aggregate": false, "aggregate_group_role": "4B_overlay_only", "is_new_independent_case": false, "reuse_reason": "same_symbol_different_trigger_family_4B_timing_audit", "independent_evidence_weight": 0.25, "do_not_count_as_new_case": true}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R6L15_C21_KB_20240208_CAPITAL_RETURN_QUALITY", "trigger_id": "TRG_R6L15_KB_20240208_STAGE2A", "symbol": "105560", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 6, "relative_strength_score": 8, "customer_quality_score": 0, "policy_or_regulatory_score": 6, "valuation_repricing_score": 7, "execution_risk_score": 0, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "roe_pbr_capital_return_score": 8, "capital_return_quality_score": 7, "policy_only_beta_score": 0, "post_event_absorption_score": 5}, "weighted_score_before": 82, "stage_label_before": "Stage3-Yellow", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 7, "relative_strength_score": 8, "customer_quality_score": 0, "policy_or_regulatory_score": 6, "valuation_repricing_score": 8, "execution_risk_score": 0, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "roe_pbr_capital_return_score": 9, "capital_return_quality_score": 9, "policy_only_beta_score": 0, "post_event_absorption_score": 6}, "weighted_score_after": 88, "stage_label_after": "Stage3-Green", "changed_components": ["capital_return_quality_score", "+confirmed_cancel_or_buyback_quality_bonus", "+post_event_absorption_score"], "component_delta_explanation": "Confirmed capital-return quality and market absorption justify C21 Green; the move was not policy-only.", "MFE_90D_pct": 23.37, "MAE_90D_pct": -11.69, "score_return_alignment_label": "positive_rerating_with_manageable_MAE_after_initial_whipsaw", "current_profile_verdict": "current_profile_correct"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R6L15_C21_HANA_20240208_CAPITAL_RETURN_QUALITY", "trigger_id": "TRG_R6L15_HANA_20240208_STAGE2A", "symbol": "086790", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 5, "relative_strength_score": 7, "customer_quality_score": 0, "policy_or_regulatory_score": 6, "valuation_repricing_score": 6, "execution_risk_score": 0, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "roe_pbr_capital_return_score": 7, "capital_return_quality_score": 6, "policy_only_beta_score": 0, "post_event_absorption_score": 5}, "weighted_score_before": 78, "stage_label_before": "Stage3-Yellow", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 5, "relative_strength_score": 7, "customer_quality_score": 0, "policy_or_regulatory_score": 6, "valuation_repricing_score": 7, "execution_risk_score": 0, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "roe_pbr_capital_return_score": 8, "capital_return_quality_score": 7, "policy_only_beta_score": 0, "post_event_absorption_score": 5}, "weighted_score_after": 82, "stage_label_after": "Stage3-Yellow", "changed_components": ["capital_return_quality_score", "+company_specific_return_bonus"], "component_delta_explanation": "Moderate positive. Enough for Stage2/Yellow, not enough for aggressive Green without stronger revision/ROE evidence.", "MFE_90D_pct": 15.37, "MAE_90D_pct": -8.83, "score_return_alignment_label": "moderate_positive_rerating", "current_profile_verdict": "current_profile_correct"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R6L15_C21_SHINHAN_20240729_RETURN_SCALE_MAE_GUARD", "trigger_id": "TRG_R6L15_SHINHAN_20240729_STAGE2A", "symbol": "055550", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 4, "relative_strength_score": 7, "customer_quality_score": 0, "policy_or_regulatory_score": 6, "valuation_repricing_score": 6, "execution_risk_score": 5, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "roe_pbr_capital_return_score": 7, "capital_return_quality_score": 6, "policy_only_beta_score": 0, "post_event_absorption_score": 2}, "weighted_score_before": 77, "stage_label_before": "Stage3-Yellow", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 4, "relative_strength_score": 5, "customer_quality_score": 0, "policy_or_regulatory_score": 6, "valuation_repricing_score": 5, "execution_risk_score": 7, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "roe_pbr_capital_return_score": 6, "capital_return_quality_score": 4, "policy_only_beta_score": 0, "post_event_absorption_score": 1}, "weighted_score_after": 71, "stage_label_after": "Stage2-Actionable", "changed_components": ["-capital_return_quality_score", "-post_event_absorption_score", "+high_MAE_guard"], "component_delta_explanation": "Real return evidence existed, but high MAE and weak absorption argue against automatic Yellow/Green promotion.", "MFE_90D_pct": 6.43, "MAE_90D_pct": -18.29, "score_return_alignment_label": "return_evidence_real_but_entry_quality_poor_high_MAE", "current_profile_verdict": "current_profile_false_positive"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R6L15_C21_KAKAOBANK_20240227_POLICY_ONLY_FALSE_POSITIVE", "trigger_id": "TRG_R6L15_KAKAOBANK_20240227_STAGE2_POLICY_ONLY", "symbol": "323410", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 0, "customer_quality_score": 0, "policy_or_regulatory_score": 7, "valuation_repricing_score": 5, "execution_risk_score": 4, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "roe_pbr_capital_return_score": 3, "capital_return_quality_score": 0, "policy_only_beta_score": 8, "post_event_absorption_score": 0}, "weighted_score_before": 64, "stage_label_before": "Stage2-Watch", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 0, "customer_quality_score": 0, "policy_or_regulatory_score": 5, "valuation_repricing_score": 3, "execution_risk_score": 7, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "roe_pbr_capital_return_score": 1, "capital_return_quality_score": 0, "policy_only_beta_score": 2, "post_event_absorption_score": 0}, "weighted_score_after": 54, "stage_label_after": "NarrativeOnly/BlockedPositive", "changed_components": ["-policy_only_beta_score", "-roe_pbr_capital_return_score", "+no_company_specific_return_guard"], "component_delta_explanation": "Policy-only low-PBR beta should not count as C21 positive evidence without company-specific return and ROE bridge.", "MFE_90D_pct": 3.72, "MAE_90D_pct": -32.15, "score_return_alignment_label": "policy_only_low_pbr_false_positive", "current_profile_verdict": "current_profile_false_positive"}
{"row_type": "residual_contribution", "round": "R6", "loop": "15", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "new_independent_case_count": 4, "reused_case_count": 0, "new_symbol_count": 4, "same_archetype_new_symbol_count": 4, "same_archetype_new_trigger_family_count": 4, "new_canonical_archetype_count": 1, "new_trigger_family_count": 4, "positive_case_count": 2, "counterexample_count": 2, "current_profile_error_count": 2, "tested_existing_calibrated_axes": ["stage2_actionable_evidence_bonus", "stage3_yellow_total_min", "stage3_green_total_min", "price_only_blowoff_blocks_positive_stage", "full_4b_requires_non_price_evidence", "hard_4c_thesis_break_routes_to_4c"], "residual_error_types_found": ["policy_only_valueup_false_positive", "capital_return_scale_high_MAE_false_positive", "price_only_local_4B_too_early"], "loop_contribution_label": "canonical_archetype_rule_candidate", "do_not_propose_new_weight_delta": false, "auto_selected_coverage_gap": "R6/L6/C21 lacked positive+counterexample balance for capital-return quality versus policy-only beta"}
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
next_round_candidate_1 = R7 / L7 / C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION
next_round_candidate_2 = R8 / L8 / C28_SOFTWARE_SECURITY_CONTRACT_RETENTION
next_round_candidate_3 = R5 / L5 / C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION
```

## 28. Source Notes

Stock-Web source files validated in session:

```text
atlas/manifest.json
atlas/schema.json
atlas/symbol_profiles/105/105560.json
atlas/symbol_profiles/086/086790.json
atlas/symbol_profiles/055/055550.json
atlas/symbol_profiles/323/323410.json
atlas/ohlcv_tradable_by_symbol_year/105/105560/2024.csv
atlas/ohlcv_tradable_by_symbol_year/105/105560/2025.csv
atlas/ohlcv_tradable_by_symbol_year/086/086790/2024.csv
atlas/ohlcv_tradable_by_symbol_year/055/055550/2024.csv
atlas/ohlcv_tradable_by_symbol_year/055/055550/2025.csv
atlas/ohlcv_tradable_by_symbol_year/323/323410/2024.csv
```

External policy context:

```text
Corporate Value-Up Programme policy context was used only as background. C21 promotion is explicitly tied to company-specific capital-return evidence.
```
