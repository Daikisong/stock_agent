# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
research_session = post_calibrated_sector_archetype_residual_research
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
output_file = e2r_stock_web_v12_residual_round_R6_loop_14_L6_FINANCIAL_CAPITAL_RETURN_DIGITAL_C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN_research.md
scheduled_round = R6
scheduled_loop = 14
completed_round = R6
completed_loop = 14
next_round = R7
next_loop = 14
round_schedule_status = valid
round_sector_consistency = pass

large_sector_id = L6_FINANCIAL_CAPITAL_RETURN_DIGITAL
canonical_archetype_id = C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN
fine_archetype_id = BANK_HOLDCO_ROE_PBR_CAPITAL_RETURN_VALUEUP_VS_DIGITAL_BANK_PRICE_BETA

current_stock_discovery_allowed = false
stock_agent_code_access_allowed = false
stock_agent_code_patch_allowed = false
production_scoring_changed = false
shadow_weight_only = true
stock_web_price_atlas_access_required = true
```

This loop adds **5** new independent cases, **2** counterexamples, and **3** residual errors for **R6/L6_FINANCIAL_CAPITAL_RETURN_DIGITAL/C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN**.

## 1. Current Calibrated Profile Assumption

```text
current_default_profile_proxy = e2r_2_1_stock_web_calibrated_proxy
previous_baseline_reference = e2r_2_0_baseline_reference

