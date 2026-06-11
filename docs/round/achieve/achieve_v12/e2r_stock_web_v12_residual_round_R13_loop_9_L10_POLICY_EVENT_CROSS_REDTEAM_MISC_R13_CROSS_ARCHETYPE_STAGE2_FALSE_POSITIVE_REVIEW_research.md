# E2R v12 R13 cross-archetype residual calibration research

## 0. Execution metadata

```yaml
schema_family: v12_sector_archetype_residual
selected_round: R13
selected_loop: 9
large_sector_id: L10_POLICY_EVENT_CROSS_REDTEAM_MISC
canonical_archetype_id: R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW
fine_archetype_id: OPERATING_CASH_BRIDGE_STAGE2_FALSE_POSITIVE_GATE_CONSUMER_PLATFORM_MOBILITY_CONSTRUCTION_FINANCIAL_INSURANCE
selection_basis:
  main_execution_prompt: docs/core/e2r_v12_prompt_round_scheduler_corrected.txt
  no_repeat_index: docs/core/V12_Research_No_Repeat_Index.md
web_raw_fetch_status_this_turn:
  main_execution_prompt: read_ok
  no_repeat_index: read_ok
selected_priority_bucket: Priority 0
round_schedule_status: coverage_index_selected
round_sector_consistency: pass
price_source: Songdaiki/stock-web
price_basis: tradable_raw
price_adjustment_status: raw_unadjusted_marcap
stock_web_manifest_max_date: 2026-02-20
production_scoring_changed: false
shadow_weight_only: true
```

R13 is a cross-archetype checkpoint, not a sector-specific positive discovery round. This loop tests the newest C18, C26, C29, C30, C21 and C22 sector-rule files through a single Stage2 false-positive gate:

```text
Does the label have a company-specific operating cash bridge?
```

If the answer is yes, Stage2 can survive. If the answer is no, Stage2 must be capped, reclassified or blocked.

The previous local `R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW` run reached loop 8. This continuation is therefore `loop 9`.

---

## 1. Research thesis

Stage2 false positives usually happen when the model mistakes a vocabulary label for a working bridge.

```text
export label
platform label
mobility label
builder label
low-PBR label
insurance label
```

These labels are not useless. They are signposts. But Stage2 should require that the signpost points to an actual accounting road:

```text
sell-through / reorder / inventory normalization / OPM
owned ad inventory / ARPU / retention / margin leverage
volume / mix / customer order / utilization / margin
refinancing / debt-service / guarantee relief / cash conversion
ROE / CET1 / payout / buyback / capital return
reserve quality / CSM / solvency / loss ratio / capital return
```

The rule is simple:

```text
label + bridge = possible Stage2
label without bridge = Watch, reclassify or block
```

---

## 2. Validation scope

```yaml
validation_scope:
  required_cases: 8
  actual_cases: 10
  source_archetypes:
    - C18_CONSUMER_EXPORT_CHANNEL_REORDER
    - C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE
    - C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE
    - C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK
    - C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN
    - C22_INSURANCE_RATE_CYCLE_RESERVE
  price_windows:
    - 30D MFE/MAE
    - 90D MFE/MAE
    - 180D MFE/MAE
  output_use:
    - Stage2 false-positive review
    - label-vs-bridge gate
    - reclassification/cap logic
    - local 4B vs hard block split
    - no production scoring changes
```

---

## 3. Source validation

```yaml
stock_web_manifest:
  source_name: FinanceData/marcap
  price_adjustment_status: raw_unadjusted_marcap
  max_date: 2026-02-20
  calibration_shard_root: atlas/ohlcv_tradable_by_symbol_year
  caveat: Raw/unadjusted OHLC; corporate-action contaminated windows blocked by default.
```

Local stock-web-derived row provenance:

```yaml
reused_price_rows_from_current_session:
  - R5/C18 loop 142
  - R8/C26 loop 100
  - R9/C29 loop 103
  - R10/C30 loop 3
  - R6/C21 loop 112
  - R6/C22 loop 111
  - R13 accounting-trust loop 10
reason:
  - all reused rows were calculated from Songdaiki/stock-web tradable raw 1D OHLC
  - this file changes canonical scope to R13 Stage2 false-positive review
  - exact source-archetype keys should be deduped separately from this R13 guardrail key
  - no production scoring changed
```

---

## 4. Trigger rows

