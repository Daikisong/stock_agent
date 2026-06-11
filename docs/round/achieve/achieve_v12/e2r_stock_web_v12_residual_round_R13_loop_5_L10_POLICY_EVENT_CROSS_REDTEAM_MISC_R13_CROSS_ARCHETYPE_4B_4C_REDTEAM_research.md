# E2R v12 R13 cross-archetype residual calibration research

## 0. Execution metadata

```yaml
schema_family: v12_sector_archetype_residual
selected_round: R13
selected_loop: 5
large_sector_id: L10_POLICY_EVENT_CROSS_REDTEAM_MISC
canonical_archetype_id: R13_CROSS_ARCHETYPE_4B_4C_REDTEAM
fine_archetype_id: RECENT_C18_C26_C29_VERTICAL_MFE_ROUTE_SPLIT_LOCAL_4B_VS_HARD_4C
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

R13 is a cross-archetype checkpoint. This loop does not search for new sector-specific positives. It uses the most recent C18 / C26 / C29 outputs to retest the border between:

```text
local 4B watch
vs
hard 4C / Stage2 false-positive block
```

The prior local `R13_CROSS_ARCHETYPE_4B_4C_REDTEAM` pair reached loop 4, so this continuation is loop 5.

---

## 1. Research thesis

The current profile can still over-compress vertical price paths. A stock can jump sharply for a valid reason and still need local 4B watch. Another stock can jump sharply but collapse because the reason was only a label. A third stock may never show MFE at all and should move straight toward hard 4C or Stage2 block.

This loop uses six cases:

1. `000270 / C29 / Kia`: clean positive-control; hard 4C should be blocked.
2. `192820 / C18 / Cosmax`: vertical MFE with real ODM/export bridge, but 90D MAE requires local 4B.
3. `067160 / C26 / SOOP`: owned platform surface and rebrand MFE, but monetization refresh required.
4. `010690 / C29 / Hwashin`: auto-parts vertical MFE followed by collapse; local 4B should convert to block if bridge is absent.
5. `035720 / C26 / Kakao`: true platform structure but low MFE/high MAE; route to Stage2 cap / hard review.
6. `090430 / C18 / Amorepacific`: legacy brand/China-channel decay after early K-beauty participation; hard review if non-China reorder bridge is absent.

---

## 2. Validation scope

```yaml
validation_scope:
  required_cases: 6
  actual_cases: 6
  source_archetypes:
    - C18_CONSUMER_EXPORT_CHANNEL_REORDER
    - C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE
    - C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE
  price_windows:
    - 30D MFE/MAE
    - 90D MFE/MAE
    - 180D MFE/MAE
  aggregate_rule_goal:
    - distinguish local_4B_watch from hard_4C_review
    - prevent vertical MFE from being mistaken for Green
    - preserve direct-bridge positive controls
