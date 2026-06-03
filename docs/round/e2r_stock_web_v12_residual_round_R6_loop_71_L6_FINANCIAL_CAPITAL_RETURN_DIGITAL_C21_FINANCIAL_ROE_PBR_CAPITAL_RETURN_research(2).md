# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```yaml
schema_family: v12_sector_archetype_residual
scheduled_round: R6
scheduled_loop: "71"
large_sector_id: L6_FINANCIAL_CAPITAL_RETURN_DIGITAL
canonical_archetype_id: C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN
fine_archetype_id: REGIONAL_POLICY_BANK_VALUEUP_CAPITAL_RETURN_BRIDGE_VS_POLICY_ONLY_RETAIL_FINANCE
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
output_file: e2r_stock_web_v12_residual_round_R6_loop_71_L6_FINANCIAL_CAPITAL_RETURN_DIGITAL_C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN_research.md
production_scoring_changed: false
shadow_weight_only: true
handoff_prompt_embedded: true
handoff_prompt_executed_now: false
round_schedule_status: valid
round_sector_consistency: pass
```

This loop adds **4 new independent cases**, **1 counterexample**, and **2 residual-error modes** for `R6/L6_FINANCIAL_CAPITAL_RETURN_DIGITAL/C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN`.

## 1. Current Calibrated Profile Assumption

Current proxy profile for this research:

```text
current_default_profile_proxy = e2r_2_1_stock_web_calibrated
previous_baseline_reference = e2r_2_0_baseline
```

Already-applied global axes are **not re-proposed**. This loop stress-tests `stage2_actionable_evidence_bonus`, `stage3_yellow_total_min`, and `full_4b_requires_non_price_evidence` inside C21 only.

## 2. Round / Large Sector / Canonical Archetype Scope

| field | value |
|---|---|
| round | `R6` |
| loop | `71` |
| large_sector_id | `L6_FINANCIAL_CAPITAL_RETURN_DIGITAL` |
| canonical_archetype_id | `C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN` |
| fine_archetype_id | `REGIONAL_POLICY_BANK_VALUEUP_CAPITAL_RETURN_BRIDGE_VS_POLICY_ONLY_RETAIL_FINANCE` |
| scope | Korean regional/policy bank value-up, low-PBR, capital-return bridge |
| rule_scope | `canonical_archetype_specific` |

R6 is mapped to `L6_FINANCIAL_CAPITAL_RETURN_DIGITAL`, so round-sector consistency passes.

## 3. Previous Coverage / Duplicate Avoidance Check

No-repeat index says C21 is heavily covered, but the top repeated C21 symbols are `105560`, `323410`, `086790`, `UNKNOWN_SYMBOL`, `006220`, and `055550`. This run avoids that over-covered cluster and uses `024110`, `138930`, `139130`, and `175330`.

Repository search returned no exact C21 rows for these chosen symbols:

```text
024110 C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN -> no match
138930 C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN -> no match
139130 C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN -> no match
175330 C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN -> no match
```

Hard duplicate key check:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

All four selected rows use new symbols under C21 and therefore pass the novelty gate in this session.

## 4. Stock-Web OHLC Input / Price Source Validation

| item | value |
|---|---|
| price_data_source | Songdaiki/stock-web |
| upstream_source | FinanceData/marcap |
| price_basis | tradable_raw |
| price_adjustment_status | raw_unadjusted_marcap |
| manifest_max_date | 2026-02-20 |
| calibration_shard_root | atlas/ohlcv_tradable_by_symbol_year |
| raw_shard_root | atlas/ohlcv_raw_by_symbol_year |

Checked files:

| symbol | company | profile_path | price_shard_path | corporate-action status |
|---|---|---|---|---|
| 175330 | JB금융지주 | `atlas/symbol_profiles/175/175330.json` | `atlas/ohlcv_tradable_by_symbol_year/175/175330/2024.csv` | profile candidates only 2014/2015/2018; 2024 180D window clean |
| 024110 | 기업은행 | `atlas/symbol_profiles/024/024110.json` | `atlas/ohlcv_tradable_by_symbol_year/024/024110/2024.csv` | no 2024 candidate observed in profile segment used |
| 138930 | BNK금융지주 | `atlas/symbol_profiles/138/138930.json` | `atlas/ohlcv_tradable_by_symbol_year/138/138930/2024.csv` | candidates 2014/2016; 2024 180D window clean |
| 139130 | DGB금융지주 / iM금융지주 | `atlas/symbol_profiles/139/139130.json` | `atlas/ohlcv_tradable_by_symbol_year/139/139130/2024.csv` | candidate 2015; 2024 180D window clean |

## 5. Historical Eligibility Gate

| gate | status |
|---|---|
| trigger_date is historical | pass |
| entry_date exists in tradable shard | pass |
| 180 forward trading days available before manifest max_date | pass |
| OHLCV positive and present | pass |
| MFE/MAE 30/90/180D computed | pass |
| 180D corporate-action contamination | clean for selected windows |
| exact evidence URL verification | pending |

Important limitation: evidence is currently `source_proxy_only=true` and `evidence_url_pending=true`. Therefore this loop can support residual shadow analysis, but **must not directly promote production scoring** until exact public URLs are attached.

## 6. Canonical Archetype Compression Map

| canonical | fine/deep sub-archetype | compression logic |
|---|---|---|
| C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | REGIONAL_BANK_SHAREHOLDER_RETURN_ROE_PBR_REPRICING | low PBR + shareholder return execution + stable credit cost |
| C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | POLICY_BANK_DIVIDEND_YIELD_VALUEUP_LOW_PBR | policy bank dividend/yield bridge, but 4B watch after quick repricing |
| C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | REGIONAL_BANK_VALUEUP_CET1_CAPITAL_RETURN_WITH_LAGGED_REPRICING | delayed rerating after policy event when capital-return quality improves |
| C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | REGIONAL_BANK_POLICY_ONLY_WITH_CREDIT_COST_EXECUTION_GUARD | counterexample: policy headline alone is insufficient |

## 7. Case Selection Summary

| case_id | symbol | company | role | entry | MFE90 | MAE90 | current_profile_verdict |
|---|---:|---|---|---:|---:|---:|---|
| R6L71_C21_JBFG_VALUEUP_CAPITAL_RETURN_20240129 | 175330 | JB금융지주 | positive | 11,160 | 33.42 | -3.14 | current_profile_correct |
| R6L71_C21_IBK_POLICYBANK_DIVIDEND_VALUEUP_20240129 | 024110 | 기업은행 | positive | 12,100 | 32.31 | -1.98 | current_profile_correct_but_4B_watch_needed_after_fast_repricing |
| R6L71_C21_BNK_REGIONAL_BANK_VALUEUP_20240129 | 138930 | BNK금융지주 | positive | 7,420 | 17.92 | -3.23 | current_profile_mildly_too_late_if_requires_green_confirmation |
| R6L71_C21_DGB_POLICY_ONLY_CREDIT_GUARD_20240129 | 139130 | DGB금융지주 / iM금융지주 | counterexample | 8,830 | 13.02 | -6.11 | current_profile_false_positive_if_stage2_bonus_ignores_credit_cost |

## 8. Positive vs Counterexample Balance

| metric | count |
|---|---:|
| calibration_usable_case_count | 4 |
| positive_case_count | 3 |
| counterexample_count | 1 |
| 4B_or_4C_case_count | 1 watch-only |
| new_independent_case_count | 4 |
| reused_case_count | 0 |

The balance is not enough for a production delta because exact evidence URLs are pending, but it is enough to preserve a C21-specific residual rule candidate.

## 9. Evidence Source Map

| evidence family | status | use |
|---|---|---|
| Korea value-up policy regime | source proxy | Stage2 context only |
| company capital-return / dividend / ROE-PBR disclosures | source proxy | C21 bridge, URL verification pending |
| stock-web price path | verified from shard | MFE/MAE computation |
| credit-cost / execution guard | source proxy | counterexample guard |

## 10. Price Data Source Map

| symbol | entry_date | entry_price | peak_date | peak_price | shard |
|---|---|---:|---|---:|---|
| 175330 | 2024-01-29 | 11160 | 2024-10-22 | 17250 | `atlas/ohlcv_tradable_by_symbol_year/175/175330/2024.csv` |
| 024110 | 2024-01-29 | 12100 | 2024-03-15 | 16010 | `atlas/ohlcv_tradable_by_symbol_year/024/024110/2024.csv` |
| 138930 | 2024-01-29 | 7420 | 2024-08-26 | 10340 | `atlas/ohlcv_tradable_by_symbol_year/138/138930/2024.csv` |
| 139130 | 2024-01-29 | 8830 | 2024-02-02 | 9980 | `atlas/ohlcv_tradable_by_symbol_year/139/139130/2024.csv` |

## 11. Case-by-Case Trigger Grid

| symbol | trigger_type | trigger_date | entry_date | Stage2 evidence | Stage3 bridge | 4B/4C note |
|---|---|---|---|---|---|---|
| 175330 | Stage2-Actionable | 2024-01-26 | 2024-01-29 | low PBR + shareholder-return policy | later relative strength + capital-return quality | no full 4B; upside persisted |
| 024110 | Stage2-Actionable | 2024-01-26 | 2024-01-29 | policy bank + dividend/yield value-up | fast repricing | 4B watch after 30D MFE >20 |
| 138930 | Stage2-Actionable | 2024-01-26 | 2024-01-29 | regional bank low PBR | lagged capital-return rerating | 4B watch only |
| 139130 | Stage2-Actionable | 2024-01-26 | 2024-01-29 | policy headline only | weak credit/execution bridge | counterexample; credit guard needed |

## 12. Trigger-Level OHLC Backtest Tables

| symbol | entry_price | MFE30 | MAE30 | MFE90 | MAE90 | MFE180 | MAE180 | below entry 90D |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| 175330 | 11160 | 26.34 | -3.14 | 33.42 | -3.14 | 54.57 | -3.14 | true |
| 024110 | 12100 | 23.64 | -1.98 | 32.31 | -1.98 | 32.31 | -1.98 | true |
| 138930 | 7420 | 9.16 | -3.23 | 17.92 | -3.23 | 39.35 | -3.23 | true |
| 139130 | 8830 | 13.02 | -2.83 | 13.02 | -6.11 | 13.02 | -15.74 | true |

## 13. Current Calibrated Profile Stress Test

1. Stage2 actionable bonus was useful for JB/IBK/BNK, but too permissive for DGB/iM if it is triggered by policy headline alone.
2. Yellow threshold 75 catches the positive regional-bank rerating but should require capital-return execution and credit-cost stability.
3. Green threshold 87/revision 55 should not be loosened for banks; no case here proves that Green should be easier.
4. Price-only blowoff guard remains correct.
5. Full 4B non-price requirement remains correct. Fast 20%+ local MFE in IBK/JB is not enough for full 4B without valuation/execution evidence.
6. Hard 4C routing is not tested here; DGB/iM is a watch/failed-rerating counterexample, not a hard thesis break.

## 14. Stage2 / Yellow / Green Comparison

| profile | eligible triggers | avg MFE90 | avg MAE90 | false_positive_rate | missed_structural_count | verdict |
|---|---:|---:|---:|---:|---:|---|
| P0 e2r_2_1_stock_web_calibrated_proxy | 4 | 24.07 | -3.62 | 0.25 | 0 | useful but needs C21 credit guard |
| P1 sector_specific_candidate_profile | 4 | 24.07 | -3.62 | 0.25 | 0 | no sector-wide relaxation |
| P2 canonical_archetype_candidate_profile | 4 | 27.88 | -2.78 | 0.00 selected positives after guard | 0 | best shadow profile |
| P3 counterexample_guard_profile | 1 | 13.02 | -6.11 | 1.00 | 0 | keep as policy-only guard |

## 15. 4B Local vs Full-window Timing Audit

IBK and JB both show fast local repricing after value-up triggers. This supports **4B watch**, not full 4B. JB continued to make a later high near October, so a price-only local 4B would have been too early. The existing `full_4b_requires_non_price_evidence` axis is kept.

## 16. 4C Protection Audit

No hard 4C case is claimed. DGB/iM is labeled as `thesis_break_watch_only` because the price path shows weaker upside and larger MAE when policy-only repricing lacks credit-cost / capital-return execution proof.

## 17. Sector-Specific Rule Candidate

No broad L6 sector rule is proposed. The result is C21-specific because insurance C22 has a different reserve/rate-cycle mechanism.

## 18. Canonical-Archetype Rule Candidate

```text
rule_scope = canonical_archetype_specific
rule_candidate = C21 regional/policy bank Stage2 bridge
condition:
  low_pbr_or_valueup_policy_signal
  AND explicit_capital_return_or_dividend_execution
  AND credit_cost_stability_or_no_large_accounting_trust_risk
