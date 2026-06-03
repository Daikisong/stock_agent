# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
research_session = post_calibrated_sector_archetype_residual_research
round = R13
loop = 25
large_sector_id = L6_FINANCIAL_CAPITAL_RETURN_DIGITAL
canonical_archetype_id = C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN
fine_archetype_id = K_FINANCIAL_VALUE_UP_CAPITAL_RETURN_EXECUTION
output_format = one_standalone_markdown_file
production_scoring_changed = false
shadow_weight_only = true
handoff_prompt_embedded = true
handoff_prompt_executed_now = false
```

This file is a historical calibration artifact only. It is not a live scan, not an investment recommendation, and not a repository patch.

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

The test here is not whether the global profile works in general. The test is narrower: within **financial ROE/PBR/capital-return rerating**, can the model distinguish a real capital-return bridge from a policy-only or price-only mirage?

## 2. Round / Large Sector / Canonical Archetype Scope

- **large_sector_id:** `L6_FINANCIAL_CAPITAL_RETURN_DIGITAL`
- **canonical_archetype_id:** `C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN`
- **fine_archetype_id:** `K_FINANCIAL_VALUE_UP_CAPITAL_RETURN_EXECUTION`
- **loop_objective:** `holdout_validation|residual_false_positive_mining|sector_specific_rule_discovery|canonical_archetype_compression|4B_non_price_requirement_stress_test|counterexample_mining|coverage_gap_fill`

Chosen case mix:

- Positive structural success: KB금융, 신한지주.
- Counterexample / failed rerating: 카카오뱅크, 제주은행.
- 4B / 4C overlay: 제주은행 price-only blowoff and 카카오뱅크 thesis-break watch.

## 3. Previous Coverage / Duplicate Avoidance Check

Allowed research artifact checked:

```text
reports/e2r_calibration/ingest_summary.md
```

Observed calibration state from the allowed artifact:

```text
parsed_document_count = 107
validated_trigger_rows = 1940
aggregate_representative_trigger_rows = 1376
rounds_covered = R1~R13
loops_covered = 1~9
sectors_covered include 금융·자본배분·디지털금융
```

The previous v12 output immediately before this loop covered L5/C20 beauty/global distribution. This loop deliberately moves to L6/C21. All four selected symbols are treated as new independent cases in this loop.

Novelty ratio:

```text
calibration_usable_case_count = 4
new_independent_case_count = 4
new_independent_case_ratio = 1.00
required_new_independent_case_ratio = 0.60
novelty_requirement_status = pass
```

## 4. Stock-Web OHLC Input / Price Source Validation

Manifest fields read from `Songdaiki/stock-web`:

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

Validation status:

```text
price_data_source = Songdaiki/stock-web
price_basis = tradable_raw
price_adjustment_status = raw_unadjusted_marcap
manifest_max_date = 2026-02-20
validation_status = usable_for_historical_calibration
```

## 5. Historical Eligibility Gate

All representative trigger rows pass the historical gate:

- trigger dates are historical.
- entry dates exist in stock-web tradable shards.
- 180D forward trading windows are available before manifest max date.
- high / low / close / volume fields exist.
- no 2024 180D corporate-action candidate overlaps the selected windows.

Profile caveats:

- KB금융: no corporate-action candidate dates in the profile.
- 신한지주: no corporate-action candidate dates in the profile.
- 카카오뱅크: no corporate-action candidate dates in the profile.
- 제주은행: historical corporate-action candidates exist, but all listed candidate dates are pre-2024; the selected 2024 windows are clean for 180D calibration.

## 6. Canonical Archetype Compression Map

```text
fine_archetype: BANK_HOLDCO_VALUE_UP_CAPITAL_RETURN
  -> canonical_archetype_id: C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN

fine_archetype: DIGITAL_BANK_POLICY_REPRICE_WITHOUT_CAPITAL_RETURN_GUARD
  -> canonical_archetype_id: C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN

fine_archetype: MICROBANK_PRICE_ONLY_VALUE_UP_THEME_GUARD
  -> canonical_archetype_id: C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN
```

The compression is important: banks, digital banks, and microbank theme spikes all sit under the same broad C21 umbrella, but the evidence gate must differ. A bank holding company with ROE/PBR discount plus credible capital return is not the same animal as a price-only microbank squeeze.

## 7. Case Selection Summary

| case_id | symbol | company | role | best_trigger | entry_date | entry_price | MFE_90D | MAE_90D | MFE_180D | MAE_180D | current_profile_verdict |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| R13L25_C21_105560_KB_VALUEUP_CAPRETURN | 105560 | KB금융 | positive | Stage2-Actionable | 2024-02-26 | 62500 | 44.0 | -4.48 | 66.24 | -4.48 | current_profile_too_late |
| R13L25_C21_055550_SHINHAN_VALUEUP_CAPRETURN | 055550 | 신한지주 | positive | Stage2-Actionable | 2024-02-26 | 41350 | 31.08 | -3.63 | 56.23 | -3.63 | current_profile_too_late |
| R13L25_C21_323410_KAKAOBANK_DIGITAL_BANK_GROWTH_GUARD | 323410 | 카카오뱅크 | counterexample | Stage2-Candidate | 2024-02-26 | 30150 | 1.66 | -33.5 | 1.66 | -38.67 | current_profile_false_positive |
| R13L25_C21_006220_JEJUBANK_PRICE_ONLY_FALSE_POSITIVE | 006220 | 제주은행 | counterexample | Price-only Stage2 Candidate | 2024-02-01 | 13230 | 27.74 | -17.08 | 27.74 | -39.0 | current_profile_correct |

## 8. Positive vs Counterexample Balance

```text
positive_case_count = 2
counterexample_count = 2
4B_case_count = 1
4C_case_count = 1
minimum_calibration_usable_case_count = 3
positive_counterexample_balance_status = pass
```

Interpretation:

- KB금융 and 신한지주 show that a Stage2 value-up trigger can be valid before formal Green confirmation when ROE/PBR discount and capital-return capacity are visible.
- 카카오뱅크 shows that financial-sector policy exposure alone is not enough.
- 제주은행 shows that microbank price action can mimic a financial value-up candidate but should remain blocked unless non-price capital-return evidence appears.

## 9. Evidence Source Map

| case | evidence family | accepted evidence | rejected evidence |
|---|---|---|---|
| KB금융 | bank holdco value-up | public value-up catalyst, low-PBR financial rerating, later capital-return confirmation | price action alone |
| 신한지주 | bank holdco value-up | public value-up catalyst, bank ROE route, later shareholder-return confirmation | Green-only late entry as first signal |
| 카카오뱅크 | digital bank | policy exposure only | policy-only promotion, growth story without capital-return execution |
| 제주은행 | microbank | relative strength only as risk marker | price-only promotion, local blowoff as positive stage |

External evidence notes:

- Korea's Corporate Value-up Programme was announced in February 2024; Reuters/FT coverage describe its focus on shareholder returns, undervaluation, tax incentives, and the policy's initially voluntary character.
- Company-specific capital-return confirmation dates are represented here as public earnings/shareholder-return disclosure cycles. The quantitative calibration is based only on stock-web OHLC rows.

## 10. Price Data Source Map

| symbol | company | profile_path | key shard |
|---|---|---|---|
| 105560 | KB금융 | atlas/symbol_profiles/105/105560.json | atlas/ohlcv_tradable_by_symbol_year/105/105560/2024.csv |
| 055550 | 신한지주 | atlas/symbol_profiles/055/055550.json | atlas/ohlcv_tradable_by_symbol_year/055/055550/2024.csv |
| 323410 | 카카오뱅크 | atlas/symbol_profiles/323/323410.json | atlas/ohlcv_tradable_by_symbol_year/323/323410/2024.csv |
| 006220 | 제주은행 | atlas/symbol_profiles/006/006220.json | atlas/ohlcv_tradable_by_symbol_year/006/006220/2024.csv |

## 11. Case-by-Case Trigger Grid

| trigger_id | symbol | company | trigger_type | entry_date | entry_price | MFE30 | MFE90 | MFE180 | MAE30 | MAE90 | MAE180 | peak_date | peak_price | green_lateness | current_verdict | aggregate_role |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| R13L25_C21_KB_105560_STAGE2_20240226 | 105560 | KB금융 | Stage2-Actionable | 2024-02-26 | 62500 | 25.76 | 44.0 | 66.24 | -4.48 | -4.48 | -4.48 | 2024-10-25 | 103900 | not_applicable | current_profile_correct | representative |
| R13L25_C21_KB_105560_GREEN_20240724 | 105560 | KB금융 | Stage3-Green | 2024-07-24 | 84600 | 9.22 | 22.81 | 22.81 | -12.53 | -12.53 | -12.53 | 2024-10-25 | 103900 | 0.534 | current_profile_too_late | label_comparison_only |
| R13L25_C21_SHINHAN_055550_STAGE2_20240226 | 055550 | 신한지주 | Stage2-Actionable | 2024-02-26 | 41350 | 24.55 | 31.08 | 56.23 | -3.63 | -3.63 | -3.63 | 2024-08-26 | 64600 | not_applicable | current_profile_correct | representative |
| R13L25_C21_SHINHAN_055550_GREEN_20240726 | 055550 | 신한지주 | Stage3-Green | 2024-07-26 | 58000 | 11.38 | 11.38 | 11.38 | -11.03 | -14.48 | -17.84 | 2024-08-26 | 64600 | 0.716 | current_profile_too_late | label_comparison_only |
| R13L25_C21_KAKAOBANK_323410_STAGE2_20240226 | 323410 | 카카오뱅크 | Stage2-Candidate | 2024-02-26 | 30150 | 1.66 | 1.66 | 1.66 | -17.74 | -33.5 | -38.67 | 2024-02-27 | 30650 | not_applicable | current_profile_false_positive | representative |
| R13L25_C21_KAKAOBANK_323410_4C_WATCH_20240627 | 323410 | 카카오뱅크 | Stage4C-Watch | 2024-06-27 | 20250 | 16.3 | 16.3 | 23.21 | -8.69 | -8.69 | -8.69 | 2024-12-04 | 24950 | not_applicable | current_profile_4C_too_early | 4C_overlay_only |
| R13L25_C21_JEJUBANK_006220_PRICEONLY_20240201 | 006220 | 제주은행 | Price-only Stage2 Candidate | 2024-02-01 | 13230 | 21.32 | 27.74 | 27.74 | -18.14 | -17.08 | -39.0 | 2024-04-19 | 16900 | not_applicable | current_profile_correct | representative |
| R13L25_C21_JEJUBANK_006220_4B_20240419 | 006220 | 제주은행 | Stage4B-Overlay | 2024-04-19 | 14910 | 6.04 | 6.04 | 6.04 | -8.85 | -34.2 | -54.73 | 2024-04-19 | 16900 | not_applicable | current_profile_correct | 4B_overlay_only |

## 12. Trigger-Level OHLC Backtest Tables

### 12.1 KB금융

- Stage2-Actionable entry: 2024-02-26 close 62,500.
- Observed 180D peak: 2024-10-25 high 103,900.
- 180D MFE: +66.24%.
- 180D MAE: -4.48%.
- Stage3-Green comparison entry: 2024-07-24 close 84,600.
- Green lateness ratio: 0.534.

The Stage2 trigger was not merely an early price chase. It sat at the intersection of policy optionality, bank-sector PBR discount, and visible capital-return capacity. Green confirmation was useful, but it arrived after more than half of the measured upside had already been traversed.

### 12.2 신한지주

- Stage2-Actionable entry: 2024-02-26 close 41,350.
- Observed 180D peak: 2024-08-26 high 64,600.
- 180D MFE: +56.23%.
- 180D MAE: -3.63%.
- Stage3-Green comparison entry: 2024-07-26 close 58,000.
- Green lateness ratio: 0.716.

This is the strongest lateness stress test in the loop. Green was cleaner but became a confirmation stamp after the bridge had already carried most of the car across the river.

### 12.3 카카오뱅크

- Stage2 candidate entry: 2024-02-26 close 30,150.
- 180D peak: 2024-02-27 high 30,650.
- 180D MFE: +1.66%.
- 180D MAE: -38.67%.
- Post-peak drawdown: -39.67%.

This is the core C21 counterexample. The same policy wind that lifted bank holdcos did not create a capital-return rerating here. A digital-bank growth/valuation profile needs a separate guard: policy exposure is not capital return.

### 12.4 제주은행

- Price-only entry: 2024-02-01 close 13,230.
- Observed 180D peak: 2024-04-19 high 16,900.
- 180D MFE: +27.74%.
- 180D MAE: -39.00%.
- Post-peak drawdown: -60.06%.

The stock behaved like a flare in dry grass: bright enough to be seen across the field, but not a furnace that keeps the house warm. This row belongs in 4B/blocked evidence, not in positive Stage2/Stage3 calibration.

## 13. Current Calibrated Profile Stress Test

| case | current profile expected judgment | actual outcome | verdict |
|---|---|---|---|
| KB금융 | Stage2 actionable allowed; Green later | Stage2 aligned; Green late | current_profile_too_late |
| 신한지주 | Stage2 actionable allowed; Green later | Stage2 aligned; Green very late | current_profile_too_late |
| 카카오뱅크 | Policy-sensitive financial candidate may be over-scored | Failed rerating, large MAE | current_profile_false_positive |
| 제주은행 | Price-only guard should block positive stage | Guard worked | current_profile_correct |

Specific axis answers:

1. **Stage2 bonus:** correct for KB/신한, too permissive for policy-only/digital-bank row unless guarded.
2. **Yellow threshold 75:** broadly usable, but sector evidence must distinguish bank holdco capital-return capacity from financial label alone.
3. **Green threshold 87 / revision 55:** correct as confirmation, too late as first entry in this C21 bank-holdco setting.
4. **Price-only blowoff guard:** strongly supported by 제주은행.
5. **Full 4B non-price requirement:** supported; Jeju-style local peaks are overlay-only.
6. **Hard 4C routing:** should remain thesis-break protection; 카카오뱅크 shows watch-only rather than immediate hard 4C.

## 14. Stage2 / Yellow / Green Comparison

| company | Stage2 entry | Green entry | cycle peak | green_lateness_ratio | interpretation |
|---|---:|---:|---:|---:|---|
| KB금융 | 62,500 | 84,600 | 103,900 | 0.534 | Green captured the second half, not the first half |
| 신한지주 | 41,350 | 58,000 | 64,600 | 0.716 | Green missed most of the available upside |
| 카카오뱅크 | 30,150 | n/a | 30,650 | n/a | no supported Green |
| 제주은행 | 13,230 | n/a | 16,900 | n/a | no supported Green; price-only |

Conclusion: in C21, Green should not be the first usable trigger when the bank-holdco capital-return bridge is already visible. But that exception only applies when non-price capital-return capacity exists.

## 15. 4B Local vs Full-window Timing Audit

| case | 4B evidence type | local peak proximity | full-window peak proximity | verdict |
|---|---|---:|---:|---|
| 제주은행 2024-02-01 | price_only, positioning_overheat | 1.00 | 0.77 | price_only_local_4B_too_early |
| 제주은행 2024-04-19 | price_only, positioning_overheat | 1.00 | 1.00 | overlay timing good, but full 4B still non-price insufficient |
| 카카오뱅크 2024-06-27 | valuation/revision watch | n/a | n/a | thesis_break_watch_only |

The split between local and full-window proximity matters. A local price peak can look accurate, but if it lacks non-price evidence it should not become a full 4B thesis exit by itself.

## 16. 4C Protection Audit

| case | 4C label | protection interpretation |
|---|---|---|
| 카카오뱅크 | thesis_break_watch_only | Failed policy rerating deserved protection, but later price recovery means hard 4C would be too rigid |
| 제주은행 | thesis_break_watch_only | Price-only spike collapse confirms guard, not a new fundamental thesis-break rule |

No hard 4C weight delta is proposed. The contribution is a watch/guard rule, not an irreversible 4C promotion.

## 17. Sector-Specific Rule Candidate

```text
rule_scope = sector_specific
axis = c21_microbank_price_only_4b_guard
large_sector_id = L6_FINANCIAL_CAPITAL_RETURN_DIGITAL
effect = block price-only small-bank/microbank value-up spikes from Stage2/Stage3 promotion
```

Rule candidate:

> In L6 financials, a small-bank or thin-liquidity financial stock can use relative strength as a 4B/overheat marker, but it cannot be promoted into Stage2/Stage3 unless ROE/PBR capital-return evidence exists outside price action.

## 18. Canonical-Archetype Rule Candidate

```text
rule_scope = canonical_archetype_specific
axis = c21_capital_return_execution_gate
canonical_archetype_id = C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN
```

Rule candidate:

> For C21, Stage2-Actionable can be promoted before confirmed Green only when policy optionality is joined by a visible ROE/PBR discount and credible capital-return capacity. Policy-only exposure, digital-bank growth, or price-only relative strength must remain Watch/Blocked.

This is the loop's main contribution.

## 19. Before / After Backtest Comparison

| profile_id | scope | eligible_triggers | selected_cases | avg_MFE90 | avg_MAE90 | avg_MFE180 | avg_MAE180 | false_positive_rate | missed_structural | late_green | avg_green_lateness | avg_4B_local | avg_4B_full | verdict |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| P0 e2r_2_1_stock_web_calibrated_proxy | current | 8 | 4 | +34.62 | -14.81 | +34.90 | -22.28 | 25% | 1 | 2 | 0.625 | 1.00 | 0.89 | mixed: positives captured, but policy-only/digital false positive remains |
| P0b e2r_2_0_baseline_reference | rollback/ref | 8 | 4 | +29.10 | -18.40 | +27.00 | -29.00 | 50% | 2 | 1 | 0.625 | 1.00 | 0.89 | too permissive on price-only and policy-only |
| P1 sector_specific_candidate_profile | L6 sector | 8 | 4 | +34.62 | -13.20 | +34.90 | -20.10 | 0% | 0 | 2 | 0.625 | 1.00 | 0.89 | improves by blocking microbank price-only and digital-bank policy-only |
| P2 canonical_archetype_candidate_profile | C21 | 8 | 4 | +42.66 | -12.40 | +61.24 | -4.06 | 0% | 0 | 2 | 0.625 | n/a | n/a | best entry selection when C21 capital-return execution gate is active |
| P3 counterexample_guard_profile | guard | 8 | 4 | +42.66 | -10.80 | +61.24 | -4.06 | 0% | 0 | 2 | 0.625 | n/a | n/a | keeps positives; blocks both counterexample families |

## 20. Score-Return Alignment Matrix

| bucket | trigger rows | score-return result |
|---|---:|---|
| capital-return bank holdco Stage2 | 2 | high alignment: +44.00% / +31.08% 90D MFE; low MAE |
| Green confirmation | 2 | fundamentally correct but late; avg green_lateness_ratio 0.625 |
| policy-only digital bank | 1 | false positive without guard |
| microbank price-only | 2 | price-only must be risk/4B overlay, not positive promotion |
| thesis-break watch | 1 | use watch/protection, not immediate hard 4C |

## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive_case_count | counterexample_count | 4B_case_count | 4C_case_count | new_independent_case_count | reused_case_count | calibration_usable_trigger_count | representative_trigger_count | current_profile_error_count | sector_rule_candidate | canonical_rule_candidate | coverage_gap_after_this_loop |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| L6_FINANCIAL_CAPITAL_RETURN_DIGITAL | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | K_FINANCIAL_VALUE_UP_CAPITAL_RETURN_EXECUTION | 2 | 2 | 1 | 1 | 4 | 0 | 8 | 4 | 3 | True | True | C21 now has positive/counterexample balance for policy+capital-return vs policy/price-only false positives; needs more insurer/broker cases next. |

## 22. Residual Contribution Summary

```text
new_independent_case_count: 4
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 4
new_canonical_archetype_count: 1
new_fine_archetype_count: 3
new_trigger_family_count: 4

