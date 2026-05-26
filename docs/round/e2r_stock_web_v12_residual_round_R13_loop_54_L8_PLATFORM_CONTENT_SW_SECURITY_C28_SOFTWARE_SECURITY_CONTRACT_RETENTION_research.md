# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
research_session = post_calibrated_sector_archetype_residual_research
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
round = R13
loop = 54
large_sector_id = L8_PLATFORM_CONTENT_SW_SECURITY
canonical_archetype_id = C28_SOFTWARE_SECURITY_CONTRACT_RETENTION
fine_archetype_id = SECURITY_OPERATIONS_SOAR_CONTRACT_RETENTION | PUBLIC_AUTH_IDENTITY_SECURITY_THEME_GUARD | QUANTUM_SECURITY_THEME_CAP | SMALLCAP_SECURITY_MSS_EVENT_PREMIUM_GUARD
output_format = one_standalone_markdown_file
production_scoring_changed = false
shadow_weight_only = true
stock_agent_code_access_allowed = false
stock_agent_code_patch_allowed = false
stock_agent_live_scan_allowed = false
stock_web_price_atlas_access_required = true
handoff_prompt_embedded = true
handoff_prompt_executed_now = false
```

This file is a historical calibration artifact. It is not a current stock screen, not a live candidate list, not a recommendation, and not a repository patch.

## 1. Current Calibrated Profile Assumption

```text
current_default_profile_proxy = e2r_2_1_stock_web_calibrated
rollback_reference_profile_id = e2r_2_0_baseline_reference

stage2_actionable_evidence_bonus = +2.0
stage3_yellow_total_min = 75.0
stage3_green_total_min = 87.0
stage3_green_revision_min = 55.0
stage3_cross_evidence_green_buffer = +1.5
price_only_blowoff_blocks_positive_stage = true
full_4b_requires_non_price_evidence = true
hard_4c_thesis_break_routes_to_4c = true
```

This loop does not re-prove the global profile. It tests residual C28 behavior: security operations and recurring customer routes can re-rate earlier than strict Green, while identity/quantum/security headline premiums should be capped unless contract retention, repeat customer confirmation, or revision evidence appears.

## 2. Round / Large Sector / Canonical Archetype Scope

```text
large_sector_id = L8_PLATFORM_CONTENT_SW_SECURITY
canonical_archetype_id = C28_SOFTWARE_SECURITY_CONTRACT_RETENTION
loop_objective = auto_coverage_gap_fill, sector_specific_rule_discovery, canonical_archetype_compression, counterexample_mining, 4B_non_price_requirement_stress_test
```

This loop intentionally remains inside C28. The novelty is not a new canonical archetype. The novelty is new C28 symbols and new trigger families that avoid the previously repeated large/representative C28 set.

## 3. Previous Coverage / Duplicate Avoidance Check

This loop is generated after the C27 Loop 53 handoff and uses the C28 security/software retention coverage lane. The case set intentionally avoids the older C28 Douzone/AhnLab/Wins/Genian/Hancom cluster and focuses on security-ops, identity, quantum-security, and MSS event-premium residual paths. It is treated as a standalone v12 MD for later batch ingestion; production scoring is not changed here.

Allowed stock_agent research artifacts were not opened as code. Duplicate avoidance was based on prior local v12 MD outputs and the previous loop state.

Previous C28 coverage concentrated on the following symbol families:

```text
012510 = 더존비즈온
030520 = 한글과컴퓨터
053800 = 안랩
136540 = 윈스
131370 = 알서포트
263860 = 지니언스
```

This loop avoids those symbols and avoids the repeated `AhnLab/Douzone/Wins/Genian` trigger families.

Selected new C28 symbols:

```text
067920 = 이글루
184230 = SGA솔루션즈
042510 = 라온시큐어
203650 = 드림시큐리티
356890 = 싸이버원
```

Novelty decision:

```text
same_canonical_archetype_research = allowed_and_required
same_symbol_same_trigger_date_research = none
same_archetype_new_symbol_count = 5
same_archetype_new_trigger_family_count = 5
new_independent_case_ratio = 1.00
```

## 4. Stock-Web OHLC Input / Price Source Validation

`Songdaiki/stock-web` manifest and schema were checked before case work.

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
```

Manifest fields used:

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

Important caveat:

```text
price_basis = tradable_raw
price_adjustment_status = raw_unadjusted_marcap
stock_web_manifest_max_date = 2026-02-20
```

All forward windows in this MD are judged against the stock-web manifest max date, not against the current calendar date.

## 5. Historical Eligibility Gate

|symbol|profile_path|entry_year_shard|entry_date|180D window|corporate_action_window_status|calibration_usable|block_reason|
|---|---|---|---|---|---|---|---|
|067920|atlas/symbol_profiles/067/067920.json|atlas/ohlcv_tradable_by_symbol_year/067/067920/2021.csv|2021-02-04|available by manifest/profile max_date 2026-02-20|clean_180D_window|True|none|
|184230|atlas/symbol_profiles/184/184230.json|atlas/ohlcv_tradable_by_symbol_year/184/184230/2021.csv|2021-02-23|available by manifest/profile max_date 2026-02-20|clean_180D_window|True|none|
|042510|atlas/symbol_profiles/042/042510.json|atlas/ohlcv_tradable_by_symbol_year/042/042510/2022.csv|2022-01-28|available by manifest/profile max_date 2026-02-20|clean_180D_window|True|none|
|203650|atlas/symbol_profiles/203/203650.json|atlas/ohlcv_tradable_by_symbol_year/203/203650/2023.csv|2023-03-09|available by manifest/profile max_date 2026-02-20|clean_180D_window|True|none|
|356890|atlas/symbol_profiles/356/356890.json|atlas/ohlcv_tradable_by_symbol_year/356/356890/2023.csv|2023-02-20|available by manifest/profile max_date 2026-02-20|clean_180D_window|True|none|

Eligibility conclusion:

```text
calibration_usable_case_count = 5
calibration_usable_trigger_count = 10
representative_trigger_count = 5
corporate_action_contaminated_180D_window_count = 0
```

1Y/2Y fields are not used for this loop's weight calibration. The quantitative calibration decision is based on 30D/90D/180D windows.

## 6. Canonical Archetype Compression Map

| fine_archetype_id | canonical_archetype_id | Compression logic |
|---|---|---|
| SECURITY_OPERATIONS_SOAR_CONTRACT_RETENTION | C28_SOFTWARE_SECURITY_CONTRACT_RETENTION | Retained security operations, SOC/SOAR, managed detection, or customer-retained security service route. |
| SMALLCAP_SECURITY_INTEGRATION_EVENT_PREMIUM | C28_SOFTWARE_SECURITY_CONTRACT_RETENTION | Security integration and product event route; positive only if supported by non-price customer/retention bridge. |
| PUBLIC_AUTH_IDENTITY_SECURITY_THEME_GUARD | C28_SOFTWARE_SECURITY_CONTRACT_RETENTION | Identity/DID/public-auth theme is inside C28 but should not promote without retained-contract evidence. |
| QUANTUM_SECURITY_THEME_CAP | C28_SOFTWARE_SECURITY_CONTRACT_RETENTION | Quantum/security theme belongs to C28 but should be capped unless customer/revenue bridge is visible. |
| SMALLCAP_SECURITY_MSS_EVENT_PREMIUM_GUARD | C28_SOFTWARE_SECURITY_CONTRACT_RETENTION | MSS/security event spike can be watch/4B overlay; not Stage3 without repeat revenue confirmation. |

## 7. Case Selection Summary

|case_id|symbol|company|role|positive_or_counterexample|best_trigger|current_profile_verdict|calibration_usable|new_independent|
|---|---|---|---|---|---|---|---|---|
|R13L54_C28_067920_IGLOO_SECURITY_OPS_2021|067920|이글루|structural_success|positive|R13L54_C28_067920_STAGE2A_20210204|current_profile_too_late|True|True|
|R13L54_C28_184230_SGA_SOLUTIONS_2021|184230|SGA솔루션즈|high_mae_success|positive|R13L54_C28_184230_STAGE2A_20210223|current_profile_too_late|True|True|
|R13L54_C28_042510_RAON_IDENTITY_2022|042510|라온시큐어|failed_rerating|counterexample|R13L54_C28_042510_STAGE2_BLOCKED_20220128|current_profile_correct|True|True|
|R13L54_C28_203650_DREAM_QUANTUM_2023|203650|드림시큐리티|failed_rerating|counterexample|R13L54_C28_203650_STAGE2_BLOCKED_20230309|current_profile_correct|True|True|
|R13L54_C28_356890_CYBERONE_MSS_2023|356890|싸이버원|4B_too_early|counterexample|R13L54_C28_356890_STAGE2_BLOCKED_20230220|current_profile_false_positive|True|True|

