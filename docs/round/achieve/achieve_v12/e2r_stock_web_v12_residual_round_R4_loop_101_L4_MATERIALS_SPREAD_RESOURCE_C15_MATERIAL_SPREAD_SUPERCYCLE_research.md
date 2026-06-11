# E2R stock-web v12 residual research — R4 / Loop 101 / C15 material spread supercycle

```text
schema_family = v12_sector_archetype_residual
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
research_session = post_calibrated_sector_archetype_residual_research
selected_round = R4
selected_loop = 101
large_sector_id = L4_MATERIALS_SPREAD_RESOURCE
canonical_archetype_id = C15_MATERIAL_SPREAD_SUPERCYCLE
fine_archetype_id = COPPER_PRICE_SPREAD_COMPANY_MARGIN_BRIDGE_VS_COPPER_BETA_PRICE_ONLY_FALSE_STAGE2
selection_basis = docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket = Priority 0
round_schedule_status = coverage_index_selected
round_sector_consistency = pass
price_source = Songdaiki/stock-web
price_basis = tradable_raw
price_adjustment_status = raw_unadjusted_marcap
stock_web_manifest_max_date = 2026-02-20
production_scoring_changed = false
shadow_weight_only = true
```

## 1. Selection and novelty check

`V12_Research_No_Repeat_Index.md` marks `C15_MATERIAL_SPREAD_SUPERCYCLE` as a Priority 0 under-covered canonical archetype with 6 rows and need-to-30 of 24. In this conversation-local run sequence, the previously generated local artifacts already covered C18, C26, C29, C30, C31, C32 and then C04, so this pass moves to the next under-covered canonical.

Existing registry has a prior `R4 / loop 100 / C15_MATERIAL_SPREAD_SUPERCYCLE` file. The selected loop therefore follows the v12 rule:

```text
selected_loop = max(existing loop for selected_round and selected_canonical_archetype_id) + 1
selected_loop = 100 + 1 = 101
```

Novelty policy:

```text
same canonical repeat = allowed
same symbol + trigger_type + entry_date repeat = avoided
known C15 covered symbols = 001390, 001550, 005490, 009520, 025860, 103140
new symbols in this file = 025820, 012800
reused symbol with new trigger family = 103140
```

This file deliberately separates two things that often look identical on a chart:

1. **real material spread bridge**: commodity price / ASP / volume / inventory / margin moves together;
2. **commodity-beta price-only spike**: copper/lithium/steel label moves first, but the company never proves pass-through or margin conversion.

The C15 mechanism is not “copper up, stock up.” It is more like a refinery gate: the raw material price is only the incoming pressure; the investable signal appears only if the company can turn that pressure into saleable spread, working-capital control, and durable earnings revision.

## 2. External non-price context

Global copper entered a strong rally in 2024. Reuters later referenced the May 2024 all-time high near USD 11,104.50/t when discussing the next copper move to USD 11,000/t. That supports the commodity backdrop, but it is not enough for a Green unlock by itself.

Poongsan is directly tied to non-ferrous metalworking and copper alloy products, while also having defense ammunition exposure. The positive case below uses that company-specific bridge. By contrast, IGOO/Daechang-type copper processors can show sharp stock beta to copper headlines while still failing the pass-through / margin / inventory-turn test.

Reference URLs used in the research narrative:

```text
https://www.reuters.com/business/lme-copper-hits-11000-ton-first-time-since-may-2024-2025-10-09/
https://en.wikipedia.org/wiki/Poongsan_Corporation
https://github.com/Songdaiki/stock-web/blob/main/atlas/manifest.json
```

## 3. Price source validation

```text
stock_web_repo = Songdaiki/stock-web
manifest_path = atlas/manifest.json
calibration_shard_root = atlas/ohlcv_tradable_by_symbol_year
research_pack_default_price_basis = tradable_raw
price_adjustment_status = raw_unadjusted_marcap
max_date = 2026-02-20
```

Symbol validation:

| symbol | name | profile path | tradable rows | corporate-action caveat | validation |
|---|---|---|---:|---|---|
| 103140 | 풍산 | atlas/symbol_profiles/103/103140.json | 4,331 | none | pass |
| 025820 | 이구산업 | atlas/symbol_profiles/025/025820.json | 7,558 | old CA windows only, not in 2024 window | pass |
| 012800 | 대창 | atlas/symbol_profiles/012/012800.json | 7,755 | old CA windows only, not in 2024 window | pass |

## 4. Case table

