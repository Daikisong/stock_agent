# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
research_session = post_calibrated_sector_archetype_residual_research
round = R13
loop = 23
large_sector_id = L6_FINANCIAL_CAPITAL_RETURN_DIGITAL
canonical_archetype_id = C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN
fine_archetype_id = REGIONAL_BANK_CAPITAL_RETURN_ROE_PBR_HOLDOUT_2025
loop_objective = holdout_validation/residual_missed_structural_mining/4B_non_price_requirement_stress_test/sector_specific_rule_discovery/canonical_archetype_compression/counterexample_mining/coverage_gap_fill
production_scoring_changed = false
shadow_weight_only = true
handoff_prompt_embedded = true
handoff_prompt_executed_now = false
stock_agent_code_access_allowed = false
stock_agent_code_patch_allowed = false
stock_agent_live_scan_allowed = false
current_stock_discovery_allowed = false
auto_trading_allowed = false
brokerage_api_allowed = false
```

This file is historical calibration research only. It is not a live candidate scan, not an investment recommendation, and not a repository patch. The loop extends the prior C21 bank-value-up file into **regional-bank / state-bank holdout validation** using actual `Songdaiki/stock-web` OHLC rows.

## 1. Current Calibrated Profile Assumption

```text
current_default_profile_proxy = e2r_2_1_stock_web_calibrated_proxy
previous_baseline_reference = e2r_2_0_baseline_reference
stage2_actionable_evidence_bonus = +2.0
stage3_yellow_total_min = 75.0
stage3_green_total_min = 87.0
stage3_green_revision_min = 55.0
stage3_cross_evidence_green_buffer = +1.5
price_only_blowoff_blocks_positive_stage = true
full_4b_requires_non_price_evidence = true
hard_4c_thesis_break_routes_to_4c = true
```

This loop does not re-prove the global Stage2 bonus or Green strictness. It asks a narrower C21 question: when a regional bank already shows capital-return / ROE-PBR rerating evidence, should Stage2 be promoted earlier, and when should a July local peak remain only a **watch-only 4B overlay** because the later full-window peak is still far ahead?

## 2. Round / Large Sector / Canonical Archetype Scope

```text
large_sector_id = L6_FINANCIAL_CAPITAL_RETURN_DIGITAL
canonical_archetype_id = C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN
fine_archetype_id = REGIONAL_BANK_CAPITAL_RETURN_ROE_PBR_HOLDOUT_2025
sector = 금융·자본배분·디지털금융
primary_archetype = regional_bank_capital_return_roe_pbr
```

Canonical compression: all selected names are C21 because the evidence is about financial-sector ROE/PBR rerating, shareholder-return or dividend capacity, capital allocation visibility, and policy/value-up optionality. The local 4B rows are risk overlays, not a separate canonical archetype.

## 3. Previous Coverage / Duplicate Avoidance Check

Allowed `stock_agent` research artifacts were checked only for coverage and duplicate avoidance. Existing calibration already has 107 parsed result MDs, 1,940 validated trigger rows, and 1,376 aggregate representative rows across R1~R13 / loops 1~9. The currently applied global axes already include Stage2 actionable bonus, stricter Green gates, full 4B non-price requirement, and hard 4C thesis-break routing.

No `src/e2r` code was opened. The immediately prior C21 loop used KB금융, 신한지주, 카카오뱅크, and 제주은행. This loop uses new independent symbols only.

```text
calibration_usable_case_count = 4
new_independent_case_count = 4
reused_case_count = 0
new_independent_case_ratio = 1.00
required_new_independent_case_ratio = 0.60
novelty_status = pass
```

## 4. Stock-Web OHLC Input / Price Source Validation

```json
{
  "source_name": "FinanceData/marcap",
  "source_repo_url": "https://github.com/FinanceData/marcap",
  "price_adjustment_status": "raw_unadjusted_marcap",
  "min_date": "1995-05-02",
  "max_date": "2026-02-20",
  "tradable_row_count": 14354401,
  "raw_row_count": 15214118,
  "symbol_count": 5414,
  "active_like_symbol_count": 2868,
  "inactive_or_delisted_like_symbol_count": 2546,
  "markets": [
    "KONEX",
    "KOSDAQ",
    "KOSDAQ GLOBAL",
    "KOSPI"
  ],
  "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year",
  "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year",
  "schema_path": "atlas/schema.json",
  "universe_path": "atlas/universe/all_symbols.csv"
}
```

Price basis used for all representative calculations:

```text
price_data_source = Songdaiki/stock-web
price_basis = tradable_raw
price_adjustment_status = raw_unadjusted_marcap
stock_web_manifest_max_date = 2026-02-20
```

The atlas manifest states that the OHLC is raw/unadjusted, zero-volume and invalid OHLC rows are excluded from calibration shards, and corporate-action-contaminated windows should be blocked. All four representative 2025-04-25 entry-to-180D windows are clean for weight calibration.

### 4.1 Symbol profile validation

|symbol|company|first_date|last_date|trading_days|corporate_action_candidate_count|corporate_action_candidate_dates|180D status|
|---:|---|---:|---:|---:|---:|---|---|
|175330|JB금융지주|2013-07-18|2026-02-20|3089|4|2014-01-29, 2014-09-26, 2015-12-01, 2018-10-26|clean_180D_window; old CA candidates outside 2025 window|
|138930|BNK금융지주|2011-03-30|2026-02-20|3663|2|2014-07-25, 2016-02-05|clean_180D_window; old CA candidates outside 2025 window|
|139130|iM금융지주|2011-06-07|2026-02-20|3617|1|2015-01-29|clean_180D_window; old CA candidate outside 2025 window; name changed from DGB금융지주 to iM금융지주 on stock-web profile history|
|024110|기업은행|1996-07-01|2026-02-20|7398|4|1998-10-27, 1998-11-05, 2000-02-02, 2003-12-24|clean_180D_window; old CA candidates outside 2025 window; 24 non-tradable zero-volume historical raw rows outside this window|

## 5. Historical Eligibility Gate

Representative Stage2 triggers pass:

```text
trigger_date_is_historical = true
entry_date_exists_in_stock_web_tradable_shard = true
forward_180D_available_by_manifest_max_date = true
high_low_close_volume_present = true
MFE_MAE_30D_90D_180D_calculated = true
corporate_action_contaminated_180D_window = false
```

The two July local-4B rows are included as machine-readable overlay rows but are `calibration_usable=false` because their forward 180D windows are not available by manifest max_date. They are risk-timing evidence only.

## 6. Canonical Archetype Compression Map

| fine_archetype | canonical_archetype_id | compression logic |
|---|---|---|
| REGIONAL_BANK_CAPITAL_RETURN_ROE_PBR_HOLDOUT_2025 | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | Regional financial holding rerating works when ROE/PBR value-up evidence is attached to distribution capacity and capital-return execution, not merely low-PBR beta. |
| STATE_BANK_DIVIDEND_VALUEUP_ROUTE | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | State-bank dividend/policy route can be positive, but should be separated from private buyback-cancellation evidence. |
| REGIONAL_BANK_PRICE_ONLY_LOCAL_4B_WATCH | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | July local overheat is a 4B watch overlay only unless non-price 4B evidence is present. |

## 7. Case Selection Summary

|case_id|symbol|company|role|case_type|current_profile_verdict|best_trigger|
|---|---:|---|---|---|---|---|
|R13L23_C21_JBFG_175330_REGIONAL_BANK_CAPITAL_RETURN|175330|JB금융지주|positive|structural_success|current_profile_too_late|T_JBFG_2025_04_25_STAGE2_ACTIONABLE|
|R13L23_C21_BNKFG_138930_LOCAL_4B_TOO_EARLY|138930|BNK금융지주|counterexample|4B_too_early|current_profile_correct|T_BNKFG_2025_04_25_STAGE2_ACTIONABLE|
|R13L23_C21_IMFG_139130_LOCAL_4B_TOO_EARLY|139130|iM금융지주|counterexample|4B_too_early|current_profile_correct|T_IMFG_2025_04_25_STAGE2_ACTIONABLE|
|R13L23_C21_IBK_024110_STATE_BANK_DIVIDEND_ROUTE|024110|기업은행|positive|structural_success|current_profile_too_late|T_IBK_2025_04_25_STAGE2_ACTIONABLE|

## 8. Positive vs Counterexample Balance

```text
positive_case_count = 2
counterexample_count = 2
4B_case_count = 2
4C_case_count = 0
minimum_positive_case_count = pass
minimum_counterexample_count = pass
minimum_calibration_usable_case_count = pass
```

The two positive cases are JB금융지주 and 기업은행, where the April 2025 entry had low MAE and large 90D/180D MFE. BNK금융지주 and iM금융지주 are counterexample/guard cases: their April Stage2 entries worked, but the July local peak was a poor full-cycle 4B because later full-window highs arrived much higher.

## 9. Evidence Source Map

| case_id | evidence class | evidence source summary | evidence fields used |
|---|---|---|---|
| R13L23_C21_JBFG_175330_REGIONAL_BANK_CAPITAL_RETURN | positive | FY2024/1Q2025 regional-bank value-up, shareholder-return and ROE/PBR framing; validated by stock-web OHLC. | public_event_or_disclosure, policy_or_regulatory_optionality, relative_strength, early_revision_signal, financial_visibility |
| R13L23_C21_BNKFG_138930_LOCAL_4B_TOO_EARLY | counterexample / 4B stress | April route works, but July local peak should be watch-only because later full-window peak was much higher. | public_event_or_disclosure, relative_strength, price_only_local_peak, positioning_overheat |
| R13L23_C21_IMFG_139130_LOCAL_4B_TOO_EARLY | counterexample / 4B stress | iM/DGB transition plus value-up route works, but local price-only 4B is too early without non-price evidence. | public_event_or_disclosure, relative_strength, price_only_local_peak, positioning_overheat |
| R13L23_C21_IBK_024110_STATE_BANK_DIVIDEND_ROUTE | positive / route separation | State-bank dividend/value-up route validates C21, but should not be merged blindly with private-bank buyback-cancellation scoring. | public_event_or_disclosure, policy_or_regulatory_optionality, relative_strength, financial_visibility |

## 10. Price Data Source Map

|symbol|company|profile_path|representative shard paths|profile window status|
|---:|---|---|---|---|
|175330|JB금융지주|atlas/symbol_profiles/175/175330.json|atlas/ohlcv_tradable_by_symbol_year/175/175330/2025.csv; 2026.csv|clean_180D_window; old CA candidates outside 2025 window|
|138930|BNK금융지주|atlas/symbol_profiles/138/138930.json|atlas/ohlcv_tradable_by_symbol_year/138/138930/2025.csv; 2026.csv|clean_180D_window; old CA candidates outside 2025 window|
|139130|iM금융지주|atlas/symbol_profiles/139/139130.json|atlas/ohlcv_tradable_by_symbol_year/139/139130/2025.csv; 2026.csv|clean_180D_window; old CA candidate outside 2025 window; name changed from DGB금융지주 to iM금융지주 on stock-web profile history|
|024110|기업은행|atlas/symbol_profiles/024/024110.json|atlas/ohlcv_tradable_by_symbol_year/024/024110/2025.csv; 2026.csv|clean_180D_window; old CA candidates outside 2025 window; 24 non-tradable zero-volume historical raw rows outside this window|

## 11. Case-by-Case Trigger Grid

|trigger_id|symbol|trigger_type|entry_date|entry_price|MFE30|MFE90|MFE180|MAE30|MAE90|MAE180|outcome|current_profile|aggregate|
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|---|
|T_JBFG_2025_04_25_STAGE2_ACTIONABLE|175330|Stage2-Actionable|2025-04-25|17070|26.24|53.78|55.54|-1.87|-1.87|-1.87|structural_success_high_MFE_low_MAE|current_profile_too_late|True|
|T_BNKFG_2025_04_25_STAGE2_ACTIONABLE|138930|Stage2-Actionable|2025-04-25|10570|12.77|51.84|55.25|-6.53|-6.53|-6.53|local_4b_too_early_but_structural_path_survived|current_profile_correct|True|
|T_IMFG_2025_04_25_STAGE2_ACTIONABLE|139130|Stage2-Actionable|2025-04-25|9710|20.29|60.66|64.37|-1.75|-1.75|-1.75|local_4b_too_early_after_name_change_valueup_route|current_profile_correct|True|
|T_IBK_2025_04_25_STAGE2_ACTIONABLE|024110|Stage2-Actionable|2025-04-25|14970|13.83|49.63|49.63|-0.67|-0.67|-0.67|state_bank_dividend_route_structural_success|current_profile_too_late|True|

## 12. Trigger-Level OHLC Backtest Tables

### 12.1 Representative trigger metrics

|trigger_id|entry|entry_price|peak_date|peak_price|MFE_30D|MFE_90D|MFE_180D|MAE_30D|MAE_90D|MAE_180D|drawdown_after_peak|
|---|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|
|T_JBFG_2025_04_25_STAGE2_ACTIONABLE|2025-04-25|17070|2026-02-20|38500|26.24|53.78|55.54|-1.87|-1.87|-1.87|0.0|
|T_BNKFG_2025_04_25_STAGE2_ACTIONABLE|2025-04-25|10570|2026-02-20|23050|12.77|51.84|55.25|-6.53|-6.53|-6.53|0.0|
|T_IMFG_2025_04_25_STAGE2_ACTIONABLE|2025-04-25|9710|2026-02-20|21800|20.29|60.66|64.37|-1.75|-1.75|-1.75|0.0|
|T_IBK_2025_04_25_STAGE2_ACTIONABLE|2025-04-25|14970|2026-02-20|28700|13.83|49.63|49.63|-0.67|-0.67|-0.67|0.0|

Interpretation:

- JB금융지주: 2025-04-25 close 17,070 → 90D max high 26,250 and 180D max high 26,550. This is a clean Stage2-Actionable candidate with shallow MAE.
- BNK금융지주: 2025-04-25 close 10,570 → 90D max high 16,050 and 180D max high 16,410, but the full observed high was 23,050 on 2026-02-20. July local overheat was not full 4B.
- iM금융지주: 2025-04-25 close 9,710 → 90D max high 15,600 and 180D max high 15,960, while full observed high reached 21,800 by 2026-02-20. Again, local 4B was too early.
- 기업은행: 2025-04-25 close 14,970 → 90D and 180D max high 22,400, with only -0.67% MAE in the representative window. State-bank route should be positive but separately labelled.

## 13. Current Calibrated Profile Stress Test

| question | result |
|---|---|
| 1. How would current calibrated profile judge these cases? | It would generally keep price-only 4B from becoming full 4B, but may be too slow to promote regional-bank Stage2 when actual capital-return/value-up evidence already exists. |
| 2. Did that match actual MFE/MAE? | Mostly. April entries showed strong MFE and shallow MAE. July local 4B rows would have been too early if treated as full 4B. |
| 3. Was Stage2 bonus too much or too little? | Too little for JB/IBK-style confirmed regional/state-bank evidence; adequate if local 4B is blocked. |
| 4. Was Yellow threshold 75 too strict/loose? | Kept globally. C21 needs component gating rather than a global threshold change. |
| 5. Was Green threshold/revision too strict/loose? | Kept. Green should stay strict, but Stage2-Actionable can receive a C21 shadow bonus when distribution execution is already visible. |
| 6. Was price-only blowoff guard adequate? | Adequate; this loop strengthens it for July regional-bank local peaks. |
| 7. Was full 4B non-price requirement adequate? | Adequate; BNK/iM local peaks had high local proximity but low full-window proximity. |
| 8. Was hard 4C routing too late/overdone? | No hard 4C row is proposed. These are 4B/watch-only cases, not thesis-break 4C. |

```text
current_profile_correct = 2
current_profile_too_late = 2
current_profile_false_positive = 0
current_profile_error_count = 2
```

## 14. Stage2 / Yellow / Green Comparison

No clean Stage3-Green comparison trigger is counted for weight in this loop because the most natural confirmation windows after the late-June/July move do not have forward 180D available by stock-web manifest max_date. Therefore representative rows use:

```text
green_lateness_ratio = not_applicable:no_clean_180D_stage3_green_trigger_after_confirmation_window
```

Qualitative timing: Green was probably not needed for first entry in JB/IBK because the April Stage2 entries already had high MFE/low MAE. For BNK/iM, the Stage2 entry was valid, but July local overheat needed a watch-only 4B overlay rather than a full exit label.

## 15. 4B Local vs Full-window Timing Audit

| trigger_id | Stage2 entry | 4B local entry | local peak | full observed peak | local proximity | full-window proximity | verdict |
|---|---:|---:|---:|---:|---:|---:|---|
| T_BNKFG_2025_07_15_LOCAL_4B_WATCH_ONLY | 10570 | 15950 | 16050 | 23050 | 0.982 | 0.431 | price_only_local_4B_too_early |
| T_IMFG_2025_07_15_LOCAL_4B_WATCH_ONLY | 9710 | 15510 | 15600 | 21800 | 0.985 | 0.480 | price_only_local_4B_too_early |

The mechanism is important. A local July peak looked like a boiling kettle, but the later February peak shows the pot was not finished cooking. Without non-price 4B evidence—capital raise, contract/legal block, revision slowdown, or explicit execution-risk deterioration—local price heat should be `watch_only`, not full 4B.

## 16. 4C Protection Audit

No hard 4C trigger is proposed.

```text
four_c_protection_label = thesis_break_watch_only
hard_4c_success = not_applicable
hard_4c_late = not_applicable
```

The loop is about C21 positive-stage timing and 4B local/full separation, not thesis-break routing.

## 17. Sector-Specific Rule Candidate

```text
sector_specific_rule_candidate = true
rule_scope = sector_specific
axis = c21_state_bank_dividend_route_separation
```

Proposed shadow rule: In L6, state-bank dividend/value-up evidence can be positive when actual MFE/MAE validates it, but it should be labelled as a separate route from private financial-holding buyback-cancellation execution. Otherwise the model may overfit any low-PBR state-policy beta as if it were recurring private capital allocation.

## 18. Canonical-Archetype Rule Candidate

```text
canonical_archetype_rule_candidate = true
rule_scope = canonical_archetype_specific
axis_1 = c21_regional_bank_capital_return_execution_bonus
axis_2 = c21_local_4b_watch_only_guard
```

C21 shadow rule candidate:

1. **Promote Stage2-Actionable only when capital-return execution is visible.** Low-PBR + policy beta is not enough. Evidence must include distribution route, recurring dividend/buyback/cancellation framing, capital ratio capacity, or ROE/PBR value-up materials.
2. **Do not convert a local bank spike into full 4B unless non-price 4B evidence exists.** BNK/iM show why: local proximity was very high, but full-window proximity was below 0.50.

## 19. Before / After Backtest Comparison

|profile_id|profile_scope|hypothesis|eligible_trigger_count|avg_MFE_90D_pct|avg_MAE_90D_pct|avg_MFE_180D_pct|avg_MAE_180D_pct|false_positive_rate|missed_structural_count|late_green_count|avg_green_lateness_ratio|score_return_alignment_verdict|
|---|---|---|---:|---:|---:|---:|---:|---|---:|---:|---|---|
|P0|global_current_proxy|Current e2r_2_1 profile, without regional-bank split of capital-return execution vs local overheat.|4|53.98|-2.71|56.2|-2.71|0/4 for Stage2 representatives; 2 local 4B rows blocked as watch-only|2|2|not_applicable|mixed_but_usable|
|P0b|rollback_reference|E2R 2.0 reference; likely overweights low-PBR beta and under-weights actual distribution execution.|4|53.98|-2.71|56.2|-2.71|0/4 for Stage2 representatives; 2 local 4B rows blocked as watch-only|2|2|not_applicable|weak|
|P1|sector_specific_candidate_profile|L6 regional-bank profile with capital-return execution bonus and state-bank route separation.|4|53.98|-2.71|56.2|-2.71|0/4 for Stage2 representatives; 2 local 4B rows blocked as watch-only|0|0|not_applicable|improved|
|P2|canonical_archetype_candidate_profile|C21-specific ROE/PBR rerating profile with local-4B watch-only guard.|4|53.98|-2.71|56.2|-2.71|0/4 for Stage2 representatives; 2 local 4B rows blocked as watch-only|0|0|not_applicable|best|
|P3|counterexample_guard_profile|Guard that prevents July price-only local peaks from becoming full 4B exits without non-price evidence.|4|53.98|-2.71|56.2|-2.71|0/4 for Stage2 representatives; 2 local 4B rows blocked as watch-only|0|0|not_applicable|guard_useful|

## 20. Score-Return Alignment Matrix

| case | current profile issue | proposed shadow effect | return alignment |
|---|---|---|---|
| JB금융지주 | too late if waiting for Green | C21 execution bonus allows Stage2-Actionable | high MFE / shallow MAE |
| BNK금융지주 | local 4B could look tempting | watch-only 4B guard avoids premature full exit | later full peak much higher |
| iM금융지주 | local 4B could look tempting | watch-only 4B guard avoids premature full exit | later full peak much higher |
| 기업은행 | state-bank route can be conflated | separate state-bank dividend route | high MFE / shallow MAE |

## 21. Coverage Matrix

|large_sector_id|canonical_archetype_id|fine_archetype_id|positive_case_count|counterexample_count|4B_case_count|4C_case_count|new_independent_case_count|reused_case_count|calibration_usable_trigger_count|representative_trigger_count|current_profile_error_count|sector_rule_candidate|canonical_rule_candidate|coverage_gap_after_this_loop|
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---|
|L6_FINANCIAL_CAPITAL_RETURN_DIGITAL|C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN|REGIONAL_BANK_CAPITAL_RETURN_ROE_PBR_HOLDOUT_2025|2|2|2|0|4|0|4|4|2|true|true|Need later regional-bank 2026 validation once 180D windows after February 2026 peaks exist.|

## 22. Residual Contribution Summary

```text
new_independent_case_count: 4
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 4
new_canonical_archetype_count: 0
new_fine_archetype_count: 1
new_trigger_family_count: 3
tested_existing_calibrated_axes: stage2_actionable_evidence_bonus, stage3_yellow_total_min, stage3_green_total_min, stage3_green_revision_min, price_only_blowoff_blocks_positive_stage, full_4b_requires_non_price_evidence, hard_4c_thesis_break_routes_to_4c
residual_error_types_found: regional_bank_stage2_too_late_when_capital_return_execution_visible, price_only_local_4b_too_early_vs_full_window_peak, state_bank_dividend_route_should_not_merge_with_private_buyback_route
new_axis_proposed: c21_regional_bank_capital_return_execution_bonus, c21_local_4b_watch_only_guard, c21_state_bank_dividend_route_separation
existing_axis_strengthened: price_only_blowoff_blocks_positive_stage, full_4b_requires_non_price_evidence
existing_axis_weakened: null
existing_axis_kept: stage3_yellow_total_min, stage3_green_total_min, stage3_green_revision_min, hard_4c_thesis_break_routes_to_4c
sector_specific_rule_candidate: true
canonical_archetype_rule_candidate: true
no_new_signal_reason: null
loop_contribution_label: canonical_archetype_rule_candidate
```

## 23. Validation Scope / Non-Validation Scope

Validated:

```text
- Actual stock-web 1D OHLC rows for 175330, 138930, 139130, 024110.
- Entry date = 2025-04-25 close for representative rows.
- 30D / 90D / 180D MFE/MAE.
- Manifest max_date = 2026-02-20.
- Corporate-action window status from symbol profiles.
- Local vs full-window 4B proximity for BNK/iM.
```

Not validated:

```text
- No current/live stock recommendation.
- No live watchlist.
- No brokerage API connection.
- No stock_agent code inspection or patch.
- No production scoring change.
- July local-4B overlay rows are not used for quantitative weight calibration due insufficient forward 180D from those July entries.
```

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,c21_regional_bank_capital_return_execution_bonus,canonical_archetype_specific,L6_FINANCIAL_CAPITAL_RETURN_DIGITAL,C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN,0,1,+1,"Regional-bank C21 Stage2 should receive a shadow bonus only when public capital-return/value-up execution and ROE/PBR framing are visible, not just low-PBR policy beta.","JB and IBK April 2025 entries show high 90D/180D MFE with shallow MAE.","T_JBFG_2025_04_25_STAGE2_ACTIONABLE|T_IBK_2025_04_25_STAGE2_ACTIONABLE",2,2,0,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,c21_local_4b_watch_only_guard,canonical_archetype_specific,L6_FINANCIAL_CAPITAL_RETURN_DIGITAL,C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN,0,1,+1,"A July 2025 regional-bank local peak had high local proximity but low full-window proximity; without non-price 4B evidence it should be watch-only, not full 4B.","Prevents BNK/iM July local overheat from prematurely ending the later February 2026 full-window rerating.","T_BNKFG_2025_07_15_LOCAL_4B_WATCH_ONLY|T_IMFG_2025_07_15_LOCAL_4B_WATCH_ONLY",2,2,2,medium,canonical_shadow_only,"4B overlay rows are narrative-only for weight due to insufficient forward 180D from July entries"
shadow_weight,c21_state_bank_dividend_route_separation,sector_specific,L6_FINANCIAL_CAPITAL_RETURN_DIGITAL,C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN,0,1,+1,"State-bank dividend/value-up evidence can be positive but should not train the same buyback-cancellation route as private financial holding companies.","Keeps IBK positive while preventing over-broad extrapolation from state ownership policy beta.","T_IBK_2025_04_25_STAGE2_ACTIONABLE",1,1,0,low,sector_shadow_only,"not production; post-calibrated residual"
```

