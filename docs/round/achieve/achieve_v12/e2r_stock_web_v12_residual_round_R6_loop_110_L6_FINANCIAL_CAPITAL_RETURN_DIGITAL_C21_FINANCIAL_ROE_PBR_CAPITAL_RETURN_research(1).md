# E2R v12 residual calibration research

## 0. Execution metadata

```yaml
schema_family: v12_sector_archetype_residual
selected_round: R6
selected_loop: 110
large_sector_id: L6_FINANCIAL_CAPITAL_RETURN_DIGITAL
canonical_archetype_id: C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN
fine_archetype_id: BANK_VALUEUP_CAPITAL_RETURN_EXECUTION_BRIDGE_VS_LOW_PBR_BANK_LABEL_WEAK_BRIDGE
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

`C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN` remains a low-coverage area in the no-repeat index: 6 rows / 5 symbols. The visible top-covered set is `323410`, `003530`, `024110`, `030610`, and `086790`. This loop avoids those and uses three bank-holding tuples:

- `105560 KB금융`
- `055550 신한지주`
- `316140 우리금융지주`

The repository registry shows prior C21 coverage through `R6/C21 loop 109`, so this run continues as `loop 110`.

---

## 1. Research thesis

C21 is not “low PBR finance stock.” It is the capital-efficiency bridge:

```text
low PBR / Korea Value-up pressure
→ ROE quality, CET1 headroom, credit-cost control
→ dividend / buyback / cancellation / payout policy execution
→ price path validation
```

The key distinction in this loop is execution quality.

1. **Large bank-holding capital-return execution bridge**  
   If the bank has strong ROE, enough CET1 headroom, and visible payout/buyback/cancellation execution, Stage2 can remain open even with macro drawdowns.

2. **Bank label / low PBR without enough incremental execution**  
   If the move is mainly sector beta or a low-PBR label, the model should cap Stage2 until capital return and credit-cost bridges are refreshed.

3. **High-MFE but high-MAE financial value-up path**  
   Bank stocks can re-rate and still draw down sharply. High MAE should not automatically hard-block the signal, but it must prevent Stage3-Green unless execution refresh is visible.

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
105560:
  name: KB금융
  corporate_action_candidate_count: 0
  calibration_caveat: clean

055550:
  name: 신한지주
  corporate_action_candidate_count: 0
  calibration_caveat: clean

316140:
  name: 우리금융지주
  corporate_action_candidate_count: 0
  calibration_caveat: clean
```

External macro anchor:

```text
2024-02-26: Korea Corporate Value-up Program announced to encourage listed companies to improve shareholder returns and capital efficiency.
2024-07-26 window: bank-holding value-up/capital-return execution retest after the initial Value-up trade had already become crowded.
```

---

## 3. Trigger rows

```jsonl
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","round":"R6","loop":110,"large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","fine_archetype_id":"KB_BANK_HOLDING_VALUEUP_CAPITAL_RETURN_EXECUTION_WITH_4B_WATCH","symbol":"105560","name":"KB금융","trigger_type":"Stage2-Actionable","entry_date":"2024-07-26","entry_close":87900,"price_basis":"tradable_raw","mfe_30d_pct":5.12,"mae_30d_pct":-15.81,"mfe_90d_pct":18.20,"mae_90d_pct":-15.81,"mfe_180d_pct":18.20,"mae_180d_pct":-15.81,"forward_high_30d":92400,"forward_low_30d":74000,"forward_high_90d":103900,"forward_low_90d":74000,"forward_high_180d":103900,"forward_low_180d":74000,"calibration_usable":true,"case_role":"positive_with_local_4B_watch","novelty_key":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN|105560|Stage2-Actionable|2024-07-26","non_price_bridge":"large bank holding ROE/PBR value-up and capital-return execution bridge","score_alignment":"Stage2 may stay open, but high MAE requires CET1/credit-cost/shareholder-return refresh before Green"}
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","round":"R6","loop":110,"large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","fine_archetype_id":"SHINHAN_CAPITAL_RETURN_EXECUTION_POSITIVE_WITH_HIGH_MAE_WATCH","symbol":"055550","name":"신한지주","trigger_type":"Stage2-Actionable","entry_date":"2024-07-26","entry_close":58000,"price_basis":"tradable_raw","mfe_30d_pct":11.38,"mae_30d_pct":-11.03,"mfe_90d_pct":11.38,"mae_90d_pct":-11.55,"mfe_180d_pct":11.38,"mae_180d_pct":-18.02,"forward_high_30d":64600,"forward_low_30d":51600,"forward_high_90d":64600,"forward_low_90d":51300,"forward_high_180d":64600,"forward_low_180d":47550,"calibration_usable":true,"case_role":"positive_with_4B_watch","novelty_key":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN|055550|Stage2-Actionable|2024-07-26","non_price_bridge":"bank holding value-up, ROE/PBR rerating and capital-return execution bridge","score_alignment":"Stage2 may open; 180D drawdown blocks Stage3-Green without renewed return/capital/credit-cost proof"}
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","round":"R6","loop":110,"large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","fine_archetype_id":"WOORI_LOW_PBR_BANK_LABEL_WEAK_INCREMENTAL_CAPITAL_RETURN_BRIDGE","symbol":"316140","name":"우리금융지주","trigger_type":"Stage2-Watch","entry_date":"2024-07-26","entry_close":16180,"price_basis":"tradable_raw","mfe_30d_pct":4.08,"mae_30d_pct":-15.08,"mfe_90d_pct":5.69,"mae_90d_pct":-15.08,"mfe_180d_pct":5.69,"mae_180d_pct":-15.08,"forward_high_30d":16840,"forward_low_30d":13740,"forward_high_90d":17100,"forward_low_90d":13740,"forward_high_180d":17100,"forward_low_180d":13740,"calibration_usable":true,"case_role":"weak_bridge_counterexample","novelty_key":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN|316140|Stage2-Watch|2024-07-26","non_price_bridge":"low-PBR bank label and value-up beta without enough incremental capital-return execution proof at trigger","score_alignment":"cap Stage2; require clear CET1/payout/credit-cost bridge before Actionable"}
```

