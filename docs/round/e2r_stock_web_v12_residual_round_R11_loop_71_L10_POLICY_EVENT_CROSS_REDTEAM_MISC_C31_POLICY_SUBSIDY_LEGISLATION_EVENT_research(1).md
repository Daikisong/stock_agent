# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
research_session = post_calibrated_sector_archetype_residual_research
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
scheduled_round = R11
scheduled_loop = 71
large_sector_id = L10_POLICY_EVENT_CROSS_REDTEAM_MISC
canonical_archetype_id = C31_POLICY_SUBSIDY_LEGISLATION_EVENT
fine_archetype_id = VALUEUP_POLICY_AND_PF_STABILIZATION_EVENT_BRIDGE
loop_objective = residual_false_positive_mining | 4C_thesis_break_timing_test | sector_specific_rule_discovery | counterexample_mining | coverage_gap_fill
production_scoring_changed = false
shadow_weight_only = true
handoff_prompt_embedded = true
handoff_prompt_executed_now = false
stock_agent_code_access_allowed = false
stock_agent_code_patch_allowed = false
stock_agent_live_scan_allowed = false
current_stock_discovery_allowed = false
```

This loop adds 4 calibration-usable independent cases, 2 counterexamples, and 3 residual errors for R11/L10_POLICY_EVENT_CROSS_REDTEAM_MISC/C31_POLICY_SUBSIDY_LEGISLATION_EVENT. A fifth case is kept as narrative-only 4C/liquidity-break context because the stock-web profile flags a 2024 corporate-action candidate inside or near the affected forward window.

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

The stress question for this loop is not whether a generic policy event can move prices. The question is whether a policy event becomes calibration-useful only after it attaches to a company-level bridge: executed capital return, balance-sheet repair, project visibility, margin bridge, or a legally binding subsidy/legislation route. Without that bridge, the same policy headline behaves like a match in wet grass: bright for a moment, then gone.

## 2. Round / Large Sector / Canonical Archetype Scope

| field | value |
|---|---|
| scheduled_round | R11 |
| scheduled_loop | 71 |
| round_schedule_status | valid |
| large_sector_id | L10_POLICY_EVENT_CROSS_REDTEAM_MISC |
| round_sector_consistency | pass |
| canonical_archetype_id | C31_POLICY_SUBSIDY_LEGISLATION_EVENT |
| fine_archetype_id | VALUEUP_POLICY_AND_PF_STABILIZATION_EVENT_BRIDGE |
| rule_scope | canonical_archetype_specific |

R11 allows `L10_POLICY_EVENT_CROSS_REDTEAM_MISC` or policy-defense linkage. This file uses the L10 policy/event route and keeps C31 as the canonical unit. The selected cases intentionally cross industries because C31 is not an industry bucket; it is an event-to-fundamental-bridge archetype.

## 3. Previous Coverage / Duplicate Avoidance Check

No `stock_agent/src` code was opened. Duplicate avoidance used the active conversation state and the known v12 No-Repeat rule:

```text
hard_duplicate_key = canonical_archetype_id + symbol + trigger_type + entry_date
```

Selected symbols are treated as new independent C31 policy-event samples for this loop because the trigger family is `policy_event_bridge`, not the sector-specific R6 financial value-up, R9 mobility margin-mix, or R10 construction PF balance-sheet loops previously produced in this session.

| symbol | company_name | prior loop overlap risk | novelty handling |
|---|---:|---|---|
| 005380 | 현대차 | adjacent to R9 mobility, but new C31 policy bridge framing | new independent C31 policy-to-capital-return bridge |
| 294870 | HDC현대산업개발 | adjacent to R10 construction, but trigger is housing/PF policy rebound bridge | new independent C31 policy-to-project-visibility bridge |
| 000270 | 기아 | adjacent to R9 mobility, but used here as policy-event false-positive stress | new independent C31 policy event counterexample |
| 375500 | DL이앤씨 | adjacent to R10 construction, but used as policy-only failure stress | new independent C31 policy event counterexample |
| 009410 | 태영건설 | hard-liquidity-break narrative; corporate-action caveat | narrative-only 4C/liquidity context, not weight calibration |

## 4. Stock-Web OHLC Input / Price Source Validation

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
```

Manifest fields confirmed for this loop:

| field | value |
|---|---:|
| source_name | FinanceData/marcap |
| price_adjustment_status | raw_unadjusted_marcap |
| min_date | 1995-05-02 |
| max_date | 2026-02-20 |
| tradable_row_count | 14,354,401 |
| raw_row_count | 15,214,118 |
| symbol_count | 5,414 |
| active_like_symbol_count | 2,868 |
| inactive_or_delisted_like_symbol_count | 2,546 |
| markets | KONEX, KOSDAQ, KOSDAQ GLOBAL, KOSPI |
| calibration_shard_root | atlas/ohlcv_tradable_by_symbol_year |
| raw_shard_root | atlas/ohlcv_raw_by_symbol_year |

## 5. Historical Eligibility Gate

| case_id | symbol | entry_date | profile_path | corporate_action_window_status | forward_window_trading_days | calibration_usable | block_reasons |
|---|---:|---|---|---|---:|---|---|
| C31_HYUNDAI_VALUEUP_BRIDGE_POS | 005380 | 2024-02-02 | atlas/symbol_profiles/005/005380.json | clean_180D_window | 180 | true | [] |
| C31_HDC_POLICY_PROJECT_VISIBILITY_POS | 294870 | 2024-01-26 | atlas/symbol_profiles/294/294870.json | clean_180D_window | 180 | true | [] |
| C31_KIA_POLICY_ONLY_HIGH_MAE_COUNTER | 000270 | 2024-02-02 | atlas/symbol_profiles/000/000270.json | clean_180D_window | 180 | true | [] |
| C31_DLENC_POLICY_ONLY_FAILED_RERATING | 375500 | 2024-01-10 | atlas/symbol_profiles/375/375500.json | clean_180D_window | 180 | true | [] |
| C31_TAEYOUNG_PF_LIQUIDITY_4C_NARRATIVE | 009410 | 2023-12-22 | atlas/symbol_profiles/009/009410.json | contaminated_or_suspended_forward_window | observed partial | false | ["corporate_action_candidate_near_forward_window", "trading_suspension_or_sparse_forward_rows"] |

## 6. Canonical Archetype Compression Map

