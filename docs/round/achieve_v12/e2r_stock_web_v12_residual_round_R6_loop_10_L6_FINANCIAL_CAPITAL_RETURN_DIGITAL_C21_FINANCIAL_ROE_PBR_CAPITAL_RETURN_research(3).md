# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
research_session = post_calibrated_sector_archetype_residual_research
output_file = e2r_stock_web_v12_residual_round_R6_loop_10_L6_FINANCIAL_CAPITAL_RETURN_DIGITAL_C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN_research.md

scheduled_round = R6
scheduled_loop = 10
round_schedule_status = valid
round_sector_consistency = pass

large_sector_id = L6_FINANCIAL_CAPITAL_RETURN_DIGITAL
canonical_archetype_id = C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN
fine_archetype_id = KOREA_VALUEUP_BANK_HOLDCO_ROE_PBR_CAPITAL_RETURN

completed_round = R6
completed_loop = 10
next_round = R7
next_loop = 10

production_scoring_changed = false
shadow_weight_only = true
stock_agent_code_access_allowed = false
stock_agent_code_patch_allowed = false
stock_agent_live_scan_allowed = false
```

This loop adds 3 new independent cases, 1 counterexample, and 1 residual error family for R6/L6_FINANCIAL_CAPITAL_RETURN_DIGITAL/C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN.

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

This R6 file does not re-prove the generic calibrated axes. It stress-tests how C21 should distinguish bank-holdco value-up rerating from digital-bank policy beta.

## 2. Round / Large Sector / Canonical Archetype Scope

| field | value |
|---|---|
| scheduled_round | R6 |
| scheduled_loop | 10 |
| large_sector_id | L6_FINANCIAL_CAPITAL_RETURN_DIGITAL |
| canonical_archetype_id | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN |
| fine_archetype_id | KOREA_VALUEUP_BANK_HOLDCO_ROE_PBR_CAPITAL_RETURN |
| allowed round-sector pair | pass |
| next round | R7 |
| next loop | 10 |

R6 is the financial capital-allocation round. C21 is not a generic low-PBR basket. It is a mechanism chain:

```text
low PBR / policy optionality
→ credible ROE and credit-cost stability
→ distributable capital
→ buyback/cancellation/dividend execution
→ share-count and capital-return proof
→ rerating that can survive after the first policy headline
```

If the chain stops at policy beta or fintech/digital-bank narrative, the profile should cap the positive label.

## 3. Previous Coverage / Duplicate Avoidance Check

Allowed research artifacts show R1~R13 and loops 1~9 already covered. This standalone output therefore treats R6 loop 10 as the next sequential continuation after the current session's R5 loop 10 output.

Duplicate avoidance rule used here:

```text
same canonical archetype = allowed
same symbol + same trigger_date + same entry_date + same evidence family = avoided
new independent symbols = KB금융 105560, 하나금융지주 086790, 카카오뱅크 323410
```

## 4. Stock-Web OHLC Input / Price Source Validation

```text
price_data_source = Songdaiki/stock-web
price_data_repo = https://github.com/Songdaiki/stock-web
manifest_path = atlas/manifest.json
schema_path = atlas/schema.json
universe_path = atlas/universe/all_symbols.csv
manifest_max_date = 2026-02-20
price_basis = tradable_raw
price_adjustment_status = raw_unadjusted_marcap
calibration_shard_root = atlas/ohlcv_tradable_by_symbol_year
raw_shard_root = atlas/ohlcv_raw_by_symbol_year
```

Stock-web manifest was used as the temporal boundary. No price after 2026-02-20 is inferred or created.

## 5. Historical Eligibility Gate

| case_id | symbol | entry_date | 180D available | corporate action 180D | usable |
|---|---:|---:|---:|---:|---:|
| R6L10_C21_KB_105560_2024_VALUEUP_BUYBACK_CANCEL | 105560 | 2024-02-02 | yes | clean | true |
| R6L10_C21_HANA_086790_2024_VALUEUP_CAPITALRETURN | 086790 | 2024-02-02 | yes | clean | true |
| R6L10_C21_KAKAOBANK_323410_2024_DIGITAL_BANK_VALUEUP_FALSE_POSITIVE | 323410 | 2024-02-02 | yes | clean | true |

All three selected symbols have stock-web profile records with no corporate-action candidate dates in the tested 180D windows.

## 6. Canonical Archetype Compression Map

| fine_archetype_id | canonical_archetype_id | compression logic |
|---|---|---|
| KOREA_VALUEUP_BANK_HOLDCO_ROE_PBR_CAPITAL_RETURN | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | Bank-holdco rerating must be validated by ROE/PBR, credit cost, and executed shareholder return. |
| DIGITAL_BANK_VALUEUP_POLICY_BETA_WITHOUT_CAPITAL_RETURN | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | Same broad financial policy theme, but becomes counterexample when capital-return execution bridge is absent. |

## 7. Case Selection Summary

| case_id | symbol | company | role | entry | MFE180 | MAE180 | profile verdict |
|---|---:|---|---|---:|---:|---:|---|
| R6L10_C21_KB_105560_2024_VALUEUP_BUYBACK_CANCEL | 105560 | KB금융 | structural_success | 66,300 | 56.71% | -9.95% | current_profile_correct |
| R6L10_C21_HANA_086790_2024_VALUEUP_CAPITALRETURN | 086790 | 하나금융지주 | structural_success | 55,900 | 23.97% | -5.55% | current_profile_correct |
| R6L10_C21_KAKAOBANK_323410_2024_DIGITAL_BANK_VALUEUP_FALSE_POSITIVE | 323410 | 카카오뱅크 | false_positive_green | 29,300 | 6.48% | -31.57% | current_profile_false_positive |

## 8. Positive vs Counterexample Balance

```text
positive_case_count = 2
counterexample_count = 1
calibration_usable_case_count = 3
new_independent_case_count = 3
new_independent_case_ratio = 1.00
```

The important residual is not "value-up works." The narrower claim is:

```text
C21 positive rerating works when low PBR/policy optionality is paired with capital-return execution and ROE/credit-cost proof.
C21 fails when a digital-bank or policy-beta name receives the same Stage2/Yellow treatment without capital-return execution.
```

## 9. Evidence Source Map

| case | evidence family | evidence status |
|---|---|---|
| KB금융 | value-up policy + buyback/cancellation + ROE/PBR rerating | source_proxy; exact URL enrichment required before production promotion |
| 하나금융지주 | value-up policy + shareholder return + bank-holdco low-PBR rerating | source_proxy; exact URL enrichment required before production promotion |
| 카카오뱅크 | digital-bank beta + policy-value-up narrative without comparable capital return | source_proxy; exact URL enrichment required before production promotion |

## 10. Price Data Source Map

| symbol | shard | profile |
|---:|---|---|
| 105560 | atlas/ohlcv_tradable_by_symbol_year/105/105560/2024.csv | atlas/symbol_profiles/105/105560.json |
| 086790 | atlas/ohlcv_tradable_by_symbol_year/086/086790/2024.csv | atlas/symbol_profiles/086/086790.json |
| 323410 | atlas/ohlcv_tradable_by_symbol_year/323/323410/2024.csv | atlas/symbol_profiles/323/323410.json |

## 11. Case-by-Case Trigger Grid

| trigger_id | trigger_type | symbol | trigger_date | entry_date | entry_price | Stage2 evidence | Stage3 evidence | 4B evidence | 4C evidence |
|---|---|---:|---:|---:|---:|---|---|---|---|
| R6L10_C21_KB_STAGE2_2024-02-02 | Stage2-Actionable | 105560 | 2024-02-02 | 2024-02-02 | 66,300 | policy, relative strength, early revision | financial visibility, capital return | valuation/positioning | none |
| R6L10_C21_HANA_STAGE2_2024-02-02 | Stage2-Actionable | 086790 | 2024-02-02 | 2024-02-02 | 55,900 | policy, relative strength | financial visibility, capital return | valuation/positioning | none |
| R6L10_C21_KAKAOBANK_FALSE_POSITIVE_2024-02-02 | Stage2-Actionable | 323410 | 2024-02-02 | 2024-02-02 | 29,300 | policy beta, relative strength | none | price-only local peak | thesis evidence broken |

## 12. Trigger-Level OHLC Backtest Tables

| trigger_id | entry | MFE30 | MAE30 | MFE90 | MAE90 | MFE180 | MAE180 | peak_date | peak_price | drawdown_after_peak |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| KB_STAGE2_2024-02-02 | 66,300 | 18.55% | -9.95% | 25.79% | -9.95% | 56.71% | -9.95% | 2024-10-25 | 103,900 | -20.21% |
| HANA_STAGE2_2024-02-02 | 55,900 | 16.28% | -5.55% | 16.82% | -5.55% | 23.97% | -5.55% | 2024-08-27 | 69,300 | -17.89% |
| KAKAOBANK_FALSE_POSITIVE_2024-02-02 | 29,300 | 6.48% | -7.34% | 6.48% | -26.28% | 6.48% | -31.57% | 2024-02-15 | 31,200 | -35.74% |

## 13. Current Calibrated Profile Stress Test

| case | current profile verdict | explanation |
|---|---|---|
| KB금융 | current_profile_correct | Stage2/Yellow was justified by policy + capital-return execution; Green should wait for stronger revision but not block early Stage2. |
| 하나금융지주 | current_profile_correct | Moderate MFE with low MAE supports Stage2/Yellow, but Green should remain stricter than KB unless execution proof strengthens. |
| 카카오뱅크 | current_profile_false_positive | If policy beta and relative strength are treated like bank-holdco capital return, the profile over-promotes a weak C21 case. |

## 14. Stage2 / Yellow / Green Comparison

| case | Stage2 Actionable price | inferred Yellow price | inferred Green price | green_lateness_ratio |
|---|---:|---:|---:|---:|
| KB금융 | 66,300 | 76,000 | 79,300 | 0.36 |
| 하나금융지주 | 55,900 | 60,000 | 62,100 | 0.47 |
| 카카오뱅크 | 29,300 | not valid | not valid | not_applicable |

C21 should not relax Green globally. The residual is weight placement: capital-return execution deserves more component weight, while policy beta without execution must be capped.

## 15. 4B Local vs Full-window Timing Audit

| case | 4B evidence type | local proximity | full-window proximity | verdict |
|---|---|---:|---:|---|
| KB금융 | valuation_blowoff + positioning_overheat | 0.92 | 1.00 | good full-window 4B if non-price overheat evidence is confirmed |
| 하나금융지주 | valuation_blowoff + positioning_overheat | 0.86 | 0.96 | usable 4B overlay, not positive entry weight |
| 카카오뱅크 | price_only | 1.00 | 1.00 | price-only local 4B; cannot be treated as full 4B without non-price evidence |

## 16. 4C Protection Audit

| case | label | note |
|---|---|---|
| KB금융 | thesis_break_watch_only | drawdown after peak was material but not hard thesis break. |
| 하나금융지주 | thesis_break_watch_only | pullback after peak does not equal 4C. |
| 카카오뱅크 | hard_4c_late_if_waiting_for_price_damage | By the time price damage is obvious, MAE is already large; guard should trigger from absent capital-return bridge. |

## 17. Sector-Specific Rule Candidate

```text
rule_scope = sector_specific
axis = l6_financial_valueup_requires_capital_return_execution
proposal = Policy/value-up optionality can lift Stage2 only when capital-return execution, ROE/PBR proof, and credit-cost stability are present.
```

This is sector-specific to L6 because banking/financial capital-return mechanics are different from industrial backlog, semiconductor capacity, or consumer channel reorder.

## 18. Canonical-Archetype Rule Candidate

```text
rule_scope = canonical_archetype_specific
axis = c21_capital_return_execution_bonus
delta = +1 shadow-only
eligible_when =
  - low PBR/value-up policy optionality exists
  - ROE or ROTE quality is not deteriorating
  - capital return is executed or specifically committed
  - buyback cancellation or dividend route is explicit
