---
schema_family: v12_sector_archetype_residual
selected_round: R10
scheduled_round: R10
selected_loop: 87
scheduled_loop: 87
large_sector_id: L9_CONSTRUCTION_REALESTATE_HOUSING
canonical_archetype_id: C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK
fine_archetype_id: C30_PARENT_SUPPORT_VS_POLICY_SUPPORT_PF_LIQUIDITY_BRIDGE_GUARD
sector: construction_realestate_housing_pf
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
research_session: post_calibrated_sector_archetype_residual_research
output_file: e2r_stock_web_v12_residual_round_R10_loop_87_L9_CONSTRUCTION_REALESTATE_HOUSING_C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK_research.md
price_data_source: Songdaiki/stock-web
price_basis: tradable_raw
price_adjustment_status: raw_unadjusted_marcap
stock_web_manifest_max_date: 2026-02-20
production_scoring_changed: false
shadow_weight_only: true
handoff_prompt_embedded: true
handoff_prompt_executed_now: false
---

# E2R Stock-Web v12 Residual Research — R10 Loop 87 / L9 / C30

## 0. Execution scope

This run follows the MAIN EXECUTION PROMPT as the execution procedure and uses `V12_Research_No_Repeat_Index.md` only as the no-repeat ledger.

```text
scheduled_round = R10
scheduled_loop = 87
large_sector_id = L9_CONSTRUCTION_REALESTATE_HOUSING
canonical_archetype_id = C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK
fine_archetype_id = C30_PARENT_SUPPORT_VS_POLICY_SUPPORT_PF_LIQUIDITY_BRIDGE_GUARD
round_schedule_status = valid
round_sector_consistency = pass
stock_agent_code_access_allowed = false
stock_agent_code_patch_allowed = false
production_scoring_changed = false
shadow_weight_only = true
```

R10 is hard-mapped to `L9_CONSTRUCTION_REALESTATE_HOUSING`; therefore the research is kept inside C30 PF/balance-sheet stress rather than jumping to C31/C32 or R13 red-team.

## 1. No-repeat and coverage preflight

The No-Repeat Index shows that C30 already has heavy coverage: 81 rows / 31 symbols / good-bad Stage2 16/29 / 4B-4C 3/4, with repeated top covered symbols `002990`, `294870`, `375500`, `004960`, `013580`, and `006360`.

This run therefore avoids those crowded C30 symbols and selects three less-crowded C30 symbols:

```text
034300 신세계건설
005960 동부건설
010780 아이에스동서
```

No hard duplicate was observed in the inspected No-Repeat excerpts for the exact keys below:

```text
C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK + 034300 + Stage2-Actionable-PF-RepairBridge-ParentSupportProxy + 2024-03-27
C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK + 005960 + Stage2-FalsePositive-PF-PolicySupport-NoRepairBridge + 2024-03-27
C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK + 010780 + Stage2-FalsePositive-MixedRealEstate-NoRepairBridge + 2024-03-27
```

## 2. Stock-web price-source validation

Stock-web manifest fields used:

```text
source_name = FinanceData/marcap
price_adjustment_status = raw_unadjusted_marcap
min_date = 1995-05-02
max_date = 2026-02-20
tradable_row_count = 14354401
raw_row_count = 15214118
symbol_count = 5414
calibration_shard_root = atlas/ohlcv_tradable_by_symbol_year
raw_shard_root = atlas/ohlcv_raw_by_symbol_year
```

Profile caveats:

| symbol | company | profile status | corporate-action window status |
|---|---|---|---|
| 034300 | 신세계건설 | inactive_or_delisted_like in stock-web profile; tradable through 2025-01-24 | profile has 2024-02-06 corporate-action candidate, before entry; no overlap with 2024-03-27~D+180 |
| 005960 | 동부건설 | active_like | no 2024 corporate-action candidate |
| 010780 | 아이에스동서 | active_like | no 2024 corporate-action candidate |

Because 034300 has a corporate-action candidate on 2024-02-06 and later inactive-like status, this MD keeps it calibration-usable only for the post-2024-03-27 30D/90D/180D window and blocks 1Y/2Y use.

## 3. Research thesis

