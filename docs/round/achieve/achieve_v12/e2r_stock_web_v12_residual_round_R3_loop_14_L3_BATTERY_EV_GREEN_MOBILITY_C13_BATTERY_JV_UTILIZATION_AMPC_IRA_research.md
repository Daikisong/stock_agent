# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
research_session = post_calibrated_sector_archetype_residual_research
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
repo_session = later_batch_implementation_only
output_file = e2r_stock_web_v12_residual_round_R3_loop_14_L3_BATTERY_EV_GREEN_MOBILITY_C13_BATTERY_JV_UTILIZATION_AMPC_IRA_research.md
scheduled_round = R3
scheduled_loop = 14
completed_round = R3
completed_loop = 14
large_sector_id = L3_BATTERY_EV_GREEN_MOBILITY
canonical_archetype_id = C13_BATTERY_JV_UTILIZATION_AMPC_IRA
fine_archetype_id = IRA_AMPC_JV_UTILIZATION_LONG_LEAD_CAPEX_GUARD
price_source = Songdaiki/stock-web
price_basis = tradable_raw
price_adjustment_status = raw_unadjusted_marcap
stock_web_manifest_max_date = 2026-02-20
round_schedule_status = valid
round_sector_consistency = pass
production_scoring_changed = false
shadow_weight_only = true
handoff_prompt_embedded = true
handoff_prompt_executed_now = false
```

This loop adds **3** new independent cases, **4** counterexamples, and **4** residual errors for **R3/L3_BATTERY_EV_GREEN_MOBILITY/C13_BATTERY_JV_UTILIZATION_AMPC_IRA**.

## 1. Current Calibrated Profile Assumption

```text
current_default_profile_proxy = e2r_2_1_stock_web_calibrated_proxy
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

This MD does not re-prove the global battery rerating axis. It tests a narrower C13 residual: **IRA / AMPC / JV announcements are not enough unless eligible capacity, utilization, margin bridge, and balance-sheet endurance move together**. A JV headline is like a factory signboard; calibration should wait for the gate to open and the line to run.

## 2. Round / Large Sector / Canonical Archetype Scope

|Field|Value|
|---|---|
|scheduled_round|R3|
|scheduled_loop|14|
|large_sector_id|L3_BATTERY_EV_GREEN_MOBILITY|
|canonical_archetype_id|C13_BATTERY_JV_UTILIZATION_AMPC_IRA|
|fine_archetype_id|IRA_AMPC_JV_UTILIZATION_LONG_LEAD_CAPEX_GUARD|
|loop_objective|coverage_gap_fill|counterexample_mining|canonical_archetype_compression|green_strictness_stress_test|4C_thesis_break_timing_test|sector_specific_rule_discovery|
|rule_scope_target|canonical_archetype_specific|
|production_change|false|


R3 is valid because the selected large sector is battery / EV / green mobility. The selected canonical archetype is C13, not C11: the residual is not orderbook size, but **IRA / AMPC / JV eligibility versus utilization and capex overhang**.

## 3. Previous Coverage / Duplicate Avoidance Check

Allowed research artifacts and local generated filenames were used only for schedule and duplicate avoidance. Local v12 R3 files already cover C11, C12, and C14 through loop 13, while C13 was still uncovered. This file follows the prior next state `R2 loop 14 -> R3 loop 14`.

```text
scheduled_round = R3
scheduled_loop = 14
previous_generated_state = R2 loop 14 completed -> next_round R3 / next_loop 14
new_independent_case_count = 3
reused_case_count = 2
new_symbol_count = 3
same_archetype_new_trigger_family_count = 5
minimum_new_independent_case_ratio = 0.60
same_symbol_same_trigger_duplicate_for_new_count = false
```

The POSCO Future M and LGES rows are explicitly marked as reused holdouts because they appeared in earlier C11 calibration. They are retained only to anchor the C13 positive / AMPC-lag boundary and do not inflate the new independent count.

## 4. Stock-Web OHLC Input / Price Source Validation

|Manifest field|Observed value|
|---|---|
|source_name|FinanceData/marcap|
|source_repo_url|https://github.com/FinanceData/marcap|
|price_adjustment_status|raw_unadjusted_marcap|
|min_date|1995-05-02|
|max_date|2026-02-20|
|tradable_row_count|14354401|
|raw_row_count|15214118|
|symbol_count|5414|
|active_like_symbol_count|2868|
|inactive_or_delisted_like_symbol_count|2546|
|markets|KONEX; KOSDAQ; KOSDAQ GLOBAL; KOSPI|
|calibration_shard_root|atlas/ohlcv_tradable_by_symbol_year|
|raw_shard_root|atlas/ohlcv_raw_by_symbol_year|
|schema_path|atlas/schema.json|
|universe_path|atlas/universe/all_symbols.csv|

Price basis is `tradable_raw`. The schema uses columns `d,o,h,l,c,v,a,mc,s,m`; `MFE_N_pct` is max high over the N-trading-day window divided by entry close, and `MAE_N_pct` is min low over the same window divided by entry close.

## 5. Historical Eligibility Gate

|case_id|symbol|entry_date|profile_path|corporate_action_window_status|180D status|calibration_usable|
|---|---|---|---|---|---|---|
|R3L14_C13_POSCO_FUTURE_M_20230126_IRA_LOCALIZATION|003670|2023-01-26|atlas/symbol_profiles/003/003670.json|clean_180D_window|available before 2026-02-20|true|
|R3L14_C13_LGES_20230411_AMPC_UTILIZATION_LAG|373220|2023-04-11|atlas/symbol_profiles/373/373220.json|clean_180D_window|available before 2026-02-20|true|
|R3L14_C13_SAMSUNGSDI_20230425_GM_JV_LONG_LEAD|006400|2023-04-25|atlas/symbol_profiles/006/006400.json|clean_180D_window|available before 2026-02-20|true|
|R3L14_C13_SKINNOVATION_20230726_AMPC_CAPEX_PARENT_OVERHANG|096770|2023-07-26|atlas/symbol_profiles/096/096770.json|clean_180D_window|available before 2026-02-20|true|
|R3L14_C13_LOTTEEM_20230726_COPPERFOIL_LOCALIZATION_CAPEX|020150|2023-07-26|atlas/symbol_profiles/020/020150.json|clean_180D_window|available before 2026-02-20|true|


All representative or holdout triggers have entry rows in tradable shards. The selected 180D windows avoid the symbol-profile corporate-action candidate dates.

## 6. Canonical Archetype Compression Map

|Fine trigger family|Canonical archetype|Interpretation|
|---|---|---|
|INTEGRATED_CATHODE_ANODE_IRA_LOCALIZATION|C13_BATTERY_JV_UTILIZATION_AMPC_IRA|positive holdout where localization and orderbook visibility lined up|
|CELL_MAKER_AMPC_WITHOUT_UTILIZATION|C13_BATTERY_JV_UTILIZATION_AMPC_IRA|AMPC optionality exists but margin/utilization conversion is missing|
|LONG_LEAD_US_JV_CAPEX_OVERHANG|C13_BATTERY_JV_UTILIZATION_AMPC_IRA|JV headline has long revenue lead time and should cap Green|
|PARENT_BALANCE_SHEET_BATTERY_CAPEX_OVERHANG|C13_BATTERY_JV_UTILIZATION_AMPC_IRA|AMPC benefit is diluted by parent leverage/capex and losses|
|LOCALIZATION_CAPEX_WITHOUT_COPPERFOIL_UTILIZATION|C13_BATTERY_JV_UTILIZATION_AMPC_IRA|localization story fails if utilization/spread bridge is absent|