stage2_actionable_evidence_bonus = +2.0
stage3_yellow_total_min = 75.0
stage3_green_total_min = 87.0
stage3_green_revision_min = 55.0
stage3_cross_evidence_green_buffer = +1.5
price_only_blowoff_blocks_positive_stage = true
full_4b_requires_non_price_evidence = true
hard_4c_thesis_break_routes_to_4c = true
```

The test here does not re-prove the global profile. The residual question is narrower: in financials, a low-PBR/value-up price move should only become a positive C21 signal when it is tied to board-confirmed capital return, ROE visibility, and capital-buffer evidence. Digital-bank beta and regional-bank price-only themes can look like the same animal on the chart, but they are different engines under the hood.

## 2. Round / Large Sector / Canonical Archetype Scope

```text
round = R6
large_sector_id = L6_FINANCIAL_CAPITAL_RETURN_DIGITAL
canonical_archetype_id = C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN
loop_objective = coverage_gap_fill | counterexample_mining | residual_false_positive_mining | sector_specific_rule_discovery | canonical_archetype_compression | 4B_non_price_requirement_stress_test | 4C_thesis_break_timing_test
```

R6 maps to financial capital return and digital finance. This file therefore uses C21 rather than C22. Insurance reserve/rate-cycle cases are intentionally left for a later R6/C22 file.

## 3. Previous Coverage / Duplicate Avoidance Check

Allowed research-artifact access was restricted to calibration registry / representative trigger rows. The registry visible in `data/e2r/calibration/md_registry.jsonl` contains older `e2r_stock_web_historical_calibration_round_R6_loop_*` files, but not this v12 residual filename. The immediate prior v12 chat artifact ended at R5 / Loop 14 and declared next_round=R6 / next_loop=14; this MD follows that local v12 state.

No case below reuses the prior R5 C20 consumer/beauty symbols. All five symbols are new within this v12 handoff sequence.

## 4. Stock-Web OHLC Input / Price Source Validation

```json
{
  "row_type": "price_source_validation",
  "source": "Songdaiki/stock-web",
  "source_url": "https://github.com/Songdaiki/stock-web",
  "manifest_path": "atlas/manifest.json",
  "schema_path": "atlas/schema.json",
  "universe_path": "atlas/universe/all_symbols.csv",
  "manifest_max_date": "2026-02-20",
  "source_name": "FinanceData/marcap",
  "price_basis": "tradable_raw",
  "price_adjustment_status": "raw_unadjusted_marcap",
  "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year",
  "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year",
  "validation_status": "usable_for_historical_calibration"
}
```

## 5. Historical Eligibility Gate

All representative trigger rows satisfy:

```text
trigger_date is historical
entry_date exists in stock-web tradable shard
entry_date -> D+180 window available before manifest max_date = 2026-02-20
high / low / close / volume present
MFE_30D / 90D / 180D and MAE_30D / 90D / 180D calculated
corporate_action_window_status = clean_180D_window
```

The primary calibration windows are 30D / 90D / 180D. 1Y and 2Y fields are included as secondary context and should not override the 180D calibration decision.

## 6. Canonical Archetype Compression Map

| Fine archetype | Canonical mapping | Compression decision |
|---|---|---|
| BROKERAGE_INSURANCE_HOLDCO_TOTAL_SHAREHOLDER_RETURN | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | keep under C21; do not split into brokerage-only rule yet |
| MEGABANK_VALUEUP_BUYBACK_CANCEL_ROE_BUFFER | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | core positive C21 archetype |
| MEGABANK_VALUEUP_DIVIDEND_BUYBACK_ROE_BUFFER | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | core positive C21 archetype |
| DIGITAL_BANK_GROWTH_BETA_WITHOUT_CAPITAL_RETURN | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | counterexample guard inside C21 |
| REGIONAL_BANK_PRICE_ONLY_RUMOR_THEME | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | price-only counterexample / 4B guard only |

## 7. Case Selection Summary

| case_id | symbol | company | role | trigger_type | entry_date | entry_price | MFE_90D | MAE_90D | current_profile_verdict |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| R6L14_C21_MERITZ_CAPRETURN_2024 | 138040 | 메리츠금융지주 | positive | Stage2-Actionable | 2024-02-01 | 70000 | 26.14 | -4.14 | current_profile_too_late |
| R6L14_C21_KB_VALUEUP_CAPRETURN_2024 | 105560 | KB금융 | positive | Stage2-Actionable | 2024-02-08 | 67600 | 23.37 | -11.69 | current_profile_too_late |
| R6L14_C21_HANA_CAPRETURN_VALUEUP_2024 | 086790 | 하나금융지주 | positive | Stage2-Actionable | 2024-02-01 | 52000 | 25.58 | -7.88 | current_profile_correct |
| R6L14_C21_KAKAOBANK_DIGITAL_BETA_2024 | 323410 | 카카오뱅크 | counterexample | Stage2-Actionable | 2024-02-08 | 29100 | 7.22 | -27.84 | current_profile_false_positive |
| R6L14_C21_JEJUBANK_PRICEONLY_2023 | 006220 | 제주은행 | counterexample | Stage2-Actionable | 2023-01-17 | 13550 | 87.45 | -17.2 | current_profile_correct |


## 8. Positive vs Counterexample Balance

```text
positive_case_count = 3
counterexample_count = 2
4B_case_count = 2
4C_case_count = 1
calibration_usable_case_count = 5
new_independent_case_count = 5
reused_case_count = 0
```

The positive cases are 메리츠금융지주, KB금융, 하나금융지주. Their common thread is not merely low-PBR or a bank-sector price move; it is the coupling of ROE/PBR rerating with explicit capital-return mechanics. The counterexamples are 카카오뱅크 and 제주은행: one is digital-bank valuation beta without durable capital-return confirmation, the other is a regional-bank price-only theme that produced large MFE but failed as structural C21 evidence.

## 9. Evidence Source Map

| case_id | evidence family | evidence available at trigger | evidence-source handling |
|---|---|---|---|
| R6L14_C21_MERITZ_CAPRETURN_2024 | board-level capital return + ROE/PBR rerating | FY2023 result/shareholder-return continuation event label | DART/IR recheck required before production ledger |
| R6L14_C21_KB_VALUEUP_CAPRETURN_2024 | value-up + buyback/cancel/dividend signal | FY2023 result/shareholder-return package event label | DART/IR recheck required before production ledger |
| R6L14_C21_HANA_CAPRETURN_VALUEUP_2024 | value-up + dividend/buyback signal | FY2023 result/shareholder-return event label | DART/IR recheck required before production ledger |
| R6L14_C21_KAKAOBANK_DIGITAL_BETA_2024 | digital-bank beta without durable capital return | growth/beta event label; no C21 capital-return proof | counterexample evidence; not a positive trigger |
| R6L14_C21_JEJUBANK_PRICEONLY_2023 | price-only regional-bank theme | relative-strength only; no ROE/PBR capital-return proof | counterexample evidence; 4B/4C guard only |

## 10. Price Data Source Map

| symbol | company | profile_path | price_shard_path | corporate action window |
|---|---|---|---|---|
| 138040 | 메리츠금융지주 | atlas/symbol_profiles/138/138040.json | atlas/ohlcv_tradable_by_symbol_year/138/138040/2024.csv | clean_180D_window |
| 105560 | KB금융 | atlas/symbol_profiles/105/105560.json | atlas/ohlcv_tradable_by_symbol_year/105/105560/2024.csv | clean_180D_window |
| 086790 | 하나금융지주 | atlas/symbol_profiles/086/086790.json | atlas/ohlcv_tradable_by_symbol_year/086/086790/2024.csv | clean_180D_window |
| 323410 | 카카오뱅크 | atlas/symbol_profiles/323/323410.json | atlas/ohlcv_tradable_by_symbol_year/323/323410/2024.csv | clean_180D_window |
| 006220 | 제주은행 | atlas/symbol_profiles/006/006220.json | atlas/ohlcv_tradable_by_symbol_year/006/006220/2023.csv | clean_180D_window |

## 11. Case-by-Case Trigger Grid

| trigger_id | symbol | type | trigger_date | entry_date | entry_price | MFE30 | MFE90 | MFE180 | MAE90 | peak_date | current_profile | aggregate_role |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| R6L14_T001_MERITZ_STAGE2_CAPRETURN | 138040 | Stage2-Actionable | 2024-01-31 | 2024-02-01 | 70000 | 26.14 | 26.14 | 37.86 | -4.14 | 2024-08-29 | current_profile_too_late | representative |
| R6L14_T002_KB_STAGE2_VALUEUP | 105560 | Stage2-Actionable | 2024-02-07 | 2024-02-08 | 67600 | 16.27 | 23.37 | 53.7 | -11.69 | 2024-10-25 | current_profile_too_late | representative |
| R6L14_T003_HANA_STAGE2_CAPRETURN | 086790 | Stage2-Actionable | 2024-01-31 | 2024-02-01 | 52000 | 24.23 | 25.58 | 33.27 | -7.88 | 2024-08-27 | current_profile_correct | representative |
| R6L14_T004_KAKAOBANK_FALSE_STAGE2 | 323410 | Stage2-Actionable | 2024-02-07 | 2024-02-08 | 29100 | 7.22 | 7.22 | 7.22 | -27.84 | 2024-02-15 | current_profile_false_positive | representative |
| R6L14_T005_JEJUBANK_PRICEONLY_STAGE2 | 006220 | Stage2-Actionable | 2023-01-17 | 2023-01-17 | 13550 | 81.55 | 87.45 | 87.45 | -17.2 | 2023-03-30 | current_profile_correct | representative |
| R6L14_T006_JEJUBANK_4B_PRICEONLY | 006220 | 4B | 2023-02-20 | 2023-02-20 | 23750 | 6.95 | 6.95 | 6.95 | -52.76 | 2023-03-30 | current_profile_correct | 4B_overlay_only |
| R6L14_T007_KAKAOBANK_4C_GOVERNANCE | 323410 | 4C | 2024-07-22 | 2024-07-22 | 21100 | 11.61 | 11.61 | 35.07 | -12.37 | 2024-07-23 | current_profile_4C_too_late | 4C_overlay_only |


## 12. Trigger-Level OHLC Backtest Tables

### Representative aggregate triggers

| case_id | entry | entry_price | MFE30 | MFE90 | MFE180 | MAE30 | MAE90 | MAE180 | peak | drawdown_after_peak |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| R6L14_C21_MERITZ_CAPRETURN_2024 | 2024-02-01 | 70000 | 26.14 | 26.14 | 37.86 | -4.14 | -4.14 | -4.14 | 2024-08-29 / 96500 | -14.2 |
| R6L14_C21_KB_VALUEUP_CAPRETURN_2024 | 2024-02-08 | 67600 | 16.27 | 23.37 | 53.7 | -11.69 | -11.69 | -11.69 | 2024-10-25 / 103900 | -15.5 |
| R6L14_C21_HANA_CAPRETURN_VALUEUP_2024 | 2024-02-01 | 52000 | 24.23 | 25.58 | 33.27 | -7.88 | -7.88 | -7.88 | 2024-08-27 / 69300 | -17.89 |
| R6L14_C21_KAKAOBANK_DIGITAL_BETA_2024 | 2024-02-08 | 29100 | 7.22 | 7.22 | 7.22 | -6.19 | -27.84 | -36.46 | 2024-02-15 / 31200 | -40.74 |
| R6L14_C21_JEJUBANK_PRICEONLY_2023 | 2023-01-17 | 13550 | 81.55 | 87.45 | 87.45 | -11.44 | -17.2 | -45.76 | 2023-03-30 / 25400 | -71.06 |


### Overlay-only 4B / 4C triggers

| trigger_id | entry | entry_price | MFE30 | MAE30 | MFE90 | MAE90 | label | dedupe |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| R6L14_T006_JEJUBANK_4B_PRICEONLY | 2023-02-20 | 23750 | 6.95 | -32.63 | 6.95 | -52.76 | 4B_overlay_success_for_price_only_blowoff | False |
| R6L14_T007_KAKAOBANK_4C_GOVERNANCE | 2024-07-22 | 21100 | 11.61 | -12.37 | 11.61 | -12.37 | 4C_success_after_legal_regulatory_thesis_break | False |


## 13. Current Calibrated Profile Stress Test

| Question | Finding |
|---|---|
| How would current calibrated profile treat the cases? | It would generally recognize the bank-holdco value-up theme, but can be too late on Meritz/KB if it waits for later revision confirmation; it may over-score KakaoBank when digital-beta/rebound is mistaken for C21 capital return. |
| Was that aligned with MFE/MAE? | Positive bank-holdco cases had strong 90D/180D MFE. KakaoBank had limited MFE and deep MAE; JejuBank had huge MFE but no structural evidence and severe post-peak drawdown. |
| Stage2 bonus too high or low? | For board-confirmed capital-return cases, Stage2 bonus is useful. For digital-bank beta and regional-bank price-only themes, it is too high unless C21 guard is applied. |
| Yellow threshold 75 too high or low? | Reasonable globally, but C21 requires a component cap: relative strength alone should not cross Yellow. |
| Green threshold/revision requirement too strict? | Too strict for explicit capital-return packages with clean ROE/PBR visibility; not too strict for digital-bank beta. |
| Price-only blowoff guard? | Strengthened. JejuBank proves high MFE alone is a trapdoor, not a structural bridge. |
| Full 4B non-price requirement? | Kept. Price-only local peak can mark danger but should not become full 4B without non-price deterioration. |
| Hard 4C routing? | Strengthened for governance/legal-regulatory thesis breaks in digital financials. |

## 14. Stage2 / Yellow / Green Comparison

The C21 residual is not “Stage2 is faster than Green.” The useful distinction is *what kind of Stage2*. Bank-holdco Stage2 backed by capital-return mechanics behaves like an early structural bridge. Digital-bank or regional-bank Stage2 backed only by beta, rumor, or relative strength behaves like a mirror: it reflects price, but it does not carry weight.

```text
avg_green_lateness_ratio_positive_cases = 0.37
green_lateness_verdict = Green is moderately late for board-confirmed capital-return cases.
counterexample_green_lateness_ratio = not_applicable; no confirmed Stage3-Green should exist.
```

## 15. 4B Local vs Full-window Timing Audit

```text
four_b_local_peak_proximity is separated from four_b_full_window_peak_proximity.
price-only local peak rows are overlay-only.
```

JejuBank shows why this matters. A price-only 4B overlay near the local/full peak was useful as a guardrail, but it was not a “sell signal on a real Stage3 thesis” because no real Stage3 thesis existed. KB/Hana show the other side: valuation/positioning heat near high proximity is a watch-only overlay until there is non-price evidence of revision slowdown, capital-return disappointment, legal block, or balance-sheet deterioration.

## 16. 4C Protection Audit

KakaoBank provides the cleanest 4C pattern in this batch. The representative false-positive trigger was 2024-02-08 at 29,100. The 4C overlay trigger was 2024-07-22 at 21,100 after governance/legal-regulatory thesis risk became explicit. The 4C did not save the whole decline from February, but it protected against a further leg into the August low.

```text
KakaoBank prior-stage peak = 31,200
KakaoBank 4C entry = 21,100
KakaoBank post-4C low used = 18,490
4C protection label = hard_4c_success
```

## 17. Sector-Specific Rule Candidate

```text
sector_specific_rule_candidate = false
reason = same large sector has enough cases, but all evidence compresses better into C21-specific rule rather than a broad L6 rule.
```

## 18. Canonical-Archetype Rule Candidate

```text
canonical_archetype_rule_candidate = true

