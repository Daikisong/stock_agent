# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

- file_name: `e2r_stock_web_v12_residual_round_R6_loop_10_L6_FINANCIAL_CAPITAL_RETURN_DIGITAL_C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN_research.md`
- research_session: `post_calibrated_sector_archetype_residual_research`
- mode: `historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12`
- round: `R6`
- loop: `10`
- large_sector_id: `L6_FINANCIAL_CAPITAL_RETURN_DIGITAL`
- canonical_archetype_id: `C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN`
- fine_archetype_id: `VALUE_UP_BANK_ROE_PBR_CAPITAL_RETURN_VS_DIGITAL_PREMIUM_COUNTEREXAMPLE`
- loop_objective: `counterexample_mining | sector_specific_rule_discovery | canonical_archetype_compression | coverage_gap_fill`
- current_stock_discovery_allowed: `false`
- stock_agent_code_access_allowed: `false`
- stock_agent_code_patch_allowed: `false`
- production_scoring_changed: `false`
- shadow_weight_only: `true`
- output_type: `standalone Markdown research file`
- investment_recommendation_language: `none`

## 1. Current Calibrated Profile Assumption

This loop treats `e2r_2_1_stock_web_calibrated_proxy` as the current default profile, not the old E2R 2.0 baseline.

Existing applied axes are not re-proposed as global rules:

- `stage2_actionable_evidence_bonus = +2.0`
- `stage3_yellow_total_min = 75.0`
- `stage3_green_total_min = 87.0`
- `stage3_green_revision_min = 55.0`
- `stage3_cross_evidence_green_buffer = +1.5`
- `price_only_blowoff_blocks_positive_stage = true`
- `full_4b_requires_non_price_evidence = true`
- `hard_4c_thesis_break_routes_to_4c = true`

This MD stress-tests those axes only as context. The new proposal is limited to a C21 canonical-archetype shadow guard.

## 2. Round / Large Sector / Canonical Archetype Scope

- R6 maps to `L6_FINANCIAL_CAPITAL_RETURN_DIGITAL`.
- The selected canonical archetype is `C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN`.
- The specific residual question is whether a broad 2024 Korea Corporate Value-up policy trigger should promote all financials, or whether C21 needs a sharper gate that distinguishes:
  - low-PBR financial holding companies with executable capital-return routes, from
  - high-PBR/digital-bank policy beta without comparable capital-return execution.

## 3. Previous Coverage / Duplicate Avoidance Check

Allowed research artifacts were used only for coverage and duplicate-risk framing.

- `reports/e2r_calibration/ingest_summary.md` indicates the old ingest snapshot covered R1~R13, 398 discovered MDs, 107 parsed result MDs, 1,940 validated trigger rows, and 1,376 aggregate representative trigger rows.
- `reports/e2r_calibration/applied_scoring_diff.md` already applied the global Stage2/Yellow/Green and 4B/4C guardrail axes.
- `data/e2r/calibration/md_registry.jsonl` shows R6 loops 1~8 existed under `financial_capital_allocation_digital_finance_research`, with loop 2~4 being identical by SHA and later loops having similar row counts.
- `data/e2r/calibration/trigger_rows_representative.jsonl` was empty in the accessible fetch, so symbol-level de-duplication could not be fully verified from the allowed artifacts.

Novelty stance:

```text
auto_selected_coverage_gap = R6/C21 policy-beta residual error and counterexample balance
same_canonical_archetype_research = allowed
same_symbol_same_trigger_date_research = not knowingly used
symbol_level_duplicate_verification = limited_by_empty_representative_trigger_file
```

## 4. Stock-Web OHLC Input / Price Source Validation

|source_name|source_repo_url|price_adjustment_status|min_date|max_date|tradable_row_count|raw_row_count|symbol_count|active_like_symbol_count|inactive_or_delisted_like_symbol_count|markets|calibration_shard_root|raw_shard_root|schema_path|universe_path|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|FinanceData/marcap|https://github.com/FinanceData/marcap|raw_unadjusted_marcap|1995-05-02|2026-02-20|14354401|15214118|5414|2868|2546|['KONEX', 'KOSDAQ', 'KOSDAQ GLOBAL', 'KOSPI']|atlas/ohlcv_tradable_by_symbol_year|atlas/ohlcv_raw_by_symbol_year|atlas/schema.json|atlas/universe/all_symbols.csv|


Validation notes:

- Price source: `Songdaiki/stock-web`
- Upstream source basis: `FinanceData/marcap`
- Price basis: `tradable_raw`
- Adjustment status: `raw_unadjusted_marcap`
- Manifest max date: `2026-02-20`
- The selected entry date `2024-02-26` has clean 180-trading-day forward windows for all three symbols.
- 2Y fields are not used for calibration because the forward window approaches the atlas max-date boundary.

