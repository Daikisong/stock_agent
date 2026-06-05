# E2R Stock-Web v12 Residual Research — R3 Loop 90

```yaml
artifact_type: e2r_stock_web_v12_residual_research
schema_version: v12
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
research_session: post_calibrated_sector_archetype_residual_research

scheduled_round: R3
scheduled_loop: 90
large_sector_id: L3_BATTERY_EV_GREEN_MOBILITY
canonical_archetype_id: C13_BATTERY_JV_UTILIZATION_AMPC_IRA
fine_archetype_id: US_BATTERY_JV_AMPC_IRA_UTILIZATION_BRIDGE_VS_POLICY_CREDIT_HEADLINE_ONLY

current_default_profile_proxy: e2r_2_1_stock_web_calibrated
previous_baseline_reference: e2r_2_0_baseline

price_data_source: Songdaiki/stock-web
upstream_source: FinanceData/marcap
price_basis: tradable_raw
price_adjustment_status: raw_unadjusted_marcap
calibration_shard_root: atlas/ohlcv_tradable_by_symbol_year
manifest_max_date: 2026-02-20

production_scoring_changed: false
shadow_weight_only: true
handoff_prompt_embedded: true
handoff_prompt_executed_now: false

completed_round: R3
completed_loop: 90
next_round: R4
next_loop: 90
round_schedule_status: valid
round_sector_consistency: pass
```

## 1. Schedule / novelty resolution

Previous completed file in the local run chain was:

```text
e2r_stock_web_v12_residual_round_R2_loop_90_L2_AI_SEMICONDUCTOR_ELECTRONICS_C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH_research.md
```

So the next scheduled execution is:

```text
R2 loop90 -> R3 loop90
```

R3 must map to:

```text
L3_BATTERY_EV_GREEN_MOBILITY
```

The selected canonical archetype is:

```text
C13_BATTERY_JV_UTILIZATION_AMPC_IRA
```

Reason for selection:

```text
- R3 loop88 already used C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK.
- R3 loop89 already used C14_EV_DEMAND_SLOWDOWN_4B_4C.
- C13 has meaningful coverage but still leaves an important residual: IRA/AMPC/JV headline can be real while stock return still fails if utilization, customer call-off, margin, or cash-flow bridge is weak.
```

No-repeat guard:

```text
hard_duplicate_key = canonical_archetype_id + symbol + trigger_type + entry_date

Avoided top-covered C13 symbols:
005070, 020150, 003670, 025900, 348370, 002710

Selected symbols:
373220 LG에너지솔루션
006400 삼성SDI
096770 SK이노베이션
```

These are same-sector but fresh C13 trigger families in this loop. They are not used as current recommendations or live candidates.

---

## 2. Manifest / profile checks

Stock-Web manifest basis:

```text
source_name = FinanceData/marcap
price_adjustment_status = raw_unadjusted_marcap
min_date = 1995-05-02
max_date = 2026-02-20
tradable_row_count = 14354401
raw_row_count = 15214118
symbol_count = 5414
active_like_symbol_count = 2868
inactive_or_delisted_like_symbol_count = 2546
markets = KONEX, KOSDAQ, KOSDAQ GLOBAL, KOSPI
calibration_shard_root = atlas/ohlcv_tradable_by_symbol_year
raw_shard_root = atlas/ohlcv_raw_by_symbol_year
schema_path = atlas/schema.json
universe_path = atlas/universe/all_symbols.csv
```

Profile checks:

```jsonl
{"row_type":"profile_check","symbol":"373220","name":"LG에너지솔루션","first_date":"2022-01-27","last_date":"2026-02-20","trading_day_count":992,"corporate_action_candidate_count":0,"corporate_action_candidate_dates":[],"calibration_caveat":"","calibration_usable":true}
{"row_type":"profile_check","symbol":"006400","name":"삼성SDI","first_date":"1995-05-02","last_date":"2026-02-20","trading_day_count":7762,"corporate_action_candidate_count":3,"corporate_action_candidate_dates":["1996-01-03","1998-11-03","2014-07-15"],"calibration_caveat":"Corporate-action candidate windows are blocked by default.","entry_180d_overlap":false,"calibration_usable":true}
{"row_type":"profile_check","symbol":"096770","name":"SK이노베이션","first_date":"2007-07-25","last_date":"2026-02-20","trading_day_count":4579,"corporate_action_candidate_count":1,"corporate_action_candidate_dates":["2024-11-20"],"calibration_caveat":"Corporate-action candidate windows are blocked by default.","entry_after_contamination_event":true,"entry_180d_overlap":false,"calibration_usable":true}
```