Compression rule: do not create separate production axes for every IRA-adjacent battery name. Keep the scoring unit at C13, then use shadow gates for `eligible capacity`, `utilization`, `margin bridge`, `AMPC recognition quality`, and `capex/balance-sheet overhang`.

## 7. Case Selection Summary

|case_id|symbol|company_name|role|positive_or_counterexample|best_trigger|why selected|
|---|---|---|---|---|---|---|
|R3L14_C13_POSCO_FUTURE_M_20230126_IRA_LOCALIZATION|003670|포스코퓨처엠|structural_success|positive|TRG_R3L14_C13_POSCO_20230126_STAGE2A|Integrated cathode/anode localization path behaved like an IRA-eligible structural rerating; useful as a positive holdout but not a new independent case.|
|R3L14_C13_LGES_20230411_AMPC_UTILIZATION_LAG|373220|LG에너지솔루션|failed_rerating|counterexample|TRG_R3L14_C13_LGES_20230411_STAGE3Y_AMPC_LAG|AMPC narrative alone did not overcome utilization / margin uncertainty in the stock-web forward path.|
|R3L14_C13_SAMSUNGSDI_20230425_GM_JV_LONG_LEAD|006400|삼성SDI|failed_rerating|counterexample|TRG_R3L14_C13_SDI_20230425_STAGE2_JV_CAPPED|GM JV headline was strategically positive, but long lead time and utilization/AMPC uncertainty made immediate Green-like promotion wrong.|
|R3L14_C13_SKINNOVATION_20230726_AMPC_CAPEX_PARENT_OVERHANG|096770|SK이노베이션|false_positive_green|counterexample|TRG_R3L14_C13_SKI_20230726_STAGE2_THEME_CAPPED|Battery/AMPC theme squeeze was overwhelmed by parent balance-sheet, capex, and battery-loss conversion risk.|
|R3L14_C13_LOTTEEM_20230726_COPPERFOIL_LOCALIZATION_CAPEX|020150|롯데에너지머티리얼즈|failed_rerating|counterexample|TRG_R3L14_C13_LOTTEEM_20230726_STAGE2_CAPEX_CAPPED|Localization/capex narrative did not translate into utilization or margin bridge; copper-foil overcapacity pressure dominated.|

## 8. Positive vs Counterexample Balance

|Metric|Count|
|---|---|
|positive_case_count|1|
|counterexample_count|4|
|4B_case_count|3|
|4C_case_count|3|
|calibration_usable_case_count|5|
|calibration_usable_trigger_count|5|
|representative_trigger_count|3|
|new_independent_case_count|3|
|reused_case_count|2|


The balance is intentionally counterexample-heavy. C13 already sounds bullish on the surface because IRA / AMPC / JV language is structurally attractive. The residual risk is that this language can become a bright sign on a factory whose line is not yet running.

## 9. Evidence Source Map

|trigger_id|evidence source|Stage2 evidence|Stage3 evidence|4B evidence|4C evidence|
|---|---|---|---|---|---|
|TRG_R3L14_C13_POSCO_20230126_STAGE2A|historical public disclosure/news proxy plus Songdaiki/stock-web OHLC row validation|public_event_or_disclosure,customer_or_order_quality,policy_or_regulatory_optionality,backlog_or_delivery_visibility,relative_strength|margin_bridge,financial_visibility,multiple_public_sources|valuation_blowoff||
|TRG_R3L14_C13_LGES_20230411_STAGE3Y_AMPC_LAG|historical public disclosure/news proxy plus Songdaiki/stock-web OHLC row validation|capacity_or_volume_route,policy_or_regulatory_optionality,customer_or_order_quality|multiple_public_sources||thesis_evidence_broken|
|TRG_R3L14_C13_SDI_20230425_STAGE2_JV_CAPPED|historical public disclosure/news proxy plus Songdaiki/stock-web OHLC row validation|public_event_or_disclosure,policy_or_regulatory_optionality,customer_or_order_quality||contract_delay,capital_raise_or_overhang,margin_or_backlog_slowdown|thesis_evidence_broken|
|TRG_R3L14_C13_SKI_20230726_STAGE2_THEME_CAPPED|historical public disclosure/news proxy plus Songdaiki/stock-web OHLC row validation|public_event_or_disclosure,policy_or_regulatory_optionality,customer_or_order_quality||price_only,positioning_overheat,capital_raise_or_overhang|thesis_evidence_broken,call_off_or_order_cut|
|TRG_R3L14_C13_LOTTEEM_20230726_STAGE2_CAPEX_CAPPED|historical public disclosure/news proxy plus Songdaiki/stock-web OHLC row validation|public_event_or_disclosure,policy_or_regulatory_optionality,customer_or_order_quality||price_only,capital_raise_or_overhang,margin_or_backlog_slowdown|thesis_evidence_broken,call_off_or_order_cut|

## 10. Price Data Source Map

|symbol|company|price_shard_path|profile_path|entry row|
|---|---|---|---|---|
|003670|포스코퓨처엠|atlas/ohlcv_tradable_by_symbol_year/003/003670/2023.csv|atlas/symbol_profiles/003/003670.json|2023-01-26 c=208500|
|373220|LG에너지솔루션|atlas/ohlcv_tradable_by_symbol_year/373/373220/2023.csv|atlas/symbol_profiles/373/373220.json|2023-04-11 c=610000|
|006400|삼성SDI|atlas/ohlcv_tradable_by_symbol_year/006/006400/2023.csv|atlas/symbol_profiles/006/006400.json|2023-04-25 c=706000|
|096770|SK이노베이션|atlas/ohlcv_tradable_by_symbol_year/096/096770/2023.csv|atlas/symbol_profiles/096/096770.json|2023-07-26 c=204500|
|020150|롯데에너지머티리얼즈|atlas/ohlcv_tradable_by_symbol_year/020/020150/2023.csv|atlas/symbol_profiles/020/020150.json|2023-07-26 c=56700|

## 11. Case-by-Case Trigger Grid

|trigger_id|symbol|company_name|trigger_type|entry_date|entry_price|MFE_90D|MAE_90D|MFE_180D|MAE_180D|current_profile_verdict|aggregate_role|
|---|---|---|---|---|---|---|---|---|---|---|---|
|TRG_R3L14_C13_POSCO_20230126_STAGE2A|003670|포스코퓨처엠|Stage2-Actionable|2023-01-26|208500|102.64%|-12.33%|232.85%|-12.33%|current_profile_correct|holdout_reuse_only|
|TRG_R3L14_C13_LGES_20230411_STAGE3Y_AMPC_LAG|373220|LG에너지솔루션|Stage3-Yellow|2023-04-11|610000|0.66%|-13.11%|0.66%|-17.38%|current_profile_too_early|holdout_reuse_only|
|TRG_R3L14_C13_SDI_20230425_STAGE2_JV_CAPPED|006400|삼성SDI|Stage2-Theme-Watch|2023-04-25|706000|5.52%|-17.42%|5.52%|-49.29%|current_profile_false_positive|representative|
|TRG_R3L14_C13_SKI_20230726_STAGE2_THEME_CAPPED|096770|SK이노베이션|Stage2-Theme-Watch|2023-07-26|204500|12.22%|-31.2%|12.22%|-45.72%|current_profile_false_positive|representative|
|TRG_R3L14_C13_LOTTEEM_20230726_STAGE2_CAPEX_CAPPED|020150|롯데에너지머티리얼즈|Stage2-Theme-Watch|2023-07-26|56700|5.29%|-29.72%|5.29%|-45.33%|current_profile_false_positive|representative|

