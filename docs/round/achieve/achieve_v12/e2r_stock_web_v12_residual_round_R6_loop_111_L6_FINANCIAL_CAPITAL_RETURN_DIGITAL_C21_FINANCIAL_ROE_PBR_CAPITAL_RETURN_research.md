# E2R v12 residual calibration research

## 0. Execution metadata

```yaml
schema_family: v12_sector_archetype_residual
selected_round: R6
selected_loop: 111
large_sector_id: L6_FINANCIAL_CAPITAL_RETURN_DIGITAL
canonical_archetype_id: C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN
fine_archetype_id: SECURITIES_ROE_PBR_BROKERAGE_FLOW_CAPITAL_RETURN_BRIDGE_VS_LOW_PBR_BROKERAGE_LABEL_WEAK_BRIDGE
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

`C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN` remains a low-coverage area in the no-repeat index. The prior local C21 run used bank-holding cases, so this loop deliberately changes the fine axis into securities / brokerage capital-efficiency names. The goal is to avoid learning the same “bank + low PBR + Value-up” pattern again.

Selected tuples:

- `005940 NH투자증권`
- `016360 삼성증권`
- `006800 미래에셋증권`

The repository registry shows parsed C21 runs up to `R6/C21 loop 109`, and the previous local execution completed `loop 110`; this run continues as `loop 111`.

---

## 1. Research thesis

C21 is not just “financial stock with low PBR.” For securities companies, the bridge is different from banks.

```text
brokerage flow / IB pipeline / market turnover / wealth management
→ ROE recovery and earnings quality
→ dividend or buyback/cancellation policy
→ price path validation
```

The securities sub-axis therefore needs its own guardrail.

- **High-quality capital-return brokerage bridge:** brokerage flow, IB recovery and shareholder-return execution can create a durable C21 path.
- **Securities value-up beta with high MAE:** a stock can show strong MFE and still need local 4B if earnings/turnover/IB bridge is cyclical.
- **Low-PBR brokerage label without incremental ROE bridge:** if MFE remains low and MAE expands, Stage2-Actionable should be blocked.

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
005940:
  name: NH투자증권
  corporate_action_candidate_dates: [1999-04-14, 1999-11-01, 2000-01-31, 2011-12-08, 2015-01-20]
  relevant_window_after_candidate: true

016360:
  name: 삼성증권
  corporate_action_candidate_dates: [1997-03-29, 1998-06-12, 1999-04-15, 1999-08-10, 1999-12-09, 2001-07-10]
  relevant_window_after_candidate: true

006800:
  name: 미래에셋증권
  corporate_action_candidate_dates: [1999-09-27, 1999-10-14, 2000-05-22, 2001-11-23, 2011-11-16, 2017-01-20]
  relevant_window_after_candidate: true
```

External macro anchor:

```text
2024-02-26 / 2024-02-28: Korea Corporate Value-up Programme disappointment and follow-up pressure window.
The same macro headline supported low-PBR financials, but securities-company scoring must require ROE/flow/IB/capital-return execution rather than low-PBR label alone.
```

---

## 3. Trigger rows

