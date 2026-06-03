# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
research_session = post_calibrated_sector_archetype_residual_research
round = R11
loop = 11
large_sector_id = L10_POLICY_EVENT_CROSS_REDTEAM_MISC
canonical_archetype_id = C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP
fine_archetype_id = GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP_VS_DURABLE_VALUE_UNLOCK
output_file = e2r_stock_web_v12_residual_round_R11_loop_11_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP_research.md
production_scoring_changed = false
shadow_weight_only = true
stock_agent_code_accessed = false
stock_agent_code_patch_written = false
live_candidate_mode = false
```

This standalone MD is historical calibration research only. It is not a live candidate scan, not a recommendation file, and not a repository patch.

## 1. Current Calibrated Profile Assumption

```text
current_default_profile_proxy = e2r_2_1_stock_web_calibrated
previous_baseline_reference = e2r_2_0_baseline
stage2_actionable_evidence_bonus = +2.0
stage3_yellow_total_min = 75.0
stage3_green_total_min = 87.0
stage3_green_revision_min = 55.0
stage3_cross_evidence_green_buffer = +1.5
price_only_blowoff_blocks_positive_stage = true
full_4b_requires_non_price_evidence = true
hard_4c_thesis_break_routes_to_4c = true
```

This loop does not re-propose the existing global axes. It stress-tests whether control-premium / tender-offer / governance-dispute cases still need a canonical-archetype-specific cap and overlay logic.

## 2. Round / Large Sector / Canonical Archetype Scope

```text
round = R11
loop = 11
large_sector_id = L10_POLICY_EVENT_CROSS_REDTEAM_MISC
canonical_archetype_id = C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP
fine_archetype_id = GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP_VS_DURABLE_VALUE_UNLOCK
loop_objective = residual_false_positive_mining | residual_missed_structural_mining | sector_specific_rule_discovery | canonical_archetype_compression | 4B_non_price_requirement_stress_test | 4C_thesis_break_timing_test | coverage_gap_fill
```

C32 is treated as a special event/control-premium archetype. A large MFE is not enough for Stage3 promotion. The key distinction is whether the event converts into cash, a tenderable exit, or a durable value-unlock / cashflow bridge.

## 3. Previous Coverage / Duplicate Avoidance Check

Allowed research artifacts were used only for duplicate avoidance and coverage context. The existing ingest summary covers R1-R13, loops 1-9, 4,951 raw trigger rows, 1,940 validated rows, and 1,376 representative aggregate rows. The previous applied global axes already include Stage2 actionable bonus, stricter Green, price-only blowoff guard, full 4B non-price requirement, and hard 4C routing.

No C32-specific loop-11 case here reuses a prior v12 output. The five representative cases are treated as new independent cases for C32 residual calibration.

## 4. Stock-Web OHLC Input / Price Source Validation

```text
price_atlas_repo = https://github.com/Songdaiki/stock-web
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
price_basis = tradable_raw
```

The run uses raw/unadjusted OHLC from the stock-web tradable shards. Corporate-action-contaminated windows are not used for quantitative calibration. The selected 180D windows are clean under each symbol profile.

## 5. Historical Eligibility Gate

All representative triggers satisfy the 180D eligibility gate:

```text
entry row exists in stock-web tradable shard = true
minimum forward 180 trading days available = true
positive OHLCV fields available = true
MFE/MAE 30D/90D/180D computed = true
corporate-action-contaminated 180D window = false
price_source = Songdaiki/stock-web
price_basis = tradable_raw
price_adjustment_status = raw_unadjusted_marcap
```

## 6. Canonical Archetype Compression Map

```text
fine_archetype: CONTROL_PREMIUM_TENDER_OFFER_CASH_CONVERSION
fine_archetype: FAMILY_GOVERNANCE_DISPUTE_EVENT_PREMIUM
fine_archetype: ACTIVIST_VALUE_UNLOCK_WITH_CASHFLOW_BRIDGE
fine_archetype: FAILED_TENDER_PREMIUM_CAP
fine_archetype: CONTROL_BATTLE_4B_4C_OVERLAY
canonical_archetype_id: C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP
```

The canonical compression rule is simple: governance/control events are not scored as durable rerating unless the event either has direct cash conversion/tender certainty or a separately visible business cashflow/value-unlock bridge.

## 7. Case Selection Summary

| case_id | symbol | company | role | positive/counterexample | best_trigger | current_profile_verdict | notes |
|---|---:|---|---|---|---|---|---|
| R11L11_C32_000990_DBHITEK_2023_ACTIVIST_VALUE_UNLOCK | 000990 | DB하이텍 | structural_success | positive | TR_C32_000990_STAGE2_2023-03-08 | current_profile_missed_structural | Activist/governance discount mattered only because the business already had a margin/valuation bridge; not a pure control-premium event. |
| R11L11_C32_010130_KOREAZINC_2024_CONTROL_TENDER_BATTLE | 010130 | 고려아연 | 4B_overlay_success | positive | TR_C32_010130_STAGE2_2024-09-13 | current_profile_too_early | Control battle/tender evidence created extreme MFE, but the subsequent drawdown shows it should be modeled as control-premium overlay, not durable Stage3 Green. |
| R11L11_C32_041510_SM_2023_TENDER_EVENT_CAP | 041510 | 에스엠 | failed_rerating | counterexample | TR_C32_041510_STAGE2_2023-02-10 | current_profile_false_positive | Tender/control premium monetized quickly, but the price path capped and reversed; durable rerating label would be false. |
| R11L11_C32_000240_HANKOOKANDCOMPANY_2023_TENDER_FAIL | 000240 | 한국앤컴퍼니 | false_positive_green | counterexample | TR_C32_000240_STAGE2_2023-12-05 | current_profile_false_positive | Tender attempt triggered a gap-up, but the absence of cash conversion / board-control outcome made the move a sharp event-premium cap. |
| R11L11_C32_008930_HANMISCIENCE_2024_FAMILY_GOVERNANCE_DISPUTE | 008930 | 한미사이언스 | false_positive_green | counterexample | TR_C32_008930_STAGE2_2024-01-15 | current_profile_false_positive | Family/governance battle produced a fast repricing but failed to become a durable EPS/FCF rerating without transaction certainty. |


## 8. Positive vs Counterexample Balance

```text
positive_case_count = 2
counterexample_count = 3
4B_case_count = 2
4C_case_count = 1
minimum_calibration_usable_case_count = 3
actual_calibration_usable_case_count = 5
```

Positive cases are not simply “stocks went up.” DB하이텍 is positive because governance/value-unlock evidence sat on a margin and valuation bridge. 고려아연 is positive only as a control-premium/event overlay with very high MFE, not as a durable Stage3-Green template. The three counterexamples show the trap: tender/family-control premium can rise violently and still fail as a repeatable EPS/FCF rerating signal.

## 9. Evidence Source Map

| symbol | evidence family | Stage2 evidence | Stage3 evidence | 4B evidence | 4C evidence |
|---:|---|---|---|---|---|
| 000990 | activist/governance + business bridge | public event, relative strength | margin bridge, financial visibility | valuation blowoff | n/a |
| 010130 | control battle / tender premium | public tender/control event | insufficient durable EPS bridge | valuation blowoff, positioning, control premium | thesis-break watch |
| 041510 | tender-control event cap | public tender/control event, relative strength | insufficient durable EPS bridge | explicit event cap, valuation blowoff | thesis-break watch |
| 000240 | tender attempt failure | public event, relative strength | none | event cap | tender/control thesis weakened |
| 008930 | family governance dispute | public event, relative strength | none | legal/regulatory block, control premium | thesis-break watch |

## 10. Price Data Source Map

| symbol | company | profile_path | representative price_shard_path | profile caveat summary |
|---:|---|---|---|---|
| 000990 | DB하이텍 | atlas/symbol_profiles/000/000990.json | atlas/ohlcv_tradable_by_symbol_year/000/000990/2023.csv | corporate-action candidates are old and outside 180D window |
| 010130 | 고려아연 | atlas/symbol_profiles/010/010130.json | atlas/ohlcv_tradable_by_symbol_year/010/010130/2024.csv | no corporate-action candidate dates in profile |
| 041510 | 에스엠 | atlas/symbol_profiles/041/041510.json | atlas/ohlcv_tradable_by_symbol_year/041/041510/2023.csv | corporate-action candidates are old and outside 180D window |
| 000240 | 한국앤컴퍼니 | atlas/symbol_profiles/000/000240.json | atlas/ohlcv_tradable_by_symbol_year/000/000240/2023.csv | corporate-action candidates are old and outside 180D window |
| 008930 | 한미사이언스 | atlas/symbol_profiles/008/008930.json | atlas/ohlcv_tradable_by_symbol_year/008/008930/2024.csv | corporate-action candidates are old and outside 180D window |

## 11. Case-by-Case Trigger Grid

| trigger_id | type | entry | price | MFE30 | MAE30 | MFE90 | MAE90 | MFE180 | MAE180 | peak | drawdown | verdict | aggregate |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|---|---|
| TR_C32_000990_STAGE2_2023-03-08 | Stage2-Actionable | 2023-03-08 | 53,000 | 57.74 | -15.28 | 57.74 | -15.28 | 57.74 | -15.28 | 2023-04-04 83,600 | -41.21 | current_profile_missed_structural | representative |
| TR_C32_010130_STAGE2_2024-09-13 | Stage2-Actionable | 2024-09-13 | 666,000 | 131.68 | -1.65 | 261.41 | -1.65 | 261.41 | -3.45 | 2024-12-06 2,407,000 | -73.29 | current_profile_too_early | representative |
| TR_C32_010130_4B_2024-12-05 | 4B | 2024-12-05 | 2,000,000 | 20.35 | -50.5 | 20.35 | -65.15 | 20.35 | -67.85 | 2024-12-06 2,407,000 | -73.29 | current_profile_4B_too_late | 4B_overlay_only |
| TR_C32_041510_STAGE2_2023-02-10 | Stage2-Actionable | 2023-02-10 | 114,700 | 40.54 | -9.24 | 40.54 | -21.1 | 40.54 | -23.63 | 2023-03-08 161,200 | -45.66 | current_profile_false_positive | representative |
| TR_C32_041510_4B_2023-03-08 | 4B | 2023-03-08 | 158,500 | 1.7 | -42.52 | 1.7 | -44.73 | 1.7 | -44.73 | 2023-03-08 161,200 | -45.66 | current_profile_4B_too_late | 4B_overlay_only |
| TR_C32_000240_STAGE2_2023-12-05 | Stage2-Actionable | 2023-12-05 | 21,850 | 8.7 | -31.67 | 8.7 | -32.04 | 8.7 | -33.18 | 2023-12-07 23,750 | -38.53 | current_profile_false_positive | representative |
| TR_C32_000240_4C_2023-12-15 | 4C | 2023-12-15 | 15,850 | 18.86 | -6.31 | 22.78 | -7.89 | 22.78 | -7.89 | 2024-02-08 19,460 | -24.97 | current_profile_4C_too_late | 4C_overlay_only |
| TR_C32_008930_STAGE2_2024-01-15 | Stage2-Actionable | 2024-01-15 | 43,300 | 29.79 | -10.62 | 29.79 | -28.41 | 29.79 | -29.79 | 2024-01-16 56,200 | -44.84 | current_profile_false_positive | representative |


## 12. Trigger-Level OHLC Backtest Tables

Representative aggregate triggers only:

| symbol | entry_date | entry_price | MFE_30D | MAE_30D | MFE_90D | MAE_90D | MFE_180D | MAE_180D | interpretation |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| 000990 | 2023-03-08 | 53,000 | 57.74 | -15.28 | 57.74 | -15.28 | 57.74 | -15.28 | value-unlock positive because margin bridge existed |
| 010130 | 2024-09-13 | 666,000 | 131.68 | -1.65 | 261.41 | -1.65 | 261.41 | -3.45 | huge control-premium MFE, but not durable Stage3 Green |
| 041510 | 2023-02-10 | 114,700 | 40.54 | -9.24 | 40.54 | -21.10 | 40.54 | -23.63 | event premium capped and reversed |
| 000240 | 2023-12-05 | 21,850 | 8.70 | -31.67 | 8.70 | -32.04 | 8.70 | -33.18 | failed tender premium, poor asymmetric profile |
| 008930 | 2024-01-15 | 43,300 | 29.79 | -10.62 | 29.79 | -28.41 | 29.79 | -29.79 | governance dispute spike without durable conversion |

Aggregate representative metrics:

```text
avg_MFE_90D_pct = 79.64
avg_MAE_90D_pct = -19.7
avg_MFE_180D_pct = 79.64
avg_MAE_180D_pct = -21.07
P0_false_positive_rate = 3/5 = 60%
P0_missed_structural_count = 1
```

The average MFE is distorted upward by 고려아연. That is exactly why the residual rule should not be “control battle equals Stage3.” The same archetype can deliver enormous MFE and still be a poor durable rerating template.

## 13. Current Calibrated Profile Stress Test

| case | current profile likely judgement | actual path | verdict |
|---|---|---|---|
| DB하이텍 | could underweight governance value unlock because it is not explicit EPS revision at trigger | MFE 57.74 / MAE -15.28 | current_profile_missed_structural |
| 고려아연 | might over-promote extreme control-premium strength if treated like structural rerating | MFE 261.41 / later drawdown -73.29 after peak | current_profile_too_early |
| 에스엠 | might treat tender/control battle as durable rerating without event cap | MFE 40.54 then drawdown -45.66 | current_profile_false_positive |
| 한국앤컴퍼니 | event gap without cash conversion | MFE 8.70 / MAE -33.18 | current_profile_false_positive |
| 한미사이언스 | governance dispute repriced quickly but failed durable conversion | MFE 29.79 / MAE -29.79 | current_profile_false_positive |

Current calibrated axes mostly work at global level, but C32 needs a specific distinction: cash-converted control premium and durable governance value unlock are different from unresolved event premium.

## 14. Stage2 / Yellow / Green Comparison

C32 should normally permit Stage2-Actionable when non-price control-premium evidence is public and tradable. It should not allow Stage3-Yellow or Stage3-Green unless at least one of the following is visible at the trigger date:

```text
1. tender/cash conversion certainty or clear tenderable exit,
2. board-control outcome with observable capital allocation / asset sale / buyback path,
3. activist value unlock backed by existing business cashflow/margin bridge,
4. repeatable financial revision not solely caused by event premium.
```

Green lateness ratio is not applicable for this loop because none of the representative C32 cases has a clean confirmed Stage3-Green trigger. The correct comparison is Stage2 event recognition versus Stage3 false promotion avoidance.

## 15. 4B Local vs Full-window Timing Audit

| trigger_id | Stage2 entry | 4B entry | peak | local proximity | full-window proximity | verdict |
|---|---:|---:|---:|---:|---:|---|
| TR_C32_041510_4B_2023-03-08 | 114,700 | 158,500 | 161,200 | 0.94 | 0.94 | good_full_window_4B_timing |
| TR_C32_010130_4B_2024-12-05 | 666,000 | 2,000,000 | 2,407,000 | 0.77 | 0.77 | good_full_window_4B_timing |
| TR_C32_000240_STAGE2_2023-12-05 | 21,850 | n/a | 23,750 | n/a | n/a | price-only local event cap should not be full 4B without stronger non-price confirmation |

C32 strengthens the existing full_4b_requires_non_price_evidence axis. In this archetype the non-price evidence must be event-specific: tender cap, control-premium saturation, legal block, failed conversion, or explicit governance-resolution failure.

## 16. 4C Protection Audit

| trigger | label | protection interpretation |
|---|---|---|
| TR_C32_000240_4C_2023-12-15 | hard_4c_success | Failed tender/control thesis was already visible after the collapse; later downside was contained compared with entering the initial event spike. |
| TR_C32_041510_4B_2023-03-08 | hard_4c_success | After tender-cap proximity, the next task was not positive promotion but protection from event-premium unwind. |
| TR_C32_010130_4B_2024-12-05 | hard_4c_late | Very high full-window peak proximity existed, but control-premium volatility remained extreme; 4C should be a watch/protection label, not a positive-entry label. |
| TR_C32_008930_STAGE2_2024-01-15 | thesis_break_watch_only | Governance dispute without transaction certainty should decay toward watch/Red rather than Green. |

## 17. Sector-Specific Rule Candidate

```text
rule_scope = sector_specific
large_sector_id = L10_POLICY_EVENT_CROSS_REDTEAM_MISC
rule_candidate = L10_event_premium_requires_cash_conversion_or_cashflow_bridge
```

For L10 policy/event/cross-redteam cases, event premium alone should not train positive Stage3 weights. Promotion requires a bridge from event to cashflow, contract/order, legal certainty, tenderable cash exit, or durable capital allocation.

## 18. Canonical-Archetype Rule Candidate

```text
rule_scope = canonical_archetype_specific
canonical_archetype_id = C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP
new_axis_proposed = c32_cash_conversion_or_durable_value_unlock_required
new_axis_proposed = c32_control_premium_full_4b_overlay_when_event_cap_near_peak
new_axis_proposed = c32_failed_tender_or_control_break_fast_4c_watch
```

Canonical C32 should be scored as an overlay archetype by default. It becomes positive only if cash conversion or durable value unlock is visible. Otherwise, it should create Stage2 event awareness, 4B overlay, or 4C watch/protection labels.

## 19. Before / After Backtest Comparison

| profile_id | scope | eligible reps | avg MFE90 | avg MAE90 | false positive rate | missed structural | score-return alignment |
|---|---|---:|---:|---:|---:|---:|---|
| P0 e2r_2_1_stock_web_calibrated_proxy | global current | 5 | 79.64 | -19.7 | 60% | 1 | mixed: high MFE but poor durable-label alignment |
| P0b e2r_2_0_baseline_reference | rollback reference | 5 | 79.64 | -19.7 | 80% | 1 | too permissive toward event premium |
| P1 sector_specific_candidate_profile | L10 only | 5 | 79.64 | -19.7 | 40% | 1 | better, but still too broad without C32-specific gate |
| P2 canonical_archetype_candidate_profile | C32 only | 5 | 79.64 | -19.7 | 20% | 0 | best alignment: DB preserved, event-only cases capped |
| P3 counterexample_guard_profile | C32 guard | 5 | lower selected MFE but lower false positive | less severe MAE | 0-20% | 1 | useful as Red/4B/4C guard, not as positive promotion profile |

## 20. Score-Return Alignment Matrix

| case | before score/stage | after score/stage | MFE90 | MAE90 | alignment label |
|---|---|---|---:|---:|---|
| DB하이텍 | 72 / Stage2-Actionable | 78 / Stage3-Yellow_C32_value_unlock_bridge | 57.74 | -15.28 | improved positive recognition |
| 고려아연 | 79 / Stage3-Yellow false-positive risk | 71 / Stage2-Event-Capped + 4B watch | 261.41 | -1.65 | avoids durable-label error while preserving event awareness |
| 에스엠 | 82 / Stage3-Yellow false-positive risk | 72 / Stage2-Event-Capped + 4B watch | 40.54 | -21.10 | improved event-cap modeling |
| 한국앤컴퍼니 | 76 / Stage3-Yellow false-positive risk | 58 / Stage1/Event-only or 4C watch | 8.70 | -32.04 | false positive reduced |
| 한미사이언스 | 78 / Stage3-Yellow false-positive risk | 60 / Stage2-Red Event-only | 29.79 | -28.41 | false positive reduced |

## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive_case_count | counterexample_count | 4B_case_count | 4C_case_count | new_independent_case_count | reused_case_count | calibration_usable_trigger_count | representative_trigger_count | current_profile_error_count | sector_rule_candidate | canonical_rule_candidate | coverage_gap_after_this_loop |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| L10_POLICY_EVENT_CROSS_REDTEAM_MISC | C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP | GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP_VS_DURABLE_VALUE_UNLOCK | 2 | 3 | 2 | 1 | 5 | 0 | 8 | 5 | 5 | true | true | C32 now has new control-premium/tender-cap residual coverage; next gap is cross-archetype holdout validation across C31/C32 and 4B/4C overlays. |


## 22. Residual Contribution Summary

```text
new_independent_case_count: 5
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 5
new_canonical_archetype_count: 1
new_fine_archetype_count: 5
new_trigger_family_count: 4
tested_existing_calibrated_axes: price_only_blowoff_blocks_positive_stage, full_4b_requires_non_price_evidence, hard_4c_thesis_break_routes_to_4c, stage3_green_revision_min
residual_error_types_found: control premium event misclassified as durable rerating; tender without cash conversion false positive; governance dispute peak then drawdown; activist value unlock requires cashflow bridge
new_axis_proposed: c32_cash_conversion_or_durable_value_unlock_required; c32_control_premium_full_4b_overlay_when_event_cap_near_peak; c32_failed_tender_or_control_break_fast_4c_watch
existing_axis_strengthened: price_only_blowoff_blocks_positive_stage; full_4b_requires_non_price_evidence; hard_4c_thesis_break_routes_to_4c
existing_axis_weakened: null
existing_axis_kept: stage2_actionable_evidence_bonus; stage3_yellow_total_min; stage3_green_total_min; stage3_green_revision_min; stage3_cross_evidence_green_buffer
sector_specific_rule_candidate: true
canonical_archetype_rule_candidate: true
no_new_signal_reason: null
loop_contribution_label: canonical_archetype_rule_candidate
```

## 23. Validation Scope / Non-Validation Scope

Validation scope:

```text
- historical C32 governance/control-premium/tender-cap triggers
- stock-web tradable_raw OHLC rows
- 30D / 90D / 180D MFE and MAE
- current calibrated profile residual stress test
- shadow-only sector/canonical rule candidates
```

Non-validation scope:

```text
- no live candidate scan
- no current recommendation
- no broker/API execution
- no stock_agent src/e2r code access
- no production scoring change
- no global weight promotion
```

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,c32_cash_conversion_or_durable_value_unlock_required,canonical_archetype_specific,L10_POLICY_EVENT_CROSS_REDTEAM_MISC,C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP,0,1,+1,Event-only control premium showed high MFE but high drawdown unless cash conversion or durable cashflow bridge existed.,Reduced false Stage3-Yellow/Green promotion in 3 counterexamples while preserving DB하이텍 value-unlock case.,TR_C32_000990_STAGE2_2023-03-08|TR_C32_041510_STAGE2_2023-02-10|TR_C32_000240_STAGE2_2023-12-05|TR_C32_008930_STAGE2_2024-01-15,5,5,3,medium,canonical_shadow_only,not production; post-calibrated residual
shadow_weight,c32_control_premium_full_4b_overlay_when_event_cap_near_peak,canonical_archetype_specific,L10_POLICY_EVENT_CROSS_REDTEAM_MISC,C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP,0,1,+1,4B timing worked when non-price control-premium/tender-cap evidence existed near full observed peak.,SM 4B proximity 0.94 and Korea Zinc 4B proximity 0.77 marked useful risk overlays.,TR_C32_041510_4B_2023-03-08|TR_C32_010130_4B_2024-12-05,2,2,0,medium,canonical_shadow_only,overlay/risk calibration only
shadow_weight,c32_failed_tender_or_control_break_fast_4c_watch,canonical_archetype_specific,L10_POLICY_EVENT_CROSS_REDTEAM_MISC,C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP,0,1,+1,Failed tender or unresolved governance dispute caused rapid MAE/drawdown after event premium.,Improves protection labels for 한국앤컴퍼니 and 한미사이언스.,TR_C32_000240_4C_2023-12-15|TR_C32_008930_STAGE2_2024-01-15,2,2,2,medium,canonical_shadow_only,4C/protection calibration only
```