| case | symbol | name | role | trigger type | trigger/entry date | entry price | 30D MFE/MAE | 90D MFE/MAE | 180D MFE/MAE | interpretation |
|---:|---|---|---|---|---|---:|---:|---:|---:|---|
| 1 | 103140 | 풍산 | positive | Stage2-Actionable | 2024-03-07 | 46,100 | +46.42% / -3.90% | +71.15% / -3.90% | +71.15% / -3.90% | copper/alloy + defense bridge worked as Stage2-Actionable, but still requires 4B watch after vertical MFE |
| 2 | 025820 | 이구산업 | counterexample | Stage2 | 2024-04-15 | 6,570 | +28.16% / -11.42% | +28.16% / -42.24% | +28.16% / -46.04% | copper headline beta produced early MFE, then failed margin/bridge durability |
| 3 | 012800 | 대창 | counterexample | Stage2 | 2024-04-15 | 1,624 | +42.86% / -13.55% | +42.86% / -32.27% | +42.86% / -32.88% | brass/copper label spike failed durable spread conversion |

## 5. Case notes

### Case 1 — 103140 Poongsan: material spread bridge positive, but not unrestricted Green

Poongsan had a direct material-processing business bridge and an additional defense earnings channel. Entry is 2024-03-07 close 46,100. The 2024 copper rally backdrop helped, but the key distinction is that this was not a tiny copper-label proxy: its operating structure gives a plausible route from copper/alloy price and volume into realizable earnings.

Price path:

```text
entry = 2024-03-07 close 46,100
30D high = 67,500 on 2024-04-12
30D low = 44,300 on 2024-03-13
90D high = 78,900 on 2024-05-14
90D low = 44,300 on 2024-03-13
180D high = 78,900 on 2024-05-14
180D low = 44,300 on 2024-03-13
```

Interpretation:

```text
profile_result = current profile may under-credit if it blocks all commodity beta
guardrail = require company-specific ASP/volume/margin bridge before Stage2-Actionable
4B = after +70% MFE, local 4B watch is appropriate even if full 4B is not automatic
```

### Case 2 — 025820 IGOO: copper price spike without proof of margin bridge

IGOO moved like a copper-beta stock during the copper rally. Entry is 2024-04-15 close 6,570 after a violent move. It reached 8,420 on 2024-05-20, but the later path fell below 3,800 and then 3,545 by December. That shape is the classic C15 trap: the chart wears the copper crown for a few weeks, then the crown becomes inventory risk.

Price path:

```text
entry = 2024-04-15 close 6,570
30D high = 8,420 on 2024-05-20
30D low = 5,820 on 2024-04-17
90D high = 8,420 on 2024-05-20
90D low = 3,795 on 2024-08-05
180D high = 8,420 on 2024-05-20
180D low = 3,545 on 2024-12-09
```

Interpretation:

```text
profile_result = false positive if copper-label information score overrides missing margin bridge
guardrail = copper price + stock move must not become Stage2-Actionable without evidence of ASP pass-through / inventory gain / volume durability
4B = local 4B should trigger quickly after price-only MFE
```

### Case 3 — 012800 Daechang: brass/copper beta spike with weak durability

Daechang also reacted sharply to copper/brass enthusiasm. Entry is 2024-04-15 close 1,624. The move to 2,320 by 2024-05-21 was strong enough to look like a rerating, but the later low near 1,100 and 1,090 shows that the move was not protected by a durable company-specific spread bridge.

Price path:

```text
entry = 2024-04-15 close 1,624
30D high = 2,320 on 2024-05-21
30D low = 1,404 on 2024-04-25
90D high = 2,320 on 2024-05-21
90D low = 1,100 on 2024-08-05
180D high = 2,320 on 2024-05-21
180D low = 1,090 on 2024-11-15
```

Interpretation:

```text
profile_result = false positive if brass/copper vocabulary is scored as bottleneck visibility
guardrail = require realized spread/margin evidence, not just raw copper price or inventory mark-up speculation
4B = local 4B / watch should activate after early vertical MFE with no non-price bridge
```

## 6. Score-return alignment

| symbol | role | raw score | stage candidate | realized 90D MFE | realized 90D MAE | alignment |
|---|---|---:|---|---:|---:|---|
| 103140 | positive | 68 | Stage2-Actionable | +71.15% | -3.90% | aligned; bridge-backed material name deserved Stage2-Actionable |
| 025820 | counterexample | 38 | Stage1/Watch | +28.16% | -42.24% | current profile must avoid upgrading price-only copper beta |
| 012800 | counterexample | 34 | Stage1/Watch | +42.86% | -32.27% | early MFE was tradable, but not a durable C15 rerating |

## 7. Raw component score breakdown

C15 runtime component weights from the current index are:

```text
EPS/FCF = 20
Visibility = 12
Bottleneck = 20
Mispricing = 10
Valuation = 10
Capital = 8
Info = 20
```

