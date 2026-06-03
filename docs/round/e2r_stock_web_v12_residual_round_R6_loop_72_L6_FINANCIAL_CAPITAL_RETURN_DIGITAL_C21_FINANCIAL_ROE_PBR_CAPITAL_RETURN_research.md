# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```yaml
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
scheduled_round: R6
scheduled_loop: 72
completed_round: R6
completed_loop: 72
large_sector_id: L6_FINANCIAL_CAPITAL_RETURN_DIGITAL
canonical_archetype_id: C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN
fine_archetype_id: BANK_HOLDCO_VALUEUP_CET1_CAPITAL_RETURN__VS__CAPITAL_RETURN_ABSENT_PLATFORM_LOW_FLOAT_PRICE_ONLY
output_file: e2r_stock_web_v12_residual_round_R6_loop_72_L6_FINANCIAL_CAPITAL_RETURN_DIGITAL_C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN_research.md
production_scoring_changed: false
shadow_weight_only: true
stock_agent_code_access_allowed: false
stock_web_price_atlas_access_required: true
```

This loop adds **4** new independent cases, **2** counterexamples, and **3** residual errors for `R6/L6_FINANCIAL_CAPITAL_RETURN_DIGITAL/C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN`.

## 1. Current Calibrated Profile Assumption

Current proxy profile: `e2r_2_1_stock_web_calibrated_proxy`.

Already-applied global axes are treated as active and are not re-proposed globally:

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

This R6 loop stress-tests whether C21 financial rerating requires a more specific bridge: **formal capital-return policy + CET1/ROE visibility + PBR repair**, rather than generic financial-sector relative strength.

## 2. Round / Large Sector / Canonical Archetype Scope

| Field | Value |
|---|---|
| scheduled_round | R6 |
| scheduled_loop | 72 |
| round_schedule_status | valid |
| large_sector_id | L6_FINANCIAL_CAPITAL_RETURN_DIGITAL |
| round_sector_consistency | pass |
| canonical_archetype_id | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN |
| fine_archetype_id | BANK_HOLDCO_VALUEUP_CET1_CAPITAL_RETURN vs PLATFORM/LOW_FLOAT_FALSE_POSITIVE |
| loop_objective | sector_specific_rule_discovery, canonical_archetype_compression, counterexample_mining, coverage_gap_fill, 4B_non_price_requirement_stress_test |

## 3. Previous Coverage / Duplicate Avoidance Check

No `stock_agent` source code was opened. This standalone MD uses the prior chat state as the schedule ledger: previous completed state was `R5 / loop 72`, so this run resolves to `R6 / loop 72`. The case selection deliberately avoids reusing the prior R5 consumer-export symbols and moves into the R6 financial capital-return axis.

Novelty check:

| Metric | Value |
|---|---:|
| calibration_usable_case_count | 4 |
| new_independent_case_count | 4 |
| reused_case_count | 0 |
| new_symbol_count | 4 |
| same_archetype_new_symbol_count | 4 |
| same_archetype_new_trigger_family_count | 3 |
| new_trigger_family_count | 3 |
| positive_case_count | 2 |
| counterexample_count | 2 |
| current_profile_error_count | 3 |
| new_independent_case_ratio | 1.00 |

## 4. Stock-Web OHLC Input / Price Source Validation

Manifest snapshot used:

| Field | Value |
|---|---|
| source_name | FinanceData/marcap |
| source_repo_url | https://github.com/FinanceData/marcap |
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
| schema_path | atlas/schema.json |
| universe_path | atlas/universe/all_symbols.csv |

Price basis is `tradable_raw`; the upstream basis is raw/unadjusted FinanceData/marcap. No adjusted-price reconstruction was used.

## 5. Historical Eligibility Gate

All four representative triggers pass the 180 trading-day forward-window gate under stock-web manifest max date `2026-02-20`.

| Symbol | Company | Profile path | 180D window | Corporate-action window status | Calibration usable |
|---|---|---|---|---|---|
| 105560 | KB금융 | atlas/symbol_profiles/105/105560.json | available | clean_180D_window | true |
| 055550 | 신한지주 | atlas/symbol_profiles/055/055550.json | available | clean_180D_window | true |
| 323410 | 카카오뱅크 | atlas/symbol_profiles/323/323410.json | available | clean_180D_window | true |
| 006220 | 제주은행 | atlas/symbol_profiles/006/006220.json | available | clean_180D_window | true |

## 6. Canonical Archetype Compression Map

| Fine archetype | Canonical archetype | Compression note |
|---|---|---|
| BANK_HOLDCO_VALUEUP_CET1_CAPITAL_RETURN | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | Positive C21 path: shareholder-return credibility plus CET1/ROE/PBR repair. |
| CAPITAL_RETURN_ABSENT_PLATFORM_BANK_VALUATION_TRAP | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | Counterexample: value-up sympathy without payout/cancellation bridge. |
| LOW_FLOAT_BANK_THEMATIC_PRICE_ONLY_BLOWOFF | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | Counterexample/4B: bank label and price strength alone do not create C21 evidence. |

## 7. Case Selection Summary

| Case | Symbol | Company | Role | Trigger date | Entry date | Entry price | New independent? |
|---|---:|---|---|---|---|---:|---|
| R6L72_C21_KB_20240208_CAPITAL_RETURN_VALUEUP | 105560 | KB금융 | structural_success | 2024-02-08 | 2024-02-08 | 67,600 | true |
| R6L72_C21_SHINHAN_20240208_CAPITAL_RETURN_VALUEUP | 055550 | 신한지주 | structural_success | 2024-02-08 | 2024-02-08 | 44,150 | true |
| R6L72_C21_KAKAOBANK_20240208_PLATFORM_BANK_FALSE_POSITIVE | 323410 | 카카오뱅크 | false_positive_green | 2024-02-08 | 2024-02-08 | 29,100 | true |
| R6L72_C21_JEJUBANK_20240201_LOW_FLOAT_PRICE_ONLY | 006220 | 제주은행 | price_moved_without_evidence | 2024-02-01 | 2024-02-01 | 13,230 | true |

## 8. Positive vs Counterexample Balance

| Bucket | Count | Symbols | Interpretation |
|---|---:|---|---|
| positive_structural_success | 2 | 105560, 055550 | Bank-holdco value-up/CET1/shareholder-return bridge aligned with positive 180D MFE. |
| counterexample_or_failed_rerating | 2 | 323410, 006220 | Generic financial-sector sympathy or low-float price-only bank moves produced poor score-return alignment. |
| 4B_or_4C_case | 2 | 323410, 006220 | Both are useful guardrail cases: price-only or valuation-sympathy spikes should not promote C21. |

## 9. Evidence Source Map

| Symbol | Evidence family | Stage2 evidence | Stage3 evidence | 4B/4C evidence |
|---|---|---|---|---|
| 105560 | public 2024 value-up / earnings / capital-return announcement family; exact DART/KRX URL binding deferred for implementation ledger | public_event_or_disclosure, policy_or_regulatory_optionality, relative_strength, early_revision_signal | financial_visibility, multiple_public_sources, low_red_team_risk | valuation_blowoff, positioning_overheat |
| 055550 | public 2024 value-up / earnings / capital-return announcement family; exact DART/KRX URL binding deferred for implementation ledger | public_event_or_disclosure, policy_or_regulatory_optionality, relative_strength, early_revision_signal | confirmed_revision, financial_visibility, multiple_public_sources | valuation_blowoff, positioning_overheat |
| 323410 | public market value-up sympathy / platform-bank earnings narrative; exact DART/KRX URL binding deferred for implementation ledger | public_event_or_disclosure, relative_strength, policy_or_regulatory_optionality | - | valuation_blowoff, positioning_overheat, price_only_local_peak, thesis_evidence_broken |
| 006220 | stock-web price-only relative-strength episode; no positive non-price capital-return evidence used | relative_strength | - | price_only_local_peak, positioning_overheat, thesis_evidence_broken |

Evidence binding note: this MD is a historical calibration artifact. The evidence family is recorded at trigger-date granularity; exact filing/news URL ingestion is deferred to the coding-agent ledger phase. Price calculations are based on stock-web rows, not on external chart services.

## 10. Price Data Source Map

| Symbol | Shard path | Representative stock-web rows used |
|---:|---|---|
| 105560 | atlas/ohlcv_tradable_by_symbol_year/105/105560/2024.csv | 2024-02-08,65400.0,67600.0,65000.0,67600.0,...<br>2024-02-26,64200.0,64800.0,59700.0,62500.0,...<br>2024-10-25,96000.0,103900.0,96000.0,101000.0,... |
| 055550 | atlas/ohlcv_tradable_by_symbol_year/055/055550/2024.csv | 2024-02-08,42450.0,44350.0,42250.0,44150.0,...<br>2024-02-26,42450.0,42500.0,39850.0,41350.0,...<br>2024-08-26,59800.0,64600.0,59500.0,61400.0,... |
| 323410 | atlas/ohlcv_tradable_by_symbol_year/323/323410/2024.csv | 2024-02-08,28400.0,29750.0,28250.0,29100.0,...<br>2024-02-15,30350.0,31200.0,29800.0,29800.0,...<br>2024-09-09,19710.0,20250.0,19450.0,20150.0,... |
| 006220 | atlas/ohlcv_tradable_by_symbol_year/006/006220/2024.csv | 2024-02-01,13910.0,16050.0,13200.0,13230.0,...<br>2024-04-19,15450.0,16900.0,14780.0,14910.0,...<br>2024-10-24,8250.0,8250.0,8070.0,8100.0,... |

## 11. Case-by-Case Trigger Grid

| Symbol | Trigger type | Entry | Stage2 score logic | Stage3 score logic | 4B/4C logic | Current profile verdict |
|---:|---|---:|---|---|---|---|
| 105560 | Stage2-Actionable | 67,600 | public_event_or_disclosure, policy_or_regulatory_optionality, relative_strength, early_revision_signal | financial_visibility, multiple_public_sources, low_red_team_risk | valuation_blowoff, positioning_overheat | current_profile_too_late |
| 055550 | Stage2-Actionable | 44,150 | public_event_or_disclosure, policy_or_regulatory_optionality, relative_strength, early_revision_signal | confirmed_revision, financial_visibility, multiple_public_sources | valuation_blowoff, positioning_overheat | current_profile_too_late |
| 323410 | Stage2-Actionable-candidate | 29,100 | public_event_or_disclosure, relative_strength, policy_or_regulatory_optionality | - | valuation_blowoff, positioning_overheat, price_only_local_peak, thesis_evidence_broken | current_profile_false_positive |
| 006220 | Stage4B-price-only-overlay | 13,230 | relative_strength | - | price_only_local_peak, positioning_overheat, thesis_evidence_broken | current_profile_correct |

## 12. Trigger-Level OHLC Backtest Tables

| Symbol | Entry date | Entry price | MFE 30D | MAE 30D | MFE 90D | MAE 90D | MFE 180D | MAE 180D | Peak date | Peak price | Drawdown after peak |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---|---:|---:|
| 105560 | 2024-02-08 | 67,600 | 16.27% | -11.69% | 23.37% | -11.69% | 53.70% | -11.69% | 2024-10-25 | 103,900 | -15.01% |
| 055550 | 2024-02-08 | 44,150 | 16.65% | -9.74% | 16.65% | -9.74% | 46.32% | -9.74% | 2024-08-26 | 64,600 | -20.59% |
| 323410 | 2024-02-08 | 29,100 | 7.22% | -6.19% | 7.22% | -28.52% | 7.22% | -33.16% | 2024-02-15 | 31,200 | -37.66% |
| 006220 | 2024-02-01 | 13,230 | 21.32% | -18.14% | 27.74% | -18.14% | 27.74% | -39.00% | 2024-04-19 | 16,900 | -52.25% |

Aggregate note: P0-style broad R6 selection gives avg MFE90 `18.75%` and avg MAE90 `-17.02%`, but this is polluted by two counterexamples. A C21-specific guard selecting only formal capital-return bridge cases improves avg MFE90 to `20.01%` with avg MAE90 `-10.71%`.

## 13. Current Calibrated Profile Stress Test

| Symbol | Current profile judgment | Actual MFE/MAE alignment | Residual interpretation |
|---:|---|---|---|
| 105560 | current_profile_too_late | Strong 90/180D MFE despite early MAE | Formal shareholder-return/CET1 bridge should reach Green earlier than generic financial rerating. |
| 055550 | current_profile_too_late | Positive 180D MFE, moderate early MAE | Same C21 underweight: return cadence and capital buffer should promote more cleanly. |
| 323410 | current_profile_false_positive | MFE capped near 7%, 180D MAE below -33% | Value-up sympathy without payout bridge must be capped below Yellow/Green. |
| 006220 | current_profile_correct | Price-only spike suffered deep drawdown | Price-only blowoff guard worked, but C21 ledger should retain it as a hard negative exemplar. |

Answers to required stress-test questions:

1. The current profile is broadly correct on price-only blocking, but too coarse inside C21.
2. Actual MFE/MAE supports early promotion only when shareholder-return and capital-buffer evidence exist.
3. Stage2 actionable bonus is too generous for platform-bank or low-float bank sympathy.
4. Yellow threshold 75 is not enough for C21 unless payout/cancellation evidence is present.
5. Green threshold 87 remains reasonable, but C21 needs a faster path when CET1 + ROE/PBR + return policy align.
6. Price-only blowoff guard is appropriate and should be strengthened for low-float bank themes.
7. Full 4B non-price requirement is kept; price-only remains overlay/blocker, not full sell thesis.
8. Hard 4C routing is useful for KakaoBank/Jeju-style failed-thesis labeling after the drawdown confirms lack of non-price support.

## 14. Stage2 / Yellow / Green Comparison

| Symbol | Stage2 candidate | Stage2-Actionable | Stage3-Yellow | Stage3-Green | Green lateness ratio |
|---:|---|---|---|---|---|
| 105560 | 2024-02-01 policy sympathy | 2024-02-08 | P0: yes | P0: delayed; P2: yes | not_applicable_no_confirmed_green_on_trigger_date |
| 055550 | 2024-02-01 policy sympathy | 2024-02-08 | P0: yes | P0: delayed; P2: yes | not_applicable_no_confirmed_green_on_trigger_date |
| 323410 | 2024-02-08 sympathy | blocked by P2 | P0 false-positive risk | no | not_applicable_no_confirmed_green_trigger |
| 006220 | price-only | blocked | blocked | blocked | not_applicable_price_only |

## 15. 4B Local vs Full-window Timing Audit

| Symbol | 4B evidence type | local proximity | full-window proximity | Verdict |
|---:|---|---:|---:|---|
| 105560 | valuation_blowoff, positioning_overheat | null | null | not_primary_4B_row |
| 055550 | valuation_blowoff, positioning_overheat | null | null | not_primary_4B_row |
| 323410 | valuation_blowoff, positioning_overheat, price_only | 0.92 | 0.92 | good_counterexample_4B_watch_timing |
| 006220 | price_only, positioning_overheat | 0.60 | 0.54 | price_only_local_4B_not_full_positive |

C21 conclusion: price-only bank-theme strength can be a **blocker/overlay**, but it is not positive capital-return evidence.

## 16. 4C Protection Audit

| Symbol | 4C label | Protection interpretation |
|---:|---|---|
| 105560 | thesis_break_watch_only | No 4C in 180D window. |
| 055550 | thesis_break_watch_only | No 4C in 180D window. |
| 323410 | hard_4c_success | The failed rerating and large MAE support hard thesis-break handling after payout bridge fails. |
| 006220 | hard_4c_success | Price-only spike retraced deeply; no positive C21 thesis should survive. |

## 17. Sector-Specific Rule Candidate

`sector_specific_rule_candidate = true`

Proposed R6 sector shadow rule:

```text
R6_C21_FORMAL_RETURN_BRIDGE_GATE
If large_sector_id == L6 and canonical_archetype_id == C21:
  promote Stage2-Actionable -> Stage3-Green only when at least two of the following are present:
    1. explicit shareholder-return policy, buyback, cancellation, or payout-ratio path;
    2. CET1/capital buffer or solvency-capital room supporting the return;
    3. ROE/PBR repair narrative backed by financial visibility;
    4. repeat public source confirmation after earnings.
  Cap at Stage2-Watch/Yellow if only financial-sector sympathy, rate beta, or platform-bank relative strength exists.
