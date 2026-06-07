# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
selected_round = R2
selected_loop = 97
large_sector_id = L2_AI_SEMICONDUCTOR_ELECTRONICS
canonical_archetype_id = C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY
fine_archetype_id = TEST_SOCKET_PROBE_CARD_CUSTOMER_QUALITY_BRIDGE_VS_THEME_PRICE_SPIKE_HIGH_MAE_GUARD
selection_basis = docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket = Priority 0
round_schedule_status = coverage_index_selected
round_sector_consistency = pass
loop_objective = coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | high_MAE_guardrail | canonical_archetype_compression
output_file = e2r_stock_web_v12_residual_round_R2_loop_97_L2_AI_SEMICONDUCTOR_ELECTRONICS_C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY_research.md
```

This loop follows the v12 coverage-index scheduler. `C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY` is the thinnest Priority 0 archetype in the current index, with 14 rows and a 16-row gap to the 30-row minimum. The chosen scope is therefore R2 / L2 / C08. This MD does not change production scoring.

## 1. Current Calibrated Profile Assumption

```text
current_default_profile_proxy = e2r_2_1_stock_web_calibrated_proxy
rolling_profile_reference = e2r_2_2_rolling_calibrated
shadow_weight_only = true
production_scoring_changed = false
```

The tested residual is not the global Stage2 bonus itself. The residual question is narrower:

> In C08, should price/relative-strength signals from test socket, probe-card, and test-interface names be allowed to remain positive Stage2 unless there is explicit customer qualification, repeat consumable demand, or margin conversion evidence?

## 2. Round / Large Sector / Canonical Archetype Scope

- selected_round: `R2`
- large_sector_id: `L2_AI_SEMICONDUCTOR_ELECTRONICS`
- canonical_archetype_id: `C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY`
- fine_archetype_id: `TEST_SOCKET_PROBE_CARD_CUSTOMER_QUALITY_BRIDGE_VS_THEME_PRICE_SPIKE_HIGH_MAE_GUARD`

Canonical compression:

```text
ISC / TSE positive bridge cases
  -> C08 customer qualification / repeat-demand / test-interface quality bridge

TFE / Micro2Nano theme-price cases
  -> C08 price-only socket/probe-card label spike
  -> 4B watch or Stage1/weak-watch unless customer bridge is verified
```

## 3. Previous Coverage / Duplicate Avoidance Check

Current index snapshot:

- C08 rows before this loop: `14`
- need to 30: `16`
- priority bucket: `Priority 0`
- top covered C08 symbols in index: `098120`, `080580`, `058470`, `067310`, `092870`, `097800`

Selected symbols in this loop:

```text
095340 ISC
131290 티에스이
425420 티에프이
424980 마이크로투나노
```

Duplicate gate:

```text
hard_duplicate_key = canonical_archetype_id + symbol + trigger_type + entry_date
hard_duplicate_found = false
new_symbol_count = 4
reused_case_count = 0
```

## 4. Stock-Web OHLC Input / Price Source Validation

```text
price_source = Songdaiki/stock-web
manifest_path = atlas/manifest.json
schema_path = atlas/schema.json
price_basis = tradable_raw
price_adjustment_status = raw_unadjusted_marcap
stock_web_manifest_max_date = 2026-02-20
calibration_shard_root = atlas/ohlcv_tradable_by_symbol_year
```

Validation row:

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration"}
```

## 5. Historical Eligibility Gate

All selected entry rows are in 2024 tradable shards and have at least 180 forward trading rows before the stock-web manifest max date. Corporate action profile checks do not show 2024 entry-to-180D contamination for these windows.

| symbol | profile | 2024 entry window | corporate action status | usable |
|---|---|---|---|---|
| 095340 | atlas/symbol_profiles/095/095340.json | 2024-02-15~180D | profile has old candidate dates, not in 2024 entry window | true |
| 131290 | atlas/symbol_profiles/131/131290.json | 2024-02-22~180D | old candidate dates only | true |
| 425420 | atlas/symbol_profiles/425/425420.json | 2024-03-08~180D | no corporate action candidates | true |
| 424980 | atlas/symbol_profiles/424/424980.json | 2024-04-23~180D | no corporate action candidates | true |

## 6. Canonical Archetype Compression Map

| fine/deep pattern | canonical |
|---|---|
| test socket customer qualification + HBM/AI interface demand | C08 |
| probe-card / test-interface customer quality bridge | C08 |
| COK/socket/test-board vocabulary without durable customer evidence | C08 counterexample |
| MEMS probe-card price spike without revenue/margin bridge | C08 4B watch |

## 7. Case Selection Summary

| case_id | symbol | type | polarity | alignment |
|---|---|---|---|---|
| C08_R2L97_ISC_095340_20240215 | 095340 | high_mae_success | positive | early_signal_worked_but_requires_4B_high_MAE_guard |
| C08_R2L97_TSE_131290_20240222 | 131290 | structural_success_high_mae | positive | good_90D_MFE_with_later_high_MAE |
| C08_R2L97_TFE_425420_20240308 | 425420 | failed_rerating | counterexample | Stage2_should_be_blocked_without_customer_qualification_or_margin_bridge |
| C08_R2L97_MICRO2NANO_424980_20240423 | 424980 | 4B_overlay_success | counterexample | 4B_watch_should_override_positive_stage_without_non_price_bridge |

