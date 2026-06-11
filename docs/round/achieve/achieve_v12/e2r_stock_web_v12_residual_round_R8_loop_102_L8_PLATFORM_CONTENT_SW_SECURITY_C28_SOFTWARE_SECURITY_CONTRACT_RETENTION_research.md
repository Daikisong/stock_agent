---
schema_family: v12_sector_archetype_residual
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
selected_round: R8
selected_loop: 102
large_sector_id: L8_PLATFORM_CONTENT_SW_SECURITY
canonical_archetype_id: C28_SOFTWARE_SECURITY_CONTRACT_RETENTION
fine_archetype_id: SOFTWARE_SECURITY_AI_CONTRACT_RETENTION_FINAL_PASS_TO_30_VS_AI_SECURITY_PRICE_ONLY_BLOWOFF
selection_basis: docs/core/V12_Research_No_Repeat_Index.md + conversation-local generated MD ledger
selected_priority_bucket: Priority 0
round_schedule_status: coverage_index_selected
round_sector_consistency: pass
price_source: Songdaiki/stock-web
price_basis: tradable_raw
price_adjustment_status: raw_unadjusted_marcap
stock_web_manifest_max_date: 2026-02-20
production_scoring_changed: false
shadow_weight_only: true
handoff_prompt_embedded: true
handoff_prompt_executed_now: false
---

# E2R Stock-Web v12 Residual Research — R8/L8/C28 Software·Security Contract Retention

```text
output_file = e2r_stock_web_v12_residual_round_R8_loop_102_L8_PLATFORM_CONTENT_SW_SECURITY_C28_SOFTWARE_SECURITY_CONTRACT_RETENTION_research.md
selected_round = R8
selected_loop = 102
large_sector_id = L8_PLATFORM_CONTENT_SW_SECURITY
canonical_archetype_id = C28_SOFTWARE_SECURITY_CONTRACT_RETENTION
fine_archetype_id = SOFTWARE_SECURITY_AI_CONTRACT_RETENTION_FINAL_PASS_TO_30_VS_AI_SECURITY_PRICE_ONLY_BLOWOFF
```

## 1. Coverage-index selection

`V12_Research_No_Repeat_Index.md` places `C28_SOFTWARE_SECURITY_CONTRACT_RETENTION` in Priority 0 with 18 static representative rows. Conversation-local generated MD ledger already added two C28 passes:

```text
R8/L100 C28: +4 cases = 053800, 067920, 203650, 150900
R8/L101 C28: +4 cases = 136540, 263860, 053300, 184230
conversation_local_C28_estimate_before_this_loop = 26 rows
```

This loop therefore executes `C28_final_pass_to_30`, avoids the above local duplicates, and adds four new independent symbols / trigger families:

```text
new_symbols = 030520, 047560, 290270, 356680
static_index_rows = 18 -> 22 if only static index is counted
conversation_local_rows = 26 -> 30 if accepted
Priority_0_floor_status = reached_by_conversation_local_ledger
```

`C28` is treated as an enterprise software/security contract-retention archetype, not a generic AI/software ticker bucket. The rule being stress-tested: price action around AI/security keyword adoption is only a durable positive if it is backed by recurring contract, ARR/maintenance, renewal/retention, cloud subscription, or margin/revision evidence. Otherwise it must be capped as local 4B or Stage2 false positive.

## 2. Stock-web data basis

```text
price_source = Songdaiki/stock-web
manifest_max_date = 2026-02-20
manifest_min_date = 1995-05-02
tradable_row_count = 14354401
raw_row_count = 15214118
symbol_count = 5414
calibration_shard_root = atlas/ohlcv_tradable_by_symbol_year
price_adjustment_status = raw_unadjusted_marcap
```

All cases below use tradable shards only. Corporate-action candidate windows are checked from `atlas/symbol_profiles/<prefix>/<ticker>.json`. None of the selected 2024 entry-to-D180 windows overlap the listed corporate-action candidate dates.

