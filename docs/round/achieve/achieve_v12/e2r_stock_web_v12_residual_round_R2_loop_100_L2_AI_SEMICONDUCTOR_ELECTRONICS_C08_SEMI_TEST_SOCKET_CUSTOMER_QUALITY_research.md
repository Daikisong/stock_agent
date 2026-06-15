# E2R Stock-Web v12 Residual Research — R2 / Loop 100

```yaml
scheduled_round: R2
scheduled_loop: 100
large_sector_id: L2_AI_SEMICONDUCTOR_ELECTRONICS
canonical_archetype_id: C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY
fine_archetype_id: TEST_SOCKET_PROBE_CARD_TEST_INTERFACE_CUSTOMER_QUALIFICATION_REPEAT_CONSUMABLE_MARGIN_BRIDGE_VS_TEST_SOCKET_LABEL_SPIKE

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
hard_4c_secondary_guard_count: 1

probe_card_test_interface_case_count: 1
test_interface_socket_case_count: 1
test_socket_consumable_case_count: 1
customer_qualification_bridge_count: 1
repeat_consumable_margin_bridge_missing_count: 2
delivery_conversion_margin_bridge_missing_count: 2
valuation_late_chase_or_label_overheat_count: 2
short_listing_or_market_segment_caveat_count: 2
old_corporate_action_or_row_trust_caveat_count: 3
calibration_usable_trigger_count: 3

loop_contribution_label: residual_error_found
canonical_archetype_rule_candidate: true
do_not_propose_new_weight_delta: true

completed_round: R2
completed_loop: 100
next_round: R3
next_loop: 100
round_schedule_status: valid
round_sector_consistency: pass
```

---

## 1. Schedule resolution

Previous completed file in the active sequence was:

```text
e2r_stock_web_v12_residual_round_R1_loop_100_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C02_POWER_GRID_DATACENTER_CAPEX_research.md
```

Under v12:

```text
R1 -> R2 -> R3 -> R4 -> R5 -> R6 -> R7 -> R8 -> R9 -> R10 -> R11 -> R12 -> R13 -> R1
```

Therefore:

```text
scheduled_round = R2
scheduled_loop = 100
large_sector_id = L2_AI_SEMICONDUCTOR_ELECTRONICS
```

R2 canonical mapping allows:

```text
C06~C10 -> R2 / L2_AI_SEMICONDUCTOR_ELECTRONICS
```

Selected archetype:

```text
C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY
```

The No-Repeat Index shows C08 remains the thinnest current priority:

```text
C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY
rows: 14
need_to_30: 16
need_to_50: 36
research point: customer qualification, repeat consumable demand, socket/test margin, delivery conversion counterexamples
```

Selected fine branch:

```text
test socket / probe card / test interface consumable
customer qualification, device/package compatibility, yield/quality, delivery conversion,
repeat consumable demand, ASP/mix, labor/material cost, working capital,
and gross-margin / OP bridge
vs generic semi-test socket label spike
```

---

## 2. No-repeat / novelty check

Hard duplicate key:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

Selected symbols:

```text
131290 티에스이
425420 티에프이
098120 마이크로컨텍솔
```

They avoid the recent R2 loop97~100 names already used in this local run history:

```text
loop100 C02 was R1 and unrelated.
loop99 C06: 089030, 353200, 195870
loop98 C10: 074600, 101160, 253590
loop97 C09: 084370, 036930, 083310
loop96 C08: not repeated in this visible run segment.
```

Novelty classification:

