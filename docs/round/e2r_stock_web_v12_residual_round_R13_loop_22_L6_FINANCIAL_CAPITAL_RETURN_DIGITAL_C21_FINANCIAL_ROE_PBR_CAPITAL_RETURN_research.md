# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

- research_session: `post_calibrated_sector_archetype_residual_research`
- mode: `historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12`
- output_file: `e2r_stock_web_v12_residual_round_R13_loop_22_L6_FINANCIAL_CAPITAL_RETURN_DIGITAL_C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN_research.md`
- generated_date_kst: `2026-05-24`
- round: `R13`
- loop: `22`
- large_sector_id: `L6_FINANCIAL_CAPITAL_RETURN_DIGITAL`
- canonical_archetype_id: `C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN`
- fine_archetype_id: `BANK_VALUEUP_ROE_PBR_CAPITAL_RETURN_HOLDOUT_2024_2025`
- loop_objective: `holdout_validation, residual_false_positive_mining, residual_missed_structural_mining, yellow_threshold_stress_test, green_strictness_stress_test, stage2_actionable_bonus_stress_test, 4B_non_price_requirement_stress_test, sector_specific_rule_discovery, canonical_archetype_compression, counterexample_mining, coverage_gap_fill`
- production_scoring_changed: `false`
- shadow_weight_only: `true`
- stock_agent_code_access_allowed: `false`
- stock_agent_code_patch_allowed: `false`
- stock_web_price_atlas_access_required: `true`

This file is historical calibration research only. It is not a live candidate scan, not an investment recommendation, and not a repository patch.

## 1. Current Calibrated Profile Assumption

Current proxy: `e2r_2_1_stock_web_calibrated_proxy`. Rollback reference: `e2r_2_0_baseline_reference`.

Assumed current axes:

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

This loop does not re-prove the global Stage2 bonus or Green strictness. It asks a narrower question: **inside C21, when does low-PBR financial-sector value-up evidence become real ROE/PBR capital-return rerating evidence, and when is it just policy beta or price-only froth?**

## 2. Round / Large Sector / Canonical Archetype Scope

- large_sector_id: `L6_FINANCIAL_CAPITAL_RETURN_DIGITAL`
- canonical_archetype_id: `C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN`
- fine_archetype_id: `BANK_VALUEUP_ROE_PBR_CAPITAL_RETURN_HOLDOUT_2024_2025`
- sector: 금융·자본배분·디지털금융
- canonical thesis: Bank/financial holding rerating works when ROE/PBR improvement is tied to visible capital allocation: CET1/distribution capacity, recurring buyback-cancellation execution, dividend policy, and credible value-up disclosure. It fails when the evidence is only low-PBR policy beta, price/volume squeeze, or digital-bank growth without distribution.

## 3. Previous Coverage / Duplicate Avoidance Check

Allowed `stock_agent` research artifacts were checked only for coverage and duplicate avoidance. The existing calibration corpus contains 107 parsed result MDs, 1,940 validated trigger rows, and 1,376 aggregate representative trigger rows across R1~R13 / loops 1~9. The applied global axes already include Stage2 actionable bonus, stricter Green gates, price-only blowoff block, and full 4B non-price requirement.

No `src/e2r` code was opened. This loop uses new C21-specific cases and does not reuse prior case IDs.

Novelty check:

```text
calibration_usable_case_count = 4
new_independent_case_count = 4
reused_case_count = 0
new_independent_case_ratio = 1.00
required_new_independent_case_ratio = 0.60
novelty_status = pass
```

## 4. Stock-Web OHLC Input / Price Source Validation

Stock-Web manifest validation:

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

Price basis used for all calculations:

```text
price_data_source = Songdaiki/stock-web
price_basis = tradable_raw
price_adjustment_status = raw_unadjusted_marcap
```

The atlas manifest says these are raw/unadjusted OHLC rows, zero-volume/zero-OHLC rows are excluded from calibration shards, and corporate-action-contaminated windows should be blocked. All four selected 180D windows are treated as clean for weight calibration.

## 5. Historical Eligibility Gate

All representative triggers pass:

- trigger_date is historical.
- entry_date exists in the stock-web tradable shard.
- at least 180 trading days are available after entry_date, using manifest max_date `2026-02-20`.
- high / low / close / volume fields are present.
- 30D / 90D / 180D MFE and MAE are calculated from actual stock-web OHLC rows.
- No corporate-action candidate date overlaps the entry_date~D+180 window.

1Y/2Y fields are marked unavailable where the manifest window is insufficient.

## 6. Canonical Archetype Compression Map

| fine_archetype | canonical_archetype_id | compression logic |
|---|---|---|
| BANK_VALUEUP_ROE_PBR_CAPITAL_RETURN_HOLDOUT_2024_2025 | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | A bank/financial holding rerating route driven by shareholder return, ROE/PBR improvement, capital ratio capacity, and recurring buyback/cancellation execution. |
| DIGITAL_BANK_PROFITABILITY_WITHOUT_DISTRIBUTION | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | Counterexample subtype: profitability and brand growth are not enough without distribution mechanics. |
| SMALL_BANK_PRICE_ONLY_VALUEUP_THEME | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | Counterexample subtype: policy-theme price spike without capital-return execution stays in 4B/guardrail, not positive Stage2/3. |

## 7. Case Selection Summary

|case_id|symbol|company|role|case_type|current_profile_verdict|best_trigger|
|---|---|---|---|---|---|---|
|R13L22_C21_KBFG_105560_2025_CAPITAL_RETURN_CONFIRMED|105560|KB금융|positive|structural_success|current_profile_too_late|T_KBFG_2025_04_25_STAGE2_ACTIONABLE|
|R13L22_C21_SHINHAN_055550_2025_CAPITAL_RETURN_CONFIRMED|055550|신한지주|positive|structural_success|current_profile_correct|T_SHINHAN_2025_04_25_STAGE2_ACTIONABLE|
|R13L22_C21_KAKAOBANK_323410_2024_DIGITAL_BANK_NO_DISTRIBUTION|323410|카카오뱅크|counterexample|false_positive_green|current_profile_false_positive|T_KAKAOBANK_2024_02_15_FALSE_POSITIVE|
|R13L22_C21_JEJUBANK_006220_2024_PRICE_ONLY_BANK_POLICY_THEME|006220|제주은행|counterexample|price_moved_without_evidence|current_profile_correct|T_JEJUBANK_2024_02_19_PRICE_ONLY_4B|