## 8. Positive vs Counterexample Balance

```text
positive_case_count = 2
counterexample_count = 3
4B_case_count = 3
4C_case_count = 1
minimum_positive_case_count = passed
minimum_counterexample_count = passed
minimum_calibration_usable_case_count = passed
```

Interpretation:

- Positive C28 rows are accepted only when a non-price retained security operations/customer route exists.
- Counterexamples show that security theme, identity/DID, quantum, or event-premium price movement should not by itself promote Stage2/3.
- 4B rows are retained as overlays and not as full 4B unless non-price overheat evidence exists.

## 9. Evidence Source Map

| case_id | evidence scope used in this MD | production note |
|---|---|---|
| R13L54_C28_067920_IGLOO_SECURITY_OPS_2021 | historical public/security-ops demand proxy + stock-web OHLC validation | attach primary filing/news before production weight promotion |
| R13L54_C28_184230_SGA_SOLUTIONS_2021 | security solution/integration event proxy + stock-web OHLC validation | positive but high-MAE; require additional non-price confirmation |
| R13L54_C28_042510_RAON_IDENTITY_2022 | identity/DID/security-policy theme proxy + stock-web OHLC validation | counterexample; contract-retention evidence missing |
| R13L54_C28_203650_DREAM_QUANTUM_2023 | quantum/security headline proxy + stock-web OHLC validation | counterexample; theme cap candidate |
| R13L54_C28_356890_CYBERONE_MSS_2023 | small-cap security event premium proxy + stock-web OHLC validation | counterexample; 4B/watch overlay rather than promotion |

Evidence warning:

```text
Evidence source is deliberately separated from price outcome.
No trigger label is assigned from future return.
The non-price evidence in this MD is research-proxy level and must be reattached to primary source documents before production promotion.
```

## 10. Price Data Source Map

|symbol|company|profile_path|shard_path|known CA dates from profile|180D status|
|---|---|---|---|---|---|
|067920|이글루|atlas/symbol_profiles/067/067920.json|atlas/ohlcv_tradable_by_symbol_year/067/067920/2021.csv|2014-04-24|clean_180D_window|
|184230|SGA솔루션즈|atlas/symbol_profiles/184/184230.json|atlas/ohlcv_tradable_by_symbol_year/184/184230/2021.csv|2015-06-16; 2015-07-10|clean_180D_window|
|042510|라온시큐어|atlas/symbol_profiles/042/042510.json|atlas/ohlcv_tradable_by_symbol_year/042/042510/2022.csv|2007-07-25; 2008-10-16; 2009-09-28; 2009-11-13; 2010-03-18; 2011-05-19; 2012-11-09; 2023-12-18; 2025-05-07|clean_180D_window|
|203650|드림시큐리티|atlas/symbol_profiles/203/203650.json|atlas/ohlcv_tradable_by_symbol_year/203/203650/2023.csv|2017-01-20; 2019-11-26; 2025-11-18; 2025-12-12|clean_180D_window|
|356890|싸이버원|atlas/symbol_profiles/356/356890.json|atlas/ohlcv_tradable_by_symbol_year/356/356890/2023.csv|2024-05-07|clean_180D_window|

## 11. Case-by-Case Trigger Grid

|trigger_id|symbol|trigger_type|trigger_date|entry_date|entry_price|MFE90|MAE90|MFE180|MAE180|peak|current_verdict|agg_role|
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R13L54_C28_067920_STAGE2A_20210204|067920|Stage2-Actionable|2021-02-03|2021-02-04|6040|47.52|-8.94|47.52|-8.94|2021-05-07 8910|current_profile_too_late|representative|
|R13L54_C28_067920_GREEN_20210507|067920|Stage3-Green|2021-05-07|2021-05-07|7890|12.93|-17.11|12.93|-17.11|2021-05-07 8910|current_profile_too_late|label_comparison_only|
|R13L54_C28_184230_STAGE2A_20210223|184230|Stage2-Actionable|2021-02-22|2021-02-23|1235|83.0|-10.12|83.0|-11.34|2021-06-17 2260|current_profile_too_late|representative|
|R13L54_C28_184230_4B_20210617|184230|Stage4B|2021-06-17|2021-06-17|2065|9.44|-31.23|9.44|-46.97|2021-06-17 2260|current_profile_4B_too_early|4B_overlay_only|
|R13L54_C28_042510_STAGE2_BLOCKED_20220128|042510|Stage2-Blocked|2022-01-27|2022-01-28|3395|21.8|-16.35|21.8|-39.03|2022-03-16 4135|current_profile_correct|representative|
|R13L54_C28_042510_4C_20221013|042510|Stage4C|2022-10-13|2022-10-13|2105|27.08|-1.66|27.08|-1.66|2022-10-26 2680|current_profile_4C_too_late|4C_overlay_only|
|R13L54_C28_203650_STAGE2_BLOCKED_20230309|203650|Stage2-Blocked|2023-03-09|2023-03-09|3740|9.63|-24.06|9.63|-24.06|2023-03-10 4100|current_profile_correct|representative|
|R13L54_C28_203650_4B_20230310|203650|Stage4B|2023-03-10|2023-03-10|3790|8.18|-25.07|8.18|-25.07|2023-03-10 4100|current_profile_4B_too_early|4B_overlay_only|
|R13L54_C28_356890_STAGE2_BLOCKED_20230220|356890|Stage2-Blocked|2023-02-20|2023-02-20|10890|29.94|-13.22|29.94|-17.91|2023-02-21 14150|current_profile_false_positive|representative|
|R13L54_C28_356890_4B_20230221|356890|Stage4B|2023-02-21|2023-02-21|13130|7.77|-26.88|7.77|-31.91|2023-02-21 14150|current_profile_4B_too_early|4B_overlay_only|

## 12. Trigger-Level OHLC Backtest Tables

### Representative triggers only

|case_id|trigger_id|entry|MFE30|MFE90|MFE180|MAE30|MAE90|MAE180|peak_date|peak_price|drawdown_after_peak|outcome|
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R13L54_C28_067920_IGLOO_SECURITY_OPS_2021|R13L54_C28_067920_STAGE2A_20210204|2021-02-04 / 6040|13.25|47.52|47.52|-8.94|-8.94|-8.94|2021-05-07|8910|-26.6|structural_success_high_late_green|
|R13L54_C28_184230_SGA_SOLUTIONS_2021|R13L54_C28_184230_STAGE2A_20210223|2021-02-23 / 1235|33.6|83.0|83.0|-10.12|-10.12|-11.34|2021-06-17|2260|-51.55|high_mae_success|
|R13L54_C28_042510_RAON_IDENTITY_2022|R13L54_C28_042510_STAGE2_BLOCKED_20220128|2022-01-28 / 3395|21.8|21.8|21.8|-5.15|-16.35|-39.03|2022-03-16|4135|-49.94|failed_rerating_theme_guard_worked|
|R13L54_C28_203650_DREAM_QUANTUM_2023|R13L54_C28_203650_STAGE2_BLOCKED_20230309|2023-03-09 / 3740|9.63|9.63|9.63|-17.25|-24.06|-24.06|2023-03-10|4100|-26.22|failed_rerating_quantum_theme_guard|
|R13L54_C28_356890_CYBERONE_MSS_2023|R13L54_C28_356890_STAGE2_BLOCKED_20230220|2023-02-20 / 10890|29.94|29.94|29.94|-7.25|-13.22|-17.91|2023-02-21|14150|-36.82|event_premium_not_structural_stage3|

Representative aggregate:

```text
eligible_representative_trigger_count = 5
avg_MFE_90D_pct = 38.38
avg_MAE_90D_pct = -14.54
avg_MFE_180D_pct = 38.38
avg_MAE_180D_pct = -20.26
positive_representative_count = 2
counterexample_representative_count = 3
```

## 13. Current Calibrated Profile Stress Test

