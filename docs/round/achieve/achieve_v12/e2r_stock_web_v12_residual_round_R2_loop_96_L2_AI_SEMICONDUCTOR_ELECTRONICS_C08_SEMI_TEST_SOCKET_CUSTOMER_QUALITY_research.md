# E2R Stock-Web v12 Residual Research — R2 / Loop 96

```yaml
scheduled_round: R2
scheduled_loop: 96
large_sector_id: L2_AI_SEMICONDUCTOR_ELECTRONICS
canonical_archetype_id: C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY
fine_archetype_id: MEMORY_TEST_EQUIPMENT_OSAT_PACKAGE_TEST_CUSTOMER_QUALITY_BRIDGE_VS_TEST_LABEL_LATE_CHASE

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
corporate_action_cutoff_case_count: 1
test_equipment_case_count: 1
osat_package_test_case_count: 2
calibration_usable_trigger_count: 3

loop_contribution_label: residual_error_found
canonical_archetype_rule_candidate: true
do_not_propose_new_weight_delta: true

completed_round: R2
completed_loop: 96
next_round: R3
next_loop: 96
round_schedule_status: valid
round_sector_consistency: pass
```

---

## 1. Schedule resolution

Previous completed file in the active sequence was:

```text
e2r_stock_web_v12_residual_round_R1_loop_96_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C01_ORDER_BACKLOG_MARGIN_BRIDGE_research.md
```

Under v12:

```text
R1 -> R2 -> R3 -> R4 -> R5 -> R6 -> R7 -> R8 -> R9 -> R10 -> R11 -> R12 -> R13 -> R1
```

Therefore:

```text
scheduled_round = R2
scheduled_loop = 96
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
loop95: C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH
```

This run returns to C08 after the R2 branch cycle, but avoids the C08 top-covered names and uses a different fine branch:

```text
memory test equipment / OSAT package-test
customer qualification, utilization, quality, delivery, and margin bridge
vs generic semiconductor-test label late chase
```

---

## 2. No-repeat / novelty check

No-Repeat Index coverage snapshot:

```text
C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY
rows: 21
symbols: 11
date_range: 2024-01-23~2024-08-01
good/bad S2: 9/5
4B/4C: 2/0
URL pending/proxy: 3/3
top covered symbols:
  UNKNOWN_SYMBOL(6), 089030(2), 095340(2), 131290(2), 252990(2), 058470(1)
```

Selected symbols:

```text
092870 엑시콘
067310 하나마이크론
097800 윈팩
```

They avoid the C08 top-covered list and avoid the most recent R2 loop95 C07 names:

```text
loop95 avoid: 039030, 083450, 095610
```

Hard duplicate key:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

Novelty classification:

```text
092870: same archetype, new symbol, memory-test equipment positive with corporate-action cutoff and 4B after large MFE
067310: same archetype, new symbol, OSAT/package-test local burst followed by high-MAE 4B failure
097800: same archetype, new symbol, post-corporate-action package-test label hard-4C without customer-quality margin survival
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
092870 엑시콘
  profile: atlas/symbol_profiles/092/092870.json
  first_date: 2014-12-24
  last_date: 2026-02-20
  market:
    KONEX until 2015-10-21
    KOSDAQ from 2015-10-22
  tradable_ohlcv rows: 2,730
  non_tradable_zero_volume rows: 7
  corporate_action_candidate_dates:
    2015-10-22, 2024-07-31
  selected validation:
    uses 2024-02-14 entry and blocks post-2024-07-31 rows for the main MFE/MAE read
  2024 entry~pre-2024-07-31 validation: usable with caveat

067310 하나마이크론
  profile: atlas/symbol_profiles/067/067310.json
  first_date: 2005-10-11
  last_date: 2026-02-20
  market:
    KOSDAQ, KOSDAQ GLOBAL segment 2022-11-21 to 2024-06-13
  tradable_ohlcv rows: 5,024
  corporate_action_candidate_dates:
    2009-11-10, 2021-12-29
  2024 entry~D+180 contamination: none

097800 윈팩
  profile: atlas/symbol_profiles/097/097800.json
  first_date: 2013-03-07
  last_date: 2026-02-20
  market: KOSDAQ
  tradable_ohlcv rows: 3,181
  corporate_action_candidate_dates:
    2017-12-22, 2024-05-31
  selected entry:
    2024-08-01, after the 2024-05-31 corporate-action candidate window
  entry~D+180 contamination: avoided
```