```

---

## 3. Trigger rows

```jsonl
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","round":"R13","loop":5,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_4B_4C_REDTEAM","fine_archetype_id":"OEM_MIX_MARGIN_POSITIVE_CONTROL_BLOCK_HARD_4C","source_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","symbol":"000270","name":"기아","trigger_type":"Stage2-Actionable","entry_date":"2024-01-25","entry_close":93000,"price_basis":"tradable_raw","mfe_30d_pct":41.61,"mae_30d_pct":-7.42,"mfe_90d_pct":45.16,"mae_90d_pct":-7.42,"mfe_180d_pct":45.16,"mae_180d_pct":-7.42,"forward_high_30d":131700,"forward_low_30d":86100,"forward_high_90d":135000,"forward_low_90d":86100,"forward_high_180d":135000,"forward_low_180d":86100,"calibration_usable":true,"case_role":"positive_control","novelty_key":"R13_CROSS_ARCHETYPE_4B_4C_REDTEAM|000270|Stage2-Actionable|2024-01-25","route":"block_hard_4C_keep_stage2","guardrail_lesson":"high MFE and controlled MAE with OEM margin/mix bridge should not be over-penalized"}
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","round":"R13","loop":5,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_4B_4C_REDTEAM","fine_archetype_id":"ODM_EXPORT_VERTICAL_MFE_LOCAL_4B_WATCH","source_archetype_id":"C18_CONSUMER_EXPORT_CHANNEL_REORDER","symbol":"192820","name":"코스맥스","trigger_type":"Stage2-Actionable","entry_date":"2024-05-13","entry_close":157700,"price_basis":"tradable_raw","mfe_30d_pct":31.90,"mae_30d_pct":-6.28,"mfe_90d_pct":31.90,"mae_90d_pct":-26.44,"mfe_180d_pct":31.90,"mae_180d_pct":-26.44,"forward_high_30d":208000,"forward_low_30d":147800,"forward_high_90d":208000,"forward_low_90d":116000,"forward_high_180d":208000,"forward_low_180d":116000,"calibration_usable":true,"case_role":"local_4B_watch","novelty_key":"R13_CROSS_ARCHETYPE_4B_4C_REDTEAM|192820|Stage2-Actionable|2024-05-13","route":"local_4B_watch_not_immediate_4C","guardrail_lesson":"real ODM export bridge plus vertical MFE deserves watch, but high MAE blocks Green until reorder/margin refresh"}
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","round":"R13","loop":5,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_4B_4C_REDTEAM","fine_archetype_id":"LIVE_PLATFORM_REBRAND_VERTICAL_MFE_LOCAL_4B_WATCH","source_archetype_id":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE","symbol":"067160","name":"SOOP","trigger_type":"Stage2-Actionable","entry_date":"2024-06-20","entry_close":117000,"price_basis":"tradable_raw","mfe_30d_pct":22.91,"mae_30d_pct":-18.38,"mfe_90d_pct":22.91,"mae_90d_pct":-26.07,"mfe_180d_pct":22.91,"mae_180d_pct":-32.82,"forward_high_30d":143800,"forward_low_30d":95500,"forward_high_90d":143800,"forward_low_90d":86500,"forward_high_180d":143800,"forward_low_180d":78600,"calibration_usable":true,"case_role":"local_4B_watch","novelty_key":"R13_CROSS_ARCHETYPE_4B_4C_REDTEAM|067160|Stage2-Actionable|2024-06-20","route":"local_4B_watch_then_hard_review_if_monetization_not_refreshed","guardrail_lesson":"owned platform surface and MFE keep Stage2 alive, but MAE requires ARPU/retention/monetization refresh"}
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","round":"R13","loop":5,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_4B_4C_REDTEAM","fine_archetype_id":"AUTO_PARTS_BLOWOFF_4B_TO_STAGE2_BLOCK","source_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","symbol":"010690","name":"화신","trigger_type":"Stage2-Watch","entry_date":"2024-06-12","entry_close":11690,"price_basis":"tradable_raw","mfe_30d_pct":35.93,"mae_30d_pct":-4.53,"mfe_90d_pct":35.93,"mae_90d_pct":-30.28,"mfe_180d_pct":35.93,"mae_180d_pct":-47.39,"forward_high_30d":15890,"forward_low_30d":11160,"forward_high_90d":15890,"forward_low_90d":8150,"forward_high_180d":15890,"forward_low_180d":6150,"calibration_usable":true,"case_role":"4B_to_block_counterexample","novelty_key":"R13_CROSS_ARCHETYPE_4B_4C_REDTEAM|010690|Stage2-Watch|2024-06-12","route":"local_4B_watch_then_Stage2_FalsePositive_Block","guardrail_lesson":"vertical auto-parts MFE should convert to hard block when margin/customer-volume bridge is absent"}
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","round":"R13","loop":5,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_4B_4C_REDTEAM","fine_archetype_id":"TRUE_PLATFORM_LOW_MFE_HIGH_MAE_HARD_REVIEW","source_archetype_id":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE","symbol":"035720","name":"카카오","trigger_type":"Stage2-Watch","entry_date":"2024-05-09","entry_close":48600,"price_basis":"tradable_raw","mfe_30d_pct":4.12,"mae_30d_pct":-13.48,"mfe_90d_pct":4.12,"mae_90d_pct":-32.30,"mfe_180d_pct":4.12,"mae_180d_pct":-33.02,"forward_high_30d":50600,"forward_low_30d":42050,"forward_high_90d":50600,"forward_low_90d":32900,"forward_high_180d":50600,"forward_low_180d":32550,"calibration_usable":true,"case_role":"hard_review_counterexample","novelty_key":"R13_CROSS_ARCHETYPE_4B_4C_REDTEAM|035720|Stage2-Watch|2024-05-09","route":"hard_4C_review_or_stage2_cap","guardrail_lesson":"even a true platform should be capped when ad/commerce leverage fails price validation"}
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","round":"R13","loop":5,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_4B_4C_REDTEAM","fine_archetype_id":"LEGACY_PRESTIGE_CHINA_CHANNEL_DECAY_HARD_REVIEW","source_archetype_id":"C18_CONSUMER_EXPORT_CHANNEL_REORDER","symbol":"090430","name":"아모레퍼시픽","trigger_type":"Stage2-Watch","entry_date":"2024-05-20","entry_close":179700,"price_basis":"tradable_raw","mfe_30d_pct":11.58,"mae_30d_pct":-6.17,"mfe_90d_pct":11.58,"mae_90d_pct":-18.81,"mfe_180d_pct":11.58,"mae_180d_pct":-44.63,"forward_high_30d":200500,"forward_low_30d":168600,"forward_high_90d":200500,"forward_low_90d":145900,"forward_high_180d":200500,"forward_low_180d":99500,"calibration_usable":true,"case_role":"hard_review_counterexample","novelty_key":"R13_CROSS_ARCHETYPE_4B_4C_REDTEAM|090430|Stage2-Watch|2024-05-20","route":"hard_4C_review_if_non_china_reorder_bridge_absent","guardrail_lesson":"brand prestige and K-beauty label need non-China reorder/margin evidence or the path decays"}
```

---

## 4. Case analysis

### 4.1 Kia / 000270 — positive-control, block hard 4C

Kia is the counterweight that prevents the red-team rule from becoming too punitive. The stock made high MFE with controlled drawdown from the selected entry. In route terms, this is not 4B or 4C; it is a positive control that says “do not kill a real OEM mix-margin signal.”

```text
route = keep_stage2_actionable
block_hard_4C = true
```

### 4.2 Cosmax / 192820 — local 4B, not immediate hard 4C

Cosmax had a real ODM/export bridge and high MFE. However, the forward drawdown was too large to graduate to Green. This is a bridge that worked, then buckled under load. The right response is not demolition; it is inspection.

```text
route = local_4B_watch
block_stage3_green = true
require_reorder_margin_refresh = true
```

### 4.3 SOOP / 067160 — platform surface with rebrand MFE, but monetization refresh required

SOOP has an owned live-streaming platform surface, so it is not an ad-agency label. The MFE validates that the market responded. But the MAE says the market later questioned durability.

```text
route = local_4B_watch
convert_to_hard_review_if_ARPU_retention_monetization_refresh_absent = true
```

### 4.4 Hwashin / 010690 — vertical MFE that should become hard block without bridge refresh

Hwashin is the dangerous archetype. It had high MFE, so price-only learning can mistakenly reward it. But the 90D and 180D collapse shows that the move was not durable operating leverage.

```text
route = local_4B_watch_then_Stage2_FalsePositive_Block
```

### 4.5 Kakao / 035720 — true platform can still be hard review

Kakao has a real platform surface, but this trigger path failed. Low MFE plus deep MAE means the platform structure did not convert into ad/commerce operating leverage during the validation window.

```text
route = hard_4C_review_or_stage2_cap
```

### 4.6 Amorepacific / 090430 — brand label cannot substitute for channel reorder

Amorepacific initially participated in K-beauty momentum but then decayed. Legacy prestige and China-channel exposure can neutralize global beauty headlines. Without non-China reorder and margin recovery, the case should not remain actionable.

```text
route = hard_4C_review_if_non_china_reorder_bridge_absent
```

---

## 5. Score-return alignment

```yaml
new_independent_case_count: 6
calibration_usable_case_count: 6
calibration_usable_trigger_count: 6
positive_control_count: 1
local_4B_watch_count: 2
hard_4C_or_stage2_block_count: 3
current_profile_error_count: 4
```

| symbol | source | route | 90D MFE/MAE | 180D MFE/MAE | lesson |
|---|---:|---:|---:|---:|---|
| 000270 | C29 | keep Stage2 / block hard 4C | +45.16 / -7.42 | +45.16 / -7.42 | real OEM margin bridge should survive red-team |
| 192820 | C18 | local 4B watch | +31.90 / -26.44 | +31.90 / -26.44 | ODM export bridge valid, but high MAE blocks Green |
| 067160 | C26 | local 4B watch | +22.91 / -26.07 | +22.91 / -32.82 | platform rebrand needs monetization refresh |
| 010690 | C29 | 4B then block | +35.93 / -30.28 | +35.93 / -47.39 | auto-parts blowoff should not become Green |
| 035720 | C26 | hard review / cap | +4.12 / -32.30 | +4.12 / -33.02 | true platform still failed ad-leverage validation |
| 090430 | C18 | hard review / cap | +11.58 / -18.81 | +11.58 / -44.63 | brand label decayed without reorder bridge |

---

## 6. Raw component score breakdown

```jsonl
{"row_type":"score_simulation","symbol":"000270","raw_EPS_revision_bridge":4,"raw_visibility":4,"raw_volume_or_reorder_bridge":4,"raw_margin_bridge":4,"raw_validation":4,"raw_info_edge":2,"stage2_actionable_bonus_before":2.0,"stage2_actionable_bonus_after":2.0,"simulated_route":"keep_Stage2_block_hard_4C"}
{"row_type":"score_simulation","symbol":"192820","raw_EPS_revision_bridge":3,"raw_visibility":4,"raw_volume_or_reorder_bridge":4,"raw_margin_bridge":2,"raw_validation":2,"raw_info_edge":2,"stage2_actionable_bonus_before":2.0,"stage2_actionable_bonus_after":2.0,"simulated_route":"local_4B_watch"}
{"row_type":"score_simulation","symbol":"067160","raw_EPS_revision_bridge":2,"raw_visibility":4,"raw_volume_or_reorder_bridge":3,"raw_margin_bridge":2,"raw_validation":2,"raw_info_edge":2,"stage2_actionable_bonus_before":2.0,"stage2_actionable_bonus_after":2.0,"simulated_route":"local_4B_watch"}
{"row_type":"score_simulation","symbol":"010690","raw_EPS_revision_bridge":1,"raw_visibility":2,"raw_volume_or_reorder_bridge":2,"raw_margin_bridge":1,"raw_validation":0,"raw_info_edge":2,"stage2_actionable_bonus_before":2.0,"stage2_actionable_bonus_after":0.0,"simulated_route":"4B_then_Stage2_false_positive_block"}
{"row_type":"score_simulation","symbol":"035720","raw_EPS_revision_bridge":1,"raw_visibility":4,"raw_volume_or_reorder_bridge":2,"raw_margin_bridge":0,"raw_validation":0,"raw_info_edge":1,"stage2_actionable_bonus_before":2.0,"stage2_actionable_bonus_after":0.0,"simulated_route":"hard_4C_review_or_stage2_cap"}
{"row_type":"score_simulation","symbol":"090430","raw_EPS_revision_bridge":1,"raw_visibility":4,"raw_volume_or_reorder_bridge":1,"raw_margin_bridge":1,"raw_validation":1,"raw_info_edge":1,"stage2_actionable_bonus_before":2.0,"stage2_actionable_bonus_after":0.0,"simulated_route":"hard_4C_review_or_stage2_cap"}
```

---

## 7. Current calibrated profile stress test

### Existing error risk

The profile can make two opposite mistakes:

1. **Over-blocking real bridges**  
   A real OEM, ODM, or platform bridge gets thrown into 4C because MAE is high.

2. **Over-rewarding vertical theme spikes**  
   A short-lived spike gets treated as a winning trigger because MFE is high.

The route split must behave like a triage desk:

```text
stable vital signs + real bridge -> keep Stage2
real bridge + high MAE -> local 4B watch
weak bridge + low MFE/high MAE -> hard 4C or Stage2 block
vertical MFE + collapse + no bridge refresh -> 4B then block
```

### Rule candidate

```text
R13_4B_4C_ROUTE_SPLIT_V5

