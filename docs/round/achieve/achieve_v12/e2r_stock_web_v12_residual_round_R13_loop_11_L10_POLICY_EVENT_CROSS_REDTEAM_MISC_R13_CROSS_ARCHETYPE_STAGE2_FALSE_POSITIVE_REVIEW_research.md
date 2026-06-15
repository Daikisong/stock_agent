# E2R v12 R13 cross-archetype residual calibration research

## 0. Execution metadata

```yaml
schema_family: v12_sector_archetype_residual
selected_round: R13
selected_loop: 11
large_sector_id: L10_POLICY_EVENT_CROSS_REDTEAM_MISC
canonical_archetype_id: R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW
fine_archetype_id: HOLDOUT_VALIDATION_STAGE2_BRIDGE_PASSPORT_FALSE_POSITIVE_GATE_C04_C15_C18_C26_C29_C30_C31_C32
selection_basis:
  main_execution_prompt: docs/core/e2r_v12_prompt_round_scheduler_corrected.txt
  no_repeat_index: docs/core/V12_Research_No_Repeat_Index.md
web_raw_fetch_status_this_turn:
  main_execution_prompt: read_ok
  no_repeat_index: read_ok
  stock_web_manifest: read_ok
  uncached_symbol_shards:
    - additional_sector_candidate_shards: cache_miss_observed
selected_priority_bucket: Priority 0
round_schedule_status: coverage_index_selected
round_sector_consistency: pass
loop_objective:
  - holdout_validation
  - duplicate_low_value_loop_marker
  - cross_archetype_stage2_false_positive_review
  - bridge_passport_gate
  - no_new_weight_delta
price_source: Songdaiki/stock-web
price_data_source: Songdaiki/stock-web
price_basis: tradable_raw
price_adjustment_status: raw_unadjusted_marcap
stock_web_manifest_max_date: 2026-02-20
production_scoring_changed: false
shadow_weight_only: true
```

R13 is a cross-archetype checkpoint. This file does not perform sector-specific discovery and does not patch scoring. It consolidates current-session holdout rows from C04, C15, C18, C26, C29, C30, C31 and C32 under one Stage2 false-positive question:

```text
Did Stage2 pay for a label, or did the row actually have a company-specific bridge passport?
```

The previous local `R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW` file reached loop 10, so this continuation uses loop 11.

This file is intentionally marked as duplicate-low-value holdout validation. It should be deduped if the same entry groups already exist.

---

## 1. Research thesis

A Stage2 row should not cross the border with only a headline.

```text
headline / label / theme
→ not enough

company-specific bridge
→ required

bridge + price path
→ Stage2 can survive

no bridge + weak MFE or deep MAE
→ Stage2 false positive / hard 4C

real bridge but wrong archetype
→ cap selected archetype and reclassify
```

The bridge passport differs by sector:

```text
C04 nuclear:
preferred bidder / supplier theme
→ final contract, legal clearance, order scope, cash bridge

C15 materials:
material label
→ ASP, utilization, margin, FCF

C18 consumer:
export / global brand label
→ sell-through, reorder, inventory quality, margin

C26 platform:
ad / platform label
→ owned inventory, ARPU, retention, margin leverage

C29 mobility:
auto / parts / Value-up label
→ volume, mix, customer order, margin

C30 construction:
PF / housing policy label
→ refinancing, guarantee relief, presale, debt-service, cash conversion

C31 policy:
policy umbrella
→ company-specific cash bridge

C32 governance:
shareholder-friendly cash
→ formal tender, appraisal, squeeze-out, minority cash-exit
```

---

## 2. Validation scope

```yaml
validation_scope:
  required_cases: 10
  actual_trigger_rows: 14
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
    - R13 Stage2 false-positive holdout validation
    - label-only Stage2 block
    - company-specific bridge escape hatch
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
  - R13 high-MAE loop 8
  - R13 4B/4C loop 103
reason:
  - all rows were already calculated from Songdaiki/stock-web tradable raw 1D OHLC
  - additional candidate shards were unavailable in this execution
  - exact same_entry_group_id rows should be deduped during batch ingest
  - this file is Stage2 false-positive holdout validation only
```

