# E2R Stock-Web v12 Residual Research — R2 / Loop 98

```yaml
scheduled_round: R2
scheduled_loop: 98
large_sector_id: L2_AI_SEMICONDUCTOR_ELECTRONICS
canonical_archetype_id: C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE
fine_archetype_id: QUARTZ_SILICON_PARTS_SSD_TEST_MEMORY_CAPEX_RECOVERY_UTILIZATION_ORDER_MARGIN_BRIDGE_VS_MEMORY_RECOVERY_LABEL_LATE_CHASE

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
watch_or_cap_case_count: 2
local_4b_overlay_case_count: 1
hard_4c_candidate_count: 1
quartz_parts_case_count: 1
silicon_consumable_parts_case_count: 1
ssd_memory_test_equipment_case_count: 1
memory_capex_recovery_bridge_missing_count: 2
customer_order_utilization_margin_bridge_missing_count: 2
late_chase_case_count: 1
market_segment_or_spac_history_caveat_count: 2
old_corporate_action_caveat_outside_window_count: 2
calibration_usable_trigger_count: 3

loop_contribution_label: residual_error_found
canonical_archetype_rule_candidate: true
do_not_propose_new_weight_delta: true

completed_round: R2
completed_loop: 98
next_round: R3
next_loop: 98
round_schedule_status: valid
round_sector_consistency: pass
```

---

## 1. Schedule resolution

Previous completed file in the active sequence was:

```text
e2r_stock_web_v12_residual_round_R1_loop_98_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C05_EPC_MEGA_CONTRACT_MARGIN_GAP_research.md
```

Under v12:

```text
R1 -> R2 -> R3 -> R4 -> R5 -> R6 -> R7 -> R8 -> R9 -> R10 -> R11 -> R12 -> R13 -> R1
```

Therefore:

```text
scheduled_round = R2
scheduled_loop = 98
large_sector_id = L2_AI_SEMICONDUCTOR_ELECTRONICS
```

R2 hard gate requires:

```text
large_sector_id = L2_AI_SEMICONDUCTOR_ELECTRONICS
```

Recent R2 branch usage:

```text
loop94: C06_HBM_MEMORY_CUSTOMER_CAPACITY
loop95: C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH
loop96: C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY
loop97: C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF
```

This run returns to C10 after the R2 branch cycle.

Selected fine branch:

```text
quartz / silicon consumable parts / SSD-memory test equipment
memory capex recovery, fab utilization, replacement cycle, order delivery, customer acceptance,
valuation discipline, and margin bridge
vs generic memory-recovery or semiconductor-equipment late chase
```

---

## 2. No-repeat / novelty check

No-Repeat Index coverage snapshot:

```text
C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE
rows: 29
symbols: 18
date_range: 2023-03-31~2024-06-14
good/bad S2: 15/5
4B/4C: 1/0
URL pending/proxy: 16/10
top covered symbols:
  089970(3), 281820(3), 319660(3), 042700(2), 064290(2), 079370(2)
```

Selected symbols:

```text
074600 원익QnC
101160 월덱스
253590 네오셈
```

They avoid the C10 top-covered names and recent R2 loop95~97 symbols:

```text
loop97 C09 avoid:
  084370, 036930, 083310

loop96 C08 avoid:
  092870, 067310, 097800

loop95 C07 avoid:
  039030, 083450, 095610

C10 top-covered avoid:
  089970, 281820, 319660, 042700, 064290, 079370
```

Hard duplicate key:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

Novelty classification:

```text
074600: same archetype, new symbol, quartz/ceramic parts memory-capex recovery positive with Green cap
101160: same archetype, new symbol, silicon consumable parts Watch cap after modest MFE and material MAE
253590: same archetype, new symbol, SSD/memory test-equipment late chase hard-4C candidate after valuation spike
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
074600 원익QnC
  profile: atlas/symbol_profiles/074/074600.json
  name history:
    원익쿼츠 until 2012-04-02
    원익QnC from 2012-04-03
  first_date: 2003-12-12
  last_date: 2026-02-20
  market:
    KOSDAQ until 2022-11-18
    KOSDAQ GLOBAL from 2022-11-21
  tradable_ohlcv rows: 5,476
  non_tradable_zero_volume rows: 0
  corporate_action_candidate_dates:
    2004-06-25, 2004-07-21, 2017-04-28, 2017-05-24
  2024 entry~D+180 contamination: none
  caveat:
    old corporate-action candidates are outside selected 2024 validation window.

101160 월덱스
  profile: atlas/symbol_profiles/101/101160.json
  first_date: 2008-06-19
  last_date: 2026-02-20
  market: KOSDAQ
  tradable_ohlcv rows: 4,359
  non_tradable_zero_volume rows: 1
  corporate_action_candidate_dates:
    2014-11-03
  2024 entry~D+180 contamination: none
  caveat:
    old corporate-action candidate is outside selected 2024 validation window.

253590 네오셈
  profile: atlas/symbol_profiles/253/253590.json
  name history:
    대신밸런스제3호스팩 until 2019-01-30
    네오셈 from 2019-01-31
  first_date: 2018-04-04
  last_date: 2026-02-20
  market: KOSDAQ
  tradable_ohlcv rows: 1,890
  non_tradable_zero_volume rows: 43
  corporate_action_candidate_dates:
    2019-01-31
  2024 entry~D+180 contamination: none
  caveat:
    old SPAC transition candidate and row-presence caveat exist outside selected 2024 validation window.
```

---

## 4. Archetype residual problem

C10 is about memory recovery and equipment/parts cycles. It is not a generic "semiconductor stock is recovering" archetype.

The model can over-score:

```text
memory recovery label
AI / HBM / NAND / SSD recovery readthrough
semiconductor parts / consumables label
quartz / silicon / ceramic parts label
SSD tester / memory test equipment label
customer capex recovery headline
one-week semiconductor equipment volume spike
late chase after a memory-equipment valuation spike
```

The C10 bridge must be stricter:

```text
memory recovery / equipment-cycle event
  -> named customer, memory type, process step, or tool/parts category
  -> capex phase and fab utilization
  -> order visibility, delivery, or replacement cycle
  -> customer acceptance and qualification
  -> ASP / mix / service or consumables revenue
  -> raw-material, logistics, and warranty cost
  -> inventory / working-capital timing
  -> margin / OP conversion
  -> valuation discipline after the first memory-recovery spike
  -> price survival after the rerating
```

A C10 thesis is like a cleanroom consumable tray. The memory cycle may be warming, but equity value appears only when the customer is actually running the fab, replacing parts, ordering tools, accepting deliveries, and paying enough for margin to survive.

---

## 5. Case 1 — 074600 원익QnC

```yaml
case_id: C10_R2L98_074600_2024_02_01
symbol: "074600"
name: "원익QnC"
canonical_archetype_id: C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE
fine_archetype_id: QUARTZ_SILICON_PARTS_SSD_TEST_MEMORY_CAPEX_RECOVERY_UTILIZATION_ORDER_MARGIN_BRIDGE_VS_MEMORY_RECOVERY_LABEL_LATE_CHASE
trigger_date: 2024-02-01
entry_date: 2024-02-01
entry_price_basis: close
entry_price: 27800
classification: positive_quartz_ceramic_parts_memory_capex_recovery_utilization_margin_bridge_with_green_cap
calibration_usable: true
```

### Evidence interpretation

원익QnC is the constructive C10 control in this set.

The useful C10 read is not simply:

```text
반도체 부품주가 강하다
```

It is:

```text
quartz / ceramic consumable parts
  -> memory fab utilization and replacement cycle
  -> customer capex and process-step recovery readthrough
  -> price confirmation into May
  -> later Green cap when order/utilization evidence becomes stale
```

