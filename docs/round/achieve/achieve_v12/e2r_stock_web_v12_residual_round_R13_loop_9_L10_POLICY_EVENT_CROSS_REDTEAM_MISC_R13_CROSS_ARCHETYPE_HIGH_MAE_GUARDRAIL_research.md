# E2R v12 R13 cross-archetype residual calibration research

## 0. Execution metadata

```yaml
schema_family: v12_sector_archetype_residual
selected_round: R13
selected_loop: 9
large_sector_id: L10_POLICY_EVENT_CROSS_REDTEAM_MISC
canonical_archetype_id: R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL
fine_archetype_id: HOLDOUT_VALIDATION_HIGH_MAE_BRIDGE_QUALITY_ROUTE_SPLIT_C04_C15_C18_C26_C29_C30_C31_C32
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
  - cross_archetype_high_MAE_holdout_validation
  - bridge_quality_before_MAE_route
  - local_4B_vs_hard_4C_split
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

R13 is a cross-archetype checkpoint. This file does not perform sector-specific discovery and does not patch scoring. It consolidates current-session holdout rows from C04, C15, C18, C26, C29, C30, C31 and C32 under one High-MAE question:

```text
When drawdown is high, should the row stay local 4B, or should it become hard 4C?
```

The previous local `R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL` file reached loop 8, so this continuation uses loop 9.

This file is intentionally marked as duplicate-low-value holdout validation. It should be deduped if the same entry groups already exist.

---

## 1. Research thesis

High MAE is smoke. It tells us something burned, but not what.

The correct route is not:

```text
high MAE -> always 4C
```

The correct route is:

```text
bridge quality first
MAE severity second
archetype ownership third
```

So the rule is:

```text
real company-specific bridge + high MAE
→ local 4B until bridge refresh

label-only / price-only spike + high MAE
→ hard 4C / Stage2 false-positive block

real bridge but wrong selected archetype
→ cap selected archetype and reclassify

later evidence after trigger
→ do not backfill
```

Cross-sector bridge dictionary:

```text
C04 nuclear:
final contract / legal clearance / order scope / cash bridge

C15 materials:
ASP / utilization / margin / FCF bridge

C18 consumer:
sell-through / reorder / inventory / margin bridge

C26 platform:
owned inventory / ARPU / retention / margin bridge

C29 mobility:
volume / mix / customer order / margin bridge

C30 construction:
issuer refinancing / guarantee relief / presale / debt-service / cash bridge

C31 policy:
policy-to-company cash bridge

C32 governance:
formal tender / appraisal / squeeze-out / minority cash-exit mechanics
```

---

## 2. Validation scope

```yaml
validation_scope:
  required_cases: 10
  actual_trigger_rows: 15
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
    - R13 High-MAE holdout validation
    - local 4B vs hard 4C route split
    - positive bridge escape hatch
    - label-only high-MAE block
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
  - R13 high-MAE loop 8
  - R13 4B/4C loop 103
reason:
  - all rows were already calculated from Songdaiki/stock-web tradable raw 1D OHLC
  - current file changes canonical scope to R13 high-MAE holdout validation
  - exact same_entry_group_id rows should be deduped during batch ingest
  - this file is holdout validation only
