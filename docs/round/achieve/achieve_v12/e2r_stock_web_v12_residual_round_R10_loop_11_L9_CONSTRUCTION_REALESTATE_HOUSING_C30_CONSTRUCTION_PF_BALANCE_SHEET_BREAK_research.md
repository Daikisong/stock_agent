# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```yaml
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
scheduled_round: R10
scheduled_loop: 11
round_schedule_status: valid
round_sector_consistency: pass
completed_round: R10
completed_loop: 11
computed_next_round: R11
computed_next_loop: 11
large_sector_id: L9_CONSTRUCTION_REALESTATE_HOUSING
canonical_archetype_id: C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK
fine_archetype_id: PF_BALANCE_SHEET_SURVIVOR_VS_VALUATION_BOUNCE_GUARD
loop_objective:
  - coverage_gap_fill
  - counterexample_mining
  - sector_specific_rule_discovery
  - canonical_archetype_compression
  - 4B_non_price_requirement_stress_test
  - 4C_thesis_break_timing_test
price_source: Songdaiki/stock-web
stock_web_manifest_max_date: 2026-02-20
production_scoring_changed: false
shadow_weight_only: true
handoff_prompt_embedded: true
handoff_prompt_executed_now: false
```

This loop adds 5 new independent cases, 4 counterexamples including one narrative-only liquidity-support guard, and 3 current-profile residual errors for R10/L9_CONSTRUCTION_REALESTATE_HOUSING/C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK.

## 1. Current Calibrated Profile Assumption

The current proxy is `e2r_2_1_stock_web_calibrated_proxy`, not the old E2R 2.0 baseline.

Already-applied global axes are treated as existing controls, not re-proposed:

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

This R10/C30 loop does not repeat the old conclusion that Stage2 is earlier than Green. It tests a narrower residual: **2024 construction/PF relief bounces can separate into two species**. Some are survivor Stage2/Yellow entries; others are valuation or price-only bounces that should be blocked from Green or routed to 4B overlay.

## 2. Round / Large Sector / Canonical Archetype Scope

| Field | Value |
|---|---|
| round | R10 |
| loop | 11 |
| large_sector_id | `L9_CONSTRUCTION_REALESTATE_HOUSING` |
| canonical_archetype_id | `C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK` |
| fine_archetype_id | `PF_BALANCE_SHEET_SURVIVOR_VS_VALUATION_BOUNCE_GUARD` |
| scheduled next | `R11 / loop 11` |

R10 maps to `L9_CONSTRUCTION_REALESTATE_HOUSING`. The selected canonical archetype remains `C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK`, but the loop deliberately avoids the loop10 set of HDC현대산업개발, 현대건설, DL이앤씨, GS건설, and 태영건설.

## 3. Previous Coverage / Duplicate Avoidance Check

Allowed stock_agent artifact used: `reports/e2r_calibration/by_round/R10.md`.

R10 already has 93 representative triggers and 28 unique cases in the accumulated calibration report. It includes Stage2, Stage2-Actionable, Stage3-Green, Stage3-Yellow, Stage4B, Stage4C, and 4C-late rows. Therefore this loop does not re-argue the global axes. It fills a C30 residual gap using new symbols:

```text
same_canonical_archetype_research = allowed
same_symbol_same_trigger_date_research = avoided
new_symbol_count = 6
new_independent_case_count = 5
reused_case_count = 0
```

## 4. Stock-Web OHLC Input / Price Source Validation

Manifest values used:

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
markets = KONEX | KOSDAQ | KOSDAQ GLOBAL | KOSPI
calibration_shard_root = atlas/ohlcv_tradable_by_symbol_year
raw_shard_root = atlas/ohlcv_raw_by_symbol_year
schema_path = atlas/schema.json
universe_path = atlas/universe/all_symbols.csv
```

The schema defines `tradable_raw` as the calibration basis and the calculation formulas as:

```text
MFE_N_pct = (max high from entry_date through N tradable rows / entry_price - 1) * 100
MAE_N_pct = (min low from entry_date through N tradable rows / entry_price - 1) * 100
```

## 5. Historical Eligibility Gate

| case_id | symbol | entry_date | clean 180D? | usable? | block reason |
|---|---:|---:|---:|---:|---|
| R10L11-C30-DAEWOO-20240125 | 047040 | 2024-01-25 | yes | yes | none |
| R10L11-C30-KYERYONG-20240125 | 013580 | 2024-01-25 | yes | yes | none |
| R10L11-C30-KOLON-20240125 | 003070 | 2024-01-25 | yes | yes | none |
| R10L11-C30-KUMHO-20240125 | 002990 | 2024-01-25 | yes | yes | none |
| R10L11-C30-DONGBU-20240125 | 005960 | 2024-01-25 | yes | yes | none |
| R10L11-C30-SHINSEGAE-20240207 | 034300 | 2024-02-07 | no | no | corporate_action_candidate_adjacent_to_trigger; inactive_or_delisted_like_forward_context |

Quantitative calibration uses the first five cases. The Shinsegae Construction row remains narrative-only because the trigger is adjacent to a stock-web corporate-action candidate and later inactive/delisted-like context.

## 6. Canonical Archetype Compression Map

| fine_archetype_id | canonical_archetype_id | compression note |
|---|---|---|
| PF_BALANCE_SHEET_SURVIVOR_VS_VALUATION_BOUNCE_GUARD | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | Separates survivor Stage2/Yellow from false Green in C30. |
| regional_survivor_recovery_with_low_MAE | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | 계룡건설-like case: not a spectacular rerating, but clean low-MAE Stage2/Yellow. |
| large_contractor_survivor_recovery_not_green | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | 대우건설-like case: policy/sector recovery works, but PF/housing margin clearance is still required for Green. |
| valuation_bounce_failed_rerating | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | 금호건설/동부건설-like cases: valuation or policy bounce without durable margin/PF bridge. |
| price_only_spike_requires_4B_overlay | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | 코오롱글로벌-like case: large MFE is not Green evidence unless non-price bridge confirms it. |
| liquidity_support_near_corporate_action_blocked | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | 신세계건설-like narrative guard: useful for thesis-break logic, not weight calibration. |

## 7. Case Selection Summary

| case_id | symbol | company | role | usable | current_profile_verdict |
|---|---:|---|---|---:|---|
| R10L11-C30-DAEWOO-20240125 | 047040 | 대우건설 | stage2_promote_candidate | true | current_profile_correct |
| R10L11-C30-KYERYONG-20240125 | 013580 | 계룡건설 | structural_success | true | current_profile_correct |
| R10L11-C30-KOLON-20240125 | 003070 | 코오롱글로벌 | high_mae_success | true | current_profile_4B_too_late |
| R10L11-C30-KUMHO-20240125 | 002990 | 금호건설 | false_positive_green | true | current_profile_false_positive |
| R10L11-C30-DONGBU-20240125 | 005960 | 동부건설 | failed_rerating | true | current_profile_false_positive |
| R10L11-C30-SHINSEGAE-20240207 | 034300 | 신세계건설 | narrative_only | false | current_profile_data_insufficient |

