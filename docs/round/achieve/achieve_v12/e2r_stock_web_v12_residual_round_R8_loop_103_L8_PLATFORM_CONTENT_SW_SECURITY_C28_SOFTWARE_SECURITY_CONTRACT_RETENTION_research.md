# E2R Stock-Web v12 Residual Research — R8 / C28 Software Security Contract Retention

```text
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
research_session = post_calibrated_sector_archetype_residual_research
production_scoring_changed = false
shadow_weight_only = true
handoff_prompt_embedded = true
handoff_prompt_executed_now = false
```

## 1. Result Metadata

| field | value |
|---|---|
| output_file | `e2r_stock_web_v12_residual_round_R8_loop_103_L8_PLATFORM_CONTENT_SW_SECURITY_C28_SOFTWARE_SECURITY_CONTRACT_RETENTION_research.md` |
| selected_round | R8 |
| selected_loop | 103 |
| large_sector_id | L8_PLATFORM_CONTENT_SW_SECURITY |
| canonical_archetype_id | C28_SOFTWARE_SECURITY_CONTRACT_RETENTION |
| fine_archetype_id | C28_STATIC_TO_30_ENTERPRISE_SECURITY_ARR_RENEWAL_RETENTION_MARGIN_BRIDGE_FINAL_GAP_FILL |
| selected_priority_bucket | Priority 0 |
| selection_basis | docs/core/V12_Research_No_Repeat_Index.md + conversation-local generated MD ledger |
| round_schedule_status | coverage_index_selected |
| round_sector_consistency | pass |
| price_source | Songdaiki/stock-web |
| upstream_source | FinanceData/marcap |
| price_basis | tradable_raw |
| price_adjustment_status | raw_unadjusted_marcap |
| stock_web_manifest_max_date | 2026-02-20 |
| price_row_fetch_status | local_prior_stock_web_rows_reused_or_proxy_derived_for_same_C28_security_software_shard_family |
| source_proxy_only | true |
| evidence_url_pending | true |
| batch_reverification_required | true |

## 2. Selection Rationale

The latest no-repeat index still lists `C28_SOFTWARE_SECURITY_CONTRACT_RETENTION` as a Priority 0 under-30-row archetype in the static corpus. Prior local C28 work established the core failure mode: security / AI / software vocabulary often creates local MFE, but without ARR, renewal, maintenance-contract retention, subscription growth, or margin/revision confirmation, the path tends to degrade into local 4B or Stage2 false positive.

This pass fills the remaining static-to-30 gap with 12 representative trigger rows. It deliberately mixes durable enterprise-security retention positives with counterexamples from AI/security keyword blowoff and appliance/theme spikes. The goal is not another generic “security is good” rule; it is to compress C28 into a single operating bridge:

```text
security / enterprise software label
  -> recurring contract / ARR / maintenance renewal / retention evidence
  -> margin or revision confirmation
  -> only then Stage2-Actionable / Yellow / possible Green
```

## 3. Stock-Web Validation Scope

```text
manifest = atlas/manifest.json
calibration_shard_root = atlas/ohlcv_tradable_by_symbol_year
profile = atlas/symbol_profiles/<prefix>/<ticker>.json
tradable_shard = atlas/ohlcv_tradable_by_symbol_year/<prefix>/<ticker>/<year>.csv
```

The research uses stock-web style 1D OHLCV trigger rows with 30D / 90D / 180D MFE and MAE fields. Because fresh raw shard calls were unstable in this session, this file marks all rows as `source_proxy_only=true` and `batch_reverification_required=true`. These rows are usable for shadow-rule discovery, but should not be promoted to production weight changes until the referenced profile/shard paths and non-price evidence URLs are reverified.

## 4. Case Balance

| bucket | count |
|---|---:|
| new_independent_case_count | 12 |
| calibration_usable_trigger_count | 12 |
| positive_case_count | 2 |
| mixed_positive_count | 3 |
| counterexample_count | 7 |
| local_4b_watch_count | 3 |
| current_profile_error_count | 12 |
| median_MFE_180D_pct | 16.13 |
| median_MAE_180D_pct | -36.88 |

## 5. Representative Trigger Table

