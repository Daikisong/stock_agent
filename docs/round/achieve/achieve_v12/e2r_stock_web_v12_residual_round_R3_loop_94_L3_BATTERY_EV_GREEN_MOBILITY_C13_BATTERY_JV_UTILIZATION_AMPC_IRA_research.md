# E2R Stock-Web v12 Residual Research — R3 / Loop 94

```yaml
scheduled_round: R3
scheduled_loop: 94
large_sector_id: L3_BATTERY_EV_GREEN_MOBILITY
canonical_archetype_id: C13_BATTERY_JV_UTILIZATION_AMPC_IRA
fine_archetype_id: SEPARATOR_CNT_PRECURSOR_CUSTOMER_CAPACITY_UTILIZATION_AMPC_IRA_BRIDGE_VS_BATTERY_LABEL_BETA

research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
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

new_independent_case_count: 3
same_archetype_new_symbol_count: 3
positive_case_count: 1
counterexample_count: 2
watch_or_cap_case_count: 1
local_4b_overlay_case_count: 2
hard_4c_candidate_count: 1
calibration_usable_trigger_count: 3

loop_contribution_label: residual_error_found
canonical_archetype_rule_candidate: true
do_not_propose_new_weight_delta: true

completed_round: R3
completed_loop: 94
next_round: R4
next_loop: 94
round_schedule_status: valid
round_sector_consistency: pass
```

---

## 1. Schedule resolution

Previous completed file in the active sequence was:

```text
e2r_stock_web_v12_residual_round_R2_loop_94_L2_AI_SEMICONDUCTOR_ELECTRONICS_C06_HBM_MEMORY_CUSTOMER_CAPACITY_research.md
```

Under v12:

```text
R1 -> R2 -> R3 -> R4 -> R5 -> R6 -> R7 -> R8 -> R9 -> R10 -> R11 -> R12 -> R13 -> R1
```

Therefore:

```text
scheduled_round = R3
scheduled_loop = 94
large_sector_id = L3_BATTERY_EV_GREEN_MOBILITY
```

R3 hard gate requires:

```text
large_sector_id = L3_BATTERY_EV_GREEN_MOBILITY
```

Recent R3 branch usage:

```text
loop90: C13_BATTERY_JV_UTILIZATION_AMPC_IRA
loop91: C11_BATTERY_ORDERBOOK_RERATING
loop92: C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK
loop93: C14_EV_DEMAND_SLOWDOWN_4B_4C
```

This run returns to C13, but avoids the top-covered C13 names and uses a different fine branch:

```text
separator / CNT conductive additive / precursor customer-capacity
utilization and AMPC/IRA economics
vs generic battery-label beta
```

---

## 2. No-repeat / novelty check

No-Repeat Index coverage snapshot:

```text
C13_BATTERY_JV_UTILIZATION_AMPC_IRA
rows: 23
symbols: 16
date_range: 2023-01-31~2024-07-16
good/bad S2: 9/2
4B/4C: 2/0
URL pending/proxy: 10/10
top covered symbols:
  005070(3), 020150(3), 003670(2), 025900(2), 348370(2), 002710(1)
```

Selected symbols:

```text
121600 나노신소재
393890 더블유씨피
450080 에코프로머티
```

They avoid the C13 top-covered symbols and avoid the most recent R3 loop92~93 names:

```text
loop92 avoid: 078600, 066970, 361610
loop93 avoid: 014820, 336370, 222080
```

Hard duplicate key:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

Novelty classification:

```text
121600: same archetype, new symbol, CNT conductive additive / customer ramp local-positive with 4B after later MAE
393890: same archetype, new symbol, separator utilization/customer-capacity label hard-4C without demand survival
450080: same archetype, new symbol, precursor / IRA-supply-chain local burst then high-MAE 4B failure
```

---

## 3. Price-atlas validation

Manifest fields checked from stock-web:

```text
source_name: FinanceData/marcap
source_repo_url: https://github.com/FinanceData/marcap
price_adjustment_status: raw_unadjusted_marcap
min_date: 1995-05-02
max_date: 2026-02-20
tradable_row_count: 14,354,401
raw_row_count: 15,214,118
symbol_count: 5,414
active_like_symbol_count: 2,868
inactive_or_delisted_like_symbol_count: 2,546
markets: KONEX, KOSDAQ, KOSDAQ GLOBAL, KOSPI
calibration_shard_root: atlas/ohlcv_tradable_by_symbol_year
raw_shard_root: atlas/ohlcv_raw_by_symbol_year
schema_path: atlas/schema.json
universe_path: atlas/universe/all_symbols.csv
```

Profile checks:

```text
121600 나노신소재
  profile: atlas/symbol_profiles/121/121600.json
  first_date: 2011-02-09
  last_date: 2026-02-20
  market: KOSDAQ
  tradable_ohlcv rows: 3,697
  corporate_action_candidate_dates:
    2015-12-17
  2024 entry~D+180 contamination: none

393890 더블유씨피
  profile: atlas/symbol_profiles/393/393890.json
  first_date: 2022-09-30
  last_date: 2026-02-20
  market:
    KOSDAQ until 2024-06-13
    KOSDAQ GLOBAL from 2024-06-14
  tradable_ohlcv rows: 827
  corporate_action_candidate_dates: none
  2024 entry~D+180 contamination: none

450080 에코프로머티
  profile: atlas/symbol_profiles/450/450080.json
  first_date: 2023-11-17
  last_date: 2026-02-20
  market: KOSPI
  tradable_ohlcv rows: 548
  corporate_action_candidate_dates: none
  2024 entry~D+180 contamination: none
```

---

## 4. Archetype residual problem

C13 is about battery JV utilization, AMPC/IRA economics, and customer capacity reaching the company. It is not a generic "battery supply chain is hot" label.

The model can over-score:

```text
IRA / AMPC / US supply-chain label
battery JV utilization headline
separator / CNT / precursor label
customer-capacity ramp hope
one-week battery-material volume spike
```

The bridge must be stricter:

```text
policy or customer-capacity event
  -> named customer or JV utilization
  -> offtake / supply slot / delivery schedule
  -> AMPC or IRA economic capture
  -> utilization and fixed-cost absorption
  -> ASP / mix / margin bridge
  -> inventory and working-capital risk
  -> price survival after the first battery-theme spike
```

A C13 battery story is like a factory receiving a subsidy map. The map matters only if the line actually runs, the customer pulls volume, the plant absorbs fixed cost, and the subsidy or margin reaches the income statement.

---

## 5. Case 1 — 121600 나노신소재

```yaml
case_id: C13_R3L94_121600_2024_02_21
symbol: "121600"
name: "나노신소재"
canonical_archetype_id: C13_BATTERY_JV_UTILIZATION_AMPC_IRA
fine_archetype_id: SEPARATOR_CNT_PRECURSOR_CUSTOMER_CAPACITY_UTILIZATION_AMPC_IRA_BRIDGE_VS_BATTERY_LABEL_BETA
trigger_date: 2024-02-21
entry_date: 2024-02-21
entry_price_basis: close
entry_price: 134000
classification: local_positive_cnt_conductive_additive_customer_capacity_ramp_with_4b_watch
calibration_usable: true
```

### Evidence interpretation

나노신소재 is the constructive control, but with strong 4B discipline.

The useful C13 read is:

```text
CNT conductive additive relevance
  -> battery customer capacity ramp
  -> high initial price confirmation
  -> later need for utilization, customer pull, and margin evidence
```

The forward path delivered immediate and meaningful MFE. But the later drawdown was large, so this is not an unrestricted Green. It is a positive local entry that needs 4B once customer-volume and margin evidence stops refreshing.

### Price path

Key Stock-Web rows:

```text
2024-02-21: high 136,300 / close 134,000
2024-02-22: high 157,800 / close 138,000
2024-03-18: high 151,000 / close 147,600
2024-04-17: low 111,000 / close 111,300
2024-08-05: low 68,500 / close 74,900
2024-09-27: high 97,700 / close 94,900
2024-10-08: high 99,600 / close 97,800
```

