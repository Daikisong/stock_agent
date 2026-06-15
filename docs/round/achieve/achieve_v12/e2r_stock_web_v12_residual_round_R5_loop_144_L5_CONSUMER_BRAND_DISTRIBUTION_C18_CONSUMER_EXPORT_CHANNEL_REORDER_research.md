# E2R v12 residual calibration research

## 0. Execution metadata

```yaml
schema_family: v12_sector_archetype_residual
selected_round: R5
selected_loop: 144
large_sector_id: L5_CONSUMER_BRAND_DISTRIBUTION
canonical_archetype_id: C18_CONSUMER_EXPORT_CHANNEL_REORDER
fine_archetype_id: K_BEAUTY_DTC_EXPORT_CHANNEL_REORDER_VS_LEGACY_PRESTIGE_CHANNEL_DECAY
selection_basis:
  main_execution_prompt: docs/core/e2r_v12_prompt_round_scheduler_corrected.txt
  no_repeat_index: docs/core/V12_Research_No_Repeat_Index.md
web_raw_fetch_status_this_turn:
  main_execution_prompt: read_ok
  no_repeat_index: read_ok
  stock_web_manifest: read_ok
  uncached_symbol_shards: cache_miss_observed
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

`C18_CONSUMER_EXPORT_CHANNEL_REORDER` remains the highest-priority under-covered archetype in the latest no-repeat index: 3 representative rows, 27 rows short of the 30-row minimum. The v12 scheduler maps C18~C20 to `R5 / L5_CONSUMER_BRAND_DISTRIBUTION`.

This run continues the local C18 sequence after `R5/C18 loop 143`, so the selected loop is `144`.

This is not a live consumer-stock scan. It is a historical calibration / residual rule file. Direct uncached `stock-web` symbol shards returned cache misses in this turn, so the trigger rows below reuse stock-web-derived rows already calculated in the current v12 session from C20 and C18 files. The rows contain 30D/90D/180D MFE and MAE calculated from `Songdaiki/stock-web` tradable OHLC. Exact source-archetype keys should be deduped separately from the C18 canonical key. No production scoring is changed.

---

## 1. Research thesis

C18 is not `K-beauty / K-food export label = reorder`.

It is the channel mechanism:

```text
global consumer attention
→ sell-through
→ distributor / DTC / retail / ODM reorder
→ inventory normalization
→ margin, revision and cash
→ price path validation
```

The main false-positive route is a brand or channel label that never becomes repeat order. The market sees a shelf, but the company only benefits if that shelf empties and the channel orders again.

This loop focuses on the K-beauty / DTC export branch.

1. **DTC / device / overseas distribution bridge**
   - Stage2 can stay open when channel expansion, repeat demand and revenue bridge are visible.
   - If MFE is vertical, a 4B watch is still required until reorder and margin cadence refresh.

2. **K-food export sell-through control**
   - Strong sell-through and ASP/OPM bridge validates C18.
   - It is reused here as a positive route-shape control.

3. **Legacy prestige / China rebound label**
   - A famous brand can still fail if the channel bridge decays.
   - Stage2 should be capped or blocked without non-China sell-through and repeat-order proof.

4. **Global apparel / brand channel inventory false positive**
   - Brand label plus low MFE and deep MAE should hard-block.

---

## 2. Source validation

```yaml
stock_web_manifest:
  source_name: FinanceData/marcap
  price_adjustment_status: raw_unadjusted_marcap
  max_date: 2026-02-20
  calibration_shard_root: atlas/ohlcv_tradable_by_symbol_year
  caveat: Raw/unadjusted OHLC; corporate-action-contaminated windows blocked by default.
```

Local stock-web-derived row provenance:

```yaml
reused_price_rows_from_current_session:
  - R5/C20 loop 114
  - R5/C20 loop 115
  - R5/C18 loop 143
  - R13 accounting-trust loop 10
  - R13 Stage2 false-positive loop 9
  - R13 high-MAE loop 7
