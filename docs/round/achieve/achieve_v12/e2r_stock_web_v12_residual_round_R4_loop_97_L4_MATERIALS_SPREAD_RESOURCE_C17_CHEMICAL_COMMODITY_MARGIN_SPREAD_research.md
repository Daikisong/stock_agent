# E2R Stock-Web v12 Residual Research — R4 / Loop 97

```yaml
scheduled_round: R4
scheduled_loop: 97
large_sector_id: L4_MATERIALS_SPREAD_RESOURCE
canonical_archetype_id: C17_CHEMICAL_COMMODITY_MARGIN_SPREAD
fine_archetype_id: CHLOR_ALKALI_POTASH_SOLAR_CHEM_POLYPROPYLENE_FEEDSTOCK_SPREAD_MARGIN_BRIDGE_VS_COMMODITY_CHEMICAL_LABEL_SPIKE

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
chlor_alkali_potash_case_count: 1
solar_chemical_spread_case_count: 1
polypropylene_commodity_chemical_case_count: 1
commodity_spread_margin_bridge_missing_count: 2
balance_sheet_or_tradeability_caveat_count: 1
row_presence_caveat_count: 2
calibration_usable_trigger_count: 3

loop_contribution_label: residual_error_found
canonical_archetype_rule_candidate: true
do_not_propose_new_weight_delta: true

completed_round: R4
completed_loop: 97
next_round: R5
next_loop: 97
round_schedule_status: valid
round_sector_consistency: pass
```

---

## 1. Schedule resolution

Previous completed file in the active sequence was:

```text
e2r_stock_web_v12_residual_round_R3_loop_97_L3_BATTERY_EV_GREEN_MOBILITY_C14_EV_DEMAND_SLOWDOWN_4B_4C_research.md
```

Under v12:

```text
R1 -> R2 -> R3 -> R4 -> R5 -> R6 -> R7 -> R8 -> R9 -> R10 -> R11 -> R12 -> R13 -> R1
```

Therefore:

```text
scheduled_round = R4
scheduled_loop = 97
large_sector_id = L4_MATERIALS_SPREAD_RESOURCE
```

R4 hard gate requires:

```text
large_sector_id = L4_MATERIALS_SPREAD_RESOURCE
```

Recent R4 branch usage:

```text
loop94: C17_CHEMICAL_COMMODITY_MARGIN_SPREAD
loop95: C15_MATERIAL_SPREAD_SUPERCYCLE
loop96: C16_STRATEGIC_RESOURCE_POLICY_SUPPLY
```

This run returns to C17 after the R4 branch cycle, but avoids the C17 top-covered names and uses a different fine branch:

```text
chlor-alkali / potash / solar chemical / polypropylene commodity spread
feedstock cost, selling price, inventory, working capital, and margin bridge
vs generic commodity chemical label spike
```

---

## 2. No-repeat / novelty check

No-Repeat Index coverage snapshot:

```text
C17_CHEMICAL_COMMODITY_MARGIN_SPREAD
rows: 21
symbols: 15
date_range: 2020-08-07~2024-03-21
good/bad S2: 8/3
4B/4C: 4/0
URL pending/proxy: 0/0
top covered symbols:
  004000(3), 006650(2), 011780(2), 014680(2), 298020(2), 001390(1)
```

Selected symbols:

```text
014830 유니드
009830 한화솔루션
298000 효성화학
```

They avoid the C17 top-covered list and avoid recent R4 loop94~96 symbols:

```text
loop94 C17 avoid: 002380, 011170, 161000
loop95 C15 avoid: 001430, 005010, 002240
loop96 C16 avoid: 006260, 000670, 011810
C17 top-covered avoid: 004000, 006650, 011780, 014680, 298020, 001390
```

Hard duplicate key:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

Novelty classification:

```text
014830: same archetype, new symbol, chlor-alkali / potash spread positive with Green cap and 4B watch
009830: same archetype, new symbol, solar-chemical / commodity spread label hard-4C without margin survival
298000: same archetype, new symbol, polypropylene / commodity chemical local burst followed by severe high-MAE 4B failure
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
014830 유니드
  profile: atlas/symbol_profiles/014/014830.json
  first_date: 2004-12-03
  last_date: 2026-02-20
  market: KOSPI
  tradable_ohlcv rows: 5,213
  non_tradable_zero_volume rows: 22
  corporate_action_candidate_dates:
    2015-08-18, 2022-11-28
  2024 entry~D+180 contamination: none
  caveat:
    older corporate-action candidates are outside the selected 2024 validation window.

009830 한화솔루션
  profile: atlas/symbol_profiles/009/009830.json
  name history:
    한화종합화학 -> 한화종화 -> 한화석화 -> 한화케미칼 -> 한화솔루션
  selected 2024 trigger name:
    한화솔루션
  first_date: 1995-05-02
  last_date: 2026-02-20
  market: KOSPI
  tradable_ohlcv rows: 7,741
  non_tradable_zero_volume rows: 23
  invalid_zero_ohlc rows: 1
  corporate_action_candidate_dates:
    1999-04-20, 2008-07-04
  2024 entry~D+180 contamination: none
  caveat:
    old raw-discontinuity / row-presence caveat exists outside selected 2024 validation window.

298000 효성화학
  profile: atlas/symbol_profiles/298/298000.json
  first_date: 2018-07-13
  last_date: 2025-02-28 in tradable profile
  raw_last_date: 2026-02-20
  market: KOSPI
  tradable_ohlcv rows: 1,629
  non_tradable_zero_volume rows: 237
  corporate_action_candidate_dates: none
  2024 entry~D+180 contamination: none
  caveat:
    row-presence / tradeability caveat and balance-sheet trust cap are required because tradable and raw row histories diverge after 2025.
```

---

## 4. Archetype residual problem

C17 is about chemical commodity margin spread. It is not a generic "chemical stock" or "commodity beta" archetype.

The model can over-score:

```text
chemical commodity label
chlor-alkali / caustic / potash label
PVC / polyolefin / polypropylene label
solar chemical / polysilicon / downstream clean-energy label
feedstock price relief headline
one-week chemical-stock volume spike
low-PBR or restructuring hope in distressed chemical names
```

The C17 bridge must be stricter:

```text
chemical commodity / spread event
  -> named product and feedstock exposure
  -> input price and output selling-price direction
  -> inventory and working-capital timing
  -> demand by end-market and export channel
  -> utilization and plant reliability
  -> FX / freight / energy-cost check
  -> margin / OP conversion
  -> balance-sheet and refinancing trust where relevant
  -> price survival after the first chemical-label spike
```

A C17 chemical spread thesis is like a distillation column. The market sees the steam first, but equity value appears only when input cost, selling price, inventory timing, plant utilization, and working capital settle into operating margin.

---

## 5. Case 1 — 014830 유니드

```yaml
case_id: C17_R4L97_014830_2024_02_01
symbol: "014830"
name: "유니드"
canonical_archetype_id: C17_CHEMICAL_COMMODITY_MARGIN_SPREAD
fine_archetype_id: CHLOR_ALKALI_POTASH_SOLAR_CHEM_POLYPROPYLENE_FEEDSTOCK_SPREAD_MARGIN_BRIDGE_VS_COMMODITY_CHEMICAL_LABEL_SPIKE
trigger_date: 2024-02-01
entry_date: 2024-02-01
entry_price_basis: close
entry_price: 76500
classification: positive_chlor_alkali_potash_spread_price_confirmation_with_green_cap_and_4b_watch
calibration_usable: true
```

### Evidence interpretation

유니드 is the constructive C17 control in this set.

The useful C17 read is not simply:

```text
화학주가 올랐다
```

It is:

```text
chlor-alkali / potassium chemical spread relevance
  -> product spread and export demand optionality
  -> feedstock / energy-cost discipline
  -> strong price confirmation into May
  -> later margin-refresh requirement
```

The forward path produced a large MFE into May and did not enter hard-failure territory in the selected window. This preserves positive classification. However, Green should be capped unless product spread, inventory, export demand, cost, and margin evidence refresh the thesis.

### Price path

Key Stock-Web rows:

```text
2024-02-01: high 77,000 / close 76,500
2024-02-21: high 84,000 / close 80,200
2024-04-25: high 101,700 / close 92,000
2024-05-07: high 108,200 / close 106,300
2024-05-09: high 109,500 / close 102,900
2024-08-05: low 76,400 / close 78,500
2024-10-25: low 65,000 / close 65,200
```

Approximate path from entry close:

```text
entry_close: 76,500
peak_high: 109,500
MFE: +43.1%
worst_low_after_entry: 65,000
MAE: -15.0%
```

### Interpretation

This is a C17 positive with Green cap:

