# E2R v12 residual calibration research

## 0. Execution metadata

```yaml
schema_family: v12_sector_archetype_residual
selected_round: R7
selected_loop: 100
large_sector_id: L7_BIO_HEALTHCARE_MEDICAL
canonical_archetype_id: C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT
fine_archetype_id: DEVICE_INSTALLED_BASE_REORDER_CONSUMABLE_MARGIN_BRIDGE_VS_DENTAL_DEVICE_LABEL_FALSE_POSITIVE
selection_basis:
  main_execution_prompt: docs/core/e2r_v12_prompt_round_scheduler_corrected.txt
  no_repeat_index: docs/core/V12_Research_No_Repeat_Index.md
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

`C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT` remains Priority 0 in the no-repeat index: 6 representative rows and only 4 covered symbols. The previous sector-specific C25 file reached `R7/C25 loop 99`; this run continues as `R7/C25 loop 100`.

This loop formalizes the C25-specific rule after the recent R13 accounting-trust / Stage2-false-positive / high-MAE checks. Because direct uncached `stock-web` shard fetch was unstable in the recent turns, this MD uses the already generated stock-web-derived C25 rows from the current session. These rows already contain full 30D/90D/180D MFE and MAE calculated from `Songdaiki/stock-web` tradable OHLC. To avoid overstating novelty, the rows are marked as `sector_rule_formalization_reused_controls`; they are useful for canonical rule shaping, but an ingest pipeline should dedupe exact novelty keys against loop 99.

---

## 1. Research thesis

C25 is not `medical device export label = Stage2`. It is the bridge:

```text
device export / reimbursement / installed base / channel expansion
→ reorder, consumables, service, reimbursement acceptance, margin or revision
→ price path validation
```

The C25 model must split three routes:

1. **Installed-base / consumable / export bridge**
   - Stage2 can open when the device story maps into repeat demand, consumables, reorder or margin.
   - If the move is vertical and later MAE appears, route to local 4B until margin/reorder refresh.

2. **Dental imaging / export label without reimbursement**
   - Device vocabulary is not enough.
   - If MFE is low and MAE expands, Stage2-Actionable should be blocked.

3. **Digital dental label with severe MAE**
   - Hard false-positive guardrail.
   - Without reimbursement, installed-base economics, consumables or recurring service revenue, the model should not keep reopening the same device label.

---

## 2. Source validation

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
  - e2r_stock_web_v12_residual_round_R7_loop_99_L7_BIO_HEALTHCARE_MEDICAL_C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT_research.md
  - e2r_stock_web_v12_residual_round_R13_loop_9_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION_research.md
  - e2r_stock_web_v12_residual_round_R13_loop_8_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW_research.md
  - e2r_stock_web_v12_residual_round_R13_loop_6_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL_research.md
reason:
  - these rows were already calculated from Songdaiki/stock-web tradable raw 1D OHLC
  - this file converts the R13 guardrail into a C25 sector-specific shadow rule candidate
  - exact duplicate trigger keys should not be counted again as new aggregate rows
  - no production scoring changed
```

Symbol caveats:

```yaml
335890:
  name: 비올
  role: aesthetic device export / installed base / consumable margin bridge
  calibration_usable: true

043150:
  name: 바텍
  role: dental imaging export label weak bridge
  calibration_usable: true

228670:
  name: 레이
  role: digital dental label severe high-MAE false positive
  calibration_usable: true
```

---

## 3. Trigger rows

