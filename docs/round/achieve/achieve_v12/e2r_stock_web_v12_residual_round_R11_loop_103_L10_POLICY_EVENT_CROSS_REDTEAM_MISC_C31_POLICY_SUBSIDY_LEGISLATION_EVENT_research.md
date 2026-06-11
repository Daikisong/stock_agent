# E2R Historical Calibration v12 — C31 Policy Subsidy Legislation Event Residual Research

```text
completed_round = R11
completed_loop = 103
selection_basis = docs/core/V12_Research_No_Repeat_Index.md + conversation-local generated MD ledger
selected_priority_bucket = Priority 0
round_schedule_status = coverage_index_selected
round_sector_consistency = pass

large_sector_id = L10_POLICY_EVENT_CROSS_REDTEAM_MISC
canonical_archetype_id = C31_POLICY_SUBSIDY_LEGISLATION_EVENT
fine_archetype_id = POLICY_SUBSIDY_TO_COMPANY_CASH_BRIDGE_THIRD_PASS_NUCLEAR_SERVICE_AND_INDIRECT_IRA_LABEL_SPLIT

price_source = Songdaiki/stock-web
price_basis = tradable_raw
upstream_source = FinanceData/marcap
price_adjustment_status = raw_unadjusted_marcap
stock_web_manifest_max_date = 2026-02-20

production_scoring_changed = false
shadow_weight_only = true
handoff_prompt_embedded = true
handoff_prompt_executed_now = false
price_row_fetch_status = local_prior_stock_web_rows_reused_for_same_shard_path; batch_reverification_required
```

## 1. Selection rationale

The v12 runner is coverage-index first. The static no-repeat index still keeps `C31_POLICY_SUBSIDY_LEGISLATION_EVENT` in Priority 0 with only 3 representative rows, and the conversation-local ledger has not yet taken C31 to the 30-row floor. The previous local C31 passes covered utility tariff/value-up/telemedicine/resource-policy and battery IRA/AMPC policy labels. This loop adds a cross-canonical C31 pass using **policy-to-company-cash bridge** rows that were already price-validated in prior v12 local artifacts under C04, C13, and C12.

This is not a duplicate for C31 because the hard key is:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

The rows below reuse stock-web price paths only to avoid the current raw URL cache-miss for individual shards. They are new C31 canonical keys and are flagged for batch re-verification before profile promotion.

Prior C31 local symbols avoided:

```text
071320, 033780, 013990, 032620,
015760, 036460, 033230, 032850,
373220, 006400, 096770, 003670
```

New C31 symbols this loop:

```text
051600, 052690, 247540, 051910
```

Research question:

```text
When a policy, subsidy, or legislation headline is true at the macro level,
which companies actually receive cash, margin, tariff pass-through, budget allocation, or service revenue,
and which companies merely inherit a theme label?
```

## 2. Stock-Web manifest and validation scope

