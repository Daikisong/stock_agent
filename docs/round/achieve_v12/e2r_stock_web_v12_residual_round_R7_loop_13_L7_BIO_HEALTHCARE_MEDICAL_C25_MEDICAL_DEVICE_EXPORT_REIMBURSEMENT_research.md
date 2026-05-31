# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```yaml
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
scheduled_round: R7
scheduled_loop: 13
completed_round: R7
completed_loop: 13
large_sector_id: L7_BIO_HEALTHCARE_MEDICAL
canonical_archetype_id: C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT
fine_archetype_id: MEDICAL_AI_REIMBURSEMENT_EXPORT_REORDER_MARGIN_BRIDGE
output_file: e2r_stock_web_v12_residual_round_R7_loop_13_L7_BIO_HEALTHCARE_MEDICAL_C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT_research.md
price_source: Songdaiki/stock-web
stock_web_manifest_max_date: 2026-02-20
production_scoring_changed: false
shadow_weight_only: true
handoff_prompt_embedded: true
handoff_prompt_executed_now: false
stock_agent_code_access_allowed: false
stock_agent_code_patch_allowed: false
stock_agent_live_scan_allowed: false
current_stock_discovery_allowed: false
auto_trading_allowed: false
brokerage_api_allowed: false
round_schedule_status: valid
round_sector_consistency: pass
```

This loop adds 5 new independent cases, 2 counterexamples, and 3 residual errors for R7/L7_BIO_HEALTHCARE_MEDICAL/C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT.

## 1. Current Calibrated Profile Assumption

Current default proxy is `e2r_2_1_stock_web_calibrated_proxy`; rollback reference is `e2r_2_0_baseline_reference`.

Already-applied axes are assumed active and are not globally re-proposed:

```text
stage2_actionable_evidence_bonus = +2.0
stage3_yellow_total_min = 75.0
stage3_green_total_min = 87.0
stage3_green_revision_min = 55.0
stage3_cross_evidence_green_buffer = +1.5
price_only_blowoff_blocks_positive_stage = true
full_4b_requires_non_price_evidence = true
hard_4c_thesis_break_routes_to_4c = true
```

The residual question is narrower. C25 contains two species that look similar on a chart but behave differently under a microscope: export/reorder medical-device companies, and medical-AI/reimbursement companies. The first is a channel-and-margin bridge. The second is a reimbursement/adoption bridge. Both can rise vertically, but only the second has a stronger binary adoption gap between narrative and cash flow. This MD therefore tests whether C25 needs a medical-AI reimbursement confirmation gate and a high-MAE guard.

## 2. Round / Large Sector / Canonical Archetype Scope

| Field | Value |
|---|---|
| scheduled_round | R7 |
| scheduled_loop | 13 |
| large_sector_id | L7_BIO_HEALTHCARE_MEDICAL |
| canonical_archetype_id | C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT |
| fine_archetype_id | MEDICAL_AI_REIMBURSEMENT_EXPORT_REORDER_MARGIN_BRIDGE |
| loop_objective | coverage_gap_fill; counterexample_mining; residual_false_positive_mining; 4B_non_price_requirement_stress_test; canonical_archetype_compression; sector_specific_rule_discovery |
| invalid_round_sector_pair | false |
| computed_next_round | R8 |
| computed_next_loop | 13 |

R7 hard gate passes because `R7 -> L7_BIO_HEALTHCARE_MEDICAL`.

## 3. Previous Coverage / Duplicate Avoidance Check

Local v12 state already has:

```text
R7 loop 10: C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT with 클래시스, 파마리서치, 덴티움, 디오
R7 loop 11: C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION with 유한양행, 알테오젠, 휴젤, HLB, 셀트리온 narrative-only
R7 loop 12: C24_BIO_TRIAL_DATA_EVENT_RISK with 유한양행, 오스코텍, 신풍제약, HLB reuse, 헬릭스미스 narrative-only
```

This loop does not repeat those symbol + trigger-date + evidence-family combinations. It extends C25 using new medical-AI/reimbursement and dental-imaging export cases: 뷰노, 제이엘케이, 아이센스, 바텍, 루닛.

```text
same_canonical_archetype_research = allowed
same_symbol_same_trigger_date_research = avoided
new_independent_case_count = 5
reused_case_count = 0
new_symbol_count = 5
same_archetype_new_symbol_count = 5
same_archetype_new_trigger_family_count = 5
minimum_new_independent_case_ratio = 5 / 5 = 1.00
```

## 4. Stock-Web OHLC Input / Price Source Validation

```yaml
price_data_source: Songdaiki/stock-web
upstream_source: FinanceData/marcap
source_repo_url: https://github.com/FinanceData/marcap
price_basis: tradable_raw
price_adjustment_status: raw_unadjusted_marcap
manifest_max_date: 2026-02-20
tradable_row_count: 14354401
raw_row_count: 15214118
symbol_count: 5414
active_like_symbol_count: 2868
inactive_or_delisted_like_symbol_count: 2546
markets: KONEX, KOSDAQ, KOSDAQ GLOBAL, KOSPI
calibration_shard_root: atlas/ohlcv_tradable_by_symbol_year
raw_shard_root: atlas/ohlcv_raw_by_symbol_year
schema_path: atlas/schema.json
universe_path: atlas/universe/all_symbols.csv
```

The stock-web manifest confirms raw/unadjusted OHLC, exclusion of non-tradable zero-volume rows from calibration shards, and default blocking of corporate-action contaminated windows. All quantitative rows below use `tradable_raw` only. Raw shards are not used for weight calibration.

## 5. Historical Eligibility Gate

| case_id | symbol | profile_path | 180D forward window | corporate-action status | calibration_usable |
|---|---:|---|---|---|---|
| R7L13-C25-338220-VUNO-MEDICAL-AI-REIMBURSEMENT-RERATING | 338220 | atlas/symbol_profiles/338/338220.json | available | no corporate-action candidate | true |
| R7L13-C25-322510-JLK-STROKE-AI-REIMBURSEMENT-HIGH-MAE | 322510 | atlas/symbol_profiles/322/322510.json | available | 2024-10-30 outside 180D window | true |
| R7L13-C25-099190-ISENS-CGM-LAUNCH-FAILED-RERATING | 099190 | atlas/symbol_profiles/099/099190.json | available | 2023-03-14 and 2023-04-10 before entry | true |
| R7L13-C25-043150-VATECH-DENTAL-IMAGING-EXPORT-RECOVERY | 043150 | atlas/symbol_profiles/043/043150.json | available | 2010-09-02 outside window | true |
| R7L13-C25-328130-LUNIT-MEDICAL-AI-NARRATIVE-BLOCKED | 328130 | atlas/symbol_profiles/328/328130.json | available | 2023-11-09 and 2023-12-01 contaminate representative 2023 window | false; narrative_only |

## 6. Canonical Archetype Compression Map

```text
C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT
  ├─ MEDICAL_AI_REIMBURSEMENT_ADOPTION_RERATING: 338220, 322510
  ├─ CGM_REIMBURSEMENT_PRODUCT_LAUNCH_WITHOUT_MARGIN_BRIDGE: 099190
  ├─ DENTAL_IMAGING_EXPORT_ORDER_MARGIN_BRIDGE: 043150
  └─ MEDICAL_AI_APPROVAL_COMMERCIALIZATION_CORPORATE_ACTION_BLOCKED: 328130 narrative_only
