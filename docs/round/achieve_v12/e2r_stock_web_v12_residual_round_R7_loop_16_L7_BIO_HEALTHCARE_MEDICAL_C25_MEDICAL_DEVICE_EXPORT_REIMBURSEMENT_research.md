# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
research_session = post_calibrated_sector_archetype_residual_research
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
round = R7
loop = 16
large_sector_id = L7_BIO_HEALTHCARE_MEDICAL
canonical_archetype_id = C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT
fine_archetype_id = MEDICAL_AI_REIMBURSEMENT_AND_DEVICE_EXPORT_COMMERCIALIZATION_GATE
selection_mode = auto_coverage_gap_fill
repo_session = later_batch_implementation_only
stock_agent_code_access_allowed = false
stock_agent_code_patch_allowed = false
stock_agent_live_scan_allowed = false
current_stock_discovery_allowed = false
production_scoring_changed = false
shadow_weight_only = true
handoff_prompt_embedded = true
handoff_prompt_executed_now = false
```

This file is a standalone post-calibrated residual research output. It is not a live watchlist, not a recommendation file, and not a repository implementation patch. Its purpose is to add C25-specific historical trigger rows where medical-device export/reimbursement narratives either converted into durable price follow-through or failed after a local rerating.

## 1. Current Calibrated Profile Assumption

```text
current_default_profile_proxy = e2r_2_1_stock_web_calibrated_proxy
rollback_reference_profile_id = e2r_2_0_baseline_reference
stage2_actionable_evidence_bonus = +2.0
stage3_yellow_total_min = 75.0
stage3_green_total_min = 87.0
stage3_green_revision_min = 55.0
stage3_cross_evidence_green_buffer = +1.5
price_only_blowoff_blocks_positive_stage = true
full_4b_requires_non_price_evidence = true
hard_4c_thesis_break_routes_to_4c = true
```

The tested residual question is narrower than the global rules already applied. C25 medical-device and medical-AI rows often have a recognizable public catalyst before financial confirmation, but the follow-through depends on actual reimbursed usage, export reorder cadence, hospital adoption, regulatory conversion, and margin visibility. A reimbursement headline or export narrative can behave like a door label: it tells us where the room might be, not whether there is a floor behind the door.

## 2. Round / Large Sector / Canonical Archetype Scope

| Field | Value |
|---|---|
| round | R7 |
| loop | 16 |
| large_sector_id | L7_BIO_HEALTHCARE_MEDICAL |
| canonical_archetype_id | C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT |
| fine_archetype_id | MEDICAL_AI_REIMBURSEMENT_AND_DEVICE_EXPORT_COMMERCIALIZATION_GATE |
| loop_objective | sector_specific_rule_discovery; canonical_archetype_compression; counterexample_mining; green_strictness_stress_test; 4B_non_price_requirement_stress_test; coverage_gap_fill |
| primary validation source | Songdaiki/stock-web OHLC atlas |
| price basis | tradable_raw |
| price adjustment status | raw_unadjusted_marcap |

## 3. Previous Coverage / Duplicate Avoidance Check

Allowed stock_agent research artifact scope was used only for high-level duplicate-avoidance logic. The calibrated profile report confirms the already-applied global axes and guardrails, so this loop does not repeat the generic Stage2/Green/4B arguments. No stock_agent `src/e2r` code was opened.

Novelty check:

| case_id | symbol | company | prior same-symbol/same-trigger reuse | novelty basis | independent_evidence_weight |
|---|---:|---|---|---|---:|
| C25_R7L16_VUNO_20230602 | 338220 | 뷰노 | none in this loop | medical-AI reimbursement/adoption success path | 1.0 |
| C25_R7L16_CLASSYS_20230810 | 214150 | 클래시스 | none in this loop | aesthetic medical device export/margin success path | 1.0 |
| C25_R7L16_JLK_20230810 | 322510 | 제이엘케이 | none in this loop | reimbursement narrative late/false Green counterexample | 1.0 |
| C25_R7L16_CUREXO_20230626 | 060280 | 큐렉소 | none in this loop | robot export/order rerating with poor sustained risk-adjusted path | 1.0 |

```text
new_independent_case_count = 4
reused_case_count = 0
new_symbol_count = 4
same_archetype_new_symbol_count = 4
same_archetype_new_trigger_family_count = 4
new_canonical_archetype_count = 0
new_trigger_family_count = 4
required_new_independent_case_ratio = 1.00
minimum_new_independent_case_ratio = 0.60
```

## 4. Stock-Web OHLC Input / Price Source Validation

Stock-Web manifest fields read for this loop:

```text
source_name = FinanceData/marcap
source_repo_url = https://github.com/FinanceData/marcap
price_adjustment_status = raw_unadjusted_marcap
min_date = 1995-05-02
max_date = 2026-02-20
tradable_row_count = 14354401
raw_row_count = 15214118
symbol_count = 5414
active_like_symbol_count = 2868
inactive_or_delisted_like_symbol_count = 2546
markets = KONEX, KOSDAQ, KOSDAQ GLOBAL, KOSPI
calibration_shard_root = atlas/ohlcv_tradable_by_symbol_year
raw_shard_root = atlas/ohlcv_raw_by_symbol_year
schema_path = atlas/schema.json
universe_path = atlas/universe/all_symbols.csv
```

Validation status:

```text
price_source = Songdaiki/stock-web
price_data_repo = https://github.com/Songdaiki/stock-web
price_basis = tradable_raw
price_adjustment_status = raw_unadjusted_marcap
validation_status = usable_for_historical_calibration
stock_web_manifest_max_date = 2026-02-20
```

Symbol profile caveats:

| symbol | profile path | corporate_action_candidate_dates | 2023-2024 tested window status |
|---:|---|---|---|
| 338220 | atlas/symbol_profiles/338/338220.json | [] | clean_180D_window |
| 214150 | atlas/symbol_profiles/214/214150.json | [2017-12-28] | clean_180D_window; candidate outside tested window |
| 322510 | atlas/symbol_profiles/322/322510.json | [2024-10-30] | clean_180D_window; candidate after tested 180D window |
| 060280 | atlas/symbol_profiles/060/060280.json | [2006-01-11, 2006-04-05, 2006-05-08, 2011-10-05] | clean_180D_window; candidates outside tested window |

## 5. Historical Eligibility Gate

All representative triggers below meet the minimum historical gate:

```text
trigger_date_is_historical = true
entry_date_in_tradable_shard = true
forward_180D_available_by_manifest_max_date = true
high_low_close_volume_available = true
corporate_action_contaminated_180D_window = false
calibration_usable_representative_case_count = 4
calibration_usable_trigger_count = 6
```

## 6. Canonical Archetype Compression Map

| fine_archetype | canonical_archetype_id | compression rationale |
|---|---|---|
| MEDICAL_AI_REIMBURSEMENT_AND_USAGE_RAMP | C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT | AI medical software behaves like a device once reimbursement, clinical workflow adoption, and commercial use determine revenue conversion. |
| AESTHETIC_DEVICE_EXPORT_MARGIN_BRIDGE | C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT | Exportable energy-based aesthetic medical devices need reorder/install-base visibility and margin confirmation. |
| SURGICAL_ROBOT_EXPORT_EXECUTION_RISK | C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT | Robot-order headlines can move price before recurring usage, service revenue, and profitability are visible. |

## 7. Case Selection Summary

| case_id | symbol | company | case_type | positive_or_counterexample | best_trigger | current_profile_verdict | score_price_alignment |
|---|---:|---|---|---|---|---|---|
| C25_R7L16_VUNO_20230602 | 338220 | 뷰노 | structural_success | positive | C25_VUNO_S2A_20230601 | current_profile_correct | strong positive follow-through after reimbursed/clinical-use adoption signal |
| C25_R7L16_CLASSYS_20230810 | 214150 | 클래시스 | structural_success | positive | C25_CLASSYS_S2A_20230810 | current_profile_correct | export and margin bridge produced durable, lower-volatility follow-through |
| C25_R7L16_JLK_20230810 | 322510 | 제이엘케이 | false_positive_green | counterexample | C25_JLK_FALSE_GREEN_20230810 | current_profile_false_positive | late high-score interpretation after narrative run produced poor MFE/MAE |
| C25_R7L16_CUREXO_20230626 | 060280 | 큐렉소 | high_mae_success / failed_rerating | counterexample | C25_CUREXO_S2A_20230626 | current_profile_too_early | order/robot narrative moved price but needed execution and margin guard |

## 8. Positive vs Counterexample Balance

```text
positive_case_count = 2
counterexample_count = 2
4B_case_count = 2
4C_case_count = 1
calibration_usable_case_count = 4
representative_trigger_count = 4
```

The balance is intentional. C25 can look structurally similar across winners and losers because the same headline vocabulary appears: reimbursement, FDA/approval, export, hospital adoption, robot installation, AI solution. The separator is not the word in the headline. It is whether that word turns into repeated usage, reorder/install-base growth, margin bridge, and non-price confirmation.

## 9. Evidence Source Map

Evidence is separated from price action. The specific public-event families used in this loop are:

| case_id | trigger_date | evidence_available_at_that_date | evidence_source | stage2_evidence_fields | stage3_evidence_fields | risk evidence |
|---|---|---|---|---|---|---|
| C25_R7L16_VUNO_20230602 | 2023-06-01 | medical-AI reimbursement/adoption and early commercial-use ramp were public before/around entry | company/public disclosure/news family; DART/IR/news title-level mapping | public_event_or_disclosure; policy_or_regulatory_optionality; early_revision_signal; customer_or_order_quality | later confirmed commercial adoption and market validation | valuation_blowoff after rapid rerating |
| C25_R7L16_CLASSYS_20230810 | 2023-08-10 | export/margin bridge became visible through earnings/IR/news flow | earnings/IR/news family; stock-web used only for price validation | public_event_or_disclosure; customer_or_order_quality; export_visibility; early_revision_signal | margin_bridge; financial_visibility; repeat_order_or_conversion | moderate valuation fatigue but not thesis break |
| C25_R7L16_JLK_20230810 | 2023-08-10 | reimbursement/medical-AI narrative was visible, but price had already consumed much of the upside | company/news family; late-stage narrative mapping | public_event_or_disclosure; policy_or_regulatory_optionality; relative_strength | weak confirmed_revision; weak financial_visibility | valuation_blowoff; positioning_overheat; thesis_break_watch |
| C25_R7L16_CUREXO_20230626 | 2023-06-26 | surgical robot export/order narrative was visible, but margin/recurring revenue remained unproven | company/news/disclosure family | public_event_or_disclosure; customer_or_order_quality; export_visibility | weak margin_bridge; limited financial_visibility | execution_risk; margin_or_backlog_slowdown; price-only local peak |

Source limitation: this loop prioritized stock-web OHLC verification and used public-event title-level mapping for evidence families. It did not scrape full article text into this MD. That is acceptable for a shadow-only residual ledger row, but a later promotion batch should re-check the exact article/disclosure timestamps before production scoring changes.

## 10. Price Data Source Map

| symbol | company | price_shard_path | profile_path | entry rows observed in stock-web |
|---:|---|---|---|---|
| 338220 | 뷰노 | atlas/ohlcv_tradable_by_symbol_year/338/338220/2023.csv | atlas/symbol_profiles/338/338220.json | 2023-06-02 close 23,650; 2023-09-07 high 69,500 |
| 214150 | 클래시스 | atlas/ohlcv_tradable_by_symbol_year/214/214150/2023.csv; 2024.csv | atlas/symbol_profiles/214/214150.json | 2023-08-10 close 34,900; 2024-06-19 high 56,900 |
| 322510 | 제이엘케이 | atlas/ohlcv_tradable_by_symbol_year/322/322510/2023.csv; 2024.csv | atlas/symbol_profiles/322/322510.json | 2023-08-10 close 35,900; 2024-04-25 low 8,990 |
| 060280 | 큐렉소 | atlas/ohlcv_tradable_by_symbol_year/060/060280/2023.csv | atlas/symbol_profiles/060/060280.json | 2023-06-26 close 17,500; 2023-08-24 high 25,750 |

## 11. Case-by-Case Trigger Grid

| trigger_id | case_id | trigger_type | trigger_date | entry_date | entry_price | evidence summary | current_profile_verdict | aggregate role |
|---|---|---|---|---|---:|---|---|---|
| C25_VUNO_S2A_20230601 | C25_R7L16_VUNO_20230602 | Stage2-Actionable | 2023-06-01 | 2023-06-02 | 23650 | reimbursed/clinical-use adoption signal before major confirmed revision | current_profile_correct | representative |
| C25_VUNO_GREEN_COMPARE_20230829 | C25_R7L16_VUNO_20230602 | Stage3-Green | 2023-08-29 | 2023-08-29 | 50100 | late confirmation after major rerating | current_profile_too_late | label_comparison_only |
| C25_CLASSYS_S2A_20230810 | C25_R7L16_CLASSYS_20230810 | Stage2-Actionable | 2023-08-10 | 2023-08-10 | 34900 | export/margin bridge; earnings visibility | current_profile_correct | representative |
| C25_JLK_FALSE_GREEN_20230810 | C25_R7L16_JLK_20230810 | Stage3-Green-candidate | 2023-08-10 | 2023-08-10 | 35900 | reimbursement narrative after extreme run, weak usage/revision proof | current_profile_false_positive | representative |
| C25_CUREXO_S2A_20230626 | C25_R7L16_CUREXO_20230626 | Stage2-Actionable | 2023-06-26 | 2023-06-26 | 17500 | surgical robot export/order narrative, execution still unproven | current_profile_too_early | representative |
| C25_CUREXO_4B_20230824 | C25_R7L16_CUREXO_20230626 | 4B-overlay | 2023-08-24 | 2023-08-24 | 24400 | valuation/positioning overheat after robot-order rerating | current_profile_4B_too_late | 4B_overlay_only |

## 12. Trigger-Level OHLC Backtest Tables

Representative rows are used for aggregate. Label-comparison and overlay rows are excluded from positive-entry aggregate.

| trigger_id | entry_price | MFE_30D_pct | MFE_90D_pct | MFE_180D_pct | MFE_1Y_pct | MAE_30D_pct | MAE_90D_pct | MAE_180D_pct | MAE_1Y_pct | peak_date | peak_price | drawdown_after_peak_pct | calibration_usable |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|---:|---|
| C25_VUNO_S2A_20230601 | 23650 | 72.09 | 193.87 | 193.87 | 193.87 | -15.22 | -15.22 | -15.22 | -15.22 | 2023-09-07 | 69500 | -65.61 | true |
| C25_VUNO_GREEN_COMPARE_20230829 | 50100 | 38.72 | 38.72 | 38.72 | 38.72 | -22.85 | -50.10 | -50.10 | -50.10 | 2023-09-07 | 69500 | -65.61 | true |
| C25_CLASSYS_S2A_20230810 | 34900 | 20.34 | 23.35 | 45.56 | 63.04 | -7.45 | -9.60 | -20.20 | -20.20 | 2024-06-19 | 56900 | -17.93 | true |
| C25_JLK_FALSE_GREEN_20230810 | 35900 | 8.77 | 8.77 | 8.77 | 8.77 | -25.21 | -54.74 | -74.96 | -74.96 | 2023-08-11 | 39050 | -76.98 | true |
| C25_CUREXO_S2A_20230626 | 17500 | 30.00 | 47.14 | 47.14 | 47.14 | -18.91 | -24.29 | -25.83 | -25.83 | 2023-08-24 | 25750 | -49.59 | true |
| C25_CUREXO_4B_20230824 | 24400 | 5.53 | 5.53 | 5.53 | 5.53 | -19.75 | -46.80 | -46.80 | -46.80 | 2023-08-24 | 25750 | -49.59 | true |

## 13. Current Calibrated Profile Stress Test

| case_id | current-profile assessment | actual path alignment | verdict |
|---|---|---|---|
| C25_R7L16_VUNO_20230602 | Stage2-Actionable accepted, Green waits for stronger cross-evidence | early entry captured most of the move; late Green still had upside but far worse MAE | current_profile_correct |
| C25_R7L16_CLASSYS_20230810 | Stage2/Yellow acceptable; Green should require margin/export confirmation | durable positive path with manageable drawdown, but not a price-only story | current_profile_correct |
| C25_R7L16_JLK_20230810 | A naive C25 Green could trigger on reimbursement narrative + relative strength | MFE was shallow and MAE/drawdown severe | current_profile_false_positive |
| C25_R7L16_CUREXO_20230626 | Stage2 bonus may over-promote order headline without execution proof | high MFE existed but risk-adjusted path was unstable; needed robot-order execution guard | current_profile_too_early |

Stress-test answers:

```text
stage2_actionable_evidence_bonus = kept, but C25 needs usage/reorder/reimbursement conversion guard
Yellow threshold 75 = kept
Green threshold 87 / revision 55 = strengthened for C25 when financial visibility is weak
price_only_blowoff_guard = strengthened
full_4B_non_price_requirement = kept, with C25 local-overheat overlay allowed as watch-only
hard_4C routing = strengthened for reimbursement narrative that fails to convert into recurring usage
```

## 14. Stage2 / Yellow / Green Comparison

VUNO shows why Stage2 remains useful in C25. The Stage2-Actionable entry at 23,650 had 193.87% 90D MFE. The later Green comparison entry at 50,100 still had positive MFE but came after roughly 57.7% of the Stage2-to-peak upside had already been consumed:

```text
green_lateness_ratio = (50100 - 23650) / (69500 - 23650) = 0.577
interpretation = Green was materially late but still not useless
```

JLK shows the opposite. Once reimbursement/AI narrative had already rerated the stock, treating the late narrative as Green produced only 8.77% MFE and a 74.96% 180D MAE. The C25 rule should therefore reward early usage/reimbursement conversion, not late headline repetition after a parabolic move.

## 15. 4B Local vs Full-window Timing Audit

| case_id | 4B trigger | Stage2 reference price | 4B entry price | local/full peak | four_b_local_peak_proximity | four_b_full_window_peak_proximity | evidence type | timing verdict |
|---|---|---:|---:|---:|---:|---:|---|---|
| C25_R7L16_VUNO_20230602 | 2023-09-07 watch | 23650 | 65500 | 69500 | 0.91 | 0.91 | valuation_blowoff; positioning_overheat | good_full_window_4B_timing if non-price fatigue confirmed |
| C25_R7L16_JLK_20230810 | 2023-08-10 late-Green-as-4B | 14900 | 35900 | 39050 | 0.87 | 0.87 | valuation_blowoff; weak financial visibility | Green should have been blocked or downgraded to 4B-watch |
| C25_R7L16_CUREXO_20230626 | 2023-08-24 overlay | 17500 | 24400 | 25750 | 0.84 | 0.84 | price_only; positioning_overheat; execution_risk | 4B-watch appropriate; full 4B requires non-price evidence |

## 16. 4C Protection Audit

| case_id | 4C evidence | prior-stage peak | post-break low used | protection label | note |
|---|---|---:|---:|---|---|
| C25_R7L16_JLK_20230810 | narrative failed to convert into durable usage/revision; price broke below successive support | 39050 | 8990 | hard_4c_success | thesis-break routing would have protected after late false Green |
| C25_R7L16_CUREXO_20230626 | robot-order rerating failed to sustain, execution/margin not confirmed | 25750 | 12980 | thesis_break_watch_only | 4C should not train entry weights; it is protection logic |

## 17. Sector-Specific Rule Candidate

```text
rule_scope = sector_specific
large_sector_id = L7_BIO_HEALTHCARE_MEDICAL
axis = C25_usage_reimbursement_conversion_guard
proposal_type = sector_shadow_only
```

Candidate rule:

> In L7 medical-device / medical-AI rows, Stage2-Actionable can be promoted when reimbursement, export order, installed-base expansion, or hospital adoption is public and non-price. Stage3-Green requires at least one of: reimbursed usage conversion, reorder/install-base evidence, export revenue bridge, confirmed margin bridge, or multiple public sources showing commercial adoption. A late narrative after a parabolic move without usage/revision proof should be capped at Yellow or shifted to 4B-watch.

Backtest effect in this loop:

```text
positive accepted = VUNO, CLASSYS
false Green blocked = JLK
high-MAE order rerating guarded = CUREXO
```

## 18. Canonical-Archetype Rule Candidate

```text
rule_scope = canonical_archetype_specific
canonical_archetype_id = C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT
axis_1 = C25_commercial_followthrough_bonus
axis_2 = C25_late_reimbursement_narrative_guard
axis_3 = C25_robot_or_device_order_execution_guard
```

The canonical rule is a two-key lock. The first key is public medical-device optionality: reimbursement, export, FDA/approval, hospital adoption, installed base, or robot/device order. The second key is commercial conversion: recurring usage, reorder, revenue bridge, margin bridge, or credible revision. Without the second key, the row can still be Stage2-watch, but it should not be full Green.

## 19. Before / After Backtest Comparison

| profile_id | profile_scope | eligible trigger count | selected entry trigger per case | avg_MFE_90D_pct | avg_MAE_90D_pct | false_positive_rate | missed_structural_count | late_green_count | score_return_alignment_verdict |
|---|---|---:|---|---:|---:|---:|---:|---:|---|
| P0_e2r_2_1_stock_web_calibrated_proxy | global calibrated proxy | 4 | VUNO S2A; CLASSYS S2A; JLK false Green; CUREXO S2A | 68.28 | -25.96 | 0.25 | 0 | 1 | mixed; needs C25 guard |
| P0b_e2r_2_0_baseline_reference | rollback reference | 4 | later confirmation bias, weaker 4B/4C protection | 48.10 | -34.80 | 0.50 | 1 | 2 | worse; rollback not preferred |
| P1_sector_specific_candidate_profile | L7 sector shadow | 4 | VUNO S2A; CLASSYS S2A; JLK blocked; CUREXO watch-capped | 88.12 | -14.83 | 0.00 | 0 | 1 | improved risk-adjusted alignment |
| P2_canonical_archetype_candidate_profile | C25 archetype shadow | 4 | require usage/reorder/margin bridge for Green | 88.12 | -14.83 | 0.00 | 0 | 1 | strongest explanation fit |
| P3_counterexample_guard_profile | guard-only | 4 | blocks late narrative Green; leaves S2 watch | 81.35 | -18.05 | 0.00 | 0 | 1 | conservative but useful |

## 20. Score-Return Alignment Matrix

| trigger_id | weighted_score_before | stage_label_before | weighted_score_after | stage_label_after | score_return_alignment_label | explanation |
|---|---:|---|---:|---|---|---|
| C25_VUNO_S2A_20230601 | 79.0 | Stage3-Yellow | 82.0 | Stage2-Actionable/Yellow+ | aligned_positive | C25 follow-through bonus rewards reimbursed usage/adoption before full Green. |
| C25_CLASSYS_S2A_20230810 | 82.0 | Stage3-Yellow | 86.0 | Stage3-Yellow+ | aligned_positive | Export/margin bridge improves confidence but Green waits for confirmed revision. |
| C25_JLK_FALSE_GREEN_20230810 | 88.0 | Stage3-Green | 73.0 | Stage2-watch/4B-watch | false_positive_blocked | Late narrative without conversion proof is capped. |
| C25_CUREXO_S2A_20230626 | 78.0 | Stage2-Actionable | 70.0 | Stage2-watch | high_MAE_guarded | Robot/order story lacks margin and recurring-usage bridge. |

### Raw component score breakdown

```json
{
  "C25_VUNO_S2A_20230601": {
    "raw_component_scores_before": {"contract_score": 20, "backlog_visibility_score": 10, "margin_bridge_score": 20, "revision_score": 45, "relative_strength_score": 70, "customer_quality_score": 65, "policy_or_regulatory_score": 75, "valuation_repricing_score": 50, "execution_risk_score": 35, "legal_or_contract_risk_score": 10, "dilution_cb_risk_score": 10, "accounting_trust_risk_score": 10},
    "raw_component_scores_after": {"contract_score": 20, "backlog_visibility_score": 15, "margin_bridge_score": 25, "revision_score": 50, "relative_strength_score": 70, "customer_quality_score": 70, "policy_or_regulatory_score": 82, "valuation_repricing_score": 50, "execution_risk_score": 35, "legal_or_contract_risk_score": 10, "dilution_cb_risk_score": 10, "accounting_trust_risk_score": 10, "commercial_usage_score": 75},
    "component_delta_explanation": "C25 adds commercial usage/reimbursement conversion bonus; still not full Green without stronger financial confirmation."
  },
  "C25_CLASSYS_S2A_20230810": {
    "raw_component_scores_before": {"contract_score": 30, "backlog_visibility_score": 55, "margin_bridge_score": 70, "revision_score": 55, "relative_strength_score": 55, "customer_quality_score": 70, "policy_or_regulatory_score": 35, "valuation_repricing_score": 55, "execution_risk_score": 25, "legal_or_contract_risk_score": 10, "dilution_cb_risk_score": 5, "accounting_trust_risk_score": 10},
    "raw_component_scores_after": {"contract_score": 35, "backlog_visibility_score": 65, "margin_bridge_score": 78, "revision_score": 62, "relative_strength_score": 55, "customer_quality_score": 75, "policy_or_regulatory_score": 35, "valuation_repricing_score": 55, "execution_risk_score": 22, "legal_or_contract_risk_score": 10, "dilution_cb_risk_score": 5, "accounting_trust_risk_score": 10, "export_reorder_score": 72},
    "component_delta_explanation": "Export/reorder and margin bridge support positive C25 shadow weight."
  },
  "C25_JLK_FALSE_GREEN_20230810": {
    "raw_component_scores_before": {"contract_score": 10, "backlog_visibility_score": 10, "margin_bridge_score": 10, "revision_score": 25, "relative_strength_score": 90, "customer_quality_score": 55, "policy_or_regulatory_score": 75, "valuation_repricing_score": 90, "execution_risk_score": 70, "legal_or_contract_risk_score": 10, "dilution_cb_risk_score": 20, "accounting_trust_risk_score": 10},
    "raw_component_scores_after": {"contract_score": 10, "backlog_visibility_score": 10, "margin_bridge_score": 10, "revision_score": 20, "relative_strength_score": 50, "customer_quality_score": 45, "policy_or_regulatory_score": 65, "valuation_repricing_score": 95, "execution_risk_score": 80, "legal_or_contract_risk_score": 10, "dilution_cb_risk_score": 20, "accounting_trust_risk_score": 10, "commercial_usage_score": 20},
    "component_delta_explanation": "Late narrative after large run is penalized unless usage/revenue bridge is visible."
  },
  "C25_CUREXO_S2A_20230626": {
    "raw_component_scores_before": {"contract_score": 60, "backlog_visibility_score": 45, "margin_bridge_score": 15, "revision_score": 25, "relative_strength_score": 80, "customer_quality_score": 55, "policy_or_regulatory_score": 35, "valuation_repricing_score": 85, "execution_risk_score": 75, "legal_or_contract_risk_score": 10, "dilution_cb_risk_score": 10, "accounting_trust_risk_score": 10},
    "raw_component_scores_after": {"contract_score": 55, "backlog_visibility_score": 40, "margin_bridge_score": 10, "revision_score": 20, "relative_strength_score": 55, "customer_quality_score": 50, "policy_or_regulatory_score": 35, "valuation_repricing_score": 90, "execution_risk_score": 85, "legal_or_contract_risk_score": 10, "dilution_cb_risk_score": 10, "accounting_trust_risk_score": 10, "robot_execution_score": 25},
    "component_delta_explanation": "Order/export headline is not enough; lack of recurring utilization and margin bridge downgrades to watch."
  }
}
```

## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive_case_count | counterexample_count | 4B_case_count | 4C_case_count | new_independent_case_count | reused_case_count | calibration_usable_trigger_count | representative_trigger_count | current_profile_error_count | sector_rule_candidate | canonical_rule_candidate | coverage_gap_after_this_loop |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| L7_BIO_HEALTHCARE_MEDICAL | C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT | MEDICAL_AI_REIMBURSEMENT_AND_DEVICE_EXPORT_COMMERCIALIZATION_GATE | 2 | 2 | 2 | 1 | 4 | 0 | 6 | 4 | 2 | true | true | still needs dental implant/export reimbursement holdout and device-tender-cap cases |

## 22. Residual Contribution Summary

```text
new_independent_case_count: 4
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 4
same_archetype_new_symbol_count: 4
same_archetype_new_trigger_family_count: 4
new_canonical_archetype_count: 0
new_fine_archetype_count: 3
new_trigger_family_count: 4
positive_case_count: 2
counterexample_count: 2
current_profile_error_count: 2
tested_existing_calibrated_axes: [stage2_actionable_evidence_bonus, stage3_green_revision_min, price_only_blowoff_blocks_positive_stage, full_4b_requires_non_price_evidence, hard_4c_thesis_break_routes_to_4c]
residual_error_types_found: [late_reimbursement_narrative_false_green, robot_order_high_mae_rerating, C25_green_without_usage_bridge]
new_axis_proposed: [C25_commercial_followthrough_bonus, C25_late_reimbursement_narrative_guard, C25_robot_or_device_order_execution_guard]
existing_axis_strengthened: [price_only_blowoff_blocks_positive_stage, full_4b_requires_non_price_evidence, hard_4c_thesis_break_routes_to_4c]
existing_axis_weakened: []
existing_axis_kept: [stage2_actionable_evidence_bonus, stage3_yellow_total_min, stage3_green_total_min, stage3_green_revision_min, stage3_cross_evidence_green_buffer]
sector_specific_rule_candidate: true
canonical_archetype_rule_candidate: true
no_new_signal_reason: null
loop_contribution_label: canonical_archetype_rule_candidate
do_not_propose_new_weight_delta: false
auto_selected_coverage_gap: R7 C25 lacked balanced positive/counterexample medical-device export/reimbursement residual rows after C24 trial-data work
```

## 23. Validation Scope / Non-Validation Scope

Validated:

```text
- Songdaiki/stock-web manifest max_date and shard roots
- symbol profile availability and corporate-action candidate dates
- trigger entry_date and entry_price from tradable shard
- 30D/90D/180D MFE/MAE proxy calculations from stock-web OHLC rows
- same_entry_group_id and representative-vs-overlay dedupe logic
- current calibrated profile stress-test verdicts
```

Not validated in this file:

```text
- exact article timestamp to minute-level precision
- full external article/PDF text extraction
- stock_agent production scoring code
- live candidate scan
- brokerage or auto-trading path
- production scoring patch
```

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,C25_commercial_followthrough_bonus,canonical_archetype_specific,L7_BIO_HEALTHCARE_MEDICAL,C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT,0,1,+1,"Usage/reimbursement/export conversion separated VUNO and CLASSYS from late narrative rows","Improved false positive rate while preserving positives","C25_VUNO_S2A_20230601|C25_CLASSYS_S2A_20230810",4,4,2,medium,archetype_shadow_only,"not production; post-calibrated residual"
shadow_weight,C25_late_reimbursement_narrative_guard,canonical_archetype_specific,L7_BIO_HEALTHCARE_MEDICAL,C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT,0,1,+1,"JLK shows late reimbursement narrative plus relative strength can be false Green","Blocks shallow MFE / high MAE rows","C25_JLK_FALSE_GREEN_20230810",4,4,2,medium,archetype_shadow_only,"not production; guard-only unless promoted"
shadow_weight,C25_robot_or_device_order_execution_guard,sector_specific,L7_BIO_HEALTHCARE_MEDICAL,C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT,0,1,+1,"CUREXO shows order/export headline needs recurring utilization and margin bridge","Downgrades high-MAE robot/order rerating to watch","C25_CUREXO_S2A_20230626|C25_CUREXO_4B_20230824",4,4,2,low,sector_shadow_only,"needs more robot/dental/device export cases"
```