```text
131290:
  same archetype, new checked symbol in this visible run segment,
  probe-card / test-interface customer qualification positive with Green cap.

425420:
  same archetype, new checked symbol,
  test interface / socket local 4B after large MFE and later hard-zone MAE.

098120:
  same archetype, new checked symbol,
  test socket / connector consumable hard-4C candidate after shallow MFE and severe MAE.
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
131290 티에스이
  profile: atlas/symbol_profiles/131/131290.json
  first_date: 2011-01-05
  last_date: 2026-02-20
  market:
    KOSDAQ
    KOSDAQ GLOBAL from 2022-11-21 to 2024-06-13
  tradable_ohlcv rows: 3,719
  non_tradable_zero_volume rows: 0
  corporate_action_candidate_dates:
    2011-04-05, 2011-04-28
  2024 entry~D+180 contamination: none
  caveat:
    old corporate-action candidates and KOSDAQ GLOBAL segment history are outside / around the selected validation window but not direct raw-price contamination.

425420 티에프이
  profile: atlas/symbol_profiles/425/425420.json
  first_date: 2022-11-17
  last_date: 2026-02-20
  market: KOSDAQ
  tradable_ohlcv rows: 795
  non_tradable_zero_volume rows: 0
  corporate_action_candidate_dates: none
  2024 entry~D+180 contamination: none
  caveat:
    short listing history versus older semiconductor test names.

098120 마이크로컨텍솔
  profile: atlas/symbol_profiles/098/098120.json
  first_date: 2008-09-23
  last_date: 2026-02-20
  market: KOSDAQ
  tradable_ohlcv rows: 4,294
  non_tradable_zero_volume rows: 0
  corporate_action_candidate_dates:
    2011-04-19, 2011-05-17
  2024 entry~D+180 contamination: none
  caveat:
    old corporate-action candidates are outside selected 2024 validation window.
```

---

## 4. Archetype residual problem

C08 is about semiconductor test socket / customer qualification / repeat consumable quality. It is not merely a generic "semi test socket stock is hot" archetype.

The model can over-score:

```text
test socket label
probe card / test interface label
AI semiconductor package readthrough
HBM or advanced package test sympathy
customer qualification rumor
socket consumable replacement-cycle headline
one-week semiconductor test volume spike
late chase after a socket/test-interface rerating
```

The C08 bridge must be stricter:

```text
semi-test socket / probe-card / interface event
  -> named customer, device, package, process, or test step
  -> customer qualification and quality approval
  -> delivery conversion and repeat order cadence
  -> socket/probe card consumable replacement cycle
  -> ASP / mix and customer concentration
  -> yield, defect, warranty, and field-return control
  -> capacity, lead-time, labor, and material bottleneck
  -> inventory and working-capital timing
  -> gross-margin / OP conversion
  -> valuation discipline after the first socket / test-label spike
  -> price survival after the rerating
```

A C08 thesis is like a test socket clipped onto a customer's new package. The socket may touch the hottest chip, but equity value appears only when the customer qualifies it, repeat orders arrive, consumable replacement becomes visible, quality does not fail, and the high ASP survives into gross margin.

---

## 5. Case 1 — 131290 티에스이

```yaml
case_id: C08_R2L100_131290_2024_02_01
symbol: "131290"
name: "티에스이"
canonical_archetype_id: C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY
fine_archetype_id: TEST_SOCKET_PROBE_CARD_TEST_INTERFACE_CUSTOMER_QUALIFICATION_REPEAT_CONSUMABLE_MARGIN_BRIDGE_VS_TEST_SOCKET_LABEL_SPIKE
trigger_date: 2024-02-01
entry_date: 2024-02-01
entry_price_basis: close
entry_price: 43500
classification: positive_probe_card_test_interface_customer_qualification_repeat_consumable_margin_bridge_with_green_cap
calibration_usable: true
```

### Evidence interpretation

티에스이 is the constructive C08 positive.

The useful C08 read is not simply:

```text
반도체 테스트 / 소켓주가 강하다
```

It is:

```text
probe-card / test-interface relevance
  -> advanced package and AI-memory test demand readthrough
  -> customer qualification and repeat consumable optionality
  -> ASP / mix and margin leverage
  -> strong April-May price confirmation
```

The price path produced a very large MFE and avoided hard drawdown. This preserves positive classification. However, after a large rerating, C08 Green should remain capped unless customer qualification, repeat order cadence, delivery conversion, quality/yield, ASP/mix, and margin evidence are current.