```jsonl
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","round":"R13","loop":9,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW","fine_archetype_id":"CONSUMER_EXPORT_REORDER_BRIDGE_STAGE2_ESCAPE_HATCH","source_archetype_id":"C18_CONSUMER_EXPORT_CHANNEL_REORDER","symbol":"003230","name":"삼양식품","trigger_type":"Stage2-Actionable","entry_date":"2024-05-20","entry_close":502000,"price_basis":"tradable_raw","mfe_30d_pct":43.03,"mae_30d_pct":-4.68,"mfe_90d_pct":43.03,"mae_90d_pct":-9.26,"mfe_180d_pct":59.36,"mae_180d_pct":-9.26,"forward_high_30d":718000,"forward_low_30d":478500,"forward_high_90d":718000,"forward_low_90d":455500,"forward_high_180d":800000,"forward_low_180d":455500,"calibration_usable":true,"case_role":"positive_escape_hatch","novelty_key":"R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW|003230|Stage2-Actionable|2024-05-20","stage2_error":"none; export sell-through and reorder bridge validated","route":"KeepStage2_ExportReorderBridge"}
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","round":"R13","loop":9,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW","fine_archetype_id":"BRAND_EXPORT_CHANNEL_INVENTORY_LABEL_STAGE2_BLOCK","source_archetype_id":"C18_CONSUMER_EXPORT_CHANNEL_REORDER","symbol":"383220","name":"F&F","trigger_type":"Stage2-FalsePositive","entry_date":"2024-07-17","entry_close":74000,"price_basis":"tradable_raw","mfe_30d_pct":3.24,"mae_30d_pct":-33.99,"mfe_90d_pct":3.24,"mae_90d_pct":-33.99,"mfe_180d_pct":3.24,"mae_180d_pct":-33.99,"forward_high_30d":76400,"forward_low_30d":48850,"forward_high_90d":76400,"forward_low_90d":48850,"forward_high_180d":76400,"forward_low_180d":48850,"calibration_usable":true,"case_role":"hard_false_positive","novelty_key":"R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW|383220|Stage2-FalsePositive|2024-07-17","stage2_error":"brand/export-channel label lacked sell-through and inventory bridge","route":"Stage2FalsePositiveBlock"}
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","round":"R13","loop":9,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW","fine_archetype_id":"OWNED_PLATFORM_ARPU_MARGIN_STAGE2_ESCAPE_HATCH","source_archetype_id":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE","symbol":"035420","name":"NAVER","trigger_type":"Stage2-Actionable","entry_date":"2024-11-08","entry_close":174600,"price_basis":"tradable_raw","mfe_30d_pct":26.00,"mae_30d_pct":-1.78,"mfe_90d_pct":34.88,"mae_90d_pct":-1.78,"mfe_180d_pct":34.88,"mae_180d_pct":-1.78,"forward_high_30d":220000,"forward_low_30d":171500,"forward_high_90d":235500,"forward_low_90d":171500,"forward_high_180d":235500,"forward_low_180d":171500,"calibration_usable":true,"case_role":"positive_escape_hatch","novelty_key":"R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW|035420|Stage2-Actionable|2024-11-08","stage2_error":"none; owned platform inventory, ARPU and margin bridge validated","route":"KeepStage2_OwnedPlatformBridge"}
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","round":"R13","loop":9,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW","fine_archetype_id":"ADTECH_MARKETING_SERVICE_LABEL_WITHOUT_OWNED_INVENTORY_BLOCK","source_archetype_id":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE","symbol":"214270","name":"FSN","trigger_type":"Stage2-FalsePositive","entry_date":"2024-07-18","entry_close":2105,"price_basis":"tradable_raw","mfe_30d_pct":16.63,"mae_30d_pct":-26.37,"mfe_90d_pct":19.00,"mae_90d_pct":-26.37,"mfe_180d_pct":19.00,"mae_180d_pct":-49.64,"forward_high_30d":2455,"forward_low_30d":1550,"forward_high_90d":2505,"forward_low_90d":1550,"forward_high_180d":2505,"forward_low_180d":1060,"calibration_usable":true,"case_role":"hard_false_positive","novelty_key":"R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW|214270|Stage2-FalsePositive|2024-07-18","stage2_error":"adtech/marketing-service label lacked owned inventory, ARPU and margin leverage","route":"Stage2FalsePositiveBlock"}
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","round":"R13","loop":9,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW","fine_archetype_id":"OEM_VOLUME_MIX_MARGIN_STAGE2_ESCAPE_HATCH","source_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","symbol":"000270","name":"기아","trigger_type":"Stage2-Actionable","entry_date":"2024-01-25","entry_close":93000,"price_basis":"tradable_raw","mfe_30d_pct":41.61,"mae_30d_pct":-7.42,"mfe_90d_pct":45.16,"mae_90d_pct":-7.42,"mfe_180d_pct":45.16,"mae_180d_pct":-7.42,"forward_high_30d":131700,"forward_low_30d":86100,"forward_high_90d":135000,"forward_low_90d":86100,"forward_high_180d":135000,"forward_low_180d":86100,"calibration_usable":true,"case_role":"positive_escape_hatch","novelty_key":"R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW|000270|Stage2-Actionable|2024-01-25","stage2_error":"none; OEM volume, mix, margin and cash bridge validated","route":"KeepStage2_OEMMarginBridge"}
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","round":"R13","loop":9,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW","fine_archetype_id":"AUTO_PARTS_THEME_WITHOUT_DURABLE_MARGIN_BRIDGE_4B_THEN_BLOCK","source_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","symbol":"010690","name":"화신","trigger_type":"Stage2-Watch","entry_date":"2024-06-12","entry_close":11690,"price_basis":"tradable_raw","mfe_30d_pct":35.93,"mae_30d_pct":-4.53,"mfe_90d_pct":35.93,"mae_90d_pct":-30.28,"mfe_180d_pct":35.93,"mae_180d_pct":-47.39,"forward_high_30d":15890,"forward_low_30d":11160,"forward_high_90d":15890,"forward_low_90d":8150,"forward_high_180d":15890,"forward_low_180d":6150,"calibration_usable":true,"case_role":"local_4B_to_block","novelty_key":"R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW|010690|Stage2-Watch|2024-06-12","stage2_error":"auto-parts theme had MFE but lacked durable customer-volume and margin bridge","route":"Local4BThenBlockIfNoRefresh"}
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","round":"R13","loop":9,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW","fine_archetype_id":"CONSTRUCTION_DELAYED_REBOUND_NOT_IMMEDIATE_STAGE2","source_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","symbol":"294870","name":"HDC현대산업개발","trigger_type":"Stage2-Watch","entry_date":"2024-05-13","entry_close":17920,"price_basis":"tradable_raw","mfe_30d_pct":2.12,"mae_30d_pct":-6.58,"mfe_90d_pct":37.28,"mae_90d_pct":-6.58,"mfe_180d_pct":57.37,"mae_180d_pct":-6.58,"forward_high_30d":18300,"forward_low_30d":16740,"forward_high_90d":24600,"forward_low_90d":16740,"forward_high_180d":28200,"forward_low_180d":16740,"calibration_usable":true,"case_role":"delayed_local_4B","novelty_key":"R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW|294870|Stage2-Watch|2024-05-13","stage2_error":"delayed rebound should not be backfilled as immediate Stage2 without issuer-specific cash bridge","route":"DelayedLocal4B_DoNotBackfillImmediateStage2"}
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","round":"R13","loop":9,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW","fine_archetype_id":"LOW_PBR_BROKERAGE_LABEL_WITHOUT_CAPITAL_RETURN_BLOCK","source_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","symbol":"006800","name":"미래에셋증권","trigger_type":"Stage2-FalsePositive","entry_date":"2024-02-26","entry_close":8680,"price_basis":"tradable_raw","mfe_30d_pct":5.53,"mae_30d_pct":-10.71,"mfe_90d_pct":5.53,"mae_90d_pct":-20.16,"mfe_180d_pct":5.53,"mae_180d_pct":-23.96,"forward_high_30d":9160,"forward_low_30d":7750,"forward_high_90d":9160,"forward_low_90d":6930,"forward_high_180d":9160,"forward_low_180d":6600,"calibration_usable":true,"case_role":"hard_false_positive","novelty_key":"R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW|006800|Stage2-FalsePositive|2024-02-26","stage2_error":"low-PBR brokerage label lacked incremental ROE/capital-return bridge","route":"Stage2FalsePositiveBlock"}
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","round":"R13","loop":9,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW","fine_archetype_id":"INSURANCE_GA_DISTRIBUTION_LABEL_RECLASSIFY_C22_STAGE2_CAP","source_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","symbol":"244920","name":"에이플러스에셋","trigger_type":"Stage2-Watch","entry_date":"2024-05-10","entry_close":4100,"price_basis":"tradable_raw","mfe_30d_pct":9.76,"mae_30d_pct":-2.32,"mfe_90d_pct":9.76,"mae_90d_pct":-13.78,"mfe_180d_pct":14.63,"mae_180d_pct":-13.78,"forward_high_30d":4500,"forward_low_30d":4005,"forward_high_90d":4500,"forward_low_90d":3535,"forward_high_180d":4700,"forward_low_180d":3535,"calibration_usable":true,"case_role":"reclassification_cap","novelty_key":"R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW|244920|Stage2-Watch|2024-05-10","stage2_error":"insurance distribution label is not reserve/CSM/solvency bridge","route":"Stage2Cap_ReclassifyToDistributionCommission"}
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","round":"R13","loop":9,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW","fine_archetype_id":"LIFE_INSURANCE_VALUEUP_LABEL_WITHOUT_CSM_SOLVENCY_BRIDGE_CAP","source_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","symbol":"088350","name":"한화생명","trigger_type":"Stage2-Watch","entry_date":"2024-02-26","entry_close":3060,"price_basis":"tradable_raw","mfe_30d_pct":9.31,"mae_30d_pct":-8.17,"mfe_90d_pct":9.31,"mae_90d_pct":-15.69,"mfe_180d_pct":9.31,"mae_180d_pct":-15.69,"forward_high_30d":3345,"forward_low_30d":2810,"forward_high_90d":3345,"forward_low_90d":2580,"forward_high_180d":3345,"forward_low_180d":2580,"calibration_usable":true,"case_role":"stage2_cap","novelty_key":"R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW|088350|Stage2-Watch|2024-02-26","stage2_error":"life-insurance Value-up label lacked CSM/solvency/capital-return bridge","route":"Stage2Cap"}
```

