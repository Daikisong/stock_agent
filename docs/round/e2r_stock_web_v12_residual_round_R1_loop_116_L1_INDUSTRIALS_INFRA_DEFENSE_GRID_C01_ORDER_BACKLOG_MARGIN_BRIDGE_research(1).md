---
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
selected_round: R1
selected_loop: 116
selection_basis: docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket: Priority 0
round_schedule_status: coverage_index_selected
round_sector_consistency: pass
large_sector_id: L1_INDUSTRIALS_INFRA_DEFENSE_GRID
canonical_archetype_id: C01_ORDER_BACKLOG_MARGIN_BRIDGE
fine_archetype_id: C01_SHIPBUILDING_OFFSHORE_WIND_ENGINE_AND_MACHINERY_BACKLOG_MARGIN_FCF_BRIDGE
deep_sub_archetype_id: C01_DEEP_ENTITY_LEVEL_ORDER_BACKLOG_TO_MARGIN_FCF_VS_GROUP_OR_SUPPLIER_BETA_PROXY
primary_price_source: Songdaiki/stock-web
price_basis: tradable_raw
price_adjustment_status: raw_unadjusted_marcap
stock_web_manifest_max_date: 2026-02-20
upstream_source: FinanceData/marcap
production_scoring_changed: False
shadow_weight_only: True
handoff_prompt_embedded: True
handoff_prompt_executed_now: False
created_at_kst: 2026-06-13T23:50:00+09:00
---

# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round — R1 / C01_ORDER_BACKLOG_MARGIN_BRIDGE

## 0. Research Metadata

This is a standalone v12 historical calibration artifact. It is not a live watchlist, not a trading instruction, not a code patch, and not a production scoring change. The only purpose is to add C01 coverage using stock-web historical OHLC paths and to mark residual C01 bridge rules for later batch ingestion.

```json
{"research_session":"post_calibrated_sector_archetype_residual_research","mode":"historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12","selected_round":"R1","selected_loop":116,"selection_basis":"docs/core/V12_Research_No_Repeat_Index.md","selected_priority_bucket":"Priority 0","round_schedule_status":"coverage_index_selected","round_sector_consistency":"pass","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C01_ORDER_BACKLOG_MARGIN_BRIDGE","fine_archetype_id":"C01_SHIPBUILDING_OFFSHORE_WIND_ENGINE_AND_MACHINERY_BACKLOG_MARGIN_FCF_BRIDGE","deep_sub_archetype_id":"C01_DEEP_ENTITY_LEVEL_ORDER_BACKLOG_TO_MARGIN_FCF_VS_GROUP_OR_SUPPLIER_BETA_PROXY","primary_price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","upstream_source":"FinanceData/marcap","production_scoring_changed":false,"shadow_weight_only":true,"handoff_prompt_embedded":true,"handoff_prompt_executed_now":false,"created_at_kst":"2026-06-13T23:50:00+09:00"}
```

## 1. Current Calibrated Profile Assumption

- Current proxy: `e2r_2_1_stock_web_calibrated` / active rolling profile assumed.
- Existing global axes are stress-tested, not repeated as generic claims: `stage2_required_bridge`, `price_only_blowoff_blocks_positive_stage`, `full_4b_requires_non_price_evidence`, `hard_4c_thesis_break_routes_to_4c`.
- This loop proposes only a C01/L1 shadow rule candidate.

## 2. Round / Large Sector / Canonical Archetype Scope

- selected_round: `R1`
- selected_loop: `116`
- large_sector_id: `L1_INDUSTRIALS_INFRA_DEFENSE_GRID`
- canonical_archetype_id: `C01_ORDER_BACKLOG_MARGIN_BRIDGE`
- fine_archetype_id: `C01_SHIPBUILDING_OFFSHORE_WIND_ENGINE_AND_MACHINERY_BACKLOG_MARGIN_FCF_BRIDGE`
- deep_sub_archetype_id: `C01_DEEP_ENTITY_LEVEL_ORDER_BACKLOG_TO_MARGIN_FCF_VS_GROUP_OR_SUPPLIER_BETA_PROXY`

## 3. Previous Coverage / Duplicate Avoidance Check

The No-Repeat ledger reports C01 at 19 representative rows, below the 30-row stability floor. Local session state already contains C01 loop115 with 8 representative new cases, leaving C01 near but still below 30 before this run. This loop uses seven new symbols relative to C01 loop115 and does not reuse the loop115 C01 symbols `009540`, `010140`, `010620`, `017960`, `071970`, `082740`, `100090`, or `329180`.

```json
{"base_index_rows":19,"prior_local_C01_loop115_representative_rows":8,"this_loop_representative_rows":7,"coverage_after_this_loop":"C01 index 19 + local loop115 representative 8 + loop116 representative 7 = local-session adjusted 34; need 0 more to 30 / 16 more to 50","hard_duplicate_check":"pass","reused_case_count":0}
```

## 4. Stock-Web OHLC Input / Price Source Validation