### Price path

Key Stock-Web rows:

```text
2024-02-01: high 45,000 / low 42,400 / close 43,500
2024-02-13: high 59,400 / close 57,000
2024-02-22: high 62,500 / close 61,300
2024-03-28: high 65,600 / close 62,600
2024-04-04: high 69,200 / close 67,400
2024-04-26: high 82,300 / close 79,000
2024-05-03: high 87,800 / close 80,000
2024-08-05: low 38,050 / close 38,800
2024-10-24: high 55,500 / close 55,100
```

Approximate path from entry close:

```text
entry_close: 43,500
peak_high: 87,800
MFE: +101.8%
worst_low_after_entry: 38,050
MAE: -12.5%
```

### Interpretation

This is a C08 positive with Green cap:

```text
Stage2-Actionable: possible if named customer/device/package, qualification, repeat demand, ASP/mix, and margin bridge are explicit.
Stage3-Green: blocked after +100% MFE unless fresh qualification/repeat-order/margin evidence appears.
Local 4B: monitor if price outruns delivery and quality evidence.
Hard 4C: no.
```

### Stress-test components

```text
raw_component_score_proxy:
  probe_card_test_interface_relevance: high
  customer_qualification_bridge: medium_high
  repeat_consumable_bridge: medium_high
  asp_mix_bridge: medium_high
  quality_yield_bridge: medium
  margin_op_bridge: medium
  valuation_overheat_risk: high
  price_confirmation: very_high
  drawdown_penalty: low_to_medium
  green_cap: required_after_large_mfe
```

---

## 6. Case 2 — 425420 티에프이

```yaml
case_id: C08_R2L100_425420_2024_02_01
symbol: "425420"
name: "티에프이"
canonical_archetype_id: C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY
fine_archetype_id: TEST_SOCKET_PROBE_CARD_TEST_INTERFACE_CUSTOMER_QUALIFICATION_REPEAT_CONSUMABLE_MARGIN_BRIDGE_VS_TEST_SOCKET_LABEL_SPIKE
trigger_date: 2024-02-01
entry_date: 2024-02-01
entry_price_basis: close
entry_price: 28800
classification: local_burst_test_interface_socket_label_high_mae_4b_failure_with_hard_4c_secondary_guard
calibration_usable: true
```

### Evidence interpretation

티에프이 is the test interface / socket local-burst failure.

The setup had real C08 relevance:

```text
test socket / test interface
  -> AI semiconductor package test readthrough
  -> customer qualification and delivery optionality
  -> February-March price confirmation
```

But the path did not sustain price survival. The stock produced meaningful MFE first, then entered a hard drawdown zone by the second half. This is not a zero-response failure; it is a local 4B failure with a hard-4C secondary guard for stale or late entries.

### Price path

Key Stock-Web rows:

```text
2024-02-01: high 30,300 / low 28,350 / close 28,800
2024-02-08: high 35,950 / close 35,200
2024-03-08: high 41,950 / close 38,850
2024-03-20: high 43,850 / close 43,100
2024-03-21: high 43,950 / close 41,800
2024-08-05: low 16,520 / close 17,490
2024-09-06: low 14,730 / close 15,200
2024-11-07: low 14,420
```

Approximate path from entry close:

```text
entry_close: 28,800
peak_high: 43,950
MFE: +52.6%
worst_low_after_entry: 14,420
MAE: -49.9%
```

### Interpretation

This is a C08 local 4B failure:

```text
Stage2-Watch: valid from test socket / test-interface relevance.
Stage2-Actionable: possible only if customer qualification, repeat consumable order, delivery conversion, and margin bridge are explicit.
Stage3-Green: blocked after hard-zone MAE.
Local 4B: required because large MFE came first.
Hard 4C secondary guard: yes for stale or late entries.
```

### Stress-test components