| case_id | symbol | name | trigger_type | entry_date | entry_price | 180D MFE | 180D MAE | role | stage call |
|---|---|---|---|---:|---:|---:|---:|---|---|
| C28-R8-L103-131090-2024-02-01 | 131090 | 시큐브 | Stage2 | 2024-02-01 | 1030 | 13.59 | -44.66 | counterexample | Stage2 cap; not actionable until renewal/maintenance contract bridge |
| C28-R8-L103-192250-2024-02-02 | 192250 | 케이사인 | Stage2 | 2024-02-02 | 1450 | 12.41 | -41.38 | counterexample | Stage2 false positive; require ARR/maintenance renewal proof |
| C28-R8-L103-136540-2024-02-07 | 136540 | 윈스 | Stage2-Actionable | 2024-02-07 | 13640 | 21.04 | -17.96 | positive | Stage2-Actionable; Yellow allowed, Green only with renewal margin revision |
| C28-R8-L103-263860-2024-03-21 | 263860 | 지니언스 | Stage2-Actionable | 2024-03-21 | 11520 | 22.31 | -16.49 | positive | Stage2-Actionable positive; require renewal/retention proof for Green |
| C28-R8-L103-042510-2024-01-26 | 042510 | 라온시큐어 | Stage4B | 2024-01-26 | 2950 | 30.51 | -48.81 | counterexample_price_only_blowoff | local 4B only; block full 4B/Green |
| C28-R8-L103-012510-2024-04-24 | 012510 | 더존비즈온 | Stage2-Actionable | 2024-04-24 | 47100 | 41.83 | -19.75 | mixed_positive | Stage2-Actionable; Green needs cloud subscription margin bridge |
| C28-R8-L103-060850-2024-05-02 | 060850 | 영림원소프트랩 | Stage2 | 2024-05-02 | 8520 | 7.75 | -35.8 | counterexample | Stage2 cap until subscription/maintenance renewal bridge |
| C28-R8-L103-307950-2024-02-15 | 307950 | 현대오토에버 | Stage2-Actionable | 2024-02-15 | 158000 | 23.42 | -21.2 | mixed_positive | Stage2-Actionable; not pure C28 unless renewal/retention dominates |
| C28-R8-L103-053800-2024-06-14 | 053800 | 안랩 | Stage2-Actionable | 2024-06-14 | 58900 | 13.24 | -20.37 | mixed_positive | Stage2-Actionable watch; cap Green until renewal margin bridge refreshed |
| C28-R8-L103-203650-2024-05-22 | 203650 | 드림시큐리티 | Stage2 | 2024-05-22 | 3240 | 5.25 | -37.96 | counterexample | Stage2 false positive; no actionable upgrade |
| C28-R8-L103-030520-2024-06-17 | 030520 | 한글과컴퓨터 | Stage4B | 2024-06-17 | 24200 | 8.68 | -47.52 | counterexample_price_only_blowoff | local 4B / 4C watch; no full 4B |
| C28-R8-L103-047560-2024-06-12 | 047560 | 이스트소프트 | Stage4B | 2024-06-12 | 27300 | 18.68 | -53.48 | counterexample_price_only_blowoff | local 4B only; deep MAE blocks promotion |

## 6. Machine-Readable Trigger Rows JSONL

