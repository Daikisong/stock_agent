# E2R Stock-Web v12 Residual Research — R4 / Loop 99

```yaml
scheduled_round: R4
scheduled_loop: 99
large_sector_id: L4_MATERIALS_SPREAD_RESOURCE
canonical_archetype_id: C16_STRATEGIC_RESOURCE_POLICY_SUPPLY
fine_archetype_id: GAS_LNG_LITHIUM_RARE_EARTH_RESOURCE_POLICY_SUPPLY_PRICE_TARIFF_INVENTORY_MARGIN_BRIDGE_VS_STRATEGIC_RESOURCE_LABEL_SPIKE

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
hard_4c_candidate_count: 2
gas_lng_resource_policy_case_count: 1
lithium_resource_processing_case_count: 1
rare_earth_policy_case_count: 1
strategic_resource_policy_to_cashflow_bridge_missing_count: 2
price_tariff_inventory_margin_bridge_missing_count: 2
market_segment_or_old_corporate_action_caveat_count: 3
row_presence_or_low_liquidity_caveat_count: 2
rejected_candidate_count: 1
calibration_usable_trigger_count: 3

loop_contribution_label: residual_error_found
canonical_archetype_rule_candidate: true
do_not_propose_new_weight_delta: true

completed_round: R4
completed_loop: 99
next_round: R5
next_loop: 99
round_schedule_status: valid
round_sector_consistency: pass
```

---

## 1. Schedule resolution

Previous completed file in the active sequence was:

```text
e2r_stock_web_v12_residual_round_R3_loop_99_L3_BATTERY_EV_GREEN_MOBILITY_C11_BATTERY_ORDERBOOK_RERATING_research.md
```

Under v12:

```text
R1 -> R2 -> R3 -> R4 -> R5 -> R6 -> R7 -> R8 -> R9 -> R10 -> R11 -> R12 -> R13 -> R1
```

Therefore:

```text
scheduled_round = R4
scheduled_loop = 99
large_sector_id = L4_MATERIALS_SPREAD_RESOURCE
```

R4 hard gate requires:

```text
large_sector_id = L4_MATERIALS_SPREAD_RESOURCE
```

Recent R4 branch usage:

```text
loop96: C16_STRATEGIC_RESOURCE_POLICY_SUPPLY
loop97: C17_CHEMICAL_COMMODITY_MARGIN_SPREAD
loop98: C15_MATERIAL_SPREAD_SUPERCYCLE
```

This run returns to C16 after the R4 branch cycle.

Selected fine branch:

```text
gas / LNG / lithium resource-processing / rare-earth policy
policy supply, tariff and regulated price, import and inventory timing,
resource security, customer demand, commodity spread, working capital,
and margin / cashflow bridge
vs generic strategic-resource policy label spike
```

---

## 2. No-repeat / novelty check

No-Repeat Index coverage snapshot:

```text
C16_STRATEGIC_RESOURCE_POLICY_SUPPLY
rows: 36
symbols: 23
date_range: 2022-10-20~2024-10-11
good/bad S2: 14/9
4B/4C: 2/0
URL pending/proxy: 17/17
top covered symbols:
  047400(6), 005490(3), 012320(3), 001570(2), 081150(2), 101670(2)
```

Selected symbols:

```text
036460 한국가스공사
009520 포스코엠텍
000910 유니온
```

They avoid the C16 top-covered symbols and avoid recent R4 names:

```text
C16 top-covered avoid:
  047400, 005490, 012320, 001570, 081150, 101670

recent R4 avoid:
  loop98 C15: 104700, 084010, 008260
  loop97 C17: 014830, 009830, 298000
  loop96 C16: 006260, 000670, 011810
  loop95 C15: 001430, 005010, 002240
```

Rejected candidate:

```text
005810 풍산홀딩스
  checked as a copper / strategic-resource holding candidate,
  but profile has a 2024-03-22 corporate-action candidate.
  It is not used as a clean early-2024 C16 validation case in this run.
```

Hard duplicate key:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

Novelty classification:

```text
036460: same archetype, new symbol, gas/LNG regulated-resource policy positive with Green cap
009520: same archetype, new symbol, lithium/resource-processing label hard-4C candidate after policy label failed price survival
000910: same archetype, new symbol, rare-earth policy label hard-4C candidate with low-liquidity / row-trust cap
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
036460 한국가스공사
  profile: atlas/symbol_profiles/036/036460.json
  first_date: 1999-12-15
  last_date: 2026-02-20
  market: KOSPI
  tradable_ohlcv rows: 6,452
  non_tradable_zero_volume rows: 0
  corporate_action_candidate_dates: none
  2024 entry~D+180 contamination: none

009520 포스코엠텍
  profile: atlas/symbol_profiles/009/009520.json
  name history:
    삼정강업 -> 삼정피앤에이 -> 포스코엠텍
  first_date: 1997-11-10
  last_date: 2026-02-20
  market:
    KOSDAQ until 2024-06-13
    KOSDAQ GLOBAL from 2024-06-14
  tradable_ohlcv rows: 6,770
  non_tradable_zero_volume rows: 253
  corporate_action_candidate_dates:
    1999-03-30, 1999-04-22, 2011-01-05, 2012-05-14
  2024 entry~D+180 contamination: none
  caveat:
    old raw-discontinuity and market-segment caveats exist outside / around the selected validation window, but no 2024 raw corporate-action candidate.

000910 유니온
  profile: atlas/symbol_profiles/000/000910.json
  first_date: 1996-07-09 in tradable profile
  raw_first_date: 1996-07-03
  last_date: 2026-02-20
  market: KOSPI
  tradable_ohlcv rows: 7,329
  non_tradable_zero_volume rows: 91
  corporate_action_candidate_dates:
    1997-01-03, 2008-05-07
  2024 entry~D+180 contamination: none
  caveat:
    historical row-presence / old corporate-action caveat exists outside selected 2024 validation window.

Rejected:
005810 풍산홀딩스
  corporate_action_candidate_dates include 2024-03-22.
  Not used as a clean early-2024 validation candidate.
```

---

## 4. Archetype residual problem

C16 is about strategic-resource policy and supply. It is not a generic "resource stock moved" or "policy theme is hot" archetype.

The model can over-score:

```text
gas / LNG / strategic energy label
lithium / resource-processing label
rare earth / strategic material label
resource security policy headline
state-owned or regulated utility salience
China export-control / geopolitics headline
import substitution or domestic supply-chain label
one-week strategic-resource stock volume spike
late chase after resource-policy rerating
```

The C16 bridge must be stricter:

```text
strategic-resource / policy-supply event
  -> named resource, import channel, domestic policy, tariff, customer, or region
  -> physical supply or contracted volume
  -> regulated price / tariff / selling-price mechanism
  -> input commodity price, FX, freight, and inventory timing
  -> working-capital and balance-sheet burden
  -> state policy / subsidy / price-cap and political-risk check
  -> customer demand and downstream conversion
  -> cash collection and margin / OP conversion
  -> event-window separation after failed first trigger
  -> price survival after the first resource-policy spike
```

A C16 thesis is like a strategic-resource pipeline or stockpile. The policy headline opens the valve, but equity value appears only when physical volume flows, tariff or selling price covers input cost, inventory does not trap cash, and the resource story reaches operating margin rather than staying as a policy label.

---

## 5. Case 1 — 036460 한국가스공사

```yaml
case_id: C16_R4L99_036460_2024_02_01
symbol: "036460"
name: "한국가스공사"
canonical_archetype_id: C16_STRATEGIC_RESOURCE_POLICY_SUPPLY
fine_archetype_id: GAS_LNG_LITHIUM_RARE_EARTH_RESOURCE_POLICY_SUPPLY_PRICE_TARIFF_INVENTORY_MARGIN_BRIDGE_VS_STRATEGIC_RESOURCE_LABEL_SPIKE
trigger_date: 2024-02-01
entry_date: 2024-02-01
entry_price_basis: close
entry_price: 27550
classification: positive_gas_lng_regulated_resource_policy_supply_tariff_cashflow_bridge_with_green_cap
calibration_usable: true
```

### Evidence interpretation

한국가스공사 is the constructive C16 gas / LNG resource-policy control.

The useful C16 read is not simply:

```text
에너지 / 자원주가 강하다
```

It is:

```text
strategic gas / LNG resource infrastructure
  -> resource-security and supply-policy salience
  -> regulated tariff / price mechanism and cashflow readthrough
  -> strong July-August price confirmation
  -> Green cap because tariff, receivables, commodity cost, policy risk, and cashflow evidence must refresh
```

The forward path produced a large MFE with controlled early drawdown. This preserves positive classification. However, after the large rerating, C16 Green should remain capped unless tariff / regulated-price mechanism, LNG procurement cost, receivables, working capital, policy risk, and OP/cashflow evidence are current.

### Price path

Key Stock-Web rows:

```text
2024-02-01: high 28,550 / low 25,800 / close 27,550
2024-02-19: high 30,600 / close 30,600
2024-04-17: low 24,850 / close 25,000
2024-07-29: high 45,750 / close 44,100
2024-08-16: high 51,100 / close 50,500
2024-08-30: high 53,000 / close 52,200
2024-09-03: high 53,800 / close 53,300
2024-11-01: low 37,750 / close 37,750
```

Approximate path from entry close:

```text
entry_close: 27,550
peak_high: 53,800
MFE: +95.3%
worst_low_after_entry: 24,550
MAE: -10.9%
```

### Interpretation

This is a C16 positive with Green cap:

```text
Stage2-Actionable: possible if tariff / regulated price, LNG supply cost, receivables, cash collection, and policy bridge are explicit.
Stage3-Green: blocked after +90% MFE unless fresh tariff/cost/cashflow evidence appears.
Local 4B: monitor if resource-policy price outruns tariff and balance-sheet evidence.
Hard 4C: no.
```

### Stress-test components

```text
raw_component_score_proxy:
  gas_lng_resource_security_relevance: high
  regulated_tariff_bridge: medium_high
  procurement_cost_fx_bridge: medium
  receivables_working_capital_bridge: medium
  policy_risk_bridge: medium
  cashflow_op_bridge: medium_high
  price_confirmation: very_high
  drawdown_penalty: low_to_medium
  green_cap: required_after_large_mfe
```

---

## 6. Case 2 — 009520 포스코엠텍

```yaml
case_id: C16_R4L99_009520_2024_02_01
symbol: "009520"
name: "포스코엠텍"
canonical_archetype_id: C16_STRATEGIC_RESOURCE_POLICY_SUPPLY
fine_archetype_id: GAS_LNG_LITHIUM_RARE_EARTH_RESOURCE_POLICY_SUPPLY_PRICE_TARIFF_INVENTORY_MARGIN_BRIDGE_VS_STRATEGIC_RESOURCE_LABEL_SPIKE
trigger_date: 2024-02-01
entry_date: 2024-02-01
entry_price_basis: close
entry_price: 23550
classification: hard_4c_candidate_lithium_resource_processing_label_without_policy_to_volume_margin_survival
calibration_usable: true
```

### Evidence interpretation

포스코엠텍 is the lithium / resource-processing hard C16 guardrail.

The label can fool the model:

```text
lithium / resource-processing / POSCO resource-chain readthrough
  -> domestic battery-resource supply-chain story
  -> strategic mineral policy salience
  -> short resource-stock event beta
```

But from the selected February entry, the path produced only modest MFE and then crossed the hard drawdown zone. The bridge from lithium/resource label to physical volume, customer demand, selling price, input cost, inventory timing, working capital, and margin was not proven.

### Price path

Key Stock-Web rows:

```text
2024-02-01: high 23,600 / low 22,750 / close 23,550
2024-02-16: high 26,300 / close 25,450
2024-04-17: low 18,700 / close 18,700
2024-08-05: low 14,660 / close 14,820
2024-09-02: high 20,550 / close 19,190
2024-10-25: low 15,510 / close 15,660
```

Approximate path from entry close:

```text
entry_close: 23,550
peak_high_first_phase: 26,300
MFE: +11.7%
worst_low_after_entry: 14,660
MAE: -37.7%
```

### Interpretation

This is a hard C16 false-positive candidate:

```text
Stage2-Watch: possible from lithium / resource-processing relevance.
Stage2-Actionable: blocked unless physical resource volume, customer demand, price mechanism, inventory, and margin bridge are explicit.
Stage3-Green: blocked.
Hard 4C: yes by modest MFE and -35%+ MAE.
Event-window separation: the September 2024 resource spike should be separated from the failed February trigger.
```