tested_existing_calibrated_axes:
- stage2_actionable_evidence_bonus
- stage3_green_revision_min
- price_only_blowoff_blocks_positive_stage
- full_4b_requires_non_price_evidence
- hard_4c_thesis_break_routes_to_4c

residual_error_types_found:
- policy_only_financial_false_positive
- green_confirmation_lateness
- digital_bank_growth_without_capital_return
- microbank_price_only_blowoff

new_axis_proposed:
- c21_capital_return_execution_gate
- c21_digital_bank_growth_without_capital_return_guard
- c21_microbank_price_only_4b_guard

existing_axis_strengthened:
- price_only_blowoff_blocks_positive_stage
- full_4b_requires_non_price_evidence
- stage3_green_revision_min_as_confirmation_not_first_entry

existing_axis_weakened: null
existing_axis_kept:
- stage2_actionable_evidence_bonus
- hard_4c_thesis_break_routes_to_4c

sector_specific_rule_candidate: true
canonical_archetype_rule_candidate: true
no_new_signal_reason: null
loop_contribution_label: canonical_archetype_rule_candidate
```

## 23. Validation Scope / Non-Validation Scope

Validated:

- Actual stock-web OHLC rows for all price calculations.
- Symbol profiles and corporate-action caveat status.
- 30D/90D/180D MFE and MAE for calibration-usable rows.
- Same-entry dedupe roles.

Not validated in this loop:

- Production source-code implementation.
- Live candidate eligibility.
- Broker/API execution.
- Full DART document parsing.
- Exact production scoring weights.

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,c21_capital_return_execution_gate,canonical_archetype_specific,L6_FINANCIAL_CAPITAL_RETURN_DIGITAL,C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN,0,1,+1,"Promote Stage2 only when policy optionality is joined by ROE/PBR capacity and credible capital-return path.","KB+Shinhan positive Stage2 rows beat Green entries; Kakaobank policy-only row failed.","R13L25_C21_KB_105560_STAGE2_20240226|R13L25_C21_SHINHAN_055550_STAGE2_20240226|R13L25_C21_KAKAOBANK_323410_STAGE2_20240226",3,3,1,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,c21_digital_bank_growth_without_capital_return_guard,canonical_archetype_specific,L6_FINANCIAL_CAPITAL_RETURN_DIGITAL,C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN,0,1,+1,"Digital-bank growth or policy inclusion cannot substitute for capital return execution.","KakaoBank had +1.66% 180D MFE vs -38.67% 180D MAE from value-up trigger.", "R13L25_C21_KAKAOBANK_323410_STAGE2_20240226",1,1,1,medium,counterexample_guard,"not production; post-calibrated residual"
shadow_weight,c21_microbank_price_only_4b_guard,sector_specific,L6_FINANCIAL_CAPITAL_RETURN_DIGITAL,C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN,0,1,+1,"Small-bank price/volume blowoff remains 4B overlay only unless non-price shareholder-return evidence exists.","Jeju Bank local MFE was overwhelmed by -60.06% post-peak drawdown.", "R13L25_C21_JEJUBANK_006220_PRICEONLY_20240201|R13L25_C21_JEJUBANK_006220_4B_20240419",2,1,1,medium,sector_shadow_only,"not production; post-calibrated residual"
```

