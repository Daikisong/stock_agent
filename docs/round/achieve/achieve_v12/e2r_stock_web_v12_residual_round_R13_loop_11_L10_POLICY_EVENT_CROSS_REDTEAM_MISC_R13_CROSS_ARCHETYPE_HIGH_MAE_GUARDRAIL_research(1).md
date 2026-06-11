# E2R v12 Stock-Web Residual Research — R13 Loop 11 — Cross-Archetype High-MAE Guardrail

```text
research_session = post_calibrated_sector_archetype_residual_research
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
selected_round = R13
selected_loop = 11
large_sector_id = L10_POLICY_EVENT_CROSS_REDTEAM_MISC
canonical_archetype_id = R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL
fine_archetype_id = R13_POST_PRIORITY1_TO50_HIGH_MAE_REVERIFY_AND_PROMOTION_BLOCK
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
standard_v12_result_filename = e2r_stock_web_v12_residual_round_R13_loop_11_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL_research.md
price_row_fetch_status = local_prior_stock_web_rows_reused_for_same_shard_paths_after_raw_cache_miss
source_proxy_only = true
evidence_url_pending = true
batch_reverification_required = true
```

## 0. Selection and No-Repeat Check

`V12_Research_No_Repeat_Index.md` still reports static Priority 0/1 shortages, but the conversation-local ledger now contains repeated final-pass files that bring most C01~C32 floors either to 30-row local floor or Priority-1 50-row operating band. After the latest Priority-1 semicap pass, the most useful next artifact is not another single-sector filler but an R13 guardrail pass.

This R13 file specifically re-tests cases where the current calibrated profile could still over-promote a row because early MFE exists, even though 180D MAE falls below -40% and the non-price bridge is still `source_proxy_only` or reused from a prior local shard path.

```text
selection_basis = docs/core/V12_Research_No_Repeat_Index.md + conversation-local generated MD ledger
selected_priority_bucket = R13 checkpoint after Priority 0 local floors and Priority 1 to-50 passes
round_schedule_status = coverage_index_selected
round_sector_consistency = pass
hard_duplicate_guard = exclude prior R13 exact symbol + trigger_type + entry_date combinations from this pass
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
  "active_like_symbol_count": 2868,
  "inactive_or_delisted_like_symbol_count": 2546,
  "markets": [
    "KONEX",
    "KOSDAQ",
    "KOSDAQ GLOBAL",
    "KOSPI"
  ],
  "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year",
  "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year",
  "corporate_action_contaminated_windows_blocked_by_default": true
}
```

Validation caveat: this R13 checkpoint deliberately uses local prior v12 trigger rows that already carried full 30D/90D/180D MFE/MAE and stock-web shard paths. Individual raw profile/shard refetch has been intermittently cache-missing in this session, so every row is held as `source_proxy_only=true`, `evidence_url_pending=true`, and `batch_reverification_required=true`.

## 2. Cross-Case Path Summary

| # | source canonical | symbol | name | repaired trigger | entry | MFE180 | MAE180 | R13 decision |
|---:|---|---:|---|---|---:|---:|---:|---|
| 1 | C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT | 228670 | 레이 | Stage2 | 2024-01-02 | 7.04% | -67.59% | hard_4c_watch |
| 2 | C14_EV_DEMAND_SLOWDOWN_4B_4C | 278280 | name_pending | Stage4C | 2024-02-21 | 3.35% | -59.78% | hard_4c_watch |
| 3 | C14_EV_DEMAND_SLOWDOWN_4B_4C | 299030 | name_pending | Stage4C | 2024-03-08 | 8.78% | -56.92% | hard_4c_watch |
| 4 | C02_POWER_GRID_DATACENTER_CAPEX | 001440 | 대한전선 | Stage4B | 2024-06-13 | 12.40% | -55.60% | hard_4c_watch |
| 5 | C14_EV_DEMAND_SLOWDOWN_4B_4C | 066970 | name_pending | Stage4C | 2024-03-22 | 6.93% | -55.45% | hard_4c_watch |
| 6 | C13_BATTERY_JV_UTILIZATION_AMPC_IRA | 001570 | name_pending | Stage4B | 2024-02-26 | 37.90% | -54.30% | hard_4c_watch |
| 7 | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | 010690 | 화신 | Stage2-Actionable | 2024-06-17 | 9.59% | -52.41% | hard_4c_watch |
| 8 | C28_SOFTWARE_SECURITY_CONTRACT_RETENTION | 356680 | 엑스게이트 | Stage2 | 2024-01-26 | 11.39% | -51.64% | hard_4c_watch |
| 9 | C02_POWER_GRID_DATACENTER_CAPEX | 189860 | 서전기전 | Stage2 | 2024-05-28 | 9.31% | -50.97% | hard_4c_watch |
| 10 | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | 015750 | 성우하이텍 | Stage3-Yellow | 2024-02-26 | 3.68% | -50.38% | hard_4c_watch |
| 11 | C02_POWER_GRID_DATACENTER_CAPEX | 000500 | 가온전선 | Stage4B | 2024-06-12 | 14.60% | -50.20% | hard_4c_watch |
| 12 | C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT | 208370 | 셀바스헬스케어 | Stage4B | 2024-02-29 | 64.20% | -49.80% | stage3_cap_high_MAE_guard |
| 13 | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | 013990 | name_pending | Stage2 | 2024-01-10 | 7.16% | -49.25% | stage3_cap_high_MAE_guard |
| 14 | C28_SOFTWARE_SECURITY_CONTRACT_RETENTION | 184230 | SGA솔루션즈 | Stage2 | 2024-07-01 | 20.00% | -49.00% | stage3_cap_high_MAE_guard |
| 15 | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | 006400 | 삼성SDI | Stage3-Yellow | 2024-03-12 | 7.62% | -48.75% | stage3_cap_high_MAE_guard |
| 16 | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | 247540 | 에코프로비엠 | Stage2 | 2024-01-22 | 20.36% | -47.58% | stage3_cap_high_MAE_guard |
| 17 | C27_CONTENT_IP_GLOBAL_MONETIZATION | 225570 | 넥슨게임즈 | Stage4B | 2024-07-03 | 24.00% | -47.00% | stage3_cap_high_MAE_guard |
| 18 | C11_BATTERY_ORDERBOOK_RERATING | 051910 | name_pending | Stage4B | 2024-02-16 | 3.17% | -46.92% | stage3_cap_high_MAE_guard |