effect:
  permit Stage2-Actionable / Stage3-Yellow watch
guard:
  policy-only headline without credit-cost / execution bridge stays Stage1/Stage2-Watch
```

## 19. Before / After Backtest Comparison

| case | before stage | after stage | score-return alignment |
|---|---|---|---|
| JB금융지주 | Stage3-Yellow | Stage3-Yellow/Green-watch | improved; keeps upside path |
| 기업은행 | Stage3-Yellow | Stage3-Yellow | unchanged but adds 4B watch after fast repricing |
| BNK금융지주 | Stage2-Actionable | Stage3-Yellow | improved; lagged rerating captured |
| DGB/iM금융지주 | Stage2-Actionable | Stage1/Stage2-Watch | improved; false positive blocked |

## 20. Score-Return Alignment Matrix

| symbol | weighted_before | weighted_after | MFE90 | MAE90 | alignment |
|---|---:|---:|---:|---:|---|
| 175330 | 78 | 81 | 33.42 | -3.14 | good |
| 024110 | 76 | 79 | 32.31 | -1.98 | good but front-loaded |
| 138930 | 72 | 76 | 17.92 | -3.23 | acceptable lagged |
| 139130 | 68 | 62 | 13.02 | -6.11 | counterexample guard |

## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive | counterexample | 4B | 4C | new_independent | reused | usable triggers | representative triggers | current_profile_error | sector_rule | canonical_rule | coverage_gap_after_this_loop |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| L6_FINANCIAL_CAPITAL_RETURN_DIGITAL | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | REGIONAL_POLICY_BANK_VALUEUP_CAPITAL_RETURN_BRIDGE_VS_POLICY_ONLY_RETAIL_FINANCE | 3 | 1 | 1 watch | 0 | 4 | 0 | 4 | 4 | 2 | false | true | evidence URL verification still needed |

## 22. Residual Contribution Summary

```yaml
new_independent_case_count: 4
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 4
new_canonical_archetype_count: 0
new_fine_archetype_count: 1
new_trigger_family_count: 1
tested_existing_calibrated_axes:
  - stage2_actionable_evidence_bonus
  - stage3_yellow_total_min
  - full_4b_requires_non_price_evidence