```text
raw_component_score_proxy:
  test_interface_socket_relevance: high
  customer_qualification_bridge: medium
  repeat_consumable_bridge: weak_to_medium
  delivery_conversion_bridge: weak_to_medium
  quality_yield_bridge: weak_to_medium
  margin_op_bridge: weak_to_medium
  price_confirmation: high_initial
  later_drawdown_penalty: high
  local_4b_overlay: required
```

---

## 7. Case 3 — 098120 마이크로컨텍솔

```yaml
case_id: C08_R2L100_098120_2024_02_01
symbol: "098120"
name: "마이크로컨텍솔"
canonical_archetype_id: C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY
fine_archetype_id: TEST_SOCKET_PROBE_CARD_TEST_INTERFACE_CUSTOMER_QUALIFICATION_REPEAT_CONSUMABLE_MARGIN_BRIDGE_VS_TEST_SOCKET_LABEL_SPIKE
trigger_date: 2024-02-01
entry_date: 2024-02-01
entry_price_basis: close
entry_price: 10980
classification: hard_4c_candidate_test_socket_connector_consumable_label_without_customer_qualification_repeat_margin_survival
calibration_usable: true
```

### Evidence interpretation

마이크로컨텍솔 is the hard C08 guardrail.

The label can fool the model:

```text
test socket / connector consumable
  -> semiconductor recovery and package test readthrough
  -> customer qualification optionality
  -> repeat consumable replacement-cycle story
```

But from the selected February entry, the forward path produced only shallow MFE and then crossed a severe drawdown zone. The bridge from socket/connector label to customer qualification, repeat order cadence, ASP/mix, quality/yield, and margin survival was not proven.

### Price path

Key Stock-Web rows:

```text
2024-02-01: high 11,330 / low 10,700 / close 10,980
2024-02-14: high 11,860 / close 11,540
2024-03-08: high 11,700 / close 11,450
2024-04-08: low 9,010 / close 9,010
2024-08-05: low 5,510 / close 5,680
2024-09-09: low 4,965 / close 5,340
2024-10-25: low 5,130 / close 5,180
```

Approximate path from entry close:

```text
entry_close: 10,980
peak_high: 11,860
MFE: +8.0%
worst_low_after_entry: 4,965
MAE: -54.8%
```

### Interpretation

This is a hard C08 false-positive candidate:

```text
Stage2-Watch: possible from test socket / connector consumable relevance.
Stage2-Actionable: blocked unless customer qualification, delivery conversion, repeat order cadence, and margin bridge are explicit.
Stage3-Green: blocked.
Hard 4C: yes by shallow MFE and severe MAE.
```

The lesson is that a socket label is not customer-qualified repeat consumable demand by itself.

### Stress-test components

```text
raw_component_score_proxy:
  test_socket_connector_label: high
  semiconductor_recovery_beta: medium_high
  customer_qualification_bridge: weak
  repeat_consumable_bridge: weak
  quality_yield_bridge: weak_to_medium
  margin_op_bridge: weak
  price_confirmation: shallow
  drawdown_penalty: severe
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
hard_4c_secondary_guard_count: 1
probe_card_test_interface_case_count: 1
test_interface_socket_case_count: 1
test_socket_consumable_case_count: 1
customer_qualification_bridge_count: 1
repeat_consumable_margin_bridge_missing_count: 2
delivery_conversion_margin_bridge_missing_count: 2
valuation_late_chase_or_label_overheat_count: 2
short_listing_or_market_segment_caveat_count: 2
old_corporate_action_or_row_trust_caveat_count: 3
calibration_usable_trigger_count: 3
```

The three-case C08 semiconductor test grid:

```text
131290 티에스이:
  probe-card / test-interface positive;
  very large MFE and non-hard MAE, but Green requires fresh qualification, repeat-order, quality, and margin evidence.

425420 티에프이:
  test-interface / socket local 4B failure;
  large MFE first, then hard-zone MAE, hard-4C secondary guard.

098120 마이크로컨텍솔:
  test socket / connector consumable label failed;
  shallow MFE and severe MAE, hard 4C candidate.
```

