# E2R Stock-Web v12 Residual Research — R2 / Loop 95

```yaml
scheduled_round: R2
scheduled_loop: 95
large_sector_id: L2_AI_SEMICONDUCTOR_ELECTRONICS
canonical_archetype_id: C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH
fine_archetype_id: LASER_CHILLER_SCRUBBER_ALD_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH_VS_EQUIPMENT_LABEL_LATE_CHASE

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
corporate_action_caveat_avoided_count: 1
calibration_usable_trigger_count: 3

loop_contribution_label: residual_error_found
canonical_archetype_rule_candidate: true
do_not_propose_new_weight_delta: true

completed_round: R2
completed_loop: 95
next_round: R3
next_loop: 95
round_schedule_status: valid
round_sector_consistency: pass
```

---

## 1. Schedule resolution

Previous completed file in the active sequence was:

```text
e2r_stock_web_v12_residual_round_R1_loop_95_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG_research.md
```

Under v12:

```text
R1 -> R2 -> R3 -> R4 -> R5 -> R6 -> R7 -> R8 -> R9 -> R10 -> R11 -> R12 -> R13 -> R1
```

Therefore:

```text
scheduled_round = R2
scheduled_loop = 95
large_sector_id = L2_AI_SEMICONDUCTOR_ELECTRONICS
```

R2 hard gate requires:

```text
large_sector_id = L2_AI_SEMICONDUCTOR_ELECTRONICS
```

Recent R2 branch usage:

```text
loop91: C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY
loop92: C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF
loop93: C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE
loop94: C06_HBM_MEMORY_CUSTOMER_CAPACITY
```

This run selects:

```text
canonical_archetype_id = C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH
```

The selected fine branch is:

```text
laser / chiller / scrubber / ALD equipment
HBM equipment order and relative-strength bridge
vs generic semiconductor-equipment label late chase
```

This deliberately avoids the prior R2 loop94 C06 memory-customer-capacity branch and avoids the C07 top-covered names.

---

## 2. No-repeat / novelty check

No-Repeat Index coverage snapshot:

```text
C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH
rows: 11
symbols: 9
date_range: 2024-02-13~2024-06-14
good/bad S2: 7/0
4B/4C: 1/0
URL pending/proxy: 0/0
top covered symbols:
  042700(2), 064760(2), 003160(1), 036200(1), 036540(1), 039440(1)
```

Selected symbols:

```text
039030 이오테크닉스
083450 GST
095610 테스
```

They avoid the C07 top-covered symbols and avoid the most recent R2 loop94 C06 names:

```text
loop94 avoid: 005290, 222800, 272290
```

Hard duplicate key:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

Novelty classification:

```text
039030: same archetype, new symbol, laser/advanced HBM equipment relative-strength positive with local 4B after later MAE
083450: same archetype, new symbol, chiller/scrubber equipment post-corporate-action Watch cap without fresh order-margin bridge
095610: same archetype, new symbol, ALD/front-end equipment late spike hard-4C without order survival
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
039030 이오테크닉스
  profile: atlas/symbol_profiles/039/039030.json
  first_date: 2000-08-24
  last_date: 2026-02-20
  market:
    KOSDAQ until 2022-11-18
    KOSDAQ GLOBAL from 2022-11-21
  tradable_ohlcv rows: 6,285
  corporate_action_candidate_dates: none in 2024 validation window
  2024 entry~D+180 contamination: none

083450 GST
  profile: atlas/symbol_profiles/083/083450.json
  first_date: 2006-02-01
  last_date: 2026-02-20
  market: KOSDAQ
  tradable_ohlcv rows: 4,945
  corporate_action_candidate_dates:
    2007-07-19, 2007-08-07, 2024-06-26, 2024-07-24
  selected entry:
    2024-08-26, after both 2024 corporate-action candidate windows
  entry~D+180 contamination: avoided

095610 테스
  profile: atlas/symbol_profiles/095/095610.json
  first_date: 2008-05-20
  last_date: 2026-02-20
  market:
    KOSDAQ / KOSDAQ GLOBAL segment history
  tradable_ohlcv rows: 4,381
  corporate_action_candidate_dates:
    2011-08-10, 2011-08-29, 2016-05-09
  2024 entry~D+180 contamination: none
```

---

## 4. Archetype residual problem

C07 is about HBM equipment order visibility and relative strength. It is not a generic "semiconductor equipment stock went up" archetype.

The model can over-score:

