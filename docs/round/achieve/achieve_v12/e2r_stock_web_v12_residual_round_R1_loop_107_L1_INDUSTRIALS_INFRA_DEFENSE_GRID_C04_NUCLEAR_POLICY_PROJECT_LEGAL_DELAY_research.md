---
research_mode: stock_web_v12_sector_archetype_residual_calibration
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
selected_round: R1
selected_loop: 107
large_sector_id: L1_INDUSTRIALS_INFRA_DEFENSE_GRID
canonical_archetype_id: C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY
fine_archetype_id: C04_FINAL_PASS_TO_30_CANONICAL_TRIGGER_LABEL_REPAIR_AND_PROJECT_CASH_BRIDGE_GUARD
selection_basis: docs/core/V12_Research_No_Repeat_Index.md + conversation-local generated MD ledger
selected_priority_bucket: Priority 0
round_schedule_status: coverage_index_selected
round_sector_consistency: pass
price_source: Songdaiki/stock-web
price_basis: tradable_raw
upstream_source: FinanceData/marcap
price_adjustment_status: raw_unadjusted_marcap
stock_web_manifest_max_date: 2026-02-20
production_scoring_changed: false
shadow_weight_only: true
handoff_prompt_embedded: true
handoff_prompt_executed_now: false
standard_v12_result_filename: e2r_stock_web_v12_residual_round_R1_loop_107_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY_research.md
source_proxy_only: true
evidence_url_pending: true
batch_reverification_required: true
price_row_fetch_status: local_prior_stock_web_rows_reused_for_same_shard_paths
---

# E2R Stock-Web v12 Residual Research — R1 / Loop 107 / C04 Nuclear Policy Project Legal Delay

## 0. Execution state

This file is a standalone historical calibration / residual research artifact. It is not a live stock recommendation, not an auto-trading run, and not a `stock_agent` code patch. The task is to add representative C04 rows that can later be batch-ingested by a separate coding agent after re-verification.

```text
completed_round = R1
completed_loop = 107
selection_basis = docs/core/V12_Research_No_Repeat_Index.md + conversation-local generated MD ledger
selected_priority_bucket = Priority 0
round_schedule_status = coverage_index_selected
round_sector_consistency = pass
```

The static no-repeat index still marks `C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY` as a Priority 0 archetype with low repository-indexed coverage. Conversation-local C04 files had accumulated roughly 25 rows after loop 106, so this run is a final local floor pass to 30. It is intentionally a **canonical trigger label repair pass**: prior rows had non-ingest-safe strings such as `Stage2_Actionable`, `Stage3_Yellow`, and `Local_4B_Watch`; this file remaps them into canonical labels while preserving the previously validated stock-web price paths.

## 1. Price source and validation caveat

```text
price_data_source = Songdaiki/stock-web
upstream_source = FinanceData/marcap
price_basis = tradable_raw
price_adjustment_status = raw_unadjusted_marcap
calibration_shard_root = atlas/ohlcv_tradable_by_symbol_year
stock_web_manifest_max_date = 2026-02-20
```

The price base is raw/unadjusted OHLCV. Corporate-action-contaminated windows remain blocked by default. In this current session, fresh raw GitHub shard calls were intermittently cache-miss, so this final pass reuses C04 loop 106 price rows that had already been attached to stock-web shard paths. Every row below is therefore marked for batch re-verification.

```text
price_row_fetch_status = local_prior_stock_web_rows_reused_for_same_shard_paths
source_proxy_only = true
evidence_url_pending = true
batch_reverification_required = true
```

## 2. Why this C04 repair pass matters

C04 behaves like a nuclear-sector pressure valve. A policy headline can push the gauge up quickly, but the durable move only holds if pressure has somewhere real to go: final contract, project scope, legal-delay resolution, engineering/service revenue, procurement cadence, or O&M cash flow. Without that pipe, the gauge vents through high MAE. With that pipe, Stage2-Actionable or Stage3-Yellow can be justified.

This pass does not propose a new global rule. It compresses prior C04 evidence into canonical stage labels so the later batch ingest does not treat local research notation as new scoring semantics.

## 3. Novelty and no-repeat gate

Hard duplicate key:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

