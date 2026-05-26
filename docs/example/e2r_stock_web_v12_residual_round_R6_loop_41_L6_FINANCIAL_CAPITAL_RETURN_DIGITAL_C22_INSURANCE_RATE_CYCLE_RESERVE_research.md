# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

- research_session: `post_calibrated_sector_archetype_residual_research`
- mode: `historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12`
- round: `R6`
- loop: `41`
- output_file: `e2r_stock_web_v12_residual_round_R6_loop_41_L6_FINANCIAL_CAPITAL_RETURN_DIGITAL_C22_INSURANCE_RATE_CYCLE_RESERVE_research.md`
- live_candidate_mode: `false`
- stock_agent_code_access_allowed: `false`
- stock_agent_code_patch_allowed: `false`
- production_scoring_changed: `false`
- shadow_weight_only: `true`
- handoff_prompt_embedded: `true`
- handoff_prompt_executed_now: `false`

## 1. Current Calibrated Profile Assumption

Current default proxy: `e2r_2_1_stock_web_calibrated_proxy`.

Existing global axes treated as already applied:
`stage2_actionable_evidence_bonus`, `stage3_yellow_total_min`, `stage3_green_total_min`,
`stage3_green_revision_min`, `stage3_cross_evidence_green_buffer`,
`price_only_blowoff_blocks_positive_stage`, `full_4b_requires_non_price_evidence`,
`hard_4c_thesis_break_routes_to_4c`.

This loop does not re-prove the global Stage2 or 4B thesis. It tests the residual C22 insurance-specific question:
**does value-up / financial-sector policy beta work for insurers without IFRS17 reserve-quality, K-ICS/capital adequacy, and explicit capital-return confirmation?**

## 2. Round / Large Sector / Canonical Archetype Scope

- large_sector_id: `L6_FINANCIAL_CAPITAL_RETURN_DIGITAL`
- canonical_archetype_id: `C22_INSURANCE_RATE_CYCLE_RESERVE`
- fine_archetype_id:
  - `INSURANCE_IFRS17_CSM_KICS_CAPITAL_RETURN`
  - `INSURANCE_IFRS17_ROE_CAPITAL_RETURN`
  - `LIFE_INSURER_POLICY_BETA_WITHOUT_CAPITAL_RETURN_CONFIRMATION`
- loop_objective:
  - `coverage_gap_fill`
  - `counterexample_mining`
  - `residual_false_positive_mining`
  - `sector_specific_rule_discovery`
  - `canonical_archetype_compression`
  - `4B_non_price_requirement_stress_test`
  - `4C_thesis_break_timing_test`

## 3. Previous Coverage / Duplicate Avoidance Check

Allowed artifact check found the calibration ingest universe already covers R1-R13 and loops 1-9, but a repository search for `C22_INSURANCE_RATE_CYCLE_RESERVE` returned no direct hit in the accessible research artifacts during this run. This loop therefore selects C22 as an auto coverage gap rather than repeating the prior C21 banking value-up file.

Diversity outcome:

- new_independent_case_count: `3`
- reused_case_count: `0`
- new_symbol_count: `3`
- same_archetype_new_symbol_count: `3`
- same_archetype_new_trigger_family_count: `5`
- counterexample_count: `1`
- minimum_new_independent_case_ratio: `1.00`

## 4. Stock-Web OHLC Input / Price Source Validation

Manifest values read from `Songdaiki/stock-web`:

- source_name: `FinanceData/marcap`
- source_repo_url: `https://github.com/FinanceData/marcap`
- price_adjustment_status: `raw_unadjusted_marcap`
- min_date: `1995-05-02`
- max_date: `2026-02-20`
- tradable_row_count: `14354401`
- raw_row_count: `15214118`
- symbol_count: `5414`
- active_like_symbol_count: `2868`
- inactive_or_delisted_like_symbol_count: `2546`
- markets: `KONEX, KOSDAQ, KOSDAQ GLOBAL, KOSPI`
- calibration_shard_root: `atlas/ohlcv_tradable_by_symbol_year`
- raw_shard_root: `atlas/ohlcv_raw_by_symbol_year`
- schema_path: `atlas/schema.json`
- universe_path: `atlas/universe/all_symbols.csv`

All quantitative rows use `tradable_raw` rows from `atlas/ohlcv_tradable_by_symbol_year`.

## 5. Historical Eligibility Gate

All representative rows pass:

- trigger_date is historical.
- entry_date exists in the stock-web tradable shard.
- 180 trading-day forward window exists before manifest max date.
- OHLCV fields exist.
- No corporate-action candidate date overlaps each 2024/2025 evaluation window.

Corporate-action note:

- `000810` profile has historical corporate-action candidate dates in 1999-2000 only; the 2024 windows are clean.
- `005830` profile has a historical corporate-action candidate date in 1999 only; the 2024 windows are clean.
- `088350` profile has no corporate-action candidate dates.

## 6. Canonical Archetype Compression Map

| fine_archetype_id | canonical_archetype_id | compression note |
|---|---|---|
| INSURANCE_IFRS17_CSM_KICS_CAPITAL_RETURN | C22_INSURANCE_RATE_CYCLE_RESERVE | reserve quality + capital return confirmation |
| INSURANCE_IFRS17_ROE_CAPITAL_RETURN | C22_INSURANCE_RATE_CYCLE_RESERVE | ROE/PBR rerating with shareholder return bridge |
| LIFE_INSURER_POLICY_BETA_WITHOUT_CAPITAL_RETURN_CONFIRMATION | C22_INSURANCE_RATE_CYCLE_RESERVE | counterexample guard: policy-only beta is not sufficient |

## 7. Case Selection Summary

| case_id | symbol | company_name | role | positive_or_counterexample | fine | current_profile_verdict |
| --- | --- | --- | --- | --- | --- | --- |
| R6L41_C22_000810_SFM_CAPITAL_RETURN_IFRS17 | 000810 | 삼성화재 | structural_success | positive | INSURANCE_IFRS17_CSM_KICS_CAPITAL_RETURN | current_profile_correct |
| R6L41_C22_005830_DBI_CAPITAL_RETURN_ROE | 005830 | DB손해보험 | structural_success | positive | INSURANCE_IFRS17_ROE_CAPITAL_RETURN | current_profile_correct |
| R6L41_C22_088350_HWL_POLICY_ONLY_FALSE_POSITIVE | 088350 | 한화생명 | failed_rerating | counterexample | LIFE_INSURER_POLICY_BETA_WITHOUT_CAPITAL_RETURN_CONFIRMATION | current_profile_false_positive |

## 8. Positive vs Counterexample Balance

- positive_case_count: `2`
- counterexample_count: `1`
- 4B_case_count: `2`
- 4C_case_count: `1`

Interpretation:

- Samsung Fire and DB Insurance show that C22 can work when insurance-specific quality bridge exists.
- Hanwha Life shows that financial value-up policy beta without confirmed capital-return/reserve-quality bridge can become a false Stage2/Yellow promotion.

## 9. Evidence Source Map