## 5. Historical Eligibility Gate

| case_id | symbol | entry_date | 180D forward window | corporate action candidate in profile | calibration_usable | block_reason |
|---|---:|---:|---:|---:|---:|---|
| R6L10_C21_KB_20240226 | 105560 | 2024-02-26 | available | 0 | true | none |
| R6L10_C21_HANA_20240226 | 086790 | 2024-02-26 | available | 0 | true | none |
| R6L10_C21_KAKAOBANK_20240226 | 323410 | 2024-02-26 | available | 0 | true | none |

## 6. Canonical Archetype Compression Map

| source sector phrase | large_sector_id | canonical_archetype_id | fine_archetype_id | compression rationale |
|---|---|---|---|---|
| 금융·자본배분·디지털금융 | L6_FINANCIAL_CAPITAL_RETURN_DIGITAL | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | VALUE_UP_BANK_ROE_PBR_CAPITAL_RETURN_VS_DIGITAL_PREMIUM_COUNTEREXAMPLE | Compresses bank value-up, shareholder return, PBR/ROE rerating, and digital-bank policy-beta failure into one C21 rule surface. |

## 7. Case Selection Summary

|case_id|symbol|company|role|polarity|trigger_date|entry_price|mfe90|mae90|mfe180|mae180|verdict|
|---|---|---|---|---|---|---|---|---|---|---|---|
|R6L10_C21_KB_20240226|105560|KB금융|structural_success|positive|2024-02-26|62500|44.0|-4.48|66.24|-4.48|current_profile_correct|
|R6L10_C21_HANA_20240226|086790|하나금융지주|structural_success|positive|2024-02-26|55400|22.38|-6.86|25.09|-6.86|current_profile_correct|
|R6L10_C21_KAKAOBANK_20240226|323410|카카오뱅크|failed_rerating|counterexample|2024-02-26|30150|1.66|-33.5|1.66|-38.67|current_profile_false_positive|


Interpretation:

- KB금융 and 하나금융지주 are positive C21 cases: broad policy trigger plus low-PBR/capital-return execution route produced positive 90D/180D MFE with controlled MAE.
- 카카오뱅크 is the counterexample: the same broad policy date did not create a durable rerating path; the stock had only +1.66% MFE and -38.67% MAE over 180D.

## 8. Positive vs Counterexample Balance

```text
positive_structural_success = 2
counterexample_or_failed_rerating = 1
4B_or_4C_case = 0
calibration_usable_case_count = 3
minimum_positive_case_count_met = true
minimum_counterexample_count_met = true
minimum_calibration_usable_case_count_met = true
```

## 9. Evidence Source Map

| evidence family | trigger date | evidence used | stage use | limitation |
|---|---:|---|---|---|
| Korea Corporate Value-up policy | 2024-02-26 | Public policy package to improve listed-company valuation/shareholder returns | Stage2 policy option | It is sector-wide and cannot by itself prove C21 rerating. |
| Low-PBR financial holding company rerating base | 2024-02-26 | KB/Hana low-PBR value-up beta plus bank shareholder-return framing | Stage2/Yellow | Needs actual capital-return execution to avoid policy-only overfit. |
| Capital-return execution route | 2024 historical context | Buyback/cancellation/dividend route is treated as C21 execution quality | Stage3/Yellow support | This MD uses proxy scoring, not production code. |
| Digital-bank high-PBR policy beta | 2024-02-26 | KakaoBank receives sector policy beta but lacks comparable low-PBR/capital-return setup | Counterexample guard | Used to cap positive promotion, not to create a short/negative recommendation. |

## 10. Price Data Source Map

| symbol | company | profile_path | tradable_shard | profile caveat |
|---:|---|---|---|---|
| 105560 | KB금융 | atlas/symbol_profiles/105/105560.json | atlas/ohlcv_tradable_by_symbol_year/105/105560/2024.csv | no corporate action candidates |
| 086790 | 하나금융지주 | atlas/symbol_profiles/086/086790.json | atlas/ohlcv_tradable_by_symbol_year/086/086790/2024.csv | no corporate action candidates |
| 323410 | 카카오뱅크 | atlas/symbol_profiles/323/323410.json | atlas/ohlcv_tradable_by_symbol_year/323/323410/2024.csv | no corporate action candidates |

## 11. Case-by-Case Trigger Grid

