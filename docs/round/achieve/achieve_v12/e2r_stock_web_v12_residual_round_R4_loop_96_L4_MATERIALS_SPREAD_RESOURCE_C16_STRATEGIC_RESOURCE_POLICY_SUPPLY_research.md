# E2R Stock-Web v12 Residual Research — R4 / Loop 96

```yaml
scheduled_round: R4
scheduled_loop: 96
large_sector_id: L4_MATERIALS_SPREAD_RESOURCE
canonical_archetype_id: C16_STRATEGIC_RESOURCE_POLICY_SUPPLY
fine_archetype_id: COPPER_ZINC_RESOURCE_TRADING_POLICY_SUPPLY_CHAIN_PRICE_PASS_THROUGH_TRUST_BRIDGE_VS_STRATEGIC_RESOURCE_LABEL_SPIKE

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
hard_4c_candidate_count: 2
strategic_copper_supply_case_count: 1
zinc_smelter_resource_case_count: 1
resource_trading_case_count: 1
cross_sector_confound_caveat_count: 2
governance_or_control_confounded_case_count: 1
corporate_action_caveat_avoided_count: 1
row_presence_or_tradeability_caveat_count: 2
calibration_usable_trigger_count: 3

loop_contribution_label: residual_error_found
canonical_archetype_rule_candidate: true
do_not_propose_new_weight_delta: true

completed_round: R4
completed_loop: 96
next_round: R5
next_loop: 96
round_schedule_status: valid
round_sector_consistency: pass
```

---

## 1. Schedule resolution

Previous completed file in the active sequence was:

```text
e2r_stock_web_v12_residual_round_R3_loop_96_L3_BATTERY_EV_GREEN_MOBILITY_C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK_research.md
```

Under v12:

```text
R1 -> R2 -> R3 -> R4 -> R5 -> R6 -> R7 -> R8 -> R9 -> R10 -> R11 -> R12 -> R13 -> R1
```

Therefore:

```text
scheduled_round = R4
scheduled_loop = 96
large_sector_id = L4_MATERIALS_SPREAD_RESOURCE
```

R4 hard gate requires:

```text
large_sector_id = L4_MATERIALS_SPREAD_RESOURCE
```

Recent R4 branch usage:

```text
loop93: C16_STRATEGIC_RESOURCE_POLICY_SUPPLY
loop94: C17_CHEMICAL_COMMODITY_MARGIN_SPREAD
loop95: C15_MATERIAL_SPREAD_SUPERCYCLE
```

This run returns to C16 after the R4 branch cycle, but avoids the C16 top-covered names and uses a different fine branch:

```text
copper / zinc / resource trading
policy supply-chain, price pass-through, customer exposure, and trust bridge
vs strategic-resource label spike
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
006260 LS
000670 영풍
011810 STX
```

They avoid the C16 top-covered list and avoid the most recent R4 loop95 C15 set:

```text
loop95 avoid: 001430, 005010, 002240
loop94 avoid: 002380, 011170, 161000
```

Hard duplicate key:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

Novelty classification:

```text
006260: same archetype, new symbol, copper/grid strategic-supply positive with cross-sector grid-capex confound and Green cap
000670: same archetype, new symbol, zinc/smelter strategic-resource label hard-4C before later governance/control confound
011810: same archetype, new symbol, resource-trading strategic-supply label hard-4C after post-corporate-action entry
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
006260 LS
  profile: atlas/symbol_profiles/006/006260.json
  name history:
    엘지전선 -> LG전선 -> LS전선 -> LS
  first_date: 1995-05-02
  last_date: 2026-02-20
  market: KOSPI
  tradable_ohlcv rows: 7,765
  non_tradable_zero_volume rows: 0
  corporate_action_candidate_dates:
    1996-01-04, 1996-12-04, 1999-06-11
  2024 entry~D+180 contamination: none

000670 영풍
  profile: atlas/symbol_profiles/000/000670.json
  first_date: 1995-05-04
  last_date: 2026-02-20
  market: KOSPI
  tradable_ohlcv rows: 6,704
  non_tradable_zero_volume rows: 1,061
  corporate_action_candidate_dates:
    2025-04-25
  2024 entry~D+180 contamination: none
  caveat:
    high historical non-tradable zero-volume count and later 2025 candidate add trust caution.
    2024 price path also has a later governance/control-premium confound that should not be counted as C16 resource-supply validation.

011810 STX
  profile: atlas/symbol_profiles/011/011810.json
  name history:
    쌍용중공업 -> STX
  first_date: 1995-05-02
  last_date: 2025-07-02 in tradable profile
  raw_last_date: 2026-02-20
  market: KOSPI
  tradable_ohlcv rows: 7,161
  non_tradable_zero_volume rows: 603
  corporate_action_candidate_dates include:
    2023-09-15, 2024-01-05
  selected entry:
    2024-02-16, after the 2024-01-05 corporate-action candidate window
  caveat:
    row-presence/tradeability trust cap applies.
```

---

## 4. Archetype residual problem

C16 is about strategic resource policy supply, procurement security, resource price exposure, pass-through, and trust. It is not a generic "resource stock" or "copper/zinc/mineral label" archetype.

The model can over-score:

```text
strategic resource policy headline
copper / zinc / nickel / lithium / rare metal label
resource trading or commodity-import label
grid / AI datacenter copper readthrough
China supply-chain risk
one-week resource-stock volume spike
governance/control event that happens to use a resource company
```

The C16 bridge must be stricter:

```text
strategic resource / supply-chain event
  -> named resource exposure or supply contract
  -> procurement / offtake / processing capacity
  -> customer or policy demand path
  -> inventory and price-risk management
  -> FX / commodity-price pass-through
  -> working-capital and funding burden
  -> margin / OP conversion
  -> governance, accounting, listing, and tradeability trust
  -> price survival after the first resource-label spike
```

A strategic-resource thesis is like a copper cable running through a grid. The market sees the shiny metal first, but C16 asks whether the company controls supply, passes price through, manages inventory and FX, collects cash, and converts the resource exposure into operating profit rather than just headline voltage.

---

## 5. Case 1 — 006260 LS

```yaml
case_id: C16_R4L96_006260_2024_02_01
symbol: "006260"
name: "LS"
canonical_archetype_id: C16_STRATEGIC_RESOURCE_POLICY_SUPPLY
fine_archetype_id: COPPER_ZINC_RESOURCE_TRADING_POLICY_SUPPLY_CHAIN_PRICE_PASS_THROUGH_TRUST_BRIDGE_VS_STRATEGIC_RESOURCE_LABEL_SPIKE
trigger_date: 2024-02-01
entry_date: 2024-02-01
entry_price_basis: close
entry_price: 96000
classification: positive_capped_copper_grid_strategic_supply_chain_price_pass_through_with_cross_sector_confound
calibration_usable: true
```

### Evidence interpretation

LS is the constructive C16 control, but with a cross-sector cap.

The useful C16 read is not simply:

```text
구리 / 전선 / 자원주가 강하다
```

It is:

```text
copper and cable supply-chain relevance
  -> grid / AI datacenter / power-infrastructure copper demand readthrough
  -> strategic supply and customer-demand bridge
  -> price pass-through and margin optionality
  -> strong price confirmation
```

The forward path delivered a large MFE with non-hard MAE. That supports positive classification. However, the move is not pure resource policy; it is also strongly entangled with grid CAPEX and power-infrastructure demand. Therefore C16 should preserve the positive path, but cap Green unless company-specific copper procurement, pass-through, inventory, customer order, and margin evidence is explicit.

### Price path

Key Stock-Web rows:

```text
2024-02-01: high 99,500 / close 96,000
2024-02-27: low 86,800 / close 87,300
2024-03-18: high 112,400 / close 110,600
2024-04-12: high 128,100 / close 122,100
2024-04-29: high 142,300 / close 138,300
2024-05-08: high 148,100 / close 144,500
2024-08-05: low 94,000 / close 99,700
2024-09-09: low 93,300 / close 97,900
```

Approximate path from entry close:

```text
entry_close: 96,000
peak_high: 148,100
MFE: +54.3%
worst_low_after_entry: 86,800
MAE: -9.6%
```

### Interpretation

This is a C16 positive with Green cap:

```text
Stage2-Actionable: possible if copper exposure, customer demand, pass-through, and margin bridge are explicit.
Stage3-Green: blocked unless fresh resource-specific procurement/inventory/pass-through evidence appears.
Local 4B: monitor after +50% MFE if grid-CAPEX or non-resource catalysts dominate.
Hard 4C: no.
Cross-sector confound: yes, C02 grid/power CAPEX overlap.
```

### Stress-test components

```text
raw_component_score_proxy:
  copper_supply_relevance: high
  strategic_resource_policy_signal: medium_high
  grid_power_capex_confound: high
  customer_order_bridge: medium_high
  pass_through_inventory_bridge: medium
  margin_op_bridge: medium
  price_confirmation: high
  drawdown_penalty: low_to_medium
  green_cap: yes
```

---

## 6. Case 2 — 000670 영풍

```yaml
case_id: C16_R4L96_000670_2024_02_01
symbol: "000670"
name: "영풍"
canonical_archetype_id: C16_STRATEGIC_RESOURCE_POLICY_SUPPLY
fine_archetype_id: COPPER_ZINC_RESOURCE_TRADING_POLICY_SUPPLY_CHAIN_PRICE_PASS_THROUGH_TRUST_BRIDGE_VS_STRATEGIC_RESOURCE_LABEL_SPIKE
trigger_date: 2024-02-01
entry_date: 2024-02-01
entry_price_basis: close
entry_price: 533000
classification: hard_4c_candidate_zinc_smelter_resource_label_without_supply_margin_trust_bridge_before_governance_confound
calibration_usable: true
```

### Evidence interpretation

영풍 is the zinc/smelter resource-label hard guardrail.

The company has real resource relevance:

```text
zinc / nonferrous smelting
resource supply and processing
strategic metal exposure
```

But C16 cannot use a later governance/control-premium-style spike as proof of strategic-resource supply execution. The resource-supply validation window is cut before the September governance/control confound. Before that later cross-archetype event, the forward path was a severe false-positive: shallow MFE, large drawdown, and weak resource-to-margin evidence.

### Price path

Key Stock-Web rows:

```text
2024-02-01: high 546,000 / close 533,000
2024-02-06: high 547,000 / close 520,000
2024-04-17: low 389,500 / close 391,500
2024-08-05: low 280,000 / close 289,000
2024-09-13 onward: governance/control-premium confound begins; not counted as C16 resource-supply validation
2024-09-20: high 649,000 / close 570,000
```

Approximate path from entry close, resource-supply validation before governance confound:

```text
entry_close: 533,000
peak_high_before_confound: 547,000
MFE: +2.6%
worst_low_before_confound: 280,000
MAE: -47.5%
```

### Interpretation

This is a hard C16 false-positive:

```text
Stage2-Watch: possible from zinc/smelter resource relevance.
Stage2-Actionable: blocked unless supply contract, processing economics, price pass-through, inventory, and margin bridge are explicit.
Stage3-Green: blocked.
Hard 4C: yes by shallow MFE and high MAE before the governance/control confound.
Trust cap: yes, high historical non-tradable zero-volume count.
Cross-archetype confound: yes, later governance/control-price action is not C16 validation.
```

The lesson is that strategic-metal relevance is not resource-supply execution.

### Stress-test components

