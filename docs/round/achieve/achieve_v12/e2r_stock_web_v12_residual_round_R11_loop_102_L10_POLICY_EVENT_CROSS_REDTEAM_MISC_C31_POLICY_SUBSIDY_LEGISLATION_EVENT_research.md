# E2R Historical Calibration v12 — C31 Policy/Subsidy/Legislation Event Residual Research

```text
completed_round = R11
completed_loop = 102
selection_basis = docs/core/V12_Research_No_Repeat_Index.md + conversation-local generated MD ledger
selected_priority_bucket = Priority 0
round_schedule_status = coverage_index_selected
round_sector_consistency = pass

large_sector_id = L10_POLICY_EVENT_CROSS_REDTEAM_MISC
canonical_archetype_id = C31_POLICY_SUBSIDY_LEGISLATION_EVENT
fine_archetype_id = BATTERY_IRA_AMPC_POLICY_SUBSIDY_TO_COMPANY_CASH_BRIDGE_VS_INDIRECT_POLICY_LABEL_FALSE_POSITIVE

price_source = Songdaiki/stock-web
price_basis = tradable_raw
upstream_source = FinanceData/marcap
price_adjustment_status = raw_unadjusted_marcap
stock_web_manifest_max_date = 2026-02-20

production_scoring_changed = false
shadow_weight_only = true
handoff_prompt_embedded = true
handoff_prompt_executed_now = false
```

## 1. Selection rationale

The v12 scheduler is coverage-index first, not round-cycle first. The static no-repeat index still places `C31_POLICY_SUBSIDY_LEGISLATION_EVENT` in Priority 0 with only 3 representative rows. Conversation-local C31 work has already added two passes: utility/value-up/low-birth/telemedicine and resource-policy/telemedicine replay. This loop keeps the same canonical under-fill but changes the failure family to **battery IRA / AMPC / subsidy legislation**.

This loop deliberately avoids the earlier C31 symbols:

```text
prior_C31_local_symbols = 071320, 033780, 013990, 032620, 015760, 036460, 033230, 032850
new_C31_symbols_this_loop = 373220, 006400, 096770, 003670
```

The research question is narrow:

```text
When a policy/subsidy/legislation headline is real at the macro level,
does the equity actually receive company-level cashflow,
or is the stock only wearing the policy flag like a borrowed uniform?
```

For C31, a subsidy is not automatically a thesis. The law is the rain cloud; the company still needs a gutter, a pipe, and a tank. Without direct credit capture, customer call-off, utilization, margin, or FCF conversion, the headline can produce MFE but still leave the 180D path as a false positive.

## 2. Stock-Web manifest and validation scope

The stock-web manifest used by this research pack reports:

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

Validation rules applied:

```text
must_use_actual_stock_web_1D_OHLC = true
price_basis = tradable_raw
corporate_action_contaminated_180D_window => calibration_usable=false
forward windows judged by stock_web_manifest_max_date, not current date
non-price evidence = source_proxy_only / evidence_url_pending=true
```

The OHLC rows below were previously verified from stock-web shards in this same v12 research session and are reused here only as price-path evidence under a different canonical archetype. The canonical duplicate key is `canonical_archetype_id + symbol + trigger_type + entry_date`; none of the C31 keys below appears in the prior C31 local ledger.

## 3. Case universe and profile checks

| case_id | ticker | name | profile status | selected role | C31 lesson |
|---|---:|---|---|---|---|
| C31-R11L102-01 | 373220 | LG에너지솔루션 | active_like, no corporate-action candidate in selected window | local positive / 180D reversion | direct subsidy/ramp can work locally, but durable Green needs utilization/cash bridge |
| C31-R11L102-02 | 006400 | 삼성SDI | active_like, old corporate-action dates only; no 2024 overlap | counterexample | premium battery policy label without cash bridge creates high MAE |
| C31-R11L102-03 | 096770 | SK이노베이션 | active_like; 2024-11-20 CA candidate outside selected 180D window | mixed positive | subsidiary subsidy benefit can be diluted by parent balance-sheet/refining/merger noise |
| C31-R11L102-04 | 003670 | 포스코퓨처엠 | active_like, no 2024 corporate-action overlap | counterexample | indirect IRA/materials label is not direct subsidy cash capture |