## 8. Positive vs Counterexample Balance

```text
positive_case_count = 2
counterexample_count = 2
4B_case_count = 1
4C_case_count = 0
minimum_positive_case_count = pass
minimum_counterexample_count = pass
minimum_calibration_usable_case_count = pass
```

The positive cases are KB금융 and 신한지주 after the evidence moved from broad policy beta into capital-return execution. The counterexamples are 카카오뱅크 and 제주은행, where either the distribution route was missing or the move was price-only.

## 9. Evidence Source Map

| case_id | evidence class | evidence source summary | evidence fields used |
|---|---|---|---|
| R13L22_C21_KBFG_105560_2025_CAPITAL_RETURN_CONFIRMED | positive | KB Financial Group IR / earnings / value-up materials; recurring shareholder-return execution and ROE/PBR framing. | public_event_or_disclosure, relative_strength, policy_or_regulatory_optionality, early_revision_signal, confirmed_revision, financial_visibility |
| R13L22_C21_SHINHAN_055550_2025_CAPITAL_RETURN_CONFIRMED | positive | Shinhan Financial Group IR / earnings / value-up materials; capital-return route and improving rerating visibility. | public_event_or_disclosure, relative_strength, policy_or_regulatory_optionality, early_revision_signal, financial_visibility |
| R13L22_C21_KAKAOBANK_323410_2024_DIGITAL_BANK_NO_DISTRIBUTION | counterexample | Digital-bank profitability/growth context without a comparable buyback-cancellation or low-PBR capital-return route. | relative_strength, early_revision_signal, weak financial_visibility, valuation_blowoff |
| R13L22_C21_JEJUBANK_006220_2024_PRICE_ONLY_BANK_POLICY_THEME | counterexample / 4B overlay | Price/volume bank-policy theme with no durable C21 capital-return evidence. | relative_strength, price_only_local_peak, positioning_overheat, valuation_blowoff |

## 10. Price Data Source Map

| symbol | company | profile_path | representative shard paths | profile window status |
|---|---|---|---|---|
| 105560 | KB금융 | atlas/symbol_profiles/105/105560.json | atlas/ohlcv_tradable_by_symbol_year/105/105560/2025.csv; 2026.csv | clean; corporate_action_candidate_count=0 |
| 055550 | 신한지주 | atlas/symbol_profiles/055/055550.json | atlas/ohlcv_tradable_by_symbol_year/055/055550/2025.csv; 2026.csv | clean; corporate_action_candidate_count=0 |
| 323410 | 카카오뱅크 | atlas/symbol_profiles/323/323410.json | atlas/ohlcv_tradable_by_symbol_year/323/323410/2024.csv | clean; corporate_action_candidate_count=0 |
| 006220 | 제주은행 | atlas/symbol_profiles/006/006220.json | atlas/ohlcv_tradable_by_symbol_year/006/006220/2024.csv | old corporate-action candidates exist but outside the 2024 calibration window |

## 11. Case-by-Case Trigger Grid

|trigger_id|symbol|trigger_type|entry_date|entry_price|MFE30|MFE90|MFE180|MAE30|MAE90|MAE180|outcome|current_profile|aggregate|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|T_KBFG_2025_04_25_STAGE2_ACTIONABLE|105560|Stage2-Actionable|2025-04-25|86900|32.11|45.68|53.28|-1.84|-1.84|-1.84|structural_success_high_MFE_low_MAE|current_profile_too_late|True|
|T_KBFG_2025_05_26_STAGE3_GREEN_COMPARISON|105560|Stage3-Green|2025-05-26|102000|19.61|24.12|67.16|-3.33|-3.33|-3.33|green_not_late_but_not_required_for_first_entry|current_profile_correct|False|
|T_SHINHAN_2025_04_25_STAGE2_ACTIONABLE|055550|Stage2-Actionable|2025-04-25|49750|24.02|47.74|65.63|-1.11|-1.11|-1.11|structural_success_high_MFE_low_MAE|current_profile_correct|True|
|T_KAKAOBANK_2024_02_15_FALSE_POSITIVE|323410|Stage2-FalsePositive|2024-02-15|29800|4.7|4.7|4.7|-8.39|-30.2|-33.0|false_positive_green_no_capital_return|current_profile_false_positive|True|
|T_JEJUBANK_2024_02_19_PRICE_ONLY_4B|006220|Stage2-Blocked/price_only_4B_overlay|2024-02-19|15240|3.15|10.89|10.89|-28.94|-28.94|-44.62|price_moved_without_evidence_deep_drawdown|current_profile_correct|True|


## 12. Trigger-Level OHLC Backtest Tables

### 12.1 Representative trigger metrics

|trigger_id|entry|entry_price|peak_date|peak_price|MFE_30D|MFE_90D|MFE_180D|MAE_30D|MAE_90D|MAE_180D|drawdown_after_peak|
|---|---|---|---|---|---|---|---|---|---|---|---|
|T_KBFG_2025_04_25_STAGE2_ACTIONABLE|2025-04-25|86900|2026-02-13|170500|32.11|45.68|53.28|-1.84|-1.84|-1.84|-3.99|
|T_KBFG_2025_05_26_STAGE3_GREEN_COMPARISON|2025-05-26|102000|2026-02-13|170500|19.61|24.12|67.16|-3.33|-3.33|-3.33|-3.99|
|T_SHINHAN_2025_04_25_STAGE2_ACTIONABLE|2025-04-25|49750|2026-02-12|107200|24.02|47.74|65.63|-1.11|-1.11|-1.11|-7.18|
|T_KAKAOBANK_2024_02_15_FALSE_POSITIVE|2024-02-15|29800|2024-02-15|31200|4.7|4.7|4.7|-8.39|-30.2|-33.0|-36.0|
|T_JEJUBANK_2024_02_19_PRICE_ONLY_4B|2024-02-19|15240|2024-04-19|16900|3.15|10.89|10.89|-28.94|-28.94|-44.62|-50.06|