|trigger_id|symbol|trigger_type|trigger_date|entry_date|entry_price|MFE_30D_pct|MFE_90D_pct|MFE_180D_pct|MAE_30D_pct|MAE_90D_pct|MAE_180D_pct|peak_date|peak_price|current_profile_verdict|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R6L10_C21_KB_STAGE2A_20240226|105560|Stage2-Actionable|2024-02-26|2024-02-26|62500|25.76|44.0|66.24|-4.48|-4.48|-4.48|2024-10-25|103900|current_profile_correct|
|R6L10_C21_HANA_STAGE2A_20240226|086790|Stage2-Actionable|2024-02-26|2024-02-26|55400|17.69|22.38|25.09|-4.69|-6.86|-6.86|2024-08-27|69300|current_profile_correct|
|R6L10_C21_KAKAOBANK_STAGE2A_20240226|323410|Stage2-Actionable_false_positive_test|2024-02-26|2024-02-26|30150|1.66|1.66|1.66|-17.74|-33.5|-38.67|2024-02-27|30650|current_profile_false_positive|


## 12. Trigger-Level OHLC Backtest Tables

Calculation rule:

```text
MFE_N_pct = (max high from entry_date through N trading rows / entry_price - 1) * 100
MAE_N_pct = (min low from entry_date through N trading rows / entry_price - 1) * 100
peak_price = max high in observed 180D window
drawdown_after_peak_pct = min low after peak_date through 180D / peak_price - 1
```

| symbol | entry close | 30D high/low | MFE30 / MAE30 | 90D high/low | MFE90 / MAE90 | 180D high/low | MFE180 / MAE180 | peak |
|---:|---:|---|---|---|---|---|---|---|
| 105560 | 62,500 | 78,600 / 59,700 | +25.76% / -4.48% | 90,000 / 59,700 | +44.00% / -4.48% | 103,900 / 59,700 | +66.24% / -4.48% | 2024-10-25, 103,900 |
| 086790 | 55,400 | 65,200 / 52,800 | +17.69% / -4.69% | 67,800 / 51,600 | +22.38% / -6.86% | 69,300 / 51,600 | +25.09% / -6.86% | 2024-08-27, 69,300 |
| 323410 | 30,150 | 30,650 / 24,800 | +1.66% / -17.74% | 30,650 / 20,050 | +1.66% / -33.50% | 30,650 / 18,490 | +1.66% / -38.67% | 2024-02-27, 30,650 |

## 13. Current Calibrated Profile Stress Test

| case | P0 likely treatment | actual path | verdict |
|---|---|---|---|
| KB금융 | Stage3-Yellow / possible Green buffer if capital-return execution recognized | +44.00% MFE90, +66.24% MFE180, -4.48% MAE180 | current_profile_correct |
| 하나금융지주 | Stage3-Yellow | +22.38% MFE90, +25.09% MFE180, -6.86% MAE180 | current_profile_correct |
| 카카오뱅크 | Stage3-Yellow false positive risk if policy and relative strength are over-weighted | +1.66% MFE180, -38.67% MAE180 | current_profile_false_positive |

Questions answered:

1. Current profile handles KB/Hana reasonably as Stage3-Yellow-type C21 positives.
2. Current profile can still over-score KakaoBank if sector-wide policy beta is allowed to substitute for capital-return execution.
3. Stage2 actionable bonus is not globally wrong; it is too permissive inside C21 when policy evidence is not paired with capital-return execution.
4. Yellow 75 is acceptable for KB/Hana but risky for KakaoBank unless C21 guard is added.
5. Green 87 / revision 55 should be kept; this loop does not argue for global Green relaxation.
6. Price-only blowoff guard remains appropriate.
7. Full 4B non-price requirement remains appropriate.
8. Hard 4C routing was not tested in this loop.

## 14. Stage2 / Yellow / Green Comparison

| case | Stage2 trigger | Stage3-Yellow proxy | Stage3-Green proxy | green_lateness_ratio |
|---|---:|---|---|---|
| KB금융 | 2024-02-26 policy+value-up route | P0 score 82 | P2 score 88 after capital-return execution weighting | not_applicable; no separate later Green trigger used |
| 하나금융지주 | 2024-02-26 policy+value-up route | P0 score 78 | not promoted to Green under P2 | not_applicable |
| 카카오뱅크 | 2024-02-26 policy beta false-positive test | P0 risk score 76 | blocked under P2/P3 | not_applicable |

This loop does not re-propose `stage2_actionable_evidence_bonus`. It proposes a C21-specific condition on what counts as actionable non-price evidence.

## 15. 4B Local vs Full-window Timing Audit

No full 4B trigger is proposed.