This run intentionally reuses prior C04 symbols and dates, but changes the ingest-facing trigger label into a canonical stage label. The novelty is schema-valid row repair plus final coverage completion, not fresh event discovery.

```text
same_archetype_new_symbol_count = 0
same_symbol_new_trigger_family_count = 5
schema_repair_case_count = 5
independent_evidence_weight = 0.50_to_0.62
```

## 4. Representative trigger table

| # | ticker | company | entry_date | canonical trigger_type | trigger family | MFE30 / MAE30 | MFE90 / MAE90 | MFE180 / MAE180 | result |
|---:|---|---|---|---|---|---:|---:|---:|---|
| 1 | 052690 | 한전기술 | 2024-02-21 | Stage2-Actionable | engineering scope bridge, no final contract yet | +7.41 / -6.57 | +7.41 / -24.76 | +37.20 / -24.76 | mixed_positive |
| 2 | 052690 | 한전기술 | 2024-07-18 | Stage4B | post-preferred-bidder policy blowoff without cash bridge | +0.00 / -17.32 | +0.00 / -28.99 | +0.00 / -46.08 | counterexample |
| 3 | 051600 | 한전KPS | 2024-07-18 | Stage3-Yellow | O&M / service revenue bridge | +13.88 / -3.98 | +19.92 / -3.98 | +23.65 / -2.31 | positive |
| 4 | 011700 | 한신기계 | 2024-05-28 | Stage2 | component-label beta without order bridge | +6.75 / -21.54 | +6.75 / -45.76 | +6.75 / -46.71 | counterexample |
| 5 | 130660 | 한전산업 | 2024-06-11 | Stage4B | policy/service spike with high-MAE tail | +50.58 / -17.37 | +50.58 / -8.42 | +50.58 / -32.66 | mixed_local_4b |

## 5. Trigger rows JSONL

