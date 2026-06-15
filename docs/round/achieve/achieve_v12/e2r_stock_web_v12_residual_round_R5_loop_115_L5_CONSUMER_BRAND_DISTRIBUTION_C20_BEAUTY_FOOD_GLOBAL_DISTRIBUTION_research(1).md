# E2R v12 residual calibration research

## 0. Execution metadata

```yaml
schema_family: v12_sector_archetype_residual
selected_round: R5
selected_loop: 115
large_sector_id: L5_CONSUMER_BRAND_DISTRIBUTION
canonical_archetype_id: C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION
fine_archetype_id: KFOOD_KBEAUTY_GLOBAL_DISTRIBUTION_SELLTHROUGH_OPM_REVISION_VS_CHANNEL_INVENTORY_LABEL_DECAY
selection_basis:
  main_execution_prompt: docs/core/e2r_v12_prompt_round_scheduler_corrected.txt
  no_repeat_index: docs/core/V12_Research_No_Repeat_Index.md
web_raw_fetch_status_this_turn:
  main_execution_prompt: read_ok
  no_repeat_index: read_ok
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

`C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION` remains a Priority 0 archetype in the no-repeat index: 6 representative rows, still 24 rows short of the 30-row minimum. The visible covered set is `018250`, `114840`, `192820`, `214420`, `237880`, and `406820`. This loop therefore uses current-session stock-web-derived consumer export rows to build a C20-specific global distribution rule, while marking reused/adjacent C18 rows as controls when appropriate.

The previous local C20 sector pass reached `R5/C20 loop 114`; this run continues as `R5/C20 loop 115`.

This is not a live consumer stock scan. It is a historical calibration MD. Direct uncached stock-web shard fetch has been unstable in recent turns, so the rows below reuse current-session stock-web-derived C18/C19/C20/R13 rows that already include complete 30D/90D/180D MFE and MAE from `Songdaiki/stock-web` tradable OHLC. No production scoring is changed.

---

## 1. Research thesis

C20 is not `K-food / K-beauty label = global winner`.

It is the global distribution earnings bridge:

```text
global channel expansion / export demand / overseas distribution
→ sell-through, repeat order, channel inventory, ASP/mix, OPM, revision and cash
→ price path validation
```

The key split versus C18:

```text
C18 = channel reorder / sell-through mechanics
C20 = global distribution scale translating into OPM, revision, earnings and durable distribution economics
```

The model must not overlearn viral brand attention or one-time overseas channel excitement. Global distribution only matters if the product keeps moving through shelves, distribution partners reorder, inventory does not stuff the channel, and OPM/revision improves.

This loop splits five routes:

1. **K-food global distribution positive-control**
   - Strong export sell-through and margin/revision bridge.
   - Stage2 can stay open.

2. **ODM/global beauty customer distribution with high-MAE 4B**
   - ODM/export customer demand is real, but channel inventory and margin refresh are required before Green.

3. **K-food/ice-cream global channel spike with deep 4B**
   - The first move is tradable, but deep 180D MAE requires repeat sell-through and margin cadence.

4. **Legacy K-beauty/China-channel decay**
   - Brand prestige is not enough when the channel mix is stale.
   - Stage2 should be capped.

5. **Apparel/global brand label inventory false positive**
   - If sell-through and inventory normalization fail, Stage2 should be blocked.

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
  - e2r_stock_web_v12_residual_round_R5_loop_142_L5_CONSUMER_BRAND_DISTRIBUTION_C18_CONSUMER_EXPORT_CHANNEL_REORDER_research.md
  - e2r_stock_web_v12_residual_round_R13_loop_10_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION_research.md
  - adjacent C20/C19 consumer distribution rows from current session
reason:
  - rows were already calculated from Songdaiki/stock-web tradable raw 1D OHLC
  - current file changes canonical scope to C20 and formalizes the global-distribution OPM/revision bridge
  - exact source-archetype keys should be deduped separately from this C20 canonical key
  - no production scoring changed
```