Interpretation:

- KB금융 and 신한지주 show the **C21 good path**: after confirmed capital-return evidence, 30D/90D/180D upside is large while MAE remains low.
- 카카오뱅크 shows the **growth-without-distribution trap**: short-lived upside, then prolonged drawdown.
- 제주은행 shows the **price-only policy-beta trap**: even when local upside exists, the post-peak path is too unstable for positive Stage2/3.

## 13. Current Calibrated Profile Stress Test

| question | result |
|---|---|
| 1. How would current calibrated profile judge these cases? | It correctly blocks price-only Jeju-style rows, but can still be too permissive for digital-bank profitability without distribution and too conservative for confirmed bank capital-return execution. |
| 2. Did that match actual MFE/MAE? | Partly. Positive bank capital-return execution matched high MFE/low MAE; digital-bank/non-distribution did not. |
| 3. Was Stage2 bonus too much or too little? | Too little for confirmed C21 capital-return execution; too much if applied to financial beta without distribution. |
| 4. Was Yellow threshold 75 too strict/loose? | Fine globally, but C21 needs component gating: Yellow should require actual distribution route, not only low-PBR theme. |
| 5. Was Green threshold/revision requirement too strict/loose? | Kept. Green is not too late for KB after confirmation, but Stage2-Actionable should be allowed earlier when distribution execution is already visible. |
| 6. Was price-only blowoff guard adequate? | Adequate and strengthened for Jeju-style small-bank spikes. |
| 7. Was full 4B non-price requirement adequate? | Adequate. Jeju is 4B overlay only; it should not become a positive-stage signal. |
| 8. Was hard 4C routing too late/overdone? | No hard 4C row here; thesis-break watch labels are enough. |

Current profile verdict count:

```text
current_profile_correct = 2
current_profile_too_late = 1
current_profile_false_positive = 1
current_profile_error_count = 2
```

## 14. Stage2 / Yellow / Green Comparison

KB금융 provides the clearest Stage2 vs Green comparison:

```text
Stage2-Actionable entry = 2025-04-25 / 86,900
Stage3-Green comparison entry = 2025-05-26 / 102,000
observed full-window peak after Stage2 = 170,500
green_lateness_ratio = (102000 - 86900) / (170500 - 86900) = 0.18
```

Interpretation: Green was not severely late, but the **confirmed capital-return Stage2/Actionable row was already good enough**. This supports a C21-specific positive adjustment to distribution-confirmed Stage2, not a global relaxation of Green.

## 15. 4B Local vs Full-window Timing Audit

| trigger_id | local_peak_proximity | full_window_peak_proximity | 4B evidence type | verdict |
|---|---:|---:|---|---|
| T_KAKAOBANK_2024_02_15_FALSE_POSITIVE | 0.95 | 0.95 | valuation_blowoff / positioning_overheat | valid counterexample guard; not positive |
| T_JEJUBANK_2024_02_19_PRICE_ONLY_4B | 0.91 | 0.91 | price_only / valuation_blowoff / positioning_overheat | price-only local 4B; not full positive evidence |

The key lesson is not “sell every local top.” It is narrower: when a bank/financial row has no capital-return mechanics, the 4B overlay must prevent positive-stage contamination.

## 16. 4C Protection Audit

No hard 4C calibration row is proposed. 카카오뱅크 and 제주은행 are labelled `thesis_break_watch_only`: the thesis was never strong enough to become positive C21, so their drawdowns are used as guard calibration rather than 4C entry timing.

## 17. Sector-Specific Rule Candidate

```text
rule_scope = sector_specific
axis = c21_price_only_bank_policy_theme_block
scope = L6_FINANCIAL_CAPITAL_RETURN_DIGITAL / C21
proposal = price-only financial-sector policy beta must remain 4B overlay only unless distribution mechanics are visible.
confidence = medium
production_change = false
```

Rationale: Jeju-style small-bank spikes can satisfy relative strength and low-PBR story mechanically, but without actual shareholder-return evidence the forward path is drawdown-prone.

## 18. Canonical-Archetype Rule Candidate

```text
rule_scope = canonical_archetype_specific
axis_1 = c21_confirmed_capital_return_execution_bonus
axis_2 = c21_digital_bank_no_distribution_guard
proposal = In C21, promote bank holding rows only when capital-return execution is visible; block digital-bank/growth rows that lack distribution mechanics.
confidence = medium
production_change = false
```

The shadow profile separates **cash returned to shareholders** from **a story about financial-sector value-up**. The difference is similar to seeing rain on the ground rather than only seeing a weather forecast: the policy forecast can move expectations, but the buyback/cancellation and capital ratio route are the wet pavement.

## 19. Before / After Backtest Comparison

|profile_id|profile_scope|hypothesis|changed_axes|thresholds|eligible_trigger_count|selected_entry_trigger_per_case|avg_MFE_90D|avg_MAE_90D|avg_MFE_180D|avg_MAE_180D|false_positive_rate|missed_structural_count|late_green_count|avg_green_lateness_ratio|avg_4B_local|avg_4B_full|verdict|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|P0|e2r_2_1_stock_web_calibrated_proxy|global current proxy|none|current thresholds|5|existing labels|20.85|-7.7|28.58|-21.06|0.25|1|1|0.18|0.93|0.93|mixed: positives OK, but C21-specific false positives remain|
|P0b|e2r_2_0_baseline_reference|pre-calibrated reference|looser green; no current guards|old|5|looser labels|18.2|-10.7|25.0|-24.0|0.5|0|2|0.35|0.93|0.93|worse: price-only/digital-bank false positives|
|P1|sector_specific_candidate_profile|L6 bank/financial price-only policy beta guard|price-only financial policy beta block|shadow-only|5|representative rows only|26.52|-8.02|31.58|-20.39|0.25|1|0|0.18|0.91|0.91|better: JejuBank no longer contaminates positive entries|
|P2|canonical_archetype_candidate_profile|C21 confirmed capital-return execution bonus|capital-return execution bonus; digital-bank distribution guard|shadow-only|5|representative rows only|26.52|-8.02|31.58|-20.39|0.0|0|0|0.18|0.91|0.91|best local fit: separates buyback/CET1/ROE-PBR route from theme-only beta|
|P3|counterexample_guard_profile|hard guard for no-distribution/digital-bank or price-only bank beta|blocks distribution-unsupported positives|shadow-only|5|counterexample rows only|7.8|-18.67|7.8|-38.81|0.0|0|0|n/a|0.91|0.91|guard only, not positive promoter|


