# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

```text
round = R6
loop = 71
scheduled_round = R6
scheduled_loop = 71
large_sector_id = L6_FINANCIAL_CAPITAL_RETURN_DIGITAL
canonical_archetype_id = C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN
fine_archetype_id = BANK_VALUEUP_CAPITAL_RETURN_EXECUTION_VS_PLATFORM_BANK_PRICE_ONLY_BETA
schema_family = v12_sector_archetype_residual
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
price_data_source = Songdaiki/stock-web
price_basis = tradable_raw
price_adjustment_status = raw_unadjusted_marcap
stock_web_manifest_max_date = 2026-02-20
round_schedule_status = valid
round_sector_consistency = pass
```

## 0. Research Metadata

This standalone MD follows the v12 post-calibrated residual research runner. It is not a live scan, not a recommendation, and not a stock_agent code patch. The scheduled state is inherited from the previous generated R5 / loop 71 output, whose next state was R6 / loop 71.

Output filename:

```text
e2r_stock_web_v12_residual_round_R6_loop_71_L6_FINANCIAL_CAPITAL_RETURN_DIGITAL_C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN_research.md
```

## 1. Current Calibrated Profile Assumption

```text
current_default_profile_proxy = e2r_2_1_stock_web_calibrated_proxy
previous_baseline_reference = e2r_2_0_baseline_reference
shadow_weight_only = true
production_scoring_changed = false
```

Existing calibrated axes tested here:

```text
stage2_actionable_evidence_bonus
stage3_yellow_total_min
stage3_green_total_min
stage3_green_revision_min
price_only_blowoff_blocks_positive_stage
full_4b_requires_non_price_evidence
```

Interpretation for C21: a Korea Value-Up headline alone is not enough. The useful bridge is explicit bank/holding-company capital return execution, CET1/capital buffer discipline, ROE/PBR normalization path, and repeatable buyback/dividend policy. A platform-bank or policy-only beta rally can produce large MFE, but it should not be treated as the same weight evidence as bank-holdco capital-return execution.

## 2. Round / Large Sector / Canonical Archetype Scope

```text
scheduled_round = R6
scheduled_loop = 71
large_sector_id = L6_FINANCIAL_CAPITAL_RETURN_DIGITAL
canonical_archetype_id = C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN
fine_archetype_id = BANK_VALUEUP_CAPITAL_RETURN_EXECUTION_VS_PLATFORM_BANK_PRICE_ONLY_BETA
```

R6 is mapped to `L6_FINANCIAL_CAPITAL_RETURN_DIGITAL`, so the round-sector gate passes.

## 3. Previous Coverage / Duplicate Avoidance Check

NO-REPEAT INDEX role: duplicate ledger only.

Observed before this loop:

```text
C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN:
  rows = 150
  symbols = 19
  date_range = 2021-08-06~2025-05-26
  good/bad Stage2 = 52/16
  4B/4C = 7/0
  top covered symbols = 105560, 323410, UNKNOWN_SYMBOL, 086790, 006220
```

Selected cases:

| case_id | symbol | reason for selection | duplicate stance |
|---|---:|---|---|
| C21-R6L71-WOORI-20250210 | 316140 | bank-holdco capital return execution route, not top-covered in No-Repeat snapshot | new independent symbol/trigger family |
| C21-R6L71-BNK-20250113 | 138930 | regional bank value-up / capital return with high-MAE drawdown test | new independent symbol/trigger family |
| C21-R6L71-KAKAOBANK-20250210 | 323410 | top-covered symbol, reused only as a platform-bank price-only beta / 4B guard stress test | soft duplicate allowed by new trigger family and guardrail purpose |

No selected row intentionally reuses the same `canonical_archetype_id + symbol + trigger_type + entry_date` hard key from the No-Repeat examples.

