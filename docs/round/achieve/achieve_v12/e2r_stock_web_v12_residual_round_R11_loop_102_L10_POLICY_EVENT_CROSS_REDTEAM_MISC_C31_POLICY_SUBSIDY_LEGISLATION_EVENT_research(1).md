# E2R v12 residual calibration research

## 0. Execution metadata

```yaml
schema_family: v12_sector_archetype_residual
selected_round: R11
selected_loop: 102
large_sector_id: L10_POLICY_EVENT_CROSS_REDTEAM_MISC
canonical_archetype_id: C31_POLICY_SUBSIDY_LEGISLATION_EVENT
fine_archetype_id: BATTERY_IRA_AMPC_POLICY_TO_UTILIZATION_CASHFLOW_BRIDGE_VS_POLICY_LABEL_FALSE_POSITIVE
selection_basis:
  main_execution_prompt: docs/core/e2r_v12_prompt_round_scheduler_corrected.txt
  no_repeat_index: docs/core/V12_Research_No_Repeat_Index.md
web_raw_fetch_status_this_turn:
  main_execution_prompt: cache_miss
  no_repeat_index: cache_miss
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

`C31_POLICY_SUBSIDY_LEGISLATION_EVENT` remains a Priority 0 policy-event archetype. Previous local C31 sector runs in this session reached `R11/C31 loop 101`, so this run continues as `R11/C31 loop 102`.

This pass focuses on the battery-policy subset of C31:

```text
IRA / AMPC / localization / battery policy support
→ customer call-off, utilization, AMPC cash credit, ESS/non-EV demand, financing stability
→ listed-company cashflow and price validation
```

The point is not to reward every battery name that sits under the IRA/AMPC umbrella. C31 should only reward the policy event when it becomes company-specific cashflow, utilization, customer diversification, or margin support.

Direct raw GitHub fetch for the prompt/index returned cache misses in this turn, so the run uses the current-session v12 procedure and stock-web-derived rows already calculated earlier. The rows below were originally computed from `Songdaiki/stock-web` tradable 1D OHLC in the current v12 session. No production scoring is changed.

---

## 1. Research thesis

C31 is not `policy support exists`.

It is the policy-to-cashflow bridge:

```text
subsidy / IRA / AMPC / localization policy
→ direct eligibility or company-specific transmission
→ utilization, customer call-off, tax credit, revenue, margin, cash conversion
→ price path validation
```

Battery-policy scoring needs three separate routes:

1. **AMPC/IRA escape hatch with customer diversification**
   - A broad demand warning can be offset if the issuer has diversified customers, AMPC cash credits, non-EV/ESS demand, and price path support.
   - Stage2 can survive, but policy contribution should remain capped until cash conversion is refreshed.

2. **Separator/material subsidiary label without utilization**
   - A battery-material or separator name can have policy exposure but still fail if customer pull, utilization, and financing bridge are weak.
   - Stage2 should be blocked.

3. **Battery customer/geography concentration risk**
   - Policy support does not fix customer concentration or weak call-off.
   - If MFE is modest and MAE deepens, C31 should cap or block the policy bonus.

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
  - e2r_stock_web_v12_residual_round_R3_loop_135_L3_BATTERY_EV_GREEN_MOBILITY_C13_BATTERY_JV_UTILIZATION_AMPC_IRA_research.md
  - e2r_stock_web_v12_residual_round_R3_loop_99_L3_BATTERY_EV_GREEN_MOBILITY_C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK_research.md
  - adjacent R13 policy-to-cashflow / Stage2 false-positive guardrail files
reason:
  - source rows were already calculated from Songdaiki/stock-web tradable raw 1D OHLC
  - this run converts C12/C13 battery-policy evidence into a C31 policy/subsidy/legislation lens
  - exact duplicate source-archetype rows should not be double-counted outside this C31 canonical key
  - no production scoring changed
```

Symbol caveats:

```yaml
373220:
  name: LG에너지솔루션
  role: AMPC/IRA/customer-diversification escape hatch
  calibration_usable: true

361610:
  name: SK아이이테크놀로지
  role: separator/material subsidiary label without utilization or financing bridge
  calibration_usable: true

006400:
  name: 삼성SDI
  role: battery customer/geography concentration and utilization risk
  calibration_usable: true
```

---

## 3. Trigger rows

```jsonl
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","round":"R11","loop":102,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","fine_archetype_id":"IRA_AMPC_CUSTOMER_DIVERSIFICATION_CASHFLOW_ESCAPE_HATCH","source_archetype_id":"C13_BATTERY_JV_UTILIZATION_AMPC_IRA","symbol":"373220","name":"LG에너지솔루션","trigger_type":"Stage2-Actionable","entry_date":"2024-07-25","entry_close":332500,"price_basis":"tradable_raw","mfe_30d_pct":18.50,"mae_30d_pct":-6.47,"mfe_90d_pct":33.53,"mae_90d_pct":-6.47,"mfe_180d_pct":33.53,"mae_180d_pct":-6.47,"forward_high_30d":394000,"forward_low_30d":311000,"forward_high_90d":444000,"forward_low_90d":311000,"forward_high_180d":444000,"forward_low_180d":311000,"calibration_usable":true,"case_role":"positive_escape_hatch","novelty_key":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT|373220|Stage2-Actionable|2024-07-25","non_price_bridge":"IRA/AMPC support plus diversified customer, ESS or non-EV demand bridge offsetting EV demand warning","score_alignment":"keep Stage2 with policy-contribution cap; require AMPC cash conversion, utilization and customer call-off refresh before Green"}
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","round":"R11","loop":102,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","fine_archetype_id":"SEPARATOR_POLICY_EXPOSURE_WITHOUT_UTILIZATION_CASHFLOW_BRIDGE_FALSE_POSITIVE","source_archetype_id":"C13_BATTERY_JV_UTILIZATION_AMPC_IRA","symbol":"361610","name":"SK아이이테크놀로지","trigger_type":"Stage2-FalsePositive","entry_date":"2024-05-16","entry_close":57600,"price_basis":"tradable_raw","mfe_30d_pct":1.04,"mae_30d_pct":-25.87,"mfe_90d_pct":1.04,"mae_90d_pct":-46.27,"mfe_180d_pct":1.04,"mae_180d_pct":-60.68,"forward_high_30d":58200,"forward_low_30d":42700,"forward_high_90d":58200,"forward_low_90d":30950,"forward_high_180d":58200,"forward_low_180d":22650,"calibration_usable":true,"case_role":"hard_counterexample","novelty_key":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT|361610|Stage2-FalsePositive|2024-05-16","non_price_bridge":"separator/material policy exposure without customer pull, utilization, parent financing or cash-conversion bridge","score_alignment":"block Stage2; policy/localization label cannot substitute for utilization and cashflow"}
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","round":"R11","loop":102,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","fine_archetype_id":"BATTERY_POLICY_LABEL_WITH_CUSTOMER_GEOGRAPHY_UTILIZATION_RISK_STAGE2_CAP","source_archetype_id":"C13_BATTERY_JV_UTILIZATION_AMPC_IRA","symbol":"006400","name":"삼성SDI","trigger_type":"Stage2-Watch","entry_date":"2024-06-28","entry_close":354000,"price_basis":"tradable_raw","mfe_30d_pct":10.17,"mae_30d_pct":-16.81,"mfe_90d_pct":11.16,"mae_90d_pct":-16.81,"mfe_180d_pct":11.16,"mae_180d_pct":-33.47,"forward_high_30d":390000,"forward_low_30d":294500,"forward_high_90d":393500,"forward_low_90d":294500,"forward_high_180d":393500,"forward_low_180d":235500,"calibration_usable":true,"case_role":"policy_cap_counterexample","novelty_key":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT|006400|Stage2-Watch|2024-06-28","non_price_bridge":"battery policy support exists but customer/geography concentration and utilization risk limited cashflow validation","score_alignment":"cap C31 Stage2; require customer call-off, AMPC eligibility, utilization and margin revision bridge before Actionable"}
```