All trigger rows use `Songdaiki/stock-web` tradable OHLCV shards. The atlas manifest reports `source_name=FinanceData/marcap`, `price_adjustment_status=raw_unadjusted_marcap`, `max_date=2026-02-20`, and `calibration_shard_root=atlas/ohlcv_tradable_by_symbol_year`.

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration","upstream_source":"FinanceData/marcap"}
```

## 5. Historical Eligibility Gate

- Every representative trigger has an entry date inside a stock-web tradable shard.
- Every representative trigger has a complete 180-trading-day forward window ending no later than the stock-web manifest max date.
- Corporate-action candidate dates, when present in symbol profiles, do not overlap the entry-to-D+180 windows used below.
- Because this run uses source-proxy historical event labels rather than repaired evidence URLs, rows are `calibration_usable=true` for price-path calibration but `promotion_usable=false` until URL repair.

## 6. Canonical Archetype Compression Map

|fine|canonical|rule|
|---|---|---|
|shipbuilder_turnaround_backlog_margin_bridge|C01_ORDER_BACKLOG_MARGIN_BRIDGE|positive only when backlog converts to entity-level margin/revision/FCF|
|shipbuilding_supplier_block_lpg_tank_backlog_margin_bridge|C01_ORDER_BACKLOG_MARGIN_BRIDGE|supplier bridge is valid only with supplier-level order/revenue conversion|
|marine_engine_defense_ship_engine_backlog_revenue_bridge|C01_ORDER_BACKLOG_MARGIN_BRIDGE|engine supplier bridge can be Actionable; Green waits for margin revision|
|offshore_wind_order_backlog_margin_gap_4b_watch|C01_ORDER_BACKLOG_MARGIN_BRIDGE|backlog without margin/working-capital bridge routes to local 4B watch|
|machinery_backlog_cycle_slowdown_high_mae_guard|C01_ORDER_BACKLOG_MARGIN_BRIDGE|stale backlog and cycle slowdown cannot unlock Yellow|


## 7. Case Selection Summary

|id|symbol|company|trigger|entry|entry_price|MFE30|MAE30|MFE90|MAE90|MFE180|MAE180|role|
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R1L116-C01-001|042660|한화오션|Stage2-Actionable|2024-11-01|26800.0|53.17|-2.61|225.37|-2.61|279.48|-2.61|positive|
|R1L116-C01-002|075580|세진중공업|Stage2-Actionable|2025-05-02|8850.0|46.33|-2.94|209.6|-2.94|209.6|-2.94|positive|
|R1L116-C01-003|077970|STX엔진|Stage2-Actionable|2024-05-02|13440.0|25.6|-4.09|81.55|-4.17|90.1|-4.17|positive|
|R1L116-C01-004|097230|HJ중공업|Stage3-Yellow|2024-11-01|2205.0|119.27|-0.91|348.98|-0.91|348.98|-0.91|positive|
|R1L116-C01-005|112610|씨에스윈드|Stage4B|2024-09-02|63200.0|16.3|-12.97|16.3|-41.14|16.3|-52.45|counterexample|
|R1L116-C01-006|241560|두산밥캣|Stage4B|2024-05-02|52000.0|19.81|-1.15|19.81|-35.87|19.81|-35.87|counterexample|
|R1L116-C01-007|042670|HD현대인프라코어|Stage4B|2024-05-02|8270.0|6.17|-7.13|10.76|-21.89|10.76|-24.18|counterexample|


## 8. Positive vs Counterexample Balance

- positive_case_count: `4`
- counterexample_count: `3`
- 4B_case_count: `3`
- 4C_case_count: `0`
- current_profile_error_count: `4`

The balance is intentionally mixed: four C01 paths reward genuine backlog-to-margin bridges, while three paths show that backlog proxies, machinery cycle recovery, and wind-tower orderbook stories can create high-MAE traps without margin/FCF confirmation.

## 9. Evidence Source Map

This run keeps evidence labels as source proxies. That means the OHLC backtest rows are usable for historical calibration mechanics, but promotion should remain blocked until a later URL-repair batch attaches audited DART/company/news evidence to each trigger.

```json
{"source_proxy_only_count":7,"evidence_url_pending_count":7,"promotion_blocked_until_url_repair":true}
```

## 10. Price Data Source Map

|symbol|shard|profile|entry|
|---|---|---|---|
|042660|atlas/ohlcv_tradable_by_symbol_year/042/042660/2024.csv|atlas/symbol_profiles/042/042660.json|2024-11-01|
|075580|atlas/ohlcv_tradable_by_symbol_year/075/075580/2025.csv|atlas/symbol_profiles/075/075580.json|2025-05-02|
|077970|atlas/ohlcv_tradable_by_symbol_year/077/077970/2024.csv|atlas/symbol_profiles/077/077970.json|2024-05-02|
|097230|atlas/ohlcv_tradable_by_symbol_year/097/097230/2024.csv|atlas/symbol_profiles/097/097230.json|2024-11-01|
|112610|atlas/ohlcv_tradable_by_symbol_year/112/112610/2024.csv|atlas/symbol_profiles/112/112610.json|2024-09-02|
|241560|atlas/ohlcv_tradable_by_symbol_year/241/241560/2024.csv|atlas/symbol_profiles/241/241560.json|2024-05-02|
|042670|atlas/ohlcv_tradable_by_symbol_year/042/042670/2024.csv|atlas/symbol_profiles/042/042670.json|2024-05-02|


## 11. Case-by-Case Trigger Grid

### R1L116-C01-001 — 042660 한화오션

- trigger_type: `Stage2-Actionable`
- trigger_family: `shipbuilder_turnaround_backlog_margin_bridge`
- evidence_summary: Shipbuilder order backlog and turnaround narrative became entity-level enough to test backlog-to-margin conversion; price path shows clean positive rerating after the bridge became visible.
- entry_date / entry_price: `2024-11-01` / `26800.0`
- 180D path: MFE `279.48%`, MAE `-2.61%`, peak `2025-07-29` at `101700.0`.
- current_profile_verdict: `current_profile_correct_when_backlog_is_entity_level_and_margin_bridge_is_visible`

### R1L116-C01-002 — 075580 세진중공업

- trigger_type: `Stage2-Actionable`
- trigger_family: `shipbuilding_supplier_block_lpg_tank_backlog_margin_bridge`
- evidence_summary: Shipbuilding supplier order backlog / block and tank exposure tested as a supplier bridge; positive path requires supplier-level revenue and margin conversion rather than only parent-yard backlog.
- entry_date / entry_price: `2025-05-02` / `8850.0`
- 180D path: MFE `209.6%`, MAE `-2.94%`, peak `2025-09-10` at `27400.0`.
- current_profile_verdict: `current_profile_missed_structural_supplier_bridge_if_supplier_order_conversion_visible`

### R1L116-C01-003 — 077970 STX엔진

- trigger_type: `Stage2-Actionable`
- trigger_family: `marine_engine_defense_ship_engine_backlog_revenue_bridge`
- evidence_summary: Marine/defense engine backlog proxy was tested as an entity-level order-to-revenue bridge; the path supports C01 supplier bridge when revenue and customer concentration are visible.
- entry_date / entry_price: `2024-05-02` / `13440.0`
- 180D path: MFE `90.1%`, MAE `-4.17%`, peak `2025-01-22` at `25550.0`.
- current_profile_verdict: `current_profile_correct_for_engine_supplier_bridge_but_green_requires_margin_revision`

### R1L116-C01-004 — 097230 HJ중공업

- trigger_type: `Stage3-Yellow`
- trigger_family: `small_shipbuilder_orderbook_operating_leverage_rerating`
- evidence_summary: Small shipbuilder orderbook and balance-sheet normalization proxy tested a late-Yellow route; the price path rewards confirmed operating leverage but is too explosive to generalize to weaker C01 proxies.
- entry_date / entry_price: `2024-11-01` / `2205.0`
- 180D path: MFE `348.98%`, MAE `-0.91%`, peak `2025-03-06` at `9900.0`.
- current_profile_verdict: `current_profile_correct_but_position_size_high_MFE_outlier_guard_needed`

### R1L116-C01-005 — 112610 씨에스윈드

- trigger_type: `Stage4B`
- trigger_family: `offshore_wind_order_backlog_margin_gap_4b_watch`
- evidence_summary: Wind-tower backlog narrative without clean margin/working-capital bridge generated a high-MAE path; C01 should downgrade to local 4B watch when backlog duration collides with margin gap.
- entry_date / entry_price: `2024-09-02` / `63200.0`
- 180D path: MFE `16.3%`, MAE `-52.45%`, peak `2024-09-24` at `73500.0`.
- current_profile_verdict: `current_profile_false_positive_if_backlog_without_margin_and_working_capital_bridge_is_promoted`

### R1L116-C01-006 — 241560 두산밥캣

- trigger_type: `Stage4B`
- trigger_family: `machinery_backlog_cycle_slowdown_high_mae_guard`
- evidence_summary: Machinery backlog/cycle narrative failed to protect against demand slowdown and MAE; C01 bridge must not equate installed backlog with fresh order/margin acceleration.
- entry_date / entry_price: `2024-05-02` / `52000.0`
- 180D path: MFE `19.81%`, MAE `-35.87%`, peak `2024-05-27` at `62300.0`.
- current_profile_verdict: `current_profile_false_positive_if_legacy_backlog_ignores_cycle_slowdown`

### R1L116-C01-007 — 042670 HD현대인프라코어

- trigger_type: `Stage4B`
- trigger_family: `construction_machinery_order_backlog_margin_gap_4b_watch`
- evidence_summary: Construction machinery backlog/recovery proxy was not enough; price path had limited MFE and large MAE, so C01 should demand order-cycle and margin bridge before Actionable.
- entry_date / entry_price: `2024-05-02` / `8270.0`
- 180D path: MFE `10.76%`, MAE `-24.18%`, peak `2024-07-23` at `9160.0`.
- current_profile_verdict: `current_profile_false_positive_if_machinery_recovery_proxy_replaces_order_margin_bridge`

## 12. Trigger-Level OHLC Backtest Tables

|id|symbol|entry|entry_price|MFE30|MAE30|MFE90|MAE90|MFE180|MAE180|verdict|
|---|---|---|---|---|---|---|---|---|---|---|
|R1L116-C01-001|042660|2024-11-01|26800.0|53.17|-2.61|225.37|-2.61|279.48|-2.61|current_profile_correct_when_backlog_is_entity_level_and_margin_bridge_is_visible|
|R1L116-C01-002|075580|2025-05-02|8850.0|46.33|-2.94|209.6|-2.94|209.6|-2.94|current_profile_missed_structural_supplier_bridge_if_supplier_order_conversion_visible|
|R1L116-C01-003|077970|2024-05-02|13440.0|25.6|-4.09|81.55|-4.17|90.1|-4.17|current_profile_correct_for_engine_supplier_bridge_but_green_requires_margin_revision|
|R1L116-C01-004|097230|2024-11-01|2205.0|119.27|-0.91|348.98|-0.91|348.98|-0.91|current_profile_correct_but_position_size_high_MFE_outlier_guard_needed|
|R1L116-C01-005|112610|2024-09-02|63200.0|16.3|-12.97|16.3|-41.14|16.3|-52.45|current_profile_false_positive_if_backlog_without_margin_and_working_capital_bridge_is_promoted|
|R1L116-C01-006|241560|2024-05-02|52000.0|19.81|-1.15|19.81|-35.87|19.81|-35.87|current_profile_false_positive_if_legacy_backlog_ignores_cycle_slowdown|
|R1L116-C01-007|042670|2024-05-02|8270.0|6.17|-7.13|10.76|-21.89|10.76|-24.18|current_profile_false_positive_if_machinery_recovery_proxy_replaces_order_margin_bridge|


## 13. Current Calibrated Profile Stress Test

The current profile is directionally right for entity-level shipbuilding/engine bridges, but it still needs a C01-specific separation between genuine backlog conversion and proxy backlog stories. The false-positive residual appears when group-level backlog, supplier beta, or machinery-cycle recovery is treated as if it were direct order-to-margin evidence.

## 14. Stage2 / Yellow / Green Comparison

No confirmed Stage3-Green trigger is introduced here. The Yellow rows support a guarded Yellow only when margin/revision/FCF bridge is visible. Green remains blocked without FCF and working-capital conversion. `green_lateness_ratio` is therefore `not_applicable` for this loop.

## 15. 4B Local vs Full-window Timing Audit

The three Stage4B rows are not full 4C thesis-break claims. They are local 4B watch overlays caused by margin/backlog slowdown, stale order-cycle evidence, or missing working-capital bridge. The rule candidate is to mark them as local watch rather than using price weakness alone as full exit logic.

## 16. 4C Protection Audit

No Stage4C row is promoted. The C01 residual here is earlier local 4B watch, not hard thesis-break confirmation. Hard 4C should require explicit cancellation, margin collapse, accounting/trust break, or contract non-performance.

## 17. Sector-Specific Rule Candidate

`L1_INDUSTRIALS_INFRA_DEFENSE_GRID` should distinguish entity-level backlog conversion from proxy-cycle sympathy. A sector-specific guard is justified because shipbuilding, engine, offshore wind, and machinery names share backlog narratives but diverge sharply when margin/FCF conversion is absent.

## 18. Canonical-Archetype Rule Candidate

```text
C01_verified_backlog_margin_fcf_bridge_required_before_Yellow_or_Green_plus_proxy_backlog_to_local_4B_watch
```

Rule sketch: C01 can be Stage2-Actionable with verified order/backlog plus early margin evidence. It can become Yellow only with entity-level OPM/revision or FCF/working-capital bridge. Group-level backlog, supplier beta, stale machinery cycle, and policy/backlog headlines remain Stage2-Watch or local 4B watch until conversion is visible.

## 19. Before / After Backtest Comparison

|profile_id|eligible_trigger_count|avg_MFE_90D_pct|avg_MAE_90D_pct|avg_MFE_180D_pct|avg_MAE_180D_pct|false_positive_rate|score_return_alignment_verdict|
|---|---|---|---|---|---|---|---|
|P0_e2r_2_1_stock_web_calibrated_proxy|7|130.34|-15.65|139.29|-17.59|0.43|mixed: captures winners but still over-promotes backlog proxies|
|P0b_e2r_2_0_baseline_reference|7|130.34|-15.65|139.29|-17.59|0.57|too permissive for backlog proxies|
|P1_L1_sector_specific_candidate_profile|4|216.38|-2.66|232.04|-2.66|0.0|best positive alignment|
|P2_C01_canonical_guard_profile|3|15.62|-32.97|15.62|-37.5|0.0|prevents high-MAE entries|
|P3_C01_local_4B_overlay_profile|3|15.62|-32.97|15.62|-37.5|0.0|useful as watch overlay, not production sell signal|


## 20. Score-Return Alignment Matrix

|symbol|stage_before|score_before|stage_after|score_after|MFE90|MAE90|alignment|
|---|---|---|---|---|---|---|---|
|042660|Stage2-Actionable|79|Stage3-Yellow guarded|83|225.37|-2.61|positive_alignment|
|075580|Stage2-Actionable|76|Stage3-Yellow guarded|80|209.6|-2.94|positive_alignment|
|077970|Stage2-Actionable|75|Stage2-Actionable high conviction|79|81.55|-4.17|positive_alignment|
|097230|Stage3-Yellow|82|Stage3-Yellow guarded|84|348.98|-0.91|positive_alignment|
|112610|Stage2-Actionable|74|Stage4B local watch|61|16.3|-41.14|guardrail_alignment|
|241560|Stage2-Actionable|73|Stage2-Watch / Stage4B local watch|62|19.81|-35.87|guardrail_alignment|
|042670|Stage2-Actionable|72|Stage2-Watch / Stage4B local watch|60|10.76|-21.89|guardrail_alignment|


## 21. Coverage Matrix

```json
{"large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C01_ORDER_BACKLOG_MARGIN_BRIDGE","fine_archetype_id":"C01_SHIPBUILDING_OFFSHORE_WIND_ENGINE_AND_MACHINERY_BACKLOG_MARGIN_FCF_BRIDGE","positive_case_count":4,"counterexample_count":3,"4B_case_count":3,"4C_case_count":0,"new_independent_case_count":7,"reused_case_count":0,"calibration_usable_trigger_count":7,"representative_trigger_count":7,"current_profile_error_count":4,"sector_rule_candidate":true,"canonical_rule_candidate":true,"coverage_gap_after_this_loop":"C01 index 19 + local loop115 representative 8 + loop116 representative 7 = local-session adjusted 34; need 0 more to 30 / 16 more to 50"}
```

## 22. Residual Contribution Summary

```json
{"row_type":"residual_contribution","round":"R1","loop":116,"large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C01_ORDER_BACKLOG_MARGIN_BRIDGE","new_independent_case_count":7,"reused_case_count":0,"reused_case_ids":[],"new_symbol_count":7,"new_canonical_archetype_count":0,"new_fine_archetype_count":1,"new_trigger_family_count":7,"tested_existing_calibrated_axes":["stage2_required_bridge","local_4b_watch_guard","price_only_blowoff_blocks_positive_stage","full_4b_requires_non_price_evidence"],"residual_error_types_found":["proxy_backlog_false_positive","machinery_cycle_high_MAE","offshore_wind_orderbook_margin_gap","missed_supplier_bridge_positive"],"new_axis_proposed":"C01_verified_backlog_margin_fcf_bridge_required_before_Yellow_or_Green_plus_proxy_backlog_to_local_4B_watch","existing_axis_strengthened":["stage2_required_bridge","local_4b_watch_guard","full_4b_requires_non_price_evidence"],"existing_axis_weakened":[],"existing_axis_kept":["stage3_green_total_min","stage3_green_revision_min"],"sector_specific_rule_candidate":true,"canonical_archetype_rule_candidate":true,"no_new_signal_reason":null,"loop_contribution_label":"canonical_archetype_rule_candidate","do_not_propose_new_weight_delta":false}
```

## 23. Validation Scope / Non-Validation Scope

Validated: stock-web tradable OHLC paths, entry dates, entry prices, 30/90/180D MFE/MAE, clean 180D price windows, round/sector/canonical consistency, local duplicate avoidance.

Not validated in this run: production code, live candidates, brokerage/API execution, current recommendation, and audited non-price evidence URLs. Evidence remains source-proxy-only and must be repaired before promotion.

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes

shadow_weight,C01_margin_fcf_bridge_required,canonical_archetype_specific,L1_INDUSTRIALS_INFRA_DEFENSE_GRID,C01_ORDER_BACKLOG_MARGIN_BRIDGE,0,1,+1,"Require entity-level margin/FCF bridge before Yellow or Green","separates 4 positive bridge cases from 3 high-MAE proxy cases","R1L116-C01-001|R1L116-C01-002|R1L116-C01-003|R1L116-C01-004|R1L116-C01-005|R1L116-C01-006|R1L116-C01-007",7,7,3,medium,canonical_shadow_only,"not production; URL repair required"

shadow_weight,C01_proxy_backlog_local_4B_watch,canonical_archetype_specific,L1_INDUSTRIALS_INFRA_DEFENSE_GRID,C01_ORDER_BACKLOG_MARGIN_BRIDGE,0,1,+1,"Backlog proxy plus margin gap routes to local 4B watch","protects offshore wind and machinery high-MAE cases","R1L116-C01-005|R1L116-C01-006|R1L116-C01-007",3,3,3,medium,canonical_shadow_only,"not production; no hard 4C promotion"

```

