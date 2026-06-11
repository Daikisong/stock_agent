# E2R v12 residual calibration research

## 0. Execution metadata

```yaml
schema_family: v12_sector_archetype_residual
selected_round: R8
selected_loop: 99
large_sector_id: L8_PLATFORM_CONTENT_SW_SECURITY
canonical_archetype_id: C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE
fine_archetype_id: LIVE_STREAMING_PLATFORM_GLOBAL_REBRAND_AND_TALK_AD_COMMERCE_LEVERAGE_VS_AD_AGENCY_LABEL
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

`C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE` remains extremely thin in the no-repeat index: 3 rows / 3 symbols. The visible top-covered symbols are `035420`, `042000`, `237820`, while the prior local C26 run used `035420`, `214270`, `216050`. This loop therefore adds visible-new C26 tuples: `067160`, `035720`, `030000`.

The selected loop is `99` because the previous local C26 run reached loop 98.

---

## 1. Research thesis

C26 is not “advertising company” and not “internet company.” It is about platform-level ad revenue operating leverage.

The core mechanism is:

```text
owned user graph / content feed / commerce surface
→ ad inventory or sponsored placement monetization
→ incremental revenue falls through operating profit
→ price path confirms rerating
```

The key split:

- **Platform ad/commerce surface:** owned traffic, first-party user data, creator ecosystem, or commerce placements can create operating leverage.
- **Ad agency / marketing service label:** can have digital marketing exposure but usually lacks the same owned-inventory ARPU flywheel.
- **Platform label with regulatory or content-overhang drag:** even a real platform can fail if ad/commerce monetization is offset by governance, content, mobility, or cost pressure.

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
067160:
  name: SOOP
  former_name: AfreecaTV
  relevant_window_after_old_corporate_actions: true
  note: 2024 name/platform transition visible in stock-web name history.

035720:
  name: 카카오
  relevant_window_after_2021 corporate-action candidate: true
  note: true platform company, but 2024 path failed from selected entry.

030000:
  name: 제일기획
  relevant_window_after_old corporate-action candidates: true
  note: ad/marketing company; not an owned ad-inventory platform.
```

---

## 3. Trigger rows

```jsonl
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","round":"R8","loop":99,"large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE","fine_archetype_id":"LIVE_STREAMING_PLATFORM_REBRAND_GLOBAL_EXPANSION_VERTICAL_MFE_WITH_4B_WATCH","symbol":"067160","name":"SOOP","trigger_type":"Stage2-Actionable","entry_date":"2024-06-20","entry_close":117000,"price_basis":"tradable_raw","mfe_30d_pct":22.91,"mae_30d_pct":-18.38,"mfe_90d_pct":22.91,"mae_90d_pct":-26.07,"mfe_180d_pct":22.91,"mae_180d_pct":-32.82,"forward_high_30d":143800,"forward_low_30d":95500,"forward_high_90d":143800,"forward_low_90d":86500,"forward_high_180d":143800,"forward_low_180d":78600,"calibration_usable":true,"case_role":"positive_with_local_4B_watch","novelty_key":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE|067160|Stage2-Actionable|2024-06-20","non_price_bridge":"owned live-streaming platform, rebrand/global expansion, creator/viewer monetization surface","score_alignment":"Stage2 may open, but high MAE requires platform monetization/retention refresh before Green"}
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","round":"R8","loop":99,"large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE","fine_archetype_id":"TALK_AD_COMMERCE_PLATFORM_LABEL_WITH_REGULATORY_CONTENT_OVERHANG_STAGE2_CAP","symbol":"035720","name":"카카오","trigger_type":"Stage2-Watch","entry_date":"2024-05-09","entry_close":48600,"price_basis":"tradable_raw","mfe_30d_pct":4.12,"mae_30d_pct":-13.48,"mfe_90d_pct":4.12,"mae_90d_pct":-32.30,"mfe_180d_pct":4.12,"mae_180d_pct":-33.02,"forward_high_30d":50600,"forward_low_30d":42050,"forward_high_90d":50600,"forward_low_90d":32900,"forward_high_180d":50600,"forward_low_180d":32550,"calibration_usable":true,"case_role":"platform_label_counterexample","novelty_key":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE|035720|Stage2-Watch|2024-05-09","non_price_bridge":"true platform/talk-commerce surface but 2024 price path did not validate ad operating leverage","score_alignment":"cap Stage2 until ad/commerce revenue bridge is visible and overhang pressure is reduced"}
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","round":"R8","loop":99,"large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE","fine_archetype_id":"AD_AGENCY_DIGITAL_MARKETING_LABEL_WITHOUT_OWNED_INVENTORY_ARPU_LEVERAGE","symbol":"030000","name":"제일기획","trigger_type":"Stage2-FalsePositive","entry_date":"2024-05-09","entry_close":19470,"price_basis":"tradable_raw","mfe_30d_pct":0.51,"mae_30d_pct":-6.88,"mfe_90d_pct":0.51,"mae_90d_pct":-10.38,"mfe_180d_pct":0.51,"mae_180d_pct":-13.82,"forward_high_30d":19570,"forward_low_30d":18130,"forward_high_90d":19570,"forward_low_90d":17450,"forward_high_180d":19570,"forward_low_180d":16780,"calibration_usable":true,"case_role":"counterexample","novelty_key":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE|030000|Stage2-FalsePositive|2024-05-09","non_price_bridge":"advertising agency/digital marketing label without owned user-feed ad inventory leverage","score_alignment":"do not award C26 Stage2-Actionable for agency label alone"}
```

