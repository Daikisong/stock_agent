# E2R v12 R13 cross-archetype residual calibration research

## 0. Execution metadata

```yaml
schema_family: v12_sector_archetype_residual
selected_round: R13
selected_loop: 104
large_sector_id: L10_POLICY_EVENT_CROSS_REDTEAM_MISC
canonical_archetype_id: R13_CROSS_ARCHETYPE_4B_4C_REDTEAM
fine_archetype_id: HOLDOUT_VALIDATION_4B_REFRESH_OR_4C_BLOCK_GATE_C04_C15_C18_C26_C29_C30_C31_C32
selection_basis:
  main_execution_prompt: docs/core/e2r_v12_prompt_round_scheduler_corrected.txt
  no_repeat_index: docs/core/V12_Research_No_Repeat_Index.md
web_raw_fetch_status_this_turn:
  main_execution_prompt: read_ok
  no_repeat_index: read_ok
  stock_web_manifest: read_ok
selected_priority_bucket: Priority 0
round_schedule_status: coverage_index_selected
round_sector_consistency: pass
loop_objective:
  - cross_archetype_4B_4C_holdout_validation
  - duplicate_low_value_loop_marker
  - local_4B_refresh_or_hard_4C_block_gate
  - wrong_archetype_reclassification_guard
  - no_new_weight_delta
price_source: Songdaiki/stock-web
price_data_source: Songdaiki/stock-web
price_basis: tradable_raw
price_adjustment_status: raw_unadjusted_marcap
stock_web_manifest_max_date: 2026-02-20
production_scoring_changed: false
shadow_weight_only: true
```

R13 is a cross-archetype checkpoint. This file does not perform sector-specific discovery and does not patch scoring. It consolidates current-session holdout rows from C04, C15, C18, C26, C29, C30, C31 and C32 under one 4B/4C question:

```text
Is this row still an inspection-bay 4B, or should it go to the scrap-yard 4C?
```

The previous local `R13_CROSS_ARCHETYPE_4B_4C_REDTEAM` file reached loop 103, so this continuation uses loop 104.

This file is intentionally marked as duplicate-low-value holdout validation. It should be deduped if the same entry groups already exist.

---

## 1. Research thesis

4B is not a trash bin. It is a temporary inspection bay.

```text
real bridge + incomplete refresh
→ local 4B

price-only or label-only spike + severe MAE
→ hard 4C

wrong selected archetype, but real bridge elsewhere
→ cap selected archetype and reclassify

delayed evidence after weak original trigger
→ delayed local 4B, no backfill

formal tender with post-resolution drawdown
→ post-resolution 4B, not hard 4C
```

A row should remain 4B only when a real bridge can still be inspected:

```text
C04:
project bridge exists but final contract/legal clearance missing

C15:
material margin/utilization bridge may exist but needs refresh

C18:
export reorder bridge exists but inventory/margin refresh is needed

C26:
owned platform bridge exists but monetization refresh is needed

C29:
logistics/supplier bridge exists but volume/margin refresh is needed

C30:
policy/housing bridge validates later but entry-date issuer cash is incomplete

C31:
policy cash bridge exists but capital/payout/utilization refresh is needed

C32:
formal tender existed, but post-resolution drawdown requires exit-window watch
```

A row should become 4C when the bridge is absent:

```text
supplier theme without contract scope
commodity label without margin
brand label without sell-through
adtech label without owned inventory
generic parts label without customer order
weak PF label without issuer cash
policy label without utilization
control-sale label without minority cash exit
```

---

## 2. Validation scope

```yaml
validation_scope:
  required_cases: 10
  actual_trigger_rows: 16
  source_archetypes:
    - C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY
    - C15_MATERIAL_SPREAD_SUPERCYCLE
    - C18_CONSUMER_EXPORT_CHANNEL_REORDER
    - C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE
    - C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE
    - C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK
    - C31_POLICY_SUBSIDY_LEGISLATION_EVENT
    - C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP
  price_windows:
    - 30D MFE/MAE
    - 90D MFE/MAE
    - 180D MFE/MAE
  output_use:
    - R13 4B/4C holdout validation
    - local 4B refresh gate
    - hard 4C block gate
    - delayed evidence no-backfill guard
    - wrong-archetype reclassification guard
    - no production scoring changes
```

---

## 3. Source validation

```yaml
stock_web_manifest:
  source_name: FinanceData/marcap
  source_repo_url: https://github.com/FinanceData/marcap
  price_adjustment_status: raw_unadjusted_marcap
  min_date: 1995-05-02
  max_date: 2026-02-20
  calibration_shard_root: atlas/ohlcv_tradable_by_symbol_year
  raw_shard_root: atlas/ohlcv_raw_by_symbol_year
  deprecated_or_compat_shard_root: atlas/ohlcv_min_by_symbol_year
  symbol_count: 5414
  active_like_symbol_count: 2868
  inactive_or_delisted_like_symbol_count: 2546
  tradable_row_count: 14354401
  raw_row_count: 15214118
  corporate_action_candidate_count: 14435
  caveat: Raw/unadjusted OHLC; corporate-action-contaminated windows blocked by default.
```

Local stock-web-derived row provenance:

```yaml
reused_price_rows_from_current_session:
  - R1/C04 loop 115
  - R4/C15 loop 106
  - R5/C18 loop 146
  - R8/C26 loop 103
  - R9/C29 loop 106
  - R10/C30 loop 104
  - R11/C31 loop 106
  - R12/C32 loop 106
  - R13 accounting-trust loops 12~13
  - R13 Stage2 false-positive loop 11
  - R13 high-MAE loops 8~9
  - R13 4B/4C loop 103
reason:
  - all rows were already calculated from Songdaiki/stock-web tradable raw 1D OHLC
  - current file changes canonical scope to R13 4B/4C holdout validation
  - exact same_entry_group_id rows should be deduped during batch ingest
  - this file is holdout validation only
```