```text
HBM / AI equipment label
laser equipment label
chiller / scrubber / process utility label
ALD / front-end equipment label
memory equipment replacement cycle
one-week semiconductor-equipment volume spike
```

The C07 bridge must be stricter:

```text
HBM or advanced-memory equipment event
  -> named customer or process step
  -> purchase order / order backlog
  -> delivery timing and capacity
  -> qualification / tool-of-record status
  -> ASP / mix / margin bridge
  -> working-capital and inventory risk
  -> relative strength and price survival after the first equipment spike
```

An HBM equipment thesis is like a cleanroom tool order. The headline says a new line needs tools, but C07 asks whether this company's tool is qualified, ordered, delivered on time, and paid for at margin.

---

## 5. Case 1 — 039030 이오테크닉스

```yaml
case_id: C07_R2L95_039030_2024_02_28
symbol: "039030"
name: "이오테크닉스"
canonical_archetype_id: C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH
fine_archetype_id: LASER_CHILLER_SCRUBBER_ALD_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH_VS_EQUIPMENT_LABEL_LATE_CHASE
trigger_date: 2024-02-28
entry_date: 2024-02-28
entry_price_basis: close
entry_price: 202000
classification: local_positive_laser_advanced_hbm_equipment_relative_strength_with_4b_watch
calibration_usable: true
```

### Evidence interpretation

이오테크닉스 is the constructive control, but not an unrestricted Green.

The useful C07 read is not simply:

```text
반도체 장비주가 강하다
```

It is:

```text
laser / advanced packaging or HBM-adjacent equipment relevance
  -> equipment relative strength
  -> order and qualification optionality
  -> strong price confirmation
```

The forward path delivered a large MFE into April, but later failed price survival. This makes the original entry useful as a local positive, while requiring 4B after the move unless fresh order and margin evidence appears.

### Price path

Key Stock-Web rows:

```text
2024-02-28: high 204,500 / close 202,000
2024-02-29: high 214,500 / close 204,500
2024-03-29: high 218,500 / close 208,500
2024-04-04: high 266,000 / close 259,000
2024-04-12: high 281,000 / close 273,000
2024-08-05: low 129,400 / close 136,400
2024-09-09: low 133,100 / close 138,600
```

Approximate path from entry close:

```text
entry_close: 202,000
peak_high: 281,000
MFE: +39.1%
worst_low_after_entry: 129,400
MAE: -35.9%
```

### Interpretation

This is a C07 local positive with 4B:

```text
Stage2-Actionable: valid if named customer/process, order visibility, and margin bridge are explicit.
Stage3-Green: blocked without fresh tool qualification, backlog, delivery, and OP evidence.
Local 4B: required because +39% MFE later became -35% MAE.
Hard 4C: no for the original entry, because meaningful MFE came first.
```

### Stress-test components

```text
raw_component_score_proxy:
  hbm_equipment_relevance: high
  laser_advanced_packaging_bridge: high
  order_visibility_bridge: medium
  relative_strength: high_initial
  margin_bridge: medium
  post_rally_price_survival: failed
  local_4b_overlay: required
```

---

## 6. Case 2 — 083450 GST

```yaml
case_id: C07_R2L95_083450_2024_08_26
symbol: "083450"
name: "GST"
canonical_archetype_id: C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH
fine_archetype_id: LASER_CHILLER_SCRUBBER_ALD_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH_VS_EQUIPMENT_LABEL_LATE_CHASE
trigger_date: 2024-08-26
entry_date: 2024-08-26
entry_price_basis: close
entry_price: 17500
classification: watch_cap_chiller_scrubber_equipment_post_corporate_action_without_fresh_order_margin_bridge
calibration_usable: true
```

### Evidence interpretation

GST is the chiller/scrubber/process utility Watch cap.

The company has plausible C07 relevance:

```text
semiconductor chiller / scrubber / process utility equipment
  -> HBM and advanced-memory fab investment readthrough
  -> equipment order optionality
```

But there is an important raw-price caveat:

```text
corporate-action candidate dates: 2024-06-26, 2024-07-24
```

Therefore, the selected trigger is after those windows:

```text
entry_date = 2024-08-26
```

From this post-candidate entry, the price path did not validate Actionable/Green. The MFE was modest and the drawdown was material.

### Price path

Key Stock-Web rows:

```text
2024-06-26: corporate-action candidate window in profile
2024-07-24: corporate-action candidate window in profile
2024-08-26: high 19,150 / close 17,500
2024-08-27: high 18,370 / close 17,510
2024-09-09: low 13,350 / close 14,500
2024-09-25: high 17,790 / close 16,430
2024-10-18: low 15,420 / close 15,430
```