```

## 18. Canonical-Archetype Rule Candidate

`canonical_archetype_rule_candidate = true`

Proposed C21 canonical rule:

```text
C21_CAPITAL_RETURN_EVIDENCE_SPLIT
positive_score_axis:
  + formal shareholder return/cancellation evidence
  + CET1/capital buffer confirmation
  + ROE/PBR repair visibility
  + repeated financial visibility after earnings
negative_guard_axis:
  - no formal payout/cancellation bridge
  - platform-bank valuation sympathy only
  - low-float bank price-only theme
  - high MAE after relative-strength-only trigger
```

## 19. Before / After Backtest Comparison

| Profile | Scope | Eligible triggers | Selected cases | Avg MFE90 | Avg MAE90 | Avg MFE180 | Avg MAE180 | False positive rate | Verdict |
|---|---|---:|---|---:|---:|---:|---:|---:|---|
| P0 e2r_2_1_stock_web_calibrated_proxy | current global proxy | 4 | all four | 18.75% | -17.02% | 33.74% | -23.4% | 50% | mixed_alignment |
| P0b e2r_2_0_baseline_reference | rollback reference | 4 | all four | 18.75% | -17.02% | 33.74% | -23.4% | 50% | weaker_than_current_on_price_only_guard |
| P1 sector_specific_candidate_profile | L6 sector | 2 | 105560, 055550 | 20.01% | -10.71% | 50.01% | -10.71% | 0% | better_alignment |
| P2 canonical_archetype_candidate_profile | C21 | 2 | 105560, 055550 | 20.01% | -10.71% | 50.01% | -10.71% | 0% | best_alignment |
| P3 counterexample_guard_profile | C21 guard | 2 blocked | 323410, 006220 blocked | n/a | n/a | n/a | n/a | 0% after blocking | guardrail_pass |

## 20. Score-Return Alignment Matrix

| Symbol | Weighted before | Stage before | Weighted after | Stage after | MFE90 | MAE90 | Alignment |
|---:|---:|---|---:|---|---:|---:|---|
| 105560 | 84.0 | Stage3-Yellow | 89.0 | Stage3-Green | 23.37% | -11.69% | current_profile_too_late |
| 055550 | 82.0 | Stage3-Yellow | 88.0 | Stage3-Green | 16.65% | -9.74% | current_profile_too_late |
| 323410 | 77.0 | Stage3-Yellow | 66.0 | Stage2-Watch | 7.22% | -28.52% | current_profile_false_positive |
| 006220 | 73.0 | Stage2-Actionable-candidate | 58.0 | Stage4B-Watch/Blocked | 27.74% | -18.14% | current_profile_correct |

## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive_case_count | counterexample_count | 4B_case_count | 4C_case_count | new_independent_case_count | reused_case_count | calibration_usable_trigger_count | representative_trigger_count | current_profile_error_count | sector_rule_candidate | canonical_rule_candidate | coverage_gap_after_this_loop |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| L6_FINANCIAL_CAPITAL_RETURN_DIGITAL | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | BANK_HOLDCO_VALUEUP_CET1_CAPITAL_RETURN__VS__CAPITAL_RETURN_ABSENT_PLATFORM_LOW_FLOAT_PRICE_ONLY | 2 | 2 | 2 | 2 | 4 | 0 | 4 | 4 | 3 | true | true | remaining: insurers C22 and broker/securities capital-return cases |

## 22. Residual Contribution Summary

```yaml
new_independent_case_count: 4
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 4
new_canonical_archetype_count: 0
new_fine_archetype_count: 3
new_trigger_family_count: 3
tested_existing_calibrated_axes:
  - stage2_actionable_evidence_bonus
  - stage3_yellow_total_min
  - stage3_green_total_min
  - price_only_blowoff_blocks_positive_stage
  - full_4b_requires_non_price_evidence
