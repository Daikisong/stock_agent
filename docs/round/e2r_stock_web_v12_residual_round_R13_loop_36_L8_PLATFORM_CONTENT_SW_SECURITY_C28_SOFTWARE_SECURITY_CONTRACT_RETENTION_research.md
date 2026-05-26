# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

|field|value|
|---|---|
|mode|historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12|
|research_session|post_calibrated_sector_archetype_residual_research|
|round|R13|
|loop|36|
|large_sector_id|L8_PLATFORM_CONTENT_SW_SECURITY|
|canonical_archetype_id|C28_SOFTWARE_SECURITY_CONTRACT_RETENTION|
|fine_archetype_id|B2B_PUBLIC_SECURITY_SOFTWARE_RECURRING_RETENTION|
|loop_objective|holdout_validation; residual_missed_structural_mining; yellow_threshold_stress_test; green_strictness_stress_test; stage2_actionable_bonus_stress_test; 4B_non_price_requirement_stress_test; 4C_thesis_break_timing_test; sector_specific_rule_discovery; canonical_archetype_compression; counterexample_mining; coverage_gap_fill|
|production_scoring_changed|false|
|shadow_weight_only|true|
|handoff_prompt_executed_now|false|


## 1. Current Calibrated Profile Assumption

|axis|value|status in this MD|
|---|---|---|
|current_default_profile_proxy|e2r_2_1_stock_web_calibrated_proxy|stress-tested only|
|previous_baseline_reference|e2r_2_0_baseline_reference|rollback/reference only|
|stage2_actionable_evidence_bonus|+2.0|kept; C28-specific add-on tested as shadow only|
|stage3_yellow_total_min|75.0|kept; Yellow gate stress-tested|
|stage3_green_total_min|87.0|kept; Green lateness audited|
|stage3_green_revision_min|55.0|kept; not globally weakened|
|price_only_blowoff_blocks_positive_stage|true|strengthened inside C28 counterexample guard|
|full_4b_requires_non_price_evidence|true|strengthened; price-only 4B is overlay only|
|hard_4c_thesis_break_routes_to_4c|true|kept; 4C rows are protection logic only|


## 2. Round / Large Sector / Canonical Archetype Scope

This loop targets L8 software/security names where the central question is whether repeatable B2B/public contracts, maintenance, renewals, or SaaS retention deserve an earlier Stage2/Yellow upgrade than global Green revision confirmation. It also tests the shadow guard that a security/software ticker with price-only or political/event momentum must not be promoted as C28 positive evidence.


## 3. Previous Coverage / Duplicate Avoidance Check

Allowed `stock_agent` research artifacts were used only for duplicate/coverage context. The ingest summary shows 107 parsed result MDs, 4,951 raw trigger rows, 1,940 validated trigger rows, 1,376 aggregate representative rows, and prior coverage across R1-R13 / loops 1-9. The applied scoring diff confirms that the current global axes already include Stage2 +2, stricter Green, price-only blowoff blocking, non-price 4B, and hard 4C routing. This loop therefore does not re-propose those globally; it proposes C28-scoped shadow rules only.


## 4. Stock-Web OHLC Input / Price Source Validation

Stock-Web manifest/schema were checked first. The manifest max date is 2026-02-20; all trigger windows below are before that date and have at least 180 tradable rows available. Price basis is `tradable_raw`; adjustment status is `raw_unadjusted_marcap`; raw corporate-action contamination is blocked at 180D.


|field|value|
|---|---|
|source|Songdaiki/stock-web|
|upstream_source|FinanceData/marcap|
|manifest|atlas/manifest.json|
|schema|atlas/schema.json|
|universe|atlas/universe/all_symbols.csv|
|manifest_max_date|2026-02-20|
|tradable_row_count|14354401|
|raw_row_count|15214118|
|symbol_count|5414|
|markets|KONEX / KOSDAQ / KOSDAQ GLOBAL / KOSPI|
|price_basis|tradable_raw|
|price_adjustment_status|raw_unadjusted_marcap|
|calibration_shard_root|atlas/ohlcv_tradable_by_symbol_year|
|raw_shard_root|atlas/ohlcv_raw_by_symbol_year|


## 5. Historical Eligibility Gate

|case_id|symbol|entry_date|forward_180D_available|corporate_action_window_status|calibration_usable|reason|
|---|---|---|---|---|---|---|
|C28_DOUZONE_2020_CLOUD_ERP_RETENTION|012510|2020-04-29|true|clean_180D_window|true|profile corporate-action candidates do not overlap entry~D+180|
|C28_WINS_2020_SECURITY_APPLIANCE_SERVICE_RETENTION|136540|2020-04-16|true|clean_180D_window|true|profile corporate-action candidates do not overlap entry~D+180|
|C28_GENIANS_2023_ZERO_TRUST_SECURITY_RETENTION|263860|2023-05-17|true|clean_180D_window|true|profile corporate-action candidates do not overlap entry~D+180|
|C28_AHNLAB_2022_PRICE_THEME_FALSE_POSITIVE|053800|2022-03-18|true|clean_180D_window|true|profile corporate-action candidates do not overlap entry~D+180|


## 6. Canonical Archetype Compression Map

|fine_archetype_id|canonical_archetype_id|compression rationale|
|---|---|---|
|CLOUD_ERP_WEHAGO_RECURRING_RETENTION|C28_SOFTWARE_SECURITY_CONTRACT_RETENTION|ERP/cloud subscription retention is C28, not C26 ad leverage.|
|NETWORK_SECURITY_PUBLIC_ENTERPRISE_RETENTION|C28_SOFTWARE_SECURITY_CONTRACT_RETENTION|Security appliance + maintenance/public enterprise route maps to contract-retention software/security.|
|ZERO_TRUST_NAC_EDR_RECURRING_SECURITY|C28_SOFTWARE_SECURITY_CONTRACT_RETENTION|Zero-trust/NAC/EDR policy-driven security software renewal route maps to C28.|
|SECURITY_SOFTWARE_PRICE_ONLY_POLITICAL_BLOWOFF_GUARD|C28_SOFTWARE_SECURITY_CONTRACT_RETENTION|Same ticker sector, but evidence family is a C28 counterexample guard, not positive promotion.|


## 7. Case Selection Summary

|case_id|symbol|company|role|best_trigger|current_profile_verdict|new?|
|---|---|---|---|---|---|---|
|C28_DOUZONE_2020_CLOUD_ERP_RETENTION|012510|더존비즈온|structural_success|C28_DOUZONE_2020_STAGE2A_2020-04-29|current_profile_too_late|true|
|C28_WINS_2020_SECURITY_APPLIANCE_SERVICE_RETENTION|136540|윈스|structural_success|C28_WINS_2020_STAGE2A_2020-04-16|current_profile_too_late|true|
|C28_GENIANS_2023_ZERO_TRUST_SECURITY_RETENTION|263860|지니언스|missed_structural|C28_GENIANS_2023_STAGE2A_2023-05-17|current_profile_too_late|true|
|C28_AHNLAB_2022_PRICE_THEME_FALSE_POSITIVE|053800|안랩|false_positive_green|C28_AHNLAB_2022_PRICE_ONLY_2022-03-18|current_profile_correct|true|


## 8. Positive vs Counterexample Balance

|positive_structural_success|missed_structural|counterexample_or_failed_rerating|4B_or_4C_case|calibration_usable_case_count|
|---|---|---|---|---|
|2|1|1|1|4|


## 9. Evidence Source Map

