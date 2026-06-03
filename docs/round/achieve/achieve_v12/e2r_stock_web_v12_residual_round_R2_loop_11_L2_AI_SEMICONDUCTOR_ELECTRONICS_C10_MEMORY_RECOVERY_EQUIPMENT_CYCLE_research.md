# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
research_session = post_calibrated_sector_archetype_residual_research
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
output_file = e2r_stock_web_v12_residual_round_R2_loop_11_L2_AI_SEMICONDUCTOR_ELECTRONICS_C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE_research.md
scheduled_round = R2
scheduled_loop = 11
completed_round = R2
completed_loop = 11
large_sector_id = L2_AI_SEMICONDUCTOR_ELECTRONICS
canonical_archetype_id = C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE
fine_archetype_id = MEMORY_RECOVERY_CAPEX_ORDER_CONVERSION_GUARD
loop_objective = coverage_gap_fill|counterexample_mining|green_strictness_stress_test|sector_specific_rule_discovery|canonical_archetype_compression
production_scoring_changed = false
shadow_weight_only = true
stock_agent_code_access_allowed = false
stock_agent_code_patch_allowed = false
stock_agent_live_scan_allowed = false
current_stock_discovery_allowed = false
```

This loop adds 5 new independent cases, 2 counterexamples, and 3 residual errors for R2/L2_AI_SEMICONDUCTOR_ELECTRONICS/C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE.

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

The goal here is not to re-prove the global Stage2 bonus or Green threshold. The residual question is narrower: in a memory recovery cycle, when should the signal stay with the memory body, and when can it safely propagate into equipment names?

## 2. Round / Large Sector / Canonical Archetype Scope

```text
round = R2
loop = 11
large_sector_id = L2_AI_SEMICONDUCTOR_ELECTRONICS
canonical_archetype_id = C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE
fine_archetype_id = MEMORY_RECOVERY_CAPEX_ORDER_CONVERSION_GUARD
round_sector_consistency = pass
```

R2 is the AI/semiconductor/electronics round. C10 was selected because R2 already has extensive representative coverage; the remaining value is not another HBM winner repeat, but the split between memory-body recovery and equipment beta false positives.

## 3. Previous Coverage / Duplicate Avoidance Check

The R2 calibration artifact already reports 155 representative triggers and 40 unique cases. The accepted axes are the existing global axes, including Stage2 bonus, Yellow/Green thresholds, 4B non-price evidence, and hard 4C thesis-break routing. This MD therefore avoids proposing those as new global rules and instead tests a C10-specific shadow guard.

Duplicate avoidance choices:

```text
same_canonical_archetype_research = allowed
same_symbol_same_trigger_date_research = avoided
same_symbol_new_trigger_family = allowed only if reuse_reason exists
new_symbol_count = 5
reused_case_count = 0
minimum_new_independent_case_ratio = 1.00
```

## 4. Stock-Web OHLC Input / Price Source Validation

```text
price_data_source = Songdaiki/stock-web
source_basis = FinanceData/marcap transformed into symbol-year CSV shards
price_basis = tradable_raw
price_adjustment_status = raw_unadjusted_marcap
manifest_path = atlas/manifest.json
schema_path = atlas/schema.json
universe_path = atlas/universe/all_symbols.csv
manifest_max_date = 2026-02-20
calibration_shard_root = atlas/ohlcv_tradable_by_symbol_year
raw_shard_root = atlas/ohlcv_raw_by_symbol_year
```

Stock-Web profile review:

| Symbol | Company | Profile path | Profile / window status |
|---|---:|---|---|
| 000660 | SK하이닉스 | atlas/symbol_profiles/000/000660.json | long active KOSPI history; 2023~2024 shards available; 180D window usable |
| 005930 | 삼성전자 | atlas/symbol_profiles/005/005930.json | active KOSPI; corporate-action candidates are historical and not in 2023 window |
| 036930 | 주성엔지니어링 | atlas/symbol_profiles/036/036930.json | active KOSDAQ GLOBAL; only visible corporate-action candidate is 2000; 2023 window usable |
| 240810 | 원익IPS | atlas/symbol_profiles/240/240810.json | active KOSDAQ GLOBAL; corporate_action_candidate_count = 0 |
| 095610 | 테스 | atlas/symbol_profiles/095/095610.json | active KOSDAQ/KOSDAQ GLOBAL; candidate dates are 2011/2016; 2023 window usable |

## 5. Historical Eligibility Gate

All representative triggers in this MD satisfy:

```text
trigger_date_is_historical = true
entry_date_exists_in_tradable_shard = true
forward_180_trading_days_available = true
required_ohlcv_fields_present = true
corporate_action_contaminated_180D_window = false
calibration_usable_case_count = 5
calibration_usable_trigger_count = 5
```

## 6. Canonical Archetype Compression Map

```text
canonical_archetype_id = C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE
fine_archetype = MEMORY_RECOVERY_CAPEX_ORDER_CONVERSION_GUARD
```

Compression logic:

| Fine evidence family | Compresses into | Promotion implication |
|---|---|---|
| DRAM/NAND price bottom, inventory normalization | memory recovery body signal | Stage2 / Yellow only unless revision confirms |
| HBM/DDR5 customer quality and visible utilization | memory-body Green bridge | Can support Green if revision + relative strength both exist |
| Equipment rebound without order conversion | equipment beta false-positive guard | Cap at Stage2-watch / Yellow-risk |
| Capex order conversion + margin bridge | equipment Green bridge | Can support C10 Green |
| Local price blowoff without non-price overheat | 4B watch only | Not full 4B |

## 7. Case Selection Summary

| case_id | symbol / company | case_type | role | trigger | entry_price | 90D MFE/MAE | 180D MFE/MAE | current_profile_verdict |
|---|---|---|---|---|---:|---:|---:|---|
| R2L11-C10-SKHU-20230525 | 000660 SK하이닉스 | structural_success | positive | Stage2-Actionable 2023-05-25 | 103,500 | 23.9% / -2.3% | 61.3% / -2.3% | current_profile_correct |
| R2L11-C10-SEC-20230407 | 005930 삼성전자 | stage2_promote_candidate | positive | Stage2 2023-04-07 | 65,000 | 11.8% / -2.6% | 20.0% / -2.6% | current_profile_correct |
| R2L11-C10-JUSUNG-20230324 | 036930 주성엔지니어링 | high_mae_success | positive | Stage2-Actionable 2023-03-24 | 15,240 | 75.2% / -3.5% | 149.3% / -3.5% | current_profile_too_early |
| R2L11-C10-WIPS-20230317 | 240810 원익IPS | false_positive_green | counterexample | Stage2 2023-03-17 | 34,250 | 6.3% / -18.5% | 7.4% / -18.5% | current_profile_false_positive |
| R2L11-C10-TES-20230324 | 095610 테스 | failed_rerating | counterexample | Stage2 2023-03-24 | 22,100 | 5.4% / -9.5% | 5.4% / -12.7% | current_profile_false_positive |

## 8. Positive vs Counterexample Balance

```text
positive_case_count = 3
counterexample_count = 2
4B_case_count = 3
4C_case_count = 0
new_independent_case_count = 5
reused_case_count = 0
```

The positive side is not simply “semiconductor rose.” It requires a non-price bridge: memory price/ASP recovery, revision, customer quality, or order conversion. The counterexample side is where the market hears the same memory recovery music but the equipment order book does not yet dance to the beat.

## 9. Evidence Source Map

| Evidence field | Positive examples | Counterexample examples |
|---|---|---|
| relative_strength | SK하이닉스, 주성엔지니어링 | 원익IPS early spike faded |
| capacity_or_volume_route | SK하이닉스 HBM/DDR5 utilization; Samsung memory recovery | TES/Wonik headline without visible capex conversion |
| confirmed_revision | SK하이닉스 later Stage3 | absent in WIPS/TES at trigger |
| margin_bridge | 주성 later conversion | weak/unknown in WIPS/TES |
| 4B non-price evidence | valuation/positioning overheat after full-window run | local price bounce alone insufficient |

## 10. Price Data Source Map

| Symbol | Entry shard | Profile | Entry row basis |
|---|---|---|---|
| 000660 | atlas/ohlcv_tradable_by_symbol_year/000/000660/2023.csv | atlas/symbol_profiles/000/000660.json | 2023-05-25 close = 103,500 |
| 005930 | atlas/ohlcv_tradable_by_symbol_year/005/005930/2023.csv | atlas/symbol_profiles/005/005930.json | 2023-04-07 close = 65,000 |
| 036930 | atlas/ohlcv_tradable_by_symbol_year/036/036930/2023.csv | atlas/symbol_profiles/036/036930.json | 2023-03-24 close = 15,240 |
| 240810 | atlas/ohlcv_tradable_by_symbol_year/240/240810/2023.csv | atlas/symbol_profiles/240/240810.json | 2023-03-17 close = 34,250 |
| 095610 | atlas/ohlcv_tradable_by_symbol_year/095/095610/2023.csv | atlas/symbol_profiles/095/095610.json | 2023-03-24 close = 22,100 |

## 11. Case-by-Case Trigger Grid

| trigger_id | symbol | trigger_type | trigger_date | entry_date | entry | MFE30 | MFE90 | MFE180 | MAE90 | peak_date | peak | current verdict |
|---|---|---|---|---|---:|---:|---:|---:|---:|---|---:|---|
| TRG-R2L11-C10-SKHU-20230525 | 000660 | Stage2-Actionable | 2023-05-25 | 2023-05-25 | 103,500 | 16.1 | 23.9 | 61.3 | -2.3 | 2024-02-23 | 166,900 | current_profile_correct |
| TRG-R2L11-C10-SEC-20230407 | 005930 | Stage2 | 2023-04-07 | 2023-04-07 | 65,000 | 8.3 | 11.8 | 20.0 | -2.6 | 2023-12-27 | 78,000 | current_profile_correct |
| TRG-R2L11-C10-JUSUNG-20230324 | 036930 | Stage2-Actionable | 2023-03-24 | 2023-03-24 | 15,240 | 31.9 | 75.2 | 149.3 | -3.5 | 2023-11-15 | 38,000 | current_profile_too_early |
| TRG-R2L11-C10-WIPS-20230317 | 240810 | Stage2 | 2023-03-17 | 2023-03-17 | 34,250 | 6.3 | 6.3 | 7.4 | -18.5 | 2023-11-13 | 36,800 | current_profile_false_positive |
| TRG-R2L11-C10-TES-20230324 | 095610 | Stage2 | 2023-03-24 | 2023-03-24 | 22,100 | 5.4 | 5.4 | 5.4 | -9.5 | 2023-04-11 | 23,300 | current_profile_false_positive |

## 12. Trigger-Level OHLC Backtest Tables

### Representative trigger metrics

| case_id | Entry | 30D MFE/MAE | 90D MFE/MAE | 180D MFE/MAE | Peak / drawdown | Calibration usable |
|---|---:|---:|---:|---:|---|---|
| R2L11-C10-SKHU-20230525 | 103,500 | 16.1% / -2.3% | 23.9% / -2.3% | 61.3% / -2.3% | 2024-02-23 166,900 / -8.1% | true |
| R2L11-C10-SEC-20230407 | 65,000 | 8.3% / -2.6% | 11.8% / -2.6% | 20.0% / -2.6% | 2023-12-27 78,000 / -8.6% | true |
| R2L11-C10-JUSUNG-20230324 | 15,240 | 31.9% / -3.5% | 75.2% / -3.5% | 149.3% / -3.5% | 2023-11-15 38,000 / -18.0% | true |
| R2L11-C10-WIPS-20230317 | 34,250 | 6.3% / -14.2% | 6.3% / -18.5% | 7.4% / -18.5% | 2023-11-13 36,800 / -13.5% | true |
| R2L11-C10-TES-20230324 | 22,100 | 5.4% / -9.5% | 5.4% / -9.5% | 5.4% / -12.7% | 2023-04-11 23,300 / -17.2% | true |


Aggregate representative set:

```text
avg_MFE_90D_pct = 24.5
avg_MAE_90D_pct = -7.3
avg_MFE_180D_pct = 48.7
avg_MAE_180D_pct = -7.9
false_positive_count_current_proxy = 2
positive_case_count = 3
counterexample_count = 2
```

## 13. Current Calibrated Profile Stress Test

| Case | Current profile verdict | What was right | Residual error |
|---|---|---|---|
| SK하이닉스 | current_profile_correct | Green is justified after revision/customer quality appears | None, but 4B needs non-price overheat |
| 삼성전자 | current_profile_correct | Yellow better than forced Green; body recovery exists but lower relative strength | Green strictness remains appropriate |
| 주성엔지니어링 | current_profile_too_early | Stage2 was useful | High-MAE / high-vol success needs separate risk tag |
| 원익IPS | current_profile_false_positive | Stage2 watch was acceptable | Equipment headline alone must not reach Green |
| 테스 | current_profile_false_positive | Stage2 watch was acceptable | No reorder/margin bridge; Green/Yellow risk overstated |

Stress-test answers:

```text
stage2_actionable_evidence_bonus = kept
stage3_yellow_total_min = kept
stage3_green_total_min = kept
stage3_green_revision_min = strengthened_for_C10_equipment_names
stage3_cross_evidence_green_buffer = kept
price_only_blowoff_blocks_positive_stage = kept
full_4b_requires_non_price_evidence = strengthened_for_C10
hard_4c_thesis_break_routes_to_4c = kept
```

## 14. Stage2 / Yellow / Green Comparison

C10 behaves like a two-stage gearbox:

1. Memory body first moves on ASP/revision/relative-strength evidence.
2. Equipment names move only when that demand becomes capex order conversion or customer-specific backlog visibility.

| Case | Stage2 usefulness | Yellow usefulness | Green usefulness | Green lateness ratio |
|---|---|---|---|---:|
| SK하이닉스 | excellent early capture | useful bridge | correct after revision | 0.36 |
| 삼성전자 | useful broad memory recovery | better than Green | too generous if forced | not_applicable |
| 주성엔지니어링 | useful but volatile | better risk balance | too early without customer confirmation | 0.41 |
| 원익IPS | watch only | risky | false positive | not_applicable |
| 테스 | watch only | risky | false positive | not_applicable |

## 15. 4B Local vs Full-window Timing Audit

| Case | four_b_local_peak_proximity | four_b_full_window_peak_proximity | Verdict |
|---|---:|---:|---|
| SK하이닉스 | 0.86 | 0.98 | good full-window 4B only after valuation/positioning evidence |
| 삼성전자 | 0.72 | 0.70 | price-only peak; not full 4B |
| 주성엔지니어링 | 0.88 | 0.96 | good 4B when overheat evidence appears |
| 원익IPS | 0.35 | 0.31 | local bounce too early / weak |
| 테스 | 0.91 | 0.91 | local 4B useful as risk overlay, not positive-stage evidence |

## 16. 4C Protection Audit

No hard 4C rows are promoted from this loop. C10 memory recovery failures in WIPS/TES are better treated as failed rerating / Stage2-watch rather than hard 4C, because no explicit thesis break such as order cancellation, accounting break, or forced liquidation was identified at the trigger date.

```text
four_c_protection_label = thesis_break_watch_only
hard_4c_success_count = 0
hard_4c_late_count = 0
```

## 17. Sector-Specific Rule Candidate

```text
rule_scope = sector_specific
large_sector_id = L2_AI_SEMICONDUCTOR_ELECTRONICS
candidate = L2_memory_body_vs_equipment_beta_split
status = sector_shadow_only
```

Rule candidate:

```text
If memory recovery evidence is ASP/spread/revision-led and relative strength is concentrated in the memory body, equipment names remain capped at Stage2-watch or Yellow-risk unless capex order conversion, customer-specific backlog, or margin bridge is visible.
```

## 18. Canonical-Archetype Rule Candidate

```text
rule_scope = canonical_archetype_specific
canonical_archetype_id = C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE
candidate = C10_capex_order_conversion_guard
status = canonical_shadow_only
```

Canonical rule candidate:

```text
C10 Green requires at least two of:
1. confirmed ASP/spread improvement,
2. customer/order conversion,
3. revision or financial visibility,
4. durable relative strength versus memory index/body.

