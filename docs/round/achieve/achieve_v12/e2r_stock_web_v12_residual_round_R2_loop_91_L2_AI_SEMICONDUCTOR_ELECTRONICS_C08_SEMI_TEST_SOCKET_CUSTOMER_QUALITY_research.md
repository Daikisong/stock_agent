# E2R Stock-Web v12 Residual Research — R2 / Loop 91

```yaml
scheduled_round: R2
scheduled_loop: 91
large_sector_id: L2_AI_SEMICONDUCTOR_ELECTRONICS
canonical_archetype_id: C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY
fine_archetype_id: HBM_AI_MEMORY_TEST_AND_OSAT_CUSTOMER_QUALITY_BRIDGE_VS_SEMI_TEST_LABEL_PRICE_SPIKE

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
local_4b_overlay_case_count: 2
hard_4c_candidate_count: 2
calibration_usable_trigger_count: 3

loop_contribution_label: residual_error_found
canonical_archetype_rule_candidate: true
do_not_propose_new_weight_delta: true

completed_round: R2
completed_loop: 91
next_round: R3
next_loop: 91
round_schedule_status: valid
round_sector_consistency: pass
```

---

## 1. Schedule resolution

Previous completed file in the active sequence was:

```text
e2r_stock_web_v12_residual_round_R1_loop_91_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C01_ORDER_BACKLOG_MARGIN_BRIDGE_research.md
```

Under v12:

```text
R1 -> R2 -> R3 -> R4 -> R5 -> R6 -> R7 -> R8 -> R9 -> R10 -> R11 -> R12 -> R13 -> R1
```

Therefore:

```text
scheduled_round = R2
scheduled_loop = 91
large_sector_id = L2_AI_SEMICONDUCTOR_ELECTRONICS
```

Recent R2 branch usage already covered:

```text
loop89: C06_HBM_MEMORY_CUSTOMER_CAPACITY
loop90: C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH
```

This run therefore selects:

```text
canonical_archetype_id = C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY
```

The goal is to separate a real test/customer-quality bridge from generic semiconductor-test label chasing.

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
232140 와이씨
131970 두산테스나
330860 네패스아크
```

These symbols avoid the C08 top-covered list and avoid the recent R2 loop90 names:

```text
031980, 039030, 403870
```

Hard duplicate key:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

Novelty classification:

```text
232140: same archetype, new symbol, memory wafer-test equipment customer-quality branch
131970: same archetype, new symbol, OSAT/test-service customer-quality false-positive branch
330860: same archetype, new symbol, test-service local burst / high-MAE branch
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
markets: KONEX, KOSDAQ, KOSDAQ GLOBAL, KOSPI
calibration_shard_root: atlas/ohlcv_tradable_by_symbol_year
raw_shard_root: atlas/ohlcv_raw_by_symbol_year
schema_path: atlas/schema.json
universe_path: atlas/universe/all_symbols.csv
```

Profile checks:

```text
232140 와이씨
  profile: atlas/symbol_profiles/232/232140.json
  current/latest name: 와이씨
  prior name in 2024 before 2024-04-25: 와이아이케이
  first_date: 2015-12-24
  last_date: 2026-02-20
  tradable_ohlcv rows: 2,425
  corporate_action_candidate_dates:
    2017-04-05
  2024 entry~D+180 contamination: none

131970 두산테스나
  profile: atlas/symbol_profiles/131/131970.json
  first_date: 2013-10-22
  last_date: 2026-02-20
  tradable_ohlcv rows: 3,027
  corporate_action_candidate_dates:
    2020-09-15, 2020-10-07
  2024 entry~D+180 contamination: none

330860 네패스아크
  profile: atlas/symbol_profiles/330/330860.json
  first_date: 2020-11-17
  last_date: 2026-02-20
  tradable_ohlcv rows: 1,289
  corporate_action_candidate_dates: none
  2024 entry~D+180 contamination: none
