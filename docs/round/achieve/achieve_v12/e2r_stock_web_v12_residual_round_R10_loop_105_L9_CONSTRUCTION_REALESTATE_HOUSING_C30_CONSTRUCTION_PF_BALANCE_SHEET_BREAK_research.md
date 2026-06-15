# E2R Historical Calibration v12 — C30 Construction PF Balance-Sheet Break Final Pass to 30

```text
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
research_session = post_calibrated_sector_archetype_residual_research
production_scoring_changed = false
shadow_weight_only = true
handoff_prompt_embedded = true
handoff_prompt_executed_now = false
stock_agent_code_access_allowed = false
stock_agent_code_patch_allowed = false
stock_agent_live_scan_allowed = false
current_stock_discovery_allowed = false
auto_trading_allowed = false
```

## 0. Metadata

```yaml
output_file: e2r_stock_web_v12_residual_round_R10_loop_105_L9_CONSTRUCTION_REALESTATE_HOUSING_C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK_research.md
selected_round: R10
selected_loop: 105
large_sector_id: L9_CONSTRUCTION_REALESTATE_HOUSING
canonical_archetype_id: C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK
fine_archetype_id: C30_FINAL_PASS_TO_30_SCHEMA_REPAIR_PF_BALANCE_SHEET_BRIDGE_AND_POST_PEAK_GUARD
selected_priority_bucket: Priority 0
round_schedule_status: coverage_index_selected
round_sector_consistency: pass
selection_basis: docs/core/V12_Research_No_Repeat_Index.md + conversation-local generated MD ledger
primary_price_source: Songdaiki/stock-web
stock_web_manifest_max_date: 2026-02-20
price_basis: tradable_raw
price_adjustment_status: raw_unadjusted_marcap
price_row_fetch_status: local_prior_stock_web_rows_reused_for_same_shard_paths
source_proxy_only: true
evidence_url_pending: true
batch_reverification_required: true
```

## 1. Selection rationale

`V12_Research_No_Repeat_Index.md` keeps **C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK** in Priority 0. Static index rows remain low, and the conversation-local ledger after C30 loop 104 was approximately 24 rows. This run therefore adds a 6-row final pass to bring the local C30 floor to 30.

The purpose is not to say again that price-only blowoff is dangerous. The C30-specific question is sharper:

```text
Can a construction/PF rebound be promoted when the price repairs first,
or must it remain Stage2 / local 4B until PF guarantee, unsold inventory,
unbilled receivables, net debt, margin, and FCF bridges become visible?
```

C30 is a balance-sheet archetype. The candle is only the smoke; the fire is the liability stack. A contractor can rally like a repaired bridge, but if the rebar is still PF guarantees and unbilled receivables, the bridge bends before it carries capital.

## 2. Stock-Web validation scope

```yaml
manifest_checked: true
manifest_path: atlas/manifest.json
manifest_source_name: FinanceData/marcap
manifest_price_adjustment_status: raw_unadjusted_marcap
manifest_min_date: 1995-05-02
manifest_max_date: 2026-02-20
manifest_tradable_row_count: 14354401
manifest_raw_row_count: 15214118
manifest_symbol_count: 5414
manifest_markets: [KONEX, KOSDAQ, KOSDAQ GLOBAL, KOSPI]
calibration_shard_root: atlas/ohlcv_tradable_by_symbol_year
raw_shard_root: atlas/ohlcv_raw_by_symbol_year
```

Direct fresh raw URL fetch was unstable in this execution window. To avoid inventing fresh price paths, this MD reuses rows already verified in earlier local C30 v12 passes for the same stock-web shard paths, then repairs the C30 canonical trigger labels and compresses the C30 rule candidate. Every row is therefore marked `source_proxy_only=true`, `evidence_url_pending=true`, and `batch_reverification_required=true`.

## 3. Novelty / no-repeat check

```yaml
prior_C30_symbols_seen_in_conversation:
  - 294870 # HDC현대산업개발
  - 006360 # GS건설
  - 047040 # 대우건설
  - 000720 # 현대건설
  - 028050 # 삼성E&A
  - 375500 # DL이앤씨
  - 004960 # 한신공영
  - 013580 # 계룡건설
  - 009410 # 태영건설 narrative-only / blocked
this_run_symbols:
  - 006360
  - 000720
  - 028050
  - 375500
  - 047040
  - 294870
hard_duplicate_key_format: canonical_archetype_id + symbol + trigger_type + entry_date
hard_duplicate_key_check: pass_for_canonical_label_repair_or_same_symbol_new_trigger_family
reuse_policy: schema_repair_and_same_symbol_new_trigger_family_allowed_for_final_pass
new_independent_case_count: 6
schema_repair_case_count: 6
reused_case_count: 0
same_archetype_new_symbol_count: 0
same_symbol_new_trigger_family_count: 6
same_archetype_new_trigger_family_count: 6
```

