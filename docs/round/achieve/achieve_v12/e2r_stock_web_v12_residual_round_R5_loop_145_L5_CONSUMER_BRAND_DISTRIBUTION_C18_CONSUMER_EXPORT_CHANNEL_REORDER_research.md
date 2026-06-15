# E2R v12 residual calibration research

## 0. Execution metadata

```yaml
schema_family: v12_sector_archetype_residual
selected_round: R5
selected_loop: 145
large_sector_id: L5_CONSUMER_BRAND_DISTRIBUTION
canonical_archetype_id: C18_CONSUMER_EXPORT_CHANNEL_REORDER
fine_archetype_id: KFOOD_KBEAUTY_EXPORT_REORDER_VS_CAPACITY_HEADLINE_AND_DOMESTIC_RETAIL_RECLASSIFICATION
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

`C18_CONSUMER_EXPORT_CHANNEL_REORDER` remains the top Priority 0 under-covered archetype in the current no-repeat index: 3 representative rows and 27 rows short of the 30-row minimum. The v12 scheduler maps C18~C20 to `R5 / L5_CONSUMER_BRAND_DISTRIBUTION`.

This run continues the local C18 sequence after `R5/C18 loop 144`; selected loop is therefore `145`.

This is not a live consumer-stock scan. It is a historical calibration / residual rule file. Direct uncached `stock-web` symbol shards returned cache misses in this turn, so this MD reuses stock-web-derived C18/C19 rows already calculated in the current v12 session. Those rows already contain complete 30D/90D/180D MFE and MAE from `Songdaiki/stock-web` tradable OHLC. Exact source keys should be deduped separately from this C18 canonical key. No production scoring is changed.

---

## 1. Research thesis

C18 is not `consumer brand is popular overseas`.

It is the export-channel reorder bridge:

```text
overseas shelf / DTC / distributor / ODM / mainstream retail entry
→ sell-through
→ repeat order
→ inventory quality
→ margin / revision / cash
→ price path validation
```

The false-positive route is deceptively simple:

```text
export headline
capacity headline
brand prestige
domestic retail value-up
```

All four can sound like channel expansion. But C18 only pays for the second order. A shelf photo is the first frame; reorder is the cash register voting twice.

This loop separates six routes:

1. **K-food export ASP/capacity positive but high MAE**
   - Export bridge can be real, but if the entry is after a vertical move, local 4B is needed until reorder/margin refresh.

2. **Mainstream shelf expansion high-MFE/high-MAE**
   - Strong early MFE is tradable.
   - Deep 90D/180D MAE requires repeat order and margin proof before Green.

3. **Capacity headline without near-term reorder**
   - Stage2 label should be capped when the bridge is capacity construction rather than immediate channel reorder.

4. **K-beauty ODM reorder positive-control**
   - Stage2 survives when customer order, export reorder and margin bridge are more direct.

5. **Domestic retail margin / department-store value-up**
   - May be positive, but it is not C18 export reorder. Reclassify toward C19 unless export-channel evidence exists.

6. **Hypermarket turnaround / restructuring label**
   - Domestic retail restructuring without reorder and margin proof should not be learned as C18.

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
  - R5/C18 loop 141
  - R5/C18 loop 143
  - R5/C19 loop 141
  - R13 accounting-trust / Stage2 false-positive / 4B-4C guardrail rows
reason:
  - all rows were already calculated from Songdaiki/stock-web tradable raw 1D OHLC
  - current file changes or preserves canonical scope to C18 and formalizes an export-channel reorder gate
  - domestic retail rows are included only as wrong-archetype reclassification controls
  - no production scoring changed
```

Symbol caveats:

```yaml
003230:
  name: 삼양식품
  role: K-food export/ASP/capacity positive with high-MAE local 4B watch
  calibration_usable: true
  note: distinct entry family from 2024-05-17 and 2024-05-20 rows already used elsewhere

004370:
  name: 농심
  role: mainstream shelf expansion high-MFE/high-MAE local 4B
  calibration_usable: true

097950:
  name: CJ제일제당
  role: capacity/global K-food proxy without near-term reorder/margin proof
  calibration_usable: true

161890:
  name: 한국콜마
  role: K-beauty ODM/export reorder positive-control
  calibration_usable: true

069960:
  name: 현대백화점
  role: domestic retail margin/value-up reclassification control
  calibration_usable: true

139480:
  name: 이마트
  role: hypermarket restructuring turnaround label counterexample
  calibration_usable: true
```