## 4. Raw price observations used

### 4.1 LG에너지솔루션 — 373220

```csv
d,o,h,l,c,v,a,mc,s,m
2024-08-21,333000,353000,332000,350000,489967,170290080500,81900000000000,234000000,KOSPI
2024-08-22,351500,364000,348500,363000,474976,171145269000,84942000000000,234000000,KOSPI
2024-09-02,392000,416500,392000,412000,792620,325246395000,96408000000000,234000000,KOSPI
2024-10-08,416500,444000,412000,436500,803706,348252123000,102141000000000,234000000,KOSPI
2025-05-16,305000,307000,290000,290500,583328,171754453500,67977000000000,234000000,KOSPI
```

### 4.2 삼성SDI — 006400

```csv
d,o,h,l,c,v,a,mc,s,m
2024-03-12,421500,461000,421500,459500,1470069,650697201000,31597301535000,68764530,KOSPI
2024-03-25,478000,494500,475000,486000,840495,409179508728,33419561580000,68764530,KOSPI
2024-04-16,387000,391000,384500,386500,245249,94884089000,26577490845000,68764530,KOSPI
2024-07-18,351000,359000,350500,355000,290914,103281416000,24411408150000,68764530,KOSPI
2024-11-15,250000,253500,235500,246500,1275347,310890340500,16950456645000,68764530,KOSPI
```

### 4.3 SK이노베이션 — 096770

```csv
d,o,h,l,c,v,a,mc,s,m
2024-01-31,116100,118800,115700,117100,267405,31387726200,11786766544400,100655564,KOSPI
2024-02-06,129400,130900,120000,120800,1101077,136448129100,12159192131200,100655564,KOSPI
2024-05-31,103100,105900,99600,100000,908750,92134328800,9573559000000,95735590,KOSPI
2024-06-20,113100,126000,112700,121000,8538298,1033741388900,11584006390000,95735590,KOSPI
2024-10-10,119300,125000,116000,123000,788299,96275822800,11775477570000,95735590,KOSPI
```

### 4.4 포스코퓨처엠 — 003670

```csv
d,o,h,l,c,v,a,mc,s,m
2024-02-15,292000,304500,292000,300500,765158,228212172000,23277697610000,77463220,KOSPI
2024-03-13,339500,341000,332500,334500,374120,125934442000,25911447090000,77463220,KOSPI
2024-04-19,255500,257500,247500,253500,274965,69388174000,19636926270000,77463220,KOSPI
2024-08-08,207500,211500,198300,199500,532765,107301473400,15453912390000,77463220,KOSPI
2024-11-04,231000,244000,227500,241000,380256,90967028000,18668636020000,77463220,KOSPI
```

## 5. Trigger-level backtest rows