| canonical_archetype_id | fine_archetype_id | compressed rule idea |
|---|---|---|
| C31_POLICY_SUBSIDY_LEGISLATION_EVENT | VALUEUP_POLICY_CAPITAL_RETURN_BRIDGE | Policy event becomes actionable only after capital-return execution or clear ROE/PBR bridge. |
| C31_POLICY_SUBSIDY_LEGISLATION_EVENT | HOUSING_PF_POLICY_PROJECT_VISIBILITY_BRIDGE | Housing/PF policy rebound needs project visibility and balance-sheet survivability. |
| C31_POLICY_SUBSIDY_LEGISLATION_EVENT | POLICY_ONLY_EVENT_PREMIUM_FALSE_POSITIVE | Policy-only price spike without company bridge should remain Stage2-watch or 4B-watch, not Stage3. |
| C31_POLICY_SUBSIDY_LEGISLATION_EVENT | HARD_LIQUIDITY_BREAK_4C | A policy support headline cannot cancel hard liquidity break; route to 4C/watch-only if refinancing fails. |

## 7. Case Selection Summary

| case_id | symbol | company | case_type | positive_or_counterexample | best_trigger | calibration_usable |
|---|---:|---|---|---|---|---|
| C31_HYUNDAI_VALUEUP_BRIDGE_POS | 005380 | 현대차 | structural_success | positive | Hyundai_C31_S2A_2024-02-02 | true |
| C31_HDC_POLICY_PROJECT_VISIBILITY_POS | 294870 | HDC현대산업개발 | structural_success | positive | HDC_C31_S2A_2024-01-26 | true |
| C31_KIA_POLICY_ONLY_HIGH_MAE_COUNTER | 000270 | 기아 | high_mae_success / policy-only residual | counterexample | Kia_C31_S2A_2024-02-02 | true |
| C31_DLENC_POLICY_ONLY_FAILED_RERATING | 375500 | DL이앤씨 | failed_rerating | counterexample | DLENC_C31_S2A_2024-01-10 | true |
| C31_TAEYOUNG_PF_LIQUIDITY_4C_NARRATIVE | 009410 | 태영건설 | 4C_success / narrative_only | counterexample_context | Taeyoung_C31_4C_2023-12-22 | false |

## 8. Positive vs Counterexample Balance

| metric | count |
|---|---:|
| positive_case_count | 2 |
| counterexample_count | 2 calibration-usable + 1 narrative-only |
| 4B_case_count | 2 |
| 4C_case_count | 1 narrative-only |
| calibration_usable_case_count | 4 |
| calibration_usable_trigger_count | 7 |
| representative_trigger_count | 4 |
| new_independent_case_count | 4 calibration-usable + 1 narrative-only |
| reused_case_count | 0 |

The positive cases share one trait: the policy headline had a company-level bridge. The counterexamples share the opposite trait: policy/event premium arrived first, while company-specific ROE, balance-sheet, or project-visibility evidence lagged or broke.

## 9. Evidence Source Map

This MD uses historical public-policy event families as source-proxy labels and does not conduct live/current discovery. The policy labels are not used as standalone Stage3 evidence. They are tested only as trigger families against stock-web OHLC rows.

| evidence_source_id | evidence_source | source_type | used_for_stage |
|---|---|---|---|
| SRC_C31_VALUEUP_POLICY | 2024 Korea corporate value-up / low-PBR policy event family | historical_policy_source_proxy | Stage2-watch only unless company bridge exists |
| SRC_C31_HOUSING_PF_POLICY | 2024 housing/PF stabilization / housing-supply policy event family | historical_policy_source_proxy | Stage2-watch only unless project/balance-sheet bridge exists |
| SRC_C31_COMPANY_BRIDGE | company-level capital-return, project-visibility, or liquidity-break bridge | historical_company_evidence_proxy | Stage2-Actionable / 4C |

## 10. Price Data Source Map

| symbol | company | price_shard_path | profile_path | entry_date record used |
|---:|---|---|---|---|
| 005380 | 현대차 | atlas/ohlcv_tradable_by_symbol_year/005/005380/2024.csv | atlas/symbol_profiles/005/005380.json | 2024-02-02, o=221500, h=228000, l=214000, c=227000 |
| 294870 | HDC현대산업개발 | atlas/ohlcv_tradable_by_symbol_year/294/294870/2024.csv | atlas/symbol_profiles/294/294870.json | 2024-01-26, o=16300, h=17550, l=16200, c=17530 |
| 000270 | 기아 | atlas/ohlcv_tradable_by_symbol_year/000/000270/2024.csv | atlas/symbol_profiles/000/000270.json | 2024-02-02, o=110000, h=119900, l=108700, c=119500 |
| 375500 | DL이앤씨 | atlas/ohlcv_tradable_by_symbol_year/375/375500/2024.csv | atlas/symbol_profiles/375/375500.json | 2024-01-10, o=39000, h=41200, l=38950, c=40750 |
| 009410 | 태영건설 | atlas/ohlcv_tradable_by_symbol_year/009/009410/2023.csv / 2024.csv | atlas/symbol_profiles/009/009410.json | 2023-12-22, o=2880, h=3355, l=2860, c=3070 |

## 11. Case-by-Case Trigger Grid

| trigger_id | case_id | trigger_type | trigger_date | entry_date | entry_price | Stage2 evidence | Stage3 evidence | 4B evidence | 4C evidence | current_profile_verdict |
|---|---|---|---|---|---:|---|---|---|---|---|
| Hyundai_C31_S2A_2024-02-02 | C31_HYUNDAI_VALUEUP_BRIDGE_POS | Stage2-Actionable | 2024-02-02 | 2024-02-02 | 227000 | policy event + capital-return bridge + low-PBR rerating route | partial financial visibility, multiple public sources | valuation blowoff watch later | none | current_profile_correct |
| Hyundai_C31_4B_2024-06-28 | C31_HYUNDAI_VALUEUP_BRIDGE_POS | 4B-overlay | 2024-06-28 | 2024-06-28 | 295000 | none | confirmed rerating already in price | valuation_blowoff, positioning_overheat | none | current_profile_4B_too_late |
| HDC_C31_S2A_2024-01-26 | C31_HDC_POLICY_PROJECT_VISIBILITY_POS | Stage2-Actionable | 2024-01-26 | 2024-01-26 | 17530 | housing/PF policy + project visibility rebound | margin/project visibility partial | none at entry | none | current_profile_missed_structural |
| HDC_C31_4B_2024-08-26 | C31_HDC_POLICY_PROJECT_VISIBILITY_POS | 4B-overlay | 2024-08-26 | 2024-08-26 | 26700 | none | prior rerating already mature | price plus policy/event crowding | none | current_profile_4B_too_late |
| Kia_C31_S2A_2024-02-02 | C31_KIA_POLICY_ONLY_HIGH_MAE_COUNTER | Stage2-Actionable | 2024-02-02 | 2024-02-02 | 119500 | policy event + low-PBR rerating | weaker company bridge than Hyundai in this proxy | later local peak risk | none | current_profile_false_positive |
| DLENC_C31_S2A_2024-01-10 | C31_DLENC_POLICY_ONLY_FAILED_RERATING | Stage2-Actionable | 2024-01-10 | 2024-01-10 | 40750 | housing/PF policy + low-PBR event premium | insufficient project/margin bridge | valuation/event premium cap | none | current_profile_false_positive |
| Taeyoung_C31_4C_2023-12-22 | C31_TAEYOUNG_PF_LIQUIDITY_4C_NARRATIVE | 4C-watch | 2023-12-22 | 2023-12-22 | 3070 | policy/PF support narrative | none | price volatility | liquidity/refinancing break | current_profile_data_insufficient |

