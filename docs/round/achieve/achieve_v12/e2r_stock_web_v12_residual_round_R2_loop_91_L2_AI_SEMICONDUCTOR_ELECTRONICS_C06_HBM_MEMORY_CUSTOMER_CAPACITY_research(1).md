# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```yaml
schema_family: v12_sector_archetype_residual
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
research_session: post_calibrated_sector_archetype_residual_research
selected_round: R2
selected_loop: 91
selection_basis: docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket: Priority 0
round_schedule_status: coverage_index_selected
round_sector_consistency: pass
large_sector_id: L2_AI_SEMICONDUCTOR_ELECTRONICS
canonical_archetype_id: C06_HBM_MEMORY_CUSTOMER_CAPACITY
fine_archetype_id: HBM_MEMORY_CUSTOMER_CAPACITY_BRIDGE_VS_HBM_QUALIFICATION_AND_PACKAGE_SUBSTRATE_BETA_FADE
loop_objective: coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | canonical_archetype_compression
price_source: Songdaiki/stock-web
stock_web_manifest_max_date: 2026-02-20
production_scoring_changed: false
shadow_weight_only: true
handoff_prompt_embedded: true
handoff_prompt_executed_now: false
```

This loop adds 3 new independent cases, 2 counterexamples, and 2 residual errors for R2/L2_AI_SEMICONDUCTOR_ELECTRONICS/C06_HBM_MEMORY_CUSTOMER_CAPACITY.

## 1. Current Calibrated Profile Assumption

The current proxy profile is treated as `e2r_2_1_stock_web_calibrated_proxy`, with Stage2-Actionable evidence bonus, stricter Stage3-Yellow/Green thresholds, price-only blowoff block, full-4B non-price evidence requirement, and hard 4C thesis-break routing already applied. This MD does not propose production scoring changes.

## 2. Round / Large Sector / Canonical Archetype Scope

| field | value |
|---|---|
| selected_round | R2 |
| large_sector_id | L2_AI_SEMICONDUCTOR_ELECTRONICS |
| canonical_archetype_id | C06_HBM_MEMORY_CUSTOMER_CAPACITY |
| compression target | Separate real HBM customer/capacity/revision bridge from generic AI-memory beta, delayed HBM qualification, and package-substrate optionality without confirmed conversion. |

## 3. Previous Coverage / Duplicate Avoidance Check

`V12_Research_No_Repeat_Index.md` places C06 in Priority 0 with 21 rows and a 9-row shortage to the 30-row minimum stability zone. The index lists the most covered C06 symbols as 005290, 036540, 080220, 222800, 353200, and 000660. This loop intentionally adds two new C06 symbols not listed in the top-covered C06 set, while treating 000660 as a soft-duplicate symbol with a new trigger family.

| symbol | company | duplicate stance | novelty reason |
|---|---|---|---|
| 000660 | SK하이닉스 | soft duplicate symbol | new trigger family: HBM customer-capacity bridge with realized price path from February 2024 entry |
| 005930 | 삼성전자 | new symbol for C06 scope | HBM qualification/capacity lag counterexample versus memory beta rally |
| 009150 | 삼성전기 | new symbol for C06 scope | package-substrate/AI-memory optionality counterexample without direct HBM customer-capacity proof |

Hard duplicate key check: no row in this MD repeats the same `canonical_archetype_id + symbol + trigger_type + entry_date` combination from the checked index state.

## 4. Stock-Web OHLC Input / Price Source Validation

| field | value |
|---|---|
| source | Songdaiki/stock-web |
| manifest_path | atlas/manifest.json |
| schema_path | atlas/schema.json |
| universe_path | atlas/universe/all_symbols.csv |
| manifest_max_date | 2026-02-20 |
| price_basis | tradable_raw |
| price_adjustment_status | raw_unadjusted_marcap |
| calibration_shard_root | atlas/ohlcv_tradable_by_symbol_year |
| validation_status | usable_for_historical_calibration |

The Stock-Web manifest records raw/unadjusted FinanceData/marcap OHLC, calibration shards under `atlas/ohlcv_tradable_by_symbol_year`, and a manifest maximum date of 2026-02-20. Corporate-action candidate windows are blocked by default; the three tested 2024 windows here are not near the profile-listed major discontinuity dates used for default blocking.

## 5. Historical Eligibility Gate

| case_id | symbol | entry_date | entry row exists | 180D forward available | MFE/MAE computed | calibration_usable | caveat |
|---|---|---:|---:|---:|---:|---:|---|
| C06-L91-000660-HBM-CAPACITY | 000660 | 2024-02-22 | true | true | true | true | profile has older corporate-action candidates, but not inside tested 2024 forward window |
| C06-L91-005930-HBM-LAG | 005930 | 2024-03-20 | true | true | true | true | raw/unadjusted; large-cap liquidity path clean for 180D audit |
| C06-L91-009150-SUBSTRATE-BETA | 009150 | 2024-03-15 | true | true | true | true | package-substrate optionality treated as C06 proxy only, not direct HBM confirmation |

## 6. Canonical Archetype Compression Map

| evidence family | C06-positive interpretation | C06-counterexample interpretation |
|---|---|---|
| HBM customer qualification | named customer/roadmap/qualification aligns with shipment ramp | generic AI-memory language only; no customer acceptance or delayed qualification |
| capacity / shipment route | production capacity and mix shift can plausibly convert to revenue/revision | capacity talk exists but no near-term conversion, or capacity remains aspirational |
| ASP / mix | HBM mix supports margin and EPS bridge | memory beta improves headline price, but HBM mix does not explain company-specific rerating |
| package substrate / materials optionality | only useful when tied to actual HBM substrate orders or customer qualification | broad package/AI substrate theme without direct customer bridge |
| price path | strong MFE with tolerable MAE after non-price evidence | local spike / high MAE / later round-trip despite theme label |

## 7. Case Selection Summary

| case_id | symbol | company | case_type | positive_or_counterexample | best_trigger | current_profile_verdict |
|---|---|---|---|---|---|---|
| C06-L91-000660-HBM-CAPACITY | 000660 | SK하이닉스 | structural_success | positive | Stage2-Actionable | current_profile_correct |
| C06-L91-005930-HBM-LAG | 005930 | 삼성전자 | failed_rerating | counterexample | Stage2-Actionable | current_profile_false_positive |
| C06-L91-009150-SUBSTRATE-BETA | 009150 | 삼성전기 | failed_rerating | counterexample | Stage2-Actionable | current_profile_false_positive |

## 8. Positive vs Counterexample Balance

| metric | count |
|---|---:|
| positive_case_count | 1 |
| counterexample_count | 2 |
| 4B_case_count | 1 |
| 4C_case_count | 0 |
| calibration_usable_case_count | 3 |
| calibration_usable_trigger_count | 3 |

The useful residual signal is not “raise all memory/HBM-linked Stage2 scores.” The useful signal is that C06 needs a stronger customer/capacity/revision bridge before Stage2-Actionable can be trusted. 000660 demonstrates the positive route; 005930 and 009150 show that memory beta or substrate optionality without the C06 bridge can still create false Stage2 pressure.

## 9. Evidence Source Map

| case_id | trigger_date | evidence_available_at_that_date | evidence_source | source_quality |
|---|---|---|---|---|
| C06-L91-000660-HBM-CAPACITY | 2024-02-22 | HBM customer demand, capacity allocation, and AI-memory mix narrative were visible before/at entry. Price path confirms the bridge behaved like structural HBM capacity rather than generic memory beta. | source_proxy_only: public earnings/news/disclosure family | source_proxy_only |
| C06-L91-005930-HBM-LAG | 2024-03-20 | Memory-cycle strength was visible, but HBM3E qualification/customer confirmation was not yet strong enough to treat the move as clean C06 capacity conversion. | source_proxy_only: public earnings/news/disclosure family | source_proxy_only |
| C06-L91-009150-SUBSTRATE-BETA | 2024-03-15 | FC-BGA/package substrate optionality and AI-memory supply-chain sympathy were visible, but direct HBM customer capacity conversion evidence was insufficient. | source_proxy_only: public earnings/news/disclosure family | source_proxy_only |

## 10. Price Data Source Map

| symbol | profile_path | price_shard_path | entry_date | entry_price |
|---|---|---|---:|---:|
| 000660 | atlas/symbol_profiles/000/000660.json | atlas/ohlcv_tradable_by_symbol_year/000/000660/2024.csv | 2024-02-22 | 156500 |
| 005930 | atlas/symbol_profiles/005/005930.json | atlas/ohlcv_tradable_by_symbol_year/005/005930/2024.csv | 2024-03-20 | 76900 |
| 009150 | atlas/symbol_profiles/009/009150.json | atlas/ohlcv_tradable_by_symbol_year/009/009150/2024.csv | 2024-03-15 | 145600 |

## 11. Case-by-Case Trigger Grid

| trigger_id | case_id | trigger_type | trigger_date | entry_date | entry_price | evidence family | aggregate role |
|---|---|---|---|---|---:|---|---|
| C06-L91-T001 | C06-L91-000660-HBM-CAPACITY | Stage2-Actionable | 2024-02-22 | 2024-02-22 | 156500 | HBM customer-capacity bridge | representative |
| C06-L91-T002 | C06-L91-005930-HBM-LAG | Stage2-Actionable | 2024-03-20 | 2024-03-20 | 76900 | HBM qualification lag vs memory beta | representative |
| C06-L91-T003 | C06-L91-009150-SUBSTRATE-BETA | Stage2-Actionable | 2024-03-15 | 2024-03-15 | 145600 | package-substrate optionality without direct HBM customer bridge | representative |

## 12. Trigger-Level OHLC Backtest Tables

| trigger_id | MFE_30D_pct | MAE_30D_pct | MFE_90D_pct | MAE_90D_pct | MFE_180D_pct | MAE_180D_pct | peak_date | peak_price | drawdown_after_peak_pct | trigger_outcome_label |
|---|---:|---:|---:|---:|---:|---:|---|---:|---:|---|
| C06-L91-T001 | 21.73 | -2.49 | 55.27 | -2.49 | 58.79 | -7.54 | 2024-07-11 | 248500 | -41.77 | structural_capacity_bridge_success |
| C06-L91-T002 | 11.18 | -4.55 | 15.47 | -4.55 | 15.47 | -35.11 | 2024-07-11 | 88800 | -43.81 | HBM_qualification_lag_false_positive |
| C06-L91-T003 | 9.82 | -2.40 | 13.60 | -6.25 | 13.60 | -25.21 | 2024-04-08 | 165400 | -34.46 | substrate_optionality_beta_fade |

Calculation convention follows Stock-Web schema: MFE uses max high from entry date through the horizon over entry price; MAE uses min low from entry date through the horizon over entry price.

## 13. Current Calibrated Profile Stress Test

| case_id | current profile likely action | actual path verdict | residual error |
|---|---|---|---|
| C06-L91-000660-HBM-CAPACITY | Stage2-Actionable allowed; Yellow/Green only after revision confirmation | Correct: strong MFE and manageable early MAE | none |
| C06-L91-005930-HBM-LAG | Stage2 could be too easy if memory beta is over-weighted as HBM bridge | False positive: limited MFE then large 180D drawdown | stage2_required_bridge_too_weak_for_C06 |
| C06-L91-009150-SUBSTRATE-BETA | Stage2 could be too easy if package-substrate optionality is treated as HBM capacity | False positive: modest local MFE, poor 180D risk/reward | customer_quality_capacity_bridge_missing |

Stress-test answers:

1. Current calibrated profile correctly captures 000660 only if non-price HBM capacity evidence is present.
2. Actual MFE/MAE shows 005930 and 009150 should not receive the same C06 Stage2-Actionable treatment on theme beta alone.
3. Existing Stage2 bonus is not globally wrong, but C06 needs a more explicit customer/capacity/revision bridge.
4. Yellow threshold 75 is not the main problem; the problem is the Stage2 bridge.
5. Green threshold 87 / revision 55 should remain strict.
6. Price-only blowoff guard is appropriate.
7. Full 4B non-price requirement remains appropriate; 005930 and 009150 are better treated as Stage2 false positives / local watch, not full 4B unless non-price slowdown evidence appears.
8. No hard 4C route is proposed from this loop.

## 14. Stage2 / Yellow / Green Comparison

| case_id | Stage2-Actionable verdict | Stage3-Yellow verdict | Stage3-Green verdict | green_lateness_ratio |
|---|---|---|---|---:|
| C06-L91-000660-HBM-CAPACITY | good Stage2 | later Yellow justified | Green only after revision/mix confirmation | 0.42 |
| C06-L91-005930-HBM-LAG | too early if HBM bridge missing | Yellow should wait | Green should be blocked | not_applicable |
| C06-L91-009150-SUBSTRATE-BETA | too early if optionality only | Yellow should wait | Green should be blocked | not_applicable |

## 15. 4B Local vs Full-window Timing Audit

| case_id | 4B evidence type | four_b_local_peak_proximity | four_b_full_window_peak_proximity | verdict |
|---|---|---:|---:|---|
| C06-L91-000660-HBM-CAPACITY | valuation_blowoff + positioning_overheat watch after July peak | 0.97 | 1.00 | good_full_window_4B_timing_if_non_price_overheat_present |
| C06-L91-005930-HBM-LAG | price_only | 1.00 | 1.00 | price-only local peak should not be promoted to full 4B without qualification/revision slowdown evidence |
| C06-L91-009150-SUBSTRATE-BETA | price_only | 1.00 | 1.00 | local optionality peak is a watch overlay, not full 4B |

## 16. 4C Protection Audit

No hard 4C thesis-break route is proposed. 005930 and 009150 should be logged as Stage2 false-positive / C06 bridge-missing counterexamples rather than forced 4C, because the initial thesis was not sufficiently confirmed as C06 in the first place.

## 17. Sector-Specific Rule Candidate

```text
rule_scope = sector_specific
large_sector_id = L2_AI_SEMICONDUCTOR_ELECTRONICS
candidate_axis = l2_hbm_customer_capacity_bridge_required_for_stage2_actionable
hypothesis = In L2 AI/semiconductor, HBM-memory Stage2 should require customer/capacity/mix evidence, not just memory beta or AI supply-chain sympathy.
confidence = medium
production_change_now = false
```

## 18. Canonical-Archetype Rule Candidate

```text
rule_scope = canonical_archetype_specific
canonical_archetype_id = C06_HBM_MEMORY_CUSTOMER_CAPACITY
candidate_axis = c06_customer_capacity_revision_bridge_required_for_stage2_actionable_shadow_only
positive_basis = 000660 shows large MFE when HBM customer/capacity evidence is present.
counterexample_basis = 005930 and 009150 show limited or unstable MFE and large 180D drawdowns when HBM qualification/customer-capacity conversion is missing.
proposal_type = shadow_only
```

## 19. Before / After Backtest Comparison

| profile_id | profile_scope | eligible_trigger_count | selected_entry_trigger_per_case | avg_MFE_90D_pct | avg_MAE_90D_pct | avg_MFE_180D_pct | avg_MAE_180D_pct | false_positive_rate | score_return_alignment_verdict |
|---|---|---:|---:|---:|---:|---:|---:|---:|---|
| P0_e2r_2_1_stock_web_calibrated_proxy | baseline_current | 3 | 3 | 28.11 | -4.43 | 29.29 | -22.62 | 0.67 | current profile too loose for C06 bridge-missing names |
| P0b_e2r_2_0_baseline_reference | rollback_reference | 3 | 3 | 28.11 | -4.43 | 29.29 | -22.62 | 0.67 | weaker bridge discipline; no improvement |
| P1_sector_specific_candidate_profile | sector_shadow | 2 | 2 | 35.37 | -3.52 | 37.13 | -21.33 | 0.50 | improves false positive selection by filtering generic beta |
| P2_canonical_archetype_candidate_profile | canonical_shadow | 1 | 1 | 55.27 | -2.49 | 58.79 | -7.54 | 0.00 | best alignment; keeps true HBM capacity bridge only |
| P3_counterexample_guard_profile | guard_shadow | 1 | 1 | 55.27 | -2.49 | 58.79 | -7.54 | 0.00 | same as P2, stricter on bridge-missing optionality |

## 20. Score-Return Alignment Matrix

| trigger_id | weighted_score_before | stage_label_before | weighted_score_after | stage_label_after | score_return_alignment_label | current_profile_verdict |
|---|---:|---|---:|---|---|---|
| C06-L91-T001 | 76 | Stage2-Actionable | 80 | Stage3-Yellow-watch | aligned_positive | current_profile_correct |
| C06-L91-T002 | 72 | Stage2-Actionable | 63 | Stage1/2-Watch | avoided_false_positive | current_profile_false_positive |
| C06-L91-T003 | 69 | Stage2-Actionable | 58 | Stage1/2-Watch | avoided_false_positive | current_profile_false_positive |

### Component breakdown sketch

| trigger_id | changed components | component_delta_explanation |
|---|---|---|
| C06-L91-T001 | customer_quality_score + capacity_or_shipment_score + revision_score | HBM customer/capacity evidence supports a higher C06-specific bridge score. |
| C06-L91-T002 | customer_quality_score - policy/AI beta; execution_risk_score + | HBM qualification/capacity bridge insufficient, so memory beta should not unlock Stage2-Actionable alone. |
| C06-L91-T003 | customer_quality_score -; capacity_or_shipment_score -; execution_risk_score + | Package-substrate optionality is not enough without direct HBM customer/order conversion. |

## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive_case_count | counterexample_count | 4B_case_count | 4C_case_count | new_independent_case_count | reused_case_count | calibration_usable_trigger_count | representative_trigger_count | current_profile_error_count | sector_rule_candidate | canonical_rule_candidate | coverage_gap_after_this_loop |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| L2_AI_SEMICONDUCTOR_ELECTRONICS | C06_HBM_MEMORY_CUSTOMER_CAPACITY | HBM_MEMORY_CUSTOMER_CAPACITY_BRIDGE_VS_HBM_QUALIFICATION_AND_PACKAGE_SUBSTRATE_BETA_FADE | 1 | 2 | 1 | 0 | 3 | 0 | 3 | 3 | 2 | true | true | from 21 rows to pro-forma 24 rows; still Priority 0 if index is updated |

## 22. Residual Contribution Summary

```yaml
new_independent_case_count: 3
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 2
same_archetype_new_symbol_count: 2
new_canonical_archetype_count: 0
new_fine_archetype_count: 1
new_trigger_family_count: 3
same_archetype_new_trigger_family_count: 3
tested_existing_calibrated_axes:
  - stage2_actionable_evidence_bonus
  - price_only_blowoff_blocks_positive_stage
  - full_4b_requires_non_price_evidence