C30 is not a simple “construction bounce” archetype. It is a plumbing problem: debt maturity, PF exposure, parent support, refinancing, project visibility, and cash conversion have to line up. If only the macro valve opens—government liquidity support, PF market support, broad sector rally—the water may run for one house and still fail in the next pipe.

This run tests a narrow residual question:

```text
Can C30 Stage2-Actionable be allowed from macro PF/builder support alone,
or should it require verified company-specific balance-sheet repair bridge?
```

Observed answer from this small holdout:

```text
Macro support alone is insufficient.
One symbol produced a strong price path, but two symbols failed with weak MFE and large MAE.
The useful shadow rule is not a global score boost; it is a C30 company-specific repair bridge requirement.
Promotion is blocked because the company-specific repair/support evidence is still source_proxy_only/evidence_url_pending.
```

## 4. Trigger rows — machine readable JSONL

```jsonl
{"row_type": "trigger", "trigger_id": "R10L87-C30-034300-T1", "case_id": "R10L87-C30-034300", "symbol": "034300", "company_name": "신세계건설", "round": "R10", "loop": "87", "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "fine_archetype_id": "C30_PARENT_SUPPORT_VS_POLICY_SUPPORT_PF_LIQUIDITY_BRIDGE_GUARD", "sector": "construction_realestate_pf", "primary_archetype": "parent_support_repair_bridge_after_pf_liquidity_stress", "loop_objective": "coverage_gap_fill | counterexample_mining | 4B_non_price_requirement_stress_test | canonical_archetype_compression", "trigger_type": "Stage2-Actionable-PF-RepairBridge-ParentSupportProxy", "trigger_date": "2024-03-27", "evidence_available_at_that_date": "Korea announced liquidity support for builders under PF/high-rate stress; 신세계건설 already had visible balance-sheet repair/parent-support narrative in 1Q24, but company-specific DART/IR URL remains pending.", "evidence_source": "Reuters 2024-03-27 builder liquidity support macro article + stock_web_price_path; company_specific_parent_support_evidence_url_pending", "stage2_evidence_fields": "macro_builder_liquidity_support; parent_support_proxy; capital_structure_repair_proxy; tradable_price_path_confirmed", "stage3_evidence_fields": "later_price_confirmation_only; not_used_as_new_green_gate", "stage4b_evidence_fields": "May-2024 price spike; non_price_4B_evidence_missing", "stage4c_evidence_fields": "not_applicable", "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/034/034300/2024.csv", "profile_path": "atlas/symbol_profiles/034/034300.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-03-27", "entry_price": 10630.0, "MFE_30D_pct": 8.75, "MFE_90D_pct": 75.45, "MFE_180D_pct": 75.45, "MFE_1Y_pct": "contaminated_or_unavailable_not_computed", "MFE_2Y_pct": "not_computed", "MAE_30D_pct": -7.34, "MAE_90D_pct": -7.34, "MAE_180D_pct": -7.34, "MAE_1Y_pct": "contaminated_or_unavailable_not_computed", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-05-30", "peak_price": 18650.0, "drawdown_after_peak_pct": -40.21, "green_lateness_ratio": "not_applicable_no_confirmed_Stage3_Green_trigger", "four_b_local_peak_proximity": "not_applicable_representative_stage2_row", "four_b_full_window_peak_proximity": "not_applicable_representative_stage2_row", "four_b_timing_verdict": "local_price_spike_requires_non_price_4B_overlay", "four_b_evidence_type": "price_only", "four_c_protection_label": "not_applicable", "trigger_outcome_label": "positive_structural_success_but_data_quality_blocked", "current_profile_verdict": "current_profile_would_allow_watch_stage2; positive_path_observed_but_no_new_delta_due_source_proxy", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": "", "corporate_action_window_status": "profile_has_2024-02-06_candidate_before_entry; no_overlap_entry_to_D180", "same_entry_group_id": "034300_2024-03-27_10630", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": "", "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "evidence_url_pending": true, "source_proxy_only": true}
{"row_type": "trigger", "trigger_id": "R10L87-C30-034300-T2", "case_id": "R10L87-C30-034300", "symbol": "034300", "company_name": "신세계건설", "round": "R10", "loop": "87", "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "fine_archetype_id": "C30_PARENT_SUPPORT_VS_POLICY_SUPPORT_PF_LIQUIDITY_BRIDGE_GUARD", "sector": "construction_realestate_pf", "primary_archetype": "price_only_local_4B_after_parent_support_rally", "loop_objective": "4B_non_price_requirement_stress_test", "trigger_type": "Stage4B-PriceOnly-LocalPeakWatch", "trigger_date": "2024-05-29", "evidence_available_at_that_date": "Sharp local price acceleration after repair/support narrative; no verified non-price thesis-break or dilution/overhang evidence in this run.", "evidence_source": "stock_web_price_path_only; non_price_4B_url_pending", "stage2_evidence_fields": "same_case_as_R10L87-C30-034300-T1", "stage3_evidence_fields": "not_applicable", "stage4b_evidence_fields": "price_only_spike; local_peak_nearby; non_price_overlay_missing", "stage4c_evidence_fields": "not_applicable", "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/034/034300/2024.csv", "profile_path": "atlas/symbol_profiles/034/034300.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-05-29", "entry_price": 14700.0, "MFE_30D_pct": 26.87, "MFE_90D_pct": 26.87, "MFE_180D_pct": 26.87, "MFE_1Y_pct": "contaminated_or_unavailable_not_computed", "MFE_2Y_pct": "not_computed", "MAE_30D_pct": -24.08, "MAE_90D_pct": -24.15, "MAE_180D_pct": -24.15, "MAE_1Y_pct": "contaminated_or_unavailable_not_computed", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-05-30", "peak_price": 18650.0, "drawdown_after_peak_pct": -40.21, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.51, "four_b_full_window_peak_proximity": 0.51, "four_b_timing_verdict": "price_only_local_4B_requires_non_price_confirmation", "four_b_evidence_type": "price_only", "four_c_protection_label": "not_applicable", "trigger_outcome_label": "4B_watch_only_not_full_4B", "current_profile_verdict": "existing full_4b_requires_non_price_evidence kept", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": "", "corporate_action_window_status": "profile_has_2024-02-06_candidate_before_entry; no_overlap_entry_to_D180", "same_entry_group_id": "034300_2024-05-29_14700", "dedupe_for_aggregate": false, "aggregate_group_role": "4B_overlay_only", "is_new_independent_case": false, "reuse_reason": "same symbol as representative but new 4B timing overlay", "independent_evidence_weight": 0.25, "do_not_count_as_new_case": true, "evidence_url_pending": true, "source_proxy_only": true}
{"row_type": "trigger", "trigger_id": "R10L87-C30-005960-T1", "case_id": "R10L87-C30-005960", "symbol": "005960", "company_name": "동부건설", "round": "R10", "loop": "87", "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "fine_archetype_id": "C30_PARENT_SUPPORT_VS_POLICY_SUPPORT_PF_LIQUIDITY_BRIDGE_GUARD", "sector": "construction_realestate_pf", "primary_archetype": "macro_policy_support_without_company_specific_repair_bridge", "loop_objective": "counterexample_mining | stage2_actionable_bonus_stress_test", "trigger_type": "Stage2-FalsePositive-PF-PolicySupport-NoRepairBridge", "trigger_date": "2024-03-27", "evidence_available_at_that_date": "Korea announced liquidity support for builders, but this run did not verify company-specific PF exposure reduction, liquidity backstop, asset sale, parent support, or margin/cashflow repair bridge for 동부건설.", "evidence_source": "Reuters 2024-03-27 builder liquidity support macro article + stock_web_price_path; company_specific_repair_evidence_url_pending", "stage2_evidence_fields": "macro_support_only; no_company_specific_repair_bridge_verified", "stage3_evidence_fields": "not_supported", "stage4b_evidence_fields": "not_applicable", "stage4c_evidence_fields": "weak_path_high_MAE_180D; thesis_break_watch_only", "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/005/005960/2024.csv", "profile_path": "atlas/symbol_profiles/005/005960.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-03-27", "entry_price": 5030.0, "MFE_30D_pct": 3.98, "MFE_90D_pct": 3.98, "MFE_180D_pct": 3.98, "MFE_1Y_pct": "not_computed", "MFE_2Y_pct": "not_computed", "MAE_30D_pct": -4.47, "MAE_90D_pct": -13.22, "MAE_180D_pct": -29.03, "MAE_1Y_pct": "not_computed", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-04-26", "peak_price": 5230.0, "drawdown_after_peak_pct": -31.74, "green_lateness_ratio": "not_applicable_no_confirmed_Stage3_Green_trigger", "four_b_local_peak_proximity": "not_applicable", "four_b_full_window_peak_proximity": "not_applicable", "four_b_timing_verdict": "not_applicable", "four_b_evidence_type": "not_applicable", "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "counterexample_failed_rerating", "current_profile_verdict": "residual_false_positive_if_macro_support_overweighted_without_company_repair_bridge", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": "", "corporate_action_window_status": "no_2024_corporate_action_candidate_in_profile", "same_entry_group_id": "005960_2024-03-27_5030", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": "", "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "evidence_url_pending": true, "source_proxy_only": true}
{"row_type": "trigger", "trigger_id": "R10L87-C30-010780-T1", "case_id": "R10L87-C30-010780", "symbol": "010780", "company_name": "아이에스동서", "round": "R10", "loop": "87", "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "fine_archetype_id": "C30_PARENT_SUPPORT_VS_POLICY_SUPPORT_PF_LIQUIDITY_BRIDGE_GUARD", "sector": "construction_realestate_pf", "primary_archetype": "non_builder_mixed_realestate_balance_sheet_no_repair_confirmation", "loop_objective": "counterexample_mining | stage2_actionable_bonus_stress_test", "trigger_type": "Stage2-FalsePositive-MixedRealEstate-NoRepairBridge", "trigger_date": "2024-03-27", "evidence_available_at_that_date": "Same macro builder/PF support tape; no verified company-specific balance-sheet repair bridge, PF risk roll-off, or cash conversion proof in this run.", "evidence_source": "Reuters 2024-03-27 builder liquidity support macro article + stock_web_price_path; company_specific_repair_evidence_url_pending", "stage2_evidence_fields": "macro_support_only; mixed_realestate_balance_sheet_watch", "stage3_evidence_fields": "not_supported", "stage4b_evidence_fields": "not_applicable", "stage4c_evidence_fields": "high_MAE_90D_and_180D; hard_4C_not_confirmed_without_company_specific_thesis_break", "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/010/010780/2024.csv", "profile_path": "atlas/symbol_profiles/010/010780.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-03-27", "entry_price": 29250.0, "MFE_30D_pct": 4.1, "MFE_90D_pct": 4.1, "MFE_180D_pct": 4.1, "MFE_1Y_pct": "not_computed", "MFE_2Y_pct": "not_computed", "MAE_30D_pct": -16.41, "MAE_90D_pct": -30.43, "MAE_180D_pct": -40.24, "MAE_1Y_pct": "not_computed", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-03-29", "peak_price": 30450.0, "drawdown_after_peak_pct": -42.59, "green_lateness_ratio": "not_applicable_no_confirmed_Stage3_Green_trigger", "four_b_local_peak_proximity": "not_applicable", "four_b_full_window_peak_proximity": "not_applicable", "four_b_timing_verdict": "not_applicable", "four_b_evidence_type": "not_applicable", "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "counterexample_failed_rerating_high_MAE", "current_profile_verdict": "residual_false_positive_if_macro_support_or_low_PBR_overlay_is_allowed_without_company_repair_bridge", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": "", "corporate_action_window_status": "no_2024_corporate_action_candidate_in_profile", "same_entry_group_id": "010780_2024-03-27_29250", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": "", "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "evidence_url_pending": true, "source_proxy_only": true}
```