Approximate path from entry close:

```text
entry_close: 134,000
peak_high: 157,800
MFE: +17.8%
worst_low_after_entry: 68,500
MAE: -48.9%
```

### Interpretation

This is a C13 local positive with 4B:

```text
Stage2-Actionable: possible if customer capacity, qualification, shipment, and margin bridge are explicit.
Stage3-Green: blocked without refreshed utilization / customer pull / margin evidence.
Local 4B: required because the initial MFE later became high MAE.
Hard 4C: not the primary label because positive MFE came first.
```

### Stress-test components

```text
raw_component_score_proxy:
  cnt_battery_material_relevance: high
  customer_capacity_bridge: medium_high
  utilization_margin_bridge: weak_to_medium
  local_price_confirmation: medium_high
  post_event_survival: failed
  local_4b_overlay: required
```

---

## 6. Case 2 — 393890 더블유씨피

```yaml
case_id: C13_R3L94_393890_2024_02_21
symbol: "393890"
name: "더블유씨피"
canonical_archetype_id: C13_BATTERY_JV_UTILIZATION_AMPC_IRA
fine_archetype_id: SEPARATOR_CNT_PRECURSOR_CUSTOMER_CAPACITY_UTILIZATION_AMPC_IRA_BRIDGE_VS_BATTERY_LABEL_BETA
trigger_date: 2024-02-21
entry_date: 2024-02-21
entry_price_basis: close
entry_price: 45750
classification: hard_4c_candidate_separator_utilization_customer_capacity_label_without_demand_survival
calibration_usable: true
```

### Evidence interpretation

더블유씨피 is the separator/utilization hard guardrail.

The setup looked plausible:

```text
separator supplier
  -> EV battery customer capacity
  -> IRA/AMPC supply-chain attention
  -> utilization recovery hope
```

But the price path did not validate durable demand or utilization. MFE was shallow, and the later downside was large. This is the classic C13 trap: relevant battery component label without customer pull.

### Price path

Key Stock-Web rows:

```text
2024-02-21: high 46,650 / close 45,750
2024-02-22: high 49,400 / close 47,100
2024-03-07: high 49,500 / close 49,500
2024-04-17: low 29,900 / close 30,000
2024-08-05: low 20,200 / close 20,450
2024-09-10: low 17,210 / close 17,330
2024-10-25: low 15,390 / close 15,510
```

Approximate path from entry close:

```text
entry_close: 45,750
peak_high: 49,500
MFE: +8.2%
worst_low_after_entry: 15,390
MAE: -66.4%
```

### Interpretation

This is a hard C13 false-positive:

```text
Stage2-Watch: possible from separator / customer-capacity relevance.
Stage2-Actionable: blocked unless utilization, offtake, customer call-off, and margin bridge are explicit.
Stage3-Green: blocked.
Hard 4C: yes by shallow MFE and extreme MAE.
```

The lesson is that separator relevance is not utilization economics.

### Stress-test components

```text
raw_component_score_proxy:
  separator_label: high
  ira_supply_chain_relevance: medium_high
  customer_calloff_bridge: weak
  utilization_margin_bridge: weak
  price_confirmation: shallow
  drawdown_penalty: extreme
  hard_4c_guard: yes
```

---

## 7. Case 3 — 450080 에코프로머티

```yaml
case_id: C13_R3L94_450080_2024_02_01
symbol: "450080"
name: "에코프로머티"
canonical_archetype_id: C13_BATTERY_JV_UTILIZATION_AMPC_IRA
fine_archetype_id: SEPARATOR_CNT_PRECURSOR_CUSTOMER_CAPACITY_UTILIZATION_AMPC_IRA_BRIDGE_VS_BATTERY_LABEL_BETA
trigger_date: 2024-02-01
entry_date: 2024-02-01
entry_price_basis: close
entry_price: 173600
classification: local_burst_precursor_ira_supply_chain_label_with_high_mae_4b_failure
calibration_usable: true
```

