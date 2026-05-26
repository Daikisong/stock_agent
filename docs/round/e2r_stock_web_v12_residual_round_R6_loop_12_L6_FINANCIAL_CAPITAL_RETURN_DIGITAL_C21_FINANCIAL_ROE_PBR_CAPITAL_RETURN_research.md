# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
research_session = post_calibrated_sector_archetype_residual_research
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
round = R6
loop = 12
large_sector_id = L6_FINANCIAL_CAPITAL_RETURN_DIGITAL
canonical_archetype_id = C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN
fine_archetype_id = BANK_VALUEUP_CAPITAL_RETURN_EXECUTION_VS_POLICY_BETA_GUARD
output_file = e2r_stock_web_v12_residual_round_R6_loop_12_L6_FINANCIAL_CAPITAL_RETURN_DIGITAL_C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN_research.md
production_scoring_changed = false
shadow_weight_only = true
stock_agent_code_access_allowed = false
stock_agent_code_patch_allowed = false
stock_web_price_atlas_access_required = true
```

This file is historical calibration research only. It is not a current stock screen, not a recommendation list, and not a repository patch. The purpose is to add residual coverage for a sector/canonical archetype that was less represented than the earlier R1/R2 industrial, grid, AI, HBM, and equipment loops.

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

The tested question is not whether Stage2 can be earlier than Green. That global result is already assumed. The residual question here is narrower: in Korean financials, does the broad Corporate Value-up policy beta deserve the same score as executed capital-return evidence? The answer from this loop is no. C21 needs a gate that separates bank-level payout/buyback/cancellation/ROE execution from policy-only or price-only low-PBR excitement.

## 2. Round / Large Sector / Canonical Archetype Scope

```text
round = R6
loop = 12
large_sector_id = L6_FINANCIAL_CAPITAL_RETURN_DIGITAL
canonical_archetype_id = C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN
fine_archetype_id = BANK_VALUEUP_CAPITAL_RETURN_EXECUTION_VS_POLICY_BETA_GUARD

loop_objective:
- sector_specific_rule_discovery
- canonical_archetype_compression
- counterexample_mining
- 4B_non_price_requirement_stress_test
- green_strictness_stress_test
```

The canonical compression is:

```text
BANK_VALUEUP_CAPITAL_RETURN_EXECUTION -> C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN
DIGITAL_BANK_PREMIUM_GUARD -> C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN
MICRO_BANK_PRICE_ONLY_VALUEUP_BETA_GUARD -> C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN
```

## 3. Previous Coverage / Duplicate Avoidance Check

`stock_agent` source code was not opened. Earlier conversation state and the immediately preceding MD output indicate the last generated file covered `R5 / L5 / C18_CONSUMER_EXPORT_CHANNEL_REORDER`. This loop therefore avoids that consumer-export C18 surface and also avoids repeating the R1/R2 power-grid/HBM representative sets.

```text
auto_selected_coverage_gap = R6/L6 C21 financial capital-return residual
same_archetype_new_symbol_count = 4
same_archetype_new_trigger_family_count = 4
new_independent_case_count = 4
reused_case_count = 0
duplicate_low_value_loop = false
```

## 4. Stock-Web OHLC Input / Price Source Validation

The price atlas manifest used here reports:

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

All representative triggers use `tradable_raw` rows from `atlas/ohlcv_tradable_by_symbol_year`. Raw/unadjusted status matters: this is not split-adjusted chart data. Corporate-action contaminated 180D windows are blocked by default. In this loop, the 2024 windows used for calibration are treated as clean for 180D calibration. 제주은행 has historical corporate-action candidates in older years, but not in the 2024 180D window used here.

## 5. Historical Eligibility Gate

| Case | Entry in tradable shard | 180D forward window | 30/90/180 MFE/MAE | 2024 180D corporate-action contamination | Calibration usable |
|---|---:|---:|---:|---:|---:|
| KB금융 105560 | true | true | true | false | true |
| 신한지주 055550 | true | true | true | false | true |
| 카카오뱅크 323410 | true | true | true | false | true |
| 제주은행 006220 | true | true | true | false for tested 2024 window | true |

## 6. Canonical Archetype Compression Map

C21 is not simply "financial stock went up after Value-up." It is a mechanism:

```text
public capital-return plan
  -> credible ROE/PBR improvement path
  -> market believes payout / cancellation / dividend discipline is repeatable
  -> valuation discount narrows
```

The counter-mechanism is also important:

```text
broad Value-up policy beta or small-cap squeeze
  -> price moves before execution evidence
  -> no durable payout / ROE / capital discipline bridge
  -> high MAE or failed rerating