```jsonl
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","round":"R6","loop":111,"large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","fine_archetype_id":"SECURITIES_BROKERAGE_ROE_CAPITAL_RETURN_POSITIVE_CONTROL","symbol":"005940","name":"NH투자증권","trigger_type":"Stage2-Actionable","entry_date":"2024-02-26","entry_close":11420,"price_basis":"tradable_raw","mfe_30d_pct":14.71,"mae_30d_pct":-2.36,"mfe_90d_pct":14.71,"mae_90d_pct":-2.36,"mfe_180d_pct":26.09,"mae_180d_pct":-2.36,"forward_high_30d":13100,"forward_low_30d":11150,"forward_high_90d":13100,"forward_low_90d":11150,"forward_high_180d":14400,"forward_low_180d":11150,"calibration_usable":true,"case_role":"positive_control","novelty_key":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN|005940|Stage2-Actionable|2024-02-26","non_price_bridge":"brokerage/IB/wealth-management earnings bridge plus capital-return/value-up sensitivity","score_alignment":"cleaner securities C21 positive; keep Stage2-Actionable and allow Stage3-Yellow if ROE and payout execution refresh"}
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","round":"R6","loop":111,"large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","fine_archetype_id":"SECURITIES_CAPITAL_RETURN_POSITIVE_WITH_EARNINGS_CYCLE_4B_WATCH","symbol":"016360","name":"삼성증권","trigger_type":"Stage2-Actionable","entry_date":"2024-02-26","entry_close":40150,"price_basis":"tradable_raw","mfe_30d_pct":5.73,"mae_30d_pct":-4.48,"mfe_90d_pct":8.34,"mae_90d_pct":-11.96,"mfe_180d_pct":21.79,"mae_180d_pct":-11.96,"forward_high_30d":42450,"forward_low_30d":38350,"forward_high_90d":43550,"forward_low_90d":35350,"forward_high_180d":48900,"forward_low_180d":35350,"calibration_usable":true,"case_role":"positive_with_4B_watch","novelty_key":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN|016360|Stage2-Actionable|2024-02-26","non_price_bridge":"securities ROE / dividend yield / brokerage-flow recovery bridge, but cyclical earnings and MAE require refresh","score_alignment":"Stage2 may open; block Stage3-Green until brokerage turnover, WM/IB earnings and payout bridge refresh"}
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","round":"R6","loop":111,"large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","fine_archetype_id":"LOW_PBR_SECURITIES_LABEL_LOW_MFE_HIGH_MAE_STAGE2_CAP","symbol":"006800","name":"미래에셋증권","trigger_type":"Stage2-Watch","entry_date":"2024-02-26","entry_close":8680,"price_basis":"tradable_raw","mfe_30d_pct":5.53,"mae_30d_pct":-10.71,"mfe_90d_pct":5.53,"mae_90d_pct":-20.16,"mfe_180d_pct":5.53,"mae_180d_pct":-23.96,"forward_high_30d":9160,"forward_low_30d":7750,"forward_high_90d":9160,"forward_low_90d":6930,"forward_high_180d":9160,"forward_low_180d":6600,"calibration_usable":true,"case_role":"weak_bridge_counterexample","novelty_key":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN|006800|Stage2-Watch|2024-02-26","non_price_bridge":"low-PBR/securities value-up label without enough post-trigger ROE or capital-return execution validation","score_alignment":"cap Stage2; low MFE and deep MAE require clearer earnings/payout bridge before Actionable"}
```

---

## 4. Case analysis

### 4.1 NH Investment & Securities / 005940 — securities positive-control

`NH투자증권` is the cleanest securities positive-control in this loop. From the 2024-02-26 Value-up disappointment/follow-up pressure anchor, it moved from 11,420 to a March high of 13,100, then to 14,400 in August with shallow drawdown.

```yaml
entry_date: 2024-02-26
entry_close: 11420
30d_high: 13100
30d_low: 11150
90d_high: 13100
90d_low: 11150
180d_high: 14400
180d_low: 11150
mfe_30d_pct: 14.71
mae_30d_pct: -2.36
mfe_180d_pct: 26.09
mae_180d_pct: -2.36
```

Interpretation:

```text
classification = Stage2-Actionable positive-control
```

This is not only a low-PBR label. The price path says the market accepted the securities-company ROE/capital-return bridge. It can remain Stage2-Actionable, with a Stage3-Yellow path if payout, ROE and earnings quality refresh.

---

### 4.2 Samsung Securities / 016360 — positive, but cyclical earnings 4B watch

`삼성증권` worked more slowly. The immediate 30D MFE was modest, and the 90D drawdown reached double digits. But by the 180D window the stock reached 48,900, creating a valid delayed securities capital-return path.

```yaml
entry_date: 2024-02-26
entry_close: 40150
30d_high: 42450
30d_low: 38350
90d_high: 43550
90d_low: 35350
180d_high: 48900
180d_low: 35350
mfe_180d_pct: 21.79
mae_180d_pct: -11.96
```

Interpretation:

```text
classification = Stage2-Actionable with local 4B watch
```

The broker/wealth-management bridge worked, but the belt needed time to catch. Stage3-Green should require turnover, WM flow, IB recovery and dividend/buyback policy refresh.

---

### 4.3 Mirae Asset Securities / 006800 — low-PBR securities label cap

`미래에셋증권` is the counterexample. It had low-PBR/value-up exposure, but from the selected entry date MFE stayed low and MAE became deep.

```yaml
entry_date: 2024-02-26
entry_close: 8680
30d_high: 9160
30d_low: 7750
90d_high: 9160
90d_low: 6930
180d_high: 9160
180d_low: 6600
mfe_90d_pct: 5.53
mae_90d_pct: -20.16
```

Interpretation:

```text
classification = Stage2-Watch / weak bridge cap
```

