# E2R v12 R13 cross-archetype residual calibration research

## 0. Execution metadata

```yaml
schema_family: v12_sector_archetype_residual
selected_round: R13
selected_loop: 13
large_sector_id: L10_POLICY_EVENT_CROSS_REDTEAM_MISC
canonical_archetype_id: R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION
fine_archetype_id: HOLDOUT_VALIDATION_BRIDGE_PASSPORT_GATE_C04_C15_C18_C26_C29_C30_C31_C32
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
  - cross_archetype_holdout_validation
  - accounting_trust_bridge_passport_gate
  - duplicate_low_value_loop_marker
  - no_new_weight_delta
price_source: Songdaiki/stock-web
price_data_source: Songdaiki/stock-web
price_basis: tradable_raw
price_adjustment_status: raw_unadjusted_marcap
stock_web_manifest_max_date: 2026-02-20
production_scoring_changed: false
shadow_weight_only: true
```

R13 is a cross-archetype checkpoint. This file does not perform live discovery and does not patch scoring. It consolidates the latest current-session holdout rows from C04, C15, C18, C26, C29, C30, C31 and C32 under one accounting-trust question:

```text
Does the trigger have a company-specific cash bridge that can pass through the ledger?
```

The previous local accounting-trust file reached `R13/R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION loop 12`, so this file uses `loop 13`.

---

## 1. Research thesis

The accounting-trust gate should behave like a passport control.

```text
headline = arrival at the border
bridge = passport
cash conversion = entry stamp
```

A row can have strong language and even strong MFE, but without a company-specific bridge it should not receive Stage2 credit. Across sectors, the same question repeats:

```text
C04 nuclear:
preferred bidder -> final contract / legal clearance / order scope / cash?

C15 materials:
material label -> ASP / utilization / margin / FCF?

C18 consumer:
export channel -> sell-through / reorder / inventory quality / margin?

C26 platform:
platform/ad label -> owned inventory / ARPU / retention / margin leverage?

C29 mobility:
mobility/value-up label -> volume / mix / ASP / customer order / margin?

C30 construction:
PF relief -> issuer refinancing / guarantee relief / presale / debt service?

C31 policy:
policy umbrella -> company cash bridge?

C32 governance:
shareholder-friendly cash -> formal tender / appraisal / squeeze-out / minority cash-exit?
```

This loop is deliberately marked as holdout validation. It reuses existing stock-web-derived rows from the current session. Its contribution is not new independent weight. Its value is route consistency:

```text
real bridge + controlled MAE -> keep Stage2
real bridge + refresh missing -> local 4B
label-only + severe MAE -> hard 4C
wrong archetype bridge -> reclassify
later evidence -> no backfill
```

---

## 2. Validation scope

```yaml
validation_scope:
  required_cases: 10
  actual_trigger_rows: 12
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
    - wrong-archetype reclassification guard
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
  - R5/C18 loop 145
  - R8/C26 loop 102
  - R9/C29 loop 105
  - R10/C30 loop 103
  - R11/C31 loop 105
  - R12/C32 loop 105
  - R13 accounting-trust loops 11~12
  - R13 Stage2 false-positive loop 10
  - R13 high-MAE loop 8
  - R13 4B/4C loop 103
reason:
  - rows were already calculated from Songdaiki/stock-web tradable raw 1D OHLC
  - current file changes canonical scope to R13 accounting-trust holdout validation
  - exact same_entry_group_id rows should be deduped during batch ingest
  - this file is holdout validation only
```

---

## 4. Trigger rows