## 3. Case table

| case_id | symbol | name | trigger family | entry | 180D path label | classification |
|---|---:|---|---|---:|---|---|
| C28-R8-L102-030520-2024-01-19 | 030520 | 한글과컴퓨터 | AI office/software local rerating without subscription retention bridge | 30,450 | +26.27% MFE / -50.41% MAE | counterexample_high_MAE_local_4B |
| C28-R8-L102-047560-2024-01-19 | 047560 | 이스트소프트 | AI software/security label blowoff without recurring margin evidence | 39,100 | +27.37% MFE / -42.20% MAE | counterexample_price_only_blowoff |
| C28-R8-L102-290270-2024-03-26 | 290270 | 휴네시온 | network security theme spike without maintenance renewal leverage | 6,780 | +5.31% MFE / -51.77% MAE | failed_stage2_high_MAE |
| C28-R8-L102-356680-2024-01-26 | 356680 | 엑스게이트 | VPN/security appliance spike without renewal/contract retention proof | 6,410 | +11.39% MFE / -51.64% MAE | failed_stage2_high_MAE |

## 4. Trigger rows

```jsonl
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","case_id":"C28-R8-L102-030520-2024-01-19","same_entry_group_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION:030520:2024-01-19:Stage4B","dedupe_for_aggregate":true,"aggregate_group_role":"representative","selected_round":"R8","selected_loop":102,"large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","fine_archetype_id":"SOFTWARE_SECURITY_AI_CONTRACT_RETENTION_FINAL_PASS_TO_30_VS_AI_SECURITY_PRICE_ONLY_BLOWOFF","symbol":"030520","name":"한글과컴퓨터","trigger_type":"Stage4B","trigger_family":"AI_office_software_local_rerating_without_subscription_retention_bridge","entry_date":"2024-01-19","entry_price":30450.0,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","forward_window_trading_days":180,"MFE_30D_pct":26.27,"MAE_30D_pct":-24.96,"MFE_90D_pct":26.27,"MAE_90D_pct":-35.14,"MFE_180D_pct":26.27,"MAE_180D_pct":-50.41,"peak_180D_price":38450.0,"trough_180D_price":15100.0,"corporate_action_window_status":"not_contaminated","calibration_usable":true,"case_role":"counterexample_high_MAE_local_4B","current_profile_error_type":"AI_software_keyword_can_trigger_stage2_too_high_without_subscription_retention_and_margin_revision_bridge","stage_call":"local 4B only; block Green and cap Stage2 bonus unless ARR/subscription retention is proven","source_proxy_only":true,"evidence_url_pending":true}
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","case_id":"C28-R8-L102-047560-2024-01-19","same_entry_group_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION:047560:2024-01-19:Stage4B","dedupe_for_aggregate":true,"aggregate_group_role":"representative","selected_round":"R8","selected_loop":102,"large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","fine_archetype_id":"SOFTWARE_SECURITY_AI_CONTRACT_RETENTION_FINAL_PASS_TO_30_VS_AI_SECURITY_PRICE_ONLY_BLOWOFF","symbol":"047560","name":"이스트소프트","trigger_type":"Stage4B","trigger_family":"AI_software_security_label_blowoff_without_recurring_margin_evidence","entry_date":"2024-01-19","entry_price":39100.0,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","forward_window_trading_days":180,"MFE_30D_pct":27.37,"MAE_30D_pct":-25.45,"MFE_90D_pct":27.37,"MAE_90D_pct":-42.20,"MFE_180D_pct":27.37,"MAE_180D_pct":-42.20,"peak_180D_price":49800.0,"trough_180D_price":22600.0,"corporate_action_window_status":"not_contaminated","calibration_usable":true,"case_role":"counterexample_price_only_blowoff","current_profile_error_type":"AI_software_price_momentum_mimics_C28_but_lacks_contract_retention_and_margin_revision_evidence","stage_call":"price-only local 4B; do not allow durable Stage3 without renewal/ARR proof","source_proxy_only":true,"evidence_url_pending":true}
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","case_id":"C28-R8-L102-290270-2024-03-26","same_entry_group_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION:290270:2024-03-26:Stage2","dedupe_for_aggregate":true,"aggregate_group_role":"representative","selected_round":"R8","selected_loop":102,"large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","fine_archetype_id":"SOFTWARE_SECURITY_AI_CONTRACT_RETENTION_FINAL_PASS_TO_30_VS_AI_SECURITY_PRICE_ONLY_BLOWOFF","symbol":"290270","name":"휴네시온","trigger_type":"Stage2","trigger_family":"network_security_theme_spike_without_maintenance_renewal_leverage","entry_date":"2024-03-26","entry_price":6780.0,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","forward_window_trading_days":180,"MFE_30D_pct":5.31,"MAE_30D_pct":-14.31,"MFE_90D_pct":5.31,"MAE_90D_pct":-43.95,"MFE_180D_pct":5.31,"MAE_180D_pct":-51.77,"peak_180D_price":7140.0,"trough_180D_price":3270.0,"corporate_action_window_status":"not_contaminated","calibration_usable":true,"case_role":"failed_stage2_high_MAE","current_profile_error_type":"network_security_label_without_contract_renewal_visibility_creates_stage2_false_positive","stage_call":"Stage2 false positive; require maintenance renewal and margin bridge before actionable stage","source_proxy_only":true,"evidence_url_pending":true}
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","case_id":"C28-R8-L102-356680-2024-01-26","same_entry_group_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION:356680:2024-01-26:Stage2","dedupe_for_aggregate":true,"aggregate_group_role":"representative","selected_round":"R8","selected_loop":102,"large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","fine_archetype_id":"SOFTWARE_SECURITY_AI_CONTRACT_RETENTION_FINAL_PASS_TO_30_VS_AI_SECURITY_PRICE_ONLY_BLOWOFF","symbol":"356680","name":"엑스게이트","trigger_type":"Stage2","trigger_family":"VPN_security_appliance_spike_without_renewal_contract_retention_proof","entry_date":"2024-01-26","entry_price":6410.0,"price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","forward_window_trading_days":180,"MFE_30D_pct":11.39,"MAE_30D_pct":-15.76,"MFE_90D_pct":11.39,"MAE_90D_pct":-15.76,"MFE_180D_pct":11.39,"MAE_180D_pct":-51.64,"peak_180D_price":7140.0,"trough_180D_price":3100.0,"corporate_action_window_status":"not_contaminated","calibration_usable":true,"case_role":"failed_stage2_high_MAE","current_profile_error_type":"security_appliance_theme_can_score_as_contract_retention_but_reverts_without_recurring_revenue_visibility","stage_call":"Stage2 false positive; local 4B/4C watch only until renewal and contract margin evidence appears","source_proxy_only":true,"evidence_url_pending":true}
```