---

## 3. Trigger rows

```jsonl
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","round":"R5","loop":145,"large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C18_CONSUMER_EXPORT_CHANNEL_REORDER","fine_archetype_id":"KFOOD_EXPORT_ASP_CAPACITY_HIGH_MAE_LOCAL_4B","symbol":"003230","name":"삼양식품","trigger_type":"Stage2-Actionable","entry_date":"2024-06-17","entry_close":686000,"price_basis":"tradable_raw","mfe_30d_pct":4.66,"mae_30d_pct":-15.31,"mfe_90d_pct":4.66,"mae_90d_pct":-33.60,"mfe_180d_pct":37.03,"mae_180d_pct":-33.60,"forward_high_30d":718000,"forward_low_30d":581000,"forward_high_90d":718000,"forward_low_90d":455500,"forward_high_180d":940000,"forward_low_180d":455500,"calibration_usable":true,"case_role":"same_symbol_distinct_trigger_family_local_4B","novelty_key":"C18_CONSUMER_EXPORT_CHANNEL_REORDER|003230|Stage2-Actionable|2024-06-17","non_price_bridge":"Buldak export, ASP, US/Europe shipment and capacity support, but post-spike entry created high MAE before later validation","score_alignment":"Stage2 may survive, but route to local 4B until reorder, ASP and margin refresh; do not treat as immediate Green"}
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","round":"R5","loop":145,"large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C18_CONSUMER_EXPORT_CHANNEL_REORDER","fine_archetype_id":"KFOOD_MAINSTREAM_SHELF_EXPANSION_HIGH_MFE_HIGH_MAE_4B","symbol":"004370","name":"농심","trigger_type":"Stage2-Actionable","entry_date":"2024-05-28","entry_close":469000,"price_basis":"tradable_raw","mfe_30d_pct":27.72,"mae_30d_pct":-8.96,"mfe_90d_pct":27.72,"mae_90d_pct":-23.13,"mfe_180d_pct":27.72,"mae_180d_pct":-32.41,"forward_high_30d":599000,"forward_low_30d":427000,"forward_high_90d":599000,"forward_low_90d":360500,"forward_high_180d":599000,"forward_low_180d":317000,"calibration_usable":true,"case_role":"high_MFE_high_MAE_local_4B","novelty_key":"C18_CONSUMER_EXPORT_CHANNEL_REORDER|004370|Stage2-Actionable|2024-05-28","non_price_bridge":"Shin Ramyun overseas mainstream shelf expansion and overseas sales mix bridge, but later drawdown requires repeat sell-through and margin proof","score_alignment":"local 4B candidate; block Stage3-Green until reorder, channel inventory and margin bridge refresh"}
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","round":"R5","loop":145,"large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C18_CONSUMER_EXPORT_CHANNEL_REORDER","fine_archetype_id":"KFOOD_CAPACITY_PROXY_WITHOUT_NEAR_TERM_REORDER_MARGIN_BRIDGE_CAP","symbol":"097950","name":"CJ제일제당","trigger_type":"Stage2-Watch","entry_date":"2024-11-22","entry_close":272000,"price_basis":"tradable_raw","mfe_30d_pct":2.39,"mae_30d_pct":-9.93,"mfe_90d_pct":2.39,"mae_90d_pct":-14.71,"mfe_180d_pct":2.39,"mae_180d_pct":-19.12,"forward_high_30d":278500,"forward_low_30d":245000,"forward_high_90d":278500,"forward_low_90d":232000,"forward_high_180d":278500,"forward_low_180d":220500,"calibration_usable":true,"case_role":"capacity_proxy_counterexample_cap","novelty_key":"C18_CONSUMER_EXPORT_CHANNEL_REORDER|097950|Stage2-Watch|2024-11-22","non_price_bridge":"global K-food capacity construction proxy without near-term repeat order, sell-through or margin bridge","score_alignment":"cap Stage2; capacity headline alone is not C18 reorder evidence"}
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","round":"R5","loop":145,"large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C18_CONSUMER_EXPORT_CHANNEL_REORDER","fine_archetype_id":"KBEAUTY_ODM_EXPORT_REORDER_POSITIVE_CONTROL","symbol":"161890","name":"한국콜마","trigger_type":"Stage2-Actionable","entry_date":"2024-05-10","entry_close":55200,"price_basis":"tradable_raw","mfe_30d_pct":35.87,"mae_30d_pct":-10.51,"mfe_90d_pct":35.87,"mae_90d_pct":-10.51,"mfe_180d_pct":35.87,"mae_180d_pct":-10.51,"forward_high_30d":75000,"forward_low_30d":49400,"forward_high_90d":75000,"forward_low_90d":49400,"forward_high_180d":75000,"forward_low_180d":49400,"calibration_usable":true,"case_role":"positive_control","novelty_key":"C18_CONSUMER_EXPORT_CHANNEL_REORDER|161890|Stage2-Actionable|2024-05-10","non_price_bridge":"K-beauty ODM/export reorder bridge with strong MFE and contained MAE","score_alignment":"cleaner Stage2-Actionable; candidate Stage3-Yellow only if margin and reorder evidence stay refreshed"}
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","round":"R5","loop":145,"large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C18_CONSUMER_EXPORT_CHANNEL_REORDER","fine_archetype_id":"DOMESTIC_RETAIL_MARGIN_VALUEUP_WRONG_ARCHETYPE_RECLASSIFY_TO_C19","source_archetype_id":"C19_BRAND_RETAIL_INVENTORY_MARGIN","symbol":"069960","name":"현대백화점","trigger_type":"Stage2-Watch","entry_date":"2024-01-29","entry_close":51200,"price_basis":"tradable_raw","mfe_30d_pct":20.90,"mae_30d_pct":-7.42,"mfe_90d_pct":20.90,"mae_90d_pct":-5.86,"mfe_180d_pct":20.90,"mae_180d_pct":-10.45,"forward_high_30d":61900,"forward_low_30d":47400,"forward_high_90d":61900,"forward_low_90d":48200,"forward_high_180d":61900,"forward_low_180d":45850,"calibration_usable":true,"case_role":"wrong_archetype_positive_elsewhere","novelty_key":"C18_CONSUMER_EXPORT_CHANNEL_REORDER|069960|Stage2-Watch|2024-01-29","non_price_bridge":"domestic department-store value-up, retail margin buffer and inventory discipline candidate, not export-channel reorder","score_alignment":"cap C18 contribution and reclassify to C19; do not use domestic value-up as C18 export evidence"}
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","round":"R5","loop":145,"large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C18_CONSUMER_EXPORT_CHANNEL_REORDER","fine_archetype_id":"DOMESTIC_HYPERMARKET_TURNAROUND_LABEL_WITHOUT_REORDER_MARGIN_BLOCK","source_archetype_id":"C19_BRAND_RETAIL_INVENTORY_MARGIN","symbol":"139480","name":"이마트","trigger_type":"Stage2-FalsePositive","entry_date":"2024-01-29","entry_close":80900,"price_basis":"tradable_raw","mfe_30d_pct":9.39,"mae_30d_pct":-10.38,"mfe_90d_pct":9.39,"mae_90d_pct":-21.76,"mfe_180d_pct":9.39,"mae_180d_pct":-31.77,"forward_high_30d":88500,"forward_low_30d":72500,"forward_high_90d":88500,"forward_low_90d":63300,"forward_high_180d":88500,"forward_low_180d":55200,"calibration_usable":true,"case_role":"wrong_archetype_counterexample","novelty_key":"C18_CONSUMER_EXPORT_CHANNEL_REORDER|139480|Stage2-FalsePositive|2024-01-29","non_price_bridge":"domestic hypermarket restructuring and turnaround label without export reorder, sell-through or durable margin proof","score_alignment":"block C18; if researched at all, use C19 inventory/margin lens with strict proof"}
```