Important SK Innovation caveat:

```text
096770 has a corporate-action candidate on 2024-11-20. This research therefore avoids pre-2024-11-20 entries for 096770 and uses a post-event 2024-12-16 trigger/entry.
```

---

## 3. Archetype thesis being tested

C13 originally captures cases where U.S. battery-policy infrastructure is not merely a headline:

```text
- IRA production credit / AMPC is visible.
- U.S. JV or plant is real.
- Customer relationship is identifiable.
- Production or utilization path is visible.
- Revenue/margin/cash conversion is not just future optionality.
```

Residual question for loop90:

```text
Can C13 still over-score policy/JV/AMPC stories after e2r_2_1_stock_web_calibrated if the case has visible IRA credit or federal financing but weak utilization, capex pace, customer demand, or margin bridge?
```

Answer:

```text
Yes. The credit can cushion accounting losses, but it is not by itself a rerating bridge. C13 needs an explicit utilization-to-margin bridge. Otherwise the same mechanism that looks like a subsidy moat can become a fixed-cost absorption trap.
```

Mechanism analogy:

```text
AMPC is like a rebate on each bottle produced. It helps only when bottles keep leaving the factory. If the line slows, the rebate becomes a small umbrella in a storm of under-utilized capacity, depreciation, customer deferrals, and working-capital drag.
```

---

## 4. Case set

### Case 1 — 373220 LG에너지솔루션

```yaml
case_id: C13_LGES_2024_04_25_AMPC_CUSHIONED_LOSS_BUT_CAPEX_UTILIZATION_BRIDGE
symbol: "373220"
name: LG에너지솔루션
canonical_archetype_id: C13_BATTERY_JV_UTILIZATION_AMPC_IRA
trigger_type: earnings_ampc_ira_credit_utilization_bridge
trigger_date: 2024-04-25
entry_date: 2024-04-25
entry_price: 372500
classification: positive_with_initial_mae_and_local_4b_watch
calibration_usable: true
```

Evidence frame:

```text
LGES reported a sharp Q1 2024 profit decline due to weak EV demand, said it would minimize capex and reassess U.S./other investments, and would have reported a loss without the IRA tax credit.
```

Price path from Stock-Web tradable rows:

```text
entry close 2024-04-25 = 372,500
early low 2024-05-30 = 326,000
summer low 2024-08-05 = 311,000
recovery high 2024-10-08 = 444,000
```

Approximate return path:

```text
MFE_to_2024-10-08 = (444000 / 372500 - 1) = +19.2%
MAE_to_2024-08-05 = (311000 / 372500 - 1) = -16.5%
```

Interpretation:

```text
This is not a clean Green. The AMPC/IRA credit was real and helped avoid an accounting loss, but the same evidence included capex minimization and utilization uncertainty. Price ultimately produced a positive MFE, yet only after a deep interim MAE. C13 should treat this as a positive only when the credit is paired with a second-half utilization/customer-volume bridge.
```

Shadow label:

```text
Stage2-Actionable allowed.
Stage3-Yellow conditional.
Stage3-Green blocked until utilization + revenue/margin bridge is explicit.
local_4b_watch = true
```

### Case 2 — 006400 삼성SDI

```yaml
case_id: C13_SDI_2024_12_04_STARPLUS_DOE_LOAN_VS_SLOW_EV_DEMAND
symbol: "006400"
name: 삼성SDI
canonical_archetype_id: C13_BATTERY_JV_UTILIZATION_AMPC_IRA
trigger_type: us_jv_federal_loan_policy_financing
trigger_date: 2024-12-03
entry_date: 2024-12-04
entry_price: 259000
classification: counterexample_hard_4c_candidate
calibration_usable: true
```

