# E2R Stock-Web v12 Residual Research — R4 / Loop 105 / C15_MATERIAL_SPREAD_SUPERCYCLE

```yaml
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
selected_round: R4
selected_loop: 105
round_schedule_status: coverage_index_selected
selection_basis: docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket: Priority 1
large_sector_id: L4_MATERIALS_SPREAD_RESOURCE
canonical_archetype_id: C15_MATERIAL_SPREAD_SUPERCYCLE
fine_archetype_id: COPPER_ZINC_STEEL_SPREAD_SUPERCYCLE_ASP_MARGIN_BRIDGE_VS_COMMODITY_BETA_AND_EVENT_CONTAMINATION
price_source: Songdaiki/stock-web
price_basis: tradable_raw
price_adjustment_status: raw_unadjusted_marcap
calibration_shard_root: atlas/ohlcv_tradable_by_symbol_year
stock_agent_code_access_allowed: false
stock_agent_code_patch_allowed: false
stock_agent_live_scan_allowed: false
production_scoring_changed: false
shadow_weight_only: true
handoff_prompt_embedded: true
handoff_prompt_executed_now: false
```

## 1. Selection rationale

C15_MATERIAL_SPREAD_SUPERCYCLE is still in Priority 1. The current no-repeat index shows C15 at 33 rows, with 17 additional rows needed to reach the 50-row practical calibration target. This run therefore adds C15-specific cases focused on the difference between a true material-spread earnings bridge and a commodity-label or cross-archetype price move.

C15 should not treat “metal price up” as a direct Stage2-Actionable proof. The mechanism has to pass through company-level ASP, volume, inventory timing, processing margin, or hedge/cost pass-through. A material spread is like wind in a sail: it only moves the boat if the sail is actually open and connected to the hull.

## 2. Stock-web price source validation

Primary source used:

```text
price_data_source = Songdaiki/stock-web
upstream_source = FinanceData/marcap
price_basis = tradable_raw
price_adjustment_status = raw_unadjusted_marcap
calibration_shard_root = atlas/ohlcv_tradable_by_symbol_year
```

All rows below are from the tradable shard. No raw shard rows were used for calibration. Corporate-action contamination is treated conservatively. Korea Zinc is separately flagged for cross-archetype governance/tender-offer contamination after 2024-09-13, even though that is not a stock-web corporate-action flag.

## 3. Case universe

| case_id | ticker | name | role | trigger_date | entry_date | entry_price | forward_peak | forward_trough | label |
|---|---:|---|---|---|---|---:|---:|---:|---|
| C15-105-A | 103140 | 풍산 | positive | 2024-03-15 | 2024-03-15 | 45,200 | 78,900 | 45,200 | copper spread + defense demand bridge |
| C15-105-B | 010130 | 고려아연 | event-contaminated positive/control | 2024-04-11 | 2024-04-11 | 472,000 | 549,000 pre-tender / 1,543,000 contaminated | 445,000 | zinc/silver spread bridge later contaminated by governance |
| C15-105-C | 004020 | 현대제철 | counterexample | 2024-09-17 | 2024-09-19 | 24,300 | 28,700 | 19,900 | steel spread false rebound / China demand weakness |

## 4. Case A — 103140 Poongsan / copper spread bridge positive

### Evidence timing

Reuters reported in March 2024 that copper was breaking out after Chinese copper smelters agreed to curb output in response to a tight raw-material market and collapsing treatment charges. This was not just a generic commodity headline: lower treatment charges indicate a concentrate squeeze and a change in the smelting economics. For Poongsan, the copper price move had a plausible ASP/inventory bridge, while the defense-ammunition business gave a second demand channel.

### Price path

```text
ticker = 103140
name = 풍산
trigger_date = 2024-03-15
entry_date = 2024-03-15
entry_price = 45,200
peak_date = 2024-05-14
peak_high = 78,900
trough_low_in_window = 45,200  # no post-entry low below entry observed in checked 180D path
mfe_pct = +74.56
mae_pct = 0.00
classification = positive
```

