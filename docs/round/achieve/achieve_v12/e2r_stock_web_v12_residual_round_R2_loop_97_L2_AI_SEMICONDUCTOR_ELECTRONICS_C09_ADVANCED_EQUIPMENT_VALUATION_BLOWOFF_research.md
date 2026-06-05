# E2R Stock-Web v12 Residual Research — R2 / Loop 97

```yaml
scheduled_round: R2
scheduled_loop: 97
large_sector_id: L2_AI_SEMICONDUCTOR_ELECTRONICS
canonical_archetype_id: C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF
fine_archetype_id: ADVANCED_SEMI_EQUIPMENT_ALD_CVD_VACUUM_PROCESS_VALUATION_BLOWOFF_ORDER_MARGIN_BRIDGE_VS_EQUIPMENT_LABEL_LATE_CHASE

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
local_4b_overlay_case_count: 1
hard_4c_candidate_count: 1
advanced_deposition_equipment_case_count: 2
vacuum_process_equipment_case_count: 1
valuation_blowoff_case_count: 2
customer_order_margin_bridge_missing_count: 2
corporate_action_caveat_outside_window_count: 3
market_segment_caveat_count: 2
calibration_usable_trigger_count: 3

loop_contribution_label: residual_error_found
canonical_archetype_rule_candidate: true
do_not_propose_new_weight_delta: true

completed_round: R2
completed_loop: 97
next_round: R3
next_loop: 97
round_schedule_status: valid
round_sector_consistency: pass
```

---

## 1. Schedule resolution

Previous completed file in the active sequence was:

```text
e2r_stock_web_v12_residual_round_R1_loop_97_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY_research.md
```

Under v12:

```text
R1 -> R2 -> R3 -> R4 -> R5 -> R6 -> R7 -> R8 -> R9 -> R10 -> R11 -> R12 -> R13 -> R1
```

Therefore:

```text
scheduled_round = R2
scheduled_loop = 97
large_sector_id = L2_AI_SEMICONDUCTOR_ELECTRONICS
```

R2 hard gate requires:

```text
large_sector_id = L2_AI_SEMICONDUCTOR_ELECTRONICS
```

Recent R2 branch usage:

```text
loop93: C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE
loop94: C06_HBM_MEMORY_CUSTOMER_CAPACITY
loop95: C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH
loop96: C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY
```

This run returns to C09 after the R2 branch cycle, but avoids the C09 top-covered names and uses a different fine branch:

```text
advanced deposition / thermal / vacuum / process equipment
customer order, capacity, utilization, valuation, and margin bridge
vs generic semiconductor-equipment label late chase
```

---

## 2. No-repeat / novelty check

No-Repeat Index coverage snapshot:

```text
C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF
rows: 17
symbols: 11
date_range: 2023-07-14~2024-09-24
good/bad S2: 7/3
4B/4C: 1/0
URL pending/proxy: 7/7
top covered symbols:
  322310(3), 348210(3), 089030(2), 140860(2), 031980(1), 064290(1)
```

Selected symbols:

```text
084370 유진테크
036930 주성엔지니어링
083310 엘오티베큠
```

They avoid the C09 top-covered list and avoid recent R2 loop95~96 names:

```text
loop96 C08 avoid: 092870, 067310, 097800
loop95 C07 avoid: 039030, 083450, 095610
C09 top-covered avoid: 322310, 348210, 089030, 140860, 031980, 064290
```

Hard duplicate key:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

Novelty classification:

```text
084370: same archetype, new symbol, deposition/thermal equipment positive with Green cap after large MFE
036930: same archetype, new symbol, ALD/CVD advanced-equipment rerating local 4B failure after valuation blowoff
083310: same archetype, new symbol, vacuum/process-equipment label hard-4C after shallow MFE and large MAE
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
084370 유진테크
  profile: atlas/symbol_profiles/084/084370.json
  first_date: 2006-01-17
  last_date: 2026-02-20
  market:
    KOSDAQ base market
    KOSDAQ GLOBAL segment from 2022-11-21 to 2024-06-13
  tradable_ohlcv rows: 4,955
  corporate_action_candidate_dates:
    2007-05-17, 2010-01-22, 2012-06-07
  2024 entry~D+180 contamination: none
  caveat:
    older corporate-action candidates are outside selected 2024 validation window.
    KOSDAQ GLOBAL segment ended in 2024, but there is no raw-price discontinuity candidate inside the entry window.

036930 주성엔지니어링
  profile: atlas/symbol_profiles/036/036930.json
  name history:
    주성엔지니어 until 2008-01-10
    주성엔지니어링 from 2008-01-11
  market:
    KOSDAQ until 2022-11-18
    KOSDAQ GLOBAL from 2022-11-21
  tradable_ohlcv rows: 6,444
  non_tradable_zero_volume rows: 1
  corporate_action_candidate_dates:
    2000-06-22
  2024 entry~D+180 contamination: none
  caveat:
    old raw-discontinuity caveat exists outside selected 2024 validation window.

083310 엘오티베큠
  profile: atlas/symbol_profiles/083/083310.json
  first_date: 2005-10-05
  last_date: 2026-02-20
  market: KOSDAQ
  tradable_ohlcv rows: 5,028
  corporate_action_candidate_dates:
    2007-05-29, 2007-06-19
  2024 entry~D+180 contamination: none
  caveat:
    old corporate-action candidates are outside selected 2024 validation window.
```

---

## 4. Archetype residual problem

C09 is about advanced semiconductor equipment valuation blowoff risk. It is not a generic "semiconductor equipment stock" archetype.

The model can over-score:

```text
advanced semiconductor equipment label
ALD / CVD / deposition / thermal process label
vacuum equipment / process infrastructure label
AI / HBM / advanced-node readthrough
customer capex recovery headline
one-week equipment-stock volume spike
late chase after equipment rerating
```

The C09 bridge must be stricter:

```text
advanced equipment event
  -> named customer, process step, tool type, or fab-node relevance
  -> order visibility or purchase order
  -> delivery / installation / acceptance schedule
  -> utilization and customer capex phase
  -> ASP / mix / service revenue
  -> component, logistics, and warranty cost
  -> margin / OP conversion
  -> valuation discipline after the first equipment-label spike
  -> price survival after the blowoff window
```

A C09 equipment thesis is like a tool moving into a cleanroom. The label says the fab needs advanced tools, but C09 asks whether this exact tool is ordered, delivered, accepted, used, serviced, and paid for at margin rather than merely admired through a valuation lens.

---

## 5. Case 1 — 084370 유진테크

```yaml
case_id: C09_R2L97_084370_2024_03_21
symbol: "084370"
name: "유진테크"
canonical_archetype_id: C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF
fine_archetype_id: ADVANCED_SEMI_EQUIPMENT_ALD_CVD_VACUUM_PROCESS_VALUATION_BLOWOFF_ORDER_MARGIN_BRIDGE_VS_EQUIPMENT_LABEL_LATE_CHASE
trigger_date: 2024-03-21
entry_date: 2024-03-21
entry_price_basis: close
entry_price: 41450
classification: positive_deposition_thermal_equipment_order_margin_bridge_with_green_cap_after_large_mfe
calibration_usable: true
```

### Evidence interpretation

유진테크 is the constructive C09 control in this set.

The useful C09 read is not simply:

```text
반도체 장비주가 강하다
```

It is:

```text
deposition / thermal process equipment relevance
  -> customer capex and process-step readthrough
  -> order and delivery optionality
  -> strong price confirmation into May
  -> valuation cap after large rerating
```

The forward path produced a large MFE and did not immediately enter a hard-failure drawdown from the selected March entry. This preserves positive classification. Still, C09 should cap Green unless the order, delivery, customer acceptance, and margin bridge is current.

### Price path

Key Stock-Web rows:

```text
2024-03-21: high 41,900 / close 41,450
2024-03-29: high 44,700 / close 44,000
2024-04-08: high 52,600 / close 50,200
2024-04-17: high 54,900 / close 52,100
2024-05-07: high 58,700 / close 57,600
2024-08-05: low 37,400 / close 38,800
2024-09-11: low 35,350 / close 35,500
2024-10-18: low 34,250 / close 34,600
```

Approximate path from entry close:

```text
entry_close: 41,450
peak_high: 58,700
MFE: +41.6%
worst_low_after_entry: 34,250
MAE: -17.4%
```

### Interpretation

This is a C09 positive with Green cap:

```text
Stage2-Actionable: possible if customer/process, order, delivery, and margin bridge are explicit.
Stage3-Green: blocked unless fresh tool order, customer acceptance, and OP/margin evidence appears.
Local 4B: monitor after +40% MFE if evidence becomes stale.
Hard 4C: no.
```

### Stress-test components

```text
raw_component_score_proxy:
  deposition_thermal_equipment_relevance: high
  customer_process_bridge: medium_high
  order_delivery_bridge: medium_high
  valuation_blowoff_risk: medium
  margin_op_bridge: medium
  price_confirmation: high
  drawdown_penalty: medium
  green_cap: required_after_large_mfe
```

---

## 6. Case 2 — 036930 주성엔지니어링

```yaml
case_id: C09_R2L97_036930_2024_02_22
symbol: "036930"
name: "주성엔지니어링"
canonical_archetype_id: C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF
fine_archetype_id: ADVANCED_SEMI_EQUIPMENT_ALD_CVD_VACUUM_PROCESS_VALUATION_BLOWOFF_ORDER_MARGIN_BRIDGE_VS_EQUIPMENT_LABEL_LATE_CHASE
trigger_date: 2024-02-22
entry_date: 2024-02-22
entry_price_basis: close
entry_price: 31900
classification: local_burst_ald_cvd_advanced_equipment_rerating_high_mae_4b_failure
calibration_usable: true
```

### Evidence interpretation

주성엔지니어링 is the advanced-equipment local-burst / 4B failure.

The setup had real C09 relevance:

```text
ALD / CVD / advanced deposition equipment
  -> AI/HBM and advanced-node capex readthrough
  -> rapid valuation rerating into late February and early April
  -> meaningful MFE
```

The forward path produced a tradable MFE, so the original trigger is not a pure hard-4C. But the later path failed price survival and crossed the high-MAE zone. This should be local 4B, not Green, unless customer order and margin evidence keeps refreshing.

### Price path

Key Stock-Web rows:

```text
2024-02-22: high 33,050 / close 31,900
2024-02-28: high 40,750 / close 40,000
2024-04-08: high 41,450 / close 36,500
2024-04-19: low 31,950 / close 33,250
2024-08-05: low 22,150 / close 23,200
2024-09-09: low 22,050 / close 22,700
2024-10-29: high 31,050 / close 31,050
```

Approximate path from entry close:

```text
entry_close: 31,900
peak_high: 41,450
MFE: +29.9%
worst_low_after_entry: 22,050
MAE: -30.9%
```

### Interpretation

This is a C09 local burst / 4B failure:

```text
Stage2-Watch: valid from ALD/CVD advanced-equipment relevance.
Stage2-Actionable: possible only if customer order, fab capex phase, delivery/acceptance, and margin bridge are explicit.
Stage3-Green: blocked after later high-MAE reversal.
Local 4B: required.
Hard 4C: not primary for the original entry because meaningful MFE came first.
```

### Stress-test components

```text
raw_component_score_proxy:
  ald_cvd_equipment_relevance: high
  ai_hbm_capex_readthrough: medium_high
  customer_order_bridge: weak_to_medium
  delivery_acceptance_bridge: weak_to_medium
  valuation_blowoff_risk: high
  price_confirmation: high_initial
  post_blowoff_survival: failed
  local_4b_overlay: required
```

---

## 7. Case 3 — 083310 엘오티베큠

```yaml
case_id: C09_R2L97_083310_2024_02_22
symbol: "083310"
name: "엘오티베큠"
canonical_archetype_id: C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF
fine_archetype_id: ADVANCED_SEMI_EQUIPMENT_ALD_CVD_VACUUM_PROCESS_VALUATION_BLOWOFF_ORDER_MARGIN_BRIDGE_VS_EQUIPMENT_LABEL_LATE_CHASE
trigger_date: 2024-02-22
entry_date: 2024-02-22
entry_price_basis: close
entry_price: 23350
classification: hard_4c_candidate_vacuum_process_equipment_label_without_customer_order_margin_survival
calibration_usable: true
```

### Evidence interpretation

엘오티베큠 is the vacuum/process-equipment hard guardrail.

The label can fool the model:

```text
vacuum equipment / process infrastructure
  -> semiconductor capex recovery
  -> advanced-equipment sympathy
  -> one-day equipment-stock volume spike
```