## 8. Positive vs Counterexample Balance

```text
positive_structural_success_or_high_MAE_success = 2
counterexample_or_failed_rerating = 2
4B_or_4C_case = 2
calibration_usable_case_count = 4
```

This loop is balanced enough for canonical-archetype shadow logic, but not for production promotion because all non-price evidence is `source_proxy_only`.

## 9. Evidence Source Map

| symbol | non-price evidence status | promotion status |
|---|---|---|
| 095340 | source_proxy_only customer/socket bridge | URL repair needed |
| 131290 | source_proxy_only probe-card/test-interface bridge | URL repair needed |
| 425420 | source_proxy_only socket/channel label with weak bridge | URL repair needed |
| 424980 | source_proxy_only MEMS probe-card spike | URL repair needed |

## 10. Price Data Source Map

| symbol | shard | profile |
|---|---|---|
| 095340 | atlas/ohlcv_tradable_by_symbol_year/095/095340/2024.csv | atlas/symbol_profiles/095/095340.json |
| 131290 | atlas/ohlcv_tradable_by_symbol_year/131/131290/2024.csv | atlas/symbol_profiles/131/131290.json |
| 425420 | atlas/ohlcv_tradable_by_symbol_year/425/425420/2024.csv | atlas/symbol_profiles/425/425420.json |
| 424980 | atlas/ohlcv_tradable_by_symbol_year/424/424980/2024.csv | atlas/symbol_profiles/424/424980.json |

## 11. Case-by-Case Trigger Grid

| symbol | company | trigger | entry | price | MFE30 | MAE30 | MFE90 | MAE90 | MFE180 | MAE180 | current verdict |
|---|---|---|---|---:|---:|---:|---:|---:|---:|---:|---|
| 095340 | ISC | Stage2-Actionable | 2024-02-15 | 76,400 | 41.36 | -9.82 | 41.36 | -17.15 | 41.36 | -46.2 | current_profile_too_late |
| 131290 | 티에스이 | Stage2-Actionable | 2024-02-22 | 61,300 | 12.89 | -13.05 | 43.23 | -14.85 | 43.23 | -37.93 | current_profile_correct_but_risk_overlay_too_late |
| 425420 | 티에프이 | Stage2 | 2024-03-08 | 38,850 | 13.13 | -15.96 | 13.13 | -36.94 | 13.13 | -62.11 | current_profile_false_positive |
| 424980 | 마이크로투나노 | Stage4B | 2024-04-23 | 18,200 | 30.49 | -26.81 | 30.49 | -50.0 | 30.49 | -50.0 | current_profile_4B_too_late |

## 12. Trigger-Level OHLC Backtest Tables

Interpretation:

- 095340 and 131290 show positive MFE, but the post-peak drawdown is too large to ignore.
- 425420 and 424980 show the exact failure family C08 needs more of: price/sector vocabulary without customer-quality bridge.

| symbol | entry | peak | peak_date | post-peak drawdown | verdict |
|---|---:|---:|---|---:|---|
| 095340 | 76,400 | 108,000 | 2024-03-28 | -61.94% | good early signal, 4B/high-MAE guard needed |
| 131290 | 61,300 | 87,800 | 2024-05-03 | -56.66% | good 90D signal, high-MAE guard needed |
| 425420 | 38,850 | 43,950 | 2024-03-21 | -66.51% | false Stage2 / price-only spike |
| 424980 | 18,200 | 23,750 | 2024-05-03 | -61.68% | price spike / 4B watch success |

## 13. Current Calibrated Profile Stress Test

| test | result |
|---|---|
| Stage2 bonus too high? | In C08, yes for price-only socket/probe-card vocabulary without customer qualification. |
| Yellow 75 too loose? | Not directly tested; issue is evidence bridge, not global total threshold. |
| Green 87/revision 55 too loose? | Kept. No Green loosening proposed. |
| price-only blowoff guard adequate? | Directionally right, but C08 needs earlier 4B-watch if no customer bridge. |
| full 4B non-price requirement adequate? | Kept for full 4B; price-only should be watch/overlay, not full positive. |
| hard 4C routing adequate? | Kept; this loop suggests bridge-missing high-MAE watch before hard 4C. |

## 14. Stage2 / Yellow / Green Comparison

No confirmed Stage3-Green labels are asserted from future outcome. Stage2/Stage2-Actionable is judged only on evidence available at entry date. The strongest learning is that C08 Stage2 should split:

```text
customer qualification + repeat demand + margin conversion present
  -> Stage2-Actionable can be retained

socket/probe/test label + relative strength only
  -> Stage1/weak-watch or 4B watch
```

## 15. 4B Local vs Full-Window Timing Audit

