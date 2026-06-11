# E2R Stock-Web v12 Residual Research — R8 / Loop 100 / C28_SOFTWARE_SECURITY_CONTRACT_RETENTION

```yaml
schema_family: v12_sector_archetype_residual
selected_round: R8
selected_loop: 100
large_sector_id: L8_PLATFORM_CONTENT_SW_SECURITY
canonical_archetype_id: C28_SOFTWARE_SECURITY_CONTRACT_RETENTION
fine_archetype_id: CYBERSECURITY_ENTERPRISE_RETENTION_CONTRACT_BRIDGE_VS_SECURITY_THEME_PRICE_ONLY_FALSE_POSITIVE
selected_priority_bucket: Priority 0
selection_basis: docs/core/V12_Research_No_Repeat_Index.md
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
```

## 1. Selection Rationale

`V12_Research_No_Repeat_Index.md` still classifies `C28_SOFTWARE_SECURITY_CONTRACT_RETENTION` as Priority 0: 18 rows, 13 symbols, and top-covered symbols concentrated in `307950`, `012510`, `042510`, `058970`, `012750`, and `041020`. This loop therefore adds four new C28-mapped symbols: `053800`, `067920`, `203650`, and `150900`.

This is not a live scan and not a production scoring patch. It is a historical trigger-level residual calibration file using `Songdaiki/stock-web` 1D OHLCV rows.

## 2. Price Atlas Validation

Stock-web manifest confirms:

```text
source_name = FinanceData/marcap
price_adjustment_status = raw_unadjusted_marcap
calibration_shard_root = atlas/ohlcv_tradable_by_symbol_year
manifest_max_date = 2026-02-20
tradable_row_count = 14354401
symbol_count = 5414
```

Profile checks:

| symbol | name | profile status | corporate-action overlap with entry~D+180 |
|---|---|---|---|
| 053800 | 안랩 | active_like, raw_unadjusted_marcap | none; only historical candidate outside 2024 window |
| 067920 | 이글루 | active_like, raw_unadjusted_marcap | none; only historical candidate outside 2024 window |
| 203650 | 드림시큐리티 | active_like, raw_unadjusted_marcap | none; candidate dates are outside selected 2024 window |
| 150900 | 파수 | active_like, raw_unadjusted_marcap | none |

All four rows are calibration-usable under the 30D/90D/180D trigger-row requirement.

## 3. Case Compression

C28 should not treat every cybersecurity vocabulary spike as durable software contract retention. The durable route is:

```text
enterprise customer base
  -> renewal / retention / recurring maintenance
  -> ARR-like or managed-service revenue visibility
  -> OPM / FCF bridge
  -> controlled Stage2-Actionable or Stage3-Yellow
```

The false-positive route is:

```text
security policy / AI security / authentication keyword
  -> local price MFE
  -> no renewal-rate or contract-retention bridge
  -> high MAE / failed rerating
  -> Stage2 watch or local 4B cap
```

## 4. Case Table

| case_id | symbol | role | entry | 180D MFE/MAE | residual lesson |
|---|---|---:|---:|---:|---|
| C28-R8-L100-053800-2024-04-11 | 053800 안랩 | structural_success + 4B watch | 64,800 | +16.67 / -21.76 | retention quality matters, but local policy/security spike still needs 4B cap |
| C28-R8-L100-067920-2024-01-19 | 067920 이글루 | mixed_positive | 7,310 | +18.74 / -32.63 | public/security contract momentum can work briefly, but renewal/margin proof is required |
| C28-R8-L100-203650-2024-02-15 | 203650 드림시큐리티 | failed_rerating_counterexample | 4,020 | +1.37 / -43.16 | security/authentication keyword without retention bridge is not Actionable |
| C28-R8-L100-150900-2024-04-01 | 150900 파수 | failed_rerating_counterexample | 6,800 | +16.32 / -26.76 | document-security spike creates MFE, not durable rerating without ARR/renewal evidence |

## 5. Machine-Readable Case Rows

