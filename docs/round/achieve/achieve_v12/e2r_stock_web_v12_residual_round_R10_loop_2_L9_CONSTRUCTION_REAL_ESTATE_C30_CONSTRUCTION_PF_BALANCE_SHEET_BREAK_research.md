# E2R v12 residual calibration research

## 0. Execution metadata

```yaml
schema_family: v12_sector_archetype_residual
selected_round: R10
selected_loop: 2
large_sector_id: L9_CONSTRUCTION_REAL_ESTATE
canonical_archetype_id: C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK
fine_archetype_id: DIRECT_WORKOUT_DEBT_RESTRUCTURING_VS_PF_SUPPORT_LABEL_AND_SECTOR_BETA
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

`C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK` remains thin in the no-repeat index: 3 rows / 3 symbols. The previous local C30 run used `294870`, `047040`, and `375500` at the 2024-05-13 PF restructuring anchor. This loop therefore changes the trigger family to direct workout / March-2024 support retest and adds new C30 tuples: `014790`, `004960`, `000720`. `009410` is included as a direct workout stress-control, but because it is visible in the existing index and has a 2024-10-31 corporate-action candidate, it is treated as a high-value control rather than clean new aggregate coverage.

---

## 1. Research thesis

C30 is the balance-sheet break archetype:

```text
PF stress / debt maturity / guarantee exposure
→ workout, maturity extension, liquidity support, or project restructuring
→ issuer-specific debt-service and cash-flow relief
→ price path validation
```

This loop separates four routes.

1. **Direct workout stress-control**: direct restructuring is real, but it can be equity-negative or corporate-action contaminated. Do not score it as automatic recovery.
2. **PF support delayed-positive**: a support headline can become useful only if the issuer later shows refinancing/liquidity relief and price confirms.
3. **Sector-beta rebound**: construction stocks can rally on housing/PF soft-landing beta without a company-specific balance-sheet bridge.
4. **Support-label false positive**: government support headlines without issuer-specific bridge can decay into deep MAE.

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

Symbol caveats:

```yaml
009410:
  name: 태영건설
  corporate_action_candidate_dates: [2007-05-03, 2020-09-22, 2024-10-31]
  use: direct workout stress-control only; not counted as clean new aggregate coverage

014790:
  name: HL D&I
  corporate_action_candidate_dates: [1996-01-03, 1997-11-03, 1997-12-27, 1999-12-21, 2010-04-28, 2012-02-06]
  relevant_window_after_candidate: true

004960:
  name: 한신공영
  corporate_action_candidate_dates: [1998-09-19, 2001-06-20, 2002-04-03, 2002-05-24, 2002-11-14]
  relevant_window_after_candidate: true

000720:
  name: 현대건설
  corporate_action_candidate_dates: [1998-05-23, 1998-11-19, 1999-03-05, 2001-07-06, 2001-07-12, 2004-01-13, 2004-04-07]
  relevant_window_after_candidate: true
