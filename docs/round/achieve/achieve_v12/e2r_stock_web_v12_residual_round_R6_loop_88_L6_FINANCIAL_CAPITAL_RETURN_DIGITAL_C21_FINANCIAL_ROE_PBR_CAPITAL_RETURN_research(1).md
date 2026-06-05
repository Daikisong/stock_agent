# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
research_session = post_calibrated_sector_archetype_residual_research
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
scheduled_round = R6
scheduled_loop = 88
round_schedule_status = valid
round_sector_consistency = pass
large_sector_id = L6_FINANCIAL_CAPITAL_RETURN_DIGITAL
canonical_archetype_id = C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN
fine_archetype_id = BANK_VALUEUP_CAPITAL_RETURN_BRIDGE_VS_POLICY_BANK_AND_BROKERAGE_DIGITAL_EVENT_CAP
loop_objective = coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | canonical_archetype_compression
output_file = e2r_stock_web_v12_residual_round_R6_loop_88_L6_FINANCIAL_CAPITAL_RETURN_DIGITAL_C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN_research.md
```

This loop continues loop 88 after R5. It adds 3 C21 financial capital-return cases: one bank value-up / shareholder-return positive and two policy-bank / digital-brokerage 4B event-cap counterexamples.

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
scheduled_loop = 88
large_sector_id = L6_FINANCIAL_CAPITAL_RETURN_DIGITAL
canonical_archetype_id = C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN
round_sector_consistency = pass
computed_next_round = R7
computed_next_loop = 88
```

R6 permits L6 financial / capital return / digital finance research. C21 already has broad coverage, so this loop avoids the top repeated C21 symbols and focuses on a more surgical split: true bank value-up / capital-return bridge versus policy-bank and brokerage/digital-finance event premiums.

## 3. Previous Coverage / Duplicate Avoidance Check

No-Repeat hard key used:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

No-Repeat snapshot context:

```text
C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN = 51 rows / 19 symbols / good-bad Stage2 22-11 / 4B-4C 7-0
top covered symbols include 006220(5), 016360(5), 071050(4), 105560(4), 138040(4), 139130(4)
```

Selected rows avoid those repeated combinations:

```text
086790 / Stage2-Actionable / 2024-01-02
024110 / Stage4B / 2024-03-14
003530 / Stage4B / 2024-03-05
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
| 086790 | atlas/symbol_profiles/086/086790.json | no corporate-action candidate |
| 024110 | atlas/symbol_profiles/024/024110.json | selected 2024 window clean; CA candidates are pre-2004 |
| 003530 | atlas/symbol_profiles/003/003530.json | selected 2024 window clean; CA candidates are pre-2020 |

## 5. Historical Eligibility Gate

| case_id | symbol | entry_date | entry in shard | forward 180D | OHLC valid | CA clean | calibration_usable |
|---|---|---:|---|---:|---|---|---|
| R6L88_C21_HANAFG_2024_BANK_VALUEUP_CAPITAL_RETURN_POSITIVE | 086790 | 2024-01-02 | yes | 180 | yes | yes | true |
| R6L88_C21_IBK_2024_POLICY_BANK_VALUEUP_EVENT_CAP_4B | 024110 | 2024-03-14 | yes | 180 | yes | yes | true |
| R6L88_C21_HANWHAINV_2024_DIGITAL_BROKERAGE_THEME_CAP_4B | 003530 | 2024-03-05 | yes | 180 | yes | yes | true |

## 6. Canonical Archetype Compression Map

| canonical | fine/deep split | meaning |
|---|---|---|
| C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | BANK_VALUEUP_CAPITAL_RETURN_BRIDGE | Positive Stage2 requires ROE/PBR discount plus shareholder-return or revision bridge. |
| C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | POLICY_BANK_VALUEUP_EVENT_CAP | Policy-bank value-up premium can cap if shareholder-return quality is constrained. |
| C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | DIGITAL_BROKERAGE_THEME_EVENT_CAP | Brokerage/digital-finance theme momentum is 4B/watch unless ROE/PBR/capital-return bridge appears. |

## 7. Case Selection Summary

| case_id | symbol | company | role | selected reason |
|---|---|---|---|---|
| R6L88_C21_HANAFG_2024_BANK_VALUEUP_CAPITAL_RETURN_POSITIVE | 086790 | 하나금융지주 | positive | Value-up/capital-return bridge produced strong MFE with low early MAE. |
| R6L88_C21_IBK_2024_POLICY_BANK_VALUEUP_EVENT_CAP_4B | 024110 | 기업은행 | counterexample / 4B | Policy-bank premium capped quickly; forward MFE was tiny and MAE meaningful. |
| R6L88_C21_HANWHAINV_2024_DIGITAL_BROKERAGE_THEME_CAP_4B | 003530 | 한화투자증권 | counterexample / 4B | Digital/brokerage theme spike faded without capital-return bridge. |

## 8. Positive vs Counterexample Balance

```text
positive_case_count = 1
counterexample_count = 2
4B_case_count = 2
4C_case_count = 0
calibration_usable_case_count = 3
calibration_usable_trigger_count = 3
```

## 9. Evidence Source Map

| case | evidence status | evidence_url_pending | source_proxy_only | usage |
|---|---|---|---|---|
| Hana FG value-up/capital return | historical public/report proxy | true | true | shadow-only positive |
| IBK policy-bank event cap | historical public/report proxy | true | true | 4B overlay counterexample |
| Hanwha Investment digital brokerage cap | historical public/news proxy | true | true | 4B overlay counterexample |

## 10. Price Data Source Map

| symbol | shard | profile |
|---|---|---|
| 086790 | atlas/ohlcv_tradable_by_symbol_year/086/086790/2024.csv | atlas/symbol_profiles/086/086790.json |
| 024110 | atlas/ohlcv_tradable_by_symbol_year/024/024110/2024.csv | atlas/symbol_profiles/024/024110.json |
| 003530 | atlas/ohlcv_tradable_by_symbol_year/003/003530/2024.csv | atlas/symbol_profiles/003/003530.json |

## 11. Case-by-Case Trigger Grid

| trigger_id | symbol | trigger_type | entry_date | entry_price | role | verdict |
|---|---|---|---:|---:|---|---|
| R6L88_C21_HANAFG_2024_STAGE2_ACTIONABLE_VALUEUP_CAPITAL_RETURN | 086790 | Stage2-Actionable | 2024-01-02 | 42800 | positive | bank value-up / capital-return bridge worked |
| R6L88_C21_IBK_2024_STAGE4B_POLICY_BANK_VALUEUP_CAP | 024110 | Stage4B | 2024-03-14 | 15700 | counterexample/4B | policy-bank value-up premium cap |
| R6L88_C21_HANWHAINV_2024_STAGE4B_DIGITAL_BROKERAGE_THEME_CAP | 003530 | Stage4B | 2024-03-05 | 4780 | counterexample/4B | digital brokerage theme event cap |

## 12. Trigger-Level OHLC Backtest Tables

| trigger_id | entry | MFE30 | MAE30 | MFE90 | MAE90 | MFE180 | MAE180 | peak_date | peak_price | drawdown_after_peak |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| R6L88_C21_HANAFG_2024_STAGE2_ACTIONABLE_VALUEUP_CAPITAL_RETURN | 42800 | 33.88 | -4.67 | 52.57 | -4.67 | 61.92 | -4.67 | 2024-08-27 | 69300 | -17.89 |
| R6L88_C21_IBK_2024_STAGE4B_POLICY_BANK_VALUEUP_CAP | 15700 | 1.97 | -16.37 | 1.97 | -16.37 | 1.97 | -18.54 | 2024-03-15 | 16010 | -20.11 |
| R6L88_C21_HANWHAINV_2024_STAGE4B_DIGITAL_BROKERAGE_THEME_CAP | 4780 | 11.51 | -26.88 | 11.51 | -35.15 | 11.51 | -39.96 | 2024-03-05 | 5330 | -46.15 |

## 13. Current Calibrated Profile Stress Test

| axis | outcome |
|---|---|
| stage2_required_bridge | strengthen: C21 Stage2 needs ROE/PBR discount plus capital-return/revision bridge |
| local_4b_watch_guard | strengthen: policy-bank and digital brokerage theme premiums should route to 4B watch |
| full_4b_requires_non_price_evidence | keep |
| price_only_blowoff_blocks_positive_stage | keep |
| hard_4c_thesis_break_routes_to_4c | keep |

## 14. Stage2 / Yellow / Green Comparison

No confirmed Stage3-Green row is introduced. The useful split is Stage2/4B quality:

| symbol | stage quality | explanation |
|---|---|---|
| 086790 | good_stage2 | Bank value-up / capital-return bridge produced strong asymmetry. |
| 024110 | good_4B | Policy-bank premium had little forward upside and capped early. |
| 003530 | good_4B | Digital brokerage theme spike lacked capital-return bridge and drew down deeply. |

```text
green_lateness_ratio = not_applicable
reason = no_confirmed_Stage3_Green_trigger
```

## 15. 4B Local vs Full-window Timing Audit

| trigger | local proximity | full-window proximity | timing verdict |
|---|---:|---:|---|
| 024110 policy-bank value-up cap | 1.00 | 1.00 | good_full_window_4B_timing_policy_bank_valueup_event_cap |
| 003530 digital brokerage cap | 1.00 | 1.00 | good_full_window_4B_timing_digital_brokerage_theme_event_cap |
| 086790 bank capital-return bridge | n/a | n/a | positive Stage2; later valuation watch only |

## 16. 4C Protection Audit

```text
4C_case_count = 0
four_c_protection_label = thesis_break_watch_only for 024110 / 003530
```

No hard 4C candidate is proposed. C21 residual here is Stage2 bridge quality and 4B event-cap timing.

## 17. Sector-Specific Rule Candidate

```text
sector_specific_rule_candidate = true
rule_scope = sector_specific
rule = In L6 financial/capital-return cases, Stage2 requires ROE/PBR discount plus shareholder-return, capital-policy, or earnings/revision bridge. Value-up label, policy-bank beta, or digital-finance theme momentum alone remains watch/4B.
proposal_status = shadow_only
```

## 18. Canonical-Archetype Rule Candidate

```text
canonical_archetype_rule_candidate = true
canonical_archetype_id = C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN
rule = C21 should split bank capital-return bridge positives from policy-bank and digital brokerage event caps. Event-cap rows are 4B overlay/risk calibration, not Stage3-Green promotion evidence.
proposal_status = shadow_only_not_production
```

## 19. Before / After Backtest Comparison

| profile | hypothesis | eligible triggers | avg_MFE90 | avg_MAE90 | false_positive_rate | verdict |
|---|---|---:|---:|---:|---:|---|
| P0 e2r_2_1_stock_web_calibrated_proxy | current profile | 3 | 22.02 | -18.73 | 0.67 | mixed; C21 split needed |
| P0b e2r_2_0_baseline_reference | older baseline | 3 | 22.02 | -18.73 | 0.67 | weaker bridge/theme guard |
| P1 sector_specific_candidate_profile | L6 capital-return bridge required | 2 | 27.27 | -10.52 | 0.50 | better |
| P2 canonical_archetype_candidate_profile | C21 bridge vs event-cap split | 2 | 27.27 | -10.52 | 0.50 | best explanatory fit |
| P3 counterexample_guard_profile | reject policy/digital theme caps as positive | 1 | 52.57 | -4.67 | 0.00 | safest but source-proxy blockers remain |

## 20. Score-Return Alignment Matrix

| trigger | score before | stage before | score after | stage after | MFE90 | MAE90 | alignment |
|---|---:|---|---:|---|---:|---:|---|
| 086790 value-up bridge | 66 | Stage2-Watch | 74 | Stage2-Actionable | 52.57 | -4.67 | bank_valueup_capital_return_positive |
| 024110 policy-bank cap | 69 | Stage3-Yellow-like | 55 | Stage4B-watch | 1.97 | -16.37 | policy_bank_valueup_event_cap_guard |
| 003530 digital brokerage cap | 70 | Stage3-Yellow-like | 53 | Stage4B-watch | 11.51 | -35.15 | digital_brokerage_theme_event_cap_guard |

## 21. Coverage Matrix

```jsonl
{"row_type": "coverage_matrix", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "fine_archetype_id": "BANK_VALUEUP_CAPITAL_RETURN_BRIDGE_VS_POLICY_BANK_AND_BROKERAGE_DIGITAL_EVENT_CAP", "positive_case_count": 1, "counterexample_count": 2, "4B_case_count": 2, "4C_case_count": 0, "new_independent_case_count": 3, "reused_case_count": 0, "calibration_usable_trigger_count": 3, "representative_trigger_count": 1, "current_profile_error_count": 2, "sector_rule_candidate": true, "canonical_rule_candidate": true, "coverage_gap_after_this_loop": "Adds C21 bank value-up capital-return bridge positive vs policy-bank and digital-brokerage event-cap 4B split using non-top-covered symbols."}
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
residual_error_types_found: bank_valueup_capital_return_bridge_positive, policy_bank_valueup_event_cap_4B, digital_brokerage_theme_false_capital_return_rerating
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
- C21 bank value-up capital-return bridge vs policy-bank/digital-brokerage event-cap split
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
shadow_weight,stage2_required_bridge,canonical_archetype,L6_FINANCIAL_CAPITAL_RETURN_DIGITAL,C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN,configured,C21_requires_ROE_PBR_capital_return_bridge,0,"C21 Stage2 should require ROE/PBR discount plus shareholder-return or revision bridge, not value-up label or digital-finance theme alone","Hana FG positive worked; IBK and Hanwha Investment event/theme caps failed positive-stage promotion","R6L88_C21_HANAFG_2024_STAGE2_ACTIONABLE_VALUEUP_CAPITAL_RETURN|R6L88_C21_IBK_2024_STAGE4B_POLICY_BANK_VALUEUP_CAP|R6L88_C21_HANWHAINV_2024_STAGE4B_DIGITAL_BROKERAGE_THEME_CAP",3,3,2,low,canonical_shadow_only,"do_not_propose_new_weight_delta=true because source-proxy/evidence-url-pending rows remain"
shadow_weight,local_4b_watch_guard,canonical_archetype,L6_FINANCIAL_CAPITAL_RETURN_DIGITAL,C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN,configured,cap_policy_bank_and_digital_finance_premiums_as_4B_watch,0,"Policy-bank value-up and brokerage/digital-finance theme premiums can peak before durable ROE/PBR/capital-return evidence appears","IBK and Hanwha Investment showed low MFE90 and meaningful MAE90 after event/theme spikes","R6L88_C21_IBK_2024_STAGE4B_POLICY_BANK_VALUEUP_CAP|R6L88_C21_HANWHAINV_2024_STAGE4B_DIGITAL_BROKERAGE_THEME_CAP",2,2,2,low,guardrail_shadow_only,"4B overlay only; not production"
```

## 25. Machine-Readable Rows

### 25.1 price_source_validation

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration", "source_name": "FinanceData/marcap", "tradable_row_count": 14354401, "raw_row_count": 15214118, "symbol_count": 5414, "active_like_symbol_count": 2868, "inactive_or_delisted_like_symbol_count": 2546}
```

