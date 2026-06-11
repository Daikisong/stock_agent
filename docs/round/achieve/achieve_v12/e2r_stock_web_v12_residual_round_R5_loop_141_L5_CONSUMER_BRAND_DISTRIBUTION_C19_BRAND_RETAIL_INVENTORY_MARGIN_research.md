# E2R v12 residual calibration research

## 0. Execution metadata

```yaml
schema_family: v12_sector_archetype_residual
selected_round: R5
selected_loop: 141
large_sector_id: L5_CONSUMER_BRAND_DISTRIBUTION
canonical_archetype_id: C19_BRAND_RETAIL_INVENTORY_MARGIN
fine_archetype_id: DEPARTMENT_STORE_VALUEUP_MARGIN_BUFFER_VS_HYPERMARKET_AND_APPAREL_INVENTORY_SPIKE_DECAY
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

`C19_BRAND_RETAIL_INVENTORY_MARGIN` was selected after the recent R13 4B/4C checkpoint because the next gap list included C19, and the repository registry shows C19 remains below practical depth despite several prior loops. The latest repository max for this pair is loop 140, so this run continues as `R5/C19 loop 141`.

This loop avoids the visible top-covered C19 names in the index and uses three new C19 tuples:

- `069960 현대백화점`
- `139480 이마트`
- `383220 F&F`

---

## 1. Research thesis

C19 is not simply “brand” or “retail.” It is the narrow bridge:

```text
inventory normalization / sell-through / markdown discipline
→ gross-margin and operating-margin repair
→ cash-flow or valuation rerating
→ price path alignment
```

This loop splits the retail universe into three routes.

1. **Department-store/value-up margin buffer**  
   A retail name can re-rate if the market believes inventory, margin, dividend/value-up, and cash discipline are improving. This can be Stage2-Actionable, but it still needs margin proof.

2. **Hypermarket restructuring label without durable margin bridge**  
   A turnaround headline can produce a local spike, but if operating leverage is not confirmed, the path decays.

3. **Apparel brand inventory spike decay**  
   A brand name or short squeeze can produce an intraday/short-window spike. If sell-through and China/channel inventory are not fixed, this should not become Green.

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
069960:
  name: 현대백화점
  corporate_action_candidate_count: 0
  calibration_caveat: clean

139480:
  name: 이마트
  corporate_action_candidate_count: 0
  calibration_caveat: clean

383220:
  name: F&F
  corporate_action_candidate_dates: [2022-04-13]
  relevant_window_after_candidate: true
```

---

## 3. Trigger rows

```jsonl
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","round":"R5","loop":141,"large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C19_BRAND_RETAIL_INVENTORY_MARGIN","fine_archetype_id":"DEPARTMENT_STORE_VALUEUP_INVENTORY_MARGIN_BUFFER_POSITIVE_WITH_4B_WATCH","symbol":"069960","name":"현대백화점","trigger_type":"Stage2-Actionable","entry_date":"2024-01-29","entry_close":51200,"price_basis":"tradable_raw","mfe_30d_pct":20.90,"mae_30d_pct":-7.42,"mfe_90d_pct":20.90,"mae_90d_pct":-5.86,"mfe_180d_pct":20.90,"mae_180d_pct":-10.45,"forward_high_30d":61900,"forward_low_30d":47400,"forward_high_90d":61900,"forward_low_90d":48200,"forward_high_180d":61900,"forward_low_180d":45850,"calibration_usable":true,"case_role":"positive_with_margin_watch","novelty_key":"C19_BRAND_RETAIL_INVENTORY_MARGIN|069960|Stage2-Actionable|2024-01-29","non_price_bridge":"department-store value-up / retail margin buffer / inventory discipline candidate","score_alignment":"Stage2 may open, but Stage3-Green requires confirmed margin and cash conversion bridge"}
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","round":"R5","loop":141,"large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C19_BRAND_RETAIL_INVENTORY_MARGIN","fine_archetype_id":"HYPERMARKET_RESTRUCTURING_TURNAROUND_LABEL_LOW_MFE_HIGH_MAE","symbol":"139480","name":"이마트","trigger_type":"Stage2-Watch","entry_date":"2024-01-29","entry_close":80900,"price_basis":"tradable_raw","mfe_30d_pct":9.39,"mae_30d_pct":-10.38,"mfe_90d_pct":9.39,"mae_90d_pct":-21.76,"mfe_180d_pct":9.39,"mae_180d_pct":-31.77,"forward_high_30d":88500,"forward_low_30d":72500,"forward_high_90d":88500,"forward_low_90d":63300,"forward_high_180d":88500,"forward_low_180d":55200,"calibration_usable":true,"case_role":"turnaround_label_counterexample","novelty_key":"C19_BRAND_RETAIL_INVENTORY_MARGIN|139480|Stage2-Watch|2024-01-29","non_price_bridge":"hypermarket restructuring and retail turnaround label without durable margin/cash proof","score_alignment":"cap Stage2; if inventory and operating leverage are not refreshed, route to false-positive block"}
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","round":"R5","loop":141,"large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C19_BRAND_RETAIL_INVENTORY_MARGIN","fine_archetype_id":"APPAREL_BRAND_INVENTORY_SHORT_SPIKE_DECAY_FALSE_POSITIVE","symbol":"383220","name":"F&F","trigger_type":"Stage2-FalsePositive","entry_date":"2024-07-17","entry_close":74000,"price_basis":"tradable_raw","mfe_30d_pct":3.24,"mae_30d_pct":-33.99,"mfe_90d_pct":3.24,"mae_90d_pct":-33.99,"mfe_180d_pct":3.24,"mae_180d_pct":-33.99,"forward_high_30d":76400,"forward_low_30d":48850,"forward_high_90d":76400,"forward_low_90d":48850,"forward_high_180d":76400,"forward_low_180d":48850,"calibration_usable":true,"case_role":"hard_counterexample","novelty_key":"C19_BRAND_RETAIL_INVENTORY_MARGIN|383220|Stage2-FalsePositive|2024-07-17","non_price_bridge":"apparel brand spike without sell-through, China/channel inventory, or margin bridge refresh","score_alignment":"do not reward vertical price-only spike; block Stage2-Actionable"}
```

