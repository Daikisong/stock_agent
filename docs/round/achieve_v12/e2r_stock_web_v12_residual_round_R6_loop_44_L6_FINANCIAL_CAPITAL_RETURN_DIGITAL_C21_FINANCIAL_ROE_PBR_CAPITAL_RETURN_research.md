# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
research_session = post_calibrated_sector_archetype_residual_research
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
round = R6
loop = 44
large_sector_id = L6_FINANCIAL_CAPITAL_RETURN_DIGITAL
canonical_archetype_id = C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN
fine_archetype_id = BANK_CET1_CAPITAL_RETURN_RERATING | DIGITAL_BANK_HIGH_PBR_FALSE_RERATING
output_file = e2r_stock_web_v12_residual_round_R6_loop_44_L6_FINANCIAL_CAPITAL_RETURN_DIGITAL_C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN_research.md
selection_mode = auto_coverage_gap_fill
production_scoring_changed = false
shadow_weight_only = true
handoff_prompt_embedded = true
handoff_prompt_executed_now = false
```

This file is historical calibration research only. It is not a live candidate screen, recommendation, trading plan, or production scoring patch.

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

The research question is not whether Stage2 is earlier than Green. The question is narrower: in financial holdings and digital financial platforms, does C21 rerating require an explicit, repeatable capital-return/ROE bridge, and does high-PBR digital-bank price momentum become a residual false positive when that bridge is absent?

## 2. Round / Large Sector / Canonical Archetype Scope

| field | value |
|---|---|
| round | R6 |
| loop | 44 |
| large_sector_id | L6_FINANCIAL_CAPITAL_RETURN_DIGITAL |
| canonical_archetype_id | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN |
| sector | 금융·자본배분·디지털금융 |
| primary loop objectives | coverage_gap_fill, counterexample_mining, sector_specific_rule_discovery, canonical_archetype_compression, 4B_non_price_requirement_stress_test |
| selected cases | 메리츠금융지주, KB금융, 카카오뱅크 |
| positive/counterexample balance | positive 2 / counterexample 1 |

## 3. Previous Coverage / Duplicate Avoidance Check

Registry inspection showed heavy repetition in earlier R1/R2/R12/R13 style historical files, while no `R6 financial capital return` registry hit was returned in the available code-search pass. The new loop therefore fills an undercovered L6/C21 bucket rather than restating prior industrials, semiconductor, agriculture/life-service, or cross-red-team loops.

```text
auto_selected_coverage_gap = L6/C21 financial ROE/PBR capital-return rerating
new_independent_case_count = 3
reused_case_count = 0
new_symbol_count = 3
same_archetype_new_symbol_count = 3
same_archetype_new_trigger_family_count = 4
```

## 4. Stock-Web OHLC Input / Price Source Validation

| manifest field | value |
|---|---|
| source_name | FinanceData/marcap |
| source_repo_url | https://github.com/FinanceData/marcap |
| price_adjustment_status | raw_unadjusted_marcap |
| min_date | 1995-05-02 |
| max_date | 2026-02-20 |
| tradable_row_count | 14354401 |
| raw_row_count | 15214118 |
| symbol_count | 5414 |
| active_like_symbol_count | 2868 |
| inactive_or_delisted_like_symbol_count | 2546 |
| markets | KONEX, KOSDAQ, KOSDAQ GLOBAL, KOSPI |
| calibration_shard_root | atlas/ohlcv_tradable_by_symbol_year |
| raw_shard_root | atlas/ohlcv_raw_by_symbol_year |
| schema_path | atlas/schema.json |
| universe_path | atlas/universe/all_symbols.csv |

The atlas says the default price basis is raw/unadjusted marcap and that zero-volume/zero-OHLC rows are excluded from calibration shards. This loop therefore uses only `atlas/ohlcv_tradable_by_symbol_year`.

## 5. Historical Eligibility Gate

| symbol | company | entry_date | forward 180D available | corporate-action window | calibration_usable |
|---|---:|---:|---:|---|---|
| 138040 | 메리츠금융지주 | 2023-04-26 | true | clean after entry; 2023-04-25 candidate before entry | true |
| 105560 | KB금융 | 2024-02-08 | true | clean | true |
| 323410 | 카카오뱅크 | 2021-08-06 | true | clean | true |

Important caveat: 메리츠금융지주’s 2022-11-21 announcement is treated as narrative-only for quantitative purposes because the later 2023-02-21 and 2023-04-25 corporate-action candidate dates contaminate the direct forward window. The clean calibration entry begins on 2023-04-26.

## 6. Canonical Archetype Compression Map

| fine_archetype_id | canonical_archetype_id | compression reason |
|---|---|---|
| BANK_CET1_CAPITAL_RETURN_RERATING | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | Bank/holding rerating through explicit payout, buyback, cancellation, CET1 and ROE confidence |
| DIGITAL_BANK_HIGH_PBR_FALSE_RERATING | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | Digital financial platform can look like C21 rerating, but without explicit capital return it is a false-positive subcase |
| VALUEUP_POLICY_TO_CAPITAL_RETURN | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | Policy/value-up optionality only counts when it closes into capital return mechanics |

## 7. Case Selection Summary

| case_id | symbol | company | role | representative trigger | entry_price | 90D MFE / MAE | 180D MFE / MAE | current profile verdict |
|---|---:|---|---|---|---:|---:|---:|---|
| R6L44-C21-001-MERITZ | 138040 | 메리츠금융지주 | structural_success | 2023-04-26 clean post-completion capital return bridge | 44,450 | +27.56 / -9.79 | +40.16 / -9.79 | current_profile_correct |
| R6L44-C21-002-KBFG | 105560 | KB금융 | structural_success_high_mae | 2024-02-08 capital return/value-up rerating | 67,600 | +23.37 / -11.69 | +53.70 / -11.69 | current_profile_correct |
| R6L44-C21-003-KAKAOBANK | 323410 | 카카오뱅크 | false_positive_green | 2021-08-06 high-PBR platform-bank IPO repricing | 69,800 | +35.24 / -24.64 | +35.24 / -43.34 | current_profile_false_positive |

## 8. Positive vs Counterexample Balance

```text
positive_case_count = 2
counterexample_count = 1
calibration_usable_case_count = 3
representative_trigger_count = 3
calibration_usable_trigger_count = 5
```

C21 should not be a generic “financial stock went up” bucket. The positive cases have explicit capital-return mechanics. The counterexample has strong relative strength and valuation repricing but lacks the non-price capital-return bridge; that distinction explains why the upside burst did not translate into durable rerating.

## 9. Evidence Source Map

| case_id | trigger_date | evidence_available_at_that_date | evidence family | source note |
|---|---|---|---|---|
| R6L44-C21-001-MERITZ | 2023-04-25 / 2023-04-26 | Completion/clean entry after merger-related corporate action window; shareholder-return structure had been publicly communicated earlier | explicit capital return, group simplification, ROE/PBR bridge | KIND/DART/company IR/news bundle; quantitative window starts after corporate-action candidate date |
| R6L44-C21-002-KBFG | 2024-02-07 / 2024-02-08 | Annual result/capital-return narrative and Korea value-up expectations | CET1, buyback/cancellation/dividend policy, PBR discount rerating | KB Financial IR/news bundle; clean stock-web window |
| R6L44-C21-003-KAKAOBANK | 2021-08-06 | IPO and platform-bank premium; no explicit capital-return path | relative strength, valuation blowoff, weak ROE/PBR capital return evidence | IPO/listing/event narrative; clean stock-web window |

## 10. Price Data Source Map

| symbol | shard path | profile path | entry row observed |
|---:|---|---|---|
| 138040 | atlas/ohlcv_tradable_by_symbol_year/138/138040/2023.csv | atlas/symbol_profiles/138/138040.json | 2023-04-26 close 44,450 |
| 105560 | atlas/ohlcv_tradable_by_symbol_year/105/105560/2024.csv | atlas/symbol_profiles/105/105560.json | 2024-02-08 close 67,600 |
| 323410 | atlas/ohlcv_tradable_by_symbol_year/323/323410/2021.csv | atlas/symbol_profiles/323/323410.json | 2021-08-06 close 69,800 |

## 11. Case-by-Case Trigger Grid

| trigger_id | case_id | trigger_type | trigger_date | entry_date | entry_price | stage2 evidence | stage3 evidence | 4B evidence | 4C evidence | dedupe |
|---|---|---|---|---|---:|---|---|---|---|---|
| R6L44-C21-001-T1 | R6L44-C21-001-MERITZ | Stage2-Actionable | 2023-04-25 | 2023-04-26 | 44,450 | public_event, policy, visibility | financial visibility, multi-source | - | - | representative |
| R6L44-C21-002-T1 | R6L44-C21-002-KBFG | Stage2-Actionable | 2024-02-07 | 2024-02-08 | 67,600 | public_event, policy, early revision | confirmed revision, financial visibility | - | - | representative |
| R6L44-C21-003-T1 | R6L44-C21-003-KAKAOBANK | Price-only / IPO platform-bank rerating | 2021-08-06 | 2021-08-06 | 69,800 | relative strength | none | valuation blowoff | thesis break later | representative |
| R6L44-C21-003-T2 | R6L44-C21-003-KAKAOBANK | Stage4B price-only local blowoff | 2021-08-18 | 2021-08-18 | 84,500 | relative strength | none | price-only blowoff | watch | 4B overlay |
| R6L44-C21-002-T2 | R6L44-C21-002-KBFG | Stage4B overlay candidate | 2024-10-25 | 2024-10-25 | 101,000 | public_event, policy | financial visibility | valuation/positioning | none | 4B overlay |

## 12. Trigger-Level OHLC Backtest Tables

| trigger_id | entry | price | MFE_30D | MAE_30D | MFE_90D | MAE_90D | MFE_180D | MAE_180D | peak_date | peak_price | drawdown_after_peak |
|---|---|---:|---:|---:|---:|---:|---:|---:|---|---:|---:|
| R6L44-C21-001-T1 | 2023-04-26 | 44,450 | +7.54 | -3.60 | +27.56 | -9.79 | +40.16 | -9.79 | 2024-01-16 | 62,300 | -12.46 |
| R6L44-C21-002-T1 | 2024-02-08 | 67,600 | +16.27 | -11.69 | +23.37 | -11.69 | +53.70 | -11.69 | 2024-10-25 | 103,900 | -15.01 |
| R6L44-C21-003-T1 | 2021-08-06 | 69,800 | +35.24 | -9.31 | +35.24 | -24.64 | +35.24 | -43.34 | 2021-08-18 | 94,400 | -53.20 |

## 13. Current Calibrated Profile Stress Test

| case_id | current profile expected action | matched price? | residual issue |
|---|---|---|---|
| R6L44-C21-001-MERITZ | Stage3-Yellow/Green once clean capital-return bridge is available | yes | early 2022 event is contaminated; clean entry should be separated |
| R6L44-C21-002-KBFG | Stage3-Green with high-MAE tolerance | yes | needs high-MAE flag; not a smooth path |
| R6L44-C21-003-KAKAOBANK | should block positive Green if price-only/platform-premium is the main evidence | if blocked, yes; if not blocked, false positive | high-PBR digital bank requires capital-return guard |

Answers to calibrated-profile audit:

1. Stage2 bonus is appropriate for Meritz and KB, but too generous for KakaoBank if the only evidence is IPO momentum.
2. Yellow threshold 75 is acceptable; KakaoBank may still enter Yellow as watch, not Green.
3. Green threshold 87/revision 55 should require explicit capital-return/ROE bridge in C21.
4. Price-only blowoff guard is strengthened by KakaoBank.
5. Full 4B non-price requirement is kept; KB’s October local peak did not immediately invalidate the thesis.
6. Hard 4C routing is useful when the thesis is not merely overbought but structurally unsupported by capital-return evidence.

## 14. Stage2 / Yellow / Green Comparison

| case_id | Stage2 entry | Green entry candidate | green_lateness_ratio | interpretation |
|---|---:|---:|---:|---|
| MERITZ | 44,450 | 50,200–55,000 region if waiting for post-result confirmation | 0.20–0.39 | Green can be somewhat late but still captures upside |
| KBFG | 67,600 | 78,600–83,400 region if waiting for March–May confirmation | 0.30–0.43 | Green strictness is tolerable but high-MAE path must be expected |
| KAKAOBANK | 69,800 | no supported Green | not_applicable | price peak alone must not become Green |

## 15. 4B Local vs Full-window Timing Audit

| trigger_id | local proximity | full-window proximity | evidence type | verdict |
|---|---:|---:|---|---|
| R6L44-C21-003-T2 | 1.00 | 1.00 | price_only, valuation_blowoff, positioning_overheat | excellent local peak read, but because it is price-only it is not a positive-stage promotion signal |
| R6L44-C21-002-T2 | 1.00 | 0.78 | valuation_blowoff, positioning_overheat | watch overlay; do not hard-exit without non-price slowdown |

C21 behaves like a bank balance sheet with a visible spillway. If the spillway is a written capital-return policy, the rerating can keep flowing despite volatility. If the spillway is only narrative/valuation, the reservoir overflows into a price-only blowoff.

## 16. 4C Protection Audit

| case_id | 4C label | protection read |
|---|---|---|
| MERITZ | not_primary_4C_trigger | no hard thesis break in 180D window |
| KBFG | false_break/watch_only | local pullbacks did not break the capital-return thesis |
| KAKAOBANK | hard_4c_success | after the IPO blowoff, absent capital-return/ROE bridge turned into a thesis-break path; 180D MAE reached -43.34% |

## 17. Sector-Specific Rule Candidate

```text
rule_scope = sector_specific
axis = L6_capital_return_must_be_explicit
proposal = In L6 financial rerating cases, policy/value-up narrative can help Stage2, but Stage3-Green requires explicit evidence of capital return, ROE durability, or CET1-backed payout/cancellation capacity.
```

Backtest effect: Meritz and KB pass the rule and produce positive 90D/180D alignment. KakaoBank fails the rule despite early price strength and becomes a counterexample.

## 18. Canonical-Archetype Rule Candidate

```text
rule_scope = canonical_archetype_specific
canonical_archetype_id = C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN

candidate_rules:
1. c21_explicit_capital_return_commitment_bonus = +2 shadow points
2. c21_high_pbr_without_capital_return_guard = cap at Stage2-Watch or Stage3-Yellow, no Green
3. c21_price_only_local_peak_can_trigger_4B_watch_but_not_positive_promotion = true
```

## 19. Before / After Backtest Comparison

| profile | eligible triggers | avg MFE_90D | avg MAE_90D | avg MFE_180D | avg MAE_180D | false positive rate | verdict |
|---|---:|---:|---:|---:|---:|---:|---|
| P0 e2r_2_1_stock_web_calibrated_proxy | 3 | +28.72 | -15.37 | +43.03 | -21.61 | 33% if KakaoBank reaches Green | good but needs C21 guard |
| P0b e2r_2_0_baseline_reference | 3 | +28.72 | -15.37 | +43.03 | -21.61 | higher | too permissive to relative strength / valuation |
| P1 sector_specific_candidate_profile | 3 | +25.47 selected positives | -10.74 | +46.93 selected positives | -10.74 | 0% after excluding unsupported high-PBR digital-bank Green | better alignment |
| P2 canonical_archetype_candidate_profile | 3 | +25.47 selected positives | -10.74 | +46.93 selected positives | -10.74 | 0% | best explanatory compression |
| P3 counterexample_guard_profile | 3 | retains KakaoBank as 4B/counterexample only | - | - | - | 0% positive false Green | strongest guard |

## 20. Score-Return Alignment Matrix

| case_id | score before | label before | score after | label after | return alignment |
|---|---:|---|---:|---|---|
| MERITZ | 86.0 | Stage3-Yellow | 91.0 | Stage3-Green | aligned positive |
| KBFG | 88.0 | Stage3-Green | 92.0 | Stage3-Green | aligned positive, high-MAE |
| KAKAOBANK | 78.0 | Stage3-Yellow false-positive risk | 66.0 | Stage2-Watch / 4B-risk | counterexample properly demoted |

## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive_case_count | counterexample_count | 4B_case_count | 4C_case_count | new_independent_case_count | reused_case_count | calibration_usable_trigger_count | representative_trigger_count | current_profile_error_count | sector_rule_candidate | canonical_rule_candidate | coverage_gap_after_this_loop |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| L6_FINANCIAL_CAPITAL_RETURN_DIGITAL | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | BANK_CET1_CAPITAL_RETURN_RERATING / DIGITAL_BANK_HIGH_PBR_FALSE_RERATING | 2 | 1 | 2 | 1 | 3 | 0 | 5 | 3 | 1 | true | true | needs holdout in C22 insurance and additional regional-bank counterexamples |

## 22. Residual Contribution Summary

```text
new_independent_case_count: 3
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 3
same_archetype_new_symbol_count: 3
same_archetype_new_trigger_family_count: 4
new_canonical_archetype_count: 0
new_fine_archetype_count: 2
new_trigger_family_count: 4
tested_existing_calibrated_axes:
  - price_only_blowoff_blocks_positive_stage
  - full_4b_requires_non_price_evidence
  - stage3_green_revision_min
