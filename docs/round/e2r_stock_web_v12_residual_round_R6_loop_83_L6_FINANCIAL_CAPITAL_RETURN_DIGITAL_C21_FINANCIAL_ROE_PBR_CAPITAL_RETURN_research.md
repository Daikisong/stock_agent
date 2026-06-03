# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```json
{
  "research_session": "post_calibrated_sector_archetype_residual_research",
  "mode": "historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12",
  "scheduled_round": "R6",
  "scheduled_loop": 83,
  "round_schedule_status": "valid",
  "round_sector_consistency": "pass",
  "completed_round": "R6",
  "completed_loop": 83,
  "computed_next_round": "R7",
  "computed_next_loop": 83,
  "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL",
  "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN",
  "fine_archetype_id": "REGIONAL_BANK_VALUEUP_CAPITAL_RETURN_EXECUTION_VS_CAPITAL_QUALITY_HIGH_MAE_BETA",
  "loop_objective": [
    "coverage_gap_fill",
    "counterexample_mining",
    "4B_non_price_requirement_stress_test",
    "canonical_archetype_compression",
    "source_repair_queue_creation"
  ],
  "price_source": "Songdaiki/stock-web",
  "price_basis": "tradable_raw",
  "price_adjustment_status": "raw_unadjusted_marcap",
  "stock_web_manifest_max_date": "2026-02-20",
  "production_scoring_changed": false,
  "shadow_weight_only": true,
  "handoff_prompt_executed_now": false,
  "do_not_propose_new_weight_delta": true
}
```

This loop adds 3 new independent cases, 1 counterexample, and 2 residual errors for R6/L6_FINANCIAL_CAPITAL_RETURN_DIGITAL/C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN.

## 1. Current Calibrated Profile Assumption

```text
before_profile_id = e2r_2_1_stock_web_calibrated_proxy
rollback_reference_profile_id = e2r_2_0_baseline_reference
after_profile_id = proposed_C21_capital_return_execution_and_high_MAE_guard_shadow_profile
production_scoring_changed = false
shadow_weight_only = true
```

Already-applied global axes are treated as baseline, not re-proposed globally:

```text
stage2_actionable_evidence_bonus
stage3_yellow_total_min
stage3_green_total_min
stage3_green_revision_min
stage3_cross_evidence_green_buffer
price_only_blowoff_blocks_positive_stage
full_4b_requires_non_price_evidence
hard_4c_thesis_break_routes_to_4c
```

## 2. Round / Large Sector / Canonical Archetype Scope

```text
scheduled_round = R6
scheduled_loop = 83
allowed_large_sector = L6_FINANCIAL_CAPITAL_RETURN_DIGITAL
selected_large_sector = L6_FINANCIAL_CAPITAL_RETURN_DIGITAL
selected_canonical_archetype_id = C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN
computed_next_round = R7
computed_next_loop = 83
```

R6 is the financial/capital-return round. This file stays inside C21 and tests whether low-PBR bank value-up beta should require repaired capital-return execution and capital-buffer quality before being counted as Stage2-Actionable.

## 3. Previous Coverage / Duplicate Avoidance Check

No-Repeat is used only as a duplicate ledger.

```text
hard_duplicate_key = canonical_archetype_id + symbol + trigger_type + entry_date
```

C21 is heavily covered in the bank-holdco / platform-bank names:

```text
top-covered C21 symbols include:
105560, 323410, 086790, UNKNOWN_SYMBOL, 006220, 055550
```

This run avoids those top-covered combinations and uses:

```text
024110 / 기업은행 / state-bank dividend-capital-return execution route
175330 / JB금융지주 / regional-bank capital-return route with high-MAE guard
139130 / DGB금융지주/iM금융지주 / regional-bank value-up false-positive and capital-quality guard
```

All three are new independent cases for this C21 loop. No selected row intentionally reuses the same canonical+symbol+trigger_type+entry_date key.

## 4. Stock-Web OHLC Input / Price Source Validation

```text
source = Songdaiki/stock-web
upstream_source = FinanceData/marcap
price_basis = tradable_raw
price_adjustment_status = raw_unadjusted_marcap
manifest_max_date = 2026-02-20
calibration_shard_root = atlas/ohlcv_tradable_by_symbol_year
raw_shard_root = atlas/ohlcv_raw_by_symbol_year
```

Symbol profile checks:

| symbol | company | profile path | corporate-action candidate dates | selected 2024 180D status |
|---|---|---|---|---|
| 024110 | 기업은행 | atlas/symbol_profiles/024/024110.json | 1998-10-27, 1998-11-05, 2000-02-02, 2003-12-24 | clean |
| 175330 | JB금융지주 | atlas/symbol_profiles/175/175330.json | 2014-01-29, 2014-09-26, 2015-12-01, 2018-10-26 | clean |
| 139130 | DGB금융지주/iM금융지주 | atlas/symbol_profiles/139/139130.json | 2015-01-29 | clean |

## 5. Historical Eligibility Gate

| case_id | symbol | trigger_date | entry_date | entry_price | forward_window_trading_days | 180D clean | calibration_usable |
|---|---:|---|---|---:|---:|---|---|
| C21-R6L83-IBK-20240226 | 024110 | 2024-02-26 | 2024-02-26 | 13400 | 180 | yes | true |
| C21-R6L83-JBFG-20240226 | 175330 | 2024-02-26 | 2024-02-26 | 13360 | 180 | yes | true |
| C21-R6L83-DGB-20240226 | 139130 | 2024-02-26 | 2024-02-26 | 9140 | 180 | yes | true |

Entry rule: trigger evidence is treated as broad value-up / bank capital-return policy visibility around the 2024-02-26 bank basket reaction window. Because exact intraday timestamp is not repaired in this file, entry uses the same tradable-day close.

## 6. Canonical Archetype Compression Map

| canonical_archetype_id | fine/deep route | promote logic | guard logic |
|---|---|---|---|
| C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | STATE_BANK_DIVIDEND_YIELD_CAPITAL_RETURN | Allow Stage2-Actionable when value-up is tied to dividend/capital-return execution and controlled MAE. | Keep Green blocked until capital buffer and payout execution are repaired. |
| C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | REGIONAL_BANK_CAPITAL_RETURN_HIGH_MAE | Allow positive lifecycle but attach high-MAE RiskWatch if post-entry drawdown is wide. | Do not count low-PBR beta alone as strong C21 evidence. |
| C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | REGIONAL_BANK_VALUEUP_PRICE_BETA_FALSE_POSITIVE | Treat as counterexample if MFE is small and MAE/drawdown dominate. | Strengthen capital-quality and shareholder-return execution bridge. |

## 7. Case Selection Summary

| case | symbol | role | reason |
|---|---:|---|---|
| IBK state-bank route | 024110 | positive | controlled positive path; dividend/capital-return story has measurable upside with limited MAE. |
| JB regional bank route | 175330 | positive with guard | large 90D/180D MFE but high MAE; should be Stage2/RiskWatch rather than clean Green. |
| DGB/iM regional bank route | 139130 | counterexample | value-up beta had small MFE and wide MAE; current profile can overcredit generic low-PBR narrative. |

## 8. Positive vs Counterexample Balance

```text
positive_case_count = 2
counterexample_count = 1
4B_case_count = 1
4C_case_count = 0
calibration_usable_case_count = 3
```

## 9. Evidence Source Map

```text
source_proxy_only = true
evidence_url_pending = true
source_repair_required = true
```

This file intentionally does not claim production-ready evidence. It creates a source-repair queue for C21: capital return execution, CET1/capital buffer, payout policy, buyback/dividend, and ROE/PBR normalization bridge.

## 10. Price Data Source Map

| symbol | price shard | profile |
|---|---|---|
| 024110 | atlas/ohlcv_tradable_by_symbol_year/024/024110/2024.csv | atlas/symbol_profiles/024/024110.json |
| 175330 | atlas/ohlcv_tradable_by_symbol_year/175/175330/2024.csv | atlas/symbol_profiles/175/175330.json |
| 139130 | atlas/ohlcv_tradable_by_symbol_year/139/139130/2024.csv | atlas/symbol_profiles/139/139130.json |

## 11. Case-by-Case Trigger Grid

| trigger_id | symbol | trigger_type | entry_date | current_profile_verdict | role |
|---|---:|---|---|---|---|
| C21-R6L83-IBK-20240226-S2A | 024110 | Stage2-Actionable | 2024-02-26 | current_profile_correct | representative |
| C21-R6L83-JBFG-20240226-S2A | 175330 | Stage2-Actionable | 2024-02-26 | current_profile_too_early | representative |
| C21-R6L83-DGB-20240226-FP | 139130 | Stage2-FalsePositive | 2024-02-26 | current_profile_false_positive | representative |

## 12. Trigger-Level OHLC Backtest Tables

| symbol | entry_price | MFE_30D | MAE_30D | MFE_90D | MAE_90D | MFE_180D | MAE_180D | peak_date | peak_price | drawdown_after_peak |
|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|---:|
| 024110 | 13400 | 19.48 | -2.01 | 19.48 | -6.64 | 19.48 | -6.64 | 2024-03-15 | 16010 | -20.11 |
| 175330 | 13360 | 5.54 | -8.61 | 20.88 | -14.75 | 20.88 | -14.75 | 2024-07-05 | 16150 | -19.63 |
| 139130 | 9140 | 2.95 | -8.10 | 2.95 | -15.21 | 2.95 | -18.60 | 2024-03-15 | 9410 | -20.93 |

## 13. Current Calibrated Profile Stress Test

| symbol | current profile likely label | observed path | verdict |
|---:|---|---|---|
| 024110 | Stage2-Actionable | controlled positive with dividend/capital-return route | current_profile_correct |
| 175330 | Stage2-Actionable / possible Yellow | good MFE but high MAE and drawdown; needs RiskWatch overlay | current_profile_too_early |
| 139130 | Stage2-Actionable if generic value-up beta is overcredited | small MFE, wide MAE, no repaired capital-return bridge | current_profile_false_positive |

## 14. Stage2 / Yellow / Green Comparison

```text
Stage2-Actionable:
  useful for 024110 when capital-return bridge exists.
  too permissive for 139130 if it only sees low-PBR/value-up beta.

