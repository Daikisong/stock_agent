# E2R Stock-Web v12 Residual Research — R2 / Loop 99

```yaml
scheduled_round: R2
scheduled_loop: 99
large_sector_id: L2_AI_SEMICONDUCTOR_ELECTRONICS
canonical_archetype_id: C06_HBM_MEMORY_CUSTOMER_CAPACITY
fine_archetype_id: HBM_TEST_HANDLER_PACKAGE_SUBSTRATE_MEMORY_CUSTOMER_CAPACITY_ORDER_UTILIZATION_MARGIN_BRIDGE_VS_HBM_CAPACITY_LABEL_SPIKE

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
hbm_test_handler_case_count: 1
package_substrate_case_count: 2
memory_customer_capacity_case_count: 3
customer_capacity_order_bridge_missing_count: 2
utilization_margin_bridge_missing_count: 2
valuation_late_chase_or_label_overheat_count: 2
old_corporate_action_or_listing_caveat_count: 2
calibration_usable_trigger_count: 3

loop_contribution_label: residual_error_found
canonical_archetype_rule_candidate: true
do_not_propose_new_weight_delta: true

completed_round: R2
completed_loop: 99
next_round: R3
next_loop: 99
round_schedule_status: valid
round_sector_consistency: pass
```

---

## 1. Schedule resolution

Previous completed file in the active sequence was:

```text
e2r_stock_web_v12_residual_round_R1_loop_99_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C01_ORDER_BACKLOG_MARGIN_BRIDGE_research.md
```

Under v12:

```text
R1 -> R2 -> R3 -> R4 -> R5 -> R6 -> R7 -> R8 -> R9 -> R10 -> R11 -> R12 -> R13 -> R1
```

Therefore:

```text
scheduled_round = R2
scheduled_loop = 99
large_sector_id = L2_AI_SEMICONDUCTOR_ELECTRONICS
```

R2 is the AI / semiconductor / electronics round. The selected canonical archetype is:

```text
C06_HBM_MEMORY_CUSTOMER_CAPACITY
```

Recent R2 branch usage:

```text
loop95: C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH
loop96: C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY
loop97: C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF
loop98: C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE
```

This run returns to C06 after the R2 branch cycle.

Selected fine branch:

```text
HBM / memory customer capacity
test handler, package substrate, memory package / substrate supply chain
customer qualification, customer capacity expansion, order visibility,
tool or substrate delivery, utilization, acceptance, working capital,
valuation discipline, and margin conversion
vs generic HBM / memory capacity label spike
```

---

## 2. No-repeat / novelty check

No-Repeat Index coverage snapshot:

```text
C06_HBM_MEMORY_CUSTOMER_CAPACITY
rows: 7
symbols: 6
date_range: 2023-09-14~2024-07-05
good/bad S2: 4/1
4B/4C: 0/0
URL pending/proxy: 3/0
top covered symbols:
  000660(2), 005930(1), 009150(1), 014680(1), 067310(1), 402340(1)
```

Selected symbols:

```text
089030 테크윙
353200 대덕전자
195870 해성디에스
```

They avoid the C06 top-covered list and avoid recent R2 loop97~98 selected names:

```text
C06 top-covered avoid:
  000660, 005930, 009150, 014680, 067310, 402340

loop98 C10 avoid:
  074600, 101160, 253590

loop97 C09 avoid:
  084370, 036930, 083310
```

Hard duplicate key:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

Novelty classification:

```text
089030: same archetype, new symbol, HBM test-handler / memory customer-capacity positive with extreme MFE and Green cap
353200: same archetype, new symbol, package-substrate / HBM capacity local burst followed by hard-zone MAE, local 4B with hard-4C secondary guard
195870: same archetype, new symbol, package-substrate / lead-frame memory capacity label hard-4C after shallow-to-moderate MFE and extreme MAE
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
089030 테크윙
  profile: atlas/symbol_profiles/089/089030.json
  first_date: 2011-11-10
  last_date: 2026-02-20
  market: KOSDAQ
  tradable_ohlcv rows: 3,509
  non_tradable_zero_volume rows: 0
  corporate_action_candidate_dates:
    2011-12-13, 2011-12-29, 2022-08-01, 2022-08-23
  2024 entry~D+180 contamination: none
  caveat:
    old raw-discontinuity windows are outside selected 2024 validation window.

353200 대덕전자
  profile: atlas/symbol_profiles/353/353200.json
  first_date: 2020-05-21
  last_date: 2026-02-20
  market: KOSPI
  tradable_ohlcv rows: 1,412
  non_tradable_zero_volume rows: 0
  corporate_action_candidate_dates: none
  2024 entry~D+180 contamination: none
  caveat:
    shorter listed history versus older semiconductor peers, but no direct 2024 contamination.

195870 해성디에스
  profile: atlas/symbol_profiles/195/195870.json
  first_date: 2016-06-24
  last_date: 2026-02-20
  market: KOSPI
  tradable_ohlcv rows: 2,369
  non_tradable_zero_volume rows: 0
  corporate_action_candidate_dates: none
  2024 entry~D+180 contamination: none
```

Rejected candidate note:

```text
077360 덕산하이메탈 was checked but not used in the final three-case set.
It is a plausible HBM / packaging-material readthrough name, but its first-half 2024 path was less clean
for C06 than the selected positive / 4B / hard-4C grid.
```

---

## 4. Archetype residual problem

C06 is about HBM / memory customer capacity. It is not merely a generic "HBM stock is hot" archetype.

The model can over-score:

```text
HBM label
AI-memory demand headline
memory customer capacity expansion headline
advanced packaging / substrate / lead-frame label
test-handler / memory test label
customer qualification rumor
one-week HBM supply-chain volume spike
late chase after an HBM capacity rerating
```

The C06 bridge must be stricter:

```text
HBM / memory customer-capacity event
  -> named customer, device, package, process step, tool, substrate, or material
  -> customer qualification and acceptance
  -> capacity expansion and utilization
  -> order visibility / delivery / call-off
  -> customer concentration and inventory risk
  -> ASP / mix / take-rate or gross-profit bridge
  -> capex, depreciation, and working-capital timing
  -> raw-material, labor, warranty, and yield cost
  -> margin / OP conversion
  -> valuation discipline after the first HBM capacity spike
  -> price survival after the rerating
```

A C06 HBM thesis is like a package stack entering a memory customer's capacity plan. The AI demand headline lights the cleanroom, but equity value appears only when the customer qualifies the part, capacity actually loads, orders are called off, deliveries are accepted, and the added volume still carries margin after yield, material, depreciation, and working-capital pressure.

---

## 5. Case 1 — 089030 테크윙

```yaml
case_id: C06_R2L99_089030_2024_02_01
symbol: "089030"
name: "테크윙"
canonical_archetype_id: C06_HBM_MEMORY_CUSTOMER_CAPACITY
fine_archetype_id: HBM_TEST_HANDLER_PACKAGE_SUBSTRATE_MEMORY_CUSTOMER_CAPACITY_ORDER_UTILIZATION_MARGIN_BRIDGE_VS_HBM_CAPACITY_LABEL_SPIKE
trigger_date: 2024-02-01
entry_date: 2024-02-01
entry_price_basis: close
entry_price: 15290
classification: positive_hbm_test_handler_customer_capacity_utilization_order_margin_bridge_with_extreme_mfe_green_cap
calibration_usable: true
```

### Evidence interpretation

테크윙 is the constructive C06 positive.

The useful C06 read is not simply:

```text
HBM / AI 메모리 장비주가 강하다
```

It is:

```text
memory / HBM test-handler relevance
  -> customer capacity expansion and qualification readthrough
  -> tool delivery and utilization optionality
  -> customer order / acceptance / gross-profit bridge
  -> extreme price confirmation into July
```

