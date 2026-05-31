# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
round = R4
loop = 71
scheduled_round = R4
scheduled_loop = 71
large_sector_id = L4_MATERIALS_SPREAD_RESOURCE
canonical_archetype_id = C16_STRATEGIC_RESOURCE_POLICY_SUPPLY
fine_archetype_id = STRATEGIC_RESOURCE_POLICY_SUPPLY_CONVERSION_GUARD
loop_objective = coverage_gap_fill | counterexample_mining | 4B_non_price_requirement_stress_test | canonical_archetype_specific_exception
research_session = post_calibrated_sector_archetype_residual_research
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
production_scoring_changed = false
shadow_weight_only = true
```

## 1. Current Calibrated Profile Assumption

```text
current_default_profile_proxy = e2r_2_1_stock_web_calibrated_proxy
previous_baseline_reference = e2r_2_0_baseline_reference
```

This loop does not re-prove the global Stage2/Yellow/Green/4B/4C rules. It tests whether C16 strategic-resource policy/supply cases need a stronger distinction between:

```text
resource policy / mine headline / supply-chain theme
vs.
funded offtake, contract economics, margin bridge, FCF conversion, and durable supply visibility
```

## 2. Round / Large Sector / Canonical Archetype Scope

```text
round_sector_consistency = pass
R4 -> L4_MATERIALS_SPREAD_RESOURCE
canonical_archetype_id = C16_STRATEGIC_RESOURCE_POLICY_SUPPLY
```

C16 is treated as a strategic resource / supply policy archetype. The research unit is not a live recommendation list. It is a historical calibration sample set.

## 3. Previous Coverage / Duplicate Avoidance Check

No-Repeat snapshot used as the anti-repetition ledger:

```text
C16_STRATEGIC_RESOURCE_POLICY_SUPPLY prior coverage: 7 rows / 4 symbols
prior top symbols: 005290, 027580, 047400, 093370
hold axis: stage2_bonus_candidate_delta
hold reason: need_3_positive_symbols_2_counterexamples_8_rows_3_transitions
```

This MD avoids the prior top-covered C16 symbols and uses four new symbols:

```text
005490 POSCO홀딩스
001570 금양
000910 유니온
012320 경동인베스트
```

Duplicate policy:

```text
hard_duplicate_check = pass
same canonical allowed = true
same canonical + same symbol + same trigger_type + same entry_date = not used
```

## 4. Stock-Web OHLC Input / Price Source Validation

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
```

Manifest basis used:

```text
source_name = FinanceData/marcap
source_repo_url = https://github.com/FinanceData/marcap
price_adjustment_status = raw_unadjusted_marcap
min_date = 1995-05-02
max_date = 2026-02-20
tradable_row_count = 14354401
raw_row_count = 15214118
symbol_count = 5414
active_like_symbol_count = 2868
inactive_or_delisted_like_symbol_count = 2546
calibration_shard_root = atlas/ohlcv_tradable_by_symbol_year
raw_shard_root = atlas/ohlcv_raw_by_symbol_year
```

## 5. Historical Eligibility Gate

| case_id | symbol | entry_date | forward 180D | corporate-action window | calibration_usable |
|---|---|---|---:|---|---|
| C16_R4L71_POSCO_005490_20230410 | 005490 | 2023-04-10 | >=180 | clean_by_profile_review | true |
| C16_R4L71_GEUMYANG_001570_20230221 | 001570 | 2023-02-21 | >=180 | clean_by_profile_review | true |
| C16_R4L71_UNION_000910_20230217 | 000910 | 2023-02-17 | >=180 | clean_by_profile_review | true |
| C16_R4L71_KDINV_012320_20221020 | 012320 | 2022-10-20 | >=180 | clean_by_profile_review | true |

## 6. Canonical Archetype Compression Map