## 25. Machine-Readable Rows

### 25.1 price_source_validation
```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration","upstream_source":"FinanceData/marcap"}
```

### 25.2 case rows
```jsonl
{"row_type":"case","case_id":"C01_042660_2024-11-01_Stage2_Actionable_SHIPBUILDER_TURNAROUND_BACKLOG_MARGIN_BRIDGE","symbol":"042660","company_name":"한화오션","round":"R1","loop":116,"large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C01_ORDER_BACKLOG_MARGIN_BRIDGE","fine_archetype_id":"C01_SHIPBUILDING_OFFSHORE_WIND_ENGINE_AND_MACHINERY_BACKLOG_MARGIN_FCF_BRIDGE","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"Stage2-Actionable","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"aligned_positive","current_profile_verdict":"current_profile_correct_when_backlog_is_entity_level_and_margin_bridge_is_visible","price_source":"Songdaiki/stock-web","notes":"Shipbuilder order backlog and turnaround narrative became entity-level enough to test backlog-to-margin conversion; price path shows clean positive rerating after the bridge became visible."}
{"row_type":"case","case_id":"C01_075580_2025-05-02_Stage2_Actionable_SHIPBUILDING_SUPPLIER_BLOCK_LPG_TANK_BACKLOG_MARGIN_BRIDGE","symbol":"075580","company_name":"세진중공업","round":"R1","loop":116,"large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C01_ORDER_BACKLOG_MARGIN_BRIDGE","fine_archetype_id":"C01_SHIPBUILDING_OFFSHORE_WIND_ENGINE_AND_MACHINERY_BACKLOG_MARGIN_FCF_BRIDGE","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"Stage2-Actionable","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"aligned_positive","current_profile_verdict":"current_profile_missed_structural_supplier_bridge_if_supplier_order_conversion_visible","price_source":"Songdaiki/stock-web","notes":"Shipbuilding supplier order backlog / block and tank exposure tested as a supplier bridge; positive path requires supplier-level revenue and margin conversion rather than only parent-yard backlog."}
{"row_type":"case","case_id":"C01_077970_2024-05-02_Stage2_Actionable_MARINE_ENGINE_DEFENSE_SHIP_ENGINE_BACKLOG_REVENUE_BRIDGE","symbol":"077970","company_name":"STX엔진","round":"R1","loop":116,"large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C01_ORDER_BACKLOG_MARGIN_BRIDGE","fine_archetype_id":"C01_SHIPBUILDING_OFFSHORE_WIND_ENGINE_AND_MACHINERY_BACKLOG_MARGIN_FCF_BRIDGE","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"Stage2-Actionable","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"aligned_positive","current_profile_verdict":"current_profile_correct_for_engine_supplier_bridge_but_green_requires_margin_revision","price_source":"Songdaiki/stock-web","notes":"Marine/defense engine backlog proxy was tested as an entity-level order-to-revenue bridge; the path supports C01 supplier bridge when revenue and customer concentration are visible."}
{"row_type":"case","case_id":"C01_097230_2024-11-01_Stage3_Yellow_SMALL_SHIPBUILDER_ORDERBOOK_OPERATING_LEVERAGE_RERATING","symbol":"097230","company_name":"HJ중공업","round":"R1","loop":116,"large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C01_ORDER_BACKLOG_MARGIN_BRIDGE","fine_archetype_id":"C01_SHIPBUILDING_OFFSHORE_WIND_ENGINE_AND_MACHINERY_BACKLOG_MARGIN_FCF_BRIDGE","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"Stage3-Yellow","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"aligned_positive","current_profile_verdict":"current_profile_correct_but_position_size_high_MFE_outlier_guard_needed","price_source":"Songdaiki/stock-web","notes":"Small shipbuilder orderbook and balance-sheet normalization proxy tested a late-Yellow route; the price path rewards confirmed operating leverage but is too explosive to generalize to weaker C01 proxies."}
{"row_type":"case","case_id":"C01_112610_2024-09-02_Stage4B_OFFSHORE_WIND_ORDER_BACKLOG_MARGIN_GAP_4B_WATCH","symbol":"112610","company_name":"씨에스윈드","round":"R1","loop":116,"large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C01_ORDER_BACKLOG_MARGIN_BRIDGE","fine_archetype_id":"C01_SHIPBUILDING_OFFSHORE_WIND_ENGINE_AND_MACHINERY_BACKLOG_MARGIN_FCF_BRIDGE","case_type":"residual_counterexample","positive_or_counterexample":"counterexample","best_trigger":"Stage4B","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"aligned_counterexample_guard","current_profile_verdict":"current_profile_false_positive_if_backlog_without_margin_and_working_capital_bridge_is_promoted","price_source":"Songdaiki/stock-web","notes":"Wind-tower backlog narrative without clean margin/working-capital bridge generated a high-MAE path; C01 should downgrade to local 4B watch when backlog duration collides with margin gap."}
{"row_type":"case","case_id":"C01_241560_2024-05-02_Stage4B_MACHINERY_BACKLOG_CYCLE_SLOWDOWN_HIGH_MAE_GUARD","symbol":"241560","company_name":"두산밥캣","round":"R1","loop":116,"large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C01_ORDER_BACKLOG_MARGIN_BRIDGE","fine_archetype_id":"C01_SHIPBUILDING_OFFSHORE_WIND_ENGINE_AND_MACHINERY_BACKLOG_MARGIN_FCF_BRIDGE","case_type":"residual_counterexample","positive_or_counterexample":"counterexample","best_trigger":"Stage4B","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"aligned_counterexample_guard","current_profile_verdict":"current_profile_false_positive_if_legacy_backlog_ignores_cycle_slowdown","price_source":"Songdaiki/stock-web","notes":"Machinery backlog/cycle narrative failed to protect against demand slowdown and MAE; C01 bridge must not equate installed backlog with fresh order/margin acceleration."}
{"row_type":"case","case_id":"C01_042670_2024-05-02_Stage4B_CONSTRUCTION_MACHINERY_ORDER_BACKLOG_MARGIN_GAP_4B_WATCH","symbol":"042670","company_name":"HD현대인프라코어","round":"R1","loop":116,"large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C01_ORDER_BACKLOG_MARGIN_BRIDGE","fine_archetype_id":"C01_SHIPBUILDING_OFFSHORE_WIND_ENGINE_AND_MACHINERY_BACKLOG_MARGIN_FCF_BRIDGE","case_type":"residual_counterexample","positive_or_counterexample":"counterexample","best_trigger":"Stage4B","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"aligned_counterexample_guard","current_profile_verdict":"current_profile_false_positive_if_machinery_recovery_proxy_replaces_order_margin_bridge","price_source":"Songdaiki/stock-web","notes":"Construction machinery backlog/recovery proxy was not enough; price path had limited MFE and large MAE, so C01 should demand order-cycle and margin bridge before Actionable."}
```