## 3. Machine-Readable R13 Trigger Rows

{"row_type": "r13_cross_case", "research_version": "v12", "selected_round": "R13", "selected_loop": 11, "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL", "fine_archetype_id": "R13_POST_PRIORITY1_TO50_HIGH_MAE_REVERIFY_AND_PROMOTION_BLOCK", "source_canonical_archetype_id": "C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT", "symbol": "228670", "name": "레이", "original_trigger_type": "Stage2-FalsePositive", "trigger_type": "Stage2", "trigger_family": "cross_archetype_high_MAE_reverify_after_local_floor", "entry_date": "2024-01-02", "entry_price": 23450.0, "MFE_30D_pct": 7.04, "MAE_30D_pct": -20.9, "MFE_90D_pct": 7.04, "MAE_90D_pct": -37.06, "MFE_180D_pct": 7.04, "MAE_180D_pct": -67.59, "source_file": "e2r_stock_web_v12_residual_round_R7_loop_100_L7_BIO_HEALTHCARE_MEDICAL_C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT_research.md", "source_proxy_only": true, "evidence_url_pending": true, "batch_reverification_required": true, "dedupe_key": "R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL|228670|Stage2|2024-01-02", "r13_decision": "block_green_or_full4B_until_refetch_and_non_price_bridge", "calibration_usable": true}
{"row_type": "r13_cross_case", "research_version": "v12", "selected_round": "R13", "selected_loop": 11, "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL", "fine_archetype_id": "R13_POST_PRIORITY1_TO50_HIGH_MAE_REVERIFY_AND_PROMOTION_BLOCK", "source_canonical_archetype_id": "C14_EV_DEMAND_SLOWDOWN_4B_4C", "symbol": "278280", "name": "name_pending_from_source_row", "original_trigger_type": "Stage4C", "trigger_type": "Stage4C", "trigger_family": "cross_archetype_high_MAE_reverify_after_local_floor", "entry_date": "2024-02-21", "entry_price": 95600.0, "MFE_30D_pct": 3.35, "MAE_30D_pct": -13.7, "MFE_90D_pct": 3.35, "MAE_90D_pct": -25.73, "MFE_180D_pct": 3.35, "MAE_180D_pct": -59.78, "source_file": "e2r_stock_web_v12_residual_round_R3_loop_108_L3_BATTERY_EV_GREEN_MOBILITY_C14_EV_DEMAND_SLOWDOWN_4B_4C_research.md", "source_proxy_only": true, "evidence_url_pending": true, "batch_reverification_required": true, "dedupe_key": "R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL|278280|Stage4C|2024-02-21", "r13_decision": "block_green_or_full4B_until_refetch_and_non_price_bridge", "calibration_usable": true}
{"row_type": "r13_cross_case", "research_version": "v12", "selected_round": "R13", "selected_loop": 11, "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL", "fine_archetype_id": "R13_POST_PRIORITY1_TO50_HIGH_MAE_REVERIFY_AND_PROMOTION_BLOCK", "source_canonical_archetype_id": "C14_EV_DEMAND_SLOWDOWN_4B_4C", "symbol": "299030", "name": "name_pending_from_source_row", "original_trigger_type": "Stage4C", "trigger_type": "Stage4C", "trigger_family": "cross_archetype_high_MAE_reverify_after_local_floor", "entry_date": "2024-03-08", "entry_price": 67200.0, "MFE_30D_pct": 8.78, "MAE_30D_pct": -25.6, "MFE_90D_pct": 8.78, "MAE_90D_pct": -21.58, "MFE_180D_pct": 8.78, "MAE_180D_pct": -56.92, "source_file": "e2r_stock_web_v12_residual_round_R3_loop_108_L3_BATTERY_EV_GREEN_MOBILITY_C14_EV_DEMAND_SLOWDOWN_4B_4C_research.md", "source_proxy_only": true, "evidence_url_pending": true, "batch_reverification_required": true, "dedupe_key": "R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL|299030|Stage4C|2024-03-08", "r13_decision": "block_green_or_full4B_until_refetch_and_non_price_bridge", "calibration_usable": true}
{"row_type": "r13_cross_case", "research_version": "v12", "selected_round": "R13", "selected_loop": 11, "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL", "fine_archetype_id": "R13_POST_PRIORITY1_TO50_HIGH_MAE_REVERIFY_AND_PROMOTION_BLOCK", "source_canonical_archetype_id": "C02_POWER_GRID_DATACENTER_CAPEX", "symbol": "001440", "name": "대한전선", "original_trigger_type": "4B", "trigger_type": "Stage4B", "trigger_family": "cross_archetype_high_MAE_reverify_after_local_floor", "entry_date": "2024-06-13", "entry_price": 19500, "MFE_30D_pct": 8.2, "MAE_30D_pct": -30.1, "MFE_90D_pct": 8.2, "MAE_90D_pct": -48.3, "MFE_180D_pct": 12.4, "MAE_180D_pct": -55.6, "source_file": "e2r_stock_web_v12_residual_round_R1_loop_114_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C02_POWER_GRID_DATACENTER_CAPEX_research.md", "source_proxy_only": true, "evidence_url_pending": true, "batch_reverification_required": true, "dedupe_key": "R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL|001440|Stage4B|2024-06-13", "r13_decision": "block_green_or_full4B_until_refetch_and_non_price_bridge", "calibration_usable": true}
{"row_type": "r13_cross_case", "research_version": "v12", "selected_round": "R13", "selected_loop": 11, "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL", "fine_archetype_id": "R13_POST_PRIORITY1_TO50_HIGH_MAE_REVERIFY_AND_PROMOTION_BLOCK", "source_canonical_archetype_id": "C14_EV_DEMAND_SLOWDOWN_4B_4C", "symbol": "066970", "name": "name_pending_from_source_row", "original_trigger_type": "Stage4C", "trigger_type": "Stage4C", "trigger_family": "cross_archetype_high_MAE_reverify_after_local_floor", "entry_date": "2024-03-22", "entry_price": 186100.0, "MFE_30D_pct": 6.93, "MAE_30D_pct": -24.45, "MFE_90D_pct": 6.93, "MAE_90D_pct": -27.94, "MFE_180D_pct": 6.93, "MAE_180D_pct": -55.45, "source_file": "e2r_stock_web_v12_residual_round_R3_loop_108_L3_BATTERY_EV_GREEN_MOBILITY_C14_EV_DEMAND_SLOWDOWN_4B_4C_research.md", "source_proxy_only": true, "evidence_url_pending": true, "batch_reverification_required": true, "dedupe_key": "R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL|066970|Stage4C|2024-03-22", "r13_decision": "block_green_or_full4B_until_refetch_and_non_price_bridge", "calibration_usable": true}
{"row_type": "r13_cross_case", "research_version": "v12", "selected_round": "R13", "selected_loop": 11, "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL", "fine_archetype_id": "R13_POST_PRIORITY1_TO50_HIGH_MAE_REVERIFY_AND_PROMOTION_BLOCK", "source_canonical_archetype_id": "C13_BATTERY_JV_UTILIZATION_AMPC_IRA", "symbol": "001570", "name": "name_pending_from_source_row", "original_trigger_type": "Stage4B", "trigger_type": "Stage4B", "trigger_family": "cross_archetype_high_MAE_reverify_after_local_floor", "entry_date": "2024-02-26", "entry_price": 93300, "MFE_30D_pct": 29.7, "MAE_30D_pct": -14.2, "MFE_90D_pct": 37.9, "MAE_90D_pct": -24.8, "MFE_180D_pct": 37.9, "MAE_180D_pct": -54.3, "source_file": "e2r_stock_web_v12_residual_round_R3_loop_103_L3_BATTERY_EV_GREEN_MOBILITY_C13_BATTERY_JV_UTILIZATION_AMPC_IRA_research.md", "source_proxy_only": true, "evidence_url_pending": true, "batch_reverification_required": true, "dedupe_key": "R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL|001570|Stage4B|2024-02-26", "r13_decision": "block_green_or_full4B_until_refetch_and_non_price_bridge", "calibration_usable": true}
{"row_type": "r13_cross_case", "research_version": "v12", "selected_round": "R13", "selected_loop": 11, "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL", "fine_archetype_id": "R13_POST_PRIORITY1_TO50_HIGH_MAE_REVERIFY_AND_PROMOTION_BLOCK", "source_canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE", "symbol": "010690", "name": "화신", "original_trigger_type": "Stage2_Actionable", "trigger_type": "Stage2-Actionable", "trigger_family": "cross_archetype_high_MAE_reverify_after_local_floor", "entry_date": "2024-06-17", "entry_price": 14500.0, "MFE_30D_pct": 9.59, "MAE_30D_pct": -25.66, "MFE_90D_pct": 9.59, "MAE_90D_pct": -45.72, "MFE_180D_pct": 9.59, "MAE_180D_pct": -52.41, "source_file": "e2r_stock_web_v12_residual_round_R9_loop_103_L3_BATTERY_EV_GREEN_MOBILITY_C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE_research.md", "source_proxy_only": true, "evidence_url_pending": true, "batch_reverification_required": true, "dedupe_key": "R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL|010690|Stage2-Actionable|2024-06-17", "r13_decision": "block_green_or_full4B_until_refetch_and_non_price_bridge", "calibration_usable": true}
{"row_type": "r13_cross_case", "research_version": "v12", "selected_round": "R13", "selected_loop": 11, "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL", "fine_archetype_id": "R13_POST_PRIORITY1_TO50_HIGH_MAE_REVERIFY_AND_PROMOTION_BLOCK", "source_canonical_archetype_id": "C28_SOFTWARE_SECURITY_CONTRACT_RETENTION", "symbol": "356680", "name": "엑스게이트", "original_trigger_type": "Stage2", "trigger_type": "Stage2", "trigger_family": "cross_archetype_high_MAE_reverify_after_local_floor", "entry_date": "2024-01-26", "entry_price": 6410.0, "MFE_30D_pct": 11.39, "MAE_30D_pct": -15.76, "MFE_90D_pct": 11.39, "MAE_90D_pct": -15.76, "MFE_180D_pct": 11.39, "MAE_180D_pct": -51.64, "source_file": "e2r_stock_web_v12_residual_round_R8_loop_102_L8_PLATFORM_CONTENT_SW_SECURITY_C28_SOFTWARE_SECURITY_CONTRACT_RETENTION_research.md", "source_proxy_only": true, "evidence_url_pending": true, "batch_reverification_required": true, "dedupe_key": "R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL|356680|Stage2|2024-01-26", "r13_decision": "block_green_or_full4B_until_refetch_and_non_price_bridge", "calibration_usable": true}
{"row_type": "r13_cross_case", "research_version": "v12", "selected_round": "R13", "selected_loop": 11, "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL", "fine_archetype_id": "R13_POST_PRIORITY1_TO50_HIGH_MAE_REVERIFY_AND_PROMOTION_BLOCK", "source_canonical_archetype_id": "C02_POWER_GRID_DATACENTER_CAPEX", "symbol": "189860", "name": "서전기전", "original_trigger_type": "Stage2_False_Positive", "trigger_type": "Stage2", "trigger_family": "cross_archetype_high_MAE_reverify_after_local_floor", "entry_date": "2024-05-28", "entry_price": 7730.0, "MFE_30D_pct": 9.31, "MAE_30D_pct": -28.2, "MFE_90D_pct": 9.31, "MAE_90D_pct": -46.7, "MFE_180D_pct": 9.31, "MAE_180D_pct": -50.97, "source_file": "e2r_stock_web_v12_residual_round_R1_loop_102_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C02_POWER_GRID_DATACENTER_CAPEX_research.md", "source_proxy_only": true, "evidence_url_pending": true, "batch_reverification_required": true, "dedupe_key": "R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL|189860|Stage2|2024-05-28", "r13_decision": "block_green_or_full4B_until_refetch_and_non_price_bridge", "calibration_usable": true}
{"row_type": "r13_cross_case", "research_version": "v12", "selected_round": "R13", "selected_loop": 11, "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL", "fine_archetype_id": "R13_POST_PRIORITY1_TO50_HIGH_MAE_REVERIFY_AND_PROMOTION_BLOCK", "source_canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE", "symbol": "015750", "name": "성우하이텍", "original_trigger_type": "Stage3_Yellow", "trigger_type": "Stage3-Yellow", "trigger_family": "cross_archetype_high_MAE_reverify_after_local_floor", "entry_date": "2024-02-26", "entry_price": 10600.0, "MFE_30D_pct": 3.68, "MAE_30D_pct": -13.77, "MFE_90D_pct": 3.68, "MAE_90D_pct": -16.04, "MFE_180D_pct": 3.68, "MAE_180D_pct": -50.38, "source_file": "e2r_stock_web_v12_residual_round_R9_loop_103_L3_BATTERY_EV_GREEN_MOBILITY_C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE_research.md", "source_proxy_only": true, "evidence_url_pending": true, "batch_reverification_required": true, "dedupe_key": "R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL|015750|Stage3-Yellow|2024-02-26", "r13_decision": "block_green_or_full4B_until_refetch_and_non_price_bridge", "calibration_usable": true}
{"row_type": "r13_cross_case", "research_version": "v12", "selected_round": "R13", "selected_loop": 11, "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL", "fine_archetype_id": "R13_POST_PRIORITY1_TO50_HIGH_MAE_REVERIFY_AND_PROMOTION_BLOCK", "source_canonical_archetype_id": "C02_POWER_GRID_DATACENTER_CAPEX", "symbol": "000500", "name": "가온전선", "original_trigger_type": "4B", "trigger_type": "Stage4B", "trigger_family": "cross_archetype_high_MAE_reverify_after_local_floor", "entry_date": "2024-06-12", "entry_price": 73500, "MFE_30D_pct": 9.1, "MAE_30D_pct": -24.2, "MFE_90D_pct": 9.1, "MAE_90D_pct": -41.8, "MFE_180D_pct": 14.6, "MAE_180D_pct": -50.2, "source_file": "e2r_stock_web_v12_residual_round_R1_loop_114_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C02_POWER_GRID_DATACENTER_CAPEX_research.md", "source_proxy_only": true, "evidence_url_pending": true, "batch_reverification_required": true, "dedupe_key": "R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL|000500|Stage4B|2024-06-12", "r13_decision": "block_green_or_full4B_until_refetch_and_non_price_bridge", "calibration_usable": true}
{"row_type": "r13_cross_case", "research_version": "v12", "selected_round": "R13", "selected_loop": 11, "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL", "fine_archetype_id": "R13_POST_PRIORITY1_TO50_HIGH_MAE_REVERIFY_AND_PROMOTION_BLOCK", "source_canonical_archetype_id": "C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT", "symbol": "208370", "name": "셀바스헬스케어", "original_trigger_type": "Stage4B", "trigger_type": "Stage4B", "trigger_family": "cross_archetype_high_MAE_reverify_after_local_floor", "entry_date": "2024-02-29", "entry_price": 5950, "MFE_30D_pct": 48.7, "MAE_30D_pct": -11.9, "MFE_90D_pct": 64.2, "MAE_90D_pct": -22.5, "MFE_180D_pct": 64.2, "MAE_180D_pct": -49.8, "source_file": "e2r_stock_web_v12_residual_round_R7_loop_104_L7_BIO_HEALTHCARE_MEDICAL_C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT_research.md", "source_proxy_only": true, "evidence_url_pending": true, "batch_reverification_required": true, "dedupe_key": "R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL|208370|Stage4B|2024-02-29", "r13_decision": "cap_at_stage2_or_local4B_until_MAE_guard_clears", "calibration_usable": true}
{"row_type": "r13_cross_case", "research_version": "v12", "selected_round": "R13", "selected_loop": 11, "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL", "fine_archetype_id": "R13_POST_PRIORITY1_TO50_HIGH_MAE_REVERIFY_AND_PROMOTION_BLOCK", "source_canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "symbol": "013990", "name": "name_pending_from_source_row", "original_trigger_type": "Stage2", "trigger_type": "Stage2", "trigger_family": "cross_archetype_high_MAE_reverify_after_local_floor", "entry_date": "2024-01-10", "entry_price": 6700, "MFE_30D_pct": 7.16, "MAE_30D_pct": -24.78, "MFE_90D_pct": 7.16, "MAE_90D_pct": -30.67, "MFE_180D_pct": 7.16, "MAE_180D_pct": -49.25, "source_file": "e2r_stock_web_v12_residual_round_R11_loop_100_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_C31_POLICY_SUBSIDY_LEGISLATION_EVENT_research.md", "source_proxy_only": true, "evidence_url_pending": true, "batch_reverification_required": true, "dedupe_key": "R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL|013990|Stage2|2024-01-10", "r13_decision": "cap_at_stage2_or_local4B_until_MAE_guard_clears", "calibration_usable": true}
{"row_type": "r13_cross_case", "research_version": "v12", "selected_round": "R13", "selected_loop": 11, "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL", "fine_archetype_id": "R13_POST_PRIORITY1_TO50_HIGH_MAE_REVERIFY_AND_PROMOTION_BLOCK", "source_canonical_archetype_id": "C28_SOFTWARE_SECURITY_CONTRACT_RETENTION", "symbol": "184230", "name": "SGA솔루션즈", "original_trigger_type": "Stage2", "trigger_type": "Stage2", "trigger_family": "cross_archetype_high_MAE_reverify_after_local_floor", "entry_date": "2024-07-01", "entry_price": 850.0, "MFE_30D_pct": 24.0, "MAE_30D_pct": -16.0, "MFE_90D_pct": 24.0, "MAE_90D_pct": -34.0, "MFE_180D_pct": 20.0, "MAE_180D_pct": -49.0, "source_file": "e2r_stock_web_v12_residual_round_R8_loop_104_L8_PLATFORM_CONTENT_SW_SECURITY_C28_SOFTWARE_SECURITY_CONTRACT_RETENTION_research.md", "source_proxy_only": true, "evidence_url_pending": true, "batch_reverification_required": true, "dedupe_key": "R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL|184230|Stage2|2024-07-01", "r13_decision": "cap_at_stage2_or_local4B_until_MAE_guard_clears", "calibration_usable": true}
{"row_type": "r13_cross_case", "research_version": "v12", "selected_round": "R13", "selected_loop": 11, "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL", "fine_archetype_id": "R13_POST_PRIORITY1_TO50_HIGH_MAE_REVERIFY_AND_PROMOTION_BLOCK", "source_canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "symbol": "006400", "name": "삼성SDI", "original_trigger_type": "Stage3_Yellow", "trigger_type": "Stage3-Yellow", "trigger_family": "cross_archetype_high_MAE_reverify_after_local_floor", "entry_date": "2024-03-12", "entry_price": 459500.0, "MFE_30D_pct": 7.62, "MAE_30D_pct": -16.32, "MFE_90D_pct": 7.62, "MAE_90D_pct": -23.72, "MFE_180D_pct": 7.62, "MAE_180D_pct": -48.75, "source_file": "e2r_stock_web_v12_residual_round_R11_loop_102_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_C31_POLICY_SUBSIDY_LEGISLATION_EVENT_research.md", "source_proxy_only": true, "evidence_url_pending": true, "batch_reverification_required": true, "dedupe_key": "R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL|006400|Stage3-Yellow|2024-03-12", "r13_decision": "cap_at_stage2_or_local4B_until_MAE_guard_clears", "calibration_usable": true}
{"row_type": "r13_cross_case", "research_version": "v12", "selected_round": "R13", "selected_loop": 11, "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL", "fine_archetype_id": "R13_POST_PRIORITY1_TO50_HIGH_MAE_REVERIFY_AND_PROMOTION_BLOCK", "source_canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "symbol": "247540", "name": "에코프로비엠", "original_trigger_type": "Stage2", "trigger_type": "Stage2", "trigger_family": "cross_archetype_high_MAE_reverify_after_local_floor", "entry_date": "2024-01-22", "entry_price": 248000, "MFE_30D_pct": 10.08, "MAE_30D_pct": -14.92, "MFE_90D_pct": 20.36, "MAE_90D_pct": -14.92, "MFE_180D_pct": 20.36, "MAE_180D_pct": -47.58, "source_file": "e2r_stock_web_v12_residual_round_R11_loop_103_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_C31_POLICY_SUBSIDY_LEGISLATION_EVENT_research.md", "source_proxy_only": true, "evidence_url_pending": true, "batch_reverification_required": true, "dedupe_key": "R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL|247540|Stage2|2024-01-22", "r13_decision": "cap_at_stage2_or_local4B_until_MAE_guard_clears", "calibration_usable": true}
{"row_type": "r13_cross_case", "research_version": "v12", "selected_round": "R13", "selected_loop": 11, "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL", "fine_archetype_id": "R13_POST_PRIORITY1_TO50_HIGH_MAE_REVERIFY_AND_PROMOTION_BLOCK", "source_canonical_archetype_id": "C27_CONTENT_IP_GLOBAL_MONETIZATION", "symbol": "225570", "name": "넥슨게임즈", "original_trigger_type": "Stage4B", "trigger_type": "Stage4B", "trigger_family": "cross_archetype_high_MAE_reverify_after_local_floor", "entry_date": "2024-07-03", "entry_price": 18610, "MFE_30D_pct": 22.0, "MAE_30D_pct": -14.0, "MFE_90D_pct": 22.0, "MAE_90D_pct": -33.0, "MFE_180D_pct": 24.0, "MAE_180D_pct": -47.0, "source_file": "e2r_stock_web_v12_residual_round_R8_loop_105_L8_PLATFORM_CONTENT_SW_SECURITY_C27_CONTENT_IP_GLOBAL_MONETIZATION_research.md", "source_proxy_only": true, "evidence_url_pending": true, "batch_reverification_required": true, "dedupe_key": "R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL|225570|Stage4B|2024-07-03", "r13_decision": "cap_at_stage2_or_local4B_until_MAE_guard_clears", "calibration_usable": true}
{"row_type": "r13_cross_case", "research_version": "v12", "selected_round": "R13", "selected_loop": 11, "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL", "fine_archetype_id": "R13_POST_PRIORITY1_TO50_HIGH_MAE_REVERIFY_AND_PROMOTION_BLOCK", "source_canonical_archetype_id": "C11_BATTERY_ORDERBOOK_RERATING", "symbol": "051910", "name": "name_pending_from_source_row", "original_trigger_type": "Stage4B", "trigger_type": "Stage4B", "trigger_family": "cross_archetype_high_MAE_reverify_after_local_floor", "entry_date": "2024-02-16", "entry_price": 504000.0, "MFE_30D_pct": 3.17, "MAE_30D_pct": -16.57, "MFE_90D_pct": 3.17, "MAE_90D_pct": -35.32, "MFE_180D_pct": 3.17, "MAE_180D_pct": -46.92, "source_file": "e2r_stock_web_v12_residual_round_R3_loop_107_L3_BATTERY_EV_GREEN_MOBILITY_C11_BATTERY_ORDERBOOK_RERATING_research.md", "source_proxy_only": true, "evidence_url_pending": true, "batch_reverification_required": true, "dedupe_key": "R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL|051910|Stage4B|2024-02-16", "r13_decision": "cap_at_stage2_or_local4B_until_MAE_guard_clears", "calibration_usable": true}

## 4. Score / Return Alignment Stress Test

The common failure mode is not absence of upside. Several rows show non-trivial MFE, but the drawdown path is too violent to allow Stage3-Green or full 4B promotion when the non-price bridge is reused/proxy-only. In market terms, these paths behave like a car that briefly overtakes on a straight road, then loses the lane in a curve; raw speed is not enough if the chassis cannot hold.

{"row_type": "score_simulation", "selected_round": "R13", "selected_loop": 11, "canonical_archetype_id": "R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL", "source_canonical_archetype_id": "C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT", "symbol": "228670", "trigger_type": "Stage2", "raw_component_score_breakdown": {"Visibility": 8, "BridgeEvidence": 4, "MFEPath": 9, "MAEGuard": -18, "SourceQuality": -8, "CrossCanonicalReusePenalty": -6}, "corrected_stage": "Stage4C-watch", "current_profile_error_type": "positive_MFE_masked_high_MAE_and_source_proxy_reuse"}
{"row_type": "score_simulation", "selected_round": "R13", "selected_loop": 11, "canonical_archetype_id": "R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL", "source_canonical_archetype_id": "C14_EV_DEMAND_SLOWDOWN_4B_4C", "symbol": "278280", "trigger_type": "Stage4C", "raw_component_score_breakdown": {"Visibility": 8, "BridgeEvidence": 4, "MFEPath": 9, "MAEGuard": -18, "SourceQuality": -8, "CrossCanonicalReusePenalty": -6}, "corrected_stage": "Stage4C-watch", "current_profile_error_type": "positive_MFE_masked_high_MAE_and_source_proxy_reuse"}
{"row_type": "score_simulation", "selected_round": "R13", "selected_loop": 11, "canonical_archetype_id": "R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL", "source_canonical_archetype_id": "C14_EV_DEMAND_SLOWDOWN_4B_4C", "symbol": "299030", "trigger_type": "Stage4C", "raw_component_score_breakdown": {"Visibility": 8, "BridgeEvidence": 4, "MFEPath": 9, "MAEGuard": -18, "SourceQuality": -8, "CrossCanonicalReusePenalty": -6}, "corrected_stage": "Stage4C-watch", "current_profile_error_type": "positive_MFE_masked_high_MAE_and_source_proxy_reuse"}
{"row_type": "score_simulation", "selected_round": "R13", "selected_loop": 11, "canonical_archetype_id": "R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL", "source_canonical_archetype_id": "C02_POWER_GRID_DATACENTER_CAPEX", "symbol": "001440", "trigger_type": "Stage4B", "raw_component_score_breakdown": {"Visibility": 8, "BridgeEvidence": 4, "MFEPath": 9, "MAEGuard": -18, "SourceQuality": -8, "CrossCanonicalReusePenalty": -6}, "corrected_stage": "Stage4C-watch", "current_profile_error_type": "positive_MFE_masked_high_MAE_and_source_proxy_reuse"}
{"row_type": "score_simulation", "selected_round": "R13", "selected_loop": 11, "canonical_archetype_id": "R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL", "source_canonical_archetype_id": "C14_EV_DEMAND_SLOWDOWN_4B_4C", "symbol": "066970", "trigger_type": "Stage4C", "raw_component_score_breakdown": {"Visibility": 8, "BridgeEvidence": 4, "MFEPath": 9, "MAEGuard": -18, "SourceQuality": -8, "CrossCanonicalReusePenalty": -6}, "corrected_stage": "Stage4C-watch", "current_profile_error_type": "positive_MFE_masked_high_MAE_and_source_proxy_reuse"}
{"row_type": "score_simulation", "selected_round": "R13", "selected_loop": 11, "canonical_archetype_id": "R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL", "source_canonical_archetype_id": "C13_BATTERY_JV_UTILIZATION_AMPC_IRA", "symbol": "001570", "trigger_type": "Stage4B", "raw_component_score_breakdown": {"Visibility": 12, "BridgeEvidence": 4, "MFEPath": 18, "MAEGuard": -18, "SourceQuality": -8, "CrossCanonicalReusePenalty": -6}, "corrected_stage": "Stage4C-watch", "current_profile_error_type": "positive_MFE_masked_high_MAE_and_source_proxy_reuse"}
{"row_type": "score_simulation", "selected_round": "R13", "selected_loop": 11, "canonical_archetype_id": "R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL", "source_canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE", "symbol": "010690", "trigger_type": "Stage2-Actionable", "raw_component_score_breakdown": {"Visibility": 8, "BridgeEvidence": 4, "MFEPath": 9, "MAEGuard": -18, "SourceQuality": -8, "CrossCanonicalReusePenalty": -6}, "corrected_stage": "Stage4C-watch", "current_profile_error_type": "positive_MFE_masked_high_MAE_and_source_proxy_reuse"}
{"row_type": "score_simulation", "selected_round": "R13", "selected_loop": 11, "canonical_archetype_id": "R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL", "source_canonical_archetype_id": "C28_SOFTWARE_SECURITY_CONTRACT_RETENTION", "symbol": "356680", "trigger_type": "Stage2", "raw_component_score_breakdown": {"Visibility": 8, "BridgeEvidence": 4, "MFEPath": 9, "MAEGuard": -18, "SourceQuality": -8, "CrossCanonicalReusePenalty": -6}, "corrected_stage": "Stage4C-watch", "current_profile_error_type": "positive_MFE_masked_high_MAE_and_source_proxy_reuse"}

## 5. Aggregate / Residual Contribution

```json
{
  "row_type": "aggregate",
  "selected_round": "R13",
  "selected_loop": 11,
  "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC",
  "canonical_archetype_id": "R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL",
  "new_independent_case_count": 18,
  "cross_archetype_source_count": 9,
  "calibration_usable_case_count": 18,
  "positive_MFE_high_MAE_count": 5,
  "hard_break_MAE50_count": 11,
  "local_4b_or_4c_source_count": 9,
  "source_proxy_only_count": 18,
  "evidence_url_pending_count": 18,
  "batch_reverification_required_count": 18,
  "current_profile_error_count": 18,
  "residual_contribution_label": "cross_archetype_guardrail_candidate"
}
```

## 6. Shadow Rule Candidates

- R13_HIGH_MAE_AFTER_POSITIVE_MFE_BLOCKS_GREEN_UNTIL_BRIDGE_REFRESH
- R13_SOURCE_PROXY_ONLY_ROWS_BLOCK_FULL4B_OR_STAGE3_GREEN_PROMOTION
- R13_REUSED_PRICE_ROW_REQUIRES_PROFILE_SHARD_REFETCH_BEFORE_WEIGHT_CHANGE
- R13_HARD4C_WATCH_IF_MAE180_BELOW_MINUS50_WITHOUT_NON_PRICE_EVIDENCE
- R13_CROSS_CANONICAL_REROUTE_REQUIRED_WHEN_TRIGGER_MECHANISM_DIFFERS_FROM_SOURCE_FILE

No production scoring change is made here. These are shadow-weight / batch-handoff candidates only.

## 7. Deferred Coding Agent Handoff Prompt

```text
Do not execute during research. Later coding-agent task:
1. Re-open every source_file + stock-web profile/shard for rows in this R13 MD.
2. Confirm that each row has full 30D/90D/180D MFE/MAE and no corporate-action contamination in entry_date~D+180.
3. If row refetch fails or evidence_url_pending remains true, block promotion and keep as review-only.
4. Implement only narrow R13 guardrail specs if at least 12 verified rows remain after refetch.
5. Do not change production scoring from this MD alone; aggregate with other verified R13 rows first.
```

## 8. Next Research State

```text
completed_round = R13
completed_loop = 11
selection_basis = docs/core/V12_Research_No_Repeat_Index.md + conversation-local generated MD ledger
selected_priority_bucket = R13 checkpoint after Priority 0 local floors and Priority 1 to-50 passes
next_recommended_archetypes = R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION_reverify_batch, R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW_source_repair, C02_POWER_GRID_DATACENTER_CAPEX_verified_url_repair, C28_SOFTWARE_SECURITY_CONTRACT_RETENTION_verified_url_repair
round_schedule_status = coverage_index_selected
round_sector_consistency = pass
```
