# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
research_session = post_calibrated_sector_archetype_residual_research
scheduled_round = R10
scheduled_loop = 12
completed_round = R10
completed_loop = 12
large_sector_id = L9_CONSTRUCTION_REALESTATE_HOUSING
canonical_archetype_id = C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK
fine_archetype_id = SMALL_MID_CONSTRUCTOR_PF_MARGIN_LIQUIDITY_RESIDUAL
output_file = e2r_stock_web_v12_residual_round_R10_loop_12_L9_CONSTRUCTION_REALESTATE_HOUSING_C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK_research.md
production_scoring_changed = false
shadow_weight_only = true
stock_agent_code_access_allowed = false
stock_agent_code_patch_allowed = false
stock_agent_live_scan_allowed = false
current_stock_discovery_allowed = false
price_route_hunt_allowed = false
stock_web_price_atlas_access_required = true
```

This loop adds 5 new independent calibration-usable cases, 3 counterexamples including one 4C narrative overlay, and 5 current-profile residual errors for R10/L9_CONSTRUCTION_REALESTATE_HOUSING/C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK.

## 1. Current Calibrated Profile Assumption

The current default profile proxy is `e2r_2_1_stock_web_calibrated_proxy`. This research does not re-prove the global Stage2 bonus or Green lateness rule. It tests a narrower C30 question: when construction/PF policy support arrives, which small/mid builders deserve a survivor score and which are only price-theme bounces.

```text
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

```text
round = R10
loop = 12
round_schedule_status = valid
round_sector_consistency = pass
large_sector_id = L9_CONSTRUCTION_REALESTATE_HOUSING
canonical_archetype_id = C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK
fine_archetype_id = SMALL_MID_CONSTRUCTOR_PF_MARGIN_LIQUIDITY_RESIDUAL
```

R10 maps to `L9_CONSTRUCTION_REALESTATE_HOUSING`. The canonical archetype is `C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK` because all selected cases sit at the junction of housing-cycle pressure, PF liquidity, balance-sheet survival, and policy support.

## 3. Previous Coverage / Duplicate Avoidance Check

Allowed research artifacts and local prior MD names indicate earlier R10 loops already covered larger or better-known construction cases including HDC현대산업개발, 현대건설, DL이앤씨, GS건설, 태영건설, 대우건설, 계룡건설, 코오롱글로벌, 금호건설, 동부건설, and 신세계건설. This loop avoids those repeated symbol/trigger families. The selected symbols are new for this scheduled-round sample set: KCC건설, HL D&I, 서희건설, 한신공영, HS화성, and 삼부토건.

```text
scheduled_round = R10
scheduled_loop = 12
new_symbol_count = 6
reused_case_count = 0
same_archetype_new_symbol_count = 6
same_archetype_new_trigger_family_count = 6
wrong_round_penalty = 0
schema_rematerialization_penalty = 0
```

## 4. Stock-Web OHLC Input / Price Source Validation

```text
source = Songdaiki/stock-web
source_url = https://github.com/Songdaiki/stock-web
source_name = FinanceData/marcap
source_repo_url = https://github.com/FinanceData/marcap
manifest_path = atlas/manifest.json
schema_path = atlas/schema.json
universe_path = atlas/universe/all_symbols.csv
min_date = 1995-05-02
max_date = 2026-02-20
tradable_row_count = 14354401
raw_row_count = 15214118
symbol_count = 5414
active_like_symbol_count = 2868
inactive_or_delisted_like_symbol_count = 2546
markets = KONEX|KOSDAQ|KOSDAQ GLOBAL|KOSPI
calibration_shard_root = atlas/ohlcv_tradable_by_symbol_year
raw_shard_root = atlas/ohlcv_raw_by_symbol_year
price_basis = tradable_raw
price_adjustment_status = raw_unadjusted_marcap
validation_status = usable_for_historical_calibration
```

The stock-web atlas max date is `2026-02-20`; every forward-window decision uses this manifest max date, not the current calendar date. The default basis remains raw/unadjusted marcap OHLC. Corporate-action contaminated windows are not used for positive weight calibration.

## 5. Historical Eligibility Gate

| case_id | symbol | entry_date | 180D window | corporate_action_window_status | calibration_usable | reason |
|---|---:|---:|---:|---|---:|---|
| R10L12-C30-KCCCON-20240327 | 021320 | 2024-03-27 | available | clean_180D_window | true | clean |
| R10L12-C30-HLDNI-20240327 | 014790 | 2024-03-27 | available | clean_180D_window | true | clean |
| R10L12-C30-SEOHEE-20240327 | 035890 | 2024-03-27 | available | clean_180D_window; 1Y usable, 2Y unavailable by profile last_date 2025-08-11 | true | clean |
| R10L12-C30-HANSHIN-20240327 | 004960 | 2024-03-27 | available | clean_180D_window | true | clean |
| R10L12-C30-HS-20240327 | 002460 | 2024-03-27 | available | clean_180D_window; 2024-07-10 name change noted, not treated as corporate-action contamination | true | clean |
| R10L12-C30-SAMBU-20240327 | 001470 | 2024-03-27 | blocked for positive calibration | share_count_shift_observed_in_2024_window; not used for positive weight calibration | false | share_count_shift_dilution_path_observed_not_profile_corporate_action_candidate |


## 6. Canonical Archetype Compression Map

```text
canonical_archetype_id = C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK
fine_archetype_id = SMALL_MID_CONSTRUCTOR_PF_MARGIN_LIQUIDITY_RESIDUAL
```

Compression logic: these are not separate permanent archetypes for each builder. They compress into one C30 subpattern: `policy/PF support + small/mid constructor balance-sheet survival + margin/cash conversion check`. The scoring implication should remain canonical-archetype-specific rather than global.

## 7. Case Selection Summary

| case_id | symbol | company | case_role | polarity | entry_date | entry_price | MFE_90D | MAE_90D | MFE_180D | MAE_180D | current_profile_verdict | usable |
|---|---:|---|---|---|---:|---:|---:|---:|---:|---:|---|---:|
| R10L12-C30-KCCCON-20240327 | 021320 | KCC건설 | failed_rerating | counterexample | 2024-03-27 | 4,625 | 24.32% | -9.84% | 24.32% | -15.68% | current_profile_false_positive | true |
| R10L12-C30-HLDNI-20240327 | 014790 | HL D&I | structural_success | positive | 2024-03-27 | 2,010 | 36.07% | -4.08% | 43.28% | -4.08% | current_profile_correct | true |
| R10L12-C30-SEOHEE-20240327 | 035890 | 서희건설 | missed_structural | positive | 2024-03-27 | 1,336 | 5.16% | -10.93% | 25.75% | -10.93% | current_profile_missed_structural | true |
| R10L12-C30-HANSHIN-20240327 | 004960 | 한신공영 | high_mae_success | positive | 2024-03-27 | 6,720 | 12.50% | -8.33% | 18.60% | -8.63% | current_profile_too_late | true |
| R10L12-C30-HS-20240327 | 002460 | HS화성 | failed_rerating | counterexample | 2024-03-27 | 10,030 | 0.70% | -12.66% | 0.70% | -17.05% | current_profile_false_positive | true |
| R10L12-C30-SAMBU-20240327 | 001470 | 삼부토건 | 4C_success | counterexample | 2024-03-27 | 1,993 | 8.63% | -42.30% | 8.63% | -77.92% | current_profile_4C_too_late | false |

