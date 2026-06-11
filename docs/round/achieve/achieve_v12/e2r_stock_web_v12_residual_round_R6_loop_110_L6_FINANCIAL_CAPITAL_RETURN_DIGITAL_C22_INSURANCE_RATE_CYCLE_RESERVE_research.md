# E2R v12 residual calibration research

## 0. Execution metadata

```yaml
schema_family: v12_sector_archetype_residual
selected_round: R6
selected_loop: 110
large_sector_id: L6_FINANCIAL_CAPITAL_RETURN_DIGITAL
canonical_archetype_id: C22_INSURANCE_RATE_CYCLE_RESERVE
fine_archetype_id: GA_DISTRIBUTION_COMMISSION_BRIDGE_VS_REINSURANCE_RATE_CYCLE_RESERVE_CONTROL
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

`C22_INSURANCE_RATE_CYCLE_RESERVE` remains thin in the no-repeat index: 6 rows / 6 symbols. The visible covered set is `000540`, `000810`, `001450`, `003690`, `085620`, and `138930`. The prior local C22 run reached loop 109 with nonlife/life-insurer value-up controls; this run therefore continues as `loop 110` and shifts the fine axis into insurance distribution / GA and reinsurance.

Selected tuples:

- `244920 에이플러스에셋` — GA / insurance distribution commission bridge.
- `211050 인카금융서비스` — GA / insurance distribution high-MFE but corporate-action-adjacent and high-MAE watch.
- `003690 코리안리` — reinsurance rate-cycle/reserve control; visible-covered symbol, so used as control rather than new clean coverage.

---

## 1. Research thesis

C22 should not score every insurance-adjacent listed company in the same way.

```text
insurance rate cycle / reserve quality / solvency / loss ratio / reinsurance pricing
→ capital-return or book-value confidence
→ price path validation
```

GA / 보험판매 companies have a different economic machine:

```text
insurance product demand / agent productivity / commission revenue
→ operating leverage and cash conversion
→ price path
```

That can be tradable, but it is not the same as reserve quality or solvency capital. The C22 model should therefore split:

1. **Reinsurer / balance-sheet insurance bridge**  
   Keep C22 credit when rate-cycle, reserve discipline, underwriting risk and capital are the actual drivers.

2. **GA distribution high-MFE path**  
   Allow a watch bucket for commission-driven insurance distribution, but cap C22 contribution unless reserve/solvency economics are truly involved.

3. **GA label with low-MFE or post-corporate-action volatility**  
   Do not award Stage2-Actionable simply because the name sits near insurance. Commission economics belong in a distribution/financial-services sub-axis unless price path and accounting bridge are refreshed.

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
244920:
  name: 에이플러스에셋
  corporate_action_candidate_count: 0
  calibration_caveat: clean

211050:
  name: 인카금융서비스
  corporate_action_candidate_dates: [2018-07-18, 2022-06-22, 2022-07-13, 2024-04-29]
  relevant_window_after_candidate: true
  caveat: 2024-04-29 split/corporate-action candidate; use post-candidate rows only and mark 4B watch.

003690:
  name: 코리안리
  visible_in_no_repeat_index: true
  role: reused_reinsurance_control
```

External macro anchor:

```text
2024-02-26 / 2024-02-28: Korea Corporate Value-up Programme disappointment and follow-up pressure window.
C22 insurance scoring must separate shareholder-return/value-up beta from actual reserve, solvency and reinsurance pricing bridge.
```

---

## 3. Trigger rows