```

That split is the main residual contribution.

## 7. Case Selection Summary

| case_id | symbol | company | role | pos/counter | trigger_date | entry_price | MFE_180D | MAE_180D | current_profile |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| R6L12_C21_KBFIN_20240208_CAPITAL_RETURN | 105560 | KB금융 | structural_success | positive | 2024-02-08 | 67600 | 53.7 | -11.69 | current_profile_correct |
| R6L12_C21_SHINHAN_20240208_CAPITAL_RETURN | 055550 | 신한지주 | structural_success | positive | 2024-02-08 | 44150 | 46.32 | -9.74 | current_profile_correct |
| R6L12_C21_KAKAOBANK_20240227_POLICY_BETA_FAIL | 323410 | 카카오뱅크 | failed_rerating | counterexample | 2024-02-26 | 29550 | 3.72 | -37.43 | current_profile_false_positive |
| R6L12_C21_JEJUBANK_20240202_PRICE_ONLY_BLOWOFF | 006220 | 제주은행 | price_moved_without_evidence | counterexample | 2024-02-02 | 13620 | 24.08 | -41.26 | current_profile_correct |


## 8. Positive vs Counterexample Balance

```text
positive_case_count = 2
counterexample_count = 2
4B_case_count = 1
4C_case_count = 0
calibration_usable_case_count = 4
new_independent_case_ratio = 1.00
```

The positive pair, KB금융 and 신한지주, shares the key C21 mechanism: capital-return execution was visible enough to connect policy optionality with financial behavior. The counterexample pair, 카카오뱅크 and 제주은행, shows the inverse: policy beta or price squeeze without capital-return execution created either failed rerating or high-MAE blowoff.

## 9. Evidence Source Map

| Evidence family | Positive cases | Counterexamples | Calibration implication |
|---|---|---|---|
| Corporate Value-up policy context | KB금융, 신한지주 | 카카오뱅크, 제주은행 | Policy is common background, not sufficient by itself |
| Explicit capital-return execution | KB금융, 신한지주 | weak/absent | Required for C21 Stage2-Actionable promotion |
| Low-PBR rerating asymmetry | KB금융, 신한지주 | not the same in premium digital bank | Needs ROE/PBR context, not broad financial label |
| Price-only relative strength | partial | 제주은행 | Must route to 4B/watch, not Stage2/3 |
| Digital-bank premium risk | no | 카카오뱅크 | Needs separate guard |

## 10. Price Data Source Map

| Symbol | Company | Tradable shard | Profile |
|---|---|---|---|
| 105560 | KB금융 | atlas/ohlcv_tradable_by_symbol_year/105/105560/2024.csv; 2025.csv; 2026.csv | atlas/symbol_profiles/105/105560.json |
| 055550 | 신한지주 | atlas/ohlcv_tradable_by_symbol_year/055/055550/2024.csv; 2026.csv | atlas/symbol_profiles/055/055550.json |
| 323410 | 카카오뱅크 | atlas/ohlcv_tradable_by_symbol_year/323/323410/2024.csv | atlas/symbol_profiles/323/323410.json |
| 006220 | 제주은행 | atlas/ohlcv_tradable_by_symbol_year/006/006220/2024.csv | atlas/symbol_profiles/006/006220.json |

## 11. Case-by-Case Trigger Grid

| trigger_id | symbol | company | trigger_type | trigger_date | entry_date | entry_price | MFE_90D | MAE_90D | MFE_180D | MAE_180D | current_profile | aggregate_role |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| R6L12_C21_KBFIN_20240208_CAPITAL_RETURN_T1 | 105560 | KB금융 | Stage2-Actionable | 2024-02-08 | 2024-02-08 | 67600 | 23.37 | -11.69 | 53.7 | -11.69 | current_profile_correct | representative |
| R6L12_C21_SHINHAN_20240208_CAPITAL_RETURN_T1 | 055550 | 신한지주 | Stage2-Actionable | 2024-02-08 | 2024-02-08 | 44150 | 16.65 | -9.74 | 46.32 | -9.74 | current_profile_correct | representative |
| R6L12_C21_KAKAOBANK_20240227_POLICY_BETA_FAIL_T1 | 323410 | 카카오뱅크 | Stage2-Policy-Beta | 2024-02-26 | 2024-02-27 | 29550 | 3.72 | -32.15 | 3.72 | -37.43 | current_profile_false_positive | representative |
| R6L12_C21_JEJUBANK_20240202_PRICE_ONLY_BLOWOFF_T1 | 006220 | 제주은행 | Stage4B-Overlay | 2024-02-02 | 2024-02-02 | 13620 | 24.08 | -19.46 | 24.08 | -41.26 | current_profile_correct | representative |
| R6L12_C21_JEJUBANK_20240219_LOCAL_4B_T2 | 006220 | 제주은행 | Stage4B-Local-PriceOnly | 2024-02-19 | 2024-02-19 | 15240 | 10.89 | -28.02 | 10.89 | -47.51 | current_profile_correct | 4B_overlay_only |


## 12. Trigger-Level OHLC Backtest Tables

### Representative trigger rows

| symbol | entry | 30D MFE | 30D MAE | 90D MFE | 90D MAE | 180D MFE | 180D MAE | 1Y MFE | 2Y MFE | peak_date | peak_price | drawdown_after_peak |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 105560 | 67600 | 16.27 | -11.69 | 23.37 | -11.69 | 53.7 | -11.69 | 53.7 | 152.22 | 2026-02-13 | 170500 | -3.99 |
| 055550 | 44150 | 16.65 | -9.74 | 16.65 | -9.74 | 46.32 | -9.74 | 46.32 | 142.81 | 2026-02-12 | 107200 | -7.18 |
| 323410 | 29550 | 3.72 | -15.57 | 3.72 | -32.15 | 3.72 | -37.43 | 3.72 | 3.72 | 2024-02-27 | 30650 | -39.67 |
| 006220 | 13620 | 15.42 | -20.48 | 24.08 | -19.46 | 24.08 | -41.26 | 24.08 | 24.08 | 2024-04-19 | 16900 | -53.79 |


The pattern is visible. Positive C21 bank cases accepted early drawdown but then produced +46% to +54% 180D MFE. Policy-only/digital-premium and micro-bank price squeeze cases carried much worse MAE and failed to create the same durable rerating bridge.

## 13. Current Calibrated Profile Stress Test

| Case | Current proxy verdict | Actual path | Residual diagnosis |
|---|---|---|---|
| KB금융 | current_profile_correct | 180D MFE +53.70%, 180D MAE -11.69% | Stage2-Actionable was justified if capital-return execution was credited |
| 신한지주 | current_profile_correct | 180D MFE +46.32%, 180D MAE -9.74% | Similar C21 mechanism; Yellow/Green strictness should not erase the actionable entry |
| 카카오뱅크 | current_profile_false_positive | 180D MFE +3.72%, 180D MAE -37.43% | Broad policy beta should not be counted like executed capital return |
| 제주은행 | current_profile_correct after price-only guard | 180D MFE +24.08%, 180D MAE -41.26% | Price-only Value-up squeeze belongs to 4B/watch, not positive Stage2/3 |

Answers to required stress-test questions:

```text
1. current profile would be right on KB/Shinhan if executed capital-return evidence is represented.
2. current profile can be too early on KakaoBank if policy beta is over-weighted.
3. stage2_actionable_evidence_bonus is not globally wrong; it is too broad for C21 unless execution evidence exists.
4. Yellow threshold 75 is acceptable, but C21 needs a sector component gate under it.
5. Green 87/revision 55 is acceptable; waiting for Green alone loses too much of C21 rerating.
6. price-only blowoff guard is strengthened by 제주은행.
7. full 4B non-price requirement is kept; 제주은행's first peak was price-only local 4B, not full thesis break.
8. hard 4C was not directly validated in this loop.
```

## 14. Stage2 / Yellow / Green Comparison

For C21, Green can be late because the market reprices bank capital discipline before full revision confirmation. This loop does not re-propose the global Stage2 bonus. It narrows it:

```text
if C21 and financial:
    Stage2-Actionable bonus applies only when capital_return_execution_score is supported.