Approximate path from entry close:

```text
entry_close: 17,500
peak_high_after_entry: 19,150
MFE: +9.4%
worst_low_after_entry: 13,350
MAE: -23.7%
```

### Interpretation

This is a Watch/Yellow cap case:

```text
Stage2-Watch: valid from equipment utility relevance and post-candidate price action.
Stage2-Actionable: blocked unless fresh order, delivery, and margin bridge are explicit.
Stage3-Green: blocked.
Hard 4C: not primary because MFE was near 10% and MAE did not cross the hard threshold.
Corporate-action caveat: avoided by selecting post-2024-07-24 entry.
```

### Stress-test components

```text
raw_component_score_proxy:
  equipment_utility_relevance: medium_high
  hbm_fab_capex_readthrough: medium
  order_delivery_bridge: weak_to_medium
  corporate_action_caveat_avoided: yes
  price_confirmation: modest
  drawdown_penalty: medium_high
  actionability_cap: Watch/Yellow
```

---

## 7. Case 3 — 095610 테스

```yaml
case_id: C07_R2L95_095610_2024_04_17
symbol: "095610"
name: "테스"
canonical_archetype_id: C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH
fine_archetype_id: LASER_CHILLER_SCRUBBER_ALD_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH_VS_EQUIPMENT_LABEL_LATE_CHASE
trigger_date: 2024-04-17
entry_date: 2024-04-17
entry_price_basis: close
entry_price: 29300
classification: hard_4c_candidate_ald_frontend_equipment_late_spike_without_order_survival
calibration_usable: true
```

### Evidence interpretation

테스 is the hard C07 guardrail.

The setup had the classic late-chase shape:

```text
front-end equipment / ALD process label
  -> HBM and memory capex readthrough
  -> high-volume April equipment spike
  -> model could mistake the spike for order conversion
```

But from the selected close after the spike, the price path did not survive. The MFE was only moderate while the later MAE crossed the hard failure zone.

### Price path

Key Stock-Web rows:

```text
2024-04-15: high 29,150 / close 28,650
2024-04-16: high 30,200 / close 29,550
2024-04-17: high 32,900 / close 29,300
2024-04-18: high 30,000 / close 29,750
2024-08-05: low 16,000 / close 16,700
2024-09-11: low 15,970 / close 15,980
2024-10-25: low 15,850 / close 15,870
```

Approximate path from entry close:

```text
entry_close: 29,300
peak_high_after_entry: 32,900
MFE: +12.3%
worst_low_after_entry: 15,850
MAE: -45.9%
```

### Interpretation

This is a hard C07 false-positive:

```text
Stage2-Watch: possible from ALD/front-end equipment and memory capex relevance.
Stage2-Actionable: blocked unless named customer, order conversion, delivery timing, and margin bridge are explicit.
Stage3-Green: blocked.
Hard 4C: yes by moderate MFE and very high MAE after a late spike.
```

The lesson is that a memory-equipment spike is not order survival.

### Stress-test components

```text
raw_component_score_proxy:
  front_end_equipment_relevance: high
  hbm_memory_capex_readthrough: medium_high
  order_conversion_bridge: weak
  delivery_margin_bridge: weak
  price_confirmation_after_entry: failed
  drawdown_penalty: high
  hard_4c_guard: yes
```

---

## 8. Aggregate calibration takeaways

```text
positive_case_count: 1
counterexample_count: 2
watch_or_cap_case_count: 1
local_4b_overlay_case_count: 2
hard_4c_candidate_count: 1
corporate_action_caveat_avoided_count: 1
calibration_usable_trigger_count: 3
```

The three-case C07 equipment grid:

```text
039030 이오테크닉스:
  laser / advanced HBM equipment relative-strength positive;
  strong MFE came first, but later high MAE requires local 4B.

083450 GST:
  chiller/scrubber equipment post-corporate-action Watch cap;
  modest MFE and material MAE without fresh order-margin bridge.

095610 테스:
  ALD/front-end equipment late spike failed;
  moderate MFE and very high MAE, hard 4C.
```

Shared rule:

```text
C07 is not "HBM equipment label."
C07 is "named customer/process, tool qualification, order conversion, delivery, relative strength, and margin survival are visible for this equipment supplier."
```

---

## 9. Machine-readable JSONL rows