The stock-web manifest basis for this v12 run:

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
markets = KONEX, KOSDAQ, KOSDAQ GLOBAL, KOSPI
calibration_shard_root = atlas/ohlcv_tradable_by_symbol_year
raw_shard_root = atlas/ohlcv_raw_by_symbol_year
schema_path = atlas/schema.json
universe_path = atlas/universe/all_symbols.csv
```

Validation caveat for this loop:

```text
price_route_access = degraded_for_new_direct_raw_urls
price_row_source = local prior v12 MD rows that themselves used Songdaiki/stock-web shards
strict_ingest_recommendation = batch_reverify_stock_web_profile_and_shard_paths_before promotion
calibration_usable_for_research_aggregate = true
promotion_usable_without_reverification = false
```

This preserves the mechanism-level lesson while preventing the coding agent from blindly promoting unreverified row paths.

## 3. Case universe

| case_id | symbol | name | role | entry | entry_price | 30D MFE/MAE | 90D MFE/MAE | 180D MFE/MAE | C31 lesson |
|---|---:|---|---|---:|---:|---:|---:|---:|---|
| C31_R11L103_051600_2024_07_18_NUCLEAR_OM_POLICY_CASH_BRIDGE_POSITIVE | 051600 | 한전KPS | positive_service_cash_bridge | 2024-07-18 | 38,900 | +13.88% / -3.98% | +19.92% / -3.98% | +23.65% / -2.31% | Stage2-Actionable_to_Stage3-Yellow_if_service_revenue_margin_revision_confirmed |
| C31_R11L103_052690_2024_07_09_NUCLEAR_ENGINEERING_POLICY_LOCAL4B_MIXED | 052690 | 한전기술 | mixed_policy_to_project_bridge | 2024-07-09 | 74,000 | +32.57% / -11.76% | +32.57% / -14.46% | +32.57% / -32.70% | Stage2-Actionable_or_local_4B_watch_until_final_contract_margin_bridge |
| C31_R11L103_247540_2024_01_22_IRA_CATHODE_POLICY_LABEL_COUNTER | 247540 | 에코프로비엠 | counterexample_indirect_policy_label | 2024-01-22 | 248,000 | +10.08% / -14.92% | +20.36% / -14.92% | +20.36% / -47.58% | Stage2_or_4B_watch_not_Green_without_utilization_cash_bridge |
| C31_R11L103_051910_2024_02_16_PARENT_MATERIAL_POLICY_CONTAMINATION_COUNTER | 051910 | LG화학 | counterexample_parent_policy_contamination | 2024-02-16 | 504,000 | +3.17% / -16.57% | +3.17% / -35.32% | +3.17% / -46.92% | Stage1_or_Stage2_watch_until_direct_subsidy_or_material_margin_bridge |


## 4. Mechanism notes

### 4.1 051600 한전KPS — service revenue bridge is different from a policy slogan

A nuclear policy headline is the weather. `051600` is useful because it also has the gutter: O&M and service revenue can convert policy visibility into repeatable cashflow. The prior stock-web path shows controlled drawdown across 30D/90D/180D and a positive 180D MFE/MAE balance. This argues that C31 should not simply suppress every policy headline; it should reward the subset with visible service revenue, margin, and budget route.

### 4.2 052690 한전기술 — local 4B flame, 180D smoke

`052690` shows the opposite side of the same nuclear-policy mechanism. The local MFE was strong, but the 180D path carried high MAE. For C31, this should be treated as a local 4B or Stage2-Actionable watch unless final contract scope, budget allocation, legal status, and engineering margin bridge are confirmed.

### 4.3 247540 에코프로비엠 — indirect IRA/AMPC label is not direct subsidy cash capture

`247540` is a clean C31 policy-label counterexample. A cathode supplier may benefit from IRA/AMPC vocabulary, but the stock path can fail if customer call-off, utilization, ASP, and cash conversion deteriorate. C31 should split direct subsidy capture from indirect thematic policy exposure.

### 4.4 051910 LG화학 — parent balance-sheet and spread contamination

`051910` demonstrates the parent-contamination problem. A policy/material label can be directionally relevant, but the actual equity path can be dominated by petrochemical spread, parent balance sheet, and demand/call-off issues. The correct C31 behavior is to cap policy-label-only cases at watch unless the company-level cash bridge is explicit.

## 5. Score-return alignment

| symbol | raw score shape | observed path | alignment verdict |
|---:|---|---|---|
| 051600 | moderate score, higher visibility/service bridge | controlled MAE, positive MFE | positive C31 bridge candidate |
| 052690 | high information/policy score, weaker final-contract bridge | high MFE but 180D drawdown | local 4B, not durable Green |
| 247540 | policy/subsidy vocabulary plus beta | high 180D MAE | false positive if policy label over-weighted |
| 051910 | policy/material label diluted by parent exposure | very low MFE and high MAE | counterexample / cap required |

Aggregate path summary:

```text
median_mfe_30d_pct = 11.98
median_mae_30d_pct = -13.34
median_mfe_90d_pct = 20.14
median_mae_90d_pct = -14.69
median_mfe_180d_pct = 22.0
median_mae_180d_pct = -39.81
high_mae_over_15pct_count = 3
local_4b_watch_count = 3
```

## 6. Shadow rule candidate

```text
new_axis_proposed:
C31_POLICY_TO_COMPANY_CASH_BRIDGE_REQUIRED
C31_DIRECT_BUDGET_TARIFF_SERVICE_REVENUE_CAPTURE_ALLOWED
C31_INDIRECT_POLICY_LABEL_STAGE3_CAP
C31_LOCAL_4B_HEADLINE_REVERSION_GUARD
C31_PARENT_BALANCE_SHEET_CONTAMINATION_GUARD
```

Rule text:

```text
For C31, policy/subsidy/legislation evidence can unlock Stage2-Actionable only when the policy maps to a company-level cash route: direct budget allocation, tariff pass-through, tax credit capture, signed contract, customer call-off, utilization, service revenue, margin, or FCF. Indirect thematic policy beneficiaries remain capped at Stage2/watch. Strong local MFE can be preserved as local 4B, but durable Stage3 requires non-price cash bridge evidence and low forward MAE.
```

Existing global axes strengthened:

```text
stage2_required_bridge
stage2_actionable_bonus_requires_non_price_bridge
price_only_blowoff_blocks_positive_stage
full_4b_requires_non_price_evidence
local_4b_watch_guard
high_MAE_guardrail
```

## 7. Machine-readable rows

```jsonl
{"row_type":"trigger_row","research_session":"post_calibrated_sector_archetype_residual_research","mode":"historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12","selected_round":"R11","selected_loop":103,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","fine_archetype_id":"POLICY_SUBSIDY_TO_COMPANY_CASH_BRIDGE_THIRD_PASS_NUCLEAR_SERVICE_AND_INDIRECT_IRA_LABEL_SPLIT","case_id":"C31_R11L103_051600_2024_07_18_NUCLEAR_OM_POLICY_CASH_BRIDGE_POSITIVE","symbol":"051600","name":"한전KPS","market":"KOSPI","trigger_type":"Stage2-Actionable","trigger_family":"nuclear_policy_OM_service_revenue_cash_bridge","entry_date":"2024-07-18","entry_price":38900,"entry_price_basis":"close","price_source_repo":"Songdaiki/stock-web","price_source_path":"atlas/ohlcv_tradable_by_symbol_year/051/051600/2024.csv + 2025 continuation","profile_path":"atlas/symbol_profiles/051/051600.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","mfe_30d_pct":13.88,"mae_30d_pct":-3.98,"peak_30d_date":"2024-08-28","trough_30d_date":"2024-07-19","mfe_90d_pct":19.92,"mae_90d_pct":-3.98,"peak_90d_date":"2024-10-17","trough_90d_date":"2024-07-19","mfe_180d_pct":23.65,"mae_180d_pct":-2.31,"peak_180d_date":"2025-01-24","trough_180d_date":"2025-04-09","local_4b_watch":false,"full_4b_requires_non_price_evidence":true,"hard_4c":false,"outcome_label":"positive","current_profile_error":"current profile can under-credit policy beneficiaries when the policy is already tied to repeat O&M/service revenue and controlled MAE","recommended_shadow_stage":"Stage2-Actionable_to_Stage3-Yellow_if_service_revenue_margin_revision_confirmed","calibration_usable":true,"corporate_action_window_status":"clean_or_prior_v12_clean_window_reused","source_proxy_only":true,"evidence_url_pending":true,"price_row_fetch_status":"local_prior_stock_web_rows_reused_for_same_shard_path; batch_reverification_required","prior_price_validation_source":"R1_loop_104_C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY","dedupe_key":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT|051600|Stage2-Actionable|2024-07-18"}
{"row_type":"trigger_row","research_session":"post_calibrated_sector_archetype_residual_research","mode":"historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12","selected_round":"R11","selected_loop":103,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","fine_archetype_id":"POLICY_SUBSIDY_TO_COMPANY_CASH_BRIDGE_THIRD_PASS_NUCLEAR_SERVICE_AND_INDIRECT_IRA_LABEL_SPLIT","case_id":"C31_R11L103_052690_2024_07_09_NUCLEAR_ENGINEERING_POLICY_LOCAL4B_MIXED","symbol":"052690","name":"한전기술","market":"KOSPI","trigger_type":"Stage3-Yellow","trigger_family":"nuclear_policy_engineering_final_contract_margin_bridge_missing","entry_date":"2024-07-09","entry_price":74000,"entry_price_basis":"close","price_source_repo":"Songdaiki/stock-web","price_source_path":"atlas/ohlcv_tradable_by_symbol_year/052/052690/2024.csv + 2025 continuation","profile_path":"atlas/symbol_profiles/052/052690.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","mfe_30d_pct":32.57,"mae_30d_pct":-11.76,"peak_30d_date":"2024-07-18","trough_30d_date":"2024-08-07","mfe_90d_pct":32.57,"mae_90d_pct":-14.46,"peak_90d_date":"2024-07-18","trough_90d_date":"2024-09-06","mfe_180d_pct":32.57,"mae_180d_pct":-32.7,"peak_180d_date":"2024-07-18","trough_180d_date":"2025-04-09","local_4b_watch":true,"full_4b_requires_non_price_evidence":true,"hard_4c":false,"outcome_label":"mixed_positive_local_4b_watch","current_profile_error":"policy/project headline can look like Stage3 but reverts if final contract scope and engineering margin bridge are not locked","recommended_shadow_stage":"Stage2-Actionable_or_local_4B_watch_until_final_contract_margin_bridge","calibration_usable":true,"corporate_action_window_status":"clean_or_prior_v12_clean_window_reused","source_proxy_only":true,"evidence_url_pending":true,"price_row_fetch_status":"local_prior_stock_web_rows_reused_for_same_shard_path; batch_reverification_required","prior_price_validation_source":"R1_loop_104_C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY","dedupe_key":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT|052690|Stage3-Yellow|2024-07-09"}
{"row_type":"trigger_row","research_session":"post_calibrated_sector_archetype_residual_research","mode":"historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12","selected_round":"R11","selected_loop":103,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","fine_archetype_id":"POLICY_SUBSIDY_TO_COMPANY_CASH_BRIDGE_THIRD_PASS_NUCLEAR_SERVICE_AND_INDIRECT_IRA_LABEL_SPLIT","case_id":"C31_R11L103_247540_2024_01_22_IRA_CATHODE_POLICY_LABEL_COUNTER","symbol":"247540","name":"에코프로비엠","market":"KOSDAQ","trigger_type":"Stage2","trigger_family":"IRA_AMPC_cathode_policy_label_without_utilization_cash_bridge","entry_date":"2024-01-22","entry_price":248000,"entry_price_basis":"close","price_source_repo":"Songdaiki/stock-web","price_source_path":"atlas/ohlcv_tradable_by_symbol_year/247/247540/2024.csv","profile_path":"atlas/symbol_profiles/247/247540.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","mfe_30d_pct":10.08,"mae_30d_pct":-14.92,"peak_30d_date":"2024-03-27","trough_30d_date":"2024-H1","mfe_90d_pct":20.36,"mae_90d_pct":-14.92,"peak_90d_date":"2024-03-27","trough_90d_date":"2024-H1","mfe_180d_pct":20.36,"mae_180d_pct":-47.58,"peak_180d_date":"2024-03-27","trough_180d_date":"2024-H2","local_4b_watch":true,"full_4b_requires_non_price_evidence":true,"hard_4c":false,"outcome_label":"counterexample_high_MAE_indirect_policy_label","current_profile_error":"IRA/AMPC vocabulary can over-credit a cathode supplier when customer call-off and utilization are already weakening","recommended_shadow_stage":"Stage2_or_4B_watch_not_Green_without_utilization_cash_bridge","calibration_usable":true,"corporate_action_window_status":"clean_or_prior_v12_clean_window_reused","source_proxy_only":true,"evidence_url_pending":true,"price_row_fetch_status":"local_prior_stock_web_rows_reused_for_same_shard_path; batch_reverification_required","prior_price_validation_source":"R3_loop_100_C13_BATTERY_JV_UTILIZATION_AMPC_IRA","dedupe_key":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT|247540|Stage2|2024-01-22"}
{"row_type":"trigger_row","research_session":"post_calibrated_sector_archetype_residual_research","mode":"historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12","selected_round":"R11","selected_loop":103,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","fine_archetype_id":"POLICY_SUBSIDY_TO_COMPANY_CASH_BRIDGE_THIRD_PASS_NUCLEAR_SERVICE_AND_INDIRECT_IRA_LABEL_SPLIT","case_id":"C31_R11L103_051910_2024_02_16_PARENT_MATERIAL_POLICY_CONTAMINATION_COUNTER","symbol":"051910","name":"LG화학","market":"KOSPI","trigger_type":"Stage4B","trigger_family":"battery_material_policy_label_parent_balance_sheet_and_spread_contamination","entry_date":"2024-02-16","entry_price":504000,"entry_price_basis":"close","price_source_repo":"Songdaiki/stock-web","price_source_path":"atlas/ohlcv_tradable_by_symbol_year/051/051910/2024.csv","profile_path":"atlas/symbol_profiles/051/051910.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","mfe_30d_pct":3.17,"mae_30d_pct":-16.57,"peak_30d_date":"2024-02-19","trough_30d_date":"2024-04-02","mfe_90d_pct":3.17,"mae_90d_pct":-35.32,"peak_90d_date":"2024-02-19","trough_90d_date":"2024-07-19","mfe_180d_pct":3.17,"mae_180d_pct":-46.92,"peak_180d_date":"2024-02-19","trough_180d_date":"2024-11-15","local_4b_watch":true,"full_4b_requires_non_price_evidence":true,"hard_4c":false,"outcome_label":"counterexample_parent_contamination_high_MAE","current_profile_error":"policy subsidy/material label is diluted by parent petrochemical spread, balance sheet, and customer call-off drag","recommended_shadow_stage":"Stage1_or_Stage2_watch_until_direct_subsidy_or_material_margin_bridge","calibration_usable":true,"corporate_action_window_status":"clean_or_prior_v12_clean_window_reused","source_proxy_only":true,"evidence_url_pending":true,"price_row_fetch_status":"local_prior_stock_web_rows_reused_for_same_shard_path; batch_reverification_required","prior_price_validation_source":"R3_loop_102_C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","dedupe_key":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT|051910|Stage4B|2024-02-16"}
{"row_type":"aggregate","selected_round":"R11","selected_loop":103,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","fine_archetype_id":"POLICY_SUBSIDY_TO_COMPANY_CASH_BRIDGE_THIRD_PASS_NUCLEAR_SERVICE_AND_INDIRECT_IRA_LABEL_SPLIT","new_independent_case_count":4,"reused_case_count":0,"cross_canonical_price_row_reuse_count":4,"same_archetype_new_symbol_count":4,"same_archetype_new_trigger_family_count":4,"calibration_usable_case_count":4,"calibration_usable_trigger_count":4,"positive_case_count":1,"mixed_positive_count":1,"counterexample_count":2,"local_4b_watch_count":3,"current_profile_error_count":4,"median_mfe_30d_pct":11.98,"median_mae_30d_pct":-13.34,"median_mfe_90d_pct":20.14,"median_mae_90d_pct":-14.69,"median_mfe_180d_pct":22.0,"median_mae_180d_pct":-39.81,"auto_selected_coverage_gap_static_index":"C31 rows 3 -> 7 if accepted; still Priority 0, need 23 to 30","auto_selected_coverage_gap_conversation_local":"C31 approx rows 15 -> 19 if accepted; still Priority 0, need about 11 to reach 30","promotion_usable_without_reverification":false,"batch_reverification_required":true}
{"row_type":"shadow_weight_candidate","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","do_not_propose_new_weight_delta":false,"new_axis_proposed":["C31_POLICY_TO_COMPANY_CASH_BRIDGE_REQUIRED","C31_DIRECT_BUDGET_TARIFF_SERVICE_REVENUE_CAPTURE_ALLOWED","C31_INDIRECT_POLICY_LABEL_STAGE3_CAP","C31_LOCAL_4B_HEADLINE_REVERSION_GUARD","C31_PARENT_BALANCE_SHEET_CONTAMINATION_GUARD"],"existing_axis_strengthened":["stage2_required_bridge","stage2_actionable_bonus_requires_non_price_bridge","price_only_blowoff_blocks_positive_stage","full_4b_requires_non_price_evidence","local_4b_watch_guard","high_MAE_guardrail"],"existing_axis_weakened":[],"candidate_rule_text":"Policy/subsidy headlines require company-level budget, tariff, tax-credit, contract, utilization, service-revenue, margin, or FCF bridge before durable Stage3. Indirect policy labels remain Stage2/watch unless cash capture is direct and forward MAE is controlled."}
```

## 8. Residual contribution summary

```text
sector_specific_rule_candidate = true
canonical_archetype_rule_candidate = true
loop_contribution_label = canonical_archetype_rule_candidate
new_independent_case_count = 4
calibration_usable_trigger_count = 4
positive_case_count = 1
mixed_positive_count = 1
counterexample_count = 2
local_4b_watch_count = 3
current_profile_error_count = 4
promotion_usable_without_reverification = false
```

C31 is a bridge archetype. The law, subsidy, or policy is only the first switch. The stock rerates durably only when current can flow through a company-specific wire: contract, tariff, tax credit, utilization, margin, service revenue, or FCF. Without that wire, the policy label can glow brightly for a few days and still burn the 180D path.

## 9. Deferred Coding Agent Handoff Prompt — do not execute now

```text
You are the later batch implementation coding agent. Do not implement this file alone. Ingest it together with other v12 residual research files. Reverify all C31_R11L103 stock-web profile/shard paths before promotion because this run reused local-prior stock-web rows after direct raw shard cache miss. If reverified, add C31-specific shadow rules:
1. require policy_to_company_cash_bridge before Stage3;
2. distinguish direct budget/tariff/service/tax-credit capture from indirect policy label;
3. cap local 4B policy headline spikes without non-price cash bridge;
4. apply parent balance-sheet contamination guard;
5. preserve positive service-revenue policy cases when MAE is controlled.
Never execute live trading. Never patch production scoring without batch validation.
```

## 10. Next research state

```text
completed_round = R11
completed_loop = 103
selection_basis = docs/core/V12_Research_No_Repeat_Index.md + conversation-local generated MD ledger
selected_priority_bucket = Priority 0
round_schedule_status = coverage_index_selected
round_sector_consistency = pass
next_recommended_archetypes = C31_POLICY_SUBSIDY_LEGISLATION_EVENT_fourth_pass_to_30, C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP_fourth_pass_to_30, C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK_third_pass_to_30, C18_CONSUMER_EXPORT_CHANNEL_REORDER_second_pass_to_30, C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE_fourth_pass_to_30, R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL
```