## 5. Price-path summary

Representative Stage2 rows only:

| case_id | symbol | trigger_type | entry_date | entry_price | MFE30 | MAE30 | MFE90 | MAE90 | MFE180 | MAE180 | verdict |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| R10L87-C30-034300 | 034300 | Stage2-Actionable-PF-RepairBridge-ParentSupportProxy | 2024-03-27 | 10630 | +8.75% | -7.34% | +75.45% | -7.34% | +75.45% | -7.34% | positive but data-quality blocked |
| R10L87-C30-005960 | 005960 | Stage2-FalsePositive-PF-PolicySupport-NoRepairBridge | 2024-03-27 | 5030 | +3.98% | -4.47% | +3.98% | -13.22% | +3.98% | -29.03% | counterexample |
| R10L87-C30-010780 | 010780 | Stage2-FalsePositive-MixedRealEstate-NoRepairBridge | 2024-03-27 | 29250 | +4.10% | -16.41% | +4.10% | -30.43% | +4.10% | -40.24% | counterexample / high MAE |

The three names share the same macro trigger date, but the price response splits sharply. That split is the residual: **policy support is a necessary weather change, not a company-specific roof repair.**

## 6. 4B local vs full-window audit

The 034300 price path included a strong May 2024 spike:

```text
Stage2 entry = 2024-03-27 / 10630
price-only 4B watch = 2024-05-29 / 14700
observed peak = 2024-05-30 / 18650
post-peak low in observed 180D window = 11150
drawdown_after_peak_pct = -40.21%
four_b_local_peak_proximity = 0.51
four_b_full_window_peak_proximity = 0.51
```