```text
Stage2-Actionable: possible if product spread, end-market demand, inventory, and cost bridge are explicit.
Stage3-Green: blocked without fresh spread and margin evidence after the rerating.
Local 4B: monitor after +40% MFE if spread evidence becomes stale.
Hard 4C: no.
```

### Stress-test components

```text
raw_component_score_proxy:
  chlor_alkali_potash_relevance: high
  product_spread_bridge: medium_high
  export_demand_bridge: medium
  feedstock_energy_cost_bridge: medium_high
  inventory_working_capital_bridge: medium
  price_confirmation: high
  drawdown_penalty: medium
  green_cap: yes
```

---

## 6. Case 2 — 009830 한화솔루션

```yaml
case_id: C17_R4L97_009830_2024_02_01
symbol: "009830"
name: "한화솔루션"
canonical_archetype_id: C17_CHEMICAL_COMMODITY_MARGIN_SPREAD
fine_archetype_id: CHLOR_ALKALI_POTASH_SOLAR_CHEM_POLYPROPYLENE_FEEDSTOCK_SPREAD_MARGIN_BRIDGE_VS_COMMODITY_CHEMICAL_LABEL_SPIKE
trigger_date: 2024-02-01
entry_date: 2024-02-01
entry_price_basis: close
entry_price: 35000
classification: hard_4c_candidate_solar_chemical_spread_label_without_margin_survival
calibration_usable: true
```

### Evidence interpretation

한화솔루션 is the solar-chemical / commodity-spread hard guardrail.

The label can fool the model:

```text
chemical platform
solar chemical / clean-energy downstream exposure
feedstock relief or spread recovery hope
large-cap quality label
```

But from the selected February trigger, the forward path produced only a shallow MFE and then a large drawdown. The bridge from chemical / solar spread label to realized margin, inventory discipline, end-market demand, and working-capital survival failed.

### Price path

Key Stock-Web rows:

```text
2024-02-01: high 35,000 / close 35,000
2024-02-02: high 35,850 / close 34,700
2024-02-22: low 28,900 / close 29,300
2024-04-17: low 24,100 / close 24,100
2024-08-05: low 22,150 / close 22,950
2024-10-23: low 20,000 / close 20,550
2024-10-25: low 20,400 / close 20,450
```

Approximate path from entry close:

```text
entry_close: 35,000
peak_high_after_entry: 35,850
MFE: +2.4%
worst_low_after_entry: 20,000
MAE: -42.9%
```

### Interpretation

This is a hard C17 false-positive:

```text
Stage2-Watch: possible from chemical / solar value-chain relevance.
Stage2-Actionable: blocked unless product spread, demand, inventory, and margin bridge are explicit.
Stage3-Green: blocked.
Hard 4C: yes by shallow MFE and high MAE.
Cross-theme caveat: yes, solar / clean-energy label may be separate from commodity-chemical margin.
```

The lesson is that clean-energy chemical exposure is not spread-margin survival.

### Stress-test components

```text
raw_component_score_proxy:
  solar_chemical_label: high
  commodity_spread_signal: medium
  demand_inventory_bridge: weak
  working_capital_margin_bridge: weak
  price_confirmation_after_entry: failed
  drawdown_penalty: high
  hard_4c_guard: yes
```

---

## 7. Case 3 — 298000 효성화학

```yaml
case_id: C17_R4L97_298000_2024_02_01
symbol: "298000"
name: "효성화학"
canonical_archetype_id: C17_CHEMICAL_COMMODITY_MARGIN_SPREAD
fine_archetype_id: CHLOR_ALKALI_POTASH_SOLAR_CHEM_POLYPROPYLENE_FEEDSTOCK_SPREAD_MARGIN_BRIDGE_VS_COMMODITY_CHEMICAL_LABEL_SPIKE
trigger_date: 2024-02-01
entry_date: 2024-02-01
entry_price_basis: close
entry_price: 71300
classification: local_burst_polypropylene_commodity_chemical_spread_label_high_mae_4b_failure_with_balance_sheet_trust_caveat
calibration_usable: true
```

### Evidence interpretation

효성화학 is the commodity-chemical local-burst / high-MAE failure.

The setup had real C17 relevance:

```text
polypropylene / commodity chemical spread
feedstock and product-spread optionality
chemical-cycle rebound hope
```

The stock produced a modest but non-zero MFE into February, so the original setup is not simply zero response. But the later path failed severely as spread, demand, working-capital, and balance-sheet trust failed to support price survival. This is a 4B failure with a trust cap, not Green.

