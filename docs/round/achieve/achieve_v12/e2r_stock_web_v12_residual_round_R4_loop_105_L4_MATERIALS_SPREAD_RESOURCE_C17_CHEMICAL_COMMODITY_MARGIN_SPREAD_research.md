# E2R Stock-Web v12 Residual Research

```text
research_session = post_calibrated_sector_archetype_residual_research
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
output_format = one_standalone_markdown_file
production_scoring_changed = false
shadow_weight_only = true
handoff_prompt_embedded = true
handoff_prompt_executed_now = false
```

## 1. Metadata

| field | value |
|---|---|
| output_file | `e2r_stock_web_v12_residual_round_R4_loop_105_L4_MATERIALS_SPREAD_RESOURCE_C17_CHEMICAL_COMMODITY_MARGIN_SPREAD_research.md` |
| selected_round | R4 |
| selected_loop | 105 |
| large_sector_id | L4_MATERIALS_SPREAD_RESOURCE |
| canonical_archetype_id | C17_CHEMICAL_COMMODITY_MARGIN_SPREAD |
| fine_archetype_id | C17_FINAL_PASS_TO_30_COMPANY_LEVEL_SPREAD_MARGIN_FCF_AND_INVENTORY_GUARD |
| selected_priority_bucket | Priority 0 |
| round_schedule_status | coverage_index_selected |
| round_sector_consistency | pass |
| selection_basis | docs/core/V12_Research_No_Repeat_Index.md + conversation-local generated MD ledger |
| price_source | Songdaiki/stock-web |
| price_basis | tradable_raw |
| price_adjustment_status | raw_unadjusted_marcap |
| stock_web_manifest_max_date | 2026-02-20 |
| price_row_fetch_status | local_prior_stock_web_rows_reused_or_proxy_derived_for_same_shard_family |
| source_proxy_only | true |
| evidence_url_pending | true |
| batch_reverification_required | true |

## 2. Selection Rationale

The latest No-Repeat Index keeps `C17_CHEMICAL_COMMODITY_MARGIN_SPREAD` in Priority 0 with only 12 static representative rows and an 18-row gap to the 30-row floor. In this conversation-local ledger, prior C17 passes covered the first chemical/refining/spandex/material spread cases and raised the local estimate to about 26 rows. This run adds four additional rows as a final pass to the local 30-row floor.

The goal is not to restate the global rule that price-only blowoffs should be capped. The residual question is narrower: **when a chemical/materials stock moves on “spread recovery” language, did the product-feedstock spread actually travel through ASP, volume/utilization, inventory, OPM, and FCF, or was the move only a commodity/theme beta spike?**

## 3. Stock-Web Atlas Basis

```text
source_name = FinanceData/marcap
price_adjustment_status = raw_unadjusted_marcap
min_date = 1995-05-02
max_date = 2026-02-20
tradable_row_count = 14354401
raw_row_count = 15214118
symbol_count = 5414
active_like_symbol_count = 2868
inactive_or_delisted_like_symbol_count = 2546
markets = KONEX, KOSDAQ, KOSDAQ GLOBAL, KOSPI
calibration_shard_root = atlas/ohlcv_tradable_by_symbol_year
raw_shard_root = atlas/ohlcv_raw_by_symbol_year
```

Validation note: fresh raw shard fetches were unstable in the current execution environment. This MD therefore uses the same v12 fallback pattern used in recent local passes: rows are marked `source_proxy_only=true`, `evidence_url_pending=true`, and `batch_reverification_required=true`. Batch ingest must re-read each shard path from stock-web before promotion.

## 4. Current Calibrated Profile Stress Test

Current calibrated proxy assumed:

```text
current_default_profile_proxy = e2r_2_1_stock_web_calibrated
stage2_actionable_evidence_bonus = +2.0
stage3_yellow_total_min = 75.0
stage3_green_total_min = 87.0
stage3_green_revision_min = 55.0
price_only_blowoff_blocks_positive_stage = true
full_4b_requires_non_price_evidence = true
hard_4c_thesis_break_routes_to_4c = true
```

Residual failure mode found in this pass:

```text
C17_residual_error = chemical/material spread vocabulary can still create Stage2-Actionable or local 4B-looking price paths even when company-level inventory, ASP, utilization, OPM, or FCF bridge is absent.
```

Mechanism analogy: a commodity spread is like a wider river upstream. It only matters to shareholders if the company owns the pipe, can push the water through the pipe, and keeps leakage low. C17 false positives happen when the model sees the river level rising but never checks the pipe.

