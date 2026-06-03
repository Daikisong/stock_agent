# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata
- output_file: `e2r_stock_web_v12_residual_round_R7_loop_14_L7_BIO_HEALTHCARE_MEDICAL_C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION_research.md`
- scheduled_round: R7
- scheduled_loop: 14
- completed_round: R7
- completed_loop: 14
- research_session: post_calibrated_sector_archetype_residual_research
- mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
- live_candidate_mode: false
- stock_agent_code_access_allowed: false
- production_scoring_changed: false
- shadow_weight_only: true
- handoff_prompt_embedded: true
- handoff_prompt_executed_now: false

## 1. Current Calibrated Profile Assumption
The active proxy is `e2r_2_1_stock_web_calibrated_proxy`, with the already-applied global gates treated as fixed. This loop does not re-prove the Stage2 bonus or price-only blowoff guard; it stress-tests C23-specific regulatory/commercialization residue.

Tested existing axes: `stage2_actionable_evidence_bonus`, `stage3_yellow_total_min`, `stage3_green_total_min`, `full_4b_requires_non_price_evidence`, `hard_4c_thesis_break_routes_to_4c`.

## 2. Round / Large Sector / Canonical Archetype Scope
- round: R7
- loop: 14
- large_sector_id: `L7_BIO_HEALTHCARE_MEDICAL`
- canonical_archetype_id: `C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION`
- fine_archetype_id: `ONCOLOGY_REGULATORY_APPROVAL_COMMERCIALIZATION_AND_FORMULATION_EVENT_RISK`
- loop_objective: coverage_gap_fill / counterexample_mining / canonical_archetype_compression / 4B_non_price_requirement_stress_test / 4C_thesis_break_timing_test
- round_schedule_status: valid
- round_sector_consistency: pass

## 3. Previous Coverage / Duplicate Avoidance Check
The previous generated file ended at R6 Loop 14 and pointed to R7 Loop 14. Because direct `stock_agent` code access is prohibited, this run uses the previous next-round state and avoids `src/e2r` entirely. Within R7, C23 is selected because approval/commercialization and follow-on regulatory delay create a clean positive/counterexample balance.

Duplicate guard result: no same symbol + same trigger date + same entry date + same evidence family is repeated. One Yuhan row reuses the symbol, but it is a distinct trigger family: initial FDA approval rerating versus follow-on subcutaneous formulation CRL overlay.

## 4. Stock-Web OHLC Input / Price Source Validation
Stock-Web manifest validation: source is FinanceData/marcap, price adjustment is raw_unadjusted_marcap, min_date is 1995-05-02, max_date is 2026-02-20, calibration shard root is `atlas/ohlcv_tradable_by_symbol_year`, and raw rows are preserved under `atlas/ohlcv_raw_by_symbol_year`. Manifest notes state that raw/unadjusted OHLC is used, zero-volume/zero-OHLC rows are excluded from calibration shards, and corporate-action-contaminated windows are blocked by default. fileciteturn994file0L3-L60

Schema validation: tradable shard columns are `d,o,h,l,c,v,a,mc,s,m`; MFE/MAE definitions use max high / min low from entry date through N tradable rows; calibration requires positive OHLC/volume, entry row existence, at least 180 forward tradable days, and no 180D corporate-action contamination. fileciteturn975file0L17-L28 fileciteturn975file0L60-L69

## 5. Historical Eligibility Gate
| case_id | symbol | entry_date | 180D available by stock-web max_date | corp-action 180D status | calibration_usable |
|---|---:|---:|---:|---|---:|
| R7L14-C23-000100-LAZERTINIB-US-APPROVAL | 000100 | 2024-08-21 | yes | clean_180D_window | true |
| R7L14-C23-196170-KEYTRUDA-SC-COMMERCIALIZATION | 196170 | 2025-03-27 | yes | clean_180D_window | true |
| R7L14-C23-028300-HCC-NDA-CRL | 028300 | 2024-05-17 | yes | clean_180D_window | true |
| R7L14-C23-000100-SC-FORMULATION-CRL | 000100 | 2024-12-17 | yes | clean_180D_window | true |
| R7L14-C23-068270-ZYMFENTRA-FDA-APPROVAL | 068270 | 2023-10-23 | yes | blocked_by_2024-01-12_profile_corp_action | false |

Celltrion is included only as narrative coverage because its profile flags a 2024-01-12 corporate-action candidate inside the forward window. fileciteturn1004file0L9-L19

## 6. Canonical Archetype Compression Map
| fine_archetype | canonical_archetype_id | compression note |
|---|---|---|
| `ONCOLOGY_REGULATORY_APPROVAL_COMMERCIALIZATION_AND_FORMULATION_EVENT_RISK` | `C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION` | compresses FDA approval, global-partner commercialization route, core NDA rejection, and follow-on formulation/manufacturing CRL into one C23 rule family |

## 7. Case Selection Summary
| case_id | symbol | company | role | trigger_family | why selected |
|---|---:|---|---|---|---|
| R7L14-C23-000100-LAZERTINIB-US-APPROVAL | 000100 | 유한양행 | positive | Stage3-Green | approval_to_rerating_success_high_MFE_then_drawdown |
| R7L14-C23-196170-KEYTRUDA-SC-COMMERCIALIZATION | 196170 | 알테오젠 | positive | Stage2-Actionable | commercialization_route_success_with_moderate_MAE |
| R7L14-C23-028300-HCC-NDA-CRL | 028300 | HLB | counterexample | 4C | regulatory_rejection_crash_then_speculative_rebound |
| R7L14-C23-000100-SC-FORMULATION-CRL | 000100 | 유한양행 | counterexample | 4B-overlay | formulation_crl_high_MAE_but_not_core_thesis_break |

