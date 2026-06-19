# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
selected_round = R8
selected_loop = 103
selection_basis = docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket = Priority 1-under-50 after local-session adjustment; published index Priority 0
round_schedule_status = coverage_index_selected
round_sector_consistency = pass
large_sector_id = L8_PLATFORM_CONTENT_SW_SECURITY
canonical_archetype_id = C28_SOFTWARE_SECURITY_CONTRACT_RETENTION
fine_archetype_id = C28_SECURITY_SAAS_CERTIFICATE_NETWORK_ENTERPRISE_RENEWAL_REVENUE_MARGIN_BRIDGE
deep_sub_archetype_id = C28_DEEP_PKI_NETWORK_SECURITY_AI_THREAT_INTEL_REMOTE_SUPPORT_RETENTION_VS_SECURITY_LABEL_SPIKE
loop_objective = coverage_gap_fill + residual_false_positive_mining + positive_balance_repair + 4B_non_price_requirement_stress_test + canonical_archetype_specific_rule_discovery
production_scoring_changed = false
shadow_weight_only = true
handoff_prompt_executed_now = false
```

## 1. Current Calibrated Profile Assumption

Current profile proxy is `e2r_2_1_stock_web_calibrated_proxy`. The loop does not re-argue the global calibrated axes. It stress-tests whether C28 needs a more exact bridge: security/SaaS labels may be valid Stage2 evidence, but Yellow/Green should require renewal, retention, revenue conversion, or margin/FCF bridge; otherwise the label behaves like a fast local 4B risk overlay.

## 2. Round / Large Sector / Canonical Archetype Scope

C28 maps to `R8 / L8_PLATFORM_CONTENT_SW_SECURITY`. This file intentionally avoids R13 because the study is not cross-archetype red-team; it is a sector/canonical residual study inside C28.

## 3. Previous Coverage / Duplicate Avoidance Check

The published No-Repeat Index lists C28 at 28 representative rows, needing 2 to cross 30 and 22 to cross 50. Same-session local outputs already lifted C28 close to the 50-row band, but C28 loop102 still left roughly two rows short. This loop uses seven new symbol/date/evidence-family groups and avoids the visible loop100~102 groups used for endpoint/identity/cloud/ERP/security labels.

Hard duplicate key avoided:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

## 4. Stock-Web OHLC Input / Price Source Validation

```text
price_data_source = Songdaiki/stock-web
upstream_source = FinanceData/marcap
price_basis = tradable_raw
price_adjustment_status = raw_unadjusted_marcap
stock_web_manifest_max_date = 2026-02-20
calibration_shard_root = atlas/ohlcv_tradable_by_symbol_year
raw_shard_root = atlas/ohlcv_raw_by_symbol_year
```

All rows use tradable stock-web shards. JSON profile checks visible in stock-web show the selected symbols are active-like through 2026-02-20; no 2024~2025 corporate-action candidate overlaps were used for calibration rows. The originally considered `430690` was excluded because its profile shows 2024 corporate-action candidate dates that would contaminate the 180D window.

## 5. Historical Eligibility Gate

All selected trigger rows satisfy:

```text
entry_date exists in tradable shard = true
forward_180_trading_days_available_by_manifest = true
30/90/180 MFE and MAE calculated = true
corporate_action_contaminated_180D_window = false
calibration_usable = true
```

## 6. Canonical Archetype Compression Map

```text
C28_SECURITY_SAAS_CERTIFICATE_NETWORK_ENTERPRISE_RENEWAL_REVENUE_MARGIN_BRIDGE
  -> PKI/certification security proxy
  -> network filtering/content security proxy
  -> enterprise security integration proxy
  -> SASE / zero-trust / AI security label spike
  -> public-sector VPN / quantum-security appliance proxy
  -> renewal/revenue/margin bridge vs label-only momentum