The forward path produced meaningful MFE and did not cross a hard-failure threshold. This preserves a positive classification. However, C10 Green should remain capped unless fab utilization, replacement-cycle demand, customer order, and margin evidence are current.

### Price path

Key Stock-Web rows:

```text
2024-02-01: high 28,550 / close 27,800
2024-03-21: high 33,350 / close 33,000
2024-03-29: high 34,500 / close 33,600
2024-05-08: high 35,950 / close 35,900
2024-08-05: low 24,250 / close 24,900
2024-10-23: low 22,250 / close 24,400
```

Approximate path from entry close:

```text
entry_close: 27,800
peak_high: 35,950
MFE: +29.3%
worst_low_after_entry: 22,250
MAE: -20.0%
```

### Interpretation

This is a C10 positive with Green cap:

```text
Stage2-Actionable: possible if customer/process, fab utilization, replacement cycle, and margin bridge are explicit.
Stage3-Green: blocked without fresh utilization, order, and margin evidence after the rerating.
Local 4B: monitor after +25% MFE if evidence becomes stale.
Hard 4C: no.
```

### Stress-test components

```text
raw_component_score_proxy:
  quartz_ceramic_parts_relevance: high
  memory_recovery_signal: high
  fab_utilization_bridge: medium_high
  customer_order_replacement_bridge: medium
  margin_op_bridge: medium
  price_confirmation: high_initial
  later_drawdown_penalty: medium
  green_cap: required
```

---

## 6. Case 2 — 101160 월덱스

```yaml
case_id: C10_R2L98_101160_2024_02_01
symbol: "101160"
name: "월덱스"
canonical_archetype_id: C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE
fine_archetype_id: QUARTZ_SILICON_PARTS_SSD_TEST_MEMORY_CAPEX_RECOVERY_UTILIZATION_ORDER_MARGIN_BRIDGE_VS_MEMORY_RECOVERY_LABEL_LATE_CHASE
trigger_date: 2024-02-01
entry_date: 2024-02-01
entry_price_basis: close
entry_price: 23400
classification: watch_cap_silicon_consumable_parts_label_without_strong_incremental_memory_utilization_margin_bridge
calibration_usable: true
```

### Evidence interpretation

월덱스 is the silicon consumable-parts Watch cap.

The setup is relevant:

```text
silicon / semiconductor consumable parts
  -> memory utilization and replacement-cycle optionality
  -> process-parts demand readthrough
```

But from the selected February entry, the path did not justify Actionable/Green. MFE was modest and later drawdown was material. This is not a hard 4C, but it shows that consumable-parts relevance is not enough unless utilization, customer replacement, and margin evidence improves.

### Price path

Key Stock-Web rows:

```text
2024-02-01: high 24,050 / close 23,400
2024-04-02: high 26,150 / close 25,700
2024-08-05: low 18,550 / close 19,050
2024-08-20: high 26,050 / close 25,900
2024-09-06: low 19,610 / close 19,690
2024-10-31: low 18,580 / close 18,860
```

Approximate path from entry close:

```text
entry_close: 23,400
peak_high: 26,150
MFE: +11.8%
worst_low_after_entry: 18,330
MAE: -21.7%
```

### Interpretation

This is a Watch/Yellow cap:

```text
Stage2-Watch: valid from silicon consumable-parts and memory-recovery relevance.
Stage2-Actionable: blocked unless utilization, replacement cycle, customer order, and margin bridge are explicit.
Stage3-Green: blocked.
Hard 4C: no, because MFE/MAE do not cross hard thresholds.
```

### Stress-test components

```text
raw_component_score_proxy:
  silicon_consumable_parts_relevance: high
  memory_utilization_bridge: medium
  replacement_cycle_bridge: weak_to_medium
  customer_order_bridge: weak_to_medium
  margin_op_bridge: weak_to_medium
  price_confirmation: modest
  drawdown_penalty: material
  actionability_cap: Watch/Yellow
```

