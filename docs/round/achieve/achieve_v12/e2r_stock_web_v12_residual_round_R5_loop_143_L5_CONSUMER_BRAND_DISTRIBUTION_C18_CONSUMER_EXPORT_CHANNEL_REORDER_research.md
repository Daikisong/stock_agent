# E2R v12 residual calibration research

## 0. Execution metadata

```yaml
schema_family: v12_sector_archetype_residual
selected_round: R5
selected_loop: 143
large_sector_id: L5_CONSUMER_BRAND_DISTRIBUTION
canonical_archetype_id: C18_CONSUMER_EXPORT_CHANNEL_REORDER
fine_archetype_id: K_BEAUTY_ODM_EXPORT_REORDER_BRIDGE_VS_CHINA_PRESTIGE_CHANNEL_DECAY
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

`C18_CONSUMER_EXPORT_CHANNEL_REORDER` remains thin in the repo index: only 3 rows / 3 symbols. This session previously reinforced C18 with food/snack/ice-cream export cases, so this loop shifts the fine axis into K-beauty. The purpose is not to repeat a generic “K-beauty is hot” label, but to separate ODM/export reorder engines from legacy prestige/China channel decay.

The selected loop is `143` because the last local C18 run in this session reached loop 142, and the v12 pair rule increments the same round/canonical pair.

---

## 1. Research thesis

C18 asks whether consumer export interest becomes repeat channel orders. The engine is:

```text
global consumer demand
→ sell-through / reorder / distributor or ODM order pull
→ margin and revision bridge
→ durable price path
```

For K-beauty, the mechanism splits in two.

- **ODM/export reorder bridge**: global brands and indie labels need production capacity, formulation, packaging, regulatory execution, and repeat orders. This can benefit ODMs like Cosmax and Kolmar Korea.
- **legacy prestige / China-channel decay**: a brand can be famous but still fail if China prestige demand, travel retail, or old channel inventory weakens. This can make a K-beauty label a false positive.

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
192820:
  name: 코스맥스
  market: KOSPI
  corporate_action_candidate_count: 0
  calibration_caveat: clean

161890:
  name: 한국콜마
  market: KOSPI
  corporate_action_candidate_count: 0
  calibration_caveat: clean

090430:
  name: 아모레퍼시픽
  market: KOSPI
  corporate_action_candidate_count: 1
  corporate_action_candidate_dates: [2015-05-08]
  relevant_window_after_candidate: true
```

---

## 3. Trigger rows