## 8. Positive vs Counterexample Balance

```text
positive_case_count = 3
counterexample_count = 3
calibration_usable_case_count = 5
calibration_usable_trigger_count = 5
minimum_positive_case_count = pass
minimum_counterexample_count = pass
minimum_calibration_usable_case_count = pass
```

Positive cases are HL D&I, 서희건설, and 한신공영. Counterexamples are KCC건설, HS화성, and 삼부토건. The distinction is not “construction went up or down”; it is whether policy liquidity turned into a durable cash/margin path or only lit a short fuse under a fragile structure.

## 9. Evidence Source Map

| evidence date | source family | C30 interpretation |
|---:|---|---|
| 2024-03-27 | Korea builder liquidity support / guarantee expansion news | Stage2-Actionable macro support for the sector, not Stage3 proof by itself. |
| 2024-05-13 | PF assessment/tougher classification news | Red-team pressure: project-level PF stress can turn policy support into forced cleanup rather than rerating. |
| 2024-07-03 | Construction-sector support package / infrastructure-policy support | Reinforces policy optionality but still does not replace margin/cash conversion evidence. |
| 2024 stock-web OHLC rows | Actual tradable_raw price path | Used for entry price, MFE, MAE, peak, and post-peak drawdown. |

## 10. Price Data Source Map

| symbol | company | profile_path | price_shard_path | profile_summary |
|---:|---|---|---|---|
| 021320 | KCC건설 | atlas/symbol_profiles/021/021320.json | atlas/ohlcv_tradable_by_symbol_year/021/021320/2024.csv | active_like; KOSDAQ; first_date 2001-08-21; last_date 2026-02-20; corporate action candidates only 2014-05-12 and 2014-07-09, outside tested window. |
| 014790 | HL D&I | atlas/symbol_profiles/014/014790.json | atlas/ohlcv_tradable_by_symbol_year/014/014790/2024.csv | active_like; KOSPI; first_date 1995-05-03; last_date 2026-02-20; corporate action candidates stop in 2012, outside tested window. |
| 035890 | 서희건설 | atlas/symbol_profiles/035/035890.json | atlas/ohlcv_tradable_by_symbol_year/035/035890/2024.csv | active_like; KOSDAQ; first_date 1999-12-24; tradable last_date 2025-08-11; corporate action candidates stop in 2012, outside tested window. |
| 004960 | 한신공영 | atlas/symbol_profiles/004/004960.json | atlas/ohlcv_tradable_by_symbol_year/004/004960/2024.csv | active_like; KOSPI; first_date 1995-05-02; last_date 2026-02-20; corporate action candidates end in 2002, outside tested window. |
| 002460 | HS화성 | atlas/symbol_profiles/002/002460.json | atlas/ohlcv_tradable_by_symbol_year/002/002460/2024.csv | active_like; KOSPI; first_date 1995-05-02; last_date 2026-02-20; name changed from 화성산업 to HS화성 on 2024-07-10; corporate action candidates are historical and outside tested window. |
| 001470 | 삼부토건 | atlas/symbol_profiles/001/001470.json | atlas/ohlcv_tradable_by_symbol_year/001/001470/2024.csv | active_like by profile, but tradable last_date 2025-03-31 and 2024 shard shows material share-count changes. Used only as 4C risk overlay / narrative-only row. |


## 11. Case-by-Case Trigger Grid

| trigger_id | symbol | trigger_type | trigger_date | entry_date | evidence fields | outcome | current verdict |
|---|---:|---|---:|---:|---|---|---|
| R10L12-C30-KCCCON-20240327-T1 | 021320 | Stage2-Actionable | 2024-03-27 | 2024-03-27 | stage2=public_event_or_disclosure,policy_or_regulatory_optionality,relative_strength; stage3=financial_visibility; 4B=price_only_local_peak,positioning_overheat; 4C=none | price_only_policy_spike_failed_rerating | current_profile_false_positive |
| R10L12-C30-HLDNI-20240327-T1 | 014790 | Stage2-Actionable | 2024-03-27 | 2024-03-27 | stage2=public_event_or_disclosure,policy_or_regulatory_optionality,relative_strength; stage3=financial_visibility,low_red_team_risk; 4B=price_only_local_peak; 4C=none | delayed_structural_success_clean_MAE | current_profile_correct |
| R10L12-C30-SEOHEE-20240327-T1 | 035890 | Stage2-Actionable | 2024-03-27 | 2024-03-27 | stage2=public_event_or_disclosure,policy_or_regulatory_optionality,relative_strength; stage3=financial_visibility,low_red_team_risk; 4B=none; 4C=none | delayed_positive_survivor_rerating | current_profile_missed_structural |
| R10L12-C30-HANSHIN-20240327-T1 | 004960 | Stage2-Actionable | 2024-03-27 | 2024-03-27 | stage2=public_event_or_disclosure,policy_or_regulatory_optionality,relative_strength; stage3=financial_visibility; 4B=price_only_local_peak; 4C=none | positive_high_MAE_success | current_profile_too_late |
| R10L12-C30-HS-20240327-T1 | 002460 | Stage2-Actionable | 2024-03-27 | 2024-03-27 | stage2=public_event_or_disclosure,policy_or_regulatory_optionality; stage3=none; 4B=none; 4C=thesis_evidence_broken | failed_rerating_low_MFE | current_profile_false_positive |
| R10L12-C30-SAMBU-20240327-4C | 001470 | 4C-Watch | 2024-03-27 | 2024-03-27 | stage2=public_event_or_disclosure,policy_or_regulatory_optionality,relative_strength; stage3=none; 4B=price_only_local_peak,valuation_blowoff,positioning_overheat; 4C=accounting_or_trust_break,forced_liquidation_or_crash,thesis_evidence_broken | price_only_blowoff_then_4C_crash | current_profile_4C_too_late |


## 12. Trigger-Level OHLC Backtest Tables

| trigger_id | symbol | entry_date | entry_price | MFE_30D | MFE_90D | MFE_180D | MAE_30D | MAE_90D | MAE_180D | peak_date | peak_price | drawdown_after_peak | usable |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| R10L12-C30-KCCCON-20240327-T1 | 021320 | 2024-03-27 | 4,625 | 24.32% | 24.32% | 24.32% | -6.81% | -9.84% | -15.68% | 2024-04-08 | 5,750 | -32.17% | true |
| R10L12-C30-HLDNI-20240327-T1 | 014790 | 2024-03-27 | 2,010 | 1.74% | 36.07% | 43.28% | -4.08% | -4.08% | -4.08% | 2024-08-23 | 2,880 | -27.78% | true |
| R10L12-C30-SEOHEE-20240327-T1 | 035890 | 2024-03-27 | 1,336 | 5.16% | 5.16% | 25.75% | -1.80% | -10.93% | -10.93% | 2024-12-18 | 1,680 | -5.89% | true |
| R10L12-C30-HANSHIN-20240327-T1 | 004960 | 2024-03-27 | 6,720 | 3.12% | 12.50% | 18.60% | -8.33% | -8.33% | -8.63% | 2024-11-12 | 7,970 | -22.96% | true |
| R10L12-C30-HS-20240327-T1 | 002460 | 2024-03-27 | 10,030 | 0.70% | 0.70% | 0.70% | -5.38% | -12.66% | -17.05% | 2024-03-28 | 10,100 | -17.62% | true |
| R10L12-C30-SAMBU-20240327-4C | 001470 | 2024-03-27 | 1,993 | 8.63% | 8.63% | 8.63% | -37.53% | -42.30% | -77.92% | 2024-03-29 | 2,165 | -79.68% | false |