### Interpretation

This is the cleanest positive C15 case in this run. The copper spread signal had both price confirmation and company-level translation. The important distinction is that Poongsan did not rise merely because “copper was thematic”; it had a believable path through copper product ASP and inventory gain, while ammunition/export demand reduced the risk that the entire move was only a metal-futures beta.

### C15 lesson

```text
if material_spread_signal and company_has_direct_asp_inventory_or_volume_bridge:
    allow Stage2-Actionable shadow candidate
else:
    treat as commodity beta watch only
```

## 5. Case B — 010130 Korea Zinc / zinc-silver bridge, later governance contamination

### Evidence timing

Korea Zinc is structurally relevant to C15 because it is a major non-ferrous metal refiner. Early 2024 metal-price strength made the company a reasonable material-spread bridge candidate. However, from 2024-09-13 onward, Reuters reported that MBK Partners and Young Poong launched a tender offer for Korea Zinc shares, pushing the stock into a control-premium and governance battle. That later move belongs closer to C32 than C15.

### Price path

```text
ticker = 010130
name = 고려아연
trigger_date = 2024-04-11
entry_date = 2024-04-11
entry_price = 472,000

pre_tender_peak_date = 2024-07-15
pre_tender_peak_high = 549,000
pre_tender_mfe_pct = +16.31

pre_tender_trough_date = 2024-08-05
pre_tender_trough_low = 445,000
pre_tender_mae_pct = -5.72

contaminated_governance_peak_date = 2024-10-29
contaminated_governance_peak_high = 1,543,000
contaminated_full_window_mfe_pct = +226.91

classification = positive_control_but_full_window_event_contaminated
calibration_usable_90d = true
calibration_usable_180d = false
blocked_reason_180d = cross_archetype_governance_tender_offer_contamination
```

### Interpretation

Korea Zinc is a useful control because it shows why C15 must split local material-spread validation from later non-material catalysts. If the full 180D window is naively counted, the model will learn a false lesson: it will attribute a takeover battle to zinc/silver spread. That would pollute the canonical archetype.

### C15 lesson

```text
if material_spread_case later enters governance_tender_control_premium_window:
    use local 30D/90D material window only
    block 180D/252D aggregate for C15
    route later price move to C32 or narrative_only
```

## 6. Case C — 004020 Hyundai Steel / steel spread false rebound counterexample

### Evidence timing

Reuters reported in September 2024 that China’s steel sector was weak: crude steel output fell, property construction demand remained strained, and rebar prices were still sharply down year-to-date. In October 2024, Reuters also reported that China’s apparent steel consumption had fallen in the first three quarters and that oversupply had hurt steelmakers’ profitability.

### Price path

```text
ticker = 004020
name = 현대제철
trigger_date = 2024-09-17
entry_date = 2024-09-19
entry_price = 24,300
peak_date = 2024-09-30
peak_high = 28,700
trough_date = 2024-12-09
trough_low = 19,900
mfe_pct = +18.11
mae_pct = -18.11
classification = counterexample
```

### Interpretation

Hyundai Steel is a useful C15 counterexample because the apparent rebound after late-September stimulus did not repair the underlying spread problem. The stock produced a short MFE, then gave back into a material MAE. This is a classic “spread headline without company margin confirmation” failure.

### C15 lesson

```text
if steel_spread_or_rebar_rebound_headline and China/property/end-demand remains weak:
    block Stage2-Actionable
    require company-specific margin and volume recovery evidence
```

## 7. Trigger rows JSONL

