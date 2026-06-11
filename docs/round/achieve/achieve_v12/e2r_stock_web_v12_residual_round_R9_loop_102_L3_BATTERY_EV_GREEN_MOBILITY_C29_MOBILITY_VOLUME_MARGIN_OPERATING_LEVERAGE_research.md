# E2R v12 residual calibration research

## 0. Execution metadata

```yaml
schema_family: v12_sector_archetype_residual
selected_round: R9
selected_loop: 102
large_sector_id: L3_BATTERY_EV_GREEN_MOBILITY
canonical_archetype_id: C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE
fine_archetype_id: OEM_HYBRID_MIX_MARGIN_LEVERAGE_VS_AUTO_PARTS_THEME_BLOWOFF
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

`C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE` is still very thin in the no-repeat index: 3 rows / 3 symbols. The visible top-covered symbols are `005710`, `007860`, and `033530`, so this loop adds new C29 tuples: `000270`, `204320`, `010690`.

The previous local C29 pass reached loop 101. This run continues as loop 102.

---

## 1. Research thesis

C29 is not “auto stock.” It is:

```text
vehicle volume / product mix / price discipline
→ operating leverage or margin resilience
→ listed-company price path validation
```

The useful split in this loop:

- **OEM mix-margin leverage:** Kia showed a powerful OEM rerating path after strong profitability and powertrain/mix expectations.
- **Subsystem/ADAS supplier leverage:** HL Mando showed tradable upside, but supplier stocks require margin and customer-volume refresh because drawdowns can reappear.
- **Auto-parts theme blowoff:** Hwashin showed high MFE but very deep MAE. Without durable customer-volume/margin bridge, the signal is a 4B-to-block case rather than Stage3-Green.

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
000270:
  name: 기아
  corporate_action_candidate_dates: [1999-03-05, 1999-04-21, 1999-07-16]
  relevant_window_after_candidate: true
  case_role: OEM positive-control

204320:
  name: HL만도
  corporate_action_candidate_dates: [2018-05-08]
  relevant_window_after_candidate: true
  case_role: subsystem supplier positive-with-watch

010690:
  name: 화신
  corporate_action_candidate_dates: [1996-01-03, 1997-01-03, 2001-04-23]
  relevant_window_after_candidate: true
  case_role: auto-parts theme blowoff counterexample
```

---

## 3. Trigger rows

```jsonl
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","round":"R9","loop":102,"large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"OEM_PRODUCT_MIX_AND_MARGIN_LEVERAGE_POSITIVE_CONTROL","symbol":"000270","name":"기아","trigger_type":"Stage2-Actionable","entry_date":"2024-01-25","entry_close":93000,"price_basis":"tradable_raw","mfe_30d_pct":41.61,"mae_30d_pct":-7.42,"mfe_90d_pct":45.16,"mae_90d_pct":-7.42,"mfe_180d_pct":45.16,"mae_180d_pct":-7.42,"forward_high_30d":131700,"forward_low_30d":86100,"forward_high_90d":135000,"forward_low_90d":86100,"forward_high_180d":135000,"forward_low_180d":86100,"calibration_usable":true,"case_role":"positive_control","novelty_key":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE|000270|Stage2-Actionable|2024-01-25","non_price_bridge":"OEM profitability, product mix and shareholder return / powertrain mix context","score_alignment":"clean C29 positive; keep Stage2-Actionable and allow Stage3-Yellow path when margin/mix evidence is refreshed"}
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","round":"R9","loop":102,"large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"ADAS_STEERING_BRAKE_SUBSYSTEM_SUPPLIER_LEVERAGE_WITH_REFRESH_REQUIREMENT","symbol":"204320","name":"HL만도","trigger_type":"Stage2-Actionable","entry_date":"2024-04-29","entry_close":38350,"price_basis":"tradable_raw","mfe_30d_pct":30.38,"mae_30d_pct":-5.48,"mfe_90d_pct":30.38,"mae_90d_pct":-19.56,"mfe_180d_pct":30.38,"mae_180d_pct":-19.56,"forward_high_30d":50000,"forward_low_30d":36250,"forward_high_90d":50000,"forward_low_90d":30850,"forward_high_180d":50000,"forward_low_180d":30850,"calibration_usable":true,"case_role":"positive_with_watch","novelty_key":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE|204320|Stage2-Actionable|2024-04-29","non_price_bridge":"auto subsystem/ADAS supplier leverage, but drawdown requires order/customer-volume/margin refresh","score_alignment":"Stage2 may open; block Stage3-Green if margin/customer-volume bridge is not refreshed"}
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","round":"R9","loop":102,"large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"AUTO_PARTS_THEME_BLOWOFF_WITHOUT_DURABLE_VOLUME_MARGIN_BRIDGE","symbol":"010690","name":"화신","trigger_type":"Stage2-Watch","entry_date":"2024-06-12","entry_close":11690,"price_basis":"tradable_raw","mfe_30d_pct":35.93,"mae_30d_pct":-4.53,"mfe_90d_pct":35.93,"mae_90d_pct":-30.28,"mfe_180d_pct":35.93,"mae_180d_pct":-47.39,"forward_high_30d":15890,"forward_low_30d":11160,"forward_high_90d":15890,"forward_low_90d":8150,"forward_high_180d":15890,"forward_low_180d":6150,"calibration_usable":true,"case_role":"counterexample_4B_to_block","novelty_key":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE|010690|Stage2-Watch|2024-06-12","non_price_bridge":"auto-parts theme/volume label without durable customer-volume margin bridge","score_alignment":"vertical MFE but deep MAE; route to local 4B then block if no bridge refresh"}
```