| symbol | local 4B evidence | full-window outcome | timing verdict |
|---|---|---|---|
| 095340 | price-only/valuation/positioning at 2024-03-28 | peak was full-window peak | 4B overlay needed |
| 131290 | late price spike into 2024-05-03 | peak was full-window peak | high-MAE overlay needed |
| 425420 | 2024-03-21 local peak | full-window peak | price-only local 4B was valid |
| 424980 | 2024-05-03 full-window peak | full-window peak | 4B watch should have fired |

## 16. 4C Protection Audit

No hard 4C production route is proposed. The appropriate label is:

```text
thesis_break_watch_only
```

If a later URL repair finds actual customer qualification failure, order cut, or repeated margin break, the TFE/Micro2Nano rows can be upgraded to hard 4C timing tests.

## 17. Sector-Specific Rule Candidate

No broad L2 sector rule is proposed. This should remain C08-specific.

## 18. Canonical-Archetype Rule Candidate

```text
candidate_axis = c08_customer_quality_bridge_required
scope = canonical_archetype:C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY
rule = Price/relative-strength C08 evidence cannot be treated as positive Stage2 unless at least one non-price bridge is present:
       customer qualification, repeat consumable demand, revenue conversion, or margin durability.
```

Companion overlay:

```text
candidate_axis = c08_price_only_spike_to_4b_watch
scope = canonical_archetype:C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY
rule = If C08 price spike has no non-price bridge, route to 4B-watch / Stage1 weak-watch, not positive Stage2.
```

## 19. Before / After Backtest Comparison

| profile | positive kept | false positive reduced | avg MFE90 | avg MAE90 | comment |
|---|---:|---:|---:|---:|---|
| P0 current proxy | 4/4 Stage2-like | 0/2 | 32.30% | -29.74% | lets price-only rows in too easily |
| P2 C08 bridge guard | 2/4 positive | 2/2 demoted | 42.30% for positives | -16.00% for positives | cleaner Stage2 sample |
| P3 4B watch guard | 2/4 positive + 2/4 watch | 2/2 watched | 21.81% all | -29.74% all | preserves risk overlay |

## 20. Score-Return Alignment Matrix

- 095340: aligned for early MFE, misaligned for risk if no 4B overlay.
- 131290: aligned for 90D MFE, misaligned for later drawdown.
- 425420: misaligned if positive Stage2; should be weak-watch.
- 424980: misaligned if positive Stage2; good 4B watch candidate.

## 21. Coverage Matrix

```json
{
  "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS",
  "canonical_archetype_id": "C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY",
  "fine_archetype_id": "TEST_SOCKET_PROBE_CARD_CUSTOMER_QUALITY_BRIDGE_VS_THEME_PRICE_SPIKE_HIGH_MAE_GUARD",
  "positive_case_count": 2,
  "counterexample_count": 2,
  "4B_case_count": 2,
  "4C_case_count": 0,
  "new_independent_case_count": 4,
  "reused_case_count": 0,
  "calibration_usable_trigger_count": 4,
  "representative_trigger_count": 4,
  "current_profile_error_count": 3,
  "sector_rule_candidate": "none",
  "canonical_rule_candidate": "c08_customer_quality_bridge_required + c08_price_only_spike_to_4b_watch",
  "coverage_gap_after_this_loop": "C08 moves from 14 to approximately 18 representative rows if all accepted"
}
```

## 22. Residual Contribution Summary

```text
new_independent_case_count: 4
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 4
new_canonical_archetype_count: 0
new_fine_archetype_count: 4
new_trigger_family_count: 3
tested_existing_calibrated_axes: stage2_actionable_evidence_bonus, full_4b_requires_non_price_evidence, hard_4c_thesis_break_routes_to_4c
residual_error_types_found: price_only_socket_probe_theme_false_positive, high_MAE_after_initial_MFE, 4B_watch_too_late_without_customer_bridge
new_axis_proposed: false
existing_axis_strengthened: full_4b_requires_non_price_evidence
existing_axis_weakened: none
existing_axis_kept: stage2_actionable_evidence_bonus, stage3_yellow_total_min, stage3_green_total_min, stage3_green_revision_min, hard_4c_thesis_break_routes_to_4c
sector_specific_rule_candidate: none
canonical_archetype_rule_candidate: c08_customer_quality_bridge_required; c08_price_only_spike_to_4b_watch
no_new_signal_reason: not_applicable

loop_contribution_label: canonical_archetype_rule_candidate
do_not_propose_new_weight_delta: true
do_not_propose_global_delta: true
promotion_blocker: source_proxy_only_non_price_evidence
```

This loop adds 4 new independent cases, 2 counterexamples, and 3 residual errors for R2/L2_AI_SEMICONDUCTOR_ELECTRONICS/C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY.

## 23. Validation Scope / Non-Validation Scope

Validation scope:

```text
- stock-web price row existence
- entry_date / entry_price
- MFE/MAE/peak/drawdown from observed tradable rows
- 180D forward availability
- corporate-action window sanity from profile
```

Non-validation scope:

```text
- exact evidence URL verification
- exact analyst report timestamp
- company-specific customer confirmation text
```