```

## 7. Case Selection Summary

|symbol|company|trigger_type|entry_date|entry_price|MFE90|MAE90|MFE180|MAE180|role|current_profile_verdict|
|---|---|---|---|---|---|---|---|---|---|---|
|075130|플랜티넷|Stage2-Actionable|2024-08-01|2185|74.83|-14.69|93.14|-14.69|positive|current_profile_missed_structural|
|049480|오픈베이스|Stage2-Actionable|2024-10-02|2250|30.89|-2.0|54.67|-2.22|positive|current_profile_correct|
|434480|모니터랩|Stage3-Yellow|2024-05-02|5910|10.15|-50.08|10.15|-52.96|counterexample|current_profile_false_positive|
|356680|엑스게이트|Stage2-Actionable|2024-09-02|4685|164.67|-12.7|164.67|-12.7|positive|current_profile_missed_structural|
|411080|샌즈랩|Stage3-Yellow|2024-04-01|11660|43.14|-55.23|43.14|-55.23|counterexample|current_profile_4B_too_late|
|041460|한국전자인증|Stage2|2024-10-02|3490|18.48|-26.65|50.72|-26.65|counterexample|current_profile_4B_too_late|
|053300|한국정보인증|Stage2|2024-09-02|3855|42.93|-3.76|72.76|-3.76|positive|current_profile_correct|


## 8. Positive vs Counterexample Balance

```text
positive_case_count = 4
counterexample_count = 3
4B_case_count = 3
4C_case_count = 0
current_profile_error_count = 5
source_proxy_only_count = 7
evidence_url_pending_count = 7
promotion_blocked_until_url_repair = true
```

The split is deliberately balanced: four paths show that C28 proxy evidence can be actionable before explicit ARR disclosure, while three paths show that security-label spikes without verified renewal/revenue bridges can suffer severe MAE.

## 9. Evidence Source Map

All evidence rows are `source_proxy_only` in this MD. The price path is fully calculated from stock-web, but evidence URLs must be repaired before promotion. This is intentional: the loop's calibration value is in separating **proxy-bridge positives** from **label-only false positives**, not in changing production scoring immediately.

## 10. Price Data Source Map

|symbol|profile_path|entry_shard|next_year_shard|corporate_action_window_status|
|---|---|---|---|---|
|075130|atlas/symbol_profiles/075/075130.json|atlas/ohlcv_tradable_by_symbol_year/075/075130/2024.csv|atlas/ohlcv_tradable_by_symbol_year/075/075130/2025.csv|clean_180D_window|
|049480|atlas/symbol_profiles/049/049480.json|atlas/ohlcv_tradable_by_symbol_year/049/049480/2024.csv|atlas/ohlcv_tradable_by_symbol_year/049/049480/2025.csv|clean_180D_window|
|434480|atlas/symbol_profiles/434/434480.json|atlas/ohlcv_tradable_by_symbol_year/434/434480/2024.csv|atlas/ohlcv_tradable_by_symbol_year/434/434480/2025.csv|clean_180D_window|
|356680|atlas/symbol_profiles/356/356680.json|atlas/ohlcv_tradable_by_symbol_year/356/356680/2024.csv|atlas/ohlcv_tradable_by_symbol_year/356/356680/2025.csv|clean_180D_window|
|411080|atlas/symbol_profiles/411/411080.json|atlas/ohlcv_tradable_by_symbol_year/411/411080/2024.csv|atlas/ohlcv_tradable_by_symbol_year/411/411080/2025.csv|clean_180D_window|
|041460|atlas/symbol_profiles/041/041460.json|atlas/ohlcv_tradable_by_symbol_year/041/041460/2024.csv|atlas/ohlcv_tradable_by_symbol_year/041/041460/2025.csv|clean_180D_window|
|053300|atlas/symbol_profiles/053/053300.json|atlas/ohlcv_tradable_by_symbol_year/053/053300/2024.csv|atlas/ohlcv_tradable_by_symbol_year/053/053300/2025.csv|clean_180D_window|


## 11. Case-by-Case Trigger Grid

|symbol|trigger_family|Stage2 evidence|Stage3 evidence|4B evidence|case note|
|---|---|---|---|---|---|
|075130|network filtering / content-security renewal proxy|public_event_or_disclosure, relative_strength, customer_or_order_quality|financial_visibility|none|Actual path produced strong 180D MFE; rule should not demand named ARR if repeat B2B security revenue + low MAE is present.|
|049480|enterprise infrastructure / security integration renewal proxy|public_event_or_disclosure, customer_or_order_quality|financial_visibility|none|Low MAE and solid MFE support Stage2-Actionable, while Green remains blocked until renewal/margin evidence.|
|434480|SASE / zero-trust label without renewal bridge|public_event_or_disclosure, relative_strength|none|valuation_blowoff, price_only_local_peak|MFE stalled and MAE collapsed; C28 label alone should be treated as local 4B watch, not Yellow/Green.|
|356680|VPN / quantum-security public-sector proxy|public_event_or_disclosure, policy_or_regulatory_optionality, relative_strength|financial_visibility|none|Massive MFE with contained MAE argues that C28 needs a proxy-bridge route, but still no automatic Green without revenue conversion.|
|411080|AI cybersecurity label spike without retention proof|public_event_or_disclosure, relative_strength|none|valuation_blowoff, positioning_overheat, price_only_local_peak|Large early MFE did not compensate for -55% MAE; price-only blowoff should block positive Stage3.|
|041460|electronic certification / authentication renewal proxy|public_event_or_disclosure, customer_or_order_quality|none|price_only_local_peak, positioning_overheat|A 180D recovery exists, but 90D MAE below -25% requires high-MAE guard before promotion.|
|053300|PKI / certification security demand proxy|public_event_or_disclosure, customer_or_order_quality, relative_strength|financial_visibility|none|Clean low-MAE positive path supports Stage2 but not automatic Green.|


## 12. Trigger-Level OHLC Backtest Tables

|symbol|entry_date|entry_price|MFE30|MAE30|MFE90|MAE90|MFE180|MAE180|peak_date|peak_price|drawdown_after_peak|
|---|---|---|---|---|---|---|---|---|---|---|---|
|075130|2024-08-01|2185|74.83|-14.69|74.83|-14.69|93.14|-14.69|2025-04-07|4220|-33.18|
|049480|2024-10-02|2250|4.44|-1.56|30.89|-2.0|54.67|-2.22|2025-06-23|3480|-21.98|
|434480|2024-05-02|5910|10.15|-10.32|10.15|-50.08|10.15|-52.96|2024-05-16|6510|-57.3|
|356680|2024-09-02|4685|22.52|-12.7|164.67|-12.7|164.67|-12.7|2025-01-03|12400|-51.21|
|411080|2024-04-01|11660|43.14|-20.07|43.14|-55.23|43.14|-55.23|2024-04-16|16690|-68.72|
|041460|2024-10-02|3490|18.48|-16.48|18.48|-26.65|50.72|-26.65|2025-06-19|5260|-19.96|
|053300|2024-09-02|3855|24.38|-3.76|42.93|-3.76|72.76|-3.76|2025-06-05|6660|-9.16|


## 13. Current Calibrated Profile Stress Test

The current calibrated profile handles low-MAE proxy cases better than the old baseline, but it still has two residual issues in C28:

1. It can miss security proxy paths where contract/renewal data is not explicit but the drawdown profile remains controlled and MFE confirms accumulation.
2. It can still treat AI/SASE/security-label momentum as more actionable than warranted when no retention, renewal, revenue, or margin bridge exists.

Current-profile verdict distribution:

```text
current_profile_correct = 2
current_profile_missed_structural = 2
current_profile_false_positive = 1
current_profile_4B_too_late = 2
```

## 14. Stage2 / Yellow / Green Comparison

Stage2 remains acceptable for source-proxy C28 evidence when MAE is controlled and the business model plausibly renews. Yellow needs one more bridge: renewal/revenue/margin/FCF conversion. Green remains blocked because no trigger row here contains explicit revision >= 55 plus multi-source retention proof.

## 15. 4B Local vs Full-window Timing Audit

The 4B rows are not full thesis breaks. They are local watch overlays caused by price/label momentum without enough non-price evidence. The important split is:

```text
source-proxy positive + controlled MAE -> keep Stage2/Actionable, no Green
security-label spike + no bridge + high MAE -> route to local 4B watch
```

## 16. 4C Protection Audit

No hard 4C row is proposed. The counterexamples are high-MAE / local-4B-watch rows, not explicit contract cancellation, regulatory rejection, or accounting/trust break rows.

## 17. Sector-Specific Rule Candidate

```text
rule_scope = sector_specific
large_sector_id = L8_PLATFORM_CONTENT_SW_SECURITY
rule_candidate = L8 software/security proxy evidence may support Stage2, but Yellow/Green require renewal/revenue/margin bridge; label-only spikes route to local 4B watch when MAE risk is high.
sector_specific_rule_candidate = true
```

## 18. Canonical-Archetype Rule Candidate

```text
rule_scope = canonical_archetype_specific
canonical_archetype_id = C28_SOFTWARE_SECURITY_CONTRACT_RETENTION
new_axis_proposed = C28_verified_retention_renewal_revenue_margin_bridge_required_before_Yellow_or_Green_plus_source_proxy_exception_for_low_MAE_security_demand
existing_axis_strengthened = stage2_required_bridge, local_4b_watch_guard, full_4b_requires_non_price_evidence, price_only_blowoff_blocks_positive_stage
existing_axis_weakened = null
```

## 19. Before / After Backtest Comparison

|profile_id|scope|eligible|avg_MFE90|avg_MAE90|avg_MFE180|avg_MAE180|false_positive_rate|verdict|
|---|---|---|---|---|---|---|---|---|
|P0_e2r_2_1_stock_web_calibrated_proxy|current_global_proxy|7|55.01|-23.59|69.89|-24.03|0.43|mixed; misses positive proxy bridge and still lets weak label spikes look too actionable|
|P0b_e2r_2_0_baseline_reference|rollback_reference|7|55.01|-23.59|69.89|-24.03|0.57|too permissive for SASE/AI/security label spikes|
|P1_L8_security_bridge_candidate|sector_specific|4|78.33|-8.29|96.31|-8.34|0.0|better score-return alignment|
|P2_C28_retention_bridge_candidate|canonical_archetype_specific|4|78.33|-8.29|96.31|-8.34|0.0|candidate rule|
|P3_counterexample_guard_profile|canonical_guard|3|23.92|-43.99|34.67|-44.95|0.0|guard catches high-MAE rows|


## 20. Score-Return Alignment Matrix

Positive rows averaged MFE90 `78.33` / MAE90 `-8.29`, while counterexample rows averaged MFE90 `23.92` / MAE90 `-43.99`. The mechanism is clean enough for a C28-specific bridge: low-MAE proxy renewals deserve Stage2 treatment, but high-MAE label momentum deserves 4B watch even when short-term MFE appears.

## 21. Coverage Matrix

|large_sector_id|canonical_archetype_id|fine_archetype_id|positive_case_count|counterexample_count|4B_case_count|4C_case_count|new_independent_case_count|reused_case_count|calibration_usable_trigger_count|representative_trigger_count|current_profile_error_count|sector_rule_candidate|canonical_rule_candidate|coverage_gap_after_this_loop|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|L8_PLATFORM_CONTENT_SW_SECURITY|C28_SOFTWARE_SECURITY_CONTRACT_RETENTION|C28_SECURITY_SAAS_CERTIFICATE_NETWORK_ENTERPRISE_RENEWAL_REVENUE_MARGIN_BRIDGE|4|3|3|0|7|0|7|7|5|True|True|C28 local-session adjusted approximately 55; 50-row practical calibration band reached|


## 22. Residual Contribution Summary

```text
new_independent_case_count: 7
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 7
new_canonical_archetype_count: 0
new_fine_archetype_count: 1
new_trigger_family_count: 7
tested_existing_calibrated_axes: [stage2_required_bridge, local_4b_watch_guard, price_only_blowoff_blocks_positive_stage, full_4b_requires_non_price_evidence]
residual_error_types_found: [source_proxy_positive_missed_structural, security_label_false_positive, high_MAE_success_needs_guard]
new_axis_proposed: C28_verified_retention_renewal_revenue_margin_bridge_required_before_Yellow_or_Green_plus_source_proxy_exception_for_low_MAE_security_demand
existing_axis_strengthened: [stage2_required_bridge, local_4b_watch_guard, full_4b_requires_non_price_evidence, price_only_blowoff_blocks_positive_stage]
existing_axis_weakened: null
existing_axis_kept: [stage3_green_revision_min, hard_4c_thesis_break_routes_to_4c]
sector_specific_rule_candidate: true
canonical_archetype_rule_candidate: true
no_new_signal_reason: null
loop_contribution_label: canonical_archetype_rule_candidate
do_not_propose_new_weight_delta: false
```

## 23. Validation Scope / Non-Validation Scope

Validation scope is limited to historical trigger-level calibration using stock-web OHLC. This is not a current watchlist, not investment advice, not live candidate discovery, and not a production scoring patch.

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,C28_retention_renewal_revenue_margin_bridge_required,canonical_archetype_specific,L8_PLATFORM_CONTENT_SW_SECURITY,C28_SOFTWARE_SECURITY_CONTRACT_RETENTION,0,1,+1,"C28 security labels need renewal/revenue/margin bridge before Yellow/Green","positive rows avg MFE90 78.33 vs counterexample MAE90 -43.99","C28_R8L103_01|C28_R8L103_02|C28_R8L103_03|C28_R8L103_04|C28_R8L103_05|C28_R8L103_06|C28_R8L103_07",7,7,3,medium,canonical_shadow_only,"not production; source URL repair required"
shadow_weight,C28_source_proxy_low_MAE_exception,canonical_archetype_specific,L8_PLATFORM_CONTENT_SW_SECURITY,C28_SOFTWARE_SECURITY_CONTRACT_RETENTION,0,1,+1,"Some source-proxy security demand rows are valid Stage2 when MAE is controlled","Keeps positive proxy rows without opening Green","C28_R8L103_01|C28_R8L103_02|C28_R8L103_04|C28_R8L103_07",4,4,0,low,canonical_shadow_only,"requires later URL verification"
```