The forward path produced extreme MFE and avoided hard drawdown from the early February trigger. This preserves positive classification. However, after such a large rerating, Green should remain capped unless customer qualification, order visibility, delivery, utilization, and margin evidence stay current.

### Price path

Key Stock-Web rows:

```text
2024-02-01: high 15,950 / low 14,810 / close 15,290
2024-02-19: high 21,800 / close 21,550
2024-03-27: high 36,000 / close 35,200
2024-04-11: high 39,100 / close 38,700
2024-07-24: high 56,600 / close 54,500
2024-08-05: low 37,200 / close 39,150
2024-10-31: high 45,500 / close 44,600
```

Approximate path from entry close:

```text
entry_close: 15,290
peak_high: 56,600
MFE: +270.2%
worst_low_after_entry: 14,810
MAE: -3.1%
```

### Interpretation

This is a C06 positive with Green cap:

```text
Stage2-Actionable: possible if customer capacity, qualification, tool delivery, utilization, and margin bridge are explicit.
Stage3-Green: blocked after +270% MFE unless fresh customer/order/margin evidence appears.
Local 4B: monitor if HBM label price outruns utilization or order evidence.
Hard 4C: no.
```

### Stress-test components

```text
raw_component_score_proxy:
  hbm_test_handler_relevance: high
  customer_capacity_bridge: high
  qualification_acceptance_bridge: medium_high
  delivery_utilization_bridge: medium_high
  margin_op_bridge: medium
  valuation_overheat_risk: high
  price_confirmation: extreme
  drawdown_penalty: low
  green_cap: required_after_extreme_mfe
```

---

## 6. Case 2 — 353200 대덕전자

```yaml
case_id: C06_R2L99_353200_2024_02_01
symbol: "353200"
name: "대덕전자"
canonical_archetype_id: C06_HBM_MEMORY_CUSTOMER_CAPACITY
fine_archetype_id: HBM_TEST_HANDLER_PACKAGE_SUBSTRATE_MEMORY_CUSTOMER_CAPACITY_ORDER_UTILIZATION_MARGIN_BRIDGE_VS_HBM_CAPACITY_LABEL_SPIKE
trigger_date: 2024-02-01
entry_date: 2024-02-01
entry_price_basis: close
entry_price: 24000
classification: local_burst_package_substrate_hbm_capacity_label_hard_zone_mae_4b_failure_with_secondary_guard
calibration_usable: true
```

### Evidence interpretation

대덕전자 is the package-substrate / HBM capacity local-burst failure.

The label can look relevant:

```text
advanced package substrate / memory substrate
  -> HBM and AI-memory capacity readthrough
  -> customer order and substrate mix optionality
  -> April event burst
```

The stock produced meaningful MFE first. But the later path entered a hard-zone drawdown. This is not a pure zero-response false positive, because the April spike was real. It is a 4B failure and should receive a secondary hard-4C guard when HBM capacity evidence is stale or the entry is late.

### Price path

Key Stock-Web rows:

```text
2024-02-01: high 24,600 / low 23,600 / close 24,000
2024-03-29: high 24,800 / close 24,550
2024-04-01: high 27,900 / close 27,000
2024-04-02: high 28,050 / close 26,900
2024-08-05: low 17,500 / close 18,580
2024-09-06: low 17,500 / close 17,520
2024-10-25: low 15,550 / close 15,820
```

Approximate path from entry close:

```text
entry_close: 24,000
peak_high: 28,050
MFE: +16.9%
worst_low_after_entry: 15,550
MAE: -35.2%
```

### Interpretation

This is a C06 local 4B failure:

```text
Stage2-Watch: valid from package-substrate / HBM capacity relevance.
Stage2-Actionable: possible only if customer qualification, order, substrate mix, utilization, and margin evidence are explicit.
Stage3-Green: blocked after hard-zone MAE.
Local 4B: required.
Hard 4C secondary guard: yes for stale or late entries when order/margin bridge is missing.
```

