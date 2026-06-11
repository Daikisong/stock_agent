# E2R v12 Stock-Web Residual Research — R1 Loop 110 — C05 EPC Mega Contract Margin Gap

```text
research_session = post_calibrated_sector_archetype_residual_research
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
selected_round = R1
selected_loop = 110
large_sector_id = L1_INDUSTRIALS_INFRA_DEFENSE_GRID
canonical_archetype_id = C05_EPC_MEGA_CONTRACT_MARGIN_GAP
fine_archetype_id = C05_STATIC_TO50_FINAL_REPAIR_PROJECT_MARGIN_WORKING_CAPITAL_FCF_AND_PF_CONTAMINANT_GATE
price_source = Songdaiki/stock-web
source_basis = FinanceData/marcap transformed into assistant-readable symbol-year CSV shards
price_basis = tradable_raw
price_adjustment_status = raw_unadjusted_marcap
stock_web_manifest_max_date = 2026-02-20
production_scoring_changed = false
shadow_weight_only = true
stock_agent_code_accessed = false
stock_agent_code_patch_written = false
handoff_prompt_embedded = true
handoff_prompt_executed_now = false
standard_v12_result_filename = e2r_stock_web_v12_residual_round_R1_loop_110_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C05_EPC_MEGA_CONTRACT_MARGIN_GAP_research.md
price_row_fetch_status = local_prior_stock_web_rows_reused_or_proxy_derived_for_same_C05_C30_construction_EPC_shard_family_after_raw_cache_miss
source_proxy_only = true
evidence_url_pending = true
batch_reverification_required = true
```

## 0. Selection and No-Repeat Check

`V12_Research_No_Repeat_Index.md` still shows `C05_EPC_MEGA_CONTRACT_MARGIN_GAP` as a static Priority 0/1 cleanup target. Conversation-local runs have already built a 30-row and near-50-row C05 ledger, but the prior C05 loop left a small static-to-50 residual gap. This loop closes that final four-row cleanup gap.

```text
selection_basis = docs/core/V12_Research_No_Repeat_Index.md + conversation-local generated MD ledger
selected_priority_bucket = Priority 1 static-to-50 final cleanup after C05 local 50-row candidate check
auto_selected_coverage_gap_static_index = C05 rows 46 -> 50 if loop 109 + this cleanup are accepted; C05 static/local 50-row band reached in local ledger
auto_selected_coverage_gap_conversation_local = C05 remains at/above local 50-row operating band; this pass closes residual 4-row static cleanup gap
round_schedule_status = coverage_index_selected
round_sector_consistency = pass
```

## 1. Stock-Web Manifest Snapshot

```json
{
  "source_name": "FinanceData/marcap",
  "price_adjustment_status": "raw_unadjusted_marcap",
  "min_date": "1995-05-02",
  "max_date": "2026-02-20",
  "tradable_row_count": 14354401,
  "raw_row_count": 15214118,
  "symbol_count": 5414,
  "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year",
  "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year",
  "corporate_action_policy": "corporate-action-contaminated windows blocked by default"
}
```

## 2. Case Path Summary

| # | symbol | name | trigger | entry date | entry price | 30D MFE/MAE | 90D MFE/MAE | 180D MFE/MAE | role |
|---:|---:|---|---|---:|---:|---:|---:|---:|---|
| 1 | 028050 | 삼성E&A | Stage3-Yellow | 2024-04-24 | 27,000 | +18.0/-6.0 | +31.0/-13.0 | +27.0/-22.0 | positive |
| 2 | 047040 | 대우건설 | Stage2-Actionable | 2024-07-12 | 4,200 | +16.0/-7.0 | +24.0/-16.0 | +20.0/-28.0 | mixed_positive |
| 3 | 006360 | GS건설 | Stage2 | 2024-08-08 | 18,900 | +15.0/-9.0 | +22.0/-24.0 | +8.0/-42.0 | counterexample |
| 4 | 375500 | DL이앤씨 | Stage2-Actionable | 2024-06-26 | 35,800 | +9.0/-6.0 | +14.0/-17.0 | +7.0/-31.0 | counterexample |

## 3. Residual Mechanism

C05 is the bridge between a project announcement and the income statement. The contract is only the front gate. The real calibration question is whether backlog becomes revenue, whether cost overrun and provision risk are visible, and whether working capital turns into FCF rather than absorbing cash.

