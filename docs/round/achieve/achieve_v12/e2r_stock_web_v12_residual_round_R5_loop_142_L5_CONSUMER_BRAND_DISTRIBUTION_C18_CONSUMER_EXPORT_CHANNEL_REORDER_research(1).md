# E2R v12 residual calibration research

## 0. Execution metadata

```yaml
schema_family: v12_sector_archetype_residual
selected_round: R5
selected_loop: 142
large_sector_id: L5_CONSUMER_BRAND_DISTRIBUTION
canonical_archetype_id: C18_CONSUMER_EXPORT_CHANNEL_REORDER
fine_archetype_id: CONSUMER_EXPORT_SELLTHROUGH_REORDER_MARGIN_BRIDGE_VS_BRAND_LABEL_CHANNEL_INVENTORY_DECAY
selection_basis:
  main_execution_prompt: docs/core/e2r_v12_prompt_round_scheduler_corrected.txt
  no_repeat_index: docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket: Priority 0
round_schedule_status: coverage_index_selected
round_sector_consistency: pass
price_source: Songdaiki/stock-web
price_basis: tradable_raw
price_adjustment_status: raw_unadjusted_marcap
stock_web_manifest_max_date: 2026-02-20
production_scoring_changed: false
shadow_weight_only: true
```

`C18_CONSUMER_EXPORT_CHANNEL_REORDER` remains the thinnest visible Priority 0 archetype in the no-repeat index: 3 rows / 3 symbols. The visible covered symbols are `003230`, `011150`, and `383220`. This run uses current-session stock-web-derived rows from adjacent C18/C20/C19/R13 files to formalize the sector-specific C18 bridge requirement.

Direct uncached stock-web shard fetch for some C18 symbols returned cache misses during this turn. Therefore this MD reuses stock-web-derived rows already computed in this v12 session. Those rows include full 30D/90D/180D MFE and MAE from `Songdaiki/stock-web` tradable OHLC. No production scoring is changed.

---

## 1. Research thesis

C18 is not `consumer export label = good`.

It is the channel bridge:

```text
export demand / overseas channel / ODM or brand distribution
→ sell-through, repeat order, reorder cadence, channel inventory, ASP/mix, margin
→ price path validation
```

This loop splits five routes:

1. **Export sell-through engine**
   - Demand converts into channel reorder, shelf velocity, export volume, and margin.
   - Stage2 can remain open.

2. **ODM/export reorder bridge with later inventory/margin drawdown**
   - The first move can be real.
   - If 90D/180D MAE expands, route to local 4B until repeat-order and margin refresh.

3. **K-food / ice-cream export spike**
   - Global channel demand can be tradable.
   - But repeated sell-through and mix/margin proof are required before Green.

4. **Legacy brand / China-channel decay**
   - Export headline and brand prestige are not enough if channel mix is stale or margin bridge decays.
   - Stage2 should be capped or blocked.

5. **Apparel brand / channel inventory false positive**
   - Price-only spike without sell-through or inventory normalization should be blocked.

---

## 2. Source validation

```yaml
stock_web_manifest:
  source_name: FinanceData/marcap
  price_adjustment_status: raw_unadjusted_marcap
  max_date: 2026-02-20
  calibration_shard_root: atlas/ohlcv_tradable_by_symbol_year
  caveat: Raw/unadjusted OHLC; corporate-action contaminated windows blocked by default.
```

Local stock-web-derived row provenance:

```yaml
reused_price_rows_from_current_session:
  - C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION loop 114
  - C19_BRAND_RETAIL_INVENTORY_MARGIN loop 141
  - R13_CROSS_ARCHETYPE_4B_4C_REDTEAM loop 5
  - R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION loop 6
reason:
  - rows already calculated from Songdaiki/stock-web tradable raw 1D OHLC
  - this file converts adjacent consumer-export evidence into a C18 sector-specific rule candidate
  - exact duplicate trigger keys should be deduped if already represented in source archetype rows
  - no production scoring changed
```

Symbol caveats:

```yaml
003230:
  name: 삼양식품
  role: export sell-through positive-control
  note: visible-covered C18 symbol; reused only as positive control

192820:
  name: 코스맥스
  role: ODM/export reorder bridge with local 4B watch

005180:
  name: 빙그레
  role: K-food/ice-cream export channel positive with local 4B watch

090430:
  name: 아모레퍼시픽
  role: legacy brand/China-channel decay counterexample

383220:
  name: F&F
  role: apparel brand/channel inventory false-positive control
  note: visible-covered C18/C19-adjacent symbol; reused as hard control
```

---

## 3. Trigger rows

```jsonl
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","round":"R5","loop":142,"large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C18_CONSUMER_EXPORT_CHANNEL_REORDER","fine_archetype_id":"KFOOD_EXPORT_SELLTHROUGH_REORDER_MARGIN_ENGINE_POSITIVE_CONTROL","symbol":"003230","name":"삼양식품","trigger_type":"Stage2-Actionable","entry_date":"2024-05-20","entry_close":502000,"price_basis":"tradable_raw","mfe_30d_pct":43.03,"mae_30d_pct":-4.68,"mfe_90d_pct":43.03,"mae_90d_pct":-9.26,"mfe_180d_pct":59.36,"mae_180d_pct":-9.26,"forward_high_30d":718000,"forward_low_30d":478500,"forward_high_90d":718000,"forward_low_90d":455500,"forward_high_180d":800000,"forward_low_180d":455500,"calibration_usable":true,"case_role":"reused_visible_positive_control","novelty_key":"C18_CONSUMER_EXPORT_CHANNEL_REORDER|003230|Stage2-Actionable|2024-05-20","non_price_bridge":"K-food export sell-through, channel reorder, shelf expansion and margin bridge","score_alignment":"keep Stage2; allow Yellow path if export volume, reorder, mix and margin bridge remain refreshed","aggregate_credit_note":"visible-covered C18 symbol; use as control if exact C18 key already exists"}
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","round":"R5","loop":142,"large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C18_CONSUMER_EXPORT_CHANNEL_REORDER","fine_archetype_id":"ODM_EXPORT_REORDER_VERTICAL_MFE_WITH_INVENTORY_MARGIN_4B_WATCH","symbol":"192820","name":"코스맥스","trigger_type":"Stage2-Actionable","entry_date":"2024-05-13","entry_close":157700,"price_basis":"tradable_raw","mfe_30d_pct":31.90,"mae_30d_pct":-6.28,"mfe_90d_pct":31.90,"mae_90d_pct":-26.44,"mfe_180d_pct":31.90,"mae_180d_pct":-26.44,"forward_high_30d":208000,"forward_low_30d":147800,"forward_high_90d":208000,"forward_low_90d":116000,"forward_high_180d":208000,"forward_low_180d":116000,"calibration_usable":true,"case_role":"positive_with_local_4B_watch","novelty_key":"C18_CONSUMER_EXPORT_CHANNEL_REORDER|192820|Stage2-Actionable|2024-05-13","non_price_bridge":"ODM/export channel reorder and global beauty customer demand bridge, but inventory/margin refresh needed after high MAE","score_alignment":"Stage2 opens; block Green until repeat-order, channel inventory and margin bridge refresh"}
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","round":"R5","loop":142,"large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C18_CONSUMER_EXPORT_CHANNEL_REORDER","fine_archetype_id":"KFOOD_ICECREAM_EXPORT_CHANNEL_SPIKE_WITH_REPEAT_SELLTHROUGH_4B_WATCH","symbol":"005180","name":"빙그레","trigger_type":"Stage2-Actionable","entry_date":"2024-05-17","entry_close":88300,"price_basis":"tradable_raw","mfe_30d_pct":34.09,"mae_30d_pct":-9.29,"mfe_90d_pct":34.09,"mae_90d_pct":-16.65,"mfe_180d_pct":34.09,"mae_180d_pct":-31.71,"forward_high_30d":118400,"forward_low_30d":80100,"forward_high_90d":118400,"forward_low_90d":73600,"forward_high_180d":118400,"forward_low_180d":60300,"calibration_usable":true,"case_role":"positive_with_deep_4B_watch","novelty_key":"C18_CONSUMER_EXPORT_CHANNEL_REORDER|005180|Stage2-Actionable|2024-05-17","non_price_bridge":"K-food/ice-cream export channel narrative with vertical MFE, but repeat sell-through and margin refresh required","score_alignment":"Stage2 may open; 180D MAE blocks Green until reorder, mix and margin cadence confirm"}
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","round":"R5","loop":142,"large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C18_CONSUMER_EXPORT_CHANNEL_REORDER","fine_archetype_id":"LEGACY_BRAND_CHINA_CHANNEL_DECAY_EXPORT_LABEL_STAGE2_CAP","symbol":"090430","name":"아모레퍼시픽","trigger_type":"Stage2-Watch","entry_date":"2024-05-20","entry_close":179700,"price_basis":"tradable_raw","mfe_30d_pct":11.58,"mae_30d_pct":-6.17,"mfe_90d_pct":11.58,"mae_90d_pct":-18.81,"mfe_180d_pct":11.58,"mae_180d_pct":-44.63,"forward_high_30d":200500,"forward_low_30d":168600,"forward_high_90d":200500,"forward_low_90d":145900,"forward_high_180d":200500,"forward_low_180d":99500,"calibration_usable":true,"case_role":"counterexample_channel_decay","novelty_key":"C18_CONSUMER_EXPORT_CHANNEL_REORDER|090430|Stage2-Watch|2024-05-20","non_price_bridge":"legacy prestige/K-beauty label and China-channel exposure without fresh non-China reorder/margin bridge","score_alignment":"cap Stage2; require non-China sell-through, repeat order and margin evidence before Actionable"}
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","round":"R5","loop":142,"large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C18_CONSUMER_EXPORT_CHANNEL_REORDER","fine_archetype_id":"APPAREL_BRAND_CHANNEL_INVENTORY_SPIKE_DECAY_FALSE_POSITIVE","symbol":"383220","name":"F&F","trigger_type":"Stage2-FalsePositive","entry_date":"2024-07-17","entry_close":74000,"price_basis":"tradable_raw","mfe_30d_pct":3.24,"mae_30d_pct":-33.99,"mfe_90d_pct":3.24,"mae_90d_pct":-33.99,"mfe_180d_pct":3.24,"mae_180d_pct":-33.99,"forward_high_30d":76400,"forward_low_30d":48850,"forward_high_90d":76400,"forward_low_90d":48850,"forward_high_180d":76400,"forward_low_180d":48850,"calibration_usable":true,"case_role":"hard_counterexample","novelty_key":"C18_CONSUMER_EXPORT_CHANNEL_REORDER|383220|Stage2-FalsePositive|2024-07-17","non_price_bridge":"apparel brand/export-channel label without sell-through or inventory normalization; price spike decayed","score_alignment":"block Stage2-Actionable; require channel inventory and repeat-order proof before reopen","aggregate_credit_note":"visible-covered symbol in index; use as hard control if duplicate exists"}
```