---

## 7. Case 3 — 253590 네오셈

```yaml
case_id: C10_R2L98_253590_2024_03_06
symbol: "253590"
name: "네오셈"
canonical_archetype_id: C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE
fine_archetype_id: QUARTZ_SILICON_PARTS_SSD_TEST_MEMORY_CAPEX_RECOVERY_UTILIZATION_ORDER_MARGIN_BRIDGE_VS_MEMORY_RECOVERY_LABEL_LATE_CHASE
trigger_date: 2024-03-06
entry_date: 2024-03-06
entry_price_basis: close
entry_price: 14950
classification: hard_4c_candidate_ssd_memory_test_equipment_late_chase_without_customer_order_margin_survival
calibration_usable: true
```

### Evidence interpretation

네오셈 is the SSD / memory-test equipment late-chase guardrail.

The label can fool the model:

```text
SSD / memory test equipment
  -> CXL / AI / NAND / SSD recovery readthrough
  -> customer capex and test-equipment optionality
  -> one-day high-volume equipment spike
```

The stock had powerful first-quarter momentum. But from the selected March 6 late-entry close, the forward path failed price survival. The bridge from memory-test label to named customer order, delivery, acceptance, utilization, and margin was not strong enough for Actionable/Green.

### Price path

Key Stock-Web rows:

```text
2024-03-06: high 16,290 / close 14,950
2024-03-07: high 17,150 / close 15,390
2024-03-18: high 16,230 / close 16,180
2024-04-08: low 11,920 / close 11,940
2024-08-05: low 8,610 / close 9,620
2024-09-06: low 7,580 / close 7,720
2024-09-26: high 11,200 / close 11,200
2024-10-14: high 12,750 / close 12,080
2024-10-18: low 10,500 / close 10,500
```

Approximate path from late entry close:

```text
entry_close: 14,950
peak_high_after_entry: 17,150
MFE: +14.7%
worst_low_after_entry: 7,420
MAE: -50.4%
```

### Interpretation

This is a hard C10 false-positive candidate:

```text
Stage2-Watch: possible from SSD/memory-test equipment relevance.
Stage2-Actionable: blocked unless named customer order, delivery/acceptance, utilization, and margin bridge are explicit.
Stage3-Green: blocked.
Hard 4C: yes by meaningful-but-insufficient MFE and extreme MAE from the late entry.
Event-window caveat: later September/October spikes should be treated as new event windows, not rescue of the March late-entry trigger.
SPAC/name-history caveat: old, outside 2024 validation window.
```

The lesson is that memory-test equipment momentum is not customer-order margin survival when entry is late.

### Stress-test components

```text
raw_component_score_proxy:
  ssd_memory_test_equipment_relevance: high
  ai_cxl_ssd_recovery_readthrough: high
  customer_order_bridge: weak
  delivery_acceptance_bridge: weak_to_medium
  utilization_margin_bridge: weak
  valuation_late_chase_risk: high
  drawdown_penalty: extreme
  hard_4c_guard: yes
```

---

## 8. Aggregate calibration takeaways

```text
positive_case_count: 1
counterexample_count: 2
watch_or_cap_case_count: 2
local_4b_overlay_case_count: 1
hard_4c_candidate_count: 1
quartz_parts_case_count: 1
silicon_consumable_parts_case_count: 1
ssd_memory_test_equipment_case_count: 1
memory_capex_recovery_bridge_missing_count: 2
customer_order_utilization_margin_bridge_missing_count: 2
late_chase_case_count: 1
market_segment_or_spac_history_caveat_count: 2
old_corporate_action_caveat_outside_window_count: 2
calibration_usable_trigger_count: 3
```

The three-case C10 memory recovery grid:

```text
074600 원익QnC:
  quartz / ceramic parts memory-recovery positive;
  meaningful MFE and non-hard MAE, but Green requires fresh utilization, replacement-cycle, and margin evidence.

101160 월덱스:
  silicon consumable-parts Watch cap;
  modest MFE and material MAE, no Actionable without stronger customer utilization and margin bridge.

253590 네오셈:
  SSD/memory-test equipment late chase failed;
  insufficient MFE and extreme MAE, hard 4C candidate.
```

Shared rule:

```text
C10 is not "memory recovery label is hot."
C10 is "fab utilization, customer order, replacement cycle, delivery/acceptance, service or consumables revenue, valuation discipline, and margin conversion are visible for this company."
```

---

## 9. Machine-readable JSONL rows

```jsonl
{"row_type":"case","case_id":"C10_R2L98_074600_2024_02_01","scheduled_round":"R2","scheduled_loop":98,"large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","fine_archetype_id":"QUARTZ_SILICON_PARTS_SSD_TEST_MEMORY_CAPEX_RECOVERY_UTILIZATION_ORDER_MARGIN_BRIDGE_VS_MEMORY_RECOVERY_LABEL_LATE_CHASE","symbol":"074600","name":"원익QnC","trigger_date":"2024-02-01","entry_date":"2024-02-01","entry_price":27800,"peak_high":35950,"peak_date":"2024-05-08","worst_low_after_entry":22250,"worst_low_after_entry_date":"2024-10-23","mfe_pct":29.3,"mae_pct":-20.0,"classification":"positive_quartz_ceramic_parts_memory_capex_recovery_utilization_margin_bridge_with_green_cap","calibration_usable":true,"market_segment_or_old_corporate_action_caveat":true,"evidence_family":"quartz_ceramic_consumable_parts_memory_fab_utilization_replacement_cycle_customer_order_margin_bridge","residual_error":"positive_memory_parts_path_requires_green_cap_without_refreshed_utilization_replacement_and_margin_evidence","shadow_rule_candidate":"allow_capped_actionable_when_fab_utilization_replacement_cycle_and_margin_bridge_confirm_but_cap_green_without_fresh_evidence"}
{"row_type":"case","case_id":"C10_R2L98_101160_2024_02_01","scheduled_round":"R2","scheduled_loop":98,"large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","fine_archetype_id":"QUARTZ_SILICON_PARTS_SSD_TEST_MEMORY_CAPEX_RECOVERY_UTILIZATION_ORDER_MARGIN_BRIDGE_VS_MEMORY_RECOVERY_LABEL_LATE_CHASE","symbol":"101160","name":"월덱스","trigger_date":"2024-02-01","entry_date":"2024-02-01","entry_price":23400,"peak_high":26150,"peak_date":"2024-04-02","worst_low_after_entry":18330,"worst_low_after_entry_date":"2024-11-01","mfe_pct":11.8,"mae_pct":-21.7,"classification":"watch_cap_silicon_consumable_parts_label_without_strong_incremental_memory_utilization_margin_bridge","calibration_usable":true,"old_corporate_action_caveat_outside_window":true,"evidence_family":"silicon_consumable_parts_memory_utilization_replacement_cycle_label_without_incremental_customer_order_margin_bridge","residual_error":"silicon_parts_relevance_can_overpromote_without_customer_utilization_replacement_cycle_and_margin_evidence","shadow_rule_candidate":"cap_silicon_consumable_parts_label_at_watch_yellow_if_mfe_modest_and_utilization_bridge_missing"}
{"row_type":"case","case_id":"C10_R2L98_253590_2024_03_06","scheduled_round":"R2","scheduled_loop":98,"large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","fine_archetype_id":"QUARTZ_SILICON_PARTS_SSD_TEST_MEMORY_CAPEX_RECOVERY_UTILIZATION_ORDER_MARGIN_BRIDGE_VS_MEMORY_RECOVERY_LABEL_LATE_CHASE","symbol":"253590","name":"네오셈","trigger_date":"2024-03-06","entry_date":"2024-03-06","entry_price":14950,"peak_high":17150,"peak_date":"2024-03-07","worst_low_after_entry":7420,"worst_low_after_entry_date":"2024-09-09","mfe_pct":14.7,"mae_pct":-50.4,"classification":"hard_4c_candidate_ssd_memory_test_equipment_late_chase_without_customer_order_margin_survival","calibration_usable":true,"spac_or_name_history_caveat_outside_window":true,"event_window_separation_required":true,"evidence_family":"ssd_memory_test_equipment_ai_cxl_nand_recovery_late_chase_without_customer_order_delivery_acceptance_margin_bridge","residual_error":"memory_test_equipment_late_chase_can_fail_when_customer_order_and_margin_bridge_missing","shadow_rule_candidate":"route_ssd_memory_test_equipment_late_chase_to_hard_4c_if_mae_extreme_and_order_margin_bridge_missing"}
```