---

## 4. Case analysis

### 4.1 KB Financial / 105560 — strongest bank-holding bridge, but not Green

KB is the best C21 bridge in this loop. From the July 26 retest entry, the stock drew down with the market in early August, then later made a new high around October. That is a valid capital-return/ROE/PBR repricing path, but not a clean Green because the 30D MAE was deep.

```yaml
entry_date: 2024-07-26
entry_close: 87900
30d_high: 92400
30d_low: 74000
90d_high: 103900
90d_low: 74000
180d_high: 103900
180d_low: 74000
mfe_30d_pct: 5.12
mae_30d_pct: -15.81
mfe_90d_pct: 18.20
mae_90d_pct: -15.81
```

Interpretation:

```text
classification = Stage2-Actionable with local_4B_watch
```

KB shows that C21 should not hard-block a major bank-holding return story merely because early MAE is high. But Stage3-Green must require refreshed shareholder-return execution, CET1 capacity and credit-cost stability.

---

### 4.2 Shinhan Financial / 055550 — positive, but weaker than KB

Shinhan also validates the bank capital-return bridge, but with a smaller forward MFE and deeper 180D drift. The 30D/90D high reached 64,600, while 180D low reached 47,550.

```yaml
entry_date: 2024-07-26
entry_close: 58000
30d_high: 64600
30d_low: 51600
90d_high: 64600
90d_low: 51300
180d_high: 64600
180d_low: 47550
mfe_90d_pct: 11.38
mae_90d_pct: -11.55
mfe_180d_pct: 11.38
mae_180d_pct: -18.02
```

Interpretation:

```text
classification = Stage2-Actionable with 4B watch
```

This keeps C21 open but makes the bridge narrower. A bank value-up signal should be refreshed by actual payout, buyback/cancellation, CET1 headroom and credit-cost control before any Green transition.

---

### 4.3 Woori Financial / 316140 — low-PBR label is not enough

Woori is the weak-bridge counterexample. It participated in the bank value-up trade but had limited forward MFE from this entry date.

```yaml
entry_date: 2024-07-26
entry_close: 16180
30d_high: 16840
30d_low: 13740
90d_high: 17100
90d_low: 13740
180d_high: 17100
180d_low: 13740
mfe_90d_pct: 5.69
mae_90d_pct: -15.08
```

Interpretation:

```text
classification = Stage2-Watch / weak bridge cap
```

This case says C21 must not reward “bank + low PBR” equally across all names. If the incremental capital-return bridge is weak and MFE stays below 10%, Stage2-Actionable should be blocked until better evidence appears.

---

## 5. Score-return alignment

```yaml
new_independent_case_count: 3
new_visible_C21_symbol_count: 3
same_archetype_new_trigger_family_count: 3
calibration_usable_case_count: 3
calibration_usable_trigger_count: 3
positive_case_count: 2
counterexample_or_cap_count: 1
current_profile_error_count: 2
```