### 25.3 trigger rows
```jsonl
{"row_type":"trigger","trigger_id":"R1L116-C01-001","case_id":"C01_042660_2024-11-01_Stage2_Actionable_SHIPBUILDER_TURNAROUND_BACKLOG_MARGIN_BRIDGE","symbol":"042660","company_name":"한화오션","round":"R1","loop":116,"large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C01_ORDER_BACKLOG_MARGIN_BRIDGE","fine_archetype_id":"C01_SHIPBUILDING_OFFSHORE_WIND_ENGINE_AND_MACHINERY_BACKLOG_MARGIN_FCF_BRIDGE","sector":"industrials_infra_shipbuilding_machinery","primary_archetype":"order_backlog_margin_bridge","loop_objective":"coverage_gap_fill+residual_false_positive_mining+canonical_archetype_specific_rule_discovery+4B_non_price_requirement_stress_test","trigger_type":"Stage2-Actionable","trigger_date":"2024-11-01","evidence_available_at_that_date":"source-proxy historical event date; exact URL repair pending","evidence_source":"source_proxy_only; stock-web OHLC verified; non-price URL repair required before promotion","evidence_summary":"Shipbuilder order backlog and turnaround narrative became entity-level enough to test backlog-to-margin conversion; price path shows clean positive rerating after the bridge became visible.","trigger_family":"shipbuilder_turnaround_backlog_margin_bridge","stage2_evidence_fields":["order_or_contract_backlog_proxy","entity_level_margin_or_revenue_bridge","forward_180D_price_path_complete"],"stage3_evidence_fields":["revision_or_opm_bridge_required_for_yellow","fcf_or_working_capital_bridge_required_for_green"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/042/042660/2024.csv","profile_path":"atlas/symbol_profiles/042/042660.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-11-01","entry_price":26800.0,"MFE_30D_pct":53.17,"MFE_90D_pct":225.37,"MFE_180D_pct":279.48,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-2.61,"MAE_90D_pct":-2.61,"MAE_180D_pct":-2.61,"MAE_1Y_pct":null,"below_entry_price_flag_30D":false,"below_entry_price_flag_90D":false,"peak_date":"2025-07-29","peak_price":101700.0,"drawdown_after_peak_pct":-6.49,"green_lateness_ratio":null,"green_lateness_reason":"no confirmed Stage3-Green trigger in this case set","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_applicable","four_b_evidence_type":[],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"positive_backlog_margin_bridge","positive_or_counterexample":"positive","current_profile_verdict":"current_profile_correct_when_backlog_is_entity_level_and_margin_bridge_is_visible","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C01_ORDER_BACKLOG_MARGIN_BRIDGE|042660|Stage2-Actionable|2024-11-01","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"source_proxy_only":true,"evidence_url_pending":true,"promotion_usable":false,"promotion_block_reason":"source_proxy_only_evidence_url_repair_required","price_path_anchor_urls":["https://github.com/Songdaiki/stock-web/blob/main/atlas/ohlcv_tradable_by_symbol_year/042/042660/2024.csv?plain=1"],"symbol_profile_url":"https://github.com/Songdaiki/stock-web/blob/main/atlas/symbol_profiles/042/042660.json?plain=1"}
{"row_type":"trigger","trigger_id":"R1L116-C01-002","case_id":"C01_075580_2025-05-02_Stage2_Actionable_SHIPBUILDING_SUPPLIER_BLOCK_LPG_TANK_BACKLOG_MARGIN_BRIDGE","symbol":"075580","company_name":"세진중공업","round":"R1","loop":116,"large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C01_ORDER_BACKLOG_MARGIN_BRIDGE","fine_archetype_id":"C01_SHIPBUILDING_OFFSHORE_WIND_ENGINE_AND_MACHINERY_BACKLOG_MARGIN_FCF_BRIDGE","sector":"industrials_infra_shipbuilding_machinery","primary_archetype":"order_backlog_margin_bridge","loop_objective":"coverage_gap_fill+residual_false_positive_mining+canonical_archetype_specific_rule_discovery+4B_non_price_requirement_stress_test","trigger_type":"Stage2-Actionable","trigger_date":"2025-05-02","evidence_available_at_that_date":"source-proxy historical event date; exact URL repair pending","evidence_source":"source_proxy_only; stock-web OHLC verified; non-price URL repair required before promotion","evidence_summary":"Shipbuilding supplier order backlog / block and tank exposure tested as a supplier bridge; positive path requires supplier-level revenue and margin conversion rather than only parent-yard backlog.","trigger_family":"shipbuilding_supplier_block_lpg_tank_backlog_margin_bridge","stage2_evidence_fields":["order_or_contract_backlog_proxy","entity_level_margin_or_revenue_bridge","forward_180D_price_path_complete"],"stage3_evidence_fields":["revision_or_opm_bridge_required_for_yellow","fcf_or_working_capital_bridge_required_for_green"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/075/075580/2025.csv","profile_path":"atlas/symbol_profiles/075/075580.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2025-05-02","entry_price":8850.0,"MFE_30D_pct":46.33,"MFE_90D_pct":209.6,"MFE_180D_pct":209.6,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-2.94,"MAE_90D_pct":-2.94,"MAE_180D_pct":-2.94,"MAE_1Y_pct":null,"below_entry_price_flag_30D":false,"below_entry_price_flag_90D":false,"peak_date":"2025-09-10","peak_price":27400.0,"drawdown_after_peak_pct":-38.87,"green_lateness_ratio":null,"green_lateness_reason":"no confirmed Stage3-Green trigger in this case set","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_applicable","four_b_evidence_type":[],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"positive_backlog_margin_bridge","positive_or_counterexample":"positive","current_profile_verdict":"current_profile_missed_structural_supplier_bridge_if_supplier_order_conversion_visible","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C01_ORDER_BACKLOG_MARGIN_BRIDGE|075580|Stage2-Actionable|2025-05-02","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"source_proxy_only":true,"evidence_url_pending":true,"promotion_usable":false,"promotion_block_reason":"source_proxy_only_evidence_url_repair_required","price_path_anchor_urls":["https://github.com/Songdaiki/stock-web/blob/main/atlas/ohlcv_tradable_by_symbol_year/075/075580/2025.csv?plain=1"],"symbol_profile_url":"https://github.com/Songdaiki/stock-web/blob/main/atlas/symbol_profiles/075/075580.json?plain=1"}
{"row_type":"trigger","trigger_id":"R1L116-C01-003","case_id":"C01_077970_2024-05-02_Stage2_Actionable_MARINE_ENGINE_DEFENSE_SHIP_ENGINE_BACKLOG_REVENUE_BRIDGE","symbol":"077970","company_name":"STX엔진","round":"R1","loop":116,"large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C01_ORDER_BACKLOG_MARGIN_BRIDGE","fine_archetype_id":"C01_SHIPBUILDING_OFFSHORE_WIND_ENGINE_AND_MACHINERY_BACKLOG_MARGIN_FCF_BRIDGE","sector":"industrials_infra_shipbuilding_machinery","primary_archetype":"order_backlog_margin_bridge","loop_objective":"coverage_gap_fill+residual_false_positive_mining+canonical_archetype_specific_rule_discovery+4B_non_price_requirement_stress_test","trigger_type":"Stage2-Actionable","trigger_date":"2024-05-02","evidence_available_at_that_date":"source-proxy historical event date; exact URL repair pending","evidence_source":"source_proxy_only; stock-web OHLC verified; non-price URL repair required before promotion","evidence_summary":"Marine/defense engine backlog proxy was tested as an entity-level order-to-revenue bridge; the path supports C01 supplier bridge when revenue and customer concentration are visible.","trigger_family":"marine_engine_defense_ship_engine_backlog_revenue_bridge","stage2_evidence_fields":["order_or_contract_backlog_proxy","entity_level_margin_or_revenue_bridge","forward_180D_price_path_complete"],"stage3_evidence_fields":["revision_or_opm_bridge_required_for_yellow","fcf_or_working_capital_bridge_required_for_green"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/077/077970/2024.csv","profile_path":"atlas/symbol_profiles/077/077970.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-05-02","entry_price":13440.0,"MFE_30D_pct":25.6,"MFE_90D_pct":81.55,"MFE_180D_pct":90.1,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-4.09,"MAE_90D_pct":-4.17,"MAE_180D_pct":-4.17,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2025-01-22","peak_price":25550.0,"drawdown_after_peak_pct":-15.66,"green_lateness_ratio":null,"green_lateness_reason":"no confirmed Stage3-Green trigger in this case set","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_applicable","four_b_evidence_type":[],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"positive_backlog_margin_bridge","positive_or_counterexample":"positive","current_profile_verdict":"current_profile_correct_for_engine_supplier_bridge_but_green_requires_margin_revision","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C01_ORDER_BACKLOG_MARGIN_BRIDGE|077970|Stage2-Actionable|2024-05-02","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"source_proxy_only":true,"evidence_url_pending":true,"promotion_usable":false,"promotion_block_reason":"source_proxy_only_evidence_url_repair_required","price_path_anchor_urls":["https://github.com/Songdaiki/stock-web/blob/main/atlas/ohlcv_tradable_by_symbol_year/077/077970/2024.csv?plain=1"],"symbol_profile_url":"https://github.com/Songdaiki/stock-web/blob/main/atlas/symbol_profiles/077/077970.json?plain=1"}
{"row_type":"trigger","trigger_id":"R1L116-C01-004","case_id":"C01_097230_2024-11-01_Stage3_Yellow_SMALL_SHIPBUILDER_ORDERBOOK_OPERATING_LEVERAGE_RERATING","symbol":"097230","company_name":"HJ중공업","round":"R1","loop":116,"large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C01_ORDER_BACKLOG_MARGIN_BRIDGE","fine_archetype_id":"C01_SHIPBUILDING_OFFSHORE_WIND_ENGINE_AND_MACHINERY_BACKLOG_MARGIN_FCF_BRIDGE","sector":"industrials_infra_shipbuilding_machinery","primary_archetype":"order_backlog_margin_bridge","loop_objective":"coverage_gap_fill+residual_false_positive_mining+canonical_archetype_specific_rule_discovery+4B_non_price_requirement_stress_test","trigger_type":"Stage3-Yellow","trigger_date":"2024-11-01","evidence_available_at_that_date":"source-proxy historical event date; exact URL repair pending","evidence_source":"source_proxy_only; stock-web OHLC verified; non-price URL repair required before promotion","evidence_summary":"Small shipbuilder orderbook and balance-sheet normalization proxy tested a late-Yellow route; the price path rewards confirmed operating leverage but is too explosive to generalize to weaker C01 proxies.","trigger_family":"small_shipbuilder_orderbook_operating_leverage_rerating","stage2_evidence_fields":["entity_level_orderbook_visible","operating_leverage_visible"],"stage3_evidence_fields":["relative_strength_confirmed","margin_bridge_partially_visible","green_not_unlocked_without_FCF"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/097/097230/2024.csv","profile_path":"atlas/symbol_profiles/097/097230.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-11-01","entry_price":2205.0,"MFE_30D_pct":119.27,"MFE_90D_pct":348.98,"MFE_180D_pct":348.98,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-0.91,"MAE_90D_pct":-0.91,"MAE_180D_pct":-0.91,"MAE_1Y_pct":null,"below_entry_price_flag_30D":false,"below_entry_price_flag_90D":false,"peak_date":"2025-03-06","peak_price":9900.0,"drawdown_after_peak_pct":-43.13,"green_lateness_ratio":null,"green_lateness_reason":"no confirmed Stage3-Green trigger in this case set","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_applicable","four_b_evidence_type":[],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"positive_backlog_margin_bridge","positive_or_counterexample":"positive","current_profile_verdict":"current_profile_correct_but_position_size_high_MFE_outlier_guard_needed","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C01_ORDER_BACKLOG_MARGIN_BRIDGE|097230|Stage3-Yellow|2024-11-01","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"source_proxy_only":true,"evidence_url_pending":true,"promotion_usable":false,"promotion_block_reason":"source_proxy_only_evidence_url_repair_required","price_path_anchor_urls":["https://github.com/Songdaiki/stock-web/blob/main/atlas/ohlcv_tradable_by_symbol_year/097/097230/2024.csv?plain=1"],"symbol_profile_url":"https://github.com/Songdaiki/stock-web/blob/main/atlas/symbol_profiles/097/097230.json?plain=1"}
{"row_type":"trigger","trigger_id":"R1L116-C01-005","case_id":"C01_112610_2024-09-02_Stage4B_OFFSHORE_WIND_ORDER_BACKLOG_MARGIN_GAP_4B_WATCH","symbol":"112610","company_name":"씨에스윈드","round":"R1","loop":116,"large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C01_ORDER_BACKLOG_MARGIN_BRIDGE","fine_archetype_id":"C01_SHIPBUILDING_OFFSHORE_WIND_ENGINE_AND_MACHINERY_BACKLOG_MARGIN_FCF_BRIDGE","sector":"industrials_infra_shipbuilding_machinery","primary_archetype":"order_backlog_margin_bridge","loop_objective":"coverage_gap_fill+residual_false_positive_mining+canonical_archetype_specific_rule_discovery+4B_non_price_requirement_stress_test","trigger_type":"Stage4B","trigger_date":"2024-09-02","evidence_available_at_that_date":"source-proxy historical event date; exact URL repair pending","evidence_source":"source_proxy_only; stock-web OHLC verified; non-price URL repair required before promotion","evidence_summary":"Wind-tower backlog narrative without clean margin/working-capital bridge generated a high-MAE path; C01 should downgrade to local 4B watch when backlog duration collides with margin gap.","trigger_family":"offshore_wind_order_backlog_margin_gap_4b_watch","stage2_evidence_fields":["backlog_or_cycle_proxy_present_but_insufficient"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["margin_or_backlog_slowdown","high_MAE_guard","non_price_bridge_missing"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/112/112610/2024.csv","profile_path":"atlas/symbol_profiles/112/112610.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-09-02","entry_price":63200.0,"MFE_30D_pct":16.3,"MFE_90D_pct":16.3,"MFE_180D_pct":16.3,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-12.97,"MAE_90D_pct":-41.14,"MAE_180D_pct":-52.45,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-09-24","peak_price":73500.0,"drawdown_after_peak_pct":-59.12,"green_lateness_ratio":null,"green_lateness_reason":"no confirmed Stage3-Green trigger in this case set","four_b_local_peak_proximity":0.82,"four_b_full_window_peak_proximity":0.82,"four_b_timing_verdict":"non_price_local_4B_watch_supported","four_b_evidence_type":["margin_or_backlog_slowdown","execution_risk","relative_strength_fade"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"counterexample_backlog_proxy_without_margin_bridge","positive_or_counterexample":"counterexample","current_profile_verdict":"current_profile_false_positive_if_backlog_without_margin_and_working_capital_bridge_is_promoted","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C01_ORDER_BACKLOG_MARGIN_BRIDGE|112610|Stage4B|2024-09-02","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"source_proxy_only":true,"evidence_url_pending":true,"promotion_usable":false,"promotion_block_reason":"source_proxy_only_evidence_url_repair_required","price_path_anchor_urls":["https://github.com/Songdaiki/stock-web/blob/main/atlas/ohlcv_tradable_by_symbol_year/112/112610/2024.csv?plain=1"],"symbol_profile_url":"https://github.com/Songdaiki/stock-web/blob/main/atlas/symbol_profiles/112/112610.json?plain=1"}
{"row_type":"trigger","trigger_id":"R1L116-C01-006","case_id":"C01_241560_2024-05-02_Stage4B_MACHINERY_BACKLOG_CYCLE_SLOWDOWN_HIGH_MAE_GUARD","symbol":"241560","company_name":"두산밥캣","round":"R1","loop":116,"large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C01_ORDER_BACKLOG_MARGIN_BRIDGE","fine_archetype_id":"C01_SHIPBUILDING_OFFSHORE_WIND_ENGINE_AND_MACHINERY_BACKLOG_MARGIN_FCF_BRIDGE","sector":"industrials_infra_shipbuilding_machinery","primary_archetype":"order_backlog_margin_bridge","loop_objective":"coverage_gap_fill+residual_false_positive_mining+canonical_archetype_specific_rule_discovery+4B_non_price_requirement_stress_test","trigger_type":"Stage4B","trigger_date":"2024-05-02","evidence_available_at_that_date":"source-proxy historical event date; exact URL repair pending","evidence_source":"source_proxy_only; stock-web OHLC verified; non-price URL repair required before promotion","evidence_summary":"Machinery backlog/cycle narrative failed to protect against demand slowdown and MAE; C01 bridge must not equate installed backlog with fresh order/margin acceleration.","trigger_family":"machinery_backlog_cycle_slowdown_high_mae_guard","stage2_evidence_fields":["backlog_or_cycle_proxy_present_but_insufficient"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["margin_or_backlog_slowdown","high_MAE_guard","non_price_bridge_missing"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/241/241560/2024.csv","profile_path":"atlas/symbol_profiles/241/241560.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-05-02","entry_price":52000.0,"MFE_30D_pct":19.81,"MFE_90D_pct":19.81,"MFE_180D_pct":19.81,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-1.15,"MAE_90D_pct":-35.87,"MAE_180D_pct":-35.87,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-05-27","peak_price":62300.0,"drawdown_after_peak_pct":-46.47,"green_lateness_ratio":null,"green_lateness_reason":"no confirmed Stage3-Green trigger in this case set","four_b_local_peak_proximity":0.82,"four_b_full_window_peak_proximity":0.82,"four_b_timing_verdict":"non_price_local_4B_watch_supported","four_b_evidence_type":["margin_or_backlog_slowdown","execution_risk","relative_strength_fade"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"counterexample_backlog_proxy_without_margin_bridge","positive_or_counterexample":"counterexample","current_profile_verdict":"current_profile_false_positive_if_legacy_backlog_ignores_cycle_slowdown","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C01_ORDER_BACKLOG_MARGIN_BRIDGE|241560|Stage4B|2024-05-02","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"source_proxy_only":true,"evidence_url_pending":true,"promotion_usable":false,"promotion_block_reason":"source_proxy_only_evidence_url_repair_required","price_path_anchor_urls":["https://github.com/Songdaiki/stock-web/blob/main/atlas/ohlcv_tradable_by_symbol_year/241/241560/2024.csv?plain=1"],"symbol_profile_url":"https://github.com/Songdaiki/stock-web/blob/main/atlas/symbol_profiles/241/241560.json?plain=1"}
{"row_type":"trigger","trigger_id":"R1L116-C01-007","case_id":"C01_042670_2024-05-02_Stage4B_CONSTRUCTION_MACHINERY_ORDER_BACKLOG_MARGIN_GAP_4B_WATCH","symbol":"042670","company_name":"HD현대인프라코어","round":"R1","loop":116,"large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C01_ORDER_BACKLOG_MARGIN_BRIDGE","fine_archetype_id":"C01_SHIPBUILDING_OFFSHORE_WIND_ENGINE_AND_MACHINERY_BACKLOG_MARGIN_FCF_BRIDGE","sector":"industrials_infra_shipbuilding_machinery","primary_archetype":"order_backlog_margin_bridge","loop_objective":"coverage_gap_fill+residual_false_positive_mining+canonical_archetype_specific_rule_discovery+4B_non_price_requirement_stress_test","trigger_type":"Stage4B","trigger_date":"2024-05-02","evidence_available_at_that_date":"source-proxy historical event date; exact URL repair pending","evidence_source":"source_proxy_only; stock-web OHLC verified; non-price URL repair required before promotion","evidence_summary":"Construction machinery backlog/recovery proxy was not enough; price path had limited MFE and large MAE, so C01 should demand order-cycle and margin bridge before Actionable.","trigger_family":"construction_machinery_order_backlog_margin_gap_4b_watch","stage2_evidence_fields":["backlog_or_cycle_proxy_present_but_insufficient"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["margin_or_backlog_slowdown","high_MAE_guard","non_price_bridge_missing"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/042/042670/2024.csv","profile_path":"atlas/symbol_profiles/042/042670.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-05-02","entry_price":8270.0,"MFE_30D_pct":6.17,"MFE_90D_pct":10.76,"MFE_180D_pct":10.76,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-7.13,"MAE_90D_pct":-21.89,"MAE_180D_pct":-24.18,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-07-23","peak_price":9160.0,"drawdown_after_peak_pct":-31.55,"green_lateness_ratio":null,"green_lateness_reason":"no confirmed Stage3-Green trigger in this case set","four_b_local_peak_proximity":0.82,"four_b_full_window_peak_proximity":0.82,"four_b_timing_verdict":"non_price_local_4B_watch_supported","four_b_evidence_type":["margin_or_backlog_slowdown","execution_risk","relative_strength_fade"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"counterexample_backlog_proxy_without_margin_bridge","positive_or_counterexample":"counterexample","current_profile_verdict":"current_profile_false_positive_if_machinery_recovery_proxy_replaces_order_margin_bridge","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C01_ORDER_BACKLOG_MARGIN_BRIDGE|042670|Stage4B|2024-05-02","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"source_proxy_only":true,"evidence_url_pending":true,"promotion_usable":false,"promotion_block_reason":"source_proxy_only_evidence_url_repair_required","price_path_anchor_urls":["https://github.com/Songdaiki/stock-web/blob/main/atlas/ohlcv_tradable_by_symbol_year/042/042670/2024.csv?plain=1"],"symbol_profile_url":"https://github.com/Songdaiki/stock-web/blob/main/atlas/symbol_profiles/042/042670.json?plain=1"}
```

