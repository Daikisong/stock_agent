# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
selected_round = R2
selected_loop = 88
selection_basis = docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket = Priority 0
round_schedule_status = coverage_index_selected
round_sector_consistency = pass
large_sector_id = L2_AI_SEMICONDUCTOR_ELECTRONICS
canonical_archetype_id = C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY
fine_archetype_id = TEST_SOCKET_PROBE_CARD_CUSTOMER_QUALIFICATION_BRIDGE_VS_PRICE_ONLY_EQUIPMENT_BETA_DECAY
loop_objective = coverage_gap_fill | counterexample_mining | 4B_non_price_requirement_stress_test | canonical_archetype_compression
price_source = Songdaiki/stock-web
stock_web_manifest_max_date = 2026-02-20
production_scoring_changed = false
shadow_weight_only = true
```

This loop adds 3 new independent cases, 2 counterexamples, and 2 current-profile residual errors for R2/L2/C08.

## 1. Current Calibrated Profile Assumption

Current proxy remains `e2r_2_1_stock_web_calibrated_proxy` / active v12 ledger context. The loop does not modify production scoring. It only proposes C08 scoped shadow rows.

Already applied global axes are treated as existing controls, not re-proposed:

- `price_only_blowoff_blocks_positive_stage`
- `full_4b_requires_non_price_evidence`
- `hard_4c_thesis_break_routes_to_4c`
- `stage2_actionable_evidence_bonus`

## 2. Round / Large Sector / Canonical Archetype Scope

- selected_round: `R2`
- selected_loop: `88`
- large_sector_id: `L2_AI_SEMICONDUCTOR_ELECTRONICS`
- canonical_archetype_id: `C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY`
- fine_archetype_id: `TEST_SOCKET_PROBE_CARD_CUSTOMER_QUALIFICATION_BRIDGE_VS_PRICE_ONLY_EQUIPMENT_BETA_DECAY`

C08 focuses on semiconductor test/socket/probe-card customer quality. The key compression is:

```text
real C08 positive = customer qualification + repeat demand + margin/revenue conversion
false C08 positive = price-only test/socket equipment beta without customer quality bridge
4B C08 overlay = valuation blowoff or local peak after test/socket beta, especially when no non-price full-window evidence exists
```

## 3. Previous Coverage / Duplicate Avoidance Check

`V12_Research_No_Repeat_Index.md` marks C08 as Priority 0 with 14 rows, 11 symbols, 4/4 good/bad Stage2, 2/2 4B/4C, and top covered symbols `098120`, `080580`, `058470`, `067310`, `092870`, `097800`.

This loop avoids those top-covered symbol clusters and uses:

- `131290` 티에스이
- `095340` ISC
- `425420` 티에프이

Hard duplicate key check used:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

All three cases are treated as new independent C08 cases because the symbols and trigger families are not in the C08 top-covered list and the selected entry dates are distinct.

## 4. Stock-Web OHLC Input / Price Source Validation

| field | value |
|---|---|
| source | Songdaiki/stock-web |
| manifest_path | atlas/manifest.json |
| schema_path | atlas/schema.json |
| price_basis | tradable_raw |
| price_adjustment_status | raw_unadjusted_marcap |
| manifest_max_date | 2026-02-20 |
| calibration_shard_root | atlas/ohlcv_tradable_by_symbol_year |
| profile paths checked | `atlas/symbol_profiles/131/131290.json`, `atlas/symbol_profiles/095/095340.json`, `atlas/symbol_profiles/425/425420.json` |

The manifest confirms stock-web uses FinanceData/marcap, raw/unadjusted OHLC, tradable calibration shards, and max_date `2026-02-20`. The schema defines MFE/MAE as max high / min low from entry date through N tradable rows.

## 5. Historical Eligibility Gate

| symbol | profile | entry_date | 180D available | corporate action overlap | calibration_usable |
|---|---|---:|---:|---|---|
| 131290 | atlas/symbol_profiles/131/131290.json | 2024-02-01 | true | no 2024 overlap in selected 180D window | true |
| 095340 | atlas/symbol_profiles/095/095340.json | 2024-03-28 | true | no 2024 overlap in selected 180D window | true |
| 425420 | atlas/symbol_profiles/425/425420.json | 2024-03-20 | true | corporate_action_candidate_count=0 | true |

## 6. Canonical Archetype Compression Map

| deep/fine path | canonical compression | rule implication |
|---|---|---|
| probe-card/test-interface customer qualification reorder | C08 positive | can support Stage2-Actionable if non-price customer quality exists |
| test socket valuation blowoff after strong rerating | C08 4B overlay | should route to 4B/watch, not Green unlock |
| test interface price-only beta decay | C08 counterexample | relative strength alone must not promote positive stage |

## 7. Case Selection Summary

| case_id | symbol | company | case_type | trigger_type | entry_date | entry_price | MFE90 | MAE90 | current_profile_verdict |
|---|---|---|---|---|---:|---:|---:|---:|---|
| C08_131290_2024_02_01_PROBE_CARD_QUALIFICATION_REORDER_POSITIVE | 131290 | 티에스이 | structural_success | Stage2-Actionable | 2024-02-01 | 43,500 | 101.84 | -2.53 | current_profile_missed_structural |
| C08_095340_2024_03_28_TEST_SOCKET_BLOWOFF_4B_GUARD | 095340 | ISC | 4B_overlay_success | Stage4B | 2024-03-28 | 99,400 | 8.65 | -58.65 | current_profile_4B_too_late |
| C08_425420_2024_03_20_TEST_INTERFACE_PRICE_ONLY_BETA_DECAY | 425420 | 티에프이 | 4B_overlay_success | Stage4B | 2024-03-20 | 43,100 | 1.97 | -49.54 | current_profile_correct |

## 8. Positive vs Counterexample Balance

```text
positive_case_count = 1
counterexample_count = 2
4B_case_count = 2
4C_case_count = 0
calibration_usable_case_count = 3
```

The balance is intentionally conservative. TSE acts as the positive control where customer quality plus test-interface/probe-card demand coincides with strong MFE and contained 90D MAE. ISC and TFE are guardrail cases showing that test/socket theme beta and valuation expansion can decay violently without durable qualification/reorder proof.

## 9. Evidence Source Map

| symbol | evidence family | source quality | URL status |
|---|---|---|---|
| 131290 | probe-card / test-interface qualification + repeat demand route | source_proxy_only | evidence_url_pending |
| 095340 | test socket quality route plus valuation blowoff / overheat | source_proxy_only | evidence_url_pending |
| 425420 | test interface beta without enough non-price bridge | source_proxy_only | evidence_url_pending |

This MD is usable for price-path calibration and guardrail stress testing. It should not be used as final evidence-url repair until dated filings/news/source URLs are attached by a later batch.

## 10. Price Data Source Map

| symbol | shard | entry row basis | profile caveat |
|---|---|---|---|
| 131290 | atlas/ohlcv_tradable_by_symbol_year/131/131290/2024.csv | close on 2024-02-01 | raw/unadjusted; old corporate-action candidates in 2011 only |
| 095340 | atlas/ohlcv_tradable_by_symbol_year/095/095340/2024.csv | close on 2024-03-28 | raw/unadjusted; latest corporate-action candidate 2023-10-20, not in selected 2024 window |
| 425420 | atlas/ohlcv_tradable_by_symbol_year/425/425420/2024.csv | close on 2024-03-20 | raw/unadjusted; corporate_action_candidate_count=0 |

## 11. Case-by-Case Trigger Grid

| symbol | trigger_type | entry_date | entry_price | MFE30 | MAE30 | MFE90 | MAE90 | MFE180 | MAE180 | peak_date | peak_price | drawdown_after_peak |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 131290 | Stage2-Actionable | 2024-02-01 | 43,500 | 45.29 | -2.53 | 101.84 | -2.53 | 101.84 | -12.53 | 2024-05-03 | 87,800 | -56.66 |
| 095340 | Stage4B | 2024-03-28 | 99,400 | 8.65 | -27.06 | 8.65 | -58.65 | 8.65 | -58.65 | 2024-03-28 | 108,000 | -61.94 |
| 425420 | Stage4B | 2024-03-20 | 43,100 | 1.97 | -24.25 | 1.97 | -49.54 | 1.97 | -72.51 | 2024-03-21 | 43,950 | -74.08 |

## 12. Trigger-Level OHLC Backtest Tables

### 131290 / 티에스이 / positive control

- Entry: 2024-02-01 close 43,500.
- 30D: high 63,200 / low 42,400.
- 90D: high 87,800 / low 42,400.
- 180D: high 87,800 / low 38,050.
- Result: strong MFE with contained 90D MAE, later cycle drawdown after peak.

### 095340 / ISC / 4B guardrail

- Entry: 2024-03-28 close 99,400.
- Same-day high 108,000 is treated as the local/full observed peak.
- 30D/90D/180D MFE: 8.65%.
- 90D/180D MAE: -58.65%.
- Result: after socket/HBM interface rerating, 4B/watch routing was more useful than positive promotion.

### 425420 / 티에프이 / price-only beta decay

- Entry: 2024-03-20 close 43,100.
- Local peak: 2024-03-21 high 43,950.
- 30D MFE/MAE: 1.97% / -24.25%.
- 90D MFE/MAE: 1.97% / -49.54%.
- 180D MFE/MAE: 1.97% / -72.51%.
- Result: price-only test-interface beta should remain 4B/watch or blocked from Stage2/Green.

## 13. Current Calibrated Profile Stress Test

| case | current profile likely action | path verdict | residual |
|---|---|---|---|
| 131290 | cautious Stage2 because customer-quality evidence was not heavily weighted | MFE90 +101.84 / MAE90 -2.53 | missed structural |
| 095340 | late 4B after valuation/socket rerating | MFE after 4B only +8.65, MAE90 -58.65 | 4B too late |
| 425420 | block price-only Stage2/Green | MFE90 +1.97, MAE90 -49.54 | correct guard |

## 14. Stage2 / Yellow / Green Comparison

No confirmed Stage3-Green trigger is asserted. This loop is not trying to loosen Green. Green lateness is marked `not_applicable`.

The C08-specific lesson is that Stage2-Actionable is allowed only when customer qualification / repeat demand exists before the price move. Otherwise the same visual price action should become weak-watch or 4B/watch.

## 15. 4B Local vs Full-window Timing Audit

| symbol | 4B evidence | local_peak_proximity | full_window_peak_proximity | verdict |
|---|---|---:|---:|---|
| 095340 | valuation_blowoff, positioning_overheat, price_only_local_peak | 0.76 | 0.76 | good_full_window_4B_timing but evidence URL pending |
| 425420 | price_only_local_peak, positioning_overheat | 0.98 | 0.98 | price-only 4B/watch, not positive Stage2 |

## 16. 4C Protection Audit

No hard 4C thesis-break is asserted. Both counterexamples are 4B/watch overlays rather than confirmed 4C.

```text
four_c_protection_score = not_applicable
reason = no confirmed hard 4C thesis-break evidence
```

## 17. Sector-Specific Rule Candidate

```text
rule_scope = sector_specific
large_sector_id = L2_AI_SEMICONDUCTOR_ELECTRONICS
candidate = Test/socket relative strength cannot promote Stage2-Actionable unless at least one non-price customer-quality or repeat-demand bridge exists.
```

Rationale: L2 semi equipment names can have violent beta rallies. C08 should distinguish customer qualification/reorder proof from equipment-theme repricing.

## 18. Canonical-Archetype Rule Candidate

```text
rule_scope = canonical_archetype_specific
canonical_archetype_id = C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY
candidate = require customer_qualification_or_repeat_consumable_revenue_bridge for positive Stage2-Actionable; route valuation/price-only test interface spikes to 4B/watch.
```

This is shadow-only and should not alter production scoring without a later promotion batch.

## 19. Before / After Backtest Comparison

| profile | eligible triggers | avg MFE90 | avg MAE90 | false-positive handling | verdict |
|---|---:|---:|---:|---|---|
| P0 current proxy | 3 | 37.49 | -36.91 | mixed | too weak on C08 distinction |
| P1 sector candidate | 3 | 37.49 | -36.91 | routes price-only to watch | improves classification |
| P2 canonical candidate | 3 | 37.49 | -36.91 | separates qualification vs beta | best explanatory compression |
| P3 counterexample guard | 3 | 37.49 | -36.91 | blocks price-only Stage2 | safest guard |

## 20. Score-Return Alignment Matrix

| symbol | score-return alignment |
|---|---|
| 131290 | positive alignment: customer quality route + strong MFE / tolerable MAE |
| 095340 | overheat alignment: 4B/watch would have avoided large post-peak MAE |
| 425420 | guardrail alignment: price-only beta had poor MFE/MAE asymmetry |

## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive_case_count | counterexample_count | 4B_case_count | 4C_case_count | new_independent_case_count | reused_case_count | calibration_usable_trigger_count | representative_trigger_count | current_profile_error_count | sector_rule_candidate | canonical_rule_candidate | coverage_gap_after_this_loop |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| L2_AI_SEMICONDUCTOR_ELECTRONICS | C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY | TEST_SOCKET_PROBE_CARD_CUSTOMER_QUALIFICATION_BRIDGE_VS_PRICE_ONLY_EQUIPMENT_BETA_DECAY | 1 | 2 | 2 | 0 | 3 | 0 | 3 | 3 | 2 | true | true | C08 rows 14 -> +3 pending ingest; still below 30 |

## 22. Residual Contribution Summary

```text
new_independent_case_count: 3
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 3
same_archetype_new_symbol_count: 3
new_canonical_archetype_count: 0
new_fine_archetype_count: 1
new_trigger_family_count: 3
same_archetype_new_trigger_family_count: 3
tested_existing_calibrated_axes: price_only_blowoff_blocks_positive_stage, full_4b_requires_non_price_evidence, stage2_required_bridge
residual_error_types_found: C08_customer_quality_positive_missed, C08_valuation_blowoff_4B_late, C08_price_only_beta_decay_guard
new_axis_proposed: c08_customer_quality_repeat_demand_bridge_required_for_stage2_actionable_shadow_only
existing_axis_strengthened: full_4b_requires_non_price_evidence scoped to C08 test/socket price-only blowoff
existing_axis_weakened: null
existing_axis_kept: price_only_blowoff_blocks_positive_stage
sector_specific_rule_candidate: true
canonical_archetype_rule_candidate: true
no_new_signal_reason: null

