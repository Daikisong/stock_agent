# E2R Stock-Web V12 Residual Research — R11 Loop 87 — C04 Nuclear Policy Project Legal Delay
```json
{
  "document_id": "e2r_stock_web_v12_residual_round_R11_loop_87_L1_C04_CZECH_NUCLEAR_LEGAL_CLEARANCE",
  "schema_family": "v12_sector_archetype_residual",
  "round": "R11",
  "loop": 87,
  "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID",
  "canonical_archetype_id": "C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY",
  "fine_archetype_id": "CZECH_NUCLEAR_PREFERRED_BIDDER_TO_LEGAL_CLEARANCE_CONTRACT_DELAY_BRIDGE",
  "sector": "원전·정책 프로젝트·전력 인프라",
  "primary_archetype": "preferred bidder policy spike vs legal/final contract clarity",
  "loop_objective": "counterexample_mining | 4B_non_price_requirement_stress_test | sector_specific_rule_discovery | canonical_archetype_compression | coverage_gap_fill",
  "price_data_source": "Songdaiki/stock-web",
  "price_data_repo": "https://github.com/Songdaiki/stock-web",
  "price_basis": "tradable_raw",
  "price_adjustment_status": "raw_unadjusted_marcap",
  "stock_web_manifest_max_date": "2026-02-20",
  "production_scoring_changed": false,
  "shadow_weight_only": true,
  "handoff_prompt_embedded": true,
  "handoff_prompt_executed_now": false
}
```

## Executive Summary

This standalone v12 research file follows the MAIN EXECUTION PROMPT for post-calibrated historical trigger-level residual research. It does **not** scan current/live candidates, does **not** patch `stock_agent`, and does **not** change production scoring.

The scheduled state is inherited from the prior local artifact:

```text
previous_completed_round = R10
previous_completed_loop = 87
scheduled_round = R11
scheduled_loop = 87
```

R11 allows `L10_POLICY_EVENT_CROSS_REDTEAM_MISC` or `L1_INDUSTRIALS_INFRA_DEFENSE_GRID` when the event is policy-defense/industrial linkage. This run selects the policy-linked nuclear infrastructure route:

```text
large_sector_id = L1_INDUSTRIALS_INFRA_DEFENSE_GRID
canonical_archetype_id = C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY
fine_archetype_id = CZECH_NUCLEAR_PREFERRED_BIDDER_TO_LEGAL_CLEARANCE_CONTRACT_DELAY_BRIDGE
```

Core residual: the July 2024 Czech preferred-bidder event was a strong policy signal, but preferred-bidder-only entries behaved like unstable theme spikes unless legal/final-contract clarity followed. The April 2025 appeal-clearance/legal-path trigger, especially for `052690`, aligned much better with forward price path. Therefore C04 should distinguish:

```text
preferred bidder only = Watch / theme spike / no Green
legal appeal clearance or final contract path = Stage2-Actionable candidate
final contract + economics + margin/order visibility = possible Yellow/Green, not before
```

## Source / Evidence Timeline

| date | evidence | role in C04 |
|---|---|---|
| 2024-07-17 | Czech government selected KHNP as preferred bidder for two Dukovany reactors; final contract details were still to be completed. | policy event / preferred-bidder-only trigger |
| 2025-04-24 | Czech competition office rejected EDF appeals, clearing a barrier for CEZ/KHNP contract path. | legal-clearance trigger |
| 2025-05-06 | Czech regional court temporarily blocked signing after EDF legal complaint. | 4C/legal-delay stress test |
| 2025-06 onward | price path later recovered strongly in directly exposed nuclear engineering names, especially `052690`. | validates that legal/final-contract milestones matter more than first preferred-bidder spike |

Evidence sources used in this MD:

```text
- Reuters, 2024-07-17, South Korea's winning bid for Czech nuclear power project
- Reuters, 2024-07-17, Czechs pick South Korea's KHNP over French bid in nuclear power tender
- Reuters, 2025-04-24, Czechs clear to sign $18 billion nuclear power deal after EDF appeals rejected
- Reuters/AP, 2025-05-06~07, Czech court temporarily blocks/signing delay after EDF complaint
- Songdaiki/stock-web OHLCV atlas
```

## Stock-Web Manifest Validation

```json
{
  "price_atlas_repo": "https://github.com/Songdaiki/stock-web",
  "manifest": "atlas/manifest.json",
  "source_name": "FinanceData/marcap",
  "price_adjustment_status": "raw_unadjusted_marcap",
  "min_date": "1995-05-02",
  "max_date": "2026-02-20",
  "tradable_row_count": 14354401,
  "raw_row_count": 15214118,
  "symbol_count": 5414,
  "markets": [
    "KONEX",
    "KOSDAQ",
    "KOSDAQ GLOBAL",
    "KOSPI"
  ],
  "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year",
  "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year",
  "price_basis": "tradable_raw",
  "calibration_note": "Raw/unadjusted OHLC. Corporate-action-contaminated windows are blocked by default."
}
```

## Profile Validation