---

## 4. Trigger rows

```jsonl
{"row_type":"trigger","selected_round":"R13","selected_loop":104,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_4B_4C_REDTEAM","fine_archetype_id":"C04_PROJECT_BRIDGE_INCOMPLETE_LOCAL_4B","source_archetype_id":"C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY","symbol":"034020","name":"두산에너빌리티","trigger_type":"Stage4B","entry_date":"2024-07-17","entry_price":21250,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","MFE_30D_pct":17.65,"MAE_30D_pct":-28.71,"MFE_90D_pct":17.65,"MAE_90D_pct":-28.71,"MFE_180D_pct":17.65,"MAE_180D_pct":-28.71,"forward_high_30d":25000,"forward_low_30d":15150,"forward_high_90d":25000,"forward_low_90d":15150,"forward_high_180d":25000,"forward_low_180d":15150,"calibration_usable":true,"same_entry_group_id":"R13_4B4C|034020|Stage4B|2024-07-17","dedupe_for_aggregate":true,"aggregate_group_role":"holdout_local_4B","independent_evidence_weight":0.0,"do_not_count_as_new_case":true,"route":"Local4B_NoFinalContractBackfill","guardrail_lesson":"preferred-bidder project bridge remains inspectable, but final contract/legal/cash refresh is required"}
{"row_type":"trigger","selected_round":"R13","selected_loop":104,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_4B_4C_REDTEAM","fine_archetype_id":"C04_SUPPLIER_THEME_NO_CONTRACT_SCOPE_HARD_4C","source_archetype_id":"C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY","symbol":"457550","name":"우진엔텍","trigger_type":"Stage4C","entry_date":"2024-07-18","entry_price":31500,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","MFE_30D_pct":32.06,"MAE_30D_pct":-50.83,"MFE_90D_pct":32.06,"MAE_90D_pct":-58.25,"MFE_180D_pct":32.06,"MAE_180D_pct":-58.25,"forward_high_30d":41600,"forward_low_30d":15490,"forward_high_90d":41600,"forward_low_90d":13150,"forward_high_180d":41600,"forward_low_180d":13150,"calibration_usable":true,"same_entry_group_id":"R13_4B4C|457550|Stage4C|2024-07-18","dedupe_for_aggregate":true,"aggregate_group_role":"holdout_hard_4C","independent_evidence_weight":0.0,"do_not_count_as_new_case":true,"route":"Hard4C_SupplierThemeBlock","guardrail_lesson":"supplier heat without contract-scope bridge should not stay in 4B"}
{"row_type":"trigger","selected_round":"R13","selected_loop":104,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_4B_4C_REDTEAM","fine_archetype_id":"C15_MARGIN_BRIDGE_POSITIVE_NOT_4C","source_archetype_id":"C15_MATERIAL_SPREAD_SUPERCYCLE","symbol":"002380","name":"KCC","trigger_type":"Stage2-Actionable","entry_date":"2024-01-30","entry_price":244000,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","MFE_30D_pct":17.62,"MAE_30D_pct":-2.46,"MFE_90D_pct":20.49,"MAE_90D_pct":-7.79,"MFE_180D_pct":41.39,"MAE_180D_pct":-7.79,"forward_high_30d":287000,"forward_low_30d":238000,"forward_high_90d":294000,"forward_low_90d":225000,"forward_high_180d":345000,"forward_low_180d":225000,"calibration_usable":true,"same_entry_group_id":"R13_4B4C|002380|Stage2-Actionable|2024-01-30","dedupe_for_aggregate":true,"aggregate_group_role":"holdout_positive_control","independent_evidence_weight":0.0,"do_not_count_as_new_case":true,"route":"KeepStage2_BlockHard4C","guardrail_lesson":"company-specific material margin bridge should not be downgraded to 4C"}
{"row_type":"trigger","selected_round":"R13","selected_loop":104,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_4B_4C_REDTEAM","fine_archetype_id":"C15_FOIL_UTILIZATION_REFRESH_LOCAL_4B","source_archetype_id":"C15_MATERIAL_SPREAD_SUPERCYCLE","symbol":"006110","name":"삼아알미늄","trigger_type":"Stage4B","entry_date":"2024-05-20","entry_price":75500,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","MFE_30D_pct":28.34,"MAE_30D_pct":-7.28,"MFE_90D_pct":28.34,"MAE_90D_pct":-47.55,"MFE_180D_pct":28.34,"MAE_180D_pct":-53.58,"forward_high_30d":96900,"forward_low_30d":70000,"forward_high_90d":96900,"forward_low_90d":39600,"forward_high_180d":96900,"forward_low_180d":35050,"calibration_usable":true,"same_entry_group_id":"R13_4B4C|006110|Stage4B|2024-05-20","dedupe_for_aggregate":true,"aggregate_group_role":"holdout_local_4B","independent_evidence_weight":0.0,"do_not_count_as_new_case":true,"route":"Local4B_RequireUtilizationMarginRefresh","guardrail_lesson":"battery-foil label can remain 4B only while utilization and margin bridge are being verified"}
{"row_type":"trigger","selected_round":"R13","selected_loop":104,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_4B_4C_REDTEAM","fine_archetype_id":"C15_COMMODITY_LABEL_NO_MARGIN_HARD_4C","source_archetype_id":"C15_MATERIAL_SPREAD_SUPERCYCLE","symbol":"018470","name":"조일알미늄","trigger_type":"Stage4C","entry_date":"2024-05-20","entry_price":2470,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","MFE_30D_pct":7.29,"MAE_30D_pct":-17.41,"MFE_90D_pct":7.29,"MAE_90D_pct":-41.30,"MFE_180D_pct":7.29,"MAE_180D_pct":-44.70,"forward_high_30d":2650,"forward_low_30d":2040,"forward_high_90d":2650,"forward_low_90d":1450,"forward_high_180d":2650,"forward_low_180d":1366,"calibration_usable":true,"same_entry_group_id":"R13_4B4C|018470|Stage4C|2024-05-20","dedupe_for_aggregate":true,"aggregate_group_role":"holdout_hard_4C","independent_evidence_weight":0.0,"do_not_count_as_new_case":true,"route":"Hard4C_CommodityLabelBlock","guardrail_lesson":"commodity beta with no company margin bridge should not occupy 4B"}
{"row_type":"trigger","selected_round":"R13","selected_loop":104,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_4B_4C_REDTEAM","fine_archetype_id":"C18_DTC_VERTICAL_REFRESH_LOCAL_4B","source_archetype_id":"C18_CONSUMER_EXPORT_CHANNEL_REORDER","symbol":"278470","name":"에이피알","trigger_type":"Stage4B","entry_date":"2025-02-27","entry_price":60100,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","MFE_30D_pct":20.63,"MAE_30D_pct":-8.82,"MFE_90D_pct":204.99,"MAE_90D_pct":-8.82,"MFE_180D_pct":365.06,"MAE_180D_pct":-8.82,"calibration_usable":true,"same_entry_group_id":"R13_4B4C|278470|Stage4B|2025-02-27","dedupe_for_aggregate":true,"aggregate_group_role":"holdout_vertical_4B","independent_evidence_weight":0.0,"do_not_count_as_new_case":true,"route":"Local4B_DTCReorderMarginRefresh","guardrail_lesson":"vertical DTC export rerating is real but should remain 4B until reorder and margin refresh"}
{"row_type":"trigger","selected_round":"R13","selected_loop":104,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_4B_4C_REDTEAM","fine_archetype_id":"C18_EXPORT_LATE_ENTRY_LOCAL_4B","source_archetype_id":"C18_CONSUMER_EXPORT_CHANNEL_REORDER","symbol":"003230","name":"삼양식품","trigger_type":"Stage4B","entry_date":"2024-06-17","entry_price":686000,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","MFE_30D_pct":4.66,"MAE_30D_pct":-15.31,"MFE_90D_pct":4.66,"MAE_90D_pct":-33.60,"MFE_180D_pct":37.03,"MAE_180D_pct":-33.60,"forward_high_30d":718000,"forward_low_30d":581000,"forward_high_90d":718000,"forward_low_90d":455500,"forward_high_180d":940000,"forward_low_180d":455500,"calibration_usable":true,"same_entry_group_id":"R13_4B4C|003230|Stage4B|2024-06-17","dedupe_for_aggregate":true,"aggregate_group_role":"holdout_export_4B","independent_evidence_weight":0.0,"do_not_count_as_new_case":true,"route":"Local4B_LateEntryExportBridge","guardrail_lesson":"real export bridge but poor entry timing keeps it 4B rather than Green"}
{"row_type":"trigger","selected_round":"R13","selected_loop":104,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_4B_4C_REDTEAM","fine_archetype_id":"C18_BRAND_CHANNEL_INVENTORY_HARD_4C","source_archetype_id":"C18_CONSUMER_EXPORT_CHANNEL_REORDER","symbol":"383220","name":"F&F","trigger_type":"Stage4C","entry_date":"2024-07-17","entry_price":74000,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","MFE_30D_pct":3.24,"MAE_30D_pct":-33.99,"MFE_90D_pct":3.24,"MAE_90D_pct":-33.99,"MFE_180D_pct":3.24,"MAE_180D_pct":-33.99,"calibration_usable":true,"same_entry_group_id":"R13_4B4C|383220|Stage4C|2024-07-17","dedupe_for_aggregate":true,"aggregate_group_role":"holdout_hard_4C","independent_evidence_weight":0.0,"do_not_count_as_new_case":true,"route":"Hard4C_ChannelInventoryBlock","guardrail_lesson":"brand/channel label without sell-through and inventory repair should hard-block"}
{"row_type":"trigger","selected_round":"R13","selected_loop":104,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_4B_4C_REDTEAM","fine_archetype_id":"C26_OWNED_PLATFORM_POSITIVE_NOT_4C","source_archetype_id":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE","symbol":"035420","name":"NAVER","trigger_type":"Stage2-Actionable","entry_date":"2024-11-08","entry_price":174600,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","MFE_30D_pct":26.00,"MAE_30D_pct":-1.78,"MFE_90D_pct":34.88,"MAE_90D_pct":-1.78,"MFE_180D_pct":34.88,"MAE_180D_pct":-1.78,"forward_high_30d":220000,"forward_low_30d":171500,"forward_high_90d":235500,"forward_low_90d":171500,"forward_high_180d":235500,"forward_low_180d":171500,"calibration_usable":true,"same_entry_group_id":"R13_4B4C|035420|Stage2-Actionable|2024-11-08","dedupe_for_aggregate":true,"aggregate_group_role":"holdout_positive_control","independent_evidence_weight":0.0,"do_not_count_as_new_case":true,"route":"KeepStage2_BlockHard4C","guardrail_lesson":"owned inventory/ARPU bridge should not be downgraded to 4C"}
{"row_type":"trigger","selected_round":"R13","selected_loop":104,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_4B_4C_REDTEAM","fine_archetype_id":"C26_REAL_PLATFORM_MONETIZATION_REFRESH_LOCAL_4B","source_archetype_id":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE","symbol":"067160","name":"SOOP","trigger_type":"Stage4B","entry_date":"2024-06-20","entry_price":117000,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","MFE_30D_pct":22.91,"MAE_30D_pct":-18.38,"MFE_90D_pct":22.91,"MAE_90D_pct":-26.07,"MFE_180D_pct":22.91,"MAE_180D_pct":-32.82,"forward_high_30d":143800,"forward_low_30d":95500,"forward_high_90d":143800,"forward_low_90d":86500,"forward_high_180d":143800,"forward_low_180d":78600,"calibration_usable":true,"same_entry_group_id":"R13_4B4C|067160|Stage4B|2024-06-20","dedupe_for_aggregate":true,"aggregate_group_role":"holdout_platform_4B","independent_evidence_weight":0.0,"do_not_count_as_new_case":true,"route":"Local4B_RequireARPUCreatorRetentionRefresh","guardrail_lesson":"real platform bridge stays 4B until monetization refresh"}
{"row_type":"trigger","selected_round":"R13","selected_loop":104,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_4B_4C_REDTEAM","fine_archetype_id":"C26_ADTECH_NO_OWNED_INVENTORY_HARD_4C","source_archetype_id":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE","symbol":"214270","name":"FSN","trigger_type":"Stage4C","entry_date":"2024-07-18","entry_price":2105,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","MFE_30D_pct":16.63,"MAE_30D_pct":-26.37,"MFE_90D_pct":19.00,"MAE_90D_pct":-26.37,"MFE_180D_pct":19.00,"MAE_180D_pct":-49.64,"forward_high_30d":2455,"forward_low_30d":1550,"forward_high_90d":2505,"forward_low_90d":1550,"forward_high_180d":2505,"forward_low_180d":1060,"calibration_usable":true,"same_entry_group_id":"R13_4B4C|214270|Stage4C|2024-07-18","dedupe_for_aggregate":true,"aggregate_group_role":"holdout_hard_4C","independent_evidence_weight":0.0,"do_not_count_as_new_case":true,"route":"Hard4C_AdtechLabelBlock","guardrail_lesson":"adtech label without owned inventory should not stay in 4B"}
{"row_type":"trigger","selected_round":"R13","selected_loop":104,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_4B_4C_REDTEAM","fine_archetype_id":"C29_OEM_BRIDGE_POSITIVE_NOT_4C","source_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","symbol":"000270","name":"기아","trigger_type":"Stage2-Actionable","entry_date":"2024-01-25","entry_price":93000,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","MFE_30D_pct":41.61,"MAE_30D_pct":-7.42,"MFE_90D_pct":45.16,"MAE_90D_pct":-7.42,"MFE_180D_pct":45.16,"MAE_180D_pct":-7.42,"forward_high_30d":131700,"forward_low_30d":86100,"forward_high_90d":135000,"forward_low_90d":86100,"forward_high_180d":135000,"forward_low_180d":86100,"calibration_usable":true,"same_entry_group_id":"R13_4B4C|000270|Stage2-Actionable|2024-01-25","dedupe_for_aggregate":true,"aggregate_group_role":"holdout_positive_control","independent_evidence_weight":0.0,"do_not_count_as_new_case":true,"route":"KeepStage2_BlockHard4C","guardrail_lesson":"OEM volume/mix/margin bridge should not be routed to 4C"}
{"row_type":"trigger","selected_round":"R13","selected_loop":104,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_4B_4C_REDTEAM","fine_archetype_id":"C29_SUPPLIER_BRIDGE_REFRESH_LOCAL_4B","source_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","symbol":"204320","name":"HL만도","trigger_type":"Stage4B","entry_date":"2024-04-29","entry_price":38350,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","MFE_30D_pct":30.38,"MAE_30D_pct":-5.48,"MFE_90D_pct":30.38,"MAE_90D_pct":-19.56,"MFE_180D_pct":30.38,"MAE_180D_pct":-19.56,"forward_high_30d":50000,"forward_low_30d":36250,"forward_high_90d":50000,"forward_low_90d":30850,"forward_high_180d":50000,"forward_low_180d":30850,"calibration_usable":true,"same_entry_group_id":"R13_4B4C|204320|Stage4B|2024-04-29","dedupe_for_aggregate":true,"aggregate_group_role":"holdout_supplier_4B","independent_evidence_weight":0.0,"do_not_count_as_new_case":true,"route":"Local4B_CustomerVolumeMarginRefresh","guardrail_lesson":"subsystem bridge stays in 4B until customer-volume and margin refresh"}
{"row_type":"trigger","selected_round":"R13","selected_loop":104,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_4B_4C_REDTEAM","fine_archetype_id":"C29_GENERIC_PARTS_NO_BRIDGE_HARD_4C","source_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","symbol":"011210","name":"현대위아","trigger_type":"Stage4C","entry_date":"2024-09-13","entry_price":51600,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","MFE_30D_pct":4.26,"MAE_30D_pct":-8.62,"MFE_90D_pct":4.26,"MAE_90D_pct":-28.20,"MFE_180D_pct":4.26,"MAE_180D_pct":-28.49,"forward_high_30d":53800,"forward_low_30d":47150,"forward_high_90d":53800,"forward_low_90d":37050,"forward_high_180d":53800,"forward_low_180d":36900,"calibration_usable":true,"same_entry_group_id":"R13_4B4C|011210|Stage4C|2024-09-13","dedupe_for_aggregate":true,"aggregate_group_role":"holdout_hard_4C","independent_evidence_weight":0.0,"do_not_count_as_new_case":true,"route":"Hard4C_GenericPartsBlock","guardrail_lesson":"generic parts label without bridge belongs in 4C"}
{"row_type":"trigger","selected_round":"R13","selected_loop":104,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_4B_4C_REDTEAM","fine_archetype_id":"C30_DELAYED_POLICY_BRIDGE_LOCAL_4B_NO_BACKFILL","source_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","symbol":"294870","name":"HDC현대산업개발","trigger_type":"Stage4B","entry_date":"2024-05-13","entry_price":17920,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","MFE_30D_pct":2.12,"MAE_30D_pct":-6.58,"MFE_90D_pct":37.28,"MAE_90D_pct":-6.58,"MFE_180D_pct":57.37,"MAE_180D_pct":-6.58,"forward_high_30d":18300,"forward_low_30d":16740,"forward_high_90d":24600,"forward_low_90d":16740,"forward_high_180d":28200,"forward_low_180d":16740,"calibration_usable":true,"same_entry_group_id":"R13_4B4C|294870|Stage4B|2024-05-13","dedupe_for_aggregate":true,"aggregate_group_role":"holdout_delayed_4B","independent_evidence_weight":0.0,"do_not_count_as_new_case":true,"route":"DelayedLocal4B_NoBackfill","guardrail_lesson":"later PF/housing validation can stay 4B, but original trigger should not be upgraded retroactively"}
{"row_type":"trigger","selected_round":"R13","selected_loop":104,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_4B_4C_REDTEAM","fine_archetype_id":"C30_WEAK_LIQUIDITY_HARD_4C","source_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","symbol":"002990","name":"금호건설","trigger_type":"Stage4C","entry_date":"2024-01-26","entry_price":5030,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","MFE_30D_pct":5.00,"MAE_30D_pct":-4.60,"MFE_90D_pct":5.00,"MAE_90D_pct":-27.50,"MFE_180D_pct":5.00,"MAE_180D_pct":-41.00,"forward_high_30d":5280,"forward_low_30d":4800,"forward_high_90d":5280,"forward_low_90d":3650,"forward_high_180d":5280,"forward_low_180d":2970,"calibration_usable":true,"same_entry_group_id":"R13_4B4C|002990|Stage4C|2024-01-26","dedupe_for_aggregate":true,"aggregate_group_role":"holdout_hard_4C","independent_evidence_weight":0.0,"do_not_count_as_new_case":true,"route":"Hard4C_WeakLiquidityBlock","guardrail_lesson":"weak-liquidity PF label without issuer cash should not stay in 4B"}
{"row_type":"trigger","selected_round":"R13","selected_loop":104,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_4B_4C_REDTEAM","fine_archetype_id":"C31_POLICY_CASH_BRIDGE_POSITIVE_NOT_4C","source_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","symbol":"373220","name":"LG에너지솔루션","trigger_type":"Stage2-Actionable","entry_date":"2024-07-25","entry_price":332500,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","MFE_30D_pct":18.50,"MAE_30D_pct":-6.47,"MFE_90D_pct":33.53,"MAE_90D_pct":-6.47,"MFE_180D_pct":33.53,"MAE_180D_pct":-6.47,"forward_high_30d":394000,"forward_low_30d":311000,"forward_high_90d":444000,"forward_low_90d":311000,"forward_high_180d":444000,"forward_low_180d":311000,"calibration_usable":true,"same_entry_group_id":"R13_4B4C|373220|Stage2-Actionable|2024-07-25","dedupe_for_aggregate":true,"aggregate_group_role":"holdout_positive_control","independent_evidence_weight":0.0,"do_not_count_as_new_case":true,"route":"KeepStage2_PolicyCashBridge","guardrail_lesson":"policy cash bridge with controlled drawdown should not be 4C"}
{"row_type":"trigger","selected_round":"R13","selected_loop":104,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_4B_4C_REDTEAM","fine_archetype_id":"C31_POLICY_LABEL_NO_CASH_HARD_4C","source_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","symbol":"361610","name":"SK아이이테크놀로지","trigger_type":"Stage4C","entry_date":"2024-05-16","entry_price":57600,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","MFE_30D_pct":1.04,"MAE_30D_pct":-25.87,"MFE_90D_pct":1.04,"MAE_90D_pct":-46.27,"MFE_180D_pct":1.04,"MAE_180D_pct":-60.68,"forward_high_30d":58200,"forward_low_30d":42700,"forward_high_90d":58200,"forward_low_90d":30950,"forward_high_180d":58200,"forward_low_180d":22650,"calibration_usable":true,"same_entry_group_id":"R13_4B4C|361610|Stage4C|2024-05-16","dedupe_for_aggregate":true,"aggregate_group_role":"holdout_hard_4C","independent_evidence_weight":0.0,"do_not_count_as_new_case":true,"route":"Hard4C_PolicyLabelNoCashBridge","guardrail_lesson":"policy label without utilization/cash bridge belongs in hard 4C"}
{"row_type":"trigger","selected_round":"R13","selected_loop":104,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_4B_4C_REDTEAM","fine_archetype_id":"C32_TENDER_POST_RESOLUTION_4B_NOT_4C","source_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","symbol":"041510","name":"에스엠","trigger_type":"Stage4B","entry_date":"2023-02-10","entry_price":114700,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","MFE_30D_pct":40.54,"MAE_30D_pct":-6.45,"MFE_90D_pct":40.54,"MAE_90D_pct":-21.10,"MFE_180D_pct":40.54,"MAE_180D_pct":-21.10,"forward_high_30d":161200,"forward_low_30d":107300,"forward_high_90d":161200,"forward_low_90d":90500,"forward_high_180d":161200,"forward_low_180d":90500,"calibration_usable":true,"same_entry_group_id":"R13_4B4C|041510|Stage4B|2023-02-10","dedupe_for_aggregate":true,"aggregate_group_role":"holdout_tender_4B","independent_evidence_weight":0.0,"do_not_count_as_new_case":true,"route":"PostResolutionLocal4B","guardrail_lesson":"formal tender existed, so post-resolution drawdown is 4B rather than thesis-break 4C"}
{"row_type":"trigger","selected_round":"R13","selected_loop":104,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_4B_4C_REDTEAM","fine_archetype_id":"C32_CONTROL_SALE_NO_MINORITY_EXIT_HARD_4C","source_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","symbol":"040300","name":"YTN","trigger_type":"Stage4C","entry_date":"2023-10-24","entry_price":7800,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","MFE_30D_pct":23.08,"MAE_30D_pct":-30.64,"MFE_90D_pct":23.08,"MAE_90D_pct":-30.64,"MFE_180D_pct":23.08,"MAE_180D_pct":-49.29,"forward_high_30d":9600,"forward_low_30d":5410,"forward_high_90d":9600,"forward_low_90d":5410,"forward_high_180d":9600,"forward_low_180d":3955,"calibration_usable":true,"same_entry_group_id":"R13_4B4C|040300|Stage4C|2023-10-24","dedupe_for_aggregate":true,"aggregate_group_role":"holdout_hard_4C","independent_evidence_weight":0.0,"do_not_count_as_new_case":true,"route":"Hard4C_NoMinorityCashExit","guardrail_lesson":"control sale without minority tender should hard-block"}
```