Rows are therefore calibration-usable for price-path residual research, but promotion-blocked until URL repair.

## 24. Shadow Weight Calibration

```jsonl
{"row_type": "shadow_weight", "axis": "c08_customer_quality_bridge_required", "scope": "canonical_archetype", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY", "baseline_value": "relative_strength_can_enter_stage2_if_sector_hot", "tested_value": "require_customer_qualification_repeat_demand_or_margin_conversion_for_positive_stage2", "delta": "guard_only", "reason": "Two positive cases had MFE but required 4B/high-MAE overlay; two theme-price cases collapsed without durable bridge.", "backtest_effect": "reduces Stage2 false positives for TFE/Micro2Nano while preserving ISC/TSE as watchable bridge cases", "trigger_ids": "C08_R2L97_095340_STAGE2A_20240215_CUSTOMER_QUALITY_SOCKET_BRIDGE|C08_R2L97_131290_STAGE2A_20240222_PROBE_CARD_TEST_INTERFACE_BRIDGE|C08_R2L97_425420_STAGE2_20240308_TEST_SOCKET_CHANNEL_FALSE_STAGE2|C08_R2L97_424980_STAGE4B_20240423_MEMS_PROBE_CARD_PRICE_SPIKE", "calibration_usable_count": 4, "new_independent_case_count": 4, "counterexample_count": 2, "confidence": "low", "proposal_type": "canonical_shadow_only", "notes": "source_proxy_only; do not promote before URL repair"}
{"row_type": "shadow_weight", "axis": "c08_price_only_spike_to_4b_watch", "scope": "canonical_archetype", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY", "baseline_value": "price-only spike may remain Stage2/Yellow until proof fails", "tested_value": "route price-only socket/probe-card spike to 4B watch unless non-price customer bridge is present", "delta": "+watch_guard", "reason": "TFE and Micro2Nano show local/full-window price spikes followed by MAE90 <= -36.9%.", "backtest_effect": "improves high-MAE guardrail for C08", "trigger_ids": "C08_R2L97_425420_STAGE2_20240308_TEST_SOCKET_CHANNEL_FALSE_STAGE2|C08_R2L97_424980_STAGE4B_20240423_MEMS_PROBE_CARD_PRICE_SPIKE", "calibration_usable_count": 2, "new_independent_case_count": 2, "counterexample_count": 2, "confidence": "low", "proposal_type": "canonical_shadow_only", "notes": "4B overlay only; not production patch"}
```

## 25. Machine-Readable Rows