| symbol | company | profile path | first/last date | corporate action window | calibration status |
|---|---|---|---|---|---|
| 052690 | 한전기술 | `atlas/symbol_profiles/052/052690.json` | 2009-12-14~2026-02-20 | none | usable |
| 051600 | 한전KPS | `atlas/symbol_profiles/051/051600.json` | 2007-12-14~2026-02-20 | none | usable |
| 130660 | 한전산업 | `atlas/symbol_profiles/130/130660.json` | 2010-12-16~2026-02-20 | none | usable |

## No-Repeat / Novelty Check

`V12_Research_No_Repeat_Index.md` was used only as a duplicate-prevention ledger.

Hard duplicate key:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

Known C04 coverage in the No-Repeat snapshot:

```text
C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY
rows = 12
symbols = 7
date range = 2022-03-10~2025-01-17
good/bad Stage2 = 5/3
4B/4C = 1/0
top covered symbols = 011700(4), 083650(3), 006910(1), 034020(1), 042370(1), 046120(1)
```

This run uses `052690`, `051600`, and `130660`, which are not in that top covered C04 set. Exact row-level ledger was not re-ingested from the repo in this execution, so novelty confidence is `medium`, but the case set is outside the known C04 high-repeat names and uses two trigger families:

```text
1. preferred-bidder-only / no final contract
2. legal-clearance / appeal rejection / contract path
```

## Case Table

| case_id | symbol | trigger family | entry | outcome | calibration role |
|---|---|---|---|---|---|
| R11L87-C04-052690-CZECH_PREFERRED_BIDDER_SPIKE | 052690 | preferred bidder only | 2024-07-18 @ 95,000 | sharp fade before legal clarity | counterexample |
| R11L87-C04-051600-CZECH_MAINTENANCE_AFFILIATED_WATCH | 051600 | indirect affiliate preferred-bidder watch | 2024-07-18 @ 43,500 | modest MFE, meaningful MAE | watch/holdout |
| R11L87-C04-130660-CZECH_POLICY_THEME_SMALL_CAP_FADE | 130660 | policy theme proxy | 2024-07-18 @ 19,500 | severe drawdown, no MFE | counterexample |
| R11L87-C04-052690-CZECH_LEGAL_CLEARANCE_TO_CONTRACT_PATH | 052690 | legal-clearance / appeal rejection | 2025-04-25 @ 67,500 | large MFE with controlled MAE | positive |

## Price Path Summary

| symbol | entry_date | entry_price | peak_date | peak_price | MFE30 | MAE30 | MFE90 | MAE90 | MFE180 | MAE180 | verdict |
|---|---:|---:|---|---:|---:|---:|---:|---:|---:|---:|---|
| 052690 | 2024-07-18 | 95,000 | 2024-07-18 | 98,100 | 3.26 | -35.16 | 3.26 | -35.16 | 3.26 | -47.58 | preferred-bidder counterexample |
| 051600 | 2024-07-18 | 43,500 | 2024-12-03 | 49,100 | 9.08 | -17.59 | 10.92 | -17.59 | 12.87 | -17.59 | watch / not Green |
| 130660 | 2024-07-18 | 19,500 | 2024-07-18 | 19,500 | 0.00 | -39.18 | 0.00 | -43.74 | 0.00 | -55.28 | theme-proxy counterexample |
| 052690 | 2025-04-25 | 67,500 | 2025-06-25 | 121,700 | 16.74 | -11.85 | 80.30 | -11.85 | 80.30 | -11.85 | legal-clearance positive |

Calculation notes:

```text
- Entry uses the next tradable session where evidence timing required next-session entry.
- Preferred-bidder event was announced 2024-07-17; main trigger entries use 2024-07-18 open.
- Legal-clearance event was 2025-04-24; legal-clearance entry uses 2025-04-25 open.
- All prices are raw/unadjusted stock-web tradable rows.
- No selected symbol profile reports corporate-action candidate dates inside entry~D+180.
```

## Machine-Readable Trigger Rows

