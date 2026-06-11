# E2R v12 residual calibration research

## 0. Execution metadata

```yaml
schema_family: v12_sector_archetype_residual
selected_round: R11
selected_loop: 101
large_sector_id: L10_POLICY_EVENT_CROSS_REDTEAM_MISC
canonical_archetype_id: C31_POLICY_SUBSIDY_LEGISLATION_EVENT
fine_archetype_id: POLICY_TO_CASHFLOW_BRIDGE_SHAREHOLDER_RETURN_EXPORT_CONTRACT_EXPLORATION_HEADLINE
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

`C31_POLICY_SUBSIDY_LEGISLATION_EVENT` remains one of the thinnest Priority 0 archetypes. The visible no-repeat index marks it as only 3 rows / 3 symbols, with visible top-covered symbols `034230`, `068290`, and `086790`. This pass therefore avoids those visible symbols and uses three new C31 tuples:

- `005380 현대차`
- `036460 한국가스공사`
- `064350 현대로템`

The repository registry already contains a parsed `R11/C31 loop 99`, and the prior local C31 pass completed loop 100. This run continues as `R11/C31 loop 101`.

---

## 1. Research thesis

C31 is not simply “policy headline.” It is the bridge:

```text
policy / subsidy / legislation / state-linked event
→ company-specific cashflow bridge
→ revenue, shareholder return, confirmed project economics, margin or orderbook
→ price path validation
```

This loop separates three very different policy-event types:

1. **Actual export contract / government-linked commercial bridge**  
   If a state-linked event is a signed order with a direct revenue bridge, Stage2 may remain open.

2. **Exploration or policy headline without confirmed economics**  
   A policy/exploration headline can create very large MFE, but without reserves, commerciality, financing and extraction economics it is local 4B at most.

3. **Shareholder-return / Value-up plan without core cycle support**  
   A cash-return plan can be real, but if volume/mix/margin pressure overwhelms it, C31 should cap the policy bonus rather than call it Green.

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
005380:
  name: 현대차
  corporate_action_candidate_dates: old only
  relevant_window_after_candidate: true
  calibration_use: usable

036460:
  name: 한국가스공사
  corporate_action_candidate_count: 0
  calibration_use: usable

064350:
  name: 현대로템
  corporate_action_candidate_dates: [2020-08-14]
  relevant_window_after_candidate: true
  calibration_use: usable
```

External policy/commercial anchors:

```text
2024-08-28: Hyundai Motor investor-day / Value-up shareholder-return package.
2024-06-03: Korea East Sea oil/gas exploration policy headline.
2025-02-26: Hyundai Rotem state-linked export contract / direct revenue bridge case.
```

---

## 3. Trigger rows

```jsonl
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","round":"R11","loop":101,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","fine_archetype_id":"VALUEUP_SHAREHOLDER_RETURN_PLAN_REAL_CASH_BUT_MARGIN_CYCLE_STAGE2_CAP","symbol":"005380","name":"현대차","trigger_type":"Stage2-Watch","entry_date":"2024-08-28","entry_close":259000,"price_basis":"tradable_raw","mfe_30d_pct":3.09,"mae_30d_pct":-14.48,"mfe_90d_pct":3.09,"mae_90d_pct":-22.78,"mfe_180d_pct":3.09,"mae_180d_pct":-32.12,"forward_high_30d":267000,"forward_low_30d":221500,"forward_high_90d":267000,"forward_low_90d":200000,"forward_high_180d":267000,"forward_low_180d":175800,"calibration_usable":true,"case_role":"counterexample_policy_cash_return_real_but_cycle_overrides","novelty_key":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT|005380|Stage2-Watch|2024-08-28","non_price_bridge":"Value-up shareholder-return plan and buyback/dividend intent, but core volume/mix/margin cycle weakened","score_alignment":"cap policy bonus; require margin-cycle confirmation before Actionable"}
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","round":"R11","loop":101,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","fine_archetype_id":"EXPLORATION_POLICY_HEADLINE_HIGH_MFE_LOCAL_4B_WITHOUT_CONFIRMED_RESERVE_CASHFLOW","symbol":"036460","name":"한국가스공사","trigger_type":"Stage2-Watch","entry_date":"2024-06-03","entry_close":38700,"price_basis":"tradable_raw","mfe_30d_pct":66.67,"mae_30d_pct":-3.49,"mfe_90d_pct":66.67,"mae_90d_pct":-5.68,"mfe_180d_pct":66.67,"mae_180d_pct":-23.51,"forward_high_30d":64500,"forward_low_30d":37350,"forward_high_90d":64500,"forward_low_90d":36500,"forward_high_180d":64500,"forward_low_180d":29600,"calibration_usable":true,"case_role":"vertical_MFE_local_4B_watch","novelty_key":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT|036460|Stage2-Watch|2024-06-03","non_price_bridge":"East Sea oil/gas exploration headline without confirmed commercial reserve or cashflow economics","score_alignment":"local 4B watch; block Green until reserve, economics and company cashflow bridge are confirmed"}
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","round":"R11","loop":101,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","fine_archetype_id":"STATE_LINKED_EXPORT_CONTRACT_DIRECT_REVENUE_BRIDGE_POSITIVE_CONTROL","symbol":"064350","name":"현대로템","trigger_type":"Stage2-Actionable","entry_date":"2025-02-26","entry_close":85600,"price_basis":"tradable_raw","mfe_30d_pct":36.45,"mae_30d_pct":-8.64,"mfe_90d_pct":157.59,"mae_90d_pct":-8.64,"mfe_180d_pct":157.59,"mae_180d_pct":-8.64,"forward_high_30d":116800,"forward_low_30d":78200,"forward_high_90d":220500,"forward_low_90d":78200,"forward_high_180d":220500,"forward_low_180d":78200,"calibration_usable":true,"case_role":"positive_control_direct_export_contract","novelty_key":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT|064350|Stage2-Actionable|2025-02-26","non_price_bridge":"state-linked export contract with direct revenue bridge","score_alignment":"keep Stage2-Actionable; direct signed order/revenue path is a C31 escape hatch"}
```

