# E2R v12 residual calibration research

## 0. Execution metadata

```yaml
schema_family: v12_sector_archetype_residual
selected_round: R11
selected_loop: 1
large_sector_id: L10_POLICY_EVENT_CROSS_REDTEAM_MISC
canonical_archetype_id: C31_POLICY_SUBSIDY_LEGISLATION_EVENT
fine_archetype_id: KOREA_SEMICONDUCTOR_SUPPORT_PACKAGE_POLICY_LABEL_VS_HBM_CAPEX_REVENUE_BRIDGE
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

C31 is a very thin area in the no-repeat index: 3 rows / 3 symbols. The visible covered set is `034230`, `068290`, and `086790`, so this run avoids those and uses new C31 tuples:

- `000660 SK하이닉스`
- `005930 삼성전자`
- `042700 한미반도체`

The prompt maps `C31` to `R11 / L10_POLICY_EVENT_CROSS_REDTEAM_MISC`. No parsed R11/C31 file was found in the fetched search/registry snippets, so this run starts the C31 continuation as `loop 1`.

---

## 1. Research thesis

C31 is not "policy headline = buy all beneficiaries." It is the bridge:

```text
policy / subsidy / legislation event
→ direct eligibility or company-specific transmission channel
→ order, capex, tax-credit, funding, margin or revenue bridge
→ price path validation
```

The 2024-05-23 Korea semiconductor support package is a useful C31 test because the headline is large and real, but the listed-company outcomes split sharply.

- `SK하이닉스`: policy support overlapped with a direct HBM/AI memory revenue bridge. C31 can keep Stage2 open, but the policy contribution must be capped because HBM demand, not subsidy alone, was the main axle.
- `삼성전자`: policy and CHIPS/subsidy labels existed, but the stock path later failed badly. This is the policy-label counterexample.
- `한미반도체`: equipment/capex bridge produced high MFE, but deep MAE requires local 4B and blocks Green without order/backlog refresh.

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
000660:
  name: SK하이닉스
  corporate_action_candidate_dates: [2001-06-27, 2002-06-07, 2003-04-14, 2003-04-21]
  relevant_window_after_candidate: true

005930:
  name: 삼성전자
  corporate_action_candidate_count: not material in relevant 2024 window
  calibration_caveat: raw_unadjusted_marcap

042700:
  name: 한미반도체
  corporate_action_candidate_dates: [2006-11-10, 2017-05-11, 2022-04-06]
  relevant_window_after_candidate: true
```

External policy anchor:

```text
2024-05-23: South Korea announced a 26 trillion won semiconductor support package, including Korea Development Bank financing for semiconductor investment, a fund for equipment makers/fabless companies, mega-cluster acceleration, and extension of investment tax credits.
```

---

## 3. Trigger rows

```jsonl
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","round":"R11","loop":1,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","fine_archetype_id":"KOREA_CHIP_SUPPORT_PACKAGE_WITH_HBM_REVENUE_BRIDGE_POSITIVE_BUT_CONTRIBUTION_CAP","symbol":"000660","name":"SK하이닉스","trigger_type":"Stage2-Actionable","entry_date":"2024-05-23","entry_close":200000,"price_basis":"tradable_raw","mfe_30d_pct":21.50,"mae_30d_pct":-5.90,"mfe_90d_pct":24.25,"mae_90d_pct":-24.20,"mfe_180d_pct":24.25,"mae_180d_pct":-27.65,"forward_high_30d":243000,"forward_low_30d":188200,"forward_high_90d":248500,"forward_low_90d":151600,"forward_high_180d":248500,"forward_low_180d":144700,"calibration_usable":true,"case_role":"positive_with_policy_contribution_cap_and_4B_watch","novelty_key":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT|000660|Stage2-Actionable|2024-05-23","non_price_bridge":"Korea chip support package plus company-specific HBM/AI memory revenue bridge","score_alignment":"Stage2 may open, but policy contribution must be capped and Green requires HBM order/revenue bridge refresh"}
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","round":"R11","loop":1,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","fine_archetype_id":"SAMSUNG_POLICY_SUBSIDY_LABEL_WITHOUT_HBM_EXECUTION_VALIDATION_FALSE_POSITIVE","symbol":"005930","name":"삼성전자","trigger_type":"Stage2-FalsePositive","entry_date":"2024-05-23","entry_close":78300,"price_basis":"tradable_raw","mfe_30d_pct":5.36,"mae_30d_pct":-6.13,"mfe_90d_pct":13.41,"mae_90d_pct":-10.34,"mfe_180d_pct":13.41,"mae_180d_pct":-36.27,"forward_high_30d":82500,"forward_low_30d":73500,"forward_high_90d":88800,"forward_low_90d":70200,"forward_high_180d":88800,"forward_low_180d":49900,"calibration_usable":true,"case_role":"hard_counterexample","novelty_key":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT|005930|Stage2-FalsePositive|2024-05-23","non_price_bridge":"semiconductor policy/subsidy label without validated HBM/execution bridge in price path","score_alignment":"policy label alone failed; block Stage2-Actionable unless company-specific execution bridge is refreshed"}
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","round":"R11","loop":1,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","fine_archetype_id":"HBM_EQUIPMENT_CAPEX_POLICY_BENEFICIARY_HIGH_MFE_HIGH_MAE_LOCAL_4B","symbol":"042700","name":"한미반도체","trigger_type":"Stage2-Actionable","entry_date":"2024-05-23","entry_close":146400,"price_basis":"tradable_raw","mfe_30d_pct":34.02,"mae_30d_pct":-5.67,"mfe_90d_pct":34.02,"mae_90d_pct":-32.99,"mfe_180d_pct":34.02,"mae_180d_pct":-45.97,"forward_high_30d":196200,"forward_low_30d":138100,"forward_high_90d":196200,"forward_low_90d":98100,"forward_high_180d":196200,"forward_low_180d":79100,"calibration_usable":true,"case_role":"vertical_MFE_local_4B_watch","novelty_key":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT|042700|Stage2-Actionable|2024-05-23","non_price_bridge":"HBM equipment/capex bridge and policy-supported equipment/fabless fund context","score_alignment":"high MFE validates a tradable bridge, but deep MAE blocks Stage3-Green without order/backlog/margin refresh"}
```

