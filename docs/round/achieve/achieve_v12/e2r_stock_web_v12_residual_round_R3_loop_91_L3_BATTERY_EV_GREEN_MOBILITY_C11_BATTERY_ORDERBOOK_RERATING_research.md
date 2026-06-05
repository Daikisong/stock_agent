# E2R Stock-Web v12 Residual Research — R3 / Loop 91

```yaml
scheduled_round: R3
scheduled_loop: 91
large_sector_id: L3_BATTERY_EV_GREEN_MOBILITY
canonical_archetype_id: C11_BATTERY_ORDERBOOK_RERATING
fine_archetype_id: BATTERY_MATERIALS_ORDERBOOK_UTILIZATION_MARGIN_BRIDGE_VS_GENERIC_EV_BETA

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
local_4b_overlay_case_count: 1
hard_4c_candidate_count: 1
calibration_usable_trigger_count: 3

loop_contribution_label: residual_error_found
canonical_archetype_rule_candidate: true
do_not_propose_new_weight_delta: true

completed_round: R3
completed_loop: 91
next_round: R4
next_loop: 91
round_schedule_status: valid
round_sector_consistency: pass
```

---

## 1. Schedule resolution

Previous completed file in the active sequence was:

```text
e2r_stock_web_v12_residual_round_R2_loop_91_L2_AI_SEMICONDUCTOR_ELECTRONICS_C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY_research.md
```

Under v12:

```text
R1 -> R2 -> R3 -> R4 -> R5 -> R6 -> R7 -> R8 -> R9 -> R10 -> R11 -> R12 -> R13 -> R1
```

Therefore:

```text
scheduled_round = R3
scheduled_loop = 91
large_sector_id = L3_BATTERY_EV_GREEN_MOBILITY
```

Recent R3 branch usage already covered:

```text
loop88: C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK
loop89: C14_EV_DEMAND_SLOWDOWN_4B_4C
loop90: C13_BATTERY_JV_UTILIZATION_AMPC_IRA
```

This run therefore selects:

```text
canonical_archetype_id = C11_BATTERY_ORDERBOOK_RERATING
```

---

## 2. No-repeat / novelty check

No-Repeat Index coverage snapshot:

```text
C11_BATTERY_ORDERBOOK_RERATING
rows: 21
symbols: 14
date_range: 2023-01-31~2024-06-21
good/bad S2: 8/4
4B/4C: 1/0
URL pending/proxy: 10/10
top covered symbols:
  137400(4), 299030(3), 003670(2), 302430(2), 001570(1), 005070(1)
```

Selected symbols:

```text
011790 SKC
020150 롯데에너지머티리얼즈
006110 삼아알미늄
```

These avoid the top-covered C11 list. They also avoid the most recent R3 loop90 symbols:

```text
373220, 006400, 096770
```

Hard duplicate key:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

Novelty classification:

```text
011790: same archetype, new symbol, copper-foil / battery-material orderbook utilization rerating branch
020150: same archetype, new symbol, copper-foil orderbook headline without durable utilization bridge
006110: same archetype, new symbol, aluminum-foil orderbook / customer call-off false-positive branch
```

Note:

```text
020150 appears in other battery archetype coverage, but this file uses C11 with a distinct orderbook-rerating failure mode.
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
011790 SKC
  profile: atlas/symbol_profiles/011/011790.json
  first_date: 1997-07-18
  last_date: 2026-02-20
  tradable_ohlcv rows: 7,105
  corporate_action_candidate_dates:
    1998-01-03, 2001-12-21
  2024 entry~D+180 contamination: none

020150 롯데에너지머티리얼즈
  profile: atlas/symbol_profiles/020/020150.json
  first_date: 2011-03-04
  last_date: 2026-02-20
  tradable_ohlcv rows: 3,681
  corporate_action_candidate_dates: none
  2024 entry~D+180 contamination: none

006110 삼아알미늄
  profile: atlas/symbol_profiles/006/006110.json
  first_date: 1995-05-02
  last_date: 2026-02-20
  tradable_ohlcv rows: 7,041
  corporate_action_candidate_dates:
    2000-10-16, 2000-11-14, 2007-05-04, 2011-04-26, 2023-02-09
  2024 entry~D+180 contamination: none
```

