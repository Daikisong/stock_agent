# E2R v12 residual calibration research

## 0. Execution metadata

```yaml
schema_family: v12_sector_archetype_residual
selected_round: R5
selected_loop: 114
large_sector_id: L5_CONSUMER_BRAND_DISTRIBUTION
canonical_archetype_id: C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION
fine_archetype_id: K_FOOD_GLOBAL_DISTRIBUTION_EXPORT_SELLTHROUGH_MARGIN_BRIDGE_VS_MATURE_GLOBAL_CHANNEL_LOW_MFE
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

`C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION` remains thin in the no-repeat index: 6 rows / 6 symbols. The visible covered set is concentrated in K-beauty symbols and a few distribution cases, so this loop moves the fine axis into K-food global distribution.

The registry already contains C20 loops 100, 107, 109, 111 and 113. This run therefore continues as `R5/C20 loop 114`.

---

## 1. Research thesis

C20 is not “K-food is popular.” It is the bridge:

```text
global demand / viral product awareness
→ real distribution shelf expansion or repeat sell-through
→ export volume, product mix, gross margin, OPM revision
→ price path alignment
```

This loop separates three flavors of C20:

1. **Buldak-style global distribution engine**: viral demand plus export/shelf expansion creates explosive operating leverage.
2. **Ice-cream/processed-food export spike with later fade**: the global distribution story works, but drawdown requires local 4B watch.
3. **Mature global confectionery footprint with low MFE**: the company is global, but the specific trigger may not be actionable if incremental distribution/margin revision is absent.

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

Symbol caveats:

```yaml
003230:
  name: 삼양식품
  corporate_action_candidate_dates: [2003-07-25]
  relevant_window_after_candidate: true

005180:
  name: 빙그레
  corporate_action_candidate_dates: [1995-09-29, 1996-09-25, 1998-12-15]
  relevant_window_after_candidate: true

271560:
  name: 오리온
  corporate_action_candidate_count: 0
  calibration_caveat: clean