else:
    policy beta alone remains watchlist / narrative-only or low-weight Stage2.
```

Approximate lateness illustration:

| Case | Stage2 actionable entry | Later confirmation proxy | Full/180D peak used | Green lateness reading |
|---|---:|---:|---:|---|
| KB금융 | 67,600 | 101,000 near 2024-10-25 | 103,900 local 180D high | would consume most of local upside |
| 신한지주 | 44,150 | 60,700 near 2024-07-29 | 64,600 local 180D high | would consume most of local upside |
| 카카오뱅크 | 29,550 | no valid Green | 30,650 | no confirmed Stage3-Green trigger |
| 제주은행 | 13,620 | no valid Green | 16,900 | price-only path; no positive Green |

## 15. 4B Local vs Full-window Timing Audit

The key 4B audit is 제주은행.

```text
Stage2/policy-beta representative entry = 2024-02-02 close 13,620
local price-only 4B entry = 2024-02-19 close 15,240
local peak proxy = 2024-02-20 high 15,720
full observed blowoff peak = 2024-04-19 high 16,900

four_b_local_peak_proximity = 0.771
four_b_full_window_peak_proximity = 0.494
four_b_timing_verdict = price_only_local_4B_too_early
do_not_treat_as_full_4B = true
```

Interpretation: the early squeeze was a valid risk overlay, but not a full exit-quality 4B unless supported by non-price deterioration, dilution, contract/legal risk, or an explicit event cap. This strengthens the existing `full_4b_requires_non_price_evidence` axis.

## 16. 4C Protection Audit

No hard 4C thesis-break event is validated in this loop. The counterexamples are better treated as:

```text
카카오뱅크 = failed_rerating / policy-beta false positive
제주은행 = price-only blowoff / 4B watch
four_c_protection_label = thesis_break_watch_only
```

Future C21 holdout should include a true thesis-break case such as a bank with explicit capital-return rollback, credit-cost shock, regulatory capital constraint, or dividend/buyback cancellation.

## 17. Sector-Specific Rule Candidate

```text
rule_id = L6_C21_capital_return_execution_gate
rule_scope = sector_specific
large_sector_id = L6_FINANCIAL_CAPITAL_RETURN_DIGITAL
canonical_archetype_id = C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN

proposal:
- Add a C21-specific capital_return_execution_score.
- Give Stage2-Actionable promotion only when policy beta is paired with executed or board-level capital-return evidence.
- Treat broad Value-up policy, low-PBR label, or relative strength alone as insufficient.
- Add a micro-bank price-only squeeze guard.
```

Rule effect:

```text
Positive preserved:
- KB금융
- 신한지주

Counterexamples blocked or downgraded:
- 카카오뱅크
- 제주은행
```

## 18. Canonical-Archetype Rule Candidate

```text
rule_id = C21_capital_return_execution_vs_policy_beta
rule_scope = canonical_archetype_specific

Required positive C21 components:
1. roe_pbr_capital_return_score supported
2. capital_return_execution_score supported
3. policy_or_regulatory_score may add context but cannot substitute for #1 and #2
4. digital_bank_premium_risk_score and microcap_policy_beta_volatility_score act as guard components
```

This is the compressed archetype rule. It does not create a new global axis.

## 19. Before / After Backtest Comparison

| profile | profile_id | hypothesis | eligible_triggers | avg_MFE_90D | avg_MAE_90D | avg_MFE_180D | avg_MAE_180D | false_positive_rate | missed_structural_count | alignment |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| P0 | e2r_2_1_stock_web_calibrated_proxy | current global calibrated proxy | 4 | 16.95 | -18.26 | 31.96 | -25.03 | 2/4 under broad policy interpretation | 1 | medium: positive banks align, policy-only cases leak |
| P0b | e2r_2_0_baseline_reference | old baseline reference | 4 | 16.95 | -18.26 | 31.96 | -25.03 | 2/4 | 2 | weak: more price/policy leakage |
| P1 | sector_specific_candidate_profile | L6 bank-capital-return execution gate | 2 | 20.01 | -10.71 | 50.01 | -10.71 | 0/2 | 0 | better: selects executed capital-return cases only |
| P2 | canonical_archetype_candidate_profile | C21 capital-return execution + low-PBR asymmetry gate | 2 | 20.01 | -10.71 | 50.01 | -10.71 | 0/2 | 0 | best candidate for ledger |
| P3 | counterexample_guard_profile | digital-bank premium/micro-bank price-only guard | 2 | 13.9 | -25.8 | 13.9 | -39.34 | blocked | 0 | guard: do not promote policy-only/price-only cases |


## 20. Score-Return Alignment Matrix

| Case | Before score/label | After score/label | 180D outcome | Alignment |
|---|---:|---:|---:|---|
| KB금융 | 82 / Stage3-Yellow | 88 / Stage3-Green | MFE +53.70 / MAE -11.69 | improved positive alignment |
| 신한지주 | 78 / Stage3-Yellow | 85 / Stage3-Yellow | MFE +46.32 / MAE -9.74 | kept positive without over-Green |
| 카카오뱅크 | 76 / Stage3-Yellow | 61 / Watch/Blocked | MFE +3.72 / MAE -37.43 | false positive blocked |
| 제주은행 | 80 / false Yellow | 52 / 4B-Watch | MFE +24.08 / MAE -41.26 | price-only squeeze blocked |

## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive_case_count | counterexample_count | 4B_case_count | 4C_case_count | new_independent_case_count | reused_case_count | calibration_usable_trigger_count | representative_trigger_count | current_profile_error_count | sector_rule_candidate | canonical_rule_candidate | coverage_gap_after_this_loop |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| L6_FINANCIAL_CAPITAL_RETURN_DIGITAL | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | BANK_VALUEUP_CAPITAL_RETURN_EXECUTION_VS_POLICY_BETA_GUARD | 2 | 2 | 1 | 0 | 4 | 0 | 5 | 4 | 1 | True | True | after loop: C21 still needs insurer/holding-company holdout and 4C thesis-break examples |


## 22. Residual Contribution Summary

```text
new_independent_case_count: 4
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 4
same_archetype_new_symbol_count: 4
same_archetype_new_trigger_family_count: 4
new_canonical_archetype_count: 1
new_fine_archetype_count: 3
new_trigger_family_count: 5