But from the selected close, incremental MFE was shallow while the later drawdown was severe. The bridge from vacuum/process-equipment relevance to named customer order, delivery schedule, utilization, service revenue, and margin was not proven.

### Price path

Key Stock-Web rows:

```text
2024-02-22: high 23,450 / close 23,350
2024-02-23: high 24,450 / close 22,400
2024-03-08: high 24,050 / close 23,500
2024-04-17: low 20,250 / close 21,050
2024-08-05: low 9,880 / close 10,200
2024-09-09: low 9,810 / close 10,280
2024-10-25: low 9,340 / close 9,340
```

Approximate path from entry close:

```text
entry_close: 23,350
peak_high: 24,450
MFE: +4.7%
worst_low_after_entry: 9,300
MAE: -60.2%
```

### Interpretation

This is a hard C09 false-positive:

```text
Stage2-Watch: possible from vacuum/process-equipment relevance.
Stage2-Actionable: blocked unless named customer, order, delivery/acceptance, service revenue, and margin bridge are explicit.
Stage3-Green: blocked.
Hard 4C: yes by shallow MFE and severe MAE.
```

The lesson is that process-equipment sympathy is not customer-order margin survival.

### Stress-test components

```text
raw_component_score_proxy:
  vacuum_process_equipment_label: high
  capex_recovery_readthrough: medium_high
  customer_order_bridge: weak
  delivery_acceptance_bridge: weak
  service_margin_bridge: weak
  price_confirmation_after_entry: shallow
  drawdown_penalty: extreme
  hard_4c_guard: yes
```

---

## 8. Aggregate calibration takeaways

```text
positive_case_count: 1
counterexample_count: 2
watch_or_cap_case_count: 1
local_4b_overlay_case_count: 1
hard_4c_candidate_count: 1
advanced_deposition_equipment_case_count: 2
vacuum_process_equipment_case_count: 1
valuation_blowoff_case_count: 2
customer_order_margin_bridge_missing_count: 2
corporate_action_caveat_outside_window_count: 3
market_segment_caveat_count: 2
calibration_usable_trigger_count: 3
```

The three-case C09 advanced-equipment grid:

```text
084370 유진테크:
  deposition / thermal equipment positive;
  large MFE and non-hard MAE, but Green requires current order/delivery/margin evidence.

036930 주성엔지니어링:
  ALD/CVD advanced-equipment local burst;
  meaningful MFE first, then high MAE, local 4B failure.

083310 엘오티베큠:
  vacuum/process-equipment label failed;
  shallow MFE and severe MAE, hard 4C.
```

Shared rule:

```text
C09 is not "semiconductor equipment label is advanced."
C09 is "customer process, order, delivery, acceptance, utilization, service revenue, valuation discipline, and margin conversion are visible for this company."
```

---

## 9. Machine-readable JSONL rows