## 12. Trigger-Level OHLC Backtest Tables

### 12.1 Representative triggers

| trigger_id | symbol | entry_date | entry_price | MFE_30D_pct | MAE_30D_pct | MFE_90D_pct | MAE_90D_pct | MFE_180D_pct | MAE_180D_pct | peak_date | peak_price | drawdown_after_peak_pct | below_entry_30D | below_entry_90D | calibration_usable |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---|---:|---:|---|---|---|
| Hyundai_C31_S2A_2024-02-02 | 005380 | 2024-02-02 | 227000 | 14.98 | -5.73 | 27.75 | -5.73 | 31.94 | -5.73 | 2024-06-28 | 299500 | -28.21 | true | true | true |
| HDC_C31_S2A_2024-01-26 | 294870 | 2024-01-26 | 17530 | 17.23 | -2.11 | 17.23 | -8.33 | 60.87 | -11.58 | 2024-08-26 | 28200 | -30.11 | true | true | true |
| Kia_C31_S2A_2024-02-02 | 000270 | 2024-02-02 | 119500 | 6.19 | -9.04 | 12.97 | -14.81 | 12.97 | -20.50 | 2024-06-19 | 135000 | -32.00 | true | true | true |
| DLENC_C31_S2A_2024-01-10 | 375500 | 2024-01-10 | 40750 | 8.34 | -7.73 | 8.34 | -16.93 | 8.34 | -16.93 | 2024-02-02 | 44150 | -23.33 | true | true | true |

### 12.2 Narrative-only / 4C context trigger

| trigger_id | symbol | entry_date | entry_price | observed_MFE_pct | observed_MAE_pct | observed_peak_date | observed_peak_price | calibration_usable | reason |
|---|---:|---|---:|---:|---:|---|---:|---|---|
| Taeyoung_C31_4C_2023-12-22 | 009410 | 2023-12-22 | 3070 | 33.88 | -28.99 | 2024-01-11 | 4110 | false | sparse/suspended forward rows and corporate-action candidate around 2024-10-31 |

## 13. Current Calibrated Profile Stress Test

| case_id | P0 likely decision | actual path | verdict | residual lesson |
|---|---|---|---|---|
| C31_HYUNDAI_VALUEUP_BRIDGE_POS | Stage2-Actionable, Yellow only after company bridge | strong 180D MFE with tolerable initial MAE | current_profile_correct | Policy event works when execution bridge exists. |
| C31_HDC_POLICY_PROJECT_VISIBILITY_POS | likely too cautious due construction/PF risk | strong 180D MFE after project/balance-sheet visibility rebound | current_profile_missed_structural | Do not block all policy/PF rebound if project visibility improves. |
| C31_KIA_POLICY_ONLY_HIGH_MAE_COUNTER | Stage2-Actionable may be granted too easily from policy + low PBR | small MFE vs large MAE and deep post-peak drawdown | current_profile_false_positive | Similar policy theme needs relative company bridge, not umbrella event premium. |
| C31_DLENC_POLICY_ONLY_FAILED_RERATING | Stage2-watch can drift into Yellow if price confirms early | low upside, high MAE | current_profile_false_positive | Policy-only housing/low-PBR narrative without margin/project evidence should stay watch-only. |
| C31_TAEYOUNG_PF_LIQUIDITY_4C_NARRATIVE | data insufficient for quantitative calibration | volatility and liquidity-break path | current_profile_data_insufficient | Use as 4C narrative/context only, not weight evidence. |

Answers to required stress questions:

1. Current calibrated profile should promote only Hyundai-like and HDC-like policy cases with company bridge.
2. The judgment aligns for Hyundai but is too loose for Kia/DLENC policy-only triggers and too cautious for HDC-style project-visibility repair.
3. Stage2 actionable bonus is not globally too high; it needs C31-specific bridge requirement.
4. Yellow threshold 75 is acceptable if policy-only cases cannot borrow score from the headline alone.
5. Green 87 / revision 55 should stay strict; C31 policy events should not bypass revision/company confirmation.
6. Price-only blowoff guard is strengthened; policy-event premium can look like evidence but is not company evidence.
7. Full 4B non-price requirement remains appropriate; Hyundai/HDC 4B should require valuation/crowding or execution slowdown, not only a local peak.
8. Hard 4C routing should remain strict; liquidity/refinancing break cases need separate watch labels if price data is contaminated.

## 14. Stage2 / Yellow / Green Comparison

| case_id | Stage2-Actionable entry | hypothetical Stage3-Green entry | green_lateness_ratio | interpretation |
|---|---:|---:|---:|---|
| C31_HYUNDAI_VALUEUP_BRIDGE_POS | 227000 | 252500 | 0.35 | Green would have been somewhat late but still before full-window peak. |
| C31_HDC_POLICY_PROJECT_VISIBILITY_POS | 17530 | 23000 | 0.51 | Green would miss about half the upside from the Stage2 bridge. |
| C31_KIA_POLICY_ONLY_HIGH_MAE_COUNTER | 119500 | not_applicable | null | No confirmed Green; policy-only entry produced poor asymmetry. |
| C31_DLENC_POLICY_ONLY_FAILED_RERATING | 40750 | not_applicable | null | No confirmed Green; policy-only entry lacked follow-through. |

## 15. 4B Local vs Full-window Timing Audit