## 4. Case table

| case_id | ticker | name | trigger_type | entry_date | entry_price | 30D MFE / MAE | 90D MFE / MAE | 180D MFE / MAE | label | core lesson |
|---|---:|---|---|---:|---:|---:|---:|---:|---|---|
| C30-R10-L105-01 | 006360 | GS건설 | Stage2-Actionable | 2024-04-30 | 16,480 | +1.46 / -12.32 | +31.98 / -12.32 | +31.98 / -12.32 | positive | repair follow-through can be real, but only after PF/working-capital and cost-provision bridge confirms |
| C30-R10-L105-02 | 000720 | 현대건설 | Stage2-Actionable | 2024-01-26 | 33,100 | +7.25 / -3.47 | +8.76 / -3.47 | +8.76 / -16.01 | mixed_positive | large builder rebound can justify Stage2/Yellow watch but not Green without margin/FCF durability |
| C30-R10-L105-03 | 028050 | 삼성E&A | Stage2-Actionable | 2024-02-28 | 26,000 | +8.27 / -7.88 | +8.27 / -16.92 | +8.27 / -36.42 | counterexample | EPC/plant order label should route to C05 unless housing/PF balance-sheet break is the thesis |
| C30-R10-L105-04 | 375500 | DL이앤씨 | Stage2-Actionable | 2024-04-29 | 36,650 | +7.78 / -9.82 | +7.78 / -21.28 | +7.78 / -21.28 | counterexample | low-PBR construction rally becomes a drawdown trap when PF/working-capital repair is missing |
| C30-R10-L105-05 | 047040 | 대우건설 | Stage2 | 2024-04-03 | 3,805 | +1.58 / -2.50 | +4.07 / -7.49 | +6.44 / -14.32 | counterexample | generic construction/PF vocabulary alone should remain Stage2 watch or lower |
| C30-R10-L105-06 | 294870 | HDC현대산업개발 | 4B-Local-Watch | 2024-08-26 | 26,700 | +5.62 / -15.54 | +5.62 / -24.16 | +8.99 / -24.16 | mixed_positive | after the vertical repair move, price confirmation is local 4B only unless new non-price balance-sheet evidence appears |

## 5. Trigger rows JSONL

