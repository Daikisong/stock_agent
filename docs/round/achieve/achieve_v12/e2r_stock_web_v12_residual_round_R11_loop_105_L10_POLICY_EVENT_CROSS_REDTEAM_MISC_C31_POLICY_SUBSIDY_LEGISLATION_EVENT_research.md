# E2R Stock-Web v12 Residual Research — R11 / C31 Policy Subsidy & Legislation Event

```yaml
schema_version: v12_stock_web_residual_research
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
output_format: one_standalone_markdown_file
selected_round: R11
selected_loop: 105
selection_basis: docs/core/V12_Research_No_Repeat_Index.md + conversation-local generated MD ledger
selected_priority_bucket: Priority 0
round_schedule_status: coverage_index_selected
round_sector_consistency: pass
large_sector_id: L10_POLICY_EVENT_CROSS_REDTEAM_MISC
canonical_archetype_id: C31_POLICY_SUBSIDY_LEGISLATION_EVENT
fine_archetype_id: POLICY_VALUEUP_TO_INSURANCE_BROKERAGE_COMPANY_CASH_BRIDGE_FINAL_PASS_TO_30
price_source: Songdaiki/stock-web
stock_web_manifest_max_date: 2026-02-20
price_basis: tradable_raw
price_adjustment_status: raw_unadjusted_marcap
production_scoring_changed: false
shadow_weight_only: true
stock_agent_code_access_allowed: false
stock_agent_code_patch_allowed: false
live_candidate_mode: false
current_stock_discovery_allowed: false
auto_trading_allowed: false
handoff_prompt_embedded: true
handoff_prompt_executed_now: false
price_row_fetch_status: local_prior_stock_web_rows_reused_for_same_shard_paths
batch_reverification_required: true
source_proxy_only: true
evidence_url_pending: true
```

## 1. Selection rationale

`V12_Research_No_Repeat_Index.md` marks `C31_POLICY_SUBSIDY_LEGISLATION_EVENT` as a Priority 0 archetype with only 3 static rows and 27 rows needed to reach the 30-row floor. Conversation-local v12 outputs have already filled several C31 passes: telecom/policy rows, battery/IRA policy rows, value-up bank rows, and indirect policy-label rows. The last local C31 pass left the archetype near the 30-row floor. This run therefore acts as a **C31 final pass to 30**, adding six policy/value-up rows from insurance and brokerage paths.

The research question is deliberately narrow: when a policy headline says “value-up”, “capital return”, “rate/CSM benefit”, or “market-activity support”, does it become a **company-specific cash bridge**, or is it only a sector-label tailwind that should be capped?

This is not a live stock scan. It does not patch production scoring. It creates a standalone historical residual calibration MD for later batch ingestion.

## 2. Stock-Web atlas confirmation

The run uses the Stock-Web atlas as the price source:

```text
price_data_source = Songdaiki/stock-web
upstream_source = FinanceData/marcap
price_basis = tradable_raw
price_adjustment_status = raw_unadjusted_marcap
calibration_shard_root = atlas/ohlcv_tradable_by_symbol_year
manifest_max_date = 2026-02-20
```

Stock-Web manifest caveat still applies: the atlas is raw/unadjusted marcap OHLCV, so corporate-action-contaminated windows must be blocked by default. In this execution, fresh individual shard fetching was intermittently cache-miss, so this file reuses stock-web-derived rows already present in local v12 research artifacts for the same symbol-year shard paths. All rows are marked `batch_reverification_required=true` for ingestion-time URL/shard re-check.

## 3. Novelty and anti-repeat check

Hard duplicate key:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

This pass does **not** reuse prior C31 hard duplicate keys. Prior C31 local passes already used telecom/battery policy rows and several bank value-up names such as `105560`, `086790`, `055550`, `316140`, and `024110`. This pass adds C31-specific interpretation for six different insurance/brokerage symbols or new symbol families:

```text
000810 삼성화재
005830 DB손해보험
001450 현대해상
032830 삼성생명
039490 키움증권
000370 한화손해보험
```

Some price rows are cross-canonical reused from prior C21/C22 stock-web residual MDs, but the C31 canonical question is different: **policy headline → company cashflow / capital-return bridge**, not insurance reserve quality alone or financial ROE/PBR alone.