### Stress-test components

```text
raw_component_score_proxy:
  package_substrate_hbm_relevance: high
  customer_capacity_bridge: medium
  order_visibility_bridge: weak_to_medium
  substrate_mix_margin_bridge: weak_to_medium
  utilization_bridge: weak
  price_confirmation: meaningful_initial
  later_drawdown_penalty: high
  local_4b_overlay: required
```

---

## 7. Case 3 — 195870 해성디에스

```yaml
case_id: C06_R2L99_195870_2024_02_01
symbol: "195870"
name: "해성디에스"
canonical_archetype_id: C06_HBM_MEMORY_CUSTOMER_CAPACITY
fine_archetype_id: HBM_TEST_HANDLER_PACKAGE_SUBSTRATE_MEMORY_CUSTOMER_CAPACITY_ORDER_UTILIZATION_MARGIN_BRIDGE_VS_HBM_CAPACITY_LABEL_SPIKE
trigger_date: 2024-02-01
entry_date: 2024-02-01
entry_price_basis: close
entry_price: 49400
classification: hard_4c_candidate_package_substrate_memory_capacity_label_without_customer_order_margin_survival
calibration_usable: true
```

### Evidence interpretation

해성디에스 is the package substrate / memory capacity hard C06 guardrail.

The setup had plausible C06 relevance:

```text
package substrate / lead-frame memory-capacity readthrough
  -> AI/HBM and memory cycle sympathy
  -> customer capacity recovery hope
  -> April local rerating
```

But from the selected February trigger, the forward path failed price survival severely. The bridge from memory capacity label to named customer order, qualification, utilization, mix improvement, working capital, and margin was not proven.

### Price path

Key Stock-Web rows:

```text
2024-02-01: high 50,500 / low 48,800 / close 49,400
2024-03-29: high 52,700 / close 52,400
2024-04-05: high 55,500 / close 54,500
2024-08-05: low 27,250 / close 28,050
2024-09-09: low 25,000 / close 26,750
2024-10-25: low 26,750 / close 26,750
```

Approximate path from entry close:

```text
entry_close: 49,400
peak_high: 55,500
MFE: +12.3%
worst_low_after_entry: 25,000
MAE: -49.4%
```

### Interpretation

This is a hard C06 false-positive candidate:

```text
Stage2-Watch: possible from package-substrate and memory-capacity relevance.
Stage2-Actionable: blocked unless named customer order, qualification, capacity loading, mix, and margin bridge are explicit.
Stage3-Green: blocked.
Hard 4C: yes by modest MFE and extreme MAE.
```

The lesson is that package-substrate memory-cycle salience is not customer-capacity margin survival.

### Stress-test components

```text
raw_component_score_proxy:
  package_substrate_label: high
  memory_capacity_readthrough: medium_high
  customer_order_bridge: weak
  qualification_acceptance_bridge: weak
  mix_margin_bridge: weak
  working_capital_bridge: weak_to_medium
  price_confirmation: modest
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
hard_4c_secondary_guard_count: 1
hbm_test_handler_case_count: 1
package_substrate_case_count: 2
memory_customer_capacity_case_count: 3
customer_capacity_order_bridge_missing_count: 2
utilization_margin_bridge_missing_count: 2
valuation_late_chase_or_label_overheat_count: 2
old_corporate_action_or_listing_caveat_count: 2
calibration_usable_trigger_count: 3
```

The three-case C06 HBM / memory customer-capacity grid:

```text
089030 테크윙:
  HBM test-handler / customer capacity positive;
  extreme MFE and low MAE, but Green requires fresh qualification/order/utilization/margin evidence.

353200 대덕전자:
  package-substrate / HBM capacity local burst;
  meaningful MFE first, then hard-zone MAE, local 4B with hard-4C secondary guard.

195870 해성디에스:
  package-substrate memory-capacity label failed;
  modest MFE and extreme MAE, hard 4C.
```

Shared rule:

```text
C06 is not "HBM or memory-capacity label is hot."
C06 is "customer qualification, capacity loading, order visibility, delivery, acceptance, mix/ASP, working capital, and margin conversion are visible for this company."
```

---

## 9. Machine-readable JSONL rows

```jsonl
{"row_type":"case","case_id":"C06_R2L99_089030_2024_02_01","scheduled_round":"R2","scheduled_loop":99,"large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C06_HBM_MEMORY_CUSTOMER_CAPACITY","fine_archetype_id":"HBM_TEST_HANDLER_PACKAGE_SUBSTRATE_MEMORY_CUSTOMER_CAPACITY_ORDER_UTILIZATION_MARGIN_BRIDGE_VS_HBM_CAPACITY_LABEL_SPIKE","symbol":"089030","name":"테크윙","trigger_date":"2024-02-01","entry_date":"2024-02-01","entry_price":15290,"peak_high":56600,"peak_date":"2024-07-24","worst_low_after_entry":14810,"worst_low_after_entry_date":"2024-02-01","mfe_pct":270.2,"mae_pct":-3.1,"classification":"positive_hbm_test_handler_customer_capacity_utilization_order_margin_bridge_with_extreme_mfe_green_cap","calibration_usable":true,"old_corporate_action_caveat_outside_window":true,"evidence_family":"hbm_test_handler_memory_customer_capacity_qualification_order_delivery_utilization_margin_bridge","residual_error":"extreme_hbm_capacity_positive_requires_green_cap_without_refreshed_customer_order_utilization_margin_evidence","shadow_rule_candidate":"allow_capped_actionable_when_customer_capacity_order_and_margin_bridge_confirm_but_cap_green_after_extreme_mfe"}
{"row_type":"case","case_id":"C06_R2L99_353200_2024_02_01","scheduled_round":"R2","scheduled_loop":99,"large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C06_HBM_MEMORY_CUSTOMER_CAPACITY","fine_archetype_id":"HBM_TEST_HANDLER_PACKAGE_SUBSTRATE_MEMORY_CUSTOMER_CAPACITY_ORDER_UTILIZATION_MARGIN_BRIDGE_VS_HBM_CAPACITY_LABEL_SPIKE","symbol":"353200","name":"대덕전자","trigger_date":"2024-02-01","entry_date":"2024-02-01","entry_price":24000,"peak_high":28050,"peak_date":"2024-04-02","worst_low_after_entry":15550,"worst_low_after_entry_date":"2024-10-25","mfe_pct":16.9,"mae_pct":-35.2,"classification":"local_burst_package_substrate_hbm_capacity_label_hard_zone_mae_4b_failure_with_secondary_guard","calibration_usable":true,"short_listing_or_history_caveat":true,"evidence_family":"package_substrate_hbm_capacity_label_without_sustained_customer_order_utilization_mix_margin_survival","residual_error":"package_substrate_hbm_capacity_label_can_create_mfe_but_fail_green_when_customer_order_and_margin_bridge_breaks","shadow_rule_candidate":"classify_meaningful_mfe_then_hard_zone_mae_package_substrate_cases_as_local_4b_with_hard_4c_secondary_guard"}
{"row_type":"case","case_id":"C06_R2L99_195870_2024_02_01","scheduled_round":"R2","scheduled_loop":99,"large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C06_HBM_MEMORY_CUSTOMER_CAPACITY","fine_archetype_id":"HBM_TEST_HANDLER_PACKAGE_SUBSTRATE_MEMORY_CUSTOMER_CAPACITY_ORDER_UTILIZATION_MARGIN_BRIDGE_VS_HBM_CAPACITY_LABEL_SPIKE","symbol":"195870","name":"해성디에스","trigger_date":"2024-02-01","entry_date":"2024-02-01","entry_price":49400,"peak_high":55500,"peak_date":"2024-04-05","worst_low_after_entry":25000,"worst_low_after_entry_date":"2024-09-09","mfe_pct":12.3,"mae_pct":-49.4,"classification":"hard_4c_candidate_package_substrate_memory_capacity_label_without_customer_order_margin_survival","calibration_usable":true,"evidence_family":"package_substrate_leadframe_memory_capacity_label_without_named_customer_order_qualification_utilization_mix_margin_bridge","residual_error":"package_substrate_memory_capacity_label_can_fail_when_customer_order_and_margin_bridge_missing","shadow_rule_candidate":"route_package_substrate_memory_capacity_label_to_hard_4c_if_mfe_modest_mae_extreme_and_order_margin_bridge_missing"}
```

