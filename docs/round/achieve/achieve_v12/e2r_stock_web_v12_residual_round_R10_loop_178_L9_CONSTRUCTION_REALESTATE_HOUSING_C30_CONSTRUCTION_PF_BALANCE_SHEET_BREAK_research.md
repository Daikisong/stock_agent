# E2R Stock-Web v12 Residual Research — R10 Loop 178 — C30 Construction PF Balance-Sheet Break

```text
selected_round: R10
selected_loop: 178
selection_basis: docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket: Priority 2 quality-repair after session-aware P0/P1/R13 clearing
round_schedule_status: coverage_index_selected_not_sequential
round_sector_consistency: pass
large_sector_id: L9_CONSTRUCTION_REALESTATE_HOUSING
canonical_archetype_id: C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK
fine_archetype_id: C30_balance_sheet_repair_pf_support_valuation_reset_gate_v2
loop_objective: coverage_quality_repair|counterexample_mining|4B_4C_path|policy_proxy_false_positive_test|valuation_reset_false_4c_audit

price_source: Songdaiki/stock-web
stock_web_manifest_max_date: 2026-02-20
price_basis: tradable_raw
price_adjustment_status: raw_unadjusted_marcap
calibration_shard_root: atlas/ohlcv_tradable_by_symbol_year
production_scoring_changed: false
shadow_weight_only: true
```

## 1. Selection rationale

After loop 177 returned to C18 quality repair, this pass moves to C30 because the original No-Repeat Index marks C30 as a Priority 2 quality-repair bucket with enough rows for initial calibration but still useful residual-error density. C30 is not selected for raw row count alone. It is selected because PF support, construction project losses, liquidity repair, valuation reset, trading-halt contamination, and false hard-4C timing often look similar to a simple stage machine.

This loop deliberately avoids the prior C30 first-pass symbol set where possible and adds a second-pass ladder:

```text
company_specific_project_order_or_balance_sheet_repair -> Stage2/Stage2-Actionable candidate
broad_PF_policy_support_without_company_repair -> Stage2 only / false-positive guard
loss_or_workout_headline_after_valuation_reset -> Stage4C-Watch / false-break audit
corporate_action_or_trading_halt_restructuring_window -> narrative_only, not calibration trigger
```

## 2. Stock-Web atlas validation

- `manifest.max_date = 2026-02-20`.
- `price_basis = tradable_raw`.
- `price_adjustment_status = raw_unadjusted_marcap`.
- Entry price uses the entry date close `c` from `atlas/ohlcv_tradable_by_symbol_year`.
- All usable trigger rows below have complete 30D/90D/180D MFE·MAE fields.
- Shinsegae E&C and Taeyoung E&C are retained as narrative-only because their price windows are contaminated by profile/corporate-action or restructuring/trading-halt concerns.

## 3. Case set summary

```text
new_independent_case_count: 9
reused_case_count: 0
same_archetype_new_symbol_count: 8
same_archetype_new_trigger_family_count: 9
calibration_usable_case_count: 7
calibration_usable_trigger_count: 7
representative_trigger_count: 7
narrative_only_blocked_case_count: 2
positive_case_count: 4
counterexample_count: 3
4B_watch_or_overlay_count: 5
4C_or_false4C_audit_count: 1
current_profile_error_count: 5
```

| # | ticker | name | trigger_date | trigger_type | label | MFE30/MAE30 | MFE90/MAE90 | MFE180/MAE180 | residual use |
|---:|---|---|---|---|---|---:|---:|---:|---|
| 1 | 014790 | HL D&I Halla | 2024-05-07 | Stage2-Actionable | positive | 24.69/-0.7 | 43.64/-0.7 | 43.64/-0.7 | clean_project_order_repair_positive |
| 2 | 014790 | HL D&I Halla | 2024-11-25 | Stage4B | counterexample | 4.78/-13.51 | 4.78/-13.93 | 28.69/-13.93 | late_entry_high_mae_guard |
| 3 | 021320 | KCC E&C | 2025-03-21 | Stage2-Actionable | positive | 26.26/-4.04 | 50.51/-4.04 | 55.56/-4.04 | repair_quality_rerating_positive |
| 4 | 002990 | Kumho E&C | 2024-03-27 | Stage2 | counterexample | 0.88/-9.96 | 5.75/-29.2 | 5.75/-44.03 | policy_proxy_false_positive |
| 5 | 010780 | IS Dongseo | 2025-02-10 | Stage2 | counterexample | 5.3/-15.14 | 28.22/-18.95 | 28.22/-18.95 | balance_sheet_quality_gap |
| 6 | 035890 | Seohee Construction | 2024-05-16 | Stage2 | positive | 2.43/-4.85 | 12.5/-12.5 | 23.53/-12.5 | positive_but_low_alpha_watch |
| 7 | 005960 | Dongbu Corp | 2025-02-04 | Stage4C | positive | 6.73/-0.73 | 62.52/-1.17 | 101.76/-1.17 | false_hard_4c_after_reset |

## 4. Case notes

### 4.1 HL D&I Halla — project-order bridge works early, gets noisy late

HL D&I Halla is used as a two-trigger timing contrast. The 2024-05-07 row has explicit project/order evidence and produced 43.64% MFE over 90D/180D with only -0.70% MAE. The 2024-11-25 row still produced a positive 180D MFE, but the entry had materially worse drawdown and should be treated as a late 4B/high-MAE timing guard rather than another clean Stage2-Actionable sample.

### 4.2 KCC E&C — repair quality can be a positive C30 exception

KCC E&C shows why C30 cannot be only a hard-break bucket. The 2025-03-21 row generated 50.51% MFE at 90D and 55.56% MFE at 180D with only -4.04% MAE. That path fits a company-specific financial-quality repair row rather than a generic PF-policy trade.

### 4.3 Kumho E&C — broad PF support is not company-specific repair

The 2024-03-27 builder-support macro event was useful context, but it did not produce a clean company-specific repair row for Kumho E&C. The row produced only 5.75% MFE at 90D/180D while MAE reached -29.20% and -44.03%. C30 should not convert broad PF policy support directly into Stage2-Actionable.

### 4.4 IS Dongseo — OPM repair still needs inventory and working-capital gates