Symbol caveats:

```yaml
003230:
  name: 삼양식품
  role: K-food global distribution sell-through positive-control
  calibration_usable: true
  note: visible in C18 source evidence; use as C20 positive-control row

192820:
  name: 코스맥스
  role: global ODM/beauty distribution bridge with local 4B watch
  calibration_usable: true
  note: visible-covered in raw C20 index; use as formalization/control if duplicate exists

005180:
  name: 빙그레
  role: K-food/ice-cream export channel spike with deep local 4B
  calibration_usable: true

090430:
  name: 아모레퍼시픽
  role: legacy K-beauty/China-channel decay cap
  calibration_usable: true

383220:
  name: F&F
  role: apparel/global brand channel inventory false-positive
  calibration_usable: true
  note: visible in C18 source evidence; use as hard control if duplicate exists
```

---

## 3. Trigger rows

```jsonl
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","round":"R5","loop":115,"large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","fine_archetype_id":"KFOOD_GLOBAL_DISTRIBUTION_SELLTHROUGH_OPM_REVISION_POSITIVE_CONTROL","symbol":"003230","name":"삼양식품","trigger_type":"Stage2-Actionable","entry_date":"2024-05-20","entry_close":502000,"price_basis":"tradable_raw","mfe_30d_pct":43.03,"mae_30d_pct":-4.68,"mfe_90d_pct":43.03,"mae_90d_pct":-9.26,"mfe_180d_pct":59.36,"mae_180d_pct":-9.26,"forward_high_30d":718000,"forward_low_30d":478500,"forward_high_90d":718000,"forward_low_90d":455500,"forward_high_180d":800000,"forward_low_180d":455500,"calibration_usable":true,"case_role":"positive_control","novelty_key":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION|003230|Stage2-Actionable|2024-05-20","non_price_bridge":"K-food global distribution, export sell-through, reorder, ASP/mix, OPM and revision bridge","score_alignment":"keep Stage2; allow Stage3-Yellow while export volume, repeat sell-through, OPM and revision bridge remain refreshed"}
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","round":"R5","loop":115,"large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","fine_archetype_id":"GLOBAL_BEAUTY_ODM_CUSTOMER_DISTRIBUTION_HIGH_MAE_LOCAL_4B","symbol":"192820","name":"코스맥스","trigger_type":"Stage2-Actionable","entry_date":"2024-05-13","entry_close":157700,"price_basis":"tradable_raw","mfe_30d_pct":31.90,"mae_30d_pct":-6.28,"mfe_90d_pct":31.90,"mae_90d_pct":-26.44,"mfe_180d_pct":31.90,"mae_180d_pct":-26.44,"forward_high_30d":208000,"forward_low_30d":147800,"forward_high_90d":208000,"forward_low_90d":116000,"forward_high_180d":208000,"forward_low_180d":116000,"calibration_usable":true,"case_role":"positive_with_local_4B_watch","novelty_key":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION|192820|Stage2-Actionable|2024-05-13","non_price_bridge":"global beauty ODM customer demand and distribution bridge, but channel inventory and OPM refresh needed after high MAE","score_alignment":"Stage2 may open; block Stage3-Green until repeat customer order, inventory quality, OPM and revision refresh","aggregate_credit_note":"192820 appears in raw C20 covered set; dedupe or use as control if already represented"}
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","round":"R5","loop":115,"large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","fine_archetype_id":"KFOOD_ICECREAM_GLOBAL_CHANNEL_SPIKE_DEEP_4B","symbol":"005180","name":"빙그레","trigger_type":"Stage2-Actionable","entry_date":"2024-05-17","entry_close":88300,"price_basis":"tradable_raw","mfe_30d_pct":34.09,"mae_30d_pct":-9.29,"mfe_90d_pct":34.09,"mae_90d_pct":-16.65,"mfe_180d_pct":34.09,"mae_180d_pct":-31.71,"forward_high_30d":118400,"forward_low_30d":80100,"forward_high_90d":118400,"forward_low_90d":73600,"forward_high_180d":118400,"forward_low_180d":60300,"calibration_usable":true,"case_role":"positive_with_deep_local_4B","novelty_key":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION|005180|Stage2-Actionable|2024-05-17","non_price_bridge":"K-food/ice-cream global channel demand with vertical MFE, but repeat sell-through, mix and OPM durability unproven","score_alignment":"Stage2 may open; deep 180D MAE blocks Green until reorder, mix and OPM cadence confirm"}
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","round":"R5","loop":115,"large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","fine_archetype_id":"LEGACY_KBEAUTY_CHINA_CHANNEL_DECAY_STAGE2_CAP","symbol":"090430","name":"아모레퍼시픽","trigger_type":"Stage2-Watch","entry_date":"2024-05-20","entry_close":179700,"price_basis":"tradable_raw","mfe_30d_pct":11.58,"mae_30d_pct":-6.17,"mfe_90d_pct":11.58,"mae_90d_pct":-18.81,"mfe_180d_pct":11.58,"mae_180d_pct":-44.63,"forward_high_30d":200500,"forward_low_30d":168600,"forward_high_90d":200500,"forward_low_90d":145900,"forward_high_180d":200500,"forward_low_180d":99500,"calibration_usable":true,"case_role":"counterexample_channel_decay","novelty_key":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION|090430|Stage2-Watch|2024-05-20","non_price_bridge":"legacy K-beauty and China-channel exposure without refreshed non-China sell-through, channel mix and OPM bridge","score_alignment":"cap Stage2; require non-China distribution sell-through, inventory and margin evidence before Actionable"}
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","round":"R5","loop":115,"large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","fine_archetype_id":"APPAREL_GLOBAL_BRAND_CHANNEL_INVENTORY_FALSE_POSITIVE_BLOCK","symbol":"383220","name":"F&F","trigger_type":"Stage2-FalsePositive","entry_date":"2024-07-17","entry_close":74000,"price_basis":"tradable_raw","mfe_30d_pct":3.24,"mae_30d_pct":-33.99,"mfe_90d_pct":3.24,"mae_90d_pct":-33.99,"mfe_180d_pct":3.24,"mae_180d_pct":-33.99,"forward_high_30d":76400,"forward_low_30d":48850,"forward_high_90d":76400,"forward_low_90d":48850,"forward_high_180d":76400,"forward_low_180d":48850,"calibration_usable":true,"case_role":"hard_counterexample","novelty_key":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION|383220|Stage2-FalsePositive|2024-07-17","non_price_bridge":"apparel/global brand label without sell-through, inventory normalization, OPM or revision bridge","score_alignment":"block Stage2; require new global distribution sell-through evidence before reopen","aggregate_credit_note":"383220 appears in C18 raw covered set; use as hard control if duplicate exists"}
```

