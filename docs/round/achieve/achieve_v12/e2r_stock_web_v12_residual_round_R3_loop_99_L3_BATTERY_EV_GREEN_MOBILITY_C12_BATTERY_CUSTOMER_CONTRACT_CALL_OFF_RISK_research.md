# E2R Historical Calibration Prompt v12 — Stock-Web OHLC Atlas / Sector-Archetype Residual Expansion

```text
schema_family = v12_sector_archetype_residual
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
research_session = post_calibrated_sector_archetype_residual_research

selected_round = R3
selected_loop = 99
large_sector_id = L3_BATTERY_EV_GREEN_MOBILITY
canonical_archetype_id = C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK
fine_archetype_id = CUSTOMER_CONTRACT_CALLOFF_AND_CAPACITY_EXPANSION_DELAY_BRIDGE_VS_DIVERSIFIED_CUSTOMER_ESS_ESCAPE_HATCH
selection_basis = docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket = Priority 0
round_schedule_status = coverage_index_selected
round_sector_consistency = pass

price_source = Songdaiki/stock-web
price_basis = tradable_raw
price_adjustment_status = raw_unadjusted_marcap
stock_web_manifest_max_date = 2026-02-20
production_scoring_changed = false
shadow_weight_only = true
```

## 1. Selection rationale

`C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK` remains under-covered relative to the post-R13 cross-check set. The repository index shows C12 at 16 rows / 11 symbols, while many adjacent battery archetypes are already materially denser. The top-covered C12 symbols are concentrated in `005070`, `020150`, `078600`, `121600`, `003670`, `006400`, so this loop adds two visible-new C12 symbols (`373220`, `361610`) and one reused-but-new-trigger-family control (`006400`).

The selected loop is `R3 loop 99` because the registry-visible C12 entries sit at `R3 loop 98`, so the next pair loop is 99.

## 2. Thesis under test

C12 is not a generic "battery demand weak" label. It is specifically a customer-contract / call-off / utilization risk archetype:

```text
bad Stage2:
    headline contract/backlog/capacity
    but customer pull timing, end-demand, utilization, or automaker order pace weakens
    and revenue/margin/cash bridge does not refresh

escape hatch:
    customer risk visible
    but diversified customer base, ESS conversion, or confirmed demand recovery bridge limits MAE
```

Mechanically, a contract is a pipe and a call-off is the water actually running through it. C12 asks whether the pipe is merely announced, or whether customers are still pulling volume through it at profitable pressure.

## 3. Price source validation

- `Songdaiki/stock-web` manifest basis: `FinanceData/marcap`
- calibration shard root: `atlas/ohlcv_tradable_by_symbol_year`
- price adjustment status: `raw_unadjusted_marcap`
- manifest max date: `2026-02-20`
- all rows below use actual 1D OHLC from `atlas/ohlcv_tradable_by_symbol_year`.

## 4. Case table

| case_id | symbol | name | trigger_date | entry_date | entry_price | classification | evidence family |
|---|---:|---|---|---|---:|---|---|
| C12-LGES-20240725 | 373220 | LG에너지솔루션 | 2024-07-25 | 2024-07-25 | 332500 | positive-control / escape hatch | revenue cut + customer demand risk but diversified/ESS bridge |
| C12-SKIET-20240516 | 361610 | SK아이이테크놀로지 | 2024-05-15 | 2024-05-16 | 57600 | counterexample / hard C12 risk | separator sale/restructuring report tied to weak EV demand |
| C12-SDI-20240628 | 006400 | 삼성SDI | 2024-06-28 | 2024-06-28 | 354000 | counterexample / customer concentration risk | Europe/Rivian demand weakness and shipment-risk forecast |

## 5. Trigger rows JSONL