```

---

## 3. Trigger rows

```jsonl
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","round":"R5","loop":114,"large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","fine_archetype_id":"BULDAK_GLOBAL_DISTRIBUTION_EXPORT_SELLTHROUGH_OPM_LEVERAGE","symbol":"003230","name":"삼양식품","trigger_type":"Stage2-Actionable","entry_date":"2024-05-20","entry_close":502000,"price_basis":"tradable_raw","mfe_30d_pct":43.03,"mae_30d_pct":-4.68,"mfe_90d_pct":43.03,"mae_90d_pct":-9.26,"mfe_180d_pct":59.36,"mae_180d_pct":-9.26,"forward_high_30d":718000,"forward_low_30d":478500,"forward_high_90d":718000,"forward_low_90d":455500,"forward_high_180d":800000,"forward_low_180d":455500,"calibration_usable":true,"case_role":"positive_control","novelty_key":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION|003230|Stage2-Actionable|2024-05-20","non_price_bridge":"Buldak/global ramen distribution sell-through and export operating leverage","score_alignment":"clean C20 positive; allow Stage2-Actionable and Stage3-Yellow path when export margin/reorder evidence is refreshed"}
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","round":"R5","loop":114,"large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","fine_archetype_id":"ICE_CREAM_GLOBAL_EXPORT_SPIKE_WITH_LOCAL_4B_WATCH","symbol":"005180","name":"빙그레","trigger_type":"Stage2-Actionable","entry_date":"2024-05-17","entry_close":88300,"price_basis":"tradable_raw","mfe_30d_pct":34.09,"mae_30d_pct":-9.29,"mfe_90d_pct":34.09,"mae_90d_pct":-16.65,"mfe_180d_pct":34.09,"mae_180d_pct":-31.71,"forward_high_30d":118400,"forward_low_30d":80100,"forward_high_90d":118400,"forward_low_90d":73600,"forward_high_180d":118400,"forward_low_180d":60300,"calibration_usable":true,"case_role":"positive_with_4B_watch","novelty_key":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION|005180|Stage2-Actionable|2024-05-17","non_price_bridge":"Melona/ice-cream and processed-food global distribution narrative with vertical MFE","score_alignment":"Stage2 may open, but 180D MAE requires sell-through/margin refresh before Green"}
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","round":"R5","loop":114,"large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","fine_archetype_id":"MATURE_GLOBAL_CONFECTIONERY_FOOTPRINT_LOW_MFE_STAGE2_CAP","symbol":"271560","name":"오리온","trigger_type":"Stage2-Watch","entry_date":"2024-06-10","entry_close":97900,"price_basis":"tradable_raw","mfe_30d_pct":8.99,"mae_30d_pct":-6.54,"mfe_90d_pct":8.99,"mae_90d_pct":-11.44,"mfe_180d_pct":8.99,"mae_180d_pct":-11.44,"forward_high_30d":106700,"forward_low_30d":91500,"forward_high_90d":106700,"forward_low_90d":86700,"forward_high_180d":106700,"forward_low_180d":86700,"calibration_usable":true,"case_role":"low_MFE_counterexample","novelty_key":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION|271560|Stage2-Watch|2024-06-10","non_price_bridge":"mature global confectionery footprint without fresh incremental sell-through/margin revision at trigger","score_alignment":"global footprint alone is not enough; cap Stage2 unless incremental distribution or margin bridge appears"}
```

---

## 4. Case analysis

### 4.1 Samyang Foods / 003230 — global distribution engine positive-control

Samyang is the clean positive-control. The entry date is after the visible global Buldak distribution/viral-demand repricing had already accelerated, but the forward path still validates the bridge.

```yaml
entry_date: 2024-05-20
entry_close: 502000
30d_high: 718000
30d_low: 478500
90d_high: 718000
90d_low: 455500
180d_high: 800000
180d_low: 455500
mfe_30d_pct: 43.03
mae_30d_pct: -4.68
mfe_180d_pct: 59.36
mae_180d_pct: -9.26
```

Interpretation:

```text
classification = Stage2-Actionable positive-control
```

This case says C20 should reward a true distribution/sell-through engine, not just a brand label. The product is viral, but the equity signal works because viral demand is translated into export shipments, shelf access, and operating leverage.

### 4.2 Binggrae / 005180 — global ice-cream narrative works, then needs 4B watch

Binggrae had a strong vertical move around the global ice-cream / processed-food export narrative.

```yaml
entry_date: 2024-05-17
entry_close: 88300
30d_high: 118400
30d_low: 80100
90d_high: 118400
90d_low: 73600
180d_high: 118400
180d_low: 60300
mfe_30d_pct: 34.09
mae_30d_pct: -9.29
mfe_90d_pct: 34.09
mae_90d_pct: -16.65
mfe_180d_pct: 34.09
mae_180d_pct: -31.71
```

Interpretation:

```text
classification = Stage2-Actionable with local_4B_watch
```

The price response proves that the global distribution narrative can work. But the full-window drawdown says C20 must demand repeat sell-through, channel order refresh, mix, and margin proof before Stage3-Green.

### 4.3 Orion / 271560 — global footprint, but low incremental MFE

Orion is a mature global confectionery/distribution footprint case. That structure is real, but the selected 2024 trigger path does not produce enough MFE.

```yaml
entry_date: 2024-06-10
entry_close: 97900
30d_high: 106700
30d_low: 91500
90d_high: 106700
90d_low: 86700
180d_high: 106700
180d_low: 86700
mfe_90d_pct: 8.99
mae_90d_pct: -11.44
```

Interpretation:

```text
classification = Stage2-Watch / low-MFE counterexample
```

This prevents C20 from over-rewarding “already global” companies. A global shelf network is the road; the trigger still needs a new truck moving faster on that road: incremental SKU rollout, channel expansion, margin improvement, or sell-through acceleration.

---

## 5. Score-return alignment

```yaml
new_independent_case_count: 3
new_visible_C20_symbol_count: 3
same_archetype_new_trigger_family_count: 3
calibration_usable_case_count: 3
calibration_usable_trigger_count: 3
positive_case_count: 2
counterexample_count: 1
current_profile_error_count: 2
```

| symbol | role | 30D MFE/MAE | 90D MFE/MAE | 180D MFE/MAE | lesson |
|---|---:|---:|---:|---:|---|
| 003230 | positive-control | +43.03 / -4.68 | +43.03 / -9.26 | +59.36 / -9.26 | true export sell-through engine deserves C20 credit |
| 005180 | positive + 4B watch | +34.09 / -9.29 | +34.09 / -16.65 | +34.09 / -31.71 | global-food spike needs repeat-order/margin refresh |
| 271560 | low-MFE counterexample | +8.99 / -6.54 | +8.99 / -11.44 | +8.99 / -11.44 | global footprint alone is not actionable |

---

## 6. Raw component score breakdown

```jsonl
{"row_type":"score_simulation","symbol":"003230","raw_EPS_revision_bridge":5,"raw_visibility":5,"raw_global_distribution":5,"raw_sellthrough_reorder":5,"raw_margin_bridge":4,"raw_validation":5,"raw_info_edge":3,"stage2_actionable_bonus_before":2.0,"stage2_actionable_bonus_after":2.0,"simulated_route":"Stage2-Actionable-positive-control"}
{"row_type":"score_simulation","symbol":"005180","raw_EPS_revision_bridge":2,"raw_visibility":4,"raw_global_distribution":4,"raw_sellthrough_reorder":3,"raw_margin_bridge":2,"raw_validation":3,"raw_info_edge":2,"stage2_actionable_bonus_before":2.0,"stage2_actionable_bonus_after":2.0,"simulated_route":"Stage2-Actionable-with-4B-watch"}
{"row_type":"score_simulation","symbol":"271560","raw_EPS_revision_bridge":1,"raw_visibility":4,"raw_global_distribution":4,"raw_sellthrough_reorder":1,"raw_margin_bridge":1,"raw_validation":1,"raw_info_edge":1,"stage2_actionable_bonus_before":2.0,"stage2_actionable_bonus_after":0.0,"simulated_route":"Stage2-Watch-low-MFE-global-footprint"}
```

---

## 7. Current calibrated profile stress test

### Existing error risk

C20 can over-reward:

```text
K-food / K-beauty label
+ known overseas sales
+ global brand awareness
```

That is too broad. Global awareness is the sign outside the store; C20 needs the cash register ringing repeatedly inside the store. The difference is sell-through and reorder.

### Rule candidate

```text
C20_GLOBAL_DISTRIBUTION_SELLTHROUGH_MARGIN_BRIDGE_REQUIREMENT