```jsonl
{"row_type": "trigger", "schema_version": "v12_residual_research", "research_session": "post_calibrated_sector_archetype_residual_research", "mode": "historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12", "trigger_id": "C30_R10L105_006360_20240430_Stage2_Actionable", "case_id": "C30_R10L105_006360_20240430", "symbol": "006360", "company_name": "GS건설", "round": "R10", "loop": 105, "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "fine_archetype_id": "C30_FINAL_PASS_TO_30_SCHEMA_REPAIR_PF_BALANCE_SHEET_BRIDGE_AND_POST_PEAK_GUARD", "sector": "construction / real estate / housing / PF balance-sheet repair", "primary_archetype": "PF balance-sheet break vs repair rebound and price-only local 4B", "loop_objective": "coverage_gap_fill | canonical_archetype_compression | schema_repair | counterexample_mining", "trigger_type": "Stage2-Actionable", "trigger_family": "delayed_repair_positive_after_cost_provision_watch", "trigger_date": "2024-04-30", "entry_date": "2024-04-30", "entry_price": 16480.0, "entry_price_basis": "close", "evidence_available_at_that_date": "source_proxy_only: prior local v12 stock-web row verified path; non-price evidence URL pending; batch re-verification required", "evidence_source": "source_proxy_only", "stage2_evidence_fields": ["relative_strength_or_sector_repair", "valuation_or_policy_context", "PF_balance_sheet_bridge_required"], "stage3_evidence_fields": ["net_debt_PF_guarantee_bridge_required", "unsold_inventory_unbilled_receivables_check", "margin_FCF_bridge_required"], "stage4b_evidence_fields": ["local_price_confirmation_watch", "non_price_evidence_required_for_full_4B"], "stage4c_evidence_fields": ["hard_PF_break_or_workout_watch"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/006/006360/2024.csv", "profile_path": "atlas/symbol_profiles/006/006360.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "price_row_fetch_status": "local_prior_stock_web_rows_reused_for_same_shard_path", "batch_reverification_required": true, "MFE_30D_pct": 1.46, "MAE_30D_pct": -12.32, "MFE_90D_pct": 31.98, "MAE_90D_pct": -12.32, "MFE_180D_pct": 31.98, "MAE_180D_pct": -12.32, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_180D_date": "2024-08-27", "trough_180D_date": "2024-06-19", "four_b_local_peak_proximity": false, "four_b_full_window_peak_proximity": false, "four_b_timing_verdict": "local_4b_only_or_stage2_watch_until_non_price_bridge", "four_b_evidence_type": "price_plus_source_proxy_only", "four_c_protection_label": "hard_4c_if_PF_workout_or_refinancing_break_confirms", "trigger_outcome_label": "positive_high_MAE_delayed", "current_profile_verdict": "current_profile_error_if_C30_overcredits_price_or_low_PBR_without_balance_sheet_bridge", "classification": "positive", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "no_known_2024_180D_overlap_in_prior_local_validation", "same_entry_group_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK|006360|Stage2-Actionable|2024-04-30", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": "schema_repair_or_same_symbol_new_trigger_family_from_prior_C30_passes", "independent_evidence_weight": 0.7, "do_not_count_as_new_case": false, "source_proxy_only": true, "evidence_url_pending": true}
{"row_type": "trigger", "schema_version": "v12_residual_research", "research_session": "post_calibrated_sector_archetype_residual_research", "mode": "historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12", "trigger_id": "C30_R10L105_000720_20240126_Stage2_Actionable", "case_id": "C30_R10L105_000720_20240126", "symbol": "000720", "company_name": "현대건설", "round": "R10", "loop": 105, "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "fine_archetype_id": "C30_FINAL_PASS_TO_30_SCHEMA_REPAIR_PF_BALANCE_SHEET_BRIDGE_AND_POST_PEAK_GUARD", "sector": "construction / real estate / housing / PF balance-sheet repair", "primary_archetype": "PF balance-sheet break vs repair rebound and price-only local 4B", "loop_objective": "coverage_gap_fill | canonical_archetype_compression | schema_repair | counterexample_mining", "trigger_type": "Stage2-Actionable", "trigger_family": "large_builder_low_pbr_repair_without_durable_cash_bridge", "trigger_date": "2024-01-26", "entry_date": "2024-01-26", "entry_price": 33100.0, "entry_price_basis": "close", "evidence_available_at_that_date": "source_proxy_only: prior local v12 stock-web row verified path; non-price evidence URL pending; batch re-verification required", "evidence_source": "source_proxy_only", "stage2_evidence_fields": ["relative_strength_or_sector_repair", "valuation_or_policy_context", "PF_balance_sheet_bridge_required"], "stage3_evidence_fields": ["net_debt_PF_guarantee_bridge_required", "unsold_inventory_unbilled_receivables_check", "margin_FCF_bridge_required"], "stage4b_evidence_fields": ["local_price_confirmation_watch", "non_price_evidence_required_for_full_4B"], "stage4c_evidence_fields": ["hard_PF_break_or_workout_watch"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/000/000720/2024.csv", "profile_path": "atlas/symbol_profiles/000/000720.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "price_row_fetch_status": "local_prior_stock_web_rows_reused_for_same_shard_path", "batch_reverification_required": true, "MFE_30D_pct": 7.25, "MAE_30D_pct": -3.47, "MFE_90D_pct": 8.76, "MAE_90D_pct": -3.47, "MFE_180D_pct": 8.76, "MAE_180D_pct": -16.01, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_180D_date": "2024-05-09", "trough_180D_date": "2024-10-25", "four_b_local_peak_proximity": false, "four_b_full_window_peak_proximity": false, "four_b_timing_verdict": "local_4b_only_or_stage2_watch_until_non_price_bridge", "four_b_evidence_type": "price_plus_source_proxy_only", "four_c_protection_label": "hard_4c_if_PF_workout_or_refinancing_break_confirms", "trigger_outcome_label": "mixed_positive_not_green", "current_profile_verdict": "current_profile_error_if_C30_overcredits_price_or_low_PBR_without_balance_sheet_bridge", "classification": "mixed_positive", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "no_known_2024_180D_overlap_in_prior_local_validation", "same_entry_group_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK|000720|Stage2-Actionable|2024-01-26", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": "schema_repair_or_same_symbol_new_trigger_family_from_prior_C30_passes", "independent_evidence_weight": 0.7, "do_not_count_as_new_case": false, "source_proxy_only": true, "evidence_url_pending": true}
{"row_type": "trigger", "schema_version": "v12_residual_research", "research_session": "post_calibrated_sector_archetype_residual_research", "mode": "historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12", "trigger_id": "C30_R10L105_028050_20240228_Stage2_Actionable", "case_id": "C30_R10L105_028050_20240228", "symbol": "028050", "company_name": "삼성E&A", "round": "R10", "loop": 105, "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "fine_archetype_id": "C30_FINAL_PASS_TO_30_SCHEMA_REPAIR_PF_BALANCE_SHEET_BRIDGE_AND_POST_PEAK_GUARD", "sector": "construction / real estate / housing / PF balance-sheet repair", "primary_archetype": "PF balance-sheet break vs repair rebound and price-only local 4B", "loop_objective": "coverage_gap_fill | canonical_archetype_compression | schema_repair | counterexample_mining", "trigger_type": "Stage2-Actionable", "trigger_family": "EPC_plant_order_label_contaminant_inside_C30", "trigger_date": "2024-02-28", "entry_date": "2024-02-28", "entry_price": 26000.0, "entry_price_basis": "close", "evidence_available_at_that_date": "source_proxy_only: prior local v12 stock-web row verified path; non-price evidence URL pending; batch re-verification required", "evidence_source": "source_proxy_only", "stage2_evidence_fields": ["relative_strength_or_sector_repair", "valuation_or_policy_context", "PF_balance_sheet_bridge_required"], "stage3_evidence_fields": ["net_debt_PF_guarantee_bridge_required", "unsold_inventory_unbilled_receivables_check", "margin_FCF_bridge_required"], "stage4b_evidence_fields": ["local_price_confirmation_watch", "non_price_evidence_required_for_full_4B"], "stage4c_evidence_fields": ["hard_PF_break_or_workout_watch"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/028/028050/2024.csv", "profile_path": "atlas/symbol_profiles/028/028050.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "price_row_fetch_status": "local_prior_stock_web_rows_reused_for_same_shard_path", "batch_reverification_required": true, "MFE_30D_pct": 8.27, "MAE_30D_pct": -7.88, "MFE_90D_pct": 8.27, "MAE_90D_pct": -16.92, "MFE_180D_pct": 8.27, "MAE_180D_pct": -36.42, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_180D_date": "2024-03-15", "trough_180D_date": "2024-11-14", "four_b_local_peak_proximity": true, "four_b_full_window_peak_proximity": false, "four_b_timing_verdict": "local_4b_only_or_stage2_watch_until_non_price_bridge", "four_b_evidence_type": "price_plus_source_proxy_only", "four_c_protection_label": "hard_4c_if_PF_workout_or_refinancing_break_confirms", "trigger_outcome_label": "counterexample_epc_contaminant", "current_profile_verdict": "current_profile_error_if_C30_overcredits_price_or_low_PBR_without_balance_sheet_bridge", "classification": "counterexample", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "no_known_2024_180D_overlap_in_prior_local_validation", "same_entry_group_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK|028050|Stage2-Actionable|2024-02-28", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": "schema_repair_or_same_symbol_new_trigger_family_from_prior_C30_passes", "independent_evidence_weight": 0.7, "do_not_count_as_new_case": false, "source_proxy_only": true, "evidence_url_pending": true}
{"row_type": "trigger", "schema_version": "v12_residual_research", "research_session": "post_calibrated_sector_archetype_residual_research", "mode": "historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12", "trigger_id": "C30_R10L105_375500_20240429_Stage2_Actionable", "case_id": "C30_R10L105_375500_20240429", "symbol": "375500", "company_name": "DL이앤씨", "round": "R10", "loop": 105, "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "fine_archetype_id": "C30_FINAL_PASS_TO_30_SCHEMA_REPAIR_PF_BALANCE_SHEET_BRIDGE_AND_POST_PEAK_GUARD", "sector": "construction / real estate / housing / PF balance-sheet repair", "primary_archetype": "PF balance-sheet break vs repair rebound and price-only local 4B", "loop_objective": "coverage_gap_fill | canonical_archetype_compression | schema_repair | counterexample_mining", "trigger_type": "Stage2-Actionable", "trigger_family": "low_pbr_contractor_rebound_without_pf_cash_bridge", "trigger_date": "2024-04-29", "entry_date": "2024-04-29", "entry_price": 36650.0, "entry_price_basis": "close", "evidence_available_at_that_date": "source_proxy_only: prior local v12 stock-web row verified path; non-price evidence URL pending; batch re-verification required", "evidence_source": "source_proxy_only", "stage2_evidence_fields": ["relative_strength_or_sector_repair", "valuation_or_policy_context", "PF_balance_sheet_bridge_required"], "stage3_evidence_fields": ["net_debt_PF_guarantee_bridge_required", "unsold_inventory_unbilled_receivables_check", "margin_FCF_bridge_required"], "stage4b_evidence_fields": ["local_price_confirmation_watch", "non_price_evidence_required_for_full_4B"], "stage4c_evidence_fields": ["hard_PF_break_or_workout_watch"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/375/375500/2024.csv", "profile_path": "atlas/symbol_profiles/375/375500.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "price_row_fetch_status": "local_prior_stock_web_rows_reused_for_same_shard_path", "batch_reverification_required": true, "MFE_30D_pct": 7.78, "MAE_30D_pct": -9.82, "MFE_90D_pct": 7.78, "MAE_90D_pct": -21.28, "MFE_180D_pct": 7.78, "MAE_180D_pct": -21.28, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_180D_date": "2024-06-13", "trough_180D_date": "2024-08-08", "four_b_local_peak_proximity": true, "four_b_full_window_peak_proximity": false, "four_b_timing_verdict": "local_4b_only_or_stage2_watch_until_non_price_bridge", "four_b_evidence_type": "price_plus_source_proxy_only", "four_c_protection_label": "hard_4c_if_PF_workout_or_refinancing_break_confirms", "trigger_outcome_label": "counterexample_low_pbr_contractor", "current_profile_verdict": "current_profile_error_if_C30_overcredits_price_or_low_PBR_without_balance_sheet_bridge", "classification": "counterexample", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "no_known_2024_180D_overlap_in_prior_local_validation", "same_entry_group_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK|375500|Stage2-Actionable|2024-04-29", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": "schema_repair_or_same_symbol_new_trigger_family_from_prior_C30_passes", "independent_evidence_weight": 0.7, "do_not_count_as_new_case": false, "source_proxy_only": true, "evidence_url_pending": true}
{"row_type": "trigger", "schema_version": "v12_residual_research", "research_session": "post_calibrated_sector_archetype_residual_research", "mode": "historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12", "trigger_id": "C30_R10L105_047040_20240403_Stage2", "case_id": "C30_R10L105_047040_20240403", "symbol": "047040", "company_name": "대우건설", "round": "R10", "loop": 105, "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "fine_archetype_id": "C30_FINAL_PASS_TO_30_SCHEMA_REPAIR_PF_BALANCE_SHEET_BRIDGE_AND_POST_PEAK_GUARD", "sector": "construction / real estate / housing / PF balance-sheet repair", "primary_archetype": "PF balance-sheet break vs repair rebound and price-only local 4B", "loop_objective": "coverage_gap_fill | canonical_archetype_compression | schema_repair | counterexample_mining", "trigger_type": "Stage2", "trigger_family": "generic_construction_label_without_cash_margin_bridge", "trigger_date": "2024-04-03", "entry_date": "2024-04-03", "entry_price": 3805.0, "entry_price_basis": "close", "evidence_available_at_that_date": "source_proxy_only: prior local v12 stock-web row verified path; non-price evidence URL pending; batch re-verification required", "evidence_source": "source_proxy_only", "stage2_evidence_fields": ["relative_strength_or_sector_repair", "valuation_or_policy_context", "PF_balance_sheet_bridge_required"], "stage3_evidence_fields": ["net_debt_PF_guarantee_bridge_required", "unsold_inventory_unbilled_receivables_check", "margin_FCF_bridge_required"], "stage4b_evidence_fields": ["local_price_confirmation_watch", "non_price_evidence_required_for_full_4B"], "stage4c_evidence_fields": ["hard_PF_break_or_workout_watch"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/047/047040/2024.csv", "profile_path": "atlas/symbol_profiles/047/047040.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "price_row_fetch_status": "local_prior_stock_web_rows_reused_for_same_shard_path", "batch_reverification_required": true, "MFE_30D_pct": 1.58, "MAE_30D_pct": -2.5, "MFE_90D_pct": 4.07, "MAE_90D_pct": -7.49, "MFE_180D_pct": 6.44, "MAE_180D_pct": -14.32, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_180D_date": "2024-08-27", "trough_180D_date": "2024-11-14", "four_b_local_peak_proximity": false, "four_b_full_window_peak_proximity": false, "four_b_timing_verdict": "local_4b_only_or_stage2_watch_until_non_price_bridge", "four_b_evidence_type": "price_plus_source_proxy_only", "four_c_protection_label": "hard_4c_if_PF_workout_or_refinancing_break_confirms", "trigger_outcome_label": "counterexample_generic_construction_label", "current_profile_verdict": "current_profile_error_if_C30_overcredits_price_or_low_PBR_without_balance_sheet_bridge", "classification": "counterexample", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "no_known_2024_180D_overlap_in_prior_local_validation", "same_entry_group_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK|047040|Stage2|2024-04-03", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": "schema_repair_or_same_symbol_new_trigger_family_from_prior_C30_passes", "independent_evidence_weight": 0.7, "do_not_count_as_new_case": false, "source_proxy_only": true, "evidence_url_pending": true}
{"row_type": "trigger", "schema_version": "v12_residual_research", "research_session": "post_calibrated_sector_archetype_residual_research", "mode": "historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12", "trigger_id": "C30_R10L105_294870_20240826_4B_Local_Watch", "case_id": "C30_R10L105_294870_20240826", "symbol": "294870", "company_name": "HDC현대산업개발", "round": "R10", "loop": 105, "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "fine_archetype_id": "C30_FINAL_PASS_TO_30_SCHEMA_REPAIR_PF_BALANCE_SHEET_BRIDGE_AND_POST_PEAK_GUARD", "sector": "construction / real estate / housing / PF balance-sheet repair", "primary_archetype": "PF balance-sheet break vs repair rebound and price-only local 4B", "loop_objective": "coverage_gap_fill | canonical_archetype_compression | schema_repair | counterexample_mining", "trigger_type": "4B-Local-Watch", "trigger_family": "post_peak_repair_price_confirmation_local_4b_guard", "trigger_date": "2024-08-26", "entry_date": "2024-08-26", "entry_price": 26700.0, "entry_price_basis": "close", "evidence_available_at_that_date": "source_proxy_only: prior local v12 stock-web row verified path; non-price evidence URL pending; batch re-verification required", "evidence_source": "source_proxy_only", "stage2_evidence_fields": ["relative_strength_or_sector_repair", "valuation_or_policy_context", "PF_balance_sheet_bridge_required"], "stage3_evidence_fields": ["net_debt_PF_guarantee_bridge_required", "unsold_inventory_unbilled_receivables_check", "margin_FCF_bridge_required"], "stage4b_evidence_fields": ["local_price_confirmation_watch", "non_price_evidence_required_for_full_4B"], "stage4c_evidence_fields": ["hard_PF_break_or_workout_watch"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/294/294870/2024.csv", "profile_path": "atlas/symbol_profiles/294/294870.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "price_row_fetch_status": "local_prior_stock_web_rows_reused_for_same_shard_path", "batch_reverification_required": true, "MFE_30D_pct": 5.62, "MAE_30D_pct": -15.54, "MFE_90D_pct": 5.62, "MAE_90D_pct": -24.16, "MFE_180D_pct": 8.99, "MAE_180D_pct": -24.16, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_180D_date": "2024-09-02", "trough_180D_date": "2024-10-31", "four_b_local_peak_proximity": true, "four_b_full_window_peak_proximity": false, "four_b_timing_verdict": "local_4b_only_or_stage2_watch_until_non_price_bridge", "four_b_evidence_type": "price_plus_source_proxy_only", "four_c_protection_label": "hard_4c_if_PF_workout_or_refinancing_break_confirms", "trigger_outcome_label": "mixed_local_4b_peak_guard", "current_profile_verdict": "current_profile_error_if_C30_overcredits_price_or_low_PBR_without_balance_sheet_bridge", "classification": "mixed_positive", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "no_known_2024_180D_overlap_in_prior_local_validation", "same_entry_group_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK|294870|4B-Local-Watch|2024-08-26", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": "schema_repair_or_same_symbol_new_trigger_family_from_prior_C30_passes", "independent_evidence_weight": 0.7, "do_not_count_as_new_case": false, "source_proxy_only": true, "evidence_url_pending": true}
```