| case_id | Current profile likely behavior | Backtest alignment | Verdict |
|---|---|---|---|
| R13L54_C28_067920_IGLOO_SECURITY_OPS_2021 | Might wait for confirmed revision/Green rather than accepting earlier security-ops retention bridge | Stage2-style entry captured much more upside than later Green | current_profile_too_late |
| R13L54_C28_184230_SGA_SOLUTIONS_2021 | Might under-promote due small-cap quality/high-MAE risk | MFE was strong but MAE and later drawdown require guard | current_profile_too_late |
| R13L54_C28_042510_RAON_IDENTITY_2022 | Should block headline/identity theme without retained contract bridge | Blocking is correct; 180D MAE was deep | current_profile_correct |
| R13L54_C28_203650_DREAM_QUANTUM_2023 | Should block quantum/security theme without retained contract bridge | Blocking is correct; MFE was weak and MAE high | current_profile_correct |
| R13L54_C28_356890_CYBERONE_MSS_2023 | Residual risk of false positive if event premium is scored like retained security demand | Durable follow-through weak after spike | current_profile_false_positive |

Axis answers:

```text
stage2_actionable_evidence_bonus = useful for 067920/184230 only with non-price security-ops retention evidence
stage3_yellow_total_min = too strict for 067920 early route, but appropriate for theme-only counterexamples
stage3_green_total_min = appropriate; do not lower globally
stage3_green_revision_min = appropriate globally; C28 needs separate retained-contract bridge, not revision bypass
price_only_blowoff_blocks_positive_stage = strengthened
full_4b_requires_non_price_evidence = strengthened
hard_4c_thesis_break_routes_to_4c = kept; RAON shows 4C can be late if theme-only thesis erodes slowly
```

## 14. Stage2 / Yellow / Green Comparison

| case_id | Stage2-actionable entry | Green/comparison entry | peak after Stage2 | green_lateness_ratio | interpretation |
|---|---:|---:|---:|---:|---|
| R13L54_C28_067920_IGLOO_SECURITY_OPS_2021 | 6040 | 7890 | 8910 | 0.645 | Green catches the move late; C28 retention bridge should allow Yellow/Stage2-actionable earlier. |
| R13L54_C28_184230_SGA_SOLUTIONS_2021 | 1235 | n/a | 2260 | not_applicable | No clean Green; high-MAE success remains Stage2-actionable shadow only. |
| R13L54_C28_042510_RAON_IDENTITY_2022 | 3395 | n/a | 4135 | not_applicable | Theme-only path should remain blocked/watch. |
| R13L54_C28_203650_DREAM_QUANTUM_2023 | 3740 | n/a | 4100 | not_applicable | Weak MFE and large MAE; no Green relaxation. |
| R13L54_C28_356890_CYBERONE_MSS_2023 | 10890 | n/a | 14150 | not_applicable | Event premium spike; not enough for Stage3. |

## 15. 4B Local vs Full-window Timing Audit

| trigger_id | Stage2 reference | Stage4B entry | local_peak_proximity | full_window_peak_proximity | evidence_type | verdict |
|---|---:|---:|---:|---:|---|---|
| R13L54_C28_184230_4B_20210617 | 1235 | 2065 | 0.810 | 0.810 | price_only, positioning_overheat | Good price proximity but not full 4B without non-price overheat evidence. |
| R13L54_C28_203650_4B_20230310 | 3740 | 3790 | 1.000 | 0.139 | price_only | Price-only local 4B too early; no full 4B. |
| R13L54_C28_356890_4B_20230221 | 10890 | 13130 | 1.000 | 0.687 | price_only, positioning_overheat | Overlay useful, but full 4B needs non-price evidence. |

Conclusion:

```text
existing_axis_strengthened = full_4b_requires_non_price_evidence
do_not_treat_price_only_local_peak_as_full_4B = true
```

## 16. 4C Protection Audit

| trigger_id | prior peak | 4C entry | label | protection interpretation |
|---|---:|---:|---|---|
| R13L54_C28_042510_4C_20221013 | 4135 | 2105 | hard_4c_late | Most drawdown already occurred by the time theme-only thesis was visibly broken. |
| R13L54_C28_203650_STAGE2_BLOCKED_20230309 | 4100 | n/a | thesis_break_watch_only | Blocking positive stage is more useful than late 4C. |
| R13L54_C28_356890_STAGE2_BLOCKED_20230220 | 14150 | n/a | thesis_break_watch_only | Event premium should be watched as 4B/guard path. |

## 17. Sector-Specific Rule Candidate

```text
rule_scope = sector_specific
large_sector_id = L8_PLATFORM_CONTENT_SW_SECURITY
candidate_axis = l8_security_theme_to_retention_bridge_guard
proposal_type = sector_shadow_only
```

Rule candidate:

```text
If a L8 security software/security service name has only policy/headline/identity/quantum/security event evidence, do not promote to Stage2-actionable or Stage3 on price/relative strength alone.

If the same name has non-price retained security operations, recurring customer, SOC/SOAR/MSS service, repeat deployment, or confirmed revenue bridge evidence, allow C28 Stage2-actionable shadow promotion even before strict Green, but keep high-MAE guard active.
```

Backtest effect:

```text
067920 and 184230 remain eligible positive rows.
042510, 203650, and 356890 are blocked or watch-only.
false_positive_rate improves versus a broad security-theme scoring path.
```

## 18. Canonical-Archetype Rule Candidate

```text
rule_scope = canonical_archetype_specific
canonical_archetype_id = C28_SOFTWARE_SECURITY_CONTRACT_RETENTION
candidate_axis_1 = c28_security_ops_retention_stage2_shadow_bonus
candidate_axis_2 = c28_identity_quantum_theme_guard
```

Candidate logic:

```text
c28_security_ops_retention_stage2_shadow_bonus = +3
eligible only if:
- non-price customer / retained operation / managed security / recurring service evidence exists,
- evidence is available at or before trigger_date,
- 180D window is clean,
- execution/accounting/dilution risk is not severe.

c28_identity_quantum_theme_guard = -4
applies if:
- evidence is mainly DID/public-auth/quantum/headline security theme,
- no retained customer or repeat revenue confirmation is visible,
- price action is the main signal.
```

## 19. Before / After Backtest Comparison

|profile_id|scope|hypothesis|eligible_trigger_count|selected_entry_trigger_per_case|avg_MFE90|avg_MAE90|avg_MFE180|avg_MAE180|false_positive_rate|missed_structural_count|late_green_count|score_return_alignment_verdict|
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|P0_e2r_2_1_stock_web_calibrated_proxy|global current|Already-applied global profile with price-only and non-price 4B guards|5|067920,184230,042510,203650,356890|38.38|-14.54|38.38|-20.26|0.20~0.40 residual|2|1|partially_aligned_but_late_or_theme_sensitive|
|P0b_e2r_2_0_baseline_reference|rollback reference|Pre-stock-web calibration would over-trust price/RS and under-block theme-only spikes|5|same representative triggers|38.38|-14.54|38.38|-20.26|0.60|2|1|weak_alignment|
|P1_sector_specific_candidate_profile|L8 sector shadow|Add security-ops retention bridge and event-premium guard|5|067920,184230 selected; 042510/203650/356890 blocked or watch-only|65.26|-9.53|65.26|-10.14|0.00|0|1|improved|
|P2_canonical_archetype_candidate_profile|C28 archetype shadow|Promote only retained security contracts/customer route; cap identity/quantum/headline-only paths|5|067920,184230 selected; others blocked|65.26|-9.53|65.26|-10.14|0.00|0|1|best_explanatory_fit|
|P3_counterexample_guard_profile|C28 guard profile|Hard cap for security theme without customer retention/revision confirmation|5|only non-price bridge rows pass Stage2-actionable|65.26|-9.53|65.26|-10.14|0.00|1|1|safer_but_may_miss_high-MAE_success|

## 20. Score-Return Alignment Matrix

| symbol | before_label | after_label | 90D MFE / MAE | alignment |
|---|---|---|---|---|
| 067920 | Stage2-Actionable | Stage3-Yellow-shadow | +47.52 / -8.94 | improved; earlier than Green captures upside |
| 184230 | Stage2-watch | Stage2-Actionable-shadow-high-MAE-guard | +83.00 / -10.12 | improved but guarded |
| 042510 | Stage2-watch | Stage2-blocked-theme-guard | +21.80 / -16.35 | improved block |
| 203650 | Stage2-watch | Stage2-blocked-quantum-theme-guard | +9.63 / -24.06 | improved block |
| 356890 | Stage2-watch / false positive risk | Stage2-blocked-event-premium-guard | +29.94 / -13.22 | safer; avoids false Green |

