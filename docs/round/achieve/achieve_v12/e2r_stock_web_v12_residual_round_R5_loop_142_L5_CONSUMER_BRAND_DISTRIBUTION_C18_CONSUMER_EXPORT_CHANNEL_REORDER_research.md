# E2R Stock-Web v12 Residual Research — R5 Loop 142 — C18 Consumer Export Channel Reorder

```text
schema_family = v12_sector_archetype_residual
research_session = post_calibrated_sector_archetype_residual_research
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
selected_round = R5
selected_loop = 142
large_sector_id = L5_CONSUMER_BRAND_DISTRIBUTION
canonical_archetype_id = C18_CONSUMER_EXPORT_CHANNEL_REORDER
fine_archetype_id = GLOBAL_K_SNACK_AND_ICECREAM_EXPORT_CHANNEL_REORDER_VS_GLOBAL_BRAND_FOOTPRINT_HIGH_MAE
selection_basis = docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket = Priority 0
round_schedule_status = coverage_index_selected
round_sector_consistency = pass
price_source = Songdaiki/stock-web
price_basis = tradable_raw
price_adjustment_status = raw_unadjusted_marcap
stock_web_manifest_max_date = 2026-02-20
production_scoring_changed = false
shadow_weight_only = true
stock_agent_code_access_allowed = false
stock_agent_code_patch_allowed = false
```

## 1. Selection and no-repeat rationale

The repository No-Repeat Index still marks `C18_CONSUMER_EXPORT_CHANNEL_REORDER` as a Priority 0 low-coverage archetype with 3 rows and 3 symbols. The prior local C18 pass in this session used `003230`, `004370`, and `097950`. This loop avoids those same symbol/entry combinations and adds:

| symbol | company | newness | role |
|---|---|---|---|
| 005180 | 빙그레 | new visible C18 symbol | export-theme high-MFE/high-MAE guard |
| 280360 | 롯데웰푸드 | new visible C18 symbol | global snack channel spike, durable-rerating counterexample |
| 271560 | 오리온 | new visible C18 symbol | diversified overseas-base positive control |

This is not a live stock scan and not a trading recommendation. It is a historical calibration handoff artifact.

## 2. Price-source validation

| field | value |
|---|---|
| price_atlas_repo | Songdaiki/stock-web |
| source_basis | FinanceData/marcap transformed into assistant-readable symbol-year CSV shards |
| calibration_shard_root | atlas/ohlcv_tradable_by_symbol_year |
| price_basis | tradable_raw |
| price_adjustment_status | raw_unadjusted_marcap |
| stock_web_manifest_max_date | 2026-02-20 |

All selected windows avoid the corporate-action candidate dates in each symbol profile. The visible profile caveats are old and outside the selected 2024~2025 windows.

## 3. Case table

| case_id | symbol | company | trigger_type | entry_date | entry_price | 30D MFE/MAE | 90D MFE/MAE | 180D MFE/MAE | verdict |
|---|---:|---|---|---:|---:|---:|---:|---:|---|
| C18_R5_L142_005180_MELONA_BANANA_MILK_EXPORT_THEME | 005180 | 빙그레 | Stage2-Actionable | 2024-05-17 | 88,300 | +34.09% / -9.29% | +34.09% / -16.65% | +34.09% / -31.71% | export theme worked, but high-MAE local 4B watch needed |
| C18_R5_L142_280360_PEPERO_GLOBAL_CHANNEL_SPIKE | 280360 | 롯데웰푸드 | Stage2-Actionable | 2024-05-17 | 142,000 | +46.83% / -2.32% | +46.83% / -10.77% | +46.83% / -27.46% | durable Green false-positive if no reorder/OPM bridge |
| C18_R5_L142_271560_ORION_OVERSEAS_STABLE_REORDER | 271560 | 오리온 | Stage2 | 2024-09-27 | 99,600 | +3.31% / -3.31% | +10.84% / -6.63% | +23.99% / -6.63% | slow, low-MAE positive control |

## 4. Evidence notes

### 005180 — Binggrae