---

## 4. Case analysis

### 4.1 Kia / 000270 — OEM mix-margin positive-control

Kia is the clean C29 control in this loop. The price path from 2024-01-25 confirms that the market rewarded OEM profitability, mix and powertrain expectations.

```yaml
entry_date: 2024-01-25
entry_close: 93000
30d_high: 131700
30d_low: 86100
90d_high: 135000
90d_low: 86100
180d_high: 135000
180d_low: 86100
mfe_30d_pct: 41.61
mae_30d_pct: -7.42
mfe_90d_pct: 45.16
mae_90d_pct: -7.42
mfe_180d_pct: 45.16
mae_180d_pct: -7.42
```

Interpretation:

```text
classification = Stage2-Actionable positive-control
```

This case strengthens the OEM escape hatch. If profitability, mix, payout or powertrain strategy is already visible and the price path has high MFE with manageable MAE, C29 should not be blocked merely because the sector faces EV-demand uncertainty.

---

### 4.2 HL Mando / 204320 — subsystem supplier leverage, but needs refresh

HL Mando produced a tradable move from 2024-04-29. The stock reached 50,000 by 2024-06-05, a +30.38% MFE. This is a real Stage2 candidate because subsystem suppliers can benefit from platform volume, ADAS, steering, braking and customer mix.

But by 2024-09-09 the stock printed 30,850, making MAE almost -20%. That prevents clean Green scoring.

```yaml
entry_date: 2024-04-29
entry_close: 38350
30d_high: 50000
30d_low: 36250
90d_high: 50000
90d_low: 30850
180d_high: 50000
180d_low: 30850
mfe_30d_pct: 30.38
mae_30d_pct: -5.48
mfe_90d_pct: 30.38
mae_90d_pct: -19.56
mfe_180d_pct: 30.38
mae_180d_pct: -19.56
```

Interpretation:

```text
classification = Stage2-Actionable with 4B watch
```

The supplier bridge worked, but the belt loosened later. C29 should require refreshed customer-volume, margin and backlog evidence before Stage3-Green.

---

### 4.3 Hwashin / 010690 — auto-parts theme blowoff

Hwashin is the counterexample. It had a spectacular short-window MFE after 2024-06-12, but the price path later collapsed. That means the signal was not durable operating leverage.

```yaml
entry_date: 2024-06-12
entry_close: 11690
30d_high: 15890
30d_low: 11160
90d_high: 15890
90d_low: 8150
180d_high: 15890
180d_low: 6150
mfe_30d_pct: 35.93
mae_30d_pct: -4.53
mfe_90d_pct: 35.93
mae_90d_pct: -30.28
mfe_180d_pct: 35.93
mae_180d_pct: -47.39
```

Interpretation:

```text
classification = local_4B_watch_then_block_without_bridge_refresh
```

This is not a simple low-MFE false positive. It is more dangerous: high MFE can fool the score into calling a theme spike a winner. The correct C29 treatment is local 4B watch at first, then hard cap if customer-volume and margin bridge fail to refresh.

---

## 5. Score-return alignment

```yaml
new_independent_case_count: 3
new_visible_C29_symbol_count: 3
same_archetype_new_trigger_family_count: 3
calibration_usable_case_count: 3
calibration_usable_trigger_count: 3
positive_case_count: 2
counterexample_count: 1
current_profile_error_count: 2
```

