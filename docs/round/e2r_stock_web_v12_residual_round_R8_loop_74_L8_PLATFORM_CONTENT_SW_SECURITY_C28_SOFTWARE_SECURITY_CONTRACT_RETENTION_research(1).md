# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
scheduled_round: R8
scheduled_loop: 74
round_schedule_status: valid
round_sector_consistency: pass
computed_next_round: R9
computed_next_loop: 74
large_sector_id: L8_PLATFORM_CONTENT_SW_SECURITY
canonical_archetype_id: C28_SOFTWARE_SECURITY_CONTRACT_RETENTION
fine_archetype_id: C28_CONTRACT_RETENTION_RECURRING_REVENUE_MARGIN_BRIDGE_GUARD
loop_objective: coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | canonical_archetype_compression
price_source: Songdaiki/stock-web
stock_web_manifest_max_date: 2026-02-20
production_scoring_changed: false
shadow_weight_only: true
```

## 1. Current Calibrated Profile Assumption

```text
current_default_profile_proxy = e2r_2_1_stock_web_calibrated
previous_baseline_reference = e2r_2_0_baseline
stage2_actionable_evidence_bonus = +2.0
stage3_yellow_total_min = 75.0
stage3_green_total_min = 87.0
stage3_green_revision_min = 55.0
stage3_cross_evidence_green_buffer = +1.5
price_only_blowoff_blocks_positive_stage = true
full_4b_requires_non_price_evidence = true
hard_4c_thesis_break_routes_to_4c = true
```

## 2. Round / Large Sector / Canonical Archetype Scope

R8 maps to `L8_PLATFORM_CONTENT_SW_SECURITY`. The previous R8 loop used C26 ad/platform revenue, so this run shifts to C28 software/security contract-retention. The branch avoids the top-covered C28 symbols and tests the line between real enterprise contract/retention economics and software, database, AI, or security theme heat.

| layer | id | definition |
|---|---|---|
| round | R8 | platform / content / software / security |
| large_sector | L8_PLATFORM_CONTENT_SW_SECURITY | platform, content, software, security, contract/retention |
| canonical | C28_SOFTWARE_SECURITY_CONTRACT_RETENTION | software/security, contract retention, recurring revenue |
| fine | C28_CONTRACT_RETENTION_RECURRING_REVENUE_MARGIN_BRIDGE_GUARD | software signal must become contract, retention, revenue and margin evidence |
| deep | ENTERPRISE_PROCUREMENT_SAAS_STRATEGIC_CUSTOMER_TO_RECURRING_CONTRACT_AND_RETENTION | procurement SaaS positive |
| deep | DATABASE_AI_OPTIONALITY_WITHOUT_ENTERPRISE_CONTRACT_RETENTION_OR_REVENUE_CONVERSION | database/AI false positive |
| deep | DOCUMENT_SECURITY_DRM_OPTIONALITY_WITHOUT_RENEWAL_CONTRACT_MARGIN_CONVERSION | security/DRM false positive |

## 3. No-Repeat / Coverage Check

No-Repeat hard duplicate key:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

C28 top-covered symbols are `012510`, `053800`, `263860`, `030520`, `131370`, and `136540`. This run avoids that cluster and also avoids the previous R8/C26 ad-platform representatives.

| archetype | selected symbol | duplicate status | reason |
|---|---:|---|---|
| C28 | 058970 | new independent | not top-covered C28 symbol; procurement SaaS / strategic customer contract bridge |
| C28 | 357880 | new independent | not top-covered C28 symbol; graph database / AI theme without contract-retention bridge |
| C28 | 150900 | new independent | not top-covered C28 symbol; security/DRM theme without renewal-retention bridge |

## 4. Stock-Web OHLC Input / Price Source Validation

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","source_name":"FinanceData/marcap","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
```

Stock-web assumptions:

```text
source_name = FinanceData/marcap
price_adjustment_status = raw_unadjusted_marcap
min_date = 1995-05-02
max_date = 2026-02-20
tradable_row_count = 14354401
symbol_count = 5414
calibration_shard_root = atlas/ohlcv_tradable_by_symbol_year
tradable columns = d,o,h,l,c,v,a,mc,s,m
```

## 5. Historical Eligibility Gate

```text
entry row exists = true
forward 180 trading days available = true
MFE/MAE 30D/90D/180D computed = true
price_basis = tradable_raw
price_adjustment_status = raw_unadjusted_marcap
corporate_action_window_status = clean_180D_window
```

Corporate-action caveat:

```text
058970 has corporate-action candidate dates in 2022, outside the selected 2023 representative window.
357880 has 2024-11-15 and 2024-12-02 corporate-action candidate dates; the selected 2024-01-29 180D representative window is treated as usable before those blocked dates.
150900 has no corporate-action candidate dates.
All three representative windows are treated as clean for 30D/90D/180D calibration.
```

## 6. Case Selection Summary

| role | symbol | company | trigger | entry | price | result |
|---|---:|---|---|---:|---:|---|
| structural_success_then_4B_watch | 058970 | 엠로 | Stage2-Actionable | 2023-03-15 | 30200 | procurement SaaS strategic-customer contract bridge worked |
| failed_rerating_high_MAE_database_AI_theme | 357880 | 비트나인 | Stage2-Actionable | 2024-01-29 | 6440 | database/AI theme lacked enterprise contract-retention bridge |
| failed_rerating_high_MAE_security_theme | 150900 | 파수 | Stage2-Actionable | 2024-01-29 | 9000 | security/DRM theme lacked renewal-retention and margin bridge |

## 7. Positive vs Counterexample Balance

```text
positive_case_count: 1
counterexample_count: 2
4B_case_count: 3
4C_or_high_MAE_watch_count: 2
calibration_usable_case_count: 3
current_profile_error_count: 2
```

## 8. Trigger-Level OHLC Backtest Table

| symbol | company | trigger | entry_date | entry_price | MFE30 | MFE90 | MFE180 | MAE30 | MAE90 | MAE180 | peak_date | peak_price | DD after peak |
|---:|---|---|---|---:|---:|---:|---:|---:|---:|---:|---|---:|---:|
| 058970 | 엠로 | Stage2-Actionable | 2023-03-15 | 30200 | 127.81 | 223.84 | 223.84 | 0.0 | 0.0 | 0.0 | 2023-07-20 | 97800 | -45.81 |
| 357880 | 비트나인 | Stage2-Actionable | 2024-01-29 | 6440 | 6.52 | 6.52 | 6.52 | -17.39 | -62.66 | -67.31 | 2024-01-29 | 6860 | -69.31 |
| 150900 | 파수 | Stage2-Actionable | 2024-01-29 | 9000 | 9.78 | 9.78 | 9.78 | -20.0 | -31.44 | -44.67 | 2024-01-29 | 9880 | -49.6 |

## 9. Case-by-Case Notes

### 9.1 058970 / 엠로 — procurement SaaS strategic-customer contract bridge

The entry row is 2023-03-15 at 30,200. The 30D path reaches 68,800 and the broader forward path reaches 97,800. This is a valid C28 positive because the move is not merely software theme heat. It is tied to strategic customer quality, procurement SaaS contract optionality, recurring-revenue visibility, and enterprise customer pull-through. The post-peak decline still requires 4B watch.

### 9.2 357880 / 비트나인 — graph database / AI theme false positive

The entry row is 2024-01-29 at 6,440. The local high is only 6,860, while the broader low reaches 2,105 before the later corporate-action windows. This is a C28 false-positive branch: database, graph, or AI language can create Stage2 heat, but without enterprise contracts, retention, recurring revenue, and margin conversion, the path leaks into high MAE.

### 9.3 150900 / 파수 — security/DRM theme without retention bridge

The entry row is 2024-01-29 at 9,000. The best forward high remains around the local peak, while the forward low falls to 4,980. Security/DRM option value alone is insufficient. The model should demand renewal, retention, recurring revenue, enterprise contract quality, or margin/cashflow conversion before allowing Stage3.

## 10. Current Calibrated Profile Stress Test

| question | result |
|---|---|
| Stage2 actionable bonus too strong? | Yes when C28 treats software/security/AI theme strength as enough evidence. |
| Stage3 Yellow threshold too loose? | Not globally; C28 needs contract-retention/recurring-revenue/margin bridge before Yellow. |
| Stage3 Green too strict? | Correct. No Green loosening. |
| Price-only blowoff guard appropriate? | Yes, especially for 357880 and 150900. |
| Full 4B non-price requirement appropriate? | Yes. 058970 has non-price bridge evidence; 357880/150900 do not. |
| 4C timing issue? | High-MAE watch is useful; no immediate hard 4C promotion proposed. |

## 11. Stage2 / Yellow / Green Comparison