residual_error_types_found:
  - current_profile_too_late
  - current_profile_false_positive
  - high_mae_relative_strength_only
new_axis_proposed:
  - C21_formal_capital_return_bridge_gate
  - C21_absent_payout_bridge_negative_cap
existing_axis_strengthened:
  - price_only_blowoff_blocks_positive_stage
  - full_4b_requires_non_price_evidence
existing_axis_weakened: null
existing_axis_kept:
  - hard_4c_thesis_break_routes_to_4c
sector_specific_rule_candidate: true
canonical_archetype_rule_candidate: true
no_new_signal_reason: null
loop_contribution_label: canonical_archetype_rule_candidate
do_not_propose_new_weight_delta: false
```

## 23. Validation Scope / Non-Validation Scope

Validated:

```text
- Stock-web manifest fields.
- Symbol profile paths and clean 180D windows.
- Representative 2024 tradable OHLC rows for entry, peak, and drawdown anchors.
- MFE/MAE for 30D/90D/180D research windows.
- Positive/counterexample balance for C21.
```

Not validated in this MD:

```text
- Exact DART filing URL ingestion.
- Production scoring implementation.
- Live candidate discovery.
- Brokerage execution or trading recommendation.
- Adjusted-price reconstruction.
```

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,C21_formal_capital_return_bridge_gate,canonical_archetype_specific,L6_FINANCIAL_CAPITAL_RETURN_DIGITAL,C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN,0,1,+1,"formal shareholder-return plus capital buffer separates KB/Shinhan from KakaoBank/JejuBank","improved false-positive control and preserved positive MFE",TRG_R6L72_C21_KB_20240208_CAPITAL_RETURN_VALUEUP|TRG_R6L72_C21_SHINHAN_20240208_CAPITAL_RETURN_VALUEUP|TRG_R6L72_C21_KAKAOBANK_20240208_PLATFORM_BANK_FALSE_POSITIVE|TRG_R6L72_C21_JEJUBANK_20240201_LOW_FLOAT_PRICE_ONLY,4,4,2,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,C21_absent_payout_bridge_negative_cap,canonical_archetype_specific,L6_FINANCIAL_CAPITAL_RETURN_DIGITAL,C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN,0,1,+1,"platform-bank or low-float bank relative strength without payout/cancellation bridge should cap promotion","blocked two counterexamples",TRG_R6L72_C21_KAKAOBANK_20240208_PLATFORM_BANK_FALSE_POSITIVE|TRG_R6L72_C21_JEJUBANK_20240201_LOW_FLOAT_PRICE_ONLY,2,2,2,medium,counterexample_guard,"not production; post-calibrated residual"
```