reason:
  - all rows were already calculated from Songdaiki/stock-web tradable raw 1D OHLC
  - current file changes canonical scope to C18 and formalizes the export-channel reorder gate
  - exact source-archetype keys should be deduped separately from this C18 canonical key
  - no production scoring changed
```

Symbol caveats:

```yaml
278470:
  name: 에이피알
  source_archetype: C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION
  role: K-beauty DTC/device global channel expansion and revenue bridge
  calibration_usable: true

003230:
  name: 삼양식품
  source_archetype: C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION
  role: K-food export sell-through / ASP / OPM positive-control
  calibration_usable: true
  note: same symbol appeared in C18 before, but this row uses a different entry date and evidence family

090430:
  name: 아모레퍼시픽
  source_archetype: C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION
  role: legacy K-beauty / China rebound without durable sell-through margin bridge
  calibration_usable: true
  note: C18 loop 143 used 2024-05-20 watch row; this row uses 2024-05-31 failed rebound row

383220:
  name: F&F
  source_archetype: C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION
  role: apparel/global brand channel inventory false-positive control
  calibration_usable: true
  note: visible-covered / control-only if duplicate exists

192820:
  name: 코스맥스
  source_archetype: C18_CONSUMER_EXPORT_CHANNEL_REORDER
  role: K-beauty ODM export reorder positive with 4B watch
  calibration_usable: true
  note: reused control from C18 loop 143; no new aggregate credit if duplicate exists
