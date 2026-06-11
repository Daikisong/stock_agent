# E2R v12 residual calibration research

## 0. Execution metadata

```yaml
schema_family: v12_sector_archetype_residual
selected_round: R10
selected_loop: 102
large_sector_id: L9_CONSTRUCTION_REALESTATE_HOUSING
canonical_archetype_id: C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK
fine_archetype_id: PF_REFINANCING_LIQUIDITY_SUPPORT_TO_ISSUER_CASH_BRIDGE_VS_CONSTRUCTION_BETA_AND_PRICE_ONLY_4B
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

`C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK` remains Priority 0 in the no-repeat index: 3 representative rows, 27 rows short of the 30-row minimum. The v12 scheduler maps C30 to `R10 / L9_CONSTRUCTION_REALESTATE_HOUSING`.

Existing local C30 files already include both an early `loop 1~3` sequence and an older `loop 100~101` sequence. Under the v12 loop rule, this execution uses the largest visible R10/C30 loop plus one, so the selected loop is `102`.

This is not a live construction-stock screen. It is a historical calibration and residual rule file. Direct uncached `stock-web` symbol shards returned cache misses in this turn, so the trigger rows below reuse stock-web-derived rows already calculated in current-session C30/C05/R13 files. Every usable trigger below still includes complete 30D/90D/180D MFE and MAE from `Songdaiki/stock-web` tradable OHLC. No production scoring is changed.

---

## 1. Research thesis

C30 is not `PF support headline = survivor`.

It is the issuer-specific balance-sheet bridge:

```text
PF stress / liquidity support / restructuring / refinancing / housing rebound
→ issuer-specific maturity rollover, guarantee relief, presale recovery, cash conversion, debt-service capacity
→ equity price validation
```

The failure mode is familiar. A sector policy headline can lift all builders for a few weeks, but some companies are repairing a balance sheet while others are only borrowing time. The model must separate the stopped bleeding from the healed patient.

This loop splits seven routes:

1. **Large-builder low-MAE survivor**
   - Stage2 can remain open when balance-sheet risk stays contained and drawdown is controlled.
   - It is not automatically Green without margin/cash bridge.

2. **Delayed construction rebound**
   - If 30D MFE is weak but 180D MFE later appears, do not backfill the original trigger as immediate Actionable.
   - Route to delayed local 4B unless later issuer-specific bridge is timestamped.

3. **Weak liquidity / low-PBR builder false positive**
   - Low-PBR or PF relief vocabulary without debt-service and margin bridge should hard block.

4. **Price-only local 4B overlay**
   - A spike after rebound can be local 4B, but without non-price evidence it should not become full 4B/Green.

5. **Developer delayed positive**
   - Later housing/PF soft-landing paths can be useful, but only as delayed 4B until bridge refresh.

6. **Mid-builder support headline**
   - Shallow drawdown and delayed MFE can stay on watch, but immediate Stage2 is not justified.

7. **Direct workout stress-control**
   - Workout/restructuring survival should not be treated as clean equity recovery.

---

## 2. Source validation

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
  - R10/C30 loop 100
  - R10/C30 loop 101
  - R10/C30 loop 3
  - R1/C05 loop 114
  - R13 accounting-trust / Stage2 false-positive / high-MAE / 4B-4C construction guardrails
reason:
  - all trigger rows were already calculated from Songdaiki/stock-web tradable raw 1D OHLC
  - this file changes the calibration lens back to C30 and consolidates a PF/refinancing cash-bridge gate
  - exact source-archetype keys should be deduped separately from this C30 loop
  - no production scoring changed
```

Symbol caveats:

```yaml
000720:
  name: 현대건설
  role: large-builder low-MAE survivor control from early PF support trigger
  calibration_usable: true

047040:
  name: 대우건설
  role: delayed rebound and price-only 4B overlay controls
  calibration_usable: true

002990:
  name: 금호건설
  role: weak liquidity / low-PBR false-positive control
  calibration_usable: true

294870:
  name: HDC현대산업개발
  role: delayed housing/PF soft-landing local 4B
  calibration_usable: true

014790:
  name: HL D&I
  role: mid-builder delayed support headline local 4B
  calibration_usable: true

009410:
  name: 태영건설
  role: direct workout stress-control
  calibration_usable: false
  caveat: workout / corporate-action / trading-gap contamination; stress-control only
```