---

## 4. Case analysis

### 4.1 SK Hynix / 000660 — policy headline worked only because HBM bridge existed

`SK하이닉스` is the positive case, but not a pure policy case. The 2024-05-23 support package was a macro tailwind, yet the stock path aligns better with company-specific HBM/AI memory economics.

```yaml
entry_date: 2024-05-23
entry_close: 200000
30d_high: 243000
30d_low: 188200
90d_high: 248500
90d_low: 151600
180d_high: 248500
180d_low: 144700
mfe_30d_pct: 21.50
mae_30d_pct: -5.90
mfe_90d_pct: 24.25
mae_90d_pct: -24.20
mfe_180d_pct: 24.25
mae_180d_pct: -27.65
```

Interpretation:

```text
classification = Stage2-Actionable with policy contribution cap and 4B watch
```

The price path initially validated a positive trigger. But the later high MAE says C31 should not award a clean Green to the policy headline itself. The signal needs HBM order, ASP, utilization, customer allocation and revenue bridge refresh.

---

### 4.2 Samsung Electronics / 005930 — policy label false positive

`삼성전자` is the critical counterexample. The same policy headline applied to the semiconductor leader, and Samsung also had a broader subsidy/policy narrative. But the selected trigger path did not validate.

```yaml
entry_date: 2024-05-23
entry_close: 78300
30d_high: 82500
30d_low: 73500
90d_high: 88800
90d_low: 70200
180d_high: 88800
180d_low: 49900
mfe_30d_pct: 5.36
mae_30d_pct: -6.13
mfe_90d_pct: 13.41
mae_90d_pct: -10.34
mfe_180d_pct: 13.41
mae_180d_pct: -36.27
```

Interpretation:

```text
classification = Stage2-FalsePositive
```

The policy label did not protect the stock when execution, HBM positioning and memory-cycle confidence weakened. This is the core C31 guardrail: broad policy benefit is not enough.

---

### 4.3 Hanmi Semiconductor / 042700 — equipment bridge produced MFE, then failed Green test

`한미반도체` is the most dangerous C31 case because MFE was high. Price-only learning would call it a success. But the full path shows a deep failure after the initial vertical move.

```yaml
entry_date: 2024-05-23
entry_close: 146400
30d_high: 196200
30d_low: 138100
90d_high: 196200
90d_low: 98100
180d_high: 196200
180d_low: 79100
mfe_30d_pct: 34.02
mae_30d_pct: -5.67
mfe_90d_pct: 34.02
mae_90d_pct: -32.99
mfe_180d_pct: 34.02
mae_180d_pct: -45.97
```

Interpretation:

```text
classification = Stage2-Actionable with local 4B watch
```

The bridge was real enough to trade, but not durable enough for Green. C31 should require order backlog, customer concentration, margin resilience and capex conversion before upgrading.