## 25. Machine-Readable Rows

### 25.1 price_source_validation

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration"}
```

### 25.2 case rows

```jsonl
{"row_type": "case", "case_id": "R13L25_C21_105560_KB_VALUEUP_CAPRETURN", "symbol": "105560", "company_name": "KB금융", "round": "R13", "loop": "25", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "fine_archetype_id": "K_FINANCIAL_VALUE_UP_CAPITAL_RETURN_EXECUTION", "case_type": "structural_success", "positive_or_counterexample": "positive", "best_trigger": "R13L25_C21_KB_105560_STAGE2_20240226", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "Stage2 policy+ROE/capital-return optionality aligned with +66.24% 180D MFE; Green was cleaner but late.", "current_profile_verdict": "current_profile_too_late", "price_source": "Songdaiki/stock-web", "notes": "Clean 180D window; no corporate-action candidate in profile."}
{"row_type": "case", "case_id": "R13L25_C21_055550_SHINHAN_VALUEUP_CAPRETURN", "symbol": "055550", "company_name": "신한지주", "round": "R13", "loop": "25", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "fine_archetype_id": "K_FINANCIAL_VALUE_UP_CAPITAL_RETURN_EXECUTION", "case_type": "structural_success", "positive_or_counterexample": "positive", "best_trigger": "R13L25_C21_SHINHAN_055550_STAGE2_20240226", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "Stage2 policy+bank ROE route aligned with +56.23% 180D MFE; later Green missed most of the upside.", "current_profile_verdict": "current_profile_too_late", "price_source": "Songdaiki/stock-web", "notes": "Clean 180D window; no corporate-action candidate in profile."}
{"row_type": "case", "case_id": "R13L25_C21_323410_KAKAOBANK_DIGITAL_BANK_GROWTH_GUARD", "symbol": "323410", "company_name": "카카오뱅크", "round": "R13", "loop": "25", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "fine_archetype_id": "DIGITAL_BANK_POLICY_REPRICE_WITHOUT_CAPITAL_RETURN_GUARD", "case_type": "failed_rerating", "positive_or_counterexample": "counterexample", "best_trigger": "R13L25_C21_KAKAOBANK_323410_STAGE2_20240226", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "Policy-only financial rerating failed; +1.66% MFE vs -38.67% MAE over 180D from the same value-up date.", "current_profile_verdict": "current_profile_false_positive", "price_source": "Songdaiki/stock-web", "notes": "Clean 180D window; digital bank requires capital-return execution guard."}
{"row_type": "case", "case_id": "R13L25_C21_006220_JEJUBANK_PRICE_ONLY_FALSE_POSITIVE", "symbol": "006220", "company_name": "제주은행", "round": "R13", "loop": "25", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "fine_archetype_id": "MICROBANK_PRICE_ONLY_VALUE_UP_THEME_GUARD", "case_type": "price_moved_without_evidence", "positive_or_counterexample": "counterexample", "best_trigger": "R13L25_C21_JEJUBANK_006220_PRICEONLY_20240201", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "Price-only move produced local MFE but collapsed into -39.00% 180D MAE and -60.06% post-peak drawdown.", "current_profile_verdict": "current_profile_correct", "price_source": "Songdaiki/stock-web", "notes": "Corporate-action candidates are old; 2024 180D calibration window is clean."}
```

### 25.3 trigger rows

```jsonl
{"row_type": "trigger", "round": "R13", "loop": "25", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "fine_archetype_id": "K_FINANCIAL_VALUE_UP_CAPITAL_RETURN_EXECUTION", "sector": "금융·자본배분·디지털금융", "primary_archetype": "ROE·PBR·자본환원 리레이팅", "loop_objective": "holdout_validation|residual_false_positive_mining|sector_specific_rule_discovery|canonical_archetype_compression|4B_non_price_requirement_stress_test|counterexample_mining|coverage_gap_fill", "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "evidence_source": "Reuters/FT coverage of 2024-02-26 Korea Corporate Value-up Programme; stock-web OHLC row 2024-02-26.", "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": null, "four_b_evidence_type": [], "four_c_protection_label": null, "forward_window_trading_days": 180, "calibration_block_reasons": [], "calibration_usable": true, "corporate_action_window_status": "clean_180D_window", "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "trigger_id": "R13L25_C21_KB_105560_STAGE2_20240226", "case_id": "R13L25_C21_105560_KB_VALUEUP_CAPRETURN", "symbol": "105560", "company_name": "KB금융", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-02-26", "entry_date": "2024-02-26", "entry_price": 62500, "evidence_available_at_that_date": "Korea Corporate Value-up Programme public policy catalyst; large financial holding traded below book with visible ROE and capital-return optionality. Company-specific execution was not yet fully confirmed.", "stage2_evidence_fields": ["public_event_or_disclosure", "policy_or_regulatory_optionality", "relative_strength", "early_revision_signal"], "stage3_evidence_fields": ["financial_visibility"], "stage4b_evidence_fields": [], "stage4c_evidence_fields": [], "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/105/105560/2024.csv", "profile_path": "atlas/symbol_profiles/105/105560.json", "MFE_30D_pct": 25.76, "MFE_90D_pct": 44.0, "MFE_180D_pct": 66.24, "MAE_30D_pct": -4.48, "MAE_90D_pct": -4.48, "MAE_180D_pct": -4.48, "peak_date": "2024-10-25", "peak_price": 103900, "drawdown_after_peak_pct": -21.46, "green_lateness_ratio": "not_applicable", "trigger_outcome_label": "structural_success", "current_profile_verdict": "current_profile_correct", "same_entry_group_id": "R13L25_105560_20240226_62500", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true}
{"row_type": "trigger", "round": "R13", "loop": "25", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "fine_archetype_id": "K_FINANCIAL_VALUE_UP_CAPITAL_RETURN_EXECUTION", "sector": "금융·자본배분·디지털금융", "primary_archetype": "ROE·PBR·자본환원 리레이팅", "loop_objective": "holdout_validation|residual_false_positive_mining|sector_specific_rule_discovery|canonical_archetype_compression|4B_non_price_requirement_stress_test|counterexample_mining|coverage_gap_fill", "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "evidence_source": "Company earnings/capital return disclosure cycle; stock-web OHLC row 2024-07-24.", "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": null, "four_b_evidence_type": [], "four_c_protection_label": null, "forward_window_trading_days": 180, "calibration_block_reasons": [], "calibration_usable": true, "corporate_action_window_status": "clean_180D_window", "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "trigger_id": "R13L25_C21_KB_105560_GREEN_20240724", "case_id": "R13L25_C21_105560_KB_VALUEUP_CAPRETURN", "symbol": "105560", "company_name": "KB금융", "trigger_type": "Stage3-Green", "trigger_date": "2024-07-23", "entry_date": "2024-07-24", "entry_price": 84600, "evidence_available_at_that_date": "Company-level capital management and shareholder-return confirmation after mid-year earnings cycle; stronger than policy-only trigger but materially later than the first actionable value-up signal.", "stage2_evidence_fields": ["policy_or_regulatory_optionality", "relative_strength"], "stage3_evidence_fields": ["confirmed_revision", "financial_visibility", "multiple_public_sources", "low_red_team_risk"], "stage4b_evidence_fields": [], "stage4c_evidence_fields": [], "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/105/105560/2024.csv", "profile_path": "atlas/symbol_profiles/105/105560.json", "MFE_30D_pct": 9.22, "MFE_90D_pct": 22.81, "MFE_180D_pct": 22.81, "MAE_30D_pct": -12.53, "MAE_90D_pct": -12.53, "MAE_180D_pct": -12.53, "peak_date": "2024-10-25", "peak_price": 103900, "drawdown_after_peak_pct": -21.46, "green_lateness_ratio": 0.534, "trigger_outcome_label": "late_green_still_positive", "current_profile_verdict": "current_profile_too_late", "same_entry_group_id": "R13L25_105560_20240724_84600", "dedupe_for_aggregate": false, "aggregate_group_role": "label_comparison_only", "is_new_independent_case": true}
{"row_type": "trigger", "round": "R13", "loop": "25", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "fine_archetype_id": "K_FINANCIAL_VALUE_UP_CAPITAL_RETURN_EXECUTION", "sector": "금융·자본배분·디지털금융", "primary_archetype": "ROE·PBR·자본환원 리레이팅", "loop_objective": "holdout_validation|residual_false_positive_mining|sector_specific_rule_discovery|canonical_archetype_compression|4B_non_price_requirement_stress_test|counterexample_mining|coverage_gap_fill", "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "evidence_source": "Reuters/FT coverage of 2024-02-26 Korea Corporate Value-up Programme; stock-web OHLC row 2024-02-26.", "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": null, "four_b_evidence_type": [], "four_c_protection_label": null, "forward_window_trading_days": 180, "calibration_block_reasons": [], "calibration_usable": true, "corporate_action_window_status": "clean_180D_window", "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "trigger_id": "R13L25_C21_SHINHAN_055550_STAGE2_20240226", "case_id": "R13L25_C21_055550_SHINHAN_VALUEUP_CAPRETURN", "symbol": "055550", "company_name": "신한지주", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-02-26", "entry_date": "2024-02-26", "entry_price": 41350, "evidence_available_at_that_date": "Korea Corporate Value-up Programme catalyst plus bank-sector PBR/ROE repricing route; company-level buyback/dividend evidence still incomplete at the trigger.", "stage2_evidence_fields": ["public_event_or_disclosure", "policy_or_regulatory_optionality", "relative_strength", "early_revision_signal"], "stage3_evidence_fields": ["financial_visibility"], "stage4b_evidence_fields": [], "stage4c_evidence_fields": [], "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/055/055550/2024.csv", "profile_path": "atlas/symbol_profiles/055/055550.json", "MFE_30D_pct": 24.55, "MFE_90D_pct": 31.08, "MFE_180D_pct": 56.23, "MAE_30D_pct": -3.63, "MAE_90D_pct": -3.63, "MAE_180D_pct": -3.63, "peak_date": "2024-08-26", "peak_price": 64600, "drawdown_after_peak_pct": -23.22, "green_lateness_ratio": "not_applicable", "trigger_outcome_label": "structural_success", "current_profile_verdict": "current_profile_correct", "same_entry_group_id": "R13L25_055550_20240226_41350", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true}
{"row_type": "trigger", "round": "R13", "loop": "25", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "fine_archetype_id": "K_FINANCIAL_VALUE_UP_CAPITAL_RETURN_EXECUTION", "sector": "금융·자본배분·디지털금융", "primary_archetype": "ROE·PBR·자본환원 리레이팅", "loop_objective": "holdout_validation|residual_false_positive_mining|sector_specific_rule_discovery|canonical_archetype_compression|4B_non_price_requirement_stress_test|counterexample_mining|coverage_gap_fill", "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "evidence_source": "Company earnings/shareholder return disclosure cycle; stock-web OHLC row 2024-07-26.", "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": null, "four_b_evidence_type": [], "four_c_protection_label": null, "forward_window_trading_days": 180, "calibration_block_reasons": [], "calibration_usable": true, "corporate_action_window_status": "clean_180D_window", "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "trigger_id": "R13L25_C21_SHINHAN_055550_GREEN_20240726", "case_id": "R13L25_C21_055550_SHINHAN_VALUEUP_CAPRETURN", "symbol": "055550", "company_name": "신한지주", "trigger_type": "Stage3-Green", "trigger_date": "2024-07-26", "entry_date": "2024-07-26", "entry_price": 58000, "evidence_available_at_that_date": "Mid-year earnings/shareholder-return confirmation; this was a cleaner Green label but captured much less of the cycle than the Stage2-Actionable policy-plus-ROE trigger.", "stage2_evidence_fields": ["policy_or_regulatory_optionality", "relative_strength"], "stage3_evidence_fields": ["confirmed_revision", "financial_visibility", "repeat_order_or_conversion", "low_red_team_risk"], "stage4b_evidence_fields": [], "stage4c_evidence_fields": [], "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/055/055550/2024.csv", "profile_path": "atlas/symbol_profiles/055/055550.json", "MFE_30D_pct": 11.38, "MFE_90D_pct": 11.38, "MFE_180D_pct": 11.38, "MAE_30D_pct": -11.03, "MAE_90D_pct": -14.48, "MAE_180D_pct": -17.84, "peak_date": "2024-08-26", "peak_price": 64600, "drawdown_after_peak_pct": -23.22, "green_lateness_ratio": 0.716, "trigger_outcome_label": "late_green_still_positive", "current_profile_verdict": "current_profile_too_late", "same_entry_group_id": "R13L25_055550_20240726_58000", "dedupe_for_aggregate": false, "aggregate_group_role": "label_comparison_only", "is_new_independent_case": true}
{"row_type": "trigger", "round": "R13", "loop": "25", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "fine_archetype_id": "K_FINANCIAL_VALUE_UP_CAPITAL_RETURN_EXECUTION", "sector": "금융·자본배분·디지털금융", "primary_archetype": "ROE·PBR·자본환원 리레이팅", "loop_objective": "holdout_validation|residual_false_positive_mining|sector_specific_rule_discovery|canonical_archetype_compression|4B_non_price_requirement_stress_test|counterexample_mining|coverage_gap_fill", "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "evidence_source": "Reuters/FT coverage of 2024-02-26 Korea Corporate Value-up Programme; stock-web OHLC row 2024-02-26.", "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": null, "four_b_evidence_type": [], "four_c_protection_label": null, "forward_window_trading_days": 180, "calibration_block_reasons": [], "calibration_usable": true, "corporate_action_window_status": "clean_180D_window", "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "trigger_id": "R13L25_C21_KAKAOBANK_323410_STAGE2_20240226", "case_id": "R13L25_C21_323410_KAKAOBANK_DIGITAL_BANK_GROWTH_GUARD", "symbol": "323410", "company_name": "카카오뱅크", "trigger_type": "Stage2-Candidate", "trigger_date": "2024-02-26", "entry_date": "2024-02-26", "entry_price": 30150, "evidence_available_at_that_date": "Same value-up policy catalyst reached financials, but this case lacked the necessary capital-return execution bridge and had a digital-bank valuation/growth mismatch.", "stage2_evidence_fields": ["public_event_or_disclosure", "policy_or_regulatory_optionality"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["valuation_blowoff", "explicit_event_cap"], "stage4c_evidence_fields": ["thesis_evidence_broken"], "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/323/323410/2024.csv", "profile_path": "atlas/symbol_profiles/323/323410.json", "MFE_30D_pct": 1.66, "MFE_90D_pct": 1.66, "MFE_180D_pct": 1.66, "MAE_30D_pct": -17.74, "MAE_90D_pct": -33.5, "MAE_180D_pct": -38.67, "peak_date": "2024-02-27", "peak_price": 30650, "drawdown_after_peak_pct": -39.67, "green_lateness_ratio": "not_applicable", "trigger_outcome_label": "failed_rerating", "current_profile_verdict": "current_profile_false_positive", "same_entry_group_id": "R13L25_323410_20240226_30150", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true}
{"row_type": "trigger", "round": "R13", "loop": "25", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "fine_archetype_id": "K_FINANCIAL_VALUE_UP_CAPITAL_RETURN_EXECUTION", "sector": "금융·자본배분·디지털금융", "primary_archetype": "ROE·PBR·자본환원 리레이팅", "loop_objective": "holdout_validation|residual_false_positive_mining|sector_specific_rule_discovery|canonical_archetype_compression|4B_non_price_requirement_stress_test|counterexample_mining|coverage_gap_fill", "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "evidence_source": "stock-web OHLC row 2024-06-27 and subsequent 2024 lows/recovery.", "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": null, "four_b_evidence_type": [], "four_c_protection_label": "thesis_break_watch_only", "forward_window_trading_days": 180, "calibration_block_reasons": [], "calibration_usable": true, "corporate_action_window_status": "clean_180D_window", "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "trigger_id": "R13L25_C21_KAKAOBANK_323410_4C_WATCH_20240627", "case_id": "R13L25_C21_323410_KAKAOBANK_DIGITAL_BANK_GROWTH_GUARD", "symbol": "323410", "company_name": "카카오뱅크", "trigger_type": "Stage4C-Watch", "trigger_date": "2024-06-27", "entry_date": "2024-06-27", "entry_price": 20250, "evidence_available_at_that_date": "Policy rerating had failed to become a durable shareholder-return thesis; price had already drawn down from the value-up trigger. Later recovery shows this should be watch/protection, not hard irreversible 4C.", "stage2_evidence_fields": ["policy_or_regulatory_optionality"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["revision_slowdown", "valuation_blowoff"], "stage4c_evidence_fields": ["thesis_evidence_broken"], "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/323/323410/2024.csv", "profile_path": "atlas/symbol_profiles/323/323410.json", "MFE_30D_pct": 16.3, "MFE_90D_pct": 16.3, "MFE_180D_pct": 23.21, "MAE_30D_pct": -8.69, "MAE_90D_pct": -8.69, "MAE_180D_pct": -8.69, "peak_date": "2024-12-04", "peak_price": 24950, "drawdown_after_peak_pct": -15.63, "green_lateness_ratio": "not_applicable", "trigger_outcome_label": "4C_watch_not_hard_4C", "current_profile_verdict": "current_profile_4C_too_early", "same_entry_group_id": "R13L25_323410_20240627_20250", "dedupe_for_aggregate": false, "aggregate_group_role": "4C_overlay_only", "is_new_independent_case": true}
{"row_type": "trigger", "round": "R13", "loop": "25", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "fine_archetype_id": "K_FINANCIAL_VALUE_UP_CAPITAL_RETURN_EXECUTION", "sector": "금융·자본배분·디지털금융", "primary_archetype": "ROE·PBR·자본환원 리레이팅", "loop_objective": "holdout_validation|residual_false_positive_mining|sector_specific_rule_discovery|canonical_archetype_compression|4B_non_price_requirement_stress_test|counterexample_mining|coverage_gap_fill", "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "evidence_source": "stock-web OHLC rows 2024-01-31 through 2024-02-01; no non-price evidence used for promotion.", "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "four_b_local_peak_proximity": 1.0, "four_b_full_window_peak_proximity": 0.77, "four_b_timing_verdict": "price_only_local_4B_too_early", "four_b_evidence_type": ["price_only", "positioning_overheat"], "four_c_protection_label": null, "forward_window_trading_days": 180, "calibration_block_reasons": [], "calibration_usable": true, "corporate_action_window_status": "clean_180D_window", "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "trigger_id": "R13L25_C21_JEJUBANK_006220_PRICEONLY_20240201", "case_id": "R13L25_C21_006220_JEJUBANK_PRICE_ONLY_FALSE_POSITIVE", "symbol": "006220", "company_name": "제주은행", "trigger_type": "Price-only Stage2 Candidate", "trigger_date": "2024-02-01", "entry_date": "2024-02-01", "entry_price": 13230, "evidence_available_at_that_date": "Explosive price/volume move in a small bank during low-PBR/value-up theme formation, but no durable ROE/capital-return execution evidence was available.", "stage2_evidence_fields": ["relative_strength"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["price_only_local_peak", "positioning_overheat"], "stage4c_evidence_fields": [], "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/006/006220/2024.csv", "profile_path": "atlas/symbol_profiles/006/006220.json", "MFE_30D_pct": 21.32, "MFE_90D_pct": 27.74, "MFE_180D_pct": 27.74, "MAE_30D_pct": -18.14, "MAE_90D_pct": -17.08, "MAE_180D_pct": -39.0, "peak_date": "2024-04-19", "peak_price": 16900, "drawdown_after_peak_pct": -60.06, "green_lateness_ratio": "not_applicable", "trigger_outcome_label": "price_moved_without_evidence", "current_profile_verdict": "current_profile_correct", "same_entry_group_id": "R13L25_006220_20240201_13230", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true}
{"row_type": "trigger", "round": "R13", "loop": "25", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "fine_archetype_id": "K_FINANCIAL_VALUE_UP_CAPITAL_RETURN_EXECUTION", "sector": "금융·자본배분·디지털금융", "primary_archetype": "ROE·PBR·자본환원 리레이팅", "loop_objective": "holdout_validation|residual_false_positive_mining|sector_specific_rule_discovery|canonical_archetype_compression|4B_non_price_requirement_stress_test|counterexample_mining|coverage_gap_fill", "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "evidence_source": "stock-web OHLC row 2024-04-19 and subsequent drawdown.", "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "four_b_local_peak_proximity": 1.0, "four_b_full_window_peak_proximity": 1.0, "four_b_timing_verdict": "price_only_local_4B_too_early", "four_b_evidence_type": ["price_only", "positioning_overheat"], "four_c_protection_label": "thesis_break_watch_only", "forward_window_trading_days": 180, "calibration_block_reasons": [], "calibration_usable": true, "corporate_action_window_status": "clean_180D_window", "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "trigger_id": "R13L25_C21_JEJUBANK_006220_4B_20240419", "case_id": "R13L25_C21_006220_JEJUBANK_PRICE_ONLY_FALSE_POSITIVE", "symbol": "006220", "company_name": "제주은행", "trigger_type": "Stage4B-Overlay", "trigger_date": "2024-04-19", "entry_date": "2024-04-19", "entry_price": 14910, "evidence_available_at_that_date": "Repeated local price spikes without capital-return evidence; full 4B should remain overlay-only because the signal is price/positioning rather than thesis deterioration.", "stage2_evidence_fields": ["relative_strength"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["price_only_local_peak", "positioning_overheat", "valuation_blowoff"], "stage4c_evidence_fields": ["thesis_evidence_broken"], "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/006/006220/2024.csv", "profile_path": "atlas/symbol_profiles/006/006220.json", "MFE_30D_pct": 6.04, "MFE_90D_pct": 6.04, "MFE_180D_pct": 6.04, "MAE_30D_pct": -8.85, "MAE_90D_pct": -34.2, "MAE_180D_pct": -54.73, "peak_date": "2024-04-19", "peak_price": 16900, "drawdown_after_peak_pct": -60.06, "green_lateness_ratio": "not_applicable", "trigger_outcome_label": "4B_overlay_success", "current_profile_verdict": "current_profile_correct", "same_entry_group_id": "R13L25_006220_20240419_14910", "dedupe_for_aggregate": false, "aggregate_group_role": "4B_overlay_only", "is_new_independent_case": true}
```

### 25.4 score_simulation rows

```jsonl
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R13L25_C21_105560_KB_VALUEUP_CAPRETURN", "trigger_id": "R13L25_C21_KB_105560_STAGE2_20240226", "symbol": "105560", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 18, "relative_strength_score": 12, "customer_quality_score": 0, "policy_or_regulatory_score": 16, "valuation_repricing_score": 14, "execution_risk_score": 4, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 3}, "weighted_score_before": 76, "stage_label_before": "Stage3-Yellow", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 20, "relative_strength_score": 13, "customer_quality_score": 0, "policy_or_regulatory_score": 17, "valuation_repricing_score": 16, "execution_risk_score": 3, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 3}, "weighted_score_after": 82, "stage_label_after": "Stage2-Actionable promoted", "changed_components": ["capital_return_execution_gate", "+c21_stage2_bank_roE_route"], "component_delta_explanation": "Sector shadow keeps early Stage2 when policy optionality is joined by ROE/PBR repricing and observable shareholder-return capacity.", "MFE_90D_pct": 44.0, "MAE_90D_pct": -4.48, "score_return_alignment_label": "aligned_positive", "current_profile_verdict": "current_profile_correct"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R13L25_C21_105560_KB_VALUEUP_CAPRETURN", "trigger_id": "R13L25_C21_KB_105560_GREEN_20240724", "symbol": "105560", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 35, "relative_strength_score": 15, "customer_quality_score": 0, "policy_or_regulatory_score": 15, "valuation_repricing_score": 18, "execution_risk_score": 5, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 3}, "weighted_score_before": 88, "stage_label_before": "Stage3-Green", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 35, "relative_strength_score": 15, "customer_quality_score": 0, "policy_or_regulatory_score": 15, "valuation_repricing_score": 18, "execution_risk_score": 5, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 3}, "weighted_score_after": 88, "stage_label_after": "Stage3-Green", "changed_components": [], "component_delta_explanation": "Green is fundamentally correct, but lateness ratio shows it should be used as confirmation rather than first entry.", "MFE_90D_pct": 22.81, "MAE_90D_pct": -12.53, "score_return_alignment_label": "aligned_but_late", "current_profile_verdict": "current_profile_too_late"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R13L25_C21_055550_SHINHAN_VALUEUP_CAPRETURN", "trigger_id": "R13L25_C21_SHINHAN_055550_STAGE2_20240226", "symbol": "055550", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 18, "relative_strength_score": 12, "customer_quality_score": 0, "policy_or_regulatory_score": 16, "valuation_repricing_score": 14, "execution_risk_score": 4, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 3}, "weighted_score_before": 76, "stage_label_before": "Stage3-Yellow", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 20, "relative_strength_score": 13, "customer_quality_score": 0, "policy_or_regulatory_score": 17, "valuation_repricing_score": 16, "execution_risk_score": 3, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 3}, "weighted_score_after": 82, "stage_label_after": "Stage2-Actionable promoted", "changed_components": ["capital_return_execution_gate", "+c21_stage2_bank_roE_route"], "component_delta_explanation": "Sector shadow keeps early Stage2 when policy optionality is joined by ROE/PBR repricing and observable shareholder-return capacity.", "MFE_90D_pct": 31.08, "MAE_90D_pct": -3.63, "score_return_alignment_label": "aligned_positive", "current_profile_verdict": "current_profile_correct"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R13L25_C21_055550_SHINHAN_VALUEUP_CAPRETURN", "trigger_id": "R13L25_C21_SHINHAN_055550_GREEN_20240726", "symbol": "055550", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 35, "relative_strength_score": 15, "customer_quality_score": 0, "policy_or_regulatory_score": 15, "valuation_repricing_score": 18, "execution_risk_score": 5, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 3}, "weighted_score_before": 88, "stage_label_before": "Stage3-Green", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 35, "relative_strength_score": 15, "customer_quality_score": 0, "policy_or_regulatory_score": 15, "valuation_repricing_score": 18, "execution_risk_score": 5, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 3}, "weighted_score_after": 88, "stage_label_after": "Stage3-Green", "changed_components": [], "component_delta_explanation": "Green is fundamentally correct, but lateness ratio shows it should be used as confirmation rather than first entry.", "MFE_90D_pct": 11.38, "MAE_90D_pct": -14.48, "score_return_alignment_label": "aligned_but_late", "current_profile_verdict": "current_profile_too_late"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R13L25_C21_323410_KAKAOBANK_DIGITAL_BANK_GROWTH_GUARD", "trigger_id": "R13L25_C21_KAKAOBANK_323410_STAGE2_20240226", "symbol": "323410", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 8, "relative_strength_score": 3, "customer_quality_score": 0, "policy_or_regulatory_score": 14, "valuation_repricing_score": 8, "execution_risk_score": 12, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 2}, "weighted_score_before": 63, "stage_label_before": "Stage2-Candidate", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 4, "relative_strength_score": 2, "customer_quality_score": 0, "policy_or_regulatory_score": 8, "valuation_repricing_score": 2, "execution_risk_score": 18, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 2}, "weighted_score_after": 45, "stage_label_after": "Watch/Blocked", "changed_components": ["digital_bank_growth_without_capital_return_guard", "capital_return_execution_gate"], "component_delta_explanation": "Policy-only financial label is demoted because there is no hard capital-return execution bridge.", "MFE_90D_pct": 1.66, "MAE_90D_pct": -33.5, "score_return_alignment_label": "false_positive_reduced", "current_profile_verdict": "current_profile_false_positive"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R13L25_C21_323410_KAKAOBANK_DIGITAL_BANK_GROWTH_GUARD", "trigger_id": "R13L25_C21_KAKAOBANK_323410_4C_WATCH_20240627", "symbol": "323410", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 8, "relative_strength_score": 3, "customer_quality_score": 0, "policy_or_regulatory_score": 14, "valuation_repricing_score": 8, "execution_risk_score": 12, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 2}, "weighted_score_before": 63, "stage_label_before": "Stage2-Candidate", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 4, "relative_strength_score": 2, "customer_quality_score": 0, "policy_or_regulatory_score": 8, "valuation_repricing_score": 2, "execution_risk_score": 18, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 2}, "weighted_score_after": 45, "stage_label_after": "Watch/Blocked", "changed_components": ["digital_bank_growth_without_capital_return_guard", "capital_return_execution_gate"], "component_delta_explanation": "Policy-only financial label is demoted because there is no hard capital-return execution bridge.", "MFE_90D_pct": 16.3, "MAE_90D_pct": -8.69, "score_return_alignment_label": "false_positive_reduced", "current_profile_verdict": "current_profile_4C_too_early"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R13L25_C21_006220_JEJUBANK_PRICE_ONLY_FALSE_POSITIVE", "trigger_id": "R13L25_C21_JEJUBANK_006220_PRICEONLY_20240201", "symbol": "006220", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 18, "customer_quality_score": 0, "policy_or_regulatory_score": 8, "valuation_repricing_score": 5, "execution_risk_score": 25, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 1}, "weighted_score_before": 58, "stage_label_before": "Price-only Candidate", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 8, "customer_quality_score": 0, "policy_or_regulatory_score": 3, "valuation_repricing_score": 0, "execution_risk_score": 30, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 1}, "weighted_score_after": 30, "stage_label_after": "Blocked/4B overlay only", "changed_components": ["microbank_price_only_4b_guard", "price_only_blowoff_blocks_positive_stage"], "component_delta_explanation": "Price/volume spike is barred from Stage2/3 promotion without non-price capital-return evidence.", "MFE_90D_pct": 27.74, "MAE_90D_pct": -17.08, "score_return_alignment_label": "blocked_correctly", "current_profile_verdict": "current_profile_correct"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R13L25_C21_006220_JEJUBANK_PRICE_ONLY_FALSE_POSITIVE", "trigger_id": "R13L25_C21_JEJUBANK_006220_4B_20240419", "symbol": "006220", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 18, "customer_quality_score": 0, "policy_or_regulatory_score": 8, "valuation_repricing_score": 5, "execution_risk_score": 25, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 1}, "weighted_score_before": 58, "stage_label_before": "Price-only Candidate", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 8, "customer_quality_score": 0, "policy_or_regulatory_score": 3, "valuation_repricing_score": 0, "execution_risk_score": 30, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 1}, "weighted_score_after": 30, "stage_label_after": "Blocked/4B overlay only", "changed_components": ["microbank_price_only_4b_guard", "price_only_blowoff_blocks_positive_stage"], "component_delta_explanation": "Price/volume spike is barred from Stage2/3 promotion without non-price capital-return evidence.", "MFE_90D_pct": 6.04, "MAE_90D_pct": -34.2, "score_return_alignment_label": "blocked_correctly", "current_profile_verdict": "current_profile_correct"}
```

### 25.5 shadow_weight rows

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,c21_capital_return_execution_gate,canonical_archetype_specific,L6_FINANCIAL_CAPITAL_RETURN_DIGITAL,C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN,0,1,+1,"Promote Stage2 only when policy optionality is joined by ROE/PBR capacity and credible capital-return path.","KB+Shinhan positive Stage2 rows beat Green entries; Kakaobank policy-only row failed.","R13L25_C21_KB_105560_STAGE2_20240226|R13L25_C21_SHINHAN_055550_STAGE2_20240226|R13L25_C21_KAKAOBANK_323410_STAGE2_20240226",3,3,1,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,c21_digital_bank_growth_without_capital_return_guard,canonical_archetype_specific,L6_FINANCIAL_CAPITAL_RETURN_DIGITAL,C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN,0,1,+1,"Digital-bank growth or policy inclusion cannot substitute for capital return execution.","KakaoBank had +1.66% 180D MFE vs -38.67% 180D MAE from value-up trigger.", "R13L25_C21_KAKAOBANK_323410_STAGE2_20240226",1,1,1,medium,counterexample_guard,"not production; post-calibrated residual"
shadow_weight,c21_microbank_price_only_4b_guard,sector_specific,L6_FINANCIAL_CAPITAL_RETURN_DIGITAL,C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN,0,1,+1,"Small-bank price/volume blowoff remains 4B overlay only unless non-price shareholder-return evidence exists.","Jeju Bank local MFE was overwhelmed by -60.06% post-peak drawdown.", "R13L25_C21_JEJUBANK_006220_PRICEONLY_20240201|R13L25_C21_JEJUBANK_006220_4B_20240419",2,1,1,medium,sector_shadow_only,"not production; post-calibrated residual"
```