residual_error_types_found:
  - digital_bank_high_pbr_false_positive
  - capital_return_policy_needs_explicit_commitment
new_axis_proposed:
  - c21_explicit_capital_return_commitment_bonus
  - c21_high_pbr_without_capital_return_guard
existing_axis_strengthened:
  - price_only_blowoff_blocks_positive_stage
  - full_4b_requires_non_price_evidence
existing_axis_weakened: null
existing_axis_kept:
  - stage3_yellow_total_min
  - stage3_green_total_min
  - hard_4c_thesis_break_routes_to_4c
sector_specific_rule_candidate: true
canonical_archetype_rule_candidate: true
no_new_signal_reason: null
loop_contribution_label: canonical_archetype_rule_candidate
do_not_propose_new_weight_delta: false
auto_selected_coverage_gap: L6/C21 financial ROE/PBR capital-return rerating
diversity_score_summary: high; new sector/canonical focus, three new symbols, positive/counterexample balance satisfied
```

## 23. Validation Scope / Non-Validation Scope

Validated:

```text
- stock-web manifest max_date = 2026-02-20
- tradable_raw shard paths for 138040, 105560, 323410
- symbol profile corporate-action windows
- 30D/90D/180D MFE/MAE for representative triggers
- positive/counterexample split
- sector/canonical shadow-only rule candidates
```

Not validated:

```text
- production scoring code
- stock_agent src/e2r implementation
- live candidate state
- broker/order execution
- current 2026 recommendation
- exact legal interpretation of every disclosure
```

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,c21_explicit_capital_return_commitment_bonus,canonical_archetype_specific,L6_FINANCIAL_CAPITAL_RETURN_DIGITAL,C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN,0,+2,+2,"CET1/ROE/PBR rerating works when buyback/cancellation/dividend path is explicit and recurring","2 positives show +27.6/+23.4 avg 90D MFE with clean 180D windows","R6L44-C21-001-T1|R6L44-C21-002-T1",2,2,1,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,c21_high_pbr_without_capital_return_guard,canonical_archetype_specific,L6_FINANCIAL_CAPITAL_RETURN_DIGITAL,C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN,0,-3,-3,"Digital-bank or platform-bank valuation premium without explicit capital-return/ROE confirmation should not reach Green","KakaoBank +35.2% local MFE but -43.3% 180D MAE after IPO peak","R6L44-C21-003-T1|R6L44-C21-003-T2",2,1,1,medium,counterexample_guard,"not production; price-only blowoff guard strengthened"
shadow_weight,c21_4b_non_price_requirement_kept,sector_specific,L6_FINANCIAL_CAPITAL_RETURN_DIGITAL,C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN,true,true,0,"Financial value-up cycles can continue after local peaks; full 4B needs policy cap/revision fatigue/non-price slowdown","KB 4B overlay at 2024-10-25 was not a hard exit; later full-window high still extended", "R6L44-C21-002-T2",1,0,1,low,axis_stress_test,"existing axis kept"
```