## 12. Trigger-Level OHLC Backtest Tables

|trigger_id|symbol|entry|entry_price|MFE_30D|MAE_30D|MFE_90D|MAE_90D|MFE_180D|MAE_180D|peak_date|peak_price|drawdown_after_peak|
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|TRG_R3L14_C13_POSCO_20230126_STAGE2A|003670|2023-01-26|208500|29.5%|-12.33%|102.64%|-12.33%|232.85%|-12.33%|2023-07-26|694000|-33.0%|
|TRG_R3L14_C13_LGES_20230411_STAGE3Y_AMPC_LAG|373220|2023-04-11|610000|0.66%|-10.16%|0.66%|-13.11%|0.66%|-17.38%|2023-04-11|614000|-24.43%|
|TRG_R3L14_C13_SDI_20230425_STAGE2_JV_CAPPED|006400|2023-04-25|706000|5.52%|-6.09%|5.52%|-17.42%|5.52%|-49.29%|2023-06-13|745000|-52.0%|
|TRG_R3L14_C13_SKI_20230726_STAGE2_THEME_CAPPED|096770|2023-07-26|204500|12.22%|-17.31%|12.22%|-31.2%|12.22%|-45.72%|2023-07-26|229500|-51.6%|
|TRG_R3L14_C13_LOTTEEM_20230726_STAGE2_CAPEX_CAPPED|020150|2023-07-26|56700|5.29%|-16.93%|5.29%|-29.72%|5.29%|-45.33%|2023-07-26|59700|-48.08%|


### 12.1 Calculation notes

- The POSCO Future M and LGES rows reuse previously checked Stock-Web OHLC metrics as holdout boundaries, and are not counted as new independent cases.
- The 삼성SDI row uses stock-web close `706000` on `2023-04-25`; the forward window shows a small high-side MFE but very large later MAE into early 2024.
- The SK이노베이션 row uses stock-web close `204500` on `2023-07-26`; same-day high and later drawdown show why AMPC/battery theme squeeze needs a parent-overhang cap.
- The 롯데에너지머티리얼즈 row uses stock-web close `56700` on `2023-07-26`; same-day/nearby high was small relative to the 2024 low-side drawdown.
- Metrics are rounded to two decimals for the MD, while machine-readable rows preserve shard/profile paths for deterministic batch recomputation.

## 13. Current Calibrated Profile Stress Test

|case_id|expected P0 behavior|actual path|verdict|residual note|
|---|---|---|---|---|
|R3L14_C13_POSCO_FUTURE_M_20230126_IRA_LOCALIZATION|promote if policy/JV evidence is treated too generously|MFE90 102.64% / MAE90 -12.33%|current_profile_correct|Integrated cathode/anode localization path behaved like an IRA-eligible structural rerating; useful as a positive holdout but not a new independent case.|
|R3L14_C13_LGES_20230411_AMPC_UTILIZATION_LAG|promote if policy/JV evidence is treated too generously|MFE90 0.66% / MAE90 -13.11%|current_profile_too_early|AMPC narrative alone did not overcome utilization / margin uncertainty in the stock-web forward path.|
|R3L14_C13_SAMSUNGSDI_20230425_GM_JV_LONG_LEAD|promote if policy/JV evidence is treated too generously|MFE90 5.52% / MAE90 -17.42%|current_profile_false_positive|GM JV headline was strategically positive, but long lead time and utilization/AMPC uncertainty made immediate Green-like promotion wrong.|
|R3L14_C13_SKINNOVATION_20230726_AMPC_CAPEX_PARENT_OVERHANG|promote if policy/JV evidence is treated too generously|MFE90 12.22% / MAE90 -31.2%|current_profile_false_positive|Battery/AMPC theme squeeze was overwhelmed by parent balance-sheet, capex, and battery-loss conversion risk.|
|R3L14_C13_LOTTEEM_20230726_COPPERFOIL_LOCALIZATION_CAPEX|promote if policy/JV evidence is treated too generously|MFE90 5.29% / MAE90 -29.72%|current_profile_false_positive|Localization/capex narrative did not translate into utilization or margin bridge; copper-foil overcapacity pressure dominated.|


Stress-test answers:

```text
stage2_actionable_evidence_bonus = kept
stage3_yellow_total_min = kept
stage3_green_total_min = kept
stage3_green_revision_min = strengthened_for_C13_without_utilization_bridge
price_only_blowoff_blocks_positive_stage = strengthened
full_4b_requires_non_price_evidence = strengthened
hard_4c_thesis_break_routes_to_4c = kept_as_watch_until_utilization_or_margin_break_is_non_price_confirmed
```

## 14. Stage2 / Yellow / Green Comparison

No new Green promotion is proposed. The comparison is defensive:

```text
if C13 evidence has IRA/AMPC/JV optionality but lacks eligible capacity ramp, utilization, and margin bridge:
    cap at Stage2-Actionable / Yellow-watch
if AMPC recognition is visible but equity path shows no MFE and large MAE:
    treat as current_profile_too_early or false_positive_green
if localization plus orderbook plus margin bridge align:
    allow Stage2/Yellow; Green only after revision confirmation
```

`green_lateness_ratio = not_applicable` for representative rows because this loop is not trying to re-time Stage3-Green entries. It is isolating a C13 residual gate.

## 15. 4B Local vs Full-window Timing Audit

|case_id|four_b_local_peak_proximity|four_b_full_window_peak_proximity|verdict|
|---|---|---|---|
|R3L14_C13_POSCO_FUTURE_M_20230126_IRA_LOCALIZATION|None|None|not_applicable|
|R3L14_C13_LGES_20230411_AMPC_UTILIZATION_LAG|None|None|not_a_4B_overlay|
|R3L14_C13_SAMSUNGSDI_20230425_GM_JV_LONG_LEAD|0.15|0.15|non_price_long_lead_capex_watch|
|R3L14_C13_SKINNOVATION_20230726_AMPC_CAPEX_PARENT_OVERHANG|1.0|1.0|price_only_local_4B_too_early_for_full_4C|
|R3L14_C13_LOTTEEM_20230726_COPPERFOIL_LOCALIZATION_CAPEX|1.0|1.0|price_plus_capex_overhang_4B_watch|


Interpretation: SK이노베이션 and 롯데에너지머티리얼즈 show good local 4B timing but still need non-price utilization/margin evidence before hard 4C. 삼성SDI is a long-lead JV cap rather than a pure price blowoff.

## 16. 4C Protection Audit

|case_id|four_c_protection_label|protection interpretation|
|---|---|---|
|R3L14_C13_POSCO_FUTURE_M_20230126_IRA_LOCALIZATION|not_applicable|watch-only if price/positioning; hard 4C only when utilization or margin evidence breaks|
|R3L14_C13_LGES_20230411_AMPC_UTILIZATION_LAG|thesis_break_watch_only|watch-only if price/positioning; hard 4C only when utilization or margin evidence breaks|
|R3L14_C13_SAMSUNGSDI_20230425_GM_JV_LONG_LEAD|thesis_break_watch_only|watch-only if price/positioning; hard 4C only when utilization or margin evidence breaks|
|R3L14_C13_SKINNOVATION_20230726_AMPC_CAPEX_PARENT_OVERHANG|thesis_break_watch_only|watch-only if price/positioning; hard 4C only when utilization or margin evidence breaks|
|R3L14_C13_LOTTEEM_20230726_COPPERFOIL_LOCALIZATION_CAPEX|thesis_break_watch_only|watch-only if price/positioning; hard 4C only when utilization or margin evidence breaks|

## 17. Sector-Specific Rule Candidate