---

## 4. Archetype residual problem

C08 is about semiconductor test, socket, customer quality, OSAT/package-test utilization, and the conversion of customer qualification into margin. It is not a generic "semiconductor test stock went up" archetype.

The model can over-score:

```text
semiconductor test label
memory tester / SSD tester / package-test label
OSAT recovery label
customer qualification or customer-quality rumor
HBM / AI server memory readthrough
one-week test-stock volume spike
late chase after a test-equipment rerating
```

The C08 bridge must be stricter:

```text
semiconductor test / socket / OSAT event
  -> named customer, product, or process step
  -> qualification / customer-quality status
  -> purchase order or test capacity allocation
  -> utilization and delivery schedule
  -> yield / quality / defect risk
  -> ASP / mix / consumable or service margin
  -> working-capital and capex risk
  -> price survival after the first test-label spike
```

A semiconductor-test thesis is like a probe station in a cleanroom. The label says chips need testing, but C08 asks whether this company's socket or tester is qualified, used at enough utilization, paid for at margin, and not rejected by yield or customer-quality issues.

---

## 5. Case 1 — 092870 엑시콘

```yaml
case_id: C08_R2L96_092870_2024_02_14
symbol: "092870"
name: "엑시콘"
canonical_archetype_id: C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY
fine_archetype_id: MEMORY_TEST_EQUIPMENT_OSAT_PACKAGE_TEST_CUSTOMER_QUALITY_BRIDGE_VS_TEST_LABEL_LATE_CHASE
trigger_date: 2024-02-14
entry_date: 2024-02-14
entry_price_basis: close
entry_price: 19300
classification: positive_memory_test_equipment_customer_quality_bridge_with_corporate_action_cutoff_and_4b_after_large_mfe
calibration_usable: true
```

### Evidence interpretation

엑시콘 is the constructive C08 control in this set.

The useful C08 read is not simply:

```text
반도체 테스트 장비주가 강하다
```

It is:

```text
memory test equipment relevance
  -> AI/HBM/server-memory test demand readthrough
  -> customer qualification and order optionality
  -> strong price confirmation before corporate-action cutoff
```

The forward path delivered very large MFE before the 2024-07-31 corporate-action candidate window. Because a 2024 raw-price discontinuity candidate appears later, post-candidate rows are blocked for the main read. The positive is preserved, but a 4B overlay is required after the large rerating unless fresh customer qualification, order, and margin evidence appears.

### Price path

Key Stock-Web rows:

```text
2024-02-14: high 20,750 / close 19,300
2024-03-07: high 25,300 / close 22,600
2024-03-12: high 30,600 / close 30,600
2024-03-20: high 32,350 / close 30,750
2024-04-02: high 35,400 / close 33,350
2024-04-24: low 21,400 / close 22,800
2024-07-31: corporate-action candidate window; post-candidate rows blocked
```

Approximate path from entry close, pre-corporate-action candidate:

```text
entry_close: 19,300
peak_high_before_candidate: 35,400
MFE: +83.4%
worst_low_before_candidate: 17,000
MAE: -11.9%
```

### Interpretation

This is a C08 positive with corporate-action cutoff and 4B:

```text
Stage2-Actionable: valid if customer/process, qualification, order visibility, and margin bridge are explicit.
Stage3-Green: possible only with current customer qualification, delivery, utilization, and OP evidence.
Local 4B: required after +80% MFE unless fresh evidence appears.
Hard 4C: no.
Corporate-action caveat: post-2024-07-31 rows blocked.
```