```jsonl
{"row_type":"aggregate","scheduled_round":"R2","scheduled_loop":98,"large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","fine_archetype_id":"QUARTZ_SILICON_PARTS_SSD_TEST_MEMORY_CAPEX_RECOVERY_UTILIZATION_ORDER_MARGIN_BRIDGE_VS_MEMORY_RECOVERY_LABEL_LATE_CHASE","case_count":3,"positive_case_count":1,"counterexample_count":2,"watch_or_cap_case_count":2,"local_4b_overlay_case_count":1,"hard_4c_candidate_count":1,"quartz_parts_case_count":1,"silicon_consumable_parts_case_count":1,"ssd_memory_test_equipment_case_count":1,"memory_capex_recovery_bridge_missing_count":2,"customer_order_utilization_margin_bridge_missing_count":2,"late_chase_case_count":1,"market_segment_or_spac_history_caveat_count":2,"old_corporate_action_caveat_outside_window_count":2,"calibration_usable_trigger_count":3,"loop_contribution_label":"residual_error_found","do_not_propose_new_weight_delta":true}
{"row_type":"shadow_rule","scheduled_round":"R2","scheduled_loop":98,"canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","rule_id":"C10_MEMORY_RECOVERY_UTILIZATION_ORDER_MARGIN_DISCIPLINE_REQUIRED","rule_type":"canonical_archetype_specific_guard","rule_text":"For C10 memory recovery / equipment-cycle cases, do not open Stage2-Actionable or Stage3-Green from memory recovery, AI/HBM/NAND/SSD recovery readthrough, semiconductor parts/consumables, quartz/silicon/ceramic parts, SSD tester, memory test equipment, customer capex recovery, one-week semiconductor equipment spike, or late chase after memory-equipment rerating labels alone. Require named customer/memory type/process step/tool or parts category, capex phase and fab utilization, order visibility/delivery/replacement cycle, customer acceptance and qualification, ASP/mix/service or consumables revenue, raw-material/logistics/warranty cost containment, inventory/working-capital timing, margin/OP conversion, valuation discipline after the first memory-recovery spike, and post-trigger price survival. Quartz/ceramic parts positives with meaningful MFE may be capped Actionable when utilization/replacement/margin bridge is explicit, but Green requires fresh evidence. Silicon consumable-parts labels with modest MFE and material MAE should cap at Watch/Yellow without stronger utilization evidence. SSD/memory-test equipment late chases with extreme MAE should route to hard-4C when customer order and margin bridge are missing, with later event windows separated from earlier failed triggers.","expected_effect":"Preserve true memory recovery equipment/parts positives while reducing generic memory-recovery, consumables, SSD-tester, and late-chase false positives where utilization, customer order, acceptance, valuation, and margin evidence fail.","production_scoring_changed":false,"shadow_weight_only":true}
{"row_type":"residual_contribution","scheduled_round":"R2","scheduled_loop":98,"canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","residual_type":"memory_recovery_utilization_order_margin_guard","contribution":"Adds one quartz/ceramic parts positive, one silicon consumable-parts Watch cap, and one SSD/memory-test equipment hard-4C counterexample to calibrate C10 fab utilization, replacement cycle, customer order, delivery/acceptance, valuation discipline, and margin requirements.","do_not_count_as_global_weight_delta":true}
```