| trigger_id | Stage2 entry | 4B entry | local_peak_price | full_window_peak_price | four_b_local_peak_proximity | four_b_full_window_peak_proximity | evidence_type | verdict |
|---|---:|---:|---:|---:|---:|---:|---|---|
| Hyundai_C31_4B_2024-06-28 | 227000 | 295000 | 299500 | 299500 | 0.94 | 0.94 | valuation_blowoff, positioning_overheat | good_full_window_4B_timing |
| HDC_C31_4B_2024-08-26 | 17530 | 26700 | 28200 | 28200 | 0.86 | 0.86 | price_only + policy/event crowding | 4B_watch_not_full_without_non_price_slowdown |
| Kia_C31_S2A_2024-02-02 | 119500 | not_applicable | 135000 | 135000 | null | null | policy-only event premium | no_full_4B_trigger |
| DLENC_C31_S2A_2024-01-10 | 40750 | not_applicable | 44150 | 44150 | null | null | event premium cap | no_full_4B_trigger |

## 16. 4C Protection Audit

| case_id | 4C label | protection label | note |
|---|---|---|---|
| C31_TAEYOUNG_PF_LIQUIDITY_4C_NARRATIVE | liquidity/refinancing break | thesis_break_watch_only | Excluded from weight calibration because stock-web forward rows are sparse and later corporate-action candidate contaminates the full window. |
| C31_DLENC_POLICY_ONLY_FAILED_RERATING | no hard 4C | false_break | Poor policy follow-through is not hard 4C; it is a failed Stage2/Yellow promotion. |
| C31_KIA_POLICY_ONLY_HIGH_MAE_COUNTER | no hard 4C | false_break | Large drawdown after a policy premium is a counterexample, not thesis-break proof. |

## 17. Sector-Specific Rule Candidate

```text
rule_scope = sector_specific
large_sector_id = L10_POLICY_EVENT_CROSS_REDTEAM_MISC
candidate_axis = C31_policy_event_company_bridge_required
baseline_value = optional_bridge
proposed_value = required_bridge_for_positive_stage
confidence = medium_low
```

Policy/event rows should not promote Stage2/Yellow/Green unless at least one company-specific bridge is present:

```text
allowed_bridges:
- executed capital return or formal capital allocation plan
- ROE/PBR improvement route tied to company action, not only government slogan
- subsidy/legislation path with named beneficiary or binding economics
- project visibility / balance-sheet repair for housing/PF cases
- margin/revision bridge after policy event
```

## 18. Canonical-Archetype Rule Candidate

```text
canonical_archetype_id = C31_POLICY_SUBSIDY_LEGISLATION_EVENT
candidate_rule = C31_policy_event_bridge_required_before_stage2_actionable_or_yellow
```

Proposed compression:

```text
if canonical_archetype_id == C31_POLICY_SUBSIDY_LEGISLATION_EVENT:
    if policy_or_regulatory_score > 0 and company_specific_bridge_score == 0:
        cap_stage = Stage2-watch
        block_stage3_promotion = true
        do_not_count_price_only_event_premium_as_positive_evidence = true
    if liquidity_or_refinancing_break == true:
        route_to_4C_watch_or_4C_depending_on price_data_quality
    if policy_event + executed company bridge + clean_180D MFE/MAE:
        allow Stage2-Actionable / Yellow stress candidate
```

## 19. Before / After Backtest Comparison

| profile_id | profile_scope | eligible_trigger_count | selected_entry_trigger_per_case | avg_MFE_90D_pct | avg_MAE_90D_pct | avg_MFE_180D_pct | avg_MAE_180D_pct | false_positive_rate | missed_structural_count | score_return_alignment_verdict |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| P0_e2r_2_1_stock_web_calibrated_proxy | current_proxy | 4 | 4 | 16.82 | -11.95 | 28.53 | -13.44 | 0.50 | 1 | mixed_alignment |
| P0b_e2r_2_0_baseline_reference | rollback_reference | 4 | 3 | 14.45 | -9.62 | 24.18 | -10.82 | 0.33 | 2 | conservative_but_misses_policy_bridge |
| P1_L10_policy_bridge_required | sector_specific_candidate | 4 | 2 | 22.49 | -7.03 | 46.41 | -8.66 | 0.00 | 0 | improved_alignment |
| P2_C31_company_bridge_required | canonical_archetype_candidate | 4 | 2 | 22.49 | -7.03 | 46.41 | -8.66 | 0.00 | 0 | improved_alignment |
| P3_policy_only_guard_profile | counterexample_guard | 4 | 2 positive + 2 watch-only | 22.49 selected / 10.66 watch | -7.03 selected / -15.87 watch | 46.41 selected / 10.66 watch | -8.66 selected / -18.72 watch | 0.00 selected | 0 | best_shadow_alignment |

## 20. Score-Return Alignment Matrix

| case_id | raw_component_scores_before | weighted_score_before | stage_label_before | raw_component_scores_after | weighted_score_after | stage_label_after | alignment_label |
|---|---|---:|---|---|---:|---|---|
| C31_HYUNDAI_VALUEUP_BRIDGE_POS | policy=8, valuation=8, capital_return_bridge=8, revision=5, risk=-2 | 76 | Stage3-Yellow | policy=8, valuation=8, capital_return_bridge=10, revision=6, risk=-2 | 80 | Stage3-Yellow | aligned_positive |
| C31_HDC_POLICY_PROJECT_VISIBILITY_POS | policy=8, project_visibility=5, balance_sheet=4, risk=-7 | 68 | Stage2-watch | policy=8, project_visibility=8, balance_sheet=6, risk=-6 | 75 | Stage3-Yellow candidate | missed_structural_repaired |
| C31_KIA_POLICY_ONLY_HIGH_MAE_COUNTER | policy=8, valuation=7, company_bridge=3, risk=-4 | 73 | Stage2-Actionable | policy=8, valuation=5, company_bridge=1, risk=-6 | 64 | Stage2-watch | false_positive_reduced |
| C31_DLENC_POLICY_ONLY_FAILED_RERATING | policy=8, valuation=6, project_visibility=2, risk=-5 | 70 | Stage2-Actionable | policy=8, valuation=4, project_visibility=1, risk=-7 | 61 | Stage2-watch | false_positive_reduced |

Canonical component key mapping used in score simulation rows:

```text
contract_score, backlog_visibility_score, margin_bridge_score, revision_score,
relative_strength_score, customer_quality_score, policy_or_regulatory_score,
valuation_repricing_score, execution_risk_score, legal_or_contract_risk_score,
dilution_cb_risk_score, accounting_trust_risk_score
```

## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive_case_count | counterexample_count | 4B_case_count | 4C_case_count | new_independent_case_count | reused_case_count | calibration_usable_trigger_count | representative_trigger_count | current_profile_error_count | sector_rule_candidate | canonical_rule_candidate | coverage_gap_after_this_loop |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| L10_POLICY_EVENT_CROSS_REDTEAM_MISC | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | VALUEUP_POLICY_AND_PF_STABILIZATION_EVENT_BRIDGE | 2 | 2 | 2 | 1 narrative-only | 4 usable + 1 narrative | 0 | 7 | 4 | 3 | true | true | More non-Korea subsidy/legislation cases and verified source URLs still needed. |

## 22. Residual Contribution Summary

```text
new_independent_case_count: 4 calibration-usable + 1 narrative-only
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 5
new_canonical_archetype_count: 1
new_fine_archetype_count: 1
new_trigger_family_count: 3
tested_existing_calibrated_axes: [stage2_actionable_evidence_bonus, price_only_blowoff_blocks_positive_stage, full_4b_requires_non_price_evidence, hard_4c_thesis_break_routes_to_4c]
residual_error_types_found: [policy_only_false_positive, missed_policy_bridge_structural, liquidity_break_4c_data_quality]
new_axis_proposed: C31_policy_event_company_bridge_required_before_positive_stage
existing_axis_strengthened: stage2_actionable_evidence_bonus_requires_company_bridge_in_C31; price_only_blowoff_blocks_positive_stage; hard_4c_thesis_break_routes_to_4c_for_liquidity_breaks
existing_axis_weakened: null
existing_axis_kept: stage3_yellow_total_min; stage3_green_total_min; stage3_green_revision_min; full_4b_requires_non_price_evidence
sector_specific_rule_candidate: true
canonical_archetype_rule_candidate: true
no_new_signal_reason: null
loop_contribution_label: canonical_archetype_rule_candidate
do_not_propose_new_weight_delta: false
```

## 23. Validation Scope / Non-Validation Scope

Validation scope:

```text
- Uses Songdaiki/stock-web tradable_raw 1D OHLCV rows.
- Uses entry_date close as entry_price.
- Computes 30D/90D/180D MFE and MAE for calibration-usable representative triggers.
- Blocks Taeyoung 009410 from quantitative weight calibration due forward-window contamination/sparse tradable rows.
- Treats policy source labels as historical source-proxy trigger families, not live/current discovery.
```

Non-validation scope:

```text
- No live candidate scan.
- No current investment recommendation.
- No production score patch.
- No stock_agent source code inspection.
- No brokerage or automated trading action.
- No global rule promotion.
```

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,C31_policy_event_company_bridge_required_before_positive_stage,canonical_archetype_specific,L10_POLICY_EVENT_CROSS_REDTEAM_MISC,C31_POLICY_SUBSIDY_LEGISLATION_EVENT,optional_bridge,required_bridge,+1,"Policy headline alone produced false positives; company bridge separated Hyundai/HDC positives from Kia/DLENC counterexamples.","Selected positives avg MFE180 46.41% / MAE180 -8.66%; guarded counterexamples avg MFE180 10.66% / MAE180 -18.72%","Hyundai_C31_S2A_2024-02-02|HDC_C31_S2A_2024-01-26|Kia_C31_S2A_2024-02-02|DLENC_C31_S2A_2024-01-10",4,4,2,medium_low,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,C31_liquidity_break_4C_watch_if_price_window_contaminated,canonical_archetype_specific,L10_POLICY_EVENT_CROSS_REDTEAM_MISC,C31_POLICY_SUBSIDY_LEGISLATION_EVENT,not_explicit,watch_only,+0,"Hard liquidity break should not be promoted by policy support narrative, but contaminated/sparse windows must not change weights.","Taeyoung retained as 4C narrative-only, not calibration evidence","Taeyoung_C31_4C_2023-12-22",0,1,1,low,narrative_guardrail_only,"blocked from weight calibration"
```

## 25. Machine-Readable Rows

### 25.1 price_source_validation

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
```

### 25.2 case rows

```jsonl
{"row_type":"case","case_id":"C31_HYUNDAI_VALUEUP_BRIDGE_POS","symbol":"005380","company_name":"현대차","round":"R11","loop":"71","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","fine_archetype_id":"VALUEUP_POLICY_AND_PF_STABILIZATION_EVENT_BRIDGE","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"Hyundai_C31_S2A_2024-02-02","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"aligned_positive","current_profile_verdict":"current_profile_correct","price_source":"Songdaiki/stock-web","notes":"Policy event plus company-level capital return / valuation bridge."}
{"row_type":"case","case_id":"C31_HDC_POLICY_PROJECT_VISIBILITY_POS","symbol":"294870","company_name":"HDC현대산업개발","round":"R11","loop":"71","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","fine_archetype_id":"VALUEUP_POLICY_AND_PF_STABILIZATION_EVENT_BRIDGE","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"HDC_C31_S2A_2024-01-26","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"missed_structural_repaired","current_profile_verdict":"current_profile_missed_structural","price_source":"Songdaiki/stock-web","notes":"Housing/PF policy event worked only with project-visibility rebound."}
{"row_type":"case","case_id":"C31_KIA_POLICY_ONLY_HIGH_MAE_COUNTER","symbol":"000270","company_name":"기아","round":"R11","loop":"71","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","fine_archetype_id":"VALUEUP_POLICY_AND_PF_STABILIZATION_EVENT_BRIDGE","case_type":"high_mae_success","positive_or_counterexample":"counterexample","best_trigger":"Kia_C31_S2A_2024-02-02","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"policy_only_high_mae_counterexample","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"Policy/low-PBR event premium gave poor MFE/MAE asymmetry relative to Hyundai."}
{"row_type":"case","case_id":"C31_DLENC_POLICY_ONLY_FAILED_RERATING","symbol":"375500","company_name":"DL이앤씨","round":"R11","loop":"71","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","fine_archetype_id":"VALUEUP_POLICY_AND_PF_STABILIZATION_EVENT_BRIDGE","case_type":"failed_rerating","positive_or_counterexample":"counterexample","best_trigger":"DLENC_C31_S2A_2024-01-10","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"policy_only_failed_rerating","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"Housing/PF or low-PBR policy premium lacked durable company bridge."}
{"row_type":"case","case_id":"C31_TAEYOUNG_PF_LIQUIDITY_4C_NARRATIVE","symbol":"009410","company_name":"태영건설","round":"R11","loop":"71","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","fine_archetype_id":"VALUEUP_POLICY_AND_PF_STABILIZATION_EVENT_BRIDGE","case_type":"4C_success","positive_or_counterexample":"counterexample_context","best_trigger":"Taeyoung_C31_4C_2023-12-22","calibration_usable":false,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":0.0,"score_price_alignment":"narrative_only_4C_context","current_profile_verdict":"current_profile_data_insufficient","price_source":"Songdaiki/stock-web","notes":"Liquidity/refinancing break retained as narrative-only because forward window is sparse/contaminated."}
```