---

## 4. Case analysis

### 4.1 Samyang Foods / 003230 — export sell-through positive-control

Samyang is the clean export-sell-through control. The stock path had strong MFE and controlled MAE. That is what C18 wants when export demand converts into reorder and margin.

```yaml
entry_close: 502000
30d_MFE_MAE: +43.03 / -4.68
90d_MFE_MAE: +43.03 / -9.26
180d_MFE_MAE: +59.36 / -9.26
route: Stage2-Actionable positive-control
```

### 4.2 Cosmax / 192820 — ODM export bridge, but 4B after high MAE

Cosmax shows the right middle route. The export/ODM bridge worked, but the later drawdown means the model should not call it Green without fresh repeat-order and margin evidence.

```yaml
entry_close: 157700
30d_MFE_MAE: +31.90 / -6.28
90d_MFE_MAE: +31.90 / -26.44
180d_MFE_MAE: +31.90 / -26.44
route: Stage2-Actionable with local 4B watch
```

### 4.3 Binggrae / 005180 — K-food export channel spike, deep 4B

Binggrae had a real export/brand/channel move, but the 180D drawdown says repeat sell-through and margin durability were not fully proven.

```yaml
entry_close: 88300
30d_MFE_MAE: +34.09 / -9.29
90d_MFE_MAE: +34.09 / -16.65
180d_MFE_MAE: +34.09 / -31.71
route: Stage2 with deep local 4B watch
```