The lesson is that lithium-chain salience is not policy-to-volume margin survival.

### Stress-test components

```text
raw_component_score_proxy:
  lithium_resource_processing_label: high
  domestic_resource_policy_signal: medium_high
  physical_volume_bridge: weak
  customer_demand_bridge: weak_to_medium
  price_inventory_bridge: weak
  margin_op_bridge: weak
  market_segment_caveat: medium
  price_confirmation: modest
  drawdown_penalty: high
  hard_4c_guard: yes
```

---

## 7. Case 3 — 000910 유니온

```yaml
case_id: C16_R4L99_000910_2024_02_01
symbol: "000910"
name: "유니온"
canonical_archetype_id: C16_STRATEGIC_RESOURCE_POLICY_SUPPLY
fine_archetype_id: GAS_LNG_LITHIUM_RARE_EARTH_RESOURCE_POLICY_SUPPLY_PRICE_TARIFF_INVENTORY_MARGIN_BRIDGE_VS_STRATEGIC_RESOURCE_LABEL_SPIKE
trigger_date: 2024-02-01
entry_date: 2024-02-01
entry_price_basis: close
entry_price: 5420
classification: hard_4c_candidate_rare_earth_policy_label_without_supply_volume_cashflow_margin_bridge
calibration_usable: true
```

### Evidence interpretation

유니온 is the rare-earth / strategic-material hard guardrail.

The label can fool the model:

```text
rare earth / strategic material label
  -> China export-control or geopolitics readthrough
  -> domestic resource-security policy theme
  -> low-liquidity resource-stock beta
```

But from the selected February trigger, the path produced shallow MFE and then fell into a hard drawdown zone. The policy label did not translate into named supply volume, contract demand, input/output price bridge, cash collection, or margin survival.

### Price path

Key Stock-Web rows:

```text
2024-02-01: high 5,490 / low 5,370 / close 5,420
2024-02-15: high 5,840 / close 5,800
2024-04-19: high 5,760 / close 5,760
2024-08-05: low 3,360 / close 4,100
2024-09-06: low 3,905 / close 3,920
2024-10-16: high 5,320 / close 4,535
```

Approximate path from entry close:

```text
entry_close: 5,420
peak_high_first_phase: 5,840
MFE: +7.7%
worst_low_after_entry: 3,360
MAE: -38.0%
```

The October 2024 spike should be treated as a new event window, not rescue of the failed February trigger.

### Interpretation

This is a hard C16 false-positive candidate:

```text
Stage2-Watch: possible from rare-earth / strategic-material relevance.
Stage2-Actionable: blocked unless named resource policy, customer demand, supply volume, price mechanism, inventory, and margin bridge are explicit.
Stage3-Green: blocked.
Hard 4C: yes by shallow MFE and hard-zone MAE.
Row/liquidity caveat: yes.
```

The lesson is that rare-earth geopolitics is not resource-supply cashflow by itself.

### Stress-test components

```text
raw_component_score_proxy:
  rare_earth_policy_label: high
  geopolitics_export_control_signal: medium_high
  named_supply_bridge: weak
  customer_volume_bridge: weak
  price_inventory_bridge: weak
  cashflow_margin_bridge: weak
  row_liquidity_caveat: medium_high
  price_confirmation: shallow
  drawdown_penalty: high
  hard_4c_guard: yes
```

---

## 8. Aggregate calibration takeaways

```text
positive_case_count: 1
counterexample_count: 2
watch_or_cap_case_count: 2
local_4b_overlay_case_count: 1
hard_4c_candidate_count: 2
gas_lng_resource_policy_case_count: 1
lithium_resource_processing_case_count: 1
rare_earth_policy_case_count: 1
strategic_resource_policy_to_cashflow_bridge_missing_count: 2
price_tariff_inventory_margin_bridge_missing_count: 2
market_segment_or_old_corporate_action_caveat_count: 3
row_presence_or_low_liquidity_caveat_count: 2
rejected_candidate_count: 1
calibration_usable_trigger_count: 3
```

The three-case C16 strategic-resource grid:

```text
036460 한국가스공사:
  gas / LNG regulated-resource positive;
  large MFE and controlled MAE, but Green requires fresh tariff, cost, receivables, working-capital, and cashflow evidence.

009520 포스코엠텍:
  lithium / resource-processing label failed;
  modest MFE and hard-zone MAE, hard 4C candidate.

000910 유니온:
  rare-earth / strategic-material policy label failed;
  shallow MFE and hard-zone MAE, hard 4C candidate.
```

Shared rule:

```text
C16 is not "strategic resource label is geopolitically hot."
C16 is "policy becomes physical volume, tariff or selling price covers input and freight cost, inventory does not trap cash, and OP/cashflow is visible."
```

---

## 9. Machine-readable JSONL rows

```jsonl
{"row_type":"case","case_id":"C16_R4L99_036460_2024_02_01","scheduled_round":"R4","scheduled_loop":99,"large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C16_STRATEGIC_RESOURCE_POLICY_SUPPLY","fine_archetype_id":"GAS_LNG_LITHIUM_RARE_EARTH_RESOURCE_POLICY_SUPPLY_PRICE_TARIFF_INVENTORY_MARGIN_BRIDGE_VS_STRATEGIC_RESOURCE_LABEL_SPIKE","symbol":"036460","name":"한국가스공사","trigger_date":"2024-02-01","entry_date":"2024-02-01","entry_price":27550,"peak_high":53800,"peak_date":"2024-09-03","worst_low_after_entry":24550,"worst_low_after_entry_date":"2024-04-12","mfe_pct":95.3,"mae_pct":-10.9,"classification":"positive_gas_lng_regulated_resource_policy_supply_tariff_cashflow_bridge_with_green_cap","calibration_usable":true,"evidence_family":"gas_lng_resource_security_regulated_tariff_procurement_cost_receivables_working_capital_cashflow_margin_bridge","residual_error":"gas_lng_resource_policy_positive_requires_green_cap_after_large_mfe_without_refreshed_tariff_cost_receivables_cashflow_evidence","shadow_rule_candidate":"allow_capped_actionable_when_tariff_cost_receivables_and_cashflow_bridge_confirm_but_cap_green_after_large_mfe"}
{"row_type":"case","case_id":"C16_R4L99_009520_2024_02_01","scheduled_round":"R4","scheduled_loop":99,"large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C16_STRATEGIC_RESOURCE_POLICY_SUPPLY","fine_archetype_id":"GAS_LNG_LITHIUM_RARE_EARTH_RESOURCE_POLICY_SUPPLY_PRICE_TARIFF_INVENTORY_MARGIN_BRIDGE_VS_STRATEGIC_RESOURCE_LABEL_SPIKE","symbol":"009520","name":"포스코엠텍","trigger_date":"2024-02-01","entry_date":"2024-02-01","entry_price":23550,"peak_high_first_phase":26300,"peak_date":"2024-02-16","worst_low_after_entry":14660,"worst_low_after_entry_date":"2024-08-05","mfe_pct":11.7,"mae_pct":-37.7,"classification":"hard_4c_candidate_lithium_resource_processing_label_without_policy_to_volume_margin_survival","calibration_usable":true,"market_segment_or_old_corporate_action_caveat":true,"event_window_separation_required":true,"evidence_family":"lithium_resource_processing_policy_label_without_physical_volume_customer_demand_price_inventory_margin_bridge","residual_error":"lithium_resource_label_can_fail_when_policy_does_not_convert_to_volume_and_margin_survival","shadow_rule_candidate":"route_lithium_resource_processing_label_to_hard_4c_if_mfe_modest_mae_hard_zone_and_volume_margin_bridge_missing"}
{"row_type":"case","case_id":"C16_R4L99_000910_2024_02_01","scheduled_round":"R4","scheduled_loop":99,"large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C16_STRATEGIC_RESOURCE_POLICY_SUPPLY","fine_archetype_id":"GAS_LNG_LITHIUM_RARE_EARTH_RESOURCE_POLICY_SUPPLY_PRICE_TARIFF_INVENTORY_MARGIN_BRIDGE_VS_STRATEGIC_RESOURCE_LABEL_SPIKE","symbol":"000910","name":"유니온","trigger_date":"2024-02-01","entry_date":"2024-02-01","entry_price":5420,"peak_high_first_phase":5840,"peak_date":"2024-02-15","worst_low_after_entry":3360,"worst_low_after_entry_date":"2024-08-05","mfe_pct":7.7,"mae_pct":-38.0,"classification":"hard_4c_candidate_rare_earth_policy_label_without_supply_volume_cashflow_margin_bridge","calibration_usable":true,"row_presence_or_old_corporate_action_caveat":true,"event_window_separation_required":true,"evidence_family":"rare_earth_strategic_material_policy_geopolitics_label_without_named_supply_customer_price_inventory_cashflow_margin_bridge","residual_error":"rare_earth_policy_label_can_fail_when_supply_volume_and_cashflow_margin_bridge_missing","shadow_rule_candidate":"route_rare_earth_policy_label_to_hard_4c_if_mfe_shallow_mae_hard_zone_and_supply_cashflow_bridge_missing"}
```