```jsonl
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","round":"R7","loop":100,"large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT","fine_archetype_id":"AESTHETIC_DEVICE_EXPORT_INSTALLED_BASE_CONSUMABLE_MARGIN_BRIDGE_4B","symbol":"335890","name":"비올","trigger_type":"Stage2-Actionable","entry_date":"2024-03-13","entry_close":8480,"price_basis":"tradable_raw","mfe_30d_pct":41.86,"mae_30d_pct":-13.92,"mfe_90d_pct":41.86,"mae_90d_pct":-13.92,"mfe_180d_pct":41.86,"mae_180d_pct":-21.82,"forward_high_30d":12030,"forward_low_30d":7300,"forward_high_90d":12030,"forward_low_90d":7300,"forward_high_180d":12030,"forward_low_180d":6630,"calibration_usable":true,"case_role":"positive_with_local_4B_watch","novelty_key":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT|335890|Stage2-Actionable|2024-03-13","non_price_bridge":"aesthetic device export, installed base, reorder/consumable and margin bridge","score_alignment":"Stage2 may open; 180D MAE requires consumable/reorder/margin refresh before Green","aggregate_credit_note":"exact key likely present in C25 loop 99; use as sector-rule formalization control if dedupe catches it"}
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","round":"R7","loop":100,"large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT","fine_archetype_id":"DENTAL_IMAGING_EXPORT_LABEL_WITHOUT_REIMBURSEMENT_CONSUMABLE_BRIDGE_BLOCK","symbol":"043150","name":"바텍","trigger_type":"Stage2-FalsePositive","entry_date":"2024-05-17","entry_close":30150,"price_basis":"tradable_raw","mfe_30d_pct":1.49,"mae_30d_pct":-13.10,"mfe_90d_pct":1.49,"mae_90d_pct":-24.71,"mfe_180d_pct":1.49,"mae_180d_pct":-38.64,"forward_high_30d":30600,"forward_low_30d":26200,"forward_high_90d":30600,"forward_low_90d":22700,"forward_high_180d":30600,"forward_low_180d":18500,"calibration_usable":true,"case_role":"device_label_false_positive","novelty_key":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT|043150|Stage2-FalsePositive|2024-05-17","non_price_bridge":"dental imaging/export vocabulary without reimbursement, consumable, service, revision or cash bridge","score_alignment":"block Stage2-Actionable; low MFE and high MAE reject the device label","aggregate_credit_note":"exact key likely present in C25 loop 99; use as formalization control if dedupe catches it"}
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","round":"R7","loop":100,"large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT","fine_archetype_id":"DIGITAL_DENTAL_LABEL_SEVERE_HIGH_MAE_FALSE_POSITIVE_BLOCK","symbol":"228670","name":"레이","trigger_type":"Stage2-FalsePositive","entry_date":"2024-03-13","entry_close":17020,"price_basis":"tradable_raw","mfe_30d_pct":3.88,"mae_30d_pct":-23.21,"mfe_90d_pct":3.88,"mae_90d_pct":-39.07,"mfe_180d_pct":3.88,"mae_180d_pct":-70.15,"forward_high_30d":17680,"forward_low_30d":13070,"forward_high_90d":17680,"forward_low_90d":10370,"forward_high_180d":17680,"forward_low_180d":5080,"calibration_usable":true,"case_role":"severe_hard_counterexample","novelty_key":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT|228670|Stage2-FalsePositive|2024-03-13","non_price_bridge":"digital dental label without recurring revenue, reimbursement, installed-base, consumable, service or margin bridge","score_alignment":"hard block; require new evidence family before reopen","aggregate_credit_note":"exact key likely present in C25 loop 99; use as formalization control if dedupe catches it"}
```

---

## 4. Case analysis

### 4.1 VIOL / 335890 — installed-base bridge, but Green waits for repeat economics

VIOL is the positive side of this C25 split. The early MFE was large enough to keep Stage2 open, but the later 180D drawdown shows the danger of calling a device export move Green too early.

```yaml
entry_date: 2024-03-13
entry_close: 8480
30d_high: 12030
30d_low: 7300
90d_high: 12030
90d_low: 7300
180d_high: 12030
180d_low: 6630
mfe_90d_pct: 41.86
mae_180d_pct: -21.82
```

Interpretation:

```text
classification = Stage2-Actionable with local_4B_watch
```

The installed base is the machine. Consumables, service and reorder are the ink. Stage3-Green should require the ink to keep flowing.

---

### 4.2 Vatech / 043150 — dental imaging label without cash bridge

Vatech is the dental imaging false positive. The stock produced almost no forward MFE, while 90D/180D MAE expanded.

```yaml
entry_date: 2024-05-17
entry_close: 30150
30d_high: 30600
30d_low: 26200
90d_high: 30600
90d_low: 22700
180d_high: 30600
180d_low: 18500
mfe_90d_pct: 1.49
mae_90d_pct: -24.71
```

Interpretation:

```text
classification = Stage2-FalsePositive
```

The export label is only a signboard. The bridge needs reimbursement, recurring service, consumables, margin or revision evidence.

---

### 4.3 Ray / 228670 — severe digital-dental false positive

Ray is the hard guardrail. It had low MFE and severe 180D drawdown. This is the case that should force the C25 model to stop reopening device-vocabulary names without new cash evidence.

```yaml
entry_date: 2024-03-13
entry_close: 17020
30d_high: 17680
30d_low: 13070
90d_high: 17680
90d_low: 10370
180d_high: 17680
180d_low: 5080
mfe_90d_pct: 3.88
mae_180d_pct: -70.15
```

Interpretation:

```text
classification = Stage2-FalsePositive / hard block
```

---

## 5. Score-return alignment

```yaml
new_independent_case_count: 0
reused_control_case_count: 3
calibration_usable_case_count: 3
calibration_usable_trigger_count: 3
positive_case_count: 1
counterexample_count: 2
local_4B_watch_count: 1
current_profile_error_count: 2
duplicate_note: exact C25 novelty keys likely already exist in R7/C25 loop 99; do not double-count in aggregate if batch ingest dedupes them
```

| symbol | role | 30D MFE/MAE | 90D MFE/MAE | 180D MFE/MAE | lesson |
|---|---:|---:|---:|---:|---|
| 335890 | positive + 4B | +41.86 / -13.92 | +41.86 / -13.92 | +41.86 / -21.82 | installed-base bridge works, but Green needs consumable/reorder refresh |
| 043150 | hard counterexample | +1.49 / -13.10 | +1.49 / -24.71 | +1.49 / -38.64 | dental imaging label without bridge fails |
| 228670 | severe hard counterexample | +3.88 / -23.21 | +3.88 / -39.07 | +3.88 / -70.15 | digital dental vocabulary without recurring cash bridge fails |