## 4. Stock-Web OHLC Input / Price Source Validation

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
```

Confirmed stock-web source context:

```text
source_name = FinanceData/marcap
price_adjustment_status = raw_unadjusted_marcap
min_date = 1995-05-02
max_date = 2026-02-20
tradable_row_count = 14354401
symbol_count = 5414
calibration_shard_root = atlas/ohlcv_tradable_by_symbol_year
raw_shard_root = atlas/ohlcv_raw_by_symbol_year
```

## 5. Historical Eligibility Gate

| case_id | symbol | entry_date | 180D forward window | corporate-action overlap | calibration_usable |
|---|---:|---:|---|---|---|
| C21-R6L71-WOORI-20250210 | 316140 | 2025-02-10 | pass by 2026-02-20 max_date | none in profile | true |
| C21-R6L71-BNK-20250113 | 138930 | 2025-01-13 | pass by 2026-02-20 max_date | profile CA dates are 2014/2016 only | true |
| C21-R6L71-KAKAOBANK-20250210 | 323410 | 2025-02-10 | pass by 2026-02-20 max_date | none in profile | true |

## 6. Canonical Archetype Compression Map

| canonical_archetype_id | fine/deep route | keep / reject logic |
|---|---|---|
| C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | BANK_HOLDCO_CET1_CAPITAL_RETURN_EXECUTION | promote Stage2 only when the evidence includes explicit capital return and ROE/PBR normalization bridge |
| C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | REGIONAL_BANK_HIGH_MAE_VALUEUP_ROUTE | allow Stage2/Yellows but keep Green strict until drawdown and capital-buffer risk are absorbed |
| C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | PLATFORM_BANK_PRICE_ONLY_OR_POLICY_BETA | do not count as positive capital-return evidence; use as 4B / price-only guard stress test |

## 7. Case Selection Summary

| case_id | company | role | trigger_type | trigger_date | entry_date | entry_price | evidence family |
|---|---|---|---|---:|---:|---:|---|
| C21-R6L71-WOORI-20250210 | 우리금융지주 | structural_success | Stage2-Actionable | 2025-02-10 | 2025-02-10 | 16310 | bank-holdco capital-return execution / value-up repricing |
| C21-R6L71-BNK-20250113 | BNK금융지주 | high_mae_success | Stage2-Actionable | 2025-01-13 | 2025-01-13 | 10940 | regional-bank value-up / dividend-yield / capital buffer route |
| C21-R6L71-KAKAOBANK-20250210 | 카카오뱅크 | price_moved_without_evidence | Stage2 | 2025-02-10 | 2025-02-10 | 23150 | platform-bank beta without durable capital-return bridge |
| C21-R6L71-KAKAOBANK-4B-20250624 | 카카오뱅크 | 4B_overlay_success | Stage4B | 2025-06-24 | 2025-06-24 | 37000 | price-only / platform momentum 4B stress |

## 8. Positive vs Counterexample Balance

```text
positive_case_count = 2
counterexample_count = 1
4B_case_count = 1
calibration_usable_case_count = 3
calibration_usable_trigger_count = 4
```

The loop satisfies the minimum positive/counterexample mix. The 323410 row is not used as new positive capital-return evidence; it is used as a guardrail/4B overlay counterexample because the price path was strong while the C21-specific capital return bridge was weak.

## 9. Evidence Source Map

| case_id | evidence_available_at_that_date | evidence_source | evidence_url_pending | source_proxy_only |
|---|---|---|---|---|
| C21-R6L71-WOORI-20250210 | company/public capital-return and value-up disclosure context; bank-holdco shareholder-return execution visible before/around entry | company IR / public disclosure proxy | true | true |
| C21-R6L71-BNK-20250113 | regional-bank value-up / dividend and capital-buffer route visible around early-2025 repricing | company IR / public disclosure proxy | true | true |
| C21-R6L71-KAKAOBANK-20250210 | Korea Value-Up / platform-bank beta, but no explicit bank-holdco capital-return bridge at trigger | public market/event proxy | true | true |

Data-quality note: exact official evidence URLs are left pending in this MD. Therefore the numeric price path is calibration-usable, but promotion should be treated as `hold_for_verified_evidence_url` before any production-weight change.

## 10. Price Data Source Map

| symbol | profile_path | price_shard_path | profile caveat |
|---:|---|---|---|
| 316140 | atlas/symbol_profiles/316/316140.json | atlas/ohlcv_tradable_by_symbol_year/316/316140/2025.csv | no corporate-action candidate dates in profile |
| 138930 | atlas/symbol_profiles/138/138930.json | atlas/ohlcv_tradable_by_symbol_year/138/138930/2025.csv | profile has historical 2014/2016 corporate-action candidates, no overlap with 2025 window |
| 323410 | atlas/symbol_profiles/323/323410.json | atlas/ohlcv_tradable_by_symbol_year/323/323410/2025.csv | no corporate-action candidate dates in profile |

## 11. Case-by-Case Trigger Grid

| trigger_id | case_id | trigger_type | entry_date | entry_price | MFE_30D | MFE_90D | MFE_180D | MAE_30D | MAE_90D | MAE_180D | current_profile_verdict |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| T-WOORI-S2A-20250210 | C21-R6L71-WOORI-20250210 | Stage2-Actionable | 2025-02-10 | 16310 | 7.30 | 36.11 | 66.16 | -2.27 | -7.97 | -7.97 | current_profile_too_late |
| T-BNK-S2A-20250113 | C21-R6L71-BNK-20250113 | Stage2-Actionable | 2025-01-13 | 10940 | 12.43 | 12.43 | 46.71 | -3.47 | -15.36 | -15.36 | current_profile_too_late |
| T-KAKAOBANK-S2-20250210 | C21-R6L71-KAKAOBANK-20250210 | Stage2 | 2025-02-10 | 23150 | 9.94 | 9.94 | 67.39 | -3.67 | -14.47 | -14.47 | current_profile_false_positive |
| T-KAKAOBANK-4B-20250624 | C21-R6L71-KAKAOBANK-20250210 | Stage4B | 2025-06-24 | 37000 | - | - | - | - | - | - | current_profile_4B_too_late |

## 12. Trigger-Level OHLC Backtest Tables

### Woori Financial / 316140

Observed rows used:

```text
2025-02-10 c=16310
2025-02-19 h=17500
2025-04-09 l=15010
2025-06-24 h=22200
2025-07-15 h=27100
2025-09-08 l=23750 after peak region
```

```text
MFE_30D = (17500 / 16310 - 1) * 100 = 7.30
MAE_30D = (15940 / 16310 - 1) * 100 = -2.27
MFE_90D = (22200 / 16310 - 1) * 100 = 36.11
MAE_90D = (15010 / 16310 - 1) * 100 = -7.97
MFE_180D = (27100 / 16310 - 1) * 100 = 66.16
MAE_180D = (15010 / 16310 - 1) * 100 = -7.97
peak_date = 2025-07-15
peak_price = 27100
drawdown_after_peak_pct ~= (23750 / 27100 - 1) * 100 = -12.36
```

### BNK Financial / 138930

Observed rows used:

```text
2025-01-13 c=10940
2025-01-31 h=12300
2025-04-09 l=9260
2025-07-15 h=16050
```

```text
MFE_30D = (12300 / 10940 - 1) * 100 = 12.43
MAE_30D = (10560 / 10940 - 1) * 100 = -3.47
MFE_90D = (12300 / 10940 - 1) * 100 = 12.43
MAE_90D = (9260 / 10940 - 1) * 100 = -15.36
MFE_180D = (16050 / 10940 - 1) * 100 = 46.71
MAE_180D = (9260 / 10940 - 1) * 100 = -15.36
peak_date = 2025-07-15
peak_price = 16050
drawdown_after_peak_pct ~= (15130 / 16050 - 1) * 100 = -5.73
```

### KakaoBank / 323410

Observed rows used:

```text
2025-02-10 c=23150
2025-02-27 h=25450
2025-04-09 l=19800
2025-06-24 h=38750
2025-07-24 l=28200 after 4B local peak
```

```text
MFE_30D = (25450 / 23150 - 1) * 100 = 9.94
MAE_30D = (22300 / 23150 - 1) * 100 = -3.67
MFE_90D = (25450 / 23150 - 1) * 100 = 9.94
MAE_90D = (19800 / 23150 - 1) * 100 = -14.47
MFE_180D = (38750 / 23150 - 1) * 100 = 67.39
MAE_180D = (19800 / 23150 - 1) * 100 = -14.47
peak_date = 2025-06-24
peak_price = 38750
drawdown_after_peak_pct ~= (28200 / 38750 - 1) * 100 = -27.23
```

## 13. Current Calibrated Profile Stress Test

| case | expected P0 behavior | actual path | verdict |
|---|---|---|---|
| Woori | should wait for non-price capital-return bridge, then Stage2/Y early | MFE180 +66.16 with manageable MAE | current_profile_too_late |
| BNK | should allow Stage2 but keep Green strict because regional-bank drawdown risk remains | MFE180 +46.71 but MAE90 -15.36 | current_profile_too_late |
| KakaoBank | should not count price/platform beta as C21 capital-return evidence | MFE180 high, but drawdown after peak large and capital-return bridge weak | current_profile_false_positive |
| KakaoBank 4B | price-only local peak needed overlay, but full 4B should require non-price evidence | peak on 2025-06-24, drawdown after peak about -27% | current_profile_4B_too_late |

## 14. Stage2 / Yellow / Green Comparison

```text
Green lateness is not computed as a full ratio because this loop uses Stage2/Actionable and 4B stress rows, not a confirmed Stage3-Green label set.
green_lateness_ratio = not_applicable
reason = no_confirmed_Stage3_Green_trigger
```

Interpretation: For bank-holdco names, forcing Stage3-Green confirmation too late can miss a large part of the rerating path. For regional banks, Stage2 is useful but Green must remain guarded by capital-buffer and drawdown risk. For platform banks, price-path success alone must not relax C21 capital-return evidence gates.

## 15. 4B Local vs Full-window Timing Audit

KakaoBank 4B stress:

```text
Stage2_Actionable_entry_price = 23150
Stage4B_entry_price = 37000
local_peak_price_after_Stage2 = 38750
full_window_peak_price_after_Stage2 = 38750
four_b_local_peak_proximity = (37000 - 23150) / (38750 - 23150) = 0.888
four_b_full_window_peak_proximity = 0.888
four_b_timing_verdict = good_local_price_peak_but_price_only_overlay
four_b_evidence_type = price_only | platform_beta | positioning_overheat
```

Rule implication: it is a good 4B timing case for risk overlay, but it should not become a full 4B unless non-price thesis exhaustion, capital-return disappointment, or explicit guidance deterioration is confirmed.

## 16. 4C Protection Audit

No hard 4C event is promoted in this MD.

```text
four_c_protection_label = thesis_break_watch_only
hard_4c_count = 0
```

## 17. Sector-Specific Rule Candidate

```text
rule_scope = sector_specific
sector_specific_rule_candidate = true
```

Candidate: within L6, bank-holdco and regional-bank capital-return cases should receive Stage2/Y attention when non-price capital-return execution is present; platform-bank / price-only policy beta should remain blocked from positive Stage2/Green promotion.

## 18. Canonical-Archetype Rule Candidate

```text
rule_scope = canonical_archetype_specific
canonical_archetype_rule_candidate = true
```

Candidate C21 compression:

```text
C21 positive route:
  explicit CET1/capital-buffer policy
  recurring dividend/buyback/cancellation visibility
  ROE/PBR normalization target
  bank-holdco or regional-bank shareholder-return execution