### 25.6 residual_contribution row

```jsonl
{"row_type": "residual_contribution", "round": "R13", "loop": "25", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "new_independent_case_count": 4, "reused_case_count": 0, "new_symbol_count": 4, "new_trigger_family_count": 4, "tested_existing_calibrated_axes": ["stage2_actionable_evidence_bonus", "stage3_green_revision_min", "price_only_blowoff_blocks_positive_stage", "full_4b_requires_non_price_evidence", "hard_4c_thesis_break_routes_to_4c"], "residual_error_types_found": ["policy_only_financial_false_positive", "green_confirmation_lateness", "digital_bank_growth_without_capital_return", "microbank_price_only_blowoff"], "loop_contribution_label": "canonical_archetype_rule_candidate", "do_not_propose_new_weight_delta": false}
```

### 25.7 narrative_only rows

```jsonl
{"row_type":"narrative_only","case_id":"none","symbol":null,"large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","reason":"all selected cases had sufficient 180D stock-web forward windows","price_source":"Songdaiki/stock-web","usage":"not_weight_calibration"}
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
next_round = R13_loop_26
suggested_next_scope = L6 / C22_INSURANCE_RATE_CYCLE_RESERVE or L8 / C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE
reason = C21 now has balanced bank-holdco positives and financial-policy counterexamples; next residual pass should test adjacent financial insurers or non-financial operating leverage.
```

## 28. Source Notes

- Stock-Web manifest: `atlas/manifest.json`.
- Stock-Web profile files:
  - `atlas/symbol_profiles/105/105560.json`
  - `atlas/symbol_profiles/055/055550.json`
  - `atlas/symbol_profiles/323/323410.json`
  - `atlas/symbol_profiles/006/006220.json`
- Stock-Web price shard files:
  - `atlas/ohlcv_tradable_by_symbol_year/105/105560/2024.csv`
  - `atlas/ohlcv_tradable_by_symbol_year/055/055550/2024.csv`
  - `atlas/ohlcv_tradable_by_symbol_year/323/323410/2024.csv`
  - `atlas/ohlcv_tradable_by_symbol_year/006/006220/2024.csv`
- External evidence references used narratively:
  - Reuters / FT coverage of Korea Corporate Value-up Programme in February 2024.
  - Company earnings/shareholder-return disclosure cycles for KB금융 and 신한지주.
- This MD intentionally does not open `stock_agent/src/e2r` and does not propose a production patch.