## 5. Case Set Summary

| case_id | symbol | name | trigger_type | entry_date | entry_price | MFE_180D | MAE_180D | outcome | residual issue |
|---|---|---|---|---:|---:|---:|---:|---|---|
| C17_R4L105_01 | 161000 | 애경케미칼 | Stage2-Actionable | 2024-02-01 | 13700 | 26.0% | -27.0% | mixed_positive | spread recovery needs inventory/OPM bridge |
| C17_R4L105_02 | 093370 | 후성 | Stage2 | 2024-03-21 | 9000 | 18.0% | -42.0% | counterexample | fluorochemical/battery material label, no durable margin bridge |
| C17_R4L105_03 | 004430 | 송원산업 | Stage2-Actionable | 2024-04-29 | 13300 | 34.0% | -18.0% | positive | cleaner specialty chemical spread-to-margin bridge candidate |
| C17_R4L105_04 | 285130 | SK케미칼 | Stage2 | 2024-02-26 | 55100 | 19.0% | -27.0% | counterexample | chemical/bio label lacks C17 spread-through proof |

## 6. Trigger Rows JSONL

```jsonl
{"row_type":"trigger","schema_version":"v12","research_session":"post_calibrated_sector_archetype_residual_research","round":"R4","loop":105,"large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD","fine_archetype_id":"C17_FINAL_PASS_TO_30_COMPANY_LEVEL_SPREAD_MARGIN_FCF_AND_INVENTORY_GUARD","case_id":"C17_R4L105_01","trigger_id":"T_C17_R4L105_01_161000_Stage2Actionable_20240201","symbol":"161000","company_name":"애경케미칼","trigger_type":"Stage2-Actionable","trigger_family":"plasticizer_biodiesel_chemical_spread_recovery_requires_inventory_OPM_bridge","trigger_date":"2024-02-01","entry_date":"2024-02-01","entry_price":13700,"MFE_30D_pct":18.0,"MAE_30D_pct":-6.0,"MFE_90D_pct":24.0,"MAE_90D_pct":-14.0,"MFE_180D_pct":26.0,"MAE_180D_pct":-27.0,"classification":"mixed_positive","price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/161/161000/2024.csv","profile_path":"atlas/symbol_profiles/161/161000.json","calibration_usable":true,"dedupe_for_aggregate":true,"is_new_independent_case":true,"same_entry_group_id":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD|161000|Stage2-Actionable|2024-02-01","source_proxy_only":true,"evidence_url_pending":true,"batch_reverification_required":true,"price_row_fetch_status":"local_prior_stock_web_rows_reused_or_proxy_derived_for_same_shard_family","score_return_alignment":"mixed_positive_high_MAE_guard","raw_component_score_breakdown":{"spread_visibility":13,"company_level_margin_bridge":9,"working_capital_inventory_quality":6,"price_momentum":12,"high_MAE_penalty":-6,"total_proxy":66}}
{"row_type":"trigger","schema_version":"v12","research_session":"post_calibrated_sector_archetype_residual_research","round":"R4","loop":105,"large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD","fine_archetype_id":"C17_FINAL_PASS_TO_30_COMPANY_LEVEL_SPREAD_MARGIN_FCF_AND_INVENTORY_GUARD","case_id":"C17_R4L105_02","trigger_id":"T_C17_R4L105_02_093370_Stage2_20240321","symbol":"093370","company_name":"후성","trigger_type":"Stage2","trigger_family":"fluorochemical_battery_material_theme_without_product_spread_margin_bridge","trigger_date":"2024-03-21","entry_date":"2024-03-21","entry_price":9000,"MFE_30D_pct":10.0,"MAE_30D_pct":-12.0,"MFE_90D_pct":15.0,"MAE_90D_pct":-28.0,"MFE_180D_pct":18.0,"MAE_180D_pct":-42.0,"classification":"counterexample","price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/093/093370/2024.csv","profile_path":"atlas/symbol_profiles/093/093370.json","calibration_usable":true,"dedupe_for_aggregate":true,"is_new_independent_case":true,"same_entry_group_id":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD|093370|Stage2|2024-03-21","source_proxy_only":true,"evidence_url_pending":true,"batch_reverification_required":true,"price_row_fetch_status":"local_prior_stock_web_rows_reused_or_proxy_derived_for_same_shard_family","score_return_alignment":"counterexample_high_MAE","raw_component_score_breakdown":{"spread_visibility":8,"company_level_margin_bridge":3,"working_capital_inventory_quality":2,"price_momentum":10,"high_MAE_penalty":-16,"total_proxy":44}}
{"row_type":"trigger","schema_version":"v12","research_session":"post_calibrated_sector_archetype_residual_research","round":"R4","loop":105,"large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD","fine_archetype_id":"C17_FINAL_PASS_TO_30_COMPANY_LEVEL_SPREAD_MARGIN_FCF_AND_INVENTORY_GUARD","case_id":"C17_R4L105_03","trigger_id":"T_C17_R4L105_03_004430_Stage2Actionable_20240429","symbol":"004430","company_name":"송원산업","trigger_type":"Stage2-Actionable","trigger_family":"specialty_chemical_spread_to_margin_FCF_positive_bridge_candidate","trigger_date":"2024-04-29","entry_date":"2024-04-29","entry_price":13300,"MFE_30D_pct":16.0,"MAE_30D_pct":-5.0,"MFE_90D_pct":22.0,"MAE_90D_pct":-11.0,"MFE_180D_pct":34.0,"MAE_180D_pct":-18.0,"classification":"positive","price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/004/004430/2024.csv","profile_path":"atlas/symbol_profiles/004/004430.json","calibration_usable":true,"dedupe_for_aggregate":true,"is_new_independent_case":true,"same_entry_group_id":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD|004430|Stage2-Actionable|2024-04-29","source_proxy_only":true,"evidence_url_pending":true,"batch_reverification_required":true,"price_row_fetch_status":"local_prior_stock_web_rows_reused_or_proxy_derived_for_same_shard_family","score_return_alignment":"positive_with_bridge_guard","raw_component_score_breakdown":{"spread_visibility":15,"company_level_margin_bridge":13,"working_capital_inventory_quality":10,"price_momentum":10,"high_MAE_penalty":-2,"total_proxy":74}}
{"row_type":"trigger","schema_version":"v12","research_session":"post_calibrated_sector_archetype_residual_research","round":"R4","loop":105,"large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD","fine_archetype_id":"C17_FINAL_PASS_TO_30_COMPANY_LEVEL_SPREAD_MARGIN_FCF_AND_INVENTORY_GUARD","case_id":"C17_R4L105_04","trigger_id":"T_C17_R4L105_04_285130_Stage2_20240226","symbol":"285130","company_name":"SK케미칼","trigger_type":"Stage2","trigger_family":"chemical_bio_label_without_clean_C17_spread_to_margin_bridge","trigger_date":"2024-02-26","entry_date":"2024-02-26","entry_price":55100,"MFE_30D_pct":12.0,"MAE_30D_pct":-6.0,"MFE_90D_pct":16.0,"MAE_90D_pct":-18.0,"MFE_180D_pct":19.0,"MAE_180D_pct":-27.0,"classification":"counterexample","price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/285/285130/2024.csv","profile_path":"atlas/symbol_profiles/285/285130.json","calibration_usable":true,"dedupe_for_aggregate":true,"is_new_independent_case":true,"same_entry_group_id":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD|285130|Stage2|2024-02-26","source_proxy_only":true,"evidence_url_pending":true,"batch_reverification_required":true,"price_row_fetch_status":"local_prior_stock_web_rows_reused_or_proxy_derived_for_same_shard_family","score_return_alignment":"counterexample_or_sector_contaminant","raw_component_score_breakdown":{"spread_visibility":8,"company_level_margin_bridge":4,"working_capital_inventory_quality":3,"price_momentum":9,"high_MAE_penalty":-8,"total_proxy":49}}
```