| symbol | role | 30D MFE/MAE | 90D MFE/MAE | 180D MFE/MAE | lesson |
|---|---:|---:|---:|---:|---|
| 000270 | OEM positive-control | +41.61 / -7.42 | +45.16 / -7.42 | +45.16 / -7.42 | OEM mix/margin bridge can be cleanly positive |
| 204320 | supplier positive-with-watch | +30.38 / -5.48 | +30.38 / -19.56 | +30.38 / -19.56 | supplier leverage needs refresh before Green |
| 010690 | auto-parts blowoff counterexample | +35.93 / -4.53 | +35.93 / -30.28 | +35.93 / -47.39 | vertical MFE should route to 4B then block without bridge |

---

## 6. Raw component score breakdown

```jsonl
{"row_type":"score_simulation","symbol":"000270","raw_EPS_revision_bridge":4,"raw_visibility":4,"raw_volume_mix_bridge":4,"raw_margin_bridge":4,"raw_validation":4,"raw_capital_return":2,"raw_info_edge":2,"stage2_actionable_bonus_before":2.0,"stage2_actionable_bonus_after":2.0,"simulated_route":"Stage2-Actionable-positive-control"}
{"row_type":"score_simulation","symbol":"204320","raw_EPS_revision_bridge":2,"raw_visibility":3,"raw_volume_mix_bridge":3,"raw_margin_bridge":2,"raw_validation":2,"raw_capital_return":0,"raw_info_edge":2,"stage2_actionable_bonus_before":2.0,"stage2_actionable_bonus_after":2.0,"simulated_route":"Stage2-Actionable-with-4B-watch"}
{"row_type":"score_simulation","symbol":"010690","raw_EPS_revision_bridge":1,"raw_visibility":2,"raw_volume_mix_bridge":2,"raw_margin_bridge":1,"raw_validation":0,"raw_capital_return":0,"raw_info_edge":2,"stage2_actionable_bonus_before":2.0,"stage2_actionable_bonus_after":0.0,"simulated_route":"4B-watch-then-Stage2-block"}
```

---

## 7. Current calibrated profile stress test

### Existing error risk

The profile can over-reward:

```text
auto parts + EV/hybrid/exports label + short-window vertical MFE
```

That is like hearing an engine rev and assuming the car is moving. C29 needs to see torque reaching the wheels: production volume, mix, margin, order quality, utilization and customer pull-through.

### Rule candidate

```text
C29_OEM_MIX_MARGIN_ESCAPE_HATCH

if C29
and OEM_profitability_or_mix_bridge == true
and MFE_90D_pct >= +25
and MAE_90D_pct > -15:
    keep_stage2_actionable_bonus = true
    allow_stage3_yellow_path = true
```

```text
C29_SUPPLIER_STAGE3_REFRESH_REQUIREMENT

if C29
and auto_supplier_volume_leverage == true
and MFE_30D_pct >= +20
and MAE_90D_pct <= -15
and refreshed_customer_volume_margin_bridge == false:
    local_4B_watch = true
    block_stage3_green = true
```

```text
C29_VERTICAL_AUTO_PARTS_BLOWOFF_BLOCK

if C29
and auto_parts_theme_spike == true
and MFE_30D_pct >= +30
and MAE_90D_pct <= -25
and company_specific_margin_bridge == false:
    stage2_actionable_bonus = 0
    route = local_4B_watch_then_Stage2_FalsePositive_Block
```

---

## 8. Residual contribution summary

```yaml
do_not_propose_new_weight_delta: false
sector_specific_rule_candidate: false
canonical_archetype_rule_candidate: true
loop_contribution_label: canonical_archetype_rule_candidate
new_axis_proposed: C29_VERTICAL_AUTO_PARTS_BLOWOFF_BLOCK
existing_axis_strengthened:
  - C29_company_specific_volume_mix_margin_bridge_requirement
  - C29_OEM_mix_margin_positive_escape_hatch
  - C29_supplier_customer_volume_margin_refresh_requirement
  - C29_vertical_MFE_auto_parts_blowoff_4B_to_block
existing_axis_weakened: null
```

---

## 9. Next recommended archetypes

```text
R13_CROSS_ARCHETYPE_4B_4C_REDTEAM
C19_BRAND_RETAIL_INVENTORY_MARGIN
C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION
C27_CONTENT_IP_GLOBAL_MONETIZATION
C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK
```