### 25.4 score_simulation rows
```jsonl
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C01_042660_2024-11-01_Stage2_Actionable_SHIPBUILDER_TURNAROUND_BACKLOG_MARGIN_BRIDGE","trigger_id":"R1L116-C01-001","symbol":"042660","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C01_ORDER_BACKLOG_MARGIN_BRIDGE","raw_component_scores_before":{"contract_score":16,"backlog_visibility_score":18,"margin_bridge_score":15,"revision_score":12,"relative_strength_score":10,"customer_quality_score":11,"policy_or_regulatory_score":2,"valuation_repricing_score":3,"execution_risk_score":-4,"legal_or_contract_risk_score":-2,"dilution_cb_risk_score":0,"accounting_trust_risk_score":-2},"weighted_score_before":79,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"contract_score":16,"backlog_visibility_score":18,"margin_bridge_score":17,"revision_score":13,"relative_strength_score":10,"customer_quality_score":11,"policy_or_regulatory_score":2,"valuation_repricing_score":3,"execution_risk_score":-3,"legal_or_contract_risk_score":-2,"dilution_cb_risk_score":0,"accounting_trust_risk_score":-2},"weighted_score_after":83,"stage_label_after":"Stage3-Yellow guarded","changed_components":["margin_bridge_score","revision_score","execution_risk_score"],"component_delta_explanation":"Keep Actionable/Yellow only when backlog is tied to entity-level OPM, working-capital and revision bridge.","MFE_90D_pct":225.37,"MAE_90D_pct":-2.61,"score_return_alignment_label":"positive_alignment","current_profile_verdict":"current_profile_correct_when_backlog_is_entity_level_and_margin_bridge_is_visible"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C01_075580_2025-05-02_Stage2_Actionable_SHIPBUILDING_SUPPLIER_BLOCK_LPG_TANK_BACKLOG_MARGIN_BRIDGE","trigger_id":"R1L116-C01-002","symbol":"075580","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C01_ORDER_BACKLOG_MARGIN_BRIDGE","raw_component_scores_before":{"contract_score":14,"backlog_visibility_score":17,"margin_bridge_score":14,"revision_score":10,"relative_strength_score":9,"customer_quality_score":10,"policy_or_regulatory_score":1,"valuation_repricing_score":2,"execution_risk_score":-4,"legal_or_contract_risk_score":-1,"dilution_cb_risk_score":0,"accounting_trust_risk_score":-1},"weighted_score_before":76,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"contract_score":14,"backlog_visibility_score":18,"margin_bridge_score":16,"revision_score":11,"relative_strength_score":9,"customer_quality_score":10,"policy_or_regulatory_score":1,"valuation_repricing_score":2,"execution_risk_score":-4,"legal_or_contract_risk_score":-1,"dilution_cb_risk_score":0,"accounting_trust_risk_score":-1},"weighted_score_after":80,"stage_label_after":"Stage3-Yellow guarded","changed_components":["backlog_visibility_score","margin_bridge_score","revision_score"],"component_delta_explanation":"Allow supplier Actionable when disclosed order/revenue conversion joins yard backlog cycle; do not require parent-yard status only.","MFE_90D_pct":209.6,"MAE_90D_pct":-2.94,"score_return_alignment_label":"positive_alignment","current_profile_verdict":"current_profile_missed_structural_supplier_bridge_if_supplier_order_conversion_visible"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C01_077970_2024-05-02_Stage2_Actionable_MARINE_ENGINE_DEFENSE_SHIP_ENGINE_BACKLOG_REVENUE_BRIDGE","trigger_id":"R1L116-C01-003","symbol":"077970","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C01_ORDER_BACKLOG_MARGIN_BRIDGE","raw_component_scores_before":{"contract_score":15,"backlog_visibility_score":16,"margin_bridge_score":13,"revision_score":9,"relative_strength_score":9,"customer_quality_score":10,"policy_or_regulatory_score":2,"valuation_repricing_score":2,"execution_risk_score":-4,"legal_or_contract_risk_score":-1,"dilution_cb_risk_score":0,"accounting_trust_risk_score":-1},"weighted_score_before":75,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"contract_score":15,"backlog_visibility_score":16,"margin_bridge_score":15,"revision_score":10,"relative_strength_score":9,"customer_quality_score":11,"policy_or_regulatory_score":2,"valuation_repricing_score":2,"execution_risk_score":-4,"legal_or_contract_risk_score":-1,"dilution_cb_risk_score":0,"accounting_trust_risk_score":-1},"weighted_score_after":79,"stage_label_after":"Stage2-Actionable high conviction","changed_components":["margin_bridge_score","revision_score","customer_quality_score"],"component_delta_explanation":"Engine supplier can be Actionable, but Green should wait for margin/revision proof.","MFE_90D_pct":81.55,"MAE_90D_pct":-4.17,"score_return_alignment_label":"positive_alignment","current_profile_verdict":"current_profile_correct_for_engine_supplier_bridge_but_green_requires_margin_revision"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C01_097230_2024-11-01_Stage3_Yellow_SMALL_SHIPBUILDER_ORDERBOOK_OPERATING_LEVERAGE_RERATING","trigger_id":"R1L116-C01-004","symbol":"097230","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C01_ORDER_BACKLOG_MARGIN_BRIDGE","raw_component_scores_before":{"contract_score":15,"backlog_visibility_score":18,"margin_bridge_score":15,"revision_score":13,"relative_strength_score":14,"customer_quality_score":8,"policy_or_regulatory_score":1,"valuation_repricing_score":2,"execution_risk_score":-3,"legal_or_contract_risk_score":-1,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":82,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":15,"backlog_visibility_score":18,"margin_bridge_score":15,"revision_score":13,"relative_strength_score":14,"customer_quality_score":8,"policy_or_regulatory_score":1,"valuation_repricing_score":2,"execution_risk_score":-2,"legal_or_contract_risk_score":-1,"dilution_cb_risk_score":0,"accounting_trust_risk_score":1},"weighted_score_after":84,"stage_label_after":"Stage3-Yellow guarded","changed_components":["accounting_trust_risk_score","execution_risk_score"],"component_delta_explanation":"Use as positive, but tag as high-MFE outlier so it does not loosen C01 Green globally.","MFE_90D_pct":348.98,"MAE_90D_pct":-0.91,"score_return_alignment_label":"positive_alignment","current_profile_verdict":"current_profile_correct_but_position_size_high_MFE_outlier_guard_needed"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C01_112610_2024-09-02_Stage4B_OFFSHORE_WIND_ORDER_BACKLOG_MARGIN_GAP_4B_WATCH","trigger_id":"R1L116-C01-005","symbol":"112610","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C01_ORDER_BACKLOG_MARGIN_BRIDGE","raw_component_scores_before":{"contract_score":14,"backlog_visibility_score":15,"margin_bridge_score":7,"revision_score":5,"relative_strength_score":8,"customer_quality_score":8,"policy_or_regulatory_score":4,"valuation_repricing_score":2,"execution_risk_score":-10,"legal_or_contract_risk_score":-2,"dilution_cb_risk_score":0,"accounting_trust_risk_score":-3},"weighted_score_before":74,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"contract_score":14,"backlog_visibility_score":15,"margin_bridge_score":3,"revision_score":3,"relative_strength_score":8,"customer_quality_score":8,"policy_or_regulatory_score":4,"valuation_repricing_score":2,"execution_risk_score":-13,"legal_or_contract_risk_score":-2,"dilution_cb_risk_score":0,"accounting_trust_risk_score":-4},"weighted_score_after":61,"stage_label_after":"Stage4B local watch","changed_components":["margin_bridge_score","revision_score","execution_risk_score","accounting_trust_risk_score"],"component_delta_explanation":"Block Yellow; require explicit margin and cash conversion bridge before positive classification.","MFE_90D_pct":16.3,"MAE_90D_pct":-41.14,"score_return_alignment_label":"guardrail_alignment","current_profile_verdict":"current_profile_false_positive_if_backlog_without_margin_and_working_capital_bridge_is_promoted"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C01_241560_2024-05-02_Stage4B_MACHINERY_BACKLOG_CYCLE_SLOWDOWN_HIGH_MAE_GUARD","trigger_id":"R1L116-C01-006","symbol":"241560","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C01_ORDER_BACKLOG_MARGIN_BRIDGE","raw_component_scores_before":{"contract_score":12,"backlog_visibility_score":14,"margin_bridge_score":8,"revision_score":5,"relative_strength_score":9,"customer_quality_score":9,"policy_or_regulatory_score":1,"valuation_repricing_score":2,"execution_risk_score":-8,"legal_or_contract_risk_score":-1,"dilution_cb_risk_score":0,"accounting_trust_risk_score":-1},"weighted_score_before":73,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"contract_score":12,"backlog_visibility_score":12,"margin_bridge_score":5,"revision_score":3,"relative_strength_score":8,"customer_quality_score":9,"policy_or_regulatory_score":1,"valuation_repricing_score":2,"execution_risk_score":-11,"legal_or_contract_risk_score":-1,"dilution_cb_risk_score":0,"accounting_trust_risk_score":-1},"weighted_score_after":62,"stage_label_after":"Stage2-Watch / Stage4B local watch","changed_components":["backlog_visibility_score","margin_bridge_score","revision_score","execution_risk_score","relative_strength_score"],"component_delta_explanation":"Require fresh order intake and margin/revision bridge; activate high-MAE guard when backlog is stale.","MFE_90D_pct":19.81,"MAE_90D_pct":-35.87,"score_return_alignment_label":"guardrail_alignment","current_profile_verdict":"current_profile_false_positive_if_legacy_backlog_ignores_cycle_slowdown"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C01_042670_2024-05-02_Stage4B_CONSTRUCTION_MACHINERY_ORDER_BACKLOG_MARGIN_GAP_4B_WATCH","trigger_id":"R1L116-C01-007","symbol":"042670","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C01_ORDER_BACKLOG_MARGIN_BRIDGE","raw_component_scores_before":{"contract_score":12,"backlog_visibility_score":13,"margin_bridge_score":7,"revision_score":5,"relative_strength_score":7,"customer_quality_score":8,"policy_or_regulatory_score":1,"valuation_repricing_score":2,"execution_risk_score":-8,"legal_or_contract_risk_score":-1,"dilution_cb_risk_score":0,"accounting_trust_risk_score":-2},"weighted_score_before":72,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"contract_score":12,"backlog_visibility_score":13,"margin_bridge_score":4,"revision_score":3,"relative_strength_score":7,"customer_quality_score":8,"policy_or_regulatory_score":1,"valuation_repricing_score":2,"execution_risk_score":-12,"legal_or_contract_risk_score":-1,"dilution_cb_risk_score":0,"accounting_trust_risk_score":-3},"weighted_score_after":60,"stage_label_after":"Stage2-Watch / Stage4B local watch","changed_components":["margin_bridge_score","revision_score","execution_risk_score","accounting_trust_risk_score"],"component_delta_explanation":"Guard construction-machinery proxy with explicit order cycle, utilization and margin bridge.","MFE_90D_pct":10.76,"MAE_90D_pct":-21.89,"score_return_alignment_label":"guardrail_alignment","current_profile_verdict":"current_profile_false_positive_if_machinery_recovery_proxy_replaces_order_margin_bridge"}
```

