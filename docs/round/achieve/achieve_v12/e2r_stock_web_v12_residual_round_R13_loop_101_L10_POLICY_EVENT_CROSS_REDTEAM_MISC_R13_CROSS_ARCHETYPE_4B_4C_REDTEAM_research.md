# E2R v12 R13 cross-archetype residual calibration research

## 0. Execution metadata

```yaml
schema_family: v12_sector_archetype_residual
selected_round: R13
selected_loop: 101
large_sector_id: L10_POLICY_EVENT_CROSS_REDTEAM_MISC
canonical_archetype_id: R13_CROSS_ARCHETYPE_4B_4C_REDTEAM
fine_archetype_id: BIO_DEVICE_AND_EPC_LOCAL_4B_VS_HARD_4C_ROUTE_SPLIT
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

R13 is a cross-archetype checkpoint, not a sector-specific discovery round. This loop uses the latest current-session C23/C25/C05 rows and asks:

```text
When does a drawdown route become local 4B, and when must it become hard 4C / Stage2 false-positive block?
```

The previous local `R13_CROSS_ARCHETYPE_4B_4C_REDTEAM` run reached loop 100. This continuation is `loop 101`.

---

## 1. Research thesis

4B is not a polite name for failure. It is a temporary inspection bay.

```text
real bridge + MFE + incomplete confirmation
→ local 4B watch
→ reopen only when revenue/margin/cash bridge refreshes
```

4C is different.

```text
label-only + low MFE or severe MAE + no bridge
→ hard block
→ reopen only with a new evidence family
```

This loop compares three bridge families:

1. **Bio approval/commercialization**
   - Commercialized revenue bridge can stay Stage2.
   - Approval-to-launch can stay local 4B.
   - Approval label without listed-company economics is hard 4C.

2. **Medical device installed base**
   - Installed-base/consumable bridge can stay local 4B after drawdown.
   - Dental/digital device vocabulary without recurring cash bridge is hard 4C.

3. **EPC / construction project**
   - Delayed rebound may stay local 4B.
   - Builder/project/support label without margin/cash bridge is hard 4C.

---

## 2. Validation scope

```yaml
validation_scope:
  required_cases: 7
  actual_cases: 7
  source_archetypes:
    - C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION
    - C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT
    - C05_EPC_MEGA_CONTRACT_MARGIN_GAP
  price_windows:
    - 30D MFE/MAE
    - 90D MFE/MAE
    - 180D MFE/MAE
  output_use:
    - local 4B vs hard 4C route split
    - Stage3-Green block condition
    - Stage2 false-positive escalation logic
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
  - R7/C23 loop 138
  - R7/C25 loop 100
  - R1/C05 loop 114
  - R13 bio/device accounting-trust, Stage2 false-positive, high-MAE guardrail files
reason:
  - rows were already calculated from Songdaiki/stock-web tradable raw 1D OHLC
  - this file changes the canonical scope to R13 4B/4C red-team
  - no production scoring changed
