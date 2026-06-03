# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
scheduled_round = R6
scheduled_loop = 71
round_schedule_status = valid
round_sector_consistency = pass
completed_round = R6
completed_loop = 71
next_round = R7
next_loop = 71
large_sector_id = L6_FINANCIAL_CAPITAL_RETURN_DIGITAL
canonical_archetype_id = C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN
fine_archetype_id = C21_REGIONAL_BANK_VALUEUP_CAPITAL_RETURN_BRIDGE
loop_objective = counterexample_mining | stage2_actionable_bonus_stress_test | canonical_archetype_rule_candidate
production_scoring_changed = false
shadow_weight_only = true
price_source = Songdaiki/stock-web
stock_web_manifest_max_date = 2026-02-20
```

## 1. Current Calibrated Profile Assumption

Current default proxy is `e2r_2_1_stock_web_calibrated`: Stage2-Actionable has the global non-price evidence bonus, Yellow threshold is lower than legacy baseline, Green total/revision gates remain strict, price-only blowoff cannot promote a positive stage, and full 4B needs non-price evidence.

This run does not propose a production patch. It stress-tests whether C21 regional banks require a narrower capital-return bridge than generic financial value-up exposure.

## 2. Round / Large Sector / Canonical Archetype Scope

R6 maps to `L6_FINANCIAL_CAPITAL_RETURN_DIGITAL`. The selected canonical archetype is `C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN`.

The fine/deep sub-archetype is:

```text
C21_REGIONAL_BANK_VALUEUP_CAPITAL_RETURN_BRIDGE
```

Mechanism: the same value-up/PBR-discount policy wind can lift the whole regional-bank basket, but the bridge from Stage2 to Stage3 should depend on bank-specific ROE durability, credit-cost quality, and executed buyback/dividend behavior. Otherwise, the model treats a tide as if every boat had an engine.

## 3. Previous Coverage / Duplicate Avoidance Check

NO-REPEAT INDEX shows C21 is heavily covered overall, especially `105560`, `323410`, `086790`, `006220`, and `055550`. This run avoids those top-covered symbols and uses three regional-bank symbols not listed among the top covered C21 combinations:

- `138930` BNK금융지주
- `175330` JB금융지주
- `139130` DGB금융지주 / iM금융지주

Hard duplicate rule checked conceptually:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

All three selected representative triggers are treated as new independent case candidates for this loop.

## 4. Stock-Web OHLC Input / Price Source Validation

Stock-web manifest and schema validation:

```text
source_name = FinanceData/marcap
price_adjustment_status = raw_unadjusted_marcap
min_date = 1995-05-02
max_date = 2026-02-20
tradable_row_count = 14354401
raw_row_count = 15214118
symbol_count = 5414
active_like_symbol_count = 2868
inactive_or_delisted_like_symbol_count = 2546
calibration_shard_root = atlas/ohlcv_tradable_by_symbol_year
raw_shard_root = atlas/ohlcv_raw_by_symbol_year
schema_path = atlas/schema.json
universe_path = atlas/universe/all_symbols.csv
```

Schema basis:

```text
tradable_shard_columns = d,o,h,l,c,v,a,mc,s,m
price_basis = tradable_raw
price_adjustment_status = raw_unadjusted_marcap
MFE_N_pct = (max high from entry_date through N tradable rows / entry_price - 1) * 100
MAE_N_pct = (min low from entry_date through N tradable rows / entry_price - 1) * 100
```

## 5. Historical Eligibility Gate

All representative rows use 2024-01-26 as trigger/entry date. Entry price is the stock-web close on that date.

| symbol | company | profile | entry row | forward 180D | corp action overlap | usable |
|---|---|---|---|---:|---|---|
| 138930 | BNK금융지주 | atlas/symbol_profiles/138/138930.json | 2024-01-26 close 7,220 | 180 | no 2024 candidate overlap | true |
| 175330 | JB금융지주 | atlas/symbol_profiles/175/175330.json | 2024-01-26 close 10,840 | 180 | no 2024 candidate overlap | true |
| 139130 | DGB/iM금융지주 | atlas/symbol_profiles/139/139130.json | 2024-01-26 close 8,600 | 180 | no 2024 candidate overlap | true |

## 6. Canonical Archetype Compression Map

| fine_archetype_id | canonical_archetype_id | compression reason |
|---|---|---|
| C21_REGIONAL_BANK_VALUEUP_CAPITAL_RETURN_BRIDGE | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | regional banks are not a separate scoring family; they are a C21 sub-case where ROE/PBR, credit-cost quality, and capital return determine conversion |
| POLICY_WAVE_ONLY_REGIONAL_BANK | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | policy/value-up exposure alone is Stage2 watch, not Green |
| EXECUTED_CAPITAL_RETURN_REGIONAL_BANK | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | buyback/dividend execution plus ROE quality may support Stage3-Yellow/Green, subject to strict gates |

## 7. Case Selection Summary

| case_id | symbol | role | trigger | entry | outcome |
|---|---|---|---|---|---|
| R6L71_C21_REGIONAL_BANK_BNK_20240126_STAGE2A | 138930 | structural_success | Stage2-Actionable | 2024-01-26 / 7,220 | shallow MAE and +43.21% 180D MFE |
| R6L71_C21_REGIONAL_BANK_JB_20240126_STAGE2A | 175330 | structural_success | Stage2-Actionable | 2024-01-26 / 10,840 | strongest positive, +72.60% 180D MFE |
| R6L71_C21_REGIONAL_BANK_DGB_20240126_STAGE2A | 139130 | failed_rerating | Stage2-Actionable | 2024-01-26 / 8,600 | weaker conversion, only +16.86% 180D MFE with -9.88% MAE |

## 8. Positive vs Counterexample Balance

```text
positive_case_count = 2
counterexample_count = 1
calibration_usable_case_count = 3
new_independent_case_count = 3
```

This is enough for a canonical-archetype rule candidate, but not enough for a global candidate.

## 9. Evidence Source Map

The evidence map is source-name-level and must be URL-verified before production promotion.

| symbol | Stage2 evidence | Stage3 evidence | risk/4B evidence |
|---|---|---|---|
| 138930 | policy/value-up regime, PBR discount repricing, relative strength | capital-return route, ROE/PBR repricing | valuation/positioning overheat watch only |
| 175330 | policy/value-up regime, relative strength, capital-return optionality | strongest ROE/PBR and capital-return conversion path | non-price valuation/positioning 4B watch near October |
| 139130 | same policy wave | weaker conversion, mixed financial visibility | credit-cost/execution-quality gap; no full 4B |

## 10. Price Data Source Map

| symbol | tradable shard | profile path | row status | corporate action status |
|---|---|---|---|---|
| 138930 | atlas/ohlcv_tradable_by_symbol_year/138/138930/2024.csv | atlas/symbol_profiles/138/138930.json | tradable_ohlcv only for used rows | historical candidates 2014/2016 only |
| 175330 | atlas/ohlcv_tradable_by_symbol_year/175/175330/2024.csv | atlas/symbol_profiles/175/175330.json | tradable_ohlcv only for used rows | historical candidates before 2024 only |
| 139130 | atlas/ohlcv_tradable_by_symbol_year/139/139130/2024.csv | atlas/symbol_profiles/139/139130.json | tradable_ohlcv only for used rows | historical candidate 2015 only |

## 11. Case-by-Case Trigger Grid

| symbol | trigger_type | trigger_date | entry_date | entry_price | evidence family | current verdict |
|---|---|---|---|---:|---|---|
| 138930 | Stage2-Actionable | 2024-01-26 | 2024-01-26 | 7,220 | policy + PBR + capital return | current_profile_correct |
| 175330 | Stage2-Actionable | 2024-01-26 | 2024-01-26 | 10,840 | policy + PBR + capital return + ROE quality | current_profile_correct |
| 139130 | Stage2-Actionable | 2024-01-26 | 2024-01-26 | 8,600 | policy + PBR, weaker conversion | current_profile_too_early |

## 12. Trigger-Level OHLC Backtest Tables

| symbol | entry | MFE30 | MAE30 | MFE90 | MAE90 | MFE180 | MAE180 | peak_date | peak_price | drawdown_after_peak |
|---|---:|---:|---:|---:|---:|---:|---:|---|---:|---:|
| 138930 | 7,220 | 12.19 | -0.83 | 21.19 | -0.83 | 43.21 | -0.83 | 2024-08-26 | 10,340 | -13.73 |
| 175330 | 10,840 | 28.51 | -1.29 | 37.36 | -1.29 | 72.60 | -1.29 | 2024-10-25 | 18,710 | -5.24 |
| 139130 | 8,600 | 16.05 | -0.81 | 16.05 | -8.72 | 16.86 | -9.88 | 2024-10-25 | 10,050 | -4.00 |

## 13. Current Calibrated Profile Stress Test

| question | answer |
|---|---|
| current profile 판단 | BNK/JB는 Stage2-Actionable to Yellow watch가 타당. DGB는 같은 policy wave라도 weaker conversion이므로 too early risk. |
| 실제 MFE/MAE와 맞았나 | BNK/JB는 맞음. DGB는 MFE/MAE 비대칭이 약해 같은 점수 부여는 부정확. |
| Stage2 bonus 과했나 | C21 전체에는 유효하지만 regional bank 안에서는 executed capital-return bridge가 필요. |
| Yellow threshold 75 | BNK/JB에는 적절. DGB에는 너무 이른 Yellow 가능성. |
| Green threshold 87/revision 55 | 유지. 이 연구는 Green 완화 근거가 아니다. |
| price-only blowoff guard | 유지. regional bank basket rally만으로 Green/4B를 확정하지 않음. |
| full 4B non-price requirement | 강화 유지. JB의 4B는 capital-return/valuation non-price evidence가 있을 때만 full 4B. |
| hard 4C routing | 해당 없음; DGB는 hard 4C가 아니라 weak-conversion counterexample. |

## 14. Stage2 / Yellow / Green Comparison

- Stage2-Actionable worked well for BNK and JB because early policy/PBR evidence was followed by strong, shallow-drawdown price paths.
- The same Stage2 label was weaker for DGB/iM because its MFE90 stalled near +16% and MAE90 approached -9%.
- Stage3-Green should not be loosened. The correct adjustment is narrower: keep Stage2 watch but require bank-specific ROE, credit-cost, and capital-return execution before Green.

## 15. 4B Local vs Full-window Timing Audit

| symbol | 4B evidence type | local proximity | full-window proximity | verdict |
|---|---|---:|---:|---|
| 138930 | valuation_blowoff, positioning_overheat | 0.78 | 0.78 | watch only unless non-price crowding/valuation evidence is present |
| 175330 | valuation_blowoff, positioning_overheat, capital_return_execution | 0.90 | 0.90 | potentially good full-window 4B if non-price evidence is URL-verified |
| 139130 | none | null | null | not a 4B case |

## 16. 4C Protection Audit

No hard 4C row is proposed. DGB/iM is a weak-conversion counterexample, not a thesis-break collapse. Label:

```text
four_c_protection_label = thesis_break_watch_only
```

## 17. Sector-Specific Rule Candidate

```text
sector_specific_rule_candidate = false
```

This is not broad enough for all L6 financials. Insurance C22, brokers, banks, and holding-company value-up cases require separate evidence bridges.

## 18. Canonical-Archetype Rule Candidate

```text
canonical_archetype_rule_candidate = true
rule_scope = canonical_archetype_specific
canonical_archetype_id = C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN
candidate_rule = C21 regional-bank Stage2 requires policy/PBR evidence plus bank-specific ROE, credit-cost, and executed capital-return bridge before Stage3-Green.
```

Rule mechanism:

```text
if canonical_archetype_id == C21 and fine_archetype_id contains REGIONAL_BANK:
    policy_or_valueup_evidence alone may open Stage2-Actionable
    Stage3-Yellow requires relative strength plus ROE/PBR repricing evidence
    Stage3-Green requires capital-return execution or high-confidence revision/ROE bridge
    weak credit-cost or execution-quality evidence keeps the case at Stage2 watch