## 21. Coverage Matrix

|large_sector_id|canonical_archetype_id|fine_archetype_id|positive_case_count|counterexample_count|4B_case_count|4C_case_count|new_independent_case_count|reused_case_count|calibration_usable_trigger_count|representative_trigger_count|current_profile_error_count|sector_rule_candidate|canonical_rule_candidate|coverage_gap_after_this_loop|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|L8_PLATFORM_CONTENT_SW_SECURITY|C28_SOFTWARE_SECURITY_CONTRACT_RETENTION|mixed: security_ops / identity / quantum / MSS event premium|2|3|3|1|5|0|10|5|3|True|True|C28 now has smaller-security-ops positives plus identity/quantum/event-premium counterexamples; still needs SaaS retention/subscription examples outside security.|

## 22. Residual Contribution Summary

```text
new_independent_case_count: 5
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 5
same_archetype_new_symbol_count: 5
same_archetype_new_trigger_family_count: 5
new_canonical_archetype_count: 0
new_fine_archetype_count: 4
new_trigger_family_count: 5
tested_existing_calibrated_axes:
  - stage2_actionable_evidence_bonus
  - stage3_green_revision_min
  - price_only_blowoff_blocks_positive_stage
  - full_4b_requires_non_price_evidence
residual_error_types_found:
  - current_profile_too_late_for_security_ops_retention
  - current_profile_false_positive_for_smallcap_event_premium
  - theme_headline_without_retention_bridge
new_axis_proposed:
  - c28_security_ops_retention_stage2_shadow_bonus
  - c28_identity_quantum_theme_guard
existing_axis_strengthened:
  - price_only_blowoff_blocks_positive_stage
  - full_4b_requires_non_price_evidence
existing_axis_weakened: null
existing_axis_kept:
  - stage3_green_total_min
  - stage3_green_revision_min
  - hard_4c_thesis_break_routes_to_4c
sector_specific_rule_candidate: true
canonical_archetype_rule_candidate: true
no_new_signal_reason: null
loop_contribution_label: canonical_archetype_rule_candidate
do_not_propose_new_weight_delta: false
diversity_score_summary: avg=24.6; five new C28 symbols, five new trigger families, zero same-symbol/same-trigger repeats
auto_selected_coverage_gap: C28 prior coverage concentrated in larger/representative software-security names; this loop adds security-ops, identity, quantum, and MSS event-premium residual paths.
```

## 23. Validation Scope / Non-Validation Scope

Validated in this MD:

```text
- Stock-web manifest fields and max_date.
- Stock-web raw/unadjusted price basis.
- Stock-web profile paths for each case.
- Entry date and close price from tradable shards.
- 30D/90D/180D MFE/MAE using observed tradable rows.
- Corporate-action 180D contamination screen using profile candidate dates.
- Same-entry trigger dedupe.
- Positive/counterexample balance.
- Current calibrated profile stress test.
```

Not validated in this MD:

```text
- live candidate suitability
- current market signal
- actual production scoring code
- stock_agent src/e2r implementation
- brokerage or auto-trading behavior
- definitive investment recommendation
- final primary-source legal/filing archive for every evidence sentence
```

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,c28_security_ops_retention_stage2_shadow_bonus,canonical_archetype_specific,L8_PLATFORM_CONTENT_SW_SECURITY,C28_SOFTWARE_SECURITY_CONTRACT_RETENTION,0,+3,+3,"Add Stage2/Yellow shadow credit only when evidence is retained security operations / SOC / SOAR / customer route, not headline-only theme","improved selection: keeps 067920/184230 positives while not promoting 042510/203650/356890","R13L54_C28_067920_STAGE2A_20210204|R13L54_C28_184230_STAGE2A_20210223",5,5,3,medium,archetype_shadow_only,"not production; post-calibrated residual"
shadow_weight,c28_identity_quantum_theme_guard,canonical_archetype_specific,L8_PLATFORM_CONTENT_SW_SECURITY,C28_SOFTWARE_SECURITY_CONTRACT_RETENTION,0,-4,-4,"Cap Stage2/3 when security theme is identity/DID/quantum/headline event without retained customer or revision bridge","reduced residual false positive on 042510/203650/356890","R13L54_C28_042510_STAGE2_BLOCKED_20220128|R13L54_C28_203650_STAGE2_BLOCKED_20230309|R13L54_C28_356890_STAGE2_BLOCKED_20230220",5,5,3,medium,archetype_shadow_only,"not production; post-calibrated residual"
shadow_weight,c28_price_only_event_premium_4b_overlay_guard,sector_specific,L8_PLATFORM_CONTENT_SW_SECURITY,C28_SOFTWARE_SECURITY_CONTRACT_RETENTION,true,true,0,"Keep full_4B_requires_non_price_evidence; price-only local spikes become overlay/watch, not full thesis exit without non-price evidence","prevents treating 203650/356890 local blowoffs as complete 4B unless non-price overheat appears","R13L54_C28_203650_4B_20230310|R13L54_C28_356890_4B_20230221",5,5,3,medium,existing_axis_strengthened,"not production; post-calibrated residual"

```

## 25. Machine-Readable Rows

### 25.1 price_source_validation

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
```

### 25.2 case rows

```jsonl
{"row_type":"case","case_id":"R13L54_C28_067920_IGLOO_SECURITY_OPS_2021","symbol":"067920","company_name":"이글루","round":"R13","loop":"54","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","fine_archetype_id":"SECURITY_OPERATIONS_SOAR_CONTRACT_RETENTION","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"R13L54_C28_067920_STAGE2A_20210204","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"Stage2 security-ops evidence preceded 90D/180D MFE; Green confirmation was later and left much of the move gone.","current_profile_verdict":"current_profile_too_late","price_source":"Songdaiki/stock-web","notes":"New C28 symbol. Security operations/SOAR-style contract retention route; not a reused AhnLab/Douzone/Wins/Genian case."}
{"row_type":"case","case_id":"R13L54_C28_184230_SGA_SOLUTIONS_2021","symbol":"184230","company_name":"SGA솔루션즈","round":"R13","loop":"54","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","fine_archetype_id":"SMALLCAP_SECURITY_INTEGRATION_EVENT_PREMIUM","case_type":"high_mae_success","positive_or_counterexample":"positive","best_trigger":"R13L54_C28_184230_STAGE2A_20210223","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"Strong MFE came with high MAE and later drawdown; useful positive but should carry execution/quality haircut.","current_profile_verdict":"current_profile_too_late","price_source":"Songdaiki/stock-web","notes":"New C28 symbol. Positive, but requires high-MAE guard; supports shadow promotion only when recurring/security contract evidence is present."}
{"row_type":"case","case_id":"R13L54_C28_042510_RAON_IDENTITY_2022","symbol":"042510","company_name":"라온시큐어","round":"R13","loop":"54","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","fine_archetype_id":"PUBLIC_AUTH_IDENTITY_SECURITY_THEME_GUARD","case_type":"failed_rerating","positive_or_counterexample":"counterexample","best_trigger":"R13L54_C28_042510_STAGE2_BLOCKED_20220128","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"Theme/policy identity-security evidence produced limited upside and deep 180D MAE; contract-retention bridge absent.","current_profile_verdict":"current_profile_correct","price_source":"Songdaiki/stock-web","notes":"New C28 symbol. Counterexample to using identity/DID/security theme alone as Stage2/3 promotion."}
{"row_type":"case","case_id":"R13L54_C28_203650_DREAM_QUANTUM_2023","symbol":"203650","company_name":"드림시큐리티","round":"R13","loop":"54","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","fine_archetype_id":"QUANTUM_SECURITY_THEME_CAP","case_type":"failed_rerating","positive_or_counterexample":"counterexample","best_trigger":"R13L54_C28_203650_STAGE2_BLOCKED_20230309","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"Quantum/security headline premium showed weak 90D/180D MFE and severe MAE; retention/revision bridge missing.","current_profile_verdict":"current_profile_correct","price_source":"Songdaiki/stock-web","notes":"New C28 symbol. Counterexample and 4B overlay sample."}
{"row_type":"case","case_id":"R13L54_C28_356890_CYBERONE_MSS_2023","symbol":"356890","company_name":"싸이버원","round":"R13","loop":"54","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","fine_archetype_id":"SMALLCAP_SECURITY_MSS_EVENT_PREMIUM_GUARD","case_type":"4B_too_early","positive_or_counterexample":"counterexample","best_trigger":"R13L54_C28_356890_STAGE2_BLOCKED_20230220","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"Event premium had large next-day spike but weak durable follow-through; better as 4B/event-premium guard than Stage3 promotion.","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"New C28 symbol. Counterexample to promoting small-cap security event spikes without customer/retention confirmation."}
```