| symbol | local price peak | full 180D peak | non-price 4B evidence | four_b_timing_verdict |
|---:|---:|---:|---|---|
| 105560 | 2024-07-29 high 92,400 | 2024-10-25 high 103,900 | none | price_only_local_peak_not_full_4B |
| 086790 | 2024-07-03 high 67,800 | 2024-08-27 high 69,300 | none | price_only_local_peak_not_full_4B |
| 323410 | 2024-02-27 high 30,650 | 2024-02-27 high 30,650 | weak rerating base, not 4B | no_positive_thesis_to_overlay |

Existing axis tested: `full_4b_requires_non_price_evidence`
Verdict: `existing_axis_kept`

## 16. 4C Protection Audit

No hard 4C evidence row is used. KakaoBank is treated as a failed C21 rerating/counterexample, not a 4C thesis-break row.

| symbol | 4C label | reason |
|---:|---|---|
| 105560 | not_applicable | positive rerating path |
| 086790 | not_applicable | positive rerating path |
| 323410 | thesis_break_watch_only | C21 rerating thesis lacked execution evidence; do not route as hard 4C |

## 17. Sector-Specific Rule Candidate

```text
rule_scope = sector_specific
large_sector_id = L6_FINANCIAL_CAPITAL_RETURN_DIGITAL
axis = financial_value_up_policy_beta_execution_gate
proposal_type = shadow_only
```

Rule candidate:

> In L6 financial value-up research, a broad regulatory/value-up policy trigger may create Stage2 watch evidence, but it should not reach Stage3-Yellow unless at least one execution-quality field is present: low-PBR repricing base, explicit buyback/cancellation/dividend route, ROE improvement, or credible capital-return plan.

This is not a production patch.

## 18. Canonical-Archetype Rule Candidate

```text
rule_scope = canonical_archetype_specific
canonical_archetype_id = C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN
axis = policy_only_value_up_cap + capital_return_execution_weight
proposal_type = shadow_only
```

C21-specific guard:

```text
if policy_or_regulatory_score is high
and capital_return_execution_score <= 2
and roe_pbr_capital_return_score <= 2:
    cap Stage at Stage1/Stage2-watch
    do_not_allow_Stage3_Yellow_or_Green = true
```

C21-specific positive weight:

```text
if actual capital-return execution is visible
and low-PBR/ROE repricing base exists:
    add +2 to C21 capital_return_execution_weight
```

## 19. Before / After Backtest Comparison

|profile_id|scope|hypothesis|changed_axes|eligible_trigger_count|avg_MFE_90D_pct|avg_MAE_90D_pct|avg_MFE_180D_pct|avg_MAE_180D_pct|false_positive_rate|score_return_alignment_verdict|
|---|---|---|---|---|---|---|---|---|---|---|
|P0:e2r_2_1_stock_web_calibrated_proxy|current_global_proxy|Existing global calibrated profile; policy + relative strength can still over-score digital-bank policy beta.|none|3|22.68|-14.95|31.0|-16.67|1/3|mixed_positive_correct_counterexample_false_positive|
|P0b:e2r_2_0_baseline_reference|rollback_reference|Old baseline would under-separate policy beta from executed capital-return rerating.|rollback reference only|3|22.68|-14.95|31.0|-16.67|1/3|weaker_than_P0|
|P1:sector_specific_candidate_profile|L6_FINANCIAL_CAPITAL_RETURN_DIGITAL|Financial value-up Stage2 should require either low-PBR repricing base or explicit capital-return execution.|policy_beta_cap; capital_return_execution_gate|3|33.19|-5.67|45.66|-5.67|0/3|improved|
|P2:canonical_archetype_candidate_profile|C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN|C21 should weight actual capital-return execution and ROE/PBR rerating base above sector-wide value-up policy beta.|roe_pbr_capital_return_score +2; capital_return_execution_score +2; digital_high_pbr_no_execution_penalty -8|3|33.19|-5.67|45.66|-5.67|0/3|best_shadow_only|
|P3:counterexample_guard_profile|C21 guard|If policy/regulatory score is high but capital-return execution <=2 and ROE/PBR repricing base <=2, cap Stage at Stage1/Stage2-watch.|policy_only_value_up_cap|3|33.19|-5.67|45.66|-5.67|0/3|guard_effective|


## 20. Score-Return Alignment Matrix

| case | weighted_score_before | stage_before | weighted_score_after | stage_after | MFE180 | MAE180 | alignment |
|---|---:|---|---:|---|---:|---:|---|
| KB금융 | 82 | Stage3-Yellow | 88 | Stage3-Green | +66.24% | -4.48% | improved positive alignment |
| 하나금융지주 | 78 | Stage3-Yellow | 82 | Stage3-Yellow | +25.09% | -6.86% | kept positive alignment |
| 카카오뱅크 | 76 | Stage3-Yellow | 62 | Stage1/Stage2-watch | +1.66% | -38.67% | false positive removed |

