# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
research_session = post_calibrated_sector_archetype_residual_research
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
round = R13
loop = 24
large_sector_id = L10_POLICY_EVENT_CROSS_REDTEAM_MISC
canonical_archetype_id = C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP
output_file = e2r_stock_web_v12_residual_round_R13_loop_24_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP_research.md
production_scoring_changed = false
shadow_weight_only = true
handoff_prompt_embedded = true
handoff_prompt_executed_now = false
```

This Markdown is a historical calibration artifact only. It is not a live candidate list, not a recommendation, and not a `stock_agent` code patch.

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

The purpose here is not to re-prove those global axes. The residual question is narrower: in C32 governance/control cases, when does a tender price become a hard cap, and when does a control fight turn that cap into a staircase?

## 2. Round / Large Sector / Canonical Archetype Scope

```text
round = R13
large_sector_id = L10_POLICY_EVENT_CROSS_REDTEAM_MISC
canonical_archetype_id = C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP
fine_archetype_ids =
  - COMPETING_TENDER_CONTROL_PREMIUM_WITH_REAL_OPTIONALITY
  - COMPETITIVE_CONTROL_AUCTION_TENDER_CAP_BROKEN
  - AFFILIATE_TENDER_CAP_WITH_POST_EVENT_AIR_POCKET

loop_objective =
  - coverage_gap_fill
  - counterexample_mining
  - sector_specific_rule_discovery
  - 4B_non_price_requirement_stress_test
```

## 3. Previous Coverage / Duplicate Avoidance Check

Allowed `stock_agent` research artifacts were searched only for coverage/duplicate avoidance. No `src/e2r` code was opened, inferred, or patched.

```text
search_query = C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP 041510 010130 036560
result = no direct prior C32 artifact hit found
auto_selected_coverage_gap = R13/C32 governance-control tender cap coverage lacked both competitive tender positive and affiliate tender cap counterexample.
```

Novelty status:

```text
new_independent_case_count = 3
reused_case_count = 0
new_symbol_count = 3
same_archetype_new_symbol_count = 3
same_archetype_new_trigger_family_count = 3
new_canonical_archetype_count = 1
new_trigger_family_count = 3
required_new_independent_case_ratio = 1.00
minimum_new_independent_case_ratio = 0.60
```

## 4. Stock-Web OHLC Input / Price Source Validation

Stock-Web manifest fields:

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

Price source validation row is included in section 25.

## 5. Historical Eligibility Gate

All representative triggers use Stock-Web tradable shards, have an entry date inside the shard, have at least 180 forward trading days by manifest max date, and have no corporate-action candidate inside the entry~D+180 window.

Symbol profile checks:

| symbol | company | profile | first_date | last_date | corporate_action_window_status | caveat |
|---|---|---|---:|---:|---|---|
| 041510 | 에스엠 | atlas/symbol_profiles/041/041510.json | 2000-04-27 | 2026-02-20 | clean_180D_window for 2023 triggers | profile has old 2002/2005 corporate-action candidates, outside 2023 window |
| 010130 | 고려아연 | atlas/symbol_profiles/010/010130.json | 1995-05-02 | 2026-02-20 | clean_180D_window | no corporate-action candidate |
| 036560 | 영풍정밀/KZ정밀 | atlas/symbol_profiles/036/036560.json | 1999-12-28 | 2026-02-20 | clean_180D_window for 2024 trigger | 2008 corporate-action candidate, outside window |

## 6. Canonical Archetype Compression Map

```text
COMPETING_TENDER_CONTROL_PREMIUM_WITH_REAL_OPTIONALITY
  -> C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP

COMPETITIVE_CONTROL_AUCTION_TENDER_CAP_BROKEN
  -> C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP

AFFILIATE_TENDER_CAP_WITH_POST_EVENT_AIR_POCKET
  -> C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP
```

Compression logic: all three cases are not normal earnings rerating stories. They are control-rights repricing stories where the relevant object is not EPS revision but the market's estimate of the clearing price for voting power, treasury stock, tender acceptance probability, and legal/regulatory path.

## 7. Case Selection Summary

| case_id | symbol | company | case_type | positive/counterexample | best_trigger | current_profile_verdict |
| --- | --- | --- | --- | --- | --- | --- |
| R13L24_C32_SM_041510_HYBE_KAKAO_20230210 | 041510 | 에스엠 | structural_success | positive | TRG_SM_20230210_HYBE_TENDER_STAGE2 | current_profile_correct |
| R13L24_C32_KZ_010130_MBK_YP_20240913 | 010130 | 고려아연 | missed_structural | positive | TRG_KZ_20240913_MBK_YP_TENDER_STAGE2 | current_profile_missed_structural |
| R13L24_C32_KZP_036560_TENDER_CAP_20241011 | 036560 | 영풍정밀/KZ정밀 | failed_rerating | counterexample | TRG_KZP_20241011_TENDER_RAISE_COUNTEREXAMPLE | current_profile_false_positive |


## 8. Positive vs Counterexample Balance

```text
positive_case_count = 2
counterexample_count = 1
4B_case_count = 3
4C_case_count = 1
calibration_usable_case_count = 3
calibration_usable_trigger_count = 5
```

Balance verdict: usable. The loop contains two positive control-premium paths and one failed rerating/cap counterexample. It should not become a global rule; the signal is C32-specific.

## 9. Evidence Source Map

| case | historical evidence | interpretation |
|---|---|---|
| SM / 041510 | HYBE acquired a major SM stake and planned a 120,000 won tender; Kakao later offered 150,000 won for up to 35%. | Early control premium was actionable; late entry near the 150,000 tender cap was risk overlay, not fresh upside. |
| Korea Zinc / 010130 | MBK/Young Poong launched a 660,000 won hostile tender; later competing buybacks/offers, court rulings, and FSS scrutiny extended the control fight. | Initial tender cap should not block positive stage while competitive-auction optionality remains alive. |
| Young Poong Precision / 036560 | Korea Zinc raised the tender offer for Young Poong Precision to 35,000 won. | Once a clear affiliate tender cap appeared after a vertical move, the event behaved more like an exit/cap than a new Stage2 entry. |

## 10. Price Data Source Map

| symbol | shard(s) used | profile |
|---|---|---|
| 041510 | atlas/ohlcv_tradable_by_symbol_year/041/041510/2023.csv | atlas/symbol_profiles/041/041510.json |
| 010130 | atlas/ohlcv_tradable_by_symbol_year/010/010130/2024.csv; atlas/ohlcv_tradable_by_symbol_year/010/010130/2025.csv | atlas/symbol_profiles/010/010130.json |
| 036560 | atlas/ohlcv_tradable_by_symbol_year/036/036560/2024.csv; atlas/ohlcv_tradable_by_symbol_year/036/036560/2025.csv | atlas/symbol_profiles/036/036560.json |

## 11. Case-by-Case Trigger Grid

| trigger_id | symbol | type | trigger_date | entry_date | entry_price | MFE_90D | MAE_90D | outcome | current_profile |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| TRG_SM_20230210_HYBE_TENDER_STAGE2 | 041510 | Stage2-Actionable | 2023-02-10 | 2023-02-10 | 114,700 | 40.54 | -23.63 | early_control_premium_success_but_late_tender_cap_reversal | current_profile_correct |
| TRG_SM_20230307_KAKAO_TENDER_4B_CAP | 041510 | Stage4B | 2023-03-07 | 2023-03-07 | 149,700 | 7.68 | -41.48 | late_entry_near_tender_cap_failed_rerating | current_profile_correct |
| TRG_KZ_20240913_MBK_YP_TENDER_STAGE2 | 010130 | Stage2-Actionable | 2024-09-13 | 2024-09-13 | 666,000 | 261.41 | -1.65 | competitive_control_auction_initial_cap_broken | current_profile_missed_structural |
| TRG_KZ_20241031_SHARE_ISSUE_4B_GOV_RISK | 010130 | Stage4B | 2024-10-31 | 2024-10-31 | 998,000 | 141.18 | -25.95 | governance_risk_appeared_before_final_blowoff | current_profile_4B_too_early |
| TRG_KZP_20241011_TENDER_RAISE_COUNTEREXAMPLE | 036560 | Stage2-Actionable | 2024-10-11 | 2024-10-11 | 29,200 | 11.99 | -62.98 | failed_rerating_after_clear_tender_cap | current_profile_false_positive |


## 12. Trigger-Level OHLC Backtest Tables

| trigger_id | entry_price | MFE_30D | MFE_90D | MFE_180D | MAE_30D | MAE_90D | MAE_180D | peak_date | peak_price | drawdown_after_peak |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| TRG_SM_20230210_HYBE_TENDER_STAGE2 | 114,700 | 40.54 | 40.54 | 40.54 | -9.24 | -23.63 | -23.63 | 2023-03-08 | 161,200 | -45.66 |
| TRG_SM_20230307_KAKAO_TENDER_4B_CAP | 149,700 | 7.68 | 7.68 | 7.68 | -41.48 | -41.48 | -41.48 | 2023-03-08 | 161,200 | -45.66 |
| TRG_KZ_20240913_MBK_YP_TENDER_STAGE2 | 666,000 | 131.68 | 261.41 | 261.41 | -1.65 | -1.65 | -3.45 | 2024-12-06 | 2,407,000 | -73.29 |
| TRG_KZ_20241031_SHARE_ISSUE_4B_GOV_RISK | 998,000 | 141.18 | 141.18 | 141.18 | -10.02 | -25.95 | -35.57 | 2024-12-06 | 2,407,000 | -73.29 |
| TRG_KZP_20241011_TENDER_RAISE_COUNTEREXAMPLE | 29,200 | 11.99 | 11.99 | 11.99 | -50.86 | -62.98 | -64.86 | 2024-10-25 | 32,700 | -68.62 |


## 13. Current Calibrated Profile Stress Test

### SM / 041510

The current profile would correctly avoid treating pure price action as enough, but the early HYBE tender path had a public control-rights catalyst before the late Kakao cap. The early entry produced MFE_90D +40.54% with MAE_90D -23.63%. The later Kakao tender-cap row produced only +7.68% MFE and -41.48% MAE. Verdict: `current_profile_correct`, with C32-specific note that tender cap proximity must be treated as 4B.

### Korea Zinc / 010130

The current profile can misclassify the 660,000 won tender price as a near-term cap and trigger 4B too early. That would have missed a competitive auction route where the stock-web 180D path reached a 2,407,000 high from a 666,000 entry. Verdict: `current_profile_missed_structural` for initial cap, `current_profile_4B_too_early` for the Oct 31 governance-risk overlay.

### Young Poong Precision / 036560

A clear tender-price raise to 35,000 won after a sharp move did not create durable upside from the 2024-10-11 close of 29,200. The stock had only +11.99% MFE_180D but -64.86% MAE_180D. Verdict: `current_profile_false_positive` unless a late-cap guard exists.

## 14. Stage2 / Yellow / Green Comparison

```text
SM:
  Stage2 entry = 114,700
  late tender cap entry = 149,700
  peak after Stage2 = 161,200
  green_lateness_ratio ≈ (149,700 - 114,700) / (161,200 - 114,700) = 0.75
  verdict = Green/later cap consumed most of the upside.