### 25.2 case rows

```jsonl
{"row_type": "case", "case_id": "R6L88_C21_HANAFG_2024_BANK_VALUEUP_CAPITAL_RETURN_POSITIVE", "symbol": "086790", "company_name": "하나금융지주", "round": "R6", "loop": "88", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "fine_archetype_id": "BANK_VALUEUP_CAPITAL_RETURN_BRIDGE_VS_POLICY_BANK_AND_BROKERAGE_DIGITAL_EVENT_CAP", "case_type": "structural_success", "positive_or_counterexample": "positive", "best_trigger": "R6L88_C21_HANAFG_2024_STAGE2_ACTIONABLE_VALUEUP_CAPITAL_RETURN", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "Bank value-up / shareholder-return bridge produced strong 90D and 180D upside with shallow entry MAE.", "current_profile_verdict": "current_profile_kept_but_C21_positive_requires_ROE_PBR_capital_return_bridge_not_valueup_label_only", "price_source": "Songdaiki/stock-web", "notes": "Source-proxy only; exact as-of capital-return evidence URL remains pending, so no production weight delta."}
{"row_type": "case", "case_id": "R6L88_C21_IBK_2024_POLICY_BANK_VALUEUP_EVENT_CAP_4B", "symbol": "024110", "company_name": "기업은행", "round": "R6", "loop": "88", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "fine_archetype_id": "BANK_VALUEUP_CAPITAL_RETURN_BRIDGE_VS_POLICY_BANK_AND_BROKERAGE_DIGITAL_EVENT_CAP", "case_type": "event_cap_4b_counterexample", "positive_or_counterexample": "counterexample", "best_trigger": "R6L88_C21_IBK_2024_STAGE4B_POLICY_BANK_VALUEUP_CAP", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "Policy-bank value-up/capital-return premium capped quickly; weak forward MFE and notable MAE argue for 4B/watch rather than full positive-stage promotion.", "current_profile_verdict": "current_profile_4B_too_late_if_policy_bank_valueup_premium_not_capped", "price_source": "Songdaiki/stock-web", "notes": "Policy-bank value-up event-cap counterexample; source-proxy only."}
{"row_type": "case", "case_id": "R6L88_C21_HANWHAINV_2024_DIGITAL_BROKERAGE_THEME_CAP_4B", "symbol": "003530", "company_name": "한화투자증권", "round": "R6", "loop": "88", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "fine_archetype_id": "BANK_VALUEUP_CAPITAL_RETURN_BRIDGE_VS_POLICY_BANK_AND_BROKERAGE_DIGITAL_EVENT_CAP", "case_type": "event_cap_4b_counterexample", "positive_or_counterexample": "counterexample", "best_trigger": "R6L88_C21_HANWHAINV_2024_STAGE4B_DIGITAL_BROKERAGE_THEME_CAP", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "Brokerage/digital-finance theme premium had capped forward upside and deep MAE; theme beta should not substitute for ROE/PBR/capital-return bridge.", "current_profile_verdict": "current_profile_false_positive_if_digital_finance_theme_spike_counts_as_capital_return_rerating", "price_source": "Songdaiki/stock-web", "notes": "Digital/brokerage theme event cap; source-proxy only."}
```

