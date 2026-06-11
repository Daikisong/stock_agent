# E2R v12 R13 cross-archetype residual calibration research

## 0. Execution metadata

```yaml
schema_family: v12_sector_archetype_residual
selected_round: R13
selected_loop: 14
large_sector_id: L10_POLICY_EVENT_CROSS_REDTEAM_MISC
canonical_archetype_id: R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION
fine_archetype_id: HOLDOUT_VALIDATION_ACCOUNTING_TRUST_BRIDGE_PASSPORT_GATE_V14_C04_C15_C18_C26_C29_C30_C31_C32
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
  - cross_archetype_accounting_trust_holdout_validation
  - duplicate_low_value_loop_marker
  - bridge_passport_gate
  - later_evidence_no_backfill_guard
  - no_new_weight_delta
price_source: Songdaiki/stock-web
price_data_source: Songdaiki/stock-web
price_basis: tradable_raw
price_adjustment_status: raw_unadjusted_marcap
stock_web_manifest_max_date: 2026-02-20
production_scoring_changed: false
shadow_weight_only: true
```

R13 is a cross-archetype checkpoint. This file does not perform live discovery, does not patch code, and does not change production scoring. It consolidates the latest current-session holdout rows from C04, C15, C18, C26, C29, C30, C31 and C32 under one accounting-trust question:

```text
Did the trigger have a company-specific bridge that could pass into accounts, cash, or legally executable proceeds?
```

The previous local `R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION` file reached loop 13, so this continuation uses loop 14.

This file is intentionally marked as duplicate-low-value holdout validation. It should be deduped if the same entry groups already exist.

---

## 1. Research thesis

Accounting trust is the bridge passport.

```text
headline = arrival at the border
company-specific bridge = passport
cash / margin / legal execution = entry stamp
```

Across sectors, the same failure repeats:

```text
label exists
price moved
but the bridge did not reach the ledger
```

R13 should not reward that. It should split rows by whether the bridge can be audited.

```text
real bridge + controlled MAE
→ keep Stage2

real bridge + incomplete refresh / high MAE
→ local 4B, no Green

label-only + severe MAE
→ hard 4C

wrong-archetype real bridge
→ cap selected archetype and reclassify

later evidence after trigger
→ new trigger only, no backfill
```

The sector dictionaries used in this holdout pass:

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
  required_cases: 12
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
    - R13 accounting-trust holdout validation
    - cross-archetype bridge-passport gate
    - no-backfill guard
    - local 4B vs hard 4C split
    - no production scoring changes
```

---

## 3. Source validation

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","source_name":"FinanceData/marcap","validation_status":"usable_for_historical_calibration","caveat":"raw/unadjusted OHLC; corporate-action-contaminated windows blocked by default"}
```

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
  - R1/C04 loop 116
  - R4/C15 loop 107
  - R5/C18 loops 146~147
  - R8/C26 loop 104
  - R9/C29 loop 107
  - R10/C30 loop 105
  - R11/C31 loop 107
  - R12/C32 loop 107
  - R13 accounting-trust loops 11~13
  - R13 Stage2 false-positive loop 11
  - R13 high-MAE loop 9
  - R13 4B/4C loop 104
reason:
  - all rows were already calculated from Songdaiki/stock-web tradable raw 1D OHLC
  - current file changes canonical scope to R13 accounting-trust holdout validation
  - exact same_entry_group_id rows should be deduped during batch ingest
  - this file is holdout validation only