```jsonl
{"row_type":"trigger_case","schema_version":"v12","round":"R4","loop":105,"large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C15_MATERIAL_SPREAD_SUPERCYCLE","fine_archetype_id":"COPPER_SPREAD_ASP_MARGIN_BRIDGE","case_id":"C15-105-A","symbol":"103140","name":"풍산","trigger_date":"2024-03-15","entry_date":"2024-03-15","entry_price":45200,"peak_date":"2024-05-14","peak_price":78900,"trough_date":"2024-03-15","trough_price":45200,"mfe_pct":74.56,"mae_pct":0.00,"classification":"positive","calibration_usable":true,"trigger_type":"copper_spread_supply_squeeze","evidence_family":"copper_concentrate_treatment_charge_squeeze","path_label":"spread_to_asp_inventory_bridge","source_url":"https://www.reuters.com/markets/commodities/raw-materials-squeeze-jolts-copper-out-its-torpor-2024-03-14/"}
{"row_type":"trigger_case","schema_version":"v12","round":"R4","loop":105,"large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C15_MATERIAL_SPREAD_SUPERCYCLE","fine_archetype_id":"ZINC_SILVER_REFINING_SPREAD_VS_CONTROL_PREMIUM_CONTAMINATION","case_id":"C15-105-B","symbol":"010130","name":"고려아연","trigger_date":"2024-04-11","entry_date":"2024-04-11","entry_price":472000,"peak_date":"2024-07-15","peak_price":549000,"trough_date":"2024-08-05","trough_price":445000,"mfe_pct":16.31,"mae_pct":-5.72,"classification":"positive_control_local_only","calibration_usable":true,"calibration_scope":"90D_local_material_window_only","blocked_180d_reason":"cross_archetype_governance_tender_offer_contamination","trigger_type":"nonferrous_refining_material_spread","evidence_family":"zinc_silver_refining_margin_with_later_tender_contamination","path_label":"local_spread_bridge_but_full_window_governance_contaminated","source_url":"https://www.reuters.com/markets/deals/private-equity-mbk-young-poong-launch-15-bln-tender-offer-korea-zinc-shares-2024-09-13/"}
{"row_type":"trigger_case","schema_version":"v12","round":"R4","loop":105,"large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C15_MATERIAL_SPREAD_SUPERCYCLE","fine_archetype_id":"STEEL_SPREAD_FALSE_REBOUND_CHINA_DEMAND_WEAKNESS","case_id":"C15-105-C","symbol":"004020","name":"현대제철","trigger_date":"2024-09-17","entry_date":"2024-09-19","entry_price":24300,"peak_date":"2024-09-30","peak_price":28700,"trough_date":"2024-12-09","trough_price":19900,"mfe_pct":18.11,"mae_pct":-18.11,"classification":"counterexample","calibration_usable":true,"trigger_type":"steel_spread_false_rebound","evidence_family":"china_steel_demand_weakness_oversupply_margin_pressure","path_label":"headline_rebound_without_margin_bridge","source_url":"https://www.reuters.com/markets/commodities/chinas-weak-steel-strong-iron-ore-imports-shaped-by-prices-russell-2024-09-17/"}
```

## 8. Score simulation

| case_id | info_conf | bottleneck | contract/backlog | margin_bridge | revision | valuation_risk | redteam_risk | current proxy behavior | residual error |
|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| C15-105-A | 80 | 74 | 50 | 76 | 60 | 52 | 30 | Stage2-Actionable / Yellow watch acceptable | low |
| C15-105-B | 70 | 66 | 45 | 58 | 50 | 82 | 75 | 90D local C15 okay, full-window C15 wrong | medium |
| C15-105-C | 72 | 40 | 30 | 24 | 25 | 55 | 68 | should block positive stage | high |

## 9. Aggregate result

```text
new_independent_case_count = 3
reused_case_count = 0
same_archetype_new_symbol_count = 3
same_archetype_new_trigger_family_count = 3
calibration_usable_case_count = 3
calibration_usable_trigger_count = 3
positive_case_count = 1
local_positive_control_count = 1
counterexample_count = 1
current_profile_error_count = 2
```

## 10. Shadow rule candidate

```text
new_axis_proposed = c15_company_specific_spread_to_margin_bridge_required_for_stage2_actionable_shadow_only
```