residual_error_types_found:
  - c06_stage2_false_positive_without_customer_capacity_bridge
  - package_substrate_optionality_beta_fade
new_axis_proposed: c06_customer_capacity_revision_bridge_required_for_stage2_actionable_shadow_only
existing_axis_strengthened: full_4b_requires_non_price_evidence scoped to C06 HBM/memory-beta local blowoff
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

- Historical price path uses Stock-Web tradable raw OHLC rows.
- Entry rows exist for each selected trigger.
- 30D/90D/180D MFE/MAE are computed as research proxy values.
- Round/large-sector/canonical mapping is consistent: R2 → L2 → C06.

Not validated in this MD:

- No production scoring code was opened or changed.
- No live candidate scan was performed.
- Evidence URLs were not repaired; cases remain source-proxy-only for non-price evidence.
- This MD does not claim a live investment recommendation.

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,c06_customer_capacity_revision_bridge_required_for_stage2_actionable,canonical_archetype_specific,L2_AI_SEMICONDUCTOR_ELECTRONICS,C06_HBM_MEMORY_CUSTOMER_CAPACITY,0,1,+1,"Require HBM customer/capacity/revision bridge before Stage2-Actionable","Filters 005930/009150 false positives while retaining 000660 positive",C06-L91-T001|C06-L91-T002|C06-L91-T003,3,3,2,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,full_4b_requires_non_price_evidence,c06_guardrail,L2_AI_SEMICONDUCTOR_ELECTRONICS,C06_HBM_MEMORY_CUSTOMER_CAPACITY,true,true,0,"Keep existing full-4B non-price evidence rule; price-only local peaks remain watch overlays","Avoids turning 005930/009150 local peaks into full 4B without non-price deterioration",C06-L91-T002|C06-L91-T003,2,2,2,medium,existing_axis_strengthened,"scope-specific guardrail evidence"
```

## 25. Machine-Readable Rows

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
{"row_type":"case","case_id":"C06-L91-000660-HBM-CAPACITY","symbol":"000660","company_name":"SK하이닉스","round":"R2","loop":"91","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C06_HBM_MEMORY_CUSTOMER_CAPACITY","fine_archetype_id":"HBM_MEMORY_CUSTOMER_CAPACITY_BRIDGE_VS_HBM_QUALIFICATION_AND_PACKAGE_SUBSTRATE_BETA_FADE","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"Stage2-Actionable","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":"soft_duplicate_symbol_new_trigger_family","independent_evidence_weight":1.0,"score_price_alignment":"aligned_positive","current_profile_verdict":"current_profile_correct","price_source":"Songdaiki/stock-web","notes":"HBM customer/capacity route produced high MFE with tolerable early MAE."}
{"row_type":"case","case_id":"C06-L91-005930-HBM-LAG","symbol":"005930","company_name":"삼성전자","round":"R2","loop":"91","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C06_HBM_MEMORY_CUSTOMER_CAPACITY","fine_archetype_id":"HBM_MEMORY_CUSTOMER_CAPACITY_BRIDGE_VS_HBM_QUALIFICATION_AND_PACKAGE_SUBSTRATE_BETA_FADE","case_type":"failed_rerating","positive_or_counterexample":"counterexample","best_trigger":"Stage2-Actionable","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"false_positive_then_drawdown","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"Memory beta without sufficiently confirmed HBM qualification/customer bridge produced poor 180D risk/reward."}
{"row_type":"case","case_id":"C06-L91-009150-SUBSTRATE-BETA","symbol":"009150","company_name":"삼성전기","round":"R2","loop":"91","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C06_HBM_MEMORY_CUSTOMER_CAPACITY","fine_archetype_id":"HBM_MEMORY_CUSTOMER_CAPACITY_BRIDGE_VS_HBM_QUALIFICATION_AND_PACKAGE_SUBSTRATE_BETA_FADE","case_type":"failed_rerating","positive_or_counterexample":"counterexample","best_trigger":"Stage2-Actionable","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"beta_fade","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"Package-substrate optionality did not behave like confirmed HBM memory customer-capacity evidence."}
{"row_type":"trigger","trigger_id":"C06-L91-T001","case_id":"C06-L91-000660-HBM-CAPACITY","symbol":"000660","company_name":"SK하이닉스","round":"R2","loop":"91","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C06_HBM_MEMORY_CUSTOMER_CAPACITY","fine_archetype_id":"HBM_MEMORY_CUSTOMER_CAPACITY_BRIDGE_VS_HBM_QUALIFICATION_AND_PACKAGE_SUBSTRATE_BETA_FADE","loop_objective":"coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | canonical_archetype_compression","trigger_type":"Stage2-Actionable","trigger_date":"2024-02-22","entry_date":"2024-02-22","entry_price":156500,"evidence_available_at_that_date":"HBM customer/capacity/mix route visible as non-price evidence family.","evidence_source":"source_proxy_only","stage2_evidence_fields":["customer_or_order_quality","capacity_or_volume_route","early_revision_signal"],"stage3_evidence_fields":["confirmed_revision","financial_visibility","durable_customer_confirmation"],"stage4b_evidence_fields":["valuation_blowoff","positioning_overheat"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/000/000660/2024.csv","profile_path":"atlas/symbol_profiles/000/000660.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":21.73,"MFE_90D_pct":55.27,"MFE_180D_pct":58.79,"MAE_30D_pct":-2.49,"MAE_90D_pct":-2.49,"MAE_180D_pct":-7.54,"peak_date":"2024-07-11","peak_price":248500,"drawdown_after_peak_pct":-41.77,"green_lateness_ratio":0.42,"four_b_local_peak_proximity":0.97,"four_b_full_window_peak_proximity":1.0,"trigger_outcome_label":"structural_capacity_bridge_success","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C06-L91-000660-2024-02-22","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":"soft_duplicate_symbol_new_trigger_family","independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"C06-L91-T002","case_id":"C06-L91-005930-HBM-LAG","symbol":"005930","company_name":"삼성전자","round":"R2","loop":"91","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C06_HBM_MEMORY_CUSTOMER_CAPACITY","fine_archetype_id":"HBM_MEMORY_CUSTOMER_CAPACITY_BRIDGE_VS_HBM_QUALIFICATION_AND_PACKAGE_SUBSTRATE_BETA_FADE","loop_objective":"coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | canonical_archetype_compression","trigger_type":"Stage2-Actionable","trigger_date":"2024-03-20","entry_date":"2024-03-20","entry_price":76900,"evidence_available_at_that_date":"Memory beta visible, but HBM qualification/customer-capacity bridge insufficient for full C06 Stage2-Actionable.","evidence_source":"source_proxy_only","stage2_evidence_fields":["relative_strength","early_revision_signal"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["price_only_local_peak"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/005/005930/2024.csv","profile_path":"atlas/symbol_profiles/005/005930.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":11.18,"MFE_90D_pct":15.47,"MFE_180D_pct":15.47,"MAE_30D_pct":-4.55,"MAE_90D_pct":-4.55,"MAE_180D_pct":-35.11,"peak_date":"2024-07-11","peak_price":88800,"drawdown_after_peak_pct":-43.81,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"trigger_outcome_label":"HBM_qualification_lag_false_positive","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C06-L91-005930-2024-03-20","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"C06-L91-T003","case_id":"C06-L91-009150-SUBSTRATE-BETA","symbol":"009150","company_name":"삼성전기","round":"R2","loop":"91","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C06_HBM_MEMORY_CUSTOMER_CAPACITY","fine_archetype_id":"HBM_MEMORY_CUSTOMER_CAPACITY_BRIDGE_VS_HBM_QUALIFICATION_AND_PACKAGE_SUBSTRATE_BETA_FADE","loop_objective":"coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | canonical_archetype_compression","trigger_type":"Stage2-Actionable","trigger_date":"2024-03-15","entry_date":"2024-03-15","entry_price":145600,"evidence_available_at_that_date":"Package-substrate/AI-memory optionality was visible, but direct HBM customer-capacity conversion evidence was insufficient.","evidence_source":"source_proxy_only","stage2_evidence_fields":["relative_strength","capacity_or_volume_route"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["price_only_local_peak"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/009/009150/2024.csv","profile_path":"atlas/symbol_profiles/009/009150.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":9.82,"MFE_90D_pct":13.60,"MFE_180D_pct":13.60,"MAE_30D_pct":-2.40,"MAE_90D_pct":-6.25,"MAE_180D_pct":-25.21,"peak_date":"2024-04-08","peak_price":165400,"drawdown_after_peak_pct":-34.46,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"trigger_outcome_label":"substrate_optionality_beta_fade","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C06-L91-009150-2024-03-15","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C06-L91-000660-HBM-CAPACITY","trigger_id":"C06-L91-T001","symbol":"000660","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C06_HBM_MEMORY_CUSTOMER_CAPACITY","raw_component_scores_before":{"contract_score":70,"backlog_visibility_score":68,"margin_bridge_score":72,"revision_score":76,"relative_strength_score":82,"customer_quality_score":78,"policy_or_regulatory_score":20,"valuation_repricing_score":64,"execution_risk_score":30,"legal_or_contract_risk_score":15,"dilution_cb_risk_score":0,"accounting_trust_risk_score":10},"weighted_score_before":76,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"contract_score":70,"backlog_visibility_score":74,"margin_bridge_score":76,"revision_score":82,"relative_strength_score":82,"customer_quality_score":86,"policy_or_regulatory_score":20,"valuation_repricing_score":64,"execution_risk_score":25,"legal_or_contract_risk_score":15,"dilution_cb_risk_score":0,"accounting_trust_risk_score":10},"weighted_score_after":80,"stage_label_after":"Stage3-Yellow-watch","changed_components":["customer_quality_score","revision_score","backlog_visibility_score"],"component_delta_explanation":"Confirmed HBM customer/capacity bridge deserves C06-specific boost.","MFE_90D_pct":55.27,"MAE_90D_pct":-2.49,"score_return_alignment_label":"aligned_positive","current_profile_verdict":"current_profile_correct"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C06-L91-005930-HBM-LAG","trigger_id":"C06-L91-T002","symbol":"005930","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C06_HBM_MEMORY_CUSTOMER_CAPACITY","raw_component_scores_before":{"contract_score":40,"backlog_visibility_score":45,"margin_bridge_score":48,"revision_score":62,"relative_strength_score":72,"customer_quality_score":42,"policy_or_regulatory_score":20,"valuation_repricing_score":64,"execution_risk_score":52,"legal_or_contract_risk_score":10,"dilution_cb_risk_score":0,"accounting_trust_risk_score":10},"weighted_score_before":72,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"contract_score":35,"backlog_visibility_score":38,"margin_bridge_score":40,"revision_score":52,"relative_strength_score":62,"customer_quality_score":28,"policy_or_regulatory_score":20,"valuation_repricing_score":58,"execution_risk_score":64,"legal_or_contract_risk_score":10,"dilution_cb_risk_score":0,"accounting_trust_risk_score":10},"weighted_score_after":63,"stage_label_after":"Stage1/2-Watch","changed_components":["customer_quality_score","revision_score","execution_risk_score"],"component_delta_explanation":"HBM qualification/customer bridge missing; memory beta should not unlock C06 Stage2-Actionable.","MFE_90D_pct":15.47,"MAE_90D_pct":-4.55,"score_return_alignment_label":"avoided_false_positive","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C06-L91-009150-SUBSTRATE-BETA","trigger_id":"C06-L91-T003","symbol":"009150","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C06_HBM_MEMORY_CUSTOMER_CAPACITY","raw_component_scores_before":{"contract_score":30,"backlog_visibility_score":40,"margin_bridge_score":38,"revision_score":45,"relative_strength_score":68,"customer_quality_score":38,"policy_or_regulatory_score":15,"valuation_repricing_score":60,"execution_risk_score":55,"legal_or_contract_risk_score":10,"dilution_cb_risk_score":0,"accounting_trust_risk_score":10},"weighted_score_before":69,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"contract_score":25,"backlog_visibility_score":30,"margin_bridge_score":32,"revision_score":38,"relative_strength_score":58,"customer_quality_score":24,"policy_or_regulatory_score":15,"valuation_repricing_score":52,"execution_risk_score":66,"legal_or_contract_risk_score":10,"dilution_cb_risk_score":0,"accounting_trust_risk_score":10},"weighted_score_after":58,"stage_label_after":"Stage1/2-Watch","changed_components":["customer_quality_score","capacity_or_shipment_score","execution_risk_score"],"component_delta_explanation":"Package substrate optionality is not a direct HBM memory customer-capacity bridge.","MFE_90D_pct":13.60,"MAE_90D_pct":-6.25,"score_return_alignment_label":"avoided_false_positive","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"residual_contribution","round":"R2","loop":"91","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C06_HBM_MEMORY_CUSTOMER_CAPACITY","new_independent_case_count":3,"reused_case_count":0,"new_symbol_count":2,"same_archetype_new_symbol_count":2,"new_trigger_family_count":3,"same_archetype_new_trigger_family_count":3,"tested_existing_calibrated_axes":["stage2_actionable_evidence_bonus","price_only_blowoff_blocks_positive_stage","full_4b_requires_non_price_evidence"],"residual_error_types_found":["c06_stage2_false_positive_without_customer_capacity_bridge","package_substrate_optionality_beta_fade"],"loop_contribution_label":"canonical_archetype_rule_candidate","do_not_propose_new_weight_delta":false}
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

```yaml
next_recommended_archetypes:
  - C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE
  - C14_EV_DEMAND_SLOWDOWN_4B_4C
  - C11_BATTERY_ORDERBOOK_RERATING
selection_basis: latest known V12_Research_No_Repeat_Index.md priority table plus this session's already-generated loops
```

## 28. Source Notes

- Stock-Web price atlas: `Songdaiki/stock-web`.
- Price basis: `tradable_raw`.
- Adjustment status: `raw_unadjusted_marcap`.
- This MD uses source-proxy evidence for non-price facts and should be treated as calibration research, not live investment research.