### Stress-test components

```text
raw_component_score_proxy:
  memory_test_equipment_relevance: high
  customer_qualification_bridge: medium_high
  order_visibility_bridge: medium_high
  price_confirmation: very_high
  margin_bridge: medium
  corporate_action_cutoff: required
  local_4b_overlay: required_after_large_mfe
```

---

## 6. Case 2 — 067310 하나마이크론

```yaml
case_id: C08_R2L96_067310_2024_02_01
symbol: "067310"
name: "하나마이크론"
canonical_archetype_id: C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY
fine_archetype_id: MEMORY_TEST_EQUIPMENT_OSAT_PACKAGE_TEST_CUSTOMER_QUALITY_BRIDGE_VS_TEST_LABEL_LATE_CHASE
trigger_date: 2024-02-01
entry_date: 2024-02-01
entry_price_basis: close
entry_price: 24600
classification: local_burst_osat_package_test_customer_quality_label_high_mae_4b_failure
calibration_usable: true
```

### Evidence interpretation

하나마이크론 is the OSAT/package-test local-burst 4B failure.

The setup had real C08 relevance:

```text
OSAT / package-test platform
  -> memory and advanced package demand
  -> customer capacity and quality optionality
  -> early price confirmation
```

The forward path produced a meaningful MFE into March/April, so the original trigger is not a pure hard-4C. But the later path failed price survival badly. This should be a local 4B / event-burst case unless customer allocation, utilization, quality, and margin evidence keeps refreshing.

### Price path

Key Stock-Web rows:

```text
2024-02-01: high 25,950 / close 24,600
2024-03-27: high 29,750 / close 28,150
2024-04-04: high 34,500 / close 33,300
2024-04-17: low 28,450 / close 28,900
2024-08-05: low 15,400 / close 15,950
2024-09-09: low 10,700 / close 11,220
2024-10-25: low 10,300 / close 10,390
```

Approximate path from entry close:

```text
entry_close: 24,600
peak_high: 34,500
MFE: +40.2%
worst_low_after_entry: 10,300
MAE: -58.1%
```

### Interpretation

This is a C08 local burst / 4B failure:

```text
Stage2-Watch: valid from OSAT/package-test relevance.
Stage2-Actionable: possible only if customer allocation, utilization, quality, and margin bridge are explicit.
Stage3-Green: blocked after later high-MAE reversal.
Local 4B: required.
Hard 4C: not primary for the original entry because meaningful MFE came first.
```

### Stress-test components

```text
raw_component_score_proxy:
  osat_package_test_relevance: high
  customer_quality_bridge: medium
  utilization_bridge: medium
  price_confirmation: high_initial
  margin_survival: failed
  later_drawdown_penalty: extreme
  local_4b_overlay: required
```

---

## 7. Case 3 — 097800 윈팩

```yaml
case_id: C08_R2L96_097800_2024_08_01
symbol: "097800"
name: "윈팩"
canonical_archetype_id: C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY
fine_archetype_id: MEMORY_TEST_EQUIPMENT_OSAT_PACKAGE_TEST_CUSTOMER_QUALITY_BRIDGE_VS_TEST_LABEL_LATE_CHASE
trigger_date: 2024-08-01
entry_date: 2024-08-01
entry_price_basis: close
entry_price: 2010
classification: hard_4c_candidate_post_corporate_action_package_test_label_without_customer_quality_margin_survival
calibration_usable: true
```

### Evidence interpretation

윈팩 is the hard C08 guardrail.

The profile has a 2024-05-31 corporate-action candidate. To avoid raw-price contamination, this case uses a post-candidate entry in August.

The label can fool the model:

```text
package-test / backend semiconductor service
  -> memory test recovery
  -> OSAT/customer-quality label
  -> one-week post-event semiconductor-test volume
```