```

C25 should therefore compress fine archetypes into two mechanical questions:

1. Does the product/device have a customer or reimbursement path that can become repeat revenue?
2. Is the price move still attached to that path, or has it become a balloon with only air under it?

## 7. Case Selection Summary

| case_id | symbol | company | role | usable | new_independent | best_trigger | current_profile_verdict |
|---|---:|---|---|---|---|---|---|
| R7L13-C25-338220-VUNO-MEDICAL-AI-REIMBURSEMENT-RERATING | 338220 | 뷰노 | structural_success | true | true | R7L13-C25-338220-T1-STAGE2A-20230602 | current_profile_missed_structural |
| R7L13-C25-322510-JLK-STROKE-AI-REIMBURSEMENT-HIGH-MAE | 322510 | 제이엘케이 | high_mae_success | true | true | R7L13-C25-322510-T1-STAGE2A-20230517 | current_profile_too_early |
| R7L13-C25-099190-ISENS-CGM-LAUNCH-FAILED-RERATING | 099190 | 아이센스 | failed_rerating | true | true | R7L13-C25-099190-T1-CGM-STAGE2-20230718 | current_profile_false_positive |
| R7L13-C25-043150-VATECH-DENTAL-IMAGING-EXPORT-RECOVERY | 043150 | 바텍 | stage2_promote_candidate | true | true | R7L13-C25-043150-T1-EXPORT-RECOVERY-20230329 | current_profile_correct |
| R7L13-C25-328130-LUNIT-MEDICAL-AI-NARRATIVE-BLOCKED | 328130 | 루닛 | narrative_only | false | true | narrative_only | current_profile_data_insufficient |

## 8. Positive vs Counterexample Balance

| bucket | count | cases |
|---|---:|---|
| positive structural / promote candidates | 3 | 뷰노, 제이엘케이, 바텍 |
| counterexample / failed rerating / blocked | 2 | 아이센스, 루닛 narrative-only |
| 4B overlay cases | 2 | 뷰노, 제이엘케이 |
| 4C / thesis-break watch cases | 2 | 아이센스, 루닛 narrative-only |
| calibration-usable cases | 4 | 뷰노, 제이엘케이, 아이센스, 바텍 |
| representative calibration triggers | 4 | one per usable case |

Positive-only bias is avoided. The loop deliberately contrasts medical-AI rerating winners with a CGM false-positive path and a corporate-action-blocked medical-AI narrative.

## 9. Evidence Source Map

| symbol | event family | trigger date | evidence interpretation |
|---:|---|---:|---|
| 338220 | medical-AI hospital adoption / reimbursement optionality | 2023-06-02 | Stage2 evidence was not only price: adoption and reimbursement optionality gave a plausible route to revenue. Green still needed confirmation. |
| 322510 | stroke-AI reimbursement narrative | 2023-05-17 | A real medical-AI option, but the path had high MAE and became highly reflexive. Stage2 yes; premature Green no. |
| 099190 | CGM launch / reimbursement expectation | 2023-07-18 | Product launch excitement was not enough without adoption and margin bridge. Good counterexample for C25 Green strictness. |
| 043150 | dental imaging export/order recovery | 2023-03-29 | Old-style device export recovery had lower binary risk and cleaner early MFE/MAE. |
| 328130 | medical-AI approval/commercialization narrative | 2023 representative window | Archetypally relevant, but corporate-action contamination blocks quantitative use. |

## 10. Price Data Source Map

| symbol | company | price_shard_path used | profile_path | corporate action window status |
|---:|---|---|---|---|
| 338220 | 뷰노 | atlas/ohlcv_tradable_by_symbol_year/338/338220/2023.csv | atlas/symbol_profiles/338/338220.json | clean_180D_window |
| 322510 | 제이엘케이 | atlas/ohlcv_tradable_by_symbol_year/322/322510/2023.csv | atlas/symbol_profiles/322/322510.json | clean_180D_window; corporate_action_candidate_date_2024-10-30_outside_window |
| 099190 | 아이센스 | atlas/ohlcv_tradable_by_symbol_year/099/099190/2023.csv | atlas/symbol_profiles/099/099190.json | clean_180D_window; corporate_action_candidate_dates_2023-03-14_2023-04-10_before_entry |
| 043150 | 바텍 | atlas/ohlcv_tradable_by_symbol_year/043/043150/2023.csv | atlas/symbol_profiles/043/043150.json | clean_180D_window; corporate_action_candidate_date_2010-09-02_outside_window |
| 328130 | 루닛 | atlas/ohlcv_tradable_by_symbol_year/328/328130/2023.csv | atlas/symbol_profiles/328/328130.json | narrative_only_blocked_by_2023-11-09_and_2023-12-01_corporate_action_candidates |

## 11. Case-by-Case Trigger Grid

| trigger_id | symbol | trigger_type | trigger_date | entry_date | entry_price | outcome | current_profile_verdict | aggregate_dedupe |
|---|---:|---|---:|---:|---:|---|---|---|
| R7L13-C25-338220-T1-STAGE2A-20230602 | 338220 | Stage2-Actionable | 2023-06-02 | 2023-06-02 | 23650 | durable_medical_ai_reimbursement_rerating_with_later_4B_need | current_profile_missed_structural | true |
| R7L13-C25-338220-T2-4B-20230906 | 338220 | Stage4B | 2023-09-06 | 2023-09-06 | 65500 | good_4B_overlay_after_medical_ai_blowoff | current_profile_4B_too_late | false |
| R7L13-C25-322510-T1-STAGE2A-20230517 | 322510 | Stage2-Actionable | 2023-05-17 | 2023-05-17 | 7700 | high_mfe_high_mae_medical_ai_reimbursement_success | current_profile_too_early | true |
| R7L13-C25-322510-T2-PRICE-ONLY-4B-20230724 | 322510 | Stage4B | 2023-07-24 | 2023-07-24 | 37000 | price_only_4B_overlay_not_full_exit_until_non_price_evidence | current_profile_4B_too_early | false |
| R7L13-C25-099190-T1-CGM-STAGE2-20230718 | 099190 | Stage2 | 2023-07-18 | 2023-07-18 | 32000 | failed_CGM_reimbursement_rerating_high_MAE | current_profile_false_positive | true |
| R7L13-C25-043150-T1-EXPORT-RECOVERY-20230329 | 043150 | Stage2-Actionable | 2023-03-29 | 2023-03-29 | 32100 | clean_low_MAE_export_recovery_stage2 | current_profile_correct | true |

## 12. Trigger-Level OHLC Backtest Tables

All MFE/MAE values use stock-web `tradable_raw` rows. `MFE_N_pct = max(high_N)/entry_price - 1`; `MAE_N_pct = min(low_N)/entry_price - 1`.

| trigger_id | entry_price | MFE_30D | MFE_90D | MFE_180D | MAE_30D | MAE_90D | MAE_180D | peak_date | peak_price | drawdown_after_peak_pct |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| R7L13-C25-338220-T1-STAGE2A-20230602 | 23650 | 72.09 | 193.87 | 193.87 | -6.77 | -6.77 | -6.77 | 2023-09-07 | 69500 | -70.72 |
| R7L13-C25-338220-T2-4B-20230906 | 65500 | 6.11 | 6.11 | 6.11 | -47.18 | -63.59 | -59.31 | 2023-09-07 | 69500 | -70.72 |
| R7L13-C25-322510-T1-STAGE2A-20230517 | 7700 | 146.75 | 402.6 | 402.6 | -19.48 | -19.48 | -19.48 | 2023-09-07 | 38700 | -80.26 |
| R7L13-C25-322510-T2-PRICE-ONLY-4B-20230724 | 37000 | 4.59 | 4.59 | 4.59 | -26.08 | -56.08 | -56.08 | 2023-09-07 | 38700 | -80.26 |
| R7L13-C25-099190-T1-CGM-STAGE2-20230718 | 32000 | 23.59 | 24.06 | 24.06 | -13.13 | -32.03 | -32.03 | 2023-09-08 | 39700 | -44.21 |
| R7L13-C25-043150-T1-EXPORT-RECOVERY-20230329 | 32100 | 38.79 | 38.79 | 38.79 | -6.23 | -6.23 | -7.79 | 2023-05-04 | 44550 | -51.74 |

## 13. Current Calibrated Profile Stress Test

| case | likely current-profile action | actual MFE/MAE alignment | verdict |
|---|---|---|---|
| 뷰노 | Stage2 or Yellow could be delayed because revisions/financial visibility were incomplete | +193.87% MFE with manageable early MAE; current profile risks missing structural medical-AI adoption rerating | current_profile_missed_structural |
| 제이엘케이 | Relative-strength and medical-AI option might push too quickly toward Yellow/Green | Massive MFE but entry-day and post-peak drawdown require high-MAE guard | current_profile_too_early |
| 아이센스 | Product launch/reimbursement expectation could look like Stage2/Yellow | MFE was modest while MAE was severe; Green would be false positive | current_profile_false_positive |
| 바텍 | Export/order recovery with margin bridge should pass Stage2/Yellow | Clean early MFE/MAE validates device-export bridge | current_profile_correct |
| 루닛 | Archetype relevant but unusable due corporate-action contaminated window | Cannot calibrate weight from this window | current_profile_data_insufficient |

Answers to the mandatory stress-test questions:

```text
1. current calibrated profile would catch export/reorder device cases better than medical-AI reimbursement cases.
2. It would be too late on VUNO, too early on JLK if it follows price too strongly, false-positive on ISENS, and correct on Vatech.
3. Stage2 bonus is useful for VUNO/JLK/Vatech but excessive for ISENS without adoption/reimbursement confirmation.
4. Yellow 75 is acceptable if C25 confirmation components are used; not acceptable if relative strength substitutes for reimbursement bridge.
5. Green 87 / revision 55 remains necessary; medical-AI cases need commercialization bridge before Green.
6. price-only blowoff guard is strengthened by JLK and VUNO 4B overlays.
7. full 4B non-price requirement is strengthened: VUNO had enough valuation/revenue-lag context; JLK price-only local 4B should remain overlay-only.
8. hard 4C routing should be kept; ISENS shows a slow thesis-break rather than an immediate crash.
```

## 14. Stage2 / Yellow / Green Comparison

C25 medical-AI Stage2 can be early and valuable, but Green must be stingier than ordinary medical-device export Green. A device export rerating is like a distributor ledger: order, shipment, margin. A medical-AI reimbursement rerating is like a hospital protocol change: adoption, reimbursement code, workflow, and repeat usage must all open before the revenue door stays open.

| case | Stage2 suitability | Yellow suitability | Green suitability | green_lateness_ratio |
|---|---|---|---|---|
| 뷰노 | high | medium-high after hospital adoption evidence | only after adoption/revenue bridge | n/a |
| 제이엘케이 | high but high-MAE | medium after reimbursement confirmation | blocked until conversion evidence | n/a |
| 아이센스 | watch only | weak | blocked | n/a |
| 바텍 | high | high | only if export growth repeats | 0.42 |

## 15. 4B Local vs Full-window Timing Audit

| trigger_id | local_peak_proximity | full_window_peak_proximity | evidence_type | verdict |
|---|---:|---:|---|---|
| R7L13-C25-338220-T2-4B-20230906 | 0.91 | 0.91 | valuation_blowoff; positioning_overheat; margin_or_backlog_slowdown | good_full_window_4B_timing |
| R7L13-C25-322510-T2-PRICE-ONLY-4B-20230724 | 0.96 | 0.95 | price_only; valuation_blowoff; positioning_overheat | price_only_local_4B_needs_non_price_confirmation |

The split matters. VUNO's later revenue-lag/valuation context makes 4B a usable overlay. JLK's July local high was mostly a price-and-theme exhaust plume; without non-price evidence it should not be treated as full 4B.

## 16. 4C Protection Audit

| case | 4C label | interpretation |
|---|---|---|
| 아이센스 | hard_4c_late | The failure was not a one-day thesis break; it was a slow realization that CGM launch did not yet translate into reimbursement/margin evidence. |
| 루닛 | narrative_only | Relevant 4C/guardrail case, but corporate-action contamination blocks quantitative use. |
| 제이엘케이 | thesis_break_watch_only | Not a hard break at Stage2; high-MAE and later drawdown require watch overlay. |
| 뷰노 | thesis_break_watch_only after 4B | 4B was timely; hard 4C only after adoption/revenue evidence weakens. |

## 17. Sector-Specific Rule Candidate

```text
rule_scope = sector_specific
large_sector_id = L7_BIO_HEALTHCARE_MEDICAL
candidate_axis = L7_medical_AI_reimbursement_confirmation_gate
proposal = In L7, medical-AI/reimbursement cases may receive Stage2-Actionable on public event + adoption/reimbursement optionality + relative strength, but cannot receive Stage3-Green unless at least two of hospital adoption, reimbursement code/payment, repeat usage, or revenue/margin bridge are confirmed.
```

Backtest effect: preserves VUNO/JLK as Stage2 opportunities, blocks ISENS-style false Green, and avoids treating Lunit-like corporate-action windows as quantitative evidence.

## 18. Canonical-Archetype Rule Candidate

```text
rule_scope = canonical_archetype_specific
canonical_archetype_id = C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT
candidate_axis = C25_medical_AI_vs_device_export_split
proposal = C25 should split device-export evidence and medical-AI reimbursement evidence. Device-export cases can promote on repeat-order/margin bridge. Medical-AI cases need adoption/reimbursement/commercialization bridge before Green.
```

This is not a global delta. It is C25-specific because the same term “medical device” hides two different engines.

## 19. Before / After Backtest Comparison

| profile_id | scope | hypothesis | eligible_trigger_count | avg_MFE_90D | avg_MAE_90D | false_positive_rate | missed_structural_count | late_green_count | score_return_alignment_verdict |
|---|---|---|---:|---:|---:|---:|---:|---:|---|
| P0_e2r_2_1_stock_web_calibrated_proxy | current | global calibrated profile only | 4 | 163.83 | -15.99 | 0.25 | 1 | 1 | mixed: catches device export, less precise for medical AI |
| P0b_e2r_2_0_baseline_reference | rollback | older baseline without stock-web calibration | 4 | 163.83 | -15.99 | 0.50 | 2 | 0 | worse: price/RS overpromotes ISENS/JLK |
| P1_L7_sector_shadow_profile | sector | require L7 medical-AI adoption/reimbursement confirmation | 4 | 163.83 | -15.99 | 0.00 | 1 | 1 | better false-positive control |
| P2_C25_archetype_shadow_profile | canonical | split medical-AI and device-export confirmation keys | 4 | 163.83 | -15.99 | 0.00 | 0 | 1 | best score-return alignment |
| P3_counterexample_guard_profile | guard | penalize product launch without reimbursement/margin bridge | 4 | 163.83 | -15.99 | 0.00 | 1 | 1 | strong guard, slightly conservative |

## 20. Score-Return Alignment Matrix

| trigger_id | score_before | stage_before | score_after | stage_after | MFE_90D | MAE_90D | alignment |
|---|---:|---|---:|---|---:|---:|---|
| R7L13-C25-338220-T1-STAGE2A-20230602 | 74 | Stage2-Actionable | 82 | Stage3-Yellow_after_adoption_bridge | 193.87 | -6.77 | positive_alignment_after_reimbursement_bridge |
| R7L13-C25-338220-T2-4B-20230906 | 84 | Stage3-Green_or_4B_watch | 70 | Stage4B_overlay | 6.11 | -63.59 | 4B_alignment_after_blowoff |
| R7L13-C25-322510-T1-STAGE2A-20230517 | 76 | Stage3-Yellow_candidate | 70 | Stage2-Actionable_high_MAE_guard | 402.6 | -19.48 | positive_but_high_MAE_alignment |
| R7L13-C25-322510-T2-PRICE-ONLY-4B-20230724 | 79 | Stage3-Yellow_or_4B_candidate | 59 | 4B_overlay_only_price_driven | 4.59 | -56.08 | price_only_4B_needs_non_price_confirmation |
| R7L13-C25-099190-T1-CGM-STAGE2-20230718 | 76 | Stage3-Yellow_candidate | 49 | Stage2_watch_or_4C_watch | 24.06 | -32.03 | false_positive_blocked_after |
| R7L13-C25-043150-T1-EXPORT-RECOVERY-20230329 | 78 | Stage3-Yellow_candidate | 82 | Stage3-Yellow | 38.79 | -6.23 | clean_low_MAE_alignment |

## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive_case_count | counterexample_count | 4B_case_count | 4C_case_count | new_independent_case_count | reused_case_count | calibration_usable_trigger_count | representative_trigger_count | current_profile_error_count | sector_rule_candidate | canonical_rule_candidate | coverage_gap_after_this_loop |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| L7_BIO_HEALTHCARE_MEDICAL | C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT | MEDICAL_AI_REIMBURSEMENT_EXPORT_REORDER_MARGIN_BRIDGE | 3 | 2 | 2 | 2 | 5 | 0 | 6 | 4 | 3 | true | true | C25 now has a second pass covering medical-AI reimbursement vs product-launch false positives; still needs more overseas reimbursement and hospital-adoption holdouts. |

## 22. Residual Contribution Summary

```yaml
new_independent_case_count: 5
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 5
new_canonical_archetype_count: 0
new_fine_archetype_count: 1
new_trigger_family_count: 5
tested_existing_calibrated_axes:
  - stage2_actionable_evidence_bonus
  - stage3_green_revision_min
  - price_only_blowoff_blocks_positive_stage
  - full_4b_requires_non_price_evidence
  - hard_4c_thesis_break_routes_to_4c