---

## 4. Case analysis

### 4.1 Samyang Foods / 003230 — K-food global distribution positive-control

Samyang is the clean C20 route. Export sell-through and margin/revision were visible enough that price confirmed strongly with shallow MAE.

```yaml
entry_close: 502000
30d_MFE_MAE: +43.03 / -4.68
90d_MFE_MAE: +43.03 / -9.26
180d_MFE_MAE: +59.36 / -9.26
route: Stage2-Actionable positive-control
```

This is the path C20 should preserve: global distribution is not the label, it is repeat shelf velocity and OPM torque.

---

### 4.2 Cosmax / 192820 — global beauty ODM bridge with 4B watch

Cosmax had valid global customer/distribution demand, but the 90D/180D drawdown says Green is premature.

```yaml
entry_close: 157700
30d_MFE_MAE: +31.90 / -6.28
90d_MFE_MAE: +31.90 / -26.44
180d_MFE_MAE: +31.90 / -26.44
route: Stage2-Actionable with local 4B
```

The bridge must refresh through repeat customer order, channel inventory quality, OPM and revision.

---

### 4.3 Binggrae / 005180 — K-food channel spike, deep 4B

Binggrae is not a pure false positive. The first move was large. But the later drawdown means the global distribution engine still needs proof.

```yaml
entry_close: 88300
30d_MFE_MAE: +34.09 / -9.29
90d_MFE_MAE: +34.09 / -16.65
180d_MFE_MAE: +34.09 / -31.71
route: Stage2 with deep local 4B watch
```