But from the selected post-candidate entry, the forward path did not validate customer quality, utilization, or margin survival. MFE was shallow relative to the later drawdown.

### Price path

Key Stock-Web rows:

```text
2024-05-31: corporate-action candidate window in profile
2024-08-01: high 2,195 / close 2,010
2024-08-05: low 1,415 / close 1,664
2024-09-06: low 1,405 / close 1,414
2024-10-15: high 1,695 / close 1,633
2024-11-05: low 1,082 / close 1,082
```

Approximate path from post-candidate entry close:

```text
entry_close: 2,010
peak_high_after_entry: 2,195
MFE: +9.2%
worst_low_after_entry: 1,082
MAE: -46.2%
```

### Interpretation

This is a hard C08 false-positive:

```text
Stage2-Watch: possible from package-test and OSAT relevance.
Stage2-Actionable: blocked unless customer allocation, test utilization, quality, and margin bridge are explicit.
Stage3-Green: blocked.
Hard 4C: yes by shallow MFE and -40%+ MAE.
Corporate-action caveat: avoided by post-candidate entry.
```

The lesson is that package-test label is not customer-quality margin survival.

### Stress-test components

```text
raw_component_score_proxy:
  package_test_label: high
  osat_recovery_readthrough: medium_high
  customer_quality_bridge: weak
  utilization_margin_bridge: weak
  price_confirmation: shallow
  drawdown_penalty: high
  corporate_action_caveat_avoided: yes
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
corporate_action_cutoff_case_count: 1
test_equipment_case_count: 1
osat_package_test_case_count: 2
calibration_usable_trigger_count: 3
```

The three-case C08 test/package grid:

```text
092870 엑시콘:
  memory-test equipment positive;
  large MFE before corporate-action cutoff, but 4B required after rerating.

067310 하나마이크론:
  OSAT/package-test local burst;
  meaningful MFE first, then extreme MAE, local 4B failure.

097800 윈팩:
  package-test label failed after post-corporate-action entry;
  shallow MFE and high MAE, hard 4C.
```

Shared rule:

```text
C08 is not "semiconductor test label."
C08 is "customer qualification, test utilization, process step, yield/quality, order visibility, and margin survival are visible for this company."
```

---

## 9. Machine-readable JSONL rows