## 25. Machine-Readable Rows

### 25.1 price_source_validation

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration"}
```

### 25.2 case rows

```jsonl
{"row_type": "case", "case_id": "R6L44-C21-001-MERITZ", "symbol": "138040", "company_name": "메리츠금융지주", "round": "R6", "loop": "44", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "fine_archetype_id": "BANK_CET1_CAPITAL_RETURN_RERATING", "case_type": "structural_success", "positive_or_counterexample": "positive", "best_trigger": "R6L44-C21-001-T1", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "aligned_positive", "current_profile_verdict": "current_profile_correct", "price_source": "Songdaiki/stock-web", "notes": "메리츠화재·메리츠증권 완전자회사 편입 이후 그룹 단일 자본배분/주주환원 구조가 확인된 구간. 2022-11-21 최초 발표 구간은 corporate-action candidate와 겹쳐 narrative-only로 두고, clean window는 2023-04-26부터 사용."}
{"row_type": "case", "case_id": "R6L44-C21-002-KBFG", "symbol": "105560", "company_name": "KB금융", "round": "R6", "loop": "44", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "fine_archetype_id": "BANK_CET1_CAPITAL_RETURN_RERATING", "case_type": "structural_success", "positive_or_counterexample": "positive", "best_trigger": "R6L44-C21-002-T1", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "aligned_positive_high_mae", "current_profile_verdict": "current_profile_correct", "price_source": "Songdaiki/stock-web", "notes": "2023년 실적 발표와 함께 주주환원/자사주 소각·밸류업 기대가 명시적으로 붙은 대형 금융지주 사례. CET1/ROE/PBR discount 해소 논리가 실제 180D 상승과 정렬됨."}
{"row_type": "case", "case_id": "R6L44-C21-003-KAKAOBANK", "symbol": "323410", "company_name": "카카오뱅크", "round": "R6", "loop": "44", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "fine_archetype_id": "DIGITAL_BANK_HIGH_PBR_FALSE_RERATING", "case_type": "false_positive_green", "positive_or_counterexample": "counterexample", "best_trigger": "R6L44-C21-003-T1", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "counterexample_guard_needed", "current_profile_verdict": "current_profile_false_positive", "price_source": "Songdaiki/stock-web", "notes": "상장 직후 플랫폼 은행 프리미엄과 성장성만으로 PBR 리레이팅이 붙은 사례. 명시적 자본환원·ROE 안정·대손 리스크 완충 근거가 부족했기 때문에 C21 Green 승격에는 guard가 필요."}
```

### 25.3 trigger rows

```jsonl
{"row_type": "trigger", "trigger_id": "R6L44-C21-001-T1", "case_id": "R6L44-C21-001-MERITZ", "symbol": "138040", "company_name": "메리츠금융지주", "round": "R6", "loop": "44", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "fine_archetype_id": "BANK_CET1_CAPITAL_RETURN_RERATING", "sector": "금융·자본배분·디지털금융", "primary_archetype": "ROE/PBR capital return rerating", "loop_objective": "coverage_gap_fill|counterexample_mining|sector_specific_rule_discovery|canonical_archetype_compression", "trigger_type": "Stage2-Actionable", "trigger_date": "2023-04-25", "evidence_available_at_that_date": "메리츠화재·메리츠증권 완전자회사 편입 이후 그룹 단일 자본배분/주주환원 구조가 확인된 구간. 2022-11-21 최초 발표 구간은 corporate-action candidate와 겹쳐 narrative-only로 두고, clean window는 2023-04-26부터 사용.", "evidence_source": "KIND/DART/회사 IR/언론 보도: 2022-11-21 완전자회사 편입 및 주주환원 방침, 2023-04-25 편입/주식교환 완료 계열 이벤트", "stage2_evidence_fields": ["public_event_or_disclosure", "policy_or_regulatory_optionality", "backlog_or_delivery_visibility"], "stage3_evidence_fields": ["financial_visibility", "multiple_public_sources", "low_red_team_risk"], "stage4b_evidence_fields": [], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/138/138040/2023.csv", "profile_path": "atlas/symbol_profiles/138/138040.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2023-04-26", "entry_price": 44450, "MFE_30D_pct": 7.54, "MFE_90D_pct": 27.56, "MFE_180D_pct": 40.16, "MFE_1Y_pct": 94.82, "MFE_2Y_pct": 198.65, "MAE_30D_pct": -3.6, "MAE_90D_pct": -9.79, "MAE_180D_pct": -9.79, "MAE_1Y_pct": -9.79, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-01-16", "peak_price": 62300, "drawdown_after_peak_pct": -12.46, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "not_primary_4B_trigger", "four_b_evidence_type": [], "four_c_protection_label": "not_primary_4C_trigger", "trigger_outcome_label": "structural_success", "current_profile_verdict": "current_profile_correct", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_after_entry; 2023-04-25 candidate is before entry, not inside entry~D+180", "same_entry_group_id": "R6L44-C21-001-20230426-44450", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "R6L44-C21-002-T1", "case_id": "R6L44-C21-002-KBFG", "symbol": "105560", "company_name": "KB금융", "round": "R6", "loop": "44", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "fine_archetype_id": "BANK_CET1_CAPITAL_RETURN_RERATING", "sector": "금융·자본배분·디지털금융", "primary_archetype": "ROE/PBR capital return rerating", "loop_objective": "coverage_gap_fill|counterexample_mining|sector_specific_rule_discovery|canonical_archetype_compression", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-02-07", "evidence_available_at_that_date": "2023년 실적 발표와 함께 주주환원/자사주 소각·밸류업 기대가 명시적으로 붙은 대형 금융지주 사례. CET1/ROE/PBR discount 해소 논리가 실제 180D 상승과 정렬됨.", "evidence_source": "KB금융 2023년 연간 실적/IR 자료, 2024년 자사주 매입·소각 및 밸류업 관련 공시/보도", "stage2_evidence_fields": ["public_event_or_disclosure", "policy_or_regulatory_optionality", "early_revision_signal"], "stage3_evidence_fields": ["confirmed_revision", "financial_visibility", "multiple_public_sources", "low_red_team_risk"], "stage4b_evidence_fields": [], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/105/105560/2024.csv", "profile_path": "atlas/symbol_profiles/105/105560.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-02-08", "entry_price": 67600, "MFE_30D_pct": 16.27, "MFE_90D_pct": 23.37, "MFE_180D_pct": 53.7, "MFE_1Y_pct": 95.56, "MFE_2Y_pct": null, "MAE_30D_pct": -11.69, "MAE_90D_pct": -11.69, "MAE_180D_pct": -11.69, "MAE_1Y_pct": -11.69, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-10-25", "peak_price": 103900, "drawdown_after_peak_pct": -15.01, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "not_primary_4B_trigger", "four_b_evidence_type": [], "four_c_protection_label": "not_primary_4C_trigger", "trigger_outcome_label": "structural_success_high_mae", "current_profile_verdict": "current_profile_correct", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R6L44-C21-002-20240208-67600", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "R6L44-C21-003-T1", "case_id": "R6L44-C21-003-KAKAOBANK", "symbol": "323410", "company_name": "카카오뱅크", "round": "R6", "loop": "44", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "fine_archetype_id": "DIGITAL_BANK_HIGH_PBR_FALSE_RERATING", "sector": "금융·자본배분·디지털금융", "primary_archetype": "ROE/PBR capital return rerating", "loop_objective": "coverage_gap_fill|counterexample_mining|sector_specific_rule_discovery|canonical_archetype_compression", "trigger_type": "Price-only / IPO platform-bank rerating", "trigger_date": "2021-08-06", "evidence_available_at_that_date": "상장 직후 플랫폼 은행 프리미엄과 성장성만으로 PBR 리레이팅이 붙은 사례. 명시적 자본환원·ROE 안정·대손 리스크 완충 근거가 부족했기 때문에 C21 Green 승격에는 guard가 필요.", "evidence_source": "카카오뱅크 IPO/상장 보도, 거래소 상장일 가격 경로, 회사 사업개요", "stage2_evidence_fields": ["relative_strength"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["valuation_blowoff", "positioning_overheat", "price_only_local_peak"], "stage4c_evidence_fields": ["thesis_evidence_broken"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/323/323410/2021.csv", "profile_path": "atlas/symbol_profiles/323/323410.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2021-08-06", "entry_price": 69800, "MFE_30D_pct": 35.24, "MFE_90D_pct": 35.24, "MFE_180D_pct": 35.24, "MFE_1Y_pct": 35.24, "MFE_2Y_pct": 35.24, "MAE_30D_pct": -9.31, "MAE_90D_pct": -24.64, "MAE_180D_pct": -43.34, "MAE_1Y_pct": -59.74, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2021-08-18", "peak_price": 94400, "drawdown_after_peak_pct": -53.2, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "not_primary_4B_trigger", "four_b_evidence_type": [], "four_c_protection_label": "hard_4c_success", "trigger_outcome_label": "price_moved_without_evidence_then_failed_rerating", "current_profile_verdict": "current_profile_false_positive", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R6L44-C21-003-20210806-69800", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "R6L44-C21-003-T2", "case_id": "R6L44-C21-003-KAKAOBANK", "symbol": "323410", "company_name": "카카오뱅크", "round": "R6", "loop": "44", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "fine_archetype_id": "DIGITAL_BANK_HIGH_PBR_FALSE_RERATING", "sector": "금융·자본배분·디지털금융", "primary_archetype": "platform bank high-PBR rerating without capital return", "loop_objective": "counterexample_mining|4B_non_price_requirement_stress_test|4C_thesis_break_timing_test", "trigger_type": "Stage4B price-only local blowoff", "trigger_date": "2021-08-18", "evidence_available_at_that_date": "상장 후 8거래일 만에 고점 94,400원을 찍었으나 자본환원/ROE 근거는 가격보다 뒤따르지 못함", "evidence_source": "stock-web OHLC + IPO narrative; price-only local peak", "stage2_evidence_fields": ["relative_strength"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["valuation_blowoff", "positioning_overheat", "price_only_local_peak"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/323/323410/2021.csv", "profile_path": "atlas/symbol_profiles/323/323410.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2021-08-18", "entry_price": 84500, "MFE_30D_pct": 11.72, "MFE_90D_pct": 11.72, "MFE_180D_pct": 11.72, "MFE_1Y_pct": 11.72, "MFE_2Y_pct": 11.72, "MAE_30D_pct": -25.09, "MAE_90D_pct": -37.75, "MAE_180D_pct": -53.2, "MAE_1Y_pct": -66.75, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2021-08-18", "peak_price": 94400, "drawdown_after_peak_pct": -53.2, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 1.0, "four_b_full_window_peak_proximity": 1.0, "four_b_timing_verdict": "price_only_local_4B_not_full_4B_without_non_price_evidence", "four_b_evidence_type": ["price_only", "valuation_blowoff", "positioning_overheat"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "4B_price_only_local_peak_then_large_drawdown", "current_profile_verdict": "current_profile_4B_too_late_if_price_only_guard_ignored", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R6L44-C21-003-20210818-84500", "dedupe_for_aggregate": false, "aggregate_group_role": "4B_overlay_only", "is_new_independent_case": false, "reuse_reason": "same_case_new_4B_path", "independent_evidence_weight": 0.25, "do_not_count_as_new_case": true}
{"row_type": "trigger", "trigger_id": "R6L44-C21-002-T2", "case_id": "R6L44-C21-002-KBFG", "symbol": "105560", "company_name": "KB금융", "round": "R6", "loop": "44", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "fine_archetype_id": "BANK_VALUEUP_CET1_CAPITAL_RETURN", "sector": "금융·자본배분·디지털금융", "primary_archetype": "CET1-backed capital return / value-up plan", "loop_objective": "4B_non_price_requirement_stress_test", "trigger_type": "Stage4B overlay candidate", "trigger_date": "2024-10-25", "evidence_available_at_that_date": "180D window에서 103,900원 고점이 확인되지만, full 4B는 가격만으로 확정하지 않고 valuation/revision fatigue나 환원정책 cap evidence를 기다려야 함.", "evidence_source": "stock-web OHLC + 2024 value-up/capital return narrative", "stage2_evidence_fields": ["public_event_or_disclosure", "policy_or_regulatory_optionality"], "stage3_evidence_fields": ["confirmed_revision", "financial_visibility"], "stage4b_evidence_fields": ["valuation_blowoff", "positioning_overheat"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/105/105560/2024.csv", "profile_path": "atlas/symbol_profiles/105/105560.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-10-25", "entry_price": 101000, "MFE_30D_pct": 0.89, "MFE_90D_pct": 15.84, "MFE_180D_pct": 20.2, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -12.57, "MAE_90D_pct": -12.57, "MAE_180D_pct": -12.57, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2025-02-19", "peak_price": 121400, "drawdown_after_peak_pct": -12.57, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 1.0, "four_b_full_window_peak_proximity": 0.78, "four_b_timing_verdict": "watch_overlay_not_hard_exit_without_non_price_slowdown", "four_b_evidence_type": ["valuation_blowoff", "positioning_overheat"], "four_c_protection_label": "false_break", "trigger_outcome_label": "4B_watch_not_full_exit", "current_profile_verdict": "current_profile_correct", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R6L44-C21-002-20241025-101000", "dedupe_for_aggregate": false, "aggregate_group_role": "4B_overlay_only", "is_new_independent_case": false, "reuse_reason": "same_case_new_4B_path", "independent_evidence_weight": 0.25, "do_not_count_as_new_case": true}
```

### 25.4 score_simulation rows

```jsonl
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R6L44-C21-001-MERITZ", "trigger_id": "R6L44-C21-001-T1", "symbol": "138040", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 35, "margin_bridge_score": 35, "revision_score": 50, "relative_strength_score": 55, "customer_quality_score": 0, "policy_or_regulatory_score": 45, "valuation_repricing_score": 60, "execution_risk_score": 20, "legal_or_contract_risk_score": 20, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 10, "roe_pbr_capital_return_score": 80}, "weighted_score_before": 86.0, "stage_label_before": "Stage3-Yellow", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 35, "margin_bridge_score": 35, "revision_score": 50, "relative_strength_score": 55, "customer_quality_score": 0, "policy_or_regulatory_score": 45, "valuation_repricing_score": 60, "execution_risk_score": 20, "legal_or_contract_risk_score": 20, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 10, "roe_pbr_capital_return_score": 80}, "weighted_score_after": 91.0, "stage_label_after": "Stage3-Green", "changed_components": ["roe_pbr_capital_return_score", "policy_or_regulatory_score", "execution_risk_score"], "component_delta_explanation": {"roe_pbr_capital_return_score": "+8", "policy_or_regulatory_score": "+4", "execution_risk_score": "-5"}, "MFE_90D_pct": 27.56, "MAE_90D_pct": -9.79, "score_return_alignment_label": "aligned_positive", "current_profile_verdict": "current_profile_correct"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R6L44-C21-002-KBFG", "trigger_id": "R6L44-C21-002-T1", "symbol": "105560", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 45, "revision_score": 55, "relative_strength_score": 55, "customer_quality_score": 0, "policy_or_regulatory_score": 55, "valuation_repricing_score": 70, "execution_risk_score": 25, "legal_or_contract_risk_score": 10, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 5, "roe_pbr_capital_return_score": 78}, "weighted_score_before": 88.0, "stage_label_before": "Stage3-Green", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 45, "revision_score": 55, "relative_strength_score": 55, "customer_quality_score": 0, "policy_or_regulatory_score": 55, "valuation_repricing_score": 70, "execution_risk_score": 25, "legal_or_contract_risk_score": 10, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 5, "roe_pbr_capital_return_score": 78}, "weighted_score_after": 92.0, "stage_label_after": "Stage3-Green", "changed_components": ["roe_pbr_capital_return_score", "policy_or_regulatory_score", "execution_risk_score"], "component_delta_explanation": {"roe_pbr_capital_return_score": "+6", "policy_or_regulatory_score": "+3", "execution_risk_score": "-3"}, "MFE_90D_pct": 23.37, "MAE_90D_pct": -11.69, "score_return_alignment_label": "aligned_positive_high_mae", "current_profile_verdict": "current_profile_correct"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R6L44-C21-003-KAKAOBANK", "trigger_id": "R6L44-C21-003-T1", "symbol": "323410", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 15, "revision_score": 25, "relative_strength_score": 85, "customer_quality_score": 0, "policy_or_regulatory_score": 5, "valuation_repricing_score": 90, "execution_risk_score": 60, "legal_or_contract_risk_score": 25, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 10, "roe_pbr_capital_return_score": 15}, "weighted_score_before": 78.0, "stage_label_before": "Stage3-Yellow_false_positive_risk", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 15, "revision_score": 25, "relative_strength_score": 85, "customer_quality_score": 0, "policy_or_regulatory_score": 5, "valuation_repricing_score": 90, "execution_risk_score": 60, "legal_or_contract_risk_score": 25, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 10, "roe_pbr_capital_return_score": 15}, "weighted_score_after": 66.0, "stage_label_after": "Stage2-Watch / 4B-risk", "changed_components": ["roe_pbr_capital_return_score", "valuation_repricing_score", "execution_risk_score"], "component_delta_explanation": {"roe_pbr_capital_return_score": "guarded_to_15", "valuation_repricing_score": "cap_without_capital_return", "execution_risk_score": "+10"}, "MFE_90D_pct": 35.24, "MAE_90D_pct": -24.64, "score_return_alignment_label": "counterexample_guard_needed", "current_profile_verdict": "current_profile_false_positive"}
```

### 25.5 residual_contribution row

```jsonl
{"row_type": "residual_contribution", "round": "R6", "loop": "44", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "new_independent_case_count": 3, "reused_case_count": 0, "new_symbol_count": 3, "same_archetype_new_symbol_count": 3, "same_archetype_new_trigger_family_count": 4, "new_canonical_archetype_count": 0, "new_trigger_family_count": 4, "positive_case_count": 2, "counterexample_count": 1, "current_profile_error_count": 1, "tested_existing_calibrated_axes": ["price_only_blowoff_blocks_positive_stage", "full_4b_requires_non_price_evidence", "stage3_green_revision_min"], "residual_error_types_found": ["digital_bank_high_pbr_false_positive", "capital_return_policy_needs_explicit_commitment"], "loop_contribution_label": "canonical_archetype_rule_candidate", "do_not_propose_new_weight_delta": false, "auto_selected_coverage_gap": "L6/C21 financial ROE/PBR capital-return rerating undercovered relative to R1/R2/R12/R13"}
```

### 25.6 narrative_only rows

```jsonl
{"row_type":"narrative_only","case_id":"R6L44-C21-001-MERITZ-20221121","symbol":"138040","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","reason":"original_2022_11_21_event_forward_window_overlaps_2023_02_21_and_2023_04_25_corporate_action_candidate_dates","price_source":"Songdaiki/stock-web","usage":"not_weight_calibration"}
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
next_round = R6/C22 insurance rate-cycle reserve or R8 platform/content/SW/security holdout
priority = add C22 insurance positive/counterexample and test whether C21 capital-return bonus wrongly leaks into insurance reserve-cycle cases
```

## 28. Source Notes

- Stock price source: Songdaiki/stock-web, FinanceData/marcap transformed into assistant-readable symbol-year CSV shards.
- Manifest max_date used for forward-window availability: 2026-02-20.
- This MD intentionally does not open or infer `stock_agent/src/e2r` production implementation.
- Event evidence is treated as historical public evidence. Quantitative calibration uses only stock-web tradable OHLC rows.
- 메리츠금융지주의 2022 initial event is recorded as narrative-only because the direct forward window overlaps corporate-action candidate dates; the representative calibration row starts after the 2023-04-25 candidate date.