### Price path

Key Stock-Web rows:

```text
2024-02-01: high 71,600 / close 71,300
2024-02-19: high 79,900 / close 74,000
2024-03-19: low 60,800 / close 61,600
2024-04-17: low 55,200 / close 57,400
2024-08-05: low 40,200 / close 41,600
2024-10-25: low 39,500 / close 39,550
2024-11-27: low 28,150 / close 28,500
```

Approximate path from entry close:

```text
entry_close: 71,300
peak_high: 79,900
MFE: +12.1%
worst_low_after_entry: 28,150
MAE: -60.5%
```

### Interpretation

This is a C17 local burst / high-MAE 4B failure with trust cap:

```text
Stage2-Watch: possible from polypropylene / commodity-chemical spread relevance.
Stage2-Actionable: blocked unless feedstock spread, utilization, product demand, working-capital, and balance-sheet bridge are explicit.
Stage3-Green: blocked after severe high-MAE reversal.
Local 4B: required.
Hard 4C: secondary candidate if the scoring engine requires stricter balance-sheet trust routing.
Balance-sheet / tradeability caveat: yes.
```

### Stress-test components

```text
raw_component_score_proxy:
  polypropylene_commodity_relevance: high
  spread_recovery_signal: medium
  product_demand_bridge: weak
  feedstock_cost_bridge: weak_to_medium
  working_capital_bridge: weak
  balance_sheet_trust: weak
  price_confirmation: modest_initial
  drawdown_penalty: extreme
  local_4b_overlay: required
```

---

## 8. Aggregate calibration takeaways

```text
positive_case_count: 1
counterexample_count: 2
watch_or_cap_case_count: 2
local_4b_overlay_case_count: 1
hard_4c_candidate_count: 1
chlor_alkali_potash_case_count: 1
solar_chemical_spread_case_count: 1
polypropylene_commodity_chemical_case_count: 1
commodity_spread_margin_bridge_missing_count: 2
balance_sheet_or_tradeability_caveat_count: 1
row_presence_caveat_count: 2
calibration_usable_trigger_count: 3
```

The three-case C17 chemical spread grid:

```text
014830 유니드:
  chlor-alkali / potassium chemical spread positive;
  large MFE and non-hard MAE, but Green requires fresh spread and margin evidence.

009830 한화솔루션:
  chemical / solar spread label failed;
  shallow MFE and high MAE, hard 4C.

298000 효성화학:
  polypropylene / commodity chemical local burst failed;
  modest MFE first, then extreme MAE, local 4B with balance-sheet trust cap.
```

Shared rule:

```text
C17 is not "chemical label is cheap or cyclically relevant."
C17 is "product spread, feedstock cost, inventory timing, utilization, working capital, balance-sheet trust, and OP margin are visible for this company."
```

---

## 9. Machine-readable JSONL rows