| fine_archetype_id | canonical_archetype_id | compression note |
|---|---|---|
| LITHIUM_VERTICAL_INTEGRATION_SUPPLY_LOCK | C16_STRATEGIC_RESOURCE_POLICY_SUPPLY | resource supply visibility must convert into margin/FCF, not only lithium keyword |
| LITHIUM_MINE_MOU_HIGH_MAE_STRESS | C16_STRATEGIC_RESOURCE_POLICY_SUPPLY | mine/MOU/resource option creates optionality but needs cashflow conversion guard |
| RARE_EARTH_POLICY_EVENT_PREMIUM | C16_STRATEGIC_RESOURCE_POLICY_SUPPLY | policy shock is event premium until contract/order/revenue conversion appears |
| DOMESTIC_TITANIUM_RESOURCE_EVENT_PREMIUM | C16_STRATEGIC_RESOURCE_POLICY_SUPPLY | mine/discovery narrative can create blowoff without durable earnings visibility |

## 7. Case Selection Summary

| case_id | symbol | company | role | positive_or_counterexample | new independent? | reason |
|---|---|---|---|---|---|---|
| C16_R4L71_POSCO_005490_20230410 | 005490 | POSCO홀딩스 | structural_success | positive | true | lithium/resource vertical integration with durable large-cap execution route |
| C16_R4L71_GEUMYANG_001570_20230221 | 001570 | 금양 | high_mae_success | counterexample | true | strong price path but high reliance on resource optionality and high drawdown risk |
| C16_R4L71_UNION_000910_20230217 | 000910 | 유니온 | failed_rerating | counterexample | true | rare-earth policy event premium without durable EPS/FCF bridge |
| C16_R4L71_KDINV_012320_20221020 | 012320 | 경동인베스트 | 4B_too_early | counterexample | true | domestic titanium/resource discovery narrative became event blowoff, not confirmed Green |

## 8. Positive vs Counterexample Balance

```text
positive_case_count = 1
counterexample_count = 3
4B_case_count = 2
4C_case_count = 0
calibration_usable_case_count = 4
minimum_positive_case_count = pass
minimum_counterexample_count = pass
minimum_calibration_usable_case_count = pass
```

## 9. Evidence Source Map

| case_id | evidence_available_at_that_date | evidence_source | evidence_url_pending | source_proxy_only |
|---|---|---|---|---|
| C16_R4L71_POSCO_005490_20230410 | lithium / battery-material supply-chain expansion was publicly reflected before entry | company/press/research-source proxy | true | true |
| C16_R4L71_GEUMYANG_001570_20230221 | lithium mine/resource optionality narrative was visible before entry | public news-source proxy | true | true |
| C16_R4L71_UNION_000910_20230217 | rare-earth geopolitical/policy event narrative was visible before entry | public news-source proxy | true | true |
| C16_R4L71_KDINV_012320_20221020 | domestic titanium/resource discovery narrative was visible before entry | public news-source proxy | true | true |

Data-quality note: this run is useful for C16 residual shape and price-path stress, but exact evidence URLs still need replacement before promotion. Therefore this MD proposes a shadow guard candidate, not a production weight delta.

## 10. Price Data Source Map

| symbol | profile_path | price_shard_path |
|---|---|---|
| 005490 | atlas/symbol_profiles/005/005490.json | atlas/ohlcv_tradable_by_symbol_year/005/005490/2023.csv |
| 001570 | atlas/symbol_profiles/001/001570.json | atlas/ohlcv_tradable_by_symbol_year/001/001570/2023.csv |
| 000910 | atlas/symbol_profiles/000/000910.json | atlas/ohlcv_tradable_by_symbol_year/000/000910/2023.csv |
| 012320 | atlas/symbol_profiles/012/012320.json | atlas/ohlcv_tradable_by_symbol_year/012/012320/2022.csv |

## 11. Case-by-Case Trigger Grid

| trigger_id | case_id | trigger_type | trigger_date | entry_date | entry_price | outcome |
|---|---|---|---|---|---:|---|
| TR_C16_POSCO_S2A_20230410 | C16_R4L71_POSCO_005490_20230410 | Stage2-Actionable | 2023-04-10 | 2023-04-10 | 398500 | good_stage2_high_mfe |
| TR_C16_GEUMYANG_S2_20230221 | C16_R4L71_GEUMYANG_001570_20230221 | Stage2 | 2023-02-21 | 2023-02-21 | 34700 | high_mfe_high_mae_event_risk |
| TR_C16_UNION_S2_20230217 | C16_R4L71_UNION_000910_20230217 | Stage2 | 2023-02-17 | 2023-02-17 | 6280 | event_premium_fade |
| TR_C16_KDINV_S2_20221020 | C16_R4L71_KDINV_012320_20221020 | Stage2 | 2022-10-20 | 2022-10-20 | 37550 | price_blowoff_then_drawdown |
| TR_C16_KDINV_4B_20221116 | C16_R4L71_KDINV_012320_20221020 | Stage4B | 2022-11-16 | 2022-11-16 | 124000 | non_price_not_confirmed_full_4B |
| TR_C16_GEUMYANG_4B_20230726 | C16_R4L71_GEUMYANG_001570_20230221 | Stage4B | 2023-07-26 | 2023-07-26 | 152200 | price_only_or_event_premium_4B |