## 4. Case table

| case | symbol | name | entry_date | trigger_type | 180D MFE / MAE | C31 interpretation | outcome |
|---|---:|---|---:|---|---:|---|---|
| C31_R11L105_000810 | 000810 | 삼성화재 | 2024-04-26 | Stage3-Yellow | +26.32% / -3.69% | value-up/rate-cycle policy becomes visible only when reserve quality + capital return capacity are both present | positive |
| C31_R11L105_005830 | 005830 | DB손해보험 | 2024-04-26 | Stage2-Actionable | +24.12% / -7.81% | policy tailwind works, but not clean enough for Green without recurring capital-return proof | mixed_positive |
| C31_R11L105_001450 | 001450 | 현대해상 | 2024-05-14 | Stage2 | +7.16% / -20.32% | policy/rate-cycle label without strong reserve/capital bridge becomes a high-MAE false positive | counterexample |
| C31_R11L105_032830 | 032830 | 삼성생명 | 2024-02-23 | Stage3-Yellow | +16.11% / -19.87% | life-insurance policy/value-up headline can recover, but drawdown is too deep for uncapped Stage3 | mixed_positive |
| C31_R11L105_039490 | 039490 | 키움증권 | 2024-02-01 | Stage2-Actionable | +36.06% / -1.95% | brokerage policy/value-up tailwind is usable when ROE, capital activity, and shareholder-return bridge align | positive |
| C31_R11L105_000370 | 000370 | 한화손해보험 | 2024-02-01 | Stage2 | +21.70% / -18.90% | small insurer policy/rate-cycle beta has high MAE; cash bridge must be stronger before promotion | counterexample |

## 5. Trigger rows JSONL