```jsonl
{"row_type":"trigger","selected_round":"R13","selected_loop":13,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION","fine_archetype_id":"C04_PREFERRED_BIDDER_BRIDGE_INCOMPLETE_LOCAL_4B","source_archetype_id":"C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY","symbol":"034020","name":"두산에너빌리티","trigger_type":"Stage2-Watch","entry_date":"2024-07-17","entry_price":21250,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","MFE_30D_pct":17.65,"MAE_30D_pct":-28.71,"MFE_90D_pct":17.65,"MAE_90D_pct":-28.71,"MFE_180D_pct":17.65,"MAE_180D_pct":-28.71,"forward_high_30d":25000,"forward_low_30d":15150,"forward_high_90d":25000,"forward_low_90d":15150,"forward_high_180d":25000,"forward_low_180d":15150,"calibration_usable":true,"same_entry_group_id":"R13_AT|034020|Stage2-Watch|2024-07-17","dedupe_for_aggregate":true,"aggregate_group_role":"holdout_local_4B","independent_evidence_weight":0.0,"do_not_count_as_new_case":true,"case_role":"bridge_incomplete_local_4B","novelty_key":"R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION|034020|Stage2-Watch|2024-07-17","accounting_bridge":"preferred-bidder supply-chain exposure without final contract, legal clearance, order-scope or cash bridge at trigger date","route":"Local4B_NoFinalContractBackfill"}
{"row_type":"trigger","selected_round":"R13","selected_loop":13,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION","fine_archetype_id":"C04_SUPPLIER_THEME_NO_CONTRACT_SCOPE_HARD_4C","source_archetype_id":"C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY","symbol":"457550","name":"우진엔텍","trigger_type":"Stage4C","entry_date":"2024-07-18","entry_price":31500,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","MFE_30D_pct":32.06,"MAE_30D_pct":-50.83,"MFE_90D_pct":32.06,"MAE_90D_pct":-58.25,"MFE_180D_pct":32.06,"MAE_180D_pct":-58.25,"forward_high_30d":41600,"forward_low_30d":15490,"forward_high_90d":41600,"forward_low_90d":13150,"forward_high_180d":41600,"forward_low_180d":13150,"calibration_usable":true,"same_entry_group_id":"R13_AT|457550|Stage4C|2024-07-18","dedupe_for_aggregate":true,"aggregate_group_role":"holdout_hard_4C","independent_evidence_weight":0.0,"do_not_count_as_new_case":true,"case_role":"accounting_trust_absent_hard_block","novelty_key":"R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION|457550|Stage4C|2024-07-18","accounting_bridge":"small supplier nuclear theme spike without listed-company final-contract, order scope or cash bridge","route":"Hard4C_SupplierThemeBlock"}
{"row_type":"trigger","selected_round":"R13","selected_loop":13,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION","fine_archetype_id":"C15_COMPANY_SPECIFIC_MARGIN_BRIDGE_VALIDATED","source_archetype_id":"C15_MATERIAL_SPREAD_SUPERCYCLE","symbol":"002380","name":"KCC","trigger_type":"Stage2-Actionable","entry_date":"2024-01-30","entry_price":244000,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","MFE_30D_pct":17.62,"MAE_30D_pct":-2.46,"MFE_90D_pct":20.49,"MAE_90D_pct":-7.79,"MFE_180D_pct":41.39,"MAE_180D_pct":-7.79,"forward_high_30d":287000,"forward_low_30d":238000,"forward_high_90d":294000,"forward_low_90d":225000,"forward_high_180d":345000,"forward_low_180d":225000,"calibration_usable":true,"same_entry_group_id":"R13_AT|002380|Stage2-Actionable|2024-01-30","dedupe_for_aggregate":true,"aggregate_group_role":"holdout_positive_control","independent_evidence_weight":0.0,"do_not_count_as_new_case":true,"case_role":"accounting_trust_validated","novelty_key":"R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION|002380|Stage2-Actionable|2024-01-30","accounting_bridge":"company-specific materials/silicone/paint margin recovery bridge rather than generic commodity beta","route":"KeepStage2_MaterialMarginBridge"}
{"row_type":"trigger","selected_round":"R13","selected_loop":13,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION","fine_archetype_id":"C15_FOIL_LABEL_NO_UTILIZATION_REFRESH_LOCAL_4B","source_archetype_id":"C15_MATERIAL_SPREAD_SUPERCYCLE","symbol":"006110","name":"삼아알미늄","trigger_type":"Stage4B","entry_date":"2024-05-20","entry_price":75500,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","MFE_30D_pct":28.34,"MAE_30D_pct":-7.28,"MFE_90D_pct":28.34,"MAE_90D_pct":-47.55,"MFE_180D_pct":28.34,"MAE_180D_pct":-53.58,"forward_high_30d":96900,"forward_low_30d":70000,"forward_high_90d":96900,"forward_low_90d":39600,"forward_high_180d":96900,"forward_low_180d":35050,"calibration_usable":true,"same_entry_group_id":"R13_AT|006110|Stage4B|2024-05-20","dedupe_for_aggregate":true,"aggregate_group_role":"holdout_local_4B","independent_evidence_weight":0.0,"do_not_count_as_new_case":true,"case_role":"bridge_unrefreshed_local_4B","novelty_key":"R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION|006110|Stage4B|2024-05-20","accounting_bridge":"aluminium battery-foil material label without refreshed customer order, utilization, ASP/margin or cash bridge","route":"Local4B_RequireUtilizationMarginRefresh"}
{"row_type":"trigger","selected_round":"R13","selected_loop":13,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION","fine_archetype_id":"C18_EXPORT_REORDER_LATE_ENTRY_LOCAL_4B","source_archetype_id":"C18_CONSUMER_EXPORT_CHANNEL_REORDER","symbol":"003230","name":"삼양식품","trigger_type":"Stage4B","entry_date":"2024-06-17","entry_price":686000,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","MFE_30D_pct":4.66,"MAE_30D_pct":-15.31,"MFE_90D_pct":4.66,"MAE_90D_pct":-33.60,"MFE_180D_pct":37.03,"MAE_180D_pct":-33.60,"forward_high_30d":718000,"forward_low_30d":581000,"forward_high_90d":718000,"forward_low_90d":455500,"forward_high_180d":940000,"forward_low_180d":455500,"calibration_usable":true,"same_entry_group_id":"R13_AT|003230|Stage4B|2024-06-17","dedupe_for_aggregate":true,"aggregate_group_role":"holdout_local_4B","independent_evidence_weight":0.0,"do_not_count_as_new_case":true,"case_role":"accounting_trust_validated_but_late_entry","novelty_key":"R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION|003230|Stage4B|2024-06-17","accounting_bridge":"Buldak export, ASP, overseas shipment and capacity support; post-spike entry created high MAE before later validation","route":"Local4B_LateEntryExportBridge"}
{"row_type":"trigger","selected_round":"R13","selected_loop":13,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION","fine_archetype_id":"C26_OWNED_PLATFORM_ARPU_MARGIN_VALIDATED","source_archetype_id":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE","symbol":"035420","name":"NAVER","trigger_type":"Stage2-Actionable","entry_date":"2024-11-08","entry_price":174600,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","MFE_30D_pct":26.00,"MAE_30D_pct":-1.78,"MFE_90D_pct":34.88,"MAE_90D_pct":-1.78,"MFE_180D_pct":34.88,"MAE_180D_pct":-1.78,"forward_high_30d":220000,"forward_low_30d":171500,"forward_high_90d":235500,"forward_low_90d":171500,"forward_high_180d":235500,"forward_low_180d":171500,"calibration_usable":true,"same_entry_group_id":"R13_AT|035420|Stage2-Actionable|2024-11-08","dedupe_for_aggregate":true,"aggregate_group_role":"holdout_positive_control","independent_evidence_weight":0.0,"do_not_count_as_new_case":true,"case_role":"accounting_trust_validated","novelty_key":"R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION|035420|Stage2-Actionable|2024-11-08","accounting_bridge":"owned search/commerce platform ad inventory, ARPU, commerce conversion and margin leverage bridge","route":"KeepStage2_OwnedPlatformBridge"}
{"row_type":"trigger","selected_round":"R13","selected_loop":13,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION","fine_archetype_id":"C29_OEM_MIX_MARGIN_VALIDATED","source_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","symbol":"000270","name":"기아","trigger_type":"Stage2-Actionable","entry_date":"2024-01-25","entry_price":93000,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","MFE_30D_pct":41.61,"MAE_30D_pct":-7.42,"MFE_90D_pct":45.16,"MAE_90D_pct":-7.42,"MFE_180D_pct":45.16,"MAE_180D_pct":-7.42,"forward_high_30d":131700,"forward_low_30d":86100,"forward_high_90d":135000,"forward_low_90d":86100,"forward_high_180d":135000,"forward_low_180d":86100,"calibration_usable":true,"same_entry_group_id":"R13_AT|000270|Stage2-Actionable|2024-01-25","dedupe_for_aggregate":true,"aggregate_group_role":"holdout_positive_control","independent_evidence_weight":0.0,"do_not_count_as_new_case":true,"case_role":"accounting_trust_validated","novelty_key":"R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION|000270|Stage2-Actionable|2024-01-25","accounting_bridge":"OEM volume, product mix, ASP, margin and shareholder-return bridge","route":"KeepStage2_OEMMarginBridge"}
{"row_type":"trigger","selected_round":"R13","selected_loop":13,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION","fine_archetype_id":"C30_WEAK_LIQUIDITY_POLICY_LABEL_HARD_4C","source_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","symbol":"002990","name":"금호건설","trigger_type":"Stage4C","entry_date":"2024-01-26","entry_price":5030,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","MFE_30D_pct":5.00,"MAE_30D_pct":-4.60,"MFE_90D_pct":5.00,"MAE_90D_pct":-27.50,"MFE_180D_pct":5.00,"MAE_180D_pct":-41.00,"forward_high_30d":5280,"forward_low_30d":4800,"forward_high_90d":5280,"forward_low_90d":3650,"forward_high_180d":5280,"forward_low_180d":2970,"calibration_usable":true,"same_entry_group_id":"R13_AT|002990|Stage4C|2024-01-26","dedupe_for_aggregate":true,"aggregate_group_role":"holdout_hard_4C","independent_evidence_weight":0.0,"do_not_count_as_new_case":true,"case_role":"accounting_trust_absent_hard_4C","novelty_key":"R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION|002990|Stage4C|2024-01-26","accounting_bridge":"PF relief vocabulary without liquidity, debt-service, margin, guarantee relief or cash bridge","route":"Hard4C_WeakLiquidityBlock"}
{"row_type":"trigger","selected_round":"R13","selected_loop":13,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION","fine_archetype_id":"C31_POLICY_CASH_BRIDGE_POSITIVE_CONTROL","source_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","symbol":"373220","name":"LG에너지솔루션","trigger_type":"Stage2-Actionable","entry_date":"2024-07-25","entry_price":332500,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","MFE_30D_pct":18.50,"MAE_30D_pct":-6.47,"MFE_90D_pct":33.53,"MAE_90D_pct":-6.47,"MFE_180D_pct":33.53,"MAE_180D_pct":-6.47,"forward_high_30d":394000,"forward_low_30d":311000,"forward_high_90d":444000,"forward_low_90d":311000,"forward_high_180d":444000,"forward_low_180d":311000,"calibration_usable":true,"same_entry_group_id":"R13_AT|373220|Stage2-Actionable|2024-07-25","dedupe_for_aggregate":true,"aggregate_group_role":"holdout_positive_control","independent_evidence_weight":0.0,"do_not_count_as_new_case":true,"case_role":"policy_cash_bridge_validated","novelty_key":"R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION|373220|Stage2-Actionable|2024-07-25","accounting_bridge":"IRA/AMPC support plus customer diversification, utilization and ESS/non-EV demand bridge","route":"KeepStage2_PolicyCashBridge"}
{"row_type":"trigger","selected_round":"R13","selected_loop":13,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION","fine_archetype_id":"C31_POLICY_LABEL_NO_UTILIZATION_CASH_BRIDGE_HARD_4C","source_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","symbol":"361610","name":"SK아이이테크놀로지","trigger_type":"Stage4C","entry_date":"2024-05-16","entry_price":57600,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","MFE_30D_pct":1.04,"MAE_30D_pct":-25.87,"MFE_90D_pct":1.04,"MAE_90D_pct":-46.27,"MFE_180D_pct":1.04,"MAE_180D_pct":-60.68,"forward_high_30d":58200,"forward_low_30d":42700,"forward_high_90d":58200,"forward_low_90d":30950,"forward_high_180d":58200,"forward_low_180d":22650,"calibration_usable":true,"same_entry_group_id":"R13_AT|361610|Stage4C|2024-05-16","dedupe_for_aggregate":true,"aggregate_group_role":"holdout_hard_4C","independent_evidence_weight":0.0,"do_not_count_as_new_case":true,"case_role":"policy_label_hard_4C","novelty_key":"R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION|361610|Stage4C|2024-05-16","accounting_bridge":"separator/material policy exposure without customer pull, utilization, parent financing or cash-conversion bridge","route":"Hard4C_PolicyLabelNoCashBridge"}
{"row_type":"trigger","selected_round":"R13","selected_loop":13,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION","fine_archetype_id":"C32_FORMAL_TENDER_CASH_EXIT_VALIDATED_POST_RESOLUTION_4B","source_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","symbol":"041510","name":"에스엠","trigger_type":"Stage2-Actionable","entry_date":"2023-02-10","entry_price":114700,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","MFE_30D_pct":40.54,"MAE_30D_pct":-6.45,"MFE_90D_pct":40.54,"MAE_90D_pct":-21.10,"MFE_180D_pct":40.54,"MAE_180D_pct":-21.10,"forward_high_30d":161200,"forward_low_30d":107300,"forward_high_90d":161200,"forward_low_90d":90500,"forward_high_180d":161200,"forward_low_180d":90500,"calibration_usable":true,"same_entry_group_id":"R13_AT|041510|Stage2-Actionable|2023-02-10","dedupe_for_aggregate":true,"aggregate_group_role":"holdout_positive_with_4B","independent_evidence_weight":0.0,"do_not_count_as_new_case":true,"case_role":"cash_exit_validated_post_resolution_4B","novelty_key":"R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION|041510|Stage2-Actionable|2023-02-10","accounting_bridge":"formal tender/control contest cash path with visible minority exit mechanics","route":"KeepStage2_PostResolution4B"}
```

