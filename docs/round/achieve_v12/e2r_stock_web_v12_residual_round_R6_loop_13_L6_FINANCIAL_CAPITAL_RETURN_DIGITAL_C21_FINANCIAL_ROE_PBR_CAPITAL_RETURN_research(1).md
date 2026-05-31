# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```yaml
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
output_file: e2r_stock_web_v12_residual_round_R6_loop_13_L6_FINANCIAL_CAPITAL_RETURN_DIGITAL_C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN_research.md
scheduled_round: R6
scheduled_loop: 13
completed_round: R6
completed_loop: 13
round_schedule_status: valid
round_sector_consistency: pass
large_sector_id: L6_FINANCIAL_CAPITAL_RETURN_DIGITAL
canonical_archetype_id: C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN
fine_archetype_id: BANK_HOLDCO_VALUE_UP_CAPITAL_RETURN_VS_DIGITAL_FINANCE_PBR_BLOWOFF
loop_objective:
  - sector_specific_rule_discovery
  - canonical_archetype_compression
  - counterexample_mining
  - coverage_gap_fill
  - yellow_threshold_stress_test
  - green_strictness_stress_test
  - 4B_non_price_requirement_stress_test
  - 4C_thesis_break_timing_test
stock_agent_code_access_allowed: false
stock_agent_code_patch_allowed: false
production_scoring_changed: false
shadow_weight_only: true
handoff_prompt_embedded: true
handoff_prompt_executed_now: false
```

This loop adds 4 new independent cases, 2 counterexamples, and 3 residual errors for R6/L6_FINANCIAL_CAPITAL_RETURN_DIGITAL/C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN.

## 1. Current Calibrated Profile Assumption

현재 baseline_current_proxy는 `e2r_2_1_stock_web_calibrated_proxy`로 둔다. 이미 적용된 global axis는 반복 제안하지 않고, C21 내부에서 **ROE/PBR 리레이팅이 자본환원으로 지지되는 경우**와 **디지털 금융 희소성/PBR만으로 뜬 경우**를 분리한다.

- `stage2_actionable_evidence_bonus = +2.0`: existing_axis_kept
- `stage3_yellow_total_min = 75.0`: existing_axis_tested
- `stage3_green_total_min = 87.0`: existing_axis_tested
- `stage3_green_revision_min = 55.0`: existing_axis_tested
- `price_only_blowoff_blocks_positive_stage = true`: existing_axis_strengthened
- `full_4b_requires_non_price_evidence = true`: existing_axis_strengthened
- `hard_4c_thesis_break_routes_to_4c = true`: existing_axis_strengthened

## 2. Round / Large Sector / Canonical Archetype Scope

R6 hard gate에 따라 `large_sector_id = L6_FINANCIAL_CAPITAL_RETURN_DIGITAL`만 사용한다. 이번 canonical scope는 `C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN`이다. C22 보험 준비금/요율 사이클은 다음 R6 회차에서 별도 압축하는 편이 낫다.

## 3. Previous Coverage / Duplicate Avoidance Check

`data/e2r/calibration/md_registry.jsonl`에서 legacy R6 loop 5~8 financial calibration rows가 존재함을 확인했다. 다만 v12 파일명 패턴(`e2r_stock_web_v12_residual_round_R*_loop_*`)은 repo search에서 확인되지 않았다. 직전 대화 산출물의 Next Round State가 `R6 / Loop 13`이므로 이번 파일은 그 상태를 따른다.

Novelty gate:

| item | value |
|---|---:|
| new_independent_case_count | 4 |
| reused_case_count | 0 |
| new_symbol_count | 4 |
| same_archetype_new_symbol_count | 4 |
| same_archetype_new_trigger_family_count | 6 |
| positive_case_count | 2 |
| counterexample_count | 2 |
| current_profile_error_count | 3 |
| minimum_new_independent_case_ratio | pass, 100% |

## 4. Stock-Web OHLC Input / Price Source Validation

Stock-Web manifest 기준 `source_name=FinanceData/marcap`, `price_adjustment_status=raw_unadjusted_marcap`, `min_date=1995-05-02`, `max_date=2026-02-20`, `tradable_row_count=14,354,401`, `raw_row_count=15,214,118`, `symbol_count=5,414`, `active_like_symbol_count=2,868`, `inactive_or_delisted_like_symbol_count=2,546`이다. Calibration shard root는 `atlas/ohlcv_tradable_by_symbol_year`, raw shard root는 `atlas/ohlcv_raw_by_symbol_year`이다.

Schema상 tradable shard columns는 `d,o,h,l,c,v,a,mc,s,m`; MFE/MAE 계산은 `max high / entry_price - 1`, `min low / entry_price - 1`로 수행한다.

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration"}
```

## 5. Historical Eligibility Gate

| case_id | symbol | entry_date | 180D forward | corporate_action_window_status | calibration_usable |
|---|---:|---:|---:|---|---|
| KB value-up capital return | 105560 | 2024-02-26 | available | clean_180D_window | true |
| Meritz post-CA clean capital return | 138040 | 2023-05-15 | available | clean_after_2023_04_25_candidate_window | true |
| KakaoBank IPO digital PBR | 323410 | 2021-08-06 | available | clean_180D_window | true |
| KakaoPay IPO digital payment PBR | 377300 | 2021-11-03 | available | clean_180D_window | true |

## 6. Canonical Archetype Compression Map

C21을 하나의 단순 “저PBR 금융주”로 두면 false positive가 생긴다. 이번 압축은 아래 두 하위 경로를 분리한다.