```

---

## 4. Trigger rows

```jsonl
{"row_type":"trigger","selected_round":"R13","selected_loop":14,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION","fine_archetype_id":"C04_PREFERRED_BIDDER_NO_FINAL_CONTRACT_LOCAL_4B","source_archetype_id":"C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY","symbol":"034020","name":"두산에너빌리티","trigger_type":"Stage4B","entry_date":"2024-07-17","entry_price":21250,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","MFE_30D_pct":17.65,"MAE_30D_pct":-28.71,"MFE_90D_pct":17.65,"MAE_90D_pct":-28.71,"MFE_180D_pct":17.65,"MAE_180D_pct":-28.71,"forward_high_30d":25000,"forward_low_30d":15150,"forward_high_90d":25000,"forward_low_90d":15150,"forward_high_180d":25000,"forward_low_180d":15150,"calibration_usable":true,"same_entry_group_id":"R13_AT|034020|Stage4B|2024-07-17","dedupe_for_aggregate":true,"aggregate_group_role":"holdout_local_4B","independent_evidence_weight":0.0,"do_not_count_as_new_case":true,"case_role":"project_bridge_incomplete_local_4B","novelty_key":"R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION|034020|Stage4B|2024-07-17","accounting_bridge":"preferred-bidder supply-chain exposure without final contract, legal clearance, order scope or cash bridge at trigger date","route":"Local4B_NoFinalContractBackfill"}
{"row_type":"trigger","selected_round":"R13","selected_loop":14,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION","fine_archetype_id":"C04_SUPPLIER_THEME_NO_CONTRACT_SCOPE_HARD_4C","source_archetype_id":"C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY","symbol":"457550","name":"우진엔텍","trigger_type":"Stage4C","entry_date":"2024-07-18","entry_price":31500,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","MFE_30D_pct":32.06,"MAE_30D_pct":-50.83,"MFE_90D_pct":32.06,"MAE_90D_pct":-58.25,"MFE_180D_pct":32.06,"MAE_180D_pct":-58.25,"forward_high_30d":41600,"forward_low_30d":15490,"forward_high_90d":41600,"forward_low_90d":13150,"forward_high_180d":41600,"forward_low_180d":13150,"calibration_usable":true,"same_entry_group_id":"R13_AT|457550|Stage4C|2024-07-18","dedupe_for_aggregate":true,"aggregate_group_role":"holdout_hard_4C","independent_evidence_weight":0.0,"do_not_count_as_new_case":true,"case_role":"no_contract_scope_hard_4C","novelty_key":"R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION|457550|Stage4C|2024-07-18","accounting_bridge":"small supplier nuclear theme spike without listed-company final contract, order scope or cash bridge","route":"Hard4C_SupplierThemeBlock"}
{"row_type":"trigger","selected_round":"R13","selected_loop":14,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION","fine_archetype_id":"C15_COMPANY_SPECIFIC_MATERIAL_MARGIN_VALIDATED","source_archetype_id":"C15_MATERIAL_SPREAD_SUPERCYCLE","symbol":"002380","name":"KCC","trigger_type":"Stage2-Actionable","entry_date":"2024-01-30","entry_price":244000,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","MFE_30D_pct":17.62,"MAE_30D_pct":-2.46,"MFE_90D_pct":20.49,"MAE_90D_pct":-7.79,"MFE_180D_pct":41.39,"MAE_180D_pct":-7.79,"forward_high_30d":287000,"forward_low_30d":238000,"forward_high_90d":294000,"forward_low_90d":225000,"forward_high_180d":345000,"forward_low_180d":225000,"calibration_usable":true,"same_entry_group_id":"R13_AT|002380|Stage2-Actionable|2024-01-30","dedupe_for_aggregate":true,"aggregate_group_role":"holdout_positive_control","independent_evidence_weight":0.0,"do_not_count_as_new_case":true,"case_role":"accounting_trust_validated","novelty_key":"R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION|002380|Stage2-Actionable|2024-01-30","accounting_bridge":"company-specific materials/silicone/paint margin recovery bridge rather than generic commodity beta","route":"KeepStage2_MaterialMarginBridge"}
{"row_type":"trigger","selected_round":"R13","selected_loop":14,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION","fine_archetype_id":"C15_COMMODITY_LABEL_NO_MARGIN_HARD_4C","source_archetype_id":"C15_MATERIAL_SPREAD_SUPERCYCLE","symbol":"018470","name":"조일알미늄","trigger_type":"Stage4C","entry_date":"2024-05-20","entry_price":2470,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","MFE_30D_pct":7.29,"MAE_30D_pct":-17.41,"MFE_90D_pct":7.29,"MAE_90D_pct":-41.30,"MFE_180D_pct":7.29,"MAE_180D_pct":-44.70,"forward_high_30d":2650,"forward_low_30d":2040,"forward_high_90d":2650,"forward_low_90d":1450,"forward_high_180d":2650,"forward_low_180d":1366,"calibration_usable":true,"same_entry_group_id":"R13_AT|018470|Stage4C|2024-05-20","dedupe_for_aggregate":true,"aggregate_group_role":"holdout_hard_4C","independent_evidence_weight":0.0,"do_not_count_as_new_case":true,"case_role":"no_margin_bridge_hard_4C","novelty_key":"R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION|018470|Stage4C|2024-05-20","accounting_bridge":"aluminium rolling commodity beta label without company-specific ASP, volume, margin or FCF bridge","route":"Hard4C_CommodityLabelBlock"}
{"row_type":"trigger","selected_round":"R13","selected_loop":14,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION","fine_archetype_id":"C18_DTC_EXPORT_VERTICAL_REORDER_BRIDGE_LOCAL_4B","source_archetype_id":"C18_CONSUMER_EXPORT_CHANNEL_REORDER","symbol":"278470","name":"에이피알","trigger_type":"Stage4B","entry_date":"2025-02-27","entry_price":60100,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","MFE_30D_pct":20.63,"MAE_30D_pct":-8.82,"MFE_90D_pct":204.99,"MAE_90D_pct":-8.82,"MFE_180D_pct":365.06,"MAE_180D_pct":-8.82,"calibration_usable":true,"same_entry_group_id":"R13_AT|278470|Stage4B|2025-02-27","dedupe_for_aggregate":true,"aggregate_group_role":"holdout_vertical_4B","independent_evidence_weight":0.0,"do_not_count_as_new_case":true,"case_role":"real_bridge_vertical_4B","novelty_key":"R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION|278470|Stage4B|2025-02-27","accounting_bridge":"DTC/device global channel expansion, overseas demand, revenue and reorder bridge","route":"Local4B_DTCReorderMarginRefresh"}
{"row_type":"trigger","selected_round":"R13","selected_loop":14,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION","fine_archetype_id":"C18_CHANNEL_INVENTORY_NO_REORDER_HARD_4C","source_archetype_id":"C18_CONSUMER_EXPORT_CHANNEL_REORDER","symbol":"383220","name":"F&F","trigger_type":"Stage4C","entry_date":"2024-07-17","entry_price":74000,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","MFE_30D_pct":3.24,"MAE_30D_pct":-33.99,"MFE_90D_pct":3.24,"MAE_90D_pct":-33.99,"MFE_180D_pct":3.24,"MAE_180D_pct":-33.99,"calibration_usable":true,"same_entry_group_id":"R13_AT|383220|Stage4C|2024-07-17","dedupe_for_aggregate":true,"aggregate_group_role":"holdout_hard_4C","independent_evidence_weight":0.0,"do_not_count_as_new_case":true,"case_role":"channel_inventory_hard_4C","novelty_key":"R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION|383220|Stage4C|2024-07-17","accounting_bridge":"apparel/global brand label without sell-through, channel inventory normalization or reorder proof","route":"Hard4C_ChannelInventoryBlock"}
{"row_type":"trigger","selected_round":"R13","selected_loop":14,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION","fine_archetype_id":"C26_OWNED_PLATFORM_ARPU_MARGIN_VALIDATED","source_archetype_id":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE","symbol":"035420","name":"NAVER","trigger_type":"Stage2-Actionable","entry_date":"2024-11-08","entry_price":174600,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","MFE_30D_pct":26.00,"MAE_30D_pct":-1.78,"MFE_90D_pct":34.88,"MAE_90D_pct":-1.78,"MFE_180D_pct":34.88,"MAE_180D_pct":-1.78,"forward_high_30d":220000,"forward_low_30d":171500,"forward_high_90d":235500,"forward_low_90d":171500,"forward_high_180d":235500,"forward_low_180d":171500,"calibration_usable":true,"same_entry_group_id":"R13_AT|035420|Stage2-Actionable|2024-11-08","dedupe_for_aggregate":true,"aggregate_group_role":"holdout_positive_control","independent_evidence_weight":0.0,"do_not_count_as_new_case":true,"case_role":"accounting_trust_validated","novelty_key":"R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION|035420|Stage2-Actionable|2024-11-08","accounting_bridge":"owned search/commerce platform ad inventory, ARPU, commerce conversion and margin leverage bridge","route":"KeepStage2_OwnedPlatformBridge"}
{"row_type":"trigger","selected_round":"R13","selected_loop":14,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION","fine_archetype_id":"C26_ADTECH_NO_OWNED_INVENTORY_HARD_4C","source_archetype_id":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE","symbol":"214270","name":"FSN","trigger_type":"Stage4C","entry_date":"2024-07-18","entry_price":2105,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","MFE_30D_pct":16.63,"MAE_30D_pct":-26.37,"MFE_90D_pct":19.00,"MAE_90D_pct":-26.37,"MFE_180D_pct":19.00,"MAE_180D_pct":-49.64,"forward_high_30d":2455,"forward_low_30d":1550,"forward_high_90d":2505,"forward_low_90d":1550,"forward_high_180d":2505,"forward_low_180d":1060,"calibration_usable":true,"same_entry_group_id":"R13_AT|214270|Stage4C|2024-07-18","dedupe_for_aggregate":true,"aggregate_group_role":"holdout_hard_4C","independent_evidence_weight":0.0,"do_not_count_as_new_case":true,"case_role":"adtech_hard_4C","novelty_key":"R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION|214270|Stage4C|2024-07-18","accounting_bridge":"adtech/marketing service label without owned ad inventory, ARPU, retention, take-rate or durable margin bridge","route":"Hard4C_AdtechLabelBlock"}
{"row_type":"trigger","selected_round":"R13","selected_loop":14,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION","fine_archetype_id":"C29_OEM_MIX_MARGIN_VALIDATED","source_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","symbol":"000270","name":"기아","trigger_type":"Stage2-Actionable","entry_date":"2024-01-25","entry_price":93000,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","MFE_30D_pct":41.61,"MAE_30D_pct":-7.42,"MFE_90D_pct":45.16,"MAE_90D_pct":-7.42,"MFE_180D_pct":45.16,"MAE_180D_pct":-7.42,"forward_high_30d":131700,"forward_low_30d":86100,"forward_high_90d":135000,"forward_low_90d":86100,"forward_high_180d":135000,"forward_low_180d":86100,"calibration_usable":true,"same_entry_group_id":"R13_AT|000270|Stage2-Actionable|2024-01-25","dedupe_for_aggregate":true,"aggregate_group_role":"holdout_positive_control","independent_evidence_weight":0.0,"do_not_count_as_new_case":true,"case_role":"accounting_trust_validated","novelty_key":"R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION|000270|Stage2-Actionable|2024-01-25","accounting_bridge":"OEM volume, product mix, ASP, margin and shareholder-return bridge","route":"KeepStage2_OEMMarginBridge"}
{"row_type":"trigger","selected_round":"R13","selected_loop":14,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION","fine_archetype_id":"C29_VALUEUP_NO_OPERATING_BRIDGE_CAP","source_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","symbol":"005380","name":"현대차","trigger_type":"Stage2","entry_date":"2024-08-28","entry_price":259000,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","MFE_30D_pct":3.09,"MAE_30D_pct":-14.48,"MFE_90D_pct":3.09,"MAE_90D_pct":-22.78,"MFE_180D_pct":3.09,"MAE_180D_pct":-32.12,"forward_high_30d":267000,"forward_low_30d":221500,"forward_high_90d":267000,"forward_low_90d":200000,"forward_high_180d":267000,"forward_low_180d":175800,"calibration_usable":true,"same_entry_group_id":"R13_AT|005380|Stage2|2024-08-28","dedupe_for_aggregate":true,"aggregate_group_role":"holdout_stage2_cap","independent_evidence_weight":0.0,"do_not_count_as_new_case":true,"case_role":"selected_bridge_missing_cap","novelty_key":"R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION|005380|Stage2|2024-08-28","accounting_bridge":"shareholder-return intent existed, but C29 volume/mix/margin operating bridge did not validate","route":"Stage2Cap_C29BridgeMissing"}
{"row_type":"trigger","selected_round":"R13","selected_loop":14,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION","fine_archetype_id":"C30_DELAYED_PF_CASH_BRIDGE_LOCAL_4B_NO_BACKFILL","source_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","symbol":"294870","name":"HDC현대산업개발","trigger_type":"Stage4B","entry_date":"2024-05-13","entry_price":17920,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","MFE_30D_pct":2.12,"MAE_30D_pct":-6.58,"MFE_90D_pct":37.28,"MAE_90D_pct":-6.58,"MFE_180D_pct":57.37,"MAE_180D_pct":-6.58,"forward_high_30d":18300,"forward_low_30d":16740,"forward_high_90d":24600,"forward_low_90d":16740,"forward_high_180d":28200,"forward_low_180d":16740,"calibration_usable":true,"same_entry_group_id":"R13_AT|294870|Stage4B|2024-05-13","dedupe_for_aggregate":true,"aggregate_group_role":"holdout_delayed_4B","independent_evidence_weight":0.0,"do_not_count_as_new_case":true,"case_role":"delayed_cash_bridge_local_4B","novelty_key":"R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION|294870|Stage4B|2024-05-13","accounting_bridge":"delayed PF/housing soft-landing path, but issuer-specific refinancing/liquidity bridge not visible at entry","route":"DelayedLocal4B_NoBackfill"}
{"row_type":"trigger","selected_round":"R13","selected_loop":14,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION","fine_archetype_id":"C30_WEAK_LIQUIDITY_NO_CASH_BRIDGE_HARD_4C","source_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","symbol":"002990","name":"금호건설","trigger_type":"Stage4C","entry_date":"2024-01-26","entry_price":5030,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","MFE_30D_pct":5.00,"MAE_30D_pct":-4.60,"MFE_90D_pct":5.00,"MAE_90D_pct":-27.50,"MFE_180D_pct":5.00,"MAE_180D_pct":-41.00,"forward_high_30d":5280,"forward_low_30d":4800,"forward_high_90d":5280,"forward_low_90d":3650,"forward_high_180d":5280,"forward_low_180d":2970,"calibration_usable":true,"same_entry_group_id":"R13_AT|002990|Stage4C|2024-01-26","dedupe_for_aggregate":true,"aggregate_group_role":"holdout_hard_4C","independent_evidence_weight":0.0,"do_not_count_as_new_case":true,"case_role":"weak_liquidity_hard_4C","novelty_key":"R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION|002990|Stage4C|2024-01-26","accounting_bridge":"PF relief vocabulary without liquidity, debt-service, guarantee relief or cash bridge","route":"Hard4C_WeakLiquidityBlock"}
{"row_type":"trigger","selected_round":"R13","selected_loop":14,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION","fine_archetype_id":"C31_POLICY_CASH_BRIDGE_VALIDATED","source_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","symbol":"373220","name":"LG에너지솔루션","trigger_type":"Stage2-Actionable","entry_date":"2024-07-25","entry_price":332500,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","MFE_30D_pct":18.50,"MAE_30D_pct":-6.47,"MFE_90D_pct":33.53,"MAE_90D_pct":-6.47,"MFE_180D_pct":33.53,"MAE_180D_pct":-6.47,"forward_high_30d":394000,"forward_low_30d":311000,"forward_high_90d":444000,"forward_low_90d":311000,"forward_high_180d":444000,"forward_low_180d":311000,"calibration_usable":true,"same_entry_group_id":"R13_AT|373220|Stage2-Actionable|2024-07-25","dedupe_for_aggregate":true,"aggregate_group_role":"holdout_positive_control","independent_evidence_weight":0.0,"do_not_count_as_new_case":true,"case_role":"policy_cash_bridge_validated","novelty_key":"R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION|373220|Stage2-Actionable|2024-07-25","accounting_bridge":"IRA/AMPC support plus customer diversification, utilization and ESS/non-EV demand bridge","route":"KeepStage2_PolicyCashBridge"}
{"row_type":"trigger","selected_round":"R13","selected_loop":14,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION","fine_archetype_id":"C31_POLICY_LABEL_NO_CASH_BRIDGE_HARD_4C","source_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","symbol":"361610","name":"SK아이이테크놀로지","trigger_type":"Stage4C","entry_date":"2024-05-16","entry_price":57600,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","MFE_30D_pct":1.04,"MAE_30D_pct":-25.87,"MFE_90D_pct":1.04,"MAE_90D_pct":-46.27,"MFE_180D_pct":1.04,"MAE_180D_pct":-60.68,"forward_high_30d":58200,"forward_low_30d":42700,"forward_high_90d":58200,"forward_low_90d":30950,"forward_high_180d":58200,"forward_low_180d":22650,"calibration_usable":true,"same_entry_group_id":"R13_AT|361610|Stage4C|2024-05-16","dedupe_for_aggregate":true,"aggregate_group_role":"holdout_hard_4C","independent_evidence_weight":0.0,"do_not_count_as_new_case":true,"case_role":"policy_label_hard_4C","novelty_key":"R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION|361610|Stage4C|2024-05-16","accounting_bridge":"separator/material policy exposure without customer pull, utilization, parent financing or cash-conversion bridge","route":"Hard4C_PolicyLabelNoCashBridge"}
{"row_type":"trigger","selected_round":"R13","selected_loop":14,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION","fine_archetype_id":"C32_FORMAL_TENDER_CASH_EXIT_VALIDATED_POST_RESOLUTION_4B","source_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","symbol":"041510","name":"에스엠","trigger_type":"Stage4B","entry_date":"2023-02-10","entry_price":114700,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","MFE_30D_pct":40.54,"MAE_30D_pct":-6.45,"MFE_90D_pct":40.54,"MAE_90D_pct":-21.10,"MFE_180D_pct":40.54,"MAE_180D_pct":-21.10,"forward_high_30d":161200,"forward_low_30d":107300,"forward_high_90d":161200,"forward_low_90d":90500,"forward_high_180d":161200,"forward_low_180d":90500,"calibration_usable":true,"same_entry_group_id":"R13_AT|041510|Stage4B|2023-02-10","dedupe_for_aggregate":true,"aggregate_group_role":"holdout_tender_4B","independent_evidence_weight":0.0,"do_not_count_as_new_case":true,"case_role":"cash_exit_validated_post_resolution_4B","novelty_key":"R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION|041510|Stage4B|2023-02-10","accounting_bridge":"formal tender/control contest cash path with visible minority exit mechanics","route":"PostResolutionLocal4B"}
{"row_type":"trigger","selected_round":"R13","selected_loop":14,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION","fine_archetype_id":"C32_CONTROL_SALE_NO_MINORITY_EXIT_HARD_4C","source_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","symbol":"040300","name":"YTN","trigger_type":"Stage4C","entry_date":"2023-10-24","entry_price":7800,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","MFE_30D_pct":23.08,"MAE_30D_pct":-30.64,"MFE_90D_pct":23.08,"MAE_90D_pct":-30.64,"MFE_180D_pct":23.08,"MAE_180D_pct":-49.29,"forward_high_30d":9600,"forward_low_30d":5410,"forward_high_90d":9600,"forward_low_90d":5410,"forward_high_180d":9600,"forward_low_180d":3955,"calibration_usable":true,"same_entry_group_id":"R13_AT|040300|Stage4C|2023-10-24","dedupe_for_aggregate":true,"aggregate_group_role":"holdout_hard_4C","independent_evidence_weight":0.0,"do_not_count_as_new_case":true,"case_role":"control_sale_no_cash_exit_hard_4C","novelty_key":"R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION|040300|Stage4C|2023-10-24","accounting_bridge":"control-sale headline without public minority tender, appraisal or squeeze-out cash path","route":"Hard4C_NoMinorityCashExit"}
```

---

## 5. Case analysis

### 5.1 Accounting-trust positive controls

```yaml
positive_controls:
  - 002380: material margin bridge reached company economics.
  - 035420: owned platform ARPU/margin bridge.
  - 000270: OEM volume/mix/margin bridge.
  - 373220: policy-to-company cash bridge.
```

These rows remind the guardrail not to over-block. They carry a real bridge into accounts.

### 5.2 Local 4B rows

```yaml
local_4B_rows:
  - 034020: project bridge potential but final contract missing.
  - 278470: DTC/device export bridge requires reorder/margin refresh.
  - 005380: selected C29 operating bridge missing; cap and reclassification possible.
  - 294870: delayed PF validation; no backfill.
  - 041510: formal tender existed, but post-resolution window requires 4B.
```

These are inspection-bay rows. They are not clean Green; they are also not all thesis-breaks.

### 5.3 Hard 4C rows

```yaml
hard_4C_rows:
  - 457550: supplier theme without listed-company contract scope.
  - 018470: commodity beta without company spread bridge.
  - 383220: channel inventory / brand label without reorder.
  - 214270: adtech label without owned inventory.
  - 002990: PF label without issuer cash.
  - 361610: policy label without utilization or cash.
  - 040300: control sale without minority cash-exit.
```

These rows do not have a bridge passport. The price path then turns a missing passport into a hard block.

---

## 6. Score-return alignment

```yaml
new_independent_case_count: 0
reused_case_count: 16
new_symbol_count: 0
same_archetype_new_symbol_count: 0
same_archetype_new_trigger_family_count: 0
new_trigger_family_count: 0
calibration_usable_case_count: 16
calibration_usable_trigger_count: 16
positive_control_count: 4
local_4B_or_stage2_cap_count: 5
hard_4C_count: 7
wrong_archetype_reclassification_count: 1
current_profile_error_count: 9
diversity_score_summary: "C04/C15/C18/C26/C29/C30/C31/C32 accounting-trust positives, 4B rows, hard 4C rows and cap/reclassification rows covered; all rows reused"
loop_contribution_label: duplicate_low_value_loop
do_not_propose_new_weight_delta: true
```

| symbol | source | route | 90D MFE/MAE | 180D MFE/MAE | accounting-trust lesson |
|---|---:|---:|---:|---:|---|
| 034020 | C04 | 4B | +17.65 / -28.71 | +17.65 / -28.71 | no final contract bridge |
| 457550 | C04 | 4C | +32.06 / -58.25 | +32.06 / -58.25 | supplier theme lacks contract economics |
| 002380 | C15 | keep Stage2 | +20.49 / -7.79 | +41.39 / -7.79 | margin bridge validates |
| 018470 | C15 | 4C | +7.29 / -41.30 | +7.29 / -44.70 | commodity beta lacks spread bridge |
| 278470 | C18 | 4B | +204.99 / -8.82 | +365.06 / -8.82 | DTC bridge needs refresh |
| 383220 | C18 | 4C | +3.24 / -33.99 | +3.24 / -33.99 | channel inventory fails |
| 035420 | C26 | keep Stage2 | +34.88 / -1.78 | +34.88 / -1.78 | owned platform validates |
| 214270 | C26 | 4C | +19.00 / -26.37 | +19.00 / -49.64 | adtech label fails |
| 000270 | C29 | keep Stage2 | +45.16 / -7.42 | +45.16 / -7.42 | OEM bridge validates |
| 005380 | C29 | cap | +3.09 / -22.78 | +3.09 / -32.12 | Value-up label lacks C29 bridge |
| 294870 | C30 | 4B | +37.28 / -6.58 | +57.37 / -6.58 | delayed PF, no backfill |
| 002990 | C30 | 4C | +5.00 / -27.50 | +5.00 / -41.00 | issuer cash absent |
| 373220 | C31 | keep Stage2 | +33.53 / -6.47 | +33.53 / -6.47 | policy cash validates |
| 361610 | C31 | 4C | +1.04 / -46.27 | +1.04 / -60.68 | policy label lacks cash |
| 041510 | C32 | 4B | +40.54 / -21.10 | +40.54 / -21.10 | tender bridge then post-resolution 4B |
| 040300 | C32 | 4C | +23.08 / -30.64 | +23.08 / -49.29 | control sale lacks minority exit |

---

## 7. Raw component score breakdown

```jsonl
{"row_type":"score_simulation","symbol":"034020","raw_bridge_quality":2,"raw_accounting_trust":1,"raw_cash_or_margin_bridge":1,"raw_legal_execution":1,"raw_price_validation":1,"raw_label_only_risk":3,"stage2_actionable_bonus_before":2.0,"stage2_actionable_bonus_after":1.0,"simulated_route":"Local4B_NoFinalContractBackfill"}
{"row_type":"score_simulation","symbol":"457550","raw_bridge_quality":0,"raw_accounting_trust":0,"raw_cash_or_margin_bridge":0,"raw_legal_execution":0,"raw_price_validation":0,"raw_label_only_risk":5,"stage2_actionable_bonus_before":2.0,"stage2_actionable_bonus_after":0.0,"simulated_route":"Hard4C_SupplierThemeBlock"}
{"row_type":"score_simulation","symbol":"002380","raw_bridge_quality":5,"raw_accounting_trust":5,"raw_cash_or_margin_bridge":5,"raw_legal_execution":0,"raw_price_validation":4,"raw_label_only_risk":0,"stage2_actionable_bonus_before":2.0,"stage2_actionable_bonus_after":2.0,"simulated_route":"KeepStage2_MaterialMargin"}
{"row_type":"score_simulation","symbol":"018470","raw_bridge_quality":0,"raw_accounting_trust":0,"raw_cash_or_margin_bridge":0,"raw_legal_execution":0,"raw_price_validation":0,"raw_label_only_risk":5,"stage2_actionable_bonus_before":2.0,"stage2_actionable_bonus_after":0.0,"simulated_route":"Hard4C_CommodityLabel"}
{"row_type":"score_simulation","symbol":"278470","raw_bridge_quality":5,"raw_accounting_trust":4,"raw_cash_or_margin_bridge":4,"raw_legal_execution":0,"raw_price_validation":5,"raw_label_only_risk":0,"stage2_actionable_bonus_before":2.0,"stage2_actionable_bonus_after":2.0,"simulated_route":"Local4B_DTCRefresh"}
{"row_type":"score_simulation","symbol":"383220","raw_bridge_quality":0,"raw_accounting_trust":0,"raw_cash_or_margin_bridge":0,"raw_legal_execution":0,"raw_price_validation":0,"raw_label_only_risk":5,"stage2_actionable_bonus_before":2.0,"stage2_actionable_bonus_after":0.0,"simulated_route":"Hard4C_ChannelInventory"}
{"row_type":"score_simulation","symbol":"035420","raw_bridge_quality":5,"raw_accounting_trust":5,"raw_cash_or_margin_bridge":5,"raw_legal_execution":0,"raw_price_validation":4,"raw_label_only_risk":0,"stage2_actionable_bonus_before":2.0,"stage2_actionable_bonus_after":2.0,"simulated_route":"KeepStage2_OwnedPlatform"}
{"row_type":"score_simulation","symbol":"214270","raw_bridge_quality":0,"raw_accounting_trust":0,"raw_cash_or_margin_bridge":0,"raw_legal_execution":0,"raw_price_validation":0,"raw_label_only_risk":5,"stage2_actionable_bonus_before":2.0,"stage2_actionable_bonus_after":0.0,"simulated_route":"Hard4C_AdtechNoInventory"}
{"row_type":"score_simulation","symbol":"000270","raw_bridge_quality":5,"raw_accounting_trust":5,"raw_cash_or_margin_bridge":5,"raw_legal_execution":0,"raw_price_validation":5,"raw_label_only_risk":0,"stage2_actionable_bonus_before":2.0,"stage2_actionable_bonus_after":2.0,"simulated_route":"KeepStage2_OEMMargin"}
{"row_type":"score_simulation","symbol":"005380","raw_bridge_quality":1,"raw_accounting_trust":1,"raw_cash_or_margin_bridge":1,"raw_legal_execution":0,"raw_price_validation":0,"raw_label_only_risk":4,"stage2_actionable_bonus_before":2.0,"stage2_actionable_bonus_after":0.0,"simulated_route":"Stage2Cap_ReclassifyIfCapitalBridge"}
{"row_type":"score_simulation","symbol":"294870","raw_bridge_quality":2,"raw_accounting_trust":2,"raw_cash_or_margin_bridge":2,"raw_legal_execution":0,"raw_price_validation":3,"raw_label_only_risk":2,"stage2_actionable_bonus_before":2.0,"stage2_actionable_bonus_after":1.0,"simulated_route":"DelayedLocal4B_NoBackfill"}
{"row_type":"score_simulation","symbol":"002990","raw_bridge_quality":0,"raw_accounting_trust":0,"raw_cash_or_margin_bridge":0,"raw_legal_execution":0,"raw_price_validation":0,"raw_label_only_risk":5,"stage2_actionable_bonus_before":2.0,"stage2_actionable_bonus_after":0.0,"simulated_route":"Hard4C_WeakLiquidity"}
{"row_type":"score_simulation","symbol":"373220","raw_bridge_quality":5,"raw_accounting_trust":5,"raw_cash_or_margin_bridge":5,"raw_legal_execution":0,"raw_price_validation":4,"raw_label_only_risk":0,"stage2_actionable_bonus_before":2.0,"stage2_actionable_bonus_after":2.0,"simulated_route":"KeepStage2_PolicyCash"}
{"row_type":"score_simulation","symbol":"361610","raw_bridge_quality":0,"raw_accounting_trust":0,"raw_cash_or_margin_bridge":0,"raw_legal_execution":0,"raw_price_validation":0,"raw_label_only_risk":5,"stage2_actionable_bonus_before":2.0,"stage2_actionable_bonus_after":0.0,"simulated_route":"Hard4C_PolicyLabelNoCash"}
{"row_type":"score_simulation","symbol":"041510","raw_bridge_quality":5,"raw_accounting_trust":5,"raw_cash_or_margin_bridge":0,"raw_legal_execution":5,"raw_price_validation":4,"raw_label_only_risk":0,"stage2_actionable_bonus_before":2.0,"stage2_actionable_bonus_after":2.0,"simulated_route":"PostResolutionLocal4B"}
{"row_type":"score_simulation","symbol":"040300","raw_bridge_quality":0,"raw_accounting_trust":0,"raw_cash_or_margin_bridge":0,"raw_legal_execution":0,"raw_price_validation":0,"raw_label_only_risk":5,"stage2_actionable_bonus_before":2.0,"stage2_actionable_bonus_after":0.0,"simulated_route":"Hard4C_NoMinorityCashExit"}
```

---

## 8. Current calibrated profile stress test

The accounting-trust bridge-passport gate held:

```text
company-specific bridge at trigger date
→ Stage2 can survive

bridge exists but refresh missing
→ local 4B, no Green

label-only or price-only spike
→ hard 4C when MAE confirms failure

wrong bridge for selected archetype
→ cap and reclassify

later evidence
→ no backfill; require new trigger row
```

### Rule candidate retained, not newly proposed

```text
R13_ACCOUNTING_TRUST_BRIDGE_PASSPORT_GATE_V14_HELD_OUT

if trigger_label_exists == true
and company_specific_accounting_bridge_at_trigger_date == false:
    stage2_actionable_bonus = 0
    max_stage = Stage2-Watch
```

```text
if company_specific_accounting_bridge_at_trigger_date == true
and MFE_90D_pct >= +20
and MAE_90D_pct > -10:
    keep_stage2_actionable_bonus = true
```

```text
if company_specific_bridge == true
and bridge_refresh_missing == true:
    route = local_4B_watch
    block_stage3_green = true
```

```text
if label_only_or_price_only_spike == true
and MAE_90D_pct <= -25:
    route = hard_4C_or_Stage2_FalsePositive_Block
```

```text
if later_evidence_after_trigger == true:
    do_not_backfill_to_original_trigger = true
    require_new_trigger_from_later_evidence_date = true
```

---

## 9. Coverage matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive_case_count | counterexample_count | 4B_case_count | 4C_case_count | new_independent_case_count | reused_case_count | calibration_usable_trigger_count | representative_trigger_count | current_profile_error_count | sector_rule_candidate | canonical_rule_candidate |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| L10_POLICY_EVENT_CROSS_REDTEAM_MISC | R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION | ACCOUNTING_TRUST_BRIDGE_PASSPORT_GATE_V14 | 4 | 7 | 5 | 7 | 0 | 16 | 16 | 0 | 9 | false | false |

---

## 10. Batch Ingest Self-Audit

```yaml
expected_v12_result_file: true
filename_pattern_pass: true
metadata_filename_consistency: pass
jsonl_trigger_row_count: 16
calibration_usable_trigger_count: 16
representative_trigger_count: 0
new_weight_evidence_candidate_count: 0
guardrail_candidate_count: 16
narrative_only_or_rejected_count: 0
rows_missing_required_mfe_mae: 0
rows_missing_entry_price_or_date: 0
rows_with_noncanonical_trigger_type: 0
rows_with_compact_mfe_mae_alias_only: 0
ready_for_batch_ingest: true
batch_ingest_recommendation: dedupe_as_holdout_validation_only
```

---

## 11. Residual contribution summary

```yaml
new_independent_case_count: 0
reused_case_count: 16
new_symbol_count: 0
new_trigger_family_count: 0
tested_existing_calibrated_axes:
  - stage2_required_bridge
  - local_4b_watch_guard
  - hard_4c_thesis_break_routes_to_4c
  - no_backfill_later_evidence
  - accounting_trust_bridge_passport_gate
residual_error_types_found:
  - label_without_ledger_bridge
  - price_only_or_theme_spike
  - wrong_archetype_bridge
  - later_evidence_backfill_risk
new_axis_proposed: null
existing_axis_strengthened:
  - R13_ACCOUNTING_TRUST_BRIDGE_PASSPORT_GATE_V14_HELD_OUT
existing_axis_weakened: null
sector_specific_rule_candidate: false
canonical_archetype_rule_candidate: false
cross_archetype_rule_candidate: false
holdout_validation_passed: true
loop_contribution_label: duplicate_low_value_loop
do_not_propose_new_weight_delta: true
```

```jsonl
{"row_type":"residual_contribution","round":"R13","loop":"14","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION","new_independent_case_count":0,"reused_case_count":16,"new_symbol_count":0,"new_trigger_family_count":0,"tested_existing_calibrated_axes":["stage2_required_bridge","local_4b_watch_guard","hard_4c_thesis_break_routes_to_4c","no_backfill_later_evidence","accounting_trust_bridge_passport_gate"],"residual_error_types_found":["label_without_ledger_bridge","price_only_or_theme_spike","wrong_archetype_bridge","later_evidence_backfill_risk"],"loop_contribution_label":"duplicate_low_value_loop","do_not_propose_new_weight_delta":true}
```

---

## 12. Deferred Coding Agent Handoff Prompt

```text
Do not patch production scoring from this MD alone. Treat R13 accounting-trust loop 14 as holdout validation only. Batch it with R13 accounting-trust loops 11~13, R13 Stage2 false-positive loop 11, R13 high-MAE loop 9, R13 4B/4C loop 104, and source loops C04/C15/C18/C26/C29/C30/C31/C32 from this session. If exact same_entry_group_id rows already exist, dedupe them. Preserve the cross-archetype accounting-trust bridge-passport gate, but do not create a new weight delta from this loop because no new independent case was added.
```

---

## 13. Next research state

```yaml
completed_round: R13
completed_loop: 14
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