`Melona` and `Banana Flavored Milk` provide a recognizable global-product proxy. The price path after 2024-05-17 shows a vertical export-theme move to 118,400 but then a full-window low near 60,300. This means C18 should not treat brand global availability as equivalent to repeat reorder plus OPM/revision bridge.

### 280360 — Lotte Wellfood

`Pepero` and Lotte Wellfood overseas footprint provide a global channel proxy. The 2024 path had a strong local MFE, but the later fall to 103,000 means a full Stage3/Green promotion would have been wrong without concrete repeat order, sell-through, and margin bridge.

### 271560 — Orion

Orion has a more diversified overseas production/market footprint. The path from 2024-09-27 was slower but cleaner: MFE expanded into 2025 while MAE stayed shallow. This prevents overblocking every C18 global-food exporter after the Binggrae/Lotte high-MAE examples.

## 5. Score-return alignment

| symbol | profile stress result | reason |
|---|---|---|
| 005180 | current_profile_4B_too_late | early MFE was good, but 180D MAE argues for earlier local 4B watch once vertical move lacks refreshed reorder/OPM proof |
| 280360 | current_profile_false_positive_if_promoted_beyond_stage2 | price spike was real but not durable; global product/channel label alone should not unlock Stage3/Green |
| 271560 | current_profile_correct | slow durable rerating with low MAE supports an escape hatch when overseas base is diversified and drawdown remains contained |

## 6. Proposed shadow rule candidate

```text
rule_id = C18_GLOBAL_BRAND_FOOTPRINT_REQUIRES_REORDER_SELLTHROUGH_OPM_BRIDGE

if canonical_archetype_id == C18_CONSUMER_EXPORT_CHANNEL_REORDER
and global_brand_or_export_footprint == true
and repeat_order_or_sellthrough_evidence == false
and OPM_or_revision_bridge == false:
    stage2_actionable_bonus = 0
    max_stage = Stage2-Watch
```

```text
if MFE_30D_pct >= +30
and MAE_180D_pct <= -25
and refreshed_reorder_or_OPM_bridge == false:
    local_4B_watch = true
    block_stage3_green = true
```

Escape hatch:

```text
if geographic_diversification == true
and MFE_180D_pct >= +20
and MAE_90D_pct > -10:
    do_not_hard_block_stage2 = true
    allow_stage2_actionable_if_non_price_bridge_is_plausible = true
```