```jsonl
{"row_type":"trigger","schema_version":"v12_stock_web_residual","case_id":"C31_R11L105_000810_20240426_VALUEUP_INSURANCE_CASH_BRIDGE","selected_round":"R11","selected_loop":105,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","fine_archetype_id":"POLICY_VALUEUP_TO_INSURANCE_BROKERAGE_COMPANY_CASH_BRIDGE_FINAL_PASS_TO_30","symbol":"000810","name":"삼성화재","market":"KOSPI","trigger_type":"Stage3-Yellow","trigger_family":"insurance_valueup_policy_csm_capital_return_cash_bridge","trigger_date":"2024-04-26","entry_date":"2024-04-26","entry_price":311500,"entry_price_basis":"close","price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/000/000810/2024.csv","profile_path":"atlas/symbol_profiles/000/000810.json","mfe_30d_pct":21.99,"mae_30d_pct":-3.69,"mfe_90d_pct":26.32,"mae_90d_pct":-3.69,"mfe_180d_pct":26.32,"mae_180d_pct":-3.69,"peak_30d_date":"2024-05-17","peak_30d_price":380000,"trough_30d_date":"2024-05-02","trough_30d_price":300000,"peak_90d_date":"2024-06-28","peak_90d_price":393500,"trough_90d_date":"2024-05-02","trough_90d_price":300000,"peak_180d_date":"2024-06-28","peak_180d_price":393500,"trough_180d_date":"2024-05-02","trough_180d_price":300000,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"four_b_local_peak_proximity":false,"four_b_full_window_peak_proximity":false,"four_b_timing_verdict":"not_4b_clean_positive_followthrough","outcome_label":"positive","positive_or_counterexample":"positive","current_profile_error_type":"policy_valueup_cash_bridge_can_be_underrecognized_if_insurance_rerouted_to_generic_policy_label","calibration_usable":true,"corporate_action_window_status":"batch_reverify_required_no_known_2024_overlap_from_prior_local_row","source_proxy_only":true,"evidence_url_pending":true,"batch_reverification_required":true,"same_entry_group_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT|000810|Stage3-Yellow|2024-04-26","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":"cross_canonical_reinterpretation_from_C22_price_row; new C31 hard duplicate key","independent_evidence_weight":0.76}
{"row_type":"trigger","schema_version":"v12_stock_web_residual","case_id":"C31_R11L105_005830_20240426_RATE_CYCLE_POLICY_BRIDGE","selected_round":"R11","selected_loop":105,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","fine_archetype_id":"POLICY_VALUEUP_TO_INSURANCE_BROKERAGE_COMPANY_CASH_BRIDGE_FINAL_PASS_TO_30","symbol":"005830","name":"DB손해보험","market":"KOSPI","trigger_type":"Stage2-Actionable","trigger_family":"nonlife_insurance_policy_rate_cycle_capital_return_bridge","trigger_date":"2024-04-26","entry_date":"2024-04-26","entry_price":99900,"entry_price_basis":"close","price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/005/005830/2024.csv","profile_path":"atlas/symbol_profiles/005/005830.json","mfe_30d_pct":14.31,"mae_30d_pct":-7.81,"mfe_90d_pct":24.12,"mae_90d_pct":-7.81,"mfe_180d_pct":24.12,"mae_180d_pct":-7.81,"peak_30d_date":"2024-05-16","peak_30d_price":114200,"trough_30d_date":"2024-05-02","trough_30d_price":92100,"peak_90d_date":"2024-08-22","peak_90d_price":124000,"trough_90d_date":"2024-05-02","trough_90d_price":92100,"peak_180d_date":"2024-08-22","peak_180d_price":124000,"trough_180d_date":"2024-05-02","trough_180d_price":92100,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"four_b_local_peak_proximity":true,"four_b_full_window_peak_proximity":true,"four_b_timing_verdict":"local_4b_watch_but_requires_capital_return_persistence","outcome_label":"mixed_positive","positive_or_counterexample":"mixed_positive","current_profile_error_type":"policy_label_plus_insurance_beta_can_be_overpromoted_without_reserve_and_capital_return_persistence","calibration_usable":true,"corporate_action_window_status":"batch_reverify_required_no_known_2024_overlap_from_prior_local_row","source_proxy_only":true,"evidence_url_pending":true,"batch_reverification_required":true,"same_entry_group_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT|005830|Stage2-Actionable|2024-04-26","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":"cross_canonical_reinterpretation_from_C22_price_row; new C31 hard duplicate key","independent_evidence_weight":0.74}
{"row_type":"trigger","schema_version":"v12_stock_web_residual","case_id":"C31_R11L105_001450_20240514_POLICY_LABEL_HIGH_MAE","selected_round":"R11","selected_loop":105,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","fine_archetype_id":"POLICY_VALUEUP_TO_INSURANCE_BROKERAGE_COMPANY_CASH_BRIDGE_FINAL_PASS_TO_30","symbol":"001450","name":"현대해상","market":"KOSPI","trigger_type":"Stage2","trigger_family":"insurance_policy_label_without_company_cash_bridge","trigger_date":"2024-05-14","entry_date":"2024-05-14","entry_price":34200,"entry_price_basis":"close","price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/001/001450/2024.csv","profile_path":"atlas/symbol_profiles/001/001450.json","mfe_30d_pct":2.34,"mae_30d_pct":-9.36,"mfe_90d_pct":7.16,"mae_90d_pct":-9.36,"mfe_180d_pct":7.16,"mae_180d_pct":-20.32,"peak_30d_date":"2024-05-16","peak_30d_price":35000,"trough_30d_date":"2024-06-18","trough_30d_price":31000,"peak_90d_date":"2024-08-20","peak_90d_price":36650,"trough_90d_date":"2024-06-18","trough_90d_price":31000,"peak_180d_date":"2024-08-20","peak_180d_price":36650,"trough_180d_date":"2024-11-15","trough_180d_price":27250,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"four_b_local_peak_proximity":false,"four_b_full_window_peak_proximity":false,"four_b_timing_verdict":"not_4b_high_MAE_counterexample","outcome_label":"counterexample_high_MAE","positive_or_counterexample":"counterexample","current_profile_error_type":"policy_label_false_positive_when_company_specific_capital_return_bridge_absent","calibration_usable":true,"corporate_action_window_status":"batch_reverify_required_no_known_2024_overlap_from_prior_local_row","source_proxy_only":true,"evidence_url_pending":true,"batch_reverification_required":true,"same_entry_group_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT|001450|Stage2|2024-05-14","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":"cross_canonical_reinterpretation_from_C22_price_row; new C31 hard duplicate key","independent_evidence_weight":0.72}
{"row_type":"trigger","schema_version":"v12_stock_web_residual","case_id":"C31_R11L105_032830_20240223_LIFE_INSURANCE_POLICY_DRAWNDOWN","selected_round":"R11","selected_loop":105,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","fine_archetype_id":"POLICY_VALUEUP_TO_INSURANCE_BROKERAGE_COMPANY_CASH_BRIDGE_FINAL_PASS_TO_30","symbol":"032830","name":"삼성생명","market":"KOSPI","trigger_type":"Stage3-Yellow","trigger_family":"life_insurance_valueup_policy_drawdown_recovery","trigger_date":"2024-02-23","entry_date":"2024-02-23","entry_price":95600,"entry_price_basis":"close","price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/032/032830/2024.csv","profile_path":"atlas/symbol_profiles/032/032830.json","mfe_30d_pct":12.76,"mae_30d_pct":-6.59,"mfe_90d_pct":12.76,"mae_90d_pct":-19.87,"mfe_180d_pct":16.11,"mae_180d_pct":-19.87,"peak_30d_date":"2024-03-05","peak_30d_price":107800,"trough_30d_date":"2024-04-09","trough_30d_price":89300,"peak_90d_date":"2024-03-05","peak_90d_price":107800,"trough_90d_date":"2024-04-19","trough_90d_price":76600,"peak_180d_date":"2024-11-18","peak_180d_price":111000,"trough_180d_date":"2024-04-19","trough_180d_price":76600,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"four_b_local_peak_proximity":true,"four_b_full_window_peak_proximity":false,"four_b_timing_verdict":"local_4b_not_full_4b_due_drawdown_recovery","outcome_label":"mixed_positive_high_MAE","positive_or_counterexample":"mixed_positive","current_profile_error_type":"life_insurance_policy_valueup_should_not_promote_to_green_without_drawdown_aware_cash_bridge","calibration_usable":true,"corporate_action_window_status":"batch_reverify_required_no_known_2024_overlap_from_prior_local_row","source_proxy_only":true,"evidence_url_pending":true,"batch_reverification_required":true,"same_entry_group_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT|032830|Stage3-Yellow|2024-02-23","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":"cross_canonical_reinterpretation_from_C22_price_row; new C31 hard duplicate key","independent_evidence_weight":0.72}
{"row_type":"trigger","schema_version":"v12_stock_web_residual","case_id":"C31_R11L105_039490_20240201_BROKERAGE_POLICY_CASH_BRIDGE","selected_round":"R11","selected_loop":105,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","fine_archetype_id":"POLICY_VALUEUP_TO_INSURANCE_BROKERAGE_COMPANY_CASH_BRIDGE_FINAL_PASS_TO_30","symbol":"039490","name":"키움증권","market":"KOSPI","trigger_type":"Stage2-Actionable","trigger_family":"brokerage_valueup_policy_market_activity_capital_return_bridge","trigger_date":"2024-02-01","entry_date":"2024-02-01","entry_price":107600,"entry_price_basis":"close","price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/039/039490/2024.csv","profile_path":"atlas/symbol_profiles/039/039490.json","mfe_30d_pct":26.95,"mae_30d_pct":-1.95,"mfe_90d_pct":26.95,"mae_90d_pct":-1.95,"mfe_180d_pct":36.06,"mae_180d_pct":-1.95,"peak_30d_date":"source_prior_row_pending_date_repair","peak_30d_price":136600,"trough_30d_date":"source_prior_row_pending_date_repair","trough_30d_price":105500,"peak_90d_date":"source_prior_row_pending_date_repair","peak_90d_price":136600,"trough_90d_date":"source_prior_row_pending_date_repair","trough_90d_price":105500,"peak_180d_date":"source_prior_row_pending_date_repair","peak_180d_price":146400,"trough_180d_date":"source_prior_row_pending_date_repair","trough_180d_price":105500,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"four_b_local_peak_proximity":true,"four_b_full_window_peak_proximity":true,"four_b_timing_verdict":"positive_if_brokerage_cash_and_market_activity_bridge_confirmed","outcome_label":"positive_with_cycle_beta_caveat","positive_or_counterexample":"positive","current_profile_error_type":"policy_valueup_tailwind_works_when_company_specific_ROE_and_activity_bridge_exist","calibration_usable":true,"corporate_action_window_status":"batch_reverify_required_no_known_2024_overlap_from_prior_local_row","source_proxy_only":true,"evidence_url_pending":true,"batch_reverification_required":true,"same_entry_group_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT|039490|Stage2-Actionable|2024-02-01","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":"cross_canonical_reinterpretation_from_C21_price_row; new C31 hard duplicate key","independent_evidence_weight":0.76}
{"row_type":"trigger","schema_version":"v12_stock_web_residual","case_id":"C31_R11L105_000370_20240201_SMALL_INSURER_POLICY_HIGH_MAE","selected_round":"R11","selected_loop":105,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","fine_archetype_id":"POLICY_VALUEUP_TO_INSURANCE_BROKERAGE_COMPANY_CASH_BRIDGE_FINAL_PASS_TO_30","symbol":"000370","name":"한화손해보험","market":"KOSPI","trigger_type":"Stage2","trigger_family":"small_nonlife_insurance_policy_beta_high_MAE_guard","trigger_date":"2024-02-01","entry_date":"2024-02-01","entry_price":5120,"entry_price_basis":"close","price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/000/000370/2024.csv","profile_path":"atlas/symbol_profiles/000/000370.json","mfe_30d_pct":20.50,"mae_30d_pct":-18.90,"mfe_90d_pct":20.50,"mae_90d_pct":-18.90,"mfe_180d_pct":21.70,"mae_180d_pct":-18.90,"peak_30d_date":"source_prior_row_pending_date_repair","peak_30d_price":6170,"trough_30d_date":"source_prior_row_pending_date_repair","trough_30d_price":4150,"peak_90d_date":"source_prior_row_pending_date_repair","peak_90d_price":6170,"trough_90d_date":"source_prior_row_pending_date_repair","trough_90d_price":4150,"peak_180d_date":"source_prior_row_pending_date_repair","peak_180d_price":6230,"trough_180d_date":"source_prior_row_pending_date_repair","trough_180d_price":4150,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"four_b_local_peak_proximity":true,"four_b_full_window_peak_proximity":false,"four_b_timing_verdict":"local_4b_high_MAE_counterexample","outcome_label":"counterexample_high_MAE","positive_or_counterexample":"counterexample","current_profile_error_type":"small_insurer_policy_beta_needs_high_MAE_guard_and_cash_bridge_confirmation","calibration_usable":true,"corporate_action_window_status":"batch_reverify_required_no_known_2024_overlap_from_prior_local_row","source_proxy_only":true,"evidence_url_pending":true,"batch_reverification_required":true,"same_entry_group_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT|000370|Stage2|2024-02-01","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":"cross_canonical_reinterpretation_from_C22_price_row; new C31 hard duplicate key","independent_evidence_weight":0.70}
```

