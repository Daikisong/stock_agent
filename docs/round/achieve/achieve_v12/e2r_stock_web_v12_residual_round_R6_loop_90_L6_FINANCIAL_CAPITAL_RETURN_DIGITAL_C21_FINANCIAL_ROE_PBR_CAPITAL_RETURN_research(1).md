# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
research_session = post_calibrated_sector_archetype_residual_research
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
scheduled_round = R6
scheduled_loop = 90
round_schedule_status = valid
round_sector_consistency = pass
large_sector_id = L6_FINANCIAL_CAPITAL_RETURN_DIGITAL
canonical_archetype_id = C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN
fine_archetype_id = BANK_VALUEUP_ROE_CAPITAL_RETURN_BRIDGE_VS_BROKERAGE_THEME_AND_CONTROL_PREMIUM_EVENT_CAP
loop_objective = coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | canonical_archetype_compression
output_file = e2r_stock_web_v12_residual_round_R6_loop_90_L6_FINANCIAL_CAPITAL_RETURN_DIGITAL_C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN_research.md
```

This loop continues loop 90 after R5. It adds 3 C21 financial ROE/PBR capital-return cases: one bank value-up ROE/capital-return positive, one small-brokerage value-up false Stage2, and one brokerage control-premium 4B event-cap counterexample.

## 1. Current Calibrated Profile Assumption

```text
current_default_profile_proxy = e2r_2_1_stock_web_calibrated
previous_baseline_reference = e2r_2_0_baseline
production_scoring_changed = false
shadow_weight_only = true
```

Existing axes tested:

```text
stage2_required_bridge = existing_axis_strengthened
local_4b_watch_guard = existing_axis_strengthened
full_4b_requires_non_price_evidence = existing_axis_kept
price_only_blowoff_blocks_positive_stage = existing_axis_kept
hard_4c_thesis_break_routes_to_4c = existing_axis_kept
```

## 2. Round / Large Sector / Canonical Archetype Scope

```text
scheduled_round = R6
scheduled_loop = 90
large_sector_id = L6_FINANCIAL_CAPITAL_RETURN_DIGITAL
canonical_archetype_id = C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN
round_sector_consistency = pass
computed_next_round = R7
computed_next_loop = 90
```

R6 permits L6 financial/capital-return/digital-finance research. Previous R6 loop 89 used C22 insurance, so this loop returns to C21 with a non-top-covered symbol set and focuses on whether value-up/PBR rerating is backed by ROE, capital-return, earnings/revision, and balance-sheet conversion.

## 3. Previous Coverage / Duplicate Avoidance Check

No-Repeat hard key used:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

No-Repeat snapshot context:

```text
C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN = 51 rows / 19 symbols / good-bad Stage2 22-11 / 4B-4C 7-0
top covered symbols include 006220(5), 016360(5), 071050(4), 105560(4), 138040(4), 139130(4)
previous R6 loop-88 C21 symbols avoided: 086790, 024110, 003530
previous R6 loop-89 C22 symbols avoided: 088350, 001450, 032830
```

Selected rows avoid those repeated combinations:

```text
316140 / Stage2-Actionable / 2024-01-24
001510 / Stage2-Actionable / 2024-02-01
001750 / Stage4B / 2024-08-05
```

## 4. Stock-Web OHLC Input / Price Source Validation

| field | value |
|---|---|
| source | Songdaiki/stock-web |
| upstream_source | FinanceData/marcap |
| manifest | atlas/manifest.json |
| stock_web_manifest_max_date | 2026-02-20 |
| price_basis | tradable_raw |
| price_adjustment_status | raw_unadjusted_marcap |
| calibration_shard_root | atlas/ohlcv_tradable_by_symbol_year |

| symbol | profile path | CA window status |
|---|---|---|
| 316140 | atlas/symbol_profiles/316/316140.json | no corporate-action candidate |
| 001510 | atlas/symbol_profiles/001/001510.json | selected 2024 window clean |
| 001750 | atlas/symbol_profiles/001/001750.json | selected 2024 window clean |

## 5. Historical Eligibility Gate

| case_id | symbol | entry_date | entry in shard | forward 180D | OHLC valid | CA clean | calibration_usable |
|---|---|---:|---|---:|---|---|---|
| R6L90_C21_WOORI_2024_BANK_VALUEUP_ROE_CAPITAL_RETURN_POSITIVE | 316140 | 2024-01-24 | yes | 180 | yes | yes | true |
| R6L90_C21_SKSEC_2024_SMALL_BROKERAGE_VALUEUP_FALSE_STAGE2 | 001510 | 2024-02-01 | yes | 180 | yes | yes | true |
| R6L90_C21_HANYANGSEC_2024_BROKERAGE_CONTROL_PREMIUM_EVENT_CAP_4B | 001750 | 2024-08-05 | yes | 180 | yes | yes | true |

## 6. Canonical Archetype Compression Map

| canonical | fine/deep split | meaning |
|---|---|---|
| C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | BANK_VALUEUP_ROE_CAPITAL_RETURN_BRIDGE | Positive Stage2 requires low-PBR rerating backed by ROE, shareholder return, capital ratio, and revision bridge. |
| C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | SMALL_BROKERAGE_VALUEUP_FALSE_STAGE2 | Brokerage/value-up label without ROE or capital-return bridge can become weak-MFE false Stage2. |
| C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | BROKERAGE_CONTROL_PREMIUM_EVENT_CAP_4B | Control-premium / sale-event spike should route to 4B if not backed by durable ROE/capital-return bridge. |

## 7. Case Selection Summary

| case_id | symbol | company | role | selected reason |
|---|---|---|---|---|
| R6L90_C21_WOORI_2024_BANK_VALUEUP_ROE_CAPITAL_RETURN_POSITIVE | 316140 | 우리금융지주 | positive | Bank value-up / ROE-PBR / capital-return path produced controlled MAE and strong 180D MFE. |
| R6L90_C21_SKSEC_2024_SMALL_BROKERAGE_VALUEUP_FALSE_STAGE2 | 001510 | SK증권 | counterexample | Small brokerage value-up theme had tiny MFE and persistent MAE. |
| R6L90_C21_HANYANGSEC_2024_BROKERAGE_CONTROL_PREMIUM_EVENT_CAP_4B | 001750 | 한양증권 | counterexample / 4B | Brokerage control-premium event capped near the August spike and then drew down. |

## 8. Positive vs Counterexample Balance

```text
positive_case_count = 1
counterexample_count = 2
4B_case_count = 1
4C_case_count = 0
calibration_usable_case_count = 3
calibration_usable_trigger_count = 3
```

## 9. Evidence Source Map

| case | evidence status | evidence_url_pending | source_proxy_only | usage |
|---|---|---|---|---|
| Woori Financial value-up/ROE bridge | historical public/report proxy | true | true | shadow-only positive |
| SK Securities small-brokerage false Stage2 | historical public/news proxy | true | true | false-Stage2 guardrail |
| Hanyang Securities control-premium cap | historical public/news proxy | true | true | 4B overlay counterexample |

## 10. Price Data Source Map

| symbol | shard | profile |
|---|---|---|
| 316140 | atlas/ohlcv_tradable_by_symbol_year/316/316140/2024.csv | atlas/symbol_profiles/316/316140.json |
| 001510 | atlas/ohlcv_tradable_by_symbol_year/001/001510/2024.csv | atlas/symbol_profiles/001/001510.json |
| 001750 | atlas/ohlcv_tradable_by_symbol_year/001/001750/2024.csv | atlas/symbol_profiles/001/001750.json |

## 11. Case-by-Case Trigger Grid

| trigger_id | symbol | trigger_type | entry_date | entry_price | role | verdict |
|---|---|---|---:|---:|---|---|
| R6L90_C21_WOORI_2024_STAGE2_ACTIONABLE_BANK_VALUEUP_ROE_CAPITAL_RETURN | 316140 | Stage2-Actionable | 2024-01-24 | 13000 | positive | bank ROE/PBR capital-return bridge worked |
| R6L90_C21_SKSEC_2024_STAGE2_FALSE_POSITIVE_SMALL_BROKERAGE_VALUEUP | 001510 | Stage2-Actionable | 2024-02-01 | 647 | counterexample | small brokerage value-up false Stage2 |
| R6L90_C21_HANYANGSEC_2024_STAGE4B_BROKERAGE_CONTROL_PREMIUM_CAP | 001750 | Stage4B | 2024-08-05 | 16160 | counterexample/4B | brokerage control-premium event cap |

## 12. Trigger-Level OHLC Backtest Tables

| trigger_id | entry | MFE30 | MAE30 | MFE90 | MAE90 | MFE180 | MAE180 | peak_date | peak_price | drawdown_after_peak |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| R6L90_C21_WOORI_2024_STAGE2_ACTIONABLE_BANK_VALUEUP_ROE_CAPITAL_RETURN | 13000 | 16.92 | -1.92 | 19.23 | -1.92 | 30.46 | -1.92 | 2024-07-29 | 16960 | -19.00 |
| R6L90_C21_SKSEC_2024_STAGE2_FALSE_POSITIVE_SMALL_BROKERAGE_VALUEUP | 647 | 3.40 | -5.56 | 3.40 | -13.45 | 3.40 | -23.34 | 2024-02-21 | 669 | -25.86 |
| R6L90_C21_HANYANGSEC_2024_STAGE4B_BROKERAGE_CONTROL_PREMIUM_CAP | 16160 | 20.11 | -11.39 | 20.11 | -23.82 | 20.11 | -23.82 | 2024-08-05 | 19410 | -36.58 |

## 13. Current Calibrated Profile Stress Test

| axis | outcome |
|---|---|
| stage2_required_bridge | strengthen: C21 Stage2 needs ROE/PBR/capital-return/revision bridge |
| local_4b_watch_guard | strengthen: brokerage value-up and control-premium events should route to 4B watch when bridge is missing |
| full_4b_requires_non_price_evidence | keep |
| price_only_blowoff_blocks_positive_stage | keep |
| hard_4c_thesis_break_routes_to_4c | keep; no hard 4C promoted |

## 14. Stage2 / Yellow / Green Comparison

No confirmed Stage3-Green row is introduced. The useful split is financial value-up conversion quality:

| symbol | stage quality | explanation |
|---|---|---|
| 316140 | good_stage2 | Bank value-up path had controlled MAE and durable 180D upside. |
| 001510 | bad_stage2 | Brokerage value-up label produced weak MFE and persistent drawdown. |
| 001750 | good_4B | Control-premium event capped near the event spike. |

```text
green_lateness_ratio = not_applicable
reason = no_confirmed_Stage3-Green trigger
```

## 15. 4B Local vs Full-window Timing Audit

| trigger | local proximity | full-window proximity | timing verdict |
|---|---:|---:|---|
| 001510 small brokerage false Stage2 | 1.00 | 1.00 | small-brokerage value-up theme spike was false Stage2 event cap |
| 001750 brokerage control-premium cap | 1.00 | 1.00 | good full-window 4B timing |
| 316140 bank value-up bridge | n/a | n/a | positive Stage2, but later bank value-up valuation watch required |

## 16. 4C Protection Audit

```text
4C_case_count = 0
four_c_protection_label = thesis_break_watch_only for 001510 / 001750
```

No hard 4C candidate is proposed. R6 loop 90 is about Stage2 bridge quality and 4B event-cap timing.

## 17. Sector-Specific Rule Candidate

```text
sector_specific_rule_candidate = true
rule_scope = sector_specific
rule = In L6 financial ROE/PBR capital-return cases, Stage2 requires verified ROE, shareholder-return policy, capital ratio, earnings/revision, or balance-sheet bridge. Financial, bank, brokerage, low-PBR, value-up, or control-premium label alone remains watch/4B.
proposal_status = shadow_only
```

## 18. Canonical-Archetype Rule Candidate

```text
canonical_archetype_rule_candidate = true
canonical_archetype_id = C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN
rule = C21 should split ROE/PBR/capital-return positives from small-brokerage value-up false Stage2 and brokerage control-premium event-cap rows. Event-cap rows are 4B overlay/risk calibration, not Stage3-Green promotion evidence.
proposal_status = shadow_only_not_production
```

## 19. Before / After Backtest Comparison

| profile | hypothesis | eligible triggers | avg_MFE90 | avg_MAE90 | false_positive_rate | verdict |
|---|---|---:|---:|---:|---:|---|
| P0 e2r_2_1_stock_web_calibrated_proxy | current profile | 3 | 14.25 | -13.06 | 0.67 | mixed; C21 split needed |
| P0b e2r_2_0_baseline_reference | older baseline | 3 | 14.25 | -13.06 | 0.67 | weaker bridge/event-cap guard |
| P1 sector_specific_candidate_profile | L6 ROE/capital-return bridge required | 2 | 11.32 | -7.69 | 0.50 | better rejection alignment |
| P2 canonical_archetype_candidate_profile | C21 bridge vs event-cap split | 2 | 11.32 | -7.69 | 0.50 | best explanatory fit |
| P3 counterexample_guard_profile | reject bridge-missing brokerage themes as positive | 1 | 19.23 | -1.92 | 0.00 | safest but source-proxy blockers remain |

## 20. Score-Return Alignment Matrix

| trigger | score before | stage before | score after | stage after | MFE90 | MAE90 | alignment |
|---|---:|---|---:|---|---:|---:|---|
| 316140 bank value-up bridge | 66 | Stage2-Watch | 74 | Stage2-Actionable | 19.23 | -1.92 | bank_valueup_ROE_capital_return_positive |
| 001510 small brokerage false | 66 | Stage2-Actionable | 53 | Stage1/Watch | 3.40 | -13.45 | small_brokerage_valueup_false_stage2 |
| 001750 brokerage cap | 70 | Stage3-Yellow-like | 54 | Stage4B-watch | 20.11 | -23.82 | brokerage_control_premium_event_cap_4B_guard |

## 21. Coverage Matrix

```jsonl
{"row_type": "coverage_matrix", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "fine_archetype_id": "BANK_VALUEUP_ROE_CAPITAL_RETURN_BRIDGE_VS_BROKERAGE_THEME_AND_CONTROL_PREMIUM_EVENT_CAP", "positive_case_count": 1, "counterexample_count": 2, "4B_case_count": 1, "4C_case_count": 0, "new_independent_case_count": 3, "reused_case_count": 0, "calibration_usable_trigger_count": 3, "representative_trigger_count": 2, "current_profile_error_count": 2, "sector_rule_candidate": true, "canonical_rule_candidate": true, "coverage_gap_after_this_loop": "Adds C21 bank value-up ROE/capital-return positive, small-brokerage value-up false Stage2, and brokerage control-premium event-cap 4B split using non-top-covered symbols."}
```

## 22. Residual Contribution Summary

```text
new_independent_case_count: 3
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 3
new_canonical_archetype_count: 0
new_fine_archetype_count: 1
new_trigger_family_count: 3
tested_existing_calibrated_axes: stage2_required_bridge, local_4b_watch_guard, full_4b_requires_non_price_evidence, price_only_blowoff_blocks_positive_stage
residual_error_types_found: bank_valueup_ROE_capital_return_positive, small_brokerage_valueup_false_stage2, brokerage_control_premium_event_cap_4B
new_axis_proposed: null
existing_axis_strengthened: stage2_required_bridge, local_4b_watch_guard
existing_axis_weakened: null
existing_axis_kept: full_4b_requires_non_price_evidence, price_only_blowoff_blocks_positive_stage, hard_4c_thesis_break_routes_to_4c
sector_specific_rule_candidate: true
canonical_archetype_rule_candidate: true
no_new_signal_reason: null
loop_contribution_label: canonical_archetype_rule_candidate
do_not_propose_new_weight_delta: true
```

## 23. Validation Scope / Non-Validation Scope

Validation scope:

```text
- Stock-web tradable raw OHLC path
- entry_date / entry_price
- MFE/MAE 30D/90D/180D
- corporate-action window cleanliness
- C21 financial ROE/PBR capital-return bridge vs brokerage event-cap split
```

Non-validation scope:

```text
- Exact as-of evidence URLs remain pending for all selected cases.
- No production scoring update.
- No live candidate scan.
- No investment recommendation.
```

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,stage2_required_bridge,canonical_archetype,L6_FINANCIAL_CAPITAL_RETURN_DIGITAL,C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN,configured,C21_requires_ROE_PBR_capital_return_revision_bridge,0,"C21 Stage2 should require ROE/PBR rerating, shareholder-return policy, capital ratio, earnings/revision, or balance-sheet bridge, not financial/value-up label alone","Woori Financial positive worked; SK Securities and Hanyang Securities theme/event rows failed positive-stage promotion","R6L90_C21_WOORI_2024_STAGE2_ACTIONABLE_BANK_VALUEUP_ROE_CAPITAL_RETURN|R6L90_C21_SKSEC_2024_STAGE2_FALSE_POSITIVE_SMALL_BROKERAGE_VALUEUP|R6L90_C21_HANYANGSEC_2024_STAGE4B_BROKERAGE_CONTROL_PREMIUM_CAP",3,3,2,low,canonical_shadow_only,"do_not_propose_new_weight_delta=true because source-proxy/evidence-url-pending rows remain"
shadow_weight,local_4b_watch_guard,canonical_archetype,L6_FINANCIAL_CAPITAL_RETURN_DIGITAL,C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN,configured,cap_brokerage_valueup_and_control_premiums_as_4B_watch,0,"Brokerage/value-up/control-premium events can peak before verified capital-return or ROE bridge appears","SK Securities showed weak MFE; Hanyang Securities showed event-cap behavior after control-premium spike","R6L90_C21_SKSEC_2024_STAGE2_FALSE_POSITIVE_SMALL_BROKERAGE_VALUEUP|R6L90_C21_HANYANGSEC_2024_STAGE4B_BROKERAGE_CONTROL_PREMIUM_CAP",2,2,2,low,guardrail_shadow_only,"4B overlay only; not production"
```