## 8. Positive vs Counterexample Balance
- positive_case_count: 2
- counterexample_count: 2
- calibration_usable_case_count: 4
- narrative_only_count: 1
- 4B_case_count: 1
- 4C_case_count: 1

## 9. Evidence Source Map
| trigger_id | evidence source | timing rule | source confidence |
|---|---|---|---|
| R7L14-C23-000100-FDA-APPROVAL-20240820 | Reuters reported FDA approval of Rybrevant + lazertinib for first-line EGFR-mutated NSCLC on 2024-08-20. citeturn209931view0 | next day close because U.S. article timing and Korea market timing differ | high |
| R7L14-C23-196170-MERCK-SC-LAUNCH-20250327 | Reuters reported Merck's planned U.S. launch timing, FDA target date, adoption expectations, and Alteogen enzyme role. citeturn209931view1 | same-day close | high |
| R7L14-C23-028300-FDA-CRL-20240517 | HLB/Elevar CRL event; specific source retrieval was incomplete in this run; CRL concept verified separately. citeturn209931view4 | same-day close because Korean market repriced immediately | medium |
| R7L14-C23-000100-RYBREVANT-SC-CRL-20241217 | Reuters reported FDA declined injectable Rybrevant, tied to manufacturing inspection and not formulation/efficacy; no additional clinical studies requested. citeturn209931view3 | same-day close | high |
| R7L14-C23-068270-ZYMFENTRA-FDA-APPROVAL | Zymfentra FDA approval is a known Celltrion event, but row is narrative-only due corporate-action contamination | next trading day close | blocked |

## 10. Price Data Source Map
| symbol | profile_path | profile status | price_shards used |
|---:|---|---|---|
| 000100 | atlas/symbol_profiles/000/000100.json | active_like; corporate-action candidates not in 2024-2025 trigger windows. fileciteturn1000file0L26-L42 | 2024, 2025 |
| 196170 | atlas/symbol_profiles/196/196170.json | active_like; no 2024-2025 corporate-action candidates. fileciteturn1009file0L116-L133 | 2024, 2025 |
| 028300 | atlas/symbol_profiles/028/028300.json | active_like; no 2024 corporate-action candidate in trigger window. fileciteturn1007file0L16-L46 | 2024 |
| 068270 | atlas/symbol_profiles/068/068270.json | blocked for this entry because 2024-01-12 candidate falls in 180D window. fileciteturn1004file0L9-L19 | 2023/2024 narrative only |

## 11. Case-by-Case Trigger Grid
| trigger_id | trigger_type | trigger_date | entry_date | entry_price | stage2_fields | stage3_fields | 4B_fields | 4C_fields | current_profile_verdict |
|---|---|---:|---:|---:|---|---|---|---|---|
| R7L14-C23-000100-FDA-APPROVAL-20240820 | Stage3-Green | 2024-08-20 | 2024-08-21 | 94300 | public_event_or_disclosure, customer_or_order_quality, policy_or_regulatory_optionality | confirmed_revision, multiple_public_sources, financial_visibility, durable_customer_confirmation |  |  | current_profile_too_late |
| R7L14-C23-196170-MERCK-SC-LAUNCH-20250327 | Stage2-Actionable | 2025-03-27 | 2025-03-27 | 352000 | public_event_or_disclosure, customer_or_order_quality, policy_or_regulatory_optionality, early_revision_signal | financial_visibility, durable_customer_confirmation | positioning_overheat |  | current_profile_correct |
| R7L14-C23-028300-FDA-CRL-20240517 | 4C | 2024-05-17 | 2024-05-17 | 67100 | public_event_or_disclosure, policy_or_regulatory_optionality |  | explicit_event_cap, legal_or_regulatory_block | regulatory_rejection, thesis_evidence_broken | current_profile_4C_too_late |
| R7L14-C23-000100-RYBREVANT-SC-CRL-20241217 | 4B-overlay | 2024-12-17 | 2024-12-17 | 112800 | public_event_or_disclosure, policy_or_regulatory_optionality |  | legal_or_regulatory_block, contract_delay, explicit_event_cap |  | current_profile_4C_too_late |

## 12. Trigger-Level OHLC Backtest Tables
The entry rows and key forward prices are taken from Stock-Web tradable shards. For example, Yuhan's 2024-08-21 entry row, the late-August and September peaks, and subsequent drawdown are visible in the 000100 2024 shard. fileciteturn1001file0L11-L35 HLB's 2024-05-17 crash row and the rebound path are visible in the 028300 2024 shard. fileciteturn1008file0L10-L45 Alteogen's March-to-September 2025 commercialization path is visible in the 196170 2025 shard. fileciteturn1011file0L3-L55 fileciteturn1012file0L7-L62

| trigger_id | entry_price | MFE_30D | MAE_30D | MFE_90D | MAE_90D | MFE_180D | MAE_180D | peak_date | peak_price | drawdown_after_peak |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| R7L14-C23-000100-FDA-APPROVAL-20240820 | 94300 | 69.99 | -2.97 | 76.99 | -2.97 | 76.99 | -14.1 | 2024-10-15 | 166900 | -51.47 |
| R7L14-C23-196170-MERCK-SC-LAUNCH-20250327 | 352000 | 13.49 | -6.96 | 44.32 | -10.37 | 50.28 | -10.37 | 2025-09-22 | 529000 | -15.88 |
| R7L14-C23-028300-FDA-CRL-20240517 | 67100 | 9.99 | -32.71 | 46.2 | -32.71 | 46.2 | -32.71 | 2024-07-08 | 98100 | -45.46 |
| R7L14-C23-000100-RYBREVANT-SC-CRL-20241217 | 112800 | 8.6 | -28.19 | 8.6 | -28.19 | 8.6 | -28.19 | 2024-12-30 | 122500 | -33.88 |