Stage3-Yellow:
  reasonable for 175330 only after MAE and capital buffer risk are accepted.

Stage3-Green:
  should remain blocked until source repair confirms explicit payout execution, capital-buffer quality and repeatability.
```

## 15. 4B Local vs Full-window Timing Audit

| symbol | local 4B interpretation | full-window interpretation |
|---:|---|---|
| 024110 | post-peak drawdown watch after March high | not full 4B without non-price thesis damage |
| 175330 | local 4B watch after July high | full 4B requires capital-quality or payout-execution deterioration |
| 139130 | high-MAE / low-MFE local 4B watch | price-only hard 4C not allowed |

## 16. 4C Protection Audit

```text
hard_4c_success = not_applicable
hard_4c_late = not_applicable
false_break = not_applicable
thesis_break_watch_only = 139130
```

No hard 4C is proposed. C21 capital-return rows need capital-buffer or payout-policy thesis break before 4C.

## 17. Sector-Specific Rule Candidate

```text
rule_scope = canonical_archetype_specific
axis = C21_capital_return_execution_and_capital_buffer_bridge
proposal_type = shadow_only
```

Candidate rule:

```text
For C21, Stage2-Actionable should require at least one repaired bridge:
  - explicit dividend/buyback/capital-return execution
  - CET1/capital-buffer quality
  - ROE/PBR normalization path with management or regulatory support
  - controlled MAE or explained high-MAE risk

