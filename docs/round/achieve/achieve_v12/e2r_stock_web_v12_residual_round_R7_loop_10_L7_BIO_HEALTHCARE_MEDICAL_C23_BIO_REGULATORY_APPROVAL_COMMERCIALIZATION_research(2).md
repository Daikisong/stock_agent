# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
research_session = post_calibrated_sector_archetype_residual_research
scheduled_round = R7
scheduled_loop = 10
round_schedule_status = valid
round_sector_consistency = pass
large_sector_id = L7_BIO_HEALTHCARE_MEDICAL
canonical_archetype_id = C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION
fine_archetype_id = BIO_APPROVAL_TO_COMMERCIALIZATION_ROYALTY_BRIDGE
output_file = e2r_stock_web_v12_residual_round_R7_loop_10_L7_BIO_HEALTHCARE_MEDICAL_C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION_research.md
production_scoring_changed = false
shadow_weight_only = true
handoff_prompt_embedded = true
handoff_prompt_executed_now = false
```

This loop adds 3 new independent cases, 1 counterexample, and 2 residual errors for R7/L7_BIO_HEALTHCARE_MEDICAL/C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION.

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

This MD does not re-prove the global Stage2/Green/4B axes. It isolates a C23 residual: **regulatory approval is not one state**. Approval with a partner/commercialization/royalty bridge behaved differently from pre-approval event optionality.

## 2. Round / Large Sector / Canonical Archetype Scope

```text
round = R7
large_sector_id = L7_BIO_HEALTHCARE_MEDICAL
canonical_archetype_id = C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION
fine_archetype_id = BIO_APPROVAL_TO_COMMERCIALIZATION_ROYALTY_BRIDGE
allowed_canonical_scope = C23 / C24 / C25
selected_canonical_scope = C23
```

R7 hard gate passes because the output sector is `L7_BIO_HEALTHCARE_MEDICAL`.

## 3. Previous Coverage / Duplicate Avoidance Check

Allowed research artifacts indicate historical calibration already covers R1~R13 and loops 1~9. This file continues the sequential cycle as R7 Loop 10. Prior R7 research may include biotech/healthcare cases, but this loop deliberately selects three **new symbol-level C23 paths**:

- 유한양행 / lazertinib approval with partner commercialization route.
- 휴젤 / Letybo FDA approval with delayed commercial follow-through.
- HLB / pre-approval PDUFA expectation that failed into a CRL-style thesis break.

```text
same_canonical_archetype_research = allowed
same_symbol_same_trigger_date_research = avoided
new_symbol_count = 3
new_independent_case_count = 3
reused_case_count = 0
minimum_new_independent_case_ratio = pass
```

## 4. Stock-Web OHLC Input / Price Source Validation

```text
price_data_source = Songdaiki/stock-web
source_basis = FinanceData/marcap
price_basis = tradable_raw
price_adjustment_status = raw_unadjusted_marcap
manifest_path = atlas/manifest.json
stock_web_manifest_max_date = 2026-02-20
calibration_shard_root = atlas/ohlcv_tradable_by_symbol_year
raw_shard_root = atlas/ohlcv_raw_by_symbol_year
```

Stock-web manifest confirms raw/unadjusted OHLC, calibration-safe tradable shards, and corporate-action contaminated windows blocked by default.

## 5. Historical Eligibility Gate

| symbol | profile | trigger window | 180D clean? | calibration_usable |
|---|---|---:|---:|---:|
| 000100 유한양행 | atlas/symbol_profiles/000/000100.json | 2024-08-21~D+180 | corporate action candidates are historical only, not in 2024 window | true |
| 145020 휴젤 | atlas/symbol_profiles/145/145020.json | 2024-03-04~D+180 | candidate dates in 2017/2020 only, not in 2024 window | true |
| 028300 HLB | atlas/symbol_profiles/028/028300.json | 2024-04-22~D+180 | candidate dates end in 2021, not in 2024 window | true |

## 6. Canonical Archetype Compression Map

```text
C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION
  ├─ approval_to_commercialization_partner_royalty_bridge
  ├─ approval_to_US_market_access_route
  └─ pre_approval_event_optional_without_approval_proof