```jsonl
{"row_type":"aggregate","scheduled_round":"R2","scheduled_loop":99,"large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C06_HBM_MEMORY_CUSTOMER_CAPACITY","fine_archetype_id":"HBM_TEST_HANDLER_PACKAGE_SUBSTRATE_MEMORY_CUSTOMER_CAPACITY_ORDER_UTILIZATION_MARGIN_BRIDGE_VS_HBM_CAPACITY_LABEL_SPIKE","case_count":3,"positive_case_count":1,"counterexample_count":2,"watch_or_cap_case_count":2,"local_4b_overlay_case_count":1,"hard_4c_candidate_count":1,"hard_4c_secondary_guard_count":1,"hbm_test_handler_case_count":1,"package_substrate_case_count":2,"memory_customer_capacity_case_count":3,"customer_capacity_order_bridge_missing_count":2,"utilization_margin_bridge_missing_count":2,"valuation_late_chase_or_label_overheat_count":2,"old_corporate_action_or_listing_caveat_count":2,"calibration_usable_trigger_count":3,"loop_contribution_label":"residual_error_found","do_not_propose_new_weight_delta":true}
{"row_type":"shadow_rule","scheduled_round":"R2","scheduled_loop":99,"canonical_archetype_id":"C06_HBM_MEMORY_CUSTOMER_CAPACITY","rule_id":"C06_HBM_CUSTOMER_CAPACITY_ORDER_UTILIZATION_MARGIN_BRIDGE_REQUIRED","rule_type":"canonical_archetype_specific_guard","rule_text":"For C06 HBM/memory customer-capacity cases, do not open Stage2-Actionable or Stage3-Green from HBM label, AI-memory demand headline, memory customer capacity expansion, advanced packaging/substrate/lead-frame label, test-handler/memory-test label, customer qualification rumor, one-week HBM supply-chain volume spike, or late chase after HBM-capacity rerating labels alone. Require named customer/device/package/process step/tool/substrate/material, customer qualification and acceptance, capacity expansion and utilization, order visibility/delivery/call-off, customer concentration and inventory-risk check, ASP/mix/take-rate or gross-profit bridge, capex/depreciation/working-capital timing, raw-material/labor/warranty/yield cost control, margin/OP conversion, valuation discipline after the first HBM capacity spike, and post-trigger price survival. HBM test-handler positives with extreme MFE may be capped Actionable when customer capacity/order/utilization/margin bridge is explicit, but Green requires fresh evidence. Package-substrate HBM-capacity labels with meaningful MFE followed by hard-zone MAE should remain local 4B and receive hard-4C secondary guard when order and margin evidence is stale. Package-substrate memory-capacity labels with modest MFE and extreme MAE should route to hard-4C when customer order and margin bridge are missing.","expected_effect":"Preserve true HBM customer-capacity positives while reducing generic HBM, package-substrate, lead-frame, customer-capacity, and memory-cycle false positives where qualification, order visibility, utilization, mix, working capital, and margin evidence fail.","production_scoring_changed":false,"shadow_weight_only":true}
{"row_type":"residual_contribution","scheduled_round":"R2","scheduled_loop":99,"canonical_archetype_id":"C06_HBM_MEMORY_CUSTOMER_CAPACITY","residual_type":"hbm_customer_capacity_order_utilization_margin_guard","contribution":"Adds one HBM test-handler positive, one package-substrate local 4B failure, and one package-substrate hard-4C counterexample to calibrate C06 customer qualification, capacity loading, order visibility, delivery, utilization, working capital, valuation discipline, and margin requirements.","do_not_count_as_global_weight_delta":true}
```