### 25.3 trigger rows

```jsonl
{"round":"R13","loop":"54","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","sector":"platform_content_sw_security","primary_archetype":"software_security_contract_retention","loop_objective":"auto_coverage_gap_fill|sector_specific_rule_discovery|canonical_archetype_compression|counterexample_mining|4B_non_price_requirement_stress_test","price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","forward_window_trading_days":180,"calibration_block_reasons":[],"calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"row_type":"trigger","trigger_id":"R13L54_C28_067920_STAGE2A_20210204","case_id":"R13L54_C28_067920_IGLOO_SECURITY_OPS_2021","symbol":"067920","company_name":"이글루","fine_archetype_id":"SECURITY_OPERATIONS_SOAR_CONTRACT_RETENTION","trigger_type":"Stage2-Actionable","trigger_date":"2021-02-03","entry_date":"2021-02-04","entry_price":6040,"evidence_available_at_that_date":"SOC/SOAR-style security operations demand and public sector/security monitoring route visible; after-close timing uses next tradable close.","evidence_source":"historical_public_event_proxy_plus_stock_web_row; attach primary filing/news before production promotion","stage2_evidence_fields":["public_event_or_disclosure","customer_or_order_quality","backlog_or_delivery_visibility","relative_strength"],"stage3_evidence_fields":["multiple_public_sources"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"MFE_30D_pct":13.25,"MFE_90D_pct":47.52,"MFE_180D_pct":47.52,"MAE_30D_pct":-8.94,"MAE_90D_pct":-8.94,"MAE_180D_pct":-8.94,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2021-05-07","peak_price":8910,"drawdown_after_peak_pct":-26.6,"green_lateness_ratio":0.645,"trigger_outcome_label":"structural_success_high_late_green","current_profile_verdict":"current_profile_too_late","same_entry_group_id":"R13L54_C28_067920_20210204_6040","dedupe_for_aggregate":true,"aggregate_group_role":"representative","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/067/067920/2021.csv","profile_path":"atlas/symbol_profiles/067/067920.json","MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_1Y_pct":null,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":null,"four_b_evidence_type":[],"four_c_protection_label":null,"corporate_action_window_status":"clean_180D_window"}
{"round":"R13","loop":"54","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","sector":"platform_content_sw_security","primary_archetype":"software_security_contract_retention","loop_objective":"auto_coverage_gap_fill|sector_specific_rule_discovery|canonical_archetype_compression|counterexample_mining|4B_non_price_requirement_stress_test","price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","forward_window_trading_days":180,"calibration_block_reasons":[],"calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"row_type":"trigger","trigger_id":"R13L54_C28_067920_GREEN_20210507","case_id":"R13L54_C28_067920_IGLOO_SECURITY_OPS_2021","symbol":"067920","company_name":"이글루","fine_archetype_id":"SECURITY_OPERATIONS_SOAR_CONTRACT_RETENTION","trigger_type":"Stage3-Green","trigger_date":"2021-05-07","entry_date":"2021-05-07","entry_price":7890,"evidence_available_at_that_date":"Later confirmation-style label; useful only for lateness audit, not representative aggregate.","evidence_source":"historical_public_event_proxy_plus_stock_web_row","stage2_evidence_fields":[],"stage3_evidence_fields":["confirmed_revision","financial_visibility","multiple_public_sources"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"MFE_30D_pct":12.93,"MFE_90D_pct":12.93,"MFE_180D_pct":12.93,"MAE_30D_pct":-8.87,"MAE_90D_pct":-17.11,"MAE_180D_pct":-17.11,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2021-05-07","peak_price":8910,"drawdown_after_peak_pct":-26.6,"green_lateness_ratio":0.645,"trigger_outcome_label":"late_green_label_comparison","current_profile_verdict":"current_profile_too_late","same_entry_group_id":"R13L54_C28_067920_20210507_7890","dedupe_for_aggregate":false,"aggregate_group_role":"label_comparison_only","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/067/067920/2021.csv","profile_path":"atlas/symbol_profiles/067/067920.json","MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_1Y_pct":null,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":null,"four_b_evidence_type":[],"four_c_protection_label":null,"corporate_action_window_status":"clean_180D_window"}
{"round":"R13","loop":"54","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","sector":"platform_content_sw_security","primary_archetype":"software_security_contract_retention","loop_objective":"auto_coverage_gap_fill|sector_specific_rule_discovery|canonical_archetype_compression|counterexample_mining|4B_non_price_requirement_stress_test","price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","forward_window_trading_days":180,"calibration_block_reasons":[],"calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"row_type":"trigger","trigger_id":"R13L54_C28_184230_STAGE2A_20210223","case_id":"R13L54_C28_184230_SGA_SOLUTIONS_2021","symbol":"184230","company_name":"SGA솔루션즈","fine_archetype_id":"SMALLCAP_SECURITY_INTEGRATION_EVENT_PREMIUM","trigger_type":"Stage2-Actionable","trigger_date":"2021-02-22","entry_date":"2021-02-23","entry_price":1235,"evidence_available_at_that_date":"Security integration/solution route and event-driven demand visible; next-day close used for uncertain timing.","evidence_source":"historical_public_event_proxy_plus_stock_web_row; attach primary filing/news before production promotion","stage2_evidence_fields":["public_event_or_disclosure","relative_strength","customer_or_order_quality"],"stage3_evidence_fields":["multiple_public_sources"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"MFE_30D_pct":33.6,"MFE_90D_pct":83.0,"MFE_180D_pct":83.0,"MAE_30D_pct":-10.12,"MAE_90D_pct":-10.12,"MAE_180D_pct":-11.34,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2021-06-17","peak_price":2260,"drawdown_after_peak_pct":-51.55,"green_lateness_ratio":null,"trigger_outcome_label":"high_mae_success","current_profile_verdict":"current_profile_too_late","same_entry_group_id":"R13L54_C28_184230_20210223_1235","dedupe_for_aggregate":true,"aggregate_group_role":"representative","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/184/184230/2021.csv","profile_path":"atlas/symbol_profiles/184/184230.json","MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_1Y_pct":null,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":null,"four_b_evidence_type":[],"four_c_protection_label":null,"corporate_action_window_status":"clean_180D_window"}
{"round":"R13","loop":"54","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","sector":"platform_content_sw_security","primary_archetype":"software_security_contract_retention","loop_objective":"auto_coverage_gap_fill|sector_specific_rule_discovery|canonical_archetype_compression|counterexample_mining|4B_non_price_requirement_stress_test","price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","forward_window_trading_days":180,"calibration_block_reasons":[],"calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"row_type":"trigger","trigger_id":"R13L54_C28_184230_4B_20210617","case_id":"R13L54_C28_184230_SGA_SOLUTIONS_2021","symbol":"184230","company_name":"SGA솔루션즈","fine_archetype_id":"SMALLCAP_SECURITY_INTEGRATION_EVENT_PREMIUM","trigger_type":"Stage4B","trigger_date":"2021-06-17","entry_date":"2021-06-17","entry_price":2065,"evidence_available_at_that_date":"Large price/volume event near full observed peak; overlay only because non-price overheat evidence is incomplete.","evidence_source":"stock_web_price_event_proxy; non-price 4B evidence incomplete","stage2_evidence_fields":[],"stage3_evidence_fields":[],"stage4b_evidence_fields":["price_only_local_peak","positioning_overheat"],"stage4c_evidence_fields":[],"MFE_30D_pct":9.44,"MFE_90D_pct":9.44,"MFE_180D_pct":9.44,"MAE_30D_pct":-23.24,"MAE_90D_pct":-31.23,"MAE_180D_pct":-46.97,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2021-06-17","peak_price":2260,"drawdown_after_peak_pct":-51.55,"four_b_local_peak_proximity":0.81,"four_b_full_window_peak_proximity":0.81,"four_b_timing_verdict":"good_price_peak_but_not_full_4B_without_non_price_evidence","four_b_evidence_type":["price_only","positioning_overheat"],"trigger_outcome_label":"4B_overlay_success_price_only_needs_non_price_confirmation","current_profile_verdict":"current_profile_4B_too_early","same_entry_group_id":"R13L54_C28_184230_20210617_2065","dedupe_for_aggregate":false,"aggregate_group_role":"4B_overlay_only","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/184/184230/2021.csv","profile_path":"atlas/symbol_profiles/184/184230.json","MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_1Y_pct":null,"green_lateness_ratio":null,"four_c_protection_label":null,"corporate_action_window_status":"clean_180D_window"}
{"round":"R13","loop":"54","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","sector":"platform_content_sw_security","primary_archetype":"software_security_contract_retention","loop_objective":"auto_coverage_gap_fill|sector_specific_rule_discovery|canonical_archetype_compression|counterexample_mining|4B_non_price_requirement_stress_test","price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","forward_window_trading_days":180,"calibration_block_reasons":[],"calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"row_type":"trigger","trigger_id":"R13L54_C28_042510_STAGE2_BLOCKED_20220128","case_id":"R13L54_C28_042510_RAON_IDENTITY_2022","symbol":"042510","company_name":"라온시큐어","fine_archetype_id":"PUBLIC_AUTH_IDENTITY_SECURITY_THEME_GUARD","trigger_type":"Stage2-Blocked","trigger_date":"2022-01-27","entry_date":"2022-01-28","entry_price":3395,"evidence_available_at_that_date":"Identity/DID/security theme without clear recurring contract-retention or revision bridge.","evidence_source":"historical_public_event_proxy_plus_stock_web_row","stage2_evidence_fields":["public_event_or_disclosure","policy_or_regulatory_optionality","relative_strength"],"stage3_evidence_fields":[],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"MFE_30D_pct":21.8,"MFE_90D_pct":21.8,"MFE_180D_pct":21.8,"MAE_30D_pct":-5.15,"MAE_90D_pct":-16.35,"MAE_180D_pct":-39.03,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2022-03-16","peak_price":4135,"drawdown_after_peak_pct":-49.94,"trigger_outcome_label":"failed_rerating_theme_guard_worked","current_profile_verdict":"current_profile_correct","same_entry_group_id":"R13L54_C28_042510_20220128_3395","dedupe_for_aggregate":true,"aggregate_group_role":"representative","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/042/042510/2022.csv","profile_path":"atlas/symbol_profiles/042/042510.json","MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_1Y_pct":null,"green_lateness_ratio":null,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":null,"four_b_evidence_type":[],"four_c_protection_label":null,"corporate_action_window_status":"clean_180D_window"}
{"round":"R13","loop":"54","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","sector":"platform_content_sw_security","primary_archetype":"software_security_contract_retention","loop_objective":"auto_coverage_gap_fill|sector_specific_rule_discovery|canonical_archetype_compression|counterexample_mining|4B_non_price_requirement_stress_test","price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","forward_window_trading_days":180,"calibration_block_reasons":[],"calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"row_type":"trigger","trigger_id":"R13L54_C28_042510_4C_20221013","case_id":"R13L54_C28_042510_RAON_IDENTITY_2022","symbol":"042510","company_name":"라온시큐어","fine_archetype_id":"PUBLIC_AUTH_IDENTITY_SECURITY_THEME_GUARD","trigger_type":"Stage4C","trigger_date":"2022-10-13","entry_date":"2022-10-13","entry_price":2105,"evidence_available_at_that_date":"Thesis broken by persistent drawdown and absence of retained-contract/revision bridge; protection came late.","evidence_source":"stock_web_price_path_plus_absent_contract_retention_proxy","stage2_evidence_fields":[],"stage3_evidence_fields":[],"stage4b_evidence_fields":["margin_or_backlog_slowdown"],"stage4c_evidence_fields":["thesis_evidence_broken"],"MFE_30D_pct":27.08,"MFE_90D_pct":27.08,"MFE_180D_pct":27.08,"MAE_30D_pct":-1.66,"MAE_90D_pct":-1.66,"MAE_180D_pct":-1.66,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2022-10-26","peak_price":2680,"drawdown_after_peak_pct":-10.07,"four_c_protection_label":"hard_4c_late","trigger_outcome_label":"4C_late","current_profile_verdict":"current_profile_4C_too_late","same_entry_group_id":"R13L54_C28_042510_20221013_2105","dedupe_for_aggregate":false,"aggregate_group_role":"4C_overlay_only","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/042/042510/2022.csv","profile_path":"atlas/symbol_profiles/042/042510.json","MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_1Y_pct":null,"green_lateness_ratio":null,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":null,"four_b_evidence_type":[],"corporate_action_window_status":"clean_180D_window"}
{"round":"R13","loop":"54","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","sector":"platform_content_sw_security","primary_archetype":"software_security_contract_retention","loop_objective":"auto_coverage_gap_fill|sector_specific_rule_discovery|canonical_archetype_compression|counterexample_mining|4B_non_price_requirement_stress_test","price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","forward_window_trading_days":180,"calibration_block_reasons":[],"calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"row_type":"trigger","trigger_id":"R13L54_C28_203650_STAGE2_BLOCKED_20230309","case_id":"R13L54_C28_203650_DREAM_QUANTUM_2023","symbol":"203650","company_name":"드림시큐리티","fine_archetype_id":"QUANTUM_SECURITY_THEME_CAP","trigger_type":"Stage2-Blocked","trigger_date":"2023-03-09","entry_date":"2023-03-09","entry_price":3740,"evidence_available_at_that_date":"Quantum/security headline premium without visible customer-retention or revision bridge.","evidence_source":"historical_public_event_proxy_plus_stock_web_row","stage2_evidence_fields":["public_event_or_disclosure","policy_or_regulatory_optionality","relative_strength"],"stage3_evidence_fields":[],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"MFE_30D_pct":9.63,"MFE_90D_pct":9.63,"MFE_180D_pct":9.63,"MAE_30D_pct":-17.25,"MAE_90D_pct":-24.06,"MAE_180D_pct":-24.06,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2023-03-10","peak_price":4100,"drawdown_after_peak_pct":-26.22,"trigger_outcome_label":"failed_rerating_quantum_theme_guard","current_profile_verdict":"current_profile_correct","same_entry_group_id":"R13L54_C28_203650_20230309_3740","dedupe_for_aggregate":true,"aggregate_group_role":"representative","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/203/203650/2023.csv","profile_path":"atlas/symbol_profiles/203/203650.json","MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_1Y_pct":null,"green_lateness_ratio":null,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":null,"four_b_evidence_type":[],"four_c_protection_label":null,"corporate_action_window_status":"clean_180D_window"}
{"round":"R13","loop":"54","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","sector":"platform_content_sw_security","primary_archetype":"software_security_contract_retention","loop_objective":"auto_coverage_gap_fill|sector_specific_rule_discovery|canonical_archetype_compression|counterexample_mining|4B_non_price_requirement_stress_test","price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","forward_window_trading_days":180,"calibration_block_reasons":[],"calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"row_type":"trigger","trigger_id":"R13L54_C28_203650_4B_20230310","case_id":"R13L54_C28_203650_DREAM_QUANTUM_2023","symbol":"203650","company_name":"드림시큐리티","fine_archetype_id":"QUANTUM_SECURITY_THEME_CAP","trigger_type":"Stage4B","trigger_date":"2023-03-10","entry_date":"2023-03-10","entry_price":3790,"evidence_available_at_that_date":"Local price spike only; no full 4B without non-price evidence.","evidence_source":"stock_web_price_event_proxy","stage2_evidence_fields":[],"stage3_evidence_fields":[],"stage4b_evidence_fields":["price_only_local_peak"],"stage4c_evidence_fields":[],"MFE_30D_pct":8.18,"MFE_90D_pct":8.18,"MFE_180D_pct":8.18,"MAE_30D_pct":-18.34,"MAE_90D_pct":-25.07,"MAE_180D_pct":-25.07,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2023-03-10","peak_price":4100,"drawdown_after_peak_pct":-26.22,"four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":0.139,"four_b_timing_verdict":"price_only_local_4B_too_early","four_b_evidence_type":["price_only"],"trigger_outcome_label":"4B_too_early_without_non_price_evidence","current_profile_verdict":"current_profile_4B_too_early","same_entry_group_id":"R13L54_C28_203650_20230310_3790","dedupe_for_aggregate":false,"aggregate_group_role":"4B_overlay_only","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/203/203650/2023.csv","profile_path":"atlas/symbol_profiles/203/203650.json","MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_1Y_pct":null,"green_lateness_ratio":null,"four_c_protection_label":null,"corporate_action_window_status":"clean_180D_window"}
{"round":"R13","loop":"54","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","sector":"platform_content_sw_security","primary_archetype":"software_security_contract_retention","loop_objective":"auto_coverage_gap_fill|sector_specific_rule_discovery|canonical_archetype_compression|counterexample_mining|4B_non_price_requirement_stress_test","price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","forward_window_trading_days":180,"calibration_block_reasons":[],"calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"row_type":"trigger","trigger_id":"R13L54_C28_356890_STAGE2_BLOCKED_20230220","case_id":"R13L54_C28_356890_CYBERONE_MSS_2023","symbol":"356890","company_name":"싸이버원","fine_archetype_id":"SMALLCAP_SECURITY_MSS_EVENT_PREMIUM_GUARD","trigger_type":"Stage2-Blocked","trigger_date":"2023-02-20","entry_date":"2023-02-20","entry_price":10890,"evidence_available_at_that_date":"Small-cap security event premium; contract-retention/customer confirmation incomplete.","evidence_source":"historical_public_event_proxy_plus_stock_web_row","stage2_evidence_fields":["public_event_or_disclosure","relative_strength"],"stage3_evidence_fields":[],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"MFE_30D_pct":29.94,"MFE_90D_pct":29.94,"MFE_180D_pct":29.94,"MAE_30D_pct":-7.25,"MAE_90D_pct":-13.22,"MAE_180D_pct":-17.91,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2023-02-21","peak_price":14150,"drawdown_after_peak_pct":-36.82,"trigger_outcome_label":"event_premium_not_structural_stage3","current_profile_verdict":"current_profile_false_positive","same_entry_group_id":"R13L54_C28_356890_20230220_10890","dedupe_for_aggregate":true,"aggregate_group_role":"representative","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/356/356890/2023.csv","profile_path":"atlas/symbol_profiles/356/356890.json","MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_1Y_pct":null,"green_lateness_ratio":null,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":null,"four_b_evidence_type":[],"four_c_protection_label":null,"corporate_action_window_status":"clean_180D_window"}
{"round":"R13","loop":"54","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","sector":"platform_content_sw_security","primary_archetype":"software_security_contract_retention","loop_objective":"auto_coverage_gap_fill|sector_specific_rule_discovery|canonical_archetype_compression|counterexample_mining|4B_non_price_requirement_stress_test","price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","forward_window_trading_days":180,"calibration_block_reasons":[],"calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"row_type":"trigger","trigger_id":"R13L54_C28_356890_4B_20230221","case_id":"R13L54_C28_356890_CYBERONE_MSS_2023","symbol":"356890","company_name":"싸이버원","fine_archetype_id":"SMALLCAP_SECURITY_MSS_EVENT_PREMIUM_GUARD","trigger_type":"Stage4B","trigger_date":"2023-02-21","entry_date":"2023-02-21","entry_price":13130,"evidence_available_at_that_date":"Next-day blowoff near full observed peak; overlay only because non-price overheat evidence absent.","evidence_source":"stock_web_price_event_proxy","stage2_evidence_fields":[],"stage3_evidence_fields":[],"stage4b_evidence_fields":["price_only_local_peak","positioning_overheat"],"stage4c_evidence_fields":[],"MFE_30D_pct":7.77,"MFE_90D_pct":7.77,"MFE_180D_pct":7.77,"MAE_30D_pct":-24.9,"MAE_90D_pct":-26.88,"MAE_180D_pct":-31.91,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2023-02-21","peak_price":14150,"drawdown_after_peak_pct":-36.82,"four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":0.687,"four_b_timing_verdict":"price_only_local_4B_not_full_without_non_price_evidence","four_b_evidence_type":["price_only","positioning_overheat"],"trigger_outcome_label":"4B_overlay_success_but_price_only","current_profile_verdict":"current_profile_4B_too_early","same_entry_group_id":"R13L54_C28_356890_20230221_13130","dedupe_for_aggregate":false,"aggregate_group_role":"4B_overlay_only","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/356/356890/2023.csv","profile_path":"atlas/symbol_profiles/356/356890.json","MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_1Y_pct":null,"green_lateness_ratio":null,"four_c_protection_label":null,"corporate_action_window_status":"clean_180D_window"}
```