Generic low-PBR or value-up policy beta without this bridge should stay Stage2-Watch or RiskWatch.
```

## 18. Canonical-Archetype Rule Candidate

```text
canonical_archetype_id = C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN
canonical_rule_candidate = C21_capital_buffer_quality_required_for_regional_bank_green
```

## 19. Before / After Backtest Comparison

| profile | eligible triggers | avg MFE_90D | avg MAE_90D | false positive count | verdict |
|---|---:|---:|---:|---:|---|
| P0 e2r_2_1_stock_web_calibrated_proxy | 3 | 14.44 | -12.20 | 1 | too broad for regional bank beta |
| P0b e2r_2_0_baseline_reference | 3 | 14.44 | -12.20 | 1 | misses capital-return acceleration nuance |
| P1 sector_specific_candidate_profile | 3 | 14.44 | -12.20 | 1 | no global change |
| P2 C21_capital_return_execution_shadow | 3 | 14.44 | -12.20 | 0~1 | better separates DGB false positive |
| P3 counterexample_guard_profile | 3 | 14.44 | -12.20 | 0 | strongest but source repair required |

## 20. Score-Return Alignment Matrix

| symbol | weighted_before | stage_before | weighted_after | stage_after | score-return alignment |
|---:|---:|---|---:|---|---|
| 024110 | 76 | Stage2-Actionable | 78 | Stage2-Actionable | aligned |
| 175330 | 77 | Stage2-Actionable | 74 | Stage2-RiskWatch | improved; high-MAE guard |
| 139130 | 72 | Stage2-Actionable | 64 | Stage2-Rejected/RiskWatch | improved; false-positive guard |

## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive_case_count | counterexample_count | 4B_case_count | 4C_case_count | new_independent_case_count | reused_case_count | calibration_usable_trigger_count | representative_trigger_count | current_profile_error_count | sector_rule_candidate | canonical_rule_candidate | coverage_gap_after_this_loop |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| L6_FINANCIAL_CAPITAL_RETURN_DIGITAL | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | REGIONAL_BANK_VALUEUP_CAPITAL_RETURN_EXECUTION_VS_CAPITAL_QUALITY_HIGH_MAE_BETA | 2 | 1 | 1 | 0 | 3 | 0 | 3 | 3 | 2 | no | yes | regional-bank high-MAE/capital-quality path still needs source repair |

## 22. Residual Contribution Summary

```text
new_independent_case_count: 3
reused_case_count: 0
reused_case_ids: null
new_symbol_count: 3
new_canonical_archetype_count: 0
new_fine_archetype_count: 1
new_trigger_family_count: 2
tested_existing_calibrated_axes:
  - stage2_actionable_evidence_bonus
  - price_only_blowoff_blocks_positive_stage
  - full_4b_requires_non_price_evidence
  - hard_4c_thesis_break_routes_to_4c