```

External macro anchor:

```text
2024-03-27: South Korean authorities announced financial support for builders and small businesses.
2024-05-13: FSS tightened and broadened real-estate PF project assessments to accelerate restructuring.
```

---

## 3. Trigger rows

```jsonl
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","round":"R10","loop":2,"large_sector_id":"L9_CONSTRUCTION_REAL_ESTATE","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","fine_archetype_id":"DIRECT_WORKOUT_STRESS_CONTROL_EQUITY_NEGATIVE_AND_CORPORATE_ACTION_CONTAMINATED","symbol":"009410","name":"태영건설","trigger_type":"Stage2-Watch","entry_date":"2024-01-11","entry_close":3765,"price_basis":"tradable_raw","mfe_30d_pct":9.16,"mae_30d_pct":-42.10,"mfe_90d_pct":9.16,"mae_90d_pct":-42.10,"mfe_180d_pct":62.28,"mae_180d_pct":-42.10,"forward_high_30d":4110,"forward_low_30d":2180,"forward_high_90d":4110,"forward_low_90d":2180,"forward_high_180d":6110,"forward_low_180d":2180,"calibration_usable":false,"case_role":"direct_workout_stress_control_not_clean_aggregate","novelty_key":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK|009410|Stage2-Watch|2024-01-11","non_price_bridge":"direct creditor workout / debt restructuring stress case; later trading gap and 2024-10-31 corporate-action candidate contaminate full-window use","score_alignment":"do not treat workout as immediate equity recovery; use as control for deep-MAE and corporate-action guardrail"}
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","round":"R10","loop":2,"large_sector_id":"L9_CONSTRUCTION_REAL_ESTATE","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","fine_archetype_id":"MID_BUILDER_SUPPORT_HEADLINE_DELAYED_PF_SOFT_LANDING_POSITIVE_WITH_4B_WATCH","symbol":"014790","name":"HL D&I","trigger_type":"Stage2-Watch","entry_date":"2024-03-27","entry_close":2010,"price_basis":"tradable_raw","mfe_30d_pct":1.74,"mae_30d_pct":-3.73,"mfe_90d_pct":32.34,"mae_90d_pct":-3.73,"mfe_180d_pct":32.34,"mae_180d_pct":-3.73,"forward_high_30d":2045,"forward_low_30d":1935,"forward_high_90d":2660,"forward_low_90d":1935,"forward_high_180d":2660,"forward_low_180d":1935,"calibration_usable":true,"case_role":"delayed_positive_with_4B_watch","novelty_key":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK|014790|Stage2-Watch|2024-03-27","non_price_bridge":"builder liquidity/PF soft-landing support headline; delayed price validation rather than immediate balance-sheet proof","score_alignment":"allow delayed local 4B; require issuer-specific refinancing, presale or cash-flow bridge before Actionable"}
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","round":"R10","loop":2,"large_sector_id":"L9_CONSTRUCTION_REAL_ESTATE","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","fine_archetype_id":"SMALL_BUILDER_SUPPORT_BETA_MODEST_MFE_WITH_BRIDGE_REFRESH_REQUIREMENT","symbol":"004960","name":"한신공영","trigger_type":"Stage2-Watch","entry_date":"2024-03-27","entry_close":6720,"price_basis":"tradable_raw","mfe_30d_pct":8.48,"mae_30d_pct":-8.33,"mfe_90d_pct":8.48,"mae_90d_pct":-8.33,"mfe_180d_pct":18.60,"mae_180d_pct":-8.63,"forward_high_30d":7290,"forward_low_30d":6160,"forward_high_90d":7290,"forward_low_90d":6160,"forward_high_180d":7970,"forward_low_180d":6140,"calibration_usable":true,"case_role":"sector_beta_rebound_with_contribution_cap","novelty_key":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK|004960|Stage2-Watch|2024-03-27","non_price_bridge":"construction/PF support beta; no clean issuer-specific debt relief bridge at trigger","score_alignment":"cap C30 contribution; require direct liquidity or PF exposure reduction evidence"}
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","round":"R10","loop":2,"large_sector_id":"L9_CONSTRUCTION_REAL_ESTATE","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","fine_archetype_id":"LARGE_BUILDER_SUPPORT_LABEL_LOW_MFE_HIGH_MAE_FALSE_POSITIVE_BLOCK","symbol":"000720","name":"현대건설","trigger_type":"Stage2-FalsePositive","entry_date":"2024-03-27","entry_close":33250,"price_basis":"tradable_raw","mfe_30d_pct":4.81,"mae_30d_pct":-6.17,"mfe_90d_pct":8.27,"mae_90d_pct":-6.17,"mfe_180d_pct":8.27,"mae_180d_pct":-27.52,"forward_high_30d":34850,"forward_low_30d":31200,"forward_high_90d":36000,"forward_low_90d":31200,"forward_high_180d":36000,"forward_low_180d":24100,"calibration_usable":true,"case_role":"hard_counterexample","novelty_key":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK|000720|Stage2-FalsePositive|2024-03-27","non_price_bridge":"large-builder support label without issuer-specific PF/refinancing bridge; later deep drawdown","score_alignment":"contractor quality or sector support label is insufficient; block Stage2-Actionable without balance-sheet bridge"}
```

---

## 4. Case analysis

### 4.1 Taeyoung E&C / 009410 — direct workout is not automatic equity recovery

Taeyoung is the direct workout stress-control. The event is real, but the price path and corporate-action caveat make it dangerous for clean aggregate calibration.

```yaml
entry_date: 2024-01-11
entry_close: 3765
30d_high: 4110
30d_low: 2180
180d_high: 6110
180d_low: 2180
mfe_30d_pct: 9.16
mae_30d_pct: -42.10
mfe_180d_pct: 62.28
mae_180d_pct: -42.10
```

The lesson is sharp: direct workout can be a survival bridge, but not necessarily a shareholder bridge. Debt rescheduling can save the building while still flooding the equity basement through dilution, asset sales, trading suspension, creditor control, or corporate-action reset.

Route:

```text
direct_workout_stress_control
calibration_usable = false for clean aggregate because 2024-10-31 corporate-action candidate contaminates full-window path
```

---

### 4.2 HL D&I / 014790 — delayed positive after support headline

HL D&I is the useful delayed-positive case. The March support headline did not create immediate MFE; the later June move validated a soft-landing / liquidity beta path.

```yaml
entry_close: 2010
30d_high: 2045
30d_low: 1935
90d_high: 2660
90d_low: 1935
180d_high: 2660
180d_low: 1935
```

This should not be backfilled as immediate Stage2-Actionable. It is local 4B watch first, then potential delayed positive if issuer-specific bridge appears.

---

### 4.3 Hanshin Engineering / 004960 — modest support beta with contribution cap

Hanshin had modest early MFE and later a larger but still not fully clean move. The case says small/mid-builder support beta can work, but C30 contribution should be capped until the balance-sheet bridge is explicit.

```yaml
entry_close: 6720
30d_high: 7290
30d_low: 6160
180d_high: 7970
180d_low: 6140
```

Route:

```text
Stage2-Watch
cap_C30_contribution = true unless refinancing / PF exposure reduction / cash conversion is refreshed
```

---

### 4.4 Hyundai E&C / 000720 — large-builder label false positive

Hyundai E&C is the large-builder false-positive control. The support headline did not become a durable C30 rerating. The forward high stayed below +10%, while the full-window low collapsed to 24,100.

```yaml
entry_close: 33250
30d_high: 34850
30d_low: 31200
90d_high: 36000
90d_low: 31200
180d_high: 36000
180d_low: 24100
```

Route:

```text
Stage2-FalsePositive_Block
```

The model should not confuse “large construction company” with “PF balance-sheet risk removed.”

---

## 5. Score-return alignment

```yaml
new_independent_case_count: 3
reused_or_visible_control_case_count: 1
new_visible_C30_symbol_count: 3
calibration_usable_case_count: 3
calibration_usable_trigger_count: 3
positive_or_delayed_positive_count: 2
counterexample_or_cap_count: 2
current_profile_error_count: 3
```

| symbol | role | 30D MFE/MAE | 90D MFE/MAE | 180D MFE/MAE | lesson |
|---|---:|---:|---:|---:|---|
| 009410 | direct workout stress-control | +9.16 / -42.10 | +9.16 / -42.10 | +62.28 / -42.10 | direct workout is not clean shareholder recovery |
| 014790 | delayed positive | +1.74 / -3.73 | +32.34 / -3.73 | +32.34 / -3.73 | delayed 4B only after bridge refresh |
| 004960 | sector beta cap | +8.48 / -8.33 | +8.48 / -8.33 | +18.60 / -8.63 | support beta needs issuer-specific proof |
| 000720 | hard counterexample | +4.81 / -6.17 | +8.27 / -6.17 | +8.27 / -27.52 | large-builder support label failed |

---

## 6. Raw component score breakdown

```jsonl
{"row_type":"score_simulation","symbol":"009410","raw_PF_refinancing_bridge":4,"raw_liquidity_survival_bridge":3,"raw_equity_value_bridge":0,"raw_cash_conversion":0,"raw_validation":0,"raw_info_edge":3,"stage2_actionable_bonus_before":2.0,"stage2_actionable_bonus_after":0.0,"simulated_route":"DirectWorkoutStressControl_NotCleanAggregate"}
{"row_type":"score_simulation","symbol":"014790","raw_PF_refinancing_bridge":2,"raw_liquidity_survival_bridge":2,"raw_equity_value_bridge":1,"raw_cash_conversion":1,"raw_validation":2,"raw_info_edge":2,"stage2_actionable_bonus_before":2.0,"stage2_actionable_bonus_after":1.0,"simulated_route":"DelayedLocal4BPositive"}
{"row_type":"score_simulation","symbol":"004960","raw_PF_refinancing_bridge":1,"raw_liquidity_survival_bridge":2,"raw_equity_value_bridge":1,"raw_cash_conversion":1,"raw_validation":1,"raw_info_edge":1,"stage2_actionable_bonus_before":2.0,"stage2_actionable_bonus_after":1.0,"simulated_route":"Stage2WatchContributionCap"}
{"row_type":"score_simulation","symbol":"000720","raw_PF_refinancing_bridge":0,"raw_liquidity_survival_bridge":1,"raw_equity_value_bridge":0,"raw_cash_conversion":1,"raw_validation":0,"raw_info_edge":1,"stage2_actionable_bonus_before":2.0,"stage2_actionable_bonus_after":0.0,"simulated_route":"Stage2FalsePositiveBlock"}
```

---

## 7. Current calibrated profile stress test

### Existing error risk

C30 can over-reward:

```text
PF support headline
+ construction sector rebound
+ large-builder brand
```

That is too loose. PF stress is a pipe-pressure problem. The score should not praise a headline saying “water is coming” unless the pipe actually stops leaking: maturities roll, guarantees are reduced, bad projects are written down or sold, and cash flow can move without breaking the balance sheet.

### Rule candidate

```text
C30_DIRECT_WORKOUT_EQUITY_BRIDGE_GUARDRAIL