## 6. Score-return alignment and current profile stress test

```jsonl
{"row_type":"score_simulation","case_id":"C31_R11L105_000810_20240426_VALUEUP_INSURANCE_CASH_BRIDGE","baseline_proxy":"e2r_2_1_stock_web_calibrated","raw_total_score_proxy":82.0,"stage_proxy_before_shadow":"Stage3-Yellow","stage_proxy_after_shadow":"Stage3-Yellow","green_allowed_after_shadow":false,"reason":"price validates the policy-to-cash bridge, but C31 should require explicit company cash/capital-return bridge before Green"}
{"row_type":"score_simulation","case_id":"C31_R11L105_005830_20240426_RATE_CYCLE_POLICY_BRIDGE","baseline_proxy":"e2r_2_1_stock_web_calibrated","raw_total_score_proxy":77.0,"stage_proxy_before_shadow":"Stage3-Yellow","stage_proxy_after_shadow":"Stage2-Actionable","green_allowed_after_shadow":false,"reason":"usable positive path, but local 4B/high-MAE risk remains unless reserve quality and capital-return persistence are confirmed"}
{"row_type":"score_simulation","case_id":"C31_R11L105_001450_20240514_POLICY_LABEL_HIGH_MAE","baseline_proxy":"e2r_2_1_stock_web_calibrated","raw_total_score_proxy":72.0,"stage_proxy_before_shadow":"Stage2","stage_proxy_after_shadow":"Stage2_or_4B_watch_cap","green_allowed_after_shadow":false,"reason":"policy label alone does not create company cash bridge; 180D MAE below -20% makes it a residual false positive"}
{"row_type":"score_simulation","case_id":"C31_R11L105_032830_20240223_LIFE_INSURANCE_POLICY_DRAWNDOWN","baseline_proxy":"e2r_2_1_stock_web_calibrated","raw_total_score_proxy":79.0,"stage_proxy_before_shadow":"Stage3-Yellow","stage_proxy_after_shadow":"Stage2-Actionable","green_allowed_after_shadow":false,"reason":"recovery exists but path suffered deep drawdown; C31 needs drawdown-aware cap until CSM/reserve/capital-return bridge is explicit"}
{"row_type":"score_simulation","case_id":"C31_R11L105_039490_20240201_BROKERAGE_POLICY_CASH_BRIDGE","baseline_proxy":"e2r_2_1_stock_web_calibrated","raw_total_score_proxy":80.0,"stage_proxy_before_shadow":"Stage2-Actionable","stage_proxy_after_shadow":"Stage3-Yellow_watch","green_allowed_after_shadow":false,"reason":"brokerage policy/value-up tailwind becomes usable when ROE/activity/capital-return bridge appears, but C31 Green still needs non-price evidence"}
{"row_type":"score_simulation","case_id":"C31_R11L105_000370_20240201_SMALL_INSURER_POLICY_HIGH_MAE","baseline_proxy":"e2r_2_1_stock_web_calibrated","raw_total_score_proxy":70.0,"stage_proxy_before_shadow":"Stage2","stage_proxy_after_shadow":"Stage2_cap_or_4B_local_watch","green_allowed_after_shadow":false,"reason":"small insurer beta creates high MAE; do not convert policy label into Stage3 without stronger cash bridge"}
```

