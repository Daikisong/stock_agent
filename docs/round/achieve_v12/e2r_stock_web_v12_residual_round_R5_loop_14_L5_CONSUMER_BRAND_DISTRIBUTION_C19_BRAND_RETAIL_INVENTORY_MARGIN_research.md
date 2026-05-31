# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```yaml
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
scheduled_round: R5
scheduled_loop: 14
round_schedule_status: valid
round_sector_consistency: pass
large_sector_id: L5_CONSUMER_BRAND_DISTRIBUTION
canonical_archetype_id: C19_BRAND_RETAIL_INVENTORY_MARGIN
fine_archetype_id: APPAREL_BRAND_AND_RETAIL_INVENTORY_MARGIN_BRIDGE
output_file: e2r_stock_web_v12_residual_round_R5_loop_14_L5_CONSUMER_BRAND_DISTRIBUTION_C19_BRAND_RETAIL_INVENTORY_MARGIN_research.md
price_source: Songdaiki/stock-web
stock_web_manifest_max_date: 2026-02-20
production_scoring_changed: false
shadow_weight_only: true
handoff_prompt_embedded: true
handoff_prompt_executed_now: false
```

This loop adds **4** new independent cases, **2** counterexamples, and **2** residual errors for **R5/L5_CONSUMER_BRAND_DISTRIBUTION/C19_BRAND_RETAIL_INVENTORY_MARGIN**.

## 1. Current Calibrated Profile Assumption

Current proxy profile is `e2r_2_1_stock_web_calibrated_proxy`.

```text
stage2_actionable_evidence_bonus = +2.0
stage3_yellow_total_min = 75.0
stage3_green_total_min = 87.0
stage3_green_revision_min = 55.0
stage3_cross_evidence_green_buffer = +1.5
price_only_blowoff_blocks_positive_stage = true
full_4b_requires_non_price_evidence = true
hard_4c_thesis_break_routes_to_4c = true
```

This file does **not** repeat the global calibration claim. It tests whether the consumer/brand/retail inventory-margin archetype needs a narrower shadow rule: brand or retail scale should not be promoted unless sell-through, inventory-turn, and margin bridge evidence move together.

## 2. Round / Large Sector / Canonical Archetype Scope

- Round: `R5`
- Loop: `14`
- Required sector: `L5_CONSUMER_BRAND_DISTRIBUTION`
- Canonical archetype: `C19_BRAND_RETAIL_INVENTORY_MARGIN`
- Fine archetype: `APPAREL_BRAND_AND_RETAIL_INVENTORY_MARGIN_BRIDGE`
- Scope: historical calibration only.
- Non-scope: no live scan, no stock recommendation, no production patch.

## 3. Previous Coverage / Duplicate Avoidance Check

Local and accessible research artifacts already include R5 loops for C18/C20, while C19 was still under-covered in the current generated v12 set. The immediately preceding generated MD completed `R4 / loop 14` and pointed the next state to `R5 / loop 14`; this file follows that scheduler state.

```text
scheduled_round = R5
scheduled_loop = 14
round_schedule_status = valid
round_sector_consistency = pass
same_canonical_archetype_research = allowed
same_symbol_same_trigger_date_research = blocked
new_symbol_count = 4
same_archetype_new_symbol_count = 4
new_trigger_family_count = 5
minimum_new_independent_case_ratio = 1.00
```

## 4. Stock-Web OHLC Input / Price Source Validation

`Songdaiki/stock-web` diagnostics report:

```text
source_name = FinanceData/marcap
source_repo_url = https://github.com/FinanceData/marcap
price_adjustment_status = raw_unadjusted_marcap
min_date = 1995-05-02
max_date = 2026-02-20
raw_row_count = 15214118
tradable_row_count = 14354401
symbol_count = 5414
active_like_symbol_count = 2868
inactive_or_delisted_like_symbol_count = 2546
calibration_shard_root = atlas/ohlcv_tradable_by_symbol_year
raw_shard_root = atlas/ohlcv_raw_by_symbol_year
```

Symbol profile validation:

| symbol | company | profile_path | first_date | last_date | corporate_action_candidate_dates | 180D status |
| --- | --- | --- | --- | --- | --- | --- |
| 383220 | F&F | atlas/symbol_profiles/383/383220.json | 2021-05-21 | 2026-02-20 | 2022-04-13 | clean after candidate; entry window starts 2022-05-17 |
| 111770 | 영원무역 | atlas/symbol_profiles/111/111770.json | 2009-07-30 | 2026-02-20 | none | clean |
| 105630 | 한세실업 | atlas/symbol_profiles/105/105630.json | 2009-03-20 | 2026-02-20 | 2011-11-30 | clean for 2022 window |
| 139480 | 이마트 | atlas/symbol_profiles/139/139480.json | 2011-06-10 | 2026-02-20 | none | clean |


## 5. Historical Eligibility Gate

All representative triggers pass:

```text
trigger_date_is_historical = true
entry_date_in_tradable_shard = true
forward_180D_available = true
high_low_close_volume_present = true
corporate_action_contaminated_180D_window = false
calibration_usable = true
```

F&F has a 2022-04-13 corporate-action candidate in the stock-web profile, but the representative entry is 2022-05-17 and the 180D window is after the candidate date, so the representative window is kept usable with caveat.

## 6. Canonical Archetype Compression Map

```text
C19_BRAND_RETAIL_INVENTORY_MARGIN
  ├─ BRAND_SELLTHROUGH_MARGIN_BRIDGE
  │   └─ F&F: brand/product sell-through + margin bridge + contained MAE
  ├─ APPAREL_ORDER_MIX_MARGIN_BRIDGE
  │   └─ 영원무역: order/mix + FX/margin bridge, but moderate upside
  ├─ APPAREL_ORDER_HEADLINE_DESTOCKING_RISK
  │   └─ 한세실업: order headline failed when buyer inventory/destocking risk surfaced
  └─ RETAIL_SCALE_WITHOUT_MARGIN_QUALITY
      └─ 이마트: scale/reopening narrative without inventory-turn or margin-quality proof