```jsonl
{"MAE_180D_pct": -47.58, "MAE_1Y_pct": -47.58, "MAE_30D_pct": -35.16, "MAE_90D_pct": -35.16, "MFE_180D_pct": 3.26, "MFE_1Y_pct": 28.11, "MFE_2Y_pct": "unavailable_by_manifest", "MFE_30D_pct": 3.26, "MFE_90D_pct": 3.26, "aggregate_group_role": "representative", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "calibration_block_reasons": "none", "calibration_usable": true, "canonical_archetype_id": "C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY", "case_id": "R11L87-C04-052690-CZECH_PREFERRED_BIDDER_SPIKE", "company_name": "한전기술", "corporate_action_window_status": "clean_no_profile_corporate_action_in_entry_to_D180", "current_profile_verdict": "current_profile_residual_false_positive_if_preferred_bidder_policy_event_is_treated_as_actionable_without_contract_legal_bridge", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -49.24, "entry_date": "2024-07-18", "entry_price": 95000, "evidence_available_at_that_date": "Czech government selected KHNP as preferred bidder for two Dukovany reactors, but contract details/final signing/legal path were not yet finished.", "evidence_source": "Reuters 2024-07-17, South Korea's winning bid for Czech nuclear power project; Reuters 2024-07-17, Czechs pick KHNP over EDF in nuclear tender", "fine_archetype_id": "CZECH_NUCLEAR_PREFERRED_BIDDER_TO_LEGAL_CLEARANCE_CONTRACT_DELAY_BRIDGE", "forward_window_trading_days": "180_available_by_stock_web_manifest", "four_b_evidence_type": "price_only | positioning_overheat", "four_b_full_window_peak_proximity": 0.0, "four_b_local_peak_proximity": 1.0, "four_b_timing_verdict": "price_only_local_4B_too_early", "four_c_protection_label": "not_applicable", "green_lateness_ratio": "not_applicable:no_confirmed_Stage3_Green_trigger", "independent_evidence_weight": 1.0, "is_new_independent_case": true, "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "loop": 87, "loop_objective": "counterexample_mining | 4B_non_price_requirement_stress_test | sector_specific_rule_discovery | canonical_archetype_compression | coverage_gap_fill", "peak_date": "2024-07-18", "peak_price": 98100, "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/052/052690/2024.csv", "primary_archetype": "preferred bidder policy spike vs legal/final contract clarity", "profile_path": "atlas/symbol_profiles/052/052690.json", "reuse_reason": "", "round": "R11", "row_type": "trigger", "same_entry_group_id": "R11L87-C04-052690-20240718-95000", "sector": "원전·정책 프로젝트·전력 인프라", "stage2_evidence_fields": "policy_or_regulatory_score=high; relative_strength_score=high; contract_score=preferred_bidder_only; legal_or_contract_risk_score=material", "stage3_evidence_fields": "missing_final_contract; missing_legal_clearance; missing_margin_or_scope_conversion", "stage4b_evidence_fields": "price_gap_and_volume_blowoff_without_non_price_4B_evidence", "stage4c_evidence_fields": "not hard 4C at entry; later May 2025 court block confirms legal-delay risk existed", "stock_web_manifest_max_date": "2026-02-20", "symbol": "052690", "trigger_date": "2024-07-17", "trigger_id": "R11L87-C04-052690-20240718-PREFERRED_BIDDER_COUNTEREXAMPLE", "trigger_outcome_label": "counterexample_preferred_bidder_gap_faded_before_legal_clarity", "trigger_type": "Stage2-ThemeSpike-PreferredBidder-NoFinalContract"}
{"MAE_180D_pct": -17.59, "MAE_1Y_pct": -17.59, "MAE_30D_pct": -17.59, "MAE_90D_pct": -17.59, "MFE_180D_pct": 12.87, "MFE_1Y_pct": 13.33, "MFE_2Y_pct": "unavailable_by_manifest", "MFE_30D_pct": 9.08, "MFE_90D_pct": 10.92, "aggregate_group_role": "representative", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "calibration_block_reasons": "none", "calibration_usable": true, "canonical_archetype_id": "C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY", "case_id": "R11L87-C04-051600-CZECH_MAINTENANCE_AFFILIATED_WATCH", "company_name": "한전KPS", "corporate_action_window_status": "clean_no_profile_corporate_action_in_entry_to_D180", "current_profile_verdict": "current_profile_kept: Stage2 watch acceptable; Green blocked without contract/legal/margin bridge", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -22.61, "entry_date": "2024-07-18", "entry_price": 43500, "evidence_available_at_that_date": "Czech preferred-bidder event lifted nuclear service/maintenance affiliate, but direct final contract economics and export backlog conversion were still indirect.", "evidence_source": "Reuters 2024-07-17 preferred-bidder event; stock-web 051600 OHLCV", "fine_archetype_id": "CZECH_NUCLEAR_PREFERRED_BIDDER_TO_LEGAL_CLEARANCE_CONTRACT_DELAY_BRIDGE", "forward_window_trading_days": "180_available_by_stock_web_manifest", "four_b_evidence_type": "price_only | positioning_overheat", "four_b_full_window_peak_proximity": 0.7, "four_b_local_peak_proximity": 1.0, "four_b_timing_verdict": "watch_only_local_event_spike_not_full_4B", "four_c_protection_label": "not_applicable", "green_lateness_ratio": "not_applicable:no_confirmed_Stage3_Green_trigger", "independent_evidence_weight": 1.0, "is_new_independent_case": true, "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "loop": 87, "loop_objective": "counterexample_mining | 4B_non_price_requirement_stress_test | sector_specific_rule_discovery | canonical_archetype_compression | coverage_gap_fill", "peak_date": "2024-12-03", "peak_price": 49100, "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/051/051600/2024.csv", "primary_archetype": "preferred bidder policy spike vs legal/final contract clarity", "profile_path": "atlas/symbol_profiles/051/051600.json", "reuse_reason": "", "round": "R11", "row_type": "trigger", "same_entry_group_id": "R11L87-C04-051600-20240718-43500", "sector": "원전·정책 프로젝트·전력 인프라", "stage2_evidence_fields": "policy_or_regulatory_score=medium_high; relative_strength_score=medium; contract_score=indirect_affiliate_not_final_contract", "stage3_evidence_fields": "not Green: direct project scope/margin visibility absent", "stage4b_evidence_fields": "local price spike but not full 4B without non-price deterioration", "stage4c_evidence_fields": "not_applicable", "stock_web_manifest_max_date": "2026-02-20", "symbol": "051600", "trigger_date": "2024-07-17", "trigger_id": "R11L87-C04-051600-20240718-PREFERRED_BIDDER_WATCH", "trigger_outcome_label": "watch_holdout_marginal_positive_but_not_Green", "trigger_type": "Stage2-Watch-PreferredBidder-ServiceAffiliate"}
{"MAE_180D_pct": -55.28, "MAE_1Y_pct": -55.28, "MAE_30D_pct": -39.18, "MAE_90D_pct": -43.74, "MFE_180D_pct": 0.0, "MFE_1Y_pct": 0.0, "MFE_2Y_pct": "unavailable_by_manifest", "MFE_30D_pct": 0.0, "MFE_90D_pct": 0.0, "aggregate_group_role": "representative", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "calibration_block_reasons": "none", "calibration_usable": true, "canonical_archetype_id": "C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY", "case_id": "R11L87-C04-130660-CZECH_POLICY_THEME_SMALL_CAP_FADE", "company_name": "한전산업", "corporate_action_window_status": "clean_no_profile_corporate_action_in_entry_to_D180", "current_profile_verdict": "current_profile_good_if_price_only_block_applies; residual_error_if_policy_theme_is_allowed_as_stage2_actionable", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -55.28, "entry_date": "2024-07-18", "entry_price": 19500, "evidence_available_at_that_date": "Preferred-bidder event produced a small-cap policy-theme proxy spike, but evidence did not identify direct contract scope, final signing, or durable project economics.", "evidence_source": "Reuters 2024-07-17 preferred-bidder event; stock-web 130660 OHLCV", "fine_archetype_id": "CZECH_NUCLEAR_PREFERRED_BIDDER_TO_LEGAL_CLEARANCE_CONTRACT_DELAY_BRIDGE", "forward_window_trading_days": "180_available_by_stock_web_manifest", "four_b_evidence_type": "price_only | positioning_overheat", "four_b_full_window_peak_proximity": 0.0, "four_b_local_peak_proximity": 1.0, "four_b_timing_verdict": "price_only_local_4B_too_early_but_full_4B_requires_non_price", "four_c_protection_label": "not_applicable", "green_lateness_ratio": "not_applicable:no_confirmed_Stage3_Green_trigger", "independent_evidence_weight": 1.0, "is_new_independent_case": true, "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "loop": 87, "loop_objective": "counterexample_mining | 4B_non_price_requirement_stress_test | sector_specific_rule_discovery | canonical_archetype_compression | coverage_gap_fill", "peak_date": "2024-07-18", "peak_price": 19500, "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/130/130660/2024.csv", "primary_archetype": "preferred bidder policy spike vs legal/final contract clarity", "profile_path": "atlas/symbol_profiles/130/130660.json", "reuse_reason": "", "round": "R11", "row_type": "trigger", "same_entry_group_id": "R11L87-C04-130660-20240718-19500", "sector": "원전·정책 프로젝트·전력 인프라", "stage2_evidence_fields": "policy_or_regulatory_score=medium; relative_strength_score=high; contract_score=unsupported_proxy", "stage3_evidence_fields": "blocked: price-only proxy with no final contract/backlog/margin bridge", "stage4b_evidence_fields": "price-only blowoff; local peak at entry", "stage4c_evidence_fields": "thesis_break_watch_only after severe post-event drawdown", "stock_web_manifest_max_date": "2026-02-20", "symbol": "130660", "trigger_date": "2024-07-17", "trigger_id": "R11L87-C04-130660-20240718-PREFERRED_BIDDER_COUNTEREXAMPLE", "trigger_outcome_label": "counterexample_policy_theme_proxy_failed", "trigger_type": "Stage2-FalsePositive-PreferredBidder-ThemeProxy"}
{"MAE_180D_pct": -11.85, "MAE_1Y_pct": "partial_by_manifest", "MAE_30D_pct": -11.85, "MAE_90D_pct": -11.85, "MFE_180D_pct": 80.3, "MFE_1Y_pct": "partial_by_manifest", "MFE_2Y_pct": "unavailable_by_manifest", "MFE_30D_pct": 16.74, "MFE_90D_pct": 80.3, "aggregate_group_role": "representative", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "calibration_block_reasons": "none", "calibration_usable": true, "canonical_archetype_id": "C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY", "case_id": "R11L87-C04-052690-CZECH_LEGAL_CLEARANCE_TO_CONTRACT_PATH", "company_name": "한전기술", "corporate_action_window_status": "clean_no_profile_corporate_action_in_entry_to_D180", "current_profile_verdict": "current_profile_missed_structural_if_C04_requires_final_contract_only; better as Stage2-Actionable not Green", "dedupe_for_aggregate": true, "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -31.72, "entry_date": "2025-04-25", "entry_price": 67500, "evidence_available_at_that_date": "Czech competition office rejected EDF appeals, clearing a barrier for the CEZ/KHNP contract path; the later court/EU pauses show why legal status must be tracked, not ignored.", "evidence_source": "Reuters 2025-04-24 EDF appeals rejected; Reuters/AP May 2025 court delay stress test; stock-web 052690 OHLCV", "fine_archetype_id": "CZECH_NUCLEAR_PREFERRED_BIDDER_TO_LEGAL_CLEARANCE_CONTRACT_DELAY_BRIDGE", "forward_window_trading_days": "180_available_by_stock_web_manifest", "four_b_evidence_type": "legal_or_regulatory_block | contract_delay", "four_b_full_window_peak_proximity": 0.0, "four_b_local_peak_proximity": 0.15, "four_b_timing_verdict": "not_4B_entry; legal_clearance_actionable_before_major_move", "four_c_protection_label": "not_applicable", "green_lateness_ratio": "not_applicable:no_confirmed_Stage3_Green_trigger", "independent_evidence_weight": 0.5, "is_new_independent_case": true, "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "loop": 87, "loop_objective": "counterexample_mining | 4B_non_price_requirement_stress_test | sector_specific_rule_discovery | canonical_archetype_compression | coverage_gap_fill", "peak_date": "2025-06-25", "peak_price": 121700, "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/052/052690/2025.csv", "primary_archetype": "preferred bidder policy spike vs legal/final contract clarity", "profile_path": "atlas/symbol_profiles/052/052690.json", "reuse_reason": "same symbol as 2024 preferred-bidder counterexample, but new trigger_family=legal_clearance and new entry_date; allowed as different Stage transition / legal bridge test", "round": "R11", "row_type": "trigger", "same_entry_group_id": "R11L87-C04-052690-20250425-67500", "sector": "원전·정책 프로젝트·전력 인프라", "stage2_evidence_fields": "policy_or_regulatory_score=high; legal_or_contract_risk_score=improved; contract_score=cleared_barrier_not_final_contract; relative_strength_score=moderate", "stage3_evidence_fields": "watch_to_yellow: final contract still needed, but legal clarity is better than preferred-bidder-only", "stage4b_evidence_fields": "not full 4B at entry; later high requires monitoring for valuation/positioning", "stage4c_evidence_fields": "court/EU delay was a watch, not immediate 4C because final positive path eventually resumed in price", "stock_web_manifest_max_date": "2026-02-20", "symbol": "052690", "trigger_date": "2025-04-24", "trigger_id": "R11L87-C04-052690-20250425-LEGAL_CLEARANCE_POSITIVE", "trigger_outcome_label": "positive_legal_clearance_entry_captured_structural_move", "trigger_type": "Stage2-Actionable-LegalClearance-ContractPath"}
```