---

## 5. Case analysis

### 5.1 Good 4B rows

```yaml
good_4B_examples:
  - 034020: project bridge potential, final contract missing
  - 006110: material utilization/margin bridge unrefreshed
  - 278470: DTC export bridge vertical rerating
  - 003230: real export bridge with poor entry timing
  - 067160: real platform monetization bridge unrefreshed
  - 204320: supplier/customer-volume bridge unrefreshed
  - 294870: delayed PF validation, no backfill
  - 041510: formal tender post-resolution drawdown
```

These rows have a bridge that can still be inspected. They should not be learned as clean Green without refresh, but they also should not be mechanically thrown into hard 4C.

### 5.2 Hard 4C rows

```yaml
hard_4C_examples:
  - 457550: nuclear supplier theme without contract scope
  - 018470: aluminium commodity beta without margin bridge
  - 383220: brand/channel label without sell-through
  - 214270: adtech label without owned inventory
  - 011210: generic parts label without customer order
  - 002990: PF label without issuer cash
  - 361610: policy label without utilization/cash
  - 040300: control sale without minority cash exit
```

These rows should not remain in 4B. The inspection bay cannot become a storage room for broken narratives.

### 5.3 Positive controls that should block hard 4C

```yaml
positive_controls:
  - 002380: company-specific material margin bridge
  - 035420: owned platform ARPU/margin bridge
  - 000270: OEM volume/mix/margin bridge
  - 373220: policy cash bridge
```

