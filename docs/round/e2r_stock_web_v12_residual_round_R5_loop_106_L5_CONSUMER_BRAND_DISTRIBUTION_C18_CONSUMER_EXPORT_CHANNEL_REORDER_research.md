# E2R v12 Stock-Web Historical Calibration Research

```yaml
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
output_format: one_standalone_markdown_file
selected_round: R5
selected_loop: 106
round_schedule_status: coverage_index_selected
selection_basis: docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket: Priority 1
large_sector_id: L5_CONSUMER_BRAND_DISTRIBUTION
canonical_archetype_id: C18_CONSUMER_EXPORT_CHANNEL_REORDER
fine_archetype_id: GLOBAL_CONSUMER_EXPORT_CHANNEL_REORDER_REPEAT_DEMAND_BRIDGE_VS_CHANNEL_EXPANSION_HEADLINE_HIGH_MAE
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

The previous coverage ladder has moved into Priority 1 after the remaining Priority 0 buckets were brought near the 30-row floor. The next underfilled L5 consumer axis is:

```text
canonical_archetype_id = C18_CONSUMER_EXPORT_CHANNEL_REORDER
row_count_proxy = 33
target_rows = 50
gap_to_target = 17
research_focus = export channel, reorder, repeat demand, inventory burden
```

C18 is intentionally narrower than C20. C20 is the broader K-food/K-beauty global distribution rerating bucket. C18 is the channel-mechanics bucket: a product enters an overseas channel, then the market needs evidence that the channel is not one trial shipment but a repeatable sell-through and reorder loop.

The practical question is:

```text
Does overseas channel access convert into repeated orders, higher ASP/mix, capacity utilization, and operating margin,
or is it just a one-off channel / viral headline that creates a high-MAE price spike?
```

## 2. Price-source validation

All price paths below use `Songdaiki/stock-web` tradable raw OHLCV shards.

```text
upstream_source = FinanceData/marcap
price_basis = tradable_raw
price_adjustment_status = raw_unadjusted_marcap
default_shard = atlas/ohlcv_tradable_by_symbol_year/<prefix>/<ticker>/<year>.csv
```

The selected cases have usable tradable rows and no case-specific 180D corporate-action block identified in the checked profile snippets.

## 3. Case table

| case_id | ticker | name | role | trigger_date | entry_date | entry_price | peak_high | trough_low | MFE | MAE | classification |
|---|---:|---|---|---|---|---:|---:|---:|---:|---:|---|
| C18-001 | 003230 | Samyang Foods | positive with high-MAE watch | 2024-06-14 | 2024-06-14 | 647000 | 800000 | 486000 | +23.65% | -24.88% | confirmed export/reorder bridge, but late/high-MAE |
| C18-002 | 004370 | Nongshim | counterexample / high-MFE high-MAE | 2024-05-27 | 2024-05-28 | 469000 | 599000 | 317000 | +27.72% | -32.41% | channel expansion headline without durable rerating |
| C18-003 | 271560 | Orion | counterexample | 2023-04-11 | 2023-04-11 | 133000 | 147800 | 110800 | +11.13% | -16.69% | overseas localization / channel expansion did not hold |

## 4. Case narratives

### C18-001 — Samyang Foods / Buldak overseas reorder bridge

**Ticker:** `003230`
**Company:** Samyang Foods
**Trigger family:** `BULDAK_US_EUROPE_SHIPMENT_ASP_CAPACITY_REORDER`
**Entry date:** `2024-06-14`
**Entry price:** `647000`

The evidence stack was not merely “K-food is popular.” The June 2024 market note described Samyang as set up for strong Q2 earnings because Buldak exports were brisk, average selling prices continued to rise, U.S. and Europe shipments increased, and capacity expansion supported revenue and earnings. That is close to the C18 ideal: overseas channel demand, reorder-like shipment growth, ASP, and capacity.

Price path:

```text
entry_price = 647000
peak_high = 800000
trough_low = 486000
MFE = +23.65%
MAE = -24.88%
```

Interpretation:

This is not a clean “no-drawdown Green” case. It is a **confirmed export/reorder positive with high-MAE watch**. The price had already rerated before the June evidence confirmation and then suffered a deep August drawdown before later making a new high into December. C18 should not blindly promote late confirmation to Green. It should allow Stage2-Actionable / Yellow only when the export bridge includes repeat shipments, ASP/mix and capacity, while keeping a 4B/full-window watch when the stock has already repriced far ahead of confirmation.

### C18-002 — Nongshim / overseas expansion headline with high-MAE path

**Ticker:** `004370`
**Company:** Nongshim
**Trigger family:** `US_WALMART_MAINSTREAM_CHANNEL_AND_RAMEN_EXPORT_EXPANSION`
**Entry date:** `2024-05-28`
**Entry price:** `469000`

The evidence stack was real but less tight than Samyang. The source described Nongshim’s overseas expansion, Shin Ramyun’s record 2023 sales with a large overseas share, Costco/Walmart presence, U.S. expansion target, and movement from niche Asian grocery space into mainstream food shelves. That is valid C18 evidence, but it is still more channel expansion than reorder/margin proof.

Price path:

```text
entry_price = 469000
peak_high = 599000
trough_low = 317000
MFE = +27.72%
MAE = -32.41%
```

Interpretation:

The first leg was strong, but the forward window later gave back far more than the initial signal should tolerate. This is a **high-MFE/high-MAE counterexample**. It says that channel access plus retailer names can create a tradable spike, but without later reorder, mix, and operating-margin evidence, the signal should not be treated as durable C18 rerating.

### C18-003 — Orion / Turtle Chips overseas localization did not produce durable rerating

**Ticker:** `271560`
**Company:** Orion
**Trigger family:** `TURTLE_CHIPS_VIETNAM_INDIA_LOCALIZATION_CHANNEL_EXPANSION`
**Entry date:** `2023-04-11`
**Entry price:** `133000`

The source-proxy evidence described Turtle Chips localization/launch in Vietnam and India, including local production and India-specific flavors. Mechanically that looks like a C18 export-channel expansion event. But the stock path did not confirm durable reorder-driven rerating.

Price path:

```text
entry_price = 133000
peak_high = 147800
trough_low = 110800
MFE = +11.13%
MAE = -16.69%
```

Interpretation:

This is the cleanest C18 counterexample in the set. Product localization is not enough. C18 should distinguish between a launch/placement and repeated sell-through. The channel must show second-order evidence: reorder, inventory turn, repeat distributor shipment, or margin/revision follow-through.

## 5. Current calibrated profile stress test

Current calibrated proxy assumptions:

```text
stage2_actionable_evidence_bonus = +2.0
stage3_yellow_total_min = 75.0
stage3_green_total_min = 87.0
stage3_green_revision_min = 55.0
price_only_blowoff_blocks_positive_stage = true
full_4b_requires_non_price_evidence = true
hard_4c_thesis_break_routes_to_4c = true
```

Observed residual:

```text
current_profile_error_count = 2
positive_case_count = 1
counterexample_count = 2
high_MAE_case_count = 2
```

The residual is not that the global calibration is wrong. The residual is that C18 needs a tighter *channel quality bridge* before the Stage2-Actionable bonus becomes safe. Export channel expansion often looks strong at the headline level, but its survival depends on repeat demand.

## 6. Raw component score simulation

The following score table is narrative/shadow only. It does not patch production scoring.

| component | Samyang | Nongshim | Orion |
|---|---:|---:|---:|
| fundamental_momentum | 83 | 68 | 55 |
| evidence_quality | 82 | 66 | 58 |
| customer_channel_quality | 86 | 72 | 55 |
| reorder_repeat_demand | 84 | 58 | 42 |
| operating_margin_bridge | 78 | 54 | 48 |
| valuation_overheat_risk | 62 | 67 | 48 |
| high_mae_penalty | -18 | -25 | -15 |
| shadow_total | 77 | 57 | 48 |
| shadow_stage | Stage3-Yellow with 4B watch | Stage2 watch / no Actionable | Stage1-2 watch |

Mechanism:

```text
Samyang = channel + repeat shipment + ASP + capacity, but late/high-MAE
Nongshim = strong channel access, insufficient reorder/margin proof in observed path
Orion = localization/launch without durable reorder confirmation
```

## 7. Machine-readable trigger rows

```jsonl
{"schema":"e2r_v12_trigger_row","case_id":"C18-001","selected_round":"R5","selected_loop":106,"large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C18_CONSUMER_EXPORT_CHANNEL_REORDER","fine_archetype_id":"GLOBAL_CONSUMER_EXPORT_CHANNEL_REORDER_REPEAT_DEMAND_BRIDGE_VS_CHANNEL_EXPANSION_HEADLINE_HIGH_MAE","ticker":"003230","company_name":"Samyang Foods","trigger_date":"2024-06-14","entry_date":"2024-06-14","entry_price":647000,"peak_date":"2024-12-26","peak_high":800000,"trough_date":"2024-08-05","trough_low":486000,"mfe_pct":23.65,"mae_pct":-24.88,"trigger_type":"export_reorder_ASP_capacity_confirmation","evidence_family":"BULDAK_US_EUROPE_SHIPMENT_ASP_CAPACITY_REORDER","path_label":"positive_with_high_mae_watch","calibration_usable":true,"representative_for_aggregate":true,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","source_url_status":"verified_secondary_market_note"}
{"schema":"e2r_v12_trigger_row","case_id":"C18-002","selected_round":"R5","selected_loop":106,"large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C18_CONSUMER_EXPORT_CHANNEL_REORDER","fine_archetype_id":"GLOBAL_CONSUMER_EXPORT_CHANNEL_REORDER_REPEAT_DEMAND_BRIDGE_VS_CHANNEL_EXPANSION_HEADLINE_HIGH_MAE","ticker":"004370","company_name":"Nongshim","trigger_date":"2024-05-27","entry_date":"2024-05-28","entry_price":469000,"peak_date":"2024-06-13","peak_high":599000,"trough_date":"2024-11-15","trough_low":317000,"mfe_pct":27.72,"mae_pct":-32.41,"trigger_type":"mainstream_US_retail_channel_expansion","evidence_family":"US_WALMART_MAINSTREAM_CHANNEL_AND_RAMEN_EXPORT_EXPANSION","path_label":"high_mfe_high_mae_counterexample","calibration_usable":true,"representative_for_aggregate":true,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","source_url_status":"verified_secondary_business_press"}
{"schema":"e2r_v12_trigger_row","case_id":"C18-003","selected_round":"R5","selected_loop":106,"large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C18_CONSUMER_EXPORT_CHANNEL_REORDER","fine_archetype_id":"GLOBAL_CONSUMER_EXPORT_CHANNEL_REORDER_REPEAT_DEMAND_BRIDGE_VS_CHANNEL_EXPANSION_HEADLINE_HIGH_MAE","ticker":"271560","company_name":"Orion","trigger_date":"2023-04-11","entry_date":"2023-04-11","entry_price":133000,"peak_date":"2023-05-08","peak_high":147800,"trough_date":"2023-12-14","trough_low":110800,"mfe_pct":11.13,"mae_pct":-16.69,"trigger_type":"overseas_product_localization_channel_launch","evidence_family":"TURTLE_CHIPS_VIETNAM_INDIA_LOCALIZATION_CHANNEL_EXPANSION","path_label":"channel_launch_without_reorder_counterexample","calibration_usable":true,"representative_for_aggregate":true,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","source_url_status":"source_proxy_only"}
```

## 8. Aggregate residual contribution

```json
{
  "schema": "e2r_v12_residual_contribution",
  "selected_round": "R5",
  "selected_loop": 106,
  "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION",
  "canonical_archetype_id": "C18_CONSUMER_EXPORT_CHANNEL_REORDER",
  "new_independent_case_count": 3,
  "reused_case_count": 0,
  "same_archetype_new_symbol_count": 3,
  "same_archetype_new_trigger_family_count": 3,
  "calibration_usable_case_count": 3,
  "calibration_usable_trigger_count": 3,
  "positive_case_count": 1,
  "counterexample_count": 2,
  "current_profile_error_count": 2,
  "proposed_axis": "c18_reorder_sellthrough_margin_bridge_required_for_stage2_actionable_shadow_only",
  "existing_axis_strengthened": "full_4b_requires_non_price_evidence scoped to C18 channel expansion headlines",
  "do_not_propose_new_weight_delta": false
}
```

## 9. Shadow rule candidate

```text
rule_id = c18_reorder_sellthrough_margin_bridge_required_for_stage2_actionable_shadow_only
scope = canonical_archetype_id == C18_CONSUMER_EXPORT_CHANNEL_REORDER

If evidence is only:
- first overseas listing,
- retailer/channel headline,
- local production launch,
- viral popularity,
- one-time distributor shipment,

then:
    block Stage2-Actionable bonus
    allow watch-only Stage1/Stage2
    require follow-up evidence before Yellow

To unlock Stage2-Actionable:
    require at least two of:
      1. repeat order / reorder / second shipment confirmation
      2. sell-through or inventory-turn proof
      3. ASP/mix improvement
      4. capacity utilization tied to overseas demand
      5. operating margin or EPS revision bridge

If price already expanded sharply before the bridge confirmation:
    keep local_4B_watch = true
    do not unlock Green solely from channel evidence
```

## 10. Deferred Coding Agent Handoff Prompt

```text
You are the later batch implementation agent for stock_agent.

Do not treat this MD as production authority by itself.
Ingest it with the rest of the v12 corpus.

Target artifact:
- selected_round: R5
- selected_loop: 106
- large_sector_id: L5_CONSUMER_BRAND_DISTRIBUTION
- canonical_archetype_id: C18_CONSUMER_EXPORT_CHANNEL_REORDER

Candidate shadow axis:
- c18_reorder_sellthrough_margin_bridge_required_for_stage2_actionable_shadow_only

Implementation intent:
- Add a C18-scoped guard requiring repeat order / sell-through / ASP-mix / utilization / margin bridge before Stage2-Actionable bonus is allowed.
- Strengthen full_4b_requires_non_price_evidence for C18 overseas channel expansion headlines.
- Do not loosen Stage3-Green.
- Do not use future MFE/MAE as same-day scoring input.
- Use these rows only for calibration / validation / shadow-rule planning.

Expected parser rows:
- 3 trigger rows
- 3 calibration-usable cases
- 1 positive-with-high-MAE watch
- 2 counterexamples
```

## 11. Final status

```text
new_independent_case_count = 3
reused_case_count = 0
same_archetype_new_symbol_count = 3
same_archetype_new_trigger_family_count = 3
calibration_usable case 수 = 3
calibration_usable trigger 수 = 3
positive_case_count = 1
counterexample_count = 2
current_profile_error_count = 2
diversity_score_summary = C18 Priority 1 보강 + Buldak repeat-export confirmation / Shin Ramyun mainstream-channel high-MAE / Turtle Chips localization false-positive 분리
do_not_propose_new_weight_delta = false
auto_selected_coverage_gap = C18 rows 33, 50-row target까지 17 부족
sector_specific_rule_candidate = true
canonical_archetype_rule_candidate = true
loop_contribution_label = canonical_archetype_rule_candidate
new_axis_proposed = c18_reorder_sellthrough_margin_bridge_required_for_stage2_actionable_shadow_only
existing_axis_strengthened = full_4b_requires_non_price_evidence scoped to C18 channel expansion headlines
existing_axis_weakened = null
next_recommended_archetypes = C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION, C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT, C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE
```