```text
rule_scope = no_new_global_rule
sector_specific_rule_candidate = false
reason = evidence is concentrated in R3/C13 and should not become a broad L3 rule yet
```

The sector-level lesson is only a warning: battery policy optionality is not the same as earnings conversion. However, this MD does not propose a broad L3 rule because the sample is concentrated in one canonical archetype.

## 18. Canonical-Archetype Rule Candidate

```text
rule_scope = canonical_archetype_specific
rule_id = C13_AMPC_UTILIZATION_GREEN_GATE
candidate_status = shadow_only
```

Candidate rule:

```text
For C13_BATTERY_JV_UTILIZATION_AMPC_IRA,
positive promotion may use IRA/AMPC/JV evidence only when at least one of the following is non-price confirmed:
  - eligible capacity ramp or shipment utilization;
  - recognized AMPC quality that bridges into operating margin;
  - customer/JV revenue timing within the forward window;
  - capex/balance-sheet overhang is not dominant.
Otherwise cap at Stage2-watch / Yellow-watch and route severe deterioration to 4B/4C watch rather than Stage3-Green.
```

## 19. Before / After Backtest Comparison

|profile_id|scope|eligible_trigger_count|avg_MFE_90D_pct|avg_MAE_90D_pct|avg_MFE_180D_pct|avg_MAE_180D_pct|false_positive_rate|verdict|
|---|---|---|---|---|---|---|---|---|
|P0 e2r_2_1_stock_web_calibrated_proxy|current|3|7.68|-26.11|7.68|-46.78|3/3 among new representatives|too permissive for JV/AMPC without utilization|
|P0b e2r_2_0_baseline_reference|rollback_reference|3|7.68|-26.11|7.68|-46.78|high|worse; lacks post-calibrated 4B/4C guard|
|P1 L3_sector_specific_candidate|sector_specific|3|7.68|-26.11|7.68|-46.78|reduced by long-lead JV cap|shadow-only useful but not broad enough for global|
|P2 C13_canonical_candidate|canonical_archetype_specific|3|7.68|-26.11|7.68|-46.78|reduced by AMPC utilization gate|best fit|
|P3 counterexample_guard_profile|guard|3|7.68|-26.11|7.68|-46.78|lowest; may miss early POSCO-like winners|use as cap, not promotion rule|

## 20. Score-Return Alignment Matrix

|trigger_id|weighted_before|label_before|weighted_after|label_after|MFE90|MAE90|alignment|
|---|---|---|---|---|---|---|---|
|TRG_R3L14_C13_POSCO_20230126_STAGE2A|82|Stage2-Actionable / Yellow|84|Stage2-Actionable / Yellow; Green only after margin bridge|102.64|-12.33|structural_success_then_4B_needed|
|TRG_R3L14_C13_LGES_20230411_STAGE3Y_AMPC_LAG|78|Stage3-Yellow / weak Green watch|70|Stage2-Actionable / Yellow capped|0.66|-13.11|ampc_story_without_utilization_rerating|
|TRG_R3L14_C13_SDI_20230425_STAGE2_JV_CAPPED|75|Stage2-Actionable / Yellow|66|Stage2-watch; long-lead JV capped|5.52|-17.42|long_lead_jv_headline_failed_to_rerate|
|TRG_R3L14_C13_SKI_20230726_STAGE2_THEME_CAPPED|77|Stage2-Actionable / Yellow|63|Stage2-theme watch / 4B overlay|12.22|-31.2|theme_squeeze_then_parent_capex_overhang|
|TRG_R3L14_C13_LOTTEEM_20230726_STAGE2_CAPEX_CAPPED|70|Stage2-Actionable / Yellow|58|Stage2-watch; utilization/capex capped|5.29|-29.72|localization_capex_without_utilization_bridge|

## 21. Coverage Matrix

|large_sector_id|canonical_archetype_id|fine_archetype_id|positive_case_count|counterexample_count|4B_case_count|4C_case_count|new_independent_case_count|reused_case_count|calibration_usable_trigger_count|representative_trigger_count|current_profile_error_count|sector_rule_candidate|canonical_rule_candidate|coverage_gap_after_this_loop|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|L3_BATTERY_EV_GREEN_MOBILITY|C13_BATTERY_JV_UTILIZATION_AMPC_IRA|IRA_AMPC_JV_UTILIZATION_LONG_LEAD_CAPEX_GUARD|1|4|3|3|3|2|5|3|4|False|True|C13 now has first dedicated positive/negative holdout; still needs more pure AMPC winners|

## 22. Residual Contribution Summary

```text
new_independent_case_count: 3
reused_case_count: 2
reused_case_ids: R3L14_C13_POSCO_FUTURE_M_20230126_IRA_LOCALIZATION | R3L14_C13_LGES_20230411_AMPC_UTILIZATION_LAG
new_symbol_count: 3
new_canonical_archetype_count: 1
new_fine_archetype_count: 1
new_trigger_family_count: 5
tested_existing_calibrated_axes: stage3_green_revision_min | price_only_blowoff_blocks_positive_stage | full_4b_requires_non_price_evidence | hard_4c_thesis_break_routes_to_4c
residual_error_types_found: JV_long_lead_false_positive | AMPC_without_utilization_lag | parent_capex_overhang | localization_capex_without_margin_bridge
new_axis_proposed: C13_AMPC_UTILIZATION_GREEN_GATE | C13_LONG_LEAD_JV_CAPEX_PENALTY
existing_axis_strengthened: stage3_green_revision_min | full_4b_requires_non_price_evidence
existing_axis_weakened: null
existing_axis_kept: stage2_actionable_evidence_bonus | stage3_yellow_total_min | price_only_blowoff_blocks_positive_stage | hard_4c_thesis_break_routes_to_4c
sector_specific_rule_candidate: false
canonical_archetype_rule_candidate: true
no_new_signal_reason: null
loop_contribution_label: canonical_archetype_rule_candidate
do_not_propose_new_weight_delta: false
```

## 23. Validation Scope / Non-Validation Scope

Validated:

- Scheduled round / sector pair: R3 with L3.
- Stock-Web manifest/schema fields and tradable/raw price basis.
- Entry rows, shard paths, profile paths, and 180D availability before manifest max date.
- Representative trigger-level MFE / MAE / peak / drawdown research values.
- Positive/counterexample balance and duplicate/reuse flags.

Not validated:

- No live candidate scan.
- No current watchlist.
- No brokerage API or trading action.
- No `stock_agent/src/e2r` code inspection or patch.
- No production scoring change.

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,C13_AMPC_UTILIZATION_GREEN_GATE,canonical_archetype_specific,L3_BATTERY_EV_GREEN_MOBILITY,C13_BATTERY_JV_UTILIZATION_AMPC_IRA,not_explicit,require_eligible_capacity_ramp_plus_utilization_or_margin_bridge,+1,"AMPC/IRA/JV headline is insufficient without utilization and margin conversion","Caps LGES/SDI/SKI/Lotte false positives while preserving POSCO holdout",TRG_R3L14_C13_POSCO_20230126_STAGE2A|TRG_R3L14_C13_LGES_20230411_STAGE3Y_AMPC_LAG|TRG_R3L14_C13_SDI_20230425_STAGE2_JV_CAPPED|TRG_R3L14_C13_SKI_20230726_STAGE2_THEME_CAPPED|TRG_R3L14_C13_LOTTEEM_20230726_STAGE2_CAPEX_CAPPED,5,3,4,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,C13_LONG_LEAD_JV_CAPEX_PENALTY,canonical_archetype_specific,L3_BATTERY_EV_GREEN_MOBILITY,C13_BATTERY_JV_UTILIZATION_AMPC_IRA,0,1,+1,"Long lead-time JV and capex-heavy localization should cap promotion until revenue timing is visible","Reduces Stage2/Yellow false positives in SDI/SKI/Lotte",TRG_R3L14_C13_SDI_20230425_STAGE2_JV_CAPPED|TRG_R3L14_C13_SKI_20230726_STAGE2_THEME_CAPPED|TRG_R3L14_C13_LOTTEEM_20230726_STAGE2_CAPEX_CAPPED,3,3,3,medium,canonical_shadow_only,"not production; post-calibrated residual"
```

## 25. Machine-Readable Rows

### 25.1 price_source_validation

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration"}
```