```text
058970:
  Stage2-Actionable = correct
  Stage3-Yellow = allowed after strategic customer / contract / retention bridge
  Stage3-Green = wait for post-MFE 4B review and recurring-revenue durability

357880:
  Stage2-Actionable = too generous if based only on database/AI software theme
  Stage3-Yellow = reject without enterprise contract, retention, revenue and margin bridge
  Stage3-Green = reject

150900:
  Stage2-Actionable = too generous if based only on security/DRM theme
  Stage3-Yellow = reject without renewal, retention, recurring revenue and margin bridge
  Stage3-Green = reject
```

## 12. 4B Local vs Full-window Timing Audit

| symbol | local_peak_proximity | full_window_peak_proximity | verdict |
|---:|---:|---:|---|
| 058970 | 0.93 | 1.00 | good full-window 4B watch after procurement SaaS contract bridge |
| 357880 | 1.00 | 1.00 | database/AI theme local 4B watch, not positive stage |
| 150900 | 1.00 | 1.00 | security/DRM theme local 4B watch, not positive stage |

## 13. Canonical-Archetype Rule Candidate

```text
canonical_archetype_rule_candidate: true
rule_scope: canonical_archetype_specific
rule_id: c28_requires_contract_retention_recurring_revenue_margin_bridge

rule:
  For C28 software/security contract-retention rows, do not promote software,
  security, database, AI, SaaS, DRM, or enterprise IT Stage2 signals into Stage3-Yellow/Green
  unless at least one non-price bridge is visible:
  enterprise contract, renewal/retention, recurring revenue, backlog-to-revenue conversion,
  customer-quality evidence, margin conversion, FCF/cash conversion, or earnings revision.
```

## 14. Before / After Backtest Comparison

| profile | eligible triggers | avg MFE90 | avg MAE90 | false positive rate | verdict |
|---|---:|---:|---:|---:|---|
| P0 e2r_2_1_stock_web_calibrated_proxy | 3 | 80.05 | -31.37 | 66.7% | too generous to software/security theme rows |
| P0b e2r_2_0_baseline_reference | 3 | 80.05 | -31.37 | 33.3% | safer but may miss 058970 |
| P1 sector_specific_candidate_profile | 3 | 80.05 | -31.37 | 66.7% | no broad L8 loosen |
| P2 canonical_archetype_candidate_profile | 1 selected positive | 223.84 | 0.0 | 0% after bridge gate | preferred shadow |
| P3 counterexample_guard_profile | 2 rejected | 8.15 | -47.05 | 0% after no-Green routing | useful guard |

## 15. Score-Return Alignment Matrix

| case | current profile verdict | alignment |
|---|---|---|
| 058970 | current_profile_correct | strategic-customer contract bridge aligned with strong MFE |
| 357880 | current_profile_false_positive | database/AI theme produced shallow MFE and high MAE |
| 150900 | current_profile_false_positive | security/DRM theme produced high MAE without renewal/retention bridge |

## 16. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive | counterexample | 4B | 4C/watch | new_independent | reused | usable_triggers | representative | profile_errors | sector_rule | canonical_rule | coverage_gap_after |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| L8_PLATFORM_CONTENT_SW_SECURITY | C28_SOFTWARE_SECURITY_CONTRACT_RETENTION | C28_CONTRACT_RETENTION_RECURRING_REVENUE_MARGIN_BRIDGE_GUARD | 1 | 2 | 3 | 2 | 3 | 0 | 3 | 3 | 2 | false | true | C28 non-top-covered software/security retention residual reduced |

## 17. Residual Contribution Summary

```text
new_independent_case_count: 3
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 3
new_canonical_archetype_count: 0
new_fine_archetype_count: 1
new_trigger_family_count: 3
tested_existing_calibrated_axes:
- stage2_actionable_evidence_bonus
- price_only_blowoff_blocks_positive_stage
- full_4b_requires_non_price_evidence
- local_4b_watch_guard
- high_MAE_guardrail
residual_error_types_found:
- software/security theme without contract-retention bridge
- database AI theme high-MAE
- procurement SaaS winner needs 4B watch
new_axis_proposed: null
existing_axis_strengthened:
- stage2_required_bridge
- full_4b_requires_non_price_evidence
- local_4b_watch_guard
- high_MAE_watch_guard
existing_axis_weakened: null
existing_axis_kept:
- stage3_green_total_min
- stage3_green_revision_min
sector_specific_rule_candidate: false
canonical_archetype_rule_candidate: true
loop_contribution_label: canonical_archetype_rule_candidate
```

## 18. Validation Scope / Non-Validation Scope

Validated:

```text
- stock-web tradable_raw OHLC rows
- entry_date / entry_price
- MFE/MAE/peak/drawdown
- round/sector/canonical consistency
- duplicate avoidance at symbol level
- representative rows use clean 180D windows
```

Not validated:

```text
- exact disclosure URLs
- exact report URLs
- production scoring behavior
- live candidate status
- 357880 post-2024-11 corporate-action-contaminated periods; only 180D representative window is used
```

## 19. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,c28_requires_contract_retention_recurring_revenue_margin_bridge,canonical_archetype_specific,L8_PLATFORM_CONTENT_SW_SECURITY,C28_SOFTWARE_SECURITY_CONTRACT_RETENTION,0,1,+1,"C28 software/security rows should not promote toward Stage3-Yellow/Green unless software/security signal converts into enterprise contract, renewal/retention, recurring revenue, backlog-to-revenue, margin, or cashflow bridge","058970 survives with strong MFE after strategic customer/procurement SaaS contract bridge; 357880 and 150900 fail when database/security themes lack retention and revenue bridge","TRG_R8L74_C28_058970_20230315_PROCUREMENT_SAAS_STRATEGIC_CUSTOMER_CONTRACT_BRIDGE|TRG_R8L74_C28_357880_20240129_GRAPH_DATABASE_AI_THEME_NO_CONTRACT_RETENTION_BRIDGE|TRG_R8L74_C28_150900_20240129_SECURITY_DRM_THEME_NO_RETENTION_RENEWAL_BRIDGE",3,3,2,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,c28_software_security_theme_4b_high_mae_watch_guard,canonical_archetype_specific,L8_PLATFORM_CONTENT_SW_SECURITY,C28_SOFTWARE_SECURITY_CONTRACT_RETENTION,1,1,0,"Software/security winners and AI/security theme false starts can peak before retention and revenue durability is confirmed; local/full-window 4B and high-MAE watch should remain active","preserves 058970 positive while preventing 357880/150900 software-security theme false positives","TRG_R8L74_C28_058970_20230315_PROCUREMENT_SAAS_STRATEGIC_CUSTOMER_CONTRACT_BRIDGE|TRG_R8L74_C28_357880_20240129_GRAPH_DATABASE_AI_THEME_NO_CONTRACT_RETENTION_BRIDGE|TRG_R8L74_C28_150900_20240129_SECURITY_DRM_THEME_NO_RETENTION_RENEWAL_BRIDGE",3,3,2,medium,existing_axis_kept,"strengthens local/full-window 4B and high-MAE watch without global delta"
```

## 20. Machine-Readable Rows

### 20.1 price_source_validation

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","source_name":"FinanceData/marcap","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
```

### 20.2 case rows

```jsonl
{"row_type":"case","case_id":"R8L74_C28_058970_20230315_PROCUREMENT_SAAS_STRATEGIC_CUSTOMER_CONTRACT_BRIDGE","symbol":"058970","company_name":"엠로","round":"R8","loop":"74","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","fine_archetype_id":"C28_PROCUREMENT_SAAS_STRATEGIC_CUSTOMER_CONTRACT_BRIDGE","deep_sub_archetype_id":"ENTERPRISE_PROCUREMENT_SAAS_STRATEGIC_CUSTOMER_TO_RECURRING_CONTRACT_AND_RETENTION","case_type":"structural_success_then_4B_watch","positive_or_counterexample":"positive","best_trigger":"Stage2-Actionable","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"score_return_aligned","current_profile_verdict":"current_profile_correct","price_source":"Songdaiki/stock-web","notes":"C28 software/security rows require enterprise contract, retention, renewal, recurring revenue, backlog-to-revenue, margin, or cashflow bridge; software/AI/security theme alone is insufficient."}
{"row_type":"case","case_id":"R8L74_C28_357880_20240129_GRAPH_DATABASE_AI_THEME_NO_CONTRACT_RETENTION_BRIDGE","symbol":"357880","company_name":"비트나인","round":"R8","loop":"74","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","fine_archetype_id":"C28_GRAPH_DATABASE_AI_THEME_WITHOUT_CONTRACT_RETENTION_BRIDGE","deep_sub_archetype_id":"DATABASE_AI_OPTIONALITY_WITHOUT_ENTERPRISE_CONTRACT_RETENTION_OR_REVENUE_CONVERSION","case_type":"failed_rerating_high_MAE_database_AI_theme","positive_or_counterexample":"counterexample","best_trigger":"Stage2-Actionable","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"score_return_misaligned","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"C28 software/security rows require enterprise contract, retention, renewal, recurring revenue, backlog-to-revenue, margin, or cashflow bridge; software/AI/security theme alone is insufficient."}
{"row_type":"case","case_id":"R8L74_C28_150900_20240129_SECURITY_DRM_THEME_NO_RETENTION_RENEWAL_BRIDGE","symbol":"150900","company_name":"파수","round":"R8","loop":"74","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","fine_archetype_id":"C28_SECURITY_DRM_THEME_WITHOUT_RETENTION_RENEWAL_BRIDGE","deep_sub_archetype_id":"DOCUMENT_SECURITY_DRM_OPTIONALITY_WITHOUT_RENEWAL_CONTRACT_MARGIN_CONVERSION","case_type":"failed_rerating_high_MAE_security_theme","positive_or_counterexample":"counterexample","best_trigger":"Stage2-Actionable","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"score_return_misaligned","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"C28 software/security rows require enterprise contract, retention, renewal, recurring revenue, backlog-to-revenue, margin, or cashflow bridge; software/AI/security theme alone is insufficient."}
```