### 4.4 Amorepacific / 090430 — brand prestige and China-channel decay

Amorepacific is a warning against using K-beauty/legacy brand status as a reorder bridge. The forward low became too deep.

```yaml
entry_close: 179700
30d_MFE_MAE: +11.58 / -6.17
90d_MFE_MAE: +11.58 / -18.81
180d_MFE_MAE: +11.58 / -44.63
route: Stage2-Watch / cap
```

### 4.5 F&F / 383220 — apparel channel inventory false positive

F&F is the hard false-positive control. It had almost no MFE and deep MAE, so C18 must not reward apparel brand/export-channel label without inventory and sell-through proof.

```yaml
entry_close: 74000
30d_MFE_MAE: +3.24 / -33.99
90d_MFE_MAE: +3.24 / -33.99
180d_MFE_MAE: +3.24 / -33.99
route: Stage2-FalsePositive
```

---

## 5. Score-return alignment

```yaml
new_independent_case_count: 3
reused_control_case_count: 2
new_visible_C18_symbol_count: 3
calibration_usable_case_count: 5
calibration_usable_trigger_count: 5
positive_case_count: 3
counterexample_or_cap_count: 2
local_4B_watch_count: 2
current_profile_error_count: 3
```

| symbol | role | 30D MFE/MAE | 90D MFE/MAE | 180D MFE/MAE | lesson |
|---|---:|---:|---:|---:|---|
| 003230 | reused positive-control | +43.03 / -4.68 | +43.03 / -9.26 | +59.36 / -9.26 | export sell-through/reorder validates |
| 192820 | ODM export + 4B | +31.90 / -6.28 | +31.90 / -26.44 | +31.90 / -26.44 | repeat-order and margin refresh required |
| 005180 | K-food export + deep 4B | +34.09 / -9.29 | +34.09 / -16.65 | +34.09 / -31.71 | export spike needs durable sell-through |
| 090430 | channel decay cap | +11.58 / -6.17 | +11.58 / -18.81 | +11.58 / -44.63 | brand/China-channel label failed |
| 383220 | hard counterexample | +3.24 / -33.99 | +3.24 / -33.99 | +3.24 / -33.99 | apparel export/channel inventory label fails |

---

## 6. Raw component score breakdown

```jsonl
{"row_type":"score_simulation","symbol":"003230","raw_export_channel":5,"raw_sellthrough_reorder":5,"raw_inventory_quality":4,"raw_margin_bridge":5,"raw_validation":5,"raw_label_only_risk":0,"stage2_actionable_bonus_before":2.0,"stage2_actionable_bonus_after":2.0,"simulated_route":"Stage2-Actionable-positive-control"}
{"row_type":"score_simulation","symbol":"192820","raw_export_channel":4,"raw_sellthrough_reorder":4,"raw_inventory_quality":2,"raw_margin_bridge":2,"raw_validation":3,"raw_label_only_risk":1,"stage2_actionable_bonus_before":2.0,"stage2_actionable_bonus_after":2.0,"simulated_route":"Stage2-Actionable-local-4B"}
{"row_type":"score_simulation","symbol":"005180","raw_export_channel":4,"raw_sellthrough_reorder":3,"raw_inventory_quality":2,"raw_margin_bridge":2,"raw_validation":3,"raw_label_only_risk":2,"stage2_actionable_bonus_before":2.0,"stage2_actionable_bonus_after":2.0,"simulated_route":"Stage2-Actionable-deep-local-4B"}
{"row_type":"score_simulation","symbol":"090430","raw_export_channel":3,"raw_sellthrough_reorder":1,"raw_inventory_quality":1,"raw_margin_bridge":1,"raw_validation":1,"raw_label_only_risk":4,"stage2_actionable_bonus_before":2.0,"stage2_actionable_bonus_after":0.0,"simulated_route":"Stage2-Watch-channel-decay-cap"}
{"row_type":"score_simulation","symbol":"383220","raw_export_channel":2,"raw_sellthrough_reorder":0,"raw_inventory_quality":0,"raw_margin_bridge":0,"raw_validation":0,"raw_label_only_risk":5,"stage2_actionable_bonus_before":2.0,"stage2_actionable_bonus_after":0.0,"simulated_route":"Stage2FalsePositiveBlock"}
```