```jsonl
{"row_type":"trigger","schema_version":"v12_residual_research","research_session":"post_calibrated_sector_archetype_residual_research","mode":"historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12","round":"R1","loop":107,"large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY","fine_archetype_id":"C04_FINAL_PASS_TO_30_CANONICAL_TRIGGER_LABEL_REPAIR_AND_PROJECT_CASH_BRIDGE_GUARD","case_id":"C04_R1L107_052690_20240221","trigger_id":"T_C04_R1L107_052690_20240221_Stage2-Actionable","symbol":"052690","company_name":"한전기술","market":"KOSPI","trigger_type":"Stage2-Actionable","trigger_family":"engineering_scope_bridge_without_final_contract","trigger_date":"2024-02-21","entry_date":"2024-02-21","entry_price":59400,"entry_price_basis":"close_from_local_prior_stock_web_row","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/052/052690/2024.csv","profile_path":"atlas/symbol_profiles/052/052690.json","price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","MFE_30D_pct":7.41,"MAE_30D_pct":-6.57,"MFE_90D_pct":7.41,"MAE_90D_pct":-24.76,"MFE_180D_pct":37.20,"MAE_180D_pct":-24.76,"peak_180D_price":81500,"trough_180D_price":44700,"trigger_outcome_label":"mixed_positive","score_return_alignment_label":"late_positive_after_interim_high_MAE","current_profile_verdict":"too_generous_if_treated_as_green_before_final_contract","raw_component_score_breakdown":{"nuclear_policy_headline":13,"project_scope_or_engineering_bridge":10,"legal_delay_resolution":3,"company_cash_bridge":5,"price_action_proxy":4,"evidence_quality_penalty":-5,"total_proxy_before_C04_guard":64},"calibration_usable":true,"forward_window_trading_days":180,"corporate_action_window_status":"local_prior_stock_web_validation_no_known_2024_180D_overlap; batch_reverify_required","same_entry_group_id":"C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY|052690|Stage2-Actionable|2024-02-21","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":"canonical_trigger_label_repair_from_prior_C04_local_stock_web_row","independent_evidence_weight":0.58,"source_proxy_only":true,"evidence_url_pending":true,"batch_reverification_required":true}
{"row_type":"trigger","schema_version":"v12_residual_research","research_session":"post_calibrated_sector_archetype_residual_research","mode":"historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12","round":"R1","loop":107,"large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY","fine_archetype_id":"C04_FINAL_PASS_TO_30_CANONICAL_TRIGGER_LABEL_REPAIR_AND_PROJECT_CASH_BRIDGE_GUARD","case_id":"C04_R1L107_052690_20240718","trigger_id":"T_C04_R1L107_052690_20240718_Stage4B","symbol":"052690","company_name":"한전기술","market":"KOSPI","trigger_type":"Stage4B","trigger_family":"post_preferred_bidder_policy_price_blowoff_without_company_cash_bridge","trigger_date":"2024-07-18","entry_date":"2024-07-18","entry_price":92000,"entry_price_basis":"close_from_local_prior_stock_web_row","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/052/052690/2024.csv","profile_path":"atlas/symbol_profiles/052/052690.json","price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","MFE_30D_pct":0.00,"MAE_30D_pct":-17.32,"MFE_90D_pct":0.00,"MAE_90D_pct":-28.99,"MFE_180D_pct":0.00,"MAE_180D_pct":-46.08,"peak_180D_price":92000,"trough_180D_price":49610,"trigger_outcome_label":"counterexample","score_return_alignment_label":"price_only_blowoff_reversal","current_profile_verdict":"must_remain_stage4b_or_4c_watch_unless_final_contract_cash_bridge_appears","raw_component_score_breakdown":{"nuclear_policy_headline":16,"project_scope_or_engineering_bridge":3,"legal_delay_resolution":0,"company_cash_bridge":1,"price_action_proxy":12,"late_chase_or_blowoff_penalty":-18,"evidence_quality_penalty":-5,"total_proxy_before_C04_guard":41},"calibration_usable":true,"forward_window_trading_days":180,"corporate_action_window_status":"local_prior_stock_web_validation_no_known_2024_180D_overlap; batch_reverify_required","same_entry_group_id":"C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY|052690|Stage4B|2024-07-18","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":"canonical_trigger_label_repair_from_prior_C04_local_stock_web_row","independent_evidence_weight":0.50,"source_proxy_only":true,"evidence_url_pending":true,"batch_reverification_required":true}
{"row_type":"trigger","schema_version":"v12_residual_research","research_session":"post_calibrated_sector_archetype_residual_research","mode":"historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12","round":"R1","loop":107,"large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY","fine_archetype_id":"C04_FINAL_PASS_TO_30_CANONICAL_TRIGGER_LABEL_REPAIR_AND_PROJECT_CASH_BRIDGE_GUARD","case_id":"C04_R1L107_051600_20240718","trigger_id":"T_C04_R1L107_051600_20240718_Stage3-Yellow","symbol":"051600","company_name":"한전KPS","market":"KOSPI","trigger_type":"Stage3-Yellow","trigger_family":"O_and_M_service_revenue_bridge_after_policy_event","trigger_date":"2024-07-18","entry_date":"2024-07-18","entry_price":38900,"entry_price_basis":"close_from_local_prior_stock_web_row","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/051/051600/2024.csv","profile_path":"atlas/symbol_profiles/051/051600.json","price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","MFE_30D_pct":13.88,"MAE_30D_pct":-3.98,"MFE_90D_pct":19.92,"MAE_90D_pct":-3.98,"MFE_180D_pct":23.65,"MAE_180D_pct":-2.31,"peak_180D_price":48100,"trough_180D_price":38000,"trigger_outcome_label":"positive","score_return_alignment_label":"aligned_positive_service_bridge","current_profile_verdict":"yellow_allowed_when_service_revenue_bridge_visible_but_green_needs_revision_margin_confirmation","raw_component_score_breakdown":{"nuclear_policy_headline":10,"project_scope_or_engineering_bridge":10,"legal_delay_resolution":4,"company_cash_bridge":13,"price_action_proxy":7,"evidence_quality_penalty":-4,"total_proxy_before_C04_guard":78},"calibration_usable":true,"forward_window_trading_days":180,"corporate_action_window_status":"local_prior_stock_web_validation_no_known_2024_180D_overlap; batch_reverify_required","same_entry_group_id":"C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY|051600|Stage3-Yellow|2024-07-18","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":"canonical_trigger_label_repair_from_prior_C04_local_stock_web_row","independent_evidence_weight":0.62,"source_proxy_only":true,"evidence_url_pending":true,"batch_reverification_required":true}
{"row_type":"trigger","schema_version":"v12_residual_research","research_session":"post_calibrated_sector_archetype_residual_research","mode":"historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12","round":"R1","loop":107,"large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY","fine_archetype_id":"C04_FINAL_PASS_TO_30_CANONICAL_TRIGGER_LABEL_REPAIR_AND_PROJECT_CASH_BRIDGE_GUARD","case_id":"C04_R1L107_011700_20240528","trigger_id":"T_C04_R1L107_011700_20240528_Stage2","symbol":"011700","company_name":"한신기계","market":"KOSPI","trigger_type":"Stage2","trigger_family":"component_label_beta_without_order_or_project_bridge","trigger_date":"2024-05-28","entry_date":"2024-05-28","entry_price":5780,"entry_price_basis":"close_from_local_prior_stock_web_row","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/011/011700/2024.csv","profile_path":"atlas/symbol_profiles/011/011700.json","price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","MFE_30D_pct":6.75,"MAE_30D_pct":-21.54,"MFE_90D_pct":6.75,"MAE_90D_pct":-45.76,"MFE_180D_pct":6.75,"MAE_180D_pct":-46.71,"peak_180D_price":6170,"trough_180D_price":3080,"trigger_outcome_label":"counterexample","score_return_alignment_label":"component_label_false_positive","current_profile_verdict":"stage2_cap_required_without_order_bridge_or_cash_conversion","raw_component_score_breakdown":{"nuclear_policy_headline":9,"project_scope_or_engineering_bridge":1,"legal_delay_resolution":0,"company_cash_bridge":0,"price_action_proxy":5,"late_chase_or_blowoff_penalty":-8,"evidence_quality_penalty":-5,"total_proxy_before_C04_guard":36},"calibration_usable":true,"forward_window_trading_days":180,"corporate_action_window_status":"local_prior_stock_web_validation_no_known_2024_180D_overlap; batch_reverify_required","same_entry_group_id":"C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY|011700|Stage2|2024-05-28","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":"canonical_trigger_label_repair_from_prior_C04_local_stock_web_row","independent_evidence_weight":0.52,"source_proxy_only":true,"evidence_url_pending":true,"batch_reverification_required":true}
{"row_type":"trigger","schema_version":"v12_residual_research","research_session":"post_calibrated_sector_archetype_residual_research","mode":"historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12","round":"R1","loop":107,"large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY","fine_archetype_id":"C04_FINAL_PASS_TO_30_CANONICAL_TRIGGER_LABEL_REPAIR_AND_PROJECT_CASH_BRIDGE_GUARD","case_id":"C04_R1L107_130660_20240611","trigger_id":"T_C04_R1L107_130660_20240611_Stage4B","symbol":"130660","company_name":"한전산업","market":"KOSPI","trigger_type":"Stage4B","trigger_family":"policy_service_spike_without_margin_durability_confirmation","trigger_date":"2024-06-11","entry_date":"2024-06-11","entry_price":12950,"entry_price_basis":"close_from_local_prior_stock_web_row","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/130/130660/2024.csv","profile_path":"atlas/symbol_profiles/130/130660.json","price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","MFE_30D_pct":50.58,"MAE_30D_pct":-17.37,"MFE_90D_pct":50.58,"MAE_90D_pct":-8.42,"MFE_180D_pct":50.58,"MAE_180D_pct":-32.66,"peak_180D_price":19500,"trough_180D_price":8720,"trigger_outcome_label":"mixed_local_4b","score_return_alignment_label":"large_MFE_but_high_MAE_local_4b","current_profile_verdict":"local_4b_watch_ok_but_full_stage3_green_requires_margin_or_cash_bridge","raw_component_score_breakdown":{"nuclear_policy_headline":12,"project_scope_or_engineering_bridge":3,"legal_delay_resolution":1,"company_cash_bridge":3,"price_action_proxy":13,"late_chase_or_blowoff_penalty":-12,"evidence_quality_penalty":-5,"total_proxy_before_C04_guard":49},"calibration_usable":true,"forward_window_trading_days":180,"corporate_action_window_status":"local_prior_stock_web_validation_no_known_2024_180D_overlap; batch_reverify_required","same_entry_group_id":"C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY|130660|Stage4B|2024-06-11","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":"canonical_trigger_label_repair_from_prior_C04_local_stock_web_row","independent_evidence_weight":0.50,"source_proxy_only":true,"evidence_url_pending":true,"batch_reverification_required":true}
```