### 20.3 trigger rows

```jsonl
{"row_type":"trigger","trigger_id":"TRG_R8L74_C28_058970_20230315_PROCUREMENT_SAAS_STRATEGIC_CUSTOMER_CONTRACT_BRIDGE","case_id":"R8L74_C28_058970_20230315_PROCUREMENT_SAAS_STRATEGIC_CUSTOMER_CONTRACT_BRIDGE","symbol":"058970","company_name":"엠로","round":"R8","loop":"74","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","fine_archetype_id":"C28_PROCUREMENT_SAAS_STRATEGIC_CUSTOMER_CONTRACT_BRIDGE","deep_sub_archetype_id":"ENTERPRISE_PROCUREMENT_SAAS_STRATEGIC_CUSTOMER_TO_RECURRING_CONTRACT_AND_RETENTION","loop_objective":"coverage_gap_fill|counterexample_mining|stage2_actionable_bonus_stress_test|4B_non_price_requirement_stress_test|canonical_archetype_compression","trigger_type":"Stage2-Actionable","trigger_date":"2023-03-15","entry_date":"2023-03-15","entry_price":30200,"evidence_available_at_that_date":"source_proxy_procurement_SaaS_strategic_customer_contract_retention_revenue_bridge; evidence_url_pending","evidence_source":"source_proxy_procurement_SaaS_strategic_customer_contract_retention_revenue_bridge; evidence_url_pending","bridge_summary":"procurement SaaS and strategic customer route converted into contract/revenue visibility and retention optionality rather than generic AI/software theme","stage2_evidence_fields":["enterprise_procurement_SaaS","strategic_customer_signal","relative_strength","contract_revenue_proxy"],"stage3_evidence_fields":["contract_to_revenue_visibility","retention_or_recurring_revenue_proxy","enterprise_customer_quality_bridge"],"stage4b_evidence_fields":["post_MFE_peak_watch","software_contract_multiple_crowding"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/058/058970/2023.csv","profile_path":"atlas/symbol_profiles/058/058970.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":127.81,"MFE_90D_pct":223.84,"MFE_180D_pct":223.84,"MFE_1Y_pct":223.84,"MFE_2Y_pct":223.84,"MAE_30D_pct":0.0,"MAE_90D_pct":0.0,"MAE_180D_pct":0.0,"MAE_1Y_pct":0.0,"below_entry_price_flag_30D":false,"below_entry_price_flag_90D":false,"peak_date":"2023-07-20","peak_price":97800,"drawdown_after_peak_pct":-45.81,"green_lateness_ratio":"0.32","four_b_local_peak_proximity":0.93,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"good_full_window_4B_watch_after_procurement_SaaS_contract_bridge","four_b_evidence_type":"non_price_contract_retention_revenue_bridge","four_c_protection_label":"none","trigger_outcome_label":"structural_success_then_4B_watch","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R8L74_C28_058970_20230315_PROCUREMENT_SAAS_STRATEGIC_CUSTOMER_CONTRACT_BRIDGE_entry","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"TRG_R8L74_C28_357880_20240129_GRAPH_DATABASE_AI_THEME_NO_CONTRACT_RETENTION_BRIDGE","case_id":"R8L74_C28_357880_20240129_GRAPH_DATABASE_AI_THEME_NO_CONTRACT_RETENTION_BRIDGE","symbol":"357880","company_name":"비트나인","round":"R8","loop":"74","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","fine_archetype_id":"C28_GRAPH_DATABASE_AI_THEME_WITHOUT_CONTRACT_RETENTION_BRIDGE","deep_sub_archetype_id":"DATABASE_AI_OPTIONALITY_WITHOUT_ENTERPRISE_CONTRACT_RETENTION_OR_REVENUE_CONVERSION","loop_objective":"coverage_gap_fill|counterexample_mining|stage2_actionable_bonus_stress_test|4B_non_price_requirement_stress_test|canonical_archetype_compression","trigger_type":"Stage2-Actionable","trigger_date":"2024-01-29","entry_date":"2024-01-29","entry_price":6440,"evidence_available_at_that_date":"source_proxy_graph_database_AI_software_theme_without_enterprise_contract_retention_bridge; evidence_url_pending","evidence_source":"source_proxy_graph_database_AI_software_theme_without_enterprise_contract_retention_bridge; evidence_url_pending","bridge_summary":"graph database / AI software theme did not convert into visible enterprise contract, retention, revenue, or margin bridge and later path became high-MAE watch","stage2_evidence_fields":["database_AI_theme","software_optionality","relative_strength"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["software_theme_local_peak","contract_retention_bridge_absent","revenue_conversion_absent"],"stage4c_evidence_fields":["high_MAE_without_contract_or_revenue_bridge"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/357/357880/2024.csv","profile_path":"atlas/symbol_profiles/357/357880.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":6.52,"MFE_90D_pct":6.52,"MFE_180D_pct":6.52,"MFE_1Y_pct":6.52,"MFE_2Y_pct":6.52,"MAE_30D_pct":-17.39,"MAE_90D_pct":-62.66,"MAE_180D_pct":-67.31,"MAE_1Y_pct":-67.31,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-01-29","peak_price":6860,"drawdown_after_peak_pct":-69.31,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"database_AI_theme_local_4B_watch_not_positive_stage","four_b_evidence_type":"software_security_theme_without_retention_bridge","four_c_protection_label":"high_MAE_watch","trigger_outcome_label":"failed_rerating_high_MAE_counterexample","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R8L74_C28_357880_20240129_GRAPH_DATABASE_AI_THEME_NO_CONTRACT_RETENTION_BRIDGE_entry","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"TRG_R8L74_C28_150900_20240129_SECURITY_DRM_THEME_NO_RETENTION_RENEWAL_BRIDGE","case_id":"R8L74_C28_150900_20240129_SECURITY_DRM_THEME_NO_RETENTION_RENEWAL_BRIDGE","symbol":"150900","company_name":"파수","round":"R8","loop":"74","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","fine_archetype_id":"C28_SECURITY_DRM_THEME_WITHOUT_RETENTION_RENEWAL_BRIDGE","deep_sub_archetype_id":"DOCUMENT_SECURITY_DRM_OPTIONALITY_WITHOUT_RENEWAL_CONTRACT_MARGIN_CONVERSION","loop_objective":"coverage_gap_fill|counterexample_mining|stage2_actionable_bonus_stress_test|4B_non_price_requirement_stress_test|canonical_archetype_compression","trigger_type":"Stage2-Actionable","trigger_date":"2024-01-29","entry_date":"2024-01-29","entry_price":9000,"evidence_available_at_that_date":"source_proxy_security_DRM_theme_without_retention_renewal_margin_bridge; evidence_url_pending","evidence_source":"source_proxy_security_DRM_theme_without_retention_renewal_margin_bridge; evidence_url_pending","bridge_summary":"security/DRM theme did not convert into renewal, retention, contract backlog, margin, or recurring revenue bridge","stage2_evidence_fields":["security_DRM_theme","cybersecurity_optionality","relative_strength"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["security_theme_local_peak","renewal_retention_bridge_absent","margin_recurring_revenue_bridge_absent"],"stage4c_evidence_fields":["high_MAE_without_retention_or_margin_bridge"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/150/150900/2024.csv","profile_path":"atlas/symbol_profiles/150/150900.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":9.78,"MFE_90D_pct":9.78,"MFE_180D_pct":9.78,"MFE_1Y_pct":9.78,"MFE_2Y_pct":9.78,"MAE_30D_pct":-20.0,"MAE_90D_pct":-31.44,"MAE_180D_pct":-44.67,"MAE_1Y_pct":-44.67,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-01-29","peak_price":9880,"drawdown_after_peak_pct":-49.6,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"security_DRM_theme_local_4B_watch_not_positive_stage","four_b_evidence_type":"software_security_theme_without_retention_bridge","four_c_protection_label":"high_MAE_watch","trigger_outcome_label":"failed_rerating_high_MAE_counterexample","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R8L74_C28_150900_20240129_SECURITY_DRM_THEME_NO_RETENTION_RENEWAL_BRIDGE_entry","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
```