### 25.1 price_source_validation

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration"}
```

### 25.2 case rows

```jsonl
{"row_type": "case", "case_id": "C08_R2L97_ISC_095340_20240215", "symbol": "095340", "company_name": "ISC", "round": "R2", "loop": "97", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY", "fine_archetype_id": "TEST_SOCKET_CUSTOMER_QUALITY_REPEAT_DEMAND_BRIDGE", "case_type": "high_mae_success", "positive_or_counterexample": "positive", "best_trigger": "C08_R2L97_095340_STAGE2A_20240215_CUSTOMER_QUALITY_SOCKET_BRIDGE", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "early_signal_worked_but_requires_4B_high_MAE_guard", "current_profile_verdict": "current_profile_too_late", "price_source": "Songdaiki/stock-web", "notes": "source_proxy_only; URL repair required before promotion"}
{"row_type": "case", "case_id": "C08_R2L97_TSE_131290_20240222", "symbol": "131290", "company_name": "티에스이", "round": "R2", "loop": "97", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY", "fine_archetype_id": "PROBE_CARD_TEST_INTERFACE_CUSTOMER_QUALITY_BRIDGE", "case_type": "structural_success_high_mae", "positive_or_counterexample": "positive", "best_trigger": "C08_R2L97_131290_STAGE2A_20240222_PROBE_CARD_TEST_INTERFACE_BRIDGE", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "good_90D_MFE_with_later_high_MAE", "current_profile_verdict": "current_profile_correct_but_risk_overlay_too_late", "price_source": "Songdaiki/stock-web", "notes": "source_proxy_only; URL repair required before promotion"}
{"row_type": "case", "case_id": "C08_R2L97_TFE_425420_20240308", "symbol": "425420", "company_name": "티에프이", "round": "R2", "loop": "97", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY", "fine_archetype_id": "TEST_SOCKET_CHANNEL_FALSE_STAGE2_NO_DURABLE_QUALIFICATION_BRIDGE", "case_type": "failed_rerating", "positive_or_counterexample": "counterexample", "best_trigger": "C08_R2L97_425420_STAGE2_20240308_TEST_SOCKET_CHANNEL_FALSE_STAGE2", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "Stage2_should_be_blocked_without_customer_qualification_or_margin_bridge", "current_profile_verdict": "current_profile_false_positive", "price_source": "Songdaiki/stock-web", "notes": "source_proxy_only; URL repair required before promotion"}
{"row_type": "case", "case_id": "C08_R2L97_MICRO2NANO_424980_20240423", "symbol": "424980", "company_name": "마이크로투나노", "round": "R2", "loop": "97", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY", "fine_archetype_id": "MEMS_PROBE_CARD_THEME_PRICE_SPIKE_VS_CUSTOMER_QUALITY_BRIDGE", "case_type": "4B_overlay_success", "positive_or_counterexample": "counterexample", "best_trigger": "C08_R2L97_424980_STAGE4B_20240423_MEMS_PROBE_CARD_PRICE_SPIKE", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "4B_watch_should_override_positive_stage_without_non_price_bridge", "current_profile_verdict": "current_profile_4B_too_late", "price_source": "Songdaiki/stock-web", "notes": "source_proxy_only; URL repair required before promotion"}
```

### 25.3 trigger rows

```jsonl
{"case_id": "C08_R2L97_ISC_095340_20240215", "trigger_id": "C08_R2L97_095340_STAGE2A_20240215_CUSTOMER_QUALITY_SOCKET_BRIDGE", "symbol": "095340", "company_name": "ISC", "fine_archetype_id": "TEST_SOCKET_CUSTOMER_QUALITY_REPEAT_DEMAND_BRIDGE", "case_type": "high_mae_success", "positive_or_counterexample": "positive", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-02-15", "entry_date": "2024-02-15", "entry_price": 76400, "evidence_available_at_that_date": "source_proxy_only: semiconductor test socket / customer qualification / HBM-AI interface demand narrative; exact filing/report URL repair required before promotion", "evidence_source": "source_proxy_only; stock-web price row verified; non-price URL pending", "stage2_evidence_fields": ["customer_or_order_quality", "capacity_or_volume_route", "relative_strength"], "stage3_evidence_fields": ["repeat_order_or_conversion", "durable_customer_confirmation"], "stage4b_evidence_fields": ["valuation_blowoff", "price_only_local_peak", "positioning_overheat"], "stage4c_evidence_fields": [], "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/095/095340/2024.csv", "profile_path": "atlas/symbol_profiles/095/095340.json", "MFE_30D_pct": 41.36, "MAE_30D_pct": -9.82, "MFE_90D_pct": 41.36, "MAE_90D_pct": -17.15, "MFE_180D_pct": 41.36, "MAE_180D_pct": -46.2, "peak_date": "2024-03-28", "peak_price": 108000, "drawdown_after_peak_pct": -61.94, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.92, "four_b_full_window_peak_proximity": 1.0, "four_b_timing_verdict": "good_local_peak_but_non_price_4B_needed", "four_b_evidence_type": ["price_only", "valuation_blowoff", "positioning_overheat"], "four_c_protection_label": "hard_4c_late_if_customer_quality_bridge_not_reconfirmed", "trigger_outcome_label": "positive_initial_MFE_high_MAE_after_blowoff", "current_profile_verdict": "current_profile_too_late", "score_return_alignment": "early_signal_worked_but_requires_4B_high_MAE_guard", "is_new_independent_case": true, "row_type": "trigger", "round": "R2", "loop": "97", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY", "sector": "AI / semiconductor / electronics / test socket / probe card", "primary_archetype": "semi test socket customer quality bridge", "loop_objective": "coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | high_MAE_guardrail | canonical_archetype_compression", "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "forward_window_trading_days": 180, "calibration_usable": true, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "C08_R2L97_ISC_095340_20240215", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "evidence_url_pending": true, "source_proxy_only": true}
{"case_id": "C08_R2L97_TSE_131290_20240222", "trigger_id": "C08_R2L97_131290_STAGE2A_20240222_PROBE_CARD_TEST_INTERFACE_BRIDGE", "symbol": "131290", "company_name": "티에스이", "fine_archetype_id": "PROBE_CARD_TEST_INTERFACE_CUSTOMER_QUALITY_BRIDGE", "case_type": "structural_success_high_mae", "positive_or_counterexample": "positive", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-02-22", "entry_date": "2024-02-22", "entry_price": 61300, "evidence_available_at_that_date": "source_proxy_only: test interface / probe card / customer quality bridge narrative; exact report URL repair required", "evidence_source": "source_proxy_only; stock-web price row verified; non-price URL pending", "stage2_evidence_fields": ["customer_or_order_quality", "relative_strength", "early_revision_signal"], "stage3_evidence_fields": ["repeat_order_or_conversion", "financial_visibility"], "stage4b_evidence_fields": ["price_only_local_peak", "positioning_overheat"], "stage4c_evidence_fields": [], "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/131/131290/2024.csv", "profile_path": "atlas/symbol_profiles/131/131290.json", "MFE_30D_pct": 12.89, "MAE_30D_pct": -13.05, "MFE_90D_pct": 43.23, "MAE_90D_pct": -14.85, "MFE_180D_pct": 43.23, "MAE_180D_pct": -37.93, "peak_date": "2024-05-03", "peak_price": 87800, "drawdown_after_peak_pct": -56.66, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.55, "four_b_full_window_peak_proximity": 1.0, "four_b_timing_verdict": "late_full_window_peak_after_stage2_but_high_MAE_requires_bridge_decay_watch", "four_b_evidence_type": ["price_only", "positioning_overheat"], "four_c_protection_label": "watch_only_without_thesis_break", "trigger_outcome_label": "positive_with_large_MFE_but_later_drawdown", "current_profile_verdict": "current_profile_correct_but_risk_overlay_too_late", "score_return_alignment": "good_90D_MFE_with_later_high_MAE", "is_new_independent_case": true, "row_type": "trigger", "round": "R2", "loop": "97", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY", "sector": "AI / semiconductor / electronics / test socket / probe card", "primary_archetype": "semi test socket customer quality bridge", "loop_objective": "coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | high_MAE_guardrail | canonical_archetype_compression", "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "forward_window_trading_days": 180, "calibration_usable": true, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "C08_R2L97_TSE_131290_20240222", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "evidence_url_pending": true, "source_proxy_only": true}
{"case_id": "C08_R2L97_TFE_425420_20240308", "trigger_id": "C08_R2L97_425420_STAGE2_20240308_TEST_SOCKET_CHANNEL_FALSE_STAGE2", "symbol": "425420", "company_name": "티에프이", "fine_archetype_id": "TEST_SOCKET_CHANNEL_FALSE_STAGE2_NO_DURABLE_QUALIFICATION_BRIDGE", "case_type": "failed_rerating", "positive_or_counterexample": "counterexample", "trigger_type": "Stage2", "trigger_date": "2024-03-08", "entry_date": "2024-03-08", "entry_price": 38850, "evidence_available_at_that_date": "source_proxy_only: COK/socket/test-board vocabulary and price momentum without durable customer qualification or margin conversion confirmation", "evidence_source": "source_proxy_only; stock-web price row verified; non-price URL pending", "stage2_evidence_fields": ["relative_strength"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["price_only_local_peak", "valuation_blowoff", "positioning_overheat"], "stage4c_evidence_fields": ["thesis_evidence_broken"], "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/425/425420/2024.csv", "profile_path": "atlas/symbol_profiles/425/425420.json", "MFE_30D_pct": 13.13, "MAE_30D_pct": -15.96, "MFE_90D_pct": 13.13, "MAE_90D_pct": -36.94, "MFE_180D_pct": 13.13, "MAE_180D_pct": -62.11, "peak_date": "2024-03-21", "peak_price": 43950, "drawdown_after_peak_pct": -66.51, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 1.0, "four_b_full_window_peak_proximity": 1.0, "four_b_timing_verdict": "price_only_local_peak_was_full_window_peak", "four_b_evidence_type": ["price_only", "positioning_overheat"], "four_c_protection_label": "hard_4c_late_after_bridge_missing_and_high_MAE", "trigger_outcome_label": "counterexample_high_MAE_no_customer_quality_bridge", "current_profile_verdict": "current_profile_false_positive", "score_return_alignment": "Stage2_should_be_blocked_without_customer_qualification_or_margin_bridge", "is_new_independent_case": true, "row_type": "trigger", "round": "R2", "loop": "97", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY", "sector": "AI / semiconductor / electronics / test socket / probe card", "primary_archetype": "semi test socket customer quality bridge", "loop_objective": "coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | high_MAE_guardrail | canonical_archetype_compression", "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "forward_window_trading_days": 180, "calibration_usable": true, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "C08_R2L97_TFE_425420_20240308", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "evidence_url_pending": true, "source_proxy_only": true}
{"case_id": "C08_R2L97_MICRO2NANO_424980_20240423", "trigger_id": "C08_R2L97_424980_STAGE4B_20240423_MEMS_PROBE_CARD_PRICE_SPIKE", "symbol": "424980", "company_name": "마이크로투나노", "fine_archetype_id": "MEMS_PROBE_CARD_THEME_PRICE_SPIKE_VS_CUSTOMER_QUALITY_BRIDGE", "case_type": "4B_overlay_success", "positive_or_counterexample": "counterexample", "trigger_type": "Stage4B", "trigger_date": "2024-04-23", "entry_date": "2024-04-23", "entry_price": 18200, "evidence_available_at_that_date": "source_proxy_only: MEMS probe-card theme spike; exact customer qualification and repeat-demand evidence pending", "evidence_source": "source_proxy_only; stock-web price row verified; non-price URL pending", "stage2_evidence_fields": ["relative_strength"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["price_only_local_peak", "valuation_blowoff", "positioning_overheat"], "stage4c_evidence_fields": ["thesis_evidence_broken"], "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/424/424980/2024.csv", "profile_path": "atlas/symbol_profiles/424/424980.json", "MFE_30D_pct": 30.49, "MAE_30D_pct": -26.81, "MFE_90D_pct": 30.49, "MAE_90D_pct": -50.0, "MFE_180D_pct": 30.49, "MAE_180D_pct": -50.0, "peak_date": "2024-05-03", "peak_price": 23750, "drawdown_after_peak_pct": -61.68, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.62, "four_b_full_window_peak_proximity": 1.0, "four_b_timing_verdict": "good_4B_watch_candidate_when_spike_lacks_non_price_customer_bridge", "four_b_evidence_type": ["price_only", "valuation_blowoff", "positioning_overheat"], "four_c_protection_label": "hard_4c_late_if_revenue_bridge_not_confirmed", "trigger_outcome_label": "price_spike_counterexample_high_MAE", "current_profile_verdict": "current_profile_4B_too_late", "score_return_alignment": "4B_watch_should_override_positive_stage_without_non_price_bridge", "is_new_independent_case": true, "row_type": "trigger", "round": "R2", "loop": "97", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY", "sector": "AI / semiconductor / electronics / test socket / probe card", "primary_archetype": "semi test socket customer quality bridge", "loop_objective": "coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | high_MAE_guardrail | canonical_archetype_compression", "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "forward_window_trading_days": 180, "calibration_usable": true, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "C08_R2L97_MICRO2NANO_424980_20240423", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "evidence_url_pending": true, "source_proxy_only": true}
```

### 25.4 score_simulation rows

```jsonl
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "C08_R2L97_ISC_095340_20240215", "trigger_id": "C08_R2L97_095340_STAGE2A_20240215_CUSTOMER_QUALITY_SOCKET_BRIDGE", "symbol": "095340", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY", "raw_component_scores_before": {"contract_score": 2, "backlog_visibility_score": 4, "margin_bridge_score": 3, "revision_score": 4, "relative_strength_score": 7, "customer_quality_score": 8, "policy_or_regulatory_score": 0, "valuation_repricing_score": 5, "execution_risk_score": 2, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 76, "stage_label_before": "Stage2-Actionable", "raw_component_scores_after": {"contract_score": 2, "backlog_visibility_score": 5, "margin_bridge_score": 4, "revision_score": 4, "relative_strength_score": 6, "customer_quality_score": 9, "policy_or_regulatory_score": 0, "valuation_repricing_score": 4, "execution_risk_score": 3, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 78, "stage_label_after": "Stage2-Actionable", "changed_components": ["customer_quality_score", "execution_risk_score", "valuation_repricing_score"], "component_delta_explanation": "C08 should require customer qualification/repeat demand/margin conversion; price-only relative strength is demoted to watch/4B.", "MFE_90D_pct": 41.36, "MAE_90D_pct": -17.15, "score_return_alignment_label": "early_signal_worked_but_requires_4B_high_MAE_guard", "current_profile_verdict": "current_profile_too_late"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "C08_R2L97_TSE_131290_20240222", "trigger_id": "C08_R2L97_131290_STAGE2A_20240222_PROBE_CARD_TEST_INTERFACE_BRIDGE", "symbol": "131290", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY", "raw_component_scores_before": {"contract_score": 2, "backlog_visibility_score": 4, "margin_bridge_score": 3, "revision_score": 4, "relative_strength_score": 7, "customer_quality_score": 8, "policy_or_regulatory_score": 0, "valuation_repricing_score": 5, "execution_risk_score": 2, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 76, "stage_label_before": "Stage2-Actionable", "raw_component_scores_after": {"contract_score": 2, "backlog_visibility_score": 5, "margin_bridge_score": 4, "revision_score": 4, "relative_strength_score": 6, "customer_quality_score": 9, "policy_or_regulatory_score": 0, "valuation_repricing_score": 4, "execution_risk_score": 3, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 78, "stage_label_after": "Stage2-Actionable", "changed_components": ["customer_quality_score", "execution_risk_score", "valuation_repricing_score"], "component_delta_explanation": "C08 should require customer qualification/repeat demand/margin conversion; price-only relative strength is demoted to watch/4B.", "MFE_90D_pct": 43.23, "MAE_90D_pct": -14.85, "score_return_alignment_label": "good_90D_MFE_with_later_high_MAE", "current_profile_verdict": "current_profile_correct_but_risk_overlay_too_late"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "C08_R2L97_TFE_425420_20240308", "trigger_id": "C08_R2L97_425420_STAGE2_20240308_TEST_SOCKET_CHANNEL_FALSE_STAGE2", "symbol": "425420", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 1, "relative_strength_score": 8, "customer_quality_score": 2, "policy_or_regulatory_score": 0, "valuation_repricing_score": 7, "execution_risk_score": 6, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 72, "stage_label_before": "Stage2", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 1, "relative_strength_score": 5, "customer_quality_score": 1, "policy_or_regulatory_score": 0, "valuation_repricing_score": 3, "execution_risk_score": 8, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 61, "stage_label_after": "Stage1/weak-watch", "changed_components": ["customer_quality_score", "execution_risk_score", "valuation_repricing_score"], "component_delta_explanation": "C08 should require customer qualification/repeat demand/margin conversion; price-only relative strength is demoted to watch/4B.", "MFE_90D_pct": 13.13, "MAE_90D_pct": -36.94, "score_return_alignment_label": "Stage2_should_be_blocked_without_customer_qualification_or_margin_bridge", "current_profile_verdict": "current_profile_false_positive"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "C08_R2L97_MICRO2NANO_424980_20240423", "trigger_id": "C08_R2L97_424980_STAGE4B_20240423_MEMS_PROBE_CARD_PRICE_SPIKE", "symbol": "424980", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 1, "relative_strength_score": 8, "customer_quality_score": 2, "policy_or_regulatory_score": 0, "valuation_repricing_score": 7, "execution_risk_score": 6, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 72, "stage_label_before": "Stage2", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 1, "relative_strength_score": 5, "customer_quality_score": 1, "policy_or_regulatory_score": 0, "valuation_repricing_score": 3, "execution_risk_score": 8, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 61, "stage_label_after": "Stage1/weak-watch", "changed_components": ["customer_quality_score", "execution_risk_score", "valuation_repricing_score"], "component_delta_explanation": "C08 should require customer qualification/repeat demand/margin conversion; price-only relative strength is demoted to watch/4B.", "MFE_90D_pct": 30.49, "MAE_90D_pct": -50.0, "score_return_alignment_label": "4B_watch_should_override_positive_stage_without_non_price_bridge", "current_profile_verdict": "current_profile_4B_too_late"}
```

### 25.5 residual_contribution row

```jsonl
{"row_type": "residual_contribution", "round": "R2", "loop": "97", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY", "new_independent_case_count": 4, "reused_case_count": 0, "new_symbol_count": 4, "same_archetype_new_symbol_count": 4, "same_archetype_new_trigger_family_count": 3, "new_trigger_family_count": 3, "positive_case_count": 2, "counterexample_count": 2, "current_profile_error_count": 3, "diversity_score_summary": "+4 new symbols, +2 counterexamples, +2 high-MAE/4B paths; no hard duplicate observed in index", "tested_existing_calibrated_axes": ["stage2_actionable_evidence_bonus", "full_4b_requires_non_price_evidence", "hard_4c_thesis_break_routes_to_4c"], "residual_error_types_found": ["price_only_socket_probe_theme_false_positive", "high_MAE_after_initial_MFE", "4B_watch_too_late_without_customer_bridge"], "loop_contribution_label": "canonical_archetype_rule_candidate", "do_not_propose_new_weight_delta": true, "do_not_propose_global_delta": true}
```

## 26. Deferred Coding Agent Handoff Prompt

### Purpose

You are now in the repository implementation phase. The attached Markdown files are v12 post-calibrated residual research outputs produced using the Songdaiki/stock-web OHLC atlas.

These MDs are not live candidate research. They are historical calibration research designed to extend the already-applied e2r_2_1/e2r_2_2 calibrated profile.

Do not blindly apply every shadow row.

### Price source context

- Primary historical price source used by this research MD: Songdaiki/stock-web.
- Price basis: tradable_raw.
- Price adjustment status: raw_unadjusted_marcap.
- Price shard pattern: atlas/ohlcv_tradable_by_symbol_year/<prefix>/<ticker>/<year>.csv.
- Symbol profile pattern: atlas/symbol_profiles/<prefix>/<ticker>.json.

### Rules

- Use only `calibration_usable=true` rows for quantitative calibration.
- Do not promote this loop directly because `source_proxy_only=true` and `evidence_url_pending=true`.
- Keep the finding as a C08 canonical-archetype shadow guard:
  - require customer qualification / repeat demand / revenue conversion / margin durability for positive Stage2.
  - route price-only C08 socket/probe-card spikes to 4B-watch or Stage1/weak-watch.
- Do not loosen Stage3-Green total or revision thresholds.
- Do not create a global L2 rule from this loop alone.

## 27. Next Round State

```text
completed_round = R2
completed_loop = 97
selection_basis = docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket = Priority 0
next_recommended_archetypes = C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY, C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF, C01_ORDER_BACKLOG_MARGIN_BRIDGE, C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH
round_schedule_status = coverage_index_selected
round_sector_consistency = pass
```

## 28. Source Notes

Stock-Web files used:

```text
https://github.com/Songdaiki/stock-web/blob/main/atlas/manifest.json
https://github.com/Songdaiki/stock-web/blob/main/atlas/schema.json
https://github.com/Songdaiki/stock-web/blob/main/atlas/symbol_profiles/095/095340.json
https://github.com/Songdaiki/stock-web/blob/main/atlas/symbol_profiles/131/131290.json
https://github.com/Songdaiki/stock-web/blob/main/atlas/symbol_profiles/425/425420.json
https://github.com/Songdaiki/stock-web/blob/main/atlas/symbol_profiles/424/424980.json
https://github.com/Songdaiki/stock-web/blob/main/atlas/ohlcv_tradable_by_symbol_year/095/095340/2024.csv
https://github.com/Songdaiki/stock-web/blob/main/atlas/ohlcv_tradable_by_symbol_year/131/131290/2024.csv
https://github.com/Songdaiki/stock-web/blob/main/atlas/ohlcv_tradable_by_symbol_year/425/425420/2024.csv
https://github.com/Songdaiki/stock-web/blob/main/atlas/ohlcv_tradable_by_symbol_year/424/424980/2024.csv
```

Non-price evidence limitation:

```text
All company/archetype narratives in this loop are source_proxy_only.
Before any promotion, replace source_proxy_only with exact filings/reports/news URLs and rerun validation.
```