## 8. Positive vs Counterexample Balance

```text
positive_case_count = 2
counterexample_count = 4
calibration_usable_case_count = 5
narrative_only_case_count = 1
```

Positive cases are not interpreted as automatic Green. In C30 the bridge is like a building inspection: a clean lobby is not the same as sound foundations. The Stage2/Yellow label can buy observation time, but Green requires PF/liquidity/legal and margin clearance.

## 9. Evidence Source Map

| symbol | evidence family | Stage2 evidence | Stage3 evidence | 4B evidence | 4C evidence |
|---:|---|---|---|---|---|
| 047040 | large contractor survivor bounce after PF/real-estate relief watch | public_event_or_disclosure, relative_strength, policy_or_regulatory_optionality | financial_visibility, multiple_public_sources | price_only_local_peak | - |
| 013580 | regional survivor / low-MAE recovery | public_event_or_disclosure, relative_strength, policy_or_regulatory_optionality | financial_visibility, low_red_team_risk | price_only_local_peak | - |
| 003070 | price spike without sufficient PF/margin bridge | relative_strength, policy_or_regulatory_optionality | multiple_public_sources | valuation_blowoff, positioning_overheat, price_only_local_peak | - |
| 002990 | valuation bounce failed by PF/margin risk | public_event_or_disclosure, relative_strength | valuation_repricing_score | margin_or_backlog_slowdown, capital_raise_or_overhang | thesis_evidence_broken |
| 005960 | low-MFE failed rerating | relative_strength, policy_or_regulatory_optionality | valuation_repricing_score | margin_or_backlog_slowdown | - |
| 034300 | liquidity support near capital/stock-base shift | - | - | capital_raise_or_overhang, legal_or_regulatory_block | thesis_evidence_broken, accounting_or_trust_break |

## 10. Price Data Source Map

| symbol | company | price_shard_path | profile_path |
|---:|---|---|---|
| 047040 | 대우건설 | `atlas/ohlcv_tradable_by_symbol_year/047/047040/2024.csv` | `atlas/symbol_profiles/047/047040.json` |
| 013580 | 계룡건설 | `atlas/ohlcv_tradable_by_symbol_year/013/013580/2024.csv` | `atlas/symbol_profiles/013/013580.json` |
| 003070 | 코오롱글로벌 | `atlas/ohlcv_tradable_by_symbol_year/003/003070/2024.csv` | `atlas/symbol_profiles/003/003070.json` |
| 002990 | 금호건설 | `atlas/ohlcv_tradable_by_symbol_year/002/002990/2024.csv` | `atlas/symbol_profiles/002/002990.json` |
| 005960 | 동부건설 | `atlas/ohlcv_tradable_by_symbol_year/005/005960/2024.csv` | `atlas/symbol_profiles/005/005960.json` |
| 034300 | 신세계건설 | `atlas/ohlcv_tradable_by_symbol_year/034/034300/2024.csv` | `atlas/symbol_profiles/034/034300.json` |

## 11. Case-by-Case Trigger Grid

| trigger_id | trigger_type | trigger_date | entry_date | entry_price | current_profile_verdict | trigger_outcome_label |
|---|---|---:|---:|---:|---|---|
| R10L11-C30-DAEWOO-STAGE2-20240125 | Stage2-Actionable | 2024-01-25 | 2024-01-25 | 3925 | current_profile_correct | survivor_stage2_recovery_not_green |
| R10L11-C30-KYERYONG-STAGE2-20240125 | Stage2-Actionable | 2024-01-25 | 2024-01-25 | 13400 | current_profile_correct | regional_survivor_stage2_yellow_success |
| R10L11-C30-KOLON-STAGE2-20240125 | Stage2-Actionable | 2024-01-25 | 2024-01-25 | 9130 | current_profile_4B_too_late | price_only_spike_requires_4B_overlay_not_green |
| R10L11-C30-KUMHO-STAGE2-20240125 | Stage2-Actionable | 2024-01-25 | 2024-01-25 | 5030 | current_profile_false_positive | PF_margin_bridge_absent_false_positive |
| R10L11-C30-DONGBU-STAGE2-20240125 | Stage2-Actionable | 2024-01-25 | 2024-01-25 | 5250 | current_profile_false_positive | low_MFE_sideways_failed_rerating |
| R10L11-C30-KOLON-4B-20240620 | Stage4B | 2024-06-20 | 2024-06-20 | 15740 | current_profile_4B_too_late | 4B_overlay_success_price_only_not_Green |
| R10L11-C30-SHINSEGAE-4C-WATCH-20240207 | Stage4C-watch | 2024-02-07 | 2024-02-07 | 11460 | current_profile_data_insufficient | capital_support_near_corporate_action_blocked |

## 12. Trigger-Level OHLC Backtest Tables

| symbol | entry | entry_price | MFE30 | MAE30 | MFE90 | MAE90 | MFE180 | MAE180 | peak_date | peak_price | drawdown_after_peak |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 047040 | 2024-01-25 | 3925 | 6.5 | -3.18 | 6.5 | -8.79 | 26.5 | -9.68 | 2024-07-18 | 4965 | -28.0 |
| 013580 | 2024-01-25 | 13400 | 15.15 | -2.09 | 15.15 | -5.75 | 15.6 | -5.75 | 2024-07-17 | 15490 | -17.37 |
| 003070 | 2024-01-25 | 9130 | 17.2 | -3.61 | 76.45 | -10.51 | 76.45 | -10.51 | 2024-06-21 | 16110 | -47.24 |
| 002990 | 2024-01-25 | 5030 | 4.97 | -4.57 | 4.97 | -27.53 | 4.97 | -43.34 | 2024-02-01 | 5280 | -46.97 |
| 005960 | 2024-01-25 | 5250 | 4.76 | -3.24 | 4.76 | -9.52 | 4.76 | -9.52 | 2024-02-19 | 5500 | -18.64 |

### 4B overlay row

| trigger_id | symbol | entry | entry_price | MFE90 | MAE90 | peak_date | peak_price | local proximity | full-window proximity | verdict |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| R10L11-C30-KOLON-4B-20240620 | 003070 | 2024-06-20 | 15740 | 2.35 | -47.24 | 2024-06-21 | 16110 | 0.95 | 0.95 | price-only spike is 4B overlay, not Green evidence |

## 13. Current Calibrated Profile Stress Test

| symbol | verdict | explanation |
|---:|---|---|
| 047040 | current_profile_correct | Stage2/Yellow recovery is allowed; Green requires PF/housing margin bridge. |
| 013580 | current_profile_correct | Low-MAE survivor case supports Stage2/Yellow holdout. |
| 003070 | current_profile_4B_too_late | Huge MFE would tempt outcome-looking Green, but price-only spike needs 4B overlay treatment. |
| 002990 | current_profile_false_positive | Valuation/policy bounce had tiny MFE and deep 180D MAE. |
| 005960 | current_profile_false_positive | Low-MFE sideways path argues against Yellow/Green promotion. |
| 034300 | current_profile_data_insufficient | Useful narrative 4C/liquidity guard, blocked from quantitative calibration. |