### 20.4 score_simulation rows

```jsonl
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R8L74_C28_058970_20230315_PROCUREMENT_SAAS_STRATEGIC_CUSTOMER_CONTRACT_BRIDGE","trigger_id":"TRG_R8L74_C28_058970_20230315_PROCUREMENT_SAAS_STRATEGIC_CUSTOMER_CONTRACT_BRIDGE","symbol":"058970","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","raw_component_scores_before":{"contract_retention_score":12,"recurring_revenue_score":11,"enterprise_customer_quality_score":12,"margin_cashflow_score":9,"relative_strength_score":12,"theme_risk_penalty":5},"weighted_score_before":74,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"contract_retention_score":15,"recurring_revenue_score":14,"enterprise_customer_quality_score":15,"margin_cashflow_score":12,"relative_strength_score":9,"theme_risk_penalty":7},"weighted_score_after":82,"stage_label_after":"Stage3-Yellow","changed_components":["contract_retention_score","recurring_revenue_score","enterprise_customer_quality_score","margin_cashflow_score","relative_strength_score","theme_risk_penalty"],"component_delta_explanation":"C28 row is promoted only because software strength converts into enterprise contract, retention and revenue bridge; 4B watch remains after large MFE.","MFE_90D_pct":223.84,"MAE_90D_pct":0.0,"score_return_alignment_label":"score_return_aligned","current_profile_verdict":"current_profile_correct"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R8L74_C28_357880_20240129_GRAPH_DATABASE_AI_THEME_NO_CONTRACT_RETENTION_BRIDGE","trigger_id":"TRG_R8L74_C28_357880_20240129_GRAPH_DATABASE_AI_THEME_NO_CONTRACT_RETENTION_BRIDGE","symbol":"357880","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","raw_component_scores_before":{"contract_retention_score":2,"recurring_revenue_score":1,"enterprise_customer_quality_score":1,"margin_cashflow_score":0,"relative_strength_score":11,"theme_risk_penalty":8},"weighted_score_before":61,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"contract_retention_score":0,"recurring_revenue_score":0,"enterprise_customer_quality_score":0,"margin_cashflow_score":0,"relative_strength_score":4,"theme_risk_penalty":16},"weighted_score_after":39,"stage_label_after":"Stage1-Watch_or_4B-HighMAE","changed_components":["contract_retention_score","recurring_revenue_score","enterprise_customer_quality_score","margin_cashflow_score","relative_strength_score","theme_risk_penalty"],"component_delta_explanation":"C28 guard demotes software/security/AI theme rows when contract retention, renewal, recurring revenue, margin or cashflow bridge is absent.","MFE_90D_pct":6.52,"MAE_90D_pct":-62.66,"score_return_alignment_label":"score_return_misaligned","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R8L74_C28_150900_20240129_SECURITY_DRM_THEME_NO_RETENTION_RENEWAL_BRIDGE","trigger_id":"TRG_R8L74_C28_150900_20240129_SECURITY_DRM_THEME_NO_RETENTION_RENEWAL_BRIDGE","symbol":"150900","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","raw_component_scores_before":{"contract_retention_score":2,"recurring_revenue_score":1,"enterprise_customer_quality_score":1,"margin_cashflow_score":0,"relative_strength_score":11,"theme_risk_penalty":8},"weighted_score_before":61,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"contract_retention_score":0,"recurring_revenue_score":0,"enterprise_customer_quality_score":0,"margin_cashflow_score":0,"relative_strength_score":4,"theme_risk_penalty":16},"weighted_score_after":39,"stage_label_after":"Stage1-Watch_or_4B-HighMAE","changed_components":["contract_retention_score","recurring_revenue_score","enterprise_customer_quality_score","margin_cashflow_score","relative_strength_score","theme_risk_penalty"],"component_delta_explanation":"C28 guard demotes software/security/AI theme rows when contract retention, renewal, recurring revenue, margin or cashflow bridge is absent.","MFE_90D_pct":9.78,"MAE_90D_pct":-31.44,"score_return_alignment_label":"score_return_misaligned","current_profile_verdict":"current_profile_false_positive"}
```