## 13. Current Calibrated Profile Stress Test
| case_id | current_profile_verdict | stress-test conclusion |
|---|---|---|
| R7L14-C23-000100-LAZERTINIB-US-APPROVAL | current_profile_too_late | Green threshold captures confirmation, but the first tradable post-approval rerating already consumed a large portion of upside; C23 needs approval-plus-global-partner bonus before final revision print. |
| R7L14-C23-196170-KEYTRUDA-SC-COMMERCIALIZATION | current_profile_correct | Stage2-Actionable is correct: not yet approved, but global partner + launch plan + peak adoption estimate creates enough commercialization visibility. |
| R7L14-C23-028300-HCC-NDA-CRL | current_profile_4C_too_late | Core regulatory rejection is not mere 4B; hard 4C should route immediately when the actual approval thesis breaks. |
| R7L14-C23-000100-SC-FORMULATION-CRL | current_profile_4C_too_late | The event is non-price/non-clinical risk but not core thesis break; should be 4B-watch, not hard 4C. |

Axis answers:
1. Stage2 bonus is not generally too high; it is still under-specified for named global partner launch paths.
2. Yellow threshold 75 is acceptable but needs C23 component shape, not a lower global threshold.
3. Green threshold 87 / revision 55 is too late for already regulator-confirmed oncology approvals with explicit commercial partner economics.
4. price-only blowoff guard remains appropriate.
5. full 4B non-price requirement is strengthened.
6. hard 4C routing is strengthened for core NDA rejection but weakened for manufacturing/formulation CRL without efficacy/formulation break.

## 14. Stage2 / Yellow / Green Comparison
| case | Stage2/Actionable entry | Green entry proxy | peak after Stage2 | green_lateness_ratio | verdict |
|---|---:|---:|---:|---:|---|
| Yuhan approval | 94,300 | 157,000 | 166,900 | 0.86 | Green was late after the approval event; C23 needs an approval/commercialization-specific buffer. |
| Alteogen launch path | 352,000 | no confirmed Green in this run | 529,000 | not_applicable | Stage2-Actionable was the correct label because FDA approval was still pending. |
| HLB CRL | not_applicable | not_applicable | 98,100 rebound | not_applicable | This is not positive-stage promotion; it is 4C guardrail calibration. |
| Yuhan SC CRL | not_applicable | not_applicable | 122,500 local rebound | not_applicable | 4B-watch overlay, not hard 4C. |

## 15. 4B Local vs Full-window Timing Audit
| trigger_id | four_b_local_peak_proximity | four_b_full_window_peak_proximity | evidence_type | verdict |
|---|---:|---:|---|---|
| R7L14-C23-000100-FDA-APPROVAL-20240820 | None | None | none | not_4B_entry |
| R7L14-C23-196170-MERCK-SC-LAUNCH-20250327 | 0.63 | 0.63 | positioning_overheat, control_premium_or_event_premium | event_premium_watch_not_full_4B |
| R7L14-C23-028300-FDA-CRL-20240517 | None | None | legal_or_regulatory_block | hard_4C_not_4B |
| R7L14-C23-000100-RYBREVANT-SC-CRL-20241217 | 0.72 | 0.31 | legal_or_regulatory_block, contract_delay | non_price_4B_watch_not_hard_4C |

## 16. 4C Protection Audit
| trigger_id | 4C label | protection interpretation |
|---|---|---|
| R7L14-C23-028300-FDA-CRL-20240517 | hard_4c_success | Immediate hard 4C captured a core approval-thesis break; later rebound does not remove the initial crash protection value. |
| R7L14-C23-000100-RYBREVANT-SC-CRL-20241217 | thesis_break_watch_only | The FDA letter was tied to a manufacturing inspection and not additional clinical efficacy/formulation evidence, so hard 4C would be too severe. |

## 17. Sector-Specific Rule Candidate
sector_specific_rule_candidate: false. This loop is not broad enough across L7 C23/C24/C25 to propose an L7-wide sector rule.

## 18. Canonical-Archetype Rule Candidate
canonical_archetype_rule_candidate: true.

Proposed C23 shadow rules:
1. `named_global_partner_launch_bonus`: add C23-specific positive weight when a named global partner, regulator path, target launch/adoption economics, and stock-web clean window coexist.
2. `core_regulatory_rejection_4C_guard`: route true NDA/BLA/approval rejection to hard 4C when the approval thesis itself breaks.
3. `formulation_or_manufacturing_crl_watch_not_hard_4c`: route manufacturing/formulation CRL to 4B-watch first when the source says efficacy/formulation data and approved core indication are not impacted.

## 19. Before / After Backtest Comparison
| profile_id | scope | eligible_triggers | avg_MFE_90D | avg_MAE_90D | false_positive_rate | missed_structural_count | late_green_count | score_return_alignment |
|---|---|---:|---:|---:|---:|---:|---:|---|
| P0_e2r_2_1_stock_web_calibrated_proxy | current_global_proxy | 4 | 44.03 | -18.56 | 0.25 | 1 | 1 | mixed; correct direction but too coarse for formulation CRL vs core approval |
| P0b_e2r_2_0_baseline_reference | rollback_reference | 4 | 44.03 | -18.56 | 0.5 | 2 | 2 | weaker; underweights named global partner + regulator route and overreacts to price-only move |
| P1_sector_specific_candidate_profile | sector_specific | 4 | 44.03 | -18.56 | 0.25 | 1 | 1 | acceptable but too broad; C23-specific handling better |
| P2_canonical_archetype_candidate_profile | canonical_archetype_specific | 4 | 44.03 | -18.56 | 0.0 | 0 | 0 | best alignment in this loop |
| P3_counterexample_guard_profile | canonical_archetype_specific_guard | 4 | 44.03 | -18.56 | 0.0 | 0 | 0 | strong guardrail for 4B/4C split |