This is not a full 4B confirmation. It is a useful **local 4B watch**. The price surge was real, but without non-price evidence such as refinancing exhaustion, overhang, dilution, legal block, or margin/backlog slowdown, the existing E2R rule `full_4b_requires_non_price_evidence` should be kept.

## 7. Score component breakdown

### 7.1 Raw trigger-level proxy components

| case_id | contract | backlog visibility | margin bridge | revision | relative strength | policy/regulatory | valuation repricing | execution risk | legal/contract risk | accounting trust risk | proxy total | stage proxy |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| R10L87-C30-034300 | 0 | 1 | 2 | 1 | 3 | 3 | 2 | -1 | -1 | -1 | 66 | Stage2-Actionable shadow |
| R10L87-C30-005960 | 0 | 0 | 0 | 0 | 0 | 3 | 1 | -2 | -1 | -1 | 58 | Stage1/Watch under guard |
| R10L87-C30-010780 | 0 | 0 | 0 | 0 | 0 | 3 | 1 | -3 | -1 | -1 | 55 | Stage1/Watch under guard |

Component interpretation:

```text
policy_or_regulatory_score is shared across the three names because macro PF/builder support was observable.
margin_bridge_score differs because only the first case has a repair-bridge proxy in this run.
execution_risk and accounting_trust_risk stay negative because company-specific URL evidence remains pending.
```