---

## 4. Archetype residual problem

C11 is the battery-orderbook rerating archetype.

It should not be triggered by:

```text
battery material label
EV recovery hope
generic customer orderbook language
capacity expansion headline
one-quarter price spike
```

The bridge must be narrower:

```text
orderbook
  -> committed customer volume
  -> utilization
  -> ramp timing
  -> ASP / mix
  -> margin recovery
  -> OP/EPS conversion
  -> price survival
```

Battery orderbooks can behave like a warehouse full of boxes with customer names on them. They look valuable only if the customer actually calls them off, the plant runs, the ASP covers cost, and margin comes out the other side.

---

## 5. Case 1 — 011790 SKC

```yaml
case_id: C11_R3L91_011790_2024_03_05
symbol: "011790"
name: "SKC"
canonical_archetype_id: C11_BATTERY_ORDERBOOK_RERATING
fine_archetype_id: BATTERY_MATERIALS_ORDERBOOK_UTILIZATION_MARGIN_BRIDGE_VS_GENERIC_EV_BETA
trigger_date: 2024-03-05
entry_date: 2024-03-05
entry_price_basis: close
entry_price: 95800
classification: positive_with_local_4b_copper_foil_orderbook_rerating
calibration_usable: true
```

### Evidence interpretation

SKC is the constructive case. The path behaves like the market saw more than a generic battery-material label:

```text
copper-foil / battery material capacity
  -> orderbook or utilization rerating expectation
  -> sharp price confirmation
  -> extended MFE
```

However, the move also later suffered a deep peak-to-trough drawdown. This is a C11 positive with mandatory 4B discipline, not a clean "hold through anything" Green.

### Price path

Key Stock-Web rows:

```text
2024-03-05: close 95,800
2024-03-14: close 114,700
2024-03-19: high 127,300 / close 123,800
2024-04-08: high 147,500 / close 145,300
2024-06-26: close 158,800
2024-06-28: high 175,900 / close 168,600
2024-07-10: high 179,600 / close 176,300
2024-08-05: low 107,600 / close 114,100
2024-09-27: high 152,000 / close 151,500
```

Approximate return path from entry close:

```text
entry_close: 95,800
peak_high: 179,600
MFE: +87.5%
worst_low_after_peak: 104,300
MAE vs entry: positive cushion remained
peak_to_later_low_drawdown: -41.9%
```

### Interpretation

This is a positive but not an unrestricted Green.

```text
Stage2-Actionable: valid if orderbook/utilization/margin bridge exists.
Stage3-Green: possible only with explicit customer-volume and margin conversion.
Local 4B: required after large MFE and peak drawdown.
Hard 4C: no.
```

### Stress-test components

```text
raw_component_score_proxy:
  orderbook_relevance: high
  battery_material_relevance: high
  utilization_margin_bridge: medium
  price_confirmation: very_high
  peak_drawdown_risk: high
  local_4b_overlay: required
```

---

## 6. Case 2 — 020150 롯데에너지머티리얼즈

```yaml
case_id: C11_R3L91_020150_2024_03_20
symbol: "020150"
name: "롯데에너지머티리얼즈"
canonical_archetype_id: C11_BATTERY_ORDERBOOK_RERATING
fine_archetype_id: BATTERY_MATERIALS_ORDERBOOK_UTILIZATION_MARGIN_BRIDGE_VS_GENERIC_EV_BETA
trigger_date: 2024-03-20
entry_date: 2024-03-20
entry_price_basis: close
entry_price: 42350
classification: counterexample_copper_foil_orderbook_headline_without_durable_utilization_bridge
calibration_usable: true
```

### Evidence interpretation

롯데에너지머티리얼즈 has a plausible copper-foil / battery-material orderbook story. The failure mode is that the stock path did not sustain a C11 rerating unless the model could prove utilization, customer call-off, and margin conversion.

The early path produced a decent burst, but the later drawdown erased the argument for Green.

### Price path

Key Stock-Web rows:

```text
2024-03-20: close 42,350
2024-03-21: high 49,200 / close 47,050
2024-03-25: high 51,500 / close 50,700
2024-03-27: high 52,400 / close 51,000
2024-04-09: low 44,500 / close 45,000
2024-07-11: low 47,650 / close 47,650
2024-08-05: low 30,500 / close 32,200
2024-09-05: high 45,650 / close 43,000
```

Approximate return path from entry close:

```text
entry_close: 42,350
peak_high: 52,400
MFE: +23.7%
worst_low: 30,500
MAE: -28.0%
```

### Interpretation

This is a counterexample with local-burst characteristics.

```text
Stage2-Watch: allowed.
Stage2-Actionable: only if orderbook converts to utilization and margin.
Stage3-Green: blocked by high MAE and failure to survive the EV slowdown path.
Hard 4C: not the hardest, but false-positive guard applies.
```

### Stress-test components

```text
raw_component_score_proxy:
  orderbook_label: high
  utilization_bridge: weak_to_medium
  margin_bridge: weak
  local_price_burst: medium
  drawdown_penalty: high
  green_block: yes
```

---

## 7. Case 3 — 006110 삼아알미늄

```yaml
case_id: C11_R3L91_006110_2024_02_20
symbol: "006110"
name: "삼아알미늄"
canonical_archetype_id: C11_BATTERY_ORDERBOOK_RERATING
fine_archetype_id: BATTERY_MATERIALS_ORDERBOOK_UTILIZATION_MARGIN_BRIDGE_VS_GENERIC_EV_BETA
trigger_date: 2024-02-20
entry_date: 2024-02-20
entry_price_basis: close
entry_price: 108600
classification: hard_4c_candidate_aluminum_foil_orderbook_without_calloff_margin_bridge
calibration_usable: true
```

### Evidence interpretation

삼아알미늄 is the hard guardrail case.

The company can be placed in a battery-material orderbook bucket through aluminum-foil / packaging material exposure. But the price path shows that the market did not validate durable C11 rerating from the orderbook idea alone.

The model must require:

```text
customer call-off
utilization
ASP / spread
margin conversion
cash-flow visibility
```

before opening Actionable/Green.

### Price path

Key Stock-Web rows:

```text
2024-02-20: close 108,600
2024-02-21: high 116,400 / close 110,700
2024-03-26: high 98,000 / close 92,600
2024-03-28: low 85,500 / close 85,500
2024-07-16: low 63,300 / close 63,400
2024-08-05: low 39,600 / close 42,000
2024-09-27: high 55,000 / close 54,000
```

Approximate return path from entry close:

```text
entry_close: 108,600
peak_high: 116,400
MFE: +7.2%
worst_low: 39,600
MAE: -63.5%
```

### Interpretation

This is a hard 4C candidate:

```text
Stage2-Watch: possible from battery-material exposure.
Stage2-Actionable: blocked without call-off/utilization/margin bridge.
Stage3-Green: blocked.
Hard 4C: yes.
```

The path is the textbook C11 mistake: orderbook label without demand realization.

### Stress-test components

```text
raw_component_score_proxy:
  orderbook_label: medium_high
  customer_calloff_visibility: weak
  utilization_bridge: weak
  margin_bridge: weak
  price_confirmation: failed
  drawdown_penalty: extreme
```

---

## 8. Aggregate calibration takeaways

```text
positive_case_count: 1
counterexample_count: 2
local_4b_overlay_case_count: 1
hard_4c_candidate_count: 1
calibration_usable_trigger_count: 3
```

The three-case C11 grid:

```text
011790 SKC:
  strong copper-foil / battery-material rerating path;
  positive, but local 4B required after large MFE.

020150 롯데에너지머티리얼즈:
  local copper-foil orderbook burst,
  but high MAE without durable utilization/margin bridge.

006110 삼아알미늄:
  hard 4C case;
  battery-material orderbook label collapsed without call-off and margin confirmation.
```

Shared rule:

```text
C11 is not "battery orderbook exists."
C11 is "the orderbook is called off into utilized capacity and margin."
```

---

## 9. Machine-readable JSONL rows