```

---

## 4. Archetype residual problem

C08 is not a generic "semiconductor tester or socket stock" label.

The model can over-score:

```text
HBM
AI semiconductor
test equipment
OSAT
probe card / socket / package test
customer quality
```

when it sees only a sector label and a price spike. But the actual C08 bridge is narrower:

```text
specific test/socket capability
  -> customer qualification
  -> volume ramp
  -> repeatable revenue
  -> utilization and margin
  -> revision / OP conversion
  -> price path survival
```

A tester is like a gatekeeper on a factory line. The gatekeeper matters only if the right customer line is growing, the gate is qualified, and the fee flows repeatedly. If the signal is only "test label + spike," the path can decay quickly.

---

## 5. Case 1 — 232140 와이씨

```yaml
case_id: C08_R2L91_232140_2024_03_20
symbol: "232140"
name: "와이씨"
canonical_archetype_id: C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY
fine_archetype_id: HBM_AI_MEMORY_TEST_AND_OSAT_CUSTOMER_QUALITY_BRIDGE_VS_SEMI_TEST_LABEL_PRICE_SPIKE
trigger_date: 2024-03-20
entry_date: 2024-03-20
entry_price_basis: close
entry_price: 7930
classification: positive_with_local_4b_memory_test_equipment_customer_quality
calibration_usable: true
```

### Evidence interpretation

와이씨 is the positive control. The useful C08 thesis is:

```text
memory wafer-test / burn-in / inspection equipment relevance
  -> HBM and advanced memory cycle readthrough
  -> customer-quality and order conversion expectation
  -> price rerating
```

The stock path delivered a large MFE and did not break the entry price in the checked forward path. This supports C08 Actionable when test-equipment relevance is paired with real price confirmation.

### Price path

Key Stock-Web rows:

```text
2024-03-20: close 7,930
2024-03-21: high 8,470 / close 7,660
2024-04-02: high 7,950 / close 7,870
2024-06-26: close 18,940
2024-07-29: high 19,240 / close 18,260
2024-08-05: low 12,560 / close 13,730
```

Approximate return path from entry close:

```text
entry_close: 7,930
peak_high: 19,240
MFE: +142.6%
worst_forward_low_in_checked_window: 10,830 on 2024-09-09
MAE vs entry: positive cushion remained
peak_to_later_low_drawdown: -43.7%
```

### Interpretation

This is a strong positive but not a "never sell" Green.

```text
Stage2-Actionable: valid.
Stage3-Green: allowed only if customer qualification / order / revenue bridge is explicit.
Local 4B: mandatory after +100% MFE and later peak-to-trough drawdown.
Hard 4C: no.
```

### Stress-test components

```text
raw_component_score_proxy:
  test_equipment_customer_quality: high
  memory/HBM readthrough: high
  price_confirmation: very_high
  drawdown_after_peak: high
  local_4b_overlay: required
```

---

## 6. Case 2 — 131970 두산테스나

```yaml
case_id: C08_R2L91_131970_2024_03_20
symbol: "131970"
name: "두산테스나"
canonical_archetype_id: C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY
fine_archetype_id: HBM_AI_MEMORY_TEST_AND_OSAT_CUSTOMER_QUALITY_BRIDGE_VS_SEMI_TEST_LABEL_PRICE_SPIKE
trigger_date: 2024-03-20
entry_date: 2024-03-20
entry_price_basis: close
entry_price: 47600
classification: hard_4c_candidate_test_service_label_without_customer_quality_bridge
calibration_usable: true
```

### Evidence interpretation

두산테스나 is the OSAT/test-service false-positive. It has a plausible C08 label, but the forward price path did not validate a high-quality customer/volume/margin bridge.

The model risk:

```text
test service stock
  -> AI/HBM/test theme bucket
  -> price pop
  -> Stage2-Actionable opened too early
  -> no confirmed customer-quality bridge
  -> high MAE