---

## 4. Trigger rows

```jsonl
{"row_type":"trigger","selected_round":"R13","selected_loop":11,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW","fine_archetype_id":"C04_SUPPLIER_THEME_NO_CONTRACT_SCOPE_STAGE2_BLOCK","source_archetype_id":"C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY","symbol":"457550","name":"우진엔텍","trigger_type":"Stage4C","entry_date":"2024-07-18","entry_price":31500,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","MFE_30D_pct":32.06,"MAE_30D_pct":-50.83,"MFE_90D_pct":32.06,"MAE_90D_pct":-58.25,"MFE_180D_pct":32.06,"MAE_180D_pct":-58.25,"forward_high_30d":41600,"forward_low_30d":15490,"forward_high_90d":41600,"forward_low_90d":13150,"forward_high_180d":41600,"forward_low_180d":13150,"calibration_usable":true,"same_entry_group_id":"R13_S2FP|457550|Stage4C|2024-07-18","dedupe_for_aggregate":true,"aggregate_group_role":"holdout_hard_4C","independent_evidence_weight":0.0,"do_not_count_as_new_case":true,"stage2_error":"small supplier nuclear theme spike had no listed-company final-contract, order-scope, margin or cash bridge","route":"Stage2FalsePositiveBlock"}
{"row_type":"trigger","selected_round":"R13","selected_loop":11,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW","fine_archetype_id":"C04_PREFERRED_BIDDER_INCOMPLETE_BRIDGE_STAGE2_WATCH","source_archetype_id":"C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY","symbol":"034020","name":"두산에너빌리티","trigger_type":"Stage2-Watch","entry_date":"2024-07-17","entry_price":21250,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","MFE_30D_pct":17.65,"MAE_30D_pct":-28.71,"MFE_90D_pct":17.65,"MAE_90D_pct":-28.71,"MFE_180D_pct":17.65,"MAE_180D_pct":-28.71,"forward_high_30d":25000,"forward_low_30d":15150,"forward_high_90d":25000,"forward_low_90d":15150,"forward_high_180d":25000,"forward_low_180d":15150,"calibration_usable":true,"same_entry_group_id":"R13_S2FP|034020|Stage2-Watch|2024-07-17","dedupe_for_aggregate":true,"aggregate_group_role":"holdout_watch","independent_evidence_weight":0.0,"do_not_count_as_new_case":true,"stage2_error":"preferred-bidder headline lacked final contract, legal clearance and company cash bridge at trigger date","route":"Stage2Watch_NoBackfill"}
{"row_type":"trigger","selected_round":"R13","selected_loop":11,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW","fine_archetype_id":"C15_ALUMINIUM_ROLLING_COMMODITY_BETA_STAGE2_BLOCK","source_archetype_id":"C15_MATERIAL_SPREAD_SUPERCYCLE","symbol":"018470","name":"조일알미늄","trigger_type":"Stage4C","entry_date":"2024-05-20","entry_price":2470,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","MFE_30D_pct":7.29,"MAE_30D_pct":-17.41,"MFE_90D_pct":7.29,"MAE_90D_pct":-41.30,"MFE_180D_pct":7.29,"MAE_180D_pct":-44.70,"forward_high_30d":2650,"forward_low_30d":2040,"forward_high_90d":2650,"forward_low_90d":1450,"forward_high_180d":2650,"forward_low_180d":1366,"calibration_usable":true,"same_entry_group_id":"R13_S2FP|018470|Stage4C|2024-05-20","dedupe_for_aggregate":true,"aggregate_group_role":"holdout_hard_4C","independent_evidence_weight":0.0,"do_not_count_as_new_case":true,"stage2_error":"aluminium rolling commodity beta label lacked company-specific ASP, volume, margin or FCF bridge","route":"Stage2FalsePositiveBlock"}
{"row_type":"trigger","selected_round":"R13","selected_loop":11,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW","fine_archetype_id":"C15_MATERIAL_MARGIN_STAGE2_ESCAPE_HATCH","source_archetype_id":"C15_MATERIAL_SPREAD_SUPERCYCLE","symbol":"002380","name":"KCC","trigger_type":"Stage2-Actionable","entry_date":"2024-01-30","entry_price":244000,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","MFE_30D_pct":17.62,"MAE_30D_pct":-2.46,"MFE_90D_pct":20.49,"MAE_90D_pct":-7.79,"MFE_180D_pct":41.39,"MAE_180D_pct":-7.79,"forward_high_30d":287000,"forward_low_30d":238000,"forward_high_90d":294000,"forward_low_90d":225000,"forward_high_180d":345000,"forward_low_180d":225000,"calibration_usable":true,"same_entry_group_id":"R13_S2FP|002380|Stage2-Actionable|2024-01-30","dedupe_for_aggregate":true,"aggregate_group_role":"holdout_positive_escape","independent_evidence_weight":0.0,"do_not_count_as_new_case":true,"stage2_error":"none; company-specific material margin bridge validated","route":"KeepStage2_MaterialMarginBridge"}
{"row_type":"trigger","selected_round":"R13","selected_loop":11,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW","fine_archetype_id":"C18_BRAND_CHANNEL_INVENTORY_STAGE2_BLOCK","source_archetype_id":"C18_CONSUMER_EXPORT_CHANNEL_REORDER","symbol":"383220","name":"F&F","trigger_type":"Stage4C","entry_date":"2024-07-17","entry_price":74000,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","MFE_30D_pct":3.24,"MAE_30D_pct":-33.99,"MFE_90D_pct":3.24,"MAE_90D_pct":-33.99,"MFE_180D_pct":3.24,"MAE_180D_pct":-33.99,"calibration_usable":true,"same_entry_group_id":"R13_S2FP|383220|Stage4C|2024-07-17","dedupe_for_aggregate":true,"aggregate_group_role":"holdout_hard_4C","independent_evidence_weight":0.0,"do_not_count_as_new_case":true,"stage2_error":"apparel/global brand label lacked sell-through, channel inventory normalization and reorder proof","route":"Stage2FalsePositiveBlock"}
{"row_type":"trigger","selected_round":"R13","selected_loop":11,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW","fine_archetype_id":"C18_EXPORT_REORDER_STAGE2_ESCAPE_HATCH_WITH_4B_TIMING","source_archetype_id":"C18_CONSUMER_EXPORT_CHANNEL_REORDER","symbol":"003230","name":"삼양식품","trigger_type":"Stage4B","entry_date":"2024-06-17","entry_price":686000,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","MFE_30D_pct":4.66,"MAE_30D_pct":-15.31,"MFE_90D_pct":4.66,"MAE_90D_pct":-33.60,"MFE_180D_pct":37.03,"MAE_180D_pct":-33.60,"forward_high_30d":718000,"forward_low_30d":581000,"forward_high_90d":718000,"forward_low_90d":455500,"forward_high_180d":940000,"forward_low_180d":455500,"calibration_usable":true,"same_entry_group_id":"R13_S2FP|003230|Stage4B|2024-06-17","dedupe_for_aggregate":true,"aggregate_group_role":"holdout_real_bridge_4B","independent_evidence_weight":0.0,"do_not_count_as_new_case":true,"stage2_error":"not bridge quality, but timing; export/ASP bridge was real but post-spike entry created high MAE","route":"Local4B_LateEntryExportBridge"}
{"row_type":"trigger","selected_round":"R13","selected_loop":11,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW","fine_archetype_id":"C26_ADTECH_LABEL_NO_OWNED_INVENTORY_STAGE2_BLOCK","source_archetype_id":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE","symbol":"214270","name":"FSN","trigger_type":"Stage4C","entry_date":"2024-07-18","entry_price":2105,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","MFE_30D_pct":16.63,"MAE_30D_pct":-26.37,"MFE_90D_pct":19.00,"MAE_90D_pct":-26.37,"MFE_180D_pct":19.00,"MAE_180D_pct":-49.64,"forward_high_30d":2455,"forward_low_30d":1550,"forward_high_90d":2505,"forward_low_90d":1550,"forward_high_180d":2505,"forward_low_180d":1060,"calibration_usable":true,"same_entry_group_id":"R13_S2FP|214270|Stage4C|2024-07-18","dedupe_for_aggregate":true,"aggregate_group_role":"holdout_hard_4C","independent_evidence_weight":0.0,"do_not_count_as_new_case":true,"stage2_error":"adtech/marketing service label lacked owned ad inventory, ARPU, retention, take-rate and durable margin bridge","route":"Stage2FalsePositiveBlock"}
{"row_type":"trigger","selected_round":"R13","selected_loop":11,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW","fine_archetype_id":"C26_OWNED_PLATFORM_STAGE2_ESCAPE_HATCH","source_archetype_id":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE","symbol":"035420","name":"NAVER","trigger_type":"Stage2-Actionable","entry_date":"2024-11-08","entry_price":174600,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","MFE_30D_pct":26.00,"MAE_30D_pct":-1.78,"MFE_90D_pct":34.88,"MAE_90D_pct":-1.78,"MFE_180D_pct":34.88,"MAE_180D_pct":-1.78,"forward_high_30d":220000,"forward_low_30d":171500,"forward_high_90d":235500,"forward_low_90d":171500,"forward_high_180d":235500,"forward_low_180d":171500,"calibration_usable":true,"same_entry_group_id":"R13_S2FP|035420|Stage2-Actionable|2024-11-08","dedupe_for_aggregate":true,"aggregate_group_role":"holdout_positive_escape","independent_evidence_weight":0.0,"do_not_count_as_new_case":true,"stage2_error":"none; owned platform inventory, ARPU and margin bridge validated","route":"KeepStage2_OwnedPlatformBridge"}
{"row_type":"trigger","selected_round":"R13","selected_loop":11,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW","fine_archetype_id":"C29_VALUEUP_LABEL_WITHOUT_OPERATING_BRIDGE_CAP","source_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","symbol":"005380","name":"현대차","trigger_type":"Stage2-Watch","entry_date":"2024-08-28","entry_price":259000,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","MFE_30D_pct":3.09,"MAE_30D_pct":-14.48,"MFE_90D_pct":3.09,"MAE_90D_pct":-22.78,"MFE_180D_pct":3.09,"MAE_180D_pct":-32.12,"forward_high_30d":267000,"forward_low_30d":221500,"forward_high_90d":267000,"forward_low_90d":200000,"forward_high_180d":267000,"forward_low_180d":175800,"calibration_usable":true,"same_entry_group_id":"R13_S2FP|005380|Stage2-Watch|2024-08-28","dedupe_for_aggregate":true,"aggregate_group_role":"holdout_stage2_cap","independent_evidence_weight":0.0,"do_not_count_as_new_case":true,"stage2_error":"shareholder-return intent did not validate C29 volume/mix/margin operating bridge","route":"Stage2Cap_C29BridgeMissing"}
{"row_type":"trigger","selected_round":"R13","selected_loop":11,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW","fine_archetype_id":"C30_WEAK_LIQUIDITY_PF_LABEL_STAGE2_BLOCK","source_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","symbol":"002990","name":"금호건설","trigger_type":"Stage4C","entry_date":"2024-01-26","entry_price":5030,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","MFE_30D_pct":5.00,"MAE_30D_pct":-4.60,"MFE_90D_pct":5.00,"MAE_90D_pct":-27.50,"MFE_180D_pct":5.00,"MAE_180D_pct":-41.00,"forward_high_30d":5280,"forward_low_30d":4800,"forward_high_90d":5280,"forward_low_90d":3650,"forward_high_180d":5280,"forward_low_180d":2970,"calibration_usable":true,"same_entry_group_id":"R13_S2FP|002990|Stage4C|2024-01-26","dedupe_for_aggregate":true,"aggregate_group_role":"holdout_hard_4C","independent_evidence_weight":0.0,"do_not_count_as_new_case":true,"stage2_error":"PF relief vocabulary lacked liquidity, debt-service, guarantee relief or cash bridge","route":"Stage2FalsePositiveBlock"}
{"row_type":"trigger","selected_round":"R13","selected_loop":11,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW","fine_archetype_id":"C31_POLICY_LABEL_NO_UTILIZATION_CASH_BRIDGE_BLOCK","source_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","symbol":"361610","name":"SK아이이테크놀로지","trigger_type":"Stage4C","entry_date":"2024-05-16","entry_price":57600,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","MFE_30D_pct":1.04,"MAE_30D_pct":-25.87,"MFE_90D_pct":1.04,"MAE_90D_pct":-46.27,"MFE_180D_pct":1.04,"MAE_180D_pct":-60.68,"forward_high_30d":58200,"forward_low_30d":42700,"forward_high_90d":58200,"forward_low_90d":30950,"forward_high_180d":58200,"forward_low_180d":22650,"calibration_usable":true,"same_entry_group_id":"R13_S2FP|361610|Stage4C|2024-05-16","dedupe_for_aggregate":true,"aggregate_group_role":"holdout_hard_4C","independent_evidence_weight":0.0,"do_not_count_as_new_case":true,"stage2_error":"policy/localization label lacked utilization and cash conversion bridge","route":"Stage2FalsePositiveBlock"}
{"row_type":"trigger","selected_round":"R13","selected_loop":11,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW","fine_archetype_id":"C32_CAPITAL_RETURN_POSITIVE_ELSEWHERE_NOT_TENDER_CAP","source_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","symbol":"105560","name":"KB금융","trigger_type":"Stage4B","entry_date":"2024-07-26","entry_price":87900,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","MFE_30D_pct":5.12,"MAE_30D_pct":-15.81,"MFE_90D_pct":18.20,"MAE_90D_pct":-15.81,"MFE_180D_pct":18.20,"MAE_180D_pct":-15.81,"forward_high_30d":92400,"forward_low_30d":74000,"forward_high_90d":103900,"forward_low_90d":74000,"forward_high_180d":103900,"forward_low_180d":74000,"calibration_usable":true,"same_entry_group_id":"R13_S2FP|105560|Stage4B|2024-07-26","dedupe_for_aggregate":true,"aggregate_group_role":"holdout_wrong_archetype_4B","independent_evidence_weight":0.0,"do_not_count_as_new_case":true,"stage2_error":"capital-return bridge may be valid in C21/C31 but is not C32 tender/minority cash-exit mechanics","route":"Stage2Cap_ReclassifyToC21C31"}
{"row_type":"trigger","selected_round":"R13","selected_loop":11,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW","fine_archetype_id":"C32_TENDER_CASH_EXIT_STAGE2_ESCAPE_HATCH_POST_RESOLUTION_4B","source_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","symbol":"041510","name":"에스엠","trigger_type":"Stage2-Actionable","entry_date":"2023-02-10","entry_price":114700,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","MFE_30D_pct":40.54,"MAE_30D_pct":-6.45,"MFE_90D_pct":40.54,"MAE_90D_pct":-21.10,"MFE_180D_pct":40.54,"MAE_180D_pct":-21.10,"forward_high_30d":161200,"forward_low_30d":107300,"forward_high_90d":161200,"forward_low_90d":90500,"forward_high_180d":161200,"forward_low_180d":90500,"calibration_usable":true,"same_entry_group_id":"R13_S2FP|041510|Stage2-Actionable|2023-02-10","dedupe_for_aggregate":true,"aggregate_group_role":"holdout_positive_escape_with_4B","independent_evidence_weight":0.0,"do_not_count_as_new_case":true,"stage2_error":"none during tender; formal minority cash-exit mechanics validated, with post-resolution 4B required","route":"KeepStage2_PostResolution4B"}
```