```jsonl
{"row_type":"case","case_id":"C09_R2L97_084370_2024_03_21","scheduled_round":"R2","scheduled_loop":97,"large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF","fine_archetype_id":"ADVANCED_SEMI_EQUIPMENT_ALD_CVD_VACUUM_PROCESS_VALUATION_BLOWOFF_ORDER_MARGIN_BRIDGE_VS_EQUIPMENT_LABEL_LATE_CHASE","symbol":"084370","name":"유진테크","trigger_date":"2024-03-21","entry_date":"2024-03-21","entry_price":41450,"peak_high":58700,"peak_date":"2024-05-07","worst_low_after_entry":34250,"worst_low_after_entry_date":"2024-10-18","mfe_pct":41.6,"mae_pct":-17.4,"classification":"positive_deposition_thermal_equipment_order_margin_bridge_with_green_cap_after_large_mfe","calibration_usable":true,"evidence_family":"deposition_thermal_equipment_customer_process_order_delivery_margin_bridge","residual_error":"positive_advanced_equipment_path_requires_green_cap_after_large_mfe_without_refreshed_order_delivery_margin_evidence","shadow_rule_candidate":"allow_capped_actionable_when_order_delivery_and_margin_bridge_confirm_but_cap_green_after_large_mfe"}
{"row_type":"case","case_id":"C09_R2L97_036930_2024_02_22","scheduled_round":"R2","scheduled_loop":97,"large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF","fine_archetype_id":"ADVANCED_SEMI_EQUIPMENT_ALD_CVD_VACUUM_PROCESS_VALUATION_BLOWOFF_ORDER_MARGIN_BRIDGE_VS_EQUIPMENT_LABEL_LATE_CHASE","symbol":"036930","name":"주성엔지니어링","trigger_date":"2024-02-22","entry_date":"2024-02-22","entry_price":31900,"peak_high":41450,"peak_date":"2024-04-08","worst_low_after_entry":22050,"worst_low_after_entry_date":"2024-09-09","mfe_pct":29.9,"mae_pct":-30.9,"classification":"local_burst_ald_cvd_advanced_equipment_rerating_high_mae_4b_failure","calibration_usable":true,"evidence_family":"ald_cvd_advanced_equipment_ai_hbm_capex_readthrough_without_sustained_order_margin_survival","residual_error":"advanced_equipment_rerating_can_create_mfe_but_fail_green_without_customer_order_and_margin_survival","shadow_rule_candidate":"classify_meaningful_mfe_then_high_mae_advanced_equipment_cases_as_local_4b_not_green"}
{"row_type":"case","case_id":"C09_R2L97_083310_2024_02_22","scheduled_round":"R2","scheduled_loop":97,"large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF","fine_archetype_id":"ADVANCED_SEMI_EQUIPMENT_ALD_CVD_VACUUM_PROCESS_VALUATION_BLOWOFF_ORDER_MARGIN_BRIDGE_VS_EQUIPMENT_LABEL_LATE_CHASE","symbol":"083310","name":"엘오티베큠","trigger_date":"2024-02-22","entry_date":"2024-02-22","entry_price":23350,"peak_high":24450,"peak_date":"2024-02-23","worst_low_after_entry":9300,"worst_low_after_entry_date":"2024-10-29","mfe_pct":4.7,"mae_pct":-60.2,"classification":"hard_4c_candidate_vacuum_process_equipment_label_without_customer_order_margin_survival","calibration_usable":true,"evidence_family":"vacuum_process_equipment_capex_recovery_label_without_named_customer_delivery_service_margin_bridge","residual_error":"vacuum_process_equipment_label_can_fail_when_customer_order_delivery_and_margin_bridge_missing","shadow_rule_candidate":"route_vacuum_process_equipment_label_to_hard_4c_if_mfe_shallow_mae_extreme_and_customer_order_bridge_missing"}
```

```jsonl
{"row_type":"aggregate","scheduled_round":"R2","scheduled_loop":97,"large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF","fine_archetype_id":"ADVANCED_SEMI_EQUIPMENT_ALD_CVD_VACUUM_PROCESS_VALUATION_BLOWOFF_ORDER_MARGIN_BRIDGE_VS_EQUIPMENT_LABEL_LATE_CHASE","case_count":3,"positive_case_count":1,"counterexample_count":2,"watch_or_cap_case_count":1,"local_4b_overlay_case_count":1,"hard_4c_candidate_count":1,"advanced_deposition_equipment_case_count":2,"vacuum_process_equipment_case_count":1,"valuation_blowoff_case_count":2,"customer_order_margin_bridge_missing_count":2,"corporate_action_caveat_outside_window_count":3,"market_segment_caveat_count":2,"calibration_usable_trigger_count":3,"loop_contribution_label":"residual_error_found","do_not_propose_new_weight_delta":true}
{"row_type":"shadow_rule","scheduled_round":"R2","scheduled_loop":97,"canonical_archetype_id":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF","rule_id":"C09_ADVANCED_EQUIPMENT_ORDER_DELIVERY_MARGIN_VALUATION_DISCIPLINE_REQUIRED","rule_type":"canonical_archetype_specific_guard","rule_text":"For C09, do not open Stage2-Actionable or Stage3-Green from advanced semiconductor equipment, ALD/CVD/deposition/thermal process, vacuum/process infrastructure, AI/HBM/advanced-node readthrough, customer capex recovery, one-week equipment-stock spike, or late-chase after equipment rerating labels alone. Require named customer/process/tool/fab-node relevance, order visibility or purchase order, delivery/installation/acceptance schedule, utilization and customer capex phase, ASP/mix/service revenue, component/logistics/warranty cost control, margin/OP conversion, valuation discipline after the first equipment-label spike, and post-trigger price survival. Deposition/thermal positives with large MFE may be capped Actionable when order/delivery/margin bridge is explicit, but Green requires fresh evidence. Advanced-equipment reratings with meaningful MFE followed by high MAE should remain local 4B, not Green. Vacuum/process-equipment labels with shallow MFE and extreme MAE should route to hard-4C when customer-order and service-margin bridge are missing.","expected_effect":"Preserve true advanced-equipment order/delivery positives while reducing ALD/CVD, vacuum, and equipment-label valuation-blowoff false positives.","production_scoring_changed":false,"shadow_weight_only":true}
{"row_type":"residual_contribution","scheduled_round":"R2","scheduled_loop":97,"canonical_archetype_id":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF","residual_type":"advanced_equipment_order_delivery_margin_valuation_guard","contribution":"Adds one deposition/thermal equipment positive, one ALD/CVD local 4B failure, and one vacuum/process-equipment hard-4C counterexample to calibrate C09 customer order, delivery, acceptance, valuation, service revenue, and margin requirements.","do_not_count_as_global_weight_delta":true}
```