```

Compression rule: approval plus monetization bridge can score positively; pre-approval event optionality without approval proof must remain capped.

## 7. Case Selection Summary

|case_id|symbol|company_name|case_type|positive_or_counterexample|current_profile_verdict|
|---|---|---|---|---|---|
|R7L10_C23_YUHAN_LAZCLUZE_APPROVAL|000100|유한양행|structural_success|positive|current_profile_too_late|
|R7L10_C23_HUGEL_LETYBO_FDA_APPROVAL|145020|휴젤|stage2_promote_candidate|positive|current_profile_correct|
|R7L10_C23_HLB_CRL_FAILURE|028300|HLB|failed_rerating|counterexample|current_profile_false_positive|

## 8. Positive vs Counterexample Balance

```text
positive_case_count = 2
counterexample_count = 1
4B_case_count = 1
4C_case_count = 1
calibration_usable_case_count = 3
calibration_usable_trigger_count = 4
```

The sample satisfies the minimum balance: at least one positive case, one counterexample, and three usable cases.

## 9. Evidence Source Map

| case | stage2 evidence | stage3 evidence | 4B/4C evidence |
|---|---|---|---|
| 유한양행 | FDA approval of lazertinib + amivantamab; partner commercialization path | royalty/commercial visibility and revision path | valuation/positioning watch after rapid move |
| 휴젤 | FDA approval of Letybo; US glabellar-line market access | later commercialization availability and channel proof | valuation/revision watch after late 2024 rally |
| HLB | pre-PDUFA expectation and relative-strength run-up | absent approval/commercial proof | CRL/regulatory rejection breaks thesis |

## 10. Price Data Source Map

| symbol | shard | profile |
|---|---|---|
| 000100 | atlas/ohlcv_tradable_by_symbol_year/000/000100/2024.csv; 2025.csv | atlas/symbol_profiles/000/000100.json |
| 145020 | atlas/ohlcv_tradable_by_symbol_year/145/145020/2024.csv | atlas/symbol_profiles/145/145020.json |
| 028300 | atlas/ohlcv_tradable_by_symbol_year/028/028300/2024.csv | atlas/symbol_profiles/028/028300.json |

## 11. Case-by-Case Trigger Grid

|trigger_id|symbol|type|trigger|entry|entry_price|MFE90|MAE90|MFE180|verdict|usable|
|---|---|---|---|---|---|---|---|---|---|---|
|TRG_R7L10_YUHAN_2024-08-21_APPROVAL_COMMERCIALIZATION|000100|Stage2-Actionable|2024-08-20|2024-08-21|94300|76.99|-2.97|76.99|current_profile_too_late|True|
|TRG_R7L10_HUGEL_2024-03-04_FDA_LETYBO|145020|Stage2-Actionable|2024-02-29|2024-03-04|202500|10.62|-14.91|60.99|current_profile_correct|True|
|TRG_R7L10_HLB_2024-04-22_PDUFA_RUNUP|028300|Stage2-Actionable|2024-04-22|2024-04-22|106300|5.93|-57.53|5.93|current_profile_false_positive|True|
|TRG_R7L10_HLB_2024-05-17_CRL_4C|028300|4C|2024-05-17|2024-05-17|67100|46.2|-32.71|46.2|current_profile_4C_too_late_if_waiting_for_confirmed_financials|True|

## 12. Trigger-Level OHLC Backtest Tables

### 12.1 Representative triggers

| case | entry | entry price | 30D MFE/MAE | 90D MFE/MAE | 180D MFE/MAE | peak | drawdown after peak |
|---|---:|---:|---:|---:|---:|---|---:|
| 유한양행 | 2024-08-21 | 94,300 | +69.99% / -2.97% | +76.99% / -2.97% | +76.99% / -2.97% | 2024-10-15 / 166,900 | -39.84% |
| 휴젤 | 2024-03-04 | 202,500 | +8.15% / -14.91% | +10.62% / -14.91% | +60.99% / -14.91% | 2024-11-07 / 326,000 | -20.25% |
| HLB pre-approval | 2024-04-22 | 106,300 | +5.93% / -57.53% | +5.93% / -57.53% | +5.93% / -57.53% | 2024-04-25 / 112,600 | -59.90% |

### 12.2 4C overlay trigger

| case | 4C entry | entry price | 30D MFE/MAE | 90D MFE/MAE | 180D MFE/MAE | 4C label |
|---|---:|---:|---:|---:|---:|---|
| HLB CRL | 2024-05-17 | 67,100 | +9.99% / -32.71% | +46.20% / -32.71% | +46.20% / -32.71% | hard_4c_success_with_whipsaw_risk |

## 13. Current Calibrated Profile Stress Test

| case | current profile likely judgment | outcome | verdict |
|---|---|---|---|
| 유한양행 | Stage2/Yellow, Green delayed until revision proof | strong MFE before/around confirmation | current_profile_too_late |
| 휴젤 | Stage2 with high-MAE watch, later Yellow/Green as commercialization evidence appears | high-MAE but eventual +60.99% 180D MFE | current_profile_correct |
| HLB | event-risk Stage2 could be over-scored if regulatory optionality is not capped | +5.93% MFE then -57.53% MAE | current_profile_false_positive |

## 14. Stage2 / Yellow / Green Comparison

```text
Yuhan_green_lateness_ratio = 0.44
Hugel_green_lateness_ratio = 0.57
HLB_green_lateness_ratio = not_applicable
```

For C23, Green must not be delayed until all sales are visible when approval plus partner commercialization is already public. But Green must also not be granted to pre-approval event optionality.

## 15. 4B Local vs Full-window Timing Audit

| case | local 4B proximity | full-window 4B proximity | timing verdict |
|---|---:|---:|---|
| 유한양행 | 0.90 | 0.90 | watch-only; require non-price valuation/revision slowdown for full 4B |
| 휴젤 | 0.94 | 0.94 | good full-window 4B only if non-price valuation/revision evidence exists |
| HLB | 0.94 | 0.94 | event-premium 4B watch before CRL; not price-only positive signal |

## 16. 4C Protection Audit

HLB demonstrates a C23 hard 4C path: regulatory rejection breaks the thesis. The 4C event did not eliminate rebound/whipsaw risk, but it correctly separated broken thesis from ordinary drawdown.

```text
four_c_protection_label = hard_4c_success_with_whipsaw_risk
hard_4c_route_strengthened = true
```

## 17. Sector-Specific Rule Candidate

```text
rule_scope = sector_specific
axis = approval_commercialization_bridge_required
proposal = In L7, regulatory approval should receive positive treatment only when paired with commercialization/partner/reimbursement/royalty bridge.
```

## 18. Canonical-Archetype Rule Candidate

```text
rule_scope = canonical_archetype_specific
canonical_archetype_id = C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION

candidate_rules:
1. c23_approval_to_commercialization_bridge_bonus = +1 shadow
2. c23_pre_approval_event_risk_cap = +1 guard
3. c23_crl_hard_4c_route = strengthen existing hard 4C routing
```

## 19. Before / After Backtest Comparison

|profile_id|profile_scope|profile_hypothesis|changed_axes|eligible_trigger_count|avg_MFE_90D_pct|avg_MAE_90D_pct|false_positive_rate|score_return_alignment_verdict|
|---|---|---|---|---|---|---|---|---|
|P0|current calibrated proxy|generic e2r_2_1 calibrated profile|none|3|31.18|-25.14|0.33|mixed|
|P0b|rollback reference|e2r_2_0 baseline reference|pre-stock-web thresholds|3|31.18|-25.14|0.33|worse_late_green_and_event_risk|
|P1|sector_specific_candidate_profile|R7 approval events need commercialization bridge and 4C CRL guard|sector approval bridge +1; pre-approval event cap +1|3|31.18|-25.14|0.0|improved|
|P2|canonical_archetype_candidate_profile|C23 distinguishes approval-to-commercialization from pre-approval optionality|c23 bridge bonus; c23 pre-approval cap; c23 CRL hard route|3|31.18|-25.14|0.0|best|
|P3|counterexample_guard_profile|CRL/regulatory rejection overrides positive labels|hard 4C after thesis break|1|5.93|-57.53|0.0|protective|

## 20. Score-Return Alignment Matrix

| symbol | raw profile score before | stage before | raw score after | stage after | alignment |
|---|---:|---|---:|---|---|
| 000100 | 84 | Stage3-Yellow | 92 | Stage3-Green | improved: catches approval bridge earlier |
| 145020 | 73 | Stage2-Actionable | 81 | Stage3-Yellow | improved but high-MAE watch remains |
| 028300 | 70 | Stage2/Yellow watch | 51 | Stage1/4C-watch | improved: prevents pre-approval false positive |

## 21. Coverage Matrix

|large_sector_id|canonical_archetype_id|fine_archetype_id|positive_case_count|counterexample_count|4B_case_count|4C_case_count|new_independent_case_count|reused_case_count|calibration_usable_trigger_count|representative_trigger_count|current_profile_error_count|sector_rule_candidate|canonical_rule_candidate|coverage_gap_after_this_loop|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|L7_BIO_HEALTHCARE_MEDICAL|C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION|BIO_APPROVAL_TO_COMMERCIALIZATION_ROYALTY_BRIDGE|2|1|1|1|3|0|4|3|2|True|True|exact original evidence URL enrichment and more post-commercialization sales/royalty cases|

## 22. Residual Contribution Summary

```text
new_independent_case_count: 3
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 3
new_canonical_archetype_count: 0
new_fine_archetype_count: 1
new_trigger_family_count: 3
tested_existing_calibrated_axes:
  - stage2_actionable_evidence_bonus
  - stage3_green_revision_min
  - full_4b_requires_non_price_evidence
  - hard_4c_thesis_break_routes_to_4c