Evidence-source exact URLs were not resolved in this run; the event dates are treated as **historical public-event proxies** anchored to FY2023 / 1Q2024 insurance result and value-up windows. Price rows are verified directly through stock-web. During later ingestion, the coding agent should validate DART/IR URLs before accepting any non-price evidence delta.

| case_id | evidence family | validation status |
|---|---|---|
| R6L41_C22_000810_SFM_CAPITAL_RETURN_IFRS17 | IFRS17 result, CSM/capital adequacy, capital-return expectation | evidence URL pending; price verified |
| R6L41_C22_005830_DBI_CAPITAL_RETURN_ROE | IFRS17 result, ROE/PBR, capital-return bridge | evidence URL pending; price verified |
| R6L41_C22_088350_HWL_POLICY_ONLY_FALSE_POSITIVE | policy-only / value-up beta without company bridge | evidence URL pending; price verified |

## 10. Price Data Source Map

| symbol | company_name | profile_path | representative price_shard_path | profile caveat |
|---|---|---|---|---|
| 000810 | 삼성화재 | atlas/symbol_profiles/000/000810.json | atlas/ohlcv_tradable_by_symbol_year/000/000810/2024.csv | historical corporate action candidates outside 2024 window |
| 005830 | DB손해보험 | atlas/symbol_profiles/005/005830.json | atlas/ohlcv_tradable_by_symbol_year/005/005830/2024.csv | historical corporate action candidate outside 2024 window |
| 088350 | 한화생명 | atlas/symbol_profiles/088/088350.json | atlas/ohlcv_tradable_by_symbol_year/088/088350/2024.csv | clean profile |

## 11. Case-by-Case Trigger Grid

| trigger_id | symbol | trigger_type | trigger_date | entry_date | entry_price | MFE30 | MFE90 | MFE180 | MAE30 | MAE90 | MAE180 | current | outcome |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| R6L41_C22_000810_T1_STAGE2A | 000810 | Stage2-Actionable | 2024-02-22 | 2024-02-23 | 308500 | 12.16 | 27.55 | 27.55 | -7.46 | -11.67 | -11.67 | current_profile_correct | structural_success |
| R6L41_C22_000810_T2_GREEN_COMPARE | 000810 | Stage3-Green comparison | 2024-05-14 | 2024-05-16 | 370000 | 2.7 | 6.35 | 17.57 | -12.43 | -12.43 | -12.43 | current_profile_too_late | late_green_but_still_positive |
| R6L41_C22_000810_T3_4B_LOCAL | 000810 | Stage4B local overlay | 2024-06-28 | 2024-06-28 | 389000 | 1.16 | 1.16 | 11.83 | -16.71 | -16.71 | -16.71 | current_profile_4B_too_early | 4B_too_early |
| R6L41_C22_005830_T1_STAGE2A | 005830 | Stage2-Actionable | 2024-02-22 | 2024-02-23 | 97800 | 12.47 | 23.42 | 26.79 | -6.85 | -11.86 | -11.86 | current_profile_correct | structural_success |
| R6L41_C22_005830_T2_GREEN_COMPARE | 005830 | Stage3-Green comparison | 2024-05-14 | 2024-05-16 | 111500 | 3.5 | 11.21 | 11.21 | -15.61 | -15.61 | -18.03 | current_profile_too_late | late_green_but_still_positive |
| R6L41_C22_005830_T3_4B_FULL | 005830 | Stage4B full-window overlay | 2024-08-22 | 2024-08-22 | 120600 | 2.82 | 2.82 | 2.82 | -12.02 | -15.75 | -24.21 | current_profile_correct | 4B_overlay_success |
| R6L41_C22_088350_T1_STAGE2_POLICY_ONLY | 088350 | Stage2 policy-only stress | 2024-02-22 | 2024-02-23 | 3385 | 3.84 | 3.84 | 3.84 | -17.13 | -23.78 | -24.52 | current_profile_false_positive | failed_rerating |
| R6L41_C22_088350_T2_4C_WATCH | 088350 | Stage4C protection watch | 2024-11-14 | 2024-11-14 | 2595 | 7.13 | 9.44 | 9.44 | -5.97 | -6.36 | -6.36 | current_profile_4C_too_late | 4C_success |

## 12. Trigger-Level OHLC Backtest Tables

### Representative calibration rows

| symbol | entry_date | entry_price | 30D MFE/MAE | 90D MFE/MAE | 180D MFE/MAE | 1Y MFE/MAE | verdict |
|---|---:|---:|---:|---:|---:|---:|---|
| 000810 | 2024-02-23 | 308500 | +12.16 / -7.46 | +27.55 / -11.67 | +27.55 / -11.67 | +38.57 / -11.67 | positive |
| 005830 | 2024-02-23 | 97800 | +12.47 / -6.85 | +23.42 / -11.86 | +26.79 / -11.86 | +26.79 / -11.86 | positive |
| 088350 | 2024-02-23 | 3385 | +3.84 / -17.13 | +3.84 / -23.78 | +3.84 / -24.52 | +3.84 / -27.92 | counterexample |

## 13. Current Calibrated Profile Stress Test

1. `000810`: current profile likely accepts as Stage2A/Yellow and later Green. Directionally correct, but Green confirmation is late.
2. `005830`: current profile likely accepts as Stage2A/Yellow and later Green. Directionally correct; 4B full-window overlay is useful.
3. `088350`: if policy/regulatory beta is overweighted, current profile can create a false positive. Actual MFE/MAE says this should remain watch-only.

Answers to required axes:

- Stage2 bonus: kept, but C22-specific qualification needed.
- Yellow threshold 75: okay only when reserve/capital-return bridge exists.
- Green threshold 87 / revision 55: okay, but Green can be late in insurance rerating.
- price-only blowoff guard: strengthened; local price-only peak cannot be full 4B.
- full 4B non-price requirement: strengthened.
- hard 4C routing: strengthened for policy-only failure after thesis non-confirmation.

## 14. Stage2 / Yellow / Green Comparison

| symbol | Stage2A entry | Stage3 Green entry | peak used | green_lateness_ratio | interpretation |
|---|---:|---:|---:|---:|---|
| 000810 | 308500 | 370000 | 393500 | 0.724 | Green caught confirmation, but most upside from Stage2A to local peak was already consumed. |
| 005830 | 97800 | 111500 | 124000 | 0.523 | Green was late but still before full observed-cycle peak. |
| 088350 | 3385 | no valid Green | 3515 | not_applicable | No confirmed positive Green; policy-only Stage2 should be capped. |

## 15. 4B Local vs Full-window Timing Audit

| symbol | 4B trigger | local proximity | full-window proximity | verdict |
|---|---|---:|---:|---|
| 000810 | 2024-06-28 local high | 0.947 | 0.636 | price-only local 4B too early |
| 005830 | 2024-08-22 full-window high | 0.870 | 0.870 | good full-window 4B timing |
| 088350 | 2024-02-23 policy-only local high | 1.000 | 1.000 | price-only local high is not positive evidence |

## 16. 4C Protection Audit