C21 guard route:
  platform-bank high-PBR beta
  policy-only Value-Up headline
  price-only momentum without capital return bridge
  use for 4B overlay or counterexample, not positive capital-return weight
```

## 19. Before / After Backtest Comparison

| profile_id | hypothesis | eligible triggers | avg MFE90 | avg MAE90 | false positive rate | verdict |
|---|---|---:|---:|---:|---:|---|
| P0 | current calibrated proxy | 3 | 19.49 | -12.60 | 0.33 | too loose for platform bank; too slow for bank-holdco capital return |
| P0b | older baseline reference | 3 | 19.49 | -12.60 | 0.67 | would over-credit policy/price beta |
| P1 | sector-specific L6 bank capital-return bridge | 2 | 24.27 | -11.67 | 0.00 | better alignment for Woori/BNK |
| P2 | C21 canonical capital-return execution profile | 2 | 24.27 | -11.67 | 0.00 | useful but needs verified evidence URL before promotion |
| P3 | counterexample guard profile | 1 | 9.94 | -14.47 | 1.00 | blocks KakaoBank from positive C21 evidence; allows 4B overlay |

## 20. Score-Return Alignment Matrix

| trigger_id | raw_component_scores_before | weighted_score_before | stage_label_before | raw_component_scores_after | weighted_score_after | stage_label_after | component_delta_explanation |
|---|---|---:|---|---|---:|---|---|
| T-WOORI-S2A-20250210 | contract=40, backlog=30, margin=45, revision=55, RS=60, customer=45, policy=70, valuation=65, risk=30 | 74 | Stage2 | capital_return=75, roe_pbr=70, revision=60, valuation=70, risk=35 | 80 | Stage2-Actionable | capital-return bridge receives credit, Green still needs verified URL and repeated execution |
| T-BNK-S2A-20250113 | contract=30, backlog=25, margin=40, revision=45, RS=55, customer=40, policy=65, valuation=70, risk=45 | 71 | Stage2-Watch | capital_return=68, roe_pbr=72, regional_risk=55, drawdown_guard=60 | 76 | Stage2-Actionable | positive but high-MAE route; stage2 useful, Green guarded |
| T-KAKAOBANK-S2-20250210 | contract=10, backlog=0, margin=30, revision=35, RS=70, customer=50, policy=60, valuation=35, risk=60 | 72 | Stage2 | capital_return=20, platform_beta=75, price_only_guard=80, valuation_risk=75 | 64 | Stage2-Watch / 4B candidate | removes positive capital-return credit; keeps 4B/overheat watch |

## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive_case_count | counterexample_count | 4B_case_count | 4C_case_count | new_independent_case_count | reused_case_count | calibration_usable_trigger_count | representative_trigger_count | current_profile_error_count | sector_rule_candidate | canonical_rule_candidate | coverage_gap_after_this_loop |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| L6_FINANCIAL_CAPITAL_RETURN_DIGITAL | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | BANK_VALUEUP_CAPITAL_RETURN_EXECUTION_VS_PLATFORM_BANK_PRICE_ONLY_BETA | 2 | 1 | 1 | 0 | 2 | 1 | 4 | 3 | 3 | true | true | exact official evidence URLs still need verification before weight promotion |

## 22. Residual Contribution Summary

```text
new_independent_case_count: 2
reused_case_count: 1
reused_case_ids: C21-R6L71-KAKAOBANK-20250210
new_symbol_count: 2
new_canonical_archetype_count: 0
new_fine_archetype_count: 1
new_trigger_family_count: 3
tested_existing_calibrated_axes: [stage2_actionable_evidence_bonus, price_only_blowoff_blocks_positive_stage, full_4b_requires_non_price_evidence]
residual_error_types_found: [current_profile_too_late, current_profile_false_positive, current_profile_4B_too_late]
new_axis_proposed: null
existing_axis_strengthened: price_only_blowoff_blocks_positive_stage; full_4b_requires_non_price_evidence
existing_axis_weakened: null
existing_axis_kept: stage3_green_total_min; stage3_green_revision_min
sector_specific_rule_candidate: true
canonical_archetype_rule_candidate: true
no_new_signal_reason: null
loop_contribution_label: canonical_archetype_rule_candidate
do_not_propose_new_weight_delta: true
```

One-line contribution:

```text
This loop adds 2 new independent cases, 1 counterexample, and 3 residual errors for R6/L6_FINANCIAL_CAPITAL_RETURN_DIGITAL/C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN.
```

The file intentionally sets `do_not_propose_new_weight_delta=true` because exact official evidence URLs remain pending. The price-path rows are still useful for residual research and later URL-repair promotion.

## 23. Validation Scope / Non-Validation Scope

Validation scope:

```text
- stock-web tradable_raw OHLC path
- entry date / entry price
- MFE/MAE 30D/90D/180D
- 4B local/full proximity for KakaoBank
- duplicate-avoidance intent against No-Repeat Index
```

Non-validation scope:

```text
- no live candidate scan
- no brokerage API
- no production scoring patch
- no current investment recommendation
- exact official evidence URLs pending; this MD should be re-opened for URL repair before promotion
```

## 24. Shadow Weight Calibration

```text
row_type,round,loop,large_sector_id,canonical_archetype_id,fine_archetype_id,rule_scope,eligible_trigger_count,positive_case_count,counterexample_count,proposed_delta,confidence,implementation_note
shadow_weight,R6,71,L6_FINANCIAL_CAPITAL_RETURN_DIGITAL,C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN,BANK_VALUEUP_CAPITAL_RETURN_EXECUTION_VS_PLATFORM_BANK_PRICE_ONLY_BETA,canonical_archetype_specific,4,2,1,+0,low,"hold pending verified evidence URLs; strengthen guard semantics only"
```

## 25. Machine-Readable Rows

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
{"row_type":"case","case_id":"C21-R6L71-WOORI-20250210","symbol":"316140","company_name":"우리금융지주","round":"R6","loop":"71","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","fine_archetype_id":"BANK_HOLDCO_CET1_CAPITAL_RETURN_EXECUTION","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"T-WOORI-S2A-20250210","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"strong_positive_asymmetry","current_profile_verdict":"current_profile_too_late","price_source":"Songdaiki/stock-web","evidence_url_pending":true,"source_proxy_only":true,"notes":"bank-holdco value-up/capital-return route; exact source URL pending"}
{"row_type":"case","case_id":"C21-R6L71-BNK-20250113","symbol":"138930","company_name":"BNK금융지주","round":"R6","loop":"71","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","fine_archetype_id":"REGIONAL_BANK_CAPITAL_RETURN_HIGH_MAE_ROUTE","case_type":"high_mae_success","positive_or_counterexample":"positive","best_trigger":"T-BNK-S2A-20250113","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"positive_but_high_MAE","current_profile_verdict":"current_profile_too_late","price_source":"Songdaiki/stock-web","evidence_url_pending":true,"source_proxy_only":true,"notes":"regional bank route adds positive but MAE guard matters"}
{"row_type":"case","case_id":"C21-R6L71-KAKAOBANK-20250210","symbol":"323410","company_name":"카카오뱅크","round":"R6","loop":"71","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","fine_archetype_id":"PLATFORM_BANK_PRICE_ONLY_BETA_GUARD","case_type":"price_moved_without_evidence","positive_or_counterexample":"counterexample","best_trigger":"T-KAKAOBANK-S2-20250210","calibration_usable":true,"is_new_independent_case":false,"reuse_reason":"same top-covered symbol but new 2025 platform-bank price-only/4B guard trigger family","independent_evidence_weight":0.5,"score_price_alignment":"price_success_but_not_C21_capital_return_evidence","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","evidence_url_pending":true,"source_proxy_only":true,"notes":"do not count as positive capital-return evidence"}
{"row_type":"trigger","trigger_id":"T-WOORI-S2A-20250210","case_id":"C21-R6L71-WOORI-20250210","symbol":"316140","company_name":"우리금융지주","round":"R6","loop":"71","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","fine_archetype_id":"BANK_HOLDCO_CET1_CAPITAL_RETURN_EXECUTION","loop_objective":"coverage_gap_fill|counterexample_mining|sector_specific_rule_discovery","trigger_type":"Stage2-Actionable","trigger_date":"2025-02-10","evidence_available_at_that_date":"bank-holdco shareholder-return/value-up execution context","evidence_source":"company IR / public disclosure proxy","stage2_evidence_fields":["public_event_or_disclosure","policy_or_regulatory_optionality","early_revision_signal","relative_strength"],"stage3_evidence_fields":["financial_visibility","multiple_public_sources"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/316/316140/2025.csv","profile_path":"atlas/symbol_profiles/316/316140.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2025-02-10","entry_price":16310,"MFE_30D_pct":7.30,"MFE_90D_pct":36.11,"MFE_180D_pct":66.16,"MFE_1Y_pct":"contaminated_or_unavailable","MFE_2Y_pct":"contaminated_or_unavailable","MAE_30D_pct":-2.27,"MAE_90D_pct":-7.97,"MAE_180D_pct":-7.97,"MAE_1Y_pct":"contaminated_or_unavailable","below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2025-07-15","peak_price":27100,"drawdown_after_peak_pct":-12.36,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":null,"four_b_evidence_type":null,"four_c_protection_label":null,"trigger_outcome_label":"structural_success","current_profile_verdict":"current_profile_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_no_overlap","same_entry_group_id":"316140-2025-02-10","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"evidence_url_pending":true,"source_proxy_only":true}
{"row_type":"trigger","trigger_id":"T-BNK-S2A-20250113","case_id":"C21-R6L71-BNK-20250113","symbol":"138930","company_name":"BNK금융지주","round":"R6","loop":"71","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","fine_archetype_id":"REGIONAL_BANK_CAPITAL_RETURN_HIGH_MAE_ROUTE","loop_objective":"coverage_gap_fill|counterexample_mining|sector_specific_rule_discovery","trigger_type":"Stage2-Actionable","trigger_date":"2025-01-13","evidence_available_at_that_date":"regional-bank value-up/shareholder-return route","evidence_source":"company IR / public disclosure proxy","stage2_evidence_fields":["public_event_or_disclosure","policy_or_regulatory_optionality","relative_strength"],"stage3_evidence_fields":["financial_visibility"],"stage4b_evidence_fields":["positioning_overheat"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/138/138930/2025.csv","profile_path":"atlas/symbol_profiles/138/138930.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2025-01-13","entry_price":10940,"MFE_30D_pct":12.43,"MFE_90D_pct":12.43,"MFE_180D_pct":46.71,"MFE_1Y_pct":"contaminated_or_unavailable","MFE_2Y_pct":"contaminated_or_unavailable","MAE_30D_pct":-3.47,"MAE_90D_pct":-15.36,"MAE_180D_pct":-15.36,"MAE_1Y_pct":"contaminated_or_unavailable","below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2025-07-15","peak_price":16050,"drawdown_after_peak_pct":-5.73,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":null,"four_b_evidence_type":null,"four_c_protection_label":null,"trigger_outcome_label":"high_mae_success","current_profile_verdict":"current_profile_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_no_overlap_2025_window","same_entry_group_id":"138930-2025-01-13","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"evidence_url_pending":true,"source_proxy_only":true}
{"row_type":"trigger","trigger_id":"T-KAKAOBANK-S2-20250210","case_id":"C21-R6L71-KAKAOBANK-20250210","symbol":"323410","company_name":"카카오뱅크","round":"R6","loop":"71","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","fine_archetype_id":"PLATFORM_BANK_PRICE_ONLY_BETA_GUARD","loop_objective":"counterexample_mining|4B_non_price_requirement_stress_test","trigger_type":"Stage2","trigger_date":"2025-02-10","evidence_available_at_that_date":"platform-bank/policy beta without explicit capital-return bridge","evidence_source":"public market/event proxy","stage2_evidence_fields":["relative_strength","policy_or_regulatory_optionality"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["positioning_overheat","price_only_local_peak"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/323/323410/2025.csv","profile_path":"atlas/symbol_profiles/323/323410.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2025-02-10","entry_price":23150,"MFE_30D_pct":9.94,"MFE_90D_pct":9.94,"MFE_180D_pct":67.39,"MFE_1Y_pct":"contaminated_or_unavailable","MFE_2Y_pct":"contaminated_or_unavailable","MAE_30D_pct":-3.67,"MAE_90D_pct":-14.47,"MAE_180D_pct":-14.47,"MAE_1Y_pct":"contaminated_or_unavailable","below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2025-06-24","peak_price":38750,"drawdown_after_peak_pct":-27.23,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":0.888,"four_b_full_window_peak_proximity":0.888,"four_b_timing_verdict":"good_local_price_peak_but_price_only_overlay","four_b_evidence_type":"price_only|platform_beta|positioning_overheat","four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"price_success_but_not_C21_positive_evidence","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_no_overlap","same_entry_group_id":"323410-2025-02-10","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":false,"reuse_reason":"same top-covered symbol but new 2025 platform-bank price-only/4B guard trigger family","independent_evidence_weight":0.5,"do_not_count_as_new_case":false,"evidence_url_pending":true,"source_proxy_only":true}
{"row_type":"trigger","trigger_id":"T-KAKAOBANK-4B-20250624","case_id":"C21-R6L71-KAKAOBANK-20250210","symbol":"323410","company_name":"카카오뱅크","round":"R6","loop":"71","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","fine_archetype_id":"PLATFORM_BANK_PRICE_ONLY_BETA_GUARD","loop_objective":"4B_non_price_requirement_stress_test","trigger_type":"Stage4B","trigger_date":"2025-06-24","evidence_available_at_that_date":"local price blowoff; non-price 4B evidence not verified","evidence_source":"price-only local peak proxy","stage2_evidence_fields":[],"stage3_evidence_fields":[],"stage4b_evidence_fields":["valuation_blowoff","positioning_overheat","price_only_local_peak"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/323/323410/2025.csv","profile_path":"atlas/symbol_profiles/323/323410.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2025-06-24","entry_price":37000,"MFE_30D_pct":4.73,"MFE_90D_pct":4.73,"MFE_180D_pct":4.73,"MAE_30D_pct":-23.78,"MAE_90D_pct":-27.23,"MAE_180D_pct":-27.23,"peak_date":"2025-06-24","peak_price":38750,"drawdown_after_peak_pct":-27.23,"four_b_local_peak_proximity":0.888,"four_b_full_window_peak_proximity":0.888,"four_b_timing_verdict":"good_local_price_peak_but_price_only_overlay","four_b_evidence_type":"price_only|positioning_overheat","trigger_outcome_label":"4B_overlay_success_price_only","current_profile_verdict":"current_profile_4B_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_no_overlap","same_entry_group_id":"323410-2025-06-24","dedupe_for_aggregate":false,"aggregate_group_role":"4B_overlay_only","is_new_independent_case":false,"reuse_reason":"4B overlay stress row attached to reused counterexample case","independent_evidence_weight":0.25,"do_not_count_as_new_case":true,"evidence_url_pending":true,"source_proxy_only":true}
{"row_type":"score_simulation","round":"R6","loop":"71","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","profile_id":"P0","profile_scope":"current_calibrated_proxy","eligible_trigger_count":3,"selected_entry_trigger_per_case":"T-WOORI-S2A-20250210|T-BNK-S2A-20250113|T-KAKAOBANK-S2-20250210","avg_MFE_90D_pct":19.49,"avg_MAE_90D_pct":-12.60,"false_positive_rate":0.33,"missed_structural_count":2,"late_green_count":0,"avg_green_lateness_ratio":"not_applicable","avg_four_b_local_peak_proximity":0.888,"avg_four_b_full_window_peak_proximity":0.888,"score_return_alignment_verdict":"mixed_current_profile_too_slow_for_bank_holdcos_but_too_loose_for_platform_beta"}
{"row_type":"shadow_weight","round":"R6","loop":"71","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","fine_archetype_id":"BANK_VALUEUP_CAPITAL_RETURN_EXECUTION_VS_PLATFORM_BANK_PRICE_ONLY_BETA","rule_scope":"canonical_archetype_specific","positive_case_count":2,"counterexample_count":1,"proposed_delta":0,"confidence":"low","do_not_propose_new_weight_delta":true,"reason":"exact evidence URLs pending; use as URL-repair handoff before promotion"}
{"row_type":"coverage_matrix","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","fine_archetype_id":"BANK_VALUEUP_CAPITAL_RETURN_EXECUTION_VS_PLATFORM_BANK_PRICE_ONLY_BETA","positive_case_count":2,"counterexample_count":1,"4B_case_count":1,"4C_case_count":0,"new_independent_case_count":2,"reused_case_count":1,"calibration_usable_trigger_count":4,"representative_trigger_count":3,"current_profile_error_count":3,"sector_rule_candidate":true,"canonical_rule_candidate":true,"coverage_gap_after_this_loop":"verified_evidence_url_repair_needed"}
{"row_type":"residual_contribution","round":"R6","loop":"71","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","new_independent_case_count":2,"reused_case_count":1,"new_symbol_count":2,"new_trigger_family_count":3,"tested_existing_calibrated_axes":["stage2_actionable_evidence_bonus","price_only_blowoff_blocks_positive_stage","full_4b_requires_non_price_evidence"],"residual_error_types_found":["current_profile_too_late","current_profile_false_positive","current_profile_4B_too_late"],"loop_contribution_label":"canonical_archetype_rule_candidate","do_not_propose_new_weight_delta":true}
{"row_type":"narrative_only","case_id":"R6L71-EVIDENCE-URL-REPAIR","symbol":"MULTI","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","reason":"exact official evidence URLs pending for company IR/KRX disclosure references","price_source":"Songdaiki/stock-web","usage":"not_weight_calibration_until_url_repaired"}
```