residual_error_types_found:
  - current_profile_too_late_for_approval_commercialization_bridge
  - current_profile_false_positive_for_pre_approval_event_risk
new_axis_proposed:
  - c23_approval_to_commercialization_bridge_bonus
  - c23_pre_approval_event_risk_cap
existing_axis_strengthened:
  - hard_4c_thesis_break_routes_to_4c
  - full_4b_requires_non_price_evidence
existing_axis_weakened: null
existing_axis_kept:
  - price_only_blowoff_blocks_positive_stage
sector_specific_rule_candidate: true
canonical_archetype_rule_candidate: true
no_new_signal_reason: null
loop_contribution_label: canonical_archetype_rule_candidate
do_not_propose_new_weight_delta: false
```

## 23. Validation Scope / Non-Validation Scope

Validation scope:

- Actual stock-web 1D OHLC rows.
- 30D/90D/180D MFE/MAE.
- Clean 180D corporate-action windows.
- Stage2/Stage3/4B/4C evidence separation.

Non-validation scope:

- No live candidate discovery.
- No current watchlist.
- No stock_agent source-code access.
- No production scoring change.
- Exact primary evidence URLs should be enriched during implementation before any promotion.

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,c23_approval_to_commercialization_bridge,canonical_archetype_specific,L7_BIO_HEALTHCARE_MEDICAL,C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION,0,1,+1,"approval plus partner/commercialization/royalty bridge separated Yuhan/Hugel from pre-approval event beta","reduces missed structural and late Green for true approval bridge","TRG_R7L10_YUHAN_2024-08-21_APPROVAL_COMMERCIALIZATION|TRG_R7L10_HUGEL_2024-03-04_FDA_LETYBO",3,3,1,medium,canonical_shadow_only,"not production; source URL enrichment required"
shadow_weight,c23_pre_approval_event_risk_cap,canonical_archetype_specific,L7_BIO_HEALTHCARE_MEDICAL,C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION,0,1,+1,"PDUFA/regulatory expectation without approval/commercialization proof produced HLB false positive","caps Stage2/Yellow before approval and routes CRL to 4C","TRG_R7L10_HLB_2024-04-22_PDUFA_RUNUP|TRG_R7L10_HLB_2024-05-17_CRL_4C",3,3,1,medium,canonical_shadow_only,"4C protection overlay; not a sell recommendation"
```