Shared rule:

```text
C08 is not "test socket label is hot."
C08 is "customer qualification, repeat consumable demand, delivery conversion, quality/yield, ASP/mix, and margin conversion are visible."
```

---

## 9. Machine-readable JSONL rows

```jsonl
{"row_type":"case","case_id":"C08_R2L100_131290_2024_02_01","scheduled_round":"R2","scheduled_loop":100,"large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY","fine_archetype_id":"TEST_SOCKET_PROBE_CARD_TEST_INTERFACE_CUSTOMER_QUALIFICATION_REPEAT_CONSUMABLE_MARGIN_BRIDGE_VS_TEST_SOCKET_LABEL_SPIKE","symbol":"131290","name":"티에스이","trigger_date":"2024-02-01","entry_date":"2024-02-01","entry_price":43500,"peak_high":87800,"peak_date":"2024-05-03","worst_low_after_entry":38050,"worst_low_after_entry_date":"2024-08-05","mfe_pct":101.8,"mae_pct":-12.5,"classification":"positive_probe_card_test_interface_customer_qualification_repeat_consumable_margin_bridge_with_green_cap","calibration_usable":true,"market_segment_or_old_corporate_action_caveat":true,"evidence_family":"probe_card_test_interface_customer_qualification_repeat_consumable_asp_mix_quality_margin_bridge","residual_error":"probe_card_test_interface_positive_requires_green_cap_after_large_mfe_without_refreshed_customer_qualification_repeat_order_and_margin_evidence","shadow_rule_candidate":"allow_capped_actionable_when_customer_qualification_repeat_consumable_and_margin_bridge_confirm_but_cap_green_after_large_mfe"}
{"row_type":"case","case_id":"C08_R2L100_425420_2024_02_01","scheduled_round":"R2","scheduled_loop":100,"large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY","fine_archetype_id":"TEST_SOCKET_PROBE_CARD_TEST_INTERFACE_CUSTOMER_QUALIFICATION_REPEAT_CONSUMABLE_MARGIN_BRIDGE_VS_TEST_SOCKET_LABEL_SPIKE","symbol":"425420","name":"티에프이","trigger_date":"2024-02-01","entry_date":"2024-02-01","entry_price":28800,"peak_high":43950,"peak_date":"2024-03-21","worst_low_after_entry":14420,"worst_low_after_entry_date":"2024-11-07","mfe_pct":52.6,"mae_pct":-49.9,"classification":"local_burst_test_interface_socket_label_high_mae_4b_failure_with_hard_4c_secondary_guard","calibration_usable":true,"short_listing_or_history_caveat":true,"evidence_family":"test_interface_socket_label_without_sustained_customer_qualification_repeat_order_delivery_conversion_margin_survival","residual_error":"test_socket_interface_label_can_create_large_mfe_but_fail_green_when_qualification_repeat_order_and_margin_bridge_breaks","shadow_rule_candidate":"classify_large_mfe_then_hard_zone_mae_test_interface_cases_as_local_4b_with_hard_4c_secondary_guard"}
{"row_type":"case","case_id":"C08_R2L100_098120_2024_02_01","scheduled_round":"R2","scheduled_loop":100,"large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY","fine_archetype_id":"TEST_SOCKET_PROBE_CARD_TEST_INTERFACE_CUSTOMER_QUALIFICATION_REPEAT_CONSUMABLE_MARGIN_BRIDGE_VS_TEST_SOCKET_LABEL_SPIKE","symbol":"098120","name":"마이크로컨텍솔","trigger_date":"2024-02-01","entry_date":"2024-02-01","entry_price":10980,"peak_high":11860,"peak_date":"2024-02-14","worst_low_after_entry":4965,"worst_low_after_entry_date":"2024-09-09","mfe_pct":8.0,"mae_pct":-54.8,"classification":"hard_4c_candidate_test_socket_connector_consumable_label_without_customer_qualification_repeat_margin_survival","calibration_usable":true,"old_corporate_action_caveat_outside_window":true,"evidence_family":"test_socket_connector_consumable_label_without_customer_qualification_repeat_order_quality_margin_bridge","residual_error":"test_socket_consumable_label_can_fail_when_customer_qualification_repeat_order_and_margin_bridge_missing","shadow_rule_candidate":"route_test_socket_connector_label_to_hard_4c_if_mfe_shallow_mae_severe_and_qualification_margin_bridge_missing"}
```

