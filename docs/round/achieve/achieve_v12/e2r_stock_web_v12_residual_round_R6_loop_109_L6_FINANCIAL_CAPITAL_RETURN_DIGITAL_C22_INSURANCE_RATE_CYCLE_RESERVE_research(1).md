# E2R v12 residual calibration research

## 0. Execution metadata

```yaml
schema_family: v12_sector_archetype_residual
selected_round: R6
selected_loop: 109
large_sector_id: L6_FINANCIAL_CAPITAL_RETURN_DIGITAL
canonical_archetype_id: C22_INSURANCE_RATE_CYCLE_RESERVE
fine_archetype_id: NONLIFE_RESERVE_QUALITY_CAPITAL_RETURN_BRIDGE_VS_LIFE_INSURANCE_VALUEUP_LABEL_WEAK_BRIDGE
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

`C22_INSURANCE_RATE_CYCLE_RESERVE` was selected because the no-repeat index still marks it as thin: 6 rows / 6 symbols. The visible covered set is `000540`, `000810`, `001450`, `003690`, `085620`, and `138930`, so this loop avoids those and uses new C22 tuples:

- `005830 DB손해보험`
- `032830 삼성생명`
- `088350 한화생명`

The repository registry shows C22 runs through `R6/C22 loop 108`, so this run continues as `R6/C22 loop 109`.

---

## 1. Research thesis

C22 is not simply “insurance stock.” It is the bridge:

```text
rate cycle / reserve quality / loss ratio / solvency capital
→ capital-return or book-value confidence
→ shareholder return and price validation
```

The core split in this loop is:

1. **Nonlife/P&C reserve and loss-ratio quality bridge**  
   If underwriting quality, reserve confidence and capital return line up, C22 can remain Stage2-Actionable even after drawdowns.

2. **Large life-insurer capital-policy bridge**  
   A life insurer can work as C22 if solvency and capital-return visibility are strong, but it should not be promoted to Green unless the value-up rally is supported by reserve/capital economics.

3. **Life-insurance value-up label without enough incremental bridge**  
   A life-insurance label can spike on value-up beta, then fail to generate enough forward MFE. This should be capped.

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
005830:
  name: DB손해보험
  corporate_action_candidate_dates: [1999-07-20]
  relevant_window_after_candidate: true

032830:
  name: 삼성생명
  corporate_action_candidate_count: 0
  calibration_caveat: clean

088350:
  name: 한화생명
  corporate_action_candidate_count: 0
  calibration_caveat: clean
```

External macro anchor:

```text
2024-02-26: Korea Corporate Value-up Programme announcement window.
2024-02-28 and 2024-03-14 Reuters follow-up: regulators discussed stronger measures and faster follow-up/tax support after the initial package disappointed markets.
```

---

## 3. Trigger rows

```jsonl
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","round":"R6","loop":109,"large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","fine_archetype_id":"NONLIFE_RESERVE_LOSS_RATIO_CAPITAL_RETURN_POSITIVE_WITH_4B_WATCH","symbol":"005830","name":"DB손해보험","trigger_type":"Stage2-Actionable","entry_date":"2024-02-26","entry_close":95000,"price_basis":"tradable_raw","mfe_30d_pct":15.79,"mae_30d_pct":-4.11,"mfe_90d_pct":27.05,"mae_90d_pct":-9.26,"mfe_180d_pct":30.53,"mae_180d_pct":-9.26,"forward_high_30d":110000,"forward_low_30d":91100,"forward_high_90d":120700,"forward_low_90d":86200,"forward_high_180d":124000,"forward_low_180d":86200,"calibration_usable":true,"case_role":"positive_control","novelty_key":"C22_INSURANCE_RATE_CYCLE_RESERVE|005830|Stage2-Actionable|2024-02-26","non_price_bridge":"nonlife reserve quality / loss-ratio confidence / value-up capital-return bridge","score_alignment":"keep Stage2-Actionable; allow Stage3-Yellow path if reserve quality, solvency and payout execution are refreshed"}
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","round":"R6","loop":109,"large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","fine_archetype_id":"LIFE_INSURER_CAPITAL_POLICY_POSITIVE_WITH_RESERVE_SOLVENCY_REFRESH_REQUIREMENT","symbol":"032830","name":"삼성생명","trigger_type":"Stage2-Actionable","entry_date":"2024-02-26","entry_close":92200,"price_basis":"tradable_raw","mfe_30d_pct":17.68,"mae_30d_pct":-5.10,"mfe_90d_pct":17.68,"mae_90d_pct":-5.10,"mfe_180d_pct":17.68,"mae_180d_pct":-10.85,"forward_high_30d":108500,"forward_low_30d":87500,"forward_high_90d":108500,"forward_low_90d":87500,"forward_high_180d":108500,"forward_low_180d":82200,"calibration_usable":true,"case_role":"positive_with_4B_watch","novelty_key":"C22_INSURANCE_RATE_CYCLE_RESERVE|032830|Stage2-Actionable|2024-02-26","non_price_bridge":"large life-insurer value-up / solvency capital / shareholder-return expectation bridge","score_alignment":"Stage2 may open, but Green requires reserve, CSM, solvency and capital policy refresh"}
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","round":"R6","loop":109,"large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","fine_archetype_id":"LIFE_INSURANCE_VALUEUP_LABEL_LOW_MFE_STAGE2_CAP","symbol":"088350","name":"한화생명","trigger_type":"Stage2-Watch","entry_date":"2024-02-26","entry_close":3060,"price_basis":"tradable_raw","mfe_30d_pct":9.31,"mae_30d_pct":-8.17,"mfe_90d_pct":9.31,"mae_90d_pct":-15.69,"mfe_180d_pct":9.31,"mae_180d_pct":-15.69,"forward_high_30d":3345,"forward_low_30d":2810,"forward_high_90d":3345,"forward_low_90d":2580,"forward_high_180d":3345,"forward_low_180d":2580,"calibration_usable":true,"case_role":"weak_bridge_counterexample","novelty_key":"C22_INSURANCE_RATE_CYCLE_RESERVE|088350|Stage2-Watch|2024-02-26","non_price_bridge":"life-insurance value-up label without enough post-trigger incremental reserve/capital-return validation","score_alignment":"cap Stage2; require solvency, reserve-quality and payout bridge before Actionable"}
```