---

## 5. Case analysis

### 5.1 Samyang Foods / 003230 — Stage2 escape hatch

Export label is not the reason this survives. The reason is sell-through, reorder and margin.

```text
route = KeepStage2_ExportReorderBridge
```

### 5.2 F&F / 383220 — consumer brand label false positive

This row blocks brand/export-channel vocabulary without sell-through and inventory normalization.

```text
route = Stage2FalsePositiveBlock
```

### 5.3 NAVER / 035420 — owned platform escape hatch

Owned ad inventory, ARPU and commerce conversion make this a valid Stage2 bridge.

```text
route = KeepStage2_OwnedPlatformBridge
```

### 5.4 FSN / 214270 — adtech label false positive

Advertising exposure is not the same as platform operating leverage.

```text
route = Stage2FalsePositiveBlock
```

### 5.5 Kia / 000270 — mobility bridge escape hatch

Volume, mix, ASP and margin bridge validate Stage2.

```text
route = KeepStage2_OEMMarginBridge
```

### 5.6 Hwashin / 010690 — auto-parts theme 4B then block

High MFE came first, but the durable bridge failed. Local 4B first, block if no refresh.

```text
route = Local4BThenBlockIfNoRefresh
```

### 5.7 HDC Hyundai Development / 294870 — delayed rebound, not immediate Stage2