## 21. Coverage Matrix

|large_sector_id|canonical_archetype_id|fine_archetype_id|positive_case_count|counterexample_count|4B_case_count|4C_case_count|new_independent_case_count|reused_case_count|calibration_usable_trigger_count|representative_trigger_count|current_profile_error_count|sector_rule_candidate|canonical_rule_candidate|coverage_gap_after_this_loop|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|L6_FINANCIAL_CAPITAL_RETURN_DIGITAL|C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN|VALUE_UP_BANK_ROE_PBR_CAPITAL_RETURN_VS_DIGITAL_PREMIUM_COUNTEREXAMPLE|2|1|0|0|3|0|3|3|1|True|True|C21 now has explicit policy-beta counterexample against broad value-up promotion.|


## 22. Residual Contribution Summary

```text
new_independent_case_count: 3
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 3
same_archetype_new_symbol_count: 3
same_archetype_new_trigger_family_count: 1
new_canonical_archetype_count: 0
new_fine_archetype_count: 1
new_trigger_family_count: 1
positive_case_count: 2
counterexample_count: 1
current_profile_error_count: 1
tested_existing_calibrated_axes:
  - stage2_actionable_evidence_bonus
  - stage3_yellow_total_min
  - stage3_green_total_min
  - price_only_blowoff_blocks_positive_stage
  - full_4b_requires_non_price_evidence
residual_error_types_found:
  - policy_beta_false_positive_in_C21_digital_high_PBR_bank
new_axis_proposed:
  - policy_only_value_up_cap
  - capital_return_execution_weight
existing_axis_strengthened: null
existing_axis_weakened: null
existing_axis_kept:
  - stage2_actionable_evidence_bonus
  - stage3_yellow_total_min
  - stage3_green_total_min
  - full_4b_requires_non_price_evidence
sector_specific_rule_candidate: true
canonical_archetype_rule_candidate: true
no_new_signal_reason: null
diversity_score_summary: high_total_52_avg_17.3
loop_contribution_label: canonical_archetype_rule_candidate
do_not_propose_new_weight_delta: false
```

## 23. Validation Scope / Non-Validation Scope

Validation scope:

- Historical trigger date: 2024-02-26
- Price source validation: `Songdaiki/stock-web`
- OHLC windows: 30D, 90D, 180D
- Clean profiles: no corporate action candidates for selected symbols
- Score simulation: research proxy only
- Rule proposal: sector/canonical-archetype shadow only

Non-validation scope:

- No current/live candidate scan
- No investment recommendation
- No production scoring change
- No stock_agent code access
- No brokerage/API/autotrading
- No 2Y quantitative calibration
- No hard 4C production routing

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,policy_only_value_up_cap,canonical_archetype_specific,L6_FINANCIAL_CAPITAL_RETURN_DIGITAL,C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN,none,cap_policy_score_when_no_capital_return_execution,-5_to_-8,"Policy beta without low-PBR/capital-return execution created a high-MAE false positive in KakaoBank while KB/Hana retained positive alignment.","false_positive_rate 1/3 -> 0/3 in this small holdout","R6L10_C21_KB_STAGE2A_20240226|R6L10_C21_HANA_STAGE2A_20240226|R6L10_C21_KAKAOBANK_STAGE2A_20240226",3,3,1,low,canonical_archetype_shadow_only,"not production; post-calibrated residual"
shadow_weight,capital_return_execution_weight,canonical_archetype_specific,L6_FINANCIAL_CAPITAL_RETURN_DIGITAL,C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN,0,+2,+2,"Executed buyback/cancellation/dividend route better separated KB/Hana from policy-only digital-bank beta.","positive average MFE180 45.67 vs counterexample MFE180 1.66","R6L10_C21_KB_STAGE2A_20240226|R6L10_C21_HANA_STAGE2A_20240226|R6L10_C21_KAKAOBANK_STAGE2A_20240226",3,3,1,low,canonical_archetype_shadow_only,"not production; requires more C21 samples before promotion"
```

## 25. Machine-Readable Rows

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration"}
{"row_type": "case", "case_id": "R6L10_C21_KB_20240226", "symbol": "105560", "company_name": "KB금융", "round": "R6", "loop": "10", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "fine_archetype_id": "VALUE_UP_BANK_ROE_PBR_CAPITAL_RETURN_VS_DIGITAL_PREMIUM_COUNTEREXAMPLE", "case_type": "structural_success", "positive_or_counterexample": "positive", "best_trigger": "R6L10_C21_KB_STAGE2A_20240226", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "aligned", "current_profile_verdict": "current_profile_correct", "price_source": "Songdaiki/stock-web", "notes": "Corporate Value-up policy trigger plus low-PBR bank capital-return execution route; price row from 2024-02-26 close."}
{"row_type": "case", "case_id": "R6L10_C21_HANA_20240226", "symbol": "086790", "company_name": "하나금융지주", "round": "R6", "loop": "10", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "fine_archetype_id": "VALUE_UP_BANK_ROE_PBR_CAPITAL_RETURN_VS_DIGITAL_PREMIUM_COUNTEREXAMPLE", "case_type": "structural_success", "positive_or_counterexample": "positive", "best_trigger": "R6L10_C21_HANA_STAGE2A_20240226", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "aligned", "current_profile_verdict": "current_profile_correct", "price_source": "Songdaiki/stock-web", "notes": "Corporate Value-up policy trigger plus low-PBR bank capital-return execution route; price row from 2024-02-26 close."}
{"row_type": "case", "case_id": "R6L10_C21_KAKAOBANK_20240226", "symbol": "323410", "company_name": "카카오뱅크", "round": "R6", "loop": "10", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "fine_archetype_id": "VALUE_UP_BANK_ROE_PBR_CAPITAL_RETURN_VS_DIGITAL_PREMIUM_COUNTEREXAMPLE", "case_type": "failed_rerating", "positive_or_counterexample": "counterexample", "best_trigger": "R6L10_C21_KAKAOBANK_STAGE2A_20240226", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "counterexample_aligned_after_guard", "current_profile_verdict": "current_profile_false_positive", "price_source": "Songdaiki/stock-web", "notes": "Sector-wide policy beta without confirmed low-PBR/capital-return execution; used as C21 counterexample guard."}
{"row_type": "trigger", "trigger_id": "R6L10_C21_KB_STAGE2A_20240226", "case_id": "R6L10_C21_KB_20240226", "symbol": "105560", "company_name": "KB금융", "round": "R6", "loop": "10", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "fine_archetype_id": "VALUE_UP_BANK_ROE_PBR_CAPITAL_RETURN_VS_DIGITAL_PREMIUM_COUNTEREXAMPLE", "sector": "금융·자본배분·디지털금융", "primary_archetype": "financial_ROE_PBR_capital_return", "loop_objective": "counterexample_mining|sector_specific_rule_discovery|canonical_archetype_compression", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-02-26", "entry_date": "2024-02-26", "entry_price": 62500, "evidence_available_at_that_date": "2024-02-26 Corporate Value-up program public announcement; treated as same-day close policy trigger", "evidence_source": "public_policy_news_and_stock_web_price_row", "stage2_evidence_fields": ["policy_or_regulatory_optionality", "relative_strength", "valuation_repricing_base"], "stage3_evidence_fields": ["financial_visibility", "capital_return_execution"], "stage4b_evidence_fields": [], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/105/105560/2024.csv", "profile_path": "atlas/symbol_profiles/105/105560.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 25.76, "MFE_90D_pct": 44.0, "MFE_180D_pct": 66.24, "MFE_1Y_pct": "not_primary_in_this_loop", "MFE_2Y_pct": "unavailable_by_manifest_forward_window", "MAE_30D_pct": -4.48, "MAE_90D_pct": -4.48, "MAE_180D_pct": -4.48, "MAE_1Y_pct": "not_primary_in_this_loop", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-10-25", "peak_price": 103900, "drawdown_after_peak_pct": -15.5, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "no_full_4B_trigger", "four_b_evidence_type": [], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "structural_success_high_MFE_low_MAE", "current_profile_verdict": "current_profile_correct", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R6L10_C21_KB_20240226_2024-02-26_62500", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "R6L10_C21_HANA_STAGE2A_20240226", "case_id": "R6L10_C21_HANA_20240226", "symbol": "086790", "company_name": "하나금융지주", "round": "R6", "loop": "10", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "fine_archetype_id": "VALUE_UP_BANK_ROE_PBR_CAPITAL_RETURN_VS_DIGITAL_PREMIUM_COUNTEREXAMPLE", "sector": "금융·자본배분·디지털금융", "primary_archetype": "financial_ROE_PBR_capital_return", "loop_objective": "counterexample_mining|sector_specific_rule_discovery|canonical_archetype_compression", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-02-26", "entry_date": "2024-02-26", "entry_price": 55400, "evidence_available_at_that_date": "2024-02-26 Corporate Value-up program public announcement; treated as same-day close policy trigger", "evidence_source": "public_policy_news_and_stock_web_price_row", "stage2_evidence_fields": ["policy_or_regulatory_optionality", "relative_strength", "valuation_repricing_base"], "stage3_evidence_fields": ["financial_visibility", "capital_return_execution"], "stage4b_evidence_fields": [], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/086/086790/2024.csv", "profile_path": "atlas/symbol_profiles/086/086790.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 17.69, "MFE_90D_pct": 22.38, "MFE_180D_pct": 25.09, "MFE_1Y_pct": "not_primary_in_this_loop", "MFE_2Y_pct": "unavailable_by_manifest_forward_window", "MAE_30D_pct": -4.69, "MAE_90D_pct": -6.86, "MAE_180D_pct": -6.86, "MAE_1Y_pct": "not_primary_in_this_loop", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-08-27", "peak_price": 69300, "drawdown_after_peak_pct": -17.89, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "no_full_4B_trigger", "four_b_evidence_type": [], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "structural_success_moderate_MFE_controlled_MAE", "current_profile_verdict": "current_profile_correct", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R6L10_C21_HANA_20240226_2024-02-26_55400", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "R6L10_C21_KAKAOBANK_STAGE2A_20240226", "case_id": "R6L10_C21_KAKAOBANK_20240226", "symbol": "323410", "company_name": "카카오뱅크", "round": "R6", "loop": "10", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "fine_archetype_id": "VALUE_UP_BANK_ROE_PBR_CAPITAL_RETURN_VS_DIGITAL_PREMIUM_COUNTEREXAMPLE", "sector": "금융·자본배분·디지털금융", "primary_archetype": "financial_ROE_PBR_capital_return", "loop_objective": "counterexample_mining|sector_specific_rule_discovery|canonical_archetype_compression", "trigger_type": "Stage2-Actionable_false_positive_test", "trigger_date": "2024-02-26", "entry_date": "2024-02-26", "entry_price": 30150, "evidence_available_at_that_date": "2024-02-26 Corporate Value-up program public announcement; treated as same-day close policy trigger", "evidence_source": "public_policy_news_and_stock_web_price_row", "stage2_evidence_fields": ["policy_or_regulatory_optionality", "relative_strength", "valuation_repricing_base"], "stage3_evidence_fields": [], "stage4b_evidence_fields": [], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/323/323410/2024.csv", "profile_path": "atlas/symbol_profiles/323/323410.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 1.66, "MFE_90D_pct": 1.66, "MFE_180D_pct": 1.66, "MFE_1Y_pct": "not_primary_in_this_loop", "MFE_2Y_pct": "unavailable_by_manifest_forward_window", "MAE_30D_pct": -17.74, "MAE_90D_pct": -33.5, "MAE_180D_pct": -38.67, "MAE_1Y_pct": "not_primary_in_this_loop", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-02-27", "peak_price": 30650, "drawdown_after_peak_pct": -39.67, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "no_full_4B_trigger", "four_b_evidence_type": [], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "policy_beta_false_positive_high_MAE_no_rerating", "current_profile_verdict": "current_profile_false_positive", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R6L10_C21_KAKAOBANK_20240226_2024-02-26_30150", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R6L10_C21_KB_20240226", "trigger_id": "R6L10_C21_KB_STAGE2A_20240226", "symbol": "105560", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 7, "revision_score": 6, "relative_strength_score": 8, "customer_quality_score": 0, "policy_or_regulatory_score": 8, "valuation_repricing_score": 9, "execution_risk_score": 2, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "roe_pbr_capital_return_score": 8, "capital_return_execution_score": 8}, "weighted_score_before": 82, "stage_label_before": "Stage3-Yellow", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 7, "revision_score": 7, "relative_strength_score": 8, "customer_quality_score": 0, "policy_or_regulatory_score": 8, "valuation_repricing_score": 9, "execution_risk_score": 2, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "roe_pbr_capital_return_score": 9, "capital_return_execution_score": 9}, "weighted_score_after": 88, "stage_label_after": "Stage3-Green", "changed_components": ["roe_pbr_capital_return_score", "capital_return_execution_score", "policy_or_regulatory_score_cap"], "component_delta_explanation": "C21 shadow profile separates broad policy beta from executed capital-return/ROE-PBR rerating evidence.", "MFE_90D_pct": 44.0, "MAE_90D_pct": -4.48, "score_return_alignment_label": "aligned_positive", "current_profile_verdict": "current_profile_correct"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R6L10_C21_HANA_20240226", "trigger_id": "R6L10_C21_HANA_STAGE2A_20240226", "symbol": "086790", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 6, "revision_score": 5, "relative_strength_score": 7, "customer_quality_score": 0, "policy_or_regulatory_score": 8, "valuation_repricing_score": 8, "execution_risk_score": 3, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "roe_pbr_capital_return_score": 7, "capital_return_execution_score": 7}, "weighted_score_before": 78, "stage_label_before": "Stage3-Yellow", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 6, "revision_score": 6, "relative_strength_score": 7, "customer_quality_score": 0, "policy_or_regulatory_score": 8, "valuation_repricing_score": 8, "execution_risk_score": 3, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "roe_pbr_capital_return_score": 8, "capital_return_execution_score": 8}, "weighted_score_after": 82, "stage_label_after": "Stage3-Yellow", "changed_components": ["roe_pbr_capital_return_score", "capital_return_execution_score", "policy_or_regulatory_score_cap"], "component_delta_explanation": "C21 shadow profile separates broad policy beta from executed capital-return/ROE-PBR rerating evidence.", "MFE_90D_pct": 22.38, "MAE_90D_pct": -6.86, "score_return_alignment_label": "aligned_positive", "current_profile_verdict": "current_profile_correct"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R6L10_C21_KAKAOBANK_20240226", "trigger_id": "R6L10_C21_KAKAOBANK_STAGE2A_20240226", "symbol": "323410", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 4, "revision_score": 3, "relative_strength_score": 5, "customer_quality_score": 0, "policy_or_regulatory_score": 8, "valuation_repricing_score": 4, "execution_risk_score": 6, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "roe_pbr_capital_return_score": 2, "capital_return_execution_score": 1}, "weighted_score_before": 76, "stage_label_before": "Stage3-Yellow", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 3, "revision_score": 2, "relative_strength_score": 2, "customer_quality_score": 0, "policy_or_regulatory_score": 3, "valuation_repricing_score": 2, "execution_risk_score": 8, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "roe_pbr_capital_return_score": 1, "capital_return_execution_score": 0}, "weighted_score_after": 62, "stage_label_after": "Stage1/Stage2-watch", "changed_components": ["roe_pbr_capital_return_score", "capital_return_execution_score", "policy_or_regulatory_score_cap"], "component_delta_explanation": "C21 shadow profile separates broad policy beta from executed capital-return/ROE-PBR rerating evidence.", "MFE_90D_pct": 1.66, "MAE_90D_pct": -33.5, "score_return_alignment_label": "current_false_positive_guarded_after", "current_profile_verdict": "current_profile_false_positive"}
{"row_type": "residual_contribution", "round": "R6", "loop": "10", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "new_independent_case_count": 3, "reused_case_count": 0, "new_symbol_count": 3, "same_archetype_new_symbol_count": 3, "same_archetype_new_trigger_family_count": 1, "new_canonical_archetype_count": 0, "new_trigger_family_count": 1, "positive_case_count": 2, "counterexample_count": 1, "current_profile_error_count": 1, "tested_existing_calibrated_axes": ["stage2_actionable_evidence_bonus", "stage3_yellow_total_min", "stage3_green_total_min", "price_only_blowoff_blocks_positive_stage"], "residual_error_types_found": ["policy_beta_false_positive_in_C21_digital_high_PBR_bank"], "diversity_score_summary": "high_total_52_avg_17.3", "loop_contribution_label": "canonical_archetype_rule_candidate", "do_not_propose_new_weight_delta": false, "auto_selected_coverage_gap": "R6 had prior loops but no symbol-level representative rows available; selected C21 counterexample balance and policy-beta residual error."}
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
next_round_candidate = R7 or R5 depending on next coverage gap
recommended_next_objective = add 4B/4C case for C21 or test C22 insurance ROE/capital-return cycle
avoid_next = repeating 2024-02-26 KB/Hana/KakaoBank policy trigger without new evidence family
```