```jsonl
{"row_type":"case","case_id":"C28-R8-L100-053800-2024-04-11","selected_round":"R8","selected_loop":100,"large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","fine_archetype_id":"CYBERSECURITY_ENTERPRISE_RETENTION_CONTRACT_BRIDGE_VS_SECURITY_THEME_PRICE_ONLY_FALSE_POSITIVE","symbol":"053800","name":"안랩","case_role":"structural_success","summary":"enterprise_endpoint_security_retention_bridge_with_price_spike_4b_watch","novelty_basis":"new_symbol_for_C28_not_in_no_repeat_top_covered_symbols","independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"case","case_id":"C28-R8-L100-067920-2024-01-19","selected_round":"R8","selected_loop":100,"large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","fine_archetype_id":"CYBERSECURITY_ENTERPRISE_RETENTION_CONTRACT_BRIDGE_VS_SECURITY_THEME_PRICE_ONLY_FALSE_POSITIVE","symbol":"067920","name":"이글루","case_role":"mixed_positive","summary":"security_operation_center_public_sector_contract_momentum_then_contract_retention_followthrough_gap","novelty_basis":"new_symbol_for_C28_not_in_no_repeat_top_covered_symbols","independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"case","case_id":"C28-R8-L100-203650-2024-02-15","selected_round":"R8","selected_loop":100,"large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","fine_archetype_id":"CYBERSECURITY_ENTERPRISE_RETENTION_CONTRACT_BRIDGE_VS_SECURITY_THEME_PRICE_ONLY_FALSE_POSITIVE","symbol":"203650","name":"드림시큐리티","case_role":"failed_rerating_counterexample","summary":"authentication_security_keyword_without_enterprise_contract_retention_margin_bridge","novelty_basis":"new_symbol_for_C28_not_in_no_repeat_top_covered_symbols","independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"case","case_id":"C28-R8-L100-150900-2024-04-01","selected_round":"R8","selected_loop":100,"large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","fine_archetype_id":"CYBERSECURITY_ENTERPRISE_RETENTION_CONTRACT_BRIDGE_VS_SECURITY_THEME_PRICE_ONLY_FALSE_POSITIVE","symbol":"150900","name":"파수","case_role":"failed_rerating_counterexample","summary":"document_security_zero_trust_theme_spike_without_ARR_retention_margin_revision_followthrough","novelty_basis":"new_symbol_for_C28_not_in_no_repeat_top_covered_symbols","independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
```

## 6. Machine-Readable Trigger Rows