|case_id|Stage2 evidence|Stage3 evidence|4B/4C evidence|evidence caveat|
|---|---|---|---|---|
|C28_DOUZONE_2020_CLOUD_ERP_RETENTION|cloud ERP / WEHAGO / enterprise software retention route|later revision/valuation confirmation|none used for positive exit|Historical evidence summarized as proxy; attach original article/filing before production.|
|C28_WINS_2020_SECURITY_APPLIANCE_SERVICE_RETENTION|network security public/enterprise demand + maintenance retention|later financial/relative strength confirmation|none used for positive exit|Historical evidence summarized as proxy; attach original article/filing before production.|
|C28_GENIANS_2023_ZERO_TRUST_SECURITY_RETENTION|zero-trust/NAC/EDR policy + recurring security customer route|later momentum/revision confirmation|late Green almost at peak|Historical evidence summarized as proxy; attach original article/filing before production.|
|C28_AHNLAB_2022_PRICE_THEME_FALSE_POSITIVE|relative strength only; no contract-retention promotion|none|price-only blowoff / 4B overlay / thesis-watch|Counterexample intentionally blocks price-only promotion.|


## 10. Price Data Source Map

|symbol|profile_path|price_shard_path(s)|profile window status|
|---|---|---|---|
|012510|atlas/symbol_profiles/012/012510.json|atlas/ohlcv_tradable_by_symbol_year/012/012510/2020.csv|clean 2020+ window; corporate-action candidate dates are 2002-04-22, 2006-06-28, 2009-12-09 only.|
|136540|atlas/symbol_profiles/136/136540.json|atlas/ohlcv_tradable_by_symbol_year/136/136540/2020.csv|clean window; corporate_action_candidate_count=0.|
|263860|atlas/symbol_profiles/263/263860.json|atlas/ohlcv_tradable_by_symbol_year/263/263860/2023.csv|clean 2023 window; corporate-action candidates are 2018 only.|
|053800|atlas/symbol_profiles/053/053800.json|atlas/ohlcv_tradable_by_symbol_year/053/053800/2022.csv|clean 2022 window; only corporate-action candidate is 2005-03-31.|


## 11. Case-by-Case Trigger Grid

|trigger_id|case_id|trigger_type|entry_date|entry_price|MFE90|MAE90|peak|current_profile_verdict|aggregate_role|
|---|---|---|---|---|---|---|---|---|---|
|C28_DOUZONE_2020_STAGE2A_2020-04-29|C28_DOUZONE_2020_CLOUD_ERP_RETENTION|Stage2-Actionable|2020-04-29|87900|54.72|-3.19|2020-09-08 / 136000|current_profile_too_late|representative|
|C28_DOUZONE_2020_GREEN_2020-09-04|C28_DOUZONE_2020_CLOUD_ERP_RETENTION|Stage3-Green|2020-09-04|126500|7.51|-19.76|2020-09-08 / 136000|current_profile_too_late|label_comparison_only|
|C28_WINS_2020_STAGE2A_2020-04-16|C28_WINS_2020_SECURITY_APPLIANCE_SERVICE_RETENTION|Stage2-Actionable|2020-04-16|14700|26.87|-8.84|2020-09-11 / 23700|current_profile_too_late|representative|
|C28_WINS_2020_GREEN_2020-09-11|C28_WINS_2020_SECURITY_APPLIANCE_SERVICE_RETENTION|Stage3-Green|2020-09-11|22550|5.1|-22.62|2020-09-11 / 23700|current_profile_too_late|label_comparison_only|
|C28_GENIANS_2023_STAGE2A_2023-05-17|C28_GENIANS_2023_ZERO_TRUST_SECURITY_RETENTION|Stage2-Actionable|2023-05-17|11770|49.87|-6.2|2023-06-13 / 17640|current_profile_too_late|representative|
|C28_GENIANS_2023_GREEN_2023-06-09|C28_GENIANS_2023_ZERO_TRUST_SECURITY_RETENTION|Stage3-Green|2023-06-09|17490|0.86|-36.88|2023-06-13 / 17640|current_profile_too_late|label_comparison_only|
|C28_AHNLAB_2022_PRICE_ONLY_2022-03-18|C28_AHNLAB_2022_PRICE_THEME_FALSE_POSITIVE|Price-only Stage2-blocked|2022-03-18|101700|114.85|-20.35|2022-03-24 / 218500|current_profile_correct|representative|
|C28_AHNLAB_2022_4B_OVERLAY_2022-03-23|C28_AHNLAB_2022_PRICE_THEME_FALSE_POSITIVE|Stage4B-overlay|2022-03-23|175800|24.29|-53.92|2022-03-24 / 218500|current_profile_correct|4B_overlay_only|


## 12. Trigger-Level OHLC Backtest Tables

|trigger_id|entry|MFE30|MFE90|MFE180|MAE30|MAE90|MAE180|below_entry_30D|below_entry_90D|drawdown_after_peak|
|---|---|---|---|---|---|---|---|---|---|---|
|C28_DOUZONE_2020_STAGE2A_2020-04-29|2020-04-29 @ 87900|40.5|54.72|54.72|-3.19|-3.19|-3.19|False|False|-25.37|
|C28_DOUZONE_2020_GREEN_2020-09-04|2020-09-04 @ 126500|7.51|7.51|7.51|-19.76|-19.76|-19.76|True|True|-25.37|
|C28_WINS_2020_STAGE2A_2020-04-16|2020-04-16 @ 14700|25.17|26.87|61.22|-8.84|-8.84|-8.84|True|True|-26.37|
|C28_WINS_2020_GREEN_2020-09-11|2020-09-11 @ 22550|5.1|5.1|5.1|-22.62|-22.62|-22.62|True|True|-26.37|
|C28_GENIANS_2023_STAGE2A_2023-05-17|2023-05-17 @ 11770|49.87|49.87|49.87|-4.59|-6.2|-6.2|False|True|-37.41|
|C28_GENIANS_2023_GREEN_2023-06-09|2023-06-09 @ 17490|0.86|0.86|0.86|-36.88|-36.88|-36.88|True|True|-37.41|
|C28_AHNLAB_2022_PRICE_ONLY_2022-03-18|2022-03-18 @ 101700|114.85|114.85|114.85|-6.29|-20.35|-42.08|True|True|-73.04|
|C28_AHNLAB_2022_4B_OVERLAY_2022-03-23|2022-03-23 @ 175800|24.29|24.29|24.29|-46.53|-53.92|-66.5|True|True|-73.04|


## 13. Current Calibrated Profile Stress Test

|case_id|current profile likely action|actual price alignment|verdict|
|---|---|---|---|
|C28_DOUZONE_2020_CLOUD_ERP_RETENTION|Waits for stronger Green/revision; Stage2 bonus helps but C28 contract quality is not separately rewarded.|Stage2 MFE90 +54.72 with only -3.19 MAE; Green MFE90 +7.51 and large downside.|current_profile_too_late|
|C28_WINS_2020_SECURITY_APPLIANCE_SERVICE_RETENTION|Recognizes as Yellow/Stage2, but Green confirmation is late.|Stage2 MFE180 +61.22; Green starts near peak.|current_profile_too_late|
|C28_GENIANS_2023_ZERO_TRUST_SECURITY_RETENTION|May stay Stage2 because revision/margin evidence lags.|Stage2 MFE90 +49.87; Green at +0.86 MFE and -36.88 MAE.|current_profile_too_late|
|C28_AHNLAB_2022_PRICE_THEME_FALSE_POSITIVE|Price-only blowoff guard blocks positive promotion; 4B requires non-price evidence.|Correctly avoids treating +114.85 MFE price spike as C28 evidence because later MAE180 is -42.08 from Stage2 entry and -66.50 from 4B overlay.|current_profile_correct|


## 14. Stage2 / Yellow / Green Comparison

|case|Stage2 entry|Green entry|peak_after_Stage2|green_lateness_ratio|verdict|
|---|---|---|---|---|---|
|더존비즈온|87900|126500|136000|0.802|Green missed most upside|
|윈스|14700|22550|23700|0.872|Green near peak|
|지니언스|11770|17490|17640|0.974|Green effectively peak signal|
|안랩|101700|n/a|218500|n/a|No C28 Green; price-only blocked|


