# E2R v12 residual calibration research

## 0. Execution metadata

```yaml
schema_family: v12_sector_archetype_residual
selected_round: R11
selected_loop: 104
large_sector_id: L10_POLICY_EVENT_CROSS_REDTEAM_MISC
canonical_archetype_id: C31_POLICY_SUBSIDY_LEGISLATION_EVENT
fine_archetype_id: PF_HOUSING_POLICY_SUPPORT_TO_ISSUER_REFINANCING_CASH_BRIDGE_VS_SECTOR_RELIEF_LABEL
selection_basis:
  main_execution_prompt: docs/core/e2r_v12_prompt_round_scheduler_corrected.txt
  no_repeat_index: docs/core/V12_Research_No_Repeat_Index.md
web_raw_fetch_status_this_turn:
  main_execution_prompt: read_ok
  no_repeat_index: read_ok
  stock_web_manifest: read_ok
  uncached_symbol_shards: cache_miss_observed
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

`C31_POLICY_SUBSIDY_LEGISLATION_EVENT` remains Priority 0 in the latest no-repeat index: 3 representative rows, still 27 rows short of the 30-row minimum. The v12 scheduler maps C31 to `R11 / L10_POLICY_EVENT_CROSS_REDTEAM_MISC`.

This run continues the local C31 sequence after `R11/C31 loop 103`; selected loop is therefore `104`.

This is not a live construction or financial-stock screen. It is a historical calibration / residual rule file. Direct uncached `stock-web` symbol shards returned cache misses in this turn, so the trigger rows below reuse stock-web-derived C30 rows already calculated in the current v12 session and change the canonical lens to C31. The purpose is to test whether PF / housing policy support becomes a company-specific refinancing, guarantee-relief, presale, liquidity, debt-service or cash bridge. No production scoring is changed.

---

## 1. Research thesis

C31 is not `policy support exists`.

It is the policy-to-company-cash bridge:

```text
PF relief / housing support / construction liquidity policy / restructuring framework
→ issuer-specific refinancing, guarantee relief, maturity extension, presale recovery, cash conversion, debt-service capacity
→ price path validation
```

A sector policy headline is a raincloud. It only helps a specific builder if water reaches that builder’s reservoir. The model should not pay Stage2 bonus for the cloud alone.

This loop separates seven routes:

1. **Large-builder support label with low drawdown**
   - Policy support can keep a large builder stable.
   - But without issuer-specific refinancing/cash evidence it remains Watch, not Green.

2. **Delayed construction rebound**
   - Policy relief may eventually matter.
   - If 30D/90D MFE is weak and later MFE appears, do not backfill the original trigger.

3. **Weak-liquidity PF-relief false positive**
   - Low-PBR or PF support vocabulary without debt-service/cash bridge should hard block.

4. **Price-only rebound overlay**
   - A later local rebound can remain local 4B, but not full positive without non-price bridge.

5. **Developer delayed soft-landing**
   - Strong delayed MFE can be useful, but only as local 4B until a timestamped issuer bridge appears.

6. **Mid-builder support headline**
   - Shallow drawdown and delayed MFE are useful, but still require issuer-specific proof.

7. **Direct workout stress-control**
   - Workout/restructuring survival is not automatically equity recovery and should not be clean aggregate.

---

## 2. Validation scope

```yaml
validation_scope:
  required_cases: 6
  actual_trigger_rows: 7
  source_archetypes:
    - C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK
    - R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW
    - R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL
    - R13_CROSS_ARCHETYPE_4B_4C_REDTEAM
  price_windows:
    - 30D MFE/MAE
    - 90D MFE/MAE
    - 180D MFE/MAE
  output_use:
    - C31 policy-to-cashflow bridge rule
    - PF/housing policy support false-positive guard
    - delayed rebound no-backfill guard
    - stress-control exclusion for workout rows