---

## 4. Case analysis

### 4.1 DB Insurance / 005830 — nonlife reserve-quality positive-control

DB Insurance is the clean C22 positive-control. From the 2024-02-26 value-up anchor, the stock first reached 110,000 in March, then 120,700 in July, and later 124,000 in August.

```yaml
entry_date: 2024-02-26
entry_close: 95000
30d_high: 110000
30d_low: 91100
90d_high: 120700
90d_low: 86200
180d_high: 124000
180d_low: 86200
mfe_30d_pct: 15.79
mae_30d_pct: -4.11
mfe_90d_pct: 27.05
mae_90d_pct: -9.26
mfe_180d_pct: 30.53
mae_180d_pct: -9.26
```

Interpretation:

```text
classification = Stage2-Actionable positive-control
```

The lesson is that C22 should reward nonlife insurers when the price path confirms reserve/loss-ratio quality and capital-return confidence. The drawdown stayed under -10%, so this is a stronger escape hatch than the bank C21 high-MAE cases.

---

### 4.2 Samsung Life / 032830 — life-insurer positive, but reserve/solvency refresh required

Samsung Life worked as a C22 value-up/life-insurance positive, but the mechanism is different from nonlife. The stock made a strong early move after the anchor date, but the later low in August shows that the signal still needs reserve, CSM, solvency and capital-return refresh.

```yaml
entry_date: 2024-02-26
entry_close: 92200
30d_high: 108500
30d_low: 87500
90d_high: 108500
90d_low: 87500
180d_high: 108500
180d_low: 82200
mfe_30d_pct: 17.68
mae_30d_pct: -5.10
mfe_180d_pct: 17.68
mae_180d_pct: -10.85
```

Interpretation:

```text
classification = Stage2-Actionable with 4B watch
```

The model should keep Stage2 open but not treat a life-insurance value-up rally as a clean Green until the reserve/solvency and capital-policy bridge is explicit.

---

### 4.3 Hanwha Life / 088350 — life-insurance value-up label cap

Hanwha Life is the weak-bridge counterexample. It had already spiked before the value-up anchor, and after 2024-02-26 its forward MFE stayed below +10% while MAE deepened below -15%.

```yaml
entry_date: 2024-02-26
entry_close: 3060
30d_high: 3345
30d_low: 2810
90d_high: 3345
90d_low: 2580
180d_high: 3345
180d_low: 2580
mfe_90d_pct: 9.31
mae_90d_pct: -15.69
```

Interpretation:

```text
classification = Stage2-Watch / weak bridge cap
```

This is the guardrail: a life-insurance label and value-up beta are not enough. C22 must require post-trigger reserve-quality, solvency, CSM, payout or capital-return execution evidence.

---

## 5. Score-return alignment

```yaml
new_independent_case_count: 3
new_visible_C22_symbol_count: 3
same_archetype_new_trigger_family_count: 3
calibration_usable_case_count: 3
calibration_usable_trigger_count: 3
positive_case_count: 2
counterexample_or_cap_count: 1
current_profile_error_count: 2
```