### Existing calibrated axis assessment

| existing axis | result in this loop |
|---|---|
| stage2_actionable_evidence_bonus | existing_axis_kept; useful for 047040/013580 only under PF/legal guard |
| stage3_yellow_total_min | existing_axis_kept |
| stage3_green_total_min | existing_axis_strengthened locally: C30 Green needs PF/liquidity/margin bridge |
| stage3_green_revision_min | existing_axis_kept |
| price_only_blowoff_blocks_positive_stage | existing_axis_strengthened by 003070 price-spike case |
| full_4b_requires_non_price_evidence | existing_axis_strengthened; price-only spike can be overlay but not full positive rerating evidence |
| hard_4c_thesis_break_routes_to_4c | existing_axis_kept; 034300 remains narrative-only due data/CA caveat |

## 14. Stage2 / Yellow / Green Comparison

C30 should behave less like an ordinary orderbook cycle and more like a structural inspection. Stage2/Yellow can be assigned from sector recovery, liquidity survival, and relative strength. Green requires the missing floor beam: PF/legal/margin bridge.

```text
047040: Stage2 works; Green would be too early.
013580: Yellow holdout works; Green still needs more financial visibility.
003070: price spike makes Green look attractive after the fact, but it is a 4B overlay test, not entry proof.
002990/005960: valuation bounce without PF bridge creates false positive risk.
```

`green_lateness_ratio` is not computed as a single value because no confirmed non-price Stage3-Green trigger exists in the selected C30 samples. Each representative trigger row therefore stores `not_applicable:no_confirmed_Stage3_Green_trigger`.

## 15. 4B Local vs Full-window Timing Audit

| case | Stage2 entry | 4B entry | full-window peak | local proximity | full-window proximity | verdict |
|---|---:|---:|---:|---:|---:|---|
| 003070 코오롱글로벌 | 9130 | 15740 | 16110 | 0.95 | 0.95 | good peak proximity, but price-only; not proof of full positive thesis |
| 047040 대우건설 | 3925 | n/a | 4965 | n/a | n/a | local peak visible, but not a full 4B without non-price PF/margin slowdown evidence |
| 013580 계룡건설 | 13400 | n/a | 15490 | n/a | n/a | controlled Stage2/Yellow recovery, no full 4B signal |

## 16. 4C Protection Audit

| case | 4C label | protection comment |
|---|---|---|
| 034300 신세계건설 | thesis_break_watch_only | Quantitatively blocked because the capital/liquidity support trigger is adjacent to stock-web corporate-action candidate; useful only as narrative C30 guard. |
| 002990 금호건설 | hard_4c_late_watch | 180D MAE suggests the profile should not wait for confirmed default/workout language before blocking Green. |
| 005960 동부건설 | thesis_break_watch_only | Weak rerating and low MFE argue for watch-only rather than positive promotion. |

## 17. Sector-Specific Rule Candidate

```text
rule_scope = canonical_archetype_specific
rule_name = C30_pf_liquidity_margin_bridge_required_for_green
proposal_type = shadow_only
```

A C30 trigger can remain Stage2/Yellow on policy relief or survivor relative strength, but cannot be Green unless at least one of these non-price bridges exists:

```text
- PF exposure visibly declining or refinanced on acceptable terms
- liquidity support is confirmed without corporate-action contamination
- housing/project margin bridge is visible in financials
- legal/quality/workout thesis break is absent
- valuation or price spike is supported by non-price evidence, not only momentum
```

## 18. Canonical-Archetype Rule Candidate

```text
canonical_archetype_id = C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK
candidate_rule = price_only_spike_is_4B_overlay_not_green
```

The 003070 case is important because it could fool a backtest if Green is assigned after seeing the MFE. Its MFE was real, but the evidence structure was not. In C30, price can sprint ahead of the thesis like a messenger running before the bridge is inspected. That sprint is useful as an overheat/4B marker, not as a proof that the bridge holds.

## 19. Before / After Backtest Comparison

| profile_id | scope | eligible_trigger_count | avg_MFE_90D | avg_MAE_90D | avg_MFE_180D | avg_MAE_180D | false_positive_rate | missed_structural_count | late_green_count | score_return_alignment_verdict |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| P0 e2r_2_1_stock_web_calibrated_proxy | global current | 5 | 21.57 | -12.42 | 25.66 | -15.76 | 0.60 | 0 | 1 | mixed: price-only and valuation bounces still risk false Green |
| P0b e2r_2_0_baseline_reference | rollback reference | 5 | 21.57 | -12.42 | 25.66 | -15.76 | 0.80 | 0 | 0 | worse: would over-reward valuation/RS bounces |
| P1 sector_specific_candidate_profile | L9 shadow | 5 | 10.81 | -8.57 | 13.26 | -9.04 | 0.40 | 0 | 1 | better: blocks weakest PF-margin cases |
| P2 canonical_archetype_candidate_profile | C30 shadow | 5 | 10.83 | -7.27 | 21.05 | -7.72 | 0.20 | 0 | 0 | best: treats 003070 as 4B overlay and keeps survivors as Stage2/Yellow |
| P3 counterexample_guard_profile | C30 guard | 5 | 10.83 | -7.27 | 21.05 | -7.72 | 0.20 | 1 | 0 | safer but may undercount rare price-only spikes |

## 20. Score-Return Alignment Matrix

| symbol | P0 before score/stage | P2 after score/stage | MFE90 | MAE90 | alignment |
|---:|---|---|---:|---:|---|
| 047040 | 73 / Stage2-Actionable | 74 / Stage2-Actionable_or_Yellow_not_Green | 6.5 | -8.79 | survivor_stage2_recovery_but_not_green |
| 013580 | 76 / Stage3-Yellow | 76 / Stage3-Yellow_not_Green | 15.15 | -5.75 | regional_survivor_recovery_with_low_MAE |
| 003070 | 84 / Stage3-Yellow_near_Green | 67 / Stage4B_overlay_watch_not_Green | 76.45 | -10.51 | price_spike_success_but_not_green_evidence |
| 002990 | 77 / Stage3-Yellow_false_positive_risk | 55 / Stage2-Watch_block_Green | 4.97 | -27.53 | valuation_bounce_failed_with_large_MAE |
| 005960 | 75 / Stage3-Yellow_false_positive_risk | 58 / Stage2-Watch_block_Green | 4.76 | -9.52 | sideways_failed_rerating_low_MFE |

## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive_case_count | counterexample_count | 4B_case_count | 4C_case_count | new_independent_case_count | reused_case_count | calibration_usable_trigger_count | representative_trigger_count | current_profile_error_count | sector_rule_candidate | canonical_rule_candidate | coverage_gap_after_this_loop |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| L9_CONSTRUCTION_REALESTATE_HOUSING | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | PF_BALANCE_SHEET_SURVIVOR_VS_VALUATION_BOUNCE_GUARD | 2 | 4 | 1 | 1 narrative | 5 | 0 | 6 | 5 | 3 | true | true | lower: C30 now separates survivor recovery, valuation-bounce failure, and price-only 4B overlay |