```

---

## 3. Trigger rows

```jsonl
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","round":"R5","loop":144,"large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C18_CONSUMER_EXPORT_CHANNEL_REORDER","fine_archetype_id":"K_BEAUTY_DTC_DEVICE_GLOBAL_CHANNEL_REORDER_REVENUE_BRIDGE","source_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","symbol":"278470","name":"에이피알","trigger_type":"Stage2-Actionable","entry_date":"2025-02-27","entry_close":60100,"price_basis":"tradable_raw","mfe_30d_pct":20.63,"mae_30d_pct":-8.82,"mfe_90d_pct":204.99,"mae_90d_pct":-8.82,"mfe_180d_pct":365.06,"mae_180d_pct":-8.82,"calibration_usable":true,"case_role":"positive_vertical_reorder_bridge_with_4B_watch","novelty_key":"C18_CONSUMER_EXPORT_CHANNEL_REORDER|278470|Stage2-Actionable|2025-02-27","non_price_bridge":"K-beauty device/DTC global channel expansion, overseas demand and revenue bridge; vertical MFE requires reorder/margin cadence refresh","score_alignment":"keep Stage2; allow Yellow path only while global DTC/channel reorder and margin bridge stay refreshed"}
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","round":"R5","loop":144,"large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C18_CONSUMER_EXPORT_CHANNEL_REORDER","fine_archetype_id":"K_FOOD_EXPORT_SELLTHROUGH_ASP_OPM_REORDER_POSITIVE_CONTROL","source_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","symbol":"003230","name":"삼양식품","trigger_type":"Stage2-Actionable","entry_date":"2024-05-17","entry_close":446500,"price_basis":"tradable_raw","mfe_30d_pct":60.81,"mae_30d_pct":0.00,"mfe_90d_pct":60.81,"mae_90d_pct":0.00,"mfe_180d_pct":106.05,"mae_180d_pct":0.00,"calibration_usable":true,"case_role":"positive_control_distinct_trigger_family","novelty_key":"C18_CONSUMER_EXPORT_CHANNEL_REORDER|003230|Stage2-Actionable|2024-05-17","non_price_bridge":"export sell-through, ASP, shipment/capacity and OPM bridge; not just K-food label","score_alignment":"keep Stage2; this is a positive control for sell-through to reorder and margin conversion"}
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","round":"R5","loop":144,"large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C18_CONSUMER_EXPORT_CHANNEL_REORDER","fine_archetype_id":"LEGACY_BEAUTY_CHINA_REBOUND_WITHOUT_DURABLE_REORDER_FALSE_POSITIVE","source_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","symbol":"090430","name":"아모레퍼시픽","trigger_type":"Stage2-FalsePositive","entry_date":"2024-05-31","entry_close":194200,"price_basis":"tradable_raw","mfe_30d_pct":3.24,"mae_30d_pct":-14.68,"mfe_90d_pct":3.24,"mae_90d_pct":-40.32,"mfe_180d_pct":3.24,"mae_180d_pct":-48.76,"calibration_usable":true,"case_role":"hard_counterexample_distinct_entry","novelty_key":"C18_CONSUMER_EXPORT_CHANNEL_REORDER|090430|Stage2-FalsePositive|2024-05-31","non_price_bridge":"legacy prestige beauty and China rebound label without durable non-China sell-through, reorder or margin bridge","score_alignment":"block Stage2-Actionable; low MFE and severe MAE reject the channel label"}
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","round":"R5","loop":144,"large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C18_CONSUMER_EXPORT_CHANNEL_REORDER","fine_archetype_id":"APPAREL_GLOBAL_BRAND_CHANNEL_INVENTORY_FALSE_POSITIVE_CONTROL","source_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","symbol":"383220","name":"F&F","trigger_type":"Stage2-FalsePositive","entry_date":"2024-07-17","entry_close":74000,"price_basis":"tradable_raw","mfe_30d_pct":3.24,"mae_30d_pct":-33.99,"mfe_90d_pct":3.24,"mae_90d_pct":-33.99,"mfe_180d_pct":3.24,"mae_180d_pct":-33.99,"calibration_usable":true,"case_role":"hard_counterexample_control","novelty_key":"C18_CONSUMER_EXPORT_CHANNEL_REORDER|383220|Stage2-FalsePositive|2024-07-17","non_price_bridge":"apparel/global brand label without sell-through, channel inventory normalization or reorder proof","score_alignment":"hard block; require new channel-inventory and repeat-order evidence before reopen","aggregate_credit_note":"visible-covered control if duplicate exists"}
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","round":"R5","loop":144,"large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C18_CONSUMER_EXPORT_CHANNEL_REORDER","fine_archetype_id":"K_BEAUTY_ODM_EXPORT_REORDER_VERTICAL_MFE_LOCAL_4B_CONTROL","source_archetype_id":"C18_CONSUMER_EXPORT_CHANNEL_REORDER","symbol":"192820","name":"코스맥스","trigger_type":"Stage2-Actionable","entry_date":"2024-05-13","entry_close":157700,"price_basis":"tradable_raw","mfe_30d_pct":31.90,"mae_30d_pct":-6.28,"mfe_90d_pct":31.90,"mae_90d_pct":-26.44,"mfe_180d_pct":31.90,"mae_180d_pct":-26.44,"calibration_usable":true,"case_role":"reused_positive_with_local_4B_watch","novelty_key":"C18_CONSUMER_EXPORT_CHANNEL_REORDER|192820|Stage2-Actionable|2024-05-13","non_price_bridge":"K-beauty ODM global reorder and customer demand bridge; high MAE requires inventory and margin refresh","score_alignment":"Stage2 may open; block Green until repeat customer order, channel inventory and margin bridge refresh","aggregate_credit_note":"exact key likely present in C18 loop 143; use as control if duplicate"}
```

---

## 4. Case analysis

### 4.1 APR / 278470 — DTC/device export bridge with vertical MFE

APR is the new C18 positive route. The move was extreme, but the reason it belongs in C18 is the channel mechanism: global DTC demand, device/product channel expansion, and revenue bridge.

```yaml
entry_close: 60100
30D_MFE_MAE: +20.63 / -8.82
90D_MFE_MAE: +204.99 / -8.82
180D_MFE_MAE: +365.06 / -8.82
route: Stage2-Actionable with vertical-rerating 4B watch
```

A vertical rerating should not automatically become Green. But when the bridge is real, it should not be blocked as price-only either.

---

### 4.2 Samyang Foods / 003230 — sell-through positive-control

Samyang is the clean control for export sell-through. The price path has near-zero drawdown in this source row.

```yaml
entry_close: 446500
30D_MFE_MAE: +60.81 / 0.00
90D_MFE_MAE: +60.81 / 0.00
180D_MFE_MAE: +106.05 / 0.00
route: KeepStage2
```

The company did not merely have a K-food label. The route was export demand, ASP, shipment/capacity and OPM.

---

### 4.3 Amorepacific / 090430 — legacy China rebound false positive

This is the sharper Amore row than the earlier watch case. Entry after the rebound label did not validate.

```yaml
entry_close: 194200
30D_MFE_MAE: +3.24 / -14.68
90D_MFE_MAE: +3.24 / -40.32
180D_MFE_MAE: +3.24 / -48.76
route: Stage2-FalsePositive
```

A famous brand can still fail if the sell-through and non-China reorder bridge is absent.

---

### 4.4 F&F / 383220 — brand/channel inventory hard block

F&F remains the hard channel-inventory control.

```yaml
entry_close: 74000
30D_MFE_MAE: +3.24 / -33.99
90D_MFE_MAE: +3.24 / -33.99
180D_MFE_MAE: +3.24 / -33.99
route: hard block
```

The model should not keep reopening a brand/export-channel label without channel inventory repair.

---

### 4.5 Cosmax / 192820 — reused ODM export 4B control

Cosmax keeps the model from over-blocking K-beauty ODM cases. The bridge is real, but the drawdown says it belongs in local 4B until margin and inventory refresh.

```yaml
entry_close: 157700
30D_MFE_MAE: +31.90 / -6.28
90D_MFE_MAE: +31.90 / -26.44
180D_MFE_MAE: +31.90 / -26.44
route: local 4B control
```

---

## 5. Score-return alignment

```yaml
new_independent_case_count: 3
reused_control_case_count: 2
calibration_usable_case_count: 5
calibration_usable_trigger_count: 5
positive_case_count: 3
counterexample_count: 2
local_4B_watch_count: 2
current_profile_error_count: 3
duplicate_note: 192820 and 383220 may be controls if exact C18 keys already exist; 278470 and 090430/2024-05-31 add a distinct C18 route family
```

| symbol | role | 30D MFE/MAE | 90D MFE/MAE | 180D MFE/MAE | lesson |
|---|---:|---:|---:|---:|---|
| 278470 | DTC/device export positive | +20.63 / -8.82 | +204.99 / -8.82 | +365.06 / -8.82 | channel bridge validates, but vertical rerating needs 4B watch |
| 003230 | positive-control | +60.81 / 0.00 | +60.81 / 0.00 | +106.05 / 0.00 | export sell-through/ASP/OPM validates |
| 090430 | hard counterexample | +3.24 / -14.68 | +3.24 / -40.32 | +3.24 / -48.76 | legacy brand/China rebound failed |
| 383220 | hard control | +3.24 / -33.99 | +3.24 / -33.99 | +3.24 / -33.99 | brand/channel inventory label fails |
| 192820 | ODM 4B control | +31.90 / -6.28 | +31.90 / -26.44 | +31.90 / -26.44 | real reorder bridge but needs margin/inventory refresh |

---

## 6. Raw component score breakdown

```jsonl
{"row_type":"score_simulation","symbol":"278470","raw_export_channel":5,"raw_sellthrough_reorder":4,"raw_inventory_quality":3,"raw_margin_bridge":4,"raw_validation":5,"raw_label_only_risk":0,"stage2_actionable_bonus_before":2.0,"stage2_actionable_bonus_after":2.0,"simulated_route":"Stage2Actionable_VerticalReorderBridge4B"}
{"row_type":"score_simulation","symbol":"003230","raw_export_channel":5,"raw_sellthrough_reorder":5,"raw_inventory_quality":5,"raw_margin_bridge":5,"raw_validation":5,"raw_label_only_risk":0,"stage2_actionable_bonus_before":2.0,"stage2_actionable_bonus_after":2.0,"simulated_route":"KeepStage2_PositiveControl"}
{"row_type":"score_simulation","symbol":"090430","raw_export_channel":2,"raw_sellthrough_reorder":0,"raw_inventory_quality":0,"raw_margin_bridge":0,"raw_validation":0,"raw_label_only_risk":5,"stage2_actionable_bonus_before":2.0,"stage2_actionable_bonus_after":0.0,"simulated_route":"Stage2FalsePositiveBlock"}
{"row_type":"score_simulation","symbol":"383220","raw_export_channel":2,"raw_sellthrough_reorder":0,"raw_inventory_quality":0,"raw_margin_bridge":0,"raw_validation":0,"raw_label_only_risk":5,"stage2_actionable_bonus_before":2.0,"stage2_actionable_bonus_after":0.0,"simulated_route":"HardBlock_ChannelInventory"}
{"row_type":"score_simulation","symbol":"192820","raw_export_channel":4,"raw_sellthrough_reorder":4,"raw_inventory_quality":2,"raw_margin_bridge":2,"raw_validation":3,"raw_label_only_risk":1,"stage2_actionable_bonus_before":2.0,"stage2_actionable_bonus_after":2.0,"simulated_route":"Local4B_ReorderMarginRefresh"}
```

---

## 7. Current calibrated profile stress test

### Existing error risk

C18 can still over-credit:

```text
K-beauty label
K-food label
famous brand
global channel story
```

The correct bridge is narrower:

```text
export/channel attention -> sell-through -> repeat order -> inventory quality -> margin/revision -> cash
```

A shelf photo is only the first frame. C18 should score the second order.

### Rule candidate

```text
C18_DTC_EXPORT_REORDER_INVENTORY_MARGIN_BRIDGE_REQUIREMENT_V144