Later rebound should not be backfilled into the trigger date.

```text
route = DelayedLocal4B_DoNotBackfillImmediateStage2
```

### 5.8 Mirae Asset Securities / 006800 — low-PBR brokerage false positive

Cheapness did not become ROE or capital-return execution.

```text
route = Stage2FalsePositiveBlock
```

### 5.9 A Plus Asset / 244920 — insurance label reclassification

GA distribution commission economics belong outside C22 reserve-cycle scoring.

```text
route = Stage2Cap_ReclassifyToDistributionCommission
```

### 5.10 Hanwha Life / 088350 — life-insurance Value-up cap

Insurance Value-up label needs CSM, solvency, reserve and payout bridge.

```text
route = Stage2Cap
```

---

## 6. Score-return alignment

```yaml
new_independent_case_count: 10
calibration_usable_case_count: 10
calibration_usable_trigger_count: 10
positive_escape_hatch_count: 3
local_4B_or_delayed_watch_count: 2
stage2_cap_or_reclassification_count: 3
stage2_false_positive_count: 3
current_profile_error_count: 7
```

| symbol | source | route | 90D MFE/MAE | 180D MFE/MAE | lesson |
|---|---:|---:|---:|---:|---|
| 003230 | C18 | keep Stage2 | +43.03 / -9.26 | +59.36 / -9.26 | reorder bridge validates |
| 383220 | C18 | hard block | +3.24 / -33.99 | +3.24 / -33.99 | brand label fails |
| 035420 | C26 | keep Stage2 | +34.88 / -1.78 | +34.88 / -1.78 | owned platform bridge validates |
| 214270 | C26 | hard block | +19.00 / -26.37 | +19.00 / -49.64 | adtech label fails |
| 000270 | C29 | keep Stage2 | +45.16 / -7.42 | +45.16 / -7.42 | OEM margin bridge validates |
| 010690 | C29 | 4B -> block | +35.93 / -30.28 | +35.93 / -47.39 | theme MFE without durable bridge |
| 294870 | C30 | delayed 4B | +37.28 / -6.58 | +57.37 / -6.58 | delayed rebound not immediate Stage2 |
| 006800 | C21 | hard block | +5.53 / -20.16 | +5.53 / -23.96 | low-PBR label lacks capital-return bridge |
| 244920 | C22 | reclassify cap | +9.76 / -13.78 | +14.63 / -13.78 | GA distribution is not reserve-cycle bridge |
| 088350 | C22 | Stage2 cap | +9.31 / -15.69 | +9.31 / -15.69 | life Value-up label lacks CSM/solvency bridge |