---

## 3. Trigger rows

```jsonl
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","round":"R10","loop":102,"large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","fine_archetype_id":"LARGE_BUILDER_BALANCE_SHEET_SURVIVOR_LOW_MAE_CONTROL","symbol":"000720","name":"현대건설","trigger_type":"Stage2-Actionable","entry_date":"2024-01-26","entry_close":33100,"price_basis":"tradable_raw","MFE_30D_pct":7.30,"MAE_30D_pct":-3.50,"MFE_90D_pct":8.80,"MAE_90D_pct":-5.70,"MFE_180D_pct":8.80,"MAE_180D_pct":-12.20,"forward_high_30d":34850,"forward_low_30d":31950,"forward_high_90d":36000,"forward_low_90d":31200,"forward_high_180d":36000,"forward_low_180d":29050,"calibration_usable":true,"case_role":"low_MAE_survivor_control","novelty_key":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK|000720|Stage2-Actionable|2024-01-26","non_price_bridge":"large-builder balance-sheet survivor / order-quality bridge under PF relief lens; not Green without margin/cash bridge","score_alignment":"Stage2 can survive, but Green requires issuer-specific margin, receivable and cash conversion refresh","aggregate_credit_note":"exact key likely represented in C30 loop 100; use as control if deduped"}
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","round":"R10","loop":102,"large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","fine_archetype_id":"DELAYED_BUILDER_REBOUND_DO_NOT_BACKFILL_IMMEDIATE_STAGE2","symbol":"047040","name":"대우건설","trigger_type":"Stage2-Actionable","entry_date":"2024-01-26","entry_close":4015,"price_basis":"tradable_raw","MFE_30D_pct":2.60,"MAE_30D_pct":-5.60,"MFE_90D_pct":2.60,"MAE_90D_pct":-10.80,"MFE_180D_pct":23.70,"MAE_180D_pct":-12.30,"forward_high_30d":4120,"forward_low_30d":3790,"forward_high_90d":4120,"forward_low_90d":3580,"forward_high_180d":4965,"forward_low_180d":3520,"calibration_usable":true,"case_role":"delayed_rebound_control","novelty_key":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK|047040|Stage2-Actionable|2024-01-26","non_price_bridge":"PF relief plus order/margin bridge partially visible, but price validation arrived late","score_alignment":"delayed local 4B; do not backfill 180D rebound as immediate Stage2-Actionable","aggregate_credit_note":"exact key likely represented in C30 loop 100; use as delayed-control if deduped"}
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","round":"R10","loop":102,"large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","fine_archetype_id":"WEAK_LIQUIDITY_PF_RELIEF_LABEL_LOW_MFE_HIGH_MAE_FALSE_POSITIVE","symbol":"002990","name":"금호건설","trigger_type":"Stage2-FalsePositive","entry_date":"2024-01-26","entry_close":5030,"price_basis":"tradable_raw","MFE_30D_pct":5.00,"MAE_30D_pct":-4.60,"MFE_90D_pct":5.00,"MAE_90D_pct":-27.50,"MFE_180D_pct":5.00,"MAE_180D_pct":-41.00,"forward_high_30d":5280,"forward_low_30d":4800,"forward_high_90d":5280,"forward_low_90d":3650,"forward_high_180d":5280,"forward_low_180d":2970,"calibration_usable":true,"case_role":"hard_counterexample","novelty_key":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK|002990|Stage2-FalsePositive|2024-01-26","non_price_bridge":"low-PBR/PF-relief vocabulary without liquidity, debt-service, margin or cash bridge","score_alignment":"hard block; low MFE and deep MAE reject generic PF relief Stage2","aggregate_credit_note":"exact key likely represented in C30 loop 100; use as hard counterexample if deduped"}
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","round":"R10","loop":102,"large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","fine_archetype_id":"PRICE_ONLY_LOCAL_4B_AFTER_REBOUND_WITHOUT_NON_PRICE_CONFIRMATION","symbol":"047040","name":"대우건설","trigger_type":"Stage4B","entry_date":"2024-07-18","entry_close":4250,"price_basis":"tradable_raw","MFE_30D_pct":16.80,"MAE_30D_pct":-16.60,"MFE_90D_pct":16.80,"MAE_90D_pct":-17.20,"MFE_180D_pct":16.80,"MAE_180D_pct":-30.80,"forward_high_30d":4965,"forward_low_30d":3545,"forward_high_90d":4965,"forward_low_90d":3520,"forward_high_180d":4965,"forward_low_180d":2940,"calibration_usable":true,"case_role":"price_only_4B_overlay","novelty_key":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK|047040|Stage4B|2024-07-18","non_price_bridge":"price spike after construction/PF rebound vocabulary; non-price confirmation insufficient for full 4B production action","score_alignment":"local 4B watch only; 180D MAE confirms that price-only 4B should not become Green","aggregate_credit_note":"exact key likely represented in C30 loop 100 as overlay; use as 4B timing control"}
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","round":"R10","loop":102,"large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","fine_archetype_id":"DEVELOPER_DELAYED_HOUSING_PF_SOFT_LANDING_LOCAL_4B","symbol":"294870","name":"HDC현대산업개발","trigger_type":"Stage2-Watch","entry_date":"2024-05-13","entry_close":17920,"price_basis":"tradable_raw","MFE_30D_pct":2.12,"MAE_30D_pct":-6.58,"MFE_90D_pct":37.28,"MAE_90D_pct":-6.58,"MFE_180D_pct":57.37,"MAE_180D_pct":-6.58,"forward_high_30d":18300,"forward_low_30d":16740,"forward_high_90d":24600,"forward_low_90d":16740,"forward_high_180d":28200,"forward_low_180d":16740,"calibration_usable":true,"case_role":"delayed_positive_local_4B","novelty_key":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK|294870|Stage2-Watch|2024-05-13","non_price_bridge":"delayed PF/housing soft-landing path, but issuer-specific refinancing/liquidity bridge not visible at entry","score_alignment":"local 4B; do not backfill later rebound as immediate Stage2-Actionable","aggregate_credit_note":"exact key likely represented in C30 loop 3; use as delayed local 4B control"}
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","round":"R10","loop":102,"large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","fine_archetype_id":"MID_BUILDER_SUPPORT_HEADLINE_DELAYED_LOCAL_4B","symbol":"014790","name":"HL D&I","trigger_type":"Stage2-Watch","entry_date":"2024-03-27","entry_close":2010,"price_basis":"tradable_raw","MFE_30D_pct":1.74,"MAE_30D_pct":-3.73,"MFE_90D_pct":32.34,"MAE_90D_pct":-3.73,"MFE_180D_pct":32.34,"MAE_180D_pct":-3.73,"forward_high_30d":2045,"forward_low_30d":1935,"forward_high_90d":2660,"forward_low_90d":1935,"forward_high_180d":2660,"forward_low_180d":1935,"calibration_usable":true,"case_role":"delayed_positive_watch","novelty_key":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK|014790|Stage2-Watch|2024-03-27","non_price_bridge":"mid-builder liquidity/PF soft-landing support headline with delayed price validation but no immediate issuer bridge","score_alignment":"delayed local 4B; do not backfill as immediate Actionable","aggregate_credit_note":"exact key likely represented in C30 loop 3; use as support-headline delayed control"}
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","round":"R10","loop":102,"large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","fine_archetype_id":"DIRECT_WORKOUT_STRESS_CONTROL_NOT_CLEAN_EQUITY_RECOVERY","symbol":"009410","name":"태영건설","trigger_type":"Stage2-Watch","entry_date":"2024-01-11","entry_close":3765,"price_basis":"tradable_raw","MFE_30D_pct":9.16,"MAE_30D_pct":-42.10,"MFE_90D_pct":9.16,"MAE_90D_pct":-42.10,"MFE_180D_pct":62.28,"MAE_180D_pct":-42.10,"forward_high_30d":4110,"forward_low_30d":2180,"forward_high_90d":4110,"forward_low_90d":2180,"forward_high_180d":6110,"forward_low_180d":2180,"calibration_usable":false,"case_role":"workout_stress_control_only","novelty_key":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK|009410|Stage2-Watch|2024-01-11","non_price_bridge":"direct workout / debt restructuring survival bridge, but equity recovery and corporate-action/trading-gap window are not clean","score_alignment":"exclude from clean aggregate; use as stress-control for workout-not-equity-recovery rule","aggregate_credit_note":"stress-control only, not representative aggregate"}
```