```

### Price path

Key Stock-Web rows:

```text
2024-03-20: close 47,600
2024-03-21: high 49,400 / close 48,250
2024-03-28: high 51,800 / close 50,400
2024-04-05: high 53,300 / close 51,500
2024-08-05: low 29,250 / close 29,950
2024-09-09: low 27,650 / close 29,150
```

Approximate return path from entry close:

```text
entry_close: 47,600
peak_high: 53,300
MFE: +12.0%
worst_low: 27,650
MAE: -41.9%
```

### Interpretation

This is a hard guardrail case.

```text
Stage2-Watch: allowed from the test-service label.
Stage2-Actionable: blocked unless customer qualification / utilization / margin bridge is explicit.
Stage3-Green: blocked.
Hard 4C candidate: yes.
```

The local high did not compensate for the later drawdown.

### Stress-test components

```text
raw_component_score_proxy:
  test_service_label: high
  customer_quality_bridge: weak
  price_confirmation: shallow
  drawdown_penalty: high
  hard_4c_guard: yes
```

---

## 7. Case 3 — 330860 네패스아크

```yaml
case_id: C08_R2L91_330860_2024_02_21
symbol: "330860"
name: "네패스아크"
canonical_archetype_id: C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY
fine_archetype_id: HBM_AI_MEMORY_TEST_AND_OSAT_CUSTOMER_QUALITY_BRIDGE_VS_SEMI_TEST_LABEL_PRICE_SPIKE
trigger_date: 2024-02-21
entry_date: 2024-02-21
entry_price_basis: close
entry_price: 36900
classification: local_burst_but_high_mae_counterexample
calibration_usable: true
```

### Evidence interpretation

네패스아크 is the local-burst case. It proves that a test-service theme can produce a tradable spike, but the spike can fail durability if the customer-quality and revenue bridge are missing.

This is exactly the C08 4B/4C boundary.

### Price path

Key Stock-Web rows:

```text
2024-02-21: close 36,900
2024-02-22: high 42,650 / close 39,150
2024-03-12: high 46,400 / close 42,150
2024-03-22: low 32,300 / close 32,550
2024-07-05: low 21,150 / close 22,450
2024-08-05: low 13,980 / close 14,200
2024-09-09: low 12,000 / close 13,300
```

Approximate return path from entry close:

```text
entry_close: 36,900
peak_high: 46,400
MFE: +25.7%
worst_low: 12,000
MAE: -67.5%
```

### Interpretation

This is a local-burst counterexample:

```text
Stage2-Watch: allowed.
Stage2-Actionable: only if fast 4B/event trading, not durable Green.
Stage3-Green: blocked.
Hard 4C candidate: yes after failure to hold price survival.
```

C08 should classify this as a 4B/local-burst pattern, not a durable customer-quality positive.

### Stress-test components

```text
raw_component_score_proxy:
  test_service_theme: high
  local_price_burst: high
  customer_quality_revenue_bridge: weak
  post_burst_survival: failed
  drawdown_penalty: extreme
```

---

## 8. Aggregate calibration takeaways

```text
positive_case_count: 1
counterexample_count: 2
local_4b_overlay_case_count: 2
hard_4c_candidate_count: 2
calibration_usable_trigger_count: 3
```

The three-case C08 grid:

```text
232140 와이씨:
  true memory-test equipment winner;
  strong MFE and price survival, but local 4B required after blowoff.

131970 두산테스나:
  test-service label without confirmed bridge;
  shallow MFE and high MAE, hard 4C candidate.

330860 네패스아크:
  local burst from test-service theme;
  later high MAE means 4B/local-burst, not Green.