```jsonl
{"row_type":"case","case_id":"C07_R2L95_039030_2024_02_28","scheduled_round":"R2","scheduled_loop":95,"large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH","fine_archetype_id":"LASER_CHILLER_SCRUBBER_ALD_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH_VS_EQUIPMENT_LABEL_LATE_CHASE","symbol":"039030","name":"이오테크닉스","trigger_date":"2024-02-28","entry_date":"2024-02-28","entry_price":202000,"peak_high":281000,"peak_date":"2024-04-12","worst_low_after_entry":129400,"worst_low_after_entry_date":"2024-08-05","mfe_pct":39.1,"mae_pct":-35.9,"classification":"local_positive_laser_advanced_hbm_equipment_relative_strength_with_4b_watch","calibration_usable":true,"evidence_family":"laser_advanced_packaging_hbm_equipment_relative_strength_without_fresh_order_margin_bridge","residual_error":"equipment_relative_strength_positive_requires_4b_after_later_mae_without_fresh_tool_order_margin_evidence","shadow_rule_candidate":"preserve_local_positive_but_attach_4b_after_large_mfe_followed_by_high_mae"}
{"row_type":"case","case_id":"C07_R2L95_083450_2024_08_26","scheduled_round":"R2","scheduled_loop":95,"large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH","fine_archetype_id":"LASER_CHILLER_SCRUBBER_ALD_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH_VS_EQUIPMENT_LABEL_LATE_CHASE","symbol":"083450","name":"GST","trigger_date":"2024-08-26","entry_date":"2024-08-26","entry_price":17500,"peak_high":19150,"peak_date":"2024-08-26","worst_low_after_entry":13350,"worst_low_after_entry_date":"2024-09-09","mfe_pct":9.4,"mae_pct":-23.7,"classification":"watch_cap_chiller_scrubber_equipment_post_corporate_action_without_fresh_order_margin_bridge","calibration_usable":true,"corporate_action_caveat_avoided":true,"evidence_family":"chiller_scrubber_semiconductor_equipment_post_corporate_action_without_fresh_order_margin_bridge","residual_error":"equipment_utility_label_can_overpromote_without_new_order_delivery_margin_bridge_after_corporate_action_window","shadow_rule_candidate":"cap_chiller_scrubber_equipment_label_at_watch_yellow_if_mfe_modest_and_order_bridge_missing"}
{"row_type":"case","case_id":"C07_R2L95_095610_2024_04_17","scheduled_round":"R2","scheduled_loop":95,"large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH","fine_archetype_id":"LASER_CHILLER_SCRUBBER_ALD_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH_VS_EQUIPMENT_LABEL_LATE_CHASE","symbol":"095610","name":"테스","trigger_date":"2024-04-17","entry_date":"2024-04-17","entry_price":29300,"peak_high":32900,"peak_date":"2024-04-17","worst_low_after_entry":15850,"worst_low_after_entry_date":"2024-10-25","mfe_pct":12.3,"mae_pct":-45.9,"classification":"hard_4c_candidate_ald_frontend_equipment_late_spike_without_order_survival","calibration_usable":true,"evidence_family":"ald_frontend_equipment_late_spike_without_named_customer_order_delivery_margin_bridge","residual_error":"memory_equipment_late_spike_can_fail_when_order_conversion_and_margin_survival_missing","shadow_rule_candidate":"route_frontend_equipment_late_spike_to_hard_4c_if_mae_large_and_order_bridge_missing"}
```