### Evidence interpretation

에코프로머티 is the precursor / IRA supply-chain local-burst case.

The first price move worked:

```text
precursor / cathode supply-chain relevance
  -> IRA and supply-chain localization sympathy
  -> early strong MFE
```

But the move did not survive. The later path shows why C13 should not keep Green open unless customer volume, utilization, and margin conversion are refreshed.

### Price path

Key Stock-Web rows:

```text
2024-02-01: close 173,600
2024-02-13: high 209,500 / close 209,500
2024-02-14: high 211,500 / close 200,000
2024-03-28: low 133,100 / close 133,600
2024-04-17: low 103,800 / close 104,200
2024-05-03: low 109,300 / close 109,800
```

Approximate path from entry close:

```text
entry_close: 173,600
peak_high: 211,500
MFE: +21.8%
worst_low_after_entry: 103,800
MAE: -40.2%
```

### Interpretation

This is a local-burst / 4B-failure C13 case:

```text
Stage2-Watch: valid from precursor / IRA supply-chain relevance.
Stage2-Actionable: possible only when customer capacity, shipment, utilization, and margin bridge are explicit.
Stage3-Green: blocked after the high-MAE reversal.
Local 4B: required after +20% MFE followed by -40% MAE.
Hard 4C: not primary for the original entry because meaningful MFE came first.
```

### Stress-test components

```text
raw_component_score_proxy:
  precursor_supply_chain_relevance: high
  ira_ampc_policy_relevance: medium_high
  customer_capacity_bridge: medium
  utilization_margin_bridge: weak_to_medium
  price_confirmation: high_initial
  post_burst_survival: failed
  local_4b_overlay: required
```

---

## 8. Aggregate calibration takeaways

```text
positive_case_count: 1
counterexample_count: 2
watch_or_cap_case_count: 1
local_4b_overlay_case_count: 2
hard_4c_candidate_count: 1
calibration_usable_trigger_count: 3
```

The three-case C13 grid:

```text
121600 나노신소재:
  CNT conductive-additive customer-capacity local positive;
  meaningful MFE came first, but later high MAE requires 4B.

393890 더블유씨피:
  separator/customer-capacity relevance failed badly;
  shallow MFE and extreme MAE, hard 4C.

450080 에코프로머티:
  precursor/IRA supply-chain local burst;
  meaningful MFE came first, but later high MAE requires 4B.
```

Shared rule:

```text
C13 is not "battery component label."
C13 is "customer capacity, JV utilization, AMPC/IRA economics, shipment, and margin actually reach this company's income statement."
```

---

## 9. Machine-readable JSONL rows