---

## 4. Case analysis

### 4.1 Hyundai Motor / 005380 — cash-return plan is real, but not enough alone

Hyundai Motor’s shareholder-return plan is not fake evidence. The buyback/dividend intent is a real cash-return bridge. The problem is that the selected trigger path did not validate a standalone C31 Green route.

```yaml
entry_date: 2024-08-28
entry_close: 259000
30d_high: 267000
30d_low: 221500
90d_high: 267000
90d_low: 200000
180d_high: 267000
180d_low: 175800
mfe_90d_pct: 3.09
mae_90d_pct: -22.78
mfe_180d_pct: 3.09
mae_180d_pct: -32.12
```

Interpretation:

```text
classification = Stage2-Watch / policy cash-return cap
```

This is the key nuance: even a real shareholder-return plan can fail as a price-path trigger when the underlying auto cycle, margin mix, or volume concerns dominate. C31 should not punish the existence of cash return, but it should cap the policy bonus until the sector margin bridge confirms.

---

### 4.2 Korea Gas Corporation / 036460 — exploration policy flare, not a furnace

Korea Gas Corporation is the vertical-MFE trap. The exploration headline was powerful enough to create a large short-window move, but the commercial cash bridge was not confirmed.

```yaml
entry_date: 2024-06-03
entry_close: 38700
30d_high: 64500
30d_low: 37350
90d_high: 64500
90d_low: 36500
180d_high: 64500
180d_low: 29600
mfe_30d_pct: 66.67
mae_180d_pct: -23.51
```

Interpretation:

```text
classification = local 4B watch / no Stage3-Green
```

The spike is real. But exploration potential is not the same as reserves, recoverability, capex plan, production schedule, regulated return, or cashflow. The correct metaphor is a flare, not a furnace: it lights the sky, but it does not heat the factory until fuel and pipes are proven.

---

### 4.3 Hyundai Rotem / 064350 — signed export contract positive-control

Hyundai Rotem is the positive-control row. The trigger is a signed state-linked export order with a direct revenue bridge, not merely a policy slogan.

```yaml
entry_date: 2025-02-26
entry_close: 85600
30d_high: 116800
30d_low: 78200
90d_high: 220500
90d_low: 78200
180d_high: 220500
180d_low: 78200
mfe_90d_pct: 157.59
mae_90d_pct: -8.64
```

Interpretation:

```text
classification = Stage2-Actionable positive-control
```

This is the bridge C31 should reward: state-linked event plus signed contract plus direct revenue path. The score should preserve Stage2 and allow a Stage3-Yellow path when delivery, margin and cash collection evidence stays alive.

---

## 5. Score-return alignment

```yaml
new_independent_case_count: 3
new_visible_C31_symbol_count: 3
same_archetype_new_trigger_family_count: 3
calibration_usable_case_count: 3
calibration_usable_trigger_count: 3
positive_case_count: 1
counterexample_count: 2
current_profile_error_count: 2
```

| symbol | role | 30D MFE/MAE | 90D MFE/MAE | 180D MFE/MAE | lesson |
|---|---:|---:|---:|---:|---|
| 005380 | policy cash-return cap | +3.09 / -14.48 | +3.09 / -22.78 | +3.09 / -32.12 | real cash return can still fail if margin cycle dominates |
| 036460 | exploration local 4B | +66.67 / -3.49 | +66.67 / -5.68 | +66.67 / -23.51 | huge MFE but no confirmed reserve/cashflow bridge |
| 064350 | direct contract positive-control | +36.45 / -8.64 | +157.59 / -8.64 | +157.59 / -8.64 | signed export order validates C31 |