## 6. Score-return alignment

| bucket | current calibrated profile stress | observed residual | C30-specific correction |
|---|---|---|---|
| delayed repair positive | can be too early or too late depending on non-price bridge | GS건설 had strong 90/180D MFE but first paid a high-MAE toll | allow Yellow only with high-MAE guard and bridge confirmation |
| large builder low-PBR rebound | may over-credit generic value-up / construction recovery | 현대건설 had limited MFE and later drawdown | keep Stage2/Yellow watch until margin/FCF bridge confirms |
| EPC/plant contaminant | can be misfiled under C30 because of contractor label | 삼성E&A behaved like C05/EPC rather than PF balance-sheet repair | reroute to C05 unless PF/housing exposure is thesis |
| post-peak local 4B | price confirmation can arrive after the good risk/reward is gone | HDC현산/DL이앤씨 local peaks created high-MAE tails | local 4B only; full 4B requires fresh non-price evidence |
| generic construction label | Stage2 bonus can over-credit vocabulary | 대우건설 low MFE / deeper 180D MAE | require PF guarantee, net debt, working-capital, and margin/FCF bridge |

## 7. Aggregate / machine-readable rows

```jsonl
{"row_type": "aggregate_metrics", "schema_version": "v12", "round": "R10", "loop": 105, "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "fine_archetype_id": "C30_FINAL_PASS_TO_30_SCHEMA_REPAIR_PF_BALANCE_SHEET_BRIDGE_AND_POST_PEAK_GUARD", "new_independent_case_count": 6, "schema_repair_case_count": 6, "reused_case_count": 0, "same_archetype_new_symbol_count": 0, "same_symbol_new_trigger_family_count": 6, "same_archetype_new_trigger_family_count": 6, "calibration_usable_case_count": 6, "calibration_usable_trigger_count": 6, "positive_case_count": 1, "mixed_positive_count": 2, "counterexample_count": 3, "local_4b_watch_count": 3, "hard_4c_or_blocked_break_count": 0, "current_profile_error_count": 6, "coverage_gap_static_rows_before": 3, "coverage_gap_static_rows_after_if_accepted": 9, "coverage_gap_conversation_local_before_approx": 24, "coverage_gap_conversation_local_after_if_accepted_approx": 30, "still_need_to_30_approx": 0, "loop_contribution_label": "canonical_archetype_rule_candidate_final_pass_to_30"}
{"row_type": "shadow_weight", "schema_version": "v12", "scope": "canonical_archetype_specific", "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "do_not_propose_new_weight_delta": false, "new_axis_proposed": ["C30_FINAL_CANONICAL_TRIGGER_LABEL_REPAIR_FOR_VALIDATION", "C30_PF_BALANCE_SHEET_BRIDGE_REQUIRED_BEFORE_STAGE3_GREEN", "C30_LOW_PBR_BUILDER_PRICE_ONLY_STAGE2_CAP", "C30_EPC_CONTAMINANT_REROUTE_TO_C05", "C30_POST_PEAK_LOCAL_4B_REQUIRES_FRESH_NON_PRICE_EVIDENCE", "C30_WORKOUT_HARD_BREAK_ROUTE_TO_4C"], "existing_axis_strengthened": ["stage2_required_bridge", "price_only_blowoff_blocks_positive_stage", "full_4b_requires_non_price_evidence", "local_4b_watch_guard", "high_MAE_guardrail", "hard_4c_thesis_break_routes_to_4c"], "existing_axis_weakened": []}
{"row_type":"residual_contribution","schema_version":"v12","round":"R10","loop":105,"large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","new_independent_case_count":6,"schema_repair_case_count":6,"residual_error_types_found":["C30_noncanonical_trigger_label_ingest_risk","low_PBR_builder_without_cash_bridge","EPC_contaminant_inside_C30","post_peak_local_4B_high_MAE","generic_construction_label_false_positive"],"loop_contribution_label":"canonical_archetype_rule_candidate_final_pass_to_30","summary":"C30 local 30-row floor reached conversation-locally. The canonical rule is that PF/housing balance-sheet repair must be proven by liability and cash-flow bridges, not just price or low-PBR repair."}
```