residual_error_types_found:
  - current_profile_missed_structural
  - current_profile_too_early
  - current_profile_false_positive
  - current_profile_4B_too_late
new_axis_proposed:
  - C25_medical_ai_reimbursement_confirmation_gate
  - C25_high_MAE_medical_AI_guard
  - C25_price_only_4B_overlay_guard
existing_axis_strengthened:
  - price_only_blowoff_blocks_positive_stage
  - full_4b_requires_non_price_evidence
  - hard_4c_thesis_break_routes_to_4c
existing_axis_weakened: []
existing_axis_kept:
  - stage2_actionable_evidence_bonus
  - stage3_yellow_total_min
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
- R7 / L7 / C25 round-sector consistency.
- Stock-web manifest max_date = 2026-02-20.
- Profile availability and corporate-action caveats for selected symbols.
- Entry-date OHLC rows for representative triggers.
- 30D/90D/180D MFE/MAE proxy calculations from stock-web tradable rows.
- Positive and counterexample balance.
- 4B local vs full-window split for medical-AI vertical reratings.
```

Not validated:

```text
- No production scoring code was read.
- No live candidates were scanned.
- No brokerage or auto-trading logic was touched.
- No global score delta is proposed.
- Lunit is narrative-only because corporate-action contamination blocks representative quantitative use.
```

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,C25_medical_ai_reimbursement_confirmation_gate,canonical_archetype_specific,L7_BIO_HEALTHCARE_MEDICAL,C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT,0,1,+1,"medical-AI/device reimbursement evidence must include adoption/reimbursement/margin bridge before Green","reduces ISENS false-positive while preserving VUNO/JLK/Vatech Stage2",R7L13-C25-338220-T1-STAGE2A-20230602|R7L13-C25-322510-T1-STAGE2A-20230517|R7L13-C25-099190-T1-CGM-STAGE2-20230718|R7L13-C25-043150-T1-EXPORT-RECOVERY-20230329,4,4,1,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,C25_high_MAE_medical_AI_guard,canonical_archetype_specific,L7_BIO_HEALTHCARE_MEDICAL,C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT,0,1,+1,"JLK/VUNO show very high upside but high drawdown after blowoff; Green must wait for conversion evidence","keeps Stage2 actionable but blocks premature Green",R7L13-C25-322510-T1-STAGE2A-20230517|R7L13-C25-322510-T2-PRICE-ONLY-4B-20230724,4,4,1,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,C25_price_only_4B_overlay_guard,canonical_archetype_specific,L7_BIO_HEALTHCARE_MEDICAL,C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT,0,1,+1,"price-only local peaks in medical-AI devices need non-price valuation/revenue lag evidence to become full 4B","splits VUNO good 4B from JLK price-only overlay",R7L13-C25-338220-T2-4B-20230906|R7L13-C25-322510-T2-PRICE-ONLY-4B-20230724,4,4,1,medium,canonical_shadow_only,"not production; post-calibrated residual"
```