| symbol | role | 30D MFE/MAE | 90D MFE/MAE | 180D MFE/MAE | lesson |
|---|---:|---:|---:|---:|---|
| 105560 | positive + 4B watch | +5.12 / -15.81 | +18.20 / -15.81 | +18.20 / -15.81 | strong bank-holding bridge, but high MAE blocks Green |
| 055550 | positive + 4B watch | +11.38 / -11.03 | +11.38 / -11.55 | +11.38 / -18.02 | capital-return bridge works, but needs refresh |
| 316140 | weak-bridge cap | +4.08 / -15.08 | +5.69 / -15.08 | +5.69 / -15.08 | low-PBR bank label alone is not enough |

---

## 6. Raw component score breakdown

```jsonl
{"row_type":"score_simulation","symbol":"105560","raw_ROE_quality":4,"raw_PBR_mispricing":4,"raw_CET1_headroom":4,"raw_capital_return_execution":4,"raw_credit_cost_control":3,"raw_validation":3,"raw_info_edge":2,"stage2_actionable_bonus_before":2.0,"stage2_actionable_bonus_after":2.0,"simulated_route":"Stage2-Actionable-with-local-4B-watch"}
{"row_type":"score_simulation","symbol":"055550","raw_ROE_quality":3,"raw_PBR_mispricing":4,"raw_CET1_headroom":3,"raw_capital_return_execution":3,"raw_credit_cost_control":3,"raw_validation":2,"raw_info_edge":2,"stage2_actionable_bonus_before":2.0,"stage2_actionable_bonus_after":2.0,"simulated_route":"Stage2-Actionable-with-4B-watch"}
{"row_type":"score_simulation","symbol":"316140","raw_ROE_quality":2,"raw_PBR_mispricing":4,"raw_CET1_headroom":2,"raw_capital_return_execution":1,"raw_credit_cost_control":2,"raw_validation":1,"raw_info_edge":1,"stage2_actionable_bonus_before":2.0,"stage2_actionable_bonus_after":0.0,"simulated_route":"Stage2-Watch-weak-capital-return-bridge"}
```

---

## 7. Current calibrated profile stress test

### Existing error risk

C21 can over-reward:

```text
bank stock
+ low PBR
+ Korea Value-up headline
```

That is too broad. A bank’s capital-return story is not just a low price-to-book sticker. It is a hydraulic system: ROE creates pressure, CET1 sets the safety valve, credit cost measures leakage, and buybacks/dividends are the flow that reaches shareholders.

### Rule candidate

```text
C21_BANK_VALUEUP_CAPITAL_RETURN_EXECUTION_REQUIREMENT

if C21
and low_PBR_bank_or_financial_label == true
and ROE_quality_CET1_headroom_capital_return_execution_bridge == false:
    stage2_actionable_bonus = 0
    max_stage = Stage2-Watch
```

```text
if C21
and bank_holding_capital_return_execution == true
and MFE_90D_pct >= +10
and MAE_90D_pct <= -15:
    keep_stage2_actionable_bonus = true
    local_4B_watch = true
    block_stage3_green_until_return_CET1_credit_cost_refresh = true
```

```text
if C21
and MFE_90D_pct < +10
and low_PBR_or_valueup_label == true
and incremental_capital_return_bridge == false:
    stage2_actionable_bonus = 0
    route = Stage2-Watch_or_FalsePositive_Block
```

```text
if C21
and bank_valueup_repricing == true
and credit_cost_or_regulatory_capital_headwind == true:
    cap_stage3_green = true
    require_next_quarter_capital_return_execution_refresh = true
```

---

## 8. Residual contribution summary

```yaml
do_not_propose_new_weight_delta: false
sector_specific_rule_candidate: false
canonical_archetype_rule_candidate: true
loop_contribution_label: canonical_archetype_rule_candidate
new_axis_proposed: C21_BANK_VALUEUP_CAPITAL_RETURN_EXECUTION_REQUIREMENT
existing_axis_strengthened:
  - C21_low_PBR_label_not_enough_without_capital_return_execution
  - C21_CET1_ROE_credit_cost_bridge_required
  - C21_bank_holding_positive_with_4B_watch_after_high_MAE
  - C21_weak_bank_valueup_bridge_stage2_cap
existing_axis_weakened: null
```

---

## 9. Next recommended archetypes

```text
C22_INSURANCE_RATE_CYCLE_RESERVE
C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK_retest_with_direct_workout_controls
R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL
C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG
C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN_retest_with_securities_and_regional_bank_controls
```