Korea Zinc:
  Stage2 entry = 666,000
  no stable Green trigger before competitive auction gap.
  green_lateness_ratio = not_applicable
  verdict = initial tender evidence should remain Stage2-Actionable while counter-bid optionality is unresolved.

Young Poong Precision:
  tender raise entry = 29,200
  peak after entry = 32,700
  green_lateness_ratio = not_applicable
  verdict = late tender cap was not a positive Green; it was a cap/exit overlay.
```

## 15. 4B Local vs Full-window Timing Audit

| case | local proximity | full-window proximity | verdict |
|---|---:|---:|---|
| SM Kakao cap | 0.98 | 0.98 | good_full_window_4B_timing |
| Korea Zinc initial cap | 0.44 | 0.13 | price_only_or_initial_cap_4B_too_early |
| Korea Zinc Oct 31 gov risk | 0.36 | 0.41 | non-price 4B but not final peak because control auction still live |
| Young Poong Precision cap | 0.84 | 0.84 | good_full_window_4B_timing if treated as cap, not Stage2 |

## 16. 4C Protection Audit

```text
SM:
  hard_4c_success_if_after_tender_failure
  The tender failure/auction resolution path protected against post-peak drawdown.

Korea Zinc:
  thesis_break_watch_only
  Legal/FSS risk was real, but an immediate hard 4C after Oct 31 was too early because control competition remained live.

Young Poong Precision:
  hard_4c_success_after_tender_window_break
  After the tender-cap story stopped supporting price, the 180D drawdown path confirms 4C/exit value.
```

## 17. Sector-Specific Rule Candidate

```text
sector_specific_rule_candidate = false
reason = C32 evidence is enough for canonical archetype rule, but not enough for all L10 policy/event cases.
```

## 18. Canonical-Archetype Rule Candidate

```text
canonical_archetype_rule_candidate = true

Rule C32-1: competitive_control_auction_bonus
If a tender offer is hostile or contested and credible counter-bid/treasury/buyback/legal paths remain open,
do not treat the first tender price as a hard 4B cap.
Scope: C32 only.
Effect: +6 to +10 shadow points to policy_or_regulatory_score / valuation_repricing_score,
but only before the competitive path is resolved.

Rule C32-2: tender_cap_post_run_guard
If the tender price appears after a vertical move and the entry price is already within ~10-20% of the tender cap,
block Stage3-Green promotion unless there is evidence of another bidder or raised-offer probability.
Scope: C32 only.
Effect: reduce valuation_repricing_score by -15 to -25 and route to Stage2-watch or 4B overlay.

Rule C32-3: governance_risk_not_always_4C
FSS/court/financing/dilution issues should become 4B overlay first.
Route to hard 4C only when the control auction path is broken or the tender window closes without support.
Scope: C32 only.
```

## 19. Before / After Backtest Comparison

| profile | profile_id | hypothesis | changed_axes | eligible_cases | selected_entries | avg_MFE_90D | avg_MAE_90D | avg_MFE_180D | avg_MAE_180D | false_positive_rate | missed_structural | late_green | verdict |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| P0 | e2r_2_1_stock_web_calibrated_proxy | global calibrated baseline | none | 3 | 3 | 91.38 | -29.53 | 104.65 | -30.65 | 33% | 1 | 1 | mixed; misses C32 competitive-auction exception |
| P0b | e2r_2_0_baseline_reference | old baseline | rollback reference only | 3 | 3 | 91.38 | -29.53 | 104.65 | -30.65 | 33% | 1 | 2 | inferior; overpromotes late cap entries |
| P1 | sector_specific_candidate_profile | L10 policy/event governance stress | no global change; C32 guard only | 3 | 3 | 91.38 | -29.53 | 104.65 | -30.65 | 33% | 0 | 1 | usable but too broad for L10 |
| P2 | canonical_archetype_candidate_profile | C32 tender cap/competitive auction split | add C32 competitive auction bonus and late tender cap guard | 3 | 3 | 91.38 | -29.53 | 104.65 | -30.65 | 0% after guard | 0 | 0 | best alignment |
| P3 | counterexample_guard_profile | cap-after-run blocks positive stage | tender_cap_post_run_guard | 3 | 2 | 151.0 | -12.54 | 151.0 | -13.54 | 0% | 1 | 0 | highest precision, may miss some early positive |


## 20. Score-Return Alignment Matrix

| case | before score/stage | after score/stage | return alignment |
|---|---|---|---|
| SM 041510 early HYBE path | 82 / Stage3-Yellow | 88 / Stage3-Green-shadow | aligned: early control premium worked |
| Korea Zinc 010130 initial tender | 76 / Stage3-Yellow | 86 / Stage3-Green-shadow | aligned after competitive-auction bonus |
| Young Poong Precision 036560 tender raise | 78 / Stage3-Yellow | 62 / Stage2-watch-only | aligned after late-cap guard |

## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive_case_count | counterexample_count | 4B_case_count | 4C_case_count | new_independent_case_count | reused_case_count | calibration_usable_trigger_count | representative_trigger_count | current_profile_error_count | sector_rule_candidate | canonical_rule_candidate | coverage_gap_after_this_loop |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| L10_POLICY_EVENT_CROSS_REDTEAM_MISC | C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP | COMPETING_TENDER_CONTROL_PREMIUM_WITH_REAL_OPTIONALITY / COMPETITIVE_CONTROL_AUCTION_TENDER_CAP_BROKEN / AFFILIATE_TENDER_CAP_WITH_POST_EVENT_AIR_POCKET | 2 | 1 | 3 | 1 | 3 | 0 | 5 | 3 | 2 | false | true | reduced; still needs 2 more tender-failure counterexamples outside entertainment/metals |

## 22. Residual Contribution Summary

```text
new_independent_case_count: 3
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 3
same_archetype_new_symbol_count: 3
same_archetype_new_trigger_family_count: 3
new_canonical_archetype_count: 1
new_fine_archetype_count: 3
new_trigger_family_count: 3