## 13. Current Calibrated Profile Stress Test

1. The current profile would correctly treat the March 2024 policy event as Stage2-Actionable, but it still risks overpromoting C30 names when policy liquidity is not paired with margin/cash evidence.
2. KCC건설 and HS화성 show the residual false-positive path: policy support appears, price lifts or holds briefly, but MFE/MAE alignment remains weak.
3. HL D&I, 서희건설, and 한신공영 show the survivor path: the correct signal is not raw price excitement but whether the builder remains tradable, avoids thesis break, and later shows financial visibility.
4. 삼부토건 is a 4C warning example: price-only upside before a collapse should not be retroactively counted as a successful Stage2/Stage3 signal.

| symbol | current profile verdict | actual path | stress-test conclusion |
|---:|---|---|---|
| 021320 | current_profile_false_positive | price_only_policy_spike_failed_rerating with 180D MFE 24.32% / MAE -15.68% | error |
| 014790 | current_profile_correct | delayed_structural_success_clean_MAE with 180D MFE 43.28% / MAE -4.08% | aligned |
| 035890 | current_profile_missed_structural | delayed_positive_survivor_rerating with 180D MFE 25.75% / MAE -10.93% | error |
| 004960 | current_profile_too_late | positive_high_MAE_success with 180D MFE 18.60% / MAE -8.63% | error |
| 002460 | current_profile_false_positive | failed_rerating_low_MFE with 180D MFE 0.70% / MAE -17.05% | error |
| 001470 | current_profile_4C_too_late | price_only_blowoff_then_4C_crash with 180D MFE 8.63% / MAE -77.92% | error |


## 14. Stage2 / Yellow / Green Comparison

No case receives a confirmed Stage3-Green trigger on the original 2024-03-27 evidence date. That is the main lesson. C30 can move violently at Stage2, but Green needs more than liquidity support: it needs confirmed revision, margin bridge, cash conversion, backlog quality, or a visible PF resolution route.

```text
green_lateness_ratio = not_applicable
reason = no_confirmed_Stage3_Green_trigger_on_original_policy_liquidity_date
stage2_actionable_bonus = existing_axis_kept
stage3_yellow_total_min = existing_axis_kept
stage3_green_total_min = existing_axis_kept
stage3_green_revision_min = existing_axis_strengthened_for_C30_by_margin_cash_conversion_requirement
```

## 15. 4B Local vs Full-window Timing Audit

| symbol | local_peak_proxy | full_window_peak_proxy | four_b_local_peak_proximity | four_b_full_window_peak_proximity | verdict |
|---:|---:|---:|---:|---:|---|
| 021320 | 2024-04-08 / 5,750 | 2024-04-08 / 5,750 | 1.00 | 1.00 | price-only peak; full 4B requires non-price evidence. |
| 014790 | 2024-08-23 / 2,880 | 2024-08-23 / 2,880 | 1.00 | 1.00 | good risk overlay, but no non-price 4B thesis break. |
| 035890 | 2024-12-18 / 1,680 | 2024-12-18 / 1,680 | not_applicable | not_applicable | no mature full 4B in observed window. |
| 004960 | 2024-11-12 / 7,970 | 2024-11-12 / 7,970 | 1.00 | 1.00 | high-MAE survivor; price-only peak should be risk overlay. |
| 002460 | 2024-03-28 / 10,100 | 2024-03-28 / 10,100 | 1.00 | 1.00 | failed rerating; early peak not a positive signal. |
| 001470 | 2024-03-29 / 2,165 | 2024-03-29 / 2,165 | 1.00 | 1.00 | 4C watch; not positive calibration. |

## 16. 4C Protection Audit

삼부토건 is the only explicit 4C overlay case in this loop. Its 180D MAE of -77.92% after the March 2024 entry proxy, together with observed share-count changes in the 2024 shard, makes it a protection case rather than a positive calibration case. HS화성 is a softer failed-rerating case; it does not require hard 4C but supports a C30 low-MFE cap.

```text
four_c_protection_label = hard_4c_success for 001470
hard_4c_thesis_break_routes_to_4c = existing_axis_strengthened
```

## 17. Sector-Specific Rule Candidate

```text
rule_scope = sector_specific
sector_specific_rule_candidate = true
candidate = L9_small_mid_constructor_policy_liquidity_survivor_split
```

Proposed sector rule: in L9 construction, a policy/PF liquidity event can create Stage2-Actionable optionality, but it should not become Yellow/Green unless paired with at least one of the following: explicit PF refinancing progress, cash-flow/margin bridge, backlog collection visibility, or low red-team risk. Otherwise the signal stays Stage2-Watch or becomes a 4B/4C overlay if price moves too far first.

## 18. Canonical-Archetype Rule Candidate

```text
rule_scope = canonical_archetype_specific
canonical_archetype_rule_candidate = true
canonical_archetype_id = C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK
```

C30-specific shadow rule: `policy_support_score` is capped unless `margin_bridge_score`, `financial_visibility`, or `accounting_trust_risk` clears the red-team check. This is not a global rule because many other sectors convert policy events differently; C30 uniquely mixes asset-cycle liquidity, project-level PF, and hidden balance-sheet stress.

## 19. Before / After Backtest Comparison

| profile_id | profile_scope | profile_hypothesis | changed_axes | changed_thresholds | eligible_trigger_count | selected_entry_trigger_per_case | avg_MFE_90D_pct | avg_MAE_90D_pct | avg_MFE_180D_pct | avg_MAE_180D_pct | false_positive_rate | missed_structural_count | late_green_count | avg_green_lateness_ratio | avg_four_b_local_peak_proximity | avg_four_b_full_window_peak_proximity | score_return_alignment_verdict |
|---|---|---|---|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---|---:|---:|---|
| P0 | e2r_2_1_stock_web_calibrated_proxy | current calibrated profile; no C30-specific survivor/false-positive split | none | current thresholds | 5 | 021320|014790|035890|004960|002460 | 15.35 | -9.17 | 22.97 | -11.23 | 0.4 | 1 | 2 | not_applicable | 0.8 | 0.72 | mixed: policy-support false positives remain |
| P0b | e2r_2_0_baseline_reference | rollback reference; looser early promotion | weaker Green and 4B guards | baseline | 5 | same | 15.35 | -9.17 | 22.97 | -11.23 | 0.6 | 1 | 1 | not_applicable | 0.74 | 0.67 | worse: false positives increase |
| P1 | sector_specific_candidate_profile | L9 small/mid construction adds PF-liquidity and high-MAE guard | C30_high_MAE_liquidity_guard + C30_theme_without_margin_cap | shadow only | 5 | 014790|035890|004960 promoted; 021320/002460 capped | 18.38 | -7.78 | 29.21 | -7.88 | 0.2 | 0 | 1 | not_applicable | 0.66 | 0.6 | better: retains survivor positives and caps theme bounces |
| P2 | canonical_archetype_candidate_profile | C30 requires margin/cash visibility before Yellow/Green; policy support alone is Stage2 only | C30_margin_cash_conversion_bonus + C30_policy_only_cap | shadow only | 5 | 014790|035890 selected; 004960 watch; 021320/002460 blocked | 20.61 | -7.77 | 34.52 | -7.51 | 0.0 | 1 | 0 | not_applicable | 0.54 | 0.5 | best precision, slightly misses high-MAE survivor |
| P3 | counterexample_guard_profile | Hard guard against price-only, dilution, accounting trust, and share-count shocks | 4C_trust_break_guard + price_only_blowoff_blocks_positive_stage strengthened in C30 | shadow only | 6 | excludes 001470 from positive; marks 021320/002460 risk | 15.35 | -9.17 | 22.97 | -11.23 | 0.0 | 1 | 0 | not_applicable | 0.48 | 0.43 | best protection, conservative |