## 26. Deferred Coding Agent Handoff Prompt

### Purpose

You are now in the repository implementation phase. The attached Markdown files are v12 post-calibrated residual research outputs produced using the Songdaiki/stock-web OHLC atlas.

These MDs are not live candidate research. They are historical calibration research designed to extend the already-applied e2r_2_1_stock_web_calibrated profile.

Do not blindly apply every shadow row. In this MD, `do_not_propose_new_weight_delta=true` because exact official evidence URLs remain pending. Use it first as a URL-repair and guardrail validation handoff.

### Price source context

- Primary historical price source used by the research MD: Songdaiki/stock-web.
- Price basis: tradable_raw.
- Price adjustment status: raw_unadjusted_marcap.
- Price shard pattern: atlas/ohlcv_tradable_by_symbol_year/<prefix>/<ticker>/<year>.csv.
- Symbol profile pattern: atlas/symbol_profiles/<prefix>/<ticker>.json.

### Rules

- Use only calibration_usable=true rows for quantitative calibration.
- Do not count reused cases as new independent evidence unless independent_evidence_weight > 0.
- Do not treat source-proxy rows as promotion-ready until exact evidence URLs are repaired.
- Do not apply global deltas unless multiple large_sector_id values support the same direction.
- Prefer sector_specific or canonical_archetype_specific shadow profiles.
- Positive score promotion requires non-price evidence and clean 180D MFE/MAE.
- 4B rows are overlay/risk calibration only.
- price-only rows cannot promote Stage2/Stage3.