if C30
and direct_workout_or_debt_restructuring == true
and equity_value_bridge == false:
    stage2_actionable_bonus = 0
    max_stage = Stage2-Watch
    require_post_restructuring_shareholder_recovery_proof = true
```

```text
if C30
and trading_suspension_or_corporate_action_candidate_in_window == true:
    exclude_from_clean_aggregate = true
    use_as_stress_control_only = true
```

```text
if C30
and MFE_30D_pct < +5
and MFE_90D_pct >= +25
and issuer_specific_refinancing_or_liquidity_bridge_refreshed == true:
    route = delayed_local_4B_positive
    do_not_backfill_as_immediate_Stage2_Actionable = true
```

```text
if C30
and construction_support_or_large_builder_label == true
and issuer_specific_PF_refinancing_cash_bridge == false
and MFE_90D_pct < +10
and MAE_180D_pct <= -20:
    route = Stage2_FalsePositive_Block
    stage2_actionable_bonus = 0
```

---

## 8. Residual contribution summary

```yaml
do_not_propose_new_weight_delta: false
sector_specific_rule_candidate: false
canonical_archetype_rule_candidate: true
loop_contribution_label: canonical_archetype_rule_candidate
new_axis_proposed: C30_DIRECT_WORKOUT_EQUITY_BRIDGE_GUARDRAIL
existing_axis_strengthened:
  - C30_direct_workout_not_automatic_equity_recovery
  - C30_corporate_action_or_trading_gap_exclude_from_clean_aggregate
  - C30_delayed_4B_positive_requires_refinancing_liquidity_refresh
  - C30_large_builder_support_label_false_positive_block
existing_axis_weakened: null
```

---

## 9. Next recommended archetypes

```text
R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL
C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG
C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN_retest_with_securities_and_regional_bank_controls
C22_INSURANCE_RATE_CYCLE_RESERVE_retest_with_healthcare_GA_and_reinsurer_controls
R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW
```