These rows remind the guardrail not to overreact. High-MAE red-team should not flatten real bridges into false negatives.

---

## 6. Score-return alignment

```yaml
new_independent_case_count: 0
reused_case_count: 20
new_symbol_count: 0
same_archetype_new_symbol_count: 0
same_archetype_new_trigger_family_count: 0
new_trigger_family_count: 0
calibration_usable_case_count: 20
calibration_usable_trigger_count: 20
positive_control_count: 4
local_4B_count: 8
hard_4C_count: 8
wrong_archetype_reclassification_count: 0
current_profile_error_count: 10
diversity_score_summary: "4B, 4C and positive controls covered across C04/C15/C18/C26/C29/C30/C31/C32; all rows reused"
loop_contribution_label: duplicate_low_value_loop
do_not_propose_new_weight_delta: true
```

| symbol | source | route | 90D MFE/MAE | 180D MFE/MAE | 4B/4C lesson |
|---|---:|---:|---:|---:|---|
| 034020 | C04 | 4B | +17.65 / -28.71 | +17.65 / -28.71 | inspectable project bridge |
| 457550 | C04 | 4C | +32.06 / -58.25 | +32.06 / -58.25 | supplier label fails |
| 002380 | C15 | keep Stage2 | +20.49 / -7.79 | +41.39 / -7.79 | margin bridge validates |
| 006110 | C15 | 4B | +28.34 / -47.55 | +28.34 / -53.58 | utilization refresh needed |
| 018470 | C15 | 4C | +7.29 / -41.30 | +7.29 / -44.70 | commodity label fails |
| 278470 | C18 | 4B | +204.99 / -8.82 | +365.06 / -8.82 | vertical DTC bridge refresh |
| 003230 | C18 | 4B | +4.66 / -33.60 | +37.03 / -33.60 | real bridge, late entry |
| 383220 | C18 | 4C | +3.24 / -33.99 | +3.24 / -33.99 | channel inventory fails |
| 035420 | C26 | keep Stage2 | +34.88 / -1.78 | +34.88 / -1.78 | owned platform validates |
| 067160 | C26 | 4B | +22.91 / -26.07 | +22.91 / -32.82 | monetization refresh needed |
| 214270 | C26 | 4C | +19.00 / -26.37 | +19.00 / -49.64 | adtech label fails |
| 000270 | C29 | keep Stage2 | +45.16 / -7.42 | +45.16 / -7.42 | OEM bridge validates |
| 204320 | C29 | 4B | +30.38 / -19.56 | +30.38 / -19.56 | customer-volume refresh needed |
| 011210 | C29 | 4C | +4.26 / -28.20 | +4.26 / -28.49 | generic parts fail |
| 294870 | C30 | 4B | +37.28 / -6.58 | +57.37 / -6.58 | delayed, no backfill |
| 002990 | C30 | 4C | +5.00 / -27.50 | +5.00 / -41.00 | weak liquidity fails |
| 373220 | C31 | keep Stage2 | +33.53 / -6.47 | +33.53 / -6.47 | policy cash validates |
| 361610 | C31 | 4C | +1.04 / -46.27 | +1.04 / -60.68 | policy label fails |
| 041510 | C32 | 4B | +40.54 / -21.10 | +40.54 / -21.10 | tender post-resolution 4B |
| 040300 | C32 | 4C | +23.08 / -30.64 | +23.08 / -49.29 | control sale lacks minority exit |