## 22. Residual Contribution Summary

```text
new_independent_case_count: 5
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 6
new_canonical_archetype_count: 0
new_fine_archetype_count: 1
new_trigger_family_count: 5
tested_existing_calibrated_axes:
  - stage2_actionable_evidence_bonus
  - stage3_green_total_min
  - full_4b_requires_non_price_evidence
  - hard_4c_thesis_break_routes_to_4c
residual_error_types_found:
  - valuation_bounce_false_positive
  - low_MFE_failed_rerating
  - price_only_spike_requires_4B_overlay
  - corporate_action_adjacent_liquidity_support_blocked
new_axis_proposed: null
existing_axis_strengthened:
  - stage3_green_total_min inside C30 via PF/liquidity/margin bridge guard
  - full_4b_requires_non_price_evidence via C30 price-only spike overlay
existing_axis_weakened: []
existing_axis_kept:
  - stage2_actionable_evidence_bonus
  - stage3_yellow_total_min
  - hard_4c_thesis_break_routes_to_4c
sector_specific_rule_candidate: true
canonical_archetype_rule_candidate: true
no_new_signal_reason: null
loop_contribution_label: canonical_archetype_rule_candidate
do_not_propose_new_weight_delta: false
```

## 23. Validation Scope / Non-Validation Scope

### Validation scope

```text
- Historical trigger-level research only.
- Stock-Web tradable OHLC rows only for MFE/MAE.
- Quantitative calibration uses clean 180D windows only.
- Same-entry duplicate rows are excluded from aggregate statistics.
- Shadow profile only; no production scoring change.
```

### Non-validation scope

```text
- No current stock recommendation.
- No 2026 live scan.
- No brokerage or auto-trading connection.
- No stock_agent src/e2r code opened.
- No production patch written.
- No raw-shard weight calibration.
```

## 24. Shadow Weight Calibration

| row_type | axis | scope | large_sector_id | canonical_archetype_id | baseline_value | tested_value | delta | confidence | proposal_type |
|---|---|---|---|---|---|---|---|---|---|
| shadow_weight | C30_pf_liquidity_margin_bridge_required_for_green | canonical_archetype_specific | L9_CONSTRUCTION_REALESTATE_HOUSING | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | 0 | 1 | +1 guard | medium | canonical_archetype_shadow_only |
| shadow_weight | C30_price_only_spike_is_4B_overlay_not_green | canonical_archetype_specific | L9_CONSTRUCTION_REALESTATE_HOUSING | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | full_4b_requires_non_price_evidence | kept_plus_C30_price_spike_overlay | 0 global / +C30 annotation | medium | canonical_archetype_shadow_only |

## 25. Machine-Readable Rows