## 25. Machine-Readable Rows

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration"}
{"row_type": "case", "case_id": "R7L13-C25-338220-VUNO-MEDICAL-AI-REIMBURSEMENT-RERATING", "symbol": "338220", "company_name": "뷰노", "round": "R7", "loop": "13", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT", "fine_archetype_id": "MEDICAL_AI_REIMBURSEMENT_EXPORT_REORDER_MARGIN_BRIDGE", "case_type": "structural_success", "positive_or_counterexample": "positive", "best_trigger": "R7L13-C25-338220-T1-STAGE2A-20230602", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "see_trigger_rows", "current_profile_verdict": "current_profile_missed_structural", "price_source": "Songdaiki/stock-web", "notes": "medical-AI hospital-adoption/reimbursement optionality converted into a real rerating, but later 4B needed non-price valuation/revenue lag evidence."}
{"row_type": "case", "case_id": "R7L13-C25-322510-JLK-STROKE-AI-REIMBURSEMENT-HIGH-MAE", "symbol": "322510", "company_name": "제이엘케이", "round": "R7", "loop": "13", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT", "fine_archetype_id": "MEDICAL_AI_REIMBURSEMENT_EXPORT_REORDER_MARGIN_BRIDGE", "case_type": "high_mae_success", "positive_or_counterexample": "positive", "best_trigger": "R7L13-C25-322510-T1-STAGE2A-20230517", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "see_trigger_rows", "current_profile_verdict": "current_profile_too_early", "price_source": "Songdaiki/stock-web", "notes": "stroke-AI reimbursement narrative had enormous upside but entry-day and post-peak drawdown prove C25 medical AI should be promoted with a high-MAE guard."}
{"row_type": "case", "case_id": "R7L13-C25-099190-ISENS-CGM-LAUNCH-FAILED-RERATING", "symbol": "099190", "company_name": "아이센스", "round": "R7", "loop": "13", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT", "fine_archetype_id": "MEDICAL_AI_REIMBURSEMENT_EXPORT_REORDER_MARGIN_BRIDGE", "case_type": "failed_rerating", "positive_or_counterexample": "counterexample", "best_trigger": "R7L13-C25-099190-T1-CGM-STAGE2-20230718", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "see_trigger_rows", "current_profile_verdict": "current_profile_false_positive", "price_source": "Songdaiki/stock-web", "notes": "CGM launch/reimbursement expectation was not enough without confirmed adoption, reimbursement, and margin bridge; high MAE dominated modest MFE."}
{"row_type": "case", "case_id": "R7L13-C25-043150-VATECH-DENTAL-IMAGING-EXPORT-RECOVERY", "symbol": "043150", "company_name": "바텍", "round": "R7", "loop": "13", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT", "fine_archetype_id": "MEDICAL_AI_REIMBURSEMENT_EXPORT_REORDER_MARGIN_BRIDGE", "case_type": "stage2_promote_candidate", "positive_or_counterexample": "positive", "best_trigger": "R7L13-C25-043150-T1-EXPORT-RECOVERY-20230329", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "see_trigger_rows", "current_profile_verdict": "current_profile_correct", "price_source": "Songdaiki/stock-web", "notes": "dental imaging export recovery showed a cleaner low-MAE Stage2 path, but later growth deceleration argues against stale Green."}
{"row_type": "case", "case_id": "R7L13-C25-328130-LUNIT-MEDICAL-AI-NARRATIVE-BLOCKED", "symbol": "328130", "company_name": "루닛", "round": "R7", "loop": "13", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT", "fine_archetype_id": "MEDICAL_AI_REIMBURSEMENT_EXPORT_REORDER_MARGIN_BRIDGE", "case_type": "narrative_only", "positive_or_counterexample": "counterexample", "best_trigger": "narrative_only", "calibration_usable": false, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "narrative_only_blocked", "current_profile_verdict": "current_profile_data_insufficient", "price_source": "Songdaiki/stock-web", "notes": "C25-relevant medical-AI approval/commercialization narrative, but stock-web profile has corporate-action candidates in 2023-11/2023-12; quantitative weight calibration is blocked for that window."}
{"row_type": "trigger", "trigger_id": "R7L13-C25-338220-T1-STAGE2A-20230602", "case_id": "R7L13-C25-338220-VUNO-MEDICAL-AI-REIMBURSEMENT-RERATING", "symbol": "338220", "company_name": "뷰노", "round": "R7", "loop": "13", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT", "fine_archetype_id": "MEDICAL_AI_REIMBURSEMENT_EXPORT_REORDER_MARGIN_BRIDGE", "sector": "bio_healthcare_medical_device_ai", "primary_archetype": "medical_device_export_reimbursement_or_medical_ai_adoption", "loop_objective": "coverage_gap_fill|counterexample_mining|residual_false_positive_mining|4B_non_price_requirement_stress_test|canonical_archetype_compression", "trigger_type": "Stage2-Actionable", "trigger_date": "2023-06-02", "evidence_available_at_that_date": "medical-AI hospital-adoption/reimbursement-optionality proxy with public price/volume confirmation; price row shows 2023-06-02 close 23650 after the early June re-rating break.", "evidence_source": "research_proxy_public_news_company_disclosure_and_stock_web_row", "stage2_evidence_fields": ["public_event_or_disclosure", "customer_or_order_quality", "relative_strength", "capacity_or_volume_route", "policy_or_regulatory_optionality", "early_revision_signal"], "stage3_evidence_fields": ["multiple_public_sources", "repeat_order_or_conversion"], "stage4b_evidence_fields": [], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/338/338220/2023.csv", "profile_path": "atlas/symbol_profiles/338/338220.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2023-06-02", "entry_price": 23650, "MFE_30D_pct": 72.09, "MFE_90D_pct": 193.87, "MFE_180D_pct": 193.87, "MFE_1Y_pct": 193.87, "MFE_2Y_pct": 193.87, "MAE_30D_pct": -6.77, "MAE_90D_pct": -6.77, "MAE_180D_pct": -6.77, "MAE_1Y_pct": -6.77, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2023-09-07", "peak_price": 69500, "drawdown_after_peak_pct": -70.72, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": null, "four_b_evidence_type": [], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "durable_medical_ai_reimbursement_rerating_with_later_4B_need", "current_profile_verdict": "current_profile_missed_structural", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R7L13-C25-338220-20230602", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "R7L13-C25-338220-T2-4B-20230906", "case_id": "R7L13-C25-338220-VUNO-MEDICAL-AI-REIMBURSEMENT-RERATING", "symbol": "338220", "company_name": "뷰노", "round": "R7", "loop": "13", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT", "fine_archetype_id": "MEDICAL_AI_REIMBURSEMENT_EXPORT_REORDER_MARGIN_BRIDGE", "sector": "bio_healthcare_medical_device_ai", "primary_archetype": "medical_device_export_reimbursement_or_medical_ai_adoption", "loop_objective": "coverage_gap_fill|counterexample_mining|residual_false_positive_mining|4B_non_price_requirement_stress_test|canonical_archetype_compression", "trigger_type": "Stage4B", "trigger_date": "2023-09-06", "evidence_available_at_that_date": "vertical rerating after medical-AI adoption narrative; valuation and revenue-lag evidence present enough to treat as 4B overlay rather than pure price-only exit.", "evidence_source": "research_proxy_public_news_valuation_revenue_lag_and_stock_web_row", "stage2_evidence_fields": [], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["valuation_blowoff", "positioning_overheat", "margin_or_backlog_slowdown"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/338/338220/2023.csv", "profile_path": "atlas/symbol_profiles/338/338220.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2023-09-06", "entry_price": 65500, "MFE_30D_pct": 6.11, "MFE_90D_pct": 6.11, "MFE_180D_pct": 6.11, "MFE_1Y_pct": 6.11, "MFE_2Y_pct": 6.11, "MAE_30D_pct": -47.18, "MAE_90D_pct": -63.59, "MAE_180D_pct": -59.31, "MAE_1Y_pct": -59.31, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2023-09-07", "peak_price": 69500, "drawdown_after_peak_pct": -70.72, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.91, "four_b_full_window_peak_proximity": 0.91, "four_b_timing_verdict": "good_full_window_4B_timing", "four_b_evidence_type": ["valuation_blowoff", "positioning_overheat", "margin_or_backlog_slowdown"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "good_4B_overlay_after_medical_ai_blowoff", "current_profile_verdict": "current_profile_4B_too_late", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R7L13-C25-338220-20230906-4B", "dedupe_for_aggregate": false, "aggregate_group_role": "4B_overlay_only", "is_new_independent_case": true, "reuse_reason": "same symbol but different 4B trigger family; overlay not representative aggregate", "independent_evidence_weight": 0.25, "do_not_count_as_new_case": true}
{"row_type": "trigger", "trigger_id": "R7L13-C25-322510-T1-STAGE2A-20230517", "case_id": "R7L13-C25-322510-JLK-STROKE-AI-REIMBURSEMENT-HIGH-MAE", "symbol": "322510", "company_name": "제이엘케이", "round": "R7", "loop": "13", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT", "fine_archetype_id": "MEDICAL_AI_REIMBURSEMENT_EXPORT_REORDER_MARGIN_BRIDGE", "sector": "bio_healthcare_medical_device_ai", "primary_archetype": "medical_device_export_reimbursement_or_medical_ai_adoption", "loop_objective": "coverage_gap_fill|counterexample_mining|residual_false_positive_mining|4B_non_price_requirement_stress_test|canonical_archetype_compression", "trigger_type": "Stage2-Actionable", "trigger_date": "2023-05-17", "evidence_available_at_that_date": "stroke-AI reimbursement/adoption narrative broke above prior range; stock-web row shows 2023-05-17 close 7700 with high-volume move.", "evidence_source": "research_proxy_public_news_and_stock_web_row", "stage2_evidence_fields": ["public_event_or_disclosure", "relative_strength", "policy_or_regulatory_optionality", "early_revision_signal"], "stage3_evidence_fields": ["multiple_public_sources"], "stage4b_evidence_fields": [], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/322/322510/2023.csv", "profile_path": "atlas/symbol_profiles/322/322510.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2023-05-17", "entry_price": 7700, "MFE_30D_pct": 146.75, "MFE_90D_pct": 402.6, "MFE_180D_pct": 402.6, "MFE_1Y_pct": 402.6, "MFE_2Y_pct": 402.6, "MAE_30D_pct": -19.48, "MAE_90D_pct": -19.48, "MAE_180D_pct": -19.48, "MAE_1Y_pct": -19.48, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2023-09-07", "peak_price": 38700, "drawdown_after_peak_pct": -80.26, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": null, "four_b_evidence_type": [], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "high_mfe_high_mae_medical_ai_reimbursement_success", "current_profile_verdict": "current_profile_too_early", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window; corporate_action_candidate_date_2024-10-30_outside_window", "same_entry_group_id": "R7L13-C25-322510-20230517", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "R7L13-C25-322510-T2-PRICE-ONLY-4B-20230724", "case_id": "R7L13-C25-322510-JLK-STROKE-AI-REIMBURSEMENT-HIGH-MAE", "symbol": "322510", "company_name": "제이엘케이", "round": "R7", "loop": "13", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT", "fine_archetype_id": "MEDICAL_AI_REIMBURSEMENT_EXPORT_REORDER_MARGIN_BRIDGE", "sector": "bio_healthcare_medical_device_ai", "primary_archetype": "medical_device_export_reimbursement_or_medical_ai_adoption", "loop_objective": "coverage_gap_fill|counterexample_mining|residual_false_positive_mining|4B_non_price_requirement_stress_test|canonical_archetype_compression", "trigger_type": "Stage4B", "trigger_date": "2023-07-24", "evidence_available_at_that_date": "local price vertical after reimbursement AI rerating; non-price evidence still thin, so this is overlay-only and not a full 4B unless valuation/revenue-lag evidence is confirmed.", "evidence_source": "research_proxy_stock_web_price_only_and_reimbursement_uncertainty", "stage2_evidence_fields": [], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["price_only", "valuation_blowoff", "positioning_overheat"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/322/322510/2023.csv", "profile_path": "atlas/symbol_profiles/322/322510.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2023-07-24", "entry_price": 37000, "MFE_30D_pct": 4.59, "MFE_90D_pct": 4.59, "MFE_180D_pct": 4.59, "MFE_1Y_pct": 4.59, "MFE_2Y_pct": 4.59, "MAE_30D_pct": -26.08, "MAE_90D_pct": -56.08, "MAE_180D_pct": -56.08, "MAE_1Y_pct": -56.08, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2023-09-07", "peak_price": 38700, "drawdown_after_peak_pct": -80.26, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.96, "four_b_full_window_peak_proximity": 0.95, "four_b_timing_verdict": "price_only_local_4B_needs_non_price_confirmation", "four_b_evidence_type": ["price_only", "valuation_blowoff", "positioning_overheat"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "price_only_4B_overlay_not_full_exit_until_non_price_evidence", "current_profile_verdict": "current_profile_4B_too_early", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window; corporate_action_candidate_date_2024-10-30_outside_window", "same_entry_group_id": "R7L13-C25-322510-20230724-4B", "dedupe_for_aggregate": false, "aggregate_group_role": "4B_overlay_only", "is_new_independent_case": true, "reuse_reason": "same symbol but different 4B timing family", "independent_evidence_weight": 0.25, "do_not_count_as_new_case": true}
{"row_type": "trigger", "trigger_id": "R7L13-C25-099190-T1-CGM-STAGE2-20230718", "case_id": "R7L13-C25-099190-ISENS-CGM-LAUNCH-FAILED-RERATING", "symbol": "099190", "company_name": "아이센스", "round": "R7", "loop": "13", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT", "fine_archetype_id": "MEDICAL_AI_REIMBURSEMENT_EXPORT_REORDER_MARGIN_BRIDGE", "sector": "bio_healthcare_medical_device_ai", "primary_archetype": "medical_device_export_reimbursement_or_medical_ai_adoption", "loop_objective": "coverage_gap_fill|counterexample_mining|residual_false_positive_mining|4B_non_price_requirement_stress_test|canonical_archetype_compression", "trigger_type": "Stage2", "trigger_date": "2023-07-18", "evidence_available_at_that_date": "CGM product-launch/reimbursement expectation produced a one-day rerating, but adoption/reimbursement/margin bridge was not confirmed enough for Green.", "evidence_source": "research_proxy_public_product_launch_news_and_stock_web_row", "stage2_evidence_fields": ["public_event_or_disclosure", "policy_or_regulatory_optionality", "relative_strength"], "stage3_evidence_fields": [], "stage4b_evidence_fields": [], "stage4c_evidence_fields": ["thesis_evidence_broken"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/099/099190/2023.csv", "profile_path": "atlas/symbol_profiles/099/099190.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2023-07-18", "entry_price": 32000, "MFE_30D_pct": 23.59, "MFE_90D_pct": 24.06, "MFE_180D_pct": 24.06, "MFE_1Y_pct": 24.06, "MFE_2Y_pct": 24.06, "MAE_30D_pct": -13.13, "MAE_90D_pct": -32.03, "MAE_180D_pct": -32.03, "MAE_1Y_pct": -43.5, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2023-09-08", "peak_price": 39700, "drawdown_after_peak_pct": -44.21, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": null, "four_b_evidence_type": [], "four_c_protection_label": "hard_4c_late", "trigger_outcome_label": "failed_CGM_reimbursement_rerating_high_MAE", "current_profile_verdict": "current_profile_false_positive", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window; corporate_action_candidate_dates_2023-03-14_2023-04-10_before_entry", "same_entry_group_id": "R7L13-C25-099190-20230718", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "R7L13-C25-043150-T1-EXPORT-RECOVERY-20230329", "case_id": "R7L13-C25-043150-VATECH-DENTAL-IMAGING-EXPORT-RECOVERY", "symbol": "043150", "company_name": "바텍", "round": "R7", "loop": "13", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT", "fine_archetype_id": "MEDICAL_AI_REIMBURSEMENT_EXPORT_REORDER_MARGIN_BRIDGE", "sector": "bio_healthcare_medical_device_ai", "primary_archetype": "medical_device_export_reimbursement_or_medical_ai_adoption", "loop_objective": "coverage_gap_fill|counterexample_mining|residual_false_positive_mining|4B_non_price_requirement_stress_test|canonical_archetype_compression", "trigger_type": "Stage2-Actionable", "trigger_date": "2023-03-29", "evidence_available_at_that_date": "dental imaging export recovery and order/margin bridge proxy; stock-web row shows 2023-03-29 close 32100 followed by low-MAE advance.", "evidence_source": "research_proxy_public_earnings_export_recovery_and_stock_web_row", "stage2_evidence_fields": ["public_event_or_disclosure", "customer_or_order_quality", "relative_strength", "capacity_or_volume_route"], "stage3_evidence_fields": ["margin_bridge", "financial_visibility", "low_red_team_risk"], "stage4b_evidence_fields": [], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/043/043150/2023.csv", "profile_path": "atlas/symbol_profiles/043/043150.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2023-03-29", "entry_price": 32100, "MFE_30D_pct": 38.79, "MFE_90D_pct": 38.79, "MFE_180D_pct": 38.79, "MFE_1Y_pct": 38.79, "MFE_2Y_pct": 38.79, "MAE_30D_pct": -6.23, "MAE_90D_pct": -6.23, "MAE_180D_pct": -7.79, "MAE_1Y_pct": -20.25, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2023-05-04", "peak_price": 44550, "drawdown_after_peak_pct": -51.74, "green_lateness_ratio": 0.42, "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": null, "four_b_evidence_type": [], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "clean_low_MAE_export_recovery_stage2", "current_profile_verdict": "current_profile_correct", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window; corporate_action_candidate_date_2010-09-02_outside_window", "same_entry_group_id": "R7L13-C25-043150-20230329", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R7L13-C25-338220-VUNO-MEDICAL-AI-REIMBURSEMENT-RERATING", "trigger_id": "R7L13-C25-338220-T1-STAGE2A-20230602", "symbol": "338220", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 7, "relative_strength_score": 12, "customer_quality_score": 8, "policy_or_regulatory_score": 8, "valuation_repricing_score": 6, "execution_risk_score": -7, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "device_export_score": 0, "medical_ai_reimbursement_score": 11, "hospital_adoption_score": 10, "installed_base_or_repeat_order_score": 0, "commercialization_bridge_score": 6, "positioning_overheat_score": 0, "thesis_break_score": 0}, "weighted_score_before": 74, "stage_label_before": "Stage2-Actionable", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 8, "relative_strength_score": 12, "customer_quality_score": 10, "policy_or_regulatory_score": 10, "valuation_repricing_score": 6, "execution_risk_score": -6, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "device_export_score": 0, "medical_ai_reimbursement_score": 14, "hospital_adoption_score": 12, "installed_base_or_repeat_order_score": 0, "commercialization_bridge_score": 8, "positioning_overheat_score": 0, "thesis_break_score": 0}, "weighted_score_after": 82, "stage_label_after": "Stage3-Yellow_after_adoption_bridge", "changed_components": ["medical_ai_reimbursement_score", "hospital_adoption_score", "commercialization_bridge_score"], "component_delta_explanation": "C25 shadow separates medical-AI reimbursement or device export evidence from price-only rerating, then requires adoption/reimbursement/margin confirmation before Green.", "MFE_90D_pct": 193.87, "MAE_90D_pct": -6.77, "score_return_alignment_label": "positive_alignment_after_reimbursement_bridge", "current_profile_verdict": "current_profile_missed_structural"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R7L13-C25-338220-VUNO-MEDICAL-AI-REIMBURSEMENT-RERATING", "trigger_id": "R7L13-C25-338220-T2-4B-20230906", "symbol": "338220", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 20, "customer_quality_score": 0, "policy_or_regulatory_score": 0, "valuation_repricing_score": 18, "execution_risk_score": -8, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "device_export_score": 0, "medical_ai_reimbursement_score": 8, "hospital_adoption_score": 6, "installed_base_or_repeat_order_score": 0, "commercialization_bridge_score": 0, "positioning_overheat_score": 20, "thesis_break_score": 0}, "weighted_score_before": 84, "stage_label_before": "Stage3-Green_or_4B_watch", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 20, "customer_quality_score": 0, "policy_or_regulatory_score": 0, "valuation_repricing_score": 20, "execution_risk_score": -12, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "device_export_score": 0, "medical_ai_reimbursement_score": 8, "hospital_adoption_score": 6, "installed_base_or_repeat_order_score": 0, "commercialization_bridge_score": 2, "positioning_overheat_score": 24, "thesis_break_score": 0}, "weighted_score_after": 70, "stage_label_after": "Stage4B_overlay", "changed_components": ["positioning_overheat_score", "execution_risk_score", "commercialization_bridge_score"], "component_delta_explanation": "C25 shadow separates medical-AI reimbursement or device export evidence from price-only rerating, then requires adoption/reimbursement/margin confirmation before Green.", "MFE_90D_pct": 6.11, "MAE_90D_pct": -63.59, "score_return_alignment_label": "4B_alignment_after_blowoff", "current_profile_verdict": "current_profile_4B_too_late"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R7L13-C25-322510-JLK-STROKE-AI-REIMBURSEMENT-HIGH-MAE", "trigger_id": "R7L13-C25-322510-T1-STAGE2A-20230517", "symbol": "322510", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 5, "relative_strength_score": 18, "customer_quality_score": 0, "policy_or_regulatory_score": 8, "valuation_repricing_score": 9, "execution_risk_score": -10, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "device_export_score": 0, "medical_ai_reimbursement_score": 10, "hospital_adoption_score": 4, "installed_base_or_repeat_order_score": 0, "commercialization_bridge_score": 0, "positioning_overheat_score": 0, "thesis_break_score": 0}, "weighted_score_before": 76, "stage_label_before": "Stage3-Yellow_candidate", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 4, "relative_strength_score": 18, "customer_quality_score": 0, "policy_or_regulatory_score": 8, "valuation_repricing_score": 9, "execution_risk_score": -15, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "device_export_score": 0, "medical_ai_reimbursement_score": 12, "hospital_adoption_score": 5, "installed_base_or_repeat_order_score": 0, "commercialization_bridge_score": 2, "positioning_overheat_score": 0, "thesis_break_score": 0}, "weighted_score_after": 70, "stage_label_after": "Stage2-Actionable_high_MAE_guard", "changed_components": ["execution_risk_score", "commercialization_bridge_score"], "component_delta_explanation": "C25 shadow separates medical-AI reimbursement or device export evidence from price-only rerating, then requires adoption/reimbursement/margin confirmation before Green.", "MFE_90D_pct": 402.6, "MAE_90D_pct": -19.48, "score_return_alignment_label": "positive_but_high_MAE_alignment", "current_profile_verdict": "current_profile_too_early"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R7L13-C25-322510-JLK-STROKE-AI-REIMBURSEMENT-HIGH-MAE", "trigger_id": "R7L13-C25-322510-T2-PRICE-ONLY-4B-20230724", "symbol": "322510", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 20, "customer_quality_score": 0, "policy_or_regulatory_score": 0, "valuation_repricing_score": 18, "execution_risk_score": -8, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "device_export_score": 0, "medical_ai_reimbursement_score": 7, "hospital_adoption_score": 0, "installed_base_or_repeat_order_score": 0, "commercialization_bridge_score": 0, "positioning_overheat_score": 22, "thesis_break_score": 0}, "weighted_score_before": 79, "stage_label_before": "Stage3-Yellow_or_4B_candidate", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 20, "customer_quality_score": 0, "policy_or_regulatory_score": 0, "valuation_repricing_score": 20, "execution_risk_score": -15, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "device_export_score": 0, "medical_ai_reimbursement_score": 7, "hospital_adoption_score": 0, "installed_base_or_repeat_order_score": 0, "commercialization_bridge_score": 0, "positioning_overheat_score": 24, "thesis_break_score": 0}, "weighted_score_after": 59, "stage_label_after": "4B_overlay_only_price_driven", "changed_components": ["positioning_overheat_score", "commercialization_bridge_score"], "component_delta_explanation": "C25 shadow separates medical-AI reimbursement or device export evidence from price-only rerating, then requires adoption/reimbursement/margin confirmation before Green.", "MFE_90D_pct": 4.59, "MAE_90D_pct": -56.08, "score_return_alignment_label": "price_only_4B_needs_non_price_confirmation", "current_profile_verdict": "current_profile_4B_too_early"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R7L13-C25-099190-ISENS-CGM-LAUNCH-FAILED-RERATING", "trigger_id": "R7L13-C25-099190-T1-CGM-STAGE2-20230718", "symbol": "099190", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 5, "relative_strength_score": 14, "customer_quality_score": 0, "policy_or_regulatory_score": 10, "valuation_repricing_score": 6, "execution_risk_score": -8, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "device_export_score": 0, "medical_ai_reimbursement_score": 11, "hospital_adoption_score": 0, "installed_base_or_repeat_order_score": 0, "commercialization_bridge_score": 2, "positioning_overheat_score": 0, "thesis_break_score": 0}, "weighted_score_before": 76, "stage_label_before": "Stage3-Yellow_candidate", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 2, "relative_strength_score": 14, "customer_quality_score": 0, "policy_or_regulatory_score": 8, "valuation_repricing_score": 5, "execution_risk_score": -18, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "device_export_score": 0, "medical_ai_reimbursement_score": 8, "hospital_adoption_score": 0, "installed_base_or_repeat_order_score": 0, "commercialization_bridge_score": 0, "positioning_overheat_score": 0, "thesis_break_score": -12}, "weighted_score_after": 49, "stage_label_after": "Stage2_watch_or_4C_watch", "changed_components": ["commercialization_bridge_score", "execution_risk_score", "thesis_break_score"], "component_delta_explanation": "C25 shadow separates medical-AI reimbursement or device export evidence from price-only rerating, then requires adoption/reimbursement/margin confirmation before Green.", "MFE_90D_pct": 24.06, "MAE_90D_pct": -32.03, "score_return_alignment_label": "false_positive_blocked_after", "current_profile_verdict": "current_profile_false_positive"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R7L13-C25-043150-VATECH-DENTAL-IMAGING-EXPORT-RECOVERY", "trigger_id": "R7L13-C25-043150-T1-EXPORT-RECOVERY-20230329", "symbol": "043150", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 8, "revision_score": 6, "relative_strength_score": 8, "customer_quality_score": 8, "policy_or_regulatory_score": 0, "valuation_repricing_score": 0, "execution_risk_score": -4, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "device_export_score": 11, "medical_ai_reimbursement_score": 0, "hospital_adoption_score": 0, "installed_base_or_repeat_order_score": 8, "commercialization_bridge_score": 8, "positioning_overheat_score": 0, "thesis_break_score": 0}, "weighted_score_before": 78, "stage_label_before": "Stage3-Yellow_candidate", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 9, "revision_score": 6, "relative_strength_score": 8, "customer_quality_score": 8, "policy_or_regulatory_score": 0, "valuation_repricing_score": 0, "execution_risk_score": -5, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "device_export_score": 12, "medical_ai_reimbursement_score": 0, "hospital_adoption_score": 0, "installed_base_or_repeat_order_score": 9, "commercialization_bridge_score": 9, "positioning_overheat_score": 0, "thesis_break_score": 0}, "weighted_score_after": 82, "stage_label_after": "Stage3-Yellow", "changed_components": ["device_export_score", "installed_base_or_repeat_order_score"], "component_delta_explanation": "C25 shadow separates medical-AI reimbursement or device export evidence from price-only rerating, then requires adoption/reimbursement/margin confirmation before Green.", "MFE_90D_pct": 38.79, "MAE_90D_pct": -6.23, "score_return_alignment_label": "clean_low_MAE_alignment", "current_profile_verdict": "current_profile_correct"}
{"row_type": "residual_contribution", "round": "R7", "loop": "13", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT", "scheduled_round": "R7", "scheduled_loop": 13, "round_schedule_status": "valid", "round_sector_consistency": "pass", "new_independent_case_count": 5, "reused_case_count": 0, "new_symbol_count": 5, "same_archetype_new_symbol_count": 5, "same_archetype_new_trigger_family_count": 5, "new_trigger_family_count": 5, "positive_case_count": 3, "counterexample_count": 2, "current_profile_error_count": 3, "diversity_score_summary": "new C25 medical-AI/reimbursement/device-export names after R7 loops 10-12; avoids prior Classys, PharmaResearch, Dentium, Dio, Yuhan, Alteogen, Hugel, HLB, Oscotec, Shinpoong rows", "tested_existing_calibrated_axes": ["stage2_actionable_evidence_bonus", "stage3_green_revision_min", "price_only_blowoff_blocks_positive_stage", "full_4b_requires_non_price_evidence", "hard_4c_thesis_break_routes_to_4c"], "residual_error_types_found": ["current_profile_missed_structural", "current_profile_too_early", "current_profile_false_positive", "current_profile_4B_too_late"], "loop_contribution_label": "canonical_archetype_rule_candidate", "do_not_propose_new_weight_delta": false}
{"row_type": "narrative_only", "case_id": "R7L13-C25-328130-LUNIT-MEDICAL-AI-NARRATIVE-BLOCKED", "symbol": "328130", "company_name": "루닛", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT", "reason": "C25 medical-AI approval/commercialization narrative is relevant, but stock-web profile has corporate_action_candidate_dates 2023-11-09 and 2023-12-01 inside a representative 2023 catalyst forward window; quantitative calibration blocked.", "price_source": "Songdaiki/stock-web", "usage": "not_weight_calibration", "profile_path": "atlas/symbol_profiles/328/328130.json"}
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
completed_round = R7
completed_loop = 13
next_round = R8
next_loop = 13
round_schedule_status = valid
round_sector_consistency = pass
```

## 28. Source Notes

```text
Stock-Web files checked:
- atlas/manifest.json
- atlas/symbol_profiles/338/338220.json
- atlas/symbol_profiles/322/322510.json
- atlas/symbol_profiles/099/099190.json
- atlas/symbol_profiles/043/043150.json
- atlas/symbol_profiles/328/328130.json
- atlas/ohlcv_tradable_by_symbol_year/338/338220/2023.csv and 2024.csv
- atlas/ohlcv_tradable_by_symbol_year/322/322510/2023.csv
- atlas/ohlcv_tradable_by_symbol_year/099/099190/2023.csv
- atlas/ohlcv_tradable_by_symbol_year/043/043150/2023.csv

Evidence-source labels are historical research proxies. They are not live candidate research and should not be interpreted as investment recommendations.
```