---

## 4. Case analysis

### 4.1 LG Energy Solution / 373220 — policy support becomes cashflow only with diversified demand

LG Energy Solution is the positive escape hatch. The EV demand warning was real, but the price path did not collapse. It had enough customer diversification, AMPC/IRA support, and possible ESS/non-EV demand bridge to keep Stage2 alive.

```yaml
entry_date: 2024-07-25
entry_close: 332500
30d_high: 394000
30d_low: 311000
90d_high: 444000
90d_low: 311000
180d_high: 444000
180d_low: 311000
mfe_30d_pct: 18.50
mae_30d_pct: -6.47
mfe_90d_pct: 33.53
mae_90d_pct: -6.47
mfe_180d_pct: 33.53
mae_180d_pct: -6.47
```

Interpretation:

```text
classification = Stage2-Actionable positive escape hatch
```

C31 should preserve policy-support rows only when the policy reaches cashflow. The bridge here is not the acronym `AMPC`; the bridge is AMPC plus utilization, customer diversification, ESS/non-EV demand, and price confirmation.

---

### 4.2 SK IE Technology / 361610 — separator label without utilization bridge

SK IE Technology is the hard counterexample. It had battery-policy and separator exposure, but customer pull and utilization did not confirm. MAE expanded rapidly.

```yaml
entry_date: 2024-05-16
entry_close: 57600
30d_high: 58200
30d_low: 42700
90d_high: 58200
90d_low: 30950
180d_high: 58200
180d_low: 22650
mfe_90d_pct: 1.04
mae_90d_pct: -46.27
mfe_180d_pct: 1.04
mae_180d_pct: -60.68
```

Interpretation:

```text
classification = Stage2-FalsePositive
```

Policy exposure without utilization is only a signboard. The factory still has to run.

---

### 4.3 Samsung SDI / 006400 — policy label capped by customer/geography risk

Samsung SDI is not a full hard block, but it is a cap. There was modest MFE, but customer/geography concentration and weak utilization/revision bridge kept the path from validating.

```yaml
entry_date: 2024-06-28
entry_close: 354000
30d_high: 390000
30d_low: 294500
90d_high: 393500
90d_low: 294500
180d_high: 393500
180d_low: 235500
mfe_90d_pct: 11.16
mae_90d_pct: -16.81
mfe_180d_pct: 11.16
mae_180d_pct: -33.47
```

Interpretation:

```text
classification = Stage2-Watch / contribution cap
```

Policy cannot override customer call-off risk unless the company-specific utilization and margin bridge refreshes.

---

## 5. Score-return alignment

```yaml
new_independent_case_count: 3
new_visible_C31_symbol_count: 3
same_archetype_new_trigger_family_count: 3
calibration_usable_case_count: 3
calibration_usable_trigger_count: 3
positive_case_count: 1
counterexample_or_cap_count: 2
current_profile_error_count: 2
```

| symbol | role | 30D MFE/MAE | 90D MFE/MAE | 180D MFE/MAE | lesson |
|---|---:|---:|---:|---:|---|
| 373220 | AMPC/IRA escape hatch | +18.50 / -6.47 | +33.53 / -6.47 | +33.53 / -6.47 | policy support works only with utilization/customer/cashflow bridge |
| 361610 | hard false positive | +1.04 / -25.87 | +1.04 / -46.27 | +1.04 / -60.68 | separator label without utilization fails |
| 006400 | policy cap | +10.17 / -16.81 | +11.16 / -16.81 | +11.16 / -33.47 | customer/geography risk caps policy support |

---

## 6. Raw component score breakdown