---

## 10. Proposed canonical-archetype shadow rule

```text
C06_HBM_CUSTOMER_CAPACITY_ORDER_UTILIZATION_MARGIN_BRIDGE_REQUIRED

IF canonical_archetype_id == C06_HBM_MEMORY_CUSTOMER_CAPACITY:

  Do not open Stage3-Green from:
    - HBM label alone
    - AI-memory demand headline alone
    - memory customer capacity expansion headline alone
    - advanced packaging / substrate / lead-frame label alone
    - test-handler / memory-test label alone
    - customer qualification rumor alone
    - one-week HBM supply-chain volume spike alone
    - late chase after HBM capacity rerating alone

  Require at least two of:
    - named customer / device / package / process step / tool / substrate / material
    - customer qualification and acceptance
    - capacity expansion and utilization
    - order visibility / delivery / call-off
    - customer concentration and inventory-risk check
    - ASP / mix / take-rate or gross-profit bridge
    - capex / depreciation / working-capital timing
    - raw-material / labor / warranty / yield cost containment
    - margin / OP conversion
    - valuation discipline after first HBM capacity spike
    - low-MAE post-trigger price survival
    - fresh evidence after the HBM/capacity headline

  If MFE < 15% and MAE <= -35%:
    route to C06 hard-4C candidate.

  If MFE is meaningful but later MAE enters hard zone:
    preserve as local 4B and attach hard-4C secondary guard for stale or late entries.

  If MFE is extreme but valuation / order / utilization evidence is stale:
    cap Green until customer-capacity and margin evidence refreshes.

  Distinguish:
    - names where HBM demand becomes customer qualification, orders, utilization, accepted delivery, and OP margin
    - from labels where substrate, test, or capacity salience rerates first and order/margin proof fails.
```

---

## 11. Deferred Coding Agent Handoff Prompt

```text
You are a coding agent working on Songdaiki/stock_agent.

Do not treat this research MD as production scoring by itself.
Batch it with other v12 residual research files.

Source file:
e2r_stock_web_v12_residual_round_R2_loop_99_L2_AI_SEMICONDUCTOR_ELECTRONICS_C06_HBM_MEMORY_CUSTOMER_CAPACITY_research.md

Task:
1. Parse machine-readable JSONL rows.
2. Add the three C06 HBM/memory customer-capacity cases to calibration research ingestion.
3. Preserve production_scoring_changed=false.
4. Treat the proposed rule only as a shadow canonical-archetype guard candidate:
   C06_HBM_CUSTOMER_CAPACITY_ORDER_UTILIZATION_MARGIN_BRIDGE_REQUIRED.
5. Do not change global weights directly.
6. Compare against existing C06 cases and deduplicate by:
   canonical_archetype_id + symbol + trigger_type + entry_date.
7. If enough C06 cases agree, consider implementing a canonical guard that:
   - blocks HBM/customer-capacity Green without named customer/package/tool, qualification, order visibility, utilization, and margin bridge,
   - preserves HBM test-handler positives only with price survival and fresh order/utilization evidence,
   - treats meaningful-MFE/hard-zone-MAE package-substrate cases as local 4B with hard-4C secondary guard,
   - routes modest-MFE/extreme-MAE package-substrate/lead-frame labels to hard-4C,
   - applies old corporate-action, short-listing/history, and row/tradeability caveats where needed.

Expected next schedule:
completed_round = R2
completed_loop = 99
next_round = R3
next_loop = 99
round_schedule_status = valid
round_sector_consistency = pass
```

---

## 12. Required round-state footer

```text
completed_round = R2
completed_loop = 99
next_round = R3
next_loop = 99
round_schedule_status = valid
round_sector_consistency = pass
```