## Score Component Breakdown Rows

```jsonl
{"case_id": "R11L87-C04-052690-CZECH_PREFERRED_BIDDER_SPIKE", "company_name": "한전기술", "component_delta_explanation": "legal-clearance/final-contract bridge improves C04 score; preferred-bidder-only loses contract/legal evidence and is blocked from positive stage", "raw_component_scores_after": {"accounting_trust_risk_score": 0, "backlog_visibility_score": 1, "contract_score": 1, "customer_quality_score": "unknown_or_not_supported", "dilution_cb_risk_score": 0, "execution_risk_score": -3, "legal_or_contract_risk_score": -4, "margin_bridge_score": 0, "policy_or_regulatory_score": 4, "relative_strength_score": 1, "revision_score": 0, "valuation_repricing_score": 2}, "raw_component_scores_before": {"accounting_trust_risk_score": 0, "backlog_visibility_score": 1, "contract_score": 1, "customer_quality_score": "unknown_or_not_supported", "dilution_cb_risk_score": 0, "execution_risk_score": -2, "legal_or_contract_risk_score": -3, "margin_bridge_score": 0, "policy_or_regulatory_score": 4, "relative_strength_score": 2, "revision_score": 1, "valuation_repricing_score": 2}, "row_type": "case", "stage_label_after": "WatchOnly / no positive stage", "stage_label_before": "Stage2-Watch/Theme", "symbol": "052690", "weighted_score_after": 52, "weighted_score_before": 61}
{"case_id": "R11L87-C04-051600-CZECH_MAINTENANCE_AFFILIATED_WATCH", "company_name": "한전KPS", "component_delta_explanation": "legal-clearance/final-contract bridge improves C04 score; preferred-bidder-only loses contract/legal evidence and is blocked from positive stage", "raw_component_scores_after": {"accounting_trust_risk_score": 0, "backlog_visibility_score": 1, "contract_score": 1, "customer_quality_score": "unknown_or_not_supported", "dilution_cb_risk_score": 0, "execution_risk_score": -3, "legal_or_contract_risk_score": -4, "margin_bridge_score": 0, "policy_or_regulatory_score": 4, "relative_strength_score": 1, "revision_score": 0, "valuation_repricing_score": 2}, "raw_component_scores_before": {"accounting_trust_risk_score": 0, "backlog_visibility_score": 1, "contract_score": 1, "customer_quality_score": "unknown_or_not_supported", "dilution_cb_risk_score": 0, "execution_risk_score": -2, "legal_or_contract_risk_score": -3, "margin_bridge_score": 0, "policy_or_regulatory_score": 4, "relative_strength_score": 2, "revision_score": 1, "valuation_repricing_score": 2}, "row_type": "case", "stage_label_after": "WatchOnly / no positive stage", "stage_label_before": "Stage2-Watch/Theme", "symbol": "051600", "weighted_score_after": 58, "weighted_score_before": 66}
{"case_id": "R11L87-C04-130660-CZECH_POLICY_THEME_SMALL_CAP_FADE", "company_name": "한전산업", "component_delta_explanation": "legal-clearance/final-contract bridge improves C04 score; preferred-bidder-only loses contract/legal evidence and is blocked from positive stage", "raw_component_scores_after": {"accounting_trust_risk_score": 0, "backlog_visibility_score": 1, "contract_score": 0, "customer_quality_score": "unknown_or_not_supported", "dilution_cb_risk_score": 0, "execution_risk_score": -3, "legal_or_contract_risk_score": -4, "margin_bridge_score": 0, "policy_or_regulatory_score": 4, "relative_strength_score": 1, "revision_score": 0, "valuation_repricing_score": 2}, "raw_component_scores_before": {"accounting_trust_risk_score": 0, "backlog_visibility_score": 1, "contract_score": 0, "customer_quality_score": "unknown_or_not_supported", "dilution_cb_risk_score": 0, "execution_risk_score": -2, "legal_or_contract_risk_score": -3, "margin_bridge_score": 0, "policy_or_regulatory_score": 4, "relative_strength_score": 2, "revision_score": 1, "valuation_repricing_score": 2}, "row_type": "case", "stage_label_after": "WatchOnly / no positive stage", "stage_label_before": "Stage2-Watch/Theme", "symbol": "130660", "weighted_score_after": 52, "weighted_score_before": 61}
{"case_id": "R11L87-C04-052690-CZECH_LEGAL_CLEARANCE_TO_CONTRACT_PATH", "company_name": "한전기술", "component_delta_explanation": "legal-clearance/final-contract bridge improves C04 score; preferred-bidder-only loses contract/legal evidence and is blocked from positive stage", "raw_component_scores_after": {"accounting_trust_risk_score": 0, "backlog_visibility_score": 2, "contract_score": 3, "customer_quality_score": "unknown_or_not_supported", "dilution_cb_risk_score": 0, "execution_risk_score": -1, "legal_or_contract_risk_score": -1, "margin_bridge_score": 1, "policy_or_regulatory_score": 4, "relative_strength_score": 3, "revision_score": 2, "valuation_repricing_score": 2}, "raw_component_scores_before": {"accounting_trust_risk_score": 0, "backlog_visibility_score": 2, "contract_score": 2, "customer_quality_score": "unknown_or_not_supported", "dilution_cb_risk_score": 0, "execution_risk_score": -1, "legal_or_contract_risk_score": -1, "margin_bridge_score": 1, "policy_or_regulatory_score": 4, "relative_strength_score": 3, "revision_score": 2, "valuation_repricing_score": 2}, "row_type": "case", "stage_label_after": "Stage2-Actionable/Yellow-watch", "stage_label_before": "Stage2-Actionable", "symbol": "052690", "weighted_score_after": 78, "weighted_score_before": 76}
```