```

C19 is not just “consumer brand exposure.” It behaves like a warehouse conveyor belt: product demand enters, inventory turns, gross margin survives, and earnings revision exits. If the belt stops at “retail scale” or “orders look good,” the later price path often becomes a trapdoor.

## 7. Case Selection Summary

| case_id | symbol | company_name | case_type | positive_or_counterexample | best_trigger | current_profile_verdict | score_price_alignment |
| --- | --- | --- | --- | --- | --- | --- | --- |
| R5L14_C19_POS_FNF_202205_Q1_BRAND_INVENTORY_MARGIN | 383220 | F&F | structural_success | positive | T_FNF_20220517_STAGE2_ACTIONABLE | current_profile_correct | positive_alignment_with_controlled_MAE |
| R5L14_C19_POS_YOUNGONE_202208_Q2_ORDER_MARGIN_BRIDGE | 111770 | 영원무역 | structural_success | positive | T_YOUNGONE_20220817_STAGE2_ACTIONABLE | current_profile_correct | moderate_positive_alignment |
| R5L14_C19_NEG_HANSAE_202205_ORDER_HEADLINE_DESTOCKING | 105630 | 한세실업 | failed_rerating | counterexample | T_HANSAE_20220517_FALSE_STAGE2 | current_profile_false_positive | negative_alignment_high_MAE |
| R5L14_C19_NEG_EMART_202108_RETAIL_MARGIN_HEADLINE | 139480 | 이마트 | failed_rerating | counterexample | T_EMART_20210810_FALSE_STAGE2 | current_profile_false_positive | weak_MFE_large_drawdown |


## 8. Positive vs Counterexample Balance

| balance_item | count | notes |
| --- | --- | --- |
| positive_structural_success | 2 | F&F, 영원무역 |
| counterexample_or_failed_rerating | 2 | 한세실업, 이마트 |
| 4B_or_4C_case | 2 | F&F 4B overlay, 한세실업 4C thesis-break |
| calibration_usable_case_count | 4 | all representative cases clean |
| calibration_usable_trigger_count | 6 | four representative triggers plus two overlay triggers |


## 9. Evidence Source Map

| case | Stage2 evidence | Stage3 evidence | 4B evidence | 4C evidence |
| --- | --- | --- | --- | --- |
| F&F | brand sell-through, channel/order quality, early revision | margin bridge and financial visibility | valuation/positioning overlay after rerating | not triggered in representative entry |
| 영원무역 | order/mix and FX-supported margin bridge | confirmed margin bridge, financial visibility | watch only | not triggered |
| 한세실업 | order headline and FX optimism | absent; margin bridge not durable | destocking / margin slowdown | buyer inventory / thesis-break path |
| 이마트 | retail scale and reopening headline | absent; inventory-turn not proven | margin-quality slowdown | retail thesis break after weak path |


## 10. Price Data Source Map

| symbol | entry shard | profile path | price basis | adjustment |
| --- | --- | --- | --- | --- |
| 383220 | atlas/ohlcv_tradable_by_symbol_year/383/383220/2022.csv | atlas/symbol_profiles/383/383220.json | tradable_raw | raw_unadjusted_marcap |
| 111770 | atlas/ohlcv_tradable_by_symbol_year/111/111770/2022.csv | atlas/symbol_profiles/111/111770.json | tradable_raw | raw_unadjusted_marcap |
| 105630 | atlas/ohlcv_tradable_by_symbol_year/105/105630/2022.csv | atlas/symbol_profiles/105/105630.json | tradable_raw | raw_unadjusted_marcap |
| 139480 | atlas/ohlcv_tradable_by_symbol_year/139/139480/2021.csv | atlas/symbol_profiles/139/139480.json | tradable_raw | raw_unadjusted_marcap |


## 11. Case-by-Case Trigger Grid

| trigger_id | symbol | company_name | trigger_type | trigger_date | entry_date | entry_price | MFE_90D_pct | MAE_90D_pct | MFE_180D_pct | MAE_180D_pct | current_profile_verdict | trigger_outcome_label | aggregate_group_role |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| T_FNF_20220517_STAGE2_ACTIONABLE | 383220 | F&F | Stage2-Actionable | 2022-05-16 | 2022-05-17 | 131500 | 26.62 | -7.98 | 26.62 | -8.37 | current_profile_correct | structural_success_inventory_margin_bridge | representative |
| T_FNF_20221206_4B_INVENTORY_VALUATION_OVERLAY | 383220 | F&F | Stage4B-Overlay | 2022-12-06 | 2022-12-06 | 155000 | 6.77 | -22.26 | 6.77 | -24.64 | current_profile_correct | 4B_overlay_success | 4B_overlay_only |
| T_YOUNGONE_20220817_STAGE2_ACTIONABLE | 111770 | 영원무역 | Stage2-Actionable | 2022-08-16 | 2022-08-17 | 46000 | 14.13 | -9.46 | 14.13 | -9.57 | current_profile_correct | structural_success_moderate_MFE | representative |
| T_HANSAE_20220517_FALSE_STAGE2 | 105630 | 한세실업 | Stage2-Actionable | 2022-05-16 | 2022-05-17 | 24800 | 4.64 | -40.52 | 4.64 | -47.18 | current_profile_false_positive | false_positive_stage2_high_MAE | representative |
| T_HANSAE_20220519_4C_DESTOCKING_BREAK | 105630 | 한세실업 | Stage4C | 2022-05-19 | 2022-05-19 | 22700 | 2.2 | -35.02 | 2.2 | -42.29 | current_profile_4C_too_late | 4C_success | 4C_overlay_only |
| T_EMART_20210810_FALSE_STAGE2 | 139480 | 이마트 | Stage2-Actionable | 2021-08-10 | 2021-08-10 | 177000 | 3.11 | -13.84 | 3.11 | -31.36 | current_profile_false_positive | false_positive_stage2_weak_MFE_large_MAE | representative |


## 12. Trigger-Level OHLC Backtest Tables

### Representative entry triggers

| trigger_id | symbol | entry_date | entry_price | MFE_30D_pct | MAE_30D_pct | MFE_90D_pct | MAE_90D_pct | MFE_180D_pct | MAE_180D_pct | peak_date | peak_price | drawdown_after_peak_pct |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| T_FNF_20220517_STAGE2_ACTIONABLE | 383220 | 2022-05-17 | 131500 | 13.69 | -7.98 | 26.62 | -7.98 | 26.62 | -8.37 | 2022-08-02 | 166500 | -27.63 |
| T_YOUNGONE_20220817_STAGE2_ACTIONABLE | 111770 | 2022-08-17 | 46000 | 9.78 | -8.48 | 14.13 | -9.46 | 14.13 | -9.57 | 2022-11-14 | 52500 | -20.76 |
| T_HANSAE_20220517_FALSE_STAGE2 | 105630 | 2022-05-17 | 24800 | 4.64 | -33.27 | 4.64 | -40.52 | 4.64 | -47.18 | 2022-05-17 | 25950 | -49.52 |
| T_EMART_20210810_FALSE_STAGE2 | 139480 | 2021-08-10 | 177000 | 3.11 | -5.65 | 3.11 | -13.84 | 3.11 | -31.36 | 2021-08-17 | 182500 | -33.42 |


### Overlay / label-comparison triggers

| trigger_id | symbol | trigger_type | entry_date | entry_price | MFE_90D_pct | MAE_90D_pct | four_b_local_peak_proximity | four_b_full_window_peak_proximity | four_c_protection_label | aggregate_group_role |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| T_FNF_20221206_4B_INVENTORY_VALUATION_OVERLAY | 383220 | Stage4B-Overlay | 2022-12-06 | 155000 | 6.77 | -22.26 | 0.67 | 0.67 | thesis_break_watch_only | 4B_overlay_only |
| T_HANSAE_20220519_4C_DESTOCKING_BREAK | 105630 | Stage4C | 2022-05-19 | 22700 | 2.2 | -35.02 | null | null | hard_4c_success_if_triggered_early | 4C_overlay_only |


## 13. Current Calibrated Profile Stress Test

| case | current profile likely action | actual path | verdict |
| --- | --- | --- | --- |
| F&F | Promote to Stage2/Yellow and later Green if margin bridge confirms | positive MFE with contained 90D/180D MAE | current_profile_correct |
| 영원무역 | Promote to Stage2/Yellow, but keep Green strict | moderate positive MFE, low-to-mid MAE | current_profile_correct |
| 한세실업 | May over-promote order/FX headline | very weak MFE and severe 30D/90D/180D MAE | current_profile_false_positive |
| 이마트 | May over-promote retail scale/reopening headline | small MFE and large forward drawdown | current_profile_false_positive |


Stress-test answers:

```text
stage2_actionable_evidence_bonus: correct only when inventory-turn or margin bridge is present; too permissive for generic order/retail headline.
yellow_threshold_75: acceptable for F&F/YOUNGONE; too generous for HANSAE/EMART if inventory risk is not penalized.
green_threshold_87_revision_55: kept; C19 Green should require revision plus inventory-turn/sell-through confirmation.
price_only_blowoff_guard: kept.
full_4B_non_price_requirement: strengthened by F&F overlay; valuation plus inventory/margin slowdown is better than price-only peak.
hard_4C_routing: strengthened by HANSAE; destocking/call-off turns entry thesis into protection logic.
```

## 14. Stage2 / Yellow / Green Comparison

No separate Stage3-Green row is used as a representative trigger in this loop. The core audit is earlier: Stage2 promotion in C19 must distinguish inventory-turn/margin evidence from generic brand/reopening headlines.

```text
F&F: Stage2/Yellow works; Green only after margin bridge and channel evidence confirm.
YOUNGONE: Stage2/Yellow works; Green remains intentionally strict because upside was moderate.
HANSAE: Stage2 promotion is false positive without destocking-risk penalty.
EMART: Stage2 promotion is false positive without retail inventory/margin guard.
green_lateness_ratio = not_applicable for representative rows
```

## 15. 4B Local vs Full-window Timing Audit

| trigger_id | four_b_evidence_type | four_b_local_peak_proximity | four_b_full_window_peak_proximity | four_b_timing_verdict |
| --- | --- | --- | --- | --- |
| T_FNF_20221206_4B_INVENTORY_VALUATION_OVERLAY | valuation_blowoff,positioning_overheat,margin_or_backlog_slowdown | 0.67 | 0.67 | good_full_window_4B_timing |


The F&F overlay is not a price-only 4B. It combines a mostly-realized 2022 rerating path with valuation/positioning and later inventory/margin risk, so it should train only overlay/risk timing, not positive entry weights.

## 16. 4C Protection Audit

| trigger_id | symbol | entry_date | entry_price | MAE_90D_after_4C | four_c_protection_label | verdict |
| --- | --- | --- | --- | --- | --- | --- |
| T_HANSAE_20220519_4C_DESTOCKING_BREAK | 105630 | 2022-05-19 | 22700 | -35.02 | hard_4c_success_if_triggered_early | 4C protection would have avoided a large part of the later drawdown |
| T_EMART_20210810_FALSE_STAGE2 | 139480 | 2021-08-10 | 177000 | -13.84 | hard_4c_late | 4C should have been watched once retail margin evidence failed to confirm |


## 17. Sector-Specific Rule Candidate

```text
sector_specific_rule_candidate = false
```

The result is not broad enough for all L5 consumer names. It is narrower: C19 brand/retail inventory-margin setups need their own guard.

## 18. Canonical-Archetype Rule Candidate

```text
canonical_archetype_rule_candidate = true
rule_scope = canonical_archetype_specific
canonical_archetype_id = C19_BRAND_RETAIL_INVENTORY_MARGIN
```

Candidate rule:

```text
C19 positive promotion requires at least one of:
  - visible inventory-turn / sell-through evidence,
  - product/channel reorder quality that converts into margin bridge,
  - confirmed revision tied to margin quality rather than only revenue/order headline.