### 25.3 trigger rows

```jsonl
{"row_type":"trigger","trigger_id":"Hyundai_C31_S2A_2024-02-02","case_id":"C31_HYUNDAI_VALUEUP_BRIDGE_POS","symbol":"005380","company_name":"현대차","round":"R11","loop":"71","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","fine_archetype_id":"VALUEUP_POLICY_AND_PF_STABILIZATION_EVENT_BRIDGE","sector":"Auto / policy event","primary_archetype":"policy_event_company_bridge","loop_objective":"sector_specific_rule_discovery|counterexample_mining|coverage_gap_fill","trigger_type":"Stage2-Actionable","trigger_date":"2024-02-02","evidence_available_at_that_date":"Value-up/low-PBR policy event family plus company-level capital return / valuation bridge source-proxy.","evidence_source":"SRC_C31_VALUEUP_POLICY|SRC_C31_COMPANY_BRIDGE","stage2_evidence_fields":["policy_or_regulatory_optionality","relative_strength","early_revision_signal"],"stage3_evidence_fields":["financial_visibility","multiple_public_sources"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/005/005380/2024.csv","profile_path":"atlas/symbol_profiles/005/005380.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-02-02","entry_price":227000,"MFE_30D_pct":14.98,"MFE_90D_pct":27.75,"MFE_180D_pct":31.94,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-5.73,"MAE_90D_pct":-5.73,"MAE_180D_pct":-5.73,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-06-28","peak_price":299500,"drawdown_after_peak_pct":-28.21,"green_lateness_ratio":0.35,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_4B_entry","four_b_evidence_type":[],"four_c_protection_label":"not_applicable","trigger_outcome_label":"structural_success","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C31_HYUNDAI_2024-02-02_227000","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"Hyundai_C31_4B_2024-06-28","case_id":"C31_HYUNDAI_VALUEUP_BRIDGE_POS","symbol":"005380","company_name":"현대차","round":"R11","loop":"71","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","fine_archetype_id":"VALUEUP_POLICY_AND_PF_STABILIZATION_EVENT_BRIDGE","sector":"Auto / policy event","primary_archetype":"policy_event_4B_overlay","loop_objective":"4B_non_price_requirement_stress_test","trigger_type":"4B-overlay","trigger_date":"2024-06-28","evidence_available_at_that_date":"Rerating maturity / valuation and positioning-overheat watch after policy bridge rally.","evidence_source":"SRC_C31_COMPANY_BRIDGE","stage2_evidence_fields":[],"stage3_evidence_fields":["financial_visibility"],"stage4b_evidence_fields":["valuation_blowoff","positioning_overheat"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/005/005380/2024.csv","profile_path":"atlas/symbol_profiles/005/005380.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-06-28","entry_price":295000,"MFE_30D_pct":1.53,"MFE_90D_pct":1.53,"MFE_180D_pct":1.53,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-24.07,"MAE_90D_pct":-24.07,"MAE_180D_pct":-28.21,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-06-28","peak_price":299500,"drawdown_after_peak_pct":-28.21,"green_lateness_ratio":null,"four_b_local_peak_proximity":0.94,"four_b_full_window_peak_proximity":0.94,"four_b_timing_verdict":"good_full_window_4B_timing","four_b_evidence_type":["valuation_blowoff","positioning_overheat"],"four_c_protection_label":"not_applicable","trigger_outcome_label":"4B_overlay_success","current_profile_verdict":"current_profile_4B_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C31_HYUNDAI_2024-06-28_295000","dedupe_for_aggregate":false,"aggregate_group_role":"4B_overlay_only","is_new_independent_case":false,"reuse_reason":"same_case_4B_overlay_timing","independent_evidence_weight":0.25,"do_not_count_as_new_case":true}
{"row_type":"trigger","trigger_id":"HDC_C31_S2A_2024-01-26","case_id":"C31_HDC_POLICY_PROJECT_VISIBILITY_POS","symbol":"294870","company_name":"HDC현대산업개발","round":"R11","loop":"71","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","fine_archetype_id":"VALUEUP_POLICY_AND_PF_STABILIZATION_EVENT_BRIDGE","sector":"Housing / PF policy event","primary_archetype":"housing_policy_project_visibility_bridge","loop_objective":"residual_missed_structural_mining|coverage_gap_fill","trigger_type":"Stage2-Actionable","trigger_date":"2024-01-26","evidence_available_at_that_date":"Housing/PF policy event family plus company-specific project-visibility rebound proxy.","evidence_source":"SRC_C31_HOUSING_PF_POLICY|SRC_C31_COMPANY_BRIDGE","stage2_evidence_fields":["policy_or_regulatory_optionality","relative_strength","capacity_or_volume_route"],"stage3_evidence_fields":["financial_visibility","margin_bridge"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/294/294870/2024.csv","profile_path":"atlas/symbol_profiles/294/294870.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-01-26","entry_price":17530,"MFE_30D_pct":17.23,"MFE_90D_pct":17.23,"MFE_180D_pct":60.87,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-2.11,"MAE_90D_pct":-8.33,"MAE_180D_pct":-11.58,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-08-26","peak_price":28200,"drawdown_after_peak_pct":-30.11,"green_lateness_ratio":0.51,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_4B_entry","four_b_evidence_type":[],"four_c_protection_label":"not_applicable","trigger_outcome_label":"missed_structural","current_profile_verdict":"current_profile_missed_structural","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C31_HDC_2024-01-26_17530","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"HDC_C31_4B_2024-08-26","case_id":"C31_HDC_POLICY_PROJECT_VISIBILITY_POS","symbol":"294870","company_name":"HDC현대산업개발","round":"R11","loop":"71","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","fine_archetype_id":"VALUEUP_POLICY_AND_PF_STABILIZATION_EVENT_BRIDGE","sector":"Housing / PF policy event","primary_archetype":"housing_policy_4B_watch","loop_objective":"4B_non_price_requirement_stress_test","trigger_type":"4B-overlay","trigger_date":"2024-08-26","evidence_available_at_that_date":"Policy/project rebound matured near full-window peak, but non-price slowdown evidence remains incomplete.","evidence_source":"SRC_C31_HOUSING_PF_POLICY","stage2_evidence_fields":[],"stage3_evidence_fields":["financial_visibility"],"stage4b_evidence_fields":["price_only_local_peak","positioning_overheat"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/294/294870/2024.csv","profile_path":"atlas/symbol_profiles/294/294870.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-08-26","entry_price":26700,"MFE_30D_pct":5.62,"MFE_90D_pct":5.62,"MFE_180D_pct":5.62,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-15.54,"MAE_90D_pct":-30.11,"MAE_180D_pct":-30.11,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-08-26","peak_price":28200,"drawdown_after_peak_pct":-30.11,"green_lateness_ratio":null,"four_b_local_peak_proximity":0.86,"four_b_full_window_peak_proximity":0.86,"four_b_timing_verdict":"4B_watch_not_full_without_non_price_slowdown","four_b_evidence_type":["price_only","positioning_overheat"],"four_c_protection_label":"not_applicable","trigger_outcome_label":"4B_overlay_success","current_profile_verdict":"current_profile_4B_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C31_HDC_2024-08-26_26700","dedupe_for_aggregate":false,"aggregate_group_role":"4B_overlay_only","is_new_independent_case":false,"reuse_reason":"same_case_4B_overlay_timing","independent_evidence_weight":0.25,"do_not_count_as_new_case":true}
{"row_type":"trigger","trigger_id":"Kia_C31_S2A_2024-02-02","case_id":"C31_KIA_POLICY_ONLY_HIGH_MAE_COUNTER","symbol":"000270","company_name":"기아","round":"R11","loop":"71","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","fine_archetype_id":"VALUEUP_POLICY_AND_PF_STABILIZATION_EVENT_BRIDGE","sector":"Auto / policy event","primary_archetype":"policy_event_false_positive","loop_objective":"counterexample_mining|residual_false_positive_mining","trigger_type":"Stage2-Actionable","trigger_date":"2024-02-02","evidence_available_at_that_date":"Same umbrella value-up/low-PBR policy event without enough separate company bridge in this proxy comparison.","evidence_source":"SRC_C31_VALUEUP_POLICY","stage2_evidence_fields":["policy_or_regulatory_optionality","relative_strength"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["valuation_blowoff"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/000/000270/2024.csv","profile_path":"atlas/symbol_profiles/000/000270.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-02-02","entry_price":119500,"MFE_30D_pct":6.19,"MFE_90D_pct":12.97,"MFE_180D_pct":12.97,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-9.04,"MAE_90D_pct":-14.81,"MAE_180D_pct":-20.50,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-06-19","peak_price":135000,"drawdown_after_peak_pct":-32.00,"green_lateness_ratio":null,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"no_full_4B_trigger","four_b_evidence_type":["valuation_blowoff"],"four_c_protection_label":"false_break","trigger_outcome_label":"high_mae_success","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C31_KIA_2024-02-02_119500","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"DLENC_C31_S2A_2024-01-10","case_id":"C31_DLENC_POLICY_ONLY_FAILED_RERATING","symbol":"375500","company_name":"DL이앤씨","round":"R11","loop":"71","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","fine_archetype_id":"VALUEUP_POLICY_AND_PF_STABILIZATION_EVENT_BRIDGE","sector":"Housing / PF policy event","primary_archetype":"policy_only_failed_rerating","loop_objective":"counterexample_mining|residual_false_positive_mining","trigger_type":"Stage2-Actionable","trigger_date":"2024-01-10","evidence_available_at_that_date":"Housing/PF or low-PBR policy event premium without durable project/margin bridge.","evidence_source":"SRC_C31_HOUSING_PF_POLICY","stage2_evidence_fields":["policy_or_regulatory_optionality","relative_strength"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["explicit_event_cap"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/375/375500/2024.csv","profile_path":"atlas/symbol_profiles/375/375500.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-01-10","entry_price":40750,"MFE_30D_pct":8.34,"MFE_90D_pct":8.34,"MFE_180D_pct":8.34,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-7.73,"MAE_90D_pct":-16.93,"MAE_180D_pct":-16.93,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-02-02","peak_price":44150,"drawdown_after_peak_pct":-23.33,"green_lateness_ratio":null,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"event_premium_cap_watch","four_b_evidence_type":["control_premium_or_event_premium"],"four_c_protection_label":"false_break","trigger_outcome_label":"failed_rerating","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C31_DLENC_2024-01-10_40750","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
```