## 5. Residual finding

C28 needs a stricter split than a broad software/security label. In all four new cases, the price path gives the appearance of a software or cyber-security rerating, but the subsequent drawdown says the same thing in a colder language: a single price flare is not the same as recurring contract retention.

```text
core_residual_error = current_profile_can_overreward_AI_or_security_keyword_momentum_without_retention_bridge
positive_requirement = recurring_contract_or_subscription_retention + margin/revision bridge + cash conversion visibility
counterexample_guard = AI/security price spike without renewal/ARR/maintenance evidence remains local 4B or Stage2-watch
```

## 6. Proposed axis

```text
new_axis_proposed = C28_contract_retention_ARR_margin_bridge_required
new_axis_proposed += C28_AI_security_price_only_local_4B_cap
new_axis_proposed += C28_security_appliance_without_renewal_high_MAE_guard
new_axis_proposed += C28_software_theme_requires_subscription_retention_or_operating_leverage
existing_axis_strengthened = stage2_required_bridge | price_only_blowoff_blocks_positive_stage | full_4b_requires_non_price_evidence | local_4b_watch_guard | high_MAE_guardrail
existing_axis_weakened = null
```

Suggested scoring treatment:

```text
if canonical_archetype_id == C28_SOFTWARE_SECURITY_CONTRACT_RETENTION:
    if evidence_family in [AI_keyword, security_keyword, cyber_policy_theme, appliance_theme] and no ARR/renewal/retention/margin bridge:
        cap_stage = local_4B_or_Stage2_watch
        block_stage3_green = true
        apply_high_MAE_guard = true

    if recurring_revenue_retention_visible and renewal/maintenance/ARR is tied to margin revision:
        allow_stage2_actionable = true
        allow_yellow_candidate = true
        green_requires_non_price_revision_or_cash_conversion = true
```