### 25.5 profile comparison rows
```jsonl
{"row_type":"profile_comparison","profile_id":"P0_e2r_2_1_stock_web_calibrated_proxy","profile_scope":"current proxy","profile_hypothesis":"existing calibrated profile without C01 entity-level bridge specialization","eligible_trigger_count":7,"selected_entry_trigger_per_case":7,"avg_MFE_90D_pct":130.34,"avg_MAE_90D_pct":-15.65,"avg_MFE_180D_pct":139.29,"avg_MAE_180D_pct":-17.59,"false_positive_rate":0.43,"missed_structural_count":1,"late_green_count":0,"avg_green_lateness_ratio":null,"avg_four_b_local_peak_proximity":0.82,"avg_four_b_full_window_peak_proximity":0.82,"score_return_alignment_verdict":"mixed: captures winners but still over-promotes backlog proxies"}
{"row_type":"profile_comparison","profile_id":"P0b_e2r_2_0_baseline_reference","profile_scope":"rollback reference","profile_hypothesis":"baseline without stock-web calibrated guardrails","eligible_trigger_count":7,"selected_entry_trigger_per_case":7,"avg_MFE_90D_pct":130.34,"avg_MAE_90D_pct":-15.65,"avg_MFE_180D_pct":139.29,"avg_MAE_180D_pct":-17.59,"false_positive_rate":0.57,"missed_structural_count":0,"late_green_count":1,"avg_green_lateness_ratio":null,"avg_four_b_local_peak_proximity":null,"avg_four_b_full_window_peak_proximity":null,"score_return_alignment_verdict":"too permissive for backlog proxies"}
{"row_type":"profile_comparison","profile_id":"P1_L1_sector_specific_candidate_profile","profile_scope":"sector_specific","profile_hypothesis":"L1 backlog research requires entity-level backlog to margin/FCF bridge","eligible_trigger_count":4,"selected_entry_trigger_per_case":4,"avg_MFE_90D_pct":216.38,"avg_MAE_90D_pct":-2.66,"avg_MFE_180D_pct":232.04,"avg_MAE_180D_pct":-2.66,"false_positive_rate":0.0,"missed_structural_count":1,"late_green_count":0,"avg_green_lateness_ratio":null,"avg_four_b_local_peak_proximity":null,"avg_four_b_full_window_peak_proximity":null,"score_return_alignment_verdict":"best positive alignment"}
{"row_type":"profile_comparison","profile_id":"P2_C01_canonical_guard_profile","profile_scope":"canonical_archetype_specific","profile_hypothesis":"block group-level backlog, supplier beta and machinery cycle proxies until margin bridge appears","eligible_trigger_count":3,"selected_entry_trigger_per_case":3,"avg_MFE_90D_pct":15.62,"avg_MAE_90D_pct":-32.97,"avg_MFE_180D_pct":15.62,"avg_MAE_180D_pct":-37.5,"false_positive_rate":0.0,"missed_structural_count":0,"late_green_count":0,"avg_green_lateness_ratio":null,"avg_four_b_local_peak_proximity":0.82,"avg_four_b_full_window_peak_proximity":0.82,"score_return_alignment_verdict":"prevents high-MAE entries"}
{"row_type":"profile_comparison","profile_id":"P3_C01_local_4B_overlay_profile","profile_scope":"canonical_archetype_specific","profile_hypothesis":"when backlog proxy remains unconverted and MAE guard is hit, route to local 4B watch not full thesis-break 4C","eligible_trigger_count":3,"selected_entry_trigger_per_case":3,"avg_MFE_90D_pct":15.62,"avg_MAE_90D_pct":-32.97,"avg_MFE_180D_pct":15.62,"avg_MAE_180D_pct":-37.5,"false_positive_rate":0.0,"missed_structural_count":0,"late_green_count":0,"avg_green_lateness_ratio":null,"avg_four_b_local_peak_proximity":0.82,"avg_four_b_full_window_peak_proximity":0.82,"score_return_alignment_verdict":"useful as watch overlay, not production sell signal"}
```