C19 guardrail:
  - retail scale/reopening headline without inventory-turn evidence cannot exceed Stage2-Watch,
  - apparel order headline must be penalized if buyer inventory/destocking risk is visible,
  - 4C routing should activate when inventory/call-off evidence breaks the Stage2 thesis.
```

## 19. Before / After Backtest Comparison

| profile_id | profile_scope | profile_hypothesis | changed_axes | eligible_trigger_count | avg_MFE_90D_pct | avg_MAE_90D_pct | avg_MFE_180D_pct | avg_MAE_180D_pct | false_positive_rate | missed_structural_count | late_green_count | score_return_alignment_verdict |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| P0_e2r_2_1_stock_web_calibrated_proxy | current_global | global profile without C19 inventory-turn distinction | none | 4 | 12.12 | -17.95 | 12.12 | -24.12 | 50% | 0 | 1 | mixed; two false positives remain |
| P0b_e2r_2_0_baseline_reference | rollback_reference | pre-calibrated looser entry profile | legacy thresholds | 4 | 12.12 | -17.95 | 12.12 | -24.12 | 50%+ | 0 | 0 | worse; headline positives over-credit |
| P1_L5_consumer_inventory_shadow | sector_specific | requires visible inventory-turn or channel sell-through before promotion | inventory_turn_score + channel_reorder_score | 4 | 20.38 | -8.72 | 20.38 | -8.97 | 0% | 0 | 1 | improves C19 separation but not enough for global |
| P2_C19_inventory_margin_bridge_shadow | canonical_archetype_specific | promote only when margin bridge + inventory-turn evidence co-exist | generic_retail_headline_guard + inventory_destocking_risk_penalty | 4 | 20.38 | -8.72 | 20.38 | -8.97 | 0% | 0 | 1 | best alignment in this loop |
| P3_C19_counterexample_guard | canonical_guard | demote retail scale/order headline without sell-through proof | inventory_destocking_risk_penalty | 4 | 20.38 | -8.72 | 20.38 | -8.97 | 0% | 0 | 1 | keeps positives while blocking high-MAE false positives |


## 20. Score-Return Alignment Matrix

| trigger_id | weighted_score_before | stage_before | weighted_score_after | stage_after | MFE_90D_pct | MAE_90D_pct | alignment |
| --- | --- | --- | --- | --- | --- | --- | --- |
| T_FNF_20220517_STAGE2_ACTIONABLE | 83.0 | Stage3-Yellow | 89.0 | Stage3-Green | 26.62 | -7.98 | structural_success_inventory_margin_bridge |
| T_YOUNGONE_20220817_STAGE2_ACTIONABLE | 78.0 | Stage3-Yellow | 82.0 | Stage3-Yellow | 14.13 | -9.46 | structural_success_moderate_MFE |
| T_HANSAE_20220517_FALSE_STAGE2 | 74.0 | Stage2-Actionable | 60.0 | Stage2-Watch | 4.64 | -40.52 | false_positive_stage2_high_MAE |
| T_EMART_20210810_FALSE_STAGE2 | 69.0 | Stage2-Actionable | 55.0 | Stage2-Watch | 3.11 | -13.84 | false_positive_stage2_weak_MFE_large_MAE |


## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive_case_count | counterexample_count | 4B_case_count | 4C_case_count | new_independent_case_count | reused_case_count | calibration_usable_trigger_count | representative_trigger_count | current_profile_error_count | sector_rule_candidate | canonical_rule_candidate | coverage_gap_after_this_loop |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| L5_CONSUMER_BRAND_DISTRIBUTION | C19_BRAND_RETAIL_INVENTORY_MARGIN | APPAREL_BRAND_AND_RETAIL_INVENTORY_MARGIN_BRIDGE | 2 | 2 | 1 | 1 | 4 | 0 | 6 | 4 | 2 | False | True | C19 now has positive/counterexample balance; still needs food/retail sub-vertical expansion later |


## 22. Residual Contribution Summary

```text
new_independent_case_count: 4
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 4
new_canonical_archetype_count: 1
new_fine_archetype_count: 1
new_trigger_family_count: 5
tested_existing_calibrated_axes: [stage2_actionable_evidence_bonus, stage3_green_revision_min, full_4b_requires_non_price_evidence, hard_4c_thesis_break_routes_to_4c]
residual_error_types_found: [brand_retail_headline_false_positive, inventory_destocking_high_MAE, retail_scale_without_margin_bridge]
new_axis_proposed: [inventory_turn_score, generic_retail_reopening_headline_guard, inventory_destocking_risk_penalty]
existing_axis_strengthened: [full_4b_requires_non_price_evidence, hard_4c_thesis_break_routes_to_4c]
existing_axis_weakened: []
existing_axis_kept: [stage2_actionable_evidence_bonus, stage3_yellow_total_min, stage3_green_total_min, stage3_green_revision_min, stage3_cross_evidence_green_buffer, price_only_blowoff_blocks_positive_stage]
sector_specific_rule_candidate: false
canonical_archetype_rule_candidate: true
no_new_signal_reason: null
loop_contribution_label: canonical_archetype_rule_candidate
do_not_propose_new_weight_delta: false
```

## 23. Validation Scope / Non-Validation Scope

Validated:

```text
- Stock-Web tradable OHLC rows for selected trigger windows.
- 30D / 90D / 180D MFE and MAE directionality.
- Positive/counterexample balance inside scheduled R5.
- C19-specific inventory-turn and destocking guard hypothesis.
```

Not validated:

```text
- live candidate scan,
- investment recommendation,
- production scoring patch,
- brokerage or auto-trading path,
- global rule promotion beyond C19.
```

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,inventory_turn_score,canonical_archetype_specific,L5_CONSUMER_BRAND_DISTRIBUTION,C19_BRAND_RETAIL_INVENTORY_MARGIN,0,+2,+2,"C19 positives had sell-through/inventory-turn or clean margin bridge; false positives did not","kept F&F/YOUNGONE while blocking HANSAE/EMART","T_FNF_20220517_STAGE2_ACTIONABLE|T_YOUNGONE_20220817_STAGE2_ACTIONABLE|T_HANSAE_20220517_FALSE_STAGE2|T_EMART_20210810_FALSE_STAGE2",4,4,2,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,generic_retail_reopening_headline_guard,canonical_archetype_specific,L5_CONSUMER_BRAND_DISTRIBUTION,C19_BRAND_RETAIL_INVENTORY_MARGIN,0,-2,-2,"retail scale/reopening without margin evidence produced weak MFE and high MAE","reduces false Stage2 on EMART-like setup","T_EMART_20210810_FALSE_STAGE2",1,1,1,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,inventory_destocking_risk_penalty,canonical_archetype_specific,L5_CONSUMER_BRAND_DISTRIBUTION,C19_BRAND_RETAIL_INVENTORY_MARGIN,0,-3,-3,"buyer destocking/call-off risk turned order headline into high-MAE failure","blocks HANSAE-like order headline false positive","T_HANSAE_20220517_FALSE_STAGE2|T_HANSAE_20220519_4C_DESTOCKING_BREAK",2,1,1,medium,canonical_shadow_only,"4C rows protection-only"
```