```jsonl
{"row_type":"aggregate","scheduled_round":"R2","scheduled_loop":95,"large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH","fine_archetype_id":"LASER_CHILLER_SCRUBBER_ALD_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH_VS_EQUIPMENT_LABEL_LATE_CHASE","case_count":3,"positive_case_count":1,"counterexample_count":2,"watch_or_cap_case_count":1,"local_4b_overlay_case_count":2,"hard_4c_candidate_count":1,"corporate_action_caveat_avoided_count":1,"calibration_usable_trigger_count":3,"loop_contribution_label":"residual_error_found","do_not_propose_new_weight_delta":true}
{"row_type":"shadow_rule","scheduled_round":"R2","scheduled_loop":95,"canonical_archetype_id":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH","rule_id":"C07_EQUIPMENT_ORDER_QUALIFICATION_DELIVERY_MARGIN_BRIDGE_REQUIRED","rule_type":"canonical_archetype_specific_guard","rule_text":"For C07, do not open Stage2-Actionable or Stage3-Green from HBM/AI equipment, laser equipment, chiller/scrubber/process utility, ALD/front-end equipment, memory equipment cycle, or one-week semiconductor-equipment volume spike labels alone. Require named customer or process step, purchase order or backlog visibility, delivery timing and capacity, qualification/tool-of-record status, ASP/mix/margin bridge, working-capital and inventory-risk check, relative strength, and post-trigger price survival. Equipment relative-strength positives with large MFE followed by high MAE should remain local 4B unless fresh order/margin evidence appears. Post-corporate-action equipment labels with modest MFE should cap at Watch/Yellow without fresh order bridge. Front-end equipment late spikes with high MAE should route to hard-4C when customer/order/delivery bridge is missing.","expected_effect":"Preserve true HBM equipment order positives while reducing generic semiconductor-equipment and late-spike false positives.","production_scoring_changed":false,"shadow_weight_only":true}
{"row_type":"residual_contribution","scheduled_round":"R2","scheduled_loop":95,"canonical_archetype_id":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH","residual_type":"equipment_order_qualification_delivery_margin_guard","contribution":"Adds one laser/advanced equipment local positive with 4B, one post-corporate-action chiller/scrubber Watch cap, and one ALD/front-end equipment hard-4C counterexample to calibrate C07 equipment order, qualification, delivery, and margin requirements.","do_not_count_as_global_weight_delta":true}
```

---

## 10. Proposed canonical-archetype shadow rule

```text
C07_EQUIPMENT_ORDER_QUALIFICATION_DELIVERY_MARGIN_BRIDGE_REQUIRED

IF canonical_archetype_id == C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH:

  Do not open Stage3-Green from:
    - HBM / AI equipment headline alone
    - laser equipment label alone
    - chiller / scrubber / process utility label alone
    - ALD / front-end equipment label alone
    - memory equipment replacement-cycle label alone
    - one-week semiconductor-equipment volume spike alone

  Require at least two of:
    - named customer or process step
    - purchase order / backlog
    - delivery timing / capacity
    - qualification or tool-of-record status
    - ASP / mix / margin bridge
    - working-capital or inventory-risk containment
    - low-MAE post-trigger price survival
    - relative strength versus peer equipment group
    - fresh evidence after the equipment-order headline

  If MFE < 15% and MAE < -40%:
    route to C07 hard-4C candidate.

  If MFE > 30% but later MAE is material:
    preserve as local 4B unless fresh order/margin evidence appears.

  If MFE is modest and the order bridge is weak:
    cap at Watch/Yellow.

  If corporate-action candidate exists inside the prior window:
    select post-candidate rows only or block contaminated validation.
```

---

## 11. Deferred Coding Agent Handoff Prompt

```text
You are a coding agent working on Songdaiki/stock_agent.

Do not treat this research MD as production scoring by itself.
Batch it with other v12 residual research files.

Source file:
e2r_stock_web_v12_residual_round_R2_loop_95_L2_AI_SEMICONDUCTOR_ELECTRONICS_C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH_research.md

Task:
1. Parse machine-readable JSONL rows.
2. Add the three C07 HBM equipment order / relative-strength cases to calibration research ingestion.
3. Preserve production_scoring_changed=false.
4. Treat the proposed rule only as a shadow canonical-archetype guard candidate:
   C07_EQUIPMENT_ORDER_QUALIFICATION_DELIVERY_MARGIN_BRIDGE_REQUIRED.
5. Do not change global weights directly.
6. Compare against existing C07 cases and deduplicate by:
   canonical_archetype_id + symbol + trigger_type + entry_date.
7. If enough C07 cases agree, consider implementing a canonical guard that:
   - blocks semiconductor-equipment Green without named customer/process, order/backlog, qualification, delivery, and margin bridge,
   - preserves laser/advanced-equipment positives only with price survival and fresh order evidence,
   - attaches local 4B after large MFE followed by high MAE,
   - caps chiller/scrubber/process-utility labels at Watch/Yellow without fresh order bridge,
   - routes late ALD/front-end equipment spikes to hard-4C when order/delivery bridge is missing,
   - applies corporate-action window cutoffs for raw-price validation.

Expected next schedule:
completed_round = R2
completed_loop = 95
next_round = R3
next_loop = 95
round_schedule_status = valid
round_sector_consistency = pass
```

---

## 12. Required round-state footer

```text
completed_round = R2
completed_loop = 95
next_round = R3
next_loop = 95
round_schedule_status = valid
round_sector_consistency = pass
```