```jsonl
{"row_type":"aggregate","scheduled_round":"R2","scheduled_loop":100,"large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY","fine_archetype_id":"TEST_SOCKET_PROBE_CARD_TEST_INTERFACE_CUSTOMER_QUALIFICATION_REPEAT_CONSUMABLE_MARGIN_BRIDGE_VS_TEST_SOCKET_LABEL_SPIKE","case_count":3,"positive_case_count":1,"counterexample_count":2,"watch_or_cap_case_count":2,"local_4b_overlay_case_count":1,"hard_4c_candidate_count":1,"hard_4c_secondary_guard_count":1,"probe_card_test_interface_case_count":1,"test_interface_socket_case_count":1,"test_socket_consumable_case_count":1,"customer_qualification_bridge_count":1,"repeat_consumable_margin_bridge_missing_count":2,"delivery_conversion_margin_bridge_missing_count":2,"valuation_late_chase_or_label_overheat_count":2,"short_listing_or_market_segment_caveat_count":2,"old_corporate_action_or_row_trust_caveat_count":3,"calibration_usable_trigger_count":3,"loop_contribution_label":"residual_error_found","do_not_propose_new_weight_delta":true}
{"row_type":"shadow_rule","scheduled_round":"R2","scheduled_loop":100,"canonical_archetype_id":"C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY","rule_id":"C08_TEST_SOCKET_CUSTOMER_QUALIFICATION_REPEAT_CONSUMABLE_MARGIN_BRIDGE_REQUIRED","rule_type":"canonical_archetype_specific_guard","rule_text":"For C08 semiconductor test socket/probe-card/test-interface cases, do not open Stage2-Actionable or Stage3-Green from test socket, probe card, test interface, AI semiconductor package readthrough, HBM/advanced package test sympathy, customer qualification rumor, socket consumable replacement-cycle headline, one-week semiconductor-test volume spike, or late chase after socket/test-interface rerating labels alone. Require named customer/device/package/process/test step, customer qualification and quality approval, delivery conversion and repeat order cadence, socket/probe-card consumable replacement cycle, ASP/mix and customer concentration, yield/defect/warranty/field-return control, capacity/lead-time/labor/material bottleneck check, inventory and working-capital timing, gross-margin/OP conversion, valuation discipline after the first socket/test-label spike, and post-trigger price survival. Probe-card/test-interface positives with large MFE may be capped Actionable when qualification/repeat-order/margin bridge is explicit, but Green requires fresh evidence. Test-interface/socket names with large MFE followed by hard-zone MAE should remain local 4B and receive hard-4C secondary guard when qualification and margin evidence is stale. Test socket/connector labels with shallow MFE and severe MAE should route to hard-4C when qualification, repeat demand, and margin bridge are missing.","expected_effect":"Preserve true test-socket/probe-card customer-quality positives while reducing generic socket, interface, package-test, HBM sympathy, qualification-rumor, replacement-cycle, and late-chase false positives where qualification, repeat order, quality/yield, working capital, and OP margin evidence fail.","production_scoring_changed":false,"shadow_weight_only":true}
{"row_type":"residual_contribution","scheduled_round":"R2","scheduled_loop":100,"canonical_archetype_id":"C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY","residual_type":"test_socket_customer_qualification_repeat_consumable_margin_guard","contribution":"Adds one probe-card/test-interface positive, one test-interface local 4B failure, and one test-socket hard-4C counterexample to calibrate C08 customer qualification, repeat consumable order, delivery conversion, quality/yield, ASP/mix, working capital, valuation discipline, and OP margin requirements.","do_not_count_as_global_weight_delta":true}
```