---

## 4. Case analysis

### 4.1 Hyundai E&C / 000720 — large-builder survivor control

Hyundai E&C from the early PF-relief window had low MAE but modest MFE. It can remain Stage2, but it is not a Green unlock.

```yaml
entry_close: 33100
30D_MFE_MAE: +7.30 / -3.50
90D_MFE_MAE: +8.80 / -5.70
180D_MFE_MAE: +8.80 / -12.20
route: Stage2 survivor control
```

The price did not break, but the upside was modest. C30 should demand cash and margin bridge for promotion.

---

### 4.2 Daewoo E&C / 047040 — delayed rebound, no backfill

The January 2024 trigger did not validate inside 30D/90D, but later 180D MFE appeared.

```yaml
entry_close: 4015
30D_MFE_MAE: +2.60 / -5.60
90D_MFE_MAE: +2.60 / -10.80
180D_MFE_MAE: +23.70 / -12.30
route: delayed local 4B
```

This is the classic delayed-rebound case. It should not be scored as immediate Stage2 unless the later bridge is timestamped.

---

### 4.3 Kumho E&C / 002990 — weak-liquidity PF relief false positive

Kumho is the clean hard counterexample.

```yaml
entry_close: 5030
30D_MFE_MAE: +5.00 / -4.60
90D_MFE_MAE: +5.00 / -27.50
180D_MFE_MAE: +5.00 / -41.00
route: Stage2-FalsePositive
```