Evidence frame:

```text
The StarPlus Energy JV between Stellantis and Samsung SDI received a conditional U.S. DOE loan commitment for two Indiana battery plants. That is a real JV/financing event, but not the same as high utilization or near-term earnings conversion.
```

Price path from Stock-Web tradable rows:

```text
entry close 2024-12-04 = 259,000
near-term high 2024-12-13 = 263,000
drawdown low 2025-04-09 = 170,000
```

Approximate return path:

```text
MFE_to_2024-12-13 = (263000 / 259000 - 1) = +1.5%
MAE_to_2025-04-09 = (170000 / 259000 - 1) = -34.4%
```

Interpretation:

```text
The policy-financing headline was real, but return alignment was poor. Without confirmed utilization, customer pull, and margin timing, C13 over-scores a plant-financing story as if it were already a profit bridge.
```

Shadow label:

```text
Stage2 allowed only as watch.
Stage2-Actionable blocked unless utilization/customer schedule bridge is present.
Stage3-Green blocked.
hard_4c_candidate = true
```

### Case 3 — 096770 SK이노베이션

```yaml
case_id: C13_SKI_2024_12_16_BLUEOVAL_LOAN_POST_CORPACT_UTILIZATION_RISK
symbol: "096770"
name: SK이노베이션
canonical_archetype_id: C13_BATTERY_JV_UTILIZATION_AMPC_IRA
trigger_type: us_jv_final_loan_policy_financing_post_corporate_action_window
trigger_date: 2024-12-16
entry_date: 2024-12-16
entry_price: 121400
classification: local_positive_but_high_mae_counterexample
calibration_usable: true
```

Evidence frame:

```text
The U.S. DOE finalized a $9.63B loan for Ford and SK On's BlueOval SK JV. The loan was real, large, and specifically tied to U.S. battery manufacturing capacity. However, the same broader C13 problem remains: financing capacity is not the same as realized utilization and battery segment profit.
```

Price path from Stock-Web tradable rows:

```text
entry close 2024-12-16 = 121,400
local high 2025-03-13 = 140,200
drawdown low 2025-04-09 = 92,700
```

Approximate return path:

```text
MFE_to_2025-03-13 = (140200 / 121400 - 1) = +15.5%
MAE_to_2025-04-09 = (92700 / 121400 - 1) = -23.6%
```

Interpretation:

```text
The market gave SKI a temporary policy/JV bid, but the path was not robust enough for Green. It is a local-4B / high-MAE case: real federal loan, weak durability because utilization, customer EV demand, and segment profitability remained contested.
```

Shadow label:

```text
Stage2-Actionable possible only with post-financing utilization bridge.
Stage3-Green blocked.
local_4b_watch = true
```

---

## 5. JSONL trigger rows

