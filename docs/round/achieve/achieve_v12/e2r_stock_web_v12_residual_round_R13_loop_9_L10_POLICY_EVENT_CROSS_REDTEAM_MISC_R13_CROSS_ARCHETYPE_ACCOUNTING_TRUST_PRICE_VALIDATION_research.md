# E2R v12 R13 cross-archetype residual calibration research

## 0. Execution metadata

```yaml
schema_family: v12_sector_archetype_residual
selected_round: R13
selected_loop: 9
large_sector_id: L10_POLICY_EVENT_CROSS_REDTEAM_MISC
canonical_archetype_id: R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION
fine_archetype_id: BIO_APPROVAL_DEVICE_EXPORT_TO_COMMERCIAL_CASH_BRIDGE_VS_LABEL_ONLY_HIGH_MAE
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

R13 is a cross-archetype checkpoint, not a new sector-specific discovery round. This loop uses the most recent `C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION` and `C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT` rows from the current v12 session and asks whether the headline can be traced into listed-company commercial economics.

The previous local `R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION` run reached loop 8, so this continuation is `loop 9`.

---

## 1. Research thesis

For bio and medical-device names, accounting trust is not the same as approval or product vocabulary.

```text
regulatory approval / device export / installed base
→ prescriptions, launch revenue, reimbursement, reorder, consumables, royalty, margin, or profit
→ price path validation
```

The core split:

1. **Commercialized drug with visible sales/profit bridge**  
   Stage2 should survive when approval has already turned into repeat prescriptions or revenue.

2. **FDA approval to launch bridge**  
   Stage2 may open, but vertical MFE before quarterly launch revenue requires local 4B.

3. **Approval label without listed-company economics**  
   Stage2 must be capped or blocked if partner economics, royalty timing, market access, or launch cadence are not visible.

4. **Device export / installed-base bridge**  
   Stage2 may open if reorder, consumable, installed base, and margin bridge are plausible.

5. **Device/dental vocabulary without reimbursement or consumable bridge**  
   High MAE and low MFE should route to false-positive block.

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
  - e2r_stock_web_v12_residual_round_R7_loop_137_L7_BIO_HEALTHCARE_MEDICAL_C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION_research.md
  - e2r_stock_web_v12_residual_round_R7_loop_99_L7_BIO_HEALTHCARE_MEDICAL_C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT_research.md
reason:
  - direct uncached stock-web shard fetch was intermittently unavailable during recent turns
  - these rows were already computed from Songdaiki/stock-web tradable 1D OHLC
  - R13 canonical differs from source C23/C25, so this is a cross-archetype guardrail row, not a duplicate sector case
  - no production scoring changed
```

Symbol caveats:

```yaml
326030:
  name: SK바이오팜
  source_archetype: C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION
  role: approved commercialized drug revenue/profit bridge

006280:
  name: 녹십자
  source_archetype: C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION
  role: FDA approval to US launch bridge with 4B watch

170900:
  name: 동아에스티
  source_archetype: C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION
  role: biosimilar approval label without visible direct economics

335890:
  name: 비올
  source_archetype: C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT
  role: aesthetic device export / installed base / consumable margin bridge

043150:
  name: 바텍
  source_archetype: C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT
  role: dental imaging export label weak bridge

228670:
  name: 레이
  source_archetype: C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT
  role: digital dental label high-MAE false positive
```

---

## 3. Trigger rows