## 25. Machine-Readable Rows

### 25.1 price_source_validation

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration", "source_name": "FinanceData/marcap", "tradable_row_count": 14354401, "raw_row_count": 15214118, "symbol_count": 5414, "active_like_symbol_count": 2868, "inactive_or_delisted_like_symbol_count": 2546}
```

### 25.2 case rows

```jsonl
{"row_type": "case", "case_id": "R6L90_C21_WOORI_2024_BANK_VALUEUP_ROE_CAPITAL_RETURN_POSITIVE", "symbol": "316140", "company_name": "우리금융지주", "round": "R6", "loop": "90", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "fine_archetype_id": "BANK_VALUEUP_ROE_CAPITAL_RETURN_BRIDGE_VS_BROKERAGE_THEME_AND_CONTROL_PREMIUM_EVENT_CAP", "case_type": "structural_success", "positive_or_counterexample": "positive", "best_trigger": "R6L90_C21_WOORI_2024_STAGE2_ACTIONABLE_BANK_VALUEUP_ROE_CAPITAL_RETURN", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "Bank value-up / ROE-PBR / capital-return bridge produced controlled MAE and strong 180D MFE; C21 works when low-PBR rerating is backed by capital policy, ROE/revision, and shareholder-return bridge.", "current_profile_verdict": "current_profile_kept_but_C21_positive_requires_ROE_PBR_capital_return_revision_bridge_not_financial_label_only", "price_source": "Songdaiki/stock-web", "notes": "No corporate-action candidate in profile; source-proxy only, so no production weight delta."}
{"row_type": "case", "case_id": "R6L90_C21_SKSEC_2024_SMALL_BROKERAGE_VALUEUP_FALSE_STAGE2", "symbol": "001510", "company_name": "SK증권", "round": "R6", "loop": "90", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "fine_archetype_id": "BANK_VALUEUP_ROE_CAPITAL_RETURN_BRIDGE_VS_BROKERAGE_THEME_AND_CONTROL_PREMIUM_EVENT_CAP", "case_type": "failed_rerating_low_ROE_or_capital_bridge", "positive_or_counterexample": "counterexample", "best_trigger": "R6L90_C21_SKSEC_2024_STAGE2_FALSE_POSITIVE_SMALL_BROKERAGE_VALUEUP", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "Small brokerage / financial value-up theme had only tiny forward MFE and then persistent MAE; C21 Stage2 should not be granted without ROE, capital-return, earnings, or balance-sheet bridge.", "current_profile_verdict": "current_profile_false_positive_if_small_brokerage_valueup_theme_counts_without_ROE_capital_return_revision_bridge", "price_source": "Songdaiki/stock-web", "notes": "Selected 2024 window clean; source-proxy only."}
{"row_type": "case", "case_id": "R6L90_C21_HANYANGSEC_2024_BROKERAGE_CONTROL_PREMIUM_EVENT_CAP_4B", "symbol": "001750", "company_name": "한양증권", "round": "R6", "loop": "90", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "fine_archetype_id": "BANK_VALUEUP_ROE_CAPITAL_RETURN_BRIDGE_VS_BROKERAGE_THEME_AND_CONTROL_PREMIUM_EVENT_CAP", "case_type": "event_cap_4b_counterexample", "positive_or_counterexample": "counterexample", "best_trigger": "R6L90_C21_HANYANGSEC_2024_STAGE4B_BROKERAGE_CONTROL_PREMIUM_CAP", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "Brokerage/control-premium or sale-event premium capped near the August spike and then drew down; event premium should route to 4B unless capital-return and ROE bridge remains durable.", "current_profile_verdict": "current_profile_4B_too_late_if_brokerage_control_or_sale_event_premium_not_capped", "price_source": "Songdaiki/stock-web", "notes": "No corporate-action caveat in selected 2024 window; source-proxy only."}
```

### 25.3 trigger rows

```jsonl
{"row_type": "trigger", "trigger_id": "R6L90_C21_WOORI_2024_STAGE2_ACTIONABLE_BANK_VALUEUP_ROE_CAPITAL_RETURN", "case_id": "R6L90_C21_WOORI_2024_BANK_VALUEUP_ROE_CAPITAL_RETURN_POSITIVE", "symbol": "316140", "company_name": "우리금융지주", "round": "R6", "loop": "90", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "fine_archetype_id": "BANK_VALUEUP_ROE_CAPITAL_RETURN_BRIDGE_VS_BROKERAGE_THEME_AND_CONTROL_PREMIUM_EVENT_CAP", "sector": "bank_valueup_ROE_PBR_capital_return", "primary_archetype": "bank_lowPBR_capital_return_ROE_revision_bridge", "loop_objective": "coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | canonical_archetype_compression", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-01-24", "entry_date": "2024-01-24", "entry_price": 13000.0, "evidence_available_at_that_date": "bank value-up / low-PBR / ROE and capital-return bridge proxy; exact as-of source URL pending", "evidence_source": "source_proxy_historical_public_report_proxy", "stage2_evidence_fields": ["low_PBR_discount", "capital_return_policy_proxy", "ROE_revision_bridge_proxy", "relative_strength_reversal"], "stage3_evidence_fields": ["strong_MFE180", "controlled_entry_MAE", "bank_valueup_policy_path"], "stage4b_evidence_fields": ["valuation_watch_after_bank_valueup_run"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/316/316140/2024.csv", "profile_path": "atlas/symbol_profiles/316/316140.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 16.92, "MFE_90D_pct": 19.23, "MFE_180D_pct": 30.46, "MFE_1Y_pct": "not_calculated", "MFE_2Y_pct": "not_calculated", "MAE_30D_pct": -1.92, "MAE_90D_pct": -1.92, "MAE_180D_pct": -1.92, "MAE_1Y_pct": "not_calculated", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-07-29", "peak_price": 16960.0, "drawdown_after_peak_pct": -19.0, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "positive_stage2_but_later_bank_valueup_valuation_watch_needed", "four_b_evidence_type": ["valuation_repricing", "policy_event_premium", "positioning_overheat"], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "good_stage2_bank_valueup_ROE_capital_return_bridge_success", "current_profile_verdict": "current_profile_kept_but_source_proxy_blocks_positive_delta", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R6L90_C21_316140_2024-01-24_13000", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "evidence_url_pending": true, "source_proxy_only": true}
{"row_type": "trigger", "trigger_id": "R6L90_C21_SKSEC_2024_STAGE2_FALSE_POSITIVE_SMALL_BROKERAGE_VALUEUP", "case_id": "R6L90_C21_SKSEC_2024_SMALL_BROKERAGE_VALUEUP_FALSE_STAGE2", "symbol": "001510", "company_name": "SK증권", "round": "R6", "loop": "90", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "fine_archetype_id": "BANK_VALUEUP_ROE_CAPITAL_RETURN_BRIDGE_VS_BROKERAGE_THEME_AND_CONTROL_PREMIUM_EVENT_CAP", "sector": "small_brokerage_valueup_theme", "primary_archetype": "small_brokerage_valueup_without_ROE_capital_return_bridge", "loop_objective": "coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | canonical_archetype_compression", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-02-01", "entry_date": "2024-02-01", "entry_price": 647.0, "evidence_available_at_that_date": "small brokerage / low-PBR value-up theme spike proxy; exact as-of source URL pending", "evidence_source": "source_proxy_historical_public_news_proxy", "stage2_evidence_fields": ["brokerage_valueup_theme", "low_PBR_theme_watch", "relative_strength_spike"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["weak_MFE90", "ROE_capital_return_bridge_missing", "post_theme_drawdown"], "stage4c_evidence_fields": ["thesis_break_watch_only"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/001/001510/2024.csv", "profile_path": "atlas/symbol_profiles/001/001510.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 3.4, "MFE_90D_pct": 3.4, "MFE_180D_pct": 3.4, "MFE_1Y_pct": "not_calculated", "MFE_2Y_pct": "not_calculated", "MAE_30D_pct": -5.56, "MAE_90D_pct": -13.45, "MAE_180D_pct": -23.34, "MAE_1Y_pct": "not_calculated", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-02-21", "peak_price": 669.0, "drawdown_after_peak_pct": -25.86, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 1.0, "four_b_full_window_peak_proximity": 1.0, "four_b_timing_verdict": "small_brokerage_valueup_theme_spike_was_false_stage2_event_cap", "four_b_evidence_type": ["price_only", "positioning_overheat", "ROE_capital_return_bridge_missing"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "bad_stage2_small_brokerage_valueup_without_ROE_bridge", "current_profile_verdict": "current_profile_false_positive_if_small_brokerage_valueup_theme_counts_without_ROE_capital_return_revision_bridge", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R6L90_C21_001510_2024-02-01_647", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "evidence_url_pending": true, "source_proxy_only": true}
{"row_type": "trigger", "trigger_id": "R6L90_C21_HANYANGSEC_2024_STAGE4B_BROKERAGE_CONTROL_PREMIUM_CAP", "case_id": "R6L90_C21_HANYANGSEC_2024_BROKERAGE_CONTROL_PREMIUM_EVENT_CAP_4B", "symbol": "001750", "company_name": "한양증권", "round": "R6", "loop": "90", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "fine_archetype_id": "BANK_VALUEUP_ROE_CAPITAL_RETURN_BRIDGE_VS_BROKERAGE_THEME_AND_CONTROL_PREMIUM_EVENT_CAP", "sector": "brokerage_control_premium_sale_event", "primary_archetype": "brokerage_control_premium_event_cap_4B", "loop_objective": "coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | canonical_archetype_compression", "trigger_type": "Stage4B", "trigger_date": "2024-08-05", "entry_date": "2024-08-05", "entry_price": 16160.0, "evidence_available_at_that_date": "brokerage control-premium / sale-event premium after August spike; exact as-of source URL pending", "evidence_source": "source_proxy_historical_public_news_proxy", "stage2_evidence_fields": ["brokerage_control_premium", "sale_event_premium", "relative_strength_spike"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["event_premium_cap", "weak_follow_through", "post_peak_drawdown"], "stage4c_evidence_fields": ["thesis_break_watch_only"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/001/001750/2024.csv", "profile_path": "atlas/symbol_profiles/001/001750.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 20.11, "MFE_90D_pct": 20.11, "MFE_180D_pct": 20.11, "MFE_1Y_pct": "not_calculated", "MFE_2Y_pct": "not_calculated", "MAE_30D_pct": -11.39, "MAE_90D_pct": -23.82, "MAE_180D_pct": -23.82, "MAE_1Y_pct": "not_calculated", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-08-05", "peak_price": 19410.0, "drawdown_after_peak_pct": -36.58, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 1.0, "four_b_full_window_peak_proximity": 1.0, "four_b_timing_verdict": "good_full_window_4B_timing_brokerage_control_premium_event_cap", "four_b_evidence_type": ["control_premium", "positioning_overheat", "price_only"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "event_cap_4B_success_not_positive_stage_promotion", "current_profile_verdict": "current_profile_4B_too_late_if_brokerage_control_or_sale_event_premium_not_capped", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R6L90_C21_001750_2024-08-05_16160", "dedupe_for_aggregate": false, "aggregate_group_role": "4B_overlay_only", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "evidence_url_pending": true, "source_proxy_only": true}
```

### 25.4 score_simulation rows

```jsonl
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R6L90_C21_WOORI_2024_BANK_VALUEUP_ROE_CAPITAL_RETURN_POSITIVE", "trigger_id": "R6L90_C21_WOORI_2024_STAGE2_ACTIONABLE_BANK_VALUEUP_ROE_CAPITAL_RETURN", "symbol": "316140", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 10, "margin_bridge_score": 30, "revision_score": 35, "relative_strength_score": 70, "customer_quality_score": 20, "policy_or_regulatory_score": 55, "valuation_repricing_score": 65, "execution_risk_score": 45, "legal_or_contract_risk_score": 10, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 66, "stage_label_before": "Stage2-Watch", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 10, "margin_bridge_score": 55, "revision_score": 55, "relative_strength_score": 65, "customer_quality_score": 25, "policy_or_regulatory_score": 60, "valuation_repricing_score": 65, "execution_risk_score": 30, "legal_or_contract_risk_score": 10, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 74, "stage_label_after": "Stage2-Actionable", "changed_components": ["margin_bridge_score", "revision_score", "relative_strength_score", "policy_or_regulatory_score", "valuation_repricing_score", "execution_risk_score"], "component_delta_explanation": "bank_valueup_ROE_capital_return_positive", "MFE_90D_pct": 19.23, "MAE_90D_pct": -1.92, "score_return_alignment_label": "bank_valueup_ROE_capital_return_positive", "current_profile_verdict": "current_profile_kept_but_source_proxy_blocks_positive_delta"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R6L90_C21_SKSEC_2024_SMALL_BROKERAGE_VALUEUP_FALSE_STAGE2", "trigger_id": "R6L90_C21_SKSEC_2024_STAGE2_FALSE_POSITIVE_SMALL_BROKERAGE_VALUEUP", "symbol": "001510", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 10, "margin_bridge_score": 30, "revision_score": 35, "relative_strength_score": 70, "customer_quality_score": 20, "policy_or_regulatory_score": 55, "valuation_repricing_score": 65, "execution_risk_score": 45, "legal_or_contract_risk_score": 10, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 66, "stage_label_before": "Stage2-Actionable", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 10, "margin_bridge_score": 5, "revision_score": 10, "relative_strength_score": 25, "customer_quality_score": 10, "policy_or_regulatory_score": 30, "valuation_repricing_score": 30, "execution_risk_score": 80, "legal_or_contract_risk_score": 30, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 53, "stage_label_after": "Stage1/Watch", "changed_components": ["margin_bridge_score", "revision_score", "relative_strength_score", "policy_or_regulatory_score", "valuation_repricing_score", "execution_risk_score"], "component_delta_explanation": "small_brokerage_valueup_false_stage2", "MFE_90D_pct": 3.4, "MAE_90D_pct": -13.45, "score_return_alignment_label": "small_brokerage_valueup_false_stage2", "current_profile_verdict": "current_profile_false_positive_if_small_brokerage_valueup_theme_counts_without_ROE_capital_return_revision_bridge"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R6L90_C21_HANYANGSEC_2024_BROKERAGE_CONTROL_PREMIUM_EVENT_CAP_4B", "trigger_id": "R6L90_C21_HANYANGSEC_2024_STAGE4B_BROKERAGE_CONTROL_PREMIUM_CAP", "symbol": "001750", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 10, "margin_bridge_score": 30, "revision_score": 35, "relative_strength_score": 70, "customer_quality_score": 20, "policy_or_regulatory_score": 55, "valuation_repricing_score": 65, "execution_risk_score": 45, "legal_or_contract_risk_score": 10, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 70, "stage_label_before": "Stage3-Yellow-like", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 10, "margin_bridge_score": 5, "revision_score": 10, "relative_strength_score": 25, "customer_quality_score": 10, "policy_or_regulatory_score": 30, "valuation_repricing_score": 30, "execution_risk_score": 80, "legal_or_contract_risk_score": 30, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 54, "stage_label_after": "Stage4B-watch", "changed_components": ["margin_bridge_score", "revision_score", "relative_strength_score", "policy_or_regulatory_score", "valuation_repricing_score", "execution_risk_score"], "component_delta_explanation": "brokerage_control_premium_event_cap_4B_guard", "MFE_90D_pct": 20.11, "MAE_90D_pct": -23.82, "score_return_alignment_label": "brokerage_control_premium_event_cap_4B_guard", "current_profile_verdict": "current_profile_4B_too_late_if_brokerage_control_or_sale_event_premium_not_capped"}
```

### 25.5 residual_contribution row

```jsonl
{"row_type": "residual_contribution", "round": "R6", "loop": "90", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "fine_archetype_id": "BANK_VALUEUP_ROE_CAPITAL_RETURN_BRIDGE_VS_BROKERAGE_THEME_AND_CONTROL_PREMIUM_EVENT_CAP", "new_independent_case_count": 3, "reused_case_count": 0, "new_symbol_count": 3, "same_archetype_new_symbol_count": 3, "same_archetype_new_trigger_family_count": 3, "new_trigger_family_count": 3, "positive_case_count": 1, "counterexample_count": 2, "4B_case_count": 1, "4C_case_count": 0, "tested_existing_calibrated_axes": ["stage2_required_bridge", "local_4b_watch_guard", "full_4b_requires_non_price_evidence", "price_only_blowoff_blocks_positive_stage"], "residual_error_types_found": ["bank_valueup_ROE_capital_return_positive", "small_brokerage_valueup_false_stage2", "brokerage_control_premium_event_cap_4B"], "loop_contribution_label": "canonical_archetype_rule_candidate", "do_not_propose_new_weight_delta": true, "source_proxy_only_count": 3, "evidence_url_pending_count": 3}
```

### 25.6 narrative_only row

```jsonl
{"row_type":"narrative_only","case_id":"none","symbol":"none","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","reason":"all selected rows have usable 180D stock-web windows; no narrative-only price row required","price_source":"Songdaiki/stock-web","usage":"not_weight_calibration"}
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
completed_round = R6
completed_loop = 90
next_round = R7
next_loop = 90
round_schedule_status = valid
round_sector_consistency = pass
```

## 28. Source Notes

- Main execution prompt: Songdaiki/stock_agent docs/core/e2r_v12_prompt_round_scheduler_corrected.txt.
- No-repeat index: Songdaiki/stock_agent docs/core/V12_Research_No_Repeat_Index.md.
- Price atlas: Songdaiki/stock-web atlas/manifest.json and per-symbol tradable shards.
- This file contains no investment recommendation and no production scoring change.