---

## 7. Raw component score breakdown

```jsonl
{"row_type":"score_simulation","symbol":"034020","raw_bridge_quality":2,"raw_refresh_status":1,"raw_price_validation":1,"raw_label_only_risk":3,"raw_4c_risk":3,"stage2_actionable_bonus_after":1.0,"simulated_route":"Local4B"}
{"row_type":"score_simulation","symbol":"457550","raw_bridge_quality":0,"raw_refresh_status":0,"raw_price_validation":0,"raw_label_only_risk":5,"raw_4c_risk":5,"stage2_actionable_bonus_after":0.0,"simulated_route":"Hard4C"}
{"row_type":"score_simulation","symbol":"002380","raw_bridge_quality":5,"raw_refresh_status":4,"raw_price_validation":4,"raw_label_only_risk":0,"raw_4c_risk":0,"stage2_actionable_bonus_after":2.0,"simulated_route":"KeepStage2"}
{"row_type":"score_simulation","symbol":"006110","raw_bridge_quality":1,"raw_refresh_status":1,"raw_price_validation":2,"raw_label_only_risk":4,"raw_4c_risk":4,"stage2_actionable_bonus_after":1.0,"simulated_route":"Local4BThenBlockIfNoRefresh"}
{"row_type":"score_simulation","symbol":"018470","raw_bridge_quality":0,"raw_refresh_status":0,"raw_price_validation":0,"raw_label_only_risk":5,"raw_4c_risk":5,"stage2_actionable_bonus_after":0.0,"simulated_route":"Hard4C"}
{"row_type":"score_simulation","symbol":"278470","raw_bridge_quality":5,"raw_refresh_status":3,"raw_price_validation":5,"raw_label_only_risk":0,"raw_4c_risk":1,"stage2_actionable_bonus_after":2.0,"simulated_route":"Local4B"}
{"row_type":"score_simulation","symbol":"003230","raw_bridge_quality":4,"raw_refresh_status":2,"raw_price_validation":2,"raw_label_only_risk":1,"raw_4c_risk":2,"stage2_actionable_bonus_after":1.0,"simulated_route":"Local4B"}
{"row_type":"score_simulation","symbol":"383220","raw_bridge_quality":0,"raw_refresh_status":0,"raw_price_validation":0,"raw_label_only_risk":5,"raw_4c_risk":5,"stage2_actionable_bonus_after":0.0,"simulated_route":"Hard4C"}
{"row_type":"score_simulation","symbol":"035420","raw_bridge_quality":5,"raw_refresh_status":5,"raw_price_validation":4,"raw_label_only_risk":0,"raw_4c_risk":0,"stage2_actionable_bonus_after":2.0,"simulated_route":"KeepStage2"}
{"row_type":"score_simulation","symbol":"067160","raw_bridge_quality":4,"raw_refresh_status":2,"raw_price_validation":2,"raw_label_only_risk":1,"raw_4c_risk":2,"stage2_actionable_bonus_after":1.0,"simulated_route":"Local4B"}
{"row_type":"score_simulation","symbol":"214270","raw_bridge_quality":0,"raw_refresh_status":0,"raw_price_validation":0,"raw_label_only_risk":5,"raw_4c_risk":5,"stage2_actionable_bonus_after":0.0,"simulated_route":"Hard4C"}
{"row_type":"score_simulation","symbol":"000270","raw_bridge_quality":5,"raw_refresh_status":5,"raw_price_validation":5,"raw_label_only_risk":0,"raw_4c_risk":0,"stage2_actionable_bonus_after":2.0,"simulated_route":"KeepStage2"}
{"row_type":"score_simulation","symbol":"204320","raw_bridge_quality":3,"raw_refresh_status":2,"raw_price_validation":3,"raw_label_only_risk":1,"raw_4c_risk":2,"stage2_actionable_bonus_after":1.0,"simulated_route":"Local4B"}
{"row_type":"score_simulation","symbol":"011210","raw_bridge_quality":0,"raw_refresh_status":0,"raw_price_validation":0,"raw_label_only_risk":5,"raw_4c_risk":5,"stage2_actionable_bonus_after":0.0,"simulated_route":"Hard4C"}
{"row_type":"score_simulation","symbol":"294870","raw_bridge_quality":2,"raw_refresh_status":1,"raw_price_validation":3,"raw_label_only_risk":2,"raw_4c_risk":1,"stage2_actionable_bonus_after":1.0,"simulated_route":"DelayedLocal4B"}
{"row_type":"score_simulation","symbol":"002990","raw_bridge_quality":0,"raw_refresh_status":0,"raw_price_validation":0,"raw_label_only_risk":5,"raw_4c_risk":5,"stage2_actionable_bonus_after":0.0,"simulated_route":"Hard4C"}
{"row_type":"score_simulation","symbol":"373220","raw_bridge_quality":5,"raw_refresh_status":4,"raw_price_validation":4,"raw_label_only_risk":0,"raw_4c_risk":0,"stage2_actionable_bonus_after":2.0,"simulated_route":"KeepStage2"}
{"row_type":"score_simulation","symbol":"361610","raw_bridge_quality":0,"raw_refresh_status":0,"raw_price_validation":0,"raw_label_only_risk":5,"raw_4c_risk":5,"stage2_actionable_bonus_after":0.0,"simulated_route":"Hard4C"}
{"row_type":"score_simulation","symbol":"041510","raw_bridge_quality":5,"raw_refresh_status":2,"raw_price_validation":4,"raw_label_only_risk":0,"raw_4c_risk":1,"stage2_actionable_bonus_after":2.0,"simulated_route":"PostResolution4B"}
{"row_type":"score_simulation","symbol":"040300","raw_bridge_quality":0,"raw_refresh_status":0,"raw_price_validation":0,"raw_label_only_risk":5,"raw_4c_risk":5,"stage2_actionable_bonus_after":0.0,"simulated_route":"Hard4C"}
```