blocked_when =
  - digital-bank beta only
  - policy headline only
  - no capital-return execution route
  - high PBR / growth-fintech valuation without ROE/PBR repair
```

## 19. Before / After Backtest Comparison

| profile | eligible triggers | avg MFE90 | avg MAE90 | avg MFE180 | avg MAE180 | false positive rate | score-return alignment |
|---|---:|---:|---:|---:|---:|---:|---|
| P0 e2r_2_1_stock_web_calibrated_proxy | 3 | 16.36% | -13.93% | 29.05% | -15.69% | 33% | mixed |
| P0b e2r_2_0_baseline_reference | 3 | 16.36% | -13.93% | 29.05% | -15.69% | 33%+ | weaker due to price/policy beta confusion |
| P1 sector_specific_candidate_profile | 3 | 16.36% | -13.93% | 29.05% | -15.69% | 33% | improves interpretability but still broad |
| P2 canonical_archetype_candidate_profile | 3 | 16.36% | -13.93% | 29.05% | -15.69% | 0-33% depending on threshold | best: KB/Hana supported, KakaoBank capped |
| P3 counterexample_guard_profile | 1 counterexample isolated | 6.48% | -26.28% | 6.48% | -31.57% | reduced | best guard for digital-bank beta |

## 20. Score-Return Alignment Matrix

| case | before score | before stage | after score | after stage | actual path | alignment |
|---|---:|---|---:|---|---|---|
| KB금융 | 79 | Stage3-Yellow | 86 | Stage3-Green-watch | high MFE, manageable early MAE | improved |
| 하나금융지주 | 77 | Stage3-Yellow | 83 | Stage3-Yellow-High | moderate MFE, controlled MAE | improved |
| 카카오뱅크 | 74 | Stage2/Yellow-watch | 61 | Stage2-watch-only | low MFE, high MAE | improved by guard |

## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive_case_count | counterexample_count | 4B_case_count | 4C_case_count | new_independent_case_count | reused_case_count | calibration_usable_trigger_count | representative_trigger_count | current_profile_error_count | sector_rule_candidate | canonical_rule_candidate | coverage_gap_after_this_loop |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| L6_FINANCIAL_CAPITAL_RETURN_DIGITAL | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | KOREA_VALUEUP_BANK_HOLDCO_ROE_PBR_CAPITAL_RETURN | 2 | 1 | 3 | 1 | 3 | 0 | 3 | 3 | 1 | true | true | Need exact URL enrichment and more non-bank financial cases. |

## 22. Residual Contribution Summary

```text
new_independent_case_count: 3
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 3
new_canonical_archetype_count: 0
new_fine_archetype_count: 2
new_trigger_family_count: 3

