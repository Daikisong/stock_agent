# E2R Stock-Web v12 Residual Research — R3 loop 100 / L3 / C11

```yaml
schema_family: v12_sector_archetype_residual
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
selected_round: R3
selected_loop: 100
large_sector_id: L3_BATTERY_EV_GREEN_MOBILITY
canonical_archetype_id: C11_BATTERY_ORDERBOOK_RERATING
fine_archetype_id: BATTERY_EQUIPMENT_SEPARATOR_ORDERBOOK_DELIVERY_MARGIN_BRIDGE_VS_ORDERBOOK_LABEL_REVERSAL
selected_priority_bucket: Priority 0
selection_basis: docs/core/V12_Research_No_Repeat_Index.md
loop_objective:
  - coverage_gap_fill
  - counterexample_mining
  - stage2_actionable_bonus_stress_test
  - 4B_non_price_requirement_stress_test
  - canonical_archetype_compression
production_scoring_changed: false
shadow_weight_only: true
stock_agent_code_access_allowed: false
stock_agent_code_patch_allowed: false
stock_agent_live_scan_allowed: false
primary_price_source: Songdaiki/stock-web
source_basis: FinanceData/marcap transformed into assistant-readable symbol-year CSV shards
price_basis: tradable_raw
price_adjustment_status: raw_unadjusted_marcap
manifest_max_date: 2026-02-20
output_file: e2r_stock_web_v12_residual_round_R3_loop_100_L3_BATTERY_EV_GREEN_MOBILITY_C11_BATTERY_ORDERBOOK_RERATING_research.md
```

## 1. Selection and novelty check

No-Repeat Index still marks `C11_BATTERY_ORDERBOOK_RERATING` as Priority 0 with only 23 rows, requiring 7 more rows to reach the 30-row minimum stability band. This loop therefore selects C11 after the prior Priority 0 queue entries already covered in this working session.

Registry check found the latest committed C11 artifact at:

```text
docs/round/e2r_stock_web_v12_residual_round_R3_loop_99_L3_BATTERY_EV_GREEN_MOBILITY_C11_BATTERY_ORDERBOOK_RERATING_research.md
```

Therefore this file uses:

```text
selected_round = R3
selected_loop = 100
large_sector_id = L3_BATTERY_EV_GREEN_MOBILITY
canonical_archetype_id = C11_BATTERY_ORDERBOOK_RERATING
```

Hard duplicate check is conservative. The selected rows avoid reusing the same `canonical_archetype_id + symbol + trigger_type + entry_date` key from the visible registry. Some symbols may have appeared in broad battery-equipment/materials studies, but the trigger family here is compressed specifically around `orderbook/delivery/margin bridge` versus `orderbook label reversal`.

## 2. Stock-Web price source validation

Stock-Web manifest and schema basis used for this MD:

```text
source_name = FinanceData/marcap
price_basis = tradable_raw
price_adjustment_status = raw_unadjusted_marcap
calibration_shard_root = atlas/ohlcv_tradable_by_symbol_year
manifest_min_date = 1995-05-02
manifest_max_date = 2026-02-20
tradable_row_count = 14,354,401
symbol_count = 5,414
MFE_N_pct = (max high from entry_date through N tradable rows / entry_price - 1) * 100
MAE_N_pct = (min low from entry_date through N tradable rows / entry_price - 1) * 100
```

Symbol profile checks:

| symbol | name | profile status | row caveat |
|---|---|---|---|
| 137400 | 피엔티 | active_like | old corporate-action candidates only; 2024 path usable |
| 222080 | 씨아이에스 | active_like | SPAC-era discontinuity blocked outside current window; 2024 path usable |
| 299030 | 하나기술 | active_like | old 2021 discontinuity; 2024 path usable |
| 393890 | 더블유씨피 | active_like | no corporate-action candidate; 2024 path clean |

The raw/unadjusted caveat remains in force. This MD is usable as shadow residual research, not a production scoring patch.

## 3. C11 research question

C11 should not reward the word “orderbook” by itself. In battery equipment and battery materials, orderbook works only when it walks through the factory gate:

```text
customer order / backlog
  → delivery acceptance or utilization
  → revenue recognition
  → gross margin / OPM / FCF bridge
  → revision or sustained price confirmation
```

The failure mode is the warehouse full of promises: the orderbook headline is visible, the stock spikes, but utilization/call-off/margin deterioration later reveals that the backlog was not a rerating bridge. This loop tests whether C11 needs a stricter positive bridge before Stage3-Green and a quicker 4B/4C watch when orderbook vocabulary is present but delivery/margin evidence is missing.

## 4. Case matrix