| symbol | 4C trigger | protection label | comment |
|---|---|---|---|
| 088350 | 2024-11-14 | hard_4c_success | policy-only thesis had failed to become capital-return/quality evidence; watch-only 4C would reduce further capital lock-up. |
| 000810 | none | thesis_break_watch_only | local 4B was too early; no hard 4C in this loop. |
| 005830 | none | hard_4c_watch | 4B overlay was more useful than hard 4C. |

## 17. Sector-Specific Rule Candidate

`L6_FINANCIAL_CAPITAL_RETURN_DIGITAL` shadow rule:

> Financial-sector policy beta may create Stage2-watch, but Stage2-Actionable/Yellow promotion needs sector-specific capital implementation evidence. For insurers, the implementation evidence is not CET1 alone; it is IFRS17 reserve quality, CSM/new business margin, K-ICS/capital adequacy, and shareholder-return bridge.

rule_scope: `sector_specific`

## 18. Canonical-Archetype Rule Candidate

`C22_INSURANCE_RATE_CYCLE_RESERVE` shadow rule:

> Promote C22 only when `policy_or_regulatory_score` is paired with at least one of `reserve_quality_score`, `kics_or_capital_adequacy_score`, or `roe_pbr_capital_return_score`. If policy beta exists alone, cap at Stage2-watch / no positive promotion.

rule_scope: `canonical_archetype_specific`

## 19. Before / After Backtest Comparison

| profile_id | profile_scope | profile_hypothesis | changed_axes | eligible_trigger_count | avg_MFE_90D_pct | avg_MAE_90D_pct | avg_MFE_180D_pct | avg_MAE_180D_pct | false_positive_rate | score_return_alignment_verdict |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| P0 | current_default_proxy | Current profile works for insurers only when capital-return/reserve-quality evidence exists; policy-only remains residual false positive. | none | 3 | 18.27 | -15.77 | 19.39 | -16.02 | 1/3 | mixed; one policy-only false positive |
| P0b | rollback_reference | Baseline is looser and less able to separate policy beta from insurer-specific capital quality. | none | 3 | 18.27 | -15.77 | 19.39 | -16.02 | 1/3+ | weaker |
| P1 | sector_specific_candidate | Financial-sector profile requires shareholder-return implementation bridge or capital-quality confirmation. | capital_return_confirmation, policy_only_cap | 2 | 25.49 | -11.77 | 27.17 | -11.77 | 0/2 selected entries | improved |
| P2 | canonical_archetype_specific | C22-specific guard: IFRS17/CSM/K-ICS/capital-return confirmation must close; policy-only cannot promote. | C22 IFRS17/CSM/K-ICS/capital-return gate | 2 | 25.49 | -11.77 | 27.17 | -11.77 | 0/3 after guard | best for this loop |
| P3 | counterexample_guard | Counterexample guard caps policy-only life-insurer beta below Yellow unless reserve/capital-return evidence is present. | policy-only no-cap guard | 3 | 25.49 | -11.77 | 27.17 | -11.77 | 0/3 after guard | protective |

## 20. Score-Return Alignment Matrix

| case | current profile | proposed shadow profile | actual 180D return path | alignment |
|---|---|---|---|---|
| 000810 | Stage2A/Yellow correct, Green late | qualified C22 Stage2A retained | MFE +27.55 / MAE -11.67 | aligned |
| 005830 | Stage2A/Yellow correct, Green late | qualified C22 Stage2A retained | MFE +26.79 / MAE -11.86 | aligned |
| 088350 | policy-only false positive risk | cap to watch-only | MFE +3.84 / MAE -24.52 | improved |

## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive_case_count | counterexample_count | 4B_case_count | 4C_case_count | new_independent_case_count | reused_case_count | calibration_usable_trigger_count | representative_trigger_count | current_profile_error_count | sector_rule_candidate | canonical_rule_candidate | coverage_gap_after_this_loop |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| L6_FINANCIAL_CAPITAL_RETURN_DIGITAL | C22_INSURANCE_RATE_CYCLE_RESERVE | mixed | 2 | 1 | 2 | 1 | 3 | 0 | 8 | 3 | 1 | true | true | needs insurer holdout with 032830 / 001450 / 000370 |

## 22. Residual Contribution Summary

new_independent_case_count: 3  
reused_case_count: 0  
reused_case_ids: []  
new_symbol_count: 3  
same_archetype_new_symbol_count: 3  
same_archetype_new_trigger_family_count: 5  
new_canonical_archetype_count: 1  
new_fine_archetype_count: 3  
new_trigger_family_count: 5  
tested_existing_calibrated_axes: stage2_actionable_evidence_bonus, stage3_yellow_total_min, stage3_green_total_min, stage3_green_revision_min, price_only_blowoff_blocks_positive_stage, full_4b_requires_non_price_evidence, hard_4c_thesis_break_routes_to_4c  
residual_error_types_found: policy_only_financial_beta_false_positive, local_4B_too_early_without_non_price_evidence, green_late_in_insurer_capital_return_cycle  
new_axis_proposed: C22_capital_return_confirmation_bonus; C22_policy_only_no_cap_guard  
existing_axis_strengthened: full_4b_requires_non_price_evidence; hard_4c_thesis_break_routes_to_4c  
existing_axis_weakened: none  
existing_axis_kept: stage2_actionable_evidence_bonus; yellow/green thresholds  
sector_specific_rule_candidate: true  
canonical_archetype_rule_candidate: true  
no_new_signal_reason: null  

loop_contribution_label: canonical_archetype_rule_candidate  
do_not_propose_new_weight_delta: false

## 23. Validation Scope / Non-Validation Scope

Validated:

- stock-web manifest fields
- profile paths and corporate-action window status
- tradable raw OHLC rows for all price calculations
- 30D/90D/180D MFE/MAE calculations

Not validated in this run:

- exact DART filing URLs
- exact intraday disclosure timestamp
- current/live candidate status
- production scoring code

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,C22_capital_return_confirmation_bonus,canonical_archetype_specific,L6_FINANCIAL_CAPITAL_RETURN_DIGITAL,C22_INSURANCE_RATE_CYCLE_RESERVE,0,1,+1,"Insurer Stage2A works when capital-return/reserve-quality bridge is explicit; Samsung Fire and DB Insurance both delivered >25% 180D MFE from Stage2A.","raise qualified Stage2A/Yellow alignment","R6L41_C22_000810_T1_STAGE2A|R6L41_C22_005830_T1_STAGE2A",3,3,1,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,C22_policy_only_no_cap_guard,canonical_archetype_specific,L6_FINANCIAL_CAPITAL_RETURN_DIGITAL,C22_INSURANCE_RATE_CYCLE_RESERVE,0,1,+1,"Life-insurer policy beta without capital-return/reserve bridge produced high MAE and weak MFE in Hanwha Life.","blocks false Yellow/Green promotion","R6L41_C22_088350_T1_STAGE2_POLICY_ONLY",3,3,1,medium,counterexample_guard,"not production; cap policy-only Stage2 below Yellow"
shadow_weight,C22_full_4B_non_price_confirmation,canonical_archetype_specific,L6_FINANCIAL_CAPITAL_RETURN_DIGITAL,C22_INSURANCE_RATE_CYCLE_RESERVE,0,1,+1,"Samsung Fire local peak 4B was too early; DB Insurance full-window 4B was better when non-price fatigue was present.","split local price-only 4B from full 4B overlay","R6L41_C22_000810_T3_4B_LOCAL|R6L41_C22_005830_T3_4B_FULL",3,3,1,low,overlay_shadow_only,"strengthens existing full_4b_requires_non_price_evidence"