```jsonl
{"schema_family":"v12_sector_archetype_residual","row_type":"trigger","selected_round":"R3","selected_loop":99,"large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","fine_archetype_id":"CUSTOMER_CONTRACT_CALLOFF_AND_CAPACITY_EXPANSION_DELAY_BRIDGE_VS_DIVERSIFIED_CUSTOMER_ESS_ESCAPE_HATCH","case_id":"C12-LGES-20240725","symbol":"373220","name":"LG에너지솔루션","trigger_date":"2024-07-25","entry_date":"2024-07-25","entry_price":332500,"trigger_type":"Stage2","price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","MFE_30D_pct":13.68,"MAE_30D_pct":-6.47,"MFE_90D_pct":29.32,"MAE_90D_pct":-6.47,"MFE_180D_pct":30.98,"MAE_180D_pct":-6.47,"max_high_30D":378000,"min_low_30D":311000,"max_high_90D":430000,"min_low_90D":311000,"max_high_180D":435500,"min_low_180D":311000,"classification":"positive_control_escape_hatch","calibration_usable":true,"current_profile_verdict":"Stage2-Actionable would not be wrong if diversified customer/ESS bridge is confirmed; do not hard-block merely on EV demand headline.","residual_error_type":"avoid_overblocking_c12_when_actual_price_path_confirms_escape","evidence_family":"LGES revenue target cut, weak EV demand, customer exposure to Tesla/GM/Hyundai, capacity expansion easing; price path shows limited MAE and strong 90D/180D MFE."}
{"schema_family":"v12_sector_archetype_residual","row_type":"trigger","selected_round":"R3","selected_loop":99,"large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","fine_archetype_id":"CUSTOMER_CONTRACT_CALLOFF_AND_CAPACITY_EXPANSION_DELAY_BRIDGE_VS_DIVERSIFIED_CUSTOMER_ESS_ESCAPE_HATCH","case_id":"C12-SKIET-20240516","symbol":"361610","name":"SK아이이테크놀로지","trigger_date":"2024-05-15","entry_date":"2024-05-16","entry_price":57600,"trigger_type":"Stage2","price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","MFE_30D_pct":1.04,"MAE_30D_pct":-25.87,"MFE_90D_pct":1.04,"MAE_90D_pct":-46.27,"MFE_180D_pct":1.04,"MAE_180D_pct":-57.73,"max_high_30D":58200,"min_low_30D":42700,"max_high_90D":58200,"min_low_90D":30950,"max_high_180D":58200,"min_low_180D":24350,"classification":"counterexample","calibration_usable":true,"current_profile_verdict":"Stage2 should be blocked or capped unless separator customer pull/utilization bridge is refreshed.","residual_error_type":"customer_contract_calloff_false_stage2","evidence_family":"SKIET separator exposure; sale/restructuring report tied to SK On financial pressure and weakening EV demand; subsequent path produced low MFE/high MAE."}
{"schema_family":"v12_sector_archetype_residual","row_type":"trigger","selected_round":"R3","selected_loop":99,"large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","fine_archetype_id":"CUSTOMER_CONTRACT_CALLOFF_AND_CAPACITY_EXPANSION_DELAY_BRIDGE_VS_DIVERSIFIED_CUSTOMER_ESS_ESCAPE_HATCH","case_id":"C12-SDI-20240628","symbol":"006400","name":"삼성SDI","trigger_date":"2024-06-28","entry_date":"2024-06-28","entry_price":354000,"trigger_type":"Stage2","price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","MFE_30D_pct":10.17,"MAE_30D_pct":-16.81,"MFE_90D_pct":11.16,"MAE_90D_pct":-16.81,"MFE_180D_pct":11.16,"MAE_180D_pct":-33.47,"max_high_30D":390000,"min_low_30D":294500,"max_high_90D":393500,"min_low_90D":294500,"max_high_180D":393500,"min_low_180D":235500,"classification":"counterexample","calibration_usable":true,"current_profile_verdict":"Customer concentration / Europe-Rivian EV demand warning should cap Stage2 unless shipment/revision bridge refreshes.","residual_error_type":"battery_customer_demand_warning_high_mae","evidence_family":"Analyst warning about European/Rivian client demand; subsequent price path showed modest MFE and deep 180D MAE."}
```

## 6. Score-return alignment

### 6.1 LGES — C12 escape hatch

LGES looked like a classic C12 risk headline in July 2024: weaker-than-expected EV demand, reduced revenue target, customers including Tesla/GM/Hyundai, and easing expansion. But the price path did not behave like a hard false positive. Entry was 332,500 on 2024-07-25; the 90D high reached 430,000 and the 180D high reached 435,500, while the observed low was 311,000. This is not a Stage2 block case. It is an escape hatch case: C12 should demand a demand/capacity bridge, but it should not automatically hard-block a diversified large battery producer if ESS or diversified customer visibility keeps the path alive.