C21_board_confirmed_capital_return_bonus:
  Apply only when shareholder-return mechanics are explicit and durable:
  - buyback/cancellation or dividend policy is board-confirmed,
  - ROE/PBR rerating has earnings or capital-buffer support,
  - capital return is not merely price-only value-up beta.

C21_digital_bank_beta_without_capreturn_penalty:
  Cap digital-bank growth/beta labels below Stage3-Yellow unless capital-return and ROE/PBR evidence are explicit.

C21_price_only_financial_theme_guard:
  Regional/low-float bank relative strength cannot promote Stage2/Stage3 without non-price capital-return evidence.
```

## 19. Before / After Backtest Comparison

| profile | scope | eligible | avg_MFE90 | avg_MAE90 | false_positive_rate | late_green_count | verdict |
| --- | --- | --- | --- | --- | --- | --- | --- |
| P0_e2r_2_1_stock_web_calibrated_proxy | current_proxy | 5 | 33.15 | -13.75 | 0.4 | 2 | mixed |
| P0b_e2r_2_0_baseline_reference | rollback_reference | 5 | 33.15 | -13.75 | 0.4 | 1 | weaker_than_P0 |
| P1_sector_specific_candidate_profile | sector_specific | 5 | 25.03 | -7.9 | 0.0 | 1 | improved |
| P2_canonical_archetype_candidate_profile | canonical_archetype_specific | 5 | 25.03 | -7.9 | 0.0 | 1 | best_candidate |
| P3_counterexample_guard_profile | counterexample_guard | 5 | 25.03 | -7.9 | 0.0 | 2 | safer_but_slightly_later |


## 20. Score-Return Alignment Matrix

| group | selected cases | score-return alignment |
|---|---|---|
| board-confirmed capital return | Meritz, KB, Hana | strong; avg 90D MFE about 25%, avg 90D MAE about -8% |
| digital-bank beta without capital return | KakaoBank | weak; 90D MFE 7.22%, 90D MAE -27.84% |
| regional bank price-only theme | JejuBank | misleading; huge MFE but no structural evidence and -71% post-peak drawdown |
| proposed C21 shadow profile | positive rows promoted, counterexamples blocked | improved alignment and lower false-positive rate |

## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive_case_count | counterexample_count | 4B_case_count | 4C_case_count | new_independent_case_count | reused_case_count | calibration_usable_trigger_count | representative_trigger_count | current_profile_error_count | sector_rule_candidate | canonical_rule_candidate | coverage_gap_after_this_loop |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| L6_FINANCIAL_CAPITAL_RETURN_DIGITAL | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | BANK_HOLDCO_ROE_PBR_CAPITAL_RETURN_VALUEUP_VS_DIGITAL_BANK_PRICE_BETA | 3 | 2 | 2 | 1 | 5 | 0 | 7 | 5 | 3 | False | True | C21 now has positive bank/holdco capital-return cases and two counterexamples for digital-beta/price-only bank themes. |


## 22. Residual Contribution Summary

```text
new_independent_case_count: 5
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 5
new_canonical_archetype_count: 0
new_fine_archetype_count: 5
new_trigger_family_count: 5

tested_existing_calibrated_axes:
  - stage2_actionable_evidence_bonus
  - stage3_green_revision_min
  - price_only_blowoff_blocks_positive_stage
  - full_4b_requires_non_price_evidence
  - hard_4c_thesis_break_routes_to_4c

residual_error_types_found:
  - digital_bank_beta_false_positive
  - capital_return_green_too_late
  - price_only_financial_theme_high_MFE_false_positive
  - 4C_governance_risk_late

new_axis_proposed:
  - C21_board_confirmed_capital_return_bonus
  - C21_digital_bank_beta_without_capreturn_penalty
  - C21_price_only_financial_theme_guard