## 28. Source Notes

- `stock_agent` allowed artifact: `reports/e2r_calibration/ingest_summary.md`
- `stock_agent` allowed artifact: `reports/e2r_calibration/applied_scoring_diff.md`
- `stock_agent` allowed artifact: `reports/e2r_calibration/calibrated_profile_report.md`
- `stock_agent` allowed artifact: `data/e2r/calibration/md_registry.jsonl`
- `stock-web` price atlas manifest: `atlas/manifest.json`
- `stock-web` schema: `atlas/schema.json`
- `stock-web` symbol profiles:
  - `atlas/symbol_profiles/105/105560.json`
  - `atlas/symbol_profiles/086/086790.json`
  - `atlas/symbol_profiles/323/323410.json`
- `stock-web` price shards:
  - `atlas/ohlcv_tradable_by_symbol_year/105/105560/2024.csv`
  - `atlas/ohlcv_tradable_by_symbol_year/086/086790/2024.csv`
  - `atlas/ohlcv_tradable_by_symbol_year/323/323410/2024.csv`
- Public evidence context:
  - Korea Corporate Value-up program and shareholder-return policy reporting around 2024-02-26.
  - Reuters 2024-02-28 and 2024-03-14 reports on Korea Value-up follow-up and possible shareholder-return penalties.