```jsonl
{"row_type":"case","case_id":"C17_R4L97_014830_2024_02_01","scheduled_round":"R4","scheduled_loop":97,"large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD","fine_archetype_id":"CHLOR_ALKALI_POTASH_SOLAR_CHEM_POLYPROPYLENE_FEEDSTOCK_SPREAD_MARGIN_BRIDGE_VS_COMMODITY_CHEMICAL_LABEL_SPIKE","symbol":"014830","name":"유니드","trigger_date":"2024-02-01","entry_date":"2024-02-01","entry_price":76500,"peak_high":109500,"peak_date":"2024-05-09","worst_low_after_entry":65000,"worst_low_after_entry_date":"2024-10-25","mfe_pct":43.1,"mae_pct":-15.0,"classification":"positive_chlor_alkali_potash_spread_price_confirmation_with_green_cap_and_4b_watch","calibration_usable":true,"evidence_family":"chlor_alkali_potash_product_spread_export_demand_feedstock_energy_cost_margin_bridge","residual_error":"positive_chemical_spread_path_requires_green_cap_after_large_mfe_without_refreshed_spread_margin_evidence","shadow_rule_candidate":"allow_capped_actionable_when_product_spread_and_margin_bridge_confirm_but_cap_green_after_large_mfe"}
{"row_type":"case","case_id":"C17_R4L97_009830_2024_02_01","scheduled_round":"R4","scheduled_loop":97,"large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD","fine_archetype_id":"CHLOR_ALKALI_POTASH_SOLAR_CHEM_POLYPROPYLENE_FEEDSTOCK_SPREAD_MARGIN_BRIDGE_VS_COMMODITY_CHEMICAL_LABEL_SPIKE","symbol":"009830","name":"한화솔루션","trigger_date":"2024-02-01","entry_date":"2024-02-01","entry_price":35000,"peak_high":35850,"peak_date":"2024-02-02","worst_low_after_entry":20000,"worst_low_after_entry_date":"2024-10-23","mfe_pct":2.4,"mae_pct":-42.9,"classification":"hard_4c_candidate_solar_chemical_spread_label_without_margin_survival","calibration_usable":true,"row_presence_or_old_raw_caveat":true,"evidence_family":"solar_chemical_commodity_spread_label_without_inventory_demand_working_capital_margin_bridge","residual_error":"solar_chemical_label_can_fail_when_spread_and_margin_bridge_missing","shadow_rule_candidate":"route_solar_chemical_spread_label_to_hard_4c_if_mfe_shallow_mae_large_and_margin_bridge_missing"}
{"row_type":"case","case_id":"C17_R4L97_298000_2024_02_01","scheduled_round":"R4","scheduled_loop":97,"large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD","fine_archetype_id":"CHLOR_ALKALI_POTASH_SOLAR_CHEM_POLYPROPYLENE_FEEDSTOCK_SPREAD_MARGIN_BRIDGE_VS_COMMODITY_CHEMICAL_LABEL_SPIKE","symbol":"298000","name":"효성화학","trigger_date":"2024-02-01","entry_date":"2024-02-01","entry_price":71300,"peak_high":79900,"peak_date":"2024-02-19","worst_low_after_entry":28150,"worst_low_after_entry_date":"2024-11-27","mfe_pct":12.1,"mae_pct":-60.5,"classification":"local_burst_polypropylene_commodity_chemical_spread_label_high_mae_4b_failure_with_balance_sheet_trust_caveat","calibration_usable":true,"balance_sheet_or_tradeability_caveat":true,"evidence_family":"polypropylene_commodity_chemical_spread_label_without_demand_working_capital_balance_sheet_margin_survival","residual_error":"commodity_chemical_spread_label_can_create_modest_mfe_but_fail_green_when_balance_sheet_and_margin_bridge_break","shadow_rule_candidate":"classify_modest_mfe_then_extreme_mae_commodity_chemical_cases_as_local_4b_with_balance_sheet_trust_cap"}
```

```jsonl
{"row_type":"aggregate","scheduled_round":"R4","scheduled_loop":97,"large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD","fine_archetype_id":"CHLOR_ALKALI_POTASH_SOLAR_CHEM_POLYPROPYLENE_FEEDSTOCK_SPREAD_MARGIN_BRIDGE_VS_COMMODITY_CHEMICAL_LABEL_SPIKE","case_count":3,"positive_case_count":1,"counterexample_count":2,"watch_or_cap_case_count":2,"local_4b_overlay_case_count":1,"hard_4c_candidate_count":1,"chlor_alkali_potash_case_count":1,"solar_chemical_spread_case_count":1,"polypropylene_commodity_chemical_case_count":1,"commodity_spread_margin_bridge_missing_count":2,"balance_sheet_or_tradeability_caveat_count":1,"row_presence_caveat_count":2,"calibration_usable_trigger_count":3,"loop_contribution_label":"residual_error_found","do_not_propose_new_weight_delta":true}
{"row_type":"shadow_rule","scheduled_round":"R4","scheduled_loop":97,"canonical_archetype_id":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD","rule_id":"C17_PRODUCT_SPREAD_FEEDSTOCK_INVENTORY_MARGIN_TRUST_BRIDGE_REQUIRED","rule_type":"canonical_archetype_specific_guard","rule_text":"For C17 chemical commodity margin-spread cases, do not open Stage2-Actionable or Stage3-Green from chemical commodity, chlor-alkali, caustic, potash, PVC, polyolefin, polypropylene, solar chemical, polysilicon/downstream clean-energy, feedstock relief, one-week chemical-stock spike, or low-PBR/restructuring labels alone. Require named product and feedstock exposure, input price and output selling-price direction, inventory and working-capital timing, end-market/export demand, utilization and plant reliability, FX/freight/energy-cost control, margin/OP conversion, balance-sheet and refinancing trust where relevant, and post-trigger price survival. Chemical-spread positives with large MFE may be capped Actionable when product spread and margin bridge are explicit, but Green requires fresh evidence. Solar-chemical labels with shallow MFE and high MAE should route to hard-4C when margin bridge is missing. Commodity-chemical names with modest MFE followed by extreme MAE should remain local 4B with balance-sheet trust cap.","expected_effect":"Preserve true chemical spread positives while reducing commodity-chemical, solar-chemical, and balance-sheet-stressed spread false positives.","production_scoring_changed":false,"shadow_weight_only":true}
{"row_type":"residual_contribution","scheduled_round":"R4","scheduled_loop":97,"canonical_archetype_id":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD","residual_type":"product_spread_feedstock_inventory_margin_trust_guard","contribution":"Adds one chlor-alkali/potash positive, one solar-chemical hard-4C, and one polypropylene commodity-chemical local 4B failure to calibrate C17 product spread, feedstock, inventory, working-capital, balance-sheet trust, and margin requirements.","do_not_count_as_global_weight_delta":true}
```

