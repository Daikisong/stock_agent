# E2R v12 Residual Calibration Research
## R4 / Loop 110 / L4_MATERIALS_SPREAD_RESOURCE / C16_STRATEGIC_RESOURCE_POLICY_SUPPLY

```yaml
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
research_session: post_calibrated_sector_archetype_residual_research
selected_round: R4
selected_loop: 110
large_sector_id: L4_MATERIALS_SPREAD_RESOURCE
canonical_archetype_id: C16_STRATEGIC_RESOURCE_POLICY_SUPPLY
fine_archetype_id: BATTERY_CATHODE_PRECURSOR_SUPPLY_CONTRACT_AND_POLICY_LOCALIZATION_BRIDGE_VS_EV_DEMAND_REVISION_AND_IPO_THEME_BLOWOFF
output_format: one_standalone_markdown_file
stock_agent_code_access_allowed: false
stock_agent_code_patch_allowed: false
production_scoring_changed: false
shadow_weight_only: true
stock_web_price_atlas_access_required: true
```

## 1. Execution guardrail

This run is not a live scan, not a current recommendation run, not a broker/API run, and not a production scoring patch.
The only purpose is to create a standalone historical calibration Markdown file for later batch ingestion.

This run used `Songdaiki/stock-web` as the price atlas and only used `stock_agent` research artifacts for coverage-gap and duplicate-avoidance context.

## 2. Coverage and duplicate-avoidance basis

`C16_STRATEGIC_RESOURCE_POLICY_SUPPLY` remains a Priority 1 coverage-gap archetype in the v12 no-repeat index.
The index shows C16 at 30 rows, needing 20 more rows to reach the 50-row practical calibration target.

Already-used C16 cases were avoided:
- POSCO Holdings
- LS
- Kumyang
- POSCO International
- SungEel HiTech
- Cosmo Chemical
- STX blocked comparator
- POSCO Future M
- LG Chem
- Daejoo Electronic Materials

This run uses new symbols/cases:
- L&F / 066970
- EcoPro BM / 247540
- EcoPro Materials / 450080

## 3. Price atlas source

Price rows were read from:

```text
repo: Songdaiki/stock-web
root: atlas/ohlcv_tradable_by_symbol_year
basis: tradable_raw / raw_unadjusted_marcap
source: FinanceData/marcap
```

Manifest caveats applied:
- raw/unadjusted OHLC;
- corporate-action-contaminated windows are blocked by default;
- zero-volume and zero-OHLC rows are excluded from calibration shards.

## 4. Research question

C16 is supposed to capture strategic resource policy and supply-chain execution.

The residual error here is that “battery material localization” can look like a real strategic-resource bridge even when equity value is actually driven by:
1. contract volume uncertainty;
2. EV demand revision;
3. customer program slippage;
4. commodity-price pass-through failure;
5. IPO/liquidity/speculation blowoff rather than durable offtake/margin conversion.

The profile should not simply reward the words “cathode,” “precursor,” “nickel,” “Ford,” “Tesla,” “Canada,” or “localization.”
It should require a route from policy/resource label to actual contract volume, utilization, margin, and cash conversion.

---

# 5. Case table

| case_id | symbol | company | trigger_date | entry_date | entry_price | peak_date | peak_high | trough_date | trough_low | MFE | MAE | classification |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| C16_R4L110_001 | 066970 | 엘앤에프 | 2023-02-28 | 2023-02-28 | 262,000 | 2023-04-03 | 349,500 | 2023-11-01 | 127,900 | +33.40% | -51.18% | counterexample |
| C16_R4L110_002 | 247540 | 에코프로비엠 | 2023-08-23 | 2023-08-23 | 321,000 | 2023-12-04 | 354,000 | 2023-11-01 | 187,600 | +10.28% | -41.56% | counterexample |
| C16_R4L110_003 | 450080 | 에코프로머티 | 2023-11-17 | 2023-11-17 | 57,200 | 2024-01-11 | 244,000 | 2023-11-17 | 42,950 | +326.57% | -24.91% | positive_4B_watch |

---

# 6. Case narratives

## 6.1 L&F — Tesla high-nickel cathode supply deal that later collapsed

### Trigger