```jsonl
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","round":"R5","loop":143,"large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C18_CONSUMER_EXPORT_CHANNEL_REORDER","fine_archetype_id":"K_BEAUTY_ODM_GLOBAL_REORDER_VERTICAL_MFE_WITH_4B_WATCH","symbol":"192820","name":"코스맥스","trigger_type":"Stage2-Actionable","entry_date":"2024-05-13","entry_close":157700,"price_basis":"tradable_raw","mfe_30d_pct":31.90,"mae_30d_pct":-6.28,"mfe_90d_pct":31.90,"mae_90d_pct":-26.44,"mfe_180d_pct":31.90,"mae_180d_pct":-26.44,"forward_high_30d":208000,"forward_low_30d":147800,"forward_high_90d":208000,"forward_low_90d":116000,"forward_high_180d":208000,"forward_low_180d":116000,"calibration_usable":true,"case_role":"positive_with_local_4B_watch","novelty_key":"C18_CONSUMER_EXPORT_CHANNEL_REORDER|192820|Stage2-Actionable|2024-05-13","non_price_bridge":"global K-beauty ODM/export reorder bridge; price path confirms vertical MFE but drawdown requires reorder/revision refresh","score_alignment":"keep Stage2-Actionable; block Stage3-Green until repeat-order/margin bridge refreshed"}
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","round":"R5","loop":143,"large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C18_CONSUMER_EXPORT_CHANNEL_REORDER","fine_archetype_id":"K_BEAUTY_ODM_REORDER_LOW_MAE_POSITIVE_CONTROL","symbol":"161890","name":"한국콜마","trigger_type":"Stage2-Actionable","entry_date":"2024-05-10","entry_close":55200,"price_basis":"tradable_raw","mfe_30d_pct":35.87,"mae_30d_pct":-10.51,"mfe_90d_pct":35.87,"mae_90d_pct":-10.51,"mfe_180d_pct":35.87,"mae_180d_pct":-10.51,"forward_high_30d":75000,"forward_low_30d":49400,"forward_high_90d":75000,"forward_low_90d":49400,"forward_high_180d":75000,"forward_low_180d":49400,"calibration_usable":true,"case_role":"positive_control","novelty_key":"C18_CONSUMER_EXPORT_CHANNEL_REORDER|161890|Stage2-Actionable|2024-05-10","non_price_bridge":"K-beauty ODM/export reorder bridge with strong MFE and contained MAE","score_alignment":"cleaner Stage2-Actionable; candidate Stage3-Yellow if margin/reorder evidence is refreshed"}
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","round":"R5","loop":143,"large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C18_CONSUMER_EXPORT_CHANNEL_REORDER","fine_archetype_id":"LEGACY_PRESTIGE_CHINA_CHANNEL_DECAY_FALSE_POSITIVE","symbol":"090430","name":"아모레퍼시픽","trigger_type":"Stage2-Watch","entry_date":"2024-05-20","entry_close":179700,"price_basis":"tradable_raw","mfe_30d_pct":11.58,"mae_30d_pct":-6.17,"mfe_90d_pct":11.58,"mae_90d_pct":-18.81,"mfe_180d_pct":11.58,"mae_180d_pct":-44.63,"forward_high_30d":200500,"forward_low_30d":168600,"forward_high_90d":200500,"forward_low_90d":145900,"forward_high_180d":200500,"forward_low_180d":99500,"calibration_usable":true,"case_role":"counterexample","novelty_key":"C18_CONSUMER_EXPORT_CHANNEL_REORDER|090430|Stage2-Watch|2024-05-20","non_price_bridge":"legacy beauty brand and China/prestige-channel exposure; early K-beauty label did not become durable reorder bridge","score_alignment":"cap Stage2; require non-China channel mix/reorder proof before Actionable"}
```

---

## 4. Case analysis

### 4.1 Cosmax / 192820 — ODM export reorder works, but 4B watch is needed

`Cosmax` is a C18 positive with a warning light. Entry 2024-05-13 close was 157,700. The stock reached 208,000 in June, producing a +31.90% MFE. This price path is consistent with a K-beauty ODM export/reorder thesis.

But the drawdown later reached 116,000 by August. That means the right calibration is not blind Stage3-Green. The order engine had torque, but the belt slipped. Reorder, margin, customer mix, and revision refresh are needed to keep the signal active.

```text
classification = Stage2-Actionable with local_4B_watch
reason = high MFE but high MAE without continuous reorder/margin refresh
```

### 4.2 Kolmar Korea / 161890 — cleaner ODM positive-control

`Kolmar Korea` gives a cleaner control row. Entry 2024-05-10 close was 55,200. The price reached 75,000 by June 19, while the worst low in the 30/90/180 window was 49,400. This is a much healthier positive: high MFE and tolerable MAE.

```text
classification = Stage2-Actionable positive-control
reason = ODM/reorder bridge aligns with price path and drawdown stays manageable
```

### 4.3 Amorepacific / 090430 — brand prestige and China channel can break C18

`Amorepacific` is the counterexample. It initially participated in the K-beauty move, but the 180D path fell deeply. Entry 2024-05-20 close was 179,700; the high was 200,500, but the forward low reached 99,500 by December.

This says a brand label is not equal to reorder. Legacy prestige exposure, China demand, travel retail, and inventory resets can break the channel bridge. In C18 scoring, broad brand awareness should be lower priority than sell-through, non-China channel expansion, margin recovery, and repeat orders.

```text
classification = Stage2-Watch / counterexample
reason = early brand momentum did not survive China/prestige-channel decay
```

---

## 5. Score-return alignment

```yaml
new_independent_case_count: 3
new_visible_C18_symbol_count: 3
same_archetype_new_trigger_family_count: 3
calibration_usable_case_count: 3
calibration_usable_trigger_count: 3
positive_case_count: 2
counterexample_count: 1
current_profile_error_count: 2
```