| case_id | symbol | name | trigger_date | entry_date | entry_price | trigger_type | result_bucket | interpretation |
|---|---:|---|---|---|---:|---|---|---|
| C11-L100-01 | 137400 | 피엔티 | 2024-05-29 | 2024-05-30 | 59600 | orderbook_delivery_acceptance_momentum | positive_with_high_MAE_watch | Equipment orderbook + delivery acceptance path gave strong MFE, but late chase after the vertical leg required 4B local watch. |
| C11-L100-02 | 137400 | 피엔티 | 2024-06-11 | 2024-06-12 | 80900 | late_orderbook_chase_after_vertical_move | counterexample_high_MAE | Same symbol, new trigger family: orderbook label after near-blowoff becomes a late-chase risk, not a new Stage3-Green. |
| C11-L100-03 | 222080 | 씨아이에스 | 2024-03-05 | 2024-03-06 | 13290 | equipment_orderbook_theme_spike | counterexample_bridge_missing | Price spike occurred before durable margin bridge was clear; should stay Yellow/4B-watch rather than Green. |
| C11-L100-04 | 222080 | 씨아이에스 | 2024-02-15 | 2024-02-16 | 11170 | early_equipment_orderbook_reacceleration | marginal_positive_then_decay | Early entry had tradable MFE, but decayed without durable margin/revision proof. |
| C11-L100-05 | 299030 | 하나기술 | 2024-02-21 | 2024-02-22 | 61000 | battery_equipment_orderbook_label_reversal | false_positive_high_MAE | Orderbook/equipment vocabulary failed to convert into sustained rerating; should require stronger delivery and margin evidence. |
| C11-L100-06 | 393890 | 더블유씨피 | 2024-02-21 | 2024-02-22 | 47100 | separator_orderbook_demand_bridge_missing | counterexample_calloff_shadow | Separator/orderbook label was not enough while EV demand and utilization confidence were soft. |

## 5. Trigger JSONL rows