tested_existing_calibrated_axes:
- stage2_actionable_evidence_bonus
- stage3_yellow_total_min
- stage3_green_total_min
- price_only_blowoff_blocks_positive_stage
- full_4b_requires_non_price_evidence

residual_error_types_found:
- policy_beta_false_positive
- digital_bank_premium_misread
- micro_bank_price_only_blowoff

new_axis_proposed:
- C21_capital_return_execution_gate
- C21_digital_bank_premium_guard
- L6_micro_bank_policy_beta_volatility_guard

existing_axis_strengthened:
- price_only_blowoff_blocks_positive_stage
- full_4b_requires_non_price_evidence

existing_axis_weakened:
- null

existing_axis_kept:
- stage3_yellow_total_min
- stage3_green_total_min
- stage3_green_revision_min

sector_specific_rule_candidate: true
canonical_archetype_rule_candidate: true
no_new_signal_reason: null

loop_contribution_label: canonical_archetype_rule_candidate
do_not_propose_new_weight_delta: false
auto_selected_coverage_gap: R6/L6 C21 financial capital-return residual
```

## 23. Validation Scope / Non-Validation Scope

Validated:

```text
- Stock-Web manifest max_date checked as 2026-02-20.
- Representative entry_date / entry_price taken from tradable_raw shards.
- 30D / 90D / 180D MFE and MAE calculated from fetched stock-web rows.
- 1Y / 2Y fields populated where observed rows exist through manifest max_date.
- Current calibrated profile stress-tested as a proxy, not production code.
- Positive and counterexample balance satisfied.
```

Not validated:

```text
- No live scan.
- No current candidate discovery.
- No brokerage/API trading logic.
- No stock_agent src/e2r code read.
- No production scoring patch.
- No guarantee that this shadow proposal should be promoted without batch aggregation.
```

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,capital_return_execution_gate,canonical_archetype_specific,L6_FINANCIAL_CAPITAL_RETURN_DIGITAL,C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN,0,1,+1,"C21 needs explicit buyback/cancellation/dividend/ROE target evidence, not broad Value-up beta alone",blocks 2 counterexamples while keeping 2 positives,R6L12_C21_KBFIN_20240208_CAPITAL_RETURN_T1|R6L12_C21_SHINHAN_20240208_CAPITAL_RETURN_T1|R6L12_C21_KAKAOBANK_20240227_POLICY_BETA_FAIL_T1|R6L12_C21_JEJUBANK_20240202_PRICE_ONLY_BLOWOFF_T1,4,4,2,medium,canonical_shadow_only,not production; post-calibrated residual
shadow_weight,digital_bank_premium_guard,canonical_archetype_specific,L6_FINANCIAL_CAPITAL_RETURN_DIGITAL,C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN,0,1,+1,internet-bank premium valuation is not the same as low-PBR capital-return rerating,KakaoBank false-positive reduced,R6L12_C21_KAKAOBANK_20240227_POLICY_BETA_FAIL_T1,1,1,1,medium,canonical_shadow_only,guard only
shadow_weight,micro_bank_policy_beta_volatility_guard,sector_specific,L6_FINANCIAL_CAPITAL_RETURN_DIGITAL,C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN,0,1,+1,small-bank price-only squeeze has high MAE and no durable capital-return evidence,"JejuBank treated as 4B/watch, not Stage2/3",R6L12_C21_JEJUBANK_20240202_PRICE_ONLY_BLOWOFF_T1|R6L12_C21_JEJUBANK_20240219_LOCAL_4B_T2,2,1,1,low_to_medium,sector_shadow_only,overlay guard
```