```jsonl
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","round":"R13","loop":9,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION","fine_archetype_id":"APPROVED_DRUG_COMMERCIAL_REVENUE_PROFIT_BRIDGE_VALIDATED","source_archetype_id":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION","symbol":"326030","name":"SK바이오팜","trigger_type":"Stage2-Actionable","entry_date":"2024-08-12","entry_close":98800,"price_basis":"tradable_raw","mfe_30d_pct":20.95,"mae_30d_pct":-5.87,"mfe_90d_pct":31.58,"mae_90d_pct":-5.87,"mfe_180d_pct":31.58,"mae_180d_pct":-5.87,"forward_high_30d":119500,"forward_low_30d":93000,"forward_high_90d":130000,"forward_low_90d":93000,"forward_high_180d":130000,"forward_low_180d":93000,"calibration_usable":true,"case_role":"accounting_trust_validated","novelty_key":"R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION|326030|Stage2-Actionable|2024-08-12","accounting_bridge":"approved-drug commercialization with visible US sales/profit bridge","route":"KeepStage2_CommercializationBridge"}
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","round":"R13","loop":9,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION","fine_archetype_id":"FDA_APPROVAL_TO_US_LAUNCH_BRIDGE_WITH_4B_WATCH","source_archetype_id":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION","symbol":"006280","name":"녹십자","trigger_type":"Stage2-Actionable","entry_date":"2024-07-09","entry_close":124900,"price_basis":"tradable_raw","mfe_30d_pct":33.71,"mae_30d_pct":-4.56,"mfe_90d_pct":45.56,"mae_90d_pct":-4.56,"mfe_180d_pct":45.56,"mae_180d_pct":-10.49,"forward_high_30d":167000,"forward_low_30d":119200,"forward_high_90d":181800,"forward_low_90d":119200,"forward_high_180d":181800,"forward_low_180d":111800,"calibration_usable":true,"case_role":"accounting_trust_validated_with_4B_watch","novelty_key":"R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION|006280|Stage2-Actionable|2024-07-09","accounting_bridge":"FDA approval and US launch path, but revenue cadence still needs confirmation","route":"KeepStage2_Local4BUntilLaunchRevenue"}
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","round":"R13","loop":9,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION","fine_archetype_id":"BIOSIMILAR_APPROVAL_WITH_PARTNER_ECONOMICS_DELAY_BLOCK","source_archetype_id":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION","symbol":"170900","name":"동아에스티","trigger_type":"Stage2-FalsePositive","entry_date":"2024-10-11","entry_close":76400,"price_basis":"tradable_raw","mfe_30d_pct":5.63,"mae_30d_pct":-20.16,"mfe_90d_pct":5.63,"mae_90d_pct":-36.32,"mfe_180d_pct":5.63,"mae_180d_pct":-46.47,"forward_high_30d":80700,"forward_low_30d":61000,"forward_high_90d":80700,"forward_low_90d":48650,"forward_high_180d":80700,"forward_low_180d":40900,"calibration_usable":true,"case_role":"accounting_trust_not_validated","novelty_key":"R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION|170900|Stage2-FalsePositive|2024-10-11","accounting_bridge":"biosimilar approval label without visible listed-company launch, royalty, or margin bridge","route":"Stage2FalsePositiveBlock"}
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","round":"R13","loop":9,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION","fine_archetype_id":"AESTHETIC_DEVICE_EXPORT_INSTALLED_BASE_BRIDGE_WITH_4B_WATCH","source_archetype_id":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT","symbol":"335890","name":"비올","trigger_type":"Stage2-Actionable","entry_date":"2024-03-13","entry_close":8480,"price_basis":"tradable_raw","mfe_30d_pct":41.86,"mae_30d_pct":-13.92,"mfe_90d_pct":41.86,"mae_90d_pct":-13.92,"mfe_180d_pct":41.86,"mae_180d_pct":-21.82,"forward_high_30d":12030,"forward_low_30d":7300,"forward_high_90d":12030,"forward_low_90d":7300,"forward_high_180d":12030,"forward_low_180d":6630,"calibration_usable":true,"case_role":"accounting_trust_partial_with_4B","novelty_key":"R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION|335890|Stage2-Actionable|2024-03-13","accounting_bridge":"aesthetic device export, installed base, consumable/reorder and margin bridge, but 180D drawdown requires refresh","route":"KeepStage2_Local4BConsumableMarginRefresh"}
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","round":"R13","loop":9,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION","fine_archetype_id":"DENTAL_IMAGING_EXPORT_LABEL_WITHOUT_REIMBURSEMENT_CONSUMABLE_BRIDGE","source_archetype_id":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT","symbol":"043150","name":"바텍","trigger_type":"Stage2-FalsePositive","entry_date":"2024-05-17","entry_close":30150,"price_basis":"tradable_raw","mfe_30d_pct":1.49,"mae_30d_pct":-13.10,"mfe_90d_pct":1.49,"mae_90d_pct":-24.71,"mfe_180d_pct":1.49,"mae_180d_pct":-38.64,"forward_high_30d":30600,"forward_low_30d":26200,"forward_high_90d":30600,"forward_low_90d":22700,"forward_high_180d":30600,"forward_low_180d":18500,"calibration_usable":true,"case_role":"accounting_trust_not_validated","novelty_key":"R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION|043150|Stage2-FalsePositive|2024-05-17","accounting_bridge":"dental imaging export label without fresh reimbursement, consumable, or revision bridge","route":"Stage2FalsePositiveBlock"}
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","round":"R13","loop":9,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION","fine_archetype_id":"DIGITAL_DENTAL_LABEL_HIGH_MAE_NO_CASH_BRIDGE_BLOCK","source_archetype_id":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT","symbol":"228670","name":"레이","trigger_type":"Stage2-FalsePositive","entry_date":"2024-03-13","entry_close":17020,"price_basis":"tradable_raw","mfe_30d_pct":3.88,"mae_30d_pct":-23.21,"mfe_90d_pct":3.88,"mae_90d_pct":-39.07,"mfe_180d_pct":3.88,"mae_180d_pct":-70.15,"forward_high_30d":17680,"forward_low_30d":13070,"forward_high_90d":17680,"forward_low_90d":10370,"forward_high_180d":17680,"forward_low_180d":5080,"calibration_usable":true,"case_role":"hard_counterexample","novelty_key":"R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION|228670|Stage2-FalsePositive|2024-03-13","accounting_bridge":"digital dental label without reimbursement, installed-base, or recurring cash bridge","route":"Stage2FalsePositiveBlock"}
```