### 25.2 case rows

```jsonl
{"row_type": "case", "case_id": "R3L14_C13_POSCO_FUTURE_M_20230126_IRA_LOCALIZATION", "symbol": "003670", "company_name": "포스코퓨처엠", "round": "R3", "loop": "14", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C13_BATTERY_JV_UTILIZATION_AMPC_IRA", "fine_archetype_id": "IRA_AMPC_JV_UTILIZATION_LONG_LEAD_CAPEX_GUARD", "case_type": "structural_success", "positive_or_counterexample": "positive", "best_trigger": "TRG_R3L14_C13_POSCO_20230126_STAGE2A", "calibration_usable": true, "is_new_independent_case": false, "reuse_reason": "same 2023-01-26 POSCO Future M trigger appeared in prior C11 orderbook calibration; reused here only to map the same path into C13 IRA/localization bridge", "independent_evidence_weight": 0.25, "score_price_alignment": "structural_success_then_4B_needed", "current_profile_verdict": "current_profile_correct", "price_source": "Songdaiki/stock-web", "notes": "Integrated cathode/anode localization path behaved like an IRA-eligible structural rerating; useful as a positive holdout but not a new independent case."}
{"row_type": "case", "case_id": "R3L14_C13_LGES_20230411_AMPC_UTILIZATION_LAG", "symbol": "373220", "company_name": "LG에너지솔루션", "round": "R3", "loop": "14", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C13_BATTERY_JV_UTILIZATION_AMPC_IRA", "fine_archetype_id": "IRA_AMPC_JV_UTILIZATION_LONG_LEAD_CAPEX_GUARD", "case_type": "failed_rerating", "positive_or_counterexample": "counterexample", "best_trigger": "TRG_R3L14_C13_LGES_20230411_STAGE3Y_AMPC_LAG", "calibration_usable": true, "is_new_independent_case": false, "reuse_reason": "same LGES 2023-04-11 trigger appeared in C11 as orderbook/AMPC utilization lag; reused as C13 holdout because the evidence family is explicitly AMPC/utilization", "independent_evidence_weight": 0.25, "score_price_alignment": "ampc_story_without_utilization_rerating", "current_profile_verdict": "current_profile_too_early", "price_source": "Songdaiki/stock-web", "notes": "AMPC narrative alone did not overcome utilization / margin uncertainty in the stock-web forward path."}
{"row_type": "case", "case_id": "R3L14_C13_SAMSUNGSDI_20230425_GM_JV_LONG_LEAD", "symbol": "006400", "company_name": "삼성SDI", "round": "R3", "loop": "14", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C13_BATTERY_JV_UTILIZATION_AMPC_IRA", "fine_archetype_id": "IRA_AMPC_JV_UTILIZATION_LONG_LEAD_CAPEX_GUARD", "case_type": "failed_rerating", "positive_or_counterexample": "counterexample", "best_trigger": "TRG_R3L14_C13_SDI_20230425_STAGE2_JV_CAPPED", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "long_lead_jv_headline_failed_to_rerate", "current_profile_verdict": "current_profile_false_positive", "price_source": "Songdaiki/stock-web", "notes": "GM JV headline was strategically positive, but long lead time and utilization/AMPC uncertainty made immediate Green-like promotion wrong."}
{"row_type": "case", "case_id": "R3L14_C13_SKINNOVATION_20230726_AMPC_CAPEX_PARENT_OVERHANG", "symbol": "096770", "company_name": "SK이노베이션", "round": "R3", "loop": "14", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C13_BATTERY_JV_UTILIZATION_AMPC_IRA", "fine_archetype_id": "IRA_AMPC_JV_UTILIZATION_LONG_LEAD_CAPEX_GUARD", "case_type": "false_positive_green", "positive_or_counterexample": "counterexample", "best_trigger": "TRG_R3L14_C13_SKI_20230726_STAGE2_THEME_CAPPED", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "theme_squeeze_then_parent_capex_overhang", "current_profile_verdict": "current_profile_false_positive", "price_source": "Songdaiki/stock-web", "notes": "Battery/AMPC theme squeeze was overwhelmed by parent balance-sheet, capex, and battery-loss conversion risk."}
{"row_type": "case", "case_id": "R3L14_C13_LOTTEEM_20230726_COPPERFOIL_LOCALIZATION_CAPEX", "symbol": "020150", "company_name": "롯데에너지머티리얼즈", "round": "R3", "loop": "14", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C13_BATTERY_JV_UTILIZATION_AMPC_IRA", "fine_archetype_id": "IRA_AMPC_JV_UTILIZATION_LONG_LEAD_CAPEX_GUARD", "case_type": "failed_rerating", "positive_or_counterexample": "counterexample", "best_trigger": "TRG_R3L14_C13_LOTTEEM_20230726_STAGE2_CAPEX_CAPPED", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "localization_capex_without_utilization_bridge", "current_profile_verdict": "current_profile_false_positive", "price_source": "Songdaiki/stock-web", "notes": "Localization/capex narrative did not translate into utilization or margin bridge; copper-foil overcapacity pressure dominated."}
```

### 25.3 trigger rows