## 20. Score-Return Alignment Matrix
| trigger_id | weighted_before | stage_before | weighted_after | stage_after | MFE_90D | MAE_90D | alignment |
|---|---:|---|---:|---|---:|---:|---|
| R7L14-C23-000100-FDA-APPROVAL-20240820 | 82.0 | Stage3-Yellow | 85.8 | Stage3-Yellow | 76.99 | -2.97 | approval_to_rerating_success_high_MFE_then_drawdown |
| R7L14-C23-196170-MERCK-SC-LAUNCH-20250327 | 84.8 | Stage3-Yellow | 85.5 | Stage3-Yellow | 44.32 | -10.37 | commercialization_route_success_with_moderate_MAE |
| R7L14-C23-028300-FDA-CRL-20240517 | 0 | 4C | 0 | 4C | 46.2 | -32.71 | regulatory_rejection_crash_then_speculative_rebound |
| R7L14-C23-000100-RYBREVANT-SC-CRL-20241217 | 21.5 | 4B-watch | 19.1 | 4B-watch | 8.6 | -28.19 | formulation_crl_high_MAE_but_not_core_thesis_break |

## 21. Coverage Matrix
| large_sector_id | canonical_archetype_id | fine_archetype_id | positive_case_count | counterexample_count | 4B_case_count | 4C_case_count | new_independent_case_count | reused_case_count | calibration_usable_trigger_count | representative_trigger_count | current_profile_error_count | sector_rule_candidate | canonical_rule_candidate | coverage_gap_after_this_loop |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| L7_BIO_HEALTHCARE_MEDICAL | C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION | ONCOLOGY_REGULATORY_APPROVAL_COMMERCIALIZATION_AND_FORMULATION_EVENT_RISK | 2 | 2 | 1 | 1 | 3 | 1 | 4 | 4 | 3 | false | true | still needs device/reimbursement C25 and pure trial-data C24 loops |

## 22. Residual Contribution Summary
new_independent_case_count: 3
reused_case_count: 1
reused_case_ids: R7L14-C23-000100-SC-FORMULATION-CRL
new_symbol_count: 3
new_canonical_archetype_count: 1
new_fine_archetype_count: 1
new_trigger_family_count: 4
tested_existing_calibrated_axes: stage2_actionable_evidence_bonus, stage3_yellow_total_min, stage3_green_total_min, full_4b_requires_non_price_evidence, hard_4c_thesis_break_routes_to_4c
residual_error_types_found: current_profile_too_late, current_profile_4C_too_late, formulation_crl_not_core_thesis_break
new_axis_proposed: named_global_partner_launch_bonus; core_regulatory_rejection_4C_guard; formulation_or_manufacturing_crl_watch_not_hard_4c
existing_axis_strengthened: full_4b_requires_non_price_evidence; hard_4c_thesis_break_routes_to_4c for core rejection
existing_axis_weakened: hard_4c_thesis_break_routes_to_4c for non-core manufacturing/formulation CRL
existing_axis_kept: price_only_blowoff_blocks_positive_stage
sector_specific_rule_candidate: false
canonical_archetype_rule_candidate: true
no_new_signal_reason: null
loop_contribution_label: canonical_archetype_rule_candidate
do_not_propose_new_weight_delta: false

This loop adds 3 new independent cases, 2 counterexamples, and 3 residual errors for R7/L7_BIO_HEALTHCARE_MEDICAL/C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION.

## 23. Validation Scope / Non-Validation Scope
Validated:
- actual Stock-Web tradable rows for the selected entry windows
- manifest max_date and raw_unadjusted_marcap price basis
- profile-level corporate-action gate
- trigger-level MFE/MAE using visible Stock-Web rows

Not validated / caveats:
- HLB specific CRL source retrieval was incomplete through web search in this run; the row is kept as medium-confidence residual evidence because the price-path and public event timing are strongly aligned.
- 1Y/2Y fields are shadow-only where forward windows approach stock-web max_date; 2Y is unavailable for 2024/2025 triggers.
- No investment recommendation or live candidate scan is performed.

## 24. Shadow Weight Calibration
```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,named_global_partner_launch_bonus,canonical_archetype_specific,L7_BIO_HEALTHCARE_MEDICAL,C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION,0,1,+1,"C23 positive cases with named global partner + regulator/launch route had favorable MFE/MAE despite volatility","reduces missed_structural_count and late_green_count","R7L14-C23-000100-FDA-APPROVAL-20240820|R7L14-C23-196170-MERCK-SC-LAUNCH-20250327",4,3,2,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,core_regulatory_rejection_4C_guard,canonical_archetype_specific,L7_BIO_HEALTHCARE_MEDICAL,C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION,0,1,+1,"HLB CRL-like core NDA rejection behaves as hard 4C rather than ordinary 4B","improves hard thesis-break classification","R7L14-C23-028300-FDA-CRL-20240517",4,3,2,low_to_medium,canonical_shadow_only,"specific HLB web-source retrieval was incomplete; price path is clear but evidence-source confidence is medium"
shadow_weight,formulation_or_manufacturing_crl_watch_not_hard_4c,canonical_archetype_specific,L7_BIO_HEALTHCARE_MEDICAL,C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION,0,1,+1,"J&J SC Rybrevant CRL was not tied to efficacy/formulation and did not break approved IV+lazertinib thesis","prevents over-routing to hard 4C","R7L14-C23-000100-RYBREVANT-SC-CRL-20241217",4,3,2,medium,canonical_shadow_only,"4B overlay guard, not positive promotion"
```