## Score Simulation Rows

```jsonl
{"avg_MAE_180D_pct": -33.08, "avg_MAE_90D_pct": -27.09, "avg_MFE_180D_pct": 24.11, "avg_MFE_90D_pct": 23.62, "avg_four_b_full_window_peak_proximity": 0.18, "avg_four_b_local_peak_proximity": 0.79, "avg_green_lateness_ratio": "not_applicable", "changed_axes": "none", "changed_thresholds": "none", "eligible_trigger_count": 4, "false_positive_rate": "2/4 if preferred-bidder-only rows are treated as actionable", "late_green_count": 0, "missed_structural_count": 1, "profile_hypothesis": "current calibrated profile allows Stage2 for policy event only if evidence bridge is present, but residual risk remains when preferred-bidder-only is overweighted", "profile_id": "P0_e2r_2_1_stock_web_calibrated_proxy", "profile_scope": "canonical_archetype:C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY", "row_type": "score_simulation", "score_return_alignment_verdict": "mixed; preferred-bidder-only is poor, legal-clearance bridge is aligned", "selected_entry_trigger_per_case": "all representative rows"}
{"avg_MAE_180D_pct": -40.15, "avg_MAE_90D_pct": -32.16, "avg_MFE_180D_pct": 5.38, "avg_MFE_90D_pct": 4.73, "avg_four_b_full_window_peak_proximity": 0.23, "avg_four_b_local_peak_proximity": 1.0, "avg_green_lateness_ratio": "not_applicable", "changed_axes": "rollback_reference", "changed_thresholds": "older baseline", "eligible_trigger_count": 3, "false_positive_rate": "2/3", "late_green_count": 0, "missed_structural_count": 1, "profile_hypothesis": "baseline without price-only/policy-bridge guard would over-select policy theme spikes", "profile_id": "P0b_e2r_2_0_baseline_reference", "profile_scope": "baseline_reference", "row_type": "score_simulation", "score_return_alignment_verdict": "poor", "selected_entry_trigger_per_case": "preferred-bidder-only theme rows"}
{"avg_MAE_180D_pct": -14.72, "avg_MAE_90D_pct": -14.72, "avg_MFE_180D_pct": 46.59, "avg_MFE_90D_pct": 45.61, "avg_four_b_full_window_peak_proximity": 0.35, "avg_four_b_local_peak_proximity": 0.43, "avg_green_lateness_ratio": "not_applicable", "changed_axes": "existing_axis_strengthened: stage2_required_bridge", "changed_thresholds": "no global threshold change", "eligible_trigger_count": 2, "false_positive_rate": "0/2", "late_green_count": 0, "missed_structural_count": 0, "profile_hypothesis": "policy project events need legal/final contract bridge before Stage2-Actionable; L1 policy link should not be price-only", "profile_id": "P1_sector_specific_candidate_profile", "profile_scope": "large_sector:L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "row_type": "score_simulation", "score_return_alignment_verdict": "better", "selected_entry_trigger_per_case": "legal-clearance row plus indirect watch row"}
{"avg_MAE_180D_pct": -11.85, "avg_MAE_90D_pct": -11.85, "avg_MFE_180D_pct": 80.3, "avg_MFE_90D_pct": 80.3, "avg_four_b_full_window_peak_proximity": 0.0, "avg_four_b_local_peak_proximity": 0.15, "avg_green_lateness_ratio": "not_applicable", "changed_axes": "existing_axis_strengthened: watch_to_green_only_after_final_contract_and_legal_clarity", "changed_thresholds": "Stage3-Green unchanged; C04 legal-bridge gate clarified", "eligible_trigger_count": 1, "false_positive_rate": "0/1", "late_green_count": 0, "missed_structural_count": 0, "profile_hypothesis": "C04 should promote preferred bidder only to Watch; legal appeal rejection/final-contract clarity can be Stage2-Actionable, Green only after final contract/economics", "profile_id": "P2_canonical_archetype_candidate_profile", "profile_scope": "canonical_archetype:C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY", "row_type": "score_simulation", "score_return_alignment_verdict": "strong", "selected_entry_trigger_per_case": "052690 legal-clearance row"}
{"avg_MAE_180D_pct": -51.43, "avg_MAE_90D_pct": -39.45, "avg_MFE_180D_pct": 1.63, "avg_MFE_90D_pct": 1.63, "avg_four_b_full_window_peak_proximity": 0.0, "avg_four_b_local_peak_proximity": 1.0, "avg_green_lateness_ratio": "not_applicable", "changed_axes": "existing_axis_kept: price_only_blowoff_blocks_positive_stage; full_4b_requires_non_price_evidence", "changed_thresholds": "no Green lowering", "eligible_trigger_count": 2, "false_positive_rate": "blocked", "late_green_count": 0, "missed_structural_count": 0, "profile_hypothesis": "block price-only policy proxies where contract/legal/margin evidence is missing", "profile_id": "P3_counterexample_guard_profile", "profile_scope": "canonical_archetype:C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY", "row_type": "score_simulation", "score_return_alignment_verdict": "guardrail useful", "selected_entry_trigger_per_case": "052690/130660 preferred-bidder counterexamples rejected"}
```