### 25.4 score_simulation rows

```jsonl
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R13L54_C28_067920_IGLOO_SECURITY_OPS_2021","trigger_id":"R13L54_C28_067920_STAGE2A_20210204","symbol":"067920","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","raw_component_scores_before":{"contract_score":12,"backlog_visibility_score":7,"margin_bridge_score":4,"revision_score":5,"relative_strength_score":9,"customer_quality_score":7,"policy_or_regulatory_score":4,"valuation_repricing_score":4,"execution_risk_score":-1,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":74.5,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"contract_score":14,"backlog_visibility_score":8,"margin_bridge_score":4,"revision_score":5,"relative_strength_score":9,"customer_quality_score":9,"policy_or_regulatory_score":4,"valuation_repricing_score":4,"execution_risk_score":-1,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":79.5,"stage_label_after":"Stage3-Yellow-shadow","changed_components":["contract_score","customer_quality_score","backlog_visibility_score"],"component_delta_explanation":"C28 security-ops route gets shadow credit only when non-price evidence implies retained SOC/SOAR/customer operation, not headline-only security theme.","MFE_90D_pct":47.52,"MAE_90D_pct":-8.94,"score_return_alignment_label":"aligned_after_shadow","current_profile_verdict":"current_profile_too_late"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R13L54_C28_184230_SGA_SOLUTIONS_2021","trigger_id":"R13L54_C28_184230_STAGE2A_20210223","symbol":"184230","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","raw_component_scores_before":{"contract_score":7,"backlog_visibility_score":3,"margin_bridge_score":2,"revision_score":2,"relative_strength_score":13,"customer_quality_score":4,"policy_or_regulatory_score":5,"valuation_repricing_score":6,"execution_risk_score":-2,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":-2,"accounting_trust_risk_score":0},"weighted_score_before":70.0,"stage_label_before":"Stage2-watch","raw_component_scores_after":{"contract_score":9,"backlog_visibility_score":4,"margin_bridge_score":2,"revision_score":2,"relative_strength_score":13,"customer_quality_score":5,"policy_or_regulatory_score":5,"valuation_repricing_score":6,"execution_risk_score":-3,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":-2,"accounting_trust_risk_score":0},"weighted_score_after":74.0,"stage_label_after":"Stage2-Actionable-shadow-high-MAE-guard","changed_components":["contract_score","backlog_visibility_score","execution_risk_score"],"component_delta_explanation":"Positive MFE is accepted but high MAE and later drawdown keep this below Green unless retention/revision evidence improves.","MFE_90D_pct":83.0,"MAE_90D_pct":-10.12,"score_return_alignment_label":"aligned_with_high_mae_guard","current_profile_verdict":"current_profile_too_late"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R13L54_C28_042510_RAON_IDENTITY_2022","trigger_id":"R13L54_C28_042510_STAGE2_BLOCKED_20220128","symbol":"042510","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","raw_component_scores_before":{"contract_score":3,"backlog_visibility_score":1,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":8,"customer_quality_score":2,"policy_or_regulatory_score":9,"valuation_repricing_score":7,"execution_risk_score":-2,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":69.0,"stage_label_before":"Stage2-watch","raw_component_scores_after":{"contract_score":2,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":8,"customer_quality_score":1,"policy_or_regulatory_score":5,"valuation_repricing_score":5,"execution_risk_score":-5,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":61.0,"stage_label_after":"Stage2-blocked-theme-guard","changed_components":["policy_or_regulatory_score","contract_score","execution_risk_score","customer_quality_score"],"component_delta_explanation":"Identity/DID policy theme is capped without retained-contract, customer, or revision bridge.","MFE_90D_pct":21.8,"MAE_90D_pct":-16.35,"score_return_alignment_label":"aligned_block","current_profile_verdict":"current_profile_correct"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R13L54_C28_203650_DREAM_QUANTUM_2023","trigger_id":"R13L54_C28_203650_STAGE2_BLOCKED_20230309","symbol":"203650","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","raw_component_scores_before":{"contract_score":2,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":9,"customer_quality_score":1,"policy_or_regulatory_score":8,"valuation_repricing_score":7,"execution_risk_score":-2,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":68.0,"stage_label_before":"Stage2-watch","raw_component_scores_after":{"contract_score":1,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":9,"customer_quality_score":0,"policy_or_regulatory_score":4,"valuation_repricing_score":5,"execution_risk_score":-5,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":59.0,"stage_label_after":"Stage2-blocked-quantum-theme-guard","changed_components":["policy_or_regulatory_score","contract_score","customer_quality_score","execution_risk_score"],"component_delta_explanation":"Quantum/security headline premium is not sufficient for C28 promotion without retained contract/customer conversion.","MFE_90D_pct":9.63,"MAE_90D_pct":-24.06,"score_return_alignment_label":"aligned_block","current_profile_verdict":"current_profile_correct"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R13L54_C28_356890_CYBERONE_MSS_2023","trigger_id":"R13L54_C28_356890_STAGE2_BLOCKED_20230220","symbol":"356890","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","raw_component_scores_before":{"contract_score":5,"backlog_visibility_score":2,"margin_bridge_score":1,"revision_score":0,"relative_strength_score":10,"customer_quality_score":5,"policy_or_regulatory_score":5,"valuation_repricing_score":6,"execution_risk_score":-2,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":72.0,"stage_label_before":"Stage2-watch/possible-false-positive","raw_component_scores_after":{"contract_score":4,"backlog_visibility_score":1,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":10,"customer_quality_score":3,"policy_or_regulatory_score":4,"valuation_repricing_score":4,"execution_risk_score":-5,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":65.0,"stage_label_after":"Stage2-blocked-event-premium-guard","changed_components":["contract_score","customer_quality_score","execution_risk_score","valuation_repricing_score"],"component_delta_explanation":"Small-cap MSS/security spike is treated as event premium unless contract retention and repeat revenue confirmation are present.","MFE_90D_pct":29.94,"MAE_90D_pct":-13.22,"score_return_alignment_label":"block_or_watch_only_prevents_false_green","current_profile_verdict":"current_profile_false_positive"}
```