L&F signed a 2023 high-nickel cathode materials supply deal with Tesla and affiliates for the 2024-2025 period.
This initially looked like a clean strategic battery-material supply bridge: a named global customer, cathode material, and a high-value supply narrative.

However, Reuters later reported that the projected value of the deal was reduced from about $2.9 billion to only $7,386, with analysts citing Tesla 4680 production-yield problems and EV demand slowdown. That later evidence makes this an unusually clear C16 contract-volume revision counterexample.

### Price row confirmation

`066970` profile:
- current/latest name: 엘앤에프;
- market history includes KOSDAQ, KOSDAQ GLOBAL, and KOSPI;
- corporate-action candidate dates are 2016-02-19 and 2021-08-11, outside this 2023 route.

Entry and route:
- 2023-02-28 close: 262,000
- 2023-04-03 high: 349,500
- 2023-11-01 low: 127,900

### Calculation

```text
entry_price = 262,000
peak_high = 349,500
trough_low = 127,900

MFE = (349,500 - 262,000) / 262,000 = +33.40%
MAE = (127,900 - 262,000) / 262,000 = -51.18%
```

### Calibration interpretation

This is a hard C16 counterexample.
A named supply deal is not enough when:
- customer program execution is uncertain;
- the supply deal is tied to a specific battery format or platform ramp;
- contracted headline value can be revised down;
- equity route is exposed to EV demand and commodity-cycle repricing.

For C16, large contract headline should be discounted unless the model can see:
- take-or-pay or firm minimum volume;
- customer ramp visibility;
- utilization conversion;
- margin/revenue recognition timing;
- sensitivity to EV demand revision.

---

## 6.2 EcoPro BM — Ford/SK On/EcoPro Canada cathode localization bridge with weak equity conversion

### Trigger

The SK On / Ford / EcoPro BM Canada cathode-material localization story is C16-relevant because it connects North American battery supply-chain localization, cathode material production, and non-China supply-chain positioning.

But the equity route did not behave like a clean strategic-resource supply positive.
The event family looked strong at the policy level, yet the stock path rapidly exposed the difference between “localization label” and actual near-term margin/volume conversion.

### Price row confirmation

`247540` profile:
- current/latest name: 에코프로비엠;
- no corporate-action candidate in 2023 route;
- corporate-action candidates exist in 2022, so 2023 rows are usable under the caveat.

Entry and route:
- 2023-08-23 close: 321,000
- 2023-12-04 high: 354,000
- 2023-11-01 low: 187,600

### Calculation

```text
entry_price = 321,000
peak_high = 354,000
trough_low = 187,600

MFE = (354,000 - 321,000) / 321,000 = +10.28%
MAE = (187,600 - 321,000) / 321,000 = -41.56%
```

### Calibration interpretation

This is another C16 counterexample.
The strategic localization narrative was real enough to enter the archetype, but the price route says that localization did not protect the equity path from battery-sector de-rating.

The profile should distinguish:

```text
policy-localized plant / JV announcement
    != immediate company-level margin conversion
```

A JV/localization headline should not receive full C16 weight unless there is:
- near-term volume allocation;
- confirmed customer demand;
- funding/capex clarity;
- ramp timing;
- operating-margin bridge;
- no major EV-cycle negative revision.

---

## 6.3 EcoPro Materials — cathode precursor / nickel-cobalt refining IPO blowoff, positive route but not clean Green

### Trigger

EcoPro Materials is a C16-relevant company because it produces high-nickel precursors, participates in nickel/cobalt refining, and is part of the EcoPro battery-materials vertical chain.
The 2023 IPO created a powerful strategic-resource localization equity route.

However, this is not a clean offtake-trigger case.
The route is heavily contaminated by IPO scarcity, index/liquidity demand, retail speculation, and battery-material theme compression/expansion.

### Price row confirmation

`450080` profile:
- current/latest name: 에코프로머티;
- first_date: 2023-11-17;
- no corporate-action candidate in the profile.

Entry and route:
- 2023-11-17 close: 57,200
- 2024-01-11 high: 244,000
- 2023-11-17 low: 42,950

### Calculation

```text
entry_price = 57,200
peak_high = 244,000
trough_low = 42,950

MFE = (244,000 - 57,200) / 57,200 = +326.57%
MAE = (42,950 - 57,200) / 57,200 = -24.91%
```