```jsonl
{"row_type":"case","case_id":"C13_R3L94_121600_2024_02_21","scheduled_round":"R3","scheduled_loop":94,"large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C13_BATTERY_JV_UTILIZATION_AMPC_IRA","fine_archetype_id":"SEPARATOR_CNT_PRECURSOR_CUSTOMER_CAPACITY_UTILIZATION_AMPC_IRA_BRIDGE_VS_BATTERY_LABEL_BETA","symbol":"121600","name":"나노신소재","trigger_date":"2024-02-21","entry_date":"2024-02-21","entry_price":134000,"peak_high":157800,"peak_date":"2024-02-22","worst_low_after_entry":68500,"worst_low_after_entry_date":"2024-08-05","mfe_pct":17.8,"mae_pct":-48.9,"classification":"local_positive_cnt_conductive_additive_customer_capacity_ramp_with_4b_watch","calibration_usable":true,"evidence_family":"cnt_conductive_additive_customer_capacity_ramp_without_refreshed_utilization_margin_bridge","residual_error":"battery_material_local_mfe_can_fail_green_without_customer_pull_and_margin_refresh","shadow_rule_candidate":"preserve_local_positive_but_attach_4b_after_high_mae_when_customer_utilization_bridge_missing"}
{"row_type":"case","case_id":"C13_R3L94_393890_2024_02_21","scheduled_round":"R3","scheduled_loop":94,"large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C13_BATTERY_JV_UTILIZATION_AMPC_IRA","fine_archetype_id":"SEPARATOR_CNT_PRECURSOR_CUSTOMER_CAPACITY_UTILIZATION_AMPC_IRA_BRIDGE_VS_BATTERY_LABEL_BETA","symbol":"393890","name":"더블유씨피","trigger_date":"2024-02-21","entry_date":"2024-02-21","entry_price":45750,"peak_high":49500,"peak_date":"2024-03-07","worst_low_after_entry":15390,"worst_low_after_entry_date":"2024-10-25","mfe_pct":8.2,"mae_pct":-66.4,"classification":"hard_4c_candidate_separator_utilization_customer_capacity_label_without_demand_survival","calibration_usable":true,"evidence_family":"separator_customer_capacity_utilization_label_without_calloff_margin_bridge","residual_error":"separator_relevance_can_overpromote_without_customer_calloff_and_utilization_economics","shadow_rule_candidate":"route_separator_customer_capacity_label_to_hard_4c_if_mfe_shallow_mae_extreme_and_utilization_bridge_missing"}
{"row_type":"case","case_id":"C13_R3L94_450080_2024_02_01","scheduled_round":"R3","scheduled_loop":94,"large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C13_BATTERY_JV_UTILIZATION_AMPC_IRA","fine_archetype_id":"SEPARATOR_CNT_PRECURSOR_CUSTOMER_CAPACITY_UTILIZATION_AMPC_IRA_BRIDGE_VS_BATTERY_LABEL_BETA","symbol":"450080","name":"에코프로머티","trigger_date":"2024-02-01","entry_date":"2024-02-01","entry_price":173600,"peak_high":211500,"peak_date":"2024-02-14","worst_low_after_entry":103800,"worst_low_after_entry_date":"2024-04-17","mfe_pct":21.8,"mae_pct":-40.2,"classification":"local_burst_precursor_ira_supply_chain_label_with_high_mae_4b_failure","calibration_usable":true,"evidence_family":"precursor_ira_supply_chain_local_burst_without_utilization_margin_survival","residual_error":"ira_supply_chain_label_can_create_local_burst_but_fail_green_without_customer_volume_and_margin","shadow_rule_candidate":"classify_precursor_ira_bursts_with_meaningful_mfe_then_high_mae_as_local_4b_not_green"}
```

```jsonl
{"row_type":"aggregate","scheduled_round":"R3","scheduled_loop":94,"large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C13_BATTERY_JV_UTILIZATION_AMPC_IRA","fine_archetype_id":"SEPARATOR_CNT_PRECURSOR_CUSTOMER_CAPACITY_UTILIZATION_AMPC_IRA_BRIDGE_VS_BATTERY_LABEL_BETA","case_count":3,"positive_case_count":1,"counterexample_count":2,"watch_or_cap_case_count":1,"local_4b_overlay_case_count":2,"hard_4c_candidate_count":1,"calibration_usable_trigger_count":3,"loop_contribution_label":"residual_error_found","do_not_propose_new_weight_delta":true}
{"row_type":"shadow_rule","scheduled_round":"R3","scheduled_loop":94,"canonical_archetype_id":"C13_BATTERY_JV_UTILIZATION_AMPC_IRA","rule_id":"C13_CUSTOMER_UTILIZATION_AMPC_MARGIN_BRIDGE_REQUIRED","rule_type":"canonical_archetype_specific_guard","rule_text":"For C13, do not open Stage2-Actionable or Stage3-Green from IRA/AMPC, battery JV, separator, CNT, precursor, customer-capacity ramp, or one-week battery-material volume spike labels alone. Require named customer or JV utilization, offtake or supply slot, delivery/call-off schedule, AMPC/IRA economic capture, utilization and fixed-cost absorption, ASP/mix/margin bridge, inventory/working-capital risk check, and post-trigger price survival. Battery-material names with meaningful MFE followed by high MAE should remain local 4B unless fresh customer pull and utilization evidence appears. Separator names with shallow MFE and extreme MAE should route to hard-4C when call-off and utilization bridge are missing. Precursor/IRA supply-chain bursts with high MAE should be capped as local 4B rather than Green.","expected_effect":"Reduce battery component and IRA/AMPC label false positives while preserving true customer-utilization positives with demand, shipment, subsidy, and margin evidence.","production_scoring_changed":false,"shadow_weight_only":true}
{"row_type":"residual_contribution","scheduled_round":"R3","scheduled_loop":94,"canonical_archetype_id":"C13_BATTERY_JV_UTILIZATION_AMPC_IRA","residual_type":"battery_customer_utilization_ampc_margin_guard","contribution":"Adds one CNT local-positive 4B case, one separator hard-4C case, and one precursor/IRA local-burst 4B failure to calibrate C13 customer utilization and margin requirements.","do_not_count_as_global_weight_delta":true}
```