## 12. Trigger-Level OHLC Backtest Tables

MFE/MAE values use Stock-Web raw/unadjusted tradable OHLC rows and the prompt formula. Values are rounded to two decimals.

| trigger_id | entry_price | MFE_30D_pct | MFE_90D_pct | MFE_180D_pct | MAE_30D_pct | MAE_90D_pct | MAE_180D_pct | peak_date | peak_price | drawdown_after_peak_pct |
|---|---:|---:|---:|---:|---:|---:|---:|---|---:|---:|
| TR_C16_POSCO_S2A_20230410 | 398500 | 9.41 | 91.72 | 91.72 | -10.66 | -10.66 | -10.66 | 2023-07-26 | 764000 | -49.87 |
| TR_C16_GEUMYANG_S2_20230221 | 34700 | 143.52 | 459.08 | 459.08 | -12.25 | -12.25 | -12.25 | 2023-07-26 | 194000 | -43.71 |
| TR_C16_UNION_S2_20230217 | 6280 | 15.76 | 38.69 | 38.69 | -20.62 | -20.62 | -25.16 | 2023-04-06 | 8710 | -37.54 |
| TR_C16_KDINV_S2_20221020 | 37550 | 272.84 | 272.84 | 272.84 | -23.57 | -23.57 | -23.57 | 2022-11-16 | 140000 | -60.29 |

## 13. Current Calibrated Profile Stress Test

| case_id | current_profile_verdict | reason |
|---|---|---|
| C16_R4L71_POSCO_005490_20230410 | current_profile_correct | Stage2-Actionable is useful; Green still needs durable EPS/FCF and capital conversion evidence |
| C16_R4L71_GEUMYANG_001570_20230221 | current_profile_4B_too_late | price path rewarded early optionality, but high-MAE and event-risk require earlier 4B watch |
| C16_R4L71_UNION_000910_20230217 | current_profile_false_positive | Stage2 bonus should not apply to policy/resource keyword without non-price bridge |
| C16_R4L71_KDINV_012320_20221020 | current_profile_4B_too_late | blowoff was visible before durable supply/earnings confirmation; full Green should remain blocked |

## 14. Stage2 / Yellow / Green Comparison

C16 does not need lower Green thresholds. It needs a stricter bridge from resource/policy narrative into:

```text
1. funded offtake / final contract / government budget
2. reserve or supply volume with commercialization schedule
3. margin bridge or FCF conversion
4. non-price evidence after price rally
```

## 15. 4B Local vs Full-window Timing Audit

| case_id | four_b_local_peak_proximity | four_b_full_window_peak_proximity | verdict |
|---|---:|---:|---|
| C16_R4L71_GEUMYANG_001570_20230221 | 1.00 | 1.00 | price_only_or_event_premium_peak_requires_4B_watch |
| C16_R4L71_KDINV_012320_20221020 | 1.00 | 1.00 | event_blowoff_good_4B_watch_candidate |

## 16. 4C Protection Audit

No hard 4C trigger is promoted in this loop. The available evidence supports earlier 4B/watch and Stage2 bridge guard, not hard thesis-break routing.

## 17. Sector-Specific Rule Candidate

```text
rule_scope = sector_specific
axis = L4_STRATEGIC_RESOURCE_STAGE2_NON_PRICE_BRIDGE
candidate = require_non_price_bridge_for_resource_policy_supply_theme
status = shadow_only
```

## 18. Canonical-Archetype Rule Candidate