---

## 5. Score-return alignment

```yaml
new_independent_case_count: 3
new_visible_C31_symbol_count: 3
same_archetype_new_trigger_family_count: 3
calibration_usable_case_count: 3
calibration_usable_trigger_count: 3
positive_or_watch_case_count: 2
counterexample_count: 1
current_profile_error_count: 2
```

| symbol | role | 30D MFE/MAE | 90D MFE/MAE | 180D MFE/MAE | lesson |
|---|---:|---:|---:|---:|---|
| 000660 | positive + policy contribution cap | +21.50 / -5.90 | +24.25 / -24.20 | +24.25 / -27.65 | policy worked only with HBM revenue bridge |
| 005930 | hard counterexample | +5.36 / -6.13 | +13.41 / -10.34 | +13.41 / -36.27 | policy/subsidy label failed without execution bridge |
| 042700 | high-MFE local 4B | +34.02 / -5.67 | +34.02 / -32.99 | +34.02 / -45.97 | equipment/capex bridge needs order/margin refresh |

---

## 6. Raw component score breakdown

```jsonl
{"row_type":"score_simulation","symbol":"000660","raw_policy_directness":3,"raw_subsidy_or_tax_credit_bridge":2,"raw_company_specific_execution_bridge":5,"raw_revenue_or_margin_bridge":5,"raw_validation":3,"raw_label_only_risk":1,"stage2_actionable_bonus_before":2.0,"stage2_actionable_bonus_after":2.0,"simulated_route":"Stage2-Actionable-policy-contribution-cap-4B-watch"}
{"row_type":"score_simulation","symbol":"005930","raw_policy_directness":3,"raw_subsidy_or_tax_credit_bridge":2,"raw_company_specific_execution_bridge":1,"raw_revenue_or_margin_bridge":1,"raw_validation":0,"raw_label_only_risk":4,"stage2_actionable_bonus_before":2.0,"stage2_actionable_bonus_after":0.0,"simulated_route":"Stage2-FalsePositive-policy-label"}
{"row_type":"score_simulation","symbol":"042700","raw_policy_directness":2,"raw_subsidy_or_tax_credit_bridge":2,"raw_company_specific_execution_bridge":4,"raw_revenue_or_margin_bridge":3,"raw_validation":2,"raw_label_only_risk":2,"stage2_actionable_bonus_before":2.0,"stage2_actionable_bonus_after":1.0,"simulated_route":"Local4B-equipment-bridge"}
```

---

## 7. Current calibrated profile stress test

### Existing error risk

C31 can over-score:

```text
big policy package
+ famous sector beneficiary
+ early price spike
```

That is too broad. A policy is rain over the whole field. The model should ask which company actually has roots in the wet soil. If the company-specific pipe into orders, tax credits, capex, margin or revenue is missing, the headline evaporates.

### Rule candidate

```text
C31_POLICY_LABEL_COMPANY_SPECIFIC_BRIDGE_REQUIREMENT

if C31
and policy_subsidy_legislation_headline == true
and company_specific_order_tax_credit_capex_margin_or_revenue_bridge == false:
    stage2_actionable_bonus = 0
    max_stage = Stage2-Watch
```

```text
if C31
and broad_sector_policy_headline == true
and dominant_driver_is_company_specific_demand_or_cycle == true:
    cap_policy_contribution = true
    require_source_archetype_reclassification = true
```

```text
if C31
and MFE_30D_pct >= +25
and MAE_90D_pct <= -25
and refreshed_policy_to_cash_bridge == false:
    local_4B_watch = true
    block_stage3_green = true
```

```text
if C31
and MFE_90D_pct < +15
and MAE_180D_pct <= -25
and company_specific_execution_bridge == false:
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
new_axis_proposed: C31_POLICY_LABEL_COMPANY_SPECIFIC_BRIDGE_REQUIREMENT
existing_axis_strengthened:
  - C31_policy_subsidy_headline_not_enough_without_company_bridge
  - C31_policy_contribution_cap_when_company_specific_cycle_dominates
  - C31_vertical_MFE_policy_beneficiary_local_4B_watch
  - C31_policy_label_low_validation_false_positive_block
existing_axis_weakened: null
```

---

## 9. Next recommended archetypes

```text
C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG
C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN_retest_with_digital_financial_and_brokerage_counterexamples
C22_INSURANCE_RATE_CYCLE_RESERVE_retest_with_healthcare_underwriting_controls
R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION
C31_POLICY_SUBSIDY_LEGISLATION_EVENT_retest_with_valueup_and_energy_policy_controls
```