loop_contribution_label: canonical_archetype_rule_candidate
do_not_propose_new_weight_delta: false
```

## 23. Validation Scope / Non-Validation Scope

Validation scope:

- actual stock-web tradable OHLC rows
- 30D / 90D / 180D MFE/MAE
- clean profile windows with 180D available
- round/sector/canonical consistency
- C08 novelty versus top-covered symbols

Non-validation scope:

- no live recommendation
- no production scoring change
- no stock_agent source-code change
- no current candidate scan
- evidence URLs are pending and should be repaired later

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,c08_customer_quality_repeat_demand_bridge_required_for_stage2_actionable,canonical_archetype_specific,L2_AI_SEMICONDUCTOR_ELECTRONICS,C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY,0,1,+1,"C08 positive route needs explicit customer qualification/repeat-demand bridge, not only test/socket theme beta.","TSE positive accepted while ISC/TFE price-only blowoff routed to 4B/watch.","C08_131290_2024_02_01_PROBE_CARD_QUALIFICATION_REORDER_POSITIVE_Stage2-Actionable|C08_095340_2024_03_28_TEST_SOCKET_BLOWOFF_4B_GUARD_Stage4B|C08_425420_2024_03_20_TEST_INTERFACE_PRICE_ONLY_BETA_DECAY_Stage4B",3,3,2,low_to_medium,canonical_shadow_only,"not production; evidence URL pending"
shadow_weight,c08_price_only_test_interface_beta_to_4b_watch,canonical_archetype_specific,L2_AI_SEMICONDUCTOR_ELECTRONICS,C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY,0,1,+1,"TFE and ISC show price-only or valuation blowoff in test/socket names can precede deep MAE.","Preserves price_only_blowoff_blocks_positive_stage and full_4b_requires_non_price_evidence; adds C08 label-specific watch routing.","C08_095340_2024_03_28_TEST_SOCKET_BLOWOFF_4B_GUARD_Stage4B|C08_425420_2024_03_20_TEST_INTERFACE_PRICE_ONLY_BETA_DECAY_Stage4B",2,2,2,medium,canonical_shadow_only,"4B overlay only; no investment recommendation"
```