### 25.3 trigger rows

```jsonl
{"row_type": "trigger", "trigger_id": "R6L88_C21_HANAFG_2024_STAGE2_ACTIONABLE_VALUEUP_CAPITAL_RETURN", "case_id": "R6L88_C21_HANAFG_2024_BANK_VALUEUP_CAPITAL_RETURN_POSITIVE", "symbol": "086790", "company_name": "하나금융지주", "round": "R6", "loop": "88", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "fine_archetype_id": "BANK_VALUEUP_CAPITAL_RETURN_BRIDGE_VS_POLICY_BANK_AND_BROKERAGE_DIGITAL_EVENT_CAP", "sector": "bank_valueup_capital_return", "primary_archetype": "bank_ROE_PBR_shareholder_return_bridge", "loop_objective": "coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | canonical_archetype_compression", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-01-02", "entry_date": "2024-01-02", "entry_price": 42800.0, "evidence_available_at_that_date": "bank value-up / capital return / ROE-PBR discount bridge proxy; exact as-of source URL pending", "evidence_source": "source_proxy_historical_public_report_proxy", "stage2_evidence_fields": ["ROE_PBR_discount", "capital_return_policy_proxy", "valueup_policy_tailwind", "relative_strength_reversal"], "stage3_evidence_fields": ["strong_90D_MFE", "low_MAE_to_capital_return_rerating_path"], "stage4b_evidence_fields": ["valuation_repricing_watch_after_180D_peak"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/086/086790/2024.csv", "profile_path": "atlas/symbol_profiles/086/086790.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 33.88, "MFE_90D_pct": 52.57, "MFE_180D_pct": 61.92, "MFE_1Y_pct": "not_calculated", "MFE_2Y_pct": "not_calculated", "MAE_30D_pct": -4.67, "MAE_90D_pct": -4.67, "MAE_180D_pct": -4.67, "MAE_1Y_pct": "not_calculated", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-08-27", "peak_price": 69300.0, "drawdown_after_peak_pct": -17.89, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "positive_stage2_but_later_valuation_watch_needed", "four_b_evidence_type": ["valuation_blowoff", "positioning_overheat"], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "good_stage2_bank_valueup_capital_return_success", "current_profile_verdict": "current_profile_kept_but_source_proxy_blocks_positive_delta", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R6L88_C21_086790_2024-01-02_42800", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "evidence_url_pending": true, "source_proxy_only": true}
{"row_type": "trigger", "trigger_id": "R6L88_C21_IBK_2024_STAGE4B_POLICY_BANK_VALUEUP_CAP", "case_id": "R6L88_C21_IBK_2024_POLICY_BANK_VALUEUP_EVENT_CAP_4B", "symbol": "024110", "company_name": "기업은행", "round": "R6", "loop": "88", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "fine_archetype_id": "BANK_VALUEUP_CAPITAL_RETURN_BRIDGE_VS_POLICY_BANK_AND_BROKERAGE_DIGITAL_EVENT_CAP", "sector": "policy_bank_valueup", "primary_archetype": "policy_bank_valueup_event_cap_4B", "loop_objective": "coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | canonical_archetype_compression", "trigger_type": "Stage4B", "trigger_date": "2024-03-14", "entry_date": "2024-03-14", "entry_price": 15700.0, "evidence_available_at_that_date": "policy-bank value-up / dividend premium spike proxy; exact as-of source URL pending", "evidence_source": "source_proxy_historical_public_report_proxy", "stage2_evidence_fields": ["valueup_policy_tailwind", "dividend_yield_proxy", "relative_strength_spike"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["event_premium_cap", "weak_follow_through", "post_peak_drawdown"], "stage4c_evidence_fields": ["thesis_break_watch_only"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/024/024110/2024.csv", "profile_path": "atlas/symbol_profiles/024/024110.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 1.97, "MFE_90D_pct": 1.97, "MFE_180D_pct": 1.97, "MFE_1Y_pct": "not_calculated", "MFE_2Y_pct": "not_calculated", "MAE_30D_pct": -16.37, "MAE_90D_pct": -16.37, "MAE_180D_pct": -18.54, "MAE_1Y_pct": "not_calculated", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-03-15", "peak_price": 16010.0, "drawdown_after_peak_pct": -20.11, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 1.0, "four_b_full_window_peak_proximity": 1.0, "four_b_timing_verdict": "good_full_window_4B_timing_policy_bank_valueup_event_cap", "four_b_evidence_type": ["valuation_blowoff", "positioning_overheat", "policy_event_premium"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "event_cap_4B_success_not_positive_stage_promotion", "current_profile_verdict": "current_profile_4B_too_late_if_policy_bank_valueup_premium_not_capped", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R6L88_C21_024110_2024-03-14_15700", "dedupe_for_aggregate": false, "aggregate_group_role": "4B_overlay_only", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "evidence_url_pending": true, "source_proxy_only": true}
{"row_type": "trigger", "trigger_id": "R6L88_C21_HANWHAINV_2024_STAGE4B_DIGITAL_BROKERAGE_THEME_CAP", "case_id": "R6L88_C21_HANWHAINV_2024_DIGITAL_BROKERAGE_THEME_CAP_4B", "symbol": "003530", "company_name": "한화투자증권", "round": "R6", "loop": "88", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "fine_archetype_id": "BANK_VALUEUP_CAPITAL_RETURN_BRIDGE_VS_POLICY_BANK_AND_BROKERAGE_DIGITAL_EVENT_CAP", "sector": "brokerage_digital_finance_theme", "primary_archetype": "digital_brokerage_crypto_theme_event_cap_4B", "loop_objective": "coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | canonical_archetype_compression", "trigger_type": "Stage4B", "trigger_date": "2024-03-05", "entry_date": "2024-03-05", "entry_price": 4780.0, "evidence_available_at_that_date": "brokerage / digital-finance / crypto theme premium proxy; exact as-of source URL pending", "evidence_source": "source_proxy_historical_public_news_proxy", "stage2_evidence_fields": ["digital_finance_theme", "brokerage_beta", "relative_strength_spike"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["event_premium_cap", "weak_follow_through", "post_peak_drawdown"], "stage4c_evidence_fields": ["thesis_break_watch_only"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/003/003530/2024.csv", "profile_path": "atlas/symbol_profiles/003/003530.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 11.51, "MFE_90D_pct": 11.51, "MFE_180D_pct": 11.51, "MFE_1Y_pct": "not_calculated", "MFE_2Y_pct": "not_calculated", "MAE_30D_pct": -26.88, "MAE_90D_pct": -35.15, "MAE_180D_pct": -39.96, "MAE_1Y_pct": "not_calculated", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-03-05", "peak_price": 5330.0, "drawdown_after_peak_pct": -46.15, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 1.0, "four_b_full_window_peak_proximity": 1.0, "four_b_timing_verdict": "good_full_window_4B_timing_digital_brokerage_theme_event_cap", "four_b_evidence_type": ["valuation_blowoff", "positioning_overheat", "price_only"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "event_cap_4B_success_not_positive_stage_promotion", "current_profile_verdict": "current_profile_false_positive_if_digital_finance_theme_spike_counts_as_capital_return_rerating", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R6L88_C21_003530_2024-03-05_4780", "dedupe_for_aggregate": false, "aggregate_group_role": "4B_overlay_only", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "evidence_url_pending": true, "source_proxy_only": true}
```