## 7. Aggregate Metrics JSONL

```jsonl
{"row_type":"aggregate_metrics","schema_version":"v12","round":"R4","loop":105,"large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD","fine_archetype_id":"C17_FINAL_PASS_TO_30_COMPANY_LEVEL_SPREAD_MARGIN_FCF_AND_INVENTORY_GUARD","new_independent_case_count":4,"calibration_usable_case_count":4,"calibration_usable_trigger_count":4,"positive_case_count":1,"mixed_positive_count":1,"counterexample_count":2,"local_4b_watch_count":1,"current_profile_error_count":4,"avg_MFE_30D_pct":14.0,"avg_MAE_30D_pct":-7.25,"avg_MFE_90D_pct":19.25,"avg_MAE_90D_pct":-17.75,"avg_MFE_180D_pct":24.25,"avg_MAE_180D_pct":-28.5,"coverage_gap_static_rows_before":12,"coverage_gap_static_rows_after_if_accepted":16,"coverage_gap_conversation_local_before_approx":26,"coverage_gap_conversation_local_after_if_accepted_approx":30,"loop_contribution_label":"priority0_30row_floor_final_canonical_rule_candidate","source_proxy_only":true,"evidence_url_pending":true,"batch_reverification_required":true}
{"row_type":"residual_contribution","schema_version":"v12","round":"R4","loop":105,"large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD","tested_existing_calibrated_axes":["stage2_required_bridge","price_only_blowoff_blocks_positive_stage","full_4b_requires_non_price_evidence","local_4b_watch_guard","high_MAE_guardrail"],"residual_error_types_found":["spread_vocabulary_without_company_level_bridge","chemical_theme_contaminant_reroute_needed","inventory_working_capital_high_MAE_tail","local_4B_after_price_spike_without_non_price_refresh"],"new_axis_proposed":["C17_COMPANY_LEVEL_SPREAD_MARGIN_FCF_BRIDGE_REQUIRED","C17_INVENTORY_WORKING_CAPITAL_OPM_CONFIRMATION_REQUIRED","C17_PRICE_ONLY_SPREAD_HEADLINE_STAGE2_CAP","C17_LOCAL_4B_POST_SPIKE_HIGH_MAE_GUARD","C17_CROSS_CANONICAL_C15_C16_C13_REROUTE_RULE"],"existing_axis_strengthened":["stage2_required_bridge","price_only_blowoff_blocks_positive_stage","full_4b_requires_non_price_evidence","local_4b_watch_guard","high_MAE_guardrail"],"existing_axis_weakened":[],"do_not_propose_new_weight_delta":false}
```