### Calibration interpretation

This is a positive route but not a Green-quality C16 example.
It proves that the market can aggressively price strategic precursor/localization scarcity, but the trigger is not an offtake/margin bridge. It is an IPO blowoff route with strong 4B risk.

The right treatment:

```text
precursor/refining/localization + IPO scarcity = 4B watch, not direct Stage3-Green
```

To upgrade this type of case, the profile should require:
- customer/offtake evidence;
- utilization ramp evidence;
- gross-margin conversion;
- commodity-price sensitivity check;
- post-IPO liquidity/fade check.

---

# 7. Residual error observed

The remaining C16 residual error is not “missed battery materials.”
The issue is that the model still risks treating battery-material policy localization as if it were already cash conversion.

Wrong model:

```text
critical mineral / cathode / precursor / localization headline
  -> strategic resource positive
```

Better model:

```text
strategic resource label
  -> check contract firmness
  -> check customer ramp
  -> check utilization and margin
  -> check commodity/EV demand revision
  -> only then assign Stage2/Stage3 weight
```

## 8. Shadow rule candidate

```yaml
shadow_rule_id: c16_battery_material_contract_volume_ramp_margin_bridge_required_v2
scope:
  large_sector_id: L4_MATERIALS_SPREAD_RESOURCE
  canonical_archetype_id: C16_STRATEGIC_RESOURCE_POLICY_SUPPLY

positive_boost_conditions:
  - firm_customer_or_offtake_volume == true
  - ramp_schedule_visible == true
  - utilization_conversion_visible == true
  - margin_or_earnings_revision_bridge == true
  - commodity_price_or_ev_demand_risk_not_dominant == true
  - no_corporate_action_contamination == true

watch_conditions:
  - policy_localization_label_only == true
  - IPO_or_liquidity_theme_contamination == true
  - customer_program_ramp_uncertain == true

penalty_or_cap_conditions:
  - contract_value_revision_risk == true
  - customer_program_delay_or_demand_slowdown == true
  - high_MFE_high_MAE_blowoff == true
  - no_near_term_cash_conversion == true

stage_cap:
  localization_label_only: Stage2_watch
  IPO_theme_blowoff: Stage2_watch_or_4B
  firm_offtake_with_margin_bridge: allow_Stage3_Yellow_if_route_quality_confirmed
```

---

# 9. Machine-readable rows

```jsonl
{"row_type":"case","case_id":"C16_R4L110_001","round":"R4","loop":110,"large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C16_STRATEGIC_RESOURCE_POLICY_SUPPLY","fine_archetype_id":"BATTERY_CATHODE_PRECURSOR_SUPPLY_CONTRACT_AND_POLICY_LOCALIZATION_BRIDGE_VS_EV_DEMAND_REVISION_AND_IPO_THEME_BLOWOFF","symbol":"066970","company":"엘앤에프","trigger_date":"2023-02-28","entry_date":"2023-02-28","entry_price":262000,"peak_date":"2023-04-03","peak_high":349500,"trough_date":"2023-11-01","trough_low":127900,"mfe_pct":33.40,"mae_pct":-51.18,"classification":"counterexample","evidence_family":"tesla_high_nickel_cathode_supply_deal_later_value_revision","corporate_action_blocked":false}
{"row_type":"case","case_id":"C16_R4L110_002","round":"R4","loop":110,"large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C16_STRATEGIC_RESOURCE_POLICY_SUPPLY","fine_archetype_id":"BATTERY_CATHODE_PRECURSOR_SUPPLY_CONTRACT_AND_POLICY_LOCALIZATION_BRIDGE_VS_EV_DEMAND_REVISION_AND_IPO_THEME_BLOWOFF","symbol":"247540","company":"에코프로비엠","trigger_date":"2023-08-23","entry_date":"2023-08-23","entry_price":321000,"peak_date":"2023-12-04","peak_high":354000,"trough_date":"2023-11-01","trough_low":187600,"mfe_pct":10.28,"mae_pct":-41.56,"classification":"counterexample","evidence_family":"cathode_localization_jv_label_without_near_term_margin_conversion","corporate_action_blocked":false}
{"row_type":"case","case_id":"C16_R4L110_003","round":"R4","loop":110,"large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C16_STRATEGIC_RESOURCE_POLICY_SUPPLY","fine_archetype_id":"BATTERY_CATHODE_PRECURSOR_SUPPLY_CONTRACT_AND_POLICY_LOCALIZATION_BRIDGE_VS_EV_DEMAND_REVISION_AND_IPO_THEME_BLOWOFF","symbol":"450080","company":"에코프로머티","trigger_date":"2023-11-17","entry_date":"2023-11-17","entry_price":57200,"peak_date":"2024-01-11","peak_high":244000,"trough_date":"2023-11-17","trough_low":42950,"mfe_pct":326.57,"mae_pct":-24.91,"classification":"positive_4B_watch","evidence_family":"cathode_precursor_nickel_cobalt_refining_ipo_theme","corporate_action_blocked":false}
{"row_type":"shadow_weight","shadow_rule_id":"c16_battery_material_contract_volume_ramp_margin_bridge_required_v2","canonical_archetype_id":"C16_STRATEGIC_RESOURCE_POLICY_SUPPLY","firm_offtake_margin_bridge_boost":true,"localization_label_cap":true,"contract_value_revision_penalty":true,"ipo_blowoff_4b_watch":true,"production_scoring_changed":false}
{"row_type":"aggregate","round":"R4","loop":110,"canonical_archetype_id":"C16_STRATEGIC_RESOURCE_POLICY_SUPPLY","new_independent_case_count":3,"positive_case_count":1,"counterexample_count":2,"current_profile_error_count":3,"verified_url_repair_needed_count":1}
```