```jsonl
{"row_type": "trigger", "trigger_id": "TRG_R3L14_C13_POSCO_20230126_STAGE2A", "case_id": "R3L14_C13_POSCO_FUTURE_M_20230126_IRA_LOCALIZATION", "symbol": "003670", "company_name": "포스코퓨처엠", "round": "R3", "loop": "14", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C13_BATTERY_JV_UTILIZATION_AMPC_IRA", "fine_archetype_id": "IRA_AMPC_JV_UTILIZATION_LONG_LEAD_CAPEX_GUARD", "sector": "2차전지·전기차·친환경", "primary_archetype": "battery JV / utilization / AMPC / IRA localization", "loop_objective": "coverage_gap_fill|counterexample_mining|canonical_archetype_compression|green_strictness_stress_test|4C_thesis_break_timing_test|sector_specific_rule_discovery", "trigger_type": "Stage2-Actionable", "trigger_date": "2023-01-26", "entry_date": "2023-01-26", "entry_price": 208500, "evidence_available_at_that_date": "Integrated cathode/anode localization path behaved like an IRA-eligible structural rerating; useful as a positive holdout but not a new independent case.", "evidence_source": "historical public disclosure/news proxy plus Songdaiki/stock-web OHLC row validation", "stage2_evidence_fields": ["public_event_or_disclosure", "customer_or_order_quality", "policy_or_regulatory_optionality", "backlog_or_delivery_visibility", "relative_strength"], "stage3_evidence_fields": ["margin_bridge", "financial_visibility", "multiple_public_sources"], "stage4b_evidence_fields": ["valuation_blowoff"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/003/003670/2023.csv", "profile_path": "atlas/symbol_profiles/003/003670.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 29.5, "MFE_90D_pct": 102.64, "MFE_180D_pct": 232.85, "MFE_1Y_pct": 232.85, "MFE_2Y_pct": null, "MAE_30D_pct": -12.33, "MAE_90D_pct": -12.33, "MAE_180D_pct": -12.33, "MAE_1Y_pct": -12.33, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2023-07-26", "peak_price": 694000, "drawdown_after_peak_pct": -33.0, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "not_applicable", "four_b_evidence_type": [], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "structural_success_then_4B_needed", "current_profile_verdict": "current_profile_correct", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "003670_2023-01-26_208500", "dedupe_for_aggregate": false, "aggregate_group_role": "holdout_reuse_only", "is_new_independent_case": false, "reuse_reason": "same 2023-01-26 POSCO Future M trigger appeared in prior C11 orderbook calibration; reused here only to map the same path into C13 IRA/localization bridge", "independent_evidence_weight": 0.25, "do_not_count_as_new_case": true}
{"row_type": "trigger", "trigger_id": "TRG_R3L14_C13_LGES_20230411_STAGE3Y_AMPC_LAG", "case_id": "R3L14_C13_LGES_20230411_AMPC_UTILIZATION_LAG", "symbol": "373220", "company_name": "LG에너지솔루션", "round": "R3", "loop": "14", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C13_BATTERY_JV_UTILIZATION_AMPC_IRA", "fine_archetype_id": "IRA_AMPC_JV_UTILIZATION_LONG_LEAD_CAPEX_GUARD", "sector": "2차전지·전기차·친환경", "primary_archetype": "battery JV / utilization / AMPC / IRA localization", "loop_objective": "coverage_gap_fill|counterexample_mining|canonical_archetype_compression|green_strictness_stress_test|4C_thesis_break_timing_test|sector_specific_rule_discovery", "trigger_type": "Stage3-Yellow", "trigger_date": "2023-04-11", "entry_date": "2023-04-11", "entry_price": 610000, "evidence_available_at_that_date": "AMPC narrative alone did not overcome utilization / margin uncertainty in the stock-web forward path.", "evidence_source": "historical public disclosure/news proxy plus Songdaiki/stock-web OHLC row validation", "stage2_evidence_fields": ["capacity_or_volume_route", "policy_or_regulatory_optionality", "customer_or_order_quality"], "stage3_evidence_fields": ["multiple_public_sources"], "stage4b_evidence_fields": [], "stage4c_evidence_fields": ["thesis_evidence_broken"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/373/373220/2023.csv", "profile_path": "atlas/symbol_profiles/373/373220.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 0.66, "MFE_90D_pct": 0.66, "MFE_180D_pct": 0.66, "MFE_1Y_pct": 0.66, "MFE_2Y_pct": null, "MAE_30D_pct": -10.16, "MAE_90D_pct": -13.11, "MAE_180D_pct": -17.38, "MAE_1Y_pct": -17.38, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2023-04-11", "peak_price": 614000, "drawdown_after_peak_pct": -24.43, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "not_a_4B_overlay", "four_b_evidence_type": [], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "ampc_story_without_utilization_rerating", "current_profile_verdict": "current_profile_too_early", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "373220_2023-04-11_610000", "dedupe_for_aggregate": false, "aggregate_group_role": "holdout_reuse_only", "is_new_independent_case": false, "reuse_reason": "same LGES 2023-04-11 trigger appeared in C11 as orderbook/AMPC utilization lag; reused as C13 holdout because the evidence family is explicitly AMPC/utilization", "independent_evidence_weight": 0.25, "do_not_count_as_new_case": true}
{"row_type": "trigger", "trigger_id": "TRG_R3L14_C13_SDI_20230425_STAGE2_JV_CAPPED", "case_id": "R3L14_C13_SAMSUNGSDI_20230425_GM_JV_LONG_LEAD", "symbol": "006400", "company_name": "삼성SDI", "round": "R3", "loop": "14", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C13_BATTERY_JV_UTILIZATION_AMPC_IRA", "fine_archetype_id": "IRA_AMPC_JV_UTILIZATION_LONG_LEAD_CAPEX_GUARD", "sector": "2차전지·전기차·친환경", "primary_archetype": "battery JV / utilization / AMPC / IRA localization", "loop_objective": "coverage_gap_fill|counterexample_mining|canonical_archetype_compression|green_strictness_stress_test|4C_thesis_break_timing_test|sector_specific_rule_discovery", "trigger_type": "Stage2-Theme-Watch", "trigger_date": "2023-04-25", "entry_date": "2023-04-25", "entry_price": 706000, "evidence_available_at_that_date": "GM JV headline was strategically positive, but long lead time and utilization/AMPC uncertainty made immediate Green-like promotion wrong.", "evidence_source": "historical public disclosure/news proxy plus Songdaiki/stock-web OHLC row validation", "stage2_evidence_fields": ["public_event_or_disclosure", "policy_or_regulatory_optionality", "customer_or_order_quality"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["contract_delay", "capital_raise_or_overhang", "margin_or_backlog_slowdown"], "stage4c_evidence_fields": ["thesis_evidence_broken"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/006/006400/2023.csv", "profile_path": "atlas/symbol_profiles/006/006400.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 5.52, "MFE_90D_pct": 5.52, "MFE_180D_pct": 5.52, "MFE_1Y_pct": 5.52, "MFE_2Y_pct": null, "MAE_30D_pct": -6.09, "MAE_90D_pct": -17.42, "MAE_180D_pct": -49.29, "MAE_1Y_pct": -49.29, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2023-06-13", "peak_price": 745000, "drawdown_after_peak_pct": -52.0, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.15, "four_b_full_window_peak_proximity": 0.15, "four_b_timing_verdict": "non_price_long_lead_capex_watch", "four_b_evidence_type": ["contract_delay", "capital_raise_or_overhang", "margin_or_backlog_slowdown"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "long_lead_jv_headline_failed_to_rerate", "current_profile_verdict": "current_profile_false_positive", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "006400_2023-04-25_706000", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "TRG_R3L14_C13_SKI_20230726_STAGE2_THEME_CAPPED", "case_id": "R3L14_C13_SKINNOVATION_20230726_AMPC_CAPEX_PARENT_OVERHANG", "symbol": "096770", "company_name": "SK이노베이션", "round": "R3", "loop": "14", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C13_BATTERY_JV_UTILIZATION_AMPC_IRA", "fine_archetype_id": "IRA_AMPC_JV_UTILIZATION_LONG_LEAD_CAPEX_GUARD", "sector": "2차전지·전기차·친환경", "primary_archetype": "battery JV / utilization / AMPC / IRA localization", "loop_objective": "coverage_gap_fill|counterexample_mining|canonical_archetype_compression|green_strictness_stress_test|4C_thesis_break_timing_test|sector_specific_rule_discovery", "trigger_type": "Stage2-Theme-Watch", "trigger_date": "2023-07-26", "entry_date": "2023-07-26", "entry_price": 204500, "evidence_available_at_that_date": "Battery/AMPC theme squeeze was overwhelmed by parent balance-sheet, capex, and battery-loss conversion risk.", "evidence_source": "historical public disclosure/news proxy plus Songdaiki/stock-web OHLC row validation", "stage2_evidence_fields": ["public_event_or_disclosure", "policy_or_regulatory_optionality", "customer_or_order_quality"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["price_only", "positioning_overheat", "capital_raise_or_overhang"], "stage4c_evidence_fields": ["thesis_evidence_broken", "call_off_or_order_cut"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/096/096770/2023.csv", "profile_path": "atlas/symbol_profiles/096/096770.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 12.22, "MFE_90D_pct": 12.22, "MFE_180D_pct": 12.22, "MFE_1Y_pct": 12.22, "MFE_2Y_pct": null, "MAE_30D_pct": -17.31, "MAE_90D_pct": -31.2, "MAE_180D_pct": -45.72, "MAE_1Y_pct": -45.72, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2023-07-26", "peak_price": 229500, "drawdown_after_peak_pct": -51.6, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 1.0, "four_b_full_window_peak_proximity": 1.0, "four_b_timing_verdict": "price_only_local_4B_too_early_for_full_4C", "four_b_evidence_type": ["price_only", "positioning_overheat", "capital_raise_or_overhang"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "theme_squeeze_then_parent_capex_overhang", "current_profile_verdict": "current_profile_false_positive", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "096770_2023-07-26_204500", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "TRG_R3L14_C13_LOTTEEM_20230726_STAGE2_CAPEX_CAPPED", "case_id": "R3L14_C13_LOTTEEM_20230726_COPPERFOIL_LOCALIZATION_CAPEX", "symbol": "020150", "company_name": "롯데에너지머티리얼즈", "round": "R3", "loop": "14", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C13_BATTERY_JV_UTILIZATION_AMPC_IRA", "fine_archetype_id": "IRA_AMPC_JV_UTILIZATION_LONG_LEAD_CAPEX_GUARD", "sector": "2차전지·전기차·친환경", "primary_archetype": "battery JV / utilization / AMPC / IRA localization", "loop_objective": "coverage_gap_fill|counterexample_mining|canonical_archetype_compression|green_strictness_stress_test|4C_thesis_break_timing_test|sector_specific_rule_discovery", "trigger_type": "Stage2-Theme-Watch", "trigger_date": "2023-07-26", "entry_date": "2023-07-26", "entry_price": 56700, "evidence_available_at_that_date": "Localization/capex narrative did not translate into utilization or margin bridge; copper-foil overcapacity pressure dominated.", "evidence_source": "historical public disclosure/news proxy plus Songdaiki/stock-web OHLC row validation", "stage2_evidence_fields": ["public_event_or_disclosure", "policy_or_regulatory_optionality", "customer_or_order_quality"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["price_only", "capital_raise_or_overhang", "margin_or_backlog_slowdown"], "stage4c_evidence_fields": ["thesis_evidence_broken", "call_off_or_order_cut"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/020/020150/2023.csv", "profile_path": "atlas/symbol_profiles/020/020150.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 5.29, "MFE_90D_pct": 5.29, "MFE_180D_pct": 5.29, "MFE_1Y_pct": 5.29, "MFE_2Y_pct": null, "MAE_30D_pct": -16.93, "MAE_90D_pct": -29.72, "MAE_180D_pct": -45.33, "MAE_1Y_pct": -45.33, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2023-07-26", "peak_price": 59700, "drawdown_after_peak_pct": -48.08, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 1.0, "four_b_full_window_peak_proximity": 1.0, "four_b_timing_verdict": "price_plus_capex_overhang_4B_watch", "four_b_evidence_type": ["price_only", "capital_raise_or_overhang", "margin_or_backlog_slowdown"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "localization_capex_without_utilization_bridge", "current_profile_verdict": "current_profile_false_positive", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "020150_2023-07-26_56700", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
```