Mechanically, this is the same as separating a promise from a bank transfer. The policy headline is the promise; the company-specific cash bridge is the money actually arriving in the account. C31 should not pay scoring credit for the promise unless the path to budget, tariff, subsidy, capital return, or recurring revenue is visible.

## 7. Aggregate metrics JSONL

```jsonl
{"row_type":"aggregate_metrics","schema_version":"v12_stock_web_residual","round":"R11","loop":105,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","fine_archetype_id":"POLICY_VALUEUP_TO_INSURANCE_BROKERAGE_COMPANY_CASH_BRIDGE_FINAL_PASS_TO_30","new_independent_case_count":6,"reused_case_count":0,"cross_canonical_price_row_reuse_count":6,"same_archetype_new_symbol_count":6,"same_archetype_new_trigger_family_count":6,"calibration_usable_case_count":6,"calibration_usable_trigger_count":6,"positive_case_count":2,"mixed_positive_count":2,"counterexample_count":2,"local_4b_watch_count":4,"current_profile_error_count":6,"median_mfe_30d_pct":18.405,"median_mae_30d_pct":-7.20,"median_mfe_90d_pct":20.75,"median_mae_90d_pct":-8.585,"median_mfe_180d_pct":24.12,"median_mae_180d_pct":-13.855,"high_mae_over_15pct_count":3,"auto_selected_coverage_gap_static_index":"C31 rows 3 -> 9 if accepted; still Priority 0 by static index","auto_selected_coverage_gap_conversation_local":"C31 approx rows 24 -> 30 if accepted; C31 local 30-row floor reached","loop_contribution_label":"canonical_archetype_rule_candidate_final_pass_to_30","promotion_usable_without_reverification":false,"batch_reverification_required":true}
{"row_type":"shadow_weight_candidate","schema_version":"v12_stock_web_residual","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","do_not_propose_new_weight_delta":false,"new_axis_proposed":["C31_POLICY_TO_COMPANY_CASH_BRIDGE_REQUIRED","C31_VALUEUP_POLICY_REROUTE_TO_C21_OR_C22_WHEN_SECTOR_SPECIFIC_BRIDGE_DOMINATES","C31_INSURANCE_POLICY_HEADLINE_REQUIRES_CSM_RESERVE_CAPITAL_RETURN_CONFIRMATION","C31_BROKERAGE_POLICY_HEADLINE_REQUIRES_ROE_ACTIVITY_CAPITAL_RETURN_CONFIRMATION","C31_HIGH_MAE_POLICY_LABEL_STAGE3_CAP"],"existing_axis_strengthened":["stage2_required_bridge","price_only_blowoff_blocks_positive_stage","full_4b_requires_non_price_evidence","local_4b_watch_guard","high_MAE_guardrail"],"existing_axis_weakened":null,"confidence":"medium_low_until_url_and_shard_reverification"}
{"row_type":"residual_contribution","schema_version":"v12_stock_web_residual","round":"R11","loop":105,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","new_independent_case_count":6,"residual_error_types_found":["policy_headline_false_positive","sector_specific_bridge_double_counting","insurance_policy_high_MAE_drawdown","brokerage_policy_cash_bridge_positive","local_4b_policy_reversion"],"coverage_gap_contribution":"C31 conversation-local reaches 30-row floor if accepted","handoff_relevance":"batch coding agent can add C31-specific reroute/cap rules after URL and stock-web shard re-verification"}
```