```jsonl
{"row_type":"trigger_case","case_id":"C13_LGES_2024_04_25_AMPC_CUSHIONED_LOSS_BUT_CAPEX_UTILIZATION_BRIDGE","scheduled_round":"R3","scheduled_loop":90,"large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C13_BATTERY_JV_UTILIZATION_AMPC_IRA","fine_archetype_id":"US_BATTERY_JV_AMPC_IRA_UTILIZATION_BRIDGE_VS_POLICY_CREDIT_HEADLINE_ONLY","symbol":"373220","name":"LG에너지솔루션","trigger_type":"earnings_ampc_ira_credit_utilization_bridge","trigger_date":"2024-04-25","entry_date":"2024-04-25","entry_price":372500,"peak_date":"2024-10-08","peak_price":444000,"trough_date":"2024-08-05","trough_price":311000,"mfe_pct":19.2,"mae_pct":-16.5,"classification":"positive_with_initial_mae_and_local_4b_watch","calibration_usable":true,"corporate_action_contaminated_180d":false}
{"row_type":"trigger_case","case_id":"C13_SDI_2024_12_04_STARPLUS_DOE_LOAN_VS_SLOW_EV_DEMAND","scheduled_round":"R3","scheduled_loop":90,"large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C13_BATTERY_JV_UTILIZATION_AMPC_IRA","fine_archetype_id":"US_BATTERY_JV_AMPC_IRA_UTILIZATION_BRIDGE_VS_POLICY_CREDIT_HEADLINE_ONLY","symbol":"006400","name":"삼성SDI","trigger_type":"us_jv_federal_loan_policy_financing","trigger_date":"2024-12-03","entry_date":"2024-12-04","entry_price":259000,"peak_date":"2024-12-13","peak_price":263000,"trough_date":"2025-04-09","trough_price":170000,"mfe_pct":1.5,"mae_pct":-34.4,"classification":"counterexample_hard_4c_candidate","calibration_usable":true,"corporate_action_contaminated_180d":false}
{"row_type":"trigger_case","case_id":"C13_SKI_2024_12_16_BLUEOVAL_LOAN_POST_CORPACT_UTILIZATION_RISK","scheduled_round":"R3","scheduled_loop":90,"large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C13_BATTERY_JV_UTILIZATION_AMPC_IRA","fine_archetype_id":"US_BATTERY_JV_AMPC_IRA_UTILIZATION_BRIDGE_VS_POLICY_CREDIT_HEADLINE_ONLY","symbol":"096770","name":"SK이노베이션","trigger_type":"us_jv_final_loan_policy_financing_post_corporate_action_window","trigger_date":"2024-12-16","entry_date":"2024-12-16","entry_price":121400,"peak_date":"2025-03-13","peak_price":140200,"trough_date":"2025-04-09","trough_price":92700,"mfe_pct":15.5,"mae_pct":-23.6,"classification":"local_positive_but_high_mae_counterexample","calibration_usable":true,"corporate_action_contaminated_180d":false}
```

---

## 6. Raw component score simulation

This is a shadow simulation only. It is not a production scoring change.

```jsonl
{"row_type":"score_simulation","case_id":"C13_LGES_2024_04_25_AMPC_CUSHIONED_LOSS_BUT_CAPEX_UTILIZATION_BRIDGE","symbol":"373220","baseline_stage2":true,"baseline_stage2_actionable":true,"baseline_stage3_yellow":true,"baseline_stage3_green":false,"raw_component_scores":{"policy_credit":18,"us_jv_or_us_capacity":14,"customer_visibility":11,"utilization_bridge":8,"margin_bridge":6,"revision_quality":8,"price_relative_strength":12,"risk_penalty":-14},"simulated_total":63,"simulated_revision":34,"shadow_gate_result":"yellow_or_watch_not_green"}
{"row_type":"score_simulation","case_id":"C13_SDI_2024_12_04_STARPLUS_DOE_LOAN_VS_SLOW_EV_DEMAND","symbol":"006400","baseline_stage2":true,"baseline_stage2_actionable":false,"baseline_stage3_yellow":false,"baseline_stage3_green":false,"raw_component_scores":{"policy_credit":18,"us_jv_or_us_capacity":17,"customer_visibility":6,"utilization_bridge":2,"margin_bridge":0,"revision_quality":-6,"price_relative_strength":2,"risk_penalty":-20},"simulated_total":19,"simulated_revision":-6,"shadow_gate_result":"stage2_watch_or_4c_candidate"}
{"row_type":"score_simulation","case_id":"C13_SKI_2024_12_16_BLUEOVAL_LOAN_POST_CORPACT_UTILIZATION_RISK","symbol":"096770","baseline_stage2":true,"baseline_stage2_actionable":true,"baseline_stage3_yellow":false,"baseline_stage3_green":false,"raw_component_scores":{"policy_credit":17,"us_jv_or_us_capacity":18,"customer_visibility":7,"utilization_bridge":4,"margin_bridge":0,"revision_quality":2,"price_relative_strength":9,"risk_penalty":-19},"simulated_total":38,"simulated_revision":12,"shadow_gate_result":"local_4b_watch_not_green"}
```