---

## 5. Case analysis

### 5.1 Doosan Enerbility / 034020 — incomplete project bridge

A preferred-bidder headline reached the narrative layer, but not the accounting layer at trigger date.

```text
route = Local4B_NoFinalContractBackfill
```

### 5.2 Woojin Entech / 457550 — supplier theme hard block

Supplier theme heat had no contract-scope bridge.

```text
route = Hard4C_SupplierThemeBlock
```

### 5.3 KCC / 002380 — material margin bridge validates

The material thesis became margin and FCF evidence.

```text
route = KeepStage2_MaterialMarginBridge
```

### 5.4 Sam-A Aluminium / 006110 — foil bridge unrefreshed

Material label plus early MFE is not enough without utilization and margin refresh.

```text
route = Local4B_RequireUtilizationMarginRefresh
```

### 5.5 Samyang Foods / 003230 — export bridge, late-entry local 4B

The export bridge was real, but the post-spike entry had too much MAE for immediate Green.

```text
route = Local4B_LateEntryExportBridge
```

### 5.6 NAVER / 035420 — owned platform bridge validates

Owned inventory, ARPU and margin bridge validate.

```text
route = KeepStage2_OwnedPlatformBridge
```

### 5.7 Kia / 000270 — OEM margin bridge validates

Volume, mix and margin bridge validate.