```

## 25. Machine-Readable Rows

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration"}
{"row_type": "case", "case_id": "R6L41_C22_000810_SFM_CAPITAL_RETURN_IFRS17", "symbol": "000810", "company_name": "삼성화재", "round": "R6", "loop": "41", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C22_INSURANCE_RATE_CYCLE_RESERVE", "fine_archetype_id": "INSURANCE_IFRS17_CSM_KICS_CAPITAL_RETURN", "case_type": "structural_success", "positive_or_counterexample": "positive", "best_trigger": "R6L41_C22_000810_T1_STAGE2A", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "positive aligned", "current_profile_verdict": "current_profile_correct", "price_source": "Songdaiki/stock-web", "notes": "손보 우량주: IFRS17 이익/CSM·자본여력과 배당·자사주 기대가 함께 닫힌 구조로 해석. 2024-02-23 entry 이후 180D MFE가 +27.55%였고 MAE도 -11.67%로 정책-only 반례와 확연히 다름."}
{"row_type": "case", "case_id": "R6L41_C22_005830_DBI_CAPITAL_RETURN_ROE", "symbol": "005830", "company_name": "DB손해보험", "round": "R6", "loop": "41", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C22_INSURANCE_RATE_CYCLE_RESERVE", "fine_archetype_id": "INSURANCE_IFRS17_ROE_CAPITAL_RETURN", "case_type": "structural_success", "positive_or_counterexample": "positive", "best_trigger": "R6L41_C22_005830_T1_STAGE2A", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "positive aligned", "current_profile_verdict": "current_profile_correct", "price_source": "Songdaiki/stock-web", "notes": "손보 ROE/PBR rerating: Stage2 actionability는 정책 테마가 아니라 실적/배당/자본여력 bridge가 붙을 때만 유효했다. 180D MFE +26.79%, 이후 4B overlay가 비교적 잘 맞았다."}
{"row_type": "case", "case_id": "R6L41_C22_088350_HWL_POLICY_ONLY_FALSE_POSITIVE", "symbol": "088350", "company_name": "한화생명", "round": "R6", "loop": "41", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C22_INSURANCE_RATE_CYCLE_RESERVE", "fine_archetype_id": "LIFE_INSURER_POLICY_BETA_WITHOUT_CAPITAL_RETURN_CONFIRMATION", "case_type": "failed_rerating", "positive_or_counterexample": "counterexample", "best_trigger": "R6L41_C22_088350_T1_STAGE2_POLICY_ONLY", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "counterexample: score promotion would not align with return path", "current_profile_verdict": "current_profile_false_positive", "price_source": "Songdaiki/stock-web", "notes": "생보 policy/value-up beta만으로는 positive promotion이 위험했다. entry 이후 180D MFE는 +3.84%에 그치고 MAE는 -24.52%까지 열렸다."}
{"row_type": "trigger", "trigger_id": "R6L41_C22_000810_T1_STAGE2A", "case_id": "R6L41_C22_000810_SFM_CAPITAL_RETURN_IFRS17", "symbol": "000810", "company_name": "삼성화재", "round": "R6", "loop": "41", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C22_INSURANCE_RATE_CYCLE_RESERVE", "fine_archetype_id": "INSURANCE_IFRS17_CSM_KICS_CAPITAL_RETURN", "sector": "금융·자본배분·디지털금융", "primary_archetype": "보험 IFRS17/ROE/PBR/자본환원 rerating", "loop_objective": "coverage_gap_fill; counterexample_mining; sector_specific_rule_discovery; 4B_non_price_requirement_stress_test; 4C_thesis_break_timing_test", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-02-22", "evidence_available_at_that_date": "FY2023/IFRS17 earnings-capital-return event window; next-trading-day close used because exact intraday timestamp was not resolved in this run.", "evidence_source": "company IR/DART/news event proxy; price verified in stock-web rows", "stage2_evidence_fields": ["public_event_or_disclosure", "policy_or_regulatory_optionality", "early_revision_signal", "relative_strength"], "stage3_evidence_fields": ["financial_visibility", "margin_bridge"], "stage4b_evidence_fields": [], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/000/000810/2024.csv", "profile_path": "atlas/symbol_profiles/000/000810.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-02-23", "entry_price": 308500, "MFE_30D_pct": 12.16, "MFE_90D_pct": 27.55, "MFE_180D_pct": 27.55, "MFE_1Y_pct": 38.57, "MFE_2Y_pct": null, "MAE_30D_pct": -7.46, "MAE_90D_pct": -11.67, "MAE_180D_pct": -11.67, "MAE_1Y_pct": -11.67, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-06-28", "peak_price": 393500, "drawdown_after_peak_pct": -17.66, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "not_applicable", "four_b_evidence_type": [], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "structural_success", "current_profile_verdict": "current_profile_correct", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R6L41_000810_2024-02-23_308500", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "R6L41_C22_000810_T2_GREEN_COMPARE", "case_id": "R6L41_C22_000810_SFM_CAPITAL_RETURN_IFRS17", "symbol": "000810", "company_name": "삼성화재", "round": "R6", "loop": "41", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C22_INSURANCE_RATE_CYCLE_RESERVE", "fine_archetype_id": "INSURANCE_IFRS17_CSM_KICS_CAPITAL_RETURN", "sector": "금융·자본배분·디지털금융", "primary_archetype": "보험 IFRS17/ROE/PBR/자본환원 rerating", "loop_objective": "coverage_gap_fill; counterexample_mining; sector_specific_rule_discovery; 4B_non_price_requirement_stress_test; 4C_thesis_break_timing_test", "trigger_type": "Stage3-Green comparison", "trigger_date": "2024-05-14", "evidence_available_at_that_date": "1Q24/IFRS17 result confirmation window; 2024-05-16 row captured gap-up confirmation.", "evidence_source": "company IR/DART/news event proxy; price verified in stock-web rows", "stage2_evidence_fields": ["public_event_or_disclosure", "relative_strength"], "stage3_evidence_fields": ["confirmed_revision", "financial_visibility", "margin_bridge"], "stage4b_evidence_fields": [], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/000/000810/2024.csv", "profile_path": "atlas/symbol_profiles/000/000810.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-05-16", "entry_price": 370000, "MFE_30D_pct": 2.7, "MFE_90D_pct": 6.35, "MFE_180D_pct": 17.57, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -12.43, "MAE_90D_pct": -12.43, "MAE_180D_pct": -12.43, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-12-03", "peak_price": 435000, "drawdown_after_peak_pct": -25.52, "green_lateness_ratio": 0.724, "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "not_applicable", "four_b_evidence_type": [], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "late_green_but_still_positive", "current_profile_verdict": "current_profile_too_late", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R6L41_000810_2024-05-16_370000", "dedupe_for_aggregate": false, "aggregate_group_role": "label_comparison_only", "is_new_independent_case": true, "reuse_reason": "same_symbol_new_trigger_family_green_lateness_audit", "independent_evidence_weight": 0.5, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "R6L41_C22_000810_T3_4B_LOCAL", "case_id": "R6L41_C22_000810_SFM_CAPITAL_RETURN_IFRS17", "symbol": "000810", "company_name": "삼성화재", "round": "R6", "loop": "41", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C22_INSURANCE_RATE_CYCLE_RESERVE", "fine_archetype_id": "INSURANCE_IFRS17_CSM_KICS_CAPITAL_RETURN", "sector": "금융·자본배분·디지털금융", "primary_archetype": "보험 IFRS17/ROE/PBR/자본환원 rerating", "loop_objective": "coverage_gap_fill; counterexample_mining; sector_specific_rule_discovery; 4B_non_price_requirement_stress_test; 4C_thesis_break_timing_test", "trigger_type": "Stage4B local overlay", "trigger_date": "2024-06-28", "evidence_available_at_that_date": "local valuation/positioning overheat around 2024-06-28 price high; no full non-price fatigue confirmation.", "evidence_source": "price-verified row plus non-price evidence not fully resolved; overlay only", "stage2_evidence_fields": [], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["valuation_blowoff", "positioning_overheat", "price_only_local_peak"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/000/000810/2024.csv", "profile_path": "atlas/symbol_profiles/000/000810.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-06-28", "entry_price": 389000, "MFE_30D_pct": 1.16, "MFE_90D_pct": 1.16, "MFE_180D_pct": 11.83, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -16.71, "MAE_90D_pct": -16.71, "MAE_180D_pct": -16.71, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-12-03", "peak_price": 435000, "drawdown_after_peak_pct": -25.52, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.947, "four_b_full_window_peak_proximity": 0.636, "four_b_timing_verdict": "price_only_local_4B_too_early", "four_b_evidence_type": ["price_only", "valuation_blowoff", "positioning_overheat"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "4B_too_early", "current_profile_verdict": "current_profile_4B_too_early", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R6L41_000810_2024-06-28_389000", "dedupe_for_aggregate": false, "aggregate_group_role": "4B_overlay_only", "is_new_independent_case": true, "reuse_reason": "same_symbol_new_trigger_family_4B_local_vs_full_window", "independent_evidence_weight": 0.25, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "R6L41_C22_005830_T1_STAGE2A", "case_id": "R6L41_C22_005830_DBI_CAPITAL_RETURN_ROE", "symbol": "005830", "company_name": "DB손해보험", "round": "R6", "loop": "41", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C22_INSURANCE_RATE_CYCLE_RESERVE", "fine_archetype_id": "INSURANCE_IFRS17_ROE_CAPITAL_RETURN", "sector": "금융·자본배분·디지털금융", "primary_archetype": "보험 IFRS17/ROE/PBR/자본환원 rerating", "loop_objective": "coverage_gap_fill; counterexample_mining; sector_specific_rule_discovery; 4B_non_price_requirement_stress_test; 4C_thesis_break_timing_test", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-02-22", "evidence_available_at_that_date": "FY2023/IFRS17 earnings-capital-return event window; next-trading-day close used.", "evidence_source": "company IR/DART/news event proxy; price verified in stock-web rows", "stage2_evidence_fields": ["public_event_or_disclosure", "relative_strength", "early_revision_signal", "policy_or_regulatory_optionality"], "stage3_evidence_fields": ["financial_visibility", "margin_bridge"], "stage4b_evidence_fields": [], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/005/005830/2024.csv", "profile_path": "atlas/symbol_profiles/005/005830.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-02-23", "entry_price": 97800, "MFE_30D_pct": 12.47, "MFE_90D_pct": 23.42, "MFE_180D_pct": 26.79, "MFE_1Y_pct": 26.79, "MFE_2Y_pct": null, "MAE_30D_pct": -6.85, "MAE_90D_pct": -11.86, "MAE_180D_pct": -11.86, "MAE_1Y_pct": -11.86, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-08-22", "peak_price": 124000, "drawdown_after_peak_pct": -26.29, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "not_applicable", "four_b_evidence_type": [], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "structural_success", "current_profile_verdict": "current_profile_correct", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R6L41_005830_2024-02-23_97800", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "R6L41_C22_005830_T2_GREEN_COMPARE", "case_id": "R6L41_C22_005830_DBI_CAPITAL_RETURN_ROE", "symbol": "005830", "company_name": "DB손해보험", "round": "R6", "loop": "41", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C22_INSURANCE_RATE_CYCLE_RESERVE", "fine_archetype_id": "INSURANCE_IFRS17_ROE_CAPITAL_RETURN", "sector": "금융·자본배분·디지털금융", "primary_archetype": "보험 IFRS17/ROE/PBR/자본환원 rerating", "loop_objective": "coverage_gap_fill; counterexample_mining; sector_specific_rule_discovery; 4B_non_price_requirement_stress_test; 4C_thesis_break_timing_test", "trigger_type": "Stage3-Green comparison", "trigger_date": "2024-05-14", "evidence_available_at_that_date": "1Q24/IFRS17 result confirmation window.", "evidence_source": "company IR/DART/news event proxy; price verified in stock-web rows", "stage2_evidence_fields": ["public_event_or_disclosure"], "stage3_evidence_fields": ["confirmed_revision", "financial_visibility", "margin_bridge"], "stage4b_evidence_fields": [], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/005/005830/2024.csv", "profile_path": "atlas/symbol_profiles/005/005830.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-05-16", "entry_price": 111500, "MFE_30D_pct": 3.5, "MFE_90D_pct": 11.21, "MFE_180D_pct": 11.21, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -15.61, "MAE_90D_pct": -15.61, "MAE_180D_pct": -18.03, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-08-22", "peak_price": 124000, "drawdown_after_peak_pct": -26.29, "green_lateness_ratio": 0.523, "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "not_applicable", "four_b_evidence_type": [], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "late_green_but_still_positive", "current_profile_verdict": "current_profile_too_late", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R6L41_005830_2024-05-16_111500", "dedupe_for_aggregate": false, "aggregate_group_role": "label_comparison_only", "is_new_independent_case": true, "reuse_reason": "same_symbol_new_trigger_family_green_lateness_audit", "independent_evidence_weight": 0.5, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "R6L41_C22_005830_T3_4B_FULL", "case_id": "R6L41_C22_005830_DBI_CAPITAL_RETURN_ROE", "symbol": "005830", "company_name": "DB손해보험", "round": "R6", "loop": "41", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C22_INSURANCE_RATE_CYCLE_RESERVE", "fine_archetype_id": "INSURANCE_IFRS17_ROE_CAPITAL_RETURN", "sector": "금융·자본배분·디지털금융", "primary_archetype": "보험 IFRS17/ROE/PBR/자본환원 rerating", "loop_objective": "coverage_gap_fill; counterexample_mining; sector_specific_rule_discovery; 4B_non_price_requirement_stress_test; 4C_thesis_break_timing_test", "trigger_type": "Stage4B full-window overlay", "trigger_date": "2024-08-22", "evidence_available_at_that_date": "valuation/positioning overheat plus revision-fatigue watch around full-window peak.", "evidence_source": "price-verified row plus non-price evidence proxy; overlay only", "stage2_evidence_fields": [], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["valuation_blowoff", "positioning_overheat", "margin_or_backlog_slowdown"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/005/005830/2024.csv", "profile_path": "atlas/symbol_profiles/005/005830.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-08-22", "entry_price": 120600, "MFE_30D_pct": 2.82, "MFE_90D_pct": 2.82, "MFE_180D_pct": 2.82, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -12.02, "MAE_90D_pct": -15.75, "MAE_180D_pct": -24.21, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-08-22", "peak_price": 124000, "drawdown_after_peak_pct": -26.29, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.87, "four_b_full_window_peak_proximity": 0.87, "four_b_timing_verdict": "good_full_window_4B_timing", "four_b_evidence_type": ["valuation_blowoff", "positioning_overheat", "revision_slowdown"], "four_c_protection_label": "hard_4c_watch", "trigger_outcome_label": "4B_overlay_success", "current_profile_verdict": "current_profile_correct", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R6L41_005830_2024-08-22_120600", "dedupe_for_aggregate": false, "aggregate_group_role": "4B_overlay_only", "is_new_independent_case": true, "reuse_reason": "same_symbol_new_trigger_family_4B_full_window", "independent_evidence_weight": 0.25, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "R6L41_C22_088350_T1_STAGE2_POLICY_ONLY", "case_id": "R6L41_C22_088350_HWL_POLICY_ONLY_FALSE_POSITIVE", "symbol": "088350", "company_name": "한화생명", "round": "R6", "loop": "41", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C22_INSURANCE_RATE_CYCLE_RESERVE", "fine_archetype_id": "LIFE_INSURER_POLICY_BETA_WITHOUT_CAPITAL_RETURN_CONFIRMATION", "sector": "금융·자본배분·디지털금융", "primary_archetype": "보험 IFRS17/ROE/PBR/자본환원 rerating", "loop_objective": "coverage_gap_fill; counterexample_mining; sector_specific_rule_discovery; 4B_non_price_requirement_stress_test; 4C_thesis_break_timing_test", "trigger_type": "Stage2 policy-only stress", "trigger_date": "2024-02-22", "evidence_available_at_that_date": "value-up / financial-sector policy beta without company-level capital-return or reserve-quality confirmation.", "evidence_source": "policy/news event proxy; price verified in stock-web rows", "stage2_evidence_fields": ["policy_or_regulatory_optionality", "relative_strength"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["price_only_local_peak"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/088/088350/2024.csv", "profile_path": "atlas/symbol_profiles/088/088350.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-02-23", "entry_price": 3385, "MFE_30D_pct": 3.84, "MFE_90D_pct": 3.84, "MFE_180D_pct": 3.84, "MFE_1Y_pct": 3.84, "MFE_2Y_pct": null, "MAE_30D_pct": -17.13, "MAE_90D_pct": -23.78, "MAE_180D_pct": -24.52, "MAE_1Y_pct": -27.92, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-02-23", "peak_price": 3515, "drawdown_after_peak_pct": -30.58, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 1.0, "four_b_full_window_peak_proximity": 1.0, "four_b_timing_verdict": "price_only_local_4B_not_positive_signal", "four_b_evidence_type": ["price_only"], "four_c_protection_label": "hard_4c_watch", "trigger_outcome_label": "failed_rerating", "current_profile_verdict": "current_profile_false_positive", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R6L41_088350_2024-02-23_3385", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "R6L41_C22_088350_T2_4C_WATCH", "case_id": "R6L41_C22_088350_HWL_POLICY_ONLY_FALSE_POSITIVE", "symbol": "088350", "company_name": "한화생명", "round": "R6", "loop": "41", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C22_INSURANCE_RATE_CYCLE_RESERVE", "fine_archetype_id": "LIFE_INSURER_POLICY_BETA_WITHOUT_CAPITAL_RETURN_CONFIRMATION", "sector": "금융·자본배분·디지털금융", "primary_archetype": "보험 IFRS17/ROE/PBR/자본환원 rerating", "loop_objective": "coverage_gap_fill; counterexample_mining; sector_specific_rule_discovery; 4B_non_price_requirement_stress_test; 4C_thesis_break_timing_test", "trigger_type": "Stage4C protection watch", "trigger_date": "2024-11-14", "evidence_available_at_that_date": "price drift plus absence of thesis confirmation after policy-only signal; used as thesis-break watch, not short recommendation.", "evidence_source": "price-verified row; non-price thesis-break proxy", "stage2_evidence_fields": [], "stage3_evidence_fields": [], "stage4b_evidence_fields": [], "stage4c_evidence_fields": ["thesis_evidence_broken"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/088/088350/2024.csv", "profile_path": "atlas/symbol_profiles/088/088350.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-11-14", "entry_price": 2595, "MFE_30D_pct": 7.13, "MFE_90D_pct": 9.44, "MFE_180D_pct": 9.44, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -5.97, "MAE_90D_pct": -6.36, "MAE_180D_pct": -6.36, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2025-02-18", "peak_price": 2840, "drawdown_after_peak_pct": -14.44, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "not_applicable", "four_b_evidence_type": [], "four_c_protection_label": "hard_4c_success", "trigger_outcome_label": "4C_success", "current_profile_verdict": "current_profile_4C_too_late", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R6L41_088350_2024-11-14_2595", "dedupe_for_aggregate": false, "aggregate_group_role": "4C_overlay_only", "is_new_independent_case": true, "reuse_reason": "same_symbol_new_trigger_family_4C_thesis_break_watch", "independent_evidence_weight": 0.25, "do_not_count_as_new_case": false}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R6L41_C22_000810_SFM_CAPITAL_RETURN_IFRS17", "trigger_id": "R6L41_C22_000810_T1_STAGE2A", "symbol": "000810", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C22_INSURANCE_RATE_CYCLE_RESERVE", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 58, "revision_score": 63, "relative_strength_score": 66, "customer_quality_score": 55, "policy_or_regulatory_score": 62, "valuation_repricing_score": 61, "execution_risk_score": 35, "legal_or_contract_risk_score": 20, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 10, "roe_pbr_capital_return_score": 70, "reserve_quality_score": 62, "kics_or_capital_adequacy_score": 65}, "weighted_score_before": 80.5, "stage_label_before": "Stage3-Yellow / high Stage2-Actionable", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 58, "revision_score": 63, "relative_strength_score": 66, "customer_quality_score": 55, "policy_or_regulatory_score": 62, "valuation_repricing_score": 61, "execution_risk_score": 35, "legal_or_contract_risk_score": 20, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 10, "roe_pbr_capital_return_score": 100, "reserve_quality_score": 100, "kics_or_capital_adequacy_score": 100}, "weighted_score_after": 83.0, "stage_label_after": "Stage3-Yellow / C22-qualified Stage2A", "changed_components": ["roe_pbr_capital_return_score", "reserve_quality_score", "kics_or_capital_adequacy_score"], "component_delta_explanation": "C22 insurer-specific shadow rule adjusts policy-only, reserve quality, capital-return confirmation, and 4B non-price confirmation.", "MFE_90D_pct": 27.55, "MAE_90D_pct": -11.67, "score_return_alignment_label": "aligned", "current_profile_verdict": "current_profile_correct"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R6L41_C22_000810_SFM_CAPITAL_RETURN_IFRS17", "trigger_id": "R6L41_C22_000810_T2_GREEN_COMPARE", "symbol": "000810", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C22_INSURANCE_RATE_CYCLE_RESERVE", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 68, "revision_score": 72, "relative_strength_score": 70, "customer_quality_score": 55, "policy_or_regulatory_score": 60, "valuation_repricing_score": 70, "execution_risk_score": 42, "legal_or_contract_risk_score": 20, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 10, "roe_pbr_capital_return_score": 76, "reserve_quality_score": 70, "kics_or_capital_adequacy_score": 68}, "weighted_score_before": 88.0, "stage_label_before": "Stage3-Green", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 68, "revision_score": 72, "relative_strength_score": 70, "customer_quality_score": 55, "policy_or_regulatory_score": 60, "valuation_repricing_score": 70, "execution_risk_score": 42, "legal_or_contract_risk_score": 20, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 10, "roe_pbr_capital_return_score": 76, "reserve_quality_score": 70, "kics_or_capital_adequacy_score": 68, "green_confirmation_requires_less_local_overheat": -1}, "weighted_score_after": 87.0, "stage_label_after": "Stage3-Green but late-watch", "changed_components": ["green_confirmation_requires_less_local_overheat"], "component_delta_explanation": "C22 insurer-specific shadow rule adjusts policy-only, reserve quality, capital-return confirmation, and 4B non-price confirmation.", "MFE_90D_pct": 6.35, "MAE_90D_pct": -12.43, "score_return_alignment_label": "aligned", "current_profile_verdict": "current_profile_too_late"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R6L41_C22_000810_SFM_CAPITAL_RETURN_IFRS17", "trigger_id": "R6L41_C22_000810_T3_4B_LOCAL", "symbol": "000810", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C22_INSURANCE_RATE_CYCLE_RESERVE", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 65, "revision_score": 68, "relative_strength_score": 80, "customer_quality_score": 55, "policy_or_regulatory_score": 55, "valuation_repricing_score": 84, "execution_risk_score": 58, "legal_or_contract_risk_score": 20, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 10, "roe_pbr_capital_return_score": 74, "reserve_quality_score": 65, "kics_or_capital_adequacy_score": 65}, "weighted_score_before": 84.0, "stage_label_before": "Stage3-Green with local 4B watch", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 65, "revision_score": 68, "relative_strength_score": 80, "customer_quality_score": 55, "policy_or_regulatory_score": 55, "valuation_repricing_score": 84, "execution_risk_score": 58, "legal_or_contract_risk_score": 20, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 10, "roe_pbr_capital_return_score": 74, "reserve_quality_score": 65, "kics_or_capital_adequacy_score": 65, "full_4b_requires_non_price_evidence": 1}, "weighted_score_after": 82.0, "stage_label_after": "Stage3-Green + 4B-watch only", "changed_components": ["full_4b_requires_non_price_evidence"], "component_delta_explanation": "C22 insurer-specific shadow rule adjusts policy-only, reserve quality, capital-return confirmation, and 4B non-price confirmation.", "MFE_90D_pct": 1.16, "MAE_90D_pct": -16.71, "score_return_alignment_label": "aligned", "current_profile_verdict": "current_profile_4B_too_early"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R6L41_C22_005830_DBI_CAPITAL_RETURN_ROE", "trigger_id": "R6L41_C22_005830_T1_STAGE2A", "symbol": "005830", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C22_INSURANCE_RATE_CYCLE_RESERVE", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 60, "revision_score": 61, "relative_strength_score": 68, "customer_quality_score": 50, "policy_or_regulatory_score": 60, "valuation_repricing_score": 62, "execution_risk_score": 37, "legal_or_contract_risk_score": 20, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 10, "roe_pbr_capital_return_score": 68, "reserve_quality_score": 64, "kics_or_capital_adequacy_score": 62}, "weighted_score_before": 79.0, "stage_label_before": "Stage3-Yellow / high Stage2-Actionable", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 60, "revision_score": 61, "relative_strength_score": 68, "customer_quality_score": 50, "policy_or_regulatory_score": 60, "valuation_repricing_score": 62, "execution_risk_score": 37, "legal_or_contract_risk_score": 20, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 10, "roe_pbr_capital_return_score": 100, "reserve_quality_score": 100, "kics_or_capital_adequacy_score": 100}, "weighted_score_after": 82.0, "stage_label_after": "C22-qualified Stage2A / Yellow", "changed_components": ["roe_pbr_capital_return_score", "reserve_quality_score", "kics_or_capital_adequacy_score"], "component_delta_explanation": "C22 insurer-specific shadow rule adjusts policy-only, reserve quality, capital-return confirmation, and 4B non-price confirmation.", "MFE_90D_pct": 23.42, "MAE_90D_pct": -11.86, "score_return_alignment_label": "aligned", "current_profile_verdict": "current_profile_correct"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R6L41_C22_005830_DBI_CAPITAL_RETURN_ROE", "trigger_id": "R6L41_C22_005830_T2_GREEN_COMPARE", "symbol": "005830", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C22_INSURANCE_RATE_CYCLE_RESERVE", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 66, "revision_score": 70, "relative_strength_score": 71, "customer_quality_score": 50, "policy_or_regulatory_score": 58, "valuation_repricing_score": 72, "execution_risk_score": 45, "legal_or_contract_risk_score": 20, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 10, "roe_pbr_capital_return_score": 74, "reserve_quality_score": 69, "kics_or_capital_adequacy_score": 64}, "weighted_score_before": 87.5, "stage_label_before": "Stage3-Green", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 66, "revision_score": 70, "relative_strength_score": 71, "customer_quality_score": 50, "policy_or_regulatory_score": 58, "valuation_repricing_score": 72, "execution_risk_score": 45, "legal_or_contract_risk_score": 20, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 10, "roe_pbr_capital_return_score": 74, "reserve_quality_score": 69, "kics_or_capital_adequacy_score": 64, "green_confirmation_requires_reserve_quality": 0}, "weighted_score_after": 87.5, "stage_label_after": "Stage3-Green", "changed_components": ["green_confirmation_requires_reserve_quality"], "component_delta_explanation": "C22 insurer-specific shadow rule adjusts policy-only, reserve quality, capital-return confirmation, and 4B non-price confirmation.", "MFE_90D_pct": 11.21, "MAE_90D_pct": -15.61, "score_return_alignment_label": "aligned", "current_profile_verdict": "current_profile_too_late"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R6L41_C22_005830_DBI_CAPITAL_RETURN_ROE", "trigger_id": "R6L41_C22_005830_T3_4B_FULL", "symbol": "005830", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C22_INSURANCE_RATE_CYCLE_RESERVE", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 60, "revision_score": 58, "relative_strength_score": 76, "customer_quality_score": 50, "policy_or_regulatory_score": 52, "valuation_repricing_score": 88, "execution_risk_score": 62, "legal_or_contract_risk_score": 20, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 10, "roe_pbr_capital_return_score": 70, "reserve_quality_score": 62, "kics_or_capital_adequacy_score": 60}, "weighted_score_before": 83.0, "stage_label_before": "Stage3-Green + 4B overlay", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 60, "revision_score": 58, "relative_strength_score": 76, "customer_quality_score": 50, "policy_or_regulatory_score": 52, "valuation_repricing_score": 88, "execution_risk_score": 62, "legal_or_contract_risk_score": 20, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 10, "roe_pbr_capital_return_score": 70, "reserve_quality_score": 62, "kics_or_capital_adequacy_score": 60, "non_price_4b_confirmation_bonus": 1}, "weighted_score_after": 81.0, "stage_label_after": "4B overlay confirmed", "changed_components": ["non_price_4b_confirmation_bonus"], "component_delta_explanation": "C22 insurer-specific shadow rule adjusts policy-only, reserve quality, capital-return confirmation, and 4B non-price confirmation.", "MFE_90D_pct": 2.82, "MAE_90D_pct": -15.75, "score_return_alignment_label": "aligned", "current_profile_verdict": "current_profile_correct"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R6L41_C22_088350_HWL_POLICY_ONLY_FALSE_POSITIVE", "trigger_id": "R6L41_C22_088350_T1_STAGE2_POLICY_ONLY", "symbol": "088350", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C22_INSURANCE_RATE_CYCLE_RESERVE", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 30, "revision_score": 35, "relative_strength_score": 62, "customer_quality_score": 35, "policy_or_regulatory_score": 72, "valuation_repricing_score": 68, "execution_risk_score": 60, "legal_or_contract_risk_score": 20, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 25, "roe_pbr_capital_return_score": 28, "reserve_quality_score": 22, "kics_or_capital_adequacy_score": 35}, "weighted_score_before": 76.0, "stage_label_before": "Stage3-Yellow risk / false positive if policy-only promoted", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 30, "revision_score": 35, "relative_strength_score": 62, "customer_quality_score": 35, "policy_or_regulatory_score": 72, "valuation_repricing_score": 68, "execution_risk_score": 60, "legal_or_contract_risk_score": 20, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 25, "roe_pbr_capital_return_score": 28, "reserve_quality_score": 22, "kics_or_capital_adequacy_score": 35, "policy_only_no_cap": -12, "reserve_quality_required": -6, "capital_return_confirmation_required": -6}, "weighted_score_after": 62.0, "stage_label_after": "Stage2-watch / no positive promotion", "changed_components": ["policy_only_no_cap", "reserve_quality_required", "capital_return_confirmation_required"], "component_delta_explanation": "C22 insurer-specific shadow rule adjusts policy-only, reserve quality, capital-return confirmation, and 4B non-price confirmation.", "MFE_90D_pct": 3.84, "MAE_90D_pct": -23.78, "score_return_alignment_label": "current_profile_residual_false_positive", "current_profile_verdict": "current_profile_false_positive"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R6L41_C22_088350_HWL_POLICY_ONLY_FALSE_POSITIVE", "trigger_id": "R6L41_C22_088350_T2_4C_WATCH", "symbol": "088350", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C22_INSURANCE_RATE_CYCLE_RESERVE", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 20, "revision_score": 22, "relative_strength_score": 25, "customer_quality_score": 30, "policy_or_regulatory_score": 50, "valuation_repricing_score": 45, "execution_risk_score": 72, "legal_or_contract_risk_score": 20, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 30, "roe_pbr_capital_return_score": 20, "reserve_quality_score": 18, "kics_or_capital_adequacy_score": 30}, "weighted_score_before": 54.0, "stage_label_before": "Stage2-watch / weak thesis", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 20, "revision_score": 22, "relative_strength_score": 25, "customer_quality_score": 30, "policy_or_regulatory_score": 50, "valuation_repricing_score": 45, "execution_risk_score": 72, "legal_or_contract_risk_score": 20, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 30, "roe_pbr_capital_return_score": 20, "reserve_quality_score": 18, "kics_or_capital_adequacy_score": 30, "thesis_break_score": 10}, "weighted_score_after": 48.0, "stage_label_after": "4C thesis-break watch", "changed_components": ["thesis_break_score"], "component_delta_explanation": "C22 insurer-specific shadow rule adjusts policy-only, reserve quality, capital-return confirmation, and 4B non-price confirmation.", "MFE_90D_pct": 9.44, "MAE_90D_pct": -6.36, "score_return_alignment_label": "aligned", "current_profile_verdict": "current_profile_4C_too_late"}
{"row_type": "residual_contribution", "round": "R6", "loop": "41", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C22_INSURANCE_RATE_CYCLE_RESERVE", "new_independent_case_count": 3, "reused_case_count": 0, "new_symbol_count": 3, "same_archetype_new_symbol_count": 3, "same_archetype_new_trigger_family_count": 5, "new_canonical_archetype_count": 1, "new_trigger_family_count": 5, "tested_existing_calibrated_axes": ["stage2_actionable_evidence_bonus", "stage3_yellow_total_min", "stage3_green_total_min", "stage3_green_revision_min", "price_only_blowoff_blocks_positive_stage", "full_4b_requires_non_price_evidence", "hard_4c_thesis_break_routes_to_4c"], "residual_error_types_found": ["policy_only_financial_beta_false_positive", "local_4B_too_early_without_non_price_evidence", "green_late_in_insurer_capital_return_cycle"], "loop_contribution_label": "canonical_archetype_rule_candidate", "do_not_propose_new_weight_delta": false}
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

Recommended next coverage:

- R6 / C22 insurer holdout with Samsung Life, Hyundai Marine, Meritz Financial, Hanwha General Insurance.
- Or L7 / C23 bio approval-to-commercialization where current Green thresholds may be too strict after regulatory approval but before revenue conversion.

## 28. Source Notes

- `Songdaiki/stock-web/atlas/manifest.json` read for `max_date=2026-02-20`, `price_adjustment_status=raw_unadjusted_marcap`, and shard roots.
- `atlas/symbol_profiles/000/000810.json`, `atlas/symbol_profiles/005/005830.json`, `atlas/symbol_profiles/088/088350.json` read for profile and corporate-action status.
- `atlas/ohlcv_tradable_by_symbol_year/<prefix>/<ticker>/2024.csv` and 2025 continuation rows read for MFE/MAE.
- Evidence-source exact filing URLs should be resolved in a later ingestion validation pass before any production promotion.