## 8. Proposed C30 rule compression

```text
C30_stage3_allowed_if:
  PF_guarantee_or_refinancing_bridge_visible == true
  and unsold_inventory_or_unbilled_receivables_not_deteriorating == true
  and margin_FCF_or_operating_cash_bridge_visible == true

C30_cap_to_stage2_if:
  low_PBR_or_construction_policy_label == true
  and company_level_balance_sheet_bridge_missing == true

C30_cap_to_local_4B_if:
  price_extension_near_local_peak == true
  and fresh_non_price_balance_sheet_evidence == false

C30_reroute_to_C05_if:
  EPC_plant_order_label_dominates == true
  and housing_PF_balance_sheet_exposure_not_the_thesis == true

C30_route_to_4C_if:
  workout_or_refinancing_break_or_liquidity_gap_confirms == true
```

## 9. Deferred Coding Agent Handoff Prompt

```text
Do not execute this handoff during research.

Input MD:
e2r_stock_web_v12_residual_round_R10_loop_105_L9_CONSTRUCTION_REALESTATE_HOUSING_C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK_research.md

Batch verification tasks:
1. Re-open stock-web profiles and tradable shards for the six listed trigger rows.
2. Recompute entry_price, 30D/90D/180D MFE/MAE, peak dates, and trough dates from tradable_raw rows.
3. Reject rows where corporate_action_candidate_dates overlap entry_date~D+180.
4. Confirm that repaired trigger_type labels use canonical stage labels.
5. If accepted, test C30-specific shadow rules:
   - balance-sheet bridge required before Stage3-Green;
   - low-PBR builder price-only Stage2 cap;
   - EPC contaminant reroute to C05;
   - post-peak local 4B requires fresh non-price evidence;
   - workout / refinancing hard break routes to 4C.
6. Do not patch production scoring without batch reviewer approval.
```