## 25. Machine-Readable Rows

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
{"row_type":"case","case_id":"R6L12_C21_KBFIN_20240208_CAPITAL_RETURN","symbol":"105560","company_name":"KB금융","round":"R6","loop":"12","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","fine_archetype_id":"BANK_VALUEUP_CAPITAL_RETURN_EXECUTION_VS_POLICY_BETA_GUARD","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"R6L12_C21_KBFIN_20240208_CAPITAL_RETURN_T1","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"aligned_positive","current_profile_verdict":"current_profile_correct","price_source":"Songdaiki/stock-web","notes":"2023 result/shareholder-return disclosure plus Corporate Value-up policy beta; board-level capital return visibility existed before full rerating."}
{"row_type":"case","case_id":"R6L12_C21_SHINHAN_20240208_CAPITAL_RETURN","symbol":"055550","company_name":"신한지주","round":"R6","loop":"12","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","fine_archetype_id":"BANK_VALUEUP_CAPITAL_RETURN_EXECUTION_VS_POLICY_BETA_GUARD","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"R6L12_C21_SHINHAN_20240208_CAPITAL_RETURN_T1","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"aligned_positive","current_profile_verdict":"current_profile_correct","price_source":"Songdaiki/stock-web","notes":"Capital-return disclosure, bank-sector Value-up policy beta, and improving payout/ROE visibility; not merely low-PBR price action."}
{"row_type":"case","case_id":"R6L12_C21_KAKAOBANK_20240227_POLICY_BETA_FAIL","symbol":"323410","company_name":"카카오뱅크","round":"R6","loop":"12","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","fine_archetype_id":"BANK_VALUEUP_CAPITAL_RETURN_EXECUTION_VS_POLICY_BETA_GUARD","case_type":"failed_rerating","positive_or_counterexample":"counterexample","best_trigger":"R6L12_C21_KAKAOBANK_20240227_POLICY_BETA_FAIL_T1","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"negative_guard_needed","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"Corporate Value-up policy beta existed, but C21-specific capital-return execution and low-PBR rerating asymmetry were weak; digital-bank premium did not supply the same ROE/PBR value-up setup."}
{"row_type":"case","case_id":"R6L12_C21_JEJUBANK_20240202_PRICE_ONLY_BLOWOFF","symbol":"006220","company_name":"제주은행","round":"R6","loop":"12","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","fine_archetype_id":"BANK_VALUEUP_CAPITAL_RETURN_EXECUTION_VS_POLICY_BETA_GUARD","case_type":"price_moved_without_evidence","positive_or_counterexample":"counterexample","best_trigger":"R6L12_C21_JEJUBANK_20240202_PRICE_ONLY_BLOWOFF_T1","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"negative_guard_needed","current_profile_verdict":"current_profile_correct","price_source":"Songdaiki/stock-web","notes":"Low-PBR/policy-beta and small-bank price squeeze existed, but no durable ROE/PBR capital-return execution evidence sufficient for positive Stage2/3."}
{"row_type":"trigger","trigger_id":"R6L12_C21_KBFIN_20240208_CAPITAL_RETURN_T1","case_id":"R6L12_C21_KBFIN_20240208_CAPITAL_RETURN","symbol":"105560","company_name":"KB금융","round":"R6","loop":"12","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","fine_archetype_id":"BANK_VALUEUP_CAPITAL_RETURN_EXECUTION_VS_POLICY_BETA_GUARD","sector":"financials/capital-return","primary_archetype":"ROE-PBR capital return rerating vs policy beta","loop_objective":"sector_specific_rule_discovery;canonical_archetype_compression;counterexample_mining","trigger_type":"Stage2-Actionable","trigger_date":"2024-02-08","evidence_available_at_that_date":"2023 result/shareholder-return disclosure plus Corporate Value-up policy beta; board-level capital return visibility existed before full rerating.","evidence_source":"public company disclosure + Korea Corporate Value-up programme context","stage2_evidence_fields":["public_event_or_disclosure","policy_or_regulatory_optionality","early_revision_signal"],"stage3_evidence_fields":["confirmed_revision","financial_visibility","multiple_public_sources","low_red_team_risk"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/105/105560/2024.csv","profile_path":"atlas/symbol_profiles/105/105560.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-02-08","entry_price":67600,"MFE_30D_pct":16.27,"MFE_90D_pct":23.37,"MFE_180D_pct":53.7,"MFE_1Y_pct":53.7,"MFE_2Y_pct":152.22,"MAE_30D_pct":-11.69,"MAE_90D_pct":-11.69,"MAE_180D_pct":-11.69,"MAE_1Y_pct":-11.69,"MAE_2Y_pct":-11.69,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2026-02-13","peak_price":170500,"drawdown_after_peak_pct":-3.99,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_applicable","four_b_evidence_type":[],"four_c_protection_label":"not_applicable","trigger_outcome_label":"structural_success","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":504,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R6L12_C21_KBFIN_20240208_CAPITAL_RETURN_2024-02-08_67600","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"R6L12_C21_SHINHAN_20240208_CAPITAL_RETURN_T1","case_id":"R6L12_C21_SHINHAN_20240208_CAPITAL_RETURN","symbol":"055550","company_name":"신한지주","round":"R6","loop":"12","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","fine_archetype_id":"BANK_VALUEUP_CAPITAL_RETURN_EXECUTION_VS_POLICY_BETA_GUARD","sector":"financials/capital-return","primary_archetype":"ROE-PBR capital return rerating vs policy beta","loop_objective":"sector_specific_rule_discovery;canonical_archetype_compression;counterexample_mining","trigger_type":"Stage2-Actionable","trigger_date":"2024-02-08","evidence_available_at_that_date":"Capital-return disclosure, bank-sector Value-up policy beta, and improving payout/ROE visibility; not merely low-PBR price action.","evidence_source":"public company disclosure + Korea Corporate Value-up programme context","stage2_evidence_fields":["public_event_or_disclosure","policy_or_regulatory_optionality","early_revision_signal"],"stage3_evidence_fields":["confirmed_revision","financial_visibility","multiple_public_sources","low_red_team_risk"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/055/055550/2024.csv","profile_path":"atlas/symbol_profiles/055/055550.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-02-08","entry_price":44150,"MFE_30D_pct":16.65,"MFE_90D_pct":16.65,"MFE_180D_pct":46.32,"MFE_1Y_pct":46.32,"MFE_2Y_pct":142.81,"MAE_30D_pct":-9.74,"MAE_90D_pct":-9.74,"MAE_180D_pct":-9.74,"MAE_1Y_pct":-9.74,"MAE_2Y_pct":-9.74,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2026-02-12","peak_price":107200,"drawdown_after_peak_pct":-7.18,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_applicable","four_b_evidence_type":[],"four_c_protection_label":"not_applicable","trigger_outcome_label":"structural_success","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":504,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R6L12_C21_SHINHAN_20240208_CAPITAL_RETURN_2024-02-08_44150","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"R6L12_C21_KAKAOBANK_20240227_POLICY_BETA_FAIL_T1","case_id":"R6L12_C21_KAKAOBANK_20240227_POLICY_BETA_FAIL","symbol":"323410","company_name":"카카오뱅크","round":"R6","loop":"12","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","fine_archetype_id":"BANK_VALUEUP_CAPITAL_RETURN_EXECUTION_VS_POLICY_BETA_GUARD","sector":"financials/capital-return","primary_archetype":"ROE-PBR capital return rerating vs policy beta","loop_objective":"sector_specific_rule_discovery;canonical_archetype_compression;counterexample_mining","trigger_type":"Stage2-Policy-Beta","trigger_date":"2024-02-26","evidence_available_at_that_date":"Corporate Value-up policy beta existed, but C21-specific capital-return execution and low-PBR rerating asymmetry were weak; digital-bank premium did not supply the same ROE/PBR value-up setup.","evidence_source":"public company disclosure + Korea Corporate Value-up programme context","stage2_evidence_fields":["policy_or_regulatory_optionality"],"stage3_evidence_fields":[],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/323/323410/2024.csv","profile_path":"atlas/symbol_profiles/323/323410.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-02-27","entry_price":29550,"MFE_30D_pct":3.72,"MFE_90D_pct":3.72,"MFE_180D_pct":3.72,"MFE_1Y_pct":3.72,"MFE_2Y_pct":3.72,"MAE_30D_pct":-15.57,"MAE_90D_pct":-32.15,"MAE_180D_pct":-37.43,"MAE_1Y_pct":-37.43,"MAE_2Y_pct":-37.43,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-02-27","peak_price":30650,"drawdown_after_peak_pct":-39.67,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_applicable","four_b_evidence_type":[],"four_c_protection_label":"not_applicable","trigger_outcome_label":"failed_rerating","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":504,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R6L12_C21_KAKAOBANK_20240227_POLICY_BETA_FAIL_2024-02-27_29550","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"R6L12_C21_JEJUBANK_20240202_PRICE_ONLY_BLOWOFF_T1","case_id":"R6L12_C21_JEJUBANK_20240202_PRICE_ONLY_BLOWOFF","symbol":"006220","company_name":"제주은행","round":"R6","loop":"12","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","fine_archetype_id":"BANK_VALUEUP_CAPITAL_RETURN_EXECUTION_VS_POLICY_BETA_GUARD","sector":"financials/capital-return","primary_archetype":"ROE-PBR capital return rerating vs policy beta","loop_objective":"sector_specific_rule_discovery;canonical_archetype_compression;counterexample_mining","trigger_type":"Stage4B-Overlay","trigger_date":"2024-02-02","evidence_available_at_that_date":"Low-PBR/policy-beta and small-bank price squeeze existed, but no durable ROE/PBR capital-return execution evidence sufficient for positive Stage2/3.","evidence_source":"public company disclosure + Korea Corporate Value-up programme context","stage2_evidence_fields":["relative_strength","policy_or_regulatory_optionality"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["price_only_local_peak","positioning_overheat"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/006/006220/2024.csv","profile_path":"atlas/symbol_profiles/006/006220.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-02-02","entry_price":13620,"MFE_30D_pct":15.42,"MFE_90D_pct":24.08,"MFE_180D_pct":24.08,"MFE_1Y_pct":24.08,"MFE_2Y_pct":24.08,"MAE_30D_pct":-20.48,"MAE_90D_pct":-19.46,"MAE_180D_pct":-41.26,"MAE_1Y_pct":-42.66,"MAE_2Y_pct":-42.66,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-04-19","peak_price":16900,"drawdown_after_peak_pct":-53.79,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"price_only_blowoff_blocked_as_positive_stage","four_b_evidence_type":["price_only_local_peak","positioning_overheat"],"four_c_protection_label":"not_applicable","trigger_outcome_label":"price_only_blowoff_counterexample","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":504,"calibration_block_reasons":[],"corporate_action_window_status":"historical_profile_has_old_corporate_action_candidates_but_2024_180D_window_clean","same_entry_group_id":"R6L12_C21_JEJUBANK_20240202_PRICE_ONLY_BLOWOFF_2024-02-02_13620","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"R6L12_C21_JEJUBANK_20240219_LOCAL_4B_T2","case_id":"R6L12_C21_JEJUBANK_20240202_PRICE_ONLY_BLOWOFF","symbol":"006220","company_name":"제주은행","round":"R6","loop":"12","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","fine_archetype_id":"BANK_VALUEUP_CAPITAL_RETURN_EXECUTION_VS_POLICY_BETA_GUARD","sector":"financials/capital-return","primary_archetype":"price-only policy-beta 4B overlay","loop_objective":"4B_non_price_requirement_stress_test","trigger_type":"Stage4B-Local-PriceOnly","trigger_date":"2024-02-19","evidence_available_at_that_date":"Local price squeeze after policy/low-PBR theme; no new durable capital-return evidence.","evidence_source":"stock-web price path + public Value-up policy context","stage2_evidence_fields":["relative_strength","policy_or_regulatory_optionality"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["price_only_local_peak","positioning_overheat"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/006/006220/2024.csv","profile_path":"atlas/symbol_profiles/006/006220.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-02-19","entry_price":15240,"MFE_30D_pct":0.0,"MFE_90D_pct":10.89,"MFE_180D_pct":10.89,"MFE_1Y_pct":10.89,"MFE_2Y_pct":10.89,"MAE_30D_pct":-28.94,"MAE_90D_pct":-28.02,"MAE_180D_pct":-47.51,"MAE_1Y_pct":-48.75,"MAE_2Y_pct":-48.75,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-04-19","peak_price":16900,"drawdown_after_peak_pct":-53.79,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":0.771,"four_b_full_window_peak_proximity":0.494,"four_b_timing_verdict":"price_only_local_4B_too_early","four_b_evidence_type":["price_only","positioning_overheat"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"price_only_local_peak_not_full_4B","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":504,"calibration_block_reasons":[],"corporate_action_window_status":"historical_profile_has_old_corporate_action_candidates_but_2024_180D_window_clean","same_entry_group_id":"R6L12_C21_JEJUBANK_20240219_15240","dedupe_for_aggregate":false,"aggregate_group_role":"4B_overlay_only","is_new_independent_case":false,"reuse_reason":"same_symbol_new_trigger_family_4B_timing","independent_evidence_weight":0.25,"do_not_count_as_new_case":false}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R6L12_C21_KBFIN_20240208_CAPITAL_RETURN","trigger_id":"R6L12_C21_KBFIN_20240208_CAPITAL_RETURN_T1","symbol":"105560","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","raw_component_scores_before":{"contract_score":"unknown_or_not_supported","backlog_visibility_score":"unknown_or_not_supported","margin_bridge_score":45,"revision_score":55,"relative_strength_score":62,"customer_quality_score":"unknown_or_not_supported","policy_or_regulatory_score":70,"valuation_repricing_score":63,"execution_risk_score":15,"legal_or_contract_risk_score":5,"dilution_cb_risk_score":"unknown_or_not_supported","accounting_trust_risk_score":5,"roe_pbr_capital_return_score":70,"capital_return_execution_score":58,"digital_bank_premium_risk_score":"unknown_or_not_supported","microcap_policy_beta_volatility_score":"unknown_or_not_supported","positioning_overheat_score":20},"weighted_score_before":82,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":"unknown_or_not_supported","backlog_visibility_score":"unknown_or_not_supported","margin_bridge_score":48,"revision_score":58,"relative_strength_score":62,"customer_quality_score":"unknown_or_not_supported","policy_or_regulatory_score":70,"valuation_repricing_score":67,"execution_risk_score":12,"legal_or_contract_risk_score":5,"dilution_cb_risk_score":"unknown_or_not_supported","accounting_trust_risk_score":5,"roe_pbr_capital_return_score":78,"capital_return_execution_score":72,"digital_bank_premium_risk_score":"unknown_or_not_supported","microcap_policy_beta_volatility_score":"unknown_or_not_supported","positioning_overheat_score":20},"weighted_score_after":88,"stage_label_after":"Stage3-Green","changed_components":["roe_pbr_capital_return_score","capital_return_execution_score","policy_or_regulatory_score","digital_bank_premium_risk_score","microcap_policy_beta_volatility_score"],"component_delta_explanation":"C21 shadow profile separates executed capital-return evidence from broad Value-up/policy beta and price-only relative strength.","MFE_90D_pct":23.37,"MAE_90D_pct":-11.69,"score_return_alignment_label":"aligned","current_profile_verdict":"current_profile_correct"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R6L12_C21_SHINHAN_20240208_CAPITAL_RETURN","trigger_id":"R6L12_C21_SHINHAN_20240208_CAPITAL_RETURN_T1","symbol":"055550","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","raw_component_scores_before":{"contract_score":"unknown_or_not_supported","backlog_visibility_score":"unknown_or_not_supported","margin_bridge_score":42,"revision_score":50,"relative_strength_score":59,"customer_quality_score":"unknown_or_not_supported","policy_or_regulatory_score":68,"valuation_repricing_score":60,"execution_risk_score":18,"legal_or_contract_risk_score":5,"dilution_cb_risk_score":"unknown_or_not_supported","accounting_trust_risk_score":5,"roe_pbr_capital_return_score":66,"capital_return_execution_score":55,"digital_bank_premium_risk_score":"unknown_or_not_supported","microcap_policy_beta_volatility_score":"unknown_or_not_supported","positioning_overheat_score":18},"weighted_score_before":78,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":"unknown_or_not_supported","backlog_visibility_score":"unknown_or_not_supported","margin_bridge_score":44,"revision_score":53,"relative_strength_score":59,"customer_quality_score":"unknown_or_not_supported","policy_or_regulatory_score":68,"valuation_repricing_score":64,"execution_risk_score":15,"legal_or_contract_risk_score":5,"dilution_cb_risk_score":"unknown_or_not_supported","accounting_trust_risk_score":5,"roe_pbr_capital_return_score":74,"capital_return_execution_score":68,"digital_bank_premium_risk_score":"unknown_or_not_supported","microcap_policy_beta_volatility_score":"unknown_or_not_supported","positioning_overheat_score":18},"weighted_score_after":85,"stage_label_after":"Stage3-Yellow","changed_components":["roe_pbr_capital_return_score","capital_return_execution_score","policy_or_regulatory_score","digital_bank_premium_risk_score","microcap_policy_beta_volatility_score"],"component_delta_explanation":"C21 shadow profile separates executed capital-return evidence from broad Value-up/policy beta and price-only relative strength.","MFE_90D_pct":16.65,"MAE_90D_pct":-9.74,"score_return_alignment_label":"aligned","current_profile_verdict":"current_profile_correct"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R6L12_C21_KAKAOBANK_20240227_POLICY_BETA_FAIL","trigger_id":"R6L12_C21_KAKAOBANK_20240227_POLICY_BETA_FAIL_T1","symbol":"323410","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","raw_component_scores_before":{"contract_score":"unknown_or_not_supported","backlog_visibility_score":"unknown_or_not_supported","margin_bridge_score":30,"revision_score":38,"relative_strength_score":28,"customer_quality_score":"unknown_or_not_supported","policy_or_regulatory_score":62,"valuation_repricing_score":48,"execution_risk_score":35,"legal_or_contract_risk_score":8,"dilution_cb_risk_score":"unknown_or_not_supported","accounting_trust_risk_score":8,"roe_pbr_capital_return_score":42,"capital_return_execution_score":20,"digital_bank_premium_risk_score":70,"microcap_policy_beta_volatility_score":"unknown_or_not_supported","positioning_overheat_score":30},"weighted_score_before":76,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":"unknown_or_not_supported","backlog_visibility_score":"unknown_or_not_supported","margin_bridge_score":30,"revision_score":35,"relative_strength_score":28,"customer_quality_score":"unknown_or_not_supported","policy_or_regulatory_score":35,"valuation_repricing_score":30,"execution_risk_score":45,"legal_or_contract_risk_score":8,"dilution_cb_risk_score":"unknown_or_not_supported","accounting_trust_risk_score":8,"roe_pbr_capital_return_score":28,"capital_return_execution_score":10,"digital_bank_premium_risk_score":85,"microcap_policy_beta_volatility_score":"unknown_or_not_supported","positioning_overheat_score":30},"weighted_score_after":61,"stage_label_after":"Watch/Blocked","changed_components":["roe_pbr_capital_return_score","capital_return_execution_score","policy_or_regulatory_score","digital_bank_premium_risk_score","microcap_policy_beta_volatility_score"],"component_delta_explanation":"C21 shadow profile separates executed capital-return evidence from broad Value-up/policy beta and price-only relative strength.","MFE_90D_pct":3.72,"MAE_90D_pct":-32.15,"score_return_alignment_label":"blocked_counterexample_after_guard","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R6L12_C21_JEJUBANK_20240202_PRICE_ONLY_BLOWOFF","trigger_id":"R6L12_C21_JEJUBANK_20240202_PRICE_ONLY_BLOWOFF_T1","symbol":"006220","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","raw_component_scores_before":{"contract_score":"unknown_or_not_supported","backlog_visibility_score":"unknown_or_not_supported","margin_bridge_score":15,"revision_score":20,"relative_strength_score":85,"customer_quality_score":"unknown_or_not_supported","policy_or_regulatory_score":62,"valuation_repricing_score":50,"execution_risk_score":55,"legal_or_contract_risk_score":12,"dilution_cb_risk_score":"unknown_or_not_supported","accounting_trust_risk_score":10,"roe_pbr_capital_return_score":25,"capital_return_execution_score":5,"digital_bank_premium_risk_score":"unknown_or_not_supported","microcap_policy_beta_volatility_score":90,"positioning_overheat_score":88},"weighted_score_before":80,"stage_label_before":"Stage3-Yellow(false)","raw_component_scores_after":{"contract_score":"unknown_or_not_supported","backlog_visibility_score":"unknown_or_not_supported","margin_bridge_score":15,"revision_score":20,"relative_strength_score":25,"customer_quality_score":"unknown_or_not_supported","policy_or_regulatory_score":25,"valuation_repricing_score":22,"execution_risk_score":65,"legal_or_contract_risk_score":12,"dilution_cb_risk_score":"unknown_or_not_supported","accounting_trust_risk_score":10,"roe_pbr_capital_return_score":15,"capital_return_execution_score":0,"digital_bank_premium_risk_score":"unknown_or_not_supported","microcap_policy_beta_volatility_score":95,"positioning_overheat_score":90},"weighted_score_after":52,"stage_label_after":"4B-Watch/Blocked","changed_components":["roe_pbr_capital_return_score","capital_return_execution_score","policy_or_regulatory_score","digital_bank_premium_risk_score","microcap_policy_beta_volatility_score"],"component_delta_explanation":"C21 shadow profile separates executed capital-return evidence from broad Value-up/policy beta and price-only relative strength.","MFE_90D_pct":24.08,"MAE_90D_pct":-19.46,"score_return_alignment_label":"blocked_counterexample_after_guard","current_profile_verdict":"current_profile_correct"}
{"row_type":"residual_contribution","round":"R6","loop":"12","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","new_independent_case_count":4,"reused_case_count":0,"new_symbol_count":4,"same_archetype_new_symbol_count":4,"same_archetype_new_trigger_family_count":4,"new_canonical_archetype_count":1,"new_trigger_family_count":5,"positive_case_count":2,"counterexample_count":2,"current_profile_error_count":1,"tested_existing_calibrated_axes":["stage2_actionable_evidence_bonus","stage3_yellow_total_min","stage3_green_total_min","full_4b_requires_non_price_evidence","price_only_blowoff_blocks_positive_stage"],"residual_error_types_found":["policy_beta_false_positive","digital_bank_premium_misread","micro_bank_price_only_blowoff"],"loop_contribution_label":"canonical_archetype_rule_candidate","do_not_propose_new_weight_delta":false,"auto_selected_coverage_gap":"R6/L6 C21 bank-capital-return residual: executed capital return vs broad policy beta"}
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
next_round = R6_loop_13_C22_INSURANCE_RATE_CYCLE_RESERVE
alternative_next_round = R7_loop_14_C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION
reason = C21 now has positive/counterexample coverage; C22 and C23 remain useful residual candidates.
```

## 28. Source Notes

- Stock-Web manifest: `atlas/manifest.json`.
- Stock-Web schema: `atlas/schema.json`.
- Stock-Web shards used:
  - `atlas/ohlcv_tradable_by_symbol_year/105/105560/2024.csv`
  - `atlas/ohlcv_tradable_by_symbol_year/105/105560/2025.csv`
  - `atlas/ohlcv_tradable_by_symbol_year/105/105560/2026.csv`
  - `atlas/ohlcv_tradable_by_symbol_year/055/055550/2024.csv`
  - `atlas/ohlcv_tradable_by_symbol_year/055/055550/2026.csv`
  - `atlas/ohlcv_tradable_by_symbol_year/323/323410/2024.csv`
  - `atlas/ohlcv_tradable_by_symbol_year/006/006220/2024.csv`
- Stock-Web profiles used:
  - `atlas/symbol_profiles/105/105560.json`
  - `atlas/symbol_profiles/055/055550.json`
  - `atlas/symbol_profiles/323/323410.json`
  - `atlas/symbol_profiles/006/006220.json`
- Policy context source family:
  - Korea Corporate Value-up programme news and regulator follow-up reporting, February-May 2024.
- This MD is not investment advice and is not a live watchlist.