if C18
and consumer_export_Kbeauty_Kfood_or_brand_label == true
and sellthrough_reorder_inventory_margin_bridge == false:
    stage2_actionable_bonus = 0
    max_stage = Stage2-Watch
```

```text
if C18
and export_DTC_or_ODM_reorder_bridge == true
and MFE_90D_pct >= +25
and MAE_90D_pct > -15:
    keep_stage2_actionable_bonus = true
    allow_stage3_yellow_path = true
```

```text
if C18
and export_DTC_or_ODM_reorder_bridge == true
and MFE_30D_pct >= +25
and MAE_90D_pct <= -20:
    local_4B_watch = true
    block_stage3_green = true
    require_repeat_order_inventory_margin_refresh = true
```

```text
if C18
and legacy_brand_or_channel_rebound_label == true
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
new_axis_proposed: C18_DTC_EXPORT_REORDER_INVENTORY_MARGIN_BRIDGE_REQUIREMENT_V144
existing_axis_strengthened:
  - C18_export_label_not_enough_without_reorder_bridge
  - C18_DTC_device_export_channel_positive_escape_hatch
  - C18_Kfood_export_sellthrough_positive_control
  - C18_ODM_export_reorder_high_MAE_local_4B
  - C18_legacy_brand_channel_rebound_false_positive_block
existing_axis_weakened: null
```

---

## 9. Deferred Coding Agent Handoff Prompt

```text
Do not patch production scoring from this MD alone. Batch this C18 loop with C18 loops 141~143, C20 loops 114~115, and R13 accounting-trust / Stage2 false-positive / high-MAE guardrail files. Extract `C18_DTC_EXPORT_REORDER_INVENTORY_MARGIN_BRIDGE_REQUIREMENT_V144` as a shadow-rule candidate. Preserve DTC/device/ODM/K-food export positives only where sell-through and reorder economics are visible; block legacy brand/channel rebound labels without durable sell-through, inventory normalization, margin or cash bridge.
```

---

## 10. Next research state

```yaml
completed_round: R5
completed_loop: 144
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