---

## 4. Case analysis

### 4.1 Hyundai Department Store / 069960 — margin-buffer positive, not automatic Green

`현대백화점` provides the positive side of this loop. From 2024-01-29, the stock reached 61,900 and held drawdown inside roughly -10% through the longer validation window.

```yaml
entry_close: 51200
30d_high: 61900
30d_low: 47400
90d_high: 61900
90d_low: 48200
180d_high: 61900
180d_low: 45850
mfe_30d_pct: 20.90
mae_30d_pct: -7.42
mfe_180d_pct: 20.90
mae_180d_pct: -10.45
```

Interpretation:

```text
classification = Stage2-Actionable with margin watch
```

The department-store/value-up route can work. But C19 should not graduate it to Stage3-Green unless margin, inventory discipline, duty-free exposure, and cash conversion are refreshed.

---

### 4.2 E-Mart / 139480 — restructuring label with weak durable conversion

`이마트` is a warning case. The early move after 2024-01-29 had some upside, but MFE stayed below +10 and the longer drawdown became large.

```yaml
entry_close: 80900
30d_high: 88500
30d_low: 72500
90d_high: 88500
90d_low: 63300
180d_high: 88500
180d_low: 55200
mfe_90d_pct: 9.39
mae_90d_pct: -21.76
mfe_180d_pct: 9.39
mae_180d_pct: -31.77
```

Interpretation:

```text
classification = Stage2-Watch / turnaround-label counterexample
```

Retail restructuring is not the same as retail margin recovery. C19 should require store-level margin, inventory turnover, online-loss reduction, or cash conversion proof.

---

### 4.3 F&F / 383220 — apparel brand spike decay

`F&F` is the hard counterexample. The stock produced a very visible one-day spike, but after the 2024-07-17 entry close, forward MFE was only +3.24 while MAE moved below -30%.

```yaml
entry_close: 74000
30d_high: 76400
30d_low: 48850
90d_high: 76400
90d_low: 48850
180d_high: 76400
180d_low: 48850
mfe_90d_pct: 3.24
mae_90d_pct: -33.99
```

Interpretation:

```text
classification = Stage2-FalsePositive
```

This is the classic C19 trap: brand equity is not inventory sell-through. Without China/channel inventory repair, markdown control, or margin revision, a price spike should not be learned as a positive.

---

## 5. Score-return alignment

```yaml
new_independent_case_count: 3
new_visible_C19_symbol_count: 3
same_archetype_new_trigger_family_count: 3
calibration_usable_case_count: 3
calibration_usable_trigger_count: 3
positive_case_count: 1
counterexample_count: 2
current_profile_error_count: 2
```