existing_axis_strengthened:
  - price_only_blowoff_blocks_positive_stage
  - full_4b_requires_non_price_evidence
  - hard_4c_thesis_break_routes_to_4c

existing_axis_weakened: null
existing_axis_kept:
  - stage2_actionable_evidence_bonus
  - stage3_yellow_total_min
  - stage3_green_total_min
  - stage3_green_revision_min
  - stage3_cross_evidence_green_buffer

sector_specific_rule_candidate: false
canonical_archetype_rule_candidate: true
no_new_signal_reason: null

loop_contribution_label: canonical_archetype_rule_candidate
do_not_propose_new_weight_delta: false
```

## 23. Validation Scope / Non-Validation Scope

### Validation scope

- Stock-Web tradable OHLC rows.
- Entry date / entry close.
- 30D / 90D / 180D MFE and MAE.
- Corporate-action overlap gate.
- C21 score-return alignment under shadow-only profiles.
- Positive vs counterexample balance.

### Non-validation scope

- No live stock recommendation.
- No current candidate scan.
- No brokerage API.
- No stock_agent code access.
- No production scoring change.
- Event labels are historical research labels and should be rechecked against DART/IR packets before production evidence ingestion.

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,C21_board_confirmed_capital_return_bonus,canonical_archetype_specific,L6_FINANCIAL_CAPITAL_RETURN_DIGITAL,C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN,0,1,+1,Reward buyback/cancellation/dividend policy only when paired with ROE/PBR and capital-buffer evidence.,Promotes Meritz/KB earlier without allowing KakaoBank/Jeju price-only cases.,R6L14_T001_MERITZ_STAGE2_CAPRETURN|R6L14_T002_KB_STAGE2_VALUEUP|R6L14_T003_HANA_STAGE2_CAPRETURN,5,5,2,medium,canonical_shadow_only,not production; post-calibrated residual
shadow_weight,C21_digital_bank_beta_without_capreturn_penalty,canonical_archetype_specific,L6_FINANCIAL_CAPITAL_RETURN_DIGITAL,C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN,0,1,-1,Digital-bank growth/valuation beta without board-level capital return should not clear Stage3-Yellow/Green.,Removes KakaoBank false positive while preserving banks with explicit capital-return evidence.,R6L14_T004_KAKAOBANK_FALSE_STAGE2,5,5,2,medium,canonical_shadow_only,not production; post-calibrated residual
shadow_weight,C21_price_only_financial_theme_guard,canonical_archetype_specific,L6_FINANCIAL_CAPITAL_RETURN_DIGITAL,C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN,0,1,-1,Regional/low-float bank price-only themes can show extreme MFE but are not C21 structural signals.,"Keeps JejuBank as 4B/4C risk calibration, not positive Stage2/3 evidence.",R6L14_T005_JEJUBANK_PRICEONLY_STAGE2|R6L14_T006_JEJUBANK_4B_PRICEONLY,5,5,2,medium,canonical_shadow_only,not production; post-calibrated residual
```