---

## 7. Raw component score breakdown

```jsonl
{"row_type":"score_simulation","symbol":"003230","raw_label_signal":2,"raw_company_specific_bridge":5,"raw_accounting_trust":5,"raw_validation":5,"raw_false_positive_risk":0,"stage2_actionable_bonus_before":2.0,"stage2_actionable_bonus_after":2.0,"simulated_route":"KeepStage2_ExportReorderBridge"}
{"row_type":"score_simulation","symbol":"383220","raw_label_signal":3,"raw_company_specific_bridge":0,"raw_accounting_trust":0,"raw_validation":0,"raw_false_positive_risk":5,"stage2_actionable_bonus_before":2.0,"stage2_actionable_bonus_after":0.0,"simulated_route":"Stage2FalsePositiveBlock"}
{"row_type":"score_simulation","symbol":"035420","raw_label_signal":2,"raw_company_specific_bridge":5,"raw_accounting_trust":5,"raw_validation":4,"raw_false_positive_risk":0,"stage2_actionable_bonus_before":2.0,"stage2_actionable_bonus_after":2.0,"simulated_route":"KeepStage2_OwnedPlatformBridge"}
{"row_type":"score_simulation","symbol":"214270","raw_label_signal":4,"raw_company_specific_bridge":0,"raw_accounting_trust":0,"raw_validation":1,"raw_false_positive_risk":5,"stage2_actionable_bonus_before":2.0,"stage2_actionable_bonus_after":0.0,"simulated_route":"Stage2FalsePositiveBlock"}
{"row_type":"score_simulation","symbol":"000270","raw_label_signal":2,"raw_company_specific_bridge":5,"raw_accounting_trust":5,"raw_validation":5,"raw_false_positive_risk":0,"stage2_actionable_bonus_before":2.0,"stage2_actionable_bonus_after":2.0,"simulated_route":"KeepStage2_OEMMarginBridge"}
{"row_type":"score_simulation","symbol":"010690","raw_label_signal":4,"raw_company_specific_bridge":1,"raw_accounting_trust":1,"raw_validation":2,"raw_false_positive_risk":4,"stage2_actionable_bonus_before":2.0,"stage2_actionable_bonus_after":1.0,"simulated_route":"Local4BThenBlockIfNoRefresh"}
{"row_type":"score_simulation","symbol":"294870","raw_label_signal":3,"raw_company_specific_bridge":1,"raw_accounting_trust":1,"raw_validation":3,"raw_false_positive_risk":3,"stage2_actionable_bonus_before":2.0,"stage2_actionable_bonus_after":1.0,"simulated_route":"DelayedLocal4B"}
{"row_type":"score_simulation","symbol":"006800","raw_label_signal":4,"raw_company_specific_bridge":0,"raw_accounting_trust":0,"raw_validation":0,"raw_false_positive_risk":5,"stage2_actionable_bonus_before":2.0,"stage2_actionable_bonus_after":0.0,"simulated_route":"Stage2FalsePositiveBlock"}
{"row_type":"score_simulation","symbol":"244920","raw_label_signal":3,"raw_company_specific_bridge":2,"raw_accounting_trust":1,"raw_validation":1,"raw_false_positive_risk":4,"stage2_actionable_bonus_before":2.0,"stage2_actionable_bonus_after":0.0,"simulated_route":"Stage2Cap_Reclassify"}
{"row_type":"score_simulation","symbol":"088350","raw_label_signal":4,"raw_company_specific_bridge":1,"raw_accounting_trust":1,"raw_validation":0,"raw_false_positive_risk":4,"stage2_actionable_bonus_before":2.0,"stage2_actionable_bonus_after":0.0,"simulated_route":"Stage2Cap"}
```