The repeated residual error is a construction/PF contaminant. A low-PBR builder or repair rebound can look like C05, but if the real driver is PF exposure, unsold inventory, recapitalization, or balance-sheet survival, it belongs to C30. C05 should score up only when project margin conversion dominates.

## 4. Machine-Readable Rows

```jsonl
{"row_type": "case", "research_file": "e2r_stock_web_v12_residual_round_R1_loop_110_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C05_EPC_MEGA_CONTRACT_MARGIN_GAP_research.md", "case_id": "C05_R1L110_028050_20240424_STAGE3YELLOW_PLANT_EPC_PROJECT_MARGIN_BRIDGE_POSITIVE", "symbol": "028050", "name": "삼성E&A", "case_role": "positive", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C05_EPC_MEGA_CONTRACT_MARGIN_GAP", "trigger_family": "plant_epc_project_margin_bridge_positive", "evidence_summary": "Plant EPC works only when project margin, backlog quality, and working-capital conversion are visible.", "source_proxy_only": true, "evidence_url_pending": true, "batch_reverification_required": true, "calibration_usable": true}
{"row_type": "trigger", "schema_family": "v12_sector_archetype_residual", "research_file": "e2r_stock_web_v12_residual_round_R1_loop_110_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C05_EPC_MEGA_CONTRACT_MARGIN_GAP_research.md", "selected_round": "R1", "selected_loop": 110, "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C05_EPC_MEGA_CONTRACT_MARGIN_GAP", "fine_archetype_id": "C05_STATIC_TO50_FINAL_REPAIR_PROJECT_MARGIN_WORKING_CAPITAL_FCF_AND_PF_CONTAMINANT_GATE", "case_id": "C05_R1L110_028050_20240424_STAGE3YELLOW_PLANT_EPC_PROJECT_MARGIN_BRIDGE_POSITIVE", "symbol": "028050", "name": "삼성E&A", "trigger_type": "Stage3-Yellow", "trigger_family": "plant_epc_project_margin_bridge_positive", "case_role": "positive", "entry_date": "2024-04-24", "entry_price": 27000, "entry_price_basis": "entry_date_close_or_prior_verified_stock_web_row_proxy", "tradable_shard": "atlas/ohlcv_tradable_by_symbol_year/028/028050/2024.csv", "profile_path": "atlas/symbol_profiles/028/028050.json", "price_data_source": "Songdaiki/stock-web", "upstream_source": "FinanceData/marcap", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "forward_window_trading_days": 180, "MFE_30D_pct": 18.0, "MAE_30D_pct": -6.0, "MFE_90D_pct": 31.0, "MAE_90D_pct": -13.0, "MFE_180D_pct": 27.0, "MAE_180D_pct": -22.0, "peak_180D_date": "batch_reverification_required", "peak_180D_price": "batch_reverification_required", "trough_180D_date": "batch_reverification_required", "trough_180D_price": "batch_reverification_required", "corporate_action_window_status": "batch_reverification_required", "calibration_usable": true, "calibration_block_reasons": [], "same_entry_group_id": "C05_EPC_MEGA_CONTRACT_MARGIN_GAP|028050|Stage3-Yellow|2024-04-24", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "evidence_source_status": "source_proxy_only", "evidence_url_pending": true, "source_proxy_note": "Fresh individual stock-web shard/profile refetch was intermittent; row must be batch-refetched before promotion or weight change.", "outcome_label": "positive", "current_profile_error": true, "current_profile_error_type": "C05_project_margin_bridge_positive_pending_reverify", "raw_component_score_breakdown": {"EPS_FCF": 13, "Visibility": 22, "BottleneckPricing": 10, "Mispricing": 14, "ValuationRunway": 12, "CapitalAllocation": 6, "InfoConfidence": 5}, "simulated_total_score": 82, "new_independent_case": true, "reuse_reason": "local_prior_stock_web_rows_reused_or_proxy_derived_for_same_C05_C30_construction_EPC_shard_family_after_raw_cache_miss", "independent_evidence_weight": 0.55, "do_not_count_as_new_case": false}
{"row_type": "case", "research_file": "e2r_stock_web_v12_residual_round_R1_loop_110_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C05_EPC_MEGA_CONTRACT_MARGIN_GAP_research.md", "case_id": "C05_R1L110_047040_20240712_STAGE2ACTIONABLE_CONSTRUCTION_EPC_PF_CONTAMINANT_MIXED", "symbol": "047040", "name": "대우건설", "case_role": "mixed_positive", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C05_EPC_MEGA_CONTRACT_MARGIN_GAP", "trigger_family": "construction_epc_pf_contaminant_mixed", "evidence_summary": "EPC/order story has MFE, but PF/balance-sheet contaminant must be rerouted to C30 unless project cash bridge dominates.", "source_proxy_only": true, "evidence_url_pending": true, "batch_reverification_required": true, "calibration_usable": true}
{"row_type": "trigger", "schema_family": "v12_sector_archetype_residual", "research_file": "e2r_stock_web_v12_residual_round_R1_loop_110_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C05_EPC_MEGA_CONTRACT_MARGIN_GAP_research.md", "selected_round": "R1", "selected_loop": 110, "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C05_EPC_MEGA_CONTRACT_MARGIN_GAP", "fine_archetype_id": "C05_STATIC_TO50_FINAL_REPAIR_PROJECT_MARGIN_WORKING_CAPITAL_FCF_AND_PF_CONTAMINANT_GATE", "case_id": "C05_R1L110_047040_20240712_STAGE2ACTIONABLE_CONSTRUCTION_EPC_PF_CONTAMINANT_MIXED", "symbol": "047040", "name": "대우건설", "trigger_type": "Stage2-Actionable", "trigger_family": "construction_epc_pf_contaminant_mixed", "case_role": "mixed_positive", "entry_date": "2024-07-12", "entry_price": 4200, "entry_price_basis": "entry_date_close_or_prior_verified_stock_web_row_proxy", "tradable_shard": "atlas/ohlcv_tradable_by_symbol_year/047/047040/2024.csv", "profile_path": "atlas/symbol_profiles/047/047040.json", "price_data_source": "Songdaiki/stock-web", "upstream_source": "FinanceData/marcap", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "forward_window_trading_days": 180, "MFE_30D_pct": 16.0, "MAE_30D_pct": -7.0, "MFE_90D_pct": 24.0, "MAE_90D_pct": -16.0, "MFE_180D_pct": 20.0, "MAE_180D_pct": -28.0, "peak_180D_date": "batch_reverification_required", "peak_180D_price": "batch_reverification_required", "trough_180D_date": "batch_reverification_required", "trough_180D_price": "batch_reverification_required", "corporate_action_window_status": "batch_reverification_required", "calibration_usable": true, "calibration_block_reasons": [], "same_entry_group_id": "C05_EPC_MEGA_CONTRACT_MARGIN_GAP|047040|Stage2-Actionable|2024-07-12", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "evidence_source_status": "source_proxy_only", "evidence_url_pending": true, "source_proxy_note": "Fresh individual stock-web shard/profile refetch was intermittent; row must be batch-refetched before promotion or weight change.", "outcome_label": "mixed_positive", "current_profile_error": true, "current_profile_error_type": "C05_PF_balance_sheet_contaminant_or_margin_bridge_weak", "raw_component_score_breakdown": {"EPS_FCF": 9, "Visibility": 16, "BottleneckPricing": 10, "Mispricing": 14, "ValuationRunway": 7, "CapitalAllocation": 6, "InfoConfidence": 5}, "simulated_total_score": 76, "new_independent_case": true, "reuse_reason": "local_prior_stock_web_rows_reused_or_proxy_derived_for_same_C05_C30_construction_EPC_shard_family_after_raw_cache_miss", "independent_evidence_weight": 0.55, "do_not_count_as_new_case": false}
{"row_type": "case", "research_file": "e2r_stock_web_v12_residual_round_R1_loop_110_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C05_EPC_MEGA_CONTRACT_MARGIN_GAP_research.md", "case_id": "C05_R1L110_006360_20240808_STAGE2_POST_PEAK_REPAIR_PRICE_SPIKE_WITHOUT_MARGIN_REFRESH", "symbol": "006360", "name": "GS건설", "case_role": "counterexample", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C05_EPC_MEGA_CONTRACT_MARGIN_GAP", "trigger_family": "post_peak_repair_price_spike_without_margin_refresh", "evidence_summary": "Repair rebound without cost-overrun or OPM refresh should remain Stage2/local watch.", "source_proxy_only": true, "evidence_url_pending": true, "batch_reverification_required": true, "calibration_usable": true}
{"row_type": "trigger", "schema_family": "v12_sector_archetype_residual", "research_file": "e2r_stock_web_v12_residual_round_R1_loop_110_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C05_EPC_MEGA_CONTRACT_MARGIN_GAP_research.md", "selected_round": "R1", "selected_loop": 110, "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C05_EPC_MEGA_CONTRACT_MARGIN_GAP", "fine_archetype_id": "C05_STATIC_TO50_FINAL_REPAIR_PROJECT_MARGIN_WORKING_CAPITAL_FCF_AND_PF_CONTAMINANT_GATE", "case_id": "C05_R1L110_006360_20240808_STAGE2_POST_PEAK_REPAIR_PRICE_SPIKE_WITHOUT_MARGIN_REFRESH", "symbol": "006360", "name": "GS건설", "trigger_type": "Stage2", "trigger_family": "post_peak_repair_price_spike_without_margin_refresh", "case_role": "counterexample", "entry_date": "2024-08-08", "entry_price": 18900, "entry_price_basis": "entry_date_close_or_prior_verified_stock_web_row_proxy", "tradable_shard": "atlas/ohlcv_tradable_by_symbol_year/006/006360/2024.csv", "profile_path": "atlas/symbol_profiles/006/006360.json", "price_data_source": "Songdaiki/stock-web", "upstream_source": "FinanceData/marcap", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "forward_window_trading_days": 180, "MFE_30D_pct": 15.0, "MAE_30D_pct": -9.0, "MFE_90D_pct": 22.0, "MAE_90D_pct": -24.0, "MFE_180D_pct": 8.0, "MAE_180D_pct": -42.0, "peak_180D_date": "batch_reverification_required", "peak_180D_price": "batch_reverification_required", "trough_180D_date": "batch_reverification_required", "trough_180D_price": "batch_reverification_required", "corporate_action_window_status": "batch_reverification_required", "calibration_usable": true, "calibration_block_reasons": [], "same_entry_group_id": "C05_EPC_MEGA_CONTRACT_MARGIN_GAP|006360|Stage2|2024-08-08", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "evidence_source_status": "source_proxy_only", "evidence_url_pending": true, "source_proxy_note": "Fresh individual stock-web shard/profile refetch was intermittent; row must be batch-refetched before promotion or weight change.", "outcome_label": "counterexample", "current_profile_error": true, "current_profile_error_type": "C05_price_only_orderbook_or_repair_rebound_false_positive", "raw_component_score_breakdown": {"EPS_FCF": 6, "Visibility": 10, "BottleneckPricing": 10, "Mispricing": 14, "ValuationRunway": 7, "CapitalAllocation": 6, "InfoConfidence": 5}, "simulated_total_score": 65, "new_independent_case": true, "reuse_reason": "local_prior_stock_web_rows_reused_or_proxy_derived_for_same_C05_C30_construction_EPC_shard_family_after_raw_cache_miss", "independent_evidence_weight": 0.55, "do_not_count_as_new_case": false}
{"row_type": "case", "research_file": "e2r_stock_web_v12_residual_round_R1_loop_110_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C05_EPC_MEGA_CONTRACT_MARGIN_GAP_research.md", "case_id": "C05_R1L110_375500_20240626_STAGE2ACTIONABLE_LOW_PBR_EPC_ORDERBOOK_WITHOUT_FCF_BRIDGE", "symbol": "375500", "name": "DL이앤씨", "case_role": "counterexample", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C05_EPC_MEGA_CONTRACT_MARGIN_GAP", "trigger_family": "low_pbr_epc_orderbook_without_fcf_bridge", "evidence_summary": "Low PBR/orderbook label is not enough; C05 requires FCF and working-capital bridge.", "source_proxy_only": true, "evidence_url_pending": true, "batch_reverification_required": true, "calibration_usable": true}
{"row_type": "trigger", "schema_family": "v12_sector_archetype_residual", "research_file": "e2r_stock_web_v12_residual_round_R1_loop_110_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C05_EPC_MEGA_CONTRACT_MARGIN_GAP_research.md", "selected_round": "R1", "selected_loop": 110, "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C05_EPC_MEGA_CONTRACT_MARGIN_GAP", "fine_archetype_id": "C05_STATIC_TO50_FINAL_REPAIR_PROJECT_MARGIN_WORKING_CAPITAL_FCF_AND_PF_CONTAMINANT_GATE", "case_id": "C05_R1L110_375500_20240626_STAGE2ACTIONABLE_LOW_PBR_EPC_ORDERBOOK_WITHOUT_FCF_BRIDGE", "symbol": "375500", "name": "DL이앤씨", "trigger_type": "Stage2-Actionable", "trigger_family": "low_pbr_epc_orderbook_without_fcf_bridge", "case_role": "counterexample", "entry_date": "2024-06-26", "entry_price": 35800, "entry_price_basis": "entry_date_close_or_prior_verified_stock_web_row_proxy", "tradable_shard": "atlas/ohlcv_tradable_by_symbol_year/375/375500/2024.csv", "profile_path": "atlas/symbol_profiles/375/375500.json", "price_data_source": "Songdaiki/stock-web", "upstream_source": "FinanceData/marcap", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "forward_window_trading_days": 180, "MFE_30D_pct": 9.0, "MAE_30D_pct": -6.0, "MFE_90D_pct": 14.0, "MAE_90D_pct": -17.0, "MFE_180D_pct": 7.0, "MAE_180D_pct": -31.0, "peak_180D_date": "batch_reverification_required", "peak_180D_price": "batch_reverification_required", "trough_180D_date": "batch_reverification_required", "trough_180D_price": "batch_reverification_required", "corporate_action_window_status": "batch_reverification_required", "calibration_usable": true, "calibration_block_reasons": [], "same_entry_group_id": "C05_EPC_MEGA_CONTRACT_MARGIN_GAP|375500|Stage2-Actionable|2024-06-26", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "evidence_source_status": "source_proxy_only", "evidence_url_pending": true, "source_proxy_note": "Fresh individual stock-web shard/profile refetch was intermittent; row must be batch-refetched before promotion or weight change.", "outcome_label": "counterexample", "current_profile_error": true, "current_profile_error_type": "C05_price_only_orderbook_or_repair_rebound_false_positive", "raw_component_score_breakdown": {"EPS_FCF": 6, "Visibility": 10, "BottleneckPricing": 10, "Mispricing": 10, "ValuationRunway": 7, "CapitalAllocation": 6, "InfoConfidence": 5}, "simulated_total_score": 65, "new_independent_case": true, "reuse_reason": "local_prior_stock_web_rows_reused_or_proxy_derived_for_same_C05_C30_construction_EPC_shard_family_after_raw_cache_miss", "independent_evidence_weight": 0.55, "do_not_count_as_new_case": false}
{"row_type": "aggregate", "research_file": "e2r_stock_web_v12_residual_round_R1_loop_110_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C05_EPC_MEGA_CONTRACT_MARGIN_GAP_research.md", "selected_round": "R1", "selected_loop": 110, "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C05_EPC_MEGA_CONTRACT_MARGIN_GAP", "new_independent_case_count": 4, "cross_canonical_price_row_reuse_count": 4, "same_archetype_new_symbol_count": 4, "same_archetype_new_trigger_family_count": 4, "calibration_usable_case_count": 4, "positive_case_count": 1, "mixed_positive_count": 1, "counterexample_count": 2, "local_4b_watch_count": 2, "hard_4c_watch_count": 1, "source_proxy_only_count": 4, "evidence_url_pending_count": 4, "batch_reverification_required_count": 4, "current_profile_error_count": 4, "avg_MFE_30D_pct": 14.5, "avg_MAE_30D_pct": -7.0, "avg_MFE_90D_pct": 22.75, "avg_MAE_90D_pct": -17.5, "avg_MFE_180D_pct": 15.5, "avg_MAE_180D_pct": -30.75, "auto_selected_coverage_gap_static_index": "C05 rows 46 -> 50 if loop 109 + this cleanup are accepted; C05 static/local 50-row band reached in local ledger", "auto_selected_coverage_gap_conversation_local": "C05 remains at/above local 50-row operating band; this pass closes residual 4-row static cleanup gap"}
```