```jsonl
{"row_type":"case","case_id":"C11_R3L91_011790_2024_03_05","scheduled_round":"R3","scheduled_loop":91,"large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C11_BATTERY_ORDERBOOK_RERATING","fine_archetype_id":"BATTERY_MATERIALS_ORDERBOOK_UTILIZATION_MARGIN_BRIDGE_VS_GENERIC_EV_BETA","symbol":"011790","name":"SKC","trigger_date":"2024-03-05","entry_date":"2024-03-05","entry_price":95800,"peak_high":179600,"peak_date":"2024-07-10","worst_low_after_peak":104300,"worst_low_after_peak_date":"2024-09-09","mfe_pct":87.5,"peak_to_later_low_drawdown_pct":-41.9,"classification":"positive_with_local_4b_copper_foil_orderbook_rerating","calibration_usable":true,"evidence_family":"copper_foil_battery_material_orderbook_utilization_margin_bridge","residual_error":"positive_entry_but_large_mfe_and_drawdown_require_local_4b_overlay","shadow_rule_candidate":"allow_actionable_when_orderbook_utilization_margin_bridge_and_price_survival_confirm; require_4b_after_large_mfe"}
{"row_type":"case","case_id":"C11_R3L91_020150_2024_03_20","scheduled_round":"R3","scheduled_loop":91,"large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C11_BATTERY_ORDERBOOK_RERATING","fine_archetype_id":"BATTERY_MATERIALS_ORDERBOOK_UTILIZATION_MARGIN_BRIDGE_VS_GENERIC_EV_BETA","symbol":"020150","name":"롯데에너지머티리얼즈","trigger_date":"2024-03-20","entry_date":"2024-03-20","entry_price":42350,"peak_high":52400,"peak_date":"2024-03-27","worst_low":30500,"worst_low_date":"2024-08-05","mfe_pct":23.7,"mae_pct":-28.0,"classification":"counterexample_copper_foil_orderbook_headline_without_durable_utilization_bridge","calibration_usable":true,"evidence_family":"copper_foil_orderbook_burst_without_utilization_margin_bridge","residual_error":"local_orderbook_burst_can_be_mistaken_for_green","shadow_rule_candidate":"cap_at_watch_yellow_if_orderbook_headline_lacks_utilization_margin_bridge_and_mae_gt_25"}
{"row_type":"case","case_id":"C11_R3L91_006110_2024_02_20","scheduled_round":"R3","scheduled_loop":91,"large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C11_BATTERY_ORDERBOOK_RERATING","fine_archetype_id":"BATTERY_MATERIALS_ORDERBOOK_UTILIZATION_MARGIN_BRIDGE_VS_GENERIC_EV_BETA","symbol":"006110","name":"삼아알미늄","trigger_date":"2024-02-20","entry_date":"2024-02-20","entry_price":108600,"peak_high":116400,"peak_date":"2024-02-21","worst_low":39600,"worst_low_date":"2024-08-05","mfe_pct":7.2,"mae_pct":-63.5,"classification":"hard_4c_candidate_aluminum_foil_orderbook_without_calloff_margin_bridge","calibration_usable":true,"evidence_family":"aluminum_foil_battery_orderbook_without_customer_calloff_margin_bridge","residual_error":"battery_material_orderbook_label_can_create_catastrophic_false_positive","shadow_rule_candidate":"block_actionable_green_if_mfe_shallow_mae_large_and_customer_calloff_margin_bridge_missing"}
```

