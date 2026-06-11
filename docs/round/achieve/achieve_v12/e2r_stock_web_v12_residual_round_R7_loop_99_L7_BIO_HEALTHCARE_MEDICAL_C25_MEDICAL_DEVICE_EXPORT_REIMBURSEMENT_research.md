# E2R Stock-Web V12 Residual Research — R7 Loop 99 C25

```yaml
schema_family: v12_sector_archetype_residual
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
selected_round: R7
selected_loop: "99"
large_sector_id: L7_BIO_HEALTHCARE_MEDICAL
canonical_archetype_id: C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT
fine_archetype_id: AESTHETIC_DEVICE_EXPORT_INSTALLED_BASE_CONSUMABLE_MARGIN_BRIDGE_VS_DENTAL_DIGITAL_DEVICE_EXPORT_LABEL_HIGH_MAE
selection_basis: docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket: Priority 0
price_source: Songdaiki/stock-web
price_basis: tradable_raw
price_adjustment_status: raw_unadjusted_marcap
stock_web_manifest_max_date: "2026-02-20"
production_scoring_changed: false
shadow_weight_only: true
handoff_prompt_embedded: true
handoff_prompt_executed_now: false
```

## 1. Coverage / duplicate decision

`C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT` remains a Priority-0 under-covered archetype in the no-repeat index. Existing representative symbols listed for C25 are `145720`, `214150`, `099190`, and `336570`; this loop therefore uses new symbols `335890`, `043150`, and `228670`.

Existing registry shows C25 files up to `R7 loop 98`, so this file uses:

```text
selected_loop = 99
```

This is a historical calibration artifact only. It is not live stock discovery, not a stock recommendation, not auto-trading, and not a production scoring change.

## 2. Research thesis

C25 should not treat every Korean medical-device label as the same rerating path.

The useful C25 bridge is:

```text
device export or reimbursement headline
  -> installed base / channel reorder / reimbursement acceptance / consumable repeat demand
  -> margin and revision bridge
  -> low-to-controlled MAE with sustained MFE
```

The failure mode is:

```text
medical device / dental / digital dentistry vocabulary
  -> short price bounce or no MFE
  -> no reimbursement, consumable, or revision bridge
  -> high MAE and later 4B / false Stage2
```

## 3. Price-source validation

All price rows are from `Songdaiki/stock-web`:

```text
price_source = Songdaiki/stock-web
price_basis = tradable_raw
price_adjustment_status = raw_unadjusted_marcap
stock_web_manifest_max_date = 2026-02-20
```

No `stock_agent` source code was opened or modified. The `stock_agent` research artifact was used only for coverage gap and duplicate avoidance.

## 4. Case summary table

| symbol | company | trigger_type | entry_date | entry_price | MFE/MAE 30D % | MFE/MAE 90D % | MFE/MAE 180D % | classification |
|---|---|---|---:|---:|---:|---:|---:|---|
| 335890 | 비올 | Stage2-Actionable | 2024-03-13 | 8,480 | 41.86 / -13.92 | 41.86 / -13.92 | 41.86 / -21.82 | positive_with_4B_watch |
| 043150 | 바텍 | Stage2-FalsePositive | 2024-05-17 | 30,150 | 1.49 / -13.1 | 1.49 / -24.71 | 1.49 / -38.64 | counterexample |
| 228670 | 레이 | Stage2-FalsePositive | 2024-03-13 | 17,020 | 3.88 / -23.21 | 3.88 / -39.07 | 3.88 / -70.15 | counterexample |

## 5. Case notes

### 5.1 비올 / 335890 — aesthetic device export bridge, but with 4B watch

`비올` is used as a positive C25 sample because the aesthetic-device / installed-base / export vocabulary produced a strong forward MFE. The price path nevertheless shows why this is not an automatic Green: after the early run, the 180D low moved far below entry. C25 should therefore allow Stage2-Actionable when the installed-base/export bridge is present, but it should also keep a local 4B watch when the move becomes vertical without continuing margin confirmation.

### 5.2 바텍 / 043150 — dental imaging export label without durable bridge

`바텍` is used as a counterexample. Dental imaging / dental device / export vocabulary alone did not produce meaningful forward MFE. The path decayed from the entry area into a large 90D/180D MAE. This supports blocking Stage2-Actionable when a dental device label lacks fresh reimbursement, consumable, or revenue-revision confirmation.

### 5.3 레이 / 228670 — digital dental label high-MAE false positive