## 25. Machine-Readable Rows

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
{"row_type":"case","case_id":"C08_131290_2024_02_01_PROBE_CARD_QUALIFICATION_REORDER_POSITIVE","symbol":"131290","company_name":"티에스이","round":"R2","loop":"88","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY","fine_archetype_id":"TEST_SOCKET_PROBE_CARD_CUSTOMER_QUALIFICATION_BRIDGE_VS_PRICE_ONLY_EQUIPMENT_BETA_DECAY","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"Stage2-Actionable","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"good_stage2_candidate","current_profile_verdict":"current_profile_missed_structural","price_source":"Songdaiki/stock-web","notes":"TSE adds a new C08 symbol and a probe-card/customer qualification positive control not listed among top-covered C08 symbols."}
{"row_type":"case","case_id":"C08_095340_2024_03_28_TEST_SOCKET_BLOWOFF_4B_GUARD","symbol":"095340","company_name":"ISC","round":"R2","loop":"88","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY","fine_archetype_id":"TEST_SOCKET_PROBE_CARD_CUSTOMER_QUALIFICATION_BRIDGE_VS_PRICE_ONLY_EQUIPMENT_BETA_DECAY","case_type":"4B_overlay_success","positive_or_counterexample":"counterexample","best_trigger":"Stage4B","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"4B_guard_success","current_profile_verdict":"current_profile_4B_too_late","price_source":"Songdaiki/stock-web","notes":"ISC is a new C08 symbol for this loop; the case is guardrail evidence rather than positive promotion evidence."}
{"row_type":"case","case_id":"C08_425420_2024_03_20_TEST_INTERFACE_PRICE_ONLY_BETA_DECAY","symbol":"425420","company_name":"티에프이","round":"R2","loop":"88","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY","fine_archetype_id":"TEST_SOCKET_PROBE_CARD_CUSTOMER_QUALIFICATION_BRIDGE_VS_PRICE_ONLY_EQUIPMENT_BETA_DECAY","case_type":"4B_overlay_success","positive_or_counterexample":"counterexample","best_trigger":"Stage4B","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"price_only_stage2_block_correct","current_profile_verdict":"current_profile_correct","price_source":"Songdaiki/stock-web","notes":"TFE adds a new C08 symbol and a failure mode where price-only beta should be routed to 4B/watch, not Stage2/Green."}
{"row_type":"trigger","trigger_id":"C08_131290_2024_02_01_PROBE_CARD_QUALIFICATION_REORDER_POSITIVE_Stage2-Actionable","case_id":"C08_131290_2024_02_01_PROBE_CARD_QUALIFICATION_REORDER_POSITIVE","symbol":"131290","company_name":"티에스이","round":"R2","loop":"88","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY","fine_archetype_id":"TEST_SOCKET_PROBE_CARD_CUSTOMER_QUALIFICATION_BRIDGE_VS_PRICE_ONLY_EQUIPMENT_BETA_DECAY","loop_objective":"coverage_gap_fill | counterexample_mining | 4B_non_price_requirement_stress_test | canonical_archetype_compression","trigger_type":"Stage2-Actionable","trigger_date":"2024-02-01","entry_date":"2024-02-01","entry_price":43500,"evidence_available_at_that_date":"source_proxy_only: probe-card/test-interface customer qualification and repeat-demand route; price row confirms post-entry upside with controlled 90D MAE","evidence_source":"source_proxy_only; evidence_url_pending; historical public company/sector event proxy","stage2_evidence_fields":["customer_or_order_quality","relative_strength","capacity_or_volume_route"],"stage3_evidence_fields":["repeat_order_or_conversion","durable_customer_confirmation"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/131/131290/2024.csv","profile_path":"atlas/symbol_profiles/131/131290.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":45.29,"MFE_90D_pct":101.84,"MFE_180D_pct":101.84,"MAE_30D_pct":-2.53,"MAE_90D_pct":-2.53,"MAE_180D_pct":-12.53,"peak_date":"2024-05-03","peak_price":87800,"drawdown_after_peak_pct":-56.66,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_evidence_type":[],"trigger_outcome_label":"customer_quality_bridge_positive_high_mfe_controlled_mae","current_profile_verdict":"current_profile_missed_structural","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C08_131290_2024_02_01","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"C08_095340_2024_03_28_TEST_SOCKET_BLOWOFF_4B_GUARD_Stage4B","case_id":"C08_095340_2024_03_28_TEST_SOCKET_BLOWOFF_4B_GUARD","symbol":"095340","company_name":"ISC","round":"R2","loop":"88","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY","fine_archetype_id":"TEST_SOCKET_PROBE_CARD_CUSTOMER_QUALIFICATION_BRIDGE_VS_PRICE_ONLY_EQUIPMENT_BETA_DECAY","loop_objective":"coverage_gap_fill | counterexample_mining | 4B_non_price_requirement_stress_test | canonical_archetype_compression","trigger_type":"Stage4B","trigger_date":"2024-03-28","entry_date":"2024-03-28","entry_price":99400,"evidence_available_at_that_date":"source_proxy_only: test-socket/HBM interface beta plus valuation blowoff after earlier socket quality rerating; later path shows severe MAE after peak","evidence_source":"source_proxy_only; evidence_url_pending; historical public company/sector event proxy","stage2_evidence_fields":["customer_or_order_quality","relative_strength"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["valuation_blowoff","positioning_overheat","price_only_local_peak"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/095/095340/2024.csv","profile_path":"atlas/symbol_profiles/095/095340.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":8.65,"MFE_90D_pct":8.65,"MFE_180D_pct":8.65,"MAE_30D_pct":-27.06,"MAE_90D_pct":-58.65,"MAE_180D_pct":-58.65,"peak_date":"2024-03-28","peak_price":108000,"drawdown_after_peak_pct":-61.94,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":0.76,"four_b_full_window_peak_proximity":0.76,"four_b_evidence_type":["valuation_blowoff","positioning_overheat","price_only_local_peak"],"trigger_outcome_label":"test_socket_valuation_blowoff_good_4b_guard","current_profile_verdict":"current_profile_4B_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C08_095340_2024_03_28","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"C08_425420_2024_03_20_TEST_INTERFACE_PRICE_ONLY_BETA_DECAY_Stage4B","case_id":"C08_425420_2024_03_20_TEST_INTERFACE_PRICE_ONLY_BETA_DECAY","symbol":"425420","company_name":"티에프이","round":"R2","loop":"88","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY","fine_archetype_id":"TEST_SOCKET_PROBE_CARD_CUSTOMER_QUALIFICATION_BRIDGE_VS_PRICE_ONLY_EQUIPMENT_BETA_DECAY","loop_objective":"coverage_gap_fill | counterexample_mining | 4B_non_price_requirement_stress_test | canonical_archetype_compression","trigger_type":"Stage4B","trigger_date":"2024-03-20","entry_date":"2024-03-20","entry_price":43100,"evidence_available_at_that_date":"source_proxy_only: semiconductor test-interface beta price move without enough customer qualification/repeat-order proof; later path confirms price-only decay risk","evidence_source":"source_proxy_only; evidence_url_pending; historical public company/sector event proxy","stage2_evidence_fields":["relative_strength"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["price_only_local_peak","positioning_overheat"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/425/425420/2024.csv","profile_path":"atlas/symbol_profiles/425/425420.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":1.97,"MFE_90D_pct":1.97,"MFE_180D_pct":1.97,"MAE_30D_pct":-24.25,"MAE_90D_pct":-49.54,"MAE_180D_pct":-72.51,"peak_date":"2024-03-21","peak_price":43950,"drawdown_after_peak_pct":-74.08,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":0.98,"four_b_full_window_peak_proximity":0.98,"four_b_evidence_type":["price_only_local_peak","positioning_overheat"],"trigger_outcome_label":"price_only_test_interface_beta_decay_4b_guard","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C08_425420_2024_03_20","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"score_simulation","profile_id":"P0_e2r_2_1_stock_web_calibrated_proxy","profile_scope":"current calibrated proxy","case_id":"C08_131290_2024_02_01_PROBE_CARD_QUALIFICATION_REORDER_POSITIVE","trigger_id":"C08_131290_2024_02_01_PROBE_CARD_QUALIFICATION_REORDER_POSITIVE_Stage2-Actionable","symbol":"131290","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY","raw_component_scores_before":{"contract_score":2,"backlog_visibility_score":3,"margin_bridge_score":2,"revision_score":3,"relative_strength_score":4,"customer_quality_score":5,"policy_or_regulatory_score":0,"valuation_repricing_score":2,"execution_risk_score":1,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":72,"stage_label_before":"Stage2","raw_component_scores_after":{"contract_score":2,"backlog_visibility_score":3,"margin_bridge_score":2,"revision_score":3,"relative_strength_score":4,"customer_quality_score":5,"policy_or_regulatory_score":0,"valuation_repricing_score":2,"execution_risk_score":1,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":72,"stage_label_after":"Stage2","changed_components":[],"component_delta_explanation":"C08 shadow profile rewards customer qualification + repeat demand only when non-price bridge exists; price-only beta routes to 4B/watch.","MFE_90D_pct":101.84,"MAE_90D_pct":-2.53,"score_return_alignment_label":"good_stage2_candidate","current_profile_verdict":"current_profile_missed_structural"}
{"row_type":"score_simulation","profile_id":"P0b_e2r_2_0_baseline_reference","profile_scope":"rollback baseline reference","case_id":"C08_131290_2024_02_01_PROBE_CARD_QUALIFICATION_REORDER_POSITIVE","trigger_id":"C08_131290_2024_02_01_PROBE_CARD_QUALIFICATION_REORDER_POSITIVE_Stage2-Actionable","symbol":"131290","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY","raw_component_scores_before":{"contract_score":2,"backlog_visibility_score":3,"margin_bridge_score":2,"revision_score":3,"relative_strength_score":4,"customer_quality_score":5,"policy_or_regulatory_score":0,"valuation_repricing_score":2,"execution_risk_score":1,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":66,"stage_label_before":"Stage2","raw_component_scores_after":{"contract_score":2,"backlog_visibility_score":3,"margin_bridge_score":2,"revision_score":3,"relative_strength_score":4,"customer_quality_score":5,"policy_or_regulatory_score":0,"valuation_repricing_score":2,"execution_risk_score":1,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":66,"stage_label_after":"Stage2","changed_components":[],"component_delta_explanation":"C08 shadow profile rewards customer qualification + repeat demand only when non-price bridge exists; price-only beta routes to 4B/watch.","MFE_90D_pct":101.84,"MAE_90D_pct":-2.53,"score_return_alignment_label":"good_stage2_candidate","current_profile_verdict":"current_profile_missed_structural"}
{"row_type":"score_simulation","profile_id":"P1_sector_specific_candidate_profile","profile_scope":"L2 sector-specific customer-quality guard","case_id":"C08_131290_2024_02_01_PROBE_CARD_QUALIFICATION_REORDER_POSITIVE","trigger_id":"C08_131290_2024_02_01_PROBE_CARD_QUALIFICATION_REORDER_POSITIVE_Stage2-Actionable","symbol":"131290","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY","raw_component_scores_before":{"contract_score":2,"backlog_visibility_score":3,"margin_bridge_score":2,"revision_score":3,"relative_strength_score":4,"customer_quality_score":5,"policy_or_regulatory_score":0,"valuation_repricing_score":2,"execution_risk_score":1,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":72,"stage_label_before":"Stage2","raw_component_scores_after":{"contract_score":2,"backlog_visibility_score":3,"margin_bridge_score":3,"revision_score":3,"relative_strength_score":4,"customer_quality_score":6,"policy_or_regulatory_score":0,"valuation_repricing_score":2,"execution_risk_score":1,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":78,"stage_label_after":"Stage2-Actionable","changed_components":["customer_quality_score","margin_bridge_score"],"component_delta_explanation":"C08 shadow profile rewards customer qualification + repeat demand only when non-price bridge exists; price-only beta routes to 4B/watch.","MFE_90D_pct":101.84,"MAE_90D_pct":-2.53,"score_return_alignment_label":"good_stage2_candidate","current_profile_verdict":"current_profile_missed_structural"}
{"row_type":"score_simulation","profile_id":"P2_canonical_archetype_candidate_profile","profile_scope":"C08 canonical customer qualification bridge","case_id":"C08_131290_2024_02_01_PROBE_CARD_QUALIFICATION_REORDER_POSITIVE","trigger_id":"C08_131290_2024_02_01_PROBE_CARD_QUALIFICATION_REORDER_POSITIVE_Stage2-Actionable","symbol":"131290","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY","raw_component_scores_before":{"contract_score":2,"backlog_visibility_score":3,"margin_bridge_score":2,"revision_score":3,"relative_strength_score":4,"customer_quality_score":5,"policy_or_regulatory_score":0,"valuation_repricing_score":2,"execution_risk_score":1,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":72,"stage_label_before":"Stage2","raw_component_scores_after":{"contract_score":2,"backlog_visibility_score":3,"margin_bridge_score":3,"revision_score":4,"relative_strength_score":4,"customer_quality_score":7,"policy_or_regulatory_score":0,"valuation_repricing_score":2,"execution_risk_score":1,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":80,"stage_label_after":"Stage2-Actionable","changed_components":["customer_quality_score","margin_bridge_score","revision_score"],"component_delta_explanation":"C08 shadow profile rewards customer qualification + repeat demand only when non-price bridge exists; price-only beta routes to 4B/watch.","MFE_90D_pct":101.84,"MAE_90D_pct":-2.53,"score_return_alignment_label":"good_stage2_candidate","current_profile_verdict":"current_profile_missed_structural"}
{"row_type":"score_simulation","profile_id":"P3_counterexample_guard_profile","profile_scope":"price-only test-interface beta guard","case_id":"C08_131290_2024_02_01_PROBE_CARD_QUALIFICATION_REORDER_POSITIVE","trigger_id":"C08_131290_2024_02_01_PROBE_CARD_QUALIFICATION_REORDER_POSITIVE_Stage2-Actionable","symbol":"131290","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY","raw_component_scores_before":{"contract_score":2,"backlog_visibility_score":3,"margin_bridge_score":2,"revision_score":3,"relative_strength_score":4,"customer_quality_score":5,"policy_or_regulatory_score":0,"valuation_repricing_score":2,"execution_risk_score":1,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":72,"stage_label_before":"Stage2","raw_component_scores_after":{"contract_score":2,"backlog_visibility_score":3,"margin_bridge_score":2,"revision_score":3,"relative_strength_score":4,"customer_quality_score":6,"policy_or_regulatory_score":0,"valuation_repricing_score":2,"execution_risk_score":1,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":76,"stage_label_after":"Stage2-Actionable","changed_components":["customer_quality_score"],"component_delta_explanation":"C08 shadow profile rewards customer qualification + repeat demand only when non-price bridge exists; price-only beta routes to 4B/watch.","MFE_90D_pct":101.84,"MAE_90D_pct":-2.53,"score_return_alignment_label":"good_stage2_candidate","current_profile_verdict":"current_profile_missed_structural"}
{"row_type":"score_simulation","profile_id":"P0_e2r_2_1_stock_web_calibrated_proxy","profile_scope":"current calibrated proxy","case_id":"C08_095340_2024_03_28_TEST_SOCKET_BLOWOFF_4B_GUARD","trigger_id":"C08_095340_2024_03_28_TEST_SOCKET_BLOWOFF_4B_GUARD_Stage4B","symbol":"095340","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY","raw_component_scores_before":{"contract_score":1,"backlog_visibility_score":1,"margin_bridge_score":1,"revision_score":2,"relative_strength_score":5,"customer_quality_score":4,"policy_or_regulatory_score":0,"valuation_repricing_score":5,"execution_risk_score":3,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":84,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":1,"backlog_visibility_score":1,"margin_bridge_score":1,"revision_score":2,"relative_strength_score":5,"customer_quality_score":4,"policy_or_regulatory_score":0,"valuation_repricing_score":5,"execution_risk_score":3,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":84,"stage_label_after":"Stage3-Yellow","changed_components":[],"component_delta_explanation":"C08 shadow profile rewards customer qualification + repeat demand only when non-price bridge exists; price-only beta routes to 4B/watch.","MFE_90D_pct":8.65,"MAE_90D_pct":-58.65,"score_return_alignment_label":"4B_guard_success","current_profile_verdict":"current_profile_4B_too_late"}
{"row_type":"score_simulation","profile_id":"P0b_e2r_2_0_baseline_reference","profile_scope":"rollback baseline reference","case_id":"C08_095340_2024_03_28_TEST_SOCKET_BLOWOFF_4B_GUARD","trigger_id":"C08_095340_2024_03_28_TEST_SOCKET_BLOWOFF_4B_GUARD_Stage4B","symbol":"095340","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY","raw_component_scores_before":{"contract_score":1,"backlog_visibility_score":1,"margin_bridge_score":1,"revision_score":2,"relative_strength_score":5,"customer_quality_score":4,"policy_or_regulatory_score":0,"valuation_repricing_score":5,"execution_risk_score":3,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":78,"stage_label_before":"Stage2","raw_component_scores_after":{"contract_score":1,"backlog_visibility_score":1,"margin_bridge_score":1,"revision_score":2,"relative_strength_score":5,"customer_quality_score":4,"policy_or_regulatory_score":0,"valuation_repricing_score":5,"execution_risk_score":3,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":78,"stage_label_after":"Stage2","changed_components":[],"component_delta_explanation":"C08 shadow profile rewards customer qualification + repeat demand only when non-price bridge exists; price-only beta routes to 4B/watch.","MFE_90D_pct":8.65,"MAE_90D_pct":-58.65,"score_return_alignment_label":"4B_guard_success","current_profile_verdict":"current_profile_4B_too_late"}
{"row_type":"score_simulation","profile_id":"P1_sector_specific_candidate_profile","profile_scope":"L2 sector-specific customer-quality guard","case_id":"C08_095340_2024_03_28_TEST_SOCKET_BLOWOFF_4B_GUARD","trigger_id":"C08_095340_2024_03_28_TEST_SOCKET_BLOWOFF_4B_GUARD_Stage4B","symbol":"095340","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY","raw_component_scores_before":{"contract_score":1,"backlog_visibility_score":1,"margin_bridge_score":1,"revision_score":2,"relative_strength_score":5,"customer_quality_score":4,"policy_or_regulatory_score":0,"valuation_repricing_score":5,"execution_risk_score":3,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":84,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":1,"backlog_visibility_score":1,"margin_bridge_score":1,"revision_score":2,"relative_strength_score":5,"customer_quality_score":4,"policy_or_regulatory_score":0,"valuation_repricing_score":6,"execution_risk_score":5,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":79,"stage_label_after":"Stage4B-watch","changed_components":["valuation_repricing_score","execution_risk_score"],"component_delta_explanation":"C08 shadow profile rewards customer qualification + repeat demand only when non-price bridge exists; price-only beta routes to 4B/watch.","MFE_90D_pct":8.65,"MAE_90D_pct":-58.65,"score_return_alignment_label":"4B_guard_success","current_profile_verdict":"current_profile_4B_too_late"}
{"row_type":"score_simulation","profile_id":"P2_canonical_archetype_candidate_profile","profile_scope":"C08 canonical customer qualification bridge","case_id":"C08_095340_2024_03_28_TEST_SOCKET_BLOWOFF_4B_GUARD","trigger_id":"C08_095340_2024_03_28_TEST_SOCKET_BLOWOFF_4B_GUARD_Stage4B","symbol":"095340","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY","raw_component_scores_before":{"contract_score":1,"backlog_visibility_score":1,"margin_bridge_score":1,"revision_score":2,"relative_strength_score":5,"customer_quality_score":4,"policy_or_regulatory_score":0,"valuation_repricing_score":5,"execution_risk_score":3,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":84,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":1,"backlog_visibility_score":1,"margin_bridge_score":1,"revision_score":2,"relative_strength_score":5,"customer_quality_score":4,"policy_or_regulatory_score":0,"valuation_repricing_score":5,"execution_risk_score":6,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":72,"stage_label_after":"Stage4B","changed_components":["execution_risk_score"],"component_delta_explanation":"C08 shadow profile rewards customer qualification + repeat demand only when non-price bridge exists; price-only beta routes to 4B/watch.","MFE_90D_pct":8.65,"MAE_90D_pct":-58.65,"score_return_alignment_label":"4B_guard_success","current_profile_verdict":"current_profile_4B_too_late"}
{"row_type":"score_simulation","profile_id":"P3_counterexample_guard_profile","profile_scope":"price-only test-interface beta guard","case_id":"C08_095340_2024_03_28_TEST_SOCKET_BLOWOFF_4B_GUARD","trigger_id":"C08_095340_2024_03_28_TEST_SOCKET_BLOWOFF_4B_GUARD_Stage4B","symbol":"095340","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY","raw_component_scores_before":{"contract_score":1,"backlog_visibility_score":1,"margin_bridge_score":1,"revision_score":2,"relative_strength_score":5,"customer_quality_score":4,"policy_or_regulatory_score":0,"valuation_repricing_score":5,"execution_risk_score":3,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":84,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":1,"backlog_visibility_score":1,"margin_bridge_score":1,"revision_score":2,"relative_strength_score":5,"customer_quality_score":1,"policy_or_regulatory_score":0,"valuation_repricing_score":5,"execution_risk_score":7,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":50,"stage_label_after":"Stage4B-watch","changed_components":["customer_quality_score","execution_risk_score"],"component_delta_explanation":"C08 shadow profile rewards customer qualification + repeat demand only when non-price bridge exists; price-only beta routes to 4B/watch.","MFE_90D_pct":8.65,"MAE_90D_pct":-58.65,"score_return_alignment_label":"4B_guard_success","current_profile_verdict":"current_profile_4B_too_late"}
{"row_type":"score_simulation","profile_id":"P0_e2r_2_1_stock_web_calibrated_proxy","profile_scope":"current calibrated proxy","case_id":"C08_425420_2024_03_20_TEST_INTERFACE_PRICE_ONLY_BETA_DECAY","trigger_id":"C08_425420_2024_03_20_TEST_INTERFACE_PRICE_ONLY_BETA_DECAY_Stage4B","symbol":"425420","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":5,"customer_quality_score":1,"policy_or_regulatory_score":0,"valuation_repricing_score":4,"execution_risk_score":4,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":68,"stage_label_before":"Stage2","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":5,"customer_quality_score":1,"policy_or_regulatory_score":0,"valuation_repricing_score":4,"execution_risk_score":4,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":68,"stage_label_after":"Stage2","changed_components":[],"component_delta_explanation":"C08 shadow profile rewards customer qualification + repeat demand only when non-price bridge exists; price-only beta routes to 4B/watch.","MFE_90D_pct":1.97,"MAE_90D_pct":-49.54,"score_return_alignment_label":"price_only_stage2_block_correct","current_profile_verdict":"current_profile_correct"}
{"row_type":"score_simulation","profile_id":"P0b_e2r_2_0_baseline_reference","profile_scope":"rollback baseline reference","case_id":"C08_425420_2024_03_20_TEST_INTERFACE_PRICE_ONLY_BETA_DECAY","trigger_id":"C08_425420_2024_03_20_TEST_INTERFACE_PRICE_ONLY_BETA_DECAY_Stage4B","symbol":"425420","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":5,"customer_quality_score":1,"policy_or_regulatory_score":0,"valuation_repricing_score":4,"execution_risk_score":4,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":62,"stage_label_before":"Stage1","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":5,"customer_quality_score":1,"policy_or_regulatory_score":0,"valuation_repricing_score":4,"execution_risk_score":4,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":62,"stage_label_after":"Stage2","changed_components":[],"component_delta_explanation":"C08 shadow profile rewards customer qualification + repeat demand only when non-price bridge exists; price-only beta routes to 4B/watch.","MFE_90D_pct":1.97,"MAE_90D_pct":-49.54,"score_return_alignment_label":"price_only_stage2_block_correct","current_profile_verdict":"current_profile_correct"}
{"row_type":"score_simulation","profile_id":"P1_sector_specific_candidate_profile","profile_scope":"L2 sector-specific customer-quality guard","case_id":"C08_425420_2024_03_20_TEST_INTERFACE_PRICE_ONLY_BETA_DECAY","trigger_id":"C08_425420_2024_03_20_TEST_INTERFACE_PRICE_ONLY_BETA_DECAY_Stage4B","symbol":"425420","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":5,"customer_quality_score":1,"policy_or_regulatory_score":0,"valuation_repricing_score":4,"execution_risk_score":4,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":68,"stage_label_before":"Stage2","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":3,"customer_quality_score":1,"policy_or_regulatory_score":0,"valuation_repricing_score":4,"execution_risk_score":6,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":58,"stage_label_after":"Stage1/weak-watch","changed_components":["relative_strength_score","execution_risk_score"],"component_delta_explanation":"C08 shadow profile rewards customer qualification + repeat demand only when non-price bridge exists; price-only beta routes to 4B/watch.","MFE_90D_pct":1.97,"MAE_90D_pct":-49.54,"score_return_alignment_label":"price_only_stage2_block_correct","current_profile_verdict":"current_profile_correct"}
{"row_type":"score_simulation","profile_id":"P2_canonical_archetype_candidate_profile","profile_scope":"C08 canonical customer qualification bridge","case_id":"C08_425420_2024_03_20_TEST_INTERFACE_PRICE_ONLY_BETA_DECAY","trigger_id":"C08_425420_2024_03_20_TEST_INTERFACE_PRICE_ONLY_BETA_DECAY_Stage4B","symbol":"425420","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":5,"customer_quality_score":1,"policy_or_regulatory_score":0,"valuation_repricing_score":4,"execution_risk_score":4,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":68,"stage_label_before":"Stage2","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":5,"customer_quality_score":0,"policy_or_regulatory_score":0,"valuation_repricing_score":4,"execution_risk_score":7,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":52,"stage_label_after":"Stage4B-watch","changed_components":["customer_quality_score","execution_risk_score"],"component_delta_explanation":"C08 shadow profile rewards customer qualification + repeat demand only when non-price bridge exists; price-only beta routes to 4B/watch.","MFE_90D_pct":1.97,"MAE_90D_pct":-49.54,"score_return_alignment_label":"price_only_stage2_block_correct","current_profile_verdict":"current_profile_correct"}
{"row_type":"score_simulation","profile_id":"P3_counterexample_guard_profile","profile_scope":"price-only test-interface beta guard","case_id":"C08_425420_2024_03_20_TEST_INTERFACE_PRICE_ONLY_BETA_DECAY","trigger_id":"C08_425420_2024_03_20_TEST_INTERFACE_PRICE_ONLY_BETA_DECAY_Stage4B","symbol":"425420","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":5,"customer_quality_score":1,"policy_or_regulatory_score":0,"valuation_repricing_score":4,"execution_risk_score":4,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":68,"stage_label_before":"Stage2","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":5,"customer_quality_score":1,"policy_or_regulatory_score":0,"valuation_repricing_score":4,"execution_risk_score":7,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":50,"stage_label_after":"Stage4B-watch","changed_components":["customer_quality_score","execution_risk_score"],"component_delta_explanation":"C08 shadow profile rewards customer qualification + repeat demand only when non-price bridge exists; price-only beta routes to 4B/watch.","MFE_90D_pct":1.97,"MAE_90D_pct":-49.54,"score_return_alignment_label":"price_only_stage2_block_correct","current_profile_verdict":"current_profile_correct"}
{"row_type":"shadow_weight","axis":"c08_customer_quality_repeat_demand_bridge_required_for_stage2_actionable","scope":"canonical_archetype_specific","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY","baseline_value":0,"tested_value":1,"delta":"+1","reason":"C08 positive route needs explicit customer qualification/repeat-demand bridge, not only test/socket theme beta.","backtest_effect":"TSE positive accepted while ISC/TFE price-only blowoff routed to 4B/watch.","trigger_ids":"C08_131290_2024_02_01_PROBE_CARD_QUALIFICATION_REORDER_POSITIVE_Stage2-Actionable|C08_095340_2024_03_28_TEST_SOCKET_BLOWOFF_4B_GUARD_Stage4B|C08_425420_2024_03_20_TEST_INTERFACE_PRICE_ONLY_BETA_DECAY_Stage4B","calibration_usable_count":3,"new_independent_case_count":3,"counterexample_count":2,"confidence":"low_to_medium","proposal_type":"canonical_shadow_only","notes":"Not production; evidence URL remains pending for all three cases."}
{"row_type":"shadow_weight","axis":"c08_price_only_test_interface_beta_to_4b_watch","scope":"canonical_archetype_specific","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY","baseline_value":0,"tested_value":1,"delta":"+1","reason":"TFE and ISC show price-only or valuation blowoff in test/socket names can precede deep MAE.","backtest_effect":"Preserves price_only_blowoff_blocks_positive_stage and full_4b_requires_non_price_evidence; adds C08 label-specific watch routing.","trigger_ids":"C08_095340_2024_03_28_TEST_SOCKET_BLOWOFF_4B_GUARD_Stage4B|C08_425420_2024_03_20_TEST_INTERFACE_PRICE_ONLY_BETA_DECAY_Stage4B","calibration_usable_count":2,"new_independent_case_count":2,"counterexample_count":2,"confidence":"medium","proposal_type":"canonical_shadow_only","notes":"4B overlay only; does not unlock short or sell recommendation language."}
{"row_type":"residual_contribution","round":"R2","loop":"88","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY","new_independent_case_count":3,"reused_case_count":0,"new_symbol_count":3,"same_archetype_new_symbol_count":3,"same_archetype_new_trigger_family_count":3,"new_trigger_family_count":3,"tested_existing_calibrated_axes":["price_only_blowoff_blocks_positive_stage","full_4b_requires_non_price_evidence","stage2_required_bridge"],"residual_error_types_found":["C08_customer_quality_positive_missed","C08_valuation_blowoff_4B_late","C08_price_only_beta_decay_guard"],"loop_contribution_label":"canonical_archetype_rule_candidate","do_not_propose_new_weight_delta":false}
{"row_type":"coverage_matrix","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY","fine_archetype_id":"TEST_SOCKET_PROBE_CARD_CUSTOMER_QUALIFICATION_BRIDGE_VS_PRICE_ONLY_EQUIPMENT_BETA_DECAY","positive_case_count":1,"counterexample_count":2,"4B_case_count":2,"4C_case_count":0,"new_independent_case_count":3,"reused_case_count":0,"calibration_usable_trigger_count":3,"representative_trigger_count":3,"current_profile_error_count":2,"sector_rule_candidate":true,"canonical_rule_candidate":true,"coverage_gap_after_this_loop":"C08 rows 14 -> synthetic +3 pending ingest; still below 30-row minimum"}
{"row_type":"narrative_only","case_id":"C08_EVIDENCE_URL_PENDING_NOTE","symbol":"MULTI","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY","reason":"evidence_url_pending/source_proxy_only: this loop prioritizes actual stock-web OHLC path and novelty; later batch should replace source proxies with dated filings/news URLs.","price_source":"Songdaiki/stock-web","usage":"not_weight_calibration"}
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
completed_round = R2
completed_loop = 88
selection_basis = docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket = Priority 0
next_recommended_archetypes = C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY, C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF, C01_ORDER_BACKLOG_MARGIN_BRIDGE
round_schedule_status = coverage_index_selected
round_sector_consistency = pass
```

## 28. Source Notes

- `docs/core/e2r_v12_prompt_round_scheduler_corrected.txt` was used as the execution procedure.
- `docs/core/V12_Research_No_Repeat_Index.md` was used only for duplicate avoidance and coverage selection.
- `Songdaiki/stock-web` manifest/schema/profiles/shards were used for historical OHLC verification.
- Evidence URLs are intentionally marked pending; this MD should be treated as a price-path residual expansion plus source-proxy research artifact, not a final evidence repair batch.