---

## 7. Current calibrated profile stress test

### Existing error risk

C18 can over-credit:

```text
K-food / K-beauty / brand / export label
```

The correct bridge is narrower:

```text
export channel -> sell-through -> reorder -> inventory normalization -> margin / revision / cash
```

A product can be popular on social media but still fail if the channel is stuffed. A shelf is not a reorder. Reorder is the cash register voting twice.

### Rule candidate

```text
C18_EXPORT_SELLTHROUGH_REORDER_MARGIN_BRIDGE_REQUIREMENT_V142

if C18
and consumer_export_or_brand_label == true
and sellthrough_reorder_inventory_margin_bridge == false:
    stage2_actionable_bonus = 0
    max_stage = Stage2-Watch
```

```text
if C18
and export_sellthrough_reorder_bridge == true
and MFE_90D_pct >= +25
and MAE_90D_pct > -15:
    keep_stage2_actionable_bonus = true
    allow_stage3_yellow_path = true
```

```text
if C18
and export_reorder_bridge == true
and MFE_30D_pct >= +25
and MAE_90D_pct <= -20:
    local_4B_watch = true
    block_stage3_green = true
    require_repeat_order_inventory_margin_refresh = true
```

```text
if C18
and brand_or_export_channel_label == true
and MFE_90D_pct < +10
and MAE_90D_pct <= -25:
    route = Stage2_FalsePositive_Block
    require_new_sellthrough_evidence_before_reopen = true
```

---

## 8. Residual contribution summary

```yaml
do_not_propose_new_weight_delta: false
sector_specific_rule_candidate: false
canonical_archetype_rule_candidate: true
loop_contribution_label: canonical_archetype_rule_candidate
new_axis_proposed: C18_EXPORT_SELLTHROUGH_REORDER_MARGIN_BRIDGE_REQUIREMENT_V142
existing_axis_strengthened:
  - C18_export_label_not_enough_without_reorder_bridge
  - C18_sellthrough_reorder_positive_escape_hatch
  - C18_export_reorder_high_MAE_local_4B
  - C18_brand_channel_inventory_false_positive_block
  - C18_legacy_brand_china_channel_decay_cap
existing_axis_weakened: null
```

---

## 9. Deferred Coding Agent Handoff Prompt

```text
Do not patch production scoring from this MD alone. Batch this C18 loop with adjacent C20/C19 consumer-export files and R13 accounting-trust / 4B/4C guardrails. Extract `C18_EXPORT_SELLTHROUGH_REORDER_MARGIN_BRIDGE_REQUIREMENT_V142` as a shadow-rule candidate. Preserve export sell-through and repeat-order positive controls, but block brand/export labels without inventory normalization, reorder, margin, or cash bridge.
```

---

## 10. Next research state

```yaml
completed_round: R5
completed_loop: 142
selection_basis: docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket: Priority 0
round_schedule_status: coverage_index_selected
round_sector_consistency: pass
next_recommended_archetypes:
  - C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE
  - C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE
  - C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK
  - C31_POLICY_SUBSIDY_LEGISLATION_EVENT
  - C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP
```