```

---

## 4. Trigger rows

```jsonl
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","round":"R13","loop":101,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_4B_4C_REDTEAM","fine_archetype_id":"COMMERCIALIZED_DRUG_LOW_MAE_KEEP_STAGE2_BLOCK_HARD_4C","source_archetype_id":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION","symbol":"326030","name":"SK바이오팜","trigger_type":"Stage2-Actionable","entry_date":"2024-08-12","entry_close":98800,"price_basis":"tradable_raw","mfe_30d_pct":20.95,"mae_30d_pct":-5.87,"mfe_90d_pct":31.58,"mae_90d_pct":-5.87,"mfe_180d_pct":31.58,"mae_180d_pct":-5.87,"forward_high_30d":119500,"forward_low_30d":93000,"forward_high_90d":130000,"forward_low_90d":93000,"forward_high_180d":130000,"forward_low_180d":93000,"calibration_usable":true,"case_role":"positive_control_block_4C","novelty_key":"R13_CROSS_ARCHETYPE_4B_4C_REDTEAM|326030|Stage2-Actionable|2024-08-12","route":"KeepStage2_BlockHard4C","guardrail_lesson":"commercialized drug revenue/profit bridge with low MAE should not be downgraded to 4C"}
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","round":"R13","loop":101,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_4B_4C_REDTEAM","fine_archetype_id":"FDA_APPROVAL_LAUNCH_BRIDGE_LOCAL_4B_NOT_GREEN","source_archetype_id":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION","symbol":"006280","name":"녹십자","trigger_type":"Stage2-Actionable","entry_date":"2024-07-09","entry_close":124900,"price_basis":"tradable_raw","mfe_30d_pct":33.71,"mae_30d_pct":-4.56,"mfe_90d_pct":45.56,"mae_90d_pct":-4.56,"mfe_180d_pct":45.56,"mae_180d_pct":-10.49,"forward_high_30d":167000,"forward_low_30d":119200,"forward_high_90d":181800,"forward_low_90d":119200,"forward_high_180d":181800,"forward_low_180d":111800,"calibration_usable":true,"case_role":"local_4B_watch","novelty_key":"R13_CROSS_ARCHETYPE_4B_4C_REDTEAM|006280|Stage2-Actionable|2024-07-09","route":"Local4B_UntilLaunchRevenue","guardrail_lesson":"approval-to-launch bridge should stay local 4B until launch revenue cadence appears"}
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","round":"R13","loop":101,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_4B_4C_REDTEAM","fine_archetype_id":"APPROVAL_LABEL_WITHOUT_ECONOMICS_HARD_4C","source_archetype_id":"C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION","symbol":"170900","name":"동아에스티","trigger_type":"Stage2-FalsePositive","entry_date":"2024-10-11","entry_close":76400,"price_basis":"tradable_raw","mfe_30d_pct":5.63,"mae_30d_pct":-20.16,"mfe_90d_pct":5.63,"mae_90d_pct":-36.32,"mfe_180d_pct":5.63,"mae_180d_pct":-46.47,"forward_high_30d":80700,"forward_low_30d":61000,"forward_high_90d":80700,"forward_low_90d":48650,"forward_high_180d":80700,"forward_low_180d":40900,"calibration_usable":true,"case_role":"hard_4C_counterexample","novelty_key":"R13_CROSS_ARCHETYPE_4B_4C_REDTEAM|170900|Stage2-FalsePositive|2024-10-11","route":"Hard4C_Stage2FalsePositiveBlock","guardrail_lesson":"approval label with no listed-company economics and deep MAE should become hard 4C"}
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","round":"R13","loop":101,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_4B_4C_REDTEAM","fine_archetype_id":"DEVICE_INSTALLED_BASE_HIGH_MFE_LOCAL_4B","source_archetype_id":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT","symbol":"335890","name":"비올","trigger_type":"Stage2-Actionable","entry_date":"2024-03-13","entry_close":8480,"price_basis":"tradable_raw","mfe_30d_pct":41.86,"mae_30d_pct":-13.92,"mfe_90d_pct":41.86,"mae_90d_pct":-13.92,"mfe_180d_pct":41.86,"mae_180d_pct":-21.82,"forward_high_30d":12030,"forward_low_30d":7300,"forward_high_90d":12030,"forward_low_90d":7300,"forward_high_180d":12030,"forward_low_180d":6630,"calibration_usable":true,"case_role":"local_4B_watch","novelty_key":"R13_CROSS_ARCHETYPE_4B_4C_REDTEAM|335890|Stage2-Actionable|2024-03-13","route":"Local4B_RequireConsumableMarginRefresh","guardrail_lesson":"installed-base bridge survives Stage2 but drawdown blocks Green until consumable/reorder refresh"}
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","round":"R13","loop":101,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_4B_4C_REDTEAM","fine_archetype_id":"DIGITAL_DENTAL_LABEL_SEVERE_MAE_HARD_4C","source_archetype_id":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT","symbol":"228670","name":"레이","trigger_type":"Stage2-FalsePositive","entry_date":"2024-03-13","entry_close":17020,"price_basis":"tradable_raw","mfe_30d_pct":3.88,"mae_30d_pct":-23.21,"mfe_90d_pct":3.88,"mae_90d_pct":-39.07,"mfe_180d_pct":3.88,"mae_180d_pct":-70.15,"forward_high_30d":17680,"forward_low_30d":13070,"forward_high_90d":17680,"forward_low_90d":10370,"forward_high_180d":17680,"forward_low_180d":5080,"calibration_usable":true,"case_role":"severe_hard_4C_counterexample","novelty_key":"R13_CROSS_ARCHETYPE_4B_4C_REDTEAM|228670|Stage2-FalsePositive|2024-03-13","route":"Hard4C_ReopenRequiresNewEvidenceFamily","guardrail_lesson":"device label with severe MAE and no recurring cash bridge should be hard 4C"}
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","round":"R13","loop":101,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_4B_4C_REDTEAM","fine_archetype_id":"EPC_DELAYED_REBOUND_LOCAL_4B_NOT_IMMEDIATE_STAGE2","source_archetype_id":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP","symbol":"294870","name":"HDC현대산업개발","trigger_type":"Stage2-Watch","entry_date":"2024-05-13","entry_close":17920,"price_basis":"tradable_raw","mfe_30d_pct":2.12,"mae_30d_pct":-6.58,"mfe_90d_pct":37.28,"mae_90d_pct":-6.58,"mfe_180d_pct":57.37,"mae_180d_pct":-6.58,"forward_high_30d":18300,"forward_low_30d":16740,"forward_high_90d":24600,"forward_low_90d":16740,"forward_high_180d":28200,"forward_low_180d":16740,"calibration_usable":true,"case_role":"delayed_local_4B","novelty_key":"R13_CROSS_ARCHETYPE_4B_4C_REDTEAM|294870|Stage2-Watch|2024-05-13","route":"DelayedLocal4B_DoNotBackfillImmediateStage2","guardrail_lesson":"delayed rebound should not be backfilled as immediate Stage2 without margin/cash bridge"}
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","round":"R13","loop":101,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_4B_4C_REDTEAM","fine_archetype_id":"BUILDER_LABEL_LOW_MFE_DEEP_MAE_HARD_4C","source_archetype_id":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP","symbol":"000720","name":"현대건설","trigger_type":"Stage2-FalsePositive","entry_date":"2024-03-27","entry_close":33250,"price_basis":"tradable_raw","mfe_30d_pct":4.81,"mae_30d_pct":-6.17,"mfe_90d_pct":8.27,"mae_90d_pct":-6.17,"mfe_180d_pct":8.27,"mae_180d_pct":-27.52,"forward_high_30d":34850,"forward_low_30d":31200,"forward_high_90d":36000,"forward_low_90d":31200,"forward_high_180d":36000,"forward_low_180d":24100,"calibration_usable":true,"case_role":"hard_4C_counterexample","novelty_key":"R13_CROSS_ARCHETYPE_4B_4C_REDTEAM|000720|Stage2-FalsePositive|2024-03-27","route":"Hard4C_Stage2FalsePositiveBlock","guardrail_lesson":"builder/project label without margin/cash bridge and deep 180D MAE should be hard 4C"}
```

---

## 5. Case analysis

### 5.1 SK Biopharm / 326030 — keep Stage2, block hard 4C

Commercialized drug revenue/profit bridge is visible and drawdown is shallow.

```text
route = KeepStage2_BlockHard4C
```

### 5.2 Green Cross / 006280 — local 4B, not Green

Approval-to-launch is valid, but launch revenue cadence is not yet the same as durable commercial economics.

```text
route = Local4B_UntilLaunchRevenue
```

### 5.3 Dong-A ST / 170900 — hard 4C

Approval label without listed-company economics and deep MAE should escalate to hard 4C.

```text
route = Hard4C_Stage2FalsePositiveBlock
```

### 5.4 VIOL / 335890 — device bridge local 4B

The installed-base bridge is real enough to preserve Stage2, but not enough for Green after 180D drawdown.

```text
route = Local4B_RequireConsumableMarginRefresh
```

### 5.5 Ray / 228670 — severe hard 4C

Digital dental label without recurring cash bridge produced severe drawdown. Reopen requires a new evidence family.

```text
route = Hard4C_ReopenRequiresNewEvidenceFamily
```

### 5.6 HDC Hyundai Development / 294870 — delayed 4B, no backfill

The later rebound is real, but it should not be backfilled as immediate Stage2 without margin/cash evidence.

```text
route = DelayedLocal4B_DoNotBackfillImmediateStage2
```

### 5.7 Hyundai E&C / 000720 — builder label hard 4C

Low MFE and deep 180D MAE make this a hard block.

```text
route = Hard4C_Stage2FalsePositiveBlock
```

---

## 6. Score-return alignment

```yaml
new_independent_case_count: 7
calibration_usable_case_count: 7
calibration_usable_trigger_count: 7
positive_control_count: 1
local_4B_watch_count: 3
hard_4C_or_stage2_block_count: 3
current_profile_error_count: 5
```

| symbol | source | route | 90D MFE/MAE | 180D MFE/MAE | lesson |
|---|---:|---:|---:|---:|---|
| 326030 | C23 | keep Stage2 | +31.58 / -5.87 | +31.58 / -5.87 | real commercial bridge |
| 006280 | C23 | local 4B | +45.56 / -4.56 | +45.56 / -10.49 | approval-to-launch needs revenue cadence |
| 170900 | C23 | hard 4C | +5.63 / -36.32 | +5.63 / -46.47 | approval label fails |
| 335890 | C25 | local 4B | +41.86 / -13.92 | +41.86 / -21.82 | device bridge needs consumable refresh |
| 228670 | C25 | hard 4C | +3.88 / -39.07 | +3.88 / -70.15 | severe device-label false positive |
| 294870 | C05 | delayed 4B | +37.28 / -6.58 | +57.37 / -6.58 | do not backfill delayed rebound |
| 000720 | C05 | hard 4C | +8.27 / -6.17 | +8.27 / -27.52 | builder label lacks margin/cash bridge |

---

## 7. Raw component score breakdown

```jsonl
{"row_type":"score_simulation","symbol":"326030","raw_bridge_quality":5,"raw_accounting_trust":5,"raw_mfe_validation":4,"raw_mae_penalty":0,"raw_label_only_risk":0,"stage2_actionable_bonus_before":2.0,"stage2_actionable_bonus_after":2.0,"simulated_route":"KeepStage2_BlockHard4C"}
{"row_type":"score_simulation","symbol":"006280","raw_bridge_quality":4,"raw_accounting_trust":3,"raw_mfe_validation":4,"raw_mae_penalty":1,"raw_label_only_risk":1,"stage2_actionable_bonus_before":2.0,"stage2_actionable_bonus_after":2.0,"simulated_route":"Local4B_UntilLaunchRevenue"}
{"row_type":"score_simulation","symbol":"170900","raw_bridge_quality":1,"raw_accounting_trust":0,"raw_mfe_validation":0,"raw_mae_penalty":5,"raw_label_only_risk":4,"stage2_actionable_bonus_before":2.0,"stage2_actionable_bonus_after":0.0,"simulated_route":"Hard4C_Stage2FalsePositiveBlock"}
{"row_type":"score_simulation","symbol":"335890","raw_bridge_quality":4,"raw_accounting_trust":3,"raw_mfe_validation":4,"raw_mae_penalty":3,"raw_label_only_risk":1,"stage2_actionable_bonus_before":2.0,"stage2_actionable_bonus_after":2.0,"simulated_route":"Local4B_ConsumableRefresh"}
{"row_type":"score_simulation","symbol":"228670","raw_bridge_quality":0,"raw_accounting_trust":0,"raw_mfe_validation":0,"raw_mae_penalty":5,"raw_label_only_risk":5,"stage2_actionable_bonus_before":2.0,"stage2_actionable_bonus_after":0.0,"simulated_route":"Hard4C_ReopenRequiresNewEvidence"}
{"row_type":"score_simulation","symbol":"294870","raw_bridge_quality":2,"raw_accounting_trust":1,"raw_mfe_validation":3,"raw_mae_penalty":1,"raw_label_only_risk":2,"stage2_actionable_bonus_before":2.0,"stage2_actionable_bonus_after":1.0,"simulated_route":"DelayedLocal4B"}
{"row_type":"score_simulation","symbol":"000720","raw_bridge_quality":0,"raw_accounting_trust":0,"raw_mfe_validation":0,"raw_mae_penalty":4,"raw_label_only_risk":4,"stage2_actionable_bonus_before":2.0,"stage2_actionable_bonus_after":0.0,"simulated_route":"Hard4C_Stage2FalsePositiveBlock"}
```

---

## 8. Current calibrated profile stress test

### Existing error risk

The profile can still misroute the same price shapes:

```text
high MFE + incomplete bridge
```

This should be local 4B, not Green.

```text
label-only + low MFE + deep MAE
```

This should be hard 4C, not repeated Stage2-Watch.

```text
delayed rebound after weak entry
```

This should be delayed 4B, not backfilled as immediate Stage2.

### Rule candidate

```text
R13_4B_4C_ROUTE_SPLIT_V101