`레이` is used as a more severe counterexample. The digital dentistry/device label had a brief bounce but the subsequent path moved into a high-MAE drawdown. This is a useful C25 guardrail case for separating true installed-base monetization from vocabulary-only device stories.

## 6. JSONL trigger rows

```jsonl
{"MAE_180D_pct": -21.82, "MAE_30D_pct": -13.92, "MAE_90D_pct": -13.92, "MFE_180D_pct": 41.86, "MFE_30D_pct": 41.86, "MFE_90D_pct": 41.86, "calibration_usable": true, "canonical_archetype_id": "C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT", "case_id": "C25_335890_2024_03_13_AESTHETIC_DEVICE_EXPORT_INSTALLED_BASE", "classification": "positive_with_4B_watch", "company_name": "비올", "corporate_action_contamination": false, "current_profile_verdict": "stress_test_required", "entry_date": "2024-03-13", "entry_price": 8480, "evidence_family": "aesthetic_device_export_installed_base_consumable_margin_bridge", "fine_archetype_id": "AESTHETIC_DEVICE_EXPORT_INSTALLED_BASE_CONSUMABLE_MARGIN_BRIDGE_VS_DENTAL_DIGITAL_DEVICE_EXPORT_LABEL_HIGH_MAE", "forward_high_180D": 12030, "forward_high_30D": 12030, "forward_high_90D": 12030, "forward_low_180D": 6630, "forward_low_30D": 7300, "forward_low_90D": 7300, "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "notes": "Aesthetic device export/installed-base vocabulary produced strong early MFE, but the later 180D low requires local 4B watch unless margin/consumable repeat revenue keeps confirming.", "novelty_key": "335890|C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT|Stage2-Actionable|2024-03-13|2024-03-13|aesthetic_device_export_installed_base_consumable_margin_bridge", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_source": "Songdaiki/stock-web", "row_type": "trigger", "schema_family": "v12_trigger_row", "selected_loop": "99", "selected_round": "R7", "symbol": "335890", "trigger_date": "2024-03-13", "trigger_family": "aesthetic_device_export_reorder_margin_bridge", "trigger_type": "Stage2-Actionable"}
{"MAE_180D_pct": -38.64, "MAE_30D_pct": -13.1, "MAE_90D_pct": -24.71, "MFE_180D_pct": 1.49, "MFE_30D_pct": 1.49, "MFE_90D_pct": 1.49, "calibration_usable": true, "canonical_archetype_id": "C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT", "case_id": "C25_043150_2024_05_17_DENTAL_IMAGING_EXPORT_WEAK_BRIDGE", "classification": "counterexample", "company_name": "바텍", "corporate_action_contamination": false, "current_profile_verdict": "stress_test_required", "entry_date": "2024-05-17", "entry_price": 30150, "evidence_family": "dental_imaging_export_without_reimbursement_consumable_or_revision_bridge", "fine_archetype_id": "AESTHETIC_DEVICE_EXPORT_INSTALLED_BASE_CONSUMABLE_MARGIN_BRIDGE_VS_DENTAL_DIGITAL_DEVICE_EXPORT_LABEL_HIGH_MAE", "forward_high_180D": 30600, "forward_high_30D": 30600, "forward_high_90D": 30600, "forward_low_180D": 18500, "forward_low_30D": 26200, "forward_low_90D": 22700, "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "notes": "Dental imaging/export label alone failed to create forward MFE; the path shows steady downside and supports a Stage2 block without new reimbursement/consumable/revision confirmation.", "novelty_key": "043150|C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT|Stage2-FalsePositive|2024-05-17|2024-05-17|dental_imaging_export_without_reimbursement_consumable_or_revision_bridge", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_source": "Songdaiki/stock-web", "row_type": "trigger", "schema_family": "v12_trigger_row", "selected_loop": "99", "selected_round": "R7", "symbol": "043150", "trigger_date": "2024-05-17", "trigger_family": "dental_device_export_vocabulary_weak_bridge", "trigger_type": "Stage2-FalsePositive"}
{"MAE_180D_pct": -70.15, "MAE_30D_pct": -23.21, "MAE_90D_pct": -39.07, "MFE_180D_pct": 3.88, "MFE_30D_pct": 3.88, "MFE_90D_pct": 3.88, "calibration_usable": true, "canonical_archetype_id": "C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT", "case_id": "C25_228670_2024_03_13_DIGITAL_DENTAL_EXPORT_FALSE_POSITIVE", "classification": "counterexample", "company_name": "레이", "corporate_action_contamination": false, "current_profile_verdict": "stress_test_required", "entry_date": "2024-03-13", "entry_price": 17020, "evidence_family": "digital_dental_export_label_without_cash_conversion_or_reimbursement_bridge", "fine_archetype_id": "AESTHETIC_DEVICE_EXPORT_INSTALLED_BASE_CONSUMABLE_MARGIN_BRIDGE_VS_DENTAL_DIGITAL_DEVICE_EXPORT_LABEL_HIGH_MAE", "forward_high_180D": 17680, "forward_high_30D": 17680, "forward_high_90D": 17680, "forward_low_180D": 5080, "forward_low_30D": 13070, "forward_low_90D": 10370, "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "notes": "Digital dental/device export vocabulary had a brief bounce but not a durable revenue/reimbursement bridge; the 180D drawdown is a hard high-MAE guardrail sample.", "novelty_key": "228670|C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT|Stage2-FalsePositive|2024-03-13|2024-03-13|digital_dental_export_label_without_cash_conversion_or_reimbursement_bridge", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_source": "Songdaiki/stock-web", "row_type": "trigger", "schema_family": "v12_trigger_row", "selected_loop": "99", "selected_round": "R7", "symbol": "228670", "trigger_date": "2024-03-13", "trigger_family": "digital_dental_device_label_high_MAE", "trigger_type": "Stage2-FalsePositive"}
```