```jsonl
{"row_type":"case","case_id":"C08_R2L96_092870_2024_02_14","scheduled_round":"R2","scheduled_loop":96,"large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY","fine_archetype_id":"MEMORY_TEST_EQUIPMENT_OSAT_PACKAGE_TEST_CUSTOMER_QUALITY_BRIDGE_VS_TEST_LABEL_LATE_CHASE","symbol":"092870","name":"엑시콘","trigger_date":"2024-02-14","entry_date":"2024-02-14","entry_price":19300,"peak_high_before_corporate_action_candidate":35400,"peak_date":"2024-04-02","worst_low_before_corporate_action_candidate":17000,"worst_low_date":"2024-02-27","mfe_pct":83.4,"mae_pct":-11.9,"classification":"positive_memory_test_equipment_customer_quality_bridge_with_corporate_action_cutoff_and_4b_after_large_mfe","calibration_usable":true,"corporate_action_cutoff_case":true,"evidence_family":"memory_test_equipment_customer_qualification_order_visibility_margin_bridge","residual_error":"test_equipment_positive_requires_corporate_action_cutoff_and_4b_after_large_mfe_without_fresh_customer_order_evidence","shadow_rule_candidate":"preserve_test_equipment_positive_but_attach_4b_after_large_mfe_and_block_post_candidate_rows"}
{"row_type":"case","case_id":"C08_R2L96_067310_2024_02_01","scheduled_round":"R2","scheduled_loop":96,"large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY","fine_archetype_id":"MEMORY_TEST_EQUIPMENT_OSAT_PACKAGE_TEST_CUSTOMER_QUALITY_BRIDGE_VS_TEST_LABEL_LATE_CHASE","symbol":"067310","name":"하나마이크론","trigger_date":"2024-02-01","entry_date":"2024-02-01","entry_price":24600,"peak_high":34500,"peak_date":"2024-04-04","worst_low_after_entry":10300,"worst_low_after_entry_date":"2024-10-25","mfe_pct":40.2,"mae_pct":-58.1,"classification":"local_burst_osat_package_test_customer_quality_label_high_mae_4b_failure","calibration_usable":true,"evidence_family":"osat_package_test_customer_quality_label_without_sustained_utilization_margin_survival","residual_error":"osat_package_test_label_can_create_mfe_but_fail_green_without_customer_allocation_quality_and_margin_survival","shadow_rule_candidate":"classify_meaningful_mfe_then_extreme_mae_osat_package_test_cases_as_local_4b_not_green"}
{"row_type":"case","case_id":"C08_R2L96_097800_2024_08_01","scheduled_round":"R2","scheduled_loop":96,"large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY","fine_archetype_id":"MEMORY_TEST_EQUIPMENT_OSAT_PACKAGE_TEST_CUSTOMER_QUALITY_BRIDGE_VS_TEST_LABEL_LATE_CHASE","symbol":"097800","name":"윈팩","trigger_date":"2024-08-01","entry_date":"2024-08-01","entry_price":2010,"peak_high":2195,"peak_date":"2024-08-01","worst_low_after_entry":1082,"worst_low_after_entry_date":"2024-11-05","mfe_pct":9.2,"mae_pct":-46.2,"classification":"hard_4c_candidate_post_corporate_action_package_test_label_without_customer_quality_margin_survival","calibration_usable":true,"corporate_action_caveat_avoided":true,"evidence_family":"post_corporate_action_package_test_label_without_customer_quality_utilization_margin_bridge","residual_error":"package_test_label_can_fail_when_customer_quality_and_margin_survival_missing","shadow_rule_candidate":"route_post_corporate_action_package_test_label_to_hard_4c_if_mfe_shallow_mae_large_and_customer_quality_bridge_missing"}
```

```jsonl
{"row_type":"aggregate","scheduled_round":"R2","scheduled_loop":96,"large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY","fine_archetype_id":"MEMORY_TEST_EQUIPMENT_OSAT_PACKAGE_TEST_CUSTOMER_QUALITY_BRIDGE_VS_TEST_LABEL_LATE_CHASE","case_count":3,"positive_case_count":1,"counterexample_count":2,"watch_or_cap_case_count":1,"local_4b_overlay_case_count":2,"hard_4c_candidate_count":1,"corporate_action_caveat_avoided_count":1,"corporate_action_cutoff_case_count":1,"test_equipment_case_count":1,"osat_package_test_case_count":2,"calibration_usable_trigger_count":3,"loop_contribution_label":"residual_error_found","do_not_propose_new_weight_delta":true}
{"row_type":"shadow_rule","scheduled_round":"R2","scheduled_loop":96,"canonical_archetype_id":"C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY","rule_id":"C08_CUSTOMER_QUALIFICATION_TEST_UTILIZATION_MARGIN_BRIDGE_REQUIRED","rule_type":"canonical_archetype_specific_guard","rule_text":"For C08, do not open Stage2-Actionable or Stage3-Green from semiconductor test, memory tester, SSD tester, package-test, OSAT recovery, customer-quality rumor, AI/HBM/server-memory readthrough, or one-week test-stock volume spike labels alone. Require named customer/product/process step, qualification or customer-quality status, purchase order or test-capacity allocation, utilization and delivery schedule, yield/quality/defect risk control, ASP/mix/consumable or service margin bridge, working-capital and capex-risk check, and post-trigger price survival. Test-equipment positives with large MFE should attach local 4B unless fresh qualification/order/margin evidence appears. OSAT/package-test labels with meaningful MFE but extreme later MAE should not remain Green. Package-test labels with shallow MFE and high MAE should route to hard-4C when customer-quality and utilization-margin bridge are missing. Apply corporate-action cutoffs when candidate dates appear inside the validation window.","expected_effect":"Preserve true semiconductor test/customer qualification positives while reducing generic test-label, OSAT recovery, and package-test late-chase false positives.","production_scoring_changed":false,"shadow_weight_only":true}
{"row_type":"residual_contribution","scheduled_round":"R2","scheduled_loop":96,"canonical_archetype_id":"C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY","residual_type":"customer_qualification_test_utilization_margin_guard","contribution":"Adds one memory-test equipment positive with corporate-action cutoff, one OSAT package-test local 4B failure, and one post-corporate-action package-test hard-4C counterexample to calibrate C08 qualification, utilization, quality, order visibility, and margin requirements.","do_not_count_as_global_weight_delta":true}
```