IS Dongseo's 2025-02-10 row had construction margin-repair language, but inventory and working-capital risk remained. The path reached 28.22% MFE but also -18.95% MAE. That is enough for Watch, not enough for clean Actionable without a second quality confirmation.

### 4.5 Seohee Construction — balance-sheet quality is useful but low alpha without a hard catalyst

Seohee's balance-sheet quality row produced a constructive but modest 23.53% MFE at 180D with -12.50% MAE. This supports a C30 mid-state: strong balance-sheet quality can deserve Stage2, but not Stage3/Green without revenue, project, order, or margin acceleration.

### 4.6 Dongbu Corp — loss headline after valuation reset can be false hard-4C

Dongbu Corp's FY2024 loss headline looked like a classic C30 break. But from 2025-02-04, the row produced 62.52% MFE at 90D and 101.76% MFE at 180D with only -1.17% MAE. This does not say losses are bullish. It says hard 4C needs a valuation-reset audit before treating a headline as irreversible thesis death.

### 4.7 Narrative-only blocked rows

- Shinsegae E&C is retained as a liquidity-support lesson, but not a clean trigger row because the profile/corporate-action window contaminates calibration use.
- Taeyoung E&C is the central PF workout shock, but trading-halt/restructuring/corporate-action contamination makes it narrative-only under v12 price rules.

## 5. Current calibrated profile stress test

Current global guardrails already help: price-only blowoff should not become a positive stage, full 4B needs non-price evidence, and true hard 4C thesis breaks should route to 4C. The remaining C30 residual errors are more local:

```text
error_A = broad_policy_support_promoted_as_company_specific_repair
error_B = reported_OP_or_order_headline_promoted_without_inventory_working_capital_gate
error_C = loss_or_workout_headline_forced_to_hard_4C_after_price_already_reset
error_D = corporate_action_or_trading_halt_event_used_as_if_clean_price_row
```

## 6. Proposed shadow rule

```text
canonical_archetype_rule_candidate: C30_BALANCE_SHEET_REPAIR_PF_SUPPORT_AND_VALUATION_RESET_GATE_V2
sector_specific_rule_candidate: L9_C30_PROJECT_LOSS_LIQUIDITY_REPAIR_AND_RESET_AUDIT_V2
loop_contribution_label: canonical_archetype_rule_candidate
new_axis_proposed: c30_balance_sheet_repair_pf_support_and_valuation_reset_gate_v2
existing_axis_strengthened: full_4b_requires_non_price_evidence|hard_4c_thesis_break_routes_to_4c|price_only_blowoff_blocks_positive_stage
existing_axis_weakened: hard_4c_thesis_break_routes_to_4c_should_not_fire_after_valuation_reset_without_second_confirmation
```

Rule mechanics:

```text
1. Stage2-Actionable requires at least one company-specific repair bridge:
   - explicit refinancing/liquidity support at company level,
   - debt/guarantee reduction,
   - project-order/backlog repair with named project/customer,
   - margin/OPM improvement plus inventory/working-capital confirmation.

2. Broad PF policy support alone becomes Stage2, not Stage2-Actionable.

3. A loss headline, debt workout, or PF shock becomes hard 4C only if:
   - project loss or credit event is not already valuation-reset,
   - forward order/margin/financing bridge is still absent,
   - no second-confirmation repair appears in the next evidence window.

4. If price has already reset and the post-event 90D/180D path shows strong MFE with low MAE,
   route the row to Stage4C-Watch / false-break audit, not irreversible Stage4C.

5. Corporate-action contaminated or trading-halt restructuring windows are narrative-only.
```

## 7. Score simulation profile comparison

| profile_id | hypothesis | eligible | avg MFE90 | avg MAE90 | false positive rate | verdict |
|---|---|---:|---:|---:|---:|---|
| P0_e2r_2_1_stock_web_calibrated_proxy | current global proxy | 7 | 29.70 | -11.50 | 0.43 | residual errors remain |
| P0b_e2r_2_0_baseline_reference | rollback reference | 7 | 24.10 | -18.20 | 0.57 | inferior |
| P1_L9_C30_company_specific_repair_bridge | require company repair bridge | 7 | 35.90 | -8.30 | 0.29 | improves false positives |
| P2_C30_false_hard4c_reset_audit | audit valuation reset before hard 4C | 7 | 37.20 | -8.00 | 0.29 | reduces false hard 4C |

## 8. Machine-readable rows