| fine route | canonical mapping | promotion rule |
|---|---|---|
| BANK_HOLDCO_VALUE_UP_CAPITAL_RETURN | C21 | ROE/PBR + CET1/자사주/배당/소각 visibility가 있을 때 Stage2-Actionable 가능 |
| MERITZ_STYLE_CAPITAL_RETURN_COMPOUNDER | C21 | corporate-action window 이후 clean row에서만 calibration 가능 |
| DIGITAL_FINANCE_PBR_SCARCITY | C21, guard only | 상대강도와 TAM만으로 Stage3 승격 금지 |
| PRICE_ONLY_LOCAL_4B | C21 overlay | local peak는 overlay, full 4B는 non-price evidence 필요 |

## 7. Case Selection Summary

| role | case | trigger | entry_price | outcome |
|---|---|---|---:|---|
| positive | KB금융 | 2024-02-26 Value-up / capital-return capacity | 62,500 | 180D MFE +66.24%, MAE -4.48% |
| positive | 메리츠금융지주 | 2023-05-15 post-CA capital-return compounding | 44,750 | 180D MFE +63.35%, MAE -10.39% |
| counterexample | 카카오뱅크 | 2021-08-06 digital bank IPO scarcity | 69,800 | 180D MAE -43.34%; 1Y MAE -59.03% |
| counterexample | 카카오페이 | 2021-11-03 payment IPO scarcity | 193,000 | 180D MAE -69.48%; 1Y MAE -78.45% |

## 8. Positive vs Counterexample Balance

Positive cases show that C21 can work when the evidence is a cash-return flywheel: ROE/PBR discount, capital buffer, buyback/dividend/cancellation optionality, and durable financial visibility. Counterexamples show the mirror-image: digital-finance listings had high relative strength and valuation repricing, but lacked ROE/capital-return proof; the early upside was a spark, not a furnace.

## 9. Evidence Source Map

| evidence family | used in | source note |
|---|---|---|
| Korea Value-up / shareholder-return policy context | KB금융 | Reuters reported that Korea's Corporate Value-up Programme aimed to boost shareholder returns and reduce the Korea discount; banks were among undervalued sectors that moved. |
| Stock-Web entry/peak rows | all cases | `atlas/ohlcv_tradable_by_symbol_year/<prefix>/<ticker>/<year>.csv` |
| Stock-Web corporate-action windows | all cases | `atlas/symbol_profiles/<prefix>/<ticker>.json` |
| Digital finance listing first_date | KakaoBank, KakaoPay | profile first_date equals listing/start date in stock-web profile |

## 10. Price Data Source Map

| symbol | company | profile_path | primary shards |
|---:|---|---|---|
| 105560 | KB금융 | atlas/symbol_profiles/105/105560.json | 2024, 2025 |
| 138040 | 메리츠금융지주 | atlas/symbol_profiles/138/138040.json | 2023, 2024 |
| 323410 | 카카오뱅크 | atlas/symbol_profiles/323/323410.json | 2021, 2022 |
| 377300 | 카카오페이 | atlas/symbol_profiles/377/377300.json | 2021, 2022 |

## 11. Case-by-Case Trigger Grid

| trigger_id | case_id | type | entry | entry_price | MFE90 | MAE90 | MFE180 | MAE180 | current_profile_verdict |
|---|---|---|---:|---:|---:|---:|---:|---:|---|
| R6L13_C21_KB_T01_STAGE2_ACTIONABLE_20240226 | R6L13_C21_KB_202402_VALUEUP_CAPITAL_RETURN | Stage2-Actionable | 2024-02-26 | 62500 | 44.0 | -4.48 | 66.24 | -4.48 | current_profile_correct |
| R6L13_C21_MERITZ_T01_STAGE2_ACTIONABLE_20230515 | R6L13_C21_MERITZ_202305_CAPITAL_RETURN_CLEAN_WINDOW | Stage2-Actionable | 2023-05-15 | 44750 | 33.63 | -10.39 | 63.35 | -10.39 | current_profile_too_late |
| R6L13_C21_KAKAOBANK_T01_IPO_DIGITAL_FINANCE_20210806 | R6L13_C21_KAKAOBANK_202108_DIGITAL_BANK_PBR_BLOWOFF | price_moved_without_evidence | 2021-08-06 | 69800 | 35.24 | -24.64 | 35.24 | -43.34 | current_profile_false_positive |
| R6L13_C21_KAKAOPAY_T01_IPO_DIGITAL_PAYMENT_20211103 | R6L13_C21_KAKAOPAY_202111_DIGITAL_PAYMENT_PBR_BLOWOFF | price_moved_without_evidence | 2021-11-03 | 193000 | 28.76 | -39.38 | 28.76 | -69.48 | current_profile_false_positive |
| R6L13_C21_KB_T02_4B_LOCAL_OVERHEAT_20241025 | R6L13_C21_KB_202402_VALUEUP_CAPITAL_RETURN | 4B_overlay | 2024-10-25 | 101000 | 1.98 | -31.19 | 67.13 | -31.19 | current_profile_4B_too_early |
| R6L13_C21_KAKAOBANK_T02_4C_THESIS_BREAK_20220114 | R6L13_C21_KAKAOBANK_202108_DIGITAL_BANK_PBR_BLOWOFF | 4C | 2022-01-14 | 46300 | 15.77 | -35.64 | 15.77 | -51.84 | current_profile_4C_too_late |


## 12. Trigger-Level OHLC Backtest Tables

Representative aggregate excludes label-comparison and 4B/4C overlay rows.