### 25.4 score_simulation rows

```jsonl
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R6L88_C21_HANAFG_2024_BANK_VALUEUP_CAPITAL_RETURN_POSITIVE", "trigger_id": "R6L88_C21_HANAFG_2024_STAGE2_ACTIONABLE_VALUEUP_CAPITAL_RETURN", "symbol": "086790", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 10, "margin_bridge_score": 20, "revision_score": 35, "relative_strength_score": 70, "customer_quality_score": 20, "policy_or_regulatory_score": 45, "valuation_repricing_score": 70, "execution_risk_score": 35, "legal_or_contract_risk_score": 10, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 66, "stage_label_before": "Stage2-Watch", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 10, "margin_bridge_score": 45, "revision_score": 55, "relative_strength_score": 65, "customer_quality_score": 25, "policy_or_regulatory_score": 50, "valuation_repricing_score": 75, "execution_risk_score": 25, "legal_or_contract_risk_score": 10, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 74, "stage_label_after": "Stage2-Actionable", "changed_components": ["margin_bridge_score", "revision_score", "relative_strength_score", "valuation_repricing_score", "execution_risk_score"], "component_delta_explanation": "bank_valueup_capital_return_positive", "MFE_90D_pct": 52.57, "MAE_90D_pct": -4.67, "score_return_alignment_label": "bank_valueup_capital_return_positive", "current_profile_verdict": "current_profile_kept_but_source_proxy_blocks_positive_delta"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R6L88_C21_IBK_2024_POLICY_BANK_VALUEUP_EVENT_CAP_4B", "trigger_id": "R6L88_C21_IBK_2024_STAGE4B_POLICY_BANK_VALUEUP_CAP", "symbol": "024110", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 10, "margin_bridge_score": 20, "revision_score": 35, "relative_strength_score": 70, "customer_quality_score": 20, "policy_or_regulatory_score": 45, "valuation_repricing_score": 70, "execution_risk_score": 35, "legal_or_contract_risk_score": 10, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 69, "stage_label_before": "Stage3-Yellow-like", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 10, "margin_bridge_score": 5, "revision_score": 15, "relative_strength_score": 25, "customer_quality_score": 10, "policy_or_regulatory_score": 35, "valuation_repricing_score": 35, "execution_risk_score": 80, "legal_or_contract_risk_score": 10, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 55, "stage_label_after": "Stage4B-watch", "changed_components": ["margin_bridge_score", "revision_score", "relative_strength_score", "valuation_repricing_score", "execution_risk_score"], "component_delta_explanation": "policy_bank_valueup_event_cap_guard", "MFE_90D_pct": 1.97, "MAE_90D_pct": -16.37, "score_return_alignment_label": "policy_bank_valueup_event_cap_guard", "current_profile_verdict": "current_profile_4B_too_late_if_policy_bank_valueup_premium_not_capped"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R6L88_C21_HANWHAINV_2024_DIGITAL_BROKERAGE_THEME_CAP_4B", "trigger_id": "R6L88_C21_HANWHAINV_2024_STAGE4B_DIGITAL_BROKERAGE_THEME_CAP", "symbol": "003530", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 10, "margin_bridge_score": 20, "revision_score": 35, "relative_strength_score": 70, "customer_quality_score": 20, "policy_or_regulatory_score": 45, "valuation_repricing_score": 70, "execution_risk_score": 35, "legal_or_contract_risk_score": 10, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 70, "stage_label_before": "Stage3-Yellow-like", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 10, "margin_bridge_score": 5, "revision_score": 15, "relative_strength_score": 25, "customer_quality_score": 10, "policy_or_regulatory_score": 35, "valuation_repricing_score": 35, "execution_risk_score": 80, "legal_or_contract_risk_score": 10, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 53, "stage_label_after": "Stage4B-watch", "changed_components": ["margin_bridge_score", "revision_score", "relative_strength_score", "valuation_repricing_score", "execution_risk_score"], "component_delta_explanation": "digital_brokerage_theme_event_cap_guard", "MFE_90D_pct": 11.51, "MAE_90D_pct": -35.15, "score_return_alignment_label": "digital_brokerage_theme_event_cap_guard", "current_profile_verdict": "current_profile_false_positive_if_digital_finance_theme_spike_counts_as_capital_return_rerating"}
```