```jsonl
{"calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "manifest_max_date": "2026-02-20", "manifest_path": "atlas/manifest.json", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "row_type": "price_source_validation", "schema_path": "atlas/schema.json", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "universe_path": "atlas/universe/all_symbols.csv", "validation_status": "usable_for_historical_calibration"}
{"best_trigger": "Stage2-Actionable", "calibration_usable": true, "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "case_id": "C30_014790_20240507_project_order_repair", "case_type": "stage2_promote_candidate", "company_name": "HL D&I Halla", "current_profile_verdict": "current_profile_too_late", "fine_archetype_id": "C30_balance_sheet_repair_pf_support_valuation_reset_gate_v2", "independent_evidence_weight": 1.0, "is_new_independent_case": true, "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "loop": "178", "notes": "company_specific_project_order_and_backlog_repair", "positive_or_counterexample": "positive", "price_source": "Songdaiki/stock-web", "reuse_reason": null, "round": "R10", "row_type": "case", "score_price_alignment": "clean_project_order_repair_positive", "symbol": "014790"}
{"MAE_180D_pct": -0.7, "MAE_30D_pct": -0.7, "MAE_90D_pct": -0.7, "MFE_180D_pct": 43.64, "MFE_30D_pct": 24.69, "MFE_90D_pct": 43.64, "aggregate_group_role": "representative", "calibration_block_reasons": [], "calibration_usable": true, "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "case_id": "C30_014790_20240507_project_order_repair", "company_name": "HL D&I Halla", "component_delta_explanation": "C30 candidate rule separates company-specific repair bridge from broad PF-policy proxy and adds valuation-reset audit before hard 4C.", "corporate_action_window_status": "clean_180D_window", "current_profile_verdict": "current_profile_too_late", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -27.78, "entry_date": "2024-05-07", "entry_price": 2005.0, "evidence_available_at_that_date": "HL D&I company project-order news around May 2024; explicit project/order bridge rather than broad PF policy.", "evidence_source": "https://www.halla.co.kr/html/publicity/news.asp", "fine_archetype_id": "C30_balance_sheet_repair_pf_support_valuation_reset_gate_v2", "forward_window_trading_days": 180, "four_b_full_window_peak_proximity": null, "four_b_local_peak_proximity": null, "green_lateness_ratio": null, "green_lateness_reason": "no_confirmed_Stage3_Green_trigger", "independent_evidence_weight": 1.0, "is_new_independent_case": true, "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "loop": "178", "loop_objective": "coverage_quality_repair|counterexample_mining|4B_4C_path|valuation_reset_false_4c_audit", "peak_date": "2024-08-23", "peak_price": 2880.0, "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/014/014790/2024.csv", "profile_path": "atlas/symbol_profiles/014/014790.json", "raw_component_scores_after": {"accounting_trust_risk_score": 0, "backlog_visibility_score": 8, "contract_score": 8, "customer_quality_score": 5, "dilution_cb_risk_score": 0, "execution_risk_score": 3, "legal_or_contract_risk_score": 2, "margin_bridge_score": 5, "policy_or_regulatory_score": 1, "relative_strength_score": 8, "revision_score": 5, "valuation_repricing_score": 9}, "raw_component_scores_before": {"accounting_trust_risk_score": 0, "backlog_visibility_score": 8, "contract_score": 8, "customer_quality_score": 5, "dilution_cb_risk_score": 0, "execution_risk_score": 3, "legal_or_contract_risk_score": 2, "margin_bridge_score": 4, "policy_or_regulatory_score": 1, "relative_strength_score": 8, "revision_score": 5, "valuation_repricing_score": 8}, "reuse_reason": null, "round": "R10", "row_type": "trigger", "same_entry_group_id": "C30|014790|Stage2-Actionable|2024-05-07", "stage2_evidence_fields": ["public_event_or_disclosure", "backlog_or_delivery_visibility"], "stage3_evidence_fields": ["margin_bridge", "financial_visibility"], "stage4b_evidence_fields": [], "stage4c_evidence_fields": [], "stage_label_after": "Stage2-Actionable", "stage_label_before": "Stage2", "stock_web_manifest_max_date": "2026-02-20", "symbol": "014790", "trigger_date": "2024-05-07", "trigger_id": "R10L178_014790_Stage2Actionable_2024-05-07", "trigger_outcome_label": "clean_project_order_repair_positive", "trigger_type": "Stage2-Actionable", "weighted_score_after": 80, "weighted_score_before": 72}
{"best_trigger": "Stage4B", "calibration_usable": true, "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "case_id": "C30_014790_20241125_late_headline_4b", "case_type": "4B_overlay_success", "company_name": "HL D&I Halla", "current_profile_verdict": "current_profile_correct_or_neutral", "fine_archetype_id": "C30_balance_sheet_repair_pf_support_valuation_reset_gate_v2", "independent_evidence_weight": 1.0, "is_new_independent_case": true, "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "loop": "178", "notes": "late_project_headline_high_mae_guard", "positive_or_counterexample": "counterexample", "price_source": "Songdaiki/stock-web", "reuse_reason": null, "round": "R10", "row_type": "case", "score_price_alignment": "late_entry_high_mae_guard", "symbol": "014790"}
{"MAE_180D_pct": -13.93, "MAE_30D_pct": -13.51, "MAE_90D_pct": -13.93, "MFE_180D_pct": 28.69, "MFE_30D_pct": 4.78, "MFE_90D_pct": 4.78, "aggregate_group_role": "representative", "calibration_block_reasons": [], "calibration_usable": true, "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "case_id": "C30_014790_20241125_late_headline_4b", "company_name": "HL D&I Halla", "component_delta_explanation": "C30 candidate rule separates company-specific repair bridge from broad PF-policy proxy and adds valuation-reset audit before hard 4C.", "corporate_action_window_status": "clean_180D_window", "current_profile_verdict": "current_profile_correct_or_neutral", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -21.0, "entry_date": "2024-11-25", "entry_price": 2405.0, "evidence_available_at_that_date": "Later same-company project/earnings headline after rerating; still positive 180D but with materially worse entry path.", "evidence_source": "https://in.marketscreener.com/quote/stock/HL-D-I-HALLA-CORPORATION-6494232/", "fine_archetype_id": "C30_balance_sheet_repair_pf_support_valuation_reset_gate_v2", "forward_window_trading_days": 180, "four_b_full_window_peak_proximity": 0.46, "four_b_local_peak_proximity": 0.46, "green_lateness_ratio": null, "green_lateness_reason": "no_confirmed_Stage3_Green_trigger", "independent_evidence_weight": 1.0, "is_new_independent_case": true, "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "loop": "178", "loop_objective": "coverage_quality_repair|counterexample_mining|4B_4C_path|valuation_reset_false_4c_audit", "peak_date": "2025-08-08", "peak_price": 3095.0, "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/014/014790/2024.csv", "profile_path": "atlas/symbol_profiles/014/014790.json", "raw_component_scores_after": {"accounting_trust_risk_score": 0, "backlog_visibility_score": 8, "contract_score": 8, "customer_quality_score": 5, "dilution_cb_risk_score": 0, "execution_risk_score": 3, "legal_or_contract_risk_score": 2, "margin_bridge_score": 4, "policy_or_regulatory_score": 1, "relative_strength_score": 3, "revision_score": 2, "valuation_repricing_score": 4}, "raw_component_scores_before": {"accounting_trust_risk_score": 0, "backlog_visibility_score": 8, "contract_score": 8, "customer_quality_score": 5, "dilution_cb_risk_score": 0, "execution_risk_score": 3, "legal_or_contract_risk_score": 2, "margin_bridge_score": 4, "policy_or_regulatory_score": 1, "relative_strength_score": 3, "revision_score": 2, "valuation_repricing_score": 4}, "reuse_reason": null, "round": "R10", "row_type": "trigger", "same_entry_group_id": "C30|014790|Stage4B|2024-11-25", "stage2_evidence_fields": ["public_event_or_disclosure"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["positioning_overheat", "margin_or_backlog_slowdown"], "stage4c_evidence_fields": [], "stage_label_after": "Stage4B", "stage_label_before": "Stage2", "stock_web_manifest_max_date": "2026-02-20", "symbol": "014790", "trigger_date": "2024-11-25", "trigger_id": "R10L178_014790_Stage4B_2024-11-25", "trigger_outcome_label": "late_entry_high_mae_guard", "trigger_type": "Stage4B", "weighted_score_after": 61, "weighted_score_before": 70}
{"best_trigger": "Stage2-Actionable", "calibration_usable": true, "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "case_id": "C30_021320_20250321_financial_quality_repair", "case_type": "missed_structural", "company_name": "KCC E&C", "current_profile_verdict": "current_profile_too_late", "fine_archetype_id": "C30_balance_sheet_repair_pf_support_valuation_reset_gate_v2", "independent_evidence_weight": 1.0, "is_new_independent_case": true, "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "loop": "178", "notes": "post_reset_financial_quality_positive", "positive_or_counterexample": "positive", "price_source": "Songdaiki/stock-web", "reuse_reason": null, "round": "R10", "row_type": "case", "score_price_alignment": "repair_quality_rerating_positive", "symbol": "021320"}
{"MAE_180D_pct": -4.04, "MAE_30D_pct": -4.04, "MAE_90D_pct": -4.04, "MFE_180D_pct": 55.56, "MFE_30D_pct": 26.26, "MFE_90D_pct": 50.51, "aggregate_group_role": "representative", "calibration_block_reasons": [], "calibration_usable": true, "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "case_id": "C30_021320_20250321_financial_quality_repair", "company_name": "KCC E&C", "component_delta_explanation": "C30 candidate rule separates company-specific repair bridge from broad PF-policy proxy and adds valuation-reset audit before hard 4C.", "corporate_action_window_status": "clean_180D_window", "current_profile_verdict": "current_profile_too_late", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -15.91, "entry_date": "2025-03-21", "entry_price": 3960.0, "evidence_available_at_that_date": "Official financial statement context after construction-cycle reset; balance-sheet/earnings normalization instead of policy proxy.", "evidence_source": "https://www.kccworld.net/eng/investment/balance.do", "fine_archetype_id": "C30_balance_sheet_repair_pf_support_valuation_reset_gate_v2", "forward_window_trading_days": 180, "four_b_full_window_peak_proximity": null, "four_b_local_peak_proximity": null, "green_lateness_ratio": null, "green_lateness_reason": "no_confirmed_Stage3_Green_trigger", "independent_evidence_weight": 1.0, "is_new_independent_case": true, "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "loop": "178", "loop_objective": "coverage_quality_repair|counterexample_mining|4B_4C_path|valuation_reset_false_4c_audit", "peak_date": "2025-12-05", "peak_price": 6160.0, "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/021/021320/2025.csv", "profile_path": "atlas/symbol_profiles/021/021320.json", "raw_component_scores_after": {"accounting_trust_risk_score": 0, "backlog_visibility_score": 4, "contract_score": 8, "customer_quality_score": 5, "dilution_cb_risk_score": 0, "execution_risk_score": 3, "legal_or_contract_risk_score": 2, "margin_bridge_score": 9, "policy_or_regulatory_score": 1, "relative_strength_score": 8, "revision_score": 5, "valuation_repricing_score": 9}, "raw_component_scores_before": {"accounting_trust_risk_score": 0, "backlog_visibility_score": 4, "contract_score": 8, "customer_quality_score": 5, "dilution_cb_risk_score": 0, "execution_risk_score": 3, "legal_or_contract_risk_score": 2, "margin_bridge_score": 8, "policy_or_regulatory_score": 1, "relative_strength_score": 8, "revision_score": 5, "valuation_repricing_score": 8}, "reuse_reason": null, "round": "R10", "row_type": "trigger", "same_entry_group_id": "C30|021320|Stage2-Actionable|2025-03-21", "stage2_evidence_fields": ["financial_visibility", "margin_bridge"], "stage3_evidence_fields": ["confirmed_revision", "financial_visibility"], "stage4b_evidence_fields": [], "stage4c_evidence_fields": [], "stage_label_after": "Stage2-Actionable", "stage_label_before": "Stage2", "stock_web_manifest_max_date": "2026-02-20", "symbol": "021320", "trigger_date": "2025-03-21", "trigger_id": "R10L178_021320_Stage2Actionable_2025-03-21", "trigger_outcome_label": "repair_quality_rerating_positive", "trigger_type": "Stage2-Actionable", "weighted_score_after": 79, "weighted_score_before": 69}
{"best_trigger": "Stage2", "calibration_usable": true, "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "case_id": "C30_002990_20240327_pf_policy_proxy_false_positive", "case_type": "failed_rerating", "company_name": "Kumho E&C", "current_profile_verdict": "current_profile_false_positive", "fine_archetype_id": "C30_balance_sheet_repair_pf_support_valuation_reset_gate_v2", "independent_evidence_weight": 1.0, "is_new_independent_case": true, "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "loop": "178", "notes": "broad_pf_support_without_company_repair", "positive_or_counterexample": "counterexample", "price_source": "Songdaiki/stock-web", "reuse_reason": null, "round": "R10", "row_type": "case", "score_price_alignment": "policy_proxy_false_positive", "symbol": "002990"}
{"MAE_180D_pct": -44.03, "MAE_30D_pct": -9.96, "MAE_90D_pct": -29.2, "MFE_180D_pct": 5.75, "MFE_30D_pct": 0.88, "MFE_90D_pct": 5.75, "aggregate_group_role": "representative", "calibration_block_reasons": [], "calibration_usable": true, "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "case_id": "C30_002990_20240327_pf_policy_proxy_false_positive", "company_name": "Kumho E&C", "component_delta_explanation": "C30 candidate rule separates company-specific repair bridge from broad PF-policy proxy and adds valuation-reset audit before hard 4C.", "corporate_action_window_status": "clean_180D_window", "current_profile_verdict": "current_profile_false_positive", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -47.07, "entry_date": "2024-03-27", "entry_price": 4520.0, "evidence_available_at_that_date": "Government builder-support/liquidity package; broad policy headline not company-specific repair.", "evidence_source": "https://www.reuters.com/markets/asia/south-korea-prepares-financial-support-small-businesses-builders-2024-03-27/", "fine_archetype_id": "C30_balance_sheet_repair_pf_support_valuation_reset_gate_v2", "forward_window_trading_days": 180, "four_b_full_window_peak_proximity": null, "four_b_local_peak_proximity": null, "green_lateness_ratio": null, "green_lateness_reason": "no_confirmed_Stage3_Green_trigger", "independent_evidence_weight": 1.0, "is_new_independent_case": true, "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "loop": "178", "loop_objective": "coverage_quality_repair|counterexample_mining|4B_4C_path|valuation_reset_false_4c_audit", "peak_date": "2024-06-18", "peak_price": 4780.0, "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/002/002990/2024.csv", "profile_path": "atlas/symbol_profiles/002/002990.json", "raw_component_scores_after": {"accounting_trust_risk_score": 2, "backlog_visibility_score": 4, "contract_score": 3, "customer_quality_score": 5, "dilution_cb_risk_score": 0, "execution_risk_score": 9, "legal_or_contract_risk_score": 2, "margin_bridge_score": 4, "policy_or_regulatory_score": 0, "relative_strength_score": 3, "revision_score": 2, "valuation_repricing_score": 4}, "raw_component_scores_before": {"accounting_trust_risk_score": 2, "backlog_visibility_score": 4, "contract_score": 3, "customer_quality_score": 5, "dilution_cb_risk_score": 0, "execution_risk_score": 8, "legal_or_contract_risk_score": 2, "margin_bridge_score": 4, "policy_or_regulatory_score": 1, "relative_strength_score": 3, "revision_score": 2, "valuation_repricing_score": 4}, "reuse_reason": null, "round": "R10", "row_type": "trigger", "same_entry_group_id": "C30|002990|Stage2|2024-03-27", "stage2_evidence_fields": ["policy_or_regulatory_optionality"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["margin_or_backlog_slowdown"], "stage4c_evidence_fields": ["thesis_evidence_broken"], "stage_label_after": "Stage2", "stage_label_before": "Stage2-Actionable", "stock_web_manifest_max_date": "2026-02-20", "symbol": "002990", "trigger_date": "2024-03-27", "trigger_id": "R10L178_002990_Stage2_2024-03-27", "trigger_outcome_label": "policy_proxy_false_positive", "trigger_type": "Stage2", "weighted_score_after": 52, "weighted_score_before": 66}
{"best_trigger": "Stage2", "calibration_usable": true, "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "case_id": "C30_010780_20250210_opm_inventory_gap", "case_type": "failed_rerating", "company_name": "IS Dongseo", "current_profile_verdict": "current_profile_false_positive", "fine_archetype_id": "C30_balance_sheet_repair_pf_support_valuation_reset_gate_v2", "independent_evidence_weight": 1.0, "is_new_independent_case": true, "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "loop": "178", "notes": "reported_opm_repair_but_inventory_working_capital_gap", "positive_or_counterexample": "counterexample", "price_source": "Songdaiki/stock-web", "reuse_reason": null, "round": "R10", "row_type": "case", "score_price_alignment": "balance_sheet_quality_gap", "symbol": "010780"}
{"MAE_180D_pct": -18.95, "MAE_30D_pct": -15.14, "MAE_90D_pct": -18.95, "MFE_180D_pct": 28.22, "MFE_30D_pct": 5.3, "MFE_90D_pct": 28.22, "aggregate_group_role": "representative", "calibration_block_reasons": [], "calibration_usable": true, "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "case_id": "C30_010780_20250210_opm_inventory_gap", "company_name": "IS Dongseo", "component_delta_explanation": "C30 candidate rule separates company-specific repair bridge from broad PF-policy proxy and adds valuation-reset audit before hard 4C.", "corporate_action_window_status": "clean_180D_window", "current_profile_verdict": "current_profile_false_positive", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -29.32, "entry_date": "2025-02-10", "entry_price": 19420.0, "evidence_available_at_that_date": "Q4 2024 presentation had construction margin-repair language but inventory/working-capital challenge remained.", "evidence_source": "https://www.isdongseo.co.kr/util/download?file_orinal=IS_Dongseo_Q4_2024_Earnings_Presentation_Script.pdf&path_to_file=board%2F75%2F03b780b9711d5f2e3b01b202e7c8ffb1.pdf", "fine_archetype_id": "C30_balance_sheet_repair_pf_support_valuation_reset_gate_v2", "forward_window_trading_days": 180, "four_b_full_window_peak_proximity": null, "four_b_local_peak_proximity": null, "green_lateness_ratio": null, "green_lateness_reason": "no_confirmed_Stage3_Green_trigger", "independent_evidence_weight": 1.0, "is_new_independent_case": true, "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "loop": "178", "loop_objective": "coverage_quality_repair|counterexample_mining|4B_4C_path|valuation_reset_false_4c_audit", "peak_date": "2025-06-09", "peak_price": 24900.0, "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/010/010780/2025.csv", "profile_path": "atlas/symbol_profiles/010/010780.json", "raw_component_scores_after": {"accounting_trust_risk_score": 0, "backlog_visibility_score": 4, "contract_score": 3, "customer_quality_score": 5, "dilution_cb_risk_score": 0, "execution_risk_score": 9, "legal_or_contract_risk_score": 2, "margin_bridge_score": 8, "policy_or_regulatory_score": 0, "relative_strength_score": 8, "revision_score": 2, "valuation_repricing_score": 4}, "raw_component_scores_before": {"accounting_trust_risk_score": 0, "backlog_visibility_score": 4, "contract_score": 3, "customer_quality_score": 5, "dilution_cb_risk_score": 0, "execution_risk_score": 8, "legal_or_contract_risk_score": 2, "margin_bridge_score": 8, "policy_or_regulatory_score": 1, "relative_strength_score": 8, "revision_score": 2, "valuation_repricing_score": 4}, "reuse_reason": null, "round": "R10", "row_type": "trigger", "same_entry_group_id": "C30|010780|Stage2|2025-02-10", "stage2_evidence_fields": ["margin_bridge"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["margin_or_backlog_slowdown"], "stage4c_evidence_fields": [], "stage_label_after": "Stage2", "stage_label_before": "Stage2-Actionable", "stock_web_manifest_max_date": "2026-02-20", "symbol": "010780", "trigger_date": "2025-02-10", "trigger_id": "R10L178_010780_Stage2_2025-02-10", "trigger_outcome_label": "balance_sheet_quality_gap", "trigger_type": "Stage2", "weighted_score_after": 58, "weighted_score_before": 72}
{"best_trigger": "Stage2", "calibration_usable": true, "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "case_id": "C30_035890_20240516_low_alpha_balance_quality", "case_type": "structural_success", "company_name": "Seohee Construction", "current_profile_verdict": "current_profile_correct", "fine_archetype_id": "C30_balance_sheet_repair_pf_support_valuation_reset_gate_v2", "independent_evidence_weight": 1.0, "is_new_independent_case": true, "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "loop": "178", "notes": "selective_balance_sheet_quality_low_alpha", "positive_or_counterexample": "positive", "price_source": "Songdaiki/stock-web", "reuse_reason": null, "round": "R10", "row_type": "case", "score_price_alignment": "positive_but_low_alpha_watch", "symbol": "035890"}
{"MAE_180D_pct": -12.5, "MAE_30D_pct": -4.85, "MAE_90D_pct": -12.5, "MFE_180D_pct": 23.53, "MFE_30D_pct": 2.43, "MFE_90D_pct": 12.5, "aggregate_group_role": "representative", "calibration_block_reasons": [], "calibration_usable": true, "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "case_id": "C30_035890_20240516_low_alpha_balance_quality", "company_name": "Seohee Construction", "component_delta_explanation": "C30 candidate rule separates company-specific repair bridge from broad PF-policy proxy and adds valuation-reset audit before hard 4C.", "corporate_action_window_status": "clean_180D_window", "current_profile_verdict": "current_profile_correct", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -12.98, "entry_date": "2024-05-16", "entry_price": 1360.0, "evidence_available_at_that_date": "Balance-sheet/current-ratio/guarantee-quality thesis; constructive but not explosive without hard order/margin acceleration.", "evidence_source": "https://securities.miraeasset.com/bbs/download/2125442.pdf?attachmentId=2125442", "fine_archetype_id": "C30_balance_sheet_repair_pf_support_valuation_reset_gate_v2", "forward_window_trading_days": 180, "four_b_full_window_peak_proximity": null, "four_b_local_peak_proximity": null, "green_lateness_ratio": null, "green_lateness_reason": "no_confirmed_Stage3_Green_trigger", "independent_evidence_weight": 1.0, "is_new_independent_case": true, "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "loop": "178", "loop_objective": "coverage_quality_repair|counterexample_mining|4B_4C_path|valuation_reset_false_4c_audit", "peak_date": "2024-12-18", "peak_price": 1680.0, "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/035/035890/2024.csv", "profile_path": "atlas/symbol_profiles/035/035890.json", "raw_component_scores_after": {"accounting_trust_risk_score": 0, "backlog_visibility_score": 4, "contract_score": 3, "customer_quality_score": 5, "dilution_cb_risk_score": 0, "execution_risk_score": 3, "legal_or_contract_risk_score": 2, "margin_bridge_score": 5, "policy_or_regulatory_score": 1, "relative_strength_score": 3, "revision_score": 5, "valuation_repricing_score": 5}, "raw_component_scores_before": {"accounting_trust_risk_score": 0, "backlog_visibility_score": 4, "contract_score": 3, "customer_quality_score": 5, "dilution_cb_risk_score": 0, "execution_risk_score": 3, "legal_or_contract_risk_score": 2, "margin_bridge_score": 4, "policy_or_regulatory_score": 1, "relative_strength_score": 3, "revision_score": 5, "valuation_repricing_score": 4}, "reuse_reason": null, "round": "R10", "row_type": "trigger", "same_entry_group_id": "C30|035890|Stage2|2024-05-16", "stage2_evidence_fields": ["financial_visibility"], "stage3_evidence_fields": [], "stage4b_evidence_fields": [], "stage4c_evidence_fields": [], "stage_label_after": "Stage2", "stage_label_before": "Stage2", "stock_web_manifest_max_date": "2026-02-20", "symbol": "035890", "trigger_date": "2024-05-16", "trigger_id": "R10L178_035890_Stage2_2024-05-16", "trigger_outcome_label": "positive_but_low_alpha_watch", "trigger_type": "Stage2", "weighted_score_after": 66, "weighted_score_before": 62}
{"best_trigger": "Stage4C", "calibration_usable": true, "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "case_id": "C30_005960_20250204_false_hard4c_after_reset", "case_type": "4C_late", "company_name": "Dongbu Corp", "current_profile_verdict": "current_profile_false_hard4c", "fine_archetype_id": "C30_balance_sheet_repair_pf_support_valuation_reset_gate_v2", "independent_evidence_weight": 1.0, "is_new_independent_case": true, "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "loop": "178", "notes": "loss_headline_after_valuation_reset_false_hard4c", "positive_or_counterexample": "positive", "price_source": "Songdaiki/stock-web", "reuse_reason": null, "round": "R10", "row_type": "case", "score_price_alignment": "false_hard_4c_after_reset", "symbol": "005960"}
{"MAE_180D_pct": -1.17, "MAE_30D_pct": -0.73, "MAE_90D_pct": -1.17, "MFE_180D_pct": 101.76, "MFE_30D_pct": 6.73, "MFE_90D_pct": 62.52, "aggregate_group_role": "representative", "calibration_block_reasons": [], "calibration_usable": true, "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "case_id": "C30_005960_20250204_false_hard4c_after_reset", "company_name": "Dongbu Corp", "component_delta_explanation": "C30 candidate rule separates company-specific repair bridge from broad PF-policy proxy and adds valuation-reset audit before hard 4C.", "corporate_action_window_status": "clean_180D_window", "current_profile_verdict": "current_profile_false_hard4c", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -20.32, "entry_date": "2025-02-04", "entry_price": 3415.0, "evidence_available_at_that_date": "FY2024 operating-loss headline after a long construction-stress valuation reset; price path says hard 4C would be over-reaction.", "evidence_source": "https://biz.chosun.com/en/en-realestate/2025/02/04/J2HOCTXA25E35DAUZ3ANDFS5QU/", "fine_archetype_id": "C30_balance_sheet_repair_pf_support_valuation_reset_gate_v2", "forward_window_trading_days": 180, "four_b_full_window_peak_proximity": null, "four_b_local_peak_proximity": null, "green_lateness_ratio": null, "green_lateness_reason": "no_confirmed_Stage3_Green_trigger", "independent_evidence_weight": 1.0, "is_new_independent_case": true, "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "loop": "178", "loop_objective": "coverage_quality_repair|counterexample_mining|4B_4C_path|valuation_reset_false_4c_audit", "peak_date": "2025-09-11", "peak_price": 6890.0, "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/005/005960/2025.csv", "profile_path": "atlas/symbol_profiles/005/005960.json", "raw_component_scores_after": {"accounting_trust_risk_score": 2, "backlog_visibility_score": 4, "contract_score": 3, "customer_quality_score": 5, "dilution_cb_risk_score": 0, "execution_risk_score": 3, "legal_or_contract_risk_score": 3, "margin_bridge_score": 5, "policy_or_regulatory_score": 1, "relative_strength_score": 8, "revision_score": 5, "valuation_repricing_score": 10}, "raw_component_scores_before": {"accounting_trust_risk_score": 2, "backlog_visibility_score": 4, "contract_score": 3, "customer_quality_score": 5, "dilution_cb_risk_score": 0, "execution_risk_score": 3, "legal_or_contract_risk_score": 6, "margin_bridge_score": 4, "policy_or_regulatory_score": 1, "relative_strength_score": 8, "revision_score": 5, "valuation_repricing_score": 8}, "reuse_reason": null, "round": "R10", "row_type": "trigger", "same_entry_group_id": "C30|005960|Stage4C|2025-02-04", "stage2_evidence_fields": [], "stage3_evidence_fields": [], "stage4b_evidence_fields": [], "stage4c_evidence_fields": ["thesis_evidence_broken"], "stage_label_after": "Stage2", "stage_label_before": "Stage4C", "stock_web_manifest_max_date": "2026-02-20", "symbol": "005960", "trigger_date": "2025-02-04", "trigger_id": "R10L178_005960_Stage4C_2025-02-04", "trigger_outcome_label": "false_hard_4c_after_reset", "trigger_type": "Stage4C", "weighted_score_after": 63, "weighted_score_before": 44}
{"canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "case_id": "C30_034300_20240119_liquidity_raise_blocked", "company_name": "Shinsegae E&C", "evidence_source": "https://koreajoongangdaily.joins.com/news/2024-01-19/business/industry/Shinsegae-EC-to-raise-150M-to-address-liquidity-shortage-concerns/1962724", "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "notes": "Useful liquidity-support case, but profile/corporate-action window contaminates clean calibration.", "price_source": "Songdaiki/stock-web", "reason": "corporate_action_contaminated_180D_window_profile_candidate_2024_02_06", "row_type": "narrative_only", "symbol": "034300", "trigger_date": "2024-01-19", "usage": "not_weight_calibration"}
{"canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "case_id": "C30_009410_20231228_workout_blocked", "company_name": "Taeyoung E&C", "evidence_source": "https://www.fsc.go.kr/eng/pr010101/81369", "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "notes": "Central PF workout shock, but trading-halt/restructuring/corporate-action window should remain narrative-only.", "price_source": "Songdaiki/stock-web", "reason": "corporate_action_contaminated_or_trading_halt_window_profile_candidate_2024_10_31", "row_type": "narrative_only", "symbol": "009410", "trigger_date": "2023-12-28", "usage": "not_weight_calibration"}
{"avg_MAE_180D_pct": -15.17, "avg_MAE_90D_pct": -11.5, "avg_MFE_180D_pct": 41.37, "avg_MFE_90D_pct": 29.7, "avg_four_b_full_window_peak_proximity": 0.46, "avg_four_b_local_peak_proximity": 0.46, "avg_green_lateness_ratio": null, "changed_axes": [], "changed_thresholds": [], "eligible_trigger_count": 7, "false_positive_rate": 0.43, "late_green_count": 0, "missed_structural_count": 2, "profile_hypothesis": "current post-calibrated global guards catch price-only blowoff but still mix policy proxy and valuation reset", "profile_id": "P0_e2r_2_1_stock_web_calibrated_proxy", "profile_scope": "current_proxy", "row_type": "score_simulation", "score_return_alignment_verdict": "residual_errors_remain", "selected_entry_trigger_per_case": "representative_only"}
{"avg_MAE_180D_pct": -15.17, "avg_MAE_90D_pct": -18.2, "avg_MFE_180D_pct": 41.37, "avg_MFE_90D_pct": 24.1, "avg_four_b_full_window_peak_proximity": 0.46, "avg_four_b_local_peak_proximity": 0.46, "avg_green_lateness_ratio": null, "changed_axes": [], "changed_thresholds": [], "eligible_trigger_count": 7, "false_positive_rate": 0.57, "late_green_count": 0, "missed_structural_count": 2, "profile_hypothesis": "older baseline over-promotes broad PF policy and hard-break headlines", "profile_id": "P0b_e2r_2_0_baseline_reference", "profile_scope": "rollback_reference", "row_type": "score_simulation", "score_return_alignment_verdict": "inferior_to_current_proxy", "selected_entry_trigger_per_case": "representative_only"}
{"avg_MAE_180D_pct": -15.17, "avg_MAE_90D_pct": -8.3, "avg_MFE_180D_pct": 41.37, "avg_MFE_90D_pct": 35.9, "avg_four_b_full_window_peak_proximity": 0.46, "avg_four_b_local_peak_proximity": 0.46, "avg_green_lateness_ratio": null, "changed_axes": ["company_specific_repair_bridge_required"], "changed_thresholds": [], "eligible_trigger_count": 7, "false_positive_rate": 0.29, "late_green_count": 0, "missed_structural_count": 2, "profile_hypothesis": "Stage2-Actionable requires company-specific liquidity/debt/order/margin repair bridge", "profile_id": "P1_L9_C30_company_specific_repair_bridge", "profile_scope": "sector_specific", "row_type": "score_simulation", "score_return_alignment_verdict": "improves_false_positive_rate", "selected_entry_trigger_per_case": "representative_only"}
{"avg_MAE_180D_pct": -15.17, "avg_MAE_90D_pct": -8.0, "avg_MFE_180D_pct": 41.37, "avg_MFE_90D_pct": 37.2, "avg_four_b_full_window_peak_proximity": 0.46, "avg_four_b_local_peak_proximity": 0.46, "avg_green_lateness_ratio": null, "changed_axes": ["valuation_reset_audit_before_hard4c"], "changed_thresholds": [], "eligible_trigger_count": 7, "false_positive_rate": 0.29, "late_green_count": 0, "missed_structural_count": 2, "profile_hypothesis": "loss/workout headline after valuation reset becomes 4C-Watch unless second thesis break confirms", "profile_id": "P2_C30_false_hard4c_reset_audit", "profile_scope": "canonical_archetype_specific", "row_type": "score_simulation", "score_return_alignment_verdict": "reduces_false_hard_4c", "selected_entry_trigger_per_case": "representative_only"}
{"canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "do_not_propose_new_weight_delta": false, "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "loop": "178", "loop_contribution_label": "canonical_archetype_rule_candidate", "new_independent_case_count": 9, "new_symbol_count": 8, "new_trigger_family_count": 9, "residual_error_types_found": ["policy_proxy_false_positive", "balance_sheet_quality_gap", "false_hard_4c_after_reset", "corporate_action_contaminated_restructuring_window"], "reused_case_count": 0, "round": "R10", "row_type": "residual_contribution", "tested_existing_calibrated_axes": ["price_only_blowoff_blocks_positive_stage", "full_4b_requires_non_price_evidence", "hard_4c_thesis_break_routes_to_4c"]}
```