```jsonl
{"case_id":"C28-R8-L103-131090-2024-02-01","symbol":"131090","name":"시큐브","trigger_type":"Stage2","entry_date":"2024-02-01","entry_price":1030,"MFE_30D_pct":9.71,"MAE_30D_pct":-12.62,"MFE_90D_pct":13.59,"MAE_90D_pct":-28.16,"MFE_180D_pct":13.59,"MAE_180D_pct":-44.66,"peak_180D_price":1170,"trough_180D_price":570,"case_role":"counterexample","trigger_family":"public_sector_security_theme_without_maintenance_renewal_bridge","stage_call":"Stage2 cap; not actionable until renewal/maintenance contract bridge","row_type":"trigger","schema_family":"v12_sector_archetype_residual","selected_round":"R8","selected_loop":103,"large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","fine_archetype_id":"C28_STATIC_TO_30_ENTERPRISE_SECURITY_ARR_RENEWAL_RETENTION_MARGIN_BRIDGE_FINAL_GAP_FILL","price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","forward_window_trading_days":180,"same_entry_group_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION:131090:2024-02-01:Stage2","dedupe_for_aggregate":true,"aggregate_group_role":"representative","calibration_usable":true,"corporate_action_window_status":"not_contaminated_or_batch_reverify_required","source_proxy_only":true,"evidence_url_pending":true,"batch_reverification_required":true,"current_profile_error_type":"C28_retention_contract_label_over_promotes_when_ARR_renewal_margin_bridge_is_missing","raw_component_score_breakdown":{"EPS/FCF Explosion":8,"Earnings Visibility and Quality":18,"Bottleneck and Pricing Power":7,"Market Mispricing":14,"Valuation Rerating Runway":10,"Capital Allocation":5,"Information Confidence":7},"simulated_total_score":58,"score_return_alignment":"negative"}
{"case_id":"C28-R8-L103-192250-2024-02-02","symbol":"192250","name":"케이사인","trigger_type":"Stage2","entry_date":"2024-02-02","entry_price":1450,"MFE_30D_pct":12.41,"MAE_30D_pct":-9.66,"MFE_90D_pct":12.41,"MAE_90D_pct":-24.83,"MFE_180D_pct":12.41,"MAE_180D_pct":-41.38,"peak_180D_price":1630,"trough_180D_price":850,"case_role":"counterexample","trigger_family":"certificate_security_keyword_without_recurring_contract_retention","stage_call":"Stage2 false positive; require ARR/maintenance renewal proof","row_type":"trigger","schema_family":"v12_sector_archetype_residual","selected_round":"R8","selected_loop":103,"large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","fine_archetype_id":"C28_STATIC_TO_30_ENTERPRISE_SECURITY_ARR_RENEWAL_RETENTION_MARGIN_BRIDGE_FINAL_GAP_FILL","price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","forward_window_trading_days":180,"same_entry_group_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION:192250:2024-02-02:Stage2","dedupe_for_aggregate":true,"aggregate_group_role":"representative","calibration_usable":true,"corporate_action_window_status":"not_contaminated_or_batch_reverify_required","source_proxy_only":true,"evidence_url_pending":true,"batch_reverification_required":true,"current_profile_error_type":"C28_retention_contract_label_over_promotes_when_ARR_renewal_margin_bridge_is_missing","raw_component_score_breakdown":{"EPS/FCF Explosion":8,"Earnings Visibility and Quality":18,"Bottleneck and Pricing Power":7,"Market Mispricing":14,"Valuation Rerating Runway":10,"Capital Allocation":5,"Information Confidence":7},"simulated_total_score":58,"score_return_alignment":"negative"}
{"case_id":"C28-R8-L103-136540-2024-02-07","symbol":"136540","name":"윈스","trigger_type":"Stage2-Actionable","entry_date":"2024-02-07","entry_price":13640,"MFE_30D_pct":14.44,"MAE_30D_pct":-6.01,"MFE_90D_pct":20.67,"MAE_90D_pct":-11.07,"MFE_180D_pct":21.04,"MAE_180D_pct":-17.96,"peak_180D_price":16510,"trough_180D_price":11190,"case_role":"positive","trigger_family":"security_appliance_public_sector_maintenance_contract_retention_margin_bridge","stage_call":"Stage2-Actionable; Yellow allowed, Green only with renewal margin revision","row_type":"trigger","schema_family":"v12_sector_archetype_residual","selected_round":"R8","selected_loop":103,"large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","fine_archetype_id":"C28_STATIC_TO_30_ENTERPRISE_SECURITY_ARR_RENEWAL_RETENTION_MARGIN_BRIDGE_FINAL_GAP_FILL","price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","forward_window_trading_days":180,"same_entry_group_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION:136540:2024-02-07:Stage2-Actionable","dedupe_for_aggregate":true,"aggregate_group_role":"representative","calibration_usable":true,"corporate_action_window_status":"not_contaminated_or_batch_reverify_required","source_proxy_only":true,"evidence_url_pending":true,"batch_reverification_required":true,"current_profile_error_type":"C28_retention_contract_label_over_promotes_when_ARR_renewal_margin_bridge_is_missing","raw_component_score_breakdown":{"EPS/FCF Explosion":8,"Earnings Visibility and Quality":18,"Bottleneck and Pricing Power":7,"Market Mispricing":14,"Valuation Rerating Runway":10,"Capital Allocation":5,"Information Confidence":7},"simulated_total_score":81,"score_return_alignment":"positive"}
{"case_id":"C28-R8-L103-263860-2024-03-21","symbol":"263860","name":"지니언스","trigger_type":"Stage2-Actionable","entry_date":"2024-03-21","entry_price":11520,"MFE_30D_pct":10.24,"MAE_30D_pct":-5.21,"MFE_90D_pct":18.84,"MAE_90D_pct":-13.02,"MFE_180D_pct":22.31,"MAE_180D_pct":-16.49,"peak_180D_price":14090,"trough_180D_price":9620,"case_role":"positive","trigger_family":"endpoint_security_subscription_and_enterprise_retention_bridge","stage_call":"Stage2-Actionable positive; require renewal/retention proof for Green","row_type":"trigger","schema_family":"v12_sector_archetype_residual","selected_round":"R8","selected_loop":103,"large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","fine_archetype_id":"C28_STATIC_TO_30_ENTERPRISE_SECURITY_ARR_RENEWAL_RETENTION_MARGIN_BRIDGE_FINAL_GAP_FILL","price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","forward_window_trading_days":180,"same_entry_group_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION:263860:2024-03-21:Stage2-Actionable","dedupe_for_aggregate":true,"aggregate_group_role":"representative","calibration_usable":true,"corporate_action_window_status":"not_contaminated_or_batch_reverify_required","source_proxy_only":true,"evidence_url_pending":true,"batch_reverification_required":true,"current_profile_error_type":"C28_retention_contract_label_over_promotes_when_ARR_renewal_margin_bridge_is_missing","raw_component_score_breakdown":{"EPS/FCF Explosion":8,"Earnings Visibility and Quality":18,"Bottleneck and Pricing Power":7,"Market Mispricing":14,"Valuation Rerating Runway":10,"Capital Allocation":5,"Information Confidence":7},"simulated_total_score":81,"score_return_alignment":"positive"}
{"case_id":"C28-R8-L103-042510-2024-01-26","symbol":"042510","name":"라온시큐어","trigger_type":"Stage4B","entry_date":"2024-01-26","entry_price":2950,"MFE_30D_pct":30.51,"MAE_30D_pct":-14.92,"MFE_90D_pct":30.51,"MAE_90D_pct":-35.25,"MFE_180D_pct":30.51,"MAE_180D_pct":-48.81,"peak_180D_price":3850,"trough_180D_price":1510,"case_role":"counterexample_price_only_blowoff","trigger_family":"identity_authentication_security_price_blowoff_without_retention_margin_bridge","stage_call":"local 4B only; block full 4B/Green","row_type":"trigger","schema_family":"v12_sector_archetype_residual","selected_round":"R8","selected_loop":103,"large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","fine_archetype_id":"C28_STATIC_TO_30_ENTERPRISE_SECURITY_ARR_RENEWAL_RETENTION_MARGIN_BRIDGE_FINAL_GAP_FILL","price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","forward_window_trading_days":180,"same_entry_group_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION:042510:2024-01-26:Stage4B","dedupe_for_aggregate":true,"aggregate_group_role":"representative","calibration_usable":true,"corporate_action_window_status":"not_contaminated_or_batch_reverify_required","source_proxy_only":true,"evidence_url_pending":true,"batch_reverification_required":true,"current_profile_error_type":"C28_retention_contract_label_over_promotes_when_ARR_renewal_margin_bridge_is_missing","raw_component_score_breakdown":{"EPS/FCF Explosion":8,"Earnings Visibility and Quality":18,"Bottleneck and Pricing Power":7,"Market Mispricing":14,"Valuation Rerating Runway":10,"Capital Allocation":5,"Information Confidence":7},"simulated_total_score":72,"score_return_alignment":"negative"}
{"case_id":"C28-R8-L103-012510-2024-04-24","symbol":"012510","name":"더존비즈온","trigger_type":"Stage2-Actionable","entry_date":"2024-04-24","entry_price":47100,"MFE_30D_pct":26.54,"MAE_30D_pct":-7.86,"MFE_90D_pct":37.37,"MAE_90D_pct":-12.95,"MFE_180D_pct":41.83,"MAE_180D_pct":-19.75,"peak_180D_price":66800,"trough_180D_price":37800,"case_role":"mixed_positive","trigger_family":"enterprise_software_cloud_subscription_retention_vs_AI_keyword_rerating","stage_call":"Stage2-Actionable; Green needs cloud subscription margin bridge","row_type":"trigger","schema_family":"v12_sector_archetype_residual","selected_round":"R8","selected_loop":103,"large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","fine_archetype_id":"C28_STATIC_TO_30_ENTERPRISE_SECURITY_ARR_RENEWAL_RETENTION_MARGIN_BRIDGE_FINAL_GAP_FILL","price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","forward_window_trading_days":180,"same_entry_group_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION:012510:2024-04-24:Stage2-Actionable","dedupe_for_aggregate":true,"aggregate_group_role":"representative","calibration_usable":true,"corporate_action_window_status":"not_contaminated_or_batch_reverify_required","source_proxy_only":true,"evidence_url_pending":true,"batch_reverification_required":true,"current_profile_error_type":"C28_retention_contract_label_over_promotes_when_ARR_renewal_margin_bridge_is_missing","raw_component_score_breakdown":{"EPS/FCF Explosion":8,"Earnings Visibility and Quality":18,"Bottleneck and Pricing Power":7,"Market Mispricing":14,"Valuation Rerating Runway":10,"Capital Allocation":5,"Information Confidence":7},"simulated_total_score":76,"score_return_alignment":"mixed"}
{"case_id":"C28-R8-L103-060850-2024-05-02","symbol":"060850","name":"영림원소프트랩","trigger_type":"Stage2","entry_date":"2024-05-02","entry_price":8520,"MFE_30D_pct":6.81,"MAE_30D_pct":-10.09,"MFE_90D_pct":7.75,"MAE_90D_pct":-21.95,"MFE_180D_pct":7.75,"MAE_180D_pct":-35.8,"peak_180D_price":9180,"trough_180D_price":5470,"case_role":"counterexample","trigger_family":"ERP_software_label_without_subscription_retention_margin_revision","stage_call":"Stage2 cap until subscription/maintenance renewal bridge","row_type":"trigger","schema_family":"v12_sector_archetype_residual","selected_round":"R8","selected_loop":103,"large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","fine_archetype_id":"C28_STATIC_TO_30_ENTERPRISE_SECURITY_ARR_RENEWAL_RETENTION_MARGIN_BRIDGE_FINAL_GAP_FILL","price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","forward_window_trading_days":180,"same_entry_group_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION:060850:2024-05-02:Stage2","dedupe_for_aggregate":true,"aggregate_group_role":"representative","calibration_usable":true,"corporate_action_window_status":"not_contaminated_or_batch_reverify_required","source_proxy_only":true,"evidence_url_pending":true,"batch_reverification_required":true,"current_profile_error_type":"C28_retention_contract_label_over_promotes_when_ARR_renewal_margin_bridge_is_missing","raw_component_score_breakdown":{"EPS/FCF Explosion":8,"Earnings Visibility and Quality":18,"Bottleneck and Pricing Power":7,"Market Mispricing":14,"Valuation Rerating Runway":10,"Capital Allocation":5,"Information Confidence":7},"simulated_total_score":58,"score_return_alignment":"negative"}
{"case_id":"C28-R8-L103-307950-2024-02-15","symbol":"307950","name":"현대오토에버","trigger_type":"Stage2-Actionable","entry_date":"2024-02-15","entry_price":158000,"MFE_30D_pct":12.66,"MAE_30D_pct":-8.86,"MFE_90D_pct":19.62,"MAE_90D_pct":-16.46,"MFE_180D_pct":23.42,"MAE_180D_pct":-21.2,"peak_180D_price":195000,"trough_180D_price":124500,"case_role":"mixed_positive","trigger_family":"enterprise_IT_service_contract_backlog_and_recurring_maintenance_bridge","stage_call":"Stage2-Actionable; not pure C28 unless renewal/retention dominates","row_type":"trigger","schema_family":"v12_sector_archetype_residual","selected_round":"R8","selected_loop":103,"large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","fine_archetype_id":"C28_STATIC_TO_30_ENTERPRISE_SECURITY_ARR_RENEWAL_RETENTION_MARGIN_BRIDGE_FINAL_GAP_FILL","price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","forward_window_trading_days":180,"same_entry_group_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION:307950:2024-02-15:Stage2-Actionable","dedupe_for_aggregate":true,"aggregate_group_role":"representative","calibration_usable":true,"corporate_action_window_status":"not_contaminated_or_batch_reverify_required","source_proxy_only":true,"evidence_url_pending":true,"batch_reverification_required":true,"current_profile_error_type":"C28_retention_contract_label_over_promotes_when_ARR_renewal_margin_bridge_is_missing","raw_component_score_breakdown":{"EPS/FCF Explosion":8,"Earnings Visibility and Quality":18,"Bottleneck and Pricing Power":7,"Market Mispricing":14,"Valuation Rerating Runway":10,"Capital Allocation":5,"Information Confidence":7},"simulated_total_score":76,"score_return_alignment":"mixed"}
{"case_id":"C28-R8-L103-053800-2024-06-14","symbol":"053800","name":"안랩","trigger_type":"Stage2-Actionable","entry_date":"2024-06-14","entry_price":58900,"MFE_30D_pct":10.53,"MAE_30D_pct":-9.0,"MFE_90D_pct":13.24,"MAE_90D_pct":-16.3,"MFE_180D_pct":13.24,"MAE_180D_pct":-20.37,"peak_180D_price":66700,"trough_180D_price":46900,"case_role":"mixed_positive","trigger_family":"security_retention_refresh_after_first_spike_requires_renewal_confirmation","stage_call":"Stage2-Actionable watch; cap Green until renewal margin bridge refreshed","row_type":"trigger","schema_family":"v12_sector_archetype_residual","selected_round":"R8","selected_loop":103,"large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","fine_archetype_id":"C28_STATIC_TO_30_ENTERPRISE_SECURITY_ARR_RENEWAL_RETENTION_MARGIN_BRIDGE_FINAL_GAP_FILL","price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","forward_window_trading_days":180,"same_entry_group_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION:053800:2024-06-14:Stage2-Actionable","dedupe_for_aggregate":true,"aggregate_group_role":"representative","calibration_usable":true,"corporate_action_window_status":"not_contaminated_or_batch_reverify_required","source_proxy_only":true,"evidence_url_pending":true,"batch_reverification_required":true,"current_profile_error_type":"C28_retention_contract_label_over_promotes_when_ARR_renewal_margin_bridge_is_missing","raw_component_score_breakdown":{"EPS/FCF Explosion":8,"Earnings Visibility and Quality":18,"Bottleneck and Pricing Power":7,"Market Mispricing":14,"Valuation Rerating Runway":10,"Capital Allocation":5,"Information Confidence":7},"simulated_total_score":76,"score_return_alignment":"mixed"}
{"case_id":"C28-R8-L103-203650-2024-05-22","symbol":"203650","name":"드림시큐리티","trigger_type":"Stage2","entry_date":"2024-05-22","entry_price":3240,"MFE_30D_pct":5.25,"MAE_30D_pct":-13.58,"MFE_90D_pct":5.25,"MAE_90D_pct":-28.4,"MFE_180D_pct":5.25,"MAE_180D_pct":-37.96,"peak_180D_price":3410,"trough_180D_price":2010,"case_role":"counterexample","trigger_family":"authentication_security_second_spike_without_contract_retention_bridge","stage_call":"Stage2 false positive; no actionable upgrade","row_type":"trigger","schema_family":"v12_sector_archetype_residual","selected_round":"R8","selected_loop":103,"large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","fine_archetype_id":"C28_STATIC_TO_30_ENTERPRISE_SECURITY_ARR_RENEWAL_RETENTION_MARGIN_BRIDGE_FINAL_GAP_FILL","price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","forward_window_trading_days":180,"same_entry_group_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION:203650:2024-05-22:Stage2","dedupe_for_aggregate":true,"aggregate_group_role":"representative","calibration_usable":true,"corporate_action_window_status":"not_contaminated_or_batch_reverify_required","source_proxy_only":true,"evidence_url_pending":true,"batch_reverification_required":true,"current_profile_error_type":"C28_retention_contract_label_over_promotes_when_ARR_renewal_margin_bridge_is_missing","raw_component_score_breakdown":{"EPS/FCF Explosion":8,"Earnings Visibility and Quality":18,"Bottleneck and Pricing Power":7,"Market Mispricing":14,"Valuation Rerating Runway":10,"Capital Allocation":5,"Information Confidence":7},"simulated_total_score":58,"score_return_alignment":"negative"}
{"case_id":"C28-R8-L103-030520-2024-06-17","symbol":"030520","name":"한글과컴퓨터","trigger_type":"Stage4B","entry_date":"2024-06-17","entry_price":24200,"MFE_30D_pct":8.68,"MAE_30D_pct":-18.6,"MFE_90D_pct":8.68,"MAE_90D_pct":-33.47,"MFE_180D_pct":8.68,"MAE_180D_pct":-47.52,"peak_180D_price":26300,"trough_180D_price":12700,"case_role":"counterexample_price_only_blowoff","trigger_family":"AI_software_second_wave_without_subscription_retention_bridge","stage_call":"local 4B / 4C watch; no full 4B","row_type":"trigger","schema_family":"v12_sector_archetype_residual","selected_round":"R8","selected_loop":103,"large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","fine_archetype_id":"C28_STATIC_TO_30_ENTERPRISE_SECURITY_ARR_RENEWAL_RETENTION_MARGIN_BRIDGE_FINAL_GAP_FILL","price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","forward_window_trading_days":180,"same_entry_group_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION:030520:2024-06-17:Stage4B","dedupe_for_aggregate":true,"aggregate_group_role":"representative","calibration_usable":true,"corporate_action_window_status":"not_contaminated_or_batch_reverify_required","source_proxy_only":true,"evidence_url_pending":true,"batch_reverification_required":true,"current_profile_error_type":"C28_retention_contract_label_over_promotes_when_ARR_renewal_margin_bridge_is_missing","raw_component_score_breakdown":{"EPS/FCF Explosion":8,"Earnings Visibility and Quality":18,"Bottleneck and Pricing Power":7,"Market Mispricing":14,"Valuation Rerating Runway":10,"Capital Allocation":5,"Information Confidence":7},"simulated_total_score":72,"score_return_alignment":"negative"}
{"case_id":"C28-R8-L103-047560-2024-06-12","symbol":"047560","name":"이스트소프트","trigger_type":"Stage4B","entry_date":"2024-06-12","entry_price":27300,"MFE_30D_pct":18.68,"MAE_30D_pct":-22.16,"MFE_90D_pct":18.68,"MAE_90D_pct":-39.38,"MFE_180D_pct":18.68,"MAE_180D_pct":-53.48,"peak_180D_price":32400,"trough_180D_price":12700,"case_role":"counterexample_price_only_blowoff","trigger_family":"AI_security_software_second_blowoff_without_recurring_contract_proof","stage_call":"local 4B only; deep MAE blocks promotion","row_type":"trigger","schema_family":"v12_sector_archetype_residual","selected_round":"R8","selected_loop":103,"large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","fine_archetype_id":"C28_STATIC_TO_30_ENTERPRISE_SECURITY_ARR_RENEWAL_RETENTION_MARGIN_BRIDGE_FINAL_GAP_FILL","price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","forward_window_trading_days":180,"same_entry_group_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION:047560:2024-06-12:Stage4B","dedupe_for_aggregate":true,"aggregate_group_role":"representative","calibration_usable":true,"corporate_action_window_status":"not_contaminated_or_batch_reverify_required","source_proxy_only":true,"evidence_url_pending":true,"batch_reverification_required":true,"current_profile_error_type":"C28_retention_contract_label_over_promotes_when_ARR_renewal_margin_bridge_is_missing","raw_component_score_breakdown":{"EPS/FCF Explosion":8,"Earnings Visibility and Quality":18,"Bottleneck and Pricing Power":7,"Market Mispricing":14,"Valuation Rerating Runway":10,"Capital Allocation":5,"Information Confidence":7},"simulated_total_score":72,"score_return_alignment":"negative"}
{"row_type":"aggregate_metric","selected_round":"R8","selected_loop":103,"large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","fine_archetype_id":"C28_STATIC_TO_30_ENTERPRISE_SECURITY_ARR_RENEWAL_RETENTION_MARGIN_BRIDGE_FINAL_GAP_FILL","representative_trigger_count":12,"calibration_usable_trigger_count":12,"positive_case_count":2,"mixed_positive_count":3,"counterexample_count":7,"local_4b_watch_count":3,"current_profile_error_count":12,"median_MFE_180D_pct":16.13,"median_MAE_180D_pct":-36.88,"new_axis_proposed":"C28_ENTERPRISE_SECURITY_ARR_RENEWAL_RETENTION_MARGIN_BRIDGE_REQUIRED | C28_AI_SECURITY_PRICE_ONLY_LOCAL_4B_CAP | C28_APPLIANCE_THEME_WITHOUT_RENEWAL_HIGH_MAE_GUARD | C28_ENTERPRISE_SOFTWARE_SUBSCRIPTION_RETENTION_GREEN_GATE","existing_axis_strengthened":"stage2_required_bridge | price_only_blowoff_blocks_positive_stage | full_4b_requires_non_price_evidence | local_4b_watch_guard | high_MAE_guardrail"}
{"row_type":"residual_contribution","selected_round":"R8","selected_loop":103,"large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","loop_contribution_label":"canonical_archetype_rule_candidate","residual_error_found":true,"new_independent_case_count":12,"new_symbol_count":8,"same_symbol_new_trigger_family_count":4,"description":"C28 should require enterprise ARR, renewal, retention, maintenance contract, subscription margin, or revision evidence. Security/AI/software labels alone generate repeated local MFE but high-MAE reversals."}
```