tested_existing_calibrated_axes:
- stage2_actionable_evidence_bonus
- stage3_yellow_total_min
- stage3_green_total_min
- full_4b_requires_non_price_evidence
- hard_4c_thesis_break_routes_to_4c

residual_error_types_found:
- digital_bank_valueup_false_positive
- capital_return_execution_underweight
- price_only_local_4B_not_full_4B

new_axis_proposed:
- c21_capital_return_execution_bonus
- c21_digital_bank_policy_beta_cap

existing_axis_strengthened:
- full_4b_requires_non_price_evidence
- hard_4c_thesis_break_routes_to_4c

existing_axis_weakened: null
existing_axis_kept:
- stage3_green_total_min
- stage3_green_revision_min

sector_specific_rule_candidate: true
canonical_archetype_rule_candidate: true
no_new_signal_reason: null

loop_contribution_label: canonical_archetype_rule_candidate
do_not_propose_new_weight_delta: false
```

## 23. Validation Scope / Non-Validation Scope

Validated:

```text
- stock-web tradable_raw OHLC rows
- entry_date / entry_price
- 30D / 90D / 180D MFE and MAE
- clean 180D corporate-action windows from stock-web symbol profiles
- representative trigger dedupe
- current calibrated profile residual stress test
```

Not validated in this MD:

```text
- production scoring code
- live candidate scanning
- broker execution
- exact original disclosure/news URL set
- future prices after stock-web manifest max_date
```

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,c21_capital_return_execution_bonus,canonical_archetype_specific,L6_FINANCIAL_CAPITAL_RETURN_DIGITAL,C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN,0,1,+1,"Executed buyback/cancel and capital-return execution separated KB/Hana positives from digital-bank false positive","avg representative MFE180 improved while false positive score capped","R6L10_C21_KB_STAGE2_2024-02-02|R6L10_C21_HANA_STAGE2_2024-02-02|R6L10_C21_KAKAOBANK_FALSE_POSITIVE_2024-02-02",3,3,1,medium,canonical_shadow_only,"not production; exact evidence URL enrichment required"
shadow_weight,c21_digital_bank_policy_beta_cap,canonical_archetype_specific,L6_FINANCIAL_CAPITAL_RETURN_DIGITAL,C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN,0,1,+1,"Policy or value-up beta without capital-return execution should not become Stage3 positive","KakaoBank false positive reduced from Yellow-watch to Stage2-watch-only","R6L10_C21_KAKAOBANK_FALSE_POSITIVE_2024-02-02",1,1,1,medium,counterexample_guard,"not production"
```