```json
[
  {
    "symbol": "103140",
    "trigger_type": "Stage2-Actionable",
    "EPS_FCF_20": 15,
    "Visibility_12": 9,
    "Bottleneck_20": 14,
    "Mispricing_10": 7,
    "Valuation_10": 6,
    "Capital_8": 5,
    "Info_20": 12,
    "raw_total": 68,
    "stage_candidate": "Stage2-Actionable",
    "rule_note": "Positive but not Green unless copper spread/defense margin bridge is confirmed beyond price momentum."
  },
  {
    "symbol": "025820",
    "trigger_type": "Stage2",
    "EPS_FCF_20": 6,
    "Visibility_12": 4,
    "Bottleneck_20": 9,
    "Mispricing_10": 4,
    "Valuation_10": 4,
    "Capital_8": 2,
    "Info_20": 9,
    "raw_total": 38,
    "stage_candidate": "Stage1/Watch",
    "rule_note": "Copper price beta alone should not become Stage2-Actionable."
  },
  {
    "symbol": "012800",
    "trigger_type": "Stage2",
    "EPS_FCF_20": 5,
    "Visibility_12": 4,
    "Bottleneck_20": 8,
    "Mispricing_10": 4,
    "Valuation_10": 3,
    "Capital_8": 2,
    "Info_20": 8,
    "raw_total": 34,
    "stage_candidate": "Stage1/Watch",
    "rule_note": "Brass/copper input-cost exposure needs explicit pass-through and inventory-turn bridge."
  }
]
```

## 8. Trigger rows JSONL

```jsonl
{"schema_version":"v12_sector_archetype_residual","row_type":"trigger","selected_round":"R4","selected_loop":101,"large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C15_MATERIAL_SPREAD_SUPERCYCLE","fine_archetype_id":"COPPER_PRICE_SPREAD_COMPANY_MARGIN_BRIDGE_VS_COPPER_BETA_PRICE_ONLY_FALSE_STAGE2","symbol":"103140","name":"풍산","market":"KOSPI","trigger_type":"Stage2-Actionable","trigger_date":"2024-03-07","entry_date":"2024-03-07","entry_price":46100.0,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","MFE_30D_pct":46.42,"MAE_30D_pct":-3.9,"MFE_90D_pct":71.15,"MAE_90D_pct":-3.9,"MFE_180D_pct":71.15,"MAE_180D_pct":-3.9,"case_role":"positive","current_profile_verdict":"under_credit_if_material_spread_bridge_is_confirmed","evidence_family":"copper_price_strength_plus_company_specific_copper_alloy_and_defense_margin_bridge","calibration_usable":true,"dedupe_key":"103140|C15_MATERIAL_SPREAD_SUPERCYCLE|Stage2-Actionable|2024-03-07|2024-03-07|46100.0|copper_spread_margin_bridge"}
{"schema_version":"v12_sector_archetype_residual","row_type":"trigger","selected_round":"R4","selected_loop":101,"large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C15_MATERIAL_SPREAD_SUPERCYCLE","fine_archetype_id":"COPPER_PRICE_SPREAD_COMPANY_MARGIN_BRIDGE_VS_COPPER_BETA_PRICE_ONLY_FALSE_STAGE2","symbol":"025820","name":"이구산업","market":"KOSPI","trigger_type":"Stage2","trigger_date":"2024-04-15","entry_date":"2024-04-15","entry_price":6570.0,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","MFE_30D_pct":28.16,"MAE_30D_pct":-11.42,"MFE_90D_pct":28.16,"MAE_90D_pct":-42.24,"MFE_180D_pct":28.16,"MAE_180D_pct":-46.04,"case_role":"counterexample","current_profile_verdict":"false_positive_if_copper_price_beta_is_treated_as_margin_bridge","evidence_family":"copper_price_headline_without_verified_company_specific_margin_inventory_turn_bridge","calibration_usable":true,"dedupe_key":"025820|C15_MATERIAL_SPREAD_SUPERCYCLE|Stage2|2024-04-15|2024-04-15|6570.0|copper_beta_no_margin_bridge"}
{"schema_version":"v12_sector_archetype_residual","row_type":"trigger","selected_round":"R4","selected_loop":101,"large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C15_MATERIAL_SPREAD_SUPERCYCLE","fine_archetype_id":"COPPER_PRICE_SPREAD_COMPANY_MARGIN_BRIDGE_VS_COPPER_BETA_PRICE_ONLY_FALSE_STAGE2","symbol":"012800","name":"대창","market":"KOSPI","trigger_type":"Stage2","trigger_date":"2024-04-15","entry_date":"2024-04-15","entry_price":1624.0,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","MFE_30D_pct":42.86,"MAE_30D_pct":-13.55,"MFE_90D_pct":42.86,"MAE_90D_pct":-32.27,"MFE_180D_pct":42.86,"MAE_180D_pct":-32.88,"case_role":"counterexample","current_profile_verdict":"false_positive_if_brass_rod_copper_cost_pass_through_is_assumed_without_margin_bridge","evidence_family":"brass_copper_price_beta_without_verified_asp_volume_margin_bridge","calibration_usable":true,"dedupe_key":"012800|C15_MATERIAL_SPREAD_SUPERCYCLE|Stage2|2024-04-15|2024-04-15|1624.0|brass_copper_beta_no_margin_bridge"}
```