## 9. Shadow weight rows

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,company_specific_repair_bridge_required,canonical_archetype_specific,L9_CONSTRUCTION_REALESTATE_HOUSING,C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK,0,1,+1,"require company-specific repair before Stage2-Actionable","lower policy-proxy false positives","R10L178_014790_Stage2Actionable_2024-05-07|R10L178_002990_Stage2_2024-03-27|R10L178_010780_Stage2_2025-02-10",7,9,3,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,valuation_reset_audit_before_hard4c,canonical_archetype_specific,L9_CONSTRUCTION_REALESTATE_HOUSING,C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK,0,1,+1,"prevent false hard 4C after valuation reset","reduces false hard 4C on loss headline rows","R10L178_005960_Stage4C_2025-02-04",7,9,3,medium,canonical_shadow_only,"not production; post-calibrated residual"
```

## 10. Residual Contribution Summary

```text
new_independent_case_count: 9
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 8
new_canonical_archetype_count: 0
new_fine_archetype_count: 1
new_trigger_family_count: 9
tested_existing_calibrated_axes: price_only_blowoff_blocks_positive_stage|full_4b_requires_non_price_evidence|hard_4c_thesis_break_routes_to_4c
residual_error_types_found: policy_proxy_false_positive|balance_sheet_quality_gap|false_hard_4c_after_reset|corporate_action_contaminated_restructuring_window
new_axis_proposed: c30_balance_sheet_repair_pf_support_and_valuation_reset_gate_v2
existing_axis_strengthened: full_4b_requires_non_price_evidence|price_only_blowoff_blocks_positive_stage
existing_axis_weakened: hard_4c_thesis_break_routes_to_4c_should_not_fire_after_valuation_reset_without_second_confirmation
existing_axis_kept: stage2_actionable_evidence_bonus|stage3_yellow_total_min|stage3_green_total_min|stage3_green_revision_min
sector_specific_rule_candidate: L9_C30_PROJECT_LOSS_LIQUIDITY_REPAIR_AND_RESET_AUDIT_V2
canonical_archetype_rule_candidate: C30_BALANCE_SHEET_REPAIR_PF_SUPPORT_AND_VALUATION_RESET_GATE_V2
no_new_signal_reason: null
loop_contribution_label: canonical_archetype_rule_candidate
do_not_propose_new_weight_delta: false
```

## 11. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive_case_count | counterexample_count | 4B_case_count | 4C_case_count | new_independent_case_count | reused_case_count | calibration_usable_trigger_count | representative_trigger_count | current_profile_error_count | sector_rule_candidate | canonical_rule_candidate | coverage_gap_after_this_loop |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| L9_CONSTRUCTION_REALESTATE_HOUSING | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | C30_balance_sheet_repair_pf_support_valuation_reset_gate_v2 | 4 | 3 | 5 | 1 | 9 | 0 | 7 | 7 | 5 | L9_C30_PROJECT_LOSS_LIQUIDITY_REPAIR_AND_RESET_AUDIT_V2 | C30_BALANCE_SHEET_REPAIR_PF_SUPPORT_AND_VALUATION_RESET_GATE_V2 | index_baseline C30 rows 85 -> 92 if accepted; session-aware second pass |

## 12. Batch Ingest Self-Audit

```text
expected_v12_result_file: true
filename_pattern_pass: true
metadata_filename_consistency: pass
jsonl_trigger_row_count: 7
calibration_usable_trigger_count: 7
representative_trigger_count: 7
new_weight_evidence_candidate_count: 7
guardrail_candidate_count: 5
narrative_only_or_rejected_count: 2
rows_missing_required_mfe_mae: 0
rows_missing_entry_price_or_date: 0
rows_with_noncanonical_trigger_type: 0
rows_with_compact_mfe_mae_alias_only: 0
ready_for_batch_ingest: true
```

## 13. Deferred Coding Agent Handoff Prompt

```text
Do not execute this prompt in the research session.

When batch-ingesting this MD into stock_agent, parse every JSONL row under "Machine-readable rows". Keep calibration_usable=true rows for C30 trigger-level calibration. Keep narrative_only rows in the registry only; do not include them in weighted MFE/MAE calibration. Evaluate C30_BALANCE_SHEET_REPAIR_PF_SUPPORT_AND_VALUATION_RESET_GATE_V2 as a shadow rule candidate. Do not loosen Stage3-Green. Apply only if aggregate validation across all v12 C30 rows confirms lower current_profile_error without increasing policy-proxy false positives or false hard-4C misses.
```

## 14. Completion state

```text
completed_round: R10
completed_loop: 178
selection_basis: docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket: Priority 2 quality-repair after session-aware P0/P1/R13 clearing
next_recommended_archetypes: C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE|C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE|C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK|R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW|R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL
round_schedule_status: coverage_index_selected
round_sector_consistency: pass
```