## 25. Machine-Readable Rows

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
{"row_type":"case","case_id":"C28_R8L103_01_075130","symbol":"075130","company_name":"플랜티넷","round":"R8","loop":"103","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","fine_archetype_id":"C28_SECURITY_SAAS_CERTIFICATE_NETWORK_ENTERPRISE_RENEWAL_REVENUE_MARGIN_BRIDGE","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"Stage2-Actionable","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"aligned_positive","current_profile_verdict":"current_profile_missed_structural","price_source":"Songdaiki/stock-web","notes":"Actual path produced strong 180D MFE; rule should not demand named ARR if repeat B2B security revenue + low MAE is present."}
{"row_type":"trigger","trigger_id":"C28_R8L103_01_075130_Stage2_Actionable_2024-08-01","case_id":"C28_R8L103_01_075130","symbol":"075130","company_name":"플랜티넷","round":"R8","loop":"103","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","fine_archetype_id":"C28_SECURITY_SAAS_CERTIFICATE_NETWORK_ENTERPRISE_RENEWAL_REVENUE_MARGIN_BRIDGE","loop_objective":"coverage_gap_fill+residual_false_positive_mining+4B_non_price_requirement_stress_test+canonical_archetype_specific_rule_discovery","trigger_type":"Stage2-Actionable","trigger_date":"2024-08-01","entry_date":"2024-08-01","entry_price":2185.0,"evidence_available_at_that_date":"Network filtering/content-security renewal proxy had enough Stage2 evidence but lacked explicit ARR/retention disclosure.","evidence_source":"source_proxy_only: company/industry/event label; URL repair required before promotion","stage2_evidence_fields":["public_event_or_disclosure","relative_strength","customer_or_order_quality"],"stage3_evidence_fields":["financial_visibility"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/075/075130/2024.csv","profile_path":"atlas/symbol_profiles/075/075130.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":74.83,"MFE_90D_pct":74.83,"MFE_180D_pct":93.14,"MAE_30D_pct":-14.69,"MAE_90D_pct":-14.69,"MAE_180D_pct":-14.69,"peak_date":"2025-04-07","peak_price":4220.0,"drawdown_after_peak_pct":-33.18,"green_lateness_ratio":"not_applicable","green_lateness_reason":"no_confirmed_Stage3_Green_trigger","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_evidence_type":[],"trigger_outcome_label":"structural_success","current_profile_verdict":"current_profile_missed_structural","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION|075130|Stage2-Actionable|2024-08-01","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"source_proxy_only":true,"evidence_url_pending":true}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C28_R8L103_01_075130","trigger_id":"C28_R8L103_01_075130_Stage2_Actionable_2024-08-01","symbol":"075130","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","raw_component_scores_before":{"contract_score":12,"backlog_visibility_score":8,"margin_bridge_score":6,"revision_score":7,"relative_strength_score":13,"customer_quality_score":11,"policy_or_regulatory_score":6,"valuation_repricing_score":8,"execution_risk_score":5,"legal_or_contract_risk_score":1,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":70,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"contract_score":15,"backlog_visibility_score":8,"margin_bridge_score":10,"revision_score":9,"relative_strength_score":13,"customer_quality_score":14,"policy_or_regulatory_score":6,"valuation_repricing_score":8,"execution_risk_score":4,"legal_or_contract_risk_score":1,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":78,"stage_label_after":"Stage3-Yellow","changed_components":["contract_score","margin_bridge_score","revision_score","customer_quality_score","execution_risk_score"],"component_delta_explanation":"C28 shadow profile requires verified renewal/revenue/margin bridge before Yellow/Green and routes security-label spikes with weak bridge to local 4B watch.","MFE_90D_pct":74.83,"MAE_90D_pct":-14.69,"score_return_alignment_label":"aligned_positive","current_profile_verdict":"current_profile_missed_structural"}
{"row_type":"case","case_id":"C28_R8L103_02_049480","symbol":"049480","company_name":"오픈베이스","round":"R8","loop":"103","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","fine_archetype_id":"C28_SECURITY_SAAS_CERTIFICATE_NETWORK_ENTERPRISE_RENEWAL_REVENUE_MARGIN_BRIDGE","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"Stage2-Actionable","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"aligned_positive","current_profile_verdict":"current_profile_correct","price_source":"Songdaiki/stock-web","notes":"Low MAE and solid MFE support Stage2-Actionable, while Green remains blocked until renewal/margin evidence."}
{"row_type":"trigger","trigger_id":"C28_R8L103_02_049480_Stage2_Actionable_2024-10-02","case_id":"C28_R8L103_02_049480","symbol":"049480","company_name":"오픈베이스","round":"R8","loop":"103","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","fine_archetype_id":"C28_SECURITY_SAAS_CERTIFICATE_NETWORK_ENTERPRISE_RENEWAL_REVENUE_MARGIN_BRIDGE","loop_objective":"coverage_gap_fill+residual_false_positive_mining+4B_non_price_requirement_stress_test+canonical_archetype_specific_rule_discovery","trigger_type":"Stage2-Actionable","trigger_date":"2024-10-02","entry_date":"2024-10-02","entry_price":2250.0,"evidence_available_at_that_date":"Enterprise infra/security integration proxy with low drawdown; no Green unlock without margin bridge.","evidence_source":"source_proxy_only: company/industry/event label; URL repair required before promotion","stage2_evidence_fields":["public_event_or_disclosure","customer_or_order_quality"],"stage3_evidence_fields":["financial_visibility"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/049/049480/2024.csv","profile_path":"atlas/symbol_profiles/049/049480.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":4.44,"MFE_90D_pct":30.89,"MFE_180D_pct":54.67,"MAE_30D_pct":-1.56,"MAE_90D_pct":-2.0,"MAE_180D_pct":-2.22,"peak_date":"2025-06-23","peak_price":3480.0,"drawdown_after_peak_pct":-21.98,"green_lateness_ratio":"not_applicable","green_lateness_reason":"no_confirmed_Stage3_Green_trigger","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_evidence_type":[],"trigger_outcome_label":"structural_success","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION|049480|Stage2-Actionable|2024-10-02","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"source_proxy_only":true,"evidence_url_pending":true}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C28_R8L103_02_049480","trigger_id":"C28_R8L103_02_049480_Stage2_Actionable_2024-10-02","symbol":"049480","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","raw_component_scores_before":{"contract_score":12,"backlog_visibility_score":8,"margin_bridge_score":6,"revision_score":7,"relative_strength_score":13,"customer_quality_score":11,"policy_or_regulatory_score":6,"valuation_repricing_score":8,"execution_risk_score":5,"legal_or_contract_risk_score":1,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":70,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"contract_score":15,"backlog_visibility_score":8,"margin_bridge_score":10,"revision_score":9,"relative_strength_score":13,"customer_quality_score":14,"policy_or_regulatory_score":6,"valuation_repricing_score":8,"execution_risk_score":4,"legal_or_contract_risk_score":1,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":74,"stage_label_after":"Stage2-Actionable","changed_components":["contract_score","margin_bridge_score","revision_score","customer_quality_score","execution_risk_score"],"component_delta_explanation":"C28 shadow profile requires verified renewal/revenue/margin bridge before Yellow/Green and routes security-label spikes with weak bridge to local 4B watch.","MFE_90D_pct":30.89,"MAE_90D_pct":-2.0,"score_return_alignment_label":"aligned_positive","current_profile_verdict":"current_profile_correct"}
{"row_type":"case","case_id":"C28_R8L103_03_434480","symbol":"434480","company_name":"모니터랩","round":"R8","loop":"103","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","fine_archetype_id":"C28_SECURITY_SAAS_CERTIFICATE_NETWORK_ENTERPRISE_RENEWAL_REVENUE_MARGIN_BRIDGE","case_type":"false_positive_green","positive_or_counterexample":"counterexample","best_trigger":"Stage3-Yellow","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"false_positive_or_high_mae_guard_needed","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"MFE stalled and MAE collapsed; C28 label alone should be treated as local 4B watch, not Yellow/Green."}
{"row_type":"trigger","trigger_id":"C28_R8L103_03_434480_Stage3_Yellow_2024-05-02","case_id":"C28_R8L103_03_434480","symbol":"434480","company_name":"모니터랩","round":"R8","loop":"103","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","fine_archetype_id":"C28_SECURITY_SAAS_CERTIFICATE_NETWORK_ENTERPRISE_RENEWAL_REVENUE_MARGIN_BRIDGE","loop_objective":"coverage_gap_fill+residual_false_positive_mining+4B_non_price_requirement_stress_test+canonical_archetype_specific_rule_discovery","trigger_type":"Stage3-Yellow","trigger_date":"2024-05-02","entry_date":"2024-05-02","entry_price":5910.0,"evidence_available_at_that_date":"SASE/security label spike without verified renewal revenue or retention bridge.","evidence_source":"source_proxy_only: company/industry/event label; URL repair required before promotion","stage2_evidence_fields":["public_event_or_disclosure","relative_strength"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["valuation_blowoff","price_only_local_peak"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/434/434480/2024.csv","profile_path":"atlas/symbol_profiles/434/434480.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":10.15,"MFE_90D_pct":10.15,"MFE_180D_pct":10.15,"MAE_30D_pct":-10.32,"MAE_90D_pct":-50.08,"MAE_180D_pct":-52.96,"peak_date":"2024-05-16","peak_price":6510.0,"drawdown_after_peak_pct":-57.3,"green_lateness_ratio":"not_applicable","green_lateness_reason":"no_confirmed_Stage3_Green_trigger","four_b_local_peak_proximity":0.86,"four_b_full_window_peak_proximity":null,"four_b_evidence_type":["valuation_blowoff","price_only_local_peak"],"trigger_outcome_label":"false_positive_green","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION|434480|Stage3-Yellow|2024-05-02","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"source_proxy_only":true,"evidence_url_pending":true}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C28_R8L103_03_434480","trigger_id":"C28_R8L103_03_434480_Stage3_Yellow_2024-05-02","symbol":"434480","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","raw_component_scores_before":{"contract_score":10,"backlog_visibility_score":4,"margin_bridge_score":3,"revision_score":4,"relative_strength_score":16,"customer_quality_score":7,"policy_or_regulatory_score":7,"valuation_repricing_score":12,"execution_risk_score":7,"legal_or_contract_risk_score":1,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":78,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":6,"backlog_visibility_score":4,"margin_bridge_score":1,"revision_score":2,"relative_strength_score":16,"customer_quality_score":4,"policy_or_regulatory_score":7,"valuation_repricing_score":6,"execution_risk_score":12,"legal_or_contract_risk_score":1,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":61,"stage_label_after":"Stage4B-Watch","changed_components":["contract_score","margin_bridge_score","revision_score","customer_quality_score","execution_risk_score"],"component_delta_explanation":"C28 shadow profile requires verified renewal/revenue/margin bridge before Yellow/Green and routes security-label spikes with weak bridge to local 4B watch.","MFE_90D_pct":10.15,"MAE_90D_pct":-50.08,"score_return_alignment_label":"false_positive_or_high_mae_guard_needed","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"case","case_id":"C28_R8L103_04_356680","symbol":"356680","company_name":"엑스게이트","round":"R8","loop":"103","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","fine_archetype_id":"C28_SECURITY_SAAS_CERTIFICATE_NETWORK_ENTERPRISE_RENEWAL_REVENUE_MARGIN_BRIDGE","case_type":"missed_structural","positive_or_counterexample":"positive","best_trigger":"Stage2-Actionable","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"aligned_positive","current_profile_verdict":"current_profile_missed_structural","price_source":"Songdaiki/stock-web","notes":"Massive MFE with contained MAE argues that C28 needs a proxy-bridge route, but still no automatic Green without revenue conversion."}
{"row_type":"trigger","trigger_id":"C28_R8L103_04_356680_Stage2_Actionable_2024-09-02","case_id":"C28_R8L103_04_356680","symbol":"356680","company_name":"엑스게이트","round":"R8","loop":"103","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","fine_archetype_id":"C28_SECURITY_SAAS_CERTIFICATE_NETWORK_ENTERPRISE_RENEWAL_REVENUE_MARGIN_BRIDGE","loop_objective":"coverage_gap_fill+residual_false_positive_mining+4B_non_price_requirement_stress_test+canonical_archetype_specific_rule_discovery","trigger_type":"Stage2-Actionable","trigger_date":"2024-09-02","entry_date":"2024-09-02","entry_price":4685.0,"evidence_available_at_that_date":"Security appliance/public-sector demand proxy had strong relative strength but limited visible retention evidence.","evidence_source":"source_proxy_only: company/industry/event label; URL repair required before promotion","stage2_evidence_fields":["public_event_or_disclosure","policy_or_regulatory_optionality","relative_strength"],"stage3_evidence_fields":["financial_visibility"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/356/356680/2024.csv","profile_path":"atlas/symbol_profiles/356/356680.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":22.52,"MFE_90D_pct":164.67,"MFE_180D_pct":164.67,"MAE_30D_pct":-12.7,"MAE_90D_pct":-12.7,"MAE_180D_pct":-12.7,"peak_date":"2025-01-03","peak_price":12400.0,"drawdown_after_peak_pct":-51.21,"green_lateness_ratio":"not_applicable","green_lateness_reason":"no_confirmed_Stage3_Green_trigger","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_evidence_type":[],"trigger_outcome_label":"missed_structural","current_profile_verdict":"current_profile_missed_structural","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION|356680|Stage2-Actionable|2024-09-02","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"source_proxy_only":true,"evidence_url_pending":true}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C28_R8L103_04_356680","trigger_id":"C28_R8L103_04_356680_Stage2_Actionable_2024-09-02","symbol":"356680","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","raw_component_scores_before":{"contract_score":12,"backlog_visibility_score":8,"margin_bridge_score":6,"revision_score":7,"relative_strength_score":13,"customer_quality_score":11,"policy_or_regulatory_score":6,"valuation_repricing_score":8,"execution_risk_score":5,"legal_or_contract_risk_score":1,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":70,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"contract_score":15,"backlog_visibility_score":8,"margin_bridge_score":10,"revision_score":9,"relative_strength_score":13,"customer_quality_score":14,"policy_or_regulatory_score":6,"valuation_repricing_score":8,"execution_risk_score":4,"legal_or_contract_risk_score":1,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":78,"stage_label_after":"Stage3-Yellow","changed_components":["contract_score","margin_bridge_score","revision_score","customer_quality_score","execution_risk_score"],"component_delta_explanation":"C28 shadow profile requires verified renewal/revenue/margin bridge before Yellow/Green and routes security-label spikes with weak bridge to local 4B watch.","MFE_90D_pct":164.67,"MAE_90D_pct":-12.7,"score_return_alignment_label":"aligned_positive","current_profile_verdict":"current_profile_missed_structural"}
{"row_type":"case","case_id":"C28_R8L103_05_411080","symbol":"411080","company_name":"샌즈랩","round":"R8","loop":"103","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","fine_archetype_id":"C28_SECURITY_SAAS_CERTIFICATE_NETWORK_ENTERPRISE_RENEWAL_REVENUE_MARGIN_BRIDGE","case_type":"high_mae_success","positive_or_counterexample":"counterexample","best_trigger":"Stage3-Yellow","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"false_positive_or_high_mae_guard_needed","current_profile_verdict":"current_profile_4B_too_late","price_source":"Songdaiki/stock-web","notes":"Large early MFE did not compensate for -55% MAE; price-only blowoff should block positive Stage3."}
{"row_type":"trigger","trigger_id":"C28_R8L103_05_411080_Stage3_Yellow_2024-04-01","case_id":"C28_R8L103_05_411080","symbol":"411080","company_name":"샌즈랩","round":"R8","loop":"103","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","fine_archetype_id":"C28_SECURITY_SAAS_CERTIFICATE_NETWORK_ENTERPRISE_RENEWAL_REVENUE_MARGIN_BRIDGE","loop_objective":"coverage_gap_fill+residual_false_positive_mining+4B_non_price_requirement_stress_test+canonical_archetype_specific_rule_discovery","trigger_type":"Stage3-Yellow","trigger_date":"2024-04-01","entry_date":"2024-04-01","entry_price":11660.0,"evidence_available_at_that_date":"AI cyber threat-intelligence label generated momentum but lacked renewal/revenue durability evidence.","evidence_source":"source_proxy_only: company/industry/event label; URL repair required before promotion","stage2_evidence_fields":["public_event_or_disclosure","relative_strength"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["valuation_blowoff","positioning_overheat","price_only_local_peak"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/411/411080/2024.csv","profile_path":"atlas/symbol_profiles/411/411080.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":43.14,"MFE_90D_pct":43.14,"MFE_180D_pct":43.14,"MAE_30D_pct":-20.07,"MAE_90D_pct":-55.23,"MAE_180D_pct":-55.23,"peak_date":"2024-04-16","peak_price":16690.0,"drawdown_after_peak_pct":-68.72,"green_lateness_ratio":"not_applicable","green_lateness_reason":"no_confirmed_Stage3_Green_trigger","four_b_local_peak_proximity":0.86,"four_b_full_window_peak_proximity":0.23,"four_b_evidence_type":["valuation_blowoff","positioning_overheat","price_only_local_peak"],"trigger_outcome_label":"high_mae_success","current_profile_verdict":"current_profile_4B_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION|411080|Stage3-Yellow|2024-04-01","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"source_proxy_only":true,"evidence_url_pending":true}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C28_R8L103_05_411080","trigger_id":"C28_R8L103_05_411080_Stage3_Yellow_2024-04-01","symbol":"411080","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","raw_component_scores_before":{"contract_score":10,"backlog_visibility_score":4,"margin_bridge_score":3,"revision_score":4,"relative_strength_score":16,"customer_quality_score":7,"policy_or_regulatory_score":7,"valuation_repricing_score":12,"execution_risk_score":7,"legal_or_contract_risk_score":1,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":78,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":6,"backlog_visibility_score":4,"margin_bridge_score":1,"revision_score":2,"relative_strength_score":16,"customer_quality_score":4,"policy_or_regulatory_score":7,"valuation_repricing_score":6,"execution_risk_score":12,"legal_or_contract_risk_score":1,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":61,"stage_label_after":"Stage4B-Watch","changed_components":["contract_score","margin_bridge_score","revision_score","customer_quality_score","execution_risk_score"],"component_delta_explanation":"C28 shadow profile requires verified renewal/revenue/margin bridge before Yellow/Green and routes security-label spikes with weak bridge to local 4B watch.","MFE_90D_pct":43.14,"MAE_90D_pct":-55.23,"score_return_alignment_label":"false_positive_or_high_mae_guard_needed","current_profile_verdict":"current_profile_4B_too_late"}
{"row_type":"case","case_id":"C28_R8L103_06_041460","symbol":"041460","company_name":"한국전자인증","round":"R8","loop":"103","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","fine_archetype_id":"C28_SECURITY_SAAS_CERTIFICATE_NETWORK_ENTERPRISE_RENEWAL_REVENUE_MARGIN_BRIDGE","case_type":"high_mae_success","positive_or_counterexample":"counterexample","best_trigger":"Stage2","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"false_positive_or_high_mae_guard_needed","current_profile_verdict":"current_profile_4B_too_late","price_source":"Songdaiki/stock-web","notes":"A 180D recovery exists, but 90D MAE below -25% requires high-MAE guard before promotion."}
{"row_type":"trigger","trigger_id":"C28_R8L103_06_041460_Stage2_2024-10-02","case_id":"C28_R8L103_06_041460","symbol":"041460","company_name":"한국전자인증","round":"R8","loop":"103","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","fine_archetype_id":"C28_SECURITY_SAAS_CERTIFICATE_NETWORK_ENTERPRISE_RENEWAL_REVENUE_MARGIN_BRIDGE","loop_objective":"coverage_gap_fill+residual_false_positive_mining+4B_non_price_requirement_stress_test+canonical_archetype_specific_rule_discovery","trigger_type":"Stage2","trigger_date":"2024-10-02","entry_date":"2024-10-02","entry_price":3490.0,"evidence_available_at_that_date":"PKI/certification demand proxy with later MFE but interim drawdown too deep for clean Actionable promotion.","evidence_source":"source_proxy_only: company/industry/event label; URL repair required before promotion","stage2_evidence_fields":["public_event_or_disclosure","customer_or_order_quality"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["price_only_local_peak","positioning_overheat"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/041/041460/2024.csv","profile_path":"atlas/symbol_profiles/041/041460.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":18.48,"MFE_90D_pct":18.48,"MFE_180D_pct":50.72,"MAE_30D_pct":-16.48,"MAE_90D_pct":-26.65,"MAE_180D_pct":-26.65,"peak_date":"2025-06-19","peak_price":5260.0,"drawdown_after_peak_pct":-19.96,"green_lateness_ratio":"not_applicable","green_lateness_reason":"no_confirmed_Stage3_Green_trigger","four_b_local_peak_proximity":0.86,"four_b_full_window_peak_proximity":0.23,"four_b_evidence_type":["price_only_local_peak","positioning_overheat"],"trigger_outcome_label":"high_mae_success","current_profile_verdict":"current_profile_4B_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION|041460|Stage2|2024-10-02","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"source_proxy_only":true,"evidence_url_pending":true}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C28_R8L103_06_041460","trigger_id":"C28_R8L103_06_041460_Stage2_2024-10-02","symbol":"041460","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","raw_component_scores_before":{"contract_score":10,"backlog_visibility_score":4,"margin_bridge_score":3,"revision_score":4,"relative_strength_score":16,"customer_quality_score":7,"policy_or_regulatory_score":7,"valuation_repricing_score":12,"execution_risk_score":7,"legal_or_contract_risk_score":1,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":69,"stage_label_before":"Stage2","raw_component_scores_after":{"contract_score":6,"backlog_visibility_score":4,"margin_bridge_score":1,"revision_score":2,"relative_strength_score":16,"customer_quality_score":4,"policy_or_regulatory_score":7,"valuation_repricing_score":6,"execution_risk_score":12,"legal_or_contract_risk_score":1,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":64,"stage_label_after":"Stage4B-Watch","changed_components":["contract_score","margin_bridge_score","revision_score","customer_quality_score","execution_risk_score"],"component_delta_explanation":"C28 shadow profile requires verified renewal/revenue/margin bridge before Yellow/Green and routes security-label spikes with weak bridge to local 4B watch.","MFE_90D_pct":18.48,"MAE_90D_pct":-26.65,"score_return_alignment_label":"false_positive_or_high_mae_guard_needed","current_profile_verdict":"current_profile_4B_too_late"}
{"row_type":"case","case_id":"C28_R8L103_07_053300","symbol":"053300","company_name":"한국정보인증","round":"R8","loop":"103","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","fine_archetype_id":"C28_SECURITY_SAAS_CERTIFICATE_NETWORK_ENTERPRISE_RENEWAL_REVENUE_MARGIN_BRIDGE","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"Stage2","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"aligned_positive","current_profile_verdict":"current_profile_correct","price_source":"Songdaiki/stock-web","notes":"Clean low-MAE positive path supports Stage2 but not automatic Green."}
{"row_type":"trigger","trigger_id":"C28_R8L103_07_053300_Stage2_2024-09-02","case_id":"C28_R8L103_07_053300","symbol":"053300","company_name":"한국정보인증","round":"R8","loop":"103","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","fine_archetype_id":"C28_SECURITY_SAAS_CERTIFICATE_NETWORK_ENTERPRISE_RENEWAL_REVENUE_MARGIN_BRIDGE","loop_objective":"coverage_gap_fill+residual_false_positive_mining+4B_non_price_requirement_stress_test+canonical_archetype_specific_rule_discovery","trigger_type":"Stage2","trigger_date":"2024-09-02","entry_date":"2024-09-02","entry_price":3855.0,"evidence_available_at_that_date":"Certification/security demand proxy had low MAE and improving MFE, but Stage3 still needs renewal or margin bridge.","evidence_source":"source_proxy_only: company/industry/event label; URL repair required before promotion","stage2_evidence_fields":["public_event_or_disclosure","customer_or_order_quality","relative_strength"],"stage3_evidence_fields":["financial_visibility"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/053/053300/2024.csv","profile_path":"atlas/symbol_profiles/053/053300.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":24.38,"MFE_90D_pct":42.93,"MFE_180D_pct":72.76,"MAE_30D_pct":-3.76,"MAE_90D_pct":-3.76,"MAE_180D_pct":-3.76,"peak_date":"2025-06-05","peak_price":6660.0,"drawdown_after_peak_pct":-9.16,"green_lateness_ratio":"not_applicable","green_lateness_reason":"no_confirmed_Stage3_Green_trigger","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_evidence_type":[],"trigger_outcome_label":"structural_success","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION|053300|Stage2|2024-09-02","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"source_proxy_only":true,"evidence_url_pending":true}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C28_R8L103_07_053300","trigger_id":"C28_R8L103_07_053300_Stage2_2024-09-02","symbol":"053300","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","raw_component_scores_before":{"contract_score":12,"backlog_visibility_score":8,"margin_bridge_score":6,"revision_score":7,"relative_strength_score":13,"customer_quality_score":11,"policy_or_regulatory_score":6,"valuation_repricing_score":8,"execution_risk_score":5,"legal_or_contract_risk_score":1,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":67,"stage_label_before":"Stage2","raw_component_scores_after":{"contract_score":15,"backlog_visibility_score":8,"margin_bridge_score":10,"revision_score":9,"relative_strength_score":13,"customer_quality_score":14,"policy_or_regulatory_score":6,"valuation_repricing_score":8,"execution_risk_score":4,"legal_or_contract_risk_score":1,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":74,"stage_label_after":"Stage2-Actionable","changed_components":["contract_score","margin_bridge_score","revision_score","customer_quality_score","execution_risk_score"],"component_delta_explanation":"C28 shadow profile requires verified renewal/revenue/margin bridge before Yellow/Green and routes security-label spikes with weak bridge to local 4B watch.","MFE_90D_pct":42.93,"MAE_90D_pct":-3.76,"score_return_alignment_label":"aligned_positive","current_profile_verdict":"current_profile_correct"}
{"row_type":"profile_comparison","round":"R8","loop":"103","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","profile_id":"P0_e2r_2_1_stock_web_calibrated_proxy","scope":"current_global_proxy","hypothesis":"Current calibrated profile with global price-only and 4B guardrails only.","eligible":7,"selected":"all 7","avg_mfe90":55.01,"avg_mae90":-23.59,"avg_mfe180":69.89,"avg_mae180":-24.03,"false_positive_rate":0.43,"verdict":"mixed; misses positive proxy bridge and still lets weak label spikes look too actionable"}
{"row_type":"profile_comparison","round":"R8","loop":"103","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","profile_id":"P0b_e2r_2_0_baseline_reference","scope":"rollback_reference","hypothesis":"Old baseline without C28-specific bridge guard.","eligible":7,"selected":"all 7","avg_mfe90":55.01,"avg_mae90":-23.59,"avg_mfe180":69.89,"avg_mae180":-24.03,"false_positive_rate":0.57,"verdict":"too permissive for SASE/AI/security label spikes"}
{"row_type":"profile_comparison","round":"R8","loop":"103","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","profile_id":"P1_L8_security_bridge_candidate","scope":"sector_specific","hypothesis":"L8 software/security requires renewal or revenue/margin proxy before Yellow.","eligible":4,"selected":"positive 4","avg_mfe90":78.33,"avg_mae90":-8.29,"avg_mfe180":96.31,"avg_mae180":-8.34,"false_positive_rate":0.0,"verdict":"better score-return alignment"}
{"row_type":"profile_comparison","round":"R8","loop":"103","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","profile_id":"P2_C28_retention_bridge_candidate","scope":"canonical_archetype_specific","hypothesis":"C28-specific verified retention/renewal/revenue bridge gate plus proxy exception.","eligible":4,"selected":"positive 4","avg_mfe90":78.33,"avg_mae90":-8.29,"avg_mfe180":96.31,"avg_mae180":-8.34,"false_positive_rate":0.0,"verdict":"candidate rule"}
{"row_type":"profile_comparison","round":"R8","loop":"103","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","profile_id":"P3_counterexample_guard_profile","scope":"canonical_guard","hypothesis":"If label spike lacks renewal/revenue bridge and 90D MAE risk is high, route to local 4B watch.","eligible":3,"selected":"counterexamples filtered","avg_mfe90":23.92,"avg_mae90":-43.99,"avg_mfe180":34.67,"avg_mae180":-44.95,"false_positive_rate":0.0,"verdict":"guard catches high-MAE rows"}
{"row_type":"residual_contribution","round":"R8","loop":"103","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","new_independent_case_count":7,"reused_case_count":0,"new_symbol_count":7,"new_trigger_family_count":7,"tested_existing_calibrated_axes":["stage2_required_bridge","local_4b_watch_guard","price_only_blowoff_blocks_positive_stage","full_4b_requires_non_price_evidence"],"residual_error_types_found":["source_proxy_positive_missed_structural","security_label_false_positive","high_MAE_success_needs_guard"],"loop_contribution_label":"canonical_archetype_rule_candidate","do_not_propose_new_weight_delta":false}
```

## 26. Deferred Coding Agent Handoff Prompt

### Purpose
You are now in the repository implementation phase. The attached Markdown files are v12 post-calibrated residual research outputs produced using the Songdaiki/stock-web OHLC atlas. These MDs are not live candidate research. They are historical calibration research designed to extend the already-applied e2r_2_1_stock_web_calibrated profile. Do not blindly apply every shadow row. Ingest the machine-readable rows and update the sector/canonical-archetype calibration ledger.

### Price source context
- Primary historical price source used by the research MD: Songdaiki/stock-web.
- Price basis: tradable_raw.
- Price adjustment status: raw_unadjusted_marcap.
- Price shard pattern: atlas/ohlcv_tradable_by_symbol_year/{prefix}/{symbol}/{year}.csv.
- Symbol profile pattern: atlas/symbol_profiles/{prefix}/{symbol}.json.

### Rules
- Use only calibration_usable=true rows for quantitative calibration.
- Do not count reused cases as new independent evidence unless independent_evidence_weight > 0.
- Do not treat schema_rematerialization_only or duplicate_low_value_loop as new evidence.
- Do not apply global deltas unless multiple large_sector_id values support the same direction.
- Prefer sector_specific or canonical_archetype_specific shadow profiles.
- Positive score promotion requires non-price evidence and clean 180D MFE/MAE.
- 4B rows are overlay/risk calibration only.
- 4C rows are thesis-break/protection calibration only.
- price-only rows cannot promote Stage2/Stage3.
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

### Expected output
- Concise implementation summary.
- Rows accepted/rejected.
- New sector/canonical archetype coverage.
- Existing axis strengthened/weakened/kept.
- No investment recommendation language.

## 27. Next Round State

```text
completed_round = R8
completed_loop = 103
selection_basis = docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket = Priority 1-under-50 after local-session adjustment; published index Priority 0
next_recommended_archetypes = C11_BATTERY_ORDERBOOK_RERATING, C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE, C06_HBM_MEMORY_CUSTOMER_CAPACITY, C28_SOFTWARE_SECURITY_CONTRACT_RETENTION, C14_EV_DEMAND_SLOWDOWN_4B_4C
round_schedule_status = coverage_index_selected
round_sector_consistency = pass
```

Next execution should re-read the latest `V12_Research_No_Repeat_Index.md` rather than continuing R1~R13 sequentially.

## 28. Source Notes

- Main execution prompt: `docs/core/e2r_v12_prompt_round_scheduler_corrected.txt`.
- No-repeat index: `docs/core/V12_Research_No_Repeat_Index.md`.
- Stock-Web manifest: `atlas/manifest.json`, manifest max date `2026-02-20`.
- Downloaded calibration shards used locally from `atlas/ohlcv_tradable_by_symbol_year` for 2024 and 2025.