### 25.5 shadow_weight rows

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,c28_security_ops_retention_stage2_shadow_bonus,canonical_archetype_specific,L8_PLATFORM_CONTENT_SW_SECURITY,C28_SOFTWARE_SECURITY_CONTRACT_RETENTION,0,+3,+3,"Add Stage2/Yellow shadow credit only when evidence is retained security operations / SOC / SOAR / customer route, not headline-only theme","improved selection: keeps 067920/184230 positives while not promoting 042510/203650/356890","R13L54_C28_067920_STAGE2A_20210204|R13L54_C28_184230_STAGE2A_20210223",5,5,3,medium,archetype_shadow_only,"not production; post-calibrated residual"
shadow_weight,c28_identity_quantum_theme_guard,canonical_archetype_specific,L8_PLATFORM_CONTENT_SW_SECURITY,C28_SOFTWARE_SECURITY_CONTRACT_RETENTION,0,-4,-4,"Cap Stage2/3 when security theme is identity/DID/quantum/headline event without retained customer or revision bridge","reduced residual false positive on 042510/203650/356890","R13L54_C28_042510_STAGE2_BLOCKED_20220128|R13L54_C28_203650_STAGE2_BLOCKED_20230309|R13L54_C28_356890_STAGE2_BLOCKED_20230220",5,5,3,medium,archetype_shadow_only,"not production; post-calibrated residual"
shadow_weight,c28_price_only_event_premium_4b_overlay_guard,sector_specific,L8_PLATFORM_CONTENT_SW_SECURITY,C28_SOFTWARE_SECURITY_CONTRACT_RETENTION,true,true,0,"Keep full_4B_requires_non_price_evidence; price-only local spikes become overlay/watch, not full thesis exit without non-price evidence","prevents treating 203650/356890 local blowoffs as complete 4B unless non-price overheat appears","R13L54_C28_203650_4B_20230310|R13L54_C28_356890_4B_20230221",5,5,3,medium,existing_axis_strengthened,"not production; post-calibrated residual"