```jsonl
{"row_type":"aggregate","scheduled_round":"R4","scheduled_loop":99,"large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C16_STRATEGIC_RESOURCE_POLICY_SUPPLY","fine_archetype_id":"GAS_LNG_LITHIUM_RARE_EARTH_RESOURCE_POLICY_SUPPLY_PRICE_TARIFF_INVENTORY_MARGIN_BRIDGE_VS_STRATEGIC_RESOURCE_LABEL_SPIKE","case_count":3,"positive_case_count":1,"counterexample_count":2,"watch_or_cap_case_count":2,"local_4b_overlay_case_count":1,"hard_4c_candidate_count":2,"gas_lng_resource_policy_case_count":1,"lithium_resource_processing_case_count":1,"rare_earth_policy_case_count":1,"strategic_resource_policy_to_cashflow_bridge_missing_count":2,"price_tariff_inventory_margin_bridge_missing_count":2,"market_segment_or_old_corporate_action_caveat_count":3,"row_presence_or_low_liquidity_caveat_count":2,"rejected_candidate_count":1,"calibration_usable_trigger_count":3,"loop_contribution_label":"residual_error_found","do_not_propose_new_weight_delta":true}
{"row_type":"shadow_rule","scheduled_round":"R4","scheduled_loop":99,"canonical_archetype_id":"C16_STRATEGIC_RESOURCE_POLICY_SUPPLY","rule_id":"C16_RESOURCE_POLICY_SUPPLY_PRICE_INVENTORY_CASHFLOW_MARGIN_BRIDGE_REQUIRED","rule_type":"canonical_archetype_specific_guard","rule_text":"For C16 strategic-resource policy/supply cases, do not open Stage2-Actionable or Stage3-Green from gas/LNG, lithium, rare-earth, strategic-material, resource-security, state-owned/regulated utility, China export-control/geopolitics, import-substitution, domestic supply-chain, one-week resource-stock volume spike, or late chase after resource-policy rerating labels alone. Require named resource/import channel/domestic policy/tariff/customer/region, physical supply or contracted volume, regulated price/tariff/selling-price mechanism, input commodity price/FX/freight/inventory timing, working-capital and balance-sheet burden control, state policy/subsidy/price-cap and political-risk check, customer demand and downstream conversion, cash collection and margin/OP conversion, event-window separation after failed first trigger, and post-trigger price survival. Gas/LNG resource-policy positives with large MFE may be capped Actionable when tariff/cost/receivables/cashflow bridge is explicit, but Green requires fresh evidence. Lithium/resource-processing labels with modest MFE and hard-zone MAE should route to hard-4C when physical volume and margin bridge are missing. Rare-earth policy labels with shallow MFE and hard-zone MAE should route to hard-4C when named supply, customer demand, and cashflow bridge are missing.","expected_effect":"Preserve true strategic-resource supply positives while reducing generic gas/LNG, lithium, rare-earth, geopolitics, import-substitution, and resource-security false positives where physical volume, tariff/price, inventory, working capital, and margin evidence fail.","production_scoring_changed":false,"shadow_weight_only":true}
{"row_type":"residual_contribution","scheduled_round":"R4","scheduled_loop":99,"canonical_archetype_id":"C16_STRATEGIC_RESOURCE_POLICY_SUPPLY","residual_type":"resource_policy_supply_price_inventory_cashflow_margin_guard","contribution":"Adds one gas/LNG regulated-resource positive and two lithium/rare-earth hard-4C counterexamples to calibrate C16 physical supply, regulated price/tariff, input cost, inventory, working capital, policy risk, cash collection, and margin requirements.","do_not_count_as_global_weight_delta":true}
```