if C20
and K_food_or_K_beauty_global_label == true
and incremental_distribution_or_sellthrough_reorder == false
and margin_or_OPM_revision_bridge == false:
    stage2_actionable_bonus = 0
    max_stage = Stage2-Watch
```

```text
if C20
and global_distribution_sellthrough_bridge == true
and MFE_90D_pct >= +25
and MAE_90D_pct > -15:
    keep_stage2_actionable_bonus = true
    allow_stage3_yellow_path = true
```

```text
if C20
and MFE_30D_pct >= +30
and MAE_180D_pct <= -25
and refreshed_sellthrough_or_margin_bridge == false:
    local_4B_watch = true
    block_stage3_green = true
```

```text
if C20
and mature_global_footprint == true
and MFE_90D_pct < +10
and incremental_distribution_reorder_bridge == false:
    cap_stage2_actionable_bonus = true
```

---

## 8. Residual contribution summary

```yaml
do_not_propose_new_weight_delta: false
sector_specific_rule_candidate: false
canonical_archetype_rule_candidate: true
loop_contribution_label: canonical_archetype_rule_candidate
new_axis_proposed: C20_KFOOD_GLOBAL_DISTRIBUTION_SELLTHROUGH_VS_MATURE_FOOTPRINT_LOW_MFE
existing_axis_strengthened:
  - C20_global_distribution_sellthrough_margin_bridge_requirement
  - C20_Kfood_export_engine_positive_escape_hatch
  - C20_vertical_food_export_spike_local_4B_watch
  - C20_mature_global_footprint_low_MFE_stage2_cap
existing_axis_weakened: null
```

---

## 9. Next recommended archetypes

```text
C27_CONTENT_IP_GLOBAL_MONETIZATION
C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK
R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION
C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION_retest_with_beauty_food_balance
C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN
```