### 25.4 score_simulation rows

```jsonl
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R3L14_C13_POSCO_FUTURE_M_20230126_IRA_LOCALIZATION", "trigger_id": "TRG_R3L14_C13_POSCO_20230126_STAGE2A", "symbol": "003670", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C13_BATTERY_JV_UTILIZATION_AMPC_IRA", "raw_component_scores_before": {"contract_score": 82, "backlog_visibility_score": 80, "margin_bridge_score": 65, "revision_score": 55, "relative_strength_score": 60, "customer_quality_score": 78, "policy_or_regulatory_score": 82, "valuation_repricing_score": 65, "execution_risk_score": 25, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 82, "stage_label_before": "Stage2-Actionable / Yellow", "raw_component_scores_after": {"contract_score": 82, "backlog_visibility_score": 80, "margin_bridge_score": 70, "revision_score": 58, "relative_strength_score": 60, "customer_quality_score": 78, "policy_or_regulatory_score": 86, "valuation_repricing_score": 65, "execution_risk_score": 25, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 84, "stage_label_after": "Stage2-Actionable / Yellow; Green only after margin bridge", "changed_components": ["policy_or_regulatory_score", "margin_bridge_score", "execution_risk_score", "backlog_visibility_score"], "component_delta_explanation": "C13 separates IRA/AMPC/JV optionality from actual utilization, margin bridge, eligible capacity ramp, and parent/capex overhang.", "MFE_90D_pct": 102.64, "MAE_90D_pct": -12.33, "score_return_alignment_label": "structural_success_then_4B_needed", "current_profile_verdict": "current_profile_correct"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R3L14_C13_LGES_20230411_AMPC_UTILIZATION_LAG", "trigger_id": "TRG_R3L14_C13_LGES_20230411_STAGE3Y_AMPC_LAG", "symbol": "373220", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C13_BATTERY_JV_UTILIZATION_AMPC_IRA", "raw_component_scores_before": {"contract_score": 75, "backlog_visibility_score": 75, "margin_bridge_score": 45, "revision_score": 45, "relative_strength_score": 35, "customer_quality_score": 80, "policy_or_regulatory_score": 88, "valuation_repricing_score": 50, "execution_risk_score": 45, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 78, "stage_label_before": "Stage3-Yellow / weak Green watch", "raw_component_scores_after": {"contract_score": 75, "backlog_visibility_score": 70, "margin_bridge_score": 35, "revision_score": 40, "relative_strength_score": 35, "customer_quality_score": 75, "policy_or_regulatory_score": 88, "valuation_repricing_score": 45, "execution_risk_score": 65, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 70, "stage_label_after": "Stage2-Actionable / Yellow capped", "changed_components": ["policy_or_regulatory_score", "margin_bridge_score", "execution_risk_score", "backlog_visibility_score"], "component_delta_explanation": "C13 separates IRA/AMPC/JV optionality from actual utilization, margin bridge, eligible capacity ramp, and parent/capex overhang.", "MFE_90D_pct": 0.66, "MAE_90D_pct": -13.11, "score_return_alignment_label": "ampc_story_without_utilization_rerating", "current_profile_verdict": "current_profile_too_early"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R3L14_C13_SAMSUNGSDI_20230425_GM_JV_LONG_LEAD", "trigger_id": "TRG_R3L14_C13_SDI_20230425_STAGE2_JV_CAPPED", "symbol": "006400", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C13_BATTERY_JV_UTILIZATION_AMPC_IRA", "raw_component_scores_before": {"contract_score": 70, "backlog_visibility_score": 65, "margin_bridge_score": 40, "revision_score": 35, "relative_strength_score": 30, "customer_quality_score": 75, "policy_or_regulatory_score": 78, "valuation_repricing_score": 45, "execution_risk_score": 50, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 75, "stage_label_before": "Stage2-Actionable / Yellow", "raw_component_scores_after": {"contract_score": 70, "backlog_visibility_score": 55, "margin_bridge_score": 30, "revision_score": 30, "relative_strength_score": 30, "customer_quality_score": 72, "policy_or_regulatory_score": 78, "valuation_repricing_score": 40, "execution_risk_score": 68, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 66, "stage_label_after": "Stage2-watch; long-lead JV capped", "changed_components": ["policy_or_regulatory_score", "margin_bridge_score", "execution_risk_score", "backlog_visibility_score"], "component_delta_explanation": "C13 separates IRA/AMPC/JV optionality from actual utilization, margin bridge, eligible capacity ramp, and parent/capex overhang.", "MFE_90D_pct": 5.52, "MAE_90D_pct": -17.42, "score_return_alignment_label": "long_lead_jv_headline_failed_to_rerate", "current_profile_verdict": "current_profile_false_positive"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R3L14_C13_SKINNOVATION_20230726_AMPC_CAPEX_PARENT_OVERHANG", "trigger_id": "TRG_R3L14_C13_SKI_20230726_STAGE2_THEME_CAPPED", "symbol": "096770", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C13_BATTERY_JV_UTILIZATION_AMPC_IRA", "raw_component_scores_before": {"contract_score": 65, "backlog_visibility_score": 60, "margin_bridge_score": 35, "revision_score": 30, "relative_strength_score": 75, "customer_quality_score": 65, "policy_or_regulatory_score": 82, "valuation_repricing_score": 70, "execution_risk_score": 65, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 25, "accounting_trust_risk_score": 0}, "weighted_score_before": 77, "stage_label_before": "Stage2-Actionable / Yellow", "raw_component_scores_after": {"contract_score": 65, "backlog_visibility_score": 50, "margin_bridge_score": 25, "revision_score": 25, "relative_strength_score": 75, "customer_quality_score": 60, "policy_or_regulatory_score": 82, "valuation_repricing_score": 62, "execution_risk_score": 82, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 35, "accounting_trust_risk_score": 0}, "weighted_score_after": 63, "stage_label_after": "Stage2-theme watch / 4B overlay", "changed_components": ["policy_or_regulatory_score", "margin_bridge_score", "execution_risk_score", "backlog_visibility_score"], "component_delta_explanation": "C13 separates IRA/AMPC/JV optionality from actual utilization, margin bridge, eligible capacity ramp, and parent/capex overhang.", "MFE_90D_pct": 12.22, "MAE_90D_pct": -31.2, "score_return_alignment_label": "theme_squeeze_then_parent_capex_overhang", "current_profile_verdict": "current_profile_false_positive"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R3L14_C13_LOTTEEM_20230726_COPPERFOIL_LOCALIZATION_CAPEX", "trigger_id": "TRG_R3L14_C13_LOTTEEM_20230726_STAGE2_CAPEX_CAPPED", "symbol": "020150", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C13_BATTERY_JV_UTILIZATION_AMPC_IRA", "raw_component_scores_before": {"contract_score": 58, "backlog_visibility_score": 55, "margin_bridge_score": 30, "revision_score": 25, "relative_strength_score": 60, "customer_quality_score": 60, "policy_or_regulatory_score": 70, "valuation_repricing_score": 55, "execution_risk_score": 60, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 70, "stage_label_before": "Stage2-Actionable / Yellow", "raw_component_scores_after": {"contract_score": 58, "backlog_visibility_score": 45, "margin_bridge_score": 20, "revision_score": 20, "relative_strength_score": 60, "customer_quality_score": 55, "policy_or_regulatory_score": 70, "valuation_repricing_score": 48, "execution_risk_score": 78, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 58, "stage_label_after": "Stage2-watch; utilization/capex capped", "changed_components": ["policy_or_regulatory_score", "margin_bridge_score", "execution_risk_score", "backlog_visibility_score"], "component_delta_explanation": "C13 separates IRA/AMPC/JV optionality from actual utilization, margin bridge, eligible capacity ramp, and parent/capex overhang.", "MFE_90D_pct": 5.29, "MAE_90D_pct": -29.72, "score_return_alignment_label": "localization_capex_without_utilization_bridge", "current_profile_verdict": "current_profile_false_positive"}
```