### 25.6 stage_transition rows
```jsonl
{"row_type":"stage_transition","trigger_id":"R1L116-C01-001","symbol":"042660","canonical_archetype_id":"C01_ORDER_BACKLOG_MARGIN_BRIDGE","trigger_type":"Stage2-Actionable","entry_date":"2024-11-01","transition_label":"Stage2_or_Yellow_supported_with_entity_level_bridge","mfe_mae_180_spread_pct":276.87,"profile_residual":"current_profile_correct_when_backlog_is_entity_level_and_margin_bridge_is_visible"}
{"row_type":"stage_transition","trigger_id":"R1L116-C01-002","symbol":"075580","canonical_archetype_id":"C01_ORDER_BACKLOG_MARGIN_BRIDGE","trigger_type":"Stage2-Actionable","entry_date":"2025-05-02","transition_label":"Stage2_or_Yellow_supported_with_entity_level_bridge","mfe_mae_180_spread_pct":206.66,"profile_residual":"current_profile_missed_structural_supplier_bridge_if_supplier_order_conversion_visible"}
{"row_type":"stage_transition","trigger_id":"R1L116-C01-003","symbol":"077970","canonical_archetype_id":"C01_ORDER_BACKLOG_MARGIN_BRIDGE","trigger_type":"Stage2-Actionable","entry_date":"2024-05-02","transition_label":"Stage2_or_Yellow_supported_with_entity_level_bridge","mfe_mae_180_spread_pct":85.93,"profile_residual":"current_profile_correct_for_engine_supplier_bridge_but_green_requires_margin_revision"}
{"row_type":"stage_transition","trigger_id":"R1L116-C01-004","symbol":"097230","canonical_archetype_id":"C01_ORDER_BACKLOG_MARGIN_BRIDGE","trigger_type":"Stage3-Yellow","entry_date":"2024-11-01","transition_label":"Stage2_or_Yellow_supported_with_entity_level_bridge","mfe_mae_180_spread_pct":348.07,"profile_residual":"current_profile_correct_but_position_size_high_MFE_outlier_guard_needed"}
{"row_type":"stage_transition","trigger_id":"R1L116-C01-005","symbol":"112610","canonical_archetype_id":"C01_ORDER_BACKLOG_MARGIN_BRIDGE","trigger_type":"Stage4B","entry_date":"2024-09-02","transition_label":"Stage2_false_positive_or_4B_watch_supported","mfe_mae_180_spread_pct":-36.15,"profile_residual":"current_profile_false_positive_if_backlog_without_margin_and_working_capital_bridge_is_promoted"}
{"row_type":"stage_transition","trigger_id":"R1L116-C01-006","symbol":"241560","canonical_archetype_id":"C01_ORDER_BACKLOG_MARGIN_BRIDGE","trigger_type":"Stage4B","entry_date":"2024-05-02","transition_label":"Stage2_false_positive_or_4B_watch_supported","mfe_mae_180_spread_pct":-16.06,"profile_residual":"current_profile_false_positive_if_legacy_backlog_ignores_cycle_slowdown"}
{"row_type":"stage_transition","trigger_id":"R1L116-C01-007","symbol":"042670","canonical_archetype_id":"C01_ORDER_BACKLOG_MARGIN_BRIDGE","trigger_type":"Stage4B","entry_date":"2024-05-02","transition_label":"Stage2_false_positive_or_4B_watch_supported","mfe_mae_180_spread_pct":-13.42,"profile_residual":"current_profile_false_positive_if_machinery_recovery_proxy_replaces_order_margin_bridge"}
```