```text
rule_scope = canonical_archetype_specific
canonical_archetype_id = C16_STRATEGIC_RESOURCE_POLICY_SUPPLY
candidate_rule = C16 Stage2 bonus should require at least one of: funded offtake, final contract, reserve-to-production schedule, margin bridge, or FCF conversion.
price-only/resource-keyword rows should route to Stage1/Stage2-watch or 4B-watch stress, not Green.
```

## 19. Before / After Backtest Comparison

| profile | eligible_trigger_count | avg_MFE_90D_pct | avg_MAE_90D_pct | false_positive_rate | score_return_alignment_verdict |
|---|---:|---:|---:|---:|---|
| P0 e2r_2_1_stock_web_calibrated_proxy | 4 | 215.58 | -16.78 | 0.50 | high return but poor evidence discrimination |
| P1 sector_specific_candidate_profile | 4 | 215.58 | -16.78 | 0.25 | improved by separating POSCO-like execution path from event premium |
| P2 canonical_archetype_candidate_profile | 4 | 215.58 | -16.78 | 0.25 | C16 bridge guard improves score-return explanation |
| P3 counterexample_guard_profile | 4 | 215.58 | -16.78 | 0.00 | best false-positive control but may under-score high-MFE optionality |

## 20. Score-Return Alignment Matrix

| case_id | score_price_alignment | note |
|---|---|---|
| C16_R4L71_POSCO_005490_20230410 | aligned | non-price supply-chain route and actual MFE support Stage2-Actionable |
| C16_R4L71_GEUMYANG_001570_20230221 | mixed_high_mae | huge MFE but evidence conversion weaker than price path |
| C16_R4L71_UNION_000910_20230217 | weak_alignment | event premium without durable EPS/FCF bridge |
| C16_R4L71_KDINV_012320_20221020 | weak_alignment_4b_watch | resource discovery headline created blowoff before durable thesis |

## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive_case_count | counterexample_count | 4B_case_count | 4C_case_count | new_independent_case_count | reused_case_count | calibration_usable_trigger_count | representative_trigger_count | current_profile_error_count | sector_rule_candidate | canonical_rule_candidate | coverage_gap_after_this_loop |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| L4_MATERIALS_SPREAD_RESOURCE | C16_STRATEGIC_RESOURCE_POLICY_SUPPLY | STRATEGIC_RESOURCE_POLICY_SUPPLY_CONVERSION_GUARD | 1 | 3 | 2 | 0 | 4 | 0 | 4 | 4 | 3 | true | true | still needs verified evidence URLs and more non-resource-keyword positive cases |

## 22. Residual Contribution Summary

```text
new_independent_case_count: 4
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 4
new_canonical_archetype_count: 0
new_fine_archetype_count: 4
new_trigger_family_count: 3
tested_existing_calibrated_axes: ["stage2_actionable_evidence_bonus", "price_only_blowoff_blocks_positive_stage", "full_4b_requires_non_price_evidence"]
residual_error_types_found: ["resource_keyword_false_positive", "event_premium_4B_too_late", "high_MAE_optional_resource_success"]
new_axis_proposed: C16_STRATEGIC_RESOURCE_STAGE2_NON_PRICE_BRIDGE_SHADOW_ONLY
existing_axis_strengthened: price_only_blowoff_blocks_positive_stage for C16 resource-policy rows
existing_axis_weakened: null
existing_axis_kept: stage3_green_total_min, stage3_green_revision_min, full_4b_requires_non_price_evidence
sector_specific_rule_candidate: true
canonical_archetype_rule_candidate: true
no_new_signal_reason: null
loop_contribution_label: counterexample_added
```

```text
do_not_propose_new_weight_delta = true
reason = evidence_url_pending/source_proxy_only fields must be replaced with exact dated public URLs before promotion
```

## 23. Validation Scope / Non-Validation Scope

Validation scope:

```text
- Stock-Web OHLC path validation
- 30D/90D/180D MFE/MAE stress
- No-Repeat hard duplicate avoidance
- C16 positive/counterexample balance
```

Non-validation scope:

```text
- No production scoring patch
- No live scan
- No investment recommendation
- Exact evidence URL replacement remains required
```

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,C16_STAGE2_NON_PRICE_BRIDGE,canonical_archetype_specific,L4_MATERIALS_SPREAD_RESOURCE,C16_STRATEGIC_RESOURCE_POLICY_SUPPLY,not_configured,require_supply_contract_or_cashflow_conversion_guard,guardrail_only,"C16 resource/policy themes show high MFE but weak evidence discrimination and high-MAE/event-premium risk","reduces resource-keyword false positives without lowering Green threshold","TR_C16_POSCO_S2A_20230410|TR_C16_GEUMYANG_S2_20230221|TR_C16_UNION_S2_20230217|TR_C16_KDINV_S2_20221020",4,4,3,low,canonical_shadow_only,"not production; exact evidence URLs pending"
```

## 25. Machine-Readable Rows

```jsonl
{"row_type":"case","case_id":"C16_R4L71_POSCO_005490_20230410","symbol":"005490","company_name":"POSCO홀딩스","round":"R4","loop":"71","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C16_STRATEGIC_RESOURCE_POLICY_SUPPLY","fine_archetype_id":"LITHIUM_VERTICAL_INTEGRATION_SUPPLY_LOCK","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"TR_C16_POSCO_S2A_20230410","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"aligned","current_profile_verdict":"current_profile_correct","price_source":"Songdaiki/stock-web","notes":"positive case but Green still requires durable EPS/FCF conversion"}
{"row_type":"case","case_id":"C16_R4L71_GEUMYANG_001570_20230221","symbol":"001570","company_name":"금양","round":"R4","loop":"71","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C16_STRATEGIC_RESOURCE_POLICY_SUPPLY","fine_archetype_id":"LITHIUM_MINE_MOU_HIGH_MAE_STRESS","case_type":"high_mae_success","positive_or_counterexample":"counterexample","best_trigger":"TR_C16_GEUMYANG_S2_20230221","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"mixed_high_mae","current_profile_verdict":"current_profile_4B_too_late","price_source":"Songdaiki/stock-web","notes":"resource optionality had huge MFE but weak conversion evidence and 4B watch need"}
{"row_type":"case","case_id":"C16_R4L71_UNION_000910_20230217","symbol":"000910","company_name":"유니온","round":"R4","loop":"71","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C16_STRATEGIC_RESOURCE_POLICY_SUPPLY","fine_archetype_id":"RARE_EARTH_POLICY_EVENT_PREMIUM","case_type":"failed_rerating","positive_or_counterexample":"counterexample","best_trigger":"TR_C16_UNION_S2_20230217","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"weak_alignment","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"rare-earth policy event premium without durable EPS/FCF bridge"}
{"row_type":"case","case_id":"C16_R4L71_KDINV_012320_20221020","symbol":"012320","company_name":"경동인베스트","round":"R4","loop":"71","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C16_STRATEGIC_RESOURCE_POLICY_SUPPLY","fine_archetype_id":"DOMESTIC_TITANIUM_RESOURCE_EVENT_PREMIUM","case_type":"4B_too_early","positive_or_counterexample":"counterexample","best_trigger":"TR_C16_KDINV_S2_20221020","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"weak_alignment_4b_watch","current_profile_verdict":"current_profile_4B_too_late","price_source":"Songdaiki/stock-web","notes":"resource discovery narrative became blowoff before durable thesis"}
{"row_type":"trigger","trigger_id":"TR_C16_POSCO_S2A_20230410","case_id":"C16_R4L71_POSCO_005490_20230410","symbol":"005490","company_name":"POSCO홀딩스","round":"R4","loop":"71","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C16_STRATEGIC_RESOURCE_POLICY_SUPPLY","fine_archetype_id":"LITHIUM_VERTICAL_INTEGRATION_SUPPLY_LOCK","loop_objective":"coverage_gap_fill|counterexample_mining","trigger_type":"Stage2-Actionable","trigger_date":"2023-04-10","entry_date":"2023-04-10","entry_price":398500,"evidence_available_at_that_date":"lithium/resource vertical integration and supply-chain expansion narrative visible before entry","evidence_source":"company/press/research-source proxy; exact URL pending","stage2_evidence_fields":["public_event_or_disclosure","capacity_or_volume_route","policy_or_regulatory_optionality"],"stage3_evidence_fields":["financial_visibility","durable_customer_confirmation"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/005/005490/2023.csv","profile_path":"atlas/symbol_profiles/005/005490.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":9.41,"MFE_90D_pct":91.72,"MFE_180D_pct":91.72,"MAE_30D_pct":-10.66,"MAE_90D_pct":-10.66,"MAE_180D_pct":-10.66,"peak_date":"2023-07-26","peak_price":764000,"drawdown_after_peak_pct":-49.87,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"trigger_outcome_label":"good_stage2_high_mfe","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C16_POSCO_005490_20230410","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"evidence_url_pending":true,"source_proxy_only":true}
{"row_type":"trigger","trigger_id":"TR_C16_GEUMYANG_S2_20230221","case_id":"C16_R4L71_GEUMYANG_001570_20230221","symbol":"001570","company_name":"금양","round":"R4","loop":"71","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C16_STRATEGIC_RESOURCE_POLICY_SUPPLY","fine_archetype_id":"LITHIUM_MINE_MOU_HIGH_MAE_STRESS","loop_objective":"counterexample_mining|4B_non_price_requirement_stress_test","trigger_type":"Stage2","trigger_date":"2023-02-21","entry_date":"2023-02-21","entry_price":34700,"evidence_available_at_that_date":"lithium mine/resource optionality narrative visible before entry","evidence_source":"public-news-source proxy; exact URL pending","stage2_evidence_fields":["public_event_or_disclosure","policy_or_regulatory_optionality","relative_strength"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["valuation_blowoff","positioning_overheat","price_only_local_peak"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/001/001570/2023.csv","profile_path":"atlas/symbol_profiles/001/001570.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":143.52,"MFE_90D_pct":459.08,"MFE_180D_pct":459.08,"MAE_30D_pct":-12.25,"MAE_90D_pct":-12.25,"MAE_180D_pct":-12.25,"peak_date":"2023-07-26","peak_price":194000,"drawdown_after_peak_pct":-43.71,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"trigger_outcome_label":"high_mfe_high_mae_event_risk","current_profile_verdict":"current_profile_4B_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C16_GEUMYANG_001570_20230221","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"evidence_url_pending":true,"source_proxy_only":true}
{"row_type":"trigger","trigger_id":"TR_C16_UNION_S2_20230217","case_id":"C16_R4L71_UNION_000910_20230217","symbol":"000910","company_name":"유니온","round":"R4","loop":"71","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C16_STRATEGIC_RESOURCE_POLICY_SUPPLY","fine_archetype_id":"RARE_EARTH_POLICY_EVENT_PREMIUM","loop_objective":"counterexample_mining","trigger_type":"Stage2","trigger_date":"2023-02-17","entry_date":"2023-02-17","entry_price":6280,"evidence_available_at_that_date":"rare-earth policy event premium visible before entry","evidence_source":"public-news-source proxy; exact URL pending","stage2_evidence_fields":["public_event_or_disclosure","policy_or_regulatory_optionality","relative_strength"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["positioning_overheat","price_only_local_peak"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/000/000910/2023.csv","profile_path":"atlas/symbol_profiles/000/000910.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":15.76,"MFE_90D_pct":38.69,"MFE_180D_pct":38.69,"MAE_30D_pct":-20.62,"MAE_90D_pct":-20.62,"MAE_180D_pct":-25.16,"peak_date":"2023-04-06","peak_price":8710,"drawdown_after_peak_pct":-37.54,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"trigger_outcome_label":"event_premium_fade","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C16_UNION_000910_20230217","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"evidence_url_pending":true,"source_proxy_only":true}
{"row_type":"trigger","trigger_id":"TR_C16_KDINV_S2_20221020","case_id":"C16_R4L71_KDINV_012320_20221020","symbol":"012320","company_name":"경동인베스트","round":"R4","loop":"71","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C16_STRATEGIC_RESOURCE_POLICY_SUPPLY","fine_archetype_id":"DOMESTIC_TITANIUM_RESOURCE_EVENT_PREMIUM","loop_objective":"counterexample_mining|4B_non_price_requirement_stress_test","trigger_type":"Stage2","trigger_date":"2022-10-20","entry_date":"2022-10-20","entry_price":37550,"evidence_available_at_that_date":"domestic titanium/resource discovery narrative visible before entry","evidence_source":"public-news-source proxy; exact URL pending","stage2_evidence_fields":["public_event_or_disclosure","policy_or_regulatory_optionality","relative_strength"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["valuation_blowoff","positioning_overheat","price_only_local_peak"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/012/012320/2022.csv","profile_path":"atlas/symbol_profiles/012/012320.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":272.84,"MFE_90D_pct":272.84,"MFE_180D_pct":272.84,"MAE_30D_pct":-23.57,"MAE_90D_pct":-23.57,"MAE_180D_pct":-23.57,"peak_date":"2022-11-16","peak_price":140000,"drawdown_after_peak_pct":-60.29,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"trigger_outcome_label":"price_blowoff_then_drawdown","current_profile_verdict":"current_profile_4B_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C16_KDINV_012320_20221020","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"evidence_url_pending":true,"source_proxy_only":true}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C16_R4L71_POSCO_005490_20230410","trigger_id":"TR_C16_POSCO_S2A_20230410","symbol":"005490","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C16_STRATEGIC_RESOURCE_POLICY_SUPPLY","raw_component_scores_before":{"contract_score":35,"backlog_visibility_score":45,"margin_bridge_score":35,"revision_score":55,"relative_strength_score":65,"customer_quality_score":45,"policy_or_regulatory_score":55,"valuation_repricing_score":50,"execution_risk_score":25,"legal_or_contract_risk_score":10,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":72,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"contract_score":45,"backlog_visibility_score":55,"margin_bridge_score":45,"revision_score":60,"relative_strength_score":65,"customer_quality_score":55,"policy_or_regulatory_score":60,"valuation_repricing_score":50,"execution_risk_score":20,"legal_or_contract_risk_score":10,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":75,"stage_label_after":"Stage2-Actionable","changed_components":["margin_bridge_score","customer_quality_score"],"component_delta_explanation":"C16 positive should be driven by conversion evidence, not resource keyword alone.","MFE_90D_pct":91.72,"MAE_90D_pct":-10.66,"score_return_alignment_label":"aligned","current_profile_verdict":"current_profile_correct"}
{"row_type":"score_simulation","profile_id":"C16_shadow_bridge_guard","case_id":"C16_R4L71_UNION_000910_20230217","trigger_id":"TR_C16_UNION_S2_20230217","symbol":"000910","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C16_STRATEGIC_RESOURCE_POLICY_SUPPLY","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":10,"relative_strength_score":60,"customer_quality_score":0,"policy_or_regulatory_score":80,"valuation_repricing_score":30,"execution_risk_score":45,"legal_or_contract_risk_score":20,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":65,"stage_label_before":"Stage2","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":10,"relative_strength_score":40,"customer_quality_score":0,"policy_or_regulatory_score":50,"valuation_repricing_score":20,"execution_risk_score":55,"legal_or_contract_risk_score":20,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":56,"stage_label_after":"Stage1/Stage2-watch","changed_components":["policy_or_regulatory_score","relative_strength_score"],"component_delta_explanation":"Policy/resource keyword should not become Stage2 bonus unless non-price bridge exists.","MFE_90D_pct":38.69,"MAE_90D_pct":-20.62,"score_return_alignment_label":"weak_alignment","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"residual_contribution","round":"R4","loop":"71","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C16_STRATEGIC_RESOURCE_POLICY_SUPPLY","new_independent_case_count":4,"reused_case_count":0,"new_symbol_count":4,"new_trigger_family_count":3,"tested_existing_calibrated_axes":["stage2_actionable_evidence_bonus","price_only_blowoff_blocks_positive_stage","full_4b_requires_non_price_evidence"],"residual_error_types_found":["resource_keyword_false_positive","event_premium_4B_too_late","high_MAE_optional_resource_success"],"loop_contribution_label":"counterexample_added","do_not_propose_new_weight_delta":true}
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
completed_round = R4
completed_loop = 71
next_round = R5
next_loop = 71
round_schedule_status = valid
round_sector_consistency = pass
```

## 28. Source Notes

- `docs/core/V12_Research_No_Repeat_Index.md` was used as duplicate/coverage guard.
- Stock-Web manifest max_date used: 2026-02-20.
- Exact historical evidence URLs remain pending; this run is intentionally marked shadow-only / no new production weight delta.