---

## 10. Proposed canonical-archetype shadow rule

```text
C17_PRODUCT_SPREAD_FEEDSTOCK_INVENTORY_MARGIN_TRUST_BRIDGE_REQUIRED

IF canonical_archetype_id == C17_CHEMICAL_COMMODITY_MARGIN_SPREAD:

  Do not open Stage3-Green from:
    - chemical commodity label alone
    - chlor-alkali / caustic / potash label alone
    - PVC / polyolefin / polypropylene label alone
    - solar chemical / polysilicon / downstream clean-energy label alone
    - feedstock price relief headline alone
    - one-week chemical-stock volume spike alone
    - low-PBR or restructuring hope alone

  Require at least two of:
    - named product and feedstock exposure
    - input price and output selling-price direction
    - inventory / working-capital timing
    - end-market and export demand
    - utilization and plant reliability
    - FX / freight / energy-cost containment
    - margin / OP conversion
    - balance-sheet and refinancing trust where relevant
    - low-MAE post-trigger price survival
    - fresh evidence after the chemical-spread headline

  If MFE < 8% and MAE < -35%:
    route to C17 hard-4C candidate.

  If MFE > 10% but later MAE is extreme:
    preserve as local 4B / event burst, not Green, unless product-spread and balance-sheet evidence refreshes.

  If balance-sheet or tradeability caveat exists:
    apply trust cap even when a short MFE appears.

  Distinguish:
    - names where product spread becomes operating margin
    - from chemical labels where demand, inventory, working capital, or refinancing breaks the bridge.
```

---

## 11. Deferred Coding Agent Handoff Prompt

```text
You are a coding agent working on Songdaiki/stock_agent.

Do not treat this research MD as production scoring by itself.
Batch it with other v12 residual research files.

Source file:
e2r_stock_web_v12_residual_round_R4_loop_97_L4_MATERIALS_SPREAD_RESOURCE_C17_CHEMICAL_COMMODITY_MARGIN_SPREAD_research.md

Task:
1. Parse machine-readable JSONL rows.
2. Add the three C17 chemical commodity margin-spread cases to calibration research ingestion.
3. Preserve production_scoring_changed=false.
4. Treat the proposed rule only as a shadow canonical-archetype guard candidate:
   C17_PRODUCT_SPREAD_FEEDSTOCK_INVENTORY_MARGIN_TRUST_BRIDGE_REQUIRED.
5. Do not change global weights directly.
6. Compare against existing C17 cases and deduplicate by:
   canonical_archetype_id + symbol + trigger_type + entry_date.
7. If enough C17 cases agree, consider implementing a canonical guard that:
   - blocks chemical-label Green without product/feedstock spread, inventory, demand, utilization, and margin bridge,
   - preserves chlor-alkali/potash positives only with price survival and fresh spread evidence,
   - routes shallow-MFE/high-MAE solar-chemical labels to hard-4C,
   - treats modest-MFE/extreme-MAE commodity-chemical names as local 4B with balance-sheet trust cap,
   - applies row-presence and refinancing/tradeability caveats.

Expected next schedule:
completed_round = R4
completed_loop = 97
next_round = R5
next_loop = 97
round_schedule_status = valid
round_sector_consistency = pass
```

---

## 12. Required round-state footer

```text
completed_round = R4
completed_loop = 97
next_round = R5
next_loop = 97
round_schedule_status = valid
round_sector_consistency = pass
```