```text
raw_component_score_proxy:
  zinc_smelter_relevance: high
  strategic_resource_policy_signal: medium
  supply_contract_bridge: weak
  pass_through_inventory_bridge: weak_to_medium
  margin_op_bridge: weak
  price_confirmation_before_confound: failed
  governance_control_confound: high
  drawdown_penalty: high
  hard_4c_guard: yes
```

---

## 7. Case 3 — 011810 STX

```yaml
case_id: C16_R4L96_011810_2024_02_16
symbol: "011810"
name: "STX"
canonical_archetype_id: C16_STRATEGIC_RESOURCE_POLICY_SUPPLY
fine_archetype_id: COPPER_ZINC_RESOURCE_TRADING_POLICY_SUPPLY_CHAIN_PRICE_PASS_THROUGH_TRUST_BRIDGE_VS_STRATEGIC_RESOURCE_LABEL_SPIKE
trigger_date: 2024-02-16
entry_date: 2024-02-16
entry_price_basis: close
entry_price: 10950
classification: hard_4c_candidate_resource_trading_strategic_supply_label_without_offtake_cashflow_tradeability_trust
calibration_usable: true
```

### Evidence interpretation

STX is the resource-trading hard guardrail.

The profile has a 2024-01-05 corporate-action candidate, so the selected entry is after that window. Even after avoiding the immediate raw-price candidate window, the post-trigger path failed.

The model can be tempted by:

```text
resource trading
strategic minerals / commodity import
supply-chain diversification
one-day resource-stock volume spike
```

But from the selected close, MFE was shallow and the later MAE was severe. The bridge from resource trading label to offtake, procurement margin, cash collection, and tradeability trust was not proven.

### Price path

Key Stock-Web rows:

```text
2024-01-05: corporate-action candidate in profile
2024-02-16: high 11,900 / close 10,950
2024-02-27: low 8,990 / close 9,110
2024-04-17: low 7,160 / close 7,160
2024-08-05: low 5,000 / close 5,380
2024-09-09: low 4,800 / close 5,130
2024-10-25: low 4,700 / close 4,940
```

Approximate path from post-candidate entry close:

```text
entry_close: 10,950
peak_high_after_entry: 11,900
MFE: +8.7%
worst_low_after_entry: 4,700
MAE: -57.1%
```

### Interpretation

This is a hard C16 false-positive:

```text
Stage2-Watch: possible from resource-trading and strategic-mineral relevance.
Stage2-Actionable: blocked unless named resource, offtake, procurement, cash collection, and margin bridge are explicit.
Stage3-Green: blocked.
Hard 4C: yes by shallow MFE and severe MAE.
Corporate-action caveat: avoided by post-2024-01-05 entry.
Row/tradeability caveat: yes.
```

The lesson is that resource-trading label is not offtake-margin survival.

### Stress-test components

```text
raw_component_score_proxy:
  resource_trading_label: high
  strategic_supply_signal: medium_high
  named_offtake_bridge: weak
  procurement_cashflow_bridge: weak
  margin_op_bridge: weak
  accounting_tradeability_trust: weak
  price_confirmation_after_entry: failed
  hard_4c_guard: yes
```

---

## 8. Aggregate calibration takeaways

```text
positive_case_count: 1
counterexample_count: 2
watch_or_cap_case_count: 1
local_4b_overlay_case_count: 1
hard_4c_candidate_count: 2
strategic_copper_supply_case_count: 1
zinc_smelter_resource_case_count: 1
resource_trading_case_count: 1
cross_sector_confound_caveat_count: 2
governance_or_control_confounded_case_count: 1
corporate_action_caveat_avoided_count: 1
row_presence_or_tradeability_caveat_count: 2
calibration_usable_trigger_count: 3
```

The three-case C16 strategic-resource grid:

```text
006260 LS:
  copper/grid strategic-supply positive;
  large MFE and controlled MAE, but Green requires resource-specific pass-through and margin evidence.

000670 영풍:
  zinc/smelter resource label failed before later governance/control confound;
  shallow MFE and high MAE, hard 4C with trust caveat.

011810 STX:
  resource-trading strategic-supply label failed after post-corporate-action entry;
  shallow MFE and severe MAE, hard 4C with tradeability caveat.
```

Shared rule:

```text
C16 is not "resource label is hot."
C16 is "resource exposure becomes procurement security, offtake, price pass-through, inventory control, cash collection, and margin for this company."
```

---

## 9. Machine-readable JSONL rows

```jsonl
{"row_type":"case","case_id":"C16_R4L96_006260_2024_02_01","scheduled_round":"R4","scheduled_loop":96,"large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C16_STRATEGIC_RESOURCE_POLICY_SUPPLY","fine_archetype_id":"COPPER_ZINC_RESOURCE_TRADING_POLICY_SUPPLY_CHAIN_PRICE_PASS_THROUGH_TRUST_BRIDGE_VS_STRATEGIC_RESOURCE_LABEL_SPIKE","symbol":"006260","name":"LS","trigger_date":"2024-02-01","entry_date":"2024-02-01","entry_price":96000,"peak_high":148100,"peak_date":"2024-05-08","worst_low_after_entry":86800,"worst_low_after_entry_date":"2024-02-27","mfe_pct":54.3,"mae_pct":-9.6,"classification":"positive_capped_copper_grid_strategic_supply_chain_price_pass_through_with_cross_sector_confound","calibration_usable":true,"cross_sector_confound_caveat":true,"evidence_family":"copper_cable_grid_strategic_supply_customer_demand_pass_through_margin_bridge","residual_error":"positive_copper_supply_path_must_cap_green_when_grid_capex_confound_and_resource_specific_margin_bridge_not_refreshed","shadow_rule_candidate":"preserve_positive_but_cap_green_until_copper_procurement_pass_through_inventory_margin_evidence_refreshes"}
{"row_type":"case","case_id":"C16_R4L96_000670_2024_02_01","scheduled_round":"R4","scheduled_loop":96,"large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C16_STRATEGIC_RESOURCE_POLICY_SUPPLY","fine_archetype_id":"COPPER_ZINC_RESOURCE_TRADING_POLICY_SUPPLY_CHAIN_PRICE_PASS_THROUGH_TRUST_BRIDGE_VS_STRATEGIC_RESOURCE_LABEL_SPIKE","symbol":"000670","name":"영풍","trigger_date":"2024-02-01","entry_date":"2024-02-01","entry_price":533000,"peak_high_before_governance_confound":547000,"peak_date":"2024-02-06","worst_low_before_governance_confound":280000,"worst_low_date":"2024-08-05","mfe_pct":2.6,"mae_pct":-47.5,"classification":"hard_4c_candidate_zinc_smelter_resource_label_without_supply_margin_trust_bridge_before_governance_confound","calibration_usable":true,"row_presence_or_tradeability_caveat":true,"cross_sector_confound_caveat":true,"evidence_family":"zinc_smelter_strategic_resource_label_without_supply_contract_pass_through_margin_trust_bridge","residual_error":"resource_smelter_label_can_fail_before_later_governance_control_spike_and_must_not_auto_validate_c16","shadow_rule_candidate":"route_zinc_smelter_resource_label_to_hard_4c_if_mfe_shallow_mae_large_and_margin_trust_bridge_missing_before_confound"}
{"row_type":"case","case_id":"C16_R4L96_011810_2024_02_16","scheduled_round":"R4","scheduled_loop":96,"large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C16_STRATEGIC_RESOURCE_POLICY_SUPPLY","fine_archetype_id":"COPPER_ZINC_RESOURCE_TRADING_POLICY_SUPPLY_CHAIN_PRICE_PASS_THROUGH_TRUST_BRIDGE_VS_STRATEGIC_RESOURCE_LABEL_SPIKE","symbol":"011810","name":"STX","trigger_date":"2024-02-16","entry_date":"2024-02-16","entry_price":10950,"peak_high":11900,"peak_date":"2024-02-16","worst_low_after_entry":4700,"worst_low_after_entry_date":"2024-10-25","mfe_pct":8.7,"mae_pct":-57.1,"classification":"hard_4c_candidate_resource_trading_strategic_supply_label_without_offtake_cashflow_tradeability_trust","calibration_usable":true,"corporate_action_caveat_avoided":true,"row_presence_or_tradeability_caveat":true,"evidence_family":"resource_trading_strategic_supply_label_without_named_offtake_procurement_cashflow_margin_trust_bridge","residual_error":"resource_trading_label_can_fail_when_offtake_cashflow_and_tradeability_trust_bridge_missing","shadow_rule_candidate":"route_resource_trading_policy_supply_label_to_hard_4c_if_mfe_shallow_mae_severe_and_offtake_bridge_missing"}
```