### 25.7 residual_contribution row
```jsonl
{"row_type":"residual_contribution","round":"R1","loop":116,"large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C01_ORDER_BACKLOG_MARGIN_BRIDGE","new_independent_case_count":7,"reused_case_count":0,"reused_case_ids":[],"new_symbol_count":7,"new_canonical_archetype_count":0,"new_fine_archetype_count":1,"new_trigger_family_count":7,"tested_existing_calibrated_axes":["stage2_required_bridge","local_4b_watch_guard","price_only_blowoff_blocks_positive_stage","full_4b_requires_non_price_evidence"],"residual_error_types_found":["proxy_backlog_false_positive","machinery_cycle_high_MAE","offshore_wind_orderbook_margin_gap","missed_supplier_bridge_positive"],"new_axis_proposed":"C01_verified_backlog_margin_fcf_bridge_required_before_Yellow_or_Green_plus_proxy_backlog_to_local_4B_watch","existing_axis_strengthened":["stage2_required_bridge","local_4b_watch_guard","full_4b_requires_non_price_evidence"],"existing_axis_weakened":[],"existing_axis_kept":["stage3_green_total_min","stage3_green_revision_min"],"sector_specific_rule_candidate":true,"canonical_archetype_rule_candidate":true,"no_new_signal_reason":null,"loop_contribution_label":"canonical_archetype_rule_candidate","do_not_propose_new_weight_delta":false}
```


## Batch Ingest Self-Audit

```text
expected_v12_result_file: true
filename_pattern_pass: true
metadata_filename_consistency: pass
jsonl_trigger_row_count: 7
calibration_usable_trigger_count: 7
representative_trigger_count: 7
new_weight_evidence_candidate_count: 7
guardrail_candidate_count: 3
narrative_only_or_rejected_count: 0
rows_missing_required_mfe_mae: 0
rows_missing_entry_price_or_date: 0
rows_with_noncanonical_trigger_type: 0
rows_with_compact_mfe_mae_alias_only: 0
ready_for_batch_ingest: true
```

## 26. Deferred Coding Agent Handoff Prompt

### Purpose
You are now in the repository implementation phase. The attached Markdown files are v12 post-calibrated residual research outputs produced using the Songdaiki/stock-web OHLC atlas. These MDs are not live candidate research. They are historical calibration research designed to extend the already-applied e2r_2_1_stock_web_calibrated profile. Do not blindly apply every shadow row. Ingest the machine-readable rows and update the sector/canonical-archetype calibration ledger.

### Price source context
- Primary historical price source used by the research MD: Songdaiki/stock-web.
- Price basis: tradable_raw.
- Price adjustment status: raw_unadjusted_marcap.
- Price shard pattern: atlas/ohlcv_tradable_by_symbol_year/<prefix>/<symbol>/<year>.csv.
- Symbol profile pattern: atlas/symbol_profiles/<prefix>/<symbol>.json.

### Rules
- Use only `calibration_usable=true` rows for quantitative calibration.
- Do not promote source-proxy-only rows until evidence URL repair is complete.
- Do not count reused cases as new independent evidence unless `independent_evidence_weight > 0`.
- Do not apply global deltas from this single C01 loop.
- Preserve production scoring unless the user explicitly requests a promotion batch.
- Treat Stage4B rows as local watch overlays, not hard 4C exits.

### Expected repository tasks
1. Parse case / trigger / score_simulation / shadow_weight / residual_contribution rows.
2. Validate stock-web price source fields and required 30/90/180D MFE/MAE keys.
3. Validate R1/L1/C01 consistency.
4. Deduplicate by canonical_archetype_id + symbol + trigger_type + entry_date.
5. Update sector/canonical shadow ledger only.
6. Report rows blocked by source_proxy_only evidence.

## 27. Next Round State

```text
completed_round = R1
completed_loop = 116
selection_basis = docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket = Priority 0
next_recommended_archetypes = C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK, C02_POWER_GRID_DATACENTER_CAPEX, C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF, C14_EV_DEMAND_SLOWDOWN_4B_4C, C06_HBM_MEMORY_CUSTOMER_CAPACITY
round_schedule_status = coverage_index_selected
round_sector_consistency = pass
```

## 28. Source Notes

- Main execution prompt: `docs/core/e2r_v12_prompt_round_scheduler_corrected.txt`.
- No-repeat ledger: `docs/core/V12_Research_No_Repeat_Index.md`.
- Price atlas manifest: `Songdaiki/stock-web/atlas/manifest.json`.
- CSV shards used: stock-web `atlas/ohlcv_tradable_by_symbol_year`.
- Evidence labels are source-proxy-only in this artifact; URL repair is intentionally left for a later batch.