if company_specific_commercial_or_cash_bridge == true
and MFE_90D_pct >= +20
and MAE_90D_pct > -10:
    keep_stage2_actionable_bonus = true
    block_hard_4C = true
```

```text
if company_specific_bridge == true
and MFE_30D_pct >= +30
and MAE_180D_pct <= -10
and refreshed_revenue_margin_cash_bridge == false:
    route = local_4B_watch
    block_stage3_green = true
```

```text
if label_only_or_bridge_missing == true
and MFE_90D_pct < +10
and MAE_90D_pct <= -20:
    route = hard_4C_or_Stage2_FalsePositive_Block
    stage2_actionable_bonus = 0
```

```text
if severe_MAE_180D_pct <= -50
and recurring_cash_bridge == false:
    route = hard_4C
    require_new_evidence_family_before_reopen = true
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
loop_contribution_label: cross_archetype_4B_4C_redteam_guardrail_candidate
new_axis_proposed: R13_4B_4C_ROUTE_SPLIT_V101
existing_axis_strengthened:
  - commercial_bridge_low_MAE_keep_stage2
  - bridge_incomplete_high_MFE_local_4B
  - label_only_low_MFE_high_MAE_hard_4C
  - severe_MAE_without_cash_bridge_reopen_requires_new_evidence
  - delayed_rebound_do_not_backfill_immediate_stage2
existing_axis_weakened: null
```

---

## 10. Deferred Coding Agent Handoff Prompt

```text
Do not patch production scoring from this single MD. Batch this R13 4B/4C loop with C23 loop 138, C25 loop 100, C05 loop 114, and adjacent R13 accounting-trust/high-MAE/Stage2 false-positive files. Extract `R13_4B_4C_ROUTE_SPLIT_V101` as a cross-archetype shadow rule. Preserve low-MAE commercial bridge escape hatches, keep incomplete-but-real bridge cases in local 4B, and hard-block label-only cases with low MFE and deep MAE.
```

---

## 11. Next research state

```yaml
completed_round: R13
completed_loop: 101
selection_basis: docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket: Priority 0
round_schedule_status: coverage_index_selected
round_sector_consistency: pass
next_recommended_archetypes:
  - C24_BIO_TRIAL_DATA_EVENT_RISK
  - C31_POLICY_SUBSIDY_LEGISLATION_EVENT_retest_with_battery_and_grid_policy_controls
  - C18_CONSUMER_EXPORT_CHANNEL_REORDER
  - C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE
  - C28_SOFTWARE_SECURITY_CONTRACT_RETENTION
```