```jsonl
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","selected_round":"R8","selected_loop":100,"large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","fine_archetype_id":"CYBERSECURITY_ENTERPRISE_RETENTION_CONTRACT_BRIDGE_VS_SECURITY_THEME_PRICE_ONLY_FALSE_POSITIVE","case_id":"C28-R8-L100-053800-2024-04-11","symbol":"053800","name":"안랩","trigger_type":"Stage2-Actionable","entry_date":"2024-04-11","entry_price":64800,"price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","forward_window_trading_days":180,"MFE_30D_pct":16.67,"MAE_30D_pct":-6.17,"MFE_90D_pct":16.67,"MAE_90D_pct":-20.37,"MFE_180D_pct":16.67,"MAE_180D_pct":-21.76,"same_entry_group_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION:053800:2024-04-11:Stage2-Actionable","dedupe_for_aggregate":true,"aggregate_group_role":"representative","calibration_usable":true,"corporate_action_window_status":"not_contaminated","corporate_action_window_check":"profile corporate_action_candidate_dates do not overlap entry_date_to_D180","source_proxy_only":true,"evidence_url_pending":true,"case_role":"structural_success","path_label":"enterprise_endpoint_security_retention_bridge_with_price_spike_4b_watch","current_profile_error_type":"calibrated_profile_underweights_retention_quality_but_must_cap_local_4b_after_security_policy_spike","stage_call":"Stage2-Actionable -> local Stage4B watch, not Green","raw_component_score_breakdown":{"EPS/FCF Explosion":11,"Earnings Visibility and Quality":21,"Bottleneck and Pricing Power":7,"Market Mispricing":14,"Valuation Rerating Runway":11,"Capital Allocation":7,"Information Confidence":9},"simulated_total_score":80,"score_return_alignment":"positive"}
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","selected_round":"R8","selected_loop":100,"large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","fine_archetype_id":"CYBERSECURITY_ENTERPRISE_RETENTION_CONTRACT_BRIDGE_VS_SECURITY_THEME_PRICE_ONLY_FALSE_POSITIVE","case_id":"C28-R8-L100-067920-2024-01-19","symbol":"067920","name":"이글루","trigger_type":"Stage2-Actionable","entry_date":"2024-01-19","entry_price":7310,"price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","forward_window_trading_days":180,"MFE_30D_pct":18.74,"MAE_30D_pct":-12.45,"MFE_90D_pct":18.74,"MAE_90D_pct":-21.61,"MFE_180D_pct":18.74,"MAE_180D_pct":-32.63,"same_entry_group_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION:067920:2024-01-19:Stage2-Actionable","dedupe_for_aggregate":true,"aggregate_group_role":"representative","calibration_usable":true,"corporate_action_window_status":"not_contaminated","corporate_action_window_check":"profile corporate_action_candidate_dates do not overlap entry_date_to_D180","source_proxy_only":true,"evidence_url_pending":true,"case_role":"mixed_positive","path_label":"security_operation_center_public_sector_contract_momentum_then_contract_retention_followthrough_gap","current_profile_error_type":"current_profile_accepts_security_contract_label_too_broadly_without_renewal_margin_bridge","stage_call":"Stage2-Actionable -> local Stage4B watch","raw_component_score_breakdown":{"EPS/FCF Explosion":9,"Earnings Visibility and Quality":19,"Bottleneck and Pricing Power":8,"Market Mispricing":15,"Valuation Rerating Runway":12,"Capital Allocation":6,"Information Confidence":8},"simulated_total_score":77,"score_return_alignment":"mixed"}
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","selected_round":"R8","selected_loop":100,"large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","fine_archetype_id":"CYBERSECURITY_ENTERPRISE_RETENTION_CONTRACT_BRIDGE_VS_SECURITY_THEME_PRICE_ONLY_FALSE_POSITIVE","case_id":"C28-R8-L100-203650-2024-02-15","symbol":"203650","name":"드림시큐리티","trigger_type":"Stage2","entry_date":"2024-02-15","entry_price":4020,"price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","forward_window_trading_days":180,"MFE_30D_pct":1.37,"MAE_30D_pct":-11.07,"MFE_90D_pct":1.37,"MAE_90D_pct":-25.0,"MFE_180D_pct":1.37,"MAE_180D_pct":-43.16,"same_entry_group_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION:203650:2024-02-15:Stage2","dedupe_for_aggregate":true,"aggregate_group_role":"representative","calibration_usable":true,"corporate_action_window_status":"not_contaminated","corporate_action_window_check":"profile corporate_action_candidate_dates do not overlap entry_date_to_D180","source_proxy_only":true,"evidence_url_pending":true,"case_role":"failed_rerating_counterexample","path_label":"authentication_security_keyword_without_enterprise_contract_retention_margin_bridge","current_profile_error_type":"price_and_security_keyword_false_positive_if_retention_bridge_is_not_required","stage_call":"Stage2 false positive; should remain Stage1/Stage2 watch","raw_component_score_breakdown":{"EPS/FCF Explosion":5,"Earnings Visibility and Quality":10,"Bottleneck and Pricing Power":5,"Market Mispricing":13,"Valuation Rerating Runway":9,"Capital Allocation":4,"Information Confidence":6},"simulated_total_score":52,"score_return_alignment":"negative"}
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","selected_round":"R8","selected_loop":100,"large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","fine_archetype_id":"CYBERSECURITY_ENTERPRISE_RETENTION_CONTRACT_BRIDGE_VS_SECURITY_THEME_PRICE_ONLY_FALSE_POSITIVE","case_id":"C28-R8-L100-150900-2024-04-01","symbol":"150900","name":"파수","trigger_type":"Stage2","entry_date":"2024-04-01","entry_price":6800,"price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","forward_window_trading_days":180,"MFE_30D_pct":16.32,"MAE_30D_pct":-7.35,"MFE_90D_pct":16.32,"MAE_90D_pct":-23.53,"MFE_180D_pct":16.32,"MAE_180D_pct":-26.76,"same_entry_group_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION:150900:2024-04-01:Stage2","dedupe_for_aggregate":true,"aggregate_group_role":"representative","calibration_usable":true,"corporate_action_window_status":"not_contaminated","corporate_action_window_check":"profile corporate_action_candidate_dates do not overlap entry_date_to_D180","source_proxy_only":true,"evidence_url_pending":true,"case_role":"failed_rerating_counterexample","path_label":"document_security_zero_trust_theme_spike_without_ARR_retention_margin_revision_followthrough","current_profile_error_type":"theme_spike_and_document_security_label_can_generate_local_MFE_but_not_durable_stage2_actionable_without_retention","stage_call":"Stage2 price-only/local 4B cap; not Stage2-Actionable","raw_component_score_breakdown":{"EPS/FCF Explosion":6,"Earnings Visibility and Quality":13,"Bottleneck and Pricing Power":6,"Market Mispricing":14,"Valuation Rerating Runway":10,"Capital Allocation":5,"Information Confidence":7},"simulated_total_score":61,"score_return_alignment":"negative"}
```