## Aggregate Metric Row

```jsonl
{"avg_MAE_180D_pct": -33.08, "avg_MAE_90D_pct": -27.09, "avg_MFE_180D_pct": 24.11, "avg_MFE_90D_pct": 23.62, "calibration_usable_case_count": 4, "canonical_archetype_id": "C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY", "counterexample_count": 2, "do_not_propose_new_weight_delta": true, "fine_archetype_id": "CZECH_NUCLEAR_PREFERRED_BIDDER_TO_LEGAL_CLEARANCE_CONTRACT_DELAY_BRIDGE", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "loop": 87, "new_symbol_count": 3, "new_trigger_family_count": 2, "positive_case_count": 1, "representative_trigger_count": 4, "residual_error_types_found": ["preferred_bidder_price_only_false_positive", "legal_clearance_trigger_missed_if_C04_requires_final_contract_only", "indirect_affiliate_watch_not_Green"], "round": "R11", "row_type": "aggregate_metric", "watch_or_holdout_count": 1}
```

## Shadow Weight / Residual Rule Candidate Row

```jsonl
{"axis": "stage2_required_bridge | earlier_thesis_break_watch | local_4b_watch_guard", "counterexample_guard_ids": ["R11L87-C04-052690-20240718-PREFERRED_BIDDER_COUNTEREXAMPLE", "R11L87-C04-130660-20240718-PREFERRED_BIDDER_COUNTEREXAMPLE"], "positive_support_ids": ["R11L87-C04-052690-20250425-LEGAL_CLEARANCE_POSITIVE"], "production_scoring_changed": false, "promotion_decision": "hold_for_more_evidence", "rollback_condition": "if more C04 legal-clearance rows show high MAE without MFE or if final contract events fail after legal clearance", "row_type": "shadow_weight", "scope": "canonical_archetype:C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY", "shadow_rule": "C04 preferred-bidder-only events remain Watch; Stage2-Actionable requires at least one of final contract, legal appeal clearance, signed EPC/engineering scope, or verified order/margin bridge; price-only proxy spikes cannot unlock Green.", "supporting_trigger_ids": ["R11L87-C04-052690-20240718-PREFERRED_BIDDER_COUNTEREXAMPLE", "R11L87-C04-051600-20240718-PREFERRED_BIDDER_WATCH", "R11L87-C04-130660-20240718-PREFERRED_BIDDER_COUNTEREXAMPLE", "R11L87-C04-052690-20250425-LEGAL_CLEARANCE_POSITIVE"]}
```