### 6.2 SKIET — separator customer-pull failure

SKIET is the cleanest C12 counterexample in this loop. The May 2024 report framed SKIET as a separator asset that might be sold as SK Innovation restructured its battery business under weakening EV demand. Entry was 57,600 on 2024-05-16. The forward path produced almost no MFE and a large drawdown: low 42,700 in the first month, 30,950 inside the 90D window, and 24,350 in the extended forward path. This is what C12 is supposed to catch: the market hears "battery separator / customer exposure," but the underlying customer pull-through is weakening.

### 6.3 Samsung SDI — client mix demand warning

Samsung SDI is not a new C12 symbol in the repository index, but this trigger family is useful because it converts a general "EV demand weak" label into client-mix stress: Europe-heavy EV battery demand and Rivian-related cylindrical battery shipment caution. Entry was 354,000 on 2024-06-28. The forward high was only 393,500 while the 180D low reached 235,500. This supports a C12 rule that customer-contract warnings should cap Stage2 until actual shipment/revision bridge refreshes.

## 7. Shadow rule candidate

```text
rule_id = C12_CUSTOMER_CALLOFF_RISK_STAGE2_CAP

if canonical_archetype_id == C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK
and trigger_type == Stage2
and (
    customer_demand_warning == true
    or capacity_expansion_delay == true
    or customer_calloff_or_shipment_reduction == true
)
and company_specific_revenue_margin_cash_bridge_refreshed == false:
    stage2_actionable_bonus = 0
    max_stage = Stage2-Watch
    local_4b_watch = true
```

Escape hatch:

```text
if diversified_customer_base == true
and ESS_or_non_EV_conversion_bridge == true
and MFE_90D_pct >= +20
and MAE_90D_pct > -10:
    do_not_hard_block_stage2 = true
    keep_as_positive_control = true
```

High-MAE block:

```text
if MFE_90D_pct < +5
and MAE_90D_pct <= -25:
    classify_as_C12_customer_calloff_false_stage2
```

## 8. Residual contribution summary

```text
new_independent_case_count = 3
reused_case_count_within_C12 = 1
same_archetype_new_symbol_count_visible_index_basis = 2
same_archetype_new_trigger_family_count = 3
calibration_usable_case_count = 3
calibration_usable_trigger_count = 3
positive_control_count = 1
counterexample_count = 2
current_profile_error_count = 2
loop_contribution_label = canonical_archetype_rule_candidate
new_axis_proposed = null
existing_axis_strengthened = C12_customer_calloff_stage2_cap; C12_separator_customer_pull_high_MAE_guard; C12_escape_hatch_for_diversified_customer_ESS_bridge
do_not_propose_new_weight_delta = false
```

## 9. Deferred Coding Agent Handoff Prompt

Do not execute this section in the research run.

```text
You are a coding agent working in Songdaiki/stock_agent after the v12 research batch has been collected.

Read this MD as one candidate C12 residual research artifact only. Do not change production scoring directly unless the batch promotion planner approves it.

Extract the three trigger rows from the JSONL block. Validate:
- price_source == Songdaiki/stock-web
- price_basis == tradable_raw
- price_adjustment_status == raw_unadjusted_marcap
- all MFE/MAE 30/90/180 fields exist
- trigger_type is canonical stage label
- no duplicate row by symbol + canonical_archetype_id + trigger_type + entry_date + evidence family

Candidate shadow axis:
C12_CUSTOMER_CALLOFF_RISK_STAGE2_CAP

Promotion should require aggregation across additional C12 rows and should preserve the LGES escape hatch, so the rule does not over-block diversified large-cap battery producers with real ESS/customer-mix mitigation.
```

## 10. Completion state

```text
completed_round = R3
completed_loop = 99
selection_basis = docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket = Priority 0
next_recommended_archetypes = C13_BATTERY_JV_UTILIZATION_AMPC_IRA, C16_STRATEGIC_RESOURCE_POLICY_SUPPLY, C17_CHEMICAL_COMMODITY_MARGIN_SPREAD, R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL
round_schedule_status = coverage_index_selected
round_sector_consistency = pass
```