| symbol | role | 30D MFE/MAE | 90D MFE/MAE | 180D MFE/MAE | lesson |
|---|---:|---:|---:|---:|---|
| 069960 | positive with margin watch | +20.90 / -7.42 | +20.90 / -5.86 | +20.90 / -10.45 | department-store margin/value-up can work |
| 139480 | turnaround-label counterexample | +9.39 / -10.38 | +9.39 / -21.76 | +9.39 / -31.77 | restructuring label without margin bridge fails |
| 383220 | hard counterexample | +3.24 / -33.99 | +3.24 / -33.99 | +3.24 / -33.99 | apparel brand spike is not inventory repair |

---

## 6. Raw component score breakdown

```jsonl
{"row_type":"score_simulation","symbol":"069960","raw_EPS_revision_bridge":2,"raw_visibility":3,"raw_inventory_turnover":2,"raw_margin_bridge":2,"raw_cash_conversion":2,"raw_validation":3,"raw_info_edge":1,"stage2_actionable_bonus_before":2.0,"stage2_actionable_bonus_after":2.0,"simulated_route":"Stage2-Actionable-with-margin-watch"}
{"row_type":"score_simulation","symbol":"139480","raw_EPS_revision_bridge":0,"raw_visibility":3,"raw_inventory_turnover":1,"raw_margin_bridge":0,"raw_cash_conversion":1,"raw_validation":0,"raw_info_edge":1,"stage2_actionable_bonus_before":2.0,"stage2_actionable_bonus_after":0.0,"simulated_route":"Stage2-Watch-turnaround-label-counterexample"}
{"row_type":"score_simulation","symbol":"383220","raw_EPS_revision_bridge":0,"raw_visibility":3,"raw_inventory_turnover":0,"raw_margin_bridge":0,"raw_cash_conversion":0,"raw_validation":0,"raw_info_edge":2,"stage2_actionable_bonus_before":2.0,"stage2_actionable_bonus_after":0.0,"simulated_route":"Stage2-FalsePositive-price-spike-decay"}
```

---

## 7. Current calibrated profile stress test

### Existing error risk

C19 can over-reward:

```text
brand name
+ retail restructuring headline
+ value-up or one-day spike
```

That is too broad. Retail margin is not a slogan; it is inventory turning into cash without markdown leakage. A store can look crowded while the warehouse still leaks profit through discounting.

### Rule candidate

```text
C19_INVENTORY_MARGIN_CASH_BRIDGE_REQUIREMENT

if C19
and brand_or_retail_turnaround_label == true
and inventory_turnover_or_sellthrough_bridge == false
and gross_margin_or_operating_margin_bridge == false:
    stage2_actionable_bonus = 0
    max_stage = Stage2-Watch
```

```text
if C19
and MFE_90D_pct < +10
and MAE_90D_pct <= -20
and margin_cash_bridge_refreshed == false:
    Stage2_FalsePositive_Block = true
```

```text
if C19
and department_store_or_retail_valueup_label == true
and MFE_90D_pct >= +15
and MAE_90D_pct > -12:
    keep_stage2_actionable_bonus = true
    block_stage3_green_until_margin_cash_refresh = true
```

```text
if C19
and apparel_brand_price_spike == true
and MFE_30D_pct < +10
and MAE_30D_pct <= -25:
    route = Stage2_FalsePositive_Block
    do_not_learn_price_only_spike = true
```

---

## 8. Residual contribution summary

```yaml
do_not_propose_new_weight_delta: false
sector_specific_rule_candidate: false
canonical_archetype_rule_candidate: true
loop_contribution_label: canonical_archetype_rule_candidate
new_axis_proposed: C19_BRAND_SPIKE_AND_RESTRUCTURING_LABEL_STAGE2_BLOCK
existing_axis_strengthened:
  - C19_inventory_turnover_sellthrough_margin_bridge_requirement
  - C19_department_store_valueup_margin_buffer_escape_hatch
  - C19_hypermarket_restructuring_label_without_margin_bridge_stage2_cap
  - C19_apparel_brand_price_only_spike_false_positive_block
existing_axis_weakened: null
```

---

## 9. Next recommended archetypes

```text
C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION
C27_CONTENT_IP_GLOBAL_MONETIZATION
C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK
R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION
C19_BRAND_RETAIL_INVENTORY_MARGIN_retest_with_convenience_store_controls
```