```

Shared rule:

```text
C08 is not "semiconductor test name went up."
C08 is "test/socket capability is qualified by the right customer and converts into repeatable revenue and margin."
```

---

## 9. Machine-readable JSONL rows

```jsonl
{"row_type":"case","case_id":"C08_R2L91_232140_2024_03_20","scheduled_round":"R2","scheduled_loop":91,"large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY","fine_archetype_id":"HBM_AI_MEMORY_TEST_AND_OSAT_CUSTOMER_QUALITY_BRIDGE_VS_SEMI_TEST_LABEL_PRICE_SPIKE","symbol":"232140","name":"와이씨","trigger_date":"2024-03-20","entry_date":"2024-03-20","entry_price":7930,"peak_high":19240,"peak_date":"2024-07-29","worst_forward_low_after_peak":10830,"worst_forward_low_after_peak_date":"2024-09-09","mfe_pct":142.6,"peak_to_later_low_drawdown_pct":-43.7,"classification":"positive_with_local_4b_memory_test_equipment_customer_quality","calibration_usable":true,"evidence_family":"memory_test_equipment_customer_quality_order_bridge","residual_error":"positive_entry_but_large_mfe_requires_local_4b_overlay","shadow_rule_candidate":"allow_actionable_when_test_equipment_customer_quality_and_price_survival_confirm; require_4b_after_100pct_mfe"}
{"row_type":"case","case_id":"C08_R2L91_131970_2024_03_20","scheduled_round":"R2","scheduled_loop":91,"large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY","fine_archetype_id":"HBM_AI_MEMORY_TEST_AND_OSAT_CUSTOMER_QUALITY_BRIDGE_VS_SEMI_TEST_LABEL_PRICE_SPIKE","symbol":"131970","name":"두산테스나","trigger_date":"2024-03-20","entry_date":"2024-03-20","entry_price":47600,"peak_high":53300,"peak_date":"2024-04-05","worst_low":27650,"worst_low_date":"2024-09-09","mfe_pct":12.0,"mae_pct":-41.9,"classification":"hard_4c_candidate_test_service_label_without_customer_quality_bridge","calibration_usable":true,"evidence_family":"test_service_label_without_customer_quality_utilization_margin_bridge","residual_error":"test_service_label_can_overpromote_without_revenue_margin_bridge","shadow_rule_candidate":"block_actionable_green_if_mfe_shallow_mae_large_and_customer_quality_bridge_missing"}
{"row_type":"case","case_id":"C08_R2L91_330860_2024_02_21","scheduled_round":"R2","scheduled_loop":91,"large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY","fine_archetype_id":"HBM_AI_MEMORY_TEST_AND_OSAT_CUSTOMER_QUALITY_BRIDGE_VS_SEMI_TEST_LABEL_PRICE_SPIKE","symbol":"330860","name":"네패스아크","trigger_date":"2024-02-21","entry_date":"2024-02-21","entry_price":36900,"peak_high":46400,"peak_date":"2024-03-12","worst_low":12000,"worst_low_date":"2024-09-09","mfe_pct":25.7,"mae_pct":-67.5,"classification":"local_burst_but_high_mae_counterexample","calibration_usable":true,"evidence_family":"test_service_theme_local_burst_without_price_survival","residual_error":"local_burst_can_be_mistaken_for_customer_quality_green","shadow_rule_candidate":"keep_local_burst_as_4b_watch_not_green_if_post_burst_survival_fails"}
```

```jsonl
{"row_type":"aggregate","scheduled_round":"R2","scheduled_loop":91,"large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY","fine_archetype_id":"HBM_AI_MEMORY_TEST_AND_OSAT_CUSTOMER_QUALITY_BRIDGE_VS_SEMI_TEST_LABEL_PRICE_SPIKE","case_count":3,"positive_case_count":1,"counterexample_count":2,"local_4b_overlay_case_count":2,"hard_4c_candidate_count":2,"calibration_usable_trigger_count":3,"loop_contribution_label":"residual_error_found","do_not_propose_new_weight_delta":true}
{"row_type":"shadow_rule","scheduled_round":"R2","scheduled_loop":91,"canonical_archetype_id":"C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY","rule_id":"C08_CUSTOMER_QUALITY_REVENUE_BRIDGE_REQUIRED","rule_type":"canonical_archetype_specific_guard","rule_text":"For C08, do not open Stage2-Actionable or Stage3-Green from semiconductor-test, socket, OSAT, or AI/HBM label alone. Require customer qualification, repeatable order or utilization evidence, revenue bridge, margin bridge, and post-trigger price survival. If MFE is shallow and MAE is large, route to false-positive or hard-4C. If MFE exceeds 100%, preserve positive classification but attach local 4B unless a new revision bridge appears.","expected_effect":"Reduce test/socket false positives while preserving true memory-test equipment winners with customer-quality and price-survival evidence.","production_scoring_changed":false,"shadow_weight_only":true}
{"row_type":"residual_contribution","scheduled_round":"R2","scheduled_loop":91,"canonical_archetype_id":"C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY","residual_type":"semi_test_customer_quality_bridge_guard","contribution":"Adds one strong memory-test equipment positive and two test-service false positives to calibrate C08 customer-quality and price-survival rules.","do_not_count_as_global_weight_delta":true}
```

---

## 10. Proposed canonical-archetype shadow rule

```text
C08_CUSTOMER_QUALITY_REVENUE_BRIDGE_REQUIRED