```jsonl
{"row_type":"aggregate","scheduled_round":"R4","scheduled_loop":96,"large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C16_STRATEGIC_RESOURCE_POLICY_SUPPLY","fine_archetype_id":"COPPER_ZINC_RESOURCE_TRADING_POLICY_SUPPLY_CHAIN_PRICE_PASS_THROUGH_TRUST_BRIDGE_VS_STRATEGIC_RESOURCE_LABEL_SPIKE","case_count":3,"positive_case_count":1,"counterexample_count":2,"watch_or_cap_case_count":1,"local_4b_overlay_case_count":1,"hard_4c_candidate_count":2,"strategic_copper_supply_case_count":1,"zinc_smelter_resource_case_count":1,"resource_trading_case_count":1,"cross_sector_confound_caveat_count":2,"governance_or_control_confounded_case_count":1,"corporate_action_caveat_avoided_count":1,"row_presence_or_tradeability_caveat_count":2,"calibration_usable_trigger_count":3,"loop_contribution_label":"residual_error_found","do_not_propose_new_weight_delta":true}
{"row_type":"shadow_rule","scheduled_round":"R4","scheduled_loop":96,"canonical_archetype_id":"C16_STRATEGIC_RESOURCE_POLICY_SUPPLY","rule_id":"C16_RESOURCE_SUPPLY_PASSTHROUGH_MARGIN_TRUST_BRIDGE_REQUIRED","rule_type":"canonical_archetype_specific_guard","rule_text":"For C16, do not open Stage2-Actionable or Stage3-Green from strategic resource policy, copper/zinc/nickel/lithium/rare-metal label, resource trading, commodity import, grid/AI datacenter copper readthrough, China supply-chain risk, one-week resource-stock volume spike, or governance/control event involving a resource company alone. Require named resource exposure or supply contract, procurement/offtake/processing capacity, customer or policy demand path, inventory and price-risk management, FX/commodity-price pass-through, working-capital and funding burden, margin/OP conversion, governance/accounting/listing/tradeability trust, and post-trigger price survival. Copper/grid positives with large MFE may be capped Actionable when pass-through and margin bridge are explicit, but Green requires resource-specific evidence and cross-sector confound control. Zinc/smelter labels with shallow MFE and large MAE before governance confound should route to hard-4C. Resource-trading labels with corporate-action or tradeability caveats should route to hard-4C when named offtake and cashflow bridge are missing.","expected_effect":"Preserve true strategic-resource supply positives while reducing resource-label, cross-theme copper, governance-confounded, and resource-trading false positives.","production_scoring_changed":false,"shadow_weight_only":true}
{"row_type":"residual_contribution","scheduled_round":"R4","scheduled_loop":96,"canonical_archetype_id":"C16_STRATEGIC_RESOURCE_POLICY_SUPPLY","residual_type":"resource_supply_passthrough_margin_trust_guard","contribution":"Adds one copper/grid strategic-supply positive with cross-sector cap, one zinc/smelter hard-4C before governance confound, and one resource-trading hard-4C with corporate-action/tradeability caveat to calibrate C16 procurement, offtake, pass-through, margin, and trust requirements.","do_not_count_as_global_weight_delta":true}
```