PF relief vocabulary did not become liquidity repair or cash conversion.

---

### 4.4 Daewoo E&C / 047040 — price-only 4B overlay

The later July spike is not a separate fundamental success without non-price confirmation.

```yaml
entry_close: 4250
30D_MFE_MAE: +16.80 / -16.60
90D_MFE_MAE: +16.80 / -17.20
180D_MFE_MAE: +16.80 / -30.80
route: local 4B only
```

The 180D drawdown proves why price-only 4B must stay local.

---

### 4.5 HDC Hyundai Development / 294870 — delayed soft-landing local 4B

HDC had a strong delayed path, but entry-date accounting bridge was incomplete.

```yaml
entry_close: 17920
30D_MFE_MAE: +2.12 / -6.58
90D_MFE_MAE: +37.28 / -6.58
180D_MFE_MAE: +57.37 / -6.58
route: delayed local 4B
```

---

### 4.6 HL D&I / 014790 — support headline delayed positive

HL D&I has the same shape: weak immediate MFE, later strong MFE, shallow MAE.

```yaml
entry_close: 2010
30D_MFE_MAE: +1.74 / -3.73
90D_MFE_MAE: +32.34 / -3.73
180D_MFE_MAE: +32.34 / -3.73
route: delayed local 4B
```

Do not backfill into the trigger date.

---

### 4.7 Taeyoung E&C / 009410 — workout stress-control only

Taeyoung is crucial but not clean aggregate evidence.

```yaml
entry_close: 3765
30D_MFE_MAE: +9.16 / -42.10
90D_MFE_MAE: +9.16 / -42.10
180D_MFE_MAE: +62.28 / -42.10
route: stress-control only
```