---

## 4. Case analysis

### 4.1 SK Biopharm / 326030 — approved drug with commercial bridge

This is the clean C23 accounting-trust positive. Approval is not the thesis by itself; visible commercial revenue and profitability are the bridge.

```text
route = KeepStage2_CommercializationBridge
```

### 4.2 Green Cross / 006280 — FDA approval to launch, but 4B after vertical MFE

This is the approval-to-launch positive case. Stage2 survives, but the score must ask for launch revenue cadence before Green.

```text
route = KeepStage2_Local4BUntilLaunchRevenue
```

### 4.3 Dong-A ST / 170900 — approval label without listed-company economics

This is the C23 false positive. A biosimilar approval can be real and still fail if partner economics, launch timing, royalty capture, and reimbursement are not visible.

```text
route = Stage2FalsePositiveBlock
```

### 4.4 VIOL / 335890 — device export and installed-base bridge, but 4B

This is the C25 positive with 4B watch. The installed-base / consumable / export bridge produced MFE, but 180D MAE says the bridge needs margin and reorder refresh.

```text
route = KeepStage2_Local4BConsumableMarginRefresh
```

### 4.5 Vatech / 043150 — dental imaging label without bridge

This is a C25 false positive. Dental imaging/export vocabulary did not become reimbursement, consumable, or revision evidence.

```text
route = Stage2FalsePositiveBlock
```

### 4.6 Ray / 228670 — digital dental label hard counterexample

This is the severe C25 counterexample. The label was present, but the cash bridge was not.

```text
route = Stage2FalsePositiveBlock
```

---

## 5. Score-return alignment

```yaml
new_independent_case_count: 6
calibration_usable_case_count: 6
calibration_usable_trigger_count: 6
accounting_trust_validated_count: 2
partial_trust_local_4B_count: 2
stage2_false_positive_count: 3
current_profile_error_count: 4
```

| symbol | source | route | 90D MFE/MAE | 180D MFE/MAE | accounting lesson |
|---|---:|---:|---:|---:|---|
| 326030 | C23 | KeepStage2 | +31.58 / -5.87 | +31.58 / -5.87 | approval plus commercial revenue bridge validates |
| 006280 | C23 | Stage2 + 4B | +45.56 / -4.56 | +45.56 / -10.49 | approval-to-launch works, Green waits for revenue cadence |
| 170900 | C23 | hard block | +5.63 / -36.32 | +5.63 / -46.47 | approval label without listed-company economics fails |
| 335890 | C25 | Stage2 + 4B | +41.86 / -13.92 | +41.86 / -21.82 | device export bridge works, but margin/reorder refresh needed |
| 043150 | C25 | hard block | +1.49 / -24.71 | +1.49 / -38.64 | dental export label lacks cash bridge |
| 228670 | C25 | hard block | +3.88 / -39.07 | +3.88 / -70.15 | digital dental label is not reimbursement/cash bridge |

---

## 6. Raw component score breakdown