## 15. 4B Local vs Full-window Timing Audit

|trigger_id|4B evidence type|local_peak_proximity|full_window_peak_proximity|timing verdict|do_not_treat_as_full_4B|
|---|---|---|---|---|---|
|C28_AHNLAB_2022_4B_OVERLAY_2022-03-23|price_only / valuation_blowoff / positioning_overheat|0.635|0.635|price_only_local_4B_not_full_without_non_price_evidence|true|
|C28_GENIANS_2023_GREEN_2023-06-09|late Green near peak; no explicit non-price 4B|n/a|n/a|treat as late Green, not full 4B|true|


## 16. 4C Protection Audit

AhnLab is the only explicit 4C/protection audit row. The 2022-03-23 4B overlay entry suffered -66.50% MAE over the observed 180D window, while a thesis-watch around 2022-09-16 / 2022-09-26 would have been late but still protection-oriented rather than positive calibration. The label is `hard_4c_late` / `thesis_break_watch_only`.


## 17. Sector-Specific Rule Candidate

`l8_recurring_software_security_stage2_bonus`: In L8, if the non-price evidence is repeatable software/security contract retention—enterprise SaaS renewals, public/enterprise security maintenance, NAC/EDR/zero-trust policy adoption—add a small Stage2/Yellow shadow bonus. This does not relax Green thresholds. It is a way to hear the recurring-revenue engine before the dashboard light turns fully green.


## 18. Canonical-Archetype Rule Candidate

`c28_repeatable_contract_retention_gate`: For C28, Stage2/Yellow can be promoted when contract/renewal/customer-quality evidence is present and the 180D window is clean. `c28_price_only_theme_cap`: if relative strength comes from price-only/political/security-stock momentum without repeatable contract evidence, cap positive stages and route the row to 4B/4C watch only.


## 19. Before / After Backtest Comparison

|profile_id|profile_scope|profile_hypothesis|changed_axes|changed_thresholds|eligible_trigger_count|selected_entry_trigger_per_case|avg_MFE_90D_pct|avg_MAE_90D_pct|avg_MFE_180D_pct|avg_MAE_180D_pct|false_positive_rate|missed_structural_count|late_green_count|avg_green_lateness_ratio|avg_four_b_local_peak_proximity|avg_four_b_full_window_peak_proximity|score_return_alignment_verdict|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|P0_e2r_2_1_stock_web_calibrated_proxy|global calibrated proxy|Keep current global thresholds; Stage2 bonus exists but C28 has no special recurring-contract gate.|none|none|4|late Green for 3 positives; AhnLab blocked|4.49|-26.09|4.49|-26.09|0.0|3|3|0.883|0.635|0.635|guards work, but C28 positives are often too late|
|P0b_e2r_2_0_baseline_reference|rollback reference|Earlier profile without calibrated guardrails; price-only and late Green risk both larger.|rollback reference only|old Stage thresholds|4|inconsistent; AhnLab at risk of false positive|61.58|-9.65|61.58|-20.65|0.25|2|2|0.883|0.635|0.635|higher MFE partly from false-positive inclusion; not safer|
|P1_L8_sector_specific_candidate_profile|sector_specific|For L8 software/security, reward repeatable contract-retention route but keep price-only guard.|l8_recurring_contract_retention_bonus +2; price_only cap kept|no global threshold change|4|Stage2 for 3 positives; AhnLab blocked|43.82|-6.08|55.27|-6.08|0.0|0|0|0.0|0.635|0.635|best balance in this loop|
|P2_C28_canonical_archetype_candidate_profile|canonical_archetype_specific|C28-specific gate: repeat/reten­tion/customer renewal evidence can upgrade Stage2/Yellow; single-title/political/theme price spikes cannot.|c28_repeatable_ip_retention_gate +3; c28_single_event_cap -6|Green thresholds unchanged; Yellow can be reached through C28 gate|4|Stage2 for repeat positives; AhnLab blocked|43.82|-6.08|55.27|-6.08|0.0|0|0|0.0|0.635|0.635|candidate rule supported by 3 positive + 1 counterexample|
|P3_counterexample_guard_profile|canonical_archetype_specific guard|Explicitly demote price-only/political/security-stock momentum without contract evidence.|c28_price_only_or_political_blowoff_cap -8; 4B risk overlay only|no positive threshold relaxation|1|AhnLab blocked / 4B watch only|None|None|None|None|0.0|0|0|None|0.635|0.635|strengthens existing price-only and non-price 4B guardrails|


## 20. Score-Return Alignment Matrix

|trigger_id|weighted_before|stage_before|weighted_after|stage_after|MFE90|MAE90|alignment|
|---|---|---|---|---|---|---|---|
|C28_DOUZONE_2020_STAGE2A_2020-04-29|82|Stage3-Yellow|86|Stage2-Actionable-High / Yellow retained|54.72|-3.19|early_stage2_aligned_green_late|
|C28_WINS_2020_STAGE2A_2020-04-16|76|Stage3-Yellow / Stage2-Actionable boundary|81|Stage2-Actionable-High|26.87|-8.84|stage2_positive_with_acceptable_mae|
|C28_GENIANS_2023_STAGE2A_2023-05-17|72|Stage2-Actionable|79|Stage3-Yellow / small-cap security retention watch|49.87|-6.2|missed_structural_stage2_should_be_yellow|
|C28_AHNLAB_2022_PRICE_ONLY_2022-03-18|81|would-be Stage3-Yellow if RS/valuation were over-weighted|59|Blocked / 4B watch only|114.85|-20.35|price_moved_without_evidence_blocked|


## 21. Coverage Matrix

|large_sector_id|canonical_archetype_id|fine_archetype_id|positive_case_count|counterexample_count|4B_case_count|4C_case_count|new_independent_case_count|reused_case_count|calibration_usable_trigger_count|representative_trigger_count|current_profile_error_count|sector_rule_candidate|canonical_rule_candidate|coverage_gap_after_this_loop|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|L8_PLATFORM_CONTENT_SW_SECURITY|C28_SOFTWARE_SECURITY_CONTRACT_RETENTION|B2B_PUBLIC_SECURITY_SOFTWARE_RECURRING_RETENTION|3|1|1|1|4|0|8|4|3|True|True|C28 now has 3 recurring-contract positives and 1 price-only false-positive guard; still needs more pure SaaS/security holdouts.|


## 22. Residual Contribution Summary

|field|value|
|---|---|
|new_independent_case_count|4|
|reused_case_count|0|
|reused_case_ids|[]|
|new_symbol_count|4|
|new_canonical_archetype_count|1|
|new_fine_archetype_count|4|
|new_trigger_family_count|4|
|tested_existing_calibrated_axes|stage2_actionable_evidence_bonus, stage3_yellow_total_min, stage3_green_total_min, stage3_green_revision_min, price_only_blowoff_blocks_positive_stage, full_4b_requires_non_price_evidence, hard_4c_thesis_break_routes_to_4c|
|residual_error_types_found|current_profile_too_late_for_recurring_contract_software, late_green_near_peak, price_only_security_ticker_false_positive_risk|
|new_axis_proposed|c28_repeatable_contract_retention_gate / c28_price_only_theme_cap / l8_recurring_software_security_stage2_bonus|
|existing_axis_strengthened|price_only_blowoff_blocks_positive_stage / full_4b_requires_non_price_evidence / hard_4c_thesis_break_routes_to_4c|
|existing_axis_weakened|null|
|existing_axis_kept|stage2_actionable_evidence_bonus / Yellow 75 / Green 87 / Green revision 55|
|sector_specific_rule_candidate|true|
|canonical_archetype_rule_candidate|true|
|no_new_signal_reason|null|
|loop_contribution_label|canonical_archetype_rule_candidate|