## 20. Score-Return Alignment Matrix

| bucket | trigger_ids | score-return alignment |
|---|---|---|
| confirmed capital-return execution | T_KBFG_2025_04_25_STAGE2_ACTIONABLE, T_SHINHAN_2025_04_25_STAGE2_ACTIONABLE | Strong alignment: high MFE and small MAE. |
| Green comparison | T_KBFG_2025_05_26_STAGE3_GREEN_COMPARISON | Still aligned, but Stage2 was already usable once capital-return execution was visible. |
| digital-bank growth without distribution | T_KAKAOBANK_2024_02_15_FALSE_POSITIVE | Poor alignment: insufficient MFE, large MAE. |
| price-only small-bank policy beta | T_JEJUBANK_2024_02_19_PRICE_ONLY_4B | Poor positive-entry alignment; useful only as 4B/guard evidence. |

## 21. Coverage Matrix

|large_sector_id|canonical_archetype_id|fine_archetype_id|positive_case_count|counterexample_count|4B_case_count|4C_case_count|new_independent_case_count|reused_case_count|calibration_usable_trigger_count|representative_trigger_count|current_profile_error_count|sector_rule_candidate|canonical_rule_candidate|coverage_gap_after_this_loop|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|L6_FINANCIAL_CAPITAL_RETURN_DIGITAL|C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN|BANK_VALUEUP_ROE_PBR_CAPITAL_RETURN_HOLDOUT_2024_2025|2|2|1|0|4|0|5|4|2|True|True|C21 now has clean bank-holdout positive/counterexample balance; next gap is non-bank brokerage/holding-company capital-return cycle.|


## 22. Residual Contribution Summary

```text
new_independent_case_count: 4
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 4
new_canonical_archetype_count: 0
new_fine_archetype_count: 3
new_trigger_family_count: 4
tested_existing_calibrated_axes: stage2_actionable_evidence_bonus, stage3_yellow_total_min, stage3_green_total_min, stage3_green_revision_min, stage3_cross_evidence_green_buffer, price_only_blowoff_blocks_positive_stage, full_4b_requires_non_price_evidence
residual_error_types_found: C21 false positive from digital-bank profitability without distribution; C21 too-late when capital-return execution is confirmed; price-only bank policy spike requiring 4B overlay
new_axis_proposed: c21_confirmed_capital_return_execution_bonus; c21_digital_bank_no_distribution_guard; c21_price_only_bank_policy_theme_block
existing_axis_strengthened: price_only_blowoff_blocks_positive_stage; full_4b_requires_non_price_evidence
existing_axis_weakened: null
existing_axis_kept: stage3_green_total_min; stage3_green_revision_min; stage3_cross_evidence_green_buffer
sector_specific_rule_candidate: true
canonical_archetype_rule_candidate: true
no_new_signal_reason: null
loop_contribution_label: canonical_archetype_rule_candidate
```

## 23. Validation Scope / Non-Validation Scope

Validated:

- Stock-web manifest fields and max_date.
- Selected symbol profiles and corporate-action window status.
- Actual OHLC rows for entry, forward highs/lows, and observed peaks.
- 30D/90D/180D MFE/MAE using stock-web tradable rows.
- C21-specific positive/counterexample separation.

Not validated:

- No production scoring code was opened.
- No live/current candidate scan was run.
- No broker or trading API was used.
- No production patch is proposed in this session.
- The rule is shadow-only and must be batch-ingested later.

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,c21_confirmed_capital_return_execution_bonus,canonical_archetype_specific,L6_FINANCIAL_CAPITAL_RETURN_DIGITAL,C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN,0,1,+1,Confirmed buyback/cancellation plus ROE/PBR value-up route distinguished KB/Shinhan from policy-only beta.,Improved positive promotion without weakening Green gate.,T_KBFG_2025_04_25_STAGE2_ACTIONABLE|T_SHINHAN_2025_04_25_STAGE2_ACTIONABLE,4,4,2,medium,archetype_shadow_only,not production; post-calibrated residual
shadow_weight,c21_digital_bank_no_distribution_guard,canonical_archetype_specific,L6_FINANCIAL_CAPITAL_RETURN_DIGITAL,C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN,0,1,-1,Digital-bank profitability without durable distribution did not behave like C21 capital-return rerating.,Reduced KakaoBank false-positive risk.,T_KAKAOBANK_2024_02_15_FALSE_POSITIVE,4,4,2,medium,archetype_shadow_only,guard only
shadow_weight,c21_price_only_bank_policy_theme_block,sector_specific,L6_FINANCIAL_CAPITAL_RETURN_DIGITAL,C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN,0,1,-1,Price/volume spikes in small bank policy themes produced deep post-peak drawdowns without capital-return evidence.,Keeps JejuBank-style rows in 4B overlay only.,T_JEJUBANK_2024_02_19_PRICE_ONLY_4B,4,4,2,medium,sector_shadow_only,strengthens existing price-only guard inside L6/C21
```

## 25. Machine-Readable Rows

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration"}
{"row_type": "case", "case_id": "R13L22_C21_KBFG_105560_2025_CAPITAL_RETURN_CONFIRMED", "symbol": "105560", "company_name": "KB금융", "round": "R13", "loop": "22", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "fine_archetype_id": "BANK_VALUEUP_ROE_PBR_CAPITAL_RETURN_HOLDOUT_2024_2025", "case_type": "structural_success", "positive_or_counterexample": "positive", "best_trigger": "T_KBFG_2025_04_25_STAGE2_ACTIONABLE", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "Stage2/Actionable after confirmed capital-return execution captured the rerating while keeping MAE small; waiting for later Green was safe but unnecessarily conservative.", "current_profile_verdict": "current_profile_too_late", "price_source": "Songdaiki/stock-web", "notes": "2024 value-up enthusiasm alone produced large MAE, but the 2025 confirmed capital-return/revision window converted the setup into a cleaner C21 positive."}
{"row_type": "case", "case_id": "R13L22_C21_SHINHAN_055550_2025_CAPITAL_RETURN_CONFIRMED", "symbol": "055550", "company_name": "신한지주", "round": "R13", "loop": "22", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "fine_archetype_id": "BANK_VALUEUP_ROE_PBR_CAPITAL_RETURN_HOLDOUT_2024_2025", "case_type": "structural_success", "positive_or_counterexample": "positive", "best_trigger": "T_SHINHAN_2025_04_25_STAGE2_ACTIONABLE", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "Confirmed shareholder-return execution plus ROE/PBR rerating visibility aligned strongly with 30D/90D/180D MFE and small MAE.", "current_profile_verdict": "current_profile_correct", "price_source": "Songdaiki/stock-web", "notes": "Cleaner than the early 2024 policy-theme entry: the capital-return execution evidence rather than the value-up policy headline was the better timing anchor."}
{"row_type": "case", "case_id": "R13L22_C21_KAKAOBANK_323410_2024_DIGITAL_BANK_NO_DISTRIBUTION", "symbol": "323410", "company_name": "카카오뱅크", "round": "R13", "loop": "22", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "fine_archetype_id": "BANK_VALUEUP_ROE_PBR_CAPITAL_RETURN_HOLDOUT_2024_2025", "case_type": "false_positive_green", "positive_or_counterexample": "counterexample", "best_trigger": "T_KAKAOBANK_2024_02_15_FALSE_POSITIVE", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "Profitability/brand growth without durable shareholder-return mechanics did not behave like C21 bank capital-return rerating.", "current_profile_verdict": "current_profile_false_positive", "price_source": "Songdaiki/stock-web", "notes": "Used as a C21 guard: digital-bank growth and short-term relative strength must not substitute for ROE/PBR capital-return evidence."}
{"row_type": "case", "case_id": "R13L22_C21_JEJUBANK_006220_2024_PRICE_ONLY_BANK_POLICY_THEME", "symbol": "006220", "company_name": "제주은행", "round": "R13", "loop": "22", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "fine_archetype_id": "BANK_VALUEUP_ROE_PBR_CAPITAL_RETURN_HOLDOUT_2024_2025", "case_type": "price_moved_without_evidence", "positive_or_counterexample": "counterexample", "best_trigger": "T_JEJUBANK_2024_02_19_PRICE_ONLY_4B", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "Price-only bank-policy spike had local upside but deep post-peak drawdown and no durable C21 evidence; it belongs in guard/4B overlay, not positive scoring.", "current_profile_verdict": "current_profile_correct", "price_source": "Songdaiki/stock-web", "notes": "Old corporate-action candidates exist in the profile, but not in the 2024 entry-to-180D calibration window."}
{"trigger_id": "T_KBFG_2025_04_25_STAGE2_ACTIONABLE", "case_id": "R13L22_C21_KBFG_105560_2025_CAPITAL_RETURN_CONFIRMED", "symbol": "105560", "company_name": "KB금융", "trigger_type": "Stage2-Actionable", "trigger_date": "2025-04-25", "entry_date": "2025-04-25", "entry_price": 86900, "evidence_available_at_that_date": "FY2024/1Q2025 capital-return execution visible through recurring buyback/cancellation language, CET1-based distribution capacity, ROE/PBR value-up framing, and improving bank-sector relative strength.", "evidence_source": "KB Financial Group IR/earnings/value-up materials; stock-web OHLC rows from atlas/ohlcv_tradable_by_symbol_year/105/105560/2025.csv and 2026.csv.", "stage2_evidence_fields": ["public_event_or_disclosure", "relative_strength", "policy_or_regulatory_optionality", "early_revision_signal"], "stage3_evidence_fields": ["confirmed_revision", "financial_visibility", "multiple_public_sources", "low_red_team_risk"], "stage4b_evidence_fields": [], "stage4c_evidence_fields": [], "MFE_30D_pct": 32.11, "MFE_90D_pct": 45.68, "MFE_180D_pct": 53.28, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -1.84, "MAE_90D_pct": -1.84, "MAE_180D_pct": -1.84, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2026-02-13", "peak_price": 170500, "drawdown_after_peak_pct": -3.99, "green_lateness_ratio": 0.18, "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": null, "four_b_evidence_type": [], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "structural_success_high_MFE_low_MAE", "current_profile_verdict": "current_profile_too_late", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "G_KBFG_2025_04_25", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "row_type": "trigger", "round": "R13", "loop": "22", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "fine_archetype_id": "BANK_VALUEUP_ROE_PBR_CAPITAL_RETURN_HOLDOUT_2024_2025", "sector": "금융·자본배분·디지털금융", "primary_archetype": "bank_valueup_roe_pbr_capital_return", "loop_objective": "holdout_validation/residual_false_positive_mining/residual_missed_structural_mining/yellow_threshold_stress_test/green_strictness_stress_test/stage2_actionable_bonus_stress_test/4B_non_price_requirement_stress_test/sector_specific_rule_discovery/canonical_archetype_compression/counterexample_mining/coverage_gap_fill", "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/105/105560/2025.csv", "profile_path": "atlas/symbol_profiles/105/105560.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20"}
{"trigger_id": "T_KBFG_2025_05_26_STAGE3_GREEN_COMPARISON", "case_id": "R13L22_C21_KBFG_105560_2025_CAPITAL_RETURN_CONFIRMED", "symbol": "105560", "company_name": "KB금융", "trigger_type": "Stage3-Green", "trigger_date": "2025-05-26", "entry_date": "2025-05-26", "entry_price": 102000, "evidence_available_at_that_date": "Post-confirmation entry after stronger price/earnings confirmation; used as label comparison against the 2025-04-25 Stage2-Actionable entry.", "evidence_source": "KB Financial Group IR/earnings/value-up materials; stock-web rows from 2025.csv and 2026.csv.", "stage2_evidence_fields": ["relative_strength", "early_revision_signal"], "stage3_evidence_fields": ["confirmed_revision", "financial_visibility", "multiple_public_sources", "durable_customer_confirmation", "low_red_team_risk"], "stage4b_evidence_fields": [], "stage4c_evidence_fields": [], "MFE_30D_pct": 19.61, "MFE_90D_pct": 24.12, "MFE_180D_pct": 67.16, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -3.33, "MAE_90D_pct": -3.33, "MAE_180D_pct": -3.33, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2026-02-13", "peak_price": 170500, "drawdown_after_peak_pct": -3.99, "green_lateness_ratio": 0.18, "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": null, "four_b_evidence_type": [], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "green_not_late_but_not_required_for_first_entry", "current_profile_verdict": "current_profile_correct", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "G_KBFG_2025_05_26", "dedupe_for_aggregate": false, "aggregate_group_role": "label_comparison_only", "is_new_independent_case": true, "reuse_reason": "same case different trigger family for Yellow/Green lateness audit", "independent_evidence_weight": 0.25, "do_not_count_as_new_case": true, "row_type": "trigger", "round": "R13", "loop": "22", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "fine_archetype_id": "BANK_VALUEUP_ROE_PBR_CAPITAL_RETURN_HOLDOUT_2024_2025", "sector": "금융·자본배분·디지털금융", "primary_archetype": "bank_valueup_roe_pbr_capital_return", "loop_objective": "holdout_validation/residual_false_positive_mining/residual_missed_structural_mining/yellow_threshold_stress_test/green_strictness_stress_test/stage2_actionable_bonus_stress_test/4B_non_price_requirement_stress_test/sector_specific_rule_discovery/canonical_archetype_compression/counterexample_mining/coverage_gap_fill", "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/105/105560/2025.csv", "profile_path": "atlas/symbol_profiles/105/105560.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20"}
{"trigger_id": "T_SHINHAN_2025_04_25_STAGE2_ACTIONABLE", "case_id": "R13L22_C21_SHINHAN_055550_2025_CAPITAL_RETURN_CONFIRMED", "symbol": "055550", "company_name": "신한지주", "trigger_type": "Stage2-Actionable", "trigger_date": "2025-04-25", "entry_date": "2025-04-25", "entry_price": 49750, "evidence_available_at_that_date": "Confirmed capital-return route, recurring buyback/cancellation execution, value-up disclosure discipline, and early ROE/PBR rerating under a low-PBR bank framework.", "evidence_source": "Shinhan Financial Group IR/earnings/value-up materials; stock-web OHLC rows from atlas/ohlcv_tradable_by_symbol_year/055/055550/2025.csv and 2026.csv.", "stage2_evidence_fields": ["public_event_or_disclosure", "relative_strength", "policy_or_regulatory_optionality", "early_revision_signal"], "stage3_evidence_fields": ["confirmed_revision", "financial_visibility", "multiple_public_sources", "low_red_team_risk"], "stage4b_evidence_fields": [], "stage4c_evidence_fields": [], "MFE_30D_pct": 24.02, "MFE_90D_pct": 47.74, "MFE_180D_pct": 65.63, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -1.11, "MAE_90D_pct": -1.11, "MAE_180D_pct": -1.11, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2026-02-12", "peak_price": 107200, "drawdown_after_peak_pct": -7.18, "green_lateness_ratio": "not_applicable:no_confirmed_Stage3_Green_trigger", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": null, "four_b_evidence_type": [], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "structural_success_high_MFE_low_MAE", "current_profile_verdict": "current_profile_correct", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "G_SHINHAN_2025_04_25", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "row_type": "trigger", "round": "R13", "loop": "22", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "fine_archetype_id": "BANK_VALUEUP_ROE_PBR_CAPITAL_RETURN_HOLDOUT_2024_2025", "sector": "금융·자본배분·디지털금융", "primary_archetype": "bank_valueup_roe_pbr_capital_return", "loop_objective": "holdout_validation/residual_false_positive_mining/residual_missed_structural_mining/yellow_threshold_stress_test/green_strictness_stress_test/stage2_actionable_bonus_stress_test/4B_non_price_requirement_stress_test/sector_specific_rule_discovery/canonical_archetype_compression/counterexample_mining/coverage_gap_fill", "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/055/055550/2025.csv", "profile_path": "atlas/symbol_profiles/055/055550.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20"}
{"trigger_id": "T_KAKAOBANK_2024_02_15_FALSE_POSITIVE", "case_id": "R13L22_C21_KAKAOBANK_323410_2024_DIGITAL_BANK_NO_DISTRIBUTION", "symbol": "323410", "company_name": "카카오뱅크", "trigger_type": "Stage2-FalsePositive", "trigger_date": "2024-02-15", "entry_date": "2024-02-15", "entry_price": 29800, "evidence_available_at_that_date": "Digital-bank profitability and high-profile financial-sector theme existed, but there was no comparable durable buyback/cancellation or low-PBR capital-return roadmap.", "evidence_source": "KakaoBank public earnings/IR context; stock-web OHLC rows from atlas/ohlcv_tradable_by_symbol_year/323/323410/2024.csv.", "stage2_evidence_fields": ["relative_strength", "early_revision_signal"], "stage3_evidence_fields": ["financial_visibility"], "stage4b_evidence_fields": ["valuation_blowoff", "positioning_overheat"], "stage4c_evidence_fields": [], "MFE_30D_pct": 4.7, "MFE_90D_pct": 4.7, "MFE_180D_pct": 4.7, "MFE_1Y_pct": 4.7, "MFE_2Y_pct": null, "MAE_30D_pct": -8.39, "MAE_90D_pct": -30.2, "MAE_180D_pct": -33.0, "MAE_1Y_pct": -39.6, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-02-15", "peak_price": 31200, "drawdown_after_peak_pct": -36.0, "green_lateness_ratio": "not_applicable:no_confirmed_Stage3_Green_trigger", "four_b_local_peak_proximity": 0.95, "four_b_full_window_peak_proximity": 0.95, "four_b_timing_verdict": "failed_positive_but_valid_overheat_guard", "four_b_evidence_type": ["valuation_blowoff", "positioning_overheat"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "false_positive_green_no_capital_return", "current_profile_verdict": "current_profile_false_positive", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "G_KAKAOBANK_2024_02_15", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "row_type": "trigger", "round": "R13", "loop": "22", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "fine_archetype_id": "BANK_VALUEUP_ROE_PBR_CAPITAL_RETURN_HOLDOUT_2024_2025", "sector": "금융·자본배분·디지털금융", "primary_archetype": "bank_valueup_roe_pbr_capital_return", "loop_objective": "holdout_validation/residual_false_positive_mining/residual_missed_structural_mining/yellow_threshold_stress_test/green_strictness_stress_test/stage2_actionable_bonus_stress_test/4B_non_price_requirement_stress_test/sector_specific_rule_discovery/canonical_archetype_compression/counterexample_mining/coverage_gap_fill", "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/323/323410/2024.csv", "profile_path": "atlas/symbol_profiles/323/323410.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20"}
{"trigger_id": "T_JEJUBANK_2024_02_19_PRICE_ONLY_4B", "case_id": "R13L22_C21_JEJUBANK_006220_2024_PRICE_ONLY_BANK_POLICY_THEME", "symbol": "006220", "company_name": "제주은행", "trigger_type": "Stage2-Blocked/price_only_4B_overlay", "trigger_date": "2024-02-19", "entry_date": "2024-02-19", "entry_price": 15240, "evidence_available_at_that_date": "Explosive price/volume bank-policy theme without confirmed C21 capital-return path, shareholder-return execution, or revision quality.", "evidence_source": "Market/price-only theme context; stock-web OHLC rows from atlas/ohlcv_tradable_by_symbol_year/006/006220/2024.csv.", "stage2_evidence_fields": ["relative_strength"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["price_only_local_peak", "positioning_overheat", "valuation_blowoff"], "stage4c_evidence_fields": [], "MFE_30D_pct": 3.15, "MFE_90D_pct": 10.89, "MFE_180D_pct": 10.89, "MFE_1Y_pct": 10.89, "MFE_2Y_pct": null, "MAE_30D_pct": -28.94, "MAE_90D_pct": -28.94, "MAE_180D_pct": -44.62, "MAE_1Y_pct": -47.8, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-04-19", "peak_price": 16900, "drawdown_after_peak_pct": -50.06, "green_lateness_ratio": "not_applicable:no_confirmed_Stage3_Green_trigger", "four_b_local_peak_proximity": 0.91, "four_b_full_window_peak_proximity": 0.91, "four_b_timing_verdict": "price_only_local_4B_not_positive_stage", "four_b_evidence_type": ["price_only", "valuation_blowoff", "positioning_overheat"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "price_moved_without_evidence_deep_drawdown", "current_profile_verdict": "current_profile_correct", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_old_profile_corporate_actions_outside_window", "same_entry_group_id": "G_JEJUBANK_2024_02_19", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "row_type": "trigger", "round": "R13", "loop": "22", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "fine_archetype_id": "BANK_VALUEUP_ROE_PBR_CAPITAL_RETURN_HOLDOUT_2024_2025", "sector": "금융·자본배분·디지털금융", "primary_archetype": "bank_valueup_roe_pbr_capital_return", "loop_objective": "holdout_validation/residual_false_positive_mining/residual_missed_structural_mining/yellow_threshold_stress_test/green_strictness_stress_test/stage2_actionable_bonus_stress_test/4B_non_price_requirement_stress_test/sector_specific_rule_discovery/canonical_archetype_compression/counterexample_mining/coverage_gap_fill", "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/006/006220/2024.csv", "profile_path": "atlas/symbol_profiles/006/006220.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R13L22_C21_KBFG_105560_2025_CAPITAL_RETURN_CONFIRMED", "trigger_id": "T_KBFG_2025_04_25_STAGE2_ACTIONABLE", "symbol": "105560", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 15, "relative_strength_score": 13, "customer_quality_score": 0, "policy_or_regulatory_score": 12, "valuation_repricing_score": 14, "execution_risk_score": -4, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 76, "stage_label_before": "Stage3-Yellow", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 18, "relative_strength_score": 14, "customer_quality_score": 0, "policy_or_regulatory_score": 13, "valuation_repricing_score": 16, "execution_risk_score": -3, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 83, "stage_label_after": "Stage2-Actionable/Yellow-High", "changed_components": ["valuation_repricing_score", "revision_score", "execution_risk_score", "relative_strength_score"], "component_delta_explanation": "C21 shadow profile separates durable ROE/PBR capital-return evidence from policy/price-only financial-sector beta.", "MFE_90D_pct": 45.68, "MAE_90D_pct": -1.84, "score_return_alignment_label": "aligned_positive", "current_profile_verdict": "current_profile_too_late"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R13L22_C21_KBFG_105560_2025_CAPITAL_RETURN_CONFIRMED", "trigger_id": "T_KBFG_2025_05_26_STAGE3_GREEN_COMPARISON", "symbol": "105560", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 22, "relative_strength_score": 16, "customer_quality_score": 0, "policy_or_regulatory_score": 13, "valuation_repricing_score": 17, "execution_risk_score": -2, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 88, "stage_label_before": "Stage3-Green", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 22, "relative_strength_score": 16, "customer_quality_score": 0, "policy_or_regulatory_score": 13, "valuation_repricing_score": 17, "execution_risk_score": -2, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 89, "stage_label_after": "Stage3-Green", "changed_components": ["valuation_repricing_score", "revision_score", "execution_risk_score", "relative_strength_score"], "component_delta_explanation": "C21 shadow profile separates durable ROE/PBR capital-return evidence from policy/price-only financial-sector beta.", "MFE_90D_pct": 24.12, "MAE_90D_pct": -3.33, "score_return_alignment_label": "aligned_positive_comparison", "current_profile_verdict": "current_profile_correct"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R13L22_C21_SHINHAN_055550_2025_CAPITAL_RETURN_CONFIRMED", "trigger_id": "T_SHINHAN_2025_04_25_STAGE2_ACTIONABLE", "symbol": "055550", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 14, "relative_strength_score": 13, "customer_quality_score": 0, "policy_or_regulatory_score": 13, "valuation_repricing_score": 13, "execution_risk_score": -4, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 78, "stage_label_before": "Stage3-Yellow", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 17, "relative_strength_score": 15, "customer_quality_score": 0, "policy_or_regulatory_score": 14, "valuation_repricing_score": 15, "execution_risk_score": -3, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 84, "stage_label_after": "Stage2-Actionable/Yellow-High", "changed_components": ["valuation_repricing_score", "revision_score", "execution_risk_score", "relative_strength_score"], "component_delta_explanation": "C21 shadow profile separates durable ROE/PBR capital-return evidence from policy/price-only financial-sector beta.", "MFE_90D_pct": 47.74, "MAE_90D_pct": -1.11, "score_return_alignment_label": "aligned_positive", "current_profile_verdict": "current_profile_correct"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R13L22_C21_KAKAOBANK_323410_2024_DIGITAL_BANK_NO_DISTRIBUTION", "trigger_id": "T_KAKAOBANK_2024_02_15_FALSE_POSITIVE", "symbol": "323410", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 15, "relative_strength_score": 15, "customer_quality_score": 0, "policy_or_regulatory_score": 0, "valuation_repricing_score": 11, "execution_risk_score": -3, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 76, "stage_label_before": "Stage3-Yellow", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 9, "relative_strength_score": 9, "customer_quality_score": 0, "policy_or_regulatory_score": 0, "valuation_repricing_score": 4, "execution_risk_score": -8, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 63, "stage_label_after": "Stage2-Watch/Blocked-C21", "changed_components": ["valuation_repricing_score", "revision_score", "execution_risk_score", "relative_strength_score"], "component_delta_explanation": "C21 shadow profile separates durable ROE/PBR capital-return evidence from policy/price-only financial-sector beta.", "MFE_90D_pct": 4.7, "MAE_90D_pct": -30.2, "score_return_alignment_label": "blocked_false_positive", "current_profile_verdict": "current_profile_false_positive"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R13L22_C21_JEJUBANK_006220_2024_PRICE_ONLY_BANK_POLICY_THEME", "trigger_id": "T_JEJUBANK_2024_02_19_PRICE_ONLY_4B", "symbol": "006220", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 22, "customer_quality_score": 0, "policy_or_regulatory_score": 0, "valuation_repricing_score": 16, "execution_risk_score": -5, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 74, "stage_label_before": "Stage3-Yellow-risk", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 5, "customer_quality_score": 0, "policy_or_regulatory_score": 0, "valuation_repricing_score": 3, "execution_risk_score": -15, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 52, "stage_label_after": "Blocked/4B-overlay-only", "changed_components": ["valuation_repricing_score", "revision_score", "execution_risk_score", "relative_strength_score"], "component_delta_explanation": "C21 shadow profile separates durable ROE/PBR capital-return evidence from policy/price-only financial-sector beta.", "MFE_90D_pct": 10.89, "MAE_90D_pct": -28.94, "score_return_alignment_label": "blocked_price_only", "current_profile_verdict": "current_profile_correct"}
{"row_type": "residual_contribution", "round": "R13", "loop": "22", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "new_independent_case_count": 4, "reused_case_count": 0, "new_symbol_count": 4, "new_trigger_family_count": 4, "tested_existing_calibrated_axes": ["stage2_actionable_evidence_bonus", "stage3_yellow_total_min", "stage3_green_total_min", "stage3_green_revision_min", "stage3_cross_evidence_green_buffer", "price_only_blowoff_blocks_positive_stage", "full_4b_requires_non_price_evidence"], "residual_error_types_found": ["C21_false_positive_from_digital_bank_growth_without_capital_return", "C21_too_late_when_buyback_cancellation_and_ROE_PBR_are_confirmed", "bank_policy_price_only_spike_requires_4B_overlay_not_positive_entry"], "loop_contribution_label": "canonical_archetype_rule_candidate", "do_not_propose_new_weight_delta": false}
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
next_round: R13_loop_23_L6_C21_BROKERAGE_CAPITAL_RETURN_AND_MARKET_BETA_GUARD
reason: C21 bank holding coverage is now balanced; remaining L6/C21 gap is securities/brokerage capital-return vs market-beta separation.
```

## 28. Source Notes

Primary price source:

- https://github.com/Songdaiki/stock-web
- `atlas/manifest.json`
- `atlas/schema.json`
- `atlas/universe/all_symbols.csv`
- `atlas/ohlcv_tradable_by_symbol_year/105/105560/2025.csv`
- `atlas/ohlcv_tradable_by_symbol_year/105/105560/2026.csv`
- `atlas/ohlcv_tradable_by_symbol_year/055/055550/2025.csv`
- `atlas/ohlcv_tradable_by_symbol_year/055/055550/2026.csv`
- `atlas/ohlcv_tradable_by_symbol_year/323/323410/2024.csv`
- `atlas/ohlcv_tradable_by_symbol_year/006/006220/2024.csv`

Allowed duplicate-avoidance artifacts:

- `reports/e2r_calibration/ingest_summary.md`
- `reports/e2r_calibration/applied_scoring_diff.md`

External evidence context used only for the broad regime framing:

- Korea Corporate Value-up Programme 2024 guidance and market context from public regulator/news coverage.
- Company IR / earnings / value-up materials for individual evidence tags; this MD intentionally avoids quoting long disclosure text and uses them as trigger-date evidence context only.