residual_error_types_found:
  - policy_only_stage2_false_positive
  - fast_valueup_local_4b_watch_risk
new_axis_proposed: null
existing_axis_strengthened: stage2_actionable_evidence_bonus requires C21 capital_return_plus_credit_cost bridge
existing_axis_weakened: null
existing_axis_kept:
  - stage3_green_total_min
  - stage3_green_revision_min
  - full_4b_requires_non_price_evidence
sector_specific_rule_candidate: false
canonical_archetype_rule_candidate: true
no_new_signal_reason: null
loop_contribution_label: canonical_archetype_rule_candidate
do_not_propose_new_weight_delta: true
```

`do_not_propose_new_weight_delta=true` because evidence URLs are pending and source proxy flags remain. The finding should enter the residual ledger first.

## 23. Validation Scope / Non-Validation Scope

Validation scope:

- Stock-Web 2024 tradable OHLC shards.
- Entry date and entry price from `c` column.
- 30/90/180D MFE/MAE proxy calculations.
- No-repeat search over the visible repository index/search surface.

Non-validation scope:

- Exact DART/IR/news URLs for each capital-return announcement.
- Production scoring patch.
- Live candidate discovery.
- Current recommendation.

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,c21_regional_bank_stage2_bridge,canonical_archetype_specific,L6_FINANCIAL_CAPITAL_RETURN_DIGITAL,C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN,0,require_capital_return_plus_credit_cost_guard,guardrail_only,Three regional/policy bank positives had clean positive MFE/MAE, but DGB/iM shows policy-only credit/execution drag can turn Stage2 bonus into false-positive.,improves Stage2 selectivity without loosening Green; keeps policy-only banks as Stage2-Watch until capital-return execution is verified,R6L71_C21_JBFG_VALUEUP_CAPITAL_RETURN_20240129_T1|R6L71_C21_IBK_POLICYBANK_DIVIDEND_VALUEUP_20240129_T1|R6L71_C21_BNK_REGIONAL_BANK_VALUEUP_20240129_T1|R6L71_C21_DGB_POLICY_ONLY_CREDIT_GUARD_20240129_T1,4,4,1,low_medium,canonical_archetype_shadow_only,Evidence URLs are pending; use as shadow ledger, not production promotion.
shadow_weight,c21_fast_valueup_4b_watch,canonical_archetype_specific,L6_FINANCIAL_CAPITAL_RETURN_DIGITAL,C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN,0,watch_after_30D_MFE_gt_20_without_incremental_revision,guardrail_only,IBK/JB captured quick 20%+ MFE after value-up trigger; subsequent upside varied. 4B should remain watch-only unless valuation plus non-price slowdown evidence appears.,prevents price-only local peak from becoming full 4B; retains upside path for JB-like later rerating,R6L71_C21_JBFG_VALUEUP_CAPITAL_RETURN_20240129_T1|R6L71_C21_IBK_POLICYBANK_DIVIDEND_VALUEUP_20240129_T1,2,2,0,low,canonical_archetype_shadow_only,Existing full_4b_requires_non_price_evidence kept.
```