```text
route = KeepStage2_OEMMarginBridge
```

### 5.8 Kumho E&C / 002990 — PF relief hard block

Policy umbrella did not reach issuer cashflow.

```text
route = Hard4C_WeakLiquidityBlock
```

### 5.9 LG Energy Solution / 373220 — policy cash bridge validates

AMPC/IRA policy became utilization and cash bridge.

```text
route = KeepStage2_PolicyCashBridge
```

### 5.10 SK IE Technology / 361610 — policy label hard 4C

Localization/policy label did not become utilization or cash.

```text
route = Hard4C_PolicyLabelNoCashBridge
```

### 5.11 SM Entertainment / 041510 — tender cash-exit validates

Tender mechanics create accounting trust, followed by post-resolution 4B.

```text
route = KeepStage2_PostResolution4B
```

---

## 6. Score-return alignment

```yaml
new_independent_case_count: 0
reused_case_count: 11
new_symbol_count: 0
same_archetype_new_symbol_count: 0
same_archetype_new_trigger_family_count: 0
new_trigger_family_count: 0
calibration_usable_case_count: 11
calibration_usable_trigger_count: 11
positive_case_count: 5
counterexample_count: 5
local_4B_watch_count: 4
hard_4C_count: 4
wrong_archetype_reclassification_count: 0
current_profile_error_count: 7
diversity_score_summary: "C04/C15/C18/C26/C29/C30/C31/C32 positives and counterexamples covered; all rows reused"
loop_contribution_label: duplicate_low_value_loop
do_not_propose_new_weight_delta: true
```