```jsonl
{"row_type":"trigger_row","research_session":"post_calibrated_sector_archetype_residual_research","mode":"historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12","selected_round":"R11","selected_loop":102,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","fine_archetype_id":"BATTERY_IRA_AMPC_POLICY_SUBSIDY_TO_COMPANY_CASH_BRIDGE_VS_INDIRECT_POLICY_LABEL_FALSE_POSITIVE","case_id":"C31_R11L102_373220_2024_08_21_IRA_AMPC_LOCAL_POSITIVE_REVERSION","symbol":"373220","name":"LG에너지솔루션","market":"KOSPI","trigger_type":"Stage2_Actionable","trigger_family":"direct_policy_subsidy_ramp_local_repricing_with_180D_reversion_guard","entry_date":"2024-08-21","entry_price":350000.0,"entry_price_basis":"close","price_source_repo":"Songdaiki/stock-web","price_source_path":"atlas/ohlcv_tradable_by_symbol_year/373/373220/2024.csv + 2025 continuation","profile_path":"atlas/symbol_profiles/373/373220.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","mfe_30d_pct":19.00,"mae_30d_pct":-0.43,"close_return_30d_pct":15.29,"peak_30d_date":"2024-09-02","trough_30d_date":"2024-08-22","mfe_90d_pct":26.86,"mae_90d_pct":-2.14,"close_return_90d_pct":-1.14,"peak_90d_date":"2024-10-08","trough_90d_date":"2025-01-02","mfe_180d_pct":26.86,"mae_180d_pct":-17.14,"close_return_180d_pct":-17.00,"peak_180d_date":"2024-10-08","trough_180d_date":"2025-05-16","local_4b_watch":true,"full_4b_requires_non_price_evidence":true,"hard_4c":false,"outcome_label":"positive_local_mfe_with_180d_reversion","current_profile_error":"policy_subsidy_headline_can_be_overpromoted_to_green_without_utilization_and_cash_bridge_reversion_guard","recommended_shadow_stage":"Stage2_Actionable_or_Stage3_Yellow_local_only","calibration_usable":true,"corporate_action_window_status":"clean_180D_window","source_proxy_only":true,"evidence_url_pending":true,"dedupe_key":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT|373220|Stage2_Actionable|2024-08-21"}
{"row_type":"trigger_row","research_session":"post_calibrated_sector_archetype_residual_research","mode":"historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12","selected_round":"R11","selected_loop":102,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","fine_archetype_id":"BATTERY_IRA_AMPC_POLICY_SUBSIDY_TO_COMPANY_CASH_BRIDGE_VS_INDIRECT_POLICY_LABEL_FALSE_POSITIVE","case_id":"C31_R11L102_006400_2024_03_12_POLICY_PREMIUM_LABEL_HIGH_MAE","symbol":"006400","name":"삼성SDI","market":"KOSPI","trigger_type":"Stage3_Yellow","trigger_family":"premium_battery_policy_label_without_cashflow_conversion","entry_date":"2024-03-12","entry_price":459500.0,"entry_price_basis":"close","price_source_repo":"Songdaiki/stock-web","price_source_path":"atlas/ohlcv_tradable_by_symbol_year/006/006400/2024.csv","profile_path":"atlas/symbol_profiles/006/006400.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","mfe_30d_pct":7.62,"mae_30d_pct":-16.32,"close_return_30d_pct":-11.43,"peak_30d_date":"2024-03-25","trough_30d_date":"2024-04-16","mfe_90d_pct":7.62,"mae_90d_pct":-23.72,"close_return_90d_pct":-22.20,"peak_90d_date":"2024-03-25","trough_90d_date":"2024-07-18","mfe_180d_pct":7.62,"mae_180d_pct":-48.75,"close_return_180d_pct":-42.87,"peak_180d_date":"2024-03-25","trough_180d_date":"2024-11-15","local_4b_watch":true,"full_4b_requires_non_price_evidence":true,"hard_4c":false,"outcome_label":"counterexample_high_MAE_after_policy_label_rally","current_profile_error":"policy_subsidy_or_premium_customer_label_can_survive_yellow_despite_absent_cash_bridge_and_large_forward_drawdown","recommended_shadow_stage":"Stage2_or_4B_watch_not_Green","calibration_usable":true,"corporate_action_window_status":"clean_180D_window","source_proxy_only":true,"evidence_url_pending":true,"dedupe_key":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT|006400|Stage3_Yellow|2024-03-12"}
{"row_type":"trigger_row","research_session":"post_calibrated_sector_archetype_residual_research","mode":"historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12","selected_round":"R11","selected_loop":102,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","fine_archetype_id":"BATTERY_IRA_AMPC_POLICY_SUBSIDY_TO_COMPANY_CASH_BRIDGE_VS_INDIRECT_POLICY_LABEL_FALSE_POSITIVE","case_id":"C31_R11L102_096770_2024_01_31_POLICY_SUBSIDIARY_PARENT_NOISE_MIXED","symbol":"096770","name":"SK이노베이션","market":"KOSPI","trigger_type":"Stage2_Actionable","trigger_family":"subsidiary_subsidy_benefit_parent_balance_sheet_contamination","entry_date":"2024-01-31","entry_price":117100.0,"entry_price_basis":"close","price_source_repo":"Songdaiki/stock-web","price_source_path":"atlas/ohlcv_tradable_by_symbol_year/096/096770/2024.csv","profile_path":"atlas/symbol_profiles/096/096770.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","mfe_30d_pct":11.78,"mae_30d_pct":-1.71,"close_return_30d_pct":7.26,"peak_30d_date":"2024-02-06","trough_30d_date":"2024-03-06","mfe_90d_pct":11.78,"mae_90d_pct":-14.94,"close_return_90d_pct":-10.25,"peak_90d_date":"2024-02-06","trough_90d_date":"2024-05-31","mfe_180d_pct":11.78,"mae_180d_pct":-18.02,"close_return_180d_pct":-2.31,"peak_180d_date":"2024-02-06","trough_180d_date":"2024-08-08","local_4b_watch":true,"full_4b_requires_non_price_evidence":true,"hard_4c":false,"outcome_label":"mixed_positive_short_mfe_parent_contamination","current_profile_error":"subsidiary_policy_benefit_can_be_overcounted_when_parent_refining_leverage_merger_noise_dominates","recommended_shadow_stage":"Stage2_Actionable_only_until_parent_cash_bridge_verified","calibration_usable":true,"corporate_action_window_status":"clean_180D_window; later 2024-11-20 candidate outside selected 180D window","source_proxy_only":true,"evidence_url_pending":true,"dedupe_key":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT|096770|Stage2_Actionable|2024-01-31"}
{"row_type":"trigger_row","research_session":"post_calibrated_sector_archetype_residual_research","mode":"historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12","selected_round":"R11","selected_loop":102,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","fine_archetype_id":"BATTERY_IRA_AMPC_POLICY_SUBSIDY_TO_COMPANY_CASH_BRIDGE_VS_INDIRECT_POLICY_LABEL_FALSE_POSITIVE","case_id":"C31_R11L102_003670_2024_02_15_INDIRECT_POLICY_LABEL_COUNTER","symbol":"003670","name":"포스코퓨처엠","market":"KOSPI","trigger_type":"Stage3_Yellow","trigger_family":"indirect_IRA_material_policy_label_without_direct_subsidy_cash_capture","entry_date":"2024-02-15","entry_price":300500.0,"entry_price_basis":"close","price_source_repo":"Songdaiki/stock-web","price_source_path":"atlas/ohlcv_tradable_by_symbol_year/003/003670/2024.csv","profile_path":"atlas/symbol_profiles/003/003670.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","mfe_30d_pct":13.48,"mae_30d_pct":-2.00,"close_return_30d_pct":-1.50,"peak_30d_date":"2024-03-13","trough_30d_date":"2024-03-29","mfe_90d_pct":13.48,"mae_90d_pct":-17.64,"close_return_90d_pct":-13.98,"peak_90d_date":"2024-03-13","trough_90d_date":"2024-04-19","mfe_180d_pct":13.48,"mae_180d_pct":-34.01,"close_return_180d_pct":-19.80,"peak_180d_date":"2024-03-13","trough_180d_date":"2024-08-08","local_4b_watch":true,"full_4b_requires_non_price_evidence":true,"hard_4c":false,"outcome_label":"counterexample_indirect_policy_label_high_MAE","current_profile_error":"indirect_IRA_material_policy_label_can_score_like_direct_subsidy_cash_capture_without_offtake_margin_bridge","recommended_shadow_stage":"Stage2_or_4B_watch_unless_customer_offtake_margin_bridge_exists","calibration_usable":true,"corporate_action_window_status":"clean_180D_window","source_proxy_only":true,"evidence_url_pending":true,"dedupe_key":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT|003670|Stage3_Yellow|2024-02-15"}
```