---

## 6. Raw component score breakdown

```jsonl
{"row_type":"score_simulation","symbol":"335890","raw_device_export_bridge":4,"raw_installed_base":4,"raw_reimbursement_or_market_access":2,"raw_consumable_reorder_service":4,"raw_margin_revision_bridge":3,"raw_validation":3,"raw_label_only_risk":1,"stage2_actionable_bonus_before":2.0,"stage2_actionable_bonus_after":2.0,"simulated_route":"Stage2-Actionable-local-4B-watch"}
{"row_type":"score_simulation","symbol":"043150","raw_device_export_bridge":1,"raw_installed_base":1,"raw_reimbursement_or_market_access":0,"raw_consumable_reorder_service":1,"raw_margin_revision_bridge":1,"raw_validation":0,"raw_label_only_risk":4,"stage2_actionable_bonus_before":2.0,"stage2_actionable_bonus_after":0.0,"simulated_route":"Stage2-FalsePositive-dental-imaging-label"}
{"row_type":"score_simulation","symbol":"228670","raw_device_export_bridge":0,"raw_installed_base":0,"raw_reimbursement_or_market_access":0,"raw_consumable_reorder_service":0,"raw_margin_revision_bridge":0,"raw_validation":0,"raw_label_only_risk":5,"stage2_actionable_bonus_before":2.0,"stage2_actionable_bonus_after":0.0,"simulated_route":"Stage2-FalsePositive-severe-digital-dental-label"}
```

---

## 7. Current calibrated profile stress test

### Existing error risk

C25 can over-credit:

```text
medical device export
dental imaging
digital dental
aesthetic device vocabulary
```

The correct bridge is narrower:

```text
device -> installed base -> reorder / consumable / service / reimbursement -> margin / revision / cash
```

The device itself is hardware. The investable mechanism is whether the installed hardware keeps printing cash.

### Rule candidate

```text
C25_INSTALLED_BASE_REORDER_CONSUMABLE_MARGIN_REQUIREMENT_V100

if C25
and medical_device_export_or_dental_label == true
and installed_base_reimbursement_consumable_reorder_service_or_margin_bridge == false:
    stage2_actionable_bonus = 0
    max_stage = Stage2-Watch
```

```text
if C25
and installed_base_or_consumable_bridge == true
and MFE_30D_pct >= +30
and MAE_180D_pct <= -20:
    local_4B_watch = true
    block_stage3_green = true
    require_reorder_margin_revision_refresh = true
```

```text
if C25
and dental_or_digital_device_label == true
and MFE_90D_pct < +10
and MAE_90D_pct <= -20:
    route = Stage2_FalsePositive_Block
```

```text
if C25
and severe_MAE_180D_pct <= -50
and recurring_cash_bridge == false:
    hard_4C_or_reopen_requires_new_evidence_family = true
```

---

## 8. Residual contribution summary

```yaml
do_not_propose_new_weight_delta: false
sector_specific_rule_candidate: false
canonical_archetype_rule_candidate: true
loop_contribution_label: canonical_archetype_rule_formalization_from_existing_controls
new_axis_proposed: C25_INSTALLED_BASE_REORDER_CONSUMABLE_MARGIN_REQUIREMENT_V100
existing_axis_strengthened:
  - C25_device_label_not_enough_without_installed_base_cash_bridge
  - C25_installed_base_consumable_export_margin_bridge_local_4B
  - C25_dental_device_export_label_stage2_block_without_reimbursement_or_revision
  - C25_digital_dental_severe_MAE_hard_block
existing_axis_weakened: null
```

---

## 9. Deferred Coding Agent Handoff Prompt

```text
Do not patch production scoring from this MD alone. Batch this C25 loop with C25 loop 99 and adjacent R13 bio/device accounting-trust, Stage2 false-positive and high-MAE guardrail files. Extract `C25_INSTALLED_BASE_REORDER_CONSUMABLE_MARGIN_REQUIREMENT_V100` as a shadow-rule candidate. Ingest exact trigger rows only if dedupe does not already contain them; otherwise use this file as sector-rule formalization evidence. Preserve installed-base/consumable positive controls, but block dental/digital device labels without reimbursement, recurring cash, service, consumable, margin, or revision bridge.
```

---

## 10. Next research state

```yaml
completed_round: R7
completed_loop: 100
selection_basis: docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket: Priority 0
round_schedule_status: coverage_index_selected
round_sector_consistency: pass
next_recommended_archetypes:
  - C24_BIO_TRIAL_DATA_EVENT_RISK
  - C05_EPC_MEGA_CONTRACT_MARGIN_GAP
  - R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL
  - C31_POLICY_SUBSIDY_LEGISLATION_EVENT_retest_with_battery_and_grid_policy_controls
  - C18_CONSUMER_EXPORT_CHANNEL_REORDER
```