### 20.5 shadow_weight rows

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,c28_requires_contract_retention_recurring_revenue_margin_bridge,canonical_archetype_specific,L8_PLATFORM_CONTENT_SW_SECURITY,C28_SOFTWARE_SECURITY_CONTRACT_RETENTION,0,1,+1,"C28 software/security rows should not promote toward Stage3-Yellow/Green unless software/security signal converts into enterprise contract, renewal/retention, recurring revenue, backlog-to-revenue, margin, or cashflow bridge","058970 survives with strong MFE after strategic customer/procurement SaaS contract bridge; 357880 and 150900 fail when database/security themes lack retention and revenue bridge","TRG_R8L74_C28_058970_20230315_PROCUREMENT_SAAS_STRATEGIC_CUSTOMER_CONTRACT_BRIDGE|TRG_R8L74_C28_357880_20240129_GRAPH_DATABASE_AI_THEME_NO_CONTRACT_RETENTION_BRIDGE|TRG_R8L74_C28_150900_20240129_SECURITY_DRM_THEME_NO_RETENTION_RENEWAL_BRIDGE",3,3,2,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,c28_software_security_theme_4b_high_mae_watch_guard,canonical_archetype_specific,L8_PLATFORM_CONTENT_SW_SECURITY,C28_SOFTWARE_SECURITY_CONTRACT_RETENTION,1,1,0,"Software/security winners and AI/security theme false starts can peak before retention and revenue durability is confirmed; local/full-window 4B and high-MAE watch should remain active","preserves 058970 positive while preventing 357880/150900 software-security theme false positives","TRG_R8L74_C28_058970_20230315_PROCUREMENT_SAAS_STRATEGIC_CUSTOMER_CONTRACT_BRIDGE|TRG_R8L74_C28_357880_20240129_GRAPH_DATABASE_AI_THEME_NO_CONTRACT_RETENTION_BRIDGE|TRG_R8L74_C28_150900_20240129_SECURITY_DRM_THEME_NO_RETENTION_RENEWAL_BRIDGE",3,3,2,medium,existing_axis_kept,"strengthens local/full-window 4B and high-MAE watch without global delta"
```

### 20.6 residual_contribution row

```jsonl
{"row_type":"residual_contribution","round":"R8","loop":"74","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","new_independent_case_count":3,"reused_case_count":0,"new_symbol_count":3,"new_trigger_family_count":3,"tested_existing_calibrated_axes":["stage2_actionable_evidence_bonus","price_only_blowoff_blocks_positive_stage","full_4b_requires_non_price_evidence","local_4b_watch_guard","high_MAE_guardrail"],"residual_error_types_found":["software_security_theme_without_contract_retention_bridge","database_AI_theme_high_MAE","procurement_SaaS_winner_needs_4B_watch"],"loop_contribution_label":"canonical_archetype_rule_candidate","do_not_propose_new_weight_delta":false}
```

## 21. Deferred Coding Agent Handoff Prompt

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
- price-only/software-security-theme-only rows cannot promote Stage2/Stage3.
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
11. Add validation that C28 software/security rows cannot promote without enterprise contract, renewal/retention, recurring revenue, backlog-to-revenue, customer-quality evidence, margin conversion, FCF/cash conversion, or earnings-revision bridge.
12. Add validation that 1Y/2Y windows after 357880's 2024-11 and 2024-12 corporate-action candidates are not used unless adjusted/clean.

### Expected output

- Concise implementation summary.
- Rows accepted/rejected.
- New sector/canonical archetype coverage.
- Existing axis strengthened/weakened/kept.
- No investment recommendation language.

## 22. Next Round State

```text
completed_round = R8
completed_loop = 74
next_round = R9
next_loop = 74
round_schedule_status = valid
round_sector_consistency = pass
```

## 23. Source Notes

```text
MAIN EXECUTION PROMPT:
docs/core/e2r_v12_prompt_round_scheduler_corrected.txt

NO-REPEAT INDEX:
docs/core/V12_Research_No_Repeat_Index.md

Stock-web:
atlas/manifest.json
atlas/schema.json
atlas/symbol_profiles/058/058970.json
atlas/symbol_profiles/357/357880.json
atlas/symbol_profiles/150/150900.json
atlas/ohlcv_tradable_by_symbol_year/058/058970/2023.csv
atlas/ohlcv_tradable_by_symbol_year/357/357880/2024.csv
atlas/ohlcv_tradable_by_symbol_year/150/150900/2024.csv
```

This loop continues loop 74 with R8 and adds 3 new independent C28 representative cases, 1 positive, 2 counterexamples, and 1 canonical-archetype residual guard candidate for R8/L8.