## 6. Score-return alignment stress test

| symbol | current calibrated profile risk | observed path | desired C31 treatment |
|---:|---|---|---|
| 373220 | direct policy/subsidy ramp can be promoted too durably | large local MFE, negative 180D close return | local Stage2-Actionable / Yellow only until utilization + cash conversion persists |
| 006400 | premium battery policy label can preserve Yellow | high MAE and severe 180D loss | cap at Stage2 / 4B watch unless realized subsidy/margin bridge appears |
| 096770 | subsidiary subsidy optionality leaks into parent equity | local bounce, parent noise dominates | parent balance-sheet contamination guard |
| 003670 | indirect policy beneficiary treated like direct cash capture | initial MFE fades into deep drawdown | direct vs indirect subsidy split required |

```jsonl
{"row_type":"score_simulation","profile_proxy":"e2r_2_1_stock_web_calibrated","symbol":"373220","entry_date":"2024-08-21","current_profile_expected_stage":"Stage3_Yellow_to_Green_possible","observed_outcome_label":"positive_local_mfe_with_180d_reversion","raw_component_score":{"policy_or_subsidy_signal":22,"cashflow_bridge":12,"revision_visibility":14,"relative_strength":18,"risk_guard":-4,"total":82},"shadow_rule_effect":"requires subsidy_to_cash_bridge and 180D reversion guard","proposed_stage_after_shadow":"Stage2_Actionable_or_Stage3_Yellow_local_only"}
{"row_type":"score_simulation","profile_proxy":"e2r_2_1_stock_web_calibrated","symbol":"006400","entry_date":"2024-03-12","current_profile_expected_stage":"Stage3_Yellow_possible","observed_outcome_label":"counterexample_high_MAE_after_policy_label_rally","raw_component_score":{"policy_or_subsidy_signal":20,"cashflow_bridge":5,"revision_visibility":8,"relative_strength":15,"risk_guard":-12,"total":66},"shadow_rule_effect":"policy label cannot offset absent cash bridge and high MAE","proposed_stage_after_shadow":"Stage2_or_4B_watch"}
{"row_type":"score_simulation","profile_proxy":"e2r_2_1_stock_web_calibrated","symbol":"096770","entry_date":"2024-01-31","current_profile_expected_stage":"Stage2_Actionable_possible","observed_outcome_label":"mixed_positive_short_mfe_parent_contamination","raw_component_score":{"policy_or_subsidy_signal":18,"cashflow_bridge":8,"revision_visibility":10,"relative_strength":16,"risk_guard":-8,"total":70},"shadow_rule_effect":"parent contamination cap","proposed_stage_after_shadow":"Stage2_Actionable_only"}
{"row_type":"score_simulation","profile_proxy":"e2r_2_1_stock_web_calibrated","symbol":"003670","entry_date":"2024-02-15","current_profile_expected_stage":"Stage3_Yellow_possible","observed_outcome_label":"counterexample_indirect_policy_label_high_MAE","raw_component_score":{"policy_or_subsidy_signal":19,"cashflow_bridge":4,"revision_visibility":9,"relative_strength":16,"risk_guard":-10,"total":64},"shadow_rule_effect":"indirect beneficiary split","proposed_stage_after_shadow":"Stage2_or_4B_watch"}
```