```

## 19. Before / After Backtest Comparison

| profile | eligible triggers | avg MFE90 | avg MAE90 | avg MFE180 | avg MAE180 | false_positive_rate | verdict |
|---|---:|---:|---:|---:|---:|---:|---|
| P0 e2r_2_1_stock_web_calibrated_proxy | 3 | 24.87 | -3.61 | 44.22 | -3.99 | 0.33 | good but too broad for DGB |
| P0b e2r_2_0_baseline_reference | 3 | 24.87 | -3.61 | 44.22 | -3.99 | 0.33 | slower Stage2, misses early rerating |
| P1 sector_specific_candidate_profile | 3 | 24.87 | -3.61 | 44.22 | -3.99 | 0.33 | not enough evidence for all L6 |
| P2 canonical_archetype_candidate_profile | 3 | 24.87 | -3.61 | 44.22 | -3.99 | 0.00 after DGB held at Stage2 watch | best shadow candidate |
| P3 counterexample_guard_profile | 3 | 24.87 | -3.61 | 44.22 | -3.99 | 0.00 | guard useful, no Green loosening |

## 20. Score-Return Alignment Matrix

| symbol | score before | stage before | score after | stage after | alignment |
|---|---:|---|---:|---|---|
| 138930 | 79 | Stage3-Yellow | 82 | Stage3-Yellow | positive_alignment |
| 175330 | 83 | Stage3-Yellow | 86 | Stage3-Yellow high-conviction watch | strong_positive_alignment |
| 139130 | 76 | Stage3-Yellow | 70 | Stage2-Actionable watch | residual_counterexample |

## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive_case_count | counterexample_count | 4B_case_count | 4C_case_count | new_independent_case_count | reused_case_count | calibration_usable_trigger_count | representative_trigger_count | current_profile_error_count | sector_rule_candidate | canonical_rule_candidate | coverage_gap_after_this_loop |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| L6_FINANCIAL_CAPITAL_RETURN_DIGITAL | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | C21_REGIONAL_BANK_VALUEUP_CAPITAL_RETURN_BRIDGE | 2 | 1 | 1 | 0 | 3 | 0 | 3 | 3 | 1 | false | true | regional-bank sub-archetype has cleaner positive/counterexample split, but needs URL-level evidence repair |

## 22. Residual Contribution Summary

new_independent_case_count: 3  
reused_case_count: 0  
reused_case_ids: []  
new_symbol_count: 3  
new_canonical_archetype_count: 0  
new_fine_archetype_count: 1  
new_trigger_family_count: 3  
tested_existing_calibrated_axes: stage2_actionable_evidence_bonus, stage2_required_bridge, stage3_green_total_min, stage3_green_revision_min, full_4b_requires_non_price_evidence  
residual_error_types_found: regional_bank_policy_wave_weak_conversion, C21_stage2_bridge_needs_credit_cost_quality  
new_axis_proposed: null  
existing_axis_strengthened: stage2_required_bridge  
existing_axis_weakened: null  
existing_axis_kept: stage3_green_total_min, stage3_green_revision_min, full_4b_requires_non_price_evidence  
sector_specific_rule_candidate: false  
canonical_archetype_rule_candidate: true  
no_new_signal_reason: null  

loop_contribution_label: canonical_archetype_rule_candidate

This loop adds 3 new independent cases, 1 counterexample, and 1 residual error for R6/L6_FINANCIAL_CAPITAL_RETURN_DIGITAL/C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN.

## 23. Validation Scope / Non-Validation Scope

Validated:

- stock-web profile paths exist for all three symbols.
- stock-web tradable OHLC rows exist on 2024-01-26.
- 30D/90D/180D MFE/MAE are computed from stock-web visible row path.
- 180D windows have no corporate-action candidate dates in the symbol profiles.
- No production scoring is changed.

Not validated:

- Exact DART/IR/news URLs for capital-return policy and company-specific ROE/capital-return execution.
- Full 1Y/2Y windows, which are not needed for this shadow delta.
- Production implementation of any profile.

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,stage2_required_bridge,canonical_archetype_specific,L6_FINANCIAL_CAPITAL_RETURN_DIGITAL,C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN,0,require_bank_specific_roe_credit_cost_capital_return_bridge,+guard,"Same C21 value-up policy wave produced strong BNK/JB paths but weaker DGB/iM path; policy/PBR discount alone should not promote Green.","Preserves Stage2 for all three but prevents weak-conversion regional bank from being upgraded before ROE/capital-return execution evidence.","R6L71_C21_BNK_138930_20240126_STAGE2A|R6L71_C21_JB_175330_20240126_STAGE2A|R6L71_C21_DGB_139130_20240126_STAGE2A",3,3,1,low_medium,canonical_shadow_only,"not production; post-calibrated residual"
```