## 7. Aggregate metrics

```json
{
  "row_type": "aggregate_metric",
  "selected_round": "R7",
  "selected_loop": "99",
  "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL",
  "canonical_archetype_id": "C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT",
  "fine_archetype_id": "AESTHETIC_DEVICE_EXPORT_INSTALLED_BASE_CONSUMABLE_MARGIN_BRIDGE_VS_DENTAL_DIGITAL_DEVICE_EXPORT_LABEL_HIGH_MAE",
  "new_independent_case_count": 3,
  "reused_case_count": 0,
  "same_archetype_new_symbol_count": 3,
  "same_archetype_new_trigger_family_count": 3,
  "calibration_usable_case_count": 3,
  "calibration_usable_trigger_count": 3,
  "positive_case_count": 1,
  "counterexample_count": 2,
  "current_profile_error_count": 2,
  "local_4B_watch_case_count": 1,
  "high_MAE_guardrail_case_count": 2,
  "do_not_propose_new_weight_delta": false
}
```

## 8. Score-return alignment

```text
335890:
  score-return alignment = partial pass
  reason = early MFE is strong, but 180D MAE says Stage2 should carry a 4B proximity watch unless margin/reorder evidence persists.

043150:
  score-return alignment = fail for price-only Stage2
  reason = weak MFE and large 90D/180D MAE; dental imaging vocabulary without reimbursement/revision bridge should not pass.

228670:
  score-return alignment = fail for price-only Stage2
  reason = low MFE and very high MAE; digital dental vocabulary must be capped unless cash conversion or reimbursement evidence appears.
```

## 9. Residual contribution summary

```text
loop_contribution_label = canonical_archetype_rule_candidate

existing_axis_strengthened:
  - C25_installed_base_consumable_export_margin_bridge_requirement
  - C25_dental_device_export_label_stage2_block_without_reimbursement_or_revision
  - C25_digital_dental_high_MAE_guardrail
  - C25_vertical_MFE_local_4B_watch

new_axis_proposed = null
existing_axis_weakened = null
```

## 10. Shadow-weight note

This loop does not propose a production score change. If later batched with other C25 loops, the safe direction is not a broad C25 weight increase. The safe direction is a narrower conditional rule:

```text
raise confidence only when:
  installed base or reimbursement acceptance
  + export/channel reorder
  + consumable or recurring revenue bridge
  + margin/revision confirmation
are present.

block or cap when:
  dental / digital dental / device export vocabulary appears
  without reimbursement, consumable, or revision bridge.
```

## 11. Deferred Coding Agent Handoff Prompt

Do not execute this section in the current research session.

```text
You are the coding agent for stock_agent. Ingest this MD only as a historical calibration artifact.

Tasks:
1. Parse JSONL trigger rows.
2. Validate stock-web price_source fields.
3. Deduplicate using:
   symbol + canonical_archetype_id + trigger_type + trigger_date + entry_date + evidence_family.
4. Add usable rows to the v12 calibration corpus if they pass schema validation.
5. Treat this file as shadow calibration evidence only.
6. Do not change production scoring unless a later explicit promotion plan aggregates enough independent C25 evidence.
```