## 7. Machine-Readable Score Simulation Rows

```jsonl
{"row_type":"score_simulation","case_id":"C28-R8-L100-053800-2024-04-11","symbol":"053800","trigger_type":"Stage2-Actionable","raw_component_score_breakdown":{"EPS/FCF Explosion":11,"Earnings Visibility and Quality":21,"Bottleneck and Pricing Power":7,"Market Mispricing":14,"Valuation Rerating Runway":11,"Capital Allocation":7,"Information Confidence":9},"total_score":80,"current_profile_proxy_stage":"Stage2-Actionable -> local Stage4B watch, not Green","stage3_green_allowed":false,"reason_stage3_green_blocked":"C28 requires enterprise retention/renewal/margin bridge; price-only security theme or weak ARR proof cannot open Green."}
{"row_type":"score_simulation","case_id":"C28-R8-L100-067920-2024-01-19","symbol":"067920","trigger_type":"Stage2-Actionable","raw_component_score_breakdown":{"EPS/FCF Explosion":9,"Earnings Visibility and Quality":19,"Bottleneck and Pricing Power":8,"Market Mispricing":15,"Valuation Rerating Runway":12,"Capital Allocation":6,"Information Confidence":8},"total_score":77,"current_profile_proxy_stage":"Stage2-Actionable -> local Stage4B watch","stage3_green_allowed":false,"reason_stage3_green_blocked":"C28 requires enterprise retention/renewal/margin bridge; price-only security theme or weak ARR proof cannot open Green."}
{"row_type":"score_simulation","case_id":"C28-R8-L100-203650-2024-02-15","symbol":"203650","trigger_type":"Stage2","raw_component_score_breakdown":{"EPS/FCF Explosion":5,"Earnings Visibility and Quality":10,"Bottleneck and Pricing Power":5,"Market Mispricing":13,"Valuation Rerating Runway":9,"Capital Allocation":4,"Information Confidence":6},"total_score":52,"current_profile_proxy_stage":"Stage2 false positive; should remain Stage1/Stage2 watch","stage3_green_allowed":false,"reason_stage3_green_blocked":"C28 requires enterprise retention/renewal/margin bridge; price-only security theme or weak ARR proof cannot open Green."}
{"row_type":"score_simulation","case_id":"C28-R8-L100-150900-2024-04-01","symbol":"150900","trigger_type":"Stage2","raw_component_score_breakdown":{"EPS/FCF Explosion":6,"Earnings Visibility and Quality":13,"Bottleneck and Pricing Power":6,"Market Mispricing":14,"Valuation Rerating Runway":10,"Capital Allocation":5,"Information Confidence":7},"total_score":61,"current_profile_proxy_stage":"Stage2 price-only/local 4B cap; not Stage2-Actionable","stage3_green_allowed":false,"reason_stage3_green_blocked":"C28 requires enterprise retention/renewal/margin bridge; price-only security theme or weak ARR proof cannot open Green."}
```

## 8. Machine-Readable Aggregate / Shadow / Residual Rows