## 25. Machine-Readable Rows

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration"}
{"row_type": "case", "case_id": "R13L23_C21_JBFG_175330_REGIONAL_BANK_CAPITAL_RETURN", "symbol": "175330", "company_name": "JB금융지주", "round": "R13", "loop": "23", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "fine_archetype_id": "REGIONAL_BANK_CAPITAL_RETURN_ROE_PBR_HOLDOUT_2025", "case_type": "structural_success", "positive_or_counterexample": "positive", "best_trigger": "T_JBFG_2025_04_25_STAGE2_ACTIONABLE", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "structural_success_high_MFE_low_MAE", "current_profile_verdict": "current_profile_too_late", "price_source": "Songdaiki/stock-web", "notes": "2025 regional-bank value-up/capital-return and earnings context was already visible by 2025-04-25; the stock-web row then produced high 90D/180D MFE with shallow MAE."}
{"row_type": "case", "case_id": "R13L23_C21_BNKFG_138930_LOCAL_4B_TOO_EARLY", "symbol": "138930", "company_name": "BNK금융지주", "round": "R13", "loop": "23", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "fine_archetype_id": "REGIONAL_BANK_CAPITAL_RETURN_ROE_PBR_HOLDOUT_2025", "case_type": "4B_too_early", "positive_or_counterexample": "counterexample", "best_trigger": "T_BNKFG_2025_04_25_STAGE2_ACTIONABLE", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "local_4b_too_early_but_structural_path_survived", "current_profile_verdict": "current_profile_correct", "price_source": "Songdaiki/stock-web", "notes": "The April entry worked, but the July local peak was not a full-cycle 4B because the full observed-window peak arrived later in February 2026."}
{"row_type": "case", "case_id": "R13L23_C21_IMFG_139130_LOCAL_4B_TOO_EARLY", "symbol": "139130", "company_name": "iM금융지주", "round": "R13", "loop": "23", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "fine_archetype_id": "REGIONAL_BANK_CAPITAL_RETURN_ROE_PBR_HOLDOUT_2025", "case_type": "4B_too_early", "positive_or_counterexample": "counterexample", "best_trigger": "T_IMFG_2025_04_25_STAGE2_ACTIONABLE", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "local_4b_too_early_after_name_change_valueup_route", "current_profile_verdict": "current_profile_correct", "price_source": "Songdaiki/stock-web", "notes": "The April iM/DGB transition and regional-bank value-up path worked, but the July local high looked like a price-only 4B that would have exited too early versus the later full-window peak."}
{"row_type": "case", "case_id": "R13L23_C21_IBK_024110_STATE_BANK_DIVIDEND_ROUTE", "symbol": "024110", "company_name": "기업은행", "round": "R13", "loop": "23", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "fine_archetype_id": "REGIONAL_BANK_CAPITAL_RETURN_ROE_PBR_HOLDOUT_2025", "case_type": "structural_success", "positive_or_counterexample": "positive", "best_trigger": "T_IBK_2025_04_25_STAGE2_ACTIONABLE", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "state_bank_dividend_route_structural_success", "current_profile_verdict": "current_profile_too_late", "price_source": "Songdaiki/stock-web", "notes": "State-bank dividend/value-up route was usable as C21 evidence, but it should be separated from private regional-bank buyback-cancellation evidence rather than merged blindly."}
{"row_type": "trigger", "trigger_id": "T_JBFG_2025_04_25_STAGE2_ACTIONABLE", "case_id": "R13L23_C21_JBFG_175330_REGIONAL_BANK_CAPITAL_RETURN", "symbol": "175330", "company_name": "JB금융지주", "round": "R13", "loop": "23", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "fine_archetype_id": "REGIONAL_BANK_CAPITAL_RETURN_ROE_PBR_HOLDOUT_2025", "sector": "금융·자본배분·디지털금융", "primary_archetype": "regional_bank_capital_return_roe_pbr", "loop_objective": "holdout_validation/residual_missed_structural_mining/4B_non_price_requirement_stress_test/sector_specific_rule_discovery/canonical_archetype_compression/counterexample_mining/coverage_gap_fill", "trigger_type": "Stage2-Actionable", "trigger_date": "2025-04-25", "evidence_available_at_that_date": "2025 regional-bank value-up/capital-return and earnings context was already visible by 2025-04-25; the stock-web row then produced high 90D/180D MFE with shallow MAE.", "evidence_source": "Historical public-evidence proxy: FY2024/1Q2025 earnings, value-up/shareholder-return materials, and stock-web OHLC validation; not a live scan.", "stage2_evidence_fields": ["public_event_or_disclosure", "policy_or_regulatory_optionality", "relative_strength", "early_revision_signal", "backlog_or_delivery_visibility"], "stage3_evidence_fields": ["financial_visibility"], "stage4b_evidence_fields": [], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/175/175330/2025.csv; atlas/ohlcv_tradable_by_symbol_year/175/175330/2026.csv", "profile_path": "atlas/symbol_profiles/175/175330.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2025-04-25", "entry_price": 17070, "MFE_30D_pct": 26.24, "MFE_90D_pct": 53.78, "MFE_180D_pct": 55.54, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -1.87, "MAE_90D_pct": -1.87, "MAE_180D_pct": -1.87, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2026-02-20", "peak_price": 38500, "drawdown_after_peak_pct": 0.0, "green_lateness_ratio": "not_applicable:no_clean_180D_stage3_green_trigger_after_confirmation_window", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "not_applicable_for_stage2_representative", "four_b_evidence_type": [], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "structural_success_high_MFE_low_MAE", "current_profile_verdict": "current_profile_too_late", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window; profile has only old corporate-action candidate dates outside entry-to-180D window", "same_entry_group_id": "G_175330_2025_04_25", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "T_BNKFG_2025_04_25_STAGE2_ACTIONABLE", "case_id": "R13L23_C21_BNKFG_138930_LOCAL_4B_TOO_EARLY", "symbol": "138930", "company_name": "BNK금융지주", "round": "R13", "loop": "23", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "fine_archetype_id": "REGIONAL_BANK_CAPITAL_RETURN_ROE_PBR_HOLDOUT_2025", "sector": "금융·자본배분·디지털금융", "primary_archetype": "regional_bank_capital_return_roe_pbr", "loop_objective": "holdout_validation/residual_missed_structural_mining/4B_non_price_requirement_stress_test/sector_specific_rule_discovery/canonical_archetype_compression/counterexample_mining/coverage_gap_fill", "trigger_type": "Stage2-Actionable", "trigger_date": "2025-04-25", "evidence_available_at_that_date": "The April entry worked, but the July local peak was not a full-cycle 4B because the full observed-window peak arrived later in February 2026.", "evidence_source": "Historical public-evidence proxy: FY2024/1Q2025 earnings, value-up/shareholder-return materials, and stock-web OHLC validation; not a live scan.", "stage2_evidence_fields": ["public_event_or_disclosure", "policy_or_regulatory_optionality", "relative_strength", "early_revision_signal"], "stage3_evidence_fields": ["financial_visibility"], "stage4b_evidence_fields": ["price_only_local_peak", "positioning_overheat"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/138/138930/2025.csv; atlas/ohlcv_tradable_by_symbol_year/138/138930/2026.csv", "profile_path": "atlas/symbol_profiles/138/138930.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2025-04-25", "entry_price": 10570, "MFE_30D_pct": 12.77, "MFE_90D_pct": 51.84, "MFE_180D_pct": 55.25, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -6.53, "MAE_90D_pct": -6.53, "MAE_180D_pct": -6.53, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2026-02-20", "peak_price": 23050, "drawdown_after_peak_pct": 0.0, "green_lateness_ratio": "not_applicable:no_clean_180D_stage3_green_trigger_after_confirmation_window", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "not_applicable_for_stage2_representative", "four_b_evidence_type": [], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "local_4b_too_early_but_structural_path_survived", "current_profile_verdict": "current_profile_correct", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window; profile has only old corporate-action candidate dates outside entry-to-180D window", "same_entry_group_id": "G_138930_2025_04_25", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "T_IMFG_2025_04_25_STAGE2_ACTIONABLE", "case_id": "R13L23_C21_IMFG_139130_LOCAL_4B_TOO_EARLY", "symbol": "139130", "company_name": "iM금융지주", "round": "R13", "loop": "23", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "fine_archetype_id": "REGIONAL_BANK_CAPITAL_RETURN_ROE_PBR_HOLDOUT_2025", "sector": "금융·자본배분·디지털금융", "primary_archetype": "regional_bank_capital_return_roe_pbr", "loop_objective": "holdout_validation/residual_missed_structural_mining/4B_non_price_requirement_stress_test/sector_specific_rule_discovery/canonical_archetype_compression/counterexample_mining/coverage_gap_fill", "trigger_type": "Stage2-Actionable", "trigger_date": "2025-04-25", "evidence_available_at_that_date": "The April iM/DGB transition and regional-bank value-up path worked, but the July local high looked like a price-only 4B that would have exited too early versus the later full-window peak.", "evidence_source": "Historical public-evidence proxy: FY2024/1Q2025 earnings, value-up/shareholder-return materials, and stock-web OHLC validation; not a live scan.", "stage2_evidence_fields": ["public_event_or_disclosure", "policy_or_regulatory_optionality", "relative_strength", "early_revision_signal"], "stage3_evidence_fields": ["financial_visibility"], "stage4b_evidence_fields": ["price_only_local_peak", "positioning_overheat"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/139/139130/2025.csv; atlas/ohlcv_tradable_by_symbol_year/139/139130/2026.csv", "profile_path": "atlas/symbol_profiles/139/139130.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2025-04-25", "entry_price": 9710, "MFE_30D_pct": 20.29, "MFE_90D_pct": 60.66, "MFE_180D_pct": 64.37, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -1.75, "MAE_90D_pct": -1.75, "MAE_180D_pct": -1.75, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2026-02-20", "peak_price": 21800, "drawdown_after_peak_pct": 0.0, "green_lateness_ratio": "not_applicable:no_clean_180D_stage3_green_trigger_after_confirmation_window", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "not_applicable_for_stage2_representative", "four_b_evidence_type": [], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "local_4b_too_early_after_name_change_valueup_route", "current_profile_verdict": "current_profile_correct", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window; profile has only old corporate-action candidate dates outside entry-to-180D window", "same_entry_group_id": "G_139130_2025_04_25", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "T_IBK_2025_04_25_STAGE2_ACTIONABLE", "case_id": "R13L23_C21_IBK_024110_STATE_BANK_DIVIDEND_ROUTE", "symbol": "024110", "company_name": "기업은행", "round": "R13", "loop": "23", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "fine_archetype_id": "REGIONAL_BANK_CAPITAL_RETURN_ROE_PBR_HOLDOUT_2025", "sector": "금융·자본배분·디지털금융", "primary_archetype": "regional_bank_capital_return_roe_pbr", "loop_objective": "holdout_validation/residual_missed_structural_mining/4B_non_price_requirement_stress_test/sector_specific_rule_discovery/canonical_archetype_compression/counterexample_mining/coverage_gap_fill", "trigger_type": "Stage2-Actionable", "trigger_date": "2025-04-25", "evidence_available_at_that_date": "State-bank dividend/value-up route was usable as C21 evidence, but it should be separated from private regional-bank buyback-cancellation evidence rather than merged blindly.", "evidence_source": "Historical public-evidence proxy: FY2024/1Q2025 earnings, value-up/shareholder-return materials, and stock-web OHLC validation; not a live scan.", "stage2_evidence_fields": ["public_event_or_disclosure", "policy_or_regulatory_optionality", "relative_strength", "early_revision_signal"], "stage3_evidence_fields": ["financial_visibility"], "stage4b_evidence_fields": [], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/024/024110/2025.csv; atlas/ohlcv_tradable_by_symbol_year/024/024110/2026.csv", "profile_path": "atlas/symbol_profiles/024/024110.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2025-04-25", "entry_price": 14970, "MFE_30D_pct": 13.83, "MFE_90D_pct": 49.63, "MFE_180D_pct": 49.63, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -0.67, "MAE_90D_pct": -0.67, "MAE_180D_pct": -0.67, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2026-02-20", "peak_price": 28700, "drawdown_after_peak_pct": 0.0, "green_lateness_ratio": "not_applicable:no_clean_180D_stage3_green_trigger_after_confirmation_window", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "not_applicable_for_stage2_representative", "four_b_evidence_type": [], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "state_bank_dividend_route_structural_success", "current_profile_verdict": "current_profile_too_late", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window; profile has only old corporate-action candidate dates outside entry-to-180D window", "same_entry_group_id": "G_024110_2025_04_25", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "T_BNKFG_2025_07_15_LOCAL_4B_WATCH_ONLY", "case_id": "R13L23_C21_BNKFG_138930_LOCAL_4B_TOO_EARLY", "symbol": "138930", "company_name": "BNK금융지주", "round": "R13", "loop": "23", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "fine_archetype_id": "REGIONAL_BANK_CAPITAL_RETURN_ROE_PBR_HOLDOUT_2025", "sector": "금융·자본배분·디지털금융", "primary_archetype": "regional_bank_capital_return_roe_pbr", "loop_objective": "4B_non_price_requirement_stress_test", "trigger_type": "Stage4B-local-watch", "trigger_date": "2025-07-15", "evidence_available_at_that_date": "Local July 2025 price/positioning overheat without non-price full-4B evidence; later full-window peak invalidated treating this as a full exit signal.", "evidence_source": "Stock-web OHLC local-vs-full peak timing audit; no production scoring change.", "stage2_evidence_fields": ["relative_strength"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["price_only_local_peak", "positioning_overheat"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/138/138930/2025.csv; atlas/ohlcv_tradable_by_symbol_year/138/138930/2026.csv", "profile_path": "atlas/symbol_profiles/138/138930.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2025-07-15", "entry_price": 15950, "MFE_30D_pct": null, "MFE_90D_pct": null, "MFE_180D_pct": null, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": null, "MAE_90D_pct": null, "MAE_180D_pct": null, "MAE_1Y_pct": null, "below_entry_price_flag_30D": null, "below_entry_price_flag_90D": null, "peak_date": null, "peak_price": null, "drawdown_after_peak_pct": -14.95, "green_lateness_ratio": "not_applicable:4B_overlay_only", "four_b_local_peak_proximity": 0.982, "four_b_full_window_peak_proximity": 0.431, "four_b_timing_verdict": "price_only_local_4B_too_early", "four_b_evidence_type": ["price_only", "positioning_overheat"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "price_only_local_4B_too_early", "current_profile_verdict": "current_profile_correct", "calibration_usable": false, "forward_window_trading_days": null, "calibration_block_reasons": ["insufficient_forward_window_in_stock_web_for_July_4B_entry"], "corporate_action_window_status": "clean_window_but_forward_180D_unavailable", "same_entry_group_id": "G_138930_2025_07_15_4B", "dedupe_for_aggregate": false, "aggregate_group_role": "4B_overlay_only", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "T_IMFG_2025_07_15_LOCAL_4B_WATCH_ONLY", "case_id": "R13L23_C21_IMFG_139130_LOCAL_4B_TOO_EARLY", "symbol": "139130", "company_name": "iM금융지주", "round": "R13", "loop": "23", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "fine_archetype_id": "REGIONAL_BANK_CAPITAL_RETURN_ROE_PBR_HOLDOUT_2025", "sector": "금융·자본배분·디지털금융", "primary_archetype": "regional_bank_capital_return_roe_pbr", "loop_objective": "4B_non_price_requirement_stress_test", "trigger_type": "Stage4B-local-watch", "trigger_date": "2025-07-15", "evidence_available_at_that_date": "Local July 2025 price/positioning overheat without non-price full-4B evidence; later full-window peak invalidated treating this as a full exit signal.", "evidence_source": "Stock-web OHLC local-vs-full peak timing audit; no production scoring change.", "stage2_evidence_fields": ["relative_strength"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["price_only_local_peak", "positioning_overheat"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/139/139130/2025.csv; atlas/ohlcv_tradable_by_symbol_year/139/139130/2026.csv", "profile_path": "atlas/symbol_profiles/139/139130.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2025-07-15", "entry_price": 15510, "MFE_30D_pct": null, "MFE_90D_pct": null, "MFE_180D_pct": null, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": null, "MAE_90D_pct": null, "MAE_180D_pct": null, "MAE_1Y_pct": null, "below_entry_price_flag_30D": null, "below_entry_price_flag_90D": null, "peak_date": null, "peak_price": null, "drawdown_after_peak_pct": -16.35, "green_lateness_ratio": "not_applicable:4B_overlay_only", "four_b_local_peak_proximity": 0.985, "four_b_full_window_peak_proximity": 0.48, "four_b_timing_verdict": "price_only_local_4B_too_early", "four_b_evidence_type": ["price_only", "positioning_overheat"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "price_only_local_4B_too_early", "current_profile_verdict": "current_profile_correct", "calibration_usable": false, "forward_window_trading_days": null, "calibration_block_reasons": ["insufficient_forward_window_in_stock_web_for_July_4B_entry"], "corporate_action_window_status": "clean_window_but_forward_180D_unavailable", "same_entry_group_id": "G_139130_2025_07_15_4B", "dedupe_for_aggregate": false, "aggregate_group_role": "4B_overlay_only", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R13L23_C21_JBFG_175330_REGIONAL_BANK_CAPITAL_RETURN", "trigger_id": "T_JBFG_2025_04_25_STAGE2_ACTIONABLE", "symbol": "175330", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 13, "relative_strength_score": 20, "customer_quality_score": 0, "policy_or_regulatory_score": 12, "valuation_repricing_score": 16, "execution_risk_score": -2, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 82, "stage_label_before": "Stage3-Yellow", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 13, "relative_strength_score": 20, "customer_quality_score": 0, "policy_or_regulatory_score": 15, "valuation_repricing_score": 18, "execution_risk_score": -2, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 88, "stage_label_after": "Stage3-Green-shadow", "changed_components": ["policy_or_regulatory_score", "valuation_repricing_score"], "component_delta_explanation": "C21 regional-bank shadow profile separates true capital-return execution from broad value-up beta and price-only local 4B overheat.", "MFE_90D_pct": 53.78, "MAE_90D_pct": -1.87, "score_return_alignment_label": "structural_success_high_MFE_low_MAE", "current_profile_verdict": "current_profile_too_late"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R13L23_C21_BNKFG_138930_LOCAL_4B_TOO_EARLY", "trigger_id": "T_BNKFG_2025_04_25_STAGE2_ACTIONABLE", "symbol": "138930", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 10, "relative_strength_score": 22, "customer_quality_score": 0, "policy_or_regulatory_score": 11, "valuation_repricing_score": 18, "execution_risk_score": -4, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 80, "stage_label_before": "Stage3-Yellow-risk", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 10, "relative_strength_score": 22, "customer_quality_score": 0, "policy_or_regulatory_score": 11, "valuation_repricing_score": 16, "execution_risk_score": -8, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 76, "stage_label_after": "Stage2-Actionable-plus-4B-watch", "changed_components": ["execution_risk_score", "valuation_repricing_score"], "component_delta_explanation": "C21 regional-bank shadow profile separates true capital-return execution from broad value-up beta and price-only local 4B overheat.", "MFE_90D_pct": 51.84, "MAE_90D_pct": -6.53, "score_return_alignment_label": "local_4b_too_early_but_structural_path_survived", "current_profile_verdict": "current_profile_correct"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R13L23_C21_IMFG_139130_LOCAL_4B_TOO_EARLY", "trigger_id": "T_IMFG_2025_04_25_STAGE2_ACTIONABLE", "symbol": "139130", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 10, "relative_strength_score": 22, "customer_quality_score": 0, "policy_or_regulatory_score": 11, "valuation_repricing_score": 18, "execution_risk_score": -4, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 80, "stage_label_before": "Stage3-Yellow-risk", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 10, "relative_strength_score": 22, "customer_quality_score": 0, "policy_or_regulatory_score": 11, "valuation_repricing_score": 16, "execution_risk_score": -8, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 76, "stage_label_after": "Stage2-Actionable-plus-4B-watch", "changed_components": ["execution_risk_score", "valuation_repricing_score"], "component_delta_explanation": "C21 regional-bank shadow profile separates true capital-return execution from broad value-up beta and price-only local 4B overheat.", "MFE_90D_pct": 60.66, "MAE_90D_pct": -1.75, "score_return_alignment_label": "local_4b_too_early_after_name_change_valueup_route", "current_profile_verdict": "current_profile_correct"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R13L23_C21_IBK_024110_STATE_BANK_DIVIDEND_ROUTE", "trigger_id": "T_IBK_2025_04_25_STAGE2_ACTIONABLE", "symbol": "024110", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 10, "relative_strength_score": 18, "customer_quality_score": 0, "policy_or_regulatory_score": 14, "valuation_repricing_score": 13, "execution_risk_score": -5, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 79, "stage_label_before": "Stage3-Yellow", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 10, "relative_strength_score": 18, "customer_quality_score": 0, "policy_or_regulatory_score": 16, "valuation_repricing_score": 14, "execution_risk_score": -7, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 84, "stage_label_after": "Stage3-Yellow/Actionable-shadow", "changed_components": ["policy_or_regulatory_score", "valuation_repricing_score", "execution_risk_score"], "component_delta_explanation": "C21 regional-bank shadow profile separates true capital-return execution from broad value-up beta and price-only local 4B overheat.", "MFE_90D_pct": 49.63, "MAE_90D_pct": -0.67, "score_return_alignment_label": "state_bank_dividend_route_structural_success", "current_profile_verdict": "current_profile_too_late"}
{"row_type": "aggregate", "profile_id": "P0", "profile_scope": "global_current_proxy", "profile_hypothesis": "Current e2r_2_1 profile, without regional-bank split of capital-return execution vs local overheat.", "changed_axes": ["c21_regional_bank_capital_return_execution_bonus", "c21_local_4b_watch_only_guard", "c21_state_bank_dividend_route_separation"], "changed_thresholds": [], "eligible_trigger_count": 4, "selected_entry_trigger_per_case": ["T_JBFG_2025_04_25_STAGE2_ACTIONABLE", "T_BNKFG_2025_04_25_STAGE2_ACTIONABLE", "T_IMFG_2025_04_25_STAGE2_ACTIONABLE", "T_IBK_2025_04_25_STAGE2_ACTIONABLE"], "avg_MFE_90D_pct": 53.98, "avg_MAE_90D_pct": -2.71, "avg_MFE_180D_pct": 56.2, "avg_MAE_180D_pct": -2.71, "false_positive_rate": "0/4 for Stage2 representatives; 2 local 4B rows blocked as watch-only", "missed_structural_count": 2, "late_green_count": 2, "avg_green_lateness_ratio": "not_applicable", "avg_four_b_local_peak_proximity": 0.984, "avg_four_b_full_window_peak_proximity": 0.456, "score_return_alignment_verdict": "mixed_but_usable"}
{"row_type": "aggregate", "profile_id": "P0b", "profile_scope": "rollback_reference", "profile_hypothesis": "E2R 2.0 reference; likely overweights low-PBR beta and under-weights actual distribution execution.", "changed_axes": ["c21_regional_bank_capital_return_execution_bonus", "c21_local_4b_watch_only_guard", "c21_state_bank_dividend_route_separation"], "changed_thresholds": [], "eligible_trigger_count": 4, "selected_entry_trigger_per_case": ["T_JBFG_2025_04_25_STAGE2_ACTIONABLE", "T_BNKFG_2025_04_25_STAGE2_ACTIONABLE", "T_IMFG_2025_04_25_STAGE2_ACTIONABLE", "T_IBK_2025_04_25_STAGE2_ACTIONABLE"], "avg_MFE_90D_pct": 53.98, "avg_MAE_90D_pct": -2.71, "avg_MFE_180D_pct": 56.2, "avg_MAE_180D_pct": -2.71, "false_positive_rate": "0/4 for Stage2 representatives; 2 local 4B rows blocked as watch-only", "missed_structural_count": 2, "late_green_count": 2, "avg_green_lateness_ratio": "not_applicable", "avg_four_b_local_peak_proximity": 0.984, "avg_four_b_full_window_peak_proximity": 0.456, "score_return_alignment_verdict": "weak"}
{"row_type": "aggregate", "profile_id": "P1", "profile_scope": "sector_specific_candidate_profile", "profile_hypothesis": "L6 regional-bank profile with capital-return execution bonus and state-bank route separation.", "changed_axes": ["c21_regional_bank_capital_return_execution_bonus", "c21_local_4b_watch_only_guard", "c21_state_bank_dividend_route_separation"], "changed_thresholds": [], "eligible_trigger_count": 4, "selected_entry_trigger_per_case": ["T_JBFG_2025_04_25_STAGE2_ACTIONABLE", "T_BNKFG_2025_04_25_STAGE2_ACTIONABLE", "T_IMFG_2025_04_25_STAGE2_ACTIONABLE", "T_IBK_2025_04_25_STAGE2_ACTIONABLE"], "avg_MFE_90D_pct": 53.98, "avg_MAE_90D_pct": -2.71, "avg_MFE_180D_pct": 56.2, "avg_MAE_180D_pct": -2.71, "false_positive_rate": "0/4 for Stage2 representatives; 2 local 4B rows blocked as watch-only", "missed_structural_count": 0, "late_green_count": 0, "avg_green_lateness_ratio": "not_applicable", "avg_four_b_local_peak_proximity": 0.984, "avg_four_b_full_window_peak_proximity": 0.456, "score_return_alignment_verdict": "improved"}
{"row_type": "aggregate", "profile_id": "P2", "profile_scope": "canonical_archetype_candidate_profile", "profile_hypothesis": "C21-specific ROE/PBR rerating profile with local-4B watch-only guard.", "changed_axes": ["c21_regional_bank_capital_return_execution_bonus", "c21_local_4b_watch_only_guard", "c21_state_bank_dividend_route_separation"], "changed_thresholds": [], "eligible_trigger_count": 4, "selected_entry_trigger_per_case": ["T_JBFG_2025_04_25_STAGE2_ACTIONABLE", "T_BNKFG_2025_04_25_STAGE2_ACTIONABLE", "T_IMFG_2025_04_25_STAGE2_ACTIONABLE", "T_IBK_2025_04_25_STAGE2_ACTIONABLE"], "avg_MFE_90D_pct": 53.98, "avg_MAE_90D_pct": -2.71, "avg_MFE_180D_pct": 56.2, "avg_MAE_180D_pct": -2.71, "false_positive_rate": "0/4 for Stage2 representatives; 2 local 4B rows blocked as watch-only", "missed_structural_count": 0, "late_green_count": 0, "avg_green_lateness_ratio": "not_applicable", "avg_four_b_local_peak_proximity": 0.984, "avg_four_b_full_window_peak_proximity": 0.456, "score_return_alignment_verdict": "best"}
{"row_type": "aggregate", "profile_id": "P3", "profile_scope": "counterexample_guard_profile", "profile_hypothesis": "Guard that prevents July price-only local peaks from becoming full 4B exits without non-price evidence.", "changed_axes": ["c21_regional_bank_capital_return_execution_bonus", "c21_local_4b_watch_only_guard", "c21_state_bank_dividend_route_separation"], "changed_thresholds": [], "eligible_trigger_count": 4, "selected_entry_trigger_per_case": ["T_JBFG_2025_04_25_STAGE2_ACTIONABLE", "T_BNKFG_2025_04_25_STAGE2_ACTIONABLE", "T_IMFG_2025_04_25_STAGE2_ACTIONABLE", "T_IBK_2025_04_25_STAGE2_ACTIONABLE"], "avg_MFE_90D_pct": 53.98, "avg_MAE_90D_pct": -2.71, "avg_MFE_180D_pct": 56.2, "avg_MAE_180D_pct": -2.71, "false_positive_rate": "0/4 for Stage2 representatives; 2 local 4B rows blocked as watch-only", "missed_structural_count": 0, "late_green_count": 0, "avg_green_lateness_ratio": "not_applicable", "avg_four_b_local_peak_proximity": 0.984, "avg_four_b_full_window_peak_proximity": 0.456, "score_return_alignment_verdict": "guard_useful"}
{"row_type": "residual_contribution", "round": "R13", "loop": "23", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "new_independent_case_count": 4, "reused_case_count": 0, "new_symbol_count": 4, "new_trigger_family_count": 3, "tested_existing_calibrated_axes": ["stage2_actionable_evidence_bonus", "stage3_yellow_total_min", "stage3_green_total_min", "stage3_green_revision_min", "price_only_blowoff_blocks_positive_stage", "full_4b_requires_non_price_evidence", "hard_4c_thesis_break_routes_to_4c"], "residual_error_types_found": ["regional_bank_stage2_too_late_when_capital_return_execution_visible", "price_only_local_4b_too_early_vs_full_window_peak", "state_bank_dividend_route_should_not_merge_with_private_buyback_route"], "loop_contribution_label": "canonical_archetype_rule_candidate", "do_not_propose_new_weight_delta": false}
{"row_type": "narrative_only", "case_id": "R13L23_C21_BNKFG_138930_LOCAL_4B_TOO_EARLY", "symbol": "138930", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "reason": "July 2025 local-4B overlay has useful timing evidence but lacks a forward 180D window by stock-web manifest max_date; use for narrative/risk calibration only, not positive weight calibration.", "price_source": "Songdaiki/stock-web", "usage": "not_weight_calibration"}
{"row_type": "narrative_only", "case_id": "R13L23_C21_IMFG_139130_LOCAL_4B_TOO_EARLY", "symbol": "139130", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "reason": "July 2025 local-4B overlay has useful timing evidence but lacks a forward 180D window by stock-web manifest max_date; use for narrative/risk calibration only, not positive weight calibration.", "price_source": "Songdaiki/stock-web", "usage": "not_weight_calibration"}
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
next_round = R13_loop_24_L6_C21_CREDIT_CARD_CAPITAL_RETURN_HOLDOUT
recommended_scope = card/consumer-finance capital return vs credit-cost counterexamples
carry_forward_axes = c21_regional_bank_capital_return_execution_bonus, c21_local_4b_watch_only_guard, c21_state_bank_dividend_route_separation
```

## 28. Source Notes

- `atlas/manifest.json` was read from Songdaiki/stock-web and showed max_date `2026-02-20` and price basis `tradable_raw` / `raw_unadjusted_marcap`.
- Symbol profiles used: `175/175330.json`, `138/138930.json`, `139/139130.json`, `024/024110.json`.
- Price shards used: 2025 and 2026 `atlas/ohlcv_tradable_by_symbol_year` files for the same four symbols.
- This MD is historical calibration research only and should not be interpreted as a trading recommendation.