---

## 5. Case analysis

### 5.1 Woojin Entech / 457550 — supplier label hard block

Stage2 should not pay for supplier heat when no contract-scope bridge exists.

```text
route = Stage2FalsePositiveBlock
```

### 5.2 Doosan Enerbility / 034020 — preferred-bidder watch

Potential exists, but final contract and order-scope bridge were incomplete at trigger date.

```text
route = Stage2Watch_NoBackfill
```

### 5.3 Choil Aluminium / 018470 — commodity beta block

Material label did not become company spread.

```text
route = Stage2FalsePositiveBlock
```

### 5.4 KCC / 002380 — margin bridge escape hatch

Stage2 is valid when company-specific margin bridge exists.

```text
route = KeepStage2_MaterialMarginBridge
```

### 5.5 F&F / 383220 — channel label hard block

Global brand label lacked sell-through and inventory repair.

```text
route = Stage2FalsePositiveBlock
```

### 5.6 Samyang Foods / 003230 — real bridge but bad timing

This is not a label failure. It is a timing/local 4B issue.

```text
route = Local4B_LateEntryExportBridge
```

### 5.7 FSN / 214270 — adtech label block

No owned-inventory bridge.

```text
route = Stage2FalsePositiveBlock
```

### 5.8 NAVER / 035420 — owned platform escape hatch