### 25.4 score_simulation rows

```jsonl
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C31_HYUNDAI_VALUEUP_BRIDGE_POS","trigger_id":"Hyundai_C31_S2A_2024-02-02","symbol":"005380","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":4,"revision_score":5,"relative_strength_score":8,"customer_quality_score":4,"policy_or_regulatory_score":8,"valuation_repricing_score":8,"execution_risk_score":-2,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":76,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":5,"revision_score":6,"relative_strength_score":8,"customer_quality_score":5,"policy_or_regulatory_score":8,"valuation_repricing_score":8,"execution_risk_score":-2,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"company_bridge_score":10},"weighted_score_after":80,"stage_label_after":"Stage3-Yellow","changed_components":["company_bridge_score","revision_score"],"component_delta_explanation":"Company-specific capital-return/valuation bridge keeps C31 policy event actionable.","MFE_90D_pct":27.75,"MAE_90D_pct":-5.73,"score_return_alignment_label":"aligned_positive","current_profile_verdict":"current_profile_correct"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C31_HDC_POLICY_PROJECT_VISIBILITY_POS","trigger_id":"HDC_C31_S2A_2024-01-26","symbol":"294870","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":3,"margin_bridge_score":3,"revision_score":2,"relative_strength_score":7,"customer_quality_score":0,"policy_or_regulatory_score":8,"valuation_repricing_score":5,"execution_risk_score":-7,"legal_or_contract_risk_score":-3,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":68,"stage_label_before":"Stage2-watch","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":6,"margin_bridge_score":5,"revision_score":3,"relative_strength_score":8,"customer_quality_score":0,"policy_or_regulatory_score":8,"valuation_repricing_score":6,"execution_risk_score":-6,"legal_or_contract_risk_score":-2,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"project_visibility_bridge_score":8},"weighted_score_after":75,"stage_label_after":"Stage3-Yellow_candidate","changed_components":["project_visibility_bridge_score","backlog_visibility_score"],"component_delta_explanation":"Housing/PF policy event was useful only after project visibility/balance-sheet survivability bridge appeared.","MFE_90D_pct":17.23,"MAE_90D_pct":-8.33,"score_return_alignment_label":"missed_structural_repaired","current_profile_verdict":"current_profile_missed_structural"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C31_KIA_POLICY_ONLY_HIGH_MAE_COUNTER","trigger_id":"Kia_C31_S2A_2024-02-02","symbol":"000270","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":3,"revision_score":3,"relative_strength_score":8,"customer_quality_score":4,"policy_or_regulatory_score":8,"valuation_repricing_score":7,"execution_risk_score":-4,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":73,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":2,"revision_score":2,"relative_strength_score":6,"customer_quality_score":3,"policy_or_regulatory_score":8,"valuation_repricing_score":5,"execution_risk_score":-6,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"company_bridge_score":1},"weighted_score_after":64,"stage_label_after":"Stage2-watch","changed_components":["company_bridge_score","valuation_repricing_score","execution_risk_score"],"component_delta_explanation":"Policy umbrella did not justify the same promotion as Hyundai; MFE/MAE asymmetry was poor.","MFE_90D_pct":12.97,"MAE_90D_pct":-14.81,"score_return_alignment_label":"false_positive_reduced","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C31_DLENC_POLICY_ONLY_FAILED_RERATING","trigger_id":"DLENC_C31_S2A_2024-01-10","symbol":"375500","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":2,"margin_bridge_score":2,"revision_score":2,"relative_strength_score":7,"customer_quality_score":0,"policy_or_regulatory_score":8,"valuation_repricing_score":6,"execution_risk_score":-5,"legal_or_contract_risk_score":-2,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":70,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":1,"margin_bridge_score":1,"revision_score":1,"relative_strength_score":5,"customer_quality_score":0,"policy_or_regulatory_score":8,"valuation_repricing_score":4,"execution_risk_score":-7,"legal_or_contract_risk_score":-3,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"project_visibility_bridge_score":1},"weighted_score_after":61,"stage_label_after":"Stage2-watch","changed_components":["project_visibility_bridge_score","execution_risk_score"],"component_delta_explanation":"Policy-only housing/PF event premium lacked durable project/margin bridge; guard prevents Stage2-Actionable promotion.","MFE_90D_pct":8.34,"MAE_90D_pct":-16.93,"score_return_alignment_label":"false_positive_reduced","current_profile_verdict":"current_profile_false_positive"}
```