## 25. Machine-Readable Rows

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
{"row_type":"case","case_id":"R5L14_C19_POS_FNF_202205_Q1_BRAND_INVENTORY_MARGIN","symbol":"383220","company_name":"F&F","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"T_FNF_20220517_STAGE2_ACTIONABLE","current_profile_verdict":"current_profile_correct","round":"R5","loop":"14","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C19_BRAND_RETAIL_INVENTORY_MARGIN","fine_archetype_id":"APPAREL_BRAND_AND_RETAIL_INVENTORY_MARGIN_BRIDGE","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"positive_alignment_with_controlled_MAE","price_source":"Songdaiki/stock-web","notes":"brand sell-through and China/offline channel leverage translated into margin bridge; clean 180D window after 2022-04-13 corporate-action candidate."}
{"row_type":"case","case_id":"R5L14_C19_POS_YOUNGONE_202208_Q2_ORDER_MARGIN_BRIDGE","symbol":"111770","company_name":"영원무역","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"T_YOUNGONE_20220817_STAGE2_ACTIONABLE","current_profile_verdict":"current_profile_correct","round":"R5","loop":"14","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C19_BRAND_RETAIL_INVENTORY_MARGIN","fine_archetype_id":"APPAREL_BRAND_AND_RETAIL_INVENTORY_MARGIN_BRIDGE","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"moderate_positive_alignment","price_source":"Songdaiki/stock-web","notes":"order/mix and FX-supported margin bridge worked, but the upside was moderate and needed inventory-risk monitoring."}
{"row_type":"case","case_id":"R5L14_C19_NEG_HANSAE_202205_ORDER_HEADLINE_DESTOCKING","symbol":"105630","company_name":"한세실업","case_type":"failed_rerating","positive_or_counterexample":"counterexample","best_trigger":"T_HANSAE_20220517_FALSE_STAGE2","current_profile_verdict":"current_profile_false_positive","round":"R5","loop":"14","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C19_BRAND_RETAIL_INVENTORY_MARGIN","fine_archetype_id":"APPAREL_BRAND_AND_RETAIL_INVENTORY_MARGIN_BRIDGE","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"negative_alignment_high_MAE","price_source":"Songdaiki/stock-web","notes":"headline order/margin optimism was overwhelmed by buyer inventory destocking and margin normalization risk."}
{"row_type":"case","case_id":"R5L14_C19_NEG_EMART_202108_RETAIL_MARGIN_HEADLINE","symbol":"139480","company_name":"이마트","case_type":"failed_rerating","positive_or_counterexample":"counterexample","best_trigger":"T_EMART_20210810_FALSE_STAGE2","current_profile_verdict":"current_profile_false_positive","round":"R5","loop":"14","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C19_BRAND_RETAIL_INVENTORY_MARGIN","fine_archetype_id":"APPAREL_BRAND_AND_RETAIL_INVENTORY_MARGIN_BRIDGE","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"weak_MFE_large_drawdown","price_source":"Songdaiki/stock-web","notes":"offline reopening and retail scale did not become inventory-turn / margin recovery evidence; subsequent path punished weak margin quality."}
{"trigger_id":"T_FNF_20220517_STAGE2_ACTIONABLE","case_id":"R5L14_C19_POS_FNF_202205_Q1_BRAND_INVENTORY_MARGIN","symbol":"383220","company_name":"F&F","trigger_type":"Stage2-Actionable","trigger_date":"2022-05-16","entry_date":"2022-05-17","entry_price":131500,"evidence_available_at_that_date":"Q1 result / brand sell-through / margin bridge became observable; evidence timing assumed after close, next-trading-day close used.","evidence_source":"historical public earnings/result context; stock-web OHLC rows verified in atlas/ohlcv_tradable_by_symbol_year/383/383220/2022.csv and 2023.csv","stage2_evidence_fields":["public_event_or_disclosure","customer_or_order_quality","capacity_or_volume_route","early_revision_signal"],"stage3_evidence_fields":["confirmed_revision","margin_bridge","financial_visibility","low_red_team_risk"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/383/383220/2022.csv","profile_path":"atlas/symbol_profiles/383/383220.json","MFE_30D_pct":13.69,"MFE_90D_pct":26.62,"MFE_180D_pct":26.62,"MFE_1Y_pct":26.62,"MFE_2Y_pct":null,"MAE_30D_pct":-7.98,"MAE_90D_pct":-7.98,"MAE_180D_pct":-8.37,"MAE_1Y_pct":-24.64,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2022-08-02","peak_price":166500,"drawdown_after_peak_pct":-27.63,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_applicable","four_b_evidence_type":[],"four_c_protection_label":"not_applicable","trigger_outcome_label":"structural_success_inventory_margin_bridge","current_profile_verdict":"current_profile_correct","same_entry_group_id":"G_FNF_20220517","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"corporate_action_window_status":"clean_180D_window_after_2022_04_13_candidate","forward_window_trading_days":180,"row_type":"trigger","round":"R5","loop":"14","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C19_BRAND_RETAIL_INVENTORY_MARGIN","fine_archetype_id":"APPAREL_BRAND_AND_RETAIL_INVENTORY_MARGIN_BRIDGE","sector":"consumer_brand_distribution","primary_archetype":"brand_retail_inventory_margin","loop_objective":"coverage_gap_fill|counterexample_mining|canonical_archetype_compression|4C_thesis_break_timing_test","price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","calibration_usable":true,"calibration_block_reasons":[]}
{"trigger_id":"T_FNF_20221206_4B_INVENTORY_VALUATION_OVERLAY","case_id":"R5L14_C19_POS_FNF_202205_Q1_BRAND_INVENTORY_MARGIN","symbol":"383220","company_name":"F&F","trigger_type":"Stage4B-Overlay","trigger_date":"2022-12-06","entry_date":"2022-12-06","entry_price":155000,"evidence_available_at_that_date":"valuation/positioning overlay after the stock had largely priced the 2022 brand-margin recovery; later demand/inventory risk needed monitoring.","evidence_source":"stock-web OHLC row around 2022-12-06; narrative 4B overlay only","stage2_evidence_fields":[],"stage3_evidence_fields":[],"stage4b_evidence_fields":["valuation_blowoff","positioning_overheat","margin_or_backlog_slowdown"],"stage4c_evidence_fields":[],"price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/383/383220/2022.csv","profile_path":"atlas/symbol_profiles/383/383220.json","MFE_30D_pct":6.77,"MFE_90D_pct":6.77,"MFE_180D_pct":6.77,"MFE_1Y_pct":6.77,"MFE_2Y_pct":null,"MAE_30D_pct":-22.26,"MAE_90D_pct":-22.26,"MAE_180D_pct":-24.64,"MAE_1Y_pct":-41.03,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2022-12-06","peak_price":165500,"drawdown_after_peak_pct":-27.19,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":0.67,"four_b_full_window_peak_proximity":0.67,"four_b_timing_verdict":"good_full_window_4B_timing","four_b_evidence_type":["valuation_blowoff","positioning_overheat","margin_or_backlog_slowdown"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"4B_overlay_success","current_profile_verdict":"current_profile_correct","same_entry_group_id":"G_FNF_20221206_4B","dedupe_for_aggregate":false,"aggregate_group_role":"4B_overlay_only","is_new_independent_case":false,"reuse_reason":"same_symbol_4B_overlay_new_trigger_family","independent_evidence_weight":0.25,"do_not_count_as_new_case":true,"corporate_action_window_status":"clean_180D_window_after_2022_04_13_candidate","forward_window_trading_days":180,"row_type":"trigger","round":"R5","loop":"14","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C19_BRAND_RETAIL_INVENTORY_MARGIN","fine_archetype_id":"APPAREL_BRAND_AND_RETAIL_INVENTORY_MARGIN_BRIDGE","sector":"consumer_brand_distribution","primary_archetype":"brand_retail_inventory_margin","loop_objective":"coverage_gap_fill|counterexample_mining|canonical_archetype_compression|4C_thesis_break_timing_test","price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","calibration_usable":true,"calibration_block_reasons":[]}
{"trigger_id":"T_YOUNGONE_20220817_STAGE2_ACTIONABLE","case_id":"R5L14_C19_POS_YOUNGONE_202208_Q2_ORDER_MARGIN_BRIDGE","symbol":"111770","company_name":"영원무역","trigger_type":"Stage2-Actionable","trigger_date":"2022-08-16","entry_date":"2022-08-17","entry_price":46000,"evidence_available_at_that_date":"Q2 order/mix and FX-supported margin bridge; next-trading-day close used.","evidence_source":"historical public result context; stock-web rows verified in atlas/ohlcv_tradable_by_symbol_year/111/111770/2022.csv and 2023.csv","stage2_evidence_fields":["public_event_or_disclosure","customer_or_order_quality","early_revision_signal"],"stage3_evidence_fields":["confirmed_revision","margin_bridge","financial_visibility"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/111/111770/2022.csv","profile_path":"atlas/symbol_profiles/111/111770.json","MFE_30D_pct":9.78,"MFE_90D_pct":14.13,"MFE_180D_pct":14.13,"MFE_1Y_pct":14.13,"MFE_2Y_pct":null,"MAE_30D_pct":-8.48,"MAE_90D_pct":-9.46,"MAE_180D_pct":-9.57,"MAE_1Y_pct":-9.57,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2022-11-14","peak_price":52500,"drawdown_after_peak_pct":-20.76,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_applicable","four_b_evidence_type":[],"four_c_protection_label":"not_applicable","trigger_outcome_label":"structural_success_moderate_MFE","current_profile_verdict":"current_profile_correct","same_entry_group_id":"G_YOUNGONE_20220817","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"corporate_action_window_status":"clean_180D_window","forward_window_trading_days":180,"row_type":"trigger","round":"R5","loop":"14","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C19_BRAND_RETAIL_INVENTORY_MARGIN","fine_archetype_id":"APPAREL_BRAND_AND_RETAIL_INVENTORY_MARGIN_BRIDGE","sector":"consumer_brand_distribution","primary_archetype":"brand_retail_inventory_margin","loop_objective":"coverage_gap_fill|counterexample_mining|canonical_archetype_compression|4C_thesis_break_timing_test","price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","calibration_usable":true,"calibration_block_reasons":[]}
{"trigger_id":"T_HANSAE_20220517_FALSE_STAGE2","case_id":"R5L14_C19_NEG_HANSAE_202205_ORDER_HEADLINE_DESTOCKING","symbol":"105630","company_name":"한세실업","trigger_type":"Stage2-Actionable","trigger_date":"2022-05-16","entry_date":"2022-05-17","entry_price":24800,"evidence_available_at_that_date":"headline order/backlog and FX optimism existed, but buyer inventory/destocking risk was not resolved; next-trading-day close used.","evidence_source":"historical public result context; stock-web rows verified in atlas/ohlcv_tradable_by_symbol_year/105/105630/2022.csv","stage2_evidence_fields":["public_event_or_disclosure","customer_or_order_quality","early_revision_signal"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["margin_or_backlog_slowdown"],"stage4c_evidence_fields":["call_off_or_order_cut","thesis_evidence_broken"],"price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/105/105630/2022.csv","profile_path":"atlas/symbol_profiles/105/105630.json","MFE_30D_pct":4.64,"MFE_90D_pct":4.64,"MFE_180D_pct":4.64,"MFE_1Y_pct":4.64,"MFE_2Y_pct":null,"MAE_30D_pct":-33.27,"MAE_90D_pct":-40.52,"MAE_180D_pct":-47.18,"MAE_1Y_pct":-49.19,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2022-05-17","peak_price":25950,"drawdown_after_peak_pct":-49.52,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_full_4B_entry_failure","four_b_evidence_type":["margin_or_backlog_slowdown"],"four_c_protection_label":"hard_4c_late","trigger_outcome_label":"false_positive_stage2_high_MAE","current_profile_verdict":"current_profile_false_positive","same_entry_group_id":"G_HANSAE_20220517","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"corporate_action_window_status":"clean_180D_window_far_after_2011_candidate","forward_window_trading_days":180,"row_type":"trigger","round":"R5","loop":"14","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C19_BRAND_RETAIL_INVENTORY_MARGIN","fine_archetype_id":"APPAREL_BRAND_AND_RETAIL_INVENTORY_MARGIN_BRIDGE","sector":"consumer_brand_distribution","primary_archetype":"brand_retail_inventory_margin","loop_objective":"coverage_gap_fill|counterexample_mining|canonical_archetype_compression|4C_thesis_break_timing_test","price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","calibration_usable":true,"calibration_block_reasons":[]}
{"trigger_id":"T_HANSAE_20220519_4C_DESTOCKING_BREAK","case_id":"R5L14_C19_NEG_HANSAE_202205_ORDER_HEADLINE_DESTOCKING","symbol":"105630","company_name":"한세실업","trigger_type":"Stage4C","trigger_date":"2022-05-19","entry_date":"2022-05-19","entry_price":22700,"evidence_available_at_that_date":"large selloff after the order/margin thesis failed to hold; destocking and buyer call-off risk converted from watch item to thesis-break routing.","evidence_source":"stock-web OHLC row and subsequent drawdown path; 4C overlay only","stage2_evidence_fields":[],"stage3_evidence_fields":[],"stage4b_evidence_fields":["margin_or_backlog_slowdown"],"stage4c_evidence_fields":["call_off_or_order_cut","thesis_evidence_broken"],"price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/105/105630/2022.csv","profile_path":"atlas/symbol_profiles/105/105630.json","MFE_30D_pct":2.2,"MFE_90D_pct":2.2,"MFE_180D_pct":2.2,"MFE_1Y_pct":2.2,"MFE_2Y_pct":null,"MAE_30D_pct":-27.09,"MAE_90D_pct":-35.02,"MAE_180D_pct":-42.29,"MAE_1Y_pct":-44.49,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2022-05-23","peak_price":23200,"drawdown_after_peak_pct":-43.53,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_applicable","four_b_evidence_type":["margin_or_backlog_slowdown"],"four_c_protection_label":"hard_4c_success_if_triggered_early","trigger_outcome_label":"4C_success","current_profile_verdict":"current_profile_4C_too_late","same_entry_group_id":"G_HANSAE_20220519_4C","dedupe_for_aggregate":false,"aggregate_group_role":"4C_overlay_only","is_new_independent_case":false,"reuse_reason":"same_symbol_4C_thesis_break_new_trigger_family","independent_evidence_weight":0.25,"do_not_count_as_new_case":true,"corporate_action_window_status":"clean_180D_window_far_after_2011_candidate","forward_window_trading_days":180,"row_type":"trigger","round":"R5","loop":"14","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C19_BRAND_RETAIL_INVENTORY_MARGIN","fine_archetype_id":"APPAREL_BRAND_AND_RETAIL_INVENTORY_MARGIN_BRIDGE","sector":"consumer_brand_distribution","primary_archetype":"brand_retail_inventory_margin","loop_objective":"coverage_gap_fill|counterexample_mining|canonical_archetype_compression|4C_thesis_break_timing_test","price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","calibration_usable":true,"calibration_block_reasons":[]}
{"trigger_id":"T_EMART_20210810_FALSE_STAGE2","case_id":"R5L14_C19_NEG_EMART_202108_RETAIL_MARGIN_HEADLINE","symbol":"139480","company_name":"이마트","trigger_type":"Stage2-Actionable","trigger_date":"2021-08-10","entry_date":"2021-08-10","entry_price":177000,"evidence_available_at_that_date":"retail reopening / scale narrative and result headline existed, but inventory-turn and margin-quality bridge were not proven; same-day close used for market-reactable event.","evidence_source":"historical public result context; stock-web rows verified in atlas/ohlcv_tradable_by_symbol_year/139/139480/2021.csv and 2022.csv","stage2_evidence_fields":["public_event_or_disclosure","policy_or_regulatory_optionality"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["margin_or_backlog_slowdown"],"stage4c_evidence_fields":["thesis_evidence_broken"],"price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/139/139480/2021.csv","profile_path":"atlas/symbol_profiles/139/139480.json","MFE_30D_pct":3.11,"MFE_90D_pct":3.11,"MFE_180D_pct":3.11,"MFE_1Y_pct":3.11,"MFE_2Y_pct":null,"MAE_30D_pct":-5.65,"MAE_90D_pct":-13.84,"MAE_180D_pct":-31.36,"MAE_1Y_pct":-31.36,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2021-08-17","peak_price":182500,"drawdown_after_peak_pct":-33.42,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_full_4B_entry_failure","four_b_evidence_type":["margin_or_backlog_slowdown"],"four_c_protection_label":"hard_4c_late","trigger_outcome_label":"false_positive_stage2_weak_MFE_large_MAE","current_profile_verdict":"current_profile_false_positive","same_entry_group_id":"G_EMART_20210810","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"corporate_action_window_status":"clean_180D_window","forward_window_trading_days":180,"row_type":"trigger","round":"R5","loop":"14","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C19_BRAND_RETAIL_INVENTORY_MARGIN","fine_archetype_id":"APPAREL_BRAND_AND_RETAIL_INVENTORY_MARGIN_BRIDGE","sector":"consumer_brand_distribution","primary_archetype":"brand_retail_inventory_margin","loop_objective":"coverage_gap_fill|counterexample_mining|canonical_archetype_compression|4C_thesis_break_timing_test","price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","calibration_usable":true,"calibration_block_reasons":[]}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R5L14_C19_POS_FNF_202205_Q1_BRAND_INVENTORY_MARGIN","trigger_id":"T_FNF_20220517_STAGE2_ACTIONABLE","symbol":"383220","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C19_BRAND_RETAIL_INVENTORY_MARGIN","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":19,"revision_score":16,"relative_strength_score":11,"customer_quality_score":13,"policy_or_regulatory_score":0,"valuation_repricing_score":8,"execution_risk_score":0,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"execution_risk":5,"channel_reorder_score":14,"inventory_turn_score":13},"weighted_score_before":83.0,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":22,"revision_score":18,"relative_strength_score":11,"customer_quality_score":15,"policy_or_regulatory_score":0,"valuation_repricing_score":8,"execution_risk_score":0,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"execution_risk":4,"channel_reorder_score":16,"inventory_turn_score":15},"weighted_score_after":89.0,"stage_label_after":"Stage3-Green","changed_components":["inventory_turn_score","channel_reorder_score","margin_bridge_score"],"component_delta_explanation":"product/channel sell-through plus margin bridge deserves C19 positive credit","MFE_90D_pct":26.62,"MAE_90D_pct":-7.98,"score_return_alignment_label":"structural_success_inventory_margin_bridge","current_profile_verdict":"current_profile_correct"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R5L14_C19_POS_YOUNGONE_202208_Q2_ORDER_MARGIN_BRIDGE","trigger_id":"T_YOUNGONE_20220817_STAGE2_ACTIONABLE","symbol":"111770","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C19_BRAND_RETAIL_INVENTORY_MARGIN","raw_component_scores_before":{"contract_score":10,"backlog_visibility_score":12,"margin_bridge_score":17,"revision_score":14,"relative_strength_score":8,"customer_quality_score":12,"policy_or_regulatory_score":0,"valuation_repricing_score":5,"execution_risk_score":0,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"execution_risk":7,"inventory_turn_score":9},"weighted_score_before":78.0,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":11,"backlog_visibility_score":13,"margin_bridge_score":18,"revision_score":15,"relative_strength_score":8,"customer_quality_score":12,"policy_or_regulatory_score":0,"valuation_repricing_score":5,"execution_risk_score":0,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"execution_risk":7,"inventory_turn_score":10},"weighted_score_after":82.0,"stage_label_after":"Stage3-Yellow","changed_components":["margin_bridge_score","customer_quality_score"],"component_delta_explanation":"solid but moderate path; do not force Green without repeated inventory/margin evidence","MFE_90D_pct":14.13,"MAE_90D_pct":-9.46,"score_return_alignment_label":"structural_success_moderate_MFE","current_profile_verdict":"current_profile_correct"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R5L14_C19_NEG_HANSAE_202205_ORDER_HEADLINE_DESTOCKING","trigger_id":"T_HANSAE_20220517_FALSE_STAGE2","symbol":"105630","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C19_BRAND_RETAIL_INVENTORY_MARGIN","raw_component_scores_before":{"contract_score":10,"backlog_visibility_score":11,"margin_bridge_score":10,"revision_score":8,"relative_strength_score":4,"customer_quality_score":8,"policy_or_regulatory_score":0,"valuation_repricing_score":0,"execution_risk_score":0,"legal_or_contract_risk_score":8,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"execution_risk":14,"inventory_turn_score":-8},"weighted_score_before":74.0,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"contract_score":8,"backlog_visibility_score":7,"margin_bridge_score":5,"revision_score":4,"relative_strength_score":4,"customer_quality_score":6,"policy_or_regulatory_score":0,"valuation_repricing_score":0,"execution_risk_score":0,"legal_or_contract_risk_score":12,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"execution_risk":20,"inventory_turn_score":-15},"weighted_score_after":60.0,"stage_label_after":"Stage2-Watch","changed_components":["inventory_destocking_risk_penalty","margin_bridge_score"],"component_delta_explanation":"order headline without sell-through guard becomes false positive","MFE_90D_pct":4.64,"MAE_90D_pct":-40.52,"score_return_alignment_label":"false_positive_stage2_high_MAE","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R5L14_C19_NEG_EMART_202108_RETAIL_MARGIN_HEADLINE","trigger_id":"T_EMART_20210810_FALSE_STAGE2","symbol":"139480","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C19_BRAND_RETAIL_INVENTORY_MARGIN","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":8,"revision_score":7,"relative_strength_score":4,"customer_quality_score":5,"policy_or_regulatory_score":6,"valuation_repricing_score":0,"execution_risk_score":0,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"execution_risk":13,"inventory_turn_score":-6},"weighted_score_before":69.0,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":4,"revision_score":3,"relative_strength_score":4,"customer_quality_score":4,"policy_or_regulatory_score":4,"valuation_repricing_score":0,"execution_risk_score":0,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"execution_risk":18,"inventory_turn_score":-13},"weighted_score_after":55.0,"stage_label_after":"Stage2-Watch","changed_components":["retail_inventory_margin_guard","execution_risk_score"],"component_delta_explanation":"scale/reopening narrative should not substitute for inventory-turn and margin-quality proof","MFE_90D_pct":3.11,"MAE_90D_pct":-13.84,"score_return_alignment_label":"false_positive_stage2_weak_MFE_large_MAE","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"residual_contribution","round":"R5","loop":"14","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C19_BRAND_RETAIL_INVENTORY_MARGIN","scheduled_round":"R5","scheduled_loop":14,"round_schedule_status":"valid","round_sector_consistency":"pass","new_independent_case_count":4,"reused_case_count":0,"new_symbol_count":4,"same_archetype_new_symbol_count":4,"same_archetype_new_trigger_family_count":5,"new_trigger_family_count":5,"positive_case_count":2,"counterexample_count":2,"current_profile_error_count":2,"tested_existing_calibrated_axes":["stage2_actionable_evidence_bonus","stage3_green_revision_min","full_4b_requires_non_price_evidence","hard_4c_thesis_break_routes_to_4c"],"residual_error_types_found":["brand_retail_headline_false_positive","inventory_destocking_high_MAE","retail_scale_without_margin_bridge"],"loop_contribution_label":"canonical_archetype_rule_candidate","do_not_propose_new_weight_delta":false}
```

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,inventory_turn_score,canonical_archetype_specific,L5_CONSUMER_BRAND_DISTRIBUTION,C19_BRAND_RETAIL_INVENTORY_MARGIN,0,+2,+2,"C19 positives had sell-through/inventory-turn or clean margin bridge; false positives did not","kept F&F/YOUNGONE while blocking HANSAE/EMART","T_FNF_20220517_STAGE2_ACTIONABLE|T_YOUNGONE_20220817_STAGE2_ACTIONABLE|T_HANSAE_20220517_FALSE_STAGE2|T_EMART_20210810_FALSE_STAGE2",4,4,2,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,generic_retail_reopening_headline_guard,canonical_archetype_specific,L5_CONSUMER_BRAND_DISTRIBUTION,C19_BRAND_RETAIL_INVENTORY_MARGIN,0,-2,-2,"retail scale/reopening without margin evidence produced weak MFE and high MAE","reduces false Stage2 on EMART-like setup","T_EMART_20210810_FALSE_STAGE2",1,1,1,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,inventory_destocking_risk_penalty,canonical_archetype_specific,L5_CONSUMER_BRAND_DISTRIBUTION,C19_BRAND_RETAIL_INVENTORY_MARGIN,0,-3,-3,"buyer destocking/call-off risk turned order headline into high-MAE failure","blocks HANSAE-like order headline false positive","T_HANSAE_20220517_FALSE_STAGE2|T_HANSAE_20220519_4C_DESTOCKING_BREAK",2,1,1,medium,canonical_shadow_only,"4C rows protection-only"
```

## 26. Deferred Coding Agent Handoff Prompt

### Purpose

You are now in the repository implementation phase. The attached Markdown files are v12 post-calibrated residual research outputs produced using the Songdaiki/stock-web OHLC atlas.

These MDs are not live candidate research. They are historical calibration research designed to extend the already-applied e2r_2_1_stock_web_calibrated profile.

Do not blindly apply every shadow row. Ingest the machine-readable rows and update the sector/canonical-archetype calibration ledger.

### Price source context

- Primary historical price source used by the research MD: Songdaiki/stock-web.
- Price basis: tradable_raw.
- Price adjustment status: raw_unadjusted_marcap.
- Price shard pattern: atlas/ohlcv_tradable_by_symbol_year/<prefix>/<ticker>/<year>.csv.
- Symbol profile pattern: atlas/symbol_profiles/<prefix>/<ticker>.json.

### Rules

- Use only calibration_usable=true rows for quantitative calibration.
- Do not count reused cases as new independent evidence unless independent_evidence_weight > 0.
- Do not treat schema_rematerialization_only or duplicate_low_value_loop as new evidence.
- Do not apply global deltas unless multiple large_sector_id values support the same direction.
- Prefer sector_specific or canonical_archetype_specific shadow profiles.
- Positive score promotion requires non-price evidence and clean 180D MFE/MAE.
- 4B rows are overlay/risk calibration only.
- 4C rows are thesis-break/protection calibration only.
- price-only rows cannot promote Stage2/Stage3.
- If a v12 MD weakens an already applied axis, log it as residual counterexample rather than immediately reverting.
- Production scoring must not change unless the user explicitly asks for another promotion batch.

### Expected repository tasks

1. Parse case / trigger / score_simulation / shadow_weight / residual_contribution rows.
2. Validate stock-web price source fields.
3. Validate large_sector_id and canonical_archetype_id.
4. Validate novelty and reuse fields.
5. Deduplicate same_entry_group_id and reused cases.
6. Aggregate by large_sector_id and canonical_archetype_id.
7. Update sector_shadow_profile and archetype_shadow_profile only.
8. Preserve global calibrated profile unless explicitly promoted.
9. Report new independent cases, counterexamples, and residual error types.
10. Add tests that duplicate low-value loops cannot change weights.

### Expected output

- Concise implementation summary.
- Rows accepted/rejected.
- New sector/canonical archetype coverage.
- Existing axis strengthened/weakened/kept.
- No investment recommendation language.

## 27. Next Round State

```text
completed_round = R5
completed_loop = 14
next_round = R6
next_loop = 14
round_schedule_status = valid
round_sector_consistency = pass
```

## 28. Source Notes

```text
price_source = Songdaiki/stock-web
manifest_path = atlas/manifest.json
schema_path = atlas/schema.json
universe_path = atlas/universe/all_symbols.csv
optional_smoke_bundle = diagnostics/chatgpt_bundle.txt
stock_web_manifest_max_date = 2026-02-20
price_basis = tradable_raw
price_adjustment_status = raw_unadjusted_marcap
```

Key OHLC rows checked from stock-web excerpts:

```text
383220/F&F: 2022-05-17 c=131500; 2022-08-02 h=166500; 2023-01-06 l=120500.
111770/영원무역: 2022-08-17 c=46000; 2022-11-14 h=52500; 2023-01-04 l=41600.
105630/한세실업: 2022-05-17 c=24800; 2022-05-17 h=25950; 2022-09-30 l=13100.
139480/이마트: 2021-08-10 c=177000; 2021-08-17 h=182500; 2022-02-24 l=121500.
```