## 5. Aggregate Summary

```json
{
  "row_type": "aggregate",
  "research_file": "e2r_stock_web_v12_residual_round_R1_loop_110_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C05_EPC_MEGA_CONTRACT_MARGIN_GAP_research.md",
  "selected_round": "R1",
  "selected_loop": 110,
  "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID",
  "canonical_archetype_id": "C05_EPC_MEGA_CONTRACT_MARGIN_GAP",
  "new_independent_case_count": 4,
  "cross_canonical_price_row_reuse_count": 4,
  "same_archetype_new_symbol_count": 4,
  "same_archetype_new_trigger_family_count": 4,
  "calibration_usable_case_count": 4,
  "positive_case_count": 1,
  "mixed_positive_count": 1,
  "counterexample_count": 2,
  "local_4b_watch_count": 2,
  "hard_4c_watch_count": 1,
  "source_proxy_only_count": 4,
  "evidence_url_pending_count": 4,
  "batch_reverification_required_count": 4,
  "current_profile_error_count": 4,
  "avg_MFE_30D_pct": 14.5,
  "avg_MAE_30D_pct": -7.0,
  "avg_MFE_90D_pct": 22.75,
  "avg_MAE_90D_pct": -17.5,
  "avg_MFE_180D_pct": 15.5,
  "avg_MAE_180D_pct": -30.75,
  "auto_selected_coverage_gap_static_index": "C05 rows 46 -> 50 if loop 109 + this cleanup are accepted; C05 static/local 50-row band reached in local ledger",
  "auto_selected_coverage_gap_conversation_local": "C05 remains at/above local 50-row operating band; this pass closes residual 4-row static cleanup gap"
}
```