---

### 4.4 Amorepacific / 090430 — legacy K-beauty channel decay

Amorepacific is the legacy-brand warning. K-beauty status and China-channel exposure are not enough without fresh non-China sell-through and margin bridge.

```yaml
entry_close: 179700
30d_MFE_MAE: +11.58 / -6.17
90d_MFE_MAE: +11.58 / -18.81
180d_MFE_MAE: +11.58 / -44.63
route: Stage2-Watch / cap
```

---

### 4.5 F&F / 383220 — apparel global brand false positive

F&F is the hard control. Brand/global-channel label failed price validation.

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
new_visible_C20_symbol_count: 3
calibration_usable_case_count: 5
calibration_usable_trigger_count: 5
positive_case_count: 3
counterexample_or_cap_count: 2
local_4B_watch_count: 2
current_profile_error_count: 3
```

| symbol | role | 30D MFE/MAE | 90D MFE/MAE | 180D MFE/MAE | lesson |
|---|---:|---:|---:|---:|---|
| 003230 | positive-control | +43.03 / -4.68 | +43.03 / -9.26 | +59.36 / -9.26 | global distribution and OPM/revision validate |
| 192820 | ODM 4B | +31.90 / -6.28 | +31.90 / -26.44 | +31.90 / -26.44 | customer reorder and margin refresh needed |
| 005180 | deep 4B | +34.09 / -9.29 | +34.09 / -16.65 | +34.09 / -31.71 | export channel spike needs durable sell-through |
| 090430 | channel decay cap | +11.58 / -6.17 | +11.58 / -18.81 | +11.58 / -44.63 | legacy brand/China-channel label failed |
| 383220 | hard counterexample | +3.24 / -33.99 | +3.24 / -33.99 | +3.24 / -33.99 | brand/global label without inventory and sell-through fails |

---

## 6. Raw component score breakdown

```jsonl
{"row_type":"score_simulation","symbol":"003230","raw_global_distribution":5,"raw_sellthrough_reorder":5,"raw_inventory_quality":4,"raw_OPM_revision_bridge":5,"raw_cash_conversion":4,"raw_validation":5,"raw_label_only_risk":0,"stage2_actionable_bonus_before":2.0,"stage2_actionable_bonus_after":2.0,"simulated_route":"Stage2-Actionable-positive-control"}
{"row_type":"score_simulation","symbol":"192820","raw_global_distribution":4,"raw_sellthrough_reorder":4,"raw_inventory_quality":2,"raw_OPM_revision_bridge":2,"raw_cash_conversion":2,"raw_validation":3,"raw_label_only_risk":1,"stage2_actionable_bonus_before":2.0,"stage2_actionable_bonus_after":2.0,"simulated_route":"Stage2-Actionable-local-4B"}
{"row_type":"score_simulation","symbol":"005180","raw_global_distribution":4,"raw_sellthrough_reorder":3,"raw_inventory_quality":2,"raw_OPM_revision_bridge":2,"raw_cash_conversion":2,"raw_validation":3,"raw_label_only_risk":2,"stage2_actionable_bonus_before":2.0,"stage2_actionable_bonus_after":2.0,"simulated_route":"Stage2-Actionable-deep-4B"}
{"row_type":"score_simulation","symbol":"090430","raw_global_distribution":3,"raw_sellthrough_reorder":1,"raw_inventory_quality":1,"raw_OPM_revision_bridge":1,"raw_cash_conversion":1,"raw_validation":1,"raw_label_only_risk":4,"stage2_actionable_bonus_before":2.0,"stage2_actionable_bonus_after":0.0,"simulated_route":"Stage2-Watch-channel-decay-cap"}
{"row_type":"score_simulation","symbol":"383220","raw_global_distribution":2,"raw_sellthrough_reorder":0,"raw_inventory_quality":0,"raw_OPM_revision_bridge":0,"raw_cash_conversion":0,"raw_validation":0,"raw_label_only_risk":5,"stage2_actionable_bonus_before":2.0,"stage2_actionable_bonus_after":0.0,"simulated_route":"Stage2FalsePositiveBlock"}
```

---

## 7. Current calibrated profile stress test

### Existing error risk

C20 can over-credit:

```text
K-food label
K-beauty label
global distribution headline
brand prestige
```

The correct C20 bridge is narrower:

```text
global distribution -> sell-through -> repeat order -> channel inventory quality -> OPM/revision -> cash
```

A viral shelf photo is not a reorder. A legacy brand is not OPM. C20 should reward the cash register ringing twice, not the sign above the store.

### Rule candidate

```text
C20_GLOBAL_DISTRIBUTION_OPM_REVISION_BRIDGE_REQUIREMENT_V115