This is the key guardrail. A securities company can be cheap and still fail the C21 route if earnings quality, brokerage turnover, IB pipeline and shareholder-return execution do not confirm.

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
| 005940 | positive-control | +14.71 / -2.36 | +14.71 / -2.36 | +26.09 / -2.36 | securities ROE/capital-return bridge validated |
| 016360 | positive + 4B watch | +5.73 / -4.48 | +8.34 / -11.96 | +21.79 / -11.96 | delayed positive; earnings-cycle refresh required |
| 006800 | weak-bridge cap | +5.53 / -10.71 | +5.53 / -20.16 | +5.53 / -23.96 | low-PBR brokerage label failed |

---

## 6. Raw component score breakdown

```jsonl
{"row_type":"score_simulation","symbol":"005940","raw_ROE_quality":3,"raw_PBR_mispricing":4,"raw_brokerage_flow_bridge":3,"raw_IB_WM_earnings_bridge":3,"raw_capital_return_execution":3,"raw_validation":4,"raw_info_edge":2,"stage2_actionable_bonus_before":2.0,"stage2_actionable_bonus_after":2.0,"simulated_route":"Stage2-Actionable-securities-positive-control"}
{"row_type":"score_simulation","symbol":"016360","raw_ROE_quality":3,"raw_PBR_mispricing":3,"raw_brokerage_flow_bridge":3,"raw_IB_WM_earnings_bridge":2,"raw_capital_return_execution":3,"raw_validation":2,"raw_info_edge":2,"stage2_actionable_bonus_before":2.0,"stage2_actionable_bonus_after":2.0,"simulated_route":"Stage2-Actionable-with-4B-watch"}
{"row_type":"score_simulation","symbol":"006800","raw_ROE_quality":1,"raw_PBR_mispricing":3,"raw_brokerage_flow_bridge":1,"raw_IB_WM_earnings_bridge":1,"raw_capital_return_execution":1,"raw_validation":0,"raw_info_edge":1,"stage2_actionable_bonus_before":2.0,"stage2_actionable_bonus_after":0.0,"simulated_route":"Stage2-Watch-weak-bridge-cap"}
```

---

## 7. Current calibrated profile stress test

### Existing error risk

C21 can over-reward this pattern:

```text
securities company
+ low PBR
+ Value-up headline
```

That is too broad. A securities company’s capital-return story is a flow machine. Brokerage turnover is the inlet, IB/WM earnings are the pressure chamber, ROE is the gauge, and dividend/buyback is the pipe reaching shareholders. If the inlet is weak or the pressure leaks, the PBR label alone is not enough.

### Rule candidate

```text
C21_SECURITIES_ROE_FLOW_CAPITAL_RETURN_REQUIREMENT

if C21
and securities_or_brokerage_label == true
and brokerage_flow_IB_WM_ROE_capital_return_bridge == false:
    stage2_actionable_bonus = 0
    max_stage = Stage2-Watch
```

```text
if C21
and securities_ROE_capital_return_bridge == true
and MFE_90D_pct >= +10
and MAE_90D_pct > -10:
    keep_stage2_actionable_bonus = true
    allow_stage3_yellow_path = true
```

```text
if C21
and securities_ROE_capital_return_bridge == true
and MFE_180D_pct >= +20
and MAE_90D_pct <= -10:
    local_4B_watch = true
    block_stage3_green_until_flow_ROE_payout_refresh = true
```

```text
if C21
and MFE_90D_pct < +10
and MAE_90D_pct <= -15
and incremental_ROE_or_capital_return_bridge == false:
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
new_axis_proposed: C21_SECURITIES_ROE_FLOW_CAPITAL_RETURN_REQUIREMENT
existing_axis_strengthened:
  - C21_low_PBR_label_not_enough_without_capital_return_execution
  - C21_securities_brokerage_flow_IB_WM_ROE_bridge_required
  - C21_securities_positive_control_with_low_MAE
  - C21_securities_delayed_positive_local_4B_watch
  - C21_weak_brokerage_valueup_bridge_stage2_cap
existing_axis_weakened: null
```

---

## 9. Next recommended archetypes

```text
C22_INSURANCE_RATE_CYCLE_RESERVE_retest_with_healthcare_GA_and_reinsurer_controls
R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW
C31_POLICY_SUBSIDY_LEGISLATION_EVENT
C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG
C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN_retest_with_digital_financial_and_brokerage_counterexamples
```