| symbol | source | route | 90D MFE/MAE | 180D MFE/MAE | accounting lesson |
|---|---:|---:|---:|---:|---|
| 034020 | C04 | local 4B | +17.65 / -28.71 | +17.65 / -28.71 | preferred bidder lacks final contract bridge |
| 457550 | C04 | hard 4C | +32.06 / -58.25 | +32.06 / -58.25 | supplier theme lacks contract economics |
| 002380 | C15 | keep Stage2 | +20.49 / -7.79 | +41.39 / -7.79 | margin bridge validates |
| 006110 | C15 | local 4B | +28.34 / -47.55 | +28.34 / -53.58 | utilization/margin refresh needed |
| 003230 | C18 | local 4B | +4.66 / -33.60 | +37.03 / -33.60 | real bridge, late entry |
| 035420 | C26 | keep Stage2 | +34.88 / -1.78 | +34.88 / -1.78 | owned inventory validates |
| 000270 | C29 | keep Stage2 | +45.16 / -7.42 | +45.16 / -7.42 | OEM margin bridge validates |
| 002990 | C30 | hard 4C | +5.00 / -27.50 | +5.00 / -41.00 | PF relief lacks cash bridge |
| 373220 | C31 | keep Stage2 | +33.53 / -6.47 | +33.53 / -6.47 | AMPC/cash bridge validates |
| 361610 | C31 | hard 4C | +1.04 / -46.27 | +1.04 / -60.68 | policy label lacks utilization |
| 041510 | C32 | Stage2 + 4B | +40.54 / -21.10 | +40.54 / -21.10 | tender cash-exit validates |