### 7.2 Score simulation rows — machine readable JSONL

```jsonl
{"row_type": "score_simulation", "profile_id": "P0_e2r_2_1_stock_web_calibrated_proxy", "profile_scope": "canonical_archetype:C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "profile_hypothesis": "current calibrated profile with generic Stage2 actionable evidence and global price-only 4B guard kept", "changed_axes": "none", "changed_thresholds": "none", "eligible_trigger_count": 3, "selected_entry_trigger_per_case": ["R10L87-C30-034300-T1", "R10L87-C30-005960-T1", "R10L87-C30-010780-T1"], "avg_MFE_90D_pct": 27.84, "avg_MAE_90D_pct": -16.99, "avg_MFE_180D_pct": 27.84, "avg_MAE_180D_pct": -25.54, "false_positive_rate": 0.67, "missed_structural_count": 0, "late_green_count": 0, "avg_green_lateness_ratio": "not_applicable", "avg_four_b_local_peak_proximity": 0.51, "avg_four_b_full_window_peak_proximity": 0.51, "score_return_alignment_verdict": "weak_alignment_when_macro_support_is_used_without_company_specific_repair_bridge", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 1, "margin_bridge_score": 1, "revision_score": 0, "relative_strength_score": 2, "customer_quality_score": 0, "policy_or_regulatory_score": 3, "valuation_repricing_score": 2, "execution_risk_score": -2, "legal_or_contract_risk_score": -1, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": -1}, "weighted_score_before": 62, "stage_label_before": "Stage2-Watch/Actionable mixed", "raw_component_scores_after": "same_as_before", "weighted_score_after": 62, "stage_label_after": "unchanged_shadow_only", "component_delta_explanation": "No production delta proposed; source proxy blocks promotion."}
{"row_type": "score_simulation", "profile_id": "P3_counterexample_guard_profile", "profile_scope": "canonical_archetype:C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "profile_hypothesis": "require verified company-specific repair bridge before Stage2-Actionable in PF/balance-sheet stress; macro liquidity policy alone is Watch-only", "changed_axes": "stage2_required_bridge stress-test only", "changed_thresholds": "no_global_threshold_change", "eligible_trigger_count": 1, "selected_entry_trigger_per_case": ["R10L87-C30-034300-T1"], "avg_MFE_90D_pct": 75.45, "avg_MAE_90D_pct": -7.34, "avg_MFE_180D_pct": 75.45, "avg_MAE_180D_pct": -7.34, "false_positive_rate": 0.0, "missed_structural_count": 0, "late_green_count": 0, "avg_green_lateness_ratio": "not_applicable", "avg_four_b_local_peak_proximity": 0.51, "avg_four_b_full_window_peak_proximity": 0.51, "score_return_alignment_verdict": "improves_alignment_but_not_promotable_until_company_specific_urls_verified", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 1, "margin_bridge_score": 2, "revision_score": 1, "relative_strength_score": 3, "customer_quality_score": 0, "policy_or_regulatory_score": 3, "valuation_repricing_score": 2, "execution_risk_score": -1, "legal_or_contract_risk_score": -1, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": -1}, "weighted_score_before": 66, "stage_label_before": "Stage2-Actionable", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 1, "margin_bridge_score": 2, "revision_score": 1, "relative_strength_score": 3, "customer_quality_score": 0, "policy_or_regulatory_score": 3, "valuation_repricing_score": 2, "execution_risk_score": -1, "legal_or_contract_risk_score": -1, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": -1}, "weighted_score_after": 66, "stage_label_after": "Stage2-Actionable-shadow-only", "component_delta_explanation": "Guard filters 005960/010780, not by raising 034300; it prevents macro-only PF support from becoming actionable."}
```