### Expected repository tasks

1. Parse case / trigger / score_simulation / shadow_weight / residual_contribution rows.
2. Validate stock-web price source fields.
3. Validate large_sector_id and canonical_archetype_id.
4. Validate novelty and reuse fields.
5. Deduplicate same_entry_group_id and reused cases.
6. Repair exact official evidence URLs for Woori/BNK/KakaoBank rows.
7. Keep `do_not_propose_new_weight_delta=true` until URL repair passes.
8. Preserve global calibrated profile unless explicitly promoted.
9. Report new independent cases, counterexamples, and residual error types.
10. Add tests that source-proxy loops cannot change weights directly.

### Expected output

- Concise implementation summary.
- Rows accepted/rejected.
- New sector/canonical archetype coverage.
- Existing axis strengthened/weakened/kept.
- No investment recommendation language.

## 27. Next Round State

```text
completed_round = R6
completed_loop = 71
next_round = R7
next_loop = 71
round_schedule_status = valid
round_sector_consistency = pass
```

## 28. Source Notes

```text
primary_price_source = Songdaiki/stock-web
source_basis = FinanceData/marcap transformed into assistant-readable symbol-year CSV shards
price_basis = tradable_raw
price_adjustment_status = raw_unadjusted_marcap
research_artifact_role = historical residual calibration only
investment_recommendation = false
```