Workout can preserve creditors before equity. This row stays out of clean aggregate.

---

## 5. Score-return alignment

```yaml
new_independent_case_count: 0
reused_control_case_count: 7
calibration_usable_case_count: 6
calibration_usable_trigger_count: 6
stress_control_case_count: 1
positive_or_delayed_positive_count: 4
counterexample_or_cap_count: 3
local_4B_or_contribution_cap_count: 4
current_profile_error_count: 4
duplicate_note: exact C30 novelty keys likely already represented in loops 3, 100 and 101; this file is rule-consolidation evidence unless batch ingest finds an unrepresented key
```

| symbol | role | 30D MFE/MAE | 90D MFE/MAE | 180D MFE/MAE | lesson |
|---|---:|---:|---:|---:|---|
| 000720 | survivor control | +7.30 / -3.50 | +8.80 / -5.70 | +8.80 / -12.20 | low-MAE survivor, not Green |
| 047040 | delayed rebound | +2.60 / -5.60 | +2.60 / -10.80 | +23.70 / -12.30 | do not backfill 180D rebound |
| 002990 | hard counterexample | +5.00 / -4.60 | +5.00 / -27.50 | +5.00 / -41.00 | weak liquidity label fails |
| 047040 | price-only 4B | +16.80 / -16.60 | +16.80 / -17.20 | +16.80 / -30.80 | local 4B, no Green |
| 294870 | delayed 4B | +2.12 / -6.58 | +37.28 / -6.58 | +57.37 / -6.58 | later validation only |
| 014790 | delayed 4B | +1.74 / -3.73 | +32.34 / -3.73 | +32.34 / -3.73 | support headline needs timestamped bridge |
| 009410 | stress-control | +9.16 / -42.10 | +9.16 / -42.10 | +62.28 / -42.10 | workout is not clean equity recovery |

---

## 6. Raw component score breakdown

```jsonl
{"row_type":"score_simulation","symbol":"000720","raw_PF_refinancing_bridge":2,"raw_liquidity_survival_bridge":3,"raw_equity_value_bridge":2,"raw_cash_conversion":2,"raw_validation":2,"raw_label_only_risk":1,"stage2_actionable_bonus_before":2.0,"stage2_actionable_bonus_after":1.0,"simulated_route":"Stage2Survivor_NotGreen"}
{"row_type":"score_simulation","symbol":"047040","raw_PF_refinancing_bridge":2,"raw_liquidity_survival_bridge":2,"raw_equity_value_bridge":2,"raw_cash_conversion":1,"raw_validation":1,"raw_label_only_risk":2,"stage2_actionable_bonus_before":2.0,"stage2_actionable_bonus_after":1.0,"simulated_route":"DelayedLocal4B_NoBackfill"}
{"row_type":"score_simulation","symbol":"002990","raw_PF_refinancing_bridge":0,"raw_liquidity_survival_bridge":0,"raw_equity_value_bridge":0,"raw_cash_conversion":0,"raw_validation":0,"raw_label_only_risk":5,"stage2_actionable_bonus_before":2.0,"stage2_actionable_bonus_after":0.0,"simulated_route":"Stage2FalsePositiveBlock"}
{"row_type":"score_simulation","symbol":"047040","raw_PF_refinancing_bridge":1,"raw_liquidity_survival_bridge":1,"raw_equity_value_bridge":1,"raw_cash_conversion":0,"raw_validation":1,"raw_label_only_risk":4,"stage2_actionable_bonus_before":1.0,"stage2_actionable_bonus_after":0.0,"simulated_route":"PriceOnlyLocal4B"}
{"row_type":"score_simulation","symbol":"294870","raw_PF_refinancing_bridge":2,"raw_liquidity_survival_bridge":2,"raw_equity_value_bridge":2,"raw_cash_conversion":1,"raw_validation":2,"raw_label_only_risk":2,"stage2_actionable_bonus_before":2.0,"stage2_actionable_bonus_after":1.0,"simulated_route":"DelayedLocal4B"}
{"row_type":"score_simulation","symbol":"014790","raw_PF_refinancing_bridge":2,"raw_liquidity_survival_bridge":2,"raw_equity_value_bridge":2,"raw_cash_conversion":1,"raw_validation":2,"raw_label_only_risk":2,"stage2_actionable_bonus_before":2.0,"stage2_actionable_bonus_after":1.0,"simulated_route":"DelayedLocal4B"}
{"row_type":"score_simulation","symbol":"009410","raw_PF_refinancing_bridge":4,"raw_liquidity_survival_bridge":3,"raw_equity_value_bridge":0,"raw_cash_conversion":0,"raw_validation":0,"raw_label_only_risk":3,"stage2_actionable_bonus_before":2.0,"stage2_actionable_bonus_after":0.0,"simulated_route":"StressControlOnly"}
```