## 8. Aggregate metric row — machine readable JSONL

```jsonl
{"row_type": "aggregate_metric", "round": "R10", "loop": "87", "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "fine_archetype_id": "C30_PARENT_SUPPORT_VS_POLICY_SUPPORT_PF_LIQUIDITY_BRIDGE_GUARD", "calibration_usable_representative_case_count": 3, "positive_case_count": 1, "counterexample_count": 2, "four_b_overlay_count": 1, "four_c_case_count": 0, "new_symbol_count": 3, "new_trigger_family_count": 3, "avg_MFE_90D_pct": 27.84, "avg_MAE_90D_pct": -16.99, "avg_MFE_180D_pct": 27.84, "avg_MAE_180D_pct": -25.54, "false_positive_rate": 0.67, "source_proxy_only_count": 4, "evidence_url_pending_count": 4, "score_return_alignment_verdict": "macro_support_without_company_specific_repair_bridge_produces_two_failed_reratings", "promotion_decision": "blocked_by_data_quality", "missing_to_promote": "verify company-specific PF exposure, liquidity backstop, parent support, refinancing, asset sale, margin/cash conversion evidence URLs"}
```

## 9. Shadow rule row — machine readable JSONL

```jsonl
{"row_type": "shadow_weight", "round": "R10", "loop": "87", "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "fine_archetype_id": "C30_PARENT_SUPPORT_VS_POLICY_SUPPORT_PF_LIQUIDITY_BRIDGE_GUARD", "rule_scope": "canonical_archetype_specific", "candidate_axis": "stage2_required_bridge", "candidate_delta": "no_delta_proposed", "rule_text": "For C30, macro builder/PF liquidity policy support alone should remain Watch-only. Stage2-Actionable requires company-specific balance-sheet repair bridge: parent support, refinancing, asset sale, PF exposure roll-off, cashflow bridge, or verified margin recovery.", "supporting_positive_case_ids": ["R10L87-C30-034300"], "supporting_counterexample_case_ids": ["R10L87-C30-005960", "R10L87-C30-010780"], "counterexample_guard_ids": ["R10L87-C30-005960", "R10L87-C30-010780"], "data_quality_status": "blocked_by_data_quality_due_to_source_proxy_only", "production_scoring_changed": false, "handoff_prompt_executed_now": false}
```

## 10. Coverage matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | representative cases | positives | counterexamples | 4B overlays | 4C cases | source_proxy_only | evidence_url_pending |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|
| L9_CONSTRUCTION_REALESTATE_HOUSING | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | C30_PARENT_SUPPORT_VS_POLICY_SUPPORT_PF_LIQUIDITY_BRIDGE_GUARD | 3 | 1 | 2 | 1 | 0 | 4 | 4 |