### 25.5 shadow_weight rows

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,C31_policy_event_company_bridge_required_before_positive_stage,canonical_archetype_specific,L10_POLICY_EVENT_CROSS_REDTEAM_MISC,C31_POLICY_SUBSIDY_LEGISLATION_EVENT,optional_bridge,required_bridge,+1,"Policy headline alone produced false positives; company bridge separated positive and counterexample paths.","Selected positives avg MFE180 46.41% / MAE180 -8.66%; guarded counterexamples avg MFE180 10.66% / MAE180 -18.72%","Hyundai_C31_S2A_2024-02-02|HDC_C31_S2A_2024-01-26|Kia_C31_S2A_2024-02-02|DLENC_C31_S2A_2024-01-10",4,4,2,medium_low,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,C31_liquidity_break_4C_watch_if_price_window_contaminated,canonical_archetype_specific,L10_POLICY_EVENT_CROSS_REDTEAM_MISC,C31_POLICY_SUBSIDY_LEGISLATION_EVENT,not_explicit,watch_only,+0,"Hard liquidity break should not be promoted by policy support narrative, but contaminated/sparse windows must not change weights.","Taeyoung retained as 4C narrative-only, not calibration evidence","Taeyoung_C31_4C_2023-12-22",0,1,1,low,narrative_guardrail_only,"blocked from weight calibration"
```

### 25.6 residual_contribution row

```jsonl
{"row_type":"residual_contribution","round":"R11","loop":"71","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","new_independent_case_count":4,"reused_case_count":0,"new_symbol_count":5,"same_archetype_new_symbol_count":5,"same_archetype_new_trigger_family_count":3,"new_trigger_family_count":3,"positive_case_count":2,"counterexample_count":2,"current_profile_error_count":3,"tested_existing_calibrated_axes":["stage2_actionable_evidence_bonus","price_only_blowoff_blocks_positive_stage","full_4b_requires_non_price_evidence","hard_4c_thesis_break_routes_to_4c"],"residual_error_types_found":["policy_only_false_positive","missed_policy_bridge_structural","liquidity_break_4c_data_quality"],"loop_contribution_label":"canonical_archetype_rule_candidate","do_not_propose_new_weight_delta":false}
```

### 25.7 narrative_only row

```jsonl
{"row_type":"narrative_only","case_id":"C31_TAEYOUNG_PF_LIQUIDITY_4C_NARRATIVE","symbol":"009410","company_name":"태영건설","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","reason":"policy_support_or_PF_workout_narrative_but_forward_180D_window_sparse_or_corporate_action_contaminated","price_source":"Songdaiki/stock-web","usage":"not_weight_calibration","observed_trigger":"Taeyoung_C31_4C_2023-12-22","observed_entry_price":3070,"observed_peak_price":4110,"observed_MFE_pct":33.88,"observed_MAE_pct":-28.99}
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
completed_round = R11
completed_loop = 71
next_round = R12
next_loop = 71
round_schedule_status = valid
round_sector_consistency = pass
```

## 28. Source Notes

```text
price_source = Songdaiki/stock-web
manifest = atlas/manifest.json
manifest_max_date = 2026-02-20
price_basis = tradable_raw
price_adjustment_status = raw_unadjusted_marcap
source_basis = FinanceData/marcap transformed into assistant-readable symbol-year CSV shards
```

Stock-web rows checked directly in this loop include:

```text
005380 profile: atlas/symbol_profiles/005/005380.json
005380 2024 shard: atlas/ohlcv_tradable_by_symbol_year/005/005380/2024.csv
000270 profile: atlas/symbol_profiles/000/000270.json
000270 2024 shard: atlas/ohlcv_tradable_by_symbol_year/000/000270/2024.csv
294870 profile: atlas/symbol_profiles/294/294870.json
294870 2024 shard: atlas/ohlcv_tradable_by_symbol_year/294/294870/2024.csv
375500 profile: atlas/symbol_profiles/375/375500.json
375500 2024 shard: atlas/ohlcv_tradable_by_symbol_year/375/375500/2024.csv
009410 profile: atlas/symbol_profiles/009/009410.json
009410 2023/2024 shards: atlas/ohlcv_tradable_by_symbol_year/009/009410/2023.csv and 2024.csv
```