---

## 10. Proposed canonical-archetype shadow rule

```text
C13_CUSTOMER_UTILIZATION_AMPC_MARGIN_BRIDGE_REQUIRED

IF canonical_archetype_id == C13_BATTERY_JV_UTILIZATION_AMPC_IRA:

  Do not open Stage3-Green from:
    - IRA / AMPC policy label alone
    - battery JV label alone
    - separator / CNT / precursor label alone
    - customer-capacity ramp hope alone
    - one-week battery-material volume spike alone

  Require at least two of:
    - named customer or JV utilization
    - offtake / supply slot / call-off schedule
    - delivery timing
    - AMPC / IRA economic capture
    - utilization / fixed-cost absorption
    - ASP / mix / margin bridge
    - inventory / working-capital risk containment
    - low-MAE post-trigger price survival
    - fresh evidence after the battery-policy headline

  If MFE < 10% and MAE < -40%:
    route to C13 hard-4C candidate.

  If MFE > 15% but later MAE < -35%:
    preserve as local 4B / event burst, not Green, unless fresh customer-utilization and margin evidence appears.

  If MFE is meaningful but the bridge is not refreshed:
    attach 4B rather than keeping Stage3-Green open.

  Distinguish:
    - components where named customer capacity becomes call-off, shipment, utilization, and margin
    - from generic separator/CNT/precursor labels where EV-demand slowdown breaks utilization.
```

---

## 11. Deferred Coding Agent Handoff Prompt

```text
You are a coding agent working on Songdaiki/stock_agent.

Do not treat this research MD as production scoring by itself.
Batch it with other v12 residual research files.

Source file:
e2r_stock_web_v12_residual_round_R3_loop_94_L3_BATTERY_EV_GREEN_MOBILITY_C13_BATTERY_JV_UTILIZATION_AMPC_IRA_research.md

Task:
1. Parse machine-readable JSONL rows.
2. Add the three C13 battery JV/utilization/AMPC cases to calibration research ingestion.
3. Preserve production_scoring_changed=false.
4. Treat the proposed rule only as a shadow canonical-archetype guard candidate:
   C13_CUSTOMER_UTILIZATION_AMPC_MARGIN_BRIDGE_REQUIRED.
5. Do not change global weights directly.
6. Compare against existing C13 cases and deduplicate by:
   canonical_archetype_id + symbol + trigger_type + entry_date.
7. If enough C13 cases agree, consider implementing a canonical guard that:
   - blocks battery component/AMPC Green without customer utilization, call-off, shipment, and margin bridge,
   - preserves CNT/precursor local positives only with refreshed customer evidence,
   - attaches local 4B after meaningful MFE followed by high MAE,
   - routes shallow-MFE/high-MAE separator labels to hard-4C.

Expected next schedule:
completed_round = R3
completed_loop = 94
next_round = R4
next_loop = 94
round_schedule_status = valid
round_sector_consistency = pass
```

---

## 12. Required round-state footer

```text
completed_round = R3
completed_loop = 94
next_round = R4
next_loop = 94
round_schedule_status = valid
round_sector_consistency = pass
```