---

## 10. Proposed canonical-archetype shadow rule

```text
C08_CUSTOMER_QUALIFICATION_TEST_UTILIZATION_MARGIN_BRIDGE_REQUIRED

IF canonical_archetype_id == C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY:

  Do not open Stage3-Green from:
    - semiconductor test label alone
    - memory tester / SSD tester / package-test label alone
    - OSAT recovery label alone
    - customer-quality rumor alone
    - HBM / AI server memory readthrough alone
    - one-week test-stock volume spike alone

  Require at least two of:
    - named customer / product / process step
    - qualification or customer-quality status
    - purchase order / test capacity allocation
    - utilization / delivery schedule
    - yield / quality / defect risk control
    - ASP / mix / consumable or service margin
    - working-capital or capex-risk containment
    - low-MAE post-trigger price survival
    - fresh evidence after the test/customer-quality headline

  If MFE < 10% and MAE < -35%:
    route to C08 hard-4C candidate.

  If MFE > 30% but later MAE is material:
    preserve as local 4B / event burst, not Green, unless current qualification/order/margin evidence appears.

  If corporate-action candidate appears inside the validation window:
    block post-candidate rows and require raw-price discontinuity caution.

  Distinguish:
    - test names where customer qualification becomes utilization and margin
    - from package-test labels where OSAT recovery does not survive yield, capex, or customer allocation risk.
```

---

## 11. Deferred Coding Agent Handoff Prompt

```text
You are a coding agent working on Songdaiki/stock_agent.

Do not treat this research MD as production scoring by itself.
Batch it with other v12 residual research files.

Source file:
e2r_stock_web_v12_residual_round_R2_loop_96_L2_AI_SEMICONDUCTOR_ELECTRONICS_C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY_research.md

Task:
1. Parse machine-readable JSONL rows.
2. Add the three C08 semiconductor test/customer-quality cases to calibration research ingestion.
3. Preserve production_scoring_changed=false.
4. Treat the proposed rule only as a shadow canonical-archetype guard candidate:
   C08_CUSTOMER_QUALIFICATION_TEST_UTILIZATION_MARGIN_BRIDGE_REQUIRED.
5. Do not change global weights directly.
6. Compare against existing C08 cases and deduplicate by:
   canonical_archetype_id + symbol + trigger_type + entry_date.
7. If enough C08 cases agree, consider implementing a canonical guard that:
   - blocks test-label Green without customer/product/process, qualification, utilization, and margin bridge,
   - preserves test-equipment positives only with corporate-action cutoffs and fresh order evidence,
   - attaches local 4B after large MFE followed by material MAE,
   - routes shallow-MFE/high-MAE package-test labels to hard-4C,
   - applies corporate-action window cutoffs for raw-price validation.

Expected next schedule:
completed_round = R2
completed_loop = 96
next_round = R3
next_loop = 96
round_schedule_status = valid
round_sector_consistency = pass
```

---

## 12. Required round-state footer

```text
completed_round = R2
completed_loop = 96
next_round = R3
next_loop = 96
round_schedule_status = valid
round_sector_consistency = pass
```