## Interpretation

### 1. Preferred-bidder-only is not enough for C04 Green

The preferred-bidder event had strong policy salience but weak C04 conversion proof. It did not yet answer:

```text
- Is the final contract signed?
- Are EDF/legal appeals cleared?
- Is project economics / financing structure stable?
- Is the Korean supplier’s actual scope visible for the listed company?
- Is there backlog/order/margin conversion rather than just theme beta?
```

When those answers were missing, `052690` and especially `130660` showed large post-gap MAE. This is the core C04 residual false-positive route.

### 2. Legal-clearance is a better Stage2-Actionable bridge than first headline

The `052690` 2025-04-25 legal-clearance entry had a much better return profile than the 2024-07-18 preferred-bidder gap entry. The same symbol is intentionally reused across different trigger families because the point of this file is to compare:

```text
same project
same broad beneficiary set
different evidence maturity
different price path
```

This supports a C04-specific bridge:

```text
preferred bidder = Watch
appeal rejection / legal clearance = Stage2-Actionable
final contract + scope/margin/order conversion = possible Yellow/Green
```

### 3. 4B must remain local vs full-window split

For preferred-bidder spikes, a local price peak appeared quickly. But the full-window peak/protection logic differs:

```text
- `052690` 2024-07-18: local peak was immediate, but treating it as full 4B would be price-only.
- `130660` 2024-07-18: local peak and full-window peak were the same; the subsequent collapse confirms price-only proxy risk.
- `052690` 2025-04-25: legal-clearance entry was not 4B; later 2025 highs should be separately audited with valuation/positioning/non-price evidence.
```