## 25. Machine-Readable Rows
### 25.1 price_source_validation
```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration"}
```

### 25.2 case rows
```jsonl
{"row_type": "case", "case_id": "R7L14-C23-000100-LAZERTINIB-US-APPROVAL", "symbol": "000100", "company_name": "유한양행", "round": "R7", "loop": "14", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION", "fine_archetype_id": "ONCOLOGY_REGULATORY_APPROVAL_COMMERCIALIZATION_AND_FORMULATION_EVENT_RISK", "case_type": "structural_success", "positive_or_counterexample": "positive", "best_trigger": "R7L14-C23-000100-FDA-APPROVAL-20240820", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "approval_to_rerating_success_high_MFE_then_drawdown", "current_profile_verdict": "current_profile_too_late", "price_source": "Songdaiki/stock-web", "notes": "FDA approved J&J Rybrevant plus lazertinib for first-line EGFR-mutated NSCLC; event is directly commercial/regulatory and linked to Yuhan-origin lazertinib economics."}
{"row_type": "case", "case_id": "R7L14-C23-196170-KEYTRUDA-SC-COMMERCIALIZATION", "symbol": "196170", "company_name": "알테오젠", "round": "R7", "loop": "14", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION", "fine_archetype_id": "ONCOLOGY_REGULATORY_APPROVAL_COMMERCIALIZATION_AND_FORMULATION_EVENT_RISK", "case_type": "structural_success", "positive_or_counterexample": "positive", "best_trigger": "R7L14-C23-196170-MERCK-SC-LAUNCH-20250327", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "commercialization_route_success_with_moderate_MAE", "current_profile_verdict": "current_profile_correct", "price_source": "Songdaiki/stock-web", "notes": "Merck said it planned an October 1 U.S. launch for subcutaneous Keytruda if approved, described a September 23 FDA target date, expected 30–40% peak adoption, and identified Alteogen as the enzyme developer/manufacturer."}
{"row_type": "case", "case_id": "R7L14-C23-028300-HCC-NDA-CRL", "symbol": "028300", "company_name": "HLB", "round": "R7", "loop": "14", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION", "fine_archetype_id": "ONCOLOGY_REGULATORY_APPROVAL_COMMERCIALIZATION_AND_FORMULATION_EVENT_RISK", "case_type": "4C_success", "positive_or_counterexample": "counterexample", "best_trigger": "R7L14-C23-028300-FDA-CRL-20240517", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "regulatory_rejection_crash_then_speculative_rebound", "current_profile_verdict": "current_profile_4C_too_late", "price_source": "Songdaiki/stock-web", "notes": "FDA complete response / non-approval event for the liver-cancer NDA route; the trading row shows immediate limit-down repricing and subsequent high-MAE behavior. Web retrieval for the specific HLB press source was incomplete in this run, so evidence confidence is medium rather than high."}
{"row_type": "case", "case_id": "R7L14-C23-000100-SC-FORMULATION-CRL", "symbol": "000100", "company_name": "유한양행", "round": "R7", "loop": "14", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION", "fine_archetype_id": "ONCOLOGY_REGULATORY_APPROVAL_COMMERCIALIZATION_AND_FORMULATION_EVENT_RISK", "case_type": "4B_overlay_success", "positive_or_counterexample": "counterexample", "best_trigger": "R7L14-C23-000100-RYBREVANT-SC-CRL-20241217", "calibration_usable": true, "is_new_independent_case": false, "reuse_reason": "same symbol as Yuhan approval case, but new trigger family: follow-on subcutaneous formulation CRL / regulatory delay overlay rather than initial approval rerating", "independent_evidence_weight": 0.5, "score_price_alignment": "formulation_crl_high_MAE_but_not_core_thesis_break", "current_profile_verdict": "current_profile_4C_too_late", "price_source": "Songdaiki/stock-web", "notes": "FDA declined J&J's injectable Rybrevant; Reuters reported the issue was tied to manufacturing inspection, unrelated to formulation/efficacy, with no additional clinical studies requested and IV Rybrevant not impacted."}
```