---

## 4. Case analysis

### 4.1 Samyang Foods / 003230 — export bridge but late-entry 4B

This is a different trigger family from the earlier clean Samyang rows. Here the entry came after the market already priced a lot of the Buldak export/ASP/capacity story.

```yaml
entry_close: 686000
30D_MFE_MAE: +4.66 / -15.31
90D_MFE_MAE: +4.66 / -33.60
180D_MFE_MAE: +37.03 / -33.60
route: local 4B, no immediate Green
```

The bridge was real, but the price path says the timing was not clean.

---

### 4.2 Nongshim / 004370 — shelf expansion high-MFE/high-MAE

Nongshim had the exact C18 vocabulary the model wants: overseas shelf expansion and global brand penetration. But the deep drawdown says it should stay in local 4B until the channel proves repeat order and margin.

```yaml
entry_close: 469000
30D_MFE_MAE: +27.72 / -8.96
90D_MFE_MAE: +27.72 / -23.13
180D_MFE_MAE: +27.72 / -32.41
route: local 4B
```

---

### 4.3 CJ CheilJedang / 097950 — capacity proxy without near-term reorder

CJ is a capacity/global K-food proxy. It is not a clean C18 reorder row.

```yaml
entry_close: 272000
30D_MFE_MAE: +2.39 / -9.93
90D_MFE_MAE: +2.39 / -14.71
180D_MFE_MAE: +2.39 / -19.12
route: Stage2-Watch / cap
```