## 20. Score-Return Alignment Matrix

| symbol | before_score | before_label | after_score | after_label | MFE_90D | MAE_90D | alignment |
|---:|---:|---|---:|---|---:|---:|---|
| 021320 | 76 | Stage3-Yellow | 66 | Stage2-Actionable | 24.32% | -9.84% | price_only_policy_spike_failed_rerating |
| 014790 | 78 | Stage3-Yellow | 78 | Stage3-Yellow | 36.07% | -4.08% | delayed_structural_success_clean_MAE |
| 035890 | 66 | Stage2-Watch | 74 | Stage2-Actionable | 5.16% | -10.93% | delayed_positive_survivor_rerating |
| 004960 | 68 | Stage2-Watch | 70 | Stage2-Actionable | 12.50% | -8.33% | positive_high_MAE_success |
| 002460 | 73 | Stage2-Actionable | 58 | Stage2-Watch | 0.70% | -12.66% | failed_rerating_low_MFE |
| 001470 | 63 | Stage2-Actionable | 36 | 4C-Watch | 8.63% | -42.30% | price_only_blowoff_then_4C_crash |


## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive_case_count | counterexample_count | 4B_case_count | 4C_case_count | new_independent_case_count | reused_case_count | calibration_usable_trigger_count | representative_trigger_count | current_profile_error_count | sector_rule_candidate | canonical_rule_candidate | coverage_gap_after_this_loop |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| L9_CONSTRUCTION_REALESTATE_HOUSING | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | SMALL_MID_CONSTRUCTOR_PF_MARGIN_LIQUIDITY_RESIDUAL | 3 | 3 | 3 | 1 | 5 | 0 | 5 | 5 | 5 | true | true | C30 still needs more post-2024 holdout and official disclosure mapping, but symbol/trigger coverage gap is reduced |

## 22. Residual Contribution Summary

```text
new_independent_case_count: 5
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 6
new_canonical_archetype_count: 0
new_fine_archetype_count: 1
new_trigger_family_count: 6
tested_existing_calibrated_axes: stage2_actionable_evidence_bonus; stage3_green_total_min; price_only_blowoff_blocks_positive_stage; full_4b_requires_non_price_evidence; hard_4c_thesis_break_routes_to_4c
residual_error_types_found: policy_liquidity_false_positive; small_mid_survivor_missed_structural; high_MAE_positive_needs_guard; share_count_or_trust_break_4C_overlay
new_axis_proposed: C30_margin_cash_conversion_survivor_bonus_shadow; C30_policy_theme_without_margin_cap; C30_high_MAE_liquidity_guard
existing_axis_strengthened: price_only_blowoff_blocks_positive_stage; full_4b_requires_non_price_evidence; hard_4c_thesis_break_routes_to_4c
existing_axis_weakened: none
existing_axis_kept: stage2_actionable_evidence_bonus; stage3_yellow_total_min; stage3_green_total_min
sector_specific_rule_candidate: true
canonical_archetype_rule_candidate: true
no_new_signal_reason: null
loop_contribution_label: canonical_archetype_rule_candidate
do_not_propose_new_weight_delta: false
```

## 23. Validation Scope / Non-Validation Scope

Validated scope:

```text
- Historical trigger-level calibration only.
- Stock-web tradable_raw OHLC for entry, MFE, MAE, peak, and drawdown.
- C30 sector/archetype-specific shadow rule discovery.
- Positive/counterexample balance inside scheduled R10.
```

Non-validation scope:

```text
- No live candidate scan.
- No investment recommendation.
- No stock_agent source-code inspection.
- No production scoring patch.
- No broker or auto-trading action.
```

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,C30_margin_cash_conversion_survivor_bonus,canonical_archetype_specific,L9_CONSTRUCTION_REALESTATE_HOUSING,C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK,0,1,+1,HL D&I, 서희건설, and 한신공영 show that clean survival plus financial visibility can work even when Green confirmation is late.,raises delayed survivor positives without promoting policy-only bounces,R10L12-C30-HLDNI-20240327-T1|R10L12-C30-SEOHEE-20240327-T1|R10L12-C30-HANSHIN-20240327-T1,3,3,0,medium,canonical_archetype_shadow_only,not production; post-calibrated residual
shadow_weight,C30_policy_theme_without_margin_cap,canonical_archetype_specific,L9_CONSTRUCTION_REALESTATE_HOUSING,C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK,0,1,+1 guard,KCC건설 and HS화성 show that policy liquidity alone is not enough for durable rerating; 삼부토건 adds 4C trust-break caution.,cuts false positives and routes price-only spikes to 4B/4C watch,R10L12-C30-KCCCON-20240327-T1|R10L12-C30-HS-20240327-T1|R10L12-C30-SAMBU-20240327-4C,2,2,3,medium,canonical_archetype_shadow_only,not production; post-calibrated residual
```

## 25. Machine-Readable Rows

### price_source_validation
```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration"}
```

### case rows
```jsonl
{"row_type": "case", "case_id": "R10L12-C30-KCCCON-20240327", "symbol": "021320", "company_name": "KCC건설", "round": "R10", "loop": "12", "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "fine_archetype_id": "SMALL_MID_CONSTRUCTOR_PF_MARGIN_LIQUIDITY_RESIDUAL", "case_type": "failed_rerating", "positive_or_counterexample": "counterexample", "best_trigger": "Stage2-Actionable policy-liquidity basket", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "price_only_policy_spike_failed_rerating", "current_profile_verdict": "current_profile_false_positive", "price_source": "Songdaiki/stock-web", "notes": "2024-03-27 Korea builder liquidity-support event gave sector beta, but KCC건설 made a price-only spike and then bled below entry for months without confirmed margin/revision bridge."}
{"row_type": "case", "case_id": "R10L12-C30-HLDNI-20240327", "symbol": "014790", "company_name": "HL D&I", "round": "R10", "loop": "12", "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "fine_archetype_id": "SMALL_MID_CONSTRUCTOR_PF_MARGIN_LIQUIDITY_RESIDUAL", "case_type": "structural_success", "positive_or_counterexample": "positive", "best_trigger": "Stage2-Actionable liquidity survival + later margin path", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "delayed_structural_success_clean_MAE", "current_profile_verdict": "current_profile_correct", "price_source": "Songdaiki/stock-web", "notes": "Same policy-liquidity event produced only slow initial motion, but HL D&I later converted into a clean 180D path with contained MAE and strong MFE."}
{"row_type": "case", "case_id": "R10L12-C30-SEOHEE-20240327", "symbol": "035890", "company_name": "서희건설", "round": "R10", "loop": "12", "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "fine_archetype_id": "SMALL_MID_CONSTRUCTOR_PF_MARGIN_LIQUIDITY_RESIDUAL", "case_type": "missed_structural", "positive_or_counterexample": "positive", "best_trigger": "Stage2 survivor with delayed rerating", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "delayed_positive_survivor_rerating", "current_profile_verdict": "current_profile_missed_structural", "price_source": "Songdaiki/stock-web", "notes": "서희건설 did not explode immediately, but the 180D window showed a survivor-style rerating path after a tolerable but real August drawdown."}
{"row_type": "case", "case_id": "R10L12-C30-HANSHIN-20240327", "symbol": "004960", "company_name": "한신공영", "round": "R10", "loop": "12", "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "fine_archetype_id": "SMALL_MID_CONSTRUCTOR_PF_MARGIN_LIQUIDITY_RESIDUAL", "case_type": "high_mae_success", "positive_or_counterexample": "positive", "best_trigger": "Stage2 survivor with high-MAE guard", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "positive_high_MAE_success", "current_profile_verdict": "current_profile_too_late", "price_source": "Songdaiki/stock-web", "notes": "한신공영 gave a valid but uncomfortable survivor path: upside arrived, but the interim and post-peak drawdowns require a C30 high-MAE liquidity guard rather than an easy Green label."}
{"row_type": "case", "case_id": "R10L12-C30-HS-20240327", "symbol": "002460", "company_name": "HS화성", "round": "R10", "loop": "12", "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "fine_archetype_id": "SMALL_MID_CONSTRUCTOR_PF_MARGIN_LIQUIDITY_RESIDUAL", "case_type": "failed_rerating", "positive_or_counterexample": "counterexample", "best_trigger": "Policy support without margin conversion", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "failed_rerating_low_MFE", "current_profile_verdict": "current_profile_false_positive", "price_source": "Songdaiki/stock-web", "notes": "HS화성/화성산업 stayed liquid but did not convert the policy-support narrative into a durable rerating. The 180D path was essentially all drawdown with negligible MFE."}
{"row_type": "case", "case_id": "R10L12-C30-SAMBU-20240327", "symbol": "001470", "company_name": "삼부토건", "round": "R10", "loop": "12", "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "fine_archetype_id": "SMALL_MID_CONSTRUCTOR_PF_MARGIN_LIQUIDITY_RESIDUAL", "case_type": "4C_success", "positive_or_counterexample": "counterexample", "best_trigger": "4C thesis-break / dilution watch", "calibration_usable": false, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.25, "score_price_alignment": "price_only_blowoff_then_4C_crash", "current_profile_verdict": "current_profile_4C_too_late", "price_source": "Songdaiki/stock-web", "notes": "삼부토건 is retained as a narrative-only 4C overlay case. The price path had early upside, but share-count shifts and later collapse make it unsuitable for positive weight calibration."}
```

### trigger rows
```jsonl
{"row_type": "trigger", "trigger_id": "R10L12-C30-KCCCON-20240327-T1", "case_id": "R10L12-C30-KCCCON-20240327", "symbol": "021320", "company_name": "KCC건설", "round": "R10", "loop": "12", "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "fine_archetype_id": "SMALL_MID_CONSTRUCTOR_PF_MARGIN_LIQUIDITY_RESIDUAL", "sector": "건설·부동산·건자재", "primary_archetype": "construction_PF_balance_sheet_break", "loop_objective": "coverage_gap_fill|counterexample_mining|residual_false_positive_mining|sector_specific_rule_discovery|canonical_archetype_compression|4B_non_price_requirement_stress_test", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-03-27", "evidence_available_at_that_date": "2024-03-27 Korea builder liquidity-support event gave sector beta, but KCC건설 made a price-only spike and then bled below entry for months without confirmed margin/revision bridge.", "evidence_source": "Reuters 2024-03-27 builder liquidity support + Reuters 2024-05-13 PF assessment stress + Songdaiki/stock-web OHLC; not live scan", "stage2_evidence_fields": ["public_event_or_disclosure", "policy_or_regulatory_optionality", "relative_strength"], "stage3_evidence_fields": ["financial_visibility"], "stage4b_evidence_fields": ["price_only_local_peak", "positioning_overheat"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/021/021320/2024.csv", "profile_path": "atlas/symbol_profiles/021/021320.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-03-27", "entry_price": 4625, "MFE_30D_pct": 24.32, "MFE_90D_pct": 24.32, "MFE_180D_pct": 24.32, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -6.81, "MAE_90D_pct": -9.84, "MAE_180D_pct": -15.68, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-04-08", "peak_price": 5750, "drawdown_after_peak_pct": -32.17, "green_lateness_ratio": "not_applicable:no_confirmed_Stage3_Green_trigger", "four_b_local_peak_proximity": 1.0, "four_b_full_window_peak_proximity": 1.0, "four_b_timing_verdict": "price_only_peak_is_overlay_not_positive_promotion", "four_b_evidence_type": ["price_only_local_peak", "positioning_overheat"], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "price_only_policy_spike_failed_rerating", "current_profile_verdict": "current_profile_false_positive", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R10L12-C30-KCCCON-20240327:2024-03-27:4625", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "R10L12-C30-HLDNI-20240327-T1", "case_id": "R10L12-C30-HLDNI-20240327", "symbol": "014790", "company_name": "HL D&I", "round": "R10", "loop": "12", "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "fine_archetype_id": "SMALL_MID_CONSTRUCTOR_PF_MARGIN_LIQUIDITY_RESIDUAL", "sector": "건설·부동산·건자재", "primary_archetype": "construction_PF_balance_sheet_break", "loop_objective": "coverage_gap_fill|counterexample_mining|residual_false_positive_mining|sector_specific_rule_discovery|canonical_archetype_compression|4B_non_price_requirement_stress_test", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-03-27", "evidence_available_at_that_date": "Same policy-liquidity event produced only slow initial motion, but HL D&I later converted into a clean 180D path with contained MAE and strong MFE.", "evidence_source": "Reuters 2024-03-27 builder liquidity support + Reuters 2024-05-13 PF assessment stress + Songdaiki/stock-web OHLC; not live scan", "stage2_evidence_fields": ["public_event_or_disclosure", "policy_or_regulatory_optionality", "relative_strength"], "stage3_evidence_fields": ["financial_visibility", "low_red_team_risk"], "stage4b_evidence_fields": ["price_only_local_peak"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/014/014790/2024.csv", "profile_path": "atlas/symbol_profiles/014/014790.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-03-27", "entry_price": 2010, "MFE_30D_pct": 1.74, "MFE_90D_pct": 36.07, "MFE_180D_pct": 43.28, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -4.08, "MAE_90D_pct": -4.08, "MAE_180D_pct": -4.08, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": false, "peak_date": "2024-08-23", "peak_price": 2880, "drawdown_after_peak_pct": -27.78, "green_lateness_ratio": "not_applicable:no_confirmed_Stage3_Green_trigger", "four_b_local_peak_proximity": 1.0, "four_b_full_window_peak_proximity": 1.0, "four_b_timing_verdict": "price_only_peak_is_overlay_not_positive_promotion", "four_b_evidence_type": ["price_only_local_peak"], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "delayed_structural_success_clean_MAE", "current_profile_verdict": "current_profile_correct", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R10L12-C30-HLDNI-20240327:2024-03-27:2010", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "R10L12-C30-SEOHEE-20240327-T1", "case_id": "R10L12-C30-SEOHEE-20240327", "symbol": "035890", "company_name": "서희건설", "round": "R10", "loop": "12", "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "fine_archetype_id": "SMALL_MID_CONSTRUCTOR_PF_MARGIN_LIQUIDITY_RESIDUAL", "sector": "건설·부동산·건자재", "primary_archetype": "construction_PF_balance_sheet_break", "loop_objective": "coverage_gap_fill|counterexample_mining|residual_false_positive_mining|sector_specific_rule_discovery|canonical_archetype_compression|4B_non_price_requirement_stress_test", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-03-27", "evidence_available_at_that_date": "서희건설 did not explode immediately, but the 180D window showed a survivor-style rerating path after a tolerable but real August drawdown.", "evidence_source": "Reuters 2024-03-27 builder liquidity support + Reuters 2024-05-13 PF assessment stress + Songdaiki/stock-web OHLC; not live scan", "stage2_evidence_fields": ["public_event_or_disclosure", "policy_or_regulatory_optionality", "relative_strength"], "stage3_evidence_fields": ["financial_visibility", "low_red_team_risk"], "stage4b_evidence_fields": [], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/035/035890/2024.csv", "profile_path": "atlas/symbol_profiles/035/035890.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-03-27", "entry_price": 1336, "MFE_30D_pct": 5.16, "MFE_90D_pct": 5.16, "MFE_180D_pct": 25.75, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -1.8, "MAE_90D_pct": -10.93, "MAE_180D_pct": -10.93, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-12-18", "peak_price": 1680, "drawdown_after_peak_pct": -5.89, "green_lateness_ratio": "not_applicable:no_confirmed_Stage3_Green_trigger", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "not_applicable", "four_b_evidence_type": [], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "delayed_positive_survivor_rerating", "current_profile_verdict": "current_profile_missed_structural", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window; 1Y usable, 2Y unavailable by profile last_date 2025-08-11", "same_entry_group_id": "R10L12-C30-SEOHEE-20240327:2024-03-27:1336", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "R10L12-C30-HANSHIN-20240327-T1", "case_id": "R10L12-C30-HANSHIN-20240327", "symbol": "004960", "company_name": "한신공영", "round": "R10", "loop": "12", "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "fine_archetype_id": "SMALL_MID_CONSTRUCTOR_PF_MARGIN_LIQUIDITY_RESIDUAL", "sector": "건설·부동산·건자재", "primary_archetype": "construction_PF_balance_sheet_break", "loop_objective": "coverage_gap_fill|counterexample_mining|residual_false_positive_mining|sector_specific_rule_discovery|canonical_archetype_compression|4B_non_price_requirement_stress_test", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-03-27", "evidence_available_at_that_date": "한신공영 gave a valid but uncomfortable survivor path: upside arrived, but the interim and post-peak drawdowns require a C30 high-MAE liquidity guard rather than an easy Green label.", "evidence_source": "Reuters 2024-03-27 builder liquidity support + Reuters 2024-05-13 PF assessment stress + Songdaiki/stock-web OHLC; not live scan", "stage2_evidence_fields": ["public_event_or_disclosure", "policy_or_regulatory_optionality", "relative_strength"], "stage3_evidence_fields": ["financial_visibility"], "stage4b_evidence_fields": ["price_only_local_peak"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/004/004960/2024.csv", "profile_path": "atlas/symbol_profiles/004/004960.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-03-27", "entry_price": 6720, "MFE_30D_pct": 3.12, "MFE_90D_pct": 12.5, "MFE_180D_pct": 18.6, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -8.33, "MAE_90D_pct": -8.33, "MAE_180D_pct": -8.63, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-11-12", "peak_price": 7970, "drawdown_after_peak_pct": -22.96, "green_lateness_ratio": "not_applicable:no_confirmed_Stage3_Green_trigger", "four_b_local_peak_proximity": 1.0, "four_b_full_window_peak_proximity": 1.0, "four_b_timing_verdict": "price_only_peak_is_overlay_not_positive_promotion", "four_b_evidence_type": ["price_only_local_peak"], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "positive_high_MAE_success", "current_profile_verdict": "current_profile_too_late", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R10L12-C30-HANSHIN-20240327:2024-03-27:6720", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "R10L12-C30-HS-20240327-T1", "case_id": "R10L12-C30-HS-20240327", "symbol": "002460", "company_name": "HS화성", "round": "R10", "loop": "12", "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "fine_archetype_id": "SMALL_MID_CONSTRUCTOR_PF_MARGIN_LIQUIDITY_RESIDUAL", "sector": "건설·부동산·건자재", "primary_archetype": "construction_PF_balance_sheet_break", "loop_objective": "coverage_gap_fill|counterexample_mining|residual_false_positive_mining|sector_specific_rule_discovery|canonical_archetype_compression|4B_non_price_requirement_stress_test", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-03-27", "evidence_available_at_that_date": "HS화성/화성산업 stayed liquid but did not convert the policy-support narrative into a durable rerating. The 180D path was essentially all drawdown with negligible MFE.", "evidence_source": "Reuters 2024-03-27 builder liquidity support + Reuters 2024-05-13 PF assessment stress + Songdaiki/stock-web OHLC; not live scan", "stage2_evidence_fields": ["public_event_or_disclosure", "policy_or_regulatory_optionality"], "stage3_evidence_fields": [], "stage4b_evidence_fields": [], "stage4c_evidence_fields": ["thesis_evidence_broken"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/002/002460/2024.csv", "profile_path": "atlas/symbol_profiles/002/002460.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-03-27", "entry_price": 10030, "MFE_30D_pct": 0.7, "MFE_90D_pct": 0.7, "MFE_180D_pct": 0.7, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -5.38, "MAE_90D_pct": -12.66, "MAE_180D_pct": -17.05, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-03-28", "peak_price": 10100, "drawdown_after_peak_pct": -17.62, "green_lateness_ratio": "not_applicable:no_confirmed_Stage3_Green_trigger", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "not_applicable", "four_b_evidence_type": [], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "failed_rerating_low_MFE", "current_profile_verdict": "current_profile_false_positive", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window; 2024-07-10 name change noted, not treated as corporate-action contamination", "same_entry_group_id": "R10L12-C30-HS-20240327:2024-03-27:10030", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "R10L12-C30-SAMBU-20240327-4C", "case_id": "R10L12-C30-SAMBU-20240327", "symbol": "001470", "company_name": "삼부토건", "round": "R10", "loop": "12", "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "fine_archetype_id": "SMALL_MID_CONSTRUCTOR_PF_MARGIN_LIQUIDITY_RESIDUAL", "sector": "건설·부동산·건자재", "primary_archetype": "construction_PF_balance_sheet_break", "loop_objective": "coverage_gap_fill|counterexample_mining|residual_false_positive_mining|sector_specific_rule_discovery|canonical_archetype_compression|4B_non_price_requirement_stress_test", "trigger_type": "4C-Watch", "trigger_date": "2024-03-27", "evidence_available_at_that_date": "삼부토건 is retained as a narrative-only 4C overlay case. The price path had early upside, but share-count shifts and later collapse make it unsuitable for positive weight calibration.", "evidence_source": "Reuters 2024-03-27 builder liquidity support + Reuters 2024-05-13 PF assessment stress + Songdaiki/stock-web OHLC; not live scan", "stage2_evidence_fields": ["public_event_or_disclosure", "policy_or_regulatory_optionality", "relative_strength"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["price_only_local_peak", "valuation_blowoff", "positioning_overheat"], "stage4c_evidence_fields": ["accounting_or_trust_break", "forced_liquidation_or_crash", "thesis_evidence_broken"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/001/001470/2024.csv", "profile_path": "atlas/symbol_profiles/001/001470.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-03-27", "entry_price": 1993, "MFE_30D_pct": 8.63, "MFE_90D_pct": 8.63, "MFE_180D_pct": 8.63, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -37.53, "MAE_90D_pct": -42.3, "MAE_180D_pct": -77.92, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-03-29", "peak_price": 2165, "drawdown_after_peak_pct": -79.68, "green_lateness_ratio": "not_applicable:no_confirmed_Stage3_Green_trigger", "four_b_local_peak_proximity": 1.0, "four_b_full_window_peak_proximity": 1.0, "four_b_timing_verdict": "price_only_peak_is_overlay_not_positive_promotion", "four_b_evidence_type": ["price_only_local_peak", "valuation_blowoff", "positioning_overheat"], "four_c_protection_label": "hard_4c_success", "trigger_outcome_label": "price_only_blowoff_then_4C_crash", "current_profile_verdict": "current_profile_4C_too_late", "calibration_usable": false, "forward_window_trading_days": 0, "calibration_block_reasons": ["share_count_shift_dilution_path_observed_not_profile_corporate_action_candidate"], "corporate_action_window_status": "share_count_shift_observed_in_2024_window; not used for positive weight calibration", "same_entry_group_id": "R10L12-C30-SAMBU-20240327:2024-03-27:1993", "dedupe_for_aggregate": false, "aggregate_group_role": "4C_overlay_only", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.25, "do_not_count_as_new_case": true}
```

### score_simulation rows
```jsonl
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy_to_C30_shadow", "case_id": "R10L12-C30-KCCCON-20240327", "trigger_id": "R10L12-C30-KCCCON-20240327-T1", "symbol": "021320", "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 4, "margin_bridge_score": 2, "revision_score": 1, "relative_strength_score": 8, "customer_quality_score": 1, "policy_or_regulatory_score": 9, "valuation_repricing_score": 5, "execution_risk_score": -4, "legal_or_contract_risk_score": -5, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 76, "stage_label_before": "Stage3-Yellow", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 4, "margin_bridge_score": 2, "revision_score": 1, "relative_strength_score": 8, "customer_quality_score": 1, "policy_or_regulatory_score": 9, "valuation_repricing_score": 5, "execution_risk_score": -4, "legal_or_contract_risk_score": -5, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 66, "stage_label_after": "Stage2-Actionable", "changed_components": ["margin_bridge_score", "execution_risk_score", "accounting_trust_risk_score", "policy_or_regulatory_score"], "component_delta_explanation": "C30 shadow profile separates policy liquidity from confirmed margin/cash conversion and routes price-only or dilution paths to risk overlay.", "MFE_90D_pct": 24.32, "MAE_90D_pct": -9.84, "score_return_alignment_label": "price_only_policy_spike_failed_rerating", "current_profile_verdict": "current_profile_false_positive"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy_to_C30_shadow", "case_id": "R10L12-C30-HLDNI-20240327", "trigger_id": "R10L12-C30-HLDNI-20240327-T1", "symbol": "014790", "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 5, "margin_bridge_score": 6, "revision_score": 4, "relative_strength_score": 7, "customer_quality_score": 1, "policy_or_regulatory_score": 8, "valuation_repricing_score": 4, "execution_risk_score": -2, "legal_or_contract_risk_score": -2, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 78, "stage_label_before": "Stage3-Yellow", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 5, "margin_bridge_score": 6, "revision_score": 4, "relative_strength_score": 7, "customer_quality_score": 1, "policy_or_regulatory_score": 8, "valuation_repricing_score": 4, "execution_risk_score": -2, "legal_or_contract_risk_score": -2, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 78, "stage_label_after": "Stage3-Yellow", "changed_components": ["margin_bridge_score", "execution_risk_score", "accounting_trust_risk_score", "policy_or_regulatory_score"], "component_delta_explanation": "C30 shadow profile separates policy liquidity from confirmed margin/cash conversion and routes price-only or dilution paths to risk overlay.", "MFE_90D_pct": 36.07, "MAE_90D_pct": -4.08, "score_return_alignment_label": "delayed_structural_success_clean_MAE", "current_profile_verdict": "current_profile_correct"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy_to_C30_shadow", "case_id": "R10L12-C30-SEOHEE-20240327", "trigger_id": "R10L12-C30-SEOHEE-20240327-T1", "symbol": "035890", "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 5, "margin_bridge_score": 5, "revision_score": 3, "relative_strength_score": 7, "customer_quality_score": 1, "policy_or_regulatory_score": 8, "valuation_repricing_score": 4, "execution_risk_score": -3, "legal_or_contract_risk_score": -2, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 66, "stage_label_before": "Stage2-Watch", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 5, "margin_bridge_score": 5, "revision_score": 3, "relative_strength_score": 7, "customer_quality_score": 1, "policy_or_regulatory_score": 8, "valuation_repricing_score": 4, "execution_risk_score": -3, "legal_or_contract_risk_score": -2, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 74, "stage_label_after": "Stage2-Actionable", "changed_components": ["margin_bridge_score", "execution_risk_score", "accounting_trust_risk_score", "policy_or_regulatory_score"], "component_delta_explanation": "C30 shadow profile separates policy liquidity from confirmed margin/cash conversion and routes price-only or dilution paths to risk overlay.", "MFE_90D_pct": 5.16, "MAE_90D_pct": -10.93, "score_return_alignment_label": "delayed_positive_survivor_rerating", "current_profile_verdict": "current_profile_missed_structural"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy_to_C30_shadow", "case_id": "R10L12-C30-HANSHIN-20240327", "trigger_id": "R10L12-C30-HANSHIN-20240327-T1", "symbol": "004960", "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 4, "margin_bridge_score": 4, "revision_score": 2, "relative_strength_score": 6, "customer_quality_score": 1, "policy_or_regulatory_score": 8, "valuation_repricing_score": 3, "execution_risk_score": -5, "legal_or_contract_risk_score": -3, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 68, "stage_label_before": "Stage2-Watch", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 4, "margin_bridge_score": 4, "revision_score": 2, "relative_strength_score": 6, "customer_quality_score": 1, "policy_or_regulatory_score": 8, "valuation_repricing_score": 3, "execution_risk_score": -5, "legal_or_contract_risk_score": -3, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 70, "stage_label_after": "Stage2-Actionable", "changed_components": ["margin_bridge_score", "execution_risk_score", "accounting_trust_risk_score", "policy_or_regulatory_score"], "component_delta_explanation": "C30 shadow profile separates policy liquidity from confirmed margin/cash conversion and routes price-only or dilution paths to risk overlay.", "MFE_90D_pct": 12.5, "MAE_90D_pct": -8.33, "score_return_alignment_label": "positive_high_MAE_success", "current_profile_verdict": "current_profile_too_late"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy_to_C30_shadow", "case_id": "R10L12-C30-HS-20240327", "trigger_id": "R10L12-C30-HS-20240327-T1", "symbol": "002460", "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 2, "margin_bridge_score": 1, "revision_score": 0, "relative_strength_score": 2, "customer_quality_score": 0, "policy_or_regulatory_score": 8, "valuation_repricing_score": 2, "execution_risk_score": -7, "legal_or_contract_risk_score": -4, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 73, "stage_label_before": "Stage2-Actionable", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 2, "margin_bridge_score": 1, "revision_score": 0, "relative_strength_score": 2, "customer_quality_score": 0, "policy_or_regulatory_score": 8, "valuation_repricing_score": 2, "execution_risk_score": -7, "legal_or_contract_risk_score": -4, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 58, "stage_label_after": "Stage2-Watch", "changed_components": ["margin_bridge_score", "execution_risk_score", "accounting_trust_risk_score", "policy_or_regulatory_score"], "component_delta_explanation": "C30 shadow profile separates policy liquidity from confirmed margin/cash conversion and routes price-only or dilution paths to risk overlay.", "MFE_90D_pct": 0.7, "MAE_90D_pct": -12.66, "score_return_alignment_label": "failed_rerating_low_MFE", "current_profile_verdict": "current_profile_false_positive"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy_to_C30_shadow", "case_id": "R10L12-C30-SAMBU-20240327", "trigger_id": "R10L12-C30-SAMBU-20240327-4C", "symbol": "001470", "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 1, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 9, "customer_quality_score": 0, "policy_or_regulatory_score": 7, "valuation_repricing_score": 7, "execution_risk_score": -12, "legal_or_contract_risk_score": -10, "dilution_cb_risk_score": -8, "accounting_trust_risk_score": -10}, "weighted_score_before": 63, "stage_label_before": "Stage2-Actionable", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 1, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 9, "customer_quality_score": 0, "policy_or_regulatory_score": 7, "valuation_repricing_score": 7, "execution_risk_score": -12, "legal_or_contract_risk_score": -10, "dilution_cb_risk_score": -8, "accounting_trust_risk_score": -10}, "weighted_score_after": 36, "stage_label_after": "4C-Watch", "changed_components": ["margin_bridge_score", "execution_risk_score", "accounting_trust_risk_score", "policy_or_regulatory_score"], "component_delta_explanation": "C30 shadow profile separates policy liquidity from confirmed margin/cash conversion and routes price-only or dilution paths to risk overlay.", "MFE_90D_pct": 8.63, "MAE_90D_pct": -42.3, "score_return_alignment_label": "price_only_blowoff_then_4C_crash", "current_profile_verdict": "current_profile_4C_too_late"}
```

### shadow_weight rows
```jsonl
{"row_type": "shadow_weight", "axis": "C30_margin_cash_conversion_survivor_bonus", "scope": "canonical_archetype_specific", "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "baseline_value": 0, "tested_value": 1, "delta": "+1", "reason": "HL D&I, 서희건설, and 한신공영 show that clean survival plus financial visibility can work even when Green confirmation is late.", "backtest_effect": "raises delayed survivor positives without promoting policy-only bounces", "trigger_ids": "R10L12-C30-HLDNI-20240327-T1|R10L12-C30-SEOHEE-20240327-T1|R10L12-C30-HANSHIN-20240327-T1", "calibration_usable_count": 3, "new_independent_case_count": 3, "counterexample_count": 0, "confidence": "medium", "proposal_type": "canonical_archetype_shadow_only", "notes": "not production; post-calibrated residual"}
{"row_type": "shadow_weight", "axis": "C30_policy_theme_without_margin_cap", "scope": "canonical_archetype_specific", "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "baseline_value": 0, "tested_value": 1, "delta": "+1 guard", "reason": "KCC건설 and HS화성 show that policy liquidity alone is not enough for durable rerating; 삼부토건 adds 4C trust-break caution.", "backtest_effect": "cuts false positives and routes price-only spikes to 4B/4C watch", "trigger_ids": "R10L12-C30-KCCCON-20240327-T1|R10L12-C30-HS-20240327-T1|R10L12-C30-SAMBU-20240327-4C", "calibration_usable_count": 2, "new_independent_case_count": 2, "counterexample_count": 3, "confidence": "medium", "proposal_type": "canonical_archetype_shadow_only", "notes": "not production; post-calibrated residual"}
```

### residual_contribution row
```jsonl
{"row_type": "residual_contribution", "round": "R10", "loop": "12", "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "scheduled_round": "R10", "scheduled_loop": "12", "round_schedule_status": "valid", "round_sector_consistency": "pass", "new_independent_case_count": 5, "reused_case_count": 0, "new_symbol_count": 6, "same_archetype_new_symbol_count": 6, "same_archetype_new_trigger_family_count": 6, "new_trigger_family_count": 6, "positive_case_count": 3, "counterexample_count": 3, "current_profile_error_count": 5, "tested_existing_calibrated_axes": ["stage2_actionable_evidence_bonus", "stage3_green_total_min", "price_only_blowoff_blocks_positive_stage", "full_4b_requires_non_price_evidence", "hard_4c_thesis_break_routes_to_4c"], "residual_error_types_found": ["policy_liquidity_false_positive", "small_mid_survivor_missed_structural", "high_MAE_positive_needs_guard", "share_count_or_trust_break_4C_overlay"], "loop_contribution_label": "canonical_archetype_rule_candidate", "do_not_propose_new_weight_delta": false}
```

### narrative_only rows
```jsonl
{"row_type": "narrative_only", "case_id": "R10L12-C30-SAMBU-20240327", "symbol": "001470", "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "reason": "share_count_shift_dilution_path_observed_in_2024_window; useful as 4C guardrail but not positive weight calibration", "price_source": "Songdaiki/stock-web", "usage": "4C_risk_overlay_not_positive_weight"}
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
completed_round = R10
completed_loop = 12
next_round = R11
next_loop = 12
round_schedule_status = valid
round_sector_consistency = pass
```

## 28. Source Notes

Primary price source: Songdaiki/stock-web `atlas/manifest.json`, `atlas/schema.json`, `atlas/universe/all_symbols.csv`, symbol profiles, and 2024 tradable OHLC shards. Evidence context used for trigger interpretation includes historical Reuters reports on Korea's March 2024 builder liquidity support, May 2024 PF assessment/toughened project evaluation, and July 2024 construction-sector support package. These notes are used only for historical calibration context and are not investment advice.