### 25.3 trigger rows
```jsonl
{"row_type": "trigger", "trigger_id": "R7L14-C23-000100-FDA-APPROVAL-20240820", "case_id": "R7L14-C23-000100-LAZERTINIB-US-APPROVAL", "symbol": "000100", "company_name": "유한양행", "round": "R7", "loop": "14", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION", "fine_archetype_id": "ONCOLOGY_REGULATORY_APPROVAL_COMMERCIALIZATION_AND_FORMULATION_EVENT_RISK", "sector": "bio_healthcare_medical", "primary_archetype": "regulatory_approval_commercialization", "loop_objective": "coverage_gap_fill|counterexample_mining|canonical_archetype_compression|4B_non_price_requirement_stress_test|4C_thesis_break_timing_test", "trigger_type": "Stage3-Green", "trigger_date": "2024-08-20", "evidence_available_at_that_date": "FDA approved J&J Rybrevant plus lazertinib for first-line EGFR-mutated NSCLC; event is directly commercial/regulatory and linked to Yuhan-origin lazertinib economics.", "evidence_source": "Reuters, 2024-08-20; stock-web 000100 2024 rows", "stage2_evidence_fields": ["public_event_or_disclosure", "customer_or_order_quality", "policy_or_regulatory_optionality"], "stage3_evidence_fields": ["confirmed_revision", "multiple_public_sources", "financial_visibility", "durable_customer_confirmation"], "stage4b_evidence_fields": [], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/000/000100/2024.csv", "profile_path": "atlas/symbol_profiles/000/000100.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-08-21", "entry_price": 94300, "MFE_30D_pct": 69.99, "MFE_90D_pct": 76.99, "MFE_180D_pct": 76.99, "MFE_1Y_pct": 76.99, "MFE_2Y_pct": null, "MAE_30D_pct": -2.97, "MAE_90D_pct": -2.97, "MAE_180D_pct": -14.1, "MAE_1Y_pct": -14.1, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-10-15", "peak_price": 166900, "drawdown_after_peak_pct": -51.47, "green_lateness_ratio": 0.86, "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "not_4B_entry", "four_b_evidence_type": [], "four_c_protection_label": "not_4C", "trigger_outcome_label": "approval_to_rerating_success_high_MFE_then_drawdown", "current_profile_verdict": "current_profile_too_late", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "000100-20240821-94300", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "R7L14-C23-196170-MERCK-SC-LAUNCH-20250327", "case_id": "R7L14-C23-196170-KEYTRUDA-SC-COMMERCIALIZATION", "symbol": "196170", "company_name": "알테오젠", "round": "R7", "loop": "14", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION", "fine_archetype_id": "ONCOLOGY_REGULATORY_APPROVAL_COMMERCIALIZATION_AND_FORMULATION_EVENT_RISK", "sector": "bio_healthcare_medical", "primary_archetype": "regulatory_approval_commercialization", "loop_objective": "coverage_gap_fill|counterexample_mining|canonical_archetype_compression|4B_non_price_requirement_stress_test|4C_thesis_break_timing_test", "trigger_type": "Stage2-Actionable", "trigger_date": "2025-03-27", "evidence_available_at_that_date": "Merck said it planned an October 1 U.S. launch for subcutaneous Keytruda if approved, described a September 23 FDA target date, expected 30–40% peak adoption, and identified Alteogen as the enzyme developer/manufacturer.", "evidence_source": "Reuters, 2025-03-27; stock-web 196170 2025 rows", "stage2_evidence_fields": ["public_event_or_disclosure", "customer_or_order_quality", "policy_or_regulatory_optionality", "early_revision_signal"], "stage3_evidence_fields": ["financial_visibility", "durable_customer_confirmation"], "stage4b_evidence_fields": ["positioning_overheat"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/196/196170/2025.csv", "profile_path": "atlas/symbol_profiles/196/196170.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2025-03-27", "entry_price": 352000, "MFE_30D_pct": 13.49, "MFE_90D_pct": 44.32, "MFE_180D_pct": 50.28, "MFE_1Y_pct": 50.28, "MFE_2Y_pct": null, "MAE_30D_pct": -6.96, "MAE_90D_pct": -10.37, "MAE_180D_pct": -10.37, "MAE_1Y_pct": -10.37, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2025-09-22", "peak_price": 529000, "drawdown_after_peak_pct": -15.88, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.63, "four_b_full_window_peak_proximity": 0.63, "four_b_timing_verdict": "event_premium_watch_not_full_4B", "four_b_evidence_type": ["positioning_overheat", "control_premium_or_event_premium"], "four_c_protection_label": "not_4C", "trigger_outcome_label": "commercialization_route_success_with_moderate_MAE", "current_profile_verdict": "current_profile_correct", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "196170-20250327-352000", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "R7L14-C23-028300-FDA-CRL-20240517", "case_id": "R7L14-C23-028300-HCC-NDA-CRL", "symbol": "028300", "company_name": "HLB", "round": "R7", "loop": "14", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION", "fine_archetype_id": "ONCOLOGY_REGULATORY_APPROVAL_COMMERCIALIZATION_AND_FORMULATION_EVENT_RISK", "sector": "bio_healthcare_medical", "primary_archetype": "regulatory_approval_commercialization", "loop_objective": "coverage_gap_fill|counterexample_mining|canonical_archetype_compression|4B_non_price_requirement_stress_test|4C_thesis_break_timing_test", "trigger_type": "4C", "trigger_date": "2024-05-17", "evidence_available_at_that_date": "FDA complete response / non-approval event for the liver-cancer NDA route; the trading row shows immediate limit-down repricing and subsequent high-MAE behavior. Web retrieval for the specific HLB press source was incomplete in this run, so evidence confidence is medium rather than high.", "evidence_source": "Public CRL/news event; stock-web 028300 2024 rows; CRL definition reference", "stage2_evidence_fields": ["public_event_or_disclosure", "policy_or_regulatory_optionality"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["explicit_event_cap", "legal_or_regulatory_block"], "stage4c_evidence_fields": ["regulatory_rejection", "thesis_evidence_broken"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/028/028300/2024.csv", "profile_path": "atlas/symbol_profiles/028/028300.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-05-17", "entry_price": 67100, "MFE_30D_pct": 9.99, "MFE_90D_pct": 46.2, "MFE_180D_pct": 46.2, "MFE_1Y_pct": 46.2, "MFE_2Y_pct": null, "MAE_30D_pct": -32.71, "MAE_90D_pct": -32.71, "MAE_180D_pct": -32.71, "MAE_1Y_pct": -32.71, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-07-08", "peak_price": 98100, "drawdown_after_peak_pct": -45.46, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "hard_4C_not_4B", "four_b_evidence_type": ["legal_or_regulatory_block"], "four_c_protection_label": "hard_4c_success", "trigger_outcome_label": "regulatory_rejection_crash_then_speculative_rebound", "current_profile_verdict": "current_profile_4C_too_late", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "028300-20240517-67100", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "R7L14-C23-000100-RYBREVANT-SC-CRL-20241217", "case_id": "R7L14-C23-000100-SC-FORMULATION-CRL", "symbol": "000100", "company_name": "유한양행", "round": "R7", "loop": "14", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION", "fine_archetype_id": "ONCOLOGY_REGULATORY_APPROVAL_COMMERCIALIZATION_AND_FORMULATION_EVENT_RISK", "sector": "bio_healthcare_medical", "primary_archetype": "regulatory_approval_commercialization", "loop_objective": "coverage_gap_fill|counterexample_mining|canonical_archetype_compression|4B_non_price_requirement_stress_test|4C_thesis_break_timing_test", "trigger_type": "4B-overlay", "trigger_date": "2024-12-17", "evidence_available_at_that_date": "FDA declined J&J's injectable Rybrevant; Reuters reported the issue was tied to manufacturing inspection, unrelated to formulation/efficacy, with no additional clinical studies requested and IV Rybrevant not impacted.", "evidence_source": "Reuters, 2024-12-17; stock-web 000100 2024/2025 rows", "stage2_evidence_fields": ["public_event_or_disclosure", "policy_or_regulatory_optionality"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["legal_or_regulatory_block", "contract_delay", "explicit_event_cap"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/000/000100/2024.csv", "profile_path": "atlas/symbol_profiles/000/000100.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-12-17", "entry_price": 112800, "MFE_30D_pct": 8.6, "MFE_90D_pct": 8.6, "MFE_180D_pct": 8.6, "MFE_1Y_pct": 8.6, "MFE_2Y_pct": null, "MAE_30D_pct": -28.19, "MAE_90D_pct": -28.19, "MAE_180D_pct": -28.19, "MAE_1Y_pct": -28.19, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-12-30", "peak_price": 122500, "drawdown_after_peak_pct": -33.88, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.72, "four_b_full_window_peak_proximity": 0.31, "four_b_timing_verdict": "non_price_4B_watch_not_hard_4C", "four_b_evidence_type": ["legal_or_regulatory_block", "contract_delay"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "formulation_crl_high_MAE_but_not_core_thesis_break", "current_profile_verdict": "current_profile_4C_too_late", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "000100-20241217-112800", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": false, "reuse_reason": "same symbol as Yuhan approval case, but new trigger family: follow-on subcutaneous formulation CRL / regulatory delay overlay rather than initial approval rerating", "independent_evidence_weight": 0.5, "do_not_count_as_new_case": false}
```