Owned inventory, ARPU and margin bridge protect Stage2.

```text
route = KeepStage2_OwnedPlatformBridge
```

### 5.9 Hyundai Motor / 005380 — Value-up label cap

Shareholder-return intent did not validate the C29 operating bridge.

```text
route = Stage2Cap_C29BridgeMissing
```

### 5.10 Kumho E&C / 002990 — PF label block

Policy umbrella did not reach issuer cashflow.

```text
route = Stage2FalsePositiveBlock
```

### 5.11 SK IE Technology / 361610 — policy label block

Policy/localization label lacked utilization and cash bridge.

```text
route = Stage2FalsePositiveBlock
```

### 5.12 KB Financial / 105560 — wrong archetype cap

Capital return may be real but belongs to C21/C31, not C32 tender mechanics.

```text
route = Stage2Cap_ReclassifyToC21C31
```

### 5.13 SM Entertainment / 041510 — tender escape hatch

Formal tender mechanics are genuine Stage2 evidence during the cash-exit window.

```text
route = KeepStage2_PostResolution4B
```

---

## 6. Score-return alignment

```yaml
new_independent_case_count: 0
reused_case_count: 13
new_symbol_count: 0
same_archetype_new_symbol_count: 0
same_archetype_new_trigger_family_count: 0
new_trigger_family_count: 0
calibration_usable_case_count: 13
calibration_usable_trigger_count: 13
positive_escape_hatch_count: 4
stage2_watch_or_local_4B_count: 3
stage2_cap_or_reclassification_count: 2
stage2_false_positive_count: 7
current_profile_error_count: 9
diversity_score_summary: "cross-archetype false positives and escape hatches covered, but all rows reused"
loop_contribution_label: duplicate_low_value_loop
do_not_propose_new_weight_delta: true
```