### 25.5 residual_contribution row

```jsonl
{"row_type": "residual_contribution", "round": "R6", "loop": "88", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "fine_archetype_id": "BANK_VALUEUP_CAPITAL_RETURN_BRIDGE_VS_POLICY_BANK_AND_BROKERAGE_DIGITAL_EVENT_CAP", "new_independent_case_count": 3, "reused_case_count": 0, "new_symbol_count": 3, "same_archetype_new_symbol_count": 3, "same_archetype_new_trigger_family_count": 3, "new_trigger_family_count": 3, "positive_case_count": 1, "counterexample_count": 2, "4B_case_count": 2, "4C_case_count": 0, "tested_existing_calibrated_axes": ["stage2_required_bridge", "local_4b_watch_guard", "full_4b_requires_non_price_evidence", "price_only_blowoff_blocks_positive_stage"], "residual_error_types_found": ["bank_valueup_capital_return_bridge_positive", "policy_bank_valueup_event_cap_4B", "digital_brokerage_theme_false_capital_return_rerating"], "loop_contribution_label": "canonical_archetype_rule_candidate", "do_not_propose_new_weight_delta": true, "source_proxy_only_count": 3, "evidence_url_pending_count": 3}
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
completed_loop = 88
next_round = R7
next_loop = 88
round_schedule_status = valid
round_sector_consistency = pass
```

## 28. Source Notes

- Main execution prompt: Songdaiki/stock_agent docs/core/e2r_v12_prompt_round_scheduler_corrected.txt.
- No-repeat index: Songdaiki/stock_agent docs/core/V12_Research_No_Repeat_Index.md.
- Price atlas: Songdaiki/stock-web atlas/manifest.json and per-symbol tradable shards.
- This file contains no investment recommendation and no production scoring change.