```

---

## 3. Source validation

```yaml
stock_web_manifest:
  source_name: FinanceData/marcap
  price_adjustment_status: raw_unadjusted_marcap
  max_date: 2026-02-20
  calibration_shard_root: atlas/ohlcv_tradable_by_symbol_year
  caveat: Raw/unadjusted OHLC; corporate-action-contaminated windows blocked by default.
```

Local stock-web-derived row provenance:

```yaml
reused_price_rows_from_current_session:
  - R10/C30 loop 102
  - R10/C30 loop 3
  - R13 accounting-trust loop 10
  - R13 Stage2 false-positive loop 9
  - R13 high-MAE loop 7
  - R13 4B/4C loop 102
reason:
  - all rows were already calculated from Songdaiki/stock-web tradable raw 1D OHLC
  - current file changes canonical scope to C31 policy/subsidy/legislation event
  - exact source-archetype keys should be deduped separately from this C31 canonical key
  - no production scoring changed
```

Symbol caveats:

```yaml
000720:
  name: 현대건설
  source_archetype: C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK
  role: large-builder policy support survivor watch
  calibration_usable: true

047040:
  name: 대우건설
  source_archetype: C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK
  role: delayed rebound and price-only 4B overlay
  calibration_usable: true

002990:
  name: 금호건설
  source_archetype: C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK
  role: weak-liquidity PF relief label false positive
  calibration_usable: true

294870:
  name: HDC현대산업개발
  source_archetype: C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK
  role: delayed housing/PF soft-landing local 4B
  calibration_usable: true

014790:
  name: HL D&I
  source_archetype: C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK
  role: mid-builder delayed support headline local 4B
  calibration_usable: true

009410:
  name: 태영건설
  source_archetype: C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK
  role: direct workout stress-control only
  calibration_usable: false
  caveat: workout / corporate-action / trading-gap contamination; stress-control only