Capacity construction is a warehouse being built. C18 needs the second order coming through the door.

---

### 4.4 Kolmar Korea / 161890 — ODM export reorder positive-control

Kolmar is the cleaner K-beauty route. The bridge is customer reorder/ODM export demand rather than just brand heat.

```yaml
entry_close: 55200
30D_MFE_MAE: +35.87 / -10.51
90D_MFE_MAE: +35.87 / -10.51
180D_MFE_MAE: +35.87 / -10.51
route: Stage2-Actionable with refresh requirement
```

---

### 4.5 Hyundai Department Store / 069960 — positive elsewhere, wrong C18 room

This row may be positive under C19, but C18 should not claim it.

```yaml
entry_close: 51200
90D_MFE_MAE: +20.90 / -5.86
180D_MFE_MAE: +20.90 / -10.45
route: reclassify to C19
```

Domestic retail inventory discipline is not export-channel reorder.

---

### 4.6 E-Mart / 139480 — domestic turnaround label block

E-Mart is the domestic retail label counterexample.

```yaml
entry_close: 80900
90D_MFE_MAE: +9.39 / -21.76
180D_MFE_MAE: +9.39 / -31.77
route: C18 false positive / reclassify-or-block
```

---

## 5. Score-return alignment

```yaml
new_independent_case_count: 4
reused_or_wrong_archetype_control_count: 2
calibration_usable_case_count: 6
calibration_usable_trigger_count: 6
positive_case_count: 3
counterexample_or_cap_count: 3
local_4B_watch_count: 3
wrong_archetype_reclassification_count: 2
current_profile_error_count: 4
duplicate_note: 003230 and 161890 have prior C18 coverage but use distinct trigger context or control role; 069960/139480 are wrong-archetype controls and should not be counted as C18 positives
```

| symbol | role | 30D MFE/MAE | 90D MFE/MAE | 180D MFE/MAE | lesson |
|---|---:|---:|---:|---:|---|
| 003230 | export bridge late-entry 4B | +4.66 / -15.31 | +4.66 / -33.60 | +37.03 / -33.60 | real bridge, poor entry timing |
| 004370 | shelf expansion 4B | +27.72 / -8.96 | +27.72 / -23.13 | +27.72 / -32.41 | repeat order and margin refresh needed |
| 097950 | capacity proxy cap | +2.39 / -9.93 | +2.39 / -14.71 | +2.39 / -19.12 | capacity headline is not reorder |
| 161890 | ODM positive-control | +35.87 / -10.51 | +35.87 / -10.51 | +35.87 / -10.51 | customer reorder bridge validates |
| 069960 | reclassify positive elsewhere | +20.90 / -7.42 | +20.90 / -5.86 | +20.90 / -10.45 | domestic retail margin belongs to C19 |
| 139480 | wrong-archetype counterexample | +9.39 / -10.38 | +9.39 / -21.76 | +9.39 / -31.77 | domestic turnaround label fails C18 |

---

## 6. Raw component score breakdown