---

## 10. Proposed canonical-archetype shadow rule

```text
C16_RESOURCE_SUPPLY_PASSTHROUGH_MARGIN_TRUST_BRIDGE_REQUIRED

IF canonical_archetype_id == C16_STRATEGIC_RESOURCE_POLICY_SUPPLY:

  Do not open Stage3-Green from:
    - strategic resource policy headline alone
    - copper / zinc / nickel / lithium / rare-metal label alone
    - resource trading or commodity-import label alone
    - grid / AI datacenter copper readthrough alone
    - China supply-chain risk label alone
    - one-week resource-stock volume spike alone
    - governance/control event involving a resource company alone

  Require at least two of:
    - named resource exposure or supply contract
    - procurement / offtake / processing-capacity clarity
    - customer or policy demand path
    - inventory and price-risk management
    - FX / commodity-price pass-through
    - working-capital and funding burden containment
    - margin / OP conversion
    - governance / accounting / listing / tradeability trust
    - low-MAE post-trigger price survival
    - fresh evidence after the resource-policy headline

  If MFE < 10% and MAE < -35%:
    route to C16 hard-4C candidate.

  If MFE is large but the catalyst may be grid/AI/cross-sector:
    preserve positive path but cap Green until resource-specific pass-through and margin evidence is proven.

  If a later governance/control event appears:
    do not retroactively validate the earlier C16 resource-supply trigger unless resource economics also improved.

  If row-presence, corporate-action, or tradeability caveat exists:
    apply additional trust cap and block contaminated windows.

  Distinguish:
    - companies where strategic resource exposure becomes supply, pass-through, cash collection, and margin
    - from resource labels where policy heat, inventory risk, or governance events break the bridge.
```

---

## 11. Deferred Coding Agent Handoff Prompt

```text
You are a coding agent working on Songdaiki/stock_agent.

Do not treat this research MD as production scoring by itself.
Batch it with other v12 residual research files.

Source file:
e2r_stock_web_v12_residual_round_R4_loop_96_L4_MATERIALS_SPREAD_RESOURCE_C16_STRATEGIC_RESOURCE_POLICY_SUPPLY_research.md

Task:
1. Parse machine-readable JSONL rows.
2. Add the three C16 strategic-resource supply cases to calibration research ingestion.
3. Preserve production_scoring_changed=false.
4. Treat the proposed rule only as a shadow canonical-archetype guard candidate:
   C16_RESOURCE_SUPPLY_PASSTHROUGH_MARGIN_TRUST_BRIDGE_REQUIRED.
5. Do not change global weights directly.
6. Compare against existing C16 cases and deduplicate by:
   canonical_archetype_id + symbol + trigger_type + entry_date.
7. If enough C16 cases agree, consider implementing a canonical guard that:
   - blocks resource-label Green without named resource/offtake/procurement/pass-through/margin/trust bridge,
   - preserves copper/grid positives only with price survival and resource-specific margin evidence,
   - caps cross-sector grid/AI copper reratings until resource economics are proven,
   - routes shallow-MFE/high-MAE zinc/smelter labels to hard-4C before governance confounds,
   - routes resource-trading labels with missing offtake/cashflow/trust bridge to hard-4C,
   - applies corporate-action/row-presence/tradeability trust caps.

Expected next schedule:
completed_round = R4
completed_loop = 96
next_round = R5
next_loop = 96
round_schedule_status = valid
round_sector_consistency = pass
```

---

## 12. Required round-state footer

```text
completed_round = R4
completed_loop = 96
next_round = R5
next_loop = 96
round_schedule_status = valid
round_sector_consistency = pass
```