---

# 10. Deferred Coding Agent Handoff Prompt

Do not execute this in the current research session.

```text
You are the coding agent for Songdaiki/stock_agent.

Input: this standalone residual calibration Markdown.

Task:
1. Parse the machine-readable rows.
2. Add the cases to the v12 calibration registry if not already present.
3. Add the shadow rule candidate only as a pending candidate, not production scoring.
4. Do not change production scoring unless a later batch calibration step explicitly approves it.
5. Preserve the distinction:
   - firm offtake / supply volume / margin conversion;
   - localization or JV policy label;
   - IPO/liquidity/speculation blowoff;
   - customer-program or EV-demand revision.
6. Respect no-repeat key:
   canonical_archetype_id + symbol + trigger_type + entry_date.
```

---

# 11. Final run summary

```yaml
selected_round: R4
selected_loop: 110
selection_basis: docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket: Priority 1
round_schedule_status: coverage_index_selected
round_sector_consistency: pass
large_sector_id: L4_MATERIALS_SPREAD_RESOURCE
canonical_archetype_id: C16_STRATEGIC_RESOURCE_POLICY_SUPPLY
fine_archetype_id: BATTERY_CATHODE_PRECURSOR_SUPPLY_CONTRACT_AND_POLICY_LOCALIZATION_BRIDGE_VS_EV_DEMAND_REVISION_AND_IPO_THEME_BLOWOFF

new_independent_case_count: 3
reused_case_count: 0
same_archetype_new_symbol_count: 3
same_archetype_new_trigger_family_count: 3
calibration_usable_case_count: 3
calibration_usable_trigger_count: 3
positive_case_count: 1
counterexample_count: 2
current_profile_error_count: 3
verified_url_repair_needed_count: 1

diversity_score_summary: C16 Priority 1 보강 + L&F Tesla high-nickel cathode deal later value-revision counterexample + EcoPro BM cathode localization JV weak equity conversion counterexample + EcoPro Materials precursor/refining IPO blowoff positive 4B watch
do_not_propose_new_weight_delta: false
auto_selected_coverage_gap: C16 rows 30, 50-row target까지 20 부족
sector_specific_rule_candidate: true
canonical_archetype_rule_candidate: true
loop_contribution_label: canonical_archetype_rule_candidate
new_axis_proposed: c16_battery_material_contract_volume_ramp_margin_bridge_required_v2
existing_axis_strengthened: full_4b_requires_non_price_evidence scoped to C16 battery-material/localization/precursor rallies
existing_axis_weakened: null
next_recommended_archetypes:
  - C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY
  - C05_EPC_MEGA_CONTRACT_MARGIN_GAP
  - C15_MATERIAL_SPREAD_SUPERCYCLE
```