## 11. Existing calibrated axis status

```text
existing_axis_tested:
  - stage2_actionable_evidence_bonus
  - price_only_blowoff_blocks_positive_stage
  - full_4b_requires_non_price_evidence

existing_axis_kept:
  - full_4b_requires_non_price_evidence
  - price_only_blowoff_blocks_positive_stage

existing_axis_strengthened:
  - none, because source_proxy_only/evidence_url_pending blocks promotion

existing_axis_weakened:
  - none

new_axis_proposed:
  - none
```

Stress-test result:

```text
C30 macro support alone creates false positives.
The likely right axis is not "more Stage2 bonus"; it is "Stage2 required bridge" inside C30.
But this MD does not propose a new production delta because all company-specific evidence remains URL-pending/source-proxy.
```

## 12. Residual Contribution Summary

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
  - price_only_blowoff_blocks_positive_stage
  - full_4b_requires_non_price_evidence
residual_error_types_found:
  - macro_policy_support_false_positive_without_company_specific_repair_bridge
  - high_MAE_C30_stage2_watch
  - price_only_local_4B_requires_non_price_confirmation
new_axis_proposed: null
existing_axis_strengthened: null
existing_axis_weakened: null
existing_axis_kept:
  - full_4b_requires_non_price_evidence
  - price_only_blowoff_blocks_positive_stage
sector_specific_rule_candidate: false
canonical_archetype_rule_candidate: false
no_new_signal_reason: company-specific repair/support evidence remains source_proxy_only/evidence_url_pending; use as counterexample/data-quality backlog, not promotion patch

loop_contribution_label: counterexample_added
do_not_propose_new_weight_delta: true
```

## 13. Deferred Coding Agent Handoff Prompt

Do not execute this prompt in the research session.

```text
You are a coding agent for Songdaiki/stock_agent.

Read this MD as one v12 research artifact only. Do not alter production scoring unless the standard v12 calibration pipeline promotes a safe patch.

Tasks:
1. Ingest the trigger JSONL rows.
2. Preserve representative rows:
   - R10L87-C30-034300-T1
   - R10L87-C30-005960-T1
   - R10L87-C30-010780-T1
3. Preserve R10L87-C30-034300-T2 only as 4B_overlay_only / do_not_count_as_new_case=true.
4. Mark this artifact as blocked_by_data_quality for promotion because all company-specific repair/support evidence is source_proxy_only/evidence_url_pending.
5. If later evidence URLs are verified, retest a C30-specific stage2_required_bridge candidate:
   "macro PF/builder liquidity policy alone is Watch-only; Stage2-Actionable requires verified company-specific balance-sheet repair bridge."
6. Do not weaken global Stage3-Green thresholds.
7. Do not treat 034300 May 2024 price spike as full 4B unless non-price 4B evidence is verified.
```


## External / data references used

- MAIN EXECUTION PROMPT: `docs/core/e2r_v12_prompt_round_scheduler_corrected.txt`
- NO-REPEAT INDEX: `docs/core/V12_Research_No_Repeat_Index.md`
- Stock-web manifest: `Songdaiki/stock-web/atlas/manifest.json`
- Stock-web profile paths:
  - `atlas/symbol_profiles/034/034300.json`
  - `atlas/symbol_profiles/005/005960.json`
  - `atlas/symbol_profiles/010/010780.json`
- Stock-web tradable shards:
  - `atlas/ohlcv_tradable_by_symbol_year/034/034300/2024.csv`
  - `atlas/ohlcv_tradable_by_symbol_year/005/005960/2024.csv`
  - `atlas/ohlcv_tradable_by_symbol_year/010/010780/2024.csv`
- Macro evidence:
  - Reuters, 2024-03-27, South Korea prepared financial support for small businesses and builders.
  - Reuters, 2024-05-13, FSS tightened real-estate PF scrutiny and restructuring assessment.


## 14. Next round state

```text
completed_round = R10
completed_loop = 87
next_round = R11
next_loop = 87
round_schedule_status = valid
round_sector_consistency = pass
```