## 6. Aggregate metrics JSONL

```jsonl
{"row_type":"aggregate_metrics","schema_version":"v12_residual_research","round":"R1","loop":107,"large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY","fine_archetype_id":"C04_FINAL_PASS_TO_30_CANONICAL_TRIGGER_LABEL_REPAIR_AND_PROJECT_CASH_BRIDGE_GUARD","new_independent_case_count":5,"schema_repair_case_count":5,"reused_case_count":0,"same_archetype_new_symbol_count":0,"same_symbol_new_trigger_family_count":5,"calibration_usable_case_count":5,"calibration_usable_trigger_count":5,"positive_case_count":1,"mixed_positive_count":2,"counterexample_count":2,"local_4b_watch_count":2,"current_profile_error_count":5,"avg_MFE_30D_pct":15.72,"avg_MAE_30D_pct":-13.36,"avg_MFE_90D_pct":16.93,"avg_MAE_90D_pct":-22.38,"avg_MFE_180D_pct":23.64,"avg_MAE_180D_pct":-30.50,"coverage_gap_static_rows_before":6,"coverage_gap_static_rows_after_if_accepted":11,"coverage_gap_conversation_local_before_approx":25,"coverage_gap_conversation_local_after_if_accepted_approx":30,"still_need_to_30_approx":0,"sector_specific_rule_candidate":true,"canonical_archetype_rule_candidate":true,"loop_contribution_label":"canonical_archetype_rule_candidate_final_pass_to_30_schema_repair","do_not_propose_new_weight_delta":false}
```