| symbol | source | route | 90D MFE/MAE | 180D MFE/MAE | false-positive lesson |
|---|---:|---:|---:|---:|---|
| 457550 | C04 | hard block | +32.06 / -58.25 | +32.06 / -58.25 | supplier spike lacks contract economics |
| 034020 | C04 | watch | +17.65 / -28.71 | +17.65 / -28.71 | preferred bidder lacks final contract |
| 018470 | C15 | hard block | +7.29 / -41.30 | +7.29 / -44.70 | material beta lacks spread bridge |
| 002380 | C15 | keep Stage2 | +20.49 / -7.79 | +41.39 / -7.79 | margin bridge validates |
| 383220 | C18 | hard block | +3.24 / -33.99 | +3.24 / -33.99 | channel label fails |
| 003230 | C18 | local 4B | +4.66 / -33.60 | +37.03 / -33.60 | bridge real, entry late |
| 214270 | C26 | hard block | +19.00 / -26.37 | +19.00 / -49.64 | adtech label fails |
| 035420 | C26 | keep Stage2 | +34.88 / -1.78 | +34.88 / -1.78 | owned platform validates |
| 005380 | C29 | cap | +3.09 / -22.78 | +3.09 / -32.12 | Value-up label lacks C29 bridge |
| 002990 | C30 | hard block | +5.00 / -27.50 | +5.00 / -41.00 | PF relief lacks issuer cash |
| 361610 | C31 | hard block | +1.04 / -46.27 | +1.04 / -60.68 | policy label lacks utilization |
| 105560 | C32 boundary | reclassify | +18.20 / -15.81 | +18.20 / -15.81 | real bridge belongs elsewhere |
| 041510 | C32 | keep Stage2 + 4B | +40.54 / -21.10 | +40.54 / -21.10 | tender cash-exit validates |