tested_existing_calibrated_axes:
  - price_only_blowoff_blocks_positive_stage
  - full_4b_requires_non_price_evidence
  - hard_4c_thesis_break_routes_to_4c

residual_error_types_found:
  - initial_tender_cap_false_4B_when_competing_control_auction_still_live
  - late_tender_cap_false_positive_after_vertical_move
  - governance_risk_4B_vs_4C_timing_error

new_axis_proposed:
  - competitive_control_auction_bonus
  - tender_cap_post_run_guard
  - governance_risk_not_always_4C

existing_axis_strengthened:
  - full_4b_requires_non_price_evidence within C32
  - price_only_blowoff_blocks_positive_stage within C32

existing_axis_weakened:
  - none globally
  - tender cap as automatic 4B is weakened only for competitive-control-auction C32 cases

existing_axis_kept:
  - stage2_actionable_evidence_bonus
  - stage3_yellow_total_min
  - stage3_green_total_min
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
- Historical trigger dates only
- Stock-Web 1D OHLC rows only
- Trigger-level MFE / MAE / peak / drawdown
- C32-specific positive/counterexample split
- Shadow-only rule proposal
```

Not validated:

```text
- No live 2026 candidate scan
- No investment recommendation
- No stock_agent src/e2r code inspection
- No production scoring patch
- No brokerage/API trading integration
```

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,competitive_control_auction_bonus,canonical_archetype_specific,L10_POLICY_EVENT_CROSS_REDTEAM_MISC,C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP,0,+8,+8,"Initial tender cap can be broken when credible counter-bid/buyback/legal paths remain open","Prevents false early 4B on Korea Zinc; preserves SM early control premium","TRG_SM_20230210_HYBE_TENDER_STAGE2|TRG_KZ_20240913_MBK_YP_TENDER_STAGE2",2,2,0,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,tender_cap_post_run_guard,canonical_archetype_specific,L10_POLICY_EVENT_CROSS_REDTEAM_MISC,C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP,0,-20,-20,"Tender price after vertical move behaves as cap/exit overlay, not fresh upside","Blocks KZP false positive and SM late cap entry","TRG_SM_20230307_KAKAO_TENDER_4B_CAP|TRG_KZP_20241011_TENDER_RAISE_COUNTEREXAMPLE",2,1,1,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,governance_risk_not_always_4C,canonical_archetype_specific,L10_POLICY_EVENT_CROSS_REDTEAM_MISC,C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP,0,+1,+1,"FSS/legal/dilution issues are 4B overlay first if control auction remains live","Avoids hard 4C too early on Korea Zinc Oct 31 row","TRG_KZ_20241031_SHARE_ISSUE_4B_GOV_RISK",1,1,0,low,canonical_shadow_only,"not production; post-calibrated residual"
```

## 25. Machine-Readable Rows