if C20
and beauty_food_global_distribution_label == true
and sellthrough_reorder_inventory_OPM_revision_cash_bridge == false:
    stage2_actionable_bonus = 0
    max_stage = Stage2-Watch
```

```text
if C20
and global_distribution_sellthrough_OPM_revision_bridge == true
and MFE_90D_pct >= +25
and MAE_90D_pct > -15:
    keep_stage2_actionable_bonus = true
    allow_stage3_yellow_path = true
```

```text
if C20
and global_distribution_bridge == true
and MFE_30D_pct >= +25
and MAE_90D_pct <= -20:
    local_4B_watch = true
    block_stage3_green = true
    require_repeat_order_inventory_OPM_revision_refresh = true
```

```text
if C20
and brand_or_global_channel_label == true
and MFE_90D_pct < +15
and MAE_180D_pct <= -30:
    route = Stage2_FalsePositive_Block_or_Stage2Cap
    require_new_sellthrough_OPM_evidence_before_reopen = true
```

---

## 8. Residual contribution summary

```yaml
do_not_propose_new_weight_delta: false
sector_specific_rule_candidate: false
canonical_archetype_rule_candidate: true
loop_contribution_label: canonical_archetype_rule_candidate
new_axis_proposed: C20_GLOBAL_DISTRIBUTION_OPM_REVISION_BRIDGE_REQUIREMENT_V115
existing_axis_strengthened:
  - C20_global_distribution_label_not_enough_without_OPM_revision_bridge
  - C20_Kfood_sellthrough_positive_escape_hatch
  - C20_global_beauty_ODM_high_MAE_local_4B
  - C20_legacy_Kbeauty_channel_decay_stage2_cap
  - C20_apparel_global_brand_inventory_false_positive_block
existing_axis_weakened: null
```

---

## 9. Deferred Coding Agent Handoff Prompt

```text
Do not patch production scoring from this MD alone. Batch this C20 loop with C18 loop 142, C19 inventory/margin loops, adjacent C20 loop 114, and R13 accounting-trust / 4B-4C consumer guardrail files. Extract `C20_GLOBAL_DISTRIBUTION_OPM_REVISION_BRIDGE_REQUIREMENT_V115` as a shadow-rule candidate. Preserve K-food/global sell-through positives; cap or block K-beauty/apparel/global-channel labels without repeat order, inventory quality, OPM/revision or cash bridge.
```

---

## 10. Next research state

```yaml
completed_round: R5
completed_loop: 115
selection_basis: docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket: Priority 0
round_schedule_status: coverage_index_selected
round_sector_consistency: pass
next_recommended_archetypes:
  - C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN
  - C22_INSURANCE_RATE_CYCLE_RESERVE
  - C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY
  - C15_MATERIAL_SPREAD_SUPERCYCLE
  - R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW
```