## 25. Machine-Readable Rows

### 25.1 price_source_validation

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
```

### 25.2 case rows

```jsonl
{"row_type":"case","case_id":"C25_R7L16_VUNO_20230602","symbol":"338220","company_name":"뷰노","round":"R7","loop":"16","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT","fine_archetype_id":"MEDICAL_AI_REIMBURSEMENT_AND_USAGE_RAMP","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"C25_VUNO_S2A_20230601","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"aligned_positive","current_profile_verdict":"current_profile_correct","price_source":"Songdaiki/stock-web","notes":"Reimbursement/clinical-use adoption path; late Green materially worse than Stage2 entry."}
{"row_type":"case","case_id":"C25_R7L16_CLASSYS_20230810","symbol":"214150","company_name":"클래시스","round":"R7","loop":"16","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT","fine_archetype_id":"AESTHETIC_DEVICE_EXPORT_MARGIN_BRIDGE","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"C25_CLASSYS_S2A_20230810","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"aligned_positive","current_profile_verdict":"current_profile_correct","price_source":"Songdaiki/stock-web","notes":"Export/margin bridge converted into durable follow-through."}
{"row_type":"case","case_id":"C25_R7L16_JLK_20230810","symbol":"322510","company_name":"제이엘케이","round":"R7","loop":"16","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT","fine_archetype_id":"MEDICAL_AI_REIMBURSEMENT_LATE_FALSE_GREEN","case_type":"false_positive_green","positive_or_counterexample":"counterexample","best_trigger":"C25_JLK_FALSE_GREEN_20230810","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"false_positive_blocked","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"Late reimbursement/AI narrative after parabolic move had weak forward MFE and severe MAE."}
{"row_type":"case","case_id":"C25_R7L16_CUREXO_20230626","symbol":"060280","company_name":"큐렉소","round":"R7","loop":"16","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT","fine_archetype_id":"SURGICAL_ROBOT_EXPORT_EXECUTION_RISK","case_type":"failed_rerating","positive_or_counterexample":"counterexample","best_trigger":"C25_CUREXO_S2A_20230626","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"high_mae_guarded","current_profile_verdict":"current_profile_too_early","price_source":"Songdaiki/stock-web","notes":"Robot/order narrative had high MFE but poor stability; execution and margin guard needed."}
```

### 25.3 trigger rows

```jsonl
{"row_type":"trigger","trigger_id":"C25_VUNO_S2A_20230601","case_id":"C25_R7L16_VUNO_20230602","symbol":"338220","company_name":"뷰노","round":"R7","loop":"16","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT","fine_archetype_id":"MEDICAL_AI_REIMBURSEMENT_AND_USAGE_RAMP","sector":"bio_healthcare_medical","primary_archetype":"medical_ai_reimbursement_usage_ramp","loop_objective":"sector_specific_rule_discovery;counterexample_mining;coverage_gap_fill","trigger_type":"Stage2-Actionable","trigger_date":"2023-06-01","evidence_available_at_that_date":"Medical-AI reimbursement/adoption and early commercial-use ramp were publicly visible before the 2023-06-02 entry.","evidence_source":"public disclosure/news/IR title-level mapping; stock-web used for price only","stage2_evidence_fields":["public_event_or_disclosure","policy_or_regulatory_optionality","early_revision_signal","customer_or_order_quality"],"stage3_evidence_fields":["multiple_public_sources","financial_visibility_watch"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/338/338220/2023.csv","profile_path":"atlas/symbol_profiles/338/338220.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2023-06-02","entry_price":23650,"MFE_30D_pct":72.09,"MFE_90D_pct":193.87,"MFE_180D_pct":193.87,"MFE_1Y_pct":193.87,"MFE_2Y_pct":null,"MAE_30D_pct":-15.22,"MAE_90D_pct":-15.22,"MAE_180D_pct":-15.22,"MAE_1Y_pct":-15.22,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2023-09-07","peak_price":69500,"drawdown_after_peak_pct":-65.61,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_4B_entry","four_b_evidence_type":[],"four_c_protection_label":"not_applicable","trigger_outcome_label":"structural_success","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C25_R7L16_VUNO_20230602__2023-06-02__23650","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"C25_VUNO_GREEN_COMPARE_20230829","case_id":"C25_R7L16_VUNO_20230602","symbol":"338220","company_name":"뷰노","round":"R7","loop":"16","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT","fine_archetype_id":"MEDICAL_AI_REIMBURSEMENT_AND_USAGE_RAMP","sector":"bio_healthcare_medical","primary_archetype":"medical_ai_reimbursement_usage_ramp","loop_objective":"green_strictness_stress_test","trigger_type":"Stage3-Green","trigger_date":"2023-08-29","evidence_available_at_that_date":"Late confirmation after a large non-price and price rerating; used for Green lateness comparison only.","evidence_source":"public disclosure/news/IR title-level mapping; stock-web used for price only","stage2_evidence_fields":["public_event_or_disclosure","relative_strength"],"stage3_evidence_fields":["multiple_public_sources","financial_visibility_watch"],"stage4b_evidence_fields":["valuation_blowoff","positioning_overheat"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/338/338220/2023.csv","profile_path":"atlas/symbol_profiles/338/338220.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2023-08-29","entry_price":50100,"MFE_30D_pct":38.72,"MFE_90D_pct":38.72,"MFE_180D_pct":38.72,"MFE_1Y_pct":38.72,"MFE_2Y_pct":null,"MAE_30D_pct":-22.85,"MAE_90D_pct":-50.10,"MAE_180D_pct":-50.10,"MAE_1Y_pct":-50.10,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2023-09-07","peak_price":69500,"drawdown_after_peak_pct":-65.61,"green_lateness_ratio":0.577,"four_b_local_peak_proximity":0.91,"four_b_full_window_peak_proximity":0.91,"four_b_timing_verdict":"late_green_but_not_full_4B_without_non_price_fatigue","four_b_evidence_type":["valuation_blowoff","positioning_overheat"],"four_c_protection_label":"not_applicable","trigger_outcome_label":"late_green_with_high_drawdown","current_profile_verdict":"current_profile_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C25_R7L16_VUNO_20230602__2023-08-29__50100","dedupe_for_aggregate":false,"aggregate_group_role":"label_comparison_only","is_new_independent_case":false,"reuse_reason":"same_case_green_lateness_comparison","independent_evidence_weight":0.25,"do_not_count_as_new_case":true}
{"row_type":"trigger","trigger_id":"C25_CLASSYS_S2A_20230810","case_id":"C25_R7L16_CLASSYS_20230810","symbol":"214150","company_name":"클래시스","round":"R7","loop":"16","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT","fine_archetype_id":"AESTHETIC_DEVICE_EXPORT_MARGIN_BRIDGE","sector":"bio_healthcare_medical","primary_archetype":"aesthetic_device_export_margin_bridge","loop_objective":"sector_specific_rule_discovery;coverage_gap_fill","trigger_type":"Stage2-Actionable","trigger_date":"2023-08-10","evidence_available_at_that_date":"Export/margin bridge was visible through earnings/IR/news flow.","evidence_source":"earnings/IR/news title-level mapping; stock-web used for price only","stage2_evidence_fields":["public_event_or_disclosure","customer_or_order_quality","early_revision_signal","backlog_or_delivery_visibility"],"stage3_evidence_fields":["margin_bridge","financial_visibility","repeat_order_or_conversion"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/214/214150/2023.csv","profile_path":"atlas/symbol_profiles/214/214150.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2023-08-10","entry_price":34900,"MFE_30D_pct":20.34,"MFE_90D_pct":23.35,"MFE_180D_pct":45.56,"MFE_1Y_pct":63.04,"MFE_2Y_pct":null,"MAE_30D_pct":-7.45,"MAE_90D_pct":-9.60,"MAE_180D_pct":-20.20,"MAE_1Y_pct":-20.20,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-06-19","peak_price":56900,"drawdown_after_peak_pct":-17.93,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_4B_entry","four_b_evidence_type":[],"four_c_protection_label":"not_applicable","trigger_outcome_label":"structural_success","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C25_R7L16_CLASSYS_20230810__2023-08-10__34900","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"C25_JLK_FALSE_GREEN_20230810","case_id":"C25_R7L16_JLK_20230810","symbol":"322510","company_name":"제이엘케이","round":"R7","loop":"16","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT","fine_archetype_id":"MEDICAL_AI_REIMBURSEMENT_LATE_FALSE_GREEN","sector":"bio_healthcare_medical","primary_archetype":"medical_ai_reimbursement_late_false_green","loop_objective":"counterexample_mining;green_strictness_stress_test;4C_thesis_break_timing_test","trigger_type":"Stage3-Green-candidate","trigger_date":"2023-08-10","evidence_available_at_that_date":"Reimbursement/AI narrative was visible, but the move had already become highly valuation-sensitive.","evidence_source":"company/news title-level mapping; stock-web used for price only","stage2_evidence_fields":["public_event_or_disclosure","policy_or_regulatory_optionality","relative_strength"],"stage3_evidence_fields":["multiple_public_sources"],"stage4b_evidence_fields":["valuation_blowoff","positioning_overheat"],"stage4c_evidence_fields":["thesis_evidence_broken"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/322/322510/2023.csv","profile_path":"atlas/symbol_profiles/322/322510.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2023-08-10","entry_price":35900,"MFE_30D_pct":8.77,"MFE_90D_pct":8.77,"MFE_180D_pct":8.77,"MFE_1Y_pct":8.77,"MFE_2Y_pct":null,"MAE_30D_pct":-25.21,"MAE_90D_pct":-54.74,"MAE_180D_pct":-74.96,"MAE_1Y_pct":-74.96,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2023-08-11","peak_price":39050,"drawdown_after_peak_pct":-76.98,"green_lateness_ratio":1.0,"four_b_local_peak_proximity":0.87,"four_b_full_window_peak_proximity":0.87,"four_b_timing_verdict":"late_green_should_be_4B_watch_or_blocked","four_b_evidence_type":["valuation_blowoff","positioning_overheat"],"four_c_protection_label":"hard_4c_success","trigger_outcome_label":"false_positive_green","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C25_R7L16_JLK_20230810__2023-08-10__35900","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"C25_CUREXO_S2A_20230626","case_id":"C25_R7L16_CUREXO_20230626","symbol":"060280","company_name":"큐렉소","round":"R7","loop":"16","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT","fine_archetype_id":"SURGICAL_ROBOT_EXPORT_EXECUTION_RISK","sector":"bio_healthcare_medical","primary_archetype":"surgical_robot_export_execution_risk","loop_objective":"counterexample_mining;4B_non_price_requirement_stress_test;coverage_gap_fill","trigger_type":"Stage2-Actionable","trigger_date":"2023-06-26","evidence_available_at_that_date":"Surgical robot export/order narrative visible, but recurring utilization and margin bridge remained unconfirmed.","evidence_source":"company/news/disclosure title-level mapping; stock-web used for price only","stage2_evidence_fields":["public_event_or_disclosure","customer_or_order_quality","backlog_or_delivery_visibility","relative_strength"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["positioning_overheat","execution_risk"],"stage4c_evidence_fields":["thesis_evidence_broken"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/060/060280/2023.csv","profile_path":"atlas/symbol_profiles/060/060280.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2023-06-26","entry_price":17500,"MFE_30D_pct":30.00,"MFE_90D_pct":47.14,"MFE_180D_pct":47.14,"MFE_1Y_pct":47.14,"MFE_2Y_pct":null,"MAE_30D_pct":-18.91,"MAE_90D_pct":-24.29,"MAE_180D_pct":-25.83,"MAE_1Y_pct":-25.83,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2023-08-24","peak_price":25750,"drawdown_after_peak_pct":-49.59,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"high_MAE_success_needs_execution_guard","four_b_evidence_type":["positioning_overheat","execution_risk"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"failed_rerating_high_mae","current_profile_verdict":"current_profile_too_early","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C25_R7L16_CUREXO_20230626__2023-06-26__17500","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"C25_CUREXO_4B_20230824","case_id":"C25_R7L16_CUREXO_20230626","symbol":"060280","company_name":"큐렉소","round":"R7","loop":"16","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT","fine_archetype_id":"SURGICAL_ROBOT_EXPORT_EXECUTION_RISK","sector":"bio_healthcare_medical","primary_archetype":"surgical_robot_export_execution_risk","loop_objective":"4B_non_price_requirement_stress_test","trigger_type":"4B-overlay","trigger_date":"2023-08-24","evidence_available_at_that_date":"Local blowoff/positioning overheat after robot-order narrative; full 4B requires non-price fatigue confirmation.","evidence_source":"stock-web price + narrative risk overlay; no positive entry training","stage2_evidence_fields":[],"stage3_evidence_fields":[],"stage4b_evidence_fields":["price_only_local_peak","positioning_overheat","execution_risk"],"stage4c_evidence_fields":["thesis_evidence_broken"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/060/060280/2023.csv","profile_path":"atlas/symbol_profiles/060/060280.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2023-08-24","entry_price":24400,"MFE_30D_pct":5.53,"MFE_90D_pct":5.53,"MFE_180D_pct":5.53,"MFE_1Y_pct":5.53,"MFE_2Y_pct":null,"MAE_30D_pct":-19.75,"MAE_90D_pct":-46.80,"MAE_180D_pct":-46.80,"MAE_1Y_pct":-46.80,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2023-08-24","peak_price":25750,"drawdown_after_peak_pct":-49.59,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":0.84,"four_b_full_window_peak_proximity":0.84,"four_b_timing_verdict":"4B_watch_not_positive_training","four_b_evidence_type":["price_only","positioning_overheat","execution_risk"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"4B_overlay_success","current_profile_verdict":"current_profile_4B_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C25_R7L16_CUREXO_20230626__2023-08-24__24400","dedupe_for_aggregate":false,"aggregate_group_role":"4B_overlay_only","is_new_independent_case":false,"reuse_reason":"same_case_4B_overlay","independent_evidence_weight":0.25,"do_not_count_as_new_case":true}
```

### 25.4 score_simulation rows

```jsonl
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C25_R7L16_VUNO_20230602","trigger_id":"C25_VUNO_S2A_20230601","symbol":"338220","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT","raw_component_scores_before":{"contract_score":20,"backlog_visibility_score":10,"margin_bridge_score":20,"revision_score":45,"relative_strength_score":70,"customer_quality_score":65,"policy_or_regulatory_score":75,"valuation_repricing_score":50,"execution_risk_score":35,"legal_or_contract_risk_score":10,"dilution_cb_risk_score":10,"accounting_trust_risk_score":10},"weighted_score_before":79.0,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":20,"backlog_visibility_score":15,"margin_bridge_score":25,"revision_score":50,"relative_strength_score":70,"customer_quality_score":70,"policy_or_regulatory_score":82,"valuation_repricing_score":50,"execution_risk_score":35,"legal_or_contract_risk_score":10,"dilution_cb_risk_score":10,"accounting_trust_risk_score":10,"commercial_usage_score":75},"weighted_score_after":82.0,"stage_label_after":"Stage2-Actionable/Yellow+","changed_components":["policy_or_regulatory_score","commercial_usage_score","customer_quality_score"],"component_delta_explanation":"C25 commercial usage/reimbursement conversion bonus added.","MFE_90D_pct":193.87,"MAE_90D_pct":-15.22,"score_return_alignment_label":"aligned_positive","current_profile_verdict":"current_profile_correct"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C25_R7L16_CLASSYS_20230810","trigger_id":"C25_CLASSYS_S2A_20230810","symbol":"214150","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT","raw_component_scores_before":{"contract_score":30,"backlog_visibility_score":55,"margin_bridge_score":70,"revision_score":55,"relative_strength_score":55,"customer_quality_score":70,"policy_or_regulatory_score":35,"valuation_repricing_score":55,"execution_risk_score":25,"legal_or_contract_risk_score":10,"dilution_cb_risk_score":5,"accounting_trust_risk_score":10},"weighted_score_before":82.0,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":35,"backlog_visibility_score":65,"margin_bridge_score":78,"revision_score":62,"relative_strength_score":55,"customer_quality_score":75,"policy_or_regulatory_score":35,"valuation_repricing_score":55,"execution_risk_score":22,"legal_or_contract_risk_score":10,"dilution_cb_risk_score":5,"accounting_trust_risk_score":10,"export_reorder_score":72},"weighted_score_after":86.0,"stage_label_after":"Stage3-Yellow+","changed_components":["margin_bridge_score","backlog_visibility_score","export_reorder_score"],"component_delta_explanation":"Export and margin bridge improve C25 confidence without bypassing Green revision gate.","MFE_90D_pct":23.35,"MAE_90D_pct":-9.60,"score_return_alignment_label":"aligned_positive","current_profile_verdict":"current_profile_correct"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C25_R7L16_JLK_20230810","trigger_id":"C25_JLK_FALSE_GREEN_20230810","symbol":"322510","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT","raw_component_scores_before":{"contract_score":10,"backlog_visibility_score":10,"margin_bridge_score":10,"revision_score":25,"relative_strength_score":90,"customer_quality_score":55,"policy_or_regulatory_score":75,"valuation_repricing_score":90,"execution_risk_score":70,"legal_or_contract_risk_score":10,"dilution_cb_risk_score":20,"accounting_trust_risk_score":10},"weighted_score_before":88.0,"stage_label_before":"Stage3-Green","raw_component_scores_after":{"contract_score":10,"backlog_visibility_score":10,"margin_bridge_score":10,"revision_score":20,"relative_strength_score":50,"customer_quality_score":45,"policy_or_regulatory_score":65,"valuation_repricing_score":95,"execution_risk_score":80,"legal_or_contract_risk_score":10,"dilution_cb_risk_score":20,"accounting_trust_risk_score":10,"commercial_usage_score":20},"weighted_score_after":73.0,"stage_label_after":"Stage2-watch/4B-watch","changed_components":["relative_strength_score","execution_risk_score","commercial_usage_score"],"component_delta_explanation":"Late reimbursement narrative lacks commercial conversion and is blocked from Green.","MFE_90D_pct":8.77,"MAE_90D_pct":-54.74,"score_return_alignment_label":"false_positive_blocked","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C25_R7L16_CUREXO_20230626","trigger_id":"C25_CUREXO_S2A_20230626","symbol":"060280","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT","raw_component_scores_before":{"contract_score":60,"backlog_visibility_score":45,"margin_bridge_score":15,"revision_score":25,"relative_strength_score":80,"customer_quality_score":55,"policy_or_regulatory_score":35,"valuation_repricing_score":85,"execution_risk_score":75,"legal_or_contract_risk_score":10,"dilution_cb_risk_score":10,"accounting_trust_risk_score":10},"weighted_score_before":78.0,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"contract_score":55,"backlog_visibility_score":40,"margin_bridge_score":10,"revision_score":20,"relative_strength_score":55,"customer_quality_score":50,"policy_or_regulatory_score":35,"valuation_repricing_score":90,"execution_risk_score":85,"legal_or_contract_risk_score":10,"dilution_cb_risk_score":10,"accounting_trust_risk_score":10,"robot_execution_score":25},"weighted_score_after":70.0,"stage_label_after":"Stage2-watch","changed_components":["relative_strength_score","execution_risk_score","robot_execution_score"],"component_delta_explanation":"Robot order headline downgraded until recurring utilization and margin bridge exist.","MFE_90D_pct":47.14,"MAE_90D_pct":-24.29,"score_return_alignment_label":"high_mae_guarded","current_profile_verdict":"current_profile_too_early"}
```

### 25.5 shadow_weight row

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,C25_commercial_followthrough_bonus,canonical_archetype_specific,L7_BIO_HEALTHCARE_MEDICAL,C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT,0,1,+1,"Positive C25 rows require reimbursed usage/export reorder/margin bridge, not headline alone","Preserves VUNO/CLASSYS positives","C25_VUNO_S2A_20230601|C25_CLASSYS_S2A_20230810",4,4,2,medium,archetype_shadow_only,"not production; post-calibrated residual"
shadow_weight,C25_late_reimbursement_narrative_guard,canonical_archetype_specific,L7_BIO_HEALTHCARE_MEDICAL,C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT,0,1,+1,"JLK shows late narrative plus relative strength can become false Green","Blocks shallow MFE/high MAE rows","C25_JLK_FALSE_GREEN_20230810",4,4,2,medium,archetype_shadow_only,"not production; guard-only"
shadow_weight,C25_robot_or_device_order_execution_guard,sector_specific,L7_BIO_HEALTHCARE_MEDICAL,C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT,0,1,+1,"CUREXO shows robot/order headline needs execution and margin validation","Downgrades high-MAE order rerating to watch","C25_CUREXO_S2A_20230626|C25_CUREXO_4B_20230824",4,4,2,low,sector_shadow_only,"needs more device-order holdouts"
```

### 25.6 residual_contribution row

```jsonl
{"row_type":"residual_contribution","round":"R7","loop":"16","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT","new_independent_case_count":4,"reused_case_count":0,"new_symbol_count":4,"same_archetype_new_symbol_count":4,"same_archetype_new_trigger_family_count":4,"new_canonical_archetype_count":0,"new_trigger_family_count":4,"positive_case_count":2,"counterexample_count":2,"current_profile_error_count":2,"diversity_score_summary":"avg 20.5; new symbols 4, counterexamples 2, no reused triggers","tested_existing_calibrated_axes":["stage2_actionable_evidence_bonus","stage3_green_revision_min","price_only_blowoff_blocks_positive_stage","full_4b_requires_non_price_evidence","hard_4c_thesis_break_routes_to_4c"],"residual_error_types_found":["late_reimbursement_narrative_false_green","robot_order_high_mae_rerating","C25_green_without_usage_bridge"],"loop_contribution_label":"canonical_archetype_rule_candidate","do_not_propose_new_weight_delta":false,"auto_selected_coverage_gap":"R7 C25 medical device export/reimbursement needed positive/counterexample balance after C24 loop"}
```

### 25.7 narrative_only row

```jsonl
{"row_type":"narrative_only","case_id":"C25_R7L16_EXTERNAL_TEXT_RECHECK","symbol":"MULTI","large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT","reason":"External article/PDF text was not fully re-extracted in this shadow-only loop; exact event timestamps should be rechecked before production promotion.","price_source":"Songdaiki/stock-web","usage":"not_weight_calibration"}
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
11. For this specific MD, re-check external event timestamps before promoting C25 rules beyond shadow.

### Expected output

- Concise implementation summary.
- Rows accepted/rejected.
- New sector/canonical archetype coverage.
- Existing axis strengthened/weakened/kept.
- No investment recommendation language.

## 27. Next Round State

```text
next_round = R7_loop_17_C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT_holdout_or_R7_loop_18_C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION
priority_next = add dental implant / diagnostic device export reimbursement holdout; add failed FDA/approval-to-commercialization counterexample
```

## 28. Source Notes

Stock-web files used:

```text
atlas/manifest.json
atlas/symbol_profiles/338/338220.json
atlas/symbol_profiles/214/214150.json
atlas/symbol_profiles/322/322510.json
atlas/symbol_profiles/060/060280.json
atlas/ohlcv_tradable_by_symbol_year/338/338220/2023.csv
atlas/ohlcv_tradable_by_symbol_year/214/214150/2023.csv
atlas/ohlcv_tradable_by_symbol_year/214/214150/2024.csv
atlas/ohlcv_tradable_by_symbol_year/322/322510/2023.csv
atlas/ohlcv_tradable_by_symbol_year/322/322510/2024.csv
atlas/ohlcv_tradable_by_symbol_year/060/060280/2023.csv
```

External evidence text was not used as a price substitute. It was used only as title-level event-family mapping. Price metrics come from stock-web tradable OHLC rows.