```jsonl
{"row_type":"score_simulation","symbol":"373220","raw_policy_directness":4,"raw_AMPC_or_tax_credit_bridge":4,"raw_utilization_bridge":3,"raw_customer_diversification":4,"raw_margin_cash_conversion":3,"raw_validation":4,"raw_label_only_risk":1,"stage2_actionable_bonus_before":2.0,"stage2_actionable_bonus_after":2.0,"simulated_route":"Stage2Actionable_policy_cashflow_escape_hatch"}
{"row_type":"score_simulation","symbol":"361610","raw_policy_directness":3,"raw_AMPC_or_tax_credit_bridge":1,"raw_utilization_bridge":0,"raw_customer_diversification":0,"raw_margin_cash_conversion":0,"raw_validation":0,"raw_label_only_risk":5,"stage2_actionable_bonus_before":2.0,"stage2_actionable_bonus_after":0.0,"simulated_route":"Stage2FalsePositive_separator_policy_label"}
{"row_type":"score_simulation","symbol":"006400","raw_policy_directness":3,"raw_AMPC_or_tax_credit_bridge":2,"raw_utilization_bridge":1,"raw_customer_diversification":1,"raw_margin_cash_conversion":1,"raw_validation":1,"raw_label_only_risk":3,"stage2_actionable_bonus_before":2.0,"stage2_actionable_bonus_after":0.0,"simulated_route":"Stage2Watch_policy_cap"}
```

---

## 7. Current calibrated profile stress test

### Existing error risk

C31 can over-credit:

```text
IRA / AMPC / battery localization label
```

The correct bridge is narrower:

```text
policy support -> utilization -> customer call-off -> AMPC/tax credit cash -> margin/cash conversion
```

A subsidy is a reservoir. It only matters if the company has a pipe into it and the factory is producing enough flow.

### Rule candidate

```text
C31_BATTERY_POLICY_TO_UTILIZATION_CASHFLOW_BRIDGE_REQUIREMENT_V102

if C31
and battery_IRA_AMPC_localization_policy_label == true
and utilization_customer_calloff_AMPC_cash_margin_bridge == false:
    stage2_actionable_bonus = 0
    max_stage = Stage2-Watch
```

```text
if C31
and AMPC_IRA_cashflow_bridge == true
and customer_diversification_or_ESS_nonEV_bridge == true
and MFE_90D_pct >= +25
and MAE_90D_pct > -10:
    keep_stage2_actionable_bonus = true
```

```text
if C31
and separator_or_material_policy_exposure == true
and utilization_bridge == false
and MFE_90D_pct < +10
and MAE_90D_pct <= -25:
    route = Stage2_FalsePositive_Block
```

```text
if C31
and customer_geography_concentration_or_calloff_risk == true
and MAE_180D_pct <= -25:
    policy_bonus_cap = true
    require_customer_calloff_utilization_margin_refresh = true
```

---

## 8. Residual contribution summary

```yaml
do_not_propose_new_weight_delta: false
sector_specific_rule_candidate: false
canonical_archetype_rule_candidate: true
loop_contribution_label: canonical_archetype_rule_candidate
new_axis_proposed: C31_BATTERY_POLICY_TO_UTILIZATION_CASHFLOW_BRIDGE_REQUIREMENT_V102
existing_axis_strengthened:
  - C31_policy_label_not_enough_without_company_cashflow_bridge
  - C31_AMPC_IRA_cashflow_customer_diversification_escape_hatch
  - C31_separator_policy_exposure_without_utilization_false_positive
  - C31_customer_calloff_geography_concentration_policy_bonus_cap
existing_axis_weakened: null
```

---

## 9. Deferred Coding Agent Handoff Prompt

```text
Do not patch production scoring from this MD alone. Batch this C31 loop with C31 loops 1, 100, 101, C12/C13 battery loops, and adjacent R13 policy-to-cashflow / Stage2 false-positive / high-MAE guardrails. Extract `C31_BATTERY_POLICY_TO_UTILIZATION_CASHFLOW_BRIDGE_REQUIREMENT_V102` as a shadow-rule candidate. Preserve AMPC/IRA escape hatches only when customer diversification, utilization and cash conversion exist; block separator/material policy labels without utilization or cash bridge.
```

---

## 10. Next research state

```yaml
completed_round: R11
completed_loop: 102
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