---

## 10. Proposed canonical-archetype shadow rule

```text
C16_RESOURCE_POLICY_SUPPLY_PRICE_INVENTORY_CASHFLOW_MARGIN_BRIDGE_REQUIRED

IF canonical_archetype_id == C16_STRATEGIC_RESOURCE_POLICY_SUPPLY:

  Do not open Stage3-Green from:
    - gas / LNG / strategic energy label alone
    - lithium / resource-processing label alone
    - rare earth / strategic material label alone
    - resource security policy headline alone
    - state-owned or regulated utility salience alone
    - China export-control / geopolitics headline alone
    - import substitution or domestic supply-chain label alone
    - one-week strategic-resource stock volume spike alone
    - late chase after resource-policy rerating alone

  Require at least two of:
    - named resource / import channel / domestic policy / tariff / customer / region
    - physical supply or contracted volume
    - regulated price / tariff / selling-price mechanism
    - input commodity price / FX / freight / inventory timing
    - working-capital and balance-sheet burden control
    - state policy / subsidy / price-cap and political-risk check
    - customer demand and downstream conversion
    - cash collection and margin / OP conversion
    - low-MAE post-trigger price survival
    - fresh evidence after the strategic-resource headline

  If MFE < 12% and MAE <= -35%:
    route to C16 hard-4C candidate.

  If MFE is large but tariff / price / inventory / cashflow evidence is stale:
    preserve as capped positive or local 4B, not Green.

  If later event-like spikes appear after first-phase failure:
    create a new event window; do not retroactively validate the failed first trigger.

  If row-presence, market-segment, old corporate-action, or low-liquidity caveat exists:
    apply additional trust cap, but do not contaminate clean 2024 rows.

  Distinguish:
    - companies where resource policy becomes physical volume, price/tariff, cash collection, and OP
    - from labels where policy salience never reaches supply, inventory, and margin.
```

---

## 11. Deferred Coding Agent Handoff Prompt

```text
You are a coding agent working on Songdaiki/stock_agent.

Do not treat this research MD as production scoring by itself.
Batch it with other v12 residual research files.

Source file:
e2r_stock_web_v12_residual_round_R4_loop_99_L4_MATERIALS_SPREAD_RESOURCE_C16_STRATEGIC_RESOURCE_POLICY_SUPPLY_research.md

Task:
1. Parse machine-readable JSONL rows.
2. Add the three C16 strategic-resource policy/supply cases to calibration research ingestion.
3. Preserve production_scoring_changed=false.
4. Treat the proposed rule only as a shadow canonical-archetype guard candidate:
   C16_RESOURCE_POLICY_SUPPLY_PRICE_INVENTORY_CASHFLOW_MARGIN_BRIDGE_REQUIRED.
5. Do not change global weights directly.
6. Compare against existing C16 cases and deduplicate by:
   canonical_archetype_id + symbol + trigger_type + entry_date.
7. If enough C16 cases agree, consider implementing a canonical guard that:
   - blocks strategic-resource Green without named resource/policy/tariff/customer, physical supply, price mechanism, inventory, cashflow, and margin bridge,
   - preserves gas/LNG positives only with price survival and fresh tariff/cost/receivables evidence,
   - routes modest-MFE/hard-MAE lithium/resource-processing labels to hard-4C,
   - routes shallow-MFE/hard-MAE rare-earth policy labels to hard-4C,
   - separates renewed event windows from earlier failed resource-policy triggers,
   - applies market-segment, low-liquidity, row-presence, and old corporate-action caveats when needed.

Expected next schedule:
completed_round = R4
completed_loop = 99
next_round = R5
next_loop = 99
round_schedule_status = valid
round_sector_consistency = pass
```

---

## 12. Required round-state footer

```text
completed_round = R4
completed_loop = 99
next_round = R5
next_loop = 99
round_schedule_status = valid
round_sector_consistency = pass
```