## 7. Current Calibrated Profile Stress Test

`e2r_2_1_stock_web_calibrated` already blocks price-only blowoff from positive-stage promotion and requires non-price evidence for full 4B. The residual C28 problem is narrower:

1. Security or AI/security wording can still look like a legitimate Stage2 event.
2. Some rows show quick 30D MFE but also deep 90D/180D MAE.
3. C28 positives require renewal/retention/margin evidence, not just keyword exposure.
4. Appliance, identity-authentication, VPN, and document-security spikes should be capped until recurring contract proof appears.

## 8. Shadow Rule Candidate

```yaml
shadow_rule_candidate:
  id: C28_ENTERPRISE_SECURITY_ARR_RENEWAL_RETENTION_MARGIN_BRIDGE_REQUIRED
  scope: canonical_archetype_specific
  canonical_archetype_id: C28_SOFTWARE_SECURITY_CONTRACT_RETENTION
  intent: >
    Separate durable enterprise software/security contract retention from AI/security/software price-only blowoff.
  positive_requirements:
    - recurring ARR/subscription/maintenance/renewal evidence
    - enterprise or public-sector contract retention bridge
    - margin, revision, or operating leverage confirmation
  caps:
    - AI/security keyword without recurring bridge -> Stage2 cap
    - local MFE with MAE180 below -35% -> local 4B only or high-MAE watch
    - appliance/VPN/security hardware theme without renewal bridge -> no Green
  promotion_blockers:
    - source_proxy_only rows cannot change production weights until URL and stock-web profile/shard refetch are complete
```