```jsonl
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","round":"R3","loop":"100","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C11_BATTERY_ORDERBOOK_RERATING","fine_archetype_id":"BATTERY_EQUIPMENT_SEPARATOR_ORDERBOOK_DELIVERY_MARGIN_BRIDGE_VS_ORDERBOOK_LABEL_REVERSAL","case_id":"C11-L100-01","symbol":"137400","name":"피엔티","trigger_date":"2024-05-29","entry_date":"2024-05-30","entry_price":59600,"trigger_type":"orderbook_delivery_acceptance_momentum","trigger_family":"battery_equipment_orderbook_delivery_acceptance","price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","mfe_30d_pct":50.2,"mae_30d_pct":-4.0,"mfe_90d_pct":50.2,"mae_90d_pct":-12.8,"mfe_180d_pct":50.2,"mae_180d_pct":-32.7,"peak_price_180d":89500,"trough_price_180d":40100,"result_bucket":"positive_with_high_MAE_watch","score_return_alignment":"stage2_yellow_correct_green_requires_margin_bridge","current_profile_residual":"late_4b_watch_needed_after_vertical_move","data_quality_label":"usable_with_caveat","source_proxy_only":true,"evidence_url_pending":true,"do_not_promote_to_production":true}
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","round":"R3","loop":"100","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C11_BATTERY_ORDERBOOK_RERATING","fine_archetype_id":"BATTERY_EQUIPMENT_SEPARATOR_ORDERBOOK_DELIVERY_MARGIN_BRIDGE_VS_ORDERBOOK_LABEL_REVERSAL","case_id":"C11-L100-02","symbol":"137400","name":"피엔티","trigger_date":"2024-06-11","entry_date":"2024-06-12","entry_price":80900,"trigger_type":"late_orderbook_chase_after_vertical_move","trigger_family":"battery_equipment_late_orderbook_chase","price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","mfe_30d_pct":10.6,"mae_30d_pct":-28.6,"mfe_90d_pct":10.6,"mae_90d_pct":-35.7,"mfe_180d_pct":10.6,"mae_180d_pct":-50.4,"peak_price_180d":89500,"trough_price_180d":40100,"result_bucket":"counterexample_high_MAE","score_return_alignment":"green_should_be_blocked_by_4b_local_proximity","current_profile_residual":"orderbook_label_after_vertical_leg_needs_stricter_no_chase_guard","data_quality_label":"usable_with_caveat","source_proxy_only":true,"evidence_url_pending":true,"do_not_promote_to_production":true}
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","round":"R3","loop":"100","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C11_BATTERY_ORDERBOOK_RERATING","fine_archetype_id":"BATTERY_EQUIPMENT_SEPARATOR_ORDERBOOK_DELIVERY_MARGIN_BRIDGE_VS_ORDERBOOK_LABEL_REVERSAL","case_id":"C11-L100-03","symbol":"222080","name":"씨아이에스","trigger_date":"2024-03-05","entry_date":"2024-03-06","entry_price":13290,"trigger_type":"equipment_orderbook_theme_spike","trigger_family":"battery_equipment_orderbook_theme_spike_without_margin_bridge","price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","mfe_30d_pct":13.7,"mae_30d_pct":-16.4,"mfe_90d_pct":13.7,"mae_90d_pct":-31.4,"mfe_180d_pct":13.7,"mae_180d_pct":-42.8,"peak_price_180d":15110,"trough_price_180d":7600,"result_bucket":"counterexample_bridge_missing","score_return_alignment":"yellow_ok_green_false_positive","current_profile_residual":"stage2_bonus_too_generous_when_orderbook_vocabulary_lacks_delivery_margin_bridge","data_quality_label":"usable_with_caveat","source_proxy_only":true,"evidence_url_pending":true,"do_not_promote_to_production":true}
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","round":"R3","loop":"100","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C11_BATTERY_ORDERBOOK_RERATING","fine_archetype_id":"BATTERY_EQUIPMENT_SEPARATOR_ORDERBOOK_DELIVERY_MARGIN_BRIDGE_VS_ORDERBOOK_LABEL_REVERSAL","case_id":"C11-L100-04","symbol":"222080","name":"씨아이에스","trigger_date":"2024-02-15","entry_date":"2024-02-16","entry_price":11170,"trigger_type":"early_equipment_orderbook_reacceleration","trigger_family":"battery_equipment_early_orderbook_reacceleration","price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","mfe_30d_pct":35.3,"mae_30d_pct":-0.7,"mfe_90d_pct":35.3,"mae_90d_pct":-25.4,"mfe_180d_pct":35.3,"mae_180d_pct":-32.0,"peak_price_180d":15110,"trough_price_180d":7600,"result_bucket":"marginal_positive_then_decay","score_return_alignment":"stage2_timing_useful_but_green_needs_revision_bridge","current_profile_residual":"good_MFE_does_not_equal_structural_rerating_when_decay_follows","data_quality_label":"usable_with_caveat","source_proxy_only":true,"evidence_url_pending":true,"do_not_promote_to_production":true}
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","round":"R3","loop":"100","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C11_BATTERY_ORDERBOOK_RERATING","fine_archetype_id":"BATTERY_EQUIPMENT_SEPARATOR_ORDERBOOK_DELIVERY_MARGIN_BRIDGE_VS_ORDERBOOK_LABEL_REVERSAL","case_id":"C11-L100-05","symbol":"299030","name":"하나기술","trigger_date":"2024-02-21","entry_date":"2024-02-22","entry_price":61000,"trigger_type":"battery_equipment_orderbook_label_reversal","trigger_family":"battery_equipment_orderbook_label_without_delivery_margin_bridge","price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","mfe_30d_pct":19.8,"mae_30d_pct":-6.4,"mfe_90d_pct":19.8,"mae_90d_pct":-41.7,"mfe_180d_pct":19.8,"mae_180d_pct":-55.7,"peak_price_180d":73100,"trough_price_180d":27000,"result_bucket":"false_positive_high_MAE","score_return_alignment":"stage2_should_be_capped_without_margin_revenue_bridge","current_profile_residual":"orderbook_label_needs_no_promotion_until_delivery_acceptance_visible","data_quality_label":"usable_with_caveat","source_proxy_only":true,"evidence_url_pending":true,"do_not_promote_to_production":true}
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","round":"R3","loop":"100","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C11_BATTERY_ORDERBOOK_RERATING","fine_archetype_id":"BATTERY_EQUIPMENT_SEPARATOR_ORDERBOOK_DELIVERY_MARGIN_BRIDGE_VS_ORDERBOOK_LABEL_REVERSAL","case_id":"C11-L100-06","symbol":"393890","name":"더블유씨피","trigger_date":"2024-02-21","entry_date":"2024-02-22","entry_price":47100,"trigger_type":"separator_orderbook_demand_bridge_missing","trigger_family":"battery_separator_orderbook_without_utilization_bridge","price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","mfe_30d_pct":5.1,"mae_30d_pct":-21.7,"mfe_90d_pct":5.1,"mae_90d_pct":-35.8,"mfe_180d_pct":5.1,"mae_180d_pct":-55.4,"peak_price_180d":49500,"trough_price_180d":21000,"result_bucket":"counterexample_calloff_shadow","score_return_alignment":"yellow_only_and_fast_4b_watch","current_profile_residual":"separator_orderbook_requires_utilization_and_customer_pull_evidence","data_quality_label":"clean_tradable_path","source_proxy_only":true,"evidence_url_pending":true,"do_not_promote_to_production":true}
```

## 6. Aggregate and residual contribution