## 8. Rule candidate narrative

The C31 rule should not reward a policy headline as if it were already economic cash. It needs a bridge:

```text
policy headline
  -> legal/budget/tariff/subsidy mechanism
  -> company-level capture route
  -> margin / FCF / capital-return effect
  -> durable score credit
```

For financial names, a special reroute guard is needed. If the event is mainly bank/insurance/brokerage value-up, then the better canonical home is often `C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN` or `C22_INSURANCE_RATE_CYCLE_RESERVE`. C31 should remain the policy wrapper only when the law, budget, or subsidy mechanism itself is the causal engine.

## 9. Validation scope and caveats

```text
validation_scope = historical trigger-level residual research
price_data_source = Songdaiki/stock-web
price_basis = tradable_raw
stock_web_manifest_max_date = 2026-02-20
nonprice_event_status = source_proxy_only / evidence_url_pending
price_row_fetch_status = local_prior_stock_web_rows_reused_for_same_shard_paths
batch_reverification_required = true
production_scoring_changed = false
```

This MD is calibration-useful after batch re-verification. It should not be used as live recommendation material.

## 10. Deferred Coding Agent Handoff Prompt

```text
You are the deferred coding agent for E2R v12 batch ingestion.

Do not live-scan stocks. Do not connect brokerage APIs. Do not alter production scoring until this MD is batch-reviewed with other v12 residual MDs.

Input MD:
e2r_stock_web_v12_residual_round_R11_loop_105_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_C31_POLICY_SUBSIDY_LEGISLATION_EVENT_research.md

Tasks:
1. Re-fetch stock-web profiles and tradable shards for 000810, 005830, 001450, 032830, 039490, 000370.
2. Verify entry_date, entry_price, 30/90/180D MFE/MAE, peak/trough dates, and corporate_action_candidate overlap.
3. Verify non-price event URLs for policy/value-up, CSM/reserve quality, capital-return execution, and brokerage ROE/activity bridges.
4. If rows pass, ingest JSONL trigger rows as C31 residual calibration candidates.
5. Add or strengthen shadow-only C31 axes:
   - C31_POLICY_TO_COMPANY_CASH_BRIDGE_REQUIRED
   - C31_VALUEUP_POLICY_REROUTE_TO_C21_OR_C22_WHEN_SECTOR_SPECIFIC_BRIDGE_DOMINATES
   - C31_INSURANCE_POLICY_HEADLINE_REQUIRES_CSM_RESERVE_CAPITAL_RETURN_CONFIRMATION
   - C31_BROKERAGE_POLICY_HEADLINE_REQUIRES_ROE_ACTIVITY_CAPITAL_RETURN_CONFIRMATION
   - C31_HIGH_MAE_POLICY_LABEL_STAGE3_CAP
6. Keep production scoring unchanged unless batch consensus across multiple v12 MDs supports a patch.
```

## 11. Next research state

```text
completed_round = R11
completed_loop = 105
selection_basis = docs/core/V12_Research_No_Repeat_Index.md + conversation-local generated MD ledger
selected_priority_bucket = Priority 0
round_schedule_status = coverage_index_selected
round_sector_consistency = pass
C31_conversation_local_after_if_accepted = approx 30 rows; local 30-row floor reached
next_recommended_archetypes = C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP_final_pass_to_30, C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE_fourth_pass_to_30, C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE_fourth_pass_to_30, C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK_final_pass_to_30, C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION, C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY
```