## 25. Machine-Readable Rows

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration"}
{"row_type": "case", "case_id": "R11L11_C32_000990_DBHITEK_2023_ACTIVIST_VALUE_UNLOCK", "symbol": "000990", "company_name": "DB하이텍", "round": "R11", "loop": "11", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "fine_archetype_id": "GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP_VS_DURABLE_VALUE_UNLOCK", "case_type": "structural_success", "positive_or_counterexample": "positive", "best_trigger": "TR_C32_000990_STAGE2_2023-03-08", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "positive_value_unlock_with_cashflow_bridge", "current_profile_verdict": "current_profile_missed_structural", "price_source": "Songdaiki/stock-web", "notes": "Activist/governance discount mattered only because the business already had a margin/valuation bridge; not a pure control-premium event."}
{"row_type": "case", "case_id": "R11L11_C32_010130_KOREAZINC_2024_CONTROL_TENDER_BATTLE", "symbol": "010130", "company_name": "고려아연", "round": "R11", "loop": "11", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "fine_archetype_id": "GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP_VS_DURABLE_VALUE_UNLOCK", "case_type": "4B_overlay_success", "positive_or_counterexample": "positive", "best_trigger": "TR_C32_010130_STAGE2_2024-09-13", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "large_positive_event_premium_but_not_durable_stage3", "current_profile_verdict": "current_profile_too_early", "price_source": "Songdaiki/stock-web", "notes": "Control battle/tender evidence created extreme MFE, but the subsequent drawdown shows it should be modeled as control-premium overlay, not durable Stage3 Green."}
{"row_type": "case", "case_id": "R11L11_C32_041510_SM_2023_TENDER_EVENT_CAP", "symbol": "041510", "company_name": "에스엠", "round": "R11", "loop": "11", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "fine_archetype_id": "GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP_VS_DURABLE_VALUE_UNLOCK", "case_type": "failed_rerating", "positive_or_counterexample": "counterexample", "best_trigger": "TR_C32_041510_STAGE2_2023-02-10", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "failed_durable_rerating_event_cap", "current_profile_verdict": "current_profile_false_positive", "price_source": "Songdaiki/stock-web", "notes": "Tender/control premium monetized quickly, but the price path capped and reversed; durable rerating label would be false."}
{"row_type": "case", "case_id": "R11L11_C32_000240_HANKOOKANDCOMPANY_2023_TENDER_FAIL", "symbol": "000240", "company_name": "한국앤컴퍼니", "round": "R11", "loop": "11", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "fine_archetype_id": "GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP_VS_DURABLE_VALUE_UNLOCK", "case_type": "false_positive_green", "positive_or_counterexample": "counterexample", "best_trigger": "TR_C32_000240_STAGE2_2023-12-05", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "false_positive_event_premium", "current_profile_verdict": "current_profile_false_positive", "price_source": "Songdaiki/stock-web", "notes": "Tender attempt triggered a gap-up, but the absence of cash conversion / board-control outcome made the move a sharp event-premium cap."}
{"row_type": "case", "case_id": "R11L11_C32_008930_HANMISCIENCE_2024_FAMILY_GOVERNANCE_DISPUTE", "symbol": "008930", "company_name": "한미사이언스", "round": "R11", "loop": "11", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "fine_archetype_id": "GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP_VS_DURABLE_VALUE_UNLOCK", "case_type": "false_positive_green", "positive_or_counterexample": "counterexample", "best_trigger": "TR_C32_008930_STAGE2_2024-01-15", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "false_positive_event_premium", "current_profile_verdict": "current_profile_false_positive", "price_source": "Songdaiki/stock-web", "notes": "Family/governance battle produced a fast repricing but failed to become a durable EPS/FCF rerating without transaction certainty."}
{"trigger_id": "TR_C32_000990_STAGE2_2023-03-08", "case_id": "R11L11_C32_000990_DBHITEK_2023_ACTIVIST_VALUE_UNLOCK", "symbol": "000990", "company_name": "DB하이텍", "trigger_type": "Stage2-Actionable", "trigger_date": "2023-03-08", "entry_date": "2023-03-08", "entry_price": 53000, "evidence_available_at_that_date": "activist / governance-discount narrative plus strong foundry earnings context available by trigger date", "evidence_source": "historical public activist-governance event summary; stock-web OHLC path: atlas/ohlcv_tradable_by_symbol_year/000/000990/2023.csv", "stage2_evidence_fields": ["public_event_or_disclosure", "relative_strength", "early_revision_signal"], "stage3_evidence_fields": ["margin_bridge", "financial_visibility", "multiple_public_sources"], "stage4b_evidence_fields": ["valuation_blowoff", "price_only_local_peak"], "stage4c_evidence_fields": [], "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/000/000990/2023.csv", "profile_path": "atlas/symbol_profiles/000/000990.json", "MFE_30D_pct": 57.74, "MFE_90D_pct": 57.74, "MFE_180D_pct": 57.74, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -15.28, "MAE_90D_pct": -15.28, "MAE_180D_pct": -15.28, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2023-04-04", "peak_price": 83600, "drawdown_after_peak_pct": -41.21, "green_lateness_ratio": "not_applicable_no_confirmed_Stage3_Green_trigger", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "not_4b_trigger", "four_b_evidence_type": [], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "positive_value_unlock_with_cashflow_bridge", "current_profile_verdict": "current_profile_missed_structural", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "GRP_C32_000990_2023-03-08_53000", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "row_type": "trigger", "round": "R11", "loop": "11", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "fine_archetype_id": "GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP_VS_DURABLE_VALUE_UNLOCK", "sector": "정책·지정학·재난·이벤트 / governance-control-premium overlay", "primary_archetype": "governance_control_premium_tender_cap", "loop_objective": "residual_false_positive_mining|residual_missed_structural_mining|sector_specific_rule_discovery|canonical_archetype_compression|4B_non_price_requirement_stress_test|4C_thesis_break_timing_test|coverage_gap_fill", "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20"}
{"trigger_id": "TR_C32_010130_STAGE2_2024-09-13", "case_id": "R11L11_C32_010130_KOREAZINC_2024_CONTROL_TENDER_BATTLE", "symbol": "010130", "company_name": "고려아연", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-09-13", "entry_date": "2024-09-13", "entry_price": 666000, "evidence_available_at_that_date": "hostile control/tender battle public event became tradable; cashflow evidence not yet the driver", "evidence_source": "historical tender/control-battle event summary; stock-web OHLC path: atlas/ohlcv_tradable_by_symbol_year/010/010130/2024.csv and 2025.csv", "stage2_evidence_fields": ["public_event_or_disclosure", "relative_strength", "policy_or_regulatory_optionality"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["valuation_blowoff", "positioning_overheat", "control_premium_or_event_premium"], "stage4c_evidence_fields": ["thesis_evidence_broken"], "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/010/010130/2024.csv", "profile_path": "atlas/symbol_profiles/010/010130.json", "MFE_30D_pct": 131.68, "MFE_90D_pct": 261.41, "MFE_180D_pct": 261.41, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -1.65, "MAE_90D_pct": -1.65, "MAE_180D_pct": -3.45, "MAE_1Y_pct": null, "below_entry_price_flag_30D": false, "below_entry_price_flag_90D": false, "peak_date": "2024-12-06", "peak_price": 2407000, "drawdown_after_peak_pct": -73.29, "green_lateness_ratio": "not_applicable_no_confirmed_Stage3_Green_trigger", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "not_full_4b_at_initial_event", "four_b_evidence_type": ["control_premium_or_event_premium"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "large_positive_event_premium_but_not_durable_stage3", "current_profile_verdict": "current_profile_too_early", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "GRP_C32_010130_2024-09-13_666000", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "row_type": "trigger", "round": "R11", "loop": "11", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "fine_archetype_id": "GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP_VS_DURABLE_VALUE_UNLOCK", "sector": "정책·지정학·재난·이벤트 / governance-control-premium overlay", "primary_archetype": "governance_control_premium_tender_cap", "loop_objective": "residual_false_positive_mining|residual_missed_structural_mining|sector_specific_rule_discovery|canonical_archetype_compression|4B_non_price_requirement_stress_test|4C_thesis_break_timing_test|coverage_gap_fill", "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20"}
{"trigger_id": "TR_C32_010130_4B_2024-12-05", "case_id": "R11L11_C32_010130_KOREAZINC_2024_CONTROL_TENDER_BATTLE", "symbol": "010130", "company_name": "고려아연", "trigger_type": "4B", "trigger_date": "2024-12-05", "entry_date": "2024-12-05", "entry_price": 2000000, "evidence_available_at_that_date": "control premium had become extreme; non-price evidence was control battle / tender escalation rather than EPS revision", "evidence_source": "stock-web OHLC path: atlas/ohlcv_tradable_by_symbol_year/010/010130/2024.csv and 2025.csv", "stage2_evidence_fields": ["public_event_or_disclosure", "relative_strength"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["valuation_blowoff", "positioning_overheat", "control_premium_or_event_premium"], "stage4c_evidence_fields": ["thesis_evidence_broken"], "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/010/010130/2024.csv", "profile_path": "atlas/symbol_profiles/010/010130.json", "MFE_30D_pct": 20.35, "MFE_90D_pct": 20.35, "MFE_180D_pct": 20.35, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -50.5, "MAE_90D_pct": -65.15, "MAE_180D_pct": -67.85, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-12-06", "peak_price": 2407000, "drawdown_after_peak_pct": -73.29, "green_lateness_ratio": "not_applicable_4B_overlay", "four_b_local_peak_proximity": 0.77, "four_b_full_window_peak_proximity": 0.77, "four_b_timing_verdict": "good_full_window_4B_timing", "four_b_evidence_type": ["valuation_blowoff", "positioning_overheat", "control_premium_or_event_premium"], "four_c_protection_label": "hard_4c_late", "trigger_outcome_label": "4B_overlay_success", "current_profile_verdict": "current_profile_4B_too_late", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "GRP_C32_010130_2024-12-05_2000000", "dedupe_for_aggregate": false, "aggregate_group_role": "4B_overlay_only", "is_new_independent_case": true, "reuse_reason": "same case different 4B overlay trigger", "independent_evidence_weight": 0.5, "do_not_count_as_new_case": true, "row_type": "trigger", "round": "R11", "loop": "11", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "fine_archetype_id": "GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP_VS_DURABLE_VALUE_UNLOCK", "sector": "정책·지정학·재난·이벤트 / governance-control-premium overlay", "primary_archetype": "governance_control_premium_tender_cap", "loop_objective": "residual_false_positive_mining|residual_missed_structural_mining|sector_specific_rule_discovery|canonical_archetype_compression|4B_non_price_requirement_stress_test|4C_thesis_break_timing_test|coverage_gap_fill", "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20"}
{"trigger_id": "TR_C32_041510_STAGE2_2023-02-10", "case_id": "R11L11_C32_041510_SM_2023_TENDER_EVENT_CAP", "symbol": "041510", "company_name": "에스엠", "trigger_type": "Stage2-Actionable", "trigger_date": "2023-02-10", "entry_date": "2023-02-10", "entry_price": 114700, "evidence_available_at_that_date": "tender/control premium evidence became tradable; durable earnings evidence was not the main driver", "evidence_source": "stock-web OHLC path: atlas/ohlcv_tradable_by_symbol_year/041/041510/2023.csv", "stage2_evidence_fields": ["public_event_or_disclosure", "relative_strength", "customer_or_order_quality"], "stage3_evidence_fields": ["multiple_public_sources"], "stage4b_evidence_fields": ["valuation_blowoff", "explicit_event_cap", "control_premium_or_event_premium"], "stage4c_evidence_fields": ["thesis_evidence_broken"], "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/041/041510/2023.csv", "profile_path": "atlas/symbol_profiles/041/041510.json", "MFE_30D_pct": 40.54, "MFE_90D_pct": 40.54, "MFE_180D_pct": 40.54, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -9.24, "MAE_90D_pct": -21.1, "MAE_180D_pct": -23.63, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2023-03-08", "peak_price": 161200, "drawdown_after_peak_pct": -45.66, "green_lateness_ratio": "not_applicable_no_confirmed_Stage3_Green_trigger", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "not_full_4b_at_initial_event", "four_b_evidence_type": ["control_premium_or_event_premium"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "failed_durable_rerating_event_cap", "current_profile_verdict": "current_profile_false_positive", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "GRP_C32_041510_2023-02-10_114700", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "row_type": "trigger", "round": "R11", "loop": "11", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "fine_archetype_id": "GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP_VS_DURABLE_VALUE_UNLOCK", "sector": "정책·지정학·재난·이벤트 / governance-control-premium overlay", "primary_archetype": "governance_control_premium_tender_cap", "loop_objective": "residual_false_positive_mining|residual_missed_structural_mining|sector_specific_rule_discovery|canonical_archetype_compression|4B_non_price_requirement_stress_test|4C_thesis_break_timing_test|coverage_gap_fill", "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20"}
{"trigger_id": "TR_C32_041510_4B_2023-03-08", "case_id": "R11L11_C32_041510_SM_2023_TENDER_EVENT_CAP", "symbol": "041510", "company_name": "에스엠", "trigger_type": "4B", "trigger_date": "2023-03-08", "entry_date": "2023-03-08", "entry_price": 158500, "evidence_available_at_that_date": "control premium had reached tender/event cap zone; price sat close to full observed peak", "evidence_source": "stock-web OHLC path: atlas/ohlcv_tradable_by_symbol_year/041/041510/2023.csv", "stage2_evidence_fields": ["public_event_or_disclosure", "relative_strength"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["valuation_blowoff", "explicit_event_cap", "control_premium_or_event_premium"], "stage4c_evidence_fields": ["thesis_evidence_broken"], "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/041/041510/2023.csv", "profile_path": "atlas/symbol_profiles/041/041510.json", "MFE_30D_pct": 1.7, "MFE_90D_pct": 1.7, "MFE_180D_pct": 1.7, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -42.52, "MAE_90D_pct": -44.73, "MAE_180D_pct": -44.73, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2023-03-08", "peak_price": 161200, "drawdown_after_peak_pct": -45.66, "green_lateness_ratio": "not_applicable_4B_overlay", "four_b_local_peak_proximity": 0.94, "four_b_full_window_peak_proximity": 0.94, "four_b_timing_verdict": "good_full_window_4B_timing", "four_b_evidence_type": ["valuation_blowoff", "explicit_event_cap", "control_premium_or_event_premium"], "four_c_protection_label": "hard_4c_success", "trigger_outcome_label": "4B_overlay_success", "current_profile_verdict": "current_profile_4B_too_late", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "GRP_C32_041510_2023-03-08_158500", "dedupe_for_aggregate": false, "aggregate_group_role": "4B_overlay_only", "is_new_independent_case": true, "reuse_reason": "same case different 4B overlay trigger", "independent_evidence_weight": 0.5, "do_not_count_as_new_case": true, "row_type": "trigger", "round": "R11", "loop": "11", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "fine_archetype_id": "GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP_VS_DURABLE_VALUE_UNLOCK", "sector": "정책·지정학·재난·이벤트 / governance-control-premium overlay", "primary_archetype": "governance_control_premium_tender_cap", "loop_objective": "residual_false_positive_mining|residual_missed_structural_mining|sector_specific_rule_discovery|canonical_archetype_compression|4B_non_price_requirement_stress_test|4C_thesis_break_timing_test|coverage_gap_fill", "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20"}
{"trigger_id": "TR_C32_000240_STAGE2_2023-12-05", "case_id": "R11L11_C32_000240_HANKOOKANDCOMPANY_2023_TENDER_FAIL", "symbol": "000240", "company_name": "한국앤컴퍼니", "trigger_type": "Stage2-Actionable", "trigger_date": "2023-12-05", "entry_date": "2023-12-05", "entry_price": 21850, "evidence_available_at_that_date": "public tender attempt created a control-premium gap; no durable earnings bridge at trigger date", "evidence_source": "stock-web OHLC path: atlas/ohlcv_tradable_by_symbol_year/000/000240/2023.csv and 2024.csv", "stage2_evidence_fields": ["public_event_or_disclosure", "relative_strength"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["explicit_event_cap", "control_premium_or_event_premium"], "stage4c_evidence_fields": ["thesis_evidence_broken"], "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/000/000240/2023.csv", "profile_path": "atlas/symbol_profiles/000/000240.json", "MFE_30D_pct": 8.7, "MFE_90D_pct": 8.7, "MFE_180D_pct": 8.7, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -31.67, "MAE_90D_pct": -32.04, "MAE_180D_pct": -33.18, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2023-12-07", "peak_price": 23750, "drawdown_after_peak_pct": -38.53, "green_lateness_ratio": "not_applicable_no_confirmed_Stage3_Green_trigger", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "price_only_local_4B_too_early_without_cash_conversion", "four_b_evidence_type": ["control_premium_or_event_premium"], "four_c_protection_label": "hard_4c_success", "trigger_outcome_label": "false_positive_event_premium", "current_profile_verdict": "current_profile_false_positive", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "GRP_C32_000240_2023-12-05_21850", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "row_type": "trigger", "round": "R11", "loop": "11", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "fine_archetype_id": "GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP_VS_DURABLE_VALUE_UNLOCK", "sector": "정책·지정학·재난·이벤트 / governance-control-premium overlay", "primary_archetype": "governance_control_premium_tender_cap", "loop_objective": "residual_false_positive_mining|residual_missed_structural_mining|sector_specific_rule_discovery|canonical_archetype_compression|4B_non_price_requirement_stress_test|4C_thesis_break_timing_test|coverage_gap_fill", "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20"}
{"trigger_id": "TR_C32_000240_4C_2023-12-15", "case_id": "R11L11_C32_000240_HANKOOKANDCOMPANY_2023_TENDER_FAIL", "symbol": "000240", "company_name": "한국앤컴퍼니", "trigger_type": "4C", "trigger_date": "2023-12-15", "entry_date": "2023-12-15", "entry_price": 15850, "evidence_available_at_that_date": "tender/control-premium thesis weakened; price collapsed below the event-zone support", "evidence_source": "stock-web OHLC path: atlas/ohlcv_tradable_by_symbol_year/000/000240/2023.csv and 2024.csv", "stage2_evidence_fields": ["public_event_or_disclosure"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["explicit_event_cap", "control_premium_or_event_premium"], "stage4c_evidence_fields": ["thesis_evidence_broken"], "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/000/000240/2023.csv", "profile_path": "atlas/symbol_profiles/000/000240.json", "MFE_30D_pct": 18.86, "MFE_90D_pct": 22.78, "MFE_180D_pct": 22.78, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -6.31, "MAE_90D_pct": -7.89, "MAE_180D_pct": -7.89, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-02-08", "peak_price": 19460, "drawdown_after_peak_pct": -24.97, "green_lateness_ratio": "not_applicable_4C_overlay", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "not_4b_trigger", "four_b_evidence_type": ["control_premium_or_event_premium"], "four_c_protection_label": "hard_4c_success", "trigger_outcome_label": "4C_success_after_tender_break", "current_profile_verdict": "current_profile_4C_too_late", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "GRP_C32_000240_2023-12-15_15850", "dedupe_for_aggregate": false, "aggregate_group_role": "4C_overlay_only", "is_new_independent_case": true, "reuse_reason": "same case different 4C overlay trigger", "independent_evidence_weight": 0.5, "do_not_count_as_new_case": true, "row_type": "trigger", "round": "R11", "loop": "11", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "fine_archetype_id": "GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP_VS_DURABLE_VALUE_UNLOCK", "sector": "정책·지정학·재난·이벤트 / governance-control-premium overlay", "primary_archetype": "governance_control_premium_tender_cap", "loop_objective": "residual_false_positive_mining|residual_missed_structural_mining|sector_specific_rule_discovery|canonical_archetype_compression|4B_non_price_requirement_stress_test|4C_thesis_break_timing_test|coverage_gap_fill", "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20"}
{"trigger_id": "TR_C32_008930_STAGE2_2024-01-15", "case_id": "R11L11_C32_008930_HANMISCIENCE_2024_FAMILY_GOVERNANCE_DISPUTE", "symbol": "008930", "company_name": "한미사이언스", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-01-15", "entry_date": "2024-01-15", "entry_price": 43300, "evidence_available_at_that_date": "family/governance transaction dispute became tradable; no clean cash conversion or durable ownership resolution at entry", "evidence_source": "stock-web OHLC path: atlas/ohlcv_tradable_by_symbol_year/008/008930/2024.csv", "stage2_evidence_fields": ["public_event_or_disclosure", "relative_strength", "policy_or_regulatory_optionality"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["control_premium_or_event_premium", "legal_or_regulatory_block"], "stage4c_evidence_fields": ["thesis_evidence_broken"], "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/008/008930/2024.csv", "profile_path": "atlas/symbol_profiles/008/008930.json", "MFE_30D_pct": 29.79, "MFE_90D_pct": 29.79, "MFE_180D_pct": 29.79, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -10.62, "MAE_90D_pct": -28.41, "MAE_180D_pct": -29.79, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-01-16", "peak_price": 56200, "drawdown_after_peak_pct": -44.84, "green_lateness_ratio": "not_applicable_no_confirmed_Stage3_Green_trigger", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "price_only_local_4B_too_early_without_resolution", "four_b_evidence_type": ["legal_or_regulatory_block", "control_premium_or_event_premium"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "false_positive_event_premium", "current_profile_verdict": "current_profile_false_positive", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "GRP_C32_008930_2024-01-15_43300", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "row_type": "trigger", "round": "R11", "loop": "11", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "fine_archetype_id": "GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP_VS_DURABLE_VALUE_UNLOCK", "sector": "정책·지정학·재난·이벤트 / governance-control-premium overlay", "primary_archetype": "governance_control_premium_tender_cap", "loop_objective": "residual_false_positive_mining|residual_missed_structural_mining|sector_specific_rule_discovery|canonical_archetype_compression|4B_non_price_requirement_stress_test|4C_thesis_break_timing_test|coverage_gap_fill", "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy_to_c32_shadow", "case_id": "R11L11_C32_000990_DBHITEK_2023_ACTIVIST_VALUE_UNLOCK", "trigger_id": "TR_C32_000990_STAGE2_2023-03-08", "symbol": "000990", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 75, "revision_score": 60, "relative_strength_score": 80, "customer_quality_score": 0, "policy_or_regulatory_score": 10, "valuation_repricing_score": 65, "execution_risk_score": 35, "legal_or_contract_risk_score": 20, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 72, "stage_label_before": "Stage2-Actionable", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 80, "revision_score": 65, "relative_strength_score": 75, "customer_quality_score": 0, "policy_or_regulatory_score": 10, "valuation_repricing_score": 70, "execution_risk_score": 30, "legal_or_contract_risk_score": 20, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 78, "stage_label_after": "Stage3-Yellow_C32_value_unlock_bridge", "changed_components": ["valuation_repricing_score", "execution_risk_score", "legal_or_contract_risk_score", "c32_cash_conversion_or_durable_value_unlock_required"], "component_delta_explanation": "C32 shadow profile caps event-only control premium unless cash conversion, tender certainty, or durable value-unlock/cashflow bridge is visible at trigger date.", "MFE_90D_pct": 57.74, "MAE_90D_pct": -15.28, "score_return_alignment_label": "positive_value_unlock_with_cashflow_bridge", "current_profile_verdict": "current_profile_missed_structural"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy_to_c32_shadow", "case_id": "R11L11_C32_010130_KOREAZINC_2024_CONTROL_TENDER_BATTLE", "trigger_id": "TR_C32_010130_STAGE2_2024-09-13", "symbol": "010130", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 20, "revision_score": 10, "relative_strength_score": 100, "customer_quality_score": 0, "policy_or_regulatory_score": 35, "valuation_repricing_score": 85, "execution_risk_score": 80, "legal_or_contract_risk_score": 65, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 79, "stage_label_before": "Stage3-Yellow_false_positive_risk", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 20, "revision_score": 10, "relative_strength_score": 100, "customer_quality_score": 0, "policy_or_regulatory_score": 35, "valuation_repricing_score": 60, "execution_risk_score": 90, "legal_or_contract_risk_score": 75, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 71, "stage_label_after": "Stage2-Event-Capped_plus_4B_watch", "changed_components": ["valuation_repricing_score", "execution_risk_score", "legal_or_contract_risk_score", "c32_cash_conversion_or_durable_value_unlock_required"], "component_delta_explanation": "C32 shadow profile caps event-only control premium unless cash conversion, tender certainty, or durable value-unlock/cashflow bridge is visible at trigger date.", "MFE_90D_pct": 261.41, "MAE_90D_pct": -1.65, "score_return_alignment_label": "large_positive_event_premium_but_not_durable_stage3", "current_profile_verdict": "current_profile_too_early"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy_to_c32_shadow", "case_id": "R11L11_C32_041510_SM_2023_TENDER_EVENT_CAP", "trigger_id": "TR_C32_041510_STAGE2_2023-02-10", "symbol": "041510", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 35, "revision_score": 30, "relative_strength_score": 95, "customer_quality_score": 55, "policy_or_regulatory_score": 20, "valuation_repricing_score": 80, "execution_risk_score": 65, "legal_or_contract_risk_score": 55, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 82, "stage_label_before": "Stage3-Yellow_false_positive_risk", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 35, "revision_score": 30, "relative_strength_score": 90, "customer_quality_score": 55, "policy_or_regulatory_score": 20, "valuation_repricing_score": 55, "execution_risk_score": 75, "legal_or_contract_risk_score": 65, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 72, "stage_label_after": "Stage2-Event-Capped_plus_4B_watch", "changed_components": ["valuation_repricing_score", "execution_risk_score", "legal_or_contract_risk_score", "c32_cash_conversion_or_durable_value_unlock_required"], "component_delta_explanation": "C32 shadow profile caps event-only control premium unless cash conversion, tender certainty, or durable value-unlock/cashflow bridge is visible at trigger date.", "MFE_90D_pct": 40.54, "MAE_90D_pct": -21.1, "score_return_alignment_label": "failed_durable_rerating_event_cap", "current_profile_verdict": "current_profile_false_positive"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy_to_c32_shadow", "case_id": "R11L11_C32_000240_HANKOOKANDCOMPANY_2023_TENDER_FAIL", "trigger_id": "TR_C32_000240_STAGE2_2023-12-05", "symbol": "000240", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 10, "revision_score": 5, "relative_strength_score": 85, "customer_quality_score": 0, "policy_or_regulatory_score": 15, "valuation_repricing_score": 55, "execution_risk_score": 80, "legal_or_contract_risk_score": 70, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 76, "stage_label_before": "Stage3-Yellow_false_positive_risk", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 10, "revision_score": 5, "relative_strength_score": 75, "customer_quality_score": 0, "policy_or_regulatory_score": 15, "valuation_repricing_score": 40, "execution_risk_score": 85, "legal_or_contract_risk_score": 85, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 58, "stage_label_after": "Stage1-Event-Only_or_4C-watch", "changed_components": ["valuation_repricing_score", "execution_risk_score", "legal_or_contract_risk_score", "c32_cash_conversion_or_durable_value_unlock_required"], "component_delta_explanation": "C32 shadow profile caps event-only control premium unless cash conversion, tender certainty, or durable value-unlock/cashflow bridge is visible at trigger date.", "MFE_90D_pct": 8.7, "MAE_90D_pct": -32.04, "score_return_alignment_label": "false_positive_event_premium", "current_profile_verdict": "current_profile_false_positive"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy_to_c32_shadow", "case_id": "R11L11_C32_008930_HANMISCIENCE_2024_FAMILY_GOVERNANCE_DISPUTE", "trigger_id": "TR_C32_008930_STAGE2_2024-01-15", "symbol": "008930", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 15, "revision_score": 5, "relative_strength_score": 90, "customer_quality_score": 0, "policy_or_regulatory_score": 30, "valuation_repricing_score": 65, "execution_risk_score": 70, "legal_or_contract_risk_score": 75, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 78, "stage_label_before": "Stage3-Yellow_false_positive_risk", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 15, "revision_score": 5, "relative_strength_score": 80, "customer_quality_score": 0, "policy_or_regulatory_score": 30, "valuation_repricing_score": 45, "execution_risk_score": 85, "legal_or_contract_risk_score": 85, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 60, "stage_label_after": "Stage2-Red_Event-Only", "changed_components": ["valuation_repricing_score", "execution_risk_score", "legal_or_contract_risk_score", "c32_cash_conversion_or_durable_value_unlock_required"], "component_delta_explanation": "C32 shadow profile caps event-only control premium unless cash conversion, tender certainty, or durable value-unlock/cashflow bridge is visible at trigger date.", "MFE_90D_pct": 29.79, "MAE_90D_pct": -28.41, "score_return_alignment_label": "false_positive_event_premium", "current_profile_verdict": "current_profile_false_positive"}
{"row_type": "residual_contribution", "round": "R11", "loop": "11", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP", "new_independent_case_count": 5, "reused_case_count": 0, "new_symbol_count": 5, "new_trigger_family_count": 4, "tested_existing_calibrated_axes": ["price_only_blowoff_blocks_positive_stage", "full_4b_requires_non_price_evidence", "hard_4c_thesis_break_routes_to_4c", "stage3_green_revision_min"], "residual_error_types_found": ["control_premium_event_misclassified_as_durable_rerating", "tender_without_cash_conversion_false_positive", "governance_dispute_peak_then_drawdown", "activist_value_unlock_requires_cashflow_bridge"], "loop_contribution_label": "canonical_archetype_rule_candidate", "do_not_propose_new_weight_delta": false}
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
next_round = R12_loop_10_or_R13_cross_archetype_holdout
suggested_scope = L10 cross-archetype holdout over C31/C32 event-premium, 4B/4C protection, and duplicate-low-value-loop rejection
```

## 28. Source Notes

Stock-web source files inspected for this loop:

```text
atlas/manifest.json
atlas/schema.json
atlas/symbol_profiles/000/000240.json
atlas/symbol_profiles/000/000990.json
atlas/symbol_profiles/008/008930.json
atlas/symbol_profiles/010/010130.json
atlas/symbol_profiles/041/041510.json
atlas/ohlcv_tradable_by_symbol_year/000/000240/2023.csv
atlas/ohlcv_tradable_by_symbol_year/000/000240/2024.csv
atlas/ohlcv_tradable_by_symbol_year/000/000990/2023.csv
atlas/ohlcv_tradable_by_symbol_year/008/008930/2024.csv
atlas/ohlcv_tradable_by_symbol_year/010/010130/2024.csv
atlas/ohlcv_tradable_by_symbol_year/010/010130/2025.csv
atlas/ohlcv_tradable_by_symbol_year/041/041510/2023.csv
```

Allowed stock_agent research artifacts checked only for coverage and duplicate avoidance:

```text
reports/e2r_calibration/ingest_summary.md
reports/e2r_calibration/applied_scoring_diff.md
```