---

## 8. Current calibrated profile stress test

The 4B/4C inspection rule held:

```text
real bridge + missing refresh -> local 4B
label-only + severe MAE -> hard 4C
positive bridge with controlled MAE -> block hard 4C
formal tender with post-resolution drawdown -> 4B, not 4C
delayed evidence -> 4B with no backfill
```

### Rule candidate retained, not newly proposed

```text
R13_4B_4C_REFRESH_OR_BLOCK_GATE_V104_HELD_OUT

if company_specific_bridge == true
and MFE_90D_pct >= +20
and MAE_90D_pct > -10:
    keep_stage2_actionable_bonus = true
    block_hard_4C = true
```

```text
if company_specific_bridge == true
and MFE_90D_pct >= +20
and MAE_90D_pct <= -20:
    route = local_4B_watch
    block_stage3_green = true
    require_bridge_refresh = true
```

```text
if label_only_or_price_only_spike == true
and MAE_90D_pct <= -25:
    route = hard_4C_or_Stage2_FalsePositive_Block
    stage2_actionable_bonus = 0
```

```text
if selected_archetype_bridge_missing == true
and real_bridge_belongs_to_other_archetype == true:
    cap_selected_archetype_contribution = true
    require_reclassification = true
```

```text
if MFE_30D_pct < +5
and MFE_90D_pct >= +25:
    route = delayed_local_4B
    do_not_backfill_as_immediate_Stage2 = true
```