---

## 4. Case analysis

### 4.1 SOOP / 067160 — platform rebrand produced MFE, but not Green

SOOP is the cleanest new C26 positive-with-watch case. The company owns a live-streaming platform surface, and 2024 was a transition year from AfreecaTV to SOOP, with a global platform/rebrand narrative.

Price path from 2024-06-20:

```yaml
entry_close: 117000
30d_high: 143800
30d_low: 95500
90d_high: 143800
90d_low: 86500
180d_high: 143800
180d_low: 78600
mfe_30d_pct: 22.91
mae_30d_pct: -18.38
mfe_90d_pct: 22.91
mae_90d_pct: -26.07
mfe_180d_pct: 22.91
mae_180d_pct: -32.82
```

Interpretation:

```text
classification = Stage2-Actionable with local_4B_watch
```

The signal worked enough to keep Stage2 alive. But the 90D/180D MAE says the platform rebrand alone cannot justify Green. The model should demand creator retention, viewer growth, ad/sponsorship ARPU, global service adoption, or paid-item revenue refresh. A platform is a marketplace of attention; the score should ask whether attention rents rose, not merely whether the signboard changed.

---

### 4.2 Kakao / 035720 — true platform, but the selected 2024 path failed

Kakao is not an ad agency. It is a true platform company with messenger, commerce, content, and other surfaces. That makes it a legitimate C26 candidate on structure.

But structure did not equal price validation at the selected trigger date.

```yaml
entry_close: 48600
30d_high: 50600
30d_low: 42050
90d_high: 50600
90d_low: 32900
180d_high: 50600
180d_low: 32550
mfe_30d_pct: 4.12
mae_30d_pct: -13.48
mfe_90d_pct: 4.12
mae_90d_pct: -32.30
mfe_180d_pct: 4.12
mae_180d_pct: -33.02
```

Interpretation:

```text
classification = Stage2-Watch / platform label counterexample
```

This is an important guardrail. Even a real platform should not receive C26 Actionable credit unless ad/commerce monetization is translating into operating leverage. The machinery may exist, but if other belts are dragging—content, regulation, cost, governance, subsidiary value, or weak ad demand—the flywheel does not spin.

---

### 4.3 Cheil Worldwide / 030000 — advertising agency label is not C26 platform leverage

Cheil is a major advertising and marketing company, but C26 is not “advertising exposure.” C26 requires owned platform inventory or platform-level ARPU expansion.

```yaml
entry_close: 19470
30d_high: 19570
30d_low: 18130
90d_high: 19570
90d_low: 17450
180d_high: 19570
180d_low: 16780
mfe_30d_pct: 0.51
mae_30d_pct: -6.88
mfe_90d_pct: 0.51
mae_90d_pct: -10.38
mfe_180d_pct: 0.51
mae_180d_pct: -13.82
```

Interpretation:

```text
classification = Stage2-FalsePositive
```

The signal never produced material MFE. This strengthens the rule that agency or marketing-service labels should not be upgraded into platform ad revenue operating leverage. An ad agency buys and builds campaigns; a platform owns the toll road.

---

## 5. Score-return alignment