```

---

## 4. Trigger rows

```jsonl
{"row_type":"trigger","selected_round":"R13","selected_loop":9,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL","fine_archetype_id":"C04_PREFERRED_BIDDER_HIGH_MAE_LOCAL_4B_NO_BACKFILL","source_archetype_id":"C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY","symbol":"034020","name":"두산에너빌리티","trigger_type":"Stage4B","entry_date":"2024-07-17","entry_price":21250,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","MFE_30D_pct":17.65,"MAE_30D_pct":-28.71,"MFE_90D_pct":17.65,"MAE_90D_pct":-28.71,"MFE_180D_pct":17.65,"MAE_180D_pct":-28.71,"forward_high_30d":25000,"forward_low_30d":15150,"forward_high_90d":25000,"forward_low_90d":15150,"forward_high_180d":25000,"forward_low_180d":15150,"calibration_usable":true,"same_entry_group_id":"R13_HMAE|034020|Stage4B|2024-07-17","dedupe_for_aggregate":true,"aggregate_group_role":"holdout_local_4B","independent_evidence_weight":0.0,"do_not_count_as_new_case":true,"route":"Local4B_NoFinalContractBackfill","guardrail_lesson":"preferred-bidder story had bridge potential, but high MAE and missing final contract keep it local 4B"}
{"row_type":"trigger","selected_round":"R13","selected_loop":9,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL","fine_archetype_id":"C04_SUPPLIER_THEME_HIGH_MFE_SEVERE_MAE_HARD_4C","source_archetype_id":"C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY","symbol":"457550","name":"우진엔텍","trigger_type":"Stage4C","entry_date":"2024-07-18","entry_price":31500,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","MFE_30D_pct":32.06,"MAE_30D_pct":-50.83,"MFE_90D_pct":32.06,"MAE_90D_pct":-58.25,"MFE_180D_pct":32.06,"MAE_180D_pct":-58.25,"forward_high_30d":41600,"forward_low_30d":15490,"forward_high_90d":41600,"forward_low_90d":13150,"forward_high_180d":41600,"forward_low_180d":13150,"calibration_usable":true,"same_entry_group_id":"R13_HMAE|457550|Stage4C|2024-07-18","dedupe_for_aggregate":true,"aggregate_group_role":"holdout_hard_4C","independent_evidence_weight":0.0,"do_not_count_as_new_case":true,"route":"Hard4C_Stage2FalsePositiveBlock","guardrail_lesson":"supplier theme spike with severe MAE and no contract-scope bridge should hard-block"}
{"row_type":"trigger","selected_round":"R13","selected_loop":9,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL","fine_archetype_id":"C15_MATERIAL_MARGIN_LOW_MAE_POSITIVE_CONTROL","source_archetype_id":"C15_MATERIAL_SPREAD_SUPERCYCLE","symbol":"002380","name":"KCC","trigger_type":"Stage2-Actionable","entry_date":"2024-01-30","entry_price":244000,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","MFE_30D_pct":17.62,"MAE_30D_pct":-2.46,"MFE_90D_pct":20.49,"MAE_90D_pct":-7.79,"MFE_180D_pct":41.39,"MAE_180D_pct":-7.79,"forward_high_30d":287000,"forward_low_30d":238000,"forward_high_90d":294000,"forward_low_90d":225000,"forward_high_180d":345000,"forward_low_180d":225000,"calibration_usable":true,"same_entry_group_id":"R13_HMAE|002380|Stage2-Actionable|2024-01-30","dedupe_for_aggregate":true,"aggregate_group_role":"holdout_positive_control","independent_evidence_weight":0.0,"do_not_count_as_new_case":true,"route":"KeepStage2_BlockHard4C","guardrail_lesson":"company-specific material margin bridge with controlled MAE should not be routed to hard 4C"}
{"row_type":"trigger","selected_round":"R13","selected_loop":9,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL","fine_archetype_id":"C15_FOIL_HIGH_MFE_SEVERE_MAE_LOCAL_4B_THEN_BLOCK","source_archetype_id":"C15_MATERIAL_SPREAD_SUPERCYCLE","symbol":"006110","name":"삼아알미늄","trigger_type":"Stage4B","entry_date":"2024-05-20","entry_price":75500,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","MFE_30D_pct":28.34,"MAE_30D_pct":-7.28,"MFE_90D_pct":28.34,"MAE_90D_pct":-47.55,"MFE_180D_pct":28.34,"MAE_180D_pct":-53.58,"forward_high_30d":96900,"forward_low_30d":70000,"forward_high_90d":96900,"forward_low_90d":39600,"forward_high_180d":96900,"forward_low_180d":35050,"calibration_usable":true,"same_entry_group_id":"R13_HMAE|006110|Stage4B|2024-05-20","dedupe_for_aggregate":true,"aggregate_group_role":"holdout_local_4B","independent_evidence_weight":0.0,"do_not_count_as_new_case":true,"route":"Local4BThenBlockIfNoMarginRefresh","guardrail_lesson":"high-MFE material label can be 4B only while utilization/margin bridge is being refreshed"}
{"row_type":"trigger","selected_round":"R13","selected_loop":9,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL","fine_archetype_id":"C18_EXPORT_REORDER_REAL_BRIDGE_LATE_ENTRY_LOCAL_4B","source_archetype_id":"C18_CONSUMER_EXPORT_CHANNEL_REORDER","symbol":"003230","name":"삼양식품","trigger_type":"Stage4B","entry_date":"2024-06-17","entry_price":686000,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","MFE_30D_pct":4.66,"MAE_30D_pct":-15.31,"MFE_90D_pct":4.66,"MAE_90D_pct":-33.60,"MFE_180D_pct":37.03,"MAE_180D_pct":-33.60,"forward_high_30d":718000,"forward_low_30d":581000,"forward_high_90d":718000,"forward_low_90d":455500,"forward_high_180d":940000,"forward_low_180d":455500,"calibration_usable":true,"same_entry_group_id":"R13_HMAE|003230|Stage4B|2024-06-17","dedupe_for_aggregate":true,"aggregate_group_role":"holdout_real_bridge_4B","independent_evidence_weight":0.0,"do_not_count_as_new_case":true,"route":"Local4B_LateEntryExportBridge","guardrail_lesson":"export bridge was real, but late entry and high MAE require 4B rather than Green"}
{"row_type":"trigger","selected_round":"R13","selected_loop":9,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL","fine_archetype_id":"C18_BRAND_CHANNEL_INVENTORY_LOW_MFE_HIGH_MAE_HARD_4C","source_archetype_id":"C18_CONSUMER_EXPORT_CHANNEL_REORDER","symbol":"383220","name":"F&F","trigger_type":"Stage4C","entry_date":"2024-07-17","entry_price":74000,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","MFE_30D_pct":3.24,"MAE_30D_pct":-33.99,"MFE_90D_pct":3.24,"MAE_90D_pct":-33.99,"MFE_180D_pct":3.24,"MAE_180D_pct":-33.99,"calibration_usable":true,"same_entry_group_id":"R13_HMAE|383220|Stage4C|2024-07-17","dedupe_for_aggregate":true,"aggregate_group_role":"holdout_hard_4C","independent_evidence_weight":0.0,"do_not_count_as_new_case":true,"route":"Hard4C_ChannelInventoryBlock","guardrail_lesson":"brand/export-channel label with low MFE and deep MAE should hard-block without sell-through proof"}
{"row_type":"trigger","selected_round":"R13","selected_loop":9,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL","fine_archetype_id":"C26_OWNED_PLATFORM_LOW_MAE_POSITIVE_CONTROL","source_archetype_id":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE","symbol":"035420","name":"NAVER","trigger_type":"Stage2-Actionable","entry_date":"2024-11-08","entry_price":174600,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","MFE_30D_pct":26.00,"MAE_30D_pct":-1.78,"MFE_90D_pct":34.88,"MAE_90D_pct":-1.78,"MFE_180D_pct":34.88,"MAE_180D_pct":-1.78,"forward_high_30d":220000,"forward_low_30d":171500,"forward_high_90d":235500,"forward_low_90d":171500,"forward_high_180d":235500,"forward_low_180d":171500,"calibration_usable":true,"same_entry_group_id":"R13_HMAE|035420|Stage2-Actionable|2024-11-08","dedupe_for_aggregate":true,"aggregate_group_role":"holdout_positive_control","independent_evidence_weight":0.0,"do_not_count_as_new_case":true,"route":"KeepStage2_BlockHard4C","guardrail_lesson":"owned platform inventory/ARPU bridge with low MAE should not be downgraded to 4C"}
{"row_type":"trigger","selected_round":"R13","selected_loop":9,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL","fine_archetype_id":"C26_LIVE_PLATFORM_HIGH_MAE_LOCAL_4B","source_archetype_id":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE","symbol":"067160","name":"SOOP","trigger_type":"Stage4B","entry_date":"2024-06-20","entry_price":117000,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","MFE_30D_pct":22.91,"MAE_30D_pct":-18.38,"MFE_90D_pct":22.91,"MAE_90D_pct":-26.07,"MFE_180D_pct":22.91,"MAE_180D_pct":-32.82,"forward_high_30d":143800,"forward_low_30d":95500,"forward_high_90d":143800,"forward_low_90d":86500,"forward_high_180d":143800,"forward_low_180d":78600,"calibration_usable":true,"same_entry_group_id":"R13_HMAE|067160|Stage4B|2024-06-20","dedupe_for_aggregate":true,"aggregate_group_role":"holdout_real_platform_4B","independent_evidence_weight":0.0,"do_not_count_as_new_case":true,"route":"Local4B_RequireARPUCreatorRetentionRefresh","guardrail_lesson":"real platform bridge with high MAE should stay local 4B until monetization refresh"}
{"row_type":"trigger","selected_round":"R13","selected_loop":9,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL","fine_archetype_id":"C26_ADTECH_LABEL_HIGH_MAE_HARD_4C","source_archetype_id":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE","symbol":"214270","name":"FSN","trigger_type":"Stage4C","entry_date":"2024-07-18","entry_price":2105,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","MFE_30D_pct":16.63,"MAE_30D_pct":-26.37,"MFE_90D_pct":19.00,"MAE_90D_pct":-26.37,"MFE_180D_pct":19.00,"MAE_180D_pct":-49.64,"forward_high_30d":2455,"forward_low_30d":1550,"forward_high_90d":2505,"forward_low_90d":1550,"forward_high_180d":2505,"forward_low_180d":1060,"calibration_usable":true,"same_entry_group_id":"R13_HMAE|214270|Stage4C|2024-07-18","dedupe_for_aggregate":true,"aggregate_group_role":"holdout_hard_4C","independent_evidence_weight":0.0,"do_not_count_as_new_case":true,"route":"Hard4C_AdtechLabelBlock","guardrail_lesson":"adtech label without owned inventory/ARPU bridge and high MAE should hard-block"}
{"row_type":"trigger","selected_round":"R13","selected_loop":9,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL","fine_archetype_id":"C29_OEM_MIX_MARGIN_LOW_MAE_POSITIVE_CONTROL","source_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","symbol":"000270","name":"기아","trigger_type":"Stage2-Actionable","entry_date":"2024-01-25","entry_price":93000,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","MFE_30D_pct":41.61,"MAE_30D_pct":-7.42,"MFE_90D_pct":45.16,"MAE_90D_pct":-7.42,"MFE_180D_pct":45.16,"MAE_180D_pct":-7.42,"forward_high_30d":131700,"forward_low_30d":86100,"forward_high_90d":135000,"forward_low_90d":86100,"forward_high_180d":135000,"forward_low_180d":86100,"calibration_usable":true,"same_entry_group_id":"R13_HMAE|000270|Stage2-Actionable|2024-01-25","dedupe_for_aggregate":true,"aggregate_group_role":"holdout_positive_control","independent_evidence_weight":0.0,"do_not_count_as_new_case":true,"route":"KeepStage2_BlockHard4C","guardrail_lesson":"OEM volume/mix/margin bridge with controlled MAE should not be routed to hard 4C"}
{"row_type":"trigger","selected_round":"R13","selected_loop":9,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL","fine_archetype_id":"C29_VALUEUP_LABEL_WITHOUT_OPERATING_BRIDGE_CAP","source_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","symbol":"005380","name":"현대차","trigger_type":"Stage2-Watch","entry_date":"2024-08-28","entry_price":259000,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","MFE_30D_pct":3.09,"MAE_30D_pct":-14.48,"MFE_90D_pct":3.09,"MAE_90D_pct":-22.78,"MFE_180D_pct":3.09,"MAE_180D_pct":-32.12,"forward_high_30d":267000,"forward_low_30d":221500,"forward_high_90d":267000,"forward_low_90d":200000,"forward_high_180d":267000,"forward_low_180d":175800,"calibration_usable":true,"same_entry_group_id":"R13_HMAE|005380|Stage2-Watch|2024-08-28","dedupe_for_aggregate":true,"aggregate_group_role":"holdout_stage2_cap","independent_evidence_weight":0.0,"do_not_count_as_new_case":true,"route":"Stage2Cap_C29BridgeMissing","guardrail_lesson":"shareholder-return label may belong elsewhere, but C29 operating bridge did not validate"}
{"row_type":"trigger","selected_round":"R13","selected_loop":9,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL","fine_archetype_id":"C30_WEAK_LIQUIDITY_POLICY_LABEL_HARD_4C","source_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","symbol":"002990","name":"금호건설","trigger_type":"Stage4C","entry_date":"2024-01-26","entry_price":5030,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","MFE_30D_pct":5.00,"MAE_30D_pct":-4.60,"MFE_90D_pct":5.00,"MAE_90D_pct":-27.50,"MFE_180D_pct":5.00,"MAE_180D_pct":-41.00,"forward_high_30d":5280,"forward_low_30d":4800,"forward_high_90d":5280,"forward_low_90d":3650,"forward_high_180d":5280,"forward_low_180d":2970,"calibration_usable":true,"same_entry_group_id":"R13_HMAE|002990|Stage4C|2024-01-26","dedupe_for_aggregate":true,"aggregate_group_role":"holdout_hard_4C","independent_evidence_weight":0.0,"do_not_count_as_new_case":true,"route":"Hard4C_WeakLiquidityBlock","guardrail_lesson":"PF relief label without liquidity/cash bridge and deep MAE should hard-block"}
{"row_type":"trigger","selected_round":"R13","selected_loop":9,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL","fine_archetype_id":"C31_POLICY_CASH_BRIDGE_POSITIVE_CONTROL","source_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","symbol":"373220","name":"LG에너지솔루션","trigger_type":"Stage2-Actionable","entry_date":"2024-07-25","entry_price":332500,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","MFE_30D_pct":18.50,"MAE_30D_pct":-6.47,"MFE_90D_pct":33.53,"MAE_90D_pct":-6.47,"MFE_180D_pct":33.53,"MAE_180D_pct":-6.47,"forward_high_30d":394000,"forward_low_30d":311000,"forward_high_90d":444000,"forward_low_90d":311000,"forward_high_180d":444000,"forward_low_180d":311000,"calibration_usable":true,"same_entry_group_id":"R13_HMAE|373220|Stage2-Actionable|2024-07-25","dedupe_for_aggregate":true,"aggregate_group_role":"holdout_positive_control","independent_evidence_weight":0.0,"do_not_count_as_new_case":true,"route":"KeepStage2_PolicyCashBridge","guardrail_lesson":"policy cash bridge with controlled MAE should not be hard-blocked"}
{"row_type":"trigger","selected_round":"R13","selected_loop":9,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL","fine_archetype_id":"C31_POLICY_LABEL_NO_CASH_BRIDGE_HARD_4C","source_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","symbol":"361610","name":"SK아이이테크놀로지","trigger_type":"Stage4C","entry_date":"2024-05-16","entry_price":57600,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","MFE_30D_pct":1.04,"MAE_30D_pct":-25.87,"MFE_90D_pct":1.04,"MAE_90D_pct":-46.27,"MFE_180D_pct":1.04,"MAE_180D_pct":-60.68,"forward_high_30d":58200,"forward_low_30d":42700,"forward_high_90d":58200,"forward_low_90d":30950,"forward_high_180d":58200,"forward_low_180d":22650,"calibration_usable":true,"same_entry_group_id":"R13_HMAE|361610|Stage4C|2024-05-16","dedupe_for_aggregate":true,"aggregate_group_role":"holdout_hard_4C","independent_evidence_weight":0.0,"do_not_count_as_new_case":true,"route":"Hard4C_PolicyLabelNoCashBridge","guardrail_lesson":"policy label with severe MAE and no utilization/cash bridge should hard-block"}
{"row_type":"trigger","selected_round":"R13","selected_loop":9,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL","fine_archetype_id":"C32_FORMAL_TENDER_POST_RESOLUTION_HIGH_MAE_LOCAL_4B_NOT_HARD_BLOCK","source_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","symbol":"041510","name":"에스엠","trigger_type":"Stage2-Actionable","entry_date":"2023-02-10","entry_price":114700,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","MFE_30D_pct":40.54,"MAE_30D_pct":-6.45,"MFE_90D_pct":40.54,"MAE_90D_pct":-21.10,"MFE_180D_pct":40.54,"MAE_180D_pct":-21.10,"forward_high_30d":161200,"forward_low_30d":107300,"forward_high_90d":161200,"forward_low_90d":90500,"forward_high_180d":161200,"forward_low_180d":90500,"calibration_usable":true,"same_entry_group_id":"R13_HMAE|041510|Stage2-Actionable|2023-02-10","dedupe_for_aggregate":true,"aggregate_group_role":"holdout_tender_positive_4B","independent_evidence_weight":0.0,"do_not_count_as_new_case":true,"route":"KeepStage2_PostResolution4B","guardrail_lesson":"formal tender cash bridge can survive high MAE; post-resolution MAE routes to 4B, not hard 4C"}
```

---

## 5. Case analysis

### 5.1 Doosan Enerbility / 034020 — high MAE local 4B, not hard 4C

The bridge was incomplete but not purely imaginary. Legal/final-contract missing keeps it local 4B.

```text
route = Local4B_NoFinalContractBackfill
```

### 5.2 Woojin Entech / 457550 — supplier spike hard 4C

No contract-scope bridge. Severe MAE confirms hard block.

```text
route = Hard4C_Stage2FalsePositiveBlock
```

### 5.3 KCC / 002380 — positive control

Company-specific margin bridge with controlled MAE should not be hard-blocked.

```text
route = KeepStage2_BlockHard4C
```

### 5.4 Sam-A Aluminium / 006110 — high-MFE 4B then block

This is 4B while utilization/margin bridge is being checked, then block if absent.

```text
route = Local4BThenBlockIfNoMarginRefresh
```

### 5.5 Samyang Foods / 003230 — real bridge, poor entry timing

Bridge is real, but high MAE from late entry keeps it 4B.

```text
route = Local4B_LateEntryExportBridge
```

### 5.6 F&F / 383220 — brand label hard 4C

No sell-through proof and deep MAE.

```text
route = Hard4C_ChannelInventoryBlock
```

### 5.7 NAVER / 035420 — owned platform positive

Low MAE bridge-positive row survives.

```text
route = KeepStage2_BlockHard4C
```

### 5.8 SOOP / 067160 — real platform local 4B

Real platform bridge, but high MAE needs ARPU/retention refresh.

```text
route = Local4B_RequireARPUCreatorRetentionRefresh
```

### 5.9 FSN / 214270 — adtech hard 4C

Adtech label without owned inventory fails.

```text
route = Hard4C_AdtechLabelBlock
```

### 5.10 Kia / 000270 — OEM positive control

OEM volume/mix/margin bridge survives.

```text
route = KeepStage2_BlockHard4C
```

### 5.11 Hyundai Motor / 005380 — Value-up cap

Value-up bridge may belong elsewhere; C29 operating bridge is absent.

```text
route = Stage2Cap_C29BridgeMissing
```

### 5.12 Kumho E&C / 002990 — weak PF hard 4C

Weak liquidity label fails the issuer cash bridge test.

```text
route = Hard4C_WeakLiquidityBlock
```

### 5.13 LG Energy Solution / 373220 — policy cash positive

Policy bridge reached cash. It should not be hard-blocked.

```text
route = KeepStage2_PolicyCashBridge
```

### 5.14 SK IE Technology / 361610 — policy label hard 4C

No utilization/cash bridge, severe MAE.

```text
route = Hard4C_PolicyLabelNoCashBridge
```

### 5.15 SM Entertainment / 041510 — tender drawdown is 4B, not 4C

Tender mechanics were real; post-resolution drawdown becomes local 4B.

```text
route = KeepStage2_PostResolution4B
```

---

## 6. Score-return alignment

```yaml
new_independent_case_count: 0
reused_case_count: 15
new_symbol_count: 0
same_archetype_new_symbol_count: 0
same_archetype_new_trigger_family_count: 0
new_trigger_family_count: 0
calibration_usable_case_count: 15
calibration_usable_trigger_count: 15
positive_control_count: 5
local_4B_or_delayed_watch_count: 5
hard_4C_or_stage2_block_count: 6
stage2_cap_or_reclassification_count: 1
current_profile_error_count: 9
diversity_score_summary: "C04/C15/C18/C26/C29/C30/C31/C32 high-MAE positives, 4B rows, hard 4C rows and caps covered; all rows reused"
loop_contribution_label: duplicate_low_value_loop
do_not_propose_new_weight_delta: true
```

| symbol | source | route | 90D MFE/MAE | 180D MFE/MAE | high-MAE lesson |
|---|---:|---:|---:|---:|---|
| 034020 | C04 | local 4B | +17.65 / -28.71 | +17.65 / -28.71 | incomplete project bridge |
| 457550 | C04 | hard 4C | +32.06 / -58.25 | +32.06 / -58.25 | supplier theme fails |
| 002380 | C15 | keep Stage2 | +20.49 / -7.79 | +41.39 / -7.79 | margin bridge validates |
| 006110 | C15 | 4B -> block | +28.34 / -47.55 | +28.34 / -53.58 | material label needs refresh |
| 003230 | C18 | local 4B | +4.66 / -33.60 | +37.03 / -33.60 | real bridge, late entry |
| 383220 | C18 | hard 4C | +3.24 / -33.99 | +3.24 / -33.99 | channel label fails |
| 035420 | C26 | keep Stage2 | +34.88 / -1.78 | +34.88 / -1.78 | owned inventory validates |
| 067160 | C26 | local 4B | +22.91 / -26.07 | +22.91 / -32.82 | monetization refresh needed |
| 214270 | C26 | hard 4C | +19.00 / -26.37 | +19.00 / -49.64 | adtech label fails |
| 000270 | C29 | keep Stage2 | +45.16 / -7.42 | +45.16 / -7.42 | OEM bridge validates |
| 005380 | C29 | cap | +3.09 / -22.78 | +3.09 / -32.12 | Value-up label lacks C29 bridge |
| 002990 | C30 | hard 4C | +5.00 / -27.50 | +5.00 / -41.00 | PF relief lacks cash |
| 373220 | C31 | keep Stage2 | +33.53 / -6.47 | +33.53 / -6.47 | policy cash bridge validates |
| 361610 | C31 | hard 4C | +1.04 / -46.27 | +1.04 / -60.68 | policy label lacks utilization |
| 041510 | C32 | Stage2 + 4B | +40.54 / -21.10 | +40.54 / -21.10 | tender bridge survives post-resolution drawdown |

---

## 7. Raw component score breakdown

```jsonl
{"row_type":"score_simulation","symbol":"034020","raw_bridge_quality":2,"raw_accounting_trust":1,"raw_mfe_validation":1,"raw_mae_penalty":4,"raw_label_only_risk":3,"stage2_actionable_bonus_before":2.0,"stage2_actionable_bonus_after":1.0,"simulated_route":"Local4B_NoBackfill"}
{"row_type":"score_simulation","symbol":"457550","raw_bridge_quality":0,"raw_accounting_trust":0,"raw_mfe_validation":1,"raw_mae_penalty":5,"raw_label_only_risk":5,"stage2_actionable_bonus_before":2.0,"stage2_actionable_bonus_after":0.0,"simulated_route":"Hard4C_Stage2FalsePositiveBlock"}
{"row_type":"score_simulation","symbol":"002380","raw_bridge_quality":5,"raw_accounting_trust":5,"raw_mfe_validation":4,"raw_mae_penalty":1,"raw_label_only_risk":0,"stage2_actionable_bonus_before":2.0,"stage2_actionable_bonus_after":2.0,"simulated_route":"KeepStage2_BlockHard4C"}
{"row_type":"score_simulation","symbol":"006110","raw_bridge_quality":1,"raw_accounting_trust":1,"raw_mfe_validation":2,"raw_mae_penalty":5,"raw_label_only_risk":4,"stage2_actionable_bonus_before":2.0,"stage2_actionable_bonus_after":1.0,"simulated_route":"Local4BThenBlockIfNoRefresh"}
{"row_type":"score_simulation","symbol":"003230","raw_bridge_quality":4,"raw_accounting_trust":3,"raw_mfe_validation":2,"raw_mae_penalty":4,"raw_label_only_risk":1,"stage2_actionable_bonus_before":2.0,"stage2_actionable_bonus_after":1.0,"simulated_route":"Local4BLateEntry"}
{"row_type":"score_simulation","symbol":"383220","raw_bridge_quality":0,"raw_accounting_trust":0,"raw_mfe_validation":0,"raw_mae_penalty":5,"raw_label_only_risk":5,"stage2_actionable_bonus_before":2.0,"stage2_actionable_bonus_after":0.0,"simulated_route":"Hard4C_ChannelInventoryBlock"}
{"row_type":"score_simulation","symbol":"035420","raw_bridge_quality":5,"raw_accounting_trust":5,"raw_mfe_validation":4,"raw_mae_penalty":0,"raw_label_only_risk":0,"stage2_actionable_bonus_before":2.0,"stage2_actionable_bonus_after":2.0,"simulated_route":"KeepStage2_BlockHard4C"}
{"row_type":"score_simulation","symbol":"067160","raw_bridge_quality":4,"raw_accounting_trust":3,"raw_mfe_validation":3,"raw_mae_penalty":4,"raw_label_only_risk":1,"stage2_actionable_bonus_before":2.0,"stage2_actionable_bonus_after":1.0,"simulated_route":"Local4B_MonetizationRefresh"}
{"row_type":"score_simulation","symbol":"214270","raw_bridge_quality":0,"raw_accounting_trust":0,"raw_mfe_validation":1,"raw_mae_penalty":5,"raw_label_only_risk":5,"stage2_actionable_bonus_before":2.0,"stage2_actionable_bonus_after":0.0,"simulated_route":"Hard4C_AdtechLabel"}
{"row_type":"score_simulation","symbol":"000270","raw_bridge_quality":5,"raw_accounting_trust":5,"raw_mfe_validation":5,"raw_mae_penalty":1,"raw_label_only_risk":0,"stage2_actionable_bonus_before":2.0,"stage2_actionable_bonus_after":2.0,"simulated_route":"KeepStage2_OEMBridge"}
{"row_type":"score_simulation","symbol":"005380","raw_bridge_quality":1,"raw_accounting_trust":1,"raw_mfe_validation":0,"raw_mae_penalty":4,"raw_label_only_risk":4,"stage2_actionable_bonus_before":2.0,"stage2_actionable_bonus_after":0.0,"simulated_route":"Stage2Cap"}
{"row_type":"score_simulation","symbol":"002990","raw_bridge_quality":0,"raw_accounting_trust":0,"raw_mfe_validation":0,"raw_mae_penalty":5,"raw_label_only_risk":5,"stage2_actionable_bonus_before":2.0,"stage2_actionable_bonus_after":0.0,"simulated_route":"Hard4C_WeakLiquidity"}
{"row_type":"score_simulation","symbol":"373220","raw_bridge_quality":5,"raw_accounting_trust":5,"raw_mfe_validation":4,"raw_mae_penalty":1,"raw_label_only_risk":0,"stage2_actionable_bonus_before":2.0,"stage2_actionable_bonus_after":2.0,"simulated_route":"KeepStage2_PolicyCashBridge"}
{"row_type":"score_simulation","symbol":"361610","raw_bridge_quality":0,"raw_accounting_trust":0,"raw_mfe_validation":0,"raw_mae_penalty":5,"raw_label_only_risk":5,"stage2_actionable_bonus_before":2.0,"stage2_actionable_bonus_after":0.0,"simulated_route":"Hard4C_PolicyLabelNoCashBridge"}
{"row_type":"score_simulation","symbol":"041510","raw_bridge_quality":5,"raw_accounting_trust":5,"raw_mfe_validation":4,"raw_mae_penalty":3,"raw_label_only_risk":0,"stage2_actionable_bonus_before":2.0,"stage2_actionable_bonus_after":2.0,"simulated_route":"KeepStage2_PostResolution4B"}
```

---

## 8. Current calibrated profile stress test

The High-MAE route split held:

```text
real bridge + controlled MAE -> keep Stage2
real bridge + high MAE -> local 4B until bridge refresh
label-only + severe MAE -> hard 4C
formal tender + post-resolution MAE -> local 4B, not hard 4C
wrong or missing archetype bridge -> cap/reclassify
later evidence -> no backfill
```

### Rule candidate retained, not newly proposed

```text
R13_HIGH_MAE_BRIDGE_QUALITY_ROUTE_SPLIT_V9_HELD_OUT

if company_specific_cash_bridge == true
and MFE_90D_pct >= +20
and MAE_90D_pct > -10:
    keep_stage2_actionable_bonus = true
    block_hard_4C = true
```

```text
if company_specific_bridge == true
and MAE_90D_pct <= -20
and bridge_refresh_missing == true:
    route = local_4B_watch
    block_stage3_green = true
```

```text
if formal_tender_cash_exit_bridge == true
and post_resolution_MAE == true:
    route = local_4B_watch
    do_not_hard_4C_if_tender_bridge_was_real = true
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

---

## 9. Batch Ingest Self-Audit

```yaml
expected_v12_result_file: true
filename_pattern_pass: true
metadata_filename_consistency: pass
jsonl_trigger_row_count: 15
calibration_usable_trigger_count: 15
representative_trigger_count: 0
new_weight_evidence_candidate_count: 0
guardrail_candidate_count: 15
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
  - R13_HIGH_MAE_BRIDGE_QUALITY_ROUTE_SPLIT_V9_HELD_OUT
existing_axis_weakened: null
one_line_summary: "This loop adds 0 new independent cases and validates the R13 High-MAE bridge-quality route split across C04/C15/C18/C26/C29/C30/C31/C32."
```

---

## 11. Deferred Coding Agent Handoff Prompt

```text
Do not patch production scoring from this MD alone. Treat R13 high-MAE loop 9 as holdout validation only. Batch it with R13 high-MAE loop 8, R13 Stage2 false-positive loops 10~11, R13 accounting-trust loops 11~13, R13 4B/4C loop 103, and source loops C04/C15/C18/C26/C29/C30/C31/C32 from this session. If exact same_entry_group_id rows already exist, dedupe them. Preserve the cross-archetype high-MAE bridge-quality route split, but do not create a new weight delta from this loop because no new independent case was added.
```

---

## 12. Next research state

```yaml
completed_round: R13
completed_loop: 9
selection_basis: docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket: Priority 0
round_schedule_status: coverage_index_selected
round_sector_consistency: pass
next_recommended_archetypes:
  - R13_CROSS_ARCHETYPE_4B_4C_REDTEAM
  - C18_CONSUMER_EXPORT_CHANNEL_REORDER
  - C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE
  - C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE
  - C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK
```