```jsonl
{"row_type":"score_simulation","symbol":"326030","raw_regulatory_event":3,"raw_commercial_revenue_bridge":5,"raw_reimbursement_or_market_access":3,"raw_profit_margin_bridge":4,"raw_validation":4,"raw_label_only_risk":0,"stage2_actionable_bonus_before":2.0,"stage2_actionable_bonus_after":2.0,"simulated_route":"KeepStage2_CommercializationBridge"}
{"row_type":"score_simulation","symbol":"006280","raw_regulatory_event":5,"raw_commercial_revenue_bridge":3,"raw_reimbursement_or_market_access":3,"raw_profit_margin_bridge":2,"raw_validation":4,"raw_label_only_risk":1,"stage2_actionable_bonus_before":2.0,"stage2_actionable_bonus_after":2.0,"simulated_route":"Stage2Positive_Local4BUntilLaunchRevenue"}
{"row_type":"score_simulation","symbol":"170900","raw_regulatory_event":4,"raw_commercial_revenue_bridge":1,"raw_reimbursement_or_market_access":1,"raw_profit_margin_bridge":1,"raw_validation":0,"raw_label_only_risk":4,"stage2_actionable_bonus_before":2.0,"stage2_actionable_bonus_after":0.0,"simulated_route":"Stage2FalsePositiveBlock"}
{"row_type":"score_simulation","symbol":"335890","raw_regulatory_event":0,"raw_commercial_revenue_bridge":4,"raw_reimbursement_or_market_access":2,"raw_profit_margin_bridge":3,"raw_validation":3,"raw_label_only_risk":1,"stage2_actionable_bonus_before":2.0,"stage2_actionable_bonus_after":2.0,"simulated_route":"DeviceBridge_Local4B"}
{"row_type":"score_simulation","symbol":"043150","raw_regulatory_event":0,"raw_commercial_revenue_bridge":1,"raw_reimbursement_or_market_access":0,"raw_profit_margin_bridge":1,"raw_validation":0,"raw_label_only_risk":4,"stage2_actionable_bonus_before":2.0,"stage2_actionable_bonus_after":0.0,"simulated_route":"Stage2FalsePositiveBlock"}
{"row_type":"score_simulation","symbol":"228670","raw_regulatory_event":0,"raw_commercial_revenue_bridge":0,"raw_reimbursement_or_market_access":0,"raw_profit_margin_bridge":0,"raw_validation":0,"raw_label_only_risk":5,"stage2_actionable_bonus_before":2.0,"stage2_actionable_bonus_after":0.0,"simulated_route":"Stage2FalsePositiveBlock"}
```

---

## 7. Current calibrated profile stress test

### Existing error risk

The current profile can still confuse:

```text
approval label
device export vocabulary
commercial bridge
```

The right question is not whether a product exists. The right question is whether the product crosses into the accounts. Approval is the key; revenue is the door opening. A device installed base is the printer; consumables and service are the ink.

### Rule candidate

```text
R13_BIO_DEVICE_ACCOUNTING_TRUST_GATE_V9

if regulatory_approval_or_device_export_label == true
and listed_company_commercial_revenue_reimbursement_royalty_consumable_or_margin_bridge == false:
    accounting_trust_validated = false
    stage2_actionable_bonus = 0
    max_stage = Stage2-Watch
```

```text
if approved_drug_commercialization_bridge == true
and MFE_90D_pct >= +20
and MAE_90D_pct > -10:
    accounting_trust_validated = true
    keep_stage2_actionable_bonus = true
```

```text
if FDA_approval_to_launch_bridge == true
and MFE_30D_pct >= +30
and quarterly_launch_revenue_cadence == false:
    local_4B_watch = true
    block_stage3_green = true
```

```text
if medical_device_installed_base_or_export_bridge == true
and MFE_30D_pct >= +30
and MAE_180D_pct <= -20:
    local_4B_watch = true
    require_consumable_margin_reorder_refresh = true
```

```text
if device_or_dental_label == true
and MFE_90D_pct < +10
and MAE_90D_pct <= -20:
    route = Stage2FalsePositiveBlock
```

---

## 8. Residual contribution summary

```yaml
do_not_propose_new_weight_delta: false
sector_specific_rule_candidate: false
canonical_archetype_rule_candidate: false
cross_archetype_rule_candidate: true
loop_contribution_label: cross_archetype_bio_device_accounting_trust_candidate
new_axis_proposed: R13_BIO_DEVICE_ACCOUNTING_TRUST_GATE_V9
existing_axis_strengthened:
  - approval_label_without_commercial_bridge_stage2_block
  - approved_drug_commercialization_bridge_keep_stage2
  - FDA_approval_launch_bridge_local_4B_until_revenue_cadence
  - medical_device_installed_base_consumable_bridge_local_4B
  - dental_device_label_high_MAE_false_positive_block
existing_axis_weakened: null
```

---

## 9. Deferred Coding Agent Handoff Prompt

```text
Do not patch production scoring from this MD alone. Batch this R13 loop with C23 loop 137, C25 loop 99, and adjacent R13 accounting-trust / Stage2 false-positive files. Extract `R13_BIO_DEVICE_ACCOUNTING_TRUST_GATE_V9` as a cross-archetype shadow rule. Preserve approved-drug commercialization and device installed-base positive controls, but block approval/device labels that lack listed-company revenue, reimbursement, royalty, consumable, margin, or profit bridge.
```

---

## 10. Next research state

```yaml
completed_round: R13
completed_loop: 9
selection_basis: docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket: Priority 0
round_schedule_status: coverage_index_selected
round_sector_consistency: pass
next_recommended_archetypes:
  - C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION
  - C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT
  - C24_BIO_TRIAL_DATA_EVENT_RISK
  - C05_EPC_MEGA_CONTRACT_MARGIN_GAP
  - R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW
```