### 25.1 price_source_validation

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
```

### 25.2 case rows

```jsonl
{"row_type":"case","case_id":"R10L11-C30-DAEWOO-20240125","symbol":"047040","company_name":"대우건설","round":"R10","loop":"11","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","fine_archetype_id":"PF_BALANCE_SHEET_SURVIVOR_VS_VALUATION_BOUNCE_GUARD","case_type":"stage2_promote_candidate","positive_or_counterexample":"positive","best_trigger":"R10L11-C30-DAEWOO-STAGE2-20240125","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"survivor_stage2_recovery_but_not_green","current_profile_verdict":"current_profile_correct","price_source":"Songdaiki/stock-web","notes":"PF/주택 사이클이 남아 있어 Green은 보류하지만, 대형사 생존 회복 Stage2/Yellow는 가격 경로와 맞았다."}
{"row_type":"case","case_id":"R10L11-C30-KYERYONG-20240125","symbol":"013580","company_name":"계룡건설","round":"R10","loop":"11","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","fine_archetype_id":"PF_BALANCE_SHEET_SURVIVOR_VS_VALUATION_BOUNCE_GUARD","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"R10L11-C30-KYERYONG-STAGE2-20240125","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"regional_survivor_recovery_with_low_MAE","current_profile_verdict":"current_profile_correct","price_source":"Songdaiki/stock-web","notes":"PF/법적 thesis-break가 없는 중견 생존주 회복은 Stage2/Yellow까지는 작동했다. 낮은 MAE가 C30 안의 positive holdout 역할을 한다."}
{"row_type":"case","case_id":"R10L11-C30-KOLON-20240125","symbol":"003070","company_name":"코오롱글로벌","round":"R10","loop":"11","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","fine_archetype_id":"PF_BALANCE_SHEET_SURVIVOR_VS_VALUATION_BOUNCE_GUARD","case_type":"high_mae_success","positive_or_counterexample":"counterexample","best_trigger":"R10L11-C30-KOLON-STAGE2-20240125","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"price_spike_success_but_not_green_evidence","current_profile_verdict":"current_profile_4B_too_late","price_source":"Songdaiki/stock-web","notes":"가격은 크게 움직였지만 PF/마진 bridge가 부족했다. C30에서는 큰 MFE 자체가 Green 근거가 아니라 4B/positioning overlay 검토 대상이다."}
{"row_type":"case","case_id":"R10L11-C30-KUMHO-20240125","symbol":"002990","company_name":"금호건설","round":"R10","loop":"11","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","fine_archetype_id":"PF_BALANCE_SHEET_SURVIVOR_VS_VALUATION_BOUNCE_GUARD","case_type":"false_positive_green","positive_or_counterexample":"counterexample","best_trigger":"R10L11-C30-KUMHO-STAGE2-20240125","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"valuation_bounce_failed_with_large_MAE","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"작은 정책/valuation bounce가 있었지만 PF/마진 bridge 부재가 180D 큰 MAE로 드러났다. C30 Green에는 별도 liquidity/PF clearance가 필요하다."}
{"row_type":"case","case_id":"R10L11-C30-DONGBU-20240125","symbol":"005960","company_name":"동부건설","round":"R10","loop":"11","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","fine_archetype_id":"PF_BALANCE_SHEET_SURVIVOR_VS_VALUATION_BOUNCE_GUARD","case_type":"failed_rerating","positive_or_counterexample":"counterexample","best_trigger":"R10L11-C30-DONGBU-STAGE2-20240125","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"sideways_failed_rerating_low_MFE","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"중견 건설사의 단기 반등은 있었지만 90/180D MFE가 작고, PF/수익성 bridge가 약해 Green 승격 근거로 쓰기 어렵다."}
{"row_type":"case","case_id":"R10L11-C30-SHINSEGAE-20240207","symbol":"034300","company_name":"신세계건설","round":"R10","loop":"11","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","fine_archetype_id":"PF_BALANCE_SHEET_SURVIVOR_VS_VALUATION_BOUNCE_GUARD","case_type":"narrative_only","positive_or_counterexample":"counterexample","best_trigger":"R10L11-C30-SHINSEGAE-4C-WATCH-20240207","calibration_usable":false,"is_new_independent_case":false,"reuse_reason":"quantitative calibration blocked because share-count/corporate-action candidate is adjacent to the trigger and stock-web last tradable window ends in 2025","independent_evidence_weight":0.0,"score_price_alignment":"capital_support_near_corporate_action_blocked","current_profile_verdict":"current_profile_data_insufficient","price_source":"Songdaiki/stock-web","notes":"자본/지원 이벤트와 주식수 변화가 인접해 있어 quantitative weight에는 쓰지 않고, PF-liquidity thesis-break narrative guard로만 둔다."}
```

### 25.3 trigger rows

```jsonl
{"row_type":"trigger","trigger_id":"R10L11-C30-DAEWOO-STAGE2-20240125","case_id":"R10L11-C30-DAEWOO-20240125","symbol":"047040","company_name":"대우건설","round":"R10","loop":"11","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","fine_archetype_id":"PF_BALANCE_SHEET_SURVIVOR_VS_VALUATION_BOUNCE_GUARD","sector":"construction_real_estate_housing","primary_archetype":"PF balance-sheet break / survivor-vs-valuation-bounce guard","loop_objective":"coverage_gap_fill|counterexample_mining|sector_specific_rule_discovery|canonical_archetype_compression|4B_non_price_requirement_stress_test","trigger_type":"Stage2-Actionable","trigger_date":"2024-01-25","evidence_available_at_that_date":"historical public-event proxy: 2024 early PF/real-estate policy relief and construction-sector value/bounce watch; stock-web row fixes timing","evidence_source":"historical public-event proxy; stock-web OHLC row used for price timing only","stage2_evidence_fields":["public_event_or_disclosure","relative_strength","policy_or_regulatory_optionality"],"stage3_evidence_fields":["financial_visibility","multiple_public_sources"],"stage4b_evidence_fields":["price_only_local_peak"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/047/047040/2024.csv","profile_path":"atlas/symbol_profiles/047/047040.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-01-25","entry_price":3925,"MFE_30D_pct":6.5,"MFE_90D_pct":6.5,"MFE_180D_pct":26.5,"MFE_1Y_pct":26.5,"MFE_2Y_pct":null,"MAE_30D_pct":-3.18,"MAE_90D_pct":-8.79,"MAE_180D_pct":-9.68,"MAE_1Y_pct":-10.32,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-07-18","peak_price":4965,"drawdown_after_peak_pct":-28.0,"green_lateness_ratio":"not_applicable:no_confirmed_Stage3_Green_trigger","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_applicable_entry_trigger","four_b_evidence_type":[],"four_c_protection_label":"not_applicable_entry_trigger","trigger_outcome_label":"survivor_stage2_recovery_not_green","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R10L11-C30-DAEWOO-20240125::2024-01-25::3925","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"R10L11-C30-KYERYONG-STAGE2-20240125","case_id":"R10L11-C30-KYERYONG-20240125","symbol":"013580","company_name":"계룡건설","round":"R10","loop":"11","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","fine_archetype_id":"PF_BALANCE_SHEET_SURVIVOR_VS_VALUATION_BOUNCE_GUARD","sector":"construction_real_estate_housing","primary_archetype":"PF balance-sheet break / survivor-vs-valuation-bounce guard","loop_objective":"coverage_gap_fill|counterexample_mining|sector_specific_rule_discovery|canonical_archetype_compression|4B_non_price_requirement_stress_test","trigger_type":"Stage2-Actionable","trigger_date":"2024-01-25","evidence_available_at_that_date":"historical public-event proxy: 2024 early PF/real-estate policy relief and construction-sector value/bounce watch; stock-web row fixes timing","evidence_source":"historical public-event proxy; stock-web OHLC row used for price timing only","stage2_evidence_fields":["public_event_or_disclosure","relative_strength","policy_or_regulatory_optionality"],"stage3_evidence_fields":["financial_visibility","low_red_team_risk"],"stage4b_evidence_fields":["price_only_local_peak"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/013/013580/2024.csv","profile_path":"atlas/symbol_profiles/013/013580.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-01-25","entry_price":13400,"MFE_30D_pct":15.15,"MFE_90D_pct":15.15,"MFE_180D_pct":15.6,"MFE_1Y_pct":15.6,"MFE_2Y_pct":null,"MAE_30D_pct":-2.09,"MAE_90D_pct":-5.75,"MAE_180D_pct":-5.75,"MAE_1Y_pct":-8.96,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-07-17","peak_price":15490,"drawdown_after_peak_pct":-17.37,"green_lateness_ratio":"not_applicable:no_confirmed_Stage3_Green_trigger","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_applicable_entry_trigger","four_b_evidence_type":[],"four_c_protection_label":"not_applicable_entry_trigger","trigger_outcome_label":"regional_survivor_stage2_yellow_success","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R10L11-C30-KYERYONG-20240125::2024-01-25::13400","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"R10L11-C30-KOLON-STAGE2-20240125","case_id":"R10L11-C30-KOLON-20240125","symbol":"003070","company_name":"코오롱글로벌","round":"R10","loop":"11","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","fine_archetype_id":"PF_BALANCE_SHEET_SURVIVOR_VS_VALUATION_BOUNCE_GUARD","sector":"construction_real_estate_housing","primary_archetype":"PF balance-sheet break / survivor-vs-valuation-bounce guard","loop_objective":"coverage_gap_fill|counterexample_mining|sector_specific_rule_discovery|canonical_archetype_compression|4B_non_price_requirement_stress_test","trigger_type":"Stage2-Actionable","trigger_date":"2024-01-25","evidence_available_at_that_date":"historical public-event proxy: 2024 early PF/real-estate policy relief and construction-sector value/bounce watch; stock-web row fixes timing","evidence_source":"historical public-event proxy; stock-web OHLC row used for price timing only","stage2_evidence_fields":["relative_strength","policy_or_regulatory_optionality"],"stage3_evidence_fields":["multiple_public_sources"],"stage4b_evidence_fields":["valuation_blowoff","positioning_overheat","price_only_local_peak"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/003/003070/2024.csv","profile_path":"atlas/symbol_profiles/003/003070.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-01-25","entry_price":9130,"MFE_30D_pct":17.2,"MFE_90D_pct":76.45,"MFE_180D_pct":76.45,"MFE_1Y_pct":76.45,"MFE_2Y_pct":null,"MAE_30D_pct":-3.61,"MAE_90D_pct":-10.51,"MAE_180D_pct":-10.51,"MAE_1Y_pct":-10.51,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-06-21","peak_price":16110,"drawdown_after_peak_pct":-47.24,"green_lateness_ratio":"not_applicable:no_confirmed_Stage3_Green_trigger","four_b_local_peak_proximity":0.95,"four_b_full_window_peak_proximity":0.95,"four_b_timing_verdict":"price_only_spike_should_be_4B_overlay_not_positive_Green","four_b_evidence_type":["valuation_blowoff","positioning_overheat","price_only"],"four_c_protection_label":"not_applicable_entry_trigger","trigger_outcome_label":"price_only_spike_requires_4B_overlay_not_green","current_profile_verdict":"current_profile_4B_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R10L11-C30-KOLON-20240125::2024-01-25::9130","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"R10L11-C30-KUMHO-STAGE2-20240125","case_id":"R10L11-C30-KUMHO-20240125","symbol":"002990","company_name":"금호건설","round":"R10","loop":"11","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","fine_archetype_id":"PF_BALANCE_SHEET_SURVIVOR_VS_VALUATION_BOUNCE_GUARD","sector":"construction_real_estate_housing","primary_archetype":"PF balance-sheet break / survivor-vs-valuation-bounce guard","loop_objective":"coverage_gap_fill|counterexample_mining|sector_specific_rule_discovery|canonical_archetype_compression|4B_non_price_requirement_stress_test","trigger_type":"Stage2-Actionable","trigger_date":"2024-01-25","evidence_available_at_that_date":"historical public-event proxy: 2024 early PF/real-estate policy relief and construction-sector value/bounce watch; stock-web row fixes timing","evidence_source":"historical public-event proxy; stock-web OHLC row used for price timing only","stage2_evidence_fields":["public_event_or_disclosure","relative_strength"],"stage3_evidence_fields":["valuation_repricing_score"],"stage4b_evidence_fields":["margin_or_backlog_slowdown","capital_raise_or_overhang"],"stage4c_evidence_fields":["thesis_evidence_broken"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/002/002990/2024.csv","profile_path":"atlas/symbol_profiles/002/002990.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-01-25","entry_price":5030,"MFE_30D_pct":4.97,"MFE_90D_pct":4.97,"MFE_180D_pct":4.97,"MFE_1Y_pct":4.97,"MFE_2Y_pct":null,"MAE_30D_pct":-4.57,"MAE_90D_pct":-27.53,"MAE_180D_pct":-43.34,"MAE_1Y_pct":-44.33,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-02-01","peak_price":5280,"drawdown_after_peak_pct":-46.97,"green_lateness_ratio":"not_applicable:no_confirmed_Stage3_Green_trigger","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_applicable_entry_trigger","four_b_evidence_type":[],"four_c_protection_label":"not_applicable_entry_trigger","trigger_outcome_label":"PF_margin_bridge_absent_false_positive","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R10L11-C30-KUMHO-20240125::2024-01-25::5030","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"R10L11-C30-DONGBU-STAGE2-20240125","case_id":"R10L11-C30-DONGBU-20240125","symbol":"005960","company_name":"동부건설","round":"R10","loop":"11","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","fine_archetype_id":"PF_BALANCE_SHEET_SURVIVOR_VS_VALUATION_BOUNCE_GUARD","sector":"construction_real_estate_housing","primary_archetype":"PF balance-sheet break / survivor-vs-valuation-bounce guard","loop_objective":"coverage_gap_fill|counterexample_mining|sector_specific_rule_discovery|canonical_archetype_compression|4B_non_price_requirement_stress_test","trigger_type":"Stage2-Actionable","trigger_date":"2024-01-25","evidence_available_at_that_date":"historical public-event proxy: 2024 early PF/real-estate policy relief and construction-sector value/bounce watch; stock-web row fixes timing","evidence_source":"historical public-event proxy; stock-web OHLC row used for price timing only","stage2_evidence_fields":["relative_strength","policy_or_regulatory_optionality"],"stage3_evidence_fields":["valuation_repricing_score"],"stage4b_evidence_fields":["margin_or_backlog_slowdown"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/005/005960/2024.csv","profile_path":"atlas/symbol_profiles/005/005960.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-01-25","entry_price":5250,"MFE_30D_pct":4.76,"MFE_90D_pct":4.76,"MFE_180D_pct":4.76,"MFE_1Y_pct":4.76,"MFE_2Y_pct":null,"MAE_30D_pct":-3.24,"MAE_90D_pct":-9.52,"MAE_180D_pct":-9.52,"MAE_1Y_pct":-17.62,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-02-19","peak_price":5500,"drawdown_after_peak_pct":-18.64,"green_lateness_ratio":"not_applicable:no_confirmed_Stage3_Green_trigger","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_applicable_entry_trigger","four_b_evidence_type":[],"four_c_protection_label":"not_applicable_entry_trigger","trigger_outcome_label":"low_MFE_sideways_failed_rerating","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R10L11-C30-DONGBU-20240125::2024-01-25::5250","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"R10L11-C30-KOLON-4B-20240620","case_id":"R10L11-C30-KOLON-20240125","symbol":"003070","company_name":"코오롱글로벌","round":"R10","loop":"11","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","fine_archetype_id":"PF_BALANCE_SHEET_SURVIVOR_VS_VALUATION_BOUNCE_GUARD","sector":"construction_real_estate_housing","primary_archetype":"PF balance-sheet break / survivor-vs-valuation-bounce guard","loop_objective":"4B_non_price_requirement_stress_test|counterexample_mining","trigger_type":"Stage4B","trigger_date":"2024-06-20","evidence_available_at_that_date":"large price/volume spike after weak balance-sheet sector bounce; no fresh PF/liquidity clearance evidence","evidence_source":"stock-web price timing plus historical public-event proxy","stage2_evidence_fields":[],"stage3_evidence_fields":[],"stage4b_evidence_fields":["valuation_blowoff","positioning_overheat","price_only_local_peak"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/003/003070/2024.csv","profile_path":"atlas/symbol_profiles/003/003070.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-06-20","entry_price":15740,"MFE_30D_pct":2.35,"MFE_90D_pct":2.35,"MFE_180D_pct":2.35,"MFE_1Y_pct":2.35,"MFE_2Y_pct":null,"MAE_30D_pct":-28.91,"MAE_90D_pct":-47.24,"MAE_180D_pct":-47.24,"MAE_1Y_pct":-47.24,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-06-21","peak_price":16110,"drawdown_after_peak_pct":-47.24,"green_lateness_ratio":"not_applicable:4B_overlay","four_b_local_peak_proximity":0.95,"four_b_full_window_peak_proximity":0.95,"four_b_timing_verdict":"good_full_window_4B_timing_if_non_price_evidence_exists_but_here_price_only_overlay","four_b_evidence_type":["valuation_blowoff","positioning_overheat","price_only"],"four_c_protection_label":"not_applicable_4B","trigger_outcome_label":"4B_overlay_success_price_only_not_Green","current_profile_verdict":"current_profile_4B_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R10L11-C30-KOLON-20240125::2024-06-20::15740","dedupe_for_aggregate":false,"aggregate_group_role":"4B_overlay_only","is_new_independent_case":false,"reuse_reason":"same case 4B overlay timing row; not counted as representative entry","independent_evidence_weight":0.0,"do_not_count_as_new_case":true}
```

### 25.4 score_simulation rows

```jsonl
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R10L11-C30-DAEWOO-20240125","trigger_id":"R10L11-C30-DAEWOO-STAGE2-20240125","symbol":"047040","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","raw_component_scores_before":{"contract_score":28,"backlog_visibility_score":42,"margin_bridge_score":36,"revision_score":30,"relative_strength_score":46,"customer_quality_score":38,"policy_or_regulatory_score":52,"valuation_repricing_score":42,"execution_risk_score":30,"legal_or_contract_risk_score":18,"dilution_cb_risk_score":5,"accounting_trust_risk_score":10},"weighted_score_before":73,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"contract_score":28,"backlog_visibility_score":42,"margin_bridge_score":38,"revision_score":32,"relative_strength_score":46,"customer_quality_score":38,"policy_or_regulatory_score":52,"valuation_repricing_score":42,"execution_risk_score":26,"legal_or_contract_risk_score":16,"dilution_cb_risk_score":5,"accounting_trust_risk_score":10},"weighted_score_after":74,"stage_label_after":"Stage2-Actionable_or_Yellow_not_Green","changed_components":["supplemental_pf_liquidity_guard_score","margin_bridge_score","execution_risk_score","legal_or_contract_risk_score","relative_strength_score"],"component_delta_explanation":"C30 shadow profile does not reward price-only or valuation-only rerating unless PF/liquidity/legal and margin bridge are cleared. Survivor recovery remains Stage2/Yellow; false Green is blocked.","MFE_90D_pct":6.5,"MAE_90D_pct":-8.79,"score_return_alignment_label":"survivor_stage2_recovery_but_not_green","current_profile_verdict":"current_profile_correct"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R10L11-C30-KYERYONG-20240125","trigger_id":"R10L11-C30-KYERYONG-STAGE2-20240125","symbol":"013580","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","raw_component_scores_before":{"contract_score":24,"backlog_visibility_score":36,"margin_bridge_score":40,"revision_score":35,"relative_strength_score":50,"customer_quality_score":32,"policy_or_regulatory_score":42,"valuation_repricing_score":45,"execution_risk_score":22,"legal_or_contract_risk_score":10,"dilution_cb_risk_score":5,"accounting_trust_risk_score":8},"weighted_score_before":76,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":24,"backlog_visibility_score":36,"margin_bridge_score":42,"revision_score":35,"relative_strength_score":50,"customer_quality_score":32,"policy_or_regulatory_score":42,"valuation_repricing_score":45,"execution_risk_score":18,"legal_or_contract_risk_score":8,"dilution_cb_risk_score":5,"accounting_trust_risk_score":8},"weighted_score_after":76,"stage_label_after":"Stage3-Yellow_not_Green","changed_components":["supplemental_pf_liquidity_guard_score","margin_bridge_score","execution_risk_score","legal_or_contract_risk_score","relative_strength_score"],"component_delta_explanation":"C30 shadow profile does not reward price-only or valuation-only rerating unless PF/liquidity/legal and margin bridge are cleared. Survivor recovery remains Stage2/Yellow; false Green is blocked.","MFE_90D_pct":15.15,"MAE_90D_pct":-5.75,"score_return_alignment_label":"regional_survivor_recovery_with_low_MAE","current_profile_verdict":"current_profile_correct"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R10L11-C30-KOLON-20240125","trigger_id":"R10L11-C30-KOLON-STAGE2-20240125","symbol":"003070","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","raw_component_scores_before":{"contract_score":20,"backlog_visibility_score":30,"margin_bridge_score":24,"revision_score":24,"relative_strength_score":82,"customer_quality_score":25,"policy_or_regulatory_score":48,"valuation_repricing_score":72,"execution_risk_score":50,"legal_or_contract_risk_score":20,"dilution_cb_risk_score":5,"accounting_trust_risk_score":15},"weighted_score_before":84,"stage_label_before":"Stage3-Yellow_near_Green","raw_component_scores_after":{"contract_score":20,"backlog_visibility_score":30,"margin_bridge_score":24,"revision_score":24,"relative_strength_score":70,"customer_quality_score":25,"policy_or_regulatory_score":40,"valuation_repricing_score":58,"execution_risk_score":62,"legal_or_contract_risk_score":30,"dilution_cb_risk_score":5,"accounting_trust_risk_score":15},"weighted_score_after":67,"stage_label_after":"Stage4B_overlay_watch_not_Green","changed_components":["supplemental_pf_liquidity_guard_score","margin_bridge_score","execution_risk_score","legal_or_contract_risk_score","relative_strength_score"],"component_delta_explanation":"C30 shadow profile does not reward price-only or valuation-only rerating unless PF/liquidity/legal and margin bridge are cleared. Survivor recovery remains Stage2/Yellow; false Green is blocked.","MFE_90D_pct":76.45,"MAE_90D_pct":-10.51,"score_return_alignment_label":"price_spike_success_but_not_green_evidence","current_profile_verdict":"current_profile_4B_too_late"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R10L11-C30-KUMHO-20240125","trigger_id":"R10L11-C30-KUMHO-STAGE2-20240125","symbol":"002990","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","raw_component_scores_before":{"contract_score":18,"backlog_visibility_score":26,"margin_bridge_score":16,"revision_score":18,"relative_strength_score":32,"customer_quality_score":20,"policy_or_regulatory_score":40,"valuation_repricing_score":44,"execution_risk_score":68,"legal_or_contract_risk_score":32,"dilution_cb_risk_score":12,"accounting_trust_risk_score":20},"weighted_score_before":77,"stage_label_before":"Stage3-Yellow_false_positive_risk","raw_component_scores_after":{"contract_score":18,"backlog_visibility_score":26,"margin_bridge_score":12,"revision_score":18,"relative_strength_score":28,"customer_quality_score":20,"policy_or_regulatory_score":34,"valuation_repricing_score":36,"execution_risk_score":78,"legal_or_contract_risk_score":42,"dilution_cb_risk_score":12,"accounting_trust_risk_score":24},"weighted_score_after":55,"stage_label_after":"Stage2-Watch_block_Green","changed_components":["supplemental_pf_liquidity_guard_score","margin_bridge_score","execution_risk_score","legal_or_contract_risk_score","relative_strength_score"],"component_delta_explanation":"C30 shadow profile does not reward price-only or valuation-only rerating unless PF/liquidity/legal and margin bridge are cleared. Survivor recovery remains Stage2/Yellow; false Green is blocked.","MFE_90D_pct":4.97,"MAE_90D_pct":-27.53,"score_return_alignment_label":"valuation_bounce_failed_with_large_MAE","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R10L11-C30-DONGBU-20240125","trigger_id":"R10L11-C30-DONGBU-STAGE2-20240125","symbol":"005960","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","raw_component_scores_before":{"contract_score":20,"backlog_visibility_score":28,"margin_bridge_score":22,"revision_score":20,"relative_strength_score":35,"customer_quality_score":22,"policy_or_regulatory_score":36,"valuation_repricing_score":42,"execution_risk_score":58,"legal_or_contract_risk_score":24,"dilution_cb_risk_score":8,"accounting_trust_risk_score":16},"weighted_score_before":75,"stage_label_before":"Stage3-Yellow_false_positive_risk","raw_component_scores_after":{"contract_score":20,"backlog_visibility_score":28,"margin_bridge_score":18,"revision_score":20,"relative_strength_score":28,"customer_quality_score":22,"policy_or_regulatory_score":30,"valuation_repricing_score":34,"execution_risk_score":66,"legal_or_contract_risk_score":30,"dilution_cb_risk_score":8,"accounting_trust_risk_score":18},"weighted_score_after":58,"stage_label_after":"Stage2-Watch_block_Green","changed_components":["supplemental_pf_liquidity_guard_score","margin_bridge_score","execution_risk_score","legal_or_contract_risk_score","relative_strength_score"],"component_delta_explanation":"C30 shadow profile does not reward price-only or valuation-only rerating unless PF/liquidity/legal and margin bridge are cleared. Survivor recovery remains Stage2/Yellow; false Green is blocked.","MFE_90D_pct":4.76,"MAE_90D_pct":-9.52,"score_return_alignment_label":"sideways_failed_rerating_low_MFE","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R10L11-C30-SHINSEGAE-20240207","trigger_id":"R10L11-C30-SHINSEGAE-4C-WATCH-20240207","symbol":"034300","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","raw_component_scores_before":{"contract_score":10,"backlog_visibility_score":16,"margin_bridge_score":8,"revision_score":10,"relative_strength_score":22,"customer_quality_score":12,"policy_or_regulatory_score":28,"valuation_repricing_score":30,"execution_risk_score":88,"legal_or_contract_risk_score":55,"dilution_cb_risk_score":45,"accounting_trust_risk_score":40},"weighted_score_before":48,"stage_label_before":"4C-watch_data_insufficient","raw_component_scores_after":{"contract_score":10,"backlog_visibility_score":16,"margin_bridge_score":6,"revision_score":10,"relative_strength_score":18,"customer_quality_score":12,"policy_or_regulatory_score":20,"valuation_repricing_score":24,"execution_risk_score":90,"legal_or_contract_risk_score":70,"dilution_cb_risk_score":50,"accounting_trust_risk_score":45},"weighted_score_after":42,"stage_label_after":"4C-watch_narrative_only","changed_components":["execution_risk_score","legal_or_contract_risk_score","dilution_cb_risk_score","accounting_trust_risk_score"],"component_delta_explanation":"Narrative-only C30 liquidity support case; blocked because corporate-action candidate is adjacent to trigger and later inactive/delisted-like context.","MFE_90D_pct":null,"MAE_90D_pct":null,"score_return_alignment_label":"capital_support_near_corporate_action_blocked","current_profile_verdict":"current_profile_data_insufficient"}
```

### 25.5 shadow_weight rows

```jsonl
{"row_type":"shadow_weight","axis":"C30_pf_liquidity_margin_bridge_required_for_green","scope":"canonical_archetype_specific","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","baseline_value":0,"tested_value":1,"delta":"+1 guard","reason":"New R10 loop11 cases split stable survivor Stage2/Yellow from valuation-only or price-only construction bounces. Kumho/Dongbu failed rerating; Kolon required 4B overlay rather than Green.","backtest_effect":"blocks false Green in 002990/005960, routes 003070 spike to 4B overlay, keeps 047040/013580 as Stage2/Yellow positives","trigger_ids":"R10L11-C30-DAEWOO-STAGE2-20240125|R10L11-C30-KYERYONG-STAGE2-20240125|R10L11-C30-KOLON-STAGE2-20240125|R10L11-C30-KUMHO-STAGE2-20240125|R10L11-C30-DONGBU-STAGE2-20240125","calibration_usable_count":5,"new_independent_case_count":5,"counterexample_count":3,"confidence":"medium","proposal_type":"canonical_archetype_shadow_only","notes":"not production; post-calibrated residual"}
{"row_type":"shadow_weight","axis":"C30_price_only_spike_is_4B_overlay_not_green","scope":"canonical_archetype_specific","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","baseline_value":"full_4b_requires_non_price_evidence","tested_value":"kept_plus_C30_price_spike_overlay","delta":"0 global / +C30 annotation","reason":"Kolon 2024 price spike was near full-window peak, but it was not confirmed by PF/legal/margin bridge. Treat as overlay, not positive Green evidence.","backtest_effect":"improves score-return alignment by avoiding outcome-looking Green labels from price-only MFE","trigger_ids":"R10L11-C30-KOLON-STAGE2-20240125|R10L11-C30-KOLON-4B-20240620","calibration_usable_count":2,"new_independent_case_count":1,"counterexample_count":1,"confidence":"medium","proposal_type":"canonical_archetype_shadow_only","notes":"not production; strengthens existing full_4b_requires_non_price_evidence only inside C30"}
```

### 25.6 residual_contribution row

```jsonl
{"row_type":"residual_contribution","round":"R10","loop":"11","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","scheduled_round":"R10","scheduled_loop":"11","round_schedule_status":"valid","round_sector_consistency":"pass","new_independent_case_count":5,"reused_case_count":0,"new_symbol_count":6,"same_archetype_new_symbol_count":6,"same_archetype_new_trigger_family_count":5,"new_trigger_family_count":5,"positive_case_count":2,"counterexample_count":4,"current_profile_error_count":3,"tested_existing_calibrated_axes":["stage2_actionable_evidence_bonus","stage3_green_total_min","full_4b_requires_non_price_evidence","hard_4c_thesis_break_routes_to_4c"],"residual_error_types_found":["valuation_bounce_false_positive","low_MFE_failed_rerating","price_only_spike_requires_4B_overlay","corporate_action_adjacent_liquidity_support_blocked"],"loop_contribution_label":"canonical_archetype_rule_candidate","do_not_propose_new_weight_delta":false}
```

### 25.7 narrative_only row

```jsonl
{"row_type":"narrative_only","case_id":"R10L11-C30-SHINSEGAE-20240207","symbol":"034300","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","reason":"capital_support_or_liquidity_event_near_stock_web_corporate_action_candidate; not used for weight calibration","price_source":"Songdaiki/stock-web","usage":"not_weight_calibration"}
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
completed_round = R10
completed_loop = 11
next_round = R11
next_loop = 11
round_schedule_status = valid
round_sector_consistency = pass
```

## 28. Source Notes

```text
stock_agent artifact checked:
- reports/e2r_calibration/by_round/R10.md

stock-web files checked:
- atlas/manifest.json
- atlas/schema.json
- atlas/symbol_profiles/047/047040.json
- atlas/symbol_profiles/013/013580.json
- atlas/symbol_profiles/003/003070.json
- atlas/symbol_profiles/002/002990.json
- atlas/symbol_profiles/005/005960.json
- atlas/symbol_profiles/034/034300.json
- atlas/ohlcv_tradable_by_symbol_year/047/047040/2024.csv
- atlas/ohlcv_tradable_by_symbol_year/013/013580/2024.csv
- atlas/ohlcv_tradable_by_symbol_year/003/003070/2024.csv
- atlas/ohlcv_tradable_by_symbol_year/002/002990/2024.csv
- atlas/ohlcv_tradable_by_symbol_year/005/005960/2024.csv
- atlas/ohlcv_tradable_by_symbol_year/034/034300/2024.csv
```