## 9. Aggregate metrics

```json
{
  "row_type": "aggregate_metric",
  "selected_round": "R4",
  "selected_loop": 101,
  "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE",
  "canonical_archetype_id": "C15_MATERIAL_SPREAD_SUPERCYCLE",
  "fine_archetype_id": "COPPER_PRICE_SPREAD_COMPANY_MARGIN_BRIDGE_VS_COPPER_BETA_PRICE_ONLY_FALSE_STAGE2",
  "calibration_usable_case_count": 3,
  "calibration_usable_trigger_count": 3,
  "new_independent_case_count": 3,
  "reused_case_count": 1,
  "same_archetype_new_symbol_count": 2,
  "same_archetype_new_trigger_family_count": 3,
  "positive_case_count": 1,
  "counterexample_count": 2,
  "current_profile_error_count": 2,
  "local_4b_watch_case_count": 3,
  "hard_4c_case_count": 0,
  "do_not_propose_new_weight_delta": false,
  "loop_contribution_label": "canonical_archetype_rule_candidate"
}
```

## 10. Residual contribution summary

```text
residual_error_found = true
profile_axis = C15 material spread supercycle
new_axis_proposed = null
existing_axis_strengthened = C15_company_specific_spread_margin_bridge_requirement; C15_copper_beta_price_only_stage2_block; C15_local_4b_watch_after_vertical_mfe_without_margin_confirmation
existing_axis_weakened = null
sector_specific_rule_candidate = false
canonical_archetype_rule_candidate = true
```

Rule candidate:

```text
For C15, commodity price direction is only a macro precondition.
Stage2-Actionable requires at least one company-specific non-price bridge:
1. ASP pass-through or realized spread evidence,
2. volume/shipment durability,
3. inventory gain not offset by working-capital risk,
4. margin/revision confirmation,
5. customer or contract evidence that makes the spread monetizable.

If only copper/lithium/steel price + stock price momentum exists, cap at Stage1/Watch or Stage2 probe and mark local 4B after vertical MFE.
```

## 11. Current calibrated profile stress test

```text
e2r_2_1 / e2r_2_2 principle retained:
- price-only positive block remains valid
- Stage2-Actionable bonus is useful only when non-price bridge exists
- full 4B still requires non-price evidence, but local 4B watch should activate after price-only spike
- hard 4C not triggered here because thesis break is not established; these are mainly false positive / 4B watch cases
```

Stress-test result:

| axis | result |
|---|---|
| Stage2 bridge requirement | strengthened |
| price-only positive block | strengthened |
| local 4B watch after spike | strengthened |
| Green unlock | not supported |
| hard 4C route | not supported |

## 12. Deferred Coding Agent Handoff Prompt

```text
Do not execute this in the research session.

When a later coding agent batch-ingests this MD:
1. Parse all JSONL trigger rows under section 8.
2. Validate stock-web price fields:
   - price_source == Songdaiki/stock-web
   - price_basis == tradable_raw
   - price_adjustment_status == raw_unadjusted_marcap
   - MFE_30D_pct, MFE_90D_pct, MFE_180D_pct, MAE_30D_pct, MAE_90D_pct, MAE_180D_pct are all present.
3. Dedupe by symbol + canonical_archetype_id + trigger_type + trigger_date + entry_date + entry_price + evidence_family.
4. Treat this as shadow-weight evidence only.
5. Do not change production scoring directly from this one file.
6. Candidate rule to test:
   C15 should score material spread only when commodity-price move is joined by company-level ASP/volume/margin/working-capital bridge.
```

## 13. Completion state

```text
completed_round = R4
completed_loop = 101
selection_basis = docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket = Priority 0
round_schedule_status = coverage_index_selected
round_sector_consistency = pass
next_recommended_archetypes = C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION, C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN, C22_INSURANCE_RATE_CYCLE_RESERVE, C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT, C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG, C16_STRATEGIC_RESOURCE_POLICY_SUPPLY, C17_CHEMICAL_COMMODITY_MARGIN_SPREAD
```