Rule draft:

```text
For C15_MATERIAL_SPREAD_SUPERCYCLE:
    material_price_up alone is insufficient for Stage2-Actionable.

    Require at least one of:
        - direct ASP pass-through evidence
        - inventory gain / raw material cost timing benefit
        - company-specific spread margin expansion
        - volume/utilization confirmation
        - earnings revision tied to material spread rather than theme beta

    If later full-window price path is dominated by:
        - governance/tender/control premium
        - unrelated M&A
        - policy-only or sector ETF beta
    then:
        local 30D/90D material window may be usable
        180D/252D C15 aggregate must be blocked or moved to narrative_only / other canonical archetype.
```

## 11. Residual contribution summary

```text
sector_specific_rule_candidate = true
canonical_archetype_rule_candidate = true
loop_contribution_label = canonical_archetype_rule_candidate
new_axis_proposed = c15_company_specific_spread_to_margin_bridge_required_for_stage2_actionable_shadow_only
existing_axis_strengthened = full_4b_requires_non_price_evidence scoped to C15 commodity-beta and cross-archetype contaminated rallies
existing_axis_weakened = null
```

The main residual is not that C15 misses all spread cycles. It catches the obvious beta, but it still risks over-crediting the headline. Poongsan shows a valid bridge. Hyundai Steel shows the failure mode when the spread headline lacks margin recovery. Korea Zinc shows an orthogonal contamination: a later control-premium battle can make a material-spread case look much better than it really was.

## 12. Deferred Coding Agent Handoff Prompt

```text
Do not execute now.

When batch-applying v12 residual research to stock_agent, add a shadow-only C15 rule candidate:

axis_id = c15_company_specific_spread_to_margin_bridge_required_for_stage2_actionable_shadow_only

Scope:
- large_sector_id = L4_MATERIALS_SPREAD_RESOURCE
- canonical_archetype_id = C15_MATERIAL_SPREAD_SUPERCYCLE

Behavior:
- Do not award Stage2-Actionable on material price/spread headline alone.
- Require direct company-level ASP / spread margin / inventory gain / volume-utilization / earnings revision bridge.
- If full-window MFE is driven by governance/tender/control-premium or other non-C15 catalyst, block 180D/252D C15 aggregate and retain only local material-window rows when clean.

Do not change production scoring directly.
Add only as shadow rule candidate and compare against v12 trigger rows.
```

## 13. Final machine summary

```yaml
file_name: e2r_stock_web_v12_residual_round_R4_loop_105_L4_MATERIALS_SPREAD_RESOURCE_C15_MATERIAL_SPREAD_SUPERCYCLE_research.md
selected_round: R4
selected_loop: 105
large_sector_id: L4_MATERIALS_SPREAD_RESOURCE
canonical_archetype_id: C15_MATERIAL_SPREAD_SUPERCYCLE
fine_archetype_id: COPPER_ZINC_STEEL_SPREAD_SUPERCYCLE_ASP_MARGIN_BRIDGE_VS_COMMODITY_BETA_AND_EVENT_CONTAMINATION
new_independent_case_count: 3
reused_case_count: 0
same_archetype_new_symbol_count: 3
same_archetype_new_trigger_family_count: 3
calibration_usable_case_count: 3
calibration_usable_trigger_count: 3
positive_case_count: 1
local_positive_control_count: 1
counterexample_count: 1
current_profile_error_count: 2
auto_selected_coverage_gap: C15 rows 33, 50-row target까지 17 부족
do_not_propose_new_weight_delta: false
sector_specific_rule_candidate: true
canonical_archetype_rule_candidate: true
new_axis_proposed: c15_company_specific_spread_to_margin_bridge_required_for_stage2_actionable_shadow_only
next_recommended_archetypes:
  - C18_CONSUMER_EXPORT_CHANNEL_REORDER
  - C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION
  - C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT
```