---

## 10. Proposed canonical-archetype shadow rule

```text
C08_TEST_SOCKET_CUSTOMER_QUALIFICATION_REPEAT_CONSUMABLE_MARGIN_BRIDGE_REQUIRED

IF canonical_archetype_id == C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY:

  Do not open Stage3-Green from:
    - test socket label alone
    - probe card / test interface label alone
    - AI semiconductor package readthrough alone
    - HBM or advanced package test sympathy alone
    - customer qualification rumor alone
    - socket consumable replacement-cycle headline alone
    - one-week semiconductor test volume spike alone
    - late chase after socket/test-interface rerating alone

  Require at least two of:
    - named customer / device / package / process / test step
    - customer qualification and quality approval
    - delivery conversion and repeat order cadence
    - socket / probe card consumable replacement cycle
    - ASP / mix and customer concentration
    - yield / defect / warranty / field-return control
    - capacity / lead-time / labor / material bottleneck check
    - inventory and working-capital timing
    - gross margin / OP conversion
    - valuation discipline after first socket/test-label spike
    - low-MAE post-trigger price survival
    - fresh evidence after the semiconductor-test headline

  If MFE < 10% and MAE <= -35%:
    route to C08 hard-4C candidate.

  If MFE is large but later MAE enters hard zone:
    preserve as local 4B and attach hard-4C secondary guard for stale or late entries.

  If MFE is large but qualification / repeat-order / margin evidence is stale:
    cap Green until fresh customer-quality evidence appears.

  If market-segment, short-listing, row-presence, or old corporate-action caveat exists:
    apply trust cap but do not contaminate clean 2024 rows without direct raw discontinuity.

  Distinguish:
    - names where socket/test interface salience becomes customer qualification, repeat consumable orders, quality approval, and OP margin
    - from labels where package-test excitement rerates first and qualification/margin proof fails.
```

---

## 11. Deferred Coding Agent Handoff Prompt

```text
You are a coding agent working on Songdaiki/stock_agent.

Do not treat this research MD as production scoring by itself.
Batch it with other v12 residual research files.

Source file:
e2r_stock_web_v12_residual_round_R2_loop_100_L2_AI_SEMICONDUCTOR_ELECTRONICS_C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY_research.md

Task:
1. Parse machine-readable JSONL rows.
2. Add the three C08 semiconductor test socket / customer quality cases to calibration research ingestion.
3. Preserve production_scoring_changed=false.
4. Treat the proposed rule only as a shadow canonical-archetype guard candidate:
   C08_TEST_SOCKET_CUSTOMER_QUALIFICATION_REPEAT_CONSUMABLE_MARGIN_BRIDGE_REQUIRED.
5. Do not change global weights directly.
6. Compare against existing C08 cases and deduplicate by:
   canonical_archetype_id + symbol + trigger_type + entry_date.
7. If enough C08 cases agree, consider implementing a canonical guard that:
   - blocks test-socket Green without named customer/device/package, qualification, quality approval, repeat order, and margin bridge,
   - preserves probe-card/test-interface positives only with price survival and fresh qualification/repeat-order evidence,
   - treats large-MFE/hard-MAE test-interface cases as local 4B with hard-4C secondary guard,
   - routes shallow-MFE/severe-MAE socket/connector labels to hard-4C,
   - applies market-segment, short-listing, row-presence, and old corporate-action caveats.

Expected next schedule:
completed_round = R2
completed_loop = 100
next_round = R3
next_loop = 100
round_schedule_status = valid
round_sector_consistency = pass
```

---

## 12. Required round-state footer

```text
completed_round = R2
completed_loop = 100
next_round = R3
next_loop = 100
round_schedule_status = valid
round_sector_consistency = pass
```