residual_error_types_found:
  - regional_bank_high_mae_after_valueup_beta
  - capital_return_bridge_missing
new_axis_proposed: null
existing_axis_strengthened:
  - C21_capital_return_execution_and_capital_buffer_bridge_required
existing_axis_weakened: null
existing_axis_kept:
  - full_4b_requires_non_price_evidence
  - hard_4c_thesis_break_routes_to_4c
sector_specific_rule_candidate: false
canonical_archetype_rule_candidate: true
no_new_signal_reason: null
loop_contribution_label: canonical_archetype_rule_candidate
do_not_propose_new_weight_delta: true
```

## 23. Validation Scope / Non-Validation Scope

Validated now:

```text
- Stock-Web tradable OHLC entry rows
- profile-level corporate-action candidate status
- MFE/MAE/peak/drawdown proxy calculations
- R6/L6/C21 schedule consistency
- No-Repeat top-covered avoidance
```

Not validated now:

```text
- exact primary source URLs for capital-return announcements
- CET1/capital-buffer data
- board-level dividend/buyback decisions
- analyst consensus revisions
- official payout ratio trajectory
```

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,C21_capital_return_execution_and_capital_buffer_bridge_required,canonical_archetype_specific,L6_FINANCIAL_CAPITAL_RETURN_DIGITAL,C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN,0,1,+1,"separates explicit capital-return execution from generic low-PBR value-up beta","reduces 139130 false positive while preserving 024110 and cautious 175330","C21-R6L83-IBK-20240226-S2A|C21-R6L83-JBFG-20240226-S2A|C21-R6L83-DGB-20240226-FP",3,3,1,low,canonical_shadow_only,"source_proxy_only; evidence_url_pending; not production"
```