---

## 7. Raw component score breakdown

```jsonl
{"row_type":"score_simulation","symbol":"457550","raw_label_signal":5,"raw_company_bridge":0,"raw_price_validation":0,"raw_false_positive_risk":5,"raw_reclassification_need":1,"stage2_actionable_bonus_before":2.0,"stage2_actionable_bonus_after":0.0,"simulated_route":"Stage2FalsePositiveBlock"}
{"row_type":"score_simulation","symbol":"034020","raw_label_signal":4,"raw_company_bridge":1,"raw_price_validation":1,"raw_false_positive_risk":4,"raw_reclassification_need":0,"stage2_actionable_bonus_before":2.0,"stage2_actionable_bonus_after":0.0,"simulated_route":"Stage2Watch_NoBackfill"}
{"row_type":"score_simulation","symbol":"018470","raw_label_signal":4,"raw_company_bridge":0,"raw_price_validation":0,"raw_false_positive_risk":5,"raw_reclassification_need":0,"stage2_actionable_bonus_before":2.0,"stage2_actionable_bonus_after":0.0,"simulated_route":"Stage2FalsePositiveBlock"}
{"row_type":"score_simulation","symbol":"002380","raw_label_signal":2,"raw_company_bridge":5,"raw_price_validation":4,"raw_false_positive_risk":0,"raw_reclassification_need":0,"stage2_actionable_bonus_before":2.0,"stage2_actionable_bonus_after":2.0,"simulated_route":"KeepStage2"}
{"row_type":"score_simulation","symbol":"383220","raw_label_signal":4,"raw_company_bridge":0,"raw_price_validation":0,"raw_false_positive_risk":5,"raw_reclassification_need":0,"stage2_actionable_bonus_before":2.0,"stage2_actionable_bonus_after":0.0,"simulated_route":"Stage2FalsePositiveBlock"}
{"row_type":"score_simulation","symbol":"003230","raw_label_signal":2,"raw_company_bridge":4,"raw_price_validation":2,"raw_false_positive_risk":1,"raw_reclassification_need":0,"stage2_actionable_bonus_before":2.0,"stage2_actionable_bonus_after":1.0,"simulated_route":"Local4BTiming"}
{"row_type":"score_simulation","symbol":"214270","raw_label_signal":4,"raw_company_bridge":0,"raw_price_validation":0,"raw_false_positive_risk":5,"raw_reclassification_need":1,"stage2_actionable_bonus_before":2.0,"stage2_actionable_bonus_after":0.0,"simulated_route":"Stage2FalsePositiveBlock"}
{"row_type":"score_simulation","symbol":"035420","raw_label_signal":2,"raw_company_bridge":5,"raw_price_validation":4,"raw_false_positive_risk":0,"raw_reclassification_need":0,"stage2_actionable_bonus_before":2.0,"stage2_actionable_bonus_after":2.0,"simulated_route":"KeepStage2"}
{"row_type":"score_simulation","symbol":"005380","raw_label_signal":4,"raw_company_bridge":1,"raw_price_validation":0,"raw_false_positive_risk":4,"raw_reclassification_need":3,"stage2_actionable_bonus_before":2.0,"stage2_actionable_bonus_after":0.0,"simulated_route":"Stage2Cap"}
{"row_type":"score_simulation","symbol":"002990","raw_label_signal":4,"raw_company_bridge":0,"raw_price_validation":0,"raw_false_positive_risk":5,"raw_reclassification_need":0,"stage2_actionable_bonus_before":2.0,"stage2_actionable_bonus_after":0.0,"simulated_route":"Stage2FalsePositiveBlock"}
{"row_type":"score_simulation","symbol":"361610","raw_label_signal":4,"raw_company_bridge":0,"raw_price_validation":0,"raw_false_positive_risk":5,"raw_reclassification_need":0,"stage2_actionable_bonus_before":2.0,"stage2_actionable_bonus_after":0.0,"simulated_route":"Stage2FalsePositiveBlock"}
{"row_type":"score_simulation","symbol":"105560","raw_label_signal":3,"raw_company_bridge":4,"raw_price_validation":2,"raw_false_positive_risk":2,"raw_reclassification_need":5,"stage2_actionable_bonus_before":2.0,"stage2_actionable_bonus_after":0.0,"simulated_route":"Reclassify"}
{"row_type":"score_simulation","symbol":"041510","raw_label_signal":3,"raw_company_bridge":5,"raw_price_validation":4,"raw_false_positive_risk":1,"raw_reclassification_need":0,"stage2_actionable_bonus_before":2.0,"stage2_actionable_bonus_after":2.0,"simulated_route":"KeepStage2PostResolution4B"}
```