---

## 10. Proposed canonical-archetype shadow rule

```text
C09_ADVANCED_EQUIPMENT_ORDER_DELIVERY_MARGIN_VALUATION_DISCIPLINE_REQUIRED

IF canonical_archetype_id == C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF:

  Do not open Stage3-Green from:
    - advanced semiconductor equipment label alone
    - ALD / CVD / deposition / thermal process label alone
    - vacuum equipment / process infrastructure label alone
    - AI / HBM / advanced-node readthrough alone
    - customer capex recovery headline alone
    - one-week equipment-stock volume spike alone
    - late chase after an equipment rerating alone

  Require at least two of:
    - named customer / process step / tool type / fab-node relevance
    - order visibility or purchase order
    - delivery / installation / acceptance schedule
    - utilization and customer capex phase
    - ASP / mix / service revenue
    - component / logistics / warranty cost containment
    - margin / OP conversion
    - valuation discipline after first equipment-label spike
    - low-MAE post-trigger price survival
    - fresh evidence after the equipment headline

  If MFE < 8% and MAE < -35%:
    route to C09 hard-4C candidate.

  If MFE > 20% but later MAE <= -30%:
    preserve as local 4B / event burst, not Green, unless current order/delivery/margin evidence appears.

  If MFE is large but valuation has outrun order evidence:
    cap Green until customer acceptance and margin evidence refreshes.

  Distinguish:
    - equipment names where tools are ordered, delivered, accepted, and paid at margin
    - from equipment labels where valuation blowoff reverses before order/margin conversion.
```

---

## 11. Deferred Coding Agent Handoff Prompt

```text
You are a coding agent working on Songdaiki/stock_agent.

Do not treat this research MD as production scoring by itself.
Batch it with other v12 residual research files.

Source file:
e2r_stock_web_v12_residual_round_R2_loop_97_L2_AI_SEMICONDUCTOR_ELECTRONICS_C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF_research.md

Task:
1. Parse machine-readable JSONL rows.
2. Add the three C09 advanced semiconductor equipment valuation-blowoff cases to calibration research ingestion.
3. Preserve production_scoring_changed=false.
4. Treat the proposed rule only as a shadow canonical-archetype guard candidate:
   C09_ADVANCED_EQUIPMENT_ORDER_DELIVERY_MARGIN_VALUATION_DISCIPLINE_REQUIRED.
5. Do not change global weights directly.
6. Compare against existing C09 cases and deduplicate by:
   canonical_archetype_id + symbol + trigger_type + entry_date.
7. If enough C09 cases agree, consider implementing a canonical guard that:
   - blocks equipment-label Green without customer/process/tool, order, delivery, acceptance, utilization, and margin bridge,
   - preserves deposition/thermal positives only with price survival and fresh order evidence,
   - treats meaningful-MFE/high-MAE advanced-equipment reratings as local 4B,
   - routes shallow-MFE/extreme-MAE vacuum/process-equipment labels to hard-4C,
   - applies valuation-discipline caps after equipment blowoff moves.

Expected next schedule:
completed_round = R2
completed_loop = 97
next_round = R3
next_loop = 97
round_schedule_status = valid
round_sector_consistency = pass
```

---

## 12. Required round-state footer

```text
completed_round = R2
completed_loop = 97
next_round = R3
next_loop = 97
round_schedule_status = valid
round_sector_consistency = pass
```