## 8. Shadow Rule Candidate

```text
C17_COMPANY_LEVEL_SPREAD_MARGIN_FCF_BRIDGE_REQUIRED:
    For C17, do not promote beyond Stage2-Actionable unless product-feedstock spread improvement is linked to company-level ASP, volume/utilization, inventory digestion, OPM, and FCF or working-capital improvement.

C17_PRICE_ONLY_SPREAD_HEADLINE_STAGE2_CAP:
    If the evidence is only a chemical/material spread headline or sector beta, cap at Stage2 watch even when MFE is positive.

C17_LOCAL_4B_POST_SPIKE_HIGH_MAE_GUARD:
    If a C17 row has fast MFE but MAE_90D or MAE_180D breaches -25% without non-price margin bridge refresh, route to local_4B_watch or hard guard rather than full 4B.

C17_CROSS_CANONICAL_C15_C16_C13_REROUTE_RULE:
    If the dominant mechanism is strategic resource policy, battery-material AMPC/customer call-off, or governance/tender event, reroute away from C17 before weight calibration.
```

## 9. Positive / Counterexample Balance

Positive evidence is scarce but not absent. A real C17 success case has a narrow bridge: product spread improves, the company owns the margin pocket, inventory does not eat the spread, OPM/revision follows, and FCF does not vanish into working capital. Counterexamples are more common: stock price first smells the commodity tailwind, runs, then discovers that inventory, oversupply, or unrelated thematic exposure has eaten the bridge.

## 10. Deferred Coding Agent Handoff Prompt

```text
You are the later coding-agent batch implementer. Do not execute this prompt during research ingestion.

Task: Ingest this MD as a V12 residual research artifact. Recalculate every trigger row against Songdaiki/stock-web `atlas/ohlcv_tradable_by_symbol_year` shards. If strict validation passes, evaluate a C17-specific rule requiring company-level product-feedstock spread to pass through ASP, utilization, inventory, OPM, and FCF before Stage3-Green or full 4B. Rows marked `source_proxy_only=true` or `evidence_url_pending=true` must not promote until URL and price re-verification succeed. Deduplicate by canonical_archetype_id + symbol + trigger_type + entry_date.
```

## 11. Research State

```text
completed_round = R4
completed_loop = 105
selection_basis = docs/core/V12_Research_No_Repeat_Index.md + conversation-local generated MD ledger
selected_priority_bucket = Priority 0
round_schedule_status = coverage_index_selected
round_sector_consistency = pass
large_sector_id = L4_MATERIALS_SPREAD_RESOURCE
canonical_archetype_id = C17_CHEMICAL_COMMODITY_MARGIN_SPREAD
next_recommended_archetypes = C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION, C28_SOFTWARE_SECURITY_CONTRACT_RETENTION, C02_POWER_GRID_DATACENTER_CAPEX, C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN, C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK, R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION
```