## 25. Machine-Readable Rows

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration"}
{"row_type": "case", "case_id": "R7L10_C23_YUHAN_LAZCLUZE_APPROVAL", "symbol": "000100", "company_name": "유한양행", "round": "R7", "loop": "10", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION", "fine_archetype_id": "BIO_APPROVAL_TO_COMMERCIALIZATION_ROYALTY_BRIDGE", "case_type": "structural_success", "positive_or_counterexample": "positive", "best_trigger": "TRG_R7L10_YUHAN_2024-08-21_APPROVAL_COMMERCIALIZATION", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "aligned_positive", "current_profile_verdict": "current_profile_too_late", "price_source": "Songdaiki/stock-web", "notes": "FDA approval of lazertinib + amivantamab created a regulatory approval plus partner commercialization/royalty route rather than a single local biotech event."}
{"row_type": "case", "case_id": "R7L10_C23_HUGEL_LETYBO_FDA_APPROVAL", "symbol": "145020", "company_name": "휴젤", "round": "R7", "loop": "10", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION", "fine_archetype_id": "BIO_APPROVAL_TO_COMMERCIALIZATION_ROYALTY_BRIDGE", "case_type": "stage2_promote_candidate", "positive_or_counterexample": "positive", "best_trigger": "TRG_R7L10_HUGEL_2024-03-04_FDA_LETYBO", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "aligned_positive", "current_profile_verdict": "current_profile_correct", "price_source": "Songdaiki/stock-web", "notes": "FDA approval of Letybo/letibotulinumtoxinA gave a direct US commercialization option; initial path had drawdown but the 180D follow-through improved as commercialization visibility developed."}
{"row_type": "case", "case_id": "R7L10_C23_HLB_CRL_FAILURE", "symbol": "028300", "company_name": "HLB", "round": "R7", "loop": "10", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION", "fine_archetype_id": "BIO_APPROVAL_TO_COMMERCIALIZATION_ROYALTY_BRIDGE", "case_type": "failed_rerating", "positive_or_counterexample": "counterexample", "best_trigger": "TRG_R7L10_HLB_2024-04-22_PDUFA_RUNUP", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "counterexample_guard_needed", "current_profile_verdict": "current_profile_false_positive", "price_source": "Songdaiki/stock-web", "notes": "Pre-PDUFA expectation without approval/commercialization bridge became a classic C23 false positive and hard 4C when the CRL arrived."}
{"row_type": "trigger", "trigger_id": "TRG_R7L10_YUHAN_2024-08-21_APPROVAL_COMMERCIALIZATION", "case_id": "R7L10_C23_YUHAN_LAZCLUZE_APPROVAL", "symbol": "000100", "company_name": "유한양행", "round": "R7", "loop": "10", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION", "fine_archetype_id": "BIO_APPROVAL_TO_COMMERCIALIZATION_ROYALTY_BRIDGE", "sector": "바이오·헬스케어·의료기기", "primary_archetype": "approval_to_commercialization_royalty_bridge", "loop_objective": "coverage_gap_fill|sector_specific_rule_discovery|stage2_actionable_bonus_stress_test|green_strictness_stress_test|4B_non_price_requirement_stress_test|4C_thesis_break_timing_test|counterexample_mining", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-08-20", "entry_date": "2024-08-21", "entry_price": 94300, "evidence_available_at_that_date": "FDA approval of lazertinib with amivantamab for first-line EGFR-mutated NSCLC; partner/Janssen commercialization route implied non-local revenue/royalty optionality.", "evidence_source": "FDA/J&J approval reporting; Reuters later noted Aug approval of Rybrevant + lazertinib; exact original press URL should be attached in implementation.", "stage2_evidence_fields": ["public_event_or_disclosure", "policy_or_regulatory_optionality", "customer_or_order_quality", "early_revision_signal"], "stage3_evidence_fields": ["confirmed_revision", "multiple_public_sources", "financial_visibility", "durable_customer_confirmation"], "stage4b_evidence_fields": ["valuation_blowoff", "positioning_overheat"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/000/000100/2024.csv", "profile_path": "atlas/symbol_profiles/000/000100.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 69.99, "MFE_90D_pct": 76.99, "MFE_180D_pct": 76.99, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -2.97, "MAE_90D_pct": -2.97, "MAE_180D_pct": -2.97, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-10-15", "peak_price": 166900, "drawdown_after_peak_pct": -39.84, "green_lateness_ratio": 0.44, "four_b_local_peak_proximity": 0.9, "four_b_full_window_peak_proximity": 0.9, "four_b_timing_verdict": "watch_only_no_non_price_full_4B", "four_b_evidence_type": ["valuation_blowoff", "positioning_overheat"], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "structural_success_high_MFE_moderate_post_peak_drawdown", "current_profile_verdict": "current_profile_too_late", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "000100_2024-08-21_94300", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "TRG_R7L10_HUGEL_2024-03-04_FDA_LETYBO", "case_id": "R7L10_C23_HUGEL_LETYBO_FDA_APPROVAL", "symbol": "145020", "company_name": "휴젤", "round": "R7", "loop": "10", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION", "fine_archetype_id": "BIO_APPROVAL_TO_COMMERCIALIZATION_ROYALTY_BRIDGE", "sector": "바이오·헬스케어·의료기기", "primary_archetype": "approval_to_commercialization_royalty_bridge", "loop_objective": "coverage_gap_fill|sector_specific_rule_discovery|stage2_actionable_bonus_stress_test|green_strictness_stress_test|4B_non_price_requirement_stress_test|4C_thesis_break_timing_test|counterexample_mining", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-02-29", "entry_date": "2024-03-04", "entry_price": 202500, "evidence_available_at_that_date": "FDA approval of Letybo/letibotulinumtoxinA for glabellar lines; commercial ramp was not immediate but approval unlocked the US path.", "evidence_source": "FDA drug-trial snapshot / cosmetic-medicine reporting; exact original FDA package URL should be attached in implementation.", "stage2_evidence_fields": ["public_event_or_disclosure", "policy_or_regulatory_optionality", "capacity_or_volume_route"], "stage3_evidence_fields": ["multiple_public_sources", "repeat_order_or_conversion", "financial_visibility"], "stage4b_evidence_fields": ["valuation_blowoff", "positioning_overheat"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/145/145020/2024.csv", "profile_path": "atlas/symbol_profiles/145/145020.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 8.15, "MFE_90D_pct": 10.62, "MFE_180D_pct": 60.99, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -14.91, "MAE_90D_pct": -14.91, "MAE_180D_pct": -14.91, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-11-07", "peak_price": 326000, "drawdown_after_peak_pct": -20.25, "green_lateness_ratio": 0.57, "four_b_local_peak_proximity": 0.94, "four_b_full_window_peak_proximity": 0.94, "four_b_timing_verdict": "good_full_window_4B_timing_if_supported_by_valuation_or_revision_slowdown", "four_b_evidence_type": ["valuation_blowoff", "positioning_overheat"], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "delayed_structural_success_high_MAE_success", "current_profile_verdict": "current_profile_correct", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "145020_2024-03-04_202500", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "TRG_R7L10_HLB_2024-04-22_PDUFA_RUNUP", "case_id": "R7L10_C23_HLB_CRL_FAILURE", "symbol": "028300", "company_name": "HLB", "round": "R7", "loop": "10", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION", "fine_archetype_id": "BIO_APPROVAL_TO_COMMERCIALIZATION_ROYALTY_BRIDGE", "sector": "바이오·헬스케어·의료기기", "primary_archetype": "approval_to_commercialization_royalty_bridge", "loop_objective": "coverage_gap_fill|sector_specific_rule_discovery|stage2_actionable_bonus_stress_test|green_strictness_stress_test|4B_non_price_requirement_stress_test|4C_thesis_break_timing_test|counterexample_mining", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-04-22", "entry_date": "2024-04-22", "entry_price": 106300, "evidence_available_at_that_date": "Pre-PDUFA/regulatory expectation around rivoceranib + camrelizumab without approval/commercialization proof.", "evidence_source": "Company/regulatory-event expectation before May 2024 CRL; exact event-source enrichment required.", "stage2_evidence_fields": ["public_event_or_disclosure", "relative_strength", "policy_or_regulatory_optionality"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["valuation_blowoff", "positioning_overheat", "explicit_event_cap"], "stage4c_evidence_fields": ["regulatory_rejection", "thesis_evidence_broken"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/028/028300/2024.csv", "profile_path": "atlas/symbol_profiles/028/028300.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 5.93, "MFE_90D_pct": 5.93, "MFE_180D_pct": 5.93, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -57.53, "MAE_90D_pct": -57.53, "MAE_180D_pct": -57.53, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-04-25", "peak_price": 112600, "drawdown_after_peak_pct": -59.9, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.94, "four_b_full_window_peak_proximity": 0.94, "four_b_timing_verdict": "price_only_or_event_premium_4B_watch", "four_b_evidence_type": ["price_only", "valuation_blowoff", "explicit_event_cap"], "four_c_protection_label": "hard_4c_success_if_triggered_on_CRL", "trigger_outcome_label": "false_positive_green_or_stage2_event_risk", "current_profile_verdict": "current_profile_false_positive", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "028300_2024-04-22_106300", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "TRG_R7L10_HLB_2024-05-17_CRL_4C", "case_id": "R7L10_C23_HLB_CRL_FAILURE", "symbol": "028300", "company_name": "HLB", "round": "R7", "loop": "10", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION", "fine_archetype_id": "BIO_APPROVAL_TO_COMMERCIALIZATION_ROYALTY_BRIDGE", "sector": "바이오·헬스케어·의료기기", "primary_archetype": "approval_to_commercialization_royalty_bridge", "loop_objective": "coverage_gap_fill|sector_specific_rule_discovery|stage2_actionable_bonus_stress_test|green_strictness_stress_test|4B_non_price_requirement_stress_test|4C_thesis_break_timing_test|counterexample_mining", "trigger_type": "4C", "trigger_date": "2024-05-17", "entry_date": "2024-05-17", "entry_price": 67100, "evidence_available_at_that_date": "Complete response letter/regulatory non-approval broke the pre-approval thesis.", "evidence_source": "FDA/HLB CRL reporting; exact original company/FDA source should be attached in implementation.", "stage2_evidence_fields": [], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["explicit_event_cap"], "stage4c_evidence_fields": ["regulatory_rejection", "thesis_evidence_broken"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/028/028300/2024.csv", "profile_path": "atlas/symbol_profiles/028/028300.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 9.99, "MFE_90D_pct": 46.2, "MFE_180D_pct": 46.2, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -32.71, "MAE_90D_pct": -32.71, "MAE_180D_pct": -32.71, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-07-08", "peak_price": 98100, "drawdown_after_peak_pct": -38.84, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "not_applicable", "four_b_evidence_type": [], "four_c_protection_label": "hard_4c_success_with_whipsaw_risk", "trigger_outcome_label": "4C_success_after_thesis_break", "current_profile_verdict": "current_profile_4C_too_late_if_waiting_for_confirmed_financials", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "028300_2024-05-17_67100", "dedupe_for_aggregate": false, "aggregate_group_role": "4C_overlay_only", "is_new_independent_case": false, "reuse_reason": "same_symbol_new_4C_timing_for_failed_rerating_case", "independent_evidence_weight": 0.25, "do_not_count_as_new_case": false}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R7L10_C23_YUHAN_LAZCLUZE_APPROVAL", "trigger_id": "TRG_R7L10_YUHAN_2024-08-21_APPROVAL_COMMERCIALIZATION", "symbol": "000100", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION", "raw_component_scores_before": {"contract_score": 4, "backlog_visibility_score": 1, "margin_bridge_score": 3, "revision_score": 52, "relative_strength_score": 9, "customer_quality_score": 14, "policy_or_regulatory_score": 18, "valuation_repricing_score": 10, "execution_risk_score": -4, "legal_or_contract_risk_score": -2, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 84, "stage_label_before": "Stage3-Yellow", "raw_component_scores_after": {"contract_score": 5, "backlog_visibility_score": 1, "margin_bridge_score": 4, "revision_score": 60, "relative_strength_score": 10, "customer_quality_score": 18, "policy_or_regulatory_score": 22, "valuation_repricing_score": 10, "execution_risk_score": -4, "legal_or_contract_risk_score": -2, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 92, "stage_label_after": "Stage3-Green", "changed_components": ["policy_or_regulatory_score", "customer_quality_score", "revision_score", "legal_or_contract_risk_score"], "component_delta_explanation": "C23 shadow profile separates approval+commercialization bridge from pre-approval regulatory optionality; hard CRL/cancelled approval routes to 4C protection.", "MFE_90D_pct": 76.99, "MAE_90D_pct": -2.97, "score_return_alignment_label": "aligned", "current_profile_verdict": "current_profile_too_late"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R7L10_C23_HUGEL_LETYBO_FDA_APPROVAL", "trigger_id": "TRG_R7L10_HUGEL_2024-03-04_FDA_LETYBO", "symbol": "145020", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION", "raw_component_scores_before": {"contract_score": 2, "backlog_visibility_score": 0, "margin_bridge_score": 3, "revision_score": 45, "relative_strength_score": 5, "customer_quality_score": 10, "policy_or_regulatory_score": 20, "valuation_repricing_score": 8, "execution_risk_score": -6, "legal_or_contract_risk_score": -2, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 73, "stage_label_before": "Stage2-Actionable", "raw_component_scores_after": {"contract_score": 2, "backlog_visibility_score": 0, "margin_bridge_score": 4, "revision_score": 49, "relative_strength_score": 6, "customer_quality_score": 13, "policy_or_regulatory_score": 23, "valuation_repricing_score": 8, "execution_risk_score": -5, "legal_or_contract_risk_score": -2, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 81, "stage_label_after": "Stage3-Yellow", "changed_components": ["policy_or_regulatory_score", "customer_quality_score", "revision_score", "legal_or_contract_risk_score"], "component_delta_explanation": "C23 shadow profile separates approval+commercialization bridge from pre-approval regulatory optionality; hard CRL/cancelled approval routes to 4C protection.", "MFE_90D_pct": 10.62, "MAE_90D_pct": -14.91, "score_return_alignment_label": "aligned", "current_profile_verdict": "current_profile_correct"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R7L10_C23_HLB_CRL_FAILURE", "trigger_id": "TRG_R7L10_HLB_2024-04-22_PDUFA_RUNUP", "symbol": "028300", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 20, "relative_strength_score": 14, "customer_quality_score": 4, "policy_or_regulatory_score": 18, "valuation_repricing_score": 18, "execution_risk_score": -12, "legal_or_contract_risk_score": -6, "dilution_cb_risk_score": -4, "accounting_trust_risk_score": 0}, "weighted_score_before": 70, "stage_label_before": "Stage2-Actionable_or_Yellow_watch", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 10, "relative_strength_score": 8, "customer_quality_score": 1, "policy_or_regulatory_score": 8, "valuation_repricing_score": 14, "execution_risk_score": -18, "legal_or_contract_risk_score": -16, "dilution_cb_risk_score": -4, "accounting_trust_risk_score": 0}, "weighted_score_after": 51, "stage_label_after": "Stage1/4C-watch", "changed_components": ["policy_or_regulatory_score", "customer_quality_score", "revision_score", "legal_or_contract_risk_score"], "component_delta_explanation": "C23 shadow profile separates approval+commercialization bridge from pre-approval regulatory optionality; hard CRL/cancelled approval routes to 4C protection.", "MFE_90D_pct": 5.93, "MAE_90D_pct": -57.53, "score_return_alignment_label": "current_profile_false_positive_fixed_by_guard", "current_profile_verdict": "current_profile_false_positive"}
{"row_type": "aggregate_metric", "round": "R7", "loop": "10", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION", "profile_id": "P0_e2r_2_1_stock_web_calibrated_proxy", "eligible_trigger_count": 3, "avg_MFE_90D_pct": 31.18, "avg_MAE_90D_pct": -25.14, "false_positive_rate": 0.33, "missed_structural_count": 1, "late_green_count": 1, "score_return_alignment_verdict": "mixed_positive_success_but_regulatory_event_false_positive"}
{"row_type": "aggregate_metric", "round": "R7", "loop": "10", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION", "profile_id": "P2_canonical_archetype_candidate_profile", "eligible_trigger_count": 3, "avg_MFE_90D_pct": 31.18, "avg_MAE_90D_pct": -25.14, "false_positive_rate": 0.0, "missed_structural_count": 0, "late_green_count": 0, "score_return_alignment_verdict": "improved_by_approval_bridge_bonus_and_event_risk_cap"}
{"row_type": "residual_contribution", "round": "R7", "loop": "10", "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION", "new_independent_case_count": 3, "reused_case_count": 0, "new_symbol_count": 3, "new_trigger_family_count": 3, "tested_existing_calibrated_axes": ["stage2_actionable_evidence_bonus", "stage3_green_revision_min", "full_4b_requires_non_price_evidence", "hard_4c_thesis_break_routes_to_4c"], "residual_error_types_found": ["current_profile_too_late_for_approval_commercialization_bridge", "current_profile_false_positive_for_pre_approval_event_risk"], "loop_contribution_label": "canonical_archetype_rule_candidate", "do_not_propose_new_weight_delta": false}
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
completed_round = R7
completed_loop = 10
next_round = R8
next_loop = 10
round_schedule_status = valid
round_sector_consistency = pass
```

## 28. Source Notes

- Stock-web manifest max date: 2026-02-20.
- Yuhan 2024 entry row: 2024-08-21 close 94,300; later peak high 166,900 on 2024-10-15.
- Hugel 2024 entry row: 2024-03-04 close 202,500; later peak high 326,000 on 2024-11-07.
- HLB representative row: 2024-04-22 close 106,300; CRL break on 2024-05-17 close 67,100 and 2024-05-21 low 45,150.
- Evidence URLs are acceptable as research source notes but should be normalized to exact source records in the later implementation batch.