IF canonical_archetype_id == C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY:

  Do not open Stage3-Green from:
    - semiconductor-test label alone
    - socket / probe / OSAT label alone
    - HBM / AI readthrough alone
    - one-day customer-rumor spike alone
    - local volume burst alone

  Require at least two of:
    - named or strongly evidenced customer qualification
    - repeat order / backlog / utilization evidence
    - revenue conversion
    - gross margin or OP margin bridge
    - product mix or test-complexity improvement
    - low-MAE post-trigger price survival

  If MFE < 15% and MAE < -30%:
    route to C08 false-positive / hard-4C candidate.

  If MFE > 20% but MAE later exceeds -50%:
    classify as local 4B / burst failure, not Green.

  If MFE > 100%:
    local 4B overlay is mandatory unless a new revision bridge appears.

  Distinguish:
    - memory test equipment with price survival
    - from generic OSAT/test-service label without customer-quality conversion.
```

---

## 11. Deferred Coding Agent Handoff Prompt

```text
You are a coding agent working on Songdaiki/stock_agent.

Do not treat this research MD as production scoring by itself.
Batch it with other v12 residual research files.

Source file:
e2r_stock_web_v12_residual_round_R2_loop_91_L2_AI_SEMICONDUCTOR_ELECTRONICS_C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY_research.md

Task:
1. Parse machine-readable JSONL rows.
2. Add the three C08 semi test/socket/customer-quality cases to calibration research ingestion.
3. Preserve production_scoring_changed=false.
4. Treat the proposed rule only as a shadow canonical-archetype guard candidate:
   C08_CUSTOMER_QUALITY_REVENUE_BRIDGE_REQUIRED.
5. Do not change global weights directly.
6. Compare against existing C08 cases and deduplicate by:
   canonical_archetype_id + symbol + trigger_type + entry_date.
7. If enough C08 cases agree, consider implementing a canonical guard that:
   - blocks semiconductor-test label Green without customer-quality/revenue/margin bridge,
   - preserves memory-test equipment positives with price survival,
   - attaches local 4B after blowoff,
   - routes shallow-MFE/high-MAE test-service cases to C08 false-positive or hard-4C.

Expected next schedule:
completed_round = R2
completed_loop = 91
next_round = R3
next_loop = 91
round_schedule_status = valid
round_sector_consistency = pass
```

---

## 12. Required round-state footer

```text
completed_round = R2
completed_loop = 91
next_round = R3
next_loop = 91
round_schedule_status = valid
round_sector_consistency = pass
```