---

## 7. Aggregate summary

```json
{
  "row_type": "aggregate",
  "scheduled_round": "R3",
  "scheduled_loop": 90,
  "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY",
  "canonical_archetype_id": "C13_BATTERY_JV_UTILIZATION_AMPC_IRA",
  "fine_archetype_id": "US_BATTERY_JV_AMPC_IRA_UTILIZATION_BRIDGE_VS_POLICY_CREDIT_HEADLINE_ONLY",
  "new_independent_case_count": 3,
  "same_archetype_new_symbol_count": 3,
  "positive_case_count": 1,
  "counterexample_count": 2,
  "local_4b_overlay_case_count": 2,
  "hard_4c_candidate_count": 1,
  "calibration_usable_trigger_count": 3,
  "loop_contribution_label": "residual_error_found",
  "canonical_archetype_rule_candidate": true,
  "do_not_propose_new_weight_delta": true
}
```

---

## 8. Proposed shadow rule candidate

```text
C13_US_BATTERY_JV_AMPC_UTILIZATION_BRIDGE_RULE
```

Rule candidate:

```python
if canonical_archetype_id == "C13_BATTERY_JV_UTILIZATION_AMPC_IRA":
    if has_ira_or_ampc_credit_or_federal_loan and not has_utilization_or_customer_volume_bridge:
        cap_stage = "Stage2-Watch"
        block_stage3_green = True

    if has_us_jv_capacity and has_named_customer and has_utilization_bridge and has_margin_or_revenue_conversion:
        allow_stage2_actionable = True
        allow_stage3_yellow = True

    if price_mfe_local_positive and later_high_mae_without_revision_bridge:
        tag_local_4b_watch = True
        do_not_count_as_clean_positive = True

    if federal_loan_or_ampc_only and forward_mae <= -25 and mfe < +5:
        route_to_4c_candidate = True
```

Why this rule is different from existing global gates:

```text
The existing global profile already blocks generic price-only 4B and raises the Green bar. This C13 rule is not another generic Green-lateness rule. It is a specific bridge test for battery subsidy mechanics: IRA/AMPC/federal loan evidence must be connected to utilization and margin conversion, not merely capacity construction.
```

---

## 9. Residual contribution summary

```json
{
  "row_type": "residual_contribution",
  "contribution": "C13 distinguishes real IRA/AMPC/JV policy evidence from investable rerating evidence by requiring utilization, customer volume, and margin conversion.",
  "positive_control": "373220 LGES: AMPC helped cushion loss and later produced MFE, but only with initial drawdown and therefore not clean Green.",
  "counterexamples": [
    "006400 Samsung SDI: StarPlus federal loan/JV event without near-term utilization bridge had weak MFE and large MAE.",
    "096770 SK Innovation: BlueOval SK final loan produced local bid but later high MAE, showing financing does not equal battery-segment profit."
  ],
  "recommended_batch_action": "Add C13-specific utilization bridge guard as shadow rule candidate; do not globally lower/raise existing weights from this single loop."
}
```

---

## 10. Deferred Coding Agent Handoff Prompt

```text
You are the coding agent for Songdaiki/stock_agent. Do not execute this handoff during research collection.

When the user later asks for batch implementation, inspect all accumulated v12 residual research MD files and implement only durable, repeated, non-duplicative shadow rules.

For this file:
- Read the C13_US_BATTERY_JV_AMPC_UTILIZATION_BRIDGE_RULE candidate.
- Compare it with other C13 / C11 / C12 / C14 battery residual files.
- If repeated across multiple independent cases, add a canonical-archetype-specific guard:
  * IRA/AMPC/federal-loan/JV evidence alone should not unlock Stage3-Green.
  * Require utilization, named customer volume, revenue timing, or margin bridge.
  * Route loan/AMPC-only cases with weak MFE and high MAE to local-4B watch or 4C candidate.
- Preserve existing e2r_2_1_stock_web_calibrated global gates.
- Do not implement from this single file alone unless confirmed by batch review.
```