## 25. Machine-Readable Rows

### price_source_validation

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration"}
```

### case rows

```jsonl
{"row_type": "case", "case_id": "R6L72_C21_KB_20240208_CAPITAL_RETURN_VALUEUP", "symbol": "105560", "company_name": "KB금융", "round": "R6", "loop": "72", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "fine_archetype_id": "BANK_HOLDCO_VALUEUP_CET1_CAPITAL_RETURN", "case_type": "structural_success", "positive_or_counterexample": "positive", "best_trigger": "Stage2-Actionable", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "current_profile_too_late", "current_profile_verdict": "current_profile_too_late", "price_source": "Songdaiki/stock-web", "notes": "Corporate value-up + bank-holdco capital-return rerating; public earnings/capital-return policy family; board-level payout/cancellation credibility required for promotion."}
{"row_type": "case", "case_id": "R6L72_C21_SHINHAN_20240208_CAPITAL_RETURN_VALUEUP", "symbol": "055550", "company_name": "신한지주", "round": "R6", "loop": "72", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "fine_archetype_id": "BANK_HOLDCO_VALUEUP_CET1_CAPITAL_RETURN", "case_type": "structural_success", "positive_or_counterexample": "positive", "best_trigger": "Stage2-Actionable", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "current_profile_too_late", "current_profile_verdict": "current_profile_too_late", "price_source": "Songdaiki/stock-web", "notes": "Bank-holdco value-up rerating with explicit shareholder return cadence and capital-ratio buffer; slower but cleaner than pure price/low-float bank themes."}
{"row_type": "case", "case_id": "R6L72_C21_KAKAOBANK_20240208_PLATFORM_BANK_FALSE_POSITIVE", "symbol": "323410", "company_name": "카카오뱅크", "round": "R6", "loop": "72", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "fine_archetype_id": "CAPITAL_RETURN_ABSENT_PLATFORM_BANK_VALUATION_TRAP", "case_type": "false_positive_green", "positive_or_counterexample": "counterexample", "best_trigger": "Stage2-Actionable-candidate", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "current_profile_false_positive", "current_profile_verdict": "current_profile_false_positive", "price_source": "Songdaiki/stock-web", "notes": "Financial-sector value-up sympathy and platform-bank relative strength without board-level payout/cancellation, CET1-to-return bridge, or mature bank-holdco PBR repair mechanics."}
{"row_type": "case", "case_id": "R6L72_C21_JEJUBANK_20240201_LOW_FLOAT_PRICE_ONLY", "symbol": "006220", "company_name": "제주은행", "round": "R6", "loop": "72", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "fine_archetype_id": "LOW_FLOAT_BANK_THEMATIC_PRICE_ONLY_BLOWOFF", "case_type": "price_moved_without_evidence", "positive_or_counterexample": "counterexample", "best_trigger": "Stage4B-price-only-overlay", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "current_profile_correct", "current_profile_verdict": "current_profile_correct", "price_source": "Songdaiki/stock-web", "notes": "Low-float bank/financial-theme price spike with no durable capital-return bridge; useful as C21 guardrail rather than positive promotion evidence."}
```

### trigger rows

```jsonl
{"row_type": "trigger", "trigger_id": "TRG_R6L72_C21_KB_20240208_CAPITAL_RETURN_VALUEUP", "case_id": "R6L72_C21_KB_20240208_CAPITAL_RETURN_VALUEUP", "symbol": "105560", "company_name": "KB금융", "round": "R6", "loop": "72", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "fine_archetype_id": "BANK_HOLDCO_VALUEUP_CET1_CAPITAL_RETURN", "sector": "financial_holding_bank", "primary_archetype": "C21 capital-return / ROE-PBR repair", "loop_objective": "sector_specific_rule_discovery|canonical_archetype_compression|counterexample_mining|coverage_gap_fill", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-02-08", "entry_date": "2024-02-08", "entry_price": 67600, "evidence_available_at_that_date": "Corporate value-up + bank-holdco capital-return rerating; public earnings/capital-return policy family; board-level payout/cancellation credibility required for promotion.", "evidence_source": "public 2024 value-up / earnings / capital-return announcement family; exact DART/KRX URL binding deferred for implementation ledger", "stage2_evidence_fields": ["public_event_or_disclosure", "policy_or_regulatory_optionality", "relative_strength", "early_revision_signal"], "stage3_evidence_fields": ["financial_visibility", "multiple_public_sources", "low_red_team_risk"], "stage4b_evidence_fields": ["valuation_blowoff", "positioning_overheat"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/105/105560/2024.csv", "profile_path": "atlas/symbol_profiles/105/105560.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 16.27, "MFE_90D_pct": 23.37, "MFE_180D_pct": 53.7, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -11.69, "MAE_90D_pct": -11.69, "MAE_180D_pct": -11.69, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-10-25", "peak_price": 103900, "drawdown_after_peak_pct": -15.01, "green_lateness_ratio": "not_applicable_no_confirmed_green_on_trigger_date", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "not_primary_4B_row", "four_b_evidence_type": ["valuation_blowoff", "positioning_overheat"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "structural_success", "current_profile_verdict": "current_profile_too_late", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R6L72_105560_20240208_67600", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "TRG_R6L72_C21_SHINHAN_20240208_CAPITAL_RETURN_VALUEUP", "case_id": "R6L72_C21_SHINHAN_20240208_CAPITAL_RETURN_VALUEUP", "symbol": "055550", "company_name": "신한지주", "round": "R6", "loop": "72", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "fine_archetype_id": "BANK_HOLDCO_VALUEUP_CET1_CAPITAL_RETURN", "sector": "financial_holding_bank", "primary_archetype": "C21 capital-return / ROE-PBR repair", "loop_objective": "sector_specific_rule_discovery|canonical_archetype_compression|counterexample_mining|coverage_gap_fill", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-02-08", "entry_date": "2024-02-08", "entry_price": 44150, "evidence_available_at_that_date": "Bank-holdco value-up rerating with explicit shareholder return cadence and capital-ratio buffer; slower but cleaner than pure price/low-float bank themes.", "evidence_source": "public 2024 value-up / earnings / capital-return announcement family; exact DART/KRX URL binding deferred for implementation ledger", "stage2_evidence_fields": ["public_event_or_disclosure", "policy_or_regulatory_optionality", "relative_strength", "early_revision_signal"], "stage3_evidence_fields": ["confirmed_revision", "financial_visibility", "multiple_public_sources"], "stage4b_evidence_fields": ["valuation_blowoff", "positioning_overheat"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/055/055550/2024.csv", "profile_path": "atlas/symbol_profiles/055/055550.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 16.65, "MFE_90D_pct": 16.65, "MFE_180D_pct": 46.32, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -9.74, "MAE_90D_pct": -9.74, "MAE_180D_pct": -9.74, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-08-26", "peak_price": 64600, "drawdown_after_peak_pct": -20.59, "green_lateness_ratio": "not_applicable_no_confirmed_green_on_trigger_date", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "not_primary_4B_row", "four_b_evidence_type": ["valuation_blowoff", "positioning_overheat"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "structural_success", "current_profile_verdict": "current_profile_too_late", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R6L72_055550_20240208_44150", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "TRG_R6L72_C21_KAKAOBANK_20240208_PLATFORM_BANK_FALSE_POSITIVE", "case_id": "R6L72_C21_KAKAOBANK_20240208_PLATFORM_BANK_FALSE_POSITIVE", "symbol": "323410", "company_name": "카카오뱅크", "round": "R6", "loop": "72", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "fine_archetype_id": "CAPITAL_RETURN_ABSENT_PLATFORM_BANK_VALUATION_TRAP", "sector": "internet_bank_platform_financial", "primary_archetype": "C21 capital-return / ROE-PBR repair", "loop_objective": "sector_specific_rule_discovery|canonical_archetype_compression|counterexample_mining|coverage_gap_fill", "trigger_type": "Stage2-Actionable-candidate", "trigger_date": "2024-02-08", "entry_date": "2024-02-08", "entry_price": 29100, "evidence_available_at_that_date": "Financial-sector value-up sympathy and platform-bank relative strength without board-level payout/cancellation, CET1-to-return bridge, or mature bank-holdco PBR repair mechanics.", "evidence_source": "public market value-up sympathy / platform-bank earnings narrative; exact DART/KRX URL binding deferred for implementation ledger", "stage2_evidence_fields": ["public_event_or_disclosure", "relative_strength", "policy_or_regulatory_optionality"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["valuation_blowoff", "positioning_overheat", "price_only_local_peak"], "stage4c_evidence_fields": ["thesis_evidence_broken"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/323/323410/2024.csv", "profile_path": "atlas/symbol_profiles/323/323410.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 7.22, "MFE_90D_pct": 7.22, "MFE_180D_pct": 7.22, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -6.19, "MAE_90D_pct": -28.52, "MAE_180D_pct": -33.16, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-02-15", "peak_price": 31200, "drawdown_after_peak_pct": -37.66, "green_lateness_ratio": "not_applicable_no_confirmed_green_on_trigger_date", "four_b_local_peak_proximity": 0.92, "four_b_full_window_peak_proximity": 0.92, "four_b_timing_verdict": "good_counterexample_4B_watch_timing", "four_b_evidence_type": ["valuation_blowoff", "positioning_overheat", "price_only"], "four_c_protection_label": "hard_4c_success", "trigger_outcome_label": "failed_rerating", "current_profile_verdict": "current_profile_false_positive", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R6L72_323410_20240208_29100", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "TRG_R6L72_C21_JEJUBANK_20240201_LOW_FLOAT_PRICE_ONLY", "case_id": "R6L72_C21_JEJUBANK_20240201_LOW_FLOAT_PRICE_ONLY", "symbol": "006220", "company_name": "제주은행", "round": "R6", "loop": "72", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "fine_archetype_id": "LOW_FLOAT_BANK_THEMATIC_PRICE_ONLY_BLOWOFF", "sector": "regional_bank_low_float", "primary_archetype": "C21 capital-return / ROE-PBR repair", "loop_objective": "sector_specific_rule_discovery|canonical_archetype_compression|counterexample_mining|coverage_gap_fill", "trigger_type": "Stage4B-price-only-overlay", "trigger_date": "2024-02-01", "entry_date": "2024-02-01", "entry_price": 13230, "evidence_available_at_that_date": "Low-float bank/financial-theme price spike with no durable capital-return bridge; useful as C21 guardrail rather than positive promotion evidence.", "evidence_source": "stock-web price-only relative-strength episode; no positive non-price capital-return evidence used", "stage2_evidence_fields": ["relative_strength"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["price_only_local_peak", "positioning_overheat"], "stage4c_evidence_fields": ["thesis_evidence_broken"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/006/006220/2024.csv", "profile_path": "atlas/symbol_profiles/006/006220.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 21.32, "MFE_90D_pct": 27.74, "MFE_180D_pct": 27.74, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -18.14, "MAE_90D_pct": -18.14, "MAE_180D_pct": -39.0, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-04-19", "peak_price": 16900, "drawdown_after_peak_pct": -52.25, "green_lateness_ratio": "not_applicable_no_confirmed_green_on_trigger_date", "four_b_local_peak_proximity": 0.6, "four_b_full_window_peak_proximity": 0.54, "four_b_timing_verdict": "price_only_local_4B_not_full_positive", "four_b_evidence_type": ["price_only", "positioning_overheat"], "four_c_protection_label": "hard_4c_success", "trigger_outcome_label": "price_moved_without_evidence", "current_profile_verdict": "current_profile_correct", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R6L72_006220_20240201_13230", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
```

### score_simulation rows

```jsonl
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R6L72_C21_KB_20240208_CAPITAL_RETURN_VALUEUP", "trigger_id": "TRG_R6L72_C21_KB_20240208_CAPITAL_RETURN_VALUEUP", "symbol": "105560", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 6, "revision_score": 10, "relative_strength_score": 14, "customer_quality_score": 0, "policy_or_regulatory_score": 11, "valuation_repricing_score": 15, "execution_risk_score": -2, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "cet1_buffer_score": 16, "shareholder_return_score": 14, "roe_pbr_capital_return_score": 16}, "weighted_score_before": 84.0, "stage_label_before": "Stage3-Yellow", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 6, "revision_score": 10, "relative_strength_score": 14, "customer_quality_score": 0, "policy_or_regulatory_score": 11, "valuation_repricing_score": 15, "execution_risk_score": -2, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "cet1_buffer_score": 16, "shareholder_return_score": 17, "roe_pbr_capital_return_score": 18}, "weighted_score_after": 89.0, "stage_label_after": "Stage3-Green", "changed_components": ["shareholder_return_score", "roe_pbr_capital_return_score"], "component_delta_explanation": "C21 shadow profile rewards formal capital-return + CET1/ROE-PBR bridge and penalizes platform/low-float price-only sympathy without board-level payout evidence.", "MFE_90D_pct": 23.37, "MAE_90D_pct": -11.69, "score_return_alignment_label": "current_profile_too_late", "current_profile_verdict": "current_profile_too_late"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R6L72_C21_SHINHAN_20240208_CAPITAL_RETURN_VALUEUP", "trigger_id": "TRG_R6L72_C21_SHINHAN_20240208_CAPITAL_RETURN_VALUEUP", "symbol": "055550", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 5, "revision_score": 9, "relative_strength_score": 13, "customer_quality_score": 0, "policy_or_regulatory_score": 11, "valuation_repricing_score": 13, "execution_risk_score": -2, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "cet1_buffer_score": 15, "shareholder_return_score": 14, "roe_pbr_capital_return_score": 15}, "weighted_score_before": 82.0, "stage_label_before": "Stage3-Yellow", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 5, "revision_score": 9, "relative_strength_score": 13, "customer_quality_score": 0, "policy_or_regulatory_score": 11, "valuation_repricing_score": 13, "execution_risk_score": -2, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "cet1_buffer_score": 15, "shareholder_return_score": 18, "roe_pbr_capital_return_score": 17}, "weighted_score_after": 88.0, "stage_label_after": "Stage3-Green", "changed_components": ["shareholder_return_score", "roe_pbr_capital_return_score"], "component_delta_explanation": "C21 shadow profile rewards formal capital-return + CET1/ROE-PBR bridge and penalizes platform/low-float price-only sympathy without board-level payout evidence.", "MFE_90D_pct": 16.65, "MAE_90D_pct": -9.74, "score_return_alignment_label": "current_profile_too_late", "current_profile_verdict": "current_profile_too_late"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R6L72_C21_KAKAOBANK_20240208_PLATFORM_BANK_FALSE_POSITIVE", "trigger_id": "TRG_R6L72_C21_KAKAOBANK_20240208_PLATFORM_BANK_FALSE_POSITIVE", "symbol": "323410", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 3, "relative_strength_score": 14, "customer_quality_score": 0, "policy_or_regulatory_score": 10, "valuation_repricing_score": 12, "execution_risk_score": -6, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "cet1_buffer_score": 4, "shareholder_return_score": 1, "roe_pbr_capital_return_score": 4}, "weighted_score_before": 77.0, "stage_label_before": "Stage3-Yellow", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 3, "relative_strength_score": 14, "customer_quality_score": 0, "policy_or_regulatory_score": 10, "valuation_repricing_score": 9, "execution_risk_score": -6, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "cet1_buffer_score": 4, "shareholder_return_score": -3, "roe_pbr_capital_return_score": 0}, "weighted_score_after": 66.0, "stage_label_after": "Stage2-Watch", "changed_components": ["shareholder_return_score", "roe_pbr_capital_return_score", "valuation_repricing_score"], "component_delta_explanation": "C21 shadow profile rewards formal capital-return + CET1/ROE-PBR bridge and penalizes platform/low-float price-only sympathy without board-level payout evidence.", "MFE_90D_pct": 7.22, "MAE_90D_pct": -28.52, "score_return_alignment_label": "current_profile_false_positive", "current_profile_verdict": "current_profile_false_positive"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R6L72_C21_JEJUBANK_20240201_LOW_FLOAT_PRICE_ONLY", "trigger_id": "TRG_R6L72_C21_JEJUBANK_20240201_LOW_FLOAT_PRICE_ONLY", "symbol": "006220", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 20, "customer_quality_score": 0, "policy_or_regulatory_score": 4, "valuation_repricing_score": 8, "execution_risk_score": -10, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "cet1_buffer_score": 1, "shareholder_return_score": 0, "roe_pbr_capital_return_score": 1}, "weighted_score_before": 73.0, "stage_label_before": "Stage2-Actionable-candidate", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 12, "customer_quality_score": 0, "policy_or_regulatory_score": 4, "valuation_repricing_score": 3, "execution_risk_score": -12, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "cet1_buffer_score": 1, "shareholder_return_score": 0, "roe_pbr_capital_return_score": 1}, "weighted_score_after": 58.0, "stage_label_after": "Stage4B-Watch/Blocked", "changed_components": ["relative_strength_score", "valuation_repricing_score", "execution_risk_score"], "component_delta_explanation": "C21 shadow profile rewards formal capital-return + CET1/ROE-PBR bridge and penalizes platform/low-float price-only sympathy without board-level payout evidence.", "MFE_90D_pct": 27.74, "MAE_90D_pct": -18.14, "score_return_alignment_label": "current_profile_correct", "current_profile_verdict": "current_profile_correct"}
{"row_type": "residual_contribution", "round": "R6", "loop": "72", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "new_independent_case_count": 4, "reused_case_count": 0, "new_symbol_count": 4, "new_trigger_family_count": 3, "tested_existing_calibrated_axes": ["stage2_actionable_evidence_bonus", "stage3_yellow_total_min", "stage3_green_total_min", "price_only_blowoff_blocks_positive_stage", "full_4b_requires_non_price_evidence"], "residual_error_types_found": ["current_profile_too_late", "current_profile_false_positive", "high_mae_relative_strength_only"], "loop_contribution_label": "canonical_archetype_rule_candidate", "do_not_propose_new_weight_delta": false, "scheduled_round": "R6", "scheduled_loop": 72, "round_schedule_status": "valid", "round_sector_consistency": "pass", "positive_case_count": 2, "counterexample_count": 2, "current_profile_error_count": 3, "diversity_score_summary": "new_symbols=4; new_trigger_family=3; counterexamples=2; residual_errors=3; wrong_round_penalty=0"}
```

### narrative_only rows

```jsonl
{"row_type":"narrative_only","case_id":"R6L72_C21_1Y_2Y_EXTENSIONS","symbol":"MULTI","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","reason":"1Y/2Y values are not primary calibration fields in this loop; 30D/90D/180D windows are the quantitative basis.","price_source":"Songdaiki/stock-web","usage":"not_weight_calibration"}
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
completed_round = R6
completed_loop = 72
next_round = R7
next_loop = 72
round_schedule_status = valid
round_sector_consistency = pass
```

## 28. Source Notes

Primary source paths used:

```text
Songdaiki/stock-web/atlas/manifest.json
Songdaiki/stock-web/atlas/symbol_profiles/105/105560.json
Songdaiki/stock-web/atlas/symbol_profiles/055/055550.json
Songdaiki/stock-web/atlas/symbol_profiles/323/323410.json
Songdaiki/stock-web/atlas/symbol_profiles/006/006220.json
Songdaiki/stock-web/atlas/ohlcv_tradable_by_symbol_year/105/105560/2024.csv
Songdaiki/stock-web/atlas/ohlcv_tradable_by_symbol_year/055/055550/2024.csv
Songdaiki/stock-web/atlas/ohlcv_tradable_by_symbol_year/323/323410/2024.csv
Songdaiki/stock-web/atlas/ohlcv_tradable_by_symbol_year/006/006220/2024.csv
```

This file is a historical calibration artifact only. It is not current/live stock discovery, investment advice, brokerage execution, or production scoring change.