```

---

## 4. Trigger rows

```jsonl
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","round":"R11","loop":104,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","fine_archetype_id":"PF_POLICY_SUPPORT_LARGE_BUILDER_SURVIVOR_WATCH","source_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","symbol":"000720","name":"현대건설","trigger_type":"Stage2-Watch","entry_date":"2024-01-26","entry_close":33100,"price_basis":"tradable_raw","mfe_30d_pct":7.30,"mae_30d_pct":-3.50,"mfe_90d_pct":8.80,"mae_90d_pct":-5.70,"mfe_180d_pct":8.80,"mae_180d_pct":-12.20,"forward_high_30d":34850,"forward_low_30d":31950,"forward_high_90d":36000,"forward_low_90d":31200,"forward_high_180d":36000,"forward_low_180d":29050,"calibration_usable":true,"case_role":"large_builder_policy_survivor_watch","novelty_key":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT|000720|Stage2-Watch|2024-01-26","non_price_bridge":"PF/housing support policy stabilized large-builder risk, but issuer-specific refinancing and cash bridge remained insufficient for Green","score_alignment":"Stage2-Watch only; require debt-service, margin, receivable or cash conversion bridge before Actionable"}
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","round":"R11","loop":104,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","fine_archetype_id":"PF_POLICY_DELAYED_REBOUND_NO_BACKFILL","source_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","symbol":"047040","name":"대우건설","trigger_type":"Stage2-Watch","entry_date":"2024-01-26","entry_close":4015,"price_basis":"tradable_raw","mfe_30d_pct":2.60,"mae_30d_pct":-5.60,"mfe_90d_pct":2.60,"mae_90d_pct":-10.80,"mfe_180d_pct":23.70,"mae_180d_pct":-12.30,"forward_high_30d":4120,"forward_low_30d":3790,"forward_high_90d":4120,"forward_low_90d":3580,"forward_high_180d":4965,"forward_low_180d":3520,"calibration_usable":true,"case_role":"delayed_policy_rebound_local_4B","novelty_key":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT|047040|Stage2-Watch|2024-01-26","non_price_bridge":"PF policy relief plus construction rebound narrative, but validation arrived late and should not be backfilled","score_alignment":"delayed local 4B; do not backfill 180D rebound as immediate Stage2"}
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","round":"R11","loop":104,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","fine_archetype_id":"PF_POLICY_WEAK_LIQUIDITY_LABEL_FALSE_POSITIVE","source_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","symbol":"002990","name":"금호건설","trigger_type":"Stage2-FalsePositive","entry_date":"2024-01-26","entry_close":5030,"price_basis":"tradable_raw","mfe_30d_pct":5.00,"mae_30d_pct":-4.60,"mfe_90d_pct":5.00,"mae_90d_pct":-27.50,"mfe_180d_pct":5.00,"mae_180d_pct":-41.00,"forward_high_30d":5280,"forward_low_30d":4800,"forward_high_90d":5280,"forward_low_90d":3650,"forward_high_180d":5280,"forward_low_180d":2970,"calibration_usable":true,"case_role":"hard_counterexample","novelty_key":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT|002990|Stage2-FalsePositive|2024-01-26","non_price_bridge":"PF relief vocabulary without liquidity, debt-service, margin, guarantee relief or cash bridge","score_alignment":"hard block; policy umbrella did not become company cash bridge"}
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","round":"R11","loop":104,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","fine_archetype_id":"PF_POLICY_PRICE_ONLY_LOCAL_4B_OVERLAY","source_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","symbol":"047040","name":"대우건설","trigger_type":"Stage4B","entry_date":"2024-07-18","entry_close":4250,"price_basis":"tradable_raw","mfe_30d_pct":16.80,"mae_30d_pct":-16.60,"mfe_90d_pct":16.80,"mae_90d_pct":-17.20,"mfe_180d_pct":16.80,"mae_180d_pct":-30.80,"forward_high_30d":4965,"forward_low_30d":3545,"forward_high_90d":4965,"forward_low_90d":3520,"forward_high_180d":4965,"forward_low_180d":2940,"calibration_usable":true,"case_role":"price_only_4B_overlay","novelty_key":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT|047040|Stage4B|2024-07-18","non_price_bridge":"price rebound after PF/construction relief narrative without sufficient non-price issuer cash evidence","score_alignment":"local 4B only; 180D drawdown confirms no Green without bridge refresh"}
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","round":"R11","loop":104,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","fine_archetype_id":"PF_HOUSING_SOFT_LANDING_POLICY_DELAYED_LOCAL_4B","source_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","symbol":"294870","name":"HDC현대산업개발","trigger_type":"Stage2-Watch","entry_date":"2024-05-13","entry_close":17920,"price_basis":"tradable_raw","mfe_30d_pct":2.12,"mae_30d_pct":-6.58,"mfe_90d_pct":37.28,"mae_90d_pct":-6.58,"mfe_180d_pct":57.37,"mae_180d_pct":-6.58,"forward_high_30d":18300,"forward_low_30d":16740,"forward_high_90d":24600,"forward_low_90d":16740,"forward_high_180d":28200,"forward_low_180d":16740,"calibration_usable":true,"case_role":"delayed_positive_local_4B","novelty_key":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT|294870|Stage2-Watch|2024-05-13","non_price_bridge":"housing/PF soft-landing policy path, but issuer-specific refinancing/liquidity bridge was not visible at entry","score_alignment":"local 4B; do not backfill later rebound as immediate Stage2"}
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","round":"R11","loop":104,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","fine_archetype_id":"MID_BUILDER_POLICY_SUPPORT_DELAYED_LOCAL_4B","source_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","symbol":"014790","name":"HL D&I","trigger_type":"Stage2-Watch","entry_date":"2024-03-27","entry_close":2010,"price_basis":"tradable_raw","mfe_30d_pct":1.74,"mae_30d_pct":-3.73,"mfe_90d_pct":32.34,"mae_90d_pct":-3.73,"mfe_180d_pct":32.34,"mae_180d_pct":-3.73,"forward_high_30d":2045,"forward_low_30d":1935,"forward_high_90d":2660,"forward_low_90d":1935,"forward_high_180d":2660,"forward_low_180d":1935,"calibration_usable":true,"case_role":"delayed_positive_watch","novelty_key":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT|014790|Stage2-Watch|2024-03-27","non_price_bridge":"mid-builder PF support headline with delayed price validation but no immediate issuer-specific bridge","score_alignment":"Stage2-Watch / delayed 4B; require timestamped refinancing, presale or cash conversion bridge before Actionable"}
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","round":"R11","loop":104,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","fine_archetype_id":"PF_WORKOUT_POLICY_STRESS_CONTROL_NOT_CLEAN_EQUITY_RECOVERY","source_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","symbol":"009410","name":"태영건설","trigger_type":"Stage2-Watch","entry_date":"2024-01-11","entry_close":3765,"price_basis":"tradable_raw","mfe_30d_pct":9.16,"mae_30d_pct":-42.10,"mfe_90d_pct":9.16,"mae_90d_pct":-42.10,"mfe_180d_pct":62.28,"mae_180d_pct":-42.10,"forward_high_30d":4110,"forward_low_30d":2180,"forward_high_90d":4110,"forward_low_90d":2180,"forward_high_180d":6110,"forward_low_180d":2180,"calibration_usable":false,"case_role":"workout_stress_control_only","novelty_key":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT|009410|Stage2-Watch|2024-01-11","non_price_bridge":"workout / debt restructuring policy framework may preserve creditors before equity; corporate-action/trading-gap window not clean","score_alignment":"exclude from clean aggregate; use as stress-control for policy-workout-not-equity-recovery rule"}
```

---

## 4. Case analysis

### 4.1 Hyundai E&C / 000720 — policy survivor watch

Hyundai E&C shows that sector support can stabilize a large builder, but stabilization is not the same as an issuer cash bridge.

```yaml
entry_close: 33100
30D_MFE_MAE: +7.30 / -3.50
90D_MFE_MAE: +8.80 / -5.70
180D_MFE_MAE: +8.80 / -12.20
route: Stage2-Watch
```

### 4.2 Daewoo E&C / 047040 — delayed policy rebound

The early trigger did not validate. The later 180D rebound should not be backfilled.

```yaml
entry_close: 4015
30D_MFE_MAE: +2.60 / -5.60
90D_MFE_MAE: +2.60 / -10.80
180D_MFE_MAE: +23.70 / -12.30
route: delayed local 4B
```

### 4.3 Kumho E&C / 002990 — policy umbrella false positive

Kumho is the hard C31 counterexample. PF support vocabulary did not become liquidity or cash conversion.

```yaml
entry_close: 5030
30D_MFE_MAE: +5.00 / -4.60
90D_MFE_MAE: +5.00 / -27.50
180D_MFE_MAE: +5.00 / -41.00
route: Stage2-FalsePositive
```

### 4.4 Daewoo E&C / 047040 — price-only 4B overlay

The July local peak is a price-only overlay without enough non-price bridge.

```yaml
entry_close: 4250
30D_MFE_MAE: +16.80 / -16.60
90D_MFE_MAE: +16.80 / -17.20
180D_MFE_MAE: +16.80 / -30.80
route: local 4B only
```

### 4.5 HDC Hyundai Development / 294870 — delayed soft-landing 4B

HDC shows policy can later help, but the entry-date bridge was not visible.

```yaml
entry_close: 17920
30D_MFE_MAE: +2.12 / -6.58
90D_MFE_MAE: +37.28 / -6.58
180D_MFE_MAE: +57.37 / -6.58
route: delayed local 4B
```

### 4.6 HL D&I / 014790 — mid-builder delayed support

HL D&I is a useful delayed 4B row, not immediate Actionable.

```yaml
entry_close: 2010
30D_MFE_MAE: +1.74 / -3.73
90D_MFE_MAE: +32.34 / -3.73
180D_MFE_MAE: +32.34 / -3.73
route: delayed local 4B
```

### 4.7 Taeyoung E&C / 009410 — workout stress-control only

Workout framework is not clean equity recovery.

```yaml
entry_close: 3765
30D_MFE_MAE: +9.16 / -42.10
90D_MFE_MAE: +9.16 / -42.10
180D_MFE_MAE: +62.28 / -42.10
route: stress-control only
```

---

## 5. Score-return alignment

```yaml
new_independent_case_count: 6
stress_control_case_count: 1
calibration_usable_case_count: 6
calibration_usable_trigger_count: 6
positive_or_delayed_positive_count: 3
counterexample_or_cap_count: 4
local_4B_or_contribution_cap_count: 4
current_profile_error_count: 5
```

| symbol | role | 30D MFE/MAE | 90D MFE/MAE | 180D MFE/MAE | lesson |
|---|---:|---:|---:|---:|---|
| 000720 | policy survivor watch | +7.30 / -3.50 | +8.80 / -5.70 | +8.80 / -12.20 | stabilization is not cash bridge |
| 047040 | delayed rebound | +2.60 / -5.60 | +2.60 / -10.80 | +23.70 / -12.30 | no backfill |
| 002990 | hard false positive | +5.00 / -4.60 | +5.00 / -27.50 | +5.00 / -41.00 | policy label lacks liquidity bridge |
| 047040 | price-only 4B | +16.80 / -16.60 | +16.80 / -17.20 | +16.80 / -30.80 | no Green without non-price bridge |
| 294870 | delayed soft-landing | +2.12 / -6.58 | +37.28 / -6.58 | +57.37 / -6.58 | later validation only |
| 014790 | delayed support | +1.74 / -3.73 | +32.34 / -3.73 | +32.34 / -3.73 | support needs timestamped issuer bridge |
| 009410 | stress-control | +9.16 / -42.10 | +9.16 / -42.10 | +62.28 / -42.10 | workout is not clean equity recovery |

---

## 6. Raw component score breakdown

```jsonl
{"row_type":"score_simulation","symbol":"000720","raw_policy_directness":3,"raw_issuer_cash_bridge":2,"raw_refinancing_or_guarantee_relief":2,"raw_presale_or_debt_service":2,"raw_validation":2,"raw_label_only_risk":2,"stage2_actionable_bonus_before":2.0,"stage2_actionable_bonus_after":1.0,"simulated_route":"Stage2Watch_policy_survivor"}
{"row_type":"score_simulation","symbol":"047040","raw_policy_directness":3,"raw_issuer_cash_bridge":1,"raw_refinancing_or_guarantee_relief":1,"raw_presale_or_debt_service":1,"raw_validation":1,"raw_label_only_risk":3,"stage2_actionable_bonus_before":2.0,"stage2_actionable_bonus_after":1.0,"simulated_route":"DelayedLocal4B_no_backfill"}
{"row_type":"score_simulation","symbol":"002990","raw_policy_directness":3,"raw_issuer_cash_bridge":0,"raw_refinancing_or_guarantee_relief":0,"raw_presale_or_debt_service":0,"raw_validation":0,"raw_label_only_risk":5,"stage2_actionable_bonus_before":2.0,"stage2_actionable_bonus_after":0.0,"simulated_route":"Stage2FalsePositiveBlock"}
{"row_type":"score_simulation","symbol":"047040","raw_policy_directness":2,"raw_issuer_cash_bridge":0,"raw_refinancing_or_guarantee_relief":0,"raw_presale_or_debt_service":0,"raw_validation":1,"raw_label_only_risk":5,"stage2_actionable_bonus_before":1.0,"stage2_actionable_bonus_after":0.0,"simulated_route":"PriceOnlyLocal4B"}
{"row_type":"score_simulation","symbol":"294870","raw_policy_directness":3,"raw_issuer_cash_bridge":2,"raw_refinancing_or_guarantee_relief":2,"raw_presale_or_debt_service":2,"raw_validation":2,"raw_label_only_risk":2,"stage2_actionable_bonus_before":2.0,"stage2_actionable_bonus_after":1.0,"simulated_route":"DelayedLocal4B"}
{"row_type":"score_simulation","symbol":"014790","raw_policy_directness":3,"raw_issuer_cash_bridge":2,"raw_refinancing_or_guarantee_relief":2,"raw_presale_or_debt_service":2,"raw_validation":2,"raw_label_only_risk":2,"stage2_actionable_bonus_before":2.0,"stage2_actionable_bonus_after":1.0,"simulated_route":"DelayedLocal4B"}
{"row_type":"score_simulation","symbol":"009410","raw_policy_directness":5,"raw_issuer_cash_bridge":3,"raw_refinancing_or_guarantee_relief":4,"raw_presale_or_debt_service":2,"raw_validation":0,"raw_label_only_risk":3,"stage2_actionable_bonus_before":2.0,"stage2_actionable_bonus_after":0.0,"simulated_route":"StressControlOnly"}
```

---

## 7. Current calibrated profile stress test

### Existing error risk

C31 can still over-credit:

```text
PF support
housing relief
liquidity policy
workout framework
```

The correct C31 question is narrower:

```text
did the policy reach the issuer's cashflow?
```

A policy is a hose. It only matters if the hose is connected to the specific company’s balance sheet.

### Rule candidate

```text
C31_PF_POLICY_TO_ISSUER_CASH_BRIDGE_REQUIREMENT_V104