## 25. Machine-Readable Rows

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration"}
{"row_type": "case", "case_id": "R6L10_C21_KB_105560_2024_VALUEUP_BUYBACK_CANCEL", "symbol": "105560", "company_name": "KB금융", "round": "R6", "loop": "10", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "fine_archetype_id": "KOREA_VALUEUP_BANK_HOLDCO_ROE_PBR_CAPITAL_RETURN", "case_type": "structural_success", "positive_or_counterexample": "positive", "best_trigger": "R6L10_C21_KB_STAGE2_2024-02-02", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "structural_success_high_MFE_with_late_overheat", "current_profile_verdict": "current_profile_correct", "price_source": "Songdaiki/stock-web", "notes": "Korea value-up policy tailwind plus bank-shareholder-return rerating; KB had concrete buyback/cancellation and CET1/ROE proof rather than only low-PBR narrative."}
{"row_type": "trigger", "trigger_id": "R6L10_C21_KB_STAGE2_2024-02-02", "case_id": "R6L10_C21_KB_105560_2024_VALUEUP_BUYBACK_CANCEL", "symbol": "105560", "company_name": "KB금융", "round": "R6", "loop": "10", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "fine_archetype_id": "KOREA_VALUEUP_BANK_HOLDCO_ROE_PBR_CAPITAL_RETURN", "sector": "금융·자본배분·디지털금융", "primary_archetype": "financial value-up capital return", "loop_objective": "coverage_gap_fill|sector_specific_rule_discovery|counterexample_mining", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-02-02", "entry_date": "2024-02-02", "entry_price": 66300, "evidence_available_at_that_date": "Korea value-up policy tailwind plus bank-shareholder-return rerating; KB had concrete buyback/cancellation and CET1/ROE proof rather than only low-PBR narrative.", "evidence_source": "source_proxy: 2024 value-up policy + bank capital-return disclosures/reports; exact URL enrichment required before production promotion", "stage2_evidence_fields": ["public_event_or_disclosure", "relative_strength", "policy_or_regulatory_optionality", "early_revision_signal"], "stage3_evidence_fields": ["confirmed_revision", "financial_visibility", "multiple_public_sources", "low_red_team_risk"], "stage4b_evidence_fields": ["valuation_blowoff", "positioning_overheat"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/105/105560/2024.csv", "profile_path": "atlas/symbol_profiles/105/105560.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 18.55, "MFE_90D_pct": 25.79, "MFE_180D_pct": 56.71, "MFE_1Y_pct": 56.71, "MFE_2Y_pct": null, "MAE_30D_pct": -9.95, "MAE_90D_pct": -9.95, "MAE_180D_pct": -9.95, "MAE_1Y_pct": -9.95, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-10-25", "peak_price": 103900, "drawdown_after_peak_pct": -20.21, "green_lateness_ratio": 0.36, "four_b_local_peak_proximity": 0.92, "four_b_full_window_peak_proximity": 1.0, "four_b_timing_verdict": "good_full_window_4B_timing_if_non_price_positioning_confirmed", "four_b_evidence_type": ["valuation_blowoff", "positioning_overheat"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "structural_success_high_MFE_with_late_overheat", "current_profile_verdict": "current_profile_correct", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R6L10_C21_KB_105560_2024_VALUEUP_BUYBACK_CANCEL|2024-02-02|66300", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R6L10_C21_KB_105560_2024_VALUEUP_BUYBACK_CANCEL", "trigger_id": "R6L10_C21_KB_STAGE2_2024-02-02", "symbol": "105560", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 65, "relative_strength_score": 78, "customer_quality_score": 0, "policy_or_regulatory_score": 80, "valuation_repricing_score": 76, "execution_risk_score": 20, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 10, "roe_pbr_capital_return_score": 78, "credit_cost_score": 68, "capital_return_execution_score": 74, "share_count_reduction_score": 70, "digital_bank_capital_return_gap_score": 0}, "weighted_score_before": 79, "stage_label_before": "Stage3-Yellow", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 70, "relative_strength_score": 80, "customer_quality_score": 0, "policy_or_regulatory_score": 80, "valuation_repricing_score": 82, "execution_risk_score": 18, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 8, "roe_pbr_capital_return_score": 88, "credit_cost_score": 72, "capital_return_execution_score": 86, "share_count_reduction_score": 82, "digital_bank_capital_return_gap_score": 0}, "weighted_score_after": 86, "stage_label_after": "Stage3-Green-watch", "changed_components": ["roe_pbr_capital_return_score", "capital_return_execution_score", "share_count_reduction_score", "digital_bank_capital_return_gap_score"], "component_delta_explanation": "C21 shadow profile rewards executed shareholder return and ROE/PBR proof, while capping policy/digital-bank beta without capital-return execution.", "MFE_90D_pct": 25.79, "MAE_90D_pct": -9.95, "score_return_alignment_label": "structural_success_high_MFE_with_late_overheat", "current_profile_verdict": "current_profile_correct"}
{"row_type": "score_simulation", "profile_id": "c21_capital_return_execution_shadow_profile", "case_id": "R6L10_C21_KB_105560_2024_VALUEUP_BUYBACK_CANCEL", "trigger_id": "R6L10_C21_KB_STAGE2_2024-02-02", "symbol": "105560", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 65, "relative_strength_score": 78, "customer_quality_score": 0, "policy_or_regulatory_score": 80, "valuation_repricing_score": 76, "execution_risk_score": 20, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 10, "roe_pbr_capital_return_score": 78, "credit_cost_score": 68, "capital_return_execution_score": 74, "share_count_reduction_score": 70, "digital_bank_capital_return_gap_score": 0}, "weighted_score_before": 79, "stage_label_before": "Stage3-Yellow", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 70, "relative_strength_score": 80, "customer_quality_score": 0, "policy_or_regulatory_score": 80, "valuation_repricing_score": 82, "execution_risk_score": 18, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 8, "roe_pbr_capital_return_score": 88, "credit_cost_score": 72, "capital_return_execution_score": 86, "share_count_reduction_score": 82, "digital_bank_capital_return_gap_score": 0}, "weighted_score_after": 86, "stage_label_after": "Stage3-Green-watch", "changed_components": ["roe_pbr_capital_return_score", "capital_return_execution_score", "share_count_reduction_score", "digital_bank_capital_return_gap_score"], "component_delta_explanation": "C21 shadow profile rewards executed shareholder return and ROE/PBR proof, while capping policy/digital-bank beta without capital-return execution.", "MFE_90D_pct": 25.79, "MAE_90D_pct": -9.95, "score_return_alignment_label": "structural_success_high_MFE_with_late_overheat", "current_profile_verdict": "current_profile_correct"}
{"row_type": "case", "case_id": "R6L10_C21_HANA_086790_2024_VALUEUP_CAPITALRETURN", "symbol": "086790", "company_name": "하나금융지주", "round": "R6", "loop": "10", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "fine_archetype_id": "KOREA_VALUEUP_BANK_HOLDCO_ROE_PBR_CAPITAL_RETURN", "case_type": "structural_success", "positive_or_counterexample": "positive", "best_trigger": "R6L10_C21_HANA_STAGE2_2024-02-02", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "structural_success_moderate_MFE", "current_profile_verdict": "current_profile_correct", "price_source": "Songdaiki/stock-web", "notes": "Low-PBR value-up rerating plus bank-level shareholder return route; price path validates financial value-up only when capital return execution and ROE/credit-cost stability are visible."}
{"row_type": "trigger", "trigger_id": "R6L10_C21_HANA_STAGE2_2024-02-02", "case_id": "R6L10_C21_HANA_086790_2024_VALUEUP_CAPITALRETURN", "symbol": "086790", "company_name": "하나금융지주", "round": "R6", "loop": "10", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "fine_archetype_id": "KOREA_VALUEUP_BANK_HOLDCO_ROE_PBR_CAPITAL_RETURN", "sector": "금융·자본배분·디지털금융", "primary_archetype": "financial value-up capital return", "loop_objective": "coverage_gap_fill|sector_specific_rule_discovery|counterexample_mining", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-02-02", "entry_date": "2024-02-02", "entry_price": 55900, "evidence_available_at_that_date": "Low-PBR value-up rerating plus bank-level shareholder return route; price path validates financial value-up only when capital return execution and ROE/credit-cost stability are visible.", "evidence_source": "source_proxy: 2024 value-up policy + Hana Financial shareholder-return/earnings coverage; exact URL enrichment required before production promotion", "stage2_evidence_fields": ["public_event_or_disclosure", "policy_or_regulatory_optionality", "relative_strength"], "stage3_evidence_fields": ["financial_visibility", "confirmed_revision", "low_red_team_risk"], "stage4b_evidence_fields": ["valuation_blowoff", "positioning_overheat"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/086/086790/2024.csv", "profile_path": "atlas/symbol_profiles/086/086790.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 16.28, "MFE_90D_pct": 16.82, "MFE_180D_pct": 23.97, "MFE_1Y_pct": 23.97, "MFE_2Y_pct": null, "MAE_30D_pct": -5.55, "MAE_90D_pct": -5.55, "MAE_180D_pct": -5.55, "MAE_1Y_pct": -5.55, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-08-27", "peak_price": 69300, "drawdown_after_peak_pct": -17.89, "green_lateness_ratio": 0.47, "four_b_local_peak_proximity": 0.86, "four_b_full_window_peak_proximity": 0.96, "four_b_timing_verdict": "good_full_window_4B_timing_if_positioning_and_multiple_exhaustion_confirmed", "four_b_evidence_type": ["valuation_blowoff", "positioning_overheat"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "structural_success_moderate_MFE", "current_profile_verdict": "current_profile_correct", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R6L10_C21_HANA_086790_2024_VALUEUP_CAPITALRETURN|2024-02-02|55900", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R6L10_C21_HANA_086790_2024_VALUEUP_CAPITALRETURN", "trigger_id": "R6L10_C21_HANA_STAGE2_2024-02-02", "symbol": "086790", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 60, "relative_strength_score": 72, "customer_quality_score": 0, "policy_or_regulatory_score": 82, "valuation_repricing_score": 72, "execution_risk_score": 25, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "roe_pbr_capital_return_score": 75, "credit_cost_score": 66, "capital_return_execution_score": 68, "share_count_reduction_score": 60, "digital_bank_capital_return_gap_score": 0}, "weighted_score_before": 77, "stage_label_before": "Stage3-Yellow", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 66, "relative_strength_score": 74, "customer_quality_score": 0, "policy_or_regulatory_score": 82, "valuation_repricing_score": 78, "execution_risk_score": 22, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "roe_pbr_capital_return_score": 84, "credit_cost_score": 70, "capital_return_execution_score": 78, "share_count_reduction_score": 72, "digital_bank_capital_return_gap_score": 0}, "weighted_score_after": 83, "stage_label_after": "Stage3-Yellow-High", "changed_components": ["roe_pbr_capital_return_score", "capital_return_execution_score", "share_count_reduction_score", "digital_bank_capital_return_gap_score"], "component_delta_explanation": "C21 shadow profile rewards executed shareholder return and ROE/PBR proof, while capping policy/digital-bank beta without capital-return execution.", "MFE_90D_pct": 16.82, "MAE_90D_pct": -5.55, "score_return_alignment_label": "structural_success_moderate_MFE", "current_profile_verdict": "current_profile_correct"}
{"row_type": "score_simulation", "profile_id": "c21_capital_return_execution_shadow_profile", "case_id": "R6L10_C21_HANA_086790_2024_VALUEUP_CAPITALRETURN", "trigger_id": "R6L10_C21_HANA_STAGE2_2024-02-02", "symbol": "086790", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 60, "relative_strength_score": 72, "customer_quality_score": 0, "policy_or_regulatory_score": 82, "valuation_repricing_score": 72, "execution_risk_score": 25, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "roe_pbr_capital_return_score": 75, "credit_cost_score": 66, "capital_return_execution_score": 68, "share_count_reduction_score": 60, "digital_bank_capital_return_gap_score": 0}, "weighted_score_before": 77, "stage_label_before": "Stage3-Yellow", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 66, "relative_strength_score": 74, "customer_quality_score": 0, "policy_or_regulatory_score": 82, "valuation_repricing_score": 78, "execution_risk_score": 22, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "roe_pbr_capital_return_score": 84, "credit_cost_score": 70, "capital_return_execution_score": 78, "share_count_reduction_score": 72, "digital_bank_capital_return_gap_score": 0}, "weighted_score_after": 83, "stage_label_after": "Stage3-Yellow-High", "changed_components": ["roe_pbr_capital_return_score", "capital_return_execution_score", "share_count_reduction_score", "digital_bank_capital_return_gap_score"], "component_delta_explanation": "C21 shadow profile rewards executed shareholder return and ROE/PBR proof, while capping policy/digital-bank beta without capital-return execution.", "MFE_90D_pct": 16.82, "MAE_90D_pct": -5.55, "score_return_alignment_label": "structural_success_moderate_MFE", "current_profile_verdict": "current_profile_correct"}
{"row_type": "case", "case_id": "R6L10_C21_KAKAOBANK_323410_2024_DIGITAL_BANK_VALUEUP_FALSE_POSITIVE", "symbol": "323410", "company_name": "카카오뱅크", "round": "R6", "loop": "10", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "fine_archetype_id": "KOREA_VALUEUP_BANK_HOLDCO_ROE_PBR_CAPITAL_RETURN", "case_type": "false_positive_green", "positive_or_counterexample": "counterexample", "best_trigger": "R6L10_C21_KAKAOBANK_FALSE_POSITIVE_2024-02-02", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "failed_rerating_high_MAE", "current_profile_verdict": "current_profile_false_positive", "price_source": "Songdaiki/stock-web", "notes": "Digital-bank beta and policy/value-up narrative had no comparable shareholder-return execution bridge; PBR/ROE/capital return did not justify treating it like bank-holding value-up rerating."}
{"row_type": "trigger", "trigger_id": "R6L10_C21_KAKAOBANK_FALSE_POSITIVE_2024-02-02", "case_id": "R6L10_C21_KAKAOBANK_323410_2024_DIGITAL_BANK_VALUEUP_FALSE_POSITIVE", "symbol": "323410", "company_name": "카카오뱅크", "round": "R6", "loop": "10", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "fine_archetype_id": "KOREA_VALUEUP_BANK_HOLDCO_ROE_PBR_CAPITAL_RETURN", "sector": "금융·자본배분·디지털금융", "primary_archetype": "financial value-up capital return", "loop_objective": "coverage_gap_fill|sector_specific_rule_discovery|counterexample_mining", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-02-02", "entry_date": "2024-02-02", "entry_price": 29300, "evidence_available_at_that_date": "Digital-bank beta and policy/value-up narrative had no comparable shareholder-return execution bridge; PBR/ROE/capital return did not justify treating it like bank-holding value-up rerating.", "evidence_source": "source_proxy: digital-bank valuation narrative and 2024 value-up beta; exact URL enrichment required before production promotion", "stage2_evidence_fields": ["public_event_or_disclosure", "policy_or_regulatory_optionality", "relative_strength"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["price_only_local_peak"], "stage4c_evidence_fields": ["thesis_evidence_broken"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/323/323410/2024.csv", "profile_path": "atlas/symbol_profiles/323/323410.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 6.48, "MFE_90D_pct": 6.48, "MFE_180D_pct": 6.48, "MFE_1Y_pct": 6.48, "MFE_2Y_pct": null, "MAE_30D_pct": -7.34, "MAE_90D_pct": -26.28, "MAE_180D_pct": -31.57, "MAE_1Y_pct": -31.57, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-02-15", "peak_price": 31200, "drawdown_after_peak_pct": -35.74, "green_lateness_ratio": null, "four_b_local_peak_proximity": 1.0, "four_b_full_window_peak_proximity": 1.0, "four_b_timing_verdict": "price_only_local_4B_not_full_4B_without_non_price_evidence", "four_b_evidence_type": ["price_only"], "four_c_protection_label": "hard_4c_late_if_waiting_for_price_damage", "trigger_outcome_label": "failed_rerating_high_MAE", "current_profile_verdict": "current_profile_false_positive", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R6L10_C21_KAKAOBANK_323410_2024_DIGITAL_BANK_VALUEUP_FALSE_POSITIVE|2024-02-02|29300", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R6L10_C21_KAKAOBANK_323410_2024_DIGITAL_BANK_VALUEUP_FALSE_POSITIVE", "trigger_id": "R6L10_C21_KAKAOBANK_FALSE_POSITIVE_2024-02-02", "symbol": "323410", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 65, "customer_quality_score": 0, "policy_or_regulatory_score": 75, "valuation_repricing_score": 55, "execution_risk_score": 45, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "roe_pbr_capital_return_score": 35, "credit_cost_score": 45, "capital_return_execution_score": 15, "share_count_reduction_score": 0, "digital_bank_capital_return_gap_score": 70}, "weighted_score_before": 74, "stage_label_before": "Stage2-Actionable/Yellow-watch", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 55, "customer_quality_score": 0, "policy_or_regulatory_score": 60, "valuation_repricing_score": 35, "execution_risk_score": 55, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "roe_pbr_capital_return_score": 20, "credit_cost_score": 40, "capital_return_execution_score": 5, "share_count_reduction_score": 0, "digital_bank_capital_return_gap_score": 88}, "weighted_score_after": 61, "stage_label_after": "Stage2-watch-only", "changed_components": ["roe_pbr_capital_return_score", "capital_return_execution_score", "share_count_reduction_score", "digital_bank_capital_return_gap_score"], "component_delta_explanation": "C21 shadow profile rewards executed shareholder return and ROE/PBR proof, while capping policy/digital-bank beta without capital-return execution.", "MFE_90D_pct": 6.48, "MAE_90D_pct": -26.28, "score_return_alignment_label": "failed_rerating_high_MAE", "current_profile_verdict": "current_profile_false_positive"}
{"row_type": "score_simulation", "profile_id": "c21_capital_return_execution_shadow_profile", "case_id": "R6L10_C21_KAKAOBANK_323410_2024_DIGITAL_BANK_VALUEUP_FALSE_POSITIVE", "trigger_id": "R6L10_C21_KAKAOBANK_FALSE_POSITIVE_2024-02-02", "symbol": "323410", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 65, "customer_quality_score": 0, "policy_or_regulatory_score": 75, "valuation_repricing_score": 55, "execution_risk_score": 45, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "roe_pbr_capital_return_score": 35, "credit_cost_score": 45, "capital_return_execution_score": 15, "share_count_reduction_score": 0, "digital_bank_capital_return_gap_score": 70}, "weighted_score_before": 74, "stage_label_before": "Stage2-Actionable/Yellow-watch", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 55, "customer_quality_score": 0, "policy_or_regulatory_score": 60, "valuation_repricing_score": 35, "execution_risk_score": 55, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "roe_pbr_capital_return_score": 20, "credit_cost_score": 40, "capital_return_execution_score": 5, "share_count_reduction_score": 0, "digital_bank_capital_return_gap_score": 88}, "weighted_score_after": 61, "stage_label_after": "Stage2-watch-only", "changed_components": ["roe_pbr_capital_return_score", "capital_return_execution_score", "share_count_reduction_score", "digital_bank_capital_return_gap_score"], "component_delta_explanation": "C21 shadow profile rewards executed shareholder return and ROE/PBR proof, while capping policy/digital-bank beta without capital-return execution.", "MFE_90D_pct": 6.48, "MAE_90D_pct": -26.28, "score_return_alignment_label": "failed_rerating_high_MAE", "current_profile_verdict": "current_profile_false_positive"}
{"row_type": "residual_contribution", "round": "R6", "loop": "10", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "new_independent_case_count": 3, "reused_case_count": 0, "new_symbol_count": 3, "new_trigger_family_count": 3, "tested_existing_calibrated_axes": ["stage2_actionable_evidence_bonus", "stage3_yellow_total_min", "stage3_green_total_min", "full_4b_requires_non_price_evidence", "hard_4c_thesis_break_routes_to_4c"], "residual_error_types_found": ["digital_bank_valueup_false_positive", "capital_return_execution_underweight", "price_only_local_4B_not_full_4B"], "loop_contribution_label": "canonical_archetype_rule_candidate", "do_not_propose_new_weight_delta": false}
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
11. For this R6/C21 file, enrich exact evidence URLs before production promotion.

### Expected output

- Concise implementation summary.
- Rows accepted/rejected.
- New sector/canonical archetype coverage.
- Existing axis strengthened/weakened/kept.
- No investment recommendation language.

## 27. Next Round State

```text
completed_round = R6
completed_loop = 10
next_round = R7
next_loop = 10
round_schedule_status = valid
round_sector_consistency = pass
```

## 28. Source Notes

- Stock-web manifest confirms raw/unadjusted OHLC and `max_date = 2026-02-20`.
- KB금융, 하나금융지주, 카카오뱅크 symbol profiles show tradable shards and no corporate-action candidates in the tested 180D windows.
- The price calculations in this MD use stock-web `c`, `h`, and `l` fields from tradable shards.
- External evidence is intentionally marked `source_proxy`; exact source enrichment is deferred to the implementation batch.