```

### 25.6 residual_contribution row

```jsonl
{"row_type":"residual_contribution","round":"R13","loop":"54","large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","new_independent_case_count":5,"reused_case_count":0,"new_symbol_count":5,"same_archetype_new_symbol_count":5,"same_archetype_new_trigger_family_count":5,"new_canonical_archetype_count":0,"new_trigger_family_count":5,"tested_existing_calibrated_axes":["stage2_actionable_evidence_bonus","stage3_green_revision_min","price_only_blowoff_blocks_positive_stage","full_4b_requires_non_price_evidence"],"residual_error_types_found":["current_profile_too_late_for_security_ops_retention","current_profile_false_positive_for_smallcap_event_premium","theme_headline_without_retention_bridge"],"loop_contribution_label":"canonical_archetype_rule_candidate","do_not_propose_new_weight_delta":false,"diversity_score_summary":"avg=24.6; five new C28 symbols, five new trigger families, zero same-symbol/same-trigger repeats","auto_selected_coverage_gap":"C28 prior coverage concentrated in Douzone/AhnLab/Wins/Genian/Rsupport/Hancom-like names; this loop adds smaller security-ops, identity, quantum, and MSS event-premium paths."}
```

### 25.7 narrative_only rows

```jsonl
{"row_type":"narrative_only","case_id":"none","symbol":null,"large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C28_SOFTWARE_SECURITY_CONTRACT_RETENTION","reason":"no narrative-only cases in this loop; all representative cases had usable 180D stock-web windows","price_source":"Songdaiki/stock-web","usage":"not_weight_calibration"}
```

## 26. Deferred Coding Agent Handoff Prompt

### Purpose

You are now in the repository implementation phase. The attached Markdown files are v12 post-calibrated residual research outputs produced using the Songdaiki/stock-web OHLC atlas.

These MDs are not live candidate research. They are historical calibration research designed to extend the already-applied e2r_2_1_stock_web_calibrated profile.

Do not blindly apply every shadow row.
Ingest the machine-readable rows and update the sector/canonical-archetype calibration ledger.

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

```text
next_round = R13_loop_55
suggested_large_sector_id = L8_PLATFORM_CONTENT_SW_SECURITY
suggested_canonical_archetype_id = C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE
suggested_objective = holdout_validation + counterexample_mining
reason = C28 now has additional same-archetype diversity; L8 still needs platform/ad operating leverage residual calibration beyond software-security.
```

## 28. Source Notes

Primary price atlas:

```text
source = Songdaiki/stock-web
repository = https://github.com/Songdaiki/stock-web
manifest = atlas/manifest.json
schema = atlas/schema.json
universe = atlas/universe/all_symbols.csv
calibration_shard_root = atlas/ohlcv_tradable_by_symbol_year
raw_shard_root = atlas/ohlcv_raw_by_symbol_year
price_basis = tradable_raw
price_adjustment_status = raw_unadjusted_marcap
stock_web_manifest_max_date = 2026-02-20
```

Stock-web files inspected:

```text
atlas/manifest.json
atlas/symbol_profiles/067/067920.json
atlas/ohlcv_tradable_by_symbol_year/067/067920/2021.csv
atlas/symbol_profiles/184/184230.json
atlas/ohlcv_tradable_by_symbol_year/184/184230/2021.csv
atlas/symbol_profiles/042/042510.json
atlas/ohlcv_tradable_by_symbol_year/042/042510/2022.csv
atlas/symbol_profiles/203/203650.json
atlas/ohlcv_tradable_by_symbol_year/203/203650/2023.csv
atlas/symbol_profiles/356/356890.json
atlas/ohlcv_tradable_by_symbol_year/356/356890/2023.csv
```

Data caveat:

```text
All OHLCV rows are raw/unadjusted marcap data. Corporate-action windows are blocked by default. This loop uses 180D clean windows only for quantitative representative aggregation.
```