### 25.4 score_simulation rows
```jsonl
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R7L14-C23-000100-LAZERTINIB-US-APPROVAL", "trigger_id": "R7L14-C23-000100-FDA-APPROVAL-20240820", "symbol": "000100", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 10, "relative_strength_score": 8, "customer_quality_score": 12, "policy_or_regulatory_score": 16, "valuation_repricing_score": 10, "execution_risk_score": 0, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 82.0, "stage_label_before": "Stage3-Yellow", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 10, "relative_strength_score": 8, "customer_quality_score": 14, "policy_or_regulatory_score": 19, "valuation_repricing_score": 10, "execution_risk_score": 0, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 85.8, "stage_label_after": "Stage3-Yellow", "changed_components": ["customer_quality_score", "policy_or_regulatory_score"], "component_delta_explanation": "shadow-only: adds approval commercialization quality when named global partner + regulator + launch economics are all present; adds harsher 4C risk for real regulatory rejection; treats formulation/manufacturing CRL as 4B-watch unless core efficacy/approved IV thesis breaks.", "MFE_90D_pct": 76.99, "MAE_90D_pct": -2.97, "score_return_alignment_label": "approval_to_rerating_success_high_MFE_then_drawdown", "current_profile_verdict": "current_profile_too_late"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R7L14-C23-196170-KEYTRUDA-SC-COMMERCIALIZATION", "trigger_id": "R7L14-C23-196170-MERCK-SC-LAUNCH-20250327", "symbol": "196170", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION", "raw_component_scores_before": {"contract_score": 10, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 8, "relative_strength_score": 8, "customer_quality_score": 15, "policy_or_regulatory_score": 12, "valuation_repricing_score": 11, "execution_risk_score": 4, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 84.8, "stage_label_before": "Stage3-Yellow", "raw_component_scores_after": {"contract_score": 10, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 8, "relative_strength_score": 8, "customer_quality_score": 18, "policy_or_regulatory_score": 12, "valuation_repricing_score": 11, "execution_risk_score": 6, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 85.5, "stage_label_after": "Stage3-Yellow", "changed_components": ["customer_quality_score", "execution_risk_score"], "component_delta_explanation": "shadow-only: adds approval commercialization quality when named global partner + regulator + launch economics are all present; adds harsher 4C risk for real regulatory rejection; treats formulation/manufacturing CRL as 4B-watch unless core efficacy/approved IV thesis breaks.", "MFE_90D_pct": 44.32, "MAE_90D_pct": -10.37, "score_return_alignment_label": "commercialization_route_success_with_moderate_MAE", "current_profile_verdict": "current_profile_correct"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R7L14-C23-028300-HCC-NDA-CRL", "trigger_id": "R7L14-C23-028300-FDA-CRL-20240517", "symbol": "028300", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 0, "customer_quality_score": 0, "policy_or_regulatory_score": -5, "valuation_repricing_score": -8, "execution_risk_score": 18, "legal_or_contract_risk_score": 20, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 0, "stage_label_before": "4C", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 0, "customer_quality_score": 0, "policy_or_regulatory_score": -5, "valuation_repricing_score": -8, "execution_risk_score": 21, "legal_or_contract_risk_score": 25, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 0, "stage_label_after": "4C", "changed_components": ["execution_risk_score", "legal_or_contract_risk_score"], "component_delta_explanation": "shadow-only: adds approval commercialization quality when named global partner + regulator + launch economics are all present; adds harsher 4C risk for real regulatory rejection; treats formulation/manufacturing CRL as 4B-watch unless core efficacy/approved IV thesis breaks.", "MFE_90D_pct": 46.2, "MAE_90D_pct": -32.71, "score_return_alignment_label": "regulatory_rejection_crash_then_speculative_rebound", "current_profile_verdict": "current_profile_4C_too_late"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R7L14-C23-000100-SC-FORMULATION-CRL", "trigger_id": "R7L14-C23-000100-RYBREVANT-SC-CRL-20241217", "symbol": "000100", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 0, "customer_quality_score": 0, "policy_or_regulatory_score": 5, "valuation_repricing_score": -4, "execution_risk_score": 11, "legal_or_contract_risk_score": 13, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 21.5, "stage_label_before": "4B-watch", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 0, "customer_quality_score": 0, "policy_or_regulatory_score": 5, "valuation_repricing_score": -4, "execution_risk_score": 12, "legal_or_contract_risk_score": 15, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 19.1, "stage_label_after": "4B-watch", "changed_components": ["execution_risk_score", "legal_or_contract_risk_score"], "component_delta_explanation": "shadow-only: adds approval commercialization quality when named global partner + regulator + launch economics are all present; adds harsher 4C risk for real regulatory rejection; treats formulation/manufacturing CRL as 4B-watch unless core efficacy/approved IV thesis breaks.", "MFE_90D_pct": 8.6, "MAE_90D_pct": -28.19, "score_return_alignment_label": "formulation_crl_high_MAE_but_not_core_thesis_break", "current_profile_verdict": "current_profile_4C_too_late"}
```