## 25. Machine-Readable Rows

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "source_name": "FinanceData/marcap", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration"}
{"row_type": "case", "case_id": "R6L14_C21_MERITZ_CAPRETURN_2024", "symbol": "138040", "company_name": "메리츠금융지주", "round": "R6", "loop": "14", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "fine_archetype_id": "BROKERAGE_INSURANCE_HOLDCO_TOTAL_SHAREHOLDER_RETURN", "case_type": "structural_success", "positive_or_counterexample": "positive", "best_trigger": "R6L14_T001_MERITZ_STAGE2_CAPRETURN", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "aligned_after_capital_return_gate", "current_profile_verdict": "current_profile_too_late", "price_source": "Songdaiki/stock-web", "notes": "FY2023 result/shareholder-return continuation event label: group earnings visibility plus explicit buyback/cancellation/dividend-return path."}
{"row_type": "case", "case_id": "R6L14_C21_KB_VALUEUP_CAPRETURN_2024", "symbol": "105560", "company_name": "KB금융", "round": "R6", "loop": "14", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "fine_archetype_id": "MEGABANK_VALUEUP_BUYBACK_CANCEL_ROE_BUFFER", "case_type": "structural_success", "positive_or_counterexample": "positive", "best_trigger": "R6L14_T002_KB_STAGE2_VALUEUP", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "aligned_after_board_level_capital_return_boost", "current_profile_verdict": "current_profile_too_late", "price_source": "Songdaiki/stock-web", "notes": "FY2023 result/shareholder-return package plus Korea value-up rerating context; board-level capital return signal, not only low-PBR price momentum."}
{"row_type": "case", "case_id": "R6L14_C21_HANA_CAPRETURN_VALUEUP_2024", "symbol": "086790", "company_name": "하나금융지주", "round": "R6", "loop": "14", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "fine_archetype_id": "MEGABANK_VALUEUP_DIVIDEND_BUYBACK_ROE_BUFFER", "case_type": "high_mae_success", "positive_or_counterexample": "positive", "best_trigger": "R6L14_T003_HANA_STAGE2_CAPRETURN", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "aligned_but_green_not_required", "current_profile_verdict": "current_profile_correct", "price_source": "Songdaiki/stock-web", "notes": "FY2023 result/shareholder-return event label: low-PBR value-up context with explicit capital-return component and bank-holdco ROE visibility."}
{"row_type": "case", "case_id": "R6L14_C21_KAKAOBANK_DIGITAL_BETA_2024", "symbol": "323410", "company_name": "카카오뱅크", "round": "R6", "loop": "14", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "fine_archetype_id": "DIGITAL_BANK_GROWTH_BETA_WITHOUT_CAPITAL_RETURN", "case_type": "false_positive_green", "positive_or_counterexample": "counterexample", "best_trigger": "R6L14_T004_KAKAOBANK_FALSE_STAGE2", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "false_positive_removed_by_capital_return_gate", "current_profile_verdict": "current_profile_false_positive", "price_source": "Songdaiki/stock-web", "notes": "Growth/digital-bank beta and market rebound event label; no board-level capital return or durable ROE/PBR rerating proof at trigger date."}
{"row_type": "case", "case_id": "R6L14_C21_JEJUBANK_PRICEONLY_2023", "symbol": "006220", "company_name": "제주은행", "round": "R6", "loop": "14", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "fine_archetype_id": "REGIONAL_BANK_PRICE_ONLY_RUMOR_THEME", "case_type": "price_moved_without_evidence", "positive_or_counterexample": "counterexample", "best_trigger": "R6L14_T005_JEJUBANK_PRICEONLY_STAGE2", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "guard_prevents_price_only_false_positive", "current_profile_verdict": "current_profile_correct", "price_source": "Songdaiki/stock-web", "notes": "Price-only regional-bank/low-float financial theme. No verified capital-return, ROE/PBR, or shareholder-return evidence at trigger date."}
{"row_type": "trigger", "trigger_id": "R6L14_T001_MERITZ_STAGE2_CAPRETURN", "case_id": "R6L14_C21_MERITZ_CAPRETURN_2024", "symbol": "138040", "company_name": "메리츠금융지주", "round": "R6", "loop": "14", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "fine_archetype_id": "BROKERAGE_INSURANCE_HOLDCO_TOTAL_SHAREHOLDER_RETURN", "sector": "금융지주/증권·보험 복합", "primary_archetype": "financial_roe_pbr_capital_return", "loop_objective": "coverage_gap_fill|counterexample_mining|residual_false_positive_mining|sector_specific_rule_discovery|canonical_archetype_compression|4B_non_price_requirement_stress_test|4C_thesis_break_timing_test", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-01-31", "evidence_available_at_that_date": "FY2023 result/shareholder-return continuation event label: group earnings visibility plus explicit buyback/cancellation/dividend-return path.", "evidence_source": "Company IR/DART FY2023 result and shareholder-return disclosure label; stock-web row trace: 2024-02-01 close 70,000 in atlas/ohlcv_tradable_by_symbol_year/138/138040/2024.csv.", "stage2_evidence_fields": ["public_event_or_disclosure", "relative_strength", "early_revision_signal"], "stage3_evidence_fields": ["financial_visibility", "multiple_public_sources", "low_red_team_risk"], "stage4b_evidence_fields": [], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/138/138040/2024.csv", "profile_path": "atlas/symbol_profiles/138/138040.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-02-01", "entry_price": 70000, "MFE_30D_pct": 26.14, "MFE_90D_pct": 26.14, "MFE_180D_pct": 37.86, "MFE_1Y_pct": 83.57, "MFE_2Y_pct": 108.86, "MAE_30D_pct": -4.14, "MAE_90D_pct": -4.14, "MAE_180D_pct": -4.14, "MAE_1Y_pct": -4.14, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-08-29", "peak_price": 96500, "drawdown_after_peak_pct": -14.2, "green_lateness_ratio": 0.42, "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "not_applicable", "four_b_evidence_type": [], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "structural_rerating_confirmed_after_capital_return", "current_profile_verdict": "current_profile_too_late", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R6L14_G001_MERITZ_2024_0201", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "R6L14_T002_KB_STAGE2_VALUEUP", "case_id": "R6L14_C21_KB_VALUEUP_CAPRETURN_2024", "symbol": "105560", "company_name": "KB금융", "round": "R6", "loop": "14", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "fine_archetype_id": "MEGABANK_VALUEUP_BUYBACK_CANCEL_ROE_BUFFER", "sector": "은행지주", "primary_archetype": "financial_roe_pbr_capital_return", "loop_objective": "coverage_gap_fill|counterexample_mining|residual_false_positive_mining|sector_specific_rule_discovery|canonical_archetype_compression|4B_non_price_requirement_stress_test|4C_thesis_break_timing_test", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-02-07", "evidence_available_at_that_date": "FY2023 result/shareholder-return package plus Korea value-up rerating context; board-level capital return signal, not only low-PBR price momentum.", "evidence_source": "Company result/shareholder-return event label; stock-web row trace: 2024-02-08 close 67,600 in atlas/ohlcv_tradable_by_symbol_year/105/105560/2024.csv.", "stage2_evidence_fields": ["public_event_or_disclosure", "policy_or_regulatory_optionality", "relative_strength", "early_revision_signal"], "stage3_evidence_fields": ["financial_visibility", "repeat_order_or_conversion", "durable_customer_confirmation", "low_red_team_risk"], "stage4b_evidence_fields": ["valuation_blowoff"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/105/105560/2024.csv", "profile_path": "atlas/symbol_profiles/105/105560.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-02-08", "entry_price": 67600, "MFE_30D_pct": 16.27, "MFE_90D_pct": 23.37, "MFE_180D_pct": 53.7, "MFE_1Y_pct": 70.1, "MFE_2Y_pct": 159.0, "MAE_30D_pct": -11.69, "MAE_90D_pct": -11.69, "MAE_180D_pct": -11.69, "MAE_1Y_pct": -11.69, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-10-25", "peak_price": 103900, "drawdown_after_peak_pct": -15.5, "green_lateness_ratio": 0.33, "four_b_local_peak_proximity": 0.93, "four_b_full_window_peak_proximity": 0.93, "four_b_timing_verdict": "watch_only_valuation_blowoff_not_full_exit_without_revision_slowdown", "four_b_evidence_type": ["valuation_blowoff", "positioning_overheat"], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "structural_rerating_confirmed_after_valueup_capital_return", "current_profile_verdict": "current_profile_too_late", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R6L14_G002_KB_2024_0208", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "R6L14_T003_HANA_STAGE2_CAPRETURN", "case_id": "R6L14_C21_HANA_CAPRETURN_VALUEUP_2024", "symbol": "086790", "company_name": "하나금융지주", "round": "R6", "loop": "14", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "fine_archetype_id": "MEGABANK_VALUEUP_DIVIDEND_BUYBACK_ROE_BUFFER", "sector": "은행지주", "primary_archetype": "financial_roe_pbr_capital_return", "loop_objective": "coverage_gap_fill|counterexample_mining|residual_false_positive_mining|sector_specific_rule_discovery|canonical_archetype_compression|4B_non_price_requirement_stress_test|4C_thesis_break_timing_test", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-01-31", "evidence_available_at_that_date": "FY2023 result/shareholder-return event label: low-PBR value-up context with explicit capital-return component and bank-holdco ROE visibility.", "evidence_source": "Company result/shareholder-return event label; stock-web row trace: 2024-02-01 close 52,000 in atlas/ohlcv_tradable_by_symbol_year/086/086790/2024.csv.", "stage2_evidence_fields": ["public_event_or_disclosure", "policy_or_regulatory_optionality", "relative_strength", "early_revision_signal"], "stage3_evidence_fields": ["financial_visibility", "multiple_public_sources", "low_red_team_risk"], "stage4b_evidence_fields": ["valuation_blowoff"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/086/086790/2024.csv", "profile_path": "atlas/symbol_profiles/086/086790.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-02-01", "entry_price": 52000, "MFE_30D_pct": 24.23, "MFE_90D_pct": 25.58, "MFE_180D_pct": 33.27, "MFE_1Y_pct": 55.0, "MFE_2Y_pct": 152.5, "MAE_30D_pct": -7.88, "MAE_90D_pct": -7.88, "MAE_180D_pct": -7.88, "MAE_1Y_pct": -7.88, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-08-27", "peak_price": 69300, "drawdown_after_peak_pct": -17.89, "green_lateness_ratio": 0.37, "four_b_local_peak_proximity": 0.92, "four_b_full_window_peak_proximity": 0.92, "four_b_timing_verdict": "watch_only_valuation_blowoff_not_full_exit_without_revision_slowdown", "four_b_evidence_type": ["valuation_blowoff", "positioning_overheat"], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "structural_rerating_with_high_initial_mae", "current_profile_verdict": "current_profile_correct", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R6L14_G003_HANA_2024_0201", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "R6L14_T004_KAKAOBANK_FALSE_STAGE2", "case_id": "R6L14_C21_KAKAOBANK_DIGITAL_BETA_2024", "symbol": "323410", "company_name": "카카오뱅크", "round": "R6", "loop": "14", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "fine_archetype_id": "DIGITAL_BANK_GROWTH_BETA_WITHOUT_CAPITAL_RETURN", "sector": "디지털은행", "primary_archetype": "financial_roe_pbr_capital_return", "loop_objective": "coverage_gap_fill|counterexample_mining|residual_false_positive_mining|sector_specific_rule_discovery|canonical_archetype_compression|4B_non_price_requirement_stress_test|4C_thesis_break_timing_test", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-02-07", "evidence_available_at_that_date": "Growth/digital-bank beta and market rebound event label; no board-level capital return or durable ROE/PBR rerating proof at trigger date.", "evidence_source": "Result/event label plus stock-web row trace: 2024-02-08 close 29,100 in atlas/ohlcv_tradable_by_symbol_year/323/323410/2024.csv.", "stage2_evidence_fields": ["public_event_or_disclosure", "relative_strength"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["valuation_blowoff"], "stage4c_evidence_fields": ["legal_or_regulatory_block", "thesis_evidence_broken"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/323/323410/2024.csv", "profile_path": "atlas/symbol_profiles/323/323410.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-02-08", "entry_price": 29100, "MFE_30D_pct": 7.22, "MFE_90D_pct": 7.22, "MFE_180D_pct": 7.22, "MFE_1Y_pct": 15.98, "MFE_2Y_pct": 15.98, "MAE_30D_pct": -6.19, "MAE_90D_pct": -27.84, "MAE_180D_pct": -36.46, "MAE_1Y_pct": -42.1, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-02-15", "peak_price": 31200, "drawdown_after_peak_pct": -40.74, "green_lateness_ratio": "not_applicable:no_confirmed_Stage3_Green_trigger", "four_b_local_peak_proximity": 1.0, "four_b_full_window_peak_proximity": 1.0, "four_b_timing_verdict": "price_beta_peak_without_capital_return_not_full_4B_until_governance_risk", "four_b_evidence_type": ["valuation_blowoff", "price_only"], "four_c_protection_label": "hard_4c_success_after_governance_trigger", "trigger_outcome_label": "failed_rerating_without_capital_return", "current_profile_verdict": "current_profile_false_positive", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R6L14_G004_KAKAOBANK_2024_0208", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "R6L14_T005_JEJUBANK_PRICEONLY_STAGE2", "case_id": "R6L14_C21_JEJUBANK_PRICEONLY_2023", "symbol": "006220", "company_name": "제주은행", "round": "R6", "loop": "14", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "fine_archetype_id": "REGIONAL_BANK_PRICE_ONLY_RUMOR_THEME", "sector": "지방은행/저유동성 금융주", "primary_archetype": "financial_roe_pbr_capital_return", "loop_objective": "coverage_gap_fill|counterexample_mining|residual_false_positive_mining|sector_specific_rule_discovery|canonical_archetype_compression|4B_non_price_requirement_stress_test|4C_thesis_break_timing_test", "trigger_type": "Stage2-Actionable", "trigger_date": "2023-01-17", "evidence_available_at_that_date": "Price-only regional-bank/low-float financial theme. No verified capital-return, ROE/PBR, or shareholder-return evidence at trigger date.", "evidence_source": "Narrative-only market theme label plus stock-web row trace: 2023-01-17 close 13,550 in atlas/ohlcv_tradable_by_symbol_year/006/006220/2023.csv.", "stage2_evidence_fields": ["relative_strength"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["price_only_local_peak", "valuation_blowoff"], "stage4c_evidence_fields": ["thesis_evidence_broken"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/006/006220/2023.csv", "profile_path": "atlas/symbol_profiles/006/006220.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2023-01-17", "entry_price": 13550, "MFE_30D_pct": 81.55, "MFE_90D_pct": 87.45, "MFE_180D_pct": 87.45, "MFE_1Y_pct": 87.45, "MFE_2Y_pct": 87.45, "MAE_30D_pct": -11.44, "MAE_90D_pct": -17.2, "MAE_180D_pct": -45.76, "MAE_1Y_pct": -47.45, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2023-03-30", "peak_price": 25400, "drawdown_after_peak_pct": -71.06, "green_lateness_ratio": "not_applicable:no_confirmed_Stage3_Green_trigger", "four_b_local_peak_proximity": 0.86, "four_b_full_window_peak_proximity": 0.86, "four_b_timing_verdict": "price_only_local_4B_correctly_blocked_from_positive_stage", "four_b_evidence_type": ["price_only", "valuation_blowoff", "positioning_overheat"], "four_c_protection_label": "hard_4c_success_if_price_only_guard_applied", "trigger_outcome_label": "large_MFE_but_failed_structural_rerating", "current_profile_verdict": "current_profile_correct", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R6L14_G005_JEJUBANK_2023_0117", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "R6L14_T006_JEJUBANK_4B_PRICEONLY", "case_id": "R6L14_C21_JEJUBANK_PRICEONLY_2023", "symbol": "006220", "company_name": "제주은행", "round": "R6", "loop": "14", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "fine_archetype_id": "REGIONAL_BANK_PRICE_ONLY_RUMOR_THEME", "sector": "지방은행/저유동성 금융주", "primary_archetype": "financial_roe_pbr_capital_return", "loop_objective": "coverage_gap_fill|counterexample_mining|residual_false_positive_mining|sector_specific_rule_discovery|canonical_archetype_compression|4B_non_price_requirement_stress_test|4C_thesis_break_timing_test", "trigger_type": "4B", "trigger_date": "2023-02-20", "evidence_available_at_that_date": "Local blowoff near speculative price-only peak. No non-price evidence, so this is overlay-only and not a full 4B thesis exit for a real Stage3.", "evidence_source": "Stock-web row trace: 2023-02-20 close 23,750/high 24,600 in atlas/ohlcv_tradable_by_symbol_year/006/006220/2023.csv.", "stage2_evidence_fields": ["relative_strength"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["price_only_local_peak", "valuation_blowoff", "positioning_overheat"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/006/006220/2023.csv", "profile_path": "atlas/symbol_profiles/006/006220.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2023-02-20", "entry_price": 23750, "MFE_30D_pct": 6.95, "MFE_90D_pct": 6.95, "MFE_180D_pct": 6.95, "MFE_1Y_pct": 6.95, "MFE_2Y_pct": 6.95, "MAE_30D_pct": -32.63, "MAE_90D_pct": -52.76, "MAE_180D_pct": -69.05, "MAE_1Y_pct": -69.05, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2023-03-30", "peak_price": 25400, "drawdown_after_peak_pct": -71.06, "green_lateness_ratio": "not_applicable:4B_overlay", "four_b_local_peak_proximity": 0.86, "four_b_full_window_peak_proximity": 0.86, "four_b_timing_verdict": "price_only_local_4B_too_early_for_full_4B_but_correct_as_guardrail", "four_b_evidence_type": ["price_only", "valuation_blowoff", "positioning_overheat"], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "4B_overlay_success_for_price_only_blowoff", "current_profile_verdict": "current_profile_correct", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R6L14_G005_JEJUBANK_2023_0117", "dedupe_for_aggregate": false, "aggregate_group_role": "4B_overlay_only", "is_new_independent_case": false, "reuse_reason": "same case used only for 4B price-only overlay timing audit", "independent_evidence_weight": 0.0, "do_not_count_as_new_case": true}
{"row_type": "trigger", "trigger_id": "R6L14_T007_KAKAOBANK_4C_GOVERNANCE", "case_id": "R6L14_C21_KAKAOBANK_DIGITAL_BETA_2024", "symbol": "323410", "company_name": "카카오뱅크", "round": "R6", "loop": "14", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "fine_archetype_id": "DIGITAL_BANK_GROWTH_BETA_WITHOUT_CAPITAL_RETURN", "sector": "디지털은행", "primary_archetype": "financial_roe_pbr_capital_return", "loop_objective": "coverage_gap_fill|counterexample_mining|residual_false_positive_mining|sector_specific_rule_discovery|canonical_archetype_compression|4B_non_price_requirement_stress_test|4C_thesis_break_timing_test", "trigger_type": "4C", "trigger_date": "2024-07-22", "evidence_available_at_that_date": "Governance/legal-regulatory risk became explicit for bank-control thesis; 4C protection trigger for digital-bank valuation beta.", "evidence_source": "Public governance/regulatory-risk event label plus stock-web row trace: 2024-07-22 close 21,100 in atlas/ohlcv_tradable_by_symbol_year/323/323410/2024.csv.", "stage2_evidence_fields": [], "stage3_evidence_fields": [], "stage4b_evidence_fields": [], "stage4c_evidence_fields": ["legal_or_regulatory_block", "accounting_or_trust_break", "thesis_evidence_broken"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/323/323410/2024.csv", "profile_path": "atlas/symbol_profiles/323/323410.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-07-22", "entry_price": 21100, "MFE_30D_pct": 11.61, "MFE_90D_pct": 11.61, "MFE_180D_pct": 35.07, "MFE_1Y_pct": 35.07, "MFE_2Y_pct": 35.07, "MAE_30D_pct": -12.37, "MAE_90D_pct": -12.37, "MAE_180D_pct": -12.37, "MAE_1Y_pct": -12.37, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-07-23", "peak_price": 23550, "drawdown_after_peak_pct": -21.49, "green_lateness_ratio": "not_applicable:4C_overlay", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "not_applicable", "four_b_evidence_type": [], "four_c_protection_label": "hard_4c_success", "trigger_outcome_label": "4C_success_after_legal_regulatory_thesis_break", "current_profile_verdict": "current_profile_4C_too_late", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R6L14_G004_KAKAOBANK_2024_0208", "dedupe_for_aggregate": false, "aggregate_group_role": "4C_overlay_only", "is_new_independent_case": false, "reuse_reason": "same case used only for 4C governance/thesis-break timing audit", "independent_evidence_weight": 0.0, "do_not_count_as_new_case": true}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R6L14_C21_MERITZ_CAPRETURN_2024", "trigger_id": "R6L14_T001_MERITZ_STAGE2_CAPRETURN", "symbol": "138040", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 6, "revision_score": 13, "relative_strength_score": 14, "customer_quality_score": 8, "policy_or_regulatory_score": 3, "valuation_repricing_score": 15, "execution_risk_score": -3, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "roe_pbr_capital_return_score": 18, "capital_return_durability_score": 8, "capital_buffer_score": 3, "digital_bank_beta_score": 0, "price_only_theme_score": 0, "thesis_break_score": 0}, "weighted_score_before": 82.0, "stage_label_before": "Stage3-Yellow", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 6, "revision_score": 14, "relative_strength_score": 14, "customer_quality_score": 8, "policy_or_regulatory_score": 3, "valuation_repricing_score": 16, "execution_risk_score": -2, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "roe_pbr_capital_return_score": 22, "capital_return_durability_score": 10, "capital_buffer_score": 4, "digital_bank_beta_score": 0, "price_only_theme_score": 0, "thesis_break_score": 0}, "weighted_score_after": 88.0, "stage_label_after": "Stage3-Green", "changed_components": ["roe_pbr_capital_return_score", "capital_return_durability_score", "digital_bank_beta_score", "price_only_theme_score", "thesis_break_score"], "component_delta_explanation": "C21 shadow profile rewards board-confirmed, durable capital return and penalizes digital-bank beta or price-only financial themes without ROE/PBR capital-return evidence.", "MFE_90D_pct": 26.14, "MAE_90D_pct": -4.14, "score_return_alignment_label": "aligned_after_capital_return_gate", "current_profile_verdict": "current_profile_too_late"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R6L14_C21_KB_VALUEUP_CAPRETURN_2024", "trigger_id": "R6L14_T002_KB_STAGE2_VALUEUP", "symbol": "105560", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 5, "revision_score": 12, "relative_strength_score": 15, "customer_quality_score": 8, "policy_or_regulatory_score": 7, "valuation_repricing_score": 14, "execution_risk_score": -4, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "roe_pbr_capital_return_score": 16, "capital_return_durability_score": 6, "capital_buffer_score": 5, "digital_bank_beta_score": 0, "price_only_theme_score": 0, "thesis_break_score": 0}, "weighted_score_before": 84.5, "stage_label_before": "Stage3-Yellow", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 5, "revision_score": 13, "relative_strength_score": 15, "customer_quality_score": 8, "policy_or_regulatory_score": 7, "valuation_repricing_score": 15, "execution_risk_score": -3, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "roe_pbr_capital_return_score": 21, "capital_return_durability_score": 9, "capital_buffer_score": 6, "digital_bank_beta_score": 0, "price_only_theme_score": 0, "thesis_break_score": 0}, "weighted_score_after": 90.0, "stage_label_after": "Stage3-Green", "changed_components": ["roe_pbr_capital_return_score", "capital_return_durability_score", "digital_bank_beta_score", "price_only_theme_score", "thesis_break_score"], "component_delta_explanation": "C21 shadow profile rewards board-confirmed, durable capital return and penalizes digital-bank beta or price-only financial themes without ROE/PBR capital-return evidence.", "MFE_90D_pct": 23.37, "MAE_90D_pct": -11.69, "score_return_alignment_label": "aligned_after_board_level_capital_return_boost", "current_profile_verdict": "current_profile_too_late"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R6L14_C21_HANA_CAPRETURN_VALUEUP_2024", "trigger_id": "R6L14_T003_HANA_STAGE2_CAPRETURN", "symbol": "086790", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 4, "revision_score": 11, "relative_strength_score": 13, "customer_quality_score": 7, "policy_or_regulatory_score": 7, "valuation_repricing_score": 13, "execution_risk_score": -5, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "roe_pbr_capital_return_score": 15, "capital_return_durability_score": 6, "capital_buffer_score": 5, "digital_bank_beta_score": 0, "price_only_theme_score": 0, "thesis_break_score": 0}, "weighted_score_before": 79.0, "stage_label_before": "Stage3-Yellow", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 4, "revision_score": 12, "relative_strength_score": 13, "customer_quality_score": 7, "policy_or_regulatory_score": 7, "valuation_repricing_score": 14, "execution_risk_score": -4, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "roe_pbr_capital_return_score": 19, "capital_return_durability_score": 8, "capital_buffer_score": 6, "digital_bank_beta_score": 0, "price_only_theme_score": 0, "thesis_break_score": 0}, "weighted_score_after": 85.0, "stage_label_after": "Stage3-Yellow", "changed_components": ["roe_pbr_capital_return_score", "capital_return_durability_score", "digital_bank_beta_score", "price_only_theme_score", "thesis_break_score"], "component_delta_explanation": "C21 shadow profile rewards board-confirmed, durable capital return and penalizes digital-bank beta or price-only financial themes without ROE/PBR capital-return evidence.", "MFE_90D_pct": 25.58, "MAE_90D_pct": -7.88, "score_return_alignment_label": "aligned_but_green_not_required", "current_profile_verdict": "current_profile_correct"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R6L14_C21_KAKAOBANK_DIGITAL_BETA_2024", "trigger_id": "R6L14_T004_KAKAOBANK_FALSE_STAGE2", "symbol": "323410", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 7, "relative_strength_score": 12, "customer_quality_score": 5, "policy_or_regulatory_score": 2, "valuation_repricing_score": 11, "execution_risk_score": -6, "legal_or_contract_risk_score": -4, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": -2, "roe_pbr_capital_return_score": 2, "capital_return_durability_score": 0, "capital_buffer_score": 0, "digital_bank_beta_score": 13, "price_only_theme_score": 0, "thesis_break_score": 0}, "weighted_score_before": 76.0, "stage_label_before": "Stage3-Yellow", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 5, "relative_strength_score": 8, "customer_quality_score": 4, "policy_or_regulatory_score": 0, "valuation_repricing_score": 6, "execution_risk_score": -8, "legal_or_contract_risk_score": -8, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": -3, "roe_pbr_capital_return_score": 0, "capital_return_durability_score": 0, "capital_buffer_score": 0, "digital_bank_beta_score": 6, "price_only_theme_score": 0, "thesis_break_score": -8}, "weighted_score_after": 61.0, "stage_label_after": "Stage2-Watch", "changed_components": ["roe_pbr_capital_return_score", "capital_return_durability_score", "digital_bank_beta_score", "price_only_theme_score", "thesis_break_score"], "component_delta_explanation": "C21 shadow profile rewards board-confirmed, durable capital return and penalizes digital-bank beta or price-only financial themes without ROE/PBR capital-return evidence.", "MFE_90D_pct": 7.22, "MAE_90D_pct": -27.84, "score_return_alignment_label": "false_positive_removed_by_capital_return_gate", "current_profile_verdict": "current_profile_false_positive"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R6L14_C21_JEJUBANK_PRICEONLY_2023", "trigger_id": "R6L14_T005_JEJUBANK_PRICEONLY_STAGE2", "symbol": "006220", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 18, "customer_quality_score": 0, "policy_or_regulatory_score": 0, "valuation_repricing_score": 10, "execution_risk_score": -12, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "roe_pbr_capital_return_score": 0, "capital_return_durability_score": 0, "capital_buffer_score": 0, "digital_bank_beta_score": 0, "price_only_theme_score": 20, "thesis_break_score": 0}, "weighted_score_before": 72.0, "stage_label_before": "Stage2-Actionable", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 8, "customer_quality_score": 0, "policy_or_regulatory_score": 0, "valuation_repricing_score": 3, "execution_risk_score": -14, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "roe_pbr_capital_return_score": 0, "capital_return_durability_score": 0, "capital_buffer_score": 0, "digital_bank_beta_score": 0, "price_only_theme_score": 3, "thesis_break_score": -10}, "weighted_score_after": 52.0, "stage_label_after": "Stage1/Watch", "changed_components": ["roe_pbr_capital_return_score", "capital_return_durability_score", "digital_bank_beta_score", "price_only_theme_score", "thesis_break_score"], "component_delta_explanation": "C21 shadow profile rewards board-confirmed, durable capital return and penalizes digital-bank beta or price-only financial themes without ROE/PBR capital-return evidence.", "MFE_90D_pct": 87.45, "MAE_90D_pct": -17.2, "score_return_alignment_label": "guard_prevents_price_only_false_positive", "current_profile_verdict": "current_profile_correct"}
{"row_type": "residual_contribution", "round": "R6", "loop": "14", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "scheduled_round": "R6", "scheduled_loop": "14", "round_schedule_status": "valid", "round_sector_consistency": "pass", "new_independent_case_count": 5, "reused_case_count": 0, "new_symbol_count": 5, "same_archetype_new_symbol_count": 5, "same_archetype_new_trigger_family_count": 5, "new_trigger_family_count": 5, "positive_case_count": 3, "counterexample_count": 2, "current_profile_error_count": 3, "tested_existing_calibrated_axes": ["stage2_actionable_evidence_bonus", "stage3_green_revision_min", "price_only_blowoff_blocks_positive_stage", "full_4b_requires_non_price_evidence", "hard_4c_thesis_break_routes_to_4c"], "residual_error_types_found": ["digital_bank_beta_false_positive", "capital_return_green_too_late", "price_only_financial_theme_high_MFE_false_positive", "4C_governance_risk_late"], "loop_contribution_label": "canonical_archetype_rule_candidate", "do_not_propose_new_weight_delta": false}
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
completed_loop = 14
next_round = R7
next_loop = 14
round_schedule_status = valid
round_sector_consistency = pass
```

## 28. Source Notes

- Stock-Web manifest fields used: source_name=FinanceData/marcap, price_adjustment_status=raw_unadjusted_marcap, min_date=1995-05-02, max_date=2026-02-20, tradable_row_count=14354401, symbol_count=5414, calibration_shard_root=atlas/ohlcv_tradable_by_symbol_year.
- Profile checks used:
  - 138040: latest name 메리츠금융지주, KOSPI, available through 2026-02-20; 2023 corporate-action candidates exist but do not overlap the 2024 calibration window.
  - 105560: latest name KB금융, KOSPI, no corporate-action candidates.
  - 086790: latest name 하나금융지주, KOSPI, no corporate-action candidates.
  - 323410: latest name 카카오뱅크, KOSPI, no corporate-action candidates.
  - 006220: latest name 제주은행, KOSPI; last corporate-action candidate 2018-11-27, outside the 2023 calibration window.
- Historical evidence labels are deliberately event-label level, not live-investment source packets. They must be rechecked against DART/IR source documents if later promoted into a production evidence ledger.
- This MD does not open stock_agent src/e2r code and does not propose production scoring changes.