```jsonl
{"row_type":"score_simulation","symbol":"003230","raw_export_channel":5,"raw_sellthrough_reorder":4,"raw_inventory_quality":2,"raw_margin_bridge":3,"raw_validation":2,"raw_label_only_risk":1,"stage2_actionable_bonus_before":2.0,"stage2_actionable_bonus_after":2.0,"simulated_route":"Local4B_LateEntryExportBridge"}
{"row_type":"score_simulation","symbol":"004370","raw_export_channel":5,"raw_sellthrough_reorder":3,"raw_inventory_quality":2,"raw_margin_bridge":2,"raw_validation":2,"raw_label_only_risk":2,"stage2_actionable_bonus_before":2.0,"stage2_actionable_bonus_after":2.0,"simulated_route":"Local4B_ShelfExpansionRefresh"}
{"row_type":"score_simulation","symbol":"097950","raw_export_channel":2,"raw_sellthrough_reorder":1,"raw_inventory_quality":1,"raw_margin_bridge":1,"raw_validation":0,"raw_label_only_risk":4,"stage2_actionable_bonus_before":2.0,"stage2_actionable_bonus_after":0.0,"simulated_route":"Stage2Watch_CapacityProxyCap"}
{"row_type":"score_simulation","symbol":"161890","raw_export_channel":4,"raw_sellthrough_reorder":4,"raw_inventory_quality":3,"raw_margin_bridge":4,"raw_validation":4,"raw_label_only_risk":0,"stage2_actionable_bonus_before":2.0,"stage2_actionable_bonus_after":2.0,"simulated_route":"Stage2Actionable_ODMReorderPositive"}
{"row_type":"score_simulation","symbol":"069960","raw_export_channel":0,"raw_sellthrough_reorder":0,"raw_inventory_quality":3,"raw_margin_bridge":3,"raw_validation":3,"raw_label_only_risk":3,"raw_reclassification_need":5,"stage2_actionable_bonus_before":2.0,"stage2_actionable_bonus_after":0.0,"simulated_route":"ReclassifyToC19"}
{"row_type":"score_simulation","symbol":"139480","raw_export_channel":0,"raw_sellthrough_reorder":0,"raw_inventory_quality":1,"raw_margin_bridge":1,"raw_validation":0,"raw_label_only_risk":5,"raw_reclassification_need":4,"stage2_actionable_bonus_before":2.0,"stage2_actionable_bonus_after":0.0,"simulated_route":"C18FalsePositiveBlock"}
```

---

## 7. Current calibrated profile stress test

### Existing error risk

C18 can over-credit:

```text
capacity expansion
global brand mention
mainstream shelf entry
domestic retail turnaround
```

The proper C18 mechanism is narrower:

```text
export channel -> sell-through -> reorder -> inventory quality -> margin/cash
```

A warehouse, shelf, or domestic store turnaround is not the same as an overseas reorder.

### Rule candidate

```text
C18_EXPORT_REORDER_SECOND_ORDER_GATE_V145

if C18
and consumer_export_or_global_brand_label == true
and sellthrough_reorder_inventory_margin_bridge == false:
    stage2_actionable_bonus = 0
    max_stage = Stage2-Watch
```

```text
if C18
and export_channel_reorder_bridge == true
and MFE_90D_pct >= +25
and MAE_90D_pct <= -20:
    local_4B_watch = true
    block_stage3_green = true
    require_repeat_order_inventory_margin_refresh = true
```

```text
if C18
and capacity_construction_or_global_proxy_label == true
and near_term_sellthrough_reorder_bridge == false:
    cap_stage2_actionable_bonus = true
```

```text
if C18
and domestic_retail_margin_or_inventory_bridge == true
and export_reorder_bridge == false:
    cap_C18_contribution = true
    require_reclassification_to_C19 = true
```

```text
if C18
and MFE_90D_pct < +10
and MAE_90D_pct <= -20
and export_reorder_bridge == false:
    route = Stage2_FalsePositive_Block
```

---

## 8. Residual contribution summary

```yaml
do_not_propose_new_weight_delta: false
sector_specific_rule_candidate: false
canonical_archetype_rule_candidate: true
loop_contribution_label: canonical_archetype_rule_candidate
new_axis_proposed: C18_EXPORT_REORDER_SECOND_ORDER_GATE_V145
existing_axis_strengthened:
  - C18_export_label_not_enough_without_second_order
  - C18_high_MFE_high_MAE_shelf_expansion_local_4B
  - C18_capacity_headline_without_reorder_stage2_cap
  - C18_ODM_export_reorder_positive_escape_hatch
  - C18_domestic_retail_wrong_archetype_reclassification_guard
existing_axis_weakened: null
```

---

## 9. Deferred Coding Agent Handoff Prompt

```text
Do not patch production scoring from this MD alone. Batch this C18 loop with C18 loops 141~144, C19 inventory/margin loop 141, C20 loops 114~115, and R13 accounting-trust / 4B-4C / Stage2 false-positive guardrails. Extract `C18_EXPORT_REORDER_SECOND_ORDER_GATE_V145` as a shadow-rule candidate. Preserve K-food/K-beauty export reorder positives, route high-MFE/high-MAE shelf expansion to local 4B, cap capacity-only global proxy rows, and reclassify domestic retail margin/inventory rows to C19 instead of C18.
```

---

## 10. Next research state

```yaml
completed_round: R5
completed_loop: 145
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