## 25. Machine-Readable Rows

### 25.1 price_source_validation

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration"}
```

### 25.2 case rows

```jsonl
{"row_type": "case", "case_id": "R6L71_C21_JBFG_VALUEUP_CAPITAL_RETURN_20240129", "symbol": "175330", "company_name": "JB금융지주", "round": "R6", "loop": "71", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "fine_archetype_id": "REGIONAL_BANK_SHAREHOLDER_RETURN_ROE_PBR_REPRICING", "case_type": "structural_success", "positive_or_counterexample": "positive", "best_trigger": "Stage2-Actionable", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "good_stage2_valueup_capital_return_rerating", "current_profile_verdict": "current_profile_correct", "price_source": "Songdaiki/stock-web", "source_proxy_only": true, "evidence_url_pending": true, "notes": "value-up policy regime + high ROE/PBR discount + shareholder-return execution proxy"}
{"row_type": "case", "case_id": "R6L71_C21_IBK_POLICYBANK_DIVIDEND_VALUEUP_20240129", "symbol": "024110", "company_name": "기업은행", "round": "R6", "loop": "71", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "fine_archetype_id": "POLICY_BANK_DIVIDEND_YIELD_VALUEUP_LOW_PBR", "case_type": "structural_success", "positive_or_counterexample": "positive", "best_trigger": "Stage2-Actionable", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "front_loaded_valueup_bank_repricing_then_plateau", "current_profile_verdict": "current_profile_correct_but_4B_watch_needed_after_fast_repricing", "price_source": "Songdaiki/stock-web", "source_proxy_only": true, "evidence_url_pending": true, "notes": "policy bank dividend/value-up proxy + low PBR repricing + financial sector relative strength"}
{"row_type": "case", "case_id": "R6L71_C21_BNK_REGIONAL_BANK_VALUEUP_20240129", "symbol": "138930", "company_name": "BNK금융지주", "round": "R6", "loop": "71", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "fine_archetype_id": "REGIONAL_BANK_VALUEUP_CET1_CAPITAL_RETURN_WITH_LAGGED_REPRICING", "case_type": "structural_success", "positive_or_counterexample": "positive", "best_trigger": "Stage2-Actionable", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "lagged_valueup_repricing_after_initial_bank_rally", "current_profile_verdict": "current_profile_mildly_too_late_if_requires_green_confirmation", "price_source": "Songdaiki/stock-web", "source_proxy_only": true, "evidence_url_pending": true, "notes": "regional bank low PBR + value-up policy + capital return visibility proxy"}
{"row_type": "case", "case_id": "R6L71_C21_DGB_POLICY_ONLY_CREDIT_GUARD_20240129", "symbol": "139130", "company_name": "DGB금융지주 / iM금융지주", "round": "R6", "loop": "71", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "fine_archetype_id": "REGIONAL_BANK_POLICY_ONLY_WITH_CREDIT_COST_EXECUTION_GUARD", "case_type": "failed_rerating", "positive_or_counterexample": "counterexample", "best_trigger": "Stage2-Actionable", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "policy_only_valueup_false_positive_credit_execution_drag", "current_profile_verdict": "current_profile_false_positive_if_stage2_bonus_ignores_credit_cost", "price_source": "Songdaiki/stock-web", "source_proxy_only": true, "evidence_url_pending": true, "notes": "regional bank value-up headline without enough credit-cost/capital-return execution proof"}
```

### 25.3 trigger rows

```jsonl
{"row_type": "trigger", "trigger_id": "R6L71_C21_JBFG_VALUEUP_CAPITAL_RETURN_20240129_T1", "case_id": "R6L71_C21_JBFG_VALUEUP_CAPITAL_RETURN_20240129", "symbol": "175330", "company_name": "JB금융지주", "round": "R6", "loop": "71", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "fine_archetype_id": "REGIONAL_BANK_SHAREHOLDER_RETURN_ROE_PBR_REPRICING", "sector": "financials / banks / capital return / value-up", "primary_archetype": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "loop_objective": "coverage_gap_fill|counterexample_mining|sector_specific_rule_discovery|canonical_archetype_compression|stage2_actionable_bonus_stress_test|4B_non_price_requirement_stress_test", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-01-26", "evidence_available_at_that_date": "2024 value-up policy regime and bank capital-return/low-PBR public-event proxy; exact URL verification pending", "evidence_source": "public-event proxy: Korea value-up policy + company capital-return/ROE/PBR disclosures/reports", "stage2_evidence_fields": ["policy_or_regulatory_optionality", "capital_return_visibility", "low_pbr_mispricing", "relative_strength"], "stage3_evidence_fields": ["confirmed_revision", "executed_capital_return", "credit_cost_stability"], "stage4b_evidence_fields": ["valuation_blowoff", "positioning_overheat"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/175/175330/2024.csv", "profile_path": "atlas/symbol_profiles/175/175330.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-01-29", "entry_price": 11160, "MFE_30D_pct": 26.34, "MFE_90D_pct": 33.42, "MFE_180D_pct": 54.57, "MFE_1Y_pct": "not_computed", "MFE_2Y_pct": "not_computed", "MAE_30D_pct": -3.14, "MAE_90D_pct": -3.14, "MAE_180D_pct": -3.14, "MAE_1Y_pct": "not_computed", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-10-22", "peak_price": 17250, "drawdown_after_peak_pct": -2.0, "green_lateness_ratio": "not_applicable_no_confirmed_green_trigger", "four_b_local_peak_proximity": "not_applicable", "four_b_full_window_peak_proximity": "not_applicable", "four_b_timing_verdict": "watch_only_fast_repricing", "four_b_evidence_type": "price_only|valuation_blowoff", "four_c_protection_label": "not_applicable", "trigger_outcome_label": "good_stage2_valueup_capital_return_rerating", "current_profile_verdict": "current_profile_correct", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R6L71_C21_JBFG_VALUEUP_CAPITAL_RETURN_20240129_ENTRY_20240129", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "source_proxy_only": true, "evidence_url_pending": true}
{"row_type": "trigger", "trigger_id": "R6L71_C21_IBK_POLICYBANK_DIVIDEND_VALUEUP_20240129_T1", "case_id": "R6L71_C21_IBK_POLICYBANK_DIVIDEND_VALUEUP_20240129", "symbol": "024110", "company_name": "기업은행", "round": "R6", "loop": "71", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "fine_archetype_id": "POLICY_BANK_DIVIDEND_YIELD_VALUEUP_LOW_PBR", "sector": "financials / banks / capital return / value-up", "primary_archetype": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "loop_objective": "coverage_gap_fill|counterexample_mining|sector_specific_rule_discovery|canonical_archetype_compression|stage2_actionable_bonus_stress_test|4B_non_price_requirement_stress_test", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-01-26", "evidence_available_at_that_date": "2024 value-up policy regime and bank capital-return/low-PBR public-event proxy; exact URL verification pending", "evidence_source": "public-event proxy: Korea value-up policy + company capital-return/ROE/PBR disclosures/reports", "stage2_evidence_fields": ["policy_or_regulatory_optionality", "capital_return_visibility", "low_pbr_mispricing", "relative_strength"], "stage3_evidence_fields": ["confirmed_revision", "executed_capital_return", "credit_cost_stability"], "stage4b_evidence_fields": ["valuation_blowoff", "positioning_overheat"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/024/024110/2024.csv", "profile_path": "atlas/symbol_profiles/024/024110.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-01-29", "entry_price": 12100, "MFE_30D_pct": 23.64, "MFE_90D_pct": 32.31, "MFE_180D_pct": 32.31, "MFE_1Y_pct": "not_computed", "MFE_2Y_pct": "not_computed", "MAE_30D_pct": -1.98, "MAE_90D_pct": -1.98, "MAE_180D_pct": -1.98, "MAE_1Y_pct": "not_computed", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-03-15", "peak_price": 16010, "drawdown_after_peak_pct": -16.86, "green_lateness_ratio": "not_applicable_no_confirmed_green_trigger", "four_b_local_peak_proximity": "not_applicable", "four_b_full_window_peak_proximity": "not_applicable", "four_b_timing_verdict": "watch_only_fast_repricing", "four_b_evidence_type": "price_only|valuation_blowoff", "four_c_protection_label": "not_applicable", "trigger_outcome_label": "front_loaded_valueup_bank_repricing_then_plateau", "current_profile_verdict": "current_profile_correct_but_4B_watch_needed_after_fast_repricing", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R6L71_C21_IBK_POLICYBANK_DIVIDEND_VALUEUP_20240129_ENTRY_20240129", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "source_proxy_only": true, "evidence_url_pending": true}
{"row_type": "trigger", "trigger_id": "R6L71_C21_BNK_REGIONAL_BANK_VALUEUP_20240129_T1", "case_id": "R6L71_C21_BNK_REGIONAL_BANK_VALUEUP_20240129", "symbol": "138930", "company_name": "BNK금융지주", "round": "R6", "loop": "71", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "fine_archetype_id": "REGIONAL_BANK_VALUEUP_CET1_CAPITAL_RETURN_WITH_LAGGED_REPRICING", "sector": "financials / banks / capital return / value-up", "primary_archetype": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "loop_objective": "coverage_gap_fill|counterexample_mining|sector_specific_rule_discovery|canonical_archetype_compression|stage2_actionable_bonus_stress_test|4B_non_price_requirement_stress_test", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-01-26", "evidence_available_at_that_date": "2024 value-up policy regime and bank capital-return/low-PBR public-event proxy; exact URL verification pending", "evidence_source": "public-event proxy: Korea value-up policy + company capital-return/ROE/PBR disclosures/reports", "stage2_evidence_fields": ["policy_or_regulatory_optionality", "capital_return_visibility", "low_pbr_mispricing", "relative_strength"], "stage3_evidence_fields": ["confirmed_revision", "executed_capital_return", "credit_cost_stability"], "stage4b_evidence_fields": [], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/138/138930/2024.csv", "profile_path": "atlas/symbol_profiles/138/138930.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-01-29", "entry_price": 7420, "MFE_30D_pct": 9.16, "MFE_90D_pct": 17.92, "MFE_180D_pct": 39.35, "MFE_1Y_pct": "not_computed", "MFE_2Y_pct": "not_computed", "MAE_30D_pct": -3.23, "MAE_90D_pct": -3.23, "MAE_180D_pct": -3.23, "MAE_1Y_pct": "not_computed", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-08-26", "peak_price": 10340, "drawdown_after_peak_pct": -12.6, "green_lateness_ratio": "not_applicable_no_confirmed_green_trigger", "four_b_local_peak_proximity": "not_applicable", "four_b_full_window_peak_proximity": "not_applicable", "four_b_timing_verdict": "not_applicable", "four_b_evidence_type": "not_applicable", "four_c_protection_label": "not_applicable", "trigger_outcome_label": "lagged_valueup_repricing_after_initial_bank_rally", "current_profile_verdict": "current_profile_mildly_too_late_if_requires_green_confirmation", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R6L71_C21_BNK_REGIONAL_BANK_VALUEUP_20240129_ENTRY_20240129", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "source_proxy_only": true, "evidence_url_pending": true}
{"row_type": "trigger", "trigger_id": "R6L71_C21_DGB_POLICY_ONLY_CREDIT_GUARD_20240129_T1", "case_id": "R6L71_C21_DGB_POLICY_ONLY_CREDIT_GUARD_20240129", "symbol": "139130", "company_name": "DGB금융지주 / iM금융지주", "round": "R6", "loop": "71", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "fine_archetype_id": "REGIONAL_BANK_POLICY_ONLY_WITH_CREDIT_COST_EXECUTION_GUARD", "sector": "financials / banks / capital return / value-up", "primary_archetype": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "loop_objective": "coverage_gap_fill|counterexample_mining|sector_specific_rule_discovery|canonical_archetype_compression|stage2_actionable_bonus_stress_test|4B_non_price_requirement_stress_test", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-01-26", "evidence_available_at_that_date": "2024 value-up policy regime and bank capital-return/low-PBR public-event proxy; exact URL verification pending", "evidence_source": "public-event proxy: Korea value-up policy + company capital-return/ROE/PBR disclosures/reports", "stage2_evidence_fields": ["policy_or_regulatory_optionality", "capital_return_visibility", "low_pbr_mispricing", "relative_strength"], "stage3_evidence_fields": [], "stage4b_evidence_fields": [], "stage4c_evidence_fields": ["credit_cost_or_execution_risk"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/139/139130/2024.csv", "profile_path": "atlas/symbol_profiles/139/139130.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-01-29", "entry_price": 8830, "MFE_30D_pct": 13.02, "MFE_90D_pct": 13.02, "MFE_180D_pct": 13.02, "MFE_1Y_pct": "not_computed", "MFE_2Y_pct": "not_computed", "MAE_30D_pct": -2.83, "MAE_90D_pct": -6.11, "MAE_180D_pct": -15.74, "MAE_1Y_pct": "not_computed", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-02-02", "peak_price": 9980, "drawdown_after_peak_pct": -25.45, "green_lateness_ratio": "not_applicable_no_confirmed_green_trigger", "four_b_local_peak_proximity": "not_applicable", "four_b_full_window_peak_proximity": "not_applicable", "four_b_timing_verdict": "not_applicable", "four_b_evidence_type": "not_applicable", "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "policy_only_valueup_false_positive_credit_execution_drag", "current_profile_verdict": "current_profile_false_positive_if_stage2_bonus_ignores_credit_cost", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R6L71_C21_DGB_POLICY_ONLY_CREDIT_GUARD_20240129_ENTRY_20240129", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "source_proxy_only": true, "evidence_url_pending": true}
```

### 25.4 score_simulation rows

```jsonl
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R6L71_C21_JBFG_VALUEUP_CAPITAL_RETURN_20240129", "trigger_id": "R6L71_C21_JBFG_VALUEUP_CAPITAL_RETURN_20240129_T1", "symbol": "175330", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 45, "revision_score": 62, "relative_strength_score": 58, "customer_quality_score": 45, "policy_or_regulatory_score": 65, "valuation_repricing_score": 78, "execution_risk_score": 22, "legal_or_contract_risk_score": 10, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 18}, "weighted_score_before": 78, "stage_label_before": "Stage3-Yellow", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 50, "revision_score": 67, "relative_strength_score": 60, "customer_quality_score": 50, "policy_or_regulatory_score": 68, "valuation_repricing_score": 82, "execution_risk_score": 20, "legal_or_contract_risk_score": 10, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 16}, "weighted_score_after": 81, "stage_label_after": "Stage3-Yellow/Green-watch", "changed_components": ["roe_pbr_capital_return_score", "credit_cost_guard", "policy_only_penalty"], "component_delta_explanation": "Within C21, policy/value-up headline receives no positive promotion unless ROE/PBR repricing is paired with explicit capital-return execution and credit-cost stability; DGB/iM counterexample tightens policy-only bridge.", "MFE_90D_pct": 33.42, "MAE_90D_pct": -3.14, "score_return_alignment_label": "good_stage2_valueup_capital_return_rerating", "current_profile_verdict": "current_profile_correct"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R6L71_C21_IBK_POLICYBANK_DIVIDEND_VALUEUP_20240129", "trigger_id": "R6L71_C21_IBK_POLICYBANK_DIVIDEND_VALUEUP_20240129_T1", "symbol": "024110", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 50, "revision_score": 58, "relative_strength_score": 62, "customer_quality_score": 42, "policy_or_regulatory_score": 70, "valuation_repricing_score": 74, "execution_risk_score": 18, "legal_or_contract_risk_score": 8, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 15}, "weighted_score_before": 76, "stage_label_before": "Stage3-Yellow", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 52, "revision_score": 62, "relative_strength_score": 65, "customer_quality_score": 45, "policy_or_regulatory_score": 72, "valuation_repricing_score": 78, "execution_risk_score": 18, "legal_or_contract_risk_score": 8, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 14}, "weighted_score_after": 79, "stage_label_after": "Stage3-Yellow", "changed_components": ["roe_pbr_capital_return_score", "credit_cost_guard", "policy_only_penalty"], "component_delta_explanation": "Within C21, policy/value-up headline receives no positive promotion unless ROE/PBR repricing is paired with explicit capital-return execution and credit-cost stability; DGB/iM counterexample tightens policy-only bridge.", "MFE_90D_pct": 32.31, "MAE_90D_pct": -1.98, "score_return_alignment_label": "front_loaded_valueup_bank_repricing_then_plateau", "current_profile_verdict": "current_profile_correct_but_4B_watch_needed_after_fast_repricing"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R6L71_C21_BNK_REGIONAL_BANK_VALUEUP_20240129", "trigger_id": "R6L71_C21_BNK_REGIONAL_BANK_VALUEUP_20240129_T1", "symbol": "138930", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 45, "revision_score": 54, "relative_strength_score": 48, "customer_quality_score": 40, "policy_or_regulatory_score": 66, "valuation_repricing_score": 76, "execution_risk_score": 28, "legal_or_contract_risk_score": 12, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 20}, "weighted_score_before": 72, "stage_label_before": "Stage2-Actionable", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 48, "revision_score": 58, "relative_strength_score": 54, "customer_quality_score": 45, "policy_or_regulatory_score": 70, "valuation_repricing_score": 80, "execution_risk_score": 25, "legal_or_contract_risk_score": 12, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 18}, "weighted_score_after": 76, "stage_label_after": "Stage3-Yellow", "changed_components": ["roe_pbr_capital_return_score", "credit_cost_guard", "policy_only_penalty"], "component_delta_explanation": "Within C21, policy/value-up headline receives no positive promotion unless ROE/PBR repricing is paired with explicit capital-return execution and credit-cost stability; DGB/iM counterexample tightens policy-only bridge.", "MFE_90D_pct": 17.92, "MAE_90D_pct": -3.23, "score_return_alignment_label": "lagged_valueup_repricing_after_initial_bank_rally", "current_profile_verdict": "current_profile_mildly_too_late_if_requires_green_confirmation"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R6L71_C21_DGB_POLICY_ONLY_CREDIT_GUARD_20240129", "trigger_id": "R6L71_C21_DGB_POLICY_ONLY_CREDIT_GUARD_20240129_T1", "symbol": "139130", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 35, "revision_score": 42, "relative_strength_score": 50, "customer_quality_score": 35, "policy_or_regulatory_score": 65, "valuation_repricing_score": 72, "execution_risk_score": 45, "legal_or_contract_risk_score": 15, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 30}, "weighted_score_before": 68, "stage_label_before": "Stage2-Actionable", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 30, "revision_score": 38, "relative_strength_score": 42, "customer_quality_score": 32, "policy_or_regulatory_score": 60, "valuation_repricing_score": 64, "execution_risk_score": 55, "legal_or_contract_risk_score": 18, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 36}, "weighted_score_after": 62, "stage_label_after": "Stage1/Stage2-Watch", "changed_components": ["roe_pbr_capital_return_score", "credit_cost_guard", "policy_only_penalty"], "component_delta_explanation": "Within C21, policy/value-up headline receives no positive promotion unless ROE/PBR repricing is paired with explicit capital-return execution and credit-cost stability; DGB/iM counterexample tightens policy-only bridge.", "MFE_90D_pct": 13.02, "MAE_90D_pct": -6.11, "score_return_alignment_label": "policy_only_valueup_false_positive_credit_execution_drag", "current_profile_verdict": "current_profile_false_positive_if_stage2_bonus_ignores_credit_cost"}
```

### 25.5 shadow_weight rows

```jsonl
{"row_type": "shadow_weight", "axis": "c21_regional_bank_stage2_bridge", "scope": "canonical_archetype_specific", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "baseline_value": 0, "tested_value": "require_capital_return_plus_credit_cost_guard", "delta": "guardrail_only", "reason": "Three regional/policy bank positives had clean positive MFE/MAE, but DGB/iM shows policy-only credit/execution drag can turn Stage2 bonus into false-positive.", "backtest_effect": "improves Stage2 selectivity without loosening Green; keeps policy-only banks as Stage2-Watch until capital-return execution is verified", "trigger_ids": "R6L71_C21_JBFG_VALUEUP_CAPITAL_RETURN_20240129_T1|R6L71_C21_IBK_POLICYBANK_DIVIDEND_VALUEUP_20240129_T1|R6L71_C21_BNK_REGIONAL_BANK_VALUEUP_20240129_T1|R6L71_C21_DGB_POLICY_ONLY_CREDIT_GUARD_20240129_T1", "calibration_usable_count": 4, "new_independent_case_count": 4, "counterexample_count": 1, "confidence": "low_medium", "proposal_type": "canonical_archetype_shadow_only", "notes": "Evidence URLs are pending; use as shadow ledger, not production promotion."}
{"row_type": "shadow_weight", "axis": "c21_fast_valueup_4b_watch", "scope": "canonical_archetype_specific", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "baseline_value": 0, "tested_value": "watch_after_30D_MFE_gt_20_without_incremental_revision", "delta": "guardrail_only", "reason": "IBK/JB captured quick 20%+ MFE after value-up trigger; subsequent upside varied. 4B should remain watch-only unless valuation plus non-price slowdown evidence appears.", "backtest_effect": "prevents price-only local peak from becoming full 4B; retains upside path for JB-like later rerating", "trigger_ids": "R6L71_C21_JBFG_VALUEUP_CAPITAL_RETURN_20240129_T1|R6L71_C21_IBK_POLICYBANK_DIVIDEND_VALUEUP_20240129_T1", "calibration_usable_count": 2, "new_independent_case_count": 2, "counterexample_count": 0, "confidence": "low", "proposal_type": "canonical_archetype_shadow_only", "notes": "Existing full_4b_requires_non_price_evidence kept."}
```

### 25.6 residual_contribution row

```jsonl
{"row_type": "residual_contribution", "round": "R6", "loop": "71", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "new_independent_case_count": 4, "reused_case_count": 0, "new_symbol_count": 4, "new_trigger_family_count": 1, "tested_existing_calibrated_axes": ["stage2_actionable_evidence_bonus", "stage3_yellow_total_min", "full_4b_requires_non_price_evidence"], "residual_error_types_found": ["policy_only_stage2_false_positive", "fast_valueup_local_4b_watch_risk"], "loop_contribution_label": "canonical_archetype_rule_candidate", "do_not_propose_new_weight_delta": true, "reason": "source_proxy_only/evidence_url_pending rows require URL verification before any promotion"}
```

## 26. Deferred Coding Agent Handoff Prompt

### Purpose

You are now in the repository implementation phase. The attached Markdown files are v12 post-calibrated residual research outputs produced using the Songdaiki/stock-web OHLC atlas.

These MDs are not live candidate research. They are historical calibration research designed to extend the already-applied e2r_2_1_stock_web_calibrated profile.

Do not blindly apply every shadow row.

### Price source context

- Primary historical price source used by the research MD: Songdaiki/stock-web.
- Price basis: tradable_raw.
- Price adjustment status: raw_unadjusted_marcap.
- Price shard pattern: `atlas/ohlcv_tradable_by_symbol_year/<prefix>/<ticker>/<year>.csv`.
- Symbol profile pattern: `atlas/symbol_profiles/<prefix>/<ticker>.json`.

### Rules

- Use only `calibration_usable=true` rows for quantitative calibration.
- Do not count reused cases as new independent evidence unless `independent_evidence_weight > 0`.
- Do not treat `schema_rematerialization_only` or `duplicate_low_value_loop` as new evidence.
- Do not apply global deltas unless multiple large_sector_id values support the same direction.
- Positive score promotion requires non-price evidence and clean 180D MFE/MAE.
- `source_proxy_only=true` and `evidence_url_pending=true` rows must not be promoted until exact URLs are attached.
- For C21, policy/value-up headline alone must not trigger Stage2-Actionable without capital-return execution and credit-cost stability.

### Expected repository tasks

1. Parse case / trigger / score_simulation / shadow_weight / residual_contribution rows.
2. Validate stock-web price source fields.
3. Validate large_sector_id and canonical_archetype_id.
4. Validate novelty and reuse fields.
5. Deduplicate same_entry_group_id and reused cases.
6. Add this loop to the C21 residual ledger.
7. Keep this as a shadow rule until evidence URLs are verified.
8. Add tests that source-proxy-only positive rows cannot change production weights.

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

- Main execution prompt: `docs/core/e2r_v12_prompt_round_scheduler_corrected.txt`.
- No-repeat ledger: `docs/core/V12_Research_No_Repeat_Index.md`.
- Price manifest: `Songdaiki/stock-web/atlas/manifest.json`.
- Price schema: `Songdaiki/stock-web/atlas/schema.json`.
- Profile/shard paths are recorded in the machine-readable trigger rows.
- Evidence URL verification is deliberately marked pending.