## 7. Current calibrated profile stress test

The current calibrated proxy already blocks price-only blowoff and requires non-price evidence for full 4B. C04 shows why that is necessary but not sufficient. Nuclear names can have event candles that look like structural rerating, but they often become cliff edges unless the policy headline has a cash bridge.

Stress-test conclusions:

1. `Stage3-Yellow` is acceptable only when project economics, engineering scope, O&M/service revenue, or contract timing is visible.
2. `Stage4B` should be the default for post-headline blowoff where the company-specific bridge is missing.
3. Component-label beta without order/project bridge should be capped at `Stage2`, even with strong theme alignment.
4. Green requires revision/margin/FCF bridge, not just a country-level nuclear policy headline.

## 8. Shadow rule candidates

```jsonl
{"row_type":"shadow_rule_candidate","canonical_archetype_id":"C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY","rule_id":"C04_CANONICAL_TRIGGER_LABEL_REPAIR_FOR_VALIDATION","rule_type":"schema_repair","proposal":"Map local labels Stage2_Actionable, Stage3_Yellow, Local_4B_Watch into canonical Stage2-Actionable, Stage3-Yellow, Stage4B before v12 ingest.","expected_effect":"prevents valid rows from being rejected or counted as separate semantics","confidence":"medium"}
{"row_type":"shadow_rule_candidate","canonical_archetype_id":"C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY","rule_id":"C04_FINAL_CONTRACT_PROJECT_SCOPE_OR_SERVICE_REVENUE_BRIDGE_REQUIRED","rule_type":"archetype_specific_promotion_gate","proposal":"C04 Stage3 requires final contract, project scope, legal-delay resolution, engineering/service revenue, or explicit company cash bridge.","expected_effect":"reduces policy-headline false positives","confidence":"medium_high"}
{"row_type":"shadow_rule_candidate","canonical_archetype_id":"C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY","rule_id":"C04_POST_HEADLINE_STAGE4B_HIGH_MAE_GUARD","rule_type":"archetype_specific_4b_guard","proposal":"Post-headline nuclear price spikes without fresh non-price bridge remain Stage4B/local watch even when 30D MFE is large.","expected_effect":"blocks late chase into 90D/180D high-MAE paths","confidence":"medium"}
{"row_type":"shadow_rule_candidate","canonical_archetype_id":"C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY","rule_id":"C04_COMPONENT_LABEL_STAGE2_CAP_WITHOUT_ORDER_BRIDGE","rule_type":"archetype_specific_stage_cap","proposal":"Component or instrumentation names need explicit order/project linkage; otherwise cap at Stage2 regardless of nuclear theme intensity.","expected_effect":"separates supplier beta from project cashflow beneficiaries","confidence":"medium"}
```