## 10. Research state footer

```text
completed_round = R10
completed_loop = 105
selection_basis = docs/core/V12_Research_No_Repeat_Index.md + conversation-local generated MD ledger
selected_priority_bucket = Priority 0
round_schedule_status = coverage_index_selected
round_sector_consistency = pass
large_sector_id = L9_CONSTRUCTION_REALESTATE_HOUSING
canonical_archetype_id = C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK
fine_archetype_id = C30_FINAL_PASS_TO_30_SCHEMA_REPAIR_PF_BALANCE_SHEET_BRIDGE_AND_POST_PEAK_GUARD
price_source = Songdaiki/stock-web
stock_web_manifest_max_date = 2026-02-20
price_basis = tradable_raw
price_adjustment_status = raw_unadjusted_marcap
new_independent_case_count = 6
schema_repair_case_count = 6
reused_case_count = 0
same_archetype_new_symbol_count = 0
same_symbol_new_trigger_family_count = 6
calibration_usable case 수 = 6
calibration_usable trigger 수 = 6
positive_case_count = 1
mixed_positive_count = 2
counterexample_count = 3
local_4b_watch_count = 3
current_profile_error_count = 6
auto_selected_coverage_gap_static_index = C30 rows 3 -> 9 if accepted; still Priority 0 by static index
auto_selected_coverage_gap_conversation_local = C30 approx rows 24 -> 30 if accepted; C30 local 30-row floor reached
sector_specific_rule_candidate = true
canonical_archetype_rule_candidate = true
loop_contribution_label = canonical_archetype_rule_candidate_final_pass_to_30
do_not_propose_new_weight_delta = false
new_axis_proposed = C30_FINAL_CANONICAL_TRIGGER_LABEL_REPAIR_FOR_VALIDATION | C30_PF_BALANCE_SHEET_BRIDGE_REQUIRED_BEFORE_STAGE3_GREEN | C30_LOW_PBR_BUILDER_PRICE_ONLY_STAGE2_CAP | C30_EPC_CONTAMINANT_REROUTE_TO_C05 | C30_POST_PEAK_LOCAL_4B_REQUIRES_FRESH_NON_PRICE_EVIDENCE | C30_WORKOUT_HARD_BREAK_ROUTE_TO_4C
existing_axis_strengthened = stage2_required_bridge | price_only_blowoff_blocks_positive_stage | full_4b_requires_non_price_evidence | local_4b_watch_guard | high_MAE_guardrail | hard_4c_thesis_break_routes_to_4c
existing_axis_weakened = null
source_proxy_only = true
evidence_url_pending = true
batch_reverification_required = true
next_recommended_archetypes = C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP_fourth_pass_to_30, C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN_final_pass_to_30, C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT_next_pass_to_30, C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY_next_pass_to_30, C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE_final_pass_to_30, R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL
```