if C31
and PF_housing_liquidity_or_restructuring_policy_label == true
and issuer_specific_refinancing_guarantee_presale_cash_or_debt_service_bridge == false:
    stage2_actionable_bonus = 0
    max_stage = Stage2-Watch
```

```text
if C31
and MFE_30D_pct < +5
and MFE_90D_pct >= +25:
    route = delayed_local_4B
    do_not_backfill_as_immediate_Stage2_Actionable = true
```

```text
if C31
and price_only_rebound_or_local_peak == true
and non_price_bridge == false:
    route = local_4B_watch
    block_stage3_green = true
```

```text
if C31
and MFE_90D_pct <= +5
and MAE_90D_pct <= -20
and issuer_cash_bridge == false:
    route = Stage2_FalsePositive_Block
```

```text
if C31
and direct_workout_or_restructuring_policy == true
and shareholder_equity_bridge == false:
    route = StressControl_ExcludeCleanAggregate
    stage2_actionable_bonus = 0
```

---

## 8. Residual contribution summary

```yaml
do_not_propose_new_weight_delta: false
sector_specific_rule_candidate: false
canonical_archetype_rule_candidate: true
loop_contribution_label: canonical_archetype_rule_candidate
new_axis_proposed: C31_PF_POLICY_TO_ISSUER_CASH_BRIDGE_REQUIREMENT_V104
existing_axis_strengthened:
  - C31_policy_label_not_enough_without_company_cash_bridge
  - C31_PF_housing_support_delay_no_backfill
  - C31_price_only_policy_rebound_local_4B
  - C31_weak_liquidity_policy_false_positive_block
  - C31_workout_policy_not_clean_equity_recovery
existing_axis_weakened: null
```

---

## 9. Deferred Coding Agent Handoff Prompt

```text
Do not patch production scoring from this MD alone. Batch this C31 loop with C31 loops 100~103, C30 loops 3/100/101/102, and R13 construction/PF accounting-trust, Stage2 false-positive, high-MAE and 4B/4C guardrails. Extract `C31_PF_POLICY_TO_ISSUER_CASH_BRIDGE_REQUIREMENT_V104` as a shadow-rule candidate. Preserve delayed local 4B policy-relief paths, but block PF/housing/restructuring policy labels without issuer-specific refinancing, guarantee, presale, cash conversion, debt-service or equity bridge.
```

---

## 10. Next research state

```yaml
completed_round: R11
completed_loop: 104
selection_basis: docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket: Priority 0
round_schedule_status: coverage_index_selected
round_sector_consistency: pass
next_recommended_archetypes:
  - C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP
  - C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY
  - C15_MATERIAL_SPREAD_SUPERCYCLE
  - R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION
  - C18_CONSUMER_EXPORT_CHANNEL_REORDER
```