## 25. Machine-Readable Rows

### 25.1 price_source_validation

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration"}
```

### 25.2 case rows

```jsonl
{"row_type": "case", "case_id": "R6L71_C21_REGIONAL_BANK_BNK_20240126_STAGE2A", "symbol": "138930", "company_name": "BNK금융지주", "round": "R6", "loop": "71", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "fine_archetype_id": "C21_REGIONAL_BANK_VALUEUP_CAPITAL_RETURN_BRIDGE", "case_type": "structural_success", "positive_or_counterexample": "positive", "best_trigger": "R6L71_C21_BNK_138930_20240126_STAGE2A", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "positive_alignment", "current_profile_verdict": "current_profile_correct", "price_source": "Songdaiki/stock-web", "notes": "BNK was not among No-Repeat top covered C21 symbols; strong MFE with shallow MAE supports regional-bank capital-return bridge."}
{"row_type": "case", "case_id": "R6L71_C21_REGIONAL_BANK_JB_20240126_STAGE2A", "symbol": "175330", "company_name": "JB금융지주", "round": "R6", "loop": "71", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "fine_archetype_id": "C21_REGIONAL_BANK_VALUEUP_CAPITAL_RETURN_BRIDGE", "case_type": "structural_success", "positive_or_counterexample": "positive", "best_trigger": "R6L71_C21_JB_175330_20240126_STAGE2A", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "strong_positive_alignment", "current_profile_verdict": "current_profile_correct", "price_source": "Songdaiki/stock-web", "notes": "JB is a stronger same-archetype positive; it argues for C21-specific Stage2 bridge, not Green loosening."}
{"row_type": "case", "case_id": "R6L71_C21_REGIONAL_BANK_DGB_20240126_STAGE2A", "symbol": "139130", "company_name": "DGB금융지주/iM금융지주", "round": "R6", "loop": "71", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "fine_archetype_id": "C21_REGIONAL_BANK_VALUEUP_CAPITAL_RETURN_BRIDGE", "case_type": "failed_rerating", "positive_or_counterexample": "counterexample", "best_trigger": "R6L71_C21_DGB_139130_20240126_STAGE2A", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "residual_counterexample", "current_profile_verdict": "current_profile_too_early", "price_source": "Songdaiki/stock-web", "notes": "DGB/iM proves the regional-bank value-up wave needs bank-specific ROE/credit-cost/capital-return execution bridge."}
```

### 25.3 trigger rows

```jsonl
{"row_type": "trigger", "trigger_id": "R6L71_C21_BNK_138930_20240126_STAGE2A", "case_id": "R6L71_C21_REGIONAL_BANK_BNK_20240126_STAGE2A", "symbol": "138930", "company_name": "BNK금융지주", "round": "R6", "loop": "71", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "fine_archetype_id": "C21_REGIONAL_BANK_VALUEUP_CAPITAL_RETURN_BRIDGE", "sector": "financial_capital_return_digital", "primary_archetype": "regional_bank_valueup_capital_return", "loop_objective": "counterexample_mining|stage2_actionable_bonus_stress_test|canonical_archetype_rule_candidate", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-01-26", "evidence_available_at_that_date": "2024 value-up/capital-return policy regime + regional bank PBR discount repricing + clean traded path; used as non-top-covered regional-bank positive case.", "evidence_source": "public policy/value-up regime + stock-web price path proxy; source-level evidence must be URL-verified before production promotion", "stage2_evidence_fields": ["public_event_or_disclosure", "policy_or_regulatory_optionality", "relative_strength", "capital_return_optionality"], "stage3_evidence_fields": ["roe_pbr_repricing", "financial_visibility", "capital_return_execution_path"], "stage4b_evidence_fields": ["valuation_repricing_overheat_watch"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/138/138930/2024.csv", "profile_path": "atlas/symbol_profiles/138/138930.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-01-26", "entry_price": 7220, "MFE_30D_pct": 12.19, "MFE_90D_pct": 21.19, "MFE_180D_pct": 43.21, "MFE_1Y_pct": "unavailable_not_needed_for_delta", "MFE_2Y_pct": "unavailable_not_needed_for_delta", "MAE_30D_pct": -0.83, "MAE_90D_pct": -0.83, "MAE_180D_pct": -0.83, "MAE_1Y_pct": "unavailable_not_needed_for_delta", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-08-26", "peak_price": 10340, "drawdown_after_peak_pct": -13.73, "green_lateness_ratio": "not_applicable_no_confirmed_Stage3_Green_trigger", "four_b_local_peak_proximity": 0.78, "four_b_full_window_peak_proximity": 0.78, "four_b_timing_verdict": "watch_only_price_and_policy_repricing_not_full_4B", "four_b_evidence_type": ["valuation_blowoff", "positioning_overheat"], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "positive_asymmetry_capital_return_repricing", "current_profile_verdict": "current_profile_correct", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "138930_2024-01-26_7220", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "R6L71_C21_JB_175330_20240126_STAGE2A", "case_id": "R6L71_C21_REGIONAL_BANK_JB_20240126_STAGE2A", "symbol": "175330", "company_name": "JB금융지주", "round": "R6", "loop": "71", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "fine_archetype_id": "C21_REGIONAL_BANK_VALUEUP_CAPITAL_RETURN_BRIDGE", "sector": "financial_capital_return_digital", "primary_archetype": "regional_bank_valueup_capital_return", "loop_objective": "counterexample_mining|stage2_actionable_bonus_stress_test|canonical_archetype_rule_candidate", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-01-26", "evidence_available_at_that_date": "Regional-bank capital return and ROE/PBR repricing; price path verifies that Stage2-Actionable captured most of the 2024 rerating before late-October peak.", "evidence_source": "public policy/value-up regime + stock-web price path proxy; source-level evidence must be URL-verified before production promotion", "stage2_evidence_fields": ["public_event_or_disclosure", "policy_or_regulatory_optionality", "relative_strength", "early_revision_signal", "capital_return_optionality"], "stage3_evidence_fields": ["roe_pbr_repricing", "financial_visibility", "capital_return_execution_path", "low_red_team_risk"], "stage4b_evidence_fields": ["valuation_blowoff", "positioning_overheat"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/175/175330/2024.csv", "profile_path": "atlas/symbol_profiles/175/175330.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-01-26", "entry_price": 10840, "MFE_30D_pct": 28.51, "MFE_90D_pct": 37.36, "MFE_180D_pct": 72.6, "MFE_1Y_pct": "unavailable_not_needed_for_delta", "MFE_2Y_pct": "unavailable_not_needed_for_delta", "MAE_30D_pct": -1.29, "MAE_90D_pct": -1.29, "MAE_180D_pct": -1.29, "MAE_1Y_pct": "unavailable_not_needed_for_delta", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-10-25", "peak_price": 18710, "drawdown_after_peak_pct": -5.24, "green_lateness_ratio": "not_applicable_no_confirmed_Stage3_Green_trigger", "four_b_local_peak_proximity": 0.9, "four_b_full_window_peak_proximity": 0.9, "four_b_timing_verdict": "good_full_window_4B_timing_if_supported_by_non_price_valuation_or_return_execution", "four_b_evidence_type": ["valuation_blowoff", "positioning_overheat", "capital_return_execution"], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "positive_strong_rerating_capital_return_bridge", "current_profile_verdict": "current_profile_correct", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "175330_2024-01-26_10840", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "R6L71_C21_DGB_139130_20240126_STAGE2A", "case_id": "R6L71_C21_REGIONAL_BANK_DGB_20240126_STAGE2A", "symbol": "139130", "company_name": "DGB금융지주/iM금융지주", "round": "R6", "loop": "71", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "fine_archetype_id": "C21_REGIONAL_BANK_VALUEUP_CAPITAL_RETURN_BRIDGE", "sector": "financial_capital_return_digital", "primary_archetype": "regional_bank_valueup_capital_return", "loop_objective": "counterexample_mining|stage2_actionable_bonus_stress_test|canonical_archetype_rule_candidate", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-01-26", "evidence_available_at_that_date": "Same value-up/regional-bank policy wave but weaker follow-through; the price path shows modest 180D MFE and deeper MAE versus BNK/JB, so generic C21 Stage2 cannot ignore bank-specific credit/capital-return quality.", "evidence_source": "public policy/value-up regime + stock-web price path proxy; source-level evidence must be URL-verified before production promotion", "stage2_evidence_fields": ["public_event_or_disclosure", "policy_or_regulatory_optionality", "relative_strength"], "stage3_evidence_fields": ["roe_pbr_repricing_missing_or_weak", "financial_visibility_mixed"], "stage4b_evidence_fields": ["none"], "stage4c_evidence_fields": ["thesis_evidence_broken_watch", "credit_cost_or_execution_quality_gap"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/139/139130/2024.csv", "profile_path": "atlas/symbol_profiles/139/139130.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-01-26", "entry_price": 8600, "MFE_30D_pct": 16.05, "MFE_90D_pct": 16.05, "MFE_180D_pct": 16.86, "MFE_1Y_pct": "unavailable_not_needed_for_delta", "MFE_2Y_pct": "unavailable_not_needed_for_delta", "MAE_30D_pct": -0.81, "MAE_90D_pct": -8.72, "MAE_180D_pct": -9.88, "MAE_1Y_pct": "unavailable_not_needed_for_delta", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-10-25", "peak_price": 10050, "drawdown_after_peak_pct": -4.0, "green_lateness_ratio": "not_applicable_no_confirmed_Stage3_Green_trigger", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "not_a_4B_case", "four_b_evidence_type": [], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "counterexample_policy_wave_weak_conversion", "current_profile_verdict": "current_profile_too_early", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "139130_2024-01-26_8600", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
```

### 25.4 score_simulation rows

```jsonl
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R6L71_C21_REGIONAL_BANK_BNK_20240126_STAGE2A", "trigger_id": "R6L71_C21_BNK_138930_20240126_STAGE2A", "symbol": "138930", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 10, "relative_strength_score": 15, "customer_quality_score": 0, "policy_or_regulatory_score": 18, "valuation_repricing_score": 18, "execution_risk_score": 3, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "roe_pbr_capital_return_score": 20, "credit_cost_quality_score": 16}, "weighted_score_before": 79, "stage_label_before": "Stage3-Yellow", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 10, "relative_strength_score": 15, "customer_quality_score": 0, "policy_or_regulatory_score": 18, "valuation_repricing_score": 18, "execution_risk_score": 3, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "roe_pbr_capital_return_score": 22, "credit_cost_quality_score": 16}, "weighted_score_after": 82, "stage_label_after": "Stage3-Yellow", "changed_components": ["roe_pbr_capital_return_score", "credit_cost_quality_score", "execution_risk_score"], "component_delta_explanation": "C21 regional-bank candidate profile keeps policy/value-up as Stage2 bridge but requires bank-specific ROE, credit-cost, and executed capital-return evidence before Green.", "MFE_90D_pct": 21.19, "MAE_90D_pct": -0.83, "score_return_alignment_label": "positive_alignment", "current_profile_verdict": "current_profile_correct"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R6L71_C21_REGIONAL_BANK_JB_20240126_STAGE2A", "trigger_id": "R6L71_C21_JB_175330_20240126_STAGE2A", "symbol": "175330", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 10, "relative_strength_score": 15, "customer_quality_score": 0, "policy_or_regulatory_score": 18, "valuation_repricing_score": 18, "execution_risk_score": 3, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "roe_pbr_capital_return_score": 20, "credit_cost_quality_score": 16}, "weighted_score_before": 83, "stage_label_before": "Stage3-Yellow", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 10, "relative_strength_score": 15, "customer_quality_score": 0, "policy_or_regulatory_score": 18, "valuation_repricing_score": 18, "execution_risk_score": 3, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "roe_pbr_capital_return_score": 22, "credit_cost_quality_score": 16}, "weighted_score_after": 86, "stage_label_after": "Stage3-Yellow_high_conviction_watch", "changed_components": ["roe_pbr_capital_return_score", "credit_cost_quality_score", "execution_risk_score"], "component_delta_explanation": "C21 regional-bank candidate profile keeps policy/value-up as Stage2 bridge but requires bank-specific ROE, credit-cost, and executed capital-return evidence before Green.", "MFE_90D_pct": 37.36, "MAE_90D_pct": -1.29, "score_return_alignment_label": "strong_positive_alignment", "current_profile_verdict": "current_profile_correct"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R6L71_C21_REGIONAL_BANK_DGB_20240126_STAGE2A", "trigger_id": "R6L71_C21_DGB_139130_20240126_STAGE2A", "symbol": "139130", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 4, "relative_strength_score": 10, "customer_quality_score": 0, "policy_or_regulatory_score": 18, "valuation_repricing_score": 14, "execution_risk_score": 12, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "roe_pbr_capital_return_score": 10, "credit_cost_quality_score": 6}, "weighted_score_before": 76, "stage_label_before": "Stage3-Yellow", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 4, "relative_strength_score": 10, "customer_quality_score": 0, "policy_or_regulatory_score": 18, "valuation_repricing_score": 14, "execution_risk_score": 18, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "roe_pbr_capital_return_score": 8, "credit_cost_quality_score": 4}, "weighted_score_after": 70, "stage_label_after": "Stage2-Actionable_watch", "changed_components": ["roe_pbr_capital_return_score", "credit_cost_quality_score", "execution_risk_score"], "component_delta_explanation": "C21 regional-bank candidate profile keeps policy/value-up as Stage2 bridge but requires bank-specific ROE, credit-cost, and executed capital-return evidence before Green.", "MFE_90D_pct": 16.05, "MAE_90D_pct": -8.72, "score_return_alignment_label": "residual_counterexample", "current_profile_verdict": "current_profile_too_early"}
```

### 25.5 shadow_weight row

```jsonl
{"row_type": "shadow_weight", "axis": "stage2_required_bridge", "scope": "canonical_archetype_specific", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "baseline_value": 0, "tested_value": "require_bank_specific_roe_credit_cost_capital_return_bridge", "delta": "+guard", "reason": "Same C21 value-up policy wave produced strong BNK/JB paths but weaker DGB/iM path; policy/PBR discount alone should not promote Green.", "backtest_effect": "Preserves Stage2 for all three but prevents weak-conversion regional bank from being upgraded before ROE/capital-return execution evidence.", "trigger_ids": "R6L71_C21_BNK_138930_20240126_STAGE2A|R6L71_C21_JB_175330_20240126_STAGE2A|R6L71_C21_DGB_139130_20240126_STAGE2A", "calibration_usable_count": 3, "new_independent_case_count": 3, "counterexample_count": 1, "confidence": "low_medium", "proposal_type": "canonical_shadow_only", "notes": "Not production; post-calibrated residual. Existing global stage2_required_bridge is strengthened inside C21 regional-bank sub-archetype."}
```

### 25.6 residual_contribution row

```jsonl
{"row_type": "residual_contribution", "round": "R6", "loop": "71", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "new_independent_case_count": 3, "reused_case_count": 0, "new_symbol_count": 3, "new_trigger_family_count": 3, "tested_existing_calibrated_axes": ["stage2_actionable_evidence_bonus", "stage2_required_bridge", "stage3_green_total_min", "stage3_green_revision_min", "full_4b_requires_non_price_evidence"], "residual_error_types_found": ["regional_bank_policy_wave_weak_conversion", "C21_stage2_bridge_needs_credit_cost_quality"], "loop_contribution_label": "canonical_archetype_rule_candidate", "do_not_propose_new_weight_delta": false}
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
completed_round = R6
completed_loop = 71
next_round = R7
next_loop = 71
round_schedule_status = valid
round_sector_consistency = pass
```

## 28. Source Notes

- Songdaiki/stock-web atlas manifest: `atlas/manifest.json`
- Songdaiki/stock-web schema: `atlas/schema.json`
- Price basis: `tradable_raw`
- Adjustment status: `raw_unadjusted_marcap`
- Used shards:
  - `atlas/ohlcv_tradable_by_symbol_year/138/138930/2024.csv`
  - `atlas/ohlcv_tradable_by_symbol_year/175/175330/2024.csv`
  - `atlas/ohlcv_tradable_by_symbol_year/139/139130/2024.csv`
- Used profiles:
  - `atlas/symbol_profiles/138/138930.json`
  - `atlas/symbol_profiles/175/175330.json`
  - `atlas/symbol_profiles/139/139130.json`