---

## 7. Current calibrated profile stress test

### Existing error risk

C30 can over-credit:

```text
PF support headline
low-PBR construction rebound
large-builder label
workout survival
```

The correct C30 test is narrower:

```text
issuer-specific refinancing / maturity / guarantee / presale / cash conversion / debt-service bridge
```

A sector support headline is an umbrella. C30 needs to know whether the specific house is still leaking.

### Rule candidate

```text
C30_PF_REFINANCING_TO_ISSUER_CASH_BRIDGE_REQUIREMENT_V102

if C30
and PF_support_construction_rebound_or_low_PBR_label == true
and issuer_specific_refinancing_guarantee_presale_cash_or_debt_service_bridge == false:
    stage2_actionable_bonus = 0
    max_stage = Stage2-Watch
```

```text
if C30
and MFE_30D_pct < +5
and MFE_90D_pct >= +25:
    route = delayed_local_4B
    do_not_backfill_as_immediate_Stage2_Actionable = true
```

```text
if C30
and price_only_rebound_or_local_peak == true
and non_price_bridge == false:
    route = local_4B_watch
    block_stage3_green = true
```

```text
if C30
and MFE_90D_pct <= +5
and MAE_90D_pct <= -20
and liquidity_cash_bridge == false:
    route = Stage2_FalsePositive_Block
```

```text
if C30
and direct_workout_or_debt_restructuring == true
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
loop_contribution_label: canonical_archetype_rule_formalization_from_existing_controls
new_axis_proposed: C30_PF_REFINANCING_TO_ISSUER_CASH_BRIDGE_REQUIREMENT_V102
existing_axis_strengthened:
  - C30_PF_support_headline_not_enough_without_issuer_bridge
  - C30_delayed_rebound_do_not_backfill
  - C30_price_only_4B_local_watch
  - C30_weak_liquidity_low_MFE_high_MAE_false_positive_block
  - C30_workout_survival_not_clean_equity_recovery
existing_axis_weakened: null
```

---

## 9. Deferred Coding Agent Handoff Prompt

```text
Do not patch production scoring from this single MD. Batch this C30 loop with C30 loops 1~3 and 100~101 plus C05 and R13 construction/PF guardrail files. Extract `C30_PF_REFINANCING_TO_ISSUER_CASH_BRIDGE_REQUIREMENT_V102` as a shadow-rule candidate. Preserve low-MAE large-builder survivor controls, keep delayed rebound cases in local 4B without backfilling, block weak-liquidity PF-relief labels, and exclude direct workout rows from clean equity aggregate unless shareholder bridge is separately validated.
```

---

## 10. Next research state

```yaml
completed_round: R10
completed_loop: 102
selection_basis: docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket: Priority 0
round_schedule_status: coverage_index_selected
round_sector_consistency: pass
next_recommended_archetypes:
  - C31_POLICY_SUBSIDY_LEGISLATION_EVENT
  - C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP
  - C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY
  - C15_MATERIAL_SPREAD_SUPERCYCLE
  - R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION
```