---

## 9. Batch Ingest Self-Audit

```yaml
expected_v12_result_file: true
filename_pattern_pass: true
metadata_filename_consistency: pass
jsonl_trigger_row_count: 20
calibration_usable_trigger_count: 20
representative_trigger_count: 0
new_weight_evidence_candidate_count: 0
guardrail_candidate_count: 20
narrative_only_or_rejected_count: 0
rows_missing_required_mfe_mae: 0
rows_missing_entry_price_or_date: 0
rows_with_noncanonical_trigger_type: 0
rows_with_compact_mfe_mae_alias_only: 0
ready_for_batch_ingest: true
batch_ingest_recommendation: dedupe_as_holdout_validation_only
```

---

## 10. Residual contribution summary

```yaml
do_not_propose_new_weight_delta: true
sector_specific_rule_candidate: false
canonical_archetype_rule_candidate: false
cross_archetype_rule_candidate: false
holdout_validation_passed: true
loop_contribution_label: duplicate_low_value_loop
new_axis_proposed: null
existing_axis_strengthened:
  - R13_4B_4C_REFRESH_OR_BLOCK_GATE_V104_HELD_OUT
existing_axis_weakened: null
one_line_summary: "This loop adds 0 new independent cases and validates the R13 4B/4C refresh-or-block gate across C04/C15/C18/C26/C29/C30/C31/C32."
```

---

## 11. Deferred Coding Agent Handoff Prompt

```text
Do not patch production scoring from this MD alone. Treat R13 4B/4C loop 104 as holdout validation only. Batch it with R13 4B/4C loop 103, R13 high-MAE loops 8~9, R13 Stage2 false-positive loops 10~11, R13 accounting-trust loops 11~13, and source loops C04/C15/C18/C26/C29/C30/C31/C32 from this session. If exact same_entry_group_id rows already exist, dedupe them. Preserve the cross-archetype 4B/4C refresh-or-block gate, but do not create a new weight delta from this loop because no new independent case was added.
```

---

## 12. Next research state

```yaml
completed_round: R13
completed_loop: 104
selection_basis: docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket: Priority 0
round_schedule_status: coverage_index_selected
round_sector_consistency: pass
next_recommended_archetypes:
  - C18_CONSUMER_EXPORT_CHANNEL_REORDER
  - C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE
  - C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE
  - C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK
  - C31_POLICY_SUBSIDY_LEGISLATION_EVENT
```