```jsonl
{"row_type":"aggregate_metric","selected_round":"R8","selected_loop":100,"large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","fine_archetype_id":"CYBERSECURITY_ENTERPRISE_RETENTION_CONTRACT_BRIDGE_VS_SECURITY_THEME_PRICE_ONLY_FALSE_POSITIVE","representative_trigger_count":4,"calibration_usable_trigger_count":4,"positive_case_count":1,"mixed_positive_count":1,"counterexample_count":2,"local_4b_watch_count":2,"current_profile_error_count":4,"median_MFE_180D_pct":16.5,"median_MAE_180D_pct":-29.7,"new_axis_proposed":"C28_enterprise_retention_renewal_margin_bridge_required | C28_security_theme_local_4b_high_MAE_guard","existing_axis_strengthened":"stage2_required_bridge | price_only_blowoff_blocks_positive_stage | full_4b_requires_non_price_evidence | local_4b_watch_guard | high_MAE_guardrail"}
{"row_type":"shadow_weight","selected_round":"R8","selected_loop":100,"large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","axis":"C28_enterprise_retention_renewal_margin_bridge_required","proposed_effect":"increase visibility/information gate for C28; do not loosen Green","safe_axis":"stage2_required_bridge","shadow_only":true,"production_scoring_changed":false}
{"row_type":"residual_contribution","selected_round":"R8","selected_loop":100,"large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","loop_contribution_label":"canonical_archetype_rule_candidate","residual_error_found":true,"new_independent_case_count":4,"reused_case_count":0,"new_symbol_count":4,"same_archetype_new_trigger_family_count":4,"description":"C28 needs company-level enterprise renewal/retention/margin proof. Security vocabulary and local price MFE alone repeatedly create high-MAE or failed-rerating rows."}
```

## 9. Residual Rule Candidate

```text
new_axis_proposed =
  C28_enterprise_retention_renewal_margin_bridge_required
  C28_security_theme_local_4b_high_MAE_guard

existing_axis_strengthened =
  stage2_required_bridge
  price_only_blowoff_blocks_positive_stage
  full_4b_requires_non_price_evidence
  local_4b_watch_guard
  high_MAE_guardrail

existing_axis_weakened = null
do_not_propose_new_weight_delta = false
```

C28 should raise the importance of `Earnings Visibility and Quality` and `Information Confidence` when the evidence is truly renewal/retention based. But the same archetype should not loosen Stage3-Green. The rule is closer to a bridge requirement than a bullish weight increase.

## 10. Batch Ingest Self-Audit

```text
expected_v12_result_file: true
filename_pattern_pass: true
metadata_filename_consistency: pass
jsonl_trigger_row_count: 4
calibration_usable_trigger_count: 4
representative_trigger_count: 4
new_weight_evidence_candidate_count: 4
guardrail_candidate_count: 3
narrative_only_or_rejected_count: 0
rows_missing_required_mfe_mae: 0
rows_missing_entry_price_or_date: 0
rows_with_noncanonical_trigger_type: 0
rows_with_compact_mfe_mae_alias_only: 0
ready_for_batch_ingest: true
```

## 11. Final Research State

```text
completed_round = {selected_round}
completed_loop = {selected_loop}
selection_basis = docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket = Priority 0
round_schedule_status = coverage_index_selected
round_sector_consistency = pass

new_independent_case_count = 4
reused_case_count = 0
new_symbol_count = 4
same_archetype_new_symbol_count = 4
same_archetype_new_trigger_family_count = 4
positive_case_count = 1
mixed_positive_count = 1
counterexample_count = 2
local_4b_watch_count = 2
current_profile_error_count = 4
loop_contribution_label = canonical_archetype_rule_candidate
do_not_propose_new_weight_delta = false

auto_selected_coverage_gap = C28 rows 18 -> 22 if accepted; still Priority 0, need 8 to 30
next_recommended_archetypes = C19_BRAND_RETAIL_INVENTORY_MARGIN, C27_CONTENT_IP_GLOBAL_MONETIZATION, C02_POWER_GRID_DATACENTER_CAPEX, C18_CONSUMER_EXPORT_CHANNEL_REORDER, C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE
```

This loop adds 4 new independent cases, 2 counterexamples, and 4 residual errors for R8/L8_PLATFORM_CONTENT_SW_SECURITY/C28_SOFTWARE_SECURITY_CONTRACT_RETENTION.

## 12. Deferred Coding Agent Handoff Prompt

```text
Do not execute this prompt during the research run.

Later coding agent task:
1. Ingest this MD as a v12_sector_archetype_residual artifact.
2. Validate that all trigger rows have canonical trigger_type, entry_date, entry_price, 30D/90D/180D MFE and MAE, price_data_source=Songdaiki/stock-web, price_basis=tradable_raw, price_adjustment_status=raw_unadjusted_marcap.
3. Add C28_enterprise_retention_renewal_margin_bridge_required as a shadow-only candidate axis.
4. Stress-test whether C28 should require explicit renewal/retention/ARR-like evidence before Stage2-Actionable.
5. Do not loosen Stage3-Green.
6. Keep this as shadow_weight_only until more C28 positive cases are added.
```