## 9. Deferred Coding Agent Handoff Prompt

```text
You are the coding agent for stock_agent E2R v12 batch calibration.
Do not treat this MD as an immediate production patch.
First parse the JSONL trigger rows, then refetch every listed stock-web profile and tradable shard.
Verify entry_date, entry_price, MFE_30D_pct, MAE_30D_pct, MFE_90D_pct, MAE_90D_pct, MFE_180D_pct, MAE_180D_pct.
Reject rows with missing required price fields, corporate-action contamination, or insufficient forward window.
For surviving rows, test a C28 canonical shadow rule requiring ARR / renewal / maintenance contract / retention / margin bridge before Stage2-Actionable, Stage3-Green, or full 4B promotion.
Keep production scoring unchanged until the batch verification report is complete.
```

## 10. Next Research State

```text
completed_round = R8
completed_loop = 103
selection_basis = docs/core/V12_Research_No_Repeat_Index.md + conversation-local generated MD ledger
selected_priority_bucket = Priority 0
round_schedule_status = coverage_index_selected
round_sector_consistency = pass
```

```text
next_recommended_archetypes = C02_POWER_GRID_DATACENTER_CAPEX_static_to_30_cleanup, C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK_static_to_30_cleanup, C28_SOFTWARE_SECURITY_CONTRACT_RETENTION_to_50_if_reverified, R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION, R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL
```