| symbol | role | 30D MFE/MAE | 90D MFE/MAE | 180D MFE/MAE | lesson |
|---|---:|---:|---:|---:|---|
| 192820 | positive + 4B watch | +31.90 / -6.28 | +31.90 / -26.44 | +31.90 / -26.44 | ODM export thesis worked, but drawdown needs reorder refresh |
| 161890 | positive-control | +35.87 / -10.51 | +35.87 / -10.51 | +35.87 / -10.51 | clean ODM/reorder price alignment |
| 090430 | counterexample | +11.58 / -6.17 | +11.58 / -18.81 | +11.58 / -44.63 | legacy prestige/China channel broke the bridge |

---

## 6. Raw component score breakdown

```jsonl
{"row_type":"score_simulation","symbol":"192820","raw_EPS_revision_bridge":3,"raw_visibility":4,"raw_export_channel":4,"raw_reorder_evidence":3,"raw_margin_bridge":2,"raw_validation":2,"raw_info_edge":2,"stage2_actionable_bonus_before":2.0,"stage2_actionable_bonus_after":2.0,"simulated_route":"Stage2-Actionable-with-4B-watch"}
{"row_type":"score_simulation","symbol":"161890","raw_EPS_revision_bridge":3,"raw_visibility":4,"raw_export_channel":4,"raw_reorder_evidence":3,"raw_margin_bridge":3,"raw_validation":3,"raw_info_edge":2,"stage2_actionable_bonus_before":2.0,"stage2_actionable_bonus_after":2.0,"simulated_route":"Stage2-Actionable-positive-control"}
{"row_type":"score_simulation","symbol":"090430","raw_EPS_revision_bridge":1,"raw_visibility":4,"raw_export_channel":2,"raw_reorder_evidence":1,"raw_margin_bridge":1,"raw_validation":1,"raw_info_edge":1,"stage2_actionable_bonus_before":2.0,"stage2_actionable_bonus_after":0.0,"simulated_route":"Stage2-Watch-counterexample"}
```

---

## 7. Current calibrated profile stress test

### Existing error risk

The profile can over-reward:

```text
K-beauty label
+ global export headline
+ famous brand
```

That is too broad. The actual C18 bridge is not fame. It is reorder. A brand name is a storefront sign; reorder is the cash register ringing again after the first crowd leaves.

### Strengthened C18 rule candidate

```text
C18_K_BEAUTY_REORDER_BRIDGE_REQUIREMENT

if C18
and K_beauty_global_export_label == true
and repeat_order_sellthrough_or_ODM_customer_pull == false
and margin_or_revision_bridge == false:
    stage2_actionable_bonus = 0
    max_stage = Stage2-Watch
```

### ODM escape hatch

```text
if C18
and ODM_export_customer_pull == true
and MFE_90D_pct >= +25
and MAE_90D_pct > -15:
    keep_stage2_actionable_bonus = true
    allow_stage3_yellow_path = true
```

### 4B watch for vertical ODM spike

```text
if C18
and MFE_30D_pct >= +30
and MAE_90D_pct <= -25
and refreshed_reorder_or_margin_bridge == false:
    local_4B_watch = true
    block_stage3_green = true
```

### Legacy China-channel cap

```text
if C18
and legacy_prestige_or_China_channel_exposure == true
and MFE_90D_pct < +15
and MAE_180D_pct <= -30:
    cap_stage2_actionable_bonus = true
    require_non_China_channel_mix_reorder_proof = true
```

---

## 8. Residual contribution summary

```yaml
do_not_propose_new_weight_delta: false
sector_specific_rule_candidate: false
canonical_archetype_rule_candidate: true
loop_contribution_label: canonical_archetype_rule_candidate
new_axis_proposed: C18_K_BEAUTY_ODM_REORDER_VS_CHINA_CHANNEL_DECAY
existing_axis_strengthened:
  - C18_repeat_order_sellthrough_or_ODM_customer_pull_requirement
  - C18_vertical_export_theme_local_4B_watch
  - C18_legacy_prestige_China_channel_stage2_cap
  - C18_ODM_export_customer_pull_escape_hatch
existing_axis_weakened: null
```

---

## 9. Next recommended archetypes

```text
C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE
C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE
R13_CROSS_ARCHETYPE_4B_4C_REDTEAM
C19_BRAND_RETAIL_INVENTORY_MARGIN
C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION
```