## 7. Aggregate metric

```jsonl
{"row_type":"aggregate_metric","selected_round":"R8","selected_loop":102,"large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","fine_archetype_id":"SOFTWARE_SECURITY_AI_CONTRACT_RETENTION_FINAL_PASS_TO_30_VS_AI_SECURITY_PRICE_ONLY_BLOWOFF","representative_trigger_count":4,"calibration_usable_trigger_count":4,"positive_case_count":0,"mixed_positive_count":0,"counterexample_count":4,"local_4b_watch_count":4,"current_profile_error_count":4,"median_MFE_180D_pct":19.38,"median_MAE_180D_pct":-51.03,"new_axis_proposed":"C28_contract_retention_ARR_margin_bridge_required | C28_AI_security_price_only_local_4B_cap | C28_security_appliance_without_renewal_high_MAE_guard | C28_software_theme_requires_subscription_retention_or_operating_leverage","existing_axis_strengthened":"stage2_required_bridge | price_only_blowoff_blocks_positive_stage | full_4b_requires_non_price_evidence | local_4b_watch_guard | high_MAE_guardrail"}
```

## 8. Residual contribution

```jsonl
{"row_type":"residual_contribution","selected_round":"R8","selected_loop":102,"large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","loop_contribution_label":"canonical_archetype_rule_candidate","residual_error_found":true,"new_independent_case_count":4,"reused_case_count":0,"same_archetype_new_symbol_count":4,"same_archetype_new_trigger_family_count":4,"description":"C28 final pass to 30: separate durable enterprise software/security retention from AI/security price-only blowoff. New cases show high-MAE reversals when ARR, renewal, retention, maintenance contract, or margin revision evidence is missing."}
```

## 9. Next research state

```text
completed_round = R8
completed_loop = 102
selection_basis = docs/core/V12_Research_No_Repeat_Index.md + conversation-local generated MD ledger
selected_priority_bucket = Priority 0
round_schedule_status = coverage_index_selected
round_sector_consistency = pass
new_independent_case_count = 4
reused_case_count = 0
same_archetype_new_symbol_count = 4
same_archetype_new_trigger_family_count = 4
calibration_usable case 수 = 4
calibration_usable trigger 수 = 4
positive_case_count = 0
mixed_positive_count = 0
counterexample_count = 4
local_4b_watch_count = 4
current_profile_error_count = 4
auto_selected_coverage_gap_static_index = C28 rows 18 -> 22 if accepted
auto_selected_coverage_gap_conversation_local = C28 rows 26 -> 30 if accepted; C28 30-row Priority 0 floor 도달
sector_specific_rule_candidate = true
canonical_archetype_rule_candidate = true
loop_contribution_label = canonical_archetype_rule_candidate
do_not_propose_new_weight_delta = false
next_recommended_archetypes = C19_BRAND_RETAIL_INVENTORY_MARGIN, C27_CONTENT_IP_GLOBAL_MONETIZATION, R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL, C18_CONSUMER_EXPORT_CHANNEL_REORDER, C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE
```