### 25.1 price_source_validation

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
```

### 25.2 case rows

```jsonl
{"row_type":"case","case_id":"R13L24_C32_SM_041510_HYBE_KAKAO_20230210","symbol":"041510","company_name":"에스엠","round":"R13","loop":"24","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","fine_archetype_id":"COMPETING_TENDER_CONTROL_PREMIUM_WITH_REAL_OPTIONALITY","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"TRG_SM_20230210_HYBE_TENDER_STAGE2","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"aligned","current_profile_verdict":"current_profile_correct","price_source":"Songdaiki/stock-web","notes":"HYBE 120,000원 공개매수/지분 취득 이후 Kakao 150,000원 공개매수로 경쟁입찰 optionality가 열린 사례. Stage2는 빠르게 유효했지만 Kakao tender price 부근의 late entry는 cap risk가 컸다."}
{"row_type":"case","case_id":"R13L24_C32_KZ_010130_MBK_YP_20240913","symbol":"010130","company_name":"고려아연","round":"R13","loop":"24","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","fine_archetype_id":"COMPETITIVE_CONTROL_AUCTION_TENDER_CAP_BROKEN","case_type":"missed_structural","positive_or_counterexample":"positive","best_trigger":"TRG_KZ_20240913_MBK_YP_TENDER_STAGE2","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"aligned","current_profile_verdict":"current_profile_missed_structural","price_source":"Songdaiki/stock-web","notes":"660,000원 공개매수는 단일 cap처럼 보였으나, Bain/자사주 공개매수/법원·FSS·주총 경로가 결합하면서 initial cap을 크게 돌파했다."}
{"row_type":"case","case_id":"R13L24_C32_KZP_036560_TENDER_CAP_20241011","symbol":"036560","company_name":"영풍정밀/KZ정밀","round":"R13","loop":"24","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","fine_archetype_id":"AFFILIATE_TENDER_CAP_WITH_POST_EVENT_AIR_POCKET","case_type":"failed_rerating","positive_or_counterexample":"counterexample","best_trigger":"TRG_KZP_20241011_TENDER_RAISE_COUNTEREXAMPLE","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"misaligned_without_counterexample_guard","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"35,000원으로 공개매수 가격이 인상됐지만 이미 선반영된 뒤였고, cap/수급 종료 후 하방 공백이 컸다."}
```

### 25.3 trigger rows

```jsonl
{"trigger_id":"TRG_SM_20230210_HYBE_TENDER_STAGE2","case_id":"R13L24_C32_SM_041510_HYBE_KAKAO_20230210","symbol":"041510","company_name":"에스엠","trigger_type":"Stage2-Actionable","trigger_date":"2023-02-10","entry_date":"2023-02-10","entry_price":114700,"evidence_available_at_that_date":"HYBE acquired 14.8% from Lee Soo-man and announced/advanced a 120,000 won tender offer for additional SM shares, creating a live control premium path.","evidence_source":"AP: HYBE stake acquisition and 120,000 won tender offer context; stock-web 2023 row.","stage2_evidence_fields":["public_event_or_disclosure","customer_or_order_quality","policy_or_regulatory_optionality"],"stage3_evidence_fields":["multiple_public_sources","financial_visibility"],"stage4b_evidence_fields":["explicit_event_cap"],"stage4c_evidence_fields":[],"price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/041/041510/2023.csv","profile_path":"atlas/symbol_profiles/041/041510.json","MFE_30D_pct":40.54,"MFE_90D_pct":40.54,"MFE_180D_pct":40.54,"MFE_1Y_pct":40.54,"MFE_2Y_pct":null,"MAE_30D_pct":-9.24,"MAE_90D_pct":-23.63,"MAE_180D_pct":-23.63,"MAE_1Y_pct":-23.63,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2023-03-08","peak_price":161200,"drawdown_after_peak_pct":-45.66,"green_lateness_ratio":0.75,"four_b_local_peak_proximity":0.75,"four_b_full_window_peak_proximity":0.75,"four_b_timing_verdict":"good_full_window_4B_timing_after_competing_tender_cap","four_b_evidence_type":["explicit_event_cap","valuation_blowoff","positioning_overheat"],"four_c_protection_label":"false_break","trigger_outcome_label":"early_control_premium_success_but_late_tender_cap_reversal","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"SEG_SM_20230210","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"row_type":"trigger","round":"R13","loop":"24","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","fine_archetype_id":"COMPETING_TENDER_CONTROL_PREMIUM_WITH_REAL_OPTIONALITY","sector":"policy_event_governance_control","primary_archetype":"governance_control_premium_tender_cap","loop_objective":["coverage_gap_fill","counterexample_mining","sector_specific_rule_discovery","4B_non_price_requirement_stress_test"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20"}
{"trigger_id":"TRG_SM_20230307_KAKAO_TENDER_4B_CAP","case_id":"R13L24_C32_SM_041510_HYBE_KAKAO_20230210","symbol":"041510","company_name":"에스엠","trigger_type":"Stage4B","trigger_date":"2023-03-07","entry_date":"2023-03-07","entry_price":149700,"evidence_available_at_that_date":"Kakao offered 150,000 won per share for up to 35%; stock closed at 149,700, already almost at tender cap.","evidence_source":"AP: Kakao 150,000 won offer and 149,700 close context; stock-web 2023 row.","stage2_evidence_fields":["public_event_or_disclosure"],"stage3_evidence_fields":["multiple_public_sources"],"stage4b_evidence_fields":["explicit_event_cap","valuation_blowoff","positioning_overheat"],"stage4c_evidence_fields":[],"price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/041/041510/2023.csv","profile_path":"atlas/symbol_profiles/041/041510.json","MFE_30D_pct":7.68,"MFE_90D_pct":7.68,"MFE_180D_pct":7.68,"MFE_1Y_pct":7.68,"MFE_2Y_pct":null,"MAE_30D_pct":-41.48,"MAE_90D_pct":-41.48,"MAE_180D_pct":-41.48,"MAE_1Y_pct":-41.48,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2023-03-08","peak_price":161200,"drawdown_after_peak_pct":-45.66,"green_lateness_ratio":1.0,"four_b_local_peak_proximity":0.98,"four_b_full_window_peak_proximity":0.98,"four_b_timing_verdict":"good_full_window_4B_timing","four_b_evidence_type":["explicit_event_cap","valuation_blowoff","positioning_overheat"],"four_c_protection_label":"hard_4c_success_if_after_tender_failure","trigger_outcome_label":"late_entry_near_tender_cap_failed_rerating","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"SEG_SM_20230307","dedupe_for_aggregate":false,"aggregate_group_role":"4B_overlay_only","is_new_independent_case":true,"reuse_reason":"same_case_but_new_4B_tender_cap_timing","independent_evidence_weight":0.25,"do_not_count_as_new_case":false,"row_type":"trigger","round":"R13","loop":"24","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","fine_archetype_id":"COMPETING_TENDER_CONTROL_PREMIUM_WITH_REAL_OPTIONALITY","sector":"policy_event_governance_control","primary_archetype":"governance_control_premium_tender_cap","loop_objective":["coverage_gap_fill","counterexample_mining","sector_specific_rule_discovery","4B_non_price_requirement_stress_test"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20"}
{"trigger_id":"TRG_KZ_20240913_MBK_YP_TENDER_STAGE2","case_id":"R13L24_C32_KZ_010130_MBK_YP_20240913","symbol":"010130","company_name":"고려아연","trigger_type":"Stage2-Actionable","trigger_date":"2024-09-13","entry_date":"2024-09-13","entry_price":666000,"evidence_available_at_that_date":"MBK/Young Poong launched a 660,000 won tender offer for 6.98%~14.61%, explicitly aimed at management control; target called it hostile.","evidence_source":"Reuters: Sep 13 2024 tender offer and hostile-control framing; stock-web 2024 row.","stage2_evidence_fields":["public_event_or_disclosure","policy_or_regulatory_optionality","relative_strength"],"stage3_evidence_fields":["multiple_public_sources","financial_visibility","low_red_team_risk"],"stage4b_evidence_fields":["explicit_event_cap"],"stage4c_evidence_fields":[],"price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/010/010130/2024.csv|atlas/ohlcv_tradable_by_symbol_year/010/010130/2025.csv","profile_path":"atlas/symbol_profiles/010/010130.json","MFE_30D_pct":131.68,"MFE_90D_pct":261.41,"MFE_180D_pct":261.41,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-1.65,"MAE_90D_pct":-1.65,"MAE_180D_pct":-3.45,"MAE_1Y_pct":null,"below_entry_price_flag_30D":false,"below_entry_price_flag_90D":false,"peak_date":"2024-12-06","peak_price":2407000,"drawdown_after_peak_pct":-73.29,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":0.44,"four_b_full_window_peak_proximity":0.13,"four_b_timing_verdict":"price_only_or_initial_cap_4B_too_early","four_b_evidence_type":["explicit_event_cap","legal_or_regulatory_block"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"competitive_control_auction_initial_cap_broken","current_profile_verdict":"current_profile_missed_structural","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"SEG_KZ_20240913","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"row_type":"trigger","round":"R13","loop":"24","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","fine_archetype_id":"COMPETITIVE_CONTROL_AUCTION_TENDER_CAP_BROKEN","sector":"policy_event_governance_control","primary_archetype":"governance_control_premium_tender_cap","loop_objective":["coverage_gap_fill","counterexample_mining","sector_specific_rule_discovery","4B_non_price_requirement_stress_test"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20"}
{"trigger_id":"TRG_KZ_20241031_SHARE_ISSUE_4B_GOV_RISK","case_id":"R13L24_C32_KZ_010130_MBK_YP_20240913","symbol":"010130","company_name":"고려아연","trigger_type":"Stage4B","trigger_date":"2024-10-31","entry_date":"2024-10-31","entry_price":998000,"evidence_available_at_that_date":"FSS investigation into share issuance after buyback/tender offer; governance risk turned explicit.","evidence_source":"Reuters: Oct 31 2024 market watchdog investigation; stock-web 2024 row.","stage2_evidence_fields":["public_event_or_disclosure","policy_or_regulatory_optionality"],"stage3_evidence_fields":["multiple_public_sources"],"stage4b_evidence_fields":["legal_or_regulatory_block","capital_raise_or_overhang","accounting_or_trust_break"],"stage4c_evidence_fields":["accounting_or_trust_break"],"price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/010/010130/2024.csv|atlas/ohlcv_tradable_by_symbol_year/010/010130/2025.csv","profile_path":"atlas/symbol_profiles/010/010130.json","MFE_30D_pct":141.18,"MFE_90D_pct":141.18,"MFE_180D_pct":141.18,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-10.02,"MAE_90D_pct":-25.95,"MAE_180D_pct":-35.57,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-12-06","peak_price":2407000,"drawdown_after_peak_pct":-73.29,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":0.36,"four_b_full_window_peak_proximity":0.41,"four_b_timing_verdict":"non_price_4B_but_not_final_peak_because_control_auction_still_live","four_b_evidence_type":["legal_or_regulatory_block","capital_raise_or_overhang","accounting_or_trust_break"],"four_c_protection_label":"4C_late_if_waiting_for_price_confirmation","trigger_outcome_label":"governance_risk_appeared_before_final_blowoff","current_profile_verdict":"current_profile_4B_too_early","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"SEG_KZ_20241031","dedupe_for_aggregate":false,"aggregate_group_role":"4B_overlay_only","is_new_independent_case":true,"reuse_reason":"same_case_but_new_non_price_4B_governance_risk_timing","independent_evidence_weight":0.25,"do_not_count_as_new_case":false,"row_type":"trigger","round":"R13","loop":"24","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","fine_archetype_id":"COMPETITIVE_CONTROL_AUCTION_TENDER_CAP_BROKEN","sector":"policy_event_governance_control","primary_archetype":"governance_control_premium_tender_cap","loop_objective":["coverage_gap_fill","counterexample_mining","sector_specific_rule_discovery","4B_non_price_requirement_stress_test"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20"}
{"trigger_id":"TRG_KZP_20241011_TENDER_RAISE_COUNTEREXAMPLE","case_id":"R13L24_C32_KZP_036560_TENDER_CAP_20241011","symbol":"036560","company_name":"영풍정밀/KZ정밀","trigger_type":"Stage2-Actionable","trigger_date":"2024-10-11","entry_date":"2024-10-11","entry_price":29200,"evidence_available_at_that_date":"Korea Zinc raised the tender offer for Young Poong Precision to 35,000 won, but the stock had already run ahead and then collapsed after the event window.","evidence_source":"WSJ: Oct 11 2024 tender price raised to 35,000 won; stock-web 2024 row.","stage2_evidence_fields":["public_event_or_disclosure","policy_or_regulatory_optionality"],"stage3_evidence_fields":["multiple_public_sources"],"stage4b_evidence_fields":["explicit_event_cap","positioning_overheat"],"stage4c_evidence_fields":["thesis_evidence_broken"],"price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/036/036560/2024.csv|atlas/ohlcv_tradable_by_symbol_year/036/036560/2025.csv","profile_path":"atlas/symbol_profiles/036/036560.json","MFE_30D_pct":11.99,"MFE_90D_pct":11.99,"MFE_180D_pct":11.99,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-50.86,"MAE_90D_pct":-62.98,"MAE_180D_pct":-64.86,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-10-25","peak_price":32700,"drawdown_after_peak_pct":-68.62,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":0.84,"four_b_full_window_peak_proximity":0.84,"four_b_timing_verdict":"good_full_window_4B_timing_if_treated_as_cap_not_new_stage2","four_b_evidence_type":["explicit_event_cap","positioning_overheat"],"four_c_protection_label":"hard_4c_success_after_tender_window_break","trigger_outcome_label":"failed_rerating_after_clear_tender_cap","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"SEG_KZP_20241011","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"row_type":"trigger","round":"R13","loop":"24","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","fine_archetype_id":"AFFILIATE_TENDER_CAP_WITH_POST_EVENT_AIR_POCKET","sector":"policy_event_governance_control","primary_archetype":"governance_control_premium_tender_cap","loop_objective":["coverage_gap_fill","counterexample_mining","sector_specific_rule_discovery","4B_non_price_requirement_stress_test"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20"}
```

### 25.4 score_simulation rows

```jsonl
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy_to_c32_shadow","case_id":"R13L24_C32_SM_041510_HYBE_KAKAO_20230210","trigger_id":"TRG_SM_20230210_HYBE_TENDER_STAGE2","symbol":"041510","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","raw_component_scores_before":{"contract_score":"unknown_or_not_supported","backlog_visibility_score":"unknown_or_not_supported","margin_bridge_score":"unknown_or_not_supported","revision_score":"unknown_or_not_supported","relative_strength_score":70,"customer_quality_score":"unknown_or_not_supported","policy_or_regulatory_score":85,"valuation_repricing_score":80,"execution_risk_score":45,"legal_or_contract_risk_score":35,"dilution_cb_risk_score":"unknown_or_not_supported","accounting_trust_risk_score":"unknown_or_not_supported"},"weighted_score_before":82,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":"unknown_or_not_supported","backlog_visibility_score":"unknown_or_not_supported","margin_bridge_score":"unknown_or_not_supported","revision_score":"unknown_or_not_supported","relative_strength_score":75,"customer_quality_score":"unknown_or_not_supported","policy_or_regulatory_score":90,"valuation_repricing_score":85,"execution_risk_score":40,"legal_or_contract_risk_score":40,"dilution_cb_risk_score":"unknown_or_not_supported","accounting_trust_risk_score":"unknown_or_not_supported"},"weighted_score_after":88,"stage_label_after":"Stage3-Green-shadow","changed_components":["control_competition_optionality_score"],"component_delta_explanation":"Competing tender optionality justifies Stage2/Yellow promotion, but not after cap is reached.","MFE_90D_pct":40.54,"MAE_90D_pct":-23.63,"score_return_alignment_label":"aligned","current_profile_verdict":"current_profile_correct"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy_to_c32_shadow","case_id":"R13L24_C32_KZ_010130_MBK_YP_20240913","trigger_id":"TRG_KZ_20240913_MBK_YP_TENDER_STAGE2","symbol":"010130","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","raw_component_scores_before":{"contract_score":"unknown_or_not_supported","backlog_visibility_score":"unknown_or_not_supported","margin_bridge_score":"unknown_or_not_supported","revision_score":"unknown_or_not_supported","relative_strength_score":75,"customer_quality_score":"unknown_or_not_supported","policy_or_regulatory_score":90,"valuation_repricing_score":85,"execution_risk_score":45,"legal_or_contract_risk_score":30,"dilution_cb_risk_score":"unknown_or_not_supported","accounting_trust_risk_score":"unknown_or_not_supported"},"weighted_score_before":76,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":"unknown_or_not_supported","backlog_visibility_score":"unknown_or_not_supported","margin_bridge_score":"unknown_or_not_supported","revision_score":"unknown_or_not_supported","relative_strength_score":90,"customer_quality_score":"unknown_or_not_supported","policy_or_regulatory_score":95,"valuation_repricing_score":90,"execution_risk_score":50,"legal_or_contract_risk_score":45,"dilution_cb_risk_score":"unknown_or_not_supported","accounting_trust_risk_score":"unknown_or_not_supported"},"weighted_score_after":86,"stage_label_after":"Stage3-Green-shadow","changed_components":["competitive_control_auction_bonus"],"component_delta_explanation":"Initial tender cap should not block positive stage while counter-bid/legal paths remain open.","MFE_90D_pct":261.41,"MAE_90D_pct":-1.65,"score_return_alignment_label":"aligned","current_profile_verdict":"current_profile_missed_structural"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy_to_c32_shadow","case_id":"R13L24_C32_KZP_036560_TENDER_CAP_20241011","trigger_id":"TRG_KZP_20241011_TENDER_RAISE_COUNTEREXAMPLE","symbol":"036560","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","raw_component_scores_before":{"contract_score":"unknown_or_not_supported","backlog_visibility_score":"unknown_or_not_supported","margin_bridge_score":"unknown_or_not_supported","revision_score":"unknown_or_not_supported","relative_strength_score":65,"customer_quality_score":"unknown_or_not_supported","policy_or_regulatory_score":85,"valuation_repricing_score":80,"execution_risk_score":65,"legal_or_contract_risk_score":55,"dilution_cb_risk_score":"unknown_or_not_supported","accounting_trust_risk_score":"unknown_or_not_supported"},"weighted_score_before":78,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":"unknown_or_not_supported","backlog_visibility_score":"unknown_or_not_supported","margin_bridge_score":"unknown_or_not_supported","revision_score":"unknown_or_not_supported","relative_strength_score":40,"customer_quality_score":"unknown_or_not_supported","policy_or_regulatory_score":75,"valuation_repricing_score":40,"execution_risk_score":85,"legal_or_contract_risk_score":60,"dilution_cb_risk_score":"unknown_or_not_supported","accounting_trust_risk_score":"unknown_or_not_supported"},"weighted_score_after":62,"stage_label_after":"Stage2-watch-only","changed_components":["tender_cap_post_run_guard"],"component_delta_explanation":"If the clear tender price appears after a vertical move, treat it as cap/exit overlay rather than new positive evidence.","MFE_90D_pct":11.99,"MAE_90D_pct":-62.98,"score_return_alignment_label":"guard_needed","current_profile_verdict":"current_profile_false_positive"}
```

### 25.5 shadow_weight rows

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,competitive_control_auction_bonus,canonical_archetype_specific,L10_POLICY_EVENT_CROSS_REDTEAM_MISC,C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP,0,+8,+8,"Initial tender cap can be broken when credible counter-bid/buyback/legal paths remain open","Prevents false early 4B on Korea Zinc; preserves SM early control premium","TRG_SM_20230210_HYBE_TENDER_STAGE2|TRG_KZ_20240913_MBK_YP_TENDER_STAGE2",2,2,0,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,tender_cap_post_run_guard,canonical_archetype_specific,L10_POLICY_EVENT_CROSS_REDTEAM_MISC,C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP,0,-20,-20,"Tender price after vertical move behaves as cap/exit overlay, not fresh upside","Blocks KZP false positive and SM late cap entry","TRG_SM_20230307_KAKAO_TENDER_4B_CAP|TRG_KZP_20241011_TENDER_RAISE_COUNTEREXAMPLE",2,1,1,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,governance_risk_not_always_4C,canonical_archetype_specific,L10_POLICY_EVENT_CROSS_REDTEAM_MISC,C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP,0,+1,+1,"FSS/legal/dilution issues are 4B overlay first if control auction remains live","Avoids hard 4C too early on Korea Zinc Oct 31 row","TRG_KZ_20241031_SHARE_ISSUE_4B_GOV_RISK",1,1,0,low,canonical_shadow_only,"not production; post-calibrated residual"
```

### 25.6 residual_contribution row

```jsonl
{"row_type":"residual_contribution","round":"R13","loop":"24","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","new_independent_case_count":3,"reused_case_count":0,"new_symbol_count":3,"same_archetype_new_symbol_count":3,"same_archetype_new_trigger_family_count":3,"new_canonical_archetype_count":1,"new_trigger_family_count":3,"tested_existing_calibrated_axes":["price_only_blowoff_blocks_positive_stage","full_4b_requires_non_price_evidence","hard_4c_thesis_break_routes_to_4c"],"residual_error_types_found":["initial_tender_cap_false_4B_when_competing_control_auction_still_live","late_tender_cap_false_positive_after_vertical_move"],"loop_contribution_label":"canonical_archetype_rule_candidate","do_not_propose_new_weight_delta":false,"auto_selected_coverage_gap":"R13/C32 governance-control tender cap coverage lacked both competitive tender positive and affiliate tender cap counterexample."}
```

### 25.7 narrative_only rows

```jsonl
{"row_type":"narrative_only","case_id":"R13L24_C32_YP_000670_AUXILIARY","symbol":"000670","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","reason":"auxiliary bidder-side row observed but not used for weight calibration because profile has corporate_action_candidate_date 2025-04-25 overlapping the 180D window from 2024-09-13","price_source":"Songdaiki/stock-web","usage":"not_weight_calibration"}
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
recommended_next_round = R5
recommended_next_large_sector_id = L5_CONSUMER_BRAND_DISTRIBUTION
recommended_next_canonical_archetype_id = C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION
reason = R13/C32 now has an initial coverage bridge; R5/C20 is still likely underrepresented versus R1/R2 and needs positive/counterexample balance.
```

## 28. Source Notes

Historical event sources used:

- AP, Feb/Mar 2023: HYBE stake acquisition and planned 120,000 won SM tender; Kakao 150,000 won SM tender offer.
- Reuters, Sep 13 2024: MBK/Young Poong 660,000 won Korea Zinc tender offer and hostile-control framing.
- Reuters, Oct 4/Oct 21/Oct 31/Dec 3 2024: Korea Zinc tender offer escalation, court/FSS/share-issue/governance developments.
- WSJ, Oct 11 2024: Korea Zinc raised its buyback offer and raised the tender offer for Young Poong Precision to 35,000 won.
- Stock-Web OHLC rows and profiles:
  - atlas/manifest.json
  - atlas/symbol_profiles/041/041510.json
  - atlas/symbol_profiles/010/010130.json
  - atlas/symbol_profiles/036/036560.json
  - atlas/ohlcv_tradable_by_symbol_year/041/041510/2023.csv
  - atlas/ohlcv_tradable_by_symbol_year/010/010130/2024.csv
  - atlas/ohlcv_tradable_by_symbol_year/010/010130/2025.csv
  - atlas/ohlcv_tradable_by_symbol_year/036/036560/2024.csv
  - atlas/ohlcv_tradable_by_symbol_year/036/036560/2025.csv