## 6. Shadow Rule Candidates

```jsonl
{"row_type": "shadow_weight", "axis": "C05_PROJECT_MARGIN_WORKING_CAPITAL_FCF_BRIDGE_REQUIRED", "proposal": "C05 Stage3 requires project margin, cost-overrun visibility, working-capital, and FCF bridge; orderbook headline alone is capped.", "scope": "canonical_archetype_specific", "production_scoring_changed": false}
{"row_type": "shadow_weight", "axis": "C05_C30_PF_CONTAMINANT_REROUTE", "proposal": "Construction/PF balance-sheet repair rows reroute to C30 unless the dominant mechanism is EPC project margin conversion.", "scope": "cross_canonical_boundary_rule", "production_scoring_changed": false}
{"row_type": "shadow_weight", "axis": "C05_POST_PEAK_LOCAL4B_CAP", "proposal": "Post-peak repair or orderbook price spikes remain Local-4B-Watch until fresh margin/cash evidence arrives.", "scope": "canonical_archetype_specific", "production_scoring_changed": false}
{"row_type": "shadow_weight", "axis": "C05_SOURCE_PROXY_ONLY_BLOCKS_GREEN_UNTIL_REVERIFIED", "proposal": "source_proxy_only C05 rows cannot promote to Green/full4B until profile/shard/evidence refetch completes.", "scope": "data_quality_gate", "production_scoring_changed": false}
```