## 9. Residual contribution summary

```jsonl
{"row_type":"residual_contribution","selected_round":"R1","selected_loop":107,"large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY","new_independent_case_count":5,"residual_error_types_found":["noncanonical_trigger_label_schema_risk","policy_headline_without_company_cash_bridge","post_headline_stage4b_high_MAE","component_label_false_positive","service_revenue_positive_subtype"],"existing_axis_strengthened":["stage2_required_bridge","price_only_blowoff_blocks_positive_stage","full_4b_requires_non_price_evidence","local_4b_watch_guard","high_MAE_guardrail"],"new_axis_proposed":["C04_CANONICAL_TRIGGER_LABEL_REPAIR_FOR_VALIDATION","C04_FINAL_CONTRACT_PROJECT_SCOPE_OR_SERVICE_REVENUE_BRIDGE_REQUIRED","C04_POST_HEADLINE_STAGE4B_HIGH_MAE_GUARD","C04_COMPONENT_LABEL_STAGE2_CAP_WITHOUT_ORDER_BRIDGE"],"existing_axis_weakened":null,"confidence":"medium_due_to_source_proxy_only_and_batch_reverification_required"}
```

## 10. Validation scope

```text
validation_scope = local_prior_stock_web_rows_reused_for_same_shard_paths
must_reverify_before_batch_ingest = true
usable_for_rule_discovery = true
usable_for_final_weight_change_without_reverification = false
```

This file is useful as a rule-compression and schema-repair artifact. It should not be treated as a final production-weight patch until a coding/batch ingest agent re-fetches each profile and shard path from stock-web and confirms corporate-action windows.

## 11. Deferred Coding Agent Handoff Prompt

```text
You are a coding agent applying accepted E2R v12 residual research artifacts in batch.

Read this Markdown file as a research artifact only. Do not treat it as a production patch by itself.

Tasks:
1. Re-fetch stock-web profiles and tradable shards for 052690, 051600, 011700, and 130660.
2. Verify entry_date rows, entry_price, 30D/90D/180D MFE/MAE, and corporate-action contamination status.
3. Confirm that trigger_type values are canonical: Stage2, Stage2-Actionable, Stage3-Yellow, Stage3-Green, Stage4B, Stage4C.
4. If verified, add the five rows as representative C04 rows and mark source_proxy_only=false only after URL evidence is attached.
5. Consider adding archetype shadow guards:
   - C04_FINAL_CONTRACT_PROJECT_SCOPE_OR_SERVICE_REVENUE_BRIDGE_REQUIRED
   - C04_POST_HEADLINE_STAGE4B_HIGH_MAE_GUARD
   - C04_COMPONENT_LABEL_STAGE2_CAP_WITHOUT_ORDER_BRIDGE
6. Do not change production scoring until the batch suite validates the whole C04 group.
```

## 12. Next research state

```text
completed_round = R1
completed_loop = 107
selection_basis = docs/core/V12_Research_No_Repeat_Index.md + conversation-local generated MD ledger
selected_priority_bucket = Priority 0
round_schedule_status = coverage_index_selected
round_sector_consistency = pass
next_recommended_archetypes = C05_EPC_MEGA_CONTRACT_MARGIN_GAP_next_pass_to_30, C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG_next_pass_to_30, C16_STRATEGIC_RESOURCE_POLICY_SUPPLY_next_pass_to_30, C17_CHEMICAL_COMMODITY_MARGIN_SPREAD_next_pass_to_30, C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION_next_pass_to_30, C24_BIO_TRIAL_DATA_EVENT_RISK_next_pass_to_30
```