---

## 8. Current calibrated profile stress test

The Stage2 false-positive passport gate held:

```text
label without bridge -> Stage2 bonus zero
company-specific bridge with controlled MAE -> keep Stage2
real bridge but bad timing / refresh missing -> local 4B
wrong archetype bridge -> reclassify
formal tender bridge -> escape hatch
```

### Rule candidate retained, not newly proposed

```text
R13_STAGE2_FALSE_POSITIVE_BRIDGE_PASSPORT_GATE_V11_HELD_OUT

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
if label_only == true
and MFE_90D_pct < +10
and MAE_90D_pct <= -20:
    route = Stage2_FalsePositive_Block
```

```text
if label_only == true
and MFE_30D_pct >= +20
and MAE_90D_pct <= -25:
    route = Stage2_FalsePositive_Block_or_Local4B_then_Block
```

```text
if bridge_belongs_to_other_archetype == true:
    cap_selected_archetype_contribution = true
    require_reclassification = true
```

```text
if later_evidence_after_trigger == true:
    do_not_backfill_to_original_trigger = true
    require_new_trigger_from_later_evidence_date = true
```

---

## 9. Batch Ingest Self-Audit

```yaml
expected_v12_result_file: true
filename_pattern_pass: true
metadata_filename_consistency: pass
jsonl_trigger_row_count: 13
calibration_usable_trigger_count: 13
representative_trigger_count: 0
new_weight_evidence_candidate_count: 0
guardrail_candidate_count: 13
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
  - R13_STAGE2_FALSE_POSITIVE_BRIDGE_PASSPORT_GATE_V11_HELD_OUT
existing_axis_weakened: null
one_line_summary: "This loop adds 0 new independent cases and validates the R13 Stage2 false-positive bridge-passport gate across C04/C15/C18/C26/C29/C30/C31/C32."
```

---

## 11. Deferred Coding Agent Handoff Prompt

```text
Do not patch production scoring from this MD alone. Treat R13 Stage2 false-positive loop 11 as holdout validation only. Batch it with R13 Stage2 false-positive loop 10, R13 accounting-trust loops 11~13, R13 high-MAE loop 8, R13 4B/4C loop 103, and source loops C04/C15/C18/C26/C29/C30/C31/C32 from this session. If exact same_entry_group_id rows already exist, dedupe them. Preserve the cross-archetype Stage2 false-positive bridge-passport gate, but do not create a new weight delta from this loop because no new independent case was added.
```

---

## 12. Next research state

```yaml
completed_round: R13
completed_loop: 11
selection_basis: docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket: Priority 0
round_schedule_status: coverage_index_selected
round_sector_consistency: pass
next_recommended_archetypes:
  - R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL
  - R13_CROSS_ARCHETYPE_4B_4C_REDTEAM
  - C18_CONSUMER_EXPORT_CHANNEL_REORDER
  - C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE
  - C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE
```