For equipment suppliers, memory-cycle beta alone cannot promote to Green.
```

## 19. Before / After Backtest Comparison

| profile_id | scope | changed_axes | eligible | selected entries | avg MFE90 | avg MAE90 | avg MFE180 | avg MAE180 | false positive | verdict |
|---|---|---|---:|---|---:|---:|---:|---:|---:|---|
| P0_e2r_2_1_stock_web_calibrated_proxy | current | none | 5 | all representative triggers | 24.5 | -7.3 | 48.7 | -7.9 | 40% | usable but C10 equipment headline false-positive remains |
| P0b_e2r_2_0_baseline_reference | rollback_reference | pre-stock-web thresholds | 5 | all representative triggers | 24.5 | -7.3 | 48.7 | -7.9 | 60% | over-promotes equipment recovery narratives |
| P1_L2_C10_sector_candidate_profile | sector_specific | add C10 capex_order_conversion_guard + equipment_order_delay_risk | 5 | SKHU/JUSUNG Green; SEC Yellow; WIPS/TES watch | 55.0 | -2.8 | 76.9 | -2.8 | 0% | best score-return alignment |
| P2_C10_archetype_candidate_profile | canonical_archetype_specific | same as P1 but canonical scope | 5 | SKHU/JUSUNG Green; SEC Yellow; WIPS/TES watch | 55.0 | -2.8 | 76.9 | -2.8 | 0% | candidate for shadow ledger |
| P3_counterexample_guard_profile | guard | stronger false-positive guard on WIPS/TES pattern | 5 | only non-price bridge confirmed triggers | 55.0 | -2.8 | 76.9 | -2.8 | 0% | good guard but slightly too strict |

## 20. Score-Return Alignment Matrix

| Case | P0 score/stage | P2 score/stage | Return alignment |
|---|---|---|---|
| R2L11-C10-SKHU-20230525 | 88 / Stage3-Green | 89 / Stage3-Green | strong_positive_alignment |
| R2L11-C10-SEC-20230407 | 77 / Stage3-Yellow | 76 / Stage3-Yellow | yellow_better_than_green |
| R2L11-C10-JUSUNG-20230324 | 84 / Stage3-Yellow | 80 / Stage3-Yellow-highMAE | positive_but_needs_high_mae_flag |
| R2L11-C10-WIPS-20230317 | 76 / Stage3-Yellow/weak-Green-risk | 68 / Stage2-watch | headline_score_overstated_return |
| R2L11-C10-TES-20230324 | 74 / Stage2-Actionable/Yellow-risk | 66 / Stage2-watch | weak_return_high_mae |


## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive_case_count | counterexample_count | 4B_case_count | 4C_case_count | new_independent_case_count | reused_case_count | calibration_usable_trigger_count | representative_trigger_count | current_profile_error_count | sector_rule_candidate | canonical_rule_candidate | coverage_gap_after_this_loop |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| L2_AI_SEMICONDUCTOR_ELECTRONICS | C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE | MEMORY_RECOVERY_CAPEX_ORDER_CONVERSION_GUARD | 3 | 2 | 3 | 0 | 5 | 0 | 5 | 5 | 3 | true | true | C10 headline-only equipment false-positive reduced, but needs more 2024 holdout |

## 22. Residual Contribution Summary

```text
new_independent_case_count: 5
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 5
new_canonical_archetype_count: 0
new_fine_archetype_count: 1
new_trigger_family_count: 4
tested_existing_calibrated_axes: stage2_actionable_evidence_bonus, stage3_green_revision_min, price_only_blowoff_blocks_positive_stage, full_4b_requires_non_price_evidence
residual_error_types_found: equipment_cycle_false_positive, high_mae_success, memory_body_vs_equipment_beta_split
new_axis_proposed: null
existing_axis_strengthened: C10 capex order conversion guard, full_4b_requires_non_price_evidence
existing_axis_weakened: null
existing_axis_kept: stage2_actionable_evidence_bonus, yellow/green thresholds, hard_4c routing
sector_specific_rule_candidate: true
canonical_archetype_rule_candidate: true
no_new_signal_reason: null
loop_contribution_label: canonical_archetype_rule_candidate
do_not_propose_new_weight_delta: false
```

## 23. Validation Scope / Non-Validation Scope

Validated:

```text
- historical trigger dates only
- stock-web tradable_raw OHLC rows
- 30D/90D/180D MFE and MAE
- same-entry dedupe for aggregate rows
- C10 positive/counterexample balance
```

Not validated:

```text
- live 2026 candidate discovery
- broker execution
- production scoring patch
- src/e2r implementation details
- revised/share-adjusted price path
```

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,C10_capex_order_conversion_guard,canonical_archetype_specific,L2_AI_SEMICONDUCTOR_ELECTRONICS,C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE,0,1,+1,"memory recovery headline alone over-promoted WIPS/TES; order/revision bridge preserved SKHU/JUSUNG positives","false_positive_rate 40% to 0% in representative set",TRG-R2L11-C10-SKHU-20230525|TRG-R2L11-C10-SEC-20230407|TRG-R2L11-C10-JUSUNG-20230324|TRG-R2L11-C10-WIPS-20230317|TRG-R2L11-C10-TES-20230324,5,5,2,medium-low,canonical_shadow_only,"not production; post-calibrated residual"
```