---

## 7. Current calibrated profile stress test

The bridge-passport gate held:

```text
nuclear headline without contract bridge -> local 4B / hard 4C
material label without margin bridge -> local 4B / hard 4C
export bridge with poor entry timing -> local 4B
owned platform / OEM / AMPC bridge -> keep Stage2
PF relief without issuer cash -> hard 4C
formal tender -> keep Stage2, then post-resolution 4B
```

### Rule candidate retained, not newly proposed

```text
R13_ACCOUNTING_TRUST_BRIDGE_PASSPORT_GATE_V13_HELD_OUT

if trigger_label_exists == true
and company_specific_cash_bridge_at_trigger_date == false:
    stage2_actionable_bonus = 0
    max_stage = Stage2-Watch
```

```text
if company_specific_cash_bridge_at_trigger_date == true
and MFE_90D_pct >= +20
and MAE_90D_pct > -10:
    keep_stage2_actionable_bonus = true
```

```text
if bridge_exists_but_refresh_missing == true
and MAE_90D_pct <= -20:
    route = local_4B_watch
    block_stage3_green = true
```

```text
if label_only == true
and MAE_90D_pct <= -25:
    route = Stage4C
```

```text
if later_evidence_after_trigger == true:
    do_not_backfill_to_original_trigger = true
    require_new_trigger_from_later_evidence_date = true
```

---

## 8. Batch Ingest Self-Audit

```yaml
expected_v12_result_file: true
filename_pattern_pass: true
metadata_filename_consistency: pass
jsonl_trigger_row_count: 11
calibration_usable_trigger_count: 11
representative_trigger_count: 0
new_weight_evidence_candidate_count: 0
guardrail_candidate_count: 11
narrative_only_or_rejected_count: 0
rows_missing_required_mfe_mae: 0
rows_missing_entry_price_or_date: 0
rows_with_noncanonical_trigger_type: 0
rows_with_compact_mfe_mae_alias_only: 0
ready_for_batch_ingest: true
batch_ingest_recommendation: dedupe_as_holdout_validation_only
```

---

## 9. Residual contribution summary

```yaml
do_not_propose_new_weight_delta: true
sector_specific_rule_candidate: false
canonical_archetype_rule_candidate: false
cross_archetype_rule_candidate: false
holdout_validation_passed: true
loop_contribution_label: duplicate_low_value_loop
new_axis_proposed: null
existing_axis_strengthened:
  - R13_ACCOUNTING_TRUST_BRIDGE_PASSPORT_GATE_V13_HELD_OUT
existing_axis_weakened: null
one_line_summary: "This loop adds 0 new independent cases and validates the R13 accounting-trust bridge-passport gate across C04/C15/C18/C26/C29/C30/C31/C32."
```

---

## 10. Deferred Coding Agent Handoff Prompt

```text
Do not patch production scoring from this MD alone. Treat R13 accounting-trust loop 13 as holdout validation only. Batch it with R13 accounting-trust loops 10~12, R13 Stage2 false-positive / high-MAE / 4B-4C loops, and source loops C04/C15/C18/C26/C29/C30/C31/C32 from this session. If exact same_entry_group_id rows already exist, dedupe them. Preserve the cross-archetype accounting-trust bridge-passport gate, but do not create a new weight delta from this loop because no new independent case was added.
```

---

## 11. Next research state

```yaml
completed_round: R13
completed_loop: 13
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