```jsonl
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","round":"R6","loop":110,"large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","fine_archetype_id":"GA_INSURANCE_DISTRIBUTION_COMMISSION_BRIDGE_MODEST_MFE_STAGE2_CAP","symbol":"244920","name":"에이플러스에셋","trigger_type":"Stage2-Watch","entry_date":"2024-05-10","entry_close":4100,"price_basis":"tradable_raw","mfe_30d_pct":9.76,"mae_30d_pct":-2.32,"mfe_90d_pct":9.76,"mae_90d_pct":-13.78,"mfe_180d_pct":14.63,"mae_180d_pct":-13.78,"forward_high_30d":4500,"forward_low_30d":4005,"forward_high_90d":4500,"forward_low_90d":3535,"forward_high_180d":4700,"forward_low_180d":3535,"calibration_usable":true,"case_role":"GA_distribution_stage2_cap","novelty_key":"C22_INSURANCE_RATE_CYCLE_RESERVE|244920|Stage2-Watch|2024-05-10","non_price_bridge":"insurance distribution / GA commission revenue bridge, not reserve-quality or solvency bridge","score_alignment":"cap C22 Stage2; require commission growth and cash conversion bridge or reclassify out of C22"}
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","round":"R6","loop":110,"large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","fine_archetype_id":"GA_DISTRIBUTION_HIGH_MFE_HIGH_MAE_POST_SPLIT_4B_WATCH","symbol":"211050","name":"인카금융서비스","trigger_type":"Stage2-Watch","entry_date":"2024-05-02","entry_close":4925,"price_basis":"tradable_raw","mfe_30d_pct":31.57,"mae_30d_pct":-4.57,"mfe_90d_pct":31.57,"mae_90d_pct":-16.35,"mfe_180d_pct":31.57,"mae_180d_pct":-16.35,"forward_high_30d":6480,"forward_low_30d":4700,"forward_high_90d":6480,"forward_low_90d":4120,"forward_high_180d":6480,"forward_low_180d":4120,"calibration_usable":true,"case_role":"GA_distribution_high_MFE_4B_watch","novelty_key":"C22_INSURANCE_RATE_CYCLE_RESERVE|211050|Stage2-Watch|2024-05-02","non_price_bridge":"GA distribution/commission platform after 2024-04-29 corporate-action candidate; high MFE but high MAE and no reserve/solvency bridge","score_alignment":"local 4B watch; do not grant C22 Green without distribution cash bridge and reclassification"}
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","round":"R6","loop":110,"large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","fine_archetype_id":"REINSURANCE_RATE_CYCLE_RESERVE_LOW_VOL_CONTROL","symbol":"003690","name":"코리안리","trigger_type":"Stage2-Watch","entry_date":"2024-02-26","entry_close":7930,"price_basis":"tradable_raw","mfe_30d_pct":6.81,"mae_30d_pct":-1.01,"mfe_90d_pct":6.81,"mae_90d_pct":-5.42,"mfe_180d_pct":13.49,"mae_180d_pct":-5.42,"forward_high_30d":8470,"forward_low_30d":7850,"forward_high_90d":8470,"forward_low_90d":7500,"forward_high_180d":9000,"forward_low_180d":7500,"calibration_usable":true,"case_role":"reused_reinsurance_control","novelty_key":"C22_INSURANCE_RATE_CYCLE_RESERVE|003690|Stage2-Watch|2024-02-26","non_price_bridge":"reinsurance pricing / reserve / underwriting cycle control; visible-covered symbol in index","score_alignment":"keep as control; low-volatility positive but not a new high-conviction Stage2-Actionable trigger"}
```

---

## 4. Case analysis

### 4.1 A Plus Asset / 244920 — GA distribution is not reserve quality

`에이플러스에셋` is a clean-price-window GA/distribution case. It is useful precisely because it shows the boundary. The stock moved modestly after the 2024-05-10 trigger, but the move was not enough to call this a C22 reserve/rate-cycle validation.

```yaml
entry_date: 2024-05-10
entry_close: 4100
30d_high: 4500
30d_low: 4005
90d_high: 4500
90d_low: 3535
180d_high: 4700
180d_low: 3535
mfe_90d_pct: 9.76
mae_90d_pct: -13.78
```

Interpretation:

```text
classification = Stage2-Watch / GA distribution cap
```

The model should not confuse an insurance sales channel with an insurance balance sheet. GA economics can be real, but they are commission and productivity economics, not reserve adequacy or rate-cycle economics.

---

### 4.2 INCA Financial Service / 211050 — high MFE, but post-split 4B watch

`인카금융서비스` is more volatile and more interesting. The 2024-04-29 corporate-action candidate means the cleanest usable entry is the post-candidate window. From 2024-05-02, the stock reached 6,480 quickly, then later printed 4,120 in August.

```yaml
entry_date: 2024-05-02
entry_close: 4925
30d_high: 6480
30d_low: 4700
90d_high: 6480
90d_low: 4120
180d_high: 6480
180d_low: 4120
mfe_30d_pct: 31.57
mae_90d_pct: -16.35
```

Interpretation:

```text
classification = local 4B watch / reclassify unless commission-cash bridge is refreshed
```

The price response was real. But it is still not a reserve/solvency C22 bridge. If this signal is retained, it belongs under insurance distribution commission economics, not under classic C22 rate-cycle/reserve quality.

---

### 4.3 Korean Re / 003690 — reinsurer control, low-volatility C22 anchor

`코리안리` is the clean reinsurance control. It is already a visible-covered C22 symbol in the index, so it should not receive new independent coverage credit. Still, it anchors what C22 should look like when the economic bridge is closer to reinsurance rate/reserve/underwriting economics.

```yaml
entry_date: 2024-02-26
entry_close: 7930
30d_high: 8470
30d_low: 7850
90d_high: 8470
90d_low: 7500
180d_high: 9000
180d_low: 7500
mfe_180d_pct: 13.49
mae_180d_pct: -5.42
```

Interpretation:

```text
classification = reused reinsurance control / Stage2-Watch
```

This is not explosive, but it is economically cleaner than GA distribution for C22. Reinsurance is closer to the balance-sheet and underwriting cycle that this archetype is trying to calibrate.

---

## 5. Score-return alignment