### 25.5 shadow_weight rows
```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,named_global_partner_launch_bonus,canonical_archetype_specific,L7_BIO_HEALTHCARE_MEDICAL,C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION,0,1,+1,"C23 positive cases with named global partner + regulator/launch route had favorable MFE/MAE despite volatility","reduces missed_structural_count and late_green_count","R7L14-C23-000100-FDA-APPROVAL-20240820|R7L14-C23-196170-MERCK-SC-LAUNCH-20250327",4,3,2,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,core_regulatory_rejection_4C_guard,canonical_archetype_specific,L7_BIO_HEALTHCARE_MEDICAL,C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION,0,1,+1,"HLB CRL-like core NDA rejection behaves as hard 4C rather than ordinary 4B","improves hard thesis-break classification","R7L14-C23-028300-FDA-CRL-20240517",4,3,2,low_to_medium,canonical_shadow_only,"specific HLB web-source retrieval was incomplete; price path is clear but evidence-source confidence is medium"
shadow_weight,formulation_or_manufacturing_crl_watch_not_hard_4c,canonical_archetype_specific,L7_BIO_HEALTHCARE_MEDICAL,C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION,0,1,+1,"J&J SC Rybrevant CRL was not tied to efficacy/formulation and did not break approved IV+lazertinib thesis","prevents over-routing to hard 4C","R7L14-C23-000100-RYBREVANT-SC-CRL-20241217",4,3,2,medium,canonical_shadow_only,"4B overlay guard, not positive promotion"
```

### 25.6 residual_contribution row
```jsonl
{"row_type": "residual_contribution", "round": "R7", "loop": "14", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION", "new_independent_case_count": 3, "reused_case_count": 1, "new_symbol_count": 3, "new_trigger_family_count": 4, "tested_existing_calibrated_axes": ["stage2_actionable_evidence_bonus", "stage3_yellow_total_min", "stage3_green_total_min", "full_4b_requires_non_price_evidence", "hard_4c_thesis_break_routes_to_4c"], "residual_error_types_found": ["current_profile_too_late", "current_profile_4C_too_late", "formulation_crl_not_core_thesis_break"], "loop_contribution_label": "canonical_archetype_rule_candidate", "do_not_propose_new_weight_delta": false}
```

### 25.7 narrative_only rows
```jsonl
{"row_type": "narrative_only", "case_id": "R7L14-C23-068270-ZYMFENTRA-FDA-APPROVAL", "symbol": "068270", "company_name": "셀트리온", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION", "reason": "FDA approval event exists, but stock-web profile flags a corporate-action candidate on 2024-01-12 inside the 180D forward window from 2023-10-23, so quantitative weight calibration is blocked.", "price_source": "Songdaiki/stock-web", "usage": "not_weight_calibration"}
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
completed_round = R7
completed_loop = 14
next_round = R8
next_loop = 14
round_schedule_status = valid
round_sector_consistency = pass

## 28. Source Notes
- Stock-Web manifest and schema were read through the GitHub connector, not via local stock_agent code.
- The GitHub connector showed actual Stock-Web OHLC rows for every quantitative trigger used.
- Reuters sources were used for the Yuhan/J&J approval and formulation CRL, and for Alteogen/Merck commercialization-route evidence.
- This file is standalone research output; it does not patch production scoring.