---

## 10. Proposed canonical-archetype shadow rule

```text
C10_MEMORY_RECOVERY_UTILIZATION_ORDER_MARGIN_DISCIPLINE_REQUIRED

IF canonical_archetype_id == C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE:

  Do not open Stage3-Green from:
    - memory recovery label alone
    - AI / HBM / NAND / SSD recovery readthrough alone
    - semiconductor parts / consumables label alone
    - quartz / silicon / ceramic parts label alone
    - SSD tester / memory test equipment label alone
    - customer capex recovery headline alone
    - one-week semiconductor-equipment volume spike alone
    - late chase after memory-equipment rerating alone

  Require at least two of:
    - named customer / memory type / process step / tool or parts category
    - capex phase and fab utilization
    - order visibility / delivery / replacement cycle
    - customer acceptance and qualification
    - ASP / mix / service or consumables revenue
    - raw-material / logistics / warranty cost containment
    - inventory / working-capital timing
    - margin / OP conversion
    - valuation discipline after initial memory-recovery spike
    - low-MAE post-trigger price survival
    - fresh evidence after the memory-recovery headline

  If MFE < 8% and MAE < -30%:
    route to C10 hard-4C candidate.

  If MFE is modest and bridge is consumable-label only:
    cap at Watch/Yellow.

  If MAE is extreme after a late memory-test-equipment spike:
    route to hard-4C unless current customer order and margin evidence exists.

  If later event-like spikes appear after first failure:
    create a new event window; do not retroactively validate the earlier failed trigger.

  Distinguish:
    - companies where memory recovery becomes fab utilization, replacement cycle, order, acceptance, and margin
    - from labels where valuation moves first and utilization/order/margin proof fails.
```

---

## 11. Deferred Coding Agent Handoff Prompt

```text
You are a coding agent working on Songdaiki/stock_agent.

Do not treat this research MD as production scoring by itself.
Batch it with other v12 residual research files.

Source file:
e2r_stock_web_v12_residual_round_R2_loop_98_L2_AI_SEMICONDUCTOR_ELECTRONICS_C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE_research.md

Task:
1. Parse machine-readable JSONL rows.
2. Add the three C10 memory-recovery equipment/parts cases to calibration research ingestion.
3. Preserve production_scoring_changed=false.
4. Treat the proposed rule only as a shadow canonical-archetype guard candidate:
   C10_MEMORY_RECOVERY_UTILIZATION_ORDER_MARGIN_DISCIPLINE_REQUIRED.
5. Do not change global weights directly.
6. Compare against existing C10 cases and deduplicate by:
   canonical_archetype_id + symbol + trigger_type + entry_date.
7. If enough C10 cases agree, consider implementing a canonical guard that:
   - blocks memory-recovery Green without customer/process/tool, fab utilization, order, replacement, acceptance, and margin bridge,
   - preserves quartz/ceramic parts positives only with price survival and fresh utilization evidence,
   - caps modest-MFE silicon consumable-parts labels at Watch/Yellow,
   - routes extreme-MAE SSD/memory-test equipment late chases to hard-4C,
   - separates later renewed memory-test event windows from earlier failed late-chase triggers,
   - applies market-segment, SPAC/name-history, and old corporate-action caveats where needed.

Expected next schedule:
completed_round = R2
completed_loop = 98
next_round = R3
next_loop = 98
round_schedule_status = valid
round_sector_consistency = pass
```

---

## 12. Required round-state footer

```text
completed_round = R2
completed_loop = 98
next_round = R3
next_loop = 98
round_schedule_status = valid
round_sector_consistency = pass
```