## 25. Machine-Readable Rows

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration"}
{"row_type": "case", "case_id": "C21-R6L83-IBK-20240226", "symbol": "024110", "company_name": "기업은행", "round": "R6", "loop": 83, "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "fine_archetype_id": "REGIONAL_BANK_VALUEUP_CAPITAL_RETURN_EXECUTION_VS_CAPITAL_QUALITY_HIGH_MAE_BETA", "case_type": "state_bank_capital_return_positive", "positive_or_counterexample": "positive", "best_trigger": "C21-R6L83-IBK-20240226-S2A", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "controlled_positive_capital_return_path", "current_profile_verdict": "current_profile_correct", "price_source": "Songdaiki/stock-web", "notes": "source_proxy_only=true; evidence_url_pending=true; use as source-repair queue before runtime promotion"}
{"row_type": "trigger", "trigger_id": "C21-R6L83-IBK-20240226-S2A", "case_id": "C21-R6L83-IBK-20240226", "symbol": "024110", "company_name": "기업은행", "round": "R6", "loop": 83, "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "fine_archetype_id": "REGIONAL_BANK_VALUEUP_CAPITAL_RETURN_EXECUTION_VS_CAPITAL_QUALITY_HIGH_MAE_BETA", "sector": "financial_capital_return_digital", "primary_archetype": "financial_roe_pbr_capital_return", "loop_objective": ["coverage_gap_fill", "counterexample_mining", "4B_non_price_requirement_stress_test", "canonical_archetype_compression"], "trigger_type": "Stage2-Actionable", "trigger_date": "2024-02-26", "evidence_available_at_that_date": "state-bank value-up / dividend-yield / capital-return execution proxy", "evidence_source": "source_proxy_only; evidence_url_pending", "stage2_evidence_fields": ["value-up policy beta", "dividend/capital-return expectation", "state-bank PBR normalization"], "stage3_evidence_fields": ["capital buffer and shareholder-return execution still source-repair pending"], "stage4b_evidence_fields": ["post-peak drawdown after March bank basket peak"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/024/024110/2024.csv", "profile_path": "atlas/symbol_profiles/024/024110.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-02-26", "entry_price": 13400, "MFE_30D_pct": 19.48, "MFE_90D_pct": 19.48, "MFE_180D_pct": 19.48, "MFE_1Y_pct": 19.48, "MFE_2Y_pct": null, "MAE_30D_pct": -2.01, "MAE_90D_pct": -6.64, "MAE_180D_pct": -6.64, "MAE_1Y_pct": -6.64, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-03-15", "peak_price": 16010, "drawdown_after_peak_pct": -20.11, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.8, "four_b_full_window_peak_proximity": 0.8, "four_b_timing_verdict": "local_4B_watch_not_full_4B_without_non_price_evidence", "four_b_evidence_type": ["revision_slowdown", "capital_quality_high_mae"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "controlled_positive_capital_return_path", "current_profile_verdict": "current_profile_correct", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "C21-R6L83-IBK-20240226", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "C21-R6L83-IBK-20240226", "trigger_id": "C21-R6L83-IBK-20240226-S2A", "symbol": "024110", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 8, "customer_quality_score": 0, "policy_or_regulatory_score": 15, "valuation_repricing_score": 14, "execution_risk_score": 4, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "roe_pbr_capital_return_score": 17, "capital_buffer_quality_score": 11, "shareholder_return_execution_score": 11, "high_mae_risk_score": -4}, "weighted_score_before": 76, "stage_label_before": "Stage2-Actionable", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 8, "customer_quality_score": 0, "policy_or_regulatory_score": 15, "valuation_repricing_score": 14, "execution_risk_score": 4, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "roe_pbr_capital_return_score": 17, "capital_buffer_quality_score": 11, "shareholder_return_execution_score": 13, "high_mae_risk_score": -4}, "weighted_score_after": 78, "stage_label_after": "Stage2-Actionable", "changed_components": ["roe_pbr_capital_return_score", "capital_buffer_quality_score", "shareholder_return_execution_score", "high_mae_risk_score"], "component_delta_explanation": "C21-specific shadow profile separates generic value-up/PBR beta from explicit capital-return execution and capital-buffer quality; high-MAE regional-bank path is lowered to RiskWatch.", "MFE_90D_pct": 19.48, "MAE_90D_pct": -6.64, "score_return_alignment_label": "controlled_positive_capital_return_path", "current_profile_verdict": "current_profile_correct"}
{"row_type": "case", "case_id": "C21-R6L83-JBFG-20240226", "symbol": "175330", "company_name": "JB금융지주", "round": "R6", "loop": 83, "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "fine_archetype_id": "REGIONAL_BANK_VALUEUP_CAPITAL_RETURN_EXECUTION_VS_CAPITAL_QUALITY_HIGH_MAE_BETA", "case_type": "regional_bank_capital_return_high_mfe_positive", "positive_or_counterexample": "positive", "best_trigger": "C21-R6L83-JBFG-20240226-S2A", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "positive_but_high_mae_regional_bank_path", "current_profile_verdict": "current_profile_too_early", "price_source": "Songdaiki/stock-web", "notes": "source_proxy_only=true; evidence_url_pending=true; use as source-repair queue before runtime promotion"}
{"row_type": "trigger", "trigger_id": "C21-R6L83-JBFG-20240226-S2A", "case_id": "C21-R6L83-JBFG-20240226", "symbol": "175330", "company_name": "JB금융지주", "round": "R6", "loop": 83, "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "fine_archetype_id": "REGIONAL_BANK_VALUEUP_CAPITAL_RETURN_EXECUTION_VS_CAPITAL_QUALITY_HIGH_MAE_BETA", "sector": "financial_capital_return_digital", "primary_archetype": "financial_roe_pbr_capital_return", "loop_objective": ["coverage_gap_fill", "counterexample_mining", "4B_non_price_requirement_stress_test", "canonical_archetype_compression"], "trigger_type": "Stage2-Actionable", "trigger_date": "2024-02-26", "evidence_available_at_that_date": "regional-bank value-up / buyback-dividend route / ROE-PBR rerating proxy", "evidence_source": "source_proxy_only; evidence_url_pending", "stage2_evidence_fields": ["regional-bank value-up", "capital-return expectation", "ROE/PBR normalization"], "stage3_evidence_fields": ["capital quality and MAE absorption not fully verified at trigger"], "stage4b_evidence_fields": ["high-MFE local peak followed by near-20% drawdown"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/175/175330/2024.csv", "profile_path": "atlas/symbol_profiles/175/175330.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-02-26", "entry_price": 13360, "MFE_30D_pct": 5.54, "MFE_90D_pct": 20.88, "MFE_180D_pct": 20.88, "MFE_1Y_pct": 20.88, "MFE_2Y_pct": null, "MAE_30D_pct": -8.61, "MAE_90D_pct": -14.75, "MAE_180D_pct": -14.75, "MAE_1Y_pct": -14.75, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-07-05", "peak_price": 16150, "drawdown_after_peak_pct": -19.63, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.8, "four_b_full_window_peak_proximity": 0.8, "four_b_timing_verdict": "local_4B_watch_not_full_4B_without_non_price_evidence", "four_b_evidence_type": ["revision_slowdown", "capital_quality_high_mae"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "positive_but_high_mae_regional_bank_path", "current_profile_verdict": "current_profile_too_early", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "C21-R6L83-JBFG-20240226", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "C21-R6L83-JBFG-20240226", "trigger_id": "C21-R6L83-JBFG-20240226-S2A", "symbol": "175330", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 10, "customer_quality_score": 0, "policy_or_regulatory_score": 14, "valuation_repricing_score": 15, "execution_risk_score": 5, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "roe_pbr_capital_return_score": 16, "capital_buffer_quality_score": 8, "shareholder_return_execution_score": 10, "high_mae_risk_score": -1}, "weighted_score_before": 77, "stage_label_before": "Stage2-Actionable", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 10, "customer_quality_score": 0, "policy_or_regulatory_score": 14, "valuation_repricing_score": 15, "execution_risk_score": 5, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "roe_pbr_capital_return_score": 16, "capital_buffer_quality_score": 6, "shareholder_return_execution_score": 10, "high_mae_risk_score": -6}, "weighted_score_after": 74, "stage_label_after": "Stage2-RiskWatch", "changed_components": ["roe_pbr_capital_return_score", "capital_buffer_quality_score", "shareholder_return_execution_score", "high_mae_risk_score"], "component_delta_explanation": "C21-specific shadow profile separates generic value-up/PBR beta from explicit capital-return execution and capital-buffer quality; high-MAE regional-bank path is lowered to RiskWatch.", "MFE_90D_pct": 20.88, "MAE_90D_pct": -14.75, "score_return_alignment_label": "positive_but_high_mae_regional_bank_path", "current_profile_verdict": "current_profile_too_early"}
{"row_type": "case", "case_id": "C21-R6L83-DGB-20240226", "symbol": "139130", "company_name": "DGB금융지주/iM금융지주", "round": "R6", "loop": 83, "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "fine_archetype_id": "REGIONAL_BANK_VALUEUP_CAPITAL_RETURN_EXECUTION_VS_CAPITAL_QUALITY_HIGH_MAE_BETA", "case_type": "regional_bank_valueup_false_positive", "positive_or_counterexample": "counterexample", "best_trigger": "C21-R6L83-DGB-20240226-FP", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "capital_quality_high_mae_false_positive", "current_profile_verdict": "current_profile_false_positive", "price_source": "Songdaiki/stock-web", "notes": "source_proxy_only=true; evidence_url_pending=true; use as source-repair queue before runtime promotion"}
{"row_type": "trigger", "trigger_id": "C21-R6L83-DGB-20240226-FP", "case_id": "C21-R6L83-DGB-20240226", "symbol": "139130", "company_name": "DGB금융지주/iM금융지주", "round": "R6", "loop": 83, "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "fine_archetype_id": "REGIONAL_BANK_VALUEUP_CAPITAL_RETURN_EXECUTION_VS_CAPITAL_QUALITY_HIGH_MAE_BETA", "sector": "financial_capital_return_digital", "primary_archetype": "financial_roe_pbr_capital_return", "loop_objective": ["coverage_gap_fill", "counterexample_mining", "4B_non_price_requirement_stress_test", "canonical_archetype_compression"], "trigger_type": "Stage2-FalsePositive", "trigger_date": "2024-02-26", "evidence_available_at_that_date": "regional-bank policy beta without repaired capital-quality / return-execution bridge", "evidence_source": "source_proxy_only; evidence_url_pending", "stage2_evidence_fields": ["value-up policy beta", "low-PBR regional-bank rerating narrative"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["capital-quality / high-MAE local 4B watch"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/139/139130/2024.csv", "profile_path": "atlas/symbol_profiles/139/139130.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-02-26", "entry_price": 9140, "MFE_30D_pct": 2.95, "MFE_90D_pct": 2.95, "MFE_180D_pct": 2.95, "MFE_1Y_pct": 2.95, "MFE_2Y_pct": null, "MAE_30D_pct": -8.1, "MAE_90D_pct": -15.21, "MAE_180D_pct": -18.6, "MAE_1Y_pct": -18.6, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-03-15", "peak_price": 9410, "drawdown_after_peak_pct": -20.93, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.95, "four_b_full_window_peak_proximity": 0.95, "four_b_timing_verdict": "local_4B_watch_not_full_4B_without_non_price_evidence", "four_b_evidence_type": ["revision_slowdown", "capital_quality_high_mae"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "capital_quality_high_mae_false_positive", "current_profile_verdict": "current_profile_false_positive", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "C21-R6L83-DGB-20240226", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "C21-R6L83-DGB-20240226", "trigger_id": "C21-R6L83-DGB-20240226-FP", "symbol": "139130", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 5, "customer_quality_score": 0, "policy_or_regulatory_score": 14, "valuation_repricing_score": 15, "execution_risk_score": 8, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "roe_pbr_capital_return_score": 12, "capital_buffer_quality_score": 4, "shareholder_return_execution_score": 6, "high_mae_risk_score": 0}, "weighted_score_before": 72, "stage_label_before": "Stage2-Actionable", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 5, "customer_quality_score": 0, "policy_or_regulatory_score": 14, "valuation_repricing_score": 15, "execution_risk_score": 8, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "roe_pbr_capital_return_score": 12, "capital_buffer_quality_score": 1, "shareholder_return_execution_score": 4, "high_mae_risk_score": -8}, "weighted_score_after": 64, "stage_label_after": "Stage2-Rejected/RiskWatch", "changed_components": ["roe_pbr_capital_return_score", "capital_buffer_quality_score", "shareholder_return_execution_score", "high_mae_risk_score"], "component_delta_explanation": "C21-specific shadow profile separates generic value-up/PBR beta from explicit capital-return execution and capital-buffer quality; high-MAE regional-bank path is lowered to RiskWatch.", "MFE_90D_pct": 2.95, "MAE_90D_pct": -15.21, "score_return_alignment_label": "capital_quality_high_mae_false_positive", "current_profile_verdict": "current_profile_false_positive"}
{"row_type": "residual_contribution", "round": "R6", "loop": 83, "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "new_independent_case_count": 3, "reused_case_count": 0, "new_symbol_count": 3, "new_trigger_family_count": 2, "tested_existing_calibrated_axes": ["stage2_actionable_evidence_bonus", "price_only_blowoff_blocks_positive_stage", "full_4b_requires_non_price_evidence", "hard_4c_thesis_break_routes_to_4c"], "residual_error_types_found": ["regional_bank_high_mae_after_valueup_beta", "capital_return_bridge_missing"], "loop_contribution_label": "canonical_archetype_rule_candidate", "do_not_propose_new_weight_delta": true}
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
- Do not treat schema_rematerialization_only or duplicate_low_value_loop as calibration evidence.
- Do not promote source_proxy_only/evidence_url_pending rows without source repair.
- Preserve full_4b_requires_non_price_evidence and hard_4c_thesis_break_routes_to_4c.
- For this file, validate C21 capital-return execution, CET1/capital-buffer quality, buyback/dividend source URLs, and payout repeatability before any runtime effect.

## 27. Next Round State

```text
completed_round = R6
completed_loop = 83
next_round = R7
next_loop = 83
round_schedule_status = valid
round_sector_consistency = pass
```

## 28. Source Notes

```text
MAIN_EXECUTION_PROMPT = docs/core/e2r_v12_prompt_round_scheduler_corrected.txt
NO_REPEAT_INDEX = docs/core/V12_Research_No_Repeat_Index.md
price_source = Songdaiki/stock-web
stock_web_manifest_max_date = 2026-02-20
production_scoring_changed = false
shadow_weight_only = true
```