This keeps the existing axis:

```text
full_4b_requires_non_price_evidence = true
price_only_blowoff_blocks_positive_stage = true
```

## Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive_case_count | counterexample_count | watch_count | 4B_case_count | 4C_case_count | new_symbol_count | new_trigger_family_count |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|
| L1_INDUSTRIALS_INFRA_DEFENSE_GRID | C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY | CZECH_NUCLEAR_PREFERRED_BIDDER_TO_LEGAL_CLEARANCE_CONTRACT_DELAY_BRIDGE | 1 | 2 | 1 | 2 local price-only | 1 legal-delay watch | 3 | 2 |

## Residual Contribution Summary

```text
new_independent_case_count: 4
reused_case_count: 1
reused_case_ids: R11L87-C04-052690-CZECH_LEGAL_CLEARANCE_TO_CONTRACT_PATH reuses symbol 052690 but not trigger family or entry date
new_symbol_count: 3
new_canonical_archetype_count: 0
new_fine_archetype_count: 1
new_trigger_family_count: 2

tested_existing_calibrated_axes:
- price_only_blowoff_blocks_positive_stage
- full_4b_requires_non_price_evidence
- hard_4c_thesis_break_routes_to_4c
- stage2_required_bridge

residual_error_types_found:
- preferred_bidder_policy_event_false_positive
- legal_clearance_trigger_can_be_missed_if_final_contract_only_rule_is_too_strict
- indirect_affiliate_policy_watch_should_not_unlock_Green

new_axis_proposed: null
existing_axis_strengthened:
- C04 watch_to_green_only_after_final_contract_and_legal_clarity
- C04 stage2_required_bridge should accept legal-clearance/appeal rejection as stronger than preferred-bidder-only, but weaker than final contract
existing_axis_weakened: null
existing_axis_kept:
- price_only_blowoff_blocks_positive_stage
- full_4b_requires_non_price_evidence

sector_specific_rule_candidate: false
canonical_archetype_rule_candidate: hold_for_more_evidence
no_new_signal_reason: not applicable

loop_contribution_label: residual_error_found
do_not_propose_new_weight_delta: true
```

## Deferred Coding Agent Handoff Prompt

```text
Do not execute this handoff inside the research session.

When batch-applying v12 research outputs, ingest this MD as a C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY residual file.

Expected parser rows:
- trigger rows: 4
- case rows: 4
- score_simulation rows: 5
- aggregate_metric rows: 1
- shadow_weight rows: 1

Check that:
1. The C04 preferred-bidder-only rows do not promote to Green.
2. The 052690 legal-clearance row is treated as Stage2-Actionable candidate, not final Green by itself.
3. The 130660 price-only proxy row is a counterexample and must not add positive evidence weight.
4. Existing axes are kept/strengthened, not globally changed:
   - price_only_blowoff_blocks_positive_stage
   - full_4b_requires_non_price_evidence
   - C04 watch_to_green_only_after_final_contract_and_legal_clarity
5. No production scoring default should change from this file alone.
6. Treat this as hold_for_more_evidence for C04 legal-clearance bridge until more independent C04 legal/final-contract rows exist.
```

## Round State

```text
completed_round = R11
completed_loop = 87
next_round = R12
next_loop = 87
round_schedule_status = valid
round_sector_consistency = pass
```