if company_specific_bridge == true
and MFE_90D_pct >= +25
and MAE_90D_pct > -15:
    keep_stage2_actionable_bonus = true
    block_hard_4C = true
```

```text
if company_specific_bridge == true
and MFE_30D_pct >= +20
and MAE_90D_pct <= -20
and refreshed_bridge == false:
    route = local_4B_watch
    block_stage3_green = true
```

```text
if MFE_90D_pct < +10
and MAE_90D_pct <= -25
and company_specific_revenue_margin_cash_bridge == false:
    route = hard_4C_review_or_Stage2_FalsePositive_Block
    stage2_actionable_bonus = 0
```

```text
if MFE_30D_pct >= +30
and MAE_90D_pct <= -25
and refreshed_bridge == false:
    route = local_4B_watch_then_Stage2_FalsePositive_Block
    block_stage3_green = true
```

---

## 8. Residual contribution summary

```yaml
do_not_propose_new_weight_delta: false
sector_specific_rule_candidate: false
canonical_archetype_rule_candidate: false
cross_archetype_rule_candidate: true
loop_contribution_label: cross_archetype_4b_4c_redteam_guardrail_candidate
new_axis_proposed: R13_4B_4C_ROUTE_SPLIT_V5
existing_axis_strengthened:
  - block_hard_4C_for_real_positive_bridge
  - local_4B_watch_for_real_bridge_high_MAE
  - hard_4C_for_low_MFE_high_MAE_without_bridge
  - local_4B_then_block_for_vertical_MFE_without_refresh
existing_axis_weakened: null
```

---

## 9. Next recommended archetypes

```text
C19_BRAND_RETAIL_INVENTORY_MARGIN
C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION
C27_CONTENT_IP_GLOBAL_MONETIZATION
C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK
R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION
```