## 7. Aggregate rows

```jsonl
{"row_type":"aggregate","selected_round":"R11","selected_loop":102,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","fine_archetype_id":"BATTERY_IRA_AMPC_POLICY_SUBSIDY_TO_COMPANY_CASH_BRIDGE_VS_INDIRECT_POLICY_LABEL_FALSE_POSITIVE","new_independent_case_count":4,"reused_case_count":0,"same_archetype_new_symbol_count":4,"same_archetype_new_trigger_family_count":4,"calibration_usable_case_count":4,"calibration_usable_trigger_count":4,"positive_case_count":1,"mixed_positive_count":1,"counterexample_count":2,"local_4b_watch_count":3,"current_profile_error_count":4,"median_mfe_30d_pct":12.63,"median_mae_30d_pct":-2.0,"median_mfe_90d_pct":12.63,"median_mae_90d_pct":-16.29,"median_mfe_180d_pct":12.63,"median_mae_180d_pct":-25.99,"high_mae_over_15pct_count":4,"auto_selected_coverage_gap_static_index":"C31 rows 3 -> 7 if accepted; still Priority 0, need 23 to 30","auto_selected_coverage_gap_conversation_local":"prior generated C31 approx 11 rows -> 15 if accepted; still Priority 0, need about 15 to reach 30"}
```