## 23. Validation Scope / Non-Validation Scope

|scope|included?|note|
|---|---|---|
|actual stock-web 1D OHLC|yes|entry/peak/MFE/MAE use stock-web tradable shards|
|production scoring change|no|shadow-only|
|stock_agent code read/patch|no|not opened; no implementation|
|live candidate scan|no|all historical triggers only|
|brokerage/API/autotrading|no|out of scope|
|evidence source reattachment|partial|qualitative proxy only; original filing/news evidence should be reattached before promotion|


## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,c28_repeatable_contract_retention_gate,canonical_archetype_specific,L8_PLATFORM_CONTENT_SW_SECURITY,C28_SOFTWARE_SECURITY_CONTRACT_RETENTION,0,3,+3,Recurring B2B/public security or enterprise software contracts captured upside before strict Green.,P2 raises early non-price positives: avg 90D MFE 43.82 / avg 90D MAE -6.08.,C28_DOUZONE_2020_STAGE2A_2020-04-29|C28_WINS_2020_STAGE2A_2020-04-16|C28_GENIANS_2023_STAGE2A_2023-05-17,3,3,1,medium,archetype_shadow_only,not production; post-calibrated residual
shadow_weight,c28_price_only_theme_cap,canonical_archetype_specific,L8_PLATFORM_CONTENT_SW_SECURITY,C28_SOFTWARE_SECURITY_CONTRACT_RETENTION,0,-8,-8,Security/software ticker identity alone is insufficient when the trigger family is price-only or political/event-driven.,Blocks AhnLab false positive; keeps full_4B_requires_non_price_evidence intact.,C28_AHNLAB_2022_PRICE_ONLY_2022-03-18|C28_AHNLAB_2022_4B_OVERLAY_2022-03-23,2,1,1,medium,guard_shadow_only,not production; price-only cannot promote Stage2/3
shadow_weight,l8_recurring_software_security_stage2_bonus,sector_specific,L8_PLATFORM_CONTENT_SW_SECURITY,C28_SOFTWARE_SECURITY_CONTRACT_RETENTION,0,2,+2,L8 recurring contract quality deserves sector-level Stage2 support when non-price evidence is present.,Improves early selection for Douzone/Wins/Genians without AhnLab false positive.,C28_DOUZONE_2020_STAGE2A_2020-04-29|C28_WINS_2020_STAGE2A_2020-04-16|C28_GENIANS_2023_STAGE2A_2023-05-17,3,3,1,low_to_medium,sector_shadow_only,needs more C26/C28/C32 cross-validation before production
```


## 25. Machine-Readable Rows

### 25.1 price_source_validation
```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration"}
```

### 25.2 case rows
```jsonl
{"row_type": "case", "case_id": "C28_DOUZONE_2020_CLOUD_ERP_RETENTION", "symbol": "012510", "company_name": "더존비즈온", "round": "R13", "loop": "36", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C28_SOFTWARE_SECURITY_CONTRACT_RETENTION", "fine_archetype_id": "CLOUD_ERP_WEHAGO_RECURRING_RETENTION", "case_type": "structural_success", "positive_or_counterexample": "positive", "best_trigger": "C28_DOUZONE_2020_STAGE2A_2020-04-29", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "Stage2 evidence captured most upside; Green confirmation arrived near the later repricing band.", "current_profile_verdict": "current_profile_too_late", "price_source": "Songdaiki/stock-web", "notes": "Cloud ERP / WEHAGO and remote-work digitization were treated as recurring enterprise software evidence, not as a one-day theme."}
{"row_type": "case", "case_id": "C28_WINS_2020_SECURITY_APPLIANCE_SERVICE_RETENTION", "symbol": "136540", "company_name": "윈스", "round": "R13", "loop": "36", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C28_SOFTWARE_SECURITY_CONTRACT_RETENTION", "fine_archetype_id": "NETWORK_SECURITY_PUBLIC_ENTERPRISE_RETENTION", "case_type": "structural_success", "positive_or_counterexample": "positive", "best_trigger": "C28_WINS_2020_STAGE2A_2020-04-16", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "Stage2 captured clean 180D upside; strict Green arrived close to the observed cycle peak.", "current_profile_verdict": "current_profile_too_late", "price_source": "Songdaiki/stock-web", "notes": "Security appliance/service evidence was interpreted as repeatable customer/maintenance route; not a pure security news spike."}
{"row_type": "case", "case_id": "C28_GENIANS_2023_ZERO_TRUST_SECURITY_RETENTION", "symbol": "263860", "company_name": "지니언스", "round": "R13", "loop": "36", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C28_SOFTWARE_SECURITY_CONTRACT_RETENTION", "fine_archetype_id": "ZERO_TRUST_NAC_EDR_RECURRING_SECURITY", "case_type": "missed_structural", "positive_or_counterexample": "positive", "best_trigger": "C28_GENIANS_2023_STAGE2A_2023-05-17", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "Stage2 recurring-security evidence preceded a sharp move; Green confirmation was almost at the peak.", "current_profile_verdict": "current_profile_too_late", "price_source": "Songdaiki/stock-web", "notes": "The case is useful as a residual missed-structural example for small-cap security software where revision confirmation lags contract narrative."}
{"row_type": "case", "case_id": "C28_AHNLAB_2022_PRICE_THEME_FALSE_POSITIVE", "symbol": "053800", "company_name": "안랩", "round": "R13", "loop": "36", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C28_SOFTWARE_SECURITY_CONTRACT_RETENTION", "fine_archetype_id": "SECURITY_SOFTWARE_PRICE_ONLY_POLITICAL_BLOWOFF_GUARD", "case_type": "false_positive_green", "positive_or_counterexample": "counterexample", "best_trigger": "C28_AHNLAB_2022_PRICE_ONLY_2022-03-18", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "Price moved violently, but non-price contract-retention evidence was not enough to promote C28 positive stage.", "current_profile_verdict": "current_profile_correct", "price_source": "Songdaiki/stock-web", "notes": "This row strengthens price-only blowoff blocking inside C28; the business is security software, but the trigger family was not contract-retention evidence."}
```

### 25.3 trigger rows
```jsonl
{"row_type": "trigger", "trigger_id": "C28_DOUZONE_2020_STAGE2A_2020-04-29", "case_id": "C28_DOUZONE_2020_CLOUD_ERP_RETENTION", "symbol": "012510", "company_name": "더존비즈온", "round": "R13", "loop": "36", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C28_SOFTWARE_SECURITY_CONTRACT_RETENTION", "fine_archetype_id": "CLOUD_ERP_WEHAGO_RECURRING_RETENTION", "sector": "플랫폼·콘텐츠·SW·보안", "primary_archetype": "cloud ERP / SaaS retention / enterprise software repricing", "loop_objective": "holdout_validation;residual_missed_structural_mining;yellow_threshold_stress_test;green_strictness_stress_test;stage2_actionable_bonus_stress_test;4B_non_price_requirement_stress_test;4C_thesis_break_timing_test;sector_specific_rule_discovery;canonical_archetype_compression;counterexample_mining;coverage_gap_fill", "trigger_type": "Stage2-Actionable", "trigger_date": "2020-04-29", "evidence_available_at_that_date": "remote-work digitization + cloud ERP/WEHAGO retention route; public enterprise software demand visible before full revision confirmation", "evidence_source": "historical public-event/disclosure proxy; stock-web price rows used for OHLC validation", "stage2_evidence_fields": ["public_event_or_disclosure", "customer_or_order_quality", "backlog_or_delivery_visibility", "early_revision_signal"], "stage3_evidence_fields": [], "stage4b_evidence_fields": [], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/012/012510/2020.csv", "profile_path": "atlas/symbol_profiles/012/012510.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2020-04-29", "entry_price": 87900, "MFE_30D_pct": 40.5, "MFE_90D_pct": 54.72, "MFE_180D_pct": 54.72, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -3.19, "MAE_90D_pct": -3.19, "MAE_180D_pct": -3.19, "MAE_1Y_pct": null, "below_entry_price_flag_30D": false, "below_entry_price_flag_90D": false, "peak_date": "2020-09-08", "peak_price": 136000, "drawdown_after_peak_pct": -25.37, "green_lateness_ratio": null, "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": null, "four_b_evidence_type": [], "four_c_protection_label": null, "trigger_outcome_label": "structural_success", "current_profile_verdict": "current_profile_too_late", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "C28_DOUZONE_2020_ENTRY_2020-04-29_87900", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "C28_DOUZONE_2020_GREEN_2020-09-04", "case_id": "C28_DOUZONE_2020_CLOUD_ERP_RETENTION", "symbol": "012510", "company_name": "더존비즈온", "round": "R13", "loop": "36", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C28_SOFTWARE_SECURITY_CONTRACT_RETENTION", "fine_archetype_id": "CLOUD_ERP_WEHAGO_RECURRING_RETENTION", "sector": "플랫폼·콘텐츠·SW·보안", "primary_archetype": "cloud ERP / SaaS retention / enterprise software repricing", "loop_objective": "green_strictness_stress_test", "trigger_type": "Stage3-Green", "trigger_date": "2020-09-04", "evidence_available_at_that_date": "later market-confirmed rerating / revision visibility after most Stage2 upside had appeared", "evidence_source": "historical public-event/disclosure proxy; stock-web price rows used for OHLC validation", "stage2_evidence_fields": [], "stage3_evidence_fields": ["confirmed_revision", "margin_bridge", "multiple_public_sources", "financial_visibility"], "stage4b_evidence_fields": [], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/012/012510/2020.csv", "profile_path": "atlas/symbol_profiles/012/012510.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2020-09-04", "entry_price": 126500, "MFE_30D_pct": 7.51, "MFE_90D_pct": 7.51, "MFE_180D_pct": 7.51, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -19.76, "MAE_90D_pct": -19.76, "MAE_180D_pct": -19.76, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2020-09-08", "peak_price": 136000, "drawdown_after_peak_pct": -25.37, "green_lateness_ratio": 0.802, "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": null, "four_b_evidence_type": [], "four_c_protection_label": null, "trigger_outcome_label": "late_green", "current_profile_verdict": "current_profile_too_late", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "C28_DOUZONE_2020_ENTRY_2020-09-04_126500", "dedupe_for_aggregate": false, "aggregate_group_role": "label_comparison_only", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "C28_WINS_2020_STAGE2A_2020-04-16", "case_id": "C28_WINS_2020_SECURITY_APPLIANCE_SERVICE_RETENTION", "symbol": "136540", "company_name": "윈스", "round": "R13", "loop": "36", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C28_SOFTWARE_SECURITY_CONTRACT_RETENTION", "fine_archetype_id": "NETWORK_SECURITY_PUBLIC_ENTERPRISE_RETENTION", "sector": "플랫폼·콘텐츠·SW·보안", "primary_archetype": "network security appliance + maintenance / public-enterprise retention", "loop_objective": "holdout_validation;residual_missed_structural_mining;yellow_threshold_stress_test;green_strictness_stress_test;stage2_actionable_bonus_stress_test;4B_non_price_requirement_stress_test;4C_thesis_break_timing_test;sector_specific_rule_discovery;canonical_archetype_compression;counterexample_mining;coverage_gap_fill", "trigger_type": "Stage2-Actionable", "trigger_date": "2020-04-16", "evidence_available_at_that_date": "network-security appliance/service demand with public/enterprise retention route; non-price evidence before late-cycle confirmation", "evidence_source": "historical public-event/disclosure proxy; stock-web price rows used for OHLC validation", "stage2_evidence_fields": ["public_event_or_disclosure", "customer_or_order_quality", "backlog_or_delivery_visibility", "early_revision_signal"], "stage3_evidence_fields": [], "stage4b_evidence_fields": [], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/136/136540/2020.csv", "profile_path": "atlas/symbol_profiles/136/136540.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2020-04-16", "entry_price": 14700, "MFE_30D_pct": 25.17, "MFE_90D_pct": 26.87, "MFE_180D_pct": 61.22, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -8.84, "MAE_90D_pct": -8.84, "MAE_180D_pct": -8.84, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2020-09-11", "peak_price": 23700, "drawdown_after_peak_pct": -26.37, "green_lateness_ratio": null, "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": null, "four_b_evidence_type": [], "four_c_protection_label": null, "trigger_outcome_label": "structural_success", "current_profile_verdict": "current_profile_too_late", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "C28_WINS_2020_ENTRY_2020-04-16_14700", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "C28_WINS_2020_GREEN_2020-09-11", "case_id": "C28_WINS_2020_SECURITY_APPLIANCE_SERVICE_RETENTION", "symbol": "136540", "company_name": "윈스", "round": "R13", "loop": "36", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C28_SOFTWARE_SECURITY_CONTRACT_RETENTION", "fine_archetype_id": "NETWORK_SECURITY_PUBLIC_ENTERPRISE_RETENTION", "sector": "플랫폼·콘텐츠·SW·보안", "primary_archetype": "network security appliance + maintenance / public-enterprise retention", "loop_objective": "green_strictness_stress_test", "trigger_type": "Stage3-Green", "trigger_date": "2020-09-11", "evidence_available_at_that_date": "late-cycle confirmed rerating after repeat security-demand route was already tradable", "evidence_source": "historical public-event/disclosure proxy; stock-web price rows used for OHLC validation", "stage2_evidence_fields": [], "stage3_evidence_fields": ["confirmed_revision", "margin_bridge", "financial_visibility", "low_red_team_risk"], "stage4b_evidence_fields": [], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/136/136540/2020.csv", "profile_path": "atlas/symbol_profiles/136/136540.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2020-09-11", "entry_price": 22550, "MFE_30D_pct": 5.1, "MFE_90D_pct": 5.1, "MFE_180D_pct": 5.1, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -22.62, "MAE_90D_pct": -22.62, "MAE_180D_pct": -22.62, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2020-09-11", "peak_price": 23700, "drawdown_after_peak_pct": -26.37, "green_lateness_ratio": 0.872, "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": null, "four_b_evidence_type": [], "four_c_protection_label": null, "trigger_outcome_label": "late_green_near_peak", "current_profile_verdict": "current_profile_too_late", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "C28_WINS_2020_ENTRY_2020-09-11_22550", "dedupe_for_aggregate": false, "aggregate_group_role": "label_comparison_only", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "C28_GENIANS_2023_STAGE2A_2023-05-17", "case_id": "C28_GENIANS_2023_ZERO_TRUST_SECURITY_RETENTION", "symbol": "263860", "company_name": "지니언스", "round": "R13", "loop": "36", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C28_SOFTWARE_SECURITY_CONTRACT_RETENTION", "fine_archetype_id": "ZERO_TRUST_NAC_EDR_RECURRING_SECURITY", "sector": "플랫폼·콘텐츠·SW·보안", "primary_archetype": "zero-trust / NAC / EDR security software recurring contracts", "loop_objective": "holdout_validation;residual_missed_structural_mining;yellow_threshold_stress_test;green_strictness_stress_test;stage2_actionable_bonus_stress_test;4B_non_price_requirement_stress_test;4C_thesis_break_timing_test;sector_specific_rule_discovery;canonical_archetype_compression;counterexample_mining;coverage_gap_fill", "trigger_type": "Stage2-Actionable", "trigger_date": "2023-05-17", "evidence_available_at_that_date": "zero-trust/NAC/EDR recurring-security narrative with small-cap revision lag; contract-retention evidence became tradable before Green confirmation", "evidence_source": "historical public-event/disclosure proxy; stock-web price rows used for OHLC validation", "stage2_evidence_fields": ["public_event_or_disclosure", "customer_or_order_quality", "capacity_or_volume_route", "policy_or_regulatory_optionality", "early_revision_signal"], "stage3_evidence_fields": [], "stage4b_evidence_fields": [], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/263/263860/2023.csv", "profile_path": "atlas/symbol_profiles/263/263860.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2023-05-17", "entry_price": 11770, "MFE_30D_pct": 49.87, "MFE_90D_pct": 49.87, "MFE_180D_pct": 49.87, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -4.59, "MAE_90D_pct": -6.2, "MAE_180D_pct": -6.2, "MAE_1Y_pct": null, "below_entry_price_flag_30D": false, "below_entry_price_flag_90D": true, "peak_date": "2023-06-13", "peak_price": 17640, "drawdown_after_peak_pct": -37.41, "green_lateness_ratio": null, "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": null, "four_b_evidence_type": [], "four_c_protection_label": null, "trigger_outcome_label": "missed_structural_success", "current_profile_verdict": "current_profile_too_late", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "C28_GENIANS_2023_ENTRY_2023-05-17_11770", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "C28_GENIANS_2023_GREEN_2023-06-09", "case_id": "C28_GENIANS_2023_ZERO_TRUST_SECURITY_RETENTION", "symbol": "263860", "company_name": "지니언스", "round": "R13", "loop": "36", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C28_SOFTWARE_SECURITY_CONTRACT_RETENTION", "fine_archetype_id": "ZERO_TRUST_NAC_EDR_RECURRING_SECURITY", "sector": "플랫폼·콘텐츠·SW·보안", "primary_archetype": "zero-trust / NAC / EDR security software recurring contracts", "loop_objective": "green_strictness_stress_test", "trigger_type": "Stage3-Green", "trigger_date": "2023-06-09", "evidence_available_at_that_date": "later momentum/revision confirmation after zero-trust/security software rerating had already nearly completed", "evidence_source": "historical public-event/disclosure proxy; stock-web price rows used for OHLC validation", "stage2_evidence_fields": [], "stage3_evidence_fields": ["confirmed_revision", "multiple_public_sources", "financial_visibility"], "stage4b_evidence_fields": [], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/263/263860/2023.csv", "profile_path": "atlas/symbol_profiles/263/263860.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2023-06-09", "entry_price": 17490, "MFE_30D_pct": 0.86, "MFE_90D_pct": 0.86, "MFE_180D_pct": 0.86, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -36.88, "MAE_90D_pct": -36.88, "MAE_180D_pct": -36.88, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2023-06-13", "peak_price": 17640, "drawdown_after_peak_pct": -37.41, "green_lateness_ratio": 0.974, "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": null, "four_b_evidence_type": [], "four_c_protection_label": null, "trigger_outcome_label": "late_green_peak_aftershock", "current_profile_verdict": "current_profile_too_late", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "C28_GENIANS_2023_ENTRY_2023-06-09_17490", "dedupe_for_aggregate": false, "aggregate_group_role": "label_comparison_only", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "C28_AHNLAB_2022_PRICE_ONLY_2022-03-18", "case_id": "C28_AHNLAB_2022_PRICE_THEME_FALSE_POSITIVE", "symbol": "053800", "company_name": "안랩", "round": "R13", "loop": "36", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C28_SOFTWARE_SECURITY_CONTRACT_RETENTION", "fine_archetype_id": "SECURITY_SOFTWARE_PRICE_ONLY_POLITICAL_BLOWOFF_GUARD", "sector": "플랫폼·콘텐츠·SW·보안", "primary_archetype": "security software company with political/price-only blowoff contamination", "loop_objective": "residual_false_positive_mining;4B_non_price_requirement_stress_test;counterexample_mining", "trigger_type": "Price-only Stage2-blocked", "trigger_date": "2022-03-18", "evidence_available_at_that_date": "relative strength and price momentum existed, but contract-retention / customer-renewal evidence did not justify C28 positive promotion", "evidence_source": "stock-web OHLC + qualitative false-positive trigger classification; not a live recommendation", "stage2_evidence_fields": ["relative_strength"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["price_only_local_peak", "valuation_blowoff", "positioning_overheat"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/053/053800/2022.csv", "profile_path": "atlas/symbol_profiles/053/053800.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2022-03-18", "entry_price": 101700, "MFE_30D_pct": 114.85, "MFE_90D_pct": 114.85, "MFE_180D_pct": 114.85, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -6.29, "MAE_90D_pct": -20.35, "MAE_180D_pct": -42.08, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2022-03-24", "peak_price": 218500, "drawdown_after_peak_pct": -73.04, "green_lateness_ratio": null, "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "do_not_promote_price_only_stage", "four_b_evidence_type": ["price_only", "valuation_blowoff", "positioning_overheat"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "false_positive_green_blocked", "current_profile_verdict": "current_profile_correct", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "C28_AHNLAB_2022_ENTRY_2022-03-18_101700", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "C28_AHNLAB_2022_4B_OVERLAY_2022-03-23", "case_id": "C28_AHNLAB_2022_PRICE_THEME_FALSE_POSITIVE", "symbol": "053800", "company_name": "안랩", "round": "R13", "loop": "36", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C28_SOFTWARE_SECURITY_CONTRACT_RETENTION", "fine_archetype_id": "SECURITY_SOFTWARE_PRICE_ONLY_POLITICAL_BLOWOFF_GUARD", "sector": "플랫폼·콘텐츠·SW·보안", "primary_archetype": "security software company with political/price-only blowoff contamination", "loop_objective": "4B_non_price_requirement_stress_test;4C_thesis_break_timing_test", "trigger_type": "Stage4B-overlay", "trigger_date": "2022-03-23", "evidence_available_at_that_date": "price-only blowoff without C28 non-price contract-retention confirmation; useful only as risk overlay, not as positive entry evidence", "evidence_source": "stock-web OHLC + qualitative false-positive trigger classification; not a live recommendation", "stage2_evidence_fields": [], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["price_only_local_peak", "valuation_blowoff", "positioning_overheat"], "stage4c_evidence_fields": ["thesis_evidence_broken"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/053/053800/2022.csv", "profile_path": "atlas/symbol_profiles/053/053800.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2022-03-23", "entry_price": 175800, "MFE_30D_pct": 24.29, "MFE_90D_pct": 24.29, "MFE_180D_pct": 24.29, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -46.53, "MAE_90D_pct": -53.92, "MAE_180D_pct": -66.5, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2022-03-24", "peak_price": 218500, "drawdown_after_peak_pct": -73.04, "green_lateness_ratio": null, "four_b_local_peak_proximity": 0.635, "four_b_full_window_peak_proximity": 0.635, "four_b_timing_verdict": "price_only_local_4B_not_full_without_non_price_evidence", "four_b_evidence_type": ["price_only", "valuation_blowoff", "positioning_overheat"], "four_c_protection_label": "hard_4c_late", "trigger_outcome_label": "4B_overlay_success_as_block_not_entry", "current_profile_verdict": "current_profile_correct", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "C28_AHNLAB_2022_ENTRY_2022-03-23_175800", "dedupe_for_aggregate": false, "aggregate_group_role": "4B_overlay_only", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
```

### 25.4 score_simulation rows
```jsonl
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "C28_DOUZONE_2020_CLOUD_ERP_RETENTION", "trigger_id": "C28_DOUZONE_2020_STAGE2A_2020-04-29", "symbol": "012510", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C28_SOFTWARE_SECURITY_CONTRACT_RETENTION", "raw_component_scores_before": {"contract_score": 6, "backlog_visibility_score": 5, "margin_bridge_score": 7, "revision_score": 6, "relative_strength_score": 8, "customer_quality_score": 8, "policy_or_regulatory_score": 4, "valuation_repricing_score": 8, "execution_risk_score": 2, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 1}, "weighted_score_before": 82, "stage_label_before": "Stage3-Yellow", "raw_component_scores_after": {"contract_score": 8, "backlog_visibility_score": 6, "margin_bridge_score": 7, "revision_score": 6, "relative_strength_score": 8, "customer_quality_score": 9, "policy_or_regulatory_score": 4, "valuation_repricing_score": 7, "execution_risk_score": 2, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 1}, "weighted_score_after": 86, "stage_label_after": "Stage2-Actionable-High / Yellow retained", "changed_components": ["contract_score", "customer_quality_score", "backlog_visibility_score", "valuation_repricing_score"], "component_delta_explanation": "C28-specific recurring ERP/customer retention gate upgrades early non-price evidence without relaxing global Green revision minimum.", "MFE_90D_pct": 54.72, "MAE_90D_pct": -3.19, "score_return_alignment_label": "early_stage2_aligned_green_late", "current_profile_verdict": "current_profile_too_late"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "C28_WINS_2020_SECURITY_APPLIANCE_SERVICE_RETENTION", "trigger_id": "C28_WINS_2020_STAGE2A_2020-04-16", "symbol": "136540", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C28_SOFTWARE_SECURITY_CONTRACT_RETENTION", "raw_component_scores_before": {"contract_score": 5, "backlog_visibility_score": 5, "margin_bridge_score": 6, "revision_score": 5, "relative_strength_score": 6, "customer_quality_score": 7, "policy_or_regulatory_score": 5, "valuation_repricing_score": 5, "execution_risk_score": 2, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 76, "stage_label_before": "Stage3-Yellow / Stage2-Actionable boundary", "raw_component_scores_after": {"contract_score": 7, "backlog_visibility_score": 6, "margin_bridge_score": 6, "revision_score": 5, "relative_strength_score": 6, "customer_quality_score": 8, "policy_or_regulatory_score": 5, "valuation_repricing_score": 5, "execution_risk_score": 2, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 81, "stage_label_after": "Stage2-Actionable-High", "changed_components": ["contract_score", "customer_quality_score", "backlog_visibility_score"], "component_delta_explanation": "Public/enterprise security repeatability is rewarded before late revision confirmation; no Green promotion without revision.", "MFE_90D_pct": 26.87, "MAE_90D_pct": -8.84, "score_return_alignment_label": "stage2_positive_with_acceptable_mae", "current_profile_verdict": "current_profile_too_late"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "C28_GENIANS_2023_ZERO_TRUST_SECURITY_RETENTION", "trigger_id": "C28_GENIANS_2023_STAGE2A_2023-05-17", "symbol": "263860", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C28_SOFTWARE_SECURITY_CONTRACT_RETENTION", "raw_component_scores_before": {"contract_score": 4, "backlog_visibility_score": 4, "margin_bridge_score": 4, "revision_score": 3, "relative_strength_score": 7, "customer_quality_score": 6, "policy_or_regulatory_score": 7, "valuation_repricing_score": 5, "execution_risk_score": 3, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 72, "stage_label_before": "Stage2-Actionable", "raw_component_scores_after": {"contract_score": 6, "backlog_visibility_score": 5, "margin_bridge_score": 4, "revision_score": 3, "relative_strength_score": 7, "customer_quality_score": 7, "policy_or_regulatory_score": 8, "valuation_repricing_score": 5, "execution_risk_score": 3, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 79, "stage_label_after": "Stage3-Yellow / small-cap security retention watch", "changed_components": ["contract_score", "customer_quality_score", "policy_or_regulatory_score", "backlog_visibility_score"], "component_delta_explanation": "Zero-trust/NAC/EDR policy and renewal route should prevent early evidence from being stuck below Yellow when evidence is non-price and recurring.", "MFE_90D_pct": 49.87, "MAE_90D_pct": -6.2, "score_return_alignment_label": "missed_structural_stage2_should_be_yellow", "current_profile_verdict": "current_profile_too_late"}
{"row_type": "score_simulation", "profile_id": "counterexample_guard_profile", "case_id": "C28_AHNLAB_2022_PRICE_THEME_FALSE_POSITIVE", "trigger_id": "C28_AHNLAB_2022_PRICE_ONLY_2022-03-18", "symbol": "053800", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C28_SOFTWARE_SECURITY_CONTRACT_RETENTION", "raw_component_scores_before": {"contract_score": 2, "backlog_visibility_score": 1, "margin_bridge_score": 2, "revision_score": 1, "relative_strength_score": 10, "customer_quality_score": 4, "policy_or_regulatory_score": 3, "valuation_repricing_score": 10, "execution_risk_score": 7, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 1}, "weighted_score_before": 81, "stage_label_before": "would-be Stage3-Yellow if RS/valuation were over-weighted", "raw_component_scores_after": {"contract_score": 1, "backlog_visibility_score": 1, "margin_bridge_score": 1, "revision_score": 1, "relative_strength_score": 4, "customer_quality_score": 3, "policy_or_regulatory_score": 2, "valuation_repricing_score": 3, "execution_risk_score": 9, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 1}, "weighted_score_after": 59, "stage_label_after": "Blocked / 4B watch only", "changed_components": ["relative_strength_score", "valuation_repricing_score", "execution_risk_score", "contract_score"], "component_delta_explanation": "C28 guard caps price-only political/security-stock blowoff because no repeat contract-retention evidence is present.", "MFE_90D_pct": 114.85, "MAE_90D_pct": -20.35, "score_return_alignment_label": "price_moved_without_evidence_blocked", "current_profile_verdict": "current_profile_correct"}
```

### 25.5 profile aggregate rows
```jsonl
{"row_type": "aggregate", "profile_id": "P0_e2r_2_1_stock_web_calibrated_proxy", "profile_scope": "global calibrated proxy", "profile_hypothesis": "Keep current global thresholds; Stage2 bonus exists but C28 has no special recurring-contract gate.", "changed_axes": "none", "changed_thresholds": "none", "eligible_trigger_count": 4, "selected_entry_trigger_per_case": "late Green for 3 positives; AhnLab blocked", "avg_MFE_90D_pct": 4.49, "avg_MAE_90D_pct": -26.09, "avg_MFE_180D_pct": 4.49, "avg_MAE_180D_pct": -26.09, "false_positive_rate": 0.0, "missed_structural_count": 3, "late_green_count": 3, "avg_green_lateness_ratio": 0.883, "avg_four_b_local_peak_proximity": 0.635, "avg_four_b_full_window_peak_proximity": 0.635, "score_return_alignment_verdict": "guards work, but C28 positives are often too late"}
{"row_type": "aggregate", "profile_id": "P0b_e2r_2_0_baseline_reference", "profile_scope": "rollback reference", "profile_hypothesis": "Earlier profile without calibrated guardrails; price-only and late Green risk both larger.", "changed_axes": "rollback reference only", "changed_thresholds": "old Stage thresholds", "eligible_trigger_count": 4, "selected_entry_trigger_per_case": "inconsistent; AhnLab at risk of false positive", "avg_MFE_90D_pct": 61.58, "avg_MAE_90D_pct": -9.65, "avg_MFE_180D_pct": 61.58, "avg_MAE_180D_pct": -20.65, "false_positive_rate": 0.25, "missed_structural_count": 2, "late_green_count": 2, "avg_green_lateness_ratio": 0.883, "avg_four_b_local_peak_proximity": 0.635, "avg_four_b_full_window_peak_proximity": 0.635, "score_return_alignment_verdict": "higher MFE partly from false-positive inclusion; not safer"}
{"row_type": "aggregate", "profile_id": "P1_L8_sector_specific_candidate_profile", "profile_scope": "sector_specific", "profile_hypothesis": "For L8 software/security, reward repeatable contract-retention route but keep price-only guard.", "changed_axes": "l8_recurring_contract_retention_bonus +2; price_only cap kept", "changed_thresholds": "no global threshold change", "eligible_trigger_count": 4, "selected_entry_trigger_per_case": "Stage2 for 3 positives; AhnLab blocked", "avg_MFE_90D_pct": 43.82, "avg_MAE_90D_pct": -6.08, "avg_MFE_180D_pct": 55.27, "avg_MAE_180D_pct": -6.08, "false_positive_rate": 0.0, "missed_structural_count": 0, "late_green_count": 0, "avg_green_lateness_ratio": 0.0, "avg_four_b_local_peak_proximity": 0.635, "avg_four_b_full_window_peak_proximity": 0.635, "score_return_alignment_verdict": "best balance in this loop"}
{"row_type": "aggregate", "profile_id": "P2_C28_canonical_archetype_candidate_profile", "profile_scope": "canonical_archetype_specific", "profile_hypothesis": "C28-specific gate: repeat/reten­tion/customer renewal evidence can upgrade Stage2/Yellow; single-title/political/theme price spikes cannot.", "changed_axes": "c28_repeatable_ip_retention_gate +3; c28_single_event_cap -6", "changed_thresholds": "Green thresholds unchanged; Yellow can be reached through C28 gate", "eligible_trigger_count": 4, "selected_entry_trigger_per_case": "Stage2 for repeat positives; AhnLab blocked", "avg_MFE_90D_pct": 43.82, "avg_MAE_90D_pct": -6.08, "avg_MFE_180D_pct": 55.27, "avg_MAE_180D_pct": -6.08, "false_positive_rate": 0.0, "missed_structural_count": 0, "late_green_count": 0, "avg_green_lateness_ratio": 0.0, "avg_four_b_local_peak_proximity": 0.635, "avg_four_b_full_window_peak_proximity": 0.635, "score_return_alignment_verdict": "candidate rule supported by 3 positive + 1 counterexample"}
{"row_type": "aggregate", "profile_id": "P3_counterexample_guard_profile", "profile_scope": "canonical_archetype_specific guard", "profile_hypothesis": "Explicitly demote price-only/political/security-stock momentum without contract evidence.", "changed_axes": "c28_price_only_or_political_blowoff_cap -8; 4B risk overlay only", "changed_thresholds": "no positive threshold relaxation", "eligible_trigger_count": 1, "selected_entry_trigger_per_case": "AhnLab blocked / 4B watch only", "avg_MFE_90D_pct": null, "avg_MAE_90D_pct": null, "avg_MFE_180D_pct": null, "avg_MAE_180D_pct": null, "false_positive_rate": 0.0, "missed_structural_count": 0, "late_green_count": 0, "avg_green_lateness_ratio": null, "avg_four_b_local_peak_proximity": 0.635, "avg_four_b_full_window_peak_proximity": 0.635, "score_return_alignment_verdict": "strengthens existing price-only and non-price 4B guardrails"}
```

### 25.6 shadow_weight rows
```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,c28_repeatable_contract_retention_gate,canonical_archetype_specific,L8_PLATFORM_CONTENT_SW_SECURITY,C28_SOFTWARE_SECURITY_CONTRACT_RETENTION,0,3,+3,Recurring B2B/public security or enterprise software contracts captured upside before strict Green.,P2 raises early non-price positives: avg 90D MFE 43.82 / avg 90D MAE -6.08.,C28_DOUZONE_2020_STAGE2A_2020-04-29|C28_WINS_2020_STAGE2A_2020-04-16|C28_GENIANS_2023_STAGE2A_2023-05-17,3,3,1,medium,archetype_shadow_only,not production; post-calibrated residual
shadow_weight,c28_price_only_theme_cap,canonical_archetype_specific,L8_PLATFORM_CONTENT_SW_SECURITY,C28_SOFTWARE_SECURITY_CONTRACT_RETENTION,0,-8,-8,Security/software ticker identity alone is insufficient when the trigger family is price-only or political/event-driven.,Blocks AhnLab false positive; keeps full_4B_requires_non_price_evidence intact.,C28_AHNLAB_2022_PRICE_ONLY_2022-03-18|C28_AHNLAB_2022_4B_OVERLAY_2022-03-23,2,1,1,medium,guard_shadow_only,not production; price-only cannot promote Stage2/3
shadow_weight,l8_recurring_software_security_stage2_bonus,sector_specific,L8_PLATFORM_CONTENT_SW_SECURITY,C28_SOFTWARE_SECURITY_CONTRACT_RETENTION,0,2,+2,L8 recurring contract quality deserves sector-level Stage2 support when non-price evidence is present.,Improves early selection for Douzone/Wins/Genians without AhnLab false positive.,C28_DOUZONE_2020_STAGE2A_2020-04-29|C28_WINS_2020_STAGE2A_2020-04-16|C28_GENIANS_2023_STAGE2A_2023-05-17,3,3,1,low_to_medium,sector_shadow_only,needs more C26/C28/C32 cross-validation before production
```

### 25.7 residual_contribution row
```jsonl
{"row_type": "residual_contribution", "round": "R13", "loop": "36", "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C28_SOFTWARE_SECURITY_CONTRACT_RETENTION", "new_independent_case_count": 4, "reused_case_count": 0, "new_symbol_count": 4, "new_trigger_family_count": 4, "tested_existing_calibrated_axes": ["stage2_actionable_evidence_bonus", "stage3_yellow_total_min", "stage3_green_total_min", "stage3_green_revision_min", "price_only_blowoff_blocks_positive_stage", "full_4b_requires_non_price_evidence", "hard_4c_thesis_break_routes_to_4c"], "residual_error_types_found": ["current_profile_too_late_for_recurring_contract_software", "late_green_near_peak", "price_only_security_ticker_false_positive_risk"], "loop_contribution_label": "canonical_archetype_rule_candidate", "do_not_propose_new_weight_delta": false}
```

### 25.8 narrative_only rows
```jsonl
{"row_type": "narrative_only", "case_id": "NONE", "symbol": null, "large_sector_id": "L8_PLATFORM_CONTENT_SW_SECURITY", "canonical_archetype_id": "C28_SOFTWARE_SECURITY_CONTRACT_RETENTION", "reason": "all selected rows had usable 180D stock-web windows; no narrative-only price row generated", "price_source": "Songdaiki/stock-web", "usage": "not_weight_calibration"}
```


## 26. Deferred Coding Agent Handoff Prompt


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

|next_round|scope|reason|
|---|---|---|
|R13_loop_37|L8_PLATFORM_CONTENT_SW_SECURITY / C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE|Continue L8 residuals by comparing recurring software/contract retention vs ad/platform operating leverage.|


## 28. Source Notes

- Stock-Web manifest: `atlas/manifest.json` confirmed max_date 2026-02-20, raw_unadjusted_marcap, tradable_raw, and full OHLC atlas committed to main.

- Stock-Web schema: `atlas/schema.json` confirmed tradable shard columns, MFE/MAE formulas, calibration basis, and corporate-action blocking rules.

- Symbol profiles checked: `012/012510.json`, `136/136540.json`, `263/263860.json`, `053/053800.json`.

- Stock-web OHLC rows sampled directly from tradable shards listed in trigger rows.

- Allowed stock_agent artifacts checked for duplicate/coverage context only: `reports/e2r_calibration/ingest_summary.md` and `reports/e2r_calibration/applied_scoring_diff.md`.

- Evidence narratives are historical research proxies. Before production promotion, attach exact original filings/news/report URLs to the evidence_source fields; the quantitative calibration rows are valid only for price behavior and clean OHLC windows.