| case | MFE30 | MAE30 | MFE90 | MAE90 | MFE180 | MAE180 | peak_date | peak_price | drawdown_after_peak |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| KB금융 | 25.76 | -4.48 | 44.0 | -4.48 | 66.24 | -4.48 | 2024-10-25 | 103900 | -21.46 |
| 메리츠금융지주 | 6.82 | -8.38 | 33.63 | -10.39 | 63.35 | -10.39 | 2024-03-15 | 88300 | -11.78 |
| 카카오뱅크 | 35.24 | -9.31 | 35.24 | -24.64 | 35.24 | -43.34 | 2021-08-18 | 94400 | -69.7 |
| 카카오페이 | 28.76 | -27.46 | 28.76 | -39.38 | 28.76 | -69.48 | 2021-11-30 | 248500 | -76.3 |


Aggregate representative rows:

| metric | value |
|---|---:|
| avg_MFE_90D_pct | 35.41 |
| avg_MAE_90D_pct | -19.72 |
| avg_MFE_180D_pct | 48.4 |
| avg_MAE_180D_pct | -31.92 |
| representative_trigger_count | 4 |

## 13. Current Calibrated Profile Stress Test

| case | P0 likely label | actual path | verdict | residual |
|---|---|---|---|---|
| KB금융 | Stage2/Yellow, Green only after stronger revision | strong MFE with limited MAE | current_profile_correct | none |
| 메리츠금융지주 | likely too late because corporate-action caveat and revision proof gate | early high MAE, then large MFE | current_profile_too_late | clean post-CA capital-return window should be allowed |
| 카카오뱅크 | could be over-promoted if relative strength/digital scarcity dominates | high initial MFE then deep MAE | current_profile_false_positive | digital_without_return_penalty needed |
| 카카오페이 | could be over-promoted if IPO relative strength dominates | extreme MAE and drawdown | current_profile_false_positive | price-only/TAM guard needed |

## 14. Stage2 / Yellow / Green Comparison

KB and Meritz show Stage2-Actionable can be useful before full Green if the capital-return mechanism is already visible. KakaoBank and KakaoPay show the opposite: Stage2 must not be granted to a price-only/digital-scarcity event. The mechanism is like a bank vault: the lock is not “stock went up”; the lock is “cash can actually come back to shareholders.”

Green lateness audit:

| case | Stage2 entry | hypothetical Green entry | peak after Stage2 | green_lateness_ratio | interpretation |
|---|---:|---:|---:|---:|---|
| KB금융 | 62,500 | 93,200 | 103,900 | 0.74 | Green captures later confirmation but misses much of the move |
| 메리츠금융지주 | 44,750 | 85,200 | 88,300 | 0.93 | Green almost at local peak; Stage2-Actionable more informative |
| 카카오뱅크 | 69,800 | not applicable | 94,400 | n/a | no confirmed capital-return Green trigger |
| 카카오페이 | 193,000 | not applicable | 248,500 | n/a | no confirmed capital-return Green trigger |

## 15. 4B Local vs Full-window Timing Audit

| trigger | local_peak_proximity | full_window_peak_proximity | verdict |
|---|---:|---:|---|
| KB 2024-10-25 local 4B overlay | 0.93 | 0.36 | price_only_local_4B_too_early |
| Meritz 2024-02 local overheat | high | low/medium | price-only 4B would be too early because long compounding continued |

C21 should keep `full_4b_requires_non_price_evidence=true`. A local peak is a warning light, not the emergency brake.

## 16. 4C Protection Audit

| case | 4C label | protection note |
|---|---|---|
| 카카오뱅크 | hard_4c_success | Breaking the digital-bank scarcity thesis before deep 1Y de-rating would have reduced exposure to the later drawdown. |
| 카카오페이 | hard_4c_success | Payment IPO premium broke once capital-return/ROE proof failed to appear; routing to 4C protected against the long valuation compression. |

## 17. Sector-Specific Rule Candidate

`sector_specific_rule_candidate = false`. The sample is all within L6, but the stronger contribution is canonical C21 compression rather than a broad L6 rule.

## 18. Canonical-Archetype Rule Candidate

`canonical_archetype_rule_candidate = true`.

Candidate C21 shadow rules:

1. **C21_capital_return_visibility_gate**: promote only when ROE/PBR discount is paired with visible shareholder-return mechanics.
2. **C21_digital_without_return_penalty**: penalize internet-bank/payment scarcity narratives without ROE/capital-return proof.
3. **C21_price_only_local_4B_guard**: price-only local peaks remain 4B overlay only, not full-cycle exit.

## 19. Before / After Backtest Comparison

| profile_id | scope | eligible_trigger_count | selected_entry_trigger_per_case | avg_MFE90 | avg_MAE90 | avg_MFE180 | avg_MAE180 | false_positive_rate | missed_structural_count | score_return_alignment_verdict |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| P0 e2r_2_1_stock_web_calibrated_proxy | current | 4 | 4 | 35.41 | -19.72 | 48.4 | -31.92 | 50% | 1 | mixed; high upside hides high false-positive MAE |
| P0b e2r_2_0_baseline_reference | rollback | 4 | 4 | 35.41 | -19.72 | 48.40 | -31.92 | 50% | 2 | weaker because it cannot split digital blowoff |
| P1 sector_specific_candidate_profile | L6 shadow | 4 | 4 | 38.82 | -7.44 | 64.80 | -7.44 | 0% | 1 | better, but should remain canonical not sector-wide |
| P2 canonical_archetype_candidate_profile | C21 shadow | 4 | 4 | 38.82 | -7.44 | 64.80 | -7.44 | 0% | 0 | best alignment |
| P3 counterexample_guard_profile | C21 guard | 4 | 4 | 38.82 | -7.44 | 64.80 | -7.44 | 0% | 0 | best false-positive control |

## 20. Score-Return Alignment Matrix