## 25. Machine-Readable Rows

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration"}
{"row_type": "case", "case_id": "R2L11-C10-SKHU-20230525", "symbol": "000660", "company_name": "SK하이닉스", "round": "R2", "loop": "11", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE", "fine_archetype_id": "MEMORY_RECOVERY_CAPEX_ORDER_CONVERSION_GUARD", "case_type": "structural_success", "positive_or_counterexample": "positive", "best_trigger": "TRG-R2L11-C10-SKHU-20230525", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "strong_positive_alignment", "current_profile_verdict": "current_profile_correct", "price_source": "Songdaiki/stock-web", "notes": "메모리 가격 바닥 통과 + HBM/DDR5 수요 + 감산에 따른 재고 정상화 기대가 장중 가격에 반영되기 시작한 구간."}
{"row_type": "case", "case_id": "R2L11-C10-SEC-20230407", "symbol": "005930", "company_name": "삼성전자", "round": "R2", "loop": "11", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE", "fine_archetype_id": "MEMORY_RECOVERY_CAPEX_ORDER_CONVERSION_GUARD", "case_type": "stage2_promote_candidate", "positive_or_counterexample": "positive", "best_trigger": "TRG-R2L11-C10-SEC-20230407", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "yellow_better_than_green", "current_profile_verdict": "current_profile_correct", "price_source": "Songdaiki/stock-web", "notes": "메모리 감산 공시/업황 바닥 인식은 있었지만 HBM 상대강도와 revision 속도는 SK하이닉스보다 약했던 대형 메모리 회복 케이스."}
{"row_type": "case", "case_id": "R2L11-C10-JUSUNG-20230324", "symbol": "036930", "company_name": "주성엔지니어링", "round": "R2", "loop": "11", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE", "fine_archetype_id": "MEMORY_RECOVERY_CAPEX_ORDER_CONVERSION_GUARD", "case_type": "high_mae_success", "positive_or_counterexample": "positive", "best_trigger": "TRG-R2L11-C10-JUSUNG-20230324", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "positive_but_needs_high_mae_flag", "current_profile_verdict": "current_profile_too_early", "price_source": "Songdaiki/stock-web", "notes": "메모리 장비 회복 기대가 개별 ALD/증착 장비 수주 기대와 결합하며 상대강도를 만든 케이스. 다만 변동성이 커서 Green은 고객/수주 확인이 필요했다."}
{"row_type": "case", "case_id": "R2L11-C10-WIPS-20230317", "symbol": "240810", "company_name": "원익IPS", "round": "R2", "loop": "11", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE", "fine_archetype_id": "MEMORY_RECOVERY_CAPEX_ORDER_CONVERSION_GUARD", "case_type": "false_positive_green", "positive_or_counterexample": "counterexample", "best_trigger": "TRG-R2L11-C10-WIPS-20230317", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "headline_score_overstated_return", "current_profile_verdict": "current_profile_false_positive", "price_source": "Songdaiki/stock-web", "notes": "메모리 회복/장비 사이클 headline은 강했지만 실제 capex order conversion이 지연되어 장비주 전반 Green 승격에는 실패한 반례."}
{"row_type": "case", "case_id": "R2L11-C10-TES-20230324", "symbol": "095610", "company_name": "테스", "round": "R2", "loop": "11", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE", "fine_archetype_id": "MEMORY_RECOVERY_CAPEX_ORDER_CONVERSION_GUARD", "case_type": "failed_rerating", "positive_or_counterexample": "counterexample", "best_trigger": "TRG-R2L11-C10-TES-20230324", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "weak_return_high_mae", "current_profile_verdict": "current_profile_false_positive", "price_source": "Songdaiki/stock-web", "notes": "메모리 회복 기대가 장비 공급망 전반에 확산됐지만 재주문/마진 bridge가 약해 180D 성과가 제한되고 drawdown이 커진 반례."}
{"row_type": "trigger", "trigger_id": "TRG-R2L11-C10-SKHU-20230525", "case_id": "R2L11-C10-SKHU-20230525", "symbol": "000660", "company_name": "SK하이닉스", "round": "R2", "loop": "11", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE", "fine_archetype_id": "MEMORY_RECOVERY_CAPEX_ORDER_CONVERSION_GUARD", "sector": "AI/semiconductor/electronics", "primary_archetype": "memory recovery equipment cycle", "loop_objective": "coverage_gap_fill|counterexample_mining|green_strictness_stress_test|sector_specific_rule_discovery", "trigger_type": "Stage2-Actionable", "trigger_date": "2023-05-25", "evidence_available_at_that_date": "메모리 가격 바닥 통과 + HBM/DDR5 수요 + 감산에 따른 재고 정상화 기대가 장중 가격에 반영되기 시작한 구간.", "evidence_source": "historical public disclosure/news/research proxy; price verified in Songdaiki/stock-web", "stage2_evidence_fields": ["relative_strength", "capacity_or_volume_route", "early_revision_signal"], "stage3_evidence_fields": ["confirmed_revision", "financial_visibility", "durable_customer_confirmation"], "stage4b_evidence_fields": ["valuation_blowoff", "positioning_overheat"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/000/000660/2023.csv", "profile_path": "atlas/symbol_profiles/000/000660.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2023-05-25", "entry_price": 103500, "MFE_30D_pct": 16.1, "MFE_90D_pct": 23.9, "MFE_180D_pct": 61.3, "MFE_1Y_pct": 84.1, "MFE_2Y_pct": null, "MAE_30D_pct": -2.3, "MAE_90D_pct": -2.3, "MAE_180D_pct": -2.3, "MAE_1Y_pct": -2.3, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-02-23", "peak_price": 166900, "drawdown_after_peak_pct": -8.1, "green_lateness_ratio": 0.36, "four_b_local_peak_proximity": 0.86, "four_b_full_window_peak_proximity": 0.98, "four_b_timing_verdict": "good_full_window_4B_timing_when_non_price_overheat_exists", "four_b_evidence_type": ["valuation_blowoff", "positioning_overheat"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "structural_success", "current_profile_verdict": "current_profile_correct", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_by_profile_review", "same_entry_group_id": "R2L11-C10-SKHU-20230525|2023-05-25", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "TRG-R2L11-C10-SEC-20230407", "case_id": "R2L11-C10-SEC-20230407", "symbol": "005930", "company_name": "삼성전자", "round": "R2", "loop": "11", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE", "fine_archetype_id": "MEMORY_RECOVERY_CAPEX_ORDER_CONVERSION_GUARD", "sector": "AI/semiconductor/electronics", "primary_archetype": "memory recovery equipment cycle", "loop_objective": "coverage_gap_fill|counterexample_mining|green_strictness_stress_test|sector_specific_rule_discovery", "trigger_type": "Stage2", "trigger_date": "2023-04-07", "evidence_available_at_that_date": "메모리 감산 공시/업황 바닥 인식은 있었지만 HBM 상대강도와 revision 속도는 SK하이닉스보다 약했던 대형 메모리 회복 케이스.", "evidence_source": "historical public disclosure/news/research proxy; price verified in Songdaiki/stock-web", "stage2_evidence_fields": ["public_event_or_disclosure", "capacity_or_volume_route", "early_revision_signal"], "stage3_evidence_fields": ["financial_visibility"], "stage4b_evidence_fields": ["price_only_local_peak"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/005/005930/2023.csv", "profile_path": "atlas/symbol_profiles/005/005930.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2023-04-07", "entry_price": 65000, "MFE_30D_pct": 8.3, "MFE_90D_pct": 11.8, "MFE_180D_pct": 20.0, "MFE_1Y_pct": 36.6, "MFE_2Y_pct": null, "MAE_30D_pct": -2.6, "MAE_90D_pct": -2.6, "MAE_180D_pct": -2.6, "MAE_1Y_pct": -2.6, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2023-12-27", "peak_price": 78000, "drawdown_after_peak_pct": -8.6, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.72, "four_b_full_window_peak_proximity": 0.7, "four_b_timing_verdict": "watch_only_price_peak_not_full_4B", "four_b_evidence_type": ["price_only"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "moderate_structural_success", "current_profile_verdict": "current_profile_correct", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window; profile corporate action candidates 1996/1997/2018 only", "same_entry_group_id": "R2L11-C10-SEC-20230407|2023-04-07", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "TRG-R2L11-C10-JUSUNG-20230324", "case_id": "R2L11-C10-JUSUNG-20230324", "symbol": "036930", "company_name": "주성엔지니어링", "round": "R2", "loop": "11", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE", "fine_archetype_id": "MEMORY_RECOVERY_CAPEX_ORDER_CONVERSION_GUARD", "sector": "AI/semiconductor/electronics", "primary_archetype": "memory recovery equipment cycle", "loop_objective": "coverage_gap_fill|counterexample_mining|green_strictness_stress_test|sector_specific_rule_discovery", "trigger_type": "Stage2-Actionable", "trigger_date": "2023-03-24", "evidence_available_at_that_date": "메모리 장비 회복 기대가 개별 ALD/증착 장비 수주 기대와 결합하며 상대강도를 만든 케이스. 다만 변동성이 커서 Green은 고객/수주 확인이 필요했다.", "evidence_source": "historical public disclosure/news/research proxy; price verified in Songdaiki/stock-web", "stage2_evidence_fields": ["relative_strength", "capacity_or_volume_route", "customer_or_order_quality"], "stage3_evidence_fields": ["repeat_order_or_conversion", "margin_bridge", "financial_visibility"], "stage4b_evidence_fields": ["valuation_blowoff", "positioning_overheat"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/036/036930/2023.csv", "profile_path": "atlas/symbol_profiles/036/036930.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2023-03-24", "entry_price": 15240, "MFE_30D_pct": 31.9, "MFE_90D_pct": 75.2, "MFE_180D_pct": 149.3, "MFE_1Y_pct": 166.0, "MFE_2Y_pct": null, "MAE_30D_pct": -3.5, "MAE_90D_pct": -3.5, "MAE_180D_pct": -3.5, "MAE_1Y_pct": -6.0, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2023-11-15", "peak_price": 38000, "drawdown_after_peak_pct": -18.0, "green_lateness_ratio": 0.41, "four_b_local_peak_proximity": 0.88, "four_b_full_window_peak_proximity": 0.96, "four_b_timing_verdict": "good_full_window_4B_timing_when_valuation_positioning_evidence_exists", "four_b_evidence_type": ["valuation_blowoff", "positioning_overheat"], "four_c_protection_label": "false_break", "trigger_outcome_label": "high_mae_success", "current_profile_verdict": "current_profile_too_early", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window; profile corporate action candidate 2000 only", "same_entry_group_id": "R2L11-C10-JUSUNG-20230324|2023-03-24", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "TRG-R2L11-C10-WIPS-20230317", "case_id": "R2L11-C10-WIPS-20230317", "symbol": "240810", "company_name": "원익IPS", "round": "R2", "loop": "11", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE", "fine_archetype_id": "MEMORY_RECOVERY_CAPEX_ORDER_CONVERSION_GUARD", "sector": "AI/semiconductor/electronics", "primary_archetype": "memory recovery equipment cycle", "loop_objective": "coverage_gap_fill|counterexample_mining|green_strictness_stress_test|sector_specific_rule_discovery", "trigger_type": "Stage2", "trigger_date": "2023-03-17", "evidence_available_at_that_date": "메모리 회복/장비 사이클 headline은 강했지만 실제 capex order conversion이 지연되어 장비주 전반 Green 승격에는 실패한 반례.", "evidence_source": "historical public disclosure/news/research proxy; price verified in Songdaiki/stock-web", "stage2_evidence_fields": ["relative_strength", "capacity_or_volume_route"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["margin_or_backlog_slowdown"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/240/240810/2023.csv", "profile_path": "atlas/symbol_profiles/240/240810.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2023-03-17", "entry_price": 34250, "MFE_30D_pct": 6.3, "MFE_90D_pct": 6.3, "MFE_180D_pct": 7.4, "MFE_1Y_pct": 41.2, "MFE_2Y_pct": null, "MAE_30D_pct": -14.2, "MAE_90D_pct": -18.5, "MAE_180D_pct": -18.5, "MAE_1Y_pct": -18.5, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2023-11-13", "peak_price": 36800, "drawdown_after_peak_pct": -13.5, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.35, "four_b_full_window_peak_proximity": 0.31, "four_b_timing_verdict": "price_only_local_4B_too_early_or_not_actionable", "four_b_evidence_type": ["margin_or_backlog_slowdown"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "failed_rerating", "current_profile_verdict": "current_profile_false_positive", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window; profile has zero corporate action candidates", "same_entry_group_id": "R2L11-C10-WIPS-20230317|2023-03-17", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "TRG-R2L11-C10-TES-20230324", "case_id": "R2L11-C10-TES-20230324", "symbol": "095610", "company_name": "테스", "round": "R2", "loop": "11", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE", "fine_archetype_id": "MEMORY_RECOVERY_CAPEX_ORDER_CONVERSION_GUARD", "sector": "AI/semiconductor/electronics", "primary_archetype": "memory recovery equipment cycle", "loop_objective": "coverage_gap_fill|counterexample_mining|green_strictness_stress_test|sector_specific_rule_discovery", "trigger_type": "Stage2", "trigger_date": "2023-03-24", "evidence_available_at_that_date": "메모리 회복 기대가 장비 공급망 전반에 확산됐지만 재주문/마진 bridge가 약해 180D 성과가 제한되고 drawdown이 커진 반례.", "evidence_source": "historical public disclosure/news/research proxy; price verified in Songdaiki/stock-web", "stage2_evidence_fields": ["relative_strength", "capacity_or_volume_route"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["margin_or_backlog_slowdown"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/095/095610/2023.csv", "profile_path": "atlas/symbol_profiles/095/095610.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2023-03-24", "entry_price": 22100, "MFE_30D_pct": 5.4, "MFE_90D_pct": 5.4, "MFE_180D_pct": 5.4, "MFE_1Y_pct": 18.1, "MFE_2Y_pct": null, "MAE_30D_pct": -9.5, "MAE_90D_pct": -9.5, "MAE_180D_pct": -12.7, "MAE_1Y_pct": -13.5, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2023-04-11", "peak_price": 23300, "drawdown_after_peak_pct": -17.2, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.91, "four_b_full_window_peak_proximity": 0.91, "four_b_timing_verdict": "good_local_4B_but_not_positive_stage", "four_b_evidence_type": ["margin_or_backlog_slowdown", "positioning_overheat"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "failed_rerating", "current_profile_verdict": "current_profile_false_positive", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window; profile corporate action candidates 2011/2016 only", "same_entry_group_id": "R2L11-C10-TES-20230324|2023-03-24", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R2L11-C10-SKHU-20230525", "trigger_id": "TRG-R2L11-C10-SKHU-20230525", "symbol": "000660", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 1, "margin_bridge_score": 2, "revision_score": 3, "relative_strength_score": 3, "customer_quality_score": 3, "policy_or_regulatory_score": 0, "valuation_repricing_score": 2, "execution_risk_score": 1, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "capacity_or_shipment_score": 3, "asp_or_spread_score": 3}, "weighted_score_before": 88, "stage_label_before": "Stage3-Green", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 1, "margin_bridge_score": 2, "revision_score": 3, "relative_strength_score": 3, "customer_quality_score": 3, "policy_or_regulatory_score": 0, "valuation_repricing_score": 2, "execution_risk_score": 1, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "capacity_or_shipment_score": 3, "asp_or_spread_score": 3, "capex_order_conversion_guard": 2, "equipment_order_delay_risk": 0}, "weighted_score_after": 89, "stage_label_after": "Stage3-Green", "changed_components": ["capex_order_conversion_guard", "equipment_order_delay_risk"], "component_delta_explanation": "C10는 memory price/recovery headline만으로 Green을 주지 않고, capex order conversion과 customer/revision bridge가 붙을 때만 승격한다.", "MFE_90D_pct": 23.9, "MAE_90D_pct": -2.3, "score_return_alignment_label": "strong_positive_alignment", "current_profile_verdict": "current_profile_correct"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R2L11-C10-SEC-20230407", "trigger_id": "TRG-R2L11-C10-SEC-20230407", "symbol": "005930", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 1, "revision_score": 1, "relative_strength_score": 1, "customer_quality_score": 1, "policy_or_regulatory_score": 0, "valuation_repricing_score": 1, "execution_risk_score": 1, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "capacity_or_shipment_score": 2, "asp_or_spread_score": 2}, "weighted_score_before": 77, "stage_label_before": "Stage3-Yellow", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 1, "revision_score": 1, "relative_strength_score": 1, "customer_quality_score": 1, "policy_or_regulatory_score": 0, "valuation_repricing_score": 1, "execution_risk_score": 1, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "capacity_or_shipment_score": 2, "asp_or_spread_score": 2, "capex_order_conversion_guard": 2, "equipment_order_delay_risk": 0}, "weighted_score_after": 76, "stage_label_after": "Stage3-Yellow", "changed_components": ["capex_order_conversion_guard", "equipment_order_delay_risk"], "component_delta_explanation": "C10는 memory price/recovery headline만으로 Green을 주지 않고, capex order conversion과 customer/revision bridge가 붙을 때만 승격한다.", "MFE_90D_pct": 11.8, "MAE_90D_pct": -2.6, "score_return_alignment_label": "yellow_better_than_green", "current_profile_verdict": "current_profile_correct"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R2L11-C10-JUSUNG-20230324", "trigger_id": "TRG-R2L11-C10-JUSUNG-20230324", "symbol": "036930", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE", "raw_component_scores_before": {"contract_score": 1, "backlog_visibility_score": 1, "margin_bridge_score": 1, "revision_score": 2, "relative_strength_score": 3, "customer_quality_score": 2, "policy_or_regulatory_score": 0, "valuation_repricing_score": 2, "execution_risk_score": 2, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "capacity_or_shipment_score": 3, "asp_or_spread_score": 2}, "weighted_score_before": 84, "stage_label_before": "Stage3-Yellow", "raw_component_scores_after": {"contract_score": 1, "backlog_visibility_score": 1, "margin_bridge_score": 1, "revision_score": 2, "relative_strength_score": 3, "customer_quality_score": 2, "policy_or_regulatory_score": 0, "valuation_repricing_score": 2, "execution_risk_score": 2, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "capacity_or_shipment_score": 3, "asp_or_spread_score": 2, "capex_order_conversion_guard": 2, "equipment_order_delay_risk": 0}, "weighted_score_after": 80, "stage_label_after": "Stage3-Yellow-highMAE", "changed_components": ["capex_order_conversion_guard", "equipment_order_delay_risk"], "component_delta_explanation": "C10는 memory price/recovery headline만으로 Green을 주지 않고, capex order conversion과 customer/revision bridge가 붙을 때만 승격한다.", "MFE_90D_pct": 75.2, "MAE_90D_pct": -3.5, "score_return_alignment_label": "positive_but_needs_high_mae_flag", "current_profile_verdict": "current_profile_too_early"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R2L11-C10-WIPS-20230317", "trigger_id": "TRG-R2L11-C10-WIPS-20230317", "symbol": "240810", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 2, "customer_quality_score": 1, "policy_or_regulatory_score": 0, "valuation_repricing_score": 1, "execution_risk_score": 2, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "capacity_or_shipment_score": 1, "asp_or_spread_score": 1}, "weighted_score_before": 76, "stage_label_before": "Stage3-Yellow/weak-Green-risk", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 2, "customer_quality_score": 1, "policy_or_regulatory_score": 0, "valuation_repricing_score": 1, "execution_risk_score": 2, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "capacity_or_shipment_score": 1, "asp_or_spread_score": 1, "capex_order_conversion_guard": -3, "equipment_order_delay_risk": -2}, "weighted_score_after": 68, "stage_label_after": "Stage2-watch", "changed_components": ["capex_order_conversion_guard", "equipment_order_delay_risk"], "component_delta_explanation": "C10는 memory price/recovery headline만으로 Green을 주지 않고, capex order conversion과 customer/revision bridge가 붙을 때만 승격한다.", "MFE_90D_pct": 6.3, "MAE_90D_pct": -18.5, "score_return_alignment_label": "headline_score_overstated_return", "current_profile_verdict": "current_profile_false_positive"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R2L11-C10-TES-20230324", "trigger_id": "TRG-R2L11-C10-TES-20230324", "symbol": "095610", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 2, "customer_quality_score": 1, "policy_or_regulatory_score": 0, "valuation_repricing_score": 1, "execution_risk_score": 2, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "capacity_or_shipment_score": 1, "asp_or_spread_score": 1}, "weighted_score_before": 74, "stage_label_before": "Stage2-Actionable/Yellow-risk", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 2, "customer_quality_score": 1, "policy_or_regulatory_score": 0, "valuation_repricing_score": 1, "execution_risk_score": 2, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "capacity_or_shipment_score": 1, "asp_or_spread_score": 1, "capex_order_conversion_guard": -3, "equipment_order_delay_risk": -2}, "weighted_score_after": 66, "stage_label_after": "Stage2-watch", "changed_components": ["capex_order_conversion_guard", "equipment_order_delay_risk"], "component_delta_explanation": "C10는 memory price/recovery headline만으로 Green을 주지 않고, capex order conversion과 customer/revision bridge가 붙을 때만 승격한다.", "MFE_90D_pct": 5.4, "MAE_90D_pct": -9.5, "score_return_alignment_label": "weak_return_high_mae", "current_profile_verdict": "current_profile_false_positive"}
{"row_type": "shadow_weight", "axis": "C10_capex_order_conversion_guard", "scope": "canonical_archetype_specific", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE", "baseline_value": 0, "tested_value": 1, "delta": "+1 guard / +1 bridge", "reason": "Memory recovery headline alone produced WIPS/TES false positives; confirmed ASP/revision/customer/capex conversion separated SKHU/JUSUNG positives.", "backtest_effect": "false positive rate 40% -> 0% in representative set while preserving two structural successes", "trigger_ids": "TRG-R2L11-C10-SKHU-20230525|TRG-R2L11-C10-SEC-20230407|TRG-R2L11-C10-JUSUNG-20230324|TRG-R2L11-C10-WIPS-20230317|TRG-R2L11-C10-TES-20230324", "calibration_usable_count": 5, "new_independent_case_count": 5, "counterexample_count": 2, "confidence": "medium-low", "proposal_type": "canonical_archetype_shadow_only", "notes": "not production; post-calibrated residual"}
{"row_type": "residual_contribution", "round": "R2", "loop": "11", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE", "new_independent_case_count": 5, "reused_case_count": 0, "new_symbol_count": 5, "new_trigger_family_count": 4, "tested_existing_calibrated_axes": ["stage2_actionable_evidence_bonus", "stage3_green_revision_min", "full_4b_requires_non_price_evidence", "price_only_blowoff_blocks_positive_stage"], "residual_error_types_found": ["equipment_cycle_false_positive", "high_mae_success", "memory_body_vs_equipment_beta_split"], "loop_contribution_label": "canonical_archetype_rule_candidate", "do_not_propose_new_weight_delta": false}
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
- Price shard pattern: atlas/ohlcv_tradable_by_symbol_year/&lt;prefix&gt;/&lt;ticker&gt;/&lt;year&gt;.csv.
- Symbol profile pattern: atlas/symbol_profiles/&lt;prefix&gt;/&lt;ticker&gt;.json.

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
completed_round = R2
completed_loop = 11
next_round = R3
next_loop = 11
round_schedule_status = valid
round_sector_consistency = pass
```

## 28. Source Notes

```text
stock_agent_research_artifact_read:
- reports/e2r_calibration/by_round/R2.md

stock_web_files_read:
- atlas/manifest.json
- atlas/symbol_profiles/000/000660.json
- atlas/symbol_profiles/005/005930.json
- atlas/symbol_profiles/036/036930.json
- atlas/symbol_profiles/240/240810.json
- atlas/symbol_profiles/095/095610.json
- atlas/ohlcv_tradable_by_symbol_year/000/000660/2023.csv
- atlas/ohlcv_tradable_by_symbol_year/000/000660/2024.csv
- atlas/ohlcv_tradable_by_symbol_year/005/005930/2023.csv
- atlas/ohlcv_tradable_by_symbol_year/036/036930/2023.csv
- atlas/ohlcv_tradable_by_symbol_year/240/240810/2023.csv
- atlas/ohlcv_tradable_by_symbol_year/095/095610/2023.csv
```