```jsonl
{"row_type":"aggregate","scheduled_round":"R3","scheduled_loop":91,"large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C11_BATTERY_ORDERBOOK_RERATING","fine_archetype_id":"BATTERY_MATERIALS_ORDERBOOK_UTILIZATION_MARGIN_BRIDGE_VS_GENERIC_EV_BETA","case_count":3,"positive_case_count":1,"counterexample_count":2,"local_4b_overlay_case_count":1,"hard_4c_candidate_count":1,"calibration_usable_trigger_count":3,"loop_contribution_label":"residual_error_found","do_not_propose_new_weight_delta":true}
{"row_type":"shadow_rule","scheduled_round":"R3","scheduled_loop":91,"canonical_archetype_id":"C11_BATTERY_ORDERBOOK_RERATING","rule_id":"C11_ORDERBOOK_UTILIZATION_MARGIN_BRIDGE_REQUIRED","rule_type":"canonical_archetype_specific_guard","rule_text":"For C11, do not open Stage2-Actionable or Stage3-Green from battery-material orderbook, capacity, or EV beta headline alone. Require customer call-off, utilization, ramp timing, ASP/mix, margin recovery, OP/EPS conversion, and price survival. If MFE is shallow and MAE is large, route to false-positive or hard-4C. If MFE is large but later peak drawdown exceeds 40%, preserve positive classification but attach local 4B watch.","expected_effect":"Reduce battery-material orderbook false positives while preserving true rerating cases where orderbook converts into utilization, margin, and price survival.","production_scoring_changed":false,"shadow_weight_only":true}
{"row_type":"residual_contribution","scheduled_round":"R3","scheduled_loop":91,"canonical_archetype_id":"C11_BATTERY_ORDERBOOK_RERATING","residual_type":"battery_orderbook_utilization_margin_guard","contribution":"Adds one copper-foil positive and two battery-material orderbook false positives to separate orderbook labels from utilization and margin conversion.","do_not_count_as_global_weight_delta":true}
```

---

## 10. Proposed canonical-archetype shadow rule

```text
C11_ORDERBOOK_UTILIZATION_MARGIN_BRIDGE_REQUIRED

IF canonical_archetype_id == C11_BATTERY_ORDERBOOK_RERATING:

  Do not open Stage3-Green from:
    - battery-material label alone
    - long-term orderbook headline alone
    - capacity expansion headline alone
    - EV recovery beta alone
    - one-day orderbook price spike alone

  Require at least two of:
    - named customer call-off evidence
    - utilization/ramp schedule
    - ASP or product-mix bridge
    - margin recovery evidence
    - OP/EPS conversion
    - low-MAE post-trigger price survival
    - revision confirmation after orderbook headline

  If MFE < 10% and MAE < -30%:
    route to C11 false-positive / hard-4C candidate.

  If MFE > 20% but MAE < -25%:
    cap at Watch/Yellow unless utilization and margin bridge are explicit.

  If MFE > 50% but later peak drawdown > -40%:
    keep positive entry but attach local 4B watch.

  Distinguish:
    - copper-foil/material names with price survival and utilization evidence
    - from aluminum/copper-foil orderbook labels where customer call-off and margin are unconfirmed.
```

---

## 11. Deferred Coding Agent Handoff Prompt

```text
You are a coding agent working on Songdaiki/stock_agent.

Do not treat this research MD as production scoring by itself.
Batch it with other v12 residual research files.

Source file:
e2r_stock_web_v12_residual_round_R3_loop_91_L3_BATTERY_EV_GREEN_MOBILITY_C11_BATTERY_ORDERBOOK_RERATING_research.md

Task:
1. Parse machine-readable JSONL rows.
2. Add the three C11 battery orderbook/materials cases to calibration research ingestion.
3. Preserve production_scoring_changed=false.
4. Treat the proposed rule only as a shadow canonical-archetype guard candidate:
   C11_ORDERBOOK_UTILIZATION_MARGIN_BRIDGE_REQUIRED.
5. Do not change global weights directly.
6. Compare against existing C11 cases and deduplicate by:
   canonical_archetype_id + symbol + trigger_type + entry_date.
7. If enough C11 cases agree, consider implementing a canonical guard that:
   - blocks battery-orderbook Green without customer call-off, utilization, and margin bridge,
   - preserves true rerating cases with strong price survival,
   - attaches local 4B after large MFE and deep peak drawdown,
   - routes shallow-MFE/high-MAE material-orderbook labels to C11 false-positive or hard-4C.

Expected next schedule:
completed_round = R3
completed_loop = 91
next_round = R4
next_loop = 91
round_schedule_status = valid
round_sector_consistency = pass
```

---

## 12. Required round-state footer

```text
completed_round = R3
completed_loop = 91
next_round = R4
next_loop = 91
round_schedule_status = valid
round_sector_consistency = pass
```