```yaml
new_independent_case_count: 3
new_visible_C26_symbol_count: 3
same_archetype_new_trigger_family_count: 3
calibration_usable_case_count: 3
calibration_usable_trigger_count: 3
positive_case_count: 1
counterexample_count: 2
current_profile_error_count: 2
```

| symbol | role | 30D MFE/MAE | 90D MFE/MAE | 180D MFE/MAE | lesson |
|---|---:|---:|---:|---:|---|
| 067160 | positive + 4B watch | +22.91 / -18.38 | +22.91 / -26.07 | +22.91 / -32.82 | real platform surface, but rebrand needs monetization refresh |
| 035720 | platform counterexample | +4.12 / -13.48 | +4.12 / -32.30 | +4.12 / -33.02 | true platform but no 2024 ad-leverage validation |
| 030000 | agency-label counterexample | +0.51 / -6.88 | +0.51 / -10.38 | +0.51 / -13.82 | ad agency is not owned-platform operating leverage |

---

## 6. Raw component score breakdown

```jsonl
{"row_type":"score_simulation","symbol":"067160","raw_EPS_revision_bridge":2,"raw_visibility":4,"raw_owned_user_graph":4,"raw_ad_inventory_leverage":3,"raw_operating_leverage":2,"raw_validation":2,"raw_info_edge":2,"stage2_actionable_bonus_before":2.0,"stage2_actionable_bonus_after":2.0,"simulated_route":"Stage2-Actionable-with-4B-watch"}
{"row_type":"score_simulation","symbol":"035720","raw_EPS_revision_bridge":1,"raw_visibility":4,"raw_owned_user_graph":5,"raw_ad_inventory_leverage":2,"raw_operating_leverage":0,"raw_validation":0,"raw_info_edge":1,"stage2_actionable_bonus_before":2.0,"stage2_actionable_bonus_after":0.0,"simulated_route":"Stage2-Watch-platform-label-counterexample"}
{"row_type":"score_simulation","symbol":"030000","raw_EPS_revision_bridge":1,"raw_visibility":3,"raw_owned_user_graph":0,"raw_ad_inventory_leverage":1,"raw_operating_leverage":0,"raw_validation":0,"raw_info_edge":0,"stage2_actionable_bonus_before":1.0,"stage2_actionable_bonus_after":0.0,"simulated_route":"Stage2-FalsePositive"}
```

---

## 7. Current calibrated profile stress test

### Existing error risk

The current profile can over-reward:

```text
internet/platform keyword
or advertising/marketing keyword
or short-term rebrand spike
```

C26 needs a narrower gate. The model should ask whether the company owns the user attention surface and whether incremental ad/commerce revenue drops into operating profit.

### Rule candidate

```text
C26_OWNED_PLATFORM_AD_INVENTORY_OPERATING_LEVERAGE_REQUIREMENT

if C26
and platform_or_ad_label == true
and owned_user_graph_or_feed_inventory == false:
    stage2_actionable_bonus = 0
    max_stage = Stage2-Watch
```

```text
if C26
and owned_platform_surface == true
and ad_commerce_ARPU_or_operating_profit_bridge == false
and MFE_90D_pct < +10
and MAE_90D_pct <= -25:
    Stage2_FalsePositive_Block = true
```

```text
if C26
and owned_platform_surface == true
and MFE_30D_pct >= +20
and MAE_90D_pct <= -20:
    keep_stage2_actionable_bonus = true
    local_4B_watch = true
    block_stage3_green_until_monetization_refresh = true
```

---

## 8. Residual contribution summary

```yaml
do_not_propose_new_weight_delta: false
sector_specific_rule_candidate: false
canonical_archetype_rule_candidate: true
loop_contribution_label: canonical_archetype_rule_candidate
new_axis_proposed: C26_OWNED_PLATFORM_AD_INVENTORY_OPERATING_LEVERAGE_REQUIREMENT
existing_axis_strengthened:
  - C26_platform_level_ad_search_commerce_operating_leverage_escape_hatch
  - C26_ad_agency_or_marketing_service_label_stage2_block
  - C26_platform_label_without_ARPU_profit_bridge_stage2_cap
  - C26_rebrand_vertical_MFE_local_4B_watch
existing_axis_weakened: null
```

---

## 9. Next recommended archetypes

```text
C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE
R13_CROSS_ARCHETYPE_4B_4C_REDTEAM
C19_BRAND_RETAIL_INVENTORY_MARGIN
C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION
C27_CONTENT_IP_GLOBAL_MONETIZATION
```