---

## 6. Raw component score breakdown

```jsonl
{"row_type":"score_simulation","symbol":"005380","raw_policy_directness":3,"raw_company_specific_cash_bridge":3,"raw_revenue_or_margin_bridge":1,"raw_validation":0,"raw_label_only_risk":2,"raw_info_edge":2,"stage2_actionable_bonus_before":2.0,"stage2_actionable_bonus_after":0.0,"simulated_route":"Stage2Watch_policy_cash_return_cap"}
{"row_type":"score_simulation","symbol":"036460","raw_policy_directness":4,"raw_company_specific_cash_bridge":0,"raw_revenue_or_margin_bridge":0,"raw_validation":1,"raw_label_only_risk":4,"raw_info_edge":3,"stage2_actionable_bonus_before":2.0,"stage2_actionable_bonus_after":1.0,"simulated_route":"Local4B_exploration_policy_flare"}
{"row_type":"score_simulation","symbol":"064350","raw_policy_directness":4,"raw_company_specific_cash_bridge":5,"raw_revenue_or_margin_bridge":5,"raw_validation":5,"raw_label_only_risk":0,"raw_info_edge":3,"stage2_actionable_bonus_before":2.0,"stage2_actionable_bonus_after":2.0,"simulated_route":"Stage2Actionable_direct_export_contract"}
```

---

## 7. Current calibrated profile stress test

### Existing error risk

The current profile can over-score:

```text
policy headline
+ famous beneficiary
+ short-window MFE
```

It can also under-score direct contract cases if it treats all policy events as noisy.

The distinction is the cashflow bridge:

```text
shareholder return plan -> real, but still needs core cycle/margin support
exploration headline -> not cashflow until commerciality is proven
signed export contract -> direct revenue bridge
```

### Rule candidate

```text
C31_POLICY_TO_CASHFLOW_BRIDGE_REQUIREMENT_V101

if C31
and policy_event_or_legislation_headline == true
and company_specific_cashflow_bridge == false:
    stage2_actionable_bonus = 0
    max_stage = Stage2-Watch
```

```text
if C31
and policy_event_or_legislation_headline == true
and MFE_30D_pct >= +30
and confirmed_project_economics_or_cash_bridge == false:
    local_4B_watch = true
    block_stage3_green = true
```

```text
if C31
and signed_contract_or_legally_binding_cash_transfer == true
and direct_revenue_or_shareholder_cash_bridge == true
and MFE_90D_pct >= +20
and MAE_90D_pct > -15:
    keep_stage2_actionable_bonus = true
```

```text
if C31
and shareholder_return_plan == true
and cyclical_volume_margin_risk == true
and MFE_90D_pct < +10
and MAE_90D_pct <= -20:
    policy_bonus_cap = true
    require_sector_margin_confirmation = true
```

---

## 8. Residual contribution summary

```yaml
do_not_propose_new_weight_delta: false
sector_specific_rule_candidate: false
canonical_archetype_rule_candidate: true
loop_contribution_label: canonical_archetype_rule_candidate
new_axis_proposed: C31_POLICY_TO_CASHFLOW_BRIDGE_REQUIREMENT_V101
existing_axis_strengthened:
  - C31_policy_to_cashflow_bridge_requirement
  - C31_exploration_policy_headline_local_4B_watch
  - C31_shareholder_return_policy_bonus_cap_when_margin_cycle_weak
  - C31_signed_export_contract_direct_revenue_bridge_escape_hatch
existing_axis_weakened: null
```

---

## 9. Deferred Coding Agent Handoff Prompt

```text
Do not patch production scoring from this single MD. Batch this C31 loop with adjacent C31 policy/subsidy/legislation event files and R13 accounting-trust/Stage2 false-positive files. Extract `C31_POLICY_TO_CASHFLOW_BRIDGE_REQUIREMENT_V101` as a shadow-rule candidate. Preserve signed-contract escape hatches while capping exploration-only and shareholder-return-only policy events when core margin/cashflow confirmation is missing.
```

---

## 10. Next research state

```yaml
completed_round: R11
completed_loop: 101
selection_basis: docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket: Priority 0
round_schedule_status: coverage_index_selected
round_sector_consistency: pass
next_recommended_archetypes:
  - C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP
  - C15_MATERIAL_SPREAD_SUPERCYCLE
  - C16_STRATEGIC_RESOURCE_POLICY_SUPPLY
  - C17_CHEMICAL_COMMODITY_MARGIN_SPREAD
  - R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW
```