---

## 8. Current calibrated profile stress test

### Existing error risk

The current profile can still over-open Stage2 on familiar labels:

```text
K-food / brand
platform / adtech
mobility / parts
construction / builder
low-PBR / Value-up
insurance / GA
```

The guardrail should ask a mechanical question:

```text
What crosses into the company’s accounts?
```

If the answer is not sell-through, ARPU, margin, volume, cash conversion, capital return or reserve/solvency economics, Stage2 should not be paid.

### Rule candidate

```text
R13_STAGE2_FALSE_POSITIVE_LABEL_TO_ACCOUNTING_BRIDGE_GATE_V9

if trigger_label_exists == true
and company_specific_accounting_bridge == false:
    stage2_actionable_bonus = 0
    max_stage = Stage2-Watch
```

```text
if company_specific_accounting_bridge == true
and MFE_90D_pct >= +20
and MAE_90D_pct > -10:
    keep_stage2_actionable_bonus = true
```

```text
if MFE_30D_pct >= +30
and MAE_90D_pct <= -20
and durable_bridge_refresh == false:
    route = local_4B_then_block_if_no_refresh
```

```text
if MFE_90D_pct < +10
and MAE_90D_pct <= -20
and company_specific_accounting_bridge == false:
    route = Stage2_FalsePositive_Block
```

```text
if bridge_belongs_to_other_archetype == true:
    cap_selected_archetype_contribution = true
    require_reclassification = true
```

```text
if MFE_30D_pct < +5
and MFE_90D_pct >= +25
and bridge_refreshed_later == true:
    route = delayed_local_4B
    do_not_backfill_as_immediate_Stage2 = true
```

---

## 9. Residual contribution summary

```yaml
do_not_propose_new_weight_delta: false
sector_specific_rule_candidate: false
canonical_archetype_rule_candidate: false
cross_archetype_rule_candidate: true
loop_contribution_label: cross_archetype_stage2_false_positive_guardrail_candidate
new_axis_proposed: R13_STAGE2_FALSE_POSITIVE_LABEL_TO_ACCOUNTING_BRIDGE_GATE_V9
existing_axis_strengthened:
  - label_without_accounting_bridge_stage2_block
  - company_specific_bridge_stage2_escape_hatch
  - high_MFE_but_bridge_unrefreshed_local_4B_then_block
  - reclassification_guard_for_wrong_archetype_bridge
  - delayed_rebound_do_not_backfill_stage2
existing_axis_weakened: null
```

---

## 10. Deferred Coding Agent Handoff Prompt

```text
Do not patch production scoring from this MD alone. Batch this R13 loop with R13 accounting-trust loop 10, C18 loop 142, C26 loop 100, C29 loop 103, C30 loop 3, C21 loop 112 and C22 loop 111. Extract `R13_STAGE2_FALSE_POSITIVE_LABEL_TO_ACCOUNTING_BRIDGE_GATE_V9` as a cross-archetype shadow rule. Preserve Stage2 where a company-specific accounting bridge is validated, but cap/block label-only rows and reclassify rows where the bridge belongs to another archetype.
```

---

## 11. Next research state

```yaml
completed_round: R13
completed_loop: 9
selection_basis: docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket: Priority 0
round_schedule_status: coverage_index_selected
round_sector_consistency: pass
next_recommended_archetypes:
  - C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY
  - C15_MATERIAL_SPREAD_SUPERCYCLE
  - C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION
  - C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN
  - C22_INSURANCE_RATE_CYCLE_RESERVE
```