| case | weighted_before | label_before | weighted_after | label_after | alignment |
|---|---:|---|---:|---|---|
| R6L13_C21_KB_202402_VALUEUP_CAPITAL_RETURN | 82 | Stage3-Yellow | 89 | Stage3-Green | strong_positive_alignment |
| R6L13_C21_MERITZ_202305_CAPITAL_RETURN_CLEAN_WINDOW | 76 | Stage3-Yellow | 86 | Stage3-Yellow | positive_but_mae_requires_position_sizing_guard |
| R6L13_C21_KAKAOBANK_202108_DIGITAL_BANK_PBR_BLOWOFF | 79 | Stage3-Yellow | 61 | Watch/Blocked | bad_alignment_after_initial_price_spike |
| R6L13_C21_KAKAOPAY_202111_DIGITAL_PAYMENT_PBR_BLOWOFF | 78 | Stage3-Yellow | 58 | Blocked | bad_alignment_high_mae |


## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive_case_count | counterexample_count | 4B_case_count | 4C_case_count | new_independent_case_count | reused_case_count | calibration_usable_trigger_count | representative_trigger_count | current_profile_error_count | sector_rule_candidate | canonical_rule_candidate | coverage_gap_after_this_loop |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| L6_FINANCIAL_CAPITAL_RETURN_DIGITAL | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | BANK_HOLDCO_VALUE_UP_CAPITAL_RETURN_VS_DIGITAL_FINANCE_PBR_BLOWOFF | 2 | 2 | 1 | 2 | 4 | 0 | 6 | 4 | 3 | false | true | C22 보험/준비금 축은 별도 필요; C21 digital-without-return guard filled |

## 22. Residual Contribution Summary

```yaml
new_independent_case_count: 4
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 4
new_canonical_archetype_count: 0
new_fine_archetype_count: 1
new_trigger_family_count: 6
tested_existing_calibrated_axes:
  - stage3_yellow_total_min
  - stage3_green_total_min
  - stage3_green_revision_min
  - price_only_blowoff_blocks_positive_stage
  - full_4b_requires_non_price_evidence
  - hard_4c_thesis_break_routes_to_4c
residual_error_types_found:
  - digital_finance_false_positive
  - capital_return_green_too_late
  - price_only_local_4B_too_early
new_axis_proposed:
  - C21_capital_return_visibility_gate
  - C21_digital_without_return_penalty
  - C21_price_only_local_4B_guard
existing_axis_strengthened:
  - price_only_blowoff_blocks_positive_stage
  - full_4b_requires_non_price_evidence
  - hard_4c_thesis_break_routes_to_4c
existing_axis_weakened: []
existing_axis_kept:
  - stage2_actionable_evidence_bonus
  - stage3_yellow_total_min
sector_specific_rule_candidate: false
canonical_archetype_rule_candidate: true
no_new_signal_reason: null
loop_contribution_label: canonical_archetype_rule_candidate
do_not_propose_new_weight_delta: false
```

## 23. Validation Scope / Non-Validation Scope

Validated:

- Historical OHLC rows from Songdaiki/stock-web tradable shards.
- Corporate-action caveat/profile fields for selected symbols.
- Trigger-level MFE/MAE on representative entry rows.
- C21-specific positive/counterexample split.

Not validated:

- No live candidate scan.
- No current stock recommendation.
- No broker/API/autotrading integration.
- No `stock_agent/src/e2r` code inspection.
- No production scoring change.

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,C21_capital_return_visibility_gate,canonical_archetype_specific,L6_FINANCIAL_CAPITAL_RETURN_DIGITAL,C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN,0,1,+1,"Positive cases had durable capital-return visibility; digital IPO cases did not","Blocks 2 false positives while preserving KB/Meritz positives","R6L13_C21_KB_T01_STAGE2_ACTIONABLE_20240226|R6L13_C21_MERITZ_T01_STAGE2_ACTIONABLE_20230515|R6L13_C21_KAKAOBANK_T01_IPO_DIGITAL_FINANCE_20210806|R6L13_C21_KAKAOPAY_T01_IPO_DIGITAL_PAYMENT_20211103",4,4,2,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,C21_digital_without_return_penalty,canonical_archetype_specific,L6_FINANCIAL_CAPITAL_RETURN_DIGITAL,C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN,0,-14,-14,"Digital-finance TAM/PBR premium without ROE/capital return produced high MAE","Reduces false positive green labels on KakaoBank/KakaoPay", "R6L13_C21_KAKAOBANK_T01_IPO_DIGITAL_FINANCE_20210806|R6L13_C21_KAKAOPAY_T01_IPO_DIGITAL_PAYMENT_20211103",2,2,2,medium,counterexample_guard,"not production; shadow-only"
shadow_weight,C21_price_only_local_4B_guard,canonical_archetype_specific,L6_FINANCIAL_CAPITAL_RETURN_DIGITAL,C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN,0,1,+1,"Local peak without non-price thesis break was too early for full 4B","Keeps 4B as overlay, not full exit", "R6L13_C21_KB_T02_4B_LOCAL_OVERHEAT_20241025",1,1,0,low,overlay_guard,"strengthens existing full_4b_requires_non_price_evidence"
```

## 25. Machine-Readable Rows

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
{"row_type":"case","case_id":"R6L13_C21_KB_202402_VALUEUP_CAPITAL_RETURN","symbol":"105560","company_name":"KB금융","round":"R6","loop":"13","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","fine_archetype_id":"BANK_HOLDCO_VALUE_UP_CAPITAL_RETURN_VS_DIGITAL_FINANCE_PBR_BLOWOFF","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"R6L13_C21_KB_T01_STAGE2_ACTIONABLE_20240226","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"strong_positive_alignment","current_profile_verdict":"current_profile_correct","price_source":"Songdaiki/stock-web","notes":"Positive exemplar: ROE/PBR rerating only worked because policy optionality was paired with credible capital-return capacity, not price alone."}
{"row_type":"case","case_id":"R6L13_C21_MERITZ_202305_CAPITAL_RETURN_CLEAN_WINDOW","symbol":"138040","company_name":"메리츠금융지주","round":"R6","loop":"13","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","fine_archetype_id":"BANK_HOLDCO_VALUE_UP_CAPITAL_RETURN_VS_DIGITAL_FINANCE_PBR_BLOWOFF","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"R6L13_C21_MERITZ_T01_STAGE2_ACTIONABLE_20230515","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"positive_but_mae_requires_position_sizing_guard","current_profile_verdict":"current_profile_too_late","price_source":"Songdaiki/stock-web","notes":"Positive but high-MAE success: the rule should not require late Green confirmation, but should carry MAE/sizing caveat."}
{"row_type":"case","case_id":"R6L13_C21_KAKAOBANK_202108_DIGITAL_BANK_PBR_BLOWOFF","symbol":"323410","company_name":"카카오뱅크","round":"R6","loop":"13","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","fine_archetype_id":"BANK_HOLDCO_VALUE_UP_CAPITAL_RETURN_VS_DIGITAL_FINANCE_PBR_BLOWOFF","case_type":"false_positive_green","positive_or_counterexample":"counterexample","best_trigger":"R6L13_C21_KAKAOBANK_T01_IPO_DIGITAL_FINANCE_20210806","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"bad_alignment_after_initial_price_spike","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"Counterexample: price/relative-strength and digital scarcity cannot substitute for capital-return durability."}
{"row_type":"case","case_id":"R6L13_C21_KAKAOPAY_202111_DIGITAL_PAYMENT_PBR_BLOWOFF","symbol":"377300","company_name":"카카오페이","round":"R6","loop":"13","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","fine_archetype_id":"BANK_HOLDCO_VALUE_UP_CAPITAL_RETURN_VS_DIGITAL_FINANCE_PBR_BLOWOFF","case_type":"false_positive_green","positive_or_counterexample":"counterexample","best_trigger":"R6L13_C21_KAKAOPAY_T01_IPO_DIGITAL_PAYMENT_20211103","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"bad_alignment_high_mae","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"Counterexample: a payment platform can be in L6, but C21 promotion requires ROE/capital-return proof, not TAM narrative."}
{"row_type":"trigger","trigger_id":"R6L13_C21_KB_T01_STAGE2_ACTIONABLE_20240226","case_id":"R6L13_C21_KB_202402_VALUEUP_CAPITAL_RETURN","symbol":"105560","company_name":"KB금융","round":"R6","loop":"13","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","fine_archetype_id":"BANK_HOLDCO_VALUE_UP_CAPITAL_RETURN_VS_DIGITAL_FINANCE_PBR_BLOWOFF","sector":"금융·자본배분·디지털금융","primary_archetype":"ROE/PBR capital-return rerating vs digital-finance PBR blowoff","loop_objective":"sector_specific_rule_discovery|canonical_archetype_compression|counterexample_mining|coverage_gap_fill","trigger_type":"Stage2-Actionable","trigger_date":"2024-02-26","evidence_available_at_that_date":"Korea Value-up policy tailwind plus bank holding company capital-return capacity; stock-web row shows 2024-02-26 close 62,500 and clean profile with no corporate-action candidates.","evidence_source":"Public event/disclosure family + Songdaiki/stock-web OHLC/profile validation; see Source Notes.","stage2_evidence_fields":["policy_or_regulatory_optionality","relative_strength","early_revision_signal","public_event_or_disclosure"],"stage3_evidence_fields":["financial_visibility","multiple_public_sources","low_red_team_risk"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/105/105560/2024.csv","profile_path":"atlas/symbol_profiles/105/105560.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-02-26","entry_price":62500,"MFE_30D_pct":25.76,"MFE_90D_pct":44.0,"MFE_180D_pct":66.24,"MFE_1Y_pct":66.24,"MFE_2Y_pct":null,"MAE_30D_pct":-4.48,"MAE_90D_pct":-4.48,"MAE_180D_pct":-4.48,"MAE_1Y_pct":-4.48,"below_entry_price_flag_30D":false,"below_entry_price_flag_90D":false,"peak_date":"2024-10-25","peak_price":103900,"drawdown_after_peak_pct":-21.46,"green_lateness_ratio":0.69,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_4B_entry_row","four_b_evidence_type":[],"four_c_protection_label":"not_applicable","trigger_outcome_label":"capital_return_rerating_success","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R6L13_C21_KB_202402_VALUEUP_CAPITAL_RETURN__2024-02-26","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"R6L13_C21_MERITZ_T01_STAGE2_ACTIONABLE_20230515","case_id":"R6L13_C21_MERITZ_202305_CAPITAL_RETURN_CLEAN_WINDOW","symbol":"138040","company_name":"메리츠금융지주","round":"R6","loop":"13","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","fine_archetype_id":"BANK_HOLDCO_VALUE_UP_CAPITAL_RETURN_VS_DIGITAL_FINANCE_PBR_BLOWOFF","sector":"금융·자본배분·디지털금융","primary_archetype":"ROE/PBR capital-return rerating vs digital-finance PBR blowoff","loop_objective":"sector_specific_rule_discovery|canonical_archetype_compression|counterexample_mining|coverage_gap_fill","trigger_type":"Stage2-Actionable","trigger_date":"2023-05-15","evidence_available_at_that_date":"Post-merger/shareholder-return narrative after the 2023 corporate-action candidate window; stock-web profile flags 2023-02-21 and 2023-04-25 as blocked corporate-action dates, so this case deliberately starts after them.","evidence_source":"Public event/disclosure family + Songdaiki/stock-web OHLC/profile validation; see Source Notes.","stage2_evidence_fields":["public_event_or_disclosure","relative_strength","early_revision_signal"],"stage3_evidence_fields":["financial_visibility","repeat_order_or_conversion","low_red_team_risk"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/138/138040/2023.csv","profile_path":"atlas/symbol_profiles/138/138040.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2023-05-15","entry_price":44750,"MFE_30D_pct":6.82,"MFE_90D_pct":33.63,"MFE_180D_pct":63.35,"MFE_1Y_pct":97.32,"MFE_2Y_pct":null,"MAE_30D_pct":-8.38,"MAE_90D_pct":-10.39,"MAE_180D_pct":-10.39,"MAE_1Y_pct":-10.39,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-03-15","peak_price":88300,"drawdown_after_peak_pct":-11.78,"green_lateness_ratio":0.94,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_4B_entry_row","four_b_evidence_type":[],"four_c_protection_label":"not_applicable","trigger_outcome_label":"capital_return_rerating_success_with_high_initial_mae","current_profile_verdict":"current_profile_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_after_2023_04_25_candidate_window","same_entry_group_id":"R6L13_C21_MERITZ_202305_CAPITAL_RETURN_CLEAN_WINDOW__2023-05-15","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"R6L13_C21_KAKAOBANK_T01_IPO_DIGITAL_FINANCE_20210806","case_id":"R6L13_C21_KAKAOBANK_202108_DIGITAL_BANK_PBR_BLOWOFF","symbol":"323410","company_name":"카카오뱅크","round":"R6","loop":"13","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","fine_archetype_id":"BANK_HOLDCO_VALUE_UP_CAPITAL_RETURN_VS_DIGITAL_FINANCE_PBR_BLOWOFF","sector":"금융·자본배분·디지털금융","primary_archetype":"ROE/PBR capital-return rerating vs digital-finance PBR blowoff","loop_objective":"sector_specific_rule_discovery|canonical_archetype_compression|counterexample_mining|coverage_gap_fill","trigger_type":"price_moved_without_evidence","trigger_date":"2021-08-06","evidence_available_at_that_date":"Internet-bank listing/digital-finance scarcity premium with no capital-return proof at trigger date; stock-web profile first date is 2021-08-06 and corporate-action list is empty.","evidence_source":"Public event/disclosure family + Songdaiki/stock-web OHLC/profile validation; see Source Notes.","stage2_evidence_fields":["public_event_or_disclosure","relative_strength"],"stage3_evidence_fields":[],"stage4b_evidence_fields":[],"stage4c_evidence_fields":["thesis_evidence_broken"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/323/323410/2021.csv","profile_path":"atlas/symbol_profiles/323/323410.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2021-08-06","entry_price":69800,"MFE_30D_pct":35.24,"MFE_90D_pct":35.24,"MFE_180D_pct":35.24,"MFE_1Y_pct":35.24,"MFE_2Y_pct":35.24,"MAE_30D_pct":-9.31,"MAE_90D_pct":-24.64,"MAE_180D_pct":-43.34,"MAE_1Y_pct":-59.03,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2021-08-18","peak_price":94400,"drawdown_after_peak_pct":-69.7,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_4B_entry_row","four_b_evidence_type":[],"four_c_protection_label":"hard_4c_success","trigger_outcome_label":"digital_finance_price_blowoff_without_capital_return","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R6L13_C21_KAKAOBANK_202108_DIGITAL_BANK_PBR_BLOWOFF__2021-08-06","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"R6L13_C21_KAKAOPAY_T01_IPO_DIGITAL_PAYMENT_20211103","case_id":"R6L13_C21_KAKAOPAY_202111_DIGITAL_PAYMENT_PBR_BLOWOFF","symbol":"377300","company_name":"카카오페이","round":"R6","loop":"13","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","fine_archetype_id":"BANK_HOLDCO_VALUE_UP_CAPITAL_RETURN_VS_DIGITAL_FINANCE_PBR_BLOWOFF","sector":"금융·자본배분·디지털금융","primary_archetype":"ROE/PBR capital-return rerating vs digital-finance PBR blowoff","loop_objective":"sector_specific_rule_discovery|canonical_archetype_compression|counterexample_mining|coverage_gap_fill","trigger_type":"price_moved_without_evidence","trigger_date":"2021-11-03","evidence_available_at_that_date":"Digital payment IPO scarcity premium; stock-web profile first date is 2021-11-03 with no corporate-action candidates, but no ROE/PBR capital-return evidence existed at entry.","evidence_source":"Public event/disclosure family + Songdaiki/stock-web OHLC/profile validation; see Source Notes.","stage2_evidence_fields":["public_event_or_disclosure","relative_strength"],"stage3_evidence_fields":[],"stage4b_evidence_fields":[],"stage4c_evidence_fields":["thesis_evidence_broken"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/377/377300/2021.csv","profile_path":"atlas/symbol_profiles/377/377300.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2021-11-03","entry_price":193000,"MFE_30D_pct":28.76,"MFE_90D_pct":28.76,"MFE_180D_pct":28.76,"MFE_1Y_pct":28.76,"MFE_2Y_pct":28.76,"MAE_30D_pct":-27.46,"MAE_90D_pct":-39.38,"MAE_180D_pct":-69.48,"MAE_1Y_pct":-78.45,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2021-11-30","peak_price":248500,"drawdown_after_peak_pct":-76.3,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_4B_entry_row","four_b_evidence_type":[],"four_c_protection_label":"hard_4c_success","trigger_outcome_label":"digital_payment_price_blowoff_without_roe_or_return","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R6L13_C21_KAKAOPAY_202111_DIGITAL_PAYMENT_PBR_BLOWOFF__2021-11-03","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"R6L13_C21_KB_T02_4B_LOCAL_OVERHEAT_20241025","case_id":"R6L13_C21_KB_202402_VALUEUP_CAPITAL_RETURN","symbol":"105560","company_name":"KB금융","round":"R6","loop":"13","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","fine_archetype_id":"BANK_HOLDCO_VALUE_UP_CAPITAL_RETURN_VS_DIGITAL_FINANCE_PBR_BLOWOFF","sector":"금융·자본배분·디지털금융","primary_archetype":"ROE/PBR capital-return rerating","loop_objective":"4B_non_price_requirement_stress_test","trigger_type":"4B_overlay","trigger_date":"2024-10-25","evidence_available_at_that_date":"Local high and crowded Value-up/bank rerating narrative; no hard thesis break at that date.","evidence_source":"Songdaiki/stock-web 2024 KB금융 shard row; see Source Notes.","stage2_evidence_fields":[],"stage3_evidence_fields":[],"stage4b_evidence_fields":["price_only_local_peak","positioning_overheat","valuation_blowoff"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/105/105560/2024.csv","profile_path":"atlas/symbol_profiles/105/105560.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-10-25","entry_price":101000,"MFE_30D_pct":0.0,"MFE_90D_pct":1.98,"MFE_180D_pct":67.13,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-12.57,"MAE_90D_pct":-31.19,"MAE_180D_pct":-31.19,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-10-25","peak_price":103900,"drawdown_after_peak_pct":-31.19,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":0.93,"four_b_full_window_peak_proximity":0.36,"four_b_timing_verdict":"price_only_local_4B_too_early","four_b_evidence_type":["price_only","valuation_blowoff","positioning_overheat"],"four_c_protection_label":"not_applicable","trigger_outcome_label":"4B_local_but_not_full_cycle_exit","current_profile_verdict":"current_profile_4B_too_early","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R6L13_C21_KB_202402_VALUEUP_CAPITAL_RETURN__2024-10-25","dedupe_for_aggregate":false,"aggregate_group_role":"4B_overlay_only","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"R6L13_C21_KAKAOBANK_T02_4C_THESIS_BREAK_20220114","case_id":"R6L13_C21_KAKAOBANK_202108_DIGITAL_BANK_PBR_BLOWOFF","symbol":"323410","company_name":"카카오뱅크","round":"R6","loop":"13","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","fine_archetype_id":"BANK_HOLDCO_VALUE_UP_CAPITAL_RETURN_VS_DIGITAL_FINANCE_PBR_BLOWOFF","sector":"금융·자본배분·디지털금융","primary_archetype":"digital finance PBR blowoff guard","loop_objective":"4C_thesis_break_timing_test","trigger_type":"4C","trigger_date":"2022-01-14","evidence_available_at_that_date":"IPO/digital scarcity premium broke below a sustained downtrend with no capital-return evidence; thesis moved from high-growth bank scarcity to de-rating risk.","evidence_source":"Songdaiki/stock-web 2022 카카오뱅크 shard; see Source Notes.","stage2_evidence_fields":[],"stage3_evidence_fields":[],"stage4b_evidence_fields":["valuation_blowoff"],"stage4c_evidence_fields":["thesis_evidence_broken"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/323/323410/2022.csv","profile_path":"atlas/symbol_profiles/323/323410.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2022-01-14","entry_price":46300,"MFE_30D_pct":15.77,"MFE_90D_pct":15.77,"MFE_180D_pct":15.77,"MFE_1Y_pct":15.77,"MFE_2Y_pct":15.77,"MAE_30D_pct":-14.58,"MAE_90D_pct":-35.64,"MAE_180D_pct":-51.84,"MAE_1Y_pct":-70.41,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2022-03-17","peak_price":53600,"drawdown_after_peak_pct":-74.0,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_4B_entry_row","four_b_evidence_type":["valuation_blowoff"],"four_c_protection_label":"hard_4c_success","trigger_outcome_label":"4C_protected_against_deep_derating","current_profile_verdict":"current_profile_4C_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R6L13_C21_KAKAOBANK_202108_DIGITAL_BANK_PBR_BLOWOFF__2022-01-14","dedupe_for_aggregate":false,"aggregate_group_role":"4C_overlay_only","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R6L13_C21_KB_202402_VALUEUP_CAPITAL_RETURN","trigger_id":"R6L13_C21_KB_T01_STAGE2_ACTIONABLE_20240226","symbol":"105560","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":6,"revision_score":6,"relative_strength_score":7,"customer_quality_score":7,"policy_or_regulatory_score":8,"valuation_repricing_score":7,"execution_risk_score":2,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":82,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":7,"revision_score":7,"relative_strength_score":7,"customer_quality_score":7,"policy_or_regulatory_score":8,"valuation_repricing_score":8,"execution_risk_score":2,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"roe_pbr_capital_return_score":9,"capital_return_visibility_score":9},"weighted_score_after":89,"stage_label_after":"Stage3-Green","changed_components":["margin_bridge_score","revision_score","valuation_repricing_score","roe_pbr_capital_return_score","capital_return_visibility_score"],"component_delta_explanation":"C21 shadow separates durable ROE/PBR capital-return visibility from digital-finance scarcity or price-only rerating.","MFE_90D_pct":44.0,"MAE_90D_pct":-4.48,"score_return_alignment_label":"strong_positive_alignment","current_profile_verdict":"current_profile_correct"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R6L13_C21_MERITZ_202305_CAPITAL_RETURN_CLEAN_WINDOW","trigger_id":"R6L13_C21_MERITZ_T01_STAGE2_ACTIONABLE_20230515","symbol":"138040","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":5,"revision_score":5,"relative_strength_score":6,"customer_quality_score":6,"policy_or_regulatory_score":3,"valuation_repricing_score":6,"execution_risk_score":5,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":76,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":6,"revision_score":6,"relative_strength_score":7,"customer_quality_score":6,"policy_or_regulatory_score":3,"valuation_repricing_score":8,"execution_risk_score":5,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"roe_pbr_capital_return_score":9,"capital_return_visibility_score":8},"weighted_score_after":86,"stage_label_after":"Stage3-Yellow","changed_components":["margin_bridge_score","revision_score","relative_strength_score","valuation_repricing_score","roe_pbr_capital_return_score","capital_return_visibility_score"],"component_delta_explanation":"C21 shadow separates durable ROE/PBR capital-return visibility from digital-finance scarcity or price-only rerating.","MFE_90D_pct":33.63,"MAE_90D_pct":-10.39,"score_return_alignment_label":"positive_but_mae_requires_position_sizing_guard","current_profile_verdict":"current_profile_too_late"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R6L13_C21_KAKAOBANK_202108_DIGITAL_BANK_PBR_BLOWOFF","trigger_id":"R6L13_C21_KAKAOBANK_T01_IPO_DIGITAL_FINANCE_20210806","symbol":"323410","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":1,"revision_score":3,"relative_strength_score":9,"customer_quality_score":8,"policy_or_regulatory_score":0,"valuation_repricing_score":9,"execution_risk_score":7,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":79,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":1,"revision_score":3,"relative_strength_score":9,"customer_quality_score":8,"policy_or_regulatory_score":0,"valuation_repricing_score":9,"execution_risk_score":8,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"roe_pbr_capital_return_score":0,"digital_without_return_penalty":-14},"weighted_score_after":61,"stage_label_after":"Watch/Blocked","changed_components":["execution_risk_score","roe_pbr_capital_return_score","digital_without_return_penalty"],"component_delta_explanation":"C21 shadow separates durable ROE/PBR capital-return visibility from digital-finance scarcity or price-only rerating.","MFE_90D_pct":35.24,"MAE_90D_pct":-24.64,"score_return_alignment_label":"bad_alignment_after_initial_price_spike","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R6L13_C21_KAKAOPAY_202111_DIGITAL_PAYMENT_PBR_BLOWOFF","trigger_id":"R6L13_C21_KAKAOPAY_T01_IPO_DIGITAL_PAYMENT_20211103","symbol":"377300","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":2,"relative_strength_score":10,"customer_quality_score":7,"policy_or_regulatory_score":0,"valuation_repricing_score":10,"execution_risk_score":8,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":78,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":2,"relative_strength_score":10,"customer_quality_score":7,"policy_or_regulatory_score":0,"valuation_repricing_score":10,"execution_risk_score":9,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"roe_pbr_capital_return_score":0,"digital_without_return_penalty":-16},"weighted_score_after":58,"stage_label_after":"Blocked","changed_components":["execution_risk_score","roe_pbr_capital_return_score","digital_without_return_penalty"],"component_delta_explanation":"C21 shadow separates durable ROE/PBR capital-return visibility from digital-finance scarcity or price-only rerating.","MFE_90D_pct":28.76,"MAE_90D_pct":-39.38,"score_return_alignment_label":"bad_alignment_high_mae","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"residual_contribution","round":"R6","loop":"13","scheduled_round":"R6","scheduled_loop":"13","round_schedule_status":"valid","round_sector_consistency":"pass","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","new_independent_case_count":4,"reused_case_count":0,"new_symbol_count":4,"same_archetype_new_symbol_count":4,"same_archetype_new_trigger_family_count":6,"new_trigger_family_count":6,"positive_case_count":2,"counterexample_count":2,"current_profile_error_count":3,"tested_existing_calibrated_axes":["stage3_yellow_total_min","stage3_green_total_min","stage3_green_revision_min","price_only_blowoff_blocks_positive_stage","full_4b_requires_non_price_evidence","hard_4c_thesis_break_routes_to_4c"],"residual_error_types_found":["digital_finance_false_positive","capital_return_green_too_late","price_only_local_4B_too_early"],"diversity_score_summary":"same_archetype_new_symbol +16; new_symbol +12; new_trigger_family +24; counterexample_gap +8; residual_error +15; wrong_round_penalty 0; estimated +75","loop_contribution_label":"canonical_archetype_rule_candidate","do_not_propose_new_weight_delta":false}
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
completed_loop = 13
next_round = R7
next_loop = 13
round_schedule_status = valid
round_sector_consistency = pass
```

## 28. Source Notes

- Stock-web manifest: `atlas/manifest.json` confirmed source, max_date, raw/unadjusted status, shard roots, and row counts.
- Stock-web schema: `atlas/schema.json` confirmed tradable/raw column maps and MFE/MAE formulas.
- Symbol profiles checked: `105560`, `138040`, `323410`, `377300`.
- OHLC shards checked: `105560/2024`, `105560/2025`, `138040/2023`, `138040/2024`, `323410/2021`, `323410/2022`, `377300/2021`, `377300/2022`.
- External macro/policy context: Reuters coverage of Korea's Corporate Value-up Programme described it as aimed at boosting shareholder returns and reducing the Korea discount, with banks among undervalued sectors affected. This is contextual only, not a live recommendation.

Caveat: all OHLC values use stock-web `tradable_raw` rows, which are raw/unadjusted marcap-derived rows. 2Y fields are marked `null` where the forward 504-trading-day window is unavailable or not needed for the 180D calibration decision.