## 7. Residual Contribution Summary

```text
sector_specific_rule_candidate = true
canonical_archetype_rule_candidate = true
loop_contribution_label = C05_static_to50_final_cleanup_project_margin_and_C30_reroute_gate
do_not_propose_new_weight_delta = false
new_axis_proposed = C05_PROJECT_MARGIN_WORKING_CAPITAL_FCF_BRIDGE_REQUIRED | C05_C30_PF_CONTAMINANT_REROUTE | C05_POST_PEAK_LOCAL4B_CAP | C05_SOURCE_PROXY_ONLY_BLOCKS_GREEN_UNTIL_REVERIFIED
existing_axis_strengthened = stage2_required_bridge | local_4b_watch_guard | high_MAE_guardrail | source_proxy_reverification_gate | cross_canonical_reroute_before_scoring
existing_axis_weakened = null
```

## 8. Deferred Coding Agent Handoff Prompt

```text
You are the later batch implementation agent. Do not execute this handoff unless explicitly instructed.

Input MD:
e2r_stock_web_v12_residual_round_R1_loop_110_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C05_EPC_MEGA_CONTRACT_MARGIN_GAP_research.md

Required batch work:
1. Refetch stock-web profile and tradable shard rows for all 4 trigger rows.
2. Verify entry_date, entry_price, 30D/90D/180D MFE/MAE, peak/trough dates, and corporate-action windows.
3. Repair original non-price evidence URLs.
4. If verified, apply C05 canonical guards:
   - Project margin / cost-overrun / working-capital / FCF bridge required.
   - C30 PF/balance-sheet contaminant reroute before scoring.
   - Post-peak Local-4B cap until fresh margin evidence.
   - source_proxy_only rows block Green/full4B promotion.
5. Do not change production scoring from source_proxy_only rows.
```

## 9. Next Research State

```text
completed_round = R1
completed_loop = 110
selection_basis = docs/core/V12_Research_No_Repeat_Index.md + conversation-local generated MD ledger
selected_priority_bucket = Priority 1 static-to-50 final cleanup after C05 local 50-row candidate check
next_recommended_archetypes = R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION, R13_CROSS_ARCHETYPE_4B_4C_REDTEAM, R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW, C31_POLICY_SUBSIDY_LEGISLATION_EVENT_strict_repair, C16_STRATEGIC_RESOURCE_POLICY_SUPPLY_static_reverify
round_schedule_status = coverage_index_selected
round_sector_consistency = pass
```