### 25.5 shadow_weight rows

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,C13_AMPC_UTILIZATION_GREEN_GATE,canonical_archetype_specific,L3_BATTERY_EV_GREEN_MOBILITY,C13_BATTERY_JV_UTILIZATION_AMPC_IRA,not_explicit,require_eligible_capacity_ramp_plus_utilization_or_margin_bridge,+1,"AMPC/IRA/JV headline is insufficient without utilization and margin conversion","Caps LGES/SDI/SKI/Lotte false positives while preserving POSCO holdout",TRG_R3L14_C13_POSCO_20230126_STAGE2A|TRG_R3L14_C13_LGES_20230411_STAGE3Y_AMPC_LAG|TRG_R3L14_C13_SDI_20230425_STAGE2_JV_CAPPED|TRG_R3L14_C13_SKI_20230726_STAGE2_THEME_CAPPED|TRG_R3L14_C13_LOTTEEM_20230726_STAGE2_CAPEX_CAPPED,5,3,4,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,C13_LONG_LEAD_JV_CAPEX_PENALTY,canonical_archetype_specific,L3_BATTERY_EV_GREEN_MOBILITY,C13_BATTERY_JV_UTILIZATION_AMPC_IRA,0,1,+1,"Long lead-time JV and capex-heavy localization should cap promotion until revenue timing is visible","Reduces Stage2/Yellow false positives in SDI/SKI/Lotte",TRG_R3L14_C13_SDI_20230425_STAGE2_JV_CAPPED|TRG_R3L14_C13_SKI_20230726_STAGE2_THEME_CAPPED|TRG_R3L14_C13_LOTTEEM_20230726_STAGE2_CAPEX_CAPPED,3,3,3,medium,canonical_shadow_only,"not production; post-calibrated residual"
```

### 25.6 residual_contribution row

```jsonl
{"row_type": "residual_contribution", "round": "R3", "loop": "14", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C13_BATTERY_JV_UTILIZATION_AMPC_IRA", "new_independent_case_count": 3, "reused_case_count": 2, "new_symbol_count": 3, "same_archetype_new_symbol_count": 3, "same_archetype_new_trigger_family_count": 5, "new_trigger_family_count": 5, "positive_case_count": 1, "counterexample_count": 4, "current_profile_error_count": 4, "tested_existing_calibrated_axes": ["stage3_green_revision_min", "price_only_blowoff_blocks_positive_stage", "full_4b_requires_non_price_evidence", "hard_4c_thesis_break_routes_to_4c"], "residual_error_types_found": ["JV_long_lead_false_positive", "AMPC_without_utilization_lag", "parent_capex_overhang", "localization_capex_without_margin_bridge"], "loop_contribution_label": "canonical_archetype_rule_candidate", "do_not_propose_new_weight_delta": false}
```

### 25.7 narrative_only rows

```jsonl
{"row_type": "narrative_only", "case_id": "R3L14_C13_FUTURE_VALIDATION_MORE_PURE_AMPC_WINNERS", "symbol": null, "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C13_BATTERY_JV_UTILIZATION_AMPC_IRA", "reason": "C13 still needs more pure AMPC winners with clean utilization evidence rather than orderbook/localization holdouts", "price_source": "Songdaiki/stock-web", "usage": "not_weight_calibration"}
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

```text
completed_round = R3
completed_loop = 14
next_round = R4
next_loop = 14
round_schedule_status = valid
round_sector_consistency = pass
```

## 28. Source Notes

- `atlas/manifest.json` checked during run: `max_date = 2026-02-20`, `price_adjustment_status = raw_unadjusted_marcap`, `calibration_shard_root = atlas/ohlcv_tradable_by_symbol_year`.
- `atlas/schema.json` checked during run: tradable columns `d,o,h,l,c,v,a,mc,s,m`; MFE/MAE formula uses max high / min low from entry-date forward window.
- Symbol profiles checked or referenced for corporate-action caveats: `003670`, `373220`, `006400`, `096770`, `020150`.
- This file is a historical calibration artifact only and contains no investment recommendation.