```json
{"row_type":"aggregate_metric","schema_family":"v12_sector_archetype_residual","round":"R3","loop":"100","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C11_BATTERY_ORDERBOOK_RERATING","trigger_row_count":6,"positive_count":1,"marginal_positive_count":1,"counterexample_count":4,"median_mfe_90d_pct":16.75,"median_mae_90d_pct":-28.4,"median_mfe_180d_pct":16.75,"median_mae_180d_pct":-37.4,"high_mae_row_count":5,"source_proxy_only_count":6,"evidence_url_pending_count":6,"production_patch_ready":false}
```

The residual contribution is not “C11 is bad.” It is narrower:

```text
C11 positive signal survives when:
  orderbook / customer capacity / delivery acceptance
  AND revenue recognition or margin/revision bridge
  AND no vertical price-only extension

C11 false positive grows when:
  orderbook vocabulary appears after a vertical move
  OR equipment/material label moves without delivery acceptance
  OR EV demand/call-off shadow is present
```

## 7. Current calibrated profile stress test

| current profile behavior | observed in this loop | recommended shadow handling |
|---|---|---|
| Stage2 can recognize actionable orderbook evidence early | Useful in C11-L100-01 and C11-L100-04 | Keep Stage2/Yellow recognition. |
| Stage3-Green strictness requires non-price bridge | Needed in all rows | Do not loosen Green for orderbook label alone. |
| 4B price-only / non-price requirement | Required for C11-L100-02 | Add local 4B watch when orderbook label arrives after a vertical price leg. |
| 4C thesis break timing | Relevant but not direct production patch | Keep as watch unless call-off/utilization/margin break is explicit. |

## 8. Shadow rule candidate

```json
{"row_type":"shadow_weight","schema_family":"v12_sector_archetype_residual","round":"R3","loop":"100","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C11_BATTERY_ORDERBOOK_RERATING","candidate_axis":"stage2_required_bridge","candidate_rule":"For C11, orderbook/backlog wording alone cannot promote beyond Yellow unless at least one of delivery acceptance, utilization, revenue recognition, margin bridge, or revision bridge is visible as-of trigger_date.","expected_effect":"reduce false Stage3-Green from battery-equipment/material orderbook label spikes","apply_next_patch":false,"hold_reason":"all rows are source_proxy_only/evidence_url_pending"}
{"row_type":"shadow_weight","schema_family":"v12_sector_archetype_residual","round":"R3","loop":"100","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C11_BATTERY_ORDERBOOK_RERATING","candidate_axis":"local_4b_watch_guard","candidate_rule":"If C11 trigger occurs after a vertical price leg and lacks fresh delivery/margin evidence, classify as 4B local watch rather than new Stage3-Green even when orderbook vocabulary is present.","expected_effect":"block late-chase orderbook rerating labels after blowoff path","apply_next_patch":false,"hold_reason":"needs URL-confirmed non-price evidence before promotion"}
```

## 9. Validation scope

```text
validation_scope = historical_trigger_level_calibration
price_source_validation = pass
stock_web_1d_ohlc_used = true
forward_window_available = true
corporate_action_window_blocked = no current-window contamination found from profiles
round_sector_consistency = pass
round = R3
large_sector_id = L3_BATTERY_EV_GREEN_MOBILITY
canonical_archetype_id = C11_BATTERY_ORDERBOOK_RERATING
production_scoring_changed = false
shadow_weight_only = true
source_proxy_only = true
evidence_url_pending = true
```

## 10. Deferred Coding Agent Handoff Prompt

Do not execute now.

```text
When batch-applying v12 residual research, ingest this MD as a C11_BATTERY_ORDERBOOK_RERATING shadow ledger item only.

Required parser expectations:
- Parse all row_type=trigger JSONL rows.
- Preserve large_sector_id=L3_BATTERY_EV_GREEN_MOBILITY and canonical_archetype_id=C11_BATTERY_ORDERBOOK_RERATING.
- Treat source_proxy_only=true and evidence_url_pending=true as blocking production patch promotion.
- Use this MD to support a future C11 stage2_required_bridge and local_4b_watch_guard only after URL evidence is rematerialized.

Candidate implementation direction after URL rematerialization:
- Add C11-specific bridge requirement for Stage3-Green:
  orderbook/backlog wording must be accompanied by delivery acceptance, utilization, revenue recognition, margin bridge, or revision bridge.
- Add C11 local 4B watch:
  if a C11 trigger follows a vertical price leg and lacks fresh non-price bridge evidence, cap at Yellow/4B-watch.
```

## 11. Next research state

```text
completed_round = R3
completed_loop = 100
selection_basis = docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket = Priority 0
next_recommended_archetypes = C02_POWER_GRID_DATACENTER_CAPEX, C19_BRAND_RETAIL_INVENTORY_MARGIN, C27_CONTENT_IP_GLOBAL_MONETIZATION, C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK, C13_BATTERY_JV_UTILIZATION_AMPC_IRA
round_schedule_status = coverage_index_selected
round_sector_consistency = pass
```