## 8. Shadow rule candidates

```jsonl
{"row_type":"shadow_weight_candidate","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","do_not_propose_new_weight_delta":false,"new_axis_proposed":["C31_POLICY_SUBSIDY_TO_COMPANY_CASH_BRIDGE_REQUIRED","C31_DIRECT_SUBSIDY_CAPTURE_VS_INDIRECT_POLICY_LABEL_SPLIT","C31_POLICY_HEADLINE_LOCAL_4B_180D_REVERSION_GUARD","C31_PARENT_BALANCE_SHEET_CONTAMINATION_GUARD","C31_HIGH_MAE_POLICY_LABEL_GUARD"],"existing_axis_strengthened":["stage2_required_bridge","stage2_actionable_bonus_requires_non_price_bridge","price_only_blowoff_blocks_positive_stage","full_4b_requires_non_price_evidence","local_4b_watch_guard","high_MAE_guardrail"],"existing_axis_weakened":[],"candidate_rule_text":"For C31, policy/subsidy/legislation evidence can unlock Stage2-Actionable only if it maps to a company-level path: direct credit capture, budget appropriation, tariff pass-through, contract award, customer call-off, utilization, margin, or FCF. Indirect policy beneficiaries remain capped at Stage2/4B watch. Strong short-term MFE after a policy label must be split from durable Stage3 if 90D/180D MAE is high or 180D close return turns negative."}
```

## 9. Residual contribution summary

```text
sector_specific_rule_candidate = true
canonical_archetype_rule_candidate = true
loop_contribution_label = canonical_archetype_rule_candidate
```

C31 should act like a customs officer at the border between legislation and earnings. A policy headline can show a passport, but the model should still ask for a work permit: direct cash capture, budget, tariff, contract, adoption, or margin. Without that document, the stock may trade a beautiful local MFE and still fail the 180D inspection.

## 10. Deferred Coding Agent Handoff Prompt

```text
Do not execute this handoff in the research session.

Implement only after multiple C31 MDs are batch-ingested.

Target canonical_archetype_id:
- C31_POLICY_SUBSIDY_LEGISLATION_EVENT

Add or test shadow-rule axes:
1. C31_POLICY_SUBSIDY_TO_COMPANY_CASH_BRIDGE_REQUIRED
2. C31_DIRECT_SUBSIDY_CAPTURE_VS_INDIRECT_POLICY_LABEL_SPLIT
3. C31_POLICY_HEADLINE_LOCAL_4B_180D_REVERSION_GUARD
4. C31_PARENT_BALANCE_SHEET_CONTAMINATION_GUARD
5. C31_HIGH_MAE_POLICY_LABEL_GUARD

Expected behavior:
- Direct policy/subsidy evidence may enable Stage2-Actionable.
- Stage3-Yellow requires company-level conversion evidence.
- Stage3-Green requires realized margin/revision/FCF or tariff/budget/contract confirmation.
- Indirect policy labels and parent-contaminated structures stay capped at Stage2/4B watch.
- Strong MFE with high 90D/180D MAE is local-4B, not durable structural success.
```

## 11. Next research state

```text
completed_round = R11
completed_loop = 102
selection_basis = docs/core/V12_Research_No_Repeat_Index.md + conversation-local generated MD ledger
selected_priority_bucket = Priority 0
round_schedule_status = coverage_index_selected
round_sector_consistency = pass

auto_selected_coverage_gap_static_index = C31 rows 3 -> 7 if accepted; still Priority 0, need 23 to 30
auto_selected_coverage_gap_conversation_local = prior generated C31 approx 11 rows -> 15 if accepted; still Priority 0, need about 15 to reach 30

next_recommended_archetypes =
- C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP_third_pass_to_30
- C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK_second_pass_to_30
- C18_CONSUMER_EXPORT_CHANNEL_REORDER_second_pass_to_30
- C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE_fourth_pass_to_30
- C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE_fourth_pass_to_30
- C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY
```