```yaml
new_independent_case_count: 2
reused_control_case_count: 1
new_visible_C22_symbol_count: 2
same_archetype_new_trigger_family_count: 3
calibration_usable_case_count: 3
calibration_usable_trigger_count: 3
positive_or_watch_case_count: 2
counterexample_or_cap_count: 2
current_profile_error_count: 2
```

| symbol | role | 30D MFE/MAE | 90D MFE/MAE | 180D MFE/MAE | lesson |
|---|---:|---:|---:|---:|---|
| 244920 | GA distribution cap | +9.76 / -2.32 | +9.76 / -13.78 | +14.63 / -13.78 | insurance sales channel is not reserve-quality bridge |
| 211050 | GA high-MFE 4B watch | +31.57 / -4.57 | +31.57 / -16.35 | +31.57 / -16.35 | price works, but post-split and non-reserve bridge need reclassification |
| 003690 | reused reinsurance control | +6.81 / -1.01 | +6.81 / -5.42 | +13.49 / -5.42 | cleaner C22 bridge but low MFE; use as control |

---

## 6. Raw component score breakdown

```jsonl
{"row_type":"score_simulation","symbol":"244920","raw_reserve_quality":0,"raw_loss_ratio_quality":0,"raw_rate_cycle_support":1,"raw_solvency_capital":0,"raw_commission_distribution_bridge":3,"raw_capital_return_execution":1,"raw_validation":1,"raw_info_edge":1,"stage2_actionable_bonus_before":2.0,"stage2_actionable_bonus_after":0.0,"simulated_route":"Stage2-Watch-GA-distribution-cap"}
{"row_type":"score_simulation","symbol":"211050","raw_reserve_quality":0,"raw_loss_ratio_quality":0,"raw_rate_cycle_support":1,"raw_solvency_capital":0,"raw_commission_distribution_bridge":4,"raw_capital_return_execution":1,"raw_validation":2,"raw_info_edge":2,"stage2_actionable_bonus_before":2.0,"stage2_actionable_bonus_after":1.0,"simulated_route":"Local4B-GA-distribution-reclassify"}
{"row_type":"score_simulation","symbol":"003690","raw_reserve_quality":3,"raw_loss_ratio_quality":2,"raw_rate_cycle_support":3,"raw_solvency_capital":3,"raw_commission_distribution_bridge":0,"raw_capital_return_execution":2,"raw_validation":2,"raw_info_edge":1,"stage2_actionable_bonus_before":2.0,"stage2_actionable_bonus_after":1.0,"simulated_route":"Reinsurance-control-Stage2-Watch"}
```

---

## 7. Current calibrated profile stress test

### Existing error risk

C22 can over-reward:

```text
insurance-adjacent company
+ Value-up / financial beta
+ price spike
```

That is too broad. Insurance balance sheets are reservoirs: reserves, solvency, reinsurance pricing, loss ratios and capital return determine whether the reservoir holds. GA companies are distribution pipes: they can carry commission flow, but they do not prove the reservoir is sound.

### Rule candidate

```text
C22_GA_DISTRIBUTION_RECLASSIFICATION_GUARDRAIL

if C22
and insurance_distribution_or_GA_label == true
and reserve_quality_solvency_rate_cycle_bridge == false:
    stage2_actionable_bonus = 0
    max_stage = Stage2-Watch
    require_reclassification_to_distribution_commission_axis = true
```

```text
if C22
and GA_distribution_commission_bridge == true
and MFE_30D_pct >= +25
and MAE_90D_pct <= -15:
    local_4B_watch = true
    block_stage3_green_for_C22 = true
    require_commission_cash_conversion_refresh = true
```

```text
if C22
and reinsurance_rate_cycle_reserve_bridge == true
and MFE_180D_pct >= +10
and MAE_180D_pct > -10:
    keep_stage2_watch_or_actionable = true
    use_as_low_vol_control = true
```

```text
if C22
and MFE_90D_pct < +10
and reserve_solvency_capital_bridge == false:
    stage2_actionable_bonus = 0
    route = Stage2-Watch_or_FalsePositive_Block
```

---

## 8. Residual contribution summary

```yaml
do_not_propose_new_weight_delta: false
sector_specific_rule_candidate: false
canonical_archetype_rule_candidate: true
loop_contribution_label: canonical_archetype_rule_candidate
new_axis_proposed: C22_GA_DISTRIBUTION_RECLASSIFICATION_GUARDRAIL
existing_axis_strengthened:
  - C22_insurance_label_not_enough_without_reserve_solvency_bridge
  - C22_GA_distribution_commission_bridge_is_not_reserve_cycle
  - C22_reinsurance_rate_cycle_low_vol_control
  - C22_high_MFE_GA_distribution_local_4B_reclassification
existing_axis_weakened: null
```

---

## 9. Next recommended archetypes

```text
R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW
C31_POLICY_SUBSIDY_LEGISLATION_EVENT
C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG
C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN_retest_with_digital_financial_and_brokerage_counterexamples
C22_INSURANCE_RATE_CYCLE_RESERVE_retest_with_healthcare_underwriting_controls
```