| symbol | role | 30D MFE/MAE | 90D MFE/MAE | 180D MFE/MAE | lesson |
|---|---:|---:|---:|---:|---|
| 005830 | nonlife positive-control | +15.79 / -4.11 | +27.05 / -9.26 | +30.53 / -9.26 | reserve/loss-ratio quality bridge validated |
| 032830 | life positive + 4B watch | +17.68 / -5.10 | +17.68 / -5.10 | +17.68 / -10.85 | life-insurer value-up works, but needs solvency/reserve refresh |
| 088350 | weak-bridge cap | +9.31 / -8.17 | +9.31 / -15.69 | +9.31 / -15.69 | life-insurance label alone is not enough |

---

## 6. Raw component score breakdown

```jsonl
{"row_type":"score_simulation","symbol":"005830","raw_reserve_quality":4,"raw_loss_ratio_quality":4,"raw_rate_cycle_support":3,"raw_solvency_capital":3,"raw_capital_return_execution":3,"raw_validation":4,"raw_info_edge":2,"stage2_actionable_bonus_before":2.0,"stage2_actionable_bonus_after":2.0,"simulated_route":"Stage2-Actionable-positive-control"}
{"row_type":"score_simulation","symbol":"032830","raw_reserve_quality":3,"raw_loss_ratio_quality":1,"raw_rate_cycle_support":3,"raw_solvency_capital":4,"raw_capital_return_execution":2,"raw_validation":3,"raw_info_edge":2,"stage2_actionable_bonus_before":2.0,"stage2_actionable_bonus_after":2.0,"simulated_route":"Stage2-Actionable-with-4B-watch"}
{"row_type":"score_simulation","symbol":"088350","raw_reserve_quality":1,"raw_loss_ratio_quality":0,"raw_rate_cycle_support":2,"raw_solvency_capital":2,"raw_capital_return_execution":1,"raw_validation":1,"raw_info_edge":1,"stage2_actionable_bonus_before":2.0,"stage2_actionable_bonus_after":0.0,"simulated_route":"Stage2-Watch-weak-life-insurance-label"}
```

---

## 7. Current calibrated profile stress test

### Existing error risk

C22 can over-reward:

```text
insurance stock
+ low PBR / Value-up label
+ short-window sector beta
```

That is too broad. Insurance is a balance sheet with promises inside it. The price signal should ask whether those promises are funded, reserved and priced correctly. Nonlife insurers need loss-ratio and reserve discipline. Life insurers need solvency, CSM, capital policy and liability-rate sensitivity.

### Rule candidate

```text
C22_INSURANCE_RESERVE_CAPITAL_BRIDGE_REQUIREMENT

if C22
and insurance_or_valueup_label == true
and reserve_quality_solvency_capital_return_bridge == false:
    stage2_actionable_bonus = 0
    max_stage = Stage2-Watch
```

```text
if C22
and nonlife_loss_ratio_reserve_quality_bridge == true
and MFE_90D_pct >= +20
and MAE_90D_pct > -10:
    keep_stage2_actionable_bonus = true
    allow_stage3_yellow_path = true
```

```text
if C22
and life_insurance_valueup_label == true
and MFE_90D_pct < +10
and reserve_solvency_capital_policy_refresh == false:
    stage2_actionable_bonus = 0
    route = Stage2-Watch_or_FalsePositive_Block
```

```text
if C22
and life_insurance_valueup_bridge == true
and MAE_180D_pct <= -10:
    local_4B_watch = true
    block_stage3_green_until_CSM_solvency_capital_return_refresh = true
```

---

## 8. Residual contribution summary

```yaml
do_not_propose_new_weight_delta: false
sector_specific_rule_candidate: false
canonical_archetype_rule_candidate: true
loop_contribution_label: canonical_archetype_rule_candidate
new_axis_proposed: C22_INSURANCE_RESERVE_CAPITAL_BRIDGE_REQUIREMENT
existing_axis_strengthened:
  - C22_insurance_label_not_enough_without_reserve_solvency_bridge
  - C22_nonlife_loss_ratio_reserve_quality_positive_escape_hatch
  - C22_life_insurance_valueup_positive_with_4B_watch
  - C22_life_insurance_low_MFE_stage2_cap
existing_axis_weakened: null
```

---

## 9. Next recommended archetypes

```text
C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK_retest_with_direct_workout_controls
R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL
C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG
C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN_retest_with_securities_and_regional_bank_controls
C22_INSURANCE_RATE_CYCLE_RESERVE_retest_with_healthcare_GA_and_reinsurer_controls
```