## 7. JSONL trigger rows

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration"}
{"row_type": "coverage_matrix", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C18_CONSUMER_EXPORT_CHANNEL_REORDER", "repo_index_rows_before": 3, "local_session_added_rows_before_this_loop": 3, "this_loop_rows": 3, "visible_unique_symbol_added_this_loop": 3, "priority_bucket": "Priority 0", "coverage_note": "repo index still marks C18 as 3 rows; local session already added 003230/004370/097950 in loop 141, so loop 142 uses 005180/280360/271560."}
{"row_type": "case", "case_id": "C18_R5_L142_005180_MELONA_BANANA_MILK_EXPORT_THEME", "symbol": "005180", "company_name": "빙그레", "round": "R5", "loop": "142", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C18_CONSUMER_EXPORT_CHANNEL_REORDER", "fine_archetype_id": "GLOBAL_K_SNACK_AND_ICECREAM_EXPORT_CHANNEL_REORDER_VS_GLOBAL_BRAND_FOOTPRINT_HIGH_MAE", "case_type": "high_mfe_high_mae_guard", "positive_or_counterexample": "positive", "best_trigger": "C18_R5_L142_005180_T1", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "high_mfe_high_mae_guard_needed", "current_profile_verdict": "current_profile_4B_too_late", "price_source": "Songdaiki/stock-web"}
{"row_type": "case", "case_id": "C18_R5_L142_280360_PEPERO_GLOBAL_CHANNEL_SPIKE", "symbol": "280360", "company_name": "롯데웰푸드", "round": "R5", "loop": "142", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C18_CONSUMER_EXPORT_CHANNEL_REORDER", "fine_archetype_id": "GLOBAL_K_SNACK_AND_ICECREAM_EXPORT_CHANNEL_REORDER_VS_GLOBAL_BRAND_FOOTPRINT_HIGH_MAE", "case_type": "high_mfe_high_mae_guard", "positive_or_counterexample": "counterexample", "best_trigger": "C18_R5_L142_280360_T1", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "high_mfe_high_mae_guard_needed", "current_profile_verdict": "current_profile_false_positive_if_promoted_beyond_stage2", "price_source": "Songdaiki/stock-web"}
{"row_type": "case", "case_id": "C18_R5_L142_271560_ORION_OVERSEAS_STABLE_REORDER", "symbol": "271560", "company_name": "오리온", "round": "R5", "loop": "142", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C18_CONSUMER_EXPORT_CHANNEL_REORDER", "fine_archetype_id": "GLOBAL_K_SNACK_AND_ICECREAM_EXPORT_CHANNEL_REORDER_VS_GLOBAL_BRAND_FOOTPRINT_HIGH_MAE", "case_type": "slow_durable_positive_control", "positive_or_counterexample": "positive", "best_trigger": "C18_R5_L142_271560_T1", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "durable_low_mae_positive", "current_profile_verdict": "current_profile_correct", "price_source": "Songdaiki/stock-web"}
{"row_type": "trigger", "trigger_id": "C18_R5_L142_005180_T1", "case_id": "C18_R5_L142_005180_MELONA_BANANA_MILK_EXPORT_THEME", "symbol": "005180", "company_name": "빙그레", "round": "R5", "loop": "142", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C18_CONSUMER_EXPORT_CHANNEL_REORDER", "fine_archetype_id": "GLOBAL_K_SNACK_AND_ICECREAM_EXPORT_CHANNEL_REORDER_VS_GLOBAL_BRAND_FOOTPRINT_HIGH_MAE", "sector": "consumer/food/export", "primary_archetype": "consumer_export_channel_reorder", "loop_objective": "coverage_gap_fill|counterexample_mining|stage2_actionable_bonus_stress_test|local_4b_watch_guard|canonical_archetype_compression", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-05-16", "evidence_available_at_that_date": "Binggrae export/global-brand proxy: Melona and Banana Flavored Milk are Binggrae products with overseas retail availability; price path shows export-theme MFE but later durability stress.", "evidence_source": "https://en.wikipedia.org/wiki/Melona|https://en.wikipedia.org/wiki/Banana_Flavored_Milk|https://en.wikipedia.org/wiki/Binggrae", "evidence_source_quality": "source_proxy_only", "stage2_evidence_fields": ["public_event_or_disclosure", "brand_or_product_export_route", "relative_strength"], "stage3_evidence_fields": ["repeat_order_or_conversion_needs_confirmation"], "stage4b_evidence_fields": ["valuation_blowoff", "local_peak_after_vertical_mfe"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/005/005180/2024.csv|atlas/ohlcv_tradable_by_symbol_year/005/005180/2025.csv", "profile_path": "atlas/symbol_profiles/005/005180.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-05-17", "entry_price": 88300, "MFE_30D_pct": 34.09, "MFE_90D_pct": 34.09, "MFE_180D_pct": 34.09, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -9.29, "MAE_90D_pct": -16.65, "MAE_180D_pct": -31.71, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-06-11", "peak_price": 118400, "drawdown_after_peak_pct": -49.07, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 1.0, "four_b_full_window_peak_proximity": 1.0, "four_b_timing_verdict": "local_4B_watch_needed_after_vertical_export_theme_mfe", "four_b_evidence_type": ["valuation_blowoff", "local_peak_after_vertical_mfe"], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "global_icecream_beverage_export_theme_high_mfe_high_mae", "current_profile_verdict": "current_profile_4B_too_late", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "C18_R5_L142_005180_2024-05-17_88300", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "C18_R5_L142_280360_T1", "case_id": "C18_R5_L142_280360_PEPERO_GLOBAL_CHANNEL_SPIKE", "symbol": "280360", "company_name": "롯데웰푸드", "round": "R5", "loop": "142", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C18_CONSUMER_EXPORT_CHANNEL_REORDER", "fine_archetype_id": "GLOBAL_K_SNACK_AND_ICECREAM_EXPORT_CHANNEL_REORDER_VS_GLOBAL_BRAND_FOOTPRINT_HIGH_MAE", "sector": "consumer/food/export", "primary_archetype": "consumer_export_channel_reorder", "loop_objective": "coverage_gap_fill|counterexample_mining|stage2_actionable_bonus_stress_test|local_4b_watch_guard|canonical_archetype_compression", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-05-16", "evidence_available_at_that_date": "Lotte Wellfood/Pepero global channel proxy: Pepero has broad overseas distribution and Lotte Wellfood has overseas plants; price path had explosive MFE but later high-MAE durability failure.", "evidence_source": "https://en.wikipedia.org/wiki/Pepero|https://en.wikipedia.org/wiki/Lotte_Wellfood", "evidence_source_quality": "source_proxy_only", "stage2_evidence_fields": ["public_event_or_disclosure", "brand_or_product_export_route", "relative_strength"], "stage3_evidence_fields": ["repeat_order_or_conversion_needs_confirmation", "opm_bridge_needs_confirmation"], "stage4b_evidence_fields": ["valuation_blowoff", "local_peak_after_vertical_mfe"], "stage4c_evidence_fields": ["durability_failure_watch"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/280/280360/2024.csv|atlas/ohlcv_tradable_by_symbol_year/280/280360/2025.csv", "profile_path": "atlas/symbol_profiles/280/280360.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-05-17", "entry_price": 142000, "MFE_30D_pct": 46.83, "MFE_90D_pct": 46.83, "MFE_180D_pct": 46.83, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -2.32, "MAE_90D_pct": -10.77, "MAE_180D_pct": -27.46, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-06-18", "peak_price": 208500, "drawdown_after_peak_pct": -50.6, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 1.0, "four_b_full_window_peak_proximity": 1.0, "four_b_timing_verdict": "good_local_4B_after_vertical_channel_theme_spike", "four_b_evidence_type": ["valuation_blowoff", "local_peak_after_vertical_mfe", "margin_or_channel_followthrough_unconfirmed"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "pepero_global_channel_theme_high_mfe_but_180d_durability_failure", "current_profile_verdict": "current_profile_false_positive_if_promoted_beyond_stage2", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "C18_R5_L142_280360_2024-05-17_142000", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "C18_R5_L142_271560_T1", "case_id": "C18_R5_L142_271560_ORION_OVERSEAS_STABLE_REORDER", "symbol": "271560", "company_name": "오리온", "round": "R5", "loop": "142", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C18_CONSUMER_EXPORT_CHANNEL_REORDER", "fine_archetype_id": "GLOBAL_K_SNACK_AND_ICECREAM_EXPORT_CHANNEL_REORDER_VS_GLOBAL_BRAND_FOOTPRINT_HIGH_MAE", "sector": "consumer/food/export", "primary_archetype": "consumer_export_channel_reorder", "loop_objective": "coverage_gap_fill|counterexample_mining|stage2_actionable_bonus_stress_test|local_4b_watch_guard|canonical_archetype_compression", "trigger_type": "Stage2", "trigger_date": "2024-09-26", "evidence_available_at_that_date": "Orion overseas-market proxy: Orion has manufacturing in China, Russia, Vietnam, India and the US, with Choco Pie foothold in key overseas snack markets; price path showed slower but more durable MFE/MAE behavior.", "evidence_source": "https://en.wikipedia.org/wiki/Orion_Corporation_(South_Korean_company)|https://en.wikipedia.org/wiki/Choco_pie", "evidence_source_quality": "source_proxy_only", "stage2_evidence_fields": ["public_event_or_disclosure", "brand_or_product_export_route"], "stage3_evidence_fields": ["repeat_order_or_conversion", "geographic_diversification"], "stage4b_evidence_fields": [], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/271/271560/2024.csv|atlas/ohlcv_tradable_by_symbol_year/271/271560/2025.csv", "profile_path": "atlas/symbol_profiles/271/271560.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-09-27", "entry_price": 99600, "MFE_30D_pct": 3.31, "MFE_90D_pct": 10.84, "MFE_180D_pct": 23.99, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -3.31, "MAE_90D_pct": -6.63, "MAE_180D_pct": -6.63, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2025-03-19", "peak_price": 123500, "drawdown_after_peak_pct": -10.85, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "no_4B_needed_low_MAE_positive_control", "four_b_evidence_type": [], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "overseas_snack_footprint_slow_durable_rerating", "current_profile_verdict": "current_profile_correct", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "C18_R5_L142_271560_2024-09-27_99600", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "C18_R5_L142_005180_MELONA_BANANA_MILK_EXPORT_THEME", "trigger_id": "C18_R5_L142_005180_T1", "symbol": "005180", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C18_CONSUMER_EXPORT_CHANNEL_REORDER", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 1, "margin_bridge_score": 1, "revision_score": 2, "relative_strength_score": 8, "customer_quality_score": 3, "policy_or_regulatory_score": 0, "valuation_repricing_score": 5, "execution_risk_score": 2, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 72, "stage_label_before": "Stage2-Actionable", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 1, "margin_bridge_score": 0, "revision_score": 2, "relative_strength_score": 8, "customer_quality_score": 3, "policy_or_regulatory_score": 0, "valuation_repricing_score": 7, "execution_risk_score": 7, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 68, "stage_label_after": "Stage2-Actionable+local_4B_watch", "changed_components": ["margin_bridge_score", "execution_risk_score", "valuation_repricing_score"], "component_delta_explanation": "C18 needs repeat reorder, sell-through, and OPM/revision bridge before durable Stage3/Green; global brand footprint alone should route to watch after vertical MFE.", "MFE_90D_pct": 34.09, "MAE_90D_pct": -16.65, "score_return_alignment_label": "high_mfe_high_mae_guard_needed", "current_profile_verdict": "current_profile_4B_too_late"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "C18_R5_L142_280360_PEPERO_GLOBAL_CHANNEL_SPIKE", "trigger_id": "C18_R5_L142_280360_T1", "symbol": "280360", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C18_CONSUMER_EXPORT_CHANNEL_REORDER", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 1, "margin_bridge_score": 1, "revision_score": 2, "relative_strength_score": 8, "customer_quality_score": 3, "policy_or_regulatory_score": 0, "valuation_repricing_score": 5, "execution_risk_score": 2, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 72, "stage_label_before": "Stage2-Actionable", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 1, "margin_bridge_score": 0, "revision_score": 2, "relative_strength_score": 8, "customer_quality_score": 3, "policy_or_regulatory_score": 0, "valuation_repricing_score": 7, "execution_risk_score": 7, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 68, "stage_label_after": "Stage2-Actionable+local_4B_watch", "changed_components": ["margin_bridge_score", "execution_risk_score", "valuation_repricing_score"], "component_delta_explanation": "C18 needs repeat reorder, sell-through, and OPM/revision bridge before durable Stage3/Green; global brand footprint alone should route to watch after vertical MFE.", "MFE_90D_pct": 46.83, "MAE_90D_pct": -10.77, "score_return_alignment_label": "high_mfe_high_mae_guard_needed", "current_profile_verdict": "current_profile_false_positive_if_promoted_beyond_stage2"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "C18_R5_L142_271560_ORION_OVERSEAS_STABLE_REORDER", "trigger_id": "C18_R5_L142_271560_T1", "symbol": "271560", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C18_CONSUMER_EXPORT_CHANNEL_REORDER", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 1, "margin_bridge_score": 2, "revision_score": 3, "relative_strength_score": 4, "customer_quality_score": 3, "policy_or_regulatory_score": 0, "valuation_repricing_score": 2, "execution_risk_score": 2, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 68, "stage_label_before": "Stage2-Actionable", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 1, "margin_bridge_score": 2, "revision_score": 3, "relative_strength_score": 4, "customer_quality_score": 3, "policy_or_regulatory_score": 0, "valuation_repricing_score": 2, "execution_risk_score": 2, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 70, "stage_label_after": "Stage2-Actionable", "changed_components": ["margin_bridge_score", "execution_risk_score", "valuation_repricing_score"], "component_delta_explanation": "C18 needs repeat reorder, sell-through, and OPM/revision bridge before durable Stage3/Green; global brand footprint alone should route to watch after vertical MFE.", "MFE_90D_pct": 10.84, "MAE_90D_pct": -6.63, "score_return_alignment_label": "durable_low_mae_positive_control", "current_profile_verdict": "current_profile_correct"}
{"row_type": "shadow_weight", "shadow_id": "C18_R5_L142_STAGE2_BRIDGE_REQUIREMENT", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C18_CONSUMER_EXPORT_CHANNEL_REORDER", "rule_candidate": "C18_global_brand_footprint_requires_reorder_sellthrough_opm_bridge", "direction": "strengthen_guardrail", "proposed_delta": "+1 execution risk if no repeat-order/OPM bridge; cap Stage2 bonus", "supporting_triggers": "C18_R5_L142_005180_T1|C18_R5_L142_280360_T1", "do_not_apply_now": true}
{"row_type": "shadow_weight", "shadow_id": "C18_R5_L142_LOW_MAE_ESCAPE_HATCH", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C18_CONSUMER_EXPORT_CHANNEL_REORDER", "rule_candidate": "C18_geographic_diversification_low_MAE_escape_hatch", "direction": "prevent_overblock", "proposed_delta": "allow Stage2 if MFE_180D>=20 and MAE_90D>-10 with diversified overseas base", "supporting_triggers": "C18_R5_L142_271560_T1", "do_not_apply_now": true}
{"row_type": "residual_contribution", "round": "R5", "loop": "142", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C18_CONSUMER_EXPORT_CHANNEL_REORDER", "new_independent_case_count": 3, "reused_case_count": 0, "new_symbol_count": 3, "new_trigger_family_count": 3, "tested_existing_calibrated_axes": ["stage2_actionable_evidence_bonus", "stage2_required_bridge", "local_4b_watch_guard", "price_only_blowoff_blocks_positive_stage"], "residual_error_types_found": ["global_brand_footprint_without_reorder_margin_bridge", "vertical_export_theme_MFE_followed_by_high_MAE", "durable_low_MAE_geographic_diversification_escape_hatch"], "loop_contribution_label": "canonical_archetype_rule_candidate", "do_not_propose_new_weight_delta": false}
```

## 8. Residual contribution summary

```text
new_independent_case_count = 3
reused_case_count = 0
same_archetype_new_symbol_count_visible_index_basis = 3
same_archetype_new_trigger_family_count = 3
calibration_usable case 수 = 3
calibration_usable trigger 수 = 3
positive_case_count = 2
counterexample_count = 1
current_profile_error_count = 2
sector_specific_rule_candidate = false
canonical_archetype_rule_candidate = true
loop_contribution_label = canonical_archetype_rule_candidate
new_axis_proposed = null
existing_axis_strengthened = C18_global_brand_footprint_reorder_sellthrough_opm_bridge_requirement; C18_vertical_export_theme_local_4B_watch; C18_geographic_diversification_low_MAE_escape_hatch
existing_axis_weakened = null
do_not_propose_new_weight_delta = false
```

## 9. Deferred Coding Agent Handoff Prompt

```text
Do not execute this handoff during research generation.

Later coding agent task:
1. Ingest this MD as a v12 sector-archetype residual artifact.
2. Validate the JSONL trigger rows.
3. Confirm that all price fields are present: entry_date, entry_price, MFE_30D_pct, MFE_90D_pct, MFE_180D_pct, MAE_30D_pct, MAE_90D_pct, MAE_180D_pct.
4. Deduplicate by canonical_archetype_id + symbol + trigger_type + entry_date + entry_price + evidence family.
5. Treat C18_R5_L142_005180_T1 and C18_R5_L142_280360_T1 as local-4B/high-MAE guard candidates, not production weight changes.
6. Treat C18_R5_L142_271560_T1 as an escape-hatch positive control.
7. Do not patch production scoring unless multiple future C18 rows support the same pattern.
```

## 10. Completed state

```text
completed_round = R5
completed_loop = 142
selection_basis = docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket = Priority 0
next_recommended_archetypes = C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE, C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE, C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK, C31_POLICY_SUBSIDY_LEGISLATION_EVENT, C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP, C15_MATERIAL_SPREAD_SUPERCYCLE
round_schedule_status = coverage_index_selected
round_sector_consistency = pass
filename_pattern_pass = true
metadata_filename_consistency = pass
```
